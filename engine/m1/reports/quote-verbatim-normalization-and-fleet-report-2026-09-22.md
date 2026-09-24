# Quote Verbatim Gate — Normalization Ruling & Fleet Report (2026-09-22)

Tech-Readiness Package 3 (Fidelity as a Machine Gate), P3 relaunch thread.
This file is the durable record Mark asked for in place of the doc page
that rendered blank for him — the normalization options that were on the
table, his ruling, and the first fleet-wide sweep's results.

## Normalization policy — options that were presented

Three options were drafted (strict / editorial-tolerant / fuzzy-with-threshold), grounded in this repo's own quote records and vendored files rather than generic assumptions:

| | A — Strict | B — Editorial-tolerant | C — Fuzzy-with-threshold |
|---|---|---|---|
| Case / dash style / boundary punctuation | Compared as-is (can false-fail) | Normalized away | Absorbed into a similarity score |
| Editorial brackets `[truly]` | Must match exactly, brackets included | Matched with brackets stripped either side | Absorbed into the similarity score |
| Ellipsis (real omission) | Split on `...`, each segment verbatim, in order | Same split, boundary-tolerant | Implicit — markers stripped, whole scored |
| Edition/translation mismatch | Fails loudly (words differ) | Fails loudly (words still differ) | Real risk of a false pass — shared vocabulary can clear threshold |
| Fidelity guarantee | Strongest | Strong | Weakest, at the exact place it matters most |

Recommendation going in was B, for the reason C is structurally weaker exactly where the gate needs to be strongest (edition-mismatch risk) while gaining little over B.

## Mark's ruling (2026-09-22)

> Editorial-tolerant with a published list. The gate passes a quote only when every difference between the record's quoted words and the vendored text in `cic/texts/` is one of: whitespace, letter case, punctuation variants, an ellipsis marking an elision, a square-bracket insertion. Any word substitution, an omission without ellipsis, or an addition outside brackets fails. No fuzzy score, no threshold.

This is closer to A than the original B draft — narrower than "normalize case/dash/boundary punctuation broadly," and a closed, named list rather than a general tolerance policy. Implemented exactly as ruled in `engine/m1/quote_verbatim.py`'s `ALLOWED_DIFFERENCE_CLASSES`:

| Class | What it allows |
|---|---|
| `whitespace` | A run of spaces, tabs, or line breaks differing from the source's own. |
| `case` | A letter's capitalization differing from the source. |
| `punctuation` | A quote mark, apostrophe, or dash that is a different Unicode form of the *same* mark (curly vs. straight, hyphen vs. en/em dash) — never a different mark (a colon read as a dash still fails). |
| `ellipsis` | `...` or `…` marks a real elision; the words either side must still match, in order. |
| `bracket` | Text inside `[...]` is a labeled editorial insertion, never required to appear in the source. |

No fuzzy score anywhere: matching is a compiled regex per quote segment, searched directly against the (markup-stripped) vendored text. A pass or fail is a closed yes/no against these classes — nothing else moves the answer.

## Second ruling (2026-09-22, same day) — class six allowed, class seven not

The first fleet sweep (below) surfaced two candidate patterns not covered by the five classes above. Mark's ruling on both:

> Class six is allowed, class seven is not. An inline Arabic verse or section number in the source edition, standing at a sentence boundary, may be absent from the quote; the words on either side must still match, in order. A nested quotation mark rendered as a different mark stays a failure and gets fixed in the record.

| Class | Ruling | What it allows |
|---|---|---|
| `verse_number` (six) | **Allowed** | A bare 1–4 digit number followed by a period, standing at a word-boundary gap in the quote's own text (e.g. source "...thus give thanks. **2.** First..." vs. record "...thus give thanks. First..."). Never a wider skip — only that exact shape. |
| nested-quote-mark (seven) | **Not allowed** | A straight double quote in the record where the source has a curly single quote marking an inner quotation (or any other mark-for-mark swap) is a real difference, not a variant — stays a failure, fixed in the record, not accommodated here. |

Implemented in `_segment_pattern`'s whitespace-gap matching (an optional `\d{1,4}\.\s+` inserted at every flexible-whitespace boundary) — no change to bracket, ellipsis, or punctuation handling, and nothing added for class seven.

## Mechanism

`engine/m1/quote_verbatim.py`, `gate_quote_verbatim(records, fleet, registry) -> list[str]` — same shape as every `gate_*` in `gates.GATES`, **not registered there yet** (report-only, per both rulings — CI-blocking is still a later PR, after the report below is reviewed).

Source resolution: a quote record's own body prose is checked first for a `cic/texts/...` citation (tolerant of the citation being hard-wrapped mid-filename, a real case found in `pahc.quote.ignatius-truly-born`); falls back to the linked `source` record's `edition` field. XML/ThML-sourced quotes get `<note>` blocks (real prose, not reading text) and other tags stripped before matching.

20 unit tests in `engine/m1/tests/test_quote_verbatim.py`: one per allowed class (must pass, including two for `verse_number` — a synthetic case and one confirming the allowance doesn't license a wider skip), one per disallowed difference (must fail — including the colon-vs-dash case this project already caught by hand once, in `pahc.quote.melito-no-phantom`), XML stripping, and real-record integration checks — including `pahc.quote.first-concerning-the-cup` (now passes) and `pahc.quote.polycrates-to-victor` (a genuine unmarked omission, confirmed still failing after the verse-number ruling).

## Fleet sweep — six audited worlds + the other five

Ran `python -m engine.m1.quote_verbatim` against all 11 admitted worlds, after the `verse_number` ruling. Full per-record detail (every failure's exact failed segment and nearest source context) is in `engine/m1/reports/quote-verbatim-report-2026-09-22.json`, regenerated by this same run — this table is the summary. (First-sweep numbers, before the second ruling: 178 verified / 79 failed — kept here for the record, not in the table below.)

| World | Audited (2026-08-28)? | Total quotes | Verified | Failed | whitespace | case | punctuation | ellipsis | bracket | verse_number |
|---|---|---|---|---|---|---|---|---|---|---|
| pahc | yes | 25 | 16 | 9 | 12 | 0 | 0 | 2 | 3 | 2 |
| syr | yes | 34 | 29 | 5 | 20 | 1 | 3 | 0 | 3 | 1 |
| desert | yes | 60 | 38 | 22 | 24 | 2 | 1 | 5 | 9 | 0 |
| hal | yes | 32 | 26 | 6 | 26 | 0 | 3 | 0 | 0 | 0 |
| alx | yes | 26 | 22 | 4 | 20 | 0 | 0 | 0 | 0 | 3 |
| ijc | yes | 39 | 24 | 15 | 23 | 0 | 3 | 1 | 0 | 0 |
| cappadocian | no | 20 | 14 | 6 | 13 | 0 | 3 | 0 | 0 | 0 |
| don | no | 5 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| gallic | no | 3 | 3 | 0 | 3 | 0 | 1 | 0 | 0 | 0 |
| rzg | no | 6 | 3 | 3 | 3 | 0 | 0 | 1 | 0 | 0 |
| witt | no | 7 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 |
| **Total** | | **257** | **184** | **73** | | | | | | |

The `verse_number` ruling moved 6 previously-failing quotes to verified (178 → 184; 79 → 73 failed): `pahc.quote.first-concerning-the-cup`, `pahc.quote.two-ways-one-of-life-and-one-of-death`, `alx.quote.athanasius-death-trampled-down`, `alx.quote.demetrius-accused-him-bitterly`, `alx.quote.dionysius-too-high-for-me-to-grasp`, and `syr.quote.a-man-called-wise-amongst-the-jews` — the last two found by the fresh sweep's own classification, not among the ones hand-picked from the first sweep. Two quotes hand-identified in the first sweep as verse-number cases (`pahc.quote.not-every-one-that-speaketh-in-the-spirit`, `ijc.quote.ammianus-sicininus-massacre`) **still fail** — the verse-number gap alone wasn't the whole story for those two; a further, different break exists later in each. Both are in scope for the hand-characterization pass (next PR).

Note: the "audited" worlds do not show a materially lower failure rate than the other five — `verification_state: verified-direct` in a record's own front matter is a human's prior claim to have re-checked against `cic/texts/`, not something this mechanical sweep found any reason to trust more than any other world's records. That itself may be worth a line in the P1/P2 tech-readiness threads: the audited/unaudited distinction doesn't currently predict which quotes actually verify.

## Why quotes fail — patterns found in the first sweep, now updated

A sample of failures was hand-traced (binary-searching each failing quote's own text against its source to find the exact break point, then reading the raw source there) to characterize *why*, not just count.

**1. Genuine unmarked omissions — real defects.** Example: `pahc.quote.polycrates-to-victor`. The record's text reads "...in the day of the coming of the Lord. Moreover I also, Polycrates..." — the vendored source (anf08) has "...coming of the Lord, **when He cometh with glory from heaven and shall raise again all the saints.** Moreover I also..." — roughly fifteen words silently dropped, no ellipsis. This is exactly the defect class the gate exists to catch (CLAUDE.md: "misattributed and mis-transcribed quotes have been a real, recurring defect here"). Confirmed still failing after the `verse_number` ruling (by design — a unit test pins this).

**2. Inline verse/section numbering — resolved by the second ruling.** The six failures originally flagged here (`pahc.quote.first-concerning-the-cup` and five others) are the class `verse_number` above now covers; four of the six now verify. The other two (`pahc.quote.not-every-one-that-speaketh-in-the-spirit`, `ijc.quote.ammianus-sicininus-massacre`) have a second, distinct break beyond the verse number — not yet characterized.

**3. Quote-mark nesting convention — ruled not allowed.** At least one case (`pahc.quote.put-away-doubting-from-you`) uses a straight double quote (`"`) where the source has a single curly quote (`'`) marking a nested quotation. Mark's ruling: this stays a failure, fixed in the record, not accommodated by the gate.

**Remaining ~69 failures** (73 total, minus the ~4 already characterized above) are not yet individually hand-characterized. Full failed-segment + nearest-context data for every one is in the JSON report. Hand-characterizing all of them (one line each: omission / edition mismatch / nested mark / other) is the next PR's own deliverable — no record edits there either.

## Status

Gate built, tested, wired report-only (not in `gates.GATES`) — still true after both rulings. Not CI-blocking. Next: hand-characterize every remaining failure (separate PR, triage list only, no record edits). Record fixes themselves are a separate session Mark will dispatch. CI-blocking switch-on stays a later PR, after triage.
