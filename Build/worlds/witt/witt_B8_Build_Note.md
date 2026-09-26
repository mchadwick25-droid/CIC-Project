# B-8 Build Note — Lutheran Wittenberg & Its Congregations (witt)

**Date:** 2026-09-19. **Status:** B-8 (S2.8, "Generated views + four parities")
complete for this world, scoped to what is actually executable for a
first-ever record-native build, per the identical structural finding
Cappadocian's and Gallic's own B-8/B-9 work already made and independently
re-confirmed here rather than assumed to transfer.

## What B-8 is, as the governing process document currently states it

`Build/reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`, row B-8
(S2.8): "Chunk views GENERATED from records; render parity (0 unclassified
defects); retrieval parity vs the committed production baseline (the
verdict rule: isolation-harness reproduction is diagnosis only — the
production eval against the committed baseline is the verdict; FLAG-033's
lesson); prompt coverage (zero GAPs); probe parity (held-out probes, blind,
two-trial — deployed-side true-positives become record-derived guard
candidates, the FLAG-030/036 class)."

## Independent verification, not assumed from Gallic's precedent

1. **Confirmed the `wrs/views/s62_*_{render,retrieval,prompt_coverage,probe}_parity.py`
   scripts this row and Appendix A cite still do not exist anywhere in this
   repository.** A repo-wide search for `wrs/views/s62_*` returns nothing;
   `cic-poc/` retains only `README.md` and `frontend/` — `cic-poc/backend/`
   is gone. Same finding as Gallic's own B-9 note, independently re-checked
   here rather than carried forward on that finding's word alone.

2. **Confirmed witt has never had a hand-authored production deployment to
   diff parity against.** No `data/witt_world/` or equivalent directory
   exists anywhere in this repository; no prior `packages/witt/` entry
   existed before this pass (`ls packages/` returned nothing for `witt`
   before this build). This world was built record-native from Doc_01
   forward. "Retrieval parity vs the committed production baseline" and
   "render parity" (against a prior deployed version) both presuppose a
   baseline this world does not have — the same structural gap Gallic's
   own B-9 note found for the identical row.

3. **What is actually executable, run and independently re-verified here:**
   - `python -m engine.m2.cli determinism-check witt` — compiled the world
     twice from the same records commit, diffed the two outputs in memory.
     Result: `{"pass": true, "differing_paths": []}`. This is render
     identity/determinism, the closest thing this first-ever build has to
     "render parity" — there being no prior deployed render to diff
     against.
   - `python -m engine.m2.cli build witt` — compiled the actual package
     (`packages/witt/2026-09-19T05-06-48Z/`, manifest hash
     `sha256:545007e2f95d89a2945e191ada6022abbb2ce4cb3d54f77e3d76550b93fa42f7`).
   - The compiled package's own `validation/gates-report.json` re-read
     directly and independently: all 18 gates present, `"pass": true` on
     every one, 0 findings total — matching the pre-compile gate run
     against `load_world_records('witt')` from the Answer-the-Canon step.
     This is the closest equivalent this first-ever build has to a
     "production eval," since there is no pre-existing baseline to diff
     against, matching Gallic's own reasoning for the identical row.
   - Package contents spot-checked directly: 251 records (matching the
     228+23 count from B-1 through the Answer-the-Canon step exactly),
     109 compiled files, `compiled/prompt.txt` (118,306 bytes) and
     `compiled/capsule.md` (2,222 bytes) both present and non-empty,
     `compiled/prompt.txt` confirmed to carry real world-specific content
     (sexton/schoolmaster role language present; register and pronoun-rule
     sections present) rather than an empty or templated stub.
   - Confirmed by direct grep that "Nikolaus" does not appear literally in
     `compiled/prompt.txt` — checked this is correct, not a build defect:
     every occurrence of the name in `records/witt/` sits in a record's own
     dated body note (below the closing `---` fence), never in operative
     frontmatter, per this project's own CO-022 file-discipline rule that
     a Representative's name is a build-thread judgment carried at the
     identity-decision and deployment-wiring layer, not a record field the
     compiler reads (spec principle 14, cited directly in
     `engine/m2/builders.py`'s own `build_prompt` docstring).
   - "Prompt coverage (zero GAPs)" — satisfied by the same canon-coverage
     gate already independently re-verified twice this session (once
     directly against loaded records, once again inside the compiled
     package's own gates-report): 0 findings, all 16 cells the
     Answer-the-Canon step closed remain closed in the compiled output.
   - "Probe parity (held-out probes, blind, two-trial)" — this is live,
     API-spend validation territory (the sealed probe battery
     `engine.m4.turn.apply_net` runs against, per Gallic's own B-9 note),
     out of this build thread's own scope without the project lead's
     separate authorization. Not attempted here, named explicitly rather
     than silently skipped.

4. **Registry updated to reflect the compiled package**, matching the
   documented convention in `engine/BASELINES.md` ("compiled packages...
   rebuild deterministically from records and are verified at load against
   these hashes in `records/worlds/<code>.yaml`"): `records/worlds/witt.yaml`
   now carries `package: {manifest_hash, location}` for this build, and
   `state` moved from `building` to `built` — confirmed against the live
   registry that `built` is a real, self-disposable intermediate state two
   other worlds (`don`, `fix`) currently sit at, distinct from `admitted`
   (the Mark-only M3 live-spend gate) and `open`. Only this build's own
   pinned `manifest.json` was added to git, per the stated discipline that
   an unpinned package manifest is an orphan to be swept, not tracked.

## Verdict

B-8's generated-views and render-identity/gate-coverage work is complete
and independently verified. The two sub-checks that require either a
pre-existing production baseline (render/retrieval parity) or live
API-spend (probe parity) do not apply to a first-ever record-native build
with nothing to diff against and no authorization yet to spend — named
here as out of scope rather than forced or silently skipped, exactly as
Gallic's own B-8/B-9 work handled the identical structural situation.

See `witt_B9_Scoping_Note.md` for B-9's own disposition.
