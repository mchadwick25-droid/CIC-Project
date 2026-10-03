# Doc_03 — Lexicon Candidate List — Independent Adversarial Review (Round 1)

**World #3: Desert Monasticism**
**Reviewer:** Cold, independent subagent (no drafting context; treated all claims as unverified).
**Document reviewed:** `Build/worlds/desert/CiC_W3_Doc03_Lexicon_Candidate_List.md`
**Ground truth consulted in full:** Doc_01 (Approved), Doc_02 (Approved), Framework V7.3 Step 3, the Alexandria `alexlex008_theosis.md` file, git log, and ~10 external web sources for philology.

---

## (a) Overall verdict

**SUBSTANTIAL REVISION REQUIRED — narrow.**

The document is, on the whole, a genuinely strong Step 3 artifact: it is substantive rather than a glossary, its philology is accurate on almost every high-stakes point I could independently check (the eight logismoi, the Cassian/Matthew 5:8 substitution, the Pachomian koinōnia federation, the transliterations, the Evagrian-cluster isolation), its strand attributions are consistent with Doc_01, and its Author-Gravity risk tiering is defensible rather than merely asserted.

The verdict is nonetheless "substantial" — narrowly — because of **one integrity-level finding (F1):** the single most exotic transmission claim in the document (antirrhēsis surviving "only via Sogdian translation") is both **factually wrong** and **falsely attributed to a Doc_02 section that says no such thing and never mentions Sogdian at all.** A confident, fabricated cross-document citation supporting a "high Author Gravity risk" flag is exactly the class of defect that should not clear on a cosmetic disposition, even though the conclusion it supports survives correction and the fix is localized. Everything else I found is cosmetic.

---

## (b) Numbered findings

### F1 — SUBSTANTIAL — Section 1.17 (antirrhēsis): the Sogdian transmission claim is factually wrong and is fabricated as a Doc_02 citation

**Problem.** Section 1.17 justifies its "high Author Gravity risk" flag with: *"a genuinely unusual transmission history (Doc_02, Section 1.4: substantial fragments survive only via Sogdian translation, per Doc_02's own transmission-history note)."* Two distinct defects:

1. **Fabricated internal citation.** The string "Sogdian" appears nowhere in Doc_02. Doc_02 Section 1.4's actual transmission-history note says Evagrius's speculative works survive "substantially in Syriac and Armenian translation," and his ascetic-practical Greek works survive pseudonymously (chiefly as Nilus of Ancyra). It says nothing about Sogdian and nothing about the Antirrhetikos's specific survival channel. The parenthetical attributing the Sogdian claim to "Doc_02's own transmission-history note" asserts a source that does not contain the claim.

2. **The underlying fact is inverted.** Per the Encyclopaedia Iranica Evagrius entry and Wikipedia's sourced summary, the Antirrhetikos's original Greek is lost, but the **complete text survives in Syriac** (Frankenberg's 1912 edition, with a Greek retroversion), **plus Armenian and Georgian**, *and* some Sogdian fragments (Turfan, double recension). So the Sogdian is a marginal, fragmentary Silk-Road offshoot — **not** the sole survival channel. "Substantial fragments survive *only* via Sogdian" makes the marginal channel into the whole story and erases the Syriac backbone that actually preserves the work.

**Note on scope.** The *conclusion* — that antirrhēsis is single-text, single-author, with a genuinely unusual transmission and therefore high Author-Gravity risk — remains fully defensible after correction. The defect is in the specific supporting claim and its false sourcing, not in the risk flag. Recommended fix: rewrite to "the complete text survives only in translation (Syriac, ed. Frankenberg; also Armenian and Georgian), with additional Sogdian fragments surviving from the Turfan finds," and drop the "per Doc_02's own transmission-history note" attribution.

### F2 — COSMETIC — Intro: miscites "Doc_02 Section 4 (Cultural Scope…)"

**Problem.** The language-layer note in the intro cites "per Doc_02 Section 4 (Cultural Scope, Author Gravity concern)." Doc_02 Section 4 is "Liturgical Evidence," not Cultural Scope. The Cultural Scope / Greek-mediation Author-Gravity concern lives in Doc_01 Section 4 and Doc_02 Section 6 (Source Asymmetry). Doc_03's own Section 3 cites this correctly ("Doc_01 Section 4 / Doc_02 Section 6") — the intro is the erroneous instance and contradicts the document's own later citation. Fix: change the intro citation to match Section 3.

### F3 — COSMETIC — Section 1.15: transliteration typo "ergocheirion"

**Problem.** The Greek given is ἐργόχειρον; the transliteration printed is "ergocheirion," which carries an extra -i- (…cheir**i**on). The correct transliteration of ἐργόχειρον is "ergocheiron." All other ~16 transliterations check out.

### F4 — COSMETIC — Section 1.10 (nēpsis): missing the later-tradition caveat that hēsychia correctly receives

**Problem.** Doc_03 handles hēsychia (1.4) with exemplary care — flagging that its systematic elaboration belongs to the later Byzantine hesychast tradition, "well outside this world's own c. 430 closing boundary." nēpsis warrants the same caveat and does not get it — as a technical term it is if anything even more concentrated in the later neptic/Philokalic tradition than in the c. 320–430 desert. Minor consistency gap, not an error of fact.

### F5 — COSMETIC — Section 2 (theosis exclusion): the repo claim is TRUE but incompletely represented

**Problem.** Both halves of Section 2's claim check out (the Alexandria `alexlex008_theosis.md` file is confirmed Tier 1; the `bb0698c` vocabulary-isolation commit is confirmed real) — but two wrinkles should be surfaced: (1) the Alexandria theosis file itself carries a "Cross-build provisional constraint" stating Evagrius Ponticus's developed theosis theology "is most evidenced in the Desert Christianity world... reserved for Desert Christianity" — this actually strengthens Doc_03's claim to the apatheia/theōria cluster but complicates the clean "route deification-adjacent content away from theosis" framing, and Doc_03 doesn't mention it; (2) the file lives in `Archive/Alexandria-Build-History/Alexandria-v7/`, an archived prior build under an earlier world name ("Desert Christianity" for this world, "Phase 3"), not a live `worlds/Alexandria/` folder — Doc_03's present-tense phrasing glosses over this being an archived, earlier-vintage citation.

### F6 — COSMETIC — Step 3 activity "note terms requiring full Tier 1 treatment in Step 6" is only implicitly satisfied

**Problem.** Framework Step 3 includes "Note terms that will require full Tier 1 treatment in Step 6." Doc_03 assigns Tier-1 estimates to eight entries and flags the puritas cordis case explicitly for Doc_06, but never rolls these up into a discrete "these are the Doc_06 Tier-1 candidates" statement. The information is present but not indexed as the Framework activity phrases it.

---

## What checks out (adversarially confirmed, not assumed)

- **Eight logismoi — exact.** "gluttony, lust (fornication), avarice, sadness (lypē), anger, acedia, vainglory, pride" matches Evagrius's canonical Praktikos order item-for-item.
- **Cassian apatheia → puritas cordis / Matthew 5:8 — exact.** Confirmed across multiple sources, including the "deliberate substitution, not literal translation" framing and the 420s dating at the boundary edge.
- **Pachomian koinōnia federation — exact.** Confirmed: Pachomius's own name for the federation; nine men's houses and two women's houses at his death (346).
- **Strand attributions — consistent with Doc_01.** Evagrian cluster → Strand C; koinōnia/apotagē-codification → Strand B; synaxis → Strand C; gerōn/abba/amma → A and C. No contradictions found.
- **Author-Gravity tiering is defensible, not merely asserted.** Correctly isolates genuinely single-author Evagrian terms (high risk) from compiler-mediated Apophthegmata terms (moderate) from cross-strand/materially-corroborated terms (low). Holding *apatheia* at Tier 2 pending Doc_04 because of single-author concentration is appropriate restraint.
- **Does the Step 3 job.** Every required per-term element is present; the "terms considered and not included" section shows genuine discrimination; the language-layer section honestly surfaces the Greek-only gap as "a genuine gap, not a neutral finding." Not a superficial glossary.

---

## (c) What I did NOT / could not independently verify

- The full Framework text beyond Step 3 and its immediate neighbors.
- Independent confirmation that Alexandria is formally numbered "World #2" in the project's world index (low stakes).
- Whether Coptic-native technical vocabulary genuinely cannot be recovered from the Pachomian Coptic fragments (Doc_03's Section 3 gap-claim is plausible and honestly flagged, but not independently falsified).
- Exhaustive content-matching of all 18 source anchors — spot-checked several (all matched), did not check all.
- Frankenberg's 1912 edition of the Antirrhetikos directly (verified via Encyclopaedia Iranica, Wikipedia, and the Turfan/Syriac literature instead).

**Bottom line for the build thread:** one narrow substantial fix (F1) is required before disposition. F2 is a self-contradicting citation that should be fixed in the same pass. F3–F6 are cosmetic and can be applied directly. The document's philological and structural core is sound and does the Step 3 job well.
