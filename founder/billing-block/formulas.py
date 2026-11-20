# Блок оплаты в шапке листа Payments (H1:J3): формулы и правила условного форматирования.
# Данные берутся из таблицы Settings на листе References (столбцы U:V) по названию в первом столбце.
# Запуск: python3 formulas.py -> f.json (формулы для H1..I3 и тексты правил цвета). Разделитель — «;» (русская локаль таблицы).
# В таблицу записано через Sheets API 20.11.2026; build-request.py собирает запрос batchUpdate.
import json
# Общая часть: читаем Settings (References!U:V) по названию в первом столбце; разделители — ру-локаль (;)
H = ('=LET(k;References!$U$1:$U$100;v;References!$V$1:$V$100;'
     'g;LAMBDA(x;IFERROR(INDEX(v;MATCH(x;k;0));""));'
     'plan;LOWER(TRIM(g("Plan*")));lim;IFERROR(VALUE(g("Docs limit*"));0);used;IFERROR(VALUE(g("Docs used*"));0);'
     'fr;IFERROR(VALUE(g("Paid from*"));0);un;IFERROR(VALUE(g("Paid until*"));0);'
     'url;TRIM(g("Payment link*"));lang;LOWER(TRIM(g("Language*")));'
     'left;MAX(0;lim-used);paid;AND(plan<>"";plan<>"free");'
     'dl;IF(un<=0;"";MAX(0;INT(un)-TODAY()+1));exp;IF(un<=0;FALSE;dl=0);')
L = lambda en, ru, id_: f'SWITCH(lang;"ru";"{ru}";"id";"{id_}";"{en}")'
MON = {'en': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec', 'ru': 'янв фев мар апр мая июн июл авг сен окт ноя дек',
       'id': 'Jan Feb Mar Apr Mei Jun Jul Agu Sep Okt Nov Des'}
ch = lambda l: 'CHOOSE(MONTH(un);' + ';'.join(f'"{m}"' for m in MON[l].split()) + ')'
D = f'd;IF(un<=0;"";DAY(un)&" "&SWITCH(lang;"ru";{ch("ru")};"id";{ch("id")};{ch("en")}));'
f = {}
f['H1'] = H + 'IF(plan="";"";IF(exp;"—";left&" ")))'
f['I1'] = H + ('n;IF(OR(lim<=0;left<=0;exp);0;MIN(4;MAX(1;ROUND(4*left/lim))));'
               'IF(plan="";"";REPT("█";n)&IF(n>0;"  ";"")&' + L('Docs left · of ', 'Документов · из ', 'Sisa dok · dari ') + '&lim))')
f['H2'] = H + 'IF(plan="";"";IF(un<=0;"—";dl&" ")))'
f['I2'] = H + D + ('tot;IF(un<=0;0;IF(fr<=0;30;MAX(1;INT(un)-INT(fr)+1)));'
               'n;IF(OR(un<=0;dl<=0);0;MIN(4;MAX(1;ROUND(4*dl/tot))));'
               'IF(plan="";"";IF(un<=0;' + L('Days left · no limit', 'Дней · без срока', 'Sisa hari · tanpa batas') +
               ';IF(exp;' + L('Plan ended ', 'Тариф истёк ', 'Paket berakhir ') + '&d;'
               'REPT("█";n)&IF(n>0;"  ";"")&' + L('Days left · to ', 'Дней · до ', 'Sisa hari · s/d ') + '&d))))')
# Тариф: «Growth plan» вместо «Growth» — чтобы не читалось как подпись к кнопке (основатель 20.11)
f['H3'] = H + ('IF(plan="";"";SWITCH(plan;"free";' + L('Free plan', 'Бесплатный тариф', 'Paket Gratis') + ';"start";' + L('Start plan', 'Тариф Старт', 'Paket Start') +
               ';"growth";' + L('Growth plan', 'Тариф Рост', 'Paket Growth') + ';"scale";' + L('Scale plan', 'Тариф Масштаб', 'Paket Scale') + ';plan)&" "))')
# Кнопка: одна подпись для всех состояний (основатель 20.11), цвет меняет условное форматирование
f['I3'] = H + 't;' + L('Payment', 'Оплата', 'Bayar') + '&"  ➚";IF(plan="";"";IF(url="";t;HYPERLINK(url;t))))'
# Условное форматирование: другой лист — только через INDIRECT
I = lambda x: f'INDEX(INDIRECT("References!V1:V100");MATCH("{x}";INDIRECT("References!U1:U100");0))'
P = f'LOWER(IFERROR({I("Plan*")};""))'; Lm = f'IFERROR(VALUE({I("Docs limit*")});0)'; S = f'IFERROR(VALUE({I("Docs used*")});0)'
E = f'IFERROR(VALUE({I("Paid until*")});0)'
EXP = f'IF({E}<=0;FALSE;TODAY()>{E})'; DW = f'IF({E}<=0;FALSE;{E}-TODAY()+1<=3)'
cf = {
 'docs': f'=AND({P}<>"";{Lm}>0;{Lm}-{S}<={Lm}/10;NOT({EXP}))',
 'days': f'={DW}',
 'crit': f'=AND({P}<>"";OR(AND({Lm}>0;{S}>={Lm});{EXP}))',
 'warn': f'=AND({P}<>"";OR(AND({Lm}>0;{Lm}-{S}<={Lm}/10);{DW}))',
}
json.dump({'f': f, 'cf': cf}, open('f.json', 'w'), ensure_ascii=False, indent=1)
for k, s in {**f, **cf}.items(): print(k, len(s), s.count('(') - s.count(')'))
