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

## Scaling the build — many worlds, mostly autonomous

The build-cycle discipline already self-governs: escalation is limited to four categories (Representative identity/title decisions, portfolio-level/cross-world decisions, governance/methodology changes, and unresolved tensions the pipeline can't close on its own) plus never self-assigning Frozen status. Use that as designed, instead of re-approving every document by hand:

- Kick off a build end-to-end per world — "build [World] end-to-end per cic-build-cycle discipline; self-govern per its own rules; stop only for an escalation category or a missing input" — rather than one document at a time. Most of a world's build should run without a reply from the project lead at all.
- Run multiple worlds concurrently as separate sessions, each kicked off the same way, rather than serially in one thread. This is parallel human-supervised sessions, not automated multi-agent orchestration — scale the number running at once up as it proves out.
- Source acquisition for new worlds should be **proactive, not reactive**: the dedicated source-research thread should search, rights-verify, and download against upcoming worlds' time-windows/regions *before* their Doc_02 stage starts — adding rows to `world-build-docs/_cross-world/download-queue-seed.yaml` and vendoring into `cic/texts/` ahead of need, the same distinction `DOWNLOAD-QUEUE.md` already draws between its proactive and reactive (`WANTS-REGISTER.md`) halves. Check `CORPUS-USE.md`'s existing tier method (named-never-opened / same time-place / same time-different-region / out-of-window) against the new worlds first — much of what's needed may already sit unused among the 82 vendored files. (The sandbox blocks the patristic text hosts outright regardless of real scarcity — widening that network policy is a live open item.) A single research pass serves every future world whose window it covers, since the corpus is shared — that's higher leverage than a per-world manifest.
- The source-research thread runs long and accumulates enormous context (multi-day continuous sessions have run past a billion cached tokens). Split its work into fresh sessions per batch (an era/region at a time) rather than growing one thread indefinitely — an ever-larger context makes every later turn more expensive regardless of how good the research is.
- Representative identity and image are decided together, once, as a single packaged choice among 2–4 named candidates with trade-offs (per `Representative_Construction_Notes_Template.md`) — never open-ended, never split across two separate interruptions.
- Doc_02 (Source Ecology) and Doc_04 (Gravity Discovery) are this project's clearest instances of the "complex design and research" framing work described under Fable, above — the strategic classification the rest of a world's build depends on.
- Track fleet-wide build status in `Ministry/Operations/World_Build_Queue.md` (queued / drafting / blocked-source / blocked-identity / blocked-escalation / complete) — separate from `records/worlds.yaml`'s own governed admission ledger, which only reflects a world after it's already built.

## Usage/credit discipline

Weekly usage credits keep running out. To fix that without losing quality (and without touching anything above this line). This is a Max-200 plan; context-window management matters at least as much as model choice — a bloated context costs more than a clean one regardless of tier:

- Manage context actively: `/compact` or `/clear` between unrelated pieces of work, and delegate research/investigation to subagents so exploration doesn't bloat the main thread. Reach for these before reaching for a cheaper model.
- Use Plan Mode before committing to implementation on anything with uncertain scope — explore read-only first rather than burning implementation-priced turns on discovery.
- When a path turns out wrong, back out of it with a checkpoint/`/rewind` instead of patching over it — this is "no fix on a fix" (above), enforced mechanically.
- Fable is reserved for complex design and research — the strategic thinking that sets the frame for everything downstream (system/front-end redesign proposals, comparative source-ecology and world-strategy research, org/funding strategy). Use it where getting the frame right the first time avoids many cheaper rounds of rework later, not for routine drafting or anything that repeats.
- Opus is for the final adversarial-review gate only. Draft and do intermediate revision rounds with Sonnet.
- From round 2 onward, do a targeted recheck (only what changed, against prior findings) instead of a full re-review from scratch.
- Push mechanical work — package rebuilds, citation/log fixes, formatting, indexing — to Haiku.
- Batch related work into one longer session instead of many short restarted ones; short sessions lose the prompt cache and re-pay for context every time.
- Spread heavy build/review days across the week instead of bursting most of a week's work into 1–2 days.
- Use event-driven waits (PR/CI subscriptions) instead of manual polling loops.
- Check `/usage` periodically to catch a runaway pattern before it costs the rest of the week.
- Max-200 draws Claude chat, Claude Code, and Cowork from one shared usage pool — if more than one surface is in use, watch total burn across all of them, not just this session.
- If the ceiling still gets hit, Max-200 allows purchasing extra usage (billed at API rates) with a spending cap set in Settings → Usage — a planned fallback for a genuinely heavy week, not a substitute for the discipline above.
