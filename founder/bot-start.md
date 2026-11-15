# Бот: описание в BotFather и первое сообщение (/start)

Правки 15.11 к текстам основателя (первая строка описания — «по документам», так решил основатель): 30 документов вместо 40, «дубли» как на сайте, «Google Диск» полностью, опечатка «дуругие», в описание добавлен первый шаг и бесплатный объём, к условиям — политика конфиденциальности.

## Описание до /start (BotFather → Edit Description, до 512 знаков)

**RU** (462 знак)
```
Nota ведёт учёт расходов по документам в Telegram.

• Читает чеки, счета, скриншоты переводов и рукописные накладные на любом языке
• Записывает в вашу Google-таблицу: дата, сумма, поставщик, категория, проект
• Складывает оригиналы в папку на вашем Google Диске под номером строки
• Отмечает дубли и суммы, которые не сходятся
• Присылает отчёты за неделю и месяц

Пришлите фото, PDF или ZIP-архив с документами и получите отчёт. Первые 30 документов бесплатно.
```

**EN** (471)
```
Nota tracks expenses from your documents in Telegram.

• Reads receipts, invoices, transfer screenshots and handwritten delivery notes in any language
• Writes them to your Google Sheet: date, amount, supplier, category, project
• Saves originals to a folder on your Google Drive, numbered by row
• Flags duplicates and totals that don't add up
• Sends weekly and monthly reports

Send photos, PDFs or a ZIP archive of documents and get a report. First 30 documents free.
```

**ID** (477)
```
Nota mencatat pengeluaran dari dokumen Anda di Telegram.

• Membaca struk, invoice, bukti transfer, dan nota tulisan tangan dalam bahasa apa pun
• Mencatat ke Google Sheet Anda: tanggal, jumlah, pemasok, kategori, proyek
• Menyimpan file asli ke folder di Google Drive Anda sesuai nomor baris
• Menandai duplikat dan jumlah yang tidak cocok
• Mengirim laporan mingguan dan bulanan

Kirim foto, PDF, atau arsip ZIP berisi dokumen dan dapatkan laporan. 30 dokumen pertama gratis.
```

## Короткое описание в профиле (BotFather → Edit About, до 120 знаков)

- RU: `Учёт расходов по документам в Telegram: Google-таблица, дубли, отчёты. 30 документов бесплатно.`
- EN: `Expense tracking from documents in Telegram: Google Sheet, duplicates, reports. First 30 documents free.`
- ID: `Catat pengeluaran dari dokumen di Telegram: Google Sheet, duplikat, laporan. 30 dokumen pertama gratis.`

## Первое сообщение после /start

Задача одна: человек сразу видит два пути — прислать документы (любые: фото, PDF, ZIP с папкой или выгрузкой чата) или подключить Google — и кнопку под каждый. Что умеет Nota, он уже прочитал в описании до /start, здесь это не повторяем.

**RU**
```
👋 Привет! Я Nota — веду учёт расходов по вашим документам.

С чего начать:
1. Пришлите документы: фото, PDF или ZIP-архив (папку с чеками, выгрузку чата) — подготовлю отчёт.
2. Подключите Google — создам таблицу и две папки на вашем Google Диске. Доступ у меня будет только к ним.

Первые 30 документов бесплатно.

Подключая Google, вы принимаете условия и политику конфиденциальности.

[📦 Как собрать архив]  [📊 Подключить Google]
```
«условия» и «политику конфиденциальности» — ссылки. Отдельную ссылку «Как работает Nota» убрали: лишний пункт на первом экране.

**EN**
```
👋 Hi! I'm Nota — I track expenses from your documents.

Where to start:
1. Send documents: photos, PDFs or a ZIP archive (a folder of receipts, a chat export) — I'll prepare a report.
2. Connect Google — I'll create a sheet and two folders on your Google Drive. I'll only have access to them.

First 30 documents are free.

By connecting Google, you accept the terms and privacy policy.

[📦 How to make an archive]  [📊 Connect Google]
```

**ID**
```
👋 Halo! Saya Nota — mencatat pengeluaran dari dokumen Anda.

Mulai dari mana:
1. Kirim dokumen: foto, PDF, atau arsip ZIP (folder struk, ekspor chat) — saya siapkan laporannya.
2. Hubungkan Google — saya buat sheet dan dua folder di Google Drive Anda. Akses saya hanya ke situ.

30 dokumen pertama gratis.

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
- Telegram Desktop сохраняет экспорт папкой, а не одним файлом: шаг «сожмите папку в ZIP» уже в ответе на кнопку — проверить, что бот принимает такой ZIP.
- Какая вторая папка из «двух папок»? На сайте сейчас «в папку» (шаг 3) и «к таблице и двум папкам» («Ваши данные») — выровнять по ответу (аудит, вопрос 18).
- Ссылка на политику конфиденциальности нужна и для проверки приложения в Google.
