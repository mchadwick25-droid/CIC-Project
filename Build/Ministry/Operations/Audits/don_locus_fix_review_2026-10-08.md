# Donatist locus fix: review, 2026-10-08

Reviewer: Opus 5.5, single adversarial review.
Branch: `records/don-locus-fix` (commits b64d997f, aeb6f00b), stacked on `records/identity-scaffolding-don-leftovers` (PR #831). Diff read with `git diff origin/records/identity-scaffolding-don-leftovers...HEAD`.

Scope: `records/don/doctrinal_witness/don.witness.refusal-and-recourse.md` `sources`; OG-29 in `Build/worlds/don/Open_Gaps_Tracking.md`; the package pin in `records/worlds/don.yaml`; the package `packages/don/2026-10-08T19-32-19Z`.

## Verdict

**APPROVED TO PROCEED.** No substantial findings. Two not-substantial findings follow; neither blocks.

## What was checked

1. **English locus.** `cic/texts/optatus_against-the-donatists.txt` line 1904 reads exactly `'What has the Emperor to do with the Church?'`. The line sits after the heading `BOOK THE THIRD` (line 1821), so "Book III" holds. The new locus quotes that string with matching capitals.
2. **Latin locus.** `cic/texts/optatus_libri-vii-critical_ziwsa1893.txt` line 6557 reads `prorupit : 'qnid est imperatori cuni ecelesia ?' et de fonte leui-`. That is the retort, OCR-corrupted, as the locus says. The line sits after `Incipit Liber Tercius` (line 6217), so "Book III" holds.
3. **Source record id.** `records/don/source/don.source.ziwsa-critical-edition-optatus.md` exists, `id: don.source.ziwsa-critical-edition-optatus`, `edition: cic/texts/optatus_libri-vii-critical_ziwsa1893.txt`, public domain. The `license: public-domain` on the new entry agrees.
4. **Citation shape against the quote record.** `don.quote.donatus-quid-est-imperatori` cites the same two source ids, at the same two lines, with the same edition labels ("the Vassall-Phillips English translation" / "the Latin original, corrupted by OCR at this line"). The witness now agrees on ids, files, lines and roles. Wording order differs (see finding 2).
5. **No voiced text changed.** The diff to the record touches only `sources`: one locus rewritten, one entry added. `text`, `positions`, `tensions`, `use_note`, `confidence` and the body are untouched. The body's own pointer ("Book III, line 1904, `cic/texts/optatus_against-the-donatists.txt`") names the English file, so it is now consistent with `sources`.
6. **OG-29, statement by statement.**
   - "`sources[0].locus` gave Optatus line 1904 for the Donatus retort in its Latin form, but ... line 1904 holds only the English translation": true; old locus was `Book III, line 1904, Donatus's own reported retort ('Quid est imperatori cum ecclesia?')`.
   - "Closes the item carried in 'The two spoken fields left open ...'": the carried item is at the "Carried, for the build thread" paragraph of OG-28 and states the same defect. True.
   - "Mark ruled on it in session (converged, auto mode, 2026-10-08)": not verifiable from the repo; taken as reported by the caller.
   - "Pointer only; no voiced text changed": true (check 5).
   - "now names line 1904 of the English translation and quotes the English retort": true.
   - "A new source entry ... line 6557 ... corrupted by OCR at that line, with the retort in the form the record uses": true, though see finding 1.
   - "This matches how `don.quote.donatus-quid-est-imperatori` already cites both editions": true on ids, files, lines and roles.
   - "Gates. `records don` and `regate don --base origin/main`: pass": reproduced, both PASS.
   - Pin and hash: true (check 7).
   - "stacked on the branch of the open Donatist PR for the two spoken fields": PR #831, open, head `records/identity-scaffolding-don-leftovers`. True.
7. **Pin.** `sha256sum packages/don/2026-10-08T19-32-19Z/manifest.json` = `32a347d217c03f2968160d54c11a02340d953f13f322cb77998c11171f117546`. This equals the `manifest_hash` in `records/worlds/don.yaml` and in OG-29, and `location` is `packages/don/2026-10-08T19-32-19Z`. `diff -r packages/don/2026-10-08T19-32-19Z/records records/don`: identical.
8. **Gates, run in the worktree.**
   - `python -m engine.m10.cli records don`: PASS.
   - `python -m engine.m10.cli regate don --base origin/main`: PASS (notes only for pre-existing readability misses on unchanged records).
   - `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0; no finding on the changed record or on `records/worlds/don.yaml`.
   - `python -m engine.m9.cli check`: exit 0; "library access gate: clean - every finding is waived, every waiver is live and current".

## Findings

### 1. NOT SUBSTANTIAL: the Latin locus quotes the corrected form, not the string on the line

The new locus gives the retort as `'Quid est imperatori cum ecclesia?'`. Line 6557 carries `'qnid est imperatori cuni ecelesia ?'`. The locus does say the line is OCR-corrupted, so it does not mislead. But a reader searching the file for the quoted string will not find it. The quote record's locus gives the raw OCR string for this reason.

- Old: `locus: Book III, line 6557 of cic/texts/optatus_libri-vii-critical_ziwsa1893.txt (the Latin original, corrupted by OCR at this line), the retort 'Quid est imperatori cum ecclesia?'`
- New (suggested): `locus: Book III, line 6557 of cic/texts/optatus_libri-vii-critical_ziwsa1893.txt (the Latin original, corrupted by OCR at this line as 'qnid est imperatori cuni ecelesia ?'), the retort 'Quid est imperatori cum ecclesia?'`
- Fix: optional; take it on the next touch of this record, with a package rebuild. Not worth a separate pass.

### 2. NOT SUBSTANTIAL: OG-29 wording "in the form the record uses" is loose, and the locus word order differs from the quote record

The witness's voiced text uses only the English retort. "The form the record uses" means the corrected Latin of the old locus and of `don.quote.donatus-quid-est-imperatori` `text`. The locus order also differs: the witness writes `Book III, line N of <path> (<edition>)`, the quote record writes `Book III -- <edition>; <path>, line N`. Same content, different order. Neither is wrong.

- Old (OG-29): `with the retort in the form the record uses.`
- New (suggested): `with the retort in the corrected Latin that \`don.quote.donatus-quid-est-imperatori\` uses.`
- Fix: optional. OG-29 is not merged yet, so it can still be reworded; no record change needed.
