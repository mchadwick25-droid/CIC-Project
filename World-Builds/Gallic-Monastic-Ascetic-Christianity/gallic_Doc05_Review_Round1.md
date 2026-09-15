# Doc_05 Review — Round 1 (independent adversarial)

**Document under review:** `gallic_Doc05_Ecological_Reconstruction.md` (DRAFT, Gallic Monastic-Ascetic Christianity, Atlas I.27)
**Reviewer:** independent adversarial reviewer, fresh context, no drafting involvement in Doc_01–Doc_05.
**Date:** 2026-09-10
**Method:** every quotation checked was located in the vendored file itself by direct search-and-context, not assessed for plausibility. Instruments: flattened `npnf211`/`npnf203` with `@@DIV` ids preserved (the same working copies the drafter used — file-line numbers below are that file's); the raw `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` for the *Institutes* VI check; `salvian_on-the-government-of-god_sanford1930.txt`; `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`; `eucherius-lyon_de-laude-eremi_migne-pl50.txt`; `faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt`. Governing text read directly: CF V7.4 ll. 278–417 and 654–665; Forces Framework V1.1 §4 (ll. 182–221) and §5 (ll. 224–241); Constitution Articles 20–23 (ll. 469–524); RCF v32 "Historical Containment" (ll. 92–104). Doc_01, Doc_02, the Source Registry (all 44 rows), Doc_03 (all 81 entries + §9–§11), Doc_04 (all sections) read in full. Approximately 115 quotations, loci, div ids and file-line ranges were checked.

---

## VERDICT

**SUBSTANTIAL REVISION REQUIRED — bounded.**

One-line reason: the evidentiary base is strong and the headline discovery is real, but **the four inhabited passages are the weakest layer of the document, not the strongest** — three of the four carry a defect the drafter's own Discipline 6 forbids, including the one thing Discipline 6 names as "the live risk" (a Gallic voice speaking Egypt's practice as its own); and the factual claim on which the Doc_04 §10 item 2 disposition is built — that *Institutes* XII.9–19 are "the last eleven chapters" and "the closing statement of the whole formation manual" — is false, as the document's own citation of *Inst.* XII.30 three sections later demonstrates.

**No Doc_04 classification needs reopening.** G3 stays Supporting at world level / Primary within the south; the §10C item 2 recommendation (annotate, do not reclassify) survives and, once re-grounded on *Inst.* XII.33, is actually stronger than the version submitted. No Doc_01–Doc_03 finding is overturned. One item belongs to the Registry owner rather than to this document (S6, row 39).

**Counts: 10 substantial findings, 13 cosmetic.**

The single most important: **S1** — inhabited passage 4 puts Eucherius's image of *Lérins the island* receiving the shipwrecked into Honoratus's arms, contradicting the document's own §2.1 and §7.1, because Registry row 26 (Eucherius, *De Laude Eremi*) was reused from Doc_04 without being re-read this pass, in direct breach of the document's own Discipline 2. The Latin subject is unambiguous: *"Lirinum meam … quae … piissimis ulnis receptat venientes"* (row 26, file lines 718–722).

---

## WHAT HELD UP (verified against source text, not assessed for plausibility)

Recording this at length, because it is the majority of the document.

**1. The headline finding is real, and it is genuinely new to this build.** *Institutes* Book VI is omitted from this edition. Verified twice, independently of the flattening: in the flattened copy at lines 18889–18893, and in the source XML itself at lines 21559–21567, where `<div3 title="Book VI. On the Spirit of Fornication." … id="iv.iii.vi">` contains exactly one paragraph — "We have thought best to omit altogether the translation of this book." — before `iv.iii.vii` begins. This is not a flattening artifact. The novelty claim also checks out: `grep` across every other build document returns no record of the omission; Doc_03's own entry at line 618 records Gibson's cross-reference "*Institutes* VI. viii." as pointing to "a book not read," and Doc_03 §10 item 3 lists "*Institutes* … VI–IX … XI–XII" among "Not read this pass" — exactly as §1.2 says, on the assumption that VI was present. The consequential second half — that Gibson's footnote at *Conf.* XVIII.15 (file lines 37389–37390, `iv.vi.ii.xv`) cites VI.8 for daily communion in Gaul, i.e. cites a chapter his own edition suppressed — is also verified, and §3's "Name-the-layer note" handles it correctly as an editor's claim at Inferential/Thin.

**2. Quotation accuracy is high, and file-line numbers are unusually precise.** Of ~115 checks, the only wording deviations found are C6 and C11 below; every other quotation is verbatim. Every div id is correct, including the one-ahead Sulpitius offsets (`ii.ii.vii` = *Vita* VI, `ii.ii.x` = IX, `ii.ii.xi` = X, `ii.ii.xx` = XIX, `ii.ii.xxvii` = XXVI) and the exact *Dialogues* ids. Spot-checked file-line claims all landed: *Ep.* III at 2010, 2011, 2020, 2022, 2026, 2032–2044, 2039, 2045, 2049–2052, 2058–2061, 2062; *Vita* IX at 743 (Ruricius) and 774 (the Psalter); *Dial.* III.10 at 4318–4327; `npnf203` line 35502 (Gennadius ch. XIX, "exhorting to love of God"); Salvian at 5016–5018 (IV.6, p. 109 — page header verified), 6316–6317 (V.4, p. 139), 6454–6463 (V.5, p. 142), 6475–6505 (V.6, p. 143); Sanford's Introduction at 852–857 (p. 12); Hilary of Arles at 449–462; the *Inst.* VI notice at 18889–18893.

**3. §11's read-scope claim for the office is exactly true.** "*Inst.* II.1–18 and III.1–12, read in full … file lines 14947–16292" — Book II has exactly 18 chapters (last div `iv.iii.ii.xviii` at 15597), Book III exactly 12 (`iv.iii.iii.xii` at 16257), and 16292 is the first line of `iv.iii.iv` (Book IV). The range is precisely Books II and III, neither padded nor short. Doc_04 §10 item 8 is genuinely discharged.

**4. The Faustus (row 24) grep report is exactly reproducible.** 23 case-insensitive hits for "lirin|lerin" in the whole file, all at lines ≤ 2764 or ≥ 28706 — none inside the treatise. The five chapter-heading loci named in §11 are real: 3718 (`QUOD PELAGIl SENSUS, QUl GRATIAM NEGAIJIT…`), 4097 (`CONTRA HOC, (H'OD UICUNT, QUIA PER SOLAM GRATIAM…`), 4344, 4427, 5536; and `INCIPIT DE SPIKITV «ANCTü LIBEK PKDIVS` at 8186 confirms the treatise's end. The renderings given are honest normalizations of that OCR and are labelled Inferential/Thin.

**5. The *Vita Antonii* / row 34 finding at §10C item 10 is correct in both halves.** Doc_01's current text returns **zero** hits for "Antonii", "Antony", "counterpart" or "Athanas". And the only two *Vita Antonii* references in the whole of `npnf211` are Gibson's, at 18425 ("S. Antony is said never to have eaten till sunset (Vita Anton.)") and 24548 ("given in the Vita Antonii of Athanasius") — both in the Cassian notes, neither in Roberts's Sulpitius apparatus. Reporting item 10 as *not resolved* while narrowing it this way is the right disposition.

**6. Registry discipline is clean on Excluded rows and on Salvian.** Nothing is drawn from rows 4, 33–38 or 44. Dialogue I is named three times, always to say it is not used. Row 33 (Hilary of Poitiers) is handled well at §1.4 — the exile is taken from *Vita* ch. VI as a force acting on Martin's body, with an explicit statement that none of Hilary's own teaching is imported. Row 36 (RB) appears only as a downstream-influence citation at §9B, consistent with Doc_01 §8.3 (RB 42 and RB 73's "the Conferences of the Fathers, their Institutes and their Lives"), and §7.2 correctly excludes Gibson's Benedictine office-names from the inhabited passages — verified: no "Lauds", "Prime", "Compline", "Rule", "abbot as canonical office" or "semi-Pelagian" appears in any of the four passages. **Row 43 (Salvian) never touches G3** — every Salvian use is forces, Human Ecology, Boundary, affect, or ministry-genre, exactly as its Licensed For allows.

**7. All eleven of CF line 658's dimensions are genuinely addressed, not merely tabled.** I checked each section against its mapping-table claim, and each is substantive: Formation Ecology (§2, with the bodily half at §1.2), Meaning Transmission (§6A, with all six of CF ll. 337–345's sub-items — teaching, memory, storytelling, apprenticeship, worship, authority structures — as separately bolded paragraphs), Emotional/Affective (§8, all four of CF ll. 359–365), Worship Integration (§3, all seven of CF ll. 366–376 answered in CF's own order), Authority Structures (§4), Boundary Structures (§7), Formation Logic (§2.4), Memory Structures (§6B), Interpretive Ecology (§6C), Representative Theological Patterns (§9A), Power/Influence/Historical Dynamics (§9B, all four of CF ll. 377–382). The Discipline 1 reconciliation of CF's two lists is a real methodological contribution and is disclosed as a reading rather than a governance change.

**8. §10A and §10B are genuine assessments, not restatements.** §10A carries both of CF ll. 388–396's axes as separate columns, and uses them to reach three findings the lens prose does not state (two over-weightings, three under-weightings, with the women's-presence row deliberately inverted in both directions). §10B answers every one of CF ll. 397–404's questions — strongest relationships, uncertain relationships, hub, tension points, central, peripheral — and its hub finding (the exemplar in two media) is a new claim, correctly flagged as diverging from Doc_04's Supporting classification of G5 and correctly handed to Doc_07 rather than used to reclassify.

**9. Forces integration is real in all three named lenses.** §1.4, §2.5 and §7.3 are separately labelled, multi-paragraph, and each connects back to Doc_01 §7, Doc_02 §11/§13A and named Doc_04 forces notations. All five Governing Principles are visibly at work, not merely listed: From-Within (barbarian ruin as "the present judgment of God"), Proportionality (§1.4's closing paragraph on the barbarian force is an exemplary application of Fw §5.2 — "the force that historians treat as the period's dominant one left, in this world's formation literature, one indignant book and one discharge scene"), Named Tension (Salvian's genre; Chadwick vs. Casiday, both carried unresolved), Cross-Cell Connection (§2.5(e)), and Transmission Specificity (§7.3's table, which is the best single piece of work in the document). The Forces Fw §4 Step 5 sentence is quoted exactly (l. 206, "Boundary Structures", not CF l. 663's "Boundary Ecology") — the divergence between the two governing texts is real and the document quotes the right one for the lens it builds.

**10. The one-world question is stated as input and not decided.** §10B's closing paragraph adds two genuinely new structural observations (same hub function, different media) and gives one to each side, then recommends the provisional status be kept operative — the same posture as Doc_04 §6, with no self-authorization. The Escalation Check routes it to Step 0.

**11. Doc_04 §10 items 8 and 9 are genuinely discharged.** Item 8: *Inst.* II–III read in full (verified above), with findings distributed across §3, §2.2 and §2.5(a) and a properly-bounded input to the deferred office candidate that quotes Doc_04 §2.2's own change-criterion verbatim and declines to apply a reclassification. Item 9: §1.3 follows Article 20's order of operations exactly — absence named first, twelve traces listed with layer and strength, bounded reconstruction that (with the exceptions at S9/S10) stays inside them, and a Facilitator-Governance hand-off actually recorded rather than promised. The refusal to reconstruct ordinary-believer psychology (§1.1's closing paragraph) is correct under Article 20 ll. 492/511.

**12. Doc_03 cross-references are accurate.** All ~35 lexicon entry numbers cited in Doc_05 were checked against Doc_03's headings; every one maps to the term Doc_05 names (1.5 cell, 1.7 elder, 1.8 junior, 1.9 profession, 1.11 renunciation, 1.12 the world, 1.13 the religious, 2.1 soldier, 3.1 disciple/master, 3.5 conference, 3.6 institutes/customs, 3.7 discretion, 3.8 disclosure, 3.11 lukewarmness, 4.1 purity of heart, 4.6 accidie, 4.8 compunction, 4.9 fear→hope→love, 4.10 contemplation/fourfold sense, 4.11 unceasing prayer, 5.8 Massilians, 5.9 Pelagians, 6.1 virtus, 6.3 blessing, 6.4 devil, 6.5 possessed, 6.7 illusion, 6.8 rustics, 6.9 Antichrist, 6.10 Salvian, 7.2 the rule, 7.3 novelty, 7.6 trial, 7.11 communion, 7.12 Apostolic See, 7.13 Commonitory, 7.14 Christology, 8.2 apostolic, 8.3 catechumen, 8.4 virginity, 8.6 dress, 8.8 Gaul). One tier value is wrong (C3); nothing else.

**13. The Article 23 literal failure signature is absent.** No inhabited passage contains a reference to "sources," "evidence," "scholars," "documentation," "reconstruction," or any equivalent analytical-distance marker. On that specific test the four passages pass cleanly. Their defects (S1, S2, S5) are of a different kind.

**14. Editorial-layer discipline is right in most of the places it matters.** Gibson's "Institutes VI. viii." footnote is named as editorial (§3); the Bethlehem identification at *Inst.* III.4 is correctly identified as Gibson's (verified — line 15897 is his note, not Cassian's text); Gibson's "seems to have originated in Gaul" is named editorial; Sanford's Introduction is named editorial and rowless at §1.1, §1.3 trace 12 and §10D item 9; Gibson's XII.14 headnote ("perilously near semi-Pelagianism") is quoted as an editor's, not a voice; Engelbrecht's Prolegomena is named as the location of every Faustus "Lirin" hit. Three exceptions are S6, S7 and S8 below.

---

## SUBSTANTIAL FINDINGS

### S1. Inhabited passage 4 transfers Eucherius's image of *Lérins* to *Honoratus* — and the underlying source was never re-read this pass, in breach of the document's own Discipline 2

**Locus.** §8, "Inhabited passage (Layer 2) — Lérins, a man newly come from the world," sentence 3: "**Honoratus took the shipwrecked in his arms — that is how they say it of him**"; and its anchor line, "Eucherius, *De Laude Eremi* ('Lirinum meam … piissimis ulnis receptat,' Doc_04 G2, Inferential/Thin wording)."

**What's wrong.** The subject of the Latin is the island, not the man. `eucherius-lyon_de-laude-eremi_migne-pl50.txt` lines 718–722: *"…Lirinum [Vulg. Lerinam] meam honore complectens, **quae** procellosi naufragiis mundi effusos, piissimis ulnis receptat venientes…"* — the feminine relative *quae* takes *Lirinum/Lerinam* as antecedent; Honoratus appears six lines later in a separate clause and a separate role (*"Digna quae … Bonorato auctore fundata sit"* — worthy to have been founded with Honoratus as its author). Doc_05 itself gets this right twice elsewhere: §2.1 ("Eucherius's Lérins as the harbour that 'receives with most loving arms those cast out by the shipwrecks of the stormy world'") and §7.1 ("Lérins an island that 'receives … those cast out by the shipwrecks of the stormy world'"). The inhabited passage contradicts both, and it does so in the layer where Article 23 says a formed person must recognize the account as true.

**Root cause, which is the more serious half.** Discipline 2 states: "every quotation *reused* from those documents to support a new claim in a new context was re-read at its locus before reuse (the loci are listed in §11's search_record)." Registry row 26 (Eucherius, *De Laude Eremi*) appears nowhere in §11's search_record and nowhere in §0's "Built from" list of files read this pass — yet row 26 material is used at §2.1, §7.1, §7.2, §8's inhabited passage and its anchor line. The quotation was reused in a new context without re-reading, and the reuse introduced an error. This is precisely the failure Discipline 2 exists to prevent, and it is the first demonstrated instance in this build of the rule being stated and then not applied.

**How verified.** Direct read of `eucherius-lyon_de-laude-eremi_migne-pl50.txt` lines 712–730 and 440–458; cross-check against Doc_04 §3 G2's own rendering (which correctly assigns the image to Lérins) and against `gallic_Doc04_Review_Round1.md`'s independent verification of the same lines.

**Remedy.** (a) Rewrite the sentence to the island: e.g. "The island took me in its arms — that is how they say it of the place." (b) Add a row 26 line to §11's search_record recording what was actually read this pass, or state plainly that row 26 material is carried from Doc_04 unre-read, and amend Discipline 2 accordingly rather than leaving a rule the document does not meet. (c) Add row 26 to §10D item 13's proposed Verification-Note extensions (see C9).

---

### S2. Inhabited passage 3 fails the cross-world containment test the document itself calls "the live risk" — a Gallic voice claims Egyptian observance that Cassian's own text says Gaul does *not* keep

**Locus.** §3, "Inhabited passage (Layer 2) — the night office, in the words the south used for it," and its Cross-world check.

**What's wrong.** Discipline 6 commits the document to this: "the inhabited southern voice **always** speaks of purity of heart, discretion, the twelve psalms, and the faults as *what the fathers of Egypt handed down and Cassian brought to us*, never as what Gaul devised." Passage 3 does the opposite. It is fixed in Gaul by its own sentence — "they do not do that in the East, **but we do**" — and then renders, as the speaker's own house practice in the first person plural, a series of observances that *Institutes* II presents explicitly as **Egyptian**:

- "the rest of us sit low, because we have fasted and worked all day" — II.12 (`iv.iii.ii.xii`, 15427–15434): "**they** all, except the one who stands up in the midst … sit in very low stalls … For **they** are so worn out with fasting and working all day and night," described as "after their custom," i.e. the Egyptians'.
- "no one coughs, no one sighs aloud … a yawn is not [forgiven]" — II.10, whose chapter title is "Of the silence and conciseness with which the Collects are offered up **by the Egyptians**" (15305–15306).
- "Between the verses we rise and pray standing, hands out, and go down to the ground only for a breath, and up when he who collects the prayer rises, **not before and not after**" — II.7 (15183–15228). This is the sharpest failure. II.7's own text sets that discipline **against** Gallic practice: "when the Psalm is ended **they** do not hurry at once to kneel down, **as some of us do in this country, who, before the Psalm is fairly ended, make haste to prostrate themselves for prayer, in their hurry to finish the service**." The passage therefore has a Gallic monk claiming as his own the very practice Cassian's text says Gauls fail at — and the passage's *other* sentence ("He says we hurry to fall on our faces to get the service over," in passage 2) shows the drafter knew this.

The passage's own Cross-world check asserts the opposite of what the passage does: "the Egyptian content is what Cassian prescribes; the only Gallic-owned element is the Gloria." Prescription is exactly the point — the passage narrates it as description of the speaker's own house.

**Why this is substantial rather than cosmetic.** RCF l. 98's cross-world contamination item, Discipline 6's own framing, and the drafter's own review requirement (d) all single this out as the test to apply. The passage is the one place the document's Egypt/Gaul discipline is load-bearing and the one place it is not held.

**Remedy.** Two options, either acceptable: (i) re-voice the passage as a Marseilles junior *reading* the book — "This is how the fathers of Egypt keep the night, and what we are told to keep" — preserving every anchor while restoring the received frame; or (ii) keep the "we" but confine it to what Cassian's text actually attests of Gaul (the Gloria, the hurried prostration, the return to bed, the office "generally celebrated … in the monasteries of Gaul" at III.4) and mark the rest as what is prescribed. Option (i) is closer to what §2.1 already establishes about the southern formative relationship ("two relationships at once: to a present elder whose Gallic practice we cannot see, and to an absent Egyptian father whose words are on the page").

---

### S3. The *Institutes* XII claim that carries the Doc_04 §10 item 2 disposition is factually wrong, and the document contradicts itself about it three sections later

**Locus.** §2.4 (v): "*Institutes* XII, the last book, on pride, turns at ch. IX into a treatise on grace … and **the closing frame** — 'This then is that humility towards God…' (XII.19)"; and, load-bearing, §10C item 2: "occupying **the last eleven chapters of the *Institutes*** (XII.9–19) as the remedy for the eighth fault and **the closing statement of the whole formation manual**"; and §2.4 (v)'s inference, "the formation program **ends** by teaching the monk to attribute his own formation to God — G3 is the formation logic's **final move**."

**What's wrong.** *Institutes* Book XII has **thirty-three** chapters. Divs `iv.iii.xii.xx` (line 22030) through `iv.iii.xii.xxxiii` (line 22389) follow XII.19; XII.33's own title is "Remedies against the evil of pride," and the *Institutes* end at line 22410, immediately before `iv.iv` (the *Conferences*). XII.9–19 are therefore neither the last eleven chapters of the work nor its closing statement, and XII.19 is not a closing frame — fourteen chapters follow it. The document knows this: §2.5(c), §4.4 and §7.3 all cite "*Inst.* XII.30, title" (verified at `iv.iii.xii.xxx`, lines 22317–22320), a chapter that cannot exist if XII.19 closes the book.

**The remedy strengthens the finding it damages.** *Inst.* XII.33's actual last sentence (lines 22405–22410) reads: "Then, next after this we must keep a firm grasp of this same humility towards God: which we must so secure as not only to acknowledge that we cannot possibly perform anything connected with the attainment of perfect virtue without His assistance and grace, but also truly to believe that this very fact that we can understand this, is His own gift." The *Institutes* do in fact end on the grace-and-humility teaching — so §2.4(v)'s substantive thesis survives, and §10C item 2's "annotate, do not reclassify" recommendation survives with it. What does not survive is the arithmetic used to support it, and the claim rests on a chapter the drafter did not read.

**How verified.** Full div enumeration of `iv.iii.xii.*`; direct read of XII.19's title and text (22013–22029), XII.20–XII.23's titles, and XII.33 in full (22389–22410).

**Remedy.** In §2.4(v) and §10C item 2, replace "the last eleven chapters" with "eleven chapters (IX–XIX) of a thirty-three-chapter book," replace "the closing statement of the whole formation manual" and "the closing frame" with an accurate description, and add XII.33's own closing sentence — read this time — as the genuine terminus. Record XII.20–33 as read or as still unread in §11, whichever is true.

---

### S4. §2.1's insider-Latin evidence for **Lérins** comes from a passage that precedes Lérins in its own source and describes two men, not one — and §1.1 says so

**Locus.** §2.1, "**Lérins: formation by a founder, a succession of teachers, and a household.** The bounded evidence: Honoratus's 'anxious guardianship over the salvation of those who had bound themselves over to their teaching' (*"sollicita custodia erga eorum salutem qui se doctrinae eorum mancipaverant,"* Hilary, file line 461, my rendering, Inferential/Thin) — the disciple as one who has *mancipated* himself".

**What's wrong, in two parts.**
(a) *Location.* The phrase sits at `hilary-arles_…_migne-pl50.txt` lines 460–462, inside **CAPUT II**, whose own heading at lines 414–418 reads "Cum Venantio fratre peregrinatur. — Hujus obitus. — Honoratus et Venantius patria abscedunt. — Peregrinationes ad loca sacra." Venantius's death and funeral at Methone are narrated at 555–566; Honoratus's arrival at Lérins is **CAPUT III**, whose heading at 604–608 reads "Honoratus, fratre mortuo, venit in Italiam … — **Lirinam insulam ingreditur**." The disciples "who had bound themselves over to their teaching" are therefore pre-Lérins, in the brothers' homeland, before the island existed as a community.
(b) *Person.* The Latin is dual throughout the surrounding passage — *illos* (449), *eorum vita* (452), *alter alterum* (453), *utrumque* (456), *illorum gravitas* (457), *eorum salutem qui se doctrinae **eorum** mancipaverant* (461). It is about Honoratus **and Venantius**, not Honoratus alone.

The document's own §1.1 states both facts correctly — "of Honoratus and his brother Venantius **in their first ascetic years**" — and §1.3 trace 11 likewise ("Hilary of Arles **on Honoratus and Venantius**"). §2.1 contradicts both.

**Why it matters.** §10A rates Lérins's internal life the ecology's "most consequential and least documented" dimension. Removing this phrase makes the Lérins column of §2.1 thinner still — which is the honest result, and one §10A and §10D item 7 already anticipate.

**How verified.** Direct read of the Latin file, lines 405–470, 555–585 and 600–625, including both chapter headings.

**Remedy.** Move the phrase out of the Lérins block to §1.1's pre-Lérins account (where it already sits correctly), or retain it in §2.1 explicitly labelled as pre-Lérins and dual ("of Honoratus and Venantius before the island"), and adjust §2.1's Lérins evidence-list accordingly. §10A's "**under**, seriously" rating for Lérins should be restated as resting on Vincent's one sentence, Sanford's editorial paraphrase, and the Gennadius/Hilary attestations of the *episcopate* only.

---

### S5. Inhabited passage 2 states as an in-world fact something its own anchors do not support, and adds one invented physical detail

**Locus.** §2.4's second inhabited passage, sentences 1 and 3.

**(a) "We in this country do not keep even the year in the guest-house; Cassian says he cannot remember one of us who did."** Anchor: *Inst.* IV.2. IV.2 (`iv.iii.iv.ii`, lines 16321–16334) does not concern the guest-house. Its subject, stated in its own chapter title and first sentence, is the Egyptians' "untiring perseverance and humility and subjection, — how it lasts for so long … till they are bent double with old age; for it is so great that we cannot recollect any one who joined our monasteries keeping **it** up unbroken even for a year." The antecedent of "it" is the perseverance-and-humility of IV.1–2 (set against Tabenna's obedience, "what no one among us would render to another even for a short time"), not the probationary year, which is introduced only five chapters later at IV.7 — where Gibson's own note observes that "Cassian stands alone in mentioning a full year as the duration of this service." The inhabited voice therefore asserts a specific Gallic institutional failure that no text attests.

Doc_04 G2's looser gloss ("of the Egyptian probation") is the origin of the drift; Doc_05 hardens it into a factual sentence in the inhabited layer and then reuses that hardened form four more times (§2.5(a), §3's closing paragraph "the unkept year (IV.2)", §7.3's table row, §10A's "if Cassian's Gallic uptake was as thin as IV.2 admits", §10B's "IV.2 says not for a year").

**(b) "The fathers of Egypt lay ten days at the door and were spat on."** Anchor: *Inst.* IV.3. IV.3 (16339–16349) says the postulant lies outside the doors "for ten days or even longer," is "prostrate at the feet of all the brethren that pass by, and of set purpose **repelled and scorned** by all of them," and is "covered with many **insults and affronts**." There is no spitting. Discipline 6 states each passage "contains nothing invented to fill a gap"; this is a small invented physical detail in the most vivid position in the sentence — exactly the failure mode CF's own Tier 5 prohibition ("a generated story, however well-intentioned, is not witness") is written against.

**How verified.** Direct read of *Inst.* IV.1–IV.9 (16296–16520) in full.

**Remedy.** (a) Restate the sentence to what IV.2 says — e.g. "We do not keep up what they kept up; Cassian says he cannot remember one of us who held to it unbroken even a year" — and correct the four downstream restatements to match. (b) Replace "were spat on" with the text's own "were turned away and scorned."

---

### S6. §2.2's only Lérins evidence in the "Cell" row is Cardinal Noris's sentence attributed to Heurtley — and it re-imports a claim the Registry deliberately de-licensed

**Locus.** §2.2 table, "Cell" row, Lérins column: "Heurtley (editorial, `iii.i`): 'the whole island … built over with cells … one monastery' (Doc_03 1.5)."

**What's wrong.** In `npnf211` at `iii.i` the Latin appears at lines 10336–10344 and carries its own attribution one line later: *"Tota ubique insula, exstructis cellulis, unum velut monasterium evasit."* — **"Cardinal Noris, Histor. Pelag. p. 251."** It is not Heurtley's sentence; Heurtley is quoting a 1673 controversialist. That is Registry **row 39**, a Secondary source at Confidence C.

Worse, row 39's Licensed For was rewritten at Doc_02 Round 2 finding N16 for exactly this reason: "the two specific Doc_02 claims this row previously licensed (the Vincent-Massilian 'non modo Semipelagianum' reading and **the Lérins-as-cells quotation**) were both removed from Doc_02 … updated to match — **general reference only, not a specific licensed claim**, until Doc_02 next draws on him directly." Doc_05 re-imports the de-licensed quotation, mislabels its author, and makes it the sole content of a cell in the document's central comparative table — the one place a downstream builder will look for what Lérins's daily life looked like.

Doc_03 1.5 is the proximate source of the drift (it cites the Latin to "Heurtley's Introduction `iii.i`" as a *lemma locus* for *cella*, which is defensible for that narrow purpose); Doc_05 promotes it from lemma witness to substantive ecological evidence without re-checking the attribution.

**How verified.** Direct read of `npnf211` lines 10328–10348; cross-check against Registry row 39 and Doc_02's document log.

**Remedy.** Either drop the cell to "not attested" (consistent with every other Lérins cell in the same table), or retain it labelled as *Noris (1673), quoted by Heurtley — Registry row 39, general reference only*, and flag the Licensed For question for the Registry owner in §10D.

---

### S7. §2.1 states the editorial Lérins/abbot identification as documented fact — the exact claim Doc_02 Round 2 N4 withdrew and Registry row 9 was rewritten to prevent

**Locus.** §2.1, end of the Lérins paragraph: "the *Conferences* XI–XVII were dedicated to **its abbot** (row 9), which is **the only documented traffic in formation-content between the two southern houses**."

**What's wrong.** Registry row 9's Licensed For says the opposite, in bold: "**Cassian's own text names two 'holy brothers,' one presiding over 'a large monastery' — unnamed. The Lérins/abbot identification is the editorial apparatus's (row 17), independently corroborated only for Lérins's own existence by Gennadius's Vincentius chapter (row 30), not for the Cassian-dedication link itself** (Round 2 N4 — the prior revision's 'doubly evidenced' claim … is withdrawn)." What Cassian's own text supports (per Doc_04 §3 G1, verified) is a dedication to Honoratus and Eucherius, one of them presiding over a large monastery. That the monastery is Lérins is Gibson's and Heurtley's. Calling it "**its** abbot" and "the only **documented** traffic" restores the withdrawn claim at full strength, in a document whose Discipline 3 promises the editorial layer will be named "wherever drawn on."

**How verified.** Registry row 9 read in full; Doc_02 §15 document log (Round 2 N4 entry); Doc_04 §3 G1 evidence line and the Doc_04 Round 1 reviewer's independent confirmation of *Conf.* Pref. II/III.

**Remedy.** Restate as: "the *Conferences* XI–XVII are dedicated to two 'holy brothers,' one of them presiding over a large monastery (Cassian's own text); the identification of that house as Lérins is the editorial apparatus's (row 17, row 9's own caveat)." Adjust "the only documented traffic" to "the only traffic in formation-content the sources point to, at editorial strength for the Lérins identification."

---

### S8. "The Gloria after every psalm … repeated dozens of times a day" is Gibson's reading, presented as Cassian's, and Cassian's own clause points the other way

**Locus.** §3, "How worship shapes theology" (ii): "The Gallic Gloria — sung 'with a loud voice' by all **after every psalm**, a practice Cassian says the East never heard (II.8; Gibson's note that it 'seems to have originated in Gaul' is editorial) — is a Trinitarian confession **repeated dozens of times a day in this province specifically**." Same phrase at §2.5(a).

**What's wrong.** *Inst.* II.8 (`iv.iii.ii.viii`, 15232–15243) reads: "while **one sings to the end of the Psalm**, all standing up sing together with a loud voice, 'Glory be to the Father …' — we have never heard anywhere throughout the East … But with this hymn in honour of the Trinity **only the whole Psalmody** [*Antiphona*] **is usually ended**." Gibson's note at 15243–15250 supplies the "after every Psalm" reading, and does so as a contrast with the Eastern καθίσματα/στάσεις arrangement — his words, not Cassian's, and Gibson's own note at 15239–15242 warns that *Antiphona* here means "the whole of the Psalmody of the office," which cuts against a per-psalm reading. The document names one Gibson claim at this locus as editorial and silently adopts a second one at the same locus, then builds an arithmetical claim ("dozens of times a day") and a theological finding ("a Trinitarian confession repeated dozens of times a day in this province specifically") on it. This is the build's signature failure mode operating in the one section where worship is said to shape theology.

**How verified.** Direct read of *Inst.* II.8 with Gibson's full note (15229–15252).

**Remedy.** State what the text says — the Gloria, sung by all in a loud voice, ends the psalmody in this country and was never heard in the East — and add, separately labelled, that Gibson reads the Gallic custom as after every psalm. Drop "dozens of times a day," or re-derive it from whichever reading is adopted and label it as this document's inference.

---

### S9. §1.3 trace 1 attaches a house-name absent from its ancient source and rates it above Doc_01's own confidence

**Locus.** §1.3(b) trace 1: "**Saint-Sauveur, Marseilles** — 'one for men and one for women, which are still standing' (Gennadius ch. LXII, ancient text, c. 495). **Documented**."

**What's wrong.** Gennadius ch. LXII (`npnf203` lines 36028–36029) reads: "a presbyter at Marseilles, founded two monasteries, that is to say one for men and one for women, which are still standing." It names no house. "Saint-Sauveur" comes from Doc_01 §4, where the identification (Saint-Sauveur alongside Saint-Victor) is rated **[Widely Accepted]**, not Documented, and is not sourced to any Registry row. Doc_05 fuses the two and stamps the result "Documented."

**Why it matters here specifically.** §1.3(b)'s stated purpose is that "a reviewer can check that nothing below exceeds them," and the drafter's own review requirement (f) asks for exactly this check. A trace list whose first entry silently upgrades a confidence rating and imports an unsourced proper name undercuts the discipline the section is built to demonstrate.

**Remedy.** Split the trace: "**A women's house at Marseilles** — Gennadius ch. LXII, ancient text, **Documented**. (Its identification as Saint-Sauveur, alongside Saint-Victor, is Doc_01 §4 at **Widely Accepted**, without a Registry row of its own — carried at that strength, not this one.)"

---

### S10. §1.2 and §1.3 trace 9 over-read the single word "sex" at *Inst.* V.5 as the rule contemplating women's houses

**Locus.** §1.2: "*Inst.* V.5 … **new this pass**; the word 'sex' is one of the few places Cassian's rule **visibly contemplates women's houses**, and is carried to §1.3." §1.3 trace 9: "**Cassian's dietary rule contemplating 'sex'** (*Inst.* V.5, new) … the rule knows women exist near the men's house."

**What's wrong.** *Inst.* V.5 (`iv.iii.v.v`, 17782–17810) is titled "That one and the same rule of fasting cannot be observed by everybody," and its whole subject is variation in fasting capacity: "a difference of time, manner, and quality of the refreshment in proportion to the difference of condition of the body, the age, and sex," followed by examples of sickness, old age, beans, vegetables, dry bread and weights of food. Nothing in the chapter concerns women's houses, women near the monastery, or any female subject. The claim that the rule "visibly contemplates women's houses" is an inference from one word in a list of three, and the §1.3 restatement ("knows women exist near the men's house") is carried by *Inst.* IV.16's "familiarity with women," not by V.5.

Article 20's secondary duty permits bounded reconstruction "only on independent positive evidence, never inferred from silence." One word in a fasting-capacity clause is not positive evidence for a women's house; and §1.3(b) is precisely the place where the evidentiary floor is meant to be exact.

**How verified.** Direct read of *Inst.* V.5 in full.

**Remedy.** Keep the trace, downgrade the gloss: "*Inst.* V.5's fasting rule varies by 'the condition of the body, the age, and sex' — the one place in the dietary rule where a female subject is contemplated at all, in a chapter about fasting capacity and not about women's communities. Documented as text; what it implies about women's houses is not stated and is not inferred here." Delete "visibly contemplates women's houses" from §1.2. §1.3(c)'s bounded reconstruction does not depend on this trace and needs no change.

---

## COSMETIC FINDINGS

**C1. §2.4(iv) ellipsis removes the Egyptian frame from *Inst.* II.3.** The document quotes "monasteries stand 'not … at the fancy of every man who renounces the world, but through a succession of fathers and their traditions'." The text (15004–15008) begins "And so **throughout the whole of Egypt and the Thebaid**, where monasteries are not founded at the fancy of every man…". In a section on "the world's own account of why this works," and in a document whose containment discipline turns on keeping Egyptian content marked as Egyptian, the elided clause is the one that matters. *Remedy:* restore it.

**C2. §2.3 lists the *Inst.* II.5 "lukewarm" phrase as a communal expectation; it is a description of the primitive Church.** "the monastery must not become 'lukewarm by being dispersed among the many' (II.5, `iv.iii.ii.v`, new)". The text (15109–15112) reads: "At that time, therefore, when the perfection of the primitive Church remained unbroken … and when the fervent faith of the few had not yet grown lukewarm by being dispersed among the many, the venerable fathers … met together." It is a historical clause setting the scene for the twelve-psalm decision, not a rule imposed on a monastery. The claim survives on *Inst.* IV.6, which the same sentence already cites. *Remedy:* drop the II.5 half or restate it as the primitive-Church frame it is.

**C3. §6C item 4's tier is wrong.** "The fourfold sense … held at **Tier 3** by Doc_03 pending this lens." Doc_03 4.10, which carries the fourfold sense (*Conf.* XIV.1–3, 8), is rated "**Tier (est.). 2**". *Remedy:* correct to Tier 2.

**C4. §10C item 10 names the wrong Registry column.** "Registry row 34's **Comparandum Note** attributes the analogy to 'Doc_01 §2.1…'". In the Registry's own column order (# / Source / Type / Confidence / Boundary / Exclusion Reason / Licensed For / Verification Note / Comparandum Note / Discovery), that sentence sits in the **Verification Note**; the Comparandum Note is the "A builder or the Representative must not borrow imagery…" cell. The finding itself is correct; only the column name is wrong, and §10D item 5 will send the Registry owner to the wrong cell. *Remedy:* rename the column.

**C5. §10C items 2 and 12 over-read a single-lemma grep, and do not actually answer Doc_04 §10 item 12.** "A bounded grep of row 24 … finds no occurrence of 'Lirin/Lerin' in *De gratia*'s own text … **so row 24 cannot supply a Lérins self-location even when read**" — a negative on two spellings of one place-name does not exclude a self-location by other means (*insula*, *in monasterio*, a named abbot). And the fallback, "its date (c. 473–475) is post-window regardless, so Doc_04 §10 item 12's hope … is answered: it cannot, on chronology alone," does not answer Doc_04, which already recorded the post-window date at G3's Persistence test and still called row 24 "the one primary source that could actually settle whether Lérins attests G3 inside the window" — presumably because a post-window text can report in-window teaching. *Remedy:* soften to "this grep cannot show a self-location; a proper read remains owed (§10C item 12 already says so)," and drop the claim that item 12 is answered.

**C6. §6A substitutes words inside what reads as a quotation.** "'Never,' **said the one**, 'has the sun seen me eating,' 'nor me angry,' said the other. (V.27…)". The text at 18489–18490 reads "'Never,' said **he**, 'has the sun seen me eating,' 'nor me angry,' said the other." *Remedy:* restore "said he," or move the disambiguation outside the quotation.

**C7. §2.5(a) over-claims novelty.** "These are **ancient, first-person statements about Gallic monastic practice c. 420 — the first such direct evidence this build has found outside Sulpitius**." Two of the four items (*Inst.* IV.2; and, on climate, I.10 and IV.10–11) were already located and used by Doc_04 §3 G2 and are recorded in Registry row 7. II.7, II.8, III.4 and III.5 are genuinely new; the blanket claim is not. *Remedy:* restrict the novelty claim to the four office loci.

**C8. §7.3's table mis-states the *npnf101* omission policy.** "Letters 221–226 (Prosper's and Hilary's reports) | NPNF I.1's editors (row 31) | declared, general policy — **not Augustine's own letters**." Per Registry row 31 and `npnf101`'s Prefatory Note, that reason covers **225–226** only; 221–224 are Augustine's own and were omitted as "miscellaneous smaller letters." *Remedy:* split the cell's reason, as row 31 already does.

**C9. §10D item 13 omits row 26 from the proposed Verification-Note extensions.** Rows 7, 3, 1, 2, 10, 9, 43, 27 and 24 are listed; row 26 (Eucherius, *De Laude Eremi*) is not, although §2.1, §7.1, §7.2, §8 and the fourth inhabited passage all rest on it — and row 26's Licensed For still reads "Not yet examined beyond location," which licenses no content use at all. (Doc_04 §9 proposal 2 already flagged rows 26 and 27 together; Doc_05 carries forward only 27.) *Remedy:* add row 26 with an explicit note that its content is carried from Doc_04, not re-read here — see S1.

**C10. §10D item 13's row 7 extension over-states what was read.** "row 7 (*Inst.* II, III, **V**, XII.9–19, IV.3–9, IV.16–20, X.2 now read)". §11's own search_record says "V.1–28"; Book V has forty-one chapters (`iv.iii.v.xli` is Book VI's `prev`). *Remedy:* write "V.1–28."

**C11. The Latin at §1.1, §1.3 trace 11 and §2.1 is silently normalized from OCR.** The file reads *"Pervenire **illig δὰ** ignobilitatem et paupertatem non licebat: quanto magis eorum vita **abseondebatur**, tanto magis fama **emicabet**"* (450–453); *"quam **rera** feminarum visitatio etiam pro-|ximarum"* (458–459); *"quam sollicita **custedia** erga eorum salutem qui se **doctrine** eorum mancipaverant"* (460–462). The document's emendations are all correct Latin and the rendering is disclosed as the drafter's own, but the italicized Latin is presented in a form no reader will find by grepping the file, which is the check §1.1 invites ("presence checkable at file lines 447–462"). *Remedy:* add one clause — "Latin normalized from the OCR; the file's own readings differ in spelling" — or give the OCR forms in brackets.

**C12. §4.1 mislabels Sanford's layer in the conservative direction.** "'master of bishops, doctor of the churches' (Eucherius's phrase, quoted by Sanford — **editorial paraphrase**, p. 12)". At line 861 Sanford is quoting Eucherius directly, not paraphrasing him; the paraphrase label belongs to the tutelage-chain sentence at 852–857. The error under-claims rather than over-claims, but the layer discipline should be exact in both directions. *Remedy:* "quoted, not paraphrased, by Sanford (editorial layer, no Registry row)."

**C13. Two trivial internal line-range inconsistencies.** §3 cites *Vita* ch. IX at "file lines 770–787" while §11's search_record gives "lines 766–787"; §1.1 gives the Hilary window as "447–462" while §11 gives "428–462." Neither affects a claim. *Remedy:* reconcile.

---

## WHAT I VERIFIED AGAINST SOURCE TEXT vs. ASSESSED ONLY FOR INTERNAL CONSISTENCY

**Verified against source text:** all *Institutes* quotations in §1.2, §2.1–2.5, §3, §4.1–4.3, §6A–6C, §7.1–7.3, §8 (Books I–V, X, XI.14, XII); *Conferences* I.4/I.7/I.20, III.19, IX.2, XI.2/XI.4/XI.6, XIII.1/7/13/16/18, XIV.7/XIV.8, XV.6/XV.7, XVIII.1/XVIII.15, Prefs. I–III; *Commonitory* chs. 1, 2, 3, 22, 24, 28, 32; *Vita* chs. IV, VI, IX, X, XI, XIII, XIX, XXV, XXVI; *Ep.* I–III; *Dial.* II.2, II.11, II.12, III.6, III.10; Gennadius chs. XIX and LXII; Salvian IV.6, V.4, V.5, V.6; Sanford's Introduction p. 12; Hilary of Arles 405–470, 555–625; Eucherius §27 and the *Lirinum meam* paragraph; Faustus's whole-file grep and five heading loci; the *Institutes* VI omission in both the flattened text and the source XML; the Gibson footnotes at *Inst.* II.7, II.8, III.4, IV.7, IV.17, XII.14 and *Conf.* XVIII.15.

**Assessed only for internal consistency and against the prior build documents (not independently re-derived):** Doc_04's ten classifications and Interaction Matrix (out of scope; not reopened); Doc_01 §2.4's Mathisen consolidation (row 20, thesis level, unread by anyone in this build); Doc_02 §1.2's transmission history (Prosper, Celestine, Dionysius Carthusianus) as reported from Gibson's prolegomena; Doc_03's tier estimates apart from 4.10; the Chadwick/Casiday chronology; Registry row 31's letter-count reconciliation; Stancliffe (row 18, unvendored).

**Not checked:** *Conf.* IX–X, XXI (unread by the document and by me); *De Incarnatione*; Eucherius *De Contemptu Mundi* (row 25); Prosper (rows 28–29); *Contra Collatorem* (row 32, unvendored).

---

## SUMMARY

| # | Finding | Locus in Doc_05 | Class | Reopens a classification? |
|---|---|---|---|---|
| S1 | Eucherius's *Lérins* image given to Honoratus in inhabited prose; row 26 reused without the re-read Discipline 2 requires | §8 inhabited passage 4 + anchors; §11 search_record | Substantial | No |
| S2 | Inhabited night-office passage voices Egyptian observance as Gallic "we," including the practice *Inst.* II.7 says Gaul fails at | §3 inhabited passage 3 | Substantial | No |
| S3 | "*Inst.* XII.9–19 = the last eleven chapters / the closing statement" is false; Book XII has 33 chapters; XII.30 cited elsewhere in the same document | §2.4(v), §10C item 2 | Substantial | No — the disposition survives, re-grounded on XII.33 |
| S4 | Lérins insider-Latin evidence is pre-Lérins (CAPUT II) and dual (Honoratus + Venantius); §1.1 says so, §2.1 does not | §2.1 | Substantial | No |
| S5 | Guest-house-year claim misreads *Inst.* IV.2; "spat on" invented beyond IV.3 | §2.4 inhabited passage 2; restated at §2.5(a), §3, §7.3, §10A, §10B | Substantial | No |
| S6 | Lérins "Cell" evidence is Noris's sentence (row 39, de-licensed) attributed to Heurtley | §2.2 table | Substantial | No — Registry owner's item |
| S7 | Editorial Lérins/abbot identification stated as "documented," reversing Doc_02 Round 2 N4 and Registry row 9 | §2.1 | Substantial | No |
| S8 | "Gloria after every psalm / dozens of times a day" is Gibson's reading, unlabelled; Cassian's clause points otherwise | §3 (theology), §2.5(a) | Substantial | No |
| S9 | Trace 1 imports "Saint-Sauveur" and upgrades Doc_01's [Widely Accepted] to "Documented" | §1.3(b) trace 1 | Substantial | No |
| S10 | "sex" at *Inst.* V.5 over-read as the rule contemplating women's houses | §1.2; §1.3(b) trace 9 | Substantial | No |
| C1 | Egyptian frame elided from *Inst.* II.3 quotation | §2.4(iv) | Cosmetic | No |
| C2 | *Inst.* II.5 "lukewarm" clause is about the primitive Church, not a monastic expectation | §2.3 | Cosmetic | No |
| C3 | Fourfold sense given as Doc_03 Tier 3; Doc_03 4.10 says Tier 2 | §6C item 4 | Cosmetic | No |
| C4 | Row 34's stale pointer is in the Verification Note, not the Comparandum Note | §10C item 10, §10D item 5 | Cosmetic | No |
| C5 | Single-lemma grep over-read; Doc_04 §10 item 12 not actually answered | §10C items 2, 12 | Cosmetic | No |
| C6 | "said the one" substituted for the text's "said he" inside a quotation | §6A | Cosmetic | No |
| C7 | "first such direct evidence outside Sulpitius" over-claims (IV.2, I.10 already in Doc_04) | §2.5(a) | Cosmetic | No |
| C8 | *npnf101* omission reason applies to 225–226 only | §7.3 table | Cosmetic | No |
| C9 | Row 26 omitted from proposed Verification-Note extensions though relied on throughout | §10D item 13 | Cosmetic | No |
| C10 | Row 7 extension says "V" read; §11 says V.1–28 of 41 | §10D item 13 | Cosmetic | No |
| C11 | Latin silently normalized from OCR while inviting a grep check | §1.1, §1.3 trace 11, §2.1 | Cosmetic | No |
| C12 | Sanford's direct quotation of Eucherius called an "editorial paraphrase" | §4.1 | Cosmetic | No |
| C13 | Two line-range inconsistencies (*Vita* IX; the Hilary window) | §3 vs §11; §1.1 vs §11 | Cosmetic | No |

**Pattern across the substantial findings.** Seven of the ten (S1, S2, S4, S5, S6, S7, S8) are the same underlying failure in different clothes: *material carried forward from a prior document, or from an editor's note, without being re-read at its own locus* — and in five of those seven the carried material was then hardened into a stronger claim than its source supports. This is the build's documented recurring failure mode, and it has now migrated from the evidentiary layer (where Doc_01–Doc_04 caught it) into the **inhabited layer**, where it is harder to see and more consequential, because inhabited prose is what Doc_10 will inherit. The three inhabited passages with defects (S1, S2, S5) all fail in the same direction: toward vividness. That is worth naming as a standing risk for Doc_06–Doc_10, not only as five local fixes.

**What is not wrong.** The document's structure, its reconciliation of CF's two dimension-lists, its forces integration, its Proportionality and Ecological Integration Assessments, its handling of the one-world question, its Article 20 section as a whole, its Registry discipline on Excluded rows and on Salvian, and its headline *Institutes* VI discovery are all sound, and the discovery is a genuine addition to what this build knows about its own evidence base.

---

## DOCUMENT LOG

- **Review:** `gallic_Doc05_Review_Round1.md` — Round 1, independent adversarial, fresh context, no involvement in drafting Doc_01–Doc_05.
- **Scope.** The whole of Doc_05 §0–§11. Every quotation, div id and file-line range marked "new this pass," "read this pass," or "re-read this pass" was checked at its stated locus. All four inhabited passages were checked sentence by sentence against their own anchor lists and against all five RCF Historical Containment criteria plus the Article 23 failure signature. The §0 Discipline 1 mapping table was checked dimension by dimension against CF line 658 by reading each target section, not by reading the table. §10A and §10B were checked against CF ll. 388–404's own question lists. All four Doc_04 §10 "For Doc_05" items (2, 8, 9, 10) plus item 12 were checked for genuine discharge. Registry rows 4, 26, 27, 33–39, 43, 44 were checked for scope compliance.
- **Method.** Direct search-and-context against the vendored files, using the same flattened working copies the drafter used so that file-line claims could be checked as given; the *Institutes* VI finding was additionally verified against the raw XML to rule out a flattening artifact, per this build's standing rule that a finding is never dismissed — or accepted — as a tooling artifact without independent re-verification. Governing documents (CF V7.4, Forces Framework V1.1, Constitution Articles 20–23, RCF v32) read directly at the line ranges named in the brief, not from memory. Approximately 115 checks performed; two wording deviations (C6, C11) and the ten substantial findings above were the yield.
- **Findings:** 10 substantial, 13 cosmetic.
- **Classifications affected:** none. No Doc_04 gravity classification, no Doc_01 strand finding, no Doc_02 boundary determination and no Doc_03 tier estimate (beyond the single mis-citation at C3) requires reopening. S6 raises a Registry licensing question (row 39) that belongs to the Registry owner, not to this document.
- **Disposition recommendation: SUBSTANTIAL REVISION REQUIRED — bounded.** The ten substantial findings are precisely specified and locally fixable; none requires re-reconstructing a lens. Two of them (S3, S5) call for a small amount of new reading — *Inst.* XII.20–33, and a re-read of *Inst.* IV.1–7 — and one (S1) calls for a bounded re-read of Registry row 26. A revision pass applying the enumerated fixes, followed by a bounded spot-check that re-verifies (i) the four inhabited passages sentence-by-sentence against their revised anchors, (ii) the *Inst.* XII chapter-extent claims, (iii) the Lérins evidence in §2.1 and §2.2 after S4/S6/S7 are applied, and (iv) that §11's search_record now matches what the document actually rests on, is the proportionate next step — matching the pattern that worked for Doc_03's and Doc_04's fix rounds.
- **Disagreement log:** none. The drafter's own review requirements (a)–(i) were all executed; requirement (d) is where the document's own predicted risk turned out to be realized, and requirement (b)'s three named pressure points held while two unnamed ones (S6, S8) did not.
