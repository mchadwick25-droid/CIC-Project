# P2-G89c, the held eras 8 and 9 items the Library now sources: data release 34 — 2026-11-10

Under Mark's eras 8 and 9 gate ruling ("take every recommendation"), items held only because their
sources were not in the Library enter once the Library holds them (the same change order, G89-6 a).
Each item was first tested against its vendored source. Decision-Log entries: CFT, "P2-G89c carried
out"; Atlas World Map, the same. Open-Gaps: "The held eras 8 and 9 items the Library's sources now
carry", "Two Section A questions for Mark" and "Small points P2-G89c leaves open" (2026-11-10).

## What is here

- `Drafting_Brief.md`, `Review_Brief.md`: the briefs (each builds on the P2-G89b briefs in
  `../2026-11-10_eras8-9-rulings/`).
- `drafts/<slice>/Draft.json`: the reviewed drafts; `Changes_r*.md` maps each finding to its
  change. Slices: `main` (the two regrades and the VOC link; raw texts listed in `SOURCES.json`),
  `ASA` (AP11, AP10; AP7 held), `ASB` (AP15's Protestant line, AP12's Anglican line), `LA`
  (Saint-Domingue, the Bethlemites, Holly; LA8-8 held), `RV7` (the Transylvanian Unitarian row).
- `reviews/Review_<slice>_r*.json`: the Opus reviews. Rounds: main 1, LA 2, ASA 2, ASB 2, RV7 2;
  every slice approved.
- `SectionA_ME6_ME20.md`: the Section A assessment of the Tolstoyans and the Dukhobors, for Mark.
- `apply_g89c.py`: the merge into the census (the P2-G89b script with this chunk's slices);
  `apply_log.json` its log.

## How it ran

1. Four Sonnet drafters, each in its own scratch folder, tested and drafted the items from the
   Library files; the worker drafted the regrades and the VOC link.
2. An Opus reviewer per slice re-opened every Library quote at its lines, re-fetched every raw text
   and checked date-bearing OCR quotes on the archive.org page images where the scan was damaged.
3. `apply_g89c.py` built release 34; then atlas-sync, the tree pages, the tree site, the corpus-map
   merge (four shelf rows moved onto the entries that now carry them, one added) and the validator
   (0 errors).

## Result

1 row, 8 row changes, 3 new links, 2 links regraded. Movements 395 to 396, links 733 to 736.
