// Рендер HTML карточки в PNG: node render.cjs card.html card.png [масштаб]
// Вёрстка 1080 px, картинка в двойном разрешении (2160 px по ширине); масштаб 1 — 1080 px, для превью.
// Высота — по содержимому, но не меньше 1080 (квадрат); почти полная — ровно 1350; больше 1350 — ошибка (код 2).
// Нужен Playwright с Chromium: в этой папке npm install && npx playwright install chromium (см. package.json)
const { chromium } = require('playwright');
(async () => {
  const [src, out, sc] = process.argv.slice(2); const scale = Number(sc || 2);
  if (!src || !out) { console.error('usage: node render.cjs card.html card.png [scale]'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1800 }, deviceScaleFactor: scale });
  await p.goto(require('url').pathToFileURL(require('path').resolve(src)).href, { waitUntil: 'load' });   // пути с пробелами, # и % — тоже
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(100);
  // шрифт встроен в HTML; если он не загрузился, картинка выйдет другим шрифтом — лучше ошибка (код 3), чем тихая подмена
  const fontOk = await p.evaluate(() => { const ff = [...document.fonts].filter((f) => f.family.replace(/["']/g, '') === 'Inter');
    return ff.some((f) => f.status === 'loaded') && !ff.some((f) => f.status === 'error'); });
  if (!fontOk) { console.error('шрифт Inter не загрузился:', src); await b.close(); process.exit(3); }
  const H = await p.evaluate(() => {
    const r = document.querySelector('x-dc > div'); const nat = Math.ceil(r.getBoundingClientRect().height);
    if (nat > 1350) return -nat;
    const h = nat >= 1270 ? 1350 : Math.max(1080, nat); r.style.height = h + 'px'; return h;
  });
  if (H < 0) { console.error('карточка не влезает в 1350 px:', -H); await b.close(); process.exit(2); }
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: 1080, height: H } });
  await b.close(); console.log(out, 1080 * scale + '×' + H * scale);
})();
