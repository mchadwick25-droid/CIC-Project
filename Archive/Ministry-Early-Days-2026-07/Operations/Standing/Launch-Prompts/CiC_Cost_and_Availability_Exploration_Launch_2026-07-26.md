# Launch prompt — Cost & availability exploration thread

Paste this into a fresh Sonnet-model thread, separate from the System Hub. **This is an exploration conversation, not a design or implementation thread.** No decisions get locked here, no code changes, no brief edits — the point is to think out loud across three related ideas and see what's actually worth pursuing before anything gets designed.

---

## The three things to explore

1. **Model maxing** — using different model tiers strategically for different jobs, rather than one model doing everything. CiC already does a version of this (a hard split between the generation model and a cheaper model for every classifier), but it's worth asking how far that pattern could extend, and where it shouldn't.
2. **Model money management** — real cost control, not just "use a cheaper model." Prompt caching economics, what's already instrumented, what's still unmeasured, where spend is going that isn't buying anything back in quality.
3. **Pre-process prompts** — cheap steps that run before the expensive generation call: filtering, routing, or shaping what actually needs the full model, so quality holds but fewer expensive calls get made.

The shared goal across all three: keep real cost down, so the product stays available and sustainable, without trading away rigor or voice quality to get there. Convictions and safe space are the bedrock — cost only ever competes with rigor here to the extent Constitution Article 5 allows (rigor wins where they'd genuinely conflict).

## Grounding — real numbers already gathered, don't re-derive these

- **Real measured cost:** roughly $0.06–0.08/exchange, running close to $2/hour against an original $1/hour funding assumption. Order-of-magnitude floor, not a precise baseline — measured before a cache-read logging bug was found and fixed on the streaming endpoint. Fuller model: `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md`.
- **Caching mechanics that already changed a real decision:** cache-read tokens bill at a small fraction of the raw rate — a real prior change was approved at "~1.4x once cache-read is weighted at its true rate," not the raw 3x token multiple that would have rejected it. The direction can reverse too: a larger but *stable* cached prefix can cost less than a smaller prefix that varies every turn, because a stable prefix stays cached (Character.AI reports ~95% cache-hit rates on exactly this principle).
- **One caching risk flagged, not yet acted on:** Anthropic's cache TTL is 5 minutes by default. A participant who pauses mid-session longer than that — which this product's own contemplative pacing invites — loses the cache advantage and becomes a real, currently-unmodeled cost variable.
- **A real, unexamined cost lever already found:** retrieval volume has never once been tuned since the original scaffold. Alexandria alone can push ~4,300 words of retrieved context into a single turn against a ~900-word output cap — tokens being paid for that are actively working against voice quality, not for it. Where quality and cost pull the same direction (this is one such place), that's not a tradeoff to weigh, it's just a fix to make.
- **The classifier/generation split already in production, as a pattern to extend or question:** every classifier (fabrication check, over-settling check, safety routing) runs on a cheaper model than generation. Real per-call usage instrumentation already exists to measure this split's actual payoff.

These come from the same night's cost/architecture research that fed a separate, parallel redesign-brief effort (`Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md` and its research at `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/`) — useful background if you want deeper grounding on any specific number, but this thread doesn't need to track or block on that effort. It's its own space.

## How to run this thread

Divergent first — breadth over commitment. Generate real options for each of the three areas, including options that might not survive scrutiny, before narrowing anything. Don't write a design doc. Don't propose code changes. If a genuinely promising direction emerges, name it clearly and stop there — a real design pass is a separate, later step, in a separate thread, the same way this project has handled every other workstream.

Model tier for this thread: Sonnet, per the project's standing model-tier policy (Sonnet for live conversation/exploration, Opus reserved for deeper evaluation passes, Fable capped at 2/week for the largest comprehensive passes).
