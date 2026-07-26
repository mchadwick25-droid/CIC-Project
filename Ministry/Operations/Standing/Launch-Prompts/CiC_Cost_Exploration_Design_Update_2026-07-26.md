# Update for the cost & availability exploration thread — a real redesign now exists

Paste this into the already-running cost/availability exploration thread. It was originally grounded in the *current* system's cost data; this brings it up to speed on a real proposed redesign that exists now, and redirects the three exploration areas onto it specifically.

---

**Message to paste:**

> Update, not a new topic: since this thread started, the redesign work it was grounded in produced an actual design, not just diagnosis. `Ministry/Technology/CiC_System_Redesign_Pass1_Design_2026-07-26.md` (~15,500 words, twice adversarially reviewed, all findings applied) is the real proposed architecture — schema, build process, representative construction, facilitator governance, retrieval, cost model, all of it. It's about to go to Fable for Pass 2 (turning it into a build sequence), so this is a live window to think about cost and availability against the *actual* design, not the system you were originally grounded in.
>
> Keep doing exactly what you've been doing — exploration, not design or implementation — but retarget the three threads onto what's specifically already proposed:
>
> **Already in the design, worth reacting to rather than re-deriving:**
> - **Model maxing, taken one step further than today:** the design replaces a batched LLM relevance vote in retrieval with a **local CPU cross-encoder** — no API call at all, not even Haiku, for that specific job (§5.4 R6, removes ~2 Haiku calls per world per turn). It also adds *new* Haiku calls elsewhere (a repair-initiation classifier, a query-rewrite step, a misattribution check) — real judgment calls about which jobs actually need a model at all versus a cheap check versus nothing.
> - **Money management:** the design leans hard on cache economics — an always-present "quick-reach" layer (every term's short definition) rides in the cached prefix instead of being retrieved per turn, at roughly a tenth of today's per-turn retrieval cost for the worst case measured (Alexandria: $0.020/turn → $0.0012/turn). But it explicitly flags one real unmodeled risk: Anthropic's 5-minute cache TTL against this product's own contemplative pacing — a participant who pauses mid-session loses the cache advantage, and that's a real, currently-unquantified cost variable (§8).
> - **Pre-process prompts:** two live examples already in the design — a cheap direct-address check that runs *before* the expensive turn-selection call and skips it entirely when the previous turn already named a specific world (§6.2), and a one-Haiku-call query-rewrite step that runs before retrieval to produce a cleaner search query (§5.4 R9). Both are exactly this thread's third topic, already applied in two places.
>
> **Real open questions worth exploring, not answering yet:** what else in the design's cost table (§8) could get the same "cheap check before the expensive path" treatment as direct-address detection? Is there a cheaper answer to the cache-TTL-vs-contemplative-pacing problem than just accepting the risk? Are the three *new* Haiku calls the design adds (repair classifier, query rewrite, misattribution check) all actually necessary, or could any go the way R6 did — to a smaller, local, non-API mechanism?
>
> Still divergent-first. Still no design doc, no code, no commitment to anything — this is material to think against, not a spec to implement.
