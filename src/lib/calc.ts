// Калькуляторы на главной: доходность виллы (кэшфлоу инвестора), рассрочка или скидка, дубли и ошибки.
// Одни и те же функции считают при сборке (значения по умолчанию) и в браузере (цифры посетителя).
// Показатели не вписываются руками: IRR, NPV, MOIC и окупаемость выводятся из потоков.

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
  ota: number; // комиссии площадок бронирования, % выручки
  opex: number; // содержание: персонал, коммунальные, ремонт, бассейн, % выручки
  tax: number; // налоги, % выручки
  adrGrowth: number; // рост цены ночи в год, %
  saleCost: number; // расходы на продажу, % от цены продажи
  lease: number; // срок лизхолда на дату покупки, лет; 0 — собственность
  rate: number; // ставка дисконтирования для NPV, %
};

export const VILLA_DEFAULT: VillaIn = {
  price: 300000, adr: 200, occ: 70, mgmt: 20, years: 10, growth: 3,
  ota: 15, opex: 12, tax: 10, adrGrowth: 3, saleCost: 5, lease: 0, rate: 10,
};

export type VillaRow = {
  year: number; rev: number; ota: number; mgmt: number; opex: number; tax: number;
  net: number; sale: number; cf: number; cum: number;
};

// Одна строка аренды за год t (t от 1): цена ночи растёт с первого года владения
function rentYear(v: VillaIn, t: number) {
  const rev = v.adr * (1 + v.adrGrowth / 100) ** (t - 1) * 365 * (v.occ / 100);
  const ota = rev * (v.ota / 100);
  const mgmt = (rev - ota) * (v.mgmt / 100);
  const opex = rev * (v.opex / 100);
  const tax = rev * (v.tax / 100);
  return { rev, ota, mgmt, opex, tax, net: rev - ota - mgmt - opex - tax };
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
  rows.push({ year: 0, rev: 0, ota: 0, mgmt: 0, opex: 0, tax: 0, net: 0, sale: 0, cf: -v.price, cum });
  for (let t = 1; t <= years; t++) {
    const r = rentYear(v, t);
    const s = t === years ? sale : 0;
    const cf = r.net + s;
    cum += cf;
    rows.push({ year: t, ...r, sale: s, cf, cum });
  }
  const cf = rows.map((r) => r.cf);
  const inflow = cf.slice(1).reduce((s, c) => s + c, 0);

  // Окупаемость только арендой, без продажи: сколько лет чистый доход возвращает цену покупки.
  // Считается и за пределами срока владения (до 50 лет), с дробной частью внутри года.
  let paid = 0;
  let payback: number | null = null;
  for (let t = 1; t <= 50; t++) {
    const n = rentYear(v, t).net;
    if (n <= 0) break;
    if (paid + n >= v.price) { payback = t - 1 + (v.price - paid) / n; break; }
    paid += n;
  }

  const r1 = rows[1];
  return {
    rows,
    years,
    exitValue,
    sale,
    irr: irr(cf),
    npv: npv(cf, v.rate / 100),
    moic: inflow / v.price,
    profit: inflow - v.price,
    payback,
    gross1: r1.rev / v.price,
    net1: r1.net / v.price,
    netShare: r1.rev > 0 ? r1.net / r1.rev : 0,
    leaseCut: v.lease > 0 && v.years > v.lease,
  };
}
export type VillaOut = ReturnType<typeof villa>;

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
      // Продажа ставится на чистый доход последнего года, между сегментами зазор 2px
      if (r.sale > 0) s += bar(x, r.net + (2 * (top - bot)) / ph, r.net + r.sale, 'vc-sale');
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
  return `<b>Год ${r.year}</b>`
    + `<span>Выручка</span><em>${usd(r.rev)}</em>`
    + `<span>Чистый доход</span><em>${usd(r.net)}</em>`
    + (r.sale > 0 ? `<span>Продажа</span><em>${usd(r.sale)}</em>` : '')
    + `<span>Накопленный итог</span><em>${usd(r.cum)}</em>`;
}

// Таблица кэшфлоу по годам (для чтения без графика)
export function villaTable(o: VillaOut) {
  const head = ['Год', 'Выручка', 'Площадки', 'УК', 'Содержание', 'Налоги', 'Чистый доход', 'Продажа', 'Поток', 'Накопленный итог'];
  const cell = (v: number) => (Math.abs(v) < 0.5 ? '—' : usd(v));
  let h = `<thead><tr>${head.map((c) => `<th scope="col">${c}</th>`).join('')}</tr></thead><tbody>`;
  o.rows.forEach((r) => {
    h += `<tr><th scope="row">${r.year === 0 ? 'Покупка' : r.year}</th>`
      + [r.rev, -r.ota, -r.mgmt, -r.opex, -r.tax, r.net, r.sale, r.cf, r.cum].map((v) => `<td>${cell(v)}</td>`).join('')
      + '</tr>';
  });
  return `${h}</tbody>`;
}

// ---------- 2. Рассрочка или скидка ----------
// Как в виджете инвестанализа: первый взнос сразу, остаток равными платежами в конце каждого месяца,
// ставка в месяц = годовая / 12.
export type InstIn = { price: number; down: number; months: number; rate: number; disc: number };
export const INST_DEFAULT: InstIn = { price: 300000, down: 30, months: 18, rate: 12, disc: 5 };

export function installment(v: InstIn) {
  const n = Math.max(1, Math.round(v.months));
  const r = v.rate / 100 / 12;
  const rest = v.price * (1 - v.down / 100);
  const pay = rest / n;
  const pv = v.price * (v.down / 100) + (r > 0 ? (pay * (1 - (1 + r) ** -n)) / r : rest);
  const even = 1 - pv / v.price; // скидка, равная рассрочке
  const cash = v.price * (1 - v.disc / 100); // полная оплата со скидкой
  return { pay, pv, even, cash, diff: cash - pv, months: n };
}

// ---------- 3. Дубли и ошибки ----------
// У клиентов Axiom дубли и ошибки, остановленные до оплаты, составили 3,55 млрд IDR, около 0,9% затрат.
// Вместе с двойными оплатами и завышенными ценами инциденты набирались на 4,7% объёма операций.
export const DUP_SHARE = 0.009;
export const INC_SHARE = 0.047;
export type DupIn = { spend: number; months: number };
export const DUP_DEFAULT: DupIn = { spend: 150000, months: 24 };

export function dupes(v: DupIn) {
  const m = Math.max(1, Math.round(v.months));
  return {
    month: v.spend * DUP_SHARE,
    total: v.spend * m * DUP_SHARE,
    incidents: v.spend * m * INC_SHARE,
    volume: v.spend * m,
    months: m,
  };
}

// Разбор числа из поля ввода: пробелы в разрядах, запятая как десятичный знак
export const parseNum = (s: string) => {
  const v = Number(s.replace(/[\s  $%]/g, '').replace(',', '.'));
  return Number.isFinite(v) ? v : NaN;
};
