# Конкуренты: международный рынок и локальные игроки ЮВА и ОАЭ

Дата сбора: 26.11.2026. Зона: специалисты по финмоделям и аудиту моделей, fractional CFO и аутсорс финансов, локальные консультанты Бали, Таиланда, Дубая и Вьетнама.

## Как собирали и чего нет

- Страницы скачаны напрямую (curl), текст извлечён из HTML в порядке следования блоков. Цитаты дословные, на языке оригинала.
- Части страниц, которые рисует JavaScript, могли не попасть в текст: анимированные счётчики, формы HubSpot. Где число счётчика удалось достать из атрибутов HTML, это отмечено.
- Сайт bali-villa-management-service.com целиком собран на JavaScript. Тексты взяты из его JS-бандла и разметки schema.org. Порядок блоков восстановлен по бандлу, поэтому он приблизительный.
- **Не открылись** (защита от ботов или блокировка):
  - toptal.com: Cloudflare, «Sorry, you have been blocked»;
  - getrefm.com: Cloudflare, «Just a moment...»;
  - подстраница BDO «Financial Model Assurance and Review»: Azure WAF;
  - cavendishmaxwell.com: проверка на бота, HTTP 202;
  - cbre.com и cbre.co.th: HTTP 403;
  - crowe.com/ae: HTTP 403.

  WebFetch в этой сессии недоступен, архив web.archive.org тоже. Поэтому по этим компаниям данные взяты из поисковой выдачи. Такие места помечены **[по выдаче поиска, страницу не открыли]**. Структуру и первый экран этих страниц мы не видели.
- **refm.com — это не REFM.** Домен продаётся: «The domain name REFM.COM is for sale Price US$75000». Настоящий REFM живёт на getrefm.com.

---

## Сводная таблица

| Компания | Группа | Кому | Цена на сайте | Сроки на сайте | Лид-магнит | Что в ней главное |
|---|---|---|---|---|---|---|
| BDO UK, Financial Model Services | A | Project finance, PPP, сделки | Нет | Нет | PDF-обзор услуг | Язык кредитора: «satisfy conditions precedent» |
| Operis | A | Инфраструктура, кредиторы, спонсоры | Нет (уровни ответственности есть) | Нет | Онлайн-курс, рассылка | Три уровня аудита, у каждого свой документ и своя страховка |
| F1F9 | A | Банки, фонды, корпорации | «a fixed fee» без цифр | Нет | Примеры моделей, шаблон ТЗ | Процесс из 4 шагов с документом на каждом |
| Gridlines | A | Энергетика и инфраструктура | **Да: $16–20k и $32–40k** | **Да: 3–4 дня, 4–6 недель** | Рассылка, оценка стоимости по модели | Полная прозрачность цены, сроков, итераций |
| REFM (getrefm.com) | A | Обучение real estate modeling | [не открыли] | [не открыли] | Курсы, шаблоны | Не открылся |
| Forvis Mazars Indonesia | A | PPP, банки, «seasoned developers» | Нет | Нет | Нет | Пустая страница бренда |
| Toptal, RE financial modelers | A | Наём фрилансеров | [не открыли] | «about 48 hours» (по выдаче) | Пробный период | Не открылся |
| James Moore (JMCO) | B | Подрядчики, девелоперы (США) | Нет, пакеты без цен | Нет | PDF с пакетами, кейс | Кейс: дашборд вместо задержки 60–90 дней |
| Wiss | B | Подрядчики $10–75M, девелоперы | Нет | Нет | Нет | Вопросы, которые задаёт владелец |
| The CFO Centre | B | МСБ от £1m оборота | Нет | Старт «within a few days to a couple of weeks» | **Тест из 23 вопросов** | Квиз с персональным отчётом |
| Graphite Financial | B | Стартапы с венчурными деньгами | Нет на главной | Нет | Шаблоны (cash flow forecast) | Подзаголовок из трёх результатов |
| Kruze Consulting | B | Стартапы с венчурными деньгами | **Да: $650–850, $850–1,500/мес** | Нет | Калькуляторы | Цифра-доказательство со ссылкой на источник |
| ByBaliBuild | C | Владельцы и девелоперы на Бали | Форматы оплаты без цифр | Аудит за 72 часа, ответ за 1 рабочий день | Платный аудит с зачётом в гонорар | Лучший текст: сценарии провала, документ на каждом этапе |
| Bali Villa Management Service | C | Иностранные владельцы вилл | **Да: Rp 3.5m / 6.5m / 12.5m в месяц** | Ответ за 24 часа | Бесплатная консультация в WhatsApp | Боль словами клиента, цена на первом экране |
| Knight Frank UAE | C | Девелоперы, инвесторы, госструктуры | Нет | Нет | Рыночные отчёты | Мини-кейсы в одну строку с масштабом |
| Cavendish Maxwell | C | Девелоперы, инвесторы (ОАЭ) | [не открыли] | [не открыли] | Кейсы | Не открылся |
| CBRE Phuket | C | Девелоперы на Пхукете | [не открыли] | [не открыли] | Рыночные отчёты | Не открылся |
| Savills GRDC | C | Девелоперы, бренды (branded residences) | Нет | Нет | Рассылка | Brand premium studies |
| C9 Hotelworks (Пхукет) | C, бутик | Девелоперы гостиниц, ATK | Нет | Нет | Рыночные отчёты, рассылка | Вопрос клиента: «What do I build?» |
| Octo Bali Group | C, бутик | Европейские инвесторы на Бали | Нет | Звонок 30 минут | **ROI-калькулятор** | Калькулятор с раскрытыми допущениями |
| Algedra (Дубай) | C, бутик | Землевладельцы, девелоперы | Нет | Ответ за 1 рабочий день | Бесплатная консультация | Feasibility без финмодели |
| Bukit Vista (Бали) | C, бутик | Девелоперы, инвесторы на Бали | **Да: оценка IDR 1,500K за are** | Нет | Калькулятор дохода, ужины с инвесторами | Гарантия возврата денег |

---

## Группа A. Специалисты по финмоделям и аудиту моделей

### A1. BDO UK, Financial Model Services

**1. Кто и для кого.** https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services. Профильная команда BDO LLP по моделированию и project finance. Работает с PF, PPP, сделками, действующими проектами и вторичным рынком. Девелоперы недвижимости отдельно не упомянуты.

**2. Первый экран.**
- Заголовок: «Financial Model Services».
- Подзаголовка нет. Сразу идёт абзац: «Our dedicated and specialist modelling and project finance team has won multiple sector and industry awards and is internationally recognised as a leading provider of model audit, modelling and related support to project finance, PPP, acquisitions, operational and secondary market activity.»
- Кнопка: «Contact Us».
- Описание страницы для поиска: «Work with us, named “Top Global Model Auditor of 2021” by IJGlobal, for all your financial modelling needs.»

**3. Структура.**
1. Первый экран с кнопкой Contact Us.
2. Четыре абзаца о команде: награды, больше 50% проектов вне Великобритании, 25 лет, 2,500 проектов.
3. «Our Core Services»: 5 пунктов.
4. Ссылка на PDF-обзор и контакт.
5. «Our expertise»: 3 ссылки на подстраницы.
6. «Related Insights».
7. «Your key contacts»: 2 партнёра.
8. Форма заявки.

**4. Как описаны услуги.** Перечнем работ, но у главной услуги назван результат для кредитора:
- «Financial Model Assurance and Review – to enable your project or transaction to meet funder, bid, investor and internal control requirements and to satisfy conditions precedent»
- «Our services are tailored to give clients the right degree of confidence and reliance to support financing, commercial and investment decisions.»

**5. Доказательства.**
- Цифры: «supported over 2,500 projects worldwide», «over 25 years’ experience», «over 50% of our projects based outside of the UK».
- Награда IJGlobal 2021 упомянута только в описании для поиска.
- Названы 2 партнёра со ссылкой на биографию.
- Кейсов, логотипов и отзывов на странице нет.

**6. Цены и сроки.** Не показаны.

**7. Призыв к действию.**
- Поля формы: First name, Last name, Company, Email, Phone number, Enquiry, согласие.
- После заявки ничего не обещают.
- Лид-магнит: «Download our Financial Modelling Assurance Services Overview» (PDF).

**8. Глазами девелопера.**
- Сильно: бренд и язык кредитора. «Conditions precedent», то есть отлагательные условия кредита, — это ровно то, что требует банк.
- Слабо: о недвижимости ни слова. Нет процесса, цены и срока. Девелопер из ЮВА не поймёт, возьмут ли его проект на $10M и сколько это стоит.
- Подстраница «Financial Model Assurance and Review» не открылась (Azure WAF).

### A2. Operis

**1. Кто и для кого.** https://www.operis.com/ и https://www.operis.com/model-audit/. Лондон и Торонто, работают с 1990 года. Независимые советники по project finance, моделированию и аудиту моделей. Отрасли: инфраструктура, ВИЭ, цифровые проекты. Клиенты: кредиторы, спонсоры, госзаказчики.

**2. Первый экран.**
- Главная. Заголовок: «We bring rigour and clarity to project finance». Подзаголовок: «Operis is a leading advisor in project finance, renowned for its expertise in financial modelling.» Кнопка: «Discover Operis».
- Страница аудита. Заголовок: «Financial Model Audit». Подзаголовок: «We are an award-winning model auditor, and we provide market-leading model audit services across a wide range of infrastructure sectors.» Кнопка: «Tell us about your project».

**3. Структура главной.**
1. Первый экран.
2. «Over 30 years of experience»: 1,200 проектов.
3. Реклама курса «Master the fundamentals of project finance modelling».
4. О компании: 4 направления услуг.
5. «Our Services»: 6 карточек.
6. «Featured: Case Studies»: 5 проектов.
7. «Our clients»: логотипы.
8. «Experience matters»: 94 страны, 1,640 проектов, £23bn.
9. Регионы и отрасли.
10. Награды IJGlobal 2021.
11. Women in Finance Charter.
12. Статьи и новости.
13. Один отзыв.
14. Подвал с офисами.

**Структура страницы аудита.**
1. Первый экран.
2. Обещание «We give you the maximum reassurance that the models outputs can be trusted».
3. Три преимущества: Robust Methodology, Personal Service, Modellers at heart.
4. «Reasons to have your model audited by Operis»: 4 пункта.
5. «Auditing Services»: три уровня.
6. Счётчики.
7. Карточки проектов: 8 штук.
8. «Meet our Modelling Team»: фото и имена.
9. Новости и статьи.
10. «Let's discuss your project».

**4. Как описаны услуги.** Через последствия для сделки, а не через перечень работ:
- «We give clients greater confidence that the numbers are right, and that they will be able to see at a glance if the project is in trouble, which protects them from mispricing the deal.»
- «We focus on raising issues that have a material effect on your deal and provide you with clear and meaningful reports highlighting problems that could affect your transaction and, most importantly, its bankability.»
- «clear and concise issue reports and opinion letters, intentionally written free of jargon for the benefit of a range of stakeholders»

Уровни аудита описаны через документ, который получит клиент, и размер ответственности:

| Уровень | Документ | Страховка ответственности |
|---|---|---|
| Formal Model Audit (FMA) | «Formal Opinion Letter» | «liability cover of up to £20 million» |
| Due Diligence Review (DDR) | «Due Diligence Report» | «liability cover of up to £100,000» |
| High Level Review (HLR) | «Letter of Support» | «we offer no formal liability with an HLR» |

**5. Доказательства.**
- Цифры: «Experience spanning 94 countries», «Over 1,640 projects undertaken to date», «£23bn total project value undertaken in 2023 - 2024».
- Цифры противоречат друг другу: выше на той же главной написано «more than 1,200 projects worldwide».
- Кейсы: название проекта и один абзац о самом проекте. Что нашли и что это дало клиенту, не сказано.
- Логотипы клиентов, награды, команда с именами.
- Один отзыв: «"We hand-picked them (Operis) because of their combined expertise and the world-class service they provide."» (Bird Capital).

**6. Цены и сроки.** Цен и сроков нет.

**7. Призыв к действию.**
- Кнопка «Tell us about your project» ведёт на страницу контактов. Формы там нет: телефоны и почта по направлениям.
- Что нужно от клиента: «To help us determine how we can best assist you with your project, we need to understand your objectives and timetable, and evaluate the model's size and complexity.»
- Лид-магниты: онлайн-курс, рассылка, статья «8 Common Spreadsheet Risks and Solutions».

**8. Глазами девелопера.**
- Сильно: уровни аудита привязаны к документу для банка. Сразу понятно, что нести кредитору.
- Сильно: обещание отчёта «free of jargon».
- Слабо: только инфраструктура и PPP. Нет ни цены, ни сроков. Кейсы описывают объект, а не результат проверки.

### A3. F1F9

**1. Кто и для кого.** https://www.f1f9.com/ и https://www.f1f9.com/financial-model-build/. Великобритания, Дели, Дубай, работают с 1999 года. Строят модели по стандарту FAST и учат моделированию. Клиенты: банки, фонды, акционеры, корпорации.

**2. Первый экран.**
- Заголовок: «F1F9 are Financial Modelling Experts».
- Подзаголовок: «We specialise in knowledge sharing through the models that we build and best practice training courses that we run. We help our clients understand and make best use of the financial models that are critical to their business success.»
- Кнопки: «Contact us», «About Us».
- Счётчики (значения из атрибутов HTML):
  - 530 — «Best practice financial models built»;
  - 11,600 — «People trained to build complex financial models»;
  - 2,910 — «Have worked through our online courses».

**3. Структура главной.**
1. Первый экран со счётчиками.
2. Training & Courses.
3. Financial Model Build.
4. Our Clients: логотипы.
5. Get In Touch: вопросы.
6. Why F1F9.
7. Подвал.

На сайте есть корзина для покупки курсов.

**Структура страницы Model Build.**
1. Описание.
2. «Our approach to model build».
3. Процесс из 4 шагов.
4. Отрасли.
5. «Download a financial model».
6. Клиенты.
7. Команда.
8. Кейсы.

**4. Как описаны услуги.** Блок «Get In Touch» начинается с вопросов клиента: «Is your existing financial model providing you with the transparency, confidence and answers you need? Can it be modified, or does it need to be rebuilt? Do you want to learn to build a new model or to make changes yourself?»

Процесс построения модели расписан по шагам, и у каждого шага есть документ:
1. **Proposal.** После первого звонка присылают предложение: «a fixed fee», «the project timetable», «scope of work», «our proposed team», «our relevant experience». Документ на скачивание: Scoping Template.
2. **Project Initiation.** Стартовая встреча. Документ: «Start File».
3. **Build Phase.** «Weekly calls to: present the latest model, receive your feedback, discuss the next phase of work, review progress & timetable». Параллельно идут «QC checks & software review», «F1F9 peer review», «model documentation». Документ: «Actions Sheet».
4. **Handover.** Передача модели: «how to navigate & review», «how to maintain audit trail». После передачи: «Ongoing availability for: clarification questions, further support by the hour, additional training». Документ: «Example Model».

**5. Доказательства.**
- Счётчики и логотипы.
- Команда с фото и биографиями, например: «Omar ... Director Dubai ... He is fluent in Arabic both written and spoken.»
- Кейсы: Ofwat (с цитатой клиента), Mubadala, Masdar, Power NI, Eneco, Virgin Trains.
- «We’ve built over 140 models to help clients assess, successfully bid for and close major schemes».

**6. Цены и сроки.** Обещают «a fixed fee» в предложении, но цифр нет. Сроков нет.

**7. Призыв к действию.**
- Поля формы: First Name, Last Name, Email, Phone, message.
- Обещание: «Still have questions? Contact us anytime and we’ll get back to you shortly.»
- Лид-магниты: «These free to download example financial models demonstrates our approach to building best practice models», шаблон ТЗ (Scoping Template).

**8. Глазами девелопера.**
- Сильно: процесс без «чёрного ящика». Еженедельные созвоны, документ на каждом шаге, пример модели можно скачать до заказа.
- Сильно: вопрос «можно ли доработать или надо перестроить?» точно описывает ситуацию клиента с чужой моделью.
- Слабо: о недвижимости ничего. Первый экран без содержания («Experts»). Курсы и корзина отвлекают того, кто пришёл заказать модель.

### A4. Gridlines

**1. Кто и для кого.** https://www.gridlines.com/ и https://www.gridlines.com/financial-model-audit/. Основаны в 2017 году. Офисы: Манчестер, Дели, Дубай, Сингапур, Йоханнесбург, Мехико. Project finance в энергетике и инфраструктуре. Клиенты: девелоперы, инвесторы, кредиторы.

**2. Первый экран.**
- Главная. Заголовок: «Project finance advisory and financial modelling for energy and infrastructure.» Подзаголовок: «The numbers behind your deal have to hold. We make sure they do.» Кнопка: «Tell us about your project», рядом ссылка «Or ask a question».
- Страница аудита. Заголовок: «Financial model audit services». Подзаголовок: «Identify and resolve critical financial model issues swiftly – because the stakes are high and your project’s success can’t wait.» Кнопка: «Tell us about your project», рядом ссылка «Or see our case studies».

**3. Структура главной.**
1. Первый экран.
2. «Trusted on the deals that have to close».
3. «Straight answers on high-stakes deals».
4. Цифры: $100bn сопровождённых сделок, 100 связей с кредиторами, ECA и DFI, рейтинг Infralogic.
5. Четыре услуги.
6. «Why finance leaders choose Gridlines»: история боли.
7. Отзыв Masdar.
8. Недавние проекты.
9. Статьи.
10. Офисы.
11. Рассылка: «Join 35,492 financial modellers...».
12. Всплывающая форма.

**Структура страницы аудита.**
1. Первый экран.
2. «$8bn+» проверенных моделей.
3. «A model audit with all the rigour. None of the headaches.»
4. Три пары «боль / как у нас».
5. Отзыв.
6. Таблица двух уровней проверки с ценами.
7. «Why Gridlines?».
8. Цифры: 350+ аудитов, $130bn, 2-е место в Infralogic.
9. Команда и проекты.
10. Руководители с биографиями и почтой.
11. Статьи и офисы.
12. FAQ из 8 вопросов.

**4. Как описаны услуги.** Через боль клиента и прямое сравнение с рынком:
- «You’ve had models you couldn’t quite trust, audits that cost you every time the numbers moved, and advice that wouldn’t commit when you needed a call.»
- Модели: «Models that reflect the commercial position and hold up under lender scrutiny, built by the people who understand the deal.»
- Аудит: «Independent, lender-trusted audits with no cap on iterations. Send the model early, update it as you need.»
- Три пары на странице аудита:

| Боль | Как у нас |
|---|---|
| «Why choose to endure weeks of delay...» | «...We deliver first feedback in just 3-4 DAYS» |
| «Why choose unpredictable iteration charges...» | «...Regain control of your budget with our fixed-fee model audit. No surprises. No embarrassing over-spends.» |
| «Why endure the back and forth of old fashioned issue lists...» | «...our unique “live shared issues list”» |

- Типичные ошибки моделей описаны в FAQ четырьмя группами: «Structure and transparency», «Logic and calculation integrity», «Data linkage and control», «Financial integrity and outputs». Вывод там же: «The highest-impact errors sit in the debt, tax, and cashflow logic that lenders scrutinise most, and many are subtle enough to produce plausible but wrong results.»

**5. Доказательства.**
- «In 2025, we audited more models than KPMG, Deloitte, EY, and PwC combined.»
- Цифры (значения из атрибутов HTML): 350+ аудитов, $130bn стоимости проектов, 2-е место в Infralogic H1 2026.
- Отзывы с именем и должностью, например Ismail Chakour, Head of Structured Finance, Masdar.
- Карточки проектов: отрасль, дата, страна, клиент.
- Биографии с почтой, например: «She has worked on almost 350+ model audit assignments.»
- «appears on many lenders’ approved auditor lists».

**6. Цены и сроки.** Показаны. Это единственный в выборке специалист по моделям, который публикует цены.

|  | Comfort review | Full model audit |
|---|---|---|
| Итерации | «1 iteration + 1 further iteration limited to changes related to the comments raised by Gridlines» | «Unlimited model iterations» |
| Ответственность | «2× fees» | «£5 m typically, and up to £12 m» |
| Первая обратная связь | «3‑4 working days» | «3‑4 working days» |
| Типичная цена | «$16‑20k USD*» | «$32‑40k USD*» |
| Итоговый документ | «Comfort letter» | «Opinion letter» |

- Сноска к ценам: «*The typical fee is based on a Model with unique formula count of 3,000...»
- Срок до подписания: «a full audit typically reaches sign-off within six weeks, and a comfort review within around four weeks».
- От чего зависит цена: «Cost depends on the model’s size and complexity, often gauged by counting unique formulae ... the scope ... the level of liability cover required, and how much supporting documentation you need reviewed.»

**7. Призыв к действию.**
- Форма HubSpot: поля без JavaScript не видны.
- Обещание: «Tell us about your project and we’ll be back to you within one working day.»
- Ещё одна точка входа: «Share your model for a fee estimate».
- Рассылка раз в две недели, курсы.

**8. Глазами девелопера.**
- Сильно: максимальная прозрачность. Цена, срок, число итераций, итоговый документ и страховка собраны в одной таблице. FAQ отвечает на вопросы покупателя, а не на вопросы SEO.
- Сильно: текст строится по схеме «как обычно — как у нас».
- Слабо: всё про энергетику и инфраструктуру. Много жаргона: ECA, DFI, RfP. Девелопер вилл на Бали себя здесь не узнает.

### A5. REFM (Real Estate Financial Modeling)

**1. Кто и для кого.** refm.com продаётся и к REFM отношения не имеет. Сайт компании — https://www.getrefm.com/, он не открылся (Cloudflare). **[по выдаче поиска, страницу не открыли]**: REFM основал Bruce Kirsch. Компания продаёт курсы, сертификаты и Excel-шаблоны для real estate, а также консалтинг. В выдаче она описывает себя так: «premier financial modeling solutions provider for Excel-based financial spreadsheet models, finance and financial modeling training, and financial modeling consulting for real estate transactions of all types». Есть платформа Valuate и сертификат REFAI.

**2–8.** Первый экран, структуру, форму и цены проверить не удалось. По выдаче поиска REFM в первую очередь школа и магазин шаблонов, а не консультант по проектам. Для Axiom это скорее источник словаря и ожиданий клиента («waterfall», «JV equity»), чем прямой конкурент.

### A6. Forvis Mazars Indonesia, Project Finance and Financial Modeling

**1. Кто и для кого.** https://www.forvismazars.com/id/en/services/financial-advisory/project-finance-and-financial-modeling. Индонезийская фирма сети Forvis Mazars. Работают с госзаказчиками PPP, «seasoned private sector developers or funds», банками.

**2. Первый экран.**
- Заголовок: «Project Finance and Financial Modeling».
- Текст: «With support from our global Project Finance practice, we offer financial model audit services to public sector procurers of PPP projects or to seasoned private sector developers or funds. Our audit aims at providing you with assurance that the models developed for the project are free from material error.»
- Кнопки нет.

**3. Структура.**
1. Заголовок.
2. Два абзаца о методе: «replication methodology, reinforced with line-by-line checking».
3. Три пункта «typically used for».
4. Контакт: «Sebastien Gautier, Managing Partner, Head of Outsourcing - Jakarta».
5. Общий блок контактов.

**4. Как описаны услуги.** Перечнем. Из полезного одна идея: «our methodology can serve to provide early stage "health checks" as well as full opinion reports». Сценарии использования: «PPP / PFI / P3 transactions on behalf of banks, monoline insurers and shareholders», «Clients requiring Sarbanes-Oxley-style reviews».

**5. Доказательства.** Нет: ни цифр, ни кейсов, ни команды проектного финансирования. Отраслевая страница о недвижимости (https://www.forvismazars.com/id/en/industries/financial-services/real-estate) говорит общими словами: «A solid foundation for an uncertain property market».

**6. Цены и сроки.** Нет.

**7. Призыв к действию.** «Send a message», «Or use our contact form». Лид-магнитов нет.

**8. Глазами девелопера.**
- Сильно: бренд сети и идея «health check» до полного аудита.
- Слабо: глобальный текст без индонезийской специфики. Нет PPN, PPh, PT PMA, нет недвижимости. Контактное лицо — руководитель аутсорса, а не моделирования. Создаётся ощущение, что практики в Индонезии на самом деле нет.

### A7. Toptal, Real Estate Financial Modelers

**1. Кто и для кого.** https://www.toptal.com/finance/real-estate-financial-modelers, есть отдельная страница для Дубая. Площадка для найма фрилансеров. Страницу не открыли: Cloudflare, «Sorry, you have been blocked».

**[по выдаче поиска, страницу не открыли]:**
- обещание «the Top 3%», отбирают «fewer than 3%» соискателей;
- «No-Risk Trial, Pay Only If Satisfied», пробный период «up to two weeks»;
- «Typically, you can hire real estate financial modelers with Toptal in about 48 hours»;
- форматы: hourly, part time, full time;
- на страницах есть карточки фрилансеров с биографиями.

**8. Глазами девелопера.** Toptal задаёт ожидание по скорости (48 часов) и снимает риск пробным периодом. Слабость модели: заказчик получает человека, а не ответственность за результат. Методологии, проверки и сопровождения после сдачи нет. Против этого Axiom может играть.

---

## Группа B. Fractional CFO и аутсорс финансов для стройки и девелопмента

### B1. James Moore & Co. (JMCO)

**1. Кто и для кого.** Бухгалтерская фирма из Флориды. Услуги CFO на частичную занятость для строительных компаний и отдельный раздел для девелоперов.
- https://www.jmco.com/business-advisory/fractional-cfo-services/construction/ (сюда перенаправляет /construction-fractional-cfo/)
- https://www.jmco.com/industries/real-estate/developers/

**2. Первый экран.**
- Стройка. Заголовок: «Construction Fractional CFO Services». Второй заголовок: «Build Your Future With Confidence». Текст: «Irregular cash flow, varying job costs, surety and licensing requirements… they’re common challenges for construction companies looking to grow their business.» Кнопка «Contact Us» появляется после нескольких абзацев.
- Девелоперы. Заголовок: «Real Estate Developers». Второй заголовок: «Real Estate Development Accounting». Текст: «Build for a better financial future with the real estate development accounting team at James Moore». Кнопка: «Contact Us».

**3. Структура страницы для стройки.**
1. Боль на первом экране.
2. Три выгоды: «Improved Cash Flow», «Job Cost Accuracy», «Compliance Confidence».
3. «C-Suite Expertise Without the C-Suite Cost».
4. 15 плиток услуг.
5. «Get the Details»: PDF с пакетами.
6. FAQ «How does it work?».
7. «Case in Point».
8. Статьи.
9. Рассылка.
10. Команда: 3 биографии.
11. Офисы.

**Структура страницы для девелоперов.**
1. Первый экран.
2. Три преимущества.
3. Гайд.
4. «Measurably Better»: 5 цифр.
5. Услуги: аудит, консалтинг, налоги.
6. 5 отзывов.
7. Видеосерия.
8. «Get Started Today».
9. «Success Stories».
10. Статьи.
11. Команда.

**4. Как описаны услуги.** Перечнем работ с частотой. Это конкретно, хотя и длинно:
- «Weekly cash flow monitoring, 13-week cash flow preparation and accounts receivable tracking.»
- «Monthly rolling forecasts and scenario-based financial modeling.»
- «Financial statements with custom schedules, weekly flash reports and key KPI tracking.»
- PDF с пакетами делит работу на три уровня: «FOUNDATIONAL», «STRATEGIST», «VISIONARY CFO». Пример: «Daily and weekly flash report with key KPIs and cash data» на старшем уровне.
- Для девелоперов: «Financial projection, budgeting and pro-formas : Get a roadmap that helps you project revenues, make accurate budgets, secure funding and assess project viability».

**5. Доказательства.**
- Кейс для стройки: «See how we helped one construction company’s value grow from $250,000 to $12 million in just five years.»
- **Кейс для девелопера, ближе всего к Axiom:** «A commercial real estate development company was planning a $300 million mixed-use development ... James Moore’s real estate CPAs provided a real-time dashboard from which the developer could see all transactions, expenditures, financial reports, budgets and cash on hand for every aspect of the project. This made the data available as these transactions happened instead of having to wait 60-90 days for the information to come through the usual channels.»
- Цифры: «$600 Million — Providing CFO services for $600M in commercial developments», «$1 Billion — Providing accounting services for $1 billion in real estate properties».
- Отзывы с полным именем, должностью и компанией. Например: «Orianna Snook, Chief Executive Officer Emmer Development Corp.», «Paul Holub, President Holub Development Co.».
- Членство в отраслевых ассоциациях: CICPAC, CFMA.

**6. Цены и сроки.** Цен нет. О форме оплаты: «We offer our services primarily via monthly plans, which are tiered according to how much work you’d like for us to do. A la carte services are also available».

**7. Призыв к действию.**
- Кнопки «Contact Us», «Download Now» (пакеты), «access the case study».
- «Take the first step on your journey to financial clarity by scheduling a free consultation with our experts.»
- Первый шаг работы: «We start with an assessment to review your financial statements, cash flow picture, budgeting, business processes and operations.»
- Лид-магниты: PDF с пакетами, кейс, гайд по учёту в фондах недвижимости, видеосерия, рассылка.

**8. Глазами девелопера.**
- Сильно: кейс с дашбордом против задержки данных в 60–90 дней. Это готовая формулировка ценности для услуги Axiom по контролю платежей. Ещё плюс — частота работ (weekly, 13-week) и отзывы девелоперов с именами.
- Слабо: всё про США (surety, 1031, SALT). 15 плиток услуг превращаются в шум. Страница для девелоперов о налогах и аудите, а не о деньгах проекта.

### B2. Wiss

**1. Кто и для кого.** Бухгалтерская и консалтинговая фирма из Нью-Джерси. Целевые клиенты — подрядчики с выручкой $10–75M и девелоперы.
- https://wiss.com/fractional-cfo-services-for-construction/
- https://wiss.com/business-consulting-services-real-estate/

Обе страницы оформлены как статьи блога, это SEO-лендинги.

**2. Первый экран.**
- Заголовок: «Fractional CFO Services for Construction Companies». Под ним дата и «By: Wiss Team».
- Вместо подзаголовка история: «It started with a good problem. A commercial contractor in New Jersey had just wrapped his best year ever — $22 million in revenue, backlog full, crews booked six months out. He called his accountant expecting celebration. What he got instead was a question: “Where’s the cash?”»
- Кнопки на первом экране нет.

**3. Структура.**
1. История.
2. Key Takeaways.
3. «What a Fractional CFO Actually Changes».
4. «The Hidden Problem: Growth Without Financial Strategy».
5. «Why Construction Is Different».
6. «What a CFO Sees That Your Bookkeeper Doesn’t»: пары вопросов.
7. «When It’s Worth It: Clear Thresholds».
8. «Engagement Models».
9. «Integration With Your Existing Finance Function».
10. «The Wiss Approach».
11. «Contact Us».

**4. Как описаны услуги.** Через вопросы владельца. Это лучший пример в выборке.
- Пары «вопрос бухгалтера / вопрос CFO»: «Are all invoices coded correctly?» / «Which projects are actually profitable?», «Is the bank reconciliation done?» / «Do we have the working capital to take on that $8M project?», «Is the WIP schedule reconciled monthly?» / «What happens to our loan covenants if we take a loss on the downtown job?»
- Последствия без CFO: «You grow revenue but shrink margin», «You underprice work to keep crews busy — ... with no one running the true cost-to-complete numbers», «You think bonding is the constraint — when working capital actually is.»
- Поводы обратиться: «Experiencing cash flow problems despite profitable operations», «Expanding into new project types or geographies where the margin profile is unknown».
- Честный отбор клиентов: «Not every construction company needs a fractional CFO. Smaller contractors with straightforward operations may be fine with solid bookkeeping and periodic CPA guidance.» и «If your primary need is cleaner books and timely financial statements, you need better accounting support — not a fractional CFO.»
- Страница о недвижимости: «Scenario planning and risk assessment : What happens if occupancy rates decline 10%? If construction costs increase by 15%? If interest rates rise?» и «Budget development and variance analysis : Construction budgets change as projects progress. We track actual costs against projections, identify variances early, and help you adjust strategies before overruns threaten project viability.»

**5. Доказательства.** На этих страницах почти нет. История в начале без имени клиента и без указания, что это кейс Wiss. На главной один отзыв от пивоварни. Логотипов, цифр и команды на лендингах нет.

**6. Цены и сроки.** Цен нет. Порог: «typically sits in the $10M–$75M revenue range — ... not yet complex enough to justify a full-time executive hire at $200K+». Форматы работы: «monthly retainer arrangements», «project-based engagements», «interim CFO leadership».

**7. Призыв к действию.** «Contact Wiss to schedule a CFO advisory consultation and find out what’s actually driving — and limiting — your financial performance.» Кнопка «Contact Us», рассылка. Лид-магнитов нет.

**8. Глазами девелопера.**
- Сильно: говорит вопросами самого девелопера и честно отсеивает тех, кому услуга не нужна. Это вызывает доверие.
- Слабо: формат статьи. Нет доказательств, пакетов и цены. Заявка в конце звучит общими словами.

### B3. The CFO Centre

**1. Кто и для кого.** Глобальная сеть CFO на частичную занятость, работает с 2001 года. Есть офис в ОАЭ: https://www.cfocentre.com/ae/. Клиенты — МСБ «typically starting from £1million».
- https://www.cfocentre.com/gb/
- https://www.cfocentre.com/gb/book-a-call
- https://www.cfocentre.com/gb/free-business-assessment/

**2. Первый экран.**
- Заголовок с прокруткой фраз: «The world's # 1 fractional CFO provider, driving your financial strategy. cash flow management. profit optimisation. operational excellence. strategic growth. exit maximisation.»
- Вторая прокрутка, эмоциональная: «no more restless nights. the freedom to step away. success without sacrifice. ... more time with your kids. retirement sooner.»
- Кнопки: «Explore what we do», «Read success stories», «Hear from our clients».
- Цифра: «1320 active clients globally».
- Подпись к счётчику, значение которого рисует JS: «of our clients have a more restful sleep!»

**3. Структура.**
1. Первый экран.
2. Цели клиента: Exit Planning, Profit Improvement, Improve Cash Flow, Scaling Up, CFO’s CFO.
3. Карусель историй успеха.
4. Цифра «47% ... UK SMEs facing cash flow issues» со ссылкой на ONS.
5. «Struggling with Cash flow? Time? Scaling? Exit Strategy? Profit?».
6. Почему мы: «top 1% of CFO applicants», «750+ high calibre CFOs».
7. Команда.
8. FAQ.
9. Подвал со сносками.

**4. Как описаны услуги.** Через цели владельца:
- «Improve Cash Flow — Unlock trapped cash, improve predictability, and create breathing space to grow.»
- «Exit Planning — Increase business value, get deal-ready, and exit on your terms with confidence and control.»

Строительной специфики на главной нет. Есть отдельные CFO с опытом в девелопменте. По выдаче поиска, например, Craig Pargetter: «over 25 years of board-level experience in property».

**5. Доказательства.**
- Цифры: 750+ CFO, 1320 клиентов, 18 стран, «since 2001».
- Истории успеха в формате заголовков: «How a Fractional CFO Helped Scale a Business to £100M».
- Логотипы со сноской: «Logos shown represent companies where our CFOs have previously held roles... Their appearance does not imply any affiliation with or endorsement.» То есть это логотипы прошлых работодателей, а не клиентов.
- Звание «#1» со сноской: «Based on number of CFOs globally and volume of countries trading 2026.*»

**6. Цены и сроки.** Цен нет. Старт: «Most fractional CFOs can begin working within a few days to a couple of weeks after the onboarding process.» Обязательства: «Not necessarily, although many of our clients have been with us for years. You can scale your CFO support up or down as needed.»

**7. Призыв к действию.**
- Заявка на звонок «Book a discovery call», форма HubSpot. Что будет на звонке: «There’s no pressure, just a conversation about what’s possible. We’ll explain how our proven process works and explore whether bringing in part-time CFO expertise is the right next step for you.»
- **Лид-магнит:** «Take the free Scale-up & Exit Business Assessment™ — Answer 23 quick questions about your business and your own goals. In around four minutes, you’ll get a personalised report with your readiness score, your biggest gap and the first thing to fix.»

**8. Глазами девелопера.**
- Сильно: тест с персональным отчётом. Короткий, с обещанием конкретного результата: оценка, главный пробел, первое действие.
- Слабо: превосходные степени («#1»), эмоциональная вата про сон, логотипы прошлых работодателей. Отрасль девелопера на сайте не видна.

### B4. Graphite Financial

**1. Кто и для кого.** https://www.graphitefinancial.com/. Аутсорс бухгалтерии и финансов для стартапов с венчурными деньгами (США). Недвижимостью не занимаются. Взяты как пример B2B-лендинга финансовых услуг.

**2. Первый экран.**
- Надзаголовок: «THE FINANCE TEAM BEHIND VENTURE-BACKED STARTUPS».
- Заголовок: «Outsourced Accounting and Finance for VC-Backed Startups».
- Подзаголовок: «Accurate monthly close. Clear runway. Investor-ready reporting. One team inside your business, running accounting, finance, tax, payroll, and HR.»
- Строка «✓ Accounting ✓ Finance ✓ Tax ✓ Payroll ✓ HR».
- Кнопки: «Learn More», «Work with Us».

**3. Структура.**
1. Первый экран.
2. «Built for What’s Next».
3. «Clean books, coherent data, and confident decisions».
4. 6 карточек услуг.
5. Три результата: «Build your vision, not a spreadsheet.», «Protect momentum by eliminating preventable mistakes.», «Walk into every board meeting prepared.»
6. «Graphite works inside your company. Not at arm’s length.»
7. Три отзыва.
8. FAQ.
9. «Get started today!».

**4. Как описаны услуги.** У каждой карточки есть подзаголовок-результат. Пример: «Bill Pay & Invoicing — Cash Flow Control & Internal Oversight — ... we ensure your cash flow is predictable and your internal controls are bulletproof.»

FAQ построен на ситуациях клиента: «Our books are a mess, can you help?» — «You're not alone. ... Graphite works with you to get everything back on track, no matter what kind of disaster you're working with.»

**5. Доказательства.** Слабые. «Join hundreds of leadership teams...». Три отзыва только с именами, без компаний. Цифр и кейсов на главной нет.

**6. Цены и сроки.** На главной нет.

**7. Призыв к действию.** «Book a brief, no-pressure meeting to learn how Graphite Financial can help your business.» Лид-магниты: бесплатные шаблоны (free cash flow forecast template, chart of accounts template, payback period model).

**8. Глазами девелопера.**
- Сильно: подзаголовок из трёх коротких результатов. Хорошо работает FAQ «у нас бардак в учёте».
- Слабо: модные слова («bulletproof», «absolute confidence», «Every board meeting will be your best one ever») и ноль цифр.

### B5. Kruze Consulting

**1. Кто и для кого.** https://kruzeconsulting.com/ и https://kruzeconsulting.com/pricing/. Аудиторская фирма (CPA) из Сан-Франциско для стартапов с венчурными деньгами. Пример сильного B2B-лендинга финансовых услуг.

**2. Первый экран.**
- Заголовок: «Kruze Consulting: Expert Accounting for VC-Funded Startups».
- Текст: «Kruze Consulting specializes in providing expert accounting and bookkeeping services tailored to the unique needs of VC-funded companies.»
- Кнопка: «Get a Free Consultation».

**3. Структура.**
1. Первый экран.
2. Цифра-доказательство с фото основательницы.
3. «Why partner with Kruze?»: 5 пунктов.
4. Призыв к действию.
5. 4 услуги.
6. Кейс SnapAttack с цитатой.
7. FAQ.
8. Новости о раундах клиентов.
9. Форма с вопросами для отбора.
10. Подвал: номер лицензии, Inc. 5000.

**4. Как описаны услуги.** Средне: перечень с выгодой. Пример: «Your startup can significantly extend your runway by offsetting payroll taxes.»

**5. Доказательства.** Цифра с указанием источника — редкость в выборке:
- «Kruze Consulting clients are twice as likely to be acquired as the average startup»;
- «Data published by cap table management vendor Carta shows that 5.2% of startups incorporated in 2018 were acquired, while 11.5% of Kruze clients were acquired during the same period.»

Ещё: «800+ Of The Best Funded Startups Trust Kruze», кейс с отзывом, номер лицензии «California Board of Accountancy license number 7637».

**6. Цены и сроки.** Цены показаны:
- «Basic Bookkeeping — Great for pre-revenue, seed-stage companies — $650 - $850 per month»;
- «Founder Timesaver — Best for companies starting to scale — $850 - $1,500», с пометкой «Most Popular»;
- «Premium — Custom quote».

В FAQ честно сказано про плату за подключение: «Yes, we charge a one-time onboarding fee to onboard each new entity.» Кого берут: «Kruze specializes in funded Delaware C-Corps that have raised at least $500K in venture capital.»

**7. Призыв к действию.**
- Поля формы: First name, Last name, Work email, Phone, Company, Company entity type, «Are you a VC-backed startup?», «What is your funding stage?», «Funding amount», «Do you plan to convert to a C-Corp...», «How can Kruze help?» (несколько вариантов), «How did you hear about us?», «Anything we should know before we talk? (optional)». Кнопка: «Start the Conversation».
- Над формой: «Talk to an experienced accountant, not a generic sales person».
- Лид-магниты: калькуляторы (R&D Tax Credit Calculator, Tax Return Pricing Calculator).

**8. Глазами девелопера.**
- Сильно: диапазоны цен и чёткое «кого берём». Доказательство через измеримый результат клиентов с источником.
- Слабо: форма из 14 полей тормозит заявку. Первый экран без содержания.

---

## Группа C. Локальные игроки ЮВА и ОАЭ

### C1. ByBaliBuild (PT ByBali Build Consulting)

**1. Кто и для кого.** https://bybalibuild.com/, а также /fees/, /professionals/, /site-audit/. Управление стройкой на стороне заказчика на Бали. Клиенты: частные владельцы и «professionals» (инвесторы, девелоперы, гостиницы, ритейл, клиники). Сайт на трёх языках: EN, FR, ID.

**2. Первый экран.**
- Надзаголовок: «PROJECT MANAGEMENT IN REAL ESTATE · CONSTRUCTION & RENOVATION · BALI».
- Заголовок: «One person standing between you and your building site.»
- Подзаголовок: «Residential and commercial. Tendering, budget, quality, deadlines — we manage the site, you keep control, and you get a site report every single day.»
- Кнопки: «TALK ABOUT YOUR PROJECT», «SITE AUDIT».
- Страница для профессионалов. Заголовок: «Every week of delay is a week without revenue.» Подзаголовок: «We run the construction so that the opening date you announced is the date you open.»

**3. Структура главной.**
1. Первый экран.
2. Два входа: для частных владельцев («Your villa, watched as closely as if you were there») и для профессионалов («Open on the date you announced, on the budget you set»).
3. Цифры.
4. «WHAT HAPPENS WHEN NOBODY IS WATCHING»: 3 сценария провала.
5. «Six stages, one written deliverable at each».
6. «A site report every day, not a phone call once in a while»: что получает клиент.
7. «Three projects, with the numbers».
8. «Trusted by»: клиенты с локациями.
9. «How we are paid, in writing»: 4 формата оплаты.
10. «FIRST STEP»: кофе в офисе или видеозвонок.
11. Форма.

**4. Как описаны услуги.** Через моменты провала и через документ, который получит клиент. Лучший текст в выборке.
- «A building site in Bali does not go wrong all at once. It goes wrong line by line.»
- «An attractive price per sqm, then waterproofing, electrics or the pool invoiced later as extras. The final bill has nothing to do with the quote you signed.»
- «Seventy per cent paid, work stopped, and nobody on the ground to record it, price what is left and take back control.»
- Для девелоперов: «Investors and developers — Several units, one schedule, one cost per sqm to defend. The pressure is the date the units start earning — a two-month slip changes the whole return.»
- Что покупают профессиональные клиенты: «A schedule that can be defended», «A cost per sqm that holds», «A handover file, not a set of keys».
- Отчёты: «Built to be forwarded to your board, not just read by you» и «The weekly report is where a slipping unit becomes visible — a percentage behind plan, named trades, and a stated plan to recover it.»
- Зачем нужен посредник: «Because the contractor prices the work, executes it and certifies it. Separating the person who checks from the person who builds is the whole point».

**5. Доказательства.**
- Цифры: «60+ projects managed in Bali», «15,000+ sqm supervised in construction and renovation», «working languages: English, French, Indonesian».
- Три проекта: площадь, срок, формат работы и абзац о задаче. Пример: «550 sqm in five months meant running several trades at once...».
- Список клиентов с локациями.
- Образцы отчётов: «Both documents below are real, with the project identified only to you.»
- В подвале налоговый номер NPWP.

**6. Цены и сроки.** Цифр нет, но форматы оплаты описаны:

| Формат | Как платят |
|---|---|
| Pre-purchase inspection | «Fixed fee, per property» |
| One-off audit | «Fixed price, written report within 72 hours» |
| Monthly supervision | «Flat fee, for a project already under way» |
| Full management | «Percentage of the construction budget, tapering» |

- Зачёт аудита: «Deducted from our fit-out fee if you go on to appoint us.»
- Перерасход стройки: «Our fee is agreed at the outset and does not grow with the works.»
- Сроки: «You get an answer within one working day, and a written fee proposal within two working days of our site visit.»

**7. Призыв к действию.**
- Поля формы: NAME, EMAIL OR WHATSAPP, PROJECT TYPE (New build / Renovation / Commercial / Site audit), BUDGET (< 500 M IDR / < 1 Bn / 1 – 5 Bn / > 5 Bn).
- Две кнопки отправки: «SEND BY EMAIL» и «SEND ON WHATSAPP».
- Обещание: «Reply within one working day · Monday to Friday, 9am – 6pm WITA».
- Входной продукт: «Already holding a quote, or already on site? Our site audit is a fixed-price service: a visit, the quote checked line by line, a written report within 72 hours, deducted from our fit-out fee if you hand us the rest.»

**8. Глазами девелопера.**
- Сильно: конкретика и честность. Документ на каждом этапе, входной продукт с зачётом, отправка заявки в WhatsApp.
- Слабо: цифр в ценах нет. Денежной стороны проекта (cash flow, доходность, финансирование) нет совсем. Это ровно та часть, которую закрывает Axiom. Компания — естественный партнёр, а не конкурент.

### C2. Bali Villa Management Service

**1. Кто и для кого.** https://bali-villa-management-service.com/. Основной адрес в разметке — bali-villa-account.replit.app, то есть сайт хостится на Replit. Бухгалтерия для иностранных владельцев вилл на Бали. По сути работает один человек: «Abel Yuniartini — Villa Accounting Specialist». Сайт на JavaScript, тексты взяты из бандла.

**2. Первый экран** (порядок восстановлен по бандлу):
- Плашки: «FREE Consultation», «From Rp 3.5m / month».
- Заголовок: «Your Villa. Clean Numbers. Every Month.»
- Подзаголовок: «Bali villa bookkeeping — complete, transparent, owner-side. One clean report every month. No surprises.»
- Кнопки: «WhatsApp Now — FREE», «Book a Free Call».
- Значки: «No Commitment», «WA Reply 24hr», «Commission-Free».

**3. Структура.**
1. Первый экран.
2. «Sound Familiar? You Own the Villa. Not the Numbers.»: 3 боли.
3. «We fix all three. In your first month.» и кнопка «Check Your Villa — FREE».
4. «Why Owners Choose Us».
5. «How It Works»: 3 шага.
6. Цены: 3 пакета.
7. Отзывы.
8. FAQ.
9. Финальный призыв.

**4. Как описаны услуги.** Через боль, словами клиента:
- «You Can't Track the Money — Your manager sends a WhatsApp message. You're 8 time zones away. The numbers are vague — no breakdown, no receipts, nothing you can verify.»
- «You're Being Overcharged — Pool cleaning, gardeners, laundry, repairs — bills arrive every month. But what's the real market rate in Bali? Nobody's checking.»
- «Reports Come Late, If at All — You ask in October. It arrives in November.»
- Процесс: «You send. We work. You see your numbers.» и «Takes you about 10 minutes a week.»

**5. Доказательства.**
- Отзывы с цифрой экономии: «My pool cleaning bill was Rp 2.4 million a month. Abel checked the real Canggu market rate — it should be under Rp 900k. The saving in month one already covered the service fee.» Имён в извлечённом тексте нет.
- Счётчик «villas managed in Bali».
- Граница ответственности: «Formal Indonesian taxes and legal representation are handled by licensed Indonesian professionals.»

**6. Цены и сроки.** Цены показаны:
- Basic Rp 3,500,000 в месяц;
- Control Rp 6,500,000, «MOST POPULAR»;
- Full Service Rp 12,500,000: «Complete financial management for owners with 2+ villas. Quarterly audit included».

Сроки: «We'll review your situation within 24 hours», «Abel had a clean monthly report ready in four weeks» (из отзыва).

**7. Призыв к действию.** WhatsApp и «Book a Free Call». «First consultation is FREE. No commitment required.» Независимость подчёркнута отдельно: «No kickbacks from managers or vendors. Only working for you.» и «100% owner-side — no commission from vendors/managers».

**8. Глазами девелопера.**
- Сильно: боль словами клиента, цена на первом экране, независимость, отзыв, где экономия окупила услугу.
- Слабо: сайт на субдомене Replit, работает один человек, отзывы без имён — всё это бьёт по доверию. Сайт для владельцев готовых вилл, а не для девелоперов.

### C3. Knight Frank UAE, Real Estate Consultancy

**1. Кто и для кого.** https://www.knightfrank.ae/consulting/real-estate-consultancy. Консалтинг Knight Frank в ОАЭ для девелоперов, инвесторов и госструктур.

**2. Первый экран.**
- Надзаголовок: «CONSULTING».
- Заголовок: «Real Estate Consultancy».
- Второй заголовок: «Commercial clarity for complex real estate decisions.»
- Текст: «We deliver strategic consultancy and market intelligence across all major property classes — helping shape projects, guide investment, and unlock lasting value.» Ниже: «...commercially focused guidance underpinned by financial modelling and deep regional insight.»
- Карточка ключевого контакта с кнопками Call и Email.

**3. Структура.**
1. Первый экран.
2. Ключевой контакт.
3. «Our core services»: 4 пункта.
4. Цитата.
5. «Our proven impact»: 7 мини-кейсов.
6. Отрасли.
7. Блок ESG.
8. Исследования.
9. «Next steps»: форма.

**4. Как описаны услуги.** Перечнем работ: «Financial analysis and project financing — Business case development, cost-benefit modelling, public-private financing structures, and return forecasts.», «Strategic development advisory — Land use strategy, planning, development feasibility, and highest and best use analysis.»

**5. Доказательства.** Мини-кейсы в одну строку, с масштабом и результатом, без названий клиентов:
- «Provided strategic guidance on positioning, pricing, and investment potential for a $2 billion mixed-use development, accelerating board approval.»
- «Led land bank prioritisation for a Dubai government entity, ranking 225 plots and preparing business plans to attract private capital for viable sites.»
- «Delivered a financial feasibility study for an extreme sports theme park, enabling third-party investment and equity distribution.»

Плюс «For over 25 years» и рыночные отчёты.

**6. Цены и сроки.** Нет.

**7. Призыв к действию.**
- Кнопки: «Arrange a consultation», «Call us».
- Поля формы: Title (optional), First name, Last name, Email address, Phone number, «How can we help you?».
- После отправки: «A member of our team will be in touch with you as soon as possible to discuss your enquiry.»
- Лид-магнит: рыночные отчёты.

**8. Глазами девелопера.**
- Сильно: формат мини-кейса «масштаб + действие + результат» в одну строку.
- Слабо: проекты на миллиарды и госзаказчики. Средний девелопер почувствует, что ему здесь не место. Нет процесса и документов, есть клише «unlock lasting value».

### C4. Cavendish Maxwell (Дубай)

**1. Кто и для кого.** https://cavendishmaxwell.com/services/strategy-and-consulting/market-and-financial-feasibility-analysis. Оценка и консалтинг в ОАЭ и на Ближнем Востоке. Страница не открылась: проверка на бота.

**[по выдаче поиска, страницу не открыли]:**
- Услуга «Market and Financial Feasibility Analysis» объединяет исследование рынка и финмодель, чтобы понять, жизнеспособен ли проект. Метрики: NPV, IRR, ROI. Модель проверяет допущения при разных состояниях рынка. Итог — вывод «go / no-go».
- Кейсы на сайте:
  - «highest and best use and feasibility study» для 7 участков девелопера в Дубае (2024);
  - мастер-план Academic City площадью 1.6 млн кв. м;
  - «Financial feasibility & economic impact assessment – Muscat».
- По выдаче поиска, в блоге есть статья «how to conduct a market and financial feasibility analysis for real estate projects».

**8. Глазами девелопера.** Структуру и тексты проверить не удалось. По выдаче поиска это одна из немногих компаний, которая прямо называет NPV, IRR и вывод «go / no-go», но через крупную оценочную фирму.

### C5. CBRE Phuket (Таиланд)

**1. Кто и для кого.** Статья-лендинг «CBRE Phuket: Property Research, Consulting and Residential Sales» (https://www.cbre.co.th/insights/articles/cbre-phuket-property-research-consulting-residential-sales) и страница Development Consultancy на cbre.co.th. Обе вернули HTTP 403.

**[по выдаче поиска, страницу не открыли]:**
- «CBRE has operated in Phuket since 2004, combining Phuket property research, consulting and residential sales under one team. Over the past four years, CBRE has served 30+ clients through research and consulting assignments and handled nearly 400 residential transactions valued at more than THB 9 billion.»
- До проектирования или запуска продаж консультируют по спросу, цене, составу юнитов, позиционированию и очерёдности.
- Feasibility-исследования на тайских страницах показывают NPV, срок окупаемости и IRR.

**8. Глазами девелопера.** Сильно: локальные данные о продажах. Слабо: консалтинг и продажи в одной команде. Для девелопера это конфликт интересов: советник, который потом продаёт, заинтересован в оптимистичной цене. Axiom может показать свою независимость как противовес.

### C6. Savills, Global Residential Development Consultancy

**1. Кто и для кого.** https://www.savills.co.uk/services/consultancy/global-residential-development-consultancy/services.aspx. Консалтинг Savills по жилому девелопменту, особенно по branded residences. Клиенты: инвесторы, девелоперы, бренды. Офисы во Вьетнаме, Таиланде, Индонезии, ОАЭ.

**2. Первый экран.**
- Заголовок: «Global Residential Development Consultancy».
- Текст: «Our goal is to provide an end-to-end service to our clients, enabling and guiding them throughout the entire development lifecycle.»
- Кнопка «Contact the team» стоит в конце.

**3. Структура.** Каждая услуга оформлена отдельным заголовком первого уровня (H1):
1. «Market Feasibility Studies».
2. «Brand Premium Studies».
3. «Market Intelligence & Thought Leadership».
4. «Brand & Operator Search and Contract Negotiations».
5. «Operational Advisory».

Дальше кнопка Contact the team и рассылка.

**4. Как описаны услуги.** Перечнем:
- «On behalf of investors, developers and brands, Savills GRD produces bespoke feasibility studies to de-risk and add value to residential and mixed-use projects globally.»
- Интересно: «We undertake brand premium studies, isolating and calculating the percentage price uplift that a brand can command for a scheme.»

**5. Доказательства.** «network of 700+ offices». Списки проектов вынесены в отдельные PDF, на странице их нет.

**6–7.** Цен и сроков нет. Кнопка «Contact the team», подписка на рассылку.

**8. Глазами девелопера.**
- Сильно: идея посчитать надбавку к цене в процентах — понятная денежная ценность.
- Слабо: сплошной текст, перечень, нет доказательств на странице.

### C7. C9 Hotelworks (Пхукет, бутик)

**1. Кто и для кого.** https://c9hotelworks.com/development-advisory. Бутиковый консультант по гостиницам и branded residences из Пхукета. Лицо компании — основатель Bill Barnett. Работают по Азиатско-Тихоокеанскому региону.

**2. Первый экран.**
- Заголовок: «Development Advisory».
- Подзаголовок: «We offer advisory throughout your hospitality development process, from acquisition to construction to operation.»
- Ссылка: «Work with us».

**3. Структура.**
1. Первый экран.
2. «DEVELOPMENT ADVISORY»: текст.
3. «Advisory Process».
4. «Highlighted Projects»: 5 названий.
5. Боковая форма.
6. Рассылка C9 Insider News.

**4. Как описаны услуги.** Начинают с вопроса клиента: «Are you a developer facing the question, “What do I build?” If so, C9 Hotelworks is here to help.» Дальше общие слова: «We are transparent, approachable and innovative.» В перечне услуг на сайте есть «cash flow models, financial projections, appraisals» (по выдаче поиска).

**5. Доказательства.**
- Названия проектов: Holiday Inn and Suites Siracha, MontAzure Phuket, Lub D Hostels и другие.
- Регулярные рыночные отчёты: Phuket Hotel Market Update, The Phuket Luxury Report.
- Личный бренд основателя.
- Счётчики «PROJECTS / LOCATIONS / YEARS’ EXPERIENCE» рисует JavaScript, значения не видны.

**6–7.** Цен и сроков нет. Поля формы: NAME, EMAIL, PHONE NO., MESSAGE. Лид-магниты: рыночные отчёты и рассылка «Get the latest local and regional news updates – with Bill's signature twist.»

**8. Глазами девелопера.**
- Сильно: формулировка «What do I build?» и авторитет через регулярную аналитику рынка.
- Слабо: страница почти пустая. Нет процесса, документов и цифр результата.

### C8. Octo Bali Group (Бали, бутик)

**1. Кто и для кого.** https://octoconsulting.netlify.app/, сайт на субдомене Netlify. Австрийская команда, которая строит и консультирует на Бали. Клиенты — европейские инвесторы.

**2. Первый экран.**
- Надзаголовок: «Real Estate Consulting Bali — Since 2018».
- Заголовок: «Build. Buy. Invest. In Bali — The Right Way.»
- Подзаголовок: «We are an Austrian-led team with more than 60 villas developed in Bali. No guesswork. No false promises. Just seven years of real experience on the ground.»
- Кнопки: «Book a Free Call», «Our Team».
- Цифры в описании для поиска: «60+ villas developed, $16M+ in projects, 7+ years on the ground».

**3. Структура.**
1. Первый экран.
2. Теги услуг.
3. «Who This Is For».
4. «Where We Work».
5. «Three ways we can help you».
6. ROI Calculator.
7. Портфолио.
8. Цитата.
9. «Our Background»: хронология с 2012 года.
10. Команда.
11. «From first call to first result»: 4 шага.
12. Финальный призыв.

**4. Как описаны услуги.** Через стадию клиента: «Whether you're exploring the market for the first time or ready to break ground on your own development, there is a way to work together that makes sense for your stage.» Варианты: «Investment Consulting — A no-nonsense deep dive into whether a deal makes sense for you», «Co-Development — You bring capital. We bring expertise, team, and network.»

**5. Доказательства.**
- Портфолио: локация, год, число вилл, площадь, например «Octo Villas — 8 Villas · 105m² each · Fully Sold».
- Хронология основателя.
- Цитата «Bali is not a passive investment...».

**6. Цены и сроки.** Цен нет. Звонок 30 минут.

**7. Призыв к действию.**
- «Book Your Free Call»: «30 minutes. You tell us where you are... We tell you if and how we can help — honestly, without a sales pitch.» Под кнопкой: «No commitment. No sales pitch. Just an honest conversation.»
- **Лид-магнит: ROI-калькулятор** с примером: «Example — $220k · $140/night · 78% occupancy» → «Gross Yield 18.1%», «Net Yield / year 10.1%». Допущения раскрыты: «After 10% tourism tax, running costs, 20% management fee and a maintenance reserve.»

**8. Глазами девелопера.**
- Сильно: калькулятор с раскрытыми допущениями и сравнением сценариев.
- Слабо: сайт на субдомене. Загрузка 78% и доходность 18.1% без источника выглядят как обещание. Есть клише «No guesswork. No false promises».

### C9. Algedra (Дубай, бутик)

**1. Кто и для кого.** https://algedra.ae/en/services/real-estate-advisory/research-services-feasibility-studies. Компания по дизайну интерьеров и архитектуре в Дубае с направлением real estate advisory. Клиенты: землевладельцы, девелоперы, инвесторы в ОАЭ и странах Залива.

**2. Первый экран.**
- Заголовок H2: «Research Services & Feasibility Studies».
- Под ним: «Know What Your Land Can Do Before You Spend on It» и «Site Analysis · Zoning · Due Diligence».
- Кнопка: «Request a Feasibility Consultation →».

**3. Структура.**
1. Первый экран.
2. Три «Know...».
3. «What a Feasibility Study Covers».
4. «Who a Feasibility Study Is For».
5. «How We Work»: 5 шагов.
6. «From Study to Scheme».
7. «Where We Work».
8. Призыв к действию.
9. Форма.
10. Длинный SEO-подвал про интерьеры.

**4. Как описаны услуги.** Через вопрос клиента: «Holding a plot and weighing what to build? The wrong call costs years and millions; the right one starts with evidence.» Анафора: «Know the site inside out. ... Know what you're allowed to build. ... Know it will hold up.»

**5. Доказательства.** На странице нет.

**6. Цены и сроки.** Цен нет. Обещание: «Request a proposal and a senior consultant replies within one working day.»

**7. Призыв к действию.**
- Поля формы: Full Name, Phone, Email, Subject, Message.
- Шапка формы противоречит странице: «one of our Design Consultants will get back to you at earliest.»

**8. Глазами девелопера.**
- Слабо: в feasibility нет финансовой модели. Есть highest and best use, зонирование и участок, но нет IRR, денежного потока и финансирования. Бренд интерьерный, поэтому доверие к расчётам низкое.
- Пример того, как «feasibility» на рынке Дубая часто означает «что построить», а не «сколько денег и когда».

### C10. Bukit Vista (Бали, бутик)

**1. Кто и для кого.** https://www.bukitvista.com/bali-property-developer. Управляющая компания на Бали со стратегией и оценкой для девелоперов и инвесторов.

**2. Первый экран.**
- Заголовок H2: «Build Profitable Property Investments with Proven Strategies».
- Подзаголовок: «Partner with Bukit Vista to turn insights into high-performing real estate.»
- Цифры: «$61M+ Assets Under Management», «$100M+ Asset Valuation», «$6M+ Assets Under Advisement», «10+ Years Experience».

**3. Структура.**
1. Первый экран с цифрами.
2. Оценка со скидкой «25% OFF».
3. «WHY INVEST IN BALI REAL ESTATE?».
4. Карта роста по отзывам OTA.
5. Статьи.
6. «Our Investment Strategy Services»: 5 пунктов.
7. «OUR PRICING».
8. Эксперт: CEO.
9. Гарантия возврата денег.
10. Партнёры.
11. Ужины с инвесторами.
12. Калькулятор дохода.
13. FAQ.

**4. Как описаны услуги.** Перечнем: «Revenue Projection — Forecast your rental income with precision...», «Market Fit — Pick the right property for the right audience — based on live demand, pricing shifts, and ROI potential.»

**5. Доказательства.**
- Цифры AUM и AUA.
- Карта на данных OTA: «analyzes thousands of rental data points from OTAs».
- Гарантия: «If you find evidence against our analysis, you can get a refund plus USD 100».

**6. Цены и сроки.** Цены показаны: «Land 1500K per Are», «Bedroom 2000K Per Bedroom» (IDR, оценка). При этом висит устаревшая акция: «*Offer valid from November 21, 2024 until November 30, 2024».

**7. Призыв к действию.** «Calculate Your Revenue», «Book a Personal Consultation Now», WhatsApp. Ужины с инвесторами: «We host regular dinners with investors, developers, architects, and property owners every Tuesday and Thursday.» FAQ объясняет, почему консультация платная: «Free consultations are often a marketing tool. Bukit Vista does not sell real estate or accept kickbacks from recommendations.»

**8. Глазами девелопера.**
- Сильно: гарантия и объяснение, почему консультация стоит денег.
- Слабо: обещание доходности «Proven ROI — ... smart investments that yield 10–30% returns» без оснований. Акция двухлетней давности. Страница перегружена.

### Вьетнам: бутика не нашли

В выдаче поиска только крупные и средние игроки:
- Dat Xanh Services FERI (часть группы Dat Xanh);
- Crowe Vietnam;
- Cushman & Wakefield;
- Colliers;
- CBRE;
- KPMG.

Отдельного бутикового консультанта по финмоделям для девелоперов с внятным лендингом найти не удалось. В ОАЭ похожая картина: кроме Algedra в выдаче Crowe UAE (страница не открылась). По выдаче поиска, Crowe UAE обещает модель с «CAPEX, OPEX, revenue forecasts, break-even, ROI, IRR and cash flow» и отчёты «structured for banks and investors».

---

## Словарь клиента: какие слова о ценности встречаются

Подсчёт по скачанным страницам: 18 компаний, по которым есть текст. Заблокированные сайты в подсчёт не вошли. «Сайтов» — у скольких компаний слово встречается хотя бы раз.

| Слово или формула | Сайтов | Как звучит у конкурентов (дословно) | Что это значит для Axiom |
|---|---|---|---|
| trust / trusted | 15 | «lender-trusted audits» (Gridlines), «numbers they can trust» (Graphite), «Can I trust this model?» (Gridlines, курс) | Главный страх клиента — недоверие к цифрам. Отвечать проверяемыми фактами, а не словом «доверие». |
| clarity / clear | 12 | «We bring rigour and clarity to project finance» (Operis), «Commercial clarity for complex real estate decisions» (Knight Frank), «journey to financial clarity» (JMCO) | Затёрто, в заголовок не брать. |
| due diligence / diligence-ready | 12 | «respond quickly and accurately to due diligence requirements» (Kruze) | Для девелопера: «пройти проверку инвестора или банка». |
| confidence | 11 | «give lenders greater confidence that their numbers are right» (Operis), «the right degree of confidence and reliance» (BDO), «Build Your Future With Confidence» (JMCO) | Затёрто. |
| budget | 9 | «Construction budgets change as projects progress» (Wiss), «Open on the date you announced, on the budget you set» (ByBaliBuild) | Рабочее слово, особенно в паре «план-факт». |
| transparent / transparency | 9 | «complete, transparent, owner-side» (BVMS) | Работает только с доказательством: пример отчёта, цена. |
| cash flow / where’s the cash | 7 | «“Where’s the cash?”» (Wiss), «Unlock trapped cash» (CFO Centre), «Weekly cash flow monitoring, 13-week cash flow» (JMCO) | Ключевое для девелопера. Конкуренты говорят о нём в контексте МСБ, а не проекта. |
| independent / owner-side / no kickbacks | 7 | «Independent, lender-trusted audits» (Gridlines), «100% owner-side — no commission from vendors/managers» (BVMS), «Separating the person who checks from the person who builds is the whole point» (ByBaliBuild) | Сильный аргумент для аудита модели и контроля платежей. |
| lender / lender scrutiny / funder | 5 (26 упоминаний) | «hold up under lender scrutiny» (Gridlines), «meet funder, bid, investor and internal control requirements and to satisfy conditions precedent» (BDO) | В ЮВА банковского финансирования девелопмента мало, чаще деньги инвесторов и предпродажи. «Lender-ready» использовать осторожно, лучше «investor-ready». |
| feasibility / highest and best use / go-no-go | 6 | «Know What Your Land Can Do Before You Spend on It» (Algedra), «“What do I build?”» (C9) | На рынке feasibility часто без денег. Axiom может сказать: «feasibility с деньгами: сколько, когда, откуда». |
| fixed fee / no surprises | 4 и 3 | «fixed-fee model audit. No surprises. No embarrassing over-spends.» (Gridlines), «agreed before anything starts, with no costs discovered along the way» (ByBaliBuild) | Обещание фиксированной цены снимает страх. |
| real-time / dashboard / KPI | 4 и 3 | «real-time dashboard ... instead of having to wait 60-90 days» (JMCO) | Прямой язык для услуги контроля платежей. |
| board-ready / investor-ready | 3 и 2 | «Investor-ready reporting» (Graphite), «Walk into every board meeting prepared.» (Graphite), «Built to be forwarded to your board, not just read by you» (ByBaliBuild) | Хорошо ложится на одностраничную сводку для инвестора. |
| bankability / bankable | 1 | «problems that could affect your transaction and, most importantly, its bankability» (Operis) | В выборке почти не используется. Для ЮВА звучит чужеродно. |
| delay = lost revenue | 1 | «Every week of delay is a week without revenue.», «a two-month slip changes the whole return» (ByBaliBuild) | Сильная денежная формула. Axiom может посчитать её в модели. |
| overrun / variance / cost-to-complete | 2 | «identify variances early ... before overruns threaten project viability» (Wiss), «no one running the true cost-to-complete numbers» (Wiss) | Слова есть, но редко. Свободная ниша. |
| yield / ROI для покупателя | 3 | «Gross Yield 18.1%» (Octo), «yield 10–30% returns» (Bukit Vista) | На Бали доходность — язык продаж, часто без обоснования. Axiom может сказать: «цена продажи от целевой доходности покупателя». |
| **peak funding / максимальная потребность в капитале** | **0** | Не встречается ни на одной скачанной странице | **Свободная формулировка.** |
| **NPV / IRR / MOIC** | **0** на скачанных страницах | По выдаче поиска есть только у Cavendish Maxwell и CBRE | Метрики, которые считает Axiom, конкуренты на лендингах почти не называют. |
| DSCR / covenant | 2 | «What happens to our loan covenants if we take a loss on the downtown job?» (Wiss) | Для банковских проектов в ОАЭ. |

**Вывод по словарю.** Конкуренты продают «доверие, ясность, уверенность». Эти слова затёрты и ничего не доказывают. Денежные понятия девелопера («пик финансирования», «кассовый разрыв», «перерасход бюджета», «цена от целевой доходности», «план-факт») на лендингах почти не встречаются. Это главная возможность для текста Axiom.

---

## Общие паттерны

1. **Первый экран из трёх частей: «что мы» + «для кого» + кнопка.** Пример: «Outsourced Accounting and Finance for VC-Backed Startups» (Graphite). Почти никто не начинает с проблемы. Исключения: ByBaliBuild («One person standing between you and your building site.»), BVMS («Your Villa. Clean Numbers. Every Month.»), Wiss (история «Where’s the cash?»).
2. **Кнопка одна и та же: «Tell us about your project», «Contact us», «Book a (free) call».** Бесплатная консультация есть почти у всех. Это стандарт, а не преимущество.
3. **Услуги описаны перечнем работ.** Через ситуации клиента пишут ByBaliBuild, BVMS, Wiss, Gridlines (в блоке «Why») и CFO Centre (через цели).
4. **Доказательства — цифры-счётчики: проекты, годы, страны, миллиарды.** Почти нигде нет результата для клиента: что нашли, сколько сэкономили, что изменилось. Исключения: кейс JMCO с дашбордом, отзыв BVMS про экономию, мини-кейсы Knight Frank, цифра Kruze.
5. **Кейсы описывают проект, а не результат.** У Operis, F1F9 и C9 в кейсе только название объекта и его масштаб.
6. **Цены прячут.** Из 22 компаний цифры показывают 4 (Gridlines, Kruze, BVMS, Bukit Vista). Ещё 3 описывают форму оплаты без цифр (ByBaliBuild, F1F9, JMCO).
7. **Сроки показывают ещё реже.** Gridlines (3–4 дня до первых замечаний), ByBaliBuild (отчёт за 72 часа), обещания ответить за 1 рабочий день или 24 часа.
8. **Лид-магниты.** У крупных — отчёты и рассылки. У бутиков — калькуляторы (Octo, Bukit Vista, Kruze), тест (CFO Centre), примеры моделей (F1F9).
9. **Локальные игроки уходят в WhatsApp.** ByBaliBuild, BVMS, Algedra, Bukit Vista. Международные — в формы.
10. **Специалисты по моделям живут в инфраструктуре и PPP.** Девелопмент жилья и гостиниц в ЮВА как сегмент на их сайтах отсутствует.

## Клише, которых надо избегать

- Превосходные степени без доказательств: «world's # 1», «market-leading», «leading provider», «world-class», «industry-leading».
- Пустые слова о ценности: «rigour and clarity», «unlock lasting value», «confidence and control», «end-to-end service», «bespoke / tailored solutions», «beyond the numbers», «data-driven decisions».
- Эмоциональная вата: «no more restless nights», «of our clients have a more restful sleep!», «Now I sleep well at night», «peace of mind».
- «C-Suite Expertise Without the C-Suite Cost» и «at a fraction of the cost»: шаблон всех fractional-CFO.
- Модные слова: «bulletproof», «game changer», «absolute confidence», «Every board meeting will be your best one ever».
- Антиобещания, которые сами звучат как обещание: «No guesswork. No false promises.», «No pressure, just a conversation».
- Доходность без источника: «yield 10–30% returns», «Gross Yield 18.1%» при загрузке 78%. Для финансового консультанта это подрыв доверия.
- Счётчики без смысла и противоречивые цифры: у Operis на одной главной 1,200 и 1,640 проектов.
- Логотипы, которые не являются клиентами: «companies where our CFOs have previously held roles».
- Устаревшие акции и даты: Bukit Vista в 2026 году показывает скидку «until November 30, 2024».
- Сайт на техническом субдомене (replit.app, netlify.app) для финансовой услуги.

## Пробелы: на какие вопросы девелопера сайты не отвечают

1. **Сколько стоит финмодель девелоперского проекта и от чего зависит цена?** Цену публикует только Gridlines, и то за аудит в инфраструктуре. Цены на модель для девелопмента в выборке нет ни у кого.
2. **Через сколько дней будет первая версия модели и когда окончательная?** Процесс расписан у F1F9, сроков нет нигде.
3. **Что именно я получу? Как выглядит модель, сводка для инвестора, отчёт?** Пример модели показывает F1F9, образцы отчётов о стройке — ByBaliBuild. Одностраничника для инвестора или фрагмента модели девелопера нет ни у кого.
4. **Сколько денег мне нужно на пике и когда?** Можно ли финансировать стройку предпродажами и рассрочками? Понятие «peak funding» не встречается ни разу.
5. **Как выставить цену юнитов и условия рассрочки?** Для off-plan продаж на Бали и в Дубае это ключевой вопрос. Никто его не поднимает. Bukit Vista и Octo говорят о доходности покупателя, но с позиции продавца.
6. **Учитывает ли модель местные налоги и структуры?** PPN, PPh 4(2), PB1, PT PMA, leasehold в Индонезии; иностранная квота в Таиланде; эскроу-счета в ОАЭ. Forvis Mazars Indonesia местной специфики не даёт, у остальных её нет совсем.
7. **Что будет после запуска?** Кто обновляет модель по факту, как идёт план-факт, что делать при отклонении стройки от бюджета? Об этом говорят только JMCO (кейс с дашбордом) и Wiss (variance analysis), оба для США.
8. **Как поймать двойной счёт подрядчика, контролировать платежи и согласования?** Ближе всех BVMS (проверка цен вендоров) и ByBaliBuild (платёж против подтверждённого прогресса). Про систему маршрута заявок и антифрод не говорит никто.
9. **Что проверяется при аудите чужой модели девелопера, какой итоговый документ и есть ли ответственность?** Operis и Gridlines отвечают подробно, но для инфраструктуры. Для недвижимости ответа нет.
10. **Скажете ли вы честно, если проект не окупается?** Вывод «go / no-go» есть только у Cavendish Maxwell (по выдаче поиска). Остальные молчат или обещают доходность.
11. **Кто будет делать работу: старший специалист или младший?** На каком языке и в каком часовом поясе? Ответ «you work directly with the people doing the work» есть у Gridlines, «direct access to our founder» — у Octo. Русского языка для клиентов из СНГ нет ни у кого из выборки.
12. **Конфиденциальность: кто увидит мои цифры?** Отвечают только BVMS («Your data is safe. For your eyes only.») и ByBaliBuild («identified only to you»).
13. **Совместимость с моим бухгалтером или управляющим.** Ответ BVMS («Will my villa manager complain?») и Wiss («complement your existing accounting team, not replace it») — редкость.
14. **Чем вы лучше брокера, который сделает расчёт бесплатно?** Только Bukit Vista объясняет, почему консультация платная. У CBRE консалтинг и продажи в одной команде, поэтому вопрос о конфликте интересов открыт.

## 5 лучших приёмов, которые стоит взять

1. **Таблица «уровень услуги → цена → срок → итоговый документ» (Gridlines, Operis).** Две колонки: Comfort review и Full model audit. В строках итерации, ответственность, первая обратная связь «3‑4 working days», цена «$16‑20k / $32‑40k», документ («Comfort letter» / «Opinion letter»). Под таблицей одна сноска, от чего зависит цена.
   Для Axiom: такая же таблица для аудита модели (экспресс и полный) и для самой модели (базовая и полная). Диапазоны цены, дни до первой версии, число правок, что получает клиент: модель, сводка для инвестора, пояснительная записка.

2. **Боль словами клиента: сценарии провала в одну строку (ByBaliBuild, BVMS, Wiss).** Примеры: «A building site in Bali does not go wrong all at once. It goes wrong line by line.», «Seventy per cent paid, work stopped...», «You ask in October. It arrives in November.», «Do we have the working capital to take on that $8M project?»
   Для Axiom: три-пять коротких сцен из жизни девелопера. Например: «Деньги кончились на 14-м месяце стройки, а продажи стартуют на 18-м». «Подрядчик выставил один счёт дважды». «Инвестор попросил IRR, а модель не сходится после правки цен».

3. **Входной продукт с фиксированной ценой, коротким сроком и зачётом в основной заказ (ByBaliBuild, CFO Centre).** ByBaliBuild продаёт аудит сметы: «a written report within 72 hours, deducted from our fit-out fee if you hand us the rest». CFO Centre даёт тест из 23 вопросов: «In around four minutes, you’ll get a personalised report with your readiness score, your biggest gap and the first thing to fix».
   Для Axiom: «экспресс-проверка вашей модели за N дней по фиксированной цене, засчитывается при заказе полного аудита». Как бесплатный вариант — короткий тест или калькулятор пика финансирования.

4. **Показать, что получит клиент, и процесс с документом на каждом шаге (F1F9, ByBaliBuild).** F1F9: 4 шага, у каждого файл на скачивание (Scoping Template, Start File, Actions Sheet, Example Model) и еженедельные созвоны. ByBaliBuild: «Six stages, one written deliverable at each» и «Both documents below are real, with the project identified only to you».
   Для Axiom: обезличенная сводка для инвестора на одну страницу, скриншот дашборда план-факт и фрагмент модели. Процесс: бриф → допущения → первая версия → правки → передача и сопровождение. На каждом шаге назван документ.

5. **Мини-кейсы в одну строку с масштабом и результатом плюс честный отбор клиентов (Knight Frank, JMCO, Wiss, Kruze).** Knight Frank: «ranking 225 plots and preparing business plans to attract private capital for viable sites». JMCO: «real-time dashboard ... instead of having to wait 60-90 days». Отбор: «Not every construction company needs a fractional CFO» (Wiss), «funded Delaware C-Corps that have raised at least $500K» (Kruze).
   Для Axiom: три-пять обезличенных строк вида «апарт-отель на Бали, две стратегии выхода, цена продажи выведена из доходности 8–12%». Плюс блок «кому мы не подходим», например проектам без земли или без бюджета на модель. Это одновременно доказательство и отсев.

Отдельно стоит взять **заявление о независимости** в формулировках BVMS («No kickbacks from managers or vendors. Only working for you.») и ByBaliBuild («Separating the person who checks from the person who builds is the whole point»). Для аудита моделей и контроля платежей это главный аргумент против брокеров и подрядчиков, которые «считают бесплатно».

---

## Источники

**Открылись (текст собран напрямую):**
- BDO UK: https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services
- Operis: https://www.operis.com/ · https://www.operis.com/model-audit/ · https://www.operis.com/contact/
- F1F9: https://www.f1f9.com/ · https://www.f1f9.com/financial-model-build/ · https://www.f1f9.com/contact-us/
- Gridlines: https://www.gridlines.com/ · https://www.gridlines.com/financial-model-audit/ · https://www.gridlines.com/contact-us/
- Forvis Mazars Indonesia: https://www.forvismazars.com/id/en/services/financial-advisory/project-finance-and-financial-modeling · https://www.forvismazars.com/id/en/industries/financial-services/real-estate
- REFM: https://www.refm.com/ (домен продаётся)
- JMCO: https://www.jmco.com/business-advisory/fractional-cfo-services/construction/ · https://www.jmco.com/industries/real-estate/developers/ · PDF с пакетами: https://www.jmco.com/wp-content/uploads/2025/04/2025_Construction-frac-CFO-Services_Updated.pdf
- Wiss: https://wiss.com/ · https://wiss.com/fractional-cfo-services-for-construction/ · https://wiss.com/business-consulting-services-real-estate/
- The CFO Centre: https://www.cfocentre.com/gb/ · https://www.cfocentre.com/gb/book-a-call · https://www.cfocentre.com/gb/free-business-assessment/ · https://www.cfocentre.com/ae/
- Graphite Financial: https://www.graphitefinancial.com/
- Kruze Consulting: https://kruzeconsulting.com/ · https://kruzeconsulting.com/pricing/
- ByBaliBuild: https://bybalibuild.com/ · https://bybalibuild.com/fees/ · https://bybalibuild.com/professionals/
- Bali Villa Management Service: https://bali-villa-management-service.com/ (тексты из JS-бандла и schema.org)
- Knight Frank UAE: https://www.knightfrank.ae/consulting/real-estate-consultancy
- Savills GRDC: https://www.savills.co.uk/services/consultancy/global-residential-development-consultancy/services.aspx
- C9 Hotelworks: https://c9hotelworks.com/development-advisory · https://c9hotelworks.com/
- Octo Bali Group: https://octoconsulting.netlify.app/
- Algedra: https://algedra.ae/en/services/real-estate-advisory/research-services-feasibility-studies
- Bukit Vista: https://www.bukitvista.com/bali-property-developer

**Не открылись, данные из поисковой выдачи:**
- Toptal: https://www.toptal.com/finance/real-estate-financial-modelers (Cloudflare)
- REFM: https://www.getrefm.com/ (Cloudflare)
- BDO: https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-assurance-and-review (Azure WAF)
- Cavendish Maxwell: https://cavendishmaxwell.com/services/strategy-and-consulting/market-and-financial-feasibility-analysis (проверка на бота)
- CBRE Phuket: https://www.cbre.co.th/insights/articles/cbre-phuket-property-research-consulting-residential-sales (HTTP 403)
- Crowe UAE: https://www.crowe.com/ae/services/advisory/feasibility-studies-and-market-research (HTTP 403)
