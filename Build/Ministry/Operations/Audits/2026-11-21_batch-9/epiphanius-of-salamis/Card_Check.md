# Card check: Epiphanius of Salamis (`epiphanius-of-salamis`)

**Verdict: FIX** (one change). Separately, the three scan listings must be added to `tools/quote_scan_readings.json`; the Card_Edits entries for them are correct.

## Checks

1. Edits against evidence: the three corrections hold (HOLL1 is the Ancoratus and Panarion 1-33; HOLL2 and PG 42 cover 34-80). The new traces, remembered lines and uncertain entries were re-read at AUG, PHOT, J6, SS, SOZG, PALL, MEN, ETH and ACTA, and all hold. The ordination and curtain reasons were checked at J6 10650-10715 and 11105-11108.
2. Unlisted fields: the diff against `Card.existing.json` shows only the listed edits.
3. `briefReferences`: all eleven name what the brief tells.
4. Census rules: allowed keys; two `quotationOriginals`, one per quoted span. The Euphrates print stands at J6 10920-10922. Every cited file is in `sources`. No audit named. American spelling. The outline renders the preface from Holl's Greek, and the card carries it.
5. "checked at card": none.
6. Not found: none, and none found on recheck.

## The scan listings for `tools/quote_scan_readings.json`

Each was checked against HOLL1 by byte and by code point:
- Line 12388, "τάς TE παρ᾽". The scan has Latin capital T and E (U+0054, U+0045). It reads "τάς τε παρ᾽", which is right: it pairs with "τά τε" on the same line.
- Line 12390, "δεδηγμένων zal". The scan has Latin z, a, l. It reads "δεδηγμένων καὶ", which is right.
- Line 12391, "προχαταληπτικὰ". The scan has χ for κ. It reads "προκαταληπτικὰ", which is right: the adjective means "preventive", against "ἀλεξητήρια", "cures".

With these three added to a scratch copy of the file, the validator passes the Greek `printed` at HOLL1 12387-12391 with no error. Without them it fails. No fourth listing is needed: the "|" in line 12391 is dropped by the validator's folding. Optionally, the kinds could follow existing entries: "OCR misread (Latin letters for Greek)" for the first two and "OCR misread (χ for κ)" for the third.

## FIX

1. `uncertain[10]`. "The last" reads as the hurry, the last item in the sentence before. The Greek word ὑπόκρισιν (SOZG 30112) is for the pretense.
   - Old: "The Greek word for the last is the one for acting or hypocrisy"
   - New: "The Greek word for the pretense is the one for acting or hypocrisy"

## Note (audit file only)

`Card_Edits.md` cites AUG 2411-2426 for "quinquaginta septem ex Epiphanii ipsius opere in meum transtuli". Those words are at AUG 2429-2430. The card itself carries no line numbers here.
