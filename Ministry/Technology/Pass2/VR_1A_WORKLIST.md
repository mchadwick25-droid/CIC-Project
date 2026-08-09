# Voice Rebuild — 1A Worklist

**What this is.** The single place 1A work items live. Created 2026-08-09
on Mark's instruction ("add fixing the facilitator to the 1A worklist"),
consolidating the items that until now were scattered across the baseline
read findings, the informal category read, the 1A reassessment, and the
checkpoint watchlist. Per the standing interpretation
(`decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`): 1A is the
accessible-rigor goal everywhere it lives, and this list is its backlog.

The governing documents: the north star + B2 target (hard edge ruled) and
the Writing Standard (`decisions/VR_1A_Writing_Standard_2026-08-09.md`,
Mark's text verbatim).

Items marked **PENDING MARK** need his ruling before work starts; items
marked **READY** are decided in substance and waiting on sequencing.

---

## 1. Fix the Facilitator — READY (added by Mark, 2026-08-09)

The shared Facilitator voice (`app/prompts/facilitator_prompts.py`)
**breaches the B2 floor in 3 of 3 measured runs** — FK 11.9/FRE 44.9,
FK 10.5/58.9, FK 12.4/52.5 — the least readable voice on the
participant's screen, and until 2026-08-09 the one voice every harness
deliberately skipped. Scope: rewrite the Facilitator's participant-facing
prompt text to the Writing Standard. The Facilitator speaks etically, so
it may use the standard's own phrasing directly ("historians disagree,"
"the evidence suggests") — no emic translation needed. Verify via the
facilitator-readability report now emitted by every checkpoint; the
breach never fails a world's checkpoint (shared component ≠ per-world
records defect). Note the monitoring prompts (drift signals etc.) are
model-facing, not participant-facing — only participant-visible turns
are in scope.

## 2. The shared `_HOW_YOU_ENGAGE` rewrite — READY in substance

The Blueprint's original Phase-1A task, still unexecuted (the block
predates the rebuild; none of Design §2's six additions are in it).
Content now comes from two sources: Design §2's list (bridge-first entry,
candidate-understanding offer, callback license, lead-with-insight with
both field names, three-way disagreement license, shape repertoire) and
the Writing Standard (explain before naming; one idea per paragraph,
pause; define terms naturally; transparent uncertainty in the emic
register). Sequencing is item 10.

## 3. Engagement instruments — PENDING MARK (reassessment decision 1)

Before the block rewrite is graded: first-sentence-uptake analyzer,
bridge-first manual-read rubric with regex floor, **2 genuinely ambiguous
probes per world** (the candidate-offer mechanic currently has zero test
cases anywhere), callback-occurrence transcript check.

## 4. The blind paired read — PENDING MARK (reassessment decision 2)

1A's human bar, replacing the dangling Objective-3 clause: same 8 probes,
pre-1A vs post-1A block, scored blind. Now carries the Writing Standard's
dual-audience principle explicitly — two questions per transcript:
*could you follow it easily* (newcomer) and *do you recognize careful
scholarship* (historian/pastor/seminary reader). The second audience is
currently tested by nothing.

## 5. Layer 2 engagement demonstrations — PENDING MARK (decision 3)

One per world: **the hardest thing this world holds, said so a newcomer
understands it, without softening** — the Writing Standard's "complex
ideas expressed simply" as a worked example, scored in an engagement
vocabulary. Currently all Phase-2 demonstrations score fidelity traits
only. Alternative: ship 1A prose+code only and let pilot readers judge.

## 6. Demonstration reuse (Paula-story finding) — PENDING MARK

His baseline read: the selector has no within-session memory; Albina
retold the Paula story twice, unaware. Options he left open: (a) track
used demonstrations and deprioritize repeats, (b) require explicit
callback framing on genuine re-use — (b) doubles as a live demo of the
callback license.

## 7. Quotes / citation coverage — PENDING MARK, partially moved already

His baseline read found citations firing on ~21% of turns fleet-wide.
The rebuilt worlds now fire 4–7 of 8 probe turns, so the records rebuild
moved this substantially. Remaining call: (a) wiring/visibility fix only,
(b) increase verbatim primary-source quoting in-voice (authoring cost,
six worlds), or both.

## 8. "What would people today get wrong" pattern — READY

His informal-read catch, logged fleet-wide: Representatives answer with
confident knowledge of what "modern people" think — an anachronistic
awareness. Better shape (his own): answer from uncertainty about *any*
outside era looking in. A prose-shape fix in the shared block (item 2)
plus a probe-phrasing check; this question type recurs in the batteries.

## 9. Sentence tail — watch, no bar ruled

9–17 sentences per run over the standard's 25-word guard (worst 46w)
while averages sit in-band. Reported per world by the sentence-discipline
instrument; accumulates on the watchlist. A bar, if one is ever ruled,
comes from that data — not invented mid-stream.

## 10. Sequencing — PENDING MARK (reassessment decision 4)

Recommended: run items 1–2 (facilitator + block rewrite) before the
remaining four world checkpoints, so Chloe's and Marius's completed runs
become the pre-1A arm of the paired read and the remaining worlds are
checkpointed once, against the post-1A block. Cheaper than six-then-redo.

---

*Cross-references: fleet watch items live in
`gates/voice_rebuild_checkpoint_watchlist.md`; the structural analysis
behind items 2–5 is
`Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/CiC_VoiceRebuild_1A_Design_Reassessment_2026-08-09.md`.*
