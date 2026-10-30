# Stage 2: lpc row fields, status at checkpoint

Status: paused at a usage checkpoint. No staging file was edited. Fields set: 0 of 215 rows for each of `language`, `locus_ids`, `voice_of`, `date`. `documented_exchange` is deliberately never set here.

## What was established

- lpc has 215 rows in staging over 112 files; 37 of the 215 staging rows are shared with other worlds, so any field written to them must hold for every world.
- `language`: every file's language was checked against its header and sampled stopword counts. Files with no filename code: the ThML `anf*`/`npnf*` files, Benson and Optatus (Vassall-Phillips) are `eng`; Possidius (Weiskotten) is `lat-eng`; the Augustine CSEL 57, Petschenig, Bruns, Theodosianus, Hartel pars 1-2 and `pl11` files are `lat`; Monceaux tomes 1-3 are `fra`. Rows in multi-language volumes (Gebhardt, Knopf, Lauchert, Perpetua) take the language of the row's own work (the Latin acts are `lat`), not the whole filename.
- `locus_ids`: segmenter division lists come from `answering_library.segment.plan(entry_for(file))`. Curated files use their curation ids; ThML files use roman-path ids. Findings that shape the work:
  - Many ThML container divisions have no unit of their own, so a named div such as `div2 4.4` must be expanded to every unit locus beneath it, in document order. Some units have stray ids with no parent prefix (`II_1`, `IV_1`, `LVI`, `div`), so prefix matching alone misses them.
  - Whole-file rows: single-work TEI files, slice files (Bardenhewer, Hefele-Leclercq, Raulx) and the "whole file" rows get `[whole-file]`.
  - Shared curated files map by piece or work prefix: Gebhardt `piece4/11/13/14`, Knopf `act6/13/15/16`, Zycha CSEL 41 one prefix per work, Petschenig one prefix family per work, Duchesne `chapter20` (tome 1), `chapter8` (tome 3), Monceaux tomes 6-7 `l11/*` from line 21985. For Sermones ad populum, `sermon1`-`sermon363` and `sermon364`-`sermon396`.
  - ThML rows map by roman path: `anf05` `iv.iii`, `iv.iv`, `iv.v.i`-`iv.v.xii`, `iv.vi`, `iv.vii`, `vii.iii`, `vii.iv`.
  - The two rows on `augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt` (indices 47, 48) should stay unset. The file's divisions are paragraph numbers (`n1976` straddles the line-46795 boundary) and the Epistle's end is not stated.
  - Mansi vols 3 and 4 (start lines only), Sermones Guelferbytani, Cyprian opera spuria, Codex canonum Africanae, Lauchert, Prosper, Turner, `pl11`, Optatus appendix, Perpetua, Duchesne tome 2 and Mansi tome 2 still need a look at their division lists before deciding set or unset.
- `voice_of` and `date`: not started.

## First thing on resume

Re-run the division listing (about two minutes), write the per-row spec, add a script that checks every id against the division list, insert keys into the staging rows, then run the merge, `--check`, `corpus_map.py` and `tests_corpus_map.py`, and prove with `git diff` that only additions occurred.
