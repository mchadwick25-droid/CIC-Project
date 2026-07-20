# Update 2 to System Hub — current state, and what's open while feature-by-feature testing continues

Paste this into the Hub thread when Mark releases it to move forward. Supersedes/extends
`CiC_System_Hub_Sync_UX_Testing_Session_2026-07-20.md` (Update 1) — that one is still
good background; this covers everything since.

---

You're System Hub. You already reviewed and confirmed the epistemology-bridge fix
(`99a25e8`) in your own commit `1be1bde` — good, that review holds, nothing below
contradicts it. You also have Mark's direction already on record (`fc66ced`): hold
hosting behind a content/feature-completeness pass done together with the UX-testing
thread (this one) before standing up either deploy. This update gives you the current
state that pass needs to work from, plus what's open for you to pick up.

**What governs:** unchanged — standard git-safety protocol, no force-push, no history
rewrite. On the standing "never merge/redeploy before or during a pilot window" rule:
Mark told this thread directly he's dropping the pilot-gated framing and rebuilding the
site as it will actually look going forward — but he's the one telling you when that
takes effect, not this document. Don't treat pilot-fence removal as live until Mark
says so directly to you.

**Current state, as of `fc66ced` (pushed, origin and local both at this commit):**

1. **The epistemology-bridge fix is real, reviewed twice now, and live-verified.**
   `cic-poc/backend/app/graph/epistemology_bridge.py` — a two-beat Facilitator+Representative
   bridge for documentation-vs-inference questions, same pattern as the modern-term
   bridge. Root cause was more interesting than first thought: the existing
   `classify_frame_breaker` was already firing correctly on this question (4/4 in
   testing) — the actual gap was that its response never handed back to the seated
   Representative for the tradition-specific half. Fixed by reordering priority so the
   new bridge claims this category first. Verified live: Chloe answered fully in
   character with real citations. Full account in
   `Ministry/Operations/Audits/CiC_System_Hub_Handoff_RepresentativeSelfReference_2026-07-19.md`.

2. **The Atlas/World-Map redesign moved a long way, and is NOT merged.** A Fable-model
   research thread diagnosed why the live map was hard to use (a "Concept Demo"
   promoted straight to production, punch list undone), proposed a three-surface model,
   and built two prototypes. Mark ruled on all 5 open questions (recorded in
   `Ministry/Features/Atlas-World-Map/Decision-Log.md`, 2026-07-20 entries). A Phase 1
   build (the production Story view + one shared `world-census.json` asset, replacing
   `atlas.html`'s old iframe/wall-chart) was then built on Sonnet and is sitting on its
   own isolated branch: `worktree-agent-a4e025842dc994f8b` (worktree at
   `.claude/worktrees/agent-a4e025842dc994f8b`), tip commit `a659864`. **This has not
   been merged into `main` at all** — the live site still shows the old experience.
   - I personally re-verified it live (not just trusted the build agent's own report):
     all 5 live worlds render correctly, search/chips/panels/honest-redirects all work,
     zero console errors.
   - One real bug found in that re-verification, **not from this build**: horizontal
     scroll on phone, traced conclusively (hide-the-nav A/B test) to the site's
     pre-existing shared top nav bar — affects every page already, not new. Still
     unfixed, small, separate task.
   - **Three scope calls the build made that Mark hasn't ruled on:** (a) only ~17
     movements get real "Trace this thread" relationship graphs (the reviewed edge set
     from the spec) — the other ~160 show relations as prose only; (b) non-live entries
     without a specific researched connection get a generic "nearest open world by era
     and lane" redirect rather than a fabricated specific claim; (c) copy for 174
     entries comes straight from the census spreadsheet's own column, with the 4
     unbuilt Phase One worlds upgraded to fuller drafts for consistency. None urgent,
     all worth a quick yes/no from Mark before this merges.
   - Choose a Tradition (the in-app selector, Phase 2 — touches live `cic-poc` code) and
     the wall-chart verb-diet cleanup (Phase 3) are **not built at all**, prototype only.

3. **The full feature checklist is the current source of truth for "what's actually
   built."** `Ministry/Operations/Audits/CiC_Full_UX_Feature_Checklist_2026-07-20.md` —
   89 Program features (Implemented / Ready for implementation / Still needs testing /
   Still needs design work / No record), tagged by surface (Website/App/Both/System),
   split from the separate Business & Org Development track. This is what your
   content/feature-completeness pass should check claims against — it's been kept
   current through today's session (Alexandria fix, the epistemology bridge, the Atlas
   build all reflected in it already) and is more current than any earlier status
   report.

**What's open for you to work on, roughly by leverage:**
- **Battery A (Representative Modes validation)** — still the single longest-lead-time,
  zero-dependency item on the whole board. Nothing blocks starting this now.
- **Increment 1** (long-form transcript, table bar, brand tokens) — the single biggest
  unlock for the rest of the front-end backlog (role selection, guided questions, tour
  integration all wait behind it). Design is implementation-ready.
- **The Atlas Phase 1 merge decision** — once Mark rules on the 3 scope items above,
  this could land. Given the site-rebuild direction, this may be more timely than it
  looked yesterday.
- **The pre-existing site-nav phone overflow bug** — small, real, affects every page,
  found today, not yet fixed.
- **Content/feature-completeness pass itself** (Mark's `fc66ced` direction) — use the
  checklist above as the check-against source; flag anywhere the public site's copy
  overclaims relative to what the checklist marks as not-yet-Implemented.

**Coordination boundary:** Mark and I are continuing a feature-by-feature testing pass
conversationally in this thread — cheap, direct interaction with the running app, not
something you need to duplicate. Re-verify current git state yourself before starting
anything (`git fetch` + `git log --oneline -10`) rather than trusting this document's
snapshot, the same way you correctly caught the stale "concurrent conflict" framing
last time.

**Logging:** same standing convention,
`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`.
