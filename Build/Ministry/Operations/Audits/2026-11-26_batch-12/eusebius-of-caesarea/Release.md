# Release: Eusebius of Caesarea (`eusebius-of-caesarea`)

Released on Mark's word, relayed by the managing session: "release eusebius" (2026-11-28).

## What changed

- `cic-website/data/world-census.json`, entry `eusebius-of-caesarea` only:
  - `longDescription`: the final brief, with the final newline removed (889 words; 887 by the profile tool).
  - `card`: `eusebius-of-caesarea.card.json`, with every exact change from `Final_Check.md` applied (`Final_Check_Applied.md`). All three `secondReading` values are set to "same", from the final check's blind renderings.
  - `teaser`: Card_Edits item 1, word for word.
  - `dates`: changed from "c. 260-339" to "Alive in 303; died after Constantine" (Card_Edits item 2). `start`, `end` and `activeYear` are left as they were; they only place the entry on the map.
  - `modernWorks`: added, with the six works from Card_Edits item 5, placed before `card` as on the other entries.
- `tools/quote_renderings.json`: the entry's five old listings are removed and three new ones added, each with `second_reading` pointing at `Final_Check.md`, verdict "same".
- Rebuilt: `cft-website/index.html`, `cft-website/tree/eusebius-of-caesarea.html`, and `cft-website/tree/palestinian-church-pre-constantinian.html` (the new `dates` in its list of the people it tells).

## Judgment calls

- **Authors' first names.** The modern works' authors are used as Card_Edits gives them: A. C. Zenos, Chester D. Hartranft and Blomfield Jackson. The held files do not give these first names, but the live census already uses the same names on the `epiphanius-of-salamis` and `basil-of-caesarea` entries.
- **Notes.** Each modern work's `note` is the Card_Edits note, starting with a capital letter. The trailing "Moved from the card's `sources.about` word for word" is left out of the Hefele note, because it describes the edit and is not part of the note.
- **The privacy page.** `generate_tree_pages.mjs` also rewrote `cft-website/privacy.html` from an older source. That change is not this story's, so `privacy.html` was restored to `main`'s version. The generator's source for that page is out of step with `main`; this is flagged here and left for its owner.
- **Ledger.** `Earlier-Approved.yaml` has no entry for this story, so nothing was removed from it.

## Rulings for this story

- Slate, hearts and length, and the batch rulings (Mark, 2026-11-27): batch 12 only, as `Story_Header.md` quotes them.
- Length (Mark): "Mark accepted its length, 887 words." This story only.
- Release (Mark, 2026-11-28): "release eusebius". This story only.

## The three reviews

1. Outline check: FIX. 5 blocking and 9 minor findings, applied at the outline.
2. Brief review: REVISE. 7 blocking and 17 minor findings, then one revision and a fresh read with no blocking finding.
3. Final check: the brief passes with 0 blocking. The 3 quotes are all SAME. The card needed 4 changes and 3 minor ones, all applied word for word.

## The grade and the blind check

- **Grade:** whole-text method, weights unchanged. Rigor B (load 2.4), craft C (load 4.7), overall B. Reading grade 8.2 and reading ease 71.6 with names out (9.3 grade with names). The readers' work is in `Grade/`.
- **Blind check:** against the Basil of Caesarea reference. Basil was judged slightly better. Eusebius got B− and Basil B+, so the check passes. The verdict is in `Blind/`.

## Cost

Session record `cost_usd` was $9.10 at the start of release (telemetry, not a bill). The final figure goes to the managing session at merge.

## Not done

- Recording: not done, as instructed.
- The open craft findings are on Mark's page: Nicaea and Tyre told ahead of time in the second paragraph, the Pamphilus sentence that jumps back, and the broken-cup charge left unexplained. None of them is blocking. The brief was not changed after review 3.
