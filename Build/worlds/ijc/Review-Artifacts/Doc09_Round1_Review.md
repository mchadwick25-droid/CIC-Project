# Doc_09 Output Set — Round 1 Independent Adversarial Review

**Reviewed documents:**
- `Doc_09_Story_Inventory.md` (pre-revision draft, 2026-07-20)
- `Story-Chunks/ijcstory001` through `ijcstory006` (all six)
- `ijc_World_Profile.md` (pre-revision draft, 2026-07-20)
- `Doc_09_Validation_Layer.md` (pre-revision draft, 2026-07-20)

**Reviewer:** independent isolated agent, no drafting involvement, first-principles skeptical read per this world's own disclosed track record of confident-but-wrong claims (fabricated quotations, inverted rules, miscounts on small enumerable datasets).

**Overall verdict: SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

One HIGH finding drives this verdict: `Doc_09_Validation_Layer.md` §9 affirmatively certifies that the Story Inventory and World Profile are "each individually Cleared review and Approved to proceed" — they are not; both carry their own explicit "DRAFT — pending independent adversarial review" status, which is what this review is. Everything else checked — and a great deal was checked, independently and from source — held up. The analytical content across all four documents is, with the exceptions named below, accurate, internally consistent, and faithful to the governing documents it cites.

---

## Verification performed (shown work, not asserted)

1. **Extracted Construction Framework V7.4 DRAFT Part II and Part VI directly from the docx** (`word/document.xml`, tags stripped via `perl`, paragraph styles checked separately to confirm heading levels) rather than trusting any document's paraphrase.
2. **Independently counted Part VI's validation categories** using the extracted heading list and each heading's `pStyle` value.
3. **Row-by-row Source Registry cross-reference** of all six story chunks' own front-matter `Source:` fields against `Source_Registry.md`.
4. **Character-level side-by-side comparison** of World Profile §10's blockquote against Doc_07 §7 in the live `Doc_07_Integrated_Ecology_Analysis.md` file.
5. **Row-by-row tag comparison** of World Profile §6 against `Lexicon_Deployment_Index.md`'s own master table (columns AS/SC/DR/TC/RT/PV/CT).
6. **Cell-by-cell Force Index cross-check** of World Profile §5 against Doc_08's Section 3 (six-cell matrix) and Force Index.
7. **Repo-wide grep verification** of the Freeze Criterion quotation, the CO-016/Finding-E2 attribution (against `Build/reference/L2C-System-Status/CiC_Pipeline_Decision_Log.md`), and the "already extracted and used at Doc_01 §3" claim.
8. **Tier-definition cross-check** of all six stories against the Framework's actual Tier 1–4 text (Part II, "Story and Narrative Sources Assessment"), not the chunk template's own summary of it.

---

## HIGH

### Finding 1 — Validation Layer §9 falsely certifies Doc_09's own sibling outputs as already cleared

**What I checked:** `Doc_09_Validation_Layer.md` §9 ("Freeze Criteria") against the actual status headers of `Doc_09_Story_Inventory.md` and `ijc_World_Profile.md`.

**What I found:** §9 states, as an affirmative claim about what "this document does establish": *"Doc_01 through Doc_09 (Story Inventory and World Profile) are each individually Cleared review and Approved to proceed."* This is false. `Doc_09_Story_Inventory.md`'s own header reads: *"Status: DRAFT — pending independent adversarial review per `anthropic-skills:cic-build-cycle`. Not self-certified. Not Frozen."* `ijc_World_Profile.md`'s own Disposition reads: *"Pending independent adversarial review... If review disagrees, it is named explicitly rather than pushed through."* Neither document has been reviewed even once — this review is the first pass. The Validation Layer document itself carries the identical "DRAFT — pending independent adversarial review... Not self-certified" header, so the claim in §9 is not only false relative to its sibling documents, it is internally inconsistent with its own document's own top-of-file status.

**Location:** `Doc_09_Validation_Layer.md` §9, the sentence beginning "What this document does establish."

**Real defect or false alarm:** Real defect. This is exactly the failure mode this build's own `Open_Gaps_Tracking.md` names as a standing risk after Doc_07 and Doc_08 (item 9: *"a document that certifies its own compliance with a governing principle... is making a checkable claim, not a formality"*; *"For Doc_09, any 'CONFIRMED' or completion-checklist item should be treated with the same suspicion as a specific factual claim"*). This is precisely that pattern, caught on the first check rather than a second or third pass.

**What it does not affect:** the document's larger, correct conclusion — that this world is not Freeze-eligible — does not depend on this false clause; the real reasons (no Representative, no Permanent Prompt, no grounding-anchor paragraph to verify) are separately and accurately stated. The fix is narrow: state that Doc_01–08 are each individually Cleared review, and that Doc_09's own three outputs (Story Inventory, World Profile, this Validation Layer) are pending this round's review — not "each individually Cleared."

**Confidence:** High. Directly checkable by reading three status lines side by side; no interpretation required.

---

## MEDIUM

### Finding 2 — World Profile §2's Primacy-Claiming entry claims a superlative status its own cited sources don't give it, and that actually belongs to a different gravity

**What I checked:** the *Primatus* / Juridical Primacy-Claiming entry in World Profile §2 — *"Organizes this world's own institutional record more than any other single gravity"* and *"Doc_07 §2 confirms as this world's own organizing axis"* — against Doc_04's own six-test writeup for Candidate 1 and against Doc_07 §2 (Authority Ecology) directly.

**What I found:**
- Doc_07 §2 does not rank Candidate 1 above the other two Primary gravities. Its actual text: *"Doc_04 confirmed three Primary/Supporting-central gravities organizing this axis: Juridical Primacy-Claiming (Primary), Church-State Alliance and Its Limits (Primary), and Orthodoxy-Enforcement Through Imperial Power (Primary, cross-strand to Strands A/B only)"* — all three are presented as jointly organizing the Authority axis, with no comparative superlative attached to Primacy-Claiming specifically.
- The actual superlative language in this world's own record belongs to a *different* gravity. Doc_04's own Candidate 2 (Church-State Alliance and Its Limits) Explanatory test reads: *"Explains why church office becomes a form of state-adjacent power at all (Doc_01 §5) — **the single most load-bearing explanatory claim in this world's entire construction record to date**."* No comparable superlative appears anywhere in Doc_04's Candidate 1 writeup (its own Explanatory test says only "Passes strongly. Explains the Julius I/Athanasius episode... four otherwise separately-occurring events, one explanatory thread" — strong, but not marked as *the* most load-bearing claim in the build).
- Doc_08 §5 independently corroborates that Candidate 2, not Candidate 1, holds the one genuinely unique-superlative status among the Primary gravities: *"only Candidate 2... is confirmed cross-strand to all three strands"* — a distinction the World Profile's own Church-State Alliance entry correctly claims for itself elsewhere in the same section (*"this world's own only gravity confirmed universal in this way"*).

**Location:** `ijc_World_Profile.md` §2, *Primatus* / Juridical Primacy-Claiming entry, "Brief description" and "Grounding" lines.

**Real defect or false alarm:** Real defect — an unsupported ranking claim attributed to a source that, checked directly, does not make that ranking, in a build with a specifically disclosed history of confident claims about which gravity is "most" central turning out not to hold up on direct check (Doc_07's two-strikes lexicon-graph error is the closest prior instance of exactly this failure shape). Every other cross-strand-status and grounding claim in World Profile §2 (checked against Doc_04 §5 for all six gravities) matched its source exactly — this is the one entry that overreaches past what its own citation says.

**Confidence:** High that the claim is unsupported by the cited sources; moderate-high that it constitutes a defect worth fixing (as opposed to a defensible editorial judgment) given the specific, checkable "Doc_07 §2 confirms" attribution attached to it.

---

## LOW

### Finding 3 — Story Index table (§2) still shows "Rows 12–13" for the Tome story, one row short of the fix §4 already applied

**What I checked:** the Story Index table row for "The Tome That Would Not Bend" (`Doc_09_Story_Inventory.md` §2) against §4's own disclosed correction and against the story chunk's actual front-matter Source field.

**What I found:** the chunk itself (`ijcstory006_the-tome-that-would-not-bend.md`) cites three sources: Leo's Tome (Row 12), Leo's rejection letters (Row 13), *and* the Acts of the Council of Chalcedon (Row 11). §4 already discloses a correction: *"Row 11... was omitted from this list in the first draft, an incomplete enumeration rather than an uncaught borrowing; Row 11 is Native and was already correctly cited in the story chunk itself"* — and §4's own prose list now correctly reads "Rows 2, 3, 4, 7, 8, 11, 12, 13, 22." But the §2 Story Index table row for the same story was never updated to match: it still reads **"Rows 12–13"**, silently missing Row 11, even though the table's own "Source" column in the same row names "Acts of Chalcedon" explicitly.

**Location:** `Doc_09_Story_Inventory.md` §2, Story Index table, "The Tome That Would Not Bend" row, "Registry Cross-Reference" column.

**Real defect or false alarm:** Real defect — a propagation gap of the exact shape this build has repeatedly caught (a fix applied in one location, not carried to a second location stating the same fact). Low severity: the correct information is present elsewhere in the same document (§4's prose list, and the chunk's own front matter), so no reader relying on the full document would be misled, but the table itself, read on its own, is now inconsistent with the document's own disclosed correction.

**Confidence:** High. Direct textual comparison, not inference.

---

### Finding 4 — §1's claim that the tier categories were "already extracted and used at Doc_01 §3" is unsupported

**What I checked:** `Doc_09_Story_Inventory.md` §1's opening clause — *"Per Construction Framework V7.4 DRAFT (already extracted and used at Doc_01 §3): Tier 1 (Documented Historical Narrative)..."* — against the actual content of `Doc_01_World_Identification_Boundaries_Orientation.md` §3, and against a repo-wide search for the four-tier story classification anywhere in Doc_01–08.

**What I found:** Doc_01 §3 ("Distinct World Criteria") applies the Framework's *four world-identification questions* (recurring formation ecology, recurring gravities, recurring worship/formation/interpretation/belonging/authority patterns, distinguishing criteria) — it contains no reference whatsoever to story tiers, Tier 1–4, or narrative classification. A grep across every Doc_0X file in this world-build for the tier-category language ("Tier 1 (Documented Historical Narrative)," "four-tier story classification," "No Tier 5") returns exactly one hit in the entire build: `Doc_09_Story_Inventory.md` itself. The tier categories were not "already extracted and used" anywhere prior to this document — this is their first appearance in this build.

**Location:** `Doc_09_Story_Inventory.md` §1, opening parenthetical.

**Real defect or false alarm:** Real defect, low-to-moderate severity. It does not affect the correctness of the tier definitions themselves — I independently re-extracted Part II's actual tier text from the Framework docx and confirmed Doc_09's four-tier summary matches it exactly (see "What checked out clean" below) — only the provenance claim about where this build supposedly already used them is wrong. This is the same class of error this build has flagged in itself repeatedly (Doc_04 Open Item 5: *"claims of the form 'X already says Y' need direct verification, not inheritance from a document's own self-description"*), just not previously caught in Doc_09 itself.

**Confidence:** High on the absence (grep-verified across the full document set); the intended meaning of the clause is somewhat ambiguous (it may have meant to gesture at this build's general practice of extracting Framework text directly, exemplified at Doc_01 §3 for a different purpose), so I rate this a real but minor citation-accuracy defect rather than a fabrication with intent to mislead.

---

## What independently checked out clean (verified, not just skimmed)

**Validation Layer §1 — the "fifteen validation categories" count, independently re-derived.** I extracted every Heading2 section under Part VI directly from the docx XML and confirmed all validation-category headings sit at the identical paragraph style level:

`Validation Protocol Rigor` · `Historical Plausibility Testing` · `Ecological Integrity Testing` · `Balance Testing` · `Reduction Testing` · `Complexity Testing` · `Emergence Testing` · `Worship Integration Testing` · `Differentiation Testing` · `Author Dominance Testing` · `Anachronism Testing` · `Relational Safety Testing` · `Living Tradition Testing` · `Adversarial Resistance Testing` · `Encounter Testing` · `Revision Testing` · `Freeze Criteria` — all 17 headings are `Heading2`, i.e., structurally coordinate.

Removing the two that are governing/procedural subsections rather than testable categories — `Validation Protocol Rigor` (states the rigor bar a result must meet before being reported "confirmed"; contains no pass/fail question of its own) and `Freeze Criteria` (a freeze-readiness checklist spanning far more than validation results — Doc_08/09 completion, Registry completeness, etc.) — leaves exactly **15**: Historical Plausibility, Ecological Integrity Testing (parent) + its 5 named sub-tests (Balance, Reduction, Complexity, Emergence, Worship Integration), Differentiation, Author Dominance, Anachronism, Relational Safety, Living Tradition, Adversarial Resistance, Encounter, Revision. **This independently matches Doc_09's own claimed count of fifteen exactly**, and every one of the 15 is addressed somewhere in §§2–8 of the Validation Layer (10 given a direct result, the other 4 — Relational Safety, Adversarial Resistance, Encounter, Revision-in-its-Framework-sense — explicitly and correctly named as not yet testable without a Representative). Doc_09's own reasoning for why "Validation Protocol Rigor" isn't a 16th category is sound and matches what I found independently from the raw structure, not just the prose.

**Freeze Criterion quotation and its attribution.** The quoted Framework text — *"A complete Registry without a verified grounding-anchor paragraph in the deployed prompt does not satisfy this gate — the Registry alone does not constrain generation"* — is a verbatim match against the extracted Part VI text. The attribution (*"added system-wide via CO-016, per the project-wide Pipeline Decision Log fix E2"*) is independently confirmed against `Build/reference/L2C-System-Status/CiC_Pipeline_Decision_Log.md`, which records: *"E2 — added a Freeze Criterion: a world is not freeze-eligible on a complete Registry alone; the deployed Permanent Prompt's grounding-anchor paragraph must be verified drawn from it"* and *"CO-016 filed in the Change Orders Register (V1.13), enumerating this entire fix set."* The self-correction disclosed in §9 (withdrawing an earlier false claim that this build's own Doc_02 established the Freeze Criterion) also checks out — I grepped `Doc_02_Source_Ecology.md` for "grounding" and found zero matches, confirming the corrected claim.

**World Profile §10 — the Doc_07 §7 verbatim copy.** I placed both paragraphs of the blockquote next to the live text of `Doc_07_Integrated_Ecology_Analysis.md` §7 and compared sentence by sentence, including the bolded opening clause, italics, nested quotation marks, and em-dashes. Both paragraphs match **word for word, with no truncation, paraphrase, or drift**. The document's own disclosed history (first draft dropped the opening sentence and the entire second paragraph) is accurately described, and the current text does not repeat that error.

**Story Inventory §4 — Source Cross-Reference completeness.** I independently enumerated the Registry rows actually cited in each of the six story chunks' own front matter: Row 2 (story 1), Row 3 (story 2), Row 22 (story 3), Rows 7–8 (story 4), Row 4 (story 5), Rows 11–12–13 (story 6). That is exactly the set {2, 3, 4, 7, 8, 11, 12, 13, 22} — nine rows — which is exactly what §4's prose list states. No omission in the prose (only in the §2 table, Finding 3 above).

**World Profile §6 — vocabulary tags, checked row by row against `Lexicon_Deployment_Index.md`'s master table.** *primatus*: AS/DR/TC/RT/PV/CT — exact match. *presbeia*: AS/DR/TC/RT/PV/CT — exact match. *homoios*: AS/DR/TC/RT — exact match (correctly excludes PV and CT, both of which the index's own master table also withholds for this term). *communio*: AS/SC/DR/TC/RT — exact match. *Imperator intra Ecclesiam*: AS/DR/TC/RT/PV — exact match. *homoousios*: SC/TC/RT/CT — exact match. All six rows, zero discrepancies.

**World Profile §5 — Forces Summary cell coverage.** Doc_08's own six-cell matrix (Section 3) populates all six cells (1A, 1B, 2A, 2B, 3A, 3B) with at least one force. World Profile §5 represents 1A, 1B, 2A, 3A, 3B directly via named force entries and covers 2B via the dedicated dual-cell transmission entry ("Cell: 2B and 3B") — all six cells are genuinely represented, matching the §11 completion-checklist claim exactly. Each force's stated "Gravity connection" in §5 also matches Doc_08's own Force Index and Section 5 prose exactly, cell by cell (spot-checked all six entries, not just one).

**Story tier classifications, checked against the Framework's actual Part II text, not the chunk template's summary of it.** I extracted the real Tier 1–4 definitions and confidence-level rules directly from the docx. All six stories' Tier and Confidence-field pairings comply with the Framework's actual rule (e.g., Tier 1 permits "Documented to Widely Accepted at the narrative level... Contested confidence for specific details" — exactly the pattern used in stories 1, 2, 4, and 5, which each carry a Documented/Widely-Accepted narrative-level confidence alongside a Contested or Widely-Accepted qualifier for a specific sub-claim). "The Bees of Milan" is correctly Tier 3 for the *right* reason (explicit hagiographic genre markers, a recognizable cross-saint topos, decades-later composition by someone in the subject's own circle) rather than merely "because it's hagiography" — the Tier Justification actually engages the Framework's own distinguishing test (formation-ideal-as-evidence vs. specific-events-as-evidence), matching this skill's own stated bar for what a real tier justification must do. No story in the set shows any sign of invented or composited content; every sentence in every Story Text traces to a specific, named, Registry-confirmed source.

**No-Tier-5 audit.** Independently re-checked against the same source list — all six stories trace to named authors and named, Registry-Native texts. No candidate for an unacknowledged Tier 5 entry.

**Absent Stories (§5).** Checked each of the five named absences against its cited grounding (Doc_05 §1 for ordinary-believer experience — confirmed, Doc_05 §1 states this almost verbatim; Doc_05 §5 for the pagan-boundary gap — confirmed, matches Doc_05's own disclosed Registry gap on the Altar of Victory controversy). All five read as specific and evidenced, not placeholder language.

---

## Escalation-category assessment (reviewer's own check, not the document's self-assessment)

None of the four findings above touch Representative identity, decide a portfolio-level or cross-world question, or reopen a gravity/strand finding already cleared at Doc_01–08. Finding 1 is the only one that materially affects what the document set may claim about itself going forward (it cannot be carried into any later Freeze determination as written). Findings 2–4 are correctable in place without cascading revision elsewhere.

---

## Summary for the build thread

**Verdict: SUBSTANTIAL REVISION REQUIRED** — one HIGH finding (a false "already Cleared" certification claim about Doc_09's own sibling documents, in the Validation Layer's own Freeze Criteria section) plus one MEDIUM (an unsupported "organizing axis" superlative in the World Profile, attributed to a source that doesn't say it) and two LOW findings (a propagation gap in the Story Index table; an unsupported self-referential citation). Everything else independently checked — the 15-category validation count, the Freeze Criterion quote and its CO-016/E2 attribution, the full verbatim Doc_07 §7 copy, the Source Registry cross-reference completeness, the vocabulary tag table, the Forces Summary cell coverage, and all six story tier classifications — held up exactly as claimed.
