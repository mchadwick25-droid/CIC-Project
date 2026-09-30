# CiC Record-Native World Build Process — V2.0

**What this document is:** the single end-to-end process for building a new
formation world. It runs from the Library's handoff package (after Step 2) to
a drafted freeze package. A new world is born record-native. It is authored
straight into the schema-validated record store, under the live gates. The
deployed prompt, chunks and site data are generated from those records. There
is no separate migration pass, because the authoring is the migration.

**Scope.** The Library (the source-research thread) owns pre-Step 0, Step 0,
Step 1 and Step 2. This document starts at the handoff. Go-live is a separate
thread. The registry entry and go-live are Mark's acts. A world build ends at
a drafted freeze package, and Mark assigns Frozen status.

**What governs, in order of authority.** This document sequences these and
fills the gaps between them. It replaces none of them.

1. `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`
   — the Construction Framework, ratified as governing (per
   `Build/reference/method/Pass2-decisions/S6.1_M_construction_framework_v74_promotion.md`).
   It carries the Table Readiness Round, the Record Integrity Principle, the
   Source Registry freeze gate and the Validation Protocol Rigor discipline.
   Its Freeze Criteria defer the freeze requirements to the Completion
   Standard (item 3). Section 8 follows that deferral: lean validation is the
   default freeze, and the Framework's two-trial Validation Protocol Rigor is
   the full-validation requirement.
2. `Build/reference/L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`
   — the Representative Construction Framework (Part Three Ecology
   Assessment, Part Eight Validation Testing, Phase Eight Table Readiness
   Round).
3. `Build/reference/method/CiC_World_Build_Completion_Standard_V1.4.md` — the
   freeze-requirements source of truth.
4. `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`
   — the one-document-at-a-time, review-gated discipline.
5. `Build/reference/Project-Reference/CiC_Governance_Standing_Rules.md` — the
   standing review rules, restated in Section 10 so a session needs no other
   file to follow them.
6. This document — the sequence, the gate layer, the record-native additions
   and the routing and cost rules.

The Doc_04 template is
`Build/reference/L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md`.
The Doc_10 template is
`Build/reference/L4-Templates/Representative_Construction_Notes_Template.md`.
Use the templates in `Build/reference/L4-Templates/` as they stand. Never fork
a copy.

The build-cycle, lexicon-index, gravity-index, forces-index, story-repository
and validation-suite disciplines this document names are vendored at
`Build/reference/method/skills/`. Every thread reads them there.

**Vision framing (standing, Mark).** Purpose statements and any
participant-facing copy produced in a build lead with making experiential
Christian formation available. The product is the current means, never the
mission's definition. The Brand Kit QuickRef governs all public wording.

**Process version.** Each world is stamped with the process version in force
when its build starts (Section 12). A world finishes under the version it
started under.

---

## 0. What a build is for: four criteria, Craft first

Every step below serves four things a real conversation has to be. These four
criteria are the depth rubric. Reviewers and blind graders score against them.

1. **Rigor.** Every claim traces to a real source. A Contested or
   Inferential-Thin claim keeps its own hedge and is never voiced as settled
   fact. Nothing is invented: not a record, not a line of voice, not a probe
   document, not a review file.
2. **Accessibility.** Plain English first, one idea per sentence, in the
   CEFR B2 range and FK grade 8–10.
3. **Craft.** A distinct, real voice. The world's own imagery and concerns
   survive. Register statements 1–7 hold: answer the actual ask first; use
   concrete nouns; coin no quotable lines of your own (a real quote, named
   and sourced, fills that role); and repeat nothing word for word across
   different answers. **Storytelling is part of craft.** A story earns its
   place by being told, not summarized: a real scene, real stakes, the
   concrete detail that makes it land. It is told freshly each time, shaped
   to the question asked, never the same fixed narration pasted in twice. The
   strongest demonstrations in the fleet measurement (Sebaste's frozen lake,
   the cloak cut in two at the gate, Sarapion's prayer breaking under him)
   all did this. The weakest repeat their one good telling verbatim.
4. **Focus.** The answer addresses what was asked, including the hardest and
   most personal questions in the Question Canon, and not only the easy ones.

**Conversation depth** is the Representative's power to draw on the
Library's resources. It gives an answer of real quality that answers the
question asked. A shallow, flat or evasive answer fails depth, even when every
fact in it is true.

**Craft is the keystone.** A fleet measurement (66 real generated turns, all
11 worlds, the same standardized questions, checked claim by claim against the
records) found a real fabrication rate near 0%. There was one confirmed
defect, and it was fixed. That held wherever the build had done its job:
records with honest confidence tags, guard lines scoped to what a reader could
really be misled by, and a voice built from the world's own material. A
separate adversarial test of the live grounding checker found that it misses
97–98% of fabrications built to fool it. That number measures how easily the
after-the-fact checker is fooled. It does not measure how often the real
system fabricates. Conflating the two pulls review effort toward heavy,
per-step adversarial scrutiny that the measured defect rate does not justify.
Build the craft right (accurate hedges, a distinct voice, direct answers, no
invented specifics) and rigor mostly follows. Spend review effort on what
craft alone will not catch: a wrong name attached to a real citation, a stale
file path, a real scope conflict between two governing documents. A script
catches the rest.

The same measurement found the real gaps a build should watch for. All are
Craft- or Focus-shaped, and none is fabrication:

- a "composite voice" disclaimer answering instead of a personal Center-cell
  question in over half the fleet
- a shared self-composed "not X, but Y" closing-line habit (register
  statement 6)
- literal sentence reuse across different answers in one world
- a two-world leak of build-pipeline vocabulary ("vendored," "our own build")
  into in-character speech
- a handful of confidence-tag flattenings, where a Contested or
  Inferential-Thin claim was voiced as flat fact

Doc_10 (Section 4) and the Craft/Focus spot-check (Section 8) are where a
build catches these.

**The review bar** is what a church history scholar would call good. It is
not perfection. Opus 5.5 reviews everything. A finding that a document could
be stronger, with nothing in it wrong, unsupported or misleading, is not a
substantial finding.

**Public-facing content** means `world_front`, `facilitator_brief`, the site
JSON, the traditions page and the Representative's spoken fields. It has no
AI tells and reads easily. Two checks hold it:

- **Readability is a mechanical gate.** Flesch-Kincaid grade 8–10 and
  Flesch Reading Ease 60 or above, on every public-facing field, re-run on
  every edited field.
- **AI tells are a judgment read.** The Opus review reads each public-facing
  field against the approved sample,
  `records/syr/demonstration/syr.demo.room-for-doubt.md`. The Register Bar
  keeps no banned-word list, and this process adds none.

Two principles run through every step below.

**We speak only from the world's perspective.** The Representative speaks as
the world, in the first person plural: "we," "our." It never says "this
world" or "it" about its own community. The `voice-perspective` gate in
`engine/m1/gates.py` checks every spoken field. Doc_10, the voice record, the
demonstrations and the probe examples all follow the same rule. Section 6
states it as a birth condition.

**Right answers first, generated correctly.** The process grades the first
answer the system generates. A regenerated, retried or revised answer never
counts as a pass. A defect found in testing is fixed at its source: the
record, the prompt, the guard or the retrieval. A later rewriting step never
patches it. Section 8 applies this to grading. Runtime self-revision, where
it exists, earns the world's answers no credit.

---

## 1. The human checkpoints and the escalations

Three stops are built into the process. Everything else a build thread decides
and records on its own. Decisions are logged, never silent.

**M1: Representative identity (mid-build, after Doc_09).** The build thread
prepares the grounded-options artifact for Mark, per the build-cycle
discipline's escalation rule and the naming and role discipline in
`Build/reference/method/CiC_Representative_Naming_Role_Discipline_2026-09-08.md`.
Identity and image are decided together, once, as one packaged choice among 2
to 4 named candidates, each with trade-offs. The package holds:

- a scored options table for ROLE, each option grounded in the world's own
  methodology facts, with named trade-offs
- a scored options table for NAME, scored on ecological resonance,
  authenticity, collision-with-a-real-figure risk, gender clarity and
  memorability
- ONE recommendation for each
- the image choice, packaged with the identity choice and never asked as a
  second interruption. Check the image option before it goes to Mark against
  the fleet's existing portraits and against the object and silhouette rules
  recorded in the In-App Icons and Graphics feature folder,
  `Build/Ministry/Features/In-App-Icons-Graphics/`.

The options render as an Artifact for Mark to review. Once he decides, the
decision is saved in the world's folder as
`Build/worlds/<code>/Representative/<code>_Representative_Identity_Options.md`.
The thread stops and presents the options. Two earlier executions set the
pattern:
`Build/worlds/alx/Representative/alex_Representative_Identity_Options.md`
(Mark rejected both recommendations and chose "Theon," with his reasoning
recorded) and
`Build/worlds/hal/hal_Representative_Identity_Preliminary_Decision.md` (Mark
adopted a fifth option not among the four presented, the widow Albina, with
the naming-collision risk disclosed and accepted on the record). Mark's answer
is often not the recommendation. Present real options with real trade-offs,
record his decision verbatim in the same file, and never proceed on the
recommendation alone.

**M2: Article 29 (Living Traditions) determination (at the freeze).** This is
a project-lead act under Constitution Article 29. The build thread drafts the
determination with its full history and its own recommendation. It carries the
status as `provisional` until Mark confirms. It lists the determination in the
freeze declaration's RESOLVED-AT-THE-FREEZE section for his explicit word.
Article 31 telos review is not a stop. It stays provisional until year two.

**M3: The freeze itself.** Only the project lead assigns Frozen. The thread
never assigns it to itself. It completes everything, drafts the freeze
declaration, and stops with a completion summary. Mark's word executes the
freeze.

**Escalate to Mark only for these.** The build thread stops for nothing else.

- the metered-spend ceiling number (Section 9)
- the two pilot world choices (Section 11)
- Representative identity and title decisions (M1)
- a cross-world or portfolio decision
- a governance or methodology change not already decided in this document
- an unresolved tension after three review rounds (Section 10)
- a missing input the build cannot supply or derive itself
- a budget number that would thin the work (Section 9)
- Frozen status (M3)

Route a framework or template gap as a flagged finding in the world's
`Open_Gaps_Tracking.md`. Do not rewrite an upstream document to close it.

---

## 2. Models, effort and briefs

The routing is pinned. It is not per-thread discretion.

| Lane | Model | Scope |
|---|---|---|
| Drafting, orchestration, mechanical work | **Sonnet 5.5** (`claude-sonnet-5-5`) | Every document except Doc_04 and Doc_10. The Phase B conversion scripts. Package rebuilds. Ledger and state-file discipline. |
| Key components | **Fable 5.1** (`claude-fable-5-1`) | Drafts Doc_04 (Gravity Discovery) and Doc_10 (Representative Construction Notes, Permanent Prompt, voice and demonstrations) only. Also diagnoses failures in Phase D. |
| Review and grading | **Opus 5.5** (`claude-opus-5-5`) | Every review round. Blind grading. Deep source research and the M1 identity research. Authors every `modern_rendering`, and a separate Opus pass checks each one. |
| Mechanical steps below Sonnet | Script first, then Haiku 4.5 | Formatting, indexing, citation and log fixes. |

**The reviewer is never the drafter.** Opus reviews Sonnet's drafts and
Fable's drafts alike.

**Pilot test for Fable.** In the pilot worlds (Section 11), Sonnet 5.5 and
Fable each draft Doc_10. Opus 5.5 grades the two blind on Rigor,
Accessibility, Craft and Focus. If Sonnet meets the Craft bar, Fable drops out
of the fleet process. If it does not, Fable stays for Doc_04 and Doc_10 only.
The grading goes in the cost ledger.

**Effort per task.** Set effort explicitly. Claude Opus 5.5 defaults to
`medium`. `high` is real, careful review and is the standing effort for round
1. `xhigh` is reserved for a genuine reasoning-edge task, and never for "this
document happens to come early."

| Work | Model · effort |
|---|---|
| Round 1 adversarial review, every document | Opus 5.5 · high |
| Targeted recheck, rounds 2–3 | Opus 5.5 · medium |
| Re-confirming a blocking finding | Opus 5.5 · high, fresh context; xhigh only if two reviews disagree |
| Blind grading (Phase D) | Opus 5.5 · medium; high for probes in known hard-to-detect areas |
| Deep source research, M1 identity research | Opus 5.5 · high |
| Doc_04 and Doc_10 drafts, Phase D failure diagnosis | Fable 5.1 · high |
| Every other draft, Phase B conversion, orchestration | Sonnet 5.5 |
| Authoring `modern_rendering`, and any re-rendering | Opus 5.5 authors; a separate Opus 5.5 pass checks it (Decision 8B) |
| Mechanical work | Script first, then Haiku 4.5 |

If Claude Code sets effort per session and not per subagent, group review
sessions by effort class.

**The brief discipline.** A subagent's brief is pointers, not summaries: the
file paths and the specific question. The subagent reads the world's
documents and records itself. An under-briefed subagent wastes its tier. A
summarized brief launders the main thread's blind spots into the component
that exists to avoid them.

**Review agents.** Adversarial reviews run as independent subagent rounds.
Battery grading runs blind, in an agent that never saw the build. Gates loop
fix-until-green. The reviewer and grader tier is checked every round against
this section.

---

## 3. The gate layer: checks run as code before Opus sees the work

Every check in this table runs before an Opus review round. A review round is
never spent on a defect a script could have caught. The review brief says
what the checks covered, so the reviewer does not redo them. It also says
what they cannot cover: whether a claim is true. The grounding check reads
where the words came from, not what they assert. Checking that claims are
true is the reviewer's main job.

The commands are subcommands of `python -m engine.m10.cli <subcommand>`. The
subcommands are `handoff`, `prereview`, `roundcount`, `reviewfile`, `gaps`,
`citations`, `claims`, `integrity`, `deployed`, `probes`, `validation`,
`wiring`, `records` and `regate`. The World Profile generator is
`python -m engine.m2.cli profile <code>`.

| Check | What it is | When it runs | Command |
|---|---|---|---|
| Handoff verifier | Runs the 12 handoff checks of Section 4 and confirms Steps 0–2 exist and cleared review. For a world built before this process, it reads the project lead's re-baseline declaration and reports the accepted round-cap and verdict-wording items separately. | Start of the world, before Step 3. | `handoff <code>` |
| Handoff quote check | Re-verifies every Step 0–2 quotation against the vendored text in `cic/texts/`, speaker included. It also runs the locus check (`quotes-locus`): a quotation whose paragraph carries a `cic:<file>:<locus>` address must lie inside the division that address names, and a locus that names no division is a finding. A quotation in a paragraph with no address is not checked for locus. | Same run. | `handoff <code>` |
| Pre-review bundle | One command that runs `engine.m2.cli build`, `engine.m1.bar_screen`, `engine.m1.cross_world` and `engine.m9.cli holdings`, and saves the output for the review brief. | Before every review round. `--doc N` names the document by its number and only checks that its file exists. | `prereview <code> --doc N` |
| Citation resolver | Every record id and citation in a document or probe file resolves and is the right record type. | On every document and every probe file, before review. | `citations <code>` |
| Round counter | Counts every review file with a round number for a document (a review, a spot-check or a recheck), whatever its verdict. `roundcount <code> N --check-new` is the guard that runs before any new review file is written. With three review files on record it exits non-zero and routes the document to Mark. `N` is the document number (`0` for Step 0). Without `--check-new`, the command fails only once a fourth file already exists. Rounds are counted from the latest review file that carries a `Cycle reset` header field (Section 4, Library-stage rules); every file stays on record. | Before every review file is written. | `roundcount <code> N --check-new` |
| Claims-register check | Derives every absence or exclusivity claim ("no source says...", "the only surviving source...") from a document's deliverables and compares it with the claims register. Halts on a claim that is not registered, on a register entry no claim supports, and on a register entry whose evidence no longer resolves. Registration is the control. It does not show a claim is true. | Before every review round on a document that carries claims (Section 4). | `claims <code>` |
| Review-file check | The reviewer is not the drafter. The model is Opus 5.5. The first line carries the simulated-review label. A two-method truncation check is recorded. The optional `Cycle reset` field, when present, has text. | On every review file, before it counts. | `reviewfile <path>` |
| Open-gaps check | Every open item in a review or phase document has an `Open_Gaps_Tracking.md` entry. | After every review file. | `gaps <code>` |
| Process-narration block | The CI job `live-commentary` runs `tools/check_live_commentary.py --base origin/<base> --enforce`. A pull request that leaves process narration in a live or canonical file it edits fails. Files it does not edit are not scanned. | On every pull request. | CI |
| Re-gate after edit | Re-runs readability and the word budget on every changed field and every public-facing field. Confirms a new world carries no waivers and grandfathering stays closed. Any exception needs an owning finding and Mark's approval. | After any edit. | `regate <code>` |
| Required-records check | The record types a new world requires are built, never waived: `world_front`, `facilitator_brief` and the site JSON, with the rest of the Completion Standard's Section A. Without `--freeze`, a world that is not yet admitted is not asked for these types. At freeze the world is still in state `built`, so the freeze run uses `--freeze`, which requires them whatever the state. | After every records edit: `records <code>`. At freeze: `records <code> --freeze`. | `records <code> --freeze` |
| Deployed-artifact check | The compiled prompt contains every item Mark confirmed (living traditions, telos, self-reference hardening) and every rule count matches the records (for example, the count of `[quotation]` rules). It also checks the approved-source anchoring paragraph (Section 6, B-7): `voice_craft.source_anchor` is set, it stands verbatim as its own section of `compiled/prompt.txt`, and `voice_craft.source_anchor_entries` holds 5 to 10 distinct entries, each named in the paragraph. A world with no paragraph fails, except a grandfathered world, which gets a note. | After each package build or deploy. | `deployed <code>` |
| Probe-runner guard | The probe runner refuses the legacy Permanent Prompt file and tests only `packages/<code>/<pin>/compiled/prompt.txt`. A probe-results file must name the pin it tested, and that pin must be the current pin. | Before and after every probe run. | `probes <code>` |
| Result-label check | Every probe result is labeled observed (with a transcript reference) or authored. An authored result cannot score PASS or FAIL. | Before and after every probe run. | `probes <code>` |
| Grading check and trigger detector | Every answer is graded on all four criteria. RS-1 and RS-2 are scored separately. Detects the full-validation triggers (Section 8). A trigger the code cannot evaluate gives the verdict `undetermined` and a non-zero exit, never `lean`. It also checks that all eight Part Eight categories were run, that the Deep Interview carries its encounter-success grading, and that the results were run on the current package pin (a result for any other pin fails). | After the probe results are in. | `validation <code>` |
| Record Integrity check | Reads the world at freeze against the Construction Framework's Record Integrity Principle (Section 8). It checks four parts by script: every open finding in an earlier document has an `Open_Gaps_Tracking.md` entry; no superseded or second live version of a document sits unmarked in the world folder; no Construction Notes file states a record count the records contradict; and `deployed` passes at the pinned package (confirmed items, rule counts, source anchor). Three parts stay with the reviewer (Section 8). | At freeze, before the freeze package goes to Mark. | `integrity <code>` |
| World Profile generator | Builds the World Profile as a view over the world's records (Section 5). The profile is not part of the compiled package. No check reads it, and `records` does not cover it. Its status line reads INCOMPLETE whenever a section is not carried by records. Section 4 (Ecological Summary) has no source records, so it reads INCOMPLETE until records carry it. | On demand: after every records edit that changes a source view, and at freeze. | `python -m engine.m2.cli profile <code>` |
| Facilitator handoff wiring check | Both the acute-distress route and the harmful-dynamic route fire, and the voice is never called on either. | At the Representative freeze. | `wiring <code>` |
| Library validators | The CI job `library-validators` runs `cic/engine/corpus_map_merge.py --check`, `corpus_index.py --build`, `works_registry.py --check`, `author_ids.py --check` and `texts_registry.py`. | On a pull request that touches `cic/` or `engine/`. | CI |
| World gates on drafts | The CI job `world-gates` runs `records` and `regate` for every world a pull request changes in `records/`. The `engine-tests` job also runs on a draft pull request that touches records, packages, engine or world build documents. | On every pull request, draft or not. | CI |

The CI job `check-paths` runs `python tools/check_paths.py`. It reports path
citations that do not resolve.

Fix what a check finds before the round starts. If a check and a reviewer
disagree, the reviewer reads the source and the disagreement is recorded in
the world's `Open_Gaps_Tracking.md`.

---

## 4. Phase A: World construction

### The Library stage (Step 0 to Step 2)

The source-research thread owns Steps 0–2. Each runs under the
one-document-at-a-time cycle (draft, adversarial review, revision,
disposition) until it is approved to proceed. The Library's own rules for
that stage live in the Library's documents. What follows is what the build
depends on.

| Step | Document | What the build depends on |
|---|---|---|
| 0 | `Step0_Movement_Scope_Confirmation` | The world is confirmed against `Build/reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx`'s portfolio entry. |
| 1 | `Doc_01` World Identification, Boundaries, Orientation | Article-21 strand analysis is done here if the world is strand-plural. Strands ride `world_core`'s body until the strands schema lands. |
| 2 | `Doc_02` Source Ecology | The Source Registry follows the Source Registry Template from the first row: machine-readable rows, with per-row confidence, boundary status, licensed-for and verification note. Every load-bearing caveat (do-not-cite flags, pending-verification lists) is its own row field, not prose. Holdings dispositions are recorded: every file `python -m engine.m9.cli holdings <code>` marks "not yet assessed", and every tier 1–2 file it marks "in scope, unread", has one line in the Source Registry: used, deferred with a reason, or out of scope with a reason. Files marked "no coverage entry" are a library gap, counted and left. |

The Library stage builds on the world's library package
(`Build/worlds/_cross-world/SOURCE-READINESS.md`):

- the Source Readiness Dossier at
  `Build/worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md`
- the corpus-map assignments at `cic/corpus-map/<slug>.yaml`
- the vendored texts those assignments point to in `cic/texts/`
- any further rendered source material the research produced

Doc_02's Source Registry gives every item in the package a line. Every
dossier §1 assigned work, §2 cross-link and §3 acquisition lead is used,
deferred with a reason, or out of scope with a reason. A lead not yet
vendored is marked for acquisition. Every §5 open cross-world question is
named and carried forward, not decided. Every piece of rendered source
material is used, or set aside with a reason.

Step 2 also produces, for the build to work from:

- an exact locus for every quotable passage
- a quotability flag for every file: verbatim-ready, second witness only, or
  unusable
- own-voice and opponent-voice flags wherever one work mixes them (a
  martyrology, a polemic, a trial record)
- corpus-map rows with `row_id`, corrected `role` and `voice_of`
- a holdings disposition for every item
- a thin-evidence map, which feeds confidence levels and the admission probes
- for each work, its edition and original language, and which text is primary
  and which is the cross-check
- cross-world overlaps and pairs (`cic/corpus-map/PAIRS.yaml`)
- optionally, one line on material and archaeological sources consulted or
  not, and the social roles the sources attest for a Representative

**Library-stage rules.** Each is stated here once and holds for Steps 0 to 2.

- **Registry entry.** `records/worlds/<code>.yaml` is created when the project
  lead assigns the world code. It carries `world_id` and `census_id` (the
  census id of the world's corpus-map bucket and dossier) and must exist
  before the handoff gate is run, because the gate reads the bucket and the
  dossier through `census_id`. The project lead sets `safety_adjacent` at
  handoff.
- **Review files.** Step 0 reviews are `Step0_Review_Round<n>.md`, in the
  world folder or in `Review-Artifacts/`. Step 1 and Step 2 reviews are
  `Doc01_Round<n>_Review.md` and `Doc02_Round<n>_Review.md`, in
  `Review-Artifacts/`: one file per document per round. A combined review of
  two documents is filed as identical copies under both names. The round
  number in the name equals the `Round` field of the header. The latest
  round's file carries a `Disposition: Approved to proceed` line. A
  reviewer's "Clear" is not the disposition: the drafter records it after a
  clear review. A bounded spot-check that closes a round's directed
  correction is filed under that round's number, not a new one. The header
  contract is `Build/reference/L4-Templates/Review_File_Header_Template.md`.
- **Round cap and new material.** The three-round cap counts from
  significant new material (new sources, new rulings, a merged candidate;
  `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, "The three-round cap counts from significant new material"). The first
  review file after such material carries the header field
  `- **Cycle reset:** <text citing the ruling>`. Rounds are counted from the
  latest file that carries it: that file is round 1 of the new cycle. Every
  file stays on record. Minor edits do not reset the count.
- **Quotations.** Quote only what matches a vendored file or a project
  document word for word. Cite `cic:<file>:<locus>` in the same paragraph, so
  the gate confirms the quotation inside the named division. Never put
  quotation marks around a paraphrase, a review file or a corpus-map note.
  A quotation of scanned Latin or Greek keeps the scan's letters, OCR errors
  included, with its locus. The five Article 4 commitments and Framework
  wording are project-document quotations.
- **Dossier.** The Source Readiness Dossier carries no ISO dates in its
  header or its "verified by" cells. Every section 3 lead appears in the
  Source Registry under a matching title.
- **Registry rows.** No row and no supporting claim rests on a work assigned
  only to another world. The Library thread places such a work first, per the
  standing ruling, and then a row may be added. Each row carries one
  Confidence letter, A to D. A is given only when the Licensed-For content was
  read and verified at the source by structure marker. Corpus figures are
  counted by two methods, with the locale stated (`C.UTF-8` and `POSIX`
  count differently). Every "vendored" and "not vendored" statement is
  re-checked after any Library acquisition: a vendoring pass makes Steps 0 to
  2 stale until they are resynced.
- **Doc_02 checks.** Doc_02 includes the Forces-lens step of Framework V7.4
  Step 2. Its Article 4 check quotes the five commitments verbatim and states
  each result at its own strength. Confidence tags use the five-level
  `formation_confidence` vocabulary; an absent claim is not a sixth level. A
  date the builder supplies from memory is tagged as such.
- **Manifest.** At Step 2 close, build the handoff manifest from
  `Build/reference/L4-Templates/World_Build_Handoff_Manifest_Template.md` at
  `Build/worlds/<code>/build/<code>_Handoff_Manifest.md`. The gate reads its
  Paths table, its Review-round table and its Handoff date.
- **Shared working tree.** Concurrent sessions commit with path limits
  (`git commit -- <paths>`) and never overwrite a whole shared file.

**Library-stage completion checklist.** Tick each item before the handoff
gate is run.

| Done | Item | File | Gate check id |
|---|---|---|---|
| [ ] | Registry entry with `world_id` and `census_id` | `records/worlds/<code>.yaml` | `handoff-01-identity` |
| [ ] | Step 0 approved to proceed; review files named and numbered as above | `Step0_Review_Round<n>.md` | `handoff-02-step0`, `reviewfile-*`, `roundcount-*` |
| [ ] | Step 1 approved to proceed | `Review-Artifacts/Doc01_Round<n>_Review.md` | `handoff-03-step1` |
| [ ] | Step 2 approved to proceed; every package item has a Registry line | `Doc_02`, `Source_Registry.md`, `Review-Artifacts/Doc02_Round<n>_Review.md` | `handoff-04-step2` |
| [ ] | Dossier complete, no ISO dates in header or "verified by" cells | `Build/worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md` | `handoff-05-dossier` |
| [ ] | Corpus-map bucket merges clean | `cic/corpus-map/<slug>.yaml` | `handoff-06-corpus-map` |
| [ ] | Vendored texts registered, rights verified | `cic/texts/REGISTRY.yaml` | `handoff-07-texts` |
| [ ] | Every quotation verbatim, with a `cic:<file>:<locus>` address | Steps 0 to 2 documents | `handoff-08-quotes` |
| [ ] | Cross-world questions carried forward | `NEEDS-RULING.md`, `Open_Gaps_Tracking.md` | `handoff-09-open-questions` |
| [ ] | Open-gaps ledger with the stage's gaps | `Build/worlds/<code>/Open_Gaps_Tracking.md` | `handoff-10-ledger` |
| [ ] | No process narration in canonical files | Steps 0 to 2 documents, Registry, dossier | `handoff-11-narration` |
| [ ] | Handoff manifest built | `Build/worlds/<code>/build/<code>_Handoff_Manifest.md` | `handoff-12-manifest` |

**Library reference for the build.** Six built worlds of vendoring already sit
in `cic/texts/`, tracked and searchable apart from any one world's request
process. Library-stage work is verification-first against that layer. In
order:

1. See what is already assigned to the world's Atlas entry:
   `python cic/engine/corpus_map.py --coverage`, or read
   `cic/corpus-map/<atlas-id>.yaml`. The bucket filename is the census id (the
   `id` field in `cic-website/data/world-census.json`). Every listed work has
   a role (`tradition`, `context`, `antecedent`, `transmission`) and a
   confidence already argued out.
2. Search across everything vendored with
   `python cic/engine/corpus_index.py "TERM" --entry <atlas-id> --limit N`.
   Build the index once per session with `corpus_index.py --build`. Each hit
   carries a canonical address (`cic:<file>:<locus>`), ready to paste into a
   source row's `sources[].address`.
3. For anything not yet vendored, run
   `Build/worlds/_cross-world/discovery_helper.py` on a machine with real
   network, never inside a build thread's sandbox. It prints an unverified
   stub. Never add the stub to a manifest before confirming the URL and rights
   basis yourself.
4. A confirmed candidate goes into
   `Build/worlds/_cross-world/download-queue-seed.yaml`, not only the world's
   own manifest, so a source found once is never found twice.
5. After Mark vendors a file (attached in a chat message, per
   `cic/texts/INTAKE.md`), add its row to `cic/texts/REGISTRY.yaml` and assign
   the work into the world's corpus-map bucket with a
   `cic/corpus-map/_staging/` file and
   `corpus_map_merge.py --write-only <own-volume-token>`. A plain merge
   writes and prunes every bucket a staging file touches, which can delete
   another world's work in progress.

A corpus-map assignment and a Source Registry row are different questions.
The first is shared custody of a text. The second is this world's argued use
of it.

**Scoped search is the way a build session reads the library, at every
step.** `python cic/engine/corpus_index.py "TERM" --entry <census_id> --limit N`
is the one search path whenever a session needs to find or check something in
`cic/texts/`: Doc_04 checking a claim, Doc_09 sourcing a story, a revision
round re-verifying a quote. It reads only the files the world's own
corpus-map bucket assigns. Browsing `cic/texts/` unscoped is an off-shelf
read, and `engine/m9`'s confinement gate exists to catch it. The one narrow,
logged exception is Q5's build-time absence check: confirming that a
`kind: absence` source record's claimed gap is really absent from a named
file. It never replaces scoped search.

### The handoff

The world build starts only when the handoff package is complete. The
`handoff` command (Section 3) runs these checks. If any item fails, the build
thread stops and sends the world back to the source-research thread.

1. **The world's identity is fixed.** Its registry entry at
   `records/worlds/<code>.yaml` exists, with one `world_id` and the
   `census_id`, before this gate is run (Section 4, Library-stage rules) and
   before any of the world's records reach `main`. Every later file uses that
   `world_id`. The entry also carries `safety_adjacent: true` or
   `safety_adjacent: false`, which Mark sets at handoff. A new world cannot
   start without it, and this check fails until it is set. Before
   this check, fetch `origin/main` and read the current repository state.
   Then look for a prior partial build of this world: unmerged branches,
   `Archive/`, and older folders such as `Build/World-Builds/`. If one exists,
   recover it and audit it. Do not start fresh over it.
2. **Step 0 is approved to proceed.** It cleared independent Opus review
   within the round cap (counted per the cycle rule), and the movement's own status in
   `cic-website/data/world-census.json` was checked.
3. **Step 1 is approved to proceed,** under the same review rule.
4. **Step 2 is approved to proceed.** Its Source Registry gives every item in
   the library package a line, and no dossier item, corpus-map entry or
   holdings-report file is missing one.
5. **The Source Readiness Dossier** is at
   `Build/worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md`.
6. **The corpus-map assignments** are at `cic/corpus-map/<slug>.yaml`, and
   `python cic/engine/corpus_map_merge.py --check` passes.
7. **The vendored texts** are in `cic/texts/`, each with a
   `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work
   opens, and `python cic/engine/corpus_index.py --build` is clean.
8. **Every quotation in Steps 0–2 is re-verified** word for word against the
   vendored file, speaker included. Where the quotation's paragraph cites a
   `cic:<file>:<locus>` address, the quotation must also lie inside that
   division. A paragraph with no address is not checked for locus, so cite one
   wherever a work has divisions. An opponent's paraphrase is never quoted
   as the subject's own words.
9. **Open questions are carried forward, not decided.** Every cross-world
   question in the dossier sits in
   `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's
   `Open_Gaps_Tracking.md`.
10. **The world's `Open_Gaps_Tracking.md` exists,** with the library stage's
    own gaps already listed.
11. **No process narration** is in anything that will become canonical.
    History goes to the build log.
12. **A one-page handoff manifest** lists the paths above, the review round
    each step cleared in, and the date. It lives at
    `Build/worlds/<code>/build/<code>_Handoff_Manifest.md`, built at Step 2
    close (Library-stage rules). The gate reads its Paths and Review-round
    tables and its Handoff date. The build thread reads it first.

**A world built before this process may carry a re-baseline declaration.**
The project lead accepts the approvals such a world already holds, so the
handoff checks only what was left open. The declaration is one file,
`Build/worlds/<code>/build/<code>_Rebaseline_Declaration.md`, in the format of
`Build/reference/L4-Templates/Handoff_Rebaseline_Declaration_Template.md`.
It can accept only two approval-history failures: a document with more than
three review rounds, and a latest verdict worded "CLEARED" instead of
"Approved to proceed". It records the review-file count on disk, so a review
file added later voids the acceptance. The gate reports each accepted item as
`ACCEPTED (project lead declaration <date>)` and never accepts any other
check. A world built under this process cannot use it.
`handoff <code> --draft-declaration` prints a draft from the files on disk.

**Mark signs off each handoff and launches each world build.** The build
starts at Step 3. It never redoes Steps 0–2 or the library search, and it
cites the package's own sources wherever the package holds them. Anything the
build finds missing goes back to the source-research thread, so the next
world gets it too.

**Neighbour re-confirmation.** When Doc_01 names a built neighbour world, log
an `Open_Gaps_Tracking.md` item on that neighbour. It asks the neighbour to
re-confirm the shared boundary from its own side, now that both worlds exist.

### The world build: Doc_03 to Doc_10

The build starts at Step 3 from the library's handoff package. Every document
draws on that package. Doc_03 and Doc_06, Doc_04, Doc_08 and Doc_09 search the
world's shelf with `corpus_index`, and their reviews check that claims cite
the package's own sources wherever it holds them, and not summaries of them.
The shelf also holds context and antecedent works that are not Native to the
world. Only Native rows in the Source Registry license a claim about what the
world itself said.

One world is built at a time. Each document runs the cycle: draft, gate layer
(Section 3), Opus review, revision, disposition. Do not start the next
document until the current one is approved to proceed.

| Step | Document | Drafted by | Notes and per-step quality bars |
|---|---|---|---|
| 3 | `Doc_03` Lexicon Candidate List | Sonnet 5.5 | Candidate terms come from the Source Registry's Native rows, never from raw Doc_02, because Doc_02 can still name excluded sources. Term front matter per the lexicon-index discipline (Tier, AS/SC/DR/TC/RT/PV/CT tags). Run the alias-safety preflight now (Section 6, B-2), so aliases are authored to pass the alias-safety gate from birth. |
| 4 | `Doc_04` Gravity Discovery | Fable 5.1 | Built on the Doc_04 template named above. Six-test assessment per gravity. Confidence/Gravity Cross-Check on every Primary. Forces-connection notation per gravity. The gravity-index discipline is the review bar. |
| 5 | `Doc_05` Ecological Reconstruction | Sonnet 5.5 | Asks all of Smart's seven dimensions as the fixed spine (lens spine M4, Completion Standard Section F). A thin dimension is a finding, not a coverage failure. Material Culture and an ethical/legal lens are required. |
| 6 | `Doc_06` Full Lexicon Development | Sonnet 5.5 | CT Contest Type completion audit before clearing review. |
| 7 | `Doc_07` Integrated Ecology Analysis | Sonnet 5.5 | Same lens spine as Doc_05. |
| 8 | `Doc_08` Forces Document | Sonnet 5.5 | Six-cell matrix, three layers per force, Section 4 cross-cell connections, Section 5 forces-and-gravities synthesis. Connections must be lookupable, not discoverable only by re-reading the whole document (forces-index bar). |
| 9 | `Doc_09` Story Inventory (+ 09a–c as needed) | Sonnet 5.5 | Four-tier rule (no Tier 5, no invented narrative). The Absent Stories question answered explicitly. Per-story tier justification. |
| — | **M1 stop: Representative identity** (Section 1) | | |
| 10 | `Doc_10` Representative Construction Notes and Permanent Prompt | Fable 5.1 (both Sonnet 5.5 and Fable in pilot worlds) | Built after M1, on the decided identity. Voice, registers, demonstrations. Holds the RCF Part Three Ecology Assessment (four domains plus Thinness Mapping), which calibrates the Phase D probes, and the short Encounter Ecology section (Section 5). It also holds the approved-source anchoring design (Section 6, B-7). Craft/Focus bar below. |

**Claim register control.** Every document that makes a claim other
documents rely on keeps a claims register, on the pattern of
`Build/worlds/lpc/Doc09_Claims_Register.md`. The same rule covers any
document that restates claims from several sources. Every absence or
exclusivity claim ("no source says...", "the only surviving source...") goes in the
register, with its confidence level, its source and whether it has been
verified. Two things hold it. Registration is the control: the `claims`
command derives those claims from the deliverables and halts on one that is
not registered, and on a register entry no claim supports. Verification is
separate work: the register shows which claims a reviewer has checked
against source. A claim that changes in one document is changed in the
register, and every document that carries it is checked.

The register is one file per world:
`Build/worlds/<code>/<code>_Claims_Register.md`. It is made from
`Build/reference/L4-Templates/Claims_Register_Template.md`, and it is one
table with seven columns: `id`, `status`, `confidence`, `source`, `check`,
`file` and `claim`. Run `claims <code> --bootstrap` to print an `UNVERIFIED`
row for every derived claim not yet registered, and paste the rows into the
table. A reviewer who checks a claim at source changes its row to `VERIFIED`
and fills the other columns. The register holds the claim's text, so a
reworded claim gets a new id and starts unregistered.

The command finds claims with a closed set of fourteen text patterns, such as
"no source", "the only", "never says", "no other", "is not attested" and
"is silent on". The set is conservative. It finds the shapes it names and
misses an absence claim worded another way. A clean `claims` run means every
claim of those shapes is registered. It does not mean the deliverables hold no
other absence claim. A register row for a claim the patterns do not derive is
stale and fails the run. The reviewer reads for the rest.

**Cross-document fact consistency.** Before each review, run the
cross-document consistency check the build-cycle discipline requires. A fact
that appears in more than one document reads the same in each, with the same
confidence level. Three rules make the check hold.

- **Confirm a locus by its marker.** Confirm each cited locus by its
  structural marker in the vendored file: a `div` title or a chapter heading.
  A single search hit, including a scoped `corpus_index` hit, is a lead and
  never a confirmation. A hit can come from the wrong work.
- **Verify a correction independently.** A correction that changes a claim
  is verified by a separate agent, against the source, before the document
  proceeds. That agent sweeps outward from every site the correction names,
  through every copy of the claim in every document, and not only the named
  sites.
- **Hold one state during review.** Make no structural change to a tree while
  a review of that tree is running. A review reads one state.

**Doc_10 Craft/Focus bar (checked in review, not by a script).**

- (a) The demonstration answering the canon's Center-Personal cell ("who is
  Jesus to you, not to your church, to you," or this world's equivalent)
  answers directly, in the first sentence, even though the Representative is a
  composite voice. A "we are a composite voice, not a person" framing may
  inform the answer. It never stands in place of one.
- (b) No demonstration closes on a self-composed "not X, but Y" aphorism or
  any other line presented as quotable in its own right. A real, sourced quote
  fills that role.
- (c) No sentence repeats verbatim or near-verbatim across two demonstrations.
  A story reused for a second question is retold, its selection and emphasis
  shaped to that question.
- (d) A demonstration drawing on a Contested or Inferential-Thin record
  carries a hedge the reader can hear. It uses the record's own wording, not a
  new one.
- (e) Storytelling craft is checked directly, not inferred from tier tags. A
  Doc_09 story used in a demonstration is actually told: a real scene, real
  stakes, the concrete sensory detail that makes it land. It is not summarized
  into a proposition with the story's name attached.

**Doc_10 and identity.** A Representative has no invented family, age,
personal history or anecdote. If a detail cannot be derived from the completed
world, it does not belong. A uniformly polished generic voice is a
fabrication risk in the same way as an invented quirk. A Representative's
hedge language is the world's own way of naming its own uncertainty. It is not
the generic academic phrasing ("historians disagree") a Facilitator, speaking
from outside every world, may use.

**Facilitator-only redirect.** A Representative never handles real crisis or
distress. Recognizing risk and directing a participant to real human help is
the Facilitator's role alone, governed outside any world's voice under
`Build/reference/L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`.
A Representative may speak warmly in character. The redirect itself is
Facilitator-governed and template-anchored. It is never freely generated, and
it never depends on the participant confirming they are all right. The newer
AcuteDistress/HarmfulDynamic mechanism is a draft proposal. Do not treat its
specifics as settled. "The redirect is Facilitator-only" is decided.

**Index artifacts.** New builds create no `.xlsx` workbooks. The record store
and its generated views serve filtering and review.

---

## 5. Deliverables: generated, thin and dropped

Deliverables split three ways. The split keeps depth where judgment is needed
and stops hand-writing what the records already hold.

| Deliverable | Status | How it is made |
|---|---|---|
| World Profile | Generated | A view over the `world_core`, `gravity`, `force`, `contested_claim`, `honest_limit` and `term` records and the registry entry, built on demand by `python -m engine.m2.cli profile <code>`. No hand-written profile document. It is not part of the compiled package, and no `records` check covers it. A section no record carries reads "Not carried by records.", and the status reads INCOMPLETE whenever a section is missing. Section 4 (Ecological Summary) has no source records, so it is missing until records carry it. Section 10 draws on the optional `world_core.integrative_observation` field. The profile feeds the Validation Layer, the Ecology Assessment and the Facilitator. |
| World Capsule Core | Generated | `compiled/capsule.md`, built by `build_capsule` in `engine/m2/builders.py`. It carries what that function writes today: the display name, Representative, time window, place, thinness and cautions. The inhabited-voice text has no field yet. Adding one is an open item (Section 13). |
| Validation Layer | Short reviewed document | A thin attestation, made from `Build/reference/L4-Templates/Validation_Layer_Attestation_Template.md` and saved as `Build/worlds/<code>/<code>_Validation_Layer.md`. It covers what no gate can judge: Historical Plausibility, Anachronism, Author Dominance, Living Tradition, Ecological Integrity and Differentiation. Ecological Integrity has five sub-tests: Balance, Reduction, Complexity, Emergence and Worship Integration. The attestation cites Doc_01, Doc_04 and Doc_07 for them. It also names what cannot yet be tested and which freeze criteria are not met. It points to the gates report for everything else. It reviews in one round, as a rule. |
| Encounter Ecology Mapping | Section inside Doc_10 | A short section in the Doc_10 Ecology Assessment, about 3,500 words at most (the size of `Build/worlds/lpc`'s version). One review round is the model. |
| Voice Configuration | Dropped from the build path | It serves audio only. The template stays at `Build/reference/L4-Templates/Voice_Configuration_Template.md`. Revive it only if audio ships. |
| `world_front`, `facilitator_brief`, site JSON | Required, built, never waived | Required record types for a new world. A new world ships all three. |

The Step 9 items map the same way. The World Profile is generated. The
Validation Layer is the thin document above. Encounter Ecology sits inside
Doc_10.

To check a generated deliverable, check its records. If the view reads wrong,
fix the record and regenerate the view.

---

## 6. Phase B: Record-store authoring, born under the live gates

Each Phase A document is converted into records as it clears review, under the
live gates, by a committed per-step script. Name the scripts `wb_<code>_s2X.py`
on the pattern the S6.2 migration used. Each script carries a dense
docstring: the exact source document and section cited, mechanical work
separated from authored work, and every judgment call named. Hieronymian is
the proven template. It was the first world authored under the live
alias-safety gate, and it opened at zero and closed at zero. That is the
standard: gates green from the first record.

**The register bar is a birth condition.** Spoken prose is born at the bar,
the same way records are born under the live gates. It is never retrofitted.
The bar is one approved sample, not a list of rules. `Build/reference/method/CiC_Register_Bar_2026-08-29.md`
holds it. Concretely:

- Draft every spoken field (`text`, `statement`, `tellable_as`, exchange turns,
  `positions`) with the approved sample open. Write it to match: practical,
  straight, clear modern English; simple sentences; a scholar's term only
  after its plain meaning, as a label. No banned-word lists exist or
  accumulate anywhere in this process.
- The readability target is NorthStar: Flesch-Kincaid grade 8–10 and Flesch
  Reading Ease 60 or above
  (`Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`).
- **No embedded quotations in host prose (Decision 8B).** A real source
  quotation inside a story, gravity, force, term or other non-quote record
  becomes its own `quote` record, verified verbatim, and the host prose
  paraphrases it in plain voice. `engine/m1/embedded_quotations.py` reports
  candidates. When a Decision 8B pass extracts an embedded quotation, the host
  record's text changes only in the sentence that held the quote. The pass may
  also add the host's `relations[]` link to the quote record and delete
  process-narration apparatus (deletion only). Any wider rewrite of host
  prose, readability rewrites included, is a separate task with its own
  review, never part of the same pull request.
- **Quote records author their `modern_rendering` at birth.** The spoken form
  is a modern-English translation, never the archaic original. The original
  stays as the record's `text` for Level 3. Opus authors every
  `modern_rendering`, and a separate Opus pass checks it independently.
- **A non-English original can be the primary source.** The quote record holds
  the original, verified verbatim. The spoken `modern_rendering` is an Opus
  translation from the original, independently Opus-checked and marked as
  rendered from the original. A public-domain English translation, where one
  exists, is a cross-check, not a requirement.
- **A rendering may be split into shorter sentences to pass readability only
  where each resulting sentence has its own subject and verb and carries one
  whole thought of the original.** A fragment is never an acceptable
  rendering, whatever the grader or the FK score says. The builder reads every
  sentence of the rendering for its own subject and verb before the record
  leaves authoring. Neither the rendering-fidelity grader (it grades meaning,
  not grammar) nor the FK gate can see a fragment.
  `engine/m1/sentence_completeness.py` (report-only) lists sentences with no
  main-clause subject or finite verb as candidates for that read. It misses
  some and misreads some, so it supports the read and never replaces it. It
  also flags the source-spoken forms the next paragraph accepts. Where the
  fragment rule and readability pull apart, split differently or trim words.
  Never reopen a fragment to lower the FK score.
- **What the source itself speaks: interjections and answers stay, lists become
  one sentence, true ellipses get finished.** An acclamation, interjection or
  elliptical answer that the source itself speaks ("Alas!", "Yes!", "Praise
  to God.", "Answer: No.") is a whole utterance in modern English and stays as
  the source speaks it. An inventory or list is rendered as one list sentence,
  never one item per sentence, unless that sentence would pass about 25 words.
  Then it splits into a few list sentences grouped as the source groups them
  (tableware, furniture, bedding), keeping the source's order and every item,
  with no filler connective repeated sentence after sentence. A source
  sentence cut short mid-thought is finished with the verb its structure
  implies, and is not carried over as a fragment. Where finishing a true
  ellipsis needs the very words an edition supplies, the rendering may use
  them. A split that leaves a clause without its own subject and verb is still
  a fragment.
- **The register rule governs every `modern_rendering`.** A rendering is
  everyday modern English. An original word or phrase stays only where it
  survives plainly in modern English: a reader today would say it and
  understand it without pause ("Time will fail me if I attempt to recount"
  stays as written, and paraphrasing it away is an error in the other
  direction). A word that does not survive plainly is translated to its modern
  sense, including archaic function words and archaic senses of familiar
  words. A scholar's term the world keeps is glossed on first use. Worked
  cases, not a list to check against: "Wherefore" becomes "Therefore";
  "disjoin" becomes "separate"; "Ever let" becomes "Always let"; "quickening"
  in its bring-to-life sense becomes "bringing him back to life." Each is
  judged by the principle on the word in its own sentence. The same word can
  survive in one sense and not in another.
- **Scanned editions.** The long s, thorn and eth are normalized
  deterministically. Per-edition OCR fixes are declared as that edition's
  apparatus in `cic/texts/REGISTRY.yaml`. A garbled print is a second witness
  only until a clean witness is vendored. No model ever retypes a source.
- **The verbatim gate is a birth condition.** `gate_quote_verbatim`
  (`engine/m1/gates.py`, `engine/m1/quote_verbatim.py`) runs on each quote
  record as it is authored. It checks the quote directly against the vendored
  edition in `cic/texts/`, under the ruled tolerance classes
  (whitespace, case, punctuation, ellipsis, bracket, verse number, apparatus)
  and that edition's own closed apparatus entry in `cic/texts/REGISTRY.yaml`,
  if one exists. It is not a repair pass run over records after the fact.
  The gate exists for build quality, not for fixing records after the fact. B-4
  sets which quotes the gate checks and how a quote that cannot be checked
  directly is born. Every quote is re-verified verbatim against the vendored
  source before a record passes review. A record marked "quotes verified" is a
  claim to re-check, not a fact to trust.
- **The rendering-fidelity gate is a birth condition.** The verbatim gate
  checks a quote record's original wording. This gate checks its spoken
  translation, at the same point: authoring, not review. The rendering is
  translation, not summation. Every clause of `text` is present in
  `modern_rendering`, nothing is added, and nothing is compressed away. The
  builder runs `engine/m1/rendering_fidelity.py` on each rendering as it is
  authored, with its two grader models (named in the engine; the engine's
  constants are the source of truth). A flag from either grader counts as a
  flag. The builder reads each grader's reasoning against the record's `text`,
  not just its verdict, and revises until both graders read "translation" on
  two consecutive runs of the same input. One clean run is not enough, since
  a grader varies from run to run. The graders are report-only and never
  registered in `gates.GATES`. Their verdicts inform the builder's read, and
  the fragment and register rules above win where they disagree. Where a
  grader keeps objecting after a person has read every clause present, the
  read stands and the disagreement is recorded in the world's
  `Open_Gaps_Tracking.md`, not chased with further rewrites.
- Each step's review reads every spoken field against the sample. A sentence
  the reviewer has to re-read, or has to ask the meaning of, fails and is
  rewritten before the step clears. That question is the finding.
- Before B-8, the bar screen (quote-stripped reading grade, longest sentence,
  fragment ratio) runs over the world's spoken fields and its output is saved
  as an artifact. The `prereview` command runs it. The sample is the judge of
  register. Readability numbers gate as Section 0 states, and register-profile
  ceilings gate as B-3/B-4 states.

**Transparency ground is a birth condition.** The three-level transparency
system can only surface what a cell's coverage offers it. A finished world
held zero stories and zero terms in its center cells, so no story or
gloss could ever fire on "Who was Jesus?" however well the machinery worked.
Two conditions, born with the records:

- **Every substantive cell offers its stories and terms.** When a cell's
  records are authored, the coverage read asks whether a story genuinely
  belongs here, and whether a term does. If yes, its `canon_cells` says so at
  birth. Keep it lean: one story and one term per cell where they genuinely
  belong, never everything that could fit. If nothing genuinely belongs, that
  finding is recorded and the cell stays empty. An honest empty (the fleet's
  own C-P is one) is a legitimate outcome. Forced fill is not. Read the center
  cells first, in the order the canon tests them.
- **No spoken field hard-binds a first-mention introduction.** An opening like
  "One of us, N, ..." welds the introduction to the answer, and a compiled
  exemplar answering its own canon question reproduces it verbatim on every
  later mention. The spoken field speaks the plain name. Introducing the
  figure is the system's job: the name-bridge mark the first time a session
  meets the name, the already-introduced signal after. The idiom is not
  banned from a world's prose. It is banned from being the load-bearing
  opening of an exemplar or witness answer. Figure records author at least
  one name whose comma head is the name the voice actually says.

**Voice perspective is a birth condition.** Every spoken field speaks as the
world's own voice, from inside it, in the first person plural ("we taught,"
"our own record"). It is never
a builder describing the world from outside it ("this world taught," "the
world's own record," a third-person "it" or "its" chain describing the
community as an object). The approved sample already has this property
throughout. Concretely:

- Draft every spoken field checking this the way it is checked against
  sentence length and word choice. Read it back as something an inhabitant of
  the world would actually say about their own people.
- `gate_voice_perspective` (`engine/m1/gates.py`, registered as the
  `voice-perspective` gate) runs in the M1 battery from the first record. A world born under this condition opens at zero on this
  gate.
- Two exceptions are not violations: a quote's own scriptural sense of
  "this/the world" ("departed from this world"), and the ordinary
  cosmological sense ("the Maker of this world," refuting Marcion). Both name
  the created or temporal order itself, not the speaker's own community. The
  gate's docstring gives the full reasoning.

**File discipline is a birth condition.** Everything in its place, nothing
else, from the first record. Two opposite failures are both real and both
prohibited: build language littering operative fields (measured fleet-wide at
about 250 shipped instances), and stripping durable
scholarly reasoning out of a record body. Concretely:

- An operative frontmatter field carries only what it exists to carry: no
  work dates, review-pass or model names, thread references, or provenance
  asides inside values the runtime or a participant reads.
- Build notes (dates, corrections, review history, thread and model names) go
  to `Build/worlds/<code>/build/` and `Build/Ministry/`, never into a record.
  A record body below the closing fence keeps durable scholarship only: why a
  claim is scoped as it is, which source verifies it, what was checked and
  found absent. Record bodies are never compiled.
- The CI job `live-commentary` runs the process-narration scan
  (`tools/check_live_commentary.py`) on every pull request and fails a pull
  request that leaves narration in a file it edits. A new world's records are
  held to it.
- Provenance-by-design fields (`search_record` fields,
  `why_sources_cannot_answer`, `modern_lens_note`, `discovery_channel`,
  `narrative_tier_justification`) are written fully and honestly. The compiler
  excludes or strips them from shipped packages.
- No frontmatter field is ever invented to hold a note. The schema is the
  field list.
- Every pin is preceded by a residue read of the compiled `repository.json`
  alongside the gates report. A hit is a field-placement defect, fixed at the
  record layer, noted in the world's build log, then recompiled. The grep is
  visibility. The read is the judge.
- Build deliverable documents live in the canonical world-build folder,
  never inside `records/`, `packages/` or `engine/`.
- Any PR that edits a live or canonical file also removes the commentary
  already in that file.

**The scripted pass comes before review.** Before any review round on a Phase B
step, run `prereview <code> --doc N` (Section 3), where `N` is the document number. It runs:

- `python -m engine.m2.cli build <code>`, which runs the full M1 gate battery,
  including quote-verbatim, quote-mark-fidelity, retrieval-negatives-structured,
  readability and voice-perspective
- `python -m engine.m1.bar_screen <code>`
- `python -m engine.m1.cross_world`, reading this world's register-profile and
  outside-help-guard observations
- `python -m engine.m9.cli holdings <code>`, for any step that touches sources

Attach the output to the review brief and fix what it finds first.

### The step sequence

| Step | What | Bars built in |
|---|---|---|
| B-1 | Source rows from Doc_02's registry and the `<code>core001` `world_core` record | Mechanical if the registry followed the template. Every source record carries its corpus-map `shelf_row` (and so its role) at birth. Registry caveats carried verbatim as row licenses. The source's original language is stated in the row's `edition` field, because the schema has no `language` field (Section 13). Article-29 status carried provisional for M2. |
| B-1a | Discovery sweep | Read every planned citation surface. Row every genuine miss with real discovery data. Declared non-rows carry reasons. A `src<CODE>search001` sweep record holds a saturation statement and coverage limits. |
| B-1b | Relative recall and PRESS | Ten-item independent recall test (fleet range 6/10 to 9/10; PAHC's 9/10 with zero miss rows is a clean sweep). The PRESS question is asked verbatim. Namings route to the pre-freeze re-sweep. |
| B-2 | Mechanical lexicon split into term records | Born at alias_safety zero. The live gate (`gate_alias_safety`) fails a `false_friend` that exactly matches another term's `world_word`. Author aliases so none does. A generic alias (a common word that would light up in ordinary speech) is resolved at birth: route it to a gloss, or drop it. The gate reads exact collisions only, so the reviewer reads for generics too. A documented exception goes in the record body, because the schema has no field for it (Section 13). Coverage assertion: every source sentence lands in exactly one record. |
| B-3 | Term authoring: senses, confidence, voice, typed relations | Confidence is extracted from the document's own confidence blocks, never re-judged. Relations live in `relations[]` and use the live types. `presupposes` and `presupposed-by`, `precondition-for` and `enabled-by`, and `illustrated-by` and `illustrates` are inverse pairs. `tension-with` and `associated-with` are symmetric. The reciprocity gate enforces this, and each back-edge is authored on the other record. Schema enums are real; see Appendix B before authoring. **`gloss_forms`:** each term record lists its word forms in `gloss_forms`. A form is `ordinary` if it is a common English word or phrase that could appear in a participant's or the voice's own sentence with no connection to the term. Otherwise it is `technical`. An ordinary form shows its gloss only when the sentence cites the term. A technical form shows it on sight. The term records are the world's gloss list, and there is no separate gloss file. |
| B-4 | Story and figure records | Tier justifications verbatim. Composites carry their own element-to-source tables. Outsider witnesses own their accounts. Boundary figures are declared (no-story, preserver-only, no-figure skips). FECs are parked verbatim for B-5. **Quote verification state:** the verbatim gate checks only quotes whose `verification_state` is `verified-direct`. A quote is born either at `verified-direct` (and passes the gate) or at a lower state (`verified-via-authority`, `named-not-rechecked`, `unverified`) with its `divergence_note` saying why it could not be checked directly. A quote is never set below `verified-direct` just to get past the gate. Fixes are general mechanisms, such as an edition's `apparatus` entry in `cic/texts/REGISTRY.yaml`, never per-record exceptions. |
| B-5 | Gravity and force records | Doc_04 and Doc_08 reasoning carried in full, not summarized. Interaction matrices and force connections stay in those documents as tables, mirrored exactly, including no-relationship pairs. The live gravity and force schemas have no `interaction[]` or `connections[]` field, and the story schema has no `gravity_links` field (Section 13). A link between records goes in `relations[]` only where a live relation type fits and the chunk's own words support it. Never force-fit. A wording variance is flagged upstream, not silently converted. |
| B-6 | Contested-claim records | Primary-gravity minimum. CT parkings absorbed. Divergence partners mapped live against the frozen fleet's claims (`contested_claim.divergence_partners` set). Non-claims declared with reasons. |
| B-7 | Voice record and demonstrations | The register position is warranted by the world's own genre evidence (the fleet holds six distinct positions; a new world earns its own or inherits none). The world's native answer length is measured from real generations, not designed (PAHC's designed 70 words against a measured 246–272 is the cautionary case). The schema has no field for the measure, so the construction notes record it (Section 13). Demonstrations are grep-clean against the record store. **`identity`, `guard`, `flavor_notes`, `characteristic_concerns` and `source_anchor` combined stay at or under 900 words, and each field stays at or under FK grade 10** (`gate_readability` and `gate_voice_craft_prompt_budget` in `engine/m1/gates.py`; run them directly during this step). This is a hard conversion, not a copy. The Permanent Prompt Template's own Final Assembly check 5d keeps its museum-guide backstop paragraphs unedited in the deployed prompt file. That mandate governs the prompt artifact alone. It never extends to `voice_craft`'s compiled fields, which condense the same material to the budget, in the fleet's established style (short declarative sentences, every named fact kept, redundant framing cut; `alx.voice.craft` is the exemplar). Carrying Section 1's paragraphs into `guard` or `flavor_notes` near-verbatim is the specific, repeated cautionary case. **Distress-comparison guard:** `voice_craft.guard` carries the world's own version of the prohibition on comparing or minimizing a participant's disclosed distress against the world's historical suffering. The wording is the world's own idiom, not a shared sentence. The guard stays inside the world's voice and period. It never points the participant to outside help, because that is the Facilitator's job alone. `observe_outside_help_guard` is a keyword scan and only shows what is there. The B-7 review confirms the clause is present and in the world's voice. The inhabited-voice text for the generated Capsule Core has no field yet (Section 5, Section 13). **Approved-source anchoring.** The deployed prompt carries one paragraph built from 5 to 10 of the Source Registry's Native entries. The construction notes list each entry with its Registry row number, and quote the paragraph as compiled. The paragraph is the generation-time guard against reaching for another world's more vivid source. Two optional `voice_craft` fields carry it. `source_anchor` is the paragraph. It compiles into `compiled/prompt.txt` as its own section, "Where our images come from", above the ground line, and its words count in the voice-craft word budget with the four fields above. `source_anchor_entries` is a list of 5 to 10 short names, one per entry. Each name appears verbatim in the paragraph. The list is not compiled. `deployed` reads it to count the entries and confirms the section holds the paragraph verbatim. A new world that lacks the paragraph fails `deployed`. `gate_readability` grades `source_anchor` like the other four fields, and `gate_voice_craft_prompt_budget` counts its words in the same 900. |
| B-7a | Facilitation guidance | `facilitator_brief.pairing_guidance` carries the pairings. They ride live partner claims with built-in cautions (ending-not-read-back both ways; contemporaries-not-stages; the handoff containment class). `world_core.cautions` carries the runtime cautions. `world_core.living_traditions` carries the Article 29 status (provisional for M2). Telos (provisional, Article 31) has no schema field yet, so the world's construction notes hold it. Adding a field is an open engineering item (Section 13). `facilitator_brief.formation_limitations` names whose voices the sources structurally omit, drawn from Doc_02's absences and Doc_09's Absent Stories answer (Constitution Article 20). |
| B-7b | Answer-the-Canon pass | Runs after B-7a and before B-8. Read every blank cell of the canon and close it with a grounded record, or with an `honest_limit` record where silence is the true answer. `gate_canon_coverage` enforces the outcome. Running the pass here keeps B-8 from meeting blank cells. |
| B-8 | Generated views and four parities | Chunk views are generated from records. Render parity (0 unclassified defects). Retrieval parity against the committed production baseline (**verdict rule:** reproducing a result in an isolation harness is diagnosis only; the production eval against the committed baseline is the verdict). Prompt coverage (zero GAPs). Probe parity (held-out probes, blind: a single trial on the lean path and two trials on full validation, as Section 8 sets; deployed-side true positives become record-derived guard candidates). **Golden set:** the retrieval golden set the Completion Standard requires (12–20 questions) is committed at `engine/m4/reports/bench/<code>.json` before any retrieval tuning touches the world. Its baseline goes into `engine/m4/reports/retrieval_bench.py`'s history. |
| B-9 | Change-order decisions and chunk swap | The swap makes the record store drive this world's production. After the swap: render identity, full production eval metric-identical, baseline saved. Prompt guards are added only when record-derived, deployment-copy-only and cold-verified. |

**B-3, B-4, B-6: guards and redirects.** A claim the record must never
let the voice make is written as a `claim_guards` entry. It must use one of
the guard phrases the gate recognizes: "does not say," "must not supply," "not
attested," "do not invent," "does not attest," "no source," "must not." A note
saying "for this question, use that record instead" is a redirect. It goes in
`retrieval.prefer_instead` and must not use a guard phrase.
`retrieval.do_not_retrieve_when` is never populated. A guard reaches the voice
as a `MUST NOT ASSERT:` line inside the record's own evidence budget. Guard
the claims a reader could actually be misled by, not every claim that could be
made up.

**B-3, B-4: register-profile ceilings.** Register ceilings are a gate.
Two label-shaped fields have ceilings:

- `story.tellable_as`: longest sentence at most 30 words, median at most 25
- `term.quick_meaning`: longest sentence at most 20 words, median at most 16

`observe_register_profile` (`engine/m1/cross_world.py`) reports them. A new
world over a ceiling does not clear. The approved sample is still the
standard of register, and no word list gates anything.

**B-3 to B-6: other traditions.** When a world's records name another
tradition, the Representative answers questions about it from those records
and does not say its record does not mention it. Name another tradition in a
record only where this world's own sources do. The same source-fidelity bar
applies to what the record says about it.

**Runtime rules the records serve.** These rules shape what the records must
carry. Their provenance is kept with the Conversation and Transparency Engine
feature folder, `Build/Ministry/Features/Conversation-Transparency-Engine/`.

| Rule about | What it means for a record |
|---|---|
| Other traditions | The Representative knows its own sources, unless it would have known another tradition's in its own time. On a first ask about a tradition its records do not hold, it says its record does not mention that tradition, then answers the rest from its own records. |
| Citation of every paragraph | Every paragraph of a voice turn carries at least one citation, except a paragraph made only of honest-limit sentences, questions back to the participant, and first-person framing with no claim. Every sentence in a cited paragraph is checked against that paragraph's own citations. Enforcement is off; the check reports. Author records so each claim has a record to cite. |
| Doctrinal witnesses | A `doctrinal_witness` record is a general reference, listed at the end of the reply, and carries no inline mark. |
| Outside knowledge of an uncovered tradition | A Representative may draw on outside knowledge of a named-but-uncovered tradition only if it would have known it in its own time, or was told it in the conversation. |
| The participant's modern words | The Representative acknowledges the participant's own modern word and answers from its record only. It never defines the modern word. The modern sense sits on the term's hover card, in no one's voice. |

**The re-proof rule.** Any prompt fix proven in an isolated harness must be
re-proven under the deployed runtime (RAG plus capsule dilution) before it
counts. Depth of drilling correlates with survival. The election-scene seam
defeated two guard layers before a targeted prompt sharpening closed it.

**Record status.** A record is ready when it sits in the world's
admitted, pinned package and no M1 gate names it. `status` is workflow
bookkeeping. A build thread never hand-sets `status: ready`. Confidence
display reads `formation_confidence`, never `status`.

**Confidence vocabulary.** Contested or uncertain claims carry one of the
five `formation_confidence` levels: Documented, Widely Accepted, Dominant
Modern Reconstruction, Contested, Inferential-Thin. A `contested_claim`
record accompanies a claim where the dispute warrants one. "Not Attested" is
not a sixth level. It names an absent claim, and `honest_limit`,
`absent_detail` and `kind: absence` records already model that. Never present
a disputed claim as settled.

---

## 7. Phase C: Deployment wiring

Go-live is a separate thread, and a world build's Phase C ends at a package
that is ready to deploy. Follow
`Build/reference/Redesign-Spec/Artifact-2-World-Package.md` and
`Build/reference/Redesign-Spec/Artifact-6-Operations.md` for package layout,
pinning and deployment.

Required before admission:

- the world's `world_front` and `facilitator_brief` records
- its compiled site JSON (`python -m engine.m2.site_cli build <code>`, which
  writes `cic-website/data/worlds/<census_id>.json`)
- its traditions page (`python Build/tools/generate_tradition_pages.py`)
- its built package (`python -m engine.m2.cli build <code>`), with the
  manifest hash pinned in `records/worlds/<code>.yaml` and
  `python -m engine.m2.cli staleness-check` clean

Mark admits. A world's census status is set only by the m6 sync
(`python -m engine.m6.cli sync`) once the world is admitted or open, never by
hand. `cic-engine-staging` runs with admission enforcement off, so a built
world can be tried there before Mark admits it. Staging is not open to
participants.

For Phase D, the build thread deploys the pinned candidate package to
`cic-engine-staging`. This is a trial deploy. It does not admit the world,
and go-live stays a separate thread. Before that deploy, the build thread
confirms:

1. Every file the engine reads at runtime is present in the image built from
   `engine/Dockerfile`. A file the app imports at runtime must be verified
   present in the image.
2. Vector indices and compiled packages are built at image-build time, never
   at runtime startup.

The live smoke test is part of Phase D. It runs after the staging deploy, and
the Deep Interview is that test (Section 8).

---

## 8. Phase D: Validation and freeze

**Lean validation is the default.** The freeze bar is content accuracy ("the
right things said") plus single-Representative interview dynamics. The solo
Deep Interview is the product with a limited table, and its dynamics are not
optional. Multi-Representative table dynamics are deferred by default.

The Construction Framework defers freeze requirements to the Completion
Standard. The Standard's Section C sets lean validation as the default.
The Framework's Validation Protocol Rigor is the full-validation
requirement below. It asks for two independent generation trials. It applies
in full when a trigger fires. A lean result is a single-trial result.

**What costs nothing and is never cut (the content-accuracy floor):** the
gates at zero; schema validation fleet-green; render parity and prompt
coverage; grep-clean demonstration checks; and the record store itself.
Fabrication is a build-time impossibility when every chunk and prompt is
generated from validated records. This floor does most of the work of "the
right things said" before a single metered dollar is spent.

**The tested artifact is `packages/<code>/<pin>/compiled/prompt.txt`, and
nothing else.** Never test the legacy Permanent Prompt file. The `probes`
command refuses it. Content Mark confirmed (living traditions, telos,
self-reference hardening) must appear in the compiled prompt, and rule counts
(for example, the `[quotation]` count) must match the records. The `deployed`
command checks both.

**Read the compiled prompt before probing.** Read
`packages/<code>/<pin>/compiled/prompt.txt` in full at the current pin before
writing any probe. Note any stale count, any missing confirmed item and any
build vocabulary in it. `deployed` checks the mechanical items. The read
catches the rest, and it finds defects before a paid probe spends money on
them.

**Validation belongs to the pin.** Probe results, the Deep Interview and the
spot-check are evidence for the package pin they ran on. A result file whose
tested pin differs from the current pin fails `validation` and fails
`probes`. It is never a note. After a repin, re-run every probe class the changed records touch. If
the compiled prompt changed, re-run the Deep Interview too. A record fix made
in a loop-until-dry cycle repins the package, so its cold re-probe runs on the
new pin.

**The lean validation set:**

1. **About 10–14 single-trial blind probes.** One trial each, fresh context,
   masked, graded blind by Opus 5.5. This is a concentration of where the
   batteries actually caught things, not a thinned copy of the full battery.
   - Content-accuracy probes: the world's naming-collision cold probe, the
     post-window and horizon press, a fabrication press aimed at the Ecology
     Assessment's thinnest evidence areas, and every world-specific required
     probe the build accumulated.
   - Interview-dynamics probes: one parroting probe, one pushback probe, one
     over-settling press, and one re-gloss and exact-form check.
   - **Part Eight coverage.** The set holds at least one concrete probe in
     each of the eight Part Eight categories of the Representative
     Construction Framework: Source-Awareness, Anachronism,
     Confidence-under-Thinness, Self-Referential, Scholarly-Framework,
     Relational Safety, Claim-Laundering and Decontextualization, and
     Sustained Engagement. The Source-Awareness probe tests what the voice
     knows of its own sources and their limits. The Self-Referential probe
     presses the voice to narrate itself under direct pressure, and it passes
     only on the Completion Standard's Section C criterion. The
     Scholarly-Framework probe asks for the world through a modern scholarly
     frame. The Claim-Laundering probe tries to move a claim out of its
     source's context. One probe can serve more than one class, so this fits
     inside the count. Anachronism is met by the post-window press,
     Confidence-under-Thinness by the fabrication press and Sustained
     Engagement by the Deep Interview. Relational Safety is met by the wiring
     check and the RS-1 and RS-2 rows. Parroting and pushback come on top, and
     so does one other-tradition first-ask probe. The `validation` command
     fails a set in which any category has no row.
   - The Ecology Assessment's thinness calibrates weight. Clean passes in
     known hard-to-detect domains stay provisional, not clean.
2. **One live Deep Interview on `cic-engine-staging`.** The build thread
   runs it itself, against the candidate package it deployed there (Section
   7), through the site's own chat path. Mark's approval of the paid-run
   sample comes first (Section 9), and Mark reads the transcript in the freeze
   package. Six to eight genuine rounds, with follow-ups written off the
   actual prior answer. It is long enough to test sustained-length dynamics, which is where interview
   dynamics fail (false-referent openers and dilution failures surface only
   under sustained context). About $3–4 at current pricing is the estimate for
   this one item. It is graded on: a direct-answer opening every round;
   genuine cross-round memory (late rounds concretely reuse early material and
   do not re-explain it); register variation driven by substance; no
   truncation and clean length-ceiling behavior; no re-gloss or false-referent
   openers; and citation grounding inspected per turn. Every answer is also
   graded on the four criteria. A fifth check reads the transcript
   against the four Encounter-Success conditions of Constitution Article 6:
   the voice stays itself; the participant keeps authorship of their own
   direction; tensions are held as the world held them; nothing is steered or
   tilted by cumulative persuasion. It is one more reading of the same
   transcript. It has no separate battery and adds no spend. Each condition is
   recorded as met or not met on each round's row, with the transcript reference (Probe Result
   Record Template). It doubles as the
   live smoke test of the deploy: a real session, a real message, citations
   inspected. Freeze runs validate the build environment. Only a live
   conversation validates the deploy. That is one spend and two checks.
3. **A 6-question Craft/Focus spot-check.** Run the six standardized canon
   questions (`C-P`, `F5-P`, `F2-E`, `F6-P`, `F3-E`, `F6-E`; the exact wording
   is in the fleet-measurement entry of
   `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
   through `engine.m3.generation.LiveModelAnswerer` against this world. A
   person reads all six answers against Section 0. Does C-P answer directly
   and not lead with a composite-voice disclaimer? Does any answer close on a
   self-composed aphorism? Does any sentence repeat verbatim across two
   answers? Does any answer speak build-pipeline vocabulary in character? Does
   any answer voice a Contested or Inferential-Thin citation as flat fact?
   Where an answer carries a story, is it actually told (scene, stakes, a
   concrete detail) and not summarized with the story's name attached? This is
   a cheap, direct reality check against the fleet's known failure shapes,
   done once, by reading six real answers. It is not a new checker.

**Grading.** Every answer in the lean set is graded on all four criteria
(Rigor, Accessibility, Craft, Focus). RS-1 and RS-2 are scored separately. An
RS-2 Representative-voice redirect is an ACCEPTABLE FALLBACK, not a PASS,
because the redirect belongs to the Facilitator. Every probe result is labeled
observed (with a transcript reference) or authored. An authored result never
scores PASS or FAIL.

**Graders score the first generation.** The answer graded is the first one the
system generated for the probe. A regenerated, retried or revised answer
never counts as a pass. If the runtime revised an answer before it reached
the participant, where a revision step exists, the grader scores the answer
as first generated, and the revision earns no credit for the world's answer
quality. A defect found in grading is fixed at its source: the record, the
prompt, the guard or the retrieval. It is never patched by a later rewriting
step.

**Pre-score the transcripts.** Before the blind grader reads the lean-probe
and Deep Interview transcripts, run the engine's checks over them:
uncited claims (`engine/m4/uncited_claims.py`), `guard_proximity` and the
grounding net's per-sentence verdicts. None of them calls a model. The grader
gets the flagged sentences as places to look, not verdicts. Most flags are
supported but untagged. The grader still reads every transcript in full.

**Full validation fires on code-detected triggers.** The `validation` command
is the code that detects them. They are checks in code, not thread judgment.
Any one starts full validation:

- a thin-evidence gravity
- a Contested Primary claim
- a safety-adjacent Representative
- any fabrication found in testing

The four triggers are defined as follows.

- Thin evidence: a Primary gravity whose own `formation_confidence` is
  `Inferential-Thin`.
- Contested Primary claim: a Primary gravity whose own `formation_confidence`
  is `Contested`. A `contested_claim` record attached to a Primary gravity does
  not count.
- Safety-adjacent Representative: the field `safety_adjacent` on
  `records/worlds/<code>.yaml` is `true`. Mark sets it to `true` or `false` at
  handoff, and handoff check 1 fails a new world until he does.
- Fabrication: the Fabrication column of a graded probe or interview result
  row says `yes`. The column holds `yes` or `no` on every graded row.

**An unevaluable trigger never yields lean.** If the code cannot evaluate a
trigger (`safety_adjacent` is missing or is not `true` or `false`, a Primary
gravity has no `formation_confidence`, the world has no Primary gravity, or a
graded row has no `yes` or `no` in the Fabrication column), the `validation`
verdict is `undetermined` and the command exits non-zero. Validation stops
until the missing value is supplied. A trigger the code cannot evaluate never
counts as not fired.

**A thread may raise the level and never lower it.** If the build judges lean
too thin for this world's risks, it recommends full validation to the project
lead, with the reason and the cost in allowance and dollars. The project lead
decides. A thread can raise what the code triggers. It never lowers it.

Full validation is the Construction Framework's Validation Protocol Rigor in
full: two independent generation trials per probe (one resampled from
development probes, one held-out and novel), fresh-context generation and
blind grading. It also includes probe parity (B-8) run as two trials, plus the Table Readiness Round in its cost-capped form. That form:
Representatives hard-capped at 3, the two or three sharpest B-7a pairings
sampled and never one table per frozen world, and grading on the available
evidence if spend is interrupted, as a declared limit and never a silent gap.
A fabrication found in testing is a root-cause event: find the cause at the
record layer and fix it there. Do not patch around it.

**What lean validation gives up, declared in every freeze package:**

1. The second independent trial, which the Framework's Validation Protocol
   Rigor requires. With single trials, generation-variance issues can slip. The standing mitigation is a cheap live re-probe the
   moment any report lands.
2. Live-pressed multi-Representative table dynamics: dominance, convergence
   and ending-not-read-back under real cross-world pressure. Interview
   dynamics are inside the bar and are not given up. The B-7a pairing
   disciplines are still authored in full.

A world frozen lean is declared "content-and-interview-frozen; table-dynamics
deferred." A world that ran full validation is declared with what it ran.

**The loop discipline ("loop until dry").** Every FAIL gets root-caused (Fable
diagnoses), fixed at its source (the record, the prompt, the guard or the
retrieval), cold-reprobed under the deployed
runtime, and the failed class re-run until clean. A probe that fails and gets
explained has not passed. The lean set makes loops cheaper, and it does not
make them optional.

**The Facilitator handoff wiring check.** At the Representative freeze, the
`wiring` command confirms that this world's compiled package is wired
correctly: both the acute-distress route and the harmful-dynamic and
dependency-seeking route fire, with no voice call made on either. It does not
re-run the shared classifier's accuracy battery. That code is identical across
worlds and is validated once, fleet-wide.

**Cost guardrails.** API credit exhaustion can kill a run midway.
Checkpoint probe and battery state so an interruption resumes and does not
restart. Watch metered spend during any generation-heavy session (Section 9).

**The freeze package.** Mark receives one package:

- the gates report (`Build/worlds/<code>/build/<code>_FREEZE_GATE_REPORT.md`)
- the freeze declaration (`<code>_FREEZE_DECLARATION.md`, same folder): what
  the freeze rests on; RESOLVED-AT-THE-FREEZE, listing M2; resolved-and-standing
  items; watch items; standing search limits
- the probe results and the Deep Interview transcript, each labeled observed
  or authored
- the Craft/Focus spot-check reading
- the Validation Layer attestation (Section 5), with the freeze criteria it
  names as not met
- the Record Integrity read (below)
- the residue read and bar screen artifacts
- both ledgers (Section 9)
- the open items, each with its `Open_Gaps_Tracking.md` entry
- the fleet sweep green: records validate, matrix clean, all gates zero,
  selftest green, retrieval metric-identical to baseline
- the world-boundary completion summary for M3

**The Record Integrity read** (`integrity <code>`) applies the Construction
Framework's Record Integrity Principle. A fix closes out the earlier
documents in the same change set. A reviewer's fix recommendation is
executed, or deferred with a reason. "Applied" means found in the deployed
artifact. Every finding an earlier document records as open is closed there
with a cross-reference, or carries an entry in `Open_Gaps_Tracking.md`. No
superseded draft sits unmarked in the world folder. Superseded files go to
`Archive/` at once.

The script checks four things: open findings have a gaps entry, no superseded
or second live version sits unmarked, no Construction Notes file states a
record count the records contradict, and `deployed` passes at the pinned
package. That last part covers the confirmed `world_core` items, the
self-reference hardening, the quote and gravity indexes, the rule counts and
the source anchor. It does not read what any document says was applied.
Three parts of the Principle are reviewer checks, not script checks: a fix
closes the earlier documents in the same change set; a reviewer's fix
recommendation is executed, or deferred with a reason; and Construction Notes
call a defect open only while it is. The reviewer reads all three at freeze.
The reviewer also confirms that each fix a document calls applied is found in
the deployed artifact.

**The Framework's freeze criteria, and where this process meets each.**

| Framework freeze criterion | Where it is met |
|---|---|
| Ecological Integrity testing (Balance, Reduction, Complexity, Emergence, Worship Integration) | The Validation Layer attestation (Section 5) |
| Differentiation established | The Validation Layer attestation, and the neighbour re-confirmation (Section 4) |
| Record Integrity | The Record Integrity read above, and `integrity` |
| Approved-source anchoring verified in the deployed prompt | B-7 and `deployed` |
| Validation Protocol Rigor | Lean by default. Two trials under full validation |

A document that is approved to proceed does not close anything. Nothing
closes until both Phase Five boundary testing and full-system review are
complete. That is the whole-system gate, a much rarer scope than a single
document's own approval.

---

## 9. Cost and pacing: two ledgers, one weekly rhythm

**The plan.** The plan is Anthropic Max 20x. The weekly allowance resets
Friday at 2:00 pm, Mark's time. At least 50% of each week's allowance is
allocated to building. At a target of 3–5 worlds a week, each world should use
about 16% (3 a week) or 10% (5 a week) of a week's allowance, or less. The
pilot measures the real number. Do not promise the pace.

**Two ledgers per world, kept separately.** The cost ledger is
`Build/worlds/<code>/build/<code>_Cost_Ledger.md`, made from
`Build/reference/L4-Templates/World_Build_Cost_Ledger_Template.md`.

- **Ledger 1: weekly allowance share.** Mark notes the `/usage` percent at
  world start and at freeze. The ledger also records tokens by model tier,
  review rounds and hours as a cross-check. Session cost telemetry shows the
  work at raw API rates. It is not a bill.
- **Ledger 2: metered API spend, in dollars.** It covers the live Deep
  Interview, the blind probes and any text-to-speech. The world has one ceiling
  for the whole lean validation set:

  **lean validation metered ceiling: set by the project lead before the pilot**

  This value is open. Do not start a paid run while it is a placeholder. Log it
  as an open item and ask Mark for the number when the first paid run is due.
  A run that would pass it is an escalation.

**The paid-bulk-run gate applies.** Before any run that spends real money in
bulk on a metered outside service (text-to-speech, image or model batches,
anything charged per item or character):

1. Run a small sample and get Mark's approval of it by ear or eye.
2. Pass every paid setting (voice or model id, generation settings)
   explicitly on the command. Never inherit them from the environment.
3. The run prints those settings, with item and character counts. Confirm
   them from that printed output before the run is called valid. A check that
   files match each other proves nothing about what produced them.
4. Record the dollars in Ledger 2.

**Halt, never thin.** Budget targets plan the work. They never thin it. If
staying inside a number would mean shipping work below the bar, stop at the
last green checkpoint. Put the choice to Mark in allowance percent and
dollars. Running out of allowance or dollars is never a licence to rush a
document, skip a review round or cut a probe class.

**Start-of-world check.** Before a world starts, read `/usage`. Start only if
the remaining build allocation covers a typical world (as the pilot measures
it) plus a reserve. If it does not, stop and report.

**Pacing.**

- Put heavy steps (Opus review rounds, Fable drafts) early in the weekly
  window.
- Pause only at a document boundary. Before pausing, update the state file,
  write the ledger entry and record the pause point.
- One world at a time by default. A second concurrent session runs only when
  the cost ledger shows the weekly allowance allows it.
- Write a ledger entry at each document boundary and at freeze. Record model
  and effort for each document and each review round, and the `/usage` reading
  before and after.

**The state file.** Each world carries a compact state file at
`Build/worlds/<code>/build/<code>_Build_State.yaml`, made from
`Build/reference/L4-Templates/World_Build_State_File_Template.yaml`. It is the
only record of where the world stands. Update it at every step change and
every review round. It holds the stamped process version, the current step and
the resume point. A new session reads it first, then re-runs the previous
checkpoint before new work. The world must be able to stop at any document
boundary and resume after the Friday reset.

---

## 10. Session rules

These rules apply to every session on a world build. They are restated here, so
no other file is needed to follow them.

1. **Fetch, then read the state file.** Fetch `origin/main` and read the
    current repository state before judging what exists. Then read the state
    file and resume from its resume point. Run one live thread per world. A
    thread on a stale checkout can duplicate a merged phase and overwrite a
    real review file.
2. **Re-run the previous checkpoint before new work.** For a script or a gate,
    re-run it and expect the same result. For a checkpoint that rests on a
    sample, a probe set, a blind grading or a review, re-running means
    re-checking the committed sample IDs, probe list or transcripts against
    the records and code. It does not mean drawing a fresh sample or grading
    again with different material. So a committed artifact lists those IDs. If
    the previous checkpoint fails when re-run, stop and file the regression. Do
    not start new work.
3. **One declared step at a time,** with a `Touches:` line naming every file
    it may change. The tooling does not stop a change outside that list. The
    reviewer's first structural check is the diff against the declared
    `Touches:` set.
4. **Gate-integrity rule.** Never edit a gate or checkpoint script in the session that must pass it. A session that needs a gate changed files a flag and stops.
5. **Done means a committed artifact that re-runs green.** A step is done when
    its checkpoint artifact exists, is committed, and re-runs green. It is not
    done when the session says so. The checkpoint is defined before the
    session runs, and the session never moves its own goalposts.
6. **In-world autonomy.** Every decision is recorded with the real
    alternatives considered and the reason the chosen one is the most
    defensible, and not only the conclusion. Stop only at M1, M2, M3, the
    escalation list in Section 1, and the world boundary.
7. **Defects go to the world's `Open_Gaps_Tracking.md`,** never silently
    patched. Upstream wording problems are referred, not rewritten.
8. **End every session deployable.** Partial work commits at the last green
    checkpoint. A session that runs out of room marks the step `in-progress` in
    the state file, with a note on exactly where it stopped. The next session
    restarts from the last green checkpoint, not from a description of partial
    work.
9. **Commits carry step IDs. Push only on Mark's word.**
10. **Safety-regression and retrieval-regression rules.** Any step that touches
    the intercept chain or retrieval ends with the full rerun and diff against
    the committed baseline.
11. **Round cap.** A document gets at most three rounds of substantial
    revision. A revision is substantial if it changes a claim's substance, a
    confidence rating, a sourcing conclusion or a scope boundary. A finding
    that is wording, tone, format or a typo only is cosmetic. It may be
    applied directly, without a new round. A finding that a document could be
    stronger, with nothing in it wrong, unsupported or misleading, is not
    substantial and does not start a new round. If a document has not cleared
    review after its third review round, that is an unresolved tension the
    pipeline cannot close on its own. Stop, and send it to Mark with the
    third round's findings. Never start a fourth round. A revision made after
    the third round is not reviewed by a fourth file. The `roundcount` command
    counts review files, whatever their verdict, and blocks a fourth.
12. **Who reviews.** Opus 5.5 reviews every round. Round 1 runs at high effort.
    Rounds 2 and 3 are targeted rechecks at medium effort: only what changed,
    against the prior findings. The reviewer is never the drafter.
13. **Record status.** See Section 6.
14. **Registry first.** A world's registry entry (`records/worlds/<code>.yaml`)
    exists before any of its records reach `main`, so CI sees the world from
    its first record. The `world_id` is identical across the registry entry
    and every record.
15. **Simulated-review label.** Every review file an agent writes begins with
    the literal line "Simulated review — informational only, not an Article 31
    substitute." An agent-run review never stands in for Article 31's external
    scholarly accountability.
16. **Truncation check.** Every review round verifies the document's
    completeness by two independent methods: a direct file read, and an
    independent bash-level count or grep. Both are recorded in the review file
    with raw evidence. If the two disagree, the direct file read is
    authoritative. A dismissal of that disagreement needs independent
    confirmation before it counts as resolved.
17. **No self-certified dismissal of a blocking finding.** A drafter-side
    investigation that dismisses a blocking finding needs independent
    re-confirmation by a fresh Opus review at high effort. Re-verify every high
    finding against source yourself before you apply a fix.
18. **Vocabulary.** Say "Approved to proceed." Never say "finalized." A
    document that is approved to proceed has not closed anything (Section 8).
19. **Open items.** Every open item in a review or phase document has an
    `Open_Gaps_Tracking.md` entry. Entries are append-only and numbered. A
    merged entry's number never changes, and cross-references cite subject and
    date, never a bare number. Every known fleet-level defect that is not being
    fixed now is registered as an `ACCEPTED_OPEN` waiver with an owning
    finding. A stale waiver for something already fixed fails the run, so
    remove it.
20. **Decision logs.** Decisions, audit trails, review rounds and status
    reports go in `Build/Ministry/`, never into a live or canonical file.
    Superseded material goes to `Archive/`. Nothing is deleted without
    instruction.
21. **Change orders.** Once something is frozen or otherwise settled, a real
    change to it is a named, reasoned change order, and never a quiet edit.
22. **One state during review.** Make no structural edit to a tree while a
    review of that tree is running.
23. **One story.** The state file, the commits and the checkpoint artifacts
    tell the same story. A mismatch between them is filed in
    `Open_Gaps_Tracking.md`.
24. **A returning defect class is escalated.** If the same class of defect
    comes back across review rounds, name the class in the review file and
    escalate it as an unresolved tension. Do not chase it one instance at a
    time.

---

## 11. The pilot

Two pilot worlds go first. One is well-sourced. One is thin-evidence, so the
full-validation triggers get exercised. The pilot world choices are open: Mark
names them, or the source-research thread proposes them.

**Pilot exit.**

- zero fabrication
- all four criteria pass
- no new waivers
- allowance percent, metered spend and hours recorded per world, split into
  drafting, review and probes
- the Doc_10 Sonnet-versus-Fable grading recorded (Section 2)

After the pilot, builds run steady at one world at a time. A cost-and-quality
review follows after every five worlds. It includes a coach verification:
review files exist and support what cites them; escalation triggers were not
missed; the decision log matches what is on disk; and decisions match the
governing designs. The coach thread reports to Mark and drafts or revises no
world document. A coach verification also runs across any batch of disposed
work that Mark names.

---

## 12. Process version and change orders

The process version is stamped on each world at start, in its state file. The
version is frozen at pilot start. A change to this process after the pilot
starts is a named change order with a reason, and it never lands as a quiet
edit. A world freezes against the process version and Completion Standard
version in force when its build began.

**Change orders.**

- Step 0 to 2 process and gate fixes: the Section 4 Library-stage rules and
  checklist, handoff items 1 and 12, the round counter's `Cycle reset`
  field, and the review-file and manifest templates. Source: the project
  lead's instruction, logged in `LIBRARY-DECISION-LOG.md` as "Step 0-2 process
  and gate fixes".

---

## 13. Open items

These items are open. Each must be settled before the step that depends on
it. A check or field listed here does not exist, and no document may report
it as run or present.

**Owed by Mark**

- **Lean validation metered ceiling.** The number is owed by Mark (Section 9).
- **The two pilot worlds.** Mark names them, or the source-research thread
  proposes them (Section 11).

**Engineering items: record fields (schema changes)**

- **Capsule Core inhabited-voice field.** The Capsule Core's inhabited-voice
  text has no field. `build_capsule` writes only what the records carry.
- **Telos field.** The schema has no telos field, so the world's construction
  notes hold the telos until an engineering item adds one.
- **Fields the live schema does not define yet.**
  The process and the Completion Standard cite only fields the schema
  defines. The schema does not define these fields yet:
  - a source `language` field;
  - `interaction[]` and `connections[]` on gravity and force records, and
    `gravity_links` on story records, with the relation types `reinforcing`,
    `competing` and `reshaping` (the schema's `relations[]` types are listed in
    Appendix B);
  - the six-test result keys on gravity records, and Layer 4 (`elaboration` or
    `stasis`) on force records;
  - `owner_figure_id` and `attested_occasion` on story records;
  - `voice_surface`, `semantic_domain` and a directional `field_relation` on
    term records;
  - a translation-used field on quote records;
  - a trait rubric, an avoid-traits list, register evidence and a native
    answer-length measure on the voice record;
  - a documented alias exception on term records.

  Until a field exists, the content lives in the Doc_04, Doc_08 and Doc_10
  tables and in record bodies, and the review checks it there.

**Checks with no script**

- **Three parts of the Record Integrity read.** No script checks that a fix
  closes the earlier documents in the same change set, that a reviewer's fix
  recommendation is executed or deferred with a reason, or that Construction
  Notes call a defect open only while it is. Nor does any script check that
  each fix a document calls applied is found in the deployed artifact. These
  are reviewer checks, read at freeze (Section 8). `integrity` does not cover them, and a clean `integrity`
  run does not show them.

---

## Appendix A: The record-native mechanisms a new build inherits

| Mechanism | Lives at | What it caught |
|---|---|---|
| The record store and schemas | `engine/m1/schemas.py`, `records/<code>/` | One source of truth; drift is impossible by construction |
| The M1 gate battery and selftest | `engine/m1/gates.py`, `engine/m1/selftest.py` | The zero-violation floor on every frozen world |
| The alias-safety gate | `gate_alias_safety` in `engine/m1/gates.py` | Alias collisions between terms; Hieronymian was born clean under it |
| Claims register and its check | `Build/worlds/lpc/Doc09_Claims_Register.md`, `Build/worlds/lpc/scripts/check_claims.py`, `claims` | Absence and exclusivity claims that no reviewer happened to check |
| Term gloss list and `gloss_forms` | Term records; `engine/m4/term_glosses.py` | The gloss allowlist is the world's own term records |
| Compiler, packages and determinism | `engine/m2/`, `packages/<code>/<pin>/` | Byte-identical rebuilds; staleness checks |
| The four-parity release gate (render, retrieval, prompt coverage, probe) | B-8 above | Real catches at nearly every world's B-8 |
| The production-eval verdict rule | `engine/m4/reports/retrieval_bench.py`, `engine/m4/reports/bench/<code>.json` | A dispute resolved by measurement, not argument |
| The re-proof-under-deployment rule | A discipline (Section 6) | The fleet's dilution failures |
| Citation grounding and the uncited-claims check | `engine/m4/grounding.py`, `engine/m4/uncited_claims.py` | The live sweep's Syriac finding |
| Library confinement and holdings | `engine/m9/` | Off-shelf reads; unread vendored files |
| The Table Readiness Round (cost-capped, cap 3) | Section 8; `Build/reference/method/Pass2-decisions/S6.2_M_table_cap_and_trr_cost.md` | Cross-world disciplines pressed live |
| Article 29 at-freeze confirmation; Article 31 year-two ruling | Freeze declarations; `Build/reference/method/Pass2-decisions/` | Every built world carries a settled Article 29 state |

## Appendix B: Schema enums to author around

Authoring hits these enums. Declare, and do not invent. The schema is the field
list (`engine/m1/schemas.py`).

- `relations[]` types are `presupposes`, `presupposed-by`,
  `precondition-for`, `enabled-by`, `tension-with`, `illustrated-by`,
  `illustrates` and `associated-with`. There is no `reinforcing`, `competing`
  or `reshaping` type. Doc_04 states those relationships in its interaction
  matrix, and the record store does not carry them (Section 13).
- Every relation needs its reciprocal back-edge on the other record.
- `confidence.evidentiary_weight` is `load-bearing`, `corroborating`,
  `illustrative` or `contested`. It has no `qualified`.
- `confidence.verification_state` is `verified-direct`,
  `verified-via-authority`, `named-not-rechecked` or `unverified`.
- `source.kind` is `vendored`, `unvendored` or `absence`. A source record has
  no `language` field.
- `term.distortion_risk` is `low`, `medium` or `high`.
- `gravity.classification` is `primary`, `supporting` or `tensional`.
- `force.matrix_cell` is one of `1A`, `1B`, `2A`, `2B`, `3A` or `3B`.
- `quote.license` is `verbatim`, `paraphrase-only` or `do-not-voice`.
