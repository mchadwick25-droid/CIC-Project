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
