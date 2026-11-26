# Fictional demo data for the Nota Payments sheet (EN, USD). Nothing here comes from real clients.
# 26.11: данные для копии таблицы «Nota — demo table for site screenshots (EN, USD)» — скриншоты Payments / Monthly spend / Insights для сайта.
# Запуск: python3 demo-sheet-gen.py rows.json → строки A:O для листа Payments (даты — числа Google Sheets).
# После заливки в таблице поправлены: короткие месяцы в Purpose → полные (Jun → June), ID 187 → DOC-26-148 (совпал номер).
import random, datetime as dt, json, sys, statistics as st, collections as C
R = random.Random(2611)
TODAY = dt.date(2026, 11, 26)
MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
MONTHS = [(2026, m) for m in range(6, 12)]
LAST_DAY = {6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 25}

P = {  # people -> (name, group)
 'john': ('John Page', 'Mangata Villas'), 'daniel': ('Daniel Kim', 'Mangata Villas'),
 'rizky': ('Rizky Pratama', 'Mangata Villas'), 'ayu': ('Ayu Lestari', 'Mangata Villas'),
 'made': ('Made Wirawan', 'Sunset Resort'), 'putu': ('Putu Ariani', 'Sunset Resort'),
 'maria': ('Maria Santos', 'Head office'), 'alex': ('Alex Morgan', 'personal'),
}
def bu_of(p):
    g = P[p][1]
    return 'Personal' if g == 'personal' else g

rows = []
def add(y, m, d, who, typ, payee, purpose, amount, cat, **kw):
    d = min(max(1, d), LAST_DAY[m])
    rows.append(dict(date=dt.date(y, m, d), who=who, type=typ, payee=payee, purpose=purpose,
                     amount=int(round(amount)), cat=cat, **kw))

def rnd(a, b, step=5):
    return round(R.uniform(a, b) / step) * step

for (y, m) in MONTHS:
    mn = MON[m - 1]
    prev = MON[m - 2]
    # --- recurring, Head office
    add(y, m, 3, 'maria', 'Invoice', 'Bay Office Space', f'Office rent, {mn}', 1250, 'Rent')
    add(y, m, 5, 'maria', 'Invoice', 'Kuta Storage', f'Warehouse rent, {mn}', 450, 'Rent')
    add(y, m, R.randint(6, 9), 'maria', 'Invoice', 'Nusa Net', f'Internet, office, {mn}', 65, 'Telecom & IT')
    add(y, m, R.randint(8, 11), 'maria', 'Invoice', 'Island Power', f'Electricity, office, {prev}', rnd(95, 125), 'Utilities')
    add(y, m, R.randint(10, 14), 'maria', 'Proof', 'Regional tax office', f'Monthly tax payment, {prev}', rnd(420, 780, 10), 'Taxes & fees')
    add(y, m, R.randint(18, 22), 'maria', 'Invoice', 'Clearpoint Advisory', f'Bookkeeping and tax filing, {prev}', 650, 'Consultants')
    add(y, m, R.randint(12, 24), 'maria', 'Receipt', 'Northwind Trading', R.choice(['Printer paper and ink', 'Office supplies', 'Cleaning supplies, office']), rnd(18, 60, 1), 'Supplies')
    # --- recurring, Sunset Resort
    add(y, m, R.randint(6, 9), 'made', 'Invoice', 'Nusa Net', f'Internet, resort, {mn}', 120, 'Telecom & IT')
    add(y, m, R.randint(8, 11), 'made', 'Invoice', 'Island Power', f'Electricity, resort, {prev}', rnd(310, 420), 'Utilities')
    add(y, m, R.randint(9, 13), 'made', 'Invoice', 'Clear Water Co', f'Water supply, resort, {prev}', rnd(70, 95), 'Utilities')
    add(y, m, 25, 'made', 'Document', 'Resort staff', f'Staff salaries, {mn}', rnd(5200, 5600, 50), 'Staff')
    for _ in range(R.randint(3, 4)):
        add(y, m, R.randint(1, 28), R.choice(['made', 'putu', 'putu']), 'Receipt', 'Fresh Market', 'Breakfast supplies for guests', rnd(80, 240, 1), 'Supplies')
    add(y, m, R.randint(2, 27), 'putu', 'Receipt', 'Blue Lagoon Pools', 'Pool chemicals', rnd(85, 140, 1), 'Supplies')
    add(y, m, R.randint(2, 27), 'putu', R.choice(['Receipt', 'Hand']), 'Clean & Co', R.choice(['Laundry service, guest linen', 'Laundry service, towels']), rnd(60, 110, 1), 'Supplies')
    # --- recurring, Mangata Villas
    add(y, m, 1, 'john', 'Document', 'Site crew', 'Wages, site crew (2 weeks)', rnd(3800, 6200, 50), 'Staff')
    add(y, m, 15, 'john', 'Document', 'Site crew', 'Wages, site crew (2 weeks)', rnd(3800, 6200, 50), 'Staff')
    for d in (4, 14, 24):
        add(y, m, d + R.randint(-1, 2), R.choice(['rizky', 'daniel']), 'Receipt', 'City Fuel', 'Diesel for generator, 200 L', rnd(190, 230, 1), 'Fuel')
    for _ in range(R.randint(3, 4)):
        add(y, m, R.randint(1, 28), 'rizky', R.choice(['Receipt', 'Receipt', 'Hand']), 'City Fuel', 'Petrol, pickup truck', rnd(25, 45, 1), 'Fuel')
    for _ in range(R.randint(4, 6)):
        add(y, m, R.randint(1, 28), R.choice(['ayu', 'daniel', 'rizky', 'ayu']), 'Receipt', 'Sunrise Hardware',
            R.choice(['Nails and screws', 'Cable ties and work gloves', 'Silicone sealant, 6 tubes', 'Drill bits set', 'Sandpaper and putty knives', 'Masking tape, 2 rolls']), rnd(9, 65, 1), 'Supplies')
    for _ in range(R.randint(1, 2)):
        add(y, m, R.randint(1, 28), R.choice(['daniel', 'ayu']), 'Receipt', 'Bright Tools',
            R.choice(['Angle grinder discs, 10 pcs', 'Measuring tapes and levels', 'Paint rollers and brushes', 'Safety helmets, 6 pcs']), rnd(25, 120, 1), 'Supplies')
    for _ in range(R.randint(1, 2)):
        add(y, m, R.randint(1, 28), 'rizky', 'Hand', 'Warung Sari', 'Coffee and snacks for site meeting', rnd(14, 32, 1), 'Other')
    add(y, m, R.randint(1, 28), 'rizky', 'Hand', 'Aqua Depot', 'Drinking water, 20 gallons', rnd(16, 22, 1), 'Other')
    if R.random() < 0.8:
        add(y, m, R.randint(1, 28), R.choice(['rizky', 'daniel']), 'Hand', '', R.choice(['Payment to helper', 'Overtime, 2 workers']), rnd(25, 60, 5), 'Staff')
    add(y, m, R.randint(1, 28), 'ayu', 'Hand', '', 'SIM top-up, site phones', rnd(10, 15, 1), 'Telecom & IT')
    # --- personal
    for _ in range(R.randint(2, 4)):
        t = R.choice([('Receipt', 'Ocean Grill', 'Dinner with supplier', (45, 95), 'Other'),
                      ('Receipt', 'City Fuel', 'Petrol, car', (15, 30), 'Fuel'),
                      ('Invoice', 'SkyWay Air', 'Flight Jakarta – Bali', (120, 175), 'Transport'),
                      ('Receipt', 'Island Cabs', 'Taxi to the airport', (14, 24), 'Transport'),
                      ('Invoice', 'Nusa Mobile', f'Phone plan, {mn}', (22, 22), 'Telecom & IT')])
        add(y, m, R.randint(1, 28), 'alex', t[0], t[1], t[2], rnd(*t[3], 1), t[4])

# --- construction phases, Mangata Villas
def inv(m, d, who, payee, purpose, a, b, cat, typ='Invoice', step=10):
    add(2026, m, d, who, typ, payee, purpose, rnd(a, b, step), cat)
# June: permits, excavation, foundations
inv(6, 2, 'john', 'Regional tax office', 'Building permit fee, villas 3–4', 330, 350, 'Taxes & fees', 'Proof')
inv(6, 3, 'ayu', 'Warung Sari', 'Offerings for the groundbreaking ceremony', 80, 90, 'Other', 'Hand', 1)
inv(6, 4, 'john', 'Atlas Rental', 'Excavator rental, 3 days', 1300, 1400, 'Equipment rental')
inv(6, 6, 'john', 'Arcline Studio', 'Structural drawings, stage 2', 2400, 2400, 'Engineering')
inv(6, 9, 'daniel', 'Harbor Steel', 'Steel rebar 13 mm, full truck', 2900, 3400, 'Materials')
inv(6, 10, 'daniel', 'Metro Build', 'Cement, 120 bags', 780, 960, 'Materials')
inv(6, 12, 'ayu', 'Metro Build', 'Sand and gravel, 2 trucks', 420, 520, 'Materials')
inv(6, 16, 'john', 'Atlas Rental', 'Concrete mixer rental, 1 week', 180, 180, 'Equipment rental')
inv(6, 20, 'john', 'Structure crew', 'Foundation works, stage 1', 6500, 7200, 'Contractors', step=50)
inv(6, 23, 'daniel', 'Harbor Steel', 'Wire mesh M8, 40 sheets', 760, 820, 'Materials')
inv(6, 26, 'rizky', 'Swift Logistics', 'Delivery of steel and cement', 120, 180, 'Transport')
# July: structure
inv(7, 2, 'john', 'Atlas Rental', 'Scaffolding rental, July', 620, 760, 'Equipment rental')
inv(7, 6, 'daniel', 'Metro Build', 'Cement, 160 bags', 1050, 1250, 'Materials')
inv(7, 8, 'daniel', 'Harbor Steel', 'Steel rebar 10 mm, 4 t', 2700, 3100, 'Materials')
inv(7, 13, 'john', 'Arcline Studio', 'Site supervision, July', 1500, 1500, 'Engineering')
inv(7, 15, 'john', 'Structure crew', 'Concrete works, stage 2', 8800, 9800, 'Contractors', step=50)
inv(7, 19, 'ayu', 'Metro Build', 'Red bricks, 6 000 pcs', 1100, 1200, 'Materials')
inv(7, 22, 'rizky', 'Swift Logistics', 'Crane truck, 4 hours', 230, 250, 'Transport')
inv(7, 27, 'john', 'Structure crew', 'Concrete works, stage 3', 7400, 8200, 'Contractors', step=50)
inv(7, 29, 'daniel', 'FixPro Service', 'Generator overhaul', 460, 500, 'Repairs')
# August: roof and walls
inv(8, 1, 'john', 'Atlas Rental', 'Scaffolding rental, August', 620, 760, 'Equipment rental')
inv(8, 5, 'daniel', 'Coastline Timber', 'Roof timber, teak', 3600, 4100, 'Materials')
inv(8, 8, 'ayu', 'Metro Build', 'Red bricks, 8 000 pcs', 1450, 1600, 'Materials')
inv(8, 11, 'daniel', 'Metro Build', 'Clay roof tiles, 4 200 pcs', 2600, 2900, 'Materials')
inv(8, 14, 'rizky', 'Swift Logistics', 'Delivery of timber', 150, 220, 'Transport')
inv(8, 18, 'john', 'Structure crew', 'Walls and roof frame, stage 4', 7600, 8600, 'Contractors', step=50)
inv(8, 21, 'daniel', 'Metro Build', 'Cement, 100 bags', 650, 800, 'Materials')
inv(8, 26, 'john', 'Mike Turner', 'Roofing works, stage 1', 4200, 4800, 'Contractors', step=50)
inv(8, 29, 'ayu', 'Evercolor Paints', 'Wood stain, 20 L', 300, 330, 'Materials')
# September: MEP, windows
inv(9, 1, 'john', 'Atlas Rental', 'Scaffolding rental, September', 620, 760, 'Equipment rental')
inv(9, 3, 'daniel', 'Island Electric', 'Electrical cables and sockets', 900, 1250, 'Materials')
inv(9, 7, 'daniel', 'AquaFlow Plumbing', 'PVC pipes and fittings', 380, 540, 'Materials')
inv(9, 10, 'john', 'Arcline Studio', 'Site supervision, September', 1500, 1500, 'Engineering')
inv(9, 12, 'daniel', 'Coastline Timber', 'Window frames, teak, 14 pcs', 2000, 2200, 'Materials')
inv(9, 16, 'daniel', 'Island Electric', 'Distribution boards, 4 pcs', 620, 660, 'Materials')
inv(9, 19, 'john', 'Island Electric', 'Electrical installation, villas 1–2', 3100, 3500, 'Contractors', step=50)
inv(9, 23, 'daniel', 'Coastline Timber', 'Window glass, 14 panels', 1100, 1180, 'Materials')
inv(9, 25, 'made', 'FixPro Service', 'AC repair, villa 2', 85, 160, 'Repairs')
inv(9, 28, 'john', 'Mike Turner', 'Roofing works, stage 2', 3600, 4200, 'Contractors', step=50)
# October: finishing
inv(10, 1, 'john', 'Atlas Rental', 'Scaffolding rental, October', 620, 760, 'Equipment rental')
inv(10, 3, 'daniel', 'Stonecraft Tiles', 'Floor tiles, 220 m²', 3600, 4400, 'Materials')
inv(10, 6, 'daniel', 'AquaFlow Plumbing', 'Water heaters, 4 pcs', 1450, 1500, 'Materials')
inv(10, 9, 'john', 'Finishing crew', 'Plastering and finishing, stage 1', 4800, 5600, 'Contractors', step=50)
inv(10, 12, 'ayu', 'Evercolor Paints', 'Exterior paint, 40 L', 540, 580, 'Materials')
inv(10, 13, 'rizky', 'Swift Logistics', 'Delivery of tiles', 90, 160, 'Transport')
inv(10, 15, 'daniel', 'Stonecraft Tiles', 'Bathroom tiles, 90 m²', 1600, 1700, 'Materials')
inv(10, 20, 'john', 'Mike Turner', 'Tiling works, stage 1', 4300, 5000, 'Contractors', step=50)
inv(10, 22, 'daniel', 'Coastline Timber', 'Door frames, teak, 6 pcs', 1350, 1400, 'Materials')
inv(10, 24, 'ayu', 'Evercolor Paints', 'Primer and wall putty', 220, 260, 'Materials')
inv(10, 27, 'made', 'Blue Lagoon Pools', 'Pool pump repair', 240, 280, 'Repairs')
inv(10, 29, 'john', 'Pool Pros', 'Pool construction, advance 30%', 7600, 7900, 'Contractors', 'Proof', step=50)
inv(10, 30, 'putu', 'Linen Lane', 'Bed linen and towels, 20 sets', 480, 540, 'Supplies')
# November: finishing, pool, landscaping
inv(11, 2, 'john', 'Atlas Rental', 'Scaffolding rental, November', 620, 760, 'Equipment rental')
inv(11, 3, 'daniel', 'AquaFlow Plumbing', 'Bathroom fittings, villas 1–2', 1900, 2050, 'Materials')
inv(11, 5, 'john', 'Finishing crew', 'Plastering and finishing, stage 2', 4600, 5400, 'Contractors', step=50)
inv(11, 7, 'daniel', 'Island Electric', 'LED lights, 60 pcs', 500, 540, 'Materials')
inv(11, 7, 'john', 'Mike Turner', 'Tiling works, stage 2', 4200, 4600, 'Contractors', step=50)
inv(11, 10, 'john', 'Arcline Studio', 'Site supervision, November', 1500, 1500, 'Engineering')
inv(11, 12, 'ayu', 'Evercolor Paints', 'Interior paint, 60 L', 610, 680, 'Materials')
inv(11, 14, 'rizky', 'Swift Logistics', 'Delivery of doors and fittings', 110, 170, 'Transport')
inv(11, 18, 'john', 'Green Leaf Gardens', 'Landscaping, villas 1–2', 2000, 2200, 'Contractors', step=50)
inv(11, 20, 'daniel', 'Coastline Timber', 'Kitchen cabinets, villa 1', 2300, 2600, 'Materials')
inv(11, 24, 'john', 'Pool Pros', 'Pool construction, stage 2', 5200, 5800, 'Contractors', step=50)
inv(11, 24, 'made', 'FixPro Service', 'Water heater repair', 110, 140, 'Repairs')
inv(11, 21, 'maria', 'Tirta & Partners', 'Legal review, villa lease contract', 1200, 1200, 'Consultants')

# --- planted cases ------------------------------------------------------
# typos in the amount: the reason Insights shows "Check these"
add(2026, 11, 13, 'ayu', 'Receipt', 'Sunrise Hardware', 'Masking tape, 2 rolls', 4800, 'Supplies', plant='typo')
add(2026, 10, 18, 'rizky', 'Receipt', 'City Fuel', 'Petrol, pickup truck', 3500, 'Fuel', plant='typo')
add(2026, 9, 21, 'rizky', 'Hand', 'Warung Sari', 'Coffee and snacks for site meeting', 2250, 'Other', plant='typo')
# no category
add(2026, 11, 9, 'john', 'Receipt', 'Northwind Trading', 'Items for villa 3', 460, '', plant='nocat')
add(2026, 10, 27, 'daniel', 'Proof', '', 'Transfer, no description', 350, '', plant='nocat')
add(2026, 11, 16, 'rizky', 'Hand', '', 'Cash advance for site purchases', 200, '', plant='nocat')
add(2026, 8, 17, 'ayu', 'Receipt', 'Bright Tools', 'Tools for villa 2', 185, '', plant='nocat')
add(2026, 11, 22, 'putu', 'Receipt', 'Fresh Market', 'Items for the resort kitchen', 140, '', plant='nocat')

rows.sort(key=lambda r: (r['date'], R.random()))

# --- review rows
REVIEW = ['Amount not recognised', 'Total ≠ sum of line items', 'Date unclear, file date used',
          'Not all line items recognised', 'Blurry photo, check the amount',
          'Tax invoice: check the amount against the commercial invoice',
          'Amount after the advance not confirmed', 'Handwritten total differs from line items']
cands = [r for r in rows if r['type'] in ('Hand', 'Receipt', 'Invoice') and not r.get('plant')]
for i, r in enumerate(R.sample(cands, 16)):
    r['check'] = 'Review'
    r['comment'] = REVIEW[i % len(REVIEW)]
# OK rows that still carry a note
for r in R.sample([r for r in rows if r['type'] == 'Hand' and 'check' not in r], 6):
    r['comment'] = R.choice(['Date unclear, file date used', 'Payee not written on the note'])

# --- duplicates: the same document sent twice
orig_pool = [r for r in rows if r['type'] in ('Receipt', 'Invoice') and 'check' not in r and not r.get('plant')]
dup_src = R.sample([r for r in orig_pool if r['date'] < dt.date(2026, 11, 1)], 11) + \
          R.sample([r for r in orig_pool if r['date'] >= dt.date(2026, 11, 1)], 5)
others = {'Mangata Villas': ['john', 'daniel', 'ayu', 'rizky'], 'Sunset Resort': ['made', 'putu'],
          'Head office': ['maria', 'john'], 'personal': ['alex']}
dups = []
for r in dup_src:
    d = dict(r)
    d['date'] = r['date']  # same document, same date
    d['who'] = R.choice(others[P[r['who']][1]])
    d['check'] = 'DBL'
    d['src'] = r
    d['dup'] = True
    dups.append(d)
    r['has_dup'] = True

# insert duplicates after the original: a few positions later in processing order
for d in dups:
    i = rows.index(d['src'])
    rows.insert(min(len(rows), i + R.randint(1, 6)), d)
# processing order must keep dates non-decreasing: a duplicate keeps its document date, which is fine
for i, r in enumerate(rows, 1):
    r['id'] = i
for d in dups:
    d['match'] = f"→ ID {d['src']['id']}"

# --- file numbers
inv_no = 2900
def fileno(r):
    global inv_no
    t = r['type']
    if t == 'Hand':
        return 'no-num'
    if t == 'Invoice':
        inv_no += R.randint(3, 40)
        return f'INV-26-{inv_no}'
    if t == 'Document':
        return f'DOC-26-{R.randint(40, 199):03d}'
    if t == 'Proof':
        return R.choice(['no-num', f'TRF{R.randint(10**7, 10**8 - 1)}'])
    return R.choice([f'R-{R.randint(10000, 99999)}', f'{R.randint(1000, 9999)}', f'#{R.randint(10**6, 10**7 - 1)}'])
for r in rows:
    if r.get('dup'):
        continue
    r['file'] = fileno(r)
for d in dups:
    d['file'] = d['src']['file']

# --- statuses and accounts
to_pay_dates = {dt.date(2026, 10, 12), dt.date(2026, 11, 3), dt.date(2026, 11, 7), dt.date(2026, 11, 12), dt.date(2026, 11, 20), dt.date(2026, 11, 24)}
for r in rows:
    r.setdefault('check', 'OK')
    r.setdefault('match', '')
    r.setdefault('comment', '')
    if r['check'] == 'Review':
        r['match'] = 'Comment→'
    age = (TODAY - r['date']).days
    if r.get('dup'):
        r['status'] = 'Rejected'
    elif r['check'] == 'Review':
        r['status'] = 'Paid' if age > 40 and R.random() < 0.6 else ''
    elif age > 45:
        r['status'] = 'Paid'
    elif age > 25:
        r['status'] = 'Paid' if R.random() < 0.9 else ''
    else:
        r['status'] = R.choice(['Paid', 'Paid', 'Paid', '', ''])
    if r.get('plant') == 'typo':
        r['status'] = 'Paid' if age > 25 else ''
# invoices waiting for payment
inv_rows = [r for r in rows if r['type'] == 'Invoice' and not r.get('dup') and r['check'] == 'OK']
for dte in sorted(to_pay_dates):
    pool = [r for r in inv_rows if abs((r['date'] - dte).days) <= 3 and r['status'] != 'To pay' and r['who'] != 'alex']
    pool.sort(key=lambda r: (-r['amount']))
    if pool:
        pool[0]['status'] = 'To pay'
# recent invoices with no status at all
for r in R.sample([r for r in inv_rows if r['date'] >= dt.date(2026, 11, 10) and r['status'] != 'To pay'], 5):
    r['status'] = ''
# unresolved duplicates: the latest five stay open
for d in dups[-5:]:
    d['status'] = R.choice(['', '', 'Paid', 'To pay'])
for r in rows:
    r['account'] = ''
    if r['status'] != 'Paid':
        continue
    if r['who'] == 'alex':
        r['account'] = R.choice(['Wise', 'Wise', ''])
    elif r['type'] in ('Invoice', 'Proof', 'Document'):
        r['account'] = R.choices(['BCA', 'Mandiri', 'Wise', ''], [45, 25, 12, 18])[0]
    else:
        r['account'] = R.choices(['Cash', ''], [62, 38])[0]

def serial(d):
    return (d - dt.date(1899, 12, 30)).days

out = []
for r in rows:
    name, grp = P[r['who']]
    bu = bu_of(r['who'])
    out.append([r['id'], f"{r['id']} · {r['file']}", r['type'], f'{name} · {grp}', serial(r['date']), r['amount'],
                r['purpose'], r['payee'], r['check'], r['match'], r['status'], r['cat'], bu, r['account'], r['comment']])
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'rows.json', 'w'), ensure_ascii=False)

# --- self-checks: what Insights will flag (x >= 10 * category median and x >= 100)
valid = [r for r in rows if r['check'] != 'DBL' and r['status'] != 'Rejected']
bycat = C.defaultdict(list)
for r in valid:
    bycat[r['cat'] or '(none)'].append(r['amount'])
med = {c: st.median(v) for c, v in bycat.items()}
print('rows', len(rows), 'valid', len(valid), 'total $', sum(r['amount'] for r in valid))
for (y, m) in MONTHS:
    print(MON[m-1], sum(r['amount'] for r in valid if r['date'].month == m), sum(1 for r in rows if r['date'].month == m))
print('flags:')
for r in valid:
    c = r['cat'] or '(none)'
    if r['amount'] >= 10 * med[c] and r['amount'] >= 100:
        print('  ', round(r['amount'] / med[c]), '×', r['id'], r['purpose'], r['amount'], c, 'med', med[c])
print('checks', C.Counter(r['check'] for r in rows))
print('status', C.Counter(r['status'] for r in rows))
print('types', C.Counter(r['type'] for r in rows))
print('to pay', [(r['id'], str(r['date']), r['amount'], r['purpose']) for r in rows if r['status'] == 'To pay' and r['check'] != 'DBL'])
print('open dups', [(r['id'], r['status'], r['purpose'], r['amount']) for r in dups if r['status'] != 'Rejected'])
print('people', C.Counter(P[r['who']][0] for r in rows).most_common())
hand = sum(1 for r in valid if r['type'] == 'Hand') / len(valid)
print('hand share', round(hand, 3))
