# Doc_08 — Forces Document, and `lpc_Force_Index.md`: Latin Pastoral-Congregational Christianity
## Round 4 Independent Adversarial Review — verification of the Round 3 fix pass, and a cold read of everything it wrote

**Deliverables reviewed (together):**
`World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_08_Forces_Document.md` (466 lines)
`World-Builds/Latin-Pastoral-Congregational-Christianity/lpc_Force_Index.md` (157 lines)

**State reviewed:** the working tree, which is clean against `HEAD` = `2b76b128` ("lpc: apply Doc_08 Round 3 — all 15 findings; 4 HIGH again from the prior fix"). No uncommitted changes exist in the world directory.

**Prior rounds:** `Doc08_Round1_Review.md` (4H 5M 3L 1C), `Doc08_Round2_Review.md` (3H 4M 3L 1C), `Doc08_Round3_Review.md` (4H 5M 4L 2C) — all three SUBSTANTIAL REVISION REQUIRED. All counts re-verified at the artifacts themselves.

**Reviewer's standing:** independent of the drafting thread. Nothing in the commissioning brief was accepted without checking; two corrections to the brief are recorded at the end.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**3 HIGH · 3 MEDIUM · 5 LOW · 1 COSMETIC — 12 in total.**

**Thirteen of Round 3's fifteen findings are genuinely closed at the live text, several of them exactly and one of them (NEW-M2, the Latin emendation) better than the fix instruction asked for.** The substance of the forces analysis has now survived four rounds and is sound: seventeen forces across six populated cells, fifteen cross-cell connections with correct direction, both transmission entries present as named forces, every quotation verified to its containing work under the widened method, confidence calibrated correctly force by force on independent re-derivation.

**But two of Round 3's findings are not closed, and the way they are not closed is the pattern this document has now produced four times running.** Round 3's headline HIGH — the `2B-1`/G6 contradiction — was fixed in Doc_08 §5's prose and **nowhere else**. The co-produced Index still prints the connection the fix removed, because the generator reads the bolded force ID out of the correction notice that removes it. The delivered pair therefore says, on its face, that G6 has two connected forces (Doc_08 §5) and three (Index §3 and the `2B-1` master row) — a *new* contradiction created by the fix for the old one. And dropping `2B-1` from G6 falsified a claim in §5 that the fix's own notice certified nothing depended on.

Separately, Doc_08's masthead still reads **"Status: DRAFT — not reviewed, not self-disposed,"** and its Disposition still closes **"this is the sixth, and it has not been reviewed at all"** — in the revision whose Disposition three paragraphs earlier records three completed review rounds, and whose fix pass adopted a *standing discipline* that the review-history lines are the first thing a fix pass touches.

**Two of the three HIGH findings are defects the Round 3 fix pass introduced. The third is the "fixed at one site, missed at another" shape the brief predicted, at the two plainest statements of review status in the file.**

The distance to clearance is short. Four edits close every HIGH: strip correction notices before parsing §5 (one line in the generator), restate §5's Cross-Strand note, and rewrite two sentences in Doc_08's front and back matter. **No new source research is required.**

---

## Method — what I actually opened and ran

**Read whole:** both deliverables; `Doc08_Round3_Review.md` (all fifteen findings and its closing sections); `Doc_04_Gravity_Discovery.md` §§3–7 including the full Interaction Matrix; `L4-Templates/[world-code]_Forces_Document.md` §3 preamble and its Cell-1A and Cell-2B layer blocks; `FF.txt` (Forces Framework V1.1 plain text) Governing Principle, §3, §4; `gen_force_index.py` line by line; the `lpc_Decision_Log.md` entries for the Doc_08 Round 2 and Round 3 fix passes.

**Ran:**

1. **Regenerated the Index** from the live Doc_08 with the committed generator, writing to a scratch path. Output is **byte-identical to the delivered `lpc_Force_Index.md`** (`diff` returns nothing). The "Never hand-edited" claim holds.
2. **Instrumented the §5 gravity parse** to print each gravity's force list twice — as the generator derives it, and again after stripping `[CORRECTED …]` / `[ADDED …]` notices. **G6 is the only gravity where the two differ** (`2A-3, 2B-1, 2B-4` vs `2A-3, 2B-4`).
3. **Ran the current generator against the pre-fix draft at `9eccc532`.** It reports three `**STUB**` rows, "3 force(s) MISSING a Layer 2," and **three** §6 contradictions — `1B-1`/G2, `2A-1`/G8 and `2B-1`/G7. Against the live document it reports none. **Both claims the fix pass makes about the regression reproduce exactly.**
4. **An eight-case mutation battery** against the live Doc_08, regenerating the Index each time, with a positive control included so the instruments can be seen not to be inert. Table at "What these controls would still miss."
5. **The seven-marker Layer-2 register scan**, reconstructed from Round 3's description, over all seventeen Layer 2 blocks extracted by the generator's own rule — then re-run three more ways (notices stripped; the Reported-Experience paragraph exempted; and a completely different criterion, a grep for correction notices inside the world-voice span).
6. **A quotation pass built from scratch**: marked `<note>` spans in `cyprian.xml` **before** stripping tags, and converted every `<div1>`–`<div4>` `title=` attribute into a sentinel that survives the strip, so each hit returns both a note verdict and its containing work. Repeated on `npnf104_augustine-anti-manichaean-anti-donatist.xml` for the Augustine quotation. Ten Cyprianic/Pontian hits plus one Augustinian.
7. **The Latin emendation**, at `cic/texts/augustine_retractationes-lat_knoll-csel36.txt`: grep for both forms, whole-file counts, the raw span at lines 1508–1518, **the critical apparatus printed beneath it**, the file's own provenance header, and an independent occurrence of the same OCR error elsewhere in the file.
8. **Sibling and template survey:** all eight sibling `Doc_08` files plus the L4 template, grepped for any interposed block inside a Layer 2 span and for the specific Donatism and Alexandria wordings Doc_08 §8 attributes to them.
9. **Coverage measurement of the §6 control** over the live document's Layer-3 prose, printing every gravity-naming sentence the control examines, every one `DISCLAIM` suppresses, and every one that carries no `CONNECT` verb.
10. **Counts:** `git show` of the Status line and the Disposition's closing sentence at all four commits; `git diff --word-diff` of the Round 3 fix pass across both deliverables; correction-notice counts in both files; Layer 2 character lengths by the generator's own measure.

**Verification sources opened:** `Doc_01` §6 (the preliminary six-cell sketch), `Doc_02` §1 and §2, `Doc_05` §2.3 and §11, `Doc_06` §5, `Doc_07` §2G, `Lexicon_Deployment_Index.md` §6 and §7, `Source_Registry.md` rows 203 and 209, `cic/texts/INTAKE.md`, `reference/method/CiC_Record_Native_World_Build_Process_V1_3.md`, `World-Builds/Donatism/Doc_08_Forces_Document.md` §8 and §9, `World-Builds/Alexandria-Catechetical-School/Doc_08_Forces_Document.md` 3A-2.

---

## Job 1 — Round 3's fifteen findings, closure status at the live text

| # | Finding | Status |
|---|---|---|
| NEW-H1 | `2B-1`/G6 asserted one way at §3 and another at §5; Index prints the contradiction; §6's control blind to it | **NOT CLOSED** — fixed in Doc_08 §5's prose only. The Index's G6 row and `2B-1` row are **byte-identical to the pre-fix versions at all three fix commits**. The §6 control's new "both directions" is not the direction asked for. See **H1**, **H2**, **M1**. |
| NEW-H2 | Construction-record voice live inside Layer 2 at the three rewritten entries | **PARTLY CLOSED** — three of the four named sentences are genuinely moved out and nothing load-bearing was lost. But the same pass moved the Reported-Experience paragraphs, carrying review-provenance notices, back **into** Layer 2, and §8 certifies a scan result that the live text does not produce. See **M2**. |
| NEW-H3 | Review-history lines a round stale in both files | **PARTLY CLOSED** — Document Log rows added, Doc_08's Disposition rewritten, the Index's three literals fixed in the generator. **The masthead Status line and the Disposition's closing sentence were not touched, in any commit.** See **H3**. |
| NEW-H4 | §7 cross-check printed a false "absent" for `2B-3`; conflict branch dead for three of five levels | **CLOSED, and closed well.** §7 now prints agreement across all seventeen. Mutation-tested: relabelling `1A-1` as `(Contested)` and as `(Inferential/Thin, on a re-read)` both produce a correct **conflict** line, not an absence. |
| NEW-M1 | Regression result misreported | **CLOSED.** The restatement in the Index's §6 is accurate in every particular; I reproduced both halves of it. |
| NEW-M2 | Latin OCR silently normalised in the clause certifying it was retained | **CLOSED, and better than asked.** The emendation is marked, the file's reading printed, the OCR class named, and the apparatus claim is **true** — see the check-confirmation section. |
| NEW-M3 | Hard-coded-prose disclosure under-inclusive | **CLOSED in substance.** One residual, at §4's summary line. See **L2**. |
| NEW-M4 | §9's Reported-Experience tick said "`3B-1` and there only" | **CLOSED.** §9, §5 item 4 and §7 all now name both, and §9 adds the `2B-5` clause the fix instruction asked for. |
| NEW-M5 | The block reused a governed term; no template or sibling defines it; it relocated the template's marker | **CLOSED.** Renamed to "Construction-record notes on this entry"; the generator's split string matches the new heading exactly; the marker is back inside Layer 2; §8 declares the convention and carries it to the Disposition. All three factual claims in the declaration verify (see below). |
| NEW-L1 | §8 said three entries unwritten; §9 said one was never blank | **CLOSED in Doc_08, NOT in the Index.** See **L5**. |
| NEW-L2 | §8 dropped "complete" from Doc_02's finding | **CLOSED.** §8 now reads "no **complete** English translation vendored anywhere in this corpus — substantial excerpts survive inside NPNF's own editorial apparatus," which is `Doc_02` §1's sentence. |
| NEW-L3 | "one scoped exception" undercounted | **CLOSED.** Now "more than one scoped allowance," with FF's name-the-absence limb quoted exactly and both sibling readings named and verified. |
| NEW-L4 | 3B-2's bullets pointed at "the first sentence above" | **CLOSED.** Both referents are now quoted by their opening words. |
| NEW-C1 | "previously stood twice" | **CLOSED.** Now "at **three sites** — this entry, 3B-1, and §8," with the scope of the old count explained. |
| NEW-C2 | "2B-5's Layer 2 opened with" | **CLOSED.** Now "carried, in the tail of its opening sentence." |

**Thirteen closed, two not.** Both of the two are Round 3's own top two findings, and both are unclosed in the direction the brief warned about: a fix that landed in one file and not the other.

---

## HIGH

### H1 — The fix for Round 3's NEW-H1 never reached the Index: the correction notice that removes `2B-1` from G6 is the reason the generator still puts it there, and the delivered pair now contradicts itself on its face

**Site.** `Doc_08_Forces_Document.md` line 332 (§5, G6) and line 161 (§3, Force 2B-1, Layer 3). `lpc_Force_Index.md` line 32 (the `2B-1` master row: `G2, G6`), line 70 (the G6 by-gravity row: `2A-3`, `2B-1`, `2B-4`, count **3**), line 135 (the §6 observation row). `gen_force_index.py` lines 88–110 (the `GRAV_RE` / `explicit` pass).

**What I found.**

Round 3's NEW-H1 required `2B-1`'s gravity relation to be settled in §3, §5 and §6 **together**, and warned in terms: *"Do not close this by editing line 161 alone: the whole finding is that a claim about §5 was written without opening §5."*

The fix pass took option (a) — drop `2B-1` from §5's G6 list — and wrote the reasoning into a `[CORRECTED …]` notice appended to the same line. The line now reads:

> **G6 — Sacramental and Ordination Validity (Primary).** Connected forces: **2A-3** (…), **2B-4** (…). **[CORRECTED, 2026-09-15 — Round 3's NEW-H1:** this list also carried **2B-1** *"(its phase-two inheritance of the failed-member question)"*. … G6 keeps **two** connected forces and no claim in §5, §6 or §9 depends on the third.**]**

The generator derives each gravity's force list by matching `GRAV_RE` against the **whole line** and then running `re.findall(r'\*\*(\d[AB]-\d)\*\*', rest)` over everything after the gravity heading. `rest` includes the correction notice. The notice contains `**2B-1**` in bold. **The generator therefore reads the removal as an addition.**

I instrumented the parse and printed each gravity's list twice — as derived, and again after stripping `[CORRECTED …]` / `[ADDED …]` spans:

```
G6: as-generated=['2A-3', '2B-1', '2B-4']   notice-stripped=['2A-3', '2B-4']   <<< DIFFERS
```

G6 is the only gravity where the two differ. G2's and G8's notices name force IDs that are already in their lists, so they are invisible; G6's is not.

**The consequence, in the delivered files.**

- Doc_08 §5 says, in terms: *"G6 keeps **two** connected forces."* The Index's G6 row says **3**.
- Doc_08 §3 says, in terms: *"**This force therefore connects to G2, and to G2 only.** … **Neither §5's G6 list nor its G7 list carries it.**"* The Index's `2B-1` master row reads **`G2, G6`**.
- Index §6, the reconciliation section, prints a row — `` `2B-1` | G6 | §5's list carries it; §3's Layer 3 does not assert it in a connection sentence `` — which is the live contradiction filed as an **observation, not a defect**.
- Index §6's headline sentence prints *"**No contradictions:** … and none asserts a disconnection §5 contradicts."* §3's 2B-1 asserts exactly that disconnection, and (as the generator sees §5) §5 contradicts it. See **M1**.

**Three further confirmations, because a single instrumented parse proves only that my parse and theirs agree.**

1. **Mutation.** I edited the live Doc_08 so that §5's G6 list *genuinely* carries `2B-1` in the list proper (`**2B-4** (re-opens it across the gap), **2B-1** (its phase-two inheritance).`) and regenerated. The G6 row, the `2B-1` row, §6 and §7 come out **identical to the delivered file**. The generator cannot distinguish "§5 lists `2B-1` under G6" from "§5 removed `2B-1` from G6 and explained why."
2. **Git.** The G6 row is byte-identical at `99c1164f` (Round 1 fix), `561c2c35` (Round 2 fix) and `2b76b128` (Round 3 fix): `` | **G6** — Sacramental and Ordination Validity | Primary | `2A-3`, `2B-1`, `2B-4` | 3 | §5 list | ``. A `git diff` of the Round 3 fix pass across the Index shows **no table row changed at all**. The pass regenerated the Index, got the same tables back, and did not read them.
3. **Direct read.** §5's own prose and the Index's own count disagree by one, in plain text, three files apart.

**The masthead compounds it.** `Doc_08_Forces_Document.md` line 12 still claims the Index is *"generated from this document's own prose by script **so the two cannot drift**."* That is the exact claim `lpc_Force_Index.md`'s own header retracted at Round 1's H1 (*"its 'cannot drift' claim was false"*) and narrowed again at Round 2's M1. It has never been corrected in Doc_08, and it is now falsified by a live drift of the pair's central relation.

**Why this matters.** Doc_09 draws its gravity–force grounding from this pair, and the Index's by-gravity view is what §9's completion tick tells a reader to check. A reader who follows that pointer is sent to a table that disagrees with the section it claims to index. Worse, this is the third consecutive round in which `2B-1`'s gravity relation has been wrong in a different place each time — Round 1 found §3/§5 divergent, Round 2 found §5's two lists treated asymmetrically, Round 3 found §3 asserting a fact about §5 that §5 contradicted, and Round 4 finds §5 and the Index contradicting each other. Each fix was correct in its own file and blind to the next one.

**And the underlying G6 question is not as settled as the notice says.** The notice's whole justification is symmetry: *"Doc_04's finding runs to **both** candidates, so treating one as a connection and the other as a resemblance would be a choice this document made without defending."* That is true of Doc_04's **Persistence** test (line 47, line 175, line 182 — *"a family resemblance to Candidates 6 and 7"*). It is **not** true of Doc_04's **Interaction Matrix** (§6), which relates Candidate 2 to the two candidates by *different* relations:

- Candidate 2 × Candidate 6: *"**Reinforcing** (both are boundary/reintegration questions **Cyprian reasons about consistently** — this document's own reading)"*
- Candidate 2 × Candidate 7: *"**Reshaped by** (7 is Augustine's own phase-specific reworking of a structurally similar question, not 2's own continuation)"*

So Doc_04 records a **first-phase, Cyprian-side** relation between Candidate 2 and Candidate 6 that has nothing to do with the phase-two family resemblance — and no counterpart for Candidate 7, whose relation to Candidate 2 is explicitly the phase-two reworking. **G6 does have an independent claim to `2B-1`, at a locus in Doc_04 the notice never opens**, and it is a claim that is not symmetric with G7's. That claim, if taken, would also repair **H2** below. The document may still decide to drop `2B-1` — the Interaction Matrix is a gravity-to-gravity relation and §5's lists are force-to-gravity — but it must decide it against that locus, not against a symmetry Doc_04 only half supports.

**Fix.**
1. **In the generator**, strip `[CORRECTED …]`, `[ADDED …]`, `[MOVED HERE …]` and `[REVISED …]` spans from `rest` before `re.findall`, exactly as the §6 control already does for Layer 3 (`re.sub(r"\*\*\[(?:CORRECTED|ADDED).*?\*\*\]\*\*", "", seg, flags=re.S)`). Then regenerate and **read the G6 row and the `2B-1` row** before committing.
2. **In Doc_08 §5's G6 entry**, address Doc_04 §6's `2 × 6` "Reinforcing (… Cyprian reasons about consistently)" cell by name: either add `2B-1` back on that ground — which restores G6's first-phase reach and repairs **H2** — or state why a gravity-to-gravity interaction is not a force route. Do not leave the notice's symmetry argument standing unqualified.
3. **In Doc_08 line 12**, delete or qualify "so the two cannot drift." The Index's own header already says what is true; the source document should not say something stronger.

---

### H2 — Dropping `2B-1` from G6 falsified §5's Cross-Strand Gravity Note, in the same section whose correction notice certified that nothing in §5 depended on it

**Site.** `Doc_08_Forces_Document.md` line 342 (§5, Cross-Strand Gravity Note) against line 332 (§5, G6) and its correction notice; against `Doc_04_Gravity_Discovery.md` line 164 (§4, Candidate 6).

**What I found.**

The G6 correction notice closes: *"G6 keeps two connected forces and **no claim in §5, §6 or §9 depends on the third**."*

Four lines below, §5's Cross-Strand Gravity Note reads:

> **This world was found strand-singular at Doc_01 §5**, so no cross-strand convergence test applies. Doc_04 §5 declared **phase testing** as the substitute discipline, and **the forces analysis reproduces its results independently**: the forces connected to G2 and G8 are phase-one forces; the force producing G7 is a phase-two force; **G1, G3, G4 and G6 connect to forces in both rows.**

After the fix, G6's connected forces are `2A-3` and `2B-4` **and nothing else**. Both are second-phase forces on Doc_08's own account:

- **2A-3**, Layer 1: *"Dominant across large parts of North African Christian life for **most of the century between the two phases**, and a continuing live pastoral problem **throughout Augustine's episcopate**."* Layer 3: *"**This is the force with the most consequential reach in the second phase**."*
- **2B-4**, Layer 1: *"Augustine read, argued with and overturned the 256 Council's ruling."*

Both also sit in the **Ongoing** row. So the sentence fails on either reading of "rows" — as matrix rows (both are Ongoing) or as phases (both are phase two). `2B-1` — *"The lapsed under Cyprian; ordinary post-baptismal sin and schism-tempted believers under Augustine"* — was **the only force in G6's list with any first-phase content**, and it was removed.

**This is not a technicality about a word.** Doc_04 §4's classification table says of Candidate 6: *"Strand-singular world; **cross-phase**, the question persists as its own answer reverses."* Its Persistence test says: *"Passes. **Visible in both phases**."* The Cross-Strand note's whole claim is that "the forces analysis **reproduces its results independently**." After the fix it does not, at the one gravity Doc_04 singles out for cross-phase persistence — and the notice that caused this asserts the opposite in the same section.

**Secondary, and pre-existing rather than introduced.** The same sentence's first clause — *"the forces connected to G2 … are phase-one forces"* — is loose for the same reason in the other direction: G2's forces include `2B-1`, which Doc_08's own Layer 1 and Doc_01 §6's own cell both define as spanning both phases. This has stood since the initial draft and is not the fix pass's doing, but it should be corrected in the same edit, since one sentence is now wrong about two of its four clauses.

**How I confirmed it a second way.** The claim rests on the phase attribution of `2A-3` and `2B-4`, which I could have got wrong by reading "Ongoing" as "spans both phases." So I took the attribution from Doc_08's own prose rather than from the cell label — 2A-3's Layer 3 sentence *"the most consequential reach in the second phase"* and 2B-4's Layer 1 naming Augustine — and then checked the claim against Doc_04 §4's independent statement that Candidate 6 is cross-phase. Three sources, one conclusion.

**Why this matters.** Doc_01 §5 found this world strand-singular; Doc_04 §5 declared phase testing the substitute for Article 21's cross-strand convergence test; §5's Cross-Strand note is where Doc_08 discharges that substitute. It is a governance-bearing paragraph, and it is now false at one of its four clauses because of a fix made four lines above it.

**Fix.** Either add `2B-1` back to G6 on the Doc_04 §6 ground named in **H1** — which makes the sentence true again and is the cleaner outcome — or restate the Cross-Strand note honestly: G6's force-connections are both second-phase, which **diverges from** Doc_04's cross-phase finding for Candidate 6, and say whether that is a limit of the forces view or a reason to revisit the G6 list. Correct the G2 clause in the same edit. Then delete or re-scope "no claim in §5, §6 or §9 depends on the third."

---

### H3 — Doc_08's masthead still says the document has not been reviewed, and its Disposition still closes by saying so, in the revision that adopted a standing discipline about exactly this

**Site.** `Doc_08_Forces_Document.md` line 14 (Status) and line 466 (Disposition, closing paragraph), against lines 446–452 (Document Log) and line 458 (Disposition, opening).

**What I found.**

Line 14, the first status a reader of this document meets:

> **Status:** **DRAFT — not reviewed, not self-disposed.**

Line 466, the last sentence of the document:

> **Five documents in this world are complete, independently reviewed, and awaiting a disposition only the project lead can give; **this is the sixth, and it has not been reviewed at all.****

Both are false. Three independent adversarial rounds have been run against this document; all three review artifacts sit in `Review-Artifacts/`; the Document Log eight lines above line 466 lists all three by name, date and finding count; and line 458 reads "**Not disposed. REVISED after Round 3; the revision is unreviewed.**"

I checked both lines at every commit in the document's history:

```
9eccc532:  **Status:** **DRAFT — not reviewed, not self-disposed.**
99c1164f:  **Status:** **DRAFT — not reviewed, not self-disposed.**
561c2c35:  **Status:** **DRAFT — not reviewed, not self-disposed.**
2b76b128:  **Status:** **DRAFT — not reviewed, not self-disposed.**
```

and identically for "this is the sixth, and it has not been reviewed at all." **Neither line has been touched by any of the three fix passes.**

**What makes this a HIGH rather than a stale cross-reference.** Round 3's NEW-H3 was raised on precisely this defect, in precisely this file, and its fix instruction was *"Rewrite Doc_08's Disposition to state the true position … Then add a standing discipline: the review-history lines are the ones this build has now got wrong twice, so they should be the first thing a fix pass touches, not the last."* The fix pass wrote that discipline into the document, at line 462:

> **Standing discipline adopted: the review-history lines are the first thing a fix pass touches, not the last.**

— and then did not touch the review-history line four lines below it, or the one at the top of the same file. The pass searched for the *paragraph* Round 3 quoted rather than for the *class* of statement Round 3 named. That is the identical mechanism Round 3 diagnosed, at the identical file, one round later.

Constitution Article 30 and CO-022 make disposition turn on review status. A project lead opening this file is told at line 14 that it is an unreviewed draft, and at line 466 that it "has not been reviewed at all." The Index, by contrast, now states the position correctly at every one of its four sites. **The two co-deliverables disagree about whether this document has ever been reviewed.**

**Fix.** Line 14: `**Status:** **REVISED after Round 3 — the revision is unreviewed, and not self-disposed.**` (the Index's own wording, so the pair matches). Line 466: replace "this is the sixth, and it has not been reviewed at all" with the true position — three rounds run, all three SUBSTANTIAL REVISION REQUIRED, the current revision unreviewed. Then, before committing, `grep -in 'not reviewed\|no reviewer\|unreviewed\|first-draft' ` both files and read every hit; that is a ten-second check that would have caught this and Round 3's H3.

---

## MEDIUM

### M1 — Index §6 prints that "both directions are tested" and that "none asserts a disconnection §5 contradicts." Neither is true: there is no disconnection test in the generator, and the live NEW-H1 scenario returns clean under mutation

**Site.** `lpc_Force_Index.md` lines 122 and 141; `gen_force_index.py` lines 152–190 (`CONNECT`, `DISCLAIM`, `mismatch`, `observed`).

**What I found.**

Round 3's NEW-H1 fix instruction was: *"widen §6's control to report **both directions**, with the reverse direction printed as an observation rather than a defect if that distinction is worth keeping."* The direction that had been missed was named precisely: *"This is the reverse: §3 asserts a **dis**connection §5's list contradicts."*

The generator now computes two sets:

```python
for g in sorted(set(l3claims[f["id"]]) - set(f["grav"])):   # §3 asserts, §5 omits
    mismatch.append(...)
for g in sorted(set(f["grav"]) - set(l3claims[f["id"]])):   # §5 carries, §3 silent
    observed.append(...)
```

The second set is **presence-minus-presence**, not disclaimer-versus-list. Nothing in the file evaluates a `DISCLAIM`-matching sentence against §5's list. **Silence is not a disclaimer, and the control cannot tell the two apart.** So the direction Round 3 asked for is still untested, and the direction that was added is a different one.

Yet the `else` branch prints, as a derived finding:

> **No contradictions: no force's §3 Layer 3 asserts a gravity connection that §5's canonical list omits, and **none asserts a disconnection §5 contradicts**.** Both directions are tested; see below.

The second clause of that sentence is an unconditional string literal in a branch whose condition (`mismatch` empty) has nothing to do with it. The Index's own header classifies "the §6 reconciliation report" as **derived and therefore re-checked on every run**.

**Confirmed by mutation, not by reading the code alone.** I rewrote §5's G6 entry so that its list proper carries `2B-1` while §3's 2B-1 continues to assert *"connects to G2, and to G2 only"* — the exact NEW-H1 scenario, made explicit rather than latent — and regenerated. §6 prints **"No contradictions … and none asserts a disconnection §5 contradicts."** The control that Round 3 said *"returns clean on a live contradiction of precisely the kind it was installed to notice"* still does.

A positive control in the same battery (§5 drops `2A-4` from G7) produces `1 contradiction flagged`, so the instrument is not inert. It looks only one way, and the new table is a second view of the same one direction.

**Fix.** Implement the direction that was asked for: collect, per force, the gravities its Layer 3 **disclaims** (the `DISCLAIM` hits, which the control already computes and throws away), intersect with `f["grav"]`, and print those as contradictions. Until then, delete the clause "and none asserts a disconnection §5 contradicts" and the sentence "Both directions are tested" — they describe a test that does not exist. Note also that with **H1** fixed (notices stripped from §5), `2B-1`'s G6 entry would disappear from `f["grav"]` and this particular contradiction would resolve itself; but the control would still be blind to the next one.

### M2 — §8 certifies that a seven-marker register scan "returns zero across all seventeen" Layer 2 blocks. It returns six hits at two blocks, because the same pass that moved four sentences out of Layer 2 moved two review-provenance notices back in

**Site.** `Doc_08_Forces_Document.md` line 397 (§8, "Checked rather than asserted") and line 393 (§8, the convention statement), against line 252 (3B-1's Layer 2) and line 270 (3B-2's Layer 2).

**What I found.**

§8 now states:

> **Checked rather than asserted.** The certification above was verified by extracting all seventeen Layer 2 blocks and scanning them for seven markers of construction-record register — force IDs, `Doc_0n` citations, build-file references, `§` references, self-reference to the layer scheme, "this build / this document / this entry," and evidentiary meta-statements. **Round 3 ran that scan and found three of seventeen firing, all three in the entries the previous pass had rewritten**; **the scan now returns zero across all seventeen.**

I rebuilt that scan from Round 3's own description, over all seventeen Layer 2 blocks extracted by **the generator's own rule** (world-voice portion only; construction-record blocks split off at the new heading string). Result:

```
3B-1:  ['§ reference', 'layer-scheme self-ref', 'evidentiary meta']
3B-2:  ['§ reference', 'layer-scheme self-ref', 'evidentiary meta']
TOTAL seven-marker hits across 17 blocks: 6
```

Fourteen of seventeen return zero on every marker, as before. The three sentences Round 3 named at 2B-5 and 3B-1, and the two at 3B-2, are genuinely gone — I checked each by hand and **2B-5 now returns zero**. What fires is new material:

> ***Reported-Experience Status* (Constitution Article 17; Forces Framework §3)** applies to the whole Layer 2 above: *reported as the world's own self-understanding — not assessed for historical accuracy; confidence calibration applies to the historical-event layer only.* **[ADDED, 2026-09-15 — Round 2's C1; kept inside Layer 2 at Round 3's NEW-M5**, which found that both the L4 template and Forces Framework §3 place this marker *within* Layer 2, so moving it out was a departure from the two documents the fix was meant to satisfy.**]**

and the corresponding paragraph at 3B-2.

**Scoping this precisely, because the obvious version of this finding overstates it.** Round 3's NEW-M5 fix instruction was *"keep the Reported-Experience marker inside Layer 2 where the template puts it"* — and the template does. I verified it: `L4-Templates/[world-code]_Forces_Document.md` lines 127–135 place the marker inside the Layer 2 bracket text, and FF's Governing Principle does the same. So the marker's presence is compliance, not a breach, and any honest scan must exempt it. I re-ran the scan three more ways to find out exactly what is and is not defensible:

| Scan variant | Result |
|---|---|
| As §8 describes it — seventeen blocks, seven markers | **6 hits at 2 blocks** |
| Same, with all `[CORRECTED…]`/`[ADDED…]` notices stripped first (as the §6 control does for Layer 3) | **6 hits at 2 blocks** — the marker sentence alone fires |
| Same, with the **entire** Reported-Experience paragraph exempted | **0 across all seventeen** |
| A completely different criterion: grep for a correction notice inside the world-voice span | **2 hits** — `3B-1` and `3B-2` |

So: **§8's claim is true only under an exemption §8 does not state**, and two of the seven markers it lists by name (`§` references, self-reference to the layer scheme) are in the exempted text. That is an overclaim in a paragraph whose whole point is that the certification was checked rather than asserted.

**And one thing is not exempt on any reading.** The bracketed clause *"kept inside Layer 2 at Round 3's NEW-M5, which found that both the L4 template and Forces Framework §3 place this marker within Layer 2, so moving it out was a departure from the two documents the fix was meant to satisfy"* is **not** template-mandated. It is a sentence about a review finding, addressed to a reviewer, sitting inside the layer whose governing test is *"could someone formed within this world recognize this as an honest account of how they understood what was happening to them?"* (FF line 170). That is the same class of defect as Round 2's M3 and Round 3's NEW-H2 — smaller, because it is bracketed and typographically separated rather than embedded in a world-voice sentence, which is why this is MEDIUM and not HIGH.

§8's own convention statement makes the point against itself: *"Three entries (2B-5, 3B-1, 3B-2) carry source status **or a correction recorded against them**. **None of that is the world's voice**, so **none of it sits in Layer 2**."* Two corrections recorded against two of those three entries sit in Layer 2.

**I re-tested all seventeen Layer 2 blocks against FF's governing test by reading them, not only by scanning.** Fourteen pass without argument. The three rewritten ones read well as prose, and the moves did not break them — 3B-1's "Augustine, at the end, goes back through everything he has written and corrects it" is stronger without the provenance parenthesis, and 3B-2's opening no longer begins with an evidentiary hedge. Nothing load-bearing was lost: the Registry row, the Latin-only witness, the "this build's own rendering" disclosure and the 2B-4 cross-reference are all present, verbatim, in the blocks below. **Two residues the scan cannot see and I record rather than grade**: 2B-3's *"a century and a third later the magistrate could be asked"* and 2B-5's *"the Catholic institutional tradition's selection, and a 19th-century translation programme"* are written from outside the world's time. Both are house convention in a two-phase world, both are honest about being bounds, and 2B-5's is followed immediately by *"No one here could feel a translator's hand that had not yet reached for the page"* — which is the world's-voice way of saying it. They are named here so §8's certification is read for what the scan measures.

**Fix.** One clause in §8: say that the scan exempts the template-mandated Reported-Experience marker sentence, and that with that exemption it returns zero. Then move the `[ADDED …]` provenance clauses out of both markers into the construction-record blocks below them, where every other such notice at those entries already sits — the marker keeps its template wording and its scope sentence, the review history keeps its place, and the scan's exemption becomes narrow enough to state in one line.

### M3 — Index §6's observation table prints at least one flatly false row, because `DISCLAIM` now suppresses any sentence containing "§5"

**Site.** `lpc_Force_Index.md` line 128 (the `1B-1`/G2 observation row) and line 132 (`2A-2`/G4); `gen_force_index.py` lines 168–172 (`DISCLAIM`), against `Doc_08_Forces_Document.md` line 79 (1B-1, Layer 3).

**What I found.**

The brief asked directly whether `DISCLAIM` — which now matches `\bneither\b`, `\bnor\b`, `\bnot a\b` and `§5` anywhere in a sentence — suppresses legitimate findings. **It does, on the live document, and the suppression is printed as a false statement in the delivered Index.**

I measured the control's coverage over every Layer-3 sentence in the live document that names a gravity:

```
Layer-3 sentences naming a gravity:                   21
  examined (CONNECT matched, DISCLAIM did not):       13
  suppressed by DISCLAIM although CONNECT matched:     3
  no CONNECT verb:                                     5
```

The three suppressions:

| Force | Keyword | Sentence | Legitimate? |
|---|---|---|---|
| `1B-1` | **`§5`** | *"It also **makes G2's regulated penitential process possible** — an unorganized community could not have run one, and **§5's G2 entry carries this force for that reason**"* | **No — this is an explicit connection assertion** |
| `2A-1` | `attested only` | *"which is why **G2** and **G8** are attested only within it"* | Yes — an attestation claim |
| `2B-1` | `family resemblance` | *"Its phase-two afterlife is a *family resemblance* to **G6 and G7**"* | Yes — explicitly not a connection |

1B-1's sentence asserts the G2 connection in the clearest terms in the document, **and points the reader at §5's own list while doing it**. It is suppressed only because it contains the string `§5`. The Index consequently prints:

> | `1B-1` | G2 | §5's list carries it; **§3's Layer 3 does not assert it in a connection sentence** |

That is false. §3's Layer 3 does assert it, in a connection sentence, and the clause that makes it invisible — *"and §5's G2 entry carries this force for that reason"* — was added by the **Round 2** fix pass to close Round 2's H2, while the `§5` exclusion was added by the **Round 3** fix pass. Each was reasonable alone; together they produce a delivered artifact that denies a connection its source document asserts.

A second, weaker instance sits at `2A-2 | G4`: §3's 2A-2 Layer 3 closes *"crisis metabolized into formation content **through G4**"* — a mechanism statement naming G4 as the channel, which §5's G4 entry then reflects. It carries no `CONNECT` verb, so the same row prints the same false denial. I grade this one as arguable rather than clear-cut.

**Why this matters.** The observation table was added at Round 3 to make the control's asymmetry *visible rather than hidden*. It currently hides a different asymmetry behind a sentence that states the opposite of the document. And the failure mode is the build's signature: the `§5` exclusion was added to kill one false positive (*"Neither §5's G6 list nor its G7 list carries it"*), was not tested against the rest of the corpus, and silently removed a true positive.

**Fix.** Narrow the `§5` clause so it fires only on a sentence *about* §5's lists rather than any sentence mentioning §5 — e.g. require `§5's G\d list` or `§5's .{0,20}list` rather than a bare `§5`. Then re-run and re-read the observation table; the two rows above should disappear. Alternatively, change the observation rows' wording from "does not assert it in a connection sentence" to "the control did not recognise an assertion of it," which is what the control actually measured and is true whatever its coverage.

---

## LOW

### L1 — §5's Cross-Strand note restates Doc_04's attestation wording for G5 as if it were a forces finding, and it does not hold as one

**Site.** `Doc_08_Forces_Document.md` line 342, against `Doc_04_Gravity_Discovery.md` line 163.

§5 says: *"**G5 connects to forces in both phases at one locus each** — thin across the span rather than bounded within it, which is the distinction Doc_04 §5 insisted on and which **the forces view confirms from a different direction**."*

Doc_04 §4's row for Candidate 5 says: *"**not phase-bound** — **attested in both phases at one locus each**, so **thin across the span rather than bounded within it**."*

The wording is Doc_04's, borrowed verbatim, and it is Doc_04's claim about **attestation**. As a claim about *forces*, it does not hold: G5's connected forces are `1B-1` (first phase) and `2A-3` + `2B-4` (both second phase) — one locus and two, not one each. So the sentence does not "confirm from a different direction"; it repeats the same direction in different words. Pre-existing since the initial draft and unflagged in three rounds.

**Fix.** Either state the actual distribution ("one first-phase force and two second-phase, each of them indirect") or drop the "confirms from a different direction" claim and cite Doc_04's finding as carried rather than reproduced.

### L2 — Index §4's summary line hard-codes two force IDs inside a sentence the header's disclosure classifies as derived

**Site.** `lpc_Force_Index.md` line 100; `gen_force_index.py` line 300.

The line reads: *"**15 connections**, including **1 deliberate non-connection** (`2A-2`) and **one coincidence marked as not causal** (`3A-1` → `3B-1`)."* The count and the non-connection count are derived; `` `2A-2` ``, `` `3A-1` → `3B-1` `` and the word "one" are literals.

Demonstrated by mutation: making `1B-3` the deliberately isolated force instead of `2A-2` leaves the line reading *"**1 deliberate non-connection** (`2A-2`)"*. Adding a second isolated force produces *"**2 deliberate non-connection** (`2A-2`)"* — both the wrong ID and a broken plural.

NEW-M3's fix made the hard-coded-prose disclosure exhaustive for the header and §§2–7 explanatory paragraphs, and it is now accurate for those. This line is the residual: the disclosure says "all counts and totals" are derived and re-checked, and this total carries two undisclosed literals inside it.

**Fix.** Derive the IDs (`", ".join(c["src"] for c in conns if c["dst"].startswith("(none)"))`), pluralise on `noconn`, and derive the coincidence pair from the `dir` string, or add one clause to the disclosure naming §4's summary line.

### L3 — Doc_08's Disposition says "four have not" and "Five documents" in consecutive sentences

**Site.** `Doc_08_Forces_Document.md` line 466, against line 25 (§1).

The closing paragraph reads: *"`cic-build-cycle` requires a document to reach at least *Approved to proceed* before the next begins; **four have not**, and a category is open against each. … **Five documents** in this world are complete, independently reviewed, and awaiting a disposition only the project lead can give."*

§1 names four: *"**Doc_04, Doc_05, Doc_06 and Doc_07 — all complete and independently reviewed, none self-disposed** … categories are open against all four."* Doc_01, Doc_02 and Doc_03 are recorded there as Approved to proceed. The paragraph does not say which document is the fifth, and no fifth is identifiable from §1. Unchanged since the initial draft.

**Fix.** Make it four, or name the fifth (the `Source_Registry.md` return to independent review of 2026-09-13 is the only candidate §1 mentions, and it is not a document in the Doc_ sequence).

### L4 — Index §6's "7 of the 19" coverage figure is measured on a superseded draft and presented in the present tense about "the live document"

**Site.** `lpc_Force_Index.md` line 141.

The paragraph reads: *"**Measured across the live document, it examined 7 of the 19** Layer-3 sentences that name a gravity."* That measurement is Round 3's, taken against the document as it stood at `561c2c35`. The live document has since been rewritten at 2B-1's Layer 3 — the very entry the sentence goes on to discuss — so "the live document" no longer means what it meant when the number was taken.

My own count on the current text, by a comparable rule, is **21** gravity-naming Layer-3 sentences, of which the current control examines 13. **I am not reporting 19 as wrong**: sentence-splitting and "names a gravity" are method-dependent, and reporting a different number as a correction would be exactly the class of check-defect this build keeps producing. The finding is the tense and the referent, not the arithmetic.

**Fix.** "Measured across the document as it stood at `561c2c35`, the earlier control examined 7 of the 19 …" — or re-measure against the live text and say so.

### L5 — The Index still gives the account of the Round 1 H4 defect that Doc_08 corrected at Round 3, so the two deliverables now disagree about it

**Site.** `lpc_Force_Index.md` line 114, against `Doc_08_Forces_Document.md` lines 399 and 420, and against `lpc_Force_Index.md` line 141.

Index §5: *"**[CORRECTED, 2026-09-15 — Round 1's H4.]** **Three** Layer 2 entries were **previously unwritten** …"*

Doc_08 §8 (rewritten at Round 3 to close NEW-L1): *"An earlier version of this document left **two** Layer 2 entries genuinely blank — 2B-5 and 3B-2 — and a third, **3B-1**, written but self-declared *'left unfilled'* …"*

Doc_08 §9 says the same. The Index's own §6 also says the same — *"one of which — `3B-1` — Doc_08 §9 holds was never blank, so that third flag is a false positive"* — so the Index contradicts itself as well as its companion.

NEW-L1 was graded LOW at Round 3 and I grade this the same, for consistency: it is the same substance. It is recorded because it is the third instance in this round of a fix that landed in one file of a pair that is reviewed and disposed of together.

**Fix.** Bring the Index's §5 paragraph into line with Doc_08 §§8–9 — in `gen_force_index.py` line 268, since it is a literal.

---

## COSMETIC

### C1 — "closes with 'Do not create new workbooks'"

`Doc_08_Forces_Document.md` line 464 (Disposition, CO-022 paragraph): *"`CiC_Record_Native_World_Build_Process_V1_3.md` states that the per-world `.xlsx` workbooks are **RETIRED for new builds** and **closes with** *'Do not create new workbooks.'*"*

The *paragraph* closes with it, at line 160 of a 589-line file. The substance is exact — I opened the file and both quoted strings are verbatim at lines 156 and 160 — and the conclusion drawn from it is right. Reported only because the surrounding line is otherwise precise and this build grades this register of claim (NEW-C2 was the same shape).

**Fix.** "and whose index-artifacts paragraph closes with."

---

## Additional checks that returned clean, and which of them I tested hardest

**Quotation fidelity — tested hardest.** I rebuilt the widened method from scratch rather than reusing any prior artifact: mark `<note>` spans **before** stripping tags, and convert every `<div1>`–`<div4>` `title=` attribute into a sentinel that survives the strip, so each hit returns a note verdict **and** its containing work. Eleven quotations, two corpora, two code paths:

| Quotation (opening words) | Site | Apparatus? | Containing work |
|---|---|---|---|
| "it is the shepherd that is chiefly wounded…" | 1A-1 | outside | On the Lapsed — Cyprian |
| "your suffrage and God's judgment" | 1B-2 | outside | Ep. XXXIX, To the People, Concerning Five Schismatic Presbyters — Cyprian |
| "ancient venom" | 1B-2 | outside | same — Cyprian |
| "by the judgment of God and the favour of the people…" | 1B-2 | outside | The Life and Passion of Cyprian, by Pontius the Deacon |
| "thousands of certificates were daily given…" | 2B-2 | outside | Ep. XIV, To the Presbyters and Deacons Assembled at Rome — Cyprian |
| "these thirteen letters sent forth at various times…" | 2B-5 | outside | Ep. XIV — Cyprian |
| "you always read my letters to the very distinguished clergy…" | 2B-5 | outside | Ep. LIV, To Cornelius, Concerning Fortunatus and Felicissimus — Cyprian |
| "matter, and even the paper itself, gave me the idea…" | 2B-5 | outside | Ep. III, To the Presbyters and Deacons Abiding at Rome, A.D. 250 — Cyprian |
| "as it actually came to hand, that you may examine…" | 2B-5 | outside | same — Cyprian |
| "to send a copy of this letter to whomsoever you are able…" | 2B-5 note | outside | **Ep. II, From the Roman Clergy to the Carthaginian Clergy** |
| "even of the plenary Councils, the earlier are often corrected…" | 2B-4 | outside | On Baptism, Against the Donatists, Bk. II ch. 3 (`npnf104`) — Augustine |

Every one occurs exactly once in its volume, every one is outside editorial apparatus, and every one is by the figure Doc_08 says wrote it. **The intra-corpus misattribution corrected at Round 2's H1 is confirmed correct**: the copy-and-forward instruction is Epistle II, by the Roman clergy. I also verified the subsidiary claim that this is "by the edition's own note, the very letter Cyprian later returned for collation" — Epistle III §2 reads *"I have, moreover, read another epistle,"* and the edition's note on that phrase reads *"The foregoing letter, Ep. ii."* Exact.

**The Index's derived content — tested hardest, second.** An independent parse of Doc_08 §§3–5, written before I read the generator's derivation code, reproduces the master table's confidence column for all seventeen rows, the 14/3/0/0/0 distribution, the fifteen-row connection table with correct inversions in both directions, the `2A-2` `(none)` row, the `1B-3` `*(no §4 row)*` cell, and the by-gravity table for seven of the eight gravities including the G4 set-reference expansion to five. **The eighth is G6, and that is H1.** Everything else re-derives with zero mismatches.

**Doc_04 fidelity.** All eight `G`*n*→Candidate *n* mappings and all eight classifications re-verify against Doc_04 §4's table (Primary: 1, 2, 3, 6; Supporting: 4, 5, 7; Tensional: 8). Doc_04's Candidate 5 heading is quoted with its `[Supporting]` tag exactly. The family-resemblance reading is faithful at all three loci (lines 47, 175, 182) — with the Interaction-Matrix qualification recorded at **H1**.

**Governing-document quotations — all exact.** FF's *"This is not optional. All three layers are required for every force"* (FF line 141); FF's Governing Principle name-the-absence limb, quoted in full at §8 (FF line 34, verbatim including "documents the limit"); FF's incomplete-ecology sentence (FF lines 176 and 200); the L4 template's Proportionality carve-out (template lines 104–106, verbatim); the template's Layer 2 Reported-Experience bracket text and its Cell-2B instruction naming the slot. The `[A]` bracket on the FF quotation at §5's G5 is correct rather than a misrepresentation — Doc_04 line 97, which Doc_08 cites in the same sentence, quotes it mid-sentence with a lowercase *a*.

**§8's three factual claims about the construction-record block — all verified.** No template defines it: `L4-Templates/[world-code]_Forces_Document.md` defines exactly three headed layers per force with nothing between them, and contains no occurrence of "construction-record." No sibling uses one: I parsed every Layer 2 → Layer 3 span in all eight sibling `Doc_08` files and found **no interposed bold header in any of them**, and no occurrence of "construction-record" in any. Donatism's alternative is exact — its §8 records moving *"inline document citations inside four 'not recoverable' Layer 2 entries … which belong to Layer 1's or Layer 3's own analytical register, moved there."* Alexandria's is exact and is at exactly one force — its 3A-2 reads *"Layer 2 — not applicable: … a deliberate proportionality exception, not an omission."* Donatism's four "not recoverable" entries (3A-1, 3A-2, 3B-1, 3B-2) are correctly counted.

**The Latin emendation at 2B-5 — verified, and the justification holds.** See the check-confirmation section; this is the finding I expected to survive and it did not.

**Counts and upstream pointers.** "8 of 19 entries carry an Author Gravity note" — `Lexicon_Deployment_Index.md` line 129 says exactly that. "Seven are registered at `Lexicon_Deployment_Index.md` §7" — the register has exactly seven rows. "The eighth is recorded only in `lpc_Decision_Log.md`" — the *ad nostra subsellia* tag is at `Doc_07` line 137 carrying no flag, is recorded at `lpc_Decision_Log.md` lines 1119 and 1155, and `subsellia` returns zero hits in `Lexicon_Deployment_Index.md`. So "a reader opening either destination finds seven and none" is exact. "Twenty stem occurrences of *confessor* across all eight vendored Augustine volumes" — `Doc_05` §2.3 and its §11 item 4 both say twenty, on a corrected sweep. Registry row 209 is Knöll CSEL 36; row 203 is Prosper's *Epitoma Chronicon* and does record both 430 and the 439 Carthage capture. `INTAKE.md`'s second limb exists in the words Doc_08 relies on. Doc_01 §6's Ongoing/Internal cell holds exactly three items, and all three survive as 2B-1, 2B-3 and 2B-4. "The shortest real Layer 2 in this document is 119" — measured by the generator's own rule, 1B-3 at exactly 119.

**Article 19 / invention.** No Layer 1 claim is asserted without a traceable source. The 133-year silence is held as a silence and nothing from Donatism's territory fills it. None of this round's findings is an invention finding: H1 and H2 are consistency failures, H3 is a stale status line, M2 is a register overclaim, M3 is a control defect.

---

## Job 2's harder question — what these controls would still miss

Eight mutations against the live Doc_08, each regenerating the Index, with a positive control included.

| Mutation | §5 stub | §6 | §7 |
|---|---|---|---|
| **Baseline (live, unmutated)** | clean | **CLEAN — and H1's contradiction is live** | AGREE |
| §7 relabels `1A-1` `(Contested)` against §3's `Documented` | clean | clean | **conflict correctly reported** ✅ |
| §7 relabels `1A-1` `(Inferential/Thin, on a re-read)` | clean | clean | **conflict correctly reported** ✅ |
| §5's G6 list *genuinely* carries `2B-1` while §3 disclaims it | clean | **CLEAN — missed** | AGREE |
| *(positive control)* §5 drops `2A-4` from G7 | clean | **1 flagged — caught** ✅ | AGREE |
| §3 asserts a connection §5 omits, verb outside `CONNECT` | clean | **CLEAN — missed** | AGREE |
| §3 asserts a connection with a known verb, sentence mentions "§5" | clean | **CLEAN — missed** | AGREE |
| A Layer 2 replaced with fluent modern-analytic prose | **clean — missed** | clean | AGREE |
| **A correction notice in §5 names a force ID in bold** (`3A-1` injected into G2) | clean | clean | AGREE — **and the master table and by-gravity table both silently gain the connection** |

**What NEW-H4's fix genuinely bought.** The §7 cross-check is now real across all five of the Constitution's confidence levels. Two of the three improvements Round 3 asked for landed and work.

**What is still invisible.** (a) A §3 claim that a force *does not* connect where §5 says it does — the live H1, still. (b) Any §3 connection claim whose verb is outside a seventeen-item list, or whose sentence contains `§5`, `neither`, `nor` or `not a` — measured at eight of twenty-one gravity-naming Layer-3 sentences in the live document, one of which is a live false negative printed as a false statement (**M3**). (c) A Layer 2 that is long, fluent and entirely in the analyst's register — which the Index says honestly. (d) Every hand-carried count and certification in Doc_08 §§8–9, and every self-description in its front and back matter — no control reads any of them, and two are currently false (**H3**).

**And one new class, which is the deepest finding of this round.** *The generator reads Doc_08's correction notices as data.* Every `[CORRECTED …]` / `[ADDED …]` notice in §5 that names a force ID in bold is an injection vector into both the by-gravity table and the master table, silently, with no control anywhere in the pair able to see it. Doc_08 currently carries **31** such notices and the Index **10**; three sit inside §5 itself. One of the three is live (`G6`); the other two happen to name IDs already in their lists. The §6 control already strips notices before parsing Layer 3 — the §5 parse does not, and nobody noticed because the two parses were written in different passes for different findings.

That is the build's recurring mechanism in its purest form: a document's *apparatus for recording what it fixed* became input to the derivation of the thing it fixed. The control that would catch it is the one Round 1 destroyed and Round 2 rebuilt — a second, independent derivation that is allowed to disagree — and it still only looks one way.

---

## A check I confirmed before trusting it, and two of my own that were defective

**The one I confirmed before reporting — H1.** An instrumented parse showing `G6: ['2A-3','2B-1','2B-4']` proves only that my regex and the generator's agree; it does not prove the delivered Index is wrong about the document. So before writing H1 I confirmed it on three further, independent paths: (1) a **mutation** that made §5's G6 list genuinely carry `2B-1` and produced a **byte-identical Index** — if the delivered file cannot be distinguished from the file that has the defect, the delivered file has the defect; (2) `git show` of the G6 row at all three fix commits, which is unchanged, so the row cannot have been regenerated from a corrected §5; (3) a plain read of §5's own sentence *"G6 keeps two connected forces"* against the Index's `3`, which needs no tooling at all. Had I stopped at (1) I would have reported a parser agreement as a document defect.

**The same discipline on M2.** My reconstructed seven-marker scan firing at 3B-1 and 3B-2 proves that build-voice register is present; it does **not** prove that §8's certification is false, because a defensible scan must exempt a marker the L4 template requires. So I re-ran it three more ways — notices stripped, marker paragraph exempted, and a wholly different criterion (grep for correction notices inside the world-voice span) — and only then could I say precisely what is wrong: the certification is unqualified where it needs one clause of scope, and one non-mandated clause genuinely does not belong. My first framing of that finding would have been a HIGH and would have been an overstatement.

**And on NEW-M2's closure.** `grep "siue in libris"` returning zero hits proves nothing on its own. I also grepped the alternative (`sine in libris`, one hit), dumped the raw span at lines 1508–1518, read the file's provenance header (which names *"letter confusions (V/Y, C/G, **u/n** and similar)"* as expected OCR noise — the claim Doc_08 makes), and read the **critical apparatus printed beneath the Prologus**, whose entry for that line is `(opus)cula — libris resecta H  epistolis CDEGHSV` — an entry that covers the exact span containing the word and records **no `sine`/`siue` variant**, only a mutilated manuscript and a spelling variant of *epistulis*. So Doc_08's claim *"the reading Knöll's text requires and his apparatus records no variant against"* is **true and checkable at the vendored file itself**, which is better than the fix instruction asked for. I then confirmed the OCR diagnosis independently: line 1916 of the same file reads *"non recolo **sine** in sacris litteris nostris **siue** in"* — the identical `siue → sine` error in an identical construction, 400 lines away, with no editorial significance whatever.

**My two defective checks, reported because a reviewer who reports only the checks that survived has concealed the base rate of their own instrument.**

1. **A finding killed by opening the intermediate source.** I flagged the `[A]` bracket in §5's G5 quotation of the Forces Framework as a misrepresentation: FF's sentence begins with a capital *A* at both loci (lines 176 and 200), so bracketing it tells the reader the original was lowercase. That would have been a COSMETIC finding, and it is wrong. Doc_08 attributes the quotation in the same sentence to Doc_04, and **Doc_04 line 97 quotes it mid-sentence with a lowercase *a***. The bracket is the correct way to restore the capital from that rendering. Caught only because the sentence names Doc_04 and I opened it.

2. **A count I declined to trust, and was right to.** My coverage measurement returns **21** gravity-naming Layer-3 sentences where the Index says **19**. My first instinct was a finding. But my sentence splitter, my gravity-token rule and my notice-stripping are all mine, and the Index's figure was taken on a different draft of the document. Reporting "19 is wrong" would have been the exact shape this build keeps producing — a check that measures something adjacent to the claim and is trusted because it returned a number. **L4 therefore reports the tense and the referent, not the arithmetic**, and says so.

A third, smaller one, caught in flight: my first sibling survey grepped for the literal string "construction-record" and returned zero across all eight siblings, which would have supported §8's claim for the wrong reason — a sibling could use an interposed block under any other name. I re-ran it as a structural parse of every Layer 2 → Layer 3 span looking for **any** interposed bold header, and it still returned zero. Only the second run supports the claim §8 makes.

---

## Is the deliverable adequate to proceed to Doc_09?

**No — but by less than three HIGH findings suggests, and by less than at any prior round.**

What is underneath the defects is a real Step 8 deliverable and has now been tested four times: seventeen forces correctly distributed across six populated cells; both transmission entries as named forces of their own with named agents, selection interests and stated exclusions; fifteen cross-cell connections with correct direction, one recorded non-connection and one explicitly non-causal coincidence; all eight confirmed gravities connected; confidence calibration correct force by force on independent re-derivation; eleven quotations verified to their containing works under the widened method; every governing-document quotation exact; every hand-carried count I tested accurate except the two review-status lines. The three rewritten Layer 2 entries read as prose and survive FF's governing test in their world-voice portions.

Doc_09 will take two things from here — the gravity–force connections, through the Index, and the transmission entries, which is where a story repository's tier justifications and its Absent Stories answer have to be grounded.

- **H1 is blocking.** Doc_09 will cite gravity–force connections and the Index is the intended lookup. `2B-1` and G6 are stated two ways in the delivered pair, and the Index is the one a builder will read. This must be settled before anything cites it — and settled against Doc_04 §6, not only against Doc_04 §3.
- **H2 is blocking for §5's integrity** rather than for Doc_09's content, but it falls out of the same edit as H1 and should not be separated from it.
- **H3 is blocking for disposition, not for Doc_09.** It is the cheapest of the three to fix and the one a project lead is most likely to act on wrongly.
- **M1, M2, M3, and the LOWs are not blocking.** They are defects in what the pair says about its own checks, and they should be fixed because the next reviewer will otherwise be invited to trust a control that prints a false observation and a certification that was not run in the form it claims.

**No new source research is required.** Everything above is settled inside files already open in this build.

---

## CO-022 escalation assessment

Checked against Doc_08's own Section 1 and Disposition, `lpc_Decision_Log.md`'s Doc_08 entries, and the sibling builds named.

**Representative identity, title, or voice — does not apply.** Confirmed. Doc_08 makes no identity, title or voice decision.

**Portfolio-level or cross-world — four items, none decided here, all accurately restated.** I re-verified each: the eighth editorial-apparatus instance (correctly attributed, with both destinations correctly described as showing seven and none); the *Boundary Structures* / *Boundary Ecology* inconsistency; the Key Texts / Key Sources template mismatch; the Doc_07 template's pre-M4 lens structure. The Markdown-versus-workbook observation is correctly closed at source — `CiC_Record_Native_World_Build_Process_V1_3.md` lines 156 and 160 say what Doc_08 says they say (see **C1** for the one word) — and "only one of twelve worlds carries a Force Index" is exact: twelve world directories, and `CiC_W1_Force_Index.xlsx` is the only other one.

**Governance or methodology — five items, correctly stated, and the new one is real.** I verified the fifth independently: three worlds do read the Forces Framework's three-layer rule three different ways, and two of the three readings sit in disposed documents. Donatism's four "not recoverable" entries and Alexandria's single "Layer 2 — not applicable" proportionality exception are both exactly as Doc_08 describes them. The L4 template's Proportionality carve-out and FF's own name-the-absence limb both bear on it, and both are quoted exactly. The construction-record block is properly attached to that item and is now **declared** rather than adopted silently, which is what Round 3's NEW-M5 asked for. This is a genuine portfolio question and lpc's own resolution — write the entries — remains the safest of the three however it is settled.

**Unresolved tensions — one open**, the 411 *Gesta*, confirmed relied on for nothing in this document.

**This review adds no escalation item.** All twelve findings are correctable inside this build thread's own editing authority. One observation belongs *with* the existing governance item rather than beside it: **the generator's reading of correction notices as derivation input is a method defect, not a local one.** lpc follows the `cic-forces-index` standard, which mandates a generated index; any world that adopts it and annotates its source document in place will inherit the same vector. If the standard is going to be generalised across the portfolio — and the Disposition observes that only one of twelve worlds currently carries a Force Index — then "strip in-place correction apparatus before deriving" belongs in the standard, not in one world's scratch generator. I attach it to the existing governance/methodology item rather than opening a category.

---

## On the brief that commissioned this review

Checked rather than accepted, per its own instruction. Everything material in it held: the generator is where the brief says and reproduces the committed Index byte-for-byte; four sentences were moved out of Layer 2 at 2B-5, 3B-1 and 3B-2 and the Reported-Experience markers were moved back in; the construction-record block was renamed and §8 now declares it a local departure; the generator was changed in the five places named; the Latin emendation is at 2B-5 and is now marked; Doc_08 carries 31 correction notices and the Index 10 ("roughly thirty"); the `DISCLAIM` pattern matches `\bneither\b`, `\bnor\b`, `\bnot a\b` and `§5` exactly as described; the Decision Log records twenty-five failing checks that were defects in the check; all three prior rounds' counts are correct, and Rounds 2 and 3 do each state that every one of their HIGH findings was introduced by the immediately preceding fix pass.

**Both of the fix pass's cited results reproduce.** Against `9eccc532` the current §6 control reports all three divergences — `1B-1`/G2, `2A-1`/G8 and `2B-1`/G7 — and against the live document it reports none; the stub side flags exactly three. Those claims are true as stated.

**Two corrections, one of which matters.**

1. **The brief's premise that "§5's G6 entry lost force `2B-1`" is true of Doc_08's prose and false of the deliverable pair.** The Index — the co-deliverable under review in the same breath — still carries it, and the correction notice that removes it is the reason why. The brief invites an assessment of "dropping it" as a completed act; it is not one. That is H1, and it is the finding the brief's own framing would have concealed if I had accepted the premise.
2. **The brief says the fix pass "claims … a seven-marker register scan returns zero across all seventeen Layer 2 blocks," and asks me to reproduce it.** The claim is made, at §8 and in the Decision Log, and it does not reproduce — six marker hits at two blocks. But the gap is narrower than a bare failure: with the template-mandated Reported-Experience marker paragraph exempted, the scan does return zero. The reproducible finding is an unstated exemption plus one non-mandated clause, not a wholesale false certification. That is M2, graded accordingly.

On the brief's question about whether G6 has an independent claim to `2B-1`: **it does**, at Doc_04 §6's Interaction Matrix, where Candidate 2 relates to Candidate 6 as *"Reinforcing (both are boundary/reintegration questions Cyprian reasons about consistently)"* and to Candidate 7 as *"Reshaped by."* The symmetry the fix pass relies on is Doc_04's Persistence finding and holds there; it does not hold at the Interaction Matrix. On what depends on it: §5's G7 single-force-origin finding **holds** and is unaffected; §6's Author-Gravity convergence claim **holds** and is unaffected; §9's completion check **holds** arithmetically but points a reader at a table that disagrees with §5; the Index's by-gravity table **is broken**; and §5's Cross-Strand Gravity Note — which the fix's own notice did not consider — **is falsified**.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**3 HIGH · 3 MEDIUM · 5 LOW · 1 COSMETIC — 12 in total.**

Thirteen of Round 3's fifteen findings are closed, several of them exactly, and the forces analysis underneath has now survived four rounds of independent testing with its substance intact. The §7 cross-check is genuinely repaired and mutation-proof across all five confidence levels. The Latin emendation is closed better than the instruction asked. The construction-record block is properly renamed, properly declared and properly escalated, and every factual claim in the declaration verifies against the L4 template and all eight sibling builds. The regression claims reproduce exactly.

**But for the fourth consecutive round, the serious defects are in what the fix pass itself wrote or failed to touch.** Round 3's headline HIGH was closed in Doc_08 §5's prose and nowhere else: the generator reads the bolded force ID out of the very correction notice that removes it, so the delivered Index still prints the connection the fix deleted, and a mutation that reinstates the connection produces a byte-identical file. The same removal falsified a claim in §5 that the removal's own notice certified nothing depended on. And the document's masthead still reads "DRAFT — not reviewed," and its last sentence still reads "it has not been reviewed at all," four lines after the pass adopted a standing discipline that the review-history lines are the first thing a fix pass touches.

**What I tested hardest, and which held:** the eleven quotations, rebuilt from the XML with note-marking and containing-work recovery on two corpora; the independent re-derivation of every Index table, which matches on seventeen master rows, seven of eight gravity rows and the full connection map; the Latin emendation, checked against the file's reading, its provenance header, Knöll's own apparatus at the locus, and an independent occurrence of the same OCR error; and §8's three claims about templates and siblings, which are exact.

**What I tested hardest and which failed:** the §5 gravity derivation, under instrumentation, mutation and git; the §6 control's new "both directions," under the exact scenario it was rebuilt to catch; and the Layer 2 register certification, under four scans, one of which told me my own first framing was too strong.

**Four edits close every HIGH: strip correction notices before parsing §5; settle G6 against Doc_04 §6 and restate the Cross-Strand note; fix the masthead Status line and the Disposition's last sentence; and — the discipline this pair has now needed four times — read the regenerated Index before committing it.**
