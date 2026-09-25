# World Methodist-Revival (`meth`) — Decision Log

**World-code:** `meth`, assigned at Step 0, this world's first document.

This log holds the review-round history, revision rationale, and escalation checks for each document in this world's build, so the construction documents themselves stay clean, substantive content. Review artifacts live in `Review-Artifacts/`; this log summarizes what happened and why, per document.

**Disposition vocabulary in use (per `cic-build-cycle`):** Cleared review / Approved to proceed (self-applied by the build thread when no escalation category applies; claims nothing about completeness or closure) / Frozen (never self-assigned by the build thread; the project lead's own act).

**Standing limitation across every entry below, stated once here rather than repeated three times:** every review round recorded in this log was conducted by this same build thread in a separate adversarial analytical pass, not by an independently spawned model instance — no lightweight subagent-spawning tool with model selection was available in this session, and the only alternative (a full, heavyweight Claude Code Remote session) was judged disproportionate for iterative per-document review. See `Step0_Movement_Scope_Confirmation.md` §6 and `Open_Gaps_Tracking.md` item 3 for the full disclosure. Genuine independent review of all three documents remains a standing, owed item.

---

## Entries

### 2026-09-25 — Step 0 (Movement-Scope Confirmation)

- **Document:** `Step0_Movement_Scope_Confirmation.md`.
- **Review rounds:** 1 (`Review-Artifacts/Step0_Review_Round1.md`) — **COSMETIC ONLY.** One arithmetic error found and fixed directly (a transposed years-since-Nicaea/Chalcedon figure); two low observations (a recommended-but-not-required future improvement; a documentation-style judgment call).
- **Escalation check:** none of the four categories applies. Two genuine Article 21 strand questions (Wesleyan/Calvinistic; British/American) and the Moravian cross-world relationship are named as real, open items for Doc_01 — not decided here, and naming an open question is not itself an escalation.
- **Disposition:** Approved to proceed, self-applied.

### 2026-09-25 — Doc_01 (World Identification, Boundaries, and Orientation)

- **Document:** `Doc_01_World_Identification_Boundaries_Orientation.md`.
- **Review rounds:** 1 (`Review-Artifacts/Doc01_Review_Round1.md`) — **COSMETIC ONLY.** Three low findings, all fixed directly: an overprecise, unverifiable claim about how many British-born itinerants remained in America during the Revolutionary War (softened to what this pass can actually support); a leftover drafting artifact (a bracketed self-correction note reading like process narration) removed from the document body; a confirmation check that the Whitefield world-separation test (§4) and the Strand Determination (§5) reach opposite conclusions for defensible, non-contradictory reasons (confirmed clean, no revision needed).
- **Real decisions this document makes, not merely carries forward from Step 0:** (1) George Whitefield's own Calvinistic Methodism is a separate, contemporary movement, not a strand of this world (§4) — argued on the Framework's own six-question method, corroborated by the census's own scope (no Whitefield source named, no descendant tradition traced through his line). (2) One world, two strands — British (Wesley, then the Wesleyan Conference) and American (Asbury, the Methodist Episcopal Church from 1784) — bridged by Wesley's own authority until 1791 and by shared doctrine/hymnody, separated by a genuinely different authority structure (connexional/no bishop vs. episcopal) and formation-ecology problem (§5). Neither decision required escalation: both are this world's own scope-determination, on this world's own evidence, touching no other census entry's own boundary.
- **Escalation check:** none of the four categories applies. The Moravian relationship (§7) is stated in full and carried to `Open_Gaps_Tracking.md` item 2 as an open question for a future build thread — this document does not decide policy for VII.4, so this does not cross into the portfolio-level category.
- **Disposition:** Approved to proceed, self-applied.

### 2026-09-25 — Doc_02 (Source Ecology), Source Registry, Source Acquisition Manifest

- **Documents:** `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Source_Acquisition_Manifest.md` — co-equal Step 2 outputs, built and reviewed together.
- **Review rounds:** 1 (`Review-Artifacts/Doc02_Review_Round1.md`) — **COSMETIC ONLY.** One genuine counting error found and fixed directly (Doc_02 §1 stated "eight corpus-map rows across seven vendored files"; the actual generated corpus-map bucket carries eleven rows across seven files — recounted directly against the file, not assumed); two confirmation checks (the holdings-tool failure was independently re-run rather than trusted from the document's own account; the Author Gravity Assessment's own claim about a thin 1739–1790 Wesley corpus was checked against Doc_01's separate claim about Wesley's ongoing authority over Asbury for a silent contradiction — none found, the two documents draw on different evidence and neither overclaims from the other's).
- **A structural mismatch, not a defect this build thread introduced:** this build's own launch instruction expected a per-item "holdings disposition" via `engine.m9.cli holdings meth` before this document's review. That tool requires a Phase-B WRS record store (`records/meth/`) that does not exist for any world at the Library stage (Step 0–Doc_02) — confirmed by directly running the command and reading the resulting traceback, not assumed from the tool's own description. This document's own Source Registry (22 rows, each with an explicit Confidence A–E and Verification Note) serves the equivalent function this stage's own actual governing document and precedent (`worlds/rzg/Source_Registry.md`) call for. Logged in full at `Open_Gaps_Tracking.md` item 15.
- **Escalation check:** none of the four categories applies. The holdings-tool mismatch is reported as a finding, not resolved here as a change to the governing process itself.
- **Disposition:** Approved to proceed, self-applied, for all three documents together.

---

## Summary: what this build thread decided on its own authority, and what it left open

**Decided (this world's own scope-determination, no escalation required):** Whitefield/Calvinistic Methodism as a separate contemporary movement, not a strand (Doc_01 §4); British/American as two strands of one world (Doc_01 §5); the registry code `meth` (no collision); the doorway event and date (24 May 1738, Aldersgate).

**Named as open, not decided (correctly left for a future thread or the project lead):** the Moravian Church at Herrnhut's own eventual relationship-characterization (a future VII.4 build thread's or the project lead's call); Living Tradition Status confirmation (the project lead's own act, later); the Representative-structure question — single-figure or multi-figure, and which strand(s) — reserved for Step 10 per this build's own escalation categories.

**Flagged as a process/tooling finding, not a content decision:** the "V1.8"/holdings-tool version mismatch (`Open_Gaps_Tracking.md` items 1, 15); the standing review-independence limitation (item 3).
