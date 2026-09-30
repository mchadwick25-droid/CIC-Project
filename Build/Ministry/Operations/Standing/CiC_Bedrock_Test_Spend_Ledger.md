# Bedrock test-spend ledger

The project's live-model test runs share one AWS account with the pilot testers. This ledger tracks only test runs started from build sessions. It is not the account's spend.

## Allowance

- **2026-09-30, Mark:** test runs may use $5 of the account's $44 credit. The rest is held for the pilot.
- A run that would take the ledger past $5 waits for Mark.

## How a run is priced

Estimated bill = billed tokens x the published rate card in `engine/m8/price_tables.py`, times 1.12.

- The tokens are real: Bedrock returns input, output and cache counts with every call.
- The dollars are an estimate. The 1.12 comes from one day, 2026-09-27, when recorded runs came to $5.96 and AWS billed about $6.77. Treat it as rough.
- The invoice, in Cost Explorer a day or two late, is the only real dollar figure. It includes the pilot's charges.
- Correct the factor when two or three quiet-pilot days show a different gap.

## Ledger

| Date | Run | Rate card | Est. bill |
|---|---|---|---|
| 2026-09-30 | Two-arm voice sample: 3-seat table (alx, desert, pahc), three rounds per arm, request layout on main against the cache-history branch | $1.17 | $1.31 |

| | |
|---|---|
| Allowance | $5.00 |
| Used | $1.31 |
| Left | $3.69 |

## Read next

- Daily AWS bill by service, Sep 1 to 29, read from the account's chart, and the match against recorded runs: Sep 27 recorded $5.96 against about $6.77 billed. Sep 23 recorded $7.67 against about $22.80 billed. The gap on Sep 23 has no recorded source and may include pilot traffic.
- Model invocation logging and a separate AWS identity for test runs would make the bill separable. Neither is set up.
