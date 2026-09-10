# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 2 Independent Adversarial Review

**Reviewed documents (Revision 1, commit `d950535f`):**
- `World-Builds/Second-Century-Greek-Apologists/Step0_Movement_Scope_Confirmation.md` (Atlas I.35)
- `World-Builds/Latin-Apologists/Step0_Movement_Scope_Confirmation.md` (Atlas I.43)

**Prior round:** `Review-Artifacts/Step0_Round1_Review.md` (identical copy under both worlds), commit `09d94033`, verdict SUBSTANTIAL REVISION REQUIRED for both — 14 findings against I.35 (A1–A14, four HIGH), 9 against I.43 (B1–B9, four HIGH), plus a commissioned Era 1 sweep (Part C).

**Reviewer:** independent isolated agent. No involvement in drafting either document, in the revision, or in Round 1.

**Overall verdicts:**
- **I.35 (Second-Century Greek Apologists): SUBSTANTIAL REVISION REQUIRED** — two new HIGH findings, both introduced by the revision itself.
- **I.43 (Latin Apologists): SUBSTANTIAL REVISION REQUIRED** — no new HIGH finding, and all four Round 1 HIGH findings are genuinely discharged; but the paragraph that discharges the largest of them places Tertullian in the wrong city, and three of the revision's own new sentences contradict other new sentences in the same subsection.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**A note on method.** Nothing was accepted from the revision's own §6 "Revision history," and nothing was accepted from Round 1. Every finding below was re-derived directly: `records/<world>/` read file-by-file; `cic/corpus-map/*.yaml` parsed and cross-joined with `yaml`; `cic-website/data/world-census.json` parsed and string-tested; the Constitution and the Step 0 Methodology extracted from their `.docx` and read in full; the vendored XML in `cic/texts/` parsed and word-counted with `lxml`, independently of both Round 1's table and the revision's numbers. Where the revision presents something as a direct quotation, the quotation was matched character-for-character against its source. Round 1's own findings were re-tested as claims, not adopted as premises — **two of them turned out to be wrong, and one of those two was copied into the revision as a verified check** (see N4, and the note at B4).

**Working-tree note.** Both documents and both Round 1 artifacts live on `_review2/apologists` at `d950535f`, not at the worktree's own `HEAD` (`5eb39472`). The worktree was detached to `d950535f` for this review. No content was altered; this artifact is the only file written.

---

## Part A — I.35, The Second-Century Greek Apologists: Round 1 findings re-tested

Each entry states what the revision claimed to fix, what the repository actually shows, and whether the result is **(a) genuinely resolved**, **(b) addressed in form but wrong or incomplete in a new way**, or **(c) a new defect**.

### A1 [was HIGH] — Tatian is a built Syriac figure. **(b) Addressed in substance; the new material misreports the record it cites, and is one-sided.**

The underlying fact is real and now carried properly: `records/syr/figure/syr.figure.tatian.md` and `records/syr/source/syr.source.tatian-address-to-greeks.md` both exist; the source record is `evidentiary_weight: load-bearing`, `verification_state: verified-direct`; the corpus-map note ("Tatian sits awkwardly across two entries… Mark may want a ruling on where his voice sits") is verbatim; and "Every argument for Tatian belonging to the Syriac East runs through the statement that he was an Assyrian" is verbatim. A second binding ruling now sits in §4 item 2. That is the right shape.

Three problems in the new text:

1. **The revision says the syr source record's "THE ENCRATITE CHARGE, HANDLED HONESTLY" section states "plainly that the charge is real."** It does not. The section reads: *"Eusebius accuses him of it and this world's figure record carries the charge. The Address is not a confession of it and must not be read as one… What the Address supplies is the material for a reader to weigh the charge rather than only receive it."* The record deliberately stops short of asserting the charge's truth; that restraint is the point of the section. The revision's paraphrase reverses the one thing the record is careful about, in the same sentence that holds it up as the standard to be modelled.

2. **Every fact that makes Syriac's claim on Tatian *weaker* is omitted.** `syr.figure.tatian.md` is `evidentiary_weight: corroborating` (not load-bearing), `narratable: false`, and its own body reads: *"Boundary-adjacent: Tatian predates the window and stands outside it… the figure record exists so the voice can name the harmony's maker honestly, charge included, **without adopting him as a founding teacher**."* The revision quotes only the strong half ("leave no room for treating this as settled in this candidate's favour"). On the record's own terms, Syriac claims the Diatessaron's maker, explicitly not the man as a narratable figure — which is precisely the distinction that would make this ruling *easier* than the Justin one, and the revision inflates it into an equal-weight second ruling that then drives §3's Tier language and §4's ordering.

3. **Tatian is not on I.35's census `voices` list at all.** The revision's own new §1 correctly enumerates the seven: Quadratus, Aristides, Justin, Athenagoras, Theophilus, Melito, the writer to Diognetus. Tatian appears in the census only in the `sourcing` field. He nonetheless anchors B1, §4 items 2 and 3, and half the Tier conditional. The census/corpus-map asymmetry is real, checkable in one read, and unremarked.

### A2 [was HIGH] — PAHC already claims Justin's argument, his address to power, the Trypho debate. **(b) The correction itself is right; its replacement claim is newly wrong.**

All three quotations added in §3 B3 verified verbatim against the records: `pahc.quote.moses-is-more-ancient.md`'s `divergence_note` ("an apologetic claim about chronology made to a pagan audience"); `pahc.quote.those-who-lived-reasonably-are-christians.md`'s note ("which cites this exact chapter for 'the Logos present in every race of men'"); `pahc.quote.the-memoirs-of-the-apostles-are-read.md`'s divergence note; `pahc.figure.justin.md`'s `bridge_line`; `pahc.source.justin-dialogue.md`'s WEIGHT note and its "Ways-That-Never-Parted" caution; and `pahc.source.justin-first-apology.md`'s "this world's clearest inside evidence that the rival movements were live, contemporary, and undefeated." `locus: whole work` on both Justin works confirmed. The Round 1 finding is answered.

**But the replacement residue is asserted on a false parenthesis.** §3 B3 offers, as the lead candidate for genuinely open territory, *"the **Second Apology** in its own right (PAHC's roster names only the *First Apology* and *Dialogue*)."* `cic/corpus-map/post-apostolic-house-church.yaml` carries **eight** Justin works, including *The Second Apology* at `confidence: assigned` — plus *On the Resurrection (fragments)* and *Other Fragments from the Lost Writings of Justin*, neither of which is even on I.35's own map. "PAHC's roster" is true only of PAHC's compiled `records/`, and the document uses "roster" in the corpus-map sense everywhere else, including three paragraphs earlier. The one concrete piece of open territory the revision names is claimed by the neighbour at the level the document itself treats as authoritative.

The hedging around it ("not yet verified against a full read… Doc_01 must verify this residue directly") is good discipline and is noted. The flat parenthetical is not covered by that hedge.

### A3 [was HIGH] — the Augustine precedent misdescribed. **(b) + (c). The Augustine correction is right; the rule the revision puts in its place is refuted by the precedent cited two sentences later. See N2.**

Verified: `records/hal/figure/hal.figure.augustine.md`'s "STRICTLY AN OUTSIDE VOICE" clause; Donatism's Article 23 placement; Augustine's native home in LPC; `alx.source.athanasius-vita-antonii.md`'s bounding rule *"no Alexandrian record may treat desert formation logic as constitutively Alexandrian on this text's authority"* (verbatim); and Mark's *"THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS"* in `cic/corpus-map/latin-apologists.yaml` (verbatim). Three options in place of two is a genuine improvement.

The new generalization is not, and it is graded separately at **N2** because Round 1 never touched it.

### A4 [was HIGH] — the Article 21 finding built on a bundling that does not exist. **(a) Withdrawn correctly — with a new arithmetic error, and a much larger fact still missing.**

Independently confirmed: `cic/corpus-map/greek-apologists-second-century.yaml` holds sixteen works and **none** of Hegesippus, Dionysius of Corinth, Rhodon, Polycrates, Serapion or Apollonius is among them. Hegesippus maps to `post-apostolic-house-church`, `alexandria-catechetical`, `montanism-the-new-prophecy`, `novatianism` (and the `UNATTRIBUTED` registry); Dionysius of Corinth to `post-apostolic-house-church` only. The revision's §1 and §2 A5 corrections are accurate. The withdrawal is right.

**New arithmetic error.** §3 B1 says: *"Beyond the sixteen-work core, the corpus map also carries: three works transmitted under Justin's name…; Aristo of Pella's fragments; and the Ambrose hypomnemata."* Those five items **are** five of the sixteen. The map holds sixteen works in total, not twenty-one. (Round 1's A5 used the same misleading phrasing; the revision adopted it while presenting the paragraph as a completed roster inventory.)

**And the fact that actually governs A4's replacement question is absent — see N1.**

### A5 [was MODERATE] — roster attribution flags unnamed. **(b) Addressed; two small inaccuracies.**

The three pseudonymous Justin works, Aristo, the Ambrose piece and the Diognetus date caveat are now all named. Two slips:
- The note *"transmitted under Justin, widely doubted"* is the note on the *Hortatory Address* and *On the Sole Government of God*. The *Discourse to the Greeks*'s own note reads differently: *"Printed under the JUSTIN MARTYR div1; authenticity has long been questioned."* The revision attributes the single quoted phrase to all three.
- Aristo of Pella is **triple**-assigned (`greek-apologists-second-century`, `post-apostolic-house-church`, `ebionite-nazoraean-current`), not dual. The revision names two.

### A6 [was MODERATE] — the Marcion/A5 rule and the IJC citation. **(b) Citation fixed; the corrected rule statement is itself selectively quoted.**

Verified: census I.20 `status` is `Excluded - Doctrinal Floor (C1)` and its `statusDescription` reads *"Exclusion is not a judgment of unimportance"*; IJC's §2 A5 sentence is reproduced verbatim, with the elision of "on the doctrinal floor," correctly marked. The inversion Round 1 caught is gone.

**But the new rule statement quotes half of A5.** The Methodology's actual text (verified in `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`) is two sentences, not one: *"A movement's historical rivals… are not separately assessed for inclusion as their own worlds under this section. Per Article 23, they appear, where relevant, as an included world's own opponents, within that world's own reconstruction, **not as independently screened candidates**."* The revision quotes only "under this section" and concludes that *"the rule says nothing against a rival having been screened in its own right elsewhere."* The clause it omits says something against exactly that, on its face. IJC's own §2 A5 — the document the revision is correcting its citation of — quotes both sentences in full. The practical reading the revision reaches is defensible and matches IJC's practice; the assertion that the rule "says nothing against" it is not, and it is made in a paragraph whose entire purpose is to state the rule correctly.

### A7 [was MODERATE] — the Trypho obligation mis-routed. **(a) Genuinely resolved.**

Article 23's "Governing external opponents" paragraph verified verbatim in `CiC_L1_Constitution_V2_2.docx`, including the sentence the revision quotes. Article 20's own scope clause — *"It does not extend to the community's external opponents… That is governed by the Writing-From-Inside Principle in Article 23"* — confirmed. `pahc.source.justin-dialogue.md`'s named Doc_01 §2.1 caution confirmed. The Aristo/Ebionite adjacency and the *Dialogue* ch. 47 note are both real and are quoted accurately from the corpus map. Clean fix.

### A8 [was MODERATE] — the Tatian/Encratite disclosure duplicated a better model; and a double standard on dating. **(b) First half fixed; second half untouched and unreported.**

The Bardaisan mis-invocation is gone and §4 item 3 now points at Syriac's existing treatment. Good.

Round 1's second half is not addressed at all. §2 A2 still reads *"The Address is generally read as predating or independent of that later turn"* — an uncited appeal to consensus on a disputed dating, load-bearing for an A2 clearance — while the sibling document's §4 item 1 continues to demand *"a cited scholarly judgment"* for Minucius Felix and Commodian. The §6 revision history describes A8 as though it consisted only of the first half ("Tatian's own Encratite disclosure duplicating a better existing model without citing it") and then claims all findings were "addressed directly above."

### A9 [was MODERATE] — the A1/A2 routing misattributed to IJC. **(b) One mis-citation replaced with another.**

The IJC characterization is now correct and verified against IJC §2 ("both A1 and A2 apply, to different phases of the same continuous movement… not a forced either/or"), including the Round 1 finding about the invented rationale.

The substitute does not hold. The revision says the on-point precedent is *"LPC's own cleared Step 0 §2, which runs A2 as the sole governing test for Cyprian's wholly pre-Nicene phase and says of the Procedure's 'as applicable' language 'nothing else'."* Read directly:
- LPC's "nothing else" is not about the A1/A2 routing. It appears in LPC's century-gap discussion and bounds **what Step 0 tests at all**: *"The Procedure's own screening instruction is 'Test each candidate against A1 (and A2 or A3 as applicable)' — nothing else. None of Section A, and none of Section B's five criteria… tests Article 3's 'sufficient historical coherence.'"* The quotation has been moved onto a different proposition.
- LPC does **not** run A2 as the sole governing test for the world. It runs *"A1 for Augustine, A2 for Cyprian"* — i.e. LPC is itself a straddling case, resolved exactly as IJC resolved its own. The ground on which the revision rejects IJC ("does not describe a window that never reaches 325") applies to LPC in identical force.

On the evidence, **neither cleared confirmation supplies a precedent for a candidate whose window never reaches 325 at all**, and the honest statement is that there is none yet. The outcome (A2 governs) remains defensible on the Procedure's plain text; the warrant is misattributed for the second round running.

### A10 [was MODERATE] — the Article 4 provenance line, and restating the floor. **(b) Provenance fixed; the floor is now miscounted.**

The false "quoted verbatim in IJC §2" claim is gone, and the header now says the document *applies* rather than reproduces Article 4. Good.

**The replacement enumerates four commitments and calls them five.** Article 4's list, verified in the Constitution, is: (1) *One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen*; (2) the Son, of one Being with the Father; (3) truly human; (4) death/burial/resurrection/ascension/return; (5) the Holy Spirit as Lord and giver of life. The revision's header lists items 2–5 and labels them "the floor's five commitments." The dropped item is the first.

This is not a cosmetic miscount. It is the **same defect LPC's own Round 1 review recorded as a HIGH finding** — *"an independent restatement of Article 4's floor that both violates Article 4's own textual prohibition and drops one of its five commitments"* — and LPC's cleared fix is to quote all five exactly and say so (*"Article 4's five commitments, quoted exactly, not paraphrased or abridged"*). The revision cites LPC as its model at A1 in the same document and does not follow it here. And the omitted commitment is substantively live for this pair: it is the one Marcion fails (§2 A5's own subject), the one Minucius Felix's monotheism-only apologetic actually argues, and the one Lactantius' two-spirits cosmology brushes in the sibling document.

### A11 [was MODERATE] — the "never a per-world process" prohibition. **(b) Half-answered.**

The prohibition is now quoted verbatim and answered in §3's opening framing note, which is what Round 1 asked for, and the answer given ("a considered signal… not a disposition this document is entitled to make on its own") is honest. But the note sits under Section B only. §2 still renders flat verdicts — *"Resolution: A2 clears"*, *"**Clears Section A.**"* — with no equivalent disclaimer, while §5 describes the document as one that *"runs full A1–A5/B1–B5 tests"* and contrasts it with an instrument that *"deliberately renders no floor verdicts."* The document therefore disclaims its Section B output and not its Section A output, having just told System Hub it produces both.

### A12 [was MODERATE] — the Era 10 / Pre-Step-0 process finding. **(a) Genuinely resolved, and independently confirmed.**

`CiC_Step0_Era10_V1_0.md` verified as an era-wide run with the six-section structure the revision describes (§1 Survey update, §2 Section A, §3 Section B, §4 Source bases, §5 Gravity-bounded dates, §6 Tiered output). `CiC_World_Atlas_PreStep0_Survey_V0_1.md` verified: *"It renders no floor verdicts of its own"* and *"A signal, not a B1 score"* both exact. §0 and §5 are now accurate and better-scoped than the prior draft. Clean fix.

### A13 [was LOW] — the block quotation that was not one. **(a) Genuinely resolved.**

§1 no longer uses block-quote form for composed text. The naming-note quotation matches the census exactly, with the elision of *"and a survey may well decide it:"* correctly marked. The Hegesippus/Dionysius correction is accurate as verified at A4.

### A14 [was LOW] — small checkable items. **(b) Two of three; one dropped, one new imprecision.**

- Melito at `anf08` div2 x.v: confirmed (11,288 words). ✓
- The *Epistle to Diognetus* date caveat is now quoted from the corpus map. ✓
- **Dropped without mention:** Round 1's note that the vendored ANF Melito predates the twentieth-century recovery of the Paschal homily the census's own `voices` entry names, so that text is *not* in `cic/texts/`. B1 still says only "Melito's own fragment specifically at div2 x.v," and §6 claims "small unchecked citation details" were all addressed.
- **New:** B1's compressed sentence — *"Aristides (recovered 1889) and the ten fragmentary sub-apostolic voices collected as 'Remains of the Second and Third Centuries' (`anf08`) are also vendored"* — reads as though Aristides sits in `anf08`. He is in `anf09` (corpus map locus `div2 13.3-13.4`), a file this document never names.

---

## Part B — I.35: new defects the revision introduced

### N1. [HIGH] Not one of the sixteen works on I.35's own corpus map is assigned to I.35 alone — and B3's uniqueness case is written as though most of the roster were unclaimed.

Cross-joined directly (`greek-apologists-second-century.yaml` × `post-apostolic-house-church.yaml` × `syriac-edessa-nisibis.yaml`):

| Works on I.35's map | 16 |
|---|---|
| Also assigned to `post-apostolic-house-church` | **15** |
| Also assigned to `syriac-edessa-nisibis` | 2 (Ambrose *hypomnemata*; Tatian's *Address*, which is on all three) |
| Assigned to `greek-apologists-second-century` **alone** | **0** |

Every non-Ambrose row carries the same 2026-08-26 note verbatim: *"greek-apologists-second-century added alongside… **pahc is kept: the era and church-world really are its**."* Aristides, Athenagoras ×2, Theophilus, Quadratus, Melito, Diognetus, Aristo, and all six Justin rows are co-assigned to a built, live world.

The revision engages this fact for Justin (three works), for Tatian (one work) and for Aristo and the Ambrose piece (two works, on their *other* dual assignments). It nowhere states that the condition is universal. Consequently:
- §3 B3's second bullet ("no figure or source overlap found") is true at records level and misleading at corpus-map level, which is the level the rest of the document treats as authoritative.
- The Tier sentence's *"the remaining **confirmed-unique** roster"* has no referent. Nothing on the map is confirmed unique.
- §2 A5's replacement Article 21 question — whether five specific items "belong in this candidate's own figure roster as-is" — is a narrower version of the question the map actually poses, which is whether *any* of the sixteen is this candidate's rather than PAHC's.

This is the largest single fact about the candidate's B3 case and neither round has stated it. It does not necessarily lower the Tier — corpus-level co-assignment is explicitly non-exclusive by design, as the `ebionite-nazoraean-current` notes say — but a B3 that does not name it is not a B3.

### N2. [HIGH] The revision's newly-asserted project pattern — "not co-ownership" — is refuted by the precedent it cites two sentences later.

§3 B3 states: *"The pattern the project has actually built is: **native to one world; a declared outside voice, or a declared opponent, everywhere else** — not co-ownership."* It then cites, as the "genuinely on-point precedent," the two Athanasius *Vita Antonii* source records.

Checked directly:
- `records/alx/source/alx.source.athanasius-vita-antonii.md` — `register: emic`, `evidentiary_weight: corroborating`, cross-build flag inside the `work` field, *"held open with the Desert world."*
- `records/desert/source/desert.source.athanasius-vita-antonii.md` — `register: emic`, `evidentiary_weight: load-bearing`, with a register note explaining that emic is *deliberate* despite the outsider author.
- **`records/alx/figure/alx.figure.antony.md` and `records/desert/figure/desert.figure.antony.md` both exist.** Both `register: emic`, both `narratable: true`. The Alexandrian one says outright: *"CROSS-BUILD FLAG at full strength: Antony belongs at least as much to the Desert world… as to Alexandria, and the attribution is held open."*

One work and one figure, held emically by two built, live worlds, with reciprocal bounding rules and deliberately asymmetric weights — neither an outside voice nor an opponent. That is co-ownership, held open by design. The sentence and its own supporting citation cannot both stand.

Two consequences the document does not see:
1. **Option (a) is mislabelled.** "The Athanasius/HAL model" fuses two different mechanisms. HAL's Augustine is *"STRICTLY AN OUTSIDE VOICE."* Alexandria/Desert's Antony is a co-held native figure. Whichever is meant for Justin, it needs naming as one and not the other.
2. **There is a fourth option, and it is the only one the project has actually built at figure level:** Justin co-held by PAHC and this candidate, `emic` in both, with reciprocal cross-build flags and asymmetric weights, attribution held open. The revision's rule excludes it by assertion.

A related, smaller point in the same paragraph: the revision quotes Mark's ruling describing the Athanasius case as *"the Vita Antonii is desert's and Against the Arians is Alexandria's, one author, two entries, split by work"* and calls it "the project's actual mechanism," in the same sentence as it cites the two records showing the *Vita* is held by both. The ruling and the records say different things and the document does not notice.

### N3. [MODERATE] "The Ambrose *hypomnemata* on Quadratus" is a fabricated attribution, and it reaches a binding §4 obligation.

The work is `div2 9.18` of `anf08`, registered in `UNATTRIBUTED.yaml` as: *"'A memorial (hypomnemata) which Ambrose, a chief man of Greece'— the volume's endnote shows it is a Syriac form of the Greek Discourse to the Greeks ascribed by many to Justin; the 'Ambrose' frame is not an identifiable author. NOT Ambrose of Milan."* The corpus-map row calls it *"Ambrose: a memorial (hypomnemata) **addressed to the Greeks**"* and pairs it with the pseudo-Justin *Discourse*. It has no connection to Quadratus of any kind.

"on Quadratus" appears three times: §2 A5, §3 B1, and (by reference) §4 item 4, where it forms part of a binding Doc_01 instruction. Round 1 named the work correctly; this detail is new in the revision.

*(Aside for Doc_01, not a finding against the document: the dual assignment the revision claims for this piece is genuine — `cic/corpus-map/_staging/anf08_*.yaml` carries two rows, `greek-apologists-second-century` and `syriac-edessa-nisibis`, and both merged maps hold it.)*

### N4. [MODERATE] The Alexandria bullet's supporting check is false, and was imported from Round 1 as though independently verified.

§3 B3 states: *"verified directly against `records/alx/`, which contains no figure or source record for any name on this candidate's own roster. (The apparent hits on a naive search — **Clement's own citations of Tatian, Athenagoras, and Theophilus inside the *Stromateis*** — are Clement's citations of them, not Alexandria's own claim on their voices.)"*

Run directly: every occurrence of "tatian", "athenagoras" or "theophilus" in `records/alx/` is inside the vendored **filename** string `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, in an `edition:` field — six files, one line each. There are no Clement citations of any of the three anywhere in Alexandria's records. (`alx.source.alexandrian-canonical-answers.md`'s "Theophilus" is Theophilus of Alexandria, bp. 385–412 — a different man again.)

The conclusion is correct, and in fact stronger than stated. The stated verification is not. Round 1 made this same error at its C7 while diagnosing the identical pattern correctly for I.43 in its own "what checked out clean" section (*"the apparent grep hits are all ANF volume-title strings inside `edition:` fields"*). The revision adopted the wrong one and re-badged it "verified directly against `records/alx/`." This is precisely the failure the pair was revised to remove.

### N5. [MODERATE] The fallback roster in the Tier sentence drops three of the census's own seven named voices.

*"If both rulings go against sharing… the remaining confirmed-unique roster is Athenagoras, Theophilus, and Aristides, plus the pseudonymous-Justin works and Aristo of Pella's fragments."*

Quadratus, Melito of Sardis and the *Epistle to Diognetus* are all on the census `voices` list, all on the corpus map at `confidence: assigned`, and none is subject to any contested claim the document raises. The *Epistle to Diognetus* is the one the census itself calls *"the most quoted of all of them."* The prior draft's version of this sentence was also incomplete; the revision rewrote it specifically, upgraded it to an enumeration of "the remaining confirmed-unique roster," and made it wrong in a different way. It then reasons from that understated roster to *"a real but visibly thinner candidate."*

### N6. [MODERATE] §2 A2's heading contradicts §2 A2's body and its own resolution line.

Heading: *"A2 — Pre-Nicene continuity: clears, with **two figures** requiring honest disclosure rather than exclusion."* Body: *"Justin, Athenagoras, Theophilus, and Aristides clear cleanly and strongly"*; **only Tatian** requires a disclosure. Resolution: *"A2 clears, with **Tatian's** specific and bounded caveat carried forward"* — singular. The prior draft's heading read "one figure"; the count was raised to match the two *rulings* added at §3/§4, which are B3 uniqueness questions, not A2 continuity disclosures. This is the IJC-Round-2 pattern exactly: a revised sentence left contradicting an unrevised sibling in the same subsection.

### N7. [LOW] §4 item 7's sweep status omits PAHC and does not credit the instrument that discharged it.

*"Desert, Hieronymian, Imperial-Juridical, Cappadocian, and Alexandria are now confirmed clean directly against their own records. Syriac is not clean (item 2). This sweep is now materially complete."* PAHC — the world with by far the largest overlap, and the subject of §4 items 1 and 5 — is named in neither column. Separately, the Era 1 material now reported in §3 B3's last three bullets (Ebionite/Nazoraean via Aristo and *Dialogue* 47; the Montanism/Encratism check; the remaining entries) was performed by the Round 1 review's Part C, which explicitly proposed that these items be "marked partially discharged by this review." The document presents them as its own checks and cites Round 1 nowhere in §3 or §4. IJC's own Round 1 review recorded an uncited-prior-treatment finding of exactly this shape and IJC's fix was to credit the source by name.

---

## Part C — I.43, The Latin Apologists: Round 1 findings re-tested

### B1 [was HIGH] — Tertullian absent from the document. **(b) Substantively addressed; three new errors inside the fix.**

The structural repair is real: §2 A5 now centres on Tertullian, §3 B3 opens with an I.17 bullet, §4 item 4 replaces the old item 4, and the Tier's comparative claim against I.35 is withdrawn. Verified independently: `cic/corpus-map/tertullian-s-voice.yaml` holds **33** work rows, including *Apology (Apologeticus)*, *Ad Nationes*, *To Scapula*, *The Soul's Testimony* and *An Answer to the Jews*; LPC `Source_Registry.md` row 29 classifies the corpus **Excluded / Named Comparandum**; and the quoted clause *"he predates Cyprian's own episcopate by decades, wrote as a lay apologist rather than this world's own bishop-centered pastoral office"* is verbatim.

**(i) [MODERATE] Tertullian is placed in the wrong city, in the sentence that carries the fix.** §2 A5: *"the entire Latin apologetic corpus proper, in one man, **writing from the same city and roughly the same years as Minucius Felix**."* Census I.17 `region`: **"Carthage."** Census I.43 `region`: "Rome and Ostia; Sicca in Numidia; Nicomedia and Trier." Minucius Felix is a Roman advocate whose dialogue is set at Ostia. The years overlap; the city does not. And the error runs against the document's own interest: Round 1's B1 also observed that **Carthage is excluded by a boundary I.43 never states**, and B5 — unrevised — still claims *"Rome, Numidia, and the two imperial capitals"* as a scale strength without naming that exclusion. The revision has replaced a silence about Carthage with a claim that erases it.

**(ii) [MODERATE] "Named first" contradicts the document's own new §1.** §3 B3: *"the candidate's own census entry **names Tertullian first** among its `voices`."* §6 repeats it. The census `voices` array runs Minucius Felix, Arnobius, Commodianus, Lactantius, **Tertullian** — fifth and last — which the revision's own new §1 states correctly (*"names five figures, not four: Minucius Felix, Arnobius of Sicca, Commodian, Lactantius, and… Tertullian"*). Round 1 asserted "first"; §1 corrected it; §3 B3 and §6 kept it. The document now says both.

**(iii) [MODERATE] LPC's reasoning is quoted selectively, and the half that cuts the other way is dropped.** Row 29 gives three reasons. The revision quotes the first two and argues that the second *"is not a reason to exclude him from a lay apologist's own world."* Fair as far as it goes. The third reason is: *"and — per Step 0's own attribution — is credited with **forging** this world's own theological vocabulary, not with speaking as this world's own voice."* That reason transfers to I.43 straightforwardly, and the census's own I.43 `legacy` field states the same thing about the same man: *"The Latin vocabulary of Christian argument was largely made here, and in Tertullian's hands at the same time."* The document builds "LPC's reasoning cuts against this candidate" on the half that supports the conclusion and drops the half that supplies I.43 its readiest affirmative answer. The hedge ("supplies a model but not an automatic answer") is good; the selection under it is not.

**(iv) [LOW] The census's own stated reason for the separation is still not engaged.** `relationsSummary` for I.43: *"It touches tertullian-s-voice, which begins the enterprise and is **kept separate because a voice that distinct is its own entry**."* Round 1's C2 disposition asked the draft to *"either adopt that reason and say so, or contest it — not omit it."* The revision quotes the `voices` line instead and does neither.

### B2 [was HIGH] — Minucius Felix's Christology. **(b) The mischaracterisation and the foreclosure are both fixed; the count is off, and the clearance's own warrant is still unstated.**

Re-counted independently from `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, `div2 iv.iii` (23,819 words including editorial apparatus):

| token | occurrences |
|---|---|
| `\bJesus\b` | **0** ✓ as claimed |
| `\bSon of God\b` | **0** ✓ as claimed |
| `\bincarnat\w*` | **0** ✓ as claimed |
| `\bChrist\b` | **2** — the revision says "exactly once in the entire work" |
| `(?i)\bcrucifi` | **2** — not mentioned |

The two `Christ` hits are the ANF chapter XXXVII *Argument* heading (*"Confession of Christ's Name"*) and an editorial footnote citing Athenagoras (*"Legat. pro Christ., ch. xxviii."*). The two `crucifi` hits are the ch. IX *Argument* heading (*"They Worship a Crucified Man"*) and an editorial gloss inserted into ch. XXIX (*"[A reverent allusion to the Crucified, believed in and worshipped as God.]"*). All are apparatus, not Minucius' prose, so the substantive finding is untouched and is confirmed: **there is no positive Christological statement anywhere in the work.** Chapter XXIX reads as the revision describes it, and the move to Egyptian god-kings is immediate.

The problem is that the number now carries a binding instruction. §4 item 3 tells Doc_02 to *"disclose the absence as measured (zero 'Jesus,' one 'Christ' in an editorial heading)."* The count is presented as a hard measurement, states no exclusion rule, and does not survive an unrestricted count of the vendored division. Doc_02 will reproduce it.

**The half of B2 that went to the A2 clearance itself is unaddressed.** Round 1: *"The clearance therefore rests entirely on argument-from-silence plus external inference — which may well be right… but is not what 'clears, with a disclosure' describes."* §2 A2 now states the absence sharply, calls the scholarly question live, declines to resolve it — and then the Section A conclusion still says *"**Clears Section A.** A2 is satisfied for all four core figures"* with no statement of what the clearance rests on for the figure whose surviving text affirms none of Article 4's commitments 2–4.

### B3 [was HIGH] — Lactantius cleared without qualification. **(a) Genuinely resolved, and independently confirmed.**

Jerome, *Ep.* 84.7 (to Pammachius and Oceanus) is a real letter, correctly located, and accurately characterised: Lactantius *"in his letters, and especially in those to Demetrianus, altogether denies the substance of the Holy Spirit and by a Jewish error says that it is referred either to the Father or to the Son."* Not fabricated, not misattributed. *Divine Institutes* VII's chiliasm and II.8–9's two-spirits cosmology are correctly located and are the standard difficulties. Mapping the charge onto Article 4's fifth commitment is right: the Constitution's fifth item is indeed the Spirit. §4 item 5 is new and appropriate.

**[LOW] One qualifier lost.** Round 1 carried Jerome's own locus ("in his letters, and especially in those to Demetrianus"); the revision drops it. Those letters are lost and are not in `cic/texts/`, so §4 item 5's disclosure obligation as written reads as though the charge attached to the vendored *Divine Institutes*. Doc_02 needs that distinction to write the disclosure honestly.

### B4 [was HIGH] — the Lactantius/IJC boundary already ruled. **(a) Genuinely resolved — with a new self-contradiction three lines later.**

Verified verbatim in `cic/corpus-map/latin-apologists.yaml`, on the *Divine Institutes* row, and the three companion rows each record the `provisional` → `assigned` rise. `grep -rn "Divine Institutes" records/` returns zero across all seven built worlds. §3 B3 and §4 item 6 now state the ruling correctly and route Doc_01 to cite rather than re-derive it.

*Round 1 error not inherited, and worth recording:* Round 1's B4 said the ruling was *"dated eleven days before the draft."* 2026-08-27 to 2026-09-10 is **fourteen** days. The revision makes no arithmetic claim and correctly did not repeat it.

**[MODERATE, new] §3 B3's own conclusion inverts the finding.** *"**B3 passes**, with one new binding item (Tertullian) replacing what the prior draft **wrongly treated as settled** (the IJC boundary)."* The prior draft treated the IJC boundary as **open** — that is the whole of Round 1's B4, and it is what the same subsection's own bullet says (*"not open Doc_01 work, as the prior draft claimed — it is already resolved"*), what §4 item 6 says (*"This is not open Doc_01 work"*), what the Tier conclusion says three lines below (*"the Lactantius/IJC question the prior draft treated as open is in fact already settled"*), and what §6 says. One new sentence, contradicting four others, in the subsection it summarises.

### B5 [was MODERATE] — IJC's claim on *De Mortibus* understated. **(a) Genuinely resolved.**

`records/ijc/` confirmed: `ijc.source.lactantius-de-mortibus` is `evidentiary_weight: load-bearing` and is referenced by exactly **nine** other records (`ijc.gravity.church-state-alliance`, `ijc.figure.constantine`, `ijc.story.dream-before-battle`, `ijc.contested.constantine-conversion`, `ijc.quote.milan-edict`, `ijc.quote.lactantius-dream`, `ijc.force.constantine-alliance`, `ijc.search.anf07-lactantius`, `ijc.search.f6-e-negative-sweep`). The Edict of Milan / ch. 48 characterisation is accurate. Clean fix.

### B6 [was MODERATE] — Arnobius' provenance. **(a) Genuinely resolved, and independently confirmed.**

Jerome, *De viris illustribus* 79 is as the revision now states it: Arnobius, still a pagan, was driven toward belief by dreams, **could not obtain faith from the bishop** whom he had always attacked (*neque ab episcopo impetraret fidem quam semper impugnaverat*), wrote the books against his former religion, and thereby obtained the covenant as by pledges. The direction is now correct and the prior draft's reversal is gone. The *Chronicle* notice sits at 326/327, so "ad ann. 327" is within the ordinary range. The census hedge *"if Jerome is to be believed"* is verbatim. The Book II *media qualitas* description remains accurate. Clean fix.

### B7 [was MODERATE] — Minucius Felix's dating and I.33. **(a) Genuinely resolved.**

Census sourcing note verified (*"Two of the four authors are barely datable: Minucius Felix within a century, Commodian within three"*); census I.33 verified at c. 200–268, Rome, `voices` built around Callistus and Hippolytus. §4 item 1 now covers both authors and names the I.33 placement question. Clean fix.

### B8 [was MODERATE] — the structural findings shared with I.35. **Mixed, tracking Part A.**

- Article 4 provenance (A10): the false quotation claim is gone here too. I.43 does not itself enumerate the commitments, and its §2 A2 correctly identifies the **fifth** commitment as the Spirit. Fine as written — but it inherits by reference a header formula that miscounts in the sibling document.
- A1/A2 routing (A9): the LPC mis-citation is carried here in compressed form (*"on LPC's own precedent, which runs A2 alone as the governing test for a wholly pre-Nicene phase"*). Same defect as A9 above.
- "Never a per-world process" (A11): answered in one carried sentence, thinner than I.35's, and with the same asymmetry — Section A's flat clearances go undisclaimed.
- Block quote (A13) and Era 10 / Pre-Step-0 (A12): both fixed.

### B9 [was LOW] — roster and scale details. **(b) Two fixed; one fixed into a new imprecision.**

- Commodian's *Carmen apologeticum* now correctly excluded and stated. ✓
- The Great Persecution end-date now correctly handled (Maximinus Daia in the East to 313). ✓
- **The *Epitome of the Divine Institutes* is now listed as a co-ordinate vendored work — and it is a division inside the *Divine Institutes* whose word count already contains it.** Parsed directly: `div2 iii.ii` (*The Divine Institutes*) = 241,990 words, and its children are Books I–VII **plus** `div3 iii.ii.viii`, *The Epitome of the Divine Institutes*, 32,029 words. The seven books plus the Epitome sum to 241,987, plus the division title = 241,990. B1's total is right precisely because the Epitome is not added separately; the sentence invites a reader to add it and reach 496,826. The Epitome also carries no row of its own on `cic/corpus-map/latin-apologists.yaml`, which the document does not mention while presenting it as part of this candidate's sourcing.

**All other I.43 sourcing numbers re-derived independently and confirmed:** Minucius Felix 23,819; Commodian *Instructiones* 15,008; Arnobius 140,826; *Divine Institutes* 241,990; *Anger of God* 20,382; *Workmanship* 18,840; Fragments 3,932. **Total 464,797** — exact. (*De Mortibus Persecutorum*, 19,301 words, correctly excluded as IJC's.)

---

## Part D — I.43: further new defects

### M1. [MODERATE] §2 A2's heading undercounts its own body.

Heading: *"A2 — Pre-Nicene continuity: clears for all four core figures, with **three** honest complications disclosed."* The body discloses **four** — Minucius Felix (Christological absence), Lactantius (pneumatology and eschatology), Commodian (date), Arnobius (anthropology) — and the subsection's own Resolution sentence enumerates all four by name, as does the Section A conclusion and as does §4 (items 1, 2, 3, 5). The prior draft's heading said "two"; the revision raised it by one when it added Lactantius and did not count Minucius Felix, whose complication it also upgraded in the same pass. Same shape as I.35's N6.

### M2. [MODERATE] The Tier grading no longer matches the document's own comparison of the two candidates.

The Tier conclusion states, of the Tertullian question: *"distinct in kind from I.35's Justin/Tatian figure-sharing questions but **not lesser in the work Doc_01 must do before drafting**."* On that reasoning the two documents should grade alike. They do not:

| | I.35 | I.43 |
|---|---|---|
| B3 verdict | *"does not pass unconditionally"* / *"does not cleanly clear B3"* | **"B3 passes"** |
| Tier | **Provisional** Tier 1, *"conditional on two rulings"* | **Tier 1 — Strong seed**, unconditional |
| Binding pre-Doc_01 items | 2 (Justin, Tatian) | 2 (Tertullian §4.4; both authors' dating §4.1, *"binding on Doc_01, before drafting proceeds"*) |

I.43 carries two binding pre-drafting items of its own and grades itself unconditionally. Either the Tertullian/dating items are lesser (in which case the Tier sentence's own claim is wrong) or they are not (in which case "B3 passes" and the unqualified Tier are). This is the leftover framing the revision was meant to remove when the Lactantius/IJC item stopped being an open risk: the grade was carried over from a draft that had one soft adjacency, and two binding items were added underneath it.

### M3. [LOW] Commodian is cleared under A2 while the same paragraph says he may not belong to the candidate at all.

*"A2 is satisfied for all four core figures"* and *"none, on the evidence available, disqualifying"* sit alongside *"Doc_01 needs an actual, cited dating judgment before Commodian can be treated as belonging to this candidate at all."* Carried unrevised from the prior draft, but the revision's own upgrade of the heading to *"clears for all four core figures"* sharpens the tension rather than resolving it. A scope question is not a floor question and the document could say so in one clause.

### M4. [LOW] §4 item 7's "materially complete" sweep, like I.35's, reports Round 1's Part C work without crediting it.

*"I.35, I.33, and the remaining Era 1 entries checked with no further material bearing found."* The I.33 finding, the I.24 adjacency and the twelve immaterial Era 1 entries are Round 1's Part C results. The document does not cite the review as the instrument that discharged them.

---

## What checked out clean (verified directly this round, not carried from Round 1)

Recorded so the next revision does not disturb settled ground:

- **Article 23's text**, including the "Governing external opponents" paragraph and its distinction from Article 20 — exact, and correctly applied to the Trypho material.
- **Article 4's five commitments** — verified in `CiC_L1_Constitution_V2_2.docx`; the Spirit is genuinely the fifth, so I.43's B3 framing is right.
- **A5's rule text**, both sentences, in the Methodology docx.
- **Section B's "never a per-world process"** sentence, verbatim.
- **Both process documents** (`CiC_Step0_Era10_V1_0.md` structure; `CiC_World_Atlas_PreStep0_Survey_V0_1.md` scope language) — the revised §0/§5 accounts are accurate.
- **All PAHC Justin quotations** in I.35 §3 B3 — five records, all verbatim.
- **The Athanasius bounding rule** and **Mark's `per work` ruling** — both verbatim (the inference drawn from them is the problem, not the quotations).
- **The Syriac Tatian source record's Assyrian-claim sentence** — verbatim.
- **`tertullian-s-voice.yaml` at 33 rows**, including the four apologetic works named.
- **LPC `Source_Registry.md` row 29** — Excluded / Named Comparandum, and the two clauses quoted are exact.
- **`records/lpc/` does not exist**; LPC's Step 0 is five-round-reviewed (`Step0_Round1`–`Round5_Review.md`). I.43's corrected characterisation of LPC's state is right.
- **LPC's corpus map holds no Arnobius, Lactantius, Minucius Felix or Commodian work.**
- **IJC's nine citing records** and the load-bearing weight on `ijc.source.lactantius-de-mortibus`.
- **Every I.43 word count**, re-derived independently, including the 464,797 total.
- **Melito at `anf08` div2 x.v**, 11,288 words.
- **`records/alx/` holds no figure or source record for any I.35 or I.43 name** (the conclusion; not the reason the document gives for it — see N4).
- **Montanism carries no adjacency to either candidate**, and the Tatian/Encratism–Montanism historiographical point is correctly stated.
- **Jerome, *Ep.* 84.7** and **Jerome, *De vir. ill.* 79** — both real, both accurately used.
- **Both documents' status discipline** — "DRAFT, Revision 1. Not yet independently re-reviewed. Not self-disposed. Not Approved to proceed," no build thread opened — remains exactly right, and both §6 sections correctly route the next step through an independent round rather than self-disposing.

---

## Verdicts

### I.35 — The Second-Century Greek Apologists: **SUBSTANTIAL REVISION REQUIRED**

Eleven of the fourteen Round 1 findings are answered in substance, and four (A7, A12, A13, and A4's withdrawal) are cleanly and verifiably resolved. The Justin bullet is now built on PAHC's own records, quoted accurately, and the three-option framing is a real improvement on two.

What drives the verdict is not the Round 1 backlog. It is that the revision introduced **two HIGH defects of its own**:

**N1** — no work on this candidate's own corpus map is assigned to it alone (15 of 16 co-assigned to a built, live world), which is the governing fact for B3 and for the phrase "confirmed-unique roster," and which neither round has stated.

**N2** — the newly-asserted rule *"native to one world… not co-ownership"* is refuted by the precedent cited two sentences later: Antony is a `narratable`, `emic` figure record in **both** Alexandria and Desert, with the attribution expressly "held open." The rule forecloses the one cross-build mechanism the project has actually built at figure level, and mislabels the option the document does offer.

Underneath those: a fabricated work-attribution reaching a binding §4 item (**N3**), a supporting check that is false and was imported from Round 1 as "verified directly" (**N4**), a fallback roster missing three of the census's own seven voices (**N5**), a heading contradicting its own subsection (**N6**), the Article 4 floor listed as five and enumerated as four in the very header Round 1 flagged — the identical defect LPC's own Round 1 review graded HIGH (**A10**), the "as applicable" precedent misattributed for a second consecutive round (**A9**), and the A5 rule corrected by half-quotation (**A6**).

The pattern this project's review history predicts held. Every one of the four HIGH findings was addressed, and three of the four addresses (A2's replacement residue, A3's replacement rule, A4's replacement arithmetic) introduced a fresh error while correcting the old one.

### I.43 — The Latin Apologists: **SUBSTANTIAL REVISION REQUIRED** *(narrowly — the required work is confined to the new material)*

All four Round 1 HIGH findings are genuinely discharged, and independently confirmed as such: Tertullian is engaged rather than omitted; Minucius Felix's Christological content is stated as absent rather than thin and Doc_02 is no longer told to foreclose the question; Lactantius carries a real, accurately sourced pneumatological disclosure; the Lactantius/IJC ruling is cited by name and correctly reclassified. B5, B6 and B7 are clean. The sourcing arithmetic is the most thoroughly verifiable thing in either document and every figure holds.

The verdict is not COSMETIC ONLY because the new material contains a factual error that partly inverts the argument it serves and three internal contradictions in the document's own conclusions:

- **B1(i)** — Tertullian placed in *"the same city… as Minucius Felix."* He is in Carthage; Minucius Felix is in Rome and Ostia. The sentence is the load-bearing one in the paragraph answering Round 1's largest finding, and it erases the Carthage exclusion that Round 1 separately observed and that B5 still does not state.
- **B1(ii)** — *"names Tertullian first among its `voices`"* (twice), against the document's own new §1, which lists him fifth and correctly.
- **B4** — §3 B3's conclusion says the prior draft *"wrongly treated as settled"* the very item its own bullet, §4 item 6, the Tier conclusion and §6 all say the prior draft treated as **open**.
- **M2** — the Tier grading contradicts the document's own statement that its open items are "not lesser" than I.35's, grading "B3 passes" and unqualified Tier 1 where the sibling grades "does not cleanly clear B3" and Provisional Tier 1, on two binding pre-drafting items apiece.

Plus **B1(iii)**'s selective quotation of LPC row 29 (the third reason, which is the one that transfers *to* this candidate, is dropped), **M1**'s heading undercount, **B2**'s off-by-one measurement now written into a binding Doc_02 instruction, and **B9**'s Epitome nesting.

### Round 3 status

Not run. Neither document should open a build thread. Both should be revised against the findings above and re-reviewed, per `cic-build-cycle`'s review-gated discipline and both documents' own §6.

Two process notes for whoever runs the next revision:

1. **Round 1's Part C sweep is an instrument, not a fact source.** Two of its findings were wrong (the Alexandria/Clement diagnosis at C7, re-derived above at **N4**; the "eleven days" arithmetic at B4). One of the two was copied into the revision and re-badged as an independent check. A revision that answers a review by restating the review's own findings inherits the review's own errors — which is the specific mechanism behind this project's repeat-failure pattern, and the reason the next round should re-derive from the repository rather than from either artifact.
2. **The recurring physical defect in both documents is heading/summary drift.** Four of the new findings (N6, M1, M2, and the B4 inversion) are the same failure: a body paragraph was revised, and the heading, count or conclusion sentence above or below it was not. Before the next round, both documents would benefit from a pass that reads only the headings, the resolution lines, the section conclusions and §4's numbered items against each other, with the body closed.
