# Imperial and Juridical Christianity (`ijc`) — Record-Set Build Log

**Branch:** `world/ijc` (base `build/phase-1`) · **Built:** 2026-08-21 · **Scope:** spec §4.3 steps 2–4 (source ecology → interpretive lexicon → ecology reconstruction → answer canon). **Voice build (step 5), compile (6), admission (7), open (8): intentionally NOT started**, per the standing instruction to stop before voice/demonstration while the live-generation citation design is unproven.

**Settled ground built from (not reopened):** the per-world Step 0 confirmation (2026-07-19, Approved to proceed, Round 3) and Doc_01 (Approved to proceed, Round 2 cosmetic only) — identity ("office-holders, not congregants"), window 312–451, three strands, Homoian recentering, skew disclosure, Living Tradition PENDING.

**Content ground:** the reviewed legacy document suite (Doc_02–Doc_09 with their Review-Artifacts, all Approved to proceed under the prior framework) was used as the content input, with every claim re-anchored to the vendored public-domain corpus and every verbatim quote re-verified character-level against the vendored files. Divergences from the legacy suite are itemized in §3.

## 1. Final state

125 records in `records/ijc/`: 1 world_core · 19 source · 16 search_record · 12 term · 6 gravity · 10 force · 7 contested_claim · 12 figure · 20 quote · 8 story · 7 doctrinal_witness · 7 honest_limit. Registry entry added to `records/worlds.yaml` (state: `building`).

**M1 gate battery: 13/13 clean** (schema, referential, reciprocity, completion, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution). **Canon coverage: all 28 cells — 21 substantive, 7 honest-limited** (C-P, F1-T, F2-P, F4-P, F5-I, F5-T, F6-E), each honest limit with in-voice statement, cause, and nearest material.

## 2. Stage discipline

Built one stage at a time with gates run and a self-review pass between stages, committed incrementally (corpus vendor → sources/searches → terms → gravities/forces/claims → figures → quotes/stories → witnesses/limits → consistency pass). This is a records build, not a Doc_XX drafting cycle: the independent-review function the legacy documents received is carried here by (a) the already-reviewed legacy suite as content ground, (b) the mechanical gate battery, and (c) the disclosed verification corrections below — an honest description, not a claim that fresh per-record adversarial review rounds were run. If the project lead wants a cold adversarial review of the record set before step 5, that is a natural next action and nothing here forecloses it.

## 3. Verification findings — corrections made during this build (each disclosed in the affected record)

1. **Legacy Doc_09 story 6 factual error corrected:** "the same council, in the same session" — the Tome's reception (Session II) and Canon 28's passage were days apart. Corrected in `ijc.story.tome-that-would-not-bend` with the separation stated in `absent_detail`.
2. **Egyptian bishops' plea mis-citation caught pre-commit:** first drafted against Percival's Chalcedon extracts; a direct read found the scene absent (it is in the complete acts only). Re-sourced to via-authority in `ijc.force.chalcedon-failed-consensus` with a verification note.
3. **"Countermanded too late" detail dropped:** the often-told countermand of the Thessalonica reprisal is not in the vendored accounts (checked Theodoret V.17, Sozomen VII.25); removed from `ijc.story.emperor-penance`, with the 7,000 figure carried only under Theodoret's own "it is said."
4. **Percival's singular "prerogative of honour"** (not "prerogatives") verified against Canon 3's text and normalized across records.
5. **Legacy Registry row 13's unverified Leo letter numbering (Ep. 104–106) verified** against the edition itself; row 21 (Rufinus HE) found unreproducible in public domain and honestly dropped (search_record); Sozomen VII.4 confirmed as the Thessalonica-law witness with the Damasus/Peter clause read directly.
6. **New source findings beyond the legacy suite:** Theodoret's embedded Damasus synodical letters (a securely-transmitted Damasus documentary voice distinct from the contested decretals); Hilary's De Synodis as vendorable access to the Homoian formulae (registry append, justified in `ijc.search.npnf209-hilary`); npnf210 lacks De obitu Theodosii (penance rests on Ep. 51 + flagged Theodoret).

## 4. Additions beyond the legacy inventory (registry-grounded, disclosed)

- `ijc.story.emperor-penance` (390) and `ijc.story.altar-of-victory` (384) — the latter closes legacy Open_Gaps item 6 (the un-registered Altar of Victory material; Symmachus's Memorial is in vendored npnf210).
- Tension-coverage: the Tensional gravity carries a real matrix-mapped `tension-with` pole (primacy-claiming — the Interaction Matrix's one "competing" cell); its Strand B status stays genuinely open per Doc_04 Open Item 2.
- `canon_cells` populated at authoring time on every gravity/force/contested_claim (the Alexandria retrofit discipline), with deliberately-empty cells reasoned in-body (boundary-condition forces; the bees legend; Nea Rhōmē).

## 5. Flagged for Mark (nothing here decided by this build)

1. **Representative identity under the new spec (step 5a touchpoint):** the registry carries Marius / "Deacon of the Letters" from Mark's own 2026-07-20/22 decisions (Open_Gaps items 13, 15) — carried as his standing decision, explicitly NOT re-confirmed under the new spec.
2. **Living Tradition Status: PENDING** (Doc_01 §1); registry `living_tradition_flag: true` meanwhile, failing toward doorway disclosure.
3. **Open source requests (P3, non-blocking):** Paulinus's Vita in the 1928 Kaniecka translation (would upgrade the bees story's verifiability); Ammianus (Yonge 1862) for the Damasus-election account. See SOURCE-REQUEST-MANIFEST §2.
4. **"Church and Empire"** is the census/card short name (Mark, 2026-07-20); the registry `census_id` maps to the Atlas entry `imperial-juridical-christianity`.

## 6. Adversarial review round (2026-08-21/22) and the fixes it produced

Per §5's own flagged next action, three isolated Opus adversarial reviews were dispatched against the
full 125-record set: quote/source verbatim fidelity, historical accuracy, and canon/structure
discipline. All three are persisted in full in `Review-Artifacts/` (this project's own discipline:
reviews exist as files, not summarized claims). All three returned **SUBSTANTIAL REVISION REQUIRED**.

**Findings and disposition:** 12 HIGH, 24 MEDIUM, and 26 LOW findings across the three reviews. All 12
HIGH and all 24 MEDIUM findings were fixed; the majority of LOW findings were also fixed opportunistically.
Two per-question content gaps flagged at MEDIUM (Genesis-as-science under F2-T; hell/damnation and
divorce under F6-T) were left as honest, disclosed gaps within already cell-covered material, rather than
adding invented content under time pressure - both cells already carry a substantive record answering
their other questions, satisfying the coverage gate.

**The most consequential fixes, by category:**
- **Factual corrections** (the project's own named failure mode - a real, sourced fact carried at the
  wrong scope): a quote conflating two different ancient translations of the Milvian Bridge agreement
  under the wrong attribution; a false three-Auxentii disambiguation collapsed to the correct two, with
  Ambrose's own naming argument as warrant; the Callinicum affair's actual content (a burned synagogue
  shielded from restitution, not a euphemism) restored to the record; three false "days apart"/"same
  week" claims about the Chalcedon Session II/Canon 28 interval corrected to the actual three weeks; an
  inverted clause about who reviewed whose judgment in the Julius/Alexandria dispute; a chapter-title
  misquoted as a historian's own sentence; a silently Latinized Greek letter (chi) restored to what the
  file actually prints; a misdated "mid-reign" baptism; an anachronistic retrojection of the "Homoian"
  label to pre-357 depositions; several more (full list in the review artifacts and the two MEDIUM-fix
  commits).
- **Three honest_limit records were substantively wrong**, not just imprecise: each claimed a topic
  (original sin, the eucharist, marriage, tithing) was simply absent from this world's own record, when
  the already-vendored corpus (Leo's letters and sermons; Ambrose's De Mysteriis and Concerning Widows)
  answers each directly. Root cause, per the reviews' own diagnosis: no cell-scoped negative search had
  ever been run before those honest_limit statements were drafted - only work/volume-level searches
  existed. Fixed by adding five new doctrinal_witness records, two new source records, two new
  cell-scoped negative search_records, and narrowing each honest_limit to what genuinely remains
  unanswered.
- **F6-P (a woman's authority and its cost)** was nominally covered by a story tagged onto the cell that
  answered none of its six questions - replaced with a genuine answer built from Justina's documented
  coercive regency (Ambrose Ep. XX) and Pulcheria's role as Leo's own direct addressee.
- **Fleet-architecture leakage** (naming "other Christian worlds," "worlds that kept them," internal
  record ids, and this build's own "Corrected at review" language) was found inside compiled/participant-
  facing fields beyond the one precedented location (`world_core.cautions`) - removed from
  `doctrinal_witness.text` and `honest_limit.statement` throughout.
- **Doc_04's own Interaction Matrix** had two relationships explicitly marked "reshaping" (after that
  document's own Round-1-forced correction) flattened to undifferentiated `associated-with` in the
  compiled relations, re-introducing the ambiguity the correction had removed - re-encoded as
  `tension-with`.
- All 11 doctrinal_witness records bumped from retrieval tier 2 to tier 1, matching their definitional
  role as this world's own core answer-ground for a cell (previously unexplained inconsistency with the
  `alx` exemplar's own all-tier-1 convention).

**Record count:** 125 → 137 (12 new records: 1 story, 5 doctrinal_witness, 4 source, 2 search_record).
**Gates:** 13/13 clean throughout, re-verified after every fix pass.

No fix in this round reopened Step 0 or Doc_01's settled ground. The build otherwise remains exactly
where §1 left it: stopped before step 5 (voice_craft/demonstration), pending Mark's disposition.

## 7. Confirmation review (2026-08-22) and its fixes

A fresh, isolated Opus review was dispatched specifically to verify §6's fix round from scratch -
re-deriving every claimed fix against the vendored corpus directly rather than trusting this log's own
account. Persisted at `Review-Artifacts/Review_Confirmation_Pass.md`. Verdict: **MOSTLY CONFIRMED** - all
12 original HIGH findings and 22 of 24 MEDIUM findings genuinely check out. It also found 1 new HIGH,
8 MEDIUM, and most of Review 1's LOW block (7 items) still unworked from the original fix round.

**The new HIGH** was introduced *by* the fix round: Leo's "Collections" sermons (giving-discipline
material added to correct Review 3's H2) had been tied to a fabricated "autumn fast." The vendored
file's own explanatory note identifies the occasion as the octave of SS. Peter and Paul (early July, a
collection day repurposed from a pagan festival), not a fast at all - Leo's genuine autumn-fast sermons
are a separate, unrelated set with no Collections content. Fixed in all four affected records.

**The 8 MEDIUM findings** were each a smaller instance of the same failure mode the whole review series
exists to catch, introduced during the fix round itself: a chapter title (Theodoret V.18 vs V.17) missed
in a fourth record after three others were caught; a bridge_line sourced to "the council's own synodal
letter" when the passage is actually Anatolius of Constantinople's own letter, printed in the acts'
editorial notes; an authorship note inventing specifics ("16th-century," "the Benedictine editors," "now
universally admitted") an edition's introduction does not state; a doctrinal_witness citing a letter at
`verified-direct` for a claim (Justina acting "in her own name") that letter's own text does not make -
the attribution rests on the volume's own chronology, now cited correctly, alongside a fixed internal
contradiction ("Justina's regency" surviving after the same record's own text correctly denied one); an
NPNF editor's chapter-argument summary ("Auxentius' cruel law") quoted as Ambrose's own sermon wording -
the identical defect caught and fixed elsewhere in the same round, reintroduced here, now replaced with
Ambrose's actual sentences; an undisclosed 385/386 dating divergence between this build's stated
chronology and its own cited edition's date, now disclosed per this world's own contested-dating
discipline; and Coustant's limiting reading of Julius's "custom" claim (scoping it to the Alexandria case
specifically), sitting in the build's own vendored apparatus but carried nowhere until now. A structural
finding (R3-H5's negative-search fix had only covered 2 of 7 honest-limited cells) was closed with five
new cell-scoped search_records (C-P, F2-P, F4-P, F5-I, F6-E).

**LOW fixes:** all 7 of Review 1's too-narrow quote loci (not one had been touched in the original fix
round - `nicene-creed`, `canon28-equal-privileges`, `constantine-bishop-outside`, `julius-custom`,
`leo-tome-each-form`, `lactantius-dream`, `vc-conquer-by-this`); two undisclosed terminal-punctuation
substitutions, now disclosed; one Greek gloss restored from Latin transliteration; a dropped-words/
wrong-gloss defect inside the Auxentius identification's own warrant quotation; an arithmetic error
(fifteen years, not sixteen, between Theodosius's baptism and death); a third-person "a modern asker"
addressed in compiled answer-ground, reworded to second person; three residuals in the hymn-singing fix
(Augustine's own "throughout the rest of the world" restored in place of a narrower "the West's," the
Hilary counter-datum properly sourced instead of left anonymous, and a self-contradictory tensions line
untangled); a paraphrase and a quotation both drifted from "we cannot attain to so great a secret by one
road" to "so great a mystery... by one road only," both corrected; a lumped-together "Homoian emperors"
generalization in `ijc.term.homoousios` narrowed to the actual 357-onward window; and lowercase/
repunctuation drift inside a quoted Leo sentence. One LOW finding (the registry `role_label` dropping
"Apocrisiarius") was left as-is, per the review's own assessment that it is a defensible deferral to
Mark's step-5a touchpoint, not an error.

**Record count:** 137 → 142 (5 new cell-scoped search_records). **Gates:** 13/13 clean, re-verified.

No fix in this round reopened Step 0 or Doc_01's settled ground.

## 8. Second confirmation review (2026-08-22) and its fixes

A second isolated Opus review verified §7's fix round the same way the first verified §6 - re-deriving
every claim against the vendored corpus directly. Persisted at
`Review-Artifacts/Review_Confirmation_Pass_2.md`. Verdict: **MOSTLY CONFIRMED, the pattern repeated a
third time** - the round's hardest fixes (the autumn-fast removal, the Anatolius/De Mysteriis/Ambrose-
wording/Justina/Ep. CV/385-386/Coustant corrections) all re-derived clean, but the round again introduced
a small number of new, smaller errors of the same kind - this time concentrated in two mechanisms: (a)
adopting a prior review's own asserted line numbers without re-opening the file, and (b) an edition's
editorial apparatus stated as the primary author's own words in a compiled field.

**The new HIGH:** the Hilary of Poitiers "counter-datum" added to close a prior LOW finding was wrong
about the vendored volume (it named "the same manuscript as De Synodis" - the hymn fragments actually
share a manuscript with Hilary's own *De Mysteriis*, a different work) and, worse, was refuted by the
next several sentences of the very passage it cited - the volume's own introduction credits Hilary with
*writing* Latin hymns but explicitly denies he ever succeeded in bringing them into public worship,
crediting that to Ambrose. Reworked in `ijc.dw.f4-e-ancient-custom` to what the source actually
supports - a datum that sharpens Augustine's claim about Milan 386 rather than contradicting it.

**Mechanical finding:** three of the seven quote-locus "fixes" from the first confirmation round had
adopted that review's own asserted line ranges without checking them, and two of those ranges were
themselves wrong - producing loci that pointed at text outside the quote (`constantine-bishop-outside`,
`julius-custom`, `leo-tome-each-form`), a regression on the pre-fix state. All three re-derived directly
from the file and corrected, along with two more one-line-off ranges (`canon28-equal-privileges`,
`vc-conquer-by-this`) and one cosmetic range/single-line mismatch (`lactantius-dream`).

**Other MEDIUM fixes:** `ijc.story.vigil-in-basilica.text` still carried "the West's congregations" after
the phrase was fixed only in the doctrinal_witness record that shared it - both now match Augustine's own
"throughout the rest of the world"; the Collections-day octave dating was hedged to what Leo's own words
actually say ("the day of Apostolic institution") versus the edition's own dated reconstruction; two of
the five new negative-search records (F6-E, F5-I) were found to assert false or incomplete claims about
the corpus and were corrected with real content restored (Lactantius's *De Mortibus* does reach pre-312
and does contain torture-of-slaves testimony, licensed but deliberately not drawn on; Leo's Ep. IV.II and
Sermon XLII.VI on the treatment of enslaved persons, previously left to an editorial footnote, are now
recorded as primary sources); all five new sweeps gained their actual literal search strings; the
women's-authority witness (`ijc.dw.f6-p-women-authority-cost`) had its `positions` field left out of sync
with a `text` field the same round had corrected, plus a citation to Sozomen that was never actually
added to `sources[]` - both fixed, a `divergence_note` added, and Leo Ep. XCV added as the real warrant
for Pulcheria's convening role (asserted previously with no citation at all); and three more places still
carried the Theodoret V.17-18 citation error after three others had already been fixed in an earlier
round.

**LOW fixes:** two sentence-case/quotation drifts restored (a congregation's own words inside Ambrose's
sermon wrongly presented as entirely his; the Ambrose figure's key identification quotation); an
oversized editorial gloss moved outside its quotation marks; a vestigial "Thy" left without its vocative
context after a partial restoration; a stale instance-count in a record body; a paraphrase's remaining
intensifier drift ("by one road alone" vs. the source's plain "by one road"); a term's personal-sense
field that had swapped one unsourced claim for another equally unsourced one, now saying only what the
record supports; a search record's overstated claim about the corpus's registers (Symmachus, Lactantius,
Jerome, and Ammianus are none of them a bishop, emperor, or court historian); a second documented
forgiveness case (Callinicum) missing from a sweep that claimed only one existed; and a locus pointing
seven lines past its own cited document's actual heading.

**Record count:** unchanged at 142 (no new records this round, only corrections). **Gates:** 13/13 clean,
re-verified.

**A standing note carried forward from the review itself:** three fix rounds in a row have each closed
findings and introduced a smaller set of the same kind, most consequentially by trusting an asserted
line number instead of reopening the file, or a stated fact instead of reading past the sentence that
states it. Every quote locus in this record set has now been independently re-derived at least once
directly against the vendored file rather than inherited from a prior pass.

No fix in this round reopened Step 0 or Doc_01's settled ground.
