# CIC-Project — Working Rules

These rules apply to every session in this repo. Read them before doing anything else. They're listed in priority order — where two sections would pull in different directions, the higher one wins. Safety and fidelity are never traded away for speed, cost, or convenience.

## Safety comes first

- A Representative never handles real crisis or distress itself. Recognizing risk and directing a participant to real human help is entirely the Facilitator's role, governed outside any world's own voice — a Representative may speak warmly in-character, but the actual redirect is Facilitator-governed and template-anchored, not freely generated.
- Don't confuse a world's intended "historical otherness" fierceness or disorientation (part of the design) with genuine participant distress (a safety event) — treating the former as the latter defeats the mechanism meant to catch the latter.
- Fabrication at moments of maximum stakes is the single most serious governance failure this project recognizes. Near anything safety-adjacent, default to caution over assuming resilience, and never make a redirect conditional on the participant confirming they're okay.
- The live governing doc is `CiC_L3D_Facilitator_Governance_V3.6`. The newer AcuteDistress/HarmfulDynamic mechanism is still a draft proposal, not yet merged into it — don't treat the draft mechanism's specifics as settled, but "redirect is Facilitator-only, never the Representative" is a decided rule.

## Source fidelity — never invent

- No invented family, age, personal history, or anecdote for a Representative. If a detail isn't derivable from the completed world, it doesn't belong.
- A uniformly polished "generic AI voice" is itself a fabrication risk — no less than an invented personal quirk would be.
- Every quote must be re-verified verbatim against the vendored source file before a record passes review. A record marked "quotes verified" is a claim to re-check, not a fact to trust — misattributed and mis-transcribed quotes have been a real, recurring defect here.
- Contested or uncertain claims get tagged with the project's five-level confidence vocabulary (Widely Accepted / Dominant Modern Reconstruction / Inferential-Thin / Contested / Not Attested), with a `contested_claim` record where warranted. Never present a disputed claim as settled.

## Accessible and rigorous — participant-facing content

- Anything a participant sees or hears — Representative dialogue, front-end copy, onboarding, disclaimers — targets an English reading level of roughly grade 8–10. Accessible and rigorous go hand in hand, not in tension: write for that level without flattening the substance underneath it.
- No AI tells. Nothing should read as generated — no hedging filler, no assistant-voice cadence, no telltale LLM phrasing, no disclaimer-as-crutch. If a participant can hear the chatbot instead of the world's own voice, that's a defect, independent of whether the content is otherwise accurate.
- This applies to everything participant-facing, not just Representative dialogue — UI text, instructions, and onboarding flow are held to the same bar.

## Fix it right

- No easy fixes. No band-aids, no workarounds, no "good enough for now."
- No fix on a fix. If a previous fix was wrong or incomplete, undo it and redo it right — don't stack a second patch on top of it.
- Find and fix the root cause, not the symptom. If the root cause isn't clear yet, say so and investigate before touching code.
- No shortcuts that trade correctness or completeness for speed.

## Governance vocabulary and closure

- "Approved to proceed" — not "finalized." That word is retired; don't use it.
- Nothing closes until both Phase Five boundary testing and full-system review are complete.
- A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation.
- Truncation checks use two independent methods, not one.

## Keep the live/canonical surfaces clean

The following are **live and used by the program, or are canonical build output**. They contain only what runs the program or constitutes the finished record — no notes, commentary, change history, review discussion, or process narration embedded in them:

- `engine/`, `cic/engine/` — the core engine
- `records/`, `packages/`, `canon/`, `cic/corpus-map/`, `cic/texts/` — structured world data and compiled build output
- `world-build-docs/` — the canonical construction documents (Doc_01–Doc_09 per world) once approved to proceed

Notes, decision logs, audit trails, adversarial-review rounds, status reports, and strategy discussion belong in `Ministry/` (e.g. `Ministry/Operations/Audits/`, the various `*_Decision_Log.md` files) — never inline in the files listed above. If you find commentary, changelog cruft, or leftover process notes in a live/canonical file, treat that as corruption: remove it, don't add to it.

(This categorization is inferred from the repo layout — correct it if something's miscategorized.)

## Track gaps and exceptions explicitly — don't let them go quiet

- Every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread. Entries are append-only and numbered; a merged entry's number never changes, and cross-references cite subject + date, not a bare number.
- Every known fleet-level defect that isn't being fixed right now must be registered as an `ACCEPTED_OPEN` waiver with its owning finding. An unlisted defect is new drift and fails the run; a stale waiver for something already fixed also fails — remove it.

## Usage/credit discipline

Weekly usage credits keep running out. To fix that without losing quality (and without touching anything above this line):

- Opus is for the final adversarial-review gate only. Draft and do intermediate revision rounds with Sonnet.
- From round 2 onward, do a targeted recheck (only what changed, against prior findings) instead of a full re-review from scratch.
- Push mechanical work — package rebuilds, citation/log fixes, formatting, indexing — to Haiku.
- Batch related work into one longer session instead of many short restarted ones; short sessions lose the prompt cache and re-pay for context every time.
- Spread heavy build/review days across the week instead of bursting most of a week's work into 1–2 days.
- Use event-driven waits (PR/CI subscriptions) instead of manual polling loops.
- Check `/usage` periodically to catch a runaway pattern before it costs the rest of the week.
