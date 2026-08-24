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
   that pattern found the last unreachable route for six small calls.
4. **Measured, not asserted** (spec principle 10). A number in this
   project comes from a run, not from a plausible argument. If a stage
   ends with "it should be fine", the stage is not finished.
5. **No $/token quoted until invoice-reconciled** (principle 13). Bedrock
   is partner-operated with its own pricing. Token COUNTS are measurable
   locally and are fair game; prices are not.
6. **One stage at a time, gated.** Each stage below ends with a GATE. Do
   not start the next one until the gate is met and Mark has seen it.

---

## Stage 0 - Protect the branch  *(Mark, browser, ~5 min)*

Nothing else starts until this is done. Everything below adds risk to a
tree that currently has nothing standing between it and a force-push.

**GitHub -> Settings -> Rules -> Rulesets -> New branch ruleset.**

Ruleset one, name it `protect build branches`, Enforcement **Active** (not
"Evaluate" - that is a dry-run that logs violations and permits them):

- Target branches -> Add target -> **Include by pattern** -> `build/phase-1`
- Add target again -> `main`
- Rules: **Restrict deletions**, **Block force pushes**, **Require a pull
  request before merging** (approvals **0**), **Require status checks to
  pass**

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

> **GATE 0** - a test PR opens and merges normally, and a direct push to
> `build/phase-1` is refused. Note for the assistant: the branches API
> reports `protected: false` even for a fully-ruleset-protected branch -
> that field reflects CLASSIC protection only. Do not read it as failure.

---

## Stage 1 - Make the record match reality  *(assistant, no spend)*

Housekeeping that makes every later stage legible. None of it touches code.

1. **Fast-forward `main` to `build/phase-1`.** Verified clean on
   2026-08-24: `main` is a strict ancestor, 0 commits of its own, and
   `cic-poc`, `render.yaml` and `cic-website` are byte-identical between
   them - so the deployed prototype does not change.
   `git push origin origin/build/phase-1:main`. Do NOT rename
   `build/phase-1`; renaming breaks every clone and five merged PRs
   reference it.
2. **Delete the merged branches.** ~37 of them, all fully contained. The
   command recomputes and re-verifies rather than trusting a stale list:

   ```bash
   git fetch --prune origin
   git branch -r --merged origin/build/phase-1 \
     | sed 's|origin/||' \
     | grep -vE '^\s*(build/phase-1|main|baseline/pilot-2026-08-24|HEAD)' \
     | xargs -n 12 git push origin --delete
   ```

   The `grep -vE` is load-bearing: `baseline/pilot-2026-08-24` IS merged
   and MUST survive. **A session credential may be refused (403) on
   deleting refs** - it was on 2026-08-24. If so this is Mark's, in the
   browser.

> **GATE 1** - `main` and `build/phase-1` at the same SHA; branch count
> down from 114; `baseline/pilot-2026-08-24` still at `8b23f46e`.

---

## Stage 2 - Settle the model  *(live spend - ASK FIRST)*

The old service runs `claude-sonnet-5`. The engine runs `sonnet-4-5`, and
every quality number on record was measured on 4.5. Since the new system
REPLACES the old rather than joining it, participants would otherwise be
handed an older model on raw generation than they get today.

Read `BUILD-HANDOFF.md`'s Sonnet 5 section in full before touching this.
The short version: it is not a config flip. `max_tokens=1024`
(`engine/m4/generation.py:39`) would truncate the voice, the new tokenizer
counts ~30% more tokens for identical text, and Sonnet 5 reads tuned style
directives more literally - which is a risk to the voice that **the
grounding net cannot catch**, because the net checks whether a sentence is
grounded, not whether it sounds like the world.

The comparison run: **one world, the same questions, both models**, scored
on fabricated-id rate and net coverage - the two measures with a baseline
to compare against (0.0% and 78% on 4.5). Raise `max_tokens` before the
Sonnet 5 leg or the truncation will be mistaken for a quality difference.

> **GATE 2** - a written recommendation with both sets of numbers, and
> Mark's read of the actual transcripts. Not a score alone: the thing being
> judged is whether it still sounds like the world.

---

## Stage 3 - Give the engine a container  *(assistant, no spend)*

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

## Stage 4 - Give the engine a surface  *(assistant + Mark's design eye)*

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

Repoint `render.yaml` at the engine's Dockerfile; swap `ANTHROPIC_API_KEY`
for the AWS credentials; set the region.

**The deploy branch is not recorded anywhere in this repository.**
`render.yaml` has no `branch:` key, so it was chosen in the Render dashboard
when the blueprint was connected. Find out which branch it is before Stage 1
fast-forwards `main` - it is the one fact about the deployment that is not
in git.

> **GATE 5** - the new service answers on its own URL, a full conversation
> works against it, and the event log shows a populated `gate_decision`.

---

## Stage 6 - Move the link, retire the old  *(Mark's call to fire)*

`cic-website/index.html:177` and `atlas-v3.html:570` both hardcode
`LIVE_APP_URL = 'https://cic-poc.onrender.com'`. Point them at the new
service.

Mark's ruling, 2026-08-24: **the site is not in use, so downtime during the
transfer is acceptable.** There is no cutover window to engineer.

Only after the link moves and the new service is answering does `cic-poc`
become deletable - 1,628 files, 18.6 MB. Keep whatever the new surface
actually inherited from `cic-poc/frontend`.

> **GATE 6** - churchinconversation.com reaches the new system, and the
> Anthropic Console API is no longer called by anything deployed.

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
