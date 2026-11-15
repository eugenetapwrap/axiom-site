# Бот: описание в BotFather и первое сообщение (/start)

Правки 15.11 к текстам основателя (первая строка описания — «по документам», так решил основатель): 30 документов вместо 40, «дубли» как на сайте, «Google Диск» полностью, опечатка «дуругие», в описание добавлен первый шаг и бесплатный объём, к условиям — политика конфиденциальности.

## Описание до /start (BotFather → Edit Description, до 512 знаков)

**RU** (444 знак)
```
Nota ведёт учёт расходов по документам в Telegram.

• Читает чеки, счета, скриншоты переводов и рукописные накладные на любом языке
• Записывает в вашу Google-таблицу: дата, сумма, поставщик, категория, проект
• Складывает оригиналы в папку на вашем Google Диске под номером строки
• Отмечает дубли и суммы, которые не сходятся
• Присылает отчёты за неделю и месяц

Пришлите архив рабочего чата и получите отчёт. Первые 30 документов бесплатно.
```

**EN** (448)
```
Nota tracks expenses from your documents in Telegram.

• Reads receipts, invoices, transfer screenshots and handwritten delivery notes in any language
• Writes them to your Google Sheet: date, amount, supplier, category, project
• Saves originals to a folder on your Google Drive, numbered by row
• Flags duplicates and totals that don't add up
• Sends weekly and monthly reports

Send a work chat archive and get a report. First 30 documents free.
```

**ID** (453)
```
Nota mencatat pengeluaran dari dokumen Anda di Telegram.

• Membaca struk, invoice, bukti transfer, dan nota tulisan tangan dalam bahasa apa pun
• Mencatat ke Google Sheet Anda: tanggal, jumlah, pemasok, kategori, proyek
• Menyimpan file asli ke folder di Google Drive Anda sesuai nomor baris
• Menandai duplikat dan jumlah yang tidak cocok
• Mengirim laporan mingguan dan bulanan

Kirim arsip chat kerja dan dapatkan laporan. 30 dokumen pertama gratis.
```

## Короткое описание в профиле (BotFather → Edit About, до 120 знаков)

- RU: `Учёт расходов по документам в Telegram: Google-таблица, дубли, отчёты. 30 документов бесплатно.`
- EN: `Expense tracking from documents in Telegram: Google Sheet, duplicates, reports. First 30 documents free.`
- ID: `Catat pengeluaran dari dokumen di Telegram: Google Sheet, duplikat, laporan. 30 dokumen pertama gratis.`

## Первое сообщение после /start

Задача одна: человек сразу видит два пути — прислать чат или подключить Google — и кнопку под каждый. Что умеет Nota, он уже прочитал в описании до /start, здесь это не повторяем.

**RU**
```
👋 Привет! Я Nota — веду учёт расходов по вашим документам.

С чего начать:
1. Пришлите архив рабочего чата или перешлите чеки — подготовлю отчёт.
2. Подключите Google — создам таблицу и две папки на вашем Google Диске. Доступ у меня будет только к ним.

Первые 30 документов бесплатно.

Подключая Google, вы принимаете условия и политику конфиденциальности.

[📦 Как выгрузить чат]  [📊 Подключить Google]
```
«условия» и «политику конфиденциальности» — ссылки. Отдельную ссылку «Как работает Nota» убрали: лишний пункт на первом экране.

**EN**
```
👋 Hi! I'm Nota — I track expenses from your documents.

Where to start:
1. Send a work chat archive or forward receipts — I'll prepare a report.
2. Connect Google — I'll create a sheet and two folders on your Google Drive. I'll only have access to them.

First 30 documents are free.

By connecting Google, you accept the terms and privacy policy.

[📦 How to export a chat]  [📊 Connect Google]
```

**ID**
```
👋 Halo! Saya Nota — mencatat pengeluaran dari dokumen Anda.

Mulai dari mana:
1. Kirim arsip chat kerja atau teruskan struk — saya siapkan laporannya.
2. Hubungkan Google — saya buat sheet dan dua folder di Google Drive Anda. Akses saya hanya ke situ.

30 dokumen pertama gratis.

Dengan menghubungkan Google, Anda menyetujui ketentuan dan kebijakan privasi.

[📦 Cara ekspor chat]  [📊 Hubungkan Google]
```

## Ответ на кнопку «Как выгрузить чат» (предложение)

```
Как выгрузить чат:

Telegram — только с компьютера: откройте чат → ⋮ → «Экспорт истории чата» → оставьте «Фото» и «Файлы» → сожмите папку в ZIP и пришлите сюда.

WhatsApp — с телефона: откройте чат → «Экспорт чата» → «С медиафайлами» → отправьте сюда.

Нет архива? Просто перешлите чеки по одному.
```

## Проверить в боте
- Telegram Desktop сохраняет экспорт папкой, а не одним файлом: шаг «сожмите папку в ZIP» уже в ответе на кнопку — проверить, что бот принимает такой ZIP.
- Какая вторая папка из «двух папок»? На сайте сейчас «в папку» (шаг 3) и «к таблице и двум папкам» («Ваши данные») — выровнять по ответу (аудит, вопрос 18).
- Ссылка на политику конфиденциальности нужна и для проверки приложения в Google.
