# Пример отчёта за месяц для эскиза первого экрана (основатель, 21.11: «формат из ежемесячного отчёта, 25 дней из 30»).
#   python3 month-report.py → month-report.html и month-report.png (2160 px по ширине) в этой папке
# Карточку собирает генератор бота (../report-cards/generator/cards.py): отчёт по запросу за ноябрь на 25-е число,
# сравнение с 1–25 октября. Как в примере для сайта (report-cards/site-example.py), убрана нижняя строка «Подготовлено в Nota».
# Данные выдуманные: строительство вилл на Бали; поставщики — те же, что в примере архива и на скриншоте таблицы.
# Валюта — доллары (основатель, 21.11: «IDR может быть непонятно», итог около $11 тыс.): суммы в рупиях × RATE.
import os, sys, random, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, '..', 'report-cards', 'generator'); sys.path.insert(0, GEN)
import cards as C

CUR, RATE = 'USD', 1 / 9600      # итог месяца около $11 тыс.

# поставщик, категория, тип документа, типичные суммы (тыс. рупий)
SUP = [
    ('TB Sumber Rejeki', 'Материалы', 'Receipt', [1800, 2600, 3400, 4100, 6750]),
    ('Toko Besi Jaya', 'Материалы', 'Hand', [450, 900, 1150, 2270, 3900]),
    ('Sunrise Hardware', 'Материалы', 'Receipt', [138, 234, 582, 1200]),
    ('UD Sumber Air', 'Инструменты', 'Hand', [320, 980, 1520, 1780]),
    ('CV Bangun Bali', 'Подрядчики', 'Invoice', [3600, 4400, 5200, 8500]),
    ('Бригада Wayan', 'Зарплаты', 'Hand', [4800]),
    ('Bengkel Sinar', 'Топливо', 'Receipt', [310, 450, 520]),
    ('Island Electric', 'Электрика', 'Invoice', [1450, 3150]),
]

def build():
    rnd = random.Random(11); rows = []
    def add(d, s, amount=None, **kw):
        payee, cat, typ, amts = s
        usd = (amount or rnd.choice(amts)) * 1000 * RATE
        if CUR == 'USD':
            usd = round(usd / 5) * 5 if typ == 'Invoice' or payee == 'Бригада Wayan' else round(usd, 2)   # счета и зарплата — круглые
        else:   # рупии: счета и зарплата — до 50 тыс., чеки — до тысячи
            usd = round(usd / 50000) * 50000 if typ == 'Invoice' or payee == 'Бригада Wayan' else round(usd / 1000) * 1000
        rows.append(dict(date=d, amount=usd, payee=payee, cat=cat, type=typ, check='OK', status='', **kw))
    d = dt.date(2026, 10, 1)
    while d <= dt.date(2026, 11, 25):
        for _ in range(rnd.choice([0, 1, 2, 2, 3])):
            add(d, rnd.choice(SUP[:5] + SUP[6:]))
        if d.weekday() == 5: add(d, SUP[5])                        # зарплата бригаде — по субботам
        d += dt.timedelta(days=1)
    nov = [r for r in rows if r['date'].month == 11]
    add(dt.date(2026, 11, 3), SUP[7], 3150); add(dt.date(2026, 11, 2), ('PT Abadi Contoh', 'Аренда', 'Invoice', [12000]))
    add(dt.date(2026, 10, 1), ('PT Abadi Contoh', 'Аренда', 'Invoice', [12000]))
    nov[4].update(check='Review'); nov[17].update(check='Review')                                 # стоит проверить
    next(r for r in nov if r['payee'] == 'Sunrise Hardware' and r['date'].day > 10).update(cat='')   # без категории
    src = nov[8]; rows.append(dict(src, date=src['date'] + dt.timedelta(days=1), check='DBL'))  # тот же чек второй раз
    src = nov[30]; rows.append(dict(src, date=src['date'], check='DBL'))
    return rows

# Языки примера (25.11, сайт на EN и ID): python3 month-report.py en → month-report-en.png
NAMES = {
    'en': {'Материалы': 'Materials', 'Инструменты': 'Tools', 'Подрядчики': 'Contractors', 'Зарплаты': 'Wages', 'Топливо': 'Fuel',
           'Электрика': 'Electrical', 'Аренда': 'Rent', 'Бригада Wayan': 'Wayan crew', 'Ваша компания': 'Your company'},
    'id': {'Материалы': 'Material', 'Инструменты': 'Peralatan', 'Подрядчики': 'Kontraktor', 'Зарплаты': 'Gaji', 'Топливо': 'BBM',
           'Электрика': 'Listrik', 'Аренда': 'Sewa', 'Бригада Wayan': 'Tim Wayan', 'Ваша компания': 'Perusahaan Anda'},
}
FOOT = {'ru': 'Подготовлено в Nota', 'en': 'Made with Nota', 'id': 'Dibuat dengan Nota'}

if __name__ == '__main__':
    loc = sys.argv[1] if len(sys.argv) > 1 else 'ru'
    # Валюта (25.11: индонезийская версия сайта — отчёт в рупиях): python3 month-report.py id IDR
    if len(sys.argv) > 2 and sys.argv[2] == 'IDR':
        CUR, RATE = 'IDR', 1
    rows = build()
    N = NAMES.get(loc, {})
    if N:
        for r in rows:
            r['cat'] = N.get(r['cat'], r['cat']); r['payee'] = N.get(r['payee'], r['payee'])
    h = C.period_card(rows, dt.date(2026, 11, 1), dt.date(2026, 11, 30), 'month', N.get('Ваша компания', 'Ваша компания'), loc=loc, cur=CUR,
                      prev_rows=rows, report_date=dt.date(2026, 11, 25), client_start=dt.date(2026, 10, 1))
    i = h.find(FOOT[loc]); a = h.rfind('<div style="padding-top: ', 0, i); b = h.find('</div>', h.find('@NotaGetBot', i)) + 6
    assert i > 0 and a > 0, 'не нашёл нижнюю строку'
    h = h[:a] + h[b:]
    suf = ('' if loc == 'ru' else '-' + loc) + ('' if CUR == 'USD' else '-' + CUR.lower())
    p = os.path.join(HERE, f'month-report{suf}.html'); open(p, 'w', encoding='utf-8').write(h)
    subprocess.run(['node', os.path.join(GEN, 'render.cjs'), p, p[:-5] + '.png', '2'], check=True)
