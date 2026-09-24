# Launch prompt — System Hub V4: a redesign brief is drafted and reviewed; its fixes are the first job

Paste this into a fresh thread to succeed the current System Hub thread, which has been running a very long, productive session (multiple days of wall-clock work) and is at the end of its service. **This is not a crisis handoff like V3 was — no work is lost, nothing is broken. It's a clean handoff at a natural stopping point, with one clear, concrete next action already identified.**

---

## Read this section first. Verify every line yourself before doing anything else.

Everything below was checked directly during the outgoing session, not assumed. Re-verify the load-bearing claims yourself before treating them as settled — this project's own standing rule, reinforced tonight by an adversarial review that caught two real factual errors in a document a prior part of this same session had written.

- **Two live conversation bugs were found, fixed, and shipped** (commits `4697e2b`, `0ac2063`, both on `main`, both pushed). Run `git log --oneline -10` and confirm before assuming either is still open.
- **A full research-and-redesign arc was completed and saved as real files**, not left in chat history: `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/` (ten research documents plus an index) and `Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md` (the actual draft brief). **Read `00_INDEX.md` first** — it tells you what each research document covers and in what order to reach for them.
- **The brief was adversarially reviewed before being sent anywhere**, and the review found real problems: `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/11_Opus_Adversarial_Review_of_Brief.md`. **As of this handoff, none of the review's fixes have been applied to the brief yet.** This is the actual first job — see below.
- **Two standing decisions were made and saved to personal memory, not just this log** — check `MEMORY.md` in the project's memory directory for `cic-model-tier-allocation-policy` (Sonnet for live work, Opus for design-evaluation passes, Fable capped at 2/week) and `vision-document-v2-governs` (which of two conflicting Vision documents is authoritative, and why). If your environment carries the same memory system forward, these should already be loaded — confirm they are, don't re-derive them from scratch.

## Do not do this, given how this thread came to exist

**Do not re-run the research.** Nine research passes and one prior-day 105-agent Fable study already happened, are saved as real files, and are internally cross-referenced. Re-researching any of it from scratch would waste the exact capped, expensive resource (Fable, 2 passes/week) this whole arc exists to spend wisely.

**Do not trust a prose summary of the research over the research itself, including this project's own summaries — including the brief.** The adversarial review's most important finding was that the brief itself contains two real errors introduced while condensing real research into prose: a mechanism was misattributed (blaming the confirmed-gloss system for a bug that was actually the closing-sequence's), and a supporting quote was a fabricated composite of two separate findings fused into one. Both slipped past drafting because they *sounded* plausible and consistent with everything else being argued. **Before repeating any specific claim, quote, or attribution from the brief, verify it against the actual numbered research document it cites** — the review names exactly which claims to check.

**Do not send the brief to Fable as it currently stands.** It has real, output-changing gaps: no pointer to the actual current governing documents (Constitution V2.2, Facilitator Governance V3.6/V3.7, the Construction Framework, the L4 templates), no real transcript for its own "pressure test" requirement despite real transcripts existing elsewhere in the repo, two of its six stated objectives with no matching deliverable, and a one-sided report of the external-framework research that drops its single most important warning. All of this is itemized, with specific proposed fixes, in review document 11.

## Current state, verified at handoff

**The conversation engine is stable and both live bugs are fixed.** No open production incidents as of handoff.

**The redesign brief exists, is well-argued, but is not ready to send.** It correctly diagnoses four converging findings (build-process quality doesn't improve with build order; voice failures are organization failures, not evidence failures; retrieval has never been tuned while generation has; real relational insight already exists and never reaches the Representative) and proposes a genuinely reasonable two-phase plan (Fable designs, a later Fable pass blueprints, Sonnet builds incrementally). What it needs before it goes anywhere: the eight P0 fixes in review document 11, section 6 — reading-access instructions, real transcripts, the two factual corrections, the two missing deliverables, a rebalanced external-patterns section, doc 10 actually cited, and the brief's own files committed to git (they are currently **untracked** — confirm with `git status`).

**The bedrock is explicitly stated and should not be relitigated**: the mission, the Five Convictions, and a safe space to explore faith and the story of Jesus. Everything else in the brief — the seven-job schema framework, the external patterns, the dataset-not-prose shape — is evidence-informed hypothesis Fable should feel free to improve on, not a locked spec. Keep this framing; the review's complaint was that later sections read more directively than this framing promises, not that the framing itself is wrong.

## Standing references

- `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` — this session's full dated record, append-only, newest entries at the top. Read the 2026-07-25 entry in full before anything else in this file.
- `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/00_INDEX.md` — the research folder's own index.
- `Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md` — the draft brief.
- `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/11_Opus_Adversarial_Review_of_Brief.md` — the review, with prioritized, specific fixes.
- `Ministry/Operations/Standing/CiC_Task_Board_2026.md` — cross-thread status.

## The one thing to do before anything else, once this thread starts

Read the 2026-07-25 Decision Log entry and review document 11 in full. Then say plainly, in the first message: *"Here's what's actually fixed versus still open in the brief, and here's the order I'd apply the review's fixes in."* Get Mark's confirmation on the fix plan before editing the brief — this is exactly the kind of judgment call (which fixes matter most, whether any of the review's own proposed rewrites need further adjustment) that should stay live with him, the same way the rest of tonight's design conversation did, rather than being applied silently.
