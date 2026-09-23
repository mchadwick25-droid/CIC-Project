# System Health — Standing Thread Tracking

Running, dated ledger for the System Health thread. Same discipline as the world-build
threads' own `Open_Gaps_Tracking.md` files: dated entries, honest status, root cause over
symptom. This file is the durable record of what this thread found and did; no finding,
fix, or escalation lives only in a session's own conversation history.

---

## Thread scope (established at thread launch, 2026-09-03)

This is **not** a world-build thread, **not** the Library Build Engine thread (which owns
source acquisition and `cic/texts//cic/corpus-map/` specifically), and **not** a
governance/methodology authority. It exists to catch the gap every other thread's bounded
view leaves open: repo-wide CI/deploy/build failures that are the same on every branch,
meaning no single PR's diff caused them and nobody with standing to fix them at the root
has claimed them.

**Mandate:**
- Monitor CI across `main` and all open PRs — GitHub Actions, Cloudflare Workers Builds,
  Netlify, Docker builds, any other pipeline.
- Diagnose root cause, not symptoms — reproduce locally where possible, check whether a
  failure is new or pre-existing on `main`'s own tip before assuming a PR caused it.
- Fix directly, straight to `main`, when the fix is mechanical and non-judgmental (missing
  config, a Dockerfile line, CI YAML, a build script bug) — per Mark's direction, without
  routing one-line infra fixes through a full PR cycle.
- Escalate rather than guess when a fix touches real judgment, or would touch a specific
  world's own build content — that stays each world's own thread's call, always.
- Coordinate with the Library Build Engine thread rather than duplicating or silently
  working around its own mandate.

**Added mandate (2026-09-03, Mark's direction):** watch that other threads are not putting
the system at risk by adding notes, comments, or changes into the **build and run
documents** (engine/, cic/, records/, cic-website/, World-Builds/ final deliverables, and
this repo's other production trees) that don't serve the system running well — those
documents need to stay clean at all times. Scratch notes, WIP commentary, and tracking
belong in standing notes documents like this one, not in the build/run trees themselves.
This file itself follows that rule: it lives in `Ministry/Operations/Standing/`, not inside
any build or run tree.

**What this thread is explicitly not:** no Doc_01–Doc_10 construction work, no
representative-identity/portfolio/Change-Orders-Register authority (CO-022 escalation
categories stay with Mark directly), no duplication of the Library Engine thread's own
source-acquisition mandate.

---

## 2026-09-03 — Thread opened: two repo-wide bugs, wrangler fix shipped, first full sweep

**Context this thread was opened to address:** two same-on-every-branch bugs surfaced
today outside any single thread's view — no `wrangler.toml/json/jsonc` anywhere in the
repo (every Cloudflare Workers Build failing, every branch, "A compatibility_date is
required"), and `engine/Dockerfile` never copying `cic/texts/` into the build image
(two citation-validation gates failing in every Docker build, every world) — the second
found and fixed only as a side effect of the Library Build Engine thread's own unrelated
work.

**Fixed — `wrangler.jsonc` added, pushed directly to `main` (`6dce219c`).** Minimal
config: `name: "cic-website"` (matches the already-diagnosed Worker-name mismatch),
`compatibility_date`, and an explicit `assets.directory: "./cic-website"`.

Checked, not assumed: whether the dashboard build command's existing
`--assets=cic-website` CLI flag already covered the assets binding. Confirmed against
Cloudflare's own docs (`raw.githubusercontent.com/cloudflare/cloudflare-docs`) and
workers-sdk issue history — `--assets` only drives Wrangler's *interactive*
config-generation prompt, undocumented and reportedly non-functional in a non-interactive
CI run like Workers Build. `assets.directory` in the config file is required regardless.
Verified locally with `wrangler deploy --dry-run`, both with and without the CLI flag —
identical result (38 files read from `cic-website/`), confirming the config file alone is
sufficient.

**Verified, not assumed — Docker `cic/texts/` fix is genuinely on `main`.** Commit
`9b430204` confirmed via `git log` on `origin/main` and by reading `engine/Dockerfile`
directly (`COPY cic/texts/ cic/texts/` is present); its own CI run
(`33795931038`) is green.

**First full sweep — `main` + all 4 open PRs** (task briefing listed 3 as of today —
#78, #11, #10 — a 4th, #85, opened mid-sweep; caught it live rather than missing it):

| Where | Finding | Disposition |
|---|---|---|
| `main` tip | GH Actions green. Cloudflare Workers Build should clear on next push with the fix above — could not independently re-observe the live check result this session (no tool path to query GitHub check-runs for a bare commit outside a PR context); confirmed instead via local `wrangler deploy --dry-run` reproducing the exact fix mechanism. | Fixed |
| PR #78 | All engine/Docker checks green (PR's own body already correctly self-diagnosed the Cloudflare failure as pre-existing and unrelated to its diff). Only `Workers Builds: cic-project` red, pre-fix. | Repo-wide, fixed above — should clear once this PR next syncs/rebuilds |
| PR #85 | `Workers Builds: cic-project` red — same repo-wide bug. **Also** `M1 gate battery selftest (fixture world)` red: `test_the_fleet_carries_no_undocumented_drift` reports all 7 built worlds' `census_id` missing a `PORTRAIT_FILES` entry. Reproduced locally against `main`'s own tip — **passes clean, 10/10** — so this is not pre-existing. Root cause: `engine/m1/cross_world.py` parses `PORTRAIT_FILES = {...}` directly out of `cic-website/index.html`'s inline JS; this PR's website rewrite ("Website V2 entry path") appears to have changed or removed that block without the gate's expectation being updated. Content-level, belongs to that PR's own thread. | Repo-wide part fixed above; website-content part flagged to PR owner, not touched |
| PR #11 | One red test (`Runtime tests (prompt assembly)`) inside a test suite the PR's own description says it just added — PR-content-level, not infra. Also: PR targets `claude/cic-cost-architecture-review-6j5et0`, not `main` — its own description flags "which branch is production is still an open question," a governance question outside this thread's authority. | Not this thread's — noting the open production-branch question for Mark |
| PR #10 | All checks green but stale (last CI run 2026-08-10; `main` has moved 95+ commits since) and `mergeable_state: dirty` (merge conflict). Judgment-heavy content (B1/B2/B6 cost architecture) — not a mechanical fix. | Not this thread's — flagging staleness/conflict, not resolving |

**Ongoing monitoring structure, confirmed with Mark before standing up (2026-09-03):**
scheduled periodic full sweep of `main` + all open PRs (this session, via a recurring
Routine) plus reactive `subscribe_pr_activity` on currently-open PRs for CI/deploy signal
between sweeps. This thread's subscription to a PR is for infra-pattern signal only — it
does not make this thread a general steward of that PR's content-level review threads or
comments; those stay with the PR's own owning thread/author, same as the disposition table
above.

Routine and PR subscriptions stood up same day: `subscribe_pr_activity` on #78, #85, #11,
#10; a 6-hour recurring sweep Routine (`trig_018SBnt1JTXwWkRoEfqJTZwP`) bound to this
session.

---

## 2026-09-04 — First scheduled sweep: PR #85 fixed itself; the wrangler fix above was
## wrong, corrected, and now confirmed live

**PR #85 merged.** Its own thread found and fixed the `M1 gate battery selftest` /
`PORTRAIT_FILES` regression flagged above (`342b0660`, "Fix M1 site-portrait check for
the new homepage architecture") before merging — confirms yesterday's disposition
(content-level, that PR's own thread's call) was the right call, not a punt. No open PRs
now besides the original #78/#11/#10; nothing new to subscribe.

**Caught: the 2026-09-03 wrangler.jsonc fix did not actually clear the Cloudflare check.**
`main`'s Workers Build (checked via PR #85's own last pre-merge CI run, which included
the wrangler fix as an ancestor) was still red — same fast, 0-duration failure pattern as
before the fix, meaning it was failing at the same early pre-build stage, not later in
the actual asset upload. Root cause: the config's `"name": "cic-website"` was wrong. The
check run's own GitHub name — **"Workers Builds: cic-project"** — and its Cloudflare
dashboard URL (`.../workers/services/view/cic-project/production/...`) both name the
real registered service `cic-project`, evidence external to this repo that wasn't pulled
up before the first fix. `cic-website` was a guess from the folder name, not confirmed
against the actual dashboard-linked service — a real gap in yesterday's diagnosis, caught
here specifically because the standing sweep re-checked the *result* of a fix instead of
assuming a push meant it worked.

**Fixed:** `wrangler.jsonc`'s `name` corrected to `"cic-project"` (`1b3f767c`, pushed
straight to `main`, same authorization as the original fix). Re-validated with
`wrangler deploy --dry-run` — still parses clean, 38 files read from `cic-website/`.

**Confirmed live, same day, at Mark's request ("go ahead and run it now").** Same tooling
gap as before — no way to query GitHub check-runs for a bare `main` commit outside a PR
context — so verified by syncing PR #78 with `main` (`update_pull_request_branch`, a
standard, non-content-changing sync that PR needed regardless) to get an observable,
fresh check run. Worth noting for next time: the Cloudflare check took noticeably longer
to post than usual (~90 seconds after every other check had already completed, versus
under a minute in every prior observation) — don't read a temporarily-missing Cloudflare
check as itself a problem; give it a couple of minutes before concluding anything. Once it
posted, it ran as a real **in-progress** build rather than the instant 0-duration
pre-flight failure both earlier attempts showed — itself a strong signal before the final
result — and finished: **"✅ Deployment successful!"** (`cic-project`, commit `4eb713eb`,
both a commit preview URL and a branch preview URL returned). Both the `compatibility_date`
and the `cic-project` name fix are now verified working end-to-end, not just locally
dry-run-validated.

**Doc-hygiene spot check (2026-09-04):** reviewed `main`'s recent commit log (PRs #85–#88,
all website content/copy changes) — nothing suggesting stray notes, WIP commentary, or
scratch changes landed in a build/run tree. Nothing to flag.

**Next action:** none open on the wrangler fix — closed out. Next scheduled sweep resumes
normal cadence: main + open PRs, repo-wide vs PR-specific triage, doc-hygiene spot check.

**PR #11 and #10 re-checked, same day, at Mark's request.** No change from the sweep
above — same head commits, same check results, nobody has touched either since. #11's
one red check (`Runtime tests (prompt assembly)`) is still its own newly-added test suite
on a non-`main` base branch; #10's checks are still all green but frozen at 2026-08-10.

**Escalated to Mark directly (not a PR comment — content-level, that PR's own call, per
this thread's standing rule): PR #10 staleness.** 25 days with no commit or CI activity;
`mergeable_state: dirty` (conflict against `main`, which has moved ~100 commits since);
its own body still carries two unchecked "before merging — owner: Mark" items (a
replay-parity run needing real network egress outside the build sandbox, and a request
that a human see the transparency surfaces rendered at a table). Not inert queued work —
it carries the round-cap-6→4 change ruled to ship with Phase A, and the dormant Haiku
speaker-label-repair fix whose own ordering note says it must land before `LLM_MODEL`
ever flips to Haiku. Flagged so it doesn't fall through the cracks with nobody driving it;
disposition (merge, close, or revive) is Mark's call, not this thread's.

---

## 2026-09-04 (later) — Second scheduled sweep: `engine/api tests` red on every `main`
## push since `67398b18` — root-caused, escalated, not fixed

**Repo-wide, not PR-specific — confirmed the hard way.** `main`'s last three pushes
(the PR #78 merge, this thread's own docs-only tracking-doc commit, and a later
iframe-embed fix) all show GitHub Actions CI `failure`. The docs-only commit failing is
the tell: a markdown-only change can't break a test job, so this had to be baked into
`main` itself, not caused by any one diff. Same single job fails every time:
`engine/api tests (mocked Bedrock, fixture world)` →
`test_a_repin_mid_session_does_not_refuse_the_in_flight_session` in
`engine/api/tests/test_wiring.py`.

**Root cause, traced not guessed.** That test (added in `67398b18`, "Fix: a repin
mid-session no longer refuses an in-flight conversation" — itself a real regression test
for a live bug Mark hit) hardcodes two historical package snapshots
(`packages/fix/2026-09-03T14-57-38Z` and a same-day newer one) and expects their
compiled bytes to already exist on disk. This repo's own policy
(`packages/README`/`.gitignore`) deliberately excludes compiled package bytes from git —
only `manifest.json` is committed. The test passed for its author because those bytes
were still sitting in their own local working session; a fresh checkout (CI, or any new
clone) never has them. Now permanent: every future branch built from this point on will
hit the same failure, the same signature as the wrangler/Dockerfile bugs.

**Why this thread isn't fixing it directly.** Checked whether `engine.m2.cli build
--records-commit <hash>` could mechanically regenerate the missing snapshot — traced
`compile_world()` in `engine/m2/compiler.py` and confirmed `records_commit` is written
into the output purely as a provenance label; the compiler actually reads whatever's
*currently* on disk under `records/`, it does not check out that historical git commit.
Reproducing the exact historical package would mean checking out an old commit's
`records/` tree mid-CI-job, compiling, hash-verifying against the manifest, then
restoring `HEAD` — real engineering work with no existing tooling for it, on a
regression test guarding a real bug Mark hit. Getting it wrong risks either
destabilizing CI further or silently weakening the test. That's judgment, not a
mechanical config fix — escalated to Mark in conversation rather than guessed at.

**Recommendation given to Mark:** route back to whoever wrote `67398b18` (session
`01CeFxRLYeZxyc5dSb1Xq7Tg`) — they understand the test's actual intent and can decide
the right fix: properly rebuild both historical snapshots (checking out each one's own
`records_commit` first), or rewrite the test to compile two fresh, differently-pathed
packages itself instead of depending on specific pre-existing timestamps.

**Next action:** none from this thread until Mark or that session decides a fix
direction. Not logging this as "resolved" — CI stays red on `main` until it's addressed.

**Resolved same day.** Mark had this thread route the finding directly to that session
(`session_01CeFxRLYeZxyc5dSb1Xq7Tg`, tagged `cic-library-engine`) via a one-shot scheduled
wake — no live peer-messaging path existed since the session was idle/disconnected, not
actively running. It independently re-verified the failure against the real CI run/job
logs before touching anything (same discipline this thread held to), then pushed
`ad8ecce1` ("Fix: the repin regression test now compiles its own packages,
hermetically") — the path this thread's own writeup called safest: the test now compiles
two real `fix` packages into `tmp_path` itself rather than depending on pre-existing
historical timestamps. `main`'s CI is green again as of that push (verified: run
`33866398393`, `engine/api` + `engine/m4` suite, 329 tests, all passing). Closed.

---

## 2026-09-04 (evening) — Two new standing duties added, relayed from Mark via the
## website/product thread: M7 daily audit scheduling, and a fleet-size watch

**M7 conversation-quality audit, scheduled.** `engine/m7` is a real, working
transcript-audit pipeline that already reads the same production `session_events`
store every pilot conversation is durably and anonymously recorded into (schema
confirmed by direct code read: no name/email/IP/account_id column). It had been run
manually before; nothing ran it on a schedule — the one real gap in an otherwise-live
pilot data pipeline. Given this touches the live pilot service and real (if anonymous)
conversation data, this thread confirmed directly with Mark before writing or deploying
anything, rather than acting purely on the relay.

Investigated the mechanism before picking one: `render.yaml` confirms `cic-engine` is
the ONE Render service with the ONE Persistent Disk (`/data`) already mounted — a
separate Cron Job service would need its own attachment of that same disk, which
Render doesn't support once it's already attached elsewhere. Added
`engine/m7/scheduler.py`: a daemon thread inside the existing FastAPI app (wired into
`_build_real_app()` only, not `create_app()`, so test-built fake apps never spin up a
background thread) that runs the audit daily and writes a status file
(`/data/m7-audits/last_run.json`) on the same disk the events DB already lives on.
Read-only over the event log per the audit function's own guarantee — a bad run can
never affect a live conversation.

Verified, not assumed: `engine/m7` (29 tests, 5 new) and `engine/api` (72 tests) both
pass; the actual background thread was smoke-tested end-to-end (monkeypatched
near-future "next run" time) and confirmed to fire, run the real audit, and write a
correct status file — not just unit tests of the pure helper functions.

**Pushed same day, on Mark's explicit go-ahead** ("go ahead and push it") after the
auto-mode classifier had blocked the first attempt. `main` at `46c11d63`; CI confirmed
green (run `33917613006`). **What this thread still cannot verify from here:** whether
the scheduler is actually firing in production — no Render dashboard/log access from
this session. That gap is permanent, not a "pending" item — every future sweep should
keep saying so rather than assuming success just because the code shipped.

**Discovery-UX fleet-size watch, added.** Separate, much lower-stakes relay (no
production code, no live data — just counting entries in a git-tracked YAML file):
front-end/product thread flagged that the homepage chairs/table/Atlas discovery UX
holds up fine at the current roster size, but nobody's checked whether it holds up
once the fleet grows. Mark's call: don't audit now, just watch for the fleet reaching
15 worlds and flag it then — a product/UX call, not this thread's to judge. Current
count: 7 formation-kind worlds with `state: admitted` in `records/worlds.yaml` (the
`kind: fixture` entry excluded — test-only, never shown to real users).

**Both folded into this thread's own periodic-sweep routine** (`trig_018SBnt1JTXwWkRoEfqJTZwP`)
rather than requiring a separate mechanism — steps 6 and 7 added to its standing
prompt. Neither logs anything on a routine sweep unless there's something to report
(M7: a real content-quality finding, surfaced to Mark, never judged by this thread;
fleet watch: the one-time crossing of 15, then done).

---

## 2026-09-06 — A genuine GitHub Actions infra flake, root-caused and confirmed, no
## code touched

**All 13 CI jobs failed on `main`'s tip (`a942ea5a`, merging PR #110 "Build the
idle-close writer, reporting-only")** — including jobs with nothing to do with that
PR's diff (Docker build, `Validate world-census.json`, Prose primitives). Every job
"failed" within 1-3 seconds.

**Root-caused, not assumed.** Checked each job's own detail record before touching
anything: `runner_id: 0`, no `steps` array, zero log content on every one of them
(`get_job_logs` 404'd). That signature means these jobs never got a runner allocated
at all — a GitHub Actions provisioning failure, not a repo problem. Confirmed the
commit itself touched no CI/workflow config (just Python feature code across
`engine/api` and `engine/m4`), ruling out a code-caused break before calling this
infra.

**Confirmed, not guessed, per this thread's own "a flake needs one re-run" rule:**
triggered `rerun_workflow_run` on the same commit rather than assuming. The re-run got
a real runner and came back clean (attempt 2, all 13 jobs green). No code change, no
push — the fix was that GitHub's own infrastructure recovered, this repo was never
broken.

**Next action:** none. Recorded so a future sweep seeing this exact
zero-runner/zero-log signature again recognizes it immediately rather than re-deriving
the diagnosis from scratch.

---

## 2026-09-07 — `main` now requires PRs: this thread's direct-push convention changes

**Found during routine push of the entry above.** `git push origin main` for the
infra-flake log entry (`d998c5ae`) failed: `GH013: Repository rule violations...
Changes must be made through a pull request... 11 of 11 required status checks are
expected.` Every earlier push this thread made landed directly on `main` without this
gate — this is a new branch-protection rule, not something previously missed.

Pushed the pending commit to this thread's own branch instead (succeeded, confirming
the block is `main`-specific, not a general push failure), then raised it to Mark
rather than guessing at a workaround or unilaterally opening a PR. Mark's direction:
**"go ahead and open a PR for it."**

**Opened PR #119** (`claude/cic-system-health-ln97i3` → `main`), carrying just the
`d998c5ae` tracking-doc entry — no code changes. Subscribed this thread to its
activity; will drive it to green across the 11 required checks per this thread's
normal PR-stewardship posture for PRs it creates.

**Standing-practice note:** absent a stated exception from Mark, this thread's
mechanical/non-judgmental fixes now go through a PR rather than a direct push to
`main`. The underlying bar for *what* counts as a fix this thread can push (mechanical,
non-judgmental, repo-wide) is unchanged — only the *mechanism* (PR instead of direct
push) has changed.

**Closed out.** PR #119 landed green: all 13 CI jobs passed on its final commit
(`f4e3f09d`) and GitHub reported `mergeable_state: clean`, no conflicts, no open
review threads (only bot deploy-preview comments from Netlify/Cloudflare). Asked
Mark directly whether this thread should merge its own green, mechanical-fix PRs
going forward or leave merging to him — **Mark's answer: merge them, standing
authorization, not just this one.** Merged #119 (`ac183ade`, merge commit — this
repo has squash merges disabled, so `merge_method: "merge"` was used instead) and
confirmed on `origin/main`. Unsubscribed from #119's activity and deleted the
one-hour check-in trigger, both no longer needed once merged.

**Standing-practice note, updated:** this thread now has authorization to both open
*and merge* its own PRs for mechanical/non-judgmental fixes, once all required status
checks are green and there's no merge conflict — no per-PR check-in with Mark needed
for that merge step going forward.

---

## 2026-09-10 — Same paths-filter permissions bug recurred on PR #155; two competing
## fixes for the Actions-minutes problem now open in parallel

**PR #144** (`claude/website-v2-sandbox`, Mark's own branch, still open) was this
thread's earlier fix for the Actions-minutes-exhaustion problem: a single `changes`
gating job using `dorny/paths-filter@v3`, skipping 12 engine-touching jobs + Docker
build on non-engine changes. Root cause of that job's own first failure — missing
`pull-requests: read` (the default `GITHUB_TOKEN` only grants
`contents`/`metadata`/`packages: read`, and `dorny/paths-filter@v3` calls the GitHub
API's `listFiles` on `pull_request` events, not a local diff) — diagnosed and fixed
2026-09-09 (commit `d683c9ae`), confirmed working.

**This sweep found PR #155** (`claude/ci-minutes-path-filter`, also Mark's own
account), opened independently overnight to fix the *same* Actions-minutes problem
with a *different* architecture: per-job path filters on all 13 existing jobs directly
(via the same `changes` output job), rather than one shared gate. Its own `changes`
job failed on its first CI run with the identical signature: `##[error]Resource not
accessible by integration` from the same `listFiles` call, same missing scope — no
`permissions:` block at all on that job. Confirmed via job logs before touching
anything (`GITHUB_TOKEN Permissions: Contents: read / Metadata: read / Packages:
read`, then the same error immediately after the `listFiles` invocation) — not
assumed from the title match alone.

**Fixed directly**, same pattern as #144: added an explicit `permissions: {contents:
read, pull-requests: read}` block to the `changes` job (an explicit block replaces the
default grant entirely, so `contents: read` — needed by `actions/checkout` — has to be
restated, not just the new scope). Pushed to `claude/ci-minutes-path-filter`, commit
`bf422313`. Mechanical, non-judgmental, matches the established fix for an
already-diagnosed bug — no reason to withhold it pending Mark's read on the point
below.

**Flagging to Mark, not resolving myself:** #144 and #155 are now two independent,
unmerged PRs solving the same problem with two different architectures (one shared
gating job vs. per-job filters), both touching `.github/workflows/ci.yml`, both now
CI-green at the infra level. Merging both would conflict; only one should land. Which
one to keep — and whether to close or rebase the other — is a project-lead call, not
this thread's to make unilaterally. Surfaced directly to Mark in-session rather than
guessing.

**Resolved same session.** Mark closed #144 without merging and merged #155 himself
(`bc908d16`) — #155's per-job architecture is the one kept. Also explains the
"Workers Builds: cic-project" check that failed on #155's own commit and that this
thread flagged as undiagnosable without dashboard access: Mark had suspended the
Cloudflare Workers Build integration directly, not a real build defect. **Standing
note:** this thread does not call Cloudflare directly — its check-runs and
deploy-preview comments arrive from Cloudflare's own GitHub App integration — but per
Mark's direction, treat that integration as suspended: don't chase a red or missing
Cloudflare Workers Build check as a finding in any sweep until Mark says otherwise.

---

## 2026-09-13 — Full sweep on request: every build/live/run file, not just the diff
## since last sweep

**Mark asked directly** for a full corruption/notes/comments/cost/complexity sweep of
all active files, not the routine incremental-since-last-sweep check this thread
normally runs. Scoped to four parallel read-only audits: `engine/` + `cic/engine/`
(the running Python backend), `cic-poc/frontend/` + `cic-website/` (the live UI and
site), `records/` + `canon/` + `cic/corpus-map/` (structural/parse integrity only, no
content judgment), and `World-Builds/` + `world-build-docs/` final deliverables
(document-hygiene watch, full file set this time instead of just the delta). Findings
compiled into an Artifact ("Sweep Ledger") and put to Mark directly rather than acted
on unilaterally, since most of what came back needs either his judgment call or
belongs to another thread's own domain.

**Clean, confirmed not assumed:** `engine/`+`cic/engine/` (271 files) and
`cic-poc/frontend/`+`cic-website/` — zero corruption, zero stray debug/TODO/LLM-tell
content in either. `records/`+`canon/`+`cic/corpus-map/` (1,853 files) — 0 YAML/JSON
parse failures, 0 merge-conflict markers, 0 duplicate record IDs or keys, every
worlds.yaml package pin and census_id resolves. `.github/workflows/ci.yml`,
`engine/Dockerfile`, `render.yaml`, `wrangler.jsonc` — dense with commentary but
every line explains a real constraint, nothing stray.

**Found, not yet acted on (Mark's call, per the Ledger):**
1. **134 of 143 tracked `packages/**/manifest.json` files are orphaned** (only 9 are
   pinned by worlds.yaml) — the exact accumulation pattern the repo's own .gitignore
   already documents and tells sweeps to clean up. Orphan list computed and verified.
   Tried `git rm` on all 134 — **blocked by this session's own auto-mode classifier**
   ("Irreversible Local Destruction"), not by anything about the change itself.
   Recoverable from git history regardless; not routing around the gate. Needs Mark's
   explicit go-ahead or his own `git rm` to actually clear.
2. **~50 files across Alexandria, Syriac, Donatism, and Cappadocian's Doc_01–09
   deliverables carry embedded review/revision-log narrative** — a real violation of
   CLAUDE.md's "keep the canonical surfaces clean" rule, but substantive prose in
   documents this thread didn't write and doesn't have standing to silently edit.
   Recommended routing to each world's own build-cycle thread rather than a unilateral
   strip pass.
3. **One truncated file**:
   `World-Builds/01-Post-Apostolic-House-Church/Doc09_Story_Chunks/pahcstory009_two-ways-catechumen.md`
   cuts off mid-word at EOF. This thread has no access to the real ending — flagged to
   the pahc world thread to restore, not something to guess at.
4. **cic-website/ cost/complexity bundle**: ~2MB of dead JSON data (project's own
   decision log already admits `world-census.json` isn't rendered anywhere),
   `tour.html` unreachable from site nav (confirmed, not guessed), ~3.4MB of
   byte-identical portrait images duplicated across `cic-poc/frontend/` and
   `cic-website/`, one 1.1MB image rendered at 72×72px, movement/census data
   triplicated with a documented manual-sync requirement, and shared CSS tokens
   redeclared inline on ~14 of ~20 pages instead of using the one stylesheet that
   already exists. The dead data, the unreachable page, and one duplicate helper
   function are zero-risk deletes; the image sizing, CSS architecture, and data-sync
   questions are real design calls that belong with the frontend/product thread, not
   this one.
5. **`cic/corpus-map/cyrilline-miaphysite-egyptian-christianity.yaml` vs.
   `...-tradition.yaml`** — two buckets for what the data's own note calls a
   near-duplicate census id, self-flagged as needing "a single ruling on which of the
   two carries corpus." Routed to the Library Build Engine thread, which owns
   `cic/corpus-map/`.

**Next action:** none from this thread until Mark responds to the five decisions in
the Ledger. Nothing was edited in `records/`, `canon/`, `World-Builds/`,
`world-build-docs/`, `cic-website/`, or `cic-poc/frontend/` this sweep — every finding
above is reported, not applied.

---

## 2026-09-15 — "Fix them": three of five Ledger findings closed; revision-log
## strip completed for Alexandria/Syriac/Cappadocian, with one bad first attempt
## caught and reverted before it shipped

Mark authorized fixing the outstanding Sweep Ledger findings directly ("fix them").
Findings 1, 2 (partial — see below), and 3 closed; findings 4 and 5 stayed exactly
where the Ledger left them (frontend/product-thread and Library Build Engine thread
calls respectively — not touched).

**Finding 3 (truncated file) — fixed, PR #202.**
`pahcstory009_two-ways-catechumen.md`'s citation was completed from the real vendored
source (`cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`,
Didache 5:1), not guessed — read the actual chapter text before writing the
completion.

**Finding 1 (orphaned manifests) — fixed, PR #202, with a self-caught error en
route.** Of 146 orphans (recomputed at fix time, up from the Ledger's 134),
`git rm`'d all, then CI's own `check_paths.py` gate ("Cited paths resolve; retired
paths absent") caught 22 of them as still cited by path from `Review-Artifacts/`,
decision logs, and `Open_Gaps_Tracking.md` — restored exactly those 22 from the
pre-deletion commit, re-verified locally against `tools/check_paths_baseline.txt`
before re-pushing. Net: 124 removed, 22 kept. Also retracted two findings from the
original Ledger on re-verification before acting: `world-census.json` and
`corpus-coverage.json` are live (read by `engine/m1/cross_world.py`, generated by
`cic/engine/corpus_coverage.py`), not dead data as first reported; `tour.html` is
deliberately dormant per an existing decision-log note, not an accidental orphan.

**Finding 2 (embedded revision-log narrative) — fixed for Alexandria, Syriac, and
Cappadocian; Donatism was already clean per its own thread's prior fix. PRs #203
(merged) and #205 (open).** Three parallel background agents, one per world, each
scoped to the same instruction: remove self-contained `## Revision Log`
sections and inline round-by-round review narration; leave citations, confidence
tiers, and scholarly substance untouched; flag anything ambiguous rather than guess.

**One agent's first pass on `Alexandria Doc_04_Gravity_Discovery.md` was reverted
before committing.** It crossed from deleting narrative into rewriting inline
`[Added 2026-09-09 per OG-6 §5.X...]` Open-Gap cross-reference annotations —
a real conflict with this file's own "Track gaps and exceptions explicitly" rule,
caught by reading the diff before staging, not after. `git checkout --` on that one
file; the rest of that agent's first-wave output (Alexandria's other 7 Doc files)
was clean and shipped in PR #203 alongside Syriac's first 17 files. The same agent's
second attempt at Doc_04, later in the session, was narrow and clean (one hunk,
same "corrected [date], Round N Opus review" pattern as everywhere else) — accepted.

**Every file from every agent's output was read before staging, not trusted on the
agent's own completion report.** Two specific rewritten factual claims in Syriac's
`Doc_09_Story_Inventory.md` were checked directly against the documents they now
cite (`Doc_04_Gravity_Discovery.md`'s real `## 5. Open Items Carried Forward to
Step 5` section; `Doc_07_Integrated_Ecology_Analysis.md`'s actual Papa bar
Aggai/Miles of Susa text) rather than assumed accurate — both confirmed grounded,
not invented. The full diff for both worlds was grepped for `OG-\d+` before
committing — zero gap-tracking cross-references touched. Cappadocian's one edited
Python script (`wb_cappadocian_s21.py`, which carries the same narrative inline in
WRS data-string payloads, not just comments) was re-compiled locally after editing.

**Left deliberately untouched, flagged for a dedicated follow-up pass, not
guessed at:** round-by-round review narrative that is the primary expository mode
of some body paragraphs rather than a severable aside (Syriac Doc_01 §§5.5/5.6/§6
and equivalents elsewhere); the `*_Phase*_DRAFT.md` files' deep inline narrative
beyond their own `## Revision Log` headers; `CAPPADOCIAN_BUILD_LEDGER.md` (a
build-status/gate-tracking ledger, functionally parallel to a Decision Log though
not named one — possibly mis-filed relative to `Ministry/`, relocating it is a
separate call). This is the same shape of finding as the Alexandria Doc_04
near-miss above: mechanical section-deletion is safe to run unilaterally; rewriting
prose that carries tracked scholarly or gap-tracking content is not, and needs
either a much more precise mechanical tool (exact heading-to-next-heading matching,
no freeform rewriting) or case-by-case review — not another freeform agent pass.

**Findings 4 and 5 — untouched, as the Ledger already recommended.** cic-website's
cost/complexity bundle (dead JSON, unreachable page, duplicate helper, image
sizing/CSS architecture) stays with the frontend/product thread. The
`cyrilline-miaphysite-egyptian-christianity.yaml` vs. `...-tradition.yaml`
duplicate-census-id question stays with the Library Build Engine thread.

**PR #205 merged** (Cappadocian + Syriac). **PR #206 open** (Alexandria, final
world) — drive to green/merge per standing authorization.

**Important catch during Alexandria's pass, worth generalizing beyond this
batch: not every "Corrected [date], Round N Opus review" bracket is safe to
strip, and shape alone doesn't tell you which.** `Doc_04_Gravity_Discovery.md`
carried four `[Added 2026-09-09 per OG-6 §5.X...]` annotations, structurally
identical to hundreds of other now-safely-removed brackets elsewhere in this
batch. The difference only showed up on checking `Open_Gaps_Tracking.md`
directly: **OG-6 is `Status: OPEN — awaiting project-lead disposition`**, its
own most recent line reading "Nothing was changed." Those brackets are the
live trace of an unresolved, escalated finding still waiting on Mark's
ruling — not narrative about a completed correction. Reverted a second time
(this file was already reverted once earlier in this session for the same
reason, on a first, cruder pass). **Standing rule for any future pass on this
kind of narrative:** before stripping an inline dated annotation that cites
an OG-N number, check that OG-N's own current status in
`Open_Gaps_Tracking.md` — `OPEN` means the annotation is load-bearing content
this document still needs, not log clutter; only a `RESOLVED`/closed entry
makes the annotation safe to fold into plain prose.

**Next action:** none pending from Mark on this batch. Doc_04 stays as-is
until OG-6 is disposed of — that disposition is the project lead's, per OG-6's
own "Status: OPEN — awaiting project-lead disposition" line, not this
thread's to force by picking one of its three listed options.

---

## 2026-09-15 — Collateral CI break from the repo-architecture cleanup: caught
## on PR #197, fixed at the root (PR #207) and ported into the PR it broke

A "Cited paths resolve; retired paths absent" failure arrived via this
thread's own PR subscriptions — not for a PR this thread owns, but on
**PR #197** ("lpc-doc04-round2," a Latin-Pastoral-Congregational-Christianity
content PR this thread neither opened nor was asked to drive).

**Root cause, diagnosed before touching anything:** the repo-architecture
thread's own PR #204 (merged same session) relocated
`Ministry/Technology/CiC_World_Build_Completion_Standard_V1.3.md` and
`Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_3.md` to
`reference/method/`. PR #197 branched before that move; 4 of its own new
Review-Artifacts lines still cited the old path. Not a defect in PR #197's
own content or judgment — a structural collision between two threads' work,
squarely this thread's "repo-wide, no single PR's diff caused it" mandate,
not a content call requiring escalation.

**Also found in the same pass, genuinely pre-existing on `main` itself (not
caused by #204):** `check_paths.py` run clean against `main`'s own tip
surfaced two more items — one baseline entry now resolves
(`cappadocian_Source_Registry.md`'s `reference/section-pointer` citation,
now real thanks to #204) and one newly-surfaced, permanently-legitimate
absence (`CiC_Demo_Conversation_Captures_V0_1.md` cites `.claude/launch.json`,
a real local dev config `.gitignore` deliberately keeps untracked). Neither
was PR #197's fault either.

**Fixed, both mechanical, both verified locally before pushing:**
- **PR #207** (merged, `6f2aa8f1`): `tools/check_paths_baseline.txt` —
  removed the now-resolved Cappadocian entry, added the `.claude/launch.json`
  exception. `check_paths.py --baseline` exits 0 on `main` after.
- **Pushed directly to PR #197's own branch** (`a6c48e26`, with a courtesy
  comment explaining why and pointing at #207): rewrote its 4 stale citations
  to `reference/method/...`. Verified before pushing by merging the branch
  with current `main` in a disposable local branch and re-running
  `check_paths.py` — confirmed only the (then-still-open) #207 issue
  remained, nothing PR #197-specific.

**Process note, logged so it doesn't repeat:** this thread's designated
branch is `claude/cic-system-health-ln97i3` — the #207 fix was drafted on a
fresh branch (`sys-health-baseline-cleanup`) by mistake, caught before
merging, and moved onto the designated branch via fast-forward before
opening the PR. The stray remote branch couldn't be deleted (permission
denied) and was left in place, harmless — same commit, now also on the
designated branch and in `main`.

---

## 2026-09-15 — Scheduled sweep: main's own tip broke again (Era VI/VII
## dossiers), and LPC's own review caught — and correctly didn't fix — a
## second round of the #204 collision

**`main`'s own tip failing `check_paths.py` again, unrelated to the #204
collision above.** Six new Source Readiness Dossiers landed for the
upcoming Era VI/VII (Reformation-era) build run (PR #222); four cite
`cic/corpus-map/` buckets that don't exist yet (`lollardy`,
`lutheran-wittenberg-and-its-congregations`, `the-society-of-jesus`,
`the-tridentine-church`). Checked, not assumed, that this is normal rather
than a process error: every Era 1 dossier's own corpus-map file already
exists, but the project's own `SOURCE-READINESS.md` explicitly allows a
dossier to predate its corpus-map by years. **Fixed, PR #226 (merged,
`302e95e0`):** baselined all four — one (`lutheran-wittenberg`) self-resolves
once open PR #225 merges (its own diff creates that exact file); the other
three are genuinely pending future vendoring.

**Second LPC collision from the same #204 rename, this time caught first by
LPC's own review thread, not this one.** `Doc08_Round6_Review.md` (a new
file, didn't exist during the first collision) cited the pre-#204
`Ministry/Technology/...` paths again. LPC's Round 6 reviewer independently
investigated, correctly determined **not** to silently revert or re-fix
`a6c48e26` (this thread's earlier fix), and instead reported the
discrepancy precisely: checked `ls`/`git ls-tree` across every branch it
could reach, found `Ministry/Technology/` and not `reference/method/`
everywhere, and asked "whoever owns the rename" to decide. That check was
accurate on its own terms but used the wrong frame — CI evaluates the PR's
**merge ref** (head + current `main`), not any raw branch in isolation, and
`main` has carried `reference/method/` since #204 merged. Replied on the PR
with that distinction spelled out plainly, confirmed `a6c48e26` should
stand, and fixed Round 6's own new instance (`d8471073`) — careful, on the
first pass, to touch only the live citation (line 34) and not the
historical narrative describing what `a6c48e26` renamed *from* (a
`sed`-wide replace briefly corrupted that sentence; caught in the diff
before committing, reverted precisely).

**Three more legitimate LPC citations found and baselined in the same pass
(PR #226's second commit, `ccfec047`):** `lpc_Decision_Log.md` and
`Datus_Portrait_Prompt.md` both cite a not-yet-existing portrait image and
`records/worlds.yaml` (LPC isn't registered there yet — `Datus_Portrait_Prompt.md`
says so itself, in its own words, rather than guessing a slug); and
`Doc08_Round6_Review.md`'s own narrative legitimately re-cites both old
`Ministry/Technology/` paths as historical fact describing the rename —
correct prose, not a stale reference, but `check_paths.py`'s path-matching
can't tell the difference. All three citing files are on LPC's own
still-open branch, not `main` yet — baselined proactively rather than
waiting to hit the identical gap again once that branch merges. Verified
via a disposable local merge of this thread's branch with LPC's current
branch before pushing either commit.

**Also swept clean this round:** fleet-size watch still at 9 (no change,
well under the 15 trigger); doc-hygiene grep across everything touching
`World-Builds/`, `world-build-docs/`, `cic/texts/`, `cic/corpus-map/`,
`engine/`, `records/`, `cic-website/` since the last sweep — no stray
TODO/debug/LLM-tell content, no `## Revision Log` recurrence.

**Next action:** none pending. PRs #197 and #225 will show green once they
next receive a push or a manual CI re-run — GitHub doesn't re-trigger
checks on a PR just because its base branch advanced, and forcing one
(an empty commit, a close/reopen) is against this thread's own rules.

---

## 2026-09-16 — Scheduled sweep: repo-architecture phase 2 has landed; one
## local-only false positive caught before being reported as real

**Phase 2 of the repo-architecture cleanup is now live on `main`.** 12
worlds' `World-Builds/<Name>/` and `world-build-docs/<code>/` trees have
moved into `worlds/<code>/` and `worlds/<code>/build/` respectively
(`tools/moves-phase2.tsv`). The 6 not-yet-coded Era VI/VII worlds
(Anabaptist Movements, Lollardy, Lutheran-Wittenberg, Reformed
Zurich/Geneva, Society of Jesus, Tridentine Church) correctly stay under
`World-Builds/` until each gets a registry code, per that thread's own
design shared with this one on 2026-09-15.

**Caught before reporting: a local check_paths.py failure that wasn't
real.** A fresh `main` sync locally showed `RETIRED PATH PRESENT:
World-Builds/Cappadocian`, which would have meant this thread's own
mandate territory (a genuine repo-wide break). Investigated before acting:
the only thing actually inside that directory was a stray
`__pycache__/wb_cappadocian_s21.cpython-311.pyc` — a leftover from this
thread's own `python3 -m py_compile` verification during yesterday's
Cappadocian script review, properly `.gitignore`d and never committed.
`git log` on the file showed no history; `git status` showed nothing. Not
a `main` defect — a contaminated local checkout. Deleted the stray file
and directory locally; nothing pushed, nothing to fix upstream. Logged
here only so a future sweep (by this thread or anyone) doesn't waste time
re-diagnosing the same false alarm, and as a reminder that this check
needs a clean tree to trust — a session's own prior local commands can
poison it.

**7 open PRs this round** (#236, #234, #233, #230, #229 — all new since
the last sweep, all green, newly subscribed; #225 and #197 — already
tracked, showing their pre-fix CI state from before #226/#227 merged,
unchanged since neither has received a new push). Fleet-size watch: still
9, no change. Hygiene grep across everything touching `worlds/`,
`World-Builds/`, `cic/texts/`, `cic/corpus-map/`, `engine/`, `records/`,
`cic-website/` since the last sweep — clean.

**Next action:** none pending.

---

## 2026-09-16 (later sweep) — Real finding, not this thread's to fix: PR #197
## (lpc) now shows a genuine merge conflict from the phase-2 migration, not a
## stale citation

**Not a repo-wide infra break — flagging why this thread stops here rather
than applying its usual PR #197 fix.** This sweep found PR #245 (Go-Live
Pipeline Coordinator) failing `check_paths.py` on a citation of
`World-Builds/Latin-Pastoral-Congregational-Christianity`. Before treating
this as the same mechanical "migration renamed a path, port the citation"
fix this thread already made twice today (PRs #207/#226 lineage), checked
what that citation actually documents: the Go-Live Pipeline Coordinator
thread's own standing status doc
(`Ministry/Operations/Standing/CiC_GoLive_Pipeline_Status.md`) had already
diagnosed, correctly, that **lpc now has two diverged build lines** —
`worlds/lpc/` on `main` (the older snapshot the phase-2 rename captured,
through Doc_05 only) and PR #197 itself (`lpc-doc04-round2`, still at the
old, now-retired path), which is far more advanced: Doc_04-09 disposed,
Representative construction resolved, two governance rulings adopted, none
of it on `main`. The citation is accurate, not stale — rewriting it to
`worlds/lpc/` would have pointed at the wrong, lagging copy and quietly
endorsed exactly the outcome everyone actually needs to avoid.

**Independently re-verified before accepting the other thread's report at
face value:** `mchadwick25-droid/CIC-Project#197`'s own `mergeable_state`
is genuinely `dirty` (checked directly via the GitHub API) — confirms the
finding, not just their write-up of it.

**This thread's own involvement, for the record:** earlier today this
thread pushed two small citation fixes directly to PR #197's branch
(`a6c48e26`, `d8471073`) — both were correct, narrow path-rename fixes
made before this divergence was known, and neither touches the
disposition/content work now at risk. Not reverting them; not touching
that branch again until Mark has ruled on the reconciliation, per the
Go-Live Pipeline Coordinator's own explicit "do not touch either line"
recommendation, which this thread agrees with — this is a portfolio-level
decision (which line is authoritative, whether/how to port the newer
line's commits onto `worlds/lpc/`), squarely outside this thread's mandate
and CLAUDE.md's own "cross-world or portfolio-level decision → always
ask" default.

**Left untouched, not this thread's:** PR #245's other two unresolved
citations (a forward-reference to PR #243's own not-yet-merged launch
prompt; an incomplete `engine/m1/test_cross_world.py` path missing its
`tests/` segment, inside that PR's own new `WORLDS_REGISTRY_LOG.md`
entry) — both are that PR's own content, not a repo-wide break.

**Next action:** none from this thread. Surfaced directly to Mark in
conversation rather than acted on. Everything else this sweep found was
clean (7 other open PRs all green when checked; fleet-size and hygiene
unchanged).

---

## 2026-09-16 12:35 UTC — Periodic sweep: repo-structure phase 3 landed; three PR-owned CI reds explained, none this thread's to fix

**`main`'s own tip is green.** Confirmed indirectly (no direct
check-runs-by-ref tool): PR #250's checks, evaluated against `main`'s
current tip (`3e15fcced1`), all pass — `Cited paths resolve; retired
paths absent`, `Detect changed paths`, `M9 confinement`, `M2 staleness
sweep` all green.

**Repo-structure phase 3 landed since the last sweep**
(`01ecfa50c`, "Repo structure cleanup phase 3: the D3 promotion model").
Noting for continuity: `records/worlds.yaml` (single file) is gone,
replaced by `records/worlds/<code>.yaml` (one file per world) —
`alx.yaml`, `cappadocian.yaml`, `desert.yaml`, `don.yaml`, `fix.yaml`,
`gallic.yaml`, `hal.yaml`, `ijc.yaml`, `pahc.yaml`, `syr.yaml`. No
`lpc.yaml` yet, consistent with lpc's still-unresolved diverged-build-
lines state (see previous entry). Fleet-size watch (step 7): still **9**
formation-kind admitted/built worlds (fixture excluded) — unchanged,
below the 15 threshold, nothing to log there.

**New PR found and subscribed:** `#250` ("Migrate three OG-6 corrections
from the bucket to their staging source") — green, no action needed.

**Three PRs showed red or missing CI; none is a repo-wide break, all
explained without touching that PR's own content:**

- **PR #225** (Lutheran Wittenberg vendor texts, opened by `claude[bot]`,
  single commit, untouched since 2026-09-15T17:41Z): its one CI run is
  **stale** — it ran against `main`'s tip *before* this thread's own
  Era VI/VII baseline fix (`7322f38fe`, earlier this session) landed, so
  the "3 new unresolved citations" it reports are citations this thread
  already resolved by baselining. The PR's current `mergeable_state` is
  `dirty` — ordinary staleness from sitting unpushed while ~15 hours and
  many merges passed on `main`, not a new infra break. That PR's own
  owning thread rebases when ready to merge; not this thread's to touch.
- **PR #246** (`claude/atlas-era1-prose-review`, the Atlas prose review
  thread's own large, actively-updated PR — 91 files, 73 commits,
  pushed to as recently as 06:45 UTC today): `mergeable_state: dirty`,
  zero check runs (GitHub can't compute a merge ref to check out against
  a conflicting base). That thread's own to resolve when it's ready to
  merge — not a document-hygiene finding, just conflict staleness on
  someone else's active work.
- **PR #243** (Go-Live Pipeline Coordinator launch-prompt doc, 1 file,
  `mergeable_state: clean`): genuinely **zero** CI checks or statuses
  ever registered against its head SHA (`get_status` confirms
  `total_count: 0`, state `pending`) — no failed run, just none at all.
  Doesn't reproduce on neighboring PRs created around the same time
  (#240, #241, #244 all triggered normally), so this reads as an
  isolated GitHub Actions webhook-delivery miss for this one PR, not a
  repo-wide trigger break. Not actionable from this thread without
  pushing a commit to someone else's PR, which this thread won't do;
  noted so a future sweep doesn't waste time re-diagnosing it as new.

**PR #245** and **PR #197**: unchanged from the previous entry — still
the same known LPC-divergence and forward-reference citations, still
`dirty`, still deferred to Mark. No new information this sweep.

**Document-hygiene spot-check (step 5):** grepped the last 15 non-merge
commits' diffs under `engine/`, `cic/`, `records/`, `cic-website/`,
`worlds/` for stray debug/scratch markers. The only hits were legitimate
— TODO placeholders inside a template-generating script's own output
string (intentional, for a future author to fill in) and ordinary prose
uses of "from scratch." Nothing to flag.

All other previously-open PRs (#247, #248, #244, #241, #240, #234, #233,
#230, #229) checked green.

---

## 2026-09-21 00:31 UTC — Periodic sweep: document-hygiene scrub's PR #333 closed
## out clean; four previously-untracked PRs found and subscribed; fleet size now 11

**PR #333** (the full document-hygiene scrub — `reference/`, `engine/`,
`cic/engine/`, `cic-poc/frontend/`, `records/` 134 files, `worlds/lpc`,
`worlds/gallic` 9 Doc files — plus the fleet-wide package repin it
required) merged clean this sweep: all 18 CI checks green, no blocking
reviews, `mergeable_state: clean`. Closes out the multi-entry arc this
file has been tracking since Mark's "strip all attribution" ruling.
`main`'s tip (`bb1ef7552`) confirmed green on GitHub Actions CI; the
Cloudflare Workers Build check on `main`'s own tip specifically wasn't
independently reachable this sweep (no open PR currently sits at that
exact SHA to check through) — same known tooling gap as before, not a
finding.

**Re-listed open PRs fresh (15 total, all subscribed and all CI green):**
`#225` and `#243` — both tracked as PR-owned CI issues in the previous
entry — are no longer in the open list (resolved, merged, or closed;
not independently confirmed which, not this thread's to chase). Four
PRs found genuinely new to this thread's tracking and subscribed:
`#300` (stale world-list fix in `gen_corpus_table.py`, green), `#282`
(Atlas era-break-band removal, green), `#254` and `#253` (era-spanning
homepage image sourcing, green — both disclose real, honest sourcing
gaps in their own bodies, not CI problems). `#246` (Atlas era1 prose
review) still open, still the same PR previously logged as CI-trigger-
missed; unchanged, not re-diagnosed. Every other previously-known PR
(`#250`, `#248`, `#247`, `#244`, `#240`, `#234`, `#233`, `#230`, `#229`,
`#197`) reconfirmed green.

**Document-hygiene spot-check (step 5):** read the diffs of the most
recent non-merge commits on `main` (`9321610b6`, a mechanical jsdom-
version CI fix; `a88ba7d24`, Transparency Engine Stage 3c). Both clean
— the jsdom fix is exactly the kind of repo-wide mechanical break this
thread would otherwise have picked up, already fixed directly by its
own thread. No stray notes, scratch files, or WIP commentary found.

**Fleet-size watch (step 7):** **11** formation-kind admitted/built
worlds (fixture excluded) — up from 9 at the last count, still below
the 15 threshold. No action per the routine's own instruction; logged
here only because the count changed, not as a "found something" event.

---

## 2026-09-21 06:31 UTC — Periodic sweep: PR #346's red CI is its own
## large live-merge, not a repo-wide break — flagged, not touched

**`main`'s tip** (`f98aeb390`) confirmed green on GitHub Actions CI.
Recent commits are all clean Transparency Engine work (Stage 0c through
Stage 1, plus Decision-Log entries) from its own active thread,
including two mechanical CI fixes (`d041530d7`, missing
`engine/m4/requirements.txt` install; `dff79cdec`, a `test_prose.py`
regression) already fixed directly by that thread — nothing left for
this thread to pick up.

**One new PR found and subscribed: `#346`** ("Merge who-is-at-the-table
card redesign to live"). Its own body discloses a deliberate,
hand-resolved merge of two branches diverged by 165 commits one way and
116 the other, with explicit per-world choices about which side's
`records/worlds/<code>.yaml` package pin to keep. **7 of 20 CI checks
are red** (`Cited paths resolve`, `M2 staleness sweep`, `M2 compiler
checks`, `M3 admission harness`, `M4 event log`, `Docker build`,
`engine/api tests`). Checked out the branch locally and reproduced
both root causes directly, rather than guessing from the check names:

- `check_paths.py` finds 4 new unresolved citations, at least one
  (`records/rzg/.../rzg.facilitator_brief...md` citing `worlds/rzg.yaml`)
  a pre-repo-structure-cleanup path that no longer exists post-phase-3.
- `engine.m2.cli staleness-check` reports **all 12 fleet worlds
  stale**, with large `records/`-and-`compiled/` diffs per world — the
  expected, mechanical consequence of merging two branches this
  divergent, not a new defect either side introduced alone.

**Neither reproduces on `main`'s own tip** (confirmed clean, both
checks, same session) — this is entirely caused by PR #346's own diff,
not a repo-wide break, so per this thread's own mandate it is **flagged,
not fixed**. It's also exactly the territory Mark asked the dedicated
live-site/website thread to own (2026-09-20, "I'll have the live site
audit and amp thread look at it, we are constantly working on the live
website") — a fleet-wide repin here would mean guessing at judgment
calls (which world's package pin is actually correct post-merge) that
belong to the thread doing the merge, not this one. Left entirely
untouched; local diagnostic checkout discarded without pushing
anything.

**Fleet-size watch:** still **11**, unchanged, below threshold — no log
needed on its own.

**All 15 previously-known open PRs** (`#300`, `#282`, `#254`, `#253`,
`#250`, `#248`, `#247`, `#246`, `#244`, `#240`, `#234`, `#233`, `#230`,
`#229`, `#197`) unchanged since the last sweep — no failure
notifications arrived for any of them between sweeps, consistent with
still green.

---

## 2026-09-21 — PR #346 merged directly into `live`: promotion procedure
## bypassed, flagged as an accepted exception, not unwound

**What happened:** PR #346 (previous entry, above) was merged directly into
`live` at commit `e693b048` (merged_at 2026-09-21T09:34:15Z), base `5a9938c9`.
Confirmed via the GitHub API directly, not taken on the handoff's word: the
PR's `merged_by` is `mchadwick25-droid` — the same account that authored the
PR and owns this repository — so the merge was executed by Mark's own GitHub
account. This bypassed the procedure in `CiC_Promotion_Runbook.md` in full:
no PR from `main` into `live`, no verification pass on `cic-engine-staging`
first. The runbook's own text is explicit that this is the one procedure
meant to gate everything reaching `live`: "Nothing merges to `live` directly."

**Why:** a prior session on this same thread believed `live` was the branch
Cloudflare deploys the public website (`cic-website/`) from, and merged
directly to get the who-is-at-the-table card redesign live faster. That
belief was wrong — confirmed against `README.md` and the runbook itself:
`live` drives only `cic-engine` (Render, the backend); `cic-website`
deploys via Cloudflare Workers Build, a separate pipeline the runbook
explicitly does not touch, and whose branch is a decision the runbook
says outright is "not yet made." Mark authorized and executed the direct
merge himself, aware it was going into `live` rather than through the
normal `main` → `live` path.

**Decision (Mark's, explicit, this thread):** leave `live`'s history as
committed rather than revert or unwind the merge. Log this as a flagged,
accepted exception rather than treat it as an emergency requiring
correction. The website-relevant subset of the same content was
separately brought to `main` (where Cloudflare's production deployment
actually reads from) via PR #351, opened the same day — that PR does not
fix or touch anything about this exception; it is a parallel, independent
action.

**Open, unresolved (at the time this entry was first written):** whether
`cic-engine` (Render) is actually pointed at `live` at all right now
cannot be confirmed from this sandbox — Render's dashboard is not
reachable here (egress-blocked, per the runbook's own 2026-09-15 note),
and the runbook's own one-time setup steps that would make `live` the
real production branch are dashboard-only and stated as not yet
confirmed done. Per the runbook's own caveat, `cic-engine` "keeps
deploying from whatever branch Render's dashboard already has it connected
to, almost certainly still `main`" until that setup is complete. If that
is still the case, this exception's real production impact is smaller
than the bypassed procedure would suggest — but that can only be settled
by Mark checking Render's dashboard directly, not from here. Stated as an
open unknown, not assumed either way.

---

## 2026-09-21 — Render confirmed: `cic-engine` deploys from `live`

**Closes the open question above.** Mark checked Render's dashboard
directly (this sandbox still cannot reach it) and confirmed: the
`cic-engine` service's Settings → Build & Deploy branch is set to `live`,
with a green (healthy) status at the top of the service page. The
promotion runbook's one-time setup (`CiC_Promotion_Runbook.md`'s step 2,
pointing `cic-engine` at `live` via the Render Blueprint sync) has
happened — this is no longer the "almost certainly still `main`" default
state the runbook's own caveat assumed.

Practical effect on the exception logged above: PR #346's direct merge
into `live` did reach real participant-facing production, not a branch
Render was ignoring. The exception itself is unchanged (still logged,
still not reverted, per Mark's own decision above) - this entry only
corrects the previously-open question about its actual production impact,
which is no longer smaller than the bypassed procedure would suggest.

---

## 2026-09-21 20:15 UTC — Total system check: `cic/engine` corpus-map self-test not wired into CI, 4/13 checks failing

Requested full cross-module health sweep, wider than the routine's own
7-step check. Main CI green (run 1117); fleet size unchanged at 11;
`engine/` test suite clean (769/769, 0 skips, no TODO/FIXME debt);
`staleness-check` clean across all 12 packages. One earlier-today
Decision-Log entry (Entry 13, commit `1f13808ed`, 05:45 UTC) logged a
failing run (740 passed / 6 failed / 23 errors, blamed on a "pre-existing
Stage 0c package-completeness gap") - confirmed that commit predates the
same day's Stage 4a fleet-wide package rebuild (18:51-19:22 UTC), so this
is already resolved by that later work, not a live problem.

One genuine, currently-uncaught gap found: `cic/engine/tests_corpus_map.py`
is not pytest-collected and not wired into CI at all - it only runs if
someone invokes it directly. Run directly, 4 of its ~13 checks fail:

- `tests_corpus_map.py:18` - every map filename is a census movement id
- `tests_corpus_map.py:45` - every bucket on disk is reproducible from staging
- `tests_corpus_map.py:67` - every author ruling is used by some assignment
- `tests_corpus_map.py:112` - every transmitted work has its voice assigned
  somewhere else (named orphan: "Festal Letter XXXIX (367)")

This is corpus/source-research territory (`cic/corpus-map/`), not a
repo-wide mechanical break for this thread to fix directly - flagged here,
not fixed. Whether these four are real data defects or a stale self-test
assertion is a judgment call for that thread, and separately, someone
should decide whether this file belongs in the pytest-collected suite so a
real regression here isn't silent going forward.

Everything else surveyed (Ministry workstream status, world-fleet build
stage, frontend/website, `live` branch activity) matched already-known
state - see conversation record for the full breakdown; not duplicated
here since none of it changed anything actionable.

---

## 2026-09-21 20:05 UTC — Facilitator safety-redirect mechanism: logged done (Mark's call)

Mark's direct call: the Facilitator safety mechanism is done, logged here
as of now. Worlds stay quiet and in-character; the Facilitator recognizes
a real safety event and handles the redirect itself, per the live
governing doc (`CiC_L3D_Facilitator_Governance_V3.6`) - a Representative
never handles real crisis or distress itself, and never steps out of its
world to do so.

**Scope, stated plainly so this isn't misread later:** this is the safety
half only - participant protection during a live conversation. It is NOT
Article 31 (external, human, qualified scholarly review of a world's
content accuracy), which is a separate gate, remains open fleet-wide, and
is untouched by this entry. No world's `Open_Gaps_Tracking.md` or waiver
file was changed by this entry. Raised and clarified in conversation
before logging, to avoid exactly this conflation.

---

## 2026-09-22 00:31 UTC — Periodic sweep: two red PRs flagged (both PR-specific, not fixed), 7 new PRs subscribed

Main green (run 1170). A large amount of new activity landed overnight -
the Transparency Engine's own R5-R19 rulings cycle plus Stage 4a/4b work,
and a new "Tech-Readiness" audit (dispatched from the "CiC - Tech Review &
Funding Readiness Prep" thread opened earlier this session) producing
Security and Operations hardening packages. Spot-checked the engine-
touching commits (R19 guard-scan fix, R13 holdings-check cycle start,
Stage 4b guard_proximity, Stage 4a evidence.py riders, R8/R18 copy fixes
including a CLAUDE.md confidence-vocabulary correction) - all clean,
well-documented, Decision-Log entries correctly placed, no stray notes.

7 new open PRs found and subscribed: #384, #382, #380, #379, #378, #377,
#376. Two are currently red or conflicted - both confirmed PR-specific
(reproduced/ruled out against main's own clean tip), so flagged to their
owning threads rather than fixed here:

- **PR #384** (Ministry archive housekeeping, from the Tech-Readiness
  thread): `check_paths.py` failing twice in a row. Confirmed clean on
  main's own tip - caused by this PR's own 90-file archive move leaving
  its own dangling citations, not a repo-wide break. That thread's own
  active PR to finish.
- **PR #380** (record six Transparency Engine rulings): real merge
  conflict on `Decision-Log.md` and `Rulings-Pending.md` - both append-
  only files, edited concurrently by other PRs that landed on main first
  (Entries 25-27 landed while this PR's own draft still called itself
  "Entry 25"). PR-specific content conflict on two files this thread has
  no standing to resolve on another thread's behalf.

Fleet size unchanged at 11, still below the 15 log threshold.

---

## 2026-09-23 06:31 UTC (corrected 10:15 UTC) — Periodic sweep: main's CI red, root cause is a GitHub Actions billing/spending-limit block on Mark's account, not a platform outage - needs Mark's action, not fixed by this thread

Main's tip (run 1299, PR #433's own merge, commit `8ce19c33e`) failed CI:
both `Detect changed paths` and `Cited paths resolve; retired paths
absent` died in ~2 seconds, every other job skipped as a result.

What ruled out a repo content problem (still holds):
- `check_paths.py --baseline tools/check_paths_baseline.txt` run locally
  against that exact commit: 0 new unresolved, 0 retired - genuinely
  clean. The failure isn't a real citation problem.
- Checked whether this is isolated to main: it is not. PR #430's own CI
  run (an unrelated branch, already in flight) failed the identical two
  jobs at nearly the same time. Two independent branches failing the
  same way, simultaneously, rules out a content cause specific to either
  one.
- `.github/workflows/ci.yml` has no recent changes - the last touch was
  the live-merge reconciliation, and many runs since then (through
  06:07 UTC) passed clean on this exact workflow file.

**Original diagnosis (06:31 UTC) was wrong and is corrected here, not
patched over:** this entry first read the failure as a platform-level
GitHub Actions outage, on the reasoning that both jobs died in ~2
seconds - too fast for a real scan - matching this thread's own "died
before any test body ran" flake signature, and that the identical
failure on a re-run (this thread's one permitted retry) confirmed it as
"real" rather than a flake. That reasoning ruled out *content* and
*flakiness* correctly, but never tested the actual alternative: the jobs
weren't running and failing fast, they were never dispatched to a
runner at all.

The reviewer thread "CiC — Tech Review & Funding Readiness Prep"
(session_01A2MhC3b5CFfKbX2khnWZuW) flagged this at 10:15 UTC, pointing
to GitHub's own check-run annotation on the failing "Detect changed
paths" run. That annotation URL itself was not directly readable from
here (`api.github.com` returned 403 to an unauthenticated fetch, and
this sandbox has no authenticated HTTP path to it) - so the claim was
independently re-verified against GitHub's own Actions job API rather
than taken on trust:
- Every failing job on all three affected commits (main's `8ce19c33e`,
  PR #430, and a third independent branch caught later, PR #435's
  `0e5a4119`) shows `runner_id: 0`, `runner_name: ""`,
  `runner_group_id: 0` and no `steps` array at all.
- A normal passing run on the same workflow file minutes earlier (run
  1295, main, commit `9da9bec5`) shows a real assigned runner
  (`runner_id: 1000011960`, `runner_name: "GitHub Actions 1000011960"`)
  and a full recorded step sequence (Set up job -> checkout ->
  paths-filter -> ... -> Complete job).
- That contrast - no runner ever assigned, no steps ever recorded, vs. a
  real runner and a full step trace - is the signature of a job that was
  never started, not one that ran and failed quickly. It matches exactly
  what an Actions billing/spending-limit block looks like from the API
  side, and it explains why `check_paths.py` passed locally: the script
  was never executed in CI at all, so local reproduction was silent on
  the real cause.

**Corrected root cause:** GitHub Actions is refusing to start jobs on
this account/repo because of a billing or spending-limit block (GitHub's
own account-level message: recent payments failed, or the spending limit
needs raising). This is not a GitHub platform outage, and it will not
clear on its own - it needs Mark to check the "Billing & plans" section
of the account's GitHub settings. Nothing in the repo caused this and
nothing in the repo can fix it; this thread's mechanical-fix scope
(config, CI YAML, build scripts) doesn't reach account billing.

Surfaced to Mark directly. This is currently blocking every PR from
merging to main, including this thread's own ledger PR for this entry -
CI will stay red on all branches, this one included, until the account
issue clears.

Fleet size unchanged at 11.
