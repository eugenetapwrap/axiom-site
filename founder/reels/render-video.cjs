// Покадровый рендер HTML-анимации в MP4: node render-video.cjs reel.html out.mp4 секунды [обложка_сек ...]
// В странице должна быть функция window.render(t), которая выставляет состояние кадра на момент t (секунды).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path'), url = require('url');
(async () => {
  const [src, out, secs, ...covers] = process.argv.slice(2); const fps = 30, N = Math.round(Number(secs) * fps);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto(url.pathToFileURL(path.resolve(src)).href, { waitUntil: 'load' });
  await p.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map((i) => i.decode().catch(() => {}))); });
  for (const c of covers) { await p.evaluate((t) => window.render(t), Number(c)); await p.screenshot({ path: out.replace(/\.mp4$/, `-cover-${c}.png`) }); }
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p',
    '-r', String(fps), '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < N; i++) {
    await p.evaluate((t) => window.render(t), i / fps);
    const buf = await p.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise((r) => ff.on('close', r)); await b.close(); console.log(out, N, 'кадров');
})();
