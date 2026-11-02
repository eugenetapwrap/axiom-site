// Демо для виджета «Инвестиционный анализ»: покупка объекта со скидкой за полную оплату или в рассрочку.
// Рассрочка сравнивается по приведённой стоимости: первый взнос сразу, остаток равными платежами
// в конце каждого месяца, ставка дисконтирования 12% годовых (как в финмоделях).
// Доходность аренды = NOI / цена покупки по выгодному варианту; окупаемость — после налога 10%
// с ростом NOI 3% в год. Все цифры демонстрационные, млн USD.

export const RATE = 0.12;
export const TAX = 0.1;
const GROWTH = 0.03;

export type Offer = { name: string; price: number; down: number; noi: number; disc: number; months: number };
export const OFFERS: Offer[] = [
  { name: 'Апартаменты', price: 1.5, down: 0.3, noi: 0.11, disc: 10, months: 24 },
  { name: 'Вилла', price: 2.9, down: 0.2, noi: 0.24, disc: 6, months: 36 },
  { name: 'Таунхаус', price: 1.05, down: 0.4, noi: 0.07, disc: 8, months: 18 },
];
export const DISC = { min: 0, max: 20, step: 1 };
export const MONTHS = { min: 6, max: 48, step: 6 };

export function compare(o: Offer, disc: number, months: number) {
  const a = o.price * (1 - disc / 100);
  const r = RATE / 12;
  const pay = (o.price * (1 - o.down)) / months;
  const b = o.price * o.down + (pay * (1 - (1 + r) ** -months)) / r;
  const win: 'a' | 'b' = a <= b ? 'a' : 'b';
  const best = Math.min(a, b);
  const yld = o.noi / best;
  const net = yld * (1 - TAX);
  const pb = Math.log(1 + GROWTH / net) / Math.log(1 + GROWTH);
  return { a, b, win, yld, pb, wa: (a / o.price) * 100, wb: (b / o.price) * 100 };
}

const n = (v: number, d: number) => v.toFixed(d).replace('.', ',');
export const fmtMln = (v: number) => `${n(v, 2)} млн`;
export const fmtPct = (v: number) => `${n(v * 100, 1)}%`;
export const fmtYears = (v: number) => `${n(v, 1)} года`;
