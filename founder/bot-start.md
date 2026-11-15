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

Сначала две строки — что это за продукт (человек мог прийти по ссылке и не видеть описания), потом два пути — прислать документы (любые: фото, PDF, ZIP с папкой или выгрузкой чата) или подключить Google — и кнопку под каждый.

**RU**
```
👋 Привет! Я Nota — веду учёт расходов по вашим документам.

Разбираю чеки, счета и рукописные накладные, записываю их в вашу Google-таблицу и отмечаю дубли и ошибки в суммах. Каждую неделю и месяц присылаю отчёт.

С чего начать:
1. Пришлите ZIP-архив — папку с чеками или выгрузку чата, и я подготовлю отчёт. Первые 30 документов бесплатно.
2. Подключите Google — создам на вашем Google Диске таблицу и две папки (доступ только к ним) и буду записывать туда каждый документ.

Документы можно присылать и по одному — фото или PDF. Отчёт пришлю после 30 документов или в любой момент по кнопке «Отчёт».

Подключая Google, вы принимаете условия и политику конфиденциальности.

[📦 Как собрать архив]  [📊 Подключить Google]
```
«условия» и «политику конфиденциальности» — ссылки. Отдельную ссылку «Как работает Nota» убрали: лишний пункт на первом экране.

**EN**
```
👋 Hi! I'm Nota — I track expenses from your documents.

I read receipts, invoices and handwritten delivery notes, write them to your Google Sheet and flag duplicates and wrong totals. Every week and month I send you a report.

Where to start:
1. Send a ZIP archive — a folder of receipts or a chat export, and I'll prepare a report. First 30 documents are free.
2. Connect Google — I'll create a sheet and two folders on your Google Drive (access to them only) and record every document there.

You can also send documents one by one — photos or PDFs. I'll send a report after 30 documents or anytime with the «Report» button.

By connecting Google, you accept the terms and privacy policy.

[📦 How to make an archive]  [📊 Connect Google]
```

**ID**
```
👋 Halo! Saya Nota — mencatat pengeluaran dari dokumen Anda.

Saya membaca struk, invoice, dan nota tulisan tangan, mencatatnya ke Google Sheet Anda, dan menandai duplikat serta jumlah yang salah. Setiap minggu dan bulan saya kirim laporan.

Mulai dari mana:
1. Kirim arsip ZIP — folder struk atau ekspor chat, dan saya siapkan laporannya. 30 dokumen pertama gratis.
2. Hubungkan Google — saya buat sheet dan dua folder di Google Drive Anda (akses hanya ke situ) dan mencatat setiap dokumen di sana.

Dokumen juga bisa dikirim satu per satu — foto atau PDF. Laporan saya kirim setelah 30 dokumen atau kapan saja lewat tombol «Laporan».

Dengan menghubungkan Google, Anda menyetujui ketentuan dan kebijakan privasi.

[📦 Cara membuat arsip]  [📊 Hubungkan Google]
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
