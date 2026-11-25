# Инструкция для программиста: пишется на лист References под таблицу Settings (U18:W…) и в README.md.
LINES = [
 ('h', 'Для программиста · блок оплаты в шапке листа Payments (H1:J3)'),
 ('t', 'Бот пишет только в таблицу Settings выше, в столбец Value. Шапка считается формулами сама.'),
 ('t', 'Значение ищется по названию в столбце Setting: названия не менять (уточнение в скобках дописать можно), строки двигать можно.'),
 ('h', 'Что писать'),
 ('t', 'Plan — код тарифа латиницей: free, start, growth, scale.'),
 ('t', 'Docs limit (this month) — лимит документов в текущем месяце вместе с докупленными пакетами. У free — 30.'),
 ('t', 'Docs used (this month) — сколько документов учтено в текущем месяце. Дубли и файлы без платежа не считаются, многостраничный PDF — по страницам. Если больше лимита, шапка покажет 0.'),
 ('t', 'Paid from — первый день оплаченного срока. Дата (число), не текст. У free пусто.'),
 ('t', 'Paid until — последний оплаченный день, включительно. Дата (число), не текст. У free пусто.'),
 ('t', 'Payment link — https://notagetbot.com/pay/<код>. Код случайный и постоянный для таблицы, без почты и ID; создаёт сервер при подключении Google.'),
 ('t', 'Language — язык таблицы: en, ru или id.'),
 ('h', 'Когда писать'),
 ('t', 'Подключение Google — все 7 значений: free, 30, 0, пусто, пусто, ссылка, язык.'),
 ('t', 'Каждый учтённый документ — Docs used + 1.'),
 ('t', 'Оплата (сигнал платёжного сервиса на сервер) — Plan, Docs limit, Paid from, Paid until. Продление: новый срок с дня после Paid until. Смена тарифа посреди срока — правило ещё не утверждено.'),
 ('t', 'Начало каждого месяца внутри оплаченного срока (тарифы на 3 и 6 месяцев) — Docs used = 0, Docs limit = лимит тарифа.'),
 ('t', 'Пакет +50 документов — Docs limit + 50. Срок действия пакета ещё не утверждён (предложение: до конца оплаченного срока).'),
 ('h', 'Что считают формулы — не трогать'),
 ('t', 'Осталось документов = Docs limit − Docs used, не меньше 0. Осталось дней = Paid until − сегодня + 1; 0 — срок истёк.'),
 ('t', 'Полоски из 4 блоков, подписи и название тарифа — на языке Language. Кнопка «Billing ➚» (по-русски «Оплата», по-индонезийски «Tagihan») ведёт на Payment link.'),
 ('t', 'Цвет: кнопка зелёная; оранжевая — осталось ≤ 10% документов или ≤ 3 дней; красная — документы кончились или срок истёк.'),
 ('t', 'Новые таблицы создавать копированием шаблона — формулы и правила цвета переносятся как есть. Исходники: репозиторий axiom-site, папка founder/billing-block.'),
]
if __name__ == '__main__':
    import json, sys
    SID, R0 = 320261642, 17          # References, строка 18
    c = lambda h: {'rgbColor': {'red': int(h[0:2],16)/255, 'green': int(h[2:4],16)/255, 'blue': int(h[4:6],16)/255}}
    def cellf(kind, text):
        h = kind == 'h'
        return {'userEnteredValue': {'stringValue': text}, 'userEnteredFormat': {
            'wrapStrategy': 'WRAP', 'verticalAlignment': 'MIDDLE', 'horizontalAlignment': 'LEFT',
            'padding': {'top': 4 if h else 2, 'bottom': 2, 'left': 6, 'right': 6},
            'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10 if h else 9, 'bold': h, 'foregroundColorStyle': c('14201b' if h else '5d6269')}}}
    rows = [{'values': [cellf(k, t), {}, {}]} for k, t in LINES]
    n = len(LINES)
    req = [{'updateCells': {'range': {'sheetId': SID, 'startRowIndex': R0, 'endRowIndex': R0 + n, 'startColumnIndex': 20, 'endColumnIndex': 23},
                            'fields': 'userEnteredValue,userEnteredFormat', 'rows': rows}},
           {'mergeCells': {'range': {'sheetId': SID, 'startRowIndex': R0, 'endRowIndex': R0 + n, 'startColumnIndex': 20, 'endColumnIndex': 23}, 'mergeType': 'MERGE_ROWS'}},
           # спарклайн под «1,07B» — цвет строки заголовков таблицы Payments
           {'findReplace': {'find': '#5D6269', 'replacement': '#334154', 'range': {'sheetId': 1239511210, 'startRowIndex': 1, 'endRowIndex': 2, 'startColumnIndex': 3, 'endColumnIndex': 5},
                            'includeFormulas': True, 'matchCase': False}}]
    print(json.dumps(req, ensure_ascii=False))
    md = ['# Блок оplаты в шапке таблицы — инструкция для программиста'.replace('оplаты', 'оплаты'), '']
    for k, t in LINES[1:]:
        md += ['', f'## {t}', ''] if k == 'h' else [f'- {t}' if LINES.index((k, t)) > 3 else t]
    open('README.md', 'w', encoding='utf-8').write('\n'.join(md).replace('\n\n\n', '\n\n') + '\n\nФормулы и правила цвета: `formulas.py` → `f.json`, запрос для Sheets API: `build-request.py`.\n')
