# Curation ledger (lpc Stage 2)

State at 2026-10-29 21:20 UTC. Companion to `Stage1_Ledger.md` and `Stage2_Change_Orders.md`. Plain facts; the sampling reviews and redo reports hold the line-level detail.

## Counts on main

- 237 partial or unmarked plain-text files in the union; 66 belong to lpc's shelf.
- 52 curation files on main: 2 pilots, wave 1a (37), wave 1b (13).
- Status: 39 `drafted`, 11 `needs-redo`, 2 `sampled-ok`.
- `sampled-ok`: `augustine_de-catechizandis-rudibus-lat-eng_christopher1926`, `harnack_vita-cypriani-commentary-lat-deu_1913`.
- Sampled so far: 13 of 52 (groups A and B in full; group C 1 of 25; the 13 wave 1b files not yet sampled). 11 of 13 needed a redo.

## `needs-redo` (defects in `Curation_Sample_Review_Wave1a_A.md` and `_B.md`)

| File | Defect |
|---|---|
| `augustine_doctrina-christiana-enchiridion-lat_bruder1838` | about 54 printed chapter heads missed |
| `augustine_sermones-1-340-lat_migne-pl38` | false oversize justification; sermons print CAPUT heads |
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39` | one numeral fixed from sequence alone; false oversize justification |
| `augustine_sermones-post-maurinos-reperti-lat_morin1930` | Casinenses sermons not divided |
| `optatus_against-the-donatists` | printed editor's heading hidden as furniture; unexplained gap |
| `codex-theodosianus_latinlibrary` | paragraph text addressed as `pr`; duplicate law 16.7.3 |
| `acta-martyrum-selecta_gebhardt1902` | missed Pionius chapter heads; one Greek chapter mis-addressed |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902` | Pionius split at a running head, not at its chapters |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929` | missed Pionius chapter heads; wrong scheme statement |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | three address labels the edition does not print |
| `possidius_vita-augustini_weiskotten1919` | missed sections in chapter 30 |

Recurring causes: a margin line number in front of a numeral, numerals in Greek letters, an OCR numeral with a dropped I read as a number, a running head used to split a division, and a false `allow_oversize` justification. `curate check` does not see these; the tooling work adds checks for them.

## Not curated (12 hard files, plus the two Cyprian CSEL volumes not started)

Lauchert canons; Prosper (Chronica minora); Turner (Ecclesiae occidentalis monumenta); Mansi vol. 3; Zeno-Optatus (Migne PL11); African Codex (Bruns); Uhl (Cyprian, German); Hayd (Augustine on John, German); Guillon (Cyprian, two French volumes); Gsell (inscriptions); the German Postille; Cyprian CSEL 3 Hartel pars 1-2 and pars 3. Reasons are in the wave reports: OCR-damaged or doubled numerals that cannot be read without guessing, or missing title leaves. They wait on the curation tooling fixes.

## Tooling

Merged: long Roman numerals (to 3,888) and German, French, Latin and Italian ordinals (PR 1310). Open: `fixes` not passed through `ocr_map`; adjacent apparatus ranges; explicit divisions setting a parent for later rules; page-head splitting; a rule context condition; a per-rule language guard; and the new checker rules (unexplained numbering gaps fail; all gaps printed; false oversize justifications and missed heading-like lines reported).

## First thing on resume

1. Merge the redo PRs for groups A and B when green; re-sample them with a different Opus reviewer.
2. Finish the curation tooling items, then curate the hard files.
3. Sample group C (24 files) and the 13 wave 1b files; treat any numeral read from sequence alone as a defect.
