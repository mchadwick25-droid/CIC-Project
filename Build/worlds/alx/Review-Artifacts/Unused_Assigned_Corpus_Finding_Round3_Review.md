# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 3 Independent Adversarial Review

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md` (Round 3 draft, revised after Rounds 1 and 2)
Reviewer role: independent adversarial. Did not author the finding document, either prior review artifact, the discovery pass, or any Doc_04 round. Brief: **do not trust §11.** For each of Round 2's eight substantial findings, verify independently that the fix landed *in the document body*, is correct, and introduced no new error; audit the newly written OG-6 ledger entry against what is on disk; then re-test the headline including the routes still named-but-not-run.
Method: `Open_Gaps_Tracking.md` read in full and its heading structure enumerated; `git log` / `git show --stat` run against all three commits of this pass (`b50302d`, `48ca471`, `09c23d6`) and `git diff 48ca471 09c23d6` read line by line so that §11's claims could be checked against the actual patch rather than against its own description; `cic/corpus-map/alexandria-catechetical.yaml` re-parsed with PyYAML (65 work rows, 14 `anf06` rows enumerated by `source_file`); `anf06…xml`, `npnf201…xml`, `npnf214…xml` tag-stripped and word-counted with independent scripts, and every `div2`/`div3` locus in §2's table re-opened at the stated line; all fifteen ANF canons extracted individually and every quoted string matched; ANF's provenance endnote read for **each** of the doctrinal fragments the document relies on, not only Fragment VI; `records/alx/` walked (192 files, 14 type directories) and every cited record read in full; `Doc_04`, `Doc_02`, `S6.2_ALX_FREEZE_DECLARATION.md`, `records/worlds.yaml` opened directly.
Date: 2026-09-09

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**The headline is correct for the third time.** "This material is **not structural**" survives. I re-ran every route the prior rounds ran, ran the C3 Dependency half-route the document names and declines, ran T2, and ran one route no round has named — whether this corpus generates a *candidate* Doc_04's §1 generation step never generated. Nothing moves. See §E.

**And — unlike Round 2 — §11 is substantially honest.** I checked the patch, not the prose. All eight of Round 2's substantial findings produced a real edit in the body; all five cosmetics §11 claims are on disk; the OG-6 entry §10 asserts genuinely exists (`Open_Gaps_Tracking.md` lines 247–299, written in commit `09c23d6`, +56 lines), and §10's disclosure of the earlier false claim is accurate, complete, and does not soften what happened. Six of the eight are cleanly resolved. That is a real improvement and it should be said plainly.

**But two things are still wrong and one new artifact is defective.** The screen this document makes mandatory for everyone else is applied to exactly one item in it — and the section added *at Round 2's direction to fix that very failure* is the section that omits it. One of the three defects the document counts as produced by this corpus rests on reading a scope-limited clause at a wider scope than either source writes it at — the same defect class Round 2 named twice as N-3 and once as N-2. And the newly written OG-6 entry, the one project-lead-facing artifact this pass adds, drops one of the four defects it escalates.

Counts this round: **4 substantial, 12 cosmetic.** The disposition (§9 Option B, escalated, not self-disposed) remains sound and should stand.

---

## A. ROUND 2's EIGHT — VERIFIED INDEPENDENTLY

I did not read §11 as evidence. Each row was checked against the document body, the patch, and the primary source.

| Round 2 | Subject | Round 3 status |
|---|---|---|
| 1 | Phantom `Open_Gaps_Tracking.md` entry | **RESOLVED** — but the new entry carries its own defect (N3-1) |
| 2 | §5.4 "inside the very interval Doc_04 calls thin" | **RESOLVED** |
| 3 | Two truncations at a scope limit (§4.5, §3.3) | **RESOLVED** |
| 4 | C4 asserted, never tested | **PARTIALLY RESOLVED — FIX INTRODUCED NEW ERROR** (N3-2, N3-4) |
| 5 | §7's "work-granular" contrast unsupported | **RESOLVED** |
| 6 | Fragment VI transmission unscreened | **RESOLVED for Fragment VI only** (see N3-2) |
| 7 | §1's defect count stale | **RESOLVED** |
| 8 | §8 still counted §5.2 toward "not merely supplemental" | **RESOLVED** |

### 1 — **RESOLVED.** The entry exists; the disclosure is honest.

`git show --stat 09c23d6` touches three files, one of them `Open_Gaps_Tracking.md` (+56 lines); `git status --porcelain` is clean, so what I read is what is committed. The entry is at **`Open_Gaps_Tracking.md` lines 247–299**, headed *"OG-6. Vendored-but-unused assigned corpus (anf06) — verified finding, escalated 2026-09-09."* I checked its substance line by line against the document and against disk, not against the document's summary of itself:

- *"NOT structural… no six-test verdict flips; the Article 21 cross-stratum substitute is unchanged"* — matches §1 and §6. ✓
- *"the whole `anf06 div1 ix` division nowhere links Peter to the school"* — I re-ran the search over `div1 ix` (lines 25658–28332): five hits for `school`/`catechet`, **all** in the American editor's Introductory Notice (lines 25688–25704) about Alexandria and Antioch as centres of learning. None attaches Peter. ✓
- *"HE VII.32: **Achillas** was principal"* — `npnf201…xml` line 43204, Eusebius's own text: *"He was placed over the school of the sacred faith."* ✓
- *"He appears **0 times** in the vendored Eusebius"* — `grep -c "Theognostus"` on `npnf201…xml` returns **0.** ✓
- *"14 anf06 works assigned, only 2 opened"* — my own parse: 14 rows with `source_file: anf06…`; `grep -rl anf06 records/alx/` returns exactly two **source** records (`gregory-address-to-origen`, `dionysius-extant-fragments`). ✓
- *"Alexander of Alexandria's Epistles… `assigned` with zero records"* — the row is real (`div2 10.3`, `confidence: assigned`); `grep -ril alexander records/alx/` returns nothing. ✓ (`div1 x` in anf06 is headed *"Alexander of Alexandria"* at line 28332.)
- *"`Gravity_Index.xlsx`… is not in the repository"* — `find -iname "*Gravity_Index*"` returns only World #1's file and a PAHC generator script. ✓
- *"Status: OPEN — awaiting project-lead disposition… Nothing was changed"* — verified: `records/alx/` untouched, no corpus-map edit, `records/worlds.yaml` still pins `packages/alx/2026-09-04T16-41-49Z`, no Doc_01–Doc_09 file in any of the three commits. ✓
- The two-freezes paragraph is exact: `S6.2_ALX_FREEZE_DECLARATION.md` line 3 `**Date:** 2026-07-28`, and *"the world is NOT frozen"* at `Open_Gaps_Tracking.md` line 145. ✓

**§10's disclosure (lines 606–614) is honest and complete.** It names the defect, names who caught it and how (`git show --stat`), names the class it belongs to, quotes the rule it broke, and states that item 4 is why the Status line had to be rescoped. It does not minimise and it does not quietly repair. The Status line (lines 18–21) is correspondingly rescoped to construction documents, `records/alx/`, the corpus map and the compiled package, and now says outright *"The only world-build file modified is `Open_Gaps_Tracking.md`."* The Round 2 contradiction is gone.

**What is wrong with the entry itself is N3-1 below**, and it does not undo this verdict: the fix Round 2 demanded landed.

### 2 — **RESOLVED.**

`Doc_04` line 39 gives the inter-phase interval as *"c. 254–296"*; line 38 gives *"Late / post-Nicene — dominated by Athanasius and Didymus (c. 296–400)."* §5.4(a) (lines 352–358) now states exactly that, withdraws the false claim in its own voice, and replaces it with the narrower one. I checked the replacement against `Doc_04` §3.6 T3 (line 136), which reads verbatim: *"the mid-horizon instance (Origen–Demetrius) is HIGH-risk and thin; the confirmation is deliberately **shifted to the late-horizon evidence** (the homoousian boundary, the Origenist controversy) which is well-attested and *independent of Eusebius*."* The document quotes it correctly and draws the right consequence: Peter (bp. 300–311) is pre-Nicene and pre-homoousian, so the boundary pole is active before the evidence T3 rests on; it moves the start of the chain, it does not fill the 254–296 gap. The dependent over-claim Round 2 killed ("T3's evidence is therefore not the 'thin middle, strong late' shape") is gone from the body. One imprecision in the replacement, cosmetic only: see c-10.

### 3 — **RESOLVED, and §4.5 has not over-corrected.**

Both restorations are verbatim against source:
- `alx.contested.didaskaleion-institution` line 29, `concedes`: *"…What is contested is its INSTITUTIONAL form and continuity **before Origen's era.** The world is therefore anchored on the tradition, not the institution."* §4.5 (lines 197–202) now carries the limit and says in its own voice that the first draft dropped it. ✓
- `Doc_02` line 56, Stream 5: *"**Contested** (carried from Doc_01 §1.2) for whether it was a *formal institution with a continuous head-succession* **before c. 215–230**."* §3.3 (lines 115–119) now carries it. ✓

**On the brief's question — is §4.5 now saying nothing?** No. It has moved from a false charge to a narrower true one, and the narrower one is still testable and still lands. I tested it. The record's **voice consequence** (record body, unscoped by any date): *"the Representative may speak of teachers and the teaching tradition freely, but never of 'the School' as a documented continuous institution."* And all three corpus-map notes do assert exactly that framing — I read them: Peter, *"the bishop-martyr who also headed the catechetical school"*; Pierus, *"Head of the catechetical school"*; Theognostus, *"Head of the catechetical school after Dionysius."* Against sources that do not carry it (§4.1 verified above; §4.2's `npnf201` editorial note verbatim at lines 43062–43075; §4.3's ANF notice verbatim — *"Dodwell and others are of opinion that by this term* exegete *is meant the presidency of the Catechetical school"*). A charge of overstatement-against-their-own-sources in tension with a live voice rule is a smaller charge than "contradicts a Contested finding," and it is the one the evidence supports. That is a correct narrowing, not an evacuation.

### 4 — **PARTIALLY RESOLVED; the repair introduced a new error.**

The good half is real. New **§6.1** (lines 427–450) runs C4, and its representation of Doc_04 is accurate: `Doc_04` line 120 does classify C4 Supporting on the practice-cluster criterion despite all six tests passing, and line 121 does read *"Integrating-center function **Widely Accepted** (all three figures)."* The reasoning is right: witness count cannot cross a criterion that is about practice-clusters, so a fourth witness raises nothing. **C4 remains Supporting.** I re-ran it and agree.

**The new error is that §6.1 exempts its own evidence from the screen §5.4 was just forced to apply.** I read ANF's provenance note for every fragment §6.1 names, not just Fragment VI:

| Fragment | ANF's own provenance note | Date of the witness |
|---|---|---|
| II (On the Godhead) | *"from the Acts of the Council of Ephesus, i. and vii. 2.—Galland."* | 431 |
| III (On the Advent) | *"Apud Leontium Byzant., lib. i., contra Nestor. et Eutych."* | Leontius of Byzantium, 6th c. |
| IV (On the Sojourning) | *"Ex Leontio Hierosolymitano, contra Monophysitas, Ap. Mai."* | Leontius of Jerusalem, 6th c. |
| VIII (On St. Matthew) | *"From the Treatise of the Emperor Justinian against the Monophysites."* | Justinian, 6th c. |

Every one of the four reaches this corpus through fifth- or sixth-century **christological-controversy polemic** — the selection bias runs directly toward two-natures language, which is precisely the language §6.1 quotes. §6.1 calls them *"independent of both Origen and Eusebius"* and stops there. That is true and beside the point, exactly as Round 2 said of "pre-Nicene" for Fragment VI: it is a statement about composition, not about the witness. Five paragraphs earlier §5.4(b) says that exempting this document's own best find from its own discipline *"would be exactly the failure mode it exists to catch."* Fully evidenced at **N3-2**.

**A second, independent problem with the same passage.** §6.1 presents *"Fragments II, III, IV and VIII"* as *"a sustained Logos witness"* and Peter as *"a **fourth** witness."* Read against the text, III, IV and VIII are **one saying in three witnesses**, not three fragments: III, on Luke 22:48, ends *"He was God by nature, and… man by nature"*; IV is that sentence alone (*"Both therefore is proved, that he was God by nature, and was made man by nature"*); VIII is Justinian quoting the same Matthew/Luke betrayal-kiss exposition with the same clause. The substantive corpus here is **two** items — Fragment II from the Ephesus acts, and one homiletic sentence — not four. Round 2 noticed the repetition in a parenthesis while running the route itself; the document adopted the list without it.

Neither error changes C4's verdict — a weaker witness moves C4 even less — but the section's own framing ("on its face the strongest corroboration in this corpus") is unearned as written.

### 5 — **RESOLVED, and the correction is exact.**

`alx.source.alexandrian-canonical-answers`'s `discovery_channel` reads in full: *"found by the cross-world corpus assignment…, which assigned six npnf214 works to this world and **observed no record here had opened the volume**."* §7 (lines 476–482) now says precisely this, withdraws "work-granular" in its own voice, and gives the right reason npnf214 was caught (no record against that volume at all). The recommendation now rests on a claim I verified independently: the corpus map **is** work-granular data — every row carries `work`, `locus` and `confidence`, and nothing on disk diffs it against the works records actually open. `alx.search.unopened-volume-sweep`'s `query` and `divergence_note` are still verbatim as quoted, and the sweep's date (`channel`: 2026-08-27) matches the canonical-answers record's own verification date, so "the same day" holds.

### 6 — **RESOLVED for Fragment VI, and accurate to ANF's own note.**

ANF endnote 2382 (`anf06…xml` line 28086, inside `div3 id="ix.vi.vi"`) reads: *"Ex Leontii et Joannis **Rer. Sacr.**, lib. ii. Apud Mai, Script. Vet., tom. vii. p. 85. From his demonstration that the soul was not pre-existent to the body."* §5.4(b) quotes the first clause exactly. The identification — *Sacra Parallela*, 7th–8th-c. florilegium — is the document's own gloss, presented after an em-dash as its own gloss and not attributed to ANF. That is honest and the identification is standard. The screen's consequence ("cannot be carried at better than the confidence that transmission supports") is correctly stated and correctly does not disturb T3's classification. **The fix landed exactly where Round 2 asked.** It simply was not carried one section forward — N3-2.

### 7 — **RESOLVED.**

§1 (lines 46–51) now reads *"Five defects are recorded in §5, of which **three** are produced by this unused corpus and are substantial… §5.1, §5.3 and §5.4,"* with §5.2 and §5.5 named as not counted. I counted §5 myself: five items, four tagged `[SUBSTANTIAL]`, one tagged as a separate pre-existing defect. §1, §5 and §8 are now mutually consistent, and the wording is careful enough not to claim that only three items are substantial.

### 8 — **RESOLVED.**

§8 (lines 504–510) no longer lists §5.2 among the grounds for "not merely supplemental." It now names three (§5.1, §5.3, §5.4) and explicitly sets §5.2 and §5.5 aside as *"pre-existing defects found along the way… not evidence for the value of drawing on it."* Round 1's S-4 second consequence is finally applied.

---

## B. §11's OWN ACCURACY — CHECKED AGAINST THE PATCH

Round 2 found §11 overstating. This one does not, with one exception.

I diffed `48ca471..09c23d6` and matched each §11 claim to the hunk that implements it. All eight substantial items produced a real body edit. All five claimed cosmetics are on disk: the header cross-reference now reads *"Revision log: §11"* (line 5, was "§9"); the Elucidation II attribution shift is now stated explicitly and correctly (lines 317–321 — I verified against `div2 ix.vii`: *"Like the famous Canonical Epistles of St. Basil, however, these are compilations of canons accepted by the churches of his jurisdiction"* is the American editor on Peter, and *"not to be considered as the particular opinions of St. Basil… after the manner of synodical decisions"* is Dupin on Basil, verbatim, with the intervening sentence honestly elided); the npnf214 epitome description is not only present but **numerically right** — I extracted `div2 xvii.vi` (lines 43159–43238) and measured **551 words with endnotes, 456 without**, exactly the two figures §3.2 gives, and the content is fifteen one-or-two-sentence abstracts, i.e. an epitome; the Status line is rescoped; and the two stale "§7" cross-references (in §3.2 and §6) are corrected to "§9."

§11's closing paragraph on the four silently-declined Round 1 cosmetics is the right disposition: it records the fact rather than repairing it by assertion, and the log now claims only what landed. Good.

**The exception:** §11 item 4 propagates §6.1's overstatement verbatim — *"a fourth, episcopal, Origen- and Eusebius-independent Logos witness."* Same two problems as N3-2: no transmission screen, and III/IV/VIII are one saying. §11 does not overstate *what landed*; it does carry forward one substantive error from the body it is summarising.

---

## C. NEW SUBSTANTIAL FINDINGS (Round 3)

### N3-1 [SUBSTANTIAL — the ledger entry this pass added is inaccurate against the document it summarises] OG-6 escalates "four real defects" and one of the four is not one of the document's

`Open_Gaps_Tracking.md` line 266 opens *"**Four real defects, escalated rather than self-disposed** (`cic-build-cycle` categories 4 and 2)"* and numbers them: (1) Doc_04 §0's Theognostus/Eusebius attribution = §5.1; (2) `learning-formation` vs `didymus` = §5.2, correctly labelled pre-existing; (3) T4's "hagiography and martyrology only" = §5.3; (4) Doc_04 §6's missing T1↔T4 cell — which in the document is **not a fourth defect at all**, it is the closing sub-argument *inside* §5.3.

**§5.4 — Peter's Fragment VI and T3 — appears nowhere in the enumeration.** It is one of the three defects §1 and §8 say are produced by this corpus, and it is the one Round 1 had to force into existence. Yet at line 290 the same entry recommends *"scoped reopen of Doc_04 §5.1–§5.4"* — a project lead reading the ledger alone is asked to authorise a reopen covering a defect the ledger never states. §5.5 is likewise demoted from the numbered list into an "Also found" paragraph while §1 counts it among the five.

This is not a cosmetic mismatch. The ledger is the durable, project-lead-facing artifact this pass exists to leave behind, and it drops one of the items it escalates. **Required:** renumber the entry to the document's own set — §5.1, §5.3, §5.4 as produced by the corpus; §5.2 and §5.5 as pre-existing; the T1↔T4 cell as part of §5.3 — or state a different, explicit basis for a four-item list.

### N3-2 [SUBSTANTIAL — the screen this document makes mandatory is applied to exactly one item in it] Transmission and author-gravity screening stops at Fragment VI

§5.1 (lines 240–244) establishes the rule in the document's strongest terms: *"Trading a HIGH Eusebius screen for an unexamined Athanasius mediation would be no gain."* §5.4(b) applies it to Fragment VI and says exempting the document's own best find *"would be exactly the failure mode it exists to catch."* It is then not applied anywhere else. Three instances:

1. **§6.1's C4 evidence.** Fragments II, III, IV, VIII all reach ANF through 5th–6th-c. christological polemic (Ephesus acts; Leontius of Byzantium; Leontius of Jerusalem; Justinian — table in A/4 above, each verified in the file). §6.1 says "independent of both Origen and Eusebius" and screens nothing further. This is the section added *to repair* Round 2's N-4, adjacent to the section added to repair Round 2's N-6.
2. **§6.1's witness count.** III, IV and VIII are one homiletic sentence in three quotations, so "a fourth witness" rests on effectively two items.
3. **§5.2's Theognostus frag. III**, offered as *"C3 Divine Pedagogy vocabulary in a **non-Origen voice** from the gap interval."* The Athanasius mediation is screened; the authorial dependence is not. ANF's own notice on Theognostus says: *"That he was a disciple of Origen, or at least a devoted student of his works, is clear from Photius"*, and the corpus-map note calls the *Hypotyposes* fragments *"the school's own teaching, **Origenian in cast**."* Under Doc_04's **Discipline One — the Origen SYSTEMIC screen** (`Doc_04` line 46), which is the governing discipline of the entire document being audited, an Origen disciple's fragment is not Origen-independent corroboration. The consequence here is nil — §5.2 flags it as texture and not a classification argument — but the phrase "non-Origen voice" is the whole of its claimed corroborative value.

None of the three changes a classification; each weakens a claim the document makes for its own evidence. **Required:** apply the §5.1 screen to §6.1 and to §5.2's frag. III in the same terms it is applied to Fragment VI, and correct the witness count.

### N3-3 [SUBSTANTIAL — a scope-limited clause attacked at a wider scope] §5.3's "contradicted" charge is not the charge the evidence supports

§5.3's finding is headed *"T4's evidence base is described as narrower than it is,"* and its charge is that *"'hagiography and martyrology only', as a description of **the evidence this world holds on the martyrdom pole**, is contradicted by its own assigned corpus."*

Neither locus makes that claim. In both, the phrase is governed by a subject the document itself quotes correctly and then widens:

- `alx.gravity.martyrdom-contemplative-tension`, `description`: *"Martyrdom is the one confirmed formation mode NOT limited to the literate stratum… but **its interior** is preserved in hagiography and martyrology only (Inferential-Thin)."*
- `Doc_04` line 137, T4: *"martyrdom is the one confirmed formation mode not limited to the literate stratum — but **its interior** is Tier-3 hagiography / Coptic martyrology, held at Inferential-Thin."*

§5.3 concedes in its next breath that *"the Inferential-Thin verdict on the martyr's interior is correct and stands"* — which is the whole of what either source asserts. There is therefore no contradiction to correct. This is structurally the same defect as Round 2's N-2 (a claim tested against a wider interval than Doc_04 wrote) and N-3 (two quotations cut at their scope limit): the document is again engaging a source claim at a scope its author did not use.

**What genuinely survives is worth keeping, and is a different finding.** The record's `manifestations` list — Leonides (*HE* VI.1–2), Origen under Decius (*HE* VI.39), Dionysius's persecution letters, and the contemplative pole — contains **no documentary, non-hagiographic witness on the martyrdom pole**, and Peter's canons are exactly that. The Canon IX–XIV material is real and I re-verified every quoted string (Canon IX at `anf06…xml` line 27036: *"as it were from sleep, themselves leap forth upon a contest"*; *"take no heed unto His words"*; *"delivered not up Himself"*; *"they will deliver you up, and not, ye shall deliver up yourselves"* — all verbatim; Canon X's *"left destitute the flock of the Lord"*; Canon XIII's *"not at all to be blamed"*; Canon XIV's *"the thrice-blessed martyrs have written to me"*; Fragment I's *"has ordained in the prison several unto himself"*). So the finding is an **omission** in T4's evidence inventory, not a contradiction in its characterisation.

**Required:** restate §5.3's charge as an omission; and change §9 Option B's remedy from *"correct T4's 'hagiography and martyrology only'"* (line 554–555) — which as written asks the project lead to correct a sentence that is not wrong — to "add the documentary witness to T4's manifestations." §8 line 541 needs the same adjustment.

### N3-4 [SUBSTANTIAL — unearned completeness claim] "§6.1 C4 Logos-Centered Unity — **the last untested route**"

The heading is contradicted by its own section. §6.1's closing paragraph (lines 446–450) names C3's Dependency verdict as *"a half-route named and not run."* A section cannot be the last untested route and simultaneously name an untested route.

It is also contradicted by a route no round has named. Every route run to date — C5 Persistence, T1 pole separation, T3, T4, C4, C3, Cross-Stratum — asks whether the corpus **reclassifies an existing gravity**. None asks whether it should have **generated a candidate**. `Doc_04` §1 (line 52) generates candidates from *"elements recurring **across multiple Doc_02 streams**."* Penitential-reintegrative discipline recurs in `Doc_02` Stream 3 (*"fasting, vigils, penitential practice"*), Stream 7 (*"discipline and the reintegration of the lapsed"*) and Stream 8, is attested by Dionysius, Peter (306), Timothy and Theophilus, and — unlike C4 — has an actual practice-cluster. It is generable on Doc_04's own rule and it is not in the §1 candidate table or the §2 not-advanced list. I ran it; see §E. It fails, but the document should not claim its route inventory is closed while a generation-step route is unexamined.

**Required:** retitle §6.1 (it is not the last untested route), and either name the generation-step route and decline it explicitly, or state in §1 which routes were run and which were not.

---

## D. COSMETIC FINDINGS

- **c-1.** §6.1 misquotes `Doc_04` line 120 twice in one sentence: it prints *"the theological ***centre***"* where the source reads **"center"**, and truncates *"…makes the other gravities cohere"* mid-clause (the source continues *"into one ecology rather than four activities"*) without an ellipsis. Small, but this document's authority is exact re-derivation.
- **c-2.** §3.1 (line 92) still says a bare grep for `peter` *"returns two Origen commentary records — the apostle and the *Gospel of Peter*."* **Neither** hit is either thing: both are the anf09 volume filename inside `edition:` fields (`alx.source.origen-comm-john.md:18`, `alx.source.origen-comm-matthew.md:18`). Round 2 c-5; unrepaired at Round 3, in a control note offered as evidence of rigour.
- **c-3.** §5.4 (line 346) still calls *"From his demonstration that the soul was not pre-existent to the body"* a heading. It is inside **endnote 2382**; the heading is *"Of the Soul and Body."* Round 2 c-6; half-repaired (the real heading was added) and half not.
- **c-4.** §5.3 still folds Canon IV into *"Canons I–V — a graded penitential scale."* Canon IV is the **refusal** of the scale: *"To those who are altogether reprobate, and unrepentant, who possess the Ethiopian's unchanging skin…"* Round 2 c-7; unrepaired.
- **c-5.** §5.3's *"Fragment I is confessor-prestige asserting ordaining authority against the office"* over-reads the fragment. Peter's stated grievances are that Meletius *"is not contented with the letter of the most holy bishops and martyrs"*, is *"invading my parish"*, and seeks *"pre-eminence"* — a rival **bishop's** jurisdictional encroachment, with confessor testimony on Peter's side of the argument, not against it. Round 2 c-6, extended; unrepaired.
- **c-6.** OG-6 is entered as a `##` heading (`Open_Gaps_Tracking.md` line 247) where **every** other OG entry in the file is `###` (lines 77, 93, 104, 207, 240). It reads as a new top-level section rather than a sixth ledger item. It also cites Round 2 as *"(SUBSTANTIAL, 8 new)"* where the finding document's own header gives 8 substantial + 10 cosmetic.
- **c-7.** §2's table says `Doc_04` was *"read in full (all 9 sections)."* `Doc_04` has ten numbered sections, §0–§9 — and §0 is the one §5.1 turns on.
- **c-8.** §3.5's *"14 works assigned to Alexandria from anf06"* uses "assigned" in the membership sense; three lines later `confidence: assigned` is used in the field sense, where only **8** of the 14 carry it (I enumerated: `10.3`, `4.4`, `4.3`, the Gregory *Oration*, `9.6`, `9.4`, `6.6`, `6.5`). Round 2 c-3; unrepaired.
- **c-9.** §6.1 is filed as a subsection of §6, *"The Article 21 substitute (Cross-Stratum Test),"* which it has nothing to do with — a reader (or the OG-6 entry, which gives no locus) cannot find the C4 test where the taxonomy says it should be. Relatedly, §6 still does not name `Doc_04` §5's own two held-open majority-organizing candidates (*communal-liturgical belonging*, *martyrdom-as-formation*, line 182), so the negative result is not attached to the hole it fails to fill. Round 2 c-9; unrepaired.
- **c-10.** *"roughly a quarter-century earlier than the evidence Doc_04 actually rests T3 on"* is the outer edge of the range (Nicaea 325 less Peter 300–311 = 14–25 years), and is a large understatement against the second element of the very phrase it measures itself by — the Origenist controversy, which is later still. "Fourteen to twenty-five years before Nicaea" would be exact and would cost nothing.
- **c-11.** §9 Option C still calls §5.1 *"a plain factual error"* though the `Doc_04` §0 sentence is a hedged collective (*"the post-Origen teachers (Heraclas, Theognostus)… reaching us **largely** through Eusebius"*) that is true of Heraclas and false only of Theognostus. Round 1 C-5 / Round 2 c-10; unrepaired.
- **c-12.** §3.4's *"Canon XI is additionally marked in ANF's own apparatus as disputed in the parallel Gregory series; Peter's Canon XI is not so marked"* has no clear subject in its first clause. The point (Gregory's XI is flagged spurious, Peter's is not) is correct; the sentence does not say it.

---

## E. THE HEADLINE, RE-TESTED — AND THE C3 DEPENDENCY RUN

**"NOT structural" is correct.** Third round, third confirmation, and this time I looked for a route outside the frame the prior rounds shared.

**C3 Dependency — run, at the brief's direction.** `Doc_04` §3.3 (line 112) makes C3 Supporting on Dependency: *"removed while C1 and C2 remain, the practices persist but lose their explanatory ground — it is a meta-framework… not an independent organizing force."* Run against this corpus:

- **Theognostus frag. III** is genuine Divine Pedagogy vocabulary and I verified it verbatim (*"the Saviour converses with those not yet able to receive what is perfect, condescending to their littleness, while the Holy Spirit communes with the perfected… the Son condescends to the imperfect, while the Spirit is the seal of the perfected"*, `anf06…xml` `div2 vi.v`, transmitted *"From Athanasius, as above"*). It generates **no practice**. Remove C3 and what is lost is the explanation of the Saviour/Spirit condescension, not any practice — the Dependency test returns the same answer it already returned.
- **It is also weaker corroboration than the document says**, for the reason at N3-2(3): Theognostus is an Origen disciple whose fragments the corpus map itself calls "Origenian in cast," so under Doc_04's own Discipline One he cannot lift the Origen-concentration screen at all. On the SYSTEMIC screen this datum is close to inert.
- **Peter's canons cut the same way and harder.** They are the only substantial practice-cluster document in this corpus, and they ground themselves on episcopal authority and scriptural precedent (Matt. 26; Phil. 1:23–24; Acts 19), not on a "God teaches through suffering" framework. Remove Divine Pedagogy and the canons stand untouched. The new material therefore **confirms** C3 Supporting rather than pressuring it.

**Result: C3's Dependency verdict is unchanged. C3 remains Supporting.** The document's asserted reasoning was right; it now has a run behind it.

**T2 — run, to close the inventory.** T2's community pole is Inferential-Thin and Peter's canons legislate for the whole community, so T2 is the one classification-adjacent confidence claim this corpus could plausibly touch. It fails on the reasoning §6 already supplies and `alx.source.alexandrian-canonical-answers` already states: a literate Greek bishop ruling *about* ordinary believers is evidence of their *conditions*, not of what they organised around. T2's poles and classification are untouched.

**The generation-step route — run, and it is new.** Candidate: **penitential-reintegrative discipline** (the graded reception of the lapsed and the regulation of ordinary conduct under crisis), generable on `Doc_04` §1's own rule from Streams 3, 7 and 8, attested by Dionysius (incl. *"On the Reception of the Lapsed to Penitence"*, corpus map `div2 4.4`), Peter (306), Timothy and Theophilus. Six tests:

- **Repetition — PASS.** Three streams, four bishops, mid to late horizon.
- **Persistence — FAILS the early phase.** It is a crisis response to Decius (250) and Diocletian (303–311); there is no Clement-phase attestation of it as an organising cluster. At best PARTIAL, on the pattern `Doc_04` used for C5.
- **Dependency — FAILS as an independent organiser, decisively.** Removed while C1 and C2 remain, nothing collapses: the canons argue *from* Scripture (C1) toward the sinner's restoration (which `Doc_04` §2 already folds into C2), and their authority sits at T1's bishop pole. This is precisely the reasoning by which `Doc_04` §2 declined **Askesis** — *"a genuine urban ascetic practice, but as a practice serving C2, not an organizer in its own right"* — and **D-A**.

**Result: not a gravity, or Supporting at the very most. No existing classification moves.** The route is genuinely unexamined and genuinely worth naming; it does not change the answer.

**Re-confirmed on re-run:** C5 Persistence (the disproof is `alx.figure.didymus`, *"head of the Alexandrian teaching tradition for roughly half a century, to 398"*, already inside the store against a standing PARTIAL); T1 pole separation (`Doc_04` line 132's *"not a polarity within one person"* is verbatim, and the document's inversion of the discovery pass is correct); T3 (Fragment VI is real, correctly quoted, correctly screened, and strengthens without reclassifying); T4 (the canons are juridical throughout and contain no martyr's interior — Inferential-Thin stands); C4 (fails on the practice-cluster criterion, and fails harder once its witnesses are screened); the Cross-Stratum Test / OG-4 (unchanged, for the reason `alx.source.alexandrian-canonical-answers` already supplies).

**There is no remaining untested route to a Doc_04 classification change. I looked for one outside the frame the prior two rounds used, found one, ran it, and it fails too. Stated plainly: the headline is right and I cannot break it.**

---

## F. DISCIPLINE COMPLIANCE

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS.** Header (*"escalated to the project lead — not self-disposed"*), §8's four reasons, §9's three grounded options with a reserved open question, §10's negative inventory, and OG-6's *"Status: OPEN — awaiting project-lead disposition."* Verified independently on disk: `records/alx/` unchanged across all three commits, no corpus-map edit, `records/worlds.yaml` still pins `packages/alx/2026-09-04T16-41-49Z`, no Doc_01–Doc_09 file touched, no `Gravity_Index.xlsx` created. Escalation categories 2 and 4 correctly identified. |
| No unverifiable project-lead attribution | **PASS.** §3.2 dates the npnf214 split (2026-08-26) without attributing the ruling to Mark, though the corpus map does say *"on Mark's ruling"*. §8 cites the S6.2 declaration by date without asserting a project-lead act. §10: *"No claim that any of this was seen or approved by the project lead."* The new OG-6 entry introduces no attribution of its own. |
| Claims no status it has not earned | **PASS, and repaired.** Header states both prior outcomes, *"Round 3 review pending — this document is NOT cleared, and no disposition has been assigned to it."* §10 says the same and discloses the Round 2 false claim in full. The one residual overclaim is a section heading, not a status claim — N3-4. |
| OG number no longer pre-assigned; the entry is actually written | **PASS, verified on disk and in git.** `Open_Gaps_Tracking.md` lines 247–299; commit `09c23d6`, +56 lines; working tree clean. This is the single clearest fix of the round. Its **content** is defective — N3-1 — but its existence is not asserted, it is true. |
| Grounded-options recommendation format | **PASS.** Three options with cost, precedent and stated reason; a named recommendation; the portfolio-level item separated; the recompile/re-admission question reserved to the project lead rather than pre-answered. |
| Accurate self-report of its own revision | **PASS with one carry-through.** Checked against `git diff 48ca471..09c23d6` rather than against §11's prose: all eight substantial items and all five claimed cosmetics landed. §11 item 4 repeats the body's C4 overstatement (N3-2). No phantom claims this round. |

---

## G. SUMMARY

- **Overall verdict: SUBSTANTIAL REVISION REQUIRED.**
- **Headline: CORRECT, re-confirmed a third time and against a route no prior round ran.** "Not structural" survives C3 Dependency, C4, C5, T1, T2, T3, T4, the Cross-Stratum Test, and the candidate-generation route. §9 Option B, escalated, should stand — extended to cover N3-3's restatement and N3-1's ledger correction.
- **Round 2's eight: 6 RESOLVED** (1, 2, 3, 5, 7, 8) · **1 RESOLVED FOR ITS OWN LOCUS BUT NOT CARRIED FORWARD** (6) · **1 PARTIALLY RESOLVED, FIX INTRODUCED NEW ERROR** (4).
- **New substantial: 4** — N3-1 the OG-6 entry drops §5.4 from the four defects it escalates; N3-2 the §5.1 screen is applied to exactly one item, and not to the section added to repair that very failure; N3-3 §5.3's "contradicted" charge reads a scope-limited clause at a wider scope, and §9's remedy inherits it; N3-4 "the last untested route" is contradicted by its own section and by the generation-step route.
- **New cosmetic: 12** (c-1 … c-12), of which six are Round 1 or Round 2 cosmetics still unrepaired.
- **What this revision got right and must not lose.** The OG-6 entry is real, was written before it was claimed, and its factual content — the anf06 search, the Achillas note, the Theognostus zero-count, 14-assigned/2-opened, Alexander's zero records, the missing workbook, the two-freezes split — checks out line by line against primary sources. §10's disclosure is the model of how to report a defect of one's own rather than repair it silently. The two restored scope limits are exact and the narrowed §4.5 is a genuinely better argument than the one it replaces. The Fragment VI transmission screen is right, and saying so about one's own best find takes something. The npnf214 word figures (551/456) are reproducible to the word. Every `div2`/`div3` locus in §2's table landed exactly where stated, again. And the C4 conclusion is correct even though its evidence is over-described.

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires. A qualified subject-matter reviewer on the transmission history of the Peter fragments through the fifth- and sixth-century christological florilegia, on the Melitian chronology, and on the evidentiary standing of the Alexandrian penitential canons would be the accountable test of §5.3, §5.4 and §6.1.)*
