// Снимки v12: node shot.cjs [scale]
const { chromium } = require('playwright');
const scale = Number(process.argv[2] || 1);
const dir = __dirname + '/';  // снимки кладёт рядом; нужен сервер: python3 -m http.server 4321 в nota/dist
(async () => {
  const b = await chromium.launch();
  const d = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: scale });
  await d.goto('http://localhost:4321/v12/', { waitUntil: 'networkidle' });
  await d.evaluate(() => document.fonts.ready);
  await d.waitForTimeout(300);
  const repTop = await d.evaluate(() => document.getElementById('result').getBoundingClientRect().top + scrollY);
  const pts = [0, Math.round(repTop - 520), Math.round(repTop - 20)];
  for (let i = 0; i < pts.length; i++) {
    await d.evaluate((y) => window.scrollTo({ top: y, behavior: 'instant' }), pts[i]);
    await d.waitForTimeout(500);
    await d.screenshot({ path: dir + `d${i}.png` });
  }
  const info = await d.evaluate(() => { const btn = document.querySelector('.hero .btn').getBoundingClientRect(); return { btnBottom: Math.round(btn.bottom + scrollY), sw: document.documentElement.scrollWidth }; });
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: scale });
  await m.goto('http://localhost:4321/v12/', { waitUntil: 'networkidle' });
  await m.evaluate(() => document.fonts.ready);
  await m.screenshot({ path: dir + 'm0.png' });
  const mi = await m.evaluate(() => { const btn = document.querySelector('.hero .btn').getBoundingClientRect(); const f = document.querySelector('.s-fig-rep').getBoundingClientRect(); return { btnBottom: Math.round(btn.bottom), fig: Math.round(f.top + scrollY), sw: document.documentElement.scrollWidth }; });
  await m.evaluate((y) => window.scrollTo({ top: y, behavior: 'instant' }), mi.fig - 380);
  await m.waitForTimeout(300);
  await m.screenshot({ path: dir + 'm1.png' });
  const a = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: scale });
  await a.goto('http://localhost:4321/v12/archive/', { waitUntil: 'networkidle' });
  await a.screenshot({ path: dir + 'a0.png' });
  console.log(JSON.stringify({ desktop: info, phone: mi, pts }));
  await b.close();
})();
