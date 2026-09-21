# World Profile — Round 3 Independent Adversarial Review (SCOPED)

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

**Document under review:** `lpc_World_Profile.md`, 16,776 words (`wc -w`), 773 lines, as at commit `ae8451ed`.
**Reviewer:** isolated adversarial pass. I did not write the document, I did not write Round 1 or Round 2, and I did not apply any fixes.
**Scope:** deliberately narrow. Round 2's **NEW-1** and **NEW-2**, and NEW-2's blast radius — a full sweep of the document against `possidius_vita-augustini_weiskotten1919.txt`. Plus a bounded adjacency check on Sections 4D and 4F and the Doc_05 citations named in the brief. **Everything else Round 2 raised is out of scope and was not re-audited.**

---

# VERDICT: **REVISION REQUIRED**

**2 HIGH · 2 MEDIUM · 3 LOW (new, within scope).**

- **NEW-1 — PARTIALLY FIXED.** Both clauses Round 2 flagged are now correct and correctly sourced. The fix then drew an inference from them that is false in the same failure class, running the opposite direction. → **HIGH-1**.
- **NEW-2 — CONFIRMED FIXED at its own sentence; blast radius NOT CLEAN.** The Section 4F sentence is now right and its two new quotations resolve verbatim. The sweep Round 2 asked for turned up a claim stated at **three sites** in this document that Possidius chapter VIII refutes in terms, plus a material-lens claim the same source qualifies, plus a disclosure defect created by the 4F fix itself. → **HIGH-2, MEDIUM-1, MEDIUM-2, LOW-3**.

**This is not the clean confirming round the brief held open as the expected outcome.** I want to be equally plain about what *is* clean: the two sentences Round 2 actually wrote findings about are both fixed, at source, correctly. Every quotation newly introduced into 4D and 4F resolves verbatim to its cited source. All five Doc_05 loci the brief named say what the document attributes to them. Five of the eight Section 8 honest-limit domains, and every silence claim in the document about women's voices, Punic-speaking congregational life, the non-episcopal voice, the lapsed, the origin myth and the 133-year gap, held under direct testing against Possidius. The two HIGHs are both in material the fix pass touched or should have touched, and neither is a hedge that got stretched — each is a flat statement a Native vendored source contradicts.

---

## Method

I resolved the Cyprian corpus by `title=` on `<div3>`, never by position, and marked editorial spans before stripping.

For Possidius I applied the equivalent discipline to a non-XML source. `possidius_vita-augustini_weiskotten1919.txt` is a bilingual critical edition: Weiskotten's revised Latin and his English translation alternate by page, and both hyphenate across line breaks. I built a de-hyphenated flat stream of the whole file (54,613 tokens) before searching — searching the raw file returns false negatives on every phrase that crosses a line. **I then separated Weiskotten's own apparatus from Possidius's voice**: the file carries a 40-page Introduction, an apparatus criticus, and endnotes, all in the same stream as the text. Everything I cite below as Possidius's is in the body, between its own chapter headings, with the facing Latin verified; nothing is taken from the Introduction or the notes. That distinction is load-bearing here — Weiskotten's Introduction, for example, states that "a council which met at Carthage in 404 decided to appeal to the Emperor for protection," which is the editor's reconstruction and **not** Possidius's narrative, and would have produced a false finding against Section 4E had I read it as the world's voice.

I read the **whole** *Vita*, not the XIX–XXVII span the build read. Chapters V and VIII, which carry both HIGHs, are outside that span.

I re-derived NEW-1 from Doc_04 and Doc_05 directly and did not consult the diff until afterwards.

---

# Round 2's two findings, re-derived

## NEW-1 (HIGH) — **PARTIALLY FIXED**

### What the finding is actually about, derived at source

`Doc_04_Gravity_Discovery.md` line 92. The finding sits inside the **Formation** test of **Candidate 5 — Conciliar Authority Theory (Egalitarian vs. Hierarchical)**, the candidate classified Supporting and carried into the Profile as **G5**:

> **Formation:** Does not clearly pass. This document finds no evidence in Doc_02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, **this specific theoretical question**.

"This specific theoretical question" is, unambiguously from the candidate heading and from the Repetition and Persistence tests either side of it, **the theory of what a council is and what it binds** — Cyprian's *"neither does any of us set himself up as a bishop of bishops"* against Augustine's *"the authority of plenary Councils."* It is about G5 and nothing else. Both downstream users scope it identically: `Doc_05_Ecological_Reconstruction.md` line 175, inside **§4.2**, under the heading *"What G5 does and does not do in this ecology"*; and `Doc_07 §3C`, which applies it to *"Neither conciliar formula (G5)"*. **Round 2's derivation is correct.**

### What Doc_05 §5.3 says, and whether it holds

§5.3 is headed *"The one gravity that is formation content rather than formation medium, and its bound."* It is about **G7 (Grace and Human Incapacity)**, calls it *"a sustained catechetical and polemical formation project across thirteen dedicated works"* with *"grace"* at **1,798 raw / 1,665 stripped** occurrences inside row 23, and states the bound:

> an ordinary believer at Hippo in the 420s **is being formed by this material**; an ordinary believer at Carthage in the 250s is not, and **no Pelagian-anthropology-equivalent exists anywhere in Cyprian's corpus**, because the controversy postdates him by over a century.

It holds, and the scope of its negative limb matters for what follows: **what §5.3 says is absent from Cyprian's phase is the *Pelagian-anthropology-equivalent*, not this world's account of the human person.**

### Does Section 4D now state both correctly? **Yes.**

> The G5 conciliar question does **not** reach ordinary formation: Doc_05 carries Doc_04's finding of **no evidence in Doc_02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, that specific theoretical question**. **G7's grace material is different, and Doc_05 §5.3 says so directly:** *"an ordinary believer at Hippo in the 420s is being formed by this material; an ordinary believer at Carthage in the 250s is not,"* the controversy postdating Cyprian by over a century.

The finding is restored to G5. The false second clause (*"Doc_05 §5 does not narrate it as part of anyone's formation"*) is gone, replaced by the §5.3 contrast that refuted it. The §5.3 quotation resolves **verbatim**. The G6/G7 transposition is gone. **Round 2's finding, as written, is discharged.**

### But the sentence the fix then added is a new overstatement — HIGH-1

---

## HIGH-1 (NEW). Section 4D's closing phase-asymmetry claim is refuted by Doc_05 §5.1 and §6.6, and by this document's own Section 2

**Where.** Section 4D, line 224, the last clause of the paragraph:

> The anthropology above is therefore **formation content in the Augustine phase and absent in Cyprian's**, while the ontology underneath G6 is what the disputes presuppose rather than a catechism anyone was taught.

**What "the anthropology above" is.** The sentence's own contrast structure — *anthropology* against *the ontology underneath G6* — fixes the referent. The ontology limb is the "most given" sentence. The anthropology limb is everything else the paragraph asserts about the person:

- *most real about a person:* "that they are someone's: a member of a specific flock, under a specific bishop, in a specific place";
- *fundamental problem:* "failure under pressure — … having complied when it counted; **and in the Augustine phase, beneath that,** a will that cannot right itself unaided (G7)";
- *fundamental possibility:* "restoration to the standing already held, by a public road walked in front of the people who watched the fall."

**Three of those four clauses are Cyprian-phase-grounded, and the paragraph itself marks the fourth as the Augustine-phase addition.** The "therefore" generalises from the G7 limb — the one limb explicitly flagged as Augustine-phase — to the whole.

**Evidence that "absent in Cyprian's" is false.**

1. **Doc_05 §6.6**, the section this document cites *two paragraphs later* at 4F, lists the channels through which meaning moves in this world and names third among them: *"the penitential process, **which teaches by enacting on a named person in public what the community holds about failure** (G2)."* That is the fundamental-problem/fundamental-possibility pair named as a **formation channel** — and G2 is Cyprian-phase-grounded.
2. **Doc_05 §5.1** narrates the ordinary shape of formation as catechesis → baptism → weekly preaching → *"if they fail seriously, they enter a public, graded penitential process and return by it,"* rendered inhabited as *"if you fall you are not finished, you are set on a road back that everyone can see you walking."* That is the anthropology of 4D, described as ordinary formation, without phase restriction.
3. **This document's own Section 2, G2 entry (line 74):** *"Doc_04's own Persistence test finds this gravity **does not persist into Augustine's own phase under its own name**."* The document therefore says, thirty lines apart, that the road-back anthropology is Cyprian-phase-grounded and attenuates in Augustine's — and that it is "absent in Cyprian's."
4. **Doc_05 §5.3 does not support the generalisation.** Its negative limb is scoped to *"no Pelagian-anthropology-equivalent."* 4D widens it to the whole account of the person.
5. **Section 4A and 4E** of this same document ground the penitential road in Cyprian's phase throughout.

**Why HIGH.** It is a **silence claim** ("absent in Cyprian's"), stated flatly, refuted by an approved input, contradicting the document's own Section 2 — written into the paragraph that exists to satisfy Round 1's MEDIUM-3 and rewritten to satisfy Round 2's NEW-1. It is the build's signature defect surviving two fix passes in the same paragraph, in mirror image: Round 2 found it understating what G7 did to ordinary believers; it now understates what G2 did to them. A Representative built on 4D would carry an account of the human person it believes was taught only after 391.

**Fix.** The defensible statement is already available in the paragraph's own materials: the *problem/possibility* pair is Cyprian-phase formation content, carried into Augustine's phase as family resemblance rather than under its own name (Section 2 G2); the *grace* limb beneath it is Augustine-phase formation content and has no Cyprian-phase equivalent (Doc_05 §5.3); the *ontology* limb is presupposed by the disputes rather than taught (already correct). Three scopes, not one.

---

## The Article 19 question on the 4D ontology paragraph — derived, not invented

The brief asks whether the "most given / most real about a person / fundamental problem / fundamental possibility" claims are derived from upstream or free-invented. I traced each. **The substance is derived; the wording is this document's own synthesis, which is what a Profile is for.** No Tier 5 exposure.

| 4D claim | Upstream basis | Verdict |
|---|---|---|
| *Most given:* the one church as a bounded, visible communion with a named man answerable for it | G6 (Doc_04 §3 Candidate 6; Doc_05 §6.1) + G1 (Doc_05 §4, the 113 flock/shepherd/pastor occurrences). The supporting reason — that both bishops reverse the answer without doubting the boundary matters — is Doc_04's own reading of G6, carried at this document's 4H | **Derived** |
| *Most real about a person:* they are someone's — a member of a specific flock, under a specific bishop, in a specific place | G1 as Doc_05 §4 states it ("care for and responsibility toward a bounded local community he is personally answerable for *and to*"); Doc_05 §1 on the ordinary baptized as "the body a bishop addresses, grieves over, disciplines, and is elected by" | **Derived** |
| *Fundamental problem:* failure under pressure, having complied when it counted | Doc_01 §6, nearly in its own words: *"testing whether the church could survive its own members' failure under pressure"*; G2; Doc_05 §1.1 | **Derived** |
| *…not ignorance, not unlikeness to God* | **Nothing.** Zero hits anywhere in this build's documents | **LOW-1** |
| *Fundamental possibility:* restoration to the standing already held, by a public road walked in front of the people who watched the fall | This document's own G2 Brief description (*"walked back into standing where the community that watched the failure can watch the return"*, sourced to Doc_07 §2I); `lpclex002`; Doc_05 §5.1 | **Derived** |

The paragraph also states its own method honestly — *"This world does not argue either abstractly, and the shape has to be read off what it fought about"* — which is the right disclosure for a synthesis at this altitude. **The free-invention question comes back clean.** The failure at 4D is an inference drawn wrongly from correctly-cited material, not material invented.

---

## NEW-2 (MEDIUM) — **CONFIRMED FIXED** at its own sentence

Section 4F now reads:

> The presbyters appear in this record almost exclusively as faction (five in recorded opposition to Cyprian's election) — a real distortion in the institutional picture, **and Doc_07 §2F states it flatly. Possidius chapter V is the counter-instance, and it is Native and vendored (row 192):** Valerius *"gave his presbyter the right of preaching the Gospel in his presence in the church and very frequently of holding public discussions — contrary to the practice and custom of the African churches,"* and afterwards *"some other presbyters by permission of their bishops began to preach to the people in their presence."* That is ordinary, non-factional presbyteral work, attested twice. **The distortion is real for Cyprian's phase, where the presbyters of the record are the faction; it is not a blanket silence.**

The fix took **both** of Round 2's options rather than one, which is the stronger answer.

- Both quotations resolve **verbatim** in the de-hyphenated stream, including the em-dash, chapter V body text.
- Attribution to **Valerius** is correct: the passage's subject is *"the holy Valerius who ordained him,"* who *"saw that he himself was less useful for this end"* — Possidius's own stated reason.
- *"Doc_07 §2F states it flatly"* is accurate. Doc_07 §2F closes: *"the ordinary, non-factional work of a presbyter in this world is essentially unattested, and a Representative should not be built as though the presbyterate were inherently oppositional."*
- The narrowing to Cyprian's phase is defensible on the Epistles.

**Round 2's finding is discharged.** The blast radius is not.

---

# The Possidius sweep — every claim tested

I extracted every sentence in the document matching the silence-claim pattern (102 candidates) and tested each against the whole *Vita*. Below is everything where the source could bear at all, including the ones that held.

| # | Profile claim (line) | Possidius locus tested | Result |
|---|---|---|---|
| 1 | 4F: "the ordinary, non-factional work of a presbyter is essentially unattested here" *(pre-fix)* | ch. V | **REFUTED — already fixed.** See above |
| 2 | 4F (232), 4F (234), Force 2A-2 Layer 3 (292): congregational demand attested "at the episcopate for Cyprian… at the presbyterate for Augustine, **not at the same office for both**"; "Augustine's own episcopate came by designation and consecration **rather than a second acclamation**" | **ch. VIII** | **REFUTED → HIGH-2** |
| 3 | §8 Domain 5 (648) / 4G (238): "What this world wrote down about its own buildings is almost nothing… its record is a correspondence and a preaching corpus, **not an inventory of its own fabric**" | ch. XXII, **ch. XXIV**, ch. V, ch. XVIII | **QUALIFIED → MEDIUM-1** |
| 4 | Disposition (765): "this document draws on that read at Sections 3, 4C and 5"; 4C (218): read scope is "chapters XIX–XXVII" | ch. V is now quoted at 4F | **STALE / UNDISCLOSED → MEDIUM-2** |
| 5 | 4B (214): "This world attests all three [entry, middle, maturity] **from the bishop's side and almost nowhere else**"; maturity limb rests on Doc_05 §6.5's **Tier 4** reconstruction | ch. XIX–XXVII entire | **HELD, but a Tier 1 strengthening is left on the table → LOW-3** |
| 6 | §8 Domain 3 (640) / 4F: rural and **Punic- or Berber-speaking** congregational life is an open question this build has not answered | whole *Vita*, both languages | **HELD.** "Punic" / "Punica" occur **zero** times in Weiskotten, body or apparatus |
| 7 | §2 G8 (166), §3 (192), §5 (364), §7 (596): confessors are **Cyprian-phase-bound**, "no Augustine-phase confessor-authority material exists anywhere in this world's corpus," established by a positive sweep of the eight vendored Augustine volumes | whole *Vita* | **HELD, and now stronger.** "confessor" occurs **zero** times in Weiskotten. Row 192 was not inside the eight-volume sweep; it is now checked |
| 8 | §8 Domain 2 (632, 634): named women are "visible… none is audible"; "**we have no woman's own words**" | whole *Vita* — all 12 `she`, 12 `women`, 10 `sister`, 1 `woman`, 1 `handmaid` contexts read | **HELD.** No woman speaks anywhere in Possidius's text. ch. XXVI is entirely Augustine's rule *about* women; the Monnica material is Weiskotten's Introduction, not the *Vita* |
| 9 | §8 Domain 1 (624, 626): "**no one who merely sat in the congregation left us an account of a Sunday**"; "what we do not have is anyone who held no standing at all" | whole *Vita* | **HELD.** Possidius is bishop of Calama — episcopal, and not a congregant without standing |
| 10 | §8 Domain 7 (671): the lapsed — "**not one of them left an account of why**" | whole *Vita* | **HELD.** Cyprian-phase subject matter; "lapsed" occurs zero times in Weiskotten |
| 11 | §8 Domain 5 (648) / 4G (238): "**no site report, inscription catalogue, or excavation record has been independently verified in this build**" | whole *Vita* | **HELD.** Possidius is a text, not an excavation; the one inscription he reports (the verse on Augustine's table, ch. XXII) is a reported text, not an epigraphic record |
| 12 | §8 Domain 8 (679): "This world left **no order of service and no liturgical treatise of its own**" (Doc_05 §3) | ch. XXIV, **ch. XXX** (Augustine *Ep.* 228 quoted at length), ch. XXXI | **HELD.** No order of service and no liturgical treatise. *Note:* ch. XXX gives an Augustine-phase Native attestation of mass demand for the rites in emergency — *"some clamoring for baptism, others for reconciliation, still others for acts of penance: all of them seeking consolation and the administration and distribution of the sacraments"* — which **strengthens** 4A's ordinary-sequence claim and is uncarried. And ch. XXIV names *"the consistory, from which were supplied the things necessary for the altar."* Domain 8's own point — that the material exists and has never been read *as* liturgical evidence — is made truer, not falser |
| 13 | §8 Domain 6 (664) / §1 (34) / Force 3B-2 (438): the 133-year interval, "a genuine silence in this world's own record" | whole *Vita* | **HELD.** Possidius writes c. 431–439, wholly inside phase two. The one crossing he supplies (*De Mortalitate*) is already wired at three sites |
| 14 | §8 Domain 4 (656) / 4C (218): "This world has **no founding narrative and no origin myth**"; two pastoral biographies | whole *Vita* | **HELD.** The *Vita* is one of the two biographies already counted, and narrates a man's life, not a community's origin |
| 15 | §2 G2 (74): G2 "**does not persist into Augustine's own phase under its own name** — no Augustine-phase text is organized around a lapsed-equivalent crisis at the same acute, empire-wide scale" | **ch. XXX** | **HELD — on its hedge.** ch. XXX shows penance and reconciliation in live mass use under the Vandal invasion, but no Augustine-phase text *organized around* a lapsed-equivalent crisis. The claim survives because "under its own name" and "organized around" are doing real work. Worth knowing that they are |
| 16 | 4E (228): Augustine's relation to state coercion develops across **three phases**; the middle one "a real but narrow solicitation of legal protection, argued and **in the event not granted**" | ch. XII, ch. XIII, ch. XVIII | **HELD, and supported.** In Possidius's own narrative the anti-Donatist imperial order issues from *Crispinus's* appeal, and Augustine's recorded action is to get the resulting condemnation **withdrawn**. (The contrary-looking "council… decided to appeal to the Emperor for protection" is Weiskotten's Introduction, not Possidius) |
| 17 | §5 Force 2B-3 / lex016 (578, 582): the illegal-to-established shift "changes the instruments available to a bishop, not the thing a bishop is" | ch. XII, XIII, XIX, XX | **HELD, and strengthened.** ch. XIX–XX show the episcopal office absorbing a civil-judicial function Cyprian's never had, and Augustine calling it *"a kind of conscription"* — instruments, not identity |
| 18 | §5 Force 1B-1 area / 4D (222): the Manichaean half "named and not developed… a stated limit rather than a judgment that the Manichaean pressure was slight" | ch. VI, ch. XVI | **HELD.** It is a claim about this build's own process, not about the corpus. ch. VI's public disputation with Fortunatus supports the document's own refusal to call the pressure slight |
| 19 | §3 (192): formation logic crosses the gap by "**two demonstrated mechanisms, both textual**" | ch. XXVII | **HELD.** Re-verified at both ends independently: Weiskotten ch. XXVII against ANF *De Mortalitate*, resolved by `title=` |
| 20 | §5 Force 2A-3 (304): *De Mortalitate* "generated no gravity and no practice; it generated a treatise" | ch. XXVII | **HELD.** Possidius deploys the treatise pastorally; that is use of a text, not a practice |

---

## HIGH-2 (NEW). "Not at the same office for both" / "not a second acclamation" is refuted in terms by Possidius chapter VIII — Native, vendored, row 192, and stated at three sites

**Where, all three.**

- Section 4F, line 232: *"congregational demand overrides a reluctant convert's preference at the point of entry into clerical office — at the episcopate for Cyprian ('your suffrage and God's judgment'), at the presbyterate for Augustine, **not at the same office for both**."*
- Section 4F, line 234 (the new authority-grounds paragraph added for Round 1's MEDIUM-3): *"the consent of that people, attested at entry to clerical office — 'your suffrage and God's judgment' for Cyprian's episcopate, the presbyterate for Augustine, **not the same office for both** (Doc_05 §4.1)."*
- Section 5, Force 2A-2, Formation impact, line 292: *"Augustine's own episcopate came by designation and consecration **rather than a second acclamation**."*

**What the source says.** `possidius_vita-augustini_weiskotten1919.txt`, **chapter VIII**, whose own heading is *"He is chosen bishop while Valerius is still living, and is ordained by the primate Megalius"* — English at raw lines 2133–2144, facing Latin at 2095–2103:

> Later on, accordingly, when Megalius, Bishop of Calama, and at that time primate of Numidia, had come at his request to visit the church at Hippo, unexpectedly to all the bishop Valerius made his desire known to the bishops who happened at that time to be present, and to all the clergy of Hippo **and to all the people**. But while **all who heard rejoiced and clamored most e[a]gerly that this should be done and accomplished**, the presbyter **refused** to accept the episcopate contrary to the custom of the Church, since his bishop was still living. However, when they had convinced him that this was generally done… **under compulsion and constraint he yielded** and accepted the ordination to the higher office.

*(Weiskotten's printing reads "elageriy"; the OCR is obvious and the Latin settles it.)* The Latin: *"et universae plebi inopinatam cunctis suam insinuavit voluntatem: omnibusque audientibus gratulantibus, atque id fieri perficique **ingenti desiderio clamantibus**… compulsus atque coactus succubuit et maioris loci ordinationem suscepit."*

**What breaks.**

1. **"Rather than a second acclamation" is false.** Chapter VIII narrates a second acclamation: the whole people (*universae plebi*), the clergy of Hippo and the visiting bishops, hearing the proposal and clamoring *ingenti desiderio* that it be carried out.
2. **"Not at the same office for both" is false as a claim about where the pattern is attested.** The document's own definition of the pattern — *"congregational demand overrides a reluctant convert's preference at the point of entry into clerical office"* — is satisfied at Augustine's **episcopate** exactly as it is at his presbyterate: acclamation, refusal, *compulsus atque coactus succubuit*. It is attested at both of Augustine's offices, not one.
3. **It is not a new source.** `Doc_03_Lexicon_Candidate_List.md` rows 29 and 30 already quote **Possidius *Vita* IV** at length for the presbyterate seizure, and in the same cell assert that the episcopate came *"not a second popular acclamation."* The build read chapter IV of this file and asserted a negative about the event narrated four chapters later in the same file.

**Why HIGH rather than MEDIUM.** It is stated three times, it is not hedged, and it is presented at 4F as a **precision the build insists on keeping** ("not the same office for both" is bolded at both 4F sites). It feeds the Capsule Core's authority structure. And it is the identical failure class Round 2's NEW-2 found: a negative asserted about a source this build has in its own corpus and has already quoted. The distinction the claim is reaching for is real — Valerius's designation and Megalius's consecration were the *mechanism*, and the people's clamor was assent to a plan already formed rather than the constitutive act — but the document does not say that. It says the acclamation did not happen.

**Fix.** Re-scope to what survives. What is true is that *Cyprian's own word* for the congregational voice attaches to his episcopate and has no verbal counterpart at either of Augustine's ordinations — which is Doc_03's actual caution (*"different figures, different offices, and different words, not one term"*), and which the document already carries one sentence later at 4F. What is not true is that the phenomenon is absent at Augustine's episcopate. Correct at all three sites; Doc_05 §4.1's *"not by a second acclamation"* and Doc_03 rows 29–30 need the same correction and should be flagged upward rather than edited from this thread.

---

## MEDIUM-1 (NEW). The material lens's stated reason is falsified by two chapters inside the build's own read span

**Where.** Section 8 Domain 5, line 648: *"What this world wrote down about its own buildings is almost nothing. Its material evidence is **document-borne** — a basilica's interior recovered from a pastoral letter, two documentary artefacts — **because its record is a correspondence and a preaching corpus, not an inventory of its own fabric**."* Section 4G names the same two positives and nothing else.

**What Possidius has.** Chapter XXIV is, almost precisely, an inventory of the fabric and its administration:

> **The care of the church building and all its property** he assigned and entrusted in turn to the more capable clergy. **He never held the key nor wore his ring**, but everything which was received and spent was noted down by these overseers of the house. **At the end of the year the accounts were read to him**…

and, in the same chapter: *"For new buildings he never had any desire… Nevertheless he did not restrain those who desired or constructed them, provided only they were not extravagant"*; *"he even ordered **the holy vessels** to be broken and melted down"*; and the *gazophylacium et secretarium*, *"the treasury and the consistory, from which were supplied the things necessary for the altar."* Chapter XXII gives the vessels by material — *"silver spoons… earthen, wooden or marble vessels"* — and the verse inscription on the bishop's table. Chapter V has the monastery *within* the church; chapter XVIII the *"library of the church of Hippo."*

**Why this is a finding.** The ecological basis given is a causal claim about the corpus, and it is wrong: this world's record contains an inventory of its own fabric, by an eyewitness, in a Native vendored source. **Chapters XXII and XXIV are inside XIX–XXVII** and both appear in `Possidius_XIX-XXVII_Read_2026-09-15.md` by name — "silver spoons, earthen, wooden or marble vessels," "He never held the key nor wore his ring." The fix pass had this in hand and did not carry it to the one lens the document itself calls thinnest.

The hedge "almost nothing" survives if the claim is narrowed to what 4G's own Representative-handling line already says — *what the buildings looked like, stone by stone*. That is genuinely thin. What this world wrote down *about* its buildings and their contents is not.

**Fix.** Add Possidius XXII and XXIV to 4G alongside Letter CXXVI, and re-scope Domain 5's basis from "not an inventory of its own fabric" to the absence of *architectural description*, which is what the evidence actually shows.

---

## MEDIUM-2 (NEW). The 4F fix rests on a chapter outside the build's recorded read span, and the Disposition's list of where the read is used is now stale

Created by the NEW-2 fix itself.

- The Disposition, line 765: *"Possidius's* Vita Augustini *XIX–XXVII **has been read at source** (2026-09-15…), and this document draws on that read at **Sections 3, 4C and 5**."* It now also draws on it at **4F** — omitted.
- Worse: **4F quotes chapter V, which is not in XIX–XXVII and is not in the read artifact.** Section 4C states the read scope as "chapters XIX–XXVII." The document therefore quotes, as load-bearing correction, a chapter its own disclosure says has not been read, with no note of where the reading came from. (It came from the Round 2 reviewer.)
- Related, and the same shape: line 58 states that Doc_04 excluded the *Vita* because *"it had not then been read beyond the Megalius-consecration identification."* That accurately carries Doc_04 line 34 — but Doc_03 rows 29–30 quote *Vita* IV at length, so the build's own record of what it has read from this file is unreliable at both ends. That is the condition that produced HIGH-2.

**Fix.** Add 4F to the Disposition's list; state at 4F or in the Method Note that chapter V was read at source on this date, outside the XIX–XXVII span, and record it; and either widen the recorded read to the whole *Vita* or say plainly which chapters have been read. Given HIGH-2, **reading the whole *Vita* is the cheaper option and I would recommend it before the next pass.**

---

## LOW-1. 4D's "not ignorance, not unlikeness to God" has no upstream basis

The clause makes an implicit cross-world contrast — these are the fundamental problems of other formation worlds in this portfolio — with no citation, and neither term appears anywhere in this build's documents (`grep` across Doc_01–Doc_09, the chunks and the Profile: zero hits outside this sentence). Elsewhere the document cites its cross-world boundaries carefully (Doc_01 §7 for World #6 at 4E; the Donatism sibling at 4C and 4H). This one does not. It also sits awkwardly against a world whose Supporting gravity G4 is catechesis. Either source the contrast or drop it; the positive limb carries the sentence on its own.

## LOW-2. 4D cites "Doc_05" for the G5 finding without a locus, and alters a near-quotation silently

The finding is at **Doc_05 §4.2**, line 175 — the sentence cites Doc_05 §5.3 by number one clause later, so the asymmetry is conspicuous. Separately, the bolded span *"no evidence in Doc_02 that ordinary believers… were formed by, or even aware of, **that** specific theoretical question"* is Doc_04's wording with "this" silently changed to "that." It is bolded rather than quoted, so no quotation rule is broken; but Round 2's LOW-2 was about exactly this class of unmarked alteration, and the fix is one word of ellipsis or one set of quotation marks.

## LOW-3. 4B's maturity limb reaches for a Tier 4 reconstruction while Tier 1 material sits unread into it

4B answers the template's "maturity" question with Doc_05 §6.5's inhabited line — *"A man given a people does not get to be calm about them"* — correctly labelled as this build's **Tier 4** reconstruction. The build's own read artifact says of the span it just read: *"**Possidius XIX–XXVII is not Tier 4 material**… It is Tier 1 material. The daily work this world makes its Primary gravity is not a gap requiring reconstruction; it is attested and was unread,"* and that G1 gains *"its richest single attestation"* there, in phase two. Nine chapters of eyewitness attestation of a mature bishop's ordinary answerability — the judge who called it *"a kind of conscription,"* the annual audit, the offer to hand the church's possessions back — are exactly the template's maturity question, answered at Tier 1. Nothing in 4B is false. It is a strengthening the fix pass left on the table, and it is the same un-carried read as MEDIUM-1.

---

# What I checked and found clean, at the scope I checked it

**Every quotation newly introduced into 4D and 4F resolves verbatim to its cited source.** Specifically:

| Quotation | Source | Result |
|---|---|---|
| *"an ordinary believer at Hippo in the 420s is being formed by this material; an ordinary believer at Carthage in the 250s is not"* | Doc_05 §5.3 | **Verbatim** |
| *"gave his presbyter the right of preaching the Gospel in his presence in the church and very frequently of holding public discussions — contrary to the practice and custom of the African churches"* | Possidius ch. V, body | **Verbatim**, de-hyphenated; em-dash correct |
| *"some other presbyters by permission of their bishops began to preach to the people in their presence"* | Possidius ch. V, body | **Verbatim**; Latin *"accepta ab episcopis potestate, presbyteri nonnulli coram episcopis populis tractare coeperunt"* confirms |
| *"your suffrage and God's judgment"* / *"not the same office for both"* | Doc_05 §4.1 | **Verbatim** (the underlying claim is HIGH-2) |
| *"bishop of bishops"* / plenary Council pair | Doc_05 §4.2 | **Verbatim** |
| *"attested through different figures, different offices, and different words, not one term"* | Doc_05 §4.1, quoting Doc_03 | **Verbatim**, and present in Doc_03 rows 29–30 |
| Doc_05 §6.6 paraphrase — *"through texts read later, not through a continuous teaching succession this build can evidence"*, "a structural feature rather than a shortfall" | Doc_05 §6.6 | **Accurate**; §6.6 says "recorded as a finding rather than as a shortfall" |

**The five Doc_05 loci the brief named all say what the document attributes to them.** §3 carries both *"mostly through what preaching and catechesis presuppose about it"* and *"not through separate liturgical treatises"* (the latter §3's own quotation of Doc_01 §3, which the Profile correctly frames as "Doc_05 §3 records"). §5.2 is not cited in the Profile at all, and Section 3's treatment of G4 as medium is consistent with it. §5.3 as above. §6.5 is correctly identified as **Tier 4**, matching its own construction note *"Composed from three attested affects"* — this is careful work and I want it noted. §6.6 as above. **No mis-citation among them.**

**Sections 4D and 4F still read coherently.** The 4D ontology paragraph flows from the doctrinal-bodies paragraph above it and the insertions did not orphan anything; the 4F fix is inserted cleanly between the faction sentence and the authority-grounds paragraph, with no dangling remnant of the pre-fix text (duplicate-sentence sweep run across the whole file: no un-corrected variant of either sentence survives). The surrounding argument in both is intact.

**Possidius findings independently re-verified:** the *De Mortalitate* crossing at both ends; the chapter V passage in both languages; the chapter VIII passage in both languages; the chapter XXII/XXIV material in the English body with Latin adjacent.

---

# What I did not check

Everything outside the two findings. Specifically and deliberately: the counts, Section 11, the escalation assessment, the Method Note, the Section 10 verification command, the gravity entries in Section 2 other than G2's and G8's phase limbs, the fifteen Section 5 force entries other than 2A-2, 2A-3, 2B-3 and 3B-2, Section 6's vocabulary tags, Section 7, Section 9, and all of Round 2's other thirteen findings and their fixes. **None of these was re-audited and nothing here should be read as clearing them.**

Within scope, three further limits:

1. I tested the document against **Possidius**. I did not re-sweep it against Pontius, the Cyprian corpus, the Augustine volumes, or the Latin CSEL files. The silence claims at rows 6–14 of the sweep table held *against Possidius*; several (the women's voices, the lapsed, the non-episcopal voice) have never been tested against the Cyprian corpus by any round, and Round 1 listed some of them as unchecked.
2. I did not test the upstream chain behind HIGH-2 — **Doc_01 §2**, which Doc_03 cites as the origin of "not at the same office." I established that the Profile's claim is refuted at source and that Doc_03 and Doc_05 §4.1 carry the same error; where it originated is not my remit.
3. I did not re-run Doc_04's Confidence/Gravity Cross-Check for G1 against the now-read *Vita*, which the document itself says has not been re-run (line 58).

---

# Judgement: is this document adequate to proceed?

**Not yet — but it is close, and the gap is narrow and fully specified.**

Two HIGHs stand. Both are silences or negatives stated more widely than the sources allow, both sit in the document's ecological summary, and both feed the Capsule Core. Neither can be carried forward as a disclosed limitation, because in each case the document asserts the opposite of what a Native vendored source says — HIGH-1 against an approved input and against the document's own Section 2, HIGH-2 against a file this build has quoted from since Doc_03. A Representative built on 4D would not know that this world taught an account of failure and return to the people of Carthage; a Representative built on 4F would not know that Augustine's own congregation clamored him into the episcopate. Both are corrections of a sentence each, at five sites total.

The larger judgement is about the pattern, and the brief named it before I started. **This build's defect is not carelessness; it is that its negatives are written at one scope and its reading is done at another.** Round 2 fixed that at one sentence. This round found it at three more sites in the same source and one more in the same paragraph. The structural remedy is cheap and I would make it a condition of clearing: **read the whole *Vita Augustini*, all thirty-one chapters, and record it.** It is 3,600 English words beyond what has been read, it is Native, it is vendored, it is the richest single attestation this world has of its own Primary gravity, and it has now generated one HIGH, one MEDIUM and one LOW in a single scoped sweep of nine of its chapters and a keyword pass over the rest. The next reviewer should not have to find the fourth one.

With those two HIGHs corrected at all five sites, the two MEDIUMs discharged, and the *Vita* read through, I would expect this document to clear.

---

## Observed, out of scope

- The 4F fix creates a **new divergence from Doc_07 §2F** (which still states the presbyteral silence flatly) that the Disposition's *"One place was found where prior `lpc` documents disagree"* paragraph does not list alongside the Doc_08 2B-4 / Doc_09 §7 item 1 divergence it does list. Not investigated.
- HIGH-2's error is carried upstream at **Doc_05 §4.1** (*"not by a second acclamation"*) and **Doc_03 rows 29–30** (*"not a second popular acclamation"*), both of which cite **Doc_01 §2** as its origin. Flagged, not investigated.

---

## Document Log

| Date | Action |
|---|---|
| 2026-09-16 | Round 3 independent adversarial review (scoped to Round 2 NEW-1, NEW-2 and NEW-2's blast radius). 2 HIGH · 2 MEDIUM · 3 LOW. NEW-1 PARTIALLY FIXED; NEW-2 CONFIRMED FIXED at its own sentence, blast radius not clean. Verdict: REVISION REQUIRED. |
