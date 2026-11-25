// Сборка бандлов главной на других языках: ru.json + переводы {lang}-strings.json → {lang}.json
//   node scripts/i18n-build.mjs en id
// ru.json выгружается из content-v12.ts скриптом scripts/i18n-dump.mts (после правок русских текстов — выгрузить заново и перевести новые строки).
import fs from 'node:fs';
const dir = new URL('../src/data/i18n/', import.meta.url);
const ru = JSON.parse(fs.readFileSync(new URL('ru.json', dir), 'utf8'));
const CYR = /[А-Яа-яЁё]/;

// Что зависит от языка, кроме текста: картинки, ссылки на документы, метки
const PER_LANG = (lang) => ({
  'meta.og': `/og-v12-${lang}.png`,
  'start.report.file': `/screens/report-month-${lang}-1080.webp`,
  'start.report.file2x': `/screens/report-month-${lang}-2160.webp`,
  'footer.terms': `/${lang}/terms`,
  'footer.privacy': `/${lang}/privacy`,
  'footer.refund': `/${lang}/refund`,
});

function setAt(obj, path, value) {
  const keys = path.split('.');
  let o = obj;
  for (const k of keys.slice(0, -1)) { if (!(k in o)) throw new Error('нет пути ' + path); o = o[k]; }
  const last = keys.at(-1);
  if (!(last in o)) throw new Error('нет пути ' + path);
  o[last] = value;
}
function walk(x, p, out) {
  if (Array.isArray(x)) x.forEach((v, i) => walk(v, [...p, i], out));
  else if (x && typeof x === 'object') Object.entries(x).forEach(([k, v]) => walk(v, [...p, k], out));
  else if (typeof x === 'string' && CYR.test(x)) out.push(p.join('.'));
  return out;
}

for (const lang of process.argv.slice(2)) {
  const tr = JSON.parse(fs.readFileSync(new URL(`${lang}-strings.json`, dir), 'utf8'));
  const b = structuredClone(ru);
  const need = walk(ru, [], []);
  const missing = need.filter((p) => !(p in tr));
  if (missing.length) throw new Error(`${lang}: нет перевода для ${missing.join(', ')}`);
  for (const p of need) setAt(b, p, tr[p]);
  // строки, скрытые на телефоне в сравнении, — те же, что в списке строк
  b.compare.mobileHide = ru.compare.mobileHide.map((s) => b.compare.rows[ru.compare.rows.indexOf(s)]);
  for (const [p, v] of Object.entries(PER_LANG(lang))) setAt(b, p, v);
  if (!b.start.title.includes(b.start.underline)) throw new Error(`${lang}: подчёркнутая часть не входит в заголовок`);
  const left = walk(b, [], []);
  if (left.length) throw new Error(`${lang}: осталась кириллица: ${left.join(', ')}`);
  fs.writeFileSync(new URL(`${lang}.json`, dir), JSON.stringify(b, null, 2) + '\n');
  console.log(lang, 'ok:', need.length, 'строк');
}
