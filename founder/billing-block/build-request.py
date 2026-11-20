import json
d = json.load(open('f.json')); f, cf = d['f'], d['cf']
SID = 1239511210
c = lambda h: {'rgbColor': {'red': int(h[0:2],16)/255, 'green': int(h[2:4],16)/255, 'blue': int(h[4:6],16)/255}}
W = c('ffffff')
def fmt(align, size, bold, color, bg='ffffff'):
    return {'backgroundColorStyle': c(bg), 'horizontalAlignment': align, 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'CLIP',
            'textFormat': {'fontFamily': 'Roboto', 'fontSize': size, 'bold': bold, 'underline': False, 'foregroundColorStyle': c(color)}}
cell = lambda formula, fm: {'userEnteredValue': {'formulaValue': formula}, 'userEnteredFormat': fm}
blank = lambda bg='ffffff': {'userEnteredFormat': {'backgroundColorStyle': c(bg)}}
rows = [
 {'values': [cell(f['H1'], fmt('RIGHT', 10, True, '15181c')), cell(f['I1'], fmt('LEFT', 9, False, '5d6269')), blank()]},
 {'values': [cell(f['H2'], fmt('RIGHT', 10, True, '15181c')), cell(f['I2'], fmt('LEFT', 9, False, '5d6269')), blank()]},
 {'values': [cell(f['H3'], fmt('RIGHT', 10, True, '5d6269')), cell(f['I3'], fmt('CENTER', 9, True, 'ffffff', '0c7a4f')), blank()]},
]
gr = lambda r0, r1, c0, c1: {'sheetId': SID, 'startRowIndex': r0, 'endRowIndex': r1, 'startColumnIndex': c0, 'endColumnIndex': c1}
def rule(rng, cond, fm):
    return {'addConditionalFormatRule': {'index': 0, 'rule': {'ranges': [rng], 'booleanRule': {'condition': cond, 'format': fm}}}}
cust = lambda s: {'type': 'CUSTOM_FORMULA', 'values': [{'userEnteredValue': s}]}
txt = lambda h, bold=None: {'textFormat': {'foregroundColorStyle': c(h), **({'bold': bold} if bold is not None else {})}}
req = [
 {'updateCells': {'range': gr(0, 3, 7, 10), 'fields': 'userEnteredValue,userEnteredFormat,textFormatRuns', 'rows': rows}},
 {'updateBorders': {'range': gr(2, 3, 8, 9), **{k: {'style': 'SOLID_THICK', 'colorStyle': W} for k in ('top', 'bottom', 'left', 'right')}}},  # кнопка только в I3, белый отступ со всех сторон
 # index 0 каждый раз — значит, добавляем в обратном порядке приоритета
 rule(gr(2, 3, 8, 9), cust(cf['warn']), {'backgroundColorStyle': c('e84f1c'), **txt('ffffff')}),
 rule(gr(2, 3, 8, 9), cust(cf['crit']), {'backgroundColorStyle': c('d93025'), **txt('ffffff')}),
 rule(gr(1, 2, 7, 9), cust(cf['days']), txt('e84f1c')),
 rule(gr(0, 1, 7, 9), cust(cf['docs']), txt('e84f1c')),
 rule(gr(0, 2, 7, 8), {'type': 'TEXT_EQ', 'values': [{'userEnteredValue': '—'}]}, txt('9da0a3')),
]
json.dump(req, open('req.json', 'w'), ensure_ascii=False)
print(len(json.dumps(req, ensure_ascii=False)))
