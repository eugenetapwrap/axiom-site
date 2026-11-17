# Пример: собрать три карточки на выдуманных данных и отрисовать их в PNG.
#   python3 example.py && ls out/
# Для рендера нужен Node.js с Playwright (см. render.cjs).
import os, sys, random, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cards as C

random.seed(7)
D = dt.date
PAYEES = ['Toko Contoh Jaya', 'CV Karya Mandiri', 'UD Sumber Air', 'Bengkel Sinar', 'PT Abadi Contoh', '']
CATS = ['Материалы', 'Расходники', 'Подрядчики', 'Топливо', 'Ремонт', '']     # категории — как в листе Payments
def rows_for(start, days, n):
    out = []
    for i in range(n):
        out.append(dict(date=start + dt.timedelta(days=random.randrange(days)), amount=random.choice([85, 150, 240, 410, 760, 1200, 3450]) * 1000,
                        payee=random.choice(PAYEES), cat=random.choice(CATS), check=random.choice(['OK'] * 12 + ['Review', 'DBL']),
                        status=random.choice([''] * 15 + ['Rejected']), type=random.choice(['Receipt', 'Invoice', 'Hand'])))
    return out

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
week = rows_for(D(2026, 11, 9), 7, 40); prev_week = rows_for(D(2026, 11, 2), 7, 30)
month = rows_for(D(2026, 10, 1), 31, 150)
archive = rows_for(D(2026, 10, 1), 31, 30)
cards = {
    'archive': C.archive_card(archive, 'Андрей Соколов', 'receipts_october.zip', D(2026, 11, 3), loc='ru', cur='IDR'),
    'week': C.period_card(week, D(2026, 11, 9), D(2026, 11, 15), 'week', 'Андрей Соколов', loc='ru', cur='IDR', prev_rows=prev_week),
    'month': C.period_card(month, D(2026, 10, 1), D(2026, 10, 31), 'month', 'Андрей Соколов', loc='ru', cur='IDR', prev_rows=None),
}
for name, html in cards.items():
    if html is None: print(name, '— нет расходов, вместо карточки сообщение'); continue
    path = os.path.join(HERE, 'out', name + '.html'); open(path, 'w').write(html)
    subprocess.run(['node', os.path.join(HERE, 'render.cjs'), path, path[:-5] + '.png'], check=True)
