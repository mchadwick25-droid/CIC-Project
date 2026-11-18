# R1 review: Library headers, evidence rule (2026-11-15)

Reviewer: fresh Opus subagent, read and grep only, on the working-tree diff. Scope: 17 headers in `cic/texts/` plus one appended line in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (item 280).

## Result

| Check | Verdict |
|---|---|
| Only header lines changed (every hunk ends before the first blank line of each file) | Pass |
| Line count identical in all 17 files, HEAD against working tree | Pass |
| Wording matches INTAKE.md; no history, dates of change or review references | Pass |
| Nothing real lost (OCR, scope, vendoring-date, NPNF, WEBBE, German-commentary notes kept) | Pass, with the notes below |
| "The scan is garbled" sentence in ausbund and ribadeneira is backed by the 2026-09-25 ruling in `LIBRARY-DECISION-LOG.md` | Pass |
| No retired wording left in any `cic/texts/*.txt` header | Pass |
| Each file states its own quotable status (INTAKE.md section 9) | Open, listed for Mark |

## Files

The thirteen in Open-Gaps 280, plus four found by the grep: fasciculi-zizaniorum_shirley1858, kempis sermones-ad-novicios, wyclif de-ecclesia, wyclif de-veritate-sacrae-scripturae. Total 17.

## Fixed after review

harnack_vita-cypriani-commentary: the header now says "not primary evidence" for the reason that survives the retired rule: the commentary is secondary and most of the file is German commentary.

## Open for Mark

These 15 headers now state the rule but not whether this particular scan is clean enough to quote. Deciding that needs a scan check, so it was not guessed: augustine csel57-pars4, borromeo, busch, faber, fasciculi-zizaniorum, kempis (sermones-ad-novicios, sermones-de-compunctione, tractatus, vallis-liliorum), nestle1904, piccolomini 1592, pius-v, wyclif de-ecclesia, wyclif de-veritate. Only ausbund and ribadeneira say second witness, because the ruling lists them as garbled scans.

Pointers from existing notes: piccolomini 1592 likely second witness (the 1524 printing's REGISTRY note); borromeo and pius-v have OCR-garbled headings and numerals; nestle1904 is born-digital, not OCR; augustine's letter text reads reliably and its apparatus does not.

## Out of scope, not touched

`REGISTRY.yaml` (append-only) still carries the retired wording at the nestle1904 note and the codex-theodosianus note. The augustine and nestle1904 headers no longer say a world's records cite the NPNF or WEBBE English edition; that fact is minor and stands in REGISTRY.
