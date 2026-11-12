# Nota · Business plan

**Verdict: Not yet**

- ✓ Each paying client-month (one active subscription for one month) earns $16.77 before fixed costs (56% contribution).
- ✓ Year 1 operating profit: $93,417.
- ✓ Break-even is 45 paying client-month (one active subscription for one month)s a day against a capacity of 100000.
- ✗ 21 of 100 simulated buyers buy (21%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $30.00 a paying client-month (one active subscription for one month) |
| Profit margin at plan | 53% per paying client-month (one active subscription for one month) |
| Break-even | 45 paying client-month (one active subscription for one month)s a day |
| Year 1 operating profit | $93,417 |
| Startup spend | $0 |
| Cash needed before it pays for itself | $0 |
| Startup money earned back | month 1 |
| Buyer panel | 21 buy · 79 pass |

## The idea

- What it is: a Telegram bot that collects payment documents (receipts, invoices, handwritten delivery notes, bank-transfer screenshots, PDFs, ZIP archives) from work chats, checks them for duplicates and arithmetic errors, and writes each one as a row in the owner's own Google Sheet with a link to the original.
- Who it is for: any business owner (small business without a finance department) who has a Telegram group where employees, partners and the owner drop receipts and payments to be reimbursed or accounted for. First market: Bali / Indonesia, Russian-speaking owners and their local teams.
- What it sells, at what price: subscription, $19/month for up to 100 documents and up to 5 connected groups. First 40 documents free. Connection takes about one minute (log in with Google).
- Where and how: online, inside Telegram (@NotaGetBot). Customers find it through 10–30 free permanent accesses given to friends, the founder's ~10 warm contacts who need it, word of mouth, viral loops built into the product (shareable weekly report card, bot reactions in groups, referral links), and automated posting on Threads.
- Budget and constraints: budget not stated. Built and run by Axiom Consulting (finance consultancy, 15 years in cost control). MVP works; payments and Google OAuth verification not yet done. Goal (confirmed by founder 11.11.2026): 50 paying clients in month 1, 100 in month 2, 1,000 paying in 12 months (avg ~$30 → ~$30k MRR). Prices $19 / $45 / $119 for 100 / 300 / 1000 documents.

## Summary

**Вердикт: Not yet (пока нет).** Три из четырёх проверок пройдены. Не пройдена одна — спрос: в панели покупают 21% смоделированных покупателей при пороге 25%. Повторная проверка нового предложения на 20 тех же покупателях дала 25% (было 20%), но это в пределах шума.

**Что должно измениться — и кто это меняет:**
- **Доказать спрос на живых людях.** Бесплатная проверка архива рабочего чата должна находить реальные деньги. Это проверка «основатели» из `launch.md`: 20 человек, порог успеха — 5 предоплат за 3 месяца до 7.12.
- **Если живые не платят:**
  - находки есть — менять предложение (`/founder-offer`);
  - находок мало — менять обещание: таблица без админа вместо дублей (`/founder-offer` и `/founder-marketing`).

**Что это за бизнес.** Nota (@NotaGetBot) — Telegram-бот для малого бизнеса без финотдела. Он собирает чеки, счета и рукописные накладные из рабочих чатов в Google-таблицу владельца и ловит дубли и несходящиеся суммы до оплаты. Первый рынок — Бали: стройка, виллы, магазины и прокат байков, владельцы на расстоянии.

**Три числа** (`cfo.md`):
- **Маржа:** один платящий клиент в месяц приносит $16,77 из $30, то есть 56%, после ИИ, комиссии и привлечения (разложенного на 12 месяцев). Без привлечения — ~89%.
- **Точка безубыточности:** 45 платящих клиентов при постоянных расходах $740 в месяц.
- **Первый год:** при цели 1 000 клиентов к 12-му месяцу — $93 тыс. операционной прибыли на бумаге. Если платить за рекламу сразу, по деньгам выходит около +$3 тыс., и до выхода в плюс нужно вложить около $27 тыс.

**В чём совпали и где разошлись совет и панель.**
- **Совпали:** продукт продуман, дешёв в обслуживании, лучше всего подходит стройке и тем, кого уже обманывали. Покупатель решает, увидев найденные деньги на своих данных. Широкий фокус вреден.
- **Разошлись:** совет (Продукт, 6 баллов) ценит вкус и продуманность. Монополия (4 балла) считает, что защиты от копирования нет. Панель добавила то, чего совет не видел: главные потери у части владельцев — наличные механикам и завышенные цены на настоящих чеках. Поиск дублей их не ловит.

**Главный риск — платить за рост до того, как измерена конверсия.** При конверсии из установки в оплату 5% год уходит в −$149 тыс., при 20% — в +$79 тыс. Что делаем: первые 50–100 клиентов набираем через личную сеть, клиентов Axiom и партнёров. Рекламу по $10 за установку включаем только при конверсии ≥12%.

**Что нужно для старта:**
- **Деньги.** Постоянные $740 в месяц: продукт окупает их уже при 45 клиентах. На платный рост до 1 000 клиентов нужно $25–30 тыс. оборотных, но только после замера конверсии.
- **Блокеры.** Приём платежей и верификация Google OAuth (лимит 100 пользователей).
- **Первый тест.** Проверка «основатели» 23–29.11.

**Главное на этой неделе:** подать заявку на эквайринг в Bank of Georgia и на верификацию Google OAuth со scope drive.file. Обе задачи на критическом пути запуска 7.12.

---

Панель — это смоделированные покупатели, а все числа — прогнозы. Подтверждают их живые клиенты и реальные счета. Это не финансовая, налоговая или юридическая консультация.

## What the board said

**Голосование: 3 × FUND IF (финансировать при условиях). Средний балл 5,0 из 10.**

| Методика | Балл | Голос | Заседание 1 |
|---|---|---|---|
| Оффер (Offers lens) | 5 | FUND IF | 5 |
| Монополия (Monopoly lens) | 4 | FUND IF | 4 |
| Продукт (Product lens) | 6 | FUND IF | 7 |

Отзывы: `board/offers.md`, `board/monopoly.md`, `board/product.md`. Бриф: `board/brief.md` + `board/product-description.md`. Первое заседание: `board/round1/`.

**Что изменилось после полного брифа.** Вопрос маржи снят: при $0,01–0,02 за документ все трое признают, что экономика документа хорошая (маржа 80%+), и это даёт запас на щедрый пробный период и гарантию. Лестница тарифов $19 / $45 / $119 уже есть. Баллы при этом не выросли: полное описание само честно называет главные слабости (нет платящих, нет массового канала, связка копируется, точность не замерена, платежи и OAuth не готовы), и совет с ними согласился. Продукт снизил балл с 7 до 6 из-за блокеров запуска и широты планов (12 сфер, 3 волны рынков, второй продукт).

### Риски, которые назвали несколько членов совета

1. **Нет доказательства результата у клиента** (все трое). Платящих ноль, точность распознавания и поиска дублей не замерена, новый модуль проверки ещё в разработке. Кейс с 1 млрд IDR получен в большой системе Axiom, а не в Nota. Главной цифры «Nota поймала дублей на X» нет.
2. **Нет массового канала** (Оффер, Монополия). Личная сеть даёт около 30 клиентов по вашей же оценке, вирусность 0,1–0,3 — усилитель, а не двигатель. CAC неизвестен. Цель $10 000/мес за 3 месяца (≈526 платящих по $19 или ≈333 по $30) с этим не сходится.
3. **Без пойманного дубля Nota выглядит как обычный «чек в таблицу»** (Оффер, Продукт). Такие боты стоят от £3,99, Hubdoc $12. У маленькой компании (~37 документов в месяц) дубль за 40 пробных документов может не встретиться, и клиент не увидит главную ценность.
4. **Легко скопировать, барьер не растёт** (Монополия, Оффер). Описание само говорит, что это «фора во времени». Ни сетевого эффекта, ни бренда, ни замера «в разы лучше конкурентов» пока нет.
5. **Широкий фокус** (Продукт, Монополия). «Любой, у кого есть группа» в чате против «5–50 человек без финотдела» в описании, 12 сфер, Пхукет/Дубай/Узбекистан, второй продукт, 41 идея в бэклоге.
6. **Блокеры запуска** (Оффер, Продукт). Приём платежей не подключён, Google OAuth без верификации ограничен 100 пользователями, оплата на внешней странице разрывает путь из Telegram.

### Где члены совета расходятся

- **Сила продукта.** Продукт ставит 6: опыт продуман от клиента, «контроль, а не учёт», список «не делаем», 37 продуманных ситуаций уведомлений — это вкус. Монополия ставит 4: вкус не барьер, через полгода клон или Telegram-канал у Dext съест нишу, если не появится растущий актив.
- **Цена.** Оффер предлагает уйти от цены за документы к цене за пойманные деньги и проверить $39 на одном сегменте: ваша собственная компания помещается в $19, значит типичный покупатель платит потолком $19. Монополия и Продукт цену не оспаривают.
- **Что такое «секрет».** Монополия видит секрет в знании схем закупочного мошенничества и 100 000 документах, но требует превратить его в растущий актив (база накладных на бахаса, сеть партнёров-УК и бухгалтеров, данные о схемах). Продукт считает, что секрет проявится только через замер точности.

### Условия: чек-лист для следующих шагов

- [ ] Закрыть блокеры: приём платежей (Bank of Georgia или Telegram Stars с первого дня, оплата в два касания, по возможности без выхода из Telegram) и верификация Google OAuth. → `/founder-ops`
- [ ] Замер точности на 500+ реальных документах до платного запуска: суммы в IDR, ложные и пропущенные дубли, переснятый чек и скриншот. → продукт
- [ ] Сравнить поиск дублей с хотя бы одним конкурентом (REME или Dext) на тех же документах. Разница должна быть разительной. → `/founder-competitors`
- [ ] Один сегмент на запуск (стройка/ремонт или УК вилл на Бали): лендинг, категории, пример отчёта под него. Остальные сегменты и новые страны заморозить до 20–30 платящих. → `/founder-consumer`, `/founder-marketing`
- [ ] Ценность в первый день: загрузка архива чата (уже есть, 20 документов) должна сразу давать отчёт «что нашли в вашем архиве». Метрика: доля пробных пользователей, увидевших хотя бы один флаг. → `/founder-offer`
- [ ] Оффер вокруг денег, а не документов: «контроль утечек», гарантия с понятным условием (например, возврат, если за месяц ничего не найдено), бонусы (аудит архива, разбор первого месяца). → `/founder-offer`, `/founder-cfo`
- [ ] Проверить более высокую цену (например, $39) хотя бы на одном сегменте до того, как закреплять $19. → `/founder-pricing`
- [ ] 20–30 платящих из личной сети, конверсия из пробного периода и первая цифра «дублей поймано на X» минимум у 3–5 бизнесов вне своей компании. → `/founder-launch`
- [ ] Провести 10 незнакомых людей через путь от ссылки до оплаты, исправить каждое место, где они споткнулись. → `/founder-launch`
- [ ] Найти один повторяемый канал с измеренным CAC (партнёры-УК, бухгалтеры или реклама в Telegram) до расширения в другие страны. → `/founder-marketing`
- [ ] Письменно назвать барьер, который растёт с каждым клиентом (технология, сеть партнёров, масштаб или бренд), и чем это будет видно через 12 месяцев.
- [x] Цель по выручке выбрана (11.11.2026): 50 → 100 → 1000 платящих за 12 месяцев, около $30 тыс. MRR. → `/founder-cfo`
- [ ] Сократить 37 уведомлений до тех, которые клиент реально замечает.

### Самая сильная версия этого бизнеса

Совет видит Nota как «контроль утечек» для одной ниши на Бали, где утечки самые дорогие: стройки, ремонтные подрядчики и управляющие компании вилл. Вход — загрузка архива рабочего чата: в первый же день владелец получает отчёт «что мы нашли в вашей истории», а не ждёт дубля неделями. Продаётся не «100 документов за $19», а деньги, которые перестанут уходить, с гарантией и ценой, которая растёт с объёмом и числом объектов. Вашу экспертизу (100 000 документов, схемы закупщиков, кейс с 1 млрд IDR) совет предлагает превратить в растущий актив: базу местных документов и схем, сеть партнёров-УК и бухгалтеров, отчёты для собственников вилл (у одной УК 10–30 собственников). Это уже есть в ваших планах, но стоит в этапах 3–4. Совет предлагает перенести это в начало, а широкую географию и личные финансы отложить. Это отличается от сказанного в чате («любой бизнес с группой», рост за счёт вирусности), и совет говорит об этом прямо.

## The competition

Проверено 11.11.2026. Источники:
- ваш разбор отзывов «Конкуренты: AI-учёт расходов из чата» (копия в `research-existing-competitors.txt`);
- новый поиск по Индонезии и Telegram-ботам (`research-local-competitors.md`). Все строки с фактами лежат в `competitors.csv`.

**Проверка.** Цены и функции сверены на страницах вендоров 11.11.2026. В `research-local-competitors.md` у каждого факта стоит метка: [стр.] — проверено на странице, [сниппет] — только из поиска. Только из поиска остались помесячная цена Dext $31,50 (страница рисует её через JS) и отдельные мелочи. Google Play без JS отдаёт всего по 3 отзыва на язык. Поэтому по индонезийским приложениям прочитано по 6 отзывов, и все темы ниже помечены как тонкие (мало данных).

Рупии пересчитаны в доллары приблизительно, по курсу ~Rp16 500 за $1. Это допущение, а не данные.

### 1. Кто на рынке

Отсортировано по тому, насколько прямо продукт конкурирует с Nota.

| Продукт | Тип | Канал | Цена для бизнеса на ~5 человек и ~100 документов в месяц | Дубли |
|---|---|---|---|---|
| [REME](https://reimburseme.ai/pricing/) | прямой | WhatsApp, email, веб (Сингапур) | $5–8 за активного пользователя → **$25–40/мес**; месяц бесплатно без карты | Да, включая другой ракурс; рукописные чеки |
| [Mekari Expense](https://expense.mekari.com/en) | прямой, местный | своё приложение (Индонезия), чеки через мессенджер не принимает | Rp30 000 за сотрудника при **минимуме 50 сотрудников** → от ~Rp1,5 млн (**≈$90**)/мес; OCR включён | Да, «Fraud AI Checker»: одинаковые и почти одинаковые заявки за 7 дней ([блог](https://expense.mekari.com/en/blog/duplicative-transaction-detection)) |
| [KasKecil.id](https://kaskecil.id/) | косвенный, местный | бот в WhatsApp и Telegram, данные в своём дашборде | бесплатно до 100 транзакций; Premium **Rp149 000 (≈$9)/мес** | нет; групповых чатов и Google Sheets тоже нет |
| [Dext](https://dext.com/business/pricing) | косвенный | приложение, email, WhatsApp | **$31,50/мес** помесячно ($25,21 при оплате за год), 250 документов | заявлены, в отзывах слабое место |
| [Zoho Expense](https://www.zoho.com/expense/pricing/) | косвенный | приложение, email, **WhatsApp** (новое в Standard) | $3 при оплате за год / $4 помесячно за пользователя, до 3 пользователей бесплатно → **$0–20/мес** | подсвечивает; в Standard добавлен AI-аудит фрода |
| [Expensify](https://use.expensify.com/product) | косвенный | приложение, email, SMS | по тарифу (не перепроверено) | дата + сумма, ставит на паузу |
| [Hubdoc](https://www.capterra.com/p/165724/Hubdoc/pricing/) | косвенный | приложение, email | **$12/мес** (часть источников пишет $20) | нет, жалобы на двойные записи |
| [Veryfi](https://www.veryfi.com/products/whatsapp-receipt-submission-integration/), [WellyBox](https://www.g2.com/products/wellybox/reviews) | косвенный | приложение, email, WhatsApp | не найдена | жалобы на повторы |
| [Tailride](https://tailride.so/integrations/telegram) | косвенный | Telegram, WhatsApp → QuickBooks/Xero | бесплатно 10 счетов/мес, платные тарифы не найдены | да, повтор не тарифицируется |
| [ProverkaCheka](https://proverkacheka.kz/blog/telegram-bot-gruppa-nastrojka/) | косвенный | группа в Telegram (Казахстан) | не найдена | да, общая база в группе, но только чеки Kaspi по QR |
| [Project Receipts Bot](https://roksana870.github.io/) | косвенный | Telegram → Google Sheets и Drive | не найдена | не указано |
| [ReceiptRipper](https://receiptripper.com/), [Мобс](https://productradar.ru/product/mobs-bot/) и др. | косвенный | WhatsApp/Telegram → Google Sheets | от £3,99/мес за 50 чеков; у Мобс есть бесплатный тариф | редко |
| [Jurnal](https://www.jurnal.id/id/harga/essentials/), [Accurate](https://accurate.id/trial/aol/), [Kledo](https://kledo.com), [majoo](https://majoo.id/harga) | замена (бухгалтерия/POS) | веб, приложение | Kledo Rp159 900, majoo Rp249 000, Jurnal Rp299 250 (за год), Accurate Rp333 000 → **≈$10–20/мес** | OCR и проверка дублей не найдены |
| [BukuWarung](https://play.google.com/store/apps/details?id=com.bukuwarung) | замена (учёт для микробизнеса) | приложение | бесплатно, сместился в платёжного агента (EDC, PPOB) | нет; Google Play **3,2★, 94,7 тыс. отзывов, 35% единиц** |
| [Шаблоны n8n](https://n8n.io/workflows/19225-track-employee-expense-receipts-from-telegram-with-gpt-4o-mini-and-google-sheets), open-source боты | замена (сделать самому) | Telegram/WhatsApp → Google Sheets | $0 + хостинг + ИИ + время владельца | по ID сообщения или по связке «продавец + дата + сумма» |
| Вручную: чат + таблица + администратор | замена | рабочие группы | время сотрудника | по памяти |

### 2. Разброс цен

Сравнимый вариант: бизнес на ~5 человек и ~100 документов в месяц, у которых есть публичная цена.
- **Минимум:** $0. Это Zoho Free до 3 пользователей, KasKecil Free и самодельный бот на n8n.
- **Медиана:** около **$12–17/мес**. Ряд такой: ReceiptRipper ≈$5, KasKecil ≈$9, Hubdoc $12, Zoho $15–20 за 5 человек, REME $25, Dext $31,50.
- **Максимум:** $31,50 у Dext и $40 у REME Growth на 5 человек.
- **Nota:** **$19 за 100 документов** при любом числе сотрудников. Это чуть выше медианы. Для команды больше 5 человек Nota дешевле REME и Zoho, потому что они берут деньги за каждого пользователя.

### 3. Карта позиций

Две оси, важные для владельца: **сколько усилий нужно от сотрудников** (поставить приложение, заполнить форму или просто писать в чат как раньше) и **насколько глубоко продукт проверяет** (просто записывает или ловит дубли и ошибки).

```
                        глубокая проверка (дубли, фрод)
                                   ▲
       Mekari Expense ●            │            ● REME (WhatsApp, отдельный номер)
       Expensify ●  Zoho ●         │
       Dext ●                      │                  ★ Nota (существующие группы
                                   │                     Telegram, дубли, рукопись)
                                   │      ● ProverkaCheka (только Kaspi)
                                   │      ● Tailride (в учётку, не в таблицу)
сотрудники ◄───────────────────────┼───────────────────────► сотрудники ничего
ставят приложение                  │                         не меняют
                                   │
       Hubdoc ●  Jurnal/Accurate/  │      ● n8n / самодельные боты
       Kledo/majoo ●               │      ● KasKecil, Мобс, ReceiptRipper,
       Veryfi ● WellyBox ●         │        Project Receipts Bot
                                   │      ● вручную: чат + таблица
                                   ▼
                          просто записывает
```

Правый верхний угол почти пуст. Ближе всех там REME, но он работает через отдельный номер WhatsApp: официальный WhatsApp API не подключается к уже существующим группам ([Unipile](https://www.unipile.com/whatsapp-group-api/)). Кроме того, REME продаётся компаниям среднего размера за каждого пользователя.

### 4. На что жалуются клиенты конкурентов

Темы отсортированы по тому, у скольких продуктов они повторяются. Пункты 1–5 взяты из вашего разбора отзывов, пункт 6 — из индонезийских приложений.

1. **Дубли и двойные записи (5 продуктов).**
   - У Hubdoc появляется дубль, если документ не сопоставился с транзакцией ([Xero App Store](https://apps.xero.com/hk/app/hubdoc//reviews)).
   - У Dext поиск дублей назван главным недостатком ([Capterra AU](https://www.capterra.com.au/reviews/160189/dext)).
   - Veryfi сканирует чек дважды и складывает документы, склеенные в один PDF ([Capterra](https://www.capterra.com/p/180429/Veryfi/reviews/)).
   - WellyBox подтягивает три документа на одну покупку ([Trustpilot](https://at.trustpilot.com/review/wellybox.com)).
   - Expensify создаёт дубль, если чек не склеился с картой ([справка](https://help.expensify.com/articles/expensify-classic/expenses/How-to-prevent-duplicate-expenses)).
2. **Распознавание плохих чеков (4 продукта).** Выцветшие, мятые, неанглийские и многострочные чеки приходится править руками.
   - У Expensify на G2 это главные минусы: 36 и 34 упоминания ([CheckThat](https://checkthat.ai/brands/expensify/reviews)).
   - В Hubdoc один пользователь вводил вручную около 90% полей ([Xero App Store](https://apps.xero.com/hk/app/hubdoc//reviews)).
3. **Деньги (4 продукта).**
   - Подорожание Dext на 10–30% при продлении ([CostBench](https://costbench.com/compare/dext-vs-quickbooks-online/)).
   - Непонятные списания и сложная отмена у Expensify.
   - Платные допы у WellyBox.
4. **Поддержка (3 продукта), мнения полярные.** Dext на GetApp получает 3,9 за поддержку при 4,8 на Trustpilot. У Veryfi не работает чат.
5. **Скорость и интерфейс (3 продукта).** После перехода Expensify на чат-интерфейс простые правки требуют больше кликов.
6. **Индонезийские приложения: ошибки, падения и слабая поддержка (4 продукта, у каждого мало данных).** Цитаты со ссылками лежат в `research-local-competitors.md`.
   - BukuWarung: потеря данных, баги и ухудшение после обновлений.
   - Mekari Jurnal: ошибки, медленная поддержка, мобильное приложение беднее веб-версии, не приходит OTP.
   - Mekari Expense: приложение падает, ошибки загрузки.
   - majoo: «ошибки и медленная поддержка» ([Kimola](https://kimola.com/reports/unlock-insights-majoo-app-user-feedback-report-google-play-en-158143)).

   Общий вывод: местные приложения раздражают нестабильностью. Бот в привычном Telegram без отдельного приложения отвечает на это напрямую.

### 5. Свободная ниша

**Готового коммерческого продукта, который совмещает бота в уже существующей рабочей группе, проверку дублей между людьми, чатами и ракурсами и Google-таблицу владельца, не нашлось.** Все три признака сразу есть только в самодельных шаблонах n8n и open-source ботах. Что это значит:

- **Спрос сформулирован именно так.** На Freelancer есть заказ на бота с проверкой дубликатов чеков и синхронизацией с Google Sheets ([Freelancer](https://www.fi.freelancer.com/projects/telegram-api/telegram-40640137)). На n8n есть шаблон «Track employee expense receipts from Telegram…».
- **Боль конкурентов совпадает с ядром Nota.** Дубли и плохое распознавание — две главные жалобы на рынке. Вы делаете упор именно на это: другой ракурс, скриншот, рукописная накладная на бахаса, сверка позиций с итогом.
- **Местные игроки сюда не заходят.**
  - Mekari Expense проверяет дубли, но работает через своё приложение. Он берётся за компании от 50 сотрудников: минимум около $90 в месяц.
  - KasKecil работает в Telegram и стоит дешевле, но это учёт мелкой кассы для одного владельца. Групп, проверки дублей и Google Sheets у него нет: это проверено на странице.
  - Бухгалтерские системы (Jurnal, Accurate, Kledo, majoo) стоят $10–20 в месяц, но чеков не читают.

Ниша узкая, и её нужно доказывать. Совет уже говорил: без измеренной точности на тех же документах против REME или Dext это пока заявление, а не преимущество.

### 6. Кто может повторить быстрее всех

1. **Самодельные боты на n8n и open-source.** Это главная замена Nota уже сегодня: технически подкованный владелец соберёт «Telegram → GPT → таблица» с простой проверкой дублей за вечер. Отвечать на это нужно не функциями, а качеством: ловить переснятый чек, читать рукописные накладные, работать в группе так, чтобы бот не мешал, плюс недельный отчёт. И всё это без настройки.
2. **REME.** Модель уже та же («чат + антифрод»). Если REME добавит Telegram-группы, у него сразу будет бизнес-логика и интеграции. Пока он ориентирован на средние компании и на WhatsApp.
3. **KasKecil и индонезийские WhatsApp-боты** (Mingo, CatatAja, BotMoni). У них уже есть местные пользователи, Telegram у KasKecil и цена ≈$9. Добавить работу в группах и проверку дублей технически несложно.
4. **Mekari.** Крупнейший местный игрок с антифродом и базой клиентов. Он может выпустить бота в мессенджере, если увидит спрос.
5. **Zoho Expense.** Он уже добавил приём через WhatsApp и AI-аудит фрода в тариф за $3–4, а для 3 пользователей он бесплатный. Пока это личный канал сотрудника, а не бот в общей группе, но Zoho движется в вашу сторону быстрее остальных крупных игроков.
6. **Dext или Expensify с каналом в Telegram.** Это возможно, если рынок покажет спрос. В вашем описании этот риск уже назван.

### Что брать дальше

- В `/founder-consumer`: главные возражения покупателя:
  - «у меня бесплатный Zoho / KasKecil / самодельный бот»;
  - «а точно найдёт дубль?»;
  - «боюсь давать доступ к Google и чатам»;
  - «распознавание ошибается на плохих чеках».
- В `/founder-pricing`:
  - медиана сравнимых вариантов $12–17;
  - верх рынка $31,50–40;
  - модели «за пользователя» у REME и Zoho против «за документы» у Nota.
- Открытый замер для Монополии: точность поиска дублей у Nota против REME или Dext на одних и тех же 100–500 реальных балийских документах.

## The buyer panel

**21 buy · 79 pass** (21% buy) out of 100 simulated buyers. Seed 843138, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Construction / renovation contractor or developer | 30 | 33% |
| Shop or bike/scooter rental owner | 15 | 20% |
| Villa management company or villa rental operator | 25 | 20% |
| Remote investor in villas or a build, living abroad | 13 | 15% |
| Café / restaurant owner | 17 | 6% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Burned before | 12 | 50% |
| Runs everything through chats | 22 | 41% |
| Has an admin with Excel | 18 | 33% |
| Already uses an app | 12 | 0% |
| Tech-savvy DIY | 8 | 0% |
| Privacy-wary | 10 | 0% |
| Price-sensitive | 12 | 0% |
| Delegates to a bookkeeper | 6 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $124,000 and up | 34 | 29% |
| $77,000 to $124,000 | 33 | 24% |
| under $77,000 | 33 | 9% |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 33 | "My admin already types the receipts into Excel every week. It's behind, sure, but it gets done, and I'm not paying a monthly fee and moving everything to Google Sheets to fix something that roughly works." (P001) · "My bookkeeper already runs everything through Zoho and it works well enough. The missing documents are a staff discipline problem, and I'm not adding another tool and another login from overseas on the strength of a Telegram bot I've never heard of." (P002) |
| trust | 23 | "I might throw the 40 free documents at it out of curiosity, but I wouldn't pay. A brand-new bot from a team I've never heard of, sitting in my staff chats and my Google Drive, could vanish in six months, and I could put together something good enough with n8n and ChatGPT over a weekend." (P003) · "I don't put an unknown bot in my staff chat or sign it into my Google account. It would read everything people write there, not only receipts. The missing papers at month end bother me, but not enough to hand that over to someone I don't know." (P005) |
| need | 15 | "My bookkeeper already collects everything once a month and I almost never look at receipts myself, so this solves a problem I mostly handed off already. I might let it run on the free 40, but I doubt I'd start paying for it." (P007) · "My rental shop doesn't have that many receipts. Staff send them to the group, I look at them, and my partner and I go through the month together. A duplicate means I talk to the person, and a bot can't do that for me. I'd try the 40 free ones out of curiosity, but I wouldn't pay $19 a month for something I can do in an evening with a spreadsheet." (P009) |
| price | 4 | "I'd probably throw the free 40 at it to see if it can read my staff's handwritten nota, but after that $19 a month for something I can do in Excel on a Sunday is one more subscription I'd cancel. My expenses aren't big enough to need a bot watching them." (P006) · "I'd probably throw my old chat in for the 40 free documents just to see, but $19 every month for something my Excel sheet and the bank screenshots already half do is hard for me to justify. My crews send maybe a few dozen receipts a week, so I'd blow past 100 and be looking at $45, and that's real money." (P017) |
| quality | 4 | "I'd burn the 40 free documents on my old chat archive just to see if it flags the re-photographed transfers, but I could wire up n8n plus ChatGPT to dump receipts into a Sheet in an afternoon. Unless the duplicate catching is clearly better than what I'd build, I'm not paying monthly for a receipt-to-table bot." (P012) · "I'd burn the 40 free ones, sure, but my guys' nota from the supply shop are scribbled in Indonesian half the time and smudged with cement. If I'm checking every row by hand anyway, I'm not paying $45 a month for the privilege." (P040) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 19 | "I'm abroad half the year and only notice a problem on the build once money has already gone, so a sheet that fills itself and a Monday report I can send my partner is worth $19 to me without much thought. I'd run the free 40 on the old chat archive first, and if it catches one duplicate or a padded nota, I'm paying." (P014) · "My admin is always weeks behind on the supply-shop nota and I lose track of what the guys actually spent on site. The free 40 docs costs me nothing to test on old chat history, and if it reads the handwritten nota properly, $45 a month is nothing next to one double-paid material run." (P015) |
| convenience | 2 | "I already scroll the site chats at night trying to work out where the materials money went, so if it just sits in the group and fills a sheet without my foremen doing anything, $45 a month is nothing next to one duplicated cement receipt. I'd run the free 40 on my real chat history first and only pay if the sheet actually matches what I know was spent." (P020) · "My admin is always a week behind on the receipt spreadsheet, and I'm reading the group chat at midnight trying to work out what got spent. If my guys just keep sending photos to the same chat and it lands in a sheet, $45 a month is nothing next to one double-paid supplier invoice." (P051) |

### What would flip a no

- Seeing it catch real duplicates or mistakes in our own old chat history with the free 40 documents, and showing me money we were actually losing.
- My bookkeeper telling me it pushes straight into Zoho or Jurnal and actually cuts the month-end chasing, ideally proven on the free 40 documents from our real chat history.
- Proof it will last and that I can leave cleanly: a real company I can name, other Bali businesses that have used it for a year, and an annual plan or guarantee. The duplicate detection on re-photographed receipts would also have to beat my own DIY version in the free trial.
- If the free trial showed it really nails the handwritten nota and catches duplicates my own bot would miss, and the price was closer to $5-10 a month for my volume.
- If it could work only from receipts I forward myself, with no access to the group chat and only to one sheet it creates, not my whole Google account. And if my accountant or another shop owner here told me they use it safely.
- If it caught a duplicate or padded nota in the free trial that actually saved me more than the monthly price, or if there was a cheap plan around $5-7 for a small café's volume.
- If my bookkeeper said it cuts her monthly fee or her hours, and she'd actually work from the Google Sheet instead of the chat.
- If my admin ran the free 40 on a real week of our chats and it saved her most of a day with almost no corrections, plus caught a duplicate payment we would have missed, I'd pay for it.
- If the free trial found real money in my old chat history, like duplicates or overcharges I'd missed that add up to more than a few months of the fee.
- If the free trial on my old chat history actually turned up a double-claim or an overpriced part my admin missed, I'd pay without thinking about it.
- A local accountant or another villa operator I know using it for a few months, plus clear proof that it only reads receipts and can only access the one sheet and folder it creates, not my whole Drive.
- The free trial on my real chat history catching duplicates I had missed, with a few false alarms at most.

Buyers say they would buy **1.0 times** in the first month on average.

100 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

Источники:
- ответы 100 смоделированных владельцев (`panel/answers`, кривая — в `pricing-curve.md`);
- цены конкурентов из `competitors.md`, проверены на страницах 11.11.2026;
- себестоимость документа $0,01–0,02 (ваш замер) и комиссия платёжки около 3% (Bank of Georgia, по вашему описанию).

Панель бухгалтеров сюда не входит: у бухгалтеров другой продукт и другой вопрос «кто платит».

Цены от смоделированных покупателей показывают, что стоит проверить. Это не доказательство.

### 1. Что сказали покупатели

| Кто | Ниже этой цены «слишком дёшево» | Цена, при которой «выгодно» и «дорого» говорят поровну (IPP) | Выше этой цены «слишком дорого» | Приемлемый диапазон |
|---|---:|---:|---:|---|
| Все 100 | $5,35 | $15,15 | $44,76 | $5–45 |
| 21 покупатель | $5,45 | **$19,17** | $79,36 | $5–79 |
| Стройка (30 человек) | $5,43 | **$18,95** | $59,88 | $5–60 |

Что значит каждая цена (медианы ответов):

| Кто | «Выгодно» | «Дороговато» | «Слишком дорого» |
|---|---:|---:|---:|
| Покупатели | $15 | $60 | $120 |
| Не покупатели | $9 | $25 | $45 |
| Стройка | $13,5 | $42 | $84,5 |
| Инвесторы | $15 | $45 | $90 |
| Виллы | $10 | $35 | $60 |
| Магазины и прокат байков | $10 | $25 | $45 |
| Кафе | $8 | **$19** | $35 |

Вывод:
- Для тех, кто реально покупает, и для стройки $19 стоит ровно в точке IPP. Это правильная цена входа.
- Для кафе $19 уже «дороговато». Это совпадает с 6% покупок в этом сегменте. Кафе не стоит делать целевым сегментом и не стоит снижать цену ради них.

### 2. Что берут конкуренты

| Альтернатива | Цена для бизнеса на 5 человек и ~100 документов в месяц |
|---|---|
| Zoho Expense | $0 до 3 пользователей, иначе $15–20 ($3–4 за человека) |
| KasKecil (только мелкая касса, без групп и дублей) | ≈$9 |
| Hubdoc | $12 |
| REME | $25–40 ($5–8 за человека) |
| Dext | $31,50 (250 документов) |
| Mekari Expense | от ≈$90 (минимум 50 сотрудников) |

Медиана рынка — $12–17. Nota за $19 стоит чуть выше. Отличие в том, что Nota берёт деньги за документы, а не за людей: при 10 сотрудниках REME обойдётся в $50–80, Zoho в $30–40, а Nota останется на $19–45.

### 3. Маржа на подписку

Расчёт при полном использовании лимита, без хостинга и поддержки.

| Тариф | Цена | ИИ ($0,01–0,02 за документ) | Комиссия ~3% | Остаётся | Маржа |
|---|---:|---:|---:|---:|---:|
| Start, 100 документов | $19 | $1–2 | $0,57 | $16,4–17,4 | 86–92% |
| Business, 300 документов | $45 | $3–6 | $1,35 | $37,6–40,6 | 84–90% |
| Developer, 1000 документов | $119 | $10–20 | $3,57 | $95,4–105,4 | 80–89% |

Точные дубли проверяются по хэшу и почти ничего не стоят, поэтому реальная маржа будет выше. Постоянные расходы (хостинг, разработчик, поддержка) пока неизвестны, точку безубыточности посчитает `/founder-cfo`.

### 4. Решение

**Цена входа — $19 в месяц за 100 документов, не менять.**
- Для покупателей и стройки это точка IPP.
- Она внутри приемлемого диапазона для всех сегментов.
- Маржа 86–92%.
- Снижать цену ради кафе и тех, кто экономит, не нужно: им мешает не цена, а то, что они не видят ценности.

**Лестница тарифов:**

| Тариф | Цена | Цена документа | Для кого | Зачем переходить на него |
|---|---:|---:|---|---|
| Start | $19 | $0,19 | 1 объект или точка, до ~100 чеков | — |
| Business | $45 | $0,15 | 2–5 объектов или вилл, бригады | Документы дешевле на 21%, все 5 групп заняты делом |
| Developer | $119 | $0,12 | Девелопер или УК с большим потоком | **Выше «слишком дорого» даже у покупателей ($79)**. Продавать только через разговор, а не на сайте. Проверить $79–99 |
| Годовая оплата | −20% | | | Есть в описании, оставить |
| Доп. пакет +50 документов | $9 | $0,18 | Разовый всплеск | Дешевле, чем перейти на тариф выше |

Тариф Business ($45) укладывается в диапазон покупателей и стройки, хотя стройка начинает считать дорогим уже $42. Цену оставить, но в описании тарифа говорить на языке объектов: «до 5 объектов», а не «300 документов».

### 5. Стартовое предложение

Без скидок, которые приучают ждать распродажу:
- **Бонус до 31 января 2027:** аудит архива чата на 100 документов вместо 20. Это прямо отвечает на главный запрос панели «найдите деньги в нашем старом чате».
- **Фиксация цены на 12 месяцев для первых 50 платящих клиентов.** Это не скидка, а защита от будущего подорожания. Обещать её можно, только если вы готовы её выполнить.
- Зачёркнутых «было $X» не использовать: таких цен никогда не было.

### 6. Что проверить на живых людях

**Две цены входа: $19 и $29** за 100 документов. Обе внутри диапазона. $29 ниже, чем «дороговато» у покупателей ($60) и у стройки ($42).

Как проверить:
1. Ваши 10 тёплых контактов. Половине показать $19, половине $29, с реальной кнопкой оплаты после 40 бесплатных документов. Считать, кто оплатил.
2. Две версии лендинга или две ссылки на бота с метками, по 2 недели на каждую. Сравнить переход из пробного периода в оплату. Цель из описания — от 10%.

Отдельно спросить 2–3 крупных клиентов про Developer: $79, $99 или $119.

### 7. Что покупатели говорят о цене

1. «Попробую бесплатные 40, чтобы посмотреть, прочитает ли он рукописные накладные моих сотрудников. Но потом $19 в месяц за то, что я могу сделать в Excel в воскресенье, — ещё одна подписка, которую я отменю.» (P006, кафе)
2. «Мои бригады присылают пару десятков чеков в неделю, так что я вылечу за 100 и окажусь на $45, а это уже реальные деньги.» (P017, стройка)
3. «Админ и так вносит чеки в Excel каждую неделю. С опозданием, но вносит. Платить каждый месяц и переезжать в Google Sheets ради того, что и так примерно работает, я не буду.» (P001, кафе)

Ответ маркетинга на все три — не скидка, а деньги, найденные в архиве: «один пойманный дубль окупает год подписки».

## The offer

Метод: Offers lens из `board/lenses.md`. Это пересказ опубликованной методики, а не слова её автора.

Источники:
- панель на 100 владельцев (`panel/results.md`);
- цены (`pricing.md`);
- жалобы на конкурентов (`competitors.md`);
- условия совета директоров (`board.md`).

Файла `numbers.json` пока нет, поэтому стоимость бонусов посчитана вручную: $0,01–0,02 за документ, комиссия около 3%.

### 1. Что мешает владельцу получить результат

Формулировки взяты из ответов панели.

**До покупки**
1. «Админ и так вносит чеки в Excel» (привычка, 33 из 100).
2. «Незнакомый бот в рабочем чате и в моём Google» (недоверие, 23).
3. «Это просто бот "чек в таблицу"? Правда найдёт дубль?»
4. «Перечитает ли он рукописные и выцветшие накладные на бахаса?»
5. «$19 каждый месяц — ещё одна подписка»
6. «Есть бесплатные варианты: Zoho, KasKecil, Excel, бот, который я соберу сам»
7. «Кто за этим стоит и будет ли продукт через год?»
8. «Дубль — это проблема людей, а не софта»
9. «Добавить бота в группу с прорабом — значит показать, что я ему не доверяю»

**В первые дни**
10. «Не хочу настраивать и разбираться»
11. «Сотрудники не будут ничего менять»
12. «40 документов кончатся раньше, чем я увижу пользу»
13. «Если ошибётся, проверять каждую строку придётся мне»
14. «С бумагой работает бухгалтер, Google-таблица ему не нужна»

**Потом**
15. «Через две недели все вернутся к старому, а я буду платить»
16. «Перерасту 100 документов, и выйдет $45»
17. «Сложно отменить, как у Expensify и Dext» (жалоба на конкурентов)
18. «Мои данные останутся у вас»
19. «Главные потери — наличные механикам без чека и завышенные цены на настоящем чеке. Их поиск дублей не ловит»
20. «Половина чеков вообще не доходит до чата»

### 2. Решения: ценность и стоимость

Ценность и затраты на доставку оценены по шкале от 1 до 5.

| # | Решение | Отвечает на | Ценность | Затраты | Берём? |
|---|---|---|---:|---:|---|
| A | **Бесплатная проверка архива чата**: отчёт «что нашли» по 100 старым документам (до 31.01.2027) | 1, 3, 6, 8, 12 | 5 | 1 ($1–2 на человека) | Да, это ядро входа |
| B | Режим «только пересылаю сам», без добавления бота в группы | 2, 9 | 4 | 1 (уже есть) | Да, называть прямо |
| C | Абзац о данных: файлы в вашем Drive, у нас только зашифрованные отпечатки, удаление одной командой | 2, 18 | 4 | 1 (уже есть) | Да |
| D | Имя команды: Axiom Consulting, финансисты на Бали, 15 лет | 7 | 3 | 1 | Да |
| E | 15-минутный звонок с настройкой для первых 50 клиентов | 7, 10 | 4 | 2 (≈12 часов команды) | Да, ограничение настоящее |
| F | Возврат $19 за первый оплаченный месяц без вопросов, отмена одной командой | 5, 15, 17 | 4 | 2 (см. ниже) | Да |
| G | Фиксация цены на 12 месяцев для первых 50 платящих | 5, 16 | 2 | 1 | Да |
| H | Доступ бухгалтеру к таблице (обычное «Поделиться» в Google) | 14 | 3 | 1 | Да, упоминать |
| I | Доступ только к своей таблице и папке (Google drive.file) | 2 | 5 | 3 (ещё не сделано, нужна верификация OAuth) | **Сделать до запуска, потом добавить в питч** |
| J | Выгрузка в Jurnal или Zoho | 14 | 4 | 4 | Позже, по спросу |
| K | Учёт наличных голосом или текстом | 19 | 3 | 3 | **Нет**: противоречит принципу «только документы» |
| L | Сравнение цены с прошлыми покупками той же позиции | 19 | 4 | 3 | Позже. Это ответ на «завышенную цену», кандидат в roadmap |
| M | Напоминание о платеже без чека (кнопка «попроси чек») | 20 | 3 | 2 | Есть в плане вирусности, этап 3 |

### 3. Итоговое предложение

**Название: «Проверка чата» → Nota Start.**

- **Ядро.** Каждый чек из рабочих чатов попадает в вашу таблицу. Каждый документ проверяется на дубль и на расхождение позиций с итогом. Каждый понедельник приходит отчёт.
- **Бонус 1 — проверка архива (A).** До 100 старых документов бесплатно до 31.01.2027, сразу с отчётом «что нашли». Снимает «а точно найдёт?» и «у меня админ».
- **Бонус 2 — без группы (B + C).** Можно только пересылать самому. Файлы остаются в вашем Drive, всё удаляется одной командой. Снимает недоверие.
- **Бонус 3 — настройка с командой Axiom (D + E).** 15 минут, только для первых 50 клиентов. Снимает «кто за этим стоит».
- **Гарантия (F).** Если первый оплаченный месяц не стоил своих денег, вернём $19 без вопросов. Отмена одной командой.
- **Срочность, только настоящая.** Бонус архива действует до 31.01.2027. Звонок и фиксация цены — для первых 50 клиентов.
- **Цена:** $19 / $45 / $119 (см. `pricing.md`) плюс 40 бесплатных документов.

#### Сколько стоит

| Элемент | Расчёт | На одного пробного или платящего клиента |
|---|---|---|
| Проверка архива на 100 документов | 100 × $0,01–0,02 | $1–2 на каждого, кто попробовал, в том числе на тех, кто не заплатит |
| Звонок | 15 мин × 50 | ≈12,5 часа команды на весь запуск |
| Возврат $19 | Доля возвратов неизвестна. Пример: при 20% | ≈$3,8 на нового платящего, один раз |
| Фиксация цены | Недополученный рост цены, если цена вырастет | 0, пока цена не меняется |

При марже 86–92% на тарифе за $19 гарантия и бонусы доступны. Реальную долю возвратов и конверсию нужно замерить на первых клиентах, `/founder-cfo` сведёт это с постоянными расходами.

Юридически гарантия и бонусы должны быть описаны в пользовательском соглашении по праву Грузии. Платёжный провайдер должен поддерживать возвраты. Это не юридическая консультация.

### 4. Уравнение ценности

Оценки от 1 до 10. Для «Времени» и «Усилий» выше значит быстрее и легче.

| Множитель | Было | Стало | Что сдвинуло |
|---|---:|---:|---|
| Желанный результат | 6 | 7 | Обещание звучит как деньги («что нашли»), а не как документы |
| Вероятность получить результат | 4 | 6 | Проверка архива показывает результат на своих данных, имя команды, гарантия |
| Время до результата | 6 | 8 | Отчёт по архиву в первый день, а не после первого дубля через недели |
| Усилия | 8 | 8 | И так почти нулевые. Режим «только пересылаю» убирает шаг с группой |

### 5. Повторная проверка

Те же 20 покупателей, что и в первой панели (P001–P020), получили новый питч. Ответы лежат в `panel-offer/`.

| | Было (питч v1) | Стало (предложение) |
|---|---:|---:|
| Покупают | 4 из 20 | **5 из 20** |
| Привычка | 5 | 5 |
| Недоверие | 4 | 3 |
| Нет потребности | 4 | 3 |
| Цена | 2 | 3 |
| Качество | 1 | 1 |

Кто изменил решение:
- **P003, владелец магазина за границей: недоверие → покупает.** Сработали команда Axiom и файлы в собственном Drive.
- **P010, прокат байков, уже обманывали: «не нужно» → покупает.** Сработала бесплатная проверка архива и то, что $19 копейки против одного пойманного ремонта.
- **P014, инвестор: покупал → не покупает.** «Добавить бота в группу с прорабом — показать недоверие», плюс «у меня Excel». Это шум выборки и новое возражение (пункт 9).

**Вывод честный: предложение почти ничего не сдвинуло.** 4 → 5 из 20 — это в пределах шума. Почти все отказавшиеся отвечают одно и то же: «если бесплатная проверка найдёт реальные деньги — заплачу». Значит, результат решает не упаковка, а то, **что именно найдёт проверка архива на настоящем чате**. Оставшиеся барьеры не про оффер:
- **Привычка (админ с Excel)** — это рынок, а не упаковка. Её снимает только найденная сумма.
- **Недоверие.** Загрузка экспорта чата его даже усиливает. Нужен доступ только к своим файлам (I) и рекомендации знакомых.
- **Наличные и завышенные цены.** Этого продукт сейчас не ловит, нужна функция сравнения цен (L).

### Что делать дальше

1. До запуска довести проверку архива до отчёта, который сам по себе продаёт: сумма найденных дублей и расхождений, топ-3 примера со ссылками на документы.
2. Сделать доступ drive.file и верификацию OAuth, после этого добавить в питч «бот видит только свою таблицу».
3. Прогнать проверку архива на 5–10 настоящих чатах знакомых. Это даст первую реальную цифру «нашли на X» и кейс для маркетинга.
4. Добавить «сравнение цены с прошлыми покупками» в roadmap как ответ на завышенные чеки.

## The numbers

> Как читать таблицы ниже: единица — один платящий клиент на один месяц. Инструмент пишет «в день», но в файле `days_per_month = 1`, поэтому «в день» везде означает «в месяц». Все входные данные и пометки «оценка» — в `cfo-sources.md`. Это не финансовая, налоговая или юридическая консультация: структуру ИП в Грузии, налоги и договоры должен проверить бухгалтер, прежде чем пойдут деньги.

### Записка CFO

**Маржа.**
- Без затрат на привлечение один платящий клиент приносит $26,85 из $30, это ~89%.
- С привлечением, если разложить его на 12 месяцев жизни клиента, остаётся **$16,77 (56%)**.
- Постоянные расходы — $740 в месяц: разработчик, хостинг, сервер. Ваше время сюда не входит.
- **Точка безубыточности — 45 платящих клиентов.** При цели 1000 клиентов маржа 53%, по расчёту инструмента операционная прибыль за год составит $93 тыс.

**Но эти $93 тыс. — бумажная прибыль. Деньги на привлечение уходят сразу, а не по частям за 12 месяцев.** Я пересчитал движение денег отдельно, с оплатой рекламы в момент установки и оттоком 5% в месяц (оценка):

| Сценарий | Сколько денег нужно вложить до выхода в плюс | Итог года по деньгам | Потрачено на рекламу и пробные |
|---|---:|---:|---:|
| Цель: 1000 к 12-му месяцу | **≈$27 тыс.** (дно на 6-м месяце) | +$3 тыс. | ≈$152 тыс. |
| Половина цели (500) | ≈$16 тыс. | −$3 тыс. | ≈$76 тыс. |
| 30% цели (300) | ≈$12 тыс. | −$5 тыс. | ≈$46 тыс. |

**Что двигает результат сильнее всего — конверсия из установки в оплату.** Она пока не измерена, 10% — это ориентир из вашего описания.

| Конверсия | Стоимость платящего клиента | Цель 1000: нужно денег / итог года | 30% цели: нужно / итог |
|---|---:|---:|---:|
| 5% | $242 | −$149 тыс. / −$149 тыс. | −$51 тыс. / −$51 тыс. |
| **10%** | **$121** | −$27 тыс. / +$3 тыс. | −$12 тыс. / −$5 тыс. |
| 20% | $60 | −$5 тыс. / +$79 тыс. | −$3 тыс. / +$17 тыс. |

Вторая по силе переменная — средний чек. Если все клиенты сидят на $19, а не в среднем на $30, то при конверсии 10% цель 1000 даёт **−$57 тыс.** за год. Тариф Business ($45) нужен не для красоты: на нём держится экономика.

**Сколько нужно денег.**
- Чтобы покрыть постоянные расходы, денег почти не нужно: разработчик и сервер окупаются уже при 45 клиентах.
- На рост до 1000 клиентов через платную рекламу при $10 за установку нужно **$25–30 тыс. оборотных денег** за первые полгода. Это при условии, что конверсия будет 10%.
- Если конверсия окажется 5%, расти через рекламу нельзя: каждый клиент окупается дольше, чем живёт.

**Три способа улучшить экономику.** Цифры из расчётов выше.
1. **Поднять конверсию с 10% до 20%.** Отчёт по архиву, который сразу показывает найденные деньги, и ответ на недоверие (доступ только к своей таблице). Стоимость клиента падает со $121 до $60, нужда в деньгах — с $27 тыс. до $5 тыс., итог года вырастает с +$3 тыс. до +$79 тыс.
2. **Держать средний чек около $30, то есть продавать Business ($45) строительству и управляющим компаниям с несколькими объектами.** Если чек упадёт до $19, итог года уйдёт с +$3 тыс. до −$57 тыс.
3. **Сократить платную часть привлечения.** Каждый клиент от рекомендации, бухгалтера или из группы, где уже стоит Nota, стоит около $2 (только пробный ИИ) вместо $121. Даже 30% таких клиентов срезают расходы на рекламу примерно на треть: с ≈$152 тыс. до ≈$106 тыс. в сценарии цели. Это прикидка, а не прогон инструмента. Снижение цены не помогает: при $22 вклад клиента падает с $16,77 до $8,77, а точка безубыточности растёт с 45 до 85 клиентов.

**Условия совета по деньгам.**
- [x] Себестоимость документа посчитана: $0,01–0,02.
- [x] Маржа положительная: ~89% без привлечения, 56% с ним.
- [x] Есть лестница тарифов.
- [x] Гарантия по карману (см. `offer.md`).
- [x] Цель по выручке выбрана.
- [ ] Не измерены конверсия, отток и реальная стоимость клиента. **От конверсии зависит, нужны ли вам $5 тыс. или $150 тыс.** Поэтому совет и требовал 20–30 платящих из личной сети и замер конверсии до трат на рекламу.

**Вывод.** Продукт дешёвый в обслуживании и выходит в плюс при 45 клиентах. Опасна не себестоимость, а покупка роста рекламой до замера конверсии. Первые 50–100 клиентов стоит набрать через личную сеть и рекомендации, измерить конверсию и отток, и только потом включать рекламу. Тогда станет понятно, во что обойдётся платный рост: в $5 тыс. или в $150 тыс.

---

## Unit economics: Nota (@NotaGetBot), Telegram bot for expense control

Every number below comes from the input file. Nothing is looked up or guessed.

### One paying client-month (one active subscription for one month)

| line | per paying client-month (one active subscription for one month) |
| --- | ---: |
| Price | $30.00 |
| AI recognition, ~150 docs per client-month at $0.015 (estimate) | -$2.25 |
| Payment processing ~3% of $30 (Bank of Georgia estimate) | -$0.90 |
| Acquisition: $10 per install / 10% install-to-paid = $100 per paying client, spread over an assumed 12-month lifetime (estimate) | -$8.33 |
| Free trial AI: up to 140 docs per install x $0.015 = $2.10, / 10% conversion, over 12 months (estimate) | -$1.75 |
| **Contribution** (what each paying client-month (one active subscription for one month) leaves to pay the fixed costs) | **$16.77** (56%) |

### The margin that matters

Fixed costs: $740 a month (Developer (support included), midpoint of $500-700 $600, Hosting $100, Server, midpoint of $30-50 $40).

- **Break-even: 45 paying client-month (one active subscription for one month)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (1,000 a day): **53%** of every sale, after every cost.
- Capacity: 100000 a day.

### Year 1, month by month

| month | paying client-month (one active subscription for one month)s a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 50 | $1,500 | $98 | $98 |
| 2 | 100 | $3,000 | $937 | $1,036 |
| 3 | 190 | $5,700 | $2,446 | $3,482 |
| 4 | 280 | $8,400 | $3,956 | $7,437 |
| 5 | 370 | $11,100 | $5,465 | $12,902 |
| 6 | 460 | $13,800 | $6,974 | $19,876 |
| 7 | 550 | $16,500 | $8,484 | $28,360 |
| 8 | 640 | $19,200 | $9,993 | $38,353 |
| 9 | 730 | $21,900 | $11,502 | $49,855 |
| 10 | 820 | $24,600 | $13,011 | $62,866 |
| 11 | 910 | $27,300 | $14,521 | $77,387 |
| 12 | 1,000 | $30,000 | $16,030 | $93,417 |

- **Year 1 operating profit: $93,417** on $183,000 of revenue.
- After the $0 startup spend: $93,417.
- Startup money earned back: month 1.
- Cash you need before it pays for itself: **$0**.

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 53% | 45 | $93,417 |
| Price -10% | 48% | 54 | $75,117 |
| Volume -20% | 53% | 45 | $72,958 |
| Unit costs +15% | 47% | 51 | $81,312 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.

## Marketing

Источники:
- панель на 100 владельцев (`panel/results.md`) и повторная проверка предложения (`panel-offer/`);
- конкуренты (`competitors.md`);
- предложение и цены (`offer.md`, `pricing.md`);
- деньги (`cfo.md`).

Цитаты панели в этом документе — исследование. В рекламе их нельзя выдавать за слова клиентов.

### 1. Позиционирование

**Первая аудитория** по данным панели:
- **стройка и ремонт** — покупают 33%;
- **владельцы, которых уже обманывали** — 50%;
- **те, у кого всё в чатах** — 41%;
- **админ с Excel** — 33%.

Владельцы с доходом от $124 тыс. в год покупают 29%, до $77 тыс. — 9%.

Кафе, люди с приложением, экономные, осторожные с данными и любители собрать бота сами покупают 0–6%. На них маркетинг не тратим.

Три варианта:

1. **«Для владельцев стройки и вилл на Бали, у которых чеки тонут в Telegram-чатах, Nota — контроль платежей прямо в рабочем чате: ловит дубли и несходящиеся суммы до оплаты. В отличие от Zoho и Expensify, сотрудникам ничего не нужно ставить.»**
2. «Для владельцев, которые управляют бизнесом на Бали на расстоянии, Nota — финансист в рабочем чате: каждый чек записан в вашу таблицу, каждый понедельник отчёт, дубли видны сразу. В отличие от админа с Excel, без опозданий.»
3. «Для тех, кого уже обманывали повторным или завышенным чеком, Nota — проверка каждого чека из рабочих чатов: тот же чек, переснятый или присланный другим, будет найден. В отличие от бота "чек в таблицу", она сверяет, а не только записывает.»

**Рекомендую первый вариант.** Он называет сегмент с самой высокой долей покупок (стройка) и самый частый канал боли (чаты). Плюс он отвечает на главное отличие от конкурентов, которое подтверждает разбор: «сотрудникам ничего не ставить». Вариант 3 оставляем для рекламных заходов: он самый сильный по доле покупок, но узкий.

Короткая формула для всего: **«Чеки из рабочих чатов — в вашу таблицу, дубли — до оплаты».**

### 2. Каналы

Выбрали три. Все дешёвые: CFO прямо советует не покупать рост, пока не измерена конверсия.

| Канал | Почему подходит | Затраты | Как поймём, что работает |
|---|---|---|---|
| **1. Личная сеть + клиенты Axiom + 10 тёплых контактов** | Недоверие — вторая причина отказа, и знакомый человек снимает её лучше всего. В панели «рекомендация знакомого владельца или бухгалтера» — одно из главных условий | $0, время основателя | Из 10 контактов ≥5 запустили проверку архива, ≥3 оплатили к L+16 |
| **2. Проверка архива как повод для разговора** (в личке, в бизнес-чатах Бали, на встречах) | Почти все отказавшиеся сказали: «найдите деньги в нашем старом чате — заплачу» | ИИ: $1–2 на проверку | ≥30% проверок нашли хотя бы один дубль или расхождение. Конверсия из проверки в оплату ≥15% |
| **3. Партнёры: УК вилл, регистраторы компаний, подрядчики** | Через них приходят строители и виллы. Бухгалтеры пока не покупатели (5% в панели), но могут рекомендовать | $0 на старте. Вознаграждение позже (партнёрская программа есть в описании) | ≥3 партнёра прислали ≥1 клиента к L+16 |
| Поддержка: автопостинг в свой Telegram-канал и Threads | Вы это уже планируете. Дешёвый фон, контент из жизни продукта | Время, без бюджета | Переходы по метке в боте |

**Чего не делаем в эти 30 дней:**
- **Платная реклама за установки ($10 за штуку).** Пока не измерена конверсия, это может стоить от $5 тыс. до $150 тыс. (`cfo.md`). Включаем после первых 30–50 платящих, тестом на $300–500.
- **Кафе и рестораны.** 6% покупок, для них $19 уже «дороговато».
- **Бухгалтеры как покупатели.** Нужны выгрузка в Jurnal, тариф на много клиентов и WhatsApp (`panel-accountants/results.md`).
- **Product Hunt и каталоги** — после 10–20 живых клиентов с настоящими отзывами (описание продукта).

### 3. Десять заходов

Каждый отвечает на одно возражение панели или использует причину покупки.

| # | Заход | Формат | На что отвечает |
|---|---|---|---|
| 1 | «Пришлите выгрузку рабочего чата — покажем, сколько чеков у вас уже оплачено дважды» | Первая строка поста, личное сообщение | «а точно найдёт дубль?» |
| 2 | «Ваш админ вносит чеки в Excel. Nota делает то же за минуту и ещё сверяет, не было ли этого чека раньше» | Заголовок | «админ и так делает» |
| 3 | «Тот же чек, переснятый другим сотрудником, — это не новый расход» | 3 секунды видео: два фото одного чека рядом | «бот просто переписывает в таблицу» |
| 4 | «Сотрудникам ничего не ставить: чеки идут в тот же чат, что и раньше» | Подпись к скриншоту чата с ✍ | «сотрудники не будут менять привычки» |
| 5 | «Не хотите бота в группе? Пересылайте ему сами» | Строка в посте | «не пущу бота в рабочий чат» |
| 6 | «Файлы остаются в вашем Google Drive. У нас — только отпечатки для поиска дублей. Удаление одной командой» | Карточка «о данных» | «боюсь за данные» |
| 7 | «Рукописная накладная из магазина стройматериалов, мятая и на бахаса — в таблице через минуту» | Видео: фото накладной → строка в таблице | «не прочитает рукописное» |
| 8 | «Каждый понедельник — отчёт за неделю, который не стыдно переслать партнёру» | Изображение карточки отчёта на выдуманных данных | Причина покупки: управление на расстоянии |
| 9 | «Первый месяц не окупился — вернём $19 без вопросов» | Строка под ценой | «ещё одна подписка» |
| 10 | «Делают финансисты Axiom Consulting, 15 лет контроля расходов на стройках» | Подпись, «о нас» | «кто за этим стоит, проживёт ли год» |

Нельзя: выдуманные отзывы, «тысячи клиентов», чужие логотипы, суммы «нашли $X» до того, как они реально найдены у клиента. Публиковать цифру «нашли на X» можно только с согласия клиента и без его данных.

### 4. Кампания на 30 дней

**Рабочая дата запуска L — понедельник 7 декабря 2026.** Её стоит передвинуть, если к этому сроку не готовы приём платежей, верификация Google OAuth и отчёт по проверке архива. Это блокеры из описания продукта и `offer.md`.

| Дата | День | Канал | Что делаем и о чём говорим |
|---|---|---|---|
| 23.11 | L−14 | Внутри | Список 10 тёплых контактов + 10 клиентов Axiom со стройкой и виллами. Метка источника в ссылке на бота у каждого |
| 24.11 | L−13 | Продукт | Отчёт проверки архива: сумма найденного, топ-3 примера со ссылками. Демо-картинки на выдуманных данных |
| 25.11 | L−12 | Личка | Первым 5 контактам: «Хочу проверить Nota на настоящем чате. Пришлёте выгрузку рабочей группы? Покажу, что найдёт, бесплатно» (заход 1) |
| 26.11 | L−11 | Личка | Ещё 5 контактам, то же |
| 27.11 | L−10 | Канал/Threads | Пост «как выглядит дубль»: два фото одного чека, переснятого разными людьми (заход 3) |
| 28.11 | L−9 | Продукт | Прогон первых архивов. Записать: сколько документов, сколько дублей и расхождений, на какую сумму |
| 29.11 | L−8 | Личка | Результаты проверок владельцам лично, созвон 15 минут с каждым, у кого что-то нашлось |
| 30.11 | L−7 | Партнёры | 5 УК вилл и 3 регистраторам компаний: короткое письмо + предложение бесплатной проверки для их клиентов |
| 01.12 | L−6 | Канал/Threads | «Рукописная накладная → строка в таблице» (заход 7) |
| 02.12 | L−5 | Продукт | Сквозной тест бота (ТЗ уже есть). Проверка оплаты и возврата |
| 03.12 | L−4 | Канал/Threads | Карточка «о данных» (заход 6) |
| 04.12 | L−3 | Личка | Тем, кому проверка что-то нашла: приглашение на тариф с фиксацией цены (первые 50) |
| 05.12 | L−2 | Канал/Threads | Закулисье: «как мы 15 лет ловили дубли вручную и почему сделали бота» (заход 10) |
| 06.12 | L−1 | Внутри | Проверить метки источников, ответы поддержки, текст гарантии в соглашении |
| **07.12** | **L** | Все | Запуск: «Бесплатная проверка рабочего чата до 31 января» (заход 1). Пост в канале, Threads, личные сообщения всей сети. Профиль бота обновлён (этап 0 плана вирусности) |
| 08.12 | L+1 | Бизнес-чаты Бали | Пост о проверке архива в 2–3 тематических чатах, где это разрешено правилами |
| 09.12 | L+2 | Канал/Threads | «Сотрудникам ничего не ставить» (заход 4) |
| 10.12 | L+3 | Партнёры | Повторное касание УК и регистраторов с первыми результатами (без данных клиентов) |
| 11.12 | L+4 | Канал/Threads | «Не хотите бота в группе — пересылайте сами» (заход 5) |
| 12.12 | L+5 | Продукт | Разбор: где люди бросают онбординг (`/start` → Google → группа) |
| 13.12 | L+6 | Канал/Threads | Карточка недельного отчёта на выдуманных данных (заход 8) |
| 14.12 | L+7 | Внутри | **Неделя 1: три цифры** (см. ниже). Решение по тесту рекламы |
| 15.12 | L+8 | Канал/Threads | «Админ и Excel против Nota» (заход 2) |
| 16.12 | L+9 | Личка | Тем, кто прошёл пробный период и не заплатил: один вопрос «что помешало?» |
| 17.12 | L+10 | Канал/Threads | Цена и гарантия (заход 9) |
| 18.12 | L+11 | Партнёры | Первым партнёрам, приславшим клиента: благодарность. Разговор о партнёрской программе |
| 19.12 | L+12 | Канал/Threads | Если клиент согласен: обезличенный кейс «проверка нашла N дублей на сумму X» |
| 20.12 | L+13 | Продукт | Просьба о рекомендации владельцам после первого пойманного дубля (этап 2 плана вирусности) |
| 21.12 | L+14 | Внутри | **Неделя 2: три цифры.** Если конверсия ≥10% — тест рекламы $300–500 в Telegram-каналах Бали |
| 22.12 | L+15 | Канал/Threads | Закулисье: что поменяли по отзывам первых клиентов |
| 23.12 | L+16 | Внутри | Итог 30 дней: клиенты, конверсия, источники. Решение, что делать дальше |

**Когда нечего сказать нового:** закулисье разработки, как бот читает трудный документ, разбор одного трудного чека (на выдуманных данных), вопросы клиентов и ответы на них, правила работы бота в группе.

**Стартовое предложение** (из `pricing.md` и `offer.md`): проверка архива на 100 документов до **31.01.2027**, фиксация цены и звонок с командой для **первых 50 платящих**, возврат $19 за первый месяц. Дата окончания называется в каждом посте с предложением, без счётчиков и «осталось 3 места».

### 5. Бюджет и цифры

**Бюджет на 30 дней: $0–500.**
- $0 до L+14: личная сеть, партнёры, проверка архива. ИИ на проверки — около $1–2 за штуку, примерно $50–100.
- $300–500 на тест рекламы в Telegram-каналах Бали, **только если к L+14 конверсия из установки в оплату ≥10%.**

**Сколько можно платить за клиента.** Клиент приносит $26,85 в месяц после ИИ и комиссии (`cfo.md`). Панель: в среднем 1,0 покупка в первый месяц. При окупаемости за 4 месяца предел — **$26,85 × 4 ≈ $107 за платящего клиента.** Сейчас при $10 за установку и конверсии 10% клиент стоит $121, это выше предела. Значит, реклама оправдана при конверсии **≥12%** или установке **≤$9**.

**Три цифры каждую неделю:**

| Цифра | Ориентир | Если ниже — что менять |
|---|---|---|
| Проверки архива, которые что-то нашли | ≥30% | Если почти ничего не находят, проблема в рынке или продукте, а не в рекламе. Разобрать с командой |
| Установка → оплата | ≥10% (цель 20%) | Где бросают онбординг. Текст про доступ к Google. Отчёт по проверке |
| Доля клиентов от рекомендаций и партнёров | ≥30% | Включить просьбу о рекомендации и кнопку «Поделиться отчётом» (план вирусности) |

Реклама в Индонезии должна соответствовать местным правилам о заявлениях. Заявления о найденных суммах и экономии допустимы только подтверждённые. Это не юридическая консультация.

## Brand

Основа:
- позиционирование из `marketing.md`: «Для владельцев стройки и вилл на Бали, у которых чеки тонут в Telegram-чатах, Nota — контроль платежей прямо в рабочем чате…»;
- причины покупки из панели: «уже обманывали», «управляю на расстоянии», «админ всегда опаздывает»;
- конкуренты из `competitors.md`.

Это не юридическая консультация по товарным знакам.

### 1. Название

**Название Nota остаётся.** Бот @NotaGetBot уже работает, логотип и эскизы есть в ваших артефактах, тексты описания написаны. Поэтому десять новых вариантов я не придумывал. Ниже — что даёт имя и где его риски.

| | |
|---|---|
| Что говорит | По-индонезийски *nota* — чек или товарная накладная. Так подписан почти каждый чек из магазина стройматериалов на Бали («NOTA PENJUALAN TUNAI»). Для местных сотрудников и владельцев, которые давно на Бали, имя объясняет само себя. Латинское *nota* значит «заметка, отметка» и тоже подходит. |
| Звучание | Два слога, одинаково читается на русском, английском и индонезийском |
| На иконке 32 px | Одна буква N читается. Короткое слово помещается под иконкой целиком |
| **Риск 1: описательность в Индонезии** | Раз «nota» — обычное слово для чека, зарегистрировать его как знак в Индонезии для чеков и учёта может быть трудно или невозможно без отличительного элемента: логотипа или пары «Nota by Axiom». Это решает патентный поверенный |
| **Риск 2: похожие названия** | В софте есть другие продукты с близкими именами, например сервис транскрибации Notta. Это другая категория, но тот же класс софта. Проверить при поиске знаков |
| Риск 3: поиск | «nota» в индонезийском поиске выдаёт миллионы обычных чеков. Ищут по @NotaGetBot и по связке «Nota бот чеки» |

**Предложение:** использовать пару **«Nota by Axiom»** там, где важна регистрация и доверие (соглашение, сайт, заявка на знак). Это и отличительный элемент, и ответ на возражение «кто за этим стоит». В боте и в разговоре оставить просто Nota.

#### Проверки, которые нужно сделать вам

Я могу запускать только публичные поиски. Окончательно подтверждает патентный поверенный, и знак ничей, пока вы его не зарегистрируете.

**Товарные знаки, классы МКТУ:**
- **9** — программное обеспечение;
- **42** — SaaS;
- **35** — бухгалтерский учёт и управление бизнесом;
- **36** — финансовые услуги, если позиционироваться как финансовый контроль.

Где искать:
- Индонезия, DJKI / PDKI: https://pdki-indonesia.dgip.go.id
- Грузия, Sakpatenti (ваш ИП зарегистрирован там): https://www.sakpatenti.gov.ge
- Международная база WIPO Global Brand Database: https://branddb.wipo.int
- Если пойдёте в Узбекистан и Казахстан: местные патентные ведомства, либо подача через Мадридскую систему WIPO из Грузии.

**Домены.** Из этой сессии DNS не отвечает ни на один адрес, поэтому свободные домены проверить не удалось. Проверьте у регистратора:
- getnota.com, nota.app, nota.id, usenota.com;
- nota.axiomco.io (поддомен на вашем домене — бесплатно и сразу; домен axiomco.io указан в настройках сайта как неподтверждённый).

**Аккаунты:** Telegram-канал (@nota…), Threads и Instagram (у вас запланирован автопостинг в Threads), YouTube для коротких видео.

**Путаница с конкурентами из `competitors.md`:** REME, Dext, Zoho, Expensify, Hubdoc, Veryfi, KasKecil, Mekari. Ни одно из этих имён не похоже на Nota.

### 2. Обещание и голос

**Обещание, одной строкой:** *Каждый чек из рабочих чатов — в вашей таблице, проверен на дубль до оплаты.*

**Слоган, три варианта:**
1. **«Не бухгалтерия. Контроль.»** Уже есть на сайте Axiom и в описании. Рекомендую оставить: коротко и сразу отделяет от бухгалтерских приложений.
2. «Чеки из чата — в таблицу. Дубли — до оплаты.»
3. «Один чек — одна оплата.»

**Голос в трёх словах:**

| Качество | Как делать | Как не делать |
|---|---|---|
| **Спокойный, как финансист** | «Этот чек уже записан 3 ноября под №14» | «Внимание! Обнаружено мошенничество!» |
| **Конкретный** | Числа, даты, номера строк, ссылка на оригинал | «Мы революционно меняем учёт» |
| **Никого не обвиняет** | О дублях — только владельцу в личку, без имён в общем чате | «Сотрудник Х пытался получить деньги дважды» в группе |

Эти правила совпадают с принципами в вашем описании продукта: «никого не обвиняет», «тон спокойного финансиста».

**Пример: строка из питча до и после**

- До: «It reads receipts, invoices, PDFs, transfer screenshots and handwritten nota in any language and writes each one as a row in a Google Sheet in your own Drive, with a link to the original.»
- После: «Сфотографировали накладную — через минуту она строкой в вашей таблице, со ссылкой на оригинал. Если этот чек уже был, вы узнаете до оплаты.»

### 3. Визуальный стиль: что уже утверждено

**Обновлено 12.11.2026** по вашему дизайн-проекту «Nota, эскизы» (https://claude.ai/artifact/RgNYC6pvc5RMjix1Q4THFU): страницы «Финал», «Отчёты», «Языки и валюты». В первой версии этого раздела я предложил свою палитру, не видя проекта. Она отменена, правильный стиль — ниже.

#### Знак и надпись

- Надпись **Nota**, у которой буква «o» — оранжевый круг. Есть варианты на светлом и тёмном фоне, в один цвет и в инверсии.
- **Связка «Nota by Axiom»** уже нарисована, в строку и в столбик. Это совпадает с рекомендацией из раздела 1: использовать её там, где важны регистрация и доверие.
- **Аватар бота** 640 × 640: надпись на «бумажном» фоне с зонами безопасности под круглую обрезку Telegram.
- Знак проверен в реакциях размером 18 px (страница «В чатах и реакциях»).

#### Цвета (из «Финал → Надпись, связка, цвета»)

| Роль | Цвет | Контраст (WCAG) |
|---|---|---|
| Бумага, фон | **#F2F0EA** | — |
| Чернила, текст и надпись | **#15181D** | 15,6:1 на бумаге — AAA |
| Оранжевый: точка в «o», акцент | **#E8501C** | 3,3:1 на бумаге — только для крупных элементов и знака, **не для мелкого текста** |
| Зелёный: статусы | **#12A36B** | 2,85:1 на бумаге — только как цвет плашки или значка, **не для текста** |

В отчётах используются более тёмные оттенки для текста: #14201B (основной), #56635D (второстепенный), #0E5A52 и #0C7A4F (зелёные), фоны плашек #EEF1EE и #E2E7E3. Их и стоит брать для текста на статусах: #0C7A4F даёт 4,7:1, #0E5A52 — 7,1:1, #56635D — 5,5:1 на бумаге (AA).

#### Шрифт

**Inter** — в знаке-подписях и во всех отчётах (Google Fonts, лицензия SIL Open Font License, есть кириллица). Предложенные мной в первой версии Manrope и Inter заменены на один Inter, как в проекте. Для сумм — моноширинные цифры (`tabular-nums`).

#### Что уже готово для точек контакта

- **Отчёты в формате 1080 × 1350:** неделя, месяц и **«первые 30 платежей»**, с вариантами «нет дублей», «нечего проверять», «всё чисто». Есть на трёх языках (RU, EN, ID) и в пяти валютах (IDR, USD, EUR, THB, RUB).
- Нижняя строка отчёта: «Подготовлено в Nota · контроль расходов в Telegram · @NotaGetBot».

**Что из этого следует для предложения (`offer.md`):** отчёт «первые 30 платежей» — почти готовый макет для **отчёта проверки архива**, главного продающего момента. Не хватает одного блока сверху: «нашли N дублей и расхождений на сумму X» с тремя примерами. Это самая дешёвая доработка с самым большим эффектом.

#### Первые пять точек контакта

1. **Профиль бота:** имя, описание, аватар (готов: «Финал → Аватар бота»). Тексты есть в плане вирусности: «Nota · расходы», вариант Б описания. Обновить число «30 документов бесплатно» на 40.
2. **Отчёт по проверке архива** (на основе макета «первые 30 платежей»): первое, что видит владелец. Сумма найденного крупно, три примера, кнопка «Подключить». Нижняя строка «Подготовлено в Nota».
3. **Реакция ✍ в группе и приветствие:** единственное, что видят сотрудники. Спокойно, без рекламы.
4. **Карточка понедельничного отчёта:** её пересылают партнёрам, поэтому это главный носитель бренда.
5. **Ответ на первую жалобу:** «Спасибо, что написали. Вот что произошло: … Строку №… мы исправили / вы можете исправить так: … Если первый месяц не стоил своих денег, вернём $19.» Без шаблонного «ваше обращение очень важно для нас».

## Operations

Nota — это бот, а не магазин. Поэтому «день» здесь — поток документов, проверки, поддержка и отчёты.

Источники:
- описание продукта (стек, оператор, платежи, открытые вопросы);
- `numbers.json`, `offer.md`, план вирусности.

Правила и цены у поставщиков меняются: всё, что отмечено ссылкой, проверьте на странице перед решением.

### 1. Ежедневный цикл

Пометка 👁 значит, что этот шаг видит клиент.

1. **Ночью и утром — проверка здоровья системы:** очередь распознавания пуста, ошибок записи в Google нет, бот отвечает.
2. 👁 **Весь день — приём документов** в личке и в группах, ✍ на записанный документ.
3. **Весь день — распознавание и проверка:** хэш, визуальное сходство, сверка полей, вердикт OK / Review / DBL.
4. 👁 **Запись в таблицу пакетами раз в 1–2 минуты**, файл кладётся в папку на Drive клиента.
5. 👁 **Сигналы владельцу** о дублях и ошибках в личку.
6. 👁 **Поддержка:** ответы в боте через меню, цель — в течение рабочего дня.
7. 👁 **Проверки архива** у новых пользователей, отчёт «что нашли». На запуске это главный продающий момент.
8. **Вечером — разбор Review и ложных дублей:** выборочно 10–20 документов, чтобы замерить точность. До замера точность публично не называем.
9. 👁 **Понедельник 09:00 — недельные отчёты; 1-е число 10:00 — месячные.**
10. **Неделя — метрики:** установки, проверки архива, оплаты, отток, источники (Metabase и метки в ссылках).

### 2. Поставщики

| Что | Варианты | Цена и условия | Статус |
|---|---|---|---|
| **ИИ для распознавания** | Google Gemini API, OpenAI API, Anthropic API | Публичные прайсы: https://ai.google.dev/pricing · https://openai.com/api/pricing · https://www.anthropic.com/pricing. Оплата по факту, без минимума | Провайдер не выбран. Ваш замер — $0,01–0,02 за документ. **Сравнить на одних и тех же 200 балийских документах**: точность на рукописных накладных важнее цены |
| **Сервер и хостинг** (рассматривается Сингапур) | DigitalOcean (Singapore), AWS Lightsail (ap-southeast-1), Hetzner (Singapore) | https://www.digitalocean.com/pricing · https://aws.amazon.com/lightsail/pricing/ · https://www.hetzner.com/cloud | В расчёте $140 в месяц (хостинг $100 + сервер $40). Свой сервер Telegram Bot API, Redis и PostgreSQL помещаются на 1–2 машины |
| **Приём платежей** | Эквайринг Bank of Georgia; Telegram Stars (запасной вариант и основной для Узбекистана) | По описанию: около 2,8–3,2% для иностранных карт по данным интеграторов. Stars: https://core.telegram.org/bots/payments-stars | **Блокер запуска.** Узнать у банка: тарифы, автосписание, возвраты (нужны для гарантии), срок подключения |
| **Google API** (Sheets, Drive) | Google Cloud | API бесплатны в пределах квот. Верификация OAuth: https://support.google.com/cloud/answer/13463073 | **Блокер:** без верификации лимит 100 пользователей. Scope drive.file Google относит к рекомендуемым неограниченным, платный аудит безопасности для него обычно не нужен — проверить по документации на момент подачи |
| **Наблюдаемость ИИ** | Langfuse (упомянут в плане) | https://langfuse.com/pricing, есть бесплатный тариф | Для учёта затрат ИИ по каждому клиенту |
| **Домен и страницы** | Регистратор + Telegra.ph (описание и соглашение) | Домен — около десятка долларов в год, Telegra.ph бесплатно | Решить: свой домен или поддомен axiomco.io |

Реальных цен, которые отличались бы от `numbers.json`, нет, поэтому файл не менял. Когда выберете ИИ-провайдера и хостинг, обновите строки, и CFO пересчитает.

### 3. Люди

| Роль | Кто | Часы | Стоимость |
|---|---|---|---|
| Разработка и поддержка | Разработчик по задачам | По задачам, плюс ответы в поддержке в рабочие часы | $500–700 в месяц (от основателя) |
| Продукт, тексты, продажи, партнёры | Основатель | Сейчас параллельно с консалтингом | В расчёте не учтено |
| Проверка точности и Review | Основатель или сотрудник Axiom | 30 минут в день на запуске | Не учтено |

**График на первый месяц** (до 50 клиентов):

| День | Задача |
|---|---|
| Пн | Отчёты ушли в 09:00 — проверить. Разобрать метрики прошлой недели |
| Каждый день | Поддержка (разработчик). Звонки-настройки с первыми 50 клиентами (основатель) |
| Вт, Чт | Проверки архива и разговоры с теми, у кого что-то нашлось |
| Ср | Партнёры: УК, регистраторы |
| Пт | Выборка 20 документов на точность. Список правок разработчику |

**На 300+ клиентах** понадобится человек на поддержку и рост. Это слабое место, названное в вашем описании. Подходящая точка — после 100 платящих, когда станут известны конверсия и отток.

Налоги и взносы за людей зависят от страны: ИП в Грузии, работа на Бали. Проверить с бухгалтером.

### 4. Регламенты

**A. Утро (5 минут)**
1. Открыть дашборд: ошибки за ночь, длина очереди, ошибки записи в Google.
2. Если очередь больше 100 или есть ошибки записи — написать разработчику и включить в боте статус «работаем с задержкой».
3. Проверить, что в понедельник отчёты ушли всем активным клиентам.

**B. Проверка архива нового пользователя** (главная продажа)
1. Пользователь загрузил ZIP или выгрузку чата. Бот обрабатывает до 100 документов (бонус до 31.01.2027).
2. Отчёт: сколько документов, найденные дубли и расхождения, сумма, три примера со ссылками.
3. Если нашлось хоть что-то — в течение дня предложить звонок на 15 минут (первые 50 клиентов).
4. Если ничего не нашлось — так и написать. Показать, как будет работать недельный отчёт, без давления.
5. Записать результат в таблицу метрик: нашли / не нашли, сумма, источник клиента.

**C. Жалоба или ошибка распознавания**
1. Ответить в течение рабочего дня, по шаблону из `brand.md`: что случилось и что исправлено.
2. Если ошибка в сумме — исправить строку или показать, как это сделать. Правки клиента бот не перезаписывает.
3. Если ложный дубль — пометить пример для разбора точности.
4. Если клиент недоволен первым месяцем — вернуть $19 без вопросов (гарантия) и записать причину.

**D. Конец дня (5 минут)**
1. Разобрать все Review и ложные дубли за день по выборке.
2. Перенести неотвеченные обращения на утро с пометкой.

**E. Раз в неделю**
1. Метрики: установки, проверки архива, оплаты, отток, источники, затраты ИИ по клиентам.
2. Сверить счёт ИИ-провайдера с расчётом $0,01–0,02 за документ.
3. Список правок разработчику на неделю, сначала то, что мешает оплате и онбордингу.

### 5. Инструменты

| Задача | Инструмент | Почему |
|---|---|---|
| Бот и очереди | Python, aiogram 3, Redis, свой Bot API сервер | Уже работает (описание) |
| Данные | PostgreSQL с изоляцией клиентов | Уже работает |
| Таблица клиента | Google Sheets и Drive в аккаунте клиента | Ядро продукта |
| Метрики | Metabase (вы им пользуетесь в Axiom) | Без новых затрат |
| Затраты и качество ИИ | Langfuse | Учёт по каждому клиенту |
| Платежи | Bank of Georgia + Telegram Stars | Работают для ИП в Грузии. Stripe и PayPal недоступны (описание) |
| Поддержка | Меню бота | Клиент не выходит из Telegram |
| Учёт компании | Бухгалтер ИП в Грузии | Налоги и отчётность |

### 6. Регистрация, налоги, данные — что проверить

Правила разные в каждой стране и меняются. Каждый пункт нужно подтвердить в ведомстве или у специалиста. Это не юридическая консультация.

- [ ] **ИП в Грузии и налоговый режим** (например, статус малого бизнеса). Подходит ли он для продажи подписки клиентам за рубежом. Официальный портал налоговой службы: https://www.rs.ge
- [ ] **Пользовательское соглашение и политика конфиденциальности** по праву Грузии. Черновик соглашения уже есть. Добавить условия гарантии и возврата.
- [ ] **Персональные данные клиентов в Индонезии (UU PDP, закон 27/2022).** Обработка данных индонезийских пользователей, передача за рубеж. Ваше описание это уже называет: «юридическая проверка до масштаба».
- [ ] **Работа на Бали.** Какой статус нужен основателю и сотрудникам, чтобы вести эту деятельность из Индонезии (визы, KITAS, PT PMA). Подтвердить у вашего консультанта.
- [ ] **Правила Telegram для ботов и платежей.** Требование Stars для цифровых товаров внутри Telegram: https://core.telegram.org/bots/payments-stars и https://telegram.org/tos/bots
- [ ] **Google API Services User Data Policy и верификация OAuth.** Политика конфиденциальности на своём домене: https://developers.google.com/terms/api-services-user-data-policy
- [ ] **Товарный знак** (см. `brand.md`).
- [ ] **Страхование** профессиональной ответственности. Для софта на старте обычно не обязательно, но спросить у брокера, учитывая работу с финансовыми данными.

### 7. Риски

| # | Что может случиться | Вероятность | Насколько плохо | План |
|---|---|---|---|---|
| 1 | Платежи не подключены к запуску | Высокая | Высоко: нет выручки | Начать с Telegram Stars параллельно с банком. Сдвинуть дату запуска, а не запускаться бесплатно |
| 2 | Google OAuth не верифицирован, лимит 100 пользователей | Средняя | Высоко на росте | Подать заявку сейчас со scope drive.file и политикой на своём домене. На первые 100 лимита хватит |
| 3 | ИИ ошибается в суммах IDR (лишние нули), ложные дубли | Средняя | Высоко: подрывает доверие | Фильтр выбросов, статус Review, ежедневная выборка, замер точности до публичных заявлений |
| 4 | Проверки архива ничего не находят у малого бизнеса | Средняя | Высоко: рушится главное предложение | Прогнать 5–10 настоящих чатов до запуска. Если находок мало — продавать «таблицу без админа» и отчёт, а не дубли |
| 5 | Разработчик недоступен (болезнь, другая работа) | Средняя | Высоко: продукт без поддержки | Документация стека (описание: «легко передать»). Доступы у основателя. Запасной подрядчик на примете |
| 6 | Конверсия ниже 10% | Средняя | Высоко: платный рост невозможен (`cfo.md`) | Не включать рекламу до замера. Работать над онбордингом и отчётом архива |
| 7 | Telegram меняет правила или блокируется в стране | Низкая | Высоко | Данные клиента в его Drive. WhatsApp через отдельный номер в резерве |
| 8 | Утечка данных или инцидент с доступом | Низкая | Очень высоко | Минимум данных на серверах (только хэши), шифрование, изоляция клиентов, план уведомления по UU PDP |
| 9 | Сбой Google API или квот | Низкая | Средне | Очередь с повтором, пакетная запись, статус в боте |
| 10 | Медленный месяц, основатель занят консалтингом | Высокая | Средне | Ежедневные 30 минут на Nota в календаре. Человек на рост после 100 платящих |

## Launch plan

Сегодня 11.11.2026. Рабочая дата запуска **L — понедельник 7 декабря 2026** (из `marketing.md`). Её двигают три блокера: платежи, верификация Google OAuth и отчёт по проверке архива.

### 1. Проверка до трат: «основатели»

Формат — подписка с предоплатой. Деньги платят до публичного запуска, на реальных условиях.

**Что предлагаем.** Двадцати людям: 10 тёплых контактов основателя и 10 клиентов Axiom, у которых есть стройка или виллы.
1. Бесплатная проверка их рабочего чата: до 100 документов, отчёт «что нашли».
2. Если проверка их убедила — «пакет основателя»: **3 месяца Start за $57, оплата сразу**.
   - Цена та же, что в прайсе. Без скидки, чтобы не приучать ждать распродаж.
   - Цена фиксируется на 12 месяцев.
   - Звонок-настройка с командой.
   - Возврат за первый месяц, если не окупился.

**Как принять оплату, пока эквайринг не подключён:** Telegram Stars или обычный счёт и перевод на счёт ИП в Bank of Georgia. Что из этого допустимо для вашего ИП, проверить с бухгалтером.

**Критерий успеха (записан до начала):**

| Шаг | Порог успеха | С чем сравнить |
|---|---|---|
| Согласились на проверку чата | ≥10 из 20 | — |
| Проверка нашла хотя бы один дубль или расхождение | ≥30% проверок | Главное условие панели: «найдите деньги в старом чате» |
| Оплатили пакет основателя до L | **≥5 из 20 (25%)** | Панель: 21% (а это верхняя граница), повторная проверка предложения — 25% |

**Как читать результат:**
- **≥5 оплат.** Панель подтверждается. Запускаемся 7.12 по плану.
- **2–4 оплаты.** Запуск без платной рекламы. Разобрать причины отказов, вернуться в `/founder-offer`.
- **0–1 оплата.** Доверять живым людям, а не панели. Смотреть, что нашла проверка:
  - нашла мало — менять обещание: таблица без админа и отчёт вместо дублей;
  - нашла много, но не платят — дело в цене или доверии: `/founder-pricing`, доступ drive.file.

### 2. Обратный отсчёт

Пометка **★ — критический путь**: если задача опоздает, дата запуска сдвигается.

| Неделя | Задача | Кто | Срок |
|---|---|---|---|
| **11–15.11** | ★ Подать в банк заявку на эквайринг: тарифы, автосписание, возвраты | Основатель | 13.11 |
| | ★ Подать заявку на верификацию Google OAuth со scope drive.file, политика на своём домене | Разработчик + основатель | 15.11 |
| | Выбрать ИИ-провайдера: сравнить на 200 балийских документах | Разработчик | 15.11 |
| | Решить вопрос домена: свой или поддомен axiomco.io | Основатель | 15.11 |
| **16–22.11** | ★ Отчёт проверки архива: сумма, топ-3 примера, кнопка «Подключить», лимит 100 документов | Разработчик | 20.11 |
| | Telegram Stars как запасной способ оплаты | Разработчик | 22.11 |
| | Соглашение и политика: добавить гарантию и возврат, перевести на EN и ID | Основатель | 22.11 |
| | Профиль бота на RU, EN и ID; «40 документов бесплатно» везде (этап 0 плана вирусности) | Основатель | 18.11 |
| **23–29.11** | ★ **Проверка «основатели»**: 20 приглашений, прогон архивов (см. раздел 1) | Основатель | 23–29.11 |
| | Карточки на выдуманных данных: дубль, недельный отчёт, «о данных» | Основатель | 25.11 |
| | Маркетинговый календарь с L−14 (`marketing.md`) | Основатель | с 23.11 |
| | Строка в приветствии группы, строка в шапке таблицы, ссылка в подписи отчёта (этап 1 плана вирусности) | Разработчик | 29.11 |
| **30.11–6.12** | ★ Сквозной тест бота по ТЗ, оплата и возврат по-настоящему | Разработчик + основатель | 2.12 |
| | **Тихий запуск 3–4.12:** клиенты-основатели подключают свои группы | Основатель | 4.12 |
| | Решение «запускаемся или сдвигаем» по критерию проверки и блокерам | Основатель | 5.12 |
| | Метки источников, дашборд с тремя цифрами в Metabase | Разработчик | 5.12 |
| **7.12** | **Запуск** | Все | 7.12 |

Если к 5.12 не готова оплата или отчёт архива, запуск сдвигается на неделю. Запускаться бесплатно «пока без оплаты» нельзя: тогда не будет главной цифры — конверсии.

### 3. День запуска, 7.12 (время по Бали, WITA)

| Время | Что | Кто |
|---|---|---|
| 07:30 | Проверка системы по утреннему регламенту из `ops.md`: очередь, ошибки, оплата тестовой картой | Разработчик |
| 08:30 | Профиль бота, описание на Telegra.ph и ссылки с метками — финальная проверка | Основатель |
| 09:00 | Пост в своём Telegram-канале и Threads: «Бесплатная проверка рабочего чата до 31 января» | Основатель |
| 09:30–12:00 | Личные сообщения всей сети и клиентам Axiom: короткий текст + ссылка с меткой | Основатель |
| 10:00 | Письмо партнёрам: УК вилл и регистраторам | Основатель |
| 12:00 | Первые проверки архива: следить, что отчёты уходят. Звонки тем, у кого что-то нашлось | Основатель |
| 14:00 | Посты в 2–3 бизнес-чатах Бали, где это разрешено | Основатель |
| 18:00 | Сводка дня: установки, проверки, находки, оплаты, ошибки | Основатель + разработчик |
| Весь день | Поддержка в боте; ответ в течение 1–2 часов в день запуска | Разработчик |

**Если что-то ломается** (по рискам из `ops.md`):
- **Оплата не проходит.** Переключить на Telegram Stars. Принимать оплату счётом вручную для тех, кто готов.
- **Очередь распознавания растёт.** Статус «работаем с задержкой» в боте, проверки архива ставить в очередь, не отменять.
- **Ошибки записи в Google.** Повтор из очереди. Предупредить затронутых клиентов лично.
- **Ложные дубли и неверные суммы.** Извиниться, исправить, записать пример. Публично точность не обещать.
- **Достигнут лимит OAuth в 100 пользователей.** Лист ожидания в боте: «подключим в течение N дней».

### 4. Первые 30 дней

**Цифры каждую неделю** (из `cfo.md` и `marketing.md`):

| Цифра | Ориентир | Если хуже |
|---|---|---|
| Активные платящие против точки безубыточности | ≥45 к L+30 (безубыточность по постоянным расходам $740) | Ниже 20 к L+30 — разобрать воронку, рекламу не включать |
| Установка → оплата | ≥10%, цель 20% | Онбординг, текст о доступе, отчёт архива |
| Проверки архива с находками | ≥30% | Менять главное обещание (см. раздел 1) |
| Доля клиентов от рекомендаций и партнёров | ≥30% | Включить просьбу о рекомендации и кнопку «Поделиться отчётом» |
| Возвраты по гарантии | ≤20% | Читать причины, в первую очередь ошибки распознавания |

**Разборы:**
- **День 7 (14.12).** Сколько установок, откуда? Где бросают онбординг? Что нашли проверки? Включать ли тест рекламы на $300–500? Только если конверсия ≥10%.
- **День 14 (21.12).** Какой средний чек: $19 или $45? Держится ли около $30, на котором стоит экономика (`cfo.md`)? Какие возражения повторяются в «что помешало?»? Нужна ли проверка цены $19 против $29 (`pricing.md`)?
- **День 30 (6.01.2027).**
  - Сколько платящих и каков отток?
  - Достигнута ли цель первого месяца — 50 клиентов?
  - Какой канал дал больше всего клиентов по самой низкой цене?
  - Решение по рекламе по $10 за установку: при конверсии ≥12% она окупается за 4 месяца (`marketing.md`).
  - Обновить `numbers.json` реальной конверсией, оттоком и средним чеком, перезапустить `/founder-cfo` и `/founder-plan`.

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
