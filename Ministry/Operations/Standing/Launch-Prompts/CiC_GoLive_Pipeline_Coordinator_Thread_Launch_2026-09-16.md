# Go-Live Pipeline Coordinator — thread launch — 2026-09-16

**What this is.** A standing thread, not a one-shot task, and it owns the *entire* rest of
the distance to production — not just the pipeline mechanics. Several worlds are at
different points right now (`alx`, `cappadocian`, `desert`, `gallic`, `hal`, `ijc`, `pahc`,
`syr` are `admitted`; `don` is `built`, not yet admitted; `lpc` is mid-build through
Doc_05; `grkap`/`latap` have only cleared Step0 — a `worlds/<code>/` folder exists but the
real build hasn't started). Those worlds' own dedicated build threads have run long,
accumulated enormous context, and are past the point of being the right vehicle to keep
going (Mark's call, 2026-09-16) — this thread absorbs their remaining work rather than
waiting on them. It both **finishes whatever build work is left** on a world and **runs the
go-live pipeline** once it is, so nothing sits waiting on a hand-off between two threads
that both have to be separately kept warm and re-briefed. One thread, start to finish: from
wherever a world currently sits through to "live on the website with search, Atlas listing,
and full conversation working."

## Build work is now in scope — with the usual guardrails, not fewer of them

Finishing a world's build (remaining `Doc_0N` documents, chunking, Representative
construction, closing `Open_Gaps_Tracking.md` items, fixing a failing gate or a bad
citation) runs under the **same self-governance the build-cycle discipline already
uses** (CLAUDE.md "Scaling the build"): kick off and drive a world end-to-end,
self-governing per that discipline's own rules, and escalate to Mark only for one of its
four named categories — Representative identity/title decisions, portfolio-level/
cross-world decisions, governance/methodology changes, or an unresolved tension the
pipeline genuinely can't close on its own — plus never self-assigning Frozen status.
Absorbing build work does **not** loosen any of that; it just means this thread is now
the one doing it directly instead of relaying it to a separate thread. Before treating any
of `grkap`, `latap`, or `lpc`'s prior build threads as closed, read whatever state they
left (their own decision logs, `Open_Gaps_Tracking.md`, any Review-Artifacts) so real
in-flight reasoning isn't silently dropped — inherit their work, don't restart it from
zero.

## The pipeline this thread owns, per world, in order

1. **Get to build-complete.** Doc_01–09 approved to proceed, chunks and Representative
   done, sitting at `worlds/<code>/`, `Open_Gaps_Tracking.md` has nothing blocking. If a
   world isn't there yet, finish it — under the build-cycle self-governance above — rather
   than waiting on a separate thread. This is the step most worlds currently sit at: `lpc`
   needs Doc_06–09 plus chunking and Representative construction; `grkap`/`latap` need
   nearly the whole build from Step0 forward.
2. **M9 confinement/shelf gates green** (`engine/m9`) — Library Access Gate discipline,
   `corpus_index.py --entry <census_id>` used correctly, any waiver counts in
   `engine/m9/enforce.py` actually match what's newly vendored, not stale.
3. **M2 compile.** `python -m engine.m2.cli build <code>`, then
   `determinism-check`. Package lands under `packages/<code>/<package_id>/`; registry's
   `package` block repoints to it.
4. **M3 admission battery.** Run the blind protocol against the sealed canon paraphrases.
   **Present the results — do not decide admission yourself.** Per
   `reference/Redesign-Spec/CiC-Program-Spec.md` §4.2 step 7, "the admission read" is
   explicitly one of Mark's own per-world touchpoints, not something a thread self-governs
   past. Same rule for the state flip in step 5 below (step 8: "the registry flips live" on
   Mark's word, not the thread's).
5. **Registry state flip, `built` → `admitted`**, only after Mark's explicit admission
   call — edit `records/worlds/<code>.yaml`'s `state` field, nothing else about the file.
6. **WO-1 object-storage upload**, once Cloudflare R2 is actually configured (check
   `Ministry/Operations/Standing/CiC_Object_Storage_Runbook.md` — as of this thread's
   launch, R2 bucket/token setup was still Mark's own pending dashboard step, unconfirmed
   done). `python -m engine.m2.cli upload <code>`. Until R2 is live, this step is a no-op —
   the package ships baked into the Docker image instead, which still works.
7. **Atlas/census sync.** `engine.m6` (a generator that owns this) does not exist yet — it's
   a scoped, not-yet-built proposal (mirrors `engine/m2`'s pattern; see the standing plan
   for it if it's been picked up by the time this thread starts). Until it ships, sync
   `cic-website/data/world-census.json` by hand for the newly admitted/open world: `status`
   → `"Built & Live"` only once the world is actually `open` (not merely `admitted` —
   don't get ahead of step 9), plus `entry.representativeName/representativeTitle/
   worldName`, `start`/`end`, recompute `meta.totalEntries`/`liveCount`/`statusCounts`.
   Never touch `living`, `entry.color/tile/icon`, `why`, `longDescription`, or any of the
   283 purely-historical (non-registry-linked) movements — those are hand-authored content,
   not sync targets. Validate with `node tools/validate-census.mjs
   cic-website/data/world-census.json` and the fleet's own `check_census_link`/
   `check_census_agreement` checks before moving on.
8. **Registry state flip, `admitted` → `open`.** Same rule as step 5 — Mark's own call,
   this is literally "the freeze" (spec §4.2 step 8). Don't self-flip.
9. **Merge the world's own PR(s) to `main`.** Never self-merge — wait for Mark's explicit
   "merge PR N," same standing rule this project has run on every PR so far. `main` deploys
   to `cic-engine-staging` automatically; verify the world actually seats and answers there
   before treating it as promotion-ready.
10. **Bundle into a promotion PR, `main` → `live`.** Follow
    `Ministry/Operations/Standing/CiC_Promotion_Runbook.md` exactly. Batch multiple
    newly-ready worlds into one promotion PR when they land close together rather than one
    micro-promotion per world — but name every world going out in the PR body explicitly,
    never a silent bundle. Mark reviews and merges the promotion PR himself; that merge is
    what actually deploys to production (`cic-engine`, `branch: live`).
11. **Post-deploy verification on production.** After Mark's promotion merge: the world
    lists and seats on the live API, a real conversation turn works, the Atlas card is
    live and links through, and — flagged, not yet decided — check whether
    `cic-website`'s own Cloudflare Pages/Workers production deploy branch needs to move
    from `main` to `live` too (the promotion runbook's own "what does not go through this"
    section leaves this open; don't assume either answer, ask).

## Hard rules, carried over from this project's standing discipline

- **Build work stays inside the build-cycle's own four escalation categories** (above) —
  taking on build work is a scope expansion, not a license to loosen it. Representative
  identity/title in particular is always Mark's call, never this thread's, build capability
  or not.
- **Never self-merge a PR.** Always wait for an explicit "merge PR N" from Mark.
- **Never self-admit or self-open a world** (steps 4/5/8 above) — present results, get
  Mark's explicit call, then execute the flip. This is a named exception to "auto mode":
  it's in CLAUDE.md's own escalation table ("cross-world or portfolio-level decision —
  always ask") and named directly in the spec as one of Mark's own touchpoints.
- **Never attempt Render/Cloudflare API writes.** Both are egress-blocked from this
  sandbox (confirmed repeatedly) and GitHub's branch-protection endpoint and raw
  `git/refs` write are blocked by the agent proxy too. Where a step needs one of these,
  write it up as a clear dashboard action and hand it to Mark rather than trying a
  workaround.
- **Keep pipeline state in a standing tracking doc, not just this thread's own memory.**
  Maintain a running per-world status table (which stage each world is at) in
  `Ministry/Operations/Standing/` — update it every time a world moves a stage, so the
  state survives a context reset or a fresh thread picking this up later.
- **Verify claims independently before acting on them** — including Mark's own reports of
  what he's already done in a dashboard ("I opened the PR," "I added the branch
  protection rule"). Check via the GitHub API or by asking for a screenshot before
  building on top of an assumption; this project has hit real cases this session where a
  reported action hadn't actually completed.

## First task, before touching any pipeline step

Build and report the current per-world status table before doing anything else:
- **`don`** — built, needs only Mark's admission read (step 4). No build work left.
- **`lpc`** — mid-build through Doc_05 (Ecological Reconstruction); read its own
  `lpc_Decision_Log.md` and `Open_Gaps_Tracking.md` first, then continue Doc_06 onward.
  Check whether PR #197 (flagged earlier as needing a rebase onto `worlds/lpc/` paths) is
  still relevant before restarting anything it already covers.
- **`grkap`, `latap`** — only Step0 (movement scope confirmation) is done; read their
  Review-Artifacts for whatever scoping work already happened, then pick up from Doc_01.
- **The 8 `admitted` worlds** — confirm each one's package is current (not stale against
  its own `records/`), and whether any are already `open`/live today vs. merely admitted.

Recommend, per world, the next concrete action and whether it needs Mark's input before
this thread can proceed on it — then let Mark choose where to start rather than assuming
every world should be pushed forward at once.
