# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 2 Independent Adversarial Review

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md` (Round 2 draft, Round 1 revised)
Reviewer role: independent adversarial. Did not author the finding document, its Round 1 review, the discovery pass, or any Doc_04 round. Brief: **do not trust §11.** Verify, per Round 1 substantial finding, that the fix landed *in the document body*, is correct, and introduced no new error; then re-derive every new claim from primary sources; then re-test the headline.
Method: `cic/corpus-map/alexandria-catechetical.yaml` parsed programmatically with PyYAML (all 65 rows, 14 anf06 rows enumerated by `source_file`); `anf06…xml` and `npnf201…xml` and `npnf214…xml` tag-stripped and word-counted with independent scripts; `records/alx/` walked (192 files, 14 type directories) and every cited record read in full; `Doc_04`, `Doc_02`, `Open_Gaps_Tracking.md`, `S6.2_ALX_FREEZE_DECLARATION.md`, `S6.2_IJC_FREEZE_DECLARATION.md`, `records/worlds.yaml`, `engine/`, `packages/alx/` opened directly; `git log`/`git show --stat` used to establish what this pass actually wrote to disk; the `cic-build-cycle` SKILL.md read for every definition the document quotes.
Date: 2026-09-09

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**The headline conclusion is still correct.** "This material is **not structural**" survives a second, harder attack. I re-ran Round 1's routes and added the two the document still has not run, and the classification set does not move.

**But §11 overstates what landed.** Of Round 1's eight substantial findings, **four are cleanly resolved, three are partially resolved, and one is not resolved at all — it is a fresh instance of the very defect it claims to have fixed.** Two of the repairs introduced new factual errors that Round 1 had itself flagged elsewhere in the same document.

The single worst item: **§10 asserts that this pass added "an `Open_Gaps_Tracking.md` entry." It did not.** `git show --stat` for both of this pass's commits (`b50302d`, `48ca471`) shows exactly three files touched — the finding, the Round 1 review artifact, and nothing else; `Open_Gaps_Tracking.md` is untouched since `f07eb91`, and a grep of it for `unused`, `Peter of Alexandria`, `Theognostus` and `Pierus` returns nothing. Round 1's S-8 was precisely "the document asserts a completed artefact it did not have." §11 item 8 claims that fixed. It is not fixed; it has been relocated. It also flatly contradicts the document's own Status line ("No world-build document… was changed by this pass"), since `Open_Gaps_Tracking.md` is a world-build document in the same folder. `cic-build-cycle` names this failure mode in its own CO-022 note: *"review content claimed as shown when it wasn't included."*

Counts this round: **8 substantial, 10 cosmetic.** The disposition (§9 Option B, escalated, not self-disposed) remains sound and should stand.

---

## A. ROUND 1's EIGHT SUBSTANTIAL FINDINGS — VERIFIED INDEPENDENTLY

I did not read §11 as evidence of anything. Each row below was checked against the document body and the primary source.

| Round 1 | Subject | Round 2 status |
|---|---|---|
| S-1 | Corpus-map assignment set; the npnf214 fourth Peter work | **RESOLVED** |
| S-2 | Frozen / Approved-to-proceed conflation | **RESOLVED** |
| S-3 | "two governing disciplines" | **RESOLVED** |
| S-4 | §5.2 not attributable to this corpus | **PARTIALLY RESOLVED** |
| S-5 | §4 net-effect overstatement + uncited `contested_claim` | **PARTIALLY RESOLVED — FIX INTRODUCED NEW ERROR** |
| S-6 | Cross-Stratum Test never run | **RESOLVED** |
| S-7 | T3 unexamined + Athanasian transmission risk | **PARTIALLY RESOLVED — FIX INTRODUCED NEW ERROR** |
| S-8 | Self-asserted status | **NOT RESOLVED — new instance of the same defect** |

### S-1 — **RESOLVED.**
§3.2 (lines 85–98) now names both volumes. I re-parsed the corpus map: 65 works total, 14 with `source_file: anf06…`, and the npnf214 row is real and exactly as described — `work: The canons of Peter of Alexandria, from his Sermon on Penitence`, `author: peter_alexandria`, `locus: div2 17.6 (~551 words)`, `confidence: assigned`, note *"NOTE A DUPLICATE… Two vendored witnesses to one text"* and *"Split 2026-08-26 on Mark's ruling"* (yaml lines 634–646). I opened the witness itself: `npnf214…xml` line 43159, `div2 id="xvii.vi"`, title *"The Canons of the Blessed Peter, Archbishop of Alexandria, and Martyr, which are found in his Sermon on Penitence."* It exists. §9's Option B now carries the both-witnesses remedy ("**handling both vendored witnesses**… or explicitly declining one"). The fix landed and is correct. See c-4 for one thing it should still say about that witness.

### S-2 — **RESOLVED, and every element re-verified.**
§8 reason 3 (lines 440–448) now splits the two freezes. Both halves check:
- **World NOT frozen.** `Open_Gaps_Tracking.md` line 145: *"Because this is unresolved, the world is NOT frozen"* — verbatim; also lines 78, 140, 160. `Doc_04` line 10 ends *"not 'Frozen.'"* — verbatim.
- **S6.2 baseline IS frozen, 2026-07-28.** `Archive/Technology-Pass2-2026-08/Pass2/gates/S6.2_ALX_FREEZE_DECLARATION.md` line 3: `**Date:** 2026-07-28.` Lines 58–61: *"The Alexandria record store (156 in-world records), the deployed chunks generated from it, the deployed Theon Permanent Prompt (as amended by the two fix sessions), and the validated behaviors above are FROZEN as the S6.2 per-world baseline."* The document's ellipsis is fair.
- The added parenthetical **"(not 2026-08-01, which was the last world's)"** is correct and better than Round 1's own C-4 gloss: `S6.2_IJC_FREEZE_DECLARATION.md` is dated 2026-08-01 and is headed *"World 6 of 6."*
The path placeholder Round 1 flagged is gone; §2's table and §8 both cite the real `S6.2_ALX_FREEZE_DECLARATION.md`.

### S-3 — **RESOLVED.**
§5.1 (lines 208–214) now grounds itself correctly. `Doc_04` line 31 is headed *"Method, Phase Scheme, and the Two Governing Disciplines"*; line 46 is **"Discipline One — the Origen SYSTEMIC screen"** and line 48 **"Discipline Two — the cross-build (desert) constraint"**; Eusebius appears as the closing sentence *inside* Discipline One (*"a second, distinct HIGH-risk dependency… screened separately"*). The document now says exactly that, and rests the finding on the narrower ground `cic-build-cycle` SKILL.md line 46 actually supplies (*"a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary"* — verbatim).

### S-4 — **PARTIALLY RESOLVED.**
The §5.2 restatement is right and I verified both records verbatim: `alx.gravity.learning-formation` line 43 `name: 'Learning-Formation Integration [SUPPORTING - temporally qualified: the school period, c. 150-254]'`; `alx.figure.didymus` line 35 `floruit: head of the Alexandrian teaching tradition for roughly half a century, to 398` and line 38 `bridge_line: the blind teacher who held the school's chair for fifty years`. Doc_04 §3.5 line 126 gives *"strongly operative early/mid (c. 150–254)."* The heading now reads "[SUBSTANTIAL — **pre-existing internal contradiction, not produced by this corpus**]," and Didymus is correctly used as the *disproof* of a Persistence flip. Good.

**What did not land:** Round 1's S-4 had a second consequence — *"§5.2 therefore does not support the document's claim that this material is 'not merely supplemental,' because that particular finding is not a product of this material."* §8 (line 426) still answers **"Is it merely supplemental? No."** by listing "**§5.2 is a live contradiction between two record-store records on a scope boundary**" as one of four grounds. The document concedes in the §5.2 heading that §5.2 is not produced by this corpus and then counts it anyway, four hundred lines later. §5.1, §5.3, §5.4 and §7 carry that argument on their own; §5.2 must come out of it.

### S-5 — **PARTIALLY RESOLVED; the repair introduced a new error.**
The good half: new §4.5 (lines 172–187) replaces "school continuity argument substantially weaker" with the precise claim (three men's headships), adds *HE* VII.32 on Achillas, and cites `alx.contested.didaskaleion-institution`. I verified the Achillas material at `npnf201…xml` lines 43062–43078 (editorial note, verbatim as quoted) and, independently, at line 43204 where **Eusebius's own text** says Achillas was *"placed over the school of the sacred faith."* §4.5 uses the latter; §4.2 still quotes only the editor's note, which is the understatement Round 1 flagged at (e), but §4.5 repairs the net effect.

**The new error — a truncation that removes the record's own temporal limit.** §4.5 quotes the `contested_claim` as: *"A real tradition of learned Christian teaching in Alexandria across the whole horizon is not in doubt… What is contested is its INSTITUTIONAL form and continuity."* The record's `concedes` field actually reads: *"What is contested is its INSTITUTIONAL form and continuity **before Origen's era.** The world is therefore anchored on the tradition, not the institution."* The quotation stops at the exact word before the limitation. The record's `claim` field names heads only to Dionysius, and its `held_against` turns on *"whether any formal institution predates c. 215-230."* All three men §4 is arguing about — Theognostus (fl. c. 260), Pierus (fl. c. 275), Peter (bp. 300–311) — are **after** Origen's era, i.e. outside what that record contests. The charge that the corpus-map notes "**contradict a record this world already holds**" therefore survives only through the record's *unscoped voice consequence* ("never of 'the School' as a documented continuous institution"), not through the `concedes` field the document quotes. See N-3: the same truncation pattern recurs at §3.3.

### S-6 — **RESOLVED.**
New §6 (lines 349–379) runs the test explicitly. I checked its representation of both inputs. `Doc_04` §5 (lines 173–186): the Cross-Stratum Test is the declared Article 21 substitute ✓; the test question — *"attested across registers (literate/non-literate, Greek/Coptic, urban/desert), or only within the literate-Greek stratum"* — is verbatim ✓; *"Every Primary and Supporting gravity is attested within the literate-Greek stratum only"* ✓; OG-4 is indeed the highest-stakes open item (`Open_Gaps_Tracking.md` line 240 heads it *"highest-stakes open item, deferred to Article 31"*) ✓. `alx.source.alexandrian-canonical-answers`: *"This is a bishop's desk, not a school"* and *"It is evidence about the conditions of ordinary believers' lives, which this world says it lacks"* are both verbatim (the ellipsis joins two separate paragraphs of that record, which is signalled and does not distort). Doc_02 line 207: *"evidential visibility must not be silently converted into ecological visibility"* — verbatim, and it is in §6 as cited.

**The reasoning is sound.** A literate Greek bishop legislating *about* the lapsed is the same register looking outward, not a second register. The negative result is right. One gap, recorded as c-9 rather than substantial: §6 never names Doc_04 §5's own two held-open majority-organizing candidates (*communal-liturgical belonging* and *martyrdom-as-formation*), which is what Canon XV and the whole T4 discussion respectively map onto — the section that exists to close S-6 should say which of Doc_04's named holes it just failed to fill.

### S-7 — **PARTIALLY RESOLVED; the repair introduced a new error and left the document's own screen unapplied.**
The Athanasius counter-weight landed in §5.1 and is exact: Doc_02 Stream 12 (line 77) *"Athanasius's post-Nicene concentration risks making doctrinal conflict appear more central to ordinary formation than it was"* — verbatim. New §5.4 exists. Peter's Fragment VI is real and quoted correctly: `anf06…xml` line 28084, `div3 id="ix.vi.vi"`, title *"Of the Soul and Body,"* and the text reads *"whence it is manifest that man was not formed by a conjunction of the body with a certain pre-existent type"* — verbatim.

**New error 1 — the date claim is false.** §5.4 (lines 317–320) says the fragment is *"c. 300 — pre-Nicene, Eusebius-independent, and **sitting inside the very interval Doc_04 calls thin.**"* Doc_04 calls two things thin: the *"Inter-phase interval c. 254–296"* (§0, line 36) and T3's *"mid-horizon instance (Origen–Demetrius)"* (§3.6). Peter is bishop 300–311. He is in **neither**. Doc_04's own phase scheme puts c. 300 in the **Late / post-Nicene** phase (c. 296–400) — the phase Doc_04 calls well-attested. Round 1 flagged this exact slip in its §E ("Peter… is bishop from 300, outside 254–296 on any reading"); the revision reproduced it in a new section. The correct and still-interesting claim is narrower: Fragment VI pushes T3's boundary-pole evidence **back before Nicaea**, at the front edge of the late horizon. It does not fill the thin middle, and the sentence *"T3's evidence is therefore not the 'thin middle, strong late' shape Doc_04 describes"* does not follow from a single fragment sitting inside the strong-late end.

**New error 2 — the document exempts its own best find from its own screen.** ANF's note on Fragment VI (line 28089) gives its provenance: *"Ex Leontii et Joannis Rer. Sacr., lib. ii. Apud Mai, Script. Vet., tom. vii. p. 85."* This is a 7th–8th-century florilegium (the *Sacra Parallela*), printed from Cardinal Mai. Five paragraphs earlier, §5.1 insists — rightly — that *"Trading a HIGH Eusebius screen for an unexamined Athanasius mediation would be no gain."* §5.4 then calls Fragment VI "pre-Nicene, Eusebius-independent" and applies no transmission screen at all. **"Pre-Nicene" is accurate as to composition; it is not a statement about the witness.** A document that made the Athanasius caveat a required travelling companion for Theognostus owes the same for a fragment that reaches us through a Byzantine catena.

On the brief's question: **"strengthens but does not reclassify" is right on the reclassification half** — T3 already PASSes, is already Tensional, and its poles are untouched. On the "strengthens" half the document **over-claims**, by the two errors above.

### S-8 — **NOT RESOLVED. New instance of the same defect.**
What did land: the header no longer says "independently reviewed," it states the actual Round 1 outcome and "Round 2 review pending — this document is not cleared"; and no OG number is pre-assigned (grep for `OG-` returns only genuine OG-4 references). Good, as far as it goes.

What replaced it: **§10 line 515–517 — "Files added by this pass: this document, its Round 1 review artifact… and an `Open_Gaps_Tracking.md` entry."** No such entry exists. `git show --stat b50302d` = 1 file (the finding). `git show --stat 48ca471` = 2 files (the finding, the Round 1 review). `git status --porcelain` is clean. `Open_Gaps_Tracking.md` was last touched in `f07eb91` and contains nothing about this finding. This is the same class of claim S-8 named, in the same document, one section away from where it was removed — and it contradicts the Status line's own "No world-build document… was changed by this pass." Delete the clause or write the entry.

---

## B. THE NEW CLAIMS — RE-DERIVED FROM PRIMARY SOURCES

Eight claims Round 1 never saw. **Six check out; one is materially imprecise; one is false.**

**1. §3.2's npnf214 fourth Peter work — CONFIRMED.** See S-1 above. Locus, word estimate, confidence, split date and duplicate note all verified against the yaml and the XML.

**2. §3.5's counts — CONFIRMED, with a wording ambiguity (c-3).** My own PyYAML parse: 14 works carry `source_file: anf06…`. A grep of all 192 files under `records/alx/` for `anf06` returns exactly two **source** records — `alx.source.gregory-address-to-origen` and `alx.source.dionysius-extant-fragments` (plus a figure, a story, a quote and two search records that reference the same two openings). So **14 assigned, 2 opened, 12 unopened** is exactly right, and the arithmetic closes: 5 works for the three named figures + Alexander + Dionysius *Exegetical Fragments* + Phileas, Theonas, Anatolius, Pamphilus, Methodius = 12. **Alexander of Alexandria has zero records**: `grep -ril "alexander" records/alx/` returns **nothing at all** — not a figure, not a source, not a mention. His row is real (`yaml` lines 6–19, `div2 10.3`, `confidence: assigned`, *"the earliest documents of the Arian controversy"*). §3.5's judgement that he "is arguably a stronger candidate than anything the discovery pass named," named-and-not-pursued, is correct and correctly disciplined.

**3. §5.3's Canon IX — CONFIRMED VERBATIM; the characterization is fair and, if anything, conservative.** The right Canon IX is cited. `anf06…xml` line 27036, `div3 id="ix.iv.ix"`, inside Peter's `div2 ix.iv` — **not** the Gregory Thaumaturgus Canon IX at line 2195 (`div4 id="iii.iii.iii.ix"`, on property left behind by barbarians), which the document nowhere confuses with it. Every quoted string is verbatim: *"as it were from sleep, themselves leap forth upon a contest"*; *"take no heed unto His words"*; *"often retired from those who would lay snares for Him"*; *"delivered not up Himself"*; and the decisive clause, at line ~27063, *"Now, He says, they will deliver you up, and not, ye shall deliver up yourselves"* — the document's elision of "Now, He says," is honest.

**"Explicit, argued discouragement of voluntary martyrdom" is not an overread.** The canon argues it from four scriptural moves (Matt. 26:41; 6:13; 26:55; 10:17–18, 23) and from Christ's, Stephen's, James's, Peter's and Paul's example, and the document correctly reports the counterweight that they are still to be communed with. The vendored apparatus agrees in its own voice: **Balsamon**, at line ~27110, *"although he reprehends those who act so, yet he enjoins the faithful nevertheless to communicate with them."* Independent corroboration the document did not use: the **npnf214 witness's own epitome of Canon IX** reads *"That they who provoked the magistrates to persecute themselves and others are to be blamed, yet not to be denied communion."* Two vendored witnesses and a 12th-century commentator all read it as the document reads it.

**4. §5.4's Fragment VI — see S-7.** The text is right; "pre-Nicene, Eusebius-independent" is right about composition and silent about a Byzantine-florilegium transmission; "strengthens, does not reclassify" is right on the second half and over-claimed on the first; and "inside the very interval Doc_04 calls thin" is **false**.

**5. §6's Cross-Stratum run — CONFIRMED. Reasoning sound; representation of Doc_04 §5 and of the canonical-answers record accurate.** See S-6.

**6. §7's root-cause claim — CONFIRMED AS TO THE SWEEP; but the contrast it draws is wrong (see N-5).** I read `alx.search.unopened-volume-sweep` in full. The `query` field is verbatim as quoted, and it *is* volume-scoped: *"Every vendored volume on cross_world's second-hand-source list for this world - volumes whose principal author this world NAMES while never opening that author's own works."* Four volumes, one opened (`alx.source.vita-antonii-syriac`), three declined with reasons that are, as the document says, good. The `divergence_note` is verbatim. The diagnosis is **fair, not unfair**: the document says up front "It is not a missing gate," credits the declines, and confines its criticism to the granularity and to the health inference. And the health inference *is* backwards for this failure mode — anf06 is opened, so it could never appear on a second-hand list, and the twelve assigned works inside it were structurally invisible. The `2026-08-27` date is in the record's `channel` field ✓.

**7. §8 reason 3's freeze account — CONFIRMED, both halves and the date.** See S-2.

**8. The measurement corrections — CONFIRMED, and one is better than Round 1's.**
- **"Fourteen penitential canons."** ANF prints fifteen (`ix.iv.i`–`ix.iv.xv`); Canon XV is on the Wednesday/Friday fast and Sunday non-kneeling. The corpus map says *"Peter's fourteen penitential canons (306)."* The "fourteen" attribution to "NPNF" resolves to **npnf201**, which reads *"Fourteen Canons, containing detailed directions in regard to the lapsed were drawn up by Peter in 306"* — I found it there and only there. Note for precision (c-10): the NPNF volume that actually *prints* the canons, npnf214, prints fifteen, Canon XV included. The ANF-apparatus point about a "spurious" Canon XI belonging to the Gregory series checks out (endnote 140 at line ~2208).
- **"~3,900 words" of Peter's own canon text — reproducible, and more accurate than the ~4,800 Round 1 asked for.** I extracted `ix.iv` (lines 26588–27731), stripped `<note>` blocks, and summed the fifteen canon-body paragraphs excluding Balsamon/Zonaras: 236+178+169+193+316+107+138+128+676+389+435+204+601+192+94 = **4,056 with Canon XV, 3,962 for the fourteen penitential canons alone**. Round 1's 4,767 was inflated by a 652-word unattributed paragraph after Canon X which is plainly the commentator's ("*this great father and holy martyr*… *in the opinion of this divine father*"), not Peter's. The document's ~3,900 is the better number. It should say that it departs from the figure Round 1 proposed and why (c-8).
- **"~11,300 words"** for the whole section reproduces on a whitespace split with endnotes retained (**11,277**); my token-regex count is 11,120 with endnotes, 10,877 without. Defensible as "~".
- **ANF Elucidation II** is correctly located (`div2 ix.vii`, Elucidation "II." marker precedes the passage) and the strings are verbatim — but the quotation compresses an attribution shift; see c-2.

---

## C. NEW SUBSTANTIAL FINDINGS (Round 2)

### N-1 [SUBSTANTIAL — status claim, S-8 regression] §10 claims an `Open_Gaps_Tracking.md` entry that does not exist
Fully evidenced above. Also creates a direct internal contradiction with the Status line. **Required:** remove the clause, or write the entry and say so accurately (and reconcile the Status line if the entry is written).

### N-2 [SUBSTANTIAL — false claim carrying §5.4's weight] "sitting inside the very interval Doc_04 calls thin"
Peter is bishop 300–311; Doc_04's thin interval is 254–296 and its other "thin" is the mid-horizon Origen–Demetrius instance. Fully evidenced at S-7. The dependent sentence ("T3's evidence is therefore not the 'thin middle, strong late' shape Doc_04 describes") must be restated to the claim the evidence actually supports: **the boundary pole is already active pre-Nicaea, at the front edge of the late horizon.**

### N-3 [SUBSTANTIAL — two quotations truncated at the word that limits them] The Contested rating is temporally scoped, and the document twice presents it as unscoped
Two instances, both cutting the same way, both in service of an argument about a **post-Origen** interval:
- **§4.5** quotes `alx.contested.didaskaleion-institution`'s `concedes` field and stops immediately before *"before Origen's era."*
- **§3.3** says *"Doc_02 Stream 5 rates the teaching tradition's institutional form **Contested**. Confirmed."* Doc_02 line 56 actually reads: *"**Contested** (carried from Doc_01 §1.2) for whether it was a formal institution with a continuous head-succession **before c. 215–230**."*
Neither elision is self-serving in intent — the record's unscoped voice consequence does still bite the three corpus-map notes — but a document whose whole authority is exact re-derivation cannot truncate a source at its own scope limit twice in the same argument.

### N-4 [SUBSTANTIAL — untested route to a classification change] C4 Logos-Centered Unity is asserted, never tested, and this corpus bears on it
§1 asserts "C3, **C4**, C5 remain Supporting." The document then never mentions C4 again except inside the §6 interaction list. Round 1 named this material (its §G item 2) and the revision did not take it up. It is live:
- Doc_04 §3.4 classifies C4 Supporting on the practice-cluster criterion and rates its Cross-Check *"Integrating-center function **Widely Accepted** (all three figures)"* — Clement, Origen, Athanasius.
- Peter's **Fragments II, III, IV and VIII** (`ix.vi.ii`–`iv`, `viii`; lines 27807–27871, 28122) are a **fourth** witness, and an *episcopal*, Origen-independent, Eusebius-independent, pre-Nicene one: *"the Word was made flesh"*; *"Now when Gabriel said, 'The Lord is with thee,' he meant God the Word is with thee"*; *"He was God by nature, and… man by nature"* (III, repeated verbatim at IV, and again at VIII). All verified in the file.

It **does not** move C4 — the Primary/Supporting line is the practice-cluster criterion, which no additional doctrinal witness can cross, and Doc_04 already has C4 at 6/6 PASS. But that is the argument the document owes, and it is exactly the argument it accepted having to make for T3 (§5.4) and for the Cross-Stratum Test (§6) when Round 1 said "the document must show the work, not skip it." **Asserting a classification you have not tested is the defect Round 1's S-6 named.** Either run C4 in §5, or state in §1 which gravities were tested and which were not.

### N-5 [SUBSTANTIAL — the root-cause section mis-describes its own counter-instrument] §7's "work-granular" contrast is not supported by the evidence it cites
§7's argument turns on a contrast: the sweep is volume-granular, but "the partial compensation came from elsewhere… the cross-world corpus assignment, **which is work-granular** and 'observed no record here had opened the volume' for npnf214." The quoted evidence is **volume-granular on its face.** `alx.source.alexandrian-canonical-answers`'s `discovery_channel` reads in full: *"found by the cross-world corpus assignment…, which assigned six npnf214 works to this world and **observed no record here had opened the volume**."* npnf214 was caught because the whole *volume* was unopened — the same trigger the sweep uses. It assigns works; it did not, on this record's own testimony, *check* at work level. This matters because §7 is billed as "the most portfolio-relevant thing in this document": if no existing instrument is work-granular, the remedy §7 proposes is genuinely new rather than an extension of one that already exists, and the recommendation to the project lead reads differently. Restate the contrast to what the record supports.

### N-6 [SUBSTANTIAL — the document's own screen not applied to its own best find] Fragment VI's transmission is unexamined
Evidenced at S-7 new error 2. ANF's own apparatus gives the fragment's provenance as Leontius and John's *Sacra Parallela* via Mai. The Theognostus/Athanasius caveat the document rightly makes mandatory in §5.1 has no counterpart in §5.4.

### N-7 [SUBSTANTIAL — stale count in the headline, introduced by the S-7 fix] "Four verifiable defects… three of them substantial"
§1 line 39 still carries the pre-revision count. §5 now carries **five** items, of which **four** are tagged `[SUBSTANTIAL]` (§5.1, §5.2, §5.3, §5.4) and one is the separate pre-existing `Gravity_Index.xlsx` item (§5.5). §8 is internally consistent with four-substantial; §1 is not. Adding §5.4 without updating the headline count is precisely the propagation failure `cic-build-cycle` warns about ("a fix that lands in the narrative document without the index being updated to match is not a complete fix").

### N-8 [SUBSTANTIAL — Round 1 S-4's second consequence not applied] §8 still counts §5.2 toward "not merely supplemental"
Evidenced at S-4 above.

---

## D. COSMETIC FINDINGS

- **c-1.** Header line 8: *"the revision log is §9."* It is **§11**. §9 is the Recommendation. (Line 527's "§9's Option B" is correct, so this is an isolated stale reference — in the document's own header.)
- **c-2.** §5.3's Elucidation II quotation compresses an attribution shift. *"Like the famous Canonical Epistles of St. Basil, however, these are compilations of canons accepted by the churches of his jurisdiction"* is the American editor **on Peter**; *"they are not written in the form of personal letters, but after the manner of synodical decisions"* is **Dupin on Basil**, quoted after an intervening sentence the ellipsis swallows. The sense the document draws is fair (the editor is making the analogy deliberately), and the elided clause — *"not… the particular opinions of St. Basil, but… the laws of the Church in his time"* — would have helped it. Mark the shift.
- **c-3.** §3.5's *"14 works assigned to Alexandria from anf06"* uses "assigned" in the corpus-map-membership sense; four lines later the same paragraph uses `confidence: assigned` in the field sense (only **8** of the 14 carry it). Disambiguate.
- **c-4.** §3.2 calls npnf214 `div2 17.6` *"a second vendored witness to the same text"* — the corpus map's own phrase — without telling the reader it is **Johnson's ~456-word epitome** (I measured it: fifteen one-or-two-sentence abstracts, Canon I–XV), not a parallel translation of the ~4,000-word original. That is material to §9 Option B's cost: a source record citing only anf06 loses far less than the phrasing implies.
- **c-5.** §3.1's *"a bare grep for `peter` returns two Origen commentary records — the apostle and the Gospel of Peter"* — **neither** hit is the apostle. Both are the same anf09 volume filename inside `edition:` fields (`alx.source.origen-comm-john.md:18`, `alx.source.origen-comm-matthew.md:18`). The conclusion (not the bishop) is right.
- **c-6.** §5.4 says Fragment VI is *"headed in ANF 'From his demonstration that the soul was not pre-existent to the body.'"* That phrase is in ANF's **endnote 2382**, not the heading; the heading is *"Of the Soul and Body."*
- **c-7.** §3.4 keeps the Canonical Epistle "documentary, **first-person**, and contemporaneous" with no pointer to §5.3's Elucidation II qualification (*"not written in the form of personal letters"*), which is 150 lines away. The two survive together but should be cross-referenced where the claim is first made.
- **c-8.** The ~3,900 figure silently departs from the ~4,800 Round 1 asked for while §3.4 says the corrections were "both accepted." The document's number is the better one (Round 1's heuristic swept in a 652-word commentator paragraph). Say so in a clause.
- **c-9.** §6 never names Doc_04 §5's own two held-open majority-organizing candidates (*communal-liturgical belonging*, *martyrdom-as-formation*), so a reader cannot see which named hole the negative result applies to. §5.3 likewise does not report Round 1's point that the Interaction-Matrix gap is systemic (roughly 13 of 36 pairs stated) — which strengthens the T1↔T4 finding rather than weakening it. §5.5 still omits that `Doc_04_Round2_Review.md` and `Doc_04_Round3_Review.md` both quote cell values from the workbook that does not exist (I re-confirmed: `find -iname "*Gravity_Index*"` returns only World #1's file and a PAHC generator script; `Doc_04_Round2_Review.md` lines 18, 31, 55, 63–67 quote its sheets). That belongs in front of the project lead alongside §5.5.
- **c-10.** Four of Round 1's eight cosmetics were **not applied and their decline is not disclosed** in §11 (which lists only four applied): **C-5** — §9 Option C still calls §5.1 *"a plain factual error"* after Round 1 showed the Doc_04 sentence is a hedged collective; **C-6** — §5.3 still says *"the bishop rather than confessor-prestige deciding who counts as a confessor,"* though Canon XIV admits men *"on the testimony of the rest of their brethren"* (verbatim, verified) and Fragment I's grievance is that Meletius disregards *"the letter of the most holy bishops and martyrs"* (verbatim) — the bishop adjudicates *using* confessor testimony as much as against it; **C-7** — §5.3 still folds Canon IV into *"Canons I–V — a graded penitential scale,"* though Canon IV is the refusal of the scale (*"To those who are altogether reprobate, and unrepentant, who possess the Ethiopian's unchanging skin"*); **C-8** — "PR #133" and the discovery pass remain unverifiable from this repository (the only occurrences of "#133" anywhere are this document's §Scope line and Round 1's flag of it). Declining a cosmetic is legitimate; declining it silently while §11 says "Cosmetics applied" is not.

---

## E. THE HEADLINE, RE-TESTED

**"NOT structural" is still correct.** I ran every route, including the two the document has not.

- **C5 Persistence.** Cannot flip. The disproof is `alx.figure.didymus` — a school head to 398 already inside the store, alongside a standing PARTIAL. Two mid-interval teachers cannot move a centre-of-gravity claim that already tolerates him. §5.2 has this right.
- **T1 pole separation.** Cannot be extended by this material, and the document's inversion is correct: a single man holding both poles is Doc_04 §3.6's named disqualifying case (*"not a polarity within one person"* — verbatim at line 132).
- **T4.** Peter's canons are juridical throughout; they contain no martyr's interior. Inferential-Thin on the interior stands. What moves is the *description* of the evidence base, which is a §5-class finding, not a classification.
- **T3.** Fragment VI is real and relevant, and even corrected (N-2, N-6) it strengthens rather than reclassifies. T3's poles are untouched.
- **Cross-Stratum / OG-4.** Fails, for the reason the world's own record already supplies. §6 is right.
- **C4 — the route still untested (N-4).** Peter's episcopal Logos fragments are the strongest unexamined item in this corpus. I ran it: **it also fails**, because C4's Supporting classification rests on the practice-cluster criterion, not on witness count, and Doc_04 already has C4 passing all six tests. So the headline survives — but the document asserts C4 without testing it, and that assertion is currently unearned.
- **C3.** §5.2 offers Theognostus frag. III as "texture, explicitly not a classification argument" and then asserts "it reclassifies nothing" without running C3's Dependency test — the test that made C3 Supporting. A non-Origen instance is exactly the kind of datum that bears on an Origen-dependency screen. The assertion is almost certainly right (one Athanasius-mediated fragment cannot make an explanatory framework produce a practice-cluster), but it is an assertion.

**Net: the conclusion holds. One named route (C4) and one half-route (C3) are still asserted rather than shown.**

---

## F. DISCIPLINE COMPLIANCE

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS.** Header ("escalated to the project lead — not self-disposed"), §8's four reasons, §9's grounded options and reserved open question, §10's negative inventory. I verified the inventory's substance independently: `records/alx/` unchanged, no corpus-map edit, no `Gravity_Index.xlsx` created, `records/worlds.yaml` still pins `packages/alx/2026-09-04T16-41-49Z`, no Doc_01–Doc_09 file touched. Escalation categories 2 and 4 are correctly identified against `cic-build-cycle` SKILL.md lines 57 and 59. |
| No unverifiable attribution to the project lead | **PASS, and carefully done.** §3.2 says the npnf214 row was "split out on 2026-08-26" without attributing the ruling to Mark, though the corpus map does; §8 cites the S6.2 declaration by date without asserting a project-lead act; §10 states "No claim that any of this was seen or approved by the project lead." This meets SKILL.md line 81. |
| Claims no status it has not earned | **FAIL — N-1.** The header is repaired; §10 is not. "Files added by this pass… an `Open_Gaps_Tracking.md` entry" is a claimed artefact that does not exist. |
| Declines to pre-assign an OG number | **PASS.** `grep "OG-"` returns only genuine OG-4 references and §11's account of removing the fabricated OG-6. |
| Grounded-options recommendation format | **PASS.** Three options with cost, precedent and a stated reason; a named recommendation; a portfolio-level item separated; an open question reserved to the project lead rather than pre-answered. |
| Accurate self-report of its own revision | **FAIL — §11 overstates.** One of eight substantial findings is not resolved (S-8/N-1); two repairs introduced new errors (N-2, N-3); the cosmetic list omits four declined items (c-10); and the headline count was not propagated (N-7). |

---

## G. SUMMARY

- **Overall verdict: SUBSTANTIAL REVISION REQUIRED.**
- **Headline: CORRECT and re-confirmed.** "Not structural" survives C5, T1, T3, T4, the Cross-Stratum Test, and the C4 route the document has not run. The disposition (§9 Option B, escalated) should stand, expanded to cover the C4 evidential-base item (N-4) and the corrected §5.4 claim (N-2, N-6).
- **Round 1's eight: 4 RESOLVED** (S-1, S-2, S-3, S-6) · **3 PARTIALLY RESOLVED, two of them with new errors** (S-4; S-5 → N-3; S-7 → N-2, N-6) · **1 NOT RESOLVED, replaced by a fresh instance of itself** (S-8 → N-1).
- **New substantial: 8** — N-1 false `Open_Gaps` entry claim; N-2 "inside the thin interval"; N-3 twice-truncated scope limits; N-4 C4 untested; N-5 "work-granular" contrast unsupported; N-6 Fragment VI's transmission unscreened; N-7 stale headline count; N-8 §5.2 still counted toward "not merely supplemental."
- **New cosmetic: 10** (c-1 … c-10).
- **What the revision got right and must not lose.** Every line locus in §2's table landed exactly where stated (`vi.v` 15787, `vi.vi` 15957, `div1 ix` 25658, `ix.ii` 25667, `ix.iv` 26588, `ix.vi` 27779, `ix.vii` 28157, `ix.iv.ix` 27036) — this is the cleanest citation hygiene I have checked in this build. Canon IX is the right Canon IX, quoted verbatim, and its characterisation is corroborated by both Balsamon and the npnf214 epitome. The word-count correction is better than the one Round 1 asked for. The freeze split is exact, including the 2026-08-01 parenthetical. The Cross-Stratum run is a genuine, correctly-reasoned negative result on the build's highest-stakes item. The corpus-map counts are exactly right and Alexander is correctly named-and-not-pursued. The root-cause diagnosis of the sweep is fair to the sweep and portfolio-relevant. The refusal to fill the martyr's interior, the refusal to self-dispose, and the refusal to pre-assign an OG number all hold.

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires. A qualified subject-matter reviewer on the Melitian chronology, Peter's anthropology and the transmission history of the Sacra Parallela fragments would be the accountable test of §4, §5.3 and §5.4.)*
