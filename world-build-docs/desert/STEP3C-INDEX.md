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

**Roster discipline, TWO separate criteria (revised, Step3c Round 1 Finding S3, corrected again at Round 2 Findings S3/S4/M11):** this roster is not built on one bar; it is built on two, kept explicitly distinct after Round 2 found the single-bar account this index gave at Round 1 was self-contradicting.

- **Criterion A, for Antony/Pachomius/Evagrius: an absolute personal birth and/or death *year*, stated in a registered source record or fixed by a named external chronology combined with an age given in a vendored primary source, with any derivation marked openly** (not merely an age or interval left undated, and not a settlement's own founding date). Pachomius: `desert.source.pachomian-corpus.md` states "c. 292-346" directly. Evagrius: `desert.source.evagrius-praktikos.md` states "c. 345-399 CE" directly (consult-only channel) — the vendored Palladius ch. XXXVIII independently confirms the *intervals* around that anchor (age fifty-four at death, two years at Nitria then fourteen at Kellia) but carries no calendar year of its own; `desert.figure.evagrius`'s own `divergence_note` says so explicitly. Antony: **not** the NPNF editors' endnote at *De viris illustribus* ch. 88 ("Born 251, died 356") - that note is the edition's own apparatus, not Jerome's text, exactly the kind of note `desert.source.jerome-de-viris` already flags elsewhere in the same volume as "the edition's note, not ancient testimony" - but the *Vita*'s own §89 (vendored), which has Antony say he is "near a hundred and five years old" shortly before his death, combined with the death year 356 fixed by external chronology (Doc_01 §2.1) and marked as derived in `desert.figure.antony.dates.born` itself. Amoun, Macarius, and Pambo do not clear Criterion A: Doc_01 §2.2 gives Nitria, Scetis, and Kellia absolute *founding* years and names Amoun and Macarius as founders, but that is the settlement's date, not the person's own birth or death year; `desert.source.palladius-lausiac-history` gives all three a real, individually traceable career (ch. VIII: Amoun's marriage, eighteen years, then two cells at Nitria, then twenty-two more years, then death; ch. XVII: Macarius of Egypt retired to the desert at thirty, received grace at forty, ninety years total; ch. X: Pambo quoted at least seven times, age seventy at death) but never an age-plus-external-chronology anchor or a directly registered year, for any of the three men themselves.
- **Criterion B, for Sarah: a specific, individually verified saying or encounter, independent of absolute dates.** `desert.figure.sarah` has no `dates` field at all (schema-optional, correctly omitted) and does not clear Criterion A. It answers a different, explicitly named obligation instead (below). Honestly stated: **Pambo clears a saying-based criterion more strongly than Sarah does** — Palladius ch. X quotes him at least four times in a vendored, `verified-direct`, `load-bearing` source, where Sarah's one saying is paraphrase-only with no vendored edition at `verified-via-authority`. Sarah is built anyway, because Criterion B exists to answer a specific instruction Criterion A cannot (see below), not because her saying is this corpus's strongest.

Nepheros remains barred outright by `desert.source.nepheros-archive`'s own standing caution (Step2 Review Round 1, Finding 5 — the archive-to-edition mapping must be re-checked against the editions themselves "before any figure or quote record leans on either monk by name").

**The gender axis (Step3c Round 1 Finding S4):** `desert.source.apophthegmata-patrum`'s own cleared body names an obligation aimed specifically at "the amma figure records at step 3," tied to Doc_02 §6's Affirmative Duty gender axis. An earlier draft of this step built three male figure records under Criterion A and passed over that obligation in silence. `desert.figure.sarah` now answers it under Criterion B: among the three named ammas (Syncletica, Theodora, Sarah), Sarah is the one this corpus can trace to a specific, independently verified saying (the prior build's cleared Doc_09a Story 2.3, itself web-verified) rather than to bare naming alone. Syncletica and Theodora remain unbuilt as figure records — both are genuinely named and attested, but this corpus currently holds only bare naming for either, not a specific saying or encounter, and a figure record built on bare naming risks inventing the concreteness a `bridge_line` needs. This is a deliberate, logged decision (see `desert.figure.sarah`'s own body), not a second silent omission.

## Contested claims

| id | claim (one line) | poles | canon_cells | classification confidence |
|---|---|---|---|---|
| `desert.contested.antony-literacy` | Was Antony really the unlettered rustic Athanasius portrays? | Athanasius's Vita vs. Rubenson's Letters-based reading (Gould's counter-position against Rubenson specifically) | F2-E | Contested |
| `desert.contested.strand-porousness` | Were the three organizational patterns lived boundaries, or a later compiler's arrangement? | the Kellia founding link and the sayings tradition's own cross-pattern compilation vs. each pattern's own distinct authority/formation logic; the Nepheros community as evidence the typology may be incomplete | (none) | Contested |
| `desert.contested.alexandria-continuity` | Does desert monastic formation belong to Alexandria's ecology as its intensified continuation? | the Alexandria build's own claim (`alx.contested.desert-attribution`) vs. this world's own distinct-world evidence | (none) | Contested |

None of the three resolves its own question — each states the claim, the strongest case against it this corpus's own registered evidence supports, and what can honestly be conceded, per this step's own governing instruction (Framework Step 6 / Constitution Article 22's contested-claim discipline, matching Alexandria's `alx.contested.*` convention).

**Canon-cells basis** (added, Round 1 Finding M7; corrected again at Round 2 Finding M4 to name a basis for every row, not only the three contested_claim rows, and to fix the one wrong justification):

| record | cell | basis |
|---|---|---|
| `desert.figure.antony` | F4-I, F4-P | F4-I: "How did a person actually become one of you?" — his own staged withdrawal is this world's paradigm formation account. F4-P: "Does your way of life have anything for someone like me?" — his own spiritual-combat career speaks directly to it. |
| `desert.figure.pachomius` | F3-I, F4-I | F3-I: "Who held authority among you, and how did anyone come to have it?" — he founded the one pattern with an office. F4-I: as Antony, for the cenobitic pattern's own becoming-a-member process. |
| `desert.figure.evagrius` | F4-P, F6-I | F4-P: his own systematized combat-scheme. F6-I: "Was there anything about your own community that troubled you?" — his own record states, in terms, that within this world's own horizon his standing was "inheritance-and-unease, not condemnation" (the internal, in-horizon thinness and contest over his systematized register, per Doc_05 §8.5 item 3/Doc_07 §11) - **not** the later, out-of-horizon controversy and condemnation, which the same record explicitly declines to let decide anything. |
| `desert.figure.sarah` | F6-P | "You've told me what women's days were like — but could a woman carry real authority among you, and what did it cost her?" — a direct fit for the one case this corpus can show, not only assert. |
| `desert.contested.antony-literacy` | F2-E | "Isn't most of what's said about you legend, collected centuries later?" / "Where is your own record thinnest?" — a direct fit, already shared with `desert.term.apophthegma`; moved here from an earlier, unsupported F3-E assignment (F3-E is the catacombs/Constantine cell). |
| `desert.contested.strand-porousness` | (none) | Round 1 assigned F3-T; Round 2 found its justification circular (F3-T's two canon questions are both about ecclesial/denominational identity - "Was your church 'Catholic'?", "Did you have denominations..." - and this record's own body explicitly declines to cover that axis); Round 3 found the Round 2 rewrite still resting on the same axis under a different name. No fleet canon question actually asks about organizational-pattern porousness independent of ecclesial identity - moved to no cells, matching `alexandria-continuity`'s own convention, rather than force a third rewrite of a fit that has not held across three rounds. |
| `desert.contested.alexandria-continuity` | (none) | Nothing in the fleet's canon questions asks about cross-world scholarly attribution; moved here from an earlier, unsupported F3-T assignment, matching `alx.contested.desert-attribution`'s own `canon_cells: []` — a build-internal boundary question, not one a participant would put to a Representative. |
| `desert.core.desert` | (none) | Matching `alx.core.alexandria`'s own convention. |

**Gravity-risk statement, corrected (Round 1 Finding M6; corrected again at Round 2 Finding M2, and again at Round 3 Finding M3, each round finding the prior correction's own trailing clause overreached):** an earlier draft claimed "each contested_claim record states explicitly which gravities are and are not put at risk by leaving its question open" as a universal. Checked against all three: `antony-literacy.concedes` does this precisely, for the two gravities (withdrawal, elder-authority) Doc_04 SS3 routes its own contest to. `strand-porousness.concedes` states the three-pattern finding is held as settled structure, not a gravity-classification statement, and makes no statement about the other eight gravities. `alexandria-continuity.concedes` speaks to the systematized register's own scope, not to any gravity's classification, and likewise makes no broader statement. What is true, stated without a universal of any kind this round: no candidate gravity anywhere in this corpus has its own classification made to depend on resolving any of the three open questions - a claim checked directly against every gravity record's own text, not inferred from what any one contested_claim record's body happens to say about itself.

## World core

`desert.core.desert` (time window 320–430) synthesizes the horizon, formation logic, thinness, and cautions established across every prior step. Of its seven numbered cautions, **three** have a full contested_claim treatment: (3) at `antony-literacy`, (5) at `strand-porousness`, (7) at `alexandria-continuity`, wired via `relations[]`. **Caution (4)** (the Melitian ecclesial-boundary question) does **not** have one — an earlier draft of this world_core wired it to `strand-porousness` alongside caution (5), contradicting that record's own explicit disclaimer of the ecclesial-identity axis (Round 1 review Finding S6, now corrected in both records). Caution (4) remains a genuinely open item carried at its source, `desert.source.nepheros-archive`'s own standing caution, and at Doc_01 §11 item 1 / Doc_05 §4 — not an oversight, and not folded into a record that says it does not cover that ground. Cautions (1), (2), and (6) are single-voice concentration, compiler mediation, and the out-of-horizon trap — standing per-source disciplines rather than open contested questions requiring their own record.

**Thin topics** (structured index over the same ground `thinness`/`cautions` state in prose):

| keywords | note |
|---|---|
| liturgy, worship, psalter, prayer, synaxis | liturgical content beyond the Psalter and the Lord's Prayer is Inferential/Thin |
| woman, women, amma, female | named women and their sayings survive; no extended first-person narrative centered on a named woman, comparable to the founding narratives centered on men, survives |
| melitian, schism, nepheros | documentary business survives; no first-person Melitian voice does |
| wilderness, exile, typology, elijah, israel | a plausible, not yet textually confirmed, scholarly connection |
| authority, rule, elder, office, tension | well-evidenced structurally, not dramatized in any single scene |

**Absent stories** (carried forward from the prior build's cleared Doc_09a §5, restated in the world_core record's own body since this build's own Step 4 story repository has not yet been built): no named woman's own *extended* narrative (Sarah's single saying does not close this absence — it is one attributed reply, not a narrative on the scale of the founding accounts); no Melitian ascetic's own first-person account; no single scene dramatizing the authority tension directly. All three are structural absences (who could write, what got kept), not gaps to be filled by invention.

## Cross-build: Alexandria

`desert.contested.alexandria-continuity` is the Desert-side counterpart to the Alexandria build's own `alx.contested.desert-attribution` (`records/alx/contested_claim/`, `origin/world/alexandria`), which explicitly holds its question open "resolvable only there [in the Desert build] — by discovery, not by this world's assertion." This step supplies that discovery pass, built entirely from this corpus's own registered sources — Alexandria's own internal evidence is neither cited nor independently verified here. GRAVITY-INDEX.md's own cross-build sheet (Step 3b) had flagged Alexandria's material as comparative reference only, with no action item, because no open question had yet been raised from Alexandria's own side requiring a Desert-side answer; this record is that answer, generated once `alx.contested.desert-attribution`'s own text was read. No relation crosses the world boundary (a cross-world `relations[]` or `sources[].source_id` target would fail this corpus's own `gate_referential` when run against Desert's records alone) — the connection is carried in prose and by matching record ids only.

**Corrected, Round 1 Finding S1 (front matter) and Round 2 Finding S2 (body, since Round 1's own fix left the body untouched and self-contradicting):** an earlier draft's only concession claimed Evagrius's own systematized writing carried "genuinely Origenist-adjacent conceptual vocabulary" as evidence of Alexandrian conceptual affinity — checked against `desert.gravity.evagrian-systematization`'s own transmission-history note (which names only a *reception* history, the later controversy and condemnation, and explicitly declines to let it decide anything) and against `desert.source.evagrius-praktikos` (whose `author` field states Evagrius was "formed under the Cappadocians" as a biographical fact and whose `work` field describes his scheme, but which nowhere attributes the scheme *to* that training - the causal attribution belongs to Doc_07 §2, and the Cappadocian naming to Doc_01 §4/§2.3; no single record makes the compound claim an earlier draft of this sentence attributed to one). No record in this corpus supports the original claim. The concession is rebuilt on this corpus's actual Origenist-adjacent thread: Rubenson's contested reading of the *Letters* attributed to Antony as "substantively Origenist," already the full subject of `desert.contested.antony-literacy` — the two records are now cross-related. Round 1's own fix rewrote the front matter correctly but left the record's body still crediting its position to "gravity 9's own strand-bound Origenist-adjacent concession," which Round 2 caught and which is now also corrected. **Also corrected, Finding S5:** `held_against[3]` claimed the person-vs-office authority tension (gravity 10) "already accounts for" the Theophilus/Origenist-controversy contact with Alexandria's episcopal authority; that gravity's own description states its Interaction is "by construction... with those two [other] gravities specifically" and excludes external contact by definition. Reworded to state plainly that this contact remains an unresolved feature of the world's own boundary, per Doc_01 §5(b). **Also corrected, Finding M13 (genuinely this time — Round 1's own claim to have removed this sentence was itself false, per Round 2 Finding M1):** the body's claim that Doc_01 makes no comparison to Alexandria "on this record's own initiative" was false — Doc_01 §4, Doc_05 §8.2, and Doc_09b §3 all make the comparison directly; the sentence claiming a blank page is now actually removed, from the body directly rather than only from this index's own account of the record.

## Canon cells

| record | canon_cells |
|---|---|
| `desert.figure.antony` | F4-I, F4-P |
| `desert.figure.pachomius` | F3-I, F4-I |
| `desert.figure.evagrius` | F4-P, F6-I |
| `desert.figure.sarah` | F6-P |
| `desert.contested.antony-literacy` | F2-E |
| `desert.contested.strand-porousness` | (none — see Canon-cells basis above) |
| `desert.contested.alexandria-continuity` | (none — matching `alx.contested.desert-attribution`'s own convention) |
| `desert.core.desert` | (none — matching Alexandria's own `alx.core.alexandria` convention) |

`figure`, `contested_claim`, and `world_core` are not in `engine/m1/canon.py`'s `substantive_types()` (`{"doctrinal_witness", "term", "story", "quote"}`), so none of the cells above are gate-visible for canon-coverage purposes — matching the precedent already established for `gravity`/`force` at Step 3b. Populated as authored, per this build's own CANON_CELLS discipline, not retrofitted.

## Reciprocity and referential integrity

Every relation this step added is reciprocated, re-derived mechanically from the record files rather than read off this list: **38** directed relation ends corpus-wide involving a Step 3c record, over **19** distinct pairs, all `associated-with` and correctly symmetric, zero dangling. The pairs: `desert.contested.antony-literacy` ↔ `desert.gravity.withdrawal`, `desert.gravity.elder-authority`, `desert.term.apatheia`, `desert.figure.antony`, `desert.core.desert`, `desert.contested.alexandria-continuity`; `desert.contested.strand-porousness` ↔ `desert.gravity.economic-embeddedness`, `desert.gravity.manual-labor`, `desert.gravity.withdrawal`, `desert.core.desert`; `desert.contested.alexandria-continuity` ↔ `desert.gravity.scriptural-engagement`, `desert.core.desert` (plus `antony-literacy` above); `desert.figure.antony` ↔ `desert.gravity.spiritual-combat`, `desert.gravity.withdrawal` (plus `antony-literacy` above); `desert.figure.pachomius` ↔ `desert.gravity.koinonia`, `desert.gravity.authority-tension`; `desert.figure.evagrius` ↔ `desert.gravity.evagrian-systematization`; `desert.figure.sarah` ↔ `desert.term.geron-abba-amma`, `desert.gravity.elder-authority`. `desert.gravity.authority-tension`'s own relation to `desert.figure.pachomius` is `associated-with`, not `tension-with` — that record's own description states its Interaction is "by construction... with those two gravities specifically" (elder-authority and koinonia), and this step does not introduce a third, figure-level tension Doc_04 never tested (re-confirmed correct on independent review). Full gate battery re-run after every edit in this step: 70 records, 0 non-coverage findings. **Addendum, Doc_08 (added after Step 3c was approved to proceed, per Doc08 Round 1 review Finding S5):** Doc_08 has since added five new pairs involving a Step 3c record (`figure.pachomius`↔`formation-at-scale`, `figure.evagrius`↔`evagrian-intensification`, `figure.sarah`↔`oral-to-written-shift`, `contested.strand-porousness`↔`melitian-rivalry`, `contested.alexandria-continuity`↔`origenist-controversy`), none of them in the enumeration above - the corrected corpus-wide count is **48** directed ends over **24** distinct pairs. The sentence above describes this step's own state as of its own close and is no longer current; see `DOC08-INDEX.md`'s own reciprocity section for the up-to-date count, independently re-derived there rather than copied here. Not corrected in place, to preserve this document's own historical record of what step 3c actually verified at the time.

**Addendum, Step 4 (added after Doc_08 was approved to proceed, per Step4 Round 2 review Finding S6):** Step 4 has since added ten further new pairs, all connecting `desert.figure.antony`, `desert.figure.pachomius`, or `desert.figure.sarah` to one of this step's own story or quote records (`figure.antony`↔`quote.antony-arians-serpents`, `figure.antony`↔`quote.antony-dying-daily`, `figure.antony`↔`quote.antony-nicene-formula`, `figure.antony`↔`quote.antony-not-worsted`, `figure.antony`↔`story.antony-call`, `figure.antony`↔`story.antony-tomb-combat`, `figure.antony`↔`story.antony-withdrawal`, `figure.pachomius`↔`quote.pachomius-angel-tablet`, `figure.pachomius`↔`story.pachomius-founding`, `figure.sarah`↔`story.sarah-answer`) - the corrected corpus-wide count involving a Step 3c record is **68** directed ends over **34** distinct pairs, re-derived directly from the record files rather than copied forward. The sentence above (and the Doc_08 addendum immediately preceding it) each describe this step's own state as of its own close and are no longer current. Not corrected in place, to preserve this document's own historical record of what each prior step actually verified at the time.

## Open items carried forward

1. None of the three contested_claim records resolves its own question — that is by design, not an incompleteness of this step. A future step or audit revisiting any of the three with new evidence would not contradict this step's own work, only extend it.
2. Amoun, Macarius, and Pambo each have an individually traceable career in this corpus's own vendored Palladius chapters, and Doc_01 §2.2 gives absolute *founding* years for the settlements two of them are named with - but no absolute *personal* birth/death years anywhere in this corpus, Criterion A above. Revisit if a later step's own needs (Doc_08 forces, Step 4 stories) surface dated material for any of them, or if the roster bar itself should be loosened. Note that Pambo already clears a saying-based bar (Criterion B) more strongly than Sarah does, on source strength alone - he is not built as a figure record because no instruction comparable to the gender-axis obligation currently names him, not because his material is weaker.
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

Step3c Review Round 3 (`world-build-docs/desert/reviews/Step3c_Review_Round3.md`)
found the fabrication check clean a third time, independently re-derived
from scratch across all eight records including every clause the Round 2
fix pass had newly written, and found reciprocity (38 ends, 19 pairs),
the census, all five tables, and the gate battery all clean and
independently re-confirmed. All four of Round 2's substantial findings
were found genuinely and completely closed. But it found the build's own
recurring pattern - a fix that closes its target while introducing a new
defect of the same shape - recurring a third time, this round entirely in
the deliverable's own apparatus (its indexes and correction notes) rather
than in what the records assert about the world: a wrong relation count
(six gravity records and one term, copied from Round 2's own finding text
without re-derivation, where the correct figures are nine and two) written
into the otherwise-frozen GRAVITY-INDEX.md's own new addendum; a false
claim about desert.source.evagrius-praktikos (that it attributes
Evagrius's scheme to Cappadocian training) corrected on
evagrian-systematization but left standing in this index's own account of
that same fix, three screens away; Criterion A's own Antony anchor citing
an NPNF editorial endnote as if it were Jerome's own text, when this
corpus's own desert.source.jerome-de-viris record already flags the
identical kind of note in the identical volume as "the edition's note,
not ancient testimony"; and desert.figure.evagrius's Round 1 body note,
never revisited by either subsequent round's own front-matter fixes,
still stating a superseded quotation count and a claim (that Palladius
ch. XXXVIII "independently supplies every element of this record's own
dates block") the Round 2 fix exists specifically to deny. All four
fixed: GRAVITY-INDEX.md's addendum corrected to the true count, with the
records it lists named explicitly; this index's own Cross-build section
corrected to state the same accurate, split attribution
evagrian-systematization now carries; Criterion A rewritten to anchor
Antony on the Vita's own age-at-death plus external chronology, matching
his own figure record's marked derivation, rather than an editorial
endnote; and desert.figure.evagrius's stale body note rewritten with an
exact, re-verified quotation count (seven) and the "every element" claim
removed. Nine minor and seven cosmetic findings addressed throughout,
including a third-round overreach in the gravity-risk statement's
trailing clause; a canon-cell justification (F3-T for strand-porousness)
that had been rewritten twice and still rested on the ecclesial-identity
axis its own record disclaims, closed by moving the cell to empty rather
than attempting a third rewrite; a freshly written F6-I justification for
Evagrius that cited the very out-of-horizon material the record excludes;
a fresh positional self-reference in a compiled field cleaned of one in
the same commit; and a misdescription, in this index's own Round 2
narration, of what the pre-fix index had actually said. All records and
this index were revised again in response; see each record's own body
note for its Round 3 fix.

Step3c Review Round 2 (`world-build-docs/desert/reviews/Step3c_Review_Round2.md`)
found the fabrication check clean a second time, independently re-derived
from scratch across all eight records including the brand-new
desert.figure.sarah, and found reciprocity, the census, all four tables,
and the gate battery all clean and independently re-confirmed. It found
four substantial and fourteen minor issues, and named its own governing
pattern precisely: this build's recurring "illusory fix" failure mode
recurred *inside* Round 1's own fix pass, on the finding that named it.
The fix note written into desert.gravity.evagrian-systematization to
correct Round 1's S1 contained a fresh false claim about the very
paragraph it was correcting (asserting the paragraph attributed
Evagrius's scheme to Cappadocian training, when the paragraph makes no
such attribution at all) - fixed by removing the claim and naming the
attribution's real location (Doc_07 SS2; the evagrius-praktikos source
record) instead. More seriously: desert.contested.alexandria-continuity's
front matter was rebuilt correctly at Round 1 but its body was never
opened, so it kept crediting its position to "gravity 9's own
strand-bound Origenist-adjacent concession" - the exact claim Round 1
found false - and kept the false-novelty sentence this index had already
certified as removed. Fixed by rewriting the body to match what the
front matter actually now says. And the revised roster justification
(Round 1's own fix for S3) was itself internally contradictory: it stated
a single "absolute birth/death years" bar in one paragraph (correctly
scoped to "the three built figures," excluding Sarah) while a second
paragraph, open item 2, generalized that same bar to "the bar the four
built figure records each clear" - silently sweeping Sarah, who carries
no dates at all, into a criterion the first paragraph had correctly
excluded her from. Fixed by stating two explicit, separately-justified
criteria
(Criterion A: absolute personal birth/death years, for Antony/Pachomius/
Evagrius; Criterion B: a specific, individually verified saying,
answering the gender-axis obligation, for Sarah) rather than one
overextended bar, with the honest acknowledgment that Pambo clears a
saying-based bar more strongly than Sarah does and is not built because
no comparable instruction currently names him. Fourteen minor and seven
cosmetic findings addressed throughout, including: a second false
universal introduced by the very sentence written to remove Round 1's
first one (the gravity-risk statement, and separately the merged-relation
-pairs sentence in desert.figure.antony); a fresh jargon leak into
desert.core.desert.thinness (an internal caution-number pointer, written
by the fix pass into the one field Round 1 had singled out as the
cleanest against exactly that pattern); an index certification of a fix
("the sentence claiming a blank page is removed") that had not actually
been made; a canon-cell basis citing the axis its own record explicitly
declines to cover; and two overclaims about what Palladius ch. XXXVIII
actually supplies (a calendar year, which it does not carry, and an
ordination location it does not state). All records and this index were
revised again in response; see each record's own body note for its
Round 2 fix.
