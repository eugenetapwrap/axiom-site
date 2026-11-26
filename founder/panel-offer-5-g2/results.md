# Buyer panel: Nota (@NotaGetBot): a Telegram bot that collects receipts, invoices and handwritten delivery notes from work chats into the owner's Google Sheet and flags duplicates and arithmetic errors

**5 buy · 15 pass** (25% buy) out of 20 simulated buyers. Seed 843138, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

## By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Remote investor in villas or a build, living abroad | 3 | 67%  (thin) |
| Café / restaurant owner | 3 | 33%  (thin) |
| Villa management company or villa rental operator | 5 | 20%  (thin) |
| Construction / renovation contractor or developer | 6 | 17%  (thin) |
| Shop or bike/scooter rental owner | 3 | 0%  (thin) |

## By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Burned before | 2 | 100%  (thin) |
| Runs everything through chats | 5 | 40%  (thin) |
| Has an admin with Excel | 4 | 25%  (thin) |
| Price-sensitive | 2 | 0%  (thin) |
| Tech-savvy DIY | 2 | 0%  (thin) |
| Already uses an app | 2 | 0%  (thin) |
| Privacy-wary | 2 | 0%  (thin) |
| Delegates to a bookkeeper | 1 | 0%  (thin) |

## By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $104,000 and up | 7 | 43%  (thin) |
| $88,000 to $104,000 | 7 | 29%  (thin) |
| under $88,000 | 6 | 0%  (thin) |

## Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 6 | "I'd let the staff try the free part, but a café makes 30 receipts in a few days, so the free part is over before we know if it works. Then I'm paying $35 a month on top of the admin I already pay, and I think we slide back to the spreadsheet like always." (P002) · "My bookkeeper and I already run everything through our expense app and it works well enough. I might let the bot read one group for the free 30 out of curiosity, but I'm not paying to move a whole year of site receipts into a new tool." (P007) |
| trust | 4 | "The price is nothing for a villa business, but I'm not putting some new bot I've never heard of into my staff groups and my Google account this month. I'd maybe throw a few receipts at the free version and wait to see if it's still around in a few months." (P010) · "I'm not putting some bot I've never heard of into my work group and hooking it up to my Google account just to sort receipts for scooter parts and fuel. Half my money goes out in cash to mechanics anyway, so my notebook and the group chat do the job well enough." (P011) |
| quality | 2 | "I might throw the free 30 at it some night, but I expect it to misread the faded and handwritten nota my staff send from the warung and the hardware shop. If I still have to check every line myself, I'm not paying for it." (P001) · "I'd throw the free 30 nota at it just to see, but my guys' handwritten nota from the material shop are faded, smudged and half in shorthand, and I'm pretty sure it will misread the totals. If I have to check every line anyway, I'd rather wire up my own n8n plus ChatGPT flow for a few dollars and fix it my way." (P005) |
| price | 2 | "I'd let it try the free 30, but with receipts landing in three or four groups every day that's gone in a few days, and then I'm at $35 or even $79 a month just to sort receipts. That's another subscription I'd question every month, so I'd stop at the free part." (P016) · "I'd run the free 30 receipts to see how it works, but $19 a month every month is a lot for a small rental shop when I could put together something like this in n8n with ChatGPT over a weekend. Writing to my own sheet is nice, but it doesn't do anything I can't do myself." (P020) |
| need | 1 | "I might run the 30 free documents just to see the sheet, but I pay the contractors myself by transfer and already have the screenshots in the group. If someone double-bills me, that is my foreman's problem to answer for, not something I pay $19 a month to have flagged." (P004) |

## Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 4 | "I've already caught someone claiming the same nota twice, and my Excel sheet doesn't flag that, so I'm checking every receipt myself. It's free to try and $35 a month is nothing next to one inflated cement order, so I'd run the free 30 with a duplicate I plant myself, and if it catches it I'll pay." (P003) · "I'm abroad and my admin's spreadsheet is always a week behind, so I end up scrolling the group chat at midnight trying to work out what was spent on the build. If the free 30 show it can read our notas and flag duplicates, $35 a month costs nothing next to a single double-paid invoice, so I'd pay." (P006) |
| convenience | 1 | "The receipts are already sitting in our Telegram groups, so 30 free documents with no card costs me nothing to try before month end. If the sheet is clean when my accountant asks, $19 is nothing next to the hours I lose chasing staff for nota." (P008) |

## What would flip a no

- Running it on my own Telegram group archive and seeing it read the worst handwritten nota correctly, and flag the ones it can't read instead of guessing a number.
- A free first month, long enough to see that the sheet is really full and correct without my admin retyping anything, including our handwritten market notes.
- If the free trial actually caught a duplicate or wrong total on the build that I had missed and paid, real money lost that is bigger than a year of the fee.
- If the free 30 actually read my staff's real handwritten nota correctly, and clearly flagged the ones it wasn't sure about instead of guessing, I'd pay rather than build it myself.
- If it sent clean data straight into Jurnal or Zoho, so it fills a gap instead of replacing my app, and I could see it had been running for other Bali contractors for a year or more.
- Another villa operator in Bali I know telling me they've used it for months and it caught real duplicates or mistakes their staff sent.
- If it worked without connecting my Google account at all, like the bot just sends me the spreadsheet file and I keep it myself.
- If the free 30 documents caught a duplicate or wrong total on fuel or parts that my admin missed, so I could see it actually saves me money and not just typing.
- If during the free 30 it caught a duplicate or a padded mechanic bill and showed me cost per scooter without my admin touching it, I would pay $19.
- Another contractor in Bali I know showing me it has run clean in his groups for a few months, or a way to just forward receipts to the bot myself without adding it to the group.
- My bookkeeper telling me she wants it and will run it, or the bot chasing my staff by name for the receipts that are missing before month end.
- A full free month on all my groups, then one flat price under $20 that covers what a café actually sends.

Buyers say they would buy **1.0 times** in the first month on average.

20 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.
