# CIC-Project — Working Rules

These rules apply to every session in this repo. Read them before doing anything else. The first two sections are principles that hold together: neither is ever traded against the other, and neither is traded away for speed, cost, or convenience. The third, Safety, is a working protocol that is kept and built to be proportionate. The sections after them are listed in priority order — where two of those would pull in different directions, the higher one wins.

This program succeeds or fails on exactly two things: scholarly rigor and clear, accessible conversation. That's not one section among the others below — it's what "Trust and source fidelity" and "Accessible and rigorous" (below) are actually protecting, and it's why they outrank everything about cost, automation, and scale. The cost and scaling discipline further down exists to buy more of both, never to trade against either. A build that's cheaper, faster, or more automated but weaker on rigor or clarity is not a win — it's a failure the process didn't catch.

## Trust and source fidelity — never invent

The people in these conversations rely on what we say and on how we read them. Accessibility (the next section) holds together with this.

- Fabrication at moments of maximum stakes is the single most serious governance failure this project recognizes.
- No invented family, age, personal history, or anecdote for a Representative. If a detail isn't derivable from the completed world, it doesn't belong.
- A uniformly polished "generic AI voice" is itself a fabrication risk — no less than an invented personal quirk would be.
- Every quote must be re-verified verbatim against the vendored source file before a record passes review. A record marked "quotes verified" is a claim to re-check, not a fact to trust.
- Contested or uncertain claims get tagged with the project's five-level `formation_confidence` vocabulary (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin), with a `contested_claim` record where warranted. Never present a disputed claim as settled. "Not Attested" is not a sixth confidence level — it names an absent claim, not a confidence rating on a claim that exists (`honest_limit` / `absent_detail` / `kind: absence` records already model this).
- Don't confuse a world's intended "historical otherness" fierceness or disorientation (part of the design) with genuine participant distress (a safety event) — treating the former as the latter defeats the mechanism meant to catch the latter.

## Accessible and rigorous — participant-facing content

- The target, as a principle to write toward — not a script this file runs: **CEFR B2 / Flesch-Kincaid grade 8–10, Flesch Reading Ease ≥ 60**, in the register of BBC News or National Geographic — serious, adult, vivid, clear, readable by a non-native speaker without simplifying the substance. Treat grade 8 as a floor worth staying above, not a target to hit exactly — too-simple isn't the risk this guards against; flattening the world's own voice is. The actual per-turn scoring and hard-fail enforcement of this live in the engineering (`engine/m7/turn_readability.py`, the NorthStar decision) — full detail in `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and `VR_1A_Writing_Standard_2026-08-09.md`.
- Three things have to hold together, never traded against each other: **accessible** (the reading-level target above), **distinctive** (the world's own imagery, convictions, and flavor survive — clear but generic has failed differently, not better), and **held** (zero fabrication, doesn't cave or go hollow under real pushback).
- Practical shape: short sentences (roughly 12–20 words average), one idea per paragraph (1–4 sentences), technical terms introduced before they're used naturally, active voice and concrete verbs over passive and nominalizations, no unnecessary Greek/Latin, nothing nested or running past ~25 words. Uncertainty is stated plainly rather than hedged into vagueness, and evidence is shown naturally ("we believe this because...") rather than argued at length. Precise language beats impressive language — say the complex idea plainly rather than trading it for a simpler one. Not simplifying the scholarship; lowering the barrier to entering it.
- A Representative's hedge language is emic, not etic — a world's own way of naming its own uncertainty, not the generic academic phrasing ("historians disagree") that a Facilitator, speaking from outside every world, may use directly.
- No AI tells. Nothing should read as generated — no hedging filler, no assistant-voice cadence, no telltale LLM phrasing, no disclaimer-as-crutch. If a participant can hear the chatbot instead of the world's own voice, that's a defect, independent of whether the content is otherwise accurate.
- This applies to everything participant-facing, not just Representative dialogue — UI text, instructions, and onboarding flow are held to the same bar.

## Safety

- A Representative never handles real crisis or distress itself. Recognizing risk and directing a participant to real human help is entirely the Facilitator's role, governed outside any world's own voice — a Representative may speak warmly in-character, but the actual redirect is Facilitator-governed and template-anchored, not freely generated.
- Near anything safety-adjacent, default to caution over assuming resilience, and never make a redirect conditional on the participant confirming they're okay.
- The protocol is built to be proportionate: as cheap as it can be while still reliably catching the real event. A rare event does not raise the cost of ordinary turns beyond what detection needs.
- The safety protocol is functioning: the Facilitator classifies acute distress and harmful dynamics on each turn, the Representative stays silent on those turns, and the template-anchored crisis resources are appended by code. The governing doc is `CiC_L3D_Facilitator_Governance_V3.6`, a Word file at `Archive/Syriac-Build-2026-07/L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`.

## Fix it right

- No easy fixes. No band-aids, no workarounds, no "good enough for now."
- No fix on a fix. If a previous fix was wrong or incomplete, undo it and redo it right — don't stack a second patch on top of it.
- Find and fix the root cause, not the symptom. If the root cause isn't clear yet, say so and investigate before touching code.
- No shortcuts that trade correctness or completeness for speed.

## Governance vocabulary and closure

- "Approved to proceed" — not "finalized." That word is retired; don't use it.
- Nothing closes until both Phase Five boundary testing and full-system review are complete — this is the whole-system/portfolio closure gate, a different and much rarer scope than a single document's own "Approved to proceed" under the build-cycle's per-document self-governance ("Scaling the build," below). One document proceeding doesn't mean anything has closed.
- A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation.
- Truncation checks use two independent methods, not one.

## Keep the live/canonical surfaces clean

The following are **live and used by the program, or are canonical build output**. They contain only what runs the program or constitutes the finished record — no notes, commentary, change history, review discussion, or process narration embedded in them:

- `engine/`, `cic/engine/` — the core engine and the corpus tools
- `records/`, `packages/`, `canon/`, `fixtures/` — structured world data, compiled build output, sealed probes, the fixture world
- `cic/texts/`, `cic/corpus-map/` — the Library: vendored source editions and the map of which works belong to which tradition
- `cic-poc/frontend/`, `cic-website/` — the participant-facing app and the public site; what Render and Cloudflare serve
- `Build/worlds/` — one home per world, keyed by registry code (repo-structure cleanup phase 2, 2026-09-15): the canonical construction documents (Doc_01–Doc_09 per world, their reviews, chunks and Representative) once approved to proceed at `Build/worlds/<code>/`, each world's own indexes/build log/source manifests at `Build/worlds/<code>/build/`, and the fleet-level `_cross-world/` documents. Worlds without a registry code yet still live at `Build/World-Builds/<long-name>/` until they get one.
- `Build/reference/` — the method and spec library: the Level documents, the Redesign-Spec, the current-era method documents, the fleet-voice exemplar. Read constantly, edited rarely; a template exists once, here.
- `Sandbox/` — next-version work in progress: pure code only, held to the same discipline as everything above (decided 2026-09-26). Support material for `Sandbox/<project>/` lives in `Build/Ministry/Features/<project>/`, never inline here.

Notes, decision logs, audit trails, adversarial-review rounds, status reports, and strategy discussion belong in `Build/Ministry/` (e.g. `Build/Ministry/Operations/Audits/`, the various `*_Decision_Log.md` files) — never inline in the files listed above. If you find commentary, changelog cruft, or leftover process notes in a live/canonical file, treat that as corruption: remove it, don't add to it. Superseded material goes to `Archive/`; nothing is deleted without instruction.

Any PR that edits a live or canonical file also removes the commentary already in that file; the check in tools/check_live_commentary.py shows what is there.

The root `README.md` is the map of the whole tree — every top-level entry, its kind, and what reads it. This list follows the map; if they disagree, fix the map first (and log it in `Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`), then this list.

## Track gaps and exceptions explicitly — don't let them go quiet

- Every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread. Entries are append-only and numbered; a merged entry's number never changes, and cross-references cite subject + date, not a bare number.
- Every known fleet-level defect that isn't being fixed right now must be registered as an `ACCEPTED_OPEN` waiver with its owning finding. An unlisted defect is new drift and fails the run; a stale waiver for something already fixed also fails — remove it.

## How we work — Sam Kaner's model: diverge, struggle, converge, then auto mode

Exploring, analyzing, or designing something follows Sam Kaner's facilitation model (the Diamond of Participation), not a jump straight to a conclusion:

- **Divergent** — go wide first. Surface the real range of possibilities before narrowing to any one of them.
- **Groan zone** — struggle with it honestly. Explore options, ask "what if," sit with the tradeoffs rather than resolving them prematurely.
- **Convergent** — narrow down together, to an actual decision Mark has actually reached, not one reasoned through alone and handed over as settled.

This is Mark's own established practice, not a new process being imported — worked example and provenance: `Build/Ministry/Operations/Standing/CiC_Governance_Rationale_Log.md`.

Ground rules for all three phases: one question at a time, not several stacked at once. Present real options with explanations and a recommendation — never a flat conclusion with no alternatives shown. Say explicitly which phase the conversation is in whenever it isn't obvious. Nothing gets written into a canonical record, committed, or treated as decided until convergence is actually reached with Mark.

Anything for Mark to review or approve — options to choose between, a draft to react to, a comparison — renders in the right panel as an Artifact, never as a file written into the repo that then has to be saved, tracked, and cleaned up. A file gets written only once it's the actual converged-on output, not as a vehicle for getting there. This doesn't apply to the project's own permanent review artifacts (adversarial-review rounds, decision logs, `Open_Gaps_Tracking.md`) — those are intentional, lasting audit trail, not scratch material for one conversation's approval step.

**Implementation is a different mode — auto mode.** Once something has genuinely converged — a decision just reached together, or an already-negotiated framework like the build-cycle's own self-governance under "Scaling the build" below — execute it without asking permission step by step; don't make Mark push buttons one at a time. A converged plan isn't a license to drift from it, though: once something is frozen or otherwise settled, a real change to it is a **change order** — named and reasoned — never a quiet edit that erodes what was actually agreed. Drop out of auto mode back to divergent/groan/convergent only for a real decision that wasn't already made, a need for direction, or a need for clarification. Everything else inside a converged plan, just do.

### Convergence signal and default actions

**The literal trigger.** "Converged, auto mode" — or an unambiguous equivalent Mark states directly — means the decision is final. A thread that hears it executes the full scope without re-asking. Absent that phrase, keep checking. This doesn't replace divergent/groan-zone/convergent above; it's the signal that closes it.

**Default actions**, so a thread checks this instead of guessing under uncertainty:

| Action | Default |
|---|---|
| CI/infra mechanical fix (config, workflow YAML, build script) | Just do it |
| Package rebuild after a `records/` edit | Just do it |
| Doc-hygiene fix on content that isn't your own thread's | Flag it, don't touch it |
| Cross-world or portfolio-level decision | Always ask |
| Governance or methodology change | Always ask |

Starts here, grows only when a real new case shows up — not speculatively.

## Scaling the build — many worlds, mostly autonomous

The build-cycle discipline already self-governs: escalation is limited to four categories (Representative identity/title decisions, portfolio-level/cross-world decisions, governance/methodology changes, and unresolved tensions the pipeline can't close on its own) plus never self-assigning Frozen status. Use that as designed, instead of re-approving every document by hand:

- Kick off a build end-to-end per world — "build [World] end-to-end per cic-build-cycle discipline; self-govern per its own rules; stop only for an escalation category or a missing input" — rather than one document at a time. Most of a world's build should run without a reply from the project lead at all.
- Build one world at a time by default, each kicked off the same way. A second concurrent session runs only when the world's cost ledger shows the weekly usage allowance can carry it. This is human-supervised sessions, not automated multi-agent orchestration.
- Source acquisition for new worlds should be **proactive, not reactive**: the dedicated source-research thread should search, rights-verify, and download against upcoming worlds' time-windows/regions *before* their Doc_02 stage starts — adding rows to `Build/worlds/_cross-world/download-queue-seed.yaml` and vendoring into `cic/texts/` ahead of need, the same distinction `DOWNLOAD-QUEUE.md` already draws between its proactive and reactive (`WANTS-REGISTER.md`) halves. Check `CORPUS-USE.md`'s existing tier method (named-never-opened / same time-place / same time-different-region / out-of-window) against the new worlds first — much of what's needed may already sit unused among the vendored files. (The sandbox blocks the patristic text hosts outright regardless of real scarcity — widening that network policy is a live open item.) A single research pass serves every future world whose window it covers, since the corpus is shared — that's higher leverage than a per-world manifest.
- The source-research thread runs long and accumulates enormous context (multi-day continuous sessions have run past a billion cached tokens). Split its work into fresh sessions per batch (an era/region at a time) rather than growing one thread indefinitely — an ever-larger context makes every later turn more expensive regardless of how good the research is.
- Representative identity and image are decided together, once, as a single packaged choice among 2–4 named candidates with trade-offs (per `Representative_Construction_Notes_Template.md`) — never open-ended, never split across two separate interruptions.
- Doc_04 (Gravity Discovery) and Doc_10 (Representative construction) are the build's instances of the "complex design and research" framing work described under Fable, below — the strategic classification and the voice the rest of a world depends on. Doc_02 (Source Ecology) belongs to the Library thread.
- **Review cycles are capped, not open-ended.** The bar is acceptable scholarly rigor, not perfection — a review flagging that a document *could* be stronger or more thorough, with nothing in it actually wrong, unsupported, or misleading, is not a substantial finding and does not justify another revision round. Three rounds of substantial revision on the same document without it clearing review is itself an "unresolved tension the pipeline can't close on its own" (an existing escalation category) — stop and escalate rather than attempt a fourth round. Every review file on a document counts toward the three, whatever its kind or verdict (the `roundcount` gate enforces it). The one exception: once a document has escalated to Mark at the cap, a review he orders in his ruling does not count, when a "Cap ruling" entry in the System Hub Decision Log names its file. Why this cap exists: `Build/Ministry/Operations/Standing/CiC_Governance_Rationale_Log.md`. Full mechanics: the `cic-build-cycle` skill's own Revision decision section.

## Usage/credit discipline

Weekly usage credits keep running out. To fix that without losing quality (and without touching anything above this line). This is a Max-200 plan on a genuinely tight budget — $200/month is a real financial stretch, not a comfortable ceiling with room to spend past. Treat it as a hard cap: the goal is to get everything possible out of the flat fee, not to fall back on paid overage. Context-window management matters at least as much as model choice — a bloated context costs more than a clean one regardless of tier:

- **Paid bulk runs are gated.** Before any run that spends real money in bulk on a metered outside service (text-to-speech, image or model batches, anything charged per item or character), run a small sample first and get Mark's approval of it by ear or eye. Only then run the rest. Pass every paid setting (voice or model id, generation settings) explicitly on the command, never inherited from the environment. The run must print those settings, with item and character counts, and they are confirmed from that printed output before the run is called valid. A check that files match each other proves nothing about what produced them; verify the thing that was paid for. Why: `Build/Ministry/Operations/Standing/CiC_Governance_Rationale_Log.md`.
- Manage context actively: `/compact` or `/clear` between unrelated pieces of work, and delegate research/investigation to subagents so exploration doesn't bloat the main thread. Reach for these before reaching for a cheaper model.
- Use Plan Mode before committing to implementation on anything with uncertain scope — explore read-only first rather than burning implementation-priced turns on discovery.
- When a path turns out wrong, back out of it with a checkpoint/`/rewind` instead of patching over it — this is "no fix on a fix" (above), enforced mechanically.
- Fable is reserved for complex design and research — the strategic thinking that sets the frame for everything downstream (system/front-end redesign proposals, comparative source-ecology and world-strategy research, org/funding strategy). Use it where getting the frame right the first time avoids many cheaper rounds of rework later, not for routine drafting or anything that repeats.
- Opus 5.5 reviews every adversarial-review round; Sonnet 5.5 drafts and revises, except that Fable drafts Doc_04 and Doc_10. From round 2 onward, review is a targeted recheck at lower effort.
- The weekly allowance resets Friday at 2:00 pm, and at least half of it goes to building. Every world keeps two ledgers: allowance share, and metered spend in dollars. Start a world only when the remaining build allocation covers a typical world plus a reserve; heavy steps go early in the week.
- One exception: modern-English renderings the voice speaks (a quote's `modern_rendering`, and any re-rendering of it) are authored by Opus. Sonnet did not hold the rendering bar on them (every clause, nothing added, one thought per sentence, nothing past about 25 words, no word whose modern sense misleads). Everything else still drafts on Sonnet.
- From round 2 onward, do a targeted recheck (only what changed, against prior findings) instead of a full re-review from scratch.
- Push mechanical work — package rebuilds, citation/log fixes, formatting, indexing — to Haiku.
- Batch related work into one longer session instead of many short restarted ones; short sessions lose the prompt cache and re-pay for context every time.
- Spread heavy build/review days across the week instead of bursting most of a week's work into 1–2 days.
- Use event-driven waits (PR/CI subscriptions) instead of manual polling loops.
- Pull requests cost CI minutes and waiting time by the push, not by the size: batch related slices into one pull request, open it as a draft, push once after the local checks pass, then mark it ready. One full CI run per pull request is the target; three speculative pushes pay for three (ruled 2026-10-05).
- Check `/usage` periodically to catch a runaway pattern before it costs the rest of the week.
- Max-200 draws Claude chat, Claude Code, and Cowork from one shared usage pool — if more than one surface is in use, watch total burn across all of them, not just this session.
- Confirm "extra usage" is OFF in Settings → Usage (or capped at $0). On a tight budget, hitting the weekly ceiling is a signal to spend less via the discipline above, not a cue to let paid overage kick in — don't leave it toggled on "just in case." A session's own internal cost telemetry (what work would have cost at raw API rates) is not a bill by itself; only actual overage usage is. If overage is ever needed for something genuinely unavoidable, turn it on deliberately, do the one thing, and turn it back off.
