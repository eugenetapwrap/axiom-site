# Генератор карточек отчётов Nota v2: архив, неделя, месяц; языки ru / en / id; валюты IDR, VND, RUB, USD, EUR и др.
# Шаблоны — утверждённые карточки (archive.html, week.html); статичные части остаются, динамические пересобираются.
import os, re, datetime as dt

TPL_DIR = os.environ.get('NOTA_TPL_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def _tpl(name):
    s = open(os.path.join(TPL_DIR, name)).read()
    s = s.replace('width: 1080px; height: 1350px;', 'width: 1080px; height: auto;')          # высота по содержимому
    s = s.replace('display: grid; grid-template-columns: 1fr 2px 1fr; column-gap: 32px',
                  'display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px')
    s = s.replace('<div style="flex: 1 0 24px; max-height: 96px"></div>', '<div style="flex: 1 0 24px"></div>')
    return s

TEAL = '#0E5A52'; ORANGE = '#E8501C'; GREEN = '#0C7A4F'; MUTED = '#56635D'; GRAY = '#8A958F'; INK = '#14201B'
HSTY = 'font-size: 19px; font-weight: 700; letter-spacing: 0.08em; color: #334154'

# ---------------- валюты ----------------
# scale — делитель для коротких сумм (млн / тыс. / как есть); full_dec — знаков после запятой у полных сумм.
CUR = {
    'IDR': dict(scale=1e6, unit={'ru': 'млн', 'en': 'M', 'id': 'jt'}, full_dec=0),
    'VND': dict(scale=1e6, unit={'ru': 'млн', 'en': 'M', 'id': 'jt'}, full_dec=0),
    'RUB': dict(scale=1e3, unit={'ru': 'тыс.', 'en': 'K', 'id': 'rb'}, full_dec=0),
    'THB': dict(scale=1e3, unit={'ru': 'тыс.', 'en': 'K', 'id': 'rb'}, full_dec=0),
    'USD': dict(scale=1, unit={'ru': '', 'en': '', 'id': ''}, full_dec=2),
    'EUR': dict(scale=1, unit={'ru': '', 'en': '', 'id': ''}, full_dec=2),
    'SGD': dict(scale=1, unit={'ru': '', 'en': '', 'id': ''}, full_dec=2),
}

# ---------------- числа ----------------
SEP = {'ru': (' ', ','), 'en': (',', '.'), 'id': ('.', ',')}
def _group(intpart, loc, html=True, gap='0.33em'):
    s = f'{intpart:,}'.split(',')
    if loc == 'ru':
        return (f'<span style="display: inline-block; width: {gap}"></span>' if html else ' ').join(s)
    return SEP[loc][0].join(s)
def num(v, loc, dec=2, gap='0.24em'):
    """Число с разделителями языка: 1 230,45 / 1,230.45 / 1.230,45."""
    neg = v < 0; v = abs(v)
    q = round(v, dec); i = int(q); d = f'{q:.{dec}f}'.split('.')[1] if dec else ''
    s = _group(i, loc, gap=gap) + ((SEP[loc][1] + d) if dec else '')
    return ('−' if neg else '') + s
def short(v, loc, cur):
    """Сумма в единицах валюты (млн / тыс. / как есть), 2 знака; меньше 0,005 — «<0,01»."""
    x = v / CUR[cur]['scale']
    if 0 < abs(x) < 0.005: return '&lt;0' + SEP[loc][1] + '01'
    return num(x, loc)
def full(v, loc, cur):
    return num(v, loc, dec=CUR[cur]['full_dec'], gap='0.33em')
def big_span(v, loc, cur):
    x = v / CUR[cur]['scale']; n = len(str(int(abs(x))))
    fs, dc = (120, 72) if n <= 4 else ((100, 60) if n == 5 else ((84, 50) if n == 6 else (72, 44)))
    q = f'{x:.2f}'; i, d = q.split('.')
    body = _group(int(i), loc, gap='0.3em') + f'<span style="font-size: {dc}px">{SEP[loc][1]}{d}</span>'
    return f'<span style="font-size: {fs}px; font-weight: 700; line-height: 1; letter-spacing: 0.025em; color: {INK}; white-space: nowrap">{body}</span>'

# ---------------- тексты ----------------
def plural_ru(n, a, b, c):
    n = abs(n)
    if n % 10 == 1 and n % 100 != 11: return a
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return b
    return c
MON = {'ru': ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'],
       'en': ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
       'id': ['', 'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']}
MON_FULL = {'ru': ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'],
            'en': ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            'id': ['', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']}
MON_DAT_RU = ['', 'январю', 'февралю', 'марту', 'апрелю', 'маю', 'июню', 'июлю', 'августу', 'сентябрю', 'октябрю', 'ноябрю', 'декабрю']
WD = {'ru': ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'], 'en': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 'id': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min']}
CAT_NAMES = {   # ключи — как в таблице (столбец Category)
    'Materials': {'ru': 'Материалы', 'en': 'Materials', 'id': 'Material'},
    'Supplies': {'ru': 'Расходники', 'en': 'Supplies', 'id': 'Perlengkapan'},
    'Staff': {'ru': 'Зарплаты', 'en': 'Payroll', 'id': 'Gaji'},
    'Repairs': {'ru': 'Ремонт', 'en': 'Repairs', 'id': 'Perbaikan'},
    'Fuel': {'ru': 'Топливо', 'en': 'Fuel', 'id': 'BBM'},
    'Transport': {'ru': 'Транспорт', 'en': 'Transport', 'id': 'Transportasi'},
    'Contractors': {'ru': 'Подрядчики', 'en': 'Contractors', 'id': 'Kontraktor'},
    'Other': {'ru': 'Прочее', 'en': 'Other', 'id': 'Lainnya'},
}
def cat_name(key, loc): return CAT_NAMES.get(key, {}).get(loc, key)

def date_short(d, loc):              # 12 ноя / Nov 12 / 12 Nov
    return f'{MON[loc][d.month]} {d.day}' if loc == 'en' else f'{d.day} {MON[loc][d.month]}'
def date_wd(d, loc):                 # ср, 11.11 / Wed, Nov 11 / Rab, 11.11
    return f'{WD[loc][d.weekday()]}, {MON[loc][d.month]} {d.day}' if loc == 'en' else f'{WD[loc][d.weekday()]}, {d.day:02d}.{d.month:02d}'
def span_label(a, b, loc):
    M = MON[loc]
    if loc == 'en':
        if a == b: return f'{M[a.month]} {a.day}, {a.year}'
        if (a.month, a.year) == (b.month, b.year): return f'{M[a.month]} {a.day}–{b.day}, {b.year}'
        if a.year == b.year: return f'{M[a.month]} {a.day} – {M[b.month]} {b.day}, {b.year}'
        return f'{M[a.month]} {a.day}, {a.year} – {M[b.month]} {b.day}, {b.year}'
    if a == b: return f'{a.day} {M[a.month]} {a.year}'
    if (a.month, a.year) == (b.month, b.year): return f'{a.day}–{b.day} {M[b.month]} {b.year}'
    if a.year == b.year: return f'{a.day} {M[a.month]} – {b.day} {M[b.month]} {b.year}'
    return f'{a.day} {M[a.month]} {a.year} – {b.day} {M[b.month]} {b.year}'

T = {
 'ru': dict(
   week_label=lambda s: f'Расходы за неделю · {s}', month_label=lambda m, y: f'Расходы за месяц · {MON_FULL["ru"][m]} {y}',
   arch_label=lambda per, d: f'Расходы за {per} · архив получен {d}', since=lambda d: f'данные с {d}',
   avg='в среднем за день',
   cmp_week='к прошлой неделе', cmp_month=lambda m: f'к {MON_DAT_RU[m]}',
   docs=lambda n: f'{plural_ru(n,"документ","документа","документов")}<br>{plural_ru(n,"учтён","учтено","учтено")}',
   review=lambda n: f'{n} {plural_ru(n,"документ","документа","документов")}<br>{plural_ru(n,"ожидает","ожидают","ожидают")} проверки',
   dup=lambda n: f'{n} {plural_ru(n,"дубль","дубля","дублей")}<br>{plural_ru(n,"исключён","исключено","исключено")}',
   dup_tile=lambda n: f'{n} {plural_ru(n,"дубль","дубля","дублей")}<br>{plural_ru(n,"исключён","исключено","исключено")}',
   review_tile=lambda n: f'{n} {plural_ru(n,"документ","документа","документов")}<br>стоит проверить',
   hand_tile=lambda n: f'{n} {plural_ru(n,"рукописный","рукописных","рукописных")}<br>{plural_ru(n,"прочитан","прочитано","прочитано")}',
   no_review='Документов<br>для проверки нет', no_dup='Дублей<br>не найдено', no_hand='Рукописных<br>нет',
   payments=lambda n: f'{n} {plural_ru(n,"платёж","платежа","платежей")}', files=lambda n: f'из {n} {"файла" if (n%10==1 and n%100!=11) else "файлов"}',
   rejected=lambda n: f'Не вошли в расчёт: {n} {plural_ru(n,"отклонённый документ","отклонённых документа","отклонённых документов")}',
   h_day='ПО ДНЯМ', h_pay='КРУПНЕЙШИЕ ПЛАТЕЖИ', h_cat='КАТЕГОРИИ', h_sup='ПОСТАВЩИКИ', legend='без категории',
   uncat='Без категории', nosup='Не указан', nosup_pay='Поставщик не указан', others=lambda n: f'Остальные {n}',
   footer='Подготовлено в Nota · контроль расходов в Telegram · '),
 'en': dict(
   week_label=lambda s: f'Weekly expenses · {s}', month_label=lambda m, y: f'Monthly expenses · {MON_FULL["en"][m]} {y}',
   arch_label=lambda per, d: f'Expenses for {per} · archive received {d}', since=lambda d: f'data from {d}',
   avg='average per day',
   cmp_week='vs last week', cmp_month=lambda m: f'vs {MON_FULL["en"][m]}',
   docs=lambda n: f'{"document" if n==1 else "documents"}<br>counted',
   review=lambda n: f'{n} {"document" if n==1 else "documents"}<br>awaiting review',
   dup=lambda n: f'{n} {"duplicate" if n==1 else "duplicates"}<br>excluded',
   dup_tile=lambda n: f'{n} {"duplicate" if n==1 else "duplicates"}<br>excluded',
   review_tile=lambda n: f'{n} {"document" if n==1 else "documents"}<br>to review',
   hand_tile=lambda n: f'{n} handwritten<br>{"document" if n==1 else "documents"} read',
   no_review='No documents<br>to review', no_dup='No duplicates<br>found', no_hand='No handwritten<br>documents',
   payments=lambda n: f'{n} {"payment" if n==1 else "payments"}', files=lambda n: f'from {n} {"file" if n==1 else "files"}',
   rejected=lambda n: f'Not counted: {n} rejected {"document" if n==1 else "documents"}',
   h_day='BY DAY', h_pay='LARGEST PAYMENTS', h_cat='CATEGORIES', h_sup='SUPPLIERS', legend='uncategorized',
   uncat='Uncategorized', nosup='Not specified', nosup_pay='Supplier not specified', others=lambda n: f'Other {n}',
   footer='Made with Nota · expense tracking in Telegram · '),
 'id': dict(
   week_label=lambda s: f'Pengeluaran mingguan · {s}', month_label=lambda m, y: f'Pengeluaran bulanan · {MON_FULL["id"][m]} {y}',
   arch_label=lambda per, d: f'Pengeluaran {per} · arsip diterima {d}', since=lambda d: f'data sejak {d}',
   avg='rata-rata per hari',
   cmp_week='dari minggu lalu', cmp_month=lambda m: f'dari {MON_FULL["id"][m]}',
   docs=lambda n: 'dokumen<br>tercatat',
   review=lambda n: f'{n} dokumen<br>menunggu dicek',
   dup=lambda n: f'{n} duplikat<br>dikecualikan',
   dup_tile=lambda n: f'{n} duplikat<br>dikecualikan',
   review_tile=lambda n: f'{n} dokumen<br>perlu dicek',
   hand_tile=lambda n: f'{n} tulisan tangan<br>terbaca',
   no_review='Tidak ada dokumen<br>untuk dicek', no_dup='Tidak ada<br>duplikat', no_hand='Tidak ada<br>tulisan tangan',
   payments=lambda n: f'{n} pembayaran', files=lambda n: f'dari {n} file',
   rejected=lambda n: f'Tidak dihitung: {n} dokumen ditolak',
   h_day='PER HARI', h_pay='PEMBAYARAN TERBESAR', h_cat='KATEGORI', h_sup='PEMASOK', legend='tanpa kategori',
   uncat='Tanpa kategori', nosup='Tidak diketahui', nosup_pay='Pemasok tidak diketahui', others=lambda n: f'Lainnya {n}',
   footer='Dibuat dengan Nota · pencatatan pengeluaran di Telegram · '),
}

# ---------------- данные ----------------
def classify(rows):
    """inc — входят в расходы; dbl — дубли; rev — на проверке (входят); rej — отклонённые и неплатёжные."""
    inc = [r for r in rows if r['amount'] > 0 and r['status'] != 'Rejected' and r['check'] != 'DBL' and r['type'] not in ('Statement', 'Proof')]
    dbl = [r for r in rows if r['check'] == 'DBL']
    rev = [r for r in inc if r['check'] == 'Review']
    rej = [r for r in rows if r not in inc and r not in dbl]
    return inc, dbl, rev, rej

def list_items(rows, key, max_rows):
    agg = {}
    for r in rows: agg[r[key]] = agg.get(r[key], 0) + r['amount']
    blank = agg.pop('', 0)
    named = sorted(agg.items(), key=lambda x: -x[1])
    slots = max_rows - (1 if blank else 0)
    if len(named) > slots:
        items = [(k, v, 'n') for k, v in named[:slots - 1]] + [(('__other__', len(named) - slots + 1), sum(v for _, v in named[slots - 1:]), 'o')]
    else:
        items = [(k, v, 'n') for k, v in named]
    if blank: items.append(('', blank, 'u' if key == 'cat' else 'm'))
    return items

def shares(items, tot):
    raw = [v / tot * 100 if tot else 0 for _, v, _ in items]; base = [int(x) for x in raw]
    for i in sorted(range(len(raw)), key=lambda i: -(raw[i] - base[i]))[:max(0, 100 - sum(base))]: base[i] += 1
    return [('&lt;1' if (b == 0 and r > 0) else str(b)) for b, r in zip(base, raw)]

def deltas(items, prev_inc, key, loc, cur):
    """Изменение к прошлому периоду в единицах валюты; цветом — только самый большой рост и самое большое снижение."""
    if prev_inc is None: return {}
    p = {}
    for r in prev_inc: p[r[key]] = p.get(r[key], 0) + r['amount']
    vals = {}
    for k, v, kind in items:
        if kind == 'o': continue
        d = v - p.get(k, 0)
        if abs(d / CUR[cur]['scale']) >= 0.005: vals[k] = d
    if not vals: return {}
    mx = max(vals.values()); mn = min(vals.values()); out = {}
    for k, d in vals.items():
        txt = ('+' if d > 0 else '') + short(d, loc, cur)
        out[k] = (txt, ORANGE if (d == mx and d > 0) else (GREEN if (d == mn and d < 0) else GRAY))
    return out

def block(src, start):
    a = src.find(start); assert a >= 0, start[:70]
    depth = 0
    for m in re.finditer(r'<div\b|</div>', src[a:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0: return a, a + m.end()

def _unit_html(loc, cur, color=MUTED, size=24):
    u = CUR[cur]['unit'][loc]
    return f'<span style="font-size: {size}px; font-weight: 500; color: {color}">{u}</span>' if u else ''
def _head(text, loc, cur):
    u = CUR[cur]['unit'][loc]
    return text + (f', <span style="font-weight: 600; color: {GRAY}">{u.upper()}</span>' if u else '')

def _lists(base, max_rows, loc, cur, archive, prev_inc=None, gap=10):
    L = T[loc]; tot = sum(r['amount'] for r in base)
    def name(k, kind, key):
        if kind == 'o': return L['others'](k[1])
        if kind in ('u', 'm'): return L['uncat'] if key == 'cat' else L['nosup']
        return cat_name(k, loc) if key == 'cat' else k
    def row(k, v, kind, key, pct, dl):
        u = kind == 'u'
        dot = f'<span style="display: inline-block; width: {12 if archive else 11}px; height: {12 if archive else 11}px; background: {ORANGE}; border-radius: 50%; margin-right: 10px; vertical-align: 2px"></span>' if u else ''
        dtx = f'<span style="margin-left: 10px; font-size: 20px; font-weight: 600; color: {dl[1]}">{dl[0]}</span>' if dl else ''
        cols = '1fr auto 64px' if archive else 'minmax(0, 1fr) auto 52px'
        return ('<div><div style="display: grid; grid-template-columns: ' + cols + '; column-gap: ' + ('12' if archive else '10') + 'px; align-items: baseline">'
          f'<span style="font-size: 24px; font-weight: {600 if u else 400}; color: {INK}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{dot}{name(k, kind, key)}{dtx}</span>'
          f'<span style="font-size: 24px; font-weight: {600 if u else 500}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{short(v, loc, cur)}</span>'
          f'<span style="font-size: {22 if archive else 20}px; color: {MUTED}; text-align: right; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{pct}%</span></div>'
          f'<div style="margin-top: 6px; height: 8px; border-radius: 4px; background: #EEF1EE"><div style="width: {v / tot * 100 if tot else 0:.1f}%; height: 8px; border-radius: 4px; background: {ORANGE if u else TEAL}"></div></div></div>')
    def col(title, key):
        items = list_items(base, key, max_rows); pc = shares(items, tot)
        dl = deltas(items, prev_inc, key, loc, cur) if key == 'cat' else {}
        h = f'<div style="display: flex; flex-direction: column; gap: {gap}px"><div style="{HSTY}; margin-bottom: 10px">{_head(title, loc, cur)}</div>'
        for (k, v, kind), p in zip(items, pc): h += row(k, v, kind, key, p, dl.get(k))
        return h + '</div>'
    return ('<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'
            + col(L['h_cat'], 'cat') + '<div style="background: #E2E7E3; align-self: stretch"></div>' + col(L['h_sup'], 'payee') + '</div>')

def _localize_static(s, loc, cur, acc):
    L = T[loc]
    s = s.replace('Подготовлено в Nota · контроль расходов в Telegram · ', L['footer'])
    s = s.replace('padding: 6px 16px">IDR</div>', f'padding: 6px 16px">{cur}</div>', 1)
    s = s.replace('<div style="font-size: 22px; font-weight: 600; color: #14201B; background: #EEF1EE; border-radius: 999px; padding: 6px 16px">Разобран</div>', '')
    s = s.replace('>КРУПНЕЙШИЕ ПЛАТЕЖИ<', f'>{L["h_pay"]}<')
    return s

def _footer_gap(s, px):
    i = s.find('@NotaGetBot'); a = s.rfind('<div style="', 0, i)
    return s[:a] + s[a:i].replace('<div style="', f'<div style="padding-top: {px}px; ', 1) + s[i:]

ZERO = lambda t: f'<div style="font-size: 24px; line-height: 28px; color: {GRAY}; padding-top: 10px">{t}</div>'

# ---------------- неделя и месяц ----------------
def period_card(rows, start, end, kind, acc, loc='ru', cur='IDR', prev_rows=None, report_date=None, client_start=None):
    """prev_rows=None — данных за прошлый период нет. report_date — день отправки (для среднего за день).
    client_start — день первого документа клиента (первый период)."""
    L = T[loc]
    rows = [r for r in rows if start <= r['date'] <= end]
    inc, dbl, rev, rej = classify(rows)
    tot = sum(r['amount'] for r in inc)
    if tot <= 0: return None                                   # пусто — вместо карточки сообщение «нет расходов»
    report_date = report_date or (end + dt.timedelta(days=1))   # плановый отчёт приходит после периода — делим на все дни
    d0 = max(start, client_start) if client_start else start
    d1 = min(end, report_date)                                  # отчёт по запросу: дни до сегодняшнего включительно
    days = max(1, (d1 - d0).days + 1)
    s = _localize_static(_tpl('week.html'), loc, cur, acc).replace('Андрей Соколов', acc, 1)
    lab = L['week_label'](span_label(start, end, loc)) if kind == 'week' else L['month_label'](start.month, start.year)
    if client_start and client_start > start: lab += ' · ' + L['since'](date_short(client_start, loc))
    s = s.replace('Расходы за неделю · 26 окт – 1 ноя 2026', lab, 1)
    # число, среднее, сравнение
    if prev_rows is None:
        cmp = ''                                                   # нет данных за прошлый период — ничего не пишем (17.11)
    else:
        ptot = sum(r['amount'] for r in classify(prev_rows)[0])
        if ptot > 0:
            dd = (tot - ptot) / ptot * 100; d = round(dd)
            ctxt = (('×' + str(round(dd / 100 + 1))) if dd / 100 + 1 < 99.5 else '×99+') if dd >= 200 else (('+' if d > 0 else ('−' if d < 0 else '')) + f'{abs(d)}%')
            u = CUR[cur]['unit'][loc]
            ref = L['cmp_week'] if kind == 'week' else L['cmp_month'](((start.replace(day=1) - dt.timedelta(days=1)).month))
            cmp = (f'<span style="margin-top: 6px; font-size: 22px; line-height: 28px; color: {MUTED}; white-space: nowrap; font-variant-numeric: tabular-nums">'
                   f'<span style="font-weight: 600; color: {INK}">{ctxt}</span> {ref} · {short(ptot, loc, cur)}{(" " + u) if u else ""}</span>')
        else: cmp = ''
    numrow = ('<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px">'
      f'<div style="display: flex; align-items: baseline; gap: 14px; white-space: nowrap">{big_span(tot, loc, cur)}{_unit_html(loc, cur, size=28)}</div>'
      '<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; padding-bottom: 8px">'
      f'<div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap"><span style="font-size: 44px; font-weight: 600; line-height: 48px; color: {INK}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{short(tot / days, loc, cur)}</span>{_unit_html(loc, cur)}</div>'
      f'<span style="font-size: 24px; line-height: 28px; color: {MUTED}">{L["avg"]}</span>{cmp}</div></div>')
    a, b = block(s, '<div style="display: flex; align-items: flex-end; justify-content: space-between">'); s = s[:a] + numrow + s[b:]
    # полоса
    bign = lambda v, c: f'<span style="font-size: 44px; font-weight: 600; line-height: 48px; color: {c}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{v}</span>'
    lab_ = lambda t, c: f'<div style="font-size: 24px; line-height: 28px; color: {c}; font-variant-numeric: tabular-nums">{t}</div>'
    cell = lambda st, inner: f'<div style="{st}display: flex; flex-direction: column; gap: 4px">{inner}</div>'
    row1 = lambda n_: f'<div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap">{n_}</div>'
    n = len(inc); rv = sum(r['amount'] for r in rev); dv = sum(r['amount'] for r in dbl)
    c1 = cell('padding: 12px 16px 12px 0; ', row1(bign(n, INK)) + lab_(L['docs'](n), MUTED))
    c2 = cell('border-left: 2px solid #E2E7E3; padding: 12px 16px 12px 24px; ', (row1(bign(short(rv, loc, cur), '#ED4E17') + _unit_html(loc, cur)) + lab_(L['review'](len(rev)), MUTED)) if rev else ZERO(L['no_review']))
    c3 = (cell('background: #EAF6F0; padding: 12px 16px 12px 24px; ', row1(bign(short(dv, loc, cur), GREEN) + _unit_html(loc, cur, GREEN)) + lab_(L['dup'](len(dbl)), GREEN)) if dbl
          else cell('border-left: 2px solid #E2E7E3; padding: 12px 16px 12px 24px; ', ZERO(L['no_dup'])))
    strip = '<div style="height: 136px; box-sizing: border-box; display: grid; grid-template-columns: 1fr 1fr 1fr; border-top: 2px solid #E2E7E3; border-bottom: 2px solid #E2E7E3">' + c1 + c2 + c3 + '</div>'
    a, b = block(s, '<div style="height: 136px; box-sizing: border-box; display: grid; grid-template-columns: 1fr 1fr 1fr;'); s = s[:a] + strip + s[b:]
    # график
    dates = [start + dt.timedelta(days=i) for i in range((end - start).days + 1)]
    per = {d: sum(r['amount'] for r in inc if r['date'] == d) for d in dates}
    unc = {d: sum(r['amount'] for r in inc if r['date'] == d and not r['cat']) for d in dates}
    mx = max(per.values()); cols = len(dates); gapc = 12 if kind == 'week' else 4; rad = 4 if kind == 'week' else 3
    bars = ''
    for d in dates:
        v = per[d]
        if v <= 0: bars += '<div style="display: flex; flex-direction: column; justify-content: flex-end; min-width: 0"></div>'; continue
        h = max(4, round(v / mx * 152)); top = round(unc[d] / v * h) if unc[d] else 0; hi = v == mx; body = TEAL if hi else '#C3DBD5'
        lbl = (f'<div style="display: flex; justify-content: center; height: 26px; margin-bottom: 6px; overflow: visible"><span style="font-size: 22px; font-weight: 600; line-height: 26px; color: {INK}; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{short(v, loc, cur)}</span></div>') if hi else ''
        seg = (f'<div style="height: {top}px; background: {ORANGE}; border-radius: {rad}px {rad}px 0 0"></div><div style="flex: 1; background: {body}; border-radius: 0"></div>') if top else f'<div style="flex: 1; background: {body}; border-radius: {rad}px {rad}px 0 0"></div>'
        bars += f'<div style="display: flex; flex-direction: column; justify-content: flex-end; min-width: 0">{lbl}<div style="height: {h}px; display: flex; flex-direction: column">{seg}</div></div>'
    labels = [WD[loc][d.weekday()] for d in dates] if kind == 'week' else [str(d.day) if (d.day - 1) % 7 == 0 else '' for d in dates]
    labs = ''.join(f'<div style="display: flex; justify-content: center; white-space: nowrap; font-size: 22px; line-height: 24px; color: {MUTED}">{l}</div>' for l in labels)
    chart = (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: grid; grid-template-columns: repeat({cols}, 1fr); column-gap: {gapc}px; height: 184px; align-items: end">{bars}</div>'
             f'<div style="display: grid; grid-template-columns: repeat({cols}, 1fr); column-gap: {gapc}px">{labs}</div></div>')
    h0 = s.find('ПО ДНЯМ'); a, b = block(s[h0:], '<div style="display: flex; flex-direction: column; gap: 8px">'); s = s[:h0 + a] + chart + s[h0 + b:]
    s = s.replace('ПО ДНЯМ, <span style="font-weight: 600; color: #8A958F">МЛН</span>', _head(L['h_day'], loc, cur), 1)
    leg = f'<div style="display: flex; align-items: center; gap: 8px; font-size: 22px; color: {MUTED}; white-space: nowrap"><span style="width: 14px; height: 14px; background: {ORANGE}; border-radius: 50%"></span>без категории</div>'
    s = s.replace(leg, leg.replace('без категории', L['legend']) if any(unc.values()) else '', 1)
    # крупнейшие платежи
    prow = ''
    for i, r in enumerate(sorted(inc, key=lambda r: -r['amount'])[:3]):
        bt = 'border-top: 2px solid #E2E7E3; ' if i else ''
        prow += (f'<div style="{bt}height: 72px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; gap: 2px"><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px">'
                 f'<span style="font-size: 24px; font-weight: 500; line-height: 32px; color: {INK}; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{full(r["amount"], loc, cur)}</span>'
                 f'<span style="font-size: 22px; color: {MUTED}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0">{r["payee"] or L["nosup_pay"]}</span></div>'
                 f'<div style="font-size: 22px; line-height: 28px; color: {MUTED}; white-space: nowrap">{date_wd(r["date"], loc)}</div></div>')
    h0 = s.find(L['h_pay']); a, b = block(s[h0:], '<div style="display: flex; flex-direction: column">'); s = s[:h0 + a] + '<div style="display: flex; flex-direction: column">' + prow + '</div>' + s[h0 + b:]
    # списки
    prev_inc = classify([r for r in prev_rows])[0] if prev_rows is not None else None
    g = _lists(inc, 8, loc, cur, archive=False, prev_inc=prev_inc)
    a, b = block(s, '<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'); s = s[:a] + g + s[b:]
    return _footer_gap(s, 56)

# ---------------- архив ----------------
def archive_card(rows, acc, fname, received, loc='ru', cur='IDR'):
    L = T[loc]
    inc, dbl, rev, rej = classify(rows)
    tot = sum(r['amount'] for r in inc)                          # итог без дублей (17.11)
    if tot <= 0: return None
    s = _localize_static(_tpl('archive.html'), loc, cur, acc)
    s = s.replace('>Андрей Соколов<', f'>{acc}<', 1).replace('>receipts_october.zip<', f'>{fname}<', 1)
    s = s.replace('<div style="flex: none; font-size: 28px; line-height: 1; font-weight: 600; color: #14201B; white-space: nowrap">',
                  '<div style="flex: 0 1 auto; max-width: 440px; min-width: 0; overflow: hidden; text-overflow: ellipsis; font-size: 28px; line-height: 1.2; font-weight: 600; color: #14201B; white-space: nowrap">', 1)
    s = s.replace('<div style="font-size: 28px; line-height: 1; font-weight: 400; color: #56635D; white-space: nowrap">',
                  '<div style="flex: 1 1 0; min-width: 0; overflow: hidden; text-overflow: ellipsis; font-size: 28px; line-height: 1.2; font-weight: 400; color: #56635D; white-space: nowrap">', 1)
    dates = [r['date'] for r in rows]
    s = s.replace('Расходы за 1–31 окт 2026 · архив получен 3 ноя', L['arch_label'](span_label(min(dates), max(dates), loc), date_short(received, loc)), 1)
    numrow = ('<div style="height: 120px; display: flex; align-items: flex-end; justify-content: space-between"><div style="display: flex; align-items: baseline; gap: 14px; white-space: nowrap">'
      f'{big_span(tot, loc, cur)}{_unit_html(loc, cur, size=28)}</div>'
      '<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; padding-bottom: 8px">'
      f'<span style="font-size: 44px; font-weight: 600; line-height: 48px; color: {INK}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{L["payments"](len(inc))}</span>'
      f'<span style="font-size: 24px; line-height: 28px; color: {MUTED}">{L["files"](len(rows))}</span></div></div>')
    a, b = block(s, '<div style="height: 120px; display: flex; align-items: flex-end; justify-content: space-between">'); s = s[:a] + numrow + s[b:]
    nl = 'Не вошли в расчёт: 2 неплатёжных документа и 1 нечитаемый файл'
    i = s.find(nl); a = s.rfind('<div', 0, i); b = s.find('</div>', i) + 6
    if rej: s = s[:a] + f'<div style="font-size: 24px; line-height: 30px; color: {MUTED}; font-variant-numeric: tabular-nums">{L["rejected"](len(rej))}</div>' + s[b:]
    else:
        sp = s.rfind('<div style="height: 12px; flex: none"></div>', 0, a); s = s[:sp] + s[b:]
    def tile(c, v, t):
        nlen = len(re.sub(r'<[^>]+>', '', v))
        fs = 48 if nlen <= 8 else (40 if nlen <= 10 else 34)
        return ('<div style="box-sizing: border-box; min-width: 0; padding: 20px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column; gap: 4px">'
            f'<div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap"><span style="font-size: {fs}px; font-weight: 700; line-height: 52px; color: {c}; font-variant-numeric: tabular-nums">{v}</span>{_unit_html(loc, cur)}</div>'
            f'<div style="font-size: 24px; line-height: 28px; min-height: 56px; color: {MUTED}">{t}</div></div>')
    ztile = lambda t: ('<div style="box-sizing: border-box; min-width: 0; padding: 20px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column; gap: 4px">'
                       f'<div style="font-size: 24px; line-height: 28px; color: {GRAY}; padding-top: 12px">{t}</div></div>')
    hand = [r for r in inc if r['type'] == 'Hand']
    t1 = tile(ORANGE, short(sum(r['amount'] for r in dbl), loc, cur), L['dup_tile'](len(dbl))) if dbl else ztile(L['no_dup'])
    t2 = tile(ORANGE, short(sum(r['amount'] for r in rev), loc, cur), L['review_tile'](len(rev))) if rev else ztile(L['no_review'])
    t3 = tile('#334154', short(sum(r['amount'] for r in hand), loc, cur), L['hand_tile'](len(hand))) if hand else ztile(L['no_hand'])
    a, b = block(s, '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">')
    s = s[:a] + '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">' + t1 + t2 + t3 + '</div>' + s[b:]
    g = _lists(inc, 7, loc, cur, archive=True)
    a, b = block(s, '<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'); s = s[:a] + g + s[b:]
    rows_ = ''
    for i, r in enumerate(sorted(inc, key=lambda r: -r['amount'])[:3]):
        bt = 'border-top: 2px solid #E2E7E3; ' if i else ''
        rows_ += (f'<div style="{bt}height: 56px; display: grid; grid-template-columns: minmax(190px, max-content) 110px minmax(0, 1fr) auto; column-gap: 20px; align-items: center">'
          f'<span style="font-size: 26px; font-weight: 600; color: {INK}; text-align: left; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{full(r["amount"], loc, cur)}</span>'
          f'<span style="font-size: 22px; color: {MUTED}; white-space: nowrap">{date_short(r["date"], loc)}</span>'
          f'<span style="font-size: 24px; color: {INK}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{r["payee"] or L["nosup_pay"]}</span>'
          f'<span style="font-size: 22px; color: {MUTED}; white-space: nowrap">{cat_name(r["cat"], loc) if r["cat"] else L["uncat"]}</span></div>')
    a, b = block(s, '<div style="box-sizing: border-box; padding: 4px 24px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column">')
    s = s[:a] + '<div style="box-sizing: border-box; padding: 4px 24px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column">' + rows_ + '</div>' + s[b:]
    s = s.replace('>Категории, <span', '>Категории, <span')  # no-op: заголовки списков пересобраны
    return _footer_gap(s, 32)
