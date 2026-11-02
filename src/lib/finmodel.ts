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

export const YEARS = [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035];
export const RATE = 0.12; // ставка дисконтирования для NPV

export type Param = { label: string; value: string; p: number };
export type Scenario = { name: string; params: Param[]; cf: number[] }; // cf в млн USD

const NOI = [0.65, 0.92, 1.0, 1.03, 1.06, 1.09, 1.12];
const EXIT = 11.15;

export const SCENARIOS: Scenario[] = [
  {
    name: 'Продажа',
    params: [
      { label: 'Цена продажи, USD/м²', value: '3 200', p: 64 },
      { label: 'Темп продаж, юнитов в месяц', value: '4', p: 50 },
      { label: 'Рост цен на материалы, в год', value: '6%', p: 40 },
    ],
    cf: [-1.5, -2.7, -2.0, 9.5, 0, 0, 0, 0, 0, 0],
  },
  {
    name: 'Аренда',
    params: [
      { label: 'Средний тариф, USD за ночь', value: '175', p: 55 },
      { label: 'Загрузка', value: '72%', p: 72 },
      { label: 'Рост цен на материалы, в год', value: '6%', p: 40 },
    ],
    cf: [-1.6, -2.8, -2.2, ...NOI],
  },
  {
    name: 'Смешанный',
    params: [
      { label: 'Средний тариф, USD за ночь', value: '175', p: 55 },
      { label: 'Загрузка', value: '72%', p: 72 },
      { label: 'Продажа в 2035, ставка капитализации', value: '10%', p: 50 },
    ],
    cf: [-1.6, -2.8, -2.2, ...NOI.slice(0, -1), Math.round((NOI[NOI.length - 1] + EXIT) * 100) / 100],
  },
];

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
// Ниже нуля остаётся место для накопленного итога: яма вложений до −6,6 млн уходит на 88%.
export const ZERO = 58;
const SPAN = 56;
const maxPos = Math.max(...SCENARIOS.flatMap((s) => s.cf));
export const barHeight = (v: number) => `${((Math.abs(v) / maxPos) * SPAN).toFixed(1)}%`;

// Накопленный итог (J-кривая) в том же масштабе, координаты 0–100 по ширине и высоте графика
export const cumulative = (cf: number[]) => {
  let c = 0;
  return cf.map((v) => (c = Math.round((c + v) * 100) / 100));
};
const cumY = (v: number) => ZERO - (v / maxPos) * SPAN;
export function cumPath(cf: number[]) {
  const pts = cumulative(cf).map((v, i) => `${((i + 0.5) * 10).toFixed(1)},${cumY(v).toFixed(1)}`);
  return `M0,${ZERO} L${pts.join(' L')}`;
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
