# World Profile — Round 2 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

**Document under review:** `lpc_World_Profile.md`, 16,295 words (`wc -w`), 772 lines, as at commit `178d358c`.
**Reviewer:** isolated adversarial pass. I did not write the document, I did not write Round 1, and I did not apply the fixes. I have no stake in this clearing.
**Round 1 under re-derivation:** `WorldProfile_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED, 5 HIGH · 8 MEDIUM · 6 LOW · 2 COSMETIC.

---

# VERDICT: **REVISION REQUIRED**

**1 HIGH · 6 MEDIUM · 6 LOW · 2 COSMETIC (new).**

**Of Round 1's 21 findings: 20 CONFIRMED FIXED, 1 PARTIALLY FIXED, 0 NOT FIXED, 0 FIXED WRONGLY.**

**The fix pass is, on the substance, good work, and I want that on the record before the findings.** I re-derived all five HIGHs from the primary sources rather than from the diff, and all five hold. The replacement quotation at Section 7 resolves verbatim in `anf05` by `title=`, outside every `<note>` span, correctly attributed to Celerinus and not to Cyprian, with the `(spiritual)` parenthesis intact. The Possidius–*De Mortalitate* link the whole of HIGH-1's fix now rests on is real: I verified it at both ends myself, in Weiskotten and in ANF's *De Mortalitate*, and it is a genuine second textual crossing of the 133-year gap. Registry row 27 is a primary, Native source writing inside the interval, exactly as the corrected text says. Both new force entries match `Doc_08` and `lpc_Force_Index.md` field for field. The Section 10 verification command now points at the right line and the passage is byte-identical. Every altered chunk quotation is restored to its chunk's own wording. The CO-022 exposure is clean at source — I opened `lpc_Decision_Log.md` itself, which Round 1 could not, and both quoted strings are there.

**What fails is almost entirely inside the ~3,300 words the fix pass added.** New text is where new defects live, and they did.

- **One new HIGH.** Section 4D's new ontology paragraph takes a finding Doc_04 makes about **G5's conciliar-authority question** and restates it about **G6 and G7** — and the restatement is directly contradicted by Doc_05 §5.3, an approved input, and by this document's own Section 3.
- **One new MEDIUM of this build's signature class.** Section 4F asserts that ordinary, non-factional presbyteral work is "essentially unattested here." Possidius chapter V, Native, vendored, Registry row 192 — the very file the fix pass now cites at three other sections — attests it in two sentences.
- **The new Section 11, which is the document's own completion gate, certifies things that are not true.** Its preamble miscounts its own boxes, its first item contradicts Section 1's temporal scope, and its second item certifies a name-match that Section 2's own preamble says does not hold.
- **The count-correction sweep was incomplete in exactly the way the brief predicted.** "Thirteen Section 5 entries" was corrected to "fifteen" in the same closing sentence where "six honest limits" was left standing against a Section 8 that now has eight.
- **One orphaned fragment** from the pre-fix text survives at Section 1, mid-sentence, the literal artifact of inserting without removing.

**The document is much closer than Round 1 left it.** Nothing here would mislead a Representative about its own evidence base in the way HIGH-2 and HIGH-3 would have. But Section 4 feeds the Capsule Core's philosophical ecology directly, and Section 11 is what gates the document downstream.

---

# Method — what I derived, and how

**I diff-checked nothing until I had formed my own view.** I read the document in full, read the template's Section 4, 8 and 11 in full, opened Doc_01 §1/§2/§7/§8, Doc_02 §1/§6/§7/§8/§9, Doc_04 §3/§4/§5/§7, Doc_05 §4/§5/§6.3/§6.5/§6.6/§9, Doc_07 §2B/§2C/§7/§8, Doc_08 §3/§5/§9, Doc_09 §7/§8, `Source_Registry.md` rows 1, 9, 15, 27, 122, 192, 194, 209, `lpc_Force_Index.md` §1–§4, `Lexicon_Deployment_Index.md` §3 and §7, `lpc_Gapped_Formation_Precedent.md`, `lpc_Decision_Log.md`, `Possidius_XIX-XXVII_Read_2026-09-15.md`, `Story-Chunks/lpcstory005`, and `don_World_Profile.md`'s Section 4 heading list.

Corpus work was done against the vendored files: `anf05_hippolytus-cyprian-caius-novatian.xml` (div resolved by `title=`, never by position; `<note>` spans marked and excised *before* tag-stripping, and separately searched on their own so I could say which side of the apparatus a string sits on), `npnf101`, `possidius_vita-augustini_weiskotten1919.txt`, `augustine_retractationes-lat_knoll-csel36.txt`.

I ran a **mechanical extraction of every quoted string in the document** — the sweep Round 1 named as warranted and did not run — and resolved each one. That is how NEW-6, NEW-10 and NEW-13 surfaced.

I re-ran the one verification command the document prints.

I looked at `git diff 64b07be4 178d358c` only after all of the above, to confirm which text was new and to hunt for the un-removed-original pattern. Where a finding below was diff-informed rather than source-derived, I say so.

---

# Round 1's 21 findings, re-derived

## HIGH-1 (gap-crossing exclusivity; "unread Possidius") — **CONFIRMED FIXED**

**Re-derived, not diff-checked**, at all five sites plus the G1 Confidence limb.

I verified the load-bearing new claim myself rather than trusting the read artifact. Possidius, `possidius_vita-augustini_weiskotten1919.txt` line 3877, chapter XXVII: *"the holy martyr Cyprian speaks on this wise in his letter which he wrote on Mortality."* The Profile's ellipsis (*"the holy martyr Cyprian… in his letter which he wrote on Mortality"*) correctly steps over *"speaks on this wise"*. I then verified the far end: the anecdote Possidius goes on to quote — the dying colleague and the youth *"venerable in glory and majesty"* — resolves in ANF's *De Mortalitate* in ANF's own wording (*"a youth, venerable in honour and majesty, lofty in stature and shining in aspect… You fear to suffer, you do not wish to depart; what shall I do to you?"*). **The second crossing is real and is verified at both ends independently of this build's own artifact.**

All five sites now read correctly: Section 3 (*"two demonstrated mechanisms, both textual"*), Section 5 Force 2B-4 (*"One of two demonstrated mechanisms"*), Section 5 Force 3B-2 (*"established by the force above and, independently, by Possidius quoting Cyprian's De Mortalitate"*), Section 4C (*"read at source on 2026-09-15… superseding Doc_07 §2C's earlier 'not been read in this build' state"*), and the Disposition.

Round 1's "Related" limb is also fixed: Section 2 G1 *Confidence* now carries Doc_04 §3 Candidate 1's own exclusion of the *Vita* from the Cross-Check, verified at Doc_04 line 34, and states that the Cross-Check has not been re-run.

*But see NEW-5: the correction creates a silent divergence from Doc_08 Force 2B-4 and Doc_09 §7 item 1, both of which still say "only," and the Disposition still denies that any such divergence exists.*

## HIGH-2 ("no Registry row inside the 133 years") — **CONFIRMED FIXED**

**Re-derived, not diff-checked.** All three sites (Section 1 temporal scope; Section 5 Force 3B-2; Section 8 Domain 6) now carry the identical corrected block, and I confirmed by a duplicate-sentence sweep that no un-corrected variant survives anywhere in the file.

`Source_Registry.md` row 27 verified at source: Optatus of Milevis, *Against the Donatists*, marked **P**, **Native**, corpus map `role: tradition` — exactly as the Profile states. Doc_09 §7 item 1 verified verbatim, including *"The silence is a subject-matter gap and a build choice, not an empty archive."* The Doc_02 §7 scoping caveat the Profile now adds (*"whose 'no primary source' limb is scoped to its own §1 narrative"*) is accurate.

*But see NEW-14: at Section 1, the insertion left the pre-fix sentence's tail dangling.*

## HIGH-3 (non-episcopal silence asserted at a scope the corpus refutes) — **CONFIRMED FIXED**

**Re-derived.** Section 4B now reads *"what is missing is not the un-hostile record but any ordinary congregant writing about ordinary congregational life as such"* and names Epistles XX–XXI as the lay first-person voice. Section 8 Domain 1 carries Doc_09 §7 item 2's carve-out in full. The Representative handling line no longer denies a voice the world has; it now names the two confessors' letters before naming the limit.

`Source_Registry.md` row 1's Licensed-For column verified at source: *"Epistles XX–XXI ("Celerinus to Lucian" / "Lucian Replies to Celerinus") specifically, as this world's own lay-confessor first-person voice, licensed for Doc_02 §6's Article 20 discharge."*

*Residual: NEW-13 — Domain 1 attributes a "near-total" hedge to Doc_07 §2B, which states the claim flatly.*

## HIGH-4 (fabricated confessor quotation) — **CONFIRMED FIXED**

**Re-derived at source, by the exact method the brief specified.**

I located the letter by `title=`, not by position: `anf05_hippolytus-cyprian-caius-novatian.xml` line 30529, `<div3 id="iv.iv.xx" n="XX" … title="Celerinus to Lucian." type="Epistle">`. I marked and excised all eleven `<note>` spans in the letter **before** stripping tags, then searched the remaining body.

Both clauses are present, exact, and outside every note span:

> Know, nevertheless, that **I am placed in the midst of a great tribulation**; and, as if you were present with me, I remember your former love day and night, God only knows. And therefore I ask that you will grant my desire, and that you will grieve with me at **the (spiritual) death of my sister, who in this time of devastation has fallen from Christ**

**Attribution is correct** — the letter is Celerinus's, not Cyprian's, and the Profile says so. This is the intra-corpus misattribution trap the brief named, and it is avoided.

**The `(spiritual)` parenthesis is preserved.** `lpcstory005` line 49 records that it is *"the single word that establishes the sister is alive, so it stands."* It stands.

The fabricated string is gone. `grep` for *"and my brother stood"* across `cic/texts/` returns zero, as Round 1 said, and the string no longer appears in the Profile.

## HIGH-5 (Section 11 absent) — **CONFIRMED FIXED** (the section is present; three of its answers are not true — NEW-3)

**Re-derived against the template.** Section 11 is present with exactly eleven items, and I compared each against `L4-Templates/World_Profile_Template.md` lines 582–603: the eleven map one-to-one, in order, with the template's own wording preserved. The Disposition's *"ten template sections"* is corrected to *"eleven."*

The section itself is honestly framed in principle — Section 9 and the cross-reference sweep are left unchecked with reasons — which is the section doing its job. **What is wrong is inside it**, and it is a separate finding.

## MEDIUM-1 (Doc_04 §7 Open Item 8 presented as open) — **CONFIRMED FIXED**

**Re-derived.** Doc_04 §7 item 8 opens **"CLOSED, 2026-09-15, on the gapped-formation precedent handed to this build thread by the project lead (`lpc_Gapped_Formation_Precedent.md` §4b)"** and contains, verbatim as the Profile quotes it, *"Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding."* Item 6 opens **"CLOSED AS A PERSISTENCE QUESTION, 2026-09-15… (§4a)."** Section 2 G5 now states item 8 closed; the Disposition states both closed; *Unresolved tensions* now names the Article 3 question instead. Correct.

*Minor: the Disposition says "this document states them as closed at Section 2," which is true of item 8 only, and flattens item 6's "AS A PERSISTENCE QUESTION" qualifier. Not raised as a separate finding.*

## MEDIUM-2 (omitted open items) — **CONFIRMED FIXED**

**Re-derived.** `lpc_Gapped_Formation_Precedent.md` verified: received 2026-09-15 from the project lead, handed directly to this build thread; §1 is headed *"The open question this document does not close"* and quotes the Step 0 Conclusion's *"Checked directly against the Constitution's actual text and found genuinely undefined."* The Article 3 question is now named twice — Section 11 outstanding item 3 and the Disposition's *Unresolved tensions* — with the precedent cited.

Doc_07 §8 item 4 verified: three portfolio-level items (editorial apparatus; *Boundary Structures* / *Boundary Ecology*; Key Texts / Key Sources) and four governance/methodology items. All three portfolio items are now named. Doc_07 §8 item 8 (liturgical material) is carried as Section 8's new Domain 8.

*But see NEW-8 for the counts, and NEW-7 for how Domain 8 is written.*

## MEDIUM-3 (Section 4's four required dimensions lacked their content) — **CONFIRMED FIXED**, with a new HIGH introduced inside the fix

**Re-derived against the template's own bracketed requirements at lines 248–296.**

- **Emotional (§4B):** the template asks for entry, middle and maturity. All three are now supplied, honestly scoped to the bishop's side with the limit named. Adequate.
- **Philosophical (§4D):** the template asks for "most real, most given, most foundational" and for the human person's "fundamental problem" and "fundamental possibility." All four are now supplied and are genuinely derived from what the world fought about. Adequate — **except for the paragraph's closing disclosure, which is NEW-1.**
- **Authority (§4F):** the template asks what *grounded* authority and what formation from an authorized teacher conferred. Both are now supplied, both correctly sourced to Doc_05 §4.1 and §4.2 (verified at source, including *"your suffrage and God's judgment"* / *"not the same office for both"* and the *"bishop of bishops"* / plenary Council pair). Adequate.
- **Boundary (§4H):** was already adequate.

## MEDIUM-4 (false claim to follow Donatism's Section 4 layout) — **CONFIRMED FIXED**

**Re-derived.** I listed `don_World_Profile.md`'s Section 4 headings directly: 4A Emotional Texture (§2B), 4B Philosophical Ecology (§2D), 4C Authority Structures (§2F), 4D Boundary Structures (§2H), 4E Ritual/Practical (§2A), 4F Narrative/Mythic (§2C), 4G Ethical/Legal (§2E), 4H Material (§2G). The Method Note now correctly states the layouts differ and describes Donatism's accurately — *except for a count, NEW-9.*

## MEDIUM-5 (`sed -n '221p'` verified nothing) — **CONFIRMED FIXED**

**Re-derived by re-running the command as printed.** `sed -n '222p' Doc_07_Integrated_Ecology_Analysis.md` now returns the full 130-word Integrative Observation. I then diffed it against Profile line 712: **byte-identical.** The Status field's *"Verbatim"* is correct and the printed check is now a check.

## MEDIUM-6 ("with a certain judicial severity" unattributed) — **CONFIRMED FIXED**

**Re-derived at source.** `augustine_retractationes-lat_knoll-csel36.txt` line 1512 reads *"tractatibus cum quadam iudiciaria seueritate recenseam"*, line 1510 *"opuscula mea sine in libris siue in epistulis siue in"*. The Profile now carries the Latin as the quotation, the English as an inline gloss, the *Retractationes*, Prologus citation, the row 209 second-witness caveat, and the statement that the English is this build's own rendering. This matches Doc_08's handling exactly. *(The printing's OCR "sine" for the first "siue" is normalised, as Doc_08 also does; not raised.)*

## MEDIUM-7 (13 of 17 forces, undisclosed; the Contested force dropped) — **CONFIRMED FIXED**

**Re-derived against `lpc_Force_Index.md` §1–§2 and `Doc_08_Forces_Document.md` §3 and §9.**

- Count: the Profile carries **15** `**Force:**` entries (`grep -c`), against Doc_08's **17**. Arithmetic holds.
- The two named omissions are right: **1A-2** (unlicensed-religion legal condition, Widely Accepted, G1) and **1B-3** (inherited Latin theological vocabulary, Widely Accepted, G4) — both verified against Index §1 row for row, including confidence and gravity.
- **2A-1** — Index: Ongoing/External, Documented, G1/G4/G8. Profile: identical, and its Layer 3 tracks Doc_08's own Layer 3 closely (*"ends the first phase's documentary record, which is why G2 and G8 are attested only within it"*). Its Confidence line's sourcing (*Doc_01 §2; the* Acta Proconsularia *within Registry row 194*) is Doc_08's own, and row 194 does contain the *Acta*.
- **2B-3** — Index: Ongoing/Internal, **Documented *(+Contested)***, connected gravities **—**. Profile: identical, including "none advanced." Its Layer 2 quotation (*"Cyprian never asked the magistrate for anything; a century and a third later the magistrate could be asked, and eventually was"*) is verbatim from Doc_08's Layer 2. The Contested element's description matches Doc_08's entry, and **Doc_08 §9's outstanding item 4** exists and says what the Profile says it says.
- Confidence profile: Index §2 gives **14 Documented, 3 Widely Accepted, 0 Contested with 2B-3 carrying it as a secondary element.** The Profile's preamble states this correctly, including *"This is the only force in the matrix carrying a Contested element."*
- All six cells remain occupied: 1A(1), 1B(2), 2A(4), 2B(5), 3A(1), 3B(2).

*Structural nit at NEW-12.*

## MEDIUM-8 (Doc_09 §7 item 3 omitted from Section 8) — **CONFIRMED FIXED**

**Re-derived.** Section 8 Domain 7 now carries item 3 in its own terms, including *"not one of them left an account of why"* and *"Ep. XX names Numeria and Candida."* I verified the Numeria/Candida detail independently in the letter itself: *"our sisters whom you also knew well—that is, Numeria and Candida."* Doc_09 §7 item 3 verified verbatim at source.

## LOW-1 (four citation-locus errors) — **PARTIALLY FIXED**

**Re-derived, all four.**

- G1 *Grounding*: *"the ecological hub"* is now attributed to **Doc_05 §9.1**. ✅
- G5: now quotes *"thin across the span, not bounded within it"* and cites **Doc_04 §5** — I confirmed that is §5's wording (line 169) and that §4's table cell reads *"rather than"*. ✅
- Section 3 and G3 *Brief description*: now cite **Doc_08 §5**, and the quotation is no longer truncated. ✅
- **Section 2 G3 *Grounding* (line 92) still reads:** `Doc_08 §5, §9.2 ("every force connected to G3 is a force that tested it")`. ❌ **Doc_08 has no §9.2** — `grep` for `9.2` in `Doc_08_Forces_Document.md` returns zero hits, and §9 is the Completion Certification checklist. The sentence is at Doc_08 §5 line 326. The quotation here also still truncates *"rather than produced it"* without an ellipsis. **One of four sites not fixed.**

## LOW-2 (two altered chunk quotations) — **CONFIRMED FIXED**

**Re-derived against the chunks.** `lpclex002` line 35: *"there is a road, it is walked in the open, and it ends inside"* — the Profile now matches. `lpclex005` line 41: *"nearly everything touches it"* — the interpolated *else* is gone.

## LOW-3 (Doc_01 §1 quoted for "Status: PENDING") — **CONFIRMED FIXED**

**Re-derived.** Doc_01 line 20: *"**Living Tradition Status:** Not confirmed."* Doc_01 line 178 (§8 item 8): *"Remains PENDING project-lead confirmation."* Section 9 now quotes both, each to the right locus.

## LOW-4 (four [AS] terms implied to be the set) — **CONFIRMED FIXED**

**Re-derived.** `Lexicon_Deployment_Index.md` §3: **[AS] Signature Vocabulary — 6**, and the two the Profile names as not carried (*libelli*, *libellatici* / *sacrificati*) are the correct two. I also re-checked all eleven of Section 6's tag strings against §3's seven tag lists, including the negatives: **all eleven match.**

## LOW-5 (*libellus* disclosure dropped) — **CONFIRMED FIXED**

The `lpclex017` Evidentiary disclosure is now carried in full at Section 4A, including that the Latin headword is absent from the vendored English corpus and that the word-family's single occurrence sits in the Introductory Notice to the anonymous treatise against Novatian (Registry row 8), not in *De Lapsis*. Doc_06's carried M-N3 is named. Section 4G no longer cites the chunk.

## LOW-6 (length undisclosed) — **CONFIRMED FIXED** as a disclosure

The Method Note's new third paragraph discloses the overrun, names Doc_07 §8 item 10's remedy (quotation verified), and states the condensing pass has not been run. *But see NEW-11 for the figures.*

## COSMETIC-1 (G1 name differs from Doc_04 §4) — **CONFIRMED FIXED** at Section 2, **reintroduced at Section 11** — see NEW-3(c)

## COSMETIC-2 (Feeds line) — **CONFIRMED FIXED**

Now reads *"**Doc_09 Story Inventory is an input here, not a feed** — it was built before this document and supplies ecological context to it, inverting the template's own assumed order."*

---

# NEW FINDINGS

---

## NEW-1 (HIGH). Section 4D attributes to Doc_04 a finding about **G5** and restates it about **G6 and G7** — where Doc_05 §5.3 says the opposite, and so does this document's own Section 3

**Where.** Section 4D, in the new ontology/anthropology paragraph the MEDIUM-3 fix added:

> **One disclosure belongs with this.** Doc_04 finds **no evidence in Doc_02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, the theoretical question** underneath **G6 and G7**; Doc_05 §5 does not narrate it as part of anyone's formation.

**What is wrong.** The finding is Doc_04's, the wording is nearly verbatim — and it is about **Candidate 5's conciliar-authority question**, nothing else.

**Evidence, derived at source.** `Doc_04_Gravity_Discovery.md` line 92, inside **Candidate 5's Formation test**:

> **Formation:** Does not clearly pass. This document finds no evidence in Doc_02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, **this specific theoretical question**.

Both downstream users of that finding scope it the same way. `Doc_05_Ecological_Reconstruction.md` §4.2, under the heading *"What G5 does and does not do in this ecology"*: *"What it does **not** do… is reach ordinary formation: Doc_04 finds no evidence… of this specific theoretical question, and §5 below does not narrate it as part of anyone's formation."* `Doc_07_Integrated_Ecology_Analysis.md` §3C applies it to *"Neither conciliar formula (G5)"* and to nothing else.

**Three separate things break when it is transposed to G6 and G7.**

1. **Doc_05 §5.3 states the contrary in terms, about G7 specifically:** *"an ordinary believer at Hippo in the 420s **is being formed by this material**; an ordinary believer at Carthage in the 250s is not."* §5.3 also calls G7 *"a sustained catechetical and polemical formation project across thirteen dedicated works."* Doc_05 is an approved input and the Profile cites §5 in the same sentence that contradicts it.
2. **The Profile contradicts itself.** Section 3, *Formation Logic and the Confirmed Gravities*: *"G7 (grace) is formation **content** rather than formation medium — the one gravity that is itself a sustained catechetical and polemical project, **propagated through G4's own channel**."* Section 6, *grace*, gives it the highest raw textual frequency of any term swept. Content propagated through the catechetical channel is, by this document's own account, exactly what ordinary believers were formed by.
3. **The second clause is false on its face.** *"Doc_05 §5 does not narrate it as part of anyone's formation"* — Doc_05 §5.3 **is** §5, and it narrates precisely that.

**Why HIGH rather than MEDIUM.** It is a sourced claim, in a paragraph written to satisfy a Round 1 finding, that an approved input directly refutes — the failure class that accounts for 8 of 11 HIGHs across this build's Doc_09 rounds and 4 of 5 in this document's own Round 1. Section 4D feeds the Capsule Core's philosophical ecology. And it is a *silence* claim: a Representative built on it will understate what its own densest textual object did to the people it was preached at.

**Fix.** Either restore the finding to G5, where Doc_04, Doc_05 and Doc_07 all put it, or — if a disclosure genuinely belongs on the ontology paragraph — write one that says what Doc_04 actually supports: that the *ontology stated above* is what the disputes presuppose rather than a catechism anyone was taught. That last clause is already in the paragraph and is the defensible half. The G5 sentence in front of it is the problem.

---

## NEW-2 (MEDIUM). Section 4F: "the ordinary, non-factional work of a presbyter is essentially unattested here" is refuted by Possidius chapter V — Native, vendored, row 192, the same file the fix pass now cites three times

**Where.** Section 4F, closing sentence:

> The presbyters appear in this record almost exclusively as faction (five in recorded opposition to Cyprian's election) — a real distortion in the institutional picture, since **the ordinary, non-factional work of a presbyter is essentially unattested here.**

**What is wrong.** `possidius_vita-augustini_weiskotten1919.txt`, chapter V, in this world's own Native vendored corpus:

> Therefore he gave **his presbyter the right of preaching the Gospel in his presence in the church** and very frequently of holding public discussions — contrary to the practice and custom of the African churches. On this account some bishops found fault with him…

and, four sentences later:

> And after the report of this had rapidly spread by reason of the good example which preceded it, **some other presbyters by permission of their bishops began to preach to the people in their presence.**

That is ordinary, non-factional presbyteral work — preaching by episcopal permission — attested twice, once for Augustine at Hippo and once as a practice spreading to unnamed presbyters elsewhere. The Latin at line 1895 reads *"accepta ab episcopis potestate, presbyteri nonnulli coram episcopis populis tractare coeperunt."*

**Why this is a real finding and not a quibble.** Round 1 listed this exact sentence at item 8 of *What I did NOT check* — *"traced to their upstream statements but did not independently test against the corpus."* I tested it. The fix pass read `Possidius_XIX-XXVII_Read_2026-09-15.md` and wired its findings into Sections 3, 4C and 5 — but did not carry the read back to any other claim in the document, and this is the one it most directly touches. The build's own documented failure mode is a silence asserted about a source that the source refutes; the source here is the one the build just finished reading.

**The hedge does not cover it.** "Essentially unattested" would cover an inference or a passing mention. It does not cover a named grant of preaching rights plus a reported practice spreading among other presbyters.

**Fix.** Either narrow the claim to Cyprian's phase, where it is defensible on the Epistles, or state it as Doc_07 §2F's finding and note Possidius ch. V against it. The wider point — that the institutional picture is distorted toward faction — survives either way.

---

## NEW-3 (MEDIUM). Section 11's own answers are wrong in three places, in the section that is the document's completion gate

**(a) The preamble miscounts its own boxes.** Section 11 opens: *"Three items cannot be checked, and saying so is the point of having this section."* There are **nine `- [x]` and two `- [ ]`** (`grep -c`). Two items are answered as not-checkable — Section 9 and the cross-reference sweep — not three. The brief that commissioned this review inherited the error and asked me about "the eight checked items"; there are nine.

**(b) Item 1 contradicts Section 1 and Doc_01.** It reads *"temporal and geographic scope — **c. 248–430**, Roman North Africa."* Section 1's *Temporal scope* reads *"**c. 246–430** CE."* `Doc_01_World_Identification_Boundaries_Orientation.md` line 24: *"**Approximate Time Horizon:** c. 246–430 CE."* Section 1 is right; the checklist item that certifies Section 1 is wrong.

**(c) Item 2 certifies a name-match that Section 2 says does not hold.** It reads *"classifications match Doc_04 §4 **by name** and type."* Section 2's own preamble, three hundred lines earlier, says: *"**G1 is named here 'Pastoral Office as Territorial Flock-Keeping'**… Doc_04 §4's own cell reads 'Pastoral Office as Flock-Keeping.'"* I confirmed both strings occur exactly once each in Doc_04. This is Round 1's COSMETIC-1, correctly disclosed at Section 2 and then flatly contradicted by the checklist the fix pass added.

**Why MEDIUM.** Section 11 is the section the template's Final Assembly Instruction makes mandatory *because* it is the self-audit. A self-audit that miscounts its own boxes and certifies a match the document itself disclaims is not doing the job it was added to do.

---

## NEW-4 (MEDIUM). The closing line still says "six honest limits"; Section 8 now has eight — the count corrected in one clause of the same sentence and left standing in the next

**Where.** The document's final line:

> *…fifteen Section 5 entries covering forces across all six cells… two tensions held, not resolved; **six honest limits** named as this world's own character…*

**What is wrong.** `grep -c '^\*\*Domain:\*\*'` returns **8**. The fix pass added two domains (MEDIUM-8's lapsed domain and MEDIUM-2(c)'s liturgical domain) and Section 11 item 8 correctly says *"in eight domains."*

**This is diff-confirmed as well as source-derived.** The same sentence's *"thirteen Section 5 entries"* was updated to *"fifteen"*; *"six honest limits"*, eleven words later, was not. This is precisely the inverse of the Donatism Round 2 failure mode the brief asked me to sweep for — a value corrected at one site and left at another inside a single sentence.

---

## NEW-5 (MEDIUM). The Disposition still asserts that no two prior `lpc` documents disagree — which the HIGH-1 fix itself falsified

**Where.** Disposition:

> **No place was found where two prior `lpc` documents disagree and this document had to choose between them.**

**What is wrong.** The fix pass created exactly such a place, and did not amend this sentence.

**Evidence.** `Doc_08_Forces_Document.md`, Force 2B-4, Layer 3, still reads in bold: *"**This is the only mechanism by which this world's formation logic demonstrably crosses its own 133-year silence.**"* `Doc_09_Story_Inventory.md` §7 item 1 still reads: *"Doc_08 §3B-2 records that **the only thing crossing the gap is a text**: Augustine reading Cyprian's conciliar acts."* Against these, Doc_09 §7 item 5 and §8 item 9 record the Possidius read and the artifact records the second link.

The Profile chose — correctly — and now says *"two demonstrated mechanisms"* at three sites. That is a choice between two prior documents. The Profile discloses the supersession of **Doc_07 §2C** at Section 4C (*"superseding Doc_07 §2C's earlier 'not been read in this build' state"*) but discloses nothing about Doc_08 2B-4 or Doc_09 §7 item 1, and then denies at the Disposition that any such case exists.

**Fix.** Either delete the blanket sentence or replace it with the one real case, named: Doc_08 Force 2B-4 and Doc_09 §7 item 1 both state the crossing as singular; Doc_09 §7 item 5 and §8 item 9 supersede them; this document carries the later record and says so.

---

## NEW-6 (MEDIUM). Two new citation-locus errors, both on quoted strings, both in fix-pass text — the class Round 1 flagged as LOW-1

**(a) Section 4B.** *"Doc_05 **§5**'s own inhabited rendering of that state — this build's reconstruction, not a source quotation — is **"A man given a people does not get to be calm about them."**"*

The string occurs once in the project, at `Doc_05_Ecological_Reconstruction.md` **line 243**, inside **§6.5 Emotional and Affective Ecology** (heading at line 237). Doc_05 §5 is *Ministry and Formation Ecology*; its own Inhabited block (line 191) is a different passage entirely (*"You are taught before you are washed…"*). The characterisation as this build's reconstruction is correct — §6.5's construction note marks it Tier 4 — but the locus is not.

*Secondary:* §6.5's construction note says the passage is *"Composed from three attested affects"*, i.e. the bishops' affective register as a whole. Section 4B deploys it specifically as the rendering of **maturity**. That is a mild over-read of a Tier 4 composite.

**(b) Section 4F.** *"**Doc_05 §6.3** finds that transmission between this world's two phases happens **through texts read later, not through a continuous teaching succession this build can evidence**, and records that as a structural feature rather than a shortfall."*

That wording is **§6.6 Meaning Transmission**'s, not §6.3's: *"Transmission between phases happens through **texts read later**, not through a continuous teaching succession this build can evidence (§6.3). That is a genuine structural feature of this world's meaning transmission and is recorded as a finding rather than as a shortfall."* §6.3 *Memory Structures* makes the adjacent point about memory but neither of the two bolded phrases is its. (§6.6's own back-reference to §6.3 is presumably how the slip happened.)

**Why MEDIUM and not LOW.** Round 1 raised four of these as a single LOW. The fix pass fixed three of the four (see LOW-1, above), left the fourth, and introduced two more in the text it wrote to close other findings. Two new instances of a defect class a review just named is a pattern, not a slip.

---

## NEW-7 (MEDIUM). Section 8's new Domain 8 is an unperformed build task written as a formation limit, and its handling line is meta-commentary about sources — both of which the template's Section 8 explicitly excludes

**Where.** Section 8, Domain *"The liturgical material, never read as liturgical evidence"*:

> **Ecological basis:** Doc_07 §8 item 8, carried open: the liturgical material *"has never been read as liturgical evidence"* (Doc_02 §9 item 9), and given §2A's finding that this world's crises **are** rite disputes, that document calls it *"the highest-value unblocked task in the build."*
>
> **How the Representative handles it:** What we did when we gathered, I can describe from what our disputes assumed rather than from an order of service anyone wrote down. **The shape of the rite is inferred from the arguments about it, and that is a weaker footing than it sounds.**

**What is wrong.** The template governs this section tightly, and for a stated reason — *"This section directly governs the Representative's Honest Limits section in the Permanent Prompt."*

- On the basis: *"named as natural formation depth variation, **not as AI or documentation limitation**… not 'the evidence does not support reconstruction here' but 'this world's own life did not run deep in this area.'"* The template lists the permitted bases: thinness of sources in Doc_02; strand attribution; the world's own life not concentrating deeply; transmission thinness. **"A task in this build has not been performed yet" is none of them** — and it is weaker than any of them, because it is a statement about the build's schedule. *"The highest-value unblocked task in the build"* is a work item, quoted into a section that governs a Representative's in-character silences.
- On the handling line: *"Not apology, not disclaimer, **not meta-commentary about sources**."* *"That is a weaker footing than it sounds"* is meta-commentary about sources, in the Representative's own voice. It also switches from the template's required *"we"* voice to *"I"* mid-sentence. (Domain 7's *"none of that came down to us, and I will not supply it"* does the same, less severely.)
- **Section 11 item 8 nevertheless certifies all eight domains as *"stated as natural formation character… not as construction gaps or AI limitations."*** For Domain 8 that is not true, and for Domain 4 (*"this construction pass has not independently verified it — no site report, inscription catalogue, or excavation record has been checked at source"*) it is barely true.

**I checked that the coverage is otherwise right.** Doc_07 §7's four named thin domains (ordinary believer's interior life; rural and Punic/Berber life; the physical setting of worship; the 133-year interval) plus §2C's narrative thinness and §2G's material thinness all have entries, and Doc_09 §7 items 2, 3 and 4 all have entries. Item 5 is correctly dropped as answered by the Possidius read. **Section 8's coverage is complete.** The problem is how Domain 8 is written, not that it is there.

**Fix.** Rewrite Domain 8's basis as a source-thinness statement — this world left no order of service, and the rite is known from the arguments about it — and carry the unread-as-liturgical-evidence item where it belongs, in the outstanding-items list at Section 11, which already has four. Rewrite the handling line in the "we" voice without the evidentiary aside.

---

## NEW-8 (LOW). The escalation assessment's counts do not reconcile with what it names

- Disposition, *Portfolio-level or cross-world:* **"none decided here, four carried open"** — then names **three**, all from Doc_07 §8 item 4 (editorial apparatus; *Boundary Structures* / *Boundary Ecology*; Key Texts / Key Sources). Doc_07 §8 item 4 carries exactly three portfolio-level items; I verified this at source. There is no fourth.
- Section 11, outstanding item 5: **"The four portfolio and governance items carried from Doc_07 §8 item 4."** Item 4 carries **three portfolio-level items plus four governance/methodology items = seven**. The Disposition's own next sentence gets this right (*"**none introduced here; four carried** from Doc_07 §8 item 4"* for governance); Section 11's summary of the same thing does not.

---

## NEW-9 (LOW). The Method Note miscounts Donatism's Section 4

> *`don_World_Profile.md` keeps the template's four named dimensions in the template's own 4A–4D slots and **appends the five further lenses at 4E–4H**…*

4E–4H is four slots and holds four lenses: Ritual/Practical (§2A), Narrative/Mythic (§2C), Ethical/Legal (§2E), Material (§2G). I listed them from the file. The ninth lens, Formation Logic (§2I), is not in Donatism's Section 4 at all — as the Profile's own next clause about `lpc`'s Section 3 implies. "Five" is wrong on either reading.

---

## NEW-10 (LOW). Two template claims that do not resolve against the template

**(a) Section 4 preamble:** *"…and Boundary Structures is `§2H` (4H below), **unchanged in letter from the template's own assumption**."* The template sources its 4D Boundary Structures to **"Doc_07 Section 2D"** (line 295). Neither the slot letter (4D → 4H) nor the lens letter (2D → 2H) is unchanged. *(Pre-existing text, not fix-pass; Round 1 did not test it.)*

**(b) Method Note, second paragraph:** *"The template cites Doc_07 **"§2A–§2E"** for lens content…"* — in quotation marks. That string does not occur in the template. The template cites Doc_07 Section 2A, 2B, 2C and 2D for its four lens dimensions and reserves **Section 2E for Formation Logic**, which is the Profile's own Section 3, not Section 4. The range as quoted conflates the two. The rest of the paragraph — the correction of *"§5 Integrative Observation"* and *"§6 Gaps and Limits"*, and the enumeration of Doc_07's actual current headings — I re-derived and it is accurate. *(Pre-existing text.)*

---

## NEW-11 (LOW). The length disclosure's figures and comparison set

The Method Note states *"roughly **16,403**, the longest World Profile in the portfolio (don 9,430; ijc 4,615; hal 4,605; cappadocian 3,342)."*

- `wc -w` returns **16,295**. "Roughly" covers a 0.7% gap; I note it only because the parenthetical figures are given to the unit.
- **The comparison set is not the portfolio.** `World-Builds/Syriac-Christianity-Edessa-Nisibis/syr_World_Profile.md` is **10,704** words — the actual second-longest, ahead of Donatism — and `World-Builds/Alexandria-Catechetical-School/alex_World_Profile.md` is 1,768. Neither is listed. The headline claim (*longest in the portfolio*) is still true. The list presented as evidence for it is not the field. *(Round 1's LOW-6 used the same incomplete set; the fix pass carried it forward.)*

---

## NEW-12 (LOW). Section 5's two added force entries sit under the "Transmission forces" heading and out of cell order

Section 5 runs 1A → 1B → 1B → 2A → 2A → 2A → 2B → 2B → 2B, then the standing heading **"Transmission forces (Cells 2B and 3B):"**, then 2B-5, 3A-1, 3B-1, 3B-2 — and then the two new entries, **2A-1** and **2B-3**, appended after 3B-2, still nominally under the transmission heading. Neither is a transmission force. A reader checking the preamble's *"at least one per occupied cell"* against a cell-ordered list will read the section as ending at 3B-2. *(The heading already over-covered 3A-1 and 3B-1 before the fix; the fix made it worse rather than repairing it.)*

---

## NEW-13 (LOW). Section 8 Domain 1 attributes to Doc_07 §2B a hedge Doc_07 §2B does not carry

Domain 1: *"Doc_07 §2B finds this world's asymmetry is not hostile mediation… but **the near-total absence of any non-episcopal voice**."*

Doc_07 §2B states it without the hedge: *"What is missing is not the un-hostile record but **the non-episcopal one**: the interior life of any ordinary believer in this world is Inferential/Thin and is narrated nowhere in this build."* That unhedged sentence is what Round 1's HIGH-3 found false. Softening it silently and attributing the softened form to §2B papers over the upstream error rather than recording it. The carve-out that follows in the same paragraph is correct and does the real work; the attribution should say Doc_07 §2B states it flatly and Doc_09 §7 item 2 narrows it.

---

## COSMETIC-1. An orphaned fragment from the pre-fix text survives at Section 1

Section 1, *Temporal scope*:

> …the interval's documented material being the neighbouring Donatism world's own territory. **— a genuine silence in *this world's own* documentary record**, not a period in which nothing happened…

A full stop followed immediately by an em-dash continuation. This is the tail of the pre-fix sentence whose head was replaced: the corrected block was inserted and the original's remainder was not repaired. Diff-confirmed. The parallel insertions at Section 5 (3B-2) and Section 8 (Domain 6) both read cleanly; this is the one site where the seam shows.

## COSMETIC-2. Three smaller things

- The Method Note opens *"**The template is stale in two ways, and both are disclosed here**"* and then presents three bolded paragraphs (*First*, *Second*, *Third*). The third is a departure this document makes, not a template staleness — which the paragraph itself says — but the count in the topic sentence was not updated when it was added.
- Force 3B-2 states the Donatism-territory point twice in one paragraph (*"the interval's documented material being the neighbouring Donatism world's own territory"* and *"the interval is richly attested through sources that are the neighboring Donatism world's own territory"*), a redundancy created by the HIGH-2 insertion.
- The same sentence spells it *neighbouring* and *neighboring*.

---

# What I checked and found CLEAN — at the scope I actually checked it

**Every quoted string in the document, mechanically extracted and resolved.** I pulled all 68 distinct quoted strings of 12 characters or more by regex and chased each one. Beyond the loci reported at NEW-6 and NEW-10(b), **all resolve verbatim to the source named**, including every string the fix pass added. This is the sweep Round 1 named as warranted before clearing and could not run; it is now run, and it is the reason I can say the remaining defects are not more fabricated quotations.

**The Cyprian corpus quotations, re-verified with notes excised before tag-stripping.** *"it is the shepherd that is chiefly wounded in the wound of his flock"*, *"I wail with the wailing, I weep with the weeping"*, *"neither does any of us set himself up as a bishop of bishops"*, *"judging no man, nor rejecting any one from the right of communion, if he should think differently from us"*, *"ancient venom"*, *"your suffrage and God's judgment"* — each occurs exactly once in body text and zero times in a `<note>`.

**The known editorial trap is still correctly avoided.** *"thousands of certificates were daily given, contrary to the law of the Gospel"* — one occurrence, in body text. The endnote's competing wording, *"against the Gospel law"*, occurs once and **only** inside a note. `Lexicon_Deployment_Index.md` §7's seventh register entry is the record of a prior pass quoting the endnote as Cyprian; this document quotes the body. Checked character by character, on both sides of the apparatus boundary.

**No quotation in the document resolves to a 19th-century preface, endnote or footnote.** I searched notes separately from body for every corpus string. Zero hits.

**No intra-corpus misattribution.** The only quotation from a letter in Cyprian's corpus that is not Cyprian's — *Ep.* XX — is attributed to Celerinus, correctly, by name, with the div resolved by `title=`.

**CO-022.** The masthead's two project-lead quotations are verbatim in `lpc_Decision_Log.md` — I opened the Decision Log itself, which Round 1 explicitly did not. `lpc_Gapped_Formation_Precedent.md`'s masthead independently records *"Received 2026-09-15 from the project lead, who handed it directly to this build thread."* Every project-lead attribution in the document has a verifiable record.

**Section 5 against `lpc_Force_Index.md` §1–§2 and Doc_08 §3/§9 — all 15 entries, every field, plus both omissions.** Cell, Layer 1 confidence and connected gravities match row for row. The confidence-profile claim (14/3/1), the 15-of-17 arithmetic, the two named omissions and the Contested-element claim all reconcile.

**Section 6 against `Lexicon_Deployment_Index.md` §3 — all eleven entries, every tag, including negatives.** Seven Tier 1 terms, each with a YES/NO always-present designation. Six [AS] terms, four carried, two correctly named as not carried.

**Section 8 coverage.** Every thin domain named in Doc_07 §7 and in Doc_09 §7 items 1–4 has an entry; item 5 is correctly dropped as answered. Section 4B, Section 4F and Section 8 Domain 1 are now mutually consistent on the confessors: a recognised status, a real lay first-person voice, and not the ordinary congregant. Section 4C/Domain 5, Section 4G/Domain 4, Section 1/Section 5 3B-2/Domain 6 and Section 4A/Domain 8 are each consistent pairs. **The Section 4B–4F contradiction Round 1 found is gone.**

**Section 10.** `sed -n '222p'` re-run as printed; output diffed against Profile line 712; **byte-identical**. The Status field is correct.

**Doc_04 §7 Open Items 6 and 8 — both CLOSED**, verified at source, with the closure reasons and the quoted sentence exact.

**Arithmetic on what the document says it contains:** 8 gravities (4/3/1) ✓; 15 Section 5 entries across all six cells ✓; 11 vocabulary terms ✓; 2 tensions ✓; 11 Section 11 items ✓. *(Failing: 8 domains vs "six" — NEW-4; nine/two boxes vs "three" — NEW-3a; "four carried open" vs three named — NEW-8.)*

**Registry rows 1, 9, 15, 27, 122, 192, 194, 209** opened and read; every use of each in the document is accurate.

**Letter CXXVI** located by `title=` in `npnf101`: *"Letter CXXVI. (a.d. 411.) To… Albina"*, on Pinianus and the Hippo crowd. The 4B and 4G uses are both accurate.

---

# What I did NOT check

1. **I did not re-derive `lpc_Force_Index.md` from `Doc_08_Forces_Document.md`.** I compared the Profile against both, and against each other for the entries I quoted, but I did not re-run `scripts/gen_force_index.py` or audit the Index's §6/§7 reconciliation.
2. **I did not read Doc_05, Doc_06 or Doc_07 in full.** Doc_05: §4, §5, §6.3–§6.6, §9. Doc_07: §2B, §2C, §7, §8. Doc_06: not opened at all — I worked from `Lexicon_Deployment_Index.md`.
3. **I did not read the nineteen Lexicon-Chunks or the seven Story-Chunks.** I opened `lpcstory005` and grepped `lpclex002`, `lpclex005`, `lpclex017`.
4. **I did not audit `Doc09_Claims_Register.md` at all**, or `Source_Registry.md` beyond the eight rows listed above.
5. **I did not open the 411 *Gesta* or the *Acta Proconsularia*.**
6. **I read Possidius only at chapters V and XXVI–XXVII** plus targeted greps. I did not read XIX–XXVII in full, so I cannot say whether any other Profile claim is refuted there the way NEW-2's is. **Given that the one claim I did test against it failed, a pass over the whole document against that read is warranted.**
7. **I did not test "this world has no distinctive liturgical epigraphic marker"** against `cil8-supplementum-numidiae_cagnat-schmidt1894.txt`, which is vendored. It is an untested absolute claim of the class this build gets wrong.
8. **I did not test "nothing else in this ecology is found to depend on it resolving either way"** (G7) or *"no comparative-community instrument has been run"* independently; I traced both to upstream statements only.
9. **I did not verify the Latin OCR of the *Retractationes* quotation** beyond line 1512 and its two neighbours.
10. **I did not assess readability** against the CLAUDE.md B2 / FK 8–10 / FRE ≥ 60 target, and note, as Round 1 did, that nobody has yet said whether it applies to this document or only to what is built from it.
11. **I did not run the Section 3 usability test** by attempting to write a Capsule Core from Section 3 alone. Section 11 item 3 certifies that it passes; that certification remains unaudited.
12. **I did not compare against `ijc`, `hal`, `cappadocian`, `syr` or `alex` profiles** beyond word counts, and against `don` only for its Section 4 heading list.
13. **A hygiene question I am flagging rather than finding.** The document now narrates its own review history inline — Section 4's preamble (*"Round 1 found the mapping correct and three of the four dimensions' required content missing"*) and Section 11 item 11 (*"Round 1 found four citation-locus errors, two altered quotations…"*). CLAUDE.md reserves live/canonical surfaces for output free of *"review discussion"*, but names `world-build-docs/` rather than `World-Builds/` and says the categorisation is inferred. I do not treat it as a finding; somebody should rule on it.

---

# Is the document adequate to proceed?

**Not quite — and the gap is one paragraph wide.**

Round 1's five HIGHs are genuinely gone, and I say that having re-derived every one of them from the primary sources rather than from the diff. The Representative-facing risks Round 1 identified — a Representative denying it has a lay voice it demonstrably has, and describing the 133-year interval as an empty archive — are both resolved at every site, in Section 8, where they would have propagated. The fabricated confessor line is replaced with a real one that I verified by `title=`, outside every note, with the parenthesis the story chunk says is load-bearing. The analytical spine that Round 1 found sound is still sound, and the mechanical quotation sweep it asked for now returns clean.

**What blocks is NEW-1.** It is a single sentence, but it is the same failure class that produced four of Round 1's five HIGHs — a sourced silence claim that an approved input refutes — and it now sits inside Section 4D, in text written to satisfy a review finding, contradicting Doc_05 §5.3 and this document's own Section 3 about the world's densest textual object. That is not a citation slip. A Capsule Core builder reading Section 4D will take away that G7 reached nobody's formation, which is the opposite of what the ecology says.

**NEW-2 is the one I would want re-run beyond its own sentence.** The fix pass wired the Possidius read into three sections and did not carry it anywhere else. The single claim I tested against that read failed. There may be others.

**Everything else is small, and most of it is arithmetic.** But the arithmetic is in Section 11, which the template makes mandatory precisely because it is the self-audit, and a self-audit that miscounts its own checkboxes and certifies a name-match the document disclaims on page one is not yet doing its job.

**What I would want before clearing:**

1. **NEW-1 fixed at source** — the G5 finding restored to G5, and whatever disclosure genuinely belongs on the 4D ontology paragraph written from what Doc_04 and Doc_05 actually support.
2. **NEW-2 fixed, and the Possidius read carried across the whole document**, not just Sections 3, 4C and 5, by a thread that reads XIX–XXVII rather than the artifact.
3. **Section 11 re-answered honestly** — the box count, the date, the by-name claim, and a decision about whether Domain 8 and Domain 4 really satisfy item 8.
4. **The count sweep finished** — "six honest limits," the escalation counts, "five further lenses," and the length figures.
5. **LOW-1's fourth site** — `Doc_08 §9.2` does not exist.

**With those done, this document clears.** It is closer than the count reads, and considerably closer than Round 1 left it. The fix pass did the hard work correctly; what it did not do is re-read what it had just written.

---

*Round 2 complete. 1 HIGH · 6 MEDIUM · 6 LOW · 2 COSMETIC. Of Round 1's 21: 20 CONFIRMED FIXED, 1 PARTIALLY FIXED, 0 NOT FIXED, 0 FIXED WRONGLY. REVISION REQUIRED.*
