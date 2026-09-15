# Phase 1 launch runbook

**Read this first, then `BUILD-HANDOFF.md`'s current-stage section.** That
note says what was built and why. This says what to do next, in what order,
and where to stop.

Written 2026-08-24 at the close of the build thread, at
`build/phase-1` = `9d9f2a5f`.

---

## Standing rules for this work

These are not preferences. Every one of them was earned by something going
wrong on this project, and the reasoning is in `BUILD-HANDOFF.md`.

1. **`baseline/pilot-2026-08-24` is the undo.** Frozen at `8b23f46e` - the
   exact tree behind the voice quality Mark signed off on. Every package
   manifest hash is recorded in `engine/BASELINES.md`, so a restored tree
   can be CHECKED rather than assumed. If anything in this runbook makes
   the voice worse, that branch is the way back and no argument is needed.
2. **The voice lives in `records/` and the compiled packages.** Nothing in
   this runbook should change either. If a step wants to, that is a
   decision to raise, not a step to take. Prove it with the manifest
   hashes, not with a claim.
3. **No live model spend without Mark's explicit go-ahead**, per stage,
   every time. Probe the cheap gate alone before spending a full turn -
   that pattern found the last unreachable route for six small calls. As
   of 2026-08-24 **there is no paid stage left on the path to a running
   pilot** (Stage 2 is deferred by decision), so any request to spend is a
   departure from this plan and needs saying out loud as one.
4. **Measured, not asserted** (spec principle 10). A number in this
   project comes from a run, not from a plausible argument. If a stage
   ends with "it should be fine", the stage is not finished. This applies
   to git as much as to models: on 2026-08-24 two clones ran the same
   `git branch --merged` against the same commit and disagreed by 17
   branches holding thousands of commits. **A command that is usually
   right is not a check.** Before anything destructive, verify each item
   individually and say what the verification actually returned.
5. **No $/token quoted until invoice-reconciled** (principle 13). Bedrock
   is partner-operated with its own pricing. Token COUNTS are measurable
   locally and are fair game; prices are not.
6. **One stage at a time, gated.** Each stage below ends with a GATE. Do
   not start the next one until the gate is met and Mark has seen it.
7. **Mark runs Windows PowerShell.** Any command handed to him to run
   himself must be PowerShell, not bash - no `sed`/`grep`/`xargs`, and `\`
   is not a line continuation there. This cost a round trip on 2026-08-24.
   Commands the assistant runs in its own session are a different matter;
   that container is Linux.

---

## Stage 0 - Protect the branch  *(Mark, browser, ~5 min)*

**READ THIS FIRST - 2026-08-24: rulesets are not available on this
repository.** They are free on public repos and a paid plan on private
ones, and GitHub asks for Team. Do not buy Team over this yet; read
"Protection without rulesets" below, which is what was actually done, then
come back to the ruleset recipe if and when the plan changes.

### Protection without rulesets - what was actually done

Two corrections to how this was framed while the build was closing, both
checked rather than argued:

**The baseline was never the fragile thing.** `8b23f46e` is an ANCESTOR of
`build/phase-1`, so `baseline/pilot-2026-08-24` is a convenience label, not
the only ref holding that commit. Delete the branch, move it, lose it - the
tree is still reachable from `build/phase-1`'s history, and
`engine/BASELINES.md` records the SHA. `git checkout 8b23f46e` works
regardless.

**The single point of failure was `build/phase-1` itself**, which was the
only ref holding 366 commits. **Fixed 2026-08-24 by fast-forwarding `main`
to it** - two refs now hold the same history, and a force-push over either
leaves the other intact. Redundancy, not permission. It is free, it needed
no plan upgrade, and it buys more than half of what the ruleset would have.

A local `git clone` on Mark's own machine is a third copy and costs
nothing.

**What is genuinely given up, stated plainly rather than glossed:**
CI-green-before-merge is a DISCIPLINE here, not a gate. It was held on ten
pull requests on 2026-08-24 by choice, and a future session could merge
red. The standing rules at the top of this file are the only thing holding
it. That is weaker than enforcement and it is an accepted cost, not a
solved problem.

**When to revisit Team:** the moment there is a second contributor.
Enforcement earns its price when discipline stops scaling past one
practitioner - not before.

### The ruleset recipe, for when the plan allows it

Everything below is verified against the actual GitHub form as of
2026-08-24, including the sub-options, and is worth keeping because getting
it wrong locks the assistant out of the repository.

**GitHub -> Settings -> Rules -> Rulesets -> New branch ruleset.**

Ruleset one, name it `protect build branches`, Enforcement **Active** (not
"Evaluate" - that is a dry-run that logs violations and permits them):

- Target branches -> Add target -> **Include by pattern** -> `build/phase-1`
- Add target again -> `main`
- Rules: **Restrict deletions**, **Block force pushes**, **Require a pull
  request before merging**, **Require status checks to pass**

Sub-options under "Require a pull request", all of which appear only after
ticking it:

| Sub-option | Set to | Why |
|---|---|---|
| Required approvals | **0** | Anything >= 1 and every merge waits for Mark |
| Require approval of the most recent reviewable push | **off** | Demands approval from someone OTHER than the pusher - unmeetable on a solo repo even at 0 approvals |
| Allowed merge methods | **include Merge** | Every merge in this repo is a merge commit; disabling it breaks the workflow the same way "Require linear history" does |
| Dismiss stale approvals / specific teams / Copilot approval / conversation resolution | off | Nothing to dismiss at 0 approvals, no teams, no Copilot; conversation resolution turns any bot comment into a merge blocker |

Sub-option under "Require status checks":

| Sub-option | Set to | Why |
|---|---|---|
| Require branches to be up to date before merging | **off** | Forces every open PR to be updated to the latest base before merging. Ten PRs merged sequentially on 2026-08-24 would each have forced a rebase of all the others. Churn, no safety gain for a solo repo |
| Do not require status checks on creation | off | No effect unless "Restrict creations" is ticked, which it is not |

The twelve current check names:

```
M1 gate battery selftest (fixture world)
M2 compiler checks (determinism, stub loader)
M2 staleness sweep (built/admitted/open worlds)
M3 admission harness (mock, fixture world)
M4 event log, projection, entrance seal, resume, turn loop
M5 Facilitator gate routing + failure semantics
M8 cost & observability unit tests (mocked, no live AWS call)
engine/api tests (mocked Bedrock, fixture world)
Docker build (engine/Dockerfile)
Prose primitives (shared measurement)
Provider seam unit tests (mocked, no live AWS call)
Canon v1 + sealed probe isolation
Validate world-census.json
```

Ruleset two, `freeze baselines`, target `baseline/*`: **Restrict updates**,
**Restrict deletions**, **Block force pushes**. Nothing else - nothing ever
merges into a baseline.

**Do NOT tick**, on either ruleset:

| Rule | Why not |
|---|---|
| Restrict updates *(on ruleset one)* | Blocks all pushes including PR merges. Work stops. |
| Require signed commits | Claude's commits are unsigned. Locks the assistant out entirely. |
| Require linear history | Every merge in this repo is a merge commit. Forces squash/rebase from here on - a real workflow change, not a safety setting. |

Leave the **bypass list empty**. Adding yourself makes the whole thing
advisory, and the force-push it would permit is exactly what the baseline
needs protecting from.

**Two check names were REMOVED from CI on 2026-08-24** - "Repository views
current (all six worlds)" and "Frontend build (tsc + vite build)". If an
earlier attempt added them as required checks, take them out. A required
check whose job no longer exists never reports, and every pull request
waits on it forever with no error to read.

> **GATE 0 (rulesets unavailable, the actual 2026-08-24 state)** - `main`
> and `build/phase-1` at the same SHA, so two refs hold the history; the
> standing rules at the top of this file read and understood; and everyone
> touching this repository aware that CI-green-before-merge is a promise
> rather than a wall.
>
> **GATE 0 (if rulesets become available)** - a test PR opens and merges
> normally, and a direct push to `build/phase-1` is refused. Note for the
> assistant: the branches API reports `protected: false` even for a
> fully-ruleset-protected branch - that field reflects CLASSIC protection
> only. Do not read it as failure, as this session nearly did.

---

## Stage 1 - Make the record match reality  *(assistant, no spend)*

Housekeeping that makes every later stage legible. None of it touches code.

1. ~~**Fast-forward `main` to `build/phase-1`.**~~ **DONE 2026-08-24** -
   both at `50c4db23`. This turned out to be the protective step, not
   housekeeping (see Stage 0), so it was pulled forward. Verified clean
   before pushing: `main` was a strict ancestor with 0 commits of its own,
   and `cic-poc`, `render.yaml` and `cic-website` were byte-identical
   between the two, so the deployed prototype did not change. `build/phase-1`
   was deliberately NOT renamed - renaming breaks every clone, and several
   merged PRs reference it.
2. ~~**Delete the merged branches.**~~ **DONE 2026-08-24** - 120 remote
   branches down to 76. Kept here in full because the procedure nearly went
   wrong, and the reason it nearly went wrong is not obvious.

   **`--merged` IS NOT A SAFETY CHECK. Verify every branch individually
   before deleting it.**

   What happened: `git branch -r --merged origin/build/phase-1` was run in
   the assistant's Linux container and in Mark's Windows clone, against the
   same target commit, with the same branch SHAs. The container listed 44
   branches. Mark's clone listed 61. **The extra 17 were not merged** -
   `claude/confirmed-gloss-color` alone was 516 commits ahead,
   `claude/v8-v9-charter-lblaxp` 672, `claude/rollback-to-fable-base` 520.
   Deleting them would have destroyed several thousand commits that exist
   nowhere else in the repository.

   The cause was never established. Both clones agreed on
   `origin/claude/confirmed-gloss-color = f85ba6de` and disagreed only on
   whether it was reachable. **That is the point: the cause does not need
   to be known for the procedure to be safe, as long as the procedure does
   not trust one command's word for it.** What caught it was the count not
   matching an earlier count - not the process.

   ### The procedure

   **Step 1 - the assistant builds the list AND verifies each entry**, in
   its own session, and does not hand over a command that recomputes on a
   machine whose answers have not been checked:

   ```bash
   git fetch --prune origin
   KEEP='^(build/phase-1|main|baseline/pilot-2026-08-24)$'
   git branch -r --merged origin/build/phase-1 | grep -v HEAD \
     | sed 's|^ *origin/||' | grep -vE "$KEEP" | sort > /tmp/candidates.txt

   # THE CHECK THAT MATTERS - every candidate, individually
   while read b; do
     n=$(git rev-list --count origin/build/phase-1..origin/$b)
     [ "$n" != "0" ] && echo "REJECT $b ($n commits not contained)"
   done < /tmp/candidates.txt
   ```

   A branch that prints REJECT does not go in the list, whatever `--merged`
   said. If any print, say so plainly rather than quietly dropping them -
   a disagreement between the two is itself the finding.

   **Step 2 - hand over an EXPLICIT list**, as a literal array, not a
   command that rebuilds it:

   ```powershell
   $safe = @('branch-one','branch-two', ...)
   $safe.Count
   foreach ($b in $safe) { git push origin --delete $b }
   ```

   One at a time in the loop, so a failure names the branch that caused it.
   Mark runs Windows PowerShell (standing rule 7) - do not hand him bash.

   **Step 3 - verify the outcome from the assistant's side**: the branch
   count fell by exactly the number deleted; `build/phase-1`, `main` and
   `baseline/pilot-2026-08-24` still resolve; and every branch that was
   REJECTED or excluded still exists.

   ### Two things that stay true

   **The keep-list is load-bearing.** `baseline/pilot-2026-08-24` IS merged
   and any naive sweep takes it.

   **A mistake is recoverable.** Every deleted branch was fully contained,
   so its commits survive in `build/phase-1` and the branch can be
   recreated at its SHA. That is exactly why the individual check matters:
   it is what makes "fully contained" true rather than assumed.

   **A session credential may be refused (403) on deleting refs** - it was
   on 2026-08-24, retried and refused again, which is why the deletion ran
   from Mark's own shell. The GitHub UI at
   `github.com/mchadwick25-droid/CIC-Project/branches` -> Stale has a bin
   icon per row if no shell is available.

> **GATE 1 - MET 2026-08-24.** `main` and `build/phase-1` both at
> `417f3211`; remote branches 120 -> 76; `baseline/pilot-2026-08-24` still
> at `8b23f46e`; and all 18 unmerged branches confirmed still present *(count correct on 2026-08-24; by 2026-08-28 the remote held 87 branches, ~81 unmerged — the per-branch-verification rule stands, the numbers do not; see the foundation audit)*.
>
> Note for whoever keeps this level: **the `main` fast-forward is now
> protection, not housekeeping** (Stage 0). If a later merge lands on
> `build/phase-1` and `main` is not brought level, the redundancy quietly
> decays back to a single ref holding everything.

---

## Stage 2 - Settle the model  *(DEFERRED - do not run this)*

**Mark's decision, 2026-08-24: the pilot runs on `sonnet-4-5`. Do not
spend on a comparison run. Revisit only if the pilot shows a quality
problem.**

The reasoning, because a later thread will be tempted to reopen it: every
quality number on record - 0.0% fabricated ids, 78% net coverage - was
measured on 4.5. **Shipping 4.5 ships the thing that was actually
measured.** Switching first would launch on a configuration nobody has
evidence for, and pay for the privilege. A pilot is itself the
measurement: if the voice holds up with real participants the question
closes for nothing, and if it does not there will be transcripts to point
at rather than a score.

This removes the only paid stage from the path to a running pilot.
Everything from Stage 3 onward is engineering that costs nothing but time.

### If the pilot does show a quality problem

Diagnose before reaching for the model. A participant who says it feels
worse than the old site is comparing **4.5 with grounding** against
**Sonnet 5 with no grounding and no records** - two systems differing in
far more than their model. The model is one candidate cause among several,
and the cheaper ones (the Facilitator's placeholder text, a thin world,
retrieval missing the right record) should be ruled out first.

If it really is the model, `BUILD-HANDOFF.md`'s Sonnet 5 section has the
blockers in full. In short: **raise `max_tokens` first**
(`engine/m4/generation.py:39` is tuned for 4.5 prose, adaptive thinking is
on by default on Sonnet 5, and the new tokenizer needs ~30% more tokens
for the same text - truncation would otherwise be read as a quality
difference). Then the comparison: one world, the same questions, both
models, scored on fabricated-id rate and net coverage, which are the two
measures with a 4.5 baseline to compare against.

Note that Sonnet 5 reads tuned style directives more literally, and **the
grounding net cannot catch that** - the net checks whether a sentence is
grounded, not whether it sounds like the world. Only Mark reading the
transcripts settles that part.

> **GATE 2 - CLOSED BY DECISION, not by a run.** Nothing to produce. The
> pilot proceeds on 4.5.

---

## Stage 3 - Give the engine a container  *(assistant, no spend)*  -  **DONE 2026-08-25** *(marked 2026-08-28: `engine/Dockerfile` exists, CI's docker-build job builds it, and it is the deployed image — this stage's own prose below predates completion)*

There is no `engine/Dockerfile`. `render.yaml` builds `cic-poc/Dockerfile`
and nothing else.

Needs: the five `engine/*/requirements.txt` files, the compiled packages
(rebuilt from `records/` at build time, verified against the manifest
hashes in `records/worlds.yaml` - a build that does not reproduce them is
not this system), and `uvicorn` serving `engine.api.app`.

Credentials change shape here: `ANTHROPIC_API_KEY` becomes AWS credentials
for Bedrock. `cic-bedrock-dev` is a DEV identity - production wants its own,
scoped to Bedrock invoke on the models actually used.

> **GATE 3** - the container builds, `/health` answers, and one live turn
> against the fixture world returns a grounded answer. Verify the package
> hashes inside the built image match `records/worlds.yaml`.

---

## Stage 4 - Give the engine a surface  *(assistant + Mark's design eye)*  -  **DONE 2026-08-25** *(marked 2026-08-28: the surface ships inside the engine image and has since grown the launch system and Table room — see the decision log)*

`engine/api` is four HTTP endpoints and no UI. The only participant-facing
surface anywhere in this repository is `cic-poc/frontend` - **48 files**,
built for this exact product and conversation shape.

Salvage it deliberately. It speaks to the old backend's API, so the work is
repointing it at `engine/api`'s four endpoints and dropping whatever the old
system had that the engine does not.

Two things that are Mark's, not the assistant's:

- **Stage 7.5 (experience design) is still Mark's own pass.** "No surface
  code before approval" has held all build long. It still holds.
- **The Facilitator's words.** `engine/m4/facilitator_turns.py` says in its
  own CRAFT NOTE that its strings are placeholders and NOT Mark-approved
  participant-facing text. Five of the seven routes speak them. A
  participant asking "am I talking to an AI?" currently gets an
  assistant's prose. **This is the largest open quality gap in the runtime
  and no amount of code closes it.**

> **GATE 4** - a conversation held end to end through the real surface, read
> by Mark, with the Facilitator speaking his words rather than placeholders.

---

## Stage 5 - Deploy  *(Mark holds the dashboard)*

~~Repoint `render.yaml` at the engine's Dockerfile; swap `ANTHROPIC_API_KEY`
for the AWS credentials; set the region.~~ **DONE 2026-08-25, as a SECOND
service, not a repoint** - PR #52 added `cic-engine` to `render.yaml`
alongside the existing `cic-poc` entry, left untouched, rather than
replacing it in place. `engine/Dockerfile` gained a Node build stage for
`cic-poc/frontend`; `engine/api/app.py` serves the built `dist/` same-
origin (Mark's call, 2026-08-24: one service, not two, so no
`CORS_ORIGINS`). `CIC_API_REGION=us-east-1` is in the blueprint directly;
`AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY` are `sync: false`, set by hand
in the Render dashboard.

~~**The deploy branch is not recorded anywhere in this repository.**~~
**CONFIRMED 2026-08-25, directly in the Render dashboard: `main`.** The
existing Blueprint ("Church In Conversation") already tracked it.

One real snag on the way, worth keeping: the Blueprint's first sync
created `cic-engine` and deployed it before AWS credentials existed,
so it crashed on startup (`engine/api/app.py` resolves the Bedrock model
ID at import time, a real control-plane call - no credentials, no boot).
Fixed by setting the two env vars and using Manual Deploy to retry, not a
second Blueprint sync. The Blueprint's own sync status stayed "Failed
sync" afterward even with both services showing green/deployed - a Render
UI quirk, not a real problem; chased once, confirmed cosmetic, left alone.

> **GATE 5 - MET 2026-08-25.** `cic-engine` answers on its own URL
> (`/health` -> `{"status":"ok"}`), and a full conversation ran against it
> for real: asking Theon "who was Jesus" returned a live, grounded answer
> with five citation marks, correctly labeled ("Theon - Alexandrian
> Christianity") and served through the real production surface (session
> code banner, no placeholder text). `gate_decision` is written and
> validated before anything else in `engine/api/wiring.py`'s
> `handle_message` on every successful call, so a real answer is proof
> enough without a direct database read.

---

## Stage 6 - Move the link, retire the old  *(Mark's call to fire)*  -  **DONE 2026-08-25**

~~`cic-website/index.html:177` and `atlas-v3.html:570` both hardcode
`LIVE_APP_URL = 'https://cic-poc.onrender.com'`. Point them at the new
service.~~ **DONE** - PR #54. Both now point at `cic-engine`; the site's own
`?worlds=<census_id>` deep links (`records/worlds.yaml`'s own `census_id`
field, same one `cic-website/data/world-census.json` uses) now land a
visitor straight on that world's doorway rather than the world list, so
"Launch an Interview with Theon" still does exactly that. A known,
flagged-not-fixed cost: `atlas-v3.html`'s multi-select "table" tray can
still send several ids at once; the new engine seats one world per session
(spec O9), so only the first now survives - that tray affordance is
quietly stale, not redesigned by this stage.

Mark's ruling, 2026-08-24: **the site is not in use, so downtime during the
transfer is acceptable.** There is no cutover window to engineer.

Only after the link moves and the new service is answering does `cic-poc`
become deletable - 1,628 files, 18.6 MB. Keep whatever the new surface
actually inherited from `cic-poc/frontend`. ~~**Not done yet, deliberately**:
`cic-poc`'s Render service is SUSPENDED (2026-08-25, Mark, dashboard), not
deleted - suspending was the ask this gate actually needed (stop the
Anthropic API calls), and deletion is its own later decision, still open.~~
**Deletion decided 2026-08-28** - Mark: "yes we can retire the old
systems." Done in-repo the same day: `cic-poc/backend`, `docs`,
`Dockerfile`, and the setup guides removed (`frontend/` kept - it is the
surface cic-engine builds and serves); the cic-poc service entry removed
from `render.yaml`. The Anthropic keys were disabled by Mark the same
day (2026-08-28; the account's remaining credit is his to spend on
another, non-CiC project) - so all CiC model spend now flows through AWS
Bedrock alone. What remains is one action: Mark's dashboard confirmation
when Render's Blueprint sync flags the suspended service for deletion.
The old pilot's transcripts live in Supabase, untouched by any of this.

> **GATE 6 - MET 2026-08-25.** churchinconversation.com's links reach
> `cic-engine` (PR #54), and `cic-poc` is suspended in the Render dashboard
> - no deployed service can call the Anthropic Console API anymore.

---

## What is NOT in this runbook, deliberately

- **The Track B threshold.** The accumulator writes now and decides
  nothing. Its proposed threshold says of itself "proposed, not validated
  ... calibration work for live testing rather than a claimed-correct
  number". Let the writer gather a real distribution first.
- **`retrieval_surfaced`.** Declared, folded, written by nothing - but
  session exclusion already works without it (`already_told_ids` derives
  from citations). Polish, not a gap.
- **The ~45 unmerged feature branches.** Most are hundreds of commits
  divergent, from threads predating the redesign. Merging them wholesale
  would put `records/` and the compiled prompts back in play, which rule 2
  forbids. That is per-branch triage - *what capability do I actually want
  from this?* - and for the old ones, likely a rebuild against the current
  engine rather than a merge.
- **`engine/m1/gates_experimental.py`.** 295 lines, no caller anywhere,
  and deliberately kept: it carries two superseded gate ancestors with the
  reasoning for why each failed. Do not "clean" it up.
