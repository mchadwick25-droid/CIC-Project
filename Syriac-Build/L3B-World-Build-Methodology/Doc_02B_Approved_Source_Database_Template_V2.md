> **SUPERSEDED — 2026-07-04.** This draft was sent back for substantial rework by an Opus deep review (see `L2C-System-Status/CiC_Pipeline_Decision_Log.md`), which found its central justifying claim inaccurate and its Boundary/Shared-status design broken on real content. Rather than patch it, the project lead directed a complete rework of the Step 2 process that combines Source Ecology and source-tagging into one step, per-world only (cross-world checking deferred as separate follow-up work). See `Source_Registry_Template.md` for the current, live design. Kept here, unmarked-as-deleted, as the historical record of what was tried and why it didn't hold up — per this project's own Record Integrity Principle.

---

# Doc_02B — Approved Source Database Template

**Version 2.0. Companion to Doc_02 (Source Ecology), which is retroactively understood as Doc_02A from V1.0 forward. Filed in L3B-World-Build-Methodology alongside the Representative Permanent Prompt Template and the other build framework documents. Supersedes V1.0, which was built and tested once, mid-cycle, on a single completed world (Alexandria/Theon) after a defect was already found. V2.0 is a design pass, not a patch: it is built for a world-build process that will run dozens of times, not five, and it closes two things V1.0 left to a builder's judgment rather than to a mechanical check.**

---

## Governing framing

A formation world's Representative speaks for that world alone: in itself, from itself, and as itself. It does not speak as a scholar describing the world from outside, and it does not speak with another world's inheritance borrowed in, however similar, however famous, however close in era. Every mechanism in this document exists in service of that one commitment. Doc_02B is not external fact-checking apparatus bolted onto a world that doesn't carry it natively — it is how the world's own voice stays uncontaminated by a different self. Where this document requires a check, a boundary, or a default-exclusion, the reason is always the same: to protect a world's ability to speak only as itself.

## What this document is, and why it exists

Doc_02A establishes a world's evidentiary basis at the level of confidence and pattern: which claims are Documented, Widely Accepted, Contested, or Inferential-Thin (Constitution Article 17), and which streams of evidence the ecology rests on. On its own, it has never produced an itemized, retrievable, *checkable* list of the actual named works behind that assessment. Doc_02B is that list — and, as of V2.0, it is also the gate every candidate source passes through before it is allowed to shape anything downstream of it.

This gap was found the hard way (`Cross_World_Roundtable_Validation.md`, Parts XVIII–XIX): a Representative (Theon, Alexandria) passed every grammar and fabrication check cleanly while still generating vivid, specific imagery borrowed from a neighboring tradition's more famous treatment of the same text — fluent, plausible, and wrong, because nothing in the build process had given the Representative a bounded, real list of what it was actually allowed to reach for. A second, structurally different failure (Chloe, Early Communal — Part XX) showed the same underlying problem from a different angle: a source roughly fifty to eighty years *past* her world's own stated horizon shaped a controversy narrative that read as native but wasn't. One was a wrong-tradition problem; the other was a wrong-era problem inside the *same* broad tradition. V1.0 only built a mechanical answer to the first. V2.0 builds a mechanical answer to both, because at five worlds a builder can plausibly hold every other world's content in their head; at forty, they cannot, and a defect caught only by a builder's memory is a defect that will recur.

## Relationship to Doc_02A — division of labor, stated plainly so the two are never duplicated

**Doc_02A answers: what is the evidentiary situation of this world, and how confident should we be in it?** Primary and secondary voices, institutional and material evidence, the Author Gravity and Missing-Voices assessments, the narrative account of what the world's sources let us know and how well. This is judgment-and-narrative work, and it stays in Doc_02A.

**Doc_02B answers: of everything Doc_02A named, exactly which items may this world's Representative actually draw specific, vivid material from — and which may not, and why?** This is classification-and-gate work: every candidate source gets a small number of hard fields (below), not prose argument. A builder should never have to re-litigate an evidentiary judgment inside Doc_02B — if Doc_02A hasn't already established that a source belongs to this world's evidentiary base, Doc_02B is the wrong place to establish it; go back to Doc_02A first.

## Position in the build sequence: Doc_01 → Doc_02A → Doc_02B → Doc_03

This is the seam V1.0 left implicit and V2.0 makes load-bearing.

- **From Doc_01**, Doc_02B receives the one thing every Boundary Check (below) is run against: the world's own stated temporal boundary, geographic boundary, and strand/cultural scope. Doc_02B does not re-derive or second-guess this boundary — it is Doc_01's to set. Doc_02B's job is to hold every candidate source to it, mechanically, every time.
- **From Doc_02A**, Doc_02B receives the candidate sources themselves — the primary voices, secondary scholarship, material evidence, and formation-narrative sources Doc_02A has already assessed as belonging to this world's evidentiary base.
- **Doc_02B's own work** is to run every one of those candidates through the Boundary Check and the Cross-World Registry Check (below) before assigning it a Licensed-For target, and to hold anything that fails either check at Comparandum-Excluded by default rather than by a builder's afterthought.
- **To Doc_03** (Lexicon Candidate List), Doc_02B hands forward only its Native and Shared/Pan-Tradition entries as the legitimate evidentiary base for a lexicon term's Key Sources. A term whose only supporting source is Comparandum-Excluded has not yet earned a place in this world's own vocabulary, however well-attested that source is in general patristic or historical literature. **Note for the Construction Framework itself:** Step 3's current activity list reads "Identify recurring terms from source ecology" — this should be read, and eventually revised in the Framework's own text, as "from Doc_02B's approved set," not raw Doc_02A, once this template is ratified. That is a small, specific edit to queue against the Framework document, not something this template can enforce on its own.

The practical effect: by the time a builder reaches Doc_03, every source they might cite for a candidate term has already been cleared of the two failure modes this project has actually found. Lexicon, gravities, stories, and eventually the Representative's own voice are all built downstream of a source base that is clean *by construction*, not audited for cleanliness after the fact.

## Three independent classification axes

V1.0 had two axes (Type, Confidence). V2.0 adds a third (Boundary Status) as a first-class, mandatory field — not a note in the NOT-approved-for column, which is where V1.0 left this judgment and which is exactly what let it stay discretionary.

**Axis 1 — Source Type** (unchanged from V1.0):

| Type | Definition |
|---|---|
| **P — Primary** | The world's own actual texts: writings, conciliar acts, liturgical texts, letters, from within or near the world's own documented span. |
| **S — Secondary** | Modern scholarship used to interpret, date, corroborate, or contextualize primary material. |
| **M — Material/External** | Archaeology, papyrology, comparative social history, material culture. |
| **L — Period Lexicon** | Dictionaries and reference works keyed to the actual period and language. |

**Axis 2 — Citation Reliability** (unchanged from V1.0):

| Tier | Definition |
|---|---|
| **A** | Verified this session against an accessible primary source, translation, or authoritative reference. |
| **B** | Specific work/locus named, not independently re-checked this session. |
| **C** | Tied to a real author/work, no specific locus pinpointed. |
| **D** | Tradition/genre-level attribution, no specific text/author named. |
| **E** | No traceable source. Not a resting tier — remove or re-ground to at least D. |

**Axis 3 — Boundary Status (new in V2.0):**

| Status | Definition | Default licensing consequence |
|---|---|---|
| **Native** | Falls inside this world's own Doc_01 temporal and geographic boundary, and is not already claimed as Native by a different world in the Cross-World Source Registry. | Eligible for a Licensed-For target — this world's own voice may draw from it. |
| **Shared / Pan-Tradition** | Falls outside a single world's exclusive claim by its nature, not by oversight: Scripture itself; a source that predates every existing world's horizon and is inherited in common; a figure or text explicitly recorded in *multiple* worlds' own Doc_02A as part of their shared pre-history. This status must be affirmatively justified in the Verification Note, not assumed. | Eligible for a Licensed-For target in every world that legitimately shares it, with the shared claim recorded in the Registry so it is never mistaken for an oversight later. |
| **Comparandum — Excluded** | Falls outside Doc_01's boundary (temporal or geographic), OR is already claimed as Native by a different world in the Registry without a recorded Shared justification. | **Not** eligible for a Licensed-For target. May still be named in Doc_02A's own narrative discussion, or in this document's NOT-approved-for field, purely to explain why it is excluded — never as material the Representative draws from. |

The default posture is exclusion, not inclusion. A source does not need a reason to be excluded; it needs a reason — Native by Doc_01's own boundary, or an affirmatively recorded Shared justification — to be included. This inverts V1.0's practice, where NOT-approved-for was something a builder added if they happened to think of it. It is now the default outcome of two checks every source must pass.

### The Boundary Check (temporal/geographic — mechanical, not a judgment call)

For every candidate source, compare its date and place of origin directly against Doc_01's stated boundary. If it falls outside — even narrowly, even within the same broad tradition — it is Comparandum-Excluded by default. This is the check that would have caught Chloe's Novatian-adjacent material (roughly fifty to eighty years past her ~70–200 AD horizon) at construction time, before it ever reached a lexicon term, a gravity, or a story, rather than at adversarial-testing time, after a Representative had already been built and deployed.

### The Cross-World Registry Check (cross-tradition — mechanical, not a judgment call)

Before any source is finalized as Native, check it against the **Cross-World Source Registry** (`L3B-World-Build-Methodology/Cross_World_Source_Registry.md`), a single living index shared by every world's build. If the source (by author, specific work, era, and tradition) is already registered as Native to a different world, and no Shared justification is recorded, it defaults to Comparandum-Excluded here. This is the check that would have caught Theon's Nyssa/epektasis material mechanically, from a registry lookup, rather than requiring a builder to happen to know Cappadocian theology well enough to recognize the borrowing. Once a world's Doc_02B is finalized, its new Native entries are appended to the Registry (living, append-only, never renumbered or removed) so every subsequent world's build benefits from every prior one's — this is the specific mechanism that lets the project scale past the point where one person can hold all built worlds in their head.

## Entry schema

| Field | Content |
|---|---|
| **#** | Sequential ID, never reused. |
| **Source** | Full citation: author, title, specific book/chapter/letter, edition/translation if checked. |
| **Type** | P / S / M / L (may combine, e.g. a critical edition with a scholarly introduction). |
| **Confidence** | A–E. |
| **Boundary Status** | Native / Shared–Pan-Tradition / Comparandum–Excluded, per the two checks above. |
| **Licensed For** | What this source justifies — a Doc_04 gravity, a Doc_08 force, a specific Doc_06 lexicon entry, or a named Representative trait. Left blank for anything Comparandum-Excluded; an entry with Native or Shared status but nothing named here is not yet usable by the grounding-anchor mechanism (Template §3) and should not be cited by a Representative. |
| **Verification Note** | What was checked, when, against what — and, for Shared status, the affirmative justification required above. |
| **NOT-approved-for note** *(required whenever Boundary Status is Comparandum–Excluded; optional but encouraged otherwise)* | Names the specific adjacent claim or image this source does not support here, and (where relevant) which world it *is* native to per the Registry. |
| **Added** | Date and who/what added it. |

## Builder process for a new world

1. Pull forward every source Doc_02A has already established as part of this world's evidentiary base, plus any lexicon entries' own Key Sources sections if any exist yet.
2. For each candidate source: confirm it exists and confirm the specific claim it supports (unchanged from V1.0).
3. **Run the Boundary Check.** Compare the source's date and origin against Doc_01. Anything outside the boundary is Comparandum-Excluded, full stop, unless it earns Shared status under the affirmative-justification standard above.
4. **Run the Cross-World Registry Check.** Look the source up in the Registry. Already claimed elsewhere without a Shared justification means Comparandum-Excluded here.
5. For everything that survives steps 3–4 as Native or Shared, assign Type, Confidence, and a specific Licensed-For target.
6. Flag for independent second-opinion review any row where the source was discovered from the builder's own prior knowledge and not independently re-collated this session (`discovery_channel: builder-prior-knowledge`, `verification_state` not `verified-direct`) and it licenses a load-bearing, vivid, specific (rather than tradition-level) claim (`evidentiary_weight: load-bearing`). *(Re-keyed 2026-08-05, full-system review Rigor P1-2, off the SS3.0 discovery-channel/verification-state/evidentiary-weight axes — mechanically enforced by `wrs/gates/core.py::gate_priority_review_trigger`. The prior rule, "Flag anything at Confidence C or below," assumed the Confidence letter's B still meant "specific work/locus named"; after the Round-1 recalibration redefined B to mean recall, the legacy letter stopped marking the actual risk boundary — the fix is not a lower letter threshold, it is the axis that replaced the letter.)*
7. **Append this world's new Native entries to the Cross-World Source Registry.** This step did not exist in V1.0 and is not optional — skipping it is what would let the Registry silently fall out of date and stop protecting the next world built after this one.
8. Doc_02B is complete enough to build forward from once every gravity, force, and lexicon term needing a specific factual anchor has at least one Native or Shared Licensed-For entry. It remains a living document after that point.

## How Phase 5 (Representative construction) and runtime use this document

The Representative's own Approved Source List (feeding the Template's grounding-anchor paragraph, Section 3) remains a small, 5–10 entry distillation of Doc_02B's Native and Shared entries — not fresh research, and not the full database.

**New in V2.0: the full Doc_02B also has a runtime role, not only a build-time one.** Constitution Article 30 (Layered Accessibility & Progressive Depth) guarantees participants a Level 3 disclosure — "sources with specificity, confidence calibrations, scholarly tensions carried at full strength, the complete construction record" — reachable at any point, never gated. The short grounding-anchor paragraph is what keeps the Representative's own generation bounded, on every turn, at low token cost. The complete Doc_02B is what should actually be surfaced, on request, to satisfy Level 3 — retrieved when a participant asks what something is based on, not carried in every turn's context whether asked for or not. This is an efficiency choice that costs nothing in trustworthiness: the guarantee is "always reachable without restriction," not "always resident," and a source that must be fetched on request is still always reachable. Where this two-tier design isn't yet wired into the runtime/Facilitator layer, that is named here as a dependency for that layer's own build, not something this template can complete unilaterally.

## Living-document protocol

Unchanged in spirit from V1.0: new sources may be added at any time, appended with the next sequential #, never renumbered or removed. If a source is later found unreliable, its Confidence moves to E and its disposition is marked removed-from-use, but the entry stays as a record of what was tried. The Cross-World Source Registry follows the identical append-only discipline, for the identical reason: a trustworthy record of what was tried and found true is itself part of what makes this project trustworthy.
