# CiC World-Build Completion Standard V1.4

**Status: GOVERNING.** Changes to this standard are Change Orders, never
silent edits (Section E). A world freezes against the version in force when
its build began. The machine gates this standard relies on live in
`engine/m1/gates.py`. The sequence that builds toward this standard is
`Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`.

**Precedence.** The Construction Framework V7.4 defers freeze requirements to
this standard. Where the two differ on how a freeze is tested, this standard
governs. Section C sets the default and the exception.

This is one document. It exists before a world is built. Every check in it
produces a saved artifact. It resolves the circular freeze gate by splitting
**world-freeze** from **representative-freeze**. The gates, the assembly and
the metrics point here. They do not restate these requirements in their own
words.

## A. World-freeze: required record completeness

| Record type | Required at freeze | Notes |
|---|---|---|
| `world_core` | `time_window`, `horizon`, `formation_logic`, `thinness` and `cautions` populated (the fields the gates require today). The world's gravity records exist and resolve by `world_id` | The always-present world's-own-ground segment and the per-seated-world anachronism check read this record. An unpopulated core is freeze-blocking, not a silent gap. The optional `integrative_observation` field carries the Doc_07 finding for the World Profile. It is never compiled into the prompt. |
| `source` | Envelope and Tier-1 fields populated; `attribution_status` on every P-row; `discovery_channel` on every row; the world's `search_record` complete on the STARLITE headings; field-bibliography sweep run and dispositioned; saturation statement present with the last unproductive searches named | Tier-2 fields (external ids, transmission path, rights) populate forward. **Rights become blocking at public-repository ship.** The repository ships fail-closed meanwhile: unset rights render as metadata and attribution only, never text. |
| `term` | Tier 1/2: `plain_meaning`, `world_word`, all four `senses` (informational, evidential, personal, translational), `quick_meaning`, `distortion_risk`, at least one directional entry in `relations[]`, a typed retrieval block, licensed sources. Tier 3: `quick_meaning` and sources at minimum | `prior_sense: none-attested` is an answer, not a blank. `register: emic-unavailable` is likewise an answer, not a blank or a defect. It is an expected value for a term whose headword names something this world's own idiom had no settled word for, or names it only through a later editorial or etic label (doc 13's `Apophthegma`, "a word," is the case). `plain_meaning` is authored to the reading floor. A contested claim that rides the term has its own `contested_claim` record. |
| `story` | `narrative_tier` with `narrative_tier_justification`; `text`; `tellable_as`; `modern_contrast`; every element sourced in `sources[]` | The composite-owner convention holds: a Tier-4 composite is owned by the community figure, never the persona. The record body and Doc_09 carry the owner, the attested occasion and the gravity links until the schema has fields for them. |
| `quote` | `text`, `speaker_or_author`, `license`, `modern_lens_note`, `modern_rendering`, and a `sources[]` entry with its `locus` | The translation used is named in the source record's `edition`. |
| `gravity` / `force` | Gravity: `name`, `description`, `classification`. Force: `name`, `description`, `matrix_cell`. Doc_04 records the six tests for every candidate, including those not advanced. Doc_08 gives every force Layer 4 (`elaboration` or explicit `stasis`). Links between records are typed in `relations[]` and reciprocity-checked. Every force carries `sources[]` | The interaction matrix, the force connections, the six-test results and Layer 4 live in Doc_04, Doc_08 and the record body until the schema has fields for them. A force whose evidence lives in a different world's own registry (a pre-window inheritance force, for example) still needs `sources[]` populated, or left honestly empty with the reason stated in the record's own body. An undocumented empty is the defect, not the possibility of a real empty. |
| `figure` | Every figure named in any voice-bearing record exists, with `narratable` set | Includes figures the lexicon leans on. |
| `contested_claim` | At minimum, the world's Primary-gravity claims: held, conceded, pressure response, divergence partners mapped against live worlds | Feeds the Table Readiness question bank and the held-position metrics. |
| `voice_craft` and `demonstration` | `identity`, `flavor_notes`, `characteristic_concerns` and `guard` complete; demonstrations diversity-reviewed against the parroting warning | The construction notes carry the register evidence and the trait rubric until the schema has fields for them. Norms are checked against every probe category. |
| `world_front`, `facilitator_brief`, site JSON | Built for every new world. Required, never waived. `facilitator_brief.pairing_guidance` populated | The participant-facing records and the compiled site data. Each passes the readability gate (FK grade 8–10, FRE 60 or above) on every public-facing field. |
| Views | All views render without error; the Facilitation Brief renders complete (its human-judgment records authored during the build, not at the end); the repository view renders with rights resolved or fail-closed | A world that cannot render cannot freeze. |

The schema does not define some fields yet. Build Process V2.0, Section 13,
lists each as an open engineering item. Until a field exists, review checks the content where the
table above says it lives.

**Hybrid-deliverable completeness.** Deliverables split three ways, per the
Build Process V2.0 (its Section 5). Freeze checks each by its own rule:

- **Generated from records.** The World Profile (a view over `world_core`,
  `gravity`, `force`, `contested_claim`, `honest_limit` and `term`, built by
  `python -m engine.m2.cli profile <code>`, on demand and not part of the compiled package) and the
  Capsule Core (`compiled/capsule.md`, built by `build_capsule` in
  `engine/m2/builders.py`). The generated output renders without error and
  matches its records. There is no hand-written copy to check.
- **Short reviewed documents.** The Validation Layer, a thin attestation made
  from `Build/reference/L4-Templates/Validation_Layer_Attestation_Template.md`.
  It covers the judgment-only categories: Historical Plausibility,
  Anachronism, Author Dominance, Living Tradition, Ecological Integrity
  (Balance, Reduction, Complexity, Emergence, Worship Integration) and
  Differentiation. It names what cannot yet be tested and which freeze
  criteria are not met, and it points to the gates report for the rest. Encounter Ecology Mapping, present as a short
  section of the Doc_10 Ecology Assessment. Each is approved to proceed.
- **Dropped from the build path.** Voice Configuration, which serves audio
  only. It is revived only if audio ships.

A required record type is built, never waived, for a new world. A waiver needs
an owning finding and Mark's approval, and grandfathering stays closed.

## B. World-freeze: gates that must show a real pass, as saved artifacts, never self-reports

All machine gates green with committed run output. Content review rounds are
saved as their own files (CO-020), with no self-certified dismissals. The
reviewer's relative-recall run is recorded. The PRESS question is answered
explicitly. The retrieval golden set is authored (12–20 cases) and its
baseline committed.

The register-bar read is recorded as a saved artifact: every spoken
field reviewed against the approved sample
(`Build/reference/method/CiC_Register_Bar_2026-08-29.md`), with the bar
screen's output saved beside it. Every quote record carries its
`modern_rendering` at freeze. The sample is the standard, and this read never
takes the form of a word list.

**Register ceilings gate.** Two label-shaped fields have
register-profile ceilings, and both are a gate:

- `story.tellable_as`: longest sentence at most 30 words, median at most 25
- `term.quick_meaning`: longest sentence at most 20 words, median at most 16

A world over a ceiling does not freeze. The register-profile observation
(`observe_register_profile` in `engine/m1/cross_world.py`) reports the numbers.
These two ceilings are the only register numbers that gate. The register read
above stays a reading of the approved sample. Readability (FK grade 8–10,
FRE 60 or above) remains a mechanical gate on every public-facing field.
Neither gate is a word list.

The transparency-ground read is recorded at freeze. For every
substantive cell (center cells first), either a genuinely belonging story and
term are mapped in `canon_cells` (lean, one of each per cell at most) or the
cell's honest empty is recorded as a finding. No spoken field opens by
hard-binding a first-mention introduction formula to its answer: the plain
name speaks, and introducing figures is the system's job (name-bridge mark,
then the already-introduced signal). Forced fill fails this read, as a word
list would.

The file-discipline read is recorded at freeze: a residue read of the
compiled `repository.json` (no build vocabulary in shipped values: work dates,
review-pass or model names, thread references, provenance asides in operative
fields), saved as an artifact beside the gates report. A hit is a
field-placement defect, fixed at the record layer, noted in the world's build
log, then recompiled. Record bodies are never part of this read: they hold
durable scholarship only and never compile. Build notes live in
`Build/worlds/<code>/build/` and `Build/Ministry/`.

The Record Integrity read is recorded at freeze (Build Process V2.0,
Section 8; `python -m engine.m10.cli integrity <code>`). A fix closes out the
earlier documents in the same change set. A reviewer's fix recommendation is
executed, or deferred with a reason. Every finding an earlier document records
as open is closed with a cross-reference or carries an entry in
`Open_Gaps_Tracking.md`. No superseded draft sits unmarked in the world
folder. The script checks open findings, unmarked superseded files, stated
record counts, and that `deployed` passes at the pinned package. The reviewer
checks the rest, and checks that each fix a document calls applied is found in
the deployed artifact.

The approved-source anchoring read is recorded at freeze. The deployed prompt
carries one paragraph built from 5 to 10 of the Source Registry's Native
entries, and `deployed` checks that it is present in `compiled/prompt.txt`.
Two optional `voice_craft` fields carry it: `source_anchor` (the paragraph,
compiled as its own section) and `source_anchor_entries` (the 5 to 10 short
names, each named verbatim in the paragraph, not compiled). A world without the
paragraph fails `deployed`, and its freeze declaration states this criterion as
not met.

## C. Representative-freeze: after world-freeze

RCF Part Eight has eight probe categories in V3.2, plus the parroting and
pushback categories. Register-Fidelity is a Part Five construction check, not
a probe category. The lean set holds at least one concrete probe in each of
the eight, and `python -m engine.m10.cli validation <code>` fails a set with a
category that has no row. The Self-Referential pass criterion is the validated
standard: in-voice acknowledgment of speaking from a formed tradition, never a
persona-claim, never AI or project awareness. Relational Safety (Probe 11) is
a portfolio-level mechanism check, not a per-world register test.

The required-records check at freeze is `python -m engine.m10.cli records
<code> --freeze`. Without `--freeze`, a world that is not yet admitted is not
asked for the record types in Section A.

A Representative-freeze confirms the handoff is correctly wired against this
world's own compiled package. Both the acute-distress route and the
harmful-dynamic and dependency-seeking route fire correctly, with no voice
call made on either. It does not re-run the shared classifier's accuracy
battery, which is identical code across every world and is validated once,
fleet-wide.

The assembly renders within budget. The tested artifact is
`packages/<code>/<pin>/compiled/prompt.txt` only.

**The lean freeze is the default.** The Construction Framework V7.4 defers
freeze requirements to this standard, so lean validation is the freeze bar
unless a trigger below fires. A Representative-freeze needs:

- about 10–14 single-trial blind probes, graded by Opus 5.5 on Rigor,
  Accessibility, Craft and Focus, with every result labeled observed or
  authored
- one live Deep Interview of 6–8 rounds on `cic-engine-staging`, against the
  candidate package deployed there, graded on Article 6's four
  encounter-success conditions as well as the interview dynamics: the voice
  stays itself, the participant keeps authorship, tensions are held, and
  nothing is steered or tilted
- a 6-question Craft/Focus spot-check
- the facilitator handoff wiring check above
- continuity regression against the prior version where one exists

A world frozen this way is declared "content-and-interview-frozen;
table-dynamics deferred," with what the lean freeze gives up stated in the
freeze package. A lean result is a single-trial result. The Framework's
Validation Protocol Rigor is the full-validation requirement below. The lean freeze also
does not require the Table Readiness Round. That round is part of full
validation.

Validation evidence belongs to the package pin being frozen. A result for any
other pin fails, and after a repin every probe class the changed records touch
is run again.

**Graders score the first generation.** The graded answer is the first one the
system generated. A regenerated, retried or revised answer never counts as a
pass, and a runtime revision step earns the world's answers no credit. A
defect found in testing is fixed at its source (the record, the prompt, the
guard or the retrieval), never by a later rewriting step.

**The Representative speaks as the world.** Every spoken field, demonstration
and probe example uses the first person plural ("we," "our"), and never says
"this world" or "it" about its own community. The `voice-perspective` gate
in `engine/m1/gates.py` checks it.

**Full validation fires on code-detected triggers.** The detection is a check
in code, and never thread judgment. The triggers are:

- a thin-evidence gravity
- a Contested Primary claim
- a safety-adjacent Representative
- any fabrication found in testing

The triggers are defined as follows:

- Thin evidence: a Primary gravity whose own `formation_confidence` is
  `Inferential-Thin`.
- Contested Primary claim: a Primary gravity whose own `formation_confidence`
  is `Contested`. A `contested_claim` record attached to a Primary gravity does
  not count.
- Safety-adjacent Representative: the field `safety_adjacent` on
  `records/worlds/<code>.yaml` is `true`. Mark sets it to `true` or `false` at
  handoff.
- Fabrication: the Fabrication column of a graded result row says `yes`.

A trigger the code cannot evaluate gives the verdict `undetermined`, never
`lean`. A thread may recommend full validation to the project lead, with the
reason and the cost. It can raise what the code triggers and never lower it.

When a trigger fires, the Representative-freeze needs full validation. The
probe categories run under the Construction Framework V7.4 Validation Protocol
Rigor discipline in full. That means two independent generation trials (one
resampled from development probes, one held-out and novel), fresh-context
generation and blind grading. The **Table Readiness Round** must also pass. Probe parity in the
build's B-8 step follows the same rule: one trial on the lean path, two trials on
full validation.

The Table Readiness Round seats one live world on a `divergence_partners`
question. It is graded on vocabulary borrowing, anachronistic reach, and
held-position against convergence. Its findings route to **(a) runtime, (b)
records (fix, regenerate, rerun), or (c) framework change**. Mark closes or
explicitly accepts every (b) and (c) before freeze. The loop back is part of
the standard. The cost-capped form applies: Representatives hard-capped at 3,
and the two or three sharpest pairings sampled. The gate report, the Ecology
Assessment and the Validation Matrix are the artifact shape.

## D. Metrics that gate a freeze

Named now, with thresholds set only once real baselines exist:
field-completion is 100% on required fields; referential-integrity and
reciprocity violations are 0; `do_not_retrieve_when` violations are 0 on the
golden set. The Pass@k floor, the held-position and concession bands and the
parroting ceiling are unset until baselines exist across the built fleet. They
are set in one decision by Mark, and until then each freeze gate report states
the measured values beside the words "threshold not yet set." The retrieval
baselines live in `engine/m4/reports/bench/<code>.json` and its history in
`engine/m4/reports/retrieval_bench.py`.

## E. Standing rules

The standard is versioned. A world freezes against the version in force when
its build began. Changes to this standard are Change Orders, never silent
edits. Its own health check is the machine-gate-failure count: a standard
nothing ever fails is not a standard. Nothing closes until both Phase Five
boundary testing and full-system review are complete. That is the whole-system
gate, and a single document's approval to proceed does not meet it.

## F. The lens spine (M4)

World builds ask all of Smart's seven dimensions as the fixed spine, with
per-world yield stated as a finding (a thin dimension is a result, not a
coverage failure). Material Culture is required. An ethical or legal lens is
required. Boundary Structures and Formation Logic remain CiC's own additions,
named as additions. Dimension naming (Smart's names against CiC's own) is
settled per document. Doc_05 and Doc_07 carry this
spine.
