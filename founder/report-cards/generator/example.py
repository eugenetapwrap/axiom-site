# Пример: четыре формата карточек на выдуманных данных — архив, первые 30 документов, неделя, месяц.
#   python3 example.py          → out/ru-IDR/*.png (2160 px по ширине, как в боте)
#   python3 example.py --all    → все языки и валюты: out/<язык>-<валюта>/*.png
#   python3 example.py --all --scale 1 → то же в 1080 px (так сделаны картинки в ../examples/)
# Для рендера нужен Node.js с Playwright (см. render.cjs). Данные выдуманные, совпадения случайны.
import os, sys, random, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cards as C

D = dt.date
# Категории — как в листе Payments, на языке таблицы клиента; генератор их не переводит.
CATS = {'ru': ['Материалы', 'Подрядчики', 'Расходники', 'Топливо', 'Инструменты', 'Ремонт'],
        'en': ['Materials', 'Contractors', 'Supplies', 'Fuel', 'Tools', 'Repairs'],
        'id': ['Material', 'Kontraktor', 'Bahan habis pakai', 'Bahan bakar', 'Peralatan', 'Perbaikan']}
ACC = {'ru': 'Андрей Соколов', 'en': 'Daniel Brooks', 'id': 'Budi Santoso'}
PAYEES = ['Toko Contoh Jaya', 'CV Karya Mandiri', 'UD Sumber Air', 'Bengkel Sinar', 'PT Abadi Contoh', 'Toko Besi Makmur', '']
RATE = {'IDR': 1, 'VND': 1.6, 'RUB': 1 / 195, 'THB': 1 / 470, 'USD': 1 / 16300, 'EUR': 1 / 17600, 'SGD': 1 / 12300}   # из IDR, примерно
COMBOS = [('ru', 'IDR'), ('en', 'USD'), ('id', 'IDR'), ('ru', 'RUB'), ('en', 'EUR'), ('id', 'VND'), ('ru', 'THB'), ('en', 'SGD')]

def money(idr, cur):
    v = idr * RATE[cur]
    return round(v, -3) if cur in ('IDR', 'VND') else (round(v) if cur in ('RUB', 'THB') else round(v, 2))

def build(loc='ru', cur='IDR', seed=7):
    """Клиент подключился 14 сентября 2026; первые 30 документов набрались в конце сентября; дальше тариф."""
    rnd = random.Random(seed); cats = CATS[loc] + ['']
    def row(d):
        return dict(date=d, amount=money(rnd.choice([65, 120, 180, 250, 340, 480, 750, 1100, 1650, 2400, 3800]) * 1000, cur),
                    payee=rnd.choice(PAYEES), cat=rnd.choice(cats), check=rnd.choice(['OK'] * 14 + ['Review']), status='',
                    type=rnd.choice(['Receipt'] * 5 + ['Invoice', 'Hand']))
    rows, d = [], D(2026, 9, 14)
    while d <= D(2026, 11, 15):
        rows += [row(d) for _ in range(rnd.choice([0, 1, 2, 2, 3, 4]))]; d += dt.timedelta(days=1)
    for i in range(9, len(rows), 37):                      # дубль — копия предыдущей строки
        rows[i].update(check='DBL', amount=rows[i - 1]['amount'], payee=rows[i - 1]['payee'], cat=rows[i - 1]['cat'])
    for i in range(23, len(rows), 53): rows[i].update(status='Rejected')
    big = [i for i in range(len(rows)) if rows[i]['date'].day in (5, 13)][:6]
    for i in big: rows[i].update(amount=money(rnd.choice([6200, 7400, 9800]) * 1000, cur), payee='CV Karya Mandiri', cat=CATS[loc][1], type='Invoice')
    archive = []                                            # архив рабочего чата за август — до подключения
    d = D(2026, 8, 1)
    while d <= D(2026, 8, 31):
        archive += [row(d) for _ in range(rnd.choice([0, 1, 2]))]; d += dt.timedelta(days=1)
    archive[4].update(check='DBL', amount=archive[3]['amount'], payee=archive[3]['payee'], cat=archive[3]['cat'])
    archive[11].update(status='Rejected')
    return rows, archive

def cards_for(loc='ru', cur='IDR'):
    rows, archive = build(loc, cur); acc = ACC[loc]
    by = lambda a, b: [r for r in rows if a <= r['date'] <= b]
    return {
        'archive': C.archive_card(archive, acc, 'chat_export_august.zip', D(2026, 9, 14), loc=loc, cur=cur),
        'first30': C.first30_card(rows[:30], acc, loc=loc, cur=cur),
        'week': C.period_card(rows, D(2026, 11, 9), D(2026, 11, 15), 'week', acc, loc=loc, cur=cur, prev_rows=by(D(2026, 11, 2), D(2026, 11, 8))),
        'month': C.period_card(rows, D(2026, 10, 1), D(2026, 10, 31), 'month', acc, loc=loc, cur=cur, prev_rows=by(D(2026, 9, 1), D(2026, 9, 30)),
                               client_start=D(2026, 9, 14)),
    }

if __name__ == '__main__':
    combos = COMBOS if '--all' in sys.argv else COMBOS[:1]
    scale = sys.argv[sys.argv.index('--scale') + 1] if '--scale' in sys.argv else '2'
    for loc, cur in combos:
        out = os.path.join(HERE, 'out', f'{loc}-{cur}'); os.makedirs(out, exist_ok=True)
        for name, html in cards_for(loc, cur).items():
            if html is None: print(loc, cur, name, '— нет расходов, вместо карточки сообщение'); continue
            path = os.path.join(out, name + '.html'); open(path, 'w').write(html)
            subprocess.run(['node', os.path.join(HERE, 'render.cjs'), path, path[:-5] + '.png', scale], check=True)
