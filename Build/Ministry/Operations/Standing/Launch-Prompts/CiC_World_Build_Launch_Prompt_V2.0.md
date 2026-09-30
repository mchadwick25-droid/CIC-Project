# Launch prompt: World Build under Process V2.0, world `<code>`

Replace `<code>` with the world's registry code before use. This prompt
starts one world's build, from the Library handoff to a drafted freeze
package. Go-live is a separate thread.

## Read first, in full

1. `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`
2. `CLAUDE.md`
3. `Build/reference/method/CiC_World_Build_Completion_Standard_V1.4.md`
4. `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`
   and `Build/reference/L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`.
   Both are .docx files. Read `word/document.xml` from the zip.
5. `Build/reference/method/CiC_Register_Bar_2026-08-29.md`
6. `Build/reference/method/CiC_Representative_Naming_Role_Discipline_2026-09-08.md`
7. `Build/reference/method/CiC_Adversarial_Review_Standard_Practice.md`
8. The handoff manifest: `Build/worlds/<code>/build/<code>_Handoff_Manifest.md`
9. The world's `Open_Gaps_Tracking.md` at `Build/worlds/<code>/`
10. The six build skills at `Build/reference/method/skills/`. Start with
    `cic-build-cycle/SKILL.md`, then read the skill for the document at hand.

## Task

Build world `<code>` from handoff to freeze, one document at a time,
under Process V2.0. Draft, review, revise, then approve to proceed. Use
the templates in `Build/reference/L4-Templates/` and never fork a copy.

## Before any drafting

0. Fetch `origin/main` and read the current repository state before judging
   what exists. Look for a prior partial build of this world: unmerged
   branches, `Archive/` and older folders such as `Build/World-Builds/`. If
   one exists, recover and audit it. Do not start fresh over it. Run one live
   thread for this world.
1. Read `/usage`. Compare what is left of this week's build allocation
   with the pilot-measured cost of a typical world plus a reserve. If it
   does not cover both, stop and report. The weekly allowance resets
   Friday at 2:00 pm, Mark's time.
2. Ask Mark to note the `/usage` percent. Record it in the cost ledger.
3. Stamp the process version (`V2.0`) in the state file.
4. Create the state file and the cost ledger from their templates:
   - `Build/reference/L4-Templates/World_Build_State_File_Template.yaml`
     becomes `Build/worlds/<code>/build/<code>_Build_State.yaml`
   - `Build/reference/L4-Templates/World_Build_Cost_Ledger_Template.md`
     becomes `Build/worlds/<code>/build/<code>_Cost_Ledger.md`
5. Run the handoff gate:
   `python -m engine.m10.cli handoff <code>`
   If any check fails, stop. Send the world back to the source-research
   thread. Check 1 fails until `records/worlds/<code>.yaml` carries
   `safety_adjacent: true` or `safety_adjacent: false`. Mark sets it at
   handoff, and a world cannot start without it. Never set it yourself.
6. If the metered ceiling for this world is still a placeholder, do not
   start any paid run. Log it as an open item and ask Mark for the number
   when the first paid run is due.

## State file

The state file is the only record of where the world stands. Update it at
every step change and every review round. On a new session, read it
first, then re-run the last gate before new work. The world must be able
to stop at any document boundary and resume after the Friday reset.

## Document sequence

Steps 3 to 10 follow Process V2.0. Do not start the next document until
the current one is approved to proceed.

## Model routing

- Sonnet 5.5 (`claude-sonnet-5-5`) drafts every document except Doc_04
  and Doc_10. It also handles orchestration and mechanical work.
- Fable 5.1 drafts Doc_04 and Doc_10 only. It also diagnoses failures in
  validation.
- In a pilot world, Sonnet 5.5 and Fable each draft Doc_10. Opus 5.5
  grades the two blind on Rigor, Accessibility, Craft and Focus. Record
  the grading in the cost ledger. Follow
  `Build/reference/method/CiC_Pilot_Protocol_V2.0.md` for the blinding,
  grading and decision rule.
- Opus 5.5 (`claude-opus-5-5`) runs every review round and every blind
  grading. It writes every `modern_rendering`. A separate Opus pass checks
  each rendering.
- The reviewer is never the drafter.

## Gate layer

Run each command before Opus sees the work. Fix every failure first.

- `python -m engine.m10.cli handoff <code>` at the start of the world.
- `python -m engine.m10.cli prereview <code> --doc N` before every review
  round. `N` is the document number.
- `python -m engine.m10.cli roundcount <code> N --check-new` before any new
  review file is written (`N` is `0` for Step 0). With three review files on
  record it exits non-zero, and the document goes to Mark. Without
  `--check-new` it fails only once a fourth file exists.
- `python -m engine.m10.cli reviewfile <path>` on every review file.
- `python -m engine.m10.cli gaps <code>` after every review file.
- `python -m engine.m10.cli citations <code>` on every document and probe
  file.
- `python -m engine.m10.cli claims <code>` before every review round on a
  document that carries claims. It halts on an unregistered absence or
  exclusivity claim and on a stale register entry.
- `python -m engine.m10.cli records <code>` after every records edit, and
  `records <code> --freeze` at freeze.
- `python -m engine.m10.cli regate <code>` after any edit. It re-runs
  readability and word budgets on every changed field and every
  public-facing field.
- `python -m engine.m10.cli deployed <code>` after each deploy. It also
  checks that the approved-source anchoring paragraph is in the compiled
  prompt.
- `python -m engine.m10.cli probes <code>` before and after every probe
  run. It fails a results file whose tested pin is not the current pin.
- `python -m engine.m10.cli validation <code>` after the probe results
  are in. It also checks that all eight Part Eight categories were run, that
  the Deep Interview carries its encounter-success grading, and that
  validation ran on the current package pin.
- `python -m engine.m10.cli wiring <code>` at the Representative freeze.
- `python -m engine.m10.cli integrity <code>` at freeze. It checks open
  items, unmarked superseded files, stated record counts, and that `deployed`
  passes at the pinned package. The reviewer reads the rest.
- `python -m engine.m2.cli profile <code>` to generate the World Profile on demand. It is not part of the package, and no check covers it.

A new world gets no waivers. Any exception needs an owning finding and
Mark's approval.

## Review discipline

- Opus 5.5 reviews every round. Round 1 runs at high effort. Rounds 2
  and 3 are targeted rechecks at medium effort. They check only what
  changed, against the prior findings.
- The first line of every agent-run review file reads: "Simulated review —
  informational only, not an Article 31 substitute."
- Every round records a truncation check by two independent methods.
- Re-verify every quote against the vendored file, speaker included.
  Re-verify every high finding yourself against source before you apply a
  fix.
- A blocking finding is never dismissed by self-certification. It needs
  independent re-confirmation.
- Confirm every cited passage by its structural marker in the vendored file
  (a `div` title or a chapter heading). A single search hit is a lead, not a
  confirmation.
- A correction that changes a claim is verified by a separate agent, against
  the source, and that agent sweeps outward through every copy of the claim.
- Make no structural edit to a tree while a review of that tree is running.
- Record every decision with the real alternatives considered and why the
  chosen one is the most defensible.
- The bar is what a church history scholar would call good. A finding
  that a document could be stronger, with nothing wrong, unsupported or
  misleading, is not substantial. It does not justify another round.
- A document gets three rounds of substantial revision. If it has not
  cleared by then, stop and send it to Mark. Do not run a fourth round.
- Say "Approved to proceed." Never say "finalized."
- Every open item in a review or phase document gets an entry in
  `Open_Gaps_Tracking.md`. Entries are append-only.
- A document proceeding does not close anything. Only Mark closes a
  world, and only after Phase Five boundary testing and full-system
  review.

## Fabrication and voice

- Invent nothing. A Representative has no family, age, personal history
  or anecdote beyond what the completed world supports.
- Public-facing text must pass readability (Flesch-Kincaid grade 8 to 10,
  Flesch Reading Ease 60 or higher). Read every such field for AI tells
  against `records/syr/demonstration/syr.demo.room-for-doubt.md`.
- The Representative never handles real distress. The Facilitator
  redirects. Never make a redirect depend on the participant confirming
  they are fine.
- Label every probe result observed (with a transcript reference) or
  authored. An authored result never scores PASS or FAIL.
- Test `packages/<code>/<pin>/compiled/prompt.txt` only.
- The Representative speaks only from the world's perspective, as the
  world, in the first person plural ("we," "our"). It never says "this
  world" or "it" about its own community. The `voice-perspective` gate in
  `engine/m1/gates.py` checks it, and every example you write follows it.
- Right answers first, generated correctly. Grade the first generated
  answer. A regenerated, retried or revised answer never counts as a
  pass. Fix a defect found in testing at its source (the record, the
  prompt, the guard or the retrieval), never by a later rewriting step.
  Runtime self-revision, where it exists, is not credited to the world's
  answer quality.

## Paid runs

Live interviews, blind probes and any text-to-speech spend real money.
Before each paid run:

1. Run a small sample and show it to Mark. Get his approval.
2. Pass every paid setting explicitly on the command line. Never inherit
   from the environment.
3. Let the run print its settings with item and character counts.
   Confirm them from that printed output before you call the run valid.
4. Stay under the world's metered ceiling. Record the dollars in Ledger 2.

## Ledger entries

Write an entry in the cost ledger at each document boundary and at
freeze. Record tokens by model tier, hours, and the model and effort level
for each document and each review round. Ask Mark to note the `/usage`
percent before and after each entry, and at freeze. Stamp the Completion
Standard version in the state file at world start. Session cost telemetry shows
raw-rate equivalents. It is not a bill.

## Halt, never thin

A budget number never thins the work. If staying inside a number would mean
shipping work below the bar, stop at the last green checkpoint. Put the
choice to Mark in allowance percent and dollars. Running out is never a
licence to rush.

If lean validation looks too thin for this world's risks, recommend full
validation to Mark, with the reason and the cost. You may raise what the code
triggers and never lower it.

## Pause rule

Pause only at a document boundary. Before pausing, update the state
file, write the ledger entry, and record the pause point. Put heavy
steps (Opus review rounds, Fable drafts) early in the weekly window.

## Stop and ask Mark only for

- The metered ceiling number, or a paid run that would pass it.
- A budget number that would thin the work.
- A missing input you cannot supply or derive yourself.
- The pilot world choices.
- The Representative's identity and title. Offer 2 to 4 named candidates
  with trade-offs and one recommendation, all checked against the naming
  discipline document. Ask for identity and image together, once.
- Any cross-world or portfolio decision.
- Any governance or methodology change not already decided in Process
  V2.0. Route a framework or template gap as a flagged finding.
- An unresolved tension after three review rounds.
- Frozen status. Never assign it yourself.

Do not create the registry entry. Do not go live. Commit at each green checkpoint, with the step ID. Push only on Mark's
word.

## When done

Hand Mark one package:

- the gates report
- the freeze declaration, with M2 (the Article 29 determination) listed
- what was approved to proceed, and where its review files live
- the probe results and the Deep Interview transcript, each labeled
  observed or authored
- the Craft/Focus spot-check reading
- the Validation Layer attestation, with the freeze criteria it names as
  not met
- the Record Integrity read
- the residue read and the bar screen artifacts
- both ledgers
- the open items, each with its `Open_Gaps_Tracking.md` entry
- the fleet sweep result
- the world-boundary completion summary

Send a summary to the System Hub thread. Do not edit the Standing dashboard
files, the Task Board or the Gantt. Mark decides Frozen status.
