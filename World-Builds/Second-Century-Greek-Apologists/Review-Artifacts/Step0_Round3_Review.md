# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 3 Independent Adversarial Review

**Reviewed documents (Revision 2, commit `fb054eef`):**
- `World-Builds/Second-Century-Greek-Apologists/Step0_Movement_Scope_Confirmation.md` (Atlas I.35)
- `World-Builds/Latin-Apologists/Step0_Movement_Scope_Confirmation.md` (Atlas I.43)

**Prior rounds:** `Review-Artifacts/Step0_Round1_Review.md` (commit `09d94033`) and `Step0_Round2_Review.md` (commit `17f981b7`), each duplicated under both worlds. Round 1: SUBSTANTIAL REVISION REQUIRED for both (I.35 A1–A14, four HIGH; I.43 B1–B9, four HIGH; plus a commissioned Era 1 sweep, Part C). Round 2: SUBSTANTIAL REVISION REQUIRED for both (I.35 N1–N7 plus seven partially-fixed Round 1 residuals; I.43 B1(i)–(iv), B2, B3-LOW, B4-MODERATE, B8, B9, M1–M4).

**Reviewer:** independent isolated agent. No involvement in either draft, in Revision 1, in Revision 2, or in Rounds 1–2.

**Overall verdicts:**
- **I.35 (Second-Century Greek Apologists): SUBSTANTIAL REVISION REQUIRED** — one new HIGH finding, introduced by this revision's own rewrite of the paragraph Round 1 and Round 2 both flagged, plus one Round 2 finding left unfixed and reported as fixed.
- **I.43 (Latin Apologists): SUBSTANTIAL REVISION REQUIRED** *(narrowly — no HIGH finding; every one of Round 2's twelve findings is genuinely discharged, and the remaining work is two false statements introduced by the revision's own fixes, each a one-clause correction, plus three LOW items).*

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**A note on method.** Nothing was accepted from either document's §6 revision history, and nothing was accepted from Round 1 or Round 2 as a premise. Every finding below was re-derived directly from the repository: `cic/corpus-map/*.yaml` parsed and cross-joined with `yaml`; `records/<world>/` read and grepped file-by-file across all seven built worlds; `cic-website/data/world-census.json` parsed and field-tested; `CiC_L1_Constitution_V2_2.docx` (internal version 2.3), `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx` and `CiC_Step0_Conclusion_FINAL_v2.docx` extracted from their `.docx` and read; the vendored XML in `cic/texts/` parsed and word-/token-counted with `lxml` independently of both prior rounds' tables and of the documents' own numbers. Every passage either document presents as a quotation was matched against its source. **Round 2's own findings were re-tested as claims, not adopted** — all of them held, and one of them (its N4 diagnosis) was refined; the material new finding below is one that neither prior round reached.

**Working-tree note.** Both documents and all four prior artifacts were read at `fb054eef` on branch `_round3review/apologists`, fetched from `candidate-worlds-step0-apologists`. No document content was altered; this artifact is the only file written.

---

## Part A — I.35, The Second-Century Greek Apologists: Round 2 findings re-tested

Each entry states what Revision 2 claims, what the repository actually shows, and whether the result is **(a) genuinely resolved**, **(b) addressed in form but wrong or incomplete in a new way**, or **(c) unfixed**.

### N1 [was HIGH] — no work on I.35's corpus map is assigned to it alone. **(a) Genuinely resolved, and independently confirmed.**

Cross-joined directly across all census-id corpus maps:

| Works on `greek-apologists-second-century.yaml` | **16** |
|---|---|
| Also on `post-apostolic-house-church.yaml` | **15** (all but the Ambrose *hypomnemata*) |
| Also on `syriac-edessa-nisibis.yaml` | **2** (Ambrose *hypomnemata*; Tatian's *Address*, which is on all three) |
| Union of the two | **16** |
| Assigned to `greek-apologists-second-century` alone | **0** |

§3 B3's new opening paragraph states every one of these numbers correctly, and — this is the part that matters — states explicitly that the fact belongs to the corpus-assignment bucket and is a different test from what a built world's own records claim. That distinction is exactly right, and the document's insistence on it is good discipline. **The document then gets the second test wrong; see R1 below.**

### N2 [was HIGH] — the "not co-ownership" project pattern. **(a) Genuinely resolved.**

Verified directly: `records/alx/figure/alx.figure.antony.md` and `records/desert/figure/desert.figure.antony.md` both exist; both are `register: emic`; both are `narratable: true`; the Alexandrian record's body reads *"CROSS-BUILD FLAG at full strength: Antony belongs at least as much to the Desert world (the planned second build) as to Alexandria, and the attribution is held open."* The revision's bracketed substitution (*"[Desert Monasticism]"*) and elision are marked and do not alter the sense. The refuted rule is withdrawn, the co-ownership precedent is stated correctly, and the fourth Justin option that follows from it is now before Mark. This is the strongest fix in either document.

*Two things the paragraph does not say, offered as notes rather than findings:* the Alexandrian Antony record is `evidentiary_weight: illustrative` against Desert's `load-bearing`, and its body bounds Antony's Alexandrian appearance to *"Athanasius's portrait — the formation ideal the Alexandrian bishop held up — not as the desert's own self-understanding."* Co-ownership, on the project's one built instance of it, is asymmetric by design. If option (d) is chosen for Justin, that asymmetry is the shape it would take.

**One small overreach inside the fix — see R9.**

### N3 [was MODERATE] — the fabricated "Ambrose *hypomnemata* on Quadratus." **(a) Genuinely resolved.**

`cic/corpus-map/greek-apologists-second-century.yaml`, row `ambrose-hypomnemata`, `locus: div2 9.18`, `confidence: provisional`: the note is entirely about the Syriac transmission of a Greek apology paired with the pseudo-Justin *Discourse to the Greeks*, and ends *"`provisional` because the APOLOGIST half is a date question - the entry's window is 124-200 and this piece is undated."* There is no Quadratus content of any kind. §2 A5, §3 B1 and §4 item 4 now all say so plainly. Fix confirmed at all three sites.

### N4 [was MODERATE] — the fabricated Clement-citation detail. **(a) Resolved; the withdrawal's own field-name is slightly off.**

Re-run directly: every occurrence of "tatian", "athenagoras" or "theophilus" in `records/alx/` is the vendored filename string `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, across seven files; the only other "Theophilus" is Theophilus of Alexandria (bp. 385–412) in `alx.source.alexandrian-canonical-answers.md`. There are no Clement citations of the three anywhere in Alexandria's records. The revision withdraws the fabricated detail explicitly and re-confirms the clean-overlap conclusion. Correct.

**[LOW]** The withdrawal says the hits were filename strings *"in unrelated records' own `edition:` metadata fields."* Four are in `edition:` fields; three are in `locus:` fields (`alx.quote.to-believe-or-disbelieve`, `alx.quote.couches-and-trenchers-and-bowls`, `alx.quote.the-grades-here-in-the-church`). Round 2 said "an `edition:` field — six files"; the revision inherited the field name and dropped the count. Immaterial to the conclusion, recorded so it is not restated a fourth time.

### N5 [was MODERATE] — the fallback roster dropping three census voices. **(a) Resolved in form.** The Tier sentence now enumerates Athenagoras, Theophilus, Aristides, Quadratus, Melito and the *Epistle to Diognetus*, and all six are `confidence: assigned` on the map — verified row by row. **The claim made *about* that roster is false; see R1.**

### N6 [was MODERATE] — §2 A2's heading contradicting its body. **(a) Genuinely resolved.**

Heading now reads *"clears, with one figure requiring honest disclosure rather than exclusion"*; the body clears Justin, Athenagoras, Theophilus and Aristides and discloses Tatian alone; the Resolution line is singular. The added "note on counting" paragraph separates the A2 continuity question from B3's figure-sharing questions correctly and usefully. Clean fix, and the right kind of fix — it explains the distinction rather than only adjusting a number.

### N7 [was LOW] — §4 item 7's sweep status. **(b) PAHC now named; the crediting introduced with it is wrong — see R4.**

### A5 residual [was MODERATE] — the pseudonymous-Justin note and Aristo's assignment count. **(a) Genuinely resolved.**

Verified verbatim: the *Hortatory Address to the Greeks* and *On the Sole Government of God* each carry *"Same position as the Discourse: transmitted under Justin, widely doubted"*; *The Discourse to the Greeks* carries *"Printed under the JUSTIN MARTYR div1; authenticity has long been questioned. Filed with its transmitted author per §6.2 - derive, don't assert - with the doubt recorded."* §2 A5 now attributes each note to the right work. Aristo of Pella is confirmed on three maps — `greek-apologists-second-century`, `post-apostolic-house-church`, `ebionite-nazoraean-current` — and the quoted admission (*"The Jewish-Christian current and pahc are both defensible; neither is demonstrated by the fragments"*) is exact.

### A6 residual [was MODERATE] — A5's rule quoted by half. **(a) Genuinely resolved.**

Both sentences are now quoted, and both match the Methodology character-for-character. The interpretation the document then places on the second sentence is argued openly, tied to IJC's own worked example, and does not depend on suppressing the clause. That is the right way to hold a contested reading.

### A8 residual [was MODERATE] — the Tatian dating double standard, and the Encratite-charge characterization. **(b) Second half fixed but misattributed (R2); first half relabelled rather than fixed (R6).**

### A9 residual [was MODERATE] — the A1/A2 routing precedent. **(a) Genuinely resolved.**

Read directly: LPC's Step 0 §2 does run *"A1 for Augustine, A2 for Cyprian"*, and its *"nothing else"* line bounds what Step 0 tests at all, not which of A1/A2 applies. IJC's §2 resolution is *"both A1 and A2 apply, to different phases of the same continuous movement… not a forced either/or."* Revision 2 withdraws the LPC misattribution, states honestly that no cleared confirmation supplies a precedent for a wholly pre-Nicene, non-straddling window, and rests A2 on the Procedure's plain text (*"Test each candidate against A1 (and A2 or A3 as applicable)"* — verified verbatim). Two rounds of misattributed warrant end here. Both documents make the same correction and both are right.

### A10 residual [was MODERATE] — Article 4's floor listed as five and enumerated as four. **(b) The count is fixed; a new and false verbatim claim is put in its place — see R5.**

### A11 residual [was MODERATE] — Section A's clearances undisclaimed. **(a) Genuinely resolved.**

§2 now opens with a framing note extending the "considered signal, not a disposition" caveat to every Section A clearance, and says so in terms that match §3's and §5's. The asymmetry Round 2 identified is gone in both documents.

### A14 residual [was LOW] — the Melito Paschal-homily caveat and Aristides' file. **(a) Genuinely resolved.**

The census `voices` entry reads *"Melito of Sardis - bishop, apologist to Marcus Aurelius, and author of a Paschal homily recovered in the twentieth century"* — quoted exactly, with B1's "strong pass" correctly scoped not to cover the unvendored *Peri Pascha*. Aristides is confirmed at `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` (`locus: div2 13.3-13.4`); Melito's fragment is the `anf08` item (`div2 10.5`, the roman `x.v` of prior rounds). Both corrected.

### A4 residual arithmetic [raised at Round 2 under A4] — **(c) UNFIXED, and unreported. See R3.**

### A1 residual, third problem [raised at Round 2 under A1] — **(c) UNFIXED, and unreported. See R7.**

---

## Part B — I.35: findings against Revision 2

### R1. [HIGH] "PAHC's own written records claim only Justin's voice specifically" is false — PAHC holds a load-bearing, `emic` source record naming Quadratus, Aristo of Pella and Melito of Sardis as its authors, an `emic` verbatim Melito quote feeding one of its own gravities, and a doctrinal-witness citation of Theophilus' *To Autolycus* by locus. The Tier's fallback roster is built on the false half of the claim — and the document cites the contradicting record itself, two sections earlier.

§3 B3, immediately after the corpus-map governing fact and its careful warning that the two tests must not be conflated:

> *"Direct inspection of `records/pahc/figure/` finds no figure record at all for Athenagoras, Theophilus, Aristides, Melito, or the *Diognetus* author — **PAHC's own written records claim only Justin's voice specifically**, verified file-by-file immediately below, not the other co-assigned works."*

The first clause is true: `records/pahc/figure/` holds eleven files and none is for those names. The second clause is not, and it is the clause the document reasons from.

`records/pahc/source/pahc.source.second-third-century-remains.md` — `record_type: source`, `register: emic`, `evidentiary_weight: load-bearing`, `verification_state: verified-direct` — carries this `author` field:

> *"Quadratus of Athens, Aristo of Pella, Melito of Sardis, Hegesippus, Dionysius of Corinth, Rhodon, Claudius Apollinaris of Hierapolis, Polycrates of Ephesus, Serapion of Antioch, Apollonius - the surviving voices of the sub-apostolic churches"*

and its body records per-author verification against the vendored file: *"Section loci verified directly: Quadratus 70010, Aristo 70047, Melito 70117…"*

Beyond that source record:
- **`records/pahc/quote/pahc.quote.melito-no-phantom.md`** is an `emic`, `license: verbatim`, `citation_specificity: A`, `verification_state: verified-direct` quote record of *Melito of Sardis, Fragment VII, "On the Nature of Christ"* — Melito's own words, opened 2026-09-09 and carried at `formation_confidence: Contested` with a full transmission caveat.
- **`records/pahc/gravity/pahc.gravity.boundary-drawing.md`** lists `pahc.source.second-third-century-remains` among its own `sources`, at the Melito Fragment VII locus, and discusses Melito by name in its description as *"a flagged candidate second voice."*
- **`records/pahc/doctrinal_witness/pahc.witness.jesus-as-god.md`** cites *"Theophilus of Antioch, To Autolycus II.15, c. 180 CE"* by locus, twice, as material *"inside this build's own vendored corpus… inside this world's own window and inside Antioch/Syria, one of its three core regions."*

Three consequences, all load-bearing for this document:

1. **The Tier's fallback roster is wrong.** *"If both rulings go against sharing… the remaining roster — none of it structurally exclusive to this candidate per B3's governing fact above, but **none of it currently claimed by any built world's own figure or source records either** — is Athenagoras, Theophilus, Aristides, Quadratus, Melito, and the *Epistle to Diognetus*."* Quadratus and Melito are named authors of a built world's own load-bearing source record; Melito additionally has an `emic` quote record and a place in a PAHC gravity. Only Athenagoras, Aristides and the *Diognetus* writer survive the test as stated. The paragraph then reasons from that roster to *"a real but visibly thinner candidate, plausibly still a defensible Tier 1 on B1/B2 alone"* — a conclusion drawn from a roster two of whose six members are already opened by the neighbour.

2. **§4 item 7's binding carry-forward is wrong on the same point.** *"PAHC is explicitly not clean… verified file-by-file in §3 B3 to hold load-bearing, `emic` claims on Justin's own voice, **and no figure or source record on any of this candidate's other roster names**."* `pahc.source.second-third-century-remains.md` is a source record on three of them.

3. **The document contradicts itself.** §2 A5, in the paragraph withdrawing Round 1's phantom bundling, says: *"PAHC's own source record already runs a careful per-author disposition of that fragment collection."* That is the same record. The document read it, described it accurately in §2, and then in §3 wrote a general claim its own §2 refutes.

This is the third consecutive round in which B3's central premise — how much of this candidate's roster PAHC has actually opened — has been found contradicted by PAHC's own records. Round 1's A2 caught it for Justin's argument, address to power and the *Dialogue*. Round 2's N1 caught it at corpus-map level. It is now caught for the non-Justin voices, in the paragraph written to separate those two tests. The Justin material in §3 B3 is, for the record, verified accurate this round — all five PAHC quotations are verbatim (see "What checked out clean"). The defect is entirely in the generalization laid over them.

**What a fix requires:** a direct read of `records/pahc/source/`, `quote/`, `gravity/` and `doctrinal_witness/` for every one of the seven census voices, not `records/pahc/figure/` alone; a corrected statement of what PAHC has opened for Quadratus, Aristo, Melito and Theophilus; and a fallback-roster sentence, and a §4 item 7, rewritten to match. Whether it changes the Tier is a judgment for the revision, not this review — but B3's "not yet claimed by any built world's own records" framing cannot survive in its current form.

### R2. [MODERATE] §2 A2 attributes the Syriac record's Encratite charge to Irenaeus. The record attributes it to Eusebius — and the same sentence says so in its second half.

The correction of Round 2's finding reads:

> *"the section does not state plainly that the charge is real — it deliberately stops short of asserting the charge's truth, **naming it as Irenaeus's report** and declining to adjudicate it, while noting the *Address* itself is not a confession of it and that the work predates the events **Eusebius** describes."*

`records/syr/source/syr.source.tatian-address-to-greeks.md`, "THE ENCRATITE CHARGE, HANDLED HONESTLY," in full:

> *"Eusebius accuses him of it and this world's figure record carries the charge. The Address is not a confession of it and must not be read as one: it is an apology addressed to Greeks, written before the events Eusebius describes, and its asceticism is of a piece with the whole second-century apologetic register. What the Address supplies is the material for a reader to weigh the charge rather than only receive it."*

Irenaeus appears nowhere in the section. The charge is Eusebius' (`syr.figure.tatian.md` cites *HE* IV.29 for it). Irenaeus is this document's own source, two sentences earlier, for a different proposition — that Tatian led the Encratite current and that Irenaeus derives it from Saturninus and Marcion (*AH* I.28, verified as correctly used at Round 1). The revision has carried its own citation across into a description of somebody else's record, in the one sentence whose entire purpose is to state that record's content accurately, and about the record it names as the model for a binding Doc_02 disclosure (§4 item 3). The second half of the same sentence gets the attribution right, so the sentence disagrees with itself.

Same defect class as N3 and N4 — a citation detail invented while correcting a citation detail — one round later.

### R3. [MODERATE] §3 B1 still says the corpus map holds five works "beyond the sixteen-work core." Those five *are* five of the sixteen. Round 2 raised this; Revision 2 did not fix it and §6 does not mention it.

> *"**Completing the roster (Round 1 finding A5).** Beyond the sixteen-work core, the corpus map also carries: three works transmitted under Justin's name at `confidence: provisional`…; Aristo of Pella's fragments…; and the Ambrose *hypomnemata addressed to the Greeks*."*

`greek-apologists-second-century.yaml` holds sixteen work rows in total. Enumerated: Ambrose *hypomnemata*, Aristides, Aristo of Pella, Athenagoras ×2, *Dialogue with Trypho*, *Hortatory Address*, *On the Sole Government of God*, *Discourse to the Greeks*, *First Apology*, *Second Apology*, *Epistle to Diognetus*, Melito, Quadratus, Tatian's *Address*, Theophilus. The three pseudonymous Justin works, Aristo and the Ambrose piece are items 7–9, 3 and 1 of that list. The sentence, read as written, gives the map twenty-one works.

This directly contradicts §3 B3's own new governing paragraph two subsections later (*"this candidate's own 16-work corpus map"*, *"15 of 16"*, *"2 of 16"*, *"the union of the two is all 16"*). Round 2 recorded it under A4 as a "New arithmetic error"; §6's account of Round 2's findings omits it entirely and the revision asserts it "addresses all of Round 2's findings directly."

### R4. [MODERATE] §3 B3 and §4 item 7 credit Round 1's Part C, "The full Era 1 sweep," for a clean result on four **Era 2** built worlds Part C did not cover — replacing the prior draft's own honest, hedged self-check with a false attribution and an upgraded certainty.

> §3 B3: *"Desert, Hieronymian, Imperial-Juridical, and Cappadocian checked directly, no figure or source overlap found — this clean result was first established by the independent Round 1 review's own **Part C, 'The full Era 1 sweep,'** which this document credits here rather than presenting as its own first check."*
> §4 item 7: *"Desert, Hieronymian, Imperial-Juridical, Cappadocian, and Alexandria are now confirmed clean directly against their own records — crediting the independent Round 1 review's own Part C… as the source of this finding."*

Part C's own opening: *"Twenty-one entries carry `era == 1` in `cic-website/data/world-census.json`."* Verified: exactly 21 entries carry `era: 1`. Verified from the census: Desert Monasticism is **I.3, era 2**; Cappadocian Christianity **I.5, era 2**; Imperial and Juridical Christianity **I.6, era 2**; Hieronymian Ascetic-Literary **I.9, era 2**. None of the four is in Part C's scope, and none appears anywhere in C1–C8 or in Round 1's "what checked out clean" section. (Alexandria, I.2, and Syriac, I.7, *are* era 1 and *were* covered — the credit is accurate for those two only.)

Two aggravating details:

- The **original draft** (`98ec3d32`) said of these worlds *"no figure or source overlap found in this pass… a full cross-check against all eight built worlds' own figure/source rosters should be completed at Doc_01, not assumed complete from this document alone."* That was a modest, honest self-report. Revision 2 replaced it with a credit to an instrument that never ran the check, and simultaneously upgraded §4 item 7 to *"This sweep is now materially complete."*
- §4 item 7 also credits Part C for Alexandria "as the source of this finding" — while §3 B3, four paragraphs earlier, withdraws Part C's stated Alexandria reasoning as fabricated and says the conclusion is *"independently re-confirmed here."* The two sections credit opposite instruments for the same result.

*The underlying result is true.* I re-derived it: `records/desert/`, `records/hal/`, `records/cappadocian/` and `records/ijc/` contain no figure or source record for any I.35 roster name (the only near-hits are `ijc.figure.justina.md` — the empress, not Justin — and `desert.search.unopened-volume-sweep.md`, a search record that explicitly *declines* `anf02` and names Theophilus of Antioch as a homonym false positive). The finding is against the provenance claim, not the conclusion — which is precisely the species of defect Round 2's own closing process note warned the next revision about.

### R5. [MODERATE] The header now claims to quote Article 4's five commitments "in full." Four of the five are abridged paraphrase, one carries a gloss that is not in the Constitution, and the fifth drops a word — the third consecutive round on this one sentence.

> *"this document *applies*, and where it must characterize, **quotes in full**, the floor's five commitments: (1) one God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen; (2) the Son, of one Being with the Father — full divinity and consubstantiality; (3) true humanity; (4) death, burial, resurrection, ascension, and return; (5) the Holy Spirit as Lord and giver of life, worshiped and glorified with the Father and Son."*

Article 4's actual list, extracted from `CiC_L1_Constitution_V2_2.docx` (internal version 2.3):

| # | Constitution | Document |
|---|---|---|
| 1 | *"One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen."* | verbatim ✓ |
| 2 | *"Jesus Christ as the only Son of God, eternally begotten of the Father, God from God, Light from Light, true God from true God, begotten not made, of one Being with the Father."* | abridged to fourteen words, plus *"full divinity and consubstantiality"* — a gloss not in Article 4 |
| 3 | *"Jesus Christ as truly human — incarnate of the Holy Spirit and the Virgin Mary, 'became truly human.'"* | *"true humanity"* |
| 4 | *"Christ's death under Pontius Pilate, burial, bodily resurrection on the third day, ascension, and his return in glory to judge the living and the dead."* | *"death, burial, resurrection, ascension, and return"* |
| 5 | *"The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son."* | drops *"together"* |

Round 2's finding (the floor labelled five, enumerated as four) is fixed — the count is now right. But the fix substituted a verbatim claim the text does not meet, and a paraphrase is exactly the *independent restatement* Article 4's own closing instruction — quoted correctly in the same sentence — forbids Step 0 from making. LPC's cleared answer to the identical problem, which this document cites as its model elsewhere, is to quote all five exactly and say so. Either quote them or say the document characterizes rather than quotes; the current sentence does the second while asserting the first.

### R6. [MODERATE] §2 A2's Tatian dating claim is relabelled as "cited scholarly judgment" and still cites nothing — and, unlike the sibling document's identical problem, is not carried to §4 as a binding item.

> *"The *Address* is dated by the same standard this document applies to Commodian in its sibling case — as a matter of **cited scholarly judgment**, not settled fact: it is widely, though not universally, read as predating or independent of that later turn."*

No citation is given. No §4 item requires one. The sibling document's treatment of Commodian, held up here as the standard being matched, does both: it names the dispute *and* makes a cited dating judgment binding on Doc_01 before Commodian may be treated as belonging to the candidate (§4 item 1, *"A cited scholarly judgment is required for both"*). The claim is load-bearing here — it is what allows the *Address* to clear A2 as a pre-divergence work while Tatian's later turn is bounded to a Doc_02 disclosure.

Round 2 flagged this as A8's unfixed second half. Revision 2 changed the label and left the substance; §6 reports it as *"hedged to the same cited-judgment standard as the sibling document's Commodian treatment,"* which is not what happened. (A usable warrant exists in the repository and goes uncited: `syr.source.tatian-address-to-greeks.md` states the *Address* was *"written before the events Eusebius describes"* — the document quotes that record for other purposes in the same subsection.)

### R7. [MODERATE] Round 2's third A1 problem is unaddressed and unmentioned: Tatian is not on this candidate's census `voices` list at all, yet he anchors B1, both of §4's Tatian items, and half the Tier conditional.

Verified from `cic-website/data/world-census.json`, I.35 `voices`: Quadratus, Aristides of Athens, Justin Martyr, Athenagoras of Athens, Theophilus of Antioch, Melito of Sardis, "The writer to Diognetus" — seven, no Tatian. Tatian appears in I.35's census record only inside the `sourcing` prose (*"Tatian's Address"*). §1 enumerates the seven correctly. §3 B1 then lists Tatian's *Address* among the works vendored whole; §4 items 2 and 3 are both Tatian rulings; the Tier conditional is *"conditional on two rulings"*, one of them Tatian's.

The asymmetry may be entirely benign — the corpus map is the assignment instrument and the census `voices` field is prose — but it is checkable in one read, it bears directly on whether a Tatian ruling is a roster question or a sourcing question, and neither round has drawn an answer out of the document. §6's *"This revision addresses all of Round 2's findings directly"* is false as to this item and as to R3.

### R8. [MODERATE] §6's revision history says "four" of Round 1's findings were partially fixed and then enumerates six, plus a seventh.

> *"It also found that **four** of Round 1's own findings had been only partially fixed (A5: …; A6: …; A8: …; A9: …; A10: …; A11: …) and A14 (…)."*

Six enumerated inside the parenthesis, A14 outside it. Round 2's actual count of partially-addressed Round 1 findings is higher still (it graded A1, A2, A3 and A4 the same way). This is the identical heading/count drift that produced N6 and M1 last round, now in the section whose job is to report what changed — and it appears in the very paragraph that names the repeat-failure pattern.

### R9. [LOW] "Four options… matching the four models the project has actually built" — the four options and the four models do not correspond.

§3 B3 names four mechanisms: outside voice (Augustine in HAL), opponent (Augustine in Donatism), co-ownership with attribution held open (Antony in Alexandria/Desert), and Mark's `per work` split (the Lactantius ruling). The four options are: (a) outside voice, (b) exclude from the roster, (c) `per work` split, (d) co-ownership. "Opponent" is a model with no option; "exclude" is an option with no model — and exclusion is not a cross-build mechanism at all. The option list itself is good and each option is now correctly labelled (Round 2's mislabelling is fixed); only the claim of one-to-one correspondence is wrong.

### R10. [LOW] "PAHC's own corpus map carries nine Justin works" counts a work that is not Justin's.

`post-apostolic-house-church.yaml` carries **eight** rows at `author: justin_martyr` (three `assigned`: *First Apology*, *Second Apology*, *Dialogue*; five `provisional`) plus *The Martyrdom of Justin Martyr* at `author: martyrdom_of_justin`, `confidence: provisional` — an anonymous *acta* of Justin's trial, filed under the same div1 heading, described in its own note as *"Anonymous acta of Justin and companions before the prefect Rusticus."* The document's "nine… the remaining six (including the pseudonymous works…)" arithmetic only closes if that *acta* is counted as a Justin work; it is not one, and it is not pseudonymous-Justin. The substantive point the sentence makes — that the *Second Apology* is `assigned` to PAHC and therefore is not open territory at corpus-map level — is correct and is the important part.

### R11. [LOW] §4 item 2 states only the strong half of the Tatian asymmetry §3 B3 establishes.

§3 B3 correctly and carefully establishes that Syriac's figure claim on Tatian is `evidentiary_weight: corroborating`, `narratable: false`, *"boundary-adjacent"*, held *"without adopting him as a founding teacher"* — all verified verbatim — and concludes the ruling is *"genuinely lighter than Justin's."* §4 item 2, the binding instruction Doc_01 will actually read, says only *"a built, live figure in Syriac Christianity with a load-bearing claim on the exact work this candidate names."* That is true of the *source* record (`load-bearing`, verified) and not of the figure record, and the qualification §3 was revised to add does not travel to §4.

---

## Part C — I.43, The Latin Apologists: Round 2 findings re-tested

**All twelve are genuinely discharged.** Each was re-derived independently.

### B1(i) [was MODERATE] — Tertullian's city. **(a) Resolved.** Census I.17 `region` is **"Carthage"**; census I.43 `region` is **"Rome and Ostia; Sicca in Numidia; Nicomedia and Trier"**. §2 A5 now states both, names Minucius Felix as a Roman advocate whose dialogue is set at Ostia, draws the boundary conclusion the error had erased, and connects it forward to B5 and to §4 item 4. B5 now carries the matching disclaimer (*"This roster does not include Carthage… and this scale claim should not be read as though it did"*). The silence Round 1 found and the false claim Round 2 found are both gone.

### B1(ii) [was MODERATE] — "names Tertullian first." **(a) Resolved.** The census `voices` array runs Minucius Felix, Arnobius of Sicca, Commodianus, Lactantius, Tertullian. §1 and §3 B3 now both say fifth and last, and §3 B3 says explicitly that it is being brought into line with §1.

### B1(iii) [was MODERATE] — LPC row 29's third reason. **(a) Resolved, and well.** `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Registry.md` row 29 reads *"Tertullian is not native to this world despite being its single most load-bearing named influence: he predates Cyprian's own episcopate by decades, wrote as a lay apologist rather than this world's own bishop-centered pastoral office, and — per Step 0's own attribution (Doc_01 §2, §6) — is credited with **forging** this world's own theological vocabulary, not with speaking as this world's own voice."* All three reasons are now quoted, classification confirmed **Excluded / Named Comparandum**, and the document states plainly that reason (3) cuts *for* this candidate's claim on Tertullian — verified against I.43's own census `legacy` field, *"The Latin vocabulary of Christian argument was largely made here, and in Tertullian's hands at the same time"* (verbatim). Arguing the half that damages your own conclusion is the discipline this pair has most often failed; it is done here.

### B1(iv) [was LOW] — the census's stated separation reason. **(a) Resolved.** I.43's `relationsSummary` reads *"It touches tertullian-s-voice, which begins the enterprise and is kept separate because a voice that distinct is its own entry"* — now quoted, distinguished from the `voices` field's bare bookkeeping line, and routed to Doc_01 to adopt or contest. Round 1's C2 asked the *draft* to adopt or contest; the document explicitly declines and defers. That is a disclosed deferral rather than a discharge, and it is stated as such, which is acceptable.

### B2 [was MODERATE + unaddressed half] — Minucius Felix's counts, and the clearance's warrant. **(a) Both resolved.**

Re-counted independently from `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, `div2 iv.iii`:

| token | count |
|---|---|
| `\bJesus\b` | 0 |
| `\bSon of God\b` | 0 |
| `(?i)\bincarnat` | 0 |
| `\bChrist\b` | **2** |
| `(?i)\bcrucifi` | **2** |
| words in division | **23,819** |

The two `Christ` hits are the ch. XXXVII *Argument* heading (*"Confession of Christ's Name"*) and the footnote *"Legat. pro Christ., ch. xxviii."*; the two `crucifi` hits are the ch. IX *Argument* heading (*"They Worship a Crucified Man"*) and the bracketed gloss at ch. XXIX (*"[A reverent allusion to the Crucified, believed in and worshipped as God.]"*). All four are ANF apparatus. Read directly, ch. XXIX does deny that *"an earthly being was able, to be believed God"* and moves immediately to the Egyptians choosing a man to worship and to flattered princes — exactly as described. §4 item 3 now states the count as bounded to what was counted and no longer hands Doc_02 a hard single-occurrence figure. Separately, the Section A conclusion now states what Minucius Felix's clearance actually rests on (*"an argument from silence plus external inference"*), which is the half Round 2 found unaddressed.

### B3-LOW [was LOW] — Jerome's locus for the pneumatology charge. **(a) Resolved.** *Ep.* 84.7 to Pammachius and Oceanus is correctly located and the charge accurately characterized; §2 A2 and §4 item 5 both now name the letters to Demetrianus as the target, state that they are lost and not among the vendored texts, and instruct Doc_02 to distinguish them from the vendored *Divine Institutes*.

### B4-MODERATE [was MODERATE] — §3 B3's self-inverting conclusion. **(a) Resolved.** It now reads *"one new binding item (Tertullian…) replaces what the prior draft wrongly treated as **open** (the IJC boundary, now resolved),"* consistent with the bullet above it, §4 item 6, the Tier conclusion and §6.

### B8 [was mixed] — structural findings shared with I.35. **(b) A1/A2 routing and A11 both cleanly resolved; the Article 4 header reference is now inaccurate in a new way — see R12.**

### B9 [was LOW] — the *Epitome*. **(a) Resolved, and independently confirmed.** Parsed directly: `div2 iii.ii` = **241,990** words; its eight `div3` children are Books I–VII plus `div3 iii.ii.viii`, *The Epitome of the Divine Institutes* (32,029), summing to 241,987, plus the division title = 241,990 — exactly as the revision now states. `latin-apologists.yaml` carries no *Epitome* row, also as stated.

**Every I.43 sourcing number re-derived from the XML this round and confirmed exactly:** Minucius Felix 23,819; Commodian *Instructiones* 15,008; Arnobius 140,826; *Divine Institutes* 241,990; *Anger of God* 20,382; *Workmanship of God* 18,840; Fragments 3,932. **Total 464,797.**

### M1 [was MODERATE] — §2 A2's heading undercount. **(a) Resolved, with the correction shown.** Heading now reads "four honest complications," matching body, Resolution, Section A conclusion and §4 items 1, 2, 3 and 5.

### M2 [was MODERATE] — the Tier grading inconsistency. **(a) Resolved.** §3 B3 now reads *"does not pass unconditionally, on the same footing as I.35's sibling case"* and the Tier is *"Provisional Tier 1 — Strong seed, conditional on Doc_01's own resolution of the Tertullian boundary and both authors' dating."* The document names the inconsistency, explains why it existed, and grades to its own reasoning rather than to the more comfortable framing. Both siblings now grade alike.

### M3 [was LOW] — Commodian cleared under A2 while possibly outside the window. **(a) Resolved.** *"This is a scope question, not a floor question, and this document does not conflate the two"* — and the Section A conclusion carries the same distinction. Verified against the corpus map, which is itself explicit: the *Instructiones* row is *"PROVISIONAL, NOT ASSIGNED, and the reason is the date rather than the shelf: proposals run from the 3rd century to the 5th."*

### M4 [was LOW] — §4 item 7's uncredited Part C work. **(b) Credited; the credit now over-reaches — see R13.**

---

## Part D — I.43: findings against Revision 2

### R12. [MODERATE] The header's cross-reference to I.35 is false in both halves: I.35's Revision 2 does not make the correction described, and does the opposite of what the sentence claims for the pair.

> *"this document *applies* the floor's five commitments **rather than claiming to reproduce Article 4's own text verbatim** — the same correction made in I.35's own Revision 2."*

I.35's Revision 2 header says it *"quotes in full"* the five commitments — i.e. it does claim to reproduce Article 4's text, and (per R5) does not actually do so. Two errors in one clause:

1. The described correction — applies rather than reproduces — was made in **Revision 1** of I.35, not Revision 2. Revision 2's correction to that header was the four-to-five count (Round 2's A10).
2. Whatever Revision 2 did, it was not this: the sibling now asserts full quotation, so a reader following the reference to see how the pair handles Article 4 finds the opposite discipline, applied to a paraphrase.

The practical effect is that I.43 has no accurate statement anywhere of how it treats the doctrinal floor's text, because the only such statement is a pointer to a sibling sentence that says something else. One-clause fix; but it is a verifiably false statement about the repository, in the document's governing-authority line, introduced by this revision.

### R13. [MODERATE] §4 item 7 credits Round 1's Part C for discharging the I.35 comparison, which Part C explicitly excluded from its scope and which §3 B3 says this document performed itself.

> §4 item 7: *"**I.35**, I.33, and the remaining Era 1 entries checked with no further material bearing found — crediting the independent Round 1 review's own Part C, 'The full Era 1 sweep,' as **the instrument that discharged those items**."*
> §3 B3: *"**Versus I.35** (The Second-Century Greek Apologists, unbuilt candidate): **direct check performed, not assumed.**"*

Part C's own summary bounds its scope: *"Of the **nineteen Era 1 entries not already checked by the drafts**…"* — 21 era-1 entries minus the two candidates themselves. Part C never ran the I.43-versus-I.35 comparison; it could not, since both are the objects of the review. The I.33 credit and the "remaining Era 1 entries" credit are both accurate (C3 and C7 exist and cover them); only I.35's inclusion in the list is wrong, and it contradicts the document's own §3 B3 in the process.

This is the M4 fix over-reaching by one item, and it is the same shape as I.35's R4: a crediting correction that credits the wrong instrument. It is the recurring physical defect Round 2's closing note named — a summary line revised out of step with the body it summarizes.

### R14. [LOW] §2 A5 places Tertullian's 33 works on the census entry rather than on the corpus map.

> *"he holds, on his own separate **census entry** (I.17, 'Tertullian's Voice'), 33 works including *Ad Nationes*, *To Scapula*, *The Soul's Testimony*, and *An Answer to the Jews*."*

Verified: `cic/corpus-map/tertullian-s-voice.yaml` holds exactly 33 work rows, including all four named (plus *Apology (Apologeticus)*). Census I.17 holds no works array; it carries `voices` and `sourcing` prose. §3 B3 attributes the 33 to the corpus map correctly; §2 A5 does not.

### R15. [LOW] The Tier paragraph recharacterizes §4 item 1 as an "ordinary theological disclosure," against the same paragraph's own listing of it as a binding item and against §2 A2's own new scope/floor distinction.

> *"Two binding pre-drafting items exist here just as in I.35's case (§4 items 1 and 4: both authors' dating, and the Tertullian/Article 21 boundary)… This candidate's open items are a real developmental-sequence question about its own roster's boundary (Tertullian) and **ordinary theological disclosures already common to every candidate in this pair**."*

Both authors' dating is not a theological disclosure and the document says so elsewhere: §2 A2's M3 fix states that whether Commodian belongs to the window at all is *"prior to"* the A2 test, *"a scope question, not a floor question."* Two sentences apart, the Tier paragraph counts it as binding and then files it under ordinary disclosures. The Tier itself is correctly conditional, so nothing downstream is wrong; the characterizing sentence is.

### R16. [LOW] B1 does not disclose that Commodian's *Instructiones* is the one `provisional` row on this candidate's own corpus map.

B1 lists the *Instructiones* among the vendored works with no flag. `latin-apologists.yaml` carries six rows at `confidence: assigned` and one at `provisional` — Commodian's — with the map's own reason stated: *"The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it."* The sibling document's B1 makes exactly this kind of disclosure for its own `provisional` rows, and the fact bears directly on §4 item 1's binding dating question. A one-clause addition; the substance is already argued at §2 A2.

*Cosmetic, not a finding:* B4's *"the same province and crisis from the opposite side"* sits awkwardly beside §2 A5's and B5's insistence that Sicca in Numidia is not Carthage and that this candidate's regions exclude it.

---

## What checked out clean (verified directly this round, not carried from Rounds 1–2)

Recorded so a fourth revision does not disturb settled ground:

- **The corpus-map governing fact for I.35** — 16 works, 15 co-assigned to PAHC, 2 to Syriac, union 16, zero exclusive. Cross-joined independently.
- **Aristo of Pella's triple assignment**, and the map's *"neither is demonstrated by the fragments"* admission — verbatim.
- **Tatian's *Address* at `confidence: assigned` in all three maps**, and the corpus-map note *"Tatian sits awkwardly across two entries… Mark may want a ruling on where his voice sits"* — verbatim.
- **The Antony figure and source pairs**, both worlds, register/narratable/weight fields as described.
- **All five PAHC Justin quotations in §3 B3** — `pahc.quote.moses-is-more-ancient` (`load-bearing`, 1 Apol. XLIV, divergence note verbatim); `pahc.quote.those-who-lived-reasonably-are-christians` (`load-bearing`, tier 1, *"which cites this exact chapter for 'the Logos present in every race of men'"* verbatim); `pahc.quote.the-memoirs-of-the-apostles-are-read`'s divergence note; `pahc.figure.justin`'s `bridge_line`, `narratable: true`, `emic`, `locus: whole work` on both works; `pahc.source.justin-dialogue`'s WEIGHT note and Ways-That-Never-Parted caution; `pahc.source.justin-first-apology`'s *"clearest inside evidence that the rival movements were live, contemporary, and undefeated."* All exact.
- **`syr.figure.tatian`** — `corroborating`, `narratable: false`, *"Boundary-adjacent"*, *"without adopting him as a founding teacher"*, `bridge_line` — all verbatim as used.
- **`syr.source.tatian-address-to-greeks`** — `load-bearing`, and the Assyrian-claim sentence verbatim.
- **Article 23's "Governing external opponents" paragraph and Article 20's scope clause** — both exact, both correctly applied to the Trypho material.
- **Article 4's five commitments** — verified; the Spirit is genuinely the fifth, so I.43's §2 A2 framing of Jerome's charge is right.
- **Methodology A5's two sentences, Section B's "never a per-world process," and the Procedure's "as applicable" instruction** — all verbatim in both documents.
- **LPC Step 0 §2** (*"A1 for Augustine, A2 for Cyprian"*; the "nothing else" line bounding what Step 0 tests) and **IJC §2** (*"both A1 and A2 apply… not a forced either/or"*; the Homoian exclusion sentence) — both now cited correctly in both documents.
- **LPC's state** — no `records/lpc/`; five Step 0 review rounds on file; Doc_01, Doc_02 and a full Source Registry present; `latin-pastoral-congregational-christianity.yaml` holds no Arnobius, Lactantius, Minucius Felix or Commodian work.
- **Mark's 2026-08-27 `per work` ruling** in `latin-apologists.yaml` — verbatim, including the Athanasius sentence.
- **`grep -rn "Divine Institutes" records/`** — zero hits across all seven built worlds. **`ijc.source.lactantius-de-mortibus`** — `load-bearing`, referenced by exactly nine other IJC records; ch. 48 / *"the world's most direct witness to its own legal beginning"* verbatim. All other IJC Lactantius material derives from *De Mortibus*, consistent with the ruled split.
- **`tertullian-s-voice.yaml` at 33 rows**; **LPC Source Registry row 29**, all three reasons.
- **Census fields**: I.35 `voices` (seven, no Tatian), `region`, `why`, the naming-note quotation with its marked elision; I.43 `voices` (five, Tertullian last), `region`, `legacy`, `relationsSummary`, `sourcing` (*"barely datable"*); I.17 Carthage; I.20 `Excluded - Doctrinal Floor (C1)` / *"Exclusion is not a judgment of unimportance"*; I.24 Contested — Evidentiary; I.33 c. 200–268, Rome.
- **Neither candidate appears in `CiC_Step0_Conclusion_FINAL_v2.docx`'s "The nine worlds"** — §0 is right in both documents. (Note for Doc_01: that document lists *Justin Martyr* among PAHC's own named sources at world #1, which is further weight behind §4 item 1.)
- **`CiC_Step0_Era10_V1_0.md`'s six-section era-wide structure** and **`CiC_World_Atlas_PreStep0_Survey_V0_1.md`'s** *"It renders no floor verdicts of its own"* and *"A signal, not a B1 score"* — both accurate; §0 and §5 of both documents are correctly scoped, and the System Hub question is fairly framed.
- **Both documents' status discipline** — "DRAFT, Revision 2. Not yet independently re-reviewed. Not self-disposed. Not Approved to proceed," no build thread opened, next step routed through an independent round rather than self-disposal — remains exactly right, and both §6 sections say so.

---

## Verdicts

### I.35 — The Second-Century Greek Apologists: **SUBSTANTIAL REVISION REQUIRED**

Revision 2 is a real improvement on Revision 1. Both of Round 2's HIGH findings are genuinely discharged and independently confirmed: the corpus-map governing fact is stated in full and correctly, and the refuted "not co-ownership" rule is replaced by the verified Antony precedent and a fourth option that follows honestly from it. N3, N4, N5 and N6 are fixed; A5, A6, A9, A11 and A14 are fixed; the A1/A2 routing paragraph, misattributed for two consecutive rounds, now says plainly that no precedent exists — which is the correct and harder answer.

What drives the verdict:

**R1 [HIGH]** — the claim that *"PAHC's own written records claim only Justin's voice specifically"* is false. `pahc.source.second-third-century-remains.md` is a `load-bearing`, `emic` source record whose author field names Quadratus of Athens, Aristo of Pella and Melito of Sardis, with per-author loci verified in its own body; `pahc.quote.melito-no-phantom.md` is an `emic` verbatim Melito quote feeding `pahc.gravity.boundary-drawing`; `pahc.witness.jesus-as-god.md` cites Theophilus' *To Autolycus* II.15 by locus. The Tier's fallback roster — offered as *"none of it currently claimed by any built world's own figure or source records"* — is wrong for two of its six members, and §4 item 7's binding status line is wrong on the same point. The document cites the contradicting record itself at §2 A5. This is the third consecutive round in which B3's central premise about PAHC has been found contradicted by PAHC's own records, and it now sits inside the very paragraph written to keep the corpus-map test and the records test apart.

Underneath it: a Round 2 finding left unfixed and reported as fixed (**R3**, the corpus map given twenty-one works in B1 and sixteen in B3); a second Round 2 finding neither fixed nor mentioned (**R7**, Tatian's absence from the census `voices` list while he carries half the Tier conditional); the Encratite charge attributed to Irenaeus where the record says Eusebius, in the sentence correcting last round's misreading of that same record (**R2**); a "full Era 1 sweep" credited for four Era 2 worlds it never covered, replacing the original draft's own honest hedge (**R4**); Article 4's commitments asserted as quoted in full and delivered as paraphrase, third round running on the same header (**R5**); the Tatian dating relabelled rather than cited (**R6**); and a "four" enumerating six in the revision history itself (**R8**).

The pattern this project's review history predicts held for a third time. Both HIGH findings were addressed; the paragraph doing the addressing introduced a new HIGH of its own.

### I.43 — The Latin Apologists: **SUBSTANTIAL REVISION REQUIRED** *(narrowly)*

**Every one of Round 2's twelve findings against this document is genuinely discharged, and each was independently re-derived rather than accepted.** Tertullian is in Carthage and the Carthage exclusion is now stated three times, including in B5's scale claim; he is fifth in the `voices` array in both places that mention it; LPC row 29's third reason is quoted and argued *against* the document's own conclusion; the census's separation reason is engaged; the Minucius Felix counts are exactly right (2 and 2, all apparatus) and §4 item 3 is bounded to what was counted; the Section A conclusion states what that clearance actually rests on; Jerome's Demetrianus locus is restored with the lost-letters distinction; §3 B3's inversion is corrected; the *Epitome* nesting is explained with arithmetic that checks to the word; the A2 heading counts four; the Commodian scope/floor distinction is drawn; and the Tier now grades conditionally, matching both its sibling and its own stated reasoning. The sourcing arithmetic — 464,797 words — reproduces exactly. This is a document that answered its review.

The verdict is not COSMETIC ONLY because two of the revision's own fixes introduced verifiably false statements:

- **R12** — the header tells the reader that I.43 applies rather than reproduces Article 4's text, *"the same correction made in I.35's own Revision 2."* I.35's Revision 2 header claims to quote the commitments **in full**; the applies-rather-than-reproduces correction was Revision 1's. Both halves of the cross-reference are wrong, and it is the document's only statement of how it handles the doctrinal floor.
- **R13** — §4 item 7 credits Round 1's Part C as *"the instrument that discharged"* the I.35 comparison. Part C's own scope is *"the nineteen Era 1 entries not already checked by the drafts,"* and §3 B3 of this document says the I.35 check was *"direct check performed, not assumed"* by the document itself.

Plus **R14**'s 33-works-on-the-census-entry, **R15**'s recharacterization of a scope question as a theological disclosure, and **R16**'s undisclosed `provisional` on Commodian's own corpus-map row.

No HIGH finding stands against this document, and the required work is small and bounded — two clauses and three additions, none of which touches a test outcome, the Tier, or a binding obligation's substance. But two false statements about the repository, one of them inside §4's binding carry-forward, are not cosmetic, and the same class of finding carried a SUBSTANTIAL verdict against this document last round.

### Round 4 status

Not run. Neither document should open a build thread. Both should be revised against the findings above and re-reviewed, per `cic-build-cycle`'s review-gated discipline and both documents' own §6.

Three process notes for whoever runs the next revision:

1. **The recurring defect is now specifically a *crediting* defect.** Round 2's N4 was a fabricated verification; Round 3's R2, R4 and R13 are three separate cases of attributing a check or a statement to the wrong source — the wrong ancient author, the wrong review section, the wrong sibling document — while the underlying facts hold. Every "verified directly against X," "crediting Y," and "as Z states" clause in both documents should be re-read against its named source before the next round, independently of whether the claim it carries is true.
2. **`records/<world>/figure/` is not `records/<world>/`.** R1 exists because a claim about what a built world's records hold was tested against one record type. PAHC's claims on this candidate's voices live in a `source`, a `quote`, a `gravity` and a `doctrinal_witness` record, and the document's own §2 A5 already names the first of them.
3. **The heading/summary sweep Round 2 recommended was not run, or not run over §6.** R3, R8, R13 and R15 are all body-versus-summary drift, and R8 is inside the revision history itself. Reading only the headings, resolution lines, section conclusions, §4 items and §6 against one another, with the bodies closed, would have caught four of this round's fourteen findings before submission.
