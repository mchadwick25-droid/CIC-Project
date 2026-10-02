# Launch prompt: finish world `lpc` under Process V2.0

This prompt starts one thread that finishes the world `lpc` (Latin Pastoral
and Congregational Christianity; world_id
`latin-pastoral-congregational-christianity`; Representative: Datus, Bishop
of the Kept Flock) to Process V2.0 standards. It sits on top of the V2.0
single-world launch prompt. Read that prompt first, with `<code>` = `lpc`.
Where this prompt differs, this prompt wins.

`Build/Ministry/Operations/Standing/Launch-Prompts/CiC_World_Build_Launch_Prompt_V2.0.md`

## Read first, in full

1. The V2.0 launch prompt above, and everything it lists under "Read first".
2. `Build/worlds/lpc/lpc_Decision_Log.md` (the ruling of 2026-09-29 is in
   `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, in the
   entry on the `lpc` re-baseline).
3. `Build/worlds/lpc/Open_Gaps_Tracking.md`. Several entries are stale. Trust
   the files on disk over the ledger, and append corrections. Never edit an
   old entry.
4. `Build/reference/L4-Templates/Handoff_Rebaseline_Declaration_Template.md`.

## What this world is, and the ruling

`lpc` was built under the earlier process. Steps 0 to 9 and the old
Representative phases 1 to 7 exist and were approved to proceed, some by the
project lead's direct instruction after more than three review rounds. About
309 records are authored. There is no registry entry and no `build/` folder.

The project lead ruled on 2026-09-29: accept the approvals `lpc` already
holds, check only what was left open, and build everything from the records
stage onward to V2.0 standards, with Doc_10 drafted fresh. Do not re-review
approved documents. Do not redraft Doc_04 wholesale: that would destabilise
Docs 05 to 09 and the records that cite it.

## Before anything else

0. Fetch `origin/main` and read the current repository state. A stale
   checkout has clobbered a review file in this world once. Check whether
   the canon-closure work (PR 557 and the related PRs) is merged. Run one
   live thread for this world.
1. Read `/usage`. Compare what is left of this week's build allocation with
   what this work needs. Stop and report if it does not fit. Ask Mark to note
   the `/usage` percent. Record it.
2. Create `Build/worlds/lpc/build/` with the state file and the cost ledger
   from their templates. Stamp Process V2.0 and Completion Standard V1.4.
3. Run `python -m engine.m10.cli handoff lpc --draft-declaration`. Write the
   result to `Build/worlds/lpc/build/lpc_Rebaseline_Declaration.md`, citing
   the decision-log entry of 2026-09-29 as the project lead's ruling. The
   declaration accepts only the pre-V2.0 approval history (round counts and
   approval wording). It accepts nothing else.

## Phase L0: no registry entry needed

Do all of this first. Each item is one targeted check or one mechanical
clean-up. None reopens an approved document.

A. Independent checks of what was left open. Opus 5.5 does each one, in a
   fresh context, at high effort. Each writes a review file with the V2.0
   header (`python -m engine.m10.cli reviewfile <file>` must pass). These are
   independent re-confirmations of carried-open findings, not new revision
   cycles. Any substantial finding you cannot close inside one round goes to
   Mark as a decision.
   - Doc_04: the findings from rounds 5 to 11 that were carried open, and
     the ruled classification of candidate 5 (Supporting, on Mark's ruling).
     Question: does any open finding change a downstream record, claim or
     gravity?
   - Doc_08: the generator findings on `scripts/gen_force_index.py` and
     `lpc_Force_Index.md` (Open_Gaps entry on the unreviewed round 8
     revision).
   - Doc_02 and `Source_Registry.md`: the review returned to independent
     review on 2026-09-13 and never came back, plus edits since.
   - Docs 03, 05, 06 and 07: list each carried-open finding and its
     disposition. Doc_07 was never built on the seven-dimension lens spine
     (Completion Standard V1.4, lens section): check what is missing.
B. Convert `Doc09_Claims_Register.md` (five columns) into
   `lpc_Claims_Register.md` (seven columns) with
   `python -m engine.m10.cli claims lpc --bootstrap`. Verify the unverified
   claims against source (133 were unverified at last count). Run
   `claims lpc` until it passes.
C. Clear process narration from the canonical files `python -m engine.m10.cli
   handoff lpc` flags (mostly `Source_Registry.md`, Doc_01, Doc_02, Step 0).
   Keep every fact. An earlier clean-up cut real content: read each cut. Move
   history to `Build/Ministry/`.
D. Leave the old review files as they are. Do not re-head them. The
   declaration covers them. Every new review file carries the V2.0 header.
E. Reconcile `Open_Gaps_Tracking.md` by appending entries that state the
   present truth (records exist; identity decided; numbering collisions).

## Stop point 1: bring Mark one package

When Phase L0 is done, stop and put these to Mark together, once, with a
recommendation on each:

1. The registry entry `records/worlds/lpc.yaml`: `census_id`, `state`, and
   `safety_adjacent` (true or false; Mark sets it, never you). Include the
   conflict: Article 29 confirmed `living_tradition_flag: true` on
   2026-09-16, while the census entry reads `living: false`. Only the m6 sync
   changes the census.
2. The Tier-3 question on `lpcstory006` (methodology question, open in
   Open_Gaps).
3. Whether the Decision Log entry is enough for Datus's identity, or the
   identity-options file must exist to match the other worlds.
4. The metered-spend ceiling for this world's lean validation set.
5. Whether `lpc` is a pilot world. If it is, Doc_10 is drafted by both
   Sonnet 5.5 and Fable and graded blind. If it is not, Fable drafts
   Doc_10 alone.
6. Whether `lpc_Decision_Log.md` (679 KB) moves to `Build/Ministry/`.

Do not create the registry entry or edit the census yourself.

## Phase L1: handoff gate

After Mark gives the registry entry: run `python -m engine.m10.cli handoff
lpc`. Every failure that is not covered by the declaration must clear. The
quote re-verification (check 8) has never run on this world: run it and fix
what it finds.

## Phase L2: finish the records to V2.0 Phase B

- The sweeps that never ran: B-1a and B-1b (the `srcLPCsearch001` records)
  and the field-bibliography sweep in Open_Gaps.
- Decision 8B: extract embedded quotes from stories, gravities, forces and
  terms. Every quote gets a verified `modern_rendering`: Opus 5.5 writes it,
  and a separate Opus pass checks it.
- The voice record: `source_anchor` with 5 to 10 `source_anchor_entries`
  (counted in the 900-word budget), and the distress-comparison guard in
  Datus's own idiom. The current `guard` was never checked against that
  rule.
- Check the 3 demonstrations against the Doc_10 craft bar: direct
  Center-Personal answer, no self-coined closing line, no repetition across
  demonstrations, audible hedges, stories told and not summarised.
- `world_front`, `facilitator_brief` and the site JSON, built and never
  waived. Each passes readability and the AI-tells read.
- Canon-cell parity, the golden set at `engine/m4/reports/bench/lpc.json`,
  the package build and pin. Run `records`, `regate` and `deployed` after
  each step.

## Phase L3: Doc_10

Doc_10 does not exist yet. The old Representative phases 1 to 7 are inputs,
not replacements. Produce the Construction Notes, the Permanent Prompt, the
Ecology Assessment, and Encounter Ecology as a short Doc_10 section
(the old phase 7 document is about 25 KB: bring it near 3,500 words). Follow
the model routing Mark sets in stop point 1. Three Opus rounds, then Mark.

## Phase L4: validation and freeze package

- The old phase 5 battery was simulated. It is not evidence. Run the full
  set again against the compiled package: all eight Part Eight categories,
  observed and labelled, one Deep Interview with the four encounter-success
  conditions on `cic-engine-staging`, and the six-question Craft/Focus
  spot-check.
- Lean is the default. Run `python -m engine.m10.cli validation lpc` for the
  trigger result. It reads `undetermined` until Mark has set
  `safety_adjacent`. Recommend full validation if the risks call for it, and
  say why and what it costs.
- Every paid run: sample first, Mark's approval, every paid setting explicit
  on the command, under the ceiling from stop point 1.
- Freeze package as in the V2.0 launch prompt. Mark decides Frozen status.

## Hazards

- Fetch first, always. Trust the disk over the ledger.
- YAML plain-scalar parser problems recur in record edits.
- Fixing Doc_04 or a shared claim can return old defects to other
  documents. Verify each correction in every copy with a separate agent.
- Numbering collisions among the canon-closure entries in Open_Gaps are still
  unresolved. Note them, do not renumber.

## Commit and push

Commit at each green checkpoint, with the step ID. Push your own branch at
each document boundary so work survives the session. Do not merge, open a
pull request, or touch `main` without Mark. Do not go live.

## Stop and ask Mark only for

The V2.0 launch prompt's list applies, plus stop point 1, plus any
substantial finding from the Phase L0 checks that one round cannot close.
