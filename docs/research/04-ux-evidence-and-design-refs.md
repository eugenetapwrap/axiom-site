# 04. Доказательная база по UX и дизайн-референсы для лендинга Axiom

Дата: 26.11.2026. Задача лендинга: за 10–20 секунд человек понимает, где он, какие проблемы ему решат и что делать дальше. Главное действие — заявка через форму.

**Как собирал.** Первоисточники читал целиком, если они открывались: NN/g, Hinge (PDF), Forrester, Stanford, Baymard, Google Research, SRA, Kitces, Gridlines, Kruze, Graphite, Pilot. Сайты-референсы снимал в Playwright/Chromium: 1440×900, deviceScaleFactor 1. Шрифты, кегли и цвета брал из вычисленных стилей страницы (`getComputedStyle`), а не на глаз. Поддержку кириллицы и табличных цифр в шрифтах проверил по метаданным Google Fonts и самим файлам шрифтов через fontTools.

**Ограничения.**
- Страницы Gartner закрыты антиботом. Цифры Gartner взяты из выдачи поиска, где цитируется сама страница, и из пересказа пресс-релиза в Mi3. В тексте это помечено.
- Сайт clutch.co из песочницы не открылся. Данные опроса Clutch взяты из перепечатки пресс-релиза.
- Статья HBR о скорости ответа на заявку известна только по вторичным источникам. Помечено.
- Т-Банк, Точка, Модульбанк и Альфа из песочницы недоступны, поэтому в референсы не вошли.
- Если исследование старое или узкое (B2C, юристы, SaaS), это сказано рядом с цифрой.

Скриншоты лежат во временной папке `/tmp/claude-0/-home-user-axiom-site/f76178c0-66f5-5b09-bd2b-6df8c2dc6a50/scratchpad/refs/` (`<сайт>-hero.png` — первый экран, `<сайт>-full.png` — страница до 7200 px). Если они понадобятся надолго, их нужно перенести.

---

## Коротко

1. Сайт консалтинга — место, где **проверяют**, а не где впервые узнают. 80,8% покупателей профуслуг смотрят сайт фирмы перед наймом, и это самый частый способ проверки ([Hinge, 2014](https://kevin.lexblog.com/wp-content/uploads/sites/111/2014/02/HIN-BeyondReferrals-Report-021314-1.pdf)). Решение «остаться или уйти» человек принимает за первые 10 секунд ([NN/g](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/)).
2. Покупатель выбирает по экспертизе в его отрасли, прошлым результатам и сильной команде ([Hinge, 2018](https://hingemarketing.com/wp-content/uploads/2018/09/Research-2018-IBB-SecondEdition-ExSumm.pdf); [Hinge, 2022](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf)). Больше всего он боится, что ему пообещают больше, чем сделают.
3. Цена — информация номер один на любом сайте, включая B2B ([NN/g](https://www.nngroup.com/articles/show-price/)). Прямой конкурент по аудиту моделей Gridlines публикует типовые гонорары ([Gridlines](https://www.gridlines.com/model-audit/)). Axiom стоит показать вилки или «от», объяснить, от чего зависит цена, и дать типовые сценарии.
4. Доверие в финконсалтинге держится на пяти вещах: образец того, что клиент получит (страница отчёта), методика и стандарт, реальные люди с именами, конкретные кейсы, правила конфиденциальности.
5. Форма: 3–4 поля, рядом объяснение, зачем нужно каждое поле и что будет после отправки. Кнопка называет действие: «Обсудить проект», а не «Начать» ([NN/g](https://www.nngroup.com/articles/get-started/)).
6. Рекомендованное направление дизайна — **A «Рабочий документ»**: тёплый бумажный фон, глубокий зелёный акцент, засечный шрифт в заголовках, страницы отчётов как главный визуальный объект. Подробности в части 3.

---

# Часть 1. Доказательная база

## 1.1. Как B2B-покупатели профессиональных услуг ищут и проверяют подрядчика

### Ключевые факты

| Факт | Цифра | Источник |
|---|---|---|
| Самый частый способ «проверить» фирму перед наймом — её сайт | 80,8% покупателей. В среднем используют 3,2 способа. Выборка: 1028 покупателей профуслуг, 554 из них покупали бухгалтерские и финансовые услуги | [Hinge, Beyond Referrals, 2014](https://kevin.lexblog.com/wp-content/uploads/sites/111/2014/02/HIN-BeyondReferrals-Report-021314-1.pdf) |
| Откуда узнают о фирме | Рекомендации: 59,5% (в 2013 г. было больше 70%). Онлайн-поиск: 18,2% (в 2013 г. — 11%). Выборка: 1475 покупателей | [Hinge, Inside the Buyer's Brain, 2018](https://hingemarketing.com/wp-content/uploads/2018/09/Research-2018-IBB-SecondEdition-ExSumm.pdf) |
| По чему оценивают фирму | Релевантный опыт / прошлые результаты: 35,1%. Экспертиза команды: 33,4%. Знание отрасли клиента: 20,6%. Способность дать результат: 19,6%. Репутация: 16,8% | [Hinge, 2018](https://hingemarketing.com/wp-content/uploads/2018/09/Research-2018-IBB-SecondEdition-ExSumm.pdf) |
| Топ-5 критериев оценки в 2022 г. | Знание отрасли и предметная экспертиза; релевантный опыт; сильная команда; существующие отношения (+79% к 2020 г.); сервис и скорость ответа. Выборка: 1914 покупателей | [Hinge, IBB 2022, вебинар](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf) |
| Главные опасения при выборе | 1) пообещают и не сделают — около 28% в 2022 г. против 20% в 2020 г.; 2) неопытный персонал; 3) плохой сервис и медленные ответы; 4) слабые результаты работы; 5) «фирма не понимает мою ситуацию». Проценты сопоставлены с подписями графика по рангам и изменению к 2020 г. | [Hinge, IBB 2022](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf) |
| Что важнее всего на сайте B2B-подрядчика | Прозрачная информация о стоимости: 25%. Кейсы и отзывы: 23%. Немедленный доступ к информации: 17%. Выборка: 451 человек, 2020 г. | [Clutch, 2020](https://martechseries.com/technology/b2b-buyers-concerned-transparent-costs-b2b-companies-websites-highlighting-importance-trust-b2b-sales-funnel/) |
| Цена в рейтинге 28 типов информации на B2B-сайте | Первое место «с большим отрывом»: на 29% выше второго места. Здесь же: успешность задач на B2B-сайтах 58% против 66% на обычных | [NN/g, B2B Usability, 2006](https://www.nngroup.com/articles/b2b-usability/) |
| Встречи с поставщиками | Только 17% времени покупки; при трёх кандидатах это около 5% на каждого. Выборка: 750 покупателей. Цифра взята из выдачи поиска, страница закрыта антиботом | [Gartner, B2B Buying Journey](https://www.gartner.com/en/sales/insights/b2b-buying-journey) |
| Предпочитают покупать без продавца | 61% покупателей. 73% избегают поставщиков, которые присылают нерелевантные предложения. 69% видели расхождения между сайтом и словами продавца. Выборка: 632 покупателя, август–сентябрь 2024 г. В 2026 г. Gartner сообщает уже о 67% | [Gartner, пресс-релиз 25.06.2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience), пересказ: [Mi3](https://www.mi-3.com.au/04-07-2025/gartner-survey-reveals-b2b-buyers-preference-rep-free-experience); [Gartner, 09.03.2026](https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience) |
| Сколько людей решает | В среднем 13 человек внутри компании; в 89% покупок участвуют два отдела и больше. 86% покупок «застревают». 81% недовольны выбранным поставщиком | [Forrester, State of Business Buying 2024](https://www.forrester.com/press-newsroom/forrester-the-state-of-business-buying-2024/) |
| Внешние советчики | 13 человек внутри и ещё 9 внешних | [Forrester, 2026](https://www.forrester.com/press-newsroom/forrester-2026-the-state-of-business-buying/) |
| Сайт — одно из первых действий | «Большинство пользователей сказали, что одно из первых действий, когда они думают о работе с компанией, — посмотреть её сайт» | [NN/g, B2B Usability](https://www.nngroup.com/articles/b2b-usability/) |

### В каком порядке покупатель задаёт вопросы

Это синтез приведённых данных. Для Axiom порядок важен: к нам приходят в основном «тёплые», по рекомендации или с конкретной болью. Сайт должен подтвердить выбор и снять риски, а не продавать с нуля.

| Шаг | Время | Вопрос посетителя | На что опираемся | Что показывает Axiom |
|---|---|---|---|---|
| 1 | 0–10 с | Туда ли я попал? Что они делают, для кого, где? | NN/g: 10 секунд и одна фраза о том, что делает компания ([10 с](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/), [главная](https://www.nngroup.com/articles/top-ten-guidelines-for-homepage-usability/), [«О нас»](https://www.nngroup.com/articles/about-us-information-on-websites/)) | Одна фраза: финмодели, аудит моделей и управленческий учёт для девелоперов, генподрядчиков и инвесторов в ЮВА, ОАЭ и СНГ |
| 2 | 10–60 с | Понимают ли мою ситуацию? | Hinge: знание отрасли — критерий №1 в 2022 г.; «не понимает мою ситуацию» — в топ-5 опасений | 4–6 проблем словами клиента («деньги кончатся на третьем этаже?») → услуга → результат |
| 3 | 1–2 мин | Умеют ли? Кто это сделает? | Hinge: прошлые результаты и сильная команда — №1–3 | Кейсы с цифрами, команда с фото и ролями, образец отчёта |
| 4 | 1–3 мин | Сколько стоит и как это будет? | NN/g: цена — информация №1; Clutch: 25% | Вилки или «от», что влияет на цену, сроки, этапы, состав результата |
| 5 | — | Можно ли им верить? | Clutch: кейсы и отзывы — 23%; [Stanford](https://credibility.stanford.edu/guidelines/index.html) | Отзывы с именами и должностями, реквизиты, офисы, NDA, методика |
| 6 | — | Как начать без риска и как объяснить партнёрам? | Gartner: самообслуживание; Forrester: 13 человек в решении | Короткая форма или мессенджер; материал, который можно переслать партнёру |

## 1.2. Как люди читают лендинг

| Наблюдение | Данные | Источник |
|---|---|---|
| Первые 10 секунд решают, останется ли человек | Вероятность ухода максимальна в первые секунды. Через 30 секунд кривая выравнивается. Вывод NN/g: «чтобы получить несколько минут внимания, ценность нужно донести за 10 секунд» | [NN/g, Nielsen, 2011](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/) |
| Первый экран и первые три экрана | 57% времени просмотра — выше сгиба, 74% — первые два экрана, 81% — первые три. Второй экран получает около 17% | [NN/g, Scrolling and Attention, 2018](https://www.nngroup.com/articles/scrolling-and-attention/) |
| Левая половина | 80% времени взгляд проводит в левой половине страницы | [NN/g, Horizontal Attention Leans Left, 2017](https://www.nngroup.com/articles/horizontal-attention-leans-left/) |
| F-паттерн | Возникает на неформатированном тексте, когда человек спешит. Лечение: главное — в первые два абзаца; первые два слова заголовка несут смысл; списки, жирный, ссылки с говорящим текстом | [NN/g, F-Shaped Pattern, 2006/2017](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/) |
| Сжатый, сканируемый и объективный текст | Юзабилити выше: на 58% у сжатого, на 47% у сканируемого, на 27% у объективного (без рекламного тона), на 124% у всех трёх вместе | [NN/g, Morkes & Nielsen, 1997](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/) |
| Цифры, а не слова | «23», а не «двадцать три»: цифры ловят взгляд при сканировании | [NN/g, 2007](https://www.nngroup.com/articles/web-writing-show-numbers-as-numerals/) |
| Первое впечатление | Эстетическое суждение формируется за 17–50 мс. Нравится то, что выглядит просто (низкая визуальная сложность) и привычно для категории (высокая прототипичность) | [Google Research, Tuch et al., 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/) |
| Длина строки | Оптимально 50–75 знаков | [Baymard, 2022](https://baymard.com/blog/line-length-readability) |

## 1.3. Доверие: общие механизмы

| Механизм | Что говорит исследование | Источник |
|---|---|---|
| Внешний вид | В 46,1% комментариев о доверии к сайту упоминается «внешний вид» — это самый частый фактор. Опрошено 2684 человека | [Fogg et al., 2002](https://advocacy.consumerreports.org/research/how-do-people-evaluate-a-web-sites-credibility) |
| 10 правил доверия Stanford | Дать проверить информацию; показать, что за сайтом стоит реальная организация (адрес); показать экспертизу и регалии; показать честных людей; сделать контакты простыми; профессиональный дизайн; польза и удобство; свежесть; сдержанность в рекламе; никаких ошибок. Основа — исследования с участием более 4500 человек | [Stanford Web Credibility Guidelines, Fogg, 2002](https://credibility.stanford.edu/guidelines/index.html) |
| Четыре фактора NN/g | Качество дизайна; открытость с самого начала (цены, что входит, гарантии); полный, точный и свежий контент; связь с остальным интернетом. Сайты, где нет базовой информации, «почти сразу исключались». Участница отказалась от сервиса через 35 секунд, потому что не нашла ставку | [NN/g, Trustworthiness in Web Design, 2016](https://www.nngroup.com/articles/trustworthy-design/) |
| Закрытый контент | «Просить информацию до того, как дал ценность, — нарушение доверия» | [NN/g, 2016](https://www.nngroup.com/articles/trustworthy-design/); [NN/g, B2B, 2006](https://www.nngroup.com/articles/b2b-usability/): «выносите больше информации за пределы барьера» |
| Простой язык | Понятный текст воспринимается как честный, а запутанный — как попытка скрыть. «Никто никогда не жаловался, что страницу слишком легко читать» | [NN/g, B2B trust, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/) |
| Отзывы | Людям важно, кто автор: должность и компания. Лучше всего работают отзывы в духе «сомневался — убедился» | [NN/g, B2B trust, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/) |
| Реальные люди | Фото реальных сотрудников рассматривают, стоковые фото игнорируют. На странице команды FreshBooks пользователь смотрел на портреты на 10% дольше, чем читал биографии, хотя биографии занимали на 316% больше места | [NN/g, Photos as Web Content, 2010, обновлена](https://www.nngroup.com/articles/photos-as-web-content/) |
| «О нас» | Объяснить, что компания делает, одной фразой или абзацем. Реалистичные фото, простой язык. Пользователи сверяют сайт с внешними отзывами | [NN/g, About Us, 2019](https://www.nngroup.com/articles/about-us-information-on-websites/) |
| Контакты | Адрес, телефон и почту по-прежнему ждут. Не заменять их одной формой или чатом | [NN/g, Contact Us, 2019](https://www.nngroup.com/articles/contact-us-pages/) |
| Сайт = продавец | 69% покупателей видели расхождения между сайтом и словами продавца | [Gartner, 2025](https://www.mi-3.com.au/04-07-2025/gartner-survey-reveals-b2b-buyers-preference-rep-free-experience) |

## 1.4. Формы и микрокопирайтинг

| Тема | Данные и рекомендации | Источник |
|---|---|---|
| Длина формы | «Каждое убранное поле повышает конверсию». NN/g сократила собственную форму с 6 полей до 2. Поля одной колонкой, подписи над полями, без плейсхолдеров вместо подписей, необязательных полей одно-два, и они помечены | [NN/g, Forms Top 10, 2016](https://www.nngroup.com/articles/web-form-design/) |
| Цена ошибок в форме | Если форма соответствует гайдлайнам, её с первой попытки без ошибок отправляют 78% людей, если нет — 42% (Seckler et al., CHI) | [NN/g, 2016](https://www.nngroup.com/articles/web-form-design/) |
| 5 полей против 7 и 9 | Конверсия 13,4% против 12% и 10% (MarketingExperiments, лид-форма Marketo) | [Adobe Blog, 2018](https://blog.adobe.com/en/publish/2018/07/09/less-dos-donts-designing-web-forms) |
| Контрпример | В другом тесте рост с 11 до 15 полей дал +109% конверсии, а сокращение до 10 — только +87%. Вывод: решают не только число полей, но и уместность вопросов | [Adobe Blog, 2018](https://blog.adobe.com/en/publish/2018/07/09/less-dos-donts-designing-web-forms) |
| Объяснять, зачем поле | Когда человеку объясняют причину просьбы, он охотнее соглашается (Langer & Chanowitz, 1978). Пример: «Чтобы предложить подходящее решение, нам нужно задать пару вопросов» | [NN/g, B2B trust, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/) |
| Телефон | Обязательный телефон без объяснения вызывает подозрение. Тот же человек оставил номер на другом сайте, где объяснили зачем. B2C-данные, но механизм тот же | [Baymard, 2012](https://baymard.com/blog/checkout-experience-seemingly-unnecessary-information) |
| Несколько каналов | Одни хотят позвонить, другие — форму, почту или мессенджер. Минимум — почта и телефон | [NN/g, B2B trust, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/) |
| Скорость ответа | Компании, которые связались с лидом в течение часа, почти в 7 раз чаще квалифицировали его, чем те, кто ждал на час дольше. Знаем по вторичным источникам, данные 2011 г. | HBR, Oldroyd, McElheran, Elkington, 2011 ([карточка публикации](https://scholarsarchive.byu.edu/facpub/9711)) |
| «Начать» | Расплывчатая кнопка «Get Started» собирает клики, но обманывает ожидания. Человек ждёт информацию, а попадает в воронку. «Ссылка — это обещание» | [NN/g, 2017](https://www.nngroup.com/articles/get-started/) |
| «Узнать больше» | Слабый информационный запах и плохая доступность. Ссылка должна говорить, что будет на следующей странице | [NN/g, 2015](https://www.nngroup.com/articles/learn-more-links/) |

## 1.5. Показывать ли цены консалтинга

### Аргументы «за»

- **Цена — информация номер один.** Пользователи уходят к конкурентам, если не видят цен. Список кандидатов собирают из первых сайтов, где есть внятная информация, в том числе о цене. Компании, которые прячут цену, выглядят уклончивыми ([NN/g, 2013](https://www.nngroup.com/articles/show-price/)).
- **Первая увиденная цена становится якорем.** Скрытая цена добавляет лишний шаг, создаёт ощущение «раз спрашивают — значит, дорого» и делает фирму подозрительной ([NN/g, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)).
- **B2B-бюджеты утверждают заранее и редко пересматривают**, поэтому для планирования достаточно ориентира ([NN/g, 2013](https://www.nngroup.com/articles/show-price/)).
- **Clutch:** прозрачная стоимость — самый важный элемент сайта для 25% B2B-покупателей ([2020](https://martechseries.com/technology/b2b-buyers-concerned-transparent-costs-b2b-companies-websites-highlighting-importance-trust-b2b-sales-funnel/)).
- **Фильтр нецелевых заявок.** Если цен нет, звонят все, включая тех, у кого нет бюджета, и время продаж уходит на неквалифицированные лиды ([Forrester](https://www.forrester.com/blogs/prices-public-on-website)). Майкл Китс для финансовых советников: опубликованные гонорар и минимальный чек позволяют сайту отсеять неподходящих и защищают от торга «с самим собой» ([Kitces](https://www.kitces.com/blog/advisory-firm-fees-minimums-website-fiduciary-transparency-price-haggling/)).
- **Ожидания по цене.** Юрфирмы, которые публикуют цены, называют главной пользой для клиента управление ожиданиями по стоимости — 39% ([SRA, 2017](https://guidance.sra.org.uk/globalassets/documents/sra/research/price-transparency-legal-services-market.pdf)).
- **Прецедент в нише Axiom.** Gridlines на странице аудита моделей публикует типовой гонорар. Comfort review стоит $16–20k, полный аудит — $32–40k для модели примерно на 3000 уникальных формул. Там же перечислено, от чего зависит цена (размер модели, объём проверки, уровень страхового покрытия, документы), срок первой обратной связи (3–4 рабочих дня) и срок до подписания (около 4 и 6 недель) ([Gridlines](https://www.gridlines.com/model-audit/)).

### Аргументы «против»

- **Работа сложная и разная.** 74% юрфирм, которые не публикуют цены, называют главной трудностью то, что дела «сложные и разные». 53% считают цену под каждого клиента, 17% не хотят показывать цены конкурентам ([SRA, 2017](https://guidance.sra.org.uk/globalassets/documents/sra/research/price-transparency-legal-services-market.pdf); это юристы, а не консалтинг).
- **Разговор о цене начнётся раньше разговора о ценности.** Это касается новых и сложных услуг. Молодому бренду нужно время, чтобы доказать ценность ([Forrester](https://www.forrester.com/blogs/prices-public-on-website)).
- **Риск занизить гонорар.** Опубликованная цена может держать гонорары ниже, чем удалось бы договориться. Это мнение практиков, исследований эффекта на выручку консалтинга я не нашёл.

### Компромисс, который рекомендуют сами источники

- Показывать «от» или вилку и типовые сценарии, а не сложный калькулятор: калькуляторы «сложные, долгие и с ошибками» ([NN/g, 2013](https://www.nngroup.com/articles/show-price/)).
- Можно публиковать цены не на всё. Типовые пакеты покрывают около 80% клиентов, нестандартное — по запросу ([Forrester](https://www.forrester.com/blogs/prices-public-on-website)).
- Как это делают финансовые сервисы:
  - Kruze: $650–850 и $850–1500 в месяц, премиум — «индивидуально» ([Kruze](https://kruzeconsulting.com/pricing/)).
  - Graphite: «от $500 в месяц» и список «цена зависит от: …», плюс три шага, как считают цену ([Graphite](https://graphitefinancial.com/pricing/)).
  - Pilot: тарифы от $99 в месяц ([Pilot](https://pilot.com/pricing)).
- Цену стоит давать в контексте: что за неё получит клиент и с чем сравнить ([Kitces](https://www.kitces.com/blog/why-your-financial-planning-pricing-should-be-clearly-stated-on-your-website/)).

**Вывод для Axiom.** Показывать уровень цен на каждую услугу: «от …» или вилку, 3–4 фактора цены, срок и что входит в результат. Для нестандартных проектов — «оценим за 1–2 дня после звонка». Это закрывает вопрос №1, отсеивает нецелевые заявки и ничего не обещает лишнего. Конкретные суммы утверждает Евгений.

## 1.6. Какие блоки повышают доверие именно в финансовом консалтинге

| Блок | Почему работает | Опора | Пример у референсов |
|---|---|---|---|
| **Образец результата**: страница отчёта аудита, лист Cash Flow, дашборд управленческого учёта (обезличенные) | Показывает, что именно получит клиент; снимает страх «пообещают и не сделают». Информативные изображения рассматривают, декоративные игнорируют | Hinge 2022 (опасение №1); [NN/g photos](https://www.nngroup.com/articles/photos-as-web-content/); [NN/g B2B trust](https://www.nngroup.com/articles/b2b-trust-from-b2c/) («показать продукт в работе») | Fathom: листы «KPIs» и «Cash Flow Analysis» с водопадом; Pilot: таблица движения денег в первом экране |
| **Методика и стандарт** (по каким правилам строим и проверяем модели) | Даёт проверить; показывает экспертизу. Отраслевые ориентиры: [ICAEW Financial Modelling Code](https://www.icaew.com/technical/technology/excel-community/improve-your-financial-modelling-practice) и FAST Standard | [Stanford №1, №3](https://credibility.stanford.edu/guidelines/index.html) | F1F9 вынесла FAST в главное меню; Gridlines описывает, как совмещает два метода проверки |
| **Объём, сроки, этапы** | Прямо отвечает на опасение «пообещают больше»: видно, что входит в работу, а что нет | Hinge 2022; [NN/g «How it works»](https://www.nngroup.com/articles/b2b-trust-from-b2c/) | Gridlines: таблица «comfort review / full audit» — что проверяем, итерации, сроки, гонорар, итоговый документ |
| **Конфиденциальность**: NDA до передачи файлов, кто видит данные, где они хранятся, что публикуем в кейсах | Клиент отдаёт модель и цифры проекта — это коммерческая тайна. Правила, о которых говорят заранее, NN/g относит к доверию через открытость. Отдельных исследований про NDA на сайтах консалтинга я не нашёл, это вывод по аналогии | [NN/g, Upfront Disclosure](https://www.nngroup.com/articles/trustworthy-design/) | — |
| **Обезличенные кейсы** | Обезличенный не значит расплывчатый: тип объекта, регион, масштаб, цифры «до и после», ограничения. Помечать как обезличенный. Эмпирики об эффекте нет, это практика отрасли | [Umbrex, практическое руководство](https://umbrex.com/resources/the-generative-engine-optimization-playbook-a-guide-for-professional-services/demonstrate-experience-without-compromising-confidentiality/) | Gridlines: «Recent projects» со страной, датой и типом объекта |
| **Независимость и ответственность** | Аудитор, который не строил модель, и страховка профессиональной ответственности | — | Gridlines: независимый аудит, покрытие £5 млн с расширением до £12 млн |
| **Числа о фирме** | Сканируются первыми; объём сделок и лет опыта — это прошлые результаты | [NN/g, numerals](https://www.nngroup.com/articles/web-writing-show-numbers-as-numerals/); Hinge 2018 | Gridlines: «$130bn», «60+», «2nd»; F1F9: «530+ моделей»; Puzzle: карточки с цифрами и сноской «условия гарантии» |
| **Реальная организация** | Юрлицо, адреса офисов, реквизиты | [Stanford №2, №5](https://credibility.stanford.edu/guidelines/index.html); [NN/g Contact](https://www.nngroup.com/articles/contact-us-pages/) | Gridlines: офисы с городами и регионами |

## 1.7. Правила для лендинга Axiom

1. **Первый экран отвечает на три вопроса:** что мы делаем, для кого (девелоперы, генподрядчики, инвесторы; ЮВА, ОАЭ, СНГ) и что делать дальше (одна главная кнопка). Без слогана вместо смысла. — [NN/g, 10 секунд](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/); [NN/g, главная](https://www.nngroup.com/articles/top-ten-guidelines-for-homepage-usability/); [NN/g, «О нас»](https://www.nngroup.com/articles/about-us-information-on-websites/)

2. **Заголовок называет услугу и результат, а не ценности.** Антипримеры: «Unparalleled Strategic Advice» у Centerview, «Client-Focused, Values-Driven» у Evercore. Рекламный тон снижает юзабилити, объективный повышает на 27%. — [NN/g, 1997](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/); [Stanford №9](https://credibility.stanford.edu/guidelines/index.html)

3. **Самое важное — в первых двух экранах и слева.** Выравнивание по левому краю, проблемы клиента начинаются уже во втором экране. — 57% и 74% внимания: [NN/g, Scrolling](https://www.nngroup.com/articles/scrolling-and-attention/); 80% на левой половине: [NN/g, Left](https://www.nngroup.com/articles/horizontal-attention-leans-left/)

4. **Проблемы — словами клиента, по одной строке, смысл в первых двух словах.** Например: «Деньги кончаются посреди стройки», «Инвестор не верит модели». — [NN/g, F-pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/); Hinge 2022: «фирма не понимает мою ситуацию» в топ-5 опасений ([PDF](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf))

5. **Коротко, списками, цифрами.** Без абзацев длиннее трёх строк; числа писать цифрами («12 лет», «за 5 рабочих дней»). — [NN/g, +124%](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/); [NN/g, numerals](https://www.nngroup.com/articles/web-writing-show-numbers-as-numerals/)

6. **Главный визуальный объект — артефакт работы:** обезличенная страница отчёта, лист Cash Flow, таблица сценариев. Никаких стоковых людей, абстрактных 3D и пейзажей. — [NN/g, Photos](https://www.nngroup.com/articles/photos-as-web-content/); [NN/g, B2B trust](https://www.nngroup.com/articles/b2b-trust-from-b2c/)

7. **Команда — реальные фото, имя, роль, одна строка опыта.** Не сток, как в обрамлении первого экрана у Graphite. — [NN/g, Photos](https://www.nngroup.com/articles/photos-as-web-content/); [Stanford №4](https://credibility.stanford.edu/guidelines/index.html); Hinge 2022: «сильная команда» в топ-3

8. **Кейсы — главный аргумент, и в каждом есть цифры:** объект, страна, масштаб, что было, что сделали, что изменилось в деньгах или сроках. — Прошлые результаты — критерий №1 (35%): [Hinge, 2018](https://hingemarketing.com/wp-content/uploads/2018/09/Research-2018-IBB-SecondEdition-ExSumm.pdf); кейсы и отзывы — 23%: [Clutch](https://martechseries.com/technology/b2b-buyers-concerned-transparent-costs-b2b-companies-websites-highlighting-importance-trust-b2b-sales-funnel/)

9. **Обезличенный кейс помечаем и делаем конкретным:** «вилла-комплекс на 24 юнита, Бали» вместо «крупный проект в Азии». Пишем, чего кейс не доказывает. — [Umbrex](https://umbrex.com/resources/the-generative-engine-optimization-playbook-a-guide-for-professional-services/demonstrate-experience-without-compromising-confidentiality/); [NN/g, «полный, точный, свежий»](https://www.nngroup.com/articles/trustworthy-design/)

10. **Отзывы — с именем, должностью и компанией** (или хотя бы ролью и страной). Лучшие начинаются с сомнения. — [NN/g, B2B trust](https://www.nngroup.com/articles/b2b-trust-from-b2c/)

11. **Уровень цен — на сайте:** «от …» или вилка, 3–4 фактора цены и срок. Для нестандартного — «оценим после звонка». — [NN/g, Show price](https://www.nngroup.com/articles/show-price/); [NN/g, 2006](https://www.nngroup.com/articles/b2b-usability/); [Clutch](https://martechseries.com/technology/b2b-buyers-concerned-transparent-costs-b2b-companies-websites-highlighting-importance-trust-b2b-sales-funnel/); прецедент: [Gridlines](https://www.gridlines.com/model-audit/)

12. **Для каждой услуги указываем, что входит в результат и сколько это занимает.** Какой документ получит клиент, в какой срок, сколько итераций. — Опасение №1 «пообещают и не сделают»: [Hinge 2022](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf); образец: таблица на [Gridlines](https://www.gridlines.com/model-audit/)

13. **Не прятать полезное за форму.** Пример отчёта, методика и прайс-логика доступны без контактов. — [NN/g, Trust](https://www.nngroup.com/articles/trustworthy-design/); [NN/g, 2006](https://www.nngroup.com/articles/b2b-usability/)

14. **Форма — 3–4 поля одной колонкой:** имя; Telegram, WhatsApp или почта; роль или тип проекта (выбор из 3–5 вариантов); комментарий необязательный. Подписи над полями, необязательные помечены. — [NN/g, Forms](https://www.nngroup.com/articles/web-form-design/); [MarketingExperiments через Adobe](https://blog.adobe.com/en/publish/2018/07/09/less-dos-donts-designing-web-forms)

15. **Рядом с формой — зачем каждое поле и что будет дальше:** кто ответит, в какой срок, в каком канале; «подпишем NDA до того, как вы пришлёте файлы». Обещанный срок ответа выдерживать. — [NN/g, B2B trust](https://www.nngroup.com/articles/b2b-trust-from-b2c/) (Langer, 1978); [Baymard](https://baymard.com/blog/checkout-experience-seemingly-unnecessary-information); HBR, 2011 (вторичные источники)

16. **Кнопка говорит, что произойдёт:** «Обсудить проект», «Отправить модель на аудит», «Узнать стоимость». Не «Начать», не «Подробнее», не «Отправить». — [NN/g, Get Started](https://www.nngroup.com/articles/get-started/); [NN/g, Learn More](https://www.nngroup.com/articles/learn-more-links/)

17. **Одно главное действие и одна тихая альтернатива.** «Обсудить проект» плюс «или задать вопрос в Telegram», как у Gridlines («Tell us about your project / Or ask a question») и Yandex Cloud («Попробовать бесплатно / Связаться с экспертом»). — Gartner: информацию покупатели берут сами, вопрос «подходит ли нам» решают с продавцом ([Mi3](https://www.mi-3.com.au/04-07-2025/gartner-survey-reveals-b2b-buyers-preference-rep-free-experience))

18. **Методика — отдельным коротким блоком:** по каким правилам строим модели, как проверяем (чек-лист, лог замечаний), на какие стандарты опираемся (ICAEW Code, FAST). — [Stanford №1, №3](https://credibility.stanford.edu/guidelines/index.html); [ICAEW](https://www.icaew.com/technical/technology/excel-community/improve-your-financial-modelling-practice)

19. **Конфиденциальность — 3–4 строки на главной:** NDA, доступ к файлам, что мы никогда не публикуем. — [NN/g, Upfront Disclosure](https://www.nngroup.com/articles/trustworthy-design/) (вывод по аналогии, см. 1.6)

20. **Помогаем «продать решение внутри».** Короткий PDF или страница, которую можно переслать партнёру или инвестору: услуги, пример результата, логика цены. — [Forrester: 13 человек в решении](https://www.forrester.com/press-newsroom/forrester-the-state-of-business-buying-2024/); [NN/g, «продажа внутри организации»](https://www.nngroup.com/articles/b2b-trust-from-b2c/)

21. **Сайт и разговор совпадают:** цены, сроки и состав услуг на сайте — те же, что называет Евгений на звонке. — 69% видели расхождения: [Gartner, 2025](https://www.mi-3.com.au/04-07-2025/gartner-survey-reveals-b2b-buyers-preference-rep-free-experience)

22. **Визуально — просто и привычно:** один акцентный цвет, много воздуха, никаких декоративных фонов, каруселей и видео в первом экране. — [Google Research, Tuch, 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/); [Fogg, 46,1%](https://advocacy.consumerreports.org/research/how-do-people-evaluate-a-web-sites-credibility); [NN/g, белое пространство](https://www.nngroup.com/articles/trustworthy-design/)

23. **Реальная организация и контакты на виду:** юрлица и страны, города офисов, почта, Telegram, телефон. Форма не заменяет контакты. — [Stanford №2, №5](https://credibility.stanford.edu/guidelines/index.html); [NN/g, Contact Us](https://www.nngroup.com/articles/contact-us-pages/)

24. **Ноль ошибок и видимая свежесть:** без опечаток и битых ссылок; у цифр «на дату» указана дата. — [Stanford №8, №10](https://credibility.stanford.edu/guidelines/index.html); [NN/g, опечатки](https://www.nngroup.com/articles/trustworthy-design/)

25. **Читаемость:** строка 50–75 знаков, основной текст от 17 px, контраст текста не ниже 4,5:1. — [Baymard](https://baymard.com/blog/line-length-readability); WCAG 2.1, критерий 1.4.3

---

# Часть 2. Дизайн-референсы

Сняты 25 сайтов. В основной список вошли 12: те, что ясны по смыслу и выглядят как настоящий продукт. Цифры ниже — вычисленные стили на ширине 1440 px: кегль и интерлиньяж в px, начертание (w), трекинг (ls), цвета в hex. Цвета Ramp заданы в CSS как `lab()` и пересчитаны в hex приблизительно (≈).

## 2.1. Сводная таблица

| # | Сайт | Почему здесь | Что взять в первую очередь |
|---|---|---|---|
| 1 | [gridlines.com](https://www.gridlines.com) | Ближайший по бизнесу: финмоделирование и аудит моделей для девелоперов, инвесторов и кредиторов | Формула первого экрана, лента услуг, цифры, таблица с типовыми гонорарами |
| 2 | [stripe.com](https://stripe.com) | Эталон ясной иерархии | Двухтоновый заголовок, бенто-карточки с реальными интерфейсами |
| 3 | [ramp.com](https://ramp.com) | Финансы, левое выравнивание, мало цвета | Левый первый экран, моно-подписи, артефакт-инвойс |
| 4 | [pilot.com](https://pilot.com) | Бухгалтерия и CFO-услуги, сервис плюс продукт | Артефакт в первом экране, «сценарии» словами клиента, карточки людей |
| 5 | [puzzle.io](https://puzzle.io) | Услуги плюс софт, цена в первом экране | Цена «от», карточки-цифры со сноской, «Сколько помощи вам нужно?» |
| 6 | [fathomhq.com](https://www.fathomhq.com) | Финотчёты на лендинге | Листы отчётов стопкой: KPI и водопад денежного потока |
| 7 | [digits.com](https://digits.com) | Финансы, сильная типографика | Контраст начертаний в одном заголовке, таблицы реестров |
| 8 | [linear.app](https://linear.app) | Иерархия и плотность | Четыре уровня серого текста, плотный трекинг крупных заголовков |
| 9 | [vercel.com](https://vercel.com) | Сдержанность; шрифт Geist теперь есть в Google Fonts с кириллицей | Пара кнопок «главная / вторичная», минимум цвета |
| 10 | [yandex.cloud/ru](https://yandex.cloud/ru) | Русскоязычный продукт, жирная кириллица | Тяжёлый кириллический заголовок, две понятные кнопки |
| 11 | [bureau.ru/projects](https://bureau.ru/projects/) | Русская типографика, иерархия размером | Огромный H1, подписи на полях, один акцент, кнопка «Стать клиентом» |
| 12 | [maximilyahov.ru](https://maximilyahov.ru) | Информационный стиль в чистом виде | Текст вместо декора, простой язык |

Финансовые данные красиво показаны прямо на лендинге у **Fathom**, **Pilot** и **Stripe**; запасной вариант — Digits (см. 2.3).

## 2.2. Карточки референсов

### 1. Gridlines — gridlines.com

- **Первый экран.**
  - H1: «Project finance advisory and financial modelling for energy and infrastructure.» — что делаем и для кого.
  - Подзаголовок: «The numbers behind your deal have to hold. We make sure they do.»
  - Главная кнопка «Tell us about your project», под ней ссылка «Or ask a question».
  - Сразу под фото — лента из четырёх услуг.
- **Доказательства.**
  - Логотипы клиентов и цифры: «$130bn in supported global transactions», «60+ lender, ECA and DFI relationships», «2nd Infralogic League Table H1 2026».
  - Видео с партнёром.
  - Отзыв с именем и должностью: Ismail Chakour, Head of Structured Finance, Masdar.
  - «Recent projects» со страной и датой, офисы с регионами.
- **Страница аудита моделей.** Таблица «Comfort review / Full model audit»: объём, нужные документы, итерации, покрытие ответственности, первая обратная связь (3–4 рабочих дня), типовой гонорар ($16–20k / $32–40k), итоговый документ (comfort letter / opinion letter). Это лучший найденный образец блока «что входит и сколько стоит» для Axiom.
- **Типографика.** Montserrat. H1 38/48 w700, H2 34/42 w700, H3 25/32. Основной текст 18/27.
- **Палитра.** `#127486` — бирюза заголовков и секций, `#66c9d1` — светлая бирюза кнопок и ленты, `#262626` — текст, `#ffffff` — фон. Кнопки со скруглением 3 px.
- **Плотность.** Средняя, страница около 7200 px.
- **Что не брать.** Стоковое фото ветряков и солнечных панелей. Montserrat Bold везде выглядит шаблонно (WordPress).
- Скриншоты: `refs/gridlines-hero.png`, `refs/gridlines-audit-full.png`.

### 2. Stripe — stripe.com

- **Первый экран.** Одно длинное предложение-заголовок: тёмная часть — утверждение («Financial infrastructure to grow your revenue.»), серо-синее продолжение объясняет. Слева две кнопки. Над заголовком — живой счётчик «Global GDP running on Stripe: 1,7562…%».
- **Как показывают продукт.** Бенто-сетка. В каждой карточке заголовок в одну-две строки и настоящий интерфейс с цифрами: чек, оформление заказа, таблица подключённых аккаунтов.
- **Типографика.** Söhne (sohne-var) w300 даже в крупных размерах. H1 48/55,2, ls −0,96 px (−2%). H2 32/35,2. H3 26/29. Мелкий текст 14/19,6.
- **Палитра.** `#061b31` — заголовки, `#50617a` — вторичный текст, `#64748d` — подписи, `#533afd` — кнопки (скругление 4 px), фоны `#ffffff`, `#f8fafd`, `#e5edf5`, тёмная полоса `#0d1738`.
- **Плотность.** Высокая, около 15 000 px. Тонкие вертикальные направляющие задают сетку.
- **Что взять Axiom.** Двухтоновый заголовок секции: суть тёмным, пояснение серым. Карточки услуг, в каждой фрагмент реального результата.
- **Что не брать.** Градиентную ленту и длину страницы.

### 3. Ramp — ramp.com

- **Первый экран.** Выровнен влево. Над H1 моно-подпись капсом с живым счётчиком. H1 «Time is money. Save both.». Подзаголовок одной строкой. Форма из одного поля «work email» и кнопки. Ниже — макет «инвойс → сверка с заказом → помечено на проверку» с табличными данными.
- **Типографика.** TWK Lausanne w400. H1 64/64, H2 40/42, H3 24/28, основной текст 16/24. Моноширинный шрифт для подписей и счётчиков.
- **Палитра.** Текст ≈`#0c0a08`, белый фон, тёплые серые подложки ≈`#f4f2f0`. Единственный акцент — кислотный лайм ≈`#e4f222` на кнопке «See a demo» и в форме. Вторичная кнопка почти чёрная ≈`#1a1919`. Скругление 6–8 px. На фоне еле заметная точечная сетка.
- **Что взять.** Левое выравнивание. Один акцент только для главного действия. Моно-метки над заголовками. Документ-артефакт с табличными цифрами.

### 4. Pilot — pilot.com

- **Первый экран.** Над заголовком рейтинг G2. H1 «Accounting and tax services for small businesses and startups». Под ним композиция из реального интерфейса: столбики Cash In / Cash Out, таблица изменений по месяцам с зелёными и красными процентами, чек-лист налоговой декларации, карточка Net income.
- **Блок «Growth scenarios we support».** Проблемы цитатами клиента: «We keep running out of cash. How do I know if we can afford three more hires?», «Investors want financial projections…». Это прямой шаблон для блока проблем Axiom.
- **Команда.** Карточки CFO и COO: имя, бывшая роль («Former investment banker…»), цитата.
- **Цены.** На странице цен — тарифы «от $99/мес» ([pilot.com/pricing](https://pilot.com/pricing)).
- **Типографика.** Euclid Circular B. H1 56/64,4 w600, H2 40/42 w600, лид 18/27. Space Mono для меток.
- **Палитра.** `#281350` — тёмно-фиолетовый фон и заголовки, `#5931dc` / `#5f2ee5` — фиолетовый, `#ffd967` — жёлтая кнопка-таблетка, светлые полосы `#e7f9ff`, `#fcf3d6`.
- **Что не брать.** Рукописный шрифт и обилие цветных полос.

### 5. Puzzle — puzzle.io

- **Первый экран.**
  - Моно-плашка «INTRODUCING PUZZLE 2.0…».
  - H1 вопросом: «Accounting platform or accounting services?».
  - Кнопки «Book a demo» (чёрная) и «See Puzzle in action», ссылка «Chat with an expert →».
  - Строка фактов под кнопками: «14-day free trial · … · 10,000+ companies trust Puzzle».
  - В видео-превью — цена: «Expert reviewed starting at $99».
- **Под первым экраном.** Четыре карточки-цифры: «10,000+», «85–90%», «50% faster month-end close — or your money back*» со ссылкой «Guarantee terms», «12,000+».
- **Блок «How much help do you want?».** Четыре ситуации цитатами («I mostly want to do it myself», «I want someone to check my work» и т. д.), к каждой — рекомендованный пакет. Это самосегментация без калькулятора.
- **Типографика.** General Sans в заголовках (H2 38,7/46,4 w500), Haskoy в тексте (18/25,2), JetBrains Mono в метках.
- **Палитра.** Фон `#f3f4f1` (тёплый светло-серый), карточки `#ffffff`, кнопки `#0a0b0b` (скругление 8 px), вторичная кнопка `#ceb4fa`.

### 6. Fathom — fathomhq.com

- **Как показаны данные.** В блоке «Management reporting» два листа отчёта лежат стопкой, как бумага, с лёгкой тенью:
  - «KPIs» — сгруппированный список показателей: Profitability, Activity, Efficiency, Liquidity, Cash Flow, Gearing, у каждой группы цветной маркер-буква;
  - «Cash Flow Analysis» — водопад: зелёные и красные бары, подписи статей слева, промежуточные итоги «Operating cash flow $295,612», «Free cash flow $327,288» на серых плашках.
  
  Справа — заголовок и три коротких тезиса («Fast / Flexible / Automated»). Это готовый паттерн для блока «Образец отчёта» у Axiom.
- **Первый экран.** Тёмный. Заголовок слева, справа коллаж из графиков, под кнопкой «No credit card required · Setup in minutes».
- **Типографика.** Lausanne. H1 56/61,6 w500, ls −1,68 px (−3%). H2 40/44, ls −0,8. Текст 16/26.
- **Палитра.** `#0a1916` — тёмно-зелёный почти чёрный, `#3ce0bf` — мятный акцент, кнопки с прямыми углами, светлые фоны `#fafafc` и `#f9f9f7`.
- Скриншот фрагмента: `ux04/shots/fathom-report.png` в той же временной папке.

### 7. Digits — digits.com

- **Первый экран.** H1 «Accounting software— / that works for you.»: первая строка w300, вторая жирная, по центру. Две кнопки: мятная `#00ffbe` и контурная. Ниже — интерфейс в рамке ноутбука и телефона с таблицей транзакций и суммами.
- **Типографика.** Stabil Grotesk. H1 80/76, ls −2,4 px (−3%). H2 56/53,2 w300. Текст 16/24.
- **Палитра.** Чёрный, белый, один свежий акцент.
- **Что взять.** Контраст начертаний внутри заголовка, чтобы выделить суть. Реальные суммы в таблицах.
- **Что не брать.** Рамки устройств: консалтинг показывает документы, а не гаджеты.

### 8. Linear — linear.app

- **Что взять.**
  - Систему серых: `#f7f8f8` — заголовки, `#d0d6e0` — подзаголовки, `#8a8f98` — основной текст, `#62666d` — подписи. Иерархия строится без цвета.
  - Плотный трекинг крупных заголовков: H1 64/64 w510, ls −1,408 px (−2,2%); H2 48/48, ls −1,056 px.
  - Скриншот продукта сразу под первым экраном.
- **Шрифты.** Inter Variable и Berkeley Mono.
- **Что не брать.** Тёмную тему (фон `#08090a`) и минимум текста: для консалтинга этого мало.

### 9. Vercel — vercel.com

- **Типографика.** Geist. H1 64/64 w400, ls −3,84 px (−6%). H2 56/56 w450. Текст `#171717` / `#4d4d4d` на `#fafafa`.
- **Кнопки.** Две одинакового размера: чёрная `#171717` «Deploy now» и белая с рамкой «Talk to sales». Скругление — таблетка.
- **Что взять.** Пару «главная / вторичная», сдержанность. Шрифт Geist и Geist Mono: в Google Fonts они теперь с кириллицей (проверено по метаданным).
- **Что не брать.** Абстрактный треугольник в центре: он ничего не объясняет. И трекинг −6% — для кириллицы он слишком плотный, нужно не больше −3%.

### 10. Yandex Cloud — yandex.cloud/ru

- **Первый экран.** H1 «В ответе за Тех.» в YS Display w900. Подзаголовок: «Технологическая платформа Яндекса для создания и развития цифровых продуктов». Кнопки «Попробовать бесплатно» (чёрная) и «Связаться с экспертом» (контурная). Справа — схемная иллюстрация, ниже — три карточки новостей.
- **Типографика.** YS Display w900: H2 48/52, H3 32/40. YS Text 17/24. Шрифты фирменные, в Google Fonts их нет.
- **Палитра.** `#000000`, `#ffffff`, `#e7ebf4` — подложка первого экрана, `#2a9fff` и `#fcc67f` — акценты иллюстраций. Скругление карточек 20 px.
- **Что взять.** Тяжёлый кириллический заголовок с коротким подзаголовком. Две кнопки с действием в названии.
- **Что не брать.** Игру слов в H1: без подзаголовка она не работает. Заголовок Axiom должен быть понятен сам.

### 11. Бюро Горбунова — bureau.ru/projects

- **Типографика.** H1 85/81 w700: интерлиньяж меньше кегля, заголовок «сжат». Текст 16–20 px. Подписи вынесены на поля справа от изображения. Фирменные Bureausans и Bureauserif.
- **Палитра.** Чёрный на белом плюс один красный акцент `#e20016`: активные ссылки и кнопка «Стать клиентом» (скругление 3 px).
- **Что взять.** Иерархию размером и воздухом. Подписи на полях к макетам отчётов. Один акцент. Кнопку, которая называет действие.
- **Учесть.** Главная bureau.ru сейчас занята промо «Чёрной пятницы», как референс бралась страница проектов.

### 12. Максим Ильяхов — maximilyahov.ru

- **Типографика.** Forma. H1 86,4/95 w900 «Максим Ильяхов, главред» и маленькое фото. Текст 18/25,7. Ссылки `#0060a0` с подчёркиванием.
- **Что взять.** Текст как главный элемент, простой язык, контакт в первом экране.
- **Что не брать.** Структуру из одного списка ссылок: у лендинга должна быть иерархия действий.

### Антиреференсы

Как раз полезно знать, чего избегать.

- **Centerview Partners.** H1 «Unparalleled Strategic Advice» (Roboto Slab w300, 65/68), тёмно-синий `#102f67`, фото холла офиса, в первом экране нет кнопки. Престижно, но за 10 секунд непонятно, что предлагают и кому. Взять можно только сдержанность засечных заголовков.
- **Evercore.** H1 «Client-Focused, Values-Driven.» (IBM Plex Sans w300, 72/93,6), `#1d4289` / `#002037`, видео с лондонским автобусом. Та же проблема.
- **Kruze Consulting.** H1 Lato w900 52/57 по центру и три абзаца (63 слова) в первом экране. Но страница цен образцовая: вилки $650–850 / $850–1500 / «Custom quote».
- **Graphite Financial.** Вокруг первого экрана — стоковые портреты, кнопки «LEARN MORE / WORK WITH US» ничего не говорят. Страница цен полезная: «Starting at $500» и «Pricing varies by: …».
- **Operis.** Настоящая командная фотография — это хорошо. Но H1 общий («We bring rigour and clarity to project finance»), кнопка «Discover Operis» ничего не обещает, первый экран — карусель. Фиолетовый `#6d1f7e` плюс золотой `#f8b323`.
- **F1F9.** Шаблон WordPress (Astra и Elementor, Poppins). Полезны только строка цифр «530+ моделей / 11 600+ обученных» и пункт FAST в меню.
- **Mercury.** Конкретное «Apply online in 10 minutes». Но в первом экране сгенерированный пейзаж со столом в горах — декор, который не несёт информации.
- **CloudPayments.** Конкретное «Подключение онлайн от 1 дня» и понятные иконки сервисов, но 3D-монеты и телефоны выглядят шаблонно.

## 2.3. Как красиво показать финансовые данные на лендинге

Паттерны трёх лучших примеров:

1. **Лист-документ** (Fathom). Белый лист с полями и колонтитулом на светлом фоне, два листа стопкой, тень едва заметна. Внутри — водопад или таблица с подписями статей и итоговыми строками на плашках. Для Axiom: «Аудит финмодели · стр. 3 из 18 · Замечания» и «Cash Flow · Сценарий B».
2. **Интерфейс-коллаж** (Pilot, Ramp). Основная таблица по месяцам, поверх — одна-две карточки с выводом («Net income +10%», «Flagged for review»). Цвет только у смысла: зелёный — рост, красный — падение.
3. **Бенто с фрагментами** (Stripe). В каждой карточке услуги — маленький настоящий кусок результата: строка таблицы, мини-график, замечание из лога аудита.

Общие правила по трём примерам:

- цифры табличные, выровнены по правому краю;
- подписи мелким серым или моноширинным шрифтом;
- не больше двух смысловых цветов плюс акцент;
- числа правдоподобные, с разрядами и валютой;
- подпись «данные изменены» — у Axiom это уже правило README.

---

# Часть 3. Два направления дизайна для Axiom

Оба направления — светлая тема, шрифты из Google Fonts с кириллицей (проверено по метаданным Google Fonts). В обоих один акцентный цвет и артефакты вместо декора. Контраст посчитан по формуле WCAG.

## Направление A. «Рабочий документ» — рекомендую

**Характер.** Аудиторская записка и аккуратная финмодель. Спокойно, точно, по-взрослому. Тёплая бумага, засечный шрифт в заголовках, страницы отчётов как главный визуальный объект, подписи на полях. Без SaaS-эстетики: Axiom продаёт работу людей и документы, а не подписку.

**В основе.** Fathom (листы отчётов), Бюро Горбунова (иерархия размером, подписи на полях, один акцент), Gridlines (структура страницы и таблица «что входит и сколько стоит»), Stripe (двухтоновые заголовки секций), Centerview и Evercore (засечная сдержанность, но с понятными словами).

**Палитра (светлая тема)**

| Роль | Hex | Контраст |
|---|---|---|
| Фон страницы, тёплая бумага | `#F8F6F1` | — |
| Поверхность: листы отчётов, карточки, форма | `#FFFFFF` | — |
| Фон чередующихся секций | `#EFECE4` | — |
| Основной текст, заголовки | `#15191E` | 16,3:1 на фоне |
| Вторичный текст, лиды | `#434B54` | 8,2:1 на фоне |
| Подписи, мелкий текст | `#596069` | 5,4:1 на `#EFECE4` |
| Линии, линейки таблиц | `#DDD8CC` | — |
| Акцент: главная кнопка, ссылки, выделение в отчётах | `#0E5446` | 8,2:1 на фоне; белый на акценте 8,8:1 |
| Акцент при наведении | `#0A3F35` | 11:1 |
| Мягкий акцент: подсветка строки или ячейки | `#E3EEEA` | акцент на нём 7,5:1 |
| Рост, «ок» в макетах | `#1A6B43` | 5,5:1 на `#EFECE4` |
| Падение, критичное замечание | `#B42318` | 6,1:1 на фоне |
| Золото: метки «проверено», мелкие акценты | `#8A5C0A` | 5,4:1 на фоне; только мелкие элементы |

Глубокий зелёный продолжает палитру из README (`#0B5345` + тёплый белый + золото для мелочей), но темнее и нейтральнее. В текущем `global.css` акцент синий `#1f4fd8`, это решение нужно будет свести.

**Шрифты**

- **Source Serif 4:** H1, H2, крупные цифры. Кириллица есть, переменная ось opsz, цифры табличные по умолчанию (проверено по ширине глифов).
- **Golos Text:** основной текст и интерфейс. Сейчас уже на сайте. Кириллица от ParaType, для цифр в таблицах есть `tnum`.
- **IBM Plex Mono:** метки, колонтитулы листов, числа в макетах отчётов. Кириллица есть, моноширинный.

**Шкала (десктоп / мобайл)**

- H1: Source Serif 4, 600, 56/60 → 36/40, ls −0,01em.
- H2: Source Serif 4, 600, 40/46 → 28/34; секционный заголовок двухтоновый (суть `#15191E`, пояснение `#434B54`).
- H3: Golos Text, 600, 22/28.
- Лид: 20/30, `#434B54`.
- Основной текст: 17–18/28, ширина колонки не больше 68ch.
- Метки: IBM Plex Mono, 500, 12/16, капс, ls +0,06em, `#596069`.
- Числа в макетах: IBM Plex Mono 13–14 px или Golos Text с `font-variant-numeric: tabular-nums`, выравнивание вправо.

**Форма и плотность.**
- Скругления 4 px: углы документа.
- Рамки 1 px `#DDD8CC`.
- Тень листа: `0 1px 2px rgba(21,25,30,.06), 0 12px 32px rgba(21,25,30,.06)`.
- Секции 96–120 px по вертикали.
- Сетка из 12 колонок, контент 1200 px.
- Текст выровнен влево; поле справа от макетов — под подписи.

**Ключевые компоненты.**
- Лист отчёта с колонтитулом.
- Строка замечания аудита с цветом критичности.
- Водопад денежного потока.
- Таблица сценариев (IRR, NPV, MOIC).
- Карточка услуги «проблема → что делаем → что получите → срок → от …».
- Карточка человека с фото.

**Риски и как их снять.**
- Засечки могут выглядеть «старым банком». Поэтому засечки только в H1, H2 и крупных цифрах, а весь интерфейс — Golos.
- Тёплый фон может казаться «грязным» на плохих экранах. Поэтому листы и форма — чисто белые.

## Направление B. «Финансовый инструмент»

**Характер.** Продуктовая чистота финтеха: белое поле, холодные серые, один насыщенный синий. Гротеск с плотным трекингом, бенто-сетка карточек, в каждой живой фрагмент интерфейса. Ощущение точного инструмента и современной команды.

**В основе.** Stripe (бенто и двухтоновые заголовки), Ramp (левый первый экран, моно-метки, один акцент), Vercel (пара кнопок, сдержанность, Geist), Linear (иерархия серых), Pilot (артефакт в первом экране), Yandex Cloud (жирная кириллица, кнопки).

**Палитра (светлая тема)**

| Роль | Hex | Контраст |
|---|---|---|
| Фон страницы | `#FFFFFF` | — |
| Фон чередующихся секций | `#F4F6F9` | — |
| Основной текст, главная кнопка | `#0B1220` | 18,7:1 |
| Вторичный текст | `#3E4A5C` | 9:1 |
| Подписи | `#5E6B7D` | 5,4:1 на белом, 5:1 на `#F4F6F9` |
| Линии и рамки карточек | `#E2E7EE` | — |
| Акцент: ссылки, графики, фокус, выделение | `#2348D8` | 7:1; белый на акценте 7:1 |
| Акцент при наведении | `#1A37A8` | 9,7:1 |
| Мягкий акцент | `#EAF0FD` | акцент на нём 6,2:1 |
| Рост | `#0E7350` | 5,4:1 на `#F4F6F9` |
| Падение | `#C2362B` | 5,5:1 |
| Предупреждение | `#A35F00` | 5:1 |

Главная кнопка тёмная `#0B1220`, как у Vercel, Ramp и Yandex Cloud. Синий остаётся для ссылок и смысловых выделений в графиках. Это близко к нынешнему `global.css` (`#10161d` + `#1f4fd8`).

**Шрифты**

- **Geist:** заголовки и текст. Кириллица в Google Fonts есть, `tnum` есть.
- **Geist Mono:** числа и метки.
- Запасная пара: Inter Tight (заголовки) + Inter (текст) + JetBrains Mono. Кириллица и `tnum` есть у Inter и Inter Tight.

**Шкала**

- H1: Geist 600, 64/66 → 38/42, ls −0,03em; для кириллицы не плотнее.
- H2: 44/48 → 28/32, ls −0,02em.
- H3: 20/26 600.
- Текст: 17/26.
- Метки: Geist Mono 12/16, капс.

**Форма и плотность.**
- Скругления 10–12 px у карточек, кнопки-таблетки.
- Рамка 1 px `#E2E7EE`, без теней или почти без них.
- Бенто-сетка из 2–3 колонок.
- Плотность выше, чем в A: секции 80–96 px.

**Риски.**
- Сайт может выглядеть как SaaS. Посетитель решит, что это софт, и будет искать «попробовать бесплатно».
- Труднее отстроиться от десятков похожих финтех-лендингов.
- Меньше «бумажной» осязаемости результата.

## Рекомендация: A «Рабочий документ»

1. **Соответствие категории.** Привычный вид для категории повышает симпатию ([Tuch et al., 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). Axiom — консалтинговая фирма, её результат — документы и решения. Направление A выглядит как консалтинг, только яснее, чем Centerview или Evercore. B подаёт сигнал «это софт».
2. **Отвечает на главные критерии и опасения покупателя.** Листы отчётов — это прошлые результаты и экспертиза, критерии №1–2 у Hinge. Они же снимают опасение №1 «пообещают и не сделают»: видно, что именно получишь.
3. **Цифры читаются лучше.** У Source Serif 4 и IBM Plex Mono цифры табличные по умолчанию: таблицы IRR и Cash Flow ровные без дополнительных настроек.
4. **Преемственность.** Golos Text остаётся. Глубокий зелёный и золото для мелочей продолжают палитру из README.

**Что взять из B в рамках A.** Бенто-сетку для карточек услуг (Stripe), пару кнопок «главная / тихая альтернатива» (Vercel, Yandex Cloud), моно-метки над заголовками (Ramp, Puzzle) и левый первый экран (Ramp).

**Как может выглядеть первый экран.** Это эскиз для обсуждения, формулировки утверждаются отдельно.

- Слева:
  - метка IBM Plex Mono «ФИНАНСОВЫЙ КОНСАЛТИНГ ДЛЯ ДЕВЕЛОПЕРОВ · ЮВА · ОАЭ · СНГ»;
  - H1 в Source Serif 4 — услуга и результат;
  - лид — список из трёх услуг;
  - кнопка `#0E5446` «Обсудить проект» и рядом ссылка «или написать в Telegram»;
  - строка фактов: лет опыта, число моделей, страны.
- Справа: два листа стопкой — страница аудита с замечаниями и лист Cash Flow, с подписью на полях «Пример отчёта, данные изменены».

---

## Источники

**Поведение покупателей профуслуг и B2B**
- Hinge Research Institute. [Beyond Referrals: How Today's Buyers Check You Out](https://kevin.lexblog.com/wp-content/uploads/sites/111/2014/02/HIN-BeyondReferrals-Report-021314-1.pdf), 2014, 1028 покупателей.
- Hinge. [How Buyers Buy, Executive Summary](https://hingemarketing.com/uploads/HowBuyersBuy_Executive_Summary.pdf), исследование 2013 г.: 822 покупателя, 533 продавца.
- Hinge. [Inside the Buyer's Brain, 2nd ed., Executive Summary](https://hingemarketing.com/wp-content/uploads/2018/09/Research-2018-IBB-SecondEdition-ExSumm.pdf), 2018: 1475 покупателей, 3005 продавцов.
- Hinge. [Inside the Buyer's Brain 2022, вебинар](https://hingemarketing.com/wp-content/uploads/2022/09/IBB-Webinar-2022.pdf): 1914 покупателей.
- Gartner. [B2B Buying Journey](https://www.gartner.com/en/sales/insights/b2b-buying-journey); [пресс-релиз 25.06.2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience) и его [пересказ в Mi3](https://www.mi-3.com.au/04-07-2025/gartner-survey-reveals-b2b-buyers-preference-rep-free-experience); [пресс-релиз 09.03.2026](https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience).
- Forrester. [The State Of Business Buying, 2024](https://www.forrester.com/press-newsroom/forrester-the-state-of-business-buying-2024/); [2026](https://www.forrester.com/press-newsroom/forrester-2026-the-state-of-business-buying/); [Should You Make Your Prices Public on Your Website?](https://www.forrester.com/blogs/prices-public-on-website)
- Clutch. Опрос B2B-покупателей, 2020, 451 человек: [перепечатка пресс-релиза](https://martechseries.com/technology/b2b-buyers-concerned-transparent-costs-b2b-companies-websites-highlighting-importance-trust-b2b-sales-funnel/), [оригинал](https://clutch.co/press-releases/b2b-buyers-most-concerned-about-transparent-costs-b2b-companies-websites).

**NN/g**
- [How Long Do Users Stay on Web Pages?](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/), 2011
- [Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/), 2018
- [Horizontal Attention Leans Left](https://www.nngroup.com/articles/horizontal-attention-leans-left/), 2017
- [F-Shaped Pattern of Reading](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/), 2006/2017
- [Concise, Scannable, and Objective](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/), 1997
- [Show Numbers as Numerals](https://www.nngroup.com/articles/web-writing-show-numbers-as-numerals/), 2007
- [Top 10 Guidelines for Homepage Usability](https://www.nngroup.com/articles/top-ten-guidelines-for-homepage-usability/), 2002
- [B2B Usability](https://www.nngroup.com/articles/b2b-usability/), 2006
- [B2B Website Usability, 3rd ed.](https://www.nngroup.com/reports/b2b-websites-usability/), отчёт
- [State the Price](https://www.nngroup.com/articles/show-price/), 2013
- [What B2B Designers Can Learn from B2C About Building Trust](https://www.nngroup.com/articles/b2b-trust-from-b2c/), 2019
- [Trustworthiness in Web Design](https://www.nngroup.com/articles/trustworthy-design/), 2016
- ['About Us' Information on Corporate Websites](https://www.nngroup.com/articles/about-us-information-on-websites/), 2019
- [Contact Us Page Guidelines](https://www.nngroup.com/articles/contact-us-pages/), 2019
- [Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/)
- [Website Forms Usability: Top 10](https://www.nngroup.com/articles/web-form-design/), 2016
- ["Get Started" Stops Users](https://www.nngroup.com/articles/get-started/), 2017
- ["Learn More" Links](https://www.nngroup.com/articles/learn-more-links/), 2015

**Доверие, восприятие, читаемость**
- Fogg, B.J. [Stanford Guidelines for Web Credibility](https://credibility.stanford.edu/guidelines/index.html), 2002.
- Fogg et al. [How Do People Evaluate a Web Site's Credibility?](https://advocacy.consumerreports.org/research/how-do-people-evaluate-a-web-sites-credibility), 2002, 2684 участника.
- Tuch et al. [The role of visual complexity and prototypicality…](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/), 2012, и [пост в блоге Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/).
- Baymard. [Optimal Line Length](https://baymard.com/blog/line-length-readability), 2022; [Seemingly Unnecessary Information](https://baymard.com/blog/checkout-experience-seemingly-unnecessary-information), 2012.
- Adobe Blog. [When Less Is More: Web Forms](https://blog.adobe.com/en/publish/2018/07/09/less-dos-donts-designing-web-forms), 2018, данные MarketingExperiments.
- Oldroyd, McElheran, Elkington. The Short Life of Online Sales Leads. HBR, 2011 ([карточка публикации](https://scholarsarchive.byu.edu/facpub/9711)); цифры по вторичным источникам.

**Цены и финансовые услуги**
- SRA. [Price transparency in the legal services market](https://guidance.sra.org.uk/globalassets/documents/sra/research/price-transparency-legal-services-market.pdf), 2017.
- Kitces. [Why Advisors Should Be Transparent About Fees & Minimums](https://www.kitces.com/blog/advisory-firm-fees-minimums-website-fiduciary-transparency-price-haggling/); [Why Your Pricing Should Be Clearly Stated On Your Website](https://www.kitces.com/blog/why-your-financial-planning-pricing-should-be-clearly-stated-on-your-website/).
- Страницы цен и услуг: [Gridlines Model Audit](https://www.gridlines.com/model-audit/), [Kruze Pricing](https://kruzeconsulting.com/pricing/), [Graphite Pricing](https://graphitefinancial.com/pricing/), [Pilot Pricing](https://pilot.com/pricing).
- [ICAEW Financial Modelling Code](https://www.icaew.com/technical/technology/excel-community/improve-your-financial-modelling-practice); [FAST Standard](https://www.fast-standard.org/).
- Umbrex. [Demonstrate Experience Without Compromising Confidentiality](https://umbrex.com/resources/the-generative-engine-optimization-playbook-a-guide-for-professional-services/demonstrate-experience-without-compromising-confidentiality/), практическое руководство.

**Шрифты.** Наличие кириллицы — по [метаданным Google Fonts](https://fonts.google.com/metadata/fonts). Наличие `tnum` и табличных цифр по умолчанию проверено в файлах, которые отдаёт `fonts.googleapis.com`.
