// Геометрия фирменного мотива «Нити» в первом экране.
// Поступления проектов сходятся в один счёт и расходятся по статьям; месяц за месяцем портфель растёт.
// Одна функция строит кадр и при сборке (январь), и в браузере (смена месяцев).
import { dec } from './i18n';
import { NODES, LINKS, SERIES } from './sankey';

export const TG = {
  W: 1200,
  H: 330,
  K: 12, // px на 1 млрд IDR
  CY: 190,
  PX: 560, // планка счёта
  NW: 3,
  X1: 400, // конец прямых участков слева
  X2: 720, // начало прямых участков справа
  LSTEP: 46,
  RSTEP: 32,
  LMAX: 240,
  RMAX: 300,
};

const label = (id: string) => NODES.find((n) => n.id === id)!.label;
const PROJ = LINKS.map((l, i) => ({ l, i })).filter(({ l }) => l.to === 'cash');
const COST = LINKS.map((l, i) => ({ l, i })).filter(({ l }) => /^c\d+$/.test(l.to));

export const PROJ_NAMES = PROJ.map(({ l }) => label(l.from));
export const COST_NAMES = COST.map(({ l }) => label(l.to));
export const PROJ_COLORS = PROJ.map((_, k) => `var(--th-${k + 1})`);
export const COST_COLORS = COST.map((_, k) => `var(--th-${k + 1})`);

// Длина прямого участка считается от максимума за год: видно, как проекты набирают ход
const maxP = Math.max(...SERIES.flatMap((v) => PROJ.map(({ i }) => v[i])));
const maxC = Math.max(...SERIES.flatMap((v) => COST.map(({ i }) => v[i])));

export type Thread = { v: number; h: number; y: number; x: number; d: string; len: number };
export type Frame = { left: Thread[]; right: Thread[]; total: number; top: number };

const f = (n: number) => n.toFixed(1);

export function frame(values: number[]): Frame {
  const { K, CY, PX, NW, X1, X2, LSTEP, RSTEP, LMAX, RMAX } = TG;
  const p = PROJ.map(({ i }) => values[i]);
  const c = COST.map(({ i }) => values[i]);
  const total = p.reduce((s, v) => s + v, 0);
  const top = CY - (total * K) / 2;

  let acc = top;
  const left = p.map((v, k) => {
    const h = v * K;
    const y = CY + (k - (p.length - 1) / 2) * LSTEP;
    const x = X1 - (v / maxP) * LMAX;
    const yb = acc + h / 2;
    acc += h;
    const len = X1 - x + Math.hypot(PX - X1, yb - y);
    return { v, h, y, x, len, d: `M${f(x)},${f(y)} L${X1},${f(y)} C${X1 + 82},${f(y)} ${X1 + 78},${f(yb)} ${PX},${f(yb)}` };
  });

  acc = top;
  const right = c.map((v, k) => {
    const h = v * K;
    const y = CY + (k - (c.length - 1) / 2) * RSTEP;
    const x = X2 + (v / maxC) * RMAX;
    const ya = acc + h / 2;
    acc += h;
    const len = Math.hypot(X2 - PX, y - ya) + (x - X2);
    return { v, h: Math.max(h, v > 0 ? 1.4 : 0), y, x, len, d: `M${PX + NW},${f(ya)} C${PX + 80},${f(ya)} ${X2 - 78},${f(y)} ${X2},${f(y)} L${f(x)},${f(y)}` };
  });

  return { left, right, total, top };
}

export const fmt2 = (v: number) => dec(v, 2);
