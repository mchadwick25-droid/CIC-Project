# Record Compilation, Part 2 (Term Records) — Round 1 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`) — `worlds/lpc/scripts/wb_lpc_s22.py` and `records/lpc/term/`

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-24 · **Round:** 1 · **Deliverable under review:** 19 uncommitted `term` record files and the generator script that produced them, drafted cold by a different agent from `Doc_03_Lexicon_Candidate_List.md`, `Doc_06_Full_Lexicon_Development.md`, `Lexicon_Deployment_Index.md`, and all 19 `Lexicon-Chunks/` files.

A prior pass this session already independently confirmed: 19 files exist matching 19 Lexicon-Chunks; `engine.m1.gates.run_all` returns clean except the expected, pre-existing `gate-canon-coverage` (28 findings); the 122-link / 61-pair relations graph matches the drafting agent's own claim; and two disclosed tensions (the `lpclex007_grace.md` duplicated sentence, and `suffrage`'s missing `[DR]` tag) are pre-existing and correctly not silently resolved. Those points are not re-litigated below; this review covers what that pass did not check.

---

# VERDICT: CLEARED REVIEW — no substantial-revision finding

**0 HIGH · 1 MEDIUM · 2 LOW · 1 COSMETIC.**

This compilation holds up well against cold, independent verification. I read all 19 `Lexicon-Chunks/` files and the script's own docstring and body in full, then checked the actual 19 files on disk — not merely the script's stated intent — against both.

**Source-reference integrity, checked programmatically, not sampled:** every `sources[].source_id` across all 19 records (18 distinct source ids used) resolves to a real file in `records/lpc/source/`, with zero misses. Every `relations[].target` across all 19 records (19 distinct targets) resolves to a real term record in this same batch, with zero misses. Re-parsing all 19 files' own `relations` blocks directly from disk (not from the script's or the Index's restatement) gives exactly 122 directed edges, 61 reciprocal pairs, and zero one-way or duplicate edges — independently reproducing the count the drafting agent and `Lexicon_Deployment_Index.md` §5 both claim.

**Schema and envelope conformance, checked against `engine/m1/schemas.py` directly:** all 19 records carry `schema_version: 2`, `register: emic`, `status: draft`, `canon_cells: []`, and the correct `world_id`. Every `confidence.citation_specificity` (A×12, B×5, C×1, D×1), `verification_state`, `evidentiary_weight` (load-bearing×9, corroborating×8, illustrative×2 — `contested` used nowhere, matching the docstring's own claim), `formation_confidence` (Documented×16, Widely Accepted×1, Inferential-Thin×2), `distortion_risk` (high×9, medium×8, low×2) and `retrieval.tier` (1×7, 2×12) value falls inside its schema enum, with no stray or invented value anywhere. `distortion_risk` high-count (9) matches `Lexicon_Deployment_Index.md` §3's own `[DR]`-tagged count exactly. No record carries a populated `do_not_retrieve_when` or `claim_guards` — I independently confirmed, by scanning every `retrieval.prefer_instead` clause against `engine.prose.GUARD_MARKERS`, that none actually contains a guard-marker phrase, so the claim that every Do-Not-Retrieve-When clause is a redirect rather than a barred-claim guard holds.

**Quote and tier fidelity, checked against all 19 chunks directly, not sampled to 8:** I compared every one of the 19 term records' `plain_meaning`, `quick_meaning`, `senses.*`, `sources[].locus`, and `confidence.*` fields against its own Lexicon-Chunk's Quick Meaning, World Meaning, Key Sources, and Tier line. Every direct quotation carried into a term record (Cyprian's shepherd/flock passages, the 256 preface, the two conciliar formulas, the *De Unitate*/`On Baptism` ordination passage, the Epistle XIV certificate passages including the corrected "were **daily** given, contrary to the law of the Gospel" wording, the grace and coercion passages) is verbatim against its chunk. Every tier assignment (7 Tier 1 / 12 Tier 2) matches Doc_06 §2 exactly, including the four down-tiered terms (preaching, catechesis, bishop of bishops, plenary Council), the two corrected-upward terms (*libelli*, *libellatici*/*sacrificati*), and the one added term (certificates). All three CT Contest Type write-ups (grace, schism, "compel them to come in") are carried into `senses.informational` non-templated and match Doc_06 §3's stated contest type for each. The Schaff editorial verdict on Augustine's coercion doctrine ("a false exegesis," "least satisfactory to Protestant readers") is correctly excluded from `lpc.term.compel-them-to-come-in` entirely, matching the chunk's own instruction. No confidence upgrade or tier reassignment anywhere exceeds what its own chunk states.

Direct file reads of five records (`certificates-letters-of-peace`, `suffrage`, `grace`, `libelli`, `heresy`) against the script's own literal dict values found byte-for-byte agreement — no post-generation drift between the script and its output.

One MEDIUM finding, about an undisclosed-as-such authored judgment rather than a misstatement of fact, is below. It does not misrepresent a chunk, a source, or a historical claim, and would not block proceeding.

---

# Method

I read `CLAUDE.md` in full first. I then read `Doc_03_Lexicon_Candidate_List.md` and `Doc_06_Full_Lexicon_Development.md` in full, `Lexicon_Deployment_Index.md` in full, all 19 `Lexicon-Chunks/` files in full, `wb_lpc_s22.py`'s own docstring and body in full, and the relevant `term`/envelope sections of `engine/m1/schemas.py`. I read `worlds/lpc/Review-Artifacts/RecordCompilation_Part1_Round1_Review.md` for reporting format. I read all 19 `records/lpc/term/*.md` files (five by direct tool read against the script's literal source, the remainder parsed programmatically alongside the five). I independently re-derived, by parsing every file's YAML front matter directly rather than trusting any stated count: the source-reference bijection, the relations graph (122/61/0), every confidence/tier/distortion_risk enum's distribution, and the guard-marker scan of every `prefer_instead` clause.

---

# MEDIUM Finding

## M1 — `evidentiary_weight: load-bearing` on the two down-tiered conciliar formulas is a disclosed but chunk-unstated authored call

**Where:** `lpc.term.bishop-of-bishops` and `lpc.term.plenary-council`.

**What's wrong:** Both chunks (`lpclex012`, `lpclex013`) state plainly that Doc_04 finds no evidence the conciliar-authority question reached ordinary formation, and both are Tier 2 on that ground. Neither chunk's own Key Sources section uses the phrase "load-bearing" or an equivalent term for either formula. The script sets `evidentiary_weight: load-bearing` on both anyway, reasoning in its own provenance note that "this formula is the sole textual ground of a real, Documented Supporting gravity... Tier and evidentiary_weight are independent axes." That reasoning is sound and is stated openly in the record's own provenance note (not hidden), but it is the drafting agent's own inference about the chunk's implications, not a value the chunk itself supplies — a distinction the script's docstring elsewhere is careful to keep (e.g. explicitly separating "MECHANICAL" from "AUTHORED" field decisions), but does not flag this particular call as an authored one in the same explicit register it uses for others.

**Why MEDIUM, not HIGH:** the underlying claim (each formula is real, verbatim-attested, and the sole ground of a Documented Supporting gravity) is true and independently verifiable in the chunk; nothing is invented. This is a documentation-precision gap in how the authored/mechanical line is drawn, not a fabricated evidentiary claim.

---

# LOW Findings

## L1 — `suffrage`'s carried DR/tag tension is repeated as a script-level policy statement rather than cross-checked against the record's own `distortion_risk` field once more

The script's docstring and the `suffrage` record's own `divergence_note` both correctly state, and do not resolve, the pre-existing Index §3 tension (no `[DR]` tag despite Doc_06 naming it a sharpest-case distortion). The record's `distortion_risk: medium` is the correct mechanical mapping from the tag set. Noted only because a future pass that resolves the Index-level tension (adding `[DR]` to `suffrage`) will need to remember this record's `distortion_risk` should then also change to `high` — nothing here currently instructs that follow-through, so the two carried instances (Index tag, term-record enum) could drift out of step with each other even after the upstream tension is finally resolved.

## L2 — `bishop-of-bishops`/`plenary-council`'s "load-bearing" reasoning is stated twice, once per record, with no shared cross-reference

The independent-axis reasoning behind M1 is written out separately in both records' own provenance notes rather than in one place either record points to. Not a defect in either record — both are individually correct and disclosed — but it is the same kind of duplication-instead-of-cross-reference this project's own `Lexicon_Deployment_Index.md` §5 item 6 material names as a recognized pattern to watch for elsewhere in this build.

---

# COSMETIC

`lpc.term.libelli`'s `divergence_note` refers to "`lpc.term.certificates`," but the actual record id is `lpc.term.certificates-letters-of-peace`. The cross-reference is unambiguous to a human reader in context and does not affect any resolved field (relations/sources use the correct full id throughout), but a future automated cross-reference sweep over free-text `divergence_note` fields would not resolve this one.

---

# What I checked and found solid

- **19 term records ↔ 19 Lexicon-Chunks, exact 1:1 by slug**, matching the directory listing with no omission, extra emission, or silent merge.
- **Source-reference bijection:** 18 distinct `source_id` values used across all 19 records, all resolving to real files in `records/lpc/source/`, zero misses.
- **Relations graph, re-parsed from the 19 disk files directly:** 122 directed edges, 61 reciprocal pairs, zero one-way links, zero duplicate edges — independently reproducing the drafting agent's and the Index's own claimed count.
- **Envelope and confidence-block schema conformance, all 19 records:** every enum value (citation_specificity, verification_state, evidentiary_weight, formation_confidence, distortion_risk, retrieval.tier) falls inside `engine/m1/schemas.py`'s declared set; `register`, `status`, `schema_version`, `canon_cells`, `world_id` uniform and correct.
- **Guard-marker scan, all 19 records' `prefer_instead` clauses:** zero matches against `engine.prose.GUARD_MARKERS`, confirming `claim_guards` is legitimately empty everywhere rather than a dropped field.
- **Tier assignment, all 19:** matches Doc_06 §2's 7/12 split and every individual movement (four down-tiered, two corrected upward, one added) exactly.
- **CT Contest Type, all three tagged terms:** carried into the record non-templated and matching Doc_06 §3's stated contest type.
- **Quote fidelity, all 19 chunks against their records:** every direct quotation carried forward is verbatim, including the corrected certificate wording ("were daily given, contrary to the law of the Gospel").
- **Editorial-apparatus exclusion:** the Schaff verdict on Augustine's coercion doctrine is correctly excluded from `lpc.term.compel-them-to-come-in` in its entirety.
- **Byte-level drift check:** five records read directly from disk (certificates, suffrage, grace, libelli, heresy) match the script's own literal source exactly.
- **No invented content anywhere:** no confidence upgrade, tier reassignment, source citation, or quotation found in any of the 19 records that its own Lexicon-Chunk, Doc_03, Doc_06, or the Deployment Index does not itself state.

---

# Recommended disposition

**Cleared Review.** M1 is a documentation-precision note (explicitly label the independent-axis reasoning as an authored call in the script's own docstring register, or add a one-line cross-reference between the two paired records) rather than a substantive defect — the underlying claim is true and already disclosed. L1 and L2 are forward-looking hygiene notes, not current errors. C1 is a one-word id-string fix inside free text. None blocks proceeding, and per this project's capped-review-cycle discipline, a targeted recheck of the corrected fields (not a full re-review) is sufficient for a Round 2, if one is run before these are folded into a later mechanical pass.
