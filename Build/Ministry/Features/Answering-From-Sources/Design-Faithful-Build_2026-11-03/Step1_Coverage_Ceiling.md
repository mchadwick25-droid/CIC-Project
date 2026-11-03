# Step 1 counts (read-only and deterministic; the script and its raw output are `count.py` and `counts.json` beside this file)

Worlds with a seed file (Build/worlds/<w>/build/<w>_Passage_Seeds.yaml): alx, lpc, rzg, syr. No other world has one.

## How "reviewed record reaches a sub-question" was determined
Engine path: engine/m4/subquestion_routing.py `coverage_entries` (lines 68-79) reads the world's Answers_Sidecar (`subquestions: id -> {records: [...]}`), keeps a record only if its id is in the compiled repository and its record_type is in COVERAGE_KEY_BY_RECORD_TYPE (lines 24-34). Resolution to a split parent: `resolve` (lines 44-52). I applied the same test: sidecar lists >=1 record id that is in the latest packages/<w>/<stamp>/compiled/repository.json with a mapped record_type. Also checked records/<w>/*/*.md `status:` of each listed id: all are `ready`, none `draft`; none unheld.
Sidecar provenance differs: lpc = Build/worlds/lpc/build/lpc_Answers_Sidecar.yaml, `reviewed: true` (hand-checked). alx/syr/rzg = Build/Ministry/Features/Answering-From-Sources/Cross-World-Test_2026-11-02/<w>/<w>_Answers_Sidecar.yaml, built mechanically by tools/build_answers_sidecar.py from Question-Coverage maps, NOT reviewed (README line 9). So "reviewed" holds for record status (ready) but not for the sub-question-to-record mapping on alx/syr/rzg. No sidecar for these three is in Build/worlds/<w>/build/.
Usable seed = shelf_binding startswith "row narrowed" (passage_offer_build.py LENS_BINDING, line 41 test). Only two binding values exist: "row narrowed by locus_ids to this division..." and "file level only: the file is on the world's shelf...".

## Table (130 base sub-questions; lpc also has 19 split ids C#.S#a, shown separately)
| | lpc (130 base) | lpc (149 incl 19 splits) | alx | syr | rzg |
|---|---|---|---|---|---|
| sub-questions | 130 | 149 | 130 | 130 | 130 |
| with >=1 record | 75 | 80 | 50 | 56 | 39 |
| with >=1 usable ("row narrowed") seed | 41 | 52 | 0 | 0 | 31 |
| seeds all file-level only | 4 | 4 | 28 | 19 | 0 |
| neither records nor usable seeds | 29 | 35 | 80 | 74 | 69 |
| records AND usable seeds | 15 | 18 | 0 | 0 | 9 |
| total seeds | 119 | 143 | 52 | 49 | 50 |
| usable seeds | 84 | 102 | 0 | 0 | 50 |
| file-level-only seeds | 35 | 41 | 52 | 49 | 0 |
| voiceable (all seeds) | 32 | 39 | 0 | 0 | 13 |
| etic (all seeds) | 87 | 104 | 52 | 49 | 37 |
| voiceable among usable | 32 | 39 | 0 | 0 | 13 |
| etic among usable | 52 | 63 | 0 | 0 | 37 |
Note: alx and syr have zero voiceable and zero lens-usable seeds, so under the lens rule they offer nothing from seeds; syr header says voiceable 0, etic 49.

## Task 2: file-level-only seeds, alx (52 seeds, 11 files, 28 sub-questions)
M = multi-work volume, S = single-work file (single/multi judged from file name and corpus-map; anf/npnf = M)
| file | kind | seeds | sub-questions |
|---|---|---|---|
| anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml | M | 9 | C10.S1 C10.S5 C11.S3 C12.S1 C2.S8 C7.S4 |
| anf04_tertullian4-minucius-felix-commodian-origen1-2.xml | M | 4 | C11.S2 C3.S2 C8.S5 C9.S1 |
| anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml | M | 7 | C13.S1 C7.S2 C8.S3 C8.S5 |
| anf07_lactantius-apostolic-constitutions-didache-liturgies.xml | M | 4 | C12.S1 C13.S5 C6.S6 |
| anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml | M | 4 | C13.S3 C13.S5 C8.S5 |
| anf09_gospel-of-peter-diatessaron-origen-commentaries.xml | M | 3 | C1.S7 C12.S1 C13.S1 |
| npnf201_eusebius-church-history-life-of-constantine.xml | M (2 works) | 3 | C5.S1 C5.S3 C9.S1 |
| npnf202_socrates-sozomen-ecclesiastical-histories.xml | M (2 works) | 2 | C9.S5 |
| npnf204_athanasius-select-works-letters.xml | M | 9 | C13.S2 C2.S2 C2.S3 C2.S4 C2.S7 C5.S1 C9.S3 |
| npnf214_seven-ecumenical-councils.xml | M (council acts, many docs) | 6 | C6.S6 C7.S2 C7.S5 C8.S3 |
| origen_philocalia_lewis1911.txt | S (one work) | 1 | C5.S2 |
(counts per file above: 9+4+7+4+4+3+3+2+9+6+1 = 52)

## syr (49 seeds, 10 files, 19 sub-questions)
| file | kind | seeds | sub-questions |
|---|---|---|---|
| addai_doctrine-of-addai.txt | S | 2 | C6.S1 C6.S2 |
| anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml | M | 12 | C10.S1 C10.S5 C12.S1 C13.S2 C2.S1 C8.S5 |
| anf07_lactantius-apostolic-constitutions-didache-liturgies.xml | M | 11 | C10.S5 C12.S1 C13.S2 C13.S5 C6.S6 |
| anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml | M | 7 | C13.S2 C13.S3 C13.S5 C8.S5 |
| anf09_gospel-of-peter-diatessaron-origen-commentaries.xml | M | 5 | C1.S7 C10.S1 C13.S1 C5.S8 |
| ephraim_prose-refutations_mitchell1912-1921.txt | M (corpus-map has separate rows: Against Marcion discourses, Discourses to Hypatius...) | 2 | C1.S7 C8.S5 |
| npnf202_socrates-sozomen-ecclesiastical-histories.xml | M | 1 | C9.S5 |
| npnf208_basil-letters-select-works.xml | M | 1 | C9.S4 |
| npnf213_gregory-great-ephraim-syrus-aphrahat.xml | M | 6 | C10.S5 C13.S1 C13.S5 C2.S8 C7.S7 C8.S3 |
| palladius_paradise-v1-syriac_budge1907.txt | M (corpus-map rows: Life of Anthony, Paradise Book I, Budge preface...) | 2 | C13.S1 C8.S5 |
(12+11+7+5+2+2+1+1+6+2+... check: 2+12+11+7+5+2+1+1+6+2 = 49)
Single-work judgment for addai/origen_philocalia is from file name and corpus-map rows only; I did not open the files.

## Task 3: index keys
Index schema (Sandbox/answering-library/index/store.py):
- sub_question: named in KEY_KINDS (store.py:51) and the `keys` table has a `kind` column (store.py:45). NOTHING inserts a sub_question key: the only INSERT INTO keys is store.py:131 (kind "work_locus"). Existing alx/syr sqlite: keys table holds only work_locus (alx 56,559 rows, syr 32,290). Nothing in engine/m4 reads a sub-question key from the index; sub-question reach is by the seed file -> offer JSON (passage_offer_build.py:68-117 writes offer keyed by sub-question; engine/m4/passage_offer.py:72-77 `select` reads it; turn_prep.py:606-607 calls it).
- scripture_ref: named in KEY_KINDS (store.py:51) only. No column, no insert, no reader anywhere (grep of Sandbox/answering-library, engine, cic/engine: no other hit).
- work_locus: exists. Column passages.work_locus (store.py:36) + index (store.py:48) + keys rows (store.py:131); value is "<file>#<division_locus>" (store.py:115) i.e. file plus division, not work. Reader: retrieve.py:95-101 `by_work_locus`; no caller in engine/m4 (engine/m4 only touches sqlite in passage_offer_build.py:62, build-time, reading `passages` by passage_id and `passage_rows`, plus engine/m4/store.py which is the turn store, unrelated). Search at build/bench time is FTS5 only (retrieve.py:41-92 `search`, store.py:41); not called from engine/m4.
- At question time the engine reads the offer JSON (frame `passage_offer`, turn_prep.py:606), not the sqlite.
Embedder: only the Protocol in index/embeddings.py (9 lines, no class). grep of `embed` in .py files finds no implementation in Sandbox/answering-library or engine/m4 (matches elsewhere are unrelated: quotation embedding in engine/m1, etc.). Undetermined only in that I did not read each unrelated hit.
SQLite index files on disk: none in the repository (the index build folder is gitignored, and no sqlite file sits under the texts folder). Built indexes existed only in the session scratch area: alx 538 MB, syr 290 MB, rzg 257 MB, lpc 851 MB. They are rebuilt from the vendored texts by the Library builder.
