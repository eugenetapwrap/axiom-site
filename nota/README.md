# Лендинг Nota — nota.axiomco.io

Отдельный сайт на [Astro](https://astro.build), одна страница на русском. Структура и тексты — `../founder/landing.md`, макет — холст «Nota, эскизы», страница «Лендинг».

## Запуск

```bash
cd nota
npm install
npm run dev      # http://localhost:4321
npm run build    # готовый сайт в nota/dist/
```

## Где что

- `src/data/content.ts` — **все тексты**. Править здесь.
- `src/pages/index.astro` — порядок блоков.
- `src/styles/global.css` — цвета и шрифты (токены в `:root`).
- `src/components/MiniReport.astro` — упрощённая карточка отчёта на демо-данных. Заменить на скриншоты настоящих карточек, когда будут.
- `public/og.png` — картинка-превью, когда ссылку пересылают в Telegram.

Каждая кнопка ведёт в бота с меткой источника: `t.me/NotaGetBot?start=land_hero`, `land_offer`, `land_price_start` и т. д. Бот должен записывать этот параметр, чтобы было видно, какой блок приводит людей.

## Публикация на nota.axiomco.io

Vercel (или Cloudflare Pages):
1. Import project → репозиторий `axiom-site`.
2. **Root Directory: `nota`**. Фреймворк Astro определится сам.
3. Domains → добавить `nota.axiomco.io`.
4. У регистратора axiomco.io добавить DNS-запись **CNAME `nota` → адрес, который покажет Vercel** (обычно `cname.vercel-dns.com`).

## Перед запуском

- Ссылки на соглашение и политику в подвале (`footer` в `content.ts`) — сейчас `#`.
- Скриншоты таблицы и сообщений бота — добавить, когда будут.

## Скриншоты таблицы и аналитики

Лежат в `public/screens/`, показываются во вкладках блока «Таблица и аналитика». Тестовые данные.

| Файл | Лист |
|---|---|
| `payments.webp` | Payments |
| `monthly-spend.webp` | Monthly spend |
| `insights.webp` | Insights |

Чтобы заменить, положите файл с тем же именем и поправьте размеры `w` и `h` в `src/data/content.ts` (блок `analytics`). Если файла нет, на его месте будет заглушка.
