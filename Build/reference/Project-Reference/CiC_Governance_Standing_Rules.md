# CiC — Governance Standing Rules

*A living reference for cross-cutting process rules this project has adopted during construction work, outside the formal Constitution (`Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`). Not a replacement for the Constitution — a record of standing operational decisions made by the project lead during actual build work, so they don't have to be rediscovered or reargued world by world. Entries are appended as new standing rules are adopted; existing entries are not deleted, only marked superseded if a later decision changes them.*

---

## 1. Two-tier approval model (adopted 2026-07-08)

**Prior practice:** documents that cleared independent adversarial review were described as "Cleared review — pending project-lead sign-off," and once the project lead approved a document in chat, it was recorded as "Signed off by project lead," treated as a settled, non-self-certified approval.

**Problem:** a single-document review — even a genuinely independent, adversarial one — cannot catch everything a later system-level review, cross-document consistency check, or actual runtime testing can catch. World #7's own build surfaced a concrete example: Voice Construction was signed off, and only later, during Phase Four's own review, did an unsourced claim in Voice Construction's Section 2 come to light. Treating "signed off" as if it meant "beyond further correction" doesn't match how the project actually learns things — the project lead wants to stay genuinely open to revision through testing and use, not just in theory.

**New rule, adopted by the project lead 2026-07-08 (World #7 build, in chat):**

- **"Approved to proceed"** replaces "Signed off" as the language for project-lead approval of an individual document during construction. It records that the project lead has reviewed the document and authorizes the build to continue past it. It explicitly does **not** mean the document is final, frozen, or beyond correction.
- **No document reaches a closed, non-revisable status until:** (a) Step 10 Phase Five (Boundary Testing / Validation) has run its full probe battery against the built Representative, and (b) any full-system or full-world-level review relevant to that document has been completed. Only after both conditions are met does a document move to its actual closed state.
- **The word "finalized" remains permanently banned** for describing any document's status, at any tier, under any circumstance — this rule predates and is unaffected by the two-tier model above.
- **This is a relabeling, not a devaluation.** A project lead's "Approved to proceed" is still a genuine, non-self-certified approval — distinct from a document merely being "Cleared review" by an independent adversarial pass with no project-lead decision yet made on it at all. The two-tier model adds a ceiling above "Approved to proceed," it does not remove the floor beneath it.
- **Retroactive application:** this rule applies going forward and was also applied retroactively to the one document that had already received old-style "Signed off" language (World #7's Voice Construction, Step 10 Phase Three) — relabeled 2026-07-08 without reopening or diminishing the actual approval given on 2026-07-07.

**What "closed" gets called once Phase Five and system review actually complete** has not yet been decided — this project has not reached that point for any world yet. To be named when the situation first arises.

**Terminology note on existing documents:** Doc_01–09 and Phase One/Two of World #7 (and any other world's documents written before 2026-07-08) still read "Cleared review — pending project-lead sign-off." That phrase describes a document awaiting a project-lead decision that has not yet been made at all — it is not describing a decision already given the old "final" treatment, so it is not factually wrong, just pre-dating this rule's vocabulary. These have not been mass-edited to the new wording; when the project lead actually approves one, it should be recorded as "Approved to proceed," per this rule, regardless of what the pre-approval status line said. Documents can be updated to the new wording opportunistically as they're touched for other reasons, rather than as a dedicated sweep.

---

## 2. Other standing rules already in force (recorded here for consolidation, not newly adopted)

- **Simulated review labeling (Constitution Article 35, Section B):** every independent review round conducted by a dispatched agent, not a human external reviewer, must be saved as a standalone file beginning with the literal line "Simulated review — informational only, not an Article 31 substitute." This is never a substitute for Article 31's actual external scholarly accountability requirement.
- **Mandatory truncation check:** every review round must verify document completeness via two independent methods (direct file-read tool, plus an independent bash-level check) and report raw evidence, due to a documented, recurring, access-path-specific file-staleness bug in this project's own environment (bash-mounted file views can lag behind edits made through the direct file-access path for some period). When the two methods disagree, the direct file-access path is authoritative, but the dismissal of any such disagreement must itself be confirmed by a further independent party before being treated as resolved — see the next rule.
- **No self-certified dismissal of a blocking review finding.** If a drafter-side investigation dismisses a review's blocking finding (including a dismissal attributed to a known environment bug), that dismissal must be confirmed by a further, genuinely independent review round before the finding can be treated as closed. Adopted after Doc_06's build surfaced a case where a self-certified dismissal of a truncation finding had been treated as sufficient on its own.
- **Substantial vs. cosmetic revision threshold:** a finding is substantial if it changes a claim's substance, confidence rating, sourcing conclusion, or scope boundary; cosmetic if it is wording, tone, formatting, or a typo only. Substantial findings require a fresh independent review round; cosmetic findings may be applied directly without one.
