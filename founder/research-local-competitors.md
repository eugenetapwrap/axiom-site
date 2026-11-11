# Nota: локальные конкуренты (Индонезия), бизнес-боты в Telegram/WhatsApp, перепроверка цен

Проверено: 2026-11-11.

## Метки достоверности

- **[стр.]** (verified on page): факт прочитан мной на самой странице 2026-11-11. Страница скачана через curl и переведена в текст.
- **[сниппет]** (snippet only): факт взят из поискового сниппета, страницу я не открывал или не смог открыть. Перед публичным использованием надо проверить.
- «Слоган» везде скопирован дословно из H1 или `<title>` главной страницы вендора [стр.].
- Ничего не придумано. Где данных нет, так и написано.

Как собирались данные: в первом проходе страницы были недоступны, работал только поиск. Во втором проходе сетевой доступ открыли, и вендорские страницы и Google Play читались через curl (WebFetch по-прежнему не резолвил хосты). Google Play отдаёт без JavaScript только рейтинг, распределение звёзд и 3 «самых полезных» отзыва на язык интерфейса. Остальные отзывы подгружаются JS-запросами. Массово выгружать их через внутренний API Play я не стал, потому что это уже скрейпинг. Поэтому в разделе 4 на приложение прочитано по 6 отзывов (интерфейс id + en).

---

## 1. Индонезийские локальные конкуренты

### 1.1 Mekari Expense — самый близкий по функциям, но для средних компаний
- URL: https://expense.mekari.com/en
- Слоган (H1): «Full control over business spend with one spend management system»; title: «Mekari Expense - Top #1 Spend Management Software in Indonesia» [стр.] ([главная](https://expense.mekari.com/en))
- Что продаёт: командировки, reimbursement, корпоративные карты, AP, закупки [стр.] ([главная](https://expense.mekari.com/en)).
- **Цена [стр.]** ([pricing](https://expense.mekari.com/en/pricing)):
  - **Claims + Travel Suite: Rp30.000 за сотрудника в месяц, минимум 50 сотрудников** (то есть от Rp1.500.000/мес, около $90). Включает Reimbursement, Cash advance, Business trip, Custom policy, **OCR**.
  - Cards Suite: Rp75.000 за сотрудника в месяц, минимум 20 сотрудников.
  - Procurement Suite: Rp50.000 за сотрудника в месяц, минимум 20 сотрудников, с OCR.
  - Spend Management Suite: минимум 50 сотрудников, «Consult with us».
  - Исправление к первому проходу: раньше я писал «публичной цены нет». Это неверно, цены опубликованы. Цифра Fitgap про Rp2.500 за выплату на странице цен не подтвердилась.
- OCR по фото: **да** [стр.]: «OCR Invoice & Receipt — Automatically Scan & Extract Invoice and Receipt Data» ([главная](https://expense.mekari.com/en)); OCR входит в Claims + Travel [стр.].
- WhatsApp/Telegram: на сайте WhatsApp встречается только как «WhatsApp sales» [стр.]. Канала подачи чеков через мессенджер нет.
- Дубликаты: **да** [стр.]: «Detects identical or near-identical submissions within a 7-day window using fuzzy matching logic» (Fraud AI Checker на Airene AI, риск-скоринг в 4 уровня) ([блог Mekari](https://expense.mekari.com/en/blog/duplicative-transaction-detection)). Отдельная страница фичи `/en/feature/fraud-ai-checker` отдаёт 404 [стр.].
- Рейтинг Google Play: **4,6★, 102 отзыва, 5 тыс.+ установок**. Звёзды: 5★ 86, 4★ 3, 3★ 3, 2★ 1, 1★ 8 [стр.] ([Google Play](https://play.google.com/store/apps/details?id=com.mekari)). G2 4.7 / 12 отзывов [сниппет] ([G2](https://www.g2.com/products/mekari-expense/)).

### 1.2 Mekari Jurnal (бухгалтерия)
- URL: https://www.jurnal.id/id/
- Слоган (H1): «Optimalkan Pertumbuhan Bisnis dengan Software Akuntansi dan Operasional Terintegrasi» [стр.]
- **Цена [стр.]** ([harga](https://www.jurnal.id/id/harga/)): **Essentials Rp399.000/мес, при годовой оплате скидка 25%, то есть Rp299.250/мес**; Plus Rp899.000, со скидкой Rp674.250; Jurnal 360 по запросу. Есть вариант «Per kuarter» по Rp399.000.
  - Изменение к первому проходу: сниппет показывал скидку 10% и Rp359.100. Сейчас на странице 25% и **Rp299.250**.
- OCR / приём чеков через мессенджер / дубликаты: на странице цен не упоминаются [стр.]. WhatsApp только как «WhatsApp sales».
- Рейтинг Google Play: **4,5★, 1,28 тыс. отзывов, 100 тыс.+ установок**. 5★ 1102, 4★ 10, 3★ 30, 2★ 20, 1★ 110 [стр.] ([Google Play](https://play.google.com/store/apps/details?id=id.jurnal.mobile)).

### 1.3 Kledo (бухгалтерия) + GajiHub
- URL: https://kledo.com
- Слоган (H1 главной): «Cara Lebih Baik Untuk Mengelola Keuangan Bisnismu»; H1 страницы цен: «Semua Fitur Hebat Kledo Hanya 159rb/bulan» [стр.] ([главная](https://kledo.com/), [harga](https://kledo.com/harga))
- **Цена [стр.]** ([harga](https://kledo.com/harga)), всё без PPN:
  - Free Rp0: 1 пользователь, 1.000 счетов/мес.
  - **Pro Rp159.900/мес при годовой оплате** (Rp246.000/мес при оплате раз в 3 месяца), 3.000 счетов.
  - Elite Rp279.900 / 430.615.
  - Champion Rp399.900 / 615.231.
  - На странице заявлено «Hemat 35%» за годовую оплату. Meta-описание главной всё ещё говорит «Hanya 139.900/bln», это устаревший текст.
  - Цифру «213,000 IDR» из первого прохода [сниппет] на странице цен я не нашёл.
- OCR: на страницах цен и главной не упоминается [стр.].
- WhatsApp: только «Saldo Whatsapp — Kirim tagihan ke Whatsapp» (отправка счетов клиентам) и WhatsApp API как add-on [стр.]. Приёма чеков нет.
- Дубликаты: не упоминаются.
- GajiHub: HRIS с reimbursement [сниппет] ([App Store](https://apps.apple.com/id/app/gajihub-payroll-absensi/id1604540147?l=id)). Есть ли OCR и сколько стоит, не проверял.

### 1.4 Accurate Online (бухгалтерия)
- URL: https://accurate.id
- Слоган (H1): «Kelola Bisnis Mudah, Accurate Solusinya!» [стр.] ([главная](https://accurate.id/))
- **Цена [стр.]** ([trial/aol](https://accurate.id/trial/aol/)):
  - **Rp333.000/мес**: 1 пользователь, 1 база данных.
  - Годовой тариф Rp3.996.000.
  - Промо: Rp3.219.000 за первый год (2 пользователя; на странице также стоят Rp355.200 и Rp268.250/мес).
  - Доп. филиал +Rp99.900/мес, доп. пользователь +Rp22.200/мес.
  - Объявление о новой цене с 01.01.2026 (Rp300.000 без PPN): [сниппет] ([accurate.id](https://accurate.id/informasi/pengguna/harga-data-usaha-2026/)).
- OCR / мессенджеры / дубликаты: на проверенных страницах нет.

### 1.5 majoo (POS + бэк-офис)
- URL: https://majoo.id
- Слоган (H1): «Aplikasi Manajemen Bisnis, Operasional Serba Otomatis»; title: «Aplikasi POS Lengkap Pendukung UMKM Lebih Maju» [стр.] ([главная](https://majoo.id/))
- **Цена [стр.]** ([harga](https://majoo.id/harga)), без PPN:
  - **Starter Rp249.000 за точку в месяц**: одна точка, до 2 терминалов, «Pencatatan Keuangan».
  - Advance Rp499.000: несколько точек, полная бухгалтерия, «Struk Digital: Whatsapp».
  - Prime Rp999.000: зарплата, фото-посещаемость.
- OCR чеков расходов: нет. WhatsApp: цифровой чек покупателю, отчёты для менеджеров [стр.] ([integrasi WA](https://majoo.id/integrasi-laporan-via-whatsapp)).
- Рейтинг Google Play: **4,9★, 16,3 тыс. отзывов, 100 тыс.+ установок** [стр.] ([Google Play](https://play.google.com/store/apps/details?id=com.klopos)). В распределении звёзд на странице 5★ 5760, 4★ 49, 3★ 9, 2★ 19, 1★ 119; это расходится со счётчиком 16,3 тыс., вероятно, гистограмма считает только недавние или верифицированные оценки.

### 1.6 BukuWarung (учёт для микробизнеса, сместился в платежи)
- URL: https://bukuwarung.com
- Описание в Play сейчас начинается с «BukuAgen: Agen Pembayaran Resmi… mesin EDC Mini ATM», og:description: «Agen Pembayaran, EDC, PPOB diawasi oleh OJK» [стр.]. Продукт сместился от бухгалтерии к платёжному агентству.
- **Рейтинг Google Play: 3,2★, 94,7 тыс. отзывов, 5 млн+ установок**. Звёзды: 5★ 41.540, 4★ 5.941, 3★ 6.600, 2★ 6.660, **1★ 32.832 (около 35%)** [стр.] ([Google Play](https://play.google.com/store/apps/details?id=com.bukuwarung)).
  - Исправление: в первом проходе по сниппету AppGoblin я написал 4,38★. Это неверно.
- OCR / дубликаты / мессенджер: не заявлено.

### 1.7 Paper.id (инвойсинг и платежи; не прямой конкурент)
- URL: https://www.paper.id
- Слоган (H1): «Platform Lengkap untuk Invoicing & Transaksi Bisnis» [стр.] ([главная](https://www.paper.id/))
- Цена [стр.] ([pricing](https://www.paper.id/pricing)): Paper Free бесплатно; **PaperPlus Rp90.000/мес** (сроки 6 или 12 месяцев); Paper Network бесплатно для связанных партнёров. Страница `/harga` отдаёт 404.
- Продукт про исходящие счета, e-Meterai и приём оплат. Распознавания чеков нет [стр.].

### 1.8 Mekari Talenta (HR, модуль reimbursement)
- Цена только через отдел продаж [сниппет] ([talenta.co](https://www.talenta.co/fitur/expense-management/)). Не проверял.

### 1.9 BukuKas (Lummo): закрыт в мае 2023 [сниппет] ([CB Insights](https://www.cbinsights.com/company/bukukas), [Bisnis.com](https://teknologi.bisnis.com/read/20231222/266/1726326/15-startup-besar-yang-tutup-dan-phk-di-ri-2023-pegipegi-hingga-jdid)).

### 1.10 Индонезийские WhatsApp/Telegram-боты учёта

**KasKecil.id: проверено на странице**
- URL: https://kaskecil.id/ (оператор PT Ventera Intellix Group) [стр.]
- Слоган (H1): «Kas kecil bocor, dan kamu nggak tahu ke mana perginya.»; title: «KasKecil.id: Kelola Kas Kecil Harian dengan Mudah & Cerdas» [стр.]
- Что делает: запись трат через WhatsApp или Telegram (текст «Beli plastik 15rb», фото чека, голосовое), OCR, ежедневная сводка в 21:00 WIB в WhatsApp/Telegram/email, экспорт в Excel/PDF/CSV [стр.].
- **Цена [стр.]**: Free Rp0 (до 100 транзакций/мес, 1 счёт, «OCR dasar», бот с базовыми командами, экспорт CSV); **Premium Rp149.000/мес** без налога (безлимит, «OCR lanjutan (akurasi 99.5%)», голосовые, мультиворкспейс). Триал 14 дней без карты, возврат денег 30 дней.
- **Групповой чат сотрудников:** функции нет [стр.]. В тексте главной «WA grup» фигурирует только как боль клиента: «Sudah 3 malam ngerapiin nota, dari 5 folder WA grup…». Сводка «siap dibagikan ke tim», то есть её можно переслать команде. Модель «бот в группе» не заявлена.
- **Дубликаты:** нигде не упоминаются [стр.].
- **Google Sheets:** нет. Блог самой KasKecil пишет, что KasKecil и Rekapin «memakai dashboard bawaan aplikasi sendiri», а MoneyBot и Spendy пишут в «Google Sheets milik pengguna sendiri» [стр.] ([блог KasKecil, сравнение от 2026-09-08](https://kaskecil.id/blog/bot-telegram-pencatat-keuangan)).
- Android-приложение «KasKecil Mobile»: 10+ установок, рейтинга нет [стр.] ([Google Play](https://play.google.com/store/apps/details?id=id.kaskecil.kas_kecil_mobile)).

**Остальные боты по данным блога KasKecil** [стр. блога, сами сайты не открывал] ([блог](https://kaskecil.id/blog/bot-telegram-pencatat-keuangan)):
- **Rekapin**: Telegram, свой дашборд, Free (100 транзакций/мес) + **Premium Rp29.000/мес или Rp175.000/год**. Целится в физлиц, фрилансеров и малый бизнес.
- **MoneyBot**: данные в Google Sheets пользователя, разовая оплата Rp150.000–550.000 или подписка Rp25.000/мес.
- **Spendy**: Google Sheets пользователя («100% kepemilikan data»), ядро бесплатно, цена Pro не опубликована.

**Другие** (только [сниппет]): Mingo ([mingo.id](https://mingo.id/), «Catat Keuangan Otomatis Lewat WhatsApp, Gratis»), BotMoni ([botmoni.com](https://botmoni.com/)), CatatAja ([catataja.id](https://catataja.id/)), Ikisae ([ikisae.com](https://ikisae.com/)), Rekafin ([rekafin.id](https://rekafin.id/), фото чеков только в платных планах), Litra ([litra.litegral.com](https://litra.litegral.com/), Google Spreadsheet в платном плане). Цены не проверены.

**Вывод по Индонезии.**
- Бухгалтерские системы стоят Rp160–400 тыс./мес (около $10–25): Kledo Pro Rp159.900, Jurnal Essentials Rp299.250, Accurate Rp333.000, majoo Rp249.000. Распознавания чеков ни у одной нет.
- Единственный крупный игрок с OCR и антидублями, Mekari Expense, стоит от Rp1,5 млн/мес (минимум 50 сотрудников по Rp30.000) и работает через своё приложение.
- Чат-боты (KasKecil Rp149 тыс., Rekapin Rp29 тыс.) рассчитаны на одного пользователя. Групповой работы, дубликатов и Google Sheets владельца у них нет (у KasKecil проверено; Sheets есть у MoneyBot и Spendy, но без групп и дублей).

---

## 2. Telegram/WhatsApp-боты для бизнес-сбора чеков (вне уже изученного списка)

Все строки [сниппет]: эти сайты во втором проходе не открывались.

| Продукт | Что делает | Группа | Дубликаты | Таблица | Цена | Ссылка |
|---|---|---|---|---|---|---|
| Tailride | Счета и чеки через Telegram и WhatsApp → QuickBooks, Xero, Odoo, Business Central | Не указано | Да: повторная отправка не обрабатывается и не тарифицируется | Нет | Free 10 счетов/мес | [tailride.so](https://tailride.so/integrations/telegram), [блог](https://tailride.so/blog/capture-invoices-whatsapp-telegram) |
| ProverkaCheka (Казахстан) | Проверка чеков Kaspi по QR | Да, общая база в групповом чате; «бот покажет дубликат» | Да | CSV | Не найдена | [proverkacheka.kz/blog](https://proverkacheka.kz/blog/telegram-bot-gruppa-nastrojka/) |
| Project Receipts Bot | Чеки участников → Google Таблицы и Drive | Участники проекта | Не указано | Google Sheets | Не указана | [roksana870.github.io](https://roksana870.github.io/) |
| Бухгалтерия NurTech | Голос → Google-таблица, отчёты в Telegram | — | — | Google Sheets | — | [buh.nurtech.dev](https://buh.nurtech.dev/) |
| ExpenseBot | Командный план $10/пользователь/мес (листинг читается плохо) | — | — | — | — | [xpay.sh](https://www.xpay.sh/saas-pricing/expensebot/) |

DIY-субституты [сниппет]: шаблоны n8n «Telegram → OCR/LLM → Google Sheets» с проверкой дублей ([n8n 19225, чеки сотрудников](https://n8n.io/workflows/19225-track-employee-expense-receipts-from-telegram-with-gpt-4o-mini-and-google-sheets), [n8n 20026, кнопки «Add anyway / Ignore»](https://n8n.io/workflows/20026-log-german-vat-ready-expense-receipts-via-telegram-with-openai-and-google-sheets/)); open source: [bendorshai/expenses_bot](https://github.com/bendorshai/expenses_bot) (группа Telegram → Sheets), [dararafida/bot_tracking_financial](https://github.com/dararafida/bot_tracking_financial) (группа WhatsApp → Sheets), [rhandyta/kasbot-ai](https://github.com/rhandyta/kasbot-ai) (Индонезия, WhatsApp, OCR, «kemungkinan duplikat»).

**Новое о глобальном игроке:** в Zoho Expense Standard теперь есть «Integration with WhatsApp, Slack» с пометкой NEW и «AI powered expense Audit- Fraud and Alcohol detection» [стр.] ([zoho pricing](https://www.zoho.com/us/expense/pricing/)).

---

## 3. Перепроверка цен (2026-11-11)

| Продукт | Было у нас | Сейчас на странице вендора | Изменилось? |
|---|---|---|---|
| **REME** ([reimburseme.ai/pricing](https://reimburseme.ai/pricing)) | $5 / $8 за пользователя в месяц | [стр.] Starter **$5 /user/month**, Growth **$8 /user/month**, «Billed monthly · Active users only»; Enterprise по запросу. Годовая оплата со скидкой 15%. **Триал 1 месяц, без карты** (весь функционал Growth). Starter: подача чеков в WhatsApp без лимита, «99.9% AI OCR», 3 AI-агента против фрода; Growth: 6 агентов, мультивалютность, мультиязычность. Внедрение включено | Цены те же. Изменились условия триала: GoodFirms писал 7 дней с картой, теперь месяц без карты. Слоган (H1): «Automate expense claims. Catch fraud before you pay it.» |
| **Dext Business** ([dext.com/us/pricing](https://www.dext.com/us/pricing/prepare-direct)) | $31,50/мес за 250 документов | [стр.] **$25,21/мес при годовой оплате ($302,50/год)**, USD без налога, 5 пользователей, 250 документов/мес; «Up to 20% cheaper with an annual subscription». Помесячная цена рендерится JS и в HTML не видна: $31,50 остаётся [сниппет] (25,21 / 0,8 = 31,51, это сходится). Новый add-on «AI Assist $10.5 per month until 31 Jan 2027» | Без изменений. Месячная $31,50 по-прежнему не проверена напрямую |
| **Zoho Expense** ([zoho.com/us/expense/pricing](https://www.zoho.com/us/expense/pricing/)) | $3/user | [стр.] Free $0 (до 3 пользователей, 20 сканов на пользователя в месяц); **Standard $4/user/мес помесячно, $3 при годовой оплате** (200 сканов на пользователя в месяц, «Itemised Receipt capture with AI-powered OCR in 38+ languages», «Integration with WhatsApp, Slack» NEW, AI-аудит фрода); **Premium $6 / $5** (1000 сканов). Цены без налогов, триал 14 дней | $3 действует только при годовой оплате. Новое: интеграция с WhatsApp в Standard; у Premium помесячная цена $6 |
| **Hubdoc** ([hubdoc.com/pricing](https://www.hubdoc.com/pricing)) | $12/мес | [стр.] **$12 USD в месяц** после бесплатных 30 дней без карты; «Unlimited usage», несколько пользователей, синхронизация с Xero и QuickBooks Online | Без изменений. Цифра $20 с G2 и ITQlick на сайте не подтверждается |

---

## 4. Отзывы Google Play

**Ограничение.** Без JS Play отдаёт только 3 отзыва на язык интерфейса. Я прочитал id- и en-версию страниц, это по 6 отзывов на приложение. Остальное подгружается JS, массово выгружать отзывы я не стал. Поэтому **все темы ниже thin (меньше 3 отзывов)**, кроме отмеченной. Количество в скобках означает число отзывов из прочитанных шести. Темы 4★ с «но» не найдены: в выборке четвёрок не было.

### 4.1 BukuWarung: 3,2★, 94,7 тыс. отзывов, 35% единиц ([Play](https://play.google.com/store/apps/details?id=com.bukuwarung))
Само распределение звёзд — сильный сигнал: 32.832 единицы из ~93,6 тыс.
- **Потеря или недоступность данных (2, thin)**: «aplikasinya tdk sengaja ter uninstal. stelah di instal ulang catatan pmbukuannya hilang» (22.08.2026); «aplikasi nya tiba tiba keluar sendiri??? Dan saat masuk kembali, data nya lemot» (30.08.2026).
- **Деградация от новых функций, баги, неточные отчёты (2, thin)**: «getting new features that I never use, and it's getting less and less convenient» (10.02.2022, 241 человек отметил отзыв полезным); «Lot's of feature inconsistency, bugs, un-accurate reporting when using date filters» (14.08.2021).
- **Навязчивая верификация (1, thin)**, отзыв от балийского бизнеса «Bali Vacation Services Jimbaran»: «noticed to verify for the third time» (12.12.2022).
- Ответы разработчика шаблонные: «hubungi CS / WhatsApp».

### 4.2 Mekari Jurnal: 4,5★, 1,28 тыс. отзывов, 110 единиц ([Play](https://play.google.com/store/apps/details?id=id.jurnal.mobile))
- **Ошибки и сбои + медленная поддержка (2, thin)**: «Makin kesini makin sering error, input purchase invoice stok ga nambah» (08.12.2022); «Sistem jurnal suka error terus… sudah 3 hari lapor tetap masih error» (22.10.2022).
- **Мобильное приложение беднее веб-версии (3, на границе thin)**: «many functions we see on the browser are not exist at the app» (19.02.2019); «not as feature-rich as the desktop version… can feel a bit slow» (23.01.2025); «Too many details being left out» (18.03.2021).
- **OTP при входе не приходит (1, thin)**: «drama otp yg tidak kunjung dikirimkan, saat akan login» (10.08.2026).

### 4.3 Mekari Expense: 4,6★, 102 отзыва, 8 единиц ([Play](https://play.google.com/store/apps/details?id=com.mekari))
- **Нестабильность: падения и ошибки загрузки (2, thin)**: «Sering trouble saat loading. "Something went wrong ... please reload..."» (14.05.2024); «jelek bgt lgs auto close ga bs dibuka» (12.08.2025).
- Позитив (3 пятёрки, июль–сентябрь 2025): удобство reimbursement и автоаудит, «Semua pengeluaran team langsung terekam dan sudah langsung diaudit otomatis» (30.07.2025). Многие пятёрки пришли кучно в июле–сентябре 2025 и получили одинаковые ответы от Mekari. Это наблюдение, а не вывод о накрутке.

Следующий шаг, если нужны настоящие подсчёты: открыть «Lihat semua ulasan» в браузере вручную, отфильтровать 1–3★ и прочитать 30–50 отзывов на приложение.

---

## 5. Есть ли уже «бот в существующей группе + дубликаты + Google Sheets владельца»?

Готового коммерческого продукта со всеми тремя признаками не найдено.
- **KasKecil.id** [стр.]: Индонезия, WhatsApp/Telegram, OCR, Rp149 тыс./мес. Групп нет, дубликатов нет, Sheets нет (свой дашборд).
- **Mekari Expense** [стр.]: OCR + дубликаты (7 дней, fuzzy). Своё приложение, мессенджера и Sheets нет, от Rp1,5 млн/мес.
- **REME** [стр.]: WhatsApp + антифрод, $5–8 за пользователя. Работу в групповых чатах страница цен не упоминает (как именно идёт подача, в личке или в группе, я не проверял). Google Sheets в списке интеграций нет (QuickBooks, Xero, NetSuite и др.).
- **Zoho Expense** [стр.]: теперь с интеграцией WhatsApp и AI-аудитом, $3–4 за пользователя. Sheets нет.
- **MoneyBot / Spendy** [стр. блога KasKecil]: Google Sheets пользователя. Ни групп, ни дубликатов не заявлено.
- **ProverkaCheka** [сниппет]: группа + дубликаты, но только чеки Kaspi, CSV.
- **Tailride** [сниппет]: Telegram + дубликаты, выгрузка в учётные системы.
- Все три признака есть только в **DIY-шаблонах n8n и open source**.
