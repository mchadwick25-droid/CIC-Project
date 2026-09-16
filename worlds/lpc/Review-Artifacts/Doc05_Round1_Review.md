# Doc_05 — Ecological Reconstruction: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-14.

**Document reviewed:** `worlds/lpc/Doc_05_Ecological_Reconstruction.md` (374 lines), DRAFT, no prior review round.

**Read as governing standard, not reviewed:** `Doc_01_World_Identification_Boundaries_Orientation.md`; `Doc_02_Source_Ecology.md`; `Doc_03_Lexicon_Candidate_List.md`; `Doc_04_Gravity_Discovery.md` (full) and `Doc_04_Superseded_Claims.md` (full); `Source_Registry.md` rows 1, 2, 4, 7, 11, 13, 19, 65, 122, 192; `Doc04_Round9_Review.md` and `Doc04_Round11_Review.md` (targeted); `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part III and Part VII Step 4/5 (extracted from `word/document.xml`); `CiC_L3A_Forces_Framework_V1.1.docx` Step 5 and Step 7 (extracted); `CiC_L1_Constitution_V2_2.docx` Articles 19, 20, 21, 22, 23 (extracted); `Donatism/Doc_05_Ecological_Reconstruction.md` (structural comparison only).

**Read at source and independently re-run:** every direct quotation in Doc_05 attributed to a primary source was located and character-checked against `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` and `cic/texts/npnf101_augustine-confessions-letters.xml`, `npnf104_augustine-anti-manichaean-anti-donatist.xml`, and `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`. The full-text "confessor" sweep at §2.3 was independently re-run across all eight vendored Augustine volumes (`npnf101`–`npnf108`) with every occurrence pulled in context. The "flock/shepherd/pastor" combined count was independently re-run against Cyprian's own `div1` section of `anf05`. The Framework's Part VII Step 5 dimension list and the Forces Framework's own Step 5 text were extracted directly from the governing `.docx` files rather than taken from Doc_05's own paraphrase of them.

### Method

I drafted nothing under review and hold no prior position on this world's gravities or classification. I treated every quoted string in Doc_05 as a claim to re-check, per this project's own absolute rule, not as a fact because it carries a "re-verified at source this pass" note. Where Doc_05 cites Doc_04 citing Doc_02 or the Constitution, I opened the cited document myself rather than trusting Doc_05's characterization of it. I re-ran, rather than merely re-read, the one self-reported full-corpus count (§2.3) that this document uses to close an open item in the permanent record, because that is exactly the shape of check this build's own history (Doc_04, eleven rounds) has shown cannot be trusted on the strength of its own report.

---

## VERDICT: REVISION REQUIRED

**Findings: 2 HIGH · 3 MEDIUM · 2 LOW · 1 COSMETIC — 8 in total.**

**What holds up.** This is, on the whole, a carefully built document. Of roughly twenty direct quotations checked against the vendored XML byte-for-byte, all but one reproduce exactly, including several long, exact block quotations (the *De Lapsis* grief passage, the 256 preface's egalitarian formula, *On Baptism* II.3's plenary-councils passage, *On Baptism*'s "neither sacrament may be wronged" passage, Letter CXXVI's three quoted phrases, the "importunity of the people" phrase, and Pontius's "judgment of God and the favour of the people" phrase). Registry confidence-level citations (rows 1, 2, 4, 11, 13, 19, 122, 192) all check out against `Source_Registry.md` exactly. The Doc_04 §7 item 2 four-clause instruction is quoted correctly and each of its four clauses is genuinely, separately honored at the sites Doc_05 names. The Framework's own Step 5 dimension list (extracted directly from the `.docx`) is reproduced completely and accurately at §0.7, and the "¶663" paragraph citation is correct to within one paragraph of independent count. The Constitution's own three bounding conditions for Article 20's secondary prong are quoted correctly. The century-gap discipline (§0.3) is honored throughout — no inhabited passage anywhere in the document comments on the silence or extends a phase-one attestation into phase two without saying so, which I checked passage by passage.

**What does not.** One load-bearing self-reported count that the document uses to close a Doc_04 open item in the permanent record is wrong, and wrong in a way that reproduces this build's own named failure pattern: a check that returns *something* is trusted because it returns something. And the document's own front-matter quotes a governing document that does not contain the words quoted, misattributing to the Forces Framework a phrase that actually belongs to the Construction Framework's own summary of it — which also papers over a real terminological mismatch between the two governing documents that should have been logged as a finding, not smoothed over. Neither defect touches the gravity spine, the phase discipline, or the great majority of the document's claims, which is why this is REVISION REQUIRED rather than SUBSTANTIAL REVISION REQUIRED.

---

## HIGH

### H1 — The §2.3 "confessor" sweep that discharges Doc_04 §7 item 5 undercounts by at least three, is internally inconsistent with its own stated total, and omits the one class of hit closest to a real positive

**Site:** Doc_05 §2.3 (lines ~114) and §11 item 4.

**Claim under test.** Doc_05 states: *"A full-text count of confessor/confessors across all eight vendored Augustine volumes (`npnf101`–`npnf108`) returns **seventeen occurrences in total**... every occurrence was opened and read... The seventeen sort into four kinds, enumerated rather than sampled."* This is offered as the evidence that answers Doc_04 §7 item 5 ("ANSWERED HERE, in the negative," §11 item 4) — the open item asking whether Augustine-phase confessor-authority material exists that would bear on G8's Tensional, Cyprian-phase-bound classification.

**What I found.** An independent `grep -oiE "confessor[s]?"` sweep of all eight files returns **20** occurrences, not 17:

| File | Count |
|---|---|
| npnf101 | 2 |
| npnf102 | 4 |
| npnf103 | 2 |
| npnf104 | 1 |
| npnf105 | 3 |
| npnf106 | 1 |
| npnf107 | 1 |
| npnf108 | 6 |
| **Total** | **20** |

Doc_05's own four-category enumeration (a)–(d), plus the separately-named npnf104 instance, itself sums to only **16** when counted bullet by bullet (category (a) 6, (b) 3, (c) 5, (d) 1, plus the npnf104 instance 1) — so the stated total of seventeen does not even match the document's own breakdown of it, before checking against the source at all.

At least four real occurrences are missing from the enumeration entirely:
- **npnf101, line 25368** — "Maximus Confessor" (the 7th-century Byzantine theologian's traditional epithet), in the volume's own 19th-century General Introduction. This is a **second** unflagged editorial occurrence, directly contradicting Doc_05's claim that there is "one editorial occurrence, in the Oxford Library's own 19th-century preface (npnf108)."
- **npnf103, lines 43540 and 44383** — "Felix the Confessor" / "the Confessor Felix," **two** occurrences, both inside Augustine's own Letter (not an editorial note) discussing a deceased confessor of Nola. This is the single closest thing anywhere in the eight-volume sweep to Cyprian's own honorific use of "confessor" as a title borne by a named individual, and it is entirely absent from Doc_05's four-category analysis.
- **npnf108, line 4513554** — "...if love were not in the confessor?" — a fifth, uncategorized occurrence.

**Why this matters.** This is not a cosmetic tally error. §2.3 is written and used as a dispositive check: it is what lets Doc_05 tell Doc_06, Doc_07, and Doc_08 that "G8's Cyprian-phase-boundedness is confirmed rather than disturbed" and to carry that as a closed Doc_04 open item (§11 item 4, §7 Open Item 5 in the classification summary). The claim "every occurrence was opened and read" is false on the document's own numbers. The missing "Felix the Confessor" material does not, on inspection, rescue G8 — Felix of Nola is a title of posthumous honor, not a claim to dispose of the church's peace — but Doc_05 does not get to state that conclusion without having actually looked at the material, and right now it has not.

**Fix.** Re-run the sweep with a documented, reproducible regex and scope; enumerate all twenty (or however many a corrected sweep returns) occurrences, including the two Felix-the-Confessor instances and the second editorial hit; and state explicitly, on the corrected list, whether the finding at §11 item 4 still holds (it likely does, but the document has not yet earned that conclusion).

---

### H2 — The document's own header misquotes the Forces Framework, attributing to it a phrase that belongs to a different governing document, and in doing so erases a real terminology conflict between the two

**Site:** Doc_05 header, line 9: *"Forces Framework V1.1 Step 5 (external forces integrated into every ecology lens, "especially Human Ecology, Community Ecology, and Boundary Ecology")."*

**What I found.** `CiC_L3A_Forces_Framework_V1.1.docx`'s own Step 5 section reads, in full:

> "External forces enter the ecology directly... **The Human Ecology, Community Ecology, and Boundary Structures lenses in particular** cannot be written without explicit forces integration."

The phrase "Boundary Ecology" does not occur anywhere in the Forces Framework. The phrase Doc_05 quotes — "especially Human Ecology, Community Ecology, and Boundary Ecology" — occurs verbatim not in the Forces Framework at all, but in `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part VII's own Step 5 activity entry: *"Forces Framework integration: Step 5. External forces integrated into every ecology lens, especially Human Ecology, Community Ecology, and Boundary Ecology."* That is the Construction Framework's own paraphrase/summary of what the Forces Framework requires — a different document, with a different word ("Boundary Ecology" vs. the Forces Framework's own "Boundary Structures").

**Why this matters.** Doc_05 puts the phrase in quotation marks and attributes it, specifically, to "Forces Framework V1.1 Step 5" — a citation any reader or downstream builder would take as a verbatim quotation of that document. It is not. This is exactly the class of defect this project's absolute verbatim-quotation rule exists to catch, applied here to Doc_05's own governing citation rather than to a primary source. It also has a substantive cost: Doc_05's own §0.7 coverage table treats "Boundary Structures" as a distinct, named Framework dimension (mapped to §6.1), so the two governing documents actually disagree about what this lens is called ("Boundary Structures" per the Forces Framework, "Boundary Ecology" per the Construction Framework's summary of it) — and Doc_05, by silently substituting one document's wording for the other's under a false attribution, reconciles a real cross-document disagreement instead of logging it, which this review's own governing instructions treat as a distinct kind of failure from an ordinary misquotation.

**Fix.** Quote the Forces Framework's own Step 5 text accurately ("Boundary Structures," "in particular," not "especially"), or attribute the "Boundary Ecology" phrasing correctly to the Construction Framework V7.4 Part VII. Separately, log the Boundary Structures/Boundary Ecology naming mismatch between the two L3-level governing documents as a methodology finding for the project lead (see escalation assessment, category 3, below) rather than absorbing it silently into Doc_05's own citation.

---

## MEDIUM

### M1 — The second editorial-bracket quotation (256 preface, §4.2) is not verbatim: a bracket is fabricated and the note's actual content is replaced by an ellipsis

**Site:** Doc_05 §4.2, construction note (line 160).

**Claim under test.** Doc_05 states: *"A second editorial interjection sits inside the 256 preface passage in the vendored edition —* "[Of course this implies a rebuke to the assumption of Stephen…]" *— and is the American editor's, not Cyprian's; it is excluded from the quotation above."*

**What I found.** The actual endnote at `anf05_hippolytus-cyprian-caius-novatian.xml` line 56872–56875 reads, in full: *"Of course this implies a rebuke to the assumption of Stephen, ["their brother," and forcibly contrasts the spirit of Cyprian with that of his intolerant compeer]."* There is no literal opening bracket before "Of course" anywhere in the source — the note's outer sentence is unbracketed editorial prose; only the inner clause ("their brother," and forcibly contrasts...) carries literal bracket characters in the source text. Doc_05's rendering invents a leading "[" that is not in the source, and its ellipsis silently drops the note's actual substantive content (that Stephen is elsewhere called "their brother," and that this contrasts Cyprian's spirit with his).

**Why this matters.** §9.6 holds this exact passage up as "an integrity finding, not a stylistic preference" — the worked demonstration that Doc_05 correctly separates the editor's voice from Cyprian's. The demonstration itself is not quoted verbatim from the source it claims to quote. This does not change the substantive point (it is still editorial, not Cyprian's, and no claim rests on Cyprian's 256 preface being aimed at Stephen) — but a quotation offered as proof of quotation discipline should itself survive that discipline.

**Fix.** Quote the endnote's actual text in full, or paraphrase it outside quotation marks with a line citation, rather than presenting a reconstructed approximation as a direct quotation.

---

### M2 — The §0.7 coverage-map overstates two things it claims to have covered completely: forces integration "in every lens," and the Power/Influence/Historical Dynamics dimension's fourth required question

**Site:** Doc_05 §0.7 table, rows "Forces integration in every lens | §1–§6 inline; summarized §9.3" and "Power / Influence / Historical Dynamics | §6.8."

**(a) Forces coverage.** Explicit "Forces on the X lens" paragraphs appear in §1, §2, §3, §4, §5, and §6.1 — six sites. They do **not** appear anywhere in §6.2 through §6.9 (Formation Logic, Memory Structures, Interpretive Ecology, Emotional/Affective, Meaning Transmission, Representative Theological Patterns, Power/Influence, Spatial/Regional) — eight of the nine world-specific-lens subsections. The Forces Framework's own binding requirement names only Human Ecology, Community Ecology, and Boundary Structures as lenses that *"cannot be written without explicit forces integration"* — and those three (§1, §2, §6.1) are in fact satisfied. But Doc_05's own coverage-table language, *"§1–§6 inline,"* reads as (and would mislead a reviewer checking coverage without reading for it into believing) blanket forces-integration across all of §6's nine subsections, which is not the case.

**(b) Power/Influence/Historical Dynamics.** The Construction Framework's own text for this dimension (Part III) names four required evaluation points: *"History's Impact on the World / The World's Impact on History / Position, Power & Influence / Effects on Formation, Interpretation & Theology."* §6.8 explicitly treats the first three, under matching headings ("History's impact on the world," "The world's impact on history," "Position, power, and influence"). It never explicitly treats, or cross-references, "Effects on Formation, Interpretation & Theology" as its own question — an omission the coverage table's single-cell mapping to §6.8 does not surface.

**Fix.** Narrow the coverage-table's forces-integration claim to the sections that actually carry a Forces paragraph (or add brief forces notes to §6.2–§6.9 where the ecology genuinely supports one), and add explicit treatment of, or an explicit cross-reference for, "Effects on Formation, Interpretation & Theology" to §6.8.

---

### M3 — Article 20's "against the grain" condition is applied to a genre the Framework's own illustration does not clearly cover, without the fit being argued

**Site:** Doc_05 §1.4.

**What I found.** The Construction Framework's own text defines the third bounding condition narrowly: *"Against-the-grain reading requires a specific textual trace — a polemic that presupposes a practice, a prohibition that implies the prohibited behavior — never inference from silence alone."* Doc_05 applies this condition to Letter CXXVI, a personal letter in which Augustine defends himself to a correspondent (Albina) and minimizes his own congregation's culpability — not a polemic directed against a practice, and not a prohibition implying a prohibited behavior. The underlying logic Doc_05 actually uses — a self-interested witness's concession against his own interest — is a defensible analogical extension of the same principle, but Doc_05 states flatly that "the third is available, at exactly one place, and it is used here" without acknowledging that the source's genre does not match the Framework's own worked example, or arguing why the extension is sound.

**Fix.** Add one sentence explicitly stating why a concession-against-interest in personal correspondence satisfies condition (c) as the Framework intends it, or flag the extension as an interpretive judgment call for the project lead to confirm rather than treating the fit as self-evident.

---

## LOW

### L1 — The inherited "113 combined flock/shepherd/pastor" count does not fully reproduce on independent re-count

**Site:** Doc_05 §4 (line 148), inherited from Doc_03.

Independently re-counting exact-word occurrences of "flock"/"flocks," "shepherd"/"shepherds," and "pastor"/"pastors" within Cyprian's own `div1` section of `anf05_hippolytus-cyprian-caius-novatian.xml` (lines 27373–59723) returns 55, 39, and 16 respectively — a combined 110, not 113. The "shepherd" figure (39) matches exactly; "flock" and "pastor" are each off by one or two, most likely a scope- or stemming-boundary difference from Doc_03's own original sweep. This is not original to Doc_05 — Doc_05 correctly attributes the number to Doc_03 and does not claim to have re-run it — but Doc_05 restates it as settled fact with no independent check or caveat, and the project's own numbers-reproduction discipline applies regardless of which document a figure originates in.

**Fix.** Re-run the sweep with a documented, reproducible scope and singular/plural rule, or note the figure's small margin of counting-method uncertainty when Doc_06 draws on it.

### L2 — Confidence-vocabulary imprecision at §1.4

**Site:** Doc_05 §1.4 construction note: *"**Inferential**, and presented as such."*

The project's five-level confidence vocabulary (per `CLAUDE.md` and the Constitution's own text, which Doc_05 itself uses consistently elsewhere — §1.3, §2.1, §5.1, §6.5, §9.7 all say "Inferential/Thin") names this tier "Inferential/Thin," not bare "Inferential." This is the one site in the document that drops the compound term.

**Fix.** Use "Inferential/Thin" for internal consistency.

---

## COSMETIC

### C1 — "Seven disciplines govern every lens below" (§0 opening) loosely counts §0.1–§0.7, two of which (the gravity spine, the coverage map) read as framing/index material rather than governing disciplines in the same sense as §0.2–§0.6. Not a substantive defect, just an imprecise count.

---

## Is Doc_05 adequate to proceed to Doc_06?

**My judgement: not yet, on two correctable defects — and I would not hold this document for more than one further round to fix them.** The great majority of this document's apparatus — its quotations, its Registry citations, its Framework coverage map, its century-gap discipline, its handling of Doc_04's four-clause G5 instruction, its honest disclosure of what it does not claim (§9.7) — holds up under adversarial re-verification at the level of detail this review applied. That is not a small thing given this build's history.

What has to change first: H1's confessor sweep is written into the permanent record (§11 item 4) as answering a Doc_04 open item in the negative, and it does so on a count that is wrong by at least three and internally inconsistent with itself. That must be corrected — the actual list re-run, the missed occurrences (including the two "Felix the Confessor" instances) accounted for by name, and the §11 item 4 disposition re-stated on the corrected evidence — before Doc_06, Doc_07, or Doc_08 build anything on "G8's Cyprian-phase-boundedness is confirmed." H2's misattributed Forces Framework quotation sits in the document's own governing header and should not survive into a document other builders will cite as settled; it is a one-paragraph fix, but it should not be deferred, since the Boundary Structures/Boundary Ecology mismatch it currently papers over needs to reach the project lead as a methodology question (see below), not stay buried in a corrected citation.

Neither defect touches the gravity spine (stable, and not reopened here), the phase discipline, or the bulk of the ecological claims. This is why my verdict is REVISION REQUIRED and not SUBSTANTIAL REVISION REQUIRED: a single fix pass addressing H1, H2, and the three MEDIUM findings should be sufficient, without restructuring the document.

---

## Escalation assessment (CO-022)

**1. Representative identity, title, or voice — does not apply.** §6.7 treats Representative theological *patterns*, not an identity, title, or voice decision, and I found no place in the document where one is smuggled in.

**2. Portfolio-level or cross-world — one item, and this review adds a second.** Doc_05's own §11 item 11 (the editorial-apparatus discipline should be checked against the whole vendored corpus, not only this document's own quotations) is correctly routed to review rather than acted on unilaterally — agreed, not decided here. **This review adds:** the Boundary Structures / Boundary Ecology naming mismatch between `CiC_L3A_Forces_Framework_V1.1` and `CiC_L3B_Formation_World_Construction_Framework_V7.4` (H2) is not specific to this world — every world build that reaches Ecological Reconstruction cites both documents' Step 5 entries, and the same silent substitution H2 identifies here is available to any other world's Doc_05. This should reach the project lead as a methodology question about the two L3-level documents themselves, not be fixed only inside this world's citation.

**3. Governance or methodology — open, unchanged, plus the item above.** Doc_04's own three-item governance/methodology escalation (separating the reading thread from the applying thread; the record-boundary question; the given-list-inherits-unverified-adjudications item Round 11 added) remains open and Doc_05 correctly does not attempt to close it (§11 item 3). This review's own H2 finding (category 2, above) is itself a governance/methodology item in the sense that it concerns the shared L3 documents rather than this world's build thread's own work.

**4. Unresolved tensions — one, and it is Doc_05's own, correctly carried.** The evidentiary question at Doc_04 §7 Open Item 6 (the 411 *Gesta*, unread, no owner, no acceptance criterion) is the one open tension Doc_05 names (§11 item 1), and it is right not to touch it — commissioning a third read is the project lead's decision, not this build thread's. I found no further unresolved tension of my own to add: H1 and H2 above are correctable defects with a clear fix, not open tensions between two positions that cannot be reconciled from inside this document.

---

*End of Round 1 review. Simulated review — informational only, not an Article 31 substitute.*
