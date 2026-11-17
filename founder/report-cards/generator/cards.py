# Генератор карточек отчётов Nota (архив, неделя, месяц) из строк листа Payments.
# Шаблоны — утверждённые карточки; динамические блоки пересобираются, статичные остаются как есть.
import re, datetime as dt, calendar
import os
RC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # founder/report-cards
TPL_PERIOD=open(RC+'/week.html').read().replace('width: 1080px; height: 1350px;','width: 1080px; height: auto;').replace('display: grid; grid-template-columns: 1fr 2px 1fr; column-gap: 32px','display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px')
TPL_ARCH=open(RC+'/archive.html').read().replace('width: 1080px; height: 1350px;','width: 1080px; height: auto;').replace('<div style="flex: 1 0 24px; max-height: 96px"></div>','<div style="flex: 1 0 24px"></div>').replace('display: grid; grid-template-columns: 1fr 2px 1fr; column-gap: 32px','display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px')

MON=['','янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек']
MON_NOM=['','январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
MON_DAT=['','январю','февралю','марту','апрелю','маю','июню','июлю','августу','сентябрю','октябрю','ноябрю','декабрю']
WD=['пн','вт','ср','чт','пт','сб','вс']
CAT={'Materials':'Материалы','Supplies':'Расходники','Staff':'Зарплаты','Repairs':'Ремонт','Fuel':'Топливо','Transport':'Транспорт','Contractors':'Подрядчики','Other':'Прочее'}
SP='<span style="display: inline-block; width: 0.33em"></span>'
TEAL='#0E5A52'; ORANGE='#E8501C'; GREEN='#0C7A4F'; MUTED='#56635D'; GRAY='#8A958F'

def plural(n,a,b,c):
    n=abs(n)
    if n%10==1 and n%100!=11: return a
    if 2<=n%10<=4 and not 12<=n%100<=14: return b
    return c
def full(v): return SP.join(f"{int(round(v)):,}".split(','))
def mln(v):
    s=f"{v/1e6:,.2f}"; i,d=s.split('.'); return '<span style="display: inline-block; width: 0.24em"></span>'.join(i.split(','))+','+d
def mln_plain(v):
    s=f"{v/1e6:,.2f}"; i,d=s.split('.'); return ' '.join(i.split(','))+','+d
def big(v):
    s=f"{v/1e6:,.2f}"; i,d=s.split('.')
    return '<span style="display: inline-block; width: 0.3em"></span>'.join(i.split(','))+f'<span style="font-size: 72px">,{d}</span>'

def parse_rows(values):
    head=values[0]; out=[]
    for r in values[1:]:
        r=r+['']*(15-len(r))
        amt=re.sub(r'[^\d]','',r[5]); 
        try: d=dt.datetime.strptime(r[4].strip(),'%d %b %y').date()
        except Exception: continue
        out.append(dict(id=r[0],type=r[2],date=d,amount=float(amt) if amt else 0.0,purpose=r[6],payee=r[7].strip(),check=r[8].strip(),
                        status=r[10].strip(),cat=CAT.get(r[11].strip(),'') if r[11].strip() else '',bu=r[12]))
    return out

def block(src, start):
    a=src.find(start); assert a>=0, start[:60]
    depth=0
    for m in re.finditer(r'<div\b|</div>', src[a:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth==0: return a, a+m.end()

def classify(rows):
    inc=[r for r in rows if r['amount']>0 and r['status']!='Rejected' and r['check']!='DBL' and r['type'] not in ('Statement','Proof')]
    dbl=[r for r in rows if r['check']=='DBL']
    rev=[r for r in inc if r['check']=='Review']
    rej=[r for r in rows if r not in inc and r not in dbl]
    return inc,dbl,rev,rej

# ---------- списки категорий и поставщиков ----------
def list_items(rows, key, max_rows, other_word):
    tot=sum(r['amount'] for r in rows); agg={}
    for r in rows: agg[r[key]]=agg.get(r[key],0)+r['amount']
    blank=agg.pop('',0)
    named=sorted(agg.items(), key=lambda x:-x[1])
    slots=max_rows-(1 if blank else 0)
    items=[]
    if len(named)>slots:
        keep=named[:slots-1]; rest=named[slots-1:]
        items=[(n,v,'n') for n,v in keep]+[(f'{other_word} {len(rest)}',sum(v for _,v in rest),'n')]
    else: items=[(n,v,'n') for n,v in named]
    if blank: items.append(('Без категории' if key=='cat' else 'Не указан',blank,'u' if key=='cat' else 'm'))
    return items,tot

def deltas_for(items, prev_rows, key):
    if not prev_rows: return {}
    p={}
    for r in prev_rows: p[r[key]]=p.get(r[key],0)+r['amount']
    vals={}
    for n,v,k in items:
        kk='' if k in('u','m') else n
        if kk in p and p[kk]>0: vals[n]=(v-p[kk])/p[kk]*100
    if not vals: return {}
    mx=max(vals.values()); mn=min(vals.values())
    out={}
    for n,d in vals.items():
        if d>=200: txt='×'+str(round(d/100+1))
        else:
            r=round(d); txt=('+' if r>0 else ('−' if r<0 else ''))+str(abs(r))+'%'
        c=ORANGE if (d==mx and d>0) else (GREEN if (d==mn and d<0) else GRAY)
        out[n]=(txt,c)
    return out

def row_period(name,v,tot,kind,delta,mn=None):
    pct=round(v/tot*100) if tot else 0; w=f'{v/tot*100:.1f}' if tot else '0'
    u=kind=='u'; m=kind=='m'
    dot=f'<span style="display: inline-block; width: 11px; height: 11px; background: {ORANGE}; border-radius: 50%; margin-right: 10px; vertical-align: 2px"></span>' if u else ''
    d=''
    if delta is not None:
        txt,c=delta
        d=f'<span style="margin-left: 10px; font-size: 20px; font-weight: 600; color: {c}">{txt}</span>'
    nc=GRAY if m else '#14201B'
    return ('<div><div style="display: grid; grid-template-columns: minmax(0, 1fr) auto 52px; column-gap: 10px; align-items: baseline">'
      f'<span style="font-size: 24px; font-weight: {600 if u else 400}; color: {nc}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{dot}{name}{d}</span>'
      f'<span style="font-size: 24px; font-weight: {600 if u else 500}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{mln(v)}</span>'
      f'<span style="font-size: 20px; color: {MUTED}; text-align: right; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{pct}%</span></div>'
      f'<div style="margin-top: 6px; height: 8px; border-radius: 4px; background: #EEF1EE"><div style="width: {w}%; height: 8px; border-radius: 4px; background: {ORANGE if u else ("#C9D0CB" if m else TEAL)}"></div></div></div>')

def row_arch(name,v,tot,kind):
    pct=round(v/tot*100) if tot else 0; w=f'{v/tot*100:.1f}' if tot else '0'
    u=kind=='u'; m=kind=='m'
    dot=f'<span style="display: inline-block; width: 12px; height: 12px; background: {ORANGE}; border-radius: 50%; margin-right: 10px; vertical-align: 2px"></span>' if u else ''
    nc=GRAY if m else '#14201B'
    return ('<div><div style="display: grid; grid-template-columns: 1fr auto 64px; column-gap: 12px; align-items: baseline">'
      f'<span style="font-size: 24px; font-weight: {600 if u else 400}; color: {nc}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{dot}{name}</span>'
      f'<span style="font-size: 24px; font-weight: {600 if u else 500}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{mln(v)}</span>'
      f'<span style="font-size: 22px; color: {MUTED}; text-align: right; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{pct}%</span></div>'
      f'<div style="margin-top: 6px; height: 8px; border-radius: 4px; background: #EEF1EE"><div style="width: {w}%; height: 8px; border-radius: 4px; background: {ORANGE if u else ("#C9D0CB" if m else TEAL)}"></div></div></div>')

HSTY='font-size: 19px; font-weight: 700; letter-spacing: 0.08em; color: #334154'
def lists_grid(inc, max_rows, rowfn, prev=None, gap=10, archive=False):
    cats,tot=list_items(inc,'cat',max_rows,'Остальные'); sups,_=list_items(inc,'payee',max_rows,'Остальные')
    def col(title, items, deltas):
        mn=None
        h=(f'<div style="display: flex; flex-direction: column; gap: {gap}px"><div style="{HSTY}; margin-bottom: 10px">{title}, <span style="font-weight: 600; color: {GRAY}">МЛН</span></div>')
        for n,v,k in items:
            h+= rowfn(n,v,tot,k) if archive else rowfn(n,v,tot,k,deltas.get(n),mn)
        return h+'</div>'
    dc=deltas_for(cats,prev,'cat') if prev is not None else {}
    return ('<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'+col('КАТЕГОРИИ',cats,dc)
            +'<div style="background: #E2E7E3; align-self: stretch"></div>'+col('ПОСТАВЩИКИ',sups,{})+'</div>')

# ---------- недельный и месячный ----------
def period_card(rows_all, start, end, kind, acc, prev_rows=None, prev_label=None):
    rows=[r for r in rows_all if start<=r['date']<=end]
    inc,dbl,rev,rej=classify(rows)
    tot=sum(r['amount'] for r in inc); days=(end-start).days+1
    s=TPL_PERIOD.replace('Андрей Соколов',acc,1)
    if kind=='week':
        lab=f'Расходы за неделю · {start.day}{(" "+MON[start.month]) if start.month!=end.month else ""}–{end.day} {MON[end.month]} {end.year}'
    else:
        lab=f'Расходы за месяц · {MON_NOM[start.month]} {start.year}'
    s=s.replace('Расходы за неделю · 26 окт – 1 ноя 2026',lab,1)
    # число и справа среднее + сравнение
    pinc=classify(prev_rows)[0] if prev_rows else None
    cmp=''
    if pinc:
        ptot=sum(r['amount'] for r in pinc)
        if ptot>0:
            dd=(tot-ptot)/ptot*100; d=round(dd); sign='+' if d>0 else ('−' if d<0 else '')
            ctxt=('×'+str(round(dd/100+1))) if dd>=200 else f'{sign}{abs(d)}%'
            cmp=(f'<span style="margin-top: 6px; font-size: 22px; line-height: 28px; color: {MUTED}; white-space: nowrap; font-variant-numeric: tabular-nums">'
                 f'<span style="font-weight: 600; color: #14201B">{ctxt}</span> {prev_label} · {mln(ptot)} млн</span>')
    numrow=('<div style="display: flex; align-items: flex-end; justify-content: space-between">'
      f'<div style="display: flex; align-items: baseline; gap: 14px"><span style="font-size: 120px; font-weight: 700; line-height: 1; letter-spacing: 0.025em; color: #14201B">{big(tot)}</span><span style="font-size: 28px; font-weight: 500; color: {MUTED}">млн</span></div>'
      '<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; padding-bottom: 8px">'
      f'<div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap"><span style="font-size: 44px; font-weight: 600; line-height: 48px; color: #14201B; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{mln(tot/days)}</span><span style="font-size: 24px; font-weight: 500; color: {MUTED}">млн</span></div>'
      f'<span style="font-size: 24px; line-height: 28px; color: {MUTED}">в среднем за день</span>{cmp}</div></div>')
    a,b=block(s,'<div style="display: flex; align-items: flex-end; justify-content: space-between">'); s=s[:a]+numrow+s[b:]
    # полоса
    n=len(inc); rv=sum(r['amount'] for r in rev); dv=sum(r['amount'] for r in dbl)
    num=lambda v,c: f'<span style="font-size: 44px; font-weight: 600; line-height: 48px; color: {c}; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{v}</span>'
    unit=lambda c: f'<span style="font-size: 24px; font-weight: 500; color: {c}">млн</span>'
    lab_=lambda t,c: f'<div style="font-size: 24px; line-height: 28px; color: {c}; font-variant-numeric: tabular-nums">{t}</div>'
    cell=lambda st,n_,l: f'<div style="{st}display: flex; flex-direction: column; gap: 4px"><div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap">{n_}</div>{l}</div>'
    c1=cell('padding: 12px 16px 12px 0; ',num(n,'#14201B'),lab_(f'{plural(n,"документ","документа","документов")}<br>{plural(n,"учтён","учтено","учтено")}',MUTED))
    if rev: c2=cell('border-left: 2px solid #E2E7E3; padding: 12px 16px 12px 24px; ',num(mln(rv),'#ED4E17')+unit(MUTED),lab_(f'{len(rev)} {plural(len(rev),"документ","документа","документов")}<br>{plural(len(rev),"ожидает","ожидают","ожидают")} проверки',MUTED))
    else: c2=cell('border-left: 2px solid #E2E7E3; padding: 12px 16px 12px 24px; ',num('0',GRAY),lab_('документов<br>для проверки нет',MUTED))
    if dbl: c3=cell('background: #EAF6F0; padding: 12px 16px 12px 24px; ',num(mln(dv),GREEN)+unit(GREEN),lab_(f'{len(dbl)} {plural(len(dbl),"дубль","дубля","дублей")}<br>{plural(len(dbl),"исключён","исключено","исключено")}',GREEN))
    else: c3=cell('border-left: 2px solid #E2E7E3; padding: 12px 16px 12px 24px; ',num('0',GRAY),lab_('дублей<br>не найдено',MUTED))
    strip='<div style="height: 136px; box-sizing: border-box; display: grid; grid-template-columns: 1fr 1fr 1fr; border-top: 2px solid #E2E7E3; border-bottom: 2px solid #E2E7E3">'+c1+c2+c3+'</div>'
    a,b=block(s,'<div style="height: 136px; box-sizing: border-box; display: grid; grid-template-columns: 1fr 1fr 1fr;'); s=s[:a]+strip+s[b:]
    # график
    dates=[start+dt.timedelta(days=i) for i in range(days)]
    per={d:sum(r['amount'] for r in inc if r['date']==d) for d in dates}
    unc={d:sum(r['amount'] for r in inc if r['date']==d and not r['cat']) for d in dates}
    mx=max(per.values()) if per else 0
    cols=len(dates); gapc=12 if kind=='week' else 4; rad=4 if kind=='week' else 3
    bars=''
    for d in dates:
        v=per[d]
        if v<=0: bars+='<div style="display: flex; flex-direction: column; justify-content: flex-end; min-width: 0"></div>'; continue
        hgt=max(4,round(v/mx*152)); top=round(unc[d]/v*hgt) if unc[d] else 0
        hi=(v==mx); body=TEAL if hi else '#C3DBD5'
        lbl=(f'<div style="display: flex; justify-content: center; height: 26px; margin-bottom: 6px; overflow: visible"><span style="font-size: 22px; font-weight: 600; line-height: 26px; color: #14201B; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{mln_plain(v)}</span></div>') if hi else ''
        seg=(f'<div style="height: {top}px; background: {ORANGE}; border-radius: {rad}px {rad}px 0 0"></div><div style="flex: 1; background: {body}; border-radius: 0"></div>') if top else f'<div style="flex: 1; background: {body}; border-radius: {rad}px {rad}px 0 0"></div>'
        bars+=f'<div style="display: flex; flex-direction: column; justify-content: flex-end; min-width: 0">{lbl}<div style="height: {hgt}px; display: flex; flex-direction: column">{seg}</div></div>'
    if kind=='week': labels=[WD[d.weekday()] for d in dates]
    else: labels=[str(d.day) if (d.day-1)%7==0 else '' for d in dates]
    labs=''.join(f'<div style="display: flex; justify-content: center; white-space: nowrap; font-size: 22px; line-height: 24px; color: {MUTED}">{l}</div>' for l in labels)
    chart=(f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: grid; grid-template-columns: repeat({cols}, 1fr); column-gap: {gapc}px; height: 184px; align-items: end">{bars}</div>'
           f'<div style="display: grid; grid-template-columns: repeat({cols}, 1fr); column-gap: {gapc}px">{labs}</div></div>')
    h=s.find('ПО ДНЯМ'); a,b=block(s[h:],'<div style="display: flex; flex-direction: column; gap: 8px">'); s=s[:h+a]+chart+s[h+b:]
    if not any(unc.values()):
        s=re.sub(r'<div style="display: flex; align-items: center; gap: 8px; font-size: 22px; color: #56635D; white-space: nowrap"><span style="width: 14px; height: 14px; background: #E8501C; border-radius: 50%"></span>без категории</div>','',s,count=1)
    # крупнейшие платежи
    top3=sorted(inc,key=lambda r:-r['amount'])[:3]
    prow=''
    for i,r in enumerate(top3):
        bt='border-top: 2px solid #E2E7E3; ' if i else ''
        prow+=(f'<div style="{bt}height: 72px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; gap: 2px"><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px">'
               f'<span style="font-size: 24px; font-weight: 500; line-height: 32px; color: #14201B; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{full(r["amount"])}</span>'
               f'<span style="font-size: 22px; color: {GRAY if not r["payee"] else MUTED}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0">{r["payee"] or "Поставщик не указан"}</span></div>'
               f'<div style="font-size: 22px; line-height: 28px; color: {MUTED}; white-space: nowrap">{WD[r["date"].weekday()]}, {r["date"].day:02d}.{r["date"].month:02d}</div></div>')
    h=s.find('КРУПНЕЙШИЕ ПЛАТЕЖИ'); a,b=block(s[h:],'<div style="display: flex; flex-direction: column">'); s=s[:h+a]+'<div style="display: flex; flex-direction: column">'+prow+'</div>'+s[h+b:]
    # списки
    prev_inc=classify(prev_rows)[0] if prev_rows else None
    g=lists_grid(inc,8,row_period,prev=prev_inc)
    a,b=block(s,'<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'); s=s[:a]+g+s[b:]
    return s

# ---------- архивный ----------
def archive_card(rows, acc, fname, received):
    inc,dbl,rev,rej=classify(rows)
    gross=inc+dbl; tot=sum(r['amount'] for r in gross)
    s=TPL_ARCH.replace('>Андрей Соколов<',f'>{acc}<',1).replace('>receipts_october.zip<',f'>{fname}<',1)
    d0=min(r['date'] for r in rows); d1=max(r['date'] for r in rows)
    per=(f'{d0.day}–{d1.day} {MON[d1.month]} {d1.year}' if (d0.month,d0.year)==(d1.month,d1.year) else f'{d0.day} {MON[d0.month]} – {d1.day} {MON[d1.month]} {d1.year}')
    s=s.replace('Расходы за 1–31 окт 2026 · архив получен 3 ноя',f'Расходы за {per} · архив получен {received.day} {MON[received.month]}',1)
    npay=len(gross); nf=len(rows)
    numrow=('<div style="height: 120px; display: flex; align-items: flex-end; justify-content: space-between"><div style="display: flex; align-items: baseline; gap: 14px">'
      f'<span style="font-size: 120px; font-weight: 700; line-height: 1; letter-spacing: 0.025em; color: #14201B">{big(tot)}</span><span style="font-size: 28px; font-weight: 500; color: {MUTED}">млн</span></div>'
      '<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; padding-bottom: 8px">'
      f'<span style="font-size: 44px; font-weight: 600; line-height: 48px; color: #14201B; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{npay} {plural(npay,"платёж","платежа","платежей")}</span>'
      f'<span style="font-size: 24px; line-height: 28px; color: {MUTED}">из {nf} {"файла" if (nf%10==1 and nf%100!=11) else "файлов"}</span></div></div>')
    a,b=block(s,'<div style="height: 120px; display: flex; align-items: flex-end; justify-content: space-between">'); s=s[:a]+numrow+s[b:]
    # «Не вошли в расчёт»
    nl='Не вошли в расчёт: 2 неплатёжных документа и 1 нечитаемый файл'
    i=s.find(nl); a=s.rfind('<div',0,i); b=s.find('</div>',i)+6
    if rej:
        k=len(rej); s=s[:a]+f'<div style="font-size: 24px; line-height: 30px; color: {MUTED}; font-variant-numeric: tabular-nums">Не вошли в расчёт: {k} {plural(k,"отклонённый документ","отклонённых документа","отклонённых документов")}</div>'+s[b:]
    else:
        sp=s.rfind('<div style="height: 12px; flex: none"></div>',0,a); s=s[:sp]+s[b:]
    # плитки
    tile=lambda c,v,u,t: ('<div style="box-sizing: border-box; min-width: 0; padding: 20px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column; gap: 4px">'
        f'<div style="display: flex; align-items: baseline; gap: 8px; white-space: nowrap"><span style="font-size: 48px; font-weight: 700; line-height: 52px; color: {c}; font-variant-numeric: tabular-nums">{v}</span>'
        +(f'<span style="font-size: 24px; font-weight: 500; color: {MUTED}">млн</span>' if u else '')+'</div>'
        f'<div style="font-size: 24px; line-height: 28px; min-height: 56px; color: {MUTED}">{t}</div></div>')
    hand=[r for r in gross if r['type']=='Hand']
    t1=tile(ORANGE,mln(sum(r['amount'] for r in dbl)),1,f'{len(dbl)} {plural(len(dbl),"дубль","дубля","дублей")}') if dbl else tile(GRAY,'0',0,'дублей<br>не найдено')
    t2=tile(ORANGE,mln(sum(r['amount'] for r in rev)),1,f'{len(rev)} {plural(len(rev),"документ","документа","документов")}<br>стоит проверить') if rev else tile(GRAY,'0',0,'документов<br>для проверки нет')
    t3=tile('#334154',mln(sum(r['amount'] for r in hand)),1,f'{len(hand)} {plural(len(hand),"рукописный","рукописных","рукописных")}<br>{plural(len(hand),"прочитан","прочитано","прочитано")}') if hand else tile(GRAY,'0',0,'рукописных<br>нет')
    a,b=block(s,'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">'); s=s[:a]+'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">'+t1+t2+t3+'</div>'+s[b:]
    # списки
    g=lists_grid(gross,7,row_arch,archive=True)
    a,b=block(s,'<div style="display: grid; grid-template-columns: minmax(0, 1fr) 2px minmax(0, 1fr); column-gap: 32px; align-items: start">'); s=s[:a]+g+s[b:]
    # крупнейшие платежи
    top3=sorted(gross,key=lambda r:-r['amount'])[:3]; rows_=''
    for i,r in enumerate(top3):
        bt='border-top: 2px solid #E2E7E3; ' if i else ''
        rows_+=(f'<div style="{bt}height: 56px; display: grid; grid-template-columns: 190px 110px minmax(0, 1fr) auto; column-gap: 20px; align-items: center">'
          f'<span style="font-size: 26px; font-weight: 600; color: #14201B; text-align: left; white-space: nowrap; font-variant-numeric: tabular-nums; letter-spacing: 0.02em">{full(r["amount"])}</span>'
          f'<span style="font-size: 22px; color: {MUTED}; white-space: nowrap">{r["date"].day} {MON[r["date"].month]}</span>'
          f'<span style="font-size: 24px; color: {"#14201B" if r["payee"] else GRAY}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{r["payee"] or "Поставщик не указан"}</span>'
          f'<span style="font-size: 22px; color: {MUTED}; white-space: nowrap">{r["cat"] or "Без категории"}</span></div>')
    a,b=block(s,'<div style="box-sizing: border-box; padding: 4px 24px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column">')
    s=s[:a]+'<div style="box-sizing: border-box; padding: 4px 24px; background: #EEF1EE; border-radius: 12px; display: flex; flex-direction: column">'+rows_+'</div>'+s[b:]
    return s

def footer_gap(s, px):
    i=s.find('Подготовлено в Nota'); a=s.rfind('<div style="',0,i)
    return s[:a]+s[a:i].replace('<div style="',f'<div style="padding-top: {px}px; ',1)+s[i:]
_pc=period_card; _ac=archive_card
def period_card(*a, **k): return footer_gap(_pc(*a, **k), 56)
def archive_card(*a, **k): return footer_gap(_ac(*a, **k), 32)
