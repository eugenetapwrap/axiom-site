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

This Privacy Policy (the "Policy") sets out what data the Nota service processes, for what purposes, how long it is kept and how the User can delete it. Terms have the meanings given in the [Terms of Service](/en/terms).

## 1. Data Controller

1.1. The data controller is Individual Entrepreneur Evgenii Popov, Georgia, identification number 346999215, legal address: Rustaveli Street, Kobuleti, Georgia (the "Operator").

1.2. Requests concerning data processing shall be sent to the Telegram bot [@NotaGetBot](https://t.me/NotaGetBot) or by email to [to confirm: support email].

## 2. Data Processed

2.1. Telegram data:

- the User's Telegram ID, name, username and interface language;
- the ID and name of Work Groups to which the bot has been added;
- the name and Telegram ID of the Work Group member who sent a Document;
- messages the User sends to the bot directly.

2.2. In a Work Group, the Service processes payment documents only. Other Work Group messages are not stored.

2.3. Documents: files of receipts, invoices, delivery notes, transfer confirmations and chat archives, and the information extracted from them — date, amount, supplier, payment details, line items, category, project. Documents may contain personal data of third parties, including names, phone numbers and bank account numbers.

2.4. Google data (when a Google Account is connected):

- the email address of the Google Account;
- access tokens required to write to the Sheet and Folder;
- access to the Sheet and Folder created by the Service. The Service has no access to other files on the User's Google Drive.

2.5. Payment data: Plan, amount, date and status of the payment, and the transaction number at the bank or payment service. Card details are entered on the Bank of Georgia page; the Operator does not receive or store them.

2.6. Technical data: server and error logs; IP address and browser type when the website or payment page is visited.

## 3. Purposes and Legal Bases

3.1. Data is processed in order to:

- recognise Documents, write data to the Sheet and save originals to the Folder;
- detect duplicates and discrepancies in amounts and send reports and alerts;
- accept payments, manage Plans and issue invoices;
- respond to User requests;
- fix errors and protect the Service from abuse.

3.2. Legal bases: performance of the [Terms of Service](/en/terms), the User's consent (connecting a Google Account), the Operator's legitimate interest (security of the Service) and legal obligations (payment records).

3.3. The Operator does not sell User data, does not use it for advertising and does not use Documents to train artificial intelligence models. The Operator engages recognition services that do not train models on customer data.

## 4. Data Received via Google APIs

4.1. Nota's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements. In particular:

- Google data is used solely to maintain the User's Sheet and Folder;
- it is not transferred to third parties, except as necessary to provide the Service, as required by law, or at the User's request;
- it is not used for advertising and is not sold;
- it is not read by humans, except where the User has requested assistance, where necessary for security purposes, or where required by law;
- it is not used to develop, improve or train generalised artificial intelligence or machine learning models.

4.2. The User may revoke the Service's access at any time under Google Account → Security → Third-party apps & services. The Sheet and Folder remain with the User.

## 5. Disclosure to Third Parties

5.1. Data is disclosed only to parties without which the Service cannot operate:

- Telegram — receiving and sending messages;
- Google — maintaining the Sheet and Folder on the User's Google Drive;
- the hosting provider — hosting the Service's server and database;
- a recognition service — extracting text from Documents;
- Bank of Georgia — accepting card payments;
- a payment service — accepting cryptocurrency payments.

5.2. A list of specific providers is available on request.

5.3. Data may be disclosed to public authorities where required by law.

## 6. International Transfers

6.1. The Operator's servers and providers may be located outside the User's country, including outside Indonesia. The Operator transfers data only to the providers listed in section 5 and requires them to protect it to at least the standard required by law, including Indonesian Law No. 27 of 2022 on Personal Data Protection (UU PDP). <!-- lawyer: requirements for transfers out of Indonesia -->

## 7. Retention

7.1. If no Google Account is connected, the files sent and the data extracted from them are kept for 7 days. If a Google Account is connected within that period, the data is written to the Sheet; otherwise it is deleted.

7.2. With a Google Account connected, original Documents and recorded data are kept in the Sheet and Folder on the User's Google Drive until the User deletes them. For the duration of the Plan, the Operator's servers keep records of Documents, including their fingerprints (hashes) for duplicate detection.

7.3. Documents over the limit are kept in a queue for 7 days from the date the first Document was placed in it.

7.4. After the Plan ends, User data is kept for 30 days and then deleted.

7.5. Payment data is kept for the period required by Georgian tax law.

## 8. Deletion

8.1. To delete their data, the User sends the bot the delete command or a request by email to the address in clause 1.2. Upon such request the Operator:

- deletes all records of the User's Documents in its database, including fingerprints (hashes);
- disconnects the Service from the User's Google Account;
- removes the bot from all of the User's Work Groups.

8.2. After deletion, only the Telegram username and the payment data required to be kept by law are retained. Deletion is completed within 30 days and confirmed in the bot or by email.

8.3. The Sheet and Folder remain on the User's Google Drive; the Service disconnects from them. Only the User can delete them.

## 9. User Rights

9.1. The User has the right to:

- obtain information about the data processed and a copy of it;
- request correction of inaccurate data;
- request deletion of data;
- withdraw consent, including by revoking Google Account access;
- object to or request restriction of processing;
- lodge a complaint with the data protection authority in their country.

9.2. Requests shall be sent to the bot or to the email in clause 1.2. The Operator responds within 24 hours and fulfils the request within the period set by law.

## 10. Data Security

10.1. Data is transmitted over encrypted connections. Each User's data is stored separately. Server access is granted only to persons who need it for their work.

10.2. In the event of a breach affecting User data, the Operator shall notify the User and, where required by law, the competent authority within the prescribed period.

## 11. Minors

11.1. The Service is intended for businesses. The Operator does not knowingly process data of persons under 18.

## 12. Changes to the Policy

12.1. The Operator may amend this Policy. The Operator shall notify the User of material changes in the bot in advance. The date of the current version is shown at the top of the page.
