# Nota: локальные конкуренты (Индонезия), бизнес-боты в Telegram/WhatsApp, перепроверка цен

Проверено: 2026-11-11.

## Как собирались данные (важно прочитать)

- В этой облачной сессии **прямая загрузка страниц (WebFetch/curl) была заблокирована сетевыми настройками**: kledo.com, www.mekari.com, www.paper.id, accurate.id, play.google.com, reimburseme.ai, www.dext.com, www.zoho.com, www.hubdoc.com, www.capterra.com возвращали ошибку разрешения имени. Ни одну страницу открыть и прочитать целиком не удалось.
- Всё ниже взято **из сниппетов веб-поиска** (WebSearch) по указанным ссылкам. Ссылка указывает на страницу, из которой поиск достал факт; сам я её целиком не читал. Перед публичным использованием цифры стоит открыть вручную.
- «Слоган» — это заголовок страницы, как его показал поиск (обычно это H1/title сайта). Если заголовок не похож на слоган, это помечено.
- Отзывы Google Play (пункт 4) прочитать **не удалось**: play.google.com недоступен, а в поисковых сниппетах текстов отзывов почти нет. См. раздел 4.
- Ничего не придумано: где данных нет, так и написано «не найдено».

Чтобы закончить работу полностью, в сетевых настройках сессии нужно разрешить: play.google.com, kledo.com, mekari.com, expense.mekari.com, paper.id, accurate.id, majoo.id, kaskecil.id, reimburseme.ai, dext.com, zoho.com, hubdoc.com.

---

## 1. Индонезийские локальные конкуренты

### 1.1 Mekari Expense (бывш. Mekari Stream / Jojonomic) — самый близкий по функциям
- URL: https://expense.mekari.com/en
- Что продаёт: управление расходами для компаний: reimbursement, cash advance, purchase invoice, spend management ([Fitgap](https://us.fitgap.com/products/011908/mekari-expense), [mekari.com spend management](https://mekari.com/en/product/expense/spend-management/)).
- Цена: публичной цены за пользователя нет, «Contact sales». Fitgap пишет о комиссии **Rp2.500 за выплату (disbursement)** и о квоте Pro-плана до 50 сотрудников; сам Fitgap оговаривает, что это не проверено напрямую ([Fitgap](https://us.fitgap.com/products/011908/mekari-expense)). Capterra: «Contact vendor» ([Capterra](https://www.capterra.com/p/10027882/Mekari-Expense/)). Тарифы Mekari Stream (Starter / Value / Enterprise) указаны без цифр ([mekari.com/en/pricing/stream](https://mekari.com/en/pricing/stream/)).
- OCR по фото: **да**. Извлекает дату, вендора, описание позиций и сумму ([expense.mekari.com/en/feature/ocr](https://expense.mekari.com/en/feature/ocr), [бесплатный OCR-инструмент](https://expense.mekari.com/en/free-tools/ocr)). В приложении: Claims → Request → Reimbursement – Scan Receipt ([help center](https://help-center.expense.mekari.com/hc/en-us/articles/58179157929625)). Промо: 50 бесплатных OCR-кредитов и безлимитный Fraud AI Checker на 30 дней ([community.mekari.com](https://community.mekari.com/forums/topic/gratis-ocr-credits-fraud-ai-checker-unlimited-di-mekari-expense/)).
- WhatsApp/Telegram: подтверждения, что чеки принимаются через WhatsApp, **не найдено**; WhatsApp на сайте только как контакт отдела продаж.
- Дубликаты: **да, заявлено**. «Fraud AI Checker powered by Airene AI» находит дубликаты и почти одинаковые заявки в окне 7 дней (fuzzy matching), плюс необычные суммы ([блог Mekari: duplicative transaction detection](https://expense.mekari.com/en/blog/duplicative-transaction-detection), [OCR fraud detection](https://expense.mekari.com/en/blog/ocr-fraud-detection)). Это блог, а не документация.
- Слоган: заголовок страницы OCR-инструмента «Extract receipt and invoice Automatically with OCR technology» ([ссылка](https://expense.mekari.com/en/free-tools/ocr)). Главный слоган сайта получить не удалось.
- Рейтинг: G2 **4.7 / 12 отзывов** ([G2](https://www.g2.com/products/mekari-expense/)); Gartner Peer Insights 5.0 / 4 оценки ([Gartner](https://www.gartner.com/reviews/market/expense-management-software/vendor/mekari/product/mekari-expense)); App Store iOS: оценок недостаточно для показа ([App Store](https://apps.apple.com/us/app/-/id6466607163), [AppGoblin](https://appgoblin.info/apps/6466607163)). Рейтинг Google Play не найден.

### 1.2 Mekari Jurnal (бухгалтерия)
- URL: https://www.jurnal.id/id/harga/
- Что продаёт: облачная бухгалтерия для МСП.
- Цена ближайшего плана: **Essentials Rp359.100/мес** (зачёркнуто Rp399.000, скидка 10%), при оплате за год; по стороннему источнику без PPN ([jurnal.id/id/harga/essentials](https://www.jurnal.id/id/harga/essentials/), [EN-версия](https://www.jurnal.id/en/pricing-plans/essentials), [Quasa](https://quasa.io/id/media/accurate-vs-jurnal-harga-awal-berbeda-add-on-menentukan-total-biaya)). HashMicro приводит старую сетку: Basic от Rp299.000, Pro Rp499.000 ([HashMicro](https://www.hashmicro.com/id/blog/expense-management-software/)).
- OCR: в найденных материалах не подтверждено.
- WhatsApp/Telegram: не найдено.
- Дубликаты: не найдено.
- Слоган: в сниппетах только «Standar keamanan ISO/IEC 27001» (это бейдж, а не слоган).
- Рейтинг: G2 4.9 / 24 отзыва ([G2](https://www.g2.com/sellers/jurnal)); Capterra 5.0 / 23 ([Capterra](https://www.capterra.com/p/199870/Jurnal/)); Android-приложение «Mekari Jurnal Cloud Accounting»: 306,8 тыс.+ установок, но звёзды в выдаче не показаны ([AppGoblin](https://appgoblin.info/apps/id.jurnal.mobile)).

### 1.3 Kledo (бухгалтерия) + GajiHub (HR/payroll того же разработчика)
- URL: https://kledo.com
- Что продаёт: облачная бухгалтерия для МСП; тарифы Free / Pro / Elite / Champion ([Quasa](https://quasa.io/id/media/jurnal-atau-kledo-selisih-harga-besar-tetapi-gudang-bisa-membalik-pilihan), [HashMicro](https://www.hashmicro.com/id/blog/aplikasi-kledo/)).
- Цена: источники расходятся. **Pro Rp159.900/мес** по Quasa, без PPN ([Quasa](https://quasa.io/id/media/jurnal-atau-kledo-selisih-harga-besar-tetapi-gudang-bisa-membalik-pilihan)); англоязычная страница Kledo: «starts at 213,000 IDR per month», скидка 25% при оплате за год ([kledo.com/?p=14392](https://kledo.com/?p=14392)); Champion: IDR 399.900 (зачёркнуто 615.231) в месяц ([kledo.com/startup-business](https://kledo.com/startup-business/)).
- OCR: **не найдено** ни на одной странице.
- WhatsApp/Telegram: не найдено.
- Дубликаты: не найдено.
- Слоган: заголовок EN-страницы «Accounting Software with the Most Complete and Intuitive Bookkeeping Features» ([kledo.com/accounting](https://kledo.com/accounting/)).
- Рейтинг: Capterra и GetApp: 0 отзывов ([Capterra](https://www.capterra.com/p/10016663/Kledo/)). Страница разработчика в Google Play показывает Kledo POS, GajiHub и др., без рейтинга ([Google Play dev](https://play.google.com/store/apps/developer?id=Kledo)).
- **GajiHub**: HRIS (посещаемость, отпуска, сверхурочные, **reimbursement**, расчётные листы) ([App Store](https://apps.apple.com/id/app/gajihub-payroll-absensi/id1604540147?l=id)). Есть ли фото чеков/OCR и какая цена, найти не удалось.

### 1.4 Accurate Online (бухгалтерия)
- URL: https://accurate.id
- Цена: с 1 января 2026 **Rp300.000/мес без PPN (Rp333.000 с PPN 11%)**; для старых клиентов действовала цена Rp250.000 до 30.06.2026 ([accurate.id: harga 2026](https://accurate.id/informasi/pengguna/harga-data-usaha-2026/)). Paket Dasar: Rp333.000/мес, 1 пользователь, 1 база, триал 30 дней; за год Rp3.996.000; доп. пользователь +Rp22.200/мес, филиал +Rp99.900/мес ([accurate.id/trial/aol](https://accurate.id/trial/aol/)).
- OCR / WhatsApp / дубликаты: в найденных материалах нет.
- Слоган: не получен.
- Рейтинг: не найден.

### 1.5 majoo (POS + бэк-офис)
- URL: https://majoo.id/harga
- Цена: **Starter Rp249.000 за точку в месяц** без PPN; Advance Rp499.000; Prime Rp999.000 ([majoo.id/harga](https://majoo.id/harga), [majoo.id/harga/detail](https://majoo.id/harga/detail)). FAQ: Starter до 3 точек, минимальная подписка 12 месяцев ([majoo.id/faq](https://majoo.id/faq)).
- OCR чеков расходов: не найдено.
- WhatsApp: есть WhatsApp-**уведомления и отчёты** по точке для менеджеров, add-on за точку ([majoo.id/integrasi-laporan-via-whatsapp](https://majoo.id/integrasi-laporan-via-whatsapp)). Это отчёты из POS, а не приём чеков от персонала.
- Слоган (title страницы цен): «Satu Aplikasi dengan Fitur Lengkap Tanpa Biaya Tambahan» ([majoo.id/harga](https://majoo.id/harga)).
- Рейтинг Google Play: в выдаче нет. Сторонний обзор отзывов Google Play (Kimola, платный отчёт) говорит о «frequent errors and poor customer service» ([Kimola](https://kimola.com/reports/unlock-insights-majoo-app-user-feedback-report-google-play-en-158143)).

### 1.6 BukuWarung (учёт для микробизнеса)
- URL: https://go.bukuwarung.com
- Что продаёт: бесплатная книга учёта для варунгов: продажи, расходы (pengeluaran), долги клиентов, отчёты ([исследование PNJ](https://repository.pnj.ac.id/41633/1/Halaman%20Identitas%20Skripsi_Maria%20Belen%20Marta%20Uli_2204431043.pdf), [DailySocial](https://en.dailysocial.id/post/how-to-use-shop-book)).
- Цена: не найдена.
- OCR фото чеков: **не подтверждено** ни одним источником.
- WhatsApp/Telegram, дубликаты: не найдено.
- Рейтинг Google Play: **4.38★, 94,6 тыс. оценок** (по трекеру AppGoblin; данные о листинге от 9 фев 2026) ([AppGoblin](https://appgoblin.info/apps/com.bukuwarung)).

### 1.7 BukuKas (Lummo) — закрыт
- Прекратил работу в мае 2023 (по одному источнику 26.05.2023), приложение удалено из Google Play; Lummo по CB Insights банкрот с сентября 2023 ([CB Insights](https://www.cbinsights.com/company/bukukas), [Bisnis.com](https://teknologi.bisnis.com/read/20231222/266/1726326/15-startup-besar-yang-tutup-dan-phk-di-ri-2023-pegipegi-hingga-jdid), [DealStreetAsia](https://www.dealstreetasia.com/?p=340722)). Не конкурент.

### 1.8 Paper.id
- URL: https://www.paper.id — сайт недоступен из сессии, цены в поиске **не найдены**. Ничего не утверждаю.

### 1.9 Mekari Talenta (HR, модуль reimbursement)
- URL: https://www.talenta.co/fitur/expense-management/
- Что продаёт: reimbursement как часть HR-платформы: лимиты по сотруднику/должности, периоды, категории ([talenta.co](https://www.talenta.co/fitur/software-payroll/sistem-reimbursement/)).
- Цена: только через отдел продаж ([talenta.co](https://www.talenta.co/fitur/expense-management/)).
- Слоган (title): «Percepat proses reimbursement karyawan hingga 70%» ([ссылка](https://www.talenta.co/fitur/software-payroll/sistem-reimbursement/)).
- OCR / WhatsApp / дубликаты: в найденном не указано.

### 1.10 Новый класс: индонезийские WhatsApp/Telegram-боты учёта (главная находка)

Это ближайшие локальные аналоги по форме (бот в мессенджере + фото чека). Все найдены через поиск, страницы сам не открывал.

| Продукт | URL | Канал | Фото/OCR | Цена | Слоган (title страницы) |
|---|---|---|---|---|---|
| **KasKecil.id** | https://kaskecil.id/ | WhatsApp **и Telegram** | Да: «OCR dasar» во Free, «OCR lanjutan (akurasi 99.5%)» в Premium | Free Rp0 (до 100 транзакций/мес); **Premium Rp149.000/мес** без налога, возврат денег 30 дней | «KasKecil.id: Kelola Kas Kecil Harian dengan Mudah & Cerdas» |
| Mingo | https://mingo.id/ | WhatsApp | Да (фото чека, голос) | Заявлен как бесплатный | «Mingo — Catat Keuangan Otomatis Lewat WhatsApp, Gratis» |
| Rekafin | https://rekafin.id/ | WhatsApp | Фото struk/nota только в платных планах Family/UMKM/Enterprise | Цена не найдена | — |
| BotMoni | https://botmoni.com/ | WhatsApp | Да, рекап в веб-дашборде | Не найдена | «BotMoni — Catat keuangan lewat chat WhatsApp» |
| CatatAja | https://catataja.id/ | WhatsApp | Да, веб-дашборд | Не найдена | «CatatAja: Catat Keuangan Lewat WhatsApp Pakai AI» |
| Ikisae | https://ikisae.com/ | WhatsApp | Не уточнено | Не найдена | «Ikisae — Catat Keuangan Otomatis via WhatsApp» |
| Litra | https://litra.litegral.com/ | WhatsApp | Не уточнено; интеграция с Google Spreadsheet в платном плане | Не найдена | — |

Источники по KasKecil: тарифы и OCR ([kaskecil.id](https://kaskecil.id/)), заявление «5.000+ pemilik UMKM» и экспорт в Excel, блог со сравнением с ботами ([kaskecil.id/blog](https://kaskecil.id/blog/bot-telegram-pencatat-keuangan)). В том же блоге упоминается конкурент **Rekapin за Rp29.000/мес**, отдельно подтвердить не удалось. KasKecil продаётся и в бандле Sellora (Starter от Rp199 тыс./мес за продукт) ([sellora.id](https://sellora.id/)). Работает ли KasKecil в **групповом** чате сотрудников, пишет ли в Google Sheets владельца и ловит ли дубликаты, **не найдено**.

Остальные строки таблицы: сводка поиска по запросу «bot WhatsApp catat pengeluaran foto struk» ([mingo.id](https://mingo.id/), [rekafin.id](https://rekafin.id/), [botmoni.com](https://botmoni.com/), [catataja.id](https://catataja.id/), [ikisae.com](https://ikisae.com/), [litra.litegral.com](https://litra.litegral.com/)). Поиск также упоминал MoneyBot и Spendy как боты, «пишущие в Google Sheets пользователя», но без ссылок на их сайты, поэтому в таблицу их не включаю.

Вывод по Индонезии: крупные игроки (Mekari, Accurate, Kledo, majoo) это полноценные системы с приложением и ценой Rp250–400 тыс./мес (≈$15–25), обычно на одну компанию или точку. Из них OCR и антидубли есть только у Mekari Expense, и он продаётся через отдел продаж. WhatsApp-боты (KasKecil, Mingo, CatatAja…) дешевле и проще, но рассчитаны на одного владельца и личный учёт или учёт мелкой кассы. Модель «бот в существующей группе сотрудников» ни у одного из них не заявлена.

---

## 2. Telegram/WhatsApp-боты и сервисы для бизнес-сбора чеков (вне уже изученного списка)

| Продукт | Что делает | Группа | Дубликаты | Таблица | Цена | Ссылка |
|---|---|---|---|---|---|---|
| **Tailride** | Счета/чеки через Telegram и WhatsApp → QuickBooks, Xero, Odoo, Business Central | Не указано | **Да**: повторная отправка не обрабатывается и не тарифицируется повторно | Нет (учётные системы) | Free 10 счетов/мес; платные тарифы не найдены | [tailride.so/integrations/telegram](https://tailride.so/integrations/telegram), [блог](https://tailride.so/blog/capture-invoices-whatsapp-telegram), [docs](https://docs.tailride.so/features/integrations-details/telegram) |
| **ProverkaCheka** (Казахстан) | Проверка чеков Kaspi по QR-коду против подделок и **повторного использования** | **Да**, групповой чат с общей базой: «если менеджер А проверил чек утром, а менеджер Б получит тот же чек вечером — бот покажет дубликат»; выгрузка в CSV | Да | CSV | Не найдена | [proverkacheka.kz/blog](https://proverkacheka.kz/blog/telegram-bot-gruppa-nastrojka/), [Dodo Payments](https://index.dodopayments.com/proverkacheka) |
| Project Receipts Bot | Чеки от участников в Telegram → Google Таблицы, фото → Google Drive, папка и таблица на проект | Участники проекта | Не указано | **Google Sheets** | Не указана (сайт на github.io) | [roksana870.github.io](https://roksana870.github.io/) |
| Бухгалтерия NurTech | Учёт голосом, Google-таблица, отчёты в Telegram | Не указано | Не указано | Google Sheets | Не найдена | [buh.nurtech.dev](https://buh.nurtech.dev/) |
| ExpenseBot | Командный план, по листингу $10/пользователь/мес (листинг плохо читается) | — | — | — | $10/user/mo (не проверено) | [xpay.sh](https://www.xpay.sh/saas-pricing/expensebot/) |
| MonthyBot | Telegram-бот учёта и платежей | — | — | — | — | [monthy.ru](https://monthy.ru/) |

DIY-класс (важно как субститут): шаблоны n8n «Telegram → OCR/LLM → Google Sheets» с проверкой дублей по message ID или ключу (вендор+дата+сумма), в том числе **«Track employee expense receipts from Telegram with GPT-4o-mini and Google Sheets»** ([n8n 19225](https://n8n.io/workflows/19225-track-employee-expense-receipts-from-telegram-with-gpt-4o-mini-and-google-sheets), [n8n 18286](https://n8n.io/workflows/18286-track-receipt-expenses-from-telegram-using-google-gemini-and-google-sheets), [n8n 20026, немецкий НДС, кнопки «Add anyway / Ignore» при подозрении на дубль](https://n8n.io/workflows/20026-log-german-vat-ready-expense-receipts-via-telegram-with-openai-and-google-sheets/)). Open source: бот для семейной группы в Telegram → Google Sheets ([bendorshai/expenses_bot](https://github.com/bendorshai/expenses_bot)); WhatsApp-бот, слушающий одну группу → Google Sheets ([dararafida/bot_tracking_financial](https://github.com/dararafida/bot_tracking_financial)); индонезийский kasbot-ai (WhatsApp, OCR, MySQL, предупреждение «kemungkinan duplikat») ([rhandyta/kasbot-ai](https://github.com/rhandyta/kasbot-ai)); финбот с локальной моделью, при повторном фото спрашивает кнопками ([d3c0r1x/finance-bot](https://github.com/d3c0r1x/finance-bot)). На Freelancer есть заказ на бота «проверка дубликатов чеков + синхронизация с Google Sheets», то есть спрос формулируется именно так ([freelancer](https://www.fi.freelancer.com/projects/telegram-api/telegram-40640137)).

---

## 3. Перепроверка цен (2026-11-11, по поисковым сниппетам; сайты вендоров не открывались)

| Продукт | Было у нас | Что нашёл | Изменилось? |
|---|---|---|---|
| REME (reimburseme.ai) | $5 / $8 за пользователя в месяц | Starter **$5/пользователь/мес** (WhatsApp, безлимит чеков, «3-agent fraud detection», QuickBooks/Xero, до 5 GL-счетов); **Growth $8** «Per Month» + приоритетная поддержка с SLA 4 часа; триал 7 дней с картой ([GoodFirms](https://www.goodfirms.co/software/reimburseme-ai), [Capterra UK](https://www.capterra.co.uk/software/1111009/reimburseme-ai)) | Совпадает. На GoodFirms у Growth написано «$8 Per Month» без «per user»; вероятно, это ошибка листинга. reimburseme.ai/pricing недоступен |
| Dext Business | $31,50/мес за 250 документов | 5 пользователей / 250 док.: **$25,21/мес при годовой оплате** ($302,50/год, US, без налога) по странице Dext; помесячно **$31,50** (по обзорному сайту; годовая на 20% дешевле). Следующий шаг: $46,50/мес (год) за 10 пользователей / 500 док. AU: A$33,58/мес ([dext.com/us/pricing](https://www.dext.com/us/pricing/prepare-direct/), [dext.com/business/pricing](https://dext.com/business/pricing), [help.dext.com](https://help.dext.com/en/articles/647776-dext-plans-for-businesses), [Capterra](https://www.capterra.com/p/160189/Dext/pricing/)) | Помесячная цена не изменилась; стоит указывать и годовую $25,21 |
| Zoho Expense | $3/пользователь | Standard **$3/пользователь/мес при годовой оплате, $4 помесячно**; Premium $5; Free до 3 пользователей. Pricingsaas зафиксировал снижение Standard с $4 до $3 (−25%) между окт. 2025 и янв. 2026, а также перенос **itemized receipt OCR из Premium в Standard** (2026 W32) ([Capterra](https://www.capterra.com/p/142384/Zoho-Expense/pricing/), [pricingsaas 2025Q4](https://pricingsaas.com/companies/zoho.expense/diffs/2025Q4), [pricingsaas 2026W32](https://pricingsaas.com/companies/zoho.expense/diffs/2026W32), [CostBench](https://www.costbench.com/software/expense-management/zoho-expense/)) | Цена та же ($3 только при годовой оплате). Новое: OCR с разбором позиций теперь в Standard |
| Hubdoc | $12/мес | Basic **$12/мес**, триал 30 дней без карты ([Capterra](https://www.capterra.com/p/165724/Hubdoc/pricing/), [PricingSaaS](https://pricingsaas.com/companies/hubdoc)). G2 и ITQlick пишут $20/мес ([G2](https://www.g2.com/products/hubdoc/pricing), [ITQlick](https://www.itqlick.com/hubdoc/pricing)); в Xero US есть встроенный Smart Document Capture без доплаты ([SparkReceipt, окт. 2026](https://sparkreceipt.com/alternative-to/hubdoc/)) | Без изменений ($12), но источники расходятся ($20) |

---

## 4. Отзывы Google Play по 2–3 ключевым индонезийским приложениям

**Не выполнено в полном объёме.** play.google.com заблокирован в сессии, а поиск не возвращает тексты отзывов (запросы по BukuWarung, Mekari Jurnal, Kledo, majoo с фильтрами «bintang 1», «error», «lambat» дали только маркетинговые страницы). Посчитать темы с количеством и дословными цитатами я не могу и придумывать не стал.

Что удалось найти косвенно (все темы **thin**):
- **majoo**: по платному отчёту Kimola об отзывах Google Play, недовольство в основном из-за «frequent errors and poor customer service» ([Kimola, Google Play](https://kimola.com/reports/unlock-insights-majoo-app-user-feedback-report-google-play-en-158143)). Пример отзыва в App Store от 08.03.2025: «Respon majoo chat care sangat lama,sering eror» ([Kimola, App Store](https://kimola.com/reports/unlock-business-insights-with-our-majoo-app-user-feedback-report-app-store-id-158142)). Тема «ошибки + медленная поддержка»: thin (1 цитата, сводка вендора отчётов).
- **Mekari Expense**: в G2 12 отзывов, средняя 4.7, негатив в сниппетах не виден ([G2](https://www.g2.com/products/mekari-expense/reviews_and_filters)). thin.
- **Mekari Jurnal / Kledo / BukuWarung**: тексты отзывов не получены.

Следующий шаг: открыть вручную (или разрешить play.google.com) листинги com.bukuwarung, id.jurnal.mobile, приложения Mekari Expense и majoo, отсортировать по 1–3★ и посчитать темы.

---

## 5. Есть ли уже «бот в существующей группе + дубликаты + Google Sheets владельца»?

Готового **коммерческого** продукта, где сошлись бы все три признака, не найдено:
- **ProverkaCheka**: группа + дубликаты, но только чеки Kaspi по QR, выгрузка в CSV, Казахстан.
- **Tailride**: Telegram/WhatsApp + дубликаты, но выгрузка в учётные системы, а не в Sheets, и про группы ничего не сказано.
- **Project Receipts Bot**: участники проекта + Google Sheets/Drive, про дубликаты ничего не сказано.
- **Mekari Expense**: дубликаты (7 дней, fuzzy) + OCR, но работает через своё приложение, без мессенджера и без Sheets, цена по запросу.
- **KasKecil.id**: Индонезия + WhatsApp/Telegram + OCR за Rp149.000/мес; про группы, дубликаты и Sheets ничего не сказано.
- Все три признака сразу есть только в **DIY-шаблонах n8n** и open-source проектах: это главный субститут для технически подкованного владельца.
