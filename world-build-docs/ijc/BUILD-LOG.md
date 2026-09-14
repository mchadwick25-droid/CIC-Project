# Imperial and Juridical Christianity (`ijc`) — Record-Set Build Log

**Branch:** `world/ijc` → merged to `build/phase-1` (PR #14, 2026-08-22) → continued on `claude/ijc-world-build-b9p7hr`, restarted from post-merge `build/phase-1` · **Built:** 2026-08-21–22 · **Scope:** spec §4.3 steps 2–5 (source ecology → interpretive lexicon → ecology reconstruction → answer canon → representative identity confirmation, voice_craft, demonstration), plus the cross-thread glossary/story/quote retrofit (§11). **Compile (6), admission (7), open (8): intentionally NOT started** — that stage still waits on the M4 live-generation design, per the standing instruction.

**Settled ground built from (not reopened):** the per-world Step 0 confirmation (2026-07-19, Approved to proceed, Round 3) and Doc_01 (Approved to proceed, Round 2 cosmetic only) — identity ("office-holders, not congregants"), window 312–451, three strands, Homoian recentering, skew disclosure, Living Tradition PENDING.

**Content ground:** the reviewed legacy document suite (Doc_02–Doc_09 with their Review-Artifacts, all Approved to proceed under the prior framework) was used as the content input, with every claim re-anchored to the vendored public-domain corpus and every verbatim quote re-verified character-level against the vendored files. Divergences from the legacy suite are itemized in §3.

## 1. Final state

154 records in `records/ijc/`: 1 world_core · 23 source · 23 search_record · 12 term · 6 gravity · 10 force · 7 contested_claim · 12 figure · 22 quote · 9 story · 12 doctrinal_witness · 7 honest_limit · 1 voice_craft · 9 demonstration (this tally corrected here to match the loader's own count directly - it had drifted stale across the confirmation-review rounds' own additions before this pass). 142 answer-canon records plus the step-5 voice/demonstration set of 12, after the step-5 adversarial review's own fixes - see §§9-10. Registry entry in `records/worlds.yaml` updated to `state: building` with the representative identity confirmed (§9).

**M1 gate battery: 14/14 clean** (schema, referential, reciprocity, completion, narratability, glossary-retrofit-complete, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution) — re-verified against the full 154-record set, including the retrofit fields added in §11. **Canon coverage: all 28 cells — 21 substantive, 7 honest-limited** (C-P, F1-T, F2-P, F4-P, F5-I, F5-T, F6-E), each honest limit with in-voice statement, cause, and nearest material.

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

## 9. Representative identity confirmation and step 5 (voice_craft + demonstration), 2026-08-22

**Identity confirmation.** Marius, Apocrisiarius — Deacon of the Letters, checked against this build's
full content canon (142 answer-canon records, three independent Opus adversarial reviews plus two further
confirmation passes, 13/13 M1 gates green throughout) at spec §4.3's step-5a touchpoint. Confirmed to hold
without qualification: the apocrisiarius/legate-deacon persona fits this world's own correspondence-and-
petition-carrying content precisely (Julius's letter to the Eusebian party, Damasus's synodical
correspondence embedded in Theodoret, Leo's Tome and his Canon-28 rejection letters, the Chalcedon
legates' own recorded objection), and the identity's own charge to carry Rome's, Constantinople's, and
Milan's claims alike matches this build's three-strand finding exactly (Doc_01 §§ Strand A/B/C, carried
through every gravity, force, and contested_claim record built). Nothing found during this build argues
for reopening it. Not a fresh decision — carried forward as the standing pre-rebuild identity (name and
role label set by Mark 2026-07-20 and 2026-07-22, per `records/worlds.yaml`'s own prior note), the same
way `world/syr`'s own Mar Yausep confirmation is expected to carry that identity forward. Logged in full
at `records/ijc/voice_craft/ijc.voice.craft.md`'s trailing body and in `records/worlds.yaml`'s registry
comment.

**Step 5 build.** One `voice_craft` record (`ijc.voice.craft`) and eight `demonstration` records, drafted
on Sonnet against `alx.voice.craft`/`alx`'s six demonstration records and `reference/fleet-voice/EXEMPLAR-TRANSCRIPT.md`
(`world/alexandria`) as the worked model — `records/pahc/` and a `world/syr` branch, named in the
handoff as the intended models, do not exist anywhere in this repository under the current record
schema (only a legacy `cic-poc/` proof-of-concept structure predates this rebuild's schema); this was
disclosed at the time and the real, equivalent `alx` material substituted.

Strict we-voice throughout, with the one sanctioned self-naming exception ("I am a representative of
Church and Empire") used exactly once, in the one demonstration turn that is directly about the voice's
own nature (`ijc.demo.f6-p-someone-like-me`) — and deliberately not used in the other identity-collision-
tagged turn (`ijc.demo.f6-p-woman-authority`), matching the fleet precedent that the tag alone does not
license the exception. The three strands (Rome/Constantinople/Milan) are held as one unresolved "we" in
`ijc.demo.f6-i-never-settled`, never adjudicated. The Homoian establishment is spoken of from outside, as
this world's own excluded "different we," in `ijc.demo.f1-i-argued-about`. The office-holder record skew
is stated plainly, in the voice's own honesty, in `ijc.demo.f5-i-ordinary-day` (drawn from
`ijc.limit.f5-ordinary-day`, whose compiled `statement` field carried a stale "an empress and a regent"
reference — corrected in place to "two empresses" before the demonstration was drafted from it, since no
formal regency for Justina is attested anywhere else in this build). `ijc.demo.f6-p-hypocrisy` uses this
world's own sharpest hard-places instance (Callinicum) rather than a safer one, matching the
episcopal-independence gravity's own review-corrected, deliberately double-edged description.

The set does not include an F6-T identity-collision demonstration.
Spec §6 names three identity-collision questions across F6-P and F6-T
as required before any world opens; this build's own hell/damnation and
divorce content under F6-T was left a disclosed gap at §6 above (the
cell is already substantively covered for its other questions, so the
coverage gate is satisfied, but not with content that would ground a
non-judgment demonstration on those two specific questions) - building
one now would mean fresh invention under this pass's own no-invention
discipline, not a citation of already-verified ijc content. Deferred
rather than fabricated; a natural companion task to closing the F6-T
gap itself.

The eight demonstration records first drafted: `ijc.demo.c-i-who-was-jesus` (center),
`ijc.demo.f6-p-someone-like-me` and `ijc.demo.f6-p-woman-authority` (identity-collision),
`ijc.demo.f1-t-bread-and-cup` (translational), `ijc.demo.f6-i-never-settled` (contested/two-strands),
`ijc.demo.f5-i-ordinary-day` (honest-limit-in-voice), `ijc.demo.f1-i-argued-about` (Homoian-recentering),
`ijc.demo.f6-p-hypocrisy` (hard-places). All content is drawn from and cites already-verified ijc
records; none is fresh invention. (A ninth, the required lament turn, was added at the review in §10
below, after this draft pass surfaced its absence.)

**Gates:** 13/13 clean at this draft stage, against the 151-record set. This draft pass was followed
immediately by an isolated Opus adversarial review (§10 below), per this build's own standing discipline
of never treating a first Sonnet draft as final without one.

No fix in this section reopened Step 0, Doc_01, or the answer-canon's own settled ground.

## 10. Step-5 adversarial review (2026-08-22) and its fixes

An isolated Opus dispatch reviewed the nine step-5 records cold, the same discipline as §§6-8: every
file read in full, every `sources[]` target opened and re-derived against the vendored corpus, pronoun
discipline machine-scanned, and readability computed against the `alx` model. Persisted in full at
`Review-Artifacts/Review_Step5_Voice_Demonstration.md`. Verdict: **REVISION REQUIRED, 3 HIGH, 12 MEDIUM,
14 LOW** - the pronoun discipline itself was exact and the Homoian recentering was met well, but eight
demonstrations lost real qualifications in compression, and three stated something no record in this
build actually supports.

**The three HIGH findings, all fixed:** `ijc.demo.f6-p-hypocrisy` claimed Ambrose held a basilica against
imperial command "twice" - no record in this build says twice, and the one basilica standoff's own dating
is disclosed as an open divergence, not a second event; struck to "held a basilica." `ijc.demo.f6-i-never-
settled` enclosed the Chalcedon acclamation in quotation marks with three sentences silently elided,
including the anathema; replaced with the fuller acclamation and a marked ellipsis, drawn from the
already-verified `ijc.quote.peter-has-spoken`. `ijc.demo.f6-p-someone-like-me` said the world's one
congregational glimpse "reaches us inside a bishop's own letter about himself," erasing the record's only
independent witness (Augustine, a layman in the city that night); restated to name both channels honestly.

**MEDIUM fixes, the four that matter most:** the Justina/Pulcheria demonstration
(`ijc.demo.f6-p-woman-authority`) had dropped both of its source record's own hedges - "no formal regency
is attested" and the Ambrose/chronology attribution divergence, the latter carrying a mandatory
`divergence_note` two prior confirmation rounds paid to establish - both restored, with the note now set
on the demonstration itself; the same over-claim on Ep. XCV ("thanks her directly... for overruling") was
fixed in both the demonstration and its source record, `ijc.dw.f6-p-women-authority-cost`. The Callinicum
turn's flat "public penance" was restated to the harder, contemporary-attested fact
(`ijc.story.emperor-penance`'s own tier discipline quarantines the public scene at a lower confidence),
and its dropped "worse than heathen" clause restored. The Canon 28 turn's "in the canon's own words" was
restated as "its own reasoning" (the sentence is a paraphrase, not a quotation), Leo's build-coined
"apostle's grave" line was marked as this build's own gloss rather than left undifferentiated from his
verbatim sentence, and Constantinople's own positive case (from `ijc.contested.canon-28-meaning`'s own
`claim` and `concedes` fields) was added so the turn does not demonstrate only Rome's side of a contest it
says is unresolved. The center-cell turn (`ijc.demo.c-i-who-was-jesus`) had traced its most interpretive
content to `ijc.dw.c-i-jesus` without citing it, and had dropped that record's own tension that the
confessed center was contested inside the establishment itself for two imperial reigns - both fixed, so
the cell tested first at every admission does not sound like the winning side narrating a settled outcome
backward. The bread-and-cup turn had carried ~60 words of Ambrose's own translated sentences as
unattributed narration, breaking this world's own register discipline that a source is named; a new quote
record, `ijc.quote.ambrose-blessing-changes-nature`, was created so the turn could quote Ambrose properly
by name. Four over-ceiling turns (FK 11.9-14.0, against an FK 10 ceiling and a 4.9-8.0 `alx` baseline)
were brought back under the ceiling by splitting long sentences, content unchanged. `voice_craft.guard` had
substituted this world's own line for the fleet floor line rather than adding to it; restored to carry
both. The set had no lament exchange, though spec §4.3.5 requires one; a ninth demonstration,
`ijc.demo.c-p-want-to-believe`, was added, built from `ijc.limit.c-p-jesus-to-you` and a new quote record,
`ijc.quote.leo-sinner-be-glad`, in the witness-before-answer register the lament cell requires. The
missing F6-T identity-collision turn is disclosed above as a deliberate deferral (fresh content this pass
was not licensed to invent), not silently left off the record.

**LOW fixes:** two build-architecture phrases removed from `voice_craft.identity` (inherited verbatim
from `alx.voice.craft`, and self-contradicting the self-reference flavor note's own illustrative use of
"deacon"); the term-introduction flavor note's example gloss corrected to match `ijc.term.presbeia`'s own
plain meaning; a stale-by-one word ("names" undercounting the record by omitting Marcellina as an
addressee) fixed in both `ijc.limit.f5-ordinary-day` and its demonstration; the creed rendered as a marked
summary rather than an unmarked near-quotation, restoring "for us men"; Ambrose's reverential capitals and
two canon-question em dashes restored; "It was withdrawn" softened to the source's own "promised... to
withdraw it"; "most of a century" corrected to "half a century," matching `ijc.term.homoousios`'s own
arithmetic; "Constantius" given its numeral; "at once" dropped from the Chalcedon framing sentence,
matching the story record's own three-weeks-apart correction; and Percival's own limiting reading of the
legates' objection added to `ijc.contested.canon-28-meaning.held_against`, strengthening rather than
weakening the unresolved holding.

**Not changed:** the identity confirmation itself - the review found nothing that reopens it. The gate
battery's own coverage gap (readability and citation-traceability checks do not yet reach `demonstration`
or `voice_craft` fields) was flagged by the review as worth a future architecture pass; this pass fixed
the content it exposed rather than extending the gate battery, since a mechanical check was not the thing
in short supply here - a close human reading was.

**Gates:** 13/13 clean, re-verified against the full 154-record set (151 + 2 new quote records +
1 new demonstration). **Record count:** 142 → 154 (12 new: 1 voice_craft, 9 demonstration, 2 quote).

No fix in this section reopened Step 0, Doc_01, or the answer canon's settled ground.

## 11. Glossary/story/quote modern-vs-world contrast retrofit (2026-08-22)

Populated the five fields the cross-thread retrofit (`reference/Redesign-Spec/Glossary-Story-Quote-Template.md`,
switch flipped on `build/phase-1` after all seven worlds cleared their content canon) added to
`COMPLETION_REQUIRED`/`gate_glossary_retrofit_complete`: `term.distortion_risk` (12 records),
`story.modern_contrast` (9 records), `quote.modern_lens_note` (22 records), `gravity.classification`
(6 records), `force.matrix_cell` (10 records) — 59 records, matching the 59 `completion-per-type`
findings the retrofit's own switch flip produced against this world's set. `term.false_friend` and
`senses.translational` were already populated by convention on every term and needed no fixes.

This is compression of reasoning already on record, not new research:

- **`gravity.classification`** and **`force.matrix_cell`** are fully mechanical - both were already
  encoded as free text in every gravity/force record's own `name` bracket (e.g. `[PRIMARY]`,
  `[2B - ongoing/internal]`), a direct carry-forward of the reviewed Doc_04/Doc_08 classifications.
  Extracted and set as the new structured fields with no new judgment calls.
- **`term.distortion_risk`** (low/medium/high) was assigned per term by reading each term's own
  already-written `senses.translational` bridge sentence and `false_friend[]` list and judging how
  sharp the misreading risk actually is, calibrated relative to this world's own most consequential
  terms: `high` where a misreading would distort a central, live, or ethically fraught claim this
  world's own record makes (`ijc.term.concilium`, `ijc.term.haeresis`, `ijc.term.homoios`,
  `ijc.term.homoousios`, `ijc.term.imperator-intra-ecclesiam`, `ijc.term.primatus` - the authority
  contest, the Homoian-recentering obligation, and the primacy/church-state claims all sit here);
  `medium` for a real but more contained conceptual gap (`ijc.term.communio`, `ijc.term.nea-rhome`,
  `ijc.term.presbeia`); `low` where the modern reader's basic intuition is roughly right and only the
  vocabulary needs correcting (`ijc.term.basilica`, `ijc.term.martyrium`, `ijc.term.tomus`).
- **`story.modern_contrast`** was drafted per story from its own `narrative_tier_justification`,
  `absent_detail`, and gravity/force connections - e.g. `ijc.story.callinicum-synagogue`'s contrast
  names directly what its own trailing body already states (the same sacramental leverage that
  restrains a throne elsewhere here shields arsonists), and `ijc.story.vigil-in-basilica`'s corrects
  the likeliest modern mis-mapping (church-vs-secular-state) against what the record actually shows
  (an intra-Christian contest, the Homoian confession then being the empire's own). No story needed
  the explicit-none form - every one of this world's nine stories carries a real modern-misreading risk
  worth naming.
- **`quote.modern_lens_note`** stayed strictly to vocabulary/imagery legibility, per the retrofit's own
  discipline (never softening or editorializing a quote's content): archaic address forms ("your
  Clemency's rule," "Thy handmaid"), technical patristic vocabulary read in its modern sense ("nature,"
  "form," "Person"), an unnamed visual referent (the Chi-Rho monogram in `ijc.quote.lactantius-dream`),
  an unmarked scriptural allusion (`ijc.quote.leo-rome-apostles`), and words whose modern sense would
  actively mislead (`ijc.quote.sozomen-thessalonica-law`'s "Catholic Church" meaning "universal," not
  the later denominational sense). Two quotes (`ijc.quote.ambrose-cannot-surrender`,
  `ijc.quote.julius-custom`) carry no real vocabulary/imagery risk and use the explicit-none form.

**Not done, per the retrofit's own scope note:** compiler wiring (no lightweight glossary-style index
exists yet for a hover UI to query) and frontend implementation - both named follow-up engineering on
`build/phase-1`, not part of this thread's task.

**Gates:** 14/14 clean (13 plus the new `glossary-retrofit-complete`), re-verified against the full
154-record set. **Record count:** unchanged at 154 (five fields added across 59 existing records, no
new records).

No fix in this section reopened Step 0, Doc_01, the answer canon, or the step-5 voice build's settled
ground.
