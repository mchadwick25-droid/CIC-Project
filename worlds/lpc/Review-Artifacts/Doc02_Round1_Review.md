# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review

**Documents reviewed:**
- `worlds/lpc/Doc_02_Source_Ecology.md` (DRAFT, first pass, 2026-09-01)
- `worlds/lpc/Source_Registry.md` (DRAFT, first pass, 2026-09-01)
- `worlds/lpc/Source_Acquisition_Manifest.md` (2026-09-01)

**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread. Did not draft any of the three documents, did not draft this world's Step 0 or Doc_01, and did not write any of the Step 0 or Doc_01 review rounds. **Doc_01's own nine review rounds were treated as claims to be re-derived, not as authority** — the drafts repeatedly rest a Registry Confidence letter on "re-verified across Doc_01's nine review rounds," and that sentence is precisely the kind of inherited certification this review exists to test. Every quotation named below was re-located in the vendored XML this session, with the containing `div3` recomputed by walking the markup rather than accepted from the citation. The corpus map was read whole and parsed programmatically, not read through the drafts' paraphrase of it.

**Governed by:** `cic-build-cycle` (CO-022), read in full at the live skill this session — *Where you are in the cycle*, *Draft*, *Review*, *Revision decision*, *Escalation categories*, *Naming and term propagation*, *Disposition*, *Cross-document fact consistency*; `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part II (Evidence Development) and Part VII Step 2, both extracted from the `.docx` this session; `Source_Registry_Template.md` V1.0; `CiC_L3A_Forces_Framework_V1.1.docx` Section 4 (Step 2 entry), extracted this session; `Doc_01_World_Identification_Boundaries_Orientation.md` (Approved to proceed, 2026-09-01) including its §8 binding open items and §9 disposition; `cic/corpus-map/latin-pastoral-congregational-christianity.yaml`; `cic/texts/README.md`.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 6 HIGH · 15 MEDIUM · 10 LOW · 4 COSMETIC.**

**Four things should be said before the findings.**

**First: there is no fabrication here.** Every one of the seven secondary works at §3 is real, correctly attributed, and correctly dated — including the three (Burns & Jensen, Fahey, Rebillard) the draft itself flagged as recalled from field knowledge without a check. Rebillard's row even names both translators correctly. The archive.org item named at Manifest G1 is a genuine item, correctly described, and the network block the Manifest discloses is real — `archive.org` returned `EGRESS_BLOCKED` from this review environment too, and `cic/texts/README.md` does say in terms that "the sandbox this project's agents run in blocks every patristic text host." On the axis this project treats most seriously, these documents are clean, and the draft's habit of under-claiming its own verification rather than over-claiming it is the right direction.

**Second: the verification the drafts inherited from Doc_01 was not re-checked, and it does not all hold.** The drafts say, in five separate rows and twice in Doc_02's narrative, that a quotation was "directly re-verified" or "re-verified across Doc_01's nine review rounds." I spot-checked six such quotations at source. Five are exact and correctly placed. The sixth — Cyprian's "your suffrage and God's judgment," cited as **Ep. XL** in Doc_02 §1 and in Registry row 1 — is in **Epistle XXXIX**. ANF05's Epistle XL is "To Cornelius, on His Refusal to Receive Novatian's Ordination" and contains no such phrase. The error entered at Doc_01's own Round 9 and was certified there; Doc_02 imported it and attached a fresh verification claim to it. This is exactly the failure mode the review brief anticipated, and it now sits live in an Approved-to-proceed document (H1, and the escalation note below).

**Third: the corpus map was represented rather than read.** Four separate numeric or characterizing claims about `latin-pastoral-congregational-christianity.yaml` are contradicted by the file. The most consequential is Optatus: Doc_02 §1 says the corpus map homes him "on the sibling Donatism build rather than this one, per the corpus map's own note." The corpus map homes him **here**, provisionally, and `donatism.yaml` does not contain him at all — and the Registry's own row 27 quotes the note correctly, so the two companion documents contradict each other on the same sentence (H2). Two of Doc_01 §8 item 2's three binding sub-items — the Optatus placement and the duplicated Council-of-Carthage-under-Cyprian rows — are undischarged, and the second is not disclosed anywhere (H4).

**Fourth: §6's Article 20 discharge is falsified by the corpus its own Registry licenses.** §6 states that no lay believer's letter, no woman's voice, and no non-episcopal clergyman's extended first-person account "survives anywhere in this world's own vendored corpus." Pontius, a deacon, is the third of those and is the subject of §1, §2 and §4 of the same document. Epistles XX and XXI are letters between Celerinus and Lucian, two lay confessors, in their own words. And row 11's own licensed body — the 138 general letters — contains at least six named women addressees, including Albina (Letter CXXVI, a.d. 411, Augustine's own narrative of the riot in his basilica over Pinianus) and the nuns of Hippo (Letter CCXI, a.d. 423, the revolt in the convent his own sister had led). These were one grep away (H6).

---

## Method — what was actually checked

- **The live `cic-build-cycle` skill read in full** this session, including all four escalation categories verbatim, the *Revision decision* substantial/cosmetic test, the *Cross-document fact consistency* section, and the *Naming and term propagation* rule.
- **CF V7.4 extracted from the `.docx` this session** and read whole for Part II (Source Ecology Development, Author Gravity, Source Asymmetry, Missing Voices, Affirmative Duty, Confidence Calibration, Secondary Scholarship, Formation Narrative Sources, Material Culture, Story tiers, Story Inventory Requirement, Expanded Author Gravity) and for the Part VII Step 2 entry whole, including both activity lists, the search_record rule, the field-bibliography sweep, the saturation statement, the checkpoint rule, and the Doc_02 review requirement. `Source_Registry_Template.md` read whole. Forces Framework V1.1 §4 Step 2 entry extracted and read.
- **The corpus map parsed, not paraphrased.** `latin-pastoral-congregational-christianity.yaml` loaded with a YAML parser: 73 works, 65 `assigned` / 8 `provisional`, counted by author (51 Augustine, 15 Cyprian, 1 each Pontius / Optatus / Scillitan / two councils / two anonymous) and by `source_file`. Every one of the 73 mapped by hand against the 41 Registry rows to find omissions and double-registrations. `donatism.yaml` parsed for Optatus and the two councils. `cic/corpus-map/_staging/npnf101_augustine-confessions-letters.yaml` read for the four-part letter split.
- **The vendored primary corpus, read directly, with loci recomputed.** `anf05` — every occurrence of "suffrage" and "ancient venom" printed with the containing `div3` recomputed by scanning the file's `div3` boundaries; Epistle XL's own heading and opening read; the Seventh Council proœmium and preface read in full including the `a.d. 258` heading; Pontius's *Life* §§4–5 read with the section markers located; Epistles XX and XXI read; the whole Pontius *Life* swept for "Curubis," "ordain," "deacon," "presbyter." `npnf101` — Letters XXXI and CCXIII read with the containing `div3` and the numbered section marker located; all 168 `type="Letter"` `div3`s counted and their `shorttitle`/`title` attributes swept for named women. `npnf104` — Letter 185 chapter 7 §§23–31 printed whole; every occurrence of "plenary Council" and "brought to light" located. `anf09` — the Scillitan Martyrs' own introduction read. ANF05's own introductory notice to Cyprian read for the base Latin text and translator.
- **WebSearch verification of all seven secondary works** at §3 / rows 30–36, plus Hartel/CSEL 3, Harnack 1913, and Pellegrino, against publisher records, journal reviews, and library catalogue results.
- **The sibling Donatism branch fetched** (`origin/claude/record-native-world-build-v2-e2s0dt`, head `92bc4c38`) and its Registry rows 1, 4, 24, 27, 28, 48 and Manifest G1–G7 read directly to check every cross-reference the drafts make to it.
- **A live egress test** of the archive.org item named at G1, and `cic/texts/README.md` read for both the rights rule and the sandbox claim the Manifest quotes.
- **Doc_01 read at §2, §5, §6, §7, §8 (all twelve items) and §9**, plus `Doc01_Round9_Review.md`, to test every "Doc_01 establishes / re-verified / discharges" claim in the drafts against Doc_01's own words.
- **CO-022's four escalation categories run independently** against all three documents.
- **The two reviewer-side coverage checks CF V7.4 requires** — the ten-item relative-recall test and the PRESS question — run and recorded below.

---

## HIGH

### H1. The Ep. XL quotation is Epistle XXXIX — a misattributed direct quotation carrying a false verification claim
`Doc_02_Source_Ecology.md` line 15; `Source_Registry.md` line 12 (row 1, Licensed For and Verification Note).

Doc_02 §1: *"Doc_01's own nine review rounds directly re-verified this corpus's own account of Cyprian's election (Ep. XL, 'your suffrage and God's judgment,' against the 'ancient venom' of a rival faction)."* Registry row 1 licenses *"Cyprian's own election (Ep. XL, 'your suffrage and God's judgment')"* and its Verification Note states *"Ep. XL directly verified against `anf05` in Doc_01's own Round 9 review."*

Checked at source. Both phrases occur once each in the whole volume, at `anf05` lines 32372–32373, inside `<div3 id="iv.iv.xxxix" n="XXXIX" ... title="To the People, Concerning Five Schismatic Presbyters of the Faction of Felicissimus.">` — **Epistle XXXIX** (its own heading: "Oxford ed.: Ep. xliii. a.d. 251"). The next `div3` (`iv.iv.xl`, Epistle XL, "Oxford ed.: Ep. xliv") does not begin until line 32578, and its subject is Cornelius's refusal to receive Novatian's ordination. Neither "suffrage" nor "venom" occurs anywhere in it. There is no numbering scheme under which this passage is "XL": the vendored text follows Migne's order with the Oxford number appended in a note, and both numbers for this letter are XXXIX / xliii.

The verification claim is therefore false in the strongest sense the project cares about: not merely unchecked, but asserted as checked and wrong. It was inherited. `Doc01_Round9_Review.md`'s own method note lists "Ep. XXXIX's five presbyters; **Ep. XL's** 'your suffrage and God's judgment'" as two separate checks — they are the same letter, and Round 9 certified the wrong label. Doc_01 §5 (live text) and §9 (log, twice) now carry it.

**Required:** correct to Ep. XXXIX in Doc_02 §1 and Registry row 1, and rewrite row 1's Verification Note to record what was actually re-located this session rather than what Round 9 claimed. Then propagate — see the escalation note at the end of this review; the fix is not complete while the same error stands in an Approved-to-proceed Doc_01.

### H2. Optatus: the corpus map says the opposite of what Doc_02 §1 says it says
`Doc_02_Source_Ecology.md` line 23; `Source_Registry.md` line 38 (row 27).

Doc_02 §1: *"Optatus of Milevis's *Against the Donatists* (Registry row 27) is provisionally homed on the sibling Donatism build rather than this one, per the corpus map's own note."*

The corpus map's own note, in full: *"Optatus, Bishop of Milevis... Tradition for the Catholic side of the schism; **this entry** (Carthage / Hippo Regius, c. 240s-430) **is the census's home for that tradition.** Provisional only because the entry choice is inferred from region and date — Mark may prefer another Latin home for a Numidian polemicist."* Optatus is homed **here**. I also parsed `donatism.yaml`: it contains the 419 canons and both Council-of-Carthage-under-Cyprian entries, and **no Optatus entry at all**. So both limbs of the Doc_02 sentence are false, and the corpus map is cited for the reverse of what it says.

Registry row 27 quotes the note correctly and marks Optatus **Native** — so the Registry and its companion contradict each other on the same source in the same pass. Compounding it: Doc_02 §1 files Optatus under a heading that reads *"Adjacent, non-Native or partially-Native material"* while its own row calls him Native (see L2).

This is not a stray sentence. Doc_01 §8 item 2 hands Doc_02 *"the Optatus placement question (re-home, hold, or double-place)"* as a binding open item, and says *"Doc_02 inherits only its Optatus consequence."* The draft neither answers it nor carries it forward at §9 — it dismisses it on a misreading. **Required:** correct §1; state a position on the corpus map's own open question (hold here, re-home, or double-place) on this world's own ecological evidence, or carry it to §9 as an unresolved item and assess it under CO-022 category 2.

### H3. Checkpoint-rule violations — sources named in support of specific claims with no Registry row, and one row whose Licensed-For does not carry the claim made on it
`Doc_02_Source_Ecology.md` lines 15, 17, 78; `Source_Registry.md` lines 6, 14 (row 3), 22 (row 11).

CF V7.4 and the Template state the rule identically: *"Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row. If a claim in Doc_02 cannot be traced to a Registry entry, Step 2 is not finished."* The Registry's own line 6 asserts the rule is satisfied: *"Every source named in `Doc_02_Source_Ecology.md` in support of a specific claim has a corresponding row below."* It is not.

**(a) Letter XCIII §17.** Doc_02 §1 rests one of the three phases of its state-power account on it: *"an early opinion against any coercion (Letter XCIII §17)."* No row covers it. Worse, row 11 affirmatively excludes it: it covers *"the general correspondence (138 letters... **excluding** the Jerome cluster and the Donatist/Maximianist letters registered on the sibling Donatism build)."* The staging file confirms Letter XCIII to Vincentius is in the Donatist sub-corpus, assigned to `donatism` with `role: context`, and carries 31 of that cut's own keyword hits on its own — it is the largest letter in that part. So the drafts rely evidentially on a letter their own Registry has placed outside this world.

**(b) *Codex Theodosianus*.** Doc_02 §5 names it as a real acquisition candidate that *"would bear on this world's own Augustine-phase state-coercion material (§1 above, Registry row 12) if consulted."* That is a specific claim about a specific named source. No LPC row exists for it. (The sibling build rows it at its own row 16 and requests it at G3 — correctly checked, see the clean list — but that is another world's row, not this one's.)

**(c) *On the Unity of the Church* licensed for a claim its own row does not carry — and the claim reinstates a corrected Doc_01 error.** Doc_02 §1: *"*On the Unity of the Church* and the acts of the *Seventh Council of Carthage* (256, on rebaptism; Registry rows 3–4) carry Cyprian's own egalitarian, non-coercive conciliar-authority theory — 'no bishop sets himself up as a bishop of bishops...'"* Row 3's Licensed For is *"The classic treatise on schism and the one episcopate"* — not the conciliar-authority theory, and not the quoted preface, which is row 4's alone. The Registry checkpoint is not "a row exists"; it is that the row's Licensed-For supports the claim. It does not.

This one matters beyond bookkeeping. Doc_01's own Round 2 review found and corrected precisely this: an earlier Doc_01 draft cited *De Unitate* 5 for Cyprian's anti-Stephen position, and Doc_01 §7 now records that *"it is not"* — the treatise predates the Stephen controversy by four to five years, and the passage additionally survives in two recensions, one of which reads more favourably to Roman primacy. Row 3's own Verification Note recites that history and says the correction is *"not repeated in error here."* Doc_02 §1 repeats it.

**Also unrowed, and named in support of claims:** the sibling Donatism build's own Registry (Doc_02 §2, for the claim that the Donatists independently claimed Cyprian as third-century precedent — a substantive historical claim, and one this world's *own* corpus map states directly at its npnf214 entry, which would have been a rowed source); the sibling build's own Author Gravity work (§2); the sibling build's Manifest G3 (§5); `Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` §6 (§6); Frend's *The Donatist Church* (§3, in a claim about that work's subject); `cic/corpus-map/tertullian-s-voice.yaml` (row 29). Whether the rule reaches internal project artifacts is arguable and should be argued rather than assumed; *Codex Theodosianus*, Letter XCIII and Frend are not arguable — they are sources.

### H4. The duplicated Council-of-Carthage-under-Cyprian corpus-map rows — a binding Doc_01 open item, undischarged and undisclosed
`Source_Registry.md` line 15 (row 4); `Doc_02_Source_Ecology.md` line 15.

Doc_01 §8 item 2 names three things Doc_02 inherits: *"The Optatus placement question...; **the duplicated Council-of-Carthage-under-Cyprian corpus-map rows**; the Article 23 reconstruction of Donatism as this world's own internal rival."* The second is real: this world's corpus map carries the same council twice —

- *The Seventh Council of Carthage under Cyprian*, `author: cyprian`, `source_file: anf05`, **`confidence: assigned`**;
- *The Acts of the Council of Carthage under Cyprian (256, on baptism)*, `author: council-of-carthage-under-cyprian`, `source_file: npnf214_seven-ecumenical-councils.xml`, **`confidence: provisional`**, with the note *"Donatism is included as shared ancestry rather than heresiology: the Donatists claimed this council's baptismal doctrine as their patrimony... **Provisional on that double placement.**"*

Registry row 4 reports only the first, states *"Corpus map `role: tradition`, `confidence: assigned`"* flatly, and neither of the drafts mentions the second entry, its `provisional` marker, or the double-placement question that marker exists to hold open. Doc_02 §9's carry-forward list does not name it. The one place the drafts do state the Donatist-precedent claim (§2, Cyprian's Transmission History) sources it to *the sibling build's* Registry rather than to this world's own corpus-map note that says it — which is how a suppressed row produces an unrowed citation.

**Required:** disclose the duplication, row the npnf214 entry (or state explicitly why row 4 subsumes it), carry its `provisional` marker, and either resolve or carry forward the double-placement question Doc_01 handed to this step.

### H5. Hartel's CSEL 3 is not the edition underlying the vendored ANF05 translation — the stated rationale for the world's flagship acquisition request is false, and the editor is misnamed
`Source_Registry.md` line 50 (row 39); `Source_Acquisition_Manifest.md` line 17 (G1).

Both say: *"Karl von Hartel (ed.), *S. Thasci Caecili Cypriani opera omnia*, CSEL 3.1–3.3 (Vienna: Gerold, 1868–1871)... **This is the critical Latin edition underlying the already-vendored ANF05 English translation** of Cyprian's *Epistles* and treatises (Registry row 1)."*

The vendored file says otherwise, in its own introductory notice to Cyprian: *"For the sake of uniformity, it has been thought well to adhere to the arrangement of **Migne**, in the order of the Epistles as well as in their divisions. For the convenience of reference, however, the number of each Epistle in the Oxford edition is appended in a note. For a similar reason, **the general form of Migne's text has been used in the following translation**."* The translator is named on the same page: *"[Translated by the Rev. Ernest Wallis, Ph.D.]"* The chronology confirms it independently — the ANCL Cyprian appeared 1868–69, while CSEL 3.2 (the *Epistulae*) was not published until 1871.

So G1's value proposition is real (a critical apparatus this corpus lacks) but its stated *rationale* is not: acquiring Hartel would not put the vendored translation's own base text into the library; it would put a different, later edition beside it. That is a materially different request, and it is the only substantive request this world's Manifest makes. The evidence contradicting it was inside the file the Registry rows at row 1.

Separately, **the editor is Wilhelm (Guilelmus) August von Hartel**, not Karl — confirmed against the CSEL series record and the HathiTrust catalogue entry. Title, series, volume structure (3.1 treatises 1868; 3.2 *Epistulae* 1871; 3.3 spuria and indices 1871), city and date are all correct; the forename is not.

### H6. Article 20 — three of §6's blanket negatives are falsified by the vendored corpus the Registry itself licenses
`Doc_02_Source_Ecology.md` lines 86–87.

§6: *"No ordinary lay believer's own letter, no woman's own voice, and no non-episcopal clergy member's own extended first-person account survives anywhere in this world's own vendored corpus."*

**(a) The non-episcopal clergyman is Pontius**, a deacon, whose *extended first-person account* is Registry row 7 at Confidence A and the whole subject of §4 — and whom the sentence immediately preceding this one in §6 names by office. The document contradicts itself across two adjacent sentences.

**(b) The lay letters are Epistles XX and XXI.** *"Celerinus to Lucian"* and *"Lucian Replies to Celerinus"* — two confessors, writing in the first person, in their own voices, about the reconciliation of Celerinus's lapsed sisters at Rome. Neither was ordained at the time of writing (Cyprian ordains Celerinus reader afterwards, Ep. XXXIII). They sit inside row 1, whose Licensed-For already covers "the lapsed controversy," and the corpus map's own note flags them: *"the corpus embeds letters by others (Cornelius, the Roman clergy, Firmilian of Caesarea, **the confessors**) under Cyprian's name."*

**(c) The women are in row 11's own licensed body.** Sweeping the 168 `type="Letter"` `div3` titles in `npnf101` returns eleven letters addressed to or about named women. At least two carry real narrative weight inside this world's own congregational life, in-boundary:

- **Letter CXXVI, To Albina (a.d. 411).** Augustine's own first-person account of the riot in his basilica at Hippo when the congregation demanded Pinianus's ordination — written to answer Albina's charge that Pinianus was coerced under threat of death. A named woman as the accusing counterparty in the single best-documented congregational disturbance of Augustine's episcopate. This is comparable in kind to the sibling build's Lucilla finding, and the draft's own benchmark sentence invokes Lucilla by name.
- **Letter CCXI, To the Nuns (a.d. 423).** The revolt in the women's monastery at Hippo where Augustine's own sister had been prioress — the letter that transmits the Augustinian Rule. An entire women's community as the subject, in-boundary, in this world's own see.
- Also: Letter CCX (Felicitas), Letters CXXX–CXXXI and CL (Proba), CLXXXVIII (Juliana), XCII and XCIX (Italica), CCLXIII (Sapida), CXXIV (Albina, Pinianus and Melania).

§6's own supporting parenthetical makes the gap visible: it says *"Augustine's own correspondence includes several women by name"* and then offers exactly one example — Monica — which it immediately discounts as out-of-boundary. An affirmative duty discharged by asserting the existence of evidence one has not looked for, and then illustrating it with the one instance that does not count, is not discharged.

The draft's hedge (*"stated as a genuine gap in this pass's own research, not as a claim that no such material exists"*) covers the *gender* bullet only, and does not cover the three unhedged blanket negatives in the bullet above it. **Required:** withdraw the three negatives; assess Letters CXXVI and CCXI directly; state whether Albina meets this world's own load-bearing threshold, and if not, say on what test. Note that this may also reopen §6's Affirmative-Duty secondary prong, which the draft declines "for want of a genuine trace to ground it."

---

## MEDIUM

### M1. Four numeric claims about the vendored corpus and the corpus map are wrong, and two of them disagree with each other across the companion documents
`Doc_02_Source_Ecology.md` lines 13, 17; `Source_Registry.md` lines 34 (row 23), 64.

- *"the corpus-map's **40-plus** Native entries"* (Doc_02 §1) — the file holds **73** works. "Native" is also the Registry's Boundary-Status vocabulary, not the corpus map's; the corpus map has no such field.
- *"the existing corpus-map census for this world (**60+ works**...)"* (Registry saturation statement) — closer, but a *different* count of the same census in the companion document written in the same pass. CO-022's *Cross-document fact consistency* rule is squarely on point.
- *"**~292 letters**, split by the corpus map into a 17-letter Jerome cluster... and a 138-letter general-correspondence body"* (Doc_02 §1) — the vendored volume contains exactly **168** letters (`grep -c 'type="Letter"'` on `npnf101` returns 168; the corpus map's own note says so twice: *"168 of them"*). 17 + 138 = 155, not 292. Where 292 comes from is not stated and no row supports it; it appears to be Augustine's full modern letter corpus, which is not what is vendored, not what the corpus map describes, and not what rows 10–11 register.
- *"Augustine's anti-Pelagian corpus (**nine treatises**, c. 412–429, grouped)"* (row 23) — the corpus map holds **thirteen** `npnf105` works for this world. I enumerated them.

### M2. Three of the corpus map's eight `provisional` markers are dropped
`Source_Registry.md` lines 34 (row 23), 36 (row 25), 15 (row 4).

Eight works carry `confidence: provisional`. Five are correctly disclosed (rows 5, 8 ×2, 27, 28). Three are not:

- **On the Soul and its Origin** — `provisional`; row 23 states the whole anti-Pelagian body is `confidence: assigned`. The corpus map's own note is directly relevant and is dropped with it: *"Not addressed to Pelagians... Victor was no Pelagian. The doubt is whether the pelagianism id should stand; latin-pastoral-congregational-christianity is not in doubt."*
- **Soliloquies** — `provisional`; row 25 states `confidence: assigned` for the whole group (see also M4).
- **Acts of the Council of Carthage under Cyprian** (npnf214) — `provisional`, unrowed entirely (H4).

The Registry's own confidence-calibration rule turns on faithful reporting of what the census says. Reporting `assigned` for a group containing a `provisional` member is not a rounding decision; it erases the doubt the marker exists to carry.

### M3. One work double-rowed at two confidences with contradictory licensing; one work with no row at all
`Source_Registry.md` lines 34 (row 23), 36 (row 25).

***On Nature and Grace*** appears in row 23 (Confidence **B**, licensed for *"The Pelagian controversy, 410s–420s; grace/sufficiency-test gravity candidate"*) **and** in row 25 (Confidence **C**, *"Not currently licensed for a specific claim"*). A Registry whose sole downstream function is to say what a source may be drawn on for cannot say two contradictory things about the same source. The append-only protocol makes this worse, not better: neither row can be deleted, so the correction has to be an explicit disposition note.

***Concerning Faith of Things Not Seen*** (`npnf103`, `assigned`, corpus-map note *"Short apologetic-catechetical piece for his congregation"*) has **no row**. It is the only one of the 73 with none. Given §1's catechetical-works cluster and rows 15–18, its natural home is row 18.

### M4. The Boundary Check was not run on *Soliloquies*
`Source_Registry.md` line 36 (row 25).

The Template calls the Boundary Check *"a binary gate, run on every entry."* *Soliloquies* was written 386–387 at Cassiciacum near Milan — before Augustine's baptism, before his return to Africa, and outside Doc_01's stated geography (Carthage and Hippo Regius, Latin-speaking Roman North Africa). The corpus map flags exactly this: *"a philosophical dialogue, not pastoral work from Hippo. **Held in Augustine's own entry for want of a better home**; the doubt worth a reviewer's eye is whether the Cassiciacum period should also touch ambrosian-milan-standalone."* Row 25 files it Native inside a ten-work group without comment. Whether the answer is Native (the author is this world's, the work reaches us through his corpus) or Excluded is arguable — that it was never asked is not.

### M5. Two disclosures Doc_01 won across review rounds are silently dropped, and the Registry re-presents both as source-verified
`Doc_02_Source_Ecology.md` lines 15, 17; `Source_Registry.md` lines 15 (row 4), 23 (row 12).

**(a) The council's date.** Doc_02 §1 and row 4 both state "256" flat. Doc_01 §4 discloses: *"the vendored ANF05 edition's own proœmium heading dates this council 258, following an older reckoning — the document follows modern scholarship's 256 throughout and flags the edition's own divergent date here rather than let a reader meet it unexplained."* I read the proœmium: *"Having Therefore Summoned Eighty-Seven Bishops from Africa, Numidia, and Mauritania, Who Assembled at Carthage in the Kalends of September, **a.d. 258**."* Row 4's Verification Note — which recites nine rounds of re-verification of this exact preface — is the natural and required home for that transmission fact, and omits it.

**(b) The 401 date.** Doc_02 §1: *"at the African council of 401 (Letter 185 §§25–26)."* Row 12 licenses *"the 401 African council's own narrower solicitation of state power (Letter 185 §§25–26)"* and states the passage was *"directly re-verified at source across Doc_01's Rounds 6–9, including the 401 council."* Letter 185 §25 does not date the council; it says only *"it was decreed in our council."* Doc_01 attributes the date correctly and pointedly: *"at a council of African [bishops] — **dated 401 by NPNF's own editorial footnote at Letter 185 §25, not by Augustine's own text, which does not date it**."* That attribution was a Round 7 finding (L2) that had to be re-propagated at Round 8 (L1) because it failed to reach a downstream site. Doc_02 loses it at the first hand-off.

Everything else about §§25–26 checks out exactly (see the clean list).

### M6. The council preface is paraphrased inside quotation marks, and diverges from Doc_01's own verbatim rendering of the same passage
`Doc_02_Source_Ecology.md` line 15; `Source_Registry.md` line 15 (row 4).

Both render it *"no bishop sets himself up as a bishop of bishops... every bishop has his own proper right of judgment."* The text reads: *"For neither does **any of us** set himself up as a bishop of bishops, nor by tyrannical terror does any compel his colleague to the necessity of obedience; since every bishop, **according to the allowance of his liberty and power,** has his own proper right of judgment."*

Two problems. The first clause is not a quotation — it is a gloss set in quotation marks, and it changes the sense in a way that matters to this world's own finding: Cyprian's "any of us" is a first-person-plural statement by a presiding bishop about his own college, which is what makes it non-coercive; "no bishop" is a general proposition. The second has an unmarked internal elision. Doc_01 quotes the passage verbatim, twice, at §4 and §7 — so the companion documents now carry two different renderings of the load-bearing quotation in this world's build.

### M7. Transmission History is answered institutionally, not as a transmission chain — the specific facts were in the vendored files
`Doc_02_Source_Ecology.md` lines 34, 41, 48.

CF V7.4 Part II: *"how did their work reach us? Through what translators, copyists, or editorial hands? Did those intermediaries have theological agendas that shaped the transmission? Where a significant body of work survives only in translation... this must be named and its effect on confidence calibration assessed."* Forces Framework §4 makes it mandatory at Step 2.

All three entries answer a different question — which side of history preserved the author. Not one names a translator, an editor, a recension, or a manuscript fact, though the material was to hand and is directly consequential:

- ANF05 names its translator (Ernest Wallis) and states its base Latin text (Migne, with Oxford numbers in notes) in its own introductory notice — the very facts that make H1's numbering error possible and that determine what Manifest G1 would actually add (H5).
- *De Unitate* 4–5 survives in two recensions, one the "Primacy Text" — Doc_01 §7 names this and sets it aside only because it withdrew the citation resting on it. Row 3 licenses *De Unitate* at Confidence **A** and does not carry the recension fact.
- Pontius's entry substitutes this project's own file layout for transmission history: *"Preserved and vendored inside the same ANF05 volume as Cyprian's own corpus."* Where a text sits in `cic/texts/` is not its transmission history.
- Augustine's says *"Preserved through the Catholic institutional tradition's own manuscript transmission"* — true, and not specific enough to affect any confidence calibration, which is what the dimension is for.

Cyprian's entry is the strongest of the three (the two-sided later reception is a genuine transmission observation), and the corpus map's whole-body-attribution note is correctly carried at *Limitations*. The dimension is present; it is not yet doing its work.

### M8. An unsourced biographical claim about Pontius
`Doc_02_Source_Ecology.md` line 66.

§4: *"written by a deacon with every personal and institutional reason to idealize **the bishop who ordained him**."* The *Life* does not say Cyprian ordained Pontius. I swept the whole work for "ordain," "deacon," "presbyter" and "Curubis": Pontius identifies himself only as one of Cyprian's *"household companions"* chosen to share the exile, and the ANF heading gives his office. Nothing in the vendored corpus attests the ordination, no row supports it, and §2's parallel sentence gets it right without the clause (*"every institutional and personal reason to idealize his bishop"*). Delete the clause or ground it.

### M9. Doc_01 §8 item 5's binding is not discharged where Doc_01 said it must be
`Doc_02_Source_Ecology.md` §2 (lines 29–34); §9 (lines 110–117).

Doc_01 §8 item 5: *"**Doc_02's own Author Gravity work for Cyprian** should name Tertullian as a real, non-Native influence-source (Excluded / Named Comparandum), **and log the disclosure** rather than let it pass silently a second time."*

Registry row 29 is a good Named Comparandum entry and the §1 treatment is substantive. But §2's Cyprian Author Gravity entry — the location the binding names — does not mention Tertullian in any of its five dimensions, and §9's carry-forward list does not log the disclosure. Doc_01 wrote "a second time" for a reason: the item is on record because it had already passed silently once. Placement here is the substance of the requirement, not a formality: Tertullian's relevance is precisely to Cyprian's *Representativeness* and *Influence* — four of the ten treatises grouped in row 5 are recorded by the corpus map as reworking, following, depending on, or compiling Tertullian (*On the Advantage of Patience*, *On the Dress of Virgins*, *On the Lord's Prayer*, *On the Vanity of Idols*), a fact row 5 does not carry either.

### M10. Liturgical evidence is never assessed
`Doc_02_Source_Ecology.md` §1, §5.

CF V7.4 Part II's Source Ecology Development names six evidence types to identify: *"primary voices, secondary voices, institutional evidence, **liturgical evidence**, material evidence, ordinary participant evidence."* The Registry Template's Type P definition names *"liturgical texts"* explicitly. The draft covers five of the six. Liturgical evidence appears only as a single negative in §5 (*"This world does not currently have a distinctive liturgical epigraphic marker of the kind the sibling Donatism build names for itself (*Deo laudes*)"*), which answers an epigraphic question, not the category.

The omission is substantive rather than formal for this world in particular. **Both** of its anchor crises are disputes about rites: the rebaptism controversy is about the administration of baptism, and the lapsed controversy is about the rite of penitential reconciliation. Both are treated throughout as doctrinal and conciliar matters only. The corpus holds *De Dominica Oratione* (row 5), *On Care to Be Had for the Dead* (row 25), the catechetical and creedal works preached to catechumens (rows 15–18), the 419 canons (row 26), and ~1.4 million words of preaching delivered inside the liturgy (rows 19–21). Doc_03 is instructed at §9 item 7 to draw its terms from "the lapsed/penitential vocabulary of *De Lapsis*" — vocabulary this step has not assessed as liturgical.

### M11. The field-bibliography sweep and the search_record are builder-side Step 2 requirements, and the disclosure of skipping them does not make the step complete
`Source_Registry.md` lines 60, 64; `Doc_02_Source_Ecology.md` lines 115, 123.

The drafts are honest about this, and correctly distinguish it from the reviewer-side checks (which §9 item 6 assigns correctly — see the clean list). But CF V7.4 puts both under **Registry activities**, not review:

- *"Keep a search_record as the discovery work proceeds... logged as searches happen — **never reconstructed afterward**."* The Discovery methodology note concedes: *"No `records/lpc/search_record/` was kept as searches happened during this build... it is dated to when each entry was written during this drafting pass."* That is the reconstruction the rule names.
- *"**Run a field-bibliography sweep before the Registry closes**: check the world's standard bibliographic instruments and reference works for load-bearing sources the ecology work has not yet surfaced, and disposition every find."* Not run. *"Close the Registry with a saturation statement... A Registry without a saturation statement is not complete."* Explicitly not closed.

The relative-recall test below measures the cost: **0/10**, on works drawn from standard reference instruments independent of this build. That is not a procedural gap. The bibliography as it stands is seven secondary works for a world anchored on two of the most heavily studied figures in Latin patristics, and it holds no critical edition, no standard translation-with-commentary, no reference encyclopedia, and no monograph on Augustine's pastoral practice — the world's own named subject.

### M12. §2 asserts continuity on the one axis Doc_01 expressly holds open, and §8's Confidence Map omits it
`Doc_02_Source_Ecology.md` lines 32, 105.

§2, Cyprian's *Influence*: *"Foundational for this world's own ecclesiology of the one episcopate and its conciliar procedure on readmitting the lapsed — a formation pattern this document's own construction record finds **continues, argued with rather than against**, in Augustine's own later engagement with Cyprian's conciliar acts."*

Doc_01 §8 item 10 is a governing, unclosed item on precisely this: *"Cyprian's own egalitarian, non-coercive theory of inter-episcopal authority (256 Council preface) and Augustine's own hierarchical, correctable theory of conciliar authority (*On Baptism* II.3) are **real, substantial differences** this document argues do not clearly touch this world's own formation-relevant ground, **but does not consider fully settled**."* Doc_01 §5 is blunter still: Augustine argues Cyprian's ruling *"was **not** binding and was **wrong**."*

"Argued with rather than against" compresses Doc_01's careful "argues *with* Cyprian, **disputing his ruling** while claiming his communion" into its opposite reading, and drops the disputation that is the whole point. §8's Confidence Map lists two Contested items and does not list the conciliar-authority uncertainty, though Doc_01 marks it as the one preliminary reading most likely to be reopened at Doc_04.

### M13. Confidence A is assigned on the Registry's own rule where the rule is not met
`Source_Registry.md` lines 8, 12 (row 1), 14 (row 3), 18 (row 7).

The Registry's stated rule: **A** is used *"only where a row's **Licensed-For content** was itself directly read and verified against the vendored text this session (or... already independently verified in this world's own Doc_01)."*

- **Row 3** (*De Unitate*, A). Its Verification Note records that Doc_01 Round 2 checked the treatise and found an *earlier citation of it wrong*. Verifying that a citation was mistaken is not verifying the row's Licensed-For content (*"the classic treatise on schism and the one episcopate, written amid the Novatianist and Felicissimus crises"*), and no locus in *De Unitate* is named anywhere. Under the Registry's own definitions this is **B** at best, and the recension question (M7) argues for a Verification Note either way.
- **Row 1** (Epistles, A). Its Licensed-For names seven distinct subject areas; the one specifically-cited locus is misattributed (H1). A is not sustained on the row as written.
- **Row 7** (Pontius, A) is the borderline case: §5 was verified exactly, but the Licensed-For also covers *"Cyprian's own conversion,"* which is §§2–4 and was not. Narrow the Licensed-For or the note.

### M14. Row 11's account of the letter split is wrong
`Source_Registry.md` line 22.

Row 11 describes itself as *"the general correspondence (138 letters... excluding the Jerome cluster and **the Donatist/Maximianist letters registered on the sibling Donatism build**)."* The staging file's four-part partition of the 168 letters is: Jerome (17, to both this world and Hieronymian), **Donatist** (11, to `donatism`, `role: context`), **Pelagian** (2, to `pelagianism`, `role: context`), and general (138). There is no Maximianist part. The Pelagian letters are not on the Donatism build. The count is right; the account of what was subtracted is not — and it is the account that determines whether Letter XCIII is inside or outside this Registry (H3a).

### M15. Row 28 files an Out-of-Boundary exclusion and then writes it a Comparandum Note
`Source_Registry.md` line 39.

CF V7.4 and the Template are emphatic that the two reasons are not interchangeable: *"These are not the same finding and must not share an undifferentiated label: an Out-of-Boundary source was a simple miss; a Named Comparandum is a specific, identified temptation worth naming for exactly that reason."* Out-of-Boundary is defined as a source that *"was never a serious candidate for this world's own voice."*

Row 28 assigns Out-of-Boundary and then supplies a full temptation statement: *"A builder reaching for it to characterize Cyprian's own congregation directly... would be reaching outside this world's own evidentiary window."* If a builder is genuinely tempted to reach for the Scillitan Martyrs to characterize Cyprian's Carthage — and given the corpus map's own note (*"the direct root of the Carthaginian congregational tradition"*) that is a plausible temptation — the row is a Named Comparandum and should say so. If not, the note should go. Note that the exclusion's *substance* is sound and its date is confirmed at source (see the clean list); this is about which of two mutually exclusive labels it carries.

---

## LOW

**L1.** `Doc_02` line 23 — *"Doc_01 §2, §6, and §7 all independently establish that **Tertullian forged** the Latin theological vocabulary."* Doc_01 says, in all three places and in Step 0, *"credited with forging"* — a deliberately-carried attribution hedge, which Registry row 29 preserves correctly and Doc_02 drops. And §2 (line 35) and §6 (line 124) both cross-refer to §7 as their ground, so they are not three independent establishments; they are one, pointed to twice. The verbatim clause *"without Tertullian himself being this world's own voice"* occurs once, at §7 — row 29's *"repeated at §2, §6, and §7"* reads as though the phrase recurs.

**L2.** `Doc_02` line 23 — Optatus and Petilian are filed under a heading reading *"Adjacent, non-Native or partially-Native material"* while Registry rows 27 and 14 both mark them **Native**. The Template is explicit that Native does not mean exclusive; the heading imports a distinction the Boundary Check does not make.

**L3.** `Doc_02` line 17 — *"~695,000 words of Psalm exposition, **both preached** to his own congregations at Hippo and Carthage."* The corpus map and Registry row 20 both say *"preached **and dictated**"* and *"**most** delivered to congregations."* Doc_02 overstates against its own row.

**L4.** `Source_Registry.md` line 56 — the priority-flag section applies only the Template's re-keyed trigger (builder-prior-knowledge + not verified-direct + load-bearing) and never engages CF V7.4 Step 2's own wording, which is still in force in the governing framework: *"Flag entries resting at **Confidence C or below** that are intended to support a vivid, specific claim."* On that rule, **row 8** (C; licensed for *"The Novatianist rival consecration (Doc_01 §4); the pro-Roman side of the rebaptism controversy"*) and **row 40** (C; licensed for the existence and identity of two named critical editions, on a single uncorroborated search) would be flagged and are not. The two rules genuinely diverge and the Template itself explains why; the divergence should be disclosed and a rule chosen, not left implicit.

**L5.** `Doc_02` §9 (lines 110–117) omits the field-bibliography sweep from its own carry-forward list, though §10 (line 123) and the Registry's saturation statement both name it. §9 item 6 names only the recall test and PRESS.

**L6.** `Source_Registry.md` lines 37, 38 — rows 26 and 27 name no vendored file, though both texts are in the corpus (`npnf214_seven-ecumenical-councils.xml`; `optatus_against-the-donatists.txt`). Every other primary row that was checked names its file in the Discovery column. Row 26's silence is what lets H4's duplicate hide.

**L7.** `Source_Registry.md` line 15 — row 4 refers to *"the **bracketed** reciprocal clause 'can no more be judged by another than he himself can judge another.'"* That clause is Cyprian's own continuous text. The brackets in ANF05 at that point belong to the editorial gloss that *follows* it (*"[This, then is the primitive idea of the relations existing, mutually, among bishops as brethren.]"*). Calling Cyprian's own words "bracketed" invites a future reader to treat them as editorial supplement.

**L8.** `Source_Acquisition_Manifest.md` line 31 — *CIL* VIII is housed under the heading *"3. Consultation-only secondary scholarship (never vendored)"*. The sibling build treats it as an open, public-domain **acquisition request** (its own G7). The paragraph itself says it *"sits in a different category from the works above,"* which is right — so it should not sit under that heading.

**L9.** `Doc_02` line 70 — CF V7.4 Part II: *"The Story Inventory begins provisionally at Step 2."* No provisional inventory is begun and no story is assigned a tier. §4 invokes the tier framework only negatively (*"No Tier 5 material identified"*), though it describes Pontius's *Life* in exactly the terms Part II gives for **Tier 3** (*"the idealized portrait of a saint's life... the death as completion of a formed life"*) without saying so. This may be a portfolio-wide pattern rather than this document's own defect — the sibling Donatism Doc_02 has the same shape — and if so belongs to a coach pass; either way it should be disclosed at §9 rather than left unmentioned.

**L10.** `Doc_02` line 7 — the header claims the document *"does discharge where they are this step's own job"* Doc_01 §8's binding open items, with no item-by-item accounting. Two of the five Doc_02-directed items are in fact not discharged (H2, H4) and a third is discharged in the wrong place (M9). An enumerated discharge table would have caught all three.

---

## COSMETIC

**C1.** `Source_Registry.md` line 47 / `Doc_02` line 58 — the author publishes as **Brent D. Shaw**; the sibling build's row 24 has it the same way (without the initial), so this is a propagated form rather than a fresh slip.

**C2.** `Source_Registry.md` line 17 — row 6 omits the corpus map's `confidence: assigned` for the pseudo-Cyprianic body (it gives `role` only), and omits the second half of the 2026-08-26 ruling it cites: the body files under Cyprian **and** under `apocryphal-and-pseudepigraphal-literature`, *"because a work circulating under a name that is not its author's is a pseudepigraphon by definition."*

**C3.** `Source_Acquisition_Manifest.md` line 19 / `Source_Registry.md` line 51 — Pellegrino's edition is *Ponzio: Vita e martirio di San Cipriano* (Alba: Edizioni Paoline, **1955**), edited by **Michele** Pellegrino. The Manifest says the year was *"not identified this session"*; one search returns it.

**C4.** `Source_Registry.md` line 50 / Manifest G1 — the CSEL 3 imprint is C. Geroldi filius (Gerold's son), not "Gerold."

---

## The two reviewer-side coverage checks CF V7.4 requires at Doc_02 review

CF V7.4 Step 2: *"Doc_02 review requirement: the review round includes the reviewer-side coverage checks — the ten-item relative-recall test... and the PRESS question, asked verbatim... The answer is recorded in the review artifact, and every named work is dispositioned — rowed, or excluded with a reason."*

**The drafts' own disclosure on this point is correct and should be credited.** `Doc_02` §9 item 6 and the Registry's saturation statement both say these two are reviewer-side and belong to this stage, not to the drafting pass. That is exactly what CF V7.4 says. The field-bibliography sweep and search_record are a different matter (M11).

### Ten-item relative-recall test

Ten works a specialist would expect this world's bibliography to hold, drawn from instruments independent of this build (the *Cambridge History of Early Christian Literature* ch. 14 "Cyprian and Novatian"; the Georgetown and Catholic University of America Augustine research bibliographies; the Oxford Early Christian Texts and Ancient Christian Writers series records).

| # | Work | In Registry? |
|---|---|---|
| 1 | G. W. Clarke, *The Letters of St. Cyprian of Carthage*, ACW 43, 44, 46, 47 (New York: Newman Press, 1984–89) | **No** |
| 2 | Maurice Bévenot (ed./trans.), *Cyprian: De Lapsis and De Ecclesiae Catholicae Unitate*, Oxford Early Christian Texts (Oxford: Clarendon, 1971) | **No** |
| 3 | Possidius, *Vita Augustini* | **No** |
| 4 | Allan D. Fitzgerald (ed.), *Augustine through the Ages: An Encyclopedia* (Grand Rapids: Eerdmans, 1999) | **No** |
| 5 | James J. O'Donnell, *Augustine: Confessions*, 3 vols. (Oxford: Clarendon, 1992) | **No** |
| 6 | F. van der Meer, *Augustine the Bishop* (London: Sheed & Ward, 1961) | **No** |
| 7 | Allen Brent, *Cyprian and Roman Carthage* (Cambridge: Cambridge University Press, 2010) | **No** |
| 8 | Michael M. Sage, *Cyprian* (Philadelphia Patristic Foundation, 1975) | **No** |
| 9 | Paul Monceaux, *Histoire littéraire de l'Afrique chrétienne*, vols. I–III (Paris: Leroux, 1901–05) | **No** |
| 10 | J. Divjak (ed.), *Epistulae ex duobus codicibus nuper in lucem prolatae*, CSEL 88 (1981), and F. Dolbeau, *Vingt-six sermons au peuple d'Afrique* (1996) — the Divjak letters and Dolbeau sermons | **No** |

**Recall = 0/10.** Checked by grep across all three documents for each author and title; the only apparent hits were "Brent" (Brent Shaw's forename) and "sage" inside "passage."

Two honest caveats, stated so the number is not read for more than it is. (i) CF V7.4 does not scope the test to acquirable works, and it should not — items 1, 2, 4, 5, 6, 7 and 10 are in copyright and would be consultation-only rows, never vendored, exactly as rows 30–36 already are. (ii) Item 9's vols. IV–VI are already known to this project: the sibling build requests them at its own G6. Item 10 is the sharpest of the ten for this world specifically: the Divjak letters and Dolbeau sermons are the principal modern additions to Augustine's *pastoral* corpus, they are the discovery that prompted the Epilogue in the 2000 Brown edition this Registry cites at row 30, and their existence bears directly on how complete rows 11 and 19 can claim to be.

### PRESS question

Asked verbatim: **"Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."**

I can name three.

**1. Possidius, *Vita Augustini*.** *Disposition: row it — Type P, Boundary Status Native, Confidence C (not vendored, no locus checked), Licensed For formation-narrative evidence for Augustine.* This is the single most conspicuous absence in the whole Registry. It is the exact Augustine-side counterpart to Pontius's *Life* — a bishop who lived in Augustine's household for decades, writing shortly after his death, and the source for nearly everything known about Augustine's episcopate outside his own writings. §4 (Formation Narrative Sources) assesses one narrative source where the world has two, and CF V7.4's Expanded Author Gravity Assessment requires hagiographers who function as secondary narrative sources to receive their own five-dimension entry. It is not a discovery failure: **Doc_01 §5 already names Possidius**, as the ultimate source for NPNF's editorial note identifying Megalius as Augustine's consecrator, and expressly flags it as *"not vendored in this corpus."* Doc_02 did not carry it forward. A public-domain English translation exists (Internet Archive item `PossidiusAug`), so this is also a real Manifest-level acquisition candidate — arguably a better G1 than the current one, given H5.

**2. G. W. Clarke, *The Letters of St. Cyprian of Carthage*, ACW 43/44/46/47.** *Disposition: row it — Type S, Native, Confidence B, consultation-only (in copyright), Licensed For dating, addressee identification and numbering of row 1's corpus.* The standard modern English translation with full historical commentary of the exact corpus row 1 registers, and the instrument that settles the numbering confusion H1 exposes: the vendored ANF text carries two numbering systems (Migne order, Oxford numbers in notes) and a third (Hartel/CSEL) is what modern scholarship cites. A Registry that licenses row 1 at Confidence A for seven subject areas, on a 19th-century translation of Migne's text, with no modern edition or commentary named anywhere, is under-resourced for the job Doc_03 onward will ask of it.

**3. F. van der Meer, *Augustine the Bishop: The Life and Work of a Father of the Church*.** *Disposition: row it — Type S, Native, Confidence C, consultation-only (in copyright), Licensed For congregational and liturgical practice at Hippo.* The standard study of Augustine's actual pastoral, congregational and liturgical life — which is this world's own named subject. Its absence and the absence of any liturgical-evidence assessment (M10) are the same gap seen from two sides. Rows 30–32 are all biography; row 33 (Burns & Jensen) is the only practice-focused work and is at Confidence C, unread, and flagged.

---

## What was checked and found clean

This is not a short list, and it should be read alongside the findings. The drafting is careful in most of the places where care is hardest.

**Primary-source quotations re-located at source, exact and correctly placed:**
- **Pontius, *Life* §5** — *"by the judgment of God and the favour of the people, he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte"* — verbatim, and the section marker "5." is where the drafts say it is.
- **Augustine, Letter XXXI §4** — *"the blessed father Valerius... has insisted upon adding the greater burden of sharing the episcopate with him"* and *"through the love of Valerius and the importunity of the people"* — verbatim; `div3 vii.1.XXXI`, section 4, confirmed by walking the markup.
- **Augustine, Letter CCXIII §4** — *"I was ordained bishop and occupied the episcopal see along with him"* — verbatim; `div3 vii.1.CCXIII`, section 4.
- **Augustine, Letter 185 ch. 7 §§25–26** — read whole. Every element the drafts rest on is exactly as they report it: the narrower request (protection for Catholic preachers, not abolition of the heresy); the Theodosian law and its **ten pounds of gold** fine; the confinement to districts where Catholics had suffered violence; *"yet we carried our point... it was decreed in our council, and envoys were sent to the court of the Count"*; and §26's *"our envoys could not obtain what they had undertaken to ask,"* with the reason §26 gives (a broader law had already been published after the attack on Maximianus of Bagai). The non-grant — a correction Doc_01 fought over for three rounds — is carried correctly in both Doc_02 §1 and Registry row 12.
- **Augustine, *On Baptism*** — *"was contrary to that which was afterwards brought to light... by the authority of a plenary Council"* — the underlying text reads *"...brought to light by a decision, not of mine, but of the whole Church, confirmed and strengthened by the authority of a plenary Council"*; the ellipsis is correctly placed and the sense is preserved.
- **The 256 council preface** — substance verified in full (see M6 for the rendering).
- **The Scillitan Martyrs' date** — ANF09's own introduction: *"The Scillitan Martyrs were condemned and executed at Carthage on the 17th July, a.d. 180."* Row 28's date, and Doc_02's "66 years" arithmetic against a c. 246 start, are both correct.
- **Pontius at Curubis** — supported by the *Life*'s own words (*"the condescension of his love had chosen me among his household companions to a voluntary exile"*), exactly as §4 claims.

**Secondary scholarship — no fabrication, no misattribution.** All seven verified by WebSearch against publisher, journal-review and catalogue records:
- Brown, *Augustine of Hippo: A Biography* (California, 1967; new edition with Epilogue, 2000) ✓
- Lancel, *Saint Augustine*, trans. Antonia Nevill (London: SCM, **2002**; French, Fayard, **1999**) ✓ — the year the row flagged for second-opinion review is right as printed
- Burns, *Cyprian the Bishop* (Routledge Early Church Monographs, **2002**) ✓ — the year recalled from field knowledge and flagged is right
- Burns & Jensen, *Christianity in Roman Africa: The Development of Its Practices and Beliefs* (Grand Rapids: Eerdmans, 2014) ✓ — full subtitle correct
- Fahey, *Cyprian and the Bible: A Study in Third-Century Exegesis* (Tübingen: J.C.B. Mohr [Paul Siebeck], 1971) ✓
- Rebillard, *The Care of the Dead in Late Antiquity*, trans. Elizabeth Trapnell Rawlings and Jeanine Routier-Pucci (Ithaca: Cornell, 2009) ✓ — both translators correct
- Shaw, *Sacred Violence* (Cambridge, 2011) ✓

Rows 33, 34 and 35 are marked *"recalled from general field knowledge, not independently checked or bibliographically re-verified this session"* and flagged for priority review. All three are accurate as cited. The drafts under-claimed their own reliability rather than over-claiming it; that is the right direction and worth saying plainly.

**Unvendored editions.** Hartel/CSEL 3's title, series, three-part volume structure (3.1 treatises 1868; 3.2 *Epistulae* 1871; 3.3 spuria and indices 1871), city and dates all check out (the forename does not — H5). Harnack, *Das Leben Cyprians von Pontius* (Leipzig, 1913, TU 3rd ser. 9/3) is real. Pellegrino's Alba edition is real.

**The Manifest's disclosed limitations are honest and independently confirmed.** The archive.org item `CorpusScriptoruEcclesiasticorumLatinorum3.2Cyprian` is a genuine Internet Archive item, correctly identified as CSEL 3.2 (Cyprian, *Opera*) — it surfaced as a live search result this session. The egress block is real: fetching that URL from this review environment returned `EGRESS_BLOCKED: archive.org`. And `cic/texts/README.md` does say what the Manifest attributes to it — *"the sandbox this project's agents run in blocks every patristic text host"* — and the public-domain rule is quoted accurately with correctly-marked ellipses. G2's status (*"Public domain status not independently confirmed for either this session"*, *"not independently corroborated by a second search"*) is exactly the right posture and the right honesty. The Manifest's refusal to recommend between acquiring G1/G2 and proceeding on the existing corpus, on the ground that it is the project lead's resource decision, is correct.

**Sibling-build cross-references — all four check out against the branch at `92bc4c38`:** Donatism Registry row 1 is Optatus; row 4 is *Answer to the Letters of Petilian*; row 24 is Shaw's *Sacred Violence*; row 48 is *CIL* VIII; Manifest G7 is *CIL* VIII; Manifest G3 is the *Codex Theodosianus*. Frend's *The Donatist Church* is in the Donatism Registry, so §3's scope note is accurate. And §5's comparative claim — *"Confidence D — lower than the sibling Donatism build's own comparable entry"* — is right: that build's row 28 is C.

**Arithmetic and internal cross-references.** The 184-year span (246–430), the 133-year gap (258–391), the 66-year Scillitan gap, Cyprian's ten-year episcopate, Augustine's thirty-five-year episcopate, the Apiarius affair's "419, running to c. 426" (matching Doc_01 §7, with row 26 honestly disclosing that this rests on secondary characterization rather than on the primary text) — all correct. Every Registry row number cited from Doc_02 (rows 3–4, 5, 7, 9–11, 12–13, 14, 26, 27, 28, 29, 37, 38) and from the Manifest (rows 30–36, 39, 40, 41) resolves to the row the citing text describes. §9 item 3's "rows 31–35" matches the five works it names. The sibling-build G-number references (G3, G7) resolve correctly.

**Portfolio comparison.** §1's *"the largest and most direct primary-source base of any confirmed world in the portfolio to date"* is supportable: parsing every atlas file in `cic/corpus-map/`, this world's 73 works is the largest count (next: post-apostolic-house-church 68, alexandria-catechetical 65). It remains an unrowed comparative claim, but it is true.

**Attribution discipline.** No content is attributed to the project lead anywhere in the three documents without a checkable record. Rows 10, 24 and 6 cite "Mark's ruling" or "Mark's per-work framing" — each of those phrases is in the corpus map's own on-disk note, quoted rather than asserted. This is exactly what CO-022 requires, and it is a failure mode this project has actually experienced.

**Forces integration (CO-022's six integration points; FF V1.1 §4 Step 2).** Present and substantive. §6's closing paragraph answers all three of the Forces Framework's Step 2 questions — which sources speak to external forces (Cyprian's letters as the direct, unmediated record of the Decian and Valerianic persecutions; Augustine's polemical corpora as his own side engaging rival systems), what the silences reveal (no surviving account of how an ordinary believer experienced either crisis, as distinct from how the bishop who led them through it narrated it), and what survivorship indicates — and the observation that both bishops survive in unusually full form *because* each was on the institutionally victorious side of every dispute he engaged is a real forces reading, not a label. Transmission History is named as a dimension for all three voices, as FF §4 requires (quality at M7).

**Other requirements met.** No Tier 5 material anywhere; no invented or illustrative narrative found on a full read of all three documents. Article 20's primary duty (naming structural absence) is genuinely and repeatedly discharged in structure, and the secondary duty is correctly declined for want of a trace rather than exercised speculatively — the right call, though H6 may reopen the input to it. The Article 23 routing note (this world's *opponents* are Article 23's concern, not Article 20's) is correct and well-placed. §7's century-gap disclosure discharges Doc_01 §8 item 1 precisely, including the harder half — that the gap is a silence *in this world's record*, not in the historical record, since the interval is richly attested in another world's territory. §8's Confidence Map uses Constitution Article 17's fixed five-level vocabulary correctly and uses no prohibited language. The Jerome double-placement is stated explicitly at §1 and row 10, discharging Doc_01 §8 item 4's second limb. All three documents sit in the canonical `worlds/lpc/` folder, per CO-022's *Draft* rule; no competing Approved-to-proceed or Frozen Doc_02 exists anywhere in the tree.

---

## CO-022 escalation-category assessment

Run independently against all three documents, not accepted from §10.

**1. Representative identity, name, or title.** Not touched anywhere. Clear.

**2. Portfolio-level or cross-world strategic decisions.** §10's own test — whether a document *decides* something for a reason external to this world's ecology — is the right test, and its application to the Tertullian and Scillitan exclusions, the reliance on the sibling build's verified rows, and the Manifest's ordinary acquisition request is sound. **But §10 does not assess the one live cross-world item Doc_01 handed this step**: the Optatus placement question (H2), which the corpus map itself leaves open with *"Mark may prefer another Latin home for a Numidian polemicist."* Once H2's misstatement is corrected, the underlying question has to be answered. If the build thread answers it on this world's own ecological evidence, no escalation follows; if the answer turns on portfolio convenience or on what another world wants, category 2 applies and §10 must say so. The same applies to H4's double-placement question. **Not an escalation as things stand — an unassessed item that §10 must run.**

**3. Governance or methodology decisions.** None. The CF-V7.4-versus-Template divergence in the priority-flag rule (L4) is already documented inside the Template itself; disclosing which rule was applied is a drafting fix, not a governance decision.

**4. Unresolved tensions the pipeline cannot close on its own.** No review-versus-review disagreement exists yet — this is Round 1. But **H1 is a finding that cuts against an earlier decision**, in CO-022's own words. The Ep. XL misattribution is not confined to the documents under review: it sits in live text at Doc_01 §5, twice in Doc_01 §9's revision log, and in `Doc01_Round9_Review.md`'s own method note, where the round that certified Doc_01 as Cleared listed it as a verified check. Doc_01 is **Approved to proceed**, not Frozen, and sits inside this world's own build folder, so the build thread has the standing to correct it. CO-022's *Naming and term propagation* rule then binds: *"a fix that lands in the narrative document without the index being updated to match is not a complete fix."*

**My reading: no escalation category compels a stop, but the project lead should be told about H1 rather than have it fixed silently** — because the correction touches a disposed document and a review artifact that certified the error, and because a review artifact is a record of what a round found, not a document to be quietly amended. The right shape is: correct Doc_01 §5 and §9 with a dated inline correction note disclosing what was wrong and how it was found (the pattern Doc_01's own Round 8 fix already established for a false claim in §9), leave `Doc01_Round9_Review.md` untouched as the historical record, and log the whole thing in `lpc_Decision_Log.md`. If the build thread reads the situation differently, that disagreement is itself a category-4 item.

---

## Required actions before Round 2

1. **H1** — correct Ep. XL → Ep. XXXIX in Doc_02 §1 and Registry row 1; rewrite row 1's Verification Note to state what was re-located this session; propagate to Doc_01 §5 and §9 with a dated correction note, and log it (see the escalation note above).
2. **H2** — correct the Optatus characterization in Doc_02 §1 against the corpus map's actual text; answer or carry forward the placement question Doc_01 §8 item 2 assigns.
3. **H3** — row Letter XCIII (or withdraw the claim resting on it) and the *Codex Theodosianus*; withdraw or re-ground the *De Unitate* conciliar-authority claim; correct the Registry's line-6 assertion that the checkpoint rule is satisfied.
4. **H4** — disclose and dispose of the duplicated 256-council corpus-map rows.
5. **H5** — correct "Karl" → "Wilhelm" and withdraw the "edition underlying the vendored ANF05 translation" rationale from row 39 and Manifest G1; restate G1's value on what it would actually add.
6. **H6** — withdraw §6's three blanket negatives; assess Letters CXXVI and CCXI, Epistles XX–XXI, and Pontius's own diaconal voice against the Article 20 duty.
7. **M1–M15** — each is a substantive change to a claim, a confidence rating, a sourcing conclusion, or a corpus-map representation, and each needs to land in the file.
8. **PRESS dispositions** — row Possidius, Clarke, and van der Meer, or exclude each with a stated reason.
9. **M11** — either run the field-bibliography sweep and close the Registry with a real saturation statement, or state plainly at §10 that Step 2 is knowingly incomplete on a Registry activity (not only on the reviewer-side checks) and what that costs downstream. The 0/10 recall result should be recorded in the Registry, not only here.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED.** Per CO-022's *Revision decision* rule, a revised Doc_02 / Source Registry / Manifest goes through independent review again.
