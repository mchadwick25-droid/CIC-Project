# System Hub handoff — Ground-Up Rebuild becomes the base, go-live — 2026-08-11

**What this is.** A fresh System Hub thread continues the work of an extremely long
prior session, started because that session's own context had grown too large to
keep working in efficiently. Everything below is what that thread needs to pick up
cleanly, without rediscovering it.

## What just happened, in order

1. The existing Voice Rebuild (PR #9, the "1A" accessible-rigor redesign) shipped to
   `main`, then failed a basic test live: asked "who was Jesus," Papnoute answered
   with Antony's calling story and never characterized Jesus at all. Verified against
   the redesign's own stated bar (`Ministry/Technology/Pass2/decisions/
   VR_1A_Representative_Voice_Design_2026-08-09.md` §9) — the answer didn't even
   reach that doc's own "too simplified" worked example. Logged in
   `Ministry/Technology/Pass2/VR_1A_WORKLIST.md` item 11 and the Task Board.
2. Mark ruled: hold go-live, and pursue two parallel efforts — (a) a postmortem
   analyzing why the redesign failed despite passing every internal checkpoint
   (not done — never launched), and (b) a from-scratch rebuild of Representative +
   Facilitator + Table, deliberately cut loose from the 1A prompt-writing lineage,
   built up from the six worlds' own historical records instead.
3. For (b), a `world-records-only` branch was created — an orphan branch containing
   **only** `cic-poc/backend/wrs/records/{six worlds}/{gravity,figure,source,story,
   contested_claim,world_core,quote,term,force}` (688 files), deliberately excluding
   `voice_profile` (old Representative personas), `demonstration` (old scripted
   voice examples), `search_record` (build metadata), and the `facilitator/`
   subdirectory. A Claude Code Remote session was sourced directly from that branch
   (not `main`) so it structurally could not see the old Representative prompts,
   design docs, or checkpoint machinery — not just told not to look.
4. That session (title "Voice Rebuild — Ground-Up Rebuild (Interview Mode Only)")
   built a real system over several hours and pushed real commits directly to
   `world-records-only` (not a separate branch — check `git log
   origin/world-records-only` for the full history). It is genuinely lean: FastAPI +
   `anthropic` + `pyyaml` + `pydantic` only, no langchain/langgraph/torch/faiss/
   sentence-transformers. Plain HTML/JS/CSS frontend, no build step. Its own
   eval/test framework (`cic-poc/backend/evals/`, `cic-poc/backend/tests/`). A
   `personas.yaml` carrying the name/role/no-fabrication clause Mark and the prior
   session wrote together (see below). The session's own status as of hand-off:
   **"foundation system complete; ready for feature work"** — its own words, not a
   claim of production-readiness.
5. Mark tested it directly and extensively (four real artifacts on that session:
   "Six Worlds, Interviewed — Simulated Conversations," "— Live Model Results,"
   "— The Hour Test (Naive Questions)," and "A Conversation with Papnoute") and is
   satisfied with the result. His words: **"we have a very solid simple program
   working now that builds from the worlds to the table and the facilitator is
   working."**
6. Mark's decision now: **make this the new base.** Remove the old Representative/
   Facilitator/Table code from `main` entirely; the six worlds' records stay
   untouched either way. Get this deployed live.

## The one thing Mark was explicit about

**Do not edit or rewrite the new system's own code.** It was built independently on
purpose. Integrate and deploy it; don't revise its Representative/Facilitator/Table
logic. If something in it looks wrong, surface it to Mark rather than fixing it
directly — same as the item below.

## One flagged, unconfirmed thing worth Mark's own look

The new system's commit log includes *"Codify the two-register voice rule: 'we' for
the world, 'I' for the speaker in the room"* — this differs from what Mark specified
in the brief ("Always 'we' — never 'I,' never 'they'"). Not edited or resolved by
the prior session, per the instruction above. Worth Mark looking at `personas.py`
and `representative.py` directly and deciding if this is a real deviation or a
justified refinement.

## What "remove the last two rebuilds" concretely means

Old code to remove from `main` (the 1A/Voice-Rebuild-era Representative/Facilitator/
Table implementation):
- `cic-poc/backend/app/prompts/` (Facilitator prompts)
- `cic-poc/backend/app/graph/` (nodes, builder, governance, closing_sequence,
  epistemology_bridge, modern_term_bridge, repair_classifier, replay/ — the whole
  LangGraph orchestration layer)
- `cic-poc/backend/app/world_manifest.py`
- Every world's `*_Representative_Permanent_Prompt_*.txt` and
  `*_World_Capsule_Core.md` (in both `cic-poc/backend/data/*_world/` and the
  `World-Builds/*/` source copies — check both locations)
- The old React frontend (`cic-poc/frontend/src/`, `package.json`, build config) —
  the new frontend is plain HTML/JS/CSS with no build step
- `cic-poc/backend/wrs/views/`, `wrs/migrate/`, `wrs/gates/`, `wrs/glosses/`,
  `wrs/probes/`, `wrs/metrics/`, `wrs/schema/` — the old build/checkpoint tooling
  for assembling and validating the old prompts

**Untouched either way:** `cic-poc/backend/wrs/records/` (all six worlds' actual
research — this is the foundation both the old and new systems drew from, and nothing
about this rebuild changes it).

## Real gaps to close before this can actually go live — not optional

1. **No deployment infrastructure exists on the new branch at all** — no
   `Dockerfile`, no `render.yaml`, no `requirements.txt`. These need to be written
   fresh (this is new infrastructure, not an edit to the system itself, so it
   doesn't cross what Mark asked not to be touched). Minimal Python deps needed:
   `fastapi`, `uvicorn`, `anthropic`, `pyyaml`, `pydantic` — confirmed directly by
   reading every backend file's imports, not assumed.
2. **Undecided: does the new base carry forward Stripe giving, Supabase session
   storage / pilot-logging disclosure, and the possession-based session-token
   security** (`session_auth.py` — this closed a real leak found earlier this
   session: a bare session ID used to let anyone read or post into another
   participant's conversation)? The new system has none of this — it's
   interview-mode only, per its brief. **Asked, not yet answered as of hand-off.**
   Get Mark's call before deploying publicly, especially on the session-auth point —
   that's a real security regression if dropped silently rather than deliberately.
3. **Production is live right now** at `cic-poc.onrender.com`, currently serving the
   *old* system, with real participants potentially using it. Swapping the backend
   entirely is a hard-to-reverse, high-visibility action. Recommend at minimum: a
   working local/preview run before deploying, a check that citations/glossary
   hover-click actually render in a browser (the same category of gap that caused a
   real bug earlier this session — a CSS width mismatch is one thing, this is a
   full new frontend that's never been checked in a live browser against the real
   deployed backend), and watching Render's health/memory after deploy (the
   existing service was bumped from `starter` to `standard` plan after a real OOM
   incident this session — confirm whether the new lean system even still needs
   that headroom, but don't downgrade blind).

## Standing risk this project has going into any push to `main`

A `CiC Integrity Audit <audit@cic.local>` git identity has a documented history of
pushing directly to `main` without review, including a real data-loss incident and
at least one case of citing a commit hash that didn't support its own claim. Never
fully resolved — branch protection (require PRs, block force-push/deletion, empty
bypass list) was recommended but, as of this hand-off, not confirmed enabled at the
actual GitHub repo settings level. Worth checking before or alongside this work,
since a full backend replacement landing on `main` unreviewed is exactly the kind of
change that identity's pattern would make worse, not better.

## Where things live

- New system: `origin/world-records-only` branch, real commit history from
  `d67d83d5` (the orphan world-records-only root) forward.
- The Ground-Up Rebuild session itself (for its own conversation history/artifacts,
  read-only — do not send it further instructions per Mark's "do not mess with it"):
  `session_018qX3v1BXLkzwSq8SDoDPDz`.
- Full context on the original failure and the postmortem-that-never-ran:
  `Ministry/Technology/Pass2/VR_1A_WORKLIST.md` item 11, Task Board DO NOW list.
- This document's own home, for anyone landing here later:
  `Ministry/Operations/Standing/Launch-Prompts/
  CiC_System_Hub_GroundUp_GoLive_Handoff_2026-08-11.md`.
