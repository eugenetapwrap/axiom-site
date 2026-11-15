# Бот: описание в BotFather и первое сообщение (/start)

Правки 15.11 к текстам основателя (первая строка описания — «по документам», так решил основатель): 30 документов вместо 40, «дубли» как на сайте, «Google Диск» полностью, опечатка «дуругие», в описание добавлен первый шаг и бесплатный объём, к условиям — политика конфиденциальности.

## Описание до /start (BotFather → Edit Description, до 512 знаков)

**RU** (448 знак)
```
Nota ведёт учёт расходов по документам в Telegram.

• Читает чеки, счета, скриншоты переводов и рукописные накладные на любом языке
• Записывает в вашу Google-таблицу: дата, сумма, поставщик, категория, проект
• Складывает оригиналы в папку на вашем Google Диске под номером строки
• Отмечает дубли и суммы, которые не сходятся
• Присылает отчёты за неделю и месяц

Пришлите ZIP-архив с документами и получите отчёт. Первые 30 документов бесплатно.
```

**EN** (455)
```
Nota tracks expenses from your documents in Telegram.

• Reads receipts, invoices, transfer screenshots and handwritten delivery notes in any language
• Writes them to your Google Sheet: date, amount, supplier, category, project
• Saves originals to a folder on your Google Drive, numbered by row
• Flags duplicates and totals that don't add up
• Sends weekly and monthly reports

Send a ZIP archive of documents and get a report. First 30 documents free.
```

**ID** (461)
```
Nota mencatat pengeluaran dari dokumen Anda di Telegram.

• Membaca struk, invoice, bukti transfer, dan nota tulisan tangan dalam bahasa apa pun
• Mencatat ke Google Sheet Anda: tanggal, jumlah, pemasok, kategori, proyek
• Menyimpan file asli ke folder di Google Drive Anda sesuai nomor baris
• Menandai duplikat dan jumlah yang tidak cocok
• Mengirim laporan mingguan dan bulanan

Kirim arsip ZIP berisi dokumen dan dapatkan laporan. 30 dokumen pertama gratis.
```

## Короткое описание в профиле (BotFather → Edit About, до 120 знаков)

- RU: `Учёт расходов по документам в Telegram: Google-таблица, дубли, отчёты. 30 документов бесплатно.`
- EN: `Expense tracking from documents in Telegram: Google Sheet, duplicates, reports. First 30 documents free.`
- ID: `Catat pengeluaran dari dokumen di Telegram: Google Sheet, duplikat, laporan. 30 dokumen pertama gratis.`

## Первое сообщение после /start

Главное на онбординге — человек не путается и получает обещанный результат: **отчёт**. Поэтому один путь к отчёту (архивом или по одному + кнопка «Отчёт»), а Google — следующий шаг: для первого отчёта он не нужен (на сайте: «Отчёт придёт и без Google»).

**RU**
```
👋 Привет! Я Nota — веду учёт расходов по вашим документам.

Разбираю чеки, счета и рукописные накладные, записываю их в Google-таблицу и отмечаю дубли и ошибки в суммах.

Как получить первый отчёт:
• Пришлите ZIP-архив — папку с чеками или выгрузку чата. Отчёт придёт сам.
• Или перешлите несколько чеков по одному и нажмите «Отчёт».

Первые 30 документов бесплатно.

Потом подключите Google — и каждый новый документ будет сам попадать в вашу таблицу.
Подключая Google, вы принимаете условия и политику конфиденциальности.

[📦 Как собрать архив]  [📊 Подключить Google]
```

**EN**
```
👋 Hi! I'm Nota — I track expenses from your documents.

I read receipts, invoices and handwritten delivery notes, write them to a Google Sheet and flag duplicates and wrong totals.

How to get your first report:
• Send a ZIP archive — a folder of receipts or a chat export. The report will come by itself.
• Or forward a few receipts one by one and tap «Report».

First 30 documents are free.

Then connect Google — and every new document will go to your sheet automatically.
By connecting Google, you accept the terms and privacy policy.

[📦 How to make an archive]  [📊 Connect Google]
```

**ID**
```
👋 Halo! Saya Nota — mencatat pengeluaran dari dokumen Anda.

Saya membaca struk, invoice, dan nota tulisan tangan, mencatatnya ke Google Sheet, dan menandai duplikat serta jumlah yang salah.

Cara mendapatkan laporan pertama:
• Kirim arsip ZIP — folder struk atau ekspor chat. Laporan akan datang sendiri.
• Atau teruskan beberapa struk satu per satu lalu tekan «Laporan».

30 dokumen pertama gratis.

Setelah itu hubungkan Google — setiap dokumen baru akan otomatis masuk ke sheet Anda.
Dengan menghubungkan Google, Anda menyetujui ketentuan dan kebijakan privasi.

[📦 Cara membuat arsip]  [📊 Hubungkan Google]
```

## Ответы бота на первых шагах (предложение, RU)

Чтобы человек на каждом шаге понимал, что происходит и что дальше. В ⟨⟩ — подставляет бот.

**Получил архив**
```
📦 Архив получил: ⟨47⟩ файлов. Разбираю — отчёт пришлю примерно через 15 минут.
В бесплатный отчёт войдут первые 30 документов.
```

**Получил документ по одному**
```
✍ Записал: ⟨2 450 000 IDR⟩, ⟨TB Sumber Rejeki⟩.
Документов: ⟨3⟩ из 30 бесплатных. Отчёт придёт после 30 — или нажмите «Отчёт», чтобы получить его сейчас.
```

**Прислал отчёт (Google ещё не подключён)**
```
Это ваш первый отчёт ☝️
Подключите Google — и каждый новый документ будет сам попадать в таблицу, а оригиналы в папку. Без Google присланное хранится 10 дней.

[📊 Подключить Google]
```

## Ответ на кнопку «Как собрать архив» (предложение)

```
Как собрать архив:

Папка с документами — сожмите её в ZIP и пришлите сюда.

Чат Telegram — с компьютера: откройте чат → ⋮ → «Экспорт истории чата» → оставьте «Фото» и «Файлы» → сожмите папку в ZIP и пришлите.

Чат WhatsApp — с телефона: откройте чат → «Экспорт чата» → «С медиафайлами» → отправьте сюда.

Архива нет? Пересылайте документы по одному.
```

## Проверить в боте
- Есть ли у бота кнопка «Отчёт» (на неё ссылается первое сообщение и сайт: «В любое время — по кнопке «Отчёт»»).
- Telegram Desktop сохраняет экспорт папкой, а не одним файлом: шаг «сожмите папку в ZIP» уже в ответе на кнопку — проверить, что бот принимает такой ZIP.
- Какая вторая папка из «двух папок»? На сайте сейчас «в папку» (шаг 3) и «к таблице и двум папкам» («Ваши данные») — выровнять по ответу (аудит, вопрос 18).
- Ссылка на политику конфиденциальности нужна и для проверки приложения в Google.
