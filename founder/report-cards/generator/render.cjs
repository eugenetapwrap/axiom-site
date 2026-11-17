// Рендер HTML карточки в PNG: node render.cjs card.html card.png
// Вёрстка 1080 px, картинка в двойном разрешении (2160 px по ширине).
// Высота — по содержимому, но не меньше 1080 (квадрат); почти полная — ровно 1350; больше 1350 — ошибка (код 2).
// Нужен Playwright с Chromium: npm i playwright && npx playwright install chromium
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  if (!src || !out) { console.error('usage: node render.cjs card.html card.png'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1800 }, deviceScaleFactor: 2 });
  await p.goto('file://' + require('path').resolve(src), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(100);
  const H = await p.evaluate(() => {
    const r = document.querySelector('x-dc > div'); const nat = Math.ceil(r.getBoundingClientRect().height);
    if (nat > 1350) return -nat;
    const h = nat >= 1270 ? 1350 : Math.max(1080, nat); r.style.height = h + 'px'; return h;
  });
  if (H < 0) { console.error('карточка не влезает в 1350 px:', -H); await b.close(); process.exit(2); }
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: 1080, height: H } });
  await b.close(); console.log(out, 2160 + '×' + H * 2);
})();
