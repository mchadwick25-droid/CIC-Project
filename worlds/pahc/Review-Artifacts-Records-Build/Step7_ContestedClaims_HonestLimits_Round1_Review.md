# Step 7 Cold Review, Round 1 — Contested Claims + Honest Limits (pahc)

**Scope reviewed:** `records/pahc/contested_claim/*.md` (9), `records/pahc/honest_limit/pahc.limit.f5-e-material-remains.md` (1), `worlds/pahc/build/CONTESTED-CLAIMS-INDEX.md`, `worlds/pahc/build/generate_contested_index.py`. Commit under review: `cecd75e2`.

**Reviewer stance:** cold — no visibility into the drafting conversation. Every finding below was confirmed against a file in this repository (source record, world_core, gravity/force record, generated index, Doc_01/Doc_02, or a live run of the gate battery). Nothing below is inferred from outside knowledge of the underlying historical scholarship, per the brief's instruction.

---

## Verdict: SUBSTANTIAL REVISION REQUIRED — narrow in scope

The mechanical layer of this batch is clean and the disclosure instinct behind it is right. All 13 gates run green on `load_world_records("pahc")` + `load_fleet_records()` except `canon-coverage`, which reports the 17 pre-existing blank cells this step deliberately did not close; `pahc.limit.f5-e-material-remains.statement` scores **FK 5.6**, comfortably under the ceiling of 10; the statement carries no build-attribution leak and holds first-person voice throughout; the generator's output is **byte-identical** to the committed index; every one of the five claimed `canon_cells` (F1-I, F2-E, F3-I, F3-T, F5-E) is a genuine close match to real fleet canon-question text, not a stretch; and a spot-check of five of the seventeen still-blank cells (C-P, F1-P, F2-T, F5-T, F6-T) found each of them plausibly answerable from already-built pahc material, so the decision to build exactly one honest_limit is sound and no second structural gap was missed.

But four records carry defects at the level of the record type's own purpose, not at the level of wording. `pahc.contested.hermas-dating` has **no genuine counter-position at all** — both `held_against` items either restate its own claim or attack a position it does not hold. `pahc.contested.egypt-exclusion` asserts a single-source dependency in stronger terms than this repository's own approved material supports, and is contradicted by a Step-6 record (`pahc.force.alexandria-emergence`) that already documents the second, Bagnall-independent line. `pahc.contested.rivals-undefeated` rates a normative framing instruction as `formation_confidence: Documented` while its own body and `concedes` call it methodological — the exact split its sibling `two-strand-packaging` handles correctly. And `pahc.contested.ignatius-dating`, the record whose stated job is to carry the Ignatius vulnerability "at full strength," quietly halves it. These are fixable in place, but they are not cosmetic: each one weakens the specific discipline the record exists to enforce.

**Findings: 9 SUBSTANTIVE, 6 COSMETIC.**

---

## SUBSTANTIVE findings

### 1. SUBSTANTIVE — `pahc.contested.ignatius-dating.concedes` understates the Ignatius concentration it exists to carry

**File:** `records/pahc/contested_claim/pahc.contested.ignatius-dating.md`

**What's wrong:** `concedes` says the Ignatian material supplies "**roughly half** this world's most vivid quotable material." Three already-approved sources say considerably more than half:

- `worlds/pahc/CiC_W1_Doc02_Source_Ecology_FINAL.md` §1.8: "**Nearly all** of the emotionally vivid, individually-quotable content surfacing across Doc_05, Doc_07, Doc_09, and the World Profile … is Ignatian."
- `records/pahc/source/pahc.source.ignatius-letters.md` (body): "**most** of this world's vivid quotable material rest on this one corpus."
- `records/pahc/world_core/pahc.core.house-church.md` (Absent Stories item 11): "The narratively vivid material clusters **overwhelmingly** in Strand A."

**What I checked:** grepped `vivid|quotable` across `records/pahc/`, `worlds/pahc/build/`, and Doc_02; all three statements agree with each other and disagree with the record. The record's own trailing body claims it exists so the vulnerability has "its own first-class, participant-facing home," and its `concedes` explicitly promises to carry the split "at full strength" — which makes the downward drift a defect against the record's own stated purpose, not a stylistic choice.

**Fix:** change "roughly half" to "most" (matching the source record verbatim) or "nearly all" (matching Doc_02 §1.8 verbatim).

---

### 2. SUBSTANTIVE — `pahc.contested.egypt-exclusion` asserts a single-source dependency the repo's own records falsify

**File:** `records/pahc/contested_claim/pahc.contested.egypt-exclusion.md`

**What's wrong:** two fields overstate the dependency:

- `held_against[1]`: "This world's own build depends on **exactly one scholarly voice (Bagnall)** for this exclusion, **with no second, independent corroborating line**."
- `divergence_note`: "the claim **rests entirely** on secondary scholarship this build cannot independently check."

Four pieces of already-approved material contradict this:

1. `pahc.core.house-church.md` caution 7 — the record's own stated parent — says the boundary rests "**substantially** on one papyrological argument from silence," not entirely. The record hardens its own governing caution.
2. Doc_01 §8.2 grounds the Alexandria distinction on **formation logic** ("household- and correspondence-based pastoral formation here, versus a teaching-relationship-based exegetical-philosophical formation there"), an argument nowhere derived from Bagnall.
3. Doc_01 §2 line 42: "The **Step 0 Conclusion independently dates** the Alexandrian Catechetical/Christian-Platonist Tradition to c. 190–254 CE" — a second, independently-derived line that on its own places Alexandria outside 70–190.
4. Most directly: `records/pahc/force/pahc.force.alexandria-emergence.md`, built and approved at Step 6 in this same repository, records exactly that second line — with `sources: []`, `divergence_note` crediting "the Step 0 Conclusion's own cross-world dating," and **no mention of Bagnall anywhere**. A sibling record in this build is the corroborating line the new record says does not exist.

**What I checked:** read Doc_01 §§2/3/8.2 (lines 42, 60, 120–122), `pahc.core.house-church` caution 7, and the full `pahc.force.alexandria-emergence` record.

**Fix:** align `held_against[1]` and `divergence_note` with caution 7's "substantially" wording; name the two Bagnall-independent supports (Doc_01 §8.2's formation-logic distinction; the Step 0 Conclusion's independent c. 190–254 dating of World #2); and cross-reference `pahc.force.alexandria-emergence`, which is the natural `divergence_partner`-adjacent record even though it is not a source. The disclosure stays honest — the papyrological *silence argument* is still single-source — without misreporting the exclusion decision's actual evidentiary footing.

---

### 3. SUBSTANTIVE — `pahc.contested.egypt-exclusion.held_against[2]` is not a counter-position

**File:** `records/pahc/contested_claim/pahc.contested.egypt-exclusion.md`

**What's wrong:** `held_against[2]` reads: "The Step 0/Doc_01 world-identification process that settled this boundary is already-approved, settled ground per this build's own scope authority — this record discloses the dependency without proposing to reopen the underlying decision." That argues **for** the claim and is build-process scoping language. `held_against[]` is the field that carries what cuts against the claim; padding it with a procedural defence inflates the apparent tension from two real objections to three, in the one record in the batch that most needs its disclosure to be exact.

**What I checked:** compared against the other eight records' `held_against` arrays — every other item in the batch is a real counter-consideration. The same sentence already appears, near-verbatim, in this record's own trailing body ("This is Step 0/Doc_01's own settled scoping decision … and does not propose reopening it"), so removing it from `held_against` loses nothing.

**Fix:** delete `held_against[2]`; the body already says it.

---

### 4. SUBSTANTIVE — `pahc.contested.hermas-dating` has no genuine counter-position

**File:** `records/pahc/contested_claim/pahc.contested.hermas-dating.md`

**What's wrong:** the record's `claim` is the composite multi-stage position — "composed at Rome across roughly 90-150 CE, **in multiple compositional stages**." Neither `held_against` item opposes it:

- `held_against[0]`: "Brox, Leutzsch, and Osiek's composite reading holds that no single date can be assigned to the whole work…" — this **is** the claim, restated. `divergence_note` even names the same three scholars as the position the claim adopts ("the dominant modern position").
- `held_against[1]`: the Muratorian Fragment / Sundberg-Hahneman point undercuts the **traditional mid-2nd-century single date** — a position the record does not hold. It therefore *supports* the claim rather than cutting against it.

Compare the three sibling dating records, all of which name a genuinely opposed position: didache-dating has Milavec (unified, 50–70); first-clement-dating has Welborn (80–140) and Herron (pre-70); ignatius-dating has three mutually exclusive positions. Hermas is the outlier, and the outlier status is structural, not stylistic.

**What I checked:** cross-read the claim, `divergence_note`, and both `held_against` items against `records/pahc/source/pahc.source.shepherd-hermas.md`'s `work` field, which is the authoritative statement of the dispute and which the record otherwise reproduces faithfully.

**Fix:** restructure so the live alternative is the counter-position rather than the knock-down target: state the traditional single mid-2nd-century date (the Muratorian "brother of Pius" synchronism) as `held_against[0]`, and the Sundberg/Hahneman challenge to the Fragment as the reason that alternative is itself insecure. Then add a real objection to the composite reading — that its stage boundaries are inferred from internal seams in a text no Greek manuscript preserves whole (the source record's own eclectic-reconstruction transmission note: Sinaiticus to Mandate 4.3.6, Athous to Similitude 9.30.3, Latin alone for the ending), not from any external evidence. That is a genuine, repo-grounded counter-force the record currently has none of.

---

### 5. SUBSTANTIVE — `pahc.contested.rivals-undefeated` rates a methodological framing as `Documented`, contradicting its own body

**File:** `records/pahc/contested_claim/pahc.contested.rivals-undefeated.md`

**What's wrong:** `formation_confidence: Documented`, but the record describes itself as a build framing choice in two other places:

- trailing body: "this record makes the **METHODOLOGICAL** claim (how these movements must be framed)";
- `concedes`: "The 'undefeated neighbors' framing is **this build's own disclosed corrective** against reading later orthodoxy's settled verdict back into this window."

And the `claim` itself is written as a normative instruction — "**must be read as** live, contemporary, geographically overlapping rivals … not as later, external, or already-settled heresies." A reading instruction cannot be `Documented`; what is Documented is the underlying fact pattern (that these movements existed, in-window, geographically overlapping), which the `divergence_note` correctly isolates.

The batch already contains the correct handling of exactly this situation. `pahc.contested.two-strand-packaging` is the structurally identical case — a build framing over Documented underlying evidence — and it rates itself `Inferential-Thin` with a `divergence_note` that spells out the split ("it is a disclosed methodological choice this build itself makes about how to PACKAGE the underlying evidence (which is Documented …)"). Two records in one batch handle the same problem two different ways.

**What I checked:** read both records' confidence blocks, claims, `concedes`, and bodies side by side; confirmed `gate_confidence_crosscheck` passes rivals-undefeated only because `verification_state: verified-direct`, so nothing mechanical catches this.

**Fix:** either (a) restate the `claim` as the documented factual core — Marcion, Valentinian teaching, and the New Prophecy were live, contemporaneous, geographically overlapping presences inside 70–200 — and move the "must be read as" instruction into `concedes`/body, keeping `Documented`; or (b) keep the normative claim and drop to `Inferential-Thin` with a two-strand-style `divergence_note` split. (a) is the smaller edit and preserves the record's force.

Separately note the `verification_state: verified-direct` is doing a lot of work here for a record whose `held_against[1]` rests on Lieu's secondary reading — see COSMETIC finding E for the same pattern in the martyrdom record.

---

### 6. SUBSTANTIVE — `pahc.limit.f5-e-material-remains` mischaracterises Pliny in its own `sources[]` locus

**File:** `records/pahc/honest_limit/pahc.limit.f5-e-material-remains.md`

**What's wrong:** the locus reads "10.96-97 (the nearest thing this world has to an **outside eyewitness description of a meeting place**)." Both halves are wrong against this repo's own records:

- **Not eyewitness.** `records/pahc/source/pahc.source.pliny-letters.md`: "The most granular detail was extracted from two enslaved women, called ministrae, **under torture** — a method ancient jurists themselves distrusted." `records/pahc/figure/pahc.figure.ministrae.md` says the same. Pliny reports what informants stated under interrogation; he did not witness a gathering.
- **Not a meeting place.** The source record's own content summary lists what the letter carries — "pre-dawn meeting, a hymn 'unto Christ as God' sung responsively, a moral oath, a later reassembly for 'a meal, common yet harmless'" — timing, content, and personnel. Nothing about a physical place.

The second error is the more serious one: this is the world's **material-remains** honest_limit, whose `statement` says in the participant-facing voice "No building tied to us survives." Claiming in the same record's metadata that Pliny gives a description of a meeting place is self-contradictory, and it is precisely the claim an F5-E record must not make.

**What I checked:** read `pahc.source.pliny-letters` (author/work/edition/body), `pahc.figure.ministrae`, `pahc.term.ministrae`, `pahc.term.hetaeria`, and the honest_limit's own `statement` — which, to its credit, gets this right ("comes closer to an **outside view** of a meeting than anything we wrote ourselves"). The defect is confined to the locus field.

**Fix:** `locus: "10.96-97 (this world's only outside, non-Christian description of its worship — reported under interrogation rather than eyewitnessed, and silent on the physical place)"`.

---

### 7. SUBSTANTIVE — `pahc.contested.ignatius-dating` misses a genuine F2-E match; its exclusion rationale tests only one of the cell's four questions

**Files:** `records/pahc/contested_claim/pahc.contested.ignatius-dating.md`, `records/pahc/contested_claim/pahc.contested.martyrdom-polycarp-dating.md`

**What's wrong:** ignatius-dating's body justifies `canon_cells: []` with "no fleet canon question asks participant-facing 'is your own source authentic,' and this record does not manufacture a match where none exists." That is true of the phrasing it tests, but F2-E holds four questions, and `_fleet.canon.f2-e-01` is **"How much of what you've told me would hold up in a university library?"** — the scholarly-standing question. This world's single largest honest answer to it is that its most load-bearing corpus is under a three-way authenticity split, which is exactly this record's content.

Two further checks confirm the match rather than the exclusion:

- The repository's own reference record for that cell is `records/fix/honest_limit/fix.limit.f2-e-scholarly-scrutiny.md`, whose `statement` answers f2-e-01 near-verbatim ("how much of what we have told you would hold up in a university library"). F2-E *is* the scholarly-scrutiny cell in this schema's established usage.
- Cell reuse is already this batch's declared practice (F1-I, F3-I, F3-T all reused deliberately), and F2-E is already shared by `pahc.contested.martyrdom-polycarp-dating`, `pahc.force.selective-canonization`, and `pahc.force.transmission-network` — so adding a second contested_claim to it breaks no rule.

The martyrdom record's body compounds this: it justifies its own F2-E claim by ruling that the Ignatius, Didache, and 1 Clement disputes "are left uncovered by this cell rather than stretched to match it" — a judgement made entirely against f2-e-02 ("Isn't most of what's said about you legend…"), with f2-e-01 and f2-e-03 ("Where is your own record thinnest?") never considered.

**What I checked:** read all four F2-E canon_question records in `records/_fleet/canon_question/`; confirmed via `canon.classify_cell` that F2-E is currently blank and that contested_claim membership does not close it (so this is a retrieval-grounding gain, not a coverage claim).

**Fix:** add `F2-E` to `pahc.contested.ignatius-dating.canon_cells`, justified in the body against **f2-e-01** specifically; and amend the martyrdom record's body so its exclusion reasoning is scoped to f2-e-02 rather than asserting the other dating disputes are uncovered by the whole cell.

---

### 8. SUBSTANTIVE — `generate_contested_index.py` hardcodes a computed count, guaranteeing a future contradiction

**File:** `worlds/pahc/build/generate_contested_index.py`

**What's wrong:** the generator computes `blank` correctly and emits `f"- **{len(all_ids)} total cells; {len(blank)} still blank**"`, then immediately hardcodes the same number in prose on the next line: `"- These **17** remaining blanks are deferred to Steps 8-9 …"`. The same sentence also hardcodes "F5-E is the only cell this step closed."

The output file is stamped "**GENERATED … do not hand-edit**," so the next time any cell closes (Steps 8–9 will close several by design), a regeneration produces a document that states two different blank counts three lines apart, and a reader has no way to know which is authoritative.

**What I checked:** ran the generator; output is byte-identical to the committed `CONTESTED-CLAIMS-INDEX.md`, and `len(blank)` is currently 17, so the file is correct *today* — this is a latent bug with a certain, not speculative, failure mode.

**Fix:** `f"- These {len(blank)} remaining blanks are deferred to Steps 8-9 …"`, and derive the "F5-E is the only cell this step closed" clause from the `limits` dict rather than hardcoding it.

---

### 9. SUBSTANTIVE — `pahc.contested.didache-dating` drops the provenance caveat its own source record carries, and the batch misses the resulting cross-record tension

**Files:** `records/pahc/contested_claim/pahc.contested.didache-dating.md`, `records/pahc/contested_claim/pahc.contested.egypt-exclusion.md`

**What's wrong:** `concedes` describes the Didache as "one community's own manual, **plausibly Syrian**." That reproduces `pahc.core.house-church` caution 5 faithfully, but the record's own cited source record is more careful:

- `records/pahc/source/pahc.source.didache.md`, `author`: "Anonymous/composite (**provenance unresolved — Syria likely, Egypt argued**)"
- same record, body: "**Provenance (Syria vs. Egypt) unresolved.**"
- Doc_01 §Source notes (line 146): "**Provenance (Syria vs. Egypt) is unresolved.**"

The dropped alternative matters more than usual in this specific batch, because `pahc.contested.egypt-exclusion` — drafted in the same commit — removes Egypt from this world's scope entirely. Taken together the two records leave an unaddressed tension: the world's central catechetical text has a live-argued Egyptian provenance, and the world excludes Egypt. Neither record notices. That is the kind of interaction a contested-claims step exists to surface, and it is currently invisible.

**What I checked:** compared the concedes text against the source record's `author` field and body and against Doc_01 line 146; confirmed neither contested_claim mentions the other or the provenance question.

**Fix:** restore the caveat in `concedes` ("provenance unresolved — Syria likely, Egypt argued"), and add a sentence to `pahc.contested.egypt-exclusion`'s `held_against` or body naming the Didache-provenance interaction as a live consequence of the exclusion. This strengthens both records rather than weakening either.

---

## COSMETIC findings

### A. COSMETIC — `pahc.contested.ignatius-dating` body miscounts where "THE IGNATIUS VULNERABILITY" appears

The body says the vulnerability is flagged as `"THE IGNATIUS VULNERABILITY"` in "**three** gravity records (authority-consolidation, martyrdom-meaning, boundary-drawing)." Grepping the literal string across `records/pahc/` returns exactly two hits — `pahc.gravity.authority-consolidation` and `pahc.gravity.martyrdom-meaning`. `pahc.gravity.boundary-drawing` carries the same substance under a different heading, "THE THIRD-ASIA-MINOR-PROFILE ITEM." **Fix:** "…in two gravity records under that label, and in `pahc.gravity.boundary-drawing` as THE THIRD-ASIA-MINOR-PROFILE ITEM."

### B. COSMETIC — the honest_limit's convention claim is slightly overstated

The body claims first-person **"we"** voice "per this schema's established convention for honest_limit.statement (confirmed against `records/fix/honest_limit/*.md`, the only other honest_limit records in this repository)." The "only other" half is correct — I confirmed the four `records/fix/honest_limit/` files are the sole others in the tree. But three of the four use "we" and `fix.limit.unbuilt-appendix-a-cells` uses **"I"** ("my fixture record," "I was made from two short synthetic texts"). The convention is first-person; "we" is the majority form, not the rule. **Fix:** "first-person voice (three of the four fixture records use 'we', one uses 'I'; 'we' chosen here for a community-voiced world)."

*(The voice discipline itself holds. `statement` stays in "we" throughout, never slips into third-person world-description or a named in-world role, and carries no date, name, "ruled", or "WORKING SCOPE" — confirmed both by reading and by `gate_no_build_attribution` returning clean. FK grade 5.6 via `engine.m1.fk.fk_grade`, well inside the ≤10 ceiling.)*

### C. COSMETIC — "two independent methods" is the exact wording the cited index corrects

`why_sources_cannot_answer` says the G06 finding was "verified by **two independent methods**," then immediately self-corrects ("both tracing to the identical underlying fact rather than two convergent lines of evidence"). `GRAVITY-INDEX.md`'s "Not advanced" entry deliberately words this as "verified twice by **different** methods … **not** two separately-derived confirmations," precisely to block the "independent" reading. The trailing clause rescues the sentence, but the loaded word should not be there. **Fix:** "two different methods," matching the index verbatim.

*(Otherwise the G06 citation is accurate: the quoted obligation — "a future honest_limit or contested_claim record for that cell should cite this finding directly rather than leaving it only in this generated index" — is verbatim from `GRAVITY-INDEX.md` line 63, and the scholar list (Meeks, Gehring, Balch, MacDonald), the Repetition-test failure, and the missing household-code registry rows all match the index exactly.)*

### D. COSMETIC — `pahc.contested.egypt-exclusion` overshoots Bagnall's terminus and never names the monograph

The claim says Bagnall found "no securely attributable Christian documentary evidence from Egypt **within this world's own 70-200 CE window**." Doc_01 §3 bounds it differently: "essentially silent **before Bishop Demetrius (189–231)**." Demetrius's episcopate begins inside the window, so the record states the silence claim a decade stronger than its own approved source. Separately, Doc_01 names the work (*Early Christian Books in Egypt*, Princeton, 2009) and the record does not — given `sources: []` is deliberate, naming the monograph in the claim text costs nothing and makes the disclosure checkable. **Fix:** "…before Bishop Demetrius (189–231), per Roger Bagnall, *Early Christian Books in Egypt* (Princeton, 2009)."

### E. COSMETIC — `pahc.contested.martyrdom-polycarp-dating`'s confidence block is out of step with its three siblings

It carries `citation_specificity: A` / `verification_state: verified-direct`, where didache/first-clement/hermas/ignatius-dating all carry `B` / `named-not-rechecked`. Two of its three `held_against` items rest on unrechecked modern scholarship — one on an unnamed consensus ("widely regarded by modern scholarship as later redactional additions") and one on Eusebius's Chronicon date, which is attested in `pahc.source.eusebius-historia-ecclesiastica`'s body but is not in the vendored NPNF2 volume. The text-internal facts (chapters 20–22 present; the bone-collection wording) genuinely are verified-direct, so this is defensible — but it is inconsistent within the batch and no gate catches it. **Fix:** downgrade to `verified-via-authority`, or add a body sentence stating which of the record's claims the `verified-direct` rating covers.

*(I checked and am **not** flagging the Chronicon `locus`: the batch's convention is loci that point at a source record's own dating note — "the work's own dating note," "the letter's own dating note" — so "the Chronicon's own 167 CE date" is in keeping, and the Eusebius source record does carry that fact in its screen note.)*

### F. COSMETIC — the generated index omits the two fields a reviewer most needs

`generate_contested_index.py` emits `canon_cells`, `formation_confidence`, `claim`, and `concedes` for contested_claims, and `canon_cells` + `why_sources_cannot_answer` for honest_limits. It never emits `held_against[]` — so a reviewer working from the index alone cannot check whether any counter-position carries real force, which is this record type's central discipline and the source of four of the nine substantive findings above. It also never emits the honest_limit's `statement`, the one field `engine/m2/builders.py:build_prompt()` compiles into a live model's context and the only field `gate_readability` FK-checks. **Fix:** add `held_against` (as a nested bullet list) and the honest_limit `statement` to the generator.

---

## Verified clean (checked, no finding)

Recorded so a later reader knows these were actually tested, not skipped:

- **Gate battery.** `gates.run_all(load_world_records("pahc"), load_fleet_records(), registry)` → all 13 gates return empty except `canon-coverage`, which reports the 17 pre-existing blank cells. No schema, referential, reciprocity, completion, confidence-crosscheck, readability, or build-attribution finding anywhere in the batch.
- **FK ceiling.** `fk_grade(pahc.limit.f5-e-material-remains.statement)` = **5.60**, ceiling 10.
- **Generator/record sync.** Re-ran `generate_contested_index.py`; output byte-identical to the committed file, including all nine `claim`/`concedes` strings, all `formation_confidence` values, all `canon_cells` lists, and the blank-cell list. `git status` clean afterward.
- **Blank-cell list matches `classify_cell`.** The index's 17 still-blank cells are exactly what `canon.classify_cell` reports, and exactly what `gate_canon_coverage` flags.
- **All five claimed canon cells are genuine, not stretches.** F1-I ↔ `f1-i-02` "What did you argue about among yourselves?" (two-strand-packaging is precisely this world's central internal argument); F3-T ↔ `f3-t-02` "Did you have denominations…?"; F3-I ↔ `f3-i-01` "Who held authority among you…?" (rome-monepiscopacy answers the ending-stage half); F2-E ↔ `f2-e-02` "Isn't most of what's said about you legend…?" (a real fit for the one hagiographic-genre text in the set); F5-E ↔ `f5-e-01`/`f5-e-02` — the honest_limit's first two sentences restate both questions almost word for word, the closest match in the batch. The three deliberate cell reuses are each substantively justified in their own bodies.
- **Deferral of the other 17 cells is sound.** Spot-checked five against already-built pahc material: **F1-P** (doubt) — `pahc.figure.hermas` already names "the doubt question (the double-minded soul, Commandment 9)"; **C-P** (personal register) — Hermas's own visions and Ignatius's Romans are both registered; **F5-T** (marriage/money) — Hermas, Didache almsgiving, and 1 Clement are all registered; **F2-T** (scripture's authority) — caution 10's no-closed-canon framing plus Barnabas and Justin's Dialogue are registered; **F6-T** (outsiders/divorce) — Hermas Mandate 4 and Barnabas's two-ways are registered. None is a structural evidentiary gap; all are unbuilt topics. **The judgement that F5-E is the only cell needing an honest_limit at this step holds.**
- **Faithful source-record cross-checks (no drift found):** the Didache dating range and Niederwimmer/Milavec split, the Bryennios manuscript details (1056 CE, found 1873) and the corroboration list (correctly omitting the Doctrina Apostolorum, which the source record notes witnesses the underlying Two Ways rather than the Didache); Welborn's 80–140 and Herron's pre-70 for 1 Clement; Brox/Leutzsch/Osiek, the Muratorian "brother of Pius" synchronism, and Sundberg/Hahneman for Hermas; Barnes/Foster (130s–140s), Huebner/Lechner ("Munich school," 160–180, Roman provenance), and the Ussher/Vossius/Pearson vs. Daillé and Cureton vs. Zahn/Lightfoot sequence for Ignatius; Tertullian c. 207–208, Irenaeus c. 180 from Gaul, the doubly-mediated anti-Montanist fragments, and Lieu's heresy-construction framing for rivals-undefeated. **No position was found attributed to the wrong scholar or the wrong side anywhere in the batch.**
- **Doc_08 quotation is verbatim.** `pahc.contested.rome-monepiscopacy-dating`'s body quotes Force 3B-1's confidence tag as "Well-established for the general pattern per Sullivan and Lampe; Contested on the precise Roman dating, per Lampe's own specific account" — an exact match to `CiC_W1_Doc08_Forces_Document.md` line 219. Its claim and `held_against` are also consistent with `pahc.force.monepiscopacy-consolidation` and `pahc.gravity.authority-consolidation`, with no contradiction found.
- **`nearest_material` targets all resolve** (`pahc.core.house-church`, `pahc.figure.ministrae`, `pahc.term.ekklesia` all exist) and are genuinely the nearest material — `pahc.term.ekklesia`'s `false_friend` already carries "a church building (there are none in this window)."
- **`pahc.contested.egypt-exclusion`'s empty `sources`/`divergence_partners` are honestly disclosed** — the body states plainly that Bagnall's survey is secondary scholarship this registry does not vendor and that no citation was manufactured. That specific disclosure is correct; findings 2 and 3 above concern the *strength* of the dependency claim, not the absence of the source.
- **`held_against` carries real force in six of nine records** (didache, first-clement, ignatius, martyrdom-polycarp, rivals-undefeated, rome-monepiscopacy, two-strand-packaging — seven, in fact), and `concedes` concedes something substantive in all nine. `two-strand-packaging`'s concession that "no primary voice in this world's evidentiary base uses 'Strand A'/'Strand B' language" and `ignatius-dating`'s that three gravities "would need reconsidering, not merely re-labeling" are the strongest in the set.

---

## Suggested disposition

Fix findings 1–9 in place; findings 2, 4, and 5 are the ones that change what a record actually asserts and should be re-read after editing. Findings A–F are safe to batch into the same pass. No record needs rebuilding from scratch, no already-approved upstream document needs reopening, and the step's central judgements — one honest_limit at F5-E, contested_claims for the four dating disputes plus the three framing disclosures plus Egypt, and cell reuse where a real match exists — are all sound as drafted.

---

## Round-2 verification

Performed by this build thread directly (Read/Grep/Bash, plus direct `yaml.safe_load` field checks and a live `fk_grade` call), not re-dispatched as a second agent — the same precaution taken at Steps 4-6: check each fix against the actual file content, don't trust a fix-list summary.

**All 9 SUBSTANTIVE findings, fixed and verified:**

1. `ignatius-dating.concedes` — "roughly half" replaced with "most (per pahc.source.ignatius-letters's own body)." Grepped for "roughly half" — zero live hits.
2 & 3. `egypt-exclusion` — `held_against[1]` and `divergence_note` rewritten to name the second, Bagnall-independent line (Doc_01 §8.2's formation-logic distinction; the Step 0 Conclusion's independent Alexandria dating, cross-referenced to `pahc.force.alexandria-emergence` via `divergence_partners`) and softened to caution 7's own "substantially." The procedural `held_against[2]` was deleted (confirmed: the array now has 2 items, not 3). `claim` corrected from the whole 70-200 window to Doc_01 §3's actual "before Bishop Demetrius (189-231)," with the monograph named (cosmetic D, folded in here).
4. `hermas-dating` — restructured so `held_against[0]` is the real traditional-single-date counter-position and `held_against[1]` is a genuine objection to the composite reading's own evidentiary basis (inferred stage boundaries in an eclectically-reconstructed text); the Sundberg/Hahneman point moved into `concedes` where it explains rather than duplicates. Confirmed via direct reread: neither remaining `held_against` item restates the claim.
5. `rivals-undefeated` — `claim` restated as the documented factual core (movements were in-window, geographically overlapping); the normative "must be read as... not as..." framing moved into `concedes`, explicitly marked as this build's own further methodological corrective, not a second Documented fact. `formation_confidence: Documented` kept, now consistent with what the claim field actually asserts — verified by parsing the YAML field directly, not just reading prose.
6. `pahc.limit.f5-e-material-remains` — Pliny `sources[].locus` corrected to drop both the "eyewitness" and "meeting place" claims, replaced with "reported under interrogation rather than eyewitnessed, and silent on the physical place."
7. `ignatius-dating` gained `canon_cells: [F2-E]` with body justification against f2-e-01 specifically; `martyrdom-polycarp-dating`'s body reworded so its own exclusion reasoning is scoped to f2-e-02, not the whole cell. Confirmed both files' `canon_cells` fields directly.
8. `generate_contested_index.py` — the hardcoded "17" and hardcoded "F5-E is the only cell" sentence both replaced with values derived from `len(blank)` and the `limits` dict at generation time. Regenerated the index; output unchanged today (17 blank, F5-E only) because the underlying facts haven't changed, confirming the fix doesn't alter current behavior while removing the future-contradiction risk.
9. `didache-dating.concedes` — restored "Syria likely, Egypt argued" per `pahc.source.didache`'s own author field, and named the resulting tension with `egypt-exclusion`; `egypt-exclusion`'s own trailing body now names the same tension from its side. Confirmed both records now cross-reference each other.

**All 6 COSMETIC findings, fixed and verified:**
- A: ignatius-dating body corrected to "two gravity records under that label, and... boundary-drawing as THE THIRD-ASIA-MINOR-PROFILE ITEM."
- B: honest_limit body's convention claim corrected to note 3-of-4 use "we," one uses "I."
- C: "two independent methods" → "two different methods" in the honest_limit's `why_sources_cannot_answer`, matching GRAVITY-INDEX.md verbatim. Confirmed via direct field parse.
- D: folded into fix 2/3 above (Bagnall's monograph named, Demetrius date substituted for the full window).
- E: `martyrdom-polycarp-dating`'s confidence block downgraded to `B`/`named-not-rechecked`, matching its three sibling dating records; confirmed `gate_confidence_crosscheck` still passes (formation_confidence is `Contested`, not `Documented`, so the gate's null-divergence-note rule never applied either way).
- F: `generate_contested_index.py` now emits `held_against` (nested bullets) for every contested_claim and `statement` for the honest_limit. Confirmed in the regenerated `CONTESTED-CLAIMS-INDEX.md` — all 9 records now show their held_against list, and the honest_limit's full statement appears.

**Regression checks:**
- Full YAML parse sweep: all 82 pahc record files parse cleanly.
- Full gate battery: clean on all 13 gates except `canon-coverage`, reporting the same 17 pre-existing blank cells as before this round of fixes — no new gaps, no regressions.
- `fk_grade` on the (unchanged) honest_limit `statement`: 5.60, unchanged and still well under the ceiling of 10.
- Regenerated `CONTESTED-CLAIMS-INDEX.md`; `git status` shows only the expected content changes, no drift between generator and committed file.

**Verdict: All 9 SUBSTANTIVE and all 6 COSMETIC findings LANDED CORRECTLY, confirmed against live file content (including direct YAML field parses, not just prose grep) and a clean re-run of the full gate battery. Step 7 ready for disposition.**
