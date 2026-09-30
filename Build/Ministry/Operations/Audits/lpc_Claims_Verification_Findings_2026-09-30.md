# Claims verification findings for lpc, 2026-09-30

Findings from the four Opus batch checks of `lpc_Claims_Register.md`. Each entry names a claim the check could not mark VERIFIED, with the evidence and a proposed true wording. Permanent audit record. Nothing here has been applied to a document.


---

## Batch 1

# Claims batch 1: findings (claims not marked)

Twelve claims. Two P0, six P1, four P2. Line numbers are in the file as it stands. ANF05 means `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`.

---

## `f9dafd30` (P0, wrong)

- **File and line:** Doc_04_Gravity_Discovery.md, line 94 (Candidate 5, Persistence)
- **Claim:** "Within what this document has validly read, there is no evidence that either bishop's theory was independently visible outside the one locus each is drawn from, or that it was operative or contested among ordinary clergy — only between two bishops at two moments separated by over a century."
- **What the source shows:** Both theories appear in more than one locus, and both sit in Registry rows the world already licenses.
  - **Cyprian (row 1).** The same free-judgment theory appears again in Cyprian's own letters:
    - Epistle LXXI, *To Stephen, Concerning a Council* (ANF05 line 38407): "we neither do violence to, nor impose a law upon, any one, since each prelate has in the administration of the Church the exercise of his will free, as he shall give an account of his conduct to the Lord".
    - Epistle LXXV to Magnus (line 40606): "prescribing to no one, so as to prevent any prelate from determining what he thinks right".
    - Epistle LIV to Cornelius (line 35011): each pastor rules his own portion of the flock, "having to give account of his doing to the Lord".
  - **Augustine (row 11).** The appeal to plenary councils appears outside *On Baptism*:
    - Letter XLIII (npnf101 line 28126): "there still remained a plenary Council of the universal Church".
    - Letter LIV (line 29896): "plenary Councils, whose authority in the Church is most useful".
  - **Contested by more than two bishops in Cyprian's own time.** Firmilian of Caesarea's Epistle LXXIV, *Against the Letter of Stephen* (line 39863 and following), contests it too. The 256 council also heard it before its presbyters, deacons and "a considerable part of the congregation" (line 56854).
  - **The same premise elsewhere.** Doc_04's Repetition bullet (line 90), "no second, independent Cyprian-authored locus", rests on the same false premise. That sentence is not in this batch.
- **Proposed true wording:** "Each bishop's theory recurs in more than one of his own works (Cyprian: the 256 preface and Epistles LXXI, LXXV and LIV; Augustine: *On Baptism* and Letters XLIII and LIV). In Cyprian's time it was contested among several bishops (Cyprian, Stephen, Firmilian) and argued before clergy and people at the 256 council. This document has found no evidence that it was operative in ordinary congregational formation, and the *Gesta* has not been read for this question."

## `0c59cde1` (P0, wrong)

- **File and line:** Doc_02_Source_Ecology.md, line 120 (§7)
- **Claim:** "...the pseudo-Cyprianic works of rows 6 and 194 (Hartel's Praefatio, in the row 194 file, dates manuscripts and prints no date for when the works were written)..."
- **What the source shows:** Hartel's Praefatio does date works.
  - **De Pascha Computus.** The row 194 file, pp. LXIV–LXV at lines 39129–39134, dates it: "Gordiani anno quinto Arriano et Papo consulibus a. a Christo n. 243 editus est". The text itself carries the same dating at line 14391.
  - **De duplici martyrio.** At lines 39116–39123 Hartel argues from its mentions of Diocletian's and Maximinus's persecutions that it is later. He suspects Erasmus of forging it.
  - **The inscriptions half.** This half of the sentence (row 37 names no inscription) is true.
- **Proposed true wording:** "Some Native texts are set aside from this claim because no vendored file places them inside the interval: the pseudo-Cyprianic works of rows 6 and 194 (Hartel's Praefatio dates *De Pascha Computus* to 243, before the interval, argues that *De duplici martyrio* is much later, and gives no date for the rest), and the inscriptions of row 37 (the row names no inscription and none has been checked)."

## `40334bfa` (P1, overstated)

- **File and line:** Doc_04_Gravity_Discovery.md, line 92 (Candidate 5, Formation)
- **Claim:** "This document finds no evidence in Doc02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, this specific theoretical question."
- **What the source shows:** Doc_02 §1 quotes the 256 preface from row 4. The heading of that same preface records who heard it: "a great many bishops ... together with the presbyters and deacons, and a considerable part of the congregation who were also present" (ANF05 line 56854).
  - **Awareness.** Clergy and people heard the question argued, so the source that Doc_02 relies on contradicts "not even aware" for the Cyprian phase.
  - **Formation.** No evidence of formation by the question has been found, so that half of the claim holds.
  - **The literal wording.** It survives only because Doc_02 leaves the attendance clause out. The claim misrepresents the evidence the world holds.
- **Proposed true wording:** "This document finds no evidence that ordinary believers or catechumens in either phase were formed by this theoretical question. In Cyprian's phase, clergy and 'a considerable part of the congregation' were present when the 256 council heard it (row 4), so awareness at Carthage in 256 is attested. Formation by it is not."

## `7ee09661` (P1, overstated)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 257
- **Claim:** "...because Doc04 finds no evidence that ordinary believers, catechumens, or most clergy in either phase were formed by or aware of the question."
- **What the source shows:** This claim inherits the defect in `40334bfa`. Row 4's preface records clergy and "a considerable part of the congregation" present at the 256 hearing (ANF05 line 56854).
- **Proposed true wording:** "...because Doc_04 finds no evidence that ordinary believers or catechumens in either phase were formed by the question. Clergy and people at Carthage heard it argued in 256, which attests awareness, not formation." The exclusion itself can stand on the formation ground.

## `1110900c` (P1, overstated)

- **File and line:** Doc_04_Gravity_Discovery.md, line 14 (§1)
- **Claim:** "Candidates below are generated from elements recurring across multiple Doc02 evidence streams (not one source's own emphasis)..."
- **What the source shows:** The document's own §3 contradicts this for two candidates.
  - **Candidate 7 (line 124):** "the entire evidentiary base is one voice (Augustine) within one evidence stream (the anti-Pelagian corpus, Row 23)".
  - **Candidate 5 (line 86):** each pole is "attested within each bishop's own single locus". The Augustine pole "reaches this document through Doc_01 §4 and Doc_03's own citation of it rather than through an independent Doc_02 narrative reading".
  - **The Presence/Absence clause.** Its references to Doc_02 §5–§7 check out.
- **Proposed true wording:** "Most candidates below are generated from elements recurring across multiple Doc_02 evidence streams. Two are not: Candidate 5 (one locus per pole, the Augustine pole reached through Doc_01 and Doc_03) and Candidate 7 (one voice, one stream). The Author Gravity risk for each is flagged at its heading in §3. Candidates are also generated from Attention Presence/Absence patterns Doc_02 already names: ..." Keep the rest as it is.

## `5c06ab34` (P1, overstated)

- **File and line:** Doc_02_Source_Ecology.md, line 57
- **Claim:** "Visible only through the one work attributed to him, the Vita Augustini — no other writing by Possidius survives in this world's own corpus, the same single-work visibility Pontius carries for Cyprian."
- **What the source shows:** Possidius is visible outside the Vita, in a file this world's corpus map assigns to it.
  - **The 1861 PL XI printing** of the *Gesta Collationis Carthaginiensis* (`cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`) is that file. The row 65 Verification Note records it.
  - **His own words are minuted there.** For example: "29. Possidius episcopus Ecclesiae catholicae dixit. Scriptum est: Ex multiloquio non effugies peccatum..." (line 125618), with his subscription "(Et alia manu. Recognovi.)" (line 125624). Further speeches follow at lines 128141 and 128457.
  - **His second work, the Indiculus**, is attested in the vendored Weiskotten edition (lines 622, 5625–5641), but its text is not vendored.
  - **So the parallel with Pontius fails.** Pontius is visible nowhere in this world's corpus except his Life.
- **Proposed true wording:** "Visibility: As an author, visible only through the Vita Augustini. His Indiculus of Augustine's works is attested but not vendored. His own spoken interventions and subscriptions also survive in the minutes of the 411 Conference (the PL XI *Gesta*, assigned to this world but not yet read for his voice). This is wider visibility than Pontius has for Cyprian."

## `290e910e` (P1, overstated)

- **File and line:** Doc_02_Source_Ecology.md, line 45
- **Claim:** "...§6 below documents real, if narrower, non-episcopal and lay first-person material (Pontius, Epistles XX–XXI, several of Augustine's own women correspondents)..."
- **What the source shows:**
  - **What §6 does say.** It documents Pontius, and Epistles XX–XXI (ANF05 "Celerinus to Lucian" and "Lucian Replies to Celerinus", both confirmed).
  - **The women.** §6 names only two addressees of Augustine's letters: Albina (Letter CXXVI) and the Nuns of Hippo (Letter CCXI). These are Augustine's letters to them, not first-person material by them. §6's own Gender bullet says their views "are known only through Augustine's own framing of them". The Perpetua sermons are Augustine's too.
  - **So the list overstates the lay first-person record.** Two recipients are not "several", and neither is a first-person source. The reception claim that heads the sentence holds as a reading.
- **Proposed true wording:** "...§6 below documents real, if narrower, non-episcopal and lay first-person material (Pontius; the two confessors' letters, Epistles XX–XXI), and named women who appear with real narrative weight in Augustine's own letters to them (Albina, the Nuns of Hippo), though not in their own words..."

## `b60536ca` (P1, overstated; with a P2 quotation defect)

- **File and line:** Doc_03_Lexicon_Candidate_List.md, line 46
- **Claim:** "... no bishop 'sets himself up as a bishop of bishops,' ... Row 4 (the 256 Council preface, quoted and re-verified across all nine of Doc01's own review rounds) ..."
- **What the source shows:**
  - **Quotation.** ANF05 line 56872 reads "neither does any of us set himself up as a bishop of bishops". The quotation marks enclose "sets", which the source does not have (P2). "by tyrannical terror" and "proper right of judgment" are verbatim, and the paraphrase of the rest is fair.
  - **Review rounds.** The Round 1 review (`Build/worlds/lpc/Review-Artifacts/Doc01_Round1_Review.md`) does not re-verify the preface. It asks for the Stephen dispute to be added (lines 188–196). The quotation is checked from Round 2 onward (mentions in Rounds 2–5 and 8; read in full in Rounds 6, 7 and 9). So "all nine" is overstated. Eight at most.
- **Proposed true wording:** "... that none of the bishops 'set himself up as a bishop of bishops,' ... Row 4 (the 256 Council preface, quoted from Doc_01's Round 2 onward and re-verified in each later review round) ..."

## `4dd89771` (P2, wording)

- **File and line:** Doc_03_Lexicon_Candidate_List.md, line 30
- **Claim:** "... Two adjacent details in the same chapter are attributed to Augustine's own later telling ('as he told us'): his habit, as a layman, of withholding his presence solely from churches that had no bishop ..., and, separately, his own later account that he 'understood with greater comprehension ...' ..."
- **What the source shows:**
  - **Verified quotations.** Every quotation was checked verbatim: Ep. XXXIX (ANF05 line 32373), Pontius (27818), Letter XXXI §4 (npnf101 line 25856), Possidius *Vita* IV and VIII (`cic/texts/possidius_vita-augustini_weiskotten1919.txt` lines 1809–1821, 1860, 2127–2143).
  - **Suffrage.** "Suffrage" does not occur in the Vita IV account.
  - **The count of attributions.** Vita IV has three attributions to Augustine's own telling, not two. The third, at line 1817, is: "But some, as he himself later told us, at the time ascribed his tears to wounded pride".
- **Proposed true wording:** "Three details in the same chapter are attributed to Augustine's own later telling ('as he told us'): his habit, as a layman, of withholding his presence solely from churches that had no bishop ...; that some at the time put his tears down to wounded pride and consoled him that the presbyterate was little below the episcopate; and his own later account that he 'understood with greater comprehension ...'" Keep the rest as it is.

## `77949f87` (P2, wording)

- **File and line:** Doc_03_Lexicon_Candidate_List.md, line 63
- **Claim:** "...named by Doc01 itself as 'a preliminary observation worth Doc04's own testing, not asserted as a confirmed gravity,'..."
- **What the source shows:**
  - **The misquotation.** Doc_01 line 130 reads "a preliminary observation worth Doc_04's testing, not asserted as a confirmed gravity". The word "own" is inserted inside the quotation marks.
  - **Verified content.** Everything else was checked:
    - Doc_01 §6's two refusals and its "single test of purity".
    - The "same rigor Donatism itself later revived" quotation.
    - Row 23's Licensed-For wording.
    - The 1,798 and 1,665 counts. These reproduce exactly as case-insensitive substring counts over NPNF105 div1 x–xxi, which holds thirteen works, since xxi Book II is On the Gift of Perseverance.
- **Proposed true wording:** "...named by Doc_01 itself as 'a preliminary observation worth Doc_04's testing, not asserted as a confirmed gravity,'..."

## `f945a231` (P2, wording)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 195 (§5.3)
- **Claim:** "...(Doc04 finds no other candidate depends on it resolving either way), and carries an Author Gravity risk flagged at generation: the entire evidentiary base is one voice within one evidence stream..."
- **What the source shows:**
  - **Accurate report of Doc_04.** The claim reports Doc_04 correctly (Candidate 7, lines 124 and 128).
  - **But the world holds more.** As a statement about the world's evidence, "the entire evidentiary base ... one evidence stream" is inaccurate. "Grace" also runs through Augustine's preaching in licensed rows. Word counts of "grace":

    | Volume | Rows | Count |
    |---|---|---|
    | npnf106 | 19, 21 | 190 |
    | npnf107 | 21 | 262 |
    | npnf108 | 20 | 332 |

  - **Where the gap shows.** Doc_04 did not draw on the preaching. §5.3 needs that evidence, because it goes on to say an ordinary believer at Hippo "is being formed by this material".
- **Proposed true wording:** "...carries an Author Gravity risk flagged at generation: the evidentiary base Doc_04 drew on is one voice within one evidence stream (row 23). Augustine's preaching (rows 19–21) also treats grace at length, which Doc_04 did not draw on..."

## `665fd6b0` (P2, unsupported cross-reference)

- **File and line:** Doc_02_Source_Ecology.md, line 109
- **Claim:** "...almost never record an ordinary believer speaking in their own voice, at length, in a way that survives independent of the bishop's own framing — the same structural problem Doc01 §6's own Forces sketch names for the century-gap discussion..."
- **What the source shows:**
  - **The main claim holds.** "Almost never ... at length ... independent of the bishop's framing" is a sound reading. The exceptions are Epistles XX–XXI, and short congregational acclamations recorded inside episcopal texts.
  - **The cross-reference does not.** Doc_01 §6 (lines 120–143) was read in full. Neither its prose nor its six-cell sketch names any problem about ordinary believers' voice or the century gap. The nearest statement is the Ending/Transforming cell's note that the closing decades are better attested than the opening ones. The voice-of-the-substrate point is at Doc_01 §2 (line 35).
- **Proposed true wording:** "...almost never record an ordinary believer speaking in their own voice, at length, in a way that survives independent of the bishop's own framing. This extends across the whole 184-year span the asymmetry Doc_01 §2 names, that the surviving sources overwhelmingly preserve the literate, Latin-trained episcopal voice."

---

## Batch 2

# Claims batch 2: findings (not marked)

## c403950b  (P1)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 27
- **Claim:** They belong to his phase and do not fill the silence, and no source fixes their order.
- **What the source shows:** Pontius, Life 11.1 (anf05 line 28003, Registry row 7): "what God's priest replied to the interrogation of the proconsul, there are Acts which relate", so the record of the 257 hearing already existed when the Life was written. Harnack (row 205, cic/texts/harnack_vita-cypriani-commentary-lat-deu_1913.txt lines 376-381) argues that Pontius cannot yet have had the Acta proconsularia in their compiled form, and dates the Life to 259 as the prevailing view; he calls the two martyr acts contemporary with the Life (line 4361). So a partial order is attested for the hearing record and argued for the compiled Acta. What no source fixes is the full sequence, and above all where the two martyr acts fall. Doc_02 §7 cites Harnack for the date but not for his order argument, and it makes the same statement.
- **Severity:** P1
- **Proposed true wording:** They belong to his phase and do not fill the silence. Their full sequence is not fixed: Pontius already cites the record of Cyprian's first hearing, Harnack argues that the Acta as compiled came after the Life, and no source places the two martyr acts relative to the others.

## 9e5090d0  (P2)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 281
- **Claim:** This world is not one continuous ecology; it is two attested phases with an interval that is silent in this world's own voice, and the construction says so at every level.
- **What the source shows:** The interval is not silent in every voice of this world. The Code of Canons of the African Church (row 26, cic/texts/npnf214_seven-ecumenical-councils.xml lines 32276-32279 and 32592) carries canons of Catholic African councils at Carthage under Gratus (345-348) and Genethlius (387 or 390). Augustine wrote as a layman before 391 (rows 11, 22, 25). Doc_02 §7 and this document's own table (line 287: "None that continues Cyprian's voice") use the narrower and true bound. This heading sentence drops it.
- **Severity:** P2
- **Proposed true wording:** This world is not one continuous ecology; it is two attested phases with an interval in which no source continues Cyprian's pastoral or congregational voice, and the construction says so at every level.

## 09e32fac  (P1)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 175
- **Claim:** What it does not do, on this document's evidence, is reach ordinary formation: Doc04 finds no evidence in Doc02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, this specific theoretical question, and §5 below does not narrate it as part of anyone's formation.
- **What the source shows:** The report of Doc_04 is accurate (Doc_04 line 92). But the "or even aware of" limb is contradicted by the corpus. The preface to the Seventh Council of Carthage (Registry row 4, anf05 lines 56850-56872) records "a considerable part of the congregation who were also present" when Cyprian spoke the "bishop of bishops" formula. That is evidence of lay exposure to the question. No build file mentions it (a search for "considerable part of the congregation" and "plebis maxima" in Build/worlds/lpc and records/lpc finds nothing). The formation limb still holds.
- **Severity:** P1
- **Proposed true wording:** Doc_04 finds no evidence that ordinary believers, catechumens, or most clergy in either phase were formed by this specific theoretical question. The one sign of lay contact is that a large part of the congregation was present at the 256 council when Cyprian spoke his formula (row 4). §5 below does not narrate it as part of anyone's formation.

## a187ea83  (P0)

- **File and line:** Doc_05_Ecological_Reconstruction.md, line 151
- **Claim:** [Construction note: Tier 4 — Historically Grounded Reconstruction. The catechetical sequence rendered here is what rows 5, 15 and 18 presuppose and what Doc02 §5 names; the specific order, wording, gestures and setting of the rites at Carthage or at Hippo are not attested in anything this build has verified (Doc02 §5, §9 items 2 and 9), and nothing about them is supplied.
- **What the source shows:** The wording of a baptismal rite at Carthage is attested in a Confidence A row. Cyprian, Epistle LXIX (Registry row 1, anf05 line 38062), says: "when we say, 'Dost thou believe in eternal life and remission of sins through the holy Church?'" This build's own lpcctx002_the-questions-at-the-water.md carries that interrogation at Widely Accepted. For Hippo, the order is attested: Augustine's sermon to the competentes (npnf106 lines 10643 and 10839) says "first the Creed ... and afterwards the Prayer", and lpcctx001 carries it. Gestures are attested too: signing with the cross and salt appear in Confessions I.11 (npnf101 line 4431), though for Thagaste, not Carthage or Hippo. The claim is wrong on the wording limb and on the Hippo order limb.
- **Severity:** P0
- **Proposed true wording:** The catechetical sequence rendered here is what rows 5, 15 and 18 presuppose and what Doc_02 §5 names. Some parts of the rites are attested and are not supplied here: the baptismal interrogation's wording at Carthage (Cyprian, Ep. LXIX; lpcctx002) and the creed-before-prayer order at Hippo (Augustine's sermons to the competentes; lpcctx001). The setting, gestures and full order of the rites at Carthage or Hippo are not attested in anything this build has verified, and nothing about them is supplied.

## 1b8bdab8  (P1)

- **File and line:** Doc_06_Full_Lexicon_Development.md, line 61
- **Claim:** Now Tier 2, on a bound Doc04 states and Doc05 §6.7 applies: there is no evidence that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, this question.
- **What the source shows:** The same limb as 09e32fac. The 256 council preface (row 4, anf05 line 56850 onward) records a large part of the congregation present when the "bishop of bishops" formula was spoken. So "no evidence that ... [they were] even aware of this question" overstates. The Tier 2 ground, that the question did not organize ordinary formation, still holds.
- **Severity:** P1
- **Proposed true wording:** Now Tier 2, on a bound Doc_04 states and Doc_05 §6.7 applies: there is no evidence that ordinary believers, catechumens, or most clergy in either phase were formed by this question, though a large part of the Carthaginian congregation was present when Cyprian spoke the formula in 256.

## 12785a57  (P1)

- **File and line:** Doc_07_Integrated_Ecology_Analysis.md, line 186
- **Claim:** One pattern is deliberately excluded and the exclusion is a finding, not an omission. Neither conciliar formula (G5) is a Representative theological pattern on this document's evidence, because Doc04 finds no evidence that ordinary believers, catechumens or most clergy in either phase were formed by, or aware of, the question.
- **What the source shows:** Same evidence as 09e32fac: the laity were present at the 256 council (row 4, anf05 line 56850 onward). The exclusion itself is sound on the formation limb.
- **Severity:** P1
- **Proposed true wording:** Neither conciliar formula (G5) is a Representative theological pattern on this document's evidence, because Doc_04 finds no evidence that ordinary believers, catechumens or most clergy in either phase were formed by the question; the congregation's presence at the 256 council shows exposure, not formation.

## bfad9bc9  (P1)

- **File and line:** Doc_07_Integrated_Ecology_Analysis.md, line 128
- **Claim:** That is a real distortion in the institutional picture: the ordinary, non-factional work of a presbyter in this world is essentially unattested, and a Representative should not be built as though the presbyterate were inherently oppositional.
- **What the source shows:** Ordinary, non-factional presbyteral work is attested in both phases. Cyprian, Epistle IV, To the Presbyters and Deacons (anf05 lines 28956-29000, row 1): the presbyters are to "discharge there both your own office and mine", fund the imprisoned and the poor, and "the presbyters also, who there offer with the confessors, may one by one take turns with the deacons". Augustine, Letter XXI (391), written as a presbyter to Valerius (npnf101 line 23816, row 11), is a first-person account of the presbyter's office. Possidius, Vita ch. V (cic/texts/possidius_vita-augustini_weiskotten1919.txt) records presbyters preaching by their bishops' permission. The 2026-09-29 carried-open check (P1-3) caught Possidius but proposed restricting the claim to Cyprian's phase, and Epistle IV refutes that too.
- **Severity:** P1
- **Proposed true wording:** That is a real distortion in the institutional picture: the presbyters' ordinary work is attested far more thinly than their factions, in instructions such as Cyprian's Epistle IV (presbyters offering the Eucharist with imprisoned confessors, turn by turn with the deacons) and Augustine's own Letter XXI as a presbyter, and a Representative should not be built as though the presbyterate were inherently oppositional.

## b005b155  (P1)

- **File and line:** Doc_07_Integrated_Ecology_Analysis.md, line 62
- **Claim:** What is missing is not the un-hostile record but the non-episcopal one: the interior life of any ordinary believer in this world is Inferential/Thin and is narrated nowhere in this build.
- **What the source shows:** "What is missing is ... the non-episcopal one" is contradicted by Doc_02 §6, which this build accepts (Doc_05 §0.4, Doc_08 2B-5 item 1). Doc_02 §6 names a deacon's first-person account (Pontius, row 7), two lay confessors writing in their own voices (Epistles XX-XXI, row 1) and named women in Augustine's letters. The build itself narrates Celerinus's interior grief ("weeping day and night") in Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md. What holds is narrower: there is no ordinary congregant's own account, and no build text narrates an ordinary (non-confessor) believer's interior life.
- **Severity:** P1
- **Proposed true wording:** What is missing is not the un-hostile record but the ordinary one: a deacon and two lay confessors do write, but no ordinary congregant does, and the interior life of an ordinary believer in this world is Inferential/Thin and is narrated nowhere in this build.

## 5e5e442b  (P1)

- **File and line:** Doc_07_Integrated_Ecology_Analysis.md, line 94
- **Claim:** What is tested here is the document's stated warrant for how it records that ruling." What is open is the warrant, not the outcome — whether Doc04 can reach Supporting on its own evidence rather than resting solely on the ruling.
- **What the source shows:** The Round 9 quotation is accurate (Build/worlds/lpc/Review-Artifacts/Doc04_Round9_Review.md line 18). But the status is stale. Doc_04 §7 item 8 (Doc_04 line 214) reads "CLOSED, 2026-09-15, on the gapped-formation precedent", and it records the Round 9 argument "recorded, not pursued", accepting Supporting as "honestly thin". So neither the warrant nor the outcome is open in the governing document.
- **Severity:** P1
- **Proposed true wording:** What Round 9 tested was the warrant, not the outcome — whether Doc_04 can reach Supporting on its own evidence rather than resting solely on the ruling; Doc_04 §7 item 8 has since closed that question on the gapped-formation precedent, recording the argument without pursuing it.

## 6c30b049  (P1)

- **File and line:** Doc_07_Integrated_Ecology_Analysis.md, line 128
- **Claim:** What this reveals that Doc05 alone did not show: the presbyters appear in this record almost exclusively as faction — five in recorded opposition to Cyprian's election, an Epistle addressed to the people concerning five schismatic presbyters.
- **What the source shows:** "Almost exclusively as faction" is overstated. Most of Cyprian's letters are addressed "to the presbyters and deacons" and task them with ordinary work: Epistle IV (anf05 lines 28956-29000) asks them to keep discipline, care for prisoners and the poor, and celebrate with the confessors in rotation. Epistle XXXIV (anf05 line 32115) records a confessor added to the presbyterate. On Augustine's side there is Letter XXI (npnf101 line 23816) and Possidius, Vita ch. V. The faction material is real (the five presbyters of Epistle XXXIX), but it is one strand.
- **Severity:** P1
- **Proposed true wording:** What this reveals that Doc_05 alone did not show: the presbyters' best-documented collective acts in this record are factional — five in recorded opposition to Cyprian's election, an Epistle addressed to the people concerning five schismatic presbyters — while their ordinary work survives only in the bishop's instructions to them.

## d8a49b93  (P1)

- **File and line:** Doc_08_Forces_Document.md, line 297
- **Claim:** 2A-2 (none) — Deliberately isolated. The plague connects to no other force in this matrix and produced teaching rather than structure. Recorded as a connection that does not exist, per the Named-Tension and Cross-Cell principles.
- **What the source shows:** Within the matrix the statement is true: no Named Cross-Cell Connection row touches 2A-2 (Doc_08 lines 290-304, lpc_Force_Index.md line 86). But the stated ground, that the plague "produced teaching rather than structure" (Layer 3 at line 125: "generated no gravity and no practice"), is contradicted by row 7. Pontius, Life 9-10 (anf05 lines 27939-28003) records Cyprian assembling the people and the relief that followed: "the ministrations are constantly distributed according to the quality of the men and their degrees", done "to all men". Life 11 then links the relief to the exile: "Banishment followed these actions", which is the Valerianic force 2A-1. Registry row 5's Ad Demetrianum answers the pagan charge that plague must be "imputed to the Christians" (anf05 line 45611). No build file cites Pontius 9-10 for the relief, apart from review files and lpcstory002.
- **Severity:** P1
- **Proposed true wording:** 2A-2 (none) — No cross-cell connection is registered. The plague's best-attested response is teaching (De Mortalitate), but Pontius (Life 9-11) also records organized relief distributed by rank and followed by Cyprian's banishment; whether that is a link to 1B-1 and 2A-1 is an open question, not a demonstrated absence.

## 31abcdcc  (P2)

- **File and line:** Doc_08_Forces_Document.md, line 302
- **Claim:** 2B-4 3B-2 is the sole instance of 2B-4 is the only force in this matrix that carries formation logic across the 133-year silence recorded at 3B-2. The crossing is textual and is attested twice; the second instance, Possidius quoting Cyprian, is not a force in this matrix.
- **What the source shows:** As a statement about the matrix's registered connections it is true: no other force is placed across 3B-2. But "the crossing is textual", which is Doc_07 §3A's "textual, not successive" carried into 3B-2 Layer 2 ("received as text rather than carried as living memory"), leaves out a non-textual continuity in a Native source. Confessions V.8 (npnf101 line 8104, row 9) places Monica, c. 383, at "an oratory in memory of the blessed Cyprian" near the harbour at Carthage. That is a living cult of Cyprian inside the interval. A search of Build/worlds/lpc and records/lpc for "oratory" or "memoria" finds no treatment of it.
- **Severity:** P2
- **Proposed true wording:** 2B-4 is the only force in this matrix that carries formation logic across the 133-year silence recorded at 3B-2. Its crossing is textual and is attested twice (the second, Possidius quoting Cyprian, is not a force here); a separate, non-textual continuity — the oratory in memory of Cyprian at Carthage that Confessions V.8 records — is not assessed in this matrix.

## ae707134  (P1)

- **File and line:** Doc_08_Forces_Document.md, line 264
- **Claim:** Layer 1 — Historical Event. Doc01 §6 names it as a real asymmetry this world's Doc02 must not let pass unremarked: this world's closing decades are disproportionately well-attested relative to its opening ones. And between the phases, Doc02 §7 records that the roughly 133 years between Cyprian's martyrdom and Augustine's ordination begin with the texts written at and just after Cyprian's martyrdom (the Acta Cypriani, Pontius's Life, and the two martyr acts of rows 231 and 232); they belong to his phase and do not fill the silence, no source fixes their order, and from them to Augustine's ordination no source supplies a bishop's ordinary pastoral or congregational voice, or a congregation's voice, that continues Cyprian's.
- **What the source shows:** This is the same statement as c403950b, repeated in 3B-2 Layer 1: "no source fixes their order". The evidence is the same: Pontius, Life 11.1 (anf05 line 28003) cites existing Acts of the hearing, and Harnack (row 205, lines 376-381) orders the Life before the compiled Acta. The rest of the claim checks: the Doc_01 §6 asymmetry is at Doc_01 line 138, and the Doc_02 §7 wording matches.
- **Severity:** P1
- **Proposed true wording:** Replace "no source fixes their order" with "their full sequence is not fixed (Pontius already cites the record of the first hearing; Harnack places the Acta as compiled after the Life; nothing places the two martyr acts)". Leave the rest of the sentence unchanged.

## 53939147  (P1)

- **File and line:** Doc_08_Forces_Document.md, line 330
- **Claim:** This is the weakest force-connection in the matrix and the document says so rather than padding it. Doc04 records that this candidate exhibits the shape the Forces Framework names when it states that "[A] gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete." The connection here is real but indirect: every force touching G5 touches it through a third party's citation of a text, not through a pressure on the world's own practice — which is consistent with Doc04's finding that no evidence shows the question reached ordinary formation.
- **What the source shows:** The limb "no evidence shows the question reached ordinary formation" holds. But "every force touching G5 touches it through a third party's citation of a text" contradicts this document's own 1B-1 entry. 1B-1 Layer 3 (Doc_08 line 79) "supplies G5 with the conciliar setting in which both its formulas are eventually spoken". Cyprian's formula was spoken at a council the world itself convened, with presbyters, deacons and a large part of the congregation present (row 4, anf05 line 56850 onward). That is the world's own practice, not a third party's citation. Only 2A-3 and 2B-4 run through citation.
- **Severity:** P1
- **Proposed true wording:** The connection here is real but indirect: 1B-1 supplies only the conciliar setting, and the other two forces touching G5 (2A-3, 2B-4) reach it through a later party's citation of a text rather than through a pressure on the world's own practice — which is consistent with Doc_04's finding that no evidence shows the question reached ordinary formation.

## 8903963f  (P1)

- **File and line:** Doc_09_Story_Inventory.md, line 180
- **Claim:** An escalation is a claim that a governing document is silent, and that claim needs the same verification as any other. Unresolved tensions: one open — the 411 Gesta, relied on for nothing here.
- **What the source shows:** The first sentence is a method statement and not in dispute. The second is stale. Doc_04 §7 item 6 (Doc_04 line 213) reads "CLOSED AS A PERSISTENCE QUESTION, 2026-09-15". Open_Gaps_Tracking.md OG-4 (line 464) records the 411 Gesta as "closed as a source question, not an open item". The 2026-09-29 carried-open check (Build/worlds/lpc/Review-Artifacts/L0_Docs03-05-06-07_Carried_Open_Check_2026-09-29.md line 235) says every "unresolved tensions: one open" count rests on the stale state. That the Gesta is "relied on for nothing here" is true (Doc_09 lines 110 and 137; no story chunk cites it).
- **Severity:** P1
- **Proposed true wording:** An escalation is a claim that a governing document is silent, and that claim needs the same verification as any other. Unresolved tensions: none open — the 411 Gesta, relied on for nothing here, was closed as a source question on 2026-09-15 (Doc_04 §7 item 6; OG-4).

---

## Batch 3

# Claims batch 3: findings (claims not marked)

Fourteen claims. Each is false, overstated, unsupported, or misleadingly worded when checked at source. Paths are repository-relative. Line numbers are those of the file at the time of checking.

---

## G5 group: "no evidence ... aware of" the conciliar question (5 rows, one finding)

| id | file:line |
|---|---|
| `82d0c263` | lpc_World_Profile.md:554 |
| `be767c0a` | lpc_World_Profile.md:128 |
| `52aa9b06` | lpc_World_Profile.md:242 |
| `c168ca30` | lpc_World_Profile.md:188 |
| `0641c050` | lpc_World_Profile.md:216 |

**Claim (common form):** Doc04 finds no evidence that ordinary believers, catechumens or most clergy were formed by, "or (even) aware of", the conciliar-authority question (G5).

**What the source shows:** Cyprian's egalitarian formula ("neither does any of us set himself up as a bishop of bishops") was stated in the 256 council preface. That same preface records who was in the room. The Latin reads *"cum presbyteris et diaconibus, praesentibus etiam plebis maxima parte"* (`cic/texts/cyprian_sententiae-episcoporum-lat_hartel1868-csel3-tei.txt`, preface, lines 107–109; Registry row 261). The ANF reads "together with the presbyters and deacons, and a considerable part of the congregation who were also present" (`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` line 56854; Registry row 4).

So the one text that carries the formula places presbyters, deacons and a large lay crowd at its delivery. That is direct evidence of exposure. It does not show formation. No file in `Build/worlds/lpc` or `records/lpc` cites this clause. Doc04's own finding (Doc_04 line 92) is also scoped to "no evidence in Doc_02". The World Profile drops that scope.

**Severity:** P1, overstated. "Formed by" holds. "Aware of" is contradicted by the source that carries the formula.

**Proposed wording (adapt per site):** "Doc04 finds no evidence that ordinary believers, catechumens or most clergy in either phase were formed by this question. The one sign of lay exposure is the 256 council preface: presbyters, deacons and 'a considerable part of the congregation' were present when Cyprian stated his formula (Registry rows 4 and 261). Nothing shows what they made of it, and nothing shows the question reaching ordinary believers in Augustine's phase."

Doc_04 §3 Candidate 5 (Formation test), Doc_05 line 257 and Doc_07 line 186 carry the same wording and need the same check. They are outside this batch.

---

## `8c8ff86b` — lpc_World_Profile.md:224

**Claim (the part at issue):** "Presbyters appear almost exclusively as faction in Cyprian's phase (five in recorded opposition to his election) — a real distortion."

**What was checked and holds:** The Possidius VIII quotes match Weiskotten lines 2134–2142 ("elageriy" is OCR for "eagerly"). The Pinianus episode matches NPNF101 Letter CXXVI (line 44449: "demanding Pinianus as presbyter").

**What the source shows:** Presbyters appear often in Cyprian's own letters as something other than faction:
- **Rogatianus** is a presbyter and confessor (ANF Ep. VI, addressed to him).
- **Numidicus** is ordained presbyter for his confession (Ep. XXXIV). This world's own lpcstory003 is built on that letter.
- Cyprian names both Rogatianus and Numidicus as his commissioned substitutes against Felicissimus (Ep. XXXVIII, line 32247: "to Rogatianus and Numidicus, his fellow-presbyters").
- The presbyters and deacons are the body running the church in his absence: Ep. IV, V, VII, XII, XIII. Ep. XXXV (care of the poor and strangers) is ordinary administrative work.

The five opposed presbyters (Ep. XXXIX) are the most dramatic presbyters in the record, not nearly the only ones. The same overstatement comes from Doc_07 line 128 (register id `6c30b049`, outside this batch).

**Severity:** P1, overstated. The world's own lpcstory003 contradicts it.

**Proposed wording:** "In Cyprian's phase, presbyters appear most vividly as faction: five opposed his election, and Ep. XXXIX addresses the people about them. Loyal presbyters appear too. Rogatianus and Numidicus are confessors whom Cyprian commissions as his agents (Ep. XXXVIII), and his letters to 'the presbyters and deacons' show the clergy running the church while he was away. What is thin is any presbyter's own voice about his ordinary work."

---

## `d610f6dd` — lpcstory001_election-of-cyprian.md:37

**Claim:** "Where Pontius is the only witness and the narrative carries the conventions Delehaye catalogues, this build assigns Tier 3 instead — see lpcstory006."

**What the source shows:** The build does not apply the rule as worded. lpcstory002 rests on Pontius alone for the relief ("it is the only account we have", line 68). It admits that marker one (idealising portraiture) and a scriptural typology (Tobias) are present. Yet it is Tier 1. It argues that conventions applied to Pontius's estimate of the man, rather than to what physically happened, do not move the tier. lpcstory006 is Tier 3 because the conventions shape the events themselves (typology in the narration, a providential intervention, the death as completion). So the rule the build actually uses is narrower than this sentence.

**Severity:** P2, wording. It states the rule more broadly than the build applies it.

**Proposed wording:** "Where Pontius is the only witness and the conventions Delehaye catalogues shape the events themselves (typology in the narration, a providential intervention, the death as completion), this build assigns Tier 3 instead. See lpcstory006, and lpcstory002 for why idealising portraiture alone does not move the tier."

---

## `1aba44c7` — lpcstory002_the-plague-and-the-enemies.md:33

**Claim:** "Doc08's Force 2A-2 — epidemic disease — is the one force in this world's whole matrix that connects to no other."

**What the source shows:** `Build/worlds/lpc/lpc_Force_Index.md` §1 lists two forces with no cross-cell connection:
- **2A-2**, marked "none — see §4".
- **1B-3**, the inherited Latin theological vocabulary, marked "(no §4 row)".

Doc_08 §4 has no connection row for 1B-3 (Doc_08 lines 93–97 connect it only to G4). 2A-2 is the only force Doc08 *records* as deliberately isolated (Doc_08 lines 297, 314). It is not the only force with no connection. The story repeats Doc_08 line 314 ("the one isolated force"), which has the same defect.

**Severity:** P1. Wrong against the world's own Force Index.

**Proposed wording:** "Doc08's Force 2A-2 (epidemic disease) is the one force Doc08 records as deliberately connected to no other in its matrix."

A separate open point, outside this batch: either 1B-3 needs a §4 connection, or Doc08 needs to state that 1B-3 has none.

---

## `7a0e9082` — lpcstory002_the-plague-and-the-enemies.md:68

**Claim:** "The absence is a survivorship gap of the ordinary kind: relief work leaves no documents, and the people on the receiving end of this one were not writing."

**What the source shows:** In this same world, relief work does leave documents. ANF Ep. LIX (Hartel LXII) is a relief letter. It sends 100,000 sesterces to ransom captives, and Cyprian says he has "subjoined the names of each one" who gave (ANF05 lines 36082–36105). lpcstory004 is built on it. The second half of the claim (the recipients were not writing) holds. The corpus sweep found no recipient's account.

**Severity:** P2, overstated generalisation.

**Proposed wording:** "The absence is a survivorship gap of the ordinary kind. Help given house to house in an epidemic leaves few documents, unlike the ransom letter of lpcstory004. The people on the receiving end of this help were not writing."

---

## `a5bad882` — lpcstory003_numidicus.md:33

**Claim:** "This letter shows a bishop doing something with a confessor — and doing it in a way that answers a pastoral problem the treatises never name."

The problem the chunk names in the next sentence is that "Numidicus did not want to be alive". In other words, a man ready for martyrdom was left behind.

**What the source shows:** Cyprian's treatise *On the Mortality* §17 names this very grief and answers it. The ANF05 text (lines 47069–47090) reads: "that I, who had been prepared for confession ... am deprived of martyrdom". Cyprian's answer is that "martyrdom is not in your power", and that God crowns the ready will: "It is one thing for the spirit to be wanting for martyrdom, and another for martyrdom to have been wanting for the spirit." The circumstances differ: death by plague there, surviving the stones here. The pastoral problem is the same.

**Severity:** P1. Overstated, and contradicted by a Native treatise (Registry row 1 corpus; `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`).

**Proposed wording:** "This letter shows a bishop doing something with a confessor. It answers, for one named man, a grief the treatises answer only in general. *On the Mortality* §17 consoles the Christian who was ready for martyrdom and denied it. Here the answer is an office."

---

## `85c2781c` — lpcstory005_celerinus-writes-to-lucian.md:57

**Claim:** "If a participant asks what any of them thought, the answer is that no one wrote it down."

**What the source shows:** The claim asserts that nothing was ever written. The evidence supports only that nothing survives. The chunk's own Absent Story Note (line 65) says: "The lapsed did write, and what they wrote is lost", and calls this "source loss", not silence. It cites ANF Ep. XXVI, whose argument says "the Letter of the Lapsed to Which He Replies is Wanting" (ANF05 line 31246). Whether Numeria, Candida or Celerinus's sister ever wrote is unknowable. The claim contradicts the chunk's own classification of the absence.

**Severity:** P2, wording. As worded it is unsupported, and it is inconsistent with the same chunk.

**Proposed wording:** "If a participant asks what any of them thought, the answer is that no word of theirs survives."

---

## `36bd8e42` — lpcstory006_the-death-of-cyprian.md:47

**Claim:** "... this build has no independent witness, because the Acta is unread. Reading it would likely move this story to Tier 1."

**What the source shows:**
- The *Acta* is unread. It is vendored in Latin in rows 194 and 41, and is also printed in rows 231 and 232 (Knopf; Gebhardt).
- The reason given is incomplete. The assigned corpus holds a second route independent of Pontius: Augustine's feast-day sermons on Cyprian, Sermo 309–313, in Registry row 227 (`cic/texts/augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt`).
- Sermo 309 begins at line 101237 ("In Natali Cypriani martyris, i"; the heading is OCR-garbled). It retells the passio from the *Acta*: the exile to Curubis under the proconsul Paternus, the arrest by two apparitors, the night vigil of the brethren, the order to guard the girls, and the proconsul's words.
- Row 227 is second-witness OCR only and unread by this build. So "has no independent witness" is true only as "has read none". The *Acta* is not the only one.
- The Tier 1 prediction is a judgement and is stated as one.

**Severity:** P2. The reason is incomplete.

**Proposed wording:** "... this build has read no independent witness. The *Acta Proconsularia* (rows 41 and 194; also printed in rows 231 and 232) is vendored in Latin and unread. Augustine's feast-day sermons on Cyprian (Sermo 309–313, row 227, second-witness OCR only) retell the trial from the *Acta* and are also unread. Reading the *Acta* would likely move this story to Tier 1."

**Related, outside this batch:** Doc_09 §6 item 1 and §8 item 5 say Augustine's sermons on Perpetua are "not available to this build at all ... Unavailable is a different problem from unread". Row 227's vendored file contains Sermones CCLXXX–CCLXXXII "In Natali martyrum Perpetuae et Felicitatis" (lines 91963, 92185, 92280). These are available, as second-witness OCR. That is a P0 against Doc_09, and it bears on the Doc09 register.

---

## `2e965f1d` — lpc.contested.cyprian-death-genre.md:50 (records/lpc/contested_claim)

**Claim:** "... this build has no independent witness, because the Acta Proconsularia ... is vendored in Latin only and has not been read in this build (Doc09 §6 item 2, §8 item 1; Story-Chunks/lpcstory006, Absent Story Note)."

**What was checked:** The quote matches lpcstory006 line 47 verbatim. The Doc09 §6 item 2 and §8 item 1 citations are accurate.

**What the source shows:** The same gap as `36bd8e42`. Sermo 309–313 (row 227) is a vendored, unread witness to the trial that is independent of Pontius. The *Acta* is also printed in rows 231 and 232.

**Severity:** P2.

**Proposed wording:** "... and this build has read no independent witness. The Acta Proconsularia, the strictly documentary record of the trial that Pontius himself points readers toward, is vendored in Latin only (rows 41 and 194; also printed in rows 231 and 232) and unread. Augustine's feast-day sermons on Cyprian (Sermo 309–313, row 227, second-witness OCR only), which retell the trial from it, are also unread (Doc09 §6 item 2, §8 item 1; Story-Chunks/lpcstory006, Absent Story Note)."

---

## `3b49ec7e` — lpcstory007_the-psalms-on-the-wall.md:68

**Claim:** "What no second source gives is the interior of the sickroom, and for that this story depends on one man more completely than any other Tier 1 story in this repository."

**What was checked and holds:** The first half. The sweep for the sickroom details found them only in Possidius XXXI; Prosper a. 430 gives the death, the date and the siege.

**What the source shows:** The comparative is not supported by the other Tier 1 stories:
- **lpcstory003** rests entirely on one paragraph of one letter by Cyprian (ANF Ep. XXXIV). No second witness exists for any of its events. Numidicus appears elsewhere only as a name (Ep. XXXVIII–XXXIX).
- **lpcstory004** rests on one letter (Ep. LIX).
- **lpcstory002's** relief rests on "a single friendly witness" (its own line 68).

lpcstory007 at least has Prosper corroborating the death, the date and the siege. It is no more single-witness than these stories, and arguably less.

**Severity:** P2. The comparative is overstated.

**Proposed wording:** "What no second source gives is the interior of the sickroom. For that, this story depends on one witness, as lpcstory002's account of the relief and lpcstory003's account of Numidicus also do."

---

## Batch 4

# Claims batch 4 (lpc): findings on claims not marked

These 17 claims could not be marked VERIFIED or JUDGEMENT. Line numbers are file lines. Every quoted source line was read in context at the path given.

## Group A: the 133-year silence (64c5c68e, 649d0bf6, cf8ec194, 31bdac99)

Shared evidence. Doc_02 §7 (Build/worlds/lpc/Doc_02_Source_Ecology.md, line 120) scopes the silence to "no source in the Registry". It argues that conciliar canons are not "a surviving voice of ordinary pastoral or congregational life continuous with Cyprian's", and it sets aside texts that no vendored file dates. On that reading, the claim holds for the Registry. Two things weaken it as the records state it: flat, with the Registry scope dropped, and described as "a fact about our record, and it can be checked against our sources".

1. **An unassessed in-gap bishop's sermon in the assigned corpus.** The corpus map `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` assigns to this world the entry "Tractatus novem from codex Guelferbytanus 4096 (Optatus of Milevis, Quodvultdeus of Carthage and others...)". It is in `cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt` from line 10297. Its first piece opens "Hodie, fratres carissimi", which is congregational preaching. At lines 1701-1703, Morin gives one tractatus, the sermon on the Holy Innocents, to "Optato Mileuitano episcopo, qui Augustinum aetate praecessit". He calls this "haud sine aliqua ueri similitudine" (not without some likelihood). The manuscript ascription is at line 10850. Optatus was a Catholic African bishop active c. 366-385, per the Doc_02 §7 file headers, so this is a candidate bishop's congregational voice inside 258-391. Registry row 229 says these nine tractatus are "unassessed ... no row". None of the silence claims names them.
2. **An in-gap bishop of Carthage speaking in council.** Registry row 202 (`cic/texts/codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt`, lines 7858-7880) has Gratus of Carthage speaking in his own first person ("idem Gratus episcopus dixit ...") at a council of Carthage in the time of Paul and Macarius (c. 345-348). Genethlius speaks at the 390 council (line 8382). Doc_02 §7 names these as licensed exceptions. The force record's description does too. But the manifestation (649d0bf6) lists only Optatus and the appendix as "the Registry texts dated inside the gap that this world names".

- **64c5c68e**. File `lpc.force.transmission-asymmetric-span-133-year-silence.md`, line 42 (description). Claim: "After them, none of our sources carries on Cyprian's voice." Source shows: the claim holds for the Registry only, under the Doc_02 §7 reading. The assigned corpus holds the unassessed Optatus sermon (item 1). Severity **P1** (unsupported as scoped). Proposed wording: "After them, none of the sources we have assessed carries on Cyprian's voice: no sermon, letter or treatise by a bishop of ours, and no congregation's own words."
- **649d0bf6**. Same file, line 82 (manifestations). Claim: "...the Registry texts dated inside the gap that this world names (Optatus of Milevis, rows 27, 64 and 264, and the appendix documents, row 265) are drawn on for no claim". Source shows: the Registry texts dated inside the gap also include the council canons (rows 26, 59, 202: Gratus c. 345-348, Genethlius 390), Augustine's pre-ordination writings (rows 11, 22, 25) and pre-391 Theodosian constitutions (rows 44, 88). All of these are licensed for other claims (Doc_02 §7). The Optatus sermon (item 1) is unassessed. As worded, the list reads as complete. Severity **P1** (overstated by omission). Proposed wording: "...the Registry texts dated inside the gap include Optatus of Milevis (rows 27, 64, 264) and the appendix documents (row 265), drawn on for no claim; the council canons, Augustine's pre-ordination writings and pre-391 Theodosian constitutions also dated there are licensed for other claims (Doc_02 §7), and the nine Guelferbytanus tractatus, one of which Morin gives to Optatus, are unassessed (row 229)".
- **cf8ec194**. File `lpc.limit.the-silent-century.md`, line 35. Claim: "From them to 391, no source supplies a bishop's ordinary pastoral or congregational voice, or a congregation's voice, that continues Cyprian's." Source shows: same as 64c5c68e. Doc_05 line 27 and Doc_02 §7 both carry the scope "in the Registry", and this record drops it. Severity **P1**. Proposed wording: "From them to 391, no source in our Registry supplies a bishop's ordinary pastoral or congregational voice, or a congregation's voice, that continues Cyprian's; a sermon a later manuscript gives to Optatus of Milevis is held but not yet assessed or dated (row 229)."
- **31bdac99**. Same file, line 42. Claim: "This world's congregational record is silent across it.'" Source shows: the quotation is verbatim from `Build/worlds/lpc/Representative/lpc_Rep_Phase1_Ecology_Assessment.md` line 82. The underlying claim has the same scope issue as cf8ec194. Severity **P2** (the quotation is exact; the sentence it supports needs the Registry scope). Proposed wording: keep the quotation, and state the scope in the record's own sentence around it: "...silent across it,' within the Registry's assessed sources (the Guelferbytanus tractatus, row 229, are unassessed)."

## Group B: the conciliar-authority "ecological bound" (fe19b3f1, 83e3ecd6, a40a3d7f, 6ba65352, f80a4c45, 59fc6359)

Shared evidence. Doc_04 line 92 scopes its finding to "no evidence **in Doc_02**". The records and chunks state it as a fact about the world. At source it is contradicted twice:

1. **256, Cyprian's phase.** The preface in which Cyprian speaks the "bishop of bishops" formula was delivered with "presbyteris et diaconibus, praesentibus etiam plebis maxima parte" present (`cic/texts/cyprian_sententiae-episcoporum-lat_hartel1868-csel3-tei.txt`, lines 107-109). The ANF translation reads "the presbyters and deacons, and a considerable part of the congregation who were also present" (`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`, lines 56852-56855, with the formula at line 56872). Ordinary believers and local clergy heard the question put.
2. **393, Augustine's phase.** The Psalmus contra partem Donati is in `cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`, from line 1296, and its title is in Registry row 214. The Retractationes (`cic/texts/augustine_retractationes-lat_knoll-csel36.txt`, lines 6833-6834) says it was written for "ipsius humillimi uulgi et omnino inperitorum atque idiotarum notitiam". It argues the conciliar principle directly to the people: "uel uos iam, populi, audite ... si modo episcopi uestri ex una aliqua regione haberent inter se litem, quos uelletis iudicare nisi alterarum regionum ..." (lines 1611-1616), and "proferantur nobis gesta, quae in concilio solent esse" (line 1476). That is a popular teaching song carrying the question into ordinary formation.

A search of Augustine's Latin sermons, Enarrationes, Guelferbytani, Caillau and the John tractates for "plenari-" found no use of "plenary council" in his preaching. So the narrower claim, that the technical formula "plenary Council" is not evidenced in ordinary preaching, would hold.

- **fe19b3f1**. File `lpc.gravity.conciliar-authority-theory.md`, line 68. Claim: "There is no evidence that ordinary believers, catechumens, or most clergy in either phase were shaped by this question, or even knew of it." Source shows: items 1 and 2. The "even knew of it" limb is contradicted by the text that carries the formula. Severity **P0**. Proposed wording: "Beyond the presbyters, deacons and 'greatest part of the people' recorded as present when Cyprian spoke in 256, and Augustine's popular Psalm against the Donatists, which argues the point to ordinary people, there is no evidence that this question shaped ordinary believers, catechumens, or most clergy in either phase."
- **83e3ecd6**. File `lpc.term.bishop-of-bishops.md`, line 69. Claim: "Doc04 finds no evidence this question reached ordinary believers, catechumens, or most clergy in either phase -- the formula is real and Documented; its reach into ordinary life is not evidenced." Source shows: it reports Doc_04 accurately, apart from dropping "in Doc_02", but the reported finding is contradicted (item 1: the formula was spoken before the congregation). Severity **P1**. Proposed wording: "The formula was spoken before presbyters, deacons and most of the congregation of Carthage in 256; beyond that one hearing, its reach into ordinary formation is not evidenced."
- **a40a3d7f**. Same file, line 79. Claim: "Re-derived from Doc06 SS2.2 (lpclex012, down-tiered to Tier 2 -- 'no evidence that ordinary believers..." Source shows: the quotation matches Doc_06 §2.2, line 61. The bound it carries is contradicted (items 1 and 2). Severity **P2** (provenance note accurate; it propagates the overstated bound). Proposed wording: keep the provenance, and quote the corrected bound once Doc_06 §2.2 is corrected.
- **6ba65352**. File `lpclex012_bishop-of-bishops.md`, line 59. Claim: "Ecological bound, stated plainly. Doc04 finds no evidence that ordinary believers, catechumens, or most clergy in either phase were formed by, or aware of, this question." Source shows: the "aware of" limb is contradicted by the 256 preface itself, the very locus the chunk cites (item 1). Severity **P0**. Proposed wording: "Ecological bound, stated plainly. The formula was spoken before the presbyters, deacons and most of the people of Carthage in 256; there is no evidence that it formed ordinary believers, catechumens, or most clergy beyond that hearing."
- **f80a4c45**. File `lpc.term.plenary-council.md`, line 69 (a near-copy is at line 32). Claim: "The same ecological bound as that paired entry applies: no evidence this question reached ordinary formation in either phase." Source shows: items 1 and 2. The Psalmus carries the conciliar-judgement question into ordinary formation in Augustine's phase. Only the technical phrase "plenary Council" is absent from his preaching. Severity **P1**. Proposed wording: "The phrase 'plenary Council' does not appear in Augustine's preaching to his congregation; the wider question of who judges a bishop was put to ordinary people in his Psalm against the Donatists (393), but not as this formula."
- **59fc6359**. File `lpclex013_plenary-council.md`, line 59. Claim: "Ecological bound, as for the paired entry: no evidence that this question reached ordinary formation in either phase." Source shows: same as f80a4c45. Severity **P1**. Proposed wording: as for f80a4c45.

## Other findings

- **77d40657**. File `lpc.gravity.grace-and-human-incapacity.md`, line 61. Claim: "So it does not span the whole world: no evidence for it has been found in Cyprian's phase." The record adds: "This is a real boundary in time, not a gap in the search." Source shows: Cyprian states the theme in this world's vendored texts. Ad Donatum 4: "Dei est, inquam, Dei omne, quod possumus" (`cic/texts/cyprian_ad-donatum-lat_hartel1868-csel3-tei.txt`, line 256, div n=4). Ad Quirinum III.4 heading: "In nullo gloriandum, quando nostrum nihil sit" (`cic/texts/cyprian_testimoniorum-libri-tres-adversus-judaeos-lat_hartel1868-csel3-tei.txt`, line 3300). Augustine himself cites that heading repeatedly against the Pelagians as Cyprian's witness to grace (`cic/texts/npnf105_augustine-anti-pelagian-writings.xml`, lines 18089, 18102-18104, 20094, 20912, 20975, 22251-22257). Severity **P0** (wrong as a statement about the record). Proposed wording: "It organizes only Augustine's phase. Cyprian states the theme ('It is of God, I say, of God, all that we can do'; 'we must boast in nothing, since nothing is our own'), and Augustine cites him for it against the Pelagians, but in Cyprian's phase it drives no controversy and no body of work."

- **c7aafc6f**. File `lpc.figure.possidius.md`, line 42. Claim: "The sole source for the whole of Phase Two's one built story, and the source of lpc.quote.clamour-and-tears -- the mirror of Pontius's own role for Phase One, a friendly rather than hostile mediating eyewitness whose own presence in the room ... is what the Tier Justification for lpc.story.the-psalms-on-the-wall rests its Tier 1 finding on." Source shows: the story record lpc.story.the-psalms-on-the-wall cites a second source, lpc.source.prosper-epitoma-chronicon-mommsen1892, for the death's date and the siege. That source is Prosper at a. 430, `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`, lines 54206-54211. The story's own absent_detail says "The death itself is corroborated from outside Hippo". The rest of the sentence checks out. Phase Two has one built story, since six of the seven Story-Chunks are Cyprian's. Possidius is the source of the quote (Vita IV). The Tier Justification does rest on his presence. Severity **P1** (overstated). Proposed wording: "The main source for Phase Two's one built story, and its only witness to the sickroom (Prosper's chronicle corroborates only the date of death and the siege), and the source of lpc.quote.clamour-and-tears -- ..."

- **98c89607**. File `lpc.story.the-psalms-on-the-wall.md`, line 75. Claim: "Possidius is the only witness to the last weeks -- the psalms, the request, the ten days." Source shows: Prosper also witnesses Augustine's last days. He was "in ipso dierum suorum fine respondens" to Julian's books (lines 54208-54211). He gives nothing of the sickroom. Severity **P2** (wording). Proposed wording: "Possidius is the only witness to the sickroom in the last weeks -- the psalms, the request, the ten days; Prosper's chronicle says only that he was still answering Julian's books at the very end."

- **94dc0428**. File `lpc.limit.womens-own-voice.md`, line 37. Claim: "No text authored by a woman survives anywhere in this world's own Native corpus, in either phase." Source shows two things:
  1. Letters XXV and XXX in Augustine's general correspondence (Native, row 11) are headed "from Paulinus and Therasia" (`cic/texts/npnf101_augustine-confessions-letters.xml`, lines 24531, 24538, 25665, 25675). The Latin reads "PAVLINVS ET THERASIA PECCATORES" (`cic/texts/augustine_epistulae-1-123-lat_goldbacher-csel34.txt`, line 3976). They are jointly sent in a woman's name, though the voice is Paulinus's.
  2. In the Passio of Montanus and Lucius (Native, row 231), Quartillosa narrates her own vision in the first person: "Vidi, inquit, filium meum ..." (`cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt`, lines 5771-5783). This also bears on the same record's statement that women "never narrate" and "none of them is audible", which is outside this batch.

  Severity **P1** (overstated). Proposed wording: "No text written by a woman in her own name alone survives in this world's own Native corpus, in either phase. The nearest are two letters sent jointly in the names of Paulinus and his wife Therasia, whose voice is his, and one woman's vision, Quartillosa's, reported in her own words inside a martyr act written by men."

- **d730e7a3**. File `lpc.source.duval-loca-sanctorum-africae.md`, line 35 (the same text is in Registry row 60). Claim: "Licensed for rows 37 and 38 -- this Registry's entire material-evidence layer (CIL VIII, no inscription named; basilica archaeology, Confidence D, 'only the category' named); ..." Source shows: the Registry's Type column marks many more rows as material (M): 60 (Duval itself), 63 (Marec, Monuments chrétiens d'Hippone), 82 (Ennabli), 107 (Bir Ftouha), 108 (Bir el Knissia), 129 (Duval and Caillet, M/S), 136 (L'Année épigraphique), 146 (Duval, épigraphie) and 97 (Jensen, S/M). Rows 37 and 38 are not the entire material layer. Severity **P1** (false as it now reads; likely true when the row was added). Proposed wording: "Licensed for rows 37 and 38 -- CIL VIII, no inscription named, and basilica archaeology, Confidence D, 'only the category' named -- the two material rows it would most directly turn from category into evidence; ..."

- **8fdddf7d**. File `lpc.source.granfield-episcopal-elections-in-cyprian.md`, line 32 (the same text is in Registry row 113). Claim: "Licensed for row 1 directly -- the electoral mechanism behind Cyprian's own central citation, 'your suffrage and God's judgment,' which no other row addresses at this level; row 101 (Bobertz) addresses the wider patron-bishop dynamic, a related but distinct question." Source shows: Registry row 186 (Norton, Episcopal Elections 250-600) is "Licensed for row 1's own election language ('your suffrage and God's judgment')", with "clerical/lay participation as its own central subject". That is the same question, in a book-length study. Row 101 (Bobertz) is also licensed "for row 1's own election language". Severity **P1** (false as stated). Proposed wording: "Licensed for row 1 directly -- the electoral mechanism behind Cyprian's own central citation, 'your suffrage and God's judgment'; the article-length study focused on Cyprian alone, beside row 186 (Norton), which treats the same question across 250-600, and row 101 (Bobertz), which addresses the wider patron-bishop dynamic."

- **75d73052**. File `lpc.term.bishop-of-bishops.md`, line 79. Claim: "The chunk itself never uses the term; this script infers it because the formula is the sole textual ground of a real, Documented Supporting gravity (the conciliar-authority axis), which Doc04 SS7 item 2 forbids suppressing -- Tier and evidentiaryweight are independent axes, the same rule don's own script states." Source shows four things:
  1. "Never uses the term" holds: "load-bearing" has 0 hits in lpclex012 and lpclex013.
  2. "Sole textual ground" is false. The gravity rests on two formulas: its sources are lpc.source.cyprian-seventh-council-of-carthage and lpc.source.augustine-on-baptism-against-the-donatists, and Doc_04 §7 item 2 says "both formulas' existence is Documented".
  3. "Documented Supporting gravity" mislabels it. lpc.gravity.conciliar-authority-theory carries formation_confidence Inferential-Thin, and only the formulas' existence is Documented.
  4. The don script's rule (Build/worlds/don/scripts/wb_don_s21.py, lines 160-169) keeps citation_specificity and verification_state independent, not Tier and evidentiary_weight. It is an analogous principle, not the same rule.

  Severity **P1**. Proposed wording: "The chunk itself never uses the term; this script infers it because the formula is one of the two textual grounds (with Augustine's 'plenary Councils') of a real Supporting gravity whose formulas' existence is Documented (the conciliar-authority axis), which Doc_04 §7 item 2 forbids suppressing -- Tier and evidentiary_weight are independent axes, on the same principle don's script applies to citation_specificity and verification_state."

## Note on a VERIFIED row

6516f231 holds in the Registry's own sense of "licenses". But Audollent (row 241, vendored and in this world's corpus map) does print a conversion for this exact collection: "100.000 sesterces (environ 25.000 francs)" at `cic/texts/audollent_carthage-romaine-fra_1901.txt`, line 29034. The claim_guards entry "no source of ours licenses one" is true. It would be clearer if it said that an unlicensed 1901 figure exists and is not to be used.
