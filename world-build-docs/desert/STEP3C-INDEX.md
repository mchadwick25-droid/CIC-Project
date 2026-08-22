# Desert Monasticism — Step 3c Index (Figures, Contested Claims, World Core)

**Derived from:** 4 figure records (`records/desert/figure/`), 3 contested_claim records (`records/desert/contested_claim/`), and 1 world_core record (`records/desert/world_core/`) — this index is generated against those files and re-checked against them; the records are the source of truth. Re-derivation base: the prior build's cleared Doc_01 (World Identification), Doc_05 (Ecological Reconstruction), Doc_07 (Integrated Ecology Analysis), and Doc_09a/Doc_09b (Story Inventory / World Profile) — all Approved to proceed — plus this build's own already-cleared Step 3a (`LEXICON-INDEX.md`) and Step 3b (`GRAVITY-INDEX.md`) records, which named several of this step's records by id before they existed.

**Scope discipline carried from Step 3b:** figure and contested_claim records carry only the type-specific fields their schema defines (`figure`: `names`, `dates`, `narratable`, `bridge_line`; `contested_claim`: `claim`, `held_against`, `concedes`, `divergence_partners`) plus the shared envelope. `bridge_line`, `claim`, `held_against`, and `concedes` are treated as compiled-facing content under this build's own jargon-leak discipline (matching `world_core.horizon/formation_logic/thinness/cautions`, already gate-enforced by `gate_no_build_attribution`) even though the mechanical gate does not check `figure`/`contested_claim` fields — build-apparatus vocabulary, section-number citations, and cross-record ids are kept out of those four fields by hand-check, verified below. `sources[].locus` and the trailing body carry that apparatus instead.

## Figures

| id | in-world name | dates | narratable | canon_cells | associated with |
|---|---|---|---|---|---|
| `desert.figure.antony` | Antony | c. 251 – 356 | yes | F4-I, F4-P | withdrawal, spiritual-combat, antony-literacy |
| `desert.figure.pachomius` | Pachomius | c. 292 – 346 | yes | F3-I, F4-I | koinonia, authority-tension |
| `desert.figure.evagrius` | Evagrius | c. 345 – 399 | yes | F4-P, F6-I | evagrian-systematization |
| `desert.figure.sarah` | Sarah | (none registered) | yes | F6-P | geron-abba-amma, elder-authority |

**Roster discipline (revised, Step3c Round 1 review Finding S3):** an earlier draft of this table justified excluding Amoun, Macarius, and Pambo by claiming this corpus has "no comparable individual source base" for them — checked directly against `desert.source.palladius-lausiac-history`, a vendored, `verified-direct`, `load-bearing` source: ch. VIII gives Amoun a complete career (marriage, eighteen years, then founding two cells at Nitria, then twenty-two years more, then death); ch. XVII gives Macarius of Egypt a fixable floruit (retired to the desert at thirty, received grace at forty, ninety years total); ch. X quotes Pambo at least four times and gives his age at death (seventy). The claim was false. The actual, defensible bar the three built figures each clear from a registered record is narrower: **absolute birth/death years independently registered in this corpus** — Antony (Jerome, *De viris illustribus* 88, vendored: "Born 251, died 356"), Pachomius (`desert.source.pachomian-corpus.md`: "c. 292-346"), Evagrius (Palladius ch. XXXVIII, vendored: died "at the age of fifty-four," independently dating his birth). Amoun, Macarius, and Pambo each have a real, individually traceable career but no absolute dates anywhere in this corpus; that is the honest reason they are not built as figure records here, not an absence of source material. Nepheros remains barred outright by `desert.source.nepheros-archive`'s own standing caution (Step2 Review Round 1, Finding 5 — the archive-to-edition mapping must be re-checked against the editions themselves "before any figure or quote record leans on either monk by name").

**The gender axis (Step3c Round 1 review Finding S4):** `desert.source.apophthegmata-patrum`'s own cleared body names an obligation aimed specifically at "the amma figure records at step 3," tied to Doc_02 §6's Affirmative Duty gender axis. An earlier draft of this step built three male figure records and passed over that obligation in silence. `desert.figure.sarah` now answers it with real content rather than a logged deferral alone: among the three named ammas (Syncletica, Theodora, Sarah), Sarah is the one this corpus can trace to a specific, independently verified saying (the prior build's cleared Doc_09a Story 2.3, itself web-verified). Syncletica and Theodora remain unbuilt as figure records — both are genuinely named and attested, but this corpus currently holds only bare naming for either, not a specific saying or encounter, and a figure record built on bare naming risks inventing the concreteness a `bridge_line` needs. This is a deliberate, logged decision (see `desert.figure.sarah`'s own body), not a second silent omission.

## Contested claims

| id | claim (one line) | poles | canon_cells | classification confidence |
|---|---|---|---|---|
| `desert.contested.antony-literacy` | Was Antony really the unlettered rustic Athanasius portrays? | Athanasius's Vita vs. Rubenson's Letters-based reading (Gould's counter-position against Rubenson specifically) | F2-E | Contested |
| `desert.contested.strand-porousness` | Were the three organizational patterns lived boundaries, or a later compiler's arrangement? | the Kellia founding link and the sayings tradition's own cross-pattern compilation vs. each pattern's own distinct authority/formation logic; the Nepheros community as evidence the typology may be incomplete | F3-T | Contested |
| `desert.contested.alexandria-continuity` | Does desert monastic formation belong to Alexandria's ecology as its intensified continuation? | the Alexandria build's own claim (`alx.contested.desert-attribution`) vs. this world's own distinct-world evidence | (none) | Contested |

None of the three resolves its own question — each states the claim, the strongest case against it this corpus's own registered evidence supports, and what can honestly be conceded, per this step's own governing instruction (Framework Step 6 / Constitution Article 22's contested-claim discipline, matching Alexandria's `alx.contested.*` convention).

**Canon-cells basis (added, Round 1 review Finding M7):** `desert.contested.antony-literacy` moved from an earlier F3-E assignment (which the fleet's canon questions do not actually support — F3-E is the catacombs/Constantine cell) to **F2-E**, which holds "Isn't most of what's said about you legend, collected centuries later?" and "Where is your own record thinnest?" — a direct fit, already shared with `desert.term.apophthegma`. `desert.contested.strand-porousness` keeps **F3-T** ("Was your church 'Catholic'?... Did you have denominations — how did you handle other communities who called on Christ differently?"), a good fit for its Melitian-adjacent material. `desert.contested.alexandria-continuity` moved from F3-T (no genuine fit — nothing in the fleet's canon questions asks about cross-world scholarly attribution) to **no cells at all**, matching `alx.contested.desert-attribution`'s own `canon_cells: []` — this is a build-internal boundary question, not one a participant would put to a Representative, and the earlier assignment was reaching for a cell that didn't exist rather than leaving the field honestly empty.

**Gravity-risk statement, corrected (Round 1 review Finding M6):** an earlier draft claimed "each contested_claim record states explicitly which gravities are and are not put at risk by leaving its question open" as a universal. Checked against all three: `antony-literacy.concedes` does this precisely. `strand-porousness.concedes` states the three-pattern finding is held as settled structure, not a gravity-classification statement. `alexandria-continuity.concedes` speaks to the systematized register's own scope, not to any gravity's classification. The universal is dropped; what is true is narrower — no candidate gravity anywhere in this corpus has its Primary/Supporting/Tensional classification made to depend on resolving any of the three open questions, which each record's own body states in its own terms.

## World core

`desert.core.desert` (time window 320–430) synthesizes the horizon, formation logic, thinness, and cautions established across every prior step. Of its seven numbered cautions, **three** have a full contested_claim treatment: (3) at `antony-literacy`, (5) at `strand-porousness`, (7) at `alexandria-continuity`, wired via `relations[]`. **Caution (4)** (the Melitian ecclesial-boundary question) does **not** have one — an earlier draft of this world_core wired it to `strand-porousness` alongside caution (5), contradicting that record's own explicit disclaimer of the ecclesial-identity axis (Round 1 review Finding S6, now corrected in both records). Caution (4) remains a genuinely open item carried at its source, `desert.source.nepheros-archive`'s own standing caution, and at Doc_01 §11 item 1 / Doc_05 §4 — not an oversight, and not folded into a record that says it does not cover that ground. Cautions (1), (2), and (6) are single-voice concentration, compiler mediation, and the out-of-horizon trap — standing per-source disciplines rather than open contested questions requiring their own record.

**Thin topics** (structured index over the same ground `thinness`/`cautions` state in prose):

| keywords | note |
|---|---|
| liturgy, worship, psalter, prayer, synaxis | liturgical content beyond the Psalter and the Lord's Prayer is Inferential/Thin |
| woman, women, amma, female | no extended first-person narrative centered on a named woman survives (though one saying, Sarah's, now has its own figure record) |
| melitian, schism, nepheros | documentary business survives; no first-person Melitian voice does |
| wilderness, exile, typology, elijah, israel | a plausible, not yet textually confirmed, scholarly connection |
| authority, rule, elder, office, tension | well-evidenced structurally, not dramatized in any single scene |

**Absent stories** (carried forward from the prior build's cleared Doc_09a §5, restated in the world_core record's own body since this build's own Step 4 story repository has not yet been built): no named woman's own *extended* narrative (Sarah's single saying does not close this absence — it is one attributed reply, not a narrative on the scale of the founding accounts); no Melitian ascetic's own first-person account; no single scene dramatizing the authority tension directly. All three are structural absences (who could write, what got kept), not gaps to be filled by invention.

## Cross-build: Alexandria

`desert.contested.alexandria-continuity` is the Desert-side counterpart to the Alexandria build's own `alx.contested.desert-attribution` (`records/alx/contested_claim/`, `origin/world/alexandria`), which explicitly holds its question open "resolvable only there [in the Desert build] — by discovery, not by this world's assertion." This step supplies that discovery pass, built entirely from this corpus's own registered sources — Alexandria's own internal evidence is neither cited nor independently verified here. GRAVITY-INDEX.md's own cross-build sheet (Step 3b) had flagged Alexandria's material as comparative reference only, with no action item, because no open question had yet been raised from Alexandria's own side requiring a Desert-side answer; this record is that answer, generated once `alx.contested.desert-attribution`'s own text was read. No relation crosses the world boundary (a cross-world `relations[]` or `sources[].source_id` target would fail this corpus's own `gate_referential` when run against Desert's records alone) — the connection is carried in prose and by matching record ids only.

**Corrected, Round 1 review Finding S1:** an earlier draft's only concession claimed Evagrius's own systematized writing carried "genuinely Origenist-adjacent conceptual vocabulary" as evidence of Alexandrian conceptual affinity — checked against `desert.gravity.evagrian-systematization`'s own transmission-history note (which names only a *reception* history, the later controversy and condemnation, and explicitly declines to let it decide anything) and against `desert.source.evagrius-praktikos` (which attributes his systematized scheme to Greek philosophical training under the Cappadocian Fathers, not to Alexandria). No record in this corpus supports the claim. The concession is rebuilt on this corpus's actual Origenist-adjacent thread: Rubenson's contested reading of the *Letters* attributed to Antony as "substantively Origenist," already the full subject of `desert.contested.antony-literacy` — the two records are now cross-related. **Also corrected, Finding S5:** `held_against[3]` claimed the person-vs-office authority tension (gravity 10) "already accounts for" the Theophilus/Origenist-controversy contact with Alexandria's episcopal authority; that gravity's own description states its Interaction is "by construction... with those two [other] gravities specifically" and excludes external contact by definition. Reworded to state plainly that this contact remains an unresolved feature of the world's own boundary, per Doc_01 §5(b)/§11. **Also corrected, Finding M13:** the body's claim that Doc_01 makes no comparison to Alexandria "on this record's own initiative" was false — Doc_01 §4, Doc_05 §8.2, and Doc_09b §3 all make the comparison directly; the sentence claiming a blank page is removed.

## Canon cells

| record | canon_cells |
|---|---|
| `desert.figure.antony` | F4-I, F4-P |
| `desert.figure.pachomius` | F3-I, F4-I |
| `desert.figure.evagrius` | F4-P, F6-I |
| `desert.figure.sarah` | F6-P |
| `desert.contested.antony-literacy` | F2-E |
| `desert.contested.strand-porousness` | F3-T |
| `desert.contested.alexandria-continuity` | (none — matching `alx.contested.desert-attribution`'s own convention) |
| `desert.core.desert` | (none — matching Alexandria's own `alx.core.alexandria` convention) |

`figure`, `contested_claim`, and `world_core` are not in `engine/m1/canon.py`'s `substantive_types()` (`{"doctrinal_witness", "term", "story", "quote"}`), so none of the cells above are gate-visible for canon-coverage purposes — matching the precedent already established for `gravity`/`force` at Step 3b. Populated as authored, per this build's own CANON_CELLS discipline, not retrofitted.

## Reciprocity and referential integrity

Every relation this step added is reciprocated, re-derived mechanically from the record files rather than read off this list: **38** directed relation ends corpus-wide involving a Step 3c record, over **19** distinct pairs, all `associated-with` and correctly symmetric, zero dangling. The pairs: `desert.contested.antony-literacy` ↔ `desert.gravity.withdrawal`, `desert.gravity.elder-authority`, `desert.term.apatheia`, `desert.figure.antony`, `desert.core.desert`, `desert.contested.alexandria-continuity`; `desert.contested.strand-porousness` ↔ `desert.gravity.economic-embeddedness`, `desert.gravity.manual-labor`, `desert.gravity.withdrawal`, `desert.core.desert`; `desert.contested.alexandria-continuity` ↔ `desert.gravity.scriptural-engagement`, `desert.core.desert` (plus `antony-literacy` above); `desert.figure.antony` ↔ `desert.gravity.spiritual-combat`, `desert.gravity.withdrawal` (plus `antony-literacy` above); `desert.figure.pachomius` ↔ `desert.gravity.koinonia`, `desert.gravity.authority-tension`; `desert.figure.evagrius` ↔ `desert.gravity.evagrian-systematization`; `desert.figure.sarah` ↔ `desert.term.geron-abba-amma`, `desert.gravity.elder-authority`. `desert.gravity.authority-tension`'s own relation to `desert.figure.pachomius` is `associated-with`, not `tension-with` — that record's own description states its Interaction is "by construction... with those two gravities specifically" (elder-authority and koinonia), and this step does not introduce a third, figure-level tension Doc_04 never tested (re-confirmed correct on independent review). Full gate battery re-run after every edit in this step: 70 records, 0 non-coverage findings.

## Open items carried forward

1. None of the three contested_claim records resolves its own question — that is by design, not an incompleteness of this step. A future step or audit revisiting any of the three with new evidence would not contradict this step's own work, only extend it.
2. Amoun, Macarius, and Pambo each have an individually traceable career in this corpus's own vendored Palladius chapters but no absolute birth/death years anywhere in this corpus - the bar the four built figure records each clear. Revisit if a later step's own needs (Doc_08 forces, Step 4 stories) surface dated material for any of them, or if the roster bar itself should be loosened.
3. Syncletica and Theodora remain unbuilt as figure records for the reason stated under Figures above (bare naming only, no specific verified saying) - revisit if a story or quote record independently verifies concrete material for either.
4. `desert.contested.alexandria-continuity`'s own resolution remains genuinely joint with the Alexandria build — this record states Desert's own position and does not claim to close the question unilaterally.
5. `desert.core.desert`'s caution (4) (the Melitian ecclesial-boundary question) has no contested_claim record of its own - a genuinely open item, carried at its source record and at Doc_01/Doc_05, not folded into `strand-porousness` (see World core above).

## Review rounds note (applied)

Step3c Review Round 1 (`world-build-docs/desert/reviews/Step3c_Review_Round1.md`)
found the fabrication check clean - every named person, place, title,
date and number across all seven then-existing new records' substantive
fields resolved to a registered source, a vendored file, or a cleared
prior-build document, both direct Vita quotations were verbatim-accurate,
and no "Abba Poemen"-class recurrence appeared in any form. It found ten
substantial and fifteen minor issues, all of one coherent shape: checkable
assertions about registered material that the registered material does
not actually carry, written into fields doing argumentative work. The
sharpest instances: alexandria-continuity's only concession claimed an
Origenist conceptual affinity for Evagrius that no record in this corpus
supports, propped up by a back-written note in evagrian-systematization
that misdescribed its own paragraph; strand-porousness cited the Vita for
a Kellia founding link the Vita never mentions, reaching past the correct
citation (the Apophthegmata) already one line below it; this index's own
roster justification claimed no individual source base existed for Amoun,
Macarius, and Pambo, false against four chapters of this corpus's own
vendored Palladius; and desert.figure.evagrius was built without opening
Palladius ch. XXXVIII, a dedicated eyewitness biography that independently
supplies its entire dates block. Two findings were of a different,
non-citation kind: a named, cleared step-2 instruction aimed specifically
at "the amma figure records at step 3" went unaddressed and unlogged by an
all-male roster; and the world_core wired one of its cautions to a
contested_claim record whose own most carefully argued paragraph
explicitly declines to cover that ground. All fixed: the false concession
rebuilt on this corpus's actual Origenist-adjacent thread (Rubenson's
reading of the Letters); the Kellia citation corrected to the Apophthegmata
with Doc_01's own "reportedly" hedge restored; the roster justification
corrected to the bar the three original figures actually clear (absolute
registered dates, not source-base poverty); desert.figure.evagrius rebuilt
against Palladius ch. XXXVIII with its verification_state upgraded to
verified-direct for the biographical claims; desert.figure.sarah built to
answer the gender-axis obligation with real content (a specific,
independently verified saying) rather than a logged deferral alone, with
Syncletica and Theodora's continued exclusion now explicitly reasoned; and
the world_core's caution-to-record mapping corrected to name only caution
(5), not (4), at strand-porousness. Fifteen minor and seven cosmetic
findings addressed throughout, including a controlled confidence-enum term
leaking into two compiled fields, an unhedged bridge_line on
desert.figure.pachomius (the angel-vision and house-count now carry the
same hedges the record's own dates block already used), an out-of-horizon
dating error on caution (6) that placed the 399-400 controversy itself
past this world's own closing edge when Doc_01 treats it as one of the
reasons that edge falls where it does, and two canon-cell reassignments
(antony-literacy to F2-E; alexandria-continuity to no cells at all,
matching alx.contested.desert-attribution's own convention) where the
original assignments reached for cells the fleet's own canon questions did
not support. All records and this index were revised in response; see each
record's own body note for its specific fix.
