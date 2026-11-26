# Axiom Consulting: бенчмарк структуры и дизайна сайтов

Дата исследования: 26.11.2026.
Для кого: сайт Axiom Consulting. Это бутиковый финансовый консалтинг для девелопмента и строительства в Юго-Восточной Азии, ОАЭ и Центральной Азии. Услуги: финмоделирование, аудит моделей, управленческий учёт и контроль платежей, инвестиционный анализ, аутсорсинг CFO. Отдельно есть продукт: Telegram-бот, который переносит чеки в Google Sheets. Сайт запускается на русском, английская версия появится позже.

## Как собраны данные

- Каждую страницу я скачивал напрямую. Структуру брал из HTML: заголовки h1–h4, навигация, формы, `hreflang`. Шрифты и цвета взяты из CSS и подключённых файлов шрифтов. Если в тексте есть hex-код, значит он встречается в CSS сайта.
- Скриншотов нет: CDN с картинками из моей среды недоступны. Поэтому про изображения я пишу только то, что видно по разметке: есть ли видео, какие у картинок пропорции и что на них подписано. Стиль фотографий и иллюстраций я не оценивал.
- Кириллицу у Google Fonts проверял через API `fonts.googleapis.com/css2`: смотрел, какие наборы символов отдаются для каждого шрифта.
- Цифры клиентов и рейтинги на чужих сайтах — это заявления самих компаний. Я их не проверял.

### Какие сайты удалось открыть

| Группа | Сайт | Статус |
|---|---|---|
| Референсы клиента | https://www.anthropic.com/ , https://onlytraffic.com/ | открыты, разобраны подробно |
| Крупные консультанты и советники | https://www.bain.com/ , https://www.oliverwyman.com/ , https://www.kroll.com/en , https://www.fticonsulting.com/ , https://www.lazard.com/ , https://www.evercore.com/ | открыты |
| Недвижимость и стройка (смежные) | https://www.turnerandtownsend.com/ , https://www.jll.com/en-us/ , https://www.knightfrank.com/ | открыты |
| Тихий стиль частного банка | https://www.pictet.com/us/en , https://www.centerviewpartners.com/ | открыты |
| Бутики: моделирование, CFO, бэк-офис | https://www.gridlines.com/ , https://www.cfocentre.com/ae/ , https://www.graphitefinancial.com/ | открыты |
| Мультиязычность в Центральной Азии | https://gratanet.com/ | открыт |
| B2B-финтех, известный ясностью | https://stripe.com/ , https://mercury.com/ , https://ramp.com/ | открыты |
| Не удалось проверить | McKinsey, BCG, Alvarez & Marsal, Rothschild & Co, Houlihan Lokey (hl.com), Operis, F1F9, Cavendish Maxwell, Kruze | сайты закрыты защитой от ботов (403, пустой ответ или страница-проверка). В отчёт они **не включены**. |
| Исключён | https://runway.com/ | домен принадлежит Runway ML (генерация видео), а не FP&A-сервису. Для задачи не подходит. |

Внутренние страницы Kroll и FTI тоже вернули 403. Их сервисные страницы не разобраны.

---

## 1. Короткие выводы

1. **Сильные бутики пишут на первом экране обещание результата, а не название услуги.** У Gridlines это «The numbers behind your deal have to hold. We make sure they do.» (https://www.gridlines.com/). Сразу под ним стоят две кнопки: «Tell us about your project» и «Or ask a question».
2. **Цены и сроки на странице услуги — главное отличие бутика от крупных фирм.** В FAQ страницы аудита Gridlines прямо названы вилки: comfort review $16–20k, full audit $32–40k. Там же: первая обратная связь через 3–4 дня, фиксированная цена, итерации не оплачиваются (https://www.gridlines.com/financial-model-audit/). Крупные консультанты цен не показывают.
3. **Доказательство работы — «кейс плюс две цифры».** Bain подписывает каждую историю клиента блоком «The impact» с двумя метриками, например «$300M saved over two years / 2.5x stock price increase» для EPC-подрядчика (https://www.bain.com/). FTI подписывает кейсы исходом: «VALUE RECOVERED», «FUNDS RECOVERED» (https://www.fticonsulting.com/). Инвестбанки показывают сделки «плашками» с ролью и суммой: Evercore, «Featured Transactions (Values in Millions)» (https://www.evercore.com/).
4. **В премиальном сегменте типографика держится на паре «засечный заголовок + гротеск».** Так у Bain (Graphik + Tiempos), Mercury (Arcadia + Tiempos), Knight Frank (Suisse Intl + Tiempos Headline), Turner & Townsend (Inter + Publico Headline), Lazard (Lazard Sans + VC Garamond), Pictet (Lardy Sans + Lardy Serif) и Anthropic (собственные Serif, Sans и Mono).
5. **Фон всё чаще тёплый белый, а не чистый #FFF.** Anthropic: `#faf9f5` и `#f0eee6`. Mercury: бежевая шкала от `#f6f5f2`. Ramp: `#f4f2f0`. Oliver Wyman: `#f7f3ee`. Pictet: `#f7f7f2`. Акцентный цвет обычно один.
6. **Референсы клиента устроены по-разному.** Anthropic — спокойная редакционная подача: крупная засечка, много воздуха, лента датированных новостей, без логотипов клиентов. OnlyTraffic — продуктовая прозрачность: каждый формат подаётся как цена «от», три пункта и одна кнопка. Есть метрики, FAQ на каждой странице и чат с выбором намерения и полем «Telegram, WhatsApp».
7. **Мессенджеры почти не встречаются.** Telegram и WhatsApp я увидел только у OnlyTraffic (поле контакта в чат-виджете) и ссылки на Telegram-каналы у OnlyTraffic и GRATA. Встроенный календарь (Calendly и подобные) не встретился ни на одной проверенной странице. CFO Centre собирает заявку на звонок через форму HubSpot.
8. **Мультиязычность делают тремя способами.** Первый — подпапка и `hreflang` (OnlyTraffic `/ru`, Bain, Kroll, Stripe). Второй — матрица «страна × язык» (GRATA: Казахстан EN/Қазақ/Русский, ОАЭ EN/Русский; Pictet; CFO Centre). Третий — окно выбора рынка (Knight Frank: «52 markets and 25 languages»). Чего избегать, видно у OnlyTraffic: в RU-версии часть заголовков осталась на английском.
9. **С кириллицей у Google Fonts нужно быть внимательным.** Популярные DM Sans, Space Grotesk, Instrument Sans/Serif, Fraunces, Newsreader, Figtree, Sora, Outfit и Work Sans кириллицы не имеют. У Gloock (стоит на CFO Centre), Plus Jakarta Sans и Hanken Grotesk есть только расширенный набор `cyrillic-ext` (U+0460–052F). Базовых русских букв в нём нет.

---

## 2. Референсы клиента: подробный разбор

### 2.1. anthropic.com

**Главная, секции по порядку** (https://www.anthropic.com/):
1. Хедер: News · Research · Policy · Commitments · Company (выпадающие меню), поиск, кнопка «Try Claude».
2. H1, который работает как манифест: «AI research and products that put safety at the frontier.» Под ним абзац из двух предложений о миссии.
3. Hero-блок флагманского продукта: H2 с названием модели, одна строка пользы, кнопки «Read more» и «Try Claude». В разметке есть фоновое `<video muted playsInline>` с постером.
4. Лента «Announcements» с датами. Каждая карточка: дата, заголовок, одна строка пользы, ссылки «Model Details», «System Card · View» и «Read announcement».
5. «Learn more»: четыре карточки-документа (The Anthropic Institute, Claude's Constitution, Responsible Scaling Policy, Core views on AI safety). Картинки в них вертикальные, 640×800.
6. Футер: 9 колонок (Research, Policy, Commitments, Company, Products, Models, Solutions, Help and security, Terms and policies), блок «Our mission», «Log in».

**Страница продукта** (https://www.anthropic.com/claude/opus):
H1 с названием → Announcements (история версий) → **Availability and pricing** → Use cases (5 сценариев, среди них «Financial analysis») → Benchmarks → Trust and safety → Safeguards → Hear from our customers → FAQ («When should I use…», «How much does it cost…»).
Эту схему почти без изменений можно взять для страницы Telegram-бота.

**Страница компании** (https://www.anthropic.com/company):
Our Purpose (4 тезиса) → The Team (4 функции) → What we value and how we act (7 ценностей одной строкой каждая) → Governance (совет директоров) → призыв присоединиться.

**Типографика.** Три собственных семейства: Anthropic Serif, Anthropic Sans и Anthropic Mono (файлы `AnthropicSerif_*`, `AnthropicSans_*`, `AnthropicMono_*` на главной). В CSS sans используется 432 раза, serif 301 раз, mono 71 раз. Размер текста плавный: через `clamp(...)` между мобильным и десктопным значением. Крупные заголовки задаются как `clamp(40px,5.6vw,80px)`. Ширина текстовой колонки ограничена `max-width:720px`. Сетка в 12 колонок, контейнер до 1280–1400px. Для цифр включены `tabular-nums`.

**Цвета** (токены из CSS):
- Ivory: `#faf9f5` (ivory-light), `#f0eee6` (ivory-medium), `#e8e6dc` (ivory-dark).
- Slate: `#141413` (slate-dark), `#3d3d3a`, `#5e5d59`.
- Cloud: `#b0aea5`, `#d1cfc5`.
- Акцент clay: `#d97757`; для интерактивных элементов `#c6613f`.
- Вспомогательные: oat `#e3dacc`, olive `#788c5d`, sky `#6a9bcc`.
- Отдельная палитра для графиков: `--chart-*`, около 10 цветов.

Фон каждой секции задаётся темой (`.theme-ivory`, `.theme-slate`, `.theme-black` и т. д.), поэтому светлые и тёмные блоки чередуются.

Важная деталь: `#d97757` на `#faf9f5` даёт контраст всего 2,96:1, а `#c6613f` даёт 3,85:1. То есть clay служит цветом поверхностей и декора. Мелкий текст им набирать нельзя.

**Движение.** Ключевые кадры `word-rise`, `unblur`, `fade-in`, `reveal`, `scrollcue`, `drift-x/y/zoom`. Слова заголовка проявляются по одному, медиа медленно дрейфует, есть подсказка к прокрутке. Переходы короткие: `color .2s ease-out`, `opacity .25–.3s`. В CSS 65 правил `prefers-reduced-motion`. Скругления маленькие: 2px, 4px и шаги сетки.

**Доказательства.** Опубликованные документы (system cards, политики), количественные заявления в анонсах и регулярные датированные публикации. Логотипов клиентов на главной нет.

**Почему сайт кажется ясным и дорогим:**
- одна мысль на экран;
- вместо декора — иерархия шрифтов;
- тёплый нейтральный фон и один акцент;
- засечка задаёт серьёзный тон, гротеск отвечает за интерфейс;
- короткие строки (до 720px);
- спокойное движение с уважением к reduced motion;
- доказательства в виде документов, а не громких лозунгов.

**Что взять Axiom:**
- H1-манифест плюс абзац;
- ленту «Что нового» с датами (кейсы, статьи, обновления бота);
- раздел принципов (независимость, стандарт моделирования, конфиденциальность), аналог Commitments;
- структуру продуктовой страницы для бота;
- чередование тем секций;
- мелкие радиусы.

**Чего не брать:**
- узнаваемую связку ivory + clay + засечка, иначе сайт будет похож на AI-компанию;
- отсутствие цен и сроков, которое для B2B-бутика хуже;
- серые подписи мелким кеглем.

### 2.2. onlytraffic.com

> Контекст. Судя по мета-тегам самого сайта, это партнёрская платформа трафика для OnlyFans («OnlyFans Promotion & Marketing…», https://onlytraffic.com/). Сайт годится как образец структуры и интерфейса. Публично ссылаться на него как на референс Axiom не стоит.

**Главная, секции по порядку** (https://onlytraffic.com/):
1. Хедер с выпадающими меню:
   - Work Formats: CPL / CPC / RevShare / Shoutouts;
   - Getting Started: How It Works / Pricing / Documentation;
   - Tools (Free): калькулятор, трекинг-ссылки;
   - Resources: Case Studies / Blog / Contact.

   Справа переключатель продуктов (Partners / Studio / Accounts), «Log In» и «Get Started».
2. Hero. H1 «Creator Promotion», под ним H2 одной фразой с тремя моделями оплаты: «Pay per subscriber, click or revenue share.» Основная кнопка «Start Promoting» и отдельная ссылка для второй аудитории: «I'm a marketer / media buyer →».
3. Три карточки форматов: «Fixed Price Per Subscriber», «Pay Per Click», «Pay From Fan Revenue». В каждой одна фраза, три пункта («Prices from $0.50 per subscriber…»), кнопка и картинка интерфейса шириной 728px.
4. Бесплатные инструменты: Cross-promo, Shoutouts, Tracking Links. У каждого две ссылки: «Free» и «How … works».
5. «Key metrics»: $80 Avg. Paying Fan Spend · 500+ Traffic Experts · $1.48 Avg. Cost Per Subscriber · 7.5M+ Transactions Analyzed.
6. Кейсы, где цифра стоит прямо в заголовке: «+30% Revenue in a Month… (3,670 Fans, Zero Ad Spend)».
7. «Built for Multi-Model Agencies»: четыре нумерованных шага с картинками `agency-step-1…4`.
8. Блок для соло-авторов, затем «AI Assistant, MCP and API» (документация).
9. «What Our Clients Say»: отзывы с именем, датой и источником, ссылка на Trustpilot.
10. Два повторных CTA-блока, «Frequently Asked Questions» (9 вопросов), «Latest Articles».
11. «Sign up for a free consultation»: форма с полями Name, Contact, Subject (выпадающий список), Message и согласием.
12. Футер, плюс ссылка на Telegram-канал `t.me/onlytraffic_news`.

Плавающий чат «Ask about traffic» предлагает выбрать намерение: «I want traffic for my models» или «I have traffic and want to earn». Затем кнопка «Leave a contact for a manager» с полем ввода, где подсказка начинается с «Telegram, WhatsApp…». Тексты чата переведены на EN, RU, UA, ES и DE.

**Страница услуги** (https://onlytraffic.com/cpl):
1. H1 = формат + обещание: «a fixed price for every new subscriber».
2. Цены по источникам.
3. «How a CPL order works».
4. «What you pay for and what comes back»: шесть гарантий отдельными H3, например «Undelivered fans are not charged» и «Unused balance can be refunded».
5. «How CPL fans pay back».
6. Сравнение «CPL, CPC or RevShare».
7. FAQ.
8. «Start with two or three sources».
9. Отзывы, статьи, форма.

**Страница цен** (https://onlytraffic.com/pricing): пакеты от $499 → текущие цены по источникам → скидки за уровень → минимальный заказ и стартовые бюджеты (три сценария) → FAQ по ценам → форма.

**Мультиязычность.** В `hreflang` указаны en, ru (`/ru`) и x-default. Шрифт Manrope размещён на собственном сервере в четырёх наборах: latin, latin-ext, cyrillic, cyrillic-ext. Минус: в RU-версии часть H2 осталась на английском («Cross-promo, Shoutouts and Tracking Links», «AI Assistant, MCP and API», https://onlytraffic.com/ru). Цены и страница pricing на русском отдельно не размечены.

**Визуал.**
- Цвета, самые частые hex в CSS: тёмно-синий `#0a2540`, синий `#4791ff`, серый текст `#697585`, светло-голубой фон `#edf4ff`, оранжевый акцент `#ff6833`, зелёный `#2fad7d`.
- Шрифт: только Manrope. Чаще всего вес 600, затем 500. Кегли 14/16/18/22/32px.
- Радиус 8px, у кнопок-«таблеток» 100px и 999px. Мягкие тени `0 12px 13px 7px rgba(231,231,231,.5)`.
- Движение почти отсутствует: только слайдеры (swiper, fancybox).
- `#4791ff` на белом даёт 3,11:1, то есть для мелкого текста не проходит AA.

**Почему сайт ясный:**
- у каждого формата есть цена, три пункта и одна кнопка;
- цифры в метриках, кейсах и заголовках;
- одинаковый «хвост» на каждой странице: FAQ, отзывы, статьи, форма;
- две аудитории разведены уже на первом экране;
- инструменты как бесплатный лид-магнит;
- в мессенджере можно написать без формы.

**Что взять Axiom:**
- подачу услуг как форматов работы;
- шаблон страницы услуги;
- страницу цен;
- чат с выбором намерения и полем «Telegram / WhatsApp»;
- бесплатные инструменты (калькулятор стоимости аудита, шаблоны);
- блок продукта с документацией.

---

## 3. Анатомия главной: остальные сайты

| Сайт | Первый экран | Секции по порядку (кратко) | Как показаны услуги | Как показаны доказательства |
|---|---|---|---|---|
| Bain, https://www.bain.com/ | карусель из четырёх материалов | Карусель → «We champion the bold…» с квизом из двух вопросов (отрасль → задача → Submit) → «Bold steps forward»: 4 истории клиентов → AI-блок → Latest Insights → «What can we help you achieve? LET'S GET TO WORK» → карьера → подписка | мега-меню Industries / Consulting Services; квиз | «Featured client success story», под каждой «The impact» и две метрики |
| Oliver Wyman, https://www.oliverwyman.com/index.html | баннер «Oliver Wyman is now part of the new, expanded Marsh brand», карусель «Transformative moments, shaped by AI» | Карусель → абзац позиционирования → Client Story (Experian) → «Featured perspectives» 01–03 → карьера → Contact Us | меню + выбор региона | одна большая история клиента, пронумерованные материалы |
| Kroll, https://www.kroll.com/en | «Stay Ahead with Kroll» и абзац «first firm called when decisions are complex…» | Hero-слайдер (4) → «Kroll In The News» (CNBC, WSJ, Bloomberg, FT) → вкладки Valuation / Risk / Transactions со списками решений → три линии бизнеса → «Our Scale and Reach» → футер с выбором региона и подпиской | вкладки по этапам жизненного цикла сделки | цифры: 6,500 experts, 30+ countries, «6 out of 10 Fortune 500»; упоминания в СМИ |
| FTI, https://www.fticonsulting.com/ | ротация H1: «Real-world experience that delivers.», «Steady Advisers for an Unsteady Age» | Hero → блоки по аудиториям («For the Strategic CFO», «For the Private Equity Leader») → 7 историй успеха → Most Popular Insights → News | мега-меню Services (21) и Industries (18, среди них «Construction, Projects & Assets», «Real Estate») | кейсы с меткой исхода (REPUTATION RESTORED, FUNDS RECOVERED) |
| Lazard, https://www.lazard.com/ | новостная карусель | Новости → «Three global businesses, one commitment…» → письмо CEO «Lazard 2030» → Our Businesses | мега-меню About / Expertise / People / News & Insights / Careers; верхняя строка IR / Media / Alumni | позиционирование, собственные исследования (LCOE+) |
| Evercore, https://www.evercore.com/ | «Client-Focused, Values-Driven.» и бегущая строка ценностей | Who We Are с четырьмя цифрами (~2,600 employees, 1995, 16 countries, $5T+) → Thought Leadership → Core Values (видео) → Our Founding (видео) → News → «Featured Transactions (Values in Millions)» | меню | плашки сделок: роль («Lead Financial Advisor») и сумма |
| Centerview, https://www.centerviewpartners.com/ | «Unparalleled Strategic Advice» | Hero → цифры (No.1 private IB, 25% of the 50 largest companies, $5T, 20 years) → What We Do → «Select Assignments» с фильтром M&A / Activism / Special Committee / Restructuring → команда → сообщество → карьера | 4 направления текстом | фильтруемый список сделок |
| Pictet, https://www.pictet.com/us/en | «How do you like your calm? Before, during or after the storm?» | Hero → «Select your profile» (Institutional / US Offshore / Private banking) → «Since 1805 / 220 years» → Insights / In the media → About → Responsibility | выбор профиля клиента | история, интервью партнёров |
| Turner & Townsend, https://www.turnerandtownsend.com/ | «We transform together.» и абзац | Hero → «Key facts» (23k+ people, 63 countries, 19 sectors, 30k+ projects) → смешанная лента Insights / News / Projects → вакансии | мега-меню Services (9) и Sectors (19) | цифры, проекты с подписями фото, собственный «Data centre construction cost index» |
| JLL, https://www.jll.com/en-us/ | карусель «Global Real Estate Perspective» | Карусель → «Explore a brighter way» → AI → «Illuminating insights…» → More to explore | меню Properties / Services / Technology / People / Insights / Industries / About, плюс Client stories | исследования, истории клиентов |
| Knight Frank, https://www.knightfrank.com/ | промо-баннер отчёта | «Find us where you are» → «Our global reach» → «Our property solutions» (6) → лид-блоки для разных аудиторий → карьера | мега-меню «Global solutions»: by expertise / by property type / by region; «Book a consultation» в хедере | охват (52 рынка), флагманские отчёты |
| Gridlines, https://www.gridlines.com/ | H1 «Project finance advisory and financial modelling for energy and infrastructure.» и «The numbers behind your deal have to hold. We make sure they do.» | Hero с двумя CTA и чипами 4 услуг → «Trusted on the deals that have to close» → «Straight answers on high-stakes deals» → цифры ($100bn, 2nd Infralogic H1 2026) → 4 услуги → «Why finance leaders choose Gridlines» (боль, ответ, цитата Masdar) → Recent projects → Latest insights с авторами → 6 офисов (в том числе Dubai и Singapore) → подписка («Join 35,492 financial modellers…») | 4 карточки, в каждой фраза результата и «Explore …» | цифры, именная цитата клиента, проекты (отрасль, дата, страна, клиент) |
| CFO Centre UAE, https://www.cfocentre.com/ae/ | H1 с вращающимися словами («cash flow management / profit optimisation / … exit maximisation») и тремя бейджами (Top 1% of CFO applicants · Flexible, affordable model · Immediate start) | Hero → 5 направлений → истории клиентов → «Struggling with Cash flow? Time? Scaling?…» → цифры (750+ CFOs, 18 countries) и телефон → команда (CFO с фото) → «Book a discovery call» → FAQ | 5 карточек по задачам (Exit Planning, Profit Improvement, Improve Cash Flow…) | 1320 active clients, истории, местная статистика со ссылкой на источник |
| Graphite Financial, https://www.graphitefinancial.com/ | «Outsourced Accounting and Finance for VC-Backed Startups» и «Accurate monthly close. Clear runway. Investor-ready reporting.» | Hero со списком из 5 услуг → «Built for What's Next» → 6 карточек услуг → 3 выгоды → «Graphite works inside your company. Not at arm's length.» → FAQ → «Get started today!» | карточка = H3 + жирный подзаголовок результата («Strategic FP&A & Capital Modeling») + абзац | позиционирование, «hundreds of leadership teams» |
| GRATA, https://gratanet.com/ | новостной слайдер | Новости → цифры (28 countries, 34 years, 280+ professionals, 16 050+ clients, 47 000+ projects) → новости и рейтинги (IFLR1000) | меню Industry sectors / Practice areas (в том числе Construction & Infrastructure, Real Estate, Project Finance & PPP) | цифры, рейтинги |
| Stripe, https://stripe.com/ | «Financial infrastructure to grow your revenue…», «Get started» и «Sign up with Google» | Решения → «The backbone of global commerce» (135+ currencies, $1.9T, 99.999% uptime, 200M+ subscriptions) → сегменты (enterprise / startup / platform), у каждого кейс с цифрами → для разработчиков → «What's happening» | по сегментам клиента | крупные метрики, кейсы с цифрами |
| Mercury, https://mercury.com/ | «Radically different banking», поле e-mail, «Open account», «Launch demo», «Contact sales» | Hero → 4 направления продукта → «Loved by 450K+…» с отзывами по сегментам (SaaS / Ecommerce / Agency) → фичи → «$1B in annualized revenue and 4+ years profitable» → дисклеймеры | 4 направления, у каждого цифра выгоды | отзывы с именами основателей, финансовые показатели самой компании |
| Ramp, https://ramp.com/ | «Time is money. Save both.» и поле e-mail | Соцдоказательство (85,000 companies) → платформа → **«See recommendations for your business»**: выбор боли («Chasing receipts / Approving spend / Closing the books…») → «Systems that never spoke» → продукт → **«We've got the receipts.»** (отзывы) | по задачам финансовой команды | отзывы с именем, должностью и компанией; среди авторов есть Fractional CFO |

---

## 4. Навигация

**Верхний уровень меню у консультантов:**
- Bain: Industries · Consulting Services · Insights · About · Careers, все пункты с мега-меню (https://www.bain.com/).
- FTI: Services · Industries · Digital · Insights · Our Experts · Our Impact · Careers · About (https://www.fticonsulting.com/).
- Lazard: About Us · Our Expertise · Our People · News & Insights · Careers (https://www.lazard.com/).
- Turner & Townsend: What we do · Who we are · Join us · Locations · Contact (https://www.turnerandtownsend.com/).
- Gridlines: What we do · Training courses · Locations · About us · Insights · Contact (https://www.gridlines.com/).
- Centerview: About · Capabilities · Transactions · Team · News · Careers · Community · Contact (https://www.centerviewpartners.com/).

**Как устроены мега-меню:**
- Две оси «Услуги × Отрасли»: Bain, FTI.
- Три оси «по экспертизе / по типу объекта / по региону»: Knight Frank. Это близко к задаче Axiom, где есть услуги, тип объекта и география.
- В меню встроены анонсы («Featured Expertise» у Lazard, «Featured topics» у Bain).
- В меню сразу лид-магнит: Gridlines, «Using AI for financial modelling: Receive your free 8-step guide».

**Служебная строка над основным меню:** Investor Relations / Media Relations / Alumni у Lazard; «Contact us · Hotlines» у Kroll (https://www.kroll.com/en).

**Кнопка в хедере:** «Book a consultation» у Knight Frank, «Get Started» и «Log In» у OnlyTraffic, «Try Claude» у Anthropic, «See a demo» и «Get started» у Ramp.

**Регион и язык:**
- Список регионов и языков: Oliver Wyman (Global; Africa, India, Middle East; Americas; Asia Pacific с «Southeast Asia (English)»; Europe). FTI (страна + язык, в том числе «United Arab Emirates English» и «Saudi Arabia English»).
- Окно настроек сайта: Knight Frank («We are present in 52 markets and 25 languages», среди рынков UAE, Singapore, Vietnam, Thailand, Malaysia, Indonesia, Philippines, Cambodia). Pictet (Americas / Asia Pacific / Europe / Middle East, локали en-AE и en-SG).
- Матрица «страна × язык»: GRATA. Kazakhstan: English / Қазақ / Русский. Uzbekistan, Kyrgyzstan, Tajikistan, UAE: English / Русский. Mongolia: English / Монгол (https://gratanet.com/).
- Подпапки и `hreflang`: Bain (8 языков), Kroll (9 локалей), JLL (34 локали, в том числе en-ae, en-sg, en-th, en-vn, en-my, en-id, en-ph), Stripe (89 значений hreflang, в том числе en-AE, en-SG, en-TH, en-MY), CFO Centre (17 страновых версий, в том числе en-AE, en-SG, zh-HK), OnlyTraffic (en, ru).

---

## 5. Анатомия страницы услуги

**Лучший образец по теме — аудит моделей у Gridlines** (https://www.gridlines.com/financial-model-audit/):
1. H1 «Financial model audit services» и подзаголовок о срочности. CTA «Tell us about your project» и «Or see our case studies».
2. «Trusted by industry leaders to complete $8bn+ of financial model audits».
3. «A model audit with all the rigour. None of the headaches.»
4. Три пары «боль → решение»: «Why choose to endure weeks of delay…» → «first feedback in just 3-4 DAYS». «unpredictable iteration charges» → «fixed-fee model audit». «old fashioned issue lists» → «live shared issues list».
5. Цитата клиента с именем и должностью.
6. «Two levels of review»: таблица Comfort review против Full model audit по строкам Model Logic, Documents и т. д.
7. «Why Gridlines?», затем «Numbers that speak for themselves». Судя по разметке, счётчики анимируются: в исходном HTML стоят нули.
8. «You're in safe hands» с историей фирмы.
9. Недавние проекты (страна, клиент, дата), команда, статьи, офисы.
10. **FAQ с ценами и сроками**: стоимость, длительность, comfort review против full audit, методология (cell-by-cell или shadow build), оплата итераций, уровень страхования профессиональной ответственности, присутствие в списках одобренных аудиторов у кредиторов.
11. Подписка и форма «Tell us about your project» с именными контактами экспертов.

**Другие варианты:**
- Продуктовая страница OnlyTraffic (https://onlytraffic.com/cpl): цены → процесс → «что входит и какие гарантии» → окупаемость → сравнение форматов → FAQ → CTA → отзывы → форма.
- Продуктовая страница Anthropic (https://www.anthropic.com/claude/opus): версии → доступность и цены → сценарии → бенчмарки → безопасность → клиенты → FAQ.
- Отраслевая страница Bain (https://www.bain.com/industry-expertise/construction-infrastructure/): H1 и подзаголовок «A new blueprint…» → «Our Experience» с двумя цифрами (720+ construction and EPC engagements, 110+ due diligence projects) → длинный текст → интерактивная схема стадий «Industrial Design & Construction» → AI в отрасли → Client Results → Experts → Insights → How We Can Help → «Ready to talk?».
- Сервисная страница Turner & Townsend (https://www.turnerandtownsend.com/what-we-do/services/cost-and-commercial-management/): 4 тезиса ценности (hidden value, unique data resource, independence, joined-up approach) → проекты → статьи → смежные услуги → подписка.
- CFO Centre (https://www.cfocentre.com/ae/our-expertise/strategic-planning/): вопрос-боль «Is your business plan still fit for purpose?» → как помогаем → «Strategy without execution is just a dream» → форма «Schedule your free discovery call» с полем «Where are you now, and what would you like to achieve?» и бесплатным телефоном → смежные услуги.

**Шаблон страницы услуги для Axiom** (собран из перечисленного):
1. H1 = результат для клиента + одна строка «для кого» (девелопер, генподрядчик, инвестор, банк). Две кнопки: «Обсудить проект» и «Написать в Telegram».
2. «Когда это нужно»: 3–5 ситуаций (подача в банк, вход инвестора, перерасход бюджета стройки).
3. «Что вы получаете»: результаты списком (модель, отчёт, письмо о проверке, дашборд).
4. «Как проходит работа»: шаги со сроками в днях и неделях.
5. «Форматы и стоимость»: 2–3 уровня с вилкой цены или условиями «от» (как у Gridlines) либо модель работы (фикс / абонемент / почасовая).
6. Сравнение уровней в таблице.
7. Кейс (кейсы): объект, страна, задача, две цифры результата.
8. «Стандарты и гарантии»: методология, конфиденциальность (NDA), ответственность, сколько итераций входит.
9. FAQ: цена, сроки, что нужно от клиента, языки, валюты, юрисдикции.
10. Статьи по теме и итоговая форма с полем «Telegram / WhatsApp / e-mail».

---

## 6. Как доказывают экспертизу

- **Цифры фирмы** (4 штуки, крупно):
  - Kroll: 6,500 experts / 30+ countries / 6 of 10 Fortune 500 (https://www.kroll.com/en);
  - Evercore: ~2,600 / 1995 / 16 / $5T+ (https://www.evercore.com/);
  - Turner & Townsend: 23k+ / 63 / 19 / 30k+ (https://www.turnerandtownsend.com/);
  - GRATA: 28 / 34 / 280+ / 16 050+ / 47 000+ (https://gratanet.com/);
  - Stripe: 135+ / $1.9T / 99.999% / 200M+ (https://stripe.com/).

  Бутику выгоднее цифры по сути работы: сколько моделей проверено, общий объём профинансированных проектов, сколько стран. Так делает Gridlines: $8bn+ model audits, 2nd в Infralogic.
- **Кейс + две метрики:** Bain (https://www.bain.com/). **Метка исхода:** FTI (https://www.fticonsulting.com/). **Цифра в заголовке кейса:** OnlyTraffic (https://onlytraffic.com/blog/case-studies).
- **Плашки сделок и проектов:** Evercore пишет роль и сумму. Centerview даёт фильтр по типу. Gridlines указывает отрасль, дату, страну и клиента.
- **Именные отзывы:** Gridlines (Ismail Chakour, Head of Structured Finance, Masdar), Ramp (имя, должность, компания), Mercury (основатели с названием компании).
- **Люди:** CFO Centre показывает карточки CFO и «View all our CFOs». Gridlines указывает в форме конкретных людей (Associate Director, Director) с e-mail. Bain добавляет блок «Our … Experts» на отраслевой странице.
- **Квалификация и рамки ответственности:** в FAQ Gridlines есть страхование профессиональной ответственности, списки одобренных аудиторов, методология. Anthropic публикует system cards и политики.
- **Аналитика как доказательство:** собственные индексы (Turner & Townsend, «Data centre construction cost index»; Lazard, «LCOE+»), статьи с автором и датой (Gridlines), подписка с числом подписчиков («Join 35,492 financial modellers…»).
- **Упоминания в СМИ:** «Kroll In The News» (CNBC, WSJ, Bloomberg, FT).

---

## 7. Визуальные тренды

**Типографика:**

| Сайт | Шрифты (из CSS / файлов шрифтов) |
|---|---|
| Bain | Graphik (sans) + Tiempos / Tiempos Headline + Reckless Neue |
| Mercury | Arcadia / Arcadia Display + Tiempos Headline + IBM Plex Mono |
| Knight Frank | Suisse Intl + Tiempos Headline |
| Turner & Townsend | Inter + Publico Headline |
| Lazard | Lazard Sans + VC Garamond |
| Pictet | Lardy Sans + Lardy Serif |
| Oliver Wyman | Noto Sans + MMC Display + Marsh Serif |
| Anthropic | Anthropic Sans + Serif + Mono |
| CFO Centre | DM Sans + Gloock (у обоих нет базовой кириллицы) |
| Kroll | Inter + Nunito Sans + Roboto Mono |
| Ramp | Lausanne + IBM Plex Sans / Mono |
| Stripe | Söhne + Source Code Pro |
| OnlyTraffic, Graphite | Manrope |
| Gridlines | Montserrat + Roboto (+ Roboto Slab, Poppins) |
| Centerview | Roboto + Roboto Slab |

Выводы:
- В премиальном сегменте заголовки чаще засечные.
- У финтеха засечек нет, но цифры в интерфейсе и таблицах набраны моноширинным шрифтом (Mercury, Ramp, Stripe, Anthropic, Kroll).

**Цвет:**
- Тёплые светлые фоны: Anthropic `#faf9f5`, Mercury `#f6f5f2`, Ramp `#f4f2f0`, Oliver Wyman `#f7f3ee`, Pictet `#f7f7f2`.
- Глубокие тёмные цвета: Oliver Wyman `#000f47`, Evercore `#002037`, OnlyTraffic `#0a2540`, Kroll `#001424`.
- Один акцент: Bain `#cc0000`, Pictet `#d12a46`, Anthropic `#d97757`, OnlyTraffic `#ff6833`, Ramp лаймовый `#f5ff78`.

**Изображения** (по разметке):
- Фоновое видео с постером в hero: Anthropic, Mercury.
- Картинки интерфейса продукта: OnlyTraffic (`format-cpl-728.webp`, `agency-step-*.webp`), Mercury.
- Фото проектов с указанием автора: Turner & Townsend, «Image courtesy: ©Marc A. Hermann».
- Архивные изображения к истории фирмы: Pictet, 220 лет.
- Данные и отчёты как самостоятельный визуальный контент: индексы Turner & Townsend и Lazard.
- Интерактивная схема стадий строительства: Bain.

**Воздух и сетка:** у Anthropic текстовая колонка 720px и 12-колоночная сетка. Почти все премиальные сайты держат одну мысль на экран. Плотная многоколоночная вёрстка встречается в мега-меню и футере.

**Движение:**
- Anthropic: слова заголовка проявляются по одному, лёгкий дрейф медиа, переходы 0,15–0,3s, полная поддержка reduced motion.
- Bain, FTI, JLL, Kroll: карусели в hero.
- OnlyTraffic: почти без движения.
- Gridlines: счётчики цифр.

**Скругления:** Anthropic 2–4px, Bain 0–4px, OnlyTraffic 8px плюс кнопки-«таблетки». Чем строже бренд, тем меньше радиус.

---

## 8. CTA и сбор заявок

| Приём | Где | Комментарий для Axiom |
|---|---|---|
| Основной и мягкий CTA рядом: «Tell us about your project» + «Or ask a question» | https://www.gridlines.com/ | снижает порог входа, взять обязательно |
| Именные эксперты в форме заявки | https://www.gridlines.com/ | у бутика партнёр и есть продукт |
| «Book a discovery call» + форма «Where are you now, and what would you like to achieve?» + бесплатный телефон | https://www.cfocentre.com/ae/ , https://www.cfocentre.com/ae/our-expertise/strategic-planning/ | вопрос «где вы сейчас» удобен для CFO-аутсорса |
| «Book a consultation» в хедере | https://www.knightfrank.com/ | постоянная кнопка |
| Квиз «отрасль → задача» | https://www.bain.com/ | можно сделать «тип объекта → задача → страна» |
| Выбор боли «What would you like to spend less time on?» → рекомендации | https://ramp.com/ | для бота и управленческого учёта («Сбор чеков», «Согласование платежей», «Закрытие месяца») |
| Поле e-mail прямо в hero | https://mercury.com/ , https://ramp.com/ | бутику подходит слабо, лучше кнопка Telegram |
| Чат-виджет с выбором намерения и полем «Telegram, WhatsApp» | https://onlytraffic.com/ | взять: для ОАЭ, ЮВА и Центральной Азии это естественный канал (рекомендация, не наблюдение) |
| Telegram-канал в футере | https://onlytraffic.com/ , https://gratanet.com/ | канал с разборами, кейсами и обновлениями бота |
| Подписка с числом подписчиков | https://www.gridlines.com/ | после набора базы |
| Бесплатные инструменты как лид-магнит | https://onlytraffic.com/ (Calculator, Menu Maker), https://www.gridlines.com/ (гайд, бесплатный курс) | калькулятор стоимости аудита, шаблон бюджета стройки, чек-лист для подачи в банк |

Встроенный календарь (Calendly и подобные) не встретился ни на одном проверенном сайте. CFO Centre собирает заявки на звонок через форму HubSpot.

---

## 9. Мультиязычность: что делать Axiom

1. **Адреса.** Русский как основной язык в корне (`/`), английский в `/en/`. Взаимные `hreflang` (`ru`, `en`) и `x-default`. Адреса страниц латиницей и одинаковые в обеих версиях (`/services/model-audit`, `/en/services/model-audit`). Так устроены подпапки у OnlyTraffic, Bain и Kroll.
2. **Без частичного перевода.** Страница либо переведена целиком, либо не публикуется в этой версии. Обратный пример: смешанные заголовки на https://onlytraffic.com/ru.
3. **Переключатель.** Простой «RU / EN» в хедере. Если позже появятся страновые акценты (ОАЭ, Казахстан, Узбекистан, Вьетнам и т. д.), подойдёт матрица «регион × язык», как у https://gratanet.com/ и https://www.pictet.com/us/en.
4. **Шрифт с `cyrillic-ext`.** На случай казахского и других языков Центральной Азии нужны Ә Ғ Қ Ң Ө Ұ Ү Һ І. Все шрифты, рекомендованные ниже, отдают и `cyrillic`, и `cyrillic-ext`. Наличие конкретных казахских глифов перед запуском нужно проверить на тестовой строке.
5. **Длина текста.** Русские строки на 15–25% длиннее английских. Кнопки и бейджи должны выдерживать перенос. Ширина колонки 640–720px.
6. **Числа и валюты.** Разделители по локали: «1 250 000» в RU, «1,250,000» в EN. Валюта явно: USD, AED, KZT, UZS, VND и т. д. В таблицах табличные цифры или моноширинный шрифт.

---

## 10. Шрифты Google Fonts: проверка кириллицы

Данные получены через `fonts.googleapis.com/css2` 26.11.2026.

| Шрифт | Наборы символов | Вывод |
|---|---|---|
| Inter, Inter Tight | cyrillic, cyrillic-ext, greek, latin, latin-ext, vietnamese | подходит |
| Manrope | cyrillic, cyrillic-ext, greek, latin, latin-ext, vietnamese | подходит (стоит на OnlyTraffic) |
| Onest | cyrillic, cyrillic-ext, latin, latin-ext, vietnamese | подходит |
| Golos Text | cyrillic, cyrillic-ext, latin, latin-ext | подходит (нет vietnamese) |
| Geist, Geist Mono | cyrillic, cyrillic-ext, latin, latin-ext, vietnamese | подходит |
| IBM Plex Sans / Serif / Mono | cyrillic, cyrillic-ext, latin, latin-ext, vietnamese | подходит |
| Source Serif 4 | cyrillic, cyrillic-ext, greek, latin, latin-ext, vietnamese; ось opsz 8–60 | подходит |
| Literata | cyrillic, cyrillic-ext, greek, latin, latin-ext, vietnamese | подходит |
| Spectral | cyrillic, cyrillic-ext, latin, latin-ext, vietnamese | подходит |
| EB Garamond | cyrillic, cyrillic-ext, greek, latin, latin-ext, vietnamese | подходит |
| PT Serif / PT Sans | cyrillic, cyrillic-ext, latin, latin-ext | подходит |
| Lora | cyrillic, cyrillic-ext, latin, latin-ext, vietnamese | подходит |
| JetBrains Mono, Roboto Mono, Source Code Pro | cyrillic, cyrillic-ext… | подходит |
| Playfair Display | cyrillic, latin, latin-ext, vietnamese (нет cyrillic-ext) | для русского годится, для казахского проверить |
| Jost, Tenor Sans | cyrillic без cyrillic-ext | то же |
| Gloock, Plus Jakarta Sans, Hanken Grotesk | только cyrillic-ext (U+0460–052F) | **не подходит**: нет базовых русских букв |
| DM Sans, Space Grotesk, Instrument Sans, Instrument Serif, Fraunces, Newsreader, Figtree, Bricolage Grotesque, Sora, Outfit, Urbanist, Lexend, Albert Sans, Public Sans, Archivo, Work Sans, Crimson Pro, Libre Baskerville, Syne | без кириллицы | **не подходит** |

---

## 11. Три направления дизайна

Все палитры проверены на контраст WCAG. Пары «текст / фон», указанные ниже, проходят AA для обычного текста (не ниже 4,5:1), если не оговорено иное.

### Направление A. «Тёплая редакционная ясность» (из anthropic.com)

**Идея.** Спокойная редакционная подача, как у исследовательской лаборатории: крупный засечный тезис, тёплый светлый фон, мало цвета, а доказательства — в датированных материалах и прозрачных принципах.

**Референсы:**
- https://www.anthropic.com/
- https://www.anthropic.com/claude/opus
- https://mercury.com/
- https://www.turnerandtownsend.com/
- https://www.bain.com/industry-expertise/construction-infrastructure/

**Палитра.** Акцент сознательно не clay, как у Anthropic, а темнее: так он проходит контраст и не копирует их.

| Роль | Hex | Проверка |
|---|---|---|
| Фон | `#FAF8F3` | |
| Фон секций | `#F1EDE4` | |
| Основной текст | `#1C1B19` | 16,2:1 на фоне |
| Вторичный текст | `#5F5C55` | 6,3:1 на фоне, 5,7:1 на фоне секций |
| Линии | `#DAD5CA` | |
| Акцент (ссылки, кнопки) | `#A8461F` | 5,6:1 на фоне; белый текст на нём 5,9:1 |
| Цвет данных и графиков | `#2F6B5E` | 5,8:1 |
| Тёмная секция | фон `#1C1B19`, текст `#FAF8F3`, акцент `#E08A5F` | 6,5:1 |

**Шрифты:**
- Заголовки: **Source Serif 4**, начертания 600 и 400, оптический размер для дисплея.
- Текст и интерфейс: **Inter** 400/500. Альтернатива с более «русским» характером: **Onest**.
- Цифры и таблицы: **IBM Plex Mono** 400/500.

Кириллица (`cyrillic` и `cyrillic-ext`) есть у всех трёх.

**Главная страница:**
1. Хедер: Услуги · Отрасли и география · Кейсы · Аналитика · Продукт · О нас · RU/EN · «Обсудить проект».
2. H1-тезис засечкой и абзац из двух предложений. Две кнопки: «Обсудить проект» и «Написать в Telegram».
3. «Что нового»: три датированные карточки (кейс, статья, обновление бота).
4. Услуги списком из пяти строк (без иконок). В строке: название, результат одной фразой, ссылка.
5. «Как мы работаем»: четыре шага со схемой (данные → модель → проверка → решение).
6. Кейсы: три карточки «объект · страна · две цифры результата», как «The impact» у Bain.
7. Продукт: Telegram-бот, сцена «чек → строка в Google Sheets».
8. Принципы: независимость, стандарт моделирования, конфиденциальность (аналог Commitments).
9. Команда: партнёры с фото и квалификацией.
10. Аналитика: статьи с автором и датой.
11. Финальный CTA с формой и контактами (Telegram, WhatsApp, e-mail).
12. Футер с колонками.

**Страница услуги.** Шаблон из раздела 5. Блок «Форматы и стоимость» оформлен как «Availability and pricing» у Anthropic. Тёмная секция для кейса.

**Изображения.** Собственные линейные схемы: структура модели, водопад денежного потока, график освоения бюджета. Архитектурная фотография строящихся объектов дозированно, в одном тоне. Без стоковых «рукопожатий».

**Движение.** Заголовок проявляется по словам, при прокрутке лёгкий fade и unblur на 0,2–0,3s, обязательно `prefers-reduced-motion`.

**Риски:**
- Сайт может выглядеть как копия AI-компании, если взять ivory и засечку без своего акцента и своих схем.
- Нужен регулярный контент: лента «Что нового» с датами полугодовой давности выглядит заброшенной.
- Засечная кириллица в мелком кегле читается хуже, поэтому засечку оставить для заголовков от 28px.
- Конверсия ниже, чем в направлении B, если не добавить цены и сроки.

### Направление B. «Прозрачный продукт» (из onlytraffic.com, Gridlines, Ramp и Stripe)

**Идея.** Консалтинг подаётся как понятный продукт: каждая услуга — формат с ценой «от», сроком, тремя пунктами и одной кнопкой. Цифры, калькуляторы и интерфейс бота стоят на виду, связаться можно в Telegram в один клик.

**Референсы:**
- https://onlytraffic.com/
- https://onlytraffic.com/cpl
- https://onlytraffic.com/pricing
- https://www.gridlines.com/financial-model-audit/
- https://ramp.com/

**Палитра:**

| Роль | Hex | Проверка |
|---|---|---|
| Фон | `#FFFFFF` | |
| Фон карточек и секций | `#F2F6FC` | |
| Основной текст | `#0B2240` | 15,9:1 |
| Вторичный текст | `#55657A` | 6,0:1 на белом, 5,5:1 на фоне карточек |
| Линии | `#DCE3EE` | |
| Основной (кнопки, ссылки) | `#2158D9` | белый текст на нём 6,1:1. Синий OnlyTraffic `#4791ff` даёт только 3,1:1, поэтому взят темнее |
| Акцент | `#FF6A3D` | только для плашек и графиков, текст на нём тёмный `#0B2240` (5,6:1). Белый на оранжевом 2,85:1, использовать нельзя |
| Успех | `#157A52` | 5,3:1 |

**Шрифты:**
- Всё на **Manrope** (заголовки 700/600, текст 400/500). Он же стоит на OnlyTraffic, кириллица в Google Fonts полная.
- Цифры, цены, таблицы: **JetBrains Mono** 500.
- Альтернатива для заголовков: **Onest** 600.

**Главная страница:**
1. Хедер с выпадающими меню:
   - Услуги (5);
   - Продукт (бот);
   - Цены;
   - Кейсы;
   - Ресурсы (статьи, шаблоны, калькуляторы).

   Справа RU/EN, «Открыть бота», «Обсудить проект».
2. Hero: H1 с результатом. Подзаголовок с тремя форматами работы: проект, аудит, абонемент CFO. Основная кнопка и ссылка для второй аудитории, например «Я из банка или фонда →».
3. Полоса доверия: страны и типы клиентов (девелоперы, подрядчики, фонды).
4. Карточки услуг как форматы: «от … USD», «от … дней», три пункта, кнопка.
5. Четыре цифры.
6. «Как это работает»: четыре шага с картинками интерфейса (модель, отчёт аудита, дашборд контроля платежей).
7. Интерактив: калькулятор ориентировочной стоимости аудита модели. Gridlines в FAQ объясняет, что цена зависит от числа уникальных формул и объёма проверки. Второй вариант — выбор боли, как у Ramp.
8. Кейсы с цифрой в заголовке.
9. Продукт: бот за три шага (фото чека → распознавание → строка в Google Sheets), кнопка «Открыть в Telegram».
10. Отзывы с именем, должностью и компанией.
11. FAQ.
12. Форма консультации и плавающий чат с выбором намерения («Нужна модель / аудит», «Нужен CFO / учёт», «Вопрос по боту») и полем «Telegram / WhatsApp / e-mail».

**Страница услуги** (по схеме OnlyTraffic /cpl и Gridlines):
1. H1 с результатом.
2. Таблица форматов и цен.
3. «Как проходит» с днями.
4. «Что входит, что получаете, гарантии»: 4–6 H3.
5. Сравнение уровней (как comfort review и full audit).
6. Кейсы.
7. FAQ с ценой и сроками.
8. CTA, отзывы, статьи, форма.

**Страница «Цены»** по схеме https://onlytraffic.com/pricing: пакеты → вилки по услугам → минимальный объём и старт → FAQ.

**Изображения.** Интерфейсы и макеты: фрагменты моделей с размытыми данными, графики, экраны бота. Иконки линейные. Фото людей только в разделе «Команда».

**Движение.** Минимальное: hover и состояния кнопок. Счётчики цифр без перебора и с reduced motion.

**Риски:**
- Сайт похож на SaaS и теряет ощущение «старшего советника», что важно для крупных девелоперов и банков.
- Публичные цены могут стать якорем или спорить с индивидуальными проектами. Выход — вилки «от» и фраза «точная цена после оценки».
- Цифры и цены нужно постоянно обновлять.
- Связка синего и оранжевого и шрифт Manrope распространены: без своих иллюстраций выйдет «типовой финтех».
- OnlyTraffic не упоминать как референс публично.

### Направление C. «Тихий частный банк» (Pictet, Centerview, Evercore, Lazard, Knight Frank)

**Идея.** Сдержанность как знак уровня: почти монохром, глубокий зелёный и бумажный фон, строгий гротеск, мало слов и много воздуха. Доказательства — в сделках, проектах и людях, а не в маркетинге.

**Референсы:**
- https://www.pictet.com/us/en
- https://www.centerviewpartners.com/
- https://www.evercore.com/
- https://www.lazard.com/
- https://www.knightfrank.com/

**Палитра:**

| Роль | Hex | Проверка |
|---|---|---|
| Бумажный фон | `#F5F4F0` | |
| Белый | `#FFFFFF` | |
| Основной текст | `#111315` | 16,9:1 |
| Вторичный текст | `#62655F` | 5,4:1 |
| Глубокий зелёный (hero, тёмные секции) | `#17332B` | текст `#EDEBE4` на нём 11,4:1 |
| Латунь (линии, номера, маркеры) | на зелёном `#C2A26A`, на бумаге `#8A6A35` | 5,6:1 и 4,55:1 |
| Линии | `#D9D9D3` | |

**Шрифты:**
- Заголовки: **Inter Tight** 500/600, межбуквенный интервал от −1% до −2%.
- Текст: **Inter** 400.
- Цитаты и крупные цифры (по желанию): **Spectral** 300 italic.
- Вариант одной гарнитурой: **Geist** + **Geist Mono**.

У всех `cyrillic` и `cyrillic-ext`.

**Главная страница:**
1. Узкий хедер: Экспертиза · Проекты · Команда · Аналитика · Контакты · RU/EN · выбор региона.
2. Hero на `#17332B`: короткая фраза на 4–7 слов, одна строка пояснения, одна кнопка «Запросить встречу».
3. Четыре цифры фирмы, как у Centerview и Evercore.
4. Экспертиза: пять направлений текстом, без карточек и иконок.
5. «Избранные проекты» как плашки: тип объекта, страна, объём в USD m, роль Axiom, год. Фильтр по услуге, как «Select Assignments» у Centerview. Если клиентов нельзя называть, писать без имён: «Жилой комплекс, 1,2 млн м², Ташкент».
6. Подход: независимость, конфиденциальность, стандарт моделирования.
7. Партнёры: портреты в одном тоне и квалификация.
8. Аналитика: 2–3 заметки.
9. Регионы: ЮВА · ОАЭ · Центральная Азия (как Locations у Gridlines и выбор региона у Pictet).
10. Контакт: форма запроса встречи и прямые контакты партнёров (включая Telegram и WhatsApp партнёра).

**Страница услуги:**
1. H1 и короткий абзац.
2. «Ситуации, в которых нас привлекают».
3. Объём работ.
4. Подход.
5. Команда направления.
6. Избранные проекты (плашки).
7. Публикации.
8. Контакт партнёра.

Цены не показываются: вместо них описание модели работы (фиксированная цена, абонемент, почасовая ставка) и формулировка «предварительная оценка за 48 часов». Срок условный, его должна подтвердить сама фирма.

**Изображения.** Минимум или ничего. Тонкие линии, таблицы, крупные цифры. Если фото, то архитектурные, чёрно-белые или в одном тоне, только собственных объектов с разрешения.

**Движение.** Почти нет: fade около 150ms и спокойные переходы между страницами.

**Риски:**
- Холодный «банковский» вид может отпугнуть средний сегмент (девелоперы и подрядчики, которым нужен CFO-аутсорс или бот).
- Направление держится на реальном портфеле: без 6–10 проектов для плашек оно пустое.
- Тёмно-зелёный hero на мобильных может казаться тяжёлым.
- Продукт-бот плохо вписывается в такую эстетику: для него нужна отдельная, более лёгкая страница.

---

## 12. Что взять в любом направлении

1. На каждой странице услуги: сроки, вилка цены или модель оплаты, сравнение уровней, FAQ (по образцу Gridlines).
2. Основной и мягкий CTA рядом («Обсудить проект» и «Задать вопрос в Telegram»), плюс именной контакт партнёра.
3. Кейс в формате «объект · страна · задача · две цифры».
4. Продукт-бот на отдельной странице по схеме «версии → доступность и цены → сценарии → безопасность данных → FAQ» (Anthropic /claude/opus) и бесплатная точка входа («Открыть в Telegram»).
5. Русский язык целиком, без английских вставок. Шрифты только с `cyrillic` и `cyrillic-ext`. В таблицах табличные цифры.
6. Один акцентный цвет, проверенный на контраст. Тёплый или бумажный фон вместо чистого белого (направления A и C).

Практичный вариант: визуальный язык A или C плюс механика страниц услуг из B (цены, процесс, гарантии, FAQ, мессенджер-CTA).
