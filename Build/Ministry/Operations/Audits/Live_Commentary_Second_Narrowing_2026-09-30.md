# Live-surface commentary: the second narrowing (2026-09-30)

Companion to the rule changes in `tools/check_live_commentary.py`. It records how each change was measured and the real process lines the changes stop flagging, so they are not lost. It follows `Live_Commentary_Unresolved_Sample_2026-09-30.md`.

## Method

1. Sampled the 829 lines left in scope B after the "unresolved" change and read them by group.
2. Changed five rules. After each, re-ran the whole-tree scan and compared it line by line with `main`.
3. Read every dropped line in records, engine and corpus-map. Website and package lines are compiled from records and were counted once, at the record.

## Result

- REWRITE plus ROUTE lines fell from 4,653 to 4,026 (627 lines, 13%).
- No line became newly flagged.

| Change | Lines dropped | What they were |
|---|---|---|
| Taxonomy tag on a `name:` line | 192 (records) | `[2A - ongoing/external]`, `[PRIMARY]`. `engine.prose.strip_name_taxonomy_tag` removes the tag before the compiled prompt or a citation card shows the name. The same tag in any other line is still flagged. |
| Ruling-named identifier in Python code | 72 (engine) | `r27_enforce`, `r27_regenerated`, `r27_enforcement_exhausted` as keyword arguments, keys and asserts. The same identifier in a comment is still flagged. |
| "at the gate" | 58 | A physical gate: "hanged at the gate of the patriarchate", "the beggar at the gate". The era gate is still flagged when it names an era, "same gate" or "Freeze", or follows a process verb ("corrected at the gate", "run at that gate"). |
| "open question" and "still open" | 302 | Real uncertainty in a source or a tension a world holds, plus code strings such as `"round still open - continue it"`. Both are cues only with a qualifier ("open question for now", "still open for Mark"), the same rule as "unresolved". |
| "opens round N" | 3 (engine) | A table round opening, not a review round. |

## Real process lines the narrowed rules no longer flag

Reading every dropped line in records and the corpus map found 18 that narrate the build or the mapping. Each is a state note ("carried here", "this build has not answered", "still open, held here"), not a statement about the sources.

Records:

- `records/cappadocian/doctrinal_witness/cappadocian.dw.macrina-and-its-cost.md:18`
- `records/cappadocian/figure/cappadocian.figure.macrina.md:14`
- `records/don/doctrinal_witness/don.dw.what-we-did-with-the-power-we-had.md:169`
- `records/don/search_record/don.search.gesta-collationis-carthaginiensis.md:36`
- `records/don/search_record/don.search.unrowed-vendored-sweep.md:243`
- `records/don/source/don.source.ziwsa-optatus-libri-vii-csel26.md:17`
- `records/lpc/honest_limit/lpc.limit.rural-punic-berber-life.md:19`
- `records/lpc/source/lpc.source.augustine-general-correspondence.md:17`
- `records/lpc/source/lpc.source.dossey-peasant-and-empire-in-christian-north-africa.md:32`
- `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md:376`
- `records/syr/search_record/syr.search.bar-hebraeus-chronicon-pd.md:44`
- `records/witt/force/witt.force.inheritance-refused.md:15`

Corpus map (assignment status left open):

- `cic/corpus-map/_staging/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.yaml:128`
- `cic/corpus-map/_staging/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.yaml:342`
- `cic/corpus-map/_staging/npnf214_seven-ecumenical-councils.yaml:532`
- `cic/corpus-map/apocryphal-and-pseudepigraphal-literature.yaml:168`
- `cic/corpus-map/imperial-juridical-christianity.yaml:77`
- `cic/corpus-map/valentinian-and-other-gnostic-christianities.yaml:16`

Five of the 18 are lpc's, whose build thread is active and owns them. They belong to the batched pass recorded in cappadocian OG-29 and OG-31, not to a line-level edit.

## Era-gate lines

No era-gate line in a live surface was lost. The one bare "at the gate" that names the era gate ("corrected at the gate from 330 to 451") and the process-verb form ("run at that gate and cleared") are both still flagged.
