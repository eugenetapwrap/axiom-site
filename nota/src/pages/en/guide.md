---
layout: ../../layouts/Doc.astro
title: How to use Nota
description: How to get started, how to send documents, what each column in the sheet means and what to do with the entries.
updated: '25 November 2026'
lang: en
slug: guide
---

Nota helps you keep your business expenses under control. You send receipts, invoices and payment screenshots in Telegram, and Nota reads them, checks them for duplicates and errors and records them in your Google Sheet. You don't need to type anything in by hand.

Nota does not do accounting and does not replace an accountant. It is about control: what you paid, to whom, for what, and whether you paid twice.

## 1. Getting started

1. Open [@NotaGetBot](https://t.me/NotaGetBot) in Telegram and tap “Start”.
2. Tap “Connect Google” and sign in to your account. Nota will create a sheet and a folder for documents in your Google Drive. To open the sheet: /table. Google account and folder: /google.
3. Send your first document or add Nota to a work group.

The first 30 documents are free, no card needed. Your plan and documents left: /subscription.

If you don't connect Google, you will only get the archive report. The sheet, notifications and scheduled reports work once Google is connected. Anything you send without Google is kept for 7 days: connect Google within that time, and everything will be recorded in the sheet.

## 2. How to send documents

### Directly to the bot

Take a photo of a receipt or invoice and send it to the bot. You can send a PDF or forward a message with a document from another chat, email or messenger. Files can be up to 50 MB. A minute later, the document is in the sheet.

### In a work group

Add Nota to the chat where your employees already send receipts. The /group command shows how to do this. Nothing changes for your employees: they don't need to sign in or register anywhere.

- Only the account owner can connect Nota to a group: expense data is confidential.
- When it is connected, Nota says hello to the members once. After that, it does not write in the group. It only puts ✍ on each document it records, so everyone can see that the receipt is counted.
- Nota takes only payment documents. It skips ordinary photos, drawings and chat messages.
- Nota tells only the owner about duplicates and errors, in a private message. It sends other messages to the group only with your permission.
- Each group gets its own Business Unit, for example a site, a villa or a shop, so expenses don't get mixed up.
- How many groups you can connect depends on your plan: Start — up to 5, Growth — up to 10, Scale — unlimited.

You can give partners access to the sheet, add Nota to a group they are already in, or forward them the weekly and monthly reports.

### As an archive of past months

Use the /import command. Send a ZIP archive with documents or an export of your work chat, up to 50 MB. You can export a chat in Telegram Desktop on a computer. Nota will process everything and show whether there were any duplicates before.

### What documents Nota understands

Any payment document that has an amount, a date and what the payment was for:

- bills and invoices from suppliers;
- receipts from shops, cafes and fuel stations;
- handwritten delivery notes and receipts, including ones in local languages;
- payment orders and screenshots of bank transfers;
- screenshots of orders from online shops;
- salary payment lists.

Photos, PDFs and ZIP archives up to 50 MB work, in any language. Nota reads even what a person can hardly read: faded thermal receipts, crumpled delivery notes, messy handwriting.

### How to take photos

- Photograph the whole document, in good light and without glare.
- One document per photo.
- Send a document with several pages as one PDF.

### Documents only

Nota records only what a document confirms. There is no voice or manual input: a message like “spent 500 on a taxi” without a receipt will not be recorded. An expense without a document cannot be checked, which means it cannot be controlled either.

## 3. What Nota does with each document

1. Recognises the type, the date, the amount, who was paid and what for.
2. Takes a digital fingerprint of the file and compares it with the documents already recorded.
3. Recalculates the amounts inside the document.
4. Records the document as a separate row in the sheet and puts the check result in the Check column.
5. Gives the file a clear name, puts it in a folder in your Google Drive and adds a link to it in the row.

If a screenshot confirms payment of an invoice that is already recorded, Nota will ask whether to record it as a separate row or skip it. You can save your choice, and the bot will stop asking. To change it: /proofs.

## 4. Columns in the sheet

The sheet has 14 columns, and their names are in English. You can edit any of them. A pencil ✎ in the header marks the columns you usually fill in. The options in the drop-down lists come from the References tab.

### Filled in by Nota

**ID · File** — the entry number and the document number, for example “14 · 5867486165572”. It is a link to the original in the folder in your Google Drive. The numbering is shared across private messages and all groups. If a document has no number, it shows “no-num”.

**Type** — the document type:

- **Invoice** — an invoice from a supplier;
- **Receipt** — a receipt;
- **Hand** — a handwritten document, for example a delivery note;
- **Proof** — proof of payment: a payment order or a transfer screenshot;
- **Statement** — a statement or a payment list;
- **Document** — another payment document.

**Reported By** — who sent the document.

**Date** — the date on the document, not the date it was sent.

**Amount** — the amount in the sheet currency; the currency is shown in the header, for example “Amount, IDR”. If a document is in another currency, Nota converts it at the exchange rate.

**Purpose** — what was paid for: the items from the document, short and in order.

**Payee** — who was paid: a shop, supplier, contractor or employee.

**Check** — the check result:

- **OK** — the document is new and everything matches. The amount is counted in the totals.
- **Review** — the document is accepted and counted in the totals, but you should check it: for example, the calculation does not add up or the document has corrections.
- **DBL** — a duplicate: this document is already recorded. It is not counted in the totals.

**Match** — a note on the check. For OK it is empty, for Review it is a “Comment→” link to the note in the Comments column, and for DBL it is the number of the first entry.

### Your columns

You don't have to fill them in: Nota works without them. Nota sets some of the values automatically.

**Status** — the payment status:

- **Paid** — paid. Nota sets it automatically if the document itself confirms payment: a receipt from a shop or a payment order. In other cases the column is empty.
- **To pay** — the invoice needs to be paid.
- **Rejected** — the row is not needed, for example a duplicate or a document sent by mistake. The row stays in the sheet but is left out of all totals, the dashboard and the reports.

**Category** — the expense category, for example Materials, Staff, Transport, Rent. Nota sets categories from its category list, and the set depends on your type of business (see section 8). If a different one fits, choose it from the drop-down list right in the row. List of categories: /category. The Monthly spend tab and the reports are built from this column.

**Business Unit** — what the expense belongs to. Nota puts the name of the group the document came from, or Personal if it was sent directly to the bot. You can change the value, and add your own sites, villas or shops on the References tab. The Monthly spend tab is filtered by this column.

**Account** — what you paid from: a bank account, a card or cash. The list is set on the References tab.

**Comments** — for entries marked Review, this says what to check. You can also add your own notes here.

## 5. What to do with entries

- **Review.** Open the original with the link in ID · File, read the note in Comments and fix the row if needed.
- **DBL.** Compare the row with the first entry; its number is in Match. Don't pay again, and set the duplicate's status to Rejected.
- **The invoice needs to be paid.** Set To pay, and after you pay, Paid.
- **Wrong category.** Choose the right one from the drop-down list in the Category column.
- **The expense belongs to a site.** Enter it in Business Unit. You can replace the group names with your own on the References tab.
- **Nota made a mistake.** Fix the row: the amount, description, payee, category, status or check result. Nota does not overwrite your changes, and the totals and the dashboard take them into account right away.
- **You don't need the row.** Set its status to Rejected: the row stays in the history but is not counted in the totals. You can also delete the whole row.

## 6. Dashboard and tabs

**Dashboard above the sheet.** Four figures that show the situation at a glance: how many payments are fine, how many are duplicates, how many are waiting for review and how many have no category. Each shows a count and an amount.

**Monthly spend** — spending by month as a cash flow: categories in rows, months in columns. At the top are three figures: this month's spending and the change from last month, total spending for the whole period, and the share of spending without a category. With the filters you can choose the payment status, the check result and the Business Unit. Duplicates are left out by default, and the largest expense item is highlighted.

**Insights** — things that need attention: payments many times larger than usual, invoices to pay by due date, duplicates that are still marked “To pay”, spending by employee and by payee.

**References** — lists for the drop-down menus: categories, Business Unit and payment accounts.

## 7. Notifications and reports

- **Notifications:** /notifications. Choose whether to get a card for every entry or only what needs attention: duplicates and documents to review.
- **On a schedule:** every Monday morning, a report for the past week; on the 1st of each month, a report for the past month.
- **On request:** /report. At any time you can request a report for the current week or month, even if it is not over yet, and also for the past month.

The report shows spending for the period and how it compares with the previous one, the average daily spending and the peak, spending by day and by category, how many duplicates were left out of spending and how many documents are waiting for review. The report is easy to forward to a partner or investor.

## 8. Extra features

**Any currency.** Choose the currency you track expenses in: /currency. Nota converts payments in other currencies at the exchange rate. You can change the currency at any time, and all entries, including old ones, will be recalculated.

**Checking past months.** Send an archive of documents or an export of your work chat with /import. Nota will show whether there were any duplicates and errors before.

**Categories for your business.** The list of 15 categories is based on IFRS and set up for 10 types of business, and also for personal and family expenses. Usually, somewhere between the 15th and the 30th document, Nota asks what your business does and picks the matching set:

- construction;
- villas and hotels;
- restaurants and cafes;
- trade;
- tourism;
- beauty and sports;
- services;
- manufacturing;
- transport and cars;
- events;
- personal and family finances;
- any other business where expenses are backed by receipts and invoices.

**Languages.** You can send documents in any language. The bot speaks Russian, English and Indonesian, and the language is chosen from your Telegram settings. To change it: /language. The sheet is kept in English.

**Analytics.** The sheet is broken down by category, payee, document type and Business Unit, so it is easy to analyse. For example, Gemini, built into Google Sheets, can suggest and build reports for you: who you pay the most and how prices change, which employees spend money and on what, which site costs more and what is growing faster.

**Working together.** You can share the sheet with partners, managers or an investor, like any Google file.

## 9. Common situations

- **Need to disconnect a group:** remove Nota from that group.
- **Have a question or something is wrong:** /support or the support bot [@NotaSuppBot](https://t.me/NotaSuppBot). We reply within 24 hours.
- **Want to delete your data:** /delete_all. Nota will delete the records of your documents and the fingerprints, disconnect from Google and leave all groups. The sheet and the documents folder in your Google Drive stay with you.
- **Want to start over:** /start.

## 10. Bot commands

All commands are in the bot menu.

**Main**

- /report — weekly or monthly report
- /table — open the sheet
- /google — Google account and folder
- /group — connect a work group
- /import — upload a document archive
- /subscription — plan and documents left

**Settings**

- /settings — all settings
- /currency — sheet currency
- /language — bot language
- /notifications — which notifications to get
- /category — list of categories
- /proofs — how to handle payment proofs
- /delete_all — delete my data

**Help**

- /start — start over
- /support — write to the Nota team

## 11. Frequently asked questions

**Is this accounting?** No. Nota does not calculate taxes or file reports. It helps the owner keep control of the money, and a ready sheet with the original documents will save your accountant time.

**Where is my data stored?** The sheet and the files are in your Google Drive, and you decide who has access to them. Nota sees only the sheet and the folder it created. We keep documents only while they are being processed, and we store only file fingerprints, to find duplicates.

**What will employees see in the group?** One greeting when Nota is connected, and ✍ on recorded receipts. Nota does not post amounts, duplicates or notes in the group.

**What if Nota makes a mistake?** Fix the row in the sheet. Your changes will stay, and the totals will be recalculated.

## Who makes Nota

Nota was built by the team of finance professionals at Axiom Consulting: more than 15 years of expense control and financial modelling for real estate development, construction and IT projects. Nota is based on the company's own payment control system, which already works for the company's clients. More than 100,000 documents have gone through it.

---

By using Nota, you accept the [Terms of Service](/en/terms) and the [Privacy Policy](/en/privacy). More about Nota is on the [home page](/).
