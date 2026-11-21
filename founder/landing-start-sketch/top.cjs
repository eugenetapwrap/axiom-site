// Снимок первого экрана: node top.cjs d out.png
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  await p.goto(`http://localhost:4322/${process.argv[2]}.html`, { waitUntil: 'networkidle' }); await p.screenshot({ path: process.argv[3] }); await b.close(); })();
