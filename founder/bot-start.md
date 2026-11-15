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

Цель онбординга (основатель, 15.11): человек подключает Google и видит свою таблицу. Самое лёгкое действие — первым: подключить Google в одно касание и переслать любой чек, который уже есть в телефоне, — через минуту он строкой в таблице. Архив — для тех, у кого есть документы за прошлые месяцы: «соберу завтра» не должно стоять на пути к первому результату.

**RU**
```
👋 Привет! Я Nota — веду учёт расходов по вашим документам.

Разбираю чеки, счета и рукописные накладные, записываю их в вашу Google-таблицу и отмечаю дубли и ошибки в суммах.

Начнём за минуту:
1. Подключите Google — создам на вашем Google Диске таблицу и две папки (доступ только к ним).
2. Перешлите сюда любой чек — через минуту он появится строкой в таблице.

Есть документы за прошлые месяцы? Пришлите ZIP-архив — папку или выгрузку чата, и я сделаю отчёт.

Первые 30 документов бесплатно.
Подключая Google, вы принимаете условия и политику конфиденциальности.

[📊 Подключить Google]
[📦 Как собрать архив]
```

**EN**
```
👋 Hi! I'm Nota — I track expenses from your documents.

I read receipts, invoices and handwritten delivery notes, write them to your Google Sheet and flag duplicates and wrong totals.

Let's start in a minute:
1. Connect Google — I'll create a sheet and two folders on your Google Drive (access to them only).
2. Forward any receipt here — in a minute it will appear as a row in the sheet.

Have documents from past months? Send a ZIP archive — a folder or a chat export, and I'll make a report.

First 30 documents are free.
By connecting Google, you accept the terms and privacy policy.

[📊 Connect Google]
[📦 How to make an archive]
```

**ID**
```
👋 Halo! Saya Nota — mencatat pengeluaran dari dokumen Anda.

Saya membaca struk, invoice, dan nota tulisan tangan, mencatatnya ke Google Sheet Anda, dan menandai duplikat serta jumlah yang salah.

Mulai dalam semenit:
1. Hubungkan Google — saya buat sheet dan dua folder di Google Drive Anda (akses hanya ke situ).
2. Teruskan struk apa saja ke sini — dalam semenit struk itu muncul sebagai baris di sheet.

Punya dokumen bulan-bulan sebelumnya? Kirim arsip ZIP — folder atau ekspor chat, dan saya buatkan laporan.

30 dokumen pertama gratis.
Dengan menghubungkan Google, Anda menyetujui ketentuan dan kebijakan privasi.

[📊 Hubungkan Google]
[📦 Cara membuat arsip]
```

## Ответы бота на первых шагах (предложение, RU)

Каждый ответ говорит, что произошло, и подводит к следующему шагу. В ⟨⟩ — подставляет бот.

**Google подключён**
```
✅ Таблица готова: ⟨ссылка на таблицу⟩
Перешлите сюда любой чек — через минуту он появится в таблице.
```

**Получил документ (Google подключён)**
```
✍ Записал в таблицу, строка ⟨12⟩: ⟨2 450 000 IDR⟩, ⟨TB Sumber Rejeki⟩.
Документов: ⟨3⟩ из 30 бесплатных. Отчёт придёт после 30 — или нажмите «Отчёт», чтобы получить его сейчас.
```

**Получил документ (Google не подключён)**
```
✍ Записал: ⟨2 450 000 IDR⟩, ⟨TB Sumber Rejeki⟩.
Подключите Google, чтобы видеть все документы в своей таблице.

[📊 Подключить Google]
```

**Получил архив**
```
📦 Архив получил: ⟨47⟩ файлов. Разбираю — отчёт пришлю примерно через 15 минут.
В бесплатный отчёт войдут первые 30 документов.
```
Если Google не подключён, добавить: «Подключите Google — и документы из архива сразу попадут в таблицу. [📊 Подключить Google]».

**Прислал отчёт (Google ещё не подключён)**
```
Это ваш первый отчёт ☝️
Подключите Google — и все документы будут в вашей таблице, а оригиналы в папке. Без Google присланное хранится 10 дней.

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
