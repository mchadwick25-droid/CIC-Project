# CiC Pilot Protocol — V2.0

This protocol governs the first two worlds built under
`Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`
(Section 11). It sets the running order, the blinded Doc_10 comparison
between Sonnet 5.5 and Fable 5.1, and the pilot report.

## What the pilot answers

- **Quality.** Does the process, with its gates, produce a world that meets
  the four criteria with zero fabrication and no new waivers?
- **Cost.** What share of a week's allowance does one world take? At least
  half the week goes to building. Three worlds a week need about 16 percent
  each. Five need about 10 percent each.
- **Fable.** Can Sonnet 5.5 draft Doc_10 to the Craft bar, so that Fable is
  needed only for Doc_04?
- **The gates.** Which defects did code catch before Opus saw them? Which
  reached Opus that a script should have caught?

Two worlds are a small sample. The results are indicative, not statistical.
That is why the Fable rule below is cautious.

## Running order

**Before the pilot starts:**

- The metered ceiling is set.
- The project lead has named the pilot pair.
- The Library has passed `handoff` for both worlds.
- The fixture shakedown is clean, or its defects are fixed.
- Process V2.0 is frozen. Later changes are change orders.

**Start.** Begin right after a Friday 2:00 pm reset, with the `/usage`
percent noted. Heavy steps (Opus rounds, Fable drafts) go early in the week.

**One world at a time.** Build World A from Doc_03 to its freeze package.
Review the pilot process on World A, then start World B. One process defect
then costs one world, not two. Do not start World B while World A's freeze package holds an
open blocking finding.

**What each world records.** The `/usage` percent at start, at every
document boundary and at freeze. Sonnet, Opus and Fable tokens are logged per
document and per review round.

**After both worlds,** one pilot report goes to the project lead. Nothing
runs beside the pilot except work the project lead names.

## The Doc_10 comparison

### Identical inputs

Both drafters get the same inputs:

- approved Docs 03 to 09 and the world's records
- the Doc_10 template
- the Register Bar
- the naming and role discipline
- the Craft bar, items (a) to (e), in Section 4 of the Process document

Each drafter starts in a fresh context. Neither reads the other's draft.
Both drafts are made in the same week.

### Blinding

A command assigns the labels, not a person:

`python -m engine.m10.cli blind <code> --sonnet <path> --fable <path> [--seed S]`

The command assigns A and B from the seed. It scrubs drafter and model names
from the header fields. It fails if a name appears in body text. It writes
`Doc_10_A.md` and `Doc_10_B.md`, and a mapping file,
`build/<code>_Doc10_Blind_Mapping.json`. It prints the mapping file's
sha256.

The thread commits that checksum to the cost ledger before any grading
starts. The mapping cannot change afterward.

After grading, the mapping is revealed with:

`python -m engine.m10.cli blind <code> --reveal --mapping <file> --checksum <sha>`

The command checks the checksum first. It prints the mapping only if the
checksum matches.

Style can still hint at the drafter. Each grader is told so. Each grader
records a guess of which draft is which, after scoring. The guesses show how
often the blind holds.

### Grading

Two independent Opus 5.5 passes grade the pair. Each pass runs in a fresh
context at high effort. The two passes read the drafts in opposite orders,
which controls for position bias. Each pass uses
`Build/reference/L4-Templates/Pilot_Doc10_Blind_Grading_Sheet_Template.md`.

Each pass scores both drafts on:

- the four criteria: Rigor, Accessibility, Craft and Focus
- each Craft bar item (a) to (e), pass or fail, with a quoted line as
  evidence for every fail
- fabrication, checked claim by claim against the records. Any invented
  specific is a fail, whatever else is strong
- readability, taken from the gate scores (grade 8 to 10, reading ease 60 or
  higher), not from the grader's opinion
- AI tells, read against the approved sample

Each pass ends with a head-to-head preference on Craft and on Focus: A, B or
tie.

### The decision rule

Sonnet's Doc_10 must meet both tests in each pilot world.

- **The absolute bar.** All five Craft bar items (a) to (e) pass. There is
  zero fabrication. The readability gates clear. All of this holds in both
  grading passes.
- **The relative bar.** Both graders must not prefer Fable's draft on Craft.
  A single grader preferring Fable does not fail Sonnet. Two graders
  preferring Fable does.

The result follows from the two worlds:

- If Sonnet meets both tests in both worlds, Fable is needed only for
  Doc_04.
- If Sonnet fails either test in either world, Fable stays for Doc_10 as
  well as Doc_04.
- If Sonnet meets both tests and the drafts tie, Sonnet's draft continues.
  It is cheaper.

Two worlds are a small sample. Dropping Fable saves allowance, but a weak
voice costs every world after it. The rule therefore keeps Fable unless
Sonnet clears both tests twice.

### What is recorded

- both graders' sheets
- the mapping, after grading
- each draft's cost in allowance percent and tokens
- the gate results for both drafts

The chosen draft goes on to normal review: three Opus rounds at most, then
the project lead. The other draft is archived with the review artifacts.

## The pilot report

The report follows
`Build/reference/L4-Templates/Pilot_Report_Template.md`. It has eight
sections.

| Section | Content |
|---|---|
| Cost per world | Allowance percent from start to freeze, split into drafting, review and probes. Metered spend in dollars. Hours. |
| Pace | Worlds a week at the measured cost, with half the week for building. |
| Review effort | Rounds per document, and which documents reached three. |
| Gate catches | What each gate caught before Opus. What Opus found that a script should have caught. These become new checks. |
| Validation | Lean or full, and why. Which triggers fired. Deep Interview and spot-check readings. |
| Fabrication | Any found, where, and what caught it. |
| Fable test | Both worlds' grading sheets, the decision under the rule above, and the cost of the Fable draft. |
| Process defects | Every place the process or a template gave the builder no way to proceed. |

## Stop rules

Stop and tell the project lead at any of these:

- any fabrication finding
- any document that reaches three rounds without clearing
- any waiver request
- any budget number that would thin the work

Only the project lead assigns Frozen status.
