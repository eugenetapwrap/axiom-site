// Данные и раскладка схемы движения денег (Sankey).
// Используется и при сборке (первый кадр), и в браузере (смена месяцев).
// Все цифры демонстрационные, млрд IDR в месяц.

export type SNode = { id: string; label: string; col: number; color: string };
export type SLink = { from: string; to: string };

export const NODES: SNode[] = [
  { id: 'p1', label: 'Вилла A', col: 0, color: '#5fa596' },
  { id: 'p2', label: 'Вилла B', col: 0, color: '#5fa596' },
  { id: 'p3', label: 'Апарт-отель', col: 0, color: '#5fa596' },
  { id: 'p4', label: 'Таунхаусы', col: 0, color: '#5fa596' },
  { id: 'p5', label: 'Прочие проекты', col: 0, color: '#9bb3ad' },
  { id: 'cash', label: 'Поступления', col: 1, color: '#5b93cf' },
  { id: 'g1', label: 'Строительство', col: 2, color: '#d9727b' },
  { id: 'g2', label: 'Операционные', col: 2, color: '#d9a548' },
  { id: 'g3', label: 'Инвестиции', col: 2, color: '#5b93cf' },
  { id: 'g4', label: 'Прирост остатка', col: 2, color: '#5fa596' },
  { id: 'c1', label: 'Материалы', col: 3, color: '#d9727b' },
  { id: 'c2', label: 'Работы подрядчиков', col: 3, color: '#d9727b' },
  { id: 'c3', label: 'Инжиниринг', col: 3, color: '#d9727b' },
  { id: 'c4', label: 'ФОТ и консалтинг', col: 3, color: '#d9a548' },
  { id: 'c5', label: 'Налоги', col: 3, color: '#d9a548' },
  { id: 'c6', label: 'Общие расходы', col: 3, color: '#d9a548' },
  { id: 'c7', label: 'Основные средства', col: 3, color: '#5b93cf' },
  { id: 'c8', label: 'Остаток на счетах', col: 3, color: '#5fa596' },
];

export const LINKS: SLink[] = [
  { from: 'p1', to: 'cash' },
  { from: 'p2', to: 'cash' },
  { from: 'p3', to: 'cash' },
  { from: 'p4', to: 'cash' },
  { from: 'p5', to: 'cash' },
  { from: 'cash', to: 'g1' },
  { from: 'cash', to: 'g2' },
  { from: 'cash', to: 'g3' },
  { from: 'cash', to: 'g4' },
  { from: 'g1', to: 'c1' },
  { from: 'g1', to: 'c2' },
  { from: 'g1', to: 'c3' },
  { from: 'g2', to: 'c4' },
  { from: 'g2', to: 'c5' },
  { from: 'g2', to: 'c6' },
  { from: 'g3', to: 'c7' },
  { from: 'g4', to: 'c8' },
];

export const MONTHS = [
  'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь',
];
export const MONTHS_SHORT = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'];

// Поступления по проектам: Вилла A распродаётся, Апарт-отель и Таунхаусы набирают ход.
const inflow = [
  [2.4, 2.1, 1.9, 1.8, 1.6, 1.5, 1.4, 1.3, 1.2, 1.2, 1.1, 1.1],
  [0.6, 0.8, 1.0, 1.2, 1.3, 1.4, 1.4, 1.3, 1.3, 1.2, 1.2, 1.4],
  [0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5],
  [0.1, 0.1, 0.15, 0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.9, 1.0, 1.0],
  [0.4, 0.3, 0.4, 0.3, 0.4, 0.4, 0.3, 0.4, 0.3, 0.4, 0.4, 0.5],
];
const invest = [0.12, 0.1, 0.04, 0.03, 0.02, 0.08, 0.03, 0.02, 0.06, 0.02, 0.03, 0.05];
const r2 = (v: number) => Math.round(v * 100) / 100;

// Значения потоков по месяцам в порядке LINKS.
export const SERIES: number[][] = MONTHS.map((_, m) => {
  const k = m / 11;
  const p = inflow.map((row) => row[m]);
  const total = p.reduce((s, v) => s + v, 0);
  const sBuild = 0.56 + 0.1 * Math.sin((Math.PI * m) / 11);
  const sOps = 0.17 - 0.02 * k;
  const sInv = invest[m];
  const g1 = r2(total * sBuild);
  const g2 = r2(total * sOps);
  const g3 = r2(total * sInv);
  const g4 = r2(total - g1 - g2 - g3);
  const c1 = r2(g1 * (0.58 - 0.08 * k));
  const c2 = r2(g1 * (0.28 + 0.06 * k));
  const c3 = r2(g1 - c1 - c2);
  const tax = m % 3 === 2 ? 0.32 : 0.22;
  const c4 = r2(g2 * 0.6);
  const c5 = r2(g2 * tax);
  const c6 = r2(g2 - c4 - c5);
  return [...p, g1, g2, g3, g4, c1, c2, c3, c4, c5, c6, g3, g4];
});

export const GEOM = { W: 1100, H: 520, PAD_T: 36, NODE_W: 10, GAP: 14, colX: [170, 430, 690, 900] };

const cols = [0, 1, 2, 3].map((c) => NODES.filter((n) => n.col === c));

function nodeValues(values: number[]) {
  const out: Record<string, number> = {};
  const inn: Record<string, number> = {};
  LINKS.forEach((l, i) => {
    out[l.from] = (out[l.from] ?? 0) + values[i];
    inn[l.to] = (inn[l.to] ?? 0) + values[i];
  });
  const v: Record<string, number> = {};
  NODES.forEach((n) => { v[n.id] = Math.max(out[n.id] ?? 0, inn[n.id] ?? 0); });
  return v;
}

// Масштаб один на все месяцы, чтобы было видно, как меняется объём.
const maxTotal = Math.max(...SERIES.map((vals) => {
  const v = nodeValues(vals);
  return Math.max(...cols.map((ns) => ns.reduce((s, n) => s + v[n.id], 0)));
}));
const { H, PAD_T, GAP, NODE_W, colX } = GEOM;
export const SCALE = (H - PAD_T - 10 - GAP * 7) / maxTotal;

export type Layout = {
  nodes: Record<string, { x: number; y: number; h: number; value: number }>;
  links: { d: string; value: number }[];
  total: number;
};

export function layout(values: number[]): Layout {
  const v = nodeValues(values);
  const nodes: Layout['nodes'] = {};
  const outY: Record<string, number> = {};
  const inY: Record<string, number> = {};
  for (const ns of cols) {
    const colH = ns.reduce((s, n) => s + v[n.id] * SCALE, 0) + GAP * (ns.length - 1);
    let y = PAD_T + (H - PAD_T - 10 - colH) / 2;
    for (const n of ns) {
      const h = v[n.id] * SCALE;
      nodes[n.id] = { x: colX[n.col], y, h, value: v[n.id] };
      outY[n.id] = y;
      inY[n.id] = y;
      y += h + GAP;
    }
  }
  const links = LINKS.map((l, i) => {
    const a = nodes[l.from];
    const b = nodes[l.to];
    const h = values[i] * SCALE;
    const x0 = a.x + NODE_W;
    const x1 = b.x;
    const y0 = outY[l.from];
    const y1 = inY[l.to];
    outY[l.from] += h;
    inY[l.to] += h;
    const mx = (x0 + x1) / 2;
    const f = (n: number) => n.toFixed(1);
    const d = `M${f(x0)},${f(y0)} C${f(mx)},${f(y0)} ${f(mx)},${f(y1)} ${f(x1)},${f(y1)} L${f(x1)},${f(y1 + h)} C${f(mx)},${f(y1 + h)} ${f(mx)},${f(y0 + h)} ${f(x0)},${f(y0 + h)} Z`;
    return { d, value: values[i] };
  });
  return { nodes, links, total: v.cash };
}

export const fmt = (v: number) => v.toFixed(1).replace('.', ',');

export function linkColor(l: SLink) {
  const src = NODES.find((n) => n.id === l.from)!;
  const dst = NODES.find((n) => n.id === l.to)!;
  return l.from === 'cash' ? dst.color : src.col === 0 ? src.color : dst.color;
}
