---
layout: ../../layouts/Doc.astro
title: How to use Nota
description: How to get started, how to send documents and what to do with the sheet that Nota keeps.
updated: '25 November 2026'
lang: en
slug: guide
---

Nota records receipts, invoices and delivery notes in your Google Sheet, checks the amounts, finds duplicates and sends you reports. Below is everything you need to get started and understand your sheet.

## 1. Getting started

1. Open [@NotaGetBot](https://t.me/NotaGetBot) in Telegram and tap “Start”.
2. Tap “Connect Google” and sign in to your Google account.

Nota will create a sheet and a folder for documents in your Google Drive. You can always get the link to the sheet with the /table command.

- The first 30 documents are free. Plans and payment: /subscription.
- Nota chooses its language from your Telegram settings: Russian, English or Indonesian. To change it: /language.

## 2. How to send documents

**Directly to the bot.** Take a photo of a receipt or invoice and send it to the bot. You can also send a PDF or forward a message with a document from another chat.

**In a work group.** Add Nota to the chat where your employees already send receipts. Only the account owner can do this.

- Nota says hello in the group once, and after that it only puts ✍ on each document it records.
- Your employees don't need to do anything.
- Nota tells only you about duplicates and errors, in a private message.
- How many groups you can connect depends on your plan: Start — up to 5, Growth — up to 10, Scale — unlimited.

**As an archive of past months.** Use the /history command. Send a ZIP archive with documents or an export of your work chat. To export a chat, use Telegram Desktop on a computer.

To make sure Nota reads a document correctly:

- photograph the whole document, in good light and without glare;
- one document per photo;
- send a document with several pages as one PDF.

Nota records only documents: receipts, invoices, delivery notes, payment screenshots. It will not record a message like “spent 500 on a taxi” without a document.

## 3. What you will see in the sheet

Each document is a separate row. You can open the original with the link in the **ID · File** column.

In the **Check** column, Nota shows the result of its check:

- **OK** — everything matches, you don't need to do anything.
- **Review** — the document is recorded and counted in the totals, but you should check it. Nota writes what exactly to check in the Comments column; the Match column has a “Comment→” link to that note. Open the original and fix the row if needed.
- **DBL** — a duplicate: this document is already recorded, and the number of the first entry is in the Match column. Compare both entries, don't pay twice, and set the duplicate's status to Rejected.

You can correct any data in the sheet, and you can delete a whole row. Nota does not overwrite your changes, and the totals are recalculated right away. If you simply don't need a row, it is easier to set its status to Rejected: it stays in the history but is not counted in the totals.

The totals are in the dashboard at the top of the sheet. Spending by month and by category is on the Monthly spend tab, and things that need your attention are on the Insights tab.

## 4. Columns you can fill in yourself

They are marked with a pencil ✎ in the header. You don't have to fill them in: Nota works without them. But with them it is easier to track payments and see spending by location.

**Status** — the payment status:

- **Paid** — paid. If the document itself confirms payment, for example a receipt from a shop, Nota sets Paid on its own.
- **To pay** — the invoice needs to be paid.
- **Rejected** — the row is not needed: a duplicate or a document sent by mistake. It stays in the sheet but is not counted in the totals.

**Category** — the expense category. Somewhere between the 15th and the 30th document, Nota will ask what your business does, and after that it will set categories on its own. If a different category is right, choose it from the drop-down list right in the row.

**Business Unit** — what the expense belongs to. Nota puts the name of the group the document came from, or Personal if it was sent directly to the bot. On the References tab you can replace this name with your own location, villa or shop.

**Account** — what you paid from: a bank account, a card or cash. You can add your own options in advance on the References tab, and they will appear in the drop-down list.

**Comments** — here Nota writes what to check in rows marked Review. You can also add your own notes here.

## 5. Notifications and reports

- **Notifications:** /notifications. Choose whether to get a card for every entry or only the important things: duplicates and documents to review.
- **On a schedule:** every Monday morning, a report for the past week; on the 1st of each month, a report for the past month. It is easy to forward to a partner.
- **On request:** at any time, you can request from the menu a report for the current week or month, even if it is not over yet, and also for the past month.

## 6. Common situations

- **Need a different currency:** /currency. All entries, including old ones, will be recalculated.
- **Need to disconnect a group:** remove Nota from that group.
- **Have a question or something is wrong:** /support or the support bot [@NotaSuppBot](https://t.me/NotaSuppBot). We reply within 24 hours.
- **Want to delete your data:** /delete. Nota will delete the records of your documents, disconnect from Google and leave all groups. The sheet and the documents folder in your Google Drive stay with you.

More about Nota is on the [home page](/).
