# Пример отчёта для сайта (nota/public/screens/report-archive-*.webp) и картинки для соцсетей.
#   python3 site-example.py <папка_для_результата>
# Карточку собирает генератор (generator/cards.py) на выдуманных данных, потом для сайта убираются имя файла в шапке
# и нижняя строка «Подготовлено в Nota» (основатель, 19.11). Настоящие отчёты в боте остаются с ними.
# Данные: 30 файлов = 28 платежей + 2 дубля, отклонённых нет — поэтому строки «Не вошли в расчёт» нет.
import os, re, sys, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'generator'))
import cards as C

D = lambda d: dt.date(2026, 10, d)
R = lambda d, a, cat, payee, typ='Receipt', check='OK', status='': dict(date=D(d), amount=a, cat=cat, payee=payee, type=typ, check=check, status=status)
ROWS = [
    R(1, 12_000_000, 'Аренда', 'PT Abadi Contoh', 'Invoice'), R(2, 8_500_000, 'Подрядчики', 'CV Bangun Bali', 'Invoice'),
    R(3, 6_750_000, 'Материалы', 'TB Sumber Rejeki'), R(4, 2_350_000, 'Материалы', 'UD Sumber Air', 'Hand'),
    R(5, 4_800_000, 'Зарплаты', 'Бригада Wayan', 'Hand'), R(6, 450_000, 'Топливо', 'Bengkel Sinar'),
    R(7, 3_900_000, 'Материалы', 'Toko Besi Jaya', 'Hand'), R(8, 5_200_000, 'Подрядчики', 'CV Bangun Bali', 'Invoice'),
    R(9, 1_850_000, 'Инструменты', 'Toko Besi Jaya'), R(10, 4_100_000, 'Материалы', 'TB Sumber Rejeki', check='Review'),
    R(11, 4_800_000, 'Зарплаты', 'Бригада Wayan', 'Hand'), R(12, 1_780_000, 'Материалы', 'UD Sumber Air', 'Hand'),
    R(14, 12_400_000, 'Материалы', 'TB Sumber Rejeki', 'Invoice'), R(15, 520_000, 'Топливо', 'Bengkel Sinar'),
    R(16, 3_600_000, 'Подрядчики', 'CV Bangun Bali', 'Invoice', check='Review'), R(17, 2_270_000, 'Материалы', 'Toko Besi Jaya', 'Hand'),
    R(18, 4_800_000, 'Зарплаты', 'Бригада Wayan', 'Hand'), R(19, 650_000, '', '', 'Hand', check='Review'),
    R(20, 980_000, 'Инструменты', 'UD Sumber Air'), R(21, 3_300_000, 'Материалы', 'TB Sumber Rejeki'),
    R(22, 480_000, 'Топливо', 'Bengkel Sinar'), R(23, 4_400_000, 'Подрядчики', 'CV Bangun Bali', 'Invoice'),
    R(24, 1_520_000, 'Материалы', 'UD Sumber Air', 'Hand'), R(25, 4_800_000, 'Зарплаты', 'Бригада Wayan', 'Hand'),
    R(26, 2_300_000, 'Материалы', 'Toko Besi Jaya'), R(27, 2_640_000, 'Материалы', 'Toko Besi Jaya'),
    R(28, 1_200_000, '', 'Toko Besi Jaya'), R(30, 1_500_000, 'Аренда', 'PT Abadi Contoh', 'Invoice'),
    R(9, 6_750_000, 'Материалы', 'TB Sumber Rejeki', check='DBL', status='Rejected'),   # тот же чек от другого сотрудника
    R(21, 980_000, 'Инструменты', 'UD Sumber Air', check='DBL'),
]

def site_card():
    h = C.archive_card(ROWS, 'Ваша компания', 'receipts_october.zip', dt.date(2026, 11, 3), loc='ru', cur='IDR')
    # имя файла в шапке (с разделителем перед ним)
    h2 = re.sub(r'<div style="flex: none; width: 2px; height: 20px; background: #C9D0CB"></div><div style="flex: 1 1 0;[^>]*>receipts_october\.zip</div>', '', h, count=1)
    assert h2 != h, 'не нашёл имя файла в шапке'
    # нижняя строка «Подготовлено в Nota · …»
    i = h2.find('Подготовлено в Nota'); a = h2.rfind('<div style="padding-top: 32px; ', 0, i); b = h2.find('</div>', h2.find('@NotaGetBot', i)) + 6
    assert a > 0, 'не нашёл нижнюю строку'
    return h2[:a] + h2[b:]

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out, exist_ok=True)
    inc, dbl, rev, rej = C.classify(C.norm_rows(ROWS))
    print('файлов', len(ROWS), '· платежей', len(inc), '· итог', sum(r['amount'] for r in inc), '· дублей', len(dbl), '· отклонённых', len(rej))
    p = os.path.join(out, 'report-site.html'); open(p, 'w', encoding='utf-8').write(site_card())
    subprocess.run(['node', os.path.join(HERE, 'generator', 'render.cjs'), p, p[:-5] + '.png', '2'], check=True)
