# Конкуренты и бенчмарки для нового сайта бутиковой финансово-консалтинговой фирмы

Дата исследования: 26.11.2026
Профиль заказчика (анонимно): около 15 лет в финансах девелопмента и строительства. Клиенты: девелоперы, генподрядчики, инвесторы, а также IT-компании. Рынки: Юго-Восточная Азия (Индонезия, включая Бали, и Таиланд), ОАЭ, Центральная Азия и СНГ (Узбекистан, Казахстан), Россия. Услуги: финансовое моделирование девелоперских проектов, независимый аудит финмоделей, внедрение управленческого учёта и контроля платежей, инвестиционный анализ, CFO-as-a-service (финдиректор на аутсорсе). Есть и SaaS-подобный продукт: Telegram-бот, который превращает присланные сотрудниками чеки и счета в Google-таблицу с поиском дублей. Основной язык сайта будет русский, английская версия появится позже.

---

## 0. Методика и ограничения (прочитать первым)

1. **Как собирались данные.** Прямая загрузка сайтов (WebFetch и curl) в этой сессии заблокирована сетевым allowlist окружения: запросы к operis.com, f1f9.com, gridlines.com и modelcitizn.com вернули ENOTFOUND. Поэтому все данные взяты через поисковый индекс (WebSearch) по публичным страницам, часто с ограничением на домен конкретной компании. Каждое утверждение снабжено ссылкой на страницу, из которой оно взято.
2. **Порядок секций главных страниц восстановлен по фрагментам индекса**, а не по живому рендеру. Где порядок или наличие блока не подтверждены, стоит пометка **[не подтверждено]**. Снимки индекса бывают разного возраста, от нескольких дней до нескольких лет, это тоже отмечено.
3. **Почти все цифры и заявления взяты с сайтов самих компаний** (это саморепрезентация, а не независимая проверка). Противоречия между страницами одного сайта помечены **[противоречие]**.
4. Фирмы, цифры и цитаты не выдумывались. Если факт не найден, так и написано: **«не найдено»**.
5. **Чтобы проверить данные вживую** (порядок блоков, кнопки, мессенджеры), в сетевые настройки окружения нужно добавить хосты сайтов из сводной таблицы (раздел 2). В первую очередь: www.gridlines.com, www.operis.com, financialmodelling.forvismazars.com, www.f1f9.com, www.modelcitizn.com, c9hotelworks.com, ptnsg.com, cavendishmaxwell.com, algedra.ae, kmt.uz, finmodel.kz, acpm.tech, noboring-finance.ru, finrezultat.com, planfact.io, www.cfo.ventures, jazaa.com.

Обозначения уровней: **A**: глобальные, Big4 и mid-tier; **B**: специализированные бутики по моделированию и аудиту моделей; **C**: региональные игроки (SEA, ОАЭ, ЦА); **R**: российский рынок (русскоязычные сайты); **D**: fractional CFO, outsourced FP&A, строительный учёт и системы контроля платежей; **T**: fractional CFO для IT и tech.

---

## 1. Главное (executive summary)

1. **В выборке из 36 компаний не найдено ни одной**, которая на сайте объединяет все четыре направления: моделирование девелопмента, аудит моделей, внедрение контроля платежей и CFO-as-a-service, да ещё с фокусом на SEA, ОАЭ, СНГ и Россию. Рынок поделён между узкими типами игроков (подробнее в разделе 5).
2. **Аудит моделей на Западе — зрелый продукт** с публичной упаковкой: уровни проверки, лимиты ответственности, сроки. Gridlines публикует цены: comfort review обычно $16–20 тыс., full audit $32–40 тыс. для модели около 3 000 уникальных формул ([gridlines.com](https://www.gridlines.com/financial-model-audit/)). Но лидеры (BDO, Forvis Mazars, Operis, Gridlines) работают в основном с проектным финансированием, энергетикой и инфраструктурой, а **не с девелопментом на развивающихся рынках**.
3. **На Бали, в Дубае и Таиланде моделированием занимаются «попутно»**: агентства (BREC), design-build компании (NSG), дизайн-бюро (Algedra), оценщики (Cavendish Maxwell), гостиничные консультанты (C9 Hotelworks, Horwath HTL). У первых трёх есть конфликт интересов: модель помогает продать объект или подряд. NSG прямо пишет, что её пример модели не является «full bank-level feasibility study» ([ptnsg.com](https://ptnsg.com/multi-unit-mixed-use-development-uluwatu/)). Отсюда ниша: **независимая модель и аудит модели «банковского уровня»**.
4. **На русском рынке и в СНГ принято показывать цену «от» и срок «от N дней»** прямо на странице услуги: KMT (Ташкент), Inventica, ПланФакт, Нескучные финансы. Без этого сайт будет выглядеть менее открытым, чем местные конкуренты.
5. **Контроль платежей у девелоперов закрывают софтверные вендоры** (ПланФакт, БИТ.СТРОИТЕЛЬСТВО на 1С) и Big4 для крупных компаний (KPMG Digital CFO). Средний сегмент «методология + быстрое внедрение + сопровождение» на сайтах не представлен как отдельный продукт.
6. **Fractional CFO для IT** (Kruze, Graphite, CFO Ventures, JaZaa, ФинРезультат) и **для стройки** (James Moore, Wiss) — разные миры. В выборке нет никого, кто совмещал бы обе аудитории. Сайту нужны **две отдельные «двери»** по аудиториям.
7. **Отзывы клиентов у специалистов по аудиту моделей встречаются редко.** У Gridlines найден один отзыв, у Operis не найдено ни одного. Доверие строится на премиях (IJGlobal), лимитах ответственности, именных партнёрах и методологии.
8. **Типичная ошибка конкурентов — противоречивые цифры на разных страницах**: Operis (1 640+ против 1 200+ проектов), Kruze (800+ против ~2 000 клиентов), KMT (15 против 17 лет), ФинРезультат (400+ против 300+ проектов), CFO Ventures ($350M против $60M привлечённых средств). Новому сайту нужна **единая «книга цифр»**.
9. **Telegram-бот для чеков как категория стремительно становится типовым продуктом**: есть готовые шаблоны n8n с распознаванием чеков и записью в Google Sheets ([n8n.io](https://n8n.io/workflows/19225)). Отличаться стоит за счёт встроенности в систему контроля платежей (дубли, маршруты согласования, план-факт по объекту), а не самим ботом.

---

## 2. Сводная таблица

| # | Компания | URL | Уровень | География | Ключевые услуги | Прозрачность цен | Основной CTA и контакты |
|---|---|---|---|---|---|---|---|
| 1 | BDO UK, Financial Model Services | bdo.co.uk | A | UK, глобально | Model assurance, review, build, обучение | Нет | Именные партнёры [CTA не подтверждён] |
| 2 | Forvis Mazars Financial Modelling | financialmodelling.forvismazars.com | A | Глобально (AU, SG, UK); есть страница по Индонезии | Аудит моделей, разработка, обучение | Нет (есть обещание по сроку) | Contact / Register [не подтверждено] |
| 3 | Deloitte Middle East, Real Estate Development | deloitte.com/middle-east | A | GCC | Feasibility, HBU, бизнес-планы | Нет | Не найдено |
| 4 | Knight Frank (UAE Consultancy + UK Financial Modelling) | knightfrank.ae, knightfrank.co.uk | A | ОАЭ, UK | Feasibility, HBU, model build и audit | Нет | Именной партнёр: Call / Email |
| 5 | Crowe UAE, Feasibility Studies | crowe.com/ae | A | ОАЭ | Feasibility, финмодели, RERA-аудит | Нет | Не найдено |
| 6 | Horwath HTL (APAC, Бали) | horwathhtl.com | A | Глобально, Бали | Гостиничные feasibility, планирование | Нет | «Connect with us» |
| 7 | KPMG Caucasus & Central Asia, Digital CFO | kpmg.com/kz | A | КЗ, ЦА | FP&A, EPM, управленческая отчётность | Нет | Именной партнёр |
| 8 | Operis | operis.com | B | UK, Канада | Аудит моделей (3 уровня), моделирование, советник | Нет | Офисы, телефон, email |
| 9 | F1F9 | f1f9.com | B | UK, глобально | FAST-моделирование, model review, обучение | Нет | «Contact us today» |
| 10 | Gridlines | gridlines.com | B | Глобально | Аудит моделей, моделирование, обучение | **Да** (диапазоны на аудит) | «Tell us about your project», бронирование |
| 11 | Model Citizn | modelcitizn.com | B | Австралия | Моделирование, fractional CFO, автоматизация | Нет | Телефон, email |
| 12 | Bayfield Training | bayfieldtraining.com | B | UK | Модели недвижимости: build и audit | **Да** (почасовые ставки) | Предварительная оценка по документам |
| 13 | C9 Hotelworks | c9hotelworks.com | C | Таиланд, APAC | Гостиничный и девелоперский консалтинг, feasibility | Нет | [не подтверждено] |
| 14 | Bali Real Estate Consultants (BREC) | balirealestateconsultants.com | C | Бали | Агентство + инвестиционный анализ | Нет | Телефон, email, страницы агентов |
| 15 | NSG Design Build | ptnsg.com | C | Бали | Design-build + инвестиционный консалтинг | Нет | **WhatsApp**, «Let's Talk» |
| 16 | Karyanusa Asia | karyanusaasia.com | C | Бали, Индонезия | Консалтинг + стройка + дизайн | Нет | [не подтверждено] |
| 17 | Cavendish Maxwell | cavendishmaxwell.com | C | ОАЭ, GCC | Оценка, feasibility, данные | Нет | Contact Us по офисам |
| 18 | Algedra | algedra.ae | C | ОАЭ, Турция | Дизайн + консалтинг по недвижимости, feasibility | Нет | **WhatsApp**, 800-номер, email |
| 19 | ACPM | acpm.tech | C | Казахстан (+KG, UZ) | Финансово-технический контроль, cost management, PM | Нет | Телефон, офис |
| 20 | KMT | kmt.uz | C | Узбекистан | Оценка, финмодели, ТЭО, бизнес-планы | **Да** (цена «от», срок «от») | Телефон, email, Telegram (личный аккаунт) |
| 21 | Finmodel.kz | finmodel.kz | C | Казахстан | Бизнес-планы, финмодели | Только сроки | **WhatsApp**, телефон |
| 22 | Альт-Инвест | alt-invest.ru | R | Россия | Финмодели, экспертиза моделей, ПО, обучение | Частично (ПО) | [не подтверждено] |
| 23 | Концепт Девелопмент | conceptdevelopment.ru | R | Россия | Девелоперский консалтинг, финмодели | Нет («индивидуально») | [не подтверждено] |
| 24 | Inventica | inventica.ru | R | Россия | Финмодели и бизнес-планы для банков | **Да** («от 50 тыс. руб.») | Email |
| 25 | CORE.XP | core-xp.ru | R | Россия | Финансово-технический аудит и мониторинг | Нет | [не подтверждено] |
| 26 | Нескучные финансы | noboring-finance.ru | R / T | Россия (+ «несколько стран») | Финдиректор на аутсорсе, диагностика, обучение | **Да** («от 60 000 руб.») | Консультация [текст кнопки не подтверждён] |
| 27 | ФинРезультат | finrezultat.com | R / T | Россия | Финдиректор на аутсорсе, упр. учёт, IT-фокус | Частично (в блоге) | Бесплатная диагностика 30 мин |
| 28 | ПланФакт | planfact.io | R / D | Россия, СНГ | SaaS упр. учёта + внедрение + финдиректор | **Да** (тарифы, внедрение) | Бесплатная встреча, пробный период |
| 29 | Первый Бит Казахстан (БИТ.СТРОИТЕЛЬСТВО) | 1cbit.kz | D | Казахстан | 1С: казначейство и бюджетирование в стройке | Частично | Городские поддомены |
| 30 | James Moore & Co. | jmco.com | D | США | Fractional CFO для стройки, WIP | Нет | Общий контакт |
| 31 | Wiss | wiss.com | D | США | CFO для стройки, модели для девелоперов | Нет | Связаться с практикой |
| 32 | Finline | clutch.co/profile/finlineae | D | ОАЭ | Fractional CFO, учёт, налоги | Нет | Профиль на Clutch |
| 33 | Kruze Consulting | kruzeconsulting.com | T | США | Учёт и CFO для VC-стартапов | **Да** (тарифы) | Бесплатная консультация |
| 34 | Graphite Financial | graphitefinancial.com | T | США | Модульный fractional CFO и учёт | **Да** (модульно) | Assessment call |
| 35 | CFO Ventures | cfo.ventures | T | ОАЭ, KSA | Fractional CFO, fundraising, FP&A | **Да** (часть пакетов) | «Book a Call», пробный период |
| 36 | JaZaa | jazaa.com | T | ОАЭ | Fractional CFO, SaaS CFO, PropTech CFO | **Да** (диапазоны в AED) | Contact |

Источники по каждой строке приведены в профилях ниже.

---

## 3. Профили компаний

### Уровень A. Глобальные, Big4 и mid-tier практики

#### 1. BDO UK: Financial Model Services / Assurance & Review
- **URL:** https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services ; https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-assurance-and-review
- **Уровень и география:** A; UK, сделки по всему миру.
- **Услуги:** проверка моделей по принципу «all cells» (снизу вверх) плюс аналитическая проверка сверху вниз; best practice reviews, integrity reviews, payment mechanism reviews, мониторинг ковенантов; разработка моделей; коучинг и обучение ([страница сервиса](https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services); [build](https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-build); [coaching](https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-coaching-and-training)).
- **Клиенты и сектора:** проектное финансирование, PPP, M&A; специализация на ВИЭ, инфраструктуре и PPP; недвижимость упомянута в списке секторов ([capability statement, май 2024, PDF](https://www.bdo.co.uk/getmedia/172305e8-18b9-4362-8461-d1e5f293c7d6/BDO-Financial-Modelling-Assurance-Services-Capability-Statement-Overview-May-2024.pdf)).
- **Структура сервисной страницы (по индексу):** виды проверок → сектора → подход (у каждой проверки есть руководитель проекта, финальный отчёт утверждает партнёр) → премии → ключевые контакты ([источник](https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services)). Лимиты ответственности не найдены.
- **Доказательства:** IJGlobal «Model Auditor of the Year 2022» по Europe & Africa и MENA; «No 1 Global Model Auditor for 2020 and 2021 by deal value» ([assurance page](https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-assurance-and-review)). Формулировки премий отличаются между страницами **[противоречие]**. Именные партнёры: Kirit Mistry (Head), Brian O'Connell, James Adams ([people](https://www.bdo.co.uk/en-gb/our-people/kirit-mistry)). Есть скачиваемые capability statements в PDF.
- **CTA и контакты:** именные контакты партнёров; форма [не подтверждено]. **Цены:** нет. **Языки:** EN. **Тон:** институциональный, корпоративный.
- **Сильные стороны:** премии и рейтинги, именные партнёры, описанная методология, PDF для комитетов.
- **Слабые стороны:** недвижимость не в фокусе, цен нет, страница построена по типовому корпоративному шаблону.

#### 2. Forvis Mazars Financial Modelling (бывшая Corality)
- **URL:** https://financialmodelling.forvismazars.com/ ; аудит: https://financialmodelling.forvismazars.com/services/financial-model-audit/ ; страница по Индонезии: https://www.forvismazars.com/id/en/services/financial-advisory/project-finance-and-financial-modeling
- **Уровень и география:** A; офисы и курсы в Сиднее, Сингапуре, Лондоне, Перте, Мельбурне. Есть страница по проектному финансированию и моделированию для Индонезии.
- **Услуги:** независимое заключение по транзакционной модели и «red flag report on show-stopper issues in under 5 working days»; основной метод — воспроизведение выходов модели в собственном шаблоне. Коммерческая обоснованность и достоверность исходных данных в стандартный объём не входят ([audit](https://financialmodelling.forvismazars.com/services/financial-model-audit/)). Разработка моделей: «feasibility and investment evaluation models, financing models structured for lender scrutiny and model audit» ([development](https://financialmodelling.forvismazars.com/services/financial-model-development/)). Курс по моделированию инвестиций в недвижимость.
- **Главная страница (по индексу, снимок около 7 дней):** H1 «Financial modelling training from the #1 ranked global model audit practice» → подзаголовок о курсах → блок цифр → «Where most people start» (курсы) → корпоративное обучение → «Modelling services» (audit, development, support, valuations) → футер с городами ([главная](https://financialmodelling.forvismazars.com/)). В другой версии главной был блок «Red flag report in under five days» **[не подтверждено, версии разнятся]**.
- **Доказательства:** «#1 global model audit practice», «2,000+ models given an audit opinion», «20,000+ people taught»; «100+ model audit professionals across seven offices» (более старая страница); IJGlobal Global Model Auditor of the Year 2025 ([главная](https://financialmodelling.forvismazars.com/); [services](https://financialmodelling.forvismazars.com/services/)).
- **CTA:** «Contact», «Register» на старых страницах [не подтверждено для текущей]. **Цены:** нет. **Языки:** EN. **Тон:** экспертный, уверенный, построен на рейтингах.
- **Сильные стороны:** продуктовое обещание по сроку (red flag менее чем за 5 дней), полоса с цифрами, обучение как воронка.
- **Слабые стороны:** главная смешивает аудитории (обучение и аудит), недвижимость не выделена в аудите.

#### 3. Deloitte Middle East: Real Estate Development
- **URL:** https://www.deloitte.com/middle-east/en/services/financial-advisory/services/real-estate-development.html
- **Уровень и география:** A; GCC.
- **Услуги:** market due diligence, financial feasibility, highest and best use, инвестиционные стратегии, бизнес-планы от отдельных объектов до мастер-планов, **оптимизация строящихся и перепрофилирование «замороженных» проектов** ([страница](https://www.deloitte.com/middle-east/en/services/financial-advisory/services/real-estate-development.html)). Оценка по RICS Red Book и консалтинг в гостиничном секторе ([обзор](https://www.deloitte.com/middle-east/en/Industries/real-estate/about/real-estate-in-the-middle-east.html)).
- **Доказательства:** бренд, аналитика (Real Estate Predictions, «Building portfolio resilience», [источник](https://www.deloitte.com/middle-east/en/services/consulting/perspectives/building-portfolio-resilience-in-middle-east-real-estate.html)). Кейсы и команда не найдены.
- **CTA:** не найдено. **Цены:** нет. **Языки:** EN. **Тон:** корпоративный.
- **Сильные стороны:** отдельно названа услуга по «спасению» замороженных проектов. Это сильный угол и для бутика.
- **Слабые стороны:** обезличенность, нет доказательств на странице услуги.

#### 4. Knight Frank: UAE Consultancy + UK Capital Advisory (Financial Modelling)
- **URL:** https://www.knightfrank.ae/consulting/real-estate-consultancy ; https://www.knightfrank.ae/consulting/residential-consultancy ; https://knightfrank.ae/property-development/consultancy ; https://www.knightfrank.co.uk/commercial/services/financial-modelling
- **Уровень и география:** A; ОАЭ и UK.
- **Услуги (ОАЭ):** стратегия землепользования, development feasibility, HBU; в жилом сегменте ценовая и сбытовая стратегия, feasibility, позиционирование, бенчмаркинг конкурентов, financial viability. В гостиничном сегменте заявлено «thousands of feasibility studies» ([hospitality](https://www.knightfrank.ae/consulting/hospitality-tourism-leisure)). Отдельно: cost planning и cash flow forecasting ([cost management](https://www.knightfrank.ae/project-development-services/cost-management)).
- **Услуги (UK):** команда capital advisory регулируется FCA, «decades of experience in financial analysis, model build and model audit», интерактивные дашборды, hold/exit-анализ, сценарии и чувствительность ([UK FM](https://www.knightfrank.co.uk/commercial/services/financial-modelling)).
- **Структура сервисной страницы (Residential Consultancy):** список направлений работы → типы проектов → блок «Why trust us» → именной партнёр Clare Moukabaa (Partner, Head of Residential Consultancy) с кнопками Call и Email → брошюра и отчёт Destination Dubai 2025 (опрошено 387 HNWI) ([страница](https://www.knightfrank.ae/consulting/residential-consultancy)). Форма заявки не найдена. Снимок старый, около 530 дней.
- **Доказательства:** кейсы с цифрами: бизнес-кейс для госзаказчика, по итогам которого одобрен mixed-use проект на USD 2 bn; приоритизация 225 участков земельного банка ([consultancy](https://knightfrank.ae/property-development/consultancy)).
- **Цены:** нет. **Языки:** EN (в URL встречается /en/). **Тон:** премиальный, сдержанный.
- **Сильные стороны:** именной контакт прямо на странице услуги, исследования как лид-магнит, кейсы с измеримым итогом.
- **Слабые стороны:** моделирование вторично по отношению к брокериджу и оценке, контент устарел.

#### 5. Crowe UAE: Feasibility Studies and Business Plan
- **URL:** https://www.crowe.com/ae/services/advisory/feasibility-studies-and-market-research ; RERA-аудит: https://www.crowe.com/ae/services/audit/rera-audits
- **Уровень и география:** A (mid-tier); ОАЭ.
- **Услуги:** feasibility по секторам (в том числе Real Estate): исследование рынка, анализ спроса, финмодели ([страница](https://www.crowe.com/ae/services/advisory/feasibility-studies-and-market-research)); market & financial feasibility и оценка для девелоперов в гостиничном секторе ([HTL](https://www.crowe.com/ae/industries/hotel-tourism-and-leisure)); **аудит по требованиям RERA** (регулятор недвижимости Дубая).
- **Сроки:** первичная выдача поиска сообщала «most studies take 4–12 weeks», но при повторной проверке по домену это **не подтвердилось [не подтверждено]**.
- **Цены:** нет. **Языки:** EN. **Тон:** корпоративный, обобщённый.
- **Сильные стороны:** связка с регуляторными аудитами (RERA).
- **Слабые стороны:** универсальная многоотраслевая подача без глубины в девелопменте.

#### 6. Horwath HTL (Азиатско-Тихоокеанский регион, офис на Бали)
- **URL:** https://horwathhtl.com/ ; проекты: https://horwathhtl.com/project/intercontinental-bali-sanur/ ; отчёт: https://horwathhtl.com/publication/bali-hotel-branded-residences-2026/
- **Уровень и география:** A (глобальный отраслевой); Бали, APAC.
- **Услуги и проекты:** planning & financial feasibility для InterContinental Bali Sanur (затраты, прогноз выручки, чувствительность, итог — финмодель и план реализации); мастер-план и feasibility для West Bali National Park (120 га); strategic value assessment для Waldorf Astoria Bali ([проекты](https://horwathhtl.com/project/master-planning-for-west-bali-national-park/)).
- **Доказательства:** отдельная страница на каждый проект; профили консультантов (Matt Gebbie; Michelle Song, «over 100 hospitality projects since joining in 2007», [профиль](https://horwathhtl.com/singapore/consultant/michelle-song/)); ежегодный отчёт по Бали совместно с Bali Hotels Association и C9 Hotelworks, издание 2026 насчитывает пайплайн 5 641 номер в 45 отелях ([отчёт](https://horwathhtl.com/publication/bali-hotel-branded-residences-2026/)); «55+ offices across 40 countries» ([about](https://horwathhtl.com/about/); на других страницах 50+ и 52 **[противоречие]**).
- **Главная:** блок «Connect with us» [остальной порядок не подтверждён]. **Цены:** нет. **Языки:** EN. **Тон:** экспертный, отраслевой.
- **Сильные стороны:** база проектов по объектам, именные консультанты, регулярная аналитика по Бали.
- **Слабые стороны:** только гостиничный сектор, нет услуг по контролю бюджета и платежей.

#### 7. KPMG Caucasus & Central Asia: Digital CFO
- **URL:** https://kpmg.com/kz/ru/services/consulting/digital-cfo.html ; EPM: https://kpmg.com/kz/ru/services/consulting/digital-cfo/epm-systems-implementation.html ; FP&A: https://kpmg.com/kz/ru/services/consulting/digital-cfo/financial-planning-and-analysis.html
- **Уровень и география:** A; Казахстан, Центральная Азия и Кавказ.
- **Услуги:** FP&A, бюджетирование и прогнозирование, управленческая отчётность и дашборды, рентабельность продуктов и направлений, внедрение EPM, казначейство ([EPM](https://kpmg.com/kz/ru/services/consulting/digital-cfo/epm-systems-implementation.html); [казначейство](https://kpmg.com/kz/ru/services/consulting/digital-cfo/treasury-capital.html)).
- **Доказательства:** именной партнёр Тимур Омашев, руководитель консалтинга KPMG Кавказ и Центральная Азия ([EPM](https://kpmg.com/kz/ru/services/consulting/digital-cfo/epm-systems-implementation.html)). На странице консалтинга есть анонс «KPMG и BI Group: новый этап автоматизации финансовых процессов» ([консалтинг](https://kpmg.com/kz/ru/services/consulting.html); материал: https://kpmg.com/kz/ru/insights/2026/10/bi-group.html). Содержание кейса (упоминается Anaplan) **[не подтверждено]**.
- **Языки:** RU, EN (есть пути /kz/ru/ и /kz/en/). **Цены:** нет. **Тон:** корпоративный.
- **Сильные стороны:** локальное присутствие, системные внедрения у крупных клиентов.
- **Слабые стороны:** ориентирован на крупный бизнес, средним девелоперам и подрядчикам предложение недоступно по формату.

---

### Уровень B. Специализированные бутики по моделированию и аудиту моделей

#### 8. Operis
- **URL:** https://www.operis.com/ ; аудит: https://www.operis.com/model-audit/ ; контакты: https://www.operis.com/contact/
- **Уровень и география:** B; Лондон и Торонто. Мандаты на аудит ведутся только из этих двух офисов ([contact](https://www.operis.com/contact/)).
- **Услуги:** advisory, моделирование, аудит моделей, обучение, налоговые и бухгалтерские проверки ([главная](https://www.operis.com/); [tax](https://www.operis.com/tax-accounting/)).
- **Главная (по индексу, снимок около 304 дней):** заголовок «Leading Independent Advisors in Project Finance»; счётчик «over 1,640 projects undertaken to date» с разбивкой по регионам: 685 UK, 191 Europe, 252 Americas, 15 Asia & Australia, 141 Middle East & Africa. На той же странице есть и «more than 1,200 projects» **[противоречие]** ([главная](https://www.operis.com/)).
- **Структура страницы аудита (лучший шаблон «меню уровней»):** **Formal Model Audit** (Formal Opinion Letter, ответственность до £20 млн) → **Due Diligence Review** (отчёт, ответственность до £100 000) → **High Level Review** (письмо поддержки, без формальной ответственности); подход top-down, Audit Working Paper; «over a hundred model audits each year» ([model audit](https://www.operis.com/model-audit/)); скачиваемый scope of work в PDF ([PDF](https://www.operis.com/pdf/operis-model-audit-scope-of-work.pdf)).
- **Доказательства:** IJGlobal Model Auditor of the Year 2021 в North America и в Europe & Africa ([awards](https://www.operis.com/about-operis/awards/)). Отзывы клиентов **не найдены**.
- **CTA и контакты:** телефоны офисов, info@operis.com. **Цены:** нет. **Языки:** EN. **Тон:** сдержанный, инженерный.
- **Сильные стороны:** чёткая линейка продуктов с уровнем ответственности, глубокая база знаний.
- **Слабые стороны:** Азия почти не представлена (15 проектов), нет отзывов, цифры противоречат друг другу.

#### 9. F1F9
- **URL:** https://www.f1f9.com/ ; build: https://www.f1f9.com/financial-model-build/ ; about: https://www.f1f9.com/about-us/
- **Уровень и география:** B; UK, глобально.
- **Услуги:** обучение, разработка моделей по FAST Standard, model review. Прямо сказано: «We do provide model review services, but we don't provide model audit services» ([build](https://www.f1f9.com/financial-model-build/)).
- **Главная (по индексу):** «F1F9 are Financial Modelling Experts», «Specialists in Excel Modelling», работают с 1999 года → два направления (обучение и build) → «works for leading banks, funds, equity investors…» → «Contact us today»; в навигации Contact us и Client Login ([главная](https://www.f1f9.com/)). Отзывы не найдены.
- **Доказательства:** «140+ infrastructure models delivered»; названные клиенты: University of Bath, Citi, DZ Bank, InfraRed Capital Partners, ING, Investec; кейсы: Ofwat, Mubadala, Masdar, Energia, Eneco ([build](https://www.f1f9.com/financial-model-build/)). Основатель участвовал в создании FAST Standard Organisation в 2011 году ([about](https://www.f1f9.com/about-us/)). Бесплатные e-book и пример модели ([resources](https://www.f1f9.com/download-resources/)).
- **Цены:** нет. **Языки:** EN. **Тон:** методологический, «правильный Excel».
- **Сильные стороны:** собственная методология (FAST) как бренд, честное разграничение review и audit, бесплатные материалы.
- **Слабые стороны:** фокус на инфраструктуре, мало социальных доказательств.

#### 10. Gridlines
- **URL:** https://www.gridlines.com/ ; аудит: https://www.gridlines.com/financial-model-audit/ ; review: https://www.gridlines.com/financial-model-review/
- **Уровень и география:** B; глобально.
- **Позиционирование:** H1 «project finance advisory and financial modelling for energy and infrastructure»; «expert financial advisory & modelling services for forward-thinking businesses» ([главная](https://www.gridlines.com/)); «global project finance advisory and modelling firm, supporting developers, lenders & investors» ([about](https://www.gridlines.com/financial-modelling-experts/)).
- **Структура страницы аудита (лучший шаблон с открытыми ценами):** таблица сравнения comfort review и full audit → цены: comfort review «typically costs $16,000 to $20,000 USD», full audit «$32,000 to $40,000 USD» для модели «around 3,000 unique formulae» → правило по итерациям: «does not charge for iterations» → ответственность: full audit «£5m of professional indemnity cover as standard… extendable to £12m», comfort review «2× fees» → сроки: первые замечания через 3–4 дня, full audit около 6 недель, comfort около 4 недель → «live shared issues list» → FAQ (цена, сроки, методология, итерации, типичные ошибки, PI, списки одобренных аудиторов у кредиторов) → отзыв → CTA «Tell us about your project», «share your model for a fee estimate» ([аудит](https://www.gridlines.com/financial-model-audit/)). Форма заявки визуально **[не подтверждено]**. В карте сайта есть страница «Thank you for your booking!», значит, есть онлайн-бронирование ([sitemap](https://www.gridlines.com/sitemap/)).
- **Доказательства:** отзыв Mark Rider (Financial Modelling Lead, DC Advisory): «Gridlines have been a great addition to the model-audit landscape» ([аудит](https://www.gridlines.com/financial-model-audit/)). Старый пост указывал $25–50 тыс. и около $5 тыс. за итерацию, то есть модель ценообразования менялась ([blog](https://www.gridlines.com/blog/financial-model-audit-secrets-of-pricing-2/)).
- **Языки:** EN. **Тон:** открытый, прямой, «без секретов».
- **Сильные стороны:** эталон прозрачности, FAQ закрывает возражения, политика итераций снимает страх перерасхода.
- **Слабые стороны:** энергетика и инфраструктура, девелопмента нет.

#### 11. Model Citizn
- **URL:** https://www.modelcitizn.com/ ; кейсы: https://www.modelcitizn.com/case-studies/various/
- **Уровень и география:** B; Мельбурн, Австралия; работает с 2016 года ([главная](https://www.modelcitizn.com/)).
- **Услуги:** финансовое и бизнес-моделирование, fractional и virtual CFO, data analytics, автоматизация финансов, обучение руководителей ИИ; продукт **Gen 6 Modelling**: «expert-built models with AI-powered board decks and live dashboards — one source, fully automated» ([главная](https://www.modelcitizn.com/)).
- **Главная и навигация:** Home, About, Services, Case Studies, Knowledge Hub, **Shop**, Contact; на главной блоки Financial Automation, Gen 6 Modelling, Financial and Business Modelling ([главная](https://www.modelcitizn.com/)). Отзывы и кнопка бронирования **не найдены**.
- **Доказательства:** кейсы по недвижимости (разделение участков, студенческое жильё, жилые и коммерческие проекты; модель помогла договориться о долговом финансировании) ([кейс](https://www.modelcitizn.com/case-studies/various/)); заявка на доступное жильё для госзаказчика в 2016 и 2020 годах ([кейс](https://www.modelcitizn.com/case-studies/st-vincents-de-paul/)); основатель Lance Rubin, бывший CFO ([about](https://www.modelcitizn.com/about/our-team/)); тест «8 AI builds tested, best scored 63/80» против человеческого бенчмарка 68/80 ([статья](https://www.modelcitizn.com/knowledge-hub/ai-artefacts/ai-financial-modelling/)).
- **Контакты:** адрес, телефон, info@modelcitizn.com. **Цены:** нет. **Языки:** EN. **Тон:** современный, технологичный, в центре личность основателя.
- **Сильные стороны:** сочетание моделирования и fractional CFO (как у заказчика), продуктовое название, контент про ИИ.
- **Слабые стороны:** размытый фокус, не видно доказательств на главной.

#### 12. Bayfield Training (услуги по моделированию недвижимости)
- **URL:** https://www.bayfieldtraining.com/financial-modelling-services/
- **Уровень и география:** B; UK.
- **Услуги:** build моделей для приобретений, девелопмента и портфелей; аудит («independent reviews to validate model logic, assumptions, and outputs»); сценарии; оценка и инвестиционный анализ ([страница](https://www.bayfieldtraining.com/financial-modelling-services/)).
- **Цены (открыто):** £200 в час для senior modelling consultant, £120 для modelling consultant, £70 для support staff; ориентировочное предложение после изучения материалов (снимок около 13 месяцев) ([страница](https://www.bayfieldtraining.com/financial-modelling-services/)). Однодневный курс по моделированию девелопмента стоит £600 + VAT ([курс](https://www.bayfieldtraining.com/introduction-to-real-estate-development-financial-modelling/)).
- **Языки:** EN. **Тон:** практичный, учебный.
- **Сильные стороны:** специализация на недвижимости, открытые ставки, обучение как воронка.
- **Слабые стороны:** бренд «Training» размывает консалтинговое позиционирование.

---

### Уровень C. Региональные игроки (SEA, ОАЭ, Центральная Азия)

#### 13. C9 Hotelworks (Пхукет, Таиланд)
- **URL:** https://c9hotelworks.com/ ; https://c9hotelworks.com/development-advisory ; https://c9hotelworks.com/who-we-are
- **Уровень и география:** C; Таиланд, APAC, Индийский океан.
- **Услуги:** девять направлений: Hotels & Resorts, Hotel Residences, Real Estate, Development Advisory, Operator Selection, Asset Management, Due Diligence, Market Research, Feasibility Studies. Development advisory включает cash flow models и financial projections ([главная](https://c9hotelworks.com/)).
- **Главная (снимок старый, около 6 лет):** «Discover our industry-acknowledged services» + сетка услуг → «Market reports» → «The good stuff» (счётчики проектов и локаций) ([главная](https://c9hotelworks.com/)).
- **Доказательства:** «over 700 projects across 110 locations», основана в 2003 году ([who we are](https://c9hotelworks.com/who-we-are)); названные проекты: InterContinental Phuket, Mandapa (a Ritz-Carlton Reserve), MontAzure; исследования: пайплайн Пхукета на 2026–2030 годы — 41 проект; Thailand Hotel Investment Guide 2026 совместно с Watson Farley & Williams ([2026](https://c9hotelworks.com/news_year/2026)).
- **CTA:** приглашение обсудить проект [отдельная страница контактов не подтверждена]. **Цены:** нет. **Языки:** EN. **Тон:** отраслевой, аналитический.
- **Сильные стороны:** собственная аналитика как главный актив доверия и SEO, портфель громких брендов.
- **Слабые стороны:** только гостиничный сектор, слабые контакты, устаревший сайт.

#### 14. Bali Real Estate Consultants (BREC)
- **URL:** https://balirealestateconsultants.com/ ; FAQ: https://balirealestateconsultants.com/faq/ ; услуги: https://balirealestateconsultants.com/property-services-bali/
- **Уровень и география:** C; Бали, Ломбок.
- **Услуги:** агентство (продажа и аренда) + анализ: «initial investment review through to financial performance analysis, EBITDA and cash-flow analysis, investment return modelling, and full hotel or resort feasibility studies» ([FAQ](https://balirealestateconsultants.com/faq/)); юридическое сопровождение, девелопмент, релокация через одно контактное лицо ([services](https://balirealestateconsultants.com/property-services-bali/)).
- **Главная:** позиционирование «boutique real estate agency» → поиск объектов (тип, район, статус) → «Our Latest Properties». Навигация: Properties, Specialist Properties, List With Us, Services, FAQ, About Us, Contact Us ([главная](https://balirealestateconsultants.com/)). 2,5% комиссии направляется на благотворительность ([homepage with video](https://balirealestateconsultants.com/homepage-with-video/)).
- **Доказательства и команда:** страницы агентов с личными email и телефонами (сооснователи Marc Hirte, Amadeus Förster) ([agency](https://balirealestateconsultants.com/agency/balirec/)).
- **Контакты:** телефон +62 878 6005 3153, info@balirec.com; в FAQ другие номера **[противоречие]**; WhatsApp явно **не найден**. **Цены:** нет. **Языки:** EN (немецкая версия не найдена). **Тон:** «консьерж», лайфстайл.
- **Сильные стороны:** личные страницы сотрудников.
- **Слабые стороны:** аналитика спрятана в FAQ, на первом плане продажа объектов.

#### 15. NSG Design Build (Бали)
- **URL:** https://ptnsg.com/ ; консалтинг: https://ptnsg.com/service/bali-property-investment-advisory/ ; пример: https://ptnsg.com/multi-unit-mixed-use-development-uluwatu/
- **Уровень и география:** C; Бали, международные проекты (Гоа).
- **Главная (по индексу):** «Bali Based Design And Build Experts» (luxury residential, hospitality, multi-unit) → услуги → «Where We Work» → «How We Deliver» → «Why Choose NSG» → «Our Works» → «Our Process» → «Let's Talk»; кнопка **«WhatsApp us»**; «over 150 projects completed» ([главная](https://ptnsg.com/)). Порядок восстановлен по индексу **[частично не подтверждено]**.
- **Структура страницы консалтинга (хороший шаблон «что вы получите»):** CapEx guardrails → targeted revenue model → investment yield logic → development master timeline → financial risk sensitivity → summary feasibility report; формулировка «Numbers behind the Narrative» для привлечения финансирования ([advisory](https://ptnsg.com/service/bali-property-investment-advisory/)).
- **Доказательства:** опубликованный разбор mixed-use проекта в Улувату (total CapEx IDR 285,1 млрд, включая аренду земли IDR 37,5 млрд; заголовочная доходность 24,2% накопленная, не годовая). Сама NSG оговаривает, что это не «full bank-level feasibility study». Поисковый инструмент обратил внимание, что строка «CapEx + Lease» IDR 348,9 млрд не сходится с итогом 285,1 млрд **[требует проверки]** ([пример](https://ptnsg.com/multi-unit-mixed-use-development-uluwatu/)). Рекомендация закладывать резерв 10–20% ([guide](https://ptnsg.com/bali-real-estate-investment-advisory-and-best-practices/)).
- **Контакты:** WhatsApp (в индексе три разных номера **[противоречие]**), contact@ptnsg.com. **Цены:** нет. **Языки:** EN. **Тон:** премиальный, «под ключ».
- **Сильные стороны:** перечень того, что войдёт в результат, открытый пример, WhatsApp.
- **Слабые стороны:** консалтинг служит воронкой к подряду (конфликт интересов), сами признают, что модель «не банковского уровня».

#### 16. Karyanusa Asia (Бали; «also noted»)
- **URL:** https://karyanusaasia.com/property-consulting/
- Исследование рынка, feasibility, инвестиционная стратегия, оптимизация активов; консалтинг встроен в стройку и дизайн; двуязычная команда EN и Bahasa ([consulting](https://karyanusaasia.com/property-consulting/)). Самоизданные рейтинги «7 Best…», в которых компания ставит себя на первое место ([пример](https://karyanusaasia.com/recommended-bali-contractors/)). Такой SEO-приём подрывает доверие.

#### 17. Cavendish Maxwell (ОАЭ, GCC)
- **URL:** https://cavendishmaxwell.com/ ; feasibility: https://cavendishmaxwell.com/services/strategy-and-consulting/market-and-financial-feasibility-analysis
- **Уровень и география:** C; ОАЭ, Оман, Кувейт, KSA.
- **Главная:** «leading independent firm of chartered surveyors and property consultants operating across the Middle East» → Services → Sectors → Case Studies; навигация Insights, News, Contact Us ([главная](https://cavendishmaxwell.com/)).
- **Сервисная страница feasibility:** исследование рынка + финмодель → вывод go/no-go; NPV, IRR, ROI; стресс-тест сценариев ([feasibility](https://cavendishmaxwell.com/services/strategy-and-consulting/market-and-financial-feasibility-analysis)). Кейс 2021 года для госструктуры Омана: Excel-модель с чувствительностью по продуктовой матрице, стоимости строительства и структуре финансирования ([кейс](https://cavendishmaxwell.com/insights/case-studies/confidential-government-entity-oman)).
- **Доказательства:** основана в 2008 году; «over 120 people… eight offices in the GCC»; член RICS ([about](https://cavendishmaxwell.com/about)); именной руководитель Siraj Ahmed ([strategy](https://cavendishmaxwell.com/services/strategy-and-consulting)); собственная платформа данных Property Monitor и квартальные отчёты по рынку ([report](https://cavendishmaxwell.com/insights/market-reports/residential/dubai-residential-market-performance-q3-2025)).
- **Контакты:** страницы офисов (Dubai Marina) ([Dubai](https://cavendishmaxwell.com/contact-us/dubai)). **Цены:** нет. **Языки:** EN. **Тон:** профессиональный, «сюрвейерский».
- **Сильные стороны:** собственные данные и отчёты, RICS.
- **Слабые стороны:** моделирование — дополнение к оценке, нет контроля исполнения бюджета.

#### 18. Algedra (Дубай, Стамбул)
- **URL:** https://algedra.ae/en/services/real-estate-advisory ; feasibility: https://algedra.ae/en/services/real-estate-advisory/research-services-feasibility-studies
- **Уровень и география:** C; ОАЭ и GCC (KSA, Катар, Кувейт, Бахрейн, Оман), Турция.
- **Сервисная страница:** для кого (девелоперы, инвесторы, землевладельцы) → состав (HBU, анализ участка, зонирование, рынок и спрос, due diligence и риски) → процесс из 5 шагов (бриф → исследование → регуляторика → HBU → выводы) → письменный отчёт ([feasibility](https://algedra.ae/en/services/real-estate-advisory/research-services-feasibility-studies)). По оценке: «point you to the certified valuation where you need one» ([valuation](https://algedra.ae/en/services/real-estate-advisory/property-valuation)).
- **Контакты:** 800-ALGEDRA, **WhatsApp +971 52 811 1106**, hello@algedra.ae, офис в Стамбуле ([advisory](https://algedra.ae/en/services/real-estate-advisory)). ISO-сертификация ([news](https://algedra.ae/en/news/iso-certificate)).
- **Цены и сроки:** не найдены. **Языки:** EN (путь /en/, другие версии не подтверждены). **Тон:** дизайнерский, «из концепции в реальность».
- **Сильные стороны:** понятный процесс, WhatsApp, чётко названная аудитория.
- **Слабые стороны:** финансовая глубина не показана, бренд дизайн-бюро.

#### 19. ACPM: Advanced Controls & Project Management (Алматы)
- **URL:** https://acpm.tech/en ; https://acpm.tech/kz/financial-technical-control ; рекомендации: https://project5346020.tilda.ws/en
- **Уровень и география:** C; Казахстан, есть проекты в Кыргызстане и Узбекистане.
- **Услуги:** управление проектами, технадзор, финансово-технический контроль, cost management (бенчмаркинг, закупки и контракты, cost planning, bid management, post-contract cost control), технический аудит, обучение ([главная](https://acpm.tech/en); [hh.kz](https://hh.kz/employer/6039982)).
- **Доказательства:** заявление «единственная казахстанская компания, применяющая PMI/PMBOK в строительстве» ([hh.kz](https://hh.kz/employer/6039982)); **рекомендательные письма**, например о финансово-техническом аудите для производителя фосфатов и о партнёрстве в KZ, KG и UZ ([tilda](https://project5346020.tilda.ws/en)); в команде директор с PMP и аудитор с 25 годами опыта ([training](https://acpm.tech/en/training/construction-project-cost-management)).
- **Контакты:** офис в Алматы, телефон ([contact](https://acpm.tech/kz/contact)). **Языки:** EN, KZ (по путям URL), RU [на сайте не подтверждено]. **Цены:** нет. **Тон:** инженерный.
- **Сильные стороны:** рекомендательные письма как доказательство (типично для СНГ), стандарты PMI.
- **Слабые стороны:** нет финансового моделирования, часть сайта на поддомене Tilda.

#### 20. KMT: Korporativ Maslahat Tizimlari (Ташкент, Бухара)
- **URL:** https://kmt.uz/en ; финмодель: https://kmt.uz/ru/uslugi/biznes-konsalting/razrabotka-finansovoj-modeli
- **Уровень и география:** C; Узбекистан.
- **Шаблон сервисной страницы (эталон для рынка СНГ):** цена «от» → срок «от» → результат и формат → от чего зависит цена → консультация. Финмодель: «от 5 000 000 сумов», «от 5 рабочих дней», «Excel-файл + пояснительная записка»; цена зависит от отрасли, объёма инвестиций, числа сценариев, глубины анализа и наличия данных ([финмодель](https://kmt.uz/ru/uslugi/biznes-konsalting/razrabotka-finansovoj-modeli)). ТЭО «от 8 000 000 сумов», «от 7 рабочих дней» ([ТЭО](https://kmt.uz/ru/uslugi/biznes-konsalting/teo-tehniko-ekonomicheskoe-obosnovanie)); на английской главной указано «from 5,000,000 UZS» **[противоречие]**. Бизнес-план для банка «от 4 000 000 сумов», бизнес-план ГЧП «от 15 000 000 сумов».
- **Доказательства:** «more than 15 / 17 years» **[противоречие]**; «more than 10,000 valuations» и «20,000+ business projects»; страхование ответственности на 2 000 000 000 UZS ([главная](https://kmt.uz/en)).
- **Контакты:** +998 91 400 81 00, info@kmt.uz, Пн–Сб 09:00–18:00; в разметке ссылка на личный Telegram, а не на канал компании ([главная](https://kmt.uz/en)). **Языки:** RU, EN. **Тон:** деловой, справочный.
- **Сильные стороны:** полная прозрачность по цене и сроку, страховка как довод доверия.
- **Слабые стороны:** универсал (оценка + бизнес-планы), девелоперской специализации нет, цифры не согласованы.

#### 21. Finmodel.kz (Алматы)
- **URL:** https://finmodel.kz/
- **Уровень и география:** C; Казахстан.
- **Услуги и обещания:** бизнес-планы, финмодели, презентации; «более 10 лет» опыта в «большой четвёрке» и крупных банках; сроки: модель «от 2-х дней», бизнес-план «от 3-х дней»; работа под требования Astana Hub и Банка Развития Казахстана; пример: финмодель и презентация для торгового центра в Шардже (ОАЭ) ([главная](https://finmodel.kz/)).
- **Контакты:** телефон, **WhatsApp**, офис ([главная](https://finmodel.kz/)). **Цены:** нет. **Языки:** RU. **Тон:** быстрый сервис.
- **Сильные стороны:** обещание скорости, требования госинститутов развития как якорь.
- **Слабые стороны:** нет имён и команды, универсальная подача.

---

### Уровень R. Российский рынок (русскоязычные сайты)

#### 22. Альт-Инвест
- **URL:** https://www.alt-invest.ru/ ; консалтинг: https://www.alt-invest.ru/consulting/ ; модели: https://www.alt-invest.ru/consulting/models/
- **Уровень:** R (бутик + ПО + обучение).
- **Услуги:** индивидуальные финмодели в Excel «с 1993 года», тиражное ПО (программа «Альт-Инвест» как «стандарт моделирования инвестиционных проектов»), экспертиза и аудит моделей, привлечение финансирования, обучение, в том числе моделирование с ИИ ([консалтинг](https://www.alt-invest.ru/consulting/); [ИИ-курс](https://www.alt-invest.ru/news/2026-09-28/); [финансирование](https://www.alt-invest.ru/consulting/financing/)).
- **Доказательства:** «более 3 000 компаний» пользуются программами; клиенты: РЖД, Газпром, ВТБ, Россети, Спортмастер; в списке рекомендованных РЖД консультантов с 2004 года ([профиль](https://www.alt-invest.ru/company/company-profile/)); **аудит финмоделей девелоперских проектов** (гостиничный комплекс, апарт-отель) для Strategy Partners Group ([новость, 2020](https://www.alt-invest.ru/news/2020-11-10/)); страница отзывов о консалтинге ([отзывы](https://www.alt-invest.ru/consulting/references/)).
- **Цены:** на консалтинг не найдены. **Языки:** RU. **Тон:** академично-экспертный.
- **Сильные стороны:** методологический авторитет, крупные имена, ПО как платформа.
- **Слабые стороны:** свежих кейсов по девелопменту на сайте мало (последний найденный — 2020 год), устаревший визуальный стиль [не подтверждено].

#### 23. Концепт Девелопмент
- **URL:** https://conceptdevelopment.ru/financial-model-project ; https://conceptdevelopment.ru/developers ; кейсы: https://conceptdevelopment.ru/portfolio-i-kejsy
- **Уровень:** R (девелоперский консалтинг).
- **Услуга «Финмодель»:** прогноз доходов и расходов, NPV, IRR, ROI, срок окупаемости, три сценария; аудитория: девелоперы, инвесторы, банки, управляющие компании; оговорка: модель считается только при наличии концепции или проекта; продаётся в пакете с анализом участка, концепцией, 3D, аудитом и due diligence; отдельные страницы по типам объектов (БЦ, МФК, ЦОД) ([финмодель](https://conceptdevelopment.ru/financial-model-project)).
- **Доказательства:** мини-кейсы, например одноэтажный ТЦ на 4 000 м² против двухэтажного на 8 000 м² с выбором по сроку окупаемости ([финмодель](https://conceptdevelopment.ru/financial-model-project)).
- **Цены:** «индивидуально». **Языки:** RU. **Тон:** практический, «на примерах».
- **Сильные стороны:** страницы под тип объекта (SEO), мини-кейсы прямо на странице услуги.
- **Слабые стороны:** нет цен, нет аудита моделей как отдельного продукта.

#### 24. Inventica
- **URL:** https://www.inventica.ru/razrabotka-finansovoy-modeli-dlya-banka ; EN: https://www.inventica.ru/razrabotka-finansovoj-modeli?lang=en
- **Уровень:** R (модели и бизнес-планы под банковское финансирование).
- **Прозрачность:** модели «from 50 thousand RUR», «On average, 5-10 days» ([EN](https://www.inventica.ru/razrabotka-finansovoj-modeli?lang=en)); пакет «бизнес-план склада + финмодель» за 50 000 руб. ([склад](https://www.inventica.ru/biznes-plan-sklada)); пакет для банка: «не менее 1,5–2 месяцев», на ранней стадии «от 3 месяцев» ([для банка](https://www.inventica.ru/razrabotka-finansovoy-modeli-dlya-banka)).
- **Контент доверия:** статьи «Как банк проверяет финансовую модель» (DSCR, стресс-сценарии, прогнозы ЦБ и Минэкономразвития) ([статья](https://www.inventica.ru/post/kak-bank-proveryaet-investicionnyy-proekt)); кейсы (отель 5* на Байкале, горнолыжный курорт) ([кейс](https://www.inventica.ru/post/case-investment-documentation-hotel-baikal-bank-funding)).
- **Контакты:** info@inventica.ru. **Языки:** RU, EN. **Тон:** «говорим языком банка».
- **Сильные стороны:** рамка «для банка», открытые цены и сроки, образовательные статьи.
- **Слабые стороны:** универсальные отрасли, нет ориентации на зарубежные рынки.

#### 25. CORE.XP
- **URL:** https://core-xp.ru/services/financial-and-technical-monitoring/
- **Уровень:** R (финансово-технический аудит и мониторинг).
- **Услуги:** аудит до решения о финансировании, сверка запросов на выборку с фактически выполненными работами, оценка риска незавершения; для девелоперов — план-факт и контроль подрядчиков; смежные услуги: стройконтроль, технадзор, управление стоимостью ([страница](https://core-xp.ru/services/financial-and-technical-monitoring/); [услуги](https://core-xp.ru/services/)).
- **Доказательства:** клиенты и кейсы на странице **не найдены**; часть текста на сайте технически повреждена (по данным индекса).
- **Цены:** нет. **Языки:** RU. **Тон:** технический.
- **Значение для заказчика:** банки покупают именно связку «модель ↔ бюджет ↔ факт». Это аргумент за объединение аудита модели и контроля платежей в одном предложении.

#### 26. Нескучные финансы
- **URL:** https://noboring-finance.ru/ ; услуга: https://noboring-finance.ru/services/finansovyy-direktor-na-autsorse/
- **Уровень:** R / T (финдиректор на аутсорсе, в том числе для IT).
- **Главная и навигация:** «Наводим порядок в финансах бизнеса», «Библиотека бесплатных материалов»; меню: Услуги, Кейсы, О компании, Отзывы, Финансистам, **Газета**, Мероприятия, Партнёрам, Контакты, **НФ ТВ** ([главная](https://noboring-finance.ru/)). Есть отдельные услуги «Диагностика бизнеса» и «Масштабирование» ([диагностика](https://noboring-finance.ru/services/diagnostica/)).
- **Доказательства:** «400+ финансовых директоров» ([услуги](https://noboring-finance.ru/services_new/)); «более 500 компаний из нескольких стран» ([Хабр Карьера](https://career.habr.com/companies/noboring-finance)); IT-кейс «Как айти-компания вышла из финансового кризиса за 10 месяцев» (упоминание, детали не найдены); собственный сервис ФинТабло.
- **Цены:** «от 60 000 ₽»; в статьях встречаются «около 100 000 ₽/мес» и «60–150 тыс. ₽» **[противоречие]** ([статья](https://noboring-finance.ru/gazeta/outsource/)).
- **Языки:** RU. **Тон:** «нескучный», простыми словами, медийный.
- **Сильные стороны:** медиа-бренд (Газета, ТВ), библиотека шаблонов, масштаб.
- **Слабые стороны:** массовый сегмент SMB, отраслевой глубины в стройке не видно.

#### 27. ФинРезультат
- **URL:** https://finrezultat.com/ ; блог для IT: https://www.finrezultat.com/blog/finansovyy-direktor-v-it
- **Уровень:** R / T (финдиректор на аутсорсе с IT-фокусом в контенте).
- **Главная:** hero «Готовый финансовый отдел на аутсорсе по цене одного сотрудника. Выручка есть. Ясности — нет.» → «400+ проектов. Средний рост прибыли клиентов — 23%» → «Бесплатная диагностика за 30 минут» → путь из 3 шагов за 3 месяца (финансовая стратегия → приборная панель → ежемесячные приоритеты) → блок основательницы (Наталья Джораева, 20 лет опыта) → меню: Тарифы, Отзывы, Кейсы, Услуги, База знаний, Контакты ([главная](https://finrezultat.com/)). На другой странице «300+ проектов» **[противоречие]**.
- **Цены:** в блоге диагностика 30–100 тыс. ₽, сопровождение 50–150 тыс. ₽/мес; на сайте «фиксируем стоимость на весь период сотрудничества» ([блог](https://finrezultat.com/blog/finansovyy-direktor-na-autsorse)).
- **IT-контент:** «База знаний… для IT-стартапов, технологических компаний»; кейсы: финтех перед раундом, IT-компания с выручкой 150 млн ₽ и кассовыми разрывами, разработчик CRM перед продажей ([IT-блог](https://www.finrezultat.com/blog/finansovyy-direktor-v-it)); каталоги акселераторов и инвестфондов как лид-магниты ([акселераторы](https://www.finrezultat.com/accelerator)).
- **Мессенджеры:** не найдены. **Языки:** RU. **Тон:** «боль → результат», прямой.
- **Сильные стороны:** сильный hero через боль, сравнение с ценой штатного сотрудника, понятный путь по шагам.
- **Слабые стороны:** цифры не согласованы, стройки нет.

---

### Уровень D. Fractional CFO, строительный учёт и системы контроля платежей

#### 28. ПланФакт (SaaS + внедрение + финдиректор)
- **URL:** https://planfact.io/solutions/construction ; https://planfact.io/services/findirector ; тарифы: https://planfact.io/price
- **Строительный лендинг:** учёт по объектам и этапам, прибыльность договора, долги подрядчиков, платёжный календарь; «более 450 строительных компаний» (на других страницах «3500 компаний» в целом); внедрение под ключ «до 4 недель» ([construction](https://planfact.io/solutions/construction)). Кейс: услуга «Внедрение» за 164 500 руб. + годовая подписка 37 200 руб. (по акции); строительная компания с оборотом 300 млн руб. «экономит… до 1 млн рублей» в первый год ([кейс](https://planfact.io/blog/posts/kak-stroitelnaya-kompaniya-s-oborotom-300-mln-naladila-upravlencheskij-uchet)). **Маршруты согласования платежей в найденных материалах не описаны.**
- **Финдиректор на аутсорсе:** цену называют после бесплатной онлайн-встречи; для бизнеса с оборотом от 2 млн/мес; 2 месяца погружения; сравнение со штатным финдиректором за 150–200 тыс. руб./мес ([findirector](https://planfact.io/services/findirector)).
- **Тарифы SaaS:** 2 050–11 933 ₽/мес при оплате за 24 месяца; 7 дней бесплатно ([price](https://planfact.io/price)). Партнёрская программа для финансовых консультантов ([partners](https://planfact.io/partners)).
- **Языки:** RU. **Тон:** продуктовый, понятный.
- **Значение для заказчика:** одновременно бенчмарк (вертикальные лендинги, цены, кейсы с цифрами) и возможный канал (партнёрская программа). Слабое место — описание процесса согласования и защиты от дублей.

#### 29. Первый Бит Казахстан: БИТ.СТРОИТЕЛЬСТВО (1С)
- **URL:** https://astana.1cbit.kz/1csoft/bit-stroitelstvo-kaznacheystvo-i-byudzhetirovanie-standart/ ; кейсы: https://shymkent.1cbit.kz/blog/business-cases/pervyy-bit-sozdal-sistemu-formirovaniya-byudzhetov-po-obektam-stroitelstva-v-kompanii-euroinvest-dev/
- **Что предлагают:** модуль «Казначейство и бюджетирование»: согласование платежей, бюджеты по объектам, план-факт. Кейс «Евроинвест Девелопмент»: бюджеты по объектам, план-факт, прогноз кассовых разрывов ([кейс](https://shymkent.1cbit.kz/blog/business-cases/pervyy-bit-sozdal-sistemu-formirovaniya-byudzhetov-po-obektam-stroitelstva-v-kompanii-euroinvest-dev/)). Кейс «Скандиа Девелопмент» (Астана): время подготовки отчётности сокращено «в несколько раз» ([кейс](https://astana.1cbit.kz/blog/business-cases/pervyy-bit-avtomatiziroval-uchetnuyu-deyatelnost-v-ooo-skandia-development/)).
- **Ограничения:** модули «Заказчик», «Аренда», «Продажа недвижимости» помечены «Не локализовано под Казахстан»; кейсы 2018–2021 годов (по данным индекса).
- **Паттерн сайта:** городские поддомены (astana., shymkent., kostanai.) для локального SEO.
- **Значение для заказчика:** конкурент по системам контроля платежей. Его слабости — тяжёлое внедрение 1С и пробелы в локализации.

#### 30. James Moore & Co. (Флорида, США)
- **URL:** https://www.jmco.com/business-advisory/fractional-cfo-services/construction/
- **Структура страницы:** «Build Your Future With Confidence» (боли: кэшфлоу и bonding) → услуги (отчётность по контрактам, кастомные расписания, weekly flash reports, KPI, прогноз денежных потоков, бюджеты и отклонения, обучение бухгалтеров, поддержка bonding и surety) → команда (Jeremy Wright, CPA; Scott Withrow, «over 25 years… in the construction industry») → «Case in Point»: стоимость компании выросла «from $250,000 to $12 million in just five years» → «Stay Informed» ([страница](https://www.jmco.com/business-advisory/fractional-cfo-services/construction/)). Три пакета услуг описаны в отдельной статье ([deliverables](https://www.jmco.com/articles/fractional-cfo-construction/fractional-construction-cfo-service/)); есть FAQ-статья ([FAQ](https://www.jmco.com/articles/fractional-cfo-construction/faqs-and-what-to-expect/)).
- **Технологии:** интеграция ProNovos с QuickBooks для автоматического WIP ([discover](https://discover.jmco.com/construction-wip-guide)).
- **Цены:** не найдены. **Языки:** EN. **Тон:** уверенный, «для подрядчиков».
- **Сильные стороны:** отдельная статья о том, что клиент получит на выходе, кейс с цифрами, большая база статей (WIP, job cost).
- **Слабые стороны:** только США, цен нет.

#### 31. Wiss (Нью-Джерси, США)
- **URL:** https://wiss.com/fractional-cfo-services-for-construction/ ; https://wiss.com/financial-modeling-real-estate-development/
- **Стройка:** WIP, job cost, bonding, оборотный капитал; полный fractional CFO или «advisory overlay»; минимальный инструмент — rolling 13-week cash flow; моделирование проекта «40% larger than the current largest job»; целевой клиент с выручкой «$10M–$75M» ([construction](https://wiss.com/fractional-cfo-services-for-construction/)); консультанты с CCIFP ([outsourced CFO](https://wiss.com/outsourced-cfo-services-construction-contractors/)).
- **Девелопмент:** моделирование и CFO advisory на всём цикле; акцент на sources & uses («if that schedule is wrong, every downstream output… is wrong by definition») ([RE modeling](https://wiss.com/financial-modeling-real-estate-development/)); сценарии: −10% заполняемости, +15% стоимости строительства ([consulting](https://wiss.com/business-consulting-services-real-estate/)).
- **Доказательства:** отзыв только в PDF-брошюре ([brochure](https://wiss.com/wp-content/uploads/Brochure_Construction.pdf)). **CTA:** связаться с практикой, онлайн-бронирование не найдено. **Цены:** нет. **Языки:** EN.
- **Сильные стороны:** кластер нишевых SEO-страниц, конкретный размер целевого клиента, конкретные сценарии.
- **Слабые стороны:** нет доказательств на страницах, нет цен.

#### 32. Finline (Дубай; «also noted»)
- **URL:** https://clutch.co/profile/finlineae ; https://www.goodfirms.co/company/finline-ae
- «CFO-Led, Tech-Enabled Finance & Compliance for UAE»; отрасли включают недвижимость и контрактинг; Zoho Books; клиент ERE Homes Real Estate; отзывов на Clutch нет ([Clutch](https://clutch.co/profile/finlineae); [GoodFirms](https://www.goodfirms.co/company/finline-ae)). Показывает, что в ОАЭ рынок fractional CFO для стройки фрагментирован и представлен мелкими игроками без доказательств.

---

### Уровень T. Fractional CFO для IT и tech

#### 33. Kruze Consulting (США)
- **URL:** https://kruzeconsulting.com/ ; тарифы: https://kruzeconsulting.com/pricing/
- **Главная:** «Expert Accounting for VC-Funded Startups», главный CTA — бесплатная консультация; бейдж «7 Years Straight – Inc. 5000» ([главная](https://kruzeconsulting.com/); [about](https://kruzeconsulting.com/about/)).
- **Доказательства:** «Trusted by 800+ Startups», «$15B+ in Funding Raised» ([about](https://kruzeconsulting.com/about/)); на другой странице «около 2 000 VC-backed клиентов» **[противоречие]** ([startup accounting](https://kruzeconsulting.com/startup-accounting/)).
- **Цены:** Basic около $650–850, Founder Timesaver $850–1 500, Premium по запросу, разовый онбординг ([pricing](https://kruzeconsulting.com/pricing/)); ставки CFO и financial modeling $400 в час ([rate card](https://kruzeconsulting.com/kruze-consulting-quickbooks-online-accountant-startups/)); статья о рынке: fractional CFO стоит $8–16 тыс. в месяц ([блог](https://kruzeconsulting.com/blog/startup-cfo-charges/)).
- **Языки:** EN. **Тон:** «для фаундеров», уверенный.
- **Сильные стороны:** узкая аудитория (VC-стартапы), открытые тарифы, SEO-контент о ценах.

#### 34. Graphite Financial (США)
- **URL:** https://www.graphitefinancial.com/ ; сравнения: https://www.graphitefinancial.com/graphite-vs-kruze
- **Цены (модульно):** accounting от $1 500/мес, finance (FP&A) от $2 000/мес, tax от $400/мес, payroll $500/мес, HR $700/мес; онбординг согласуется на assessment call ([vs Burkland](https://www.graphitefinancial.com/graphite-vs-burkland)); в старых материалах «от $1 250/мес» **[противоречие]** ([SaaS CFO](https://www.graphitefinancial.com/blog/saas-fractional-cfo)).
- **Состав FP&A:** владение финмоделью, ежемесячный пакет отчётности, анализ отклонений, rolling reforecast, сценарии ([vs Burkland](https://www.graphitefinancial.com/graphite-vs-burkland)).
- **Паттерн:** страницы «Graphite vs. <конкурент>» (Kruze, Burkland, Bench) перехватывают поисковый спрос по брендам конкурентов. **Языки:** EN.
- **Сильные стороны:** модульная цена, сравнительные страницы.

#### 35. CFO Ventures (Дубай)
- **URL:** https://www.cfo.ventures/ ; fundraising: https://www.cfo.ventures/venture-capital-advisory ; FAQ: https://www.cfo.ventures/faq
- **Услуги:** fractional, interim и virtual CFO, FP&A, fundraising, оценка, M&A; ОАЭ, KSA, MENA ([fractional](https://www.cfo.ventures/fractional-cfo)).
- **Лестница предложений:** бесплатный Readiness Score → Investor Pack за USD 490 → Fundraise Partner от USD 3 500/мес ([fundraising](https://www.cfo.ventures/venture-capital-advisory)); «two-week zero-risk trial», без платы за онбординг, расторжение с уведомлением за месяц; CTA «Book a Call» ([why us](https://www.cfo.ventures/why-us)).
- **Противоречия:** «USD 350 million» и «USD 60M» привлечённых средств; основание в 2019 или 2020 году; целевая выручка $3–20M против $10–100M **[противоречие]** ([about](https://www.cfo.ventures/about); [FAQ](https://www.cfo.ventures/faq)). Основатель Emilio Parente, бывший сотрудник Big 4.
- **Языки:** EN. **Тон:** стартаперский, ориентированный на результат.
- **Сильные стороны:** лестница от бесплатного к платному, пробный период снижает риск.

#### 36. JaZaa Business Services (ОАЭ)
- **URL:** https://jazaa.com/fractional-cfo/ ; PropTech CFO: https://jazaa.com/proptech-cfo/ ; цены: https://jazaa.com/blog/fractional-cfo-cost-uae-dubai/
- **Услуги:** fractional и virtual CFO, подготовка к due diligence, отдельные страницы **SaaS CFO** и **PropTech CFO** ([fractional](https://jazaa.com/fractional-cfo/); [proptech](https://jazaa.com/proptech-cfo/)).
- **Доказательства:** команда с CPA и CMA, «70+ years of combined UAE experience»; отрасли: ритейл, здравоохранение, tech, трейдинг, недвижимость ([fractional](https://jazaa.com/fractional-cfo/)).
- **Цены:** retainer «AED 15,000 and AED 35,000 per month»; для ранних стадий AED 5 000–10 000; проект по привлечению капитала AED 30 000–80 000 ([cost guide](https://jazaa.com/blog/fractional-cfo-cost-uae-dubai/)); онбординг «5 to 7 business days» против «2 to 3 weeks» **[противоречие]** ([virtual CFO](https://jazaa.com/virtual-cfo/)).
- **Языки:** EN. **Тон:** деловой, локальный.
- **Сильные стороны:** вертикальные страницы (SaaS, PropTech) и статья о ценах для SEO.

---

## 4. Синтез

### 4.1. Типовые паттерны главных страниц

| Паттерн | Где встречается | Комментарий |
|---|---|---|
| Hero с нишей и аудиторией | Gridlines («for energy and infrastructure»), NSG («Bali Based Design And Build Experts»), Kruze («for VC-Funded Startups») | Узкая формулировка работает лучше общей фразы «финансовый консалтинг» |
| Hero через боль и экономию | ФинРезультат («по цене одного сотрудника… Выручка есть. Ясности — нет.»), ПланФакт (сравнение со штатным финдиректором) | Типично для русского рынка |
| Полоса цифр | Forvis Mazars (2 000+ / 20 000+), Operis (1 640+ по регионам), C9 (700+ / 110), NSG (150+), ФинРезультат (400+ / 23%), Kruze (800+ / $15B+) | Часто противоречит другим страницам (см. п. 8 раздела 1) |
| Сетка услуг → отдельные страницы | все | Каждая услуга получает свою посадочную страницу |
| Процесс по шагам | NSG (How We Deliver / Our Process), Algedra (5 шагов), ФинРезультат (3 шага за 3 месяца) | Снижает неопределённость для клиента |
| Портфель и кейсы | NSG «Our Works», C9 featured projects, Horwath (страницы проектов), JMCO «Case in Point» | Названные объекты сильнее анонимных |
| Аналитика и отчёты | C9 «Market reports», Horwath (отчёт по Бали), Cavendish Maxwell (квартальные отчёты), Knight Frank (Destination Dubai) | Главный SEO- и trust-актив региональных игроков |
| Основатель и команда | ФинРезультат (основательница), Model Citizn (Lance Rubin), JMCO (профили) | Для бутика критично |
| База знаний и бесплатные материалы | F1F9 (resources), Нескучные финансы (Газета, библиотека), ФинРезультат (База знаний), Gridlines (blog, academy), JMCO (articles) | Лид-магниты и SEO |
| Финальный CTA | «Let's Talk» (NSG), «Book a Call» (CFO Ventures), бесплатная диагностика (ФинРезультат), бесплатная консультация (Kruze) | Низкий порог первого шага |

**Обобщённый порядок, который чаще всего восстанавливается по индексу:** Hero (ниша + обещание + CTA) → цифры → услуги → процесс → кейсы и проекты → команда или основатель → аналитика и материалы → отзывы или логотипы (у специалистов по аудиту часто отсутствуют) → финальный CTA и контакты.

### 4.2. Лучшие шаблоны сервисных страниц в нише

**Шаблон 1. Аудит модели, «прозрачная цена» (Gridlines):** таблица уровней (comfort / full) → диапазоны цен с привязкой к размеру модели → правило по итерациям → лимит ответственности → сроки (первые замечания, финальная подпись) → как идёт работа (общий список замечаний в реальном времени) → FAQ → отзыв → CTA «пришлите модель для оценки стоимости» ([gridlines.com](https://www.gridlines.com/financial-model-audit/)).

**Шаблон 2. Аудит модели, «меню уровней ответственности» (Operis):** три продукта, у каждого свой документ (Opinion Letter / Report / Letter of support) и свой лимит (£20 млн / £100 000 / нет), плюс PDF со scope of work ([operis.com](https://www.operis.com/model-audit/)).

**Шаблон 3. Услуга СНГ, «цена — срок — результат» (KMT, Inventica):** «от X», «от N дней», формат результата (Excel + записка), от чего зависит цена, консультация ([kmt.uz](https://kmt.uz/ru/uslugi/biznes-konsalting/razrabotka-finansovoj-modeli); [inventica.ru](https://www.inventica.ru/razrabotka-finansovoj-modeli?lang=en)).

**Шаблон 4. Состав результата + пример (NSG):** перечень компонентов (CapEx guardrails, revenue model, timeline, sensitivity, summary report) + опубликованный разбор проекта ([ptnsg.com](https://ptnsg.com/service/bali-property-investment-advisory/)). Важно: пример должен сходиться арифметически, иначе он работает против вас.

**Шаблон 5. Fractional CFO, «для кого и с какими инструментами» (Wiss, JMCO):** профиль клиента по выручке ($10–75M), обязательные инструменты (13-недельный cash flow, WIP), сценарии, пакеты услуг, команда, кейс с цифрами ([wiss.com](https://wiss.com/fractional-cfo-services-for-construction/); [jmco.com](https://www.jmco.com/business-advisory/fractional-cfo-services/construction/)).

**Шаблон 6. Лестница предложений (CFO Ventures, ПланФакт):** бесплатная оценка → фиксированный «вводный» продукт → подписка; пробный период; без платы за онбординг ([cfo.ventures](https://www.cfo.ventures/venture-capital-advisory); [planfact.io](https://planfact.io/price)).

**Рекомендуемый гибридный шаблон для заказчика:** (1) кому и в какой ситуации нужна услуга → (2) что вы получите (артефакты списком, со скриншотом или фрагментом) → (3) уровни или пакеты с ценой «от» и сроком «от» → (4) процесс по шагам с днями → (5) от чего зависит цена → (6) мини-кейс с цифрами и географией → (7) кто делает (имя, опыт) → (8) FAQ (5–8 вопросов) → (9) CTA с загрузкой файла или мессенджером.

### 4.3. Паттерны доверия, которые работают в финансовом консалтинге

1. **Премии и рейтинги:** IJGlobal Model Auditor of the Year (BDO, Operis, Forvis Mazars). Бутику без премий их заменяют названные проекты и рекомендательные письма.
2. **Явно указанная ответственность и страховка:** Operis (до £20 млн), Gridlines (£5–12 млн), KMT (страховка на 2 млрд сум). Указывать только при наличии реального полиса.
3. **Именные партнёры с прямым контактом на странице услуги:** BDO, Knight Frank, Cavendish Maxwell, KPMG.
4. **Квалификации:** RICS (Cavendish Maxwell, Deloitte), FCA (Knight Frank UK), CPA и CMA (JaZaa), CCIFP (Wiss), PMP (ACPM), FAST Standard (F1F9).
5. **Названные клиенты и объекты:** F1F9 (Citi, ING, Mubadala), Альт-Инвест (РЖД, ВТБ), C9 и Horwath (бренды отелей).
6. **Измеримые результаты:** Knight Frank (одобрение проекта на USD 2 bn), JMCO ($250k → $12M), ПланФакт (до 1 млн руб. экономии).
7. **Открытая методология:** Forvis Mazars (воспроизведение модели), BDO (all-cells), Gridlines (общий список замечаний), F1F9 (FAST).
8. **Собственная аналитика:** C9, Horwath, Cavendish Maxwell.
9. **Рекомендательные письма** (ACPM): характерный и ожидаемый приём для аудитории СНГ.
10. **Слабое место всей ниши — отзывы.** У специалистов по аудиту их почти нет (у Gridlines один, у Operis не найдено). Видео- или текстовые отзывы с именем и должностью дадут бутику заметное преимущество.

### 4.4. Как российские конкуренты подают услуги (для русскоязычной версии)

- **Цена «от» и срок «от» прямо на странице:** Нескучные финансы («от 60 000 ₽»), Inventica («от 50 тыс. руб.», «5–10 дней»), ПланФакт (тарифы, цена внедрения в кейсе), KMT («от 5 000 000 сумов», «от 5 рабочих дней»).
- **Сравнение со штатной единицей:** ФинРезультат («по цене одного сотрудника»), ПланФакт (150–200 тыс. руб. за штатного финдиректора).
- **Бесплатный первый шаг:** диагностика за 30 минут (ФинРезультат), бесплатная онлайн-встреча (ПланФакт), диагностика (Нескучные финансы).
- **Медиа и бесплатные материалы:** «Газета» и «НФ ТВ» (Нескучные финансы), «База знаний» и каталоги акселераторов и фондов (ФинРезультат), вебинары (Альт-Инвест).
- **Кейсы с рублёвыми цифрами** (ПланФакт, ФинРезультат) и **громкие имена клиентов** (Альт-Инвест).
- **Рамка «для банка»:** Inventica (DSCR, прогнозы ЦБ), CORE.XP (контроль выборки кредита).
- **Вертикальные страницы:** ПланФакт /solutions/construction, Концепт Девелопмент (страницы под БЦ, МФК, ЦОД).
- **Тон:** прямой, «боль → результат», простыми словами, без англицизмов в заголовках (при этом CFO, IRR, DSCR допустимы в тексте).
- **Типичные минусы:** противоречивые цифры, отсутствие имён исполнителей у небольших фирм (Finmodel.kz), устаревшие кейсы (Альт-Инвест, 2020 год).

### 4.5. Позиционные пробелы, которые может занять бутик

1. **Единый подрядчик «модель → аудит → контроль исполнения»** для девелопмента. В выборке такого не найдено. Банки покупают как раз связку «модель ↔ бюджет ↔ факт» (CORE.XP, Inventica). Бутик может продавать «финансовый контур проекта» целиком.
2. **Независимый аудит моделей девелоперских проектов на развивающихся рынках.** Лидеры аудита работают с инфраструктурой и энергетикой. На Бали, в Дубае и Таиланде модели делают агенты, оценщики и подрядчики с конфликтом интересов. Позиционирование: «независимо, без комиссии с продажи и подряда».
3. **«Банковский уровень» против «уровня продаж».** NSG сама признаёт, что её модель не банковского уровня. Пакет «модель для банка или инвестора» с чек-листом требований кредитора — свободная ниша.
4. **Прозрачная цена аудита модели в регионе.** В SEA, ОАЭ и ЦА цены на аудит не найдены. Фиксированные пакеты по размеру модели (по образцу Gridlines) выделят бутик.
5. **Контроль платежей для среднего девелопера и генподрядчика.** Сейчас выбор такой: SaaS без описанного маршрута согласования (ПланФакт), тяжёлая 1С с пробелами локализации (БИТ, Казахстан) или Big4 для крупных (KPMG). Ниша: «методология + внедрение за N недель + Telegram-бот + сопровождение».
6. **Одна команда для четырёх регионов и двух языков.** В выборке не найдено сайтов на RU и EN, которые одновременно работают на СНГ и SEA/ОАЭ. Можно продавать сопровождение проектов девелоперов из СНГ в Дубае и на Бали (и обратно) [гипотеза, требует проверки спроса].
7. **Две аудитории — стройка и IT — у одного финдиректора.** У конкурентов они не пересекаются. Это не пробел, который нужно «склеивать» на одной странице, а повод для двух входов с общим ядром доверия (команда, методология, инструменты).
8. **«Спасение» замороженных и проблемных проектов.** У Deloitte ME это отдельная услуга ([deloitte.com](https://www.deloitte.com/middle-east/en/services/financial-advisory/services/real-estate-development.html)); у бутиков в регионе такого предложения не найдено.

### 4.6. Бенчмарки для Telegram-бота (чеки → Google Sheets с поиском дублей)

- Готовые шаблоны n8n: фото чека в Telegram → распознавание (GPT-4o-mini Vision или Gemini) → проверка по правилам и существующим заявкам → автоодобрение или подтверждение руководителем → запись в Google Sheets ([n8n 19225](https://n8n.io/workflows/19225); [n8n 16166](https://n8n.io/workflows/16166)). Это значит, что функциональность становится типовой.
- Российские аналоги: «Мобс» (финансы в Google Таблицах через Telegram) ([vc.ru](https://vc.ru/91098-mobs-telegram-bot-dlya-vedeniya-finansov-v-google-tablicah)), приложение «Запись расходов» для МойСклад ([moysklad.ru](https://www.moysklad.ru/integratsii/apps/costaccounting-fluorite/)), кейс бота расходов с выгрузкой в 1С ([workspace.ru](https://workspace.ru/cases/bot-ucheta-rashodov-iz-telegram-srazu-v-1s-bez-ruchnoy-sverki/)).
- **Вывод:** продавать бот стоит не как отдельный SaaS, а как **«вход» в систему контроля платежей**. Его сильные стороны: поиск дублей, привязка к объекту и статье BOQ, маршрут согласования, план-факт. Нужны демо (GIF или видео 30–60 секунд), сценарий «как это выглядит у прораба и у собственника», понятная цена или пробный период.

---

## 5. Десять конкретных рекомендаций для нового сайта

1. **Архитектура с двумя входами и тремя осями.** На главной две «двери»: «Девелоперам и подрядчикам» и «IT-компаниям». Ниже сетка из 5 услуг: финмодель, аудит модели, контроль платежей, инвестиционный анализ, финдиректор на аутсорсе. Под каждую связку «услуга × аудитория» своя посадочная страница. Отдельные географические страницы: Бали и Индонезия, Таиланд, ОАЭ, Узбекистан и Казахстан, Россия. Образец: кластер нишевых страниц Wiss, вертикальные лендинги ПланФакта и JaZaa (SaaS CFO, PropTech CFO).

2. **Hero с конкретикой, а не «финансовый консалтинг».** Формула: кому + что + доказательство + два CTA. Пример каркаса: «Финансовые модели, аудит моделей и контроль платежей для девелоперов и подрядчиков. 15 лет, [N] проектов, Бали / Дубай / Ташкент / Алматы». Основной CTA: «Отправить модель на экспресс-оценку» (с загрузкой файла). Второй: Telegram или WhatsApp. Цифры подставлять только из проверенной «книги цифр».

3. **Страница аудита модели по образцу Gridlines и Operis.** Три уровня, например «экспресс-ревью», «полный аудит», «аудит для банка или инвестора с заключением». Для каждого: что проверяем, формат результата (red flag отчёт, полный отчёт, письмо-заключение), срок первых замечаний в днях, цена «от» в зависимости от размера модели, политика по итерациям («повторная проверка исправлений включена»). Добавить обезличенный пример red flag отчёта в PDF и FAQ. Лимит ответственности упоминать **только при наличии полиса**.

4. **Цена «от» и срок «от» на каждой сервисной странице**, как это принято у KMT, Inventica, ПланФакта и Нескучных финансов. Рядом блок «от чего зависит цена» (число очередей и фаз, сценарии, валюта, данные клиента, срочность). Для финдиректора добавить пакеты и сравнение «штатный CFO против аутсорса» (приём ФинРезультата и ПланФакта).

5. **Контроль платежей как продукт с названием и схемой.** Нужна схема маршрута «заявка → согласование → проверка дублей → оплата → план-факт по объекту и BOQ → дашборд собственника». Плюс срок внедрения в неделях, состав результата (регламент, матрица полномочий, шаблоны, дашборд, обучение) и метрики «до и после». Telegram-бот показать как первый шаг с демо-видео. Так закрывается слабое место ПланФакта (маршрут согласования не описан) и БИТ (тяжёлая 1С, пробелы локализации).

6. **Единая система доказательств.** (а) «Книга цифр»: одно значение каждой метрики на всём сайте, чтобы избежать противоречий, как у Operis, Kruze, KMT, ФинРезультата. (б) Кейсы в одном формате: контекст → задача → что сделали → цифры → артефакт → география и тип объекта, при необходимости обезличенно. (в) Рекомендательные письма для аудитории СНГ (как у ACPM). (г) Отзывы с именем и должностью, которых почти нет у специалистов по аудиту.

7. **Страница «Команда и методология».** Биография основателя: 15 лет, названные типы проектов и регионы, реальные квалификации (указывать только подтверждаемые). Страница «Как мы строим модели»: стандарты структуры (FAST, если применяется), встроенные проверки, контроль версий, скриншот структуры модели. Пример — F1F9 и FAST, Forvis Mazars и воспроизведение модели. Для аудитории банков упомянуть DSCR, LLCR и требования кредиторов (Inventica).

8. **Лид-магниты и региональная аналитика.** «20 ошибок в финмодели девелопера» (чек-лист), шаблон помесячного cash flow, заметки по рынкам: аренда земли (leasehold) и налоги на Бали, escrow и RERA в Дубае, проектное финансирование в Узбекистане и Казахстане. Формат по образцу C9 Hotelworks, Horwath и Cavendish Maxwell (отчёты) и Нескучных финансов (библиотека, «Газета»). Скачивание по email для наполнения CRM.

9. **Контакты под географию.** Telegram — основной канал для России и СНГ. WhatsApp — для ОАЭ, SEA и Казахстана (как у NSG, Algedra, Finmodel.kz). Онлайн-бронирование звонка для международных клиентов (по образцу Gridlines). Короткая форма с полем загрузки модели. Показать часовые пояса, срок ответа (например, «в течение рабочего дня») и именной контакт на каждой сервисной странице (как у Knight Frank и BDO). Telegram должен вести на аккаунт компании, а не на личный (ошибка KMT).

10. **Финдиректор на аутсорсе с низким порогом входа и раздельными сценариями.** Для стройки: WIP, BOQ, платёжный календарь, 13-недельный cash flow (Wiss, JMCO). Для IT: MRR, churn, CAC и LTV, подготовка к раунду (Kruze, JaZaa, CFO Ventures). Первый шаг: бесплатная диагностика 30–45 минут или платный фиксированный «финансовый аудит за 2 недели» с зачётом в абонемент (лестница CFO Ventures и ПланФакта). Указать целевой размер клиента (по выручке) и условия выхода (уведомление за месяц, как у CFO Ventures). Русская версия первая, английская зеркальная, с hreflang. Термины (IRR, NPV, DSCR, CFO) оставить латиницей, но пояснять их при первом упоминании.

---

## 6. Приложение

### 6.1. Что не удалось проверить и почему
- Живой порядок блоков, кнопки и мессенджеры на всех сайтах: прямая загрузка заблокирована сетевым allowlist окружения (раздел 0). Данные восстановлены по поисковому индексу.
- Срок «4–12 недель» у Crowe UAE не подтвердился при повторной проверке.
- Содержание кейса KPMG и BI Group не подтверждено.
- Наличие форм заявки у Gridlines, BDO, Knight Frank визуально не подтверждено.
- У Нескучных финансов и ФинРезультата наличие Telegram и WhatsApp не подтверждено.

### 6.2. Основные источники (по компаниям)
- BDO: https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services ; https://www.bdo.co.uk/en-gb/services/advisory/financial-model-services/financial-model-assurance-and-review
- Forvis Mazars: https://financialmodelling.forvismazars.com/ ; https://financialmodelling.forvismazars.com/services/financial-model-audit/
- Deloitte ME: https://www.deloitte.com/middle-east/en/services/financial-advisory/services/real-estate-development.html
- Knight Frank: https://www.knightfrank.ae/consulting/residential-consultancy ; https://knightfrank.ae/property-development/consultancy ; https://www.knightfrank.co.uk/commercial/services/financial-modelling
- Crowe UAE: https://www.crowe.com/ae/services/advisory/feasibility-studies-and-market-research
- Horwath HTL: https://horwathhtl.com/project/intercontinental-bali-sanur/ ; https://horwathhtl.com/publication/bali-hotel-branded-residences-2026/
- KPMG KZ: https://kpmg.com/kz/ru/services/consulting/digital-cfo/epm-systems-implementation.html
- Operis: https://www.operis.com/ ; https://www.operis.com/model-audit/ ; https://www.operis.com/about-operis/awards/
- F1F9: https://www.f1f9.com/ ; https://www.f1f9.com/financial-model-build/
- Gridlines: https://www.gridlines.com/financial-model-audit/
- Model Citizn: https://www.modelcitizn.com/
- Bayfield: https://www.bayfieldtraining.com/financial-modelling-services/
- C9 Hotelworks: https://c9hotelworks.com/ ; https://c9hotelworks.com/who-we-are
- BREC: https://balirealestateconsultants.com/faq/
- NSG: https://ptnsg.com/ ; https://ptnsg.com/service/bali-property-investment-advisory/
- Karyanusa Asia: https://karyanusaasia.com/property-consulting/
- Cavendish Maxwell: https://cavendishmaxwell.com/about ; https://cavendishmaxwell.com/services/strategy-and-consulting/market-and-financial-feasibility-analysis
- Algedra: https://algedra.ae/en/services/real-estate-advisory/research-services-feasibility-studies
- ACPM: https://acpm.tech/en ; https://hh.kz/employer/6039982
- KMT: https://kmt.uz/ru/uslugi/biznes-konsalting/razrabotka-finansovoj-modeli ; https://kmt.uz/en
- Finmodel.kz: https://finmodel.kz/
- Альт-Инвест: https://www.alt-invest.ru/consulting/ ; https://www.alt-invest.ru/news/2020-11-10/
- Концепт Девелопмент: https://conceptdevelopment.ru/financial-model-project
- Inventica: https://www.inventica.ru/razrabotka-finansovoy-modeli-dlya-banka
- CORE.XP: https://core-xp.ru/services/financial-and-technical-monitoring/
- Нескучные финансы: https://noboring-finance.ru/ ; https://career.habr.com/companies/noboring-finance
- ФинРезультат: https://finrezultat.com/ ; https://finrezultat.com/blog/finansovyy-direktor-na-autsorse
- ПланФакт: https://planfact.io/solutions/construction ; https://planfact.io/services/findirector ; https://planfact.io/price
- Первый Бит KZ: https://astana.1cbit.kz/1csoft/bit-stroitelstvo-kaznacheystvo-i-byudzhetirovanie-standart/
- James Moore: https://www.jmco.com/business-advisory/fractional-cfo-services/construction/
- Wiss: https://wiss.com/fractional-cfo-services-for-construction/ ; https://wiss.com/financial-modeling-real-estate-development/
- Finline: https://clutch.co/profile/finlineae
- Kruze: https://kruzeconsulting.com/pricing/ ; https://kruzeconsulting.com/about/
- Graphite: https://www.graphitefinancial.com/graphite-vs-burkland
- CFO Ventures: https://www.cfo.ventures/venture-capital-advisory ; https://www.cfo.ventures/faq
- JaZaa: https://jazaa.com/fractional-cfo/ ; https://jazaa.com/blog/fractional-cfo-cost-uae-dubai/
- Telegram-боты и шаблоны: https://n8n.io/workflows/19225 ; https://vc.ru/91098-mobs-telegram-bot-dlya-vedeniya-finansov-v-google-tablicah ; https://www.moysklad.ru/integratsii/apps/costaccounting-fluorite/
