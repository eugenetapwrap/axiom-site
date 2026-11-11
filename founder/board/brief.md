# Board brief: Nota

Everything below comes from the founder and the founder's own product documents. Nothing has been added by the chair.

## The idea (from founder/idea.md)

- **What it is:** a Telegram bot that collects payment documents (receipts, invoices, handwritten delivery notes, bank-transfer screenshots, PDFs, ZIP archives) from work chats, checks them for duplicates and arithmetic errors, and writes each one as a row in the owner's own Google Sheet with a link to the original.
- **Who it is for:** any business owner without a finance department who has a Telegram group where employees, partners and the owner drop receipts and payments to be reimbursed or accounted for. First market: Bali / Indonesia, Russian-speaking owners and their local teams.
- **Price:** $19/month, up to 100 documents and up to 5 connected groups. First 40 documents free. Connection takes about one minute (log in with Google).
- **Channels:** online, inside Telegram (@NotaGetBot). Free permanent access for 10–30 friends; the founder's ~10 warm contacts who need it; word of mouth; viral loops in the product; automated posting on Threads.
- **Goal:** about $10,000/month revenue within the first 3 months. (At $19/month that is roughly 525 paying accounts.)
- **Budget:** not stated.

## Who builds it

Axiom Consulting, a finance consultancy based in Bali (financial models, model audits, management accounting and payment control for developers and construction). The team says it has 15 years of cost control experience and that its in-house payment-control system, which Nota is based on, has processed over 100,000 documents for its consulting clients.

## Current state

- The bot exists and is being refined. A live test runs at one large construction company (the founder's own client/company): about 30 payments a day. A recent sheet shows ~110 documents over Oct–Nov 2026: 102 valid, 1 duplicate, 9 flagged for review.
- Bot speaks Russian, English and Indonesian. Sheet is in English.

## How the product works (from the founder's product description)

- Owner opens @NotaGetBot, logs in with Google. Nota creates a Google Sheet and two Drive folders in the owner's account. Files are not stored on Nota's servers; only encrypted file hashes are kept for duplicate detection.
- Two ways in: send documents to the bot privately, or add the bot to a work group (up to 5 groups; each group becomes a "business unit", e.g. a site, villa or outlet). Employees change nothing: they keep posting receipts in the chat. In the group the bot stays silent except a greeting and a ✍ reaction on each recorded document. Duplicates and errors go only to the owner privately.
- Per document: recognises type, date, amount, payee, purpose; hashes the file and also compares data (amount, date, number, counterparty) to catch re-photographed receipts; recalculates line items and totals; writes a row with Check = OK / Review / DBL; renames the file and stores it in Drive. Proofs of payment for an already recorded invoice go to a separate folder and are not double-counted.
- Handles faded thermal receipts, crumpled and handwritten notes, local languages. In groups it separates payment documents from ordinary photos and chat.
- Any currency; owner picks a base currency and everything is converted, including history when changed.
- Auto-categories: 15 categories (based on IFRS) tuned for 10 business types (construction, villas/hotels, food service, retail, tourism, beauty/fitness, services, manufacturing, transport, events) plus personal finance.
- Sheet has a dashboard (OK / duplicates / review / uncategorised, count and sum) and an "Expense Flow" sheet (categories × months).
- Weekly report card every Monday and monthly on the 1st: spend vs previous period, average and peak per day, by day and by category, duplicates excluded, documents pending review. Designed to be forwarded to a partner or investor.
- Can ingest a ZIP of past receipts or an exported chat history and show past duplicates.
- Deliberately no manual, voice or text entry: only documents. Positioning: "not accounting, control: what was paid, to whom, for what, and not twice."
- Owner can edit any cell; the bot never overwrites edits.

## Growth plan (from the founder's virality plan)

- Stage 0: fill in bot profile (name, about, description) in RU/EN/ID.
- Stage 1 (~1.5 weeks dev): last line in the group greeting inviting members to try Nota for their own business; "Prepared in Nota" line with referral link in the sheet header; referral link in the report caption; "Share report" button that sends the report card to any chat; referral links per account (no reward to customers — founder decided a free month at $19 motivates nobody; money rewards only in a future partner programme for accountants and villa management companies); a dedicated /start screen for group members who are not customers; flows for when someone other than the owner adds the bot to a group.
- Stage 2 (1–2 days): after a caught duplicate, ask the owner to recommend Nota (max once per 30 days); /invite command.
- Stage 3 (2–3 weeks): monthly package for the accountant (folder with month's sheet and documents); counterparty name merging; reconciliation statement for a supplier (shareable, with referral link); "ask for a receipt" message.
- Stage 4 (after first paying customers): natural-language questions in the bot; an MCP connector for Claude/ChatGPT; per-project investor report (strongest for villa management companies with 10–30 owners each); payment approval flow.
- Metrics planned: paying customers from groups per 10 connected groups per month (target ≥1); start → paid conversion from viral links (target ≥10%); share of viral customers among new payers (target 10–30%). The founder labels these targets as estimates.

## What is not known yet

- Budget, team size dedicated to Nota, and marketing spend.
- Cost per document (AI recognition) and therefore gross margin.
- Competitors and their prices.
- Conversion from free (40 docs) to paid; churn.
- Whether the 10 warm contacts will pay.
- Note: some draft texts in the product docs still say "30 documents free"; the founder's current number is 40.

## Founder's addition (emphasis)

- The bot checks the content inside each document: it reconciles what is written (line items, quantities, prices) against the stated total and flags mismatches.
- It reads handwritten documents in any format and language.
- It shows that a payment was already submitted: by identical file (hash) and also when the same receipt was re-photographed or sent as a screenshot (matching amount, date, number, counterparty).
