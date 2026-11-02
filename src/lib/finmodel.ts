// Демо-проект для виджета «Финансовые модели»: три стратегии одного и того же объекта.
// Показатели (IRR, NPV, MOIC) не вписаны руками, а считаются из потоков,
// поэтому график и цифры всегда сходятся. Используется при сборке и в браузере.
//
// Объект: 48 апартаментов по 65 м², 3 120 м². Стройка 2026–2028.
// Продажа: 3 120 м² × 3 200 USD = 9,98 млн, минус 5% комиссии агентам ≈ 9,5 млн,
//   темп 4 юнита в месяц, значит всё продано за 2029 год. Затраты 6,2 млн.
// Аренда: те же затраты + 0,4 млн на мебель и оснащение = 6,6 млн.
//   NOI = 48 × 365 × 72% × 175 USD × 45% маржи ≈ 1,0 млн в год,
//   первый год разгон (0,65), дальше рост 3% в год. Объект не продаётся.
// Смешанный: аренда 2029–2035, в 2035 продажа объекта целиком
//   по ставке капитализации 10%: 1,15 млн NOI 2036 / 10% = 11,5 млн, минус 3% ≈ 11,15 млн.
//   Проверка: в 2029 та же ставка даёт 1,0 / 10% = 10 млн, это цена из сценария «Продажа».

import { smoothPath } from './smooth';

export const YEARS = [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035];
export const RATE = 0.12; // ставка дисконтирования для NPV

export type Strategy = 'sale' | 'rent' | 'mixed';
export type Inputs = { price: number; pace: number; mat: number; adr: number; occ: number; cap: number };
export type InputKey = keyof Inputs;
export type Scenario = { name: string; id: Strategy; keys: InputKey[]; cf: number[] }; // cf в млн USD

// Предпосылки, которые посетитель двигает ползунками. Базовые значения дают потоки из комментария выше.
export const BASE: Inputs = { price: 3200, pace: 4, mat: 6, adr: 175, occ: 72, cap: 10 };
export const INPUTS: Record<InputKey, { label: string; min: number; max: number; step: number; unit: string }> = {
  price: { label: 'Цена продажи, USD/м²', min: 2400, max: 4000, step: 100, unit: '' },
  pace: { label: 'Темп продаж, юнитов в месяц', min: 1, max: 8, step: 1, unit: '' },
  mat: { label: 'Рост цен на материалы, в год', min: 0, max: 20, step: 1, unit: '%' },
  adr: { label: 'Средний тариф, USD за ночь', min: 100, max: 260, step: 5, unit: '' },
  occ: { label: 'Загрузка', min: 40, max: 90, step: 1, unit: '%' },
  cap: { label: 'Продажа в 2035, ставка капитализации', min: 7, max: 14, step: 0.5, unit: '%' },
};
export const fmtInput = (k: InputKey, v: number) =>
  `${v.toLocaleString('ru-RU', { maximumFractionDigits: 1 }).replace(/\s/g, ' ')}${INPUTS[k].unit}`;

const UNITS = 48;
const AREA = 3120;
const COST_SALE = [-1.5, -2.7, -2.0];
const COST_RENT = [-1.6, -2.8, -2.2];
const NOI = [0.65, 0.92, 1.0, 1.03, 1.06, 1.09, 1.12];
const r2 = (v: number) => Math.round(v * 100) / 100;

// Затраты: половина стройки — материалы; база посчитана с ростом цен 6% в год
const costs = (base: number[], mat: number) =>
  base.map((c, t) => r2(c * (1 + 0.5 * (((1 + mat / 100) / 1.06) ** (t + 1) - 1))));

export function buildCF(id: Strategy, inp: Inputs): number[] {
  if (id === 'sale') {
    // 3 120 м² × цена − 5% комиссии; продажи с 2029 года, по 12 месяцев в году с заданным темпом
    const total = (AREA * inp.price * 0.95) / 1e6;
    const cf = [...costs(COST_SALE, inp.mat), 0, 0, 0, 0, 0, 0, 0];
    let left = UNITS;
    for (let y = 3; y < cf.length && left > 0; y++) {
      const u = Math.min(left, inp.pace * 12);
      cf[y] = r2((total * u) / UNITS);
      left -= u;
    }
    return cf;
  }
  // NOI = выручка номеров × 45% маржи, поэтому меняется пропорционально тарифу и загрузке
  const k = (inp.adr / 175) * (inp.occ / 72);
  const noi = NOI.map((v) => r2(v * k));
  const c = costs(COST_RENT, inp.mat);
  if (id === 'rent') return [...c, ...noi];
  // Продажа объекта в 2035: NOI следующего года / ставка капитализации, минус 3% расходов на сделку
  const exit = r2((r2(noi[noi.length - 1] * 1.03) / (inp.cap / 100)) * 0.97);
  return [...c, ...noi.slice(0, -1), r2(noi[noi.length - 1] + exit)];
}

const DEFS: { name: string; id: Strategy; keys: InputKey[] }[] = [
  { name: 'Продажа', id: 'sale', keys: ['price', 'pace', 'mat'] },
  { name: 'Аренда', id: 'rent', keys: ['adr', 'occ', 'mat'] },
  { name: 'Смешанный', id: 'mixed', keys: ['adr', 'occ', 'cap'] },
];
export const SCENARIOS: Scenario[] = DEFS.map((d) => ({ ...d, cf: buildCF(d.id, BASE) }));

export function npv(cf: number[], r = RATE) {
  return cf.reduce((s, c, t) => s + c / (1 + r) ** t, 0);
}

export function irr(cf: number[]) {
  let lo = -0.9;
  let hi = 2;
  for (let k = 0; k < 200; k++) {
    const mid = (lo + hi) / 2;
    if (npv(cf, lo) * npv(cf, mid) <= 0) hi = mid;
    else lo = mid;
  }
  return (lo + hi) / 2;
}

export function moic(cf: number[]) {
  const inv = -cf.filter((c) => c < 0).reduce((s, c) => s + c, 0);
  const ret = cf.filter((c) => c > 0).reduce((s, c) => s + c, 0);
  return ret / inv;
}

const num = (v: number, d: number) => v.toFixed(d).replace('.', ',').replace('-', '−');

export function kpis(cf: number[]) {
  const n = npv(cf);
  return {
    irr: `${num(irr(cf) * 100, 1)}%`,
    npv: `${num(n, 1)} млн`,
    moic: `${num(moic(cf), 2)}×`,
    npvNeg: n < 0,
  };
}

// Масштаб графика: ноль на 58% высоты, самый большой плюс занимает 56%.
// Масштаб не меньше базового, а если посетитель разогнал цифры ползунками — растёт вместе с ними.
export const ZERO = 58;
const SPAN = 56;
const BASE_MAX = Math.max(...SCENARIOS.flatMap((s) => s.cf));
export const cumulative = (cf: number[]) => {
  let c = 0;
  return cf.map((v) => (c = Math.round((c + v) * 100) / 100));
};
export const scaleFor = (cf: number[]) => Math.max(BASE_MAX, ...cf, ...cumulative(cf));
export const barHeight = (v: number, max = BASE_MAX) => `${((Math.abs(v) / max) * SPAN).toFixed(1)}%`;

// Накопленный итог (J-кривая) в том же масштабе, координаты 0–100 по ширине и высоте графика, линия сглажена
const cumY = (v: number, max: number) => ZERO - (v / max) * SPAN;
export function cumPath(cf: number[], max = BASE_MAX) {
  const pts: [number, number][] = [[0, ZERO], ...cumulative(cf).map((v, i) => [(i + 0.5) * 10, cumY(v, max)] as [number, number])];
  return smoothPath(pts, 2);
}
// Окупаемость: год, в котором накопленный итог впервые выше нуля, и точка пересечения нуля
export function payback(cf: number[]) {
  const cum = cumulative(cf);
  const i = cum.findIndex((v, k) => v > 0 && k > 0 && cum[k - 1] <= 0);
  if (i < 0) return null;
  const x = (i - 0.5 + (0 - cum[i - 1]) / (cum[i] - cum[i - 1])) * 10;
  return { year: YEARS[i], x };
}
export const barTitle = (year: number, v: number) =>
  `${year}: ${v > 0 ? '+' : v < 0 ? '−' : ''}${num(Math.abs(v), 2)} млн USD`;
