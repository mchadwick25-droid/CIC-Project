# Tech-Readiness Package 2 — Operations — Report

Dated 2026-09-21. Dispatched by the reviewer thread "CiC — Tech Review &
Funding Readiness Prep" against AWS Well-Architected's Reliability pillar and
standard site-reliability practice (backup/restore with RPO/RTO, rollback,
alerting, incident runbook). Scope, per the launch brief: make one service on
one disk, with real participants, operable by someone who is not the
founder, and prepare — not perform — the next `main` → `live` promotion.

**A note on the brief itself.** The launch brief's own divergence claim was
checked before anything was built on it and found backwards on first pass
(a stale `origin/main` ref in this sandbox, since corrected) and, on
re-verification with `origin/main`/`origin/live` freshly fetched, the brief's
overall shape was confirmed correct (main ahead on the transparency engine,
live ahead on atlas tooling and the card redesign) — see Decision-Log entry
1 for the full back-and-forth. Every number below was produced by the git
commands themselves against the branches as fetched at report time, not
carried over from the brief.

## 1. Divergence inventory

**Commits compared:** `origin/main` = `c9b09ea1` (merge base with `live`:
`20264dec`), `origin/live` = `e693b048`. Both freshly fetched
(`git fetch origin main live`) before every command below.

```
git diff --name-only --diff-filter=A origin/main origin/live   # live-only  → 43 files
git diff --name-only --diff-filter=D origin/main origin/live   # main-only  → 158 files
git diff --name-only --diff-filter=M origin/main origin/live   # both differ → 1,300 files
```

### (a) On `main` only — the Conversation & Transparency Engine

`main` carries `Ministry/Features/Conversation-Transparency-Engine/`
(README, Adjusted-Design, Build-Plan, Rulings-Pending, Decision-Log — the
last with **27 entries**; `live`'s own copy of the same 5 files has only
**3**, i.e. `live` predates the workstream's own scope-correction, Entry 3).
Stages merged to `main` and not yet on `live` (Decision-Log entries 4–27):

| Stage | What | PR / commit |
|---|---|---|
| 0a | Concurrent safety/reader gate calls | #339 `0175b5be6` |
| 0b | Leave button no longer disables mid-turn | #340 `460b5194f` |
| 0c | Real `round_cap` surfaced to the frontend | #341 `9ddc9c843` |
| 0d | `safety_script_run.py --all`, model pin in `render.yaml` | #343 `11e2093c5` |
| 0e | `observe_outside_help_guard` (report-only) | #342 `bdc7cf252` |
| 1 | D1 grounding-fooling measurement (3 corpora) | #344 `86be79c4c` |
| 2a/2b/2e | Spoken-fields registry, bar-screen tool, 4 new retrieval benches | direct-to-main, Entries 8/9/11 |
| 2c/2d | `observe_register_profile`, `engine/m9/holdings.py` | #349/#350 |
| 3c/3d | Citation-mark dropout fix (anchor renderer), `gloss_forms` gating | #335/direct |
| 4a | R11 split: schema, gallic pilot, fleet migration (11 worlds), structural gate, evidence riders | #359/#360/#361/#366/#372 |
| 4b | `guard_proximity` output-check family | #374 `0155da66` |
| 4c/4d/4f | `retrieval_words()` relocation, tier-prior ranking, table secondary-context | #325/#326/#334 |

Also on `main` only: a new, **unregistered** world `lpc` (Latin
Pastoral-Congregational Christianity — 84 files under `worlds/lpc/`, 9 new
`packages/cappadocian` etc. repins from the fleet-wide Stage 4a migration,
not `lpc` itself). Confirmed not in `records/worlds.yaml` on either branch
and not in `packages/lpc/` — **promoting `main` → `live` today would not
newly expose it**: `CIC_ENFORCE_ADMISSION=1` in production gates on the
registry, and `lpc` isn't in it. Still in build (`Doc_02` self-disposed
2026-09-12; later docs not checked here — out of this package's scope).

A **governance-relevant single-line diff, resolved, not open:** `main`'s
`CLAUDE.md` is missing a row `live`'s copy still has —
`| Representative identity, title, or voice decision | Always ask |`.
Traced to commit `6f3a4e6e` (2026-09-20, "Remove the default-actions table's
Representative-voice row"): **Mark's own direct instruction that session**,
removing a row a prior session had added on a misread of intent (full
reasoning in that commit's own message). `live` simply predates this
authorized edit — its own last branch point is before it — so this is
ordinary one-directional staleness a promotion resolves automatically, not
a live-authored different decision competing with it. Flagged here because
`CLAUDE.md` is the one file where an unexplained diff would be disqualifying
on sight; this one has a clean, dated, already-Mark-approved explanation.

### (b) On `live` only — atlas-sync tooling and the card redesign

- **Atlas-sync tooling:** `engine/m2/site_cli.py`, `engine/m2/
  site_compiler.py` (+ tests), `engine/m6/atlas_html.py`, `engine/m6/
  census_atlas_sync.py` (+ tests) — introduced by commit `5191cf5f`
  ("Add engine/m6/census_atlas_sync: sync atlas-v3.html from
  world-census.json") and its own follow-ons. **Not on `main` at all.**
- **The "who-is-at-the-table" card redesign** (PR #346, merge commit
  `e693b048`, preceded by `957410a5` and a string of fixup commits):
  `cic-website/` template/asset changes, portrait-image removals,
  `engine/m1/tests/test_world_front_gates.py` / `test_world_front_schema.py`,
  `records/fix/world_front/fix.front.fixture-synthetic.md`, `tools/
  check_no_embedded_world_data.py` — a fleet-wide package rebuild
  (`f0801f72`, "repin all 12 worlds to this merge commit") went with it.
- A handful of `Ministry/Features/*` docs (Backend, Brand-Messaging-Rework,
  Built-World-Voice-Alignment, Front-End-Integration-Strategy,
  Representative-Modes) exist on `live` and not `main` — **not investigated
  further in this pass**: distinguishing "genuinely live-only content" from
  "moved/renamed during main's own repo-structure-cleanup phase 2/3, so it
  merely looks deleted" needs a per-file check this Operations package didn't
  have scope or reason to do (none of these are engine/render/runbook
  surfaces). Flagged for whoever runs the promotion PRs below to eyeball
  before merging, not asserted safe.

### (c) Differs both ways (1,300 files)

Overwhelmingly `records/<world>/**` and `packages/<world>/**` for all 11
built worlds (1,027 of the 1,300) — expected and mechanical: `main`'s Stage
4a fleet migration (PRs #360/#361) rewrote every world's
`do_not_retrieve_when` field and repinned every package; `live` has its own
independent repin from the card-redesign rebuild (`f0801f72`). Neither side
is wrong; a merge needs the migration tool's own output to win on content
(it's a mechanical field-level rewrite, not hand-edited prose) with a fresh
repin afterward, not a manual per-record reconciliation.

Also both-differ, worth naming directly rather than folding into the
records/packages count: `render.yaml` (see §2 below — main's Stage 0d model
pin, this package's own new backup-bucket vars), `CLAUDE.md` (§(a) above),
`.github/workflows/ci.yml` (30 insertions / 64 deletions — not
investigated line-by-line this pass; CI is green on `main`'s own head per
every Decision-Log entry above, which is the check that actually matters),
and `engine/api`, `engine/m1`–`m9` broadly (the natural footprint of the
transparency-engine's own 24 merged PRs).

## 2. Promotion PR set (drafted, not performed)

**Central finding this inventory surfaces for Mark, not resolved here**
(cross-branch/portfolio-level call, `CLAUDE.md`'s own "always ask" row):
`main` and `live` have drifted in **both directions** since their common
ancestor (`20264dec`). A plain `main` → `live` merge would not fast-forward
and risks the merge tool choosing `main`'s side of `engine/m2/`, `engine/m6/`
and `cic-website/` — silently reverting the atlas-sync tooling and the card
redesign in production, since `main` doesn't have either. **The atlas/card
work needs to land on `main` first**, the same way any other feature does,
before a `main` → `live` promotion is safe to treat as "everything on `main`
is what should ship."

Proposed order, each step gated on the Promotion Runbook's own "verify on
staging first" rule:

**PR 1 — Reconcile `live`-only work back onto `main`.**
Merge (or cherry-pick, if history conflicts make a merge messy)
`e693b048`'s own line of work — the atlas-sync tooling and PR #346's card
redesign — into `main`. This is a normal feature PR into the integration
sandbox, reviewed the same as any other `main` PR; it is not a promotion and
does not touch `live`. **Verify on `cic-engine-staging`:** the Atlas page and
`world-census.json` sync render correctly, the card redesign displays as it
does today in production, and none of Stage 4a's fleet migration (PR
#360/#361, already on `main`) gets clobbered by the reconciliation — run
`retrieval_bench.py` and `engine.m9.cli check` after, expect no change from
`main`'s current baseline (1154 grounded, 0 empty).

**PR 2 — Confirm `lpc` stays inert.** Not a PR by itself — a check to run
immediately before PR 3: `grep -c lpc records/worlds.yaml` should still be
`0` and `packages/lpc/` should not exist. If either has changed since this
report, stop and ask Mark before promoting — an unregistered, unreviewed
world reaching `live`'s own registry is exactly the boundary
`CIC_ENFORCE_ADMISSION` exists to hold.

**PR 3 — The actual promotion, `main` → `live`.** Only after PR 1 has
merged to `main`, deployed to `cic-engine-staging`, and been verified there.
Title per the Promotion Runbook's own convention: "Promote: Conversation &
Transparency Engine (Stages 0–4b) + atlas/card-redesign parity." The diff at
that point is the promotion's own record (Promotion Runbook §"the promotion
procedure itself" step 2) — no separate log entry needed beyond what this
report and the workstream's own Decision-Log already carry. Mark reviews and
merges per the runbook; Render deploys `cic-engine` from the new `live` tip
automatically.

**This package performed none of the above** — PR 1 touches `engine/m2/`,
`engine/m6/`, and `cic-website/`, all outside this package's own hard-rule
scope (render.yaml, docs, a backup script, and runbooks only), and PR 3 is
explicitly Mark's own act under the Promotion Runbook. Both are handed to
Mark and logged with the transparency-engine workstream now (Decision-Log
entry appended there, per the launch brief's own instruction).

**Correction, 2026-09-22 (superseding this section's plan, not its
divergence inventory above).** After an unshallowed check, the reviewer
thread found the merge base above (`20264dec`) was correct but the
resulting risk assessment was not: **a merge PR does not revert live-only
content** — that concern applies only to a naive "copy `main`'s side of
these specific paths" approach, which this package never attempted and the
three-PR sequence above was designed to avoid by routing around it, not
because a plain merge was actually unsafe. A real `git merge origin/live`
into a branch off `main` was run instead of the sequence above: genuinely
clean for `cic-poc/frontend` (verified: zero changes on `live`'s side since
the real base), with real, resolvable conflicts elsewhere (4 code files in
`engine/`/`.github/`, 12 registry package-pins rebuilt fresh, 4
`Open_Gaps_Tracking.md` files unioned, 6 further record conflicts that
turned out to be false alarms on full-file diffing, not scholarly
disagreements). Full detail, file-by-file: `Ministry/Features/
Conversation-Transparency-Engine/Decision-Log.md` Entry 34 and this
package's own Decision-Log, Entries 10–11. Result: merged to `main`,
895/895 tests passing, `engine.m1.cross_world` 0 new defects,
`engine.m9.cli check` clean, `tools/check_paths.py` 0 new unresolved
citations. **PR 3 (the actual `main` → `live` promotion) is unaffected by
this correction and remains Mark's own act under the Promotion Runbook,
now unblocked** — the reconciliation it was waiting on has landed.

## 3. Backup and restore

Full procedure, one-time R2 setup, and restore steps:
`Ministry/Operations/Standing/CiC_Backup_Restore_Runbook.md`. Mechanism:
`engine/api/db_backup.py` (sqlite3's online backup API, never a file copy;
in-process daily thread — a Render Cron/one-off Job cannot reach a disk
already attached to `cic-engine`, verified against Render's own docs, same
constraint `engine/m7/scheduler.py` already documents and solves the same
way). 10 new unit tests, `engine/api/tests/test_db_backup.py`, all passing;
zero regressions in the existing `engine/api` suite (identical 33
failed/23-errored/51-passed count with and without this change — a
pre-existing, unrelated Stage-0c package-completeness gap per Decision-Log
Entry 13, confirmed by running the suite both with and without this
package's changes stashed).

**Restore proven locally, row-for-row, against the real schema** (not a toy
table — `engine.m4.store.Store` and `engine.m8.log_store.UsageLogStore`
directly):

```
BEFORE: 8 events across 2 sessions, 4 usage rows
BACKUP: wrote /tmp/restore-proof/backups/events-backup.db (16384B), /tmp/restore-proof/backups/usage-backup.db (12288B)
DESTROYED: live events.db deleted, live usage.db overwritten with garbage
RESTORED: both DBs replaced from their online backups
VERIFIED: 8 events row-for-row identical, 4 usage rows row-for-row identical
RESULT: PASS
```

**RPO: up to 24 hours** (one backup per day; a stated, reasoned tradeoff for
a solo-operator pilot, not an oversight — see the runbook for the full
reasoning and how to tighten it if pilot volume ever demands it).
**RTO: estimated 30–60 minutes**, built from measured step timings (the
restore command itself, locally) plus documented Render mechanics
(Suspend/Resume, Shell/SSH) — **not yet measured end-to-end against the real
Render dashboard**, because this sandbox cannot reach the production disk
(same restriction the Promotion and Object Storage runbooks already state).
The runbook recommends a live drill against `cic-engine-staging` (no real
participant data at risk) as the natural first real measurement.

## 4. Alerting spec

Full spec, thresholds (2 options each, Mark's to pick), and dashboard steps:
`Ministry/Operations/Standing/CiC_Alerting_Runbook.md`. Verified against
Render's own docs and community answers, not assumed: Render natively
emails/Slacks on deploy failure and deploy-time health-check failure
(signal 1, ready today); 5xx rate, disk-usage threshold, and 429 rate do
**not** have a native alert without Render's Pro-tier metrics streaming, so
each gets a zero-additional-cost design (a GitHub Actions cron polling
`/health`, the Render disk-usage API, or a small new ops-metrics endpoint
this pass did not build) rather than assuming a paid tier this project's own
usage discipline doesn't budget for. Bedrock spend uses native, free AWS
Budgets (signal 4, ready today). Full readiness table in the runbook itself;
summary: **2 of 6 signals are wire-it-up-today; 1 more is half-ready; 3 name
the exact small follow-on piece needed, not silently assumed built.**

**Pre-merge fix (2026-09-21):** signal 2's own dashboard steps cited
`.github/workflows/health-check.yml` as if it already existed, which
`tools/check_paths.py`'s CI job (`Cited paths resolve; retired paths
absent`) correctly caught — that workflow is spec-only, not built this pass
(same as signals 3/5/6), so citing it as a real path was wrong to write.
Reworded to describe the workflow instead of naming a not-yet-created path;
no `tools/check_paths_baseline.txt` entry was needed, since the citation was
simply incorrect rather than a real pre-existing gap. Confirmed green
locally: `python3 tools/check_paths.py --baseline
tools/check_paths_baseline.txt` exits 0, 0 new unresolved citations. Full
account: this package's own Decision-Log, Entry 9.

## 5. Rollback drill and incident runbook

Full runbook: `Ministry/Operations/Standing/CiC_Incident_Rollback_Runbook.md`.
Rollback mechanism verified against Render's own docs (not guessed):
Dashboard rollback to a previous deploy is real, fast, and **automatically
disables autodeploy** for the service — a confirmed side effect the runbook
calls out explicitly, since forgetting to re-enable it means the next
legitimate promotion PR merges and silently doesn't deploy. The Promotion
Runbook's own "revert the promotion PR" method is the permanent fix;
dashboard rollback is the fast mitigation, and the runbook says to do both,
in that order. Trace-by-identifier: there is no separate "request ID" field
— the real identifiers are `session_id` (every event) and `trace_id`
(per model call, `usage_log` only); the runbook gives the exact
`Store.read_events`/`UsageLogStore.read_for_session` calls. Bedrock-
unreachable and disk-full procedures are in the runbook, including the one
real gap named rather than hidden: **no cross-region Bedrock failover
exists**, a deliberate scope exclusion for a single-region pilot, not an
oversight.

## 6. Baseline repin — prepared, not executed

Per the launch brief's own instruction, this runs only once Mark confirms
the PR 3 promotion above has landed — not before. Prepared procedure:

1. On `live`'s new tip (post-promotion), run the fleet determinism check:
   `python -m engine.m2.cli restore` (rebuilds every package from `records/`
   and verifies against each manifest's own hash — the same command
   `engine/Dockerfile` runs at image build time) and `python -m pytest
   engine -q` for the test-pass count.
2. Record the new baseline in `engine/BASELINES.md`: a new `## baseline/
   <name>-<date>` section, the promoted commit's short hash, one row per
   world with its `packages/<world>/<timestamp>/` path and manifest hash
   (from step 1's own restore output — never hand-typed), the
   `pytest`/`selftest` pass counts, and Mark's own quoted sign-off on the
   promoted state (this file's own established format — see the existing
   `pilot-2026-08-24` entry for the shape to match).
3. Push a new frozen branch `baseline/<name>-<date>` at that commit (this
   session's credential can push `refs/heads` but not `refs/tags`, per
   `engine/BASELINES.md`'s own note — branches, not annotated tags, same as
   the existing baseline).
4. Leave `baseline/pilot-2026-08-24` in place, untouched — nothing here
   supersedes it as *the* voice-quality baseline unless Mark says so;
   this adds a second, newer reference point, per the file's own "points
   worth being able to return to" framing (plural).

Not run in this pass: promotion PR 3 has not landed (§2 above), so there is
nothing yet to repin against.

## 7. Runbook currency

- `reference/Redesign-Spec/PHASE-1-LAUNCH.md`: added a dated currency note
  (2026-09-21) — every stage is DONE/closed-by-decision, and the
  single-branch deploy model it describes was superseded 2026-09-15 by the
  two-branch promotion model. Kept in place (not archived) as the accurate
  historical record of how Phase 1 actually shipped; nothing deleted.
- `Ministry/Operations/Standing/CiC_Promotion_Runbook.md` and
  `CiC_Object_Storage_Runbook.md`: reviewed against today's `render.yaml`
  and `README.md`, dated 2026-09-21 — both already current, no drift found.
  Their own "one-time setup" dashboard steps could not be re-verified as
  *done* from this sandbox (Render/GitHub dashboard state isn't readable
  here); left exactly as previously stated rather than asserted complete.
- Two new Standing runbooks added this pass:
  `CiC_Backup_Restore_Runbook.md`, `CiC_Alerting_Runbook.md`, and
  `CiC_Incident_Rollback_Runbook.md` (§§3–5 above).
- Nothing moved to `Archive/` this pass — nothing checked was found
  genuinely superseded-and-inert; `PHASE-1-LAUNCH.md` remains referenced by
  gate number elsewhere and earns a currency note rather than a move.

## Reliability-pillar checklist, for the reviewer thread

| Requirement | Status |
|---|---|
| Backup mechanism, verified against real platform constraints | Done — in-process online backup, Render Cron/Job disk limitation confirmed and designed around |
| Restore procedure, proven with real data | Done — row-for-row, real schema, output on file above |
| RPO stated with reasoning | Done — 24h, reasoned tradeoff for pilot scale |
| RTO stated with reasoning | Estimated, not yet live-measured — sandbox cannot reach production; staging drill recommended |
| Rollback procedure, verified against real platform mechanism | Done — dashboard rollback + PR-revert, autodeploy side effect documented |
| Incident runbook (trace lookup, Bedrock down, disk full, paging) | Done |
| Alerting: what to watch, thresholds, config location | Done — 2 of 6 wired today, 3 spec'd with a named small follow-on, 1 half-ready |
| Divergence between deploy branches inventoried before promotion | Done — 43/158/1,300 files, categorized, one governance-relevant diff traced and resolved |
| Promotion prepared, not performed | Done — 3-PR sequence drafted, handed to Mark, none executed |
| Baseline repin | Prepared, correctly not executed (promotion hasn't landed) |
| Coordination boundary with the Transparency Engine workstream | Held — no edits to `engine/m1/`, `m2/`, `m4/`, `records/`, or the frontend renderer; `engine/api/db_backup.py` and a 2-line `app.py` addition are this package's only engine-tree touches, both additive and outside those five paths |
