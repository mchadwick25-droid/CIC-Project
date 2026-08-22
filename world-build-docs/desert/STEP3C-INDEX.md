# Desert Monasticism — Step 3c Index (Figures, Contested Claims, World Core)

**Derived from:** 3 figure records (`records/desert/figure/`), 3 contested_claim records (`records/desert/contested_claim/`), and 1 world_core record (`records/desert/world_core/`) — this index is generated against those files and re-checked against them; the records are the source of truth. Re-derivation base: the prior build's cleared Doc_01 (World Identification), Doc_05 (Ecological Reconstruction), Doc_07 (Integrated Ecology Analysis), and Doc_09a/Doc_09b (Story Inventory / World Profile) — all Approved to proceed — plus this build's own already-cleared Step 3a (`LEXICON-INDEX.md`) and Step 3b (`GRAVITY-INDEX.md`) records, which named several of this step's records by id before they existed.

**Scope discipline carried from Step 3b:** figure and contested_claim records carry only the type-specific fields their schema defines (`figure`: `names`, `dates`, `narratable`, `bridge_line`; `contested_claim`: `claim`, `held_against`, `concedes`, `divergence_partners`) plus the shared envelope. `bridge_line`, `claim`, `held_against`, and `concedes` are treated as compiled-facing content under this build's own jargon-leak discipline (matching `world_core.horizon/formation_logic/thinness/cautions`, already gate-enforced by `gate_no_build_attribution`) even though the mechanical gate does not check `figure`/`contested_claim` fields — build-apparatus vocabulary, section-number citations, and cross-record ids are kept out of those four fields by hand-check, verified below. `sources[].locus` and the trailing body carry that apparatus instead.

## Figures

| id | in-world name | dates | narratable | canon_cells | associated with |
|---|---|---|---|---|---|
| `desert.figure.antony` | Antony | c. 251 – 356 | yes | F4-I, F4-P | withdrawal, spiritual-combat, antony-literacy |
| `desert.figure.pachomius` | Pachomius | c. 292 – 346 | yes | F3-I, F4-I | koinonia, authority-tension |
| `desert.figure.evagrius` | Evagrius | c. 345 – 399 | yes | F4-P, F6-I | evagrian-systematization, alexandria-continuity |

**Roster discipline:** limited deliberately to the three figures this corpus's own registered sources support with individually traceable biography (a named primary or near-primary source giving birth/death/floruit and a documented career, not merely a name recurring in the sayings tradition). Amoun and Macarius are named as settlement founders in Doc_01 §2.2 but with no comparable individual source base in this corpus; Pambo is quoted once (Palladius ch. X) but with no birth/death data; Nepheros is explicitly barred from figure-record use by `desert.source.nepheros-archive`'s own standing caution (Step2 Review Round 1, Finding 5 — the archive-to-edition mapping must be re-checked against the editions themselves "before any figure or quote record leans on either monk by name"). No figure record is built for any of these four; a future step revisiting this roster would not be a surprise, but expanding it now would outrun what this corpus can independently verify.

## Contested claims

| id | claim (one line) | poles | canon_cells | classification confidence |
|---|---|---|---|---|
| `desert.contested.antony-literacy` | Was Antony really the unlettered rustic Athanasius portrays? | Athanasius's Vita vs. Rubenson's Letters-based reading (Gould's counter-position against Rubenson specifically) | F3-E | Contested |
| `desert.contested.strand-porousness` | Were the three organizational patterns lived boundaries, or a later compiler's arrangement — and does the Nepheros community represent a fourth pattern? | the Amoun/Antony link and the sayings tradition's own cross-pattern compilation vs. each pattern's own distinct authority/formation logic | F3-T | Contested |
| `desert.contested.alexandria-continuity` | Does desert monastic formation belong to Alexandria's ecology as its intensified continuation? | the Alexandria build's own claim (`alx.contested.desert-attribution`) vs. this world's own distinct-world evidence | F3-T | Contested |

None of the three resolves its own question — each states the claim, the strongest case against it this corpus's own registered evidence supports, and what can honestly be conceded, per this step's own governing instruction (Framework Step 6 / Constitution Article 22's contested-claim discipline, matching Alexandria's `alx.contested.*` convention). No candidate gravity's own classification depends on resolving any of the three — each contested_claim record states explicitly which gravities are and are not put at risk by leaving its question open.

## World core

`desert.core.desert` (time window 320–430) synthesizes the horizon, formation logic, thinness, and cautions established across every prior step. Its seven numbered cautions each name an open question; three of the seven now have a full contested_claim treatment (cautions 3, 4/5, and 7, wired via `relations[]` to `antony-literacy`, `strand-porousness`, and `alexandria-continuity` respectively — caution 4 and 5 are the two facets `strand-porousness` folds into one record). The remaining cautions (1, 2, 6) are single-voice concentration, compiler mediation, and the out-of-horizon trap — all already carried as standing per-source disciplines rather than open contested questions requiring their own record.

**Thin topics** (structured index over the same ground `thinness`/`cautions` state in prose):

| keywords | note |
|---|---|
| liturgy, worship, psalter, prayer, synaxis | liturgical content beyond the Psalter and the Lord's Prayer is Inferential/Thin |
| woman, women, amma, female | no extended first-person narrative centered on a named woman survives |
| melitian, schism, nepheros | documentary business survives; no first-person Melitian voice does |
| wilderness, exile, typology, elijah, israel | a plausible, not yet textually confirmed, scholarly connection |
| authority, rule, elder, office, tension | well-evidenced structurally, not dramatized in any single scene |

**Absent stories** (carried forward from the prior build's cleared Doc_09a §5, restated in the world_core record's own body since this build's own Step 4 story repository has not yet been built): no named woman's own extended narrative; no Melitian ascetic's own first-person account; no single scene dramatizing the authority tension directly. All three are structural absences (who could write, what got kept), not gaps to be filled by invention.

## Cross-build: Alexandria

`desert.contested.alexandria-continuity` is the Desert-side counterpart to the Alexandria build's own `alx.contested.desert-attribution` (`records/alx/contested_claim/`, `origin/world/alexandria`), which explicitly holds its question open "resolvable only there [in the Desert build] — by discovery, not by this world's assertion." This step supplies that discovery pass, built entirely from this corpus's own registered sources — Alexandria's own internal evidence is neither cited nor independently verified here. GRAVITY-INDEX.md's own cross-build sheet (Step 3b) had flagged Alexandria's material as comparative reference only, with no action item, because no open question had yet been raised from Alexandria's own side requiring a Desert-side answer; this record is that answer, generated once `alx.contested.desert-attribution`'s own text was read. No relation crosses the world boundary (a cross-world `relations[]` or `sources[].source_id` target would fail this corpus's own `gate_referential` when run against Desert's records alone) — the connection is carried in prose and by matching record ids only.

## Canon cells

| record | canon_cells |
|---|---|
| `desert.figure.antony` | F4-I, F4-P |
| `desert.figure.pachomius` | F3-I, F4-I |
| `desert.figure.evagrius` | F4-P, F6-I |
| `desert.contested.antony-literacy` | F3-E |
| `desert.contested.strand-porousness` | F3-T |
| `desert.contested.alexandria-continuity` | F3-T |
| `desert.core.desert` | (none — matching Alexandria's own `alx.core.alexandria` convention) |

`figure`, `contested_claim`, and `world_core` are not in `engine/m1/canon.py`'s `substantive_types()` (`{"doctrinal_witness", "term", "story", "quote"}`), so none of the cells above are gate-visible for canon-coverage purposes — matching the precedent already established for `gravity`/`force` at Step 3b. Populated as authored, per this build's own CANON_CELLS discipline, not retrofitted.

## Reciprocity and referential integrity

Every new relation this step added is reciprocated: `desert.contested.antony-literacy` ↔ `desert.gravity.withdrawal`, `desert.gravity.elder-authority`, `desert.term.apatheia`, `desert.figure.antony`, `desert.core.desert`; `desert.contested.strand-porousness` ↔ `desert.gravity.economic-embeddedness`, `desert.gravity.manual-labor`, `desert.gravity.withdrawal`, `desert.core.desert`; `desert.contested.alexandria-continuity` ↔ `desert.gravity.scriptural-engagement`, `desert.gravity.evagrian-systematization`, `desert.figure.evagrius`, `desert.core.desert`; `desert.figure.antony` ↔ `desert.gravity.spiritual-combat` (in addition to the antony-literacy/withdrawal pairs above); `desert.figure.pachomius` ↔ `desert.gravity.koinonia`, `desert.gravity.authority-tension`. `desert.gravity.authority-tension`'s own added relation to `desert.figure.pachomius` is `associated-with`, not `tension-with` — that record's own description states its Interaction is "by construction... with those two gravities specifically" (elder-authority and koinonia), and this step does not introduce a third, figure-level tension Doc_04 never tested. Full gate battery re-run after every edit in this step: 69 records, 0 non-coverage findings.

## Open items carried forward

1. None of the three contested_claim records resolves its own question — that is by design, not an incompleteness of this step. A future step or audit revisiting any of the three with new evidence would not contradict this step's own work, only extend it.
2. The figure roster (Antony, Pachomius, Evagrius) is deliberately narrow; Amoun, Macarius, Pambo, and Nepheros are all named in this corpus but none currently clears the individually-traceable-biography bar this step applied. Revisit if a later step's own needs (Doc_08 forces, Step 4 stories) surface a source base for any of them this step did not have reason to develop.
3. `desert.contested.alexandria-continuity`'s own resolution remains genuinely joint with the Alexandria build — this record states Desert's own position and does not claim to close the question unilaterally.

## Review rounds note (applied)

*(populated after this step's own adversarial review rounds, per this build's standing discipline)*
