// Снимки эскизов: node shots.cjs (нужен сервер: python3 -m http.server 4321 в nota/dist, и второй на 4322 в этой папке)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const scale = Number(process.env.SCALE || 2);
  const list = process.argv.slice(2).length ? process.argv.slice(2) : ['a', 'b', 'c', 'd'];
  for (const v of list) {
    const p = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: scale });
    await p.goto(`http://localhost:4322/${v}.html`, { waitUntil: 'networkidle' });
    await p.screenshot({ path: `shots/${v}-desktop.png`, fullPage: true });
    const w = await p.evaluate(() => document.documentElement.scrollWidth);
    await p.close();
    const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: scale });
    await m.goto(`http://localhost:4322/${v}.html`, { waitUntil: 'networkidle' });
    await m.screenshot({ path: `shots/${v}-phone.png`, fullPage: false });
    const mw = await m.evaluate(() => document.documentElement.scrollWidth);
    console.log(v, 'desktop width', w, 'phone width', mw);
    await m.close();
  }
  await b.close();
})();
