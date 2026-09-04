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
