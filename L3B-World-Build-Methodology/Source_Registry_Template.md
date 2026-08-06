# Source Registry Template

**Version 1.0. Companion to Doc_02 (Source Ecology) — the two are built together as the two co-equal outputs of Step 2, per the Formation World Construction Framework V7.4. Filed in L3B-World-Build-Methodology. Supersedes the "Doc_02B Approved Source Database" naming and design (V1.0, V2.0 draft): this is not a later, subordinate step bolted onto Doc_02 after the fact, and it is not numbered as if it were. It is the second, structured output of the same Step 2 evidentiary pass.**

---

## What this is, and why it is built together with Doc_02, not after it

Doc_02 answers what the evidentiary situation of this world is, and how confident the project should be in it — that is narrative-and-judgment work, and it stays exactly that. The Source Registry answers a different, sharper question about the same material: of everything Doc_02 names, exactly which sources may this world's own voice actually draw specific, vivid material from — and which may not, and why?

These were once built as one step and then a separate, later step ("Step 2B"), the second one added only after a real defect was found in an already-completed world (Alexandria/Theon: vivid theosis and burning-bush imagery traced to Gregory of Nyssa, a different world's own source, borrowed unmarked into the Representative's generated content). Building them together, in one pass, is a real improvement for an ordinary reason: it means the Registry exists as a matter of course by the time later steps need it, rather than depending on someone remembering to schedule a separate pass. It does not, by itself, prevent the kind of defect that motivated building this mechanism at all — see the next paragraph, stated plainly rather than implied.

**What this document does and does not protect against — stated honestly, because an earlier draft of this mechanism overclaimed this exact point.** Gregory of Nyssa was never a source anyone had listed for Alexandria. The defect was not a tagging failure; it was the Representative's generation reaching, unconstrained, into the model's own broader training knowledge for a more famous treatment of a shared image. A Registry — however complete, however well-tagged — only classifies sources someone has already proposed as candidates. It cannot, by itself, stop a model from reaching for something nobody proposed. **The actual mechanism that closes that failure is downstream of this document**: the Representative's Permanent Prompt carries a short grounding-anchor paragraph (Template Section 2A — Approved Source Anchoring, added specifically to hold this line) naming specific approved anchors and instructing a fallback to plain tradition-level speech rather than a borrowed vivid image. That paragraph is what constrains generation. This Registry's job is to be the well-curated, boundary-checked source *this world actually used* that the grounding-anchor paragraph gets distilled from — necessary groundwork for the real fix, not the fix itself. Treat this document as the quarry, and Step 10's distillation into the Permanent Prompt as the wall.

## Position in the build sequence

**From Doc_01**, the Registry receives the one thing its core check depends on: the world's own stated temporal, geographic, and cultural boundary. The Registry does not set this boundary or second-guess it — that is Doc_01's own work.

**Built together with Doc_02**, not received from it as a finished input: as each source is identified and assessed for the ecology narrative, it is classified in the Registry in the same pass.

**To Doc_03** (Lexicon Candidate List) and every step after it, the Registry hands forward only its Native entries as the legitimate evidentiary base for a lexicon term, a gravity, a force, or a story. A term whose only supporting source is Excluded has not earned a place in this world's own vocabulary, however well-attested that source is in the general literature.

## Scope of this version

This template governs a single world's own Registry: what belongs to this world, on this world's own terms, checked against this world's own Doc_01 boundary. It does not attempt to check a candidate source against what any other world has already claimed as native — that is a genuinely different, harder problem (a mechanism that has to hold up across dozens of worlds, not protect one), and an earlier attempt to solve both problems in one document at once produced a design that did neither well. Cross-world checking is intentionally left as open, named follow-up work, not folded in here.

## Two independent classification axes, plus a mandatory boundary check

**Axis 1 — Source Type:**

| Type | Definition |
|---|---|
| **P — Primary** | The world's own actual texts: writings, conciliar acts, liturgical texts, letters, from within or near the world's own documented span. |
| **S — Secondary** | Modern scholarship used to interpret, date, corroborate, or contextualize primary material. |
| **M — Material/External** | Archaeology, papyrology, comparative social history, material culture. |
| **L — Period Lexicon** | Dictionaries and reference works keyed to the actual period and language. |

**Axis 2 — Citation Reliability:**

| Tier | Definition |
|---|---|
| **A** | Verified this session against an accessible primary source, translation, or authoritative reference. |
| **B** | Specific work/locus named, not independently re-checked this session. |
| **C** | Tied to a real author/work, no specific locus pinpointed. |
| **D** | Tradition/genre-level attribution, no specific text/author named. |
| **E** | No traceable source. Not a resting tier — remove or re-ground to at least D. |

**The Boundary Check (not an axis of degree — a binary gate, run on every entry):**

Assign every source a **Boundary Status of Native or Excluded**, assessed by what the source speaks *for* — its own subject, tradition, or evidentiary target — checked against Doc_01's stated boundary. This is the rule that matters most and the one an earlier draft of this mechanism got wrong: **Boundary Status is never assessed by the date a piece of scholarship happened to be written.** A monograph published last year about this world's own ancient sources is Native, because its subject is this world. A source — of any Type, including Primary — whose own subject or origin belongs to a different era, place, or tradition is Excluded, however well-regarded or however recently written. This is the same evidentiary act the Forces Framework requires under a different name: its Step 2 mandate that Author Gravity assessment include "transmission history as a named dimension" is asking the same provenance question this Boundary Check answers. Do them together, in one pass, rather than as two separate judgments about the same source.

**Native does not mean exclusive to this world, and it was never supposed to.** This project is not in the business of manufacturing artificial differentiation between worlds. Real historical traditions inherit from and cite one another constantly — Scripture is native to every one of these worlds; a later figure may draw directly and legitimately on an earlier one from a different world entirely (Calvin's own use of Augustine is the standing example: real inheritance, not contamination). The question this check asks is never "does another world already have this" — it is simply **"was this source actually used, inherited, or drawn on as part of this world's own formation, on this world's own evidence?"** If yes, it is Native here, whether or not it is also, independently and correctly, Native somewhere else. The failure this mechanism exists to prevent is not overlap — overlap is often exactly right — it is a source appearing in this world's material that this world's own record gives no actual basis for.

For every Excluded source, record an **Exclusion Reason.** This is not a formality — it is the distinction an earlier version of this mechanism collapsed and lost real information by collapsing:

| Exclusion Reason | Meaning |
|---|---|
| **Out-of-Boundary** | A straightforward temporal or geographic mismatch against Doc_01. The source was never a serious candidate for this world's own voice; it is recorded here mainly for completeness, or because it appeared in a source Doc_02 needed to discuss. |
| **Named Comparandum** | A source easily mistaken for native — most often a neighboring tradition's more famous, more vivid treatment of a similar theme, text, or figure — deliberately recorded as a warning. This is the entry type that exists specifically so a builder, or the Representative itself, never reaches for it without knowing it belongs elsewhere. |

A source that fails the Boundary Check does not stop being worth recording — it stops being worth *licensing.* Both Exclusion Reasons still get a Verification Note explaining what was checked; only a Named Comparandum additionally needs a clear statement of the specific image, claim, or reading it must not be mistaken for.

## Entry schema

| Field | Content |
|---|---|
| **#** | Sequential ID, never reused. |
| **Source** | Full citation: author, title, specific book/chapter/letter, edition/translation if checked. |
| **Type** | P / S / M / L (may combine). |
| **Confidence** | A–E. |
| **Boundary Status** | Native / Excluded. |
| **Exclusion Reason** *(required if Excluded, blank if Native)* | Out-of-Boundary / Named Comparandum. |
| **Licensed For** *(required if Native, blank if Excluded)* | The specific gravity, force, lexicon term, or Representative trait this source justifies. A Native source with nothing named here is not yet usable downstream. |
| **Verification Note** | What was checked, when, against what. |
| **Comparandum Note** *(required if Named Comparandum)* | The specific claim, image, or reading this source must not be mistaken for being this world's own. |
| **Added** | Date and who/what added it. |

## Builder process — done as one pass with Doc_02, not after it

1. As each source is identified during Doc_02's ecology-building work (primary voices, secondary scholarship, material culture, formation-narrative sources), classify it here in the same session: Type, Confidence, Boundary Status.
2. For anything Excluded, assign the Exclusion Reason and, if it's a Named Comparandum, write the Comparandum Note explaining the specific temptation it represents.
3. For anything Native, name its Licensed-For target before moving on. A source without one is not finished being processed.
4. Flag for independent second-opinion review anything where the source was discovered from the builder's own prior knowledge and not independently re-collated this session (`discovery_channel: builder-prior-knowledge`, `verification_state` not `verified-direct`) and it licenses a load-bearing, vivid, specific claim (`evidentiary_weight: load-bearing`). *(Re-keyed 2026-08-05, full-system review Rigor P1-2, off the SS3.0 discovery-channel/verification-state/evidentiary-weight axes — mechanically enforced by `wrs/gates/core.py::gate_priority_review_trigger`. The prior rule, "Flag anything at Confidence C or below," assumed the Confidence letter's B still meant "specific work/locus named"; after the Round-1 recalibration redefined B to mean recall, the legacy letter stopped marking the actual risk boundary.)*
5. The Registry's structure and every source currently known are complete as part of this same Step 2 pass — not left for later. What legitimately comes later is growth: as Steps 3 through 10 surface new candidate sources, append them here under the same rules, in the same living, append-only discipline (never renumber, never remove — a source later found unreliable moves to Confidence E and is marked removed-from-use, but the entry stays as a record of what was tried).

**Checkpoint, not just intent:** Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row. This is the one rule in this process that actually catches a builder who writes all of the ecology narrative first and treats the Registry as an afterthought — if a claim in Doc_02 cannot be traced to a Registry entry, Step 2 is not finished, regardless of how complete the narrative reads.

## How Phase 5 (Representative construction) and runtime use this document — this is where the actual protection happens

Everything above builds and tags the material. It does not, on its own, stop a Representative from generating something ungrounded — that happens here. The Representative's own Approved Source List (feeding the Permanent Prompt Template's grounding-anchor paragraph, Section 2A — Approved Source Anchoring) is a small, 5–10 entry distillation of the Registry's Native entries — not fresh research, and not the full Registry. **This distillation, and the grounding-anchor paragraph it produces, is not optional polish on top of a finished Representative — it is the load-bearing mechanism this entire document exists to feed.** A world with an exemplary Registry and no grounding-anchor paragraph in its deployed prompt has the groundwork for protection and none of the protection itself.

The full Registry also has a runtime role: Constitution Article 30 (Layered Accessibility & Progressive Depth) guarantees participants a Level 3 disclosure — sources with specificity, confidence, and the complete construction record, reachable on request and never gated. The short grounding-anchor paragraph stays resident on every turn, cheap, behavioral. The full Registry is what should be retrievable on request to satisfy Level 3 — not carried in every turn's context whether asked for or not. Where this two-tier design isn't yet wired into the runtime layer, that is a dependency for that layer's own build, not something this template completes on its own.

## Living-document protocol

Append-only, no renumbering, no deletion. A source later found unreliable is marked at Confidence E and disposition removed-from-use, but stays in the table as a record of what was tried and why it was rejected.
