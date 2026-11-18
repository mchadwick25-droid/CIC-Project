# P2-G89b, the eras 8 and 9 rulings carried out: data release 33 — 2026-11-10

Mark's rulings on the P2-G89 gate (https://claude.ai/artifact/34vANZonmFxqr9KXUUUdr4): "all
recommended", G89-8 (a) with the Coptic row from 1517, and G89-9 (a). Record:
`Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`.
Decision-Log entries: CFT, "P2-G89b carried out"; Atlas World Map, the same.

## What is here

- `Drafting_Brief.md`, `Review_Brief.md`, `Slices.md`: the briefs and the eight slices with their
  fixed row IDs.
- `drafts/<slice>/Draft.json`: the reviewed drafts (rows, row changes, links, retirements, holds,
  wants, fact tables). `drafts/<slice>/SOURCES.json` lists every raw online text quoted, with its
  URL. `Changes_r*.md` maps each review finding to its change.
- `reviews/<slice>/Review_r*.json`: the Opus reviews, every slice approved; and
  `reviews/Cap-Ruling_AF-RVA_Sources_Check.json`, the check Mark ordered at the cap.
- `check_draft.py`: reading scores and the verbatim quote check. `apply_g89b.py`: the merge into
  the census; `apply_log.json` its log.
- `HANDOVER.md`: the earlier worker's handover, kept as the record of where this pass began.

## How it ran

1. Six Sonnet drafters finished or wrote the slices; a seventh did the living pass on AF and RV-A.
   Each worked in its own scratch folder and re-fetched every raw text from its URL.
2. An Opus reviewer per slice re-fetched every text independently and checked every quote. Rounds:
   AF 3 (and the ordered check), LA 2, AS1 3, AS2 2, ME1 2, ME2 3, RV-A 3 (and the ordered check),
   RV-B 3.
3. A trial merge of all eight slices through `tools/validate-census.mjs` found 11 errors no slice
   could see alone (symmetric link order, secondary sources for Widely Accepted, country places on
   the place label). Fixes that only lowered a claim or removed data were made; the two links that
   would have needed a new quote enter at Inferential-Thin, their candidate quotes in Open-Gaps.
4. `apply_g89b.py` built release 33; then atlas-sync, the tree pages, the tree site and the
   validator (0 errors).

## Result

26 rows, 34 row changes, 48 links, 4 links retired and replaced. Movements 369 to 395, links 689 to
733, living 264 to 289. Holds and open points: Open-Gaps, "Eras 8 and 9 rulings, Africa holds" to
"Small questions the eras 8 and 9 rulings leave open" (2026-11-10).
