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

**Status:** phase 1 done, pending merge. Phase 2 waits for Gate B. Phase 3 (promotion
model, optional renames) and WO-1…5 are handed off as work orders above.
