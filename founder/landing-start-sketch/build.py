# Эскизы первого экрана Nota для входа «Start → присылайте документы» (21.11.2026).
# Собирает три варианта (a.html, b.html, c.html) на стилях текущего лендинга (site.css — копия из nota/dist).
# Картинки и шрифты берутся с локального сервера nota/dist на :4321. Снимки — shots.js.
# Блок «Подключите Google» и всё ниже остаются как на текущем лендинге: здесь показано только начало.
import pathlib

HERE = pathlib.Path(__file__).parent
SRV = 'http://localhost:4321'
HEADER = (HERE / 'header.html').read_text().replace('src="/', f'src="{SRV}/')

CHECK = '<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
UNDER = '<svg class="mk-under" viewBox="0 0 200 16" preserveAspectRatio="none" aria-hidden="true"><path d="M3 13C50 11.5 120 8 197 4"/></svg>'


def u(word):
    return f'<span class="mk-u">{word}{UNDER}</span>'


# ---------- миниатюры документов ----------
RECEIPT = '''<div class="doc doc--receipt"><b>SUNRISE HARDWARE</b><i></i><i class="s"></i><i></i><em>TOTAL 582.500</em></div>'''
HAND = '''<div class="doc doc--hand"><span>Nota</span><span>Semen 10 sak</span><span>1.150.000</span></div>'''
TRANSFER = '''<div class="doc doc--bank"><b>Transfer berhasil</b><em>Rp 12.500.000</em><i></i><i class="s"></i></div>'''
ZIP = '''<div class="doc doc--zip"><b>ZIP</b><span>WhatsApp Chat — Proyek Villa.zip</span><small>48 МБ · 212 файлов</small></div>'''

FOOT = '<div class="foot">Запишу в таблицу, когда подключите Google · храню 7 дней</div>'


def bot(lines, foot=True, time='10:41', warn=False):
    cls = 'b-bot warn' if warn else 'b-bot'
    return f'<div class="{cls}">{lines}{FOOT if foot else ""}<span class="t">{time}</span></div>'


def me(doc, time='10:41'):
    return f'<div class="b-me">{doc}<span class="t">{time} ✓✓</span></div>'


R1 = bot('<div class="h">🧾 Чек · Sunrise Hardware</div><div class="sum">582 500 IDR</div><div class="m">2 ноя 2026 · Гвозди и саморезы · Материалы</div>', time='10:41')
R2 = bot('<div class="h">✍️ Накладная от руки · Toko Besi Jaya</div><div class="sum">1 150 000 IDR</div><div class="m">4 ноя 2026 · Цемент, 10 мешков · Материалы</div>', time='10:42')
R3 = bot('<div class="h">⚠️ Похоже на дубль</div><div class="m dark">Такой чек уже был: 582 500 IDR, Sunrise Hardware, 2 ноя. Отмечу его как дубль.</div>', foot=False, time='10:43', warn=True)
R1s = bot('<div class="h">🧾 Чек · Sunrise Hardware</div><div class="sum">582 500 IDR</div><div class="m">2 ноя 2026 · Материалы</div>', time='10:41')
R2s = bot('<div class="h">✍️ От руки · Toko Besi Jaya</div><div class="sum">1 150 000 IDR</div><div class="m">4 ноя 2026 · Цемент, 10 мешков</div>', time='10:42')
RZ = bot('<div class="h">📦 Архив получен: 212 файлов</div><div class="m dark">Разберу примерно за 15 минут и пришлю отчёт. Можно закрыть Telegram — напишу, когда будет готов.</div>', foot=False, time='10:45')


def chat(rows, cls='', title=True):
    head = '<div class="tg-top"><span class="ava">N</span><div><b>Nota</b><small>бот</small></div></div>' if title else ''
    return f'<div class="tg {cls}">{head}<div class="tg-body">{"".join(rows)}</div></div>'


def counter(n):
    return f'<div class="sys">Документ {n} из 30 бесплатных</div>'


def page(name, title, body):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&display=swap"><link rel="stylesheet" href="site.css"><link rel="stylesheet" href="mk.css"></head>
<body class="mk mk-{name}">{HEADER}<main class="tight v7 v8 v9 v10 v11">{body}</main></body></html>'''


HERO_LIST = ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in ['Чеки из магазинов, счета и инвойсы', 'Рукописные накладные, даже мятые', 'Скриншоты банковских переводов', 'PDF и фото, на любом языке'])
QR = f'<div class="cta-qr"><img src="{SRV}/screens/qr-bot-v10.svg" alt="" width="54" height="54"><span>Или камерой телефона</span></div>'
NOTE = '<p class="cta-line">30 документов бесплатно, без карты и регистрации. Google — когда захотите</p>'

REPORT_IMG = f'<figure class="mk-report"><img src="{SRV}/screens/report-archive-1080.webp" alt="Пример отчёта" width="1080" height="1238"><figcaption>Пример отчёта</figcaption></figure>'
POINTS = ''.join(f'<li>{CHECK}{t}</li>' for t in [
    'Сколько всего потрачено за период и сколько было платежей',
    'На что и кому ушли деньги: категории, главные поставщики, крупные платежи',
    'Где возможны дубли и ошибки в документах',
    'Сколько документов было написано от руки',
])


def sched(rows):
    return '<div class="sched"><div class="sched-title">Когда приходит отчёт</div><dl>' + ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in rows) + '</dl></div>'


SCHED = sched([('На 30-м документе', 'первый отчёт'), ('По архиву', 'за прошлые месяцы'), ('Каждый понедельник', 'за неделю'), ('1-го числа', 'за месяц'), ('В любое время', 'по кнопке «Отчёт»')])


def step(n, h2, inner, paper=False, extra=''):
    return f'''<section class="section mk-sec{' section--paper' if paper else ''} {extra}"><div class="wrap"><div class="mk-steprow"><span class="mk-n">{n}</span><div class="mk-stepbody"><h2>{h2}</h2>{inner}</div></div></div></section>'''


def table_teaser(n):
    return f'''<section class="section mk-sec mk-teaser"><div class="wrap"><div class="mk-steprow"><span class="mk-n">{n}</span><div class="mk-stepbody">
<h2>Подключите Google, и документы станут таблицей</h2>
<p class="lead">Nota создаст на вашем Google Диске таблицу и папку и перенесёт туда всё, что вы прислали. Дальше таблица ведётся сама.</p>
<div class="mk-fade"><img src="{SRV}/screens/payments.webp" alt=""></div>
</div></div>
<div class="mk-same">Дальше — как на текущем лендинге: таблица, как присылать, что делает Nota, для кого, цены, данные, вопросы</div>
</div></section>'''


# ---------- Вариант A: чат на первом экране ----------
a_hero = f'''<section class="hero mk-hero"><div class="wrap mk-split">
<div class="mk-left">
<span class="hero-eyebrow">Для тех, кому сотрудники присылают чеки</span>
<h1>Пришлите чек — {u("через минуту")} Nota скажет, что в нём</h1>
<p class="lead">Telegram-бот разберёт чеки, счета и накладные, найдёт дубли и запишет всё в вашу Google-таблицу.</p>
<ul class="hero-list">{HERO_LIST}</ul>
<div class="cta-row cta-row--qr"><a class="btn" href="#">Прислать первый чек</a>{QR}</div>
{NOTE}
</div>
<figure class="mk-chatfig">{chat([me(RECEIPT, '10:41'), R1, me(HAND, '10:42'), R2, me(RECEIPT, '10:43'), R3])}<figcaption>Так бот отвечает на каждый документ</figcaption></figure>
</div></section>'''

a_ways = step(2, 'Два способа начать', f'''<div class="mk-ways">
<div class="mk-way"><span class="tag tag--green">Сразу</span><h3>По одному документу</h3><p>Фото, PDF, скриншот перевода — пересылайте из любых чатов. На каждый документ бот ответит через минуту. Без Google он хранит документы 7 дней и запишет их в таблицу, когда вы её подключите.</p></div>
<div class="mk-way"><span class="tag tag--grey">За прошлые месяцы</span><h3>Архивом</h3><p>Выгрузите рабочий чат из Telegram или WhatsApp и пришлите ZIP. Бот разберёт всё сам и пришлёт отчёт: куда ушли деньги, дубли, ошибки в суммах. Около 15 минут — напишет, когда будет готов.</p></div>
</div>''', paper=True)

a_report = step(3, 'Отчёт приходит сам', f'''<div class="mk-repsplit"><div><p class="mk-sub">По одному чеку отчёт не нужен: он приходит, когда документов набралось.</p><ul class="check">{POINTS}</ul>{SCHED}</div>{REPORT_IMG}</div>''')

A = page('a', 'Вариант A — чат на первом экране', a_hero + a_ways + a_report + table_teaser(4))


# ---------- Вариант B: два пути прямо на первом экране ----------
b_hero = f'''<section class="hero mk-hero mk-hero--center"><div class="wrap">
<span class="hero-eyebrow">Для тех, кому сотрудники присылают чеки</span>
<h1>Учёт расходов {u("за минуту")}</h1>
<p class="lead">Нажмите Start в Telegram-боте Nota и присылайте документы. Или сразу весь архив рабочего чата.</p>
<div class="mk-paths">
<div class="mk-path"><span class="tag tag--green">Сразу</span><h3>Присылайте документы по одному</h3><p>Через минуту бот ответит, что в документе, и предупредит, если это дубль.</p>
{chat([me(RECEIPT, '10:41'), bot('<div class="h">🧾 Чек · Sunrise Hardware</div><div class="sum">582 500 IDR</div><div class="m">2 ноя 2026 · Материалы</div>'), me(RECEIPT, '10:43'), R3], cls='tg--mini', title=False)}
<a class="btn" href="#">Прислать чек</a></div>
<div class="mk-path"><span class="tag tag--grey">За прошлые месяцы</span><h3>Пришлите архив рабочего чата</h3><p>ZIP из Telegram или WhatsApp. Бот разберёт всё сам и пришлёт отчёт — около 15 минут.</p>
<div class="mk-repcrop"><img src="{SRV}/screens/report-archive-1080.webp" alt=""></div>
<a class="btn btn--dark mk-btn-out" href="#">Прислать архив</a></div>
</div>
<div class="mk-under-paths">{QR}<p class="cta-line">30 документов бесплатно, без карты и регистрации. Google — когда захотите</p></div>
</div></section>'''

b_replies = step(2, 'Что бот отвечает на каждый документ', f'''<div class="mk-three">
<div class="mk-r"><div class="mk-r-l">Чек</div>{chat([me(RECEIPT, '10:41'), bot('<div class="h">🧾 Sunrise Hardware</div><div class="sum">582 500 IDR</div><div class="m">2 ноя · Материалы</div>', foot=False)], cls='tg--mini', title=False)}</div>
<div class="mk-r"><div class="mk-r-l">Накладная от руки</div>{chat([me(HAND, '10:42'), bot('<div class="h">✍️ Toko Besi Jaya</div><div class="sum">1 150 000 IDR</div><div class="m">4 ноя · Цемент, 10 мешков</div>', foot=False, time='10:42')], cls='tg--mini', title=False)}</div>
<div class="mk-r"><div class="mk-r-l">Скриншот перевода</div>{chat([me(TRANSFER, '10:44'), bot('<div class="h">🏦 Перевод · CV Bangun Bali</div><div class="sum">12 500 000 IDR</div><div class="m">1 ноя · Подрядчики</div>', foot=False, time='10:44')], cls='tg--mini', title=False)}</div>
</div>
<p class="mk-sub mk-sub--after">Без Google бот хранит документы 7 дней и запишет их в таблицу, когда вы её подключите.</p>''', paper=True)

b_report = step(3, 'Отчёт приходит сам', f'''<div class="mk-repsplit"><div><ul class="check">{POINTS}</ul>{SCHED}</div>{REPORT_IMG}</div>''')

B = page('b', 'Вариант B — два пути на первом экране', b_hero + b_replies + b_report + table_teaser(4))


# ---------- Вариант C: лента от первого чека до отчёта ----------
c_hero = f'''<section class="hero mk-hero"><div class="wrap mk-split mk-split--phone">
<div class="mk-left">
<span class="hero-eyebrow">Для тех, кому сотрудники присылают чеки</span>
<h1>Учёт расходов начинается с {u("одного чека")}</h1>
<p class="lead">Нажмите Start и пришлите чек: через минуту Nota скажет, что в нём. Пришлите его ещё раз — увидите, как бот находит дубли.</p>
<div class="cta-row cta-row--qr"><a class="btn" href="#">Попробовать на своём чеке</a>{QR}</div>
{NOTE}
</div>
<div class="mk-phone">{chat([me(RECEIPT, '10:41'), R1s, me(HAND, '10:42'), R2s, me(RECEIPT, '10:43'), R3])}</div>
</div></section>'''

STOPS = [
    ('Минута 1', 'Start и первый чек', 'Бот отвечает: сумма, поставщик, категория.'),
    ('Чеки 2, 3, 4…', 'Проверьте на дубле', 'Пришлите тот же чек ещё раз — бот скажет, что такой уже был.'),
    ('30-й документ', 'Первый отчёт', 'Куда ушли деньги, дубли, ошибки в суммах.'),
    ('Понедельник', 'Отчёт за неделю', 'Дальше сам: каждую неделю и 1-го числа за месяц.'),
    ('Когда удобно', 'Архив за прошлые месяцы', 'ZIP рабочего чата — отчёт по всему, что было до бота.'),
]
c_line = step(2, 'Как это идёт', '<ol class="mk-line">' + ''.join(f'<li class="{"alt" if i == 4 else ""}"><span class="dot"></span><small>{a}</small><b>{b}</b><p>{c}</p></li>' for i, (a, b, c) in enumerate(STOPS)) + '</ol>'
              + f'<div class="mk-repsplit mk-repsplit--c"><div><h3 class="mk-h3">Что покажет отчёт</h3><ul class="check">{POINTS}</ul><p class="mk-sub mk-sub--after">Google подключите, когда захотите: без него бот хранит документы 7 дней.</p></div>{REPORT_IMG}</div>', paper=True)

C = page('c', 'Вариант C — лента от первого чека до отчёта', c_hero + c_line + table_teaser(3))

for name, html in (('a', A), ('b', B), ('c', C)):
    (HERE / f'{name}.html').write_text(html)
print('ok')
