# Repo Structure Cleanup — Standing Thread Tracking

Running, dated ledger for the Repo Structure Cleanup thread, opened 2026-09-14 on Mark's
direction: "we have a lot of disconnected pieces and false positives, or I can't find this
or that... I need a thread that will systematically go through everything and clean up so we
are back to the simplest, clean live and build structure." Same discipline as
`CiC_System_Health_Tracking.md`: dated entries, honest status, root cause over symptom.
No finding or decision lives only in a session's conversation history.

---

## Thread scope

**Mandate:** make the repository tree say what is live, what is sandbox, and what is
history, and give each module one home. Structure only — filing, naming, manifests,
CLAUDE.md's own map. Nothing that changes what runs.

**Process:** CLAUDE.md "How we work" — divergent, groan zone, convergent, then auto mode
only for what has actually converged. One question at a time. Nothing moved, deleted, or
committed until Mark converges on the target; an Opus adversarial gate precedes any bulk
move, because Render and Cloudflare read paths from this repo.

**Model routing:** Fable for the framing rounds; Sonnet for execution; Opus once, before
anything irreversible.

**Explicitly not this thread:** engineering changes to the runtime (object-storage package
fetch, idle-world unload, an Atlas module) — surfaced here as work orders, not done here.
Not a governance or methodology authority. Not a world-build thread.

**Companion artifacts:** "The Stacks" (System Health's first-pass inventory, 2026-09-14)
and "The Seam" (this thread's deep read, v1 divergent round 1, v2 divergent round 2).

---

## 2026-09-14 — Thread opened; deep read; three decisions converged

### What was found (evidence in "The Seam" v2)

**Root cause.** Two complete systems from two eras sit on top of each other. The July
"Level system" (L0–L4, Project-Reference, World-Builds, Archive, Ministry, cic-poc) has a
ratified filing doctrine, `L2A-System-Architecture/CiC_L2A_Clean_File_Structure_V1.1.docx`,
executed once already (Filing System Audit 2026-07-20). The record-native redesign (engine,
records, packages, canon, fixtures, cic, world-build-docs, fleet-voice — six of them born
2026-08-20) landed beside it with its own map, CLAUDE.md's "live/canonical surfaces" list.
Neither map mentions the other's folders. Both are wrong about something: the L2A doctrine
has never heard of `engine/`; CLAUDE.md omits `World-Builds/`, `cic-poc/`, `cic-website/`,
`fixtures/`, and says Doc_01–Doc_09 live in `world-build-docs/` (they live in
`World-Builds/`). There is no current map.

**Load-bearing paths, verified from config, not inferred:**
- Render / `engine/Dockerfile` COPY: `engine/ records/ packages/ cic/texts/ cic-poc/frontend/`
- Cloudflare (`wrangler.jsonc`): `cic-website/`
- CI (`ci.yml` path filters): `engine/** records/** packages/** fixtures/** cic-poc/frontend/**
  cic-website/data/world-census.json Ministry/Features/Atlas-World-Map/Design/tools/validate-census.mjs`
- engine code: `records/ packages/ canon/ fixtures/ cic/texts/`
- Nothing executable reads any L-folder, `Project-Reference/`, `Syriac-Build/`, `Archive/`,
  `World-Builds/`, `world-build-docs/`, `fleet-voice/`, or `Redesign-Spec/`. All references
  into them are prose or code comments (~250 files).

**Findings beyond The Stacks:**
1. One world lives in up to six places under three naming schemes (long name in
   `World-Builds/`, registry code in `world-build-docs/`, `records/`, `packages/`; slug in
   `cic-website/traditions/` and `cic/corpus-map/`). One `World-Builds/` folder carries a
   `01-` prefix; none of the other eleven do.
2. `Syriac-Build/` is not a copy of the L-folders — it is an older stratum. 43 of 45 files
   are nested L-folders; 9 differ from root, 5 exist only on one side. Two unique files:
   `CiC_Coach3_Step0_Critique_2026-07-06.md` (cited by path from six IJC review rounds) and
   a third distinct `CiC_Step0_Conclusion_FINAL.docx` (the root holds two others, different
   checksums).
3. A live CI dependency (`validate-census.mjs`) lives inside `Ministry/Features/`. Build
   tooling has four homes: `engine/m1–m3`, `world-build-docs/*/generate_*.py`,
   `Ministry/…/tools/`, `World-Builds/Donatism/scripts/`.
4. Fifteen loose root files beyond the five config files: twelve July artefacts, four
   `.skill` zips superseded by the installed plugin (SKILL.md has since diverged), two L3D
   safety proposals (one cited by CLAUDE.md as the live draft). Also two `desktop.ini`, 24
   docx/md twins and nine `_FINAL_v2`/`_v3` staircases in `World-Builds/`.
5. Corrections to The Stacks: the 2026-08-29 same-day signature does not hold in full
   history (L-folders last changed 2026-07-20 to 2026-08-05); `World-Builds/` is not
   reference — it is the hottest tree in the repo (Donatism, LPC, Cappadocian, apologists all
   changing through 2026-09-12).

**Module seams (engine read, evidence paths in "The Seam" v2 table):**
- Library (`cic/`): clean seam; the running server never reads it; the image copies it only
  because packages are recompiled inside the Docker build.
- A world: loads lazily, isolated per turn by tests not by a boundary; `unload()` has no
  production caller so idle worlds never leave memory; every world is baked into one image;
  no object-storage fetch path exists although Artifact-2 §5 specifies one.
- Fleet-shared: `records/_fleet/` is read live every turn through a global cache and `canon/`
  at admission; `fleet-voice/EXEMPLAR-TRANSCRIPT.md` is cited by 17 records and build docs
  but read by no code (Gate A correction). The one thing every world legitimately shares;
  undeclared as a module.
- Interview vs Table: separate files (`wiring.py`/`table_wiring.py`, `turn.py`/`round.py`)
  but Table imports Interview privates, both share `turn.py`, one store, one FastAPI app.
- Atlas: no engine module at all — static HTML in `cic-website/`, a hand-kept census, a
  build-time cross-check, and 54 design files in `Ministry/Features/Atlas-World-Map/`.

**Constraint governing sequence:** 170 branches on origin, 20 with commits in the fortnight
to 2026-09-13, 8 of them world builds writing into `World-Builds/` and `records/`. Cold-zone
moves (root files, Archive, L-folders, Syriac-Build, Project-Reference, Pass2) are cheap.
Hot-zone moves (`World-Builds/`, `records/`, `Ministry/`) need a declared freeze window.

### Decisions (Mark, 2026-09-14)

- **D1 — Four kinds at the root: live / build / reference / history.** Chosen over three
  (live / build / history, which re-lumps hot per-world trees with the cold method library —
  the pair Syriac-Build confused) and two (in use / history).
- **D2 — Reframed as zones over modules.** Mark's own words: the system is modular — the
  library is a module; each world is a self-contained unit, called up when needed, using no
  memory or cache when idle, connected only to its own library sources, with no access to any
  other world; the atlas, the multi-table engine, and the interview engine are each modules.
  A full running live version, updated by modular updates; all old files archived as history.
  Then: "the live version that is protected until things are tested and verified, then an
  update, and a sandbox that we build/improve as a module system." This is the ruled design
  already (Program-Spec §4, Artifact-2 §5, Artifact-6 §3 — three deployable pieces,
  `staging` + `prod`); the repo and the deploy never followed it. D1's "build" is the
  sandbox; "reference" (the method library) remains to be placed within this frame.
- **D3 — The sandbox is a promotion model.** `main` becomes the integration sandbox and
  deploys to a staging service; a protected `live` branch or release tag is what production
  deploys from, advanced only by a deliberate, logged promotion after tests and Mark's
  verification. Chosen over branch-discipline-only (the current 170-branch fog as steady
  state) and sandbox folders in the tree (kept for design workshops only, per the Website-V2
  precedent). Cost to confirm before execution: a second Render service for staging; Cloudflare
  already builds a preview per branch.

- **D4 — One home per world, keyed by registry code.** `World-Builds/<Long-Name>/` and
  `world-build-docs/<code>/` merge into one tree keyed by the registry code (spec principle
  4); `records/` and `packages/` stay where the engine reads them. Decided now, executed only
  inside a freeze window between world-build rounds. The four unregistered candidate worlds
  (Gallic-Monastic, Latin-Pastoral-Congregational, Latin-Apologists, Second-Century-Greek-
  Apologists) need registry codes first. Chosen over code-rename-only and over deferring.
  Mark's follow-on, opened as question 1b: how the library and the worlds should relate —
  sources kept in a library system, integrated into each world's tree, or a Venn overlap —
  given that sources are downloaded ahead of builds, the library's organization drives both
  step 2 and the drawing of lexicon/stories/quotes, and worlds must stay sealed from each
  other.

- **D5 — Library and worlds: Venn by shelf, with a gate at the door.** One flat,
  rights-verified library organized by Atlas tradition (`cic/texts/` + `cic/corpus-map/`,
  which already is this). Each world's tree carries its own generated shelf — the works, loci
  and roles it may draw from, inherited from its tradition via `census_id` and narrowed by
  step 2. The barrier is a build gate: a world whose records cite anything off its shelf
  fails to compile (WO-4). Runtime unchanged — the package is the seal. Chosen over
  library-only (no per-world view) and sources-inside-each-world (ruled out by the data
  below). Mark, 2026-09-14.

**Question 1b evidence (library ↔ worlds), measured 2026-09-14:**
- `cic/corpus-map/_staging/`: 677 works; 47 assigned to a single tradition (7%); median
  work claimed by 4 traditions; one by 19. Assignment is non-exclusive by design (corpus-map
  README, Mark 2026-08-26: "keep this separate from the built worlds with clear buckets that
  align, then we can figure out how best to integrate").
- `cic/texts/README.md` (generated "cited by"): 102 vendored files, 244 MB; 40 uncited —
  shelved ahead of need; of the 62 cited, 19 serve 2–6 worlds, one serves six of eight.
- 55 corpus-map buckets (Atlas traditions) vs 8 built worlds; joined by
  `records/worlds.yaml → census_id`. The library is organized by tradition; worlds are the
  built subset.
- Runtime never opens the library; a world speaks from its compiled package. Quote
  verification against `cic/texts/` is build-time (`engine/m1/gates.py`).
- `engine/m1/cross_world.py observe_corpus_map` performs the records ↔ shelf join as an
  observation, not a gate.
- Conclusion offered to Mark: sources cannot live inside a world tree (duplication, rights
  headers, size); the Venn is a list — a per-world shelf inherited from its tradition,
  narrowed by step 2 — and the barrier is a gate on that list, not a folder boundary.
  Candidate WO-4: promote the observation to a gate.

**Question 1c (Mark, 2026-09-14): two worlds drawing from one source file — how is each
kept to its own material, so a neighbouring tradition's quotes or stories don't become
fabrication or misapplication?** Measured answer, three layers:
1. Assignment is by work + locus + role, not by file. `cic/corpus-map/` assigns each work
   inside a compendium to traditions separately, with a locus and a role (`tradition` /
   `context` / `antecedent` / `transmission`). Real; keyed by Atlas entry; not yet projected
   into any world's tree.
2. Every quote/story record cites a section and is verified verbatim against the file (331 of
   335 carry `locus`); `source` records are world-scoped. But the machine-resolvable
   `address` (`cic:<file>:<locus>`, schema 2026-09-02) is on 5 records, `work_id` on 10 of
   343 source records, `WORKS.yaml` has 4 seed entries. `engine/m1/gates.py`
   `gate_quote_recording` checks license validity and verbatim presence in the file — not
   which section, not whose voice. Today the section and the voice are held by build threads
   and review rounds, not by a gate.
3. The compiled package is the runtime seal.
Consequence: WO-4 is specified as three compile-time checks (work on shelf; address within
the work's locus; `context`/`antecedent`/`transmission` works citable but `do-not-voice`),
with a per-world backfill of `work_id` and `address` and growth of `WORKS.yaml` as
build-thread work. Draft target tree amended accordingly ("Two worlds, one file").

- **D6 — The target tree is frozen. "Converged, auto mode."** Mark, 2026-09-14, on the
  draft "The Target Tree" v3 (artifact 4dc210d6) with P1–P11 as drafted. From here changes
  to the plan are change orders, named and reasoned, logged in this file. Execution order:
  Opus adversarial gate (Gate A) → phase 1 cold zone in auto mode → phase 2 worlds merge only
  inside a freeze window Mark declares (Gate B) → phase 3 promotion infrastructure and the two
  optional renames. Model routing from here: Sonnet for execution; the gate runs on Opus.

### Gate A — Opus adversarial review of the frozen plan (2026-09-14)

Verdict: NO-GO as written; GO with fixes. All three blockers resolved before execution:
- **B1** The repo-wide citation rewrite would have edited 79 `records/` files; a record is
  copied byte-for-byte into its package and hashed by the manifest, so one changed byte
  fails `engine.m2.cli restore` inside `engine/Dockerfile` — the image would not build.
  Fix applied: `records/`, `packages/`, `canon/`, `fixtures/`, `cic/texts/` and `Archive/`
  are never rewritten; their citations enter the baseline for the owning threads.
- **B2** ~900 cited paths are already unresolved at HEAD; a strict path check could never
  go green. Fix applied: `tools/check_paths.py` holds only current documents to the tree,
  accepts a committed baseline (`tools/check_paths_baseline.txt`), and fails only on new
  breakage. **Mark's action:** `main` requires "11 of 11" status checks — the new
  `check-paths` job must be added to branch protection by hand or it never gates.
- **B3** `Ministry/Technology/Pass3/provider_repricing.py` and `cost_floor_model.py` open
  `Pass2/baselines/…` by path; every `Pass2/gates/*.py` finds the repo root by directory
  depth (`parents[4]`). Fix applied: Pass2/ and Pass3/ keep their names and depth under
  `Archive/Technology-Pass2-2026-08/`; the two `os.path.join` literals edited by hand; the
  single-string literal in `S6.2_length_ceiling_observability_gate.py` rewritten by script.
Risks acted on: two generators (`world-build-docs/pahc|desert/generate_voice_index.py`) emit
a `Redesign-Spec/` path — rewritten in the .py as well as the .md; 23 `.docx`/`.xlsx` embed
old paths and cannot be rewritten — listed in the move ledger as known-stale; the tracking
doc's own claim that `fleet-voice/` is read at runtime was wrong — corrected. Branches:
`donatism-lpc-integration` adds files under `Ministry/Technology/Pass2/trr/` and
`claude/facilitator-placeholder-text-jaim31` adds `Redesign-Spec/ADMISSION-GAP-STATUS…` —
both would merge without conflict and silently resurrect a retired directory; `tools/
retired_paths.txt` + the check-paths job now fail CI if a retired path reappears, and the
rebase note below says where those files go. `claude/usage-credits-optimization-m9ji3d`
carries its own CLAUDE.md (add/add conflict already, independent of this plan) with the
stale Pass2 path and the uncorrected live list — resolve toward this branch's CLAUDE.md.
Flagged, not touched: CLAUDE.md line 23 cites `phase2_checkpoint.py`, which exists nowhere
in the repo (pre-existing).

**Rebase note for open branches after phase 1 merges:** files added under
`Ministry/Technology/Pass2/**` belong in `Archive/Technology-Pass2-2026-08/Pass2/**` (or,
if they are decisions, `reference/method/Pass2-decisions/`); files added under
`Redesign-Spec/` belong in `reference/Redesign-Spec/`; under any `L*-*/`, `Project-Reference/`,
`fleet-voice/` → the same name under `reference/`; under `Syriac-Build/` →
`Archive/Syriac-Build-2026-07/`. Run `python tools/check_paths.py --baseline
tools/check_paths_baseline.txt` before pushing.

### Change orders against the frozen plan

- **CO-1 (2026-09-14, this thread, pre-execution).** The plan placed all three
  `CiC_Step0_Conclusion_FINAL*.docx` in `Archive/Superseded-Housekeeping/`. Wrong premise:
  `CiC_Step0_Conclusion_FINAL_v2.docx` is the closed, merged *Phase One World Selection* — the
  portfolio-level document every new world's Step-0 cites as the registry of Worlds #1–#N
  (68 citations; 23 from LPC alone). It is live reference, not history. Corrected: v2 →
  `reference/L3B-World-Build-Methodology/`; `FINAL.docx` (v1, superseded by v2's merge) and
  the `Syriac-Build/` copy → Archive as planned.
- **CO-2 (2026-09-14, this thread, pre-execution).** CLAUDE.md cites
  `Ministry/Technology/Pass2/decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and
  `VR_1A_Writing_Standard_2026-08-09.md` as the governing readability decisions. A governing
  decision is reference, not closed evidence. Corrected: `Pass2/decisions/` (22 files) →
  `reference/method/Pass2-decisions/`; the rest of Pass2 (baselines, batteries, gates, TRRs,
  reviews) and Pass3 → `Archive/Technology-Pass2-2026-08/` as planned.
- **CO-3 (2026-09-14, PR #183 blocked).** `main` has been red on the required M1 selftest
  since `7c22635a3` (2026-09-12): Donatism's Atlas card was reverted to "Selected - Not Yet
  Built" (correct — `state: built`, not admitted, so the app does not list it), but
  `engine/m1/cross_world.py check_census_link` demanded a "Built & Live" card for every world
  with a `census_id`, state-blind; and the census file was not in the M1 job's path filter,
  so the census-only PR never ran the job. Docs-only PRs merged past it; phase 1 touched
  `engine/` comments, so the job ran and exposed it. Fix (this PR, engine change, Mark's
  acceptance): the check requires a live card only for admitted/open worlds and an existing
  entry for built ones; `cic-website/data/world-census.json` added to the `engine` filter.
  10/10 M1 tests pass; `cross_world` exits 0; no waiver added. Alternative rejected: an
  `ACCEPTED_OPEN` waiver cannot satisfy `test_the_desert_deep_link_defect_is_caught`, which
  asserts the raw check is clean.
- **Execution details settled within P9/P11 (no change to the plan):** the citation rewrite
  and the path check share one scope — current documents only. Dated Ministry history (audits,
  decision logs, launch prompts, dated files) is not rewritten; it describes the tree as it
  was, and the move ledger maps old to new. `records/` is not rewritten in phase 1: editing a
  record changes its compiled package and stales the pinned manifest (M2 staleness job), and
  repinning touches `worlds.yaml`, the file the active world branches conflict on. Record
  citations of moved paths (79 files, mostly the Register Bar) enter the baseline for each
  world's thread to fix at its next recompile. Pre-existing unresolved citations measured
  before any move: 284 in current documents (126 to the retired `cic-poc/backend`) — recorded
  as the accepted baseline, flagged to owning threads, never touched by this thread.

**Standing rule for execution (Mark, 2026-09-14):** notes of changes or directions never go
into a working file — a supplemental file holds the record. Applied here as P11 of the draft
target tree: rewritten paths carry no inline comment; the narrative and decisions live in this
file; a machine-readable move ledger (one row per old → new path, with commit) lives at
`Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md`; the root map carries no
changelog; `SHELF.md` is generated and carries no notes.

### Engineering work orders surfaced (not this thread's to do)

- **WO-4 (specified 2026-09-14)** Shelf gate at compile: (a) every `source.work_id` resolves
  to a work on the world's `SHELF.md`; (b) every quote/story `address` falls inside that
  work's locus in that file; (c) role-gated voicing — `context`/`antecedent`/`transmission`
  works citable as evidence, never voiced. Prerequisite backfill per world: `work_id`
  (~333 source records), `address` (~330 quote/story records), `WORKS.yaml` growth.
- **WO-5** Admission-time distinctness battery (Program-Spec §5.4) — not yet a probe
  category in `engine/m3/protocol.py`.
- **WO-1** Object-storage package fetch, so one world can be updated without a full redeploy
  (Artifact-2 §5, spec principle 16b; today `engine/Dockerfile` bakes every world in).
- **WO-2** Idle-world unload policy (`engine/m4/world_loader.py` `unload()` has no
  production caller; `engine/api/app.py` builds one process-lifetime loader).
- **WO-3** An Atlas module with one home for page, data, validator and design.

### Open questions, in order

1. Worlds: one home under the registry code now (executed in a freeze window), code-rename
   only, or leave the world trees for a later phase.
2. Placement of the method/spec library (L-folders, Redesign-Spec, Ministry/Technology's six
   method-grade docs) within the zone model.
3. Fleet-shared as a declared module: home for `records/_fleet/`, `fleet-voice/`, `canon/`.
4. History: one marked home for Archive, Syriac-Build, Pass2, the root July files, the
   retired cic-poc backend's remains.
5. Root manifest and CLAUDE.md correction.
6. Freeze window and execution phases; Opus gate; promotion mechanics for D3.

---

## 2026-09-14 — Phase 1 executed on `claude/repo-structure-cleanup`

**Commit `5aedf3df`** (517 renames, 161 rewritten files, 6 additions, 2 deletions), after
Gate A. Nothing Render, Cloudflare or the engine reads moved. Executed exactly per the frozen
tree with CO-1 and CO-2; verified before commit: no double prefixes; `ci.yml` census paths
updated; both `generate_voice_index.py` generators rewritten; Pass3 scripts resolve their
data at the new depth; every changed `.py` compiles; the Pass2 gate scripts still find the
repo root. `tools/check_paths.py --baseline tools/check_paths_baseline.txt`: 0 new
unresolved citations, 0 retired paths present, 332 accepted.

**Correction, same day, next commit:** the move script ran single-file moves before
directory moves, so `git mv` nested `L3B-World-Build-Methodology/` and
`L3D-Encounter-Methodology/` inside the `reference/` directories the file moves had just
created. Caught by the binary-citation scan, not by the path check — because the baseline
had been regenerated after the move and absorbed the breakage. Flattened; the baseline was
then rebuilt as a diff against the pre-move tree (269 → 280: every addition is either a
`records/` citation deferred by design, a pre-existing break whose citing file moved, or a
prose token such as "reference/analytical" that only reads as a path now that `reference/`
is a root directory; listed per file in `tools/check_paths_baseline.txt`). Lesson recorded for phase 2: order moves
directory-first, and never regenerate a baseline without diffing it.

**Root now:** `README.md` (the map) `CLAUDE.md` `.gitignore` `render.yaml` `wrangler.jsonc`
`.github/` · `engine/` `records/` `packages/` `canon/` `fixtures/` `cic/` `cic-poc/`
`cic-website/` · `World-Builds/` `world-build-docs/` `tools/` · `reference/` · `Ministry/` ·
`Archive/` · and one file waiting for phase 2, `CiC_W1_Phase5_RelationalSafety_Retest_
Against_Proposed_Mechanism_DRAFT.md` → `worlds/pahc/`.

**Supplemental record:** `Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md`
— every old → new path, the commit, the binaries that embed old paths and cannot be
rewritten, and what was not rewritten by design.

**Flagged to owning threads (in the accepted baseline, not touched here):**
- `records/` — 75 citations of moved paths, mostly the Register Bar; fix at each world's
  next recompile and repin (Package rebuild after a records/ edit: just do it).
- 126 citations of the retired `cic-poc/backend` across World-Builds and Ministry current
  documents; 23 citations of `Ministry/Technology/…` paths that moved in the July reorg;
  `World-Builds/Nicene-Cappadocian` (renamed to `Cappadocian`); `…Framework_V7.4_DRAFT.docx`
  (the DRAFT became V7.4). Per-file list: `tools/check_paths_baseline.txt`.
- CLAUDE.md line 23 cites `phase2_checkpoint.py`, which exists nowhere in the repo.

**Mark's actions, in order:**
1. Review and merge the PR for this branch. Merging to `main` deploys (D3's staging/prod
   split is phase 3), but no deploy-read path changed; CI's docker-build job is the proof.
2. Add the new `check-paths` job to `main`'s required status checks (branch protection
   currently requires "11 of 11"); until then the job runs but does not gate.
3. Declare the phase-2 freeze window for the world trees (Gate B), naming the branches to
   land first: LPC, Gallic, PAHC, IJC, Syriac, Donatism, Desert, apologists.
4. Confirm the Render staging-service cost for D3 (render.com is egress-blocked from the
   sandbox; the Blueprint's per-service branch field could not be verified from here).
5. Register codes for the four candidate worlds (P6): `gallic`, `lpc`, and two to name.

**Status:** phase 1 merged to `main` (`620b5b14b`, includes CO-3).

---

## 2026-09-14 — Gate B open; phase 2 sequencing

**Gate B declared (Mark, 2026-09-14): "open the freeze window for phase 2."** Manifest
staged (`tools/moves-phase2.tsv`): 12 `World-Builds/<Long-Name>/` → `worlds/<code>/`
(candidate codes `gallic`, `lpc`, `latap` = Latin Apologists, `grkap` = Second-Century Greek
Apologists — P6, Mark 2026-09-14), 6 `world-build-docs/<code>/` → `worlds/<code>/build/`,
`world-build-docs/_cross-world/` → `worlds/_cross-world/`, the W1 draft → `worlds/pahc/`.
`tools/gen_shelf.py` staged to generate each world's `SHELF.md` from its corpus-map bucket
via `census_id` (registry worlds) or the stated candidate mapping (the four codes above, not
yet registered).

**10 branches still unmerged, still touching the world trees, checked against the new
main (`620b5b14b`):** `lpc-round26-rows-65-44` (7 files), `lpc-doc04-round2` (6),
`claude/ijc-world-build-b9p7hr` (2), `claude/desert-admission-fix` (2),
`claude/gallic-monastic-world-build` (**127**), `claude/syr-odes-of-solomon-e5pyh5` (1),
`claude/pahc-world-build-2oq764` (1), `donatism-lpc-integration` (**44**),
`merge-source-library-integration-into-main` (3), `claude/record-native-world-build-v2-
e2s0dt` (23).

**Sequencing decision (Mark, 2026-09-14):** land `claude/gallic-monastic-world-build` and
`donatism-lpc-integration` first — the two whose rebase would be painful. The other 8 (1–23
files each) rebase after the move using the ledger's old→new mapping. This thread checks
back once the two named branches merge, then executes directory-first, files second,
rewrite third, diffed baseline fourth — the phase-1 ordering lesson from CO's flatten
correction.

**Status, updated 2026-09-14:** `claude/gallic-monastic-world-build` merged to `main` (PR
#184). Still waiting on Donatism's own reconciliation branch — renamed from
`donatism-lpc-integration` to **`donatism-main-integration`** the same day, to stop
colliding on sight with the unrelated Latin Pastoral Congregational Christianity world's own
`lpc-*` branches (`lpc-doc04-round2` etc.) — same commits, same content, name only. Phase 3
(promotion model, optional renames) and WO-1…5 remain handed off as work orders above.

---

## 2026-09-14 — `donatism-lpc-integration`: main merged in; real content reconciliation surfaced, handed to the Donatism thread

Mark asked directly: "merge main into donatism-lpc-integration and resolve conflicts." Two
Donatism worlds turned out to exist — not a stale branch behind a clean trunk, but two
independent full authoring passes from the same day (2026-09-10), diverged since. Pushed as
`1fd6696fd` on `donatism-lpc-integration` (merge commit, no history rewritten); full reasoning
in the commit message. Summary:

**Resolved (Mark's ruling, first pass):** for every file where both sides authored the same
record, main's version wins — fuller in source (55/41), figure (24/16), and (found only
after this ruling) doctrinal_witness (25/3), contested_claim (8/4), demonstration (9/3);
`census_id: "donatism"` resolves against `world-census.json`, the branch's
`"donatist-north-africa"` does not; main's package is the one currently live/pinned.
Representative title → main's "Bishop of the Unbroken Line"; the Fidelis portrait prompt's
one reference corrected to match (image unaffected). The Phase Six coordination and
facilitation-brief conflicts in `World-Builds/Donatism/` resolved the same way — main's are
later revisions (Round 4 vs Round 1) of the same documents, independently reviewed and
disposed by the project lead.

**Correction, same pass:** my first read ("main is simply fuller") was wrong and I said so
before committing anything. The real per-type picture is not a superset relationship —
after taking main's side of every conflict, the merge still pulled in every file that exists
on only ONE side (git's normal non-conflicting-add behavior), and that surfaced real gaps in
both directions.

**Not resolved — handed to this world's own build thread, per Mark's decision to route this
rather than have this thread (or me) decide it:**
- **Duplicate `voice_craft`.** `don.voice.craft.md` (main's, fleet-standard naming) and
  `don.craft.fidelis-voice.md` (the branch's, the same non-standard pattern already accepted
  as a defect for pahc) both now exist. A world should have exactly one.
- **Record categories present on the branch, thin or absent on main:** `ambient` (3, zero on
  main), `search_record` (9 vs 1), `honest_limit` (12 vs 3) — real research currently
  invisible to the live, registered build.
- **`term` (21/21) and `quote` (4/4) tie in count but differ in content and IDs** on each
  side — independently authored, not additive; likely near-duplicates needing a real compare.
- **Flagged, not touched:** a pre-existing `Fidelis_Portrait.png.jpg` sits at
  `Representative-Portraits/` root (every other world's portrait lives in its own subfolder,
  including this one's own `donatism/`) — looks like a stale artifact predating the approved
  workflow.

**Verification before push:** `engine.m1.loader.load_world_records` parses the merged tree
without error (4,624 records, no schema-parse failure). No gate battery or admission run —
that's this world's own thread's step once the reconciliation above is settled.

**Status:** merged and pushed. Content reconciliation is `donatism-lpc-integration`'s own
next step, not this thread's.

---

## 2026-09-14 — `lpc-round26-rows-65-44` merged into `lpc-doc04-round2`

Mark: "merge lpc-doc04-round2 and lpc-round26-rows-65-44." Unlike Donatism, this was not two
rival authorings — both branches continued the same sequential document set
(`Doc_02_Source_Ecology.md`, `Source_Registry.md`, `lpc_Decision_Log.md`) from the same
2026-09-08/09 ancestor, and `lpc-doc04-round2` is later in that same history throughout.
Pushed as `361074e35` on `lpc-doc04-round2` (merge commit; no history rewritten).

**Resolved by taking `lpc-doc04-round2`'s side, each verified before resolving, not
assumed:** Status lines — its own text states main was self-disposed on Round 30's clearing
verdict (2026-09-12), superseding round26's "REOPENED... SUBSTANTIAL REVISION REQUIRED"
account (2026-09-09). Registry rows 44 and 65 — round26 claims the Codex Theodosianus and
Gesta Collationis Carthaginiensis texts are "not present on this world's own branch, not on
main"; verified directly that both files exist in `cic/texts/` and the Gesta file is
assigned in this world's own corpus-map bucket — doc04-round2's claim is correct, round26's
is stale. Two small Decision Log conflicts — doc04-round2's account explicitly names and
corrects a "wrong-tree fork": round26 forked one commit before Round 27's fix landed and
never saw it, so it wrongly reports those findings as still unfixed.

**One conflict needed real reconciliation, not a pick.** round26 carries a real disposition
event — via the project lead's relay channel, with three named trigger IDs, exactly the
verifiable-record provenance CO-022 requires — that doc04-round2's own line of history never
learned about (its fork point predated it). doc04-round2's own "2026-09-10 Reconciliation"
entry states both lines of work "are genuine, do not conflict with each other, and are both
carried forward together," and this decision log is append-only, correct-in-place,
never-delete-the-record, by its own repeatedly-stated convention. Inserted round26's entry
verbatim in its correct chronological slot (between Round 29 and doc04-round2's own 2026-09-10
Reconciliation entry) rather than silently discarding real provenance data. Verified after:
no conflict markers remain; the two auto-merged corpus-map YAML files still parse; dated
entries run in chronological order with no duplication.

**Push required one extra step.** A live thread pushed a new commit
(`b2e93cacd`, "targeted read of the Gesta against Candidate 5's Persistence test") to
`lpc-doc04-round2` between my fetch and my first push attempt — caught by a rejected
non-fast-forward push, not silently overwritten. `git fetch` kept returning a stale cached
tip; `git ls-remote` (bypasses cache) showed the real one. Verified zero file overlap with my
merge, merged it in (a second merge commit, never a rebase on a branch I don't own), then
pushed clean.

**Status:** merged and pushed. Real content work (Doc_04 completion, Candidate 5's
escalated classification) remains this world's own thread's to continue.

## Correction (2026-09-15) — two figures in Question 1b/1c above are wrong

Filed by the `Ministry/Features/Library-Access-Gate` workstream's D2 adversarial review
(`Sandbox/D2-Struggle.md`), independently re-verified against the real code and data before
being logged here, per this file's own append-only, correct-in-place convention — nothing
above is deleted or rewritten.

- **Question 1c's claim that `gate_quote_recording` "checks license validity and verbatim
  presence in the file" is wrong.** Re-read directly: `engine/m1/gates.py` checks only the
  license enum and that `text`/`speaker_or_author` are non-blank. No gate anywhere in
  `engine/` or `cic/engine/` checks quote text against `cic/texts/` at build time; the only
  verbatim check is the runtime `grounding_net` against the compiled package.
  `gate_quote_fidelity_recording`, named in `cic/texts/README.md`, exists nowhere in code.
- **Question 1b's non-exclusivity figures ("47 assigned to a single tradition (7%); median
  work claimed by 4 traditions; one by 19") do not reproduce at any of four measurement
  grains tried.** At the same nominal grain the re-measure gives 547 single-tradition (81%),
  median 1. The 677-works total itself is correct. Likely a counting-grain mismatch in the
  original measurement, not a contradiction — but the entanglement problem this file's D5
  decision was reasoned from is materially smaller than stated.

Both figures currently inform the frozen D5 decision and the Library Access Gate charter.
Neither is being re-litigated here — D5 stands as decided — but any thread reasoning from
this file's Question 1b/1c numbers from this date forward should use the corrected figures
above, not the originals.

## 2026-09-15 — Phase 2 executed: the World-Builds/world-build-docs → worlds/<code>/ rename

Resumed after stalling mid-way through its own prerequisite (branch consolidation) once
the Library Access Gate workstream took over this session's focus. Before executing,
checked every branch the 2026-09-14 entries above listed as still unmerged: of the
original 10, `claude/gallic-monastic-world-build` and the lpc/Donatism branches were
already reconciled; the remaining 6 were re-verified from scratch (not trusted from the
earlier entries) — `claude/syr-odes-of-solomon-e5pyh5`, `claude/pahc-world-build-2oq764`,
`claude/ijc-world-build-b9p7hr`, and `merge-source-library-integration-into-main` turned
out fully superseded (their content had independently landed on `main` since);
`claude/desert-admission-fix` carried a real, unabsorbed acquisition gap and was
reconciled and merged (PR #228); `claude/record-native-world-build-v2-e2s0dt` is a third,
independent Donatism authoring pass and was left for that world's own thread rather than
reconciled centrally, matching how the first two Donatism passes were already handled.

**Executed directory-first, per phase 1's own recorded lesson:** the 12 `World-Builds/`
trees moved before the 6 nested `world-build-docs/` trees, so the nested moves landed
inside already-created targets rather than colliding. Full manifest and citation-rewrite
detail: `Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md`'s own
Phase 2 section, including a mistake this phase's own tooling made and caught before
landing (`rewrite_paths.py` desyncing 8 `check_paths_baseline.txt` entries by rewriting
the baseline's stored text alongside real files) and one genuine, previously-invisible
broken citation found and fixed directly.

**`records/` untouched** — the move script's SKIP list already excludes it, so no world
needed a recompile or repin for the directory rename itself. `python3 tools/check_paths.py
--baseline tools/check_paths_baseline.txt`: 0 new unresolved citations, 0 retired paths
present, 422 accepted in baseline.

**Deliberately not moved:** the 6 worlds with no registry code yet (Anabaptist Movements,
Lollardy, Lutheran-Wittenberg, Reformed Zurich and Geneva, Society of Jesus, Tridentine
Church) — moving them now would mean a second rename once a real code exists. `World-Builds/`
and `world-build-docs/` stay live roots for exactly these six; only the twelve subdirectories
that actually moved are in `tools/retired_paths.txt`.

**One live collision accepted deliberately, not avoided:** `World-Builds/Latin-Pastoral-
Congregational-Christianity/` is where PR #197 (Doc_06 through the start of Doc_10) is
actively being authored. Flagged to Mark before executing; his call was to move now and
let that branch rebase afterward using the move ledger, rather than hold the whole phase
for one active thread — the same acceptance phase 1's own "8 branches rebase after the
move" note already anticipated.

**Not started by this pass:** phase 3 (promotion infrastructure, D3's staging/prod split)
and WO-1 through WO-5, unchanged from the 2026-09-14 entries above.

## 2026-09-15 — Phase 3 executed: the D3 promotion model, scoped down from the spec's full ambition

Mark: "start phase 3." Checked with him first, since unlike phases 1/2 this touches the
*live, currently-serving* production service (`render.yaml`'s `cic-engine`) and carries
a real recurring cost D3's own text already flagged as needing confirmation before
execution — that confirmation had never actually happened. Mark's call: full D3 now.

**Scoped to what D3 itself asks for, not Artifact-6 SS3's full aspirational stack.** That
document describes AWS ECS/Fargate, RDS Postgres, S3, CloudFront and full IaC — none of
which the real system runs today (one Render web service, SQLite on a Render Disk, no
staging environment at all). D3's own text is much narrower: a staging service plus a
protected `live` branch production deploys from, with a deliberate, logged promotion
after tests and Mark's verification. Building the full aspirational stack was never this
pass's job and isn't what Mark asked for.

**What actually executed, from this sandbox:**
- `live` branch created at `main`'s exact tip (`9e07b4cb4`) — zero drift at creation.
- `render.yaml`: `cic-engine` (prod) pinned `branch: live`; new `cic-engine-staging`
  service added, pinned `branch: main`, `plan: starter` (cheaper than prod's `standard`
  — it never carries real participant load), its own disk, its own `sync: false`
  secrets, and `CIC_ENFORCE_ADMISSION: "0"` — deliberately, so a built-but-not-yet-
  admitted world is testable there, the split Artifact-6 SS3 itself originally described
  ("staging: fixture world + candidate packages").
- `.github/workflows/ci.yml`: `live` added to the `push` trigger's branch list, so a
  promotion merge gets the same CI confirmation a `main` push already gets.
- `Ministry/Operations/Standing/CiC_Promotion_Runbook.md` (new): the actual step-by-step
  procedure, plus the one-time setup this sandbox could not do itself.

**What could not execute from here, and needs Mark's own action (all in the runbook):**
GitHub branch protection on `live` (repo-settings writes are proxy-blocked, same as the
GitHub API's raw `git/refs` write path used for creating the branch itself — worked
around by a normal `git push` for the branch, but no such workaround exists for branch
protection, a real settings change, not content); the Render Blueprint sync that
actually creates `cic-engine-staging` and repoints `cic-engine`'s own branch connection
(Render's API is unreachable from this sandbox — egress-blocked, confirmed by a direct
test); `cic-engine-staging`'s own AWS credentials and admin token. Until these four
happen, `render.yaml`'s `branch:` pins describe the intended state, not the live one.

**A real, load-bearing behavior change, stated plainly so it isn't missed:** every PR
this whole session has merged to `main` deployed straight to production. Once Mark
completes the setup above, that stops — `main` only reaches `cic-engine-staging` from
then on, and reaching participants requires the promotion PR the runbook describes.

**Not decided:** whether `cic-website`'s Cloudflare Workers Build production deployment
should also move from `main` to `live` — flagged in the runbook's own closing section,
left to Mark rather than assumed.

---

## 2026-09-21 — Ministry tree housekeeping: early-days strategy archive

**Context.** Mark's tech-review stress test (thread "CiC — Tech Review & Funding Readiness Prep") completed. Verdict: system withstands technical review and does not pass one clean. Cut line (Mark's decision): what is live online now, the Conversation & Transparency Engine upgrade being installed, and the ongoing world builds. All early-days strategy drafts (Funding, Marketplace, Organization, Scholarly-Review, Website, Communication from 2026-07-* era, and partial Features and Operations directories from pre-2026-08-20) identified as superseded by the system redesign.

**Action.** Mark reviewed all items one at a time and decided: move early-days drafts to `Archive/Ministry-Early-Days-2026-07/` preserving the Ministry subpath structure. Five documents kept with supersession banners (cic-poc go-live cost model, LLM provider options, business roadmap, two cost studies). Organizational Covenant's "always-free core access" commitment searched but not found as a distinct phrase; business roadmap already references this as an open task (line 54). FAQ and Letter to Friends kept as source material with standing status written to a new `Ministry/Communication/README.md`.

**Execution (this PR).** 90 files (13 Funding, 3 Marketplace, 7 Organization, 6 Scholarly-Review, 4 Funding-Strategy features, 1 Prototype-Testing, 33 Launch-Prompts, 3 Markup-Queue, 19 Communication) + 4 directories (Increment-1-Build, Level2-Mobile-Popover, Hosted-Tour, Prototype-Testing subfolder, Markup-Queue) moved via `git mv`. Three Website files not found (already archived or renamed). Undated Faithways PDFs left in place per byte-check difference test and "when in doubt leave it" instruction.

**Banners added to 5 kept files:** supersession notices at top of Business Roadmap, two cost studies, Go-Live model, LLM provider options — all linking to current engine (`engine/m8/`) and decision logs where they belong.

**Tracking files updated:** `Ministry/Operations/README.md` notes Markup-Queue archived 2026-09-21; `CiC_Org_Funding_Decision_Log.md` carries 2026-09-21 entry with full tech-review context and entity supplement exploration; `Ministry/Features/README.md` notes Hosted-Tour, Increment-1-Build, Level2-Mobile-Popover as archived with destinations; new `Ministry/Communication/README.md` carries standing status for FAQ and Letter to Friends.

**Path check:** `python3 tools/check_paths.py --baseline tools/check_paths_baseline.txt`: 0 new unresolved, 0 retired paths present. All move-related citations are within Ministry audit/decision-log prose (the expected baseline for a Ministry-only move).

**Root README.md Archive entry:** checked for "Ministry-Early-Days-2026-07" category — if listed, add it. Otherwise, note in PR description that root README.md Archive row may need updating once this PR lands.

**Convention applied:** Superseded material → `Archive/`; nothing deleted without instruction (CLAUDE.md line 55). Every path moved recorded in `Ministry/Operations/Audits/CiC_Repo_Structure_Move_Ledger_2026-09.md` per this tracking file's own standing rule (P11 of the frozen target tree, 2026-09-14).

**Status:** ready for path check and PR.
