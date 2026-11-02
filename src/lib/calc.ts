// Калькуляторы на главной: доходность виллы (кэшфлоу инвестора), рассрочка или скидка, дубли и ошибки.
// Одни и те же функции считают при сборке (значения по умолчанию) и в браузере (цифры посетителя).
// Показатели не вписываются руками: IRR, NPV и MOIC выводятся из потоков.

import { npv, irr } from './finmodel';

// ---------- Форматирование ----------
const NB = ' '; // узкий неразрывный пробел в разрядах
export const group = (v: number, d = 0) => {
  const s = Math.abs(v).toFixed(d);
  const [a, b] = s.split('.');
  const g = a.replace(/\B(?=(\d{3})+(?!\d))/g, NB);
  return (v < 0 && Number(s) !== 0 ? '−' : '') + (b ? `${g},${b}` : g);
};
export const usd = (v: number) => `${v < 0 ? '−' : ''}$${group(Math.abs(v))}`;
export const pct = (v: number, d = 1) => `${group(v * 100, d)}%`;
// Тысячи долларов для подписей оси: $120k
export const usdK = (v: number) => (Math.abs(v) < 0.5 ? '$0' : `${v < 0 ? '−' : ''}$${group(Math.abs(v) / 1000)}k`);

// ---------- 1. Вилла: кэшфлоу инвестора ----------
export type VillaIn = {
  price: number; // цена покупки, USD
  adr: number; // средняя цена ночи, USD
  occ: number; // загрузка, %
  mgmt: number; // комиссия управляющей компании, % от выручки после комиссий площадок
  years: number; // срок владения, лет; продажа в конце последнего года
  growth: number; // рост цены объекта в год, %
  fixed: number; // постоянные расходы, USD в год в ценах сегодня: персонал, коммунальные, страховка
  build: number; // лет до сдачи: вилла куплена на стройке, аренды в эти годы нет
  ota: number; // комиссии площадок бронирования, % выручки
  opex: number; // переменные расходы: расходники, прачечная, мелкий ремонт, % выручки
  tax: number; // налоги, % выручки
  adrGrowth: number; // рост цены ночи в год, %
  saleCost: number; // расходы на продажу, % от цены продажи
  lease: number; // срок лизхолда на дату покупки, лет; 0 — собственность
  rate: number; // ставка дисконтирования для NPV, %
};

// Значения по умолчанию ждут подтверждения Евгения (его реальные цифры содержания вилл)
export const VILLA_DEFAULT: VillaIn = {
  price: 300000, adr: 200, occ: 70, mgmt: 20, fixed: 9000, years: 10, lease: 0, growth: 3,
  build: 0, ota: 15, opex: 8, tax: 10, adrGrowth: 3, saleCost: 5, rate: 10,
};

export type VillaRow = {
  year: number; rev: number; ota: number; mgmt: number; opex: number; fixed: number; tax: number;
  net: number; sale: number; cf: number; cum: number;
};

// Одна строка за год t (t от 1). Цена ночи и постоянные расходы растут с даты покупки.
// Пока вилла строится, аренды и расходов нет.
function rentYear(v: VillaIn, t: number) {
  if (t <= v.build) return { rev: 0, ota: 0, mgmt: 0, opex: 0, fixed: 0, tax: 0, net: 0 };
  const k = (1 + v.adrGrowth / 100) ** (t - 1);
  const rev = v.adr * k * 365 * (v.occ / 100);
  const ota = rev * (v.ota / 100);
  const mgmt = (rev - ota) * (v.mgmt / 100);
  const opex = rev * (v.opex / 100);
  const fixed = v.fixed * k;
  const tax = rev * (v.tax / 100);
  return { rev, ota, mgmt, opex, fixed, tax, net: rev - ota - mgmt - opex - fixed - tax };
}

export function villa(input: VillaIn) {
  const v = { ...input };
  // По окончании лизхолда продавать нечего: срок владения не длиннее остатка аренды
  const years = Math.max(1, Math.round(v.lease > 0 ? Math.min(v.years, v.lease) : v.years));
  // Лизхолд дешевеет по мере того, как сокращается остаток срока (линейно)
  const leaseK = v.lease > 0 ? Math.max(0, (v.lease - years) / v.lease) : 1;
  const exitValue = v.price * (1 + v.growth / 100) ** years * leaseK;
  const sale = exitValue * (1 - v.saleCost / 100);

  const rows: VillaRow[] = [];
  let cum = -v.price;
  rows.push({ year: 0, rev: 0, ota: 0, mgmt: 0, opex: 0, fixed: 0, tax: 0, net: 0, sale: 0, cf: -v.price, cum });
  for (let t = 1; t <= years; t++) {
    const r = rentYear(v, t);
    const s = t === years ? sale : 0;
    const cf = r.net + s;
    cum += cf;
    rows.push({ year: t, ...r, sale: s, cf, cum });
  }
  const cf = rows.map((r) => r.cf);
  const inflow = cf.slice(1).reduce((s, c) => s + c, 0);

  // Первый год аренды (после сдачи), если он попадает в срок владения
  const r1 = rows.find((r) => r.year > v.build && r.year > 0) ?? null;
  return {
    rows,
    years,
    exitValue,
    sale,
    rent: rows.reduce((s, r) => s + r.net, 0),
    irr: irr(cf),
    npv: npv(cf, v.rate / 100),
    moic: inflow / v.price,
    net1: r1 ? r1.net / v.price : 0,
    netShare: r1 && r1.rev > 0 ? r1.net / r1.rev : 0,
    // Лизхолд кончается к концу срока владения или раньше: продавать нечего
    leaseEnd: v.lease > 0 && v.years >= v.lease,
    leaseCut: v.lease > 0 && v.years > v.lease,
  };
}
export type VillaOut = ReturnType<typeof villa>;

// Цена ночи, при которой NPV по ставке инвестора равен нулю, то есть IRR равен ставке.
// NPV растёт вместе с ценой ночи, поэтому хватает деления пополам. null, если не выйти и при $100 000.
export function villaAdrFor(v: VillaIn) {
  const f = (adr: number) => villa({ ...v, adr }).npv;
  let lo = 0;
  let hi = 100000;
  if (f(hi) < 0) return null;
  for (let i = 0; i < 60; i++) {
    const m = (lo + hi) / 2;
    if (f(m) < 0) lo = m; else hi = m;
  }
  return hi;
}

// SVG кэшфлоу: столбики по годам (покупка, чистый доход, продажа) и линия накопленного итога.
// Одна ось в долларах для всех рядов. Подписи текстом, цвета из токенов палитры.
// Ширина берётся по месту (в браузере — ширина блока), чтобы подписи оставались 11–12px на любом экране.
export const VC = { W: 720, H: 280, L: 56, R: 8, T: 14, B: 30 };

// Шаг сетки: самый мелкий «круглый» шаг, при котором линий не больше восьми
function niceStep(hi: number, lo: number) {
  const span = hi - lo || 1;
  const p = 10 ** Math.floor(Math.log10(span / 8));
  for (const k of [1, 2, 2.5, 5, 10, 20]) {
    const st = k * p;
    if (Math.ceil(hi / st) - Math.floor(lo / st) <= 8) return st;
  }
  return 50 * p;
}

export function villaChart(o: VillaOut, W = VC.W, H = VC.H) {
  const { L, R, T, B } = VC;
  const rows = o.rows;
  const hi = Math.max(0, ...rows.map((r) => r.cf), ...rows.map((r) => r.cum));
  const lo = Math.min(0, ...rows.map((r) => r.cf), ...rows.map((r) => r.cum));
  const step = niceStep(hi, lo);
  const top = Math.ceil(hi / step) * step || step;
  const bot = Math.floor(lo / step) * step;
  const ph = H - T - B;
  const y = (v: number) => T + ((top - v) / (top - bot)) * ph;
  const n = rows.length;
  const slot = (W - L - R) / n;
  const bw = Math.max(4, Math.min(28, slot * 0.56));
  const cx = (i: number) => L + slot * (i + 0.5);
  const f = (v: number) => v.toFixed(1);
  const y0 = y(0);

  let s = '';
  // Сетка и подписи оси
  for (let v = bot; v <= top + 1e-6; v += step) {
    const yy = y(v);
    s += `<line class="vc-grid${Math.abs(v) < 1e-6 ? ' vc-zero' : ''}" x1="${L}" x2="${W - R}" y1="${f(yy)}" y2="${f(yy)}"/>`;
    s += `<text class="vc-ylab" x="${L - 8}" y="${f(yy + 4)}" text-anchor="end">${usdK(v)}</text>`;
  }
  // Столбики: округлённый конец у данных, у оси прямой
  const bar = (x: number, from: number, to: number, cls: string) => {
    const y1 = y(Math.max(from, to));
    const y2 = y(Math.min(from, to));
    const h = Math.max(0, y2 - y1);
    if (h < 0.5) return '';
    const r = Math.min(3, h / 2, bw / 2);
    const up = to >= from; // растёт вверх: скругляем верх
    const x0 = x - bw / 2;
    const x1 = x + bw / 2;
    const d = up
      ? `M${f(x0)},${f(y2)} V${f(y1 + r)} Q${f(x0)},${f(y1)} ${f(x0 + r)},${f(y1)} H${f(x1 - r)} Q${f(x1)},${f(y1)} ${f(x1)},${f(y1 + r)} V${f(y2)} Z`
      : `M${f(x0)},${f(y1)} V${f(y2 - r)} Q${f(x0)},${f(y2)} ${f(x0 + r)},${f(y2)} H${f(x1 - r)} Q${f(x1)},${f(y2)} ${f(x1)},${f(y2 - r)} V${f(y1)} Z`;
    return `<path class="${cls}" d="${d}"/>`;
  };
  rows.forEach((r, i) => {
    const x = cx(i);
    if (r.year === 0) s += bar(x, 0, r.cf, 'vc-buy');
    else {
      s += bar(x, 0, r.net, 'vc-net');
      // Продажа ставится на чистый доход последнего года (если он в плюсе), между сегментами зазор 2px
      const base = Math.max(0, r.net);
      if (r.sale > 0) s += bar(x, base + (base > 0 ? (2 * (top - bot)) / ph : 0), base + r.sale, 'vc-sale');
    }
  });
  // Накопленный итог: линия по концам лет
  const pts = rows.map((r, i) => `${f(cx(i))},${f(y(r.cum))}`);
  s += `<polyline class="vc-cum" points="${pts.join(' ')}"/>`;
  rows.forEach((r, i) => { s += `<circle class="vc-dot" cx="${f(cx(i))}" cy="${f(y(r.cum))}" r="3"/>`; });
  // Подписи лет: при длинном сроке через одну
  const every = Math.max(1, Math.ceil(n / Math.max(4, Math.floor((W - L - R) / 30))));
  rows.forEach((r, i) => {
    if (i !== n - 1 && (i % every || n - 1 - i < every)) return;
    s += `<text class="vc-xlab" x="${f(cx(i))}" y="${H - 10}" text-anchor="middle">${r.year}</text>`;
  });
  // Невидимые зоны наведения шире столбика
  rows.forEach((_, i) => {
    s += `<rect class="vc-hit" data-vc-i="${i}" x="${f(L + slot * i)}" y="${T}" width="${f(slot)}" height="${ph}"/>`;
  });
  return { svg: s, W, H, y0, x: rows.map((_, i) => cx(i)), yCum: rows.map((r) => y(r.cum)) };
}

// Подсказка по году для наведения
export function villaTip(r: VillaRow) {
  if (r.year === 0) return `<b>Покупка</b><span>Вложено</span><em>${usd(r.cf)}</em><span>Накопленный итог</span><em>${usd(r.cum)}</em>`;
  if (r.rev === 0 && r.net === 0 && r.sale === 0) return `<b>Год ${r.year}</b><span>Стройка, аренды нет</span><em></em><span>Накопленный итог</span><em>${usd(r.cum)}</em>`;
  return `<b>Год ${r.year}</b>`
    + `<span>Выручка</span><em>${usd(r.rev)}</em>`
    + `<span>Чистый доход</span><em>${usd(r.net)}</em>`
    + (r.sale > 0 ? `<span>Продажа</span><em>${usd(r.sale)}</em>` : '')
    + `<span>Накопленный итог</span><em>${usd(r.cum)}</em>`;
}

// Таблица кэшфлоу по годам (для чтения без графика)
export function villaTable(o: VillaOut) {
  const head = ['Год', 'Выручка', 'Площадки', 'УК', 'Переменные', 'Постоянные', 'Налоги', 'Чистый доход', 'Продажа', 'Поток', 'Накопленный итог'];
  const cell = (v: number) => (Math.abs(v) < 0.5 ? '—' : usd(v));
  let h = `<thead><tr>${head.map((c) => `<th scope="col">${c}</th>`).join('')}</tr></thead><tbody>`;
  o.rows.forEach((r) => {
    h += `<tr><th scope="row">${r.year === 0 ? 'Покупка' : r.year}</th>`
      + [r.rev, -r.ota, -r.mgmt, -r.opex, -r.fixed, -r.tax, r.net, r.sale, r.cf, r.cum].map((v) => `<td>${cell(v)}</td>`).join('')
      + '</tr>';
  });
  return `${h}</tbody>`;
}

// ---------- 2. Рассрочка или скидка ----------
// Как в виджете инвестанализа: первый взнос сразу, остаток равными платежами в конце каждого месяца,
// ставка в месяц = годовая / 12 (12% годовых = 1% в месяц).
// У сторон деньги стоят по-разному: девелопер считает по ставке кредита или инвестора, покупатель по депозиту.
// Скидка, равная рассрочке, у каждого своя. Между ними коридор, где полная оплата выгодна обоим.
export type InstIn = { price: number; down: number; months: number; dev: number; buy: number; disc: number };
export const INST_DEFAULT: InstIn = { price: 300000, down: 30, months: 18, dev: 15, buy: 5, disc: 5 };

// Рассрочка в сегодняшних деньгах при годовой ставке rate, %
export function instPv(price: number, down: number, months: number, rate: number) {
  const n = Math.max(1, Math.round(months));
  const r = rate / 100 / 12;
  const rest = price * (1 - down / 100);
  const pay = rest / n;
  return price * (down / 100) + (r > 0 ? (pay * (1 - (1 + r) ** -n)) / r : rest);
}

export function installment(v: InstIn) {
  const n = Math.max(1, Math.round(v.months));
  const pay = (v.price * (1 - v.down / 100)) / n;
  const pvDev = instPv(v.price, v.down, n, v.dev);
  const pvBuy = instPv(v.price, v.down, n, v.buy);
  const evenDev = 1 - pvDev / v.price; // больше этой скидки девелоперу выгоднее рассрочка
  const evenBuy = 1 - pvBuy / v.price; // меньше этой скидки покупателю выгоднее рассрочка
  const cash = v.price * (1 - v.disc / 100); // полная оплата со скидкой
  return {
    pay, months: n, pvDev, pvBuy, evenDev, evenBuy, cash,
    gainDev: cash - pvDev, // выигрыш девелопера от полной оплаты в сегодняшних деньгах
    gainBuy: pvBuy - cash, // выигрыш покупателя
    corridor: evenBuy < evenDev,
  };
}

// ---------- 3. Дубли и ошибки ----------
// У клиентов Axiom дубли и ошибки, остановленные до оплаты, составили 3,55 млрд IDR, около 0,9% затрат.
// Долю 4,7% (инциденты первых недель учёта) здесь не используем: её нельзя растягивать на всю стройку.
export const DUP_SHARE = 0.009;
export type DupIn = { spend: number; months: number };
export const DUP_DEFAULT: DupIn = { spend: 2000000000, months: 24 };
export const DUP_DEFAULT_USD: DupIn = { spend: 150000, months: 24 };

export function dupes(v: DupIn) {
  const m = Math.max(1, Math.round(v.months));
  return {
    month: v.spend * DUP_SHARE,
    total: v.spend * m * DUP_SHARE,
    volume: v.spend * m,
    months: m,
  };
}

// Рупии крупно: 432 млн IDR, 1,73 млрд IDR
const trim = (s: string) => s.replace(/(,\d*?)0+$/, '$1').replace(/,$/, '');
export const idr = (v: number) => {
  const a = Math.abs(v);
  if (a >= 1e9) return `${trim(group(v / 1e9, 2))} млрд IDR`;
  if (a >= 1e6) return `${trim(group(v / 1e6, a >= 1e8 ? 0 : 1))} млн IDR`;
  return `${group(v)} IDR`;
};

// Разбор числа из поля ввода: пробелы в разрядах, запятая как десятичный знак
export const parseNum = (s: string) => {
  const v = Number(s.replace(/[\s  $%]/g, '').replace(',', '.'));
  return Number.isFinite(v) ? v : NaN;
};
