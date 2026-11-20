# Собирает запрос batchUpdate для блока оплаты в шапке листа Payments (H1:J3). Сначала: python3 formulas.py -> f.json
# ВНИМАНИЕ: генератор пишет блок в H1:J3. В таблице основатель 20.11 сдвинул блок вправо: тариф и цифры в J, кнопка K1,
# подписи K2:L2 и K3:L3, ссылки «Open Files Folder» и «Instruction» в M2:M3 — для шаблона брать раскладку из таблицы.
# Раскладка: строка 1 — тариф + кнопка «Payment ➚» (с белым отступом со всех сторон),
# строка 2 — документы, строка 3 — дни. Шрифт блока 8 (основатель уменьшил сам: блок служебный, тише аналитики), кнопка 9. Кнопка наверху, чтобы её отступ не задевал границу таблицы с заголовками.
import json
d = json.load(open('f.json')); f, cf = d['f'], d['cf']
SID = 1239511210   # лист Payments в тестовой таблице; в другой таблице — свой sheetId
c = lambda h: {'rgbColor': {'red': int(h[0:2],16)/255, 'green': int(h[2:4],16)/255, 'blue': int(h[4:6],16)/255}}
gr = lambda r0, r1, c0, c1: {'sheetId': SID, 'startRowIndex': r0, 'endRowIndex': r1, 'startColumnIndex': c0, 'endColumnIndex': c1}
def fmt(align, size, bold, color, bg='ffffff'):
    return {'backgroundColorStyle': c(bg), 'horizontalAlignment': align, 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'CLIP',
            'textFormat': {'fontFamily': 'Roboto', 'fontSize': size, 'bold': bold, 'underline': False, 'foregroundColorStyle': c(color)}}
cell = lambda formula, fm: {'userEnteredValue': {'formulaValue': formula}, 'userEnteredFormat': fm}
blank = {'userEnteredFormat': {'backgroundColorStyle': c('ffffff')}}
W = {'style': 'SOLID_THICK', 'colorStyle': c('ffffff')}; N = {'style': 'NONE'}
rows = [
 {'values': [cell(f['H3'], fmt('RIGHT', 8, True, '5d6269')), cell(f['I3'], fmt('CENTER', 9, True, 'ffffff', '0c7a4f')), blank]},  # тариф + кнопка
 {'values': [cell(f['H1'], fmt('RIGHT', 8, True, '15181c')), cell(f['I1'], fmt('LEFT', 8, False, '5d6269')), blank]},             # документы
 {'values': [cell(f['H2'], fmt('RIGHT', 8, True, '15181c')), cell(f['I2'], fmt('LEFT', 8, False, '5d6269')), blank]},             # дни
]
cust = lambda s: {'type': 'CUSTOM_FORMULA', 'values': [{'userEnteredValue': s}]}
txt = lambda h: {'textFormat': {'foregroundColorStyle': c(h)}}
def rule(rng, cond, fm):   # index 0 каждый раз — добавляем в обратном порядке приоритета
    return {'addConditionalFormatRule': {'index': 0, 'rule': {'ranges': [rng], 'booleanRule': {'condition': cond, 'format': fm}}}}
req = [
 {'unmergeCells': {'range': gr(0, 3, 8, 10)}},
 {'updateBorders': {'range': gr(0, 3, 7, 10), 'top': N, 'bottom': N, 'left': N, 'right': N, 'innerHorizontal': N, 'innerVertical': N}},
 {'updateCells': {'range': gr(0, 3, 7, 10), 'fields': 'userEnteredValue,userEnteredFormat,textFormatRuns', 'rows': rows}},
 {'mergeCells': {'range': gr(1, 3, 8, 10), 'mergeType': 'MERGE_ROWS'}},
 {'updateBorders': {'range': gr(0, 1, 8, 9), 'top': W, 'bottom': W, 'left': W, 'right': W}},
 rule(gr(0, 1, 8, 9), cust(cf['warn']), {'backgroundColorStyle': c('e84f1c'), **txt('ffffff')}),
 rule(gr(0, 1, 8, 9), cust(cf['crit']), {'backgroundColorStyle': c('d93025'), **txt('ffffff')}),
 rule(gr(2, 3, 7, 9), cust(cf['days']), txt('e84f1c')),
 rule(gr(1, 2, 7, 9), cust(cf['docs']), txt('e84f1c')),
 rule(gr(1, 3, 7, 8), {'type': 'TEXT_EQ', 'values': [{'userEnteredValue': '—'}]}, txt('9da0a3')),
]
json.dump(req, open('req.json', 'w'), ensure_ascii=False)
print(len(json.dumps(req, ensure_ascii=False)))
