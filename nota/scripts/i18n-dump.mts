// Выгрузка всех текстов главной (v12, вариант start) в один JSON — основа для переводов EN/ID.
//   npx tsx scripts/i18n-dump.mts > src/data/i18n/ru.json
import { start, hero, nav, steps, analytics, shotAlt, send, what12, segments, pricing, facts12, sched12, compare12, data12, faq12, final, footer } from '../src/data/content-v12';
const plans = pricing.plans.map(({ feats, ...p }) => p);
const bundle = {
  meta: start.meta,
  start: { ...start, meta: undefined },
  hero: { qr: hero.qr },
  nav,
  tableLead: steps.table.lead,
  analytics: { screens: analytics.screens, tabs: analytics.tabs, note: analytics.note },
  shotAlt,
  send: { title: send.title, items: send.items },
  what: { title: what12.title, items: what12.items },
  segments: { title: segments.title, items: segments.items },
  pricing: { title: pricing.title, lead: pricing.lead, billing: pricing.billing, common: pricing.common, plans },
  facts: facts12,
  sched: sched12,
  compare: { title: compare12.title, whenLabel: compare12.whenLabel, rows: compare12.rows, mobileHide: compare12.mobileHide, options: compare12.options },
  data: { title: data12.title, items: data12.items, who: data12.who },
  faq: faq12,
  final: { title: final.title, lead: final.lead },
  footer: { terms: footer.terms, privacy: footer.privacy, refund: footer.refund, testData: footer.testData },
};
process.stdout.write(JSON.stringify(bundle, null, 2));
