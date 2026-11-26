# Технические правила для прототипов Axiom Consulting

Прототипы публикуются одним артефактом claude.ai из нескольких HTML-файлов. Главный файл `index.html` (обзор вариантов) делает координатор. Ты делаешь свои файлы в папке `/tmp/claude-0/-home-user-axiom-site/de8fefbc-96f8-5634-8943-ac0f3a366fca/scratchpad/axiom-site-proto/`.

## Каждый твой HTML-файл — самостоятельная страница
- Начинается с `<!doctype html>`, `<html lang="ru">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`, своим `<title>` (2–4 слова, например «Axiom — вариант A») и полным `<style>` (сброс: `*{box-sizing:border-box}`, `body{margin:0}`, `img{max-width:100%}`).
- Тема одна, светлая, выбрана сознательно: задай `background` у `body` и ВСЕ цвета явно через CSS-переменные в `:root`. Тёмную тему не делать. Добавь `<meta name="color-scheme" content="light">` и `:root{color-scheme:light}`.
- Внешние ресурсы разрешены ТОЛЬКО так: стили шрифтов с `https://fonts.googleapis.com` (файлы с fonts.gstatic.com) — у каждого шрифта реальный запасной стек. Скрипты при необходимости только с cdnjs.cloudflare.com с точной версией (лучше обойтись без библиотек). Никаких внешних картинок, иконок-шрифтов, iframe. Иллюстрации, схемы и графики — инлайновый SVG или CSS. Все шрифты должны иметь кириллицу (`subset` cyrillic + cyrillic-ext): Source Serif 4, Inter, Onest, IBM Plex Mono, Manrope, JetBrains Mono, Inter Tight, Spectral, Geist — с кириллицей; DM Sans, Space Grotesk, Fraunces, Instrument Sans, Figtree, Sora, Outfit, Work Sans, Plus Jakarta Sans, Gloock — НЕ использовать.
- Ссылки между страницами относительные: `index.html` (обзор), `a.html`, `b.html`, `c.html`, `audit.html`. Внешняя ссылка на Nota: `https://notagetbot.com/ru/` с `target="_blank" rel="noopener"`. Пункты меню, у которых нет страницы, ведут на якоря этой же страницы.
- В левом нижнем углу маленькая плавающая плашка «← Все варианты» (ссылка на `index.html`), с отступами `calc(16px + env(safe-area-inset-left,0px))` и `calc(16px + env(safe-area-inset-bottom,0px))`. Ненавязчивая.
- Форма: обработчик `submit` с `preventDefault()`, после отправки показать под кнопкой текст «Это прототип: заявка никуда не отправляется». У каждого поля стабильный `id` и `<label>`. Никаких `action`, `mailto:`, `alert()`.
- Адаптивность: страница работает на ширине 360–400px без горизонтальной прокрутки; боковые отступы `padding-left:max(16px, env(safe-area-inset-left,0px))` и `padding-right:max(16px, env(safe-area-inset-right,0px))` на внутренних обёртках секций; колонки складываются в одну; у текстовых детей flex/grid `min-width:0`. Липкая шапка (если есть) — `top: env(safe-area-inset-top, 0px)`.
- Доступность: видимый фокус, контраст текста не ниже 4,5:1, `prefers-reduced-motion` отключает анимации. Анимации — только из видимого состояния (контент не прячется в `opacity:0` до прокрутки).
- Цифры в таблицах: `font-variant-numeric: tabular-nums`. Заголовкам `text-wrap: balance`. Длина строки текста около 65 знаков.
- Не шаблонно: никаких эмодзи, иконок-клише, градиентов «фиолетовый → синий», одинаковых карточек с тенью везде, всего по центру. Нумерация 01/02 — только там, где это реальная последовательность (процесс, шаги). Структура должна нести смысл.
- Тексты и факты — ТОЛЬКО из `content.md`. Заглушки ⟦…⟧ оставлять видимыми и оформлять как заглушки.

## Проверка перед сдачей (один раз)
Сделай скриншоты Playwright (он установлен: `require('playwright')`, `chromium.launch()` без опций) своих страниц на ширине 1440 и 390 (полная страница), открыв файл через `file://`. Шрифты Google могут не загрузиться в песочнице — это нормально, проверяй вёрстку. Посмотри скриншоты, исправь найденное (переполнение, наложения, обрезанный текст, горизонтальная прокрутка — проверь `document.documentElement.scrollWidth <= innerWidth`) и больше не зацикливайся.

## Что вернуть
Короткий отчёт (до 150 слов): какие файлы сделаны, главная идея подачи, что осталось спорным. Скриншоты сохрани рядом как `<имя>-desktop.png` и `<имя>-mobile.png`.
