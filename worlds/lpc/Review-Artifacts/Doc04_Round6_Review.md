# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 6 Independent Adversarial Review — the corrected reconciliation pass, the rewritten *Gesta* read, and the formal reopening of Doc_01 §5

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-14.

**Documents reviewed, at commit `27ed339a` (prior state `9fcc001d`), working tree clean:**

- `worlds/lpc/Doc_04_Gravity_Discovery.md`
- `worlds/lpc/Review-Artifacts/Doc04_Gesta_Targeted_Read_2026-09-14.md` (**second version**, rewritten after `Doc04_Round5_Review.md`)
- `worlds/lpc/lpc_Decision_Log.md` (both 2026-09-14 entries)

**Read for context and used as the test standard, not reviewed:** `Doc_01_World_Identification_Boundaries_Orientation.md` §4, §5, §8 items 7 and 10, §9; `Source_Registry.md` row 65; `Doc04_Round5_Review.md`; `L1-Foundation/CiC_L1_Constitution_V2_2.docx` Article 21; `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`.

### Method

This reviewer drafted nothing under review, wrote neither version of the *Gesta* read, and performed neither fix pass.

Every claim in the rewritten source read was re-derived **directly from the scan**, not from the read's account of it. All five cited file lines were opened with ±20–50 lines of context and their **column structure** reconstructed before a speaker was assigned. The band-structure claim was re-derived independently by running act-header and footnote-marker density per 500 lines across 115500–131999 and then **opening samples inside the claimed apparatus band** rather than trusting the density figure. Every count (35 strict, 64 OCR-tolerant, 180 speeches, 93 tokens, 17 acts, the per-speaker tallies) was re-run over the read's own declared domain and, separately, over the domain the read excluded. Article 21's strand definition was extracted from `word/document.xml` and compared character-for-character. Doc_01 §4's own definition of the conciliar-authority axis and §8 item 10's trigger sentence were read verbatim. Structure (both tables, pipe counts, bold/backtick balance, all 28 matrix pairs, matrix-vs-§3 agreement) was machine-checked. Round 5's 26 findings were each re-tested at HEAD at their own named sites.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**8 HIGH, 12 MEDIUM, 8 LOW, 3 COSMETIC (31 findings).**

**Against Round 5's 26 findings:** **4 genuinely resolved** (H1, H3, and the reproducibility half of H7; M4), **5 partially resolved** (H2, H4, H5, H6, M3, M8 — counted as five distinct partials, M3/M8 merged), **17 outstanding**. The pass reports Round 5's findings as simply "unaddressed" and its Decision Log says "Round 5's remaining findings are unaddressed." **That misreports in both directions**: it silently fixed H1 and H3 in full and H4 and H7 in part without a tally, and it leaves M1, M2, M5, M7 and L8 untouched at their own named sites while its Status line certifies structural re-verification.

**Verdict on the rewritten *Gesta* read: UNSOUND** — not merely overstated. Reasons in the audit section below; in short, one of the four on-axis passages is assigned to the wrong speaker by the same two-column-bleed mechanism that produced the first version's errors, the band-structure claim that frames the whole rewrite is false and is contradicted by the read's own act-158 citation, and Finding 2 is refuted by the read's own closing paragraph.

**Verdict on the §5 reopening: the reopening is formally performed and substantively evaded.** It is not a legitimate discharge of item 10's *"reopened rather than defended past the evidence."* Details in the §5 section.

---

## What was checked hard and found CLEAN

Stated before the findings, because several of these are the pass's own claims and they hold.

1. **Article 21's strand definition is quoted exactly.** Doc_04 §5's Finding quotes *"a meaningfully distinct pattern of formation emphasis, practice, authority structure, or ecological orientation within a single world, not merely a variation in detail."* Extracted from `word/document.xml`: Article 21, paragraph 3, **character-for-character identical**. No elision, no added emphasis, no splice. After five rounds of misquoted governing text in this document, this one is clean.

2. **Doc_01 §8 item 10's trigger is quoted accurately**, including the consequent Round 5 found dropped at every previous site. §5 now carries *"in which case the finding is reopened rather than defended past the evidence"* in full. The quotation is right; what is done with it is H2.

3. **Line 117492 is exactly as reported.** Line 117487 reads `40. Aureliui epitcopui Eccletuv calhotica LarthagU / nenw dixit`; the sentence runs 117490–117493 and carries `univeraalii concilii Ecclesiaa catholics ... constituli mandarunt`. Speaker, act number, file line, and normalization all check out. This is the strongest passage in the file and the read found it.

4. **Act 158 at line 121764 is genuinely a subscription, not a speech.** Line 121763–121768 reads `158. Augustinus episcop... Carthagini constitutus praesente... tribuno et notario Marcellino mendalum ·usccpi fll nibacripsj`. Surrounded by the subscription roll-call (Adeodatus at 121736, Restitutus at 121743, Lampedius at 121748) with the identical `mandavi et subscripsi` formula. The read's new diagnosis is **correct**, and it explains the anomaly Registry row 65 recorded without a cause. This is the best piece of new work in the rewrite.

5. **"Constantinus, line 119042" is verified as apparatus.** Footnote `(7-2) Eliensis` reads *"Synodicae episcoporum Byzacenorum ad Constantinum in concilio Lateranensi sub Martino subscribit Constantinus episcopus sanctae Ecclesiae Heliensis."* Lateran 649 under Martin, glossing a place-name. The withdrawal is right.

6. **The polarity correction is right.** Line 117496 is `Emeritus episcopus dixit`; 117496–117505 carries *Fidei causa est, quae et sine mandato ipso iure agi potest... superfluumque sit ceterorum mandatum, cum in uno consistat Ecclesiae tota persona*. Speaker and direction as now stated. (What is inferred *from* it is H5.)

7. **The strict `mandat` count reproduces exactly.** Case-insensitive `mandat` over 116000–118499 ∪ 125500–130999 returns **35**. The read's "35 strict" is honestly derived.

8. **All seventeen listed Augustine act-numbers exist at the lines given**, including the three new ones: 14 at 125505 (`Angustinus`), 230 at 129294 (`Autjuslinus`), 252 at 129318 (`AM(jus!i?iMS`). Each opened individually. (The *count* is M3.)

9. **The ten-term destination sweep is now reproducible.** `Tensional|escalat|Candidate 5|[Cc]onciliar|residue|bounded|the axis|trigger|unreopened|not a gravity` returns **47 lines at HEAD** and 46 at `9fcc001d`. The Decision Log's "47 lines" is exactly right. Round 5's H7 reproducibility complaint is genuinely answered — at the Decision Log. (Not at §8: see H7.)

10. **The "unreopened" residue is gone.** Zero hits at HEAD. The assertion that fired, fired correctly.

11. **Structure is clean and the pass's structural claim is true.** Both tables uniform (6 pipes × 10 rows; 10 pipes × 9 rows). Every `**` and backtick balanced on every line of both documents. **All 28 matrix pairs symmetric** — the one asymmetric-looking pair (2,7) is `Reshaped by` / `Reshapes`, a directional converse, correct. Candidate 5's row and column agree exactly with each other and with §3's Interaction bullet (reinforcing with 1, 3, 6; no demonstrated relationship with 2, 4, 7, 8).

12. **The arithmetic in the error account holds.** 35 against 64 is 45.3% low; "~45% low" is right, not rounded in the pass's favour.

13. **The three contradictions Round 5 named are fixed at two of three sites each, and Open Item 3 and Open Item 2 are fixed outright.** Line 211 no longer says "classified Tensional"; line 210 no longer instructs downstream steps both to refuse and adopt Supporting. Both were byte-identical through two prior passes. They are genuinely closed.

---

## HIGH

### H1 — §5 still certifies the opposite of its own Finding at four live sites, and still certifies the *Gesta* unread; the twelve assertions tested a token, not the proposition

**Sites:** `Doc_04_Gravity_Discovery.md` line 173 (three occurrences), line 235 (Disposition).

The pass's headline change is that Doc_01 §5's finding is **reopened**. At HEAD, §5 line 173 still opens:

> *"**Candidate 5's own result does not reopen the strand-singular finding**, and this document states why rather than asserting it..."*

and, 500 words later in the same line:

> *"**The non-reopening finding below does not rest on that classification either way**, and is argued on its own ground: What carries the **non-reopening** is Doc_01 §8 item 10's own trigger, met on its own terms..."*

and the Disposition, line 235:

> *"Candidate 5's reclassification and **the strand-singular non-reopening** are applications of Doc_01's own already-cleared §5 determination."*

Against, in the same line 173 and the Finding immediately below it: *"**The trigger is met**... **So the finding is reopened here, as item 10 directs, and then reaffirmed on the evidence**"* and *"**Finding: reopened per item 10, and reaffirmed.**"*

Worse, line 173 still contains, unedited, the certification Round 5's H2 named:

> *"Candidate 5's Repetition and Persistence tests above disclose that this document has **not** read the *Gesta Collationis Carthaginiensis*... **If a targeted read surfaced such material it would be evidence Doc_01 has not weighed, and item 10's trigger would be met.** Carried as §7 Open Item 6."*

§3 says the source "has been read twice." §7 Open Item 6 is headed "Discharged." §5 says it has not been read and states the trigger in the conditional — four sentences after saying it is met.

**Why this is the pass's central failure, not a leftover.** The Decision Log certifies: *"twelve explicit contradiction assertions then ran over it and one fired... a stale 'unreopened' survived."* `unreopened` is gone. `does not reopen`, `non-reopening` ×2, `has **not** read`, and `would be met` all survive. The assertion set tested **the literal string the author remembered writing**, not the proposition the pass exists to change. Round 5's H2 asked for exactly this passage to be deleted; the pass deleted the four-word phrase Round 5 quoted first and left the rest of the paragraph Round 5 quoted second.

**Fix:** rewrite line 173's opening clause and both "non-reopening" instances to state the reopening; delete the entire "Bound stated with the finding" passage, now false at both limbs; correct line 235. Then re-run assertions **over propositions** — "does this document anywhere deny the reopening", not "does the token `unreopened` occur".

---

### H2 — The reaffirmation answers a different axis from the one item 10 names; on item 10's own terms this is defending past the evidence in new wording

**Sites:** Doc_04 line 175 (§5 Finding); `lpc_Decision_Log.md`, second 2026-09-14 entry.

The Finding reads:

> *"The 411 evidence shows one African episcopate in which the standing of conciliar mandate is **disputed between two parties to a schism already recognised as outside this world's boundary** (Doc_01 §5's own Article 3 argument): the Donatist position is the rival communion's, not a second pattern *within* this world."*

**Tested at source, as instructed.** Doc_01 §5 does place Donatism outside this world's boundary — on the "preserve communion versus break communion and build a rival hierarchy" axis, adopted from `Syriac-Build/CiC_Coach3_Step0_Critique_2026-07-06.md` and Donatism's own Step 0 §3 B3. That much is supported, and Article 21's "within a single world" clause makes the move formally available.

**But it does not reach the axis item 10 is about.** Doc_01 §8 item 10 names the axis in its own first sentence: *"Cyprian's own egalitarian, non-coercive theory of inter-episcopal authority (256 Council preface) and Augustine's own hierarchical, correctable theory of conciliar authority (*On Baptism* II.3)."* Both poles are **inside this world**. Doc_01 §4, verbatim at line 77, is more explicit still:

> *"Both texts above concern a bishop's answerability **inside his own communion**, not his relation to a rival one... What changes on this axis is not a bishop's relation to a rival hierarchy but the ***appellate structure above the individual bishop within his own communion*** — whether a plenary council can overrule a provincial one, or an individual bishop's own judgment, in a way the 256 preface's own ecclesiology refuses."*

Doc_04's own Candidate 5 is named *Conciliar Authority Theory (**Egalitarian vs. Hierarchical**)* — Cyprian against Augustine, diachronically, within one communion.

**The argument therefore takes both horns of a fork it does not acknowledge.**

- If the 411 dispute is Catholic-versus-Donatist and therefore *cross-boundary*, then it is **not evidence on item 10's axis at all** — and the trigger is not met, the reopening is spurious, and §5's whole new structure collapses.
- If the 411 material **is** on-axis (which is what meets the trigger and what carries Persistence at line 94), then its on-axis content is the part that sits **inside** this world: Aurelius of Carthage, primate, act 40, stating that he cannot exceed the limit of a mandate given by a *universale concilium*; the Catholic delegation describing itself as *electi ab universali catholico concilio*; Augustine personally subscribing that mandate at act 158. That is an in-world bishop asserting a conciliar authority binding above the individual bishop — **precisely the pole Cyprian's 256 preface refuses** — a century and a half after Cyprian refused it. The "rival communion" argument does not touch one word of it.

Doc_04 concedes the second horn itself, in the new §3 Repetition text: *"**The on-axis content there is not Augustine's own**... the conciliar-authority claim at 411 is made by Aurelius and disputed by Emeritus."* So the document knows that the in-world half of the evidence is Aurelius's, and the reaffirmation never engages Aurelius at all.

**This is the review's sharpest finding.** Item 10 does not merely require the word "reopened"; it requires that the finding not be *defended past the evidence*. The pass performs the reopening as a formal act and then discharges it by **changing the subject** — from the Cyprian/Augustine intra-world axis item 10 names, to the Catholic/Donatist cross-boundary axis it does not. The evidence Doc_01 never weighed is left un-weighed under a new heading. "Reopened and reaffirmed" is, on this argument, a relabelling of "not reopened," which is what Round 5's H2 predicted would be attempted.

**Fix:** state Doc_01 §4's own definition of the axis before arguing; then argue the in-world half directly — whether Aurelius's *universale concilium* at 411, plus Augustine's own subscription to it, constitutes a meaningfully distinct **authority structure** from Cyprian's 256 preface within one world, or does not. The Donatist half may well be disposable as cross-boundary; the Catholic half is the case to answer and it is not answered.

---

### H3 — One of the four "on-axis passages" is assigned to the wrong speaker by two-column bleed, is not a speech at all, and carries no conciliar-authority content — the same failure class the rewrite exists to correct

**Site:** `Doc04_Gesta_Targeted_Read_2026-09-14.md` Finding 1, fourth bullet.

> *"**Petilianus, act 9, line 116941** — on who may approach *illum tranquillissimum concilii locum* beyond the prescribed number: the council's own constitution as a procedural question, argued by the Donatist side."*

Line 116941 in the scan reads, in full:

> `9.  Pelilianus  episcopns  dixit.  Salvis  omnibus  qnae` ⟶ `nium  concilii  locum  contra  probibitum  moliatur  ac-`

**These are two different columns.** The left column is Petilianus's act 9, which runs 116941–116947 and reads, whole: *"Salvis omnibus quae competunt nobis, et de persona et in causa, proponant ii qui ista elicere meruerunt. Et alia manu. Petilianus episcopus recognovi."* That is the entire speech. It contains no `concili-` token.

The phrase the read quotes is in the **right-hand column**, which runs continuously across 116933–116949:

> *"Aequissimum namque est, ut eorum universa collatio rata futura promittatur ab omnibus, qui eliguntur ab omnibus. **Nullus ergo vel laicus, vel episcopus ultra numerum praestitutum in illum tranquillissimum concilii locum contra prohibitum moliatur accedere**, quin potius etiam plebes suas pia quietis ac modestiae commonitione conveniant, hoc per Ecclesias proprias ante tractantes, quatenus a die disputationis ac loco omnis se multitudo contineat..."*

Three things follow, each independently fatal to the bullet.

- **It is not Petilianus.** It is jussive, third-person, regulatory — *"let no one, layman or bishop, attempt to approach"*, *"let them rather address their own congregations"* — and the left column immediately above it (116926–116939) is the *cognitor* speaking in the first person (*"epistolis ad meam dicationem currentibus"*). This is **Marcellinus's own edict** regulating attendance at the conference, the *formae* recited into the record at act 10 (`10. Martialis exceptor recitavit`, line 116956). It is the imperial commissioner's crowd-control provision.
- **It is not a Donatist argument.** The read's gloss — *"argued by the Donatist side"* — attributes an imperial regulation to a party it constrains.
- **It carries no on-axis content.** *"in illum tranquillissimum concilii locum... accedere"* is **the venue**: "to approach that most tranquil place of the conference." The read renders *locum* as *"the council's own constitution as a procedural question."* A rule about who may physically enter the hall is not a theory of authority above the bishop.

**Why HIGH.** The rewrite's stated diagnosis of its own first version is *"it reversed a passage's polarity... losing both the speaker and the polarity"* and its stated remedy is *"enumerate the population and look at it."* This bullet is new text, in the corrected version, and it mis-assigns a speaker across a column boundary in a file the read's own opening line describes as *"poor OCR, two-column bleed."* The rewrite **removed** the first version's OCR-hazard disclosure (M7) and then committed the error the disclosure existed to prevent. Four passages are offered as the surviving evidence; one of them is not evidence.

**Fix:** withdraw the bullet. If a Donatist procedural argument about conciliar constitution is wanted, it must be found in a Donatist speech.

---

### H4 — The band-structure claim that frames the entire rewrite is false, and the read's own act-158 citation falls inside the band it declares to be footnotes

**Site:** `Doc04_Gesta_Targeted_Read_2026-09-14.md`, "Structural finding, and the reason the first read went wrong"; repeated in `lpc_Decision_Log.md` error 3 and in the commit message.

> *"**The acts proper occupy lines 116000–118499 and 125500–130999. The band between them, 118500–125499, is Migne's own prosopographical footnote apparatus** — the editor's notes identifying bishops by the councils they attended. Measured by footnote-marker density per 500 lines, the apparatus band runs 9–27 markers with almost no numbered speeches, while the acts bands run 5–35 numbered speeches with almost none."*

**Re-derived independently.** Act-header and `(NN)` footnote-marker density per 500 lines across 115500–131999:

| span | act markers | fn markers |
|---|---|---|
| 116000–116499 | 39 | 0 |
| 118000–118499 | 22 | 9 |
| 118500–118999 | 2 | 38 |
| 119000–119499 | 3 | 38 |
| 121500–121999 | **8** | 17 |
| 122500–122999 | **12** | 3 |
| 123000–123499 | **11** | 26 |
| 125000–125499 | **8** | 13 |
| 125500–125999 | 25 | 0 |

**The claim fails on its own instrument.** The declared apparatus band carries roughly **80 numbered act headers**, not "almost no numbered speeches" — a density comparable to 116500–118499 inside the declared acts band. And footnote markers appear at 4–9 per 500 lines *inside* both declared acts bands. The discriminator does not separate the bands in either direction.

**The claim fails on direct inspection, which is decisive.** Opening samples inside the declared apparatus band returns conference record, not notes:

- **121756–121790** — acts **157** (Petilianus), **158** (Augustine's subscription), **159** (Petilianus), with the whole mandate-subscription roll-call (Adeodatus, Restitutus, Lampedius, Vincentius, Fortunatus, each `mandavi et subscripsi`).
- **122615–122640** — acts **171** (Marcellinus), **172** (Fortunatianus), **173** (Marcellinus), **174** (Alypius), full formulae, undamaged.
- **125205–125213** — act **223** (Alypius), then Primianus and Marcellinus.
- **120222–120240, 124605–124640** — more of the same, interleaved with notes.

What actually produces the high footnote density there is that this is **the recitation of the mandate with every subscriber's see named**, and Migne footnotes each see. The apparatus is *attached to* the record, not a substitute for it. Migne's page layout puts acts above and notes below; linearized OCR interleaves them. The read read density and inferred composition, and did not open the band.

**The read contradicts itself on this point in its own next section.** Finding 1's fifth bullet cites **act 158 at line 121764** — inside 118500–125499 — as a numbered act of the conference. Finding 3 counts it among Augustine's seventeen acts. The structural finding says that span is footnotes.

**Why HIGH.** This is the frame of the whole rewrite: it is the stated reason the first version went wrong, it defines the domain every count in Finding 3 is computed over, and it is what licenses withdrawing the first version's episcopal census. It is wrong in kind, and it over-corrected Round 5's H6: Round 5 proved that *one named example* (Constantinus, 119042) came from a note; the rewrite generalized from that to seven thousand lines, and discarded the conference's own subscription record along with the notes.

**Fix:** withdraw the band claim. Classify by **line type** — an act header, a subscription formula, a `(NN)`-initial note — not by line range. Then re-run every count in Finding 3 over the corrected domain.

---

### H5 — Finding 2 over-reads Emeritus in the opposite direction, and is refuted by the read's own closing paragraph

**Sites:** `Doc04_Gesta_Targeted_Read_2026-09-14.md` Finding 2; Doc_04 line 94.

Finding 2 concludes:

> *"**That is the disagreement, and it is precisely Candidate 5's axis.** The Catholic side grounds its standing in a universal council's mandate; **the Donatist side answers that conciliar mandate is a formality irrelevant to the cause**... **Two rival theories of where authority above the individual bishop resides**, argued on the record."*

**What Emeritus actually says, read whole (117496–117520).** He objects to the *mandatum*: it is a cause of faith, pursuable *ipso iure* without a mandate; why all this questioning *de mandato, vel de obligatione mandati, de subscriptione, de modo, de formulis*; each conducts his own cause and the business of his own salvation, so the mandate of the rest is superfluous. He then asks Marcellinus to decide whether this is *forensis altercatio iurisque conflictus* or *simplex illa veritas qua datur vita*.

**`concil-` does not occur anywhere in Emeritus's speech.** Verified across 117496–117545: zero hits. He never mentions a council. His objection is to **mandate formalities** — subscription, manner, formulae — which is a procedural objection to the instrument, addressed to the judge, asking that procedure be set aside for substance.

**The read refutes its own Finding 2 three paragraphs later.** Under "Does not support either":

> *"the first version's framing of the *mandatum* as in itself an inter-episcopal authority instrument. In Roman procedure a *mandatum* is a procuratorial instrument — a power to act for a party... **What is on-axis is not the mandate as such but its stated source: a universal council**."*

Finding 2's entire contested-ness claim rests on a speech that engages **the mandate as such** and never engages its stated source. By the read's own stated rule, Emeritus is off-axis. The read applied the rule to the first version's evidence and exempted its own.

**"cum in uno consistat Ecclesiae tota persona"** may be doing real ecclesiological work — it is a plausible Cyprianic echo and is worth arguing. But it is embedded in a subordinate clause of a rhetorical question about litigation formalities, and it is not argued here; it is quoted and captioned. Round 5 found the first version paraphrasing it into neutrality; the rewrite paraphrases it into a rival conciliar theory. Both are the same move.

**Why HIGH.** "Genuinely contested, on the axis, between the two sides" is one of the two things the read claims to support, and Doc_04 line 94 now carries it into the live document in bold as *"**And it is contested on precisely this axis**"* — and §5 then builds the entire reaffirmation (H2) on the premise that the contest is Catholic-versus-Donatist.

**Fix:** either argue *in uno consistat Ecclesiae tota persona* as an authority claim, against Doc_01 §4's own definition of the axis, or scope Finding 2 to what the passage shows — a Donatist objection to mandate procedure, which the read's own closing paragraph classifies as off-axis.

---

### H6 — The Disposition's escalation self-assessment contradicts §5, contradicts the Decision Log, and declines the escalation Round 5 left open

**Sites:** Doc_04 line 235 (Disposition); `lpc_Decision_Log.md`, second 2026-09-14 entry, closing line.

Doc_04's Disposition, at HEAD:

> *"No portfolio-level or cross-world decision: Candidate 5's reclassification and **the strand-singular non-reopening** are applications of Doc_01's own already-cleared §5 determination... **Unresolved tensions: closed.**... **Nothing in this document is now escalated.**"*

The Decision Log entry written by the same pass, on the same day:

> *"**Unresolved tensions: one raised, not closed** — the formal reopening of Doc_01 §5's finding under item 10 is a change in a cleared companion document's status... It is disclosed here for the project lead rather than treated as routine."*

The two governing records of this pass state opposite escalation results for the same act. Doc_04's own Disposition additionally describes the act as a "non-reopening" (H1) and as an *application* of Doc_01's cleared determination, when §5 four paragraphs above says the determination was **reopened**.

**And "disclosed for the project lead" is not escalation.** CO-022's fourth standing category is unresolved tensions the pipeline cannot close on its own — the limb this build's own template runs as "no contradiction with another cleared document exists." Round 5 closed with *"CO-022 category 4 re-opened on the item-10 trigger question"* and asked the pass to *"route the reopening through CO-022 category 3 or 4 rather than absorbing it."* The pass absorbed it and wrote a note.

**Fix:** decide one way and make both documents say it. If the reopening is routine because item 10 authorized it in advance, Doc_04's Disposition must say so and the Decision Log's "one raised, not closed" must go. If it is a live tension — which is this reviewer's assessment (see the CO-022 section) — it escalates, and both records say so.

---

### H7 — §8, the Document Log, was not touched: no entry for Round 5, the rewritten read, or this pass; and it still certifies three claims the pass itself withdrew

**Sites:** Doc_04 lines 217–229 (§8); line 3 (Status).

The last entry in §8 is the **first** reconciliation pass. There is no §8 entry for `Doc04_Round5_Review.md`, none for the rewritten source read, none for this pass. §8 therefore still states, as the document's own log of record:

- *"located **by searching the whole document** for `Tensional|escalat|Candidate 5|Conciliar Authority` — **twenty-four lines**"* — the exact certification Round 5's H7 proved unreproducible (the search returns 36 at HEAD, 37 at `b2e93cac`). The Decision Log now records the corrected ten-term/47-line sweep; **§8 and the Decision Log now describe two different sweeps as the method of the same document**, with no reconciliation.
- *"**Round 4 findings resolved by this pass: H1, H2, H3, H4, H5, H6, M1 — seven of twenty.**"* — Round 5 verified this as 3 genuinely resolved, 4 partial. Uncorrected.
- *"It falsified **both limbs** of the absence claim... and supplied Augustine's second independent, non-treatise locus (**act 50, file line 126796**)."* — both withdrawn by this pass: §7 Open Item 6 now says the second limb "remains genuinely open," and §3 now cites act 158 / 121764 as the locus.

**The Status line's own certification is therefore false.** Line 3 states: *"Each count in this line and in §8 is derived from the enumeration below it, not from a fix list."* §8 carries no enumeration for this pass at all.

**Why HIGH.** §8 is what a downstream builder reads to know what happened to this document. It currently tells that reader that the last thing that happened was a four-term sweep that closed seven of Round 4's findings, on a source read that falsified both limbs — a description that is false in every clause, in a document whose Status line advertises it as derived.

**Fix:** add §8 entries for Round 5, the rewritten read, and this pass; correct the three stale claims in place with the correction disclosed, per this document set's own convention.

---

### H8 — The Status line still asserts "falsified both limbs," which §7 Open Item 6 and §3 now contradict

**Sites:** Doc_04 line 3; against line 94, line 107, line 214.

Line 3, the Status line, rewritten by this pass:

> *"a targeted read of the *Gesta Collationis Carthaginiensis*... **falsified both limbs of the absence claim Candidate 5's Persistence test rested on.**"*

Line 214, §7 Open Item 6, also rewritten by this pass:

> *"**What remains genuinely open:** whether conciliar authority reached ordinary clergy at all. The 411 acts carry roughly a dozen speakers, so they cannot settle it, and Candidate 5's Formation test still does not pass."*

Line 94: *"**What this does not establish, and the verdict is scoped to exclude it:** that the question was operative among *ordinary clergy*."*

The absence claim's second limb, quoted by the read's first version, *was* "operative or contested among ordinary clergy." The pass's entire stated achievement is scoping the claim back to what the corrected read supports — and it left the maximal version standing in the first paragraph of the document, in the same edit that added the scoping everywhere else. This is Round 5's M8 re-created at a higher-visibility site by the pass that fixed it at the lower ones.

**Fix:** line 3 — *"falsified the first limb of the absence claim and left the second open."*

---

## MEDIUM

### M1 — Every count in Finding 3 is computed over a domain that excludes the densest concentration of mandate language in the file, and the "small cast" conclusion rests on it

Finding 3's counts are declared "within the acts proper," i.e. over the bands H4 shows to be wrong. Measured over the excluded band 118500–125499:

- **145 occurrences of `mandav*`** — the `mandavi et subscripsi` subscription formula — against **9** in the read's declared bands.
- 19 further `mandat`-family tokens.
- 460 `episcop-` tokens, a substantial share of them real subscription entries, not notes.

So the read's headline "35 strict / 64 OCR-tolerant in the acts proper" is a **narrower** undercount of the conference's own mandate language than the first version's 58, in a correction that presents itself as fixing a 45% shortfall. And the conclusion that carries the Formation verdict — *"**This is a small cast, not dozens of disputants**"*, *"a delegation and a judge, not a broad clerical constituency"* — is derived by excluding the part of the record where the 280-odd subscribing bishops appear. Round 5 correctly killed the first version's *"250 `episcop-` tokens"* as contaminated by notes; the rewrite's response discards the subscription roll with them. **Fix:** re-run over a line-type-classified domain, and state the cast size against the subscription roll rather than against the debate transcript alone.

### M2 — "64 OCR-tolerant" is not reproducible from the four variants the read names

The read gives *"35 strict, 64 OCR-tolerant (`mandalo`, `mandalum`, `mandali`, `mandaium`)"*. Strict plus exactly those four, over the read's own bands, returns **53**. A broader tolerant class returns 67. 64 is reachable only with variants the read does not name (`mandaio`, `mandaii`, `mandala`, `nandaiun`, `nandaii`, `mendalum`, `maudalum` are all present in the span). The number may be right; as written it cannot be checked, which is the property Round 5's H7 was about.

### M3 — "Augustine speaks in seventeen numbered acts" is an act-number tally presented as a speech count, and it is a floor asserted flat

Row 65's standing instruction, which the read quotes approvingly: *"any restatement of this figure elsewhere should carry the floor with it rather than assert fourteen flat."* The read writes *"Augustine speaks in **17** numbered acts, not fourteen"* and *"All seventeen confirmed at their own lines"* — flat, with no floor.

It is a floor. **Act 50 carries an Augustine speech at two distinct lines**: 125831 (`50. Angutlinut cpiscopus Ecrletia? catliolica: dixit. ... Edictum nobilitatis tuae sic se habet`) and 126796 (`50. Augustinus episcopus Eccleshv catholicai dixil. Legatur mandatum nostrum`). Different speeches, both Augustine, both numbered 50. There is a further, **unnumbered** Augustine speech at 125822–125823 (`Auguttinut episcopus Ecclesiae catholicae dixit. Non est in causa factum...`). Act numbering in this band is also non-monotonic — act 53 at 126598 precedes act 50 at 126796 — which the read's own quotation-discipline note predicts and then does not apply. **Seventeen act-numbers; at least nineteen speech instances.**

### M4 — The read counts act 158 among the acts Augustine "speaks in" while Finding 1 says it is not a speech, and Doc_04 §3 carries both

Finding 1: *"**Augustine, act 158, line 121764** — **not a debate speech** but his own subscription."* Finding 3: *"Augustine speaks in 17 numbered acts... Registry row 65 lists 50, 53, 98, **158**..."* Doc_04 §3 line 88 then reads *"Augustine **speaks** in **seventeen** numbered acts of the 411 Conference **and** personally subscribes the delegation's mandate (act 158...)"* — which double-counts 158 as both. On the read's own diagnosis, he speaks in sixteen and subscribes in a seventeenth.

### M5 — Round 5's M5 is unfixed, and the widened sweep matched one of the two sites and did not act on it

Doc_04 **line 96** still reads *"this candidate's own six-test profile above being **narrow at best**"* — against line 99's *"passes Repetition and Persistence."* Line **97** still reads *"better described as **a live, unresolved theoretical residue of the century-gap itself**"* and *"the residue is recorded at §7 Open Item 6 rather than treated as discharged"* — against line 99's *"**not** a theoretical residue visible only between two bishops a century apart"*, and against Open Item 6's new heading, *"Discharged."*

Line 97 contains the token `residue`, which is **term six of the pass's own ten-term sweep**. The sweep matched it. This is Round 5's H1 diagnosis exactly — *"the failure has moved from not finding the site to finding it and not acting on it"* — recurring one round later, in the pass that adopted the widening remedy.

### M6 — Round 5's M1 is unfixed at its own named site

Doc_04 line 173 still reads *"CF V7.4 reads 'They *may* not organize as broadly as primary gravities **but they prevent the ecology from being reducible to its primary forces**'"* — bold added, no "emphasis added," in a quotation of a governing framework whose `.docx` run carries no `<w:b/>`. Round 5 named line 173 specifically and noted that the previous pass had fixed it at a different site (line 103, where the parenthetical still sits). Unchanged.

### M7 — The rewrite dropped the OCR-hazard disclosure entirely, and two of its five citations sit on bled lines

The first version disclosed two-column bleed (Round 5's M6 found the disclosure inaccurate). The second version has **no bleed disclosure at all** — the Quotation-discipline section covers normalization only. Yet line **127075** carries visible bleed on its own line (`...univeriale eoneilium maudavll, ilii K demnmurandan Evangelium profertmHi it '</<«` — the tail is a different column), and line **116941** is bled outright (H3). Removing a disclosure Round 5 found imprecise, rather than correcting it, is a regression, and it removed the one warning that would have caught H3.

### M8 — 127075's speaker is never identified, though Finding 1's heading claims attribution

Finding 1 is headed *"conciliar authority is invoked on the record, **by bishops other than Augustine**."* For 127075 the read says only *"Possidius speaks immediately after."* Verified: Possidius's act opens at 127081. But the speaker of 127075 is not established, and cannot be by the read's line-initial method, because the region 126950–127080 carries no recoverable left-column act header. Of the five cited passages, a speaker is established for **two** (117492 Aurelius, 121764 Augustine), absent for two (118113, 127075), and wrong for one (116941).

### M9 — Registry row 65 is now contradicted by the read and is not reconciled or carried as an open item

Row 65 states: *"Act 158 is the weakest of the set — **a genuine act in which Augustine speaks**"* and *"an OCR-tolerant line-initial scan... returns **fourteen** numbered acts in which Augustine speaks."* The read supersedes both. The Registry is untouched and the pass carries no open item to reconcile it, so the Source Registry and the Review-Artifact now state different things about the same lines. (The read is right and the Registry is stale; that is the point.)

### M10 — Round 5's H4 is fixed at one of four named sites; the other three still certify Supporting on the first clause alone

§3 line 99 now runs all three clauses of CF V7.4's Supporting definition — a genuine fix, and the third-clause argument is the best reasoning in the pass. But Round 5's H4 named four sites. **§4's Classification cell, line 164**, still reads *"meets Supporting's own Framework definition (**organizes significant portions of the ecology**) on the 411 Conference evidence"* — one clause. **§7 Open Item 2, line 210**, the instruction three downstream steps inherit, likewise carries the first clause only. The Decision Log's earlier 2026-09-14 entry is uncorrected. Reported nowhere as partial.

### M11 — §5's Finding sentence, read as written, places Aurelius and Augustine outside this world

*"the standing of conciliar mandate is **disputed between two parties to a schism already recognised as outside this world's boundary**"* — the qualifier attaches to the schism, or to both parties. On either reading the Catholic delegation is outside this world's boundary, which is not what Doc_01 §5 holds and not what the next clause intends. The load-bearing premise of the reaffirmation (H2) is stated in a sentence that misstates it.

### M12 — The Repetition test is certified "Passes" on a second locus the same bullet concedes carries no on-axis content

§3's Repetition bullet requires *"a second, independent Cyprian-authored locus restating the same authority **theory**"* for Cyprian's pole and claims Augustine's pole now has one. The new text supplies it — *"Augustine speaks in seventeen numbered acts... and personally subscribes the delegation's mandate"* — and then states: *"**The on-axis content there is not Augustine's own, however, and this bullet does not claim it is**... the conciliar-authority claim at 411 is made by Aurelius and disputed by Emeritus."* A second locus at which the author does not restate the theory is not a second locus for the theory. The honesty is real and welcome; the verdict above it did not move.

---

## LOW

### L1 — §5 carries a sentence fragment at the seam of an edit
Line 173: *"...disclosed here so the dependency is visible rather than reconstructed). **the** conciliar-authority disagreement being real, Documented, and bounded on §3's own six-test profile is weaker..."* — lowercase start after a full stop, no finite main clause before the participial. This is the "tail replaced, head left" shape the pass's own Decision Log says its assertions caught once.

### L2 — §5 still routes the reopening bound to an item now headed "Discharged"
*"Carried as §7 Open Item 6"* (line 173) against Open Item 6's new heading, *"Discharged 2026-09-14, then re-run the same day after audit."*

### L3 — "180 numbered speeches" and "93 raw speaker-tokens" are not reproducible
Line-initial numbered act headers over the read's own declared bands return **198**. Distinct name-tokens immediately preceding an `episcopus`-family token return **68**. Neither method is stated, so neither figure can be checked or corrected.

### L4 — Two per-speaker tallies are off, and the set mixes strict with tolerant counting
Fortunatianus is given 3; line-initial headers return 4. Petilianus is given "~20"; OCR variants (`Pelilianus`, `Petitianus`, `Pelilianut`) bring it to ~24. Marcellinus's "32" is exactly the **strict** line-initial count, in a list the read presents as OCR-tolerant — variants add roughly ten more.

### L5 — Round 5's L8 unfixed
Line 97 still attributes the gravity/forces rule to *"Forces Framework V1.1 §4 (Step 4)"*; Round 5 located it in the Layer 3 — Formation Impact block, which precedes §4.

### L6 — Round 5's M2 unfixed
The Status line still reads *"The preceding Round 2 fix pass addressed **26 of Round 2's 27 findings**"* — the fix pass's own headline — with no verified tally anywhere.

### L7 — The read's account of the first version's errors omits the finding that would have blocked Finding 2
Round 5's H5 had two limbs: the polarity reversal, and *"**And the axis is not this axis**"* — that a procuratorial standing dispute does not reach Doc_01 §4's own definition of the conciliar-authority axis, which the read never states. The rewrite's five-item error list carries the first limb and drops the second, and the rewrite still nowhere quotes or engages Doc_01 §4's definition. The read's own account of what it got wrong is accurate as far as it goes and incomplete exactly where it matters (H2, H5).

### L8 — The pass reports Round 5's findings as uniformly unaddressed, and silently fixed four of them
The Decision Log states *"Round 5's remaining findings are unaddressed."* In fact H1 and H3 are fixed outright, H4 and H7 in part, M4 substantively. No tally is offered in either direction. This is the sixth consecutive pass whose self-report does not match its diff — this time understating, which is the less harmful direction but the same defect.

---

## COSMETIC

### C1 — Round 5's C1 unfixed
Disposition, line 233: *"...the remainder are outstanding and listed in §8. **per** CO-022, a substantial revision returns..."*

### C2 — Round 5's C3 unfixed
Line 20: *"...it is not one candidate.** **what** recurs across the two bishops is not one evidentiary base..."*

### C3 — The rewritten read shares a filename and date with the version it replaces, with no version marker in the title
Both versions are `Doc04_Gesta_Targeted_Read_2026-09-14.md`. The supersession is stated in the first body paragraph, which is good practice, but the filename, the H1, and every citation of it elsewhere are identical between the two, so a reference to "the targeted read of 2026-09-14" is ambiguous in the record — and §8 and the Status line each cite it while describing the *first* version's findings (H7, H8).

---

## Fix-pass verification table — Round 5's 26 findings at `27ed339a`

| R5 | Subject | Status at HEAD | Evidence |
|---|---|---|---|
| H1 | Open Item 3 "classified Tensional"; residue sweep | **RESOLVED** | Line 211 now "classified **Supporting**"; sweep reproducible at 47 lines |
| H2 | §5 answers the trigger both ways; *Gesta* certified unread | **PARTIAL** | Trigger now answered once; "does not reopen", "non-reopening" ×2, "has **not** read", "would be met" all survive — R6 H1 |
| H3 | Open Item 2 self-contradicting in one sentence | **RESOLVED** | Line 210 now "not a **Primary**… but a **Supporting**" |
| H4 | Supporting certified on one clause of three; invented gloss | **PARTIAL** | §3 line 99 runs all three; §4 line 164 and Open Item 2 still one-clause — R6 M10 |
| H5 | Read's load-bearing inference unsupported; axis never stated | **PARTIAL** | Polarity fixed; axis still never stated; Finding 2 over-reads the other way — R6 H5, L7 |
| H6 | Census from apparatus; Constantinus/Lateran 649 | **PARTIAL** | Census withdrawn and Constantinus correctly withdrawn; replaced by a false band claim — R6 H4 |
| H7 | "Twenty-four lines" unreproducible; terms blind to §3 | **PARTIAL** | Reproducible at the Decision Log (47); **§8 still certifies the old four-term/24-line claim** — R6 H7; sweep still passed over line 97 — R6 M5 |
| M1 | CF V7.4 Tensional quotation with added emphasis, line 173 | **OUTSTANDING** | Byte-identical at its named site — R6 M6 |
| M2 | Status line "26 of Round 2's 27" | **OUTSTANDING** | Unchanged — R6 L6 |
| M3 | `mandat` count ~40% low | **PARTIAL** | Now 35/64; 64 unreproducible from named variants, and computed over a wrong domain — R6 M1, M2 |
| M4 | Act 230 is a sixteenth act | **RESOLVED** | 230 and 252 both added and verified at their lines |
| M5 | Lines 96 and 97 stale inside Candidate 5's subsection | **OUTSTANDING** | Both byte-identical; line 97 matched the widened sweep — R6 M5 |
| M6 | OCR-hazard disclosure inaccurate | **OUTSTANDING (regressed)** | Disclosure removed rather than corrected — R6 M7 |
| M7 | Decision Log line 510 carries a retracted claim | **OUTSTANDING** | No in-place correction at 505–512; and the pass's own earlier 2026-09-14 entry now carries three withdrawn claims uncorrected — R6 M9-adjacent |
| M8 | "Passes at the world level" stated flat | **PARTIAL** | Line 94 now scopes out ordinary clergy; the bold verdict is unchanged, and the Status line still says "both limbs" — R6 H8 |
| L1 | Four *capitula* cited "in sequence" | **RESOLVED (moot)** | Passage removed in the rewrite |
| L2 | 58-count span mixes *capitula* with acts | **PARTIAL** | Span narrowed; now excludes real acts instead — R6 M1 |
| L3 | "47 distinct `Name episcopus` forms" unreproducible | **PARTIAL** | Replaced by "93 raw speaker-tokens", also unreproducible — R6 L3 |
| L4 | Act-50 normalization spans three lines | **RESOLVED (moot)** | Citation replaced by act 158 |
| L5 | Act 158 presented without row 65's caution | **RESOLVED** | Now correctly diagnosed as a subscription — the rewrite's best finding |
| L6 | `concili-` never searched; Aurelius missed | **RESOLVED** | Searched; Aurelius act 40 is now the lead passage |
| L7 | Round 4's L1 on a line the pass edited | **OUTSTANDING** | Not addressed |
| L8 | Forces Framework rule attributed to §4 | **OUTSTANDING** | Line 97 unchanged — R6 L5 |
| C1 | "…in §8. per CO-022" | **OUTSTANDING** | Unchanged — R6 C1 |
| C2 | §5 Finding's bold nesting inverted | **RESOLVED** | Finding rewritten; all `**` balanced document-wide |
| C3 | §2 lowercase sentence start | **OUTSTANDING** | Line 20 unchanged — R6 C2 |

**Tally: 7 resolved (2 moot), 9 partial, 10 outstanding.** Against the pass's own report of "Round 5's remaining findings are unaddressed": inaccurate in both directions (L8).

---

## Audit of the rewritten *Gesta* targeted read

**Verdict: UNSOUND.** Not "overstated in a different place" — the rewrite's frame is false and one of its four evidence items is misattributed.

**What genuinely improved, and it is not trivial.** The `concili-` sweep was run and it found the best sentence in the file (Aurelius, act 40, 117492) — verified verbatim, right speaker, right act, and squarely on Doc_01 §4's axis. The polarity of 117505 is corrected and the speaker restored. Act 158's diagnosis as a subscription is new, correct, and explains an anomaly Registry row 65 recorded without a cause. The Constantinus/Lateran-649 withdrawal is right. The first version's episcopal-census claim is withdrawn. The strict `mandat` count reproduces exactly. Three of the four passages exist and say substantially what is claimed.

**What is unsound.**

1. **The band structure is false (H4).** 118500–125499 is not "Migne's own prosopographical footnote apparatus." It contains numbered acts 157, 158, 159, 171, 172, 173, 174, 223 and the entire mandate-subscription roll-call — roughly 80 act headers, 145 `mandav*` subscription formulae, and the 460 `episcop-` tokens the first version was counting. The high footnote density there is caused by Migne glossing the sees **named in the record**. The read measured density and inferred composition; it did not open the band. Its own act-158 citation falls inside it.

2. **A speaker is misassigned across a column boundary (H3).** *"Petilianus, act 9, line 116941 — illum tranquillissimum concilii locum"* is Marcellinus's edict in the right-hand column, regulating who may physically enter the conference venue. Petilianus's act 9 is the left column and contains no `concili-` token. The rewrite removed the first version's bleed disclosure and then made a bleed error.

3. **Finding 2 is self-refuted (H5).** `concil-` appears nowhere in Emeritus's speech. His objection is to the *mandatum* and its formalities — the instrument the read's own closing paragraph classifies as procuratorial and off-axis. The read applied that rule to the first version's evidence and exempted its own.

4. **Every count in Finding 3 is computed over the wrong domain (M1, M2, M3, M4, L3, L4)**, and the "small cast" conclusion that carries the Formation verdict is produced by excluding the subscription roll.

5. **The account of what the first version got wrong is accurate but selectively incomplete (L7):** it carries Round 5's polarity limb and drops Round 5's axis limb, which is the one that would have blocked Finding 2 and, downstream, §5's reaffirmation.

**On the read's own closing diagnosis.** It writes: *"All five are the same mechanism in different clothes: a check that proves something adjacent to the claim, then trusted because it returned something. The correction that mattered was not a better pattern but a different move — **enumerate the population and look at it**, rather than pattern-match against it."* That diagnosis is exactly right, and the rewrite did not follow it. It ran a **new pattern** — footnote-marker density per 500 lines — over the population, got a number, and trusted it without opening the band. That is the documented mechanism, one level up.

---

## The §5 reopening

**Is "reopened and reaffirmed" a legitimate discharge of item 10's "the finding is reopened rather than defended past the evidence"?**

**On form: yes, and this is real progress.** Round 5 found §5 certifying the trigger both met and unmet. §5 now says, once and in bold, that the trigger **is** met, that the 411 material **is** evidence Doc_01 never weighed, and that the finding is therefore reopened. It quotes item 10's consequent in full for the first time. The Decision Log surfaces the consequence rather than burying it. That is the right shape, and the pass deserves the credit for choosing the harder of the two available readings.

**On substance: no.** Three reasons.

1. **The reaffirmation answers an axis item 10 does not name (H2).** Item 10's axis is Cyprian's egalitarian theory against Augustine's hierarchical one — both in-world. Doc_01 §4 defines it as *"the appellate structure above the individual bishop **within his own communion**."* The reaffirmation disposes of the 411 evidence as a dispute with a communion outside the boundary. Either the evidence is cross-boundary and therefore off-axis — in which case the trigger is not met and the reopening is theatre — or it is on-axis, in which case its on-axis content is Aurelius's *universale concilium*, the Catholic delegation's *electi ab universali catholico concilio*, and Augustine's own subscription to that mandate: all **inside** this world, all unengaged. Doc_04 §3 concedes as much in its own words: *"the conciliar-authority claim at 411 is made by Aurelius."*

2. **Article 21's definition is quoted correctly and then used to answer the easier question.** "Within a single world" does exclude the Donatist pole. It does not exclude the Catholic pole, and the Catholic pole is a primate of Carthage stating in 411 that a *universale concilium* binds the limit of what he may do — which is, on Doc_01 §4's own framing, what Cyprian's 256 preface refuses. Whether that is "a meaningfully distinct pattern of… authority structure" from Cyprian's, or "merely a variation in detail," is the question item 10 commissioned, and §5 does not ask it.

3. **§5 does not actually hold the reopening anyway (H1).** The same line opens *"Candidate 5's own result does not reopen the strand-singular finding,"* calls the result "the non-reopening finding" twice, and certifies the *Gesta* unread with the trigger in the conditional. The Disposition calls it "the strand-singular non-reopening." So on the document's own face, the reopening is asserted in one sentence and denied in four.

**Is the "rival communion outside the boundary" claim supported at source?** Partly. Doc_01 §5 does place Donatism outside the world boundary, on a portfolio-level axis (Coach3's "external-management-within-unity versus internal-schism-into-division") it applies rather than makes, and Donatism's own Step 0 §3 B3 and Doc_01 adopt it. So the premise is real, not invented. Two qualifications: the sentence as written places **both** parties outside (M11); and Doc_01 §5's Article 3 argument is about **world** boundaries, not about which evidence counts for a **strand** test — importing it wholesale means that any evidence generated in a Catholic/Donatist proceeding is automatically strand-irrelevant, which would retire not just this axis but §4's rival-consecration-validity axis too, and would also retire most of the 411 record the same paragraph relies on to pass Persistence. The move proves more than the document wants.

**Assessment:** the reopening is a genuine procedural improvement and a substantive evasion. The right next step is not to re-close it — it is to argue the in-world half.

---

## CO-022 escalation assessment

**Category 1 (Representative identity/title):** does not apply.

**Category 2 (portfolio-level or cross-world):** does not apply to the reopening itself. Doc_04's Disposition asserts it does not apply because the reopening is "an application of Doc_01's own already-cleared §5 determination" — that reasoning is wrong (§5 reopened it, it did not apply it), but the conclusion on category 2 stands for other reasons: nothing here decides anything for another world.

**Category 3 (governance/methodology):** **arguably applies, and is not assessed.** The pass establishes, in practice, a working rule that a build document may change the status of a cleared companion document's finding on the strength of a caveat that companion document wrote for itself. Doc_01 §5 states plainly that this caveat is *"its own discipline rather than as a rule either governing text states"* and that **"Constitution Article 21 contains no reopening trigger,"* which "if anything runs the other way." A self-granted reopening mandate firing for the first time in this portfolio is a methodology precedent, and neither document says so.

**Category 4 (unresolved tensions the pipeline cannot close):** **applies, and the pass declines it.**

- Round 5 closed with *"CO-022 category 4 re-opened on the item-10 trigger question"* and asked for the reopening to be routed through category 3 or 4. The pass did not route it. Under CO-022's own rule that two reviews disagreeing are logged rather than quietly reconciled — a rule Doc_04 §7 Open Item 7 itself invokes for the Round 2 disagreement — this disagreement is not logged anywhere.
- The pass's own Decision Log states *"**Unresolved tensions: one raised, not closed**"* and then discloses rather than escalates. Doc_04's Disposition states *"**Unresolved tensions: closed**"* and *"Nothing in this document is now escalated."* The two records of the same pass give opposite answers (H6).
- The build-cycle's own fourth-category limb is "no contradiction with another cleared document exists." Doc_01 is cleared and self-disposed; its §5 and §8 item 10 still describe the finding as standing subject to a caveat **not yet fired**, while Doc_04 §5 now describes it as fired, reopened, and reaffirmed. The two cleared/undisposed documents now state different statuses for the same finding. That is the contradiction the limb tests for.

**This reviewer's assessment: escalate under category 4.** Not to reverse the reaffirmation — the substantive question (H2) is a construction question Doc_04 can answer — but because (a) a cleared document's finding has changed status and the cleared document does not know it, (b) two review rounds now disagree about whether that requires escalation and the disagreement is unrecorded, and (c) the pass's own two governing records contradict each other on the answer. "Disclosed for the project lead" in a decision-log entry is not escalation; it is the thing escalation exists instead of.

---

## Note on disposition

Not assessed. CO-022's precondition is not met — this pass has not been reviewed until now, seventeen of Round 5's findings are outstanding, and thirteen of Round 4's remain. `Doc_04_Gravity_Discovery.md` remains REVISED and undisposed, correctly.

---

## Has the failure mode migrated again, and into what form?

The remedy history, as the build records it: re-derive quotations at source (R2) → read the word-level diff (R3) → open every named destination (R4) → derive the destination set by search rather than by copying (R5) → widen the search terms and run explicit contradiction assertions (R6).

**Yes. It has migrated twice in this pass, in two different directions, and both are invisible to a widened search plus an assertion set.**

**1. Assertions test tokens; the defect lives in propositions.** The pass widened from four terms to ten and ran twelve assertions. One fired, on `unreopened`. At HEAD the document still says `does not reopen`, `non-reopening` twice, `has **not** read`, and `would be met` — four live denials of the pass's own headline change, one of them in the Disposition (H1). An assertion set written by the author who made the edit will contain the strings that author remembers writing. It cannot contain the paraphrase they forgot. **A widened search plus an assertion set cannot see a contradiction expressed in words the author did not think to assert over.** The only remedy that reaches it is propositional: enumerate the claims the pass changes, then require every sentence bearing on each claim to be read and classified — which is a reading task, not a grep.

**2. The domain of measurement was never itself checked.** This is the deeper migration, and it is the one that will recur. Every remedy in the history above operates **inside** a chosen domain: re-derive the quotation (at the line you chose), read the diff (of the file you chose), open the destination (in the set you derived), assert the contradiction (over the lines your terms matched). None of them asks **whether the domain is right**. The rewritten read chose its domain by a density measurement, got a number, and never opened the region it excluded — and so its band claim is false (H4), its counts are computed over a domain missing 145 of the file's mandate formulae and the whole subscription roll (M1), its own act-158 citation falls outside its own declared domain (H4), and its "small cast" conclusion — which carries the Formation verdict — is an artefact of the exclusion. The sweep over Doc_04 has the identical shape one level up: it swept the document and never asked whether §8, which it did not touch at all, was in scope (H7).

Every check this build has added is a check **within** a frame. The failure has moved to **the frame**. The next remedy is not another term, another assertion, or another destination list — it is: **state the domain the check runs over, then open a sample of what the domain excludes and show it is excludable.** Density is not composition; a matched line is not a read line; a swept document is not a swept section list.

**Predicted next form, if only assertions are widened again:** a pass that runs a correct, propositional assertion set over a document whose §8, Registry rows, and companion documents were never in the sweep's scope — and certifies consistency across a set it defined to exclude the inconsistent part. That form is already present in this pass (H7, M9): §8 and Registry row 65 both now contradict the document, and both were outside every check the pass ran.

---

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**
