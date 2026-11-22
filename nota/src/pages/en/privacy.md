---
layout: ../../layouts/Doc.astro
title: Privacy Policy
description: Privacy Policy for Nota.
updated: ''
lang: en
slug: privacy
plan:
  - what data Nota receives from Telegram, Google and your documents;
  - why it is needed and how long it is kept;
  - access only to the Nota sheet and folder on Google Drive;
  - who data is shared with;
  - how to delete your data and contact us.
---
<!--
DRAFT 22.11, translated from the Russian version (src/pages/privacy.md). Not legal advice: have a lawyer review before publishing.
"[to confirm: …]" marks open questions, also listed in founder/legal-docs-questions.md.
This is the page to link in Google Cloud Console → OAuth consent screen.
-->

This policy explains what data Nota receives, why, where it is stored and how to delete it.

## 1. Who is responsible for your data

The data controller is Individual Entrepreneur Evgenii Popov, Georgia, identification number 346999215, legal address: Entrance 1, Floor 6, 140-v Rustaveli Street, Kobuleti, Georgia.

For questions about your data, write to [to confirm: support email] or to the bot [@NotaGetBot](https://t.me/NotaGetBot).

## 2. What data we receive

**From Telegram:**

- your Telegram ID, name, username and interface language;
- the ID and name of work groups to which you add the bot;
- the name and Telegram ID of the group member who sent a document;
- messages you send to the bot directly.

In a work group, the bot takes only payment documents. Nota does not store other group messages. [to confirm with the developer: what exactly the bot sees and stores in a group]

**Documents you send:** files of receipts, invoices, delivery notes, transfer screenshots and chat archives, and what Nota reads from them: date, amount, supplier, payment details, line items, category, project. Documents may contain other people's data: names, phone numbers, account numbers.

**From Google**, if you connect Google:

- the email address of your Google Account;
- access tokens so that Nota can write to the sheet and folder;
- access to the sheet and folder Nota creates on your Google Drive. Nota cannot see other files on your Google Drive.

**Payment data:** plan, amount, date and status of the payment, the transaction number at the bank or crypto service. You enter card details on the Bank of Georgia page; we do not receive or store them.

**Technical data:** server and error logs; IP address and browser when you open the website or the payment page. [to confirm: whether the website uses analytics or cookies]

## 3. Why we use this data

- To read documents, write rows to your sheet and save the originals to the folder.
- To find duplicates and errors in totals, and to send reports and alerts.
- To take payments, manage plans and issue invoices.
- To answer support requests.
- To fix errors and protect the service from abuse.

Legal bases: performance of our contract with you ([Terms of Service](/en/terms)), your consent (connecting Google), our legitimate interests (security of the service) and legal obligations (payment records).

We do not sell your data, do not show ads and do not use your documents to train AI models. [to confirm: that the chosen document-recognition provider does not train on the data either]

## 4. Data from Google

Nota's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements. This means:

- we use data from Google only to maintain your sheet and folder;
- we do not transfer it to third parties, except as needed to run the service, as required by law, or at your request;
- we do not use it for advertising and do not sell it;
- no one reads it, except when you ask for help, when needed for security, or as required by law;
- we do not use it to develop, improve or train generalised AI or machine learning models.

You can revoke Nota's access at any time: Google Account → Security → Third-party apps & services. The sheet and folder stay with you.

## 5. Who we share data with

Only with providers the service cannot work without:

| Who | Why | Where |
|---|---|---|
| Telegram | receiving and sending messages | [to confirm] |
| Google | your sheet and folder on Google Drive | per your account settings |
| [to confirm: document-recognition provider] | reading text on documents | [to confirm] |
| [to confirm: hosting, e.g. DigitalOcean] | server and database | [to confirm: Singapore?] |
| Bank of Georgia | card payments | Georgia |
| [to confirm: crypto service] | cryptocurrency payments | [to confirm] |

We may also disclose data to public authorities where the law requires it.

## 6. International transfers

Our servers and providers may be located outside your country, including outside Indonesia. We transfer data only to the providers listed above and require them to protect it at least to the standard required by law, including Indonesia's Personal Data Protection Law (Law No. 27 of 2022, UU PDP). [to confirm with a lawyer: requirements for transfers out of Indonesia]

## 7. How long we keep data

- **Without Google connected**, the files you send and the data read from them are kept for 7 days. If you connect Google within that time, everything is written to your sheet. If not, it is deleted, and you keep the report in the chat.
- **With Google connected**, originals and rows are kept in your sheet and folder on your Google Drive until you delete them. On its own servers, Nota keeps [to confirm with the developer: what exactly — file copies, hashes for duplicate detection, extracted data] for as long as your plan is active.
- **After your plan ends**, we keep your data for 30 days so you can come back without losing anything, then delete it.
- **Payment records** are kept for as long as Georgian tax law requires. [to confirm with an accountant: period]
- **Backups** are deleted on their own cycle within [to confirm: period] days.

## 8. How to delete your data

Send the bot the command [to confirm: command name, e.g. /delete] or email [to confirm: support email]. We will delete your data from our servers within 30 days and confirm in the bot or by email.

We do not delete the sheet and folder on your Google Drive: they are yours, and only you can delete them.

## 9. Your rights

You can:

- find out what data we hold about you and get a copy;
- correct inaccurate data;
- delete your data;
- withdraw consent, for example by revoking Google access;
- object to or restrict processing;
- complain to the data protection authority in your country.

To exercise a right, write to [to confirm: support email]. We will reply within [to confirm with a lawyer: deadline under UU PDP and Georgian law].

## 10. How we protect data

Data is sent over encrypted connections. Each customer's data is stored separately. Only people who need server access for their work have it. [to confirm with the developer: encryption at rest, who has access]

If a breach affects your data, we will notify you and, where the law requires, the regulator within the required time.

## 11. Children

Nota is a business service. We do not knowingly process data of people under 18.

## 12. Changes to this policy

We will notify you of material changes in the bot in advance. The date of the current version is shown at the top of the page.
