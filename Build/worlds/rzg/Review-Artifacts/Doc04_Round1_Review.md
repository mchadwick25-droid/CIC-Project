# Doc_04 (Gravity Discovery) — Round 1 Independent Adversarial Review

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_04_Gravity_Discovery.md`, DRAFT, Revision 1
**Reviewed against:** `Doc_01_World_Identification_Boundaries_Orientation.md` (Rev. 5, Approved to proceed), `Doc_02_Source_Ecology.md` (Rev. 3, Approved to proceed) / `Source_Registry.md`, `Doc_03_Lexicon_Candidate_List.md` (Approved to proceed), and the vendored primary texts in `cic/texts/` directly (not taken on the document's own word)
**Reviewer:** independent adversarial review agent, per `cic-build-cycle` / `cic-gravity-index`
**Date:** 2026-09-15

---

## Verdict: **Substantial revision required**

This document does real, careful work in several places — the Confidence/Gravity Cross-Check disclosures for G1 and G4 are honest and well-earned, the Article 21 cross-strand testing is genuinely run rather than asserted, and D-A/D-B are correctly excluded. But it also contains **one fabricated/altered quotation** presented as a directly re-verified verbatim source (the exact defect class this world's build has already been caught on twice at Doc_03), **a load-bearing claim resting on a Source Registry row outside that row's own declared date scope**, **a repeated misattributed cross-reference** to a document/section that does not contain the claim attributed to it, **a citation whose content does not support the claim it is cited for**, and **an Interaction Matrix that claims "full pairwise coverage" while actually missing 40% of the required pairs**. These are not cosmetic. Per "No easy fixes" / "Fix it right" (`CLAUDE.md`), this needs correction at the source, not a wording patch, before this document can be re-submitted.

---

## Findings

### Critical

**1. Fabricated/altered quotation in Zwingli's 1527 "On Election" — the theological content of the quoted words has been changed.**

**Checked:** Doc_04 §3.1 (Repetition test) and §3.1 (Confidence/Gravity Cross-Check) both present, as a directly re-verified verbatim quotation: *"God's election, predestination or marking out, calling, [justification]... you will ever say right"* (cited at line 9678, `zwingli_selected-works_jackson1901.txt`), with Doc_04 stating explicitly this was "verified directly against the vendored file, not carried by inference from Calvin."

**What the source actually says** (verified directly against the vendored file this pass, lines 9674–9679):
> "...calling, which all precede faith, but in the same order. So if you say : God's election, predestination or marking out, calling, **beatifies**, you will ever say right."

The word at that exact position is **"beatifies,"** not "justification." Doc_04's bracket `[justification]` is not a standard editorial clarification of an ambiguous referent — it silently substitutes a different, specific theological term for a word that is actually present and legible in the source. "Beatifies" (confers blessedness) and "justification" (the forensic declaration of righteousness, the Institutes' own technical *ordo salutis* term) are not interchangeable in Reformed soteriology, and this is precisely the register Doc_04 itself is arguing Zwingli's exposition anticipates and Calvin later systematizes — so the substitution is not a neutral stylistic smoothing, it imports the more Calvinist-technical term into Zwingli's own mouth at the exact place a reader would check.

**Why this matters here specifically:** this quotation is the centerpiece of G1's revised Repetition-test finding — the "sharpened" claim that Zwingli's own corpus contains a "sustained, independent treatment" of election, which Doc_04 explicitly instructs Doc_05/Doc_06 to carry forward in place of Doc_01/Doc_02's "seed form" characterization (§7, first bullet). A load-bearing, world-shaping claim rests on an altered quotation. `CLAUDE.md` states this exact failure mode is "the single most serious governance failure this project recognizes" in safety contexts and separately names "misattributed and mis-transcribed quotes" as "a real, recurring defect here" for source fidelity generally — and this world's build has already required two rounds of correction for exactly this class of error at Doc_03 (Round 1: a fabricated Doc_01 §5 quotation and a fabricated Doc_02 §8 finding; Round 2: a wrong citation locus). This is a third occurrence of the same underlying failure pattern, this time altering the actual wording of a primary source rather than misattributing a cross-reference.

**Fix required:** requote accurately — "beatifies" is the actual word — and reassess independently whether the passage still supports "sustained, independent treatment" once quoted correctly (it likely still does; the surrounding syllogistic argument through Romans 8–9 is real and does not depend on this one word). Then re-run whatever downstream conclusion depended on the altered wording specifically.

---

### High

**2. A load-bearing new claim is built on Source Registry content outside that row's own declared date scope, and the Registry is not corrected.**

**Checked:** whether the newly-cited 1527 "Refutation of the Tricks of the [Cata]Baptists" (containing the "On Election" section, lines 9591–9762) is properly licensed by the Source Registry row Doc_04 relies on (row 7).

**What I found:** `Source_Registry.md` row 7 reads: *"Selected Works — letter to Erasmus, the Constance petition, the Acts of the First and Second Zurich Disputations, other shorter writings (Zwingli, Jackson 1901)... Licensed For: **Zurich's own 1522–1523 reform record**, distinct from the Sixty-Seven Articles' own row."* The corpus-map YAML's own note for this same row similarly describes its contents as "documenting Zwingli's own early Zurich reform, **1522-1523**." The 1527 "Refutation of the Tricks of the Baptists" — confirmed directly against the vendored file to be dated 1527 in its own heading — falls **outside** the date range this row is licensed for. Doc_04 draws its central new predestination finding from exactly this out-of-scope material, and does not flag, correct, or request correction of the Registry's own "Licensed For" field.

**Why this matters:** `Source_Registry.md`'s own header states "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding row here." Doc_04 does partially self-disclose the underlying completeness gap ("this document cannot claim its own search of this one section is exhaustive"), which is honest as far as it goes — but that's about *exhaustiveness of search*, not the more specific problem that the material actually found falls outside the row's own stated date license.

**Fix required:** update (or flag as an owed correction to) `Source_Registry.md` row 7's "Licensed For" field to reflect that the file's actual contents extend past 1523 into at least 1527.

**3. Misattributed cross-reference: the "seed form" characterization is not in Doc_01 §5 or Doc_02 §2 — the same defect class already caught twice in this world's build.**

**Checked:** Doc_04 §3.1 states: *"Doc_01 §5 and Doc_02 §2 characterize Zwingli's own treatment as present only 'in seed form,' thinner and less systematic than Calvin's."*

**What I found:** the phrase "in seed form" appears exactly twice in Doc_01 — in **§3** and **§4** — never in §5 (Strand Determination), which I read in full and confirmed contains no such phrase. It also does not appear anywhere in **Doc_02 §2**, which discusses Zwingli's Visibility/Representativeness/Influence/Limitations/Transmission History but never uses this phrase — it is actually Doc_03's own wording (§1, Predestination candidate row).

**Why this matters:** this is precisely the failure pattern `CLAUDE.md` flags for this specific world and precisely the finding Doc_03 Round 1 review already caught once ("a non-existent Doc_01 §5 quotation").

**Fix required:** correct the citation to Doc_01 §3/§4 and Doc_03 §1, and drop or correct the Doc_02 §2 attribution.

**4. "Carnal" vocabulary citations are genuinely Zwingli's own words, but they do not support the specific claim they are cited for.**

**Checked:** whether lines 5422, 6931–6932, 8266–8289 (cited in §3.2 Dependency and in the §6 Interaction Matrix, G2↔G3) are (a) actually in Zwingli's own corpus rather than Calvin's, and (b) actually support the claim that this vocabulary is used "against 'carnal' misreadings of 'This is my body'" — i.e., Eucharistic hermeneutics.

**What I found:** (a) is true — all three citations are genuinely in `zwingli_selected-works_jackson1901.txt`, not Calvin's Institutes. But (b) is false: every one of these lines is part of the same 1527 "Refutation of the Tricks of the [Cata]Baptists," and in every case "carnal" is being used in the **Anabaptist/civil-magistracy controversy** — "carnal liberty" (antinomian license), a husband calling his wife "carnal" in a marriage dispute, and "the magistracy is a carnal office" in the debate over whether a Christian may serve as magistrate. None of these three citations has anything to do with the Lord's Supper. A full search of every occurrence of "carnal" in this file (8 total) confirms none appear in a Eucharistic context.

**Fix required:** either locate an actual Eucharistic "carnal" citation in Zwingli's corpus (none was found in this pass) or drop the specific line citations and state the G2↔G3 argument in more general terms.

**5. The Interaction Matrix claims "full pairwise coverage" but is missing 6 of the 15 required pairs.**

**Checked:** §6 states "Full pairwise coverage of every candidate that reached classification." Six candidates reached classification (G1, G2, G3, G4, T1, T2), requiring 15 pairs.

**What I found:** only 9 pairs are actually listed. The following **6 pairs are entirely absent** — not marked "no demonstrated relationship," simply not addressed anywhere: **G1↔T1, G1↔T2, G2↔T1, G2↔G4, G3↔T2, G4↔T2.**

**Why this matters:** the narrower claim ("every classified candidate has at least one relationship") happens to be true, so this is not the Framework's specific "empty row" red flag. But the document's own stated methodology promise — "full pairwise coverage" — is not met, and an untested pair is not the same as an honestly-disclosed "–" cell (which this document does use correctly elsewhere, e.g. G1↔G2, G1↔G4, T1↔T2).

**Fix required:** either run the six missing pairs (most look tractable, e.g. G2↔G4 and G4↔T2 plausibly resolve to "–, no demonstrated relationship") or drop the "full pairwise coverage" claim.

---

### Medium

**6. Citation-pinpoint error, repeated twice: the Second Helvetic Confession "mirror" quotation is not at the cited line.**

**Checked:** Doc_04 cites *"Let... Christ be the mirror in which we behold our predestination"* at line 677, and bundles it into a "lines 666–677" range alongside "We reject those who seek out of Christ whether they are chosen..."

**What I found:** "We reject those who seek..." is genuinely at line 667 (close to claimed). But "Let, therefore, Christ be the mirror..." is at **line 684** — seven lines past the end of the stated "666–677" range. Both quotations are otherwise accurately transcribed verbatim; only the line-pinpointing is wrong. Same defect class as Doc_03 Round 2's IV.3.9→IV.3.8 correction, recurring here twice within the same document.

**Fix required:** correct both citations to line 684 for the mirror quotation.

**7. One of four cited "sacrifice of the mass" line references does not contain that phrase.**

**Checked:** Doc_04 §3.2 cites lines 20657, 20735, 20812, 20934 in Calvin's Institutes vol. 3 as instances of "the sacrifice of the mass."

**What I found:** the literal phrase occurs at 20735, 20812, 20934 (and also 20943, 20948, 21286, not cited) but **not** at line 20657, which instead reads "...the mass is a work by which the priest who offers Christ... gain merit with God, or that it is an expiatory victim..." — same general polemic, same chapter, not the quoted phrase.

**Fix required:** drop line 20657 or replace with an accurate instance (e.g., 20943 or 20948).

**8. "Sharpens, without contradicting" understates how much the new Zwingli finding actually complicates Doc_01's general characterization.**

**Checked:** whether this framing (explicitly asked about in the review brief) is fair.

**What I found:** Doc_01's "seed form" language characterizes "Zwingli's own providential theology" generally, not a claim scoped to the Sixty-Seven Articles specifically. Doc_04 narrows this retroactively — "'seed form' is accurate for Zwingli's own founding document specifically" — to reconcile it with its own new finding. That narrowing is Doc_04's own interpretive move, not something Doc_01 itself stated. A genuinely sustained, ordered election-predestination-calling-faith argument is closer to systematic than "seed form" suggests.

**Fix required:** name the tension more plainly in the §7 carry-forward instruction rather than folding it entirely into "sharpens... without contradicting."

**9. Questionable forces-connection cell placement for G1's Augustinian-inheritance citation.**

**Checked:** Doc_04 places the Augustinian-inheritance quote in Cell 1B (Internal), attributed to Doc_01 §6.

**What I found:** Doc_01's own six-cell table places nothing about Augustine in either Cell 1A or 1B; the discussion appears in unassigned prose. By Doc_01's own logic, an inherited external antecedent reads more naturally as Cell 1A (External) than Cell 1B (reserved for this world's own two specific local founding acts).

**Fix required:** place in Cell 1A, or state plainly this is Doc_04's own interpretive extension.

**10. Minor overclaim: Doc_01's own hedge on the Beza/Dort throughline is dropped.**

Doc_04 states Beza's *Tabula* "became a genuine theological throughline toward Dort" without carrying forward Doc_01's own explicit "though at one remove" qualification (Arminius's immediate opponents were Gomarus/Junius, not Beza directly).

**Fix required:** carry the qualification forward.

---

### Low / Cosmetic

**11.** The Article 21 "different enactment = evidence for centrality" reasoning (applied to G1, G3) is not actually unfalsifiable in practice — G4 genuinely fails it — but the document would be stronger naming this risk explicitly rather than leaving it for a reader to notice. No fix required.

**12. Verified clean — no defect found**, on: the Sixty-Seven Articles' zero predestination/election language (lines 4485–4700, confirmed — only false-positive substring matches on "SELECTIONS"); Article XVIII verbatim (lines 4564–4568); Second Helvetic Ch. X heading and content characterization; Institutes IV.3.8 (not IV.3.9) correctly used as the corrected locus; Consensus Tigurinus 9th Head of Agreement quoted in the corrected form; no five-level-vocabulary misuse or conflation with the Registry's A–E scale; D-A/D-B correctly excluded; the G1 and G4 Confidence/Gravity Cross-Check divergences are real, textually grounded, and honestly named rather than resolved by upgrading (the strongest part of the document); the Interaction Matrix's present negative findings (G1↔G2, G1↔G4, T1↔T2) give specific, checkable reasons rather than functioning as a cop-out.

---

## Summary

One fabricated quotation, one out-of-scope Registry citation, one misattributed cross-reference repeating an already-flagged defect pattern, one decontextualized citation, and a falsely-claimed "full" Interaction Matrix together mean this document cannot proceed as drafted; the Confidence/Gravity Cross-Check and Article 21 testing that anchor its actual classifications are sound and should survive a corrected revision largely intact.

**Escalation categories:** none apply. This is ordinary sourcing-fidelity and citation-accuracy review work within a single document's own build cycle — it does not touch Representative identity/title/voice, portfolio-level or cross-world scope, governance or methodology, or an unresolved tension the pipeline itself cannot close. All findings above are correctable by the build thread itself, at Doc_04's own revision stage, per `cic-build-cycle`'s ordinary self-governance.
