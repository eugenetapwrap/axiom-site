# Рилсы Nota для Instagram (18.11)

Два вертикальных ролика 1080 × 1920, 30 кадров/с, H.264, без звука (тихая дорожка AAC — музыку добавить в Instagram).
Данные во всех кадрах выдуманные; тексты — утверждённые формулировки сайта v11 и бота.

| Файл | О чём | Длина | Обложка |
|---|---|---|---|
| `nota-reel-1-product.mp4` | О продукте: накладная в 9:41 → строка в таблице → дубль → оригинал в папке → отчёт по понедельникам → призыв | 25 с | `nota-reel-1-product-cover.png` |
| `nota-reel-2-report.mp4` | Об отчёте: «Куда ушли деньги за месяц?» → архив чата боту → карточка отчёта, камера по блокам → неделя и месяц → призыв | 26 с | `nota-reel-2-report-cover.png` |

Важный текст держится в безопасной зоне Instagram: сверху от 250 px, снизу до ~1500 px, справа не ближе 72 px от края.

## Как пересобрать
`reel1-product.html`, `reel2-report.html` — анимация с функцией `render(t)`; карточки отчётов в `assets/` собраны генератором (`../report-cards/generator`).
```
node render-video.cjs reel1-product.html nota-reel-1-product.mp4 25 3.0
node render-video.cjs reel2-report.html nota-reel-2-report.mp4 26 9.0
```
Нужны Node.js с Playwright (Chromium) и ffmpeg; последний аргумент — момент для обложки.
