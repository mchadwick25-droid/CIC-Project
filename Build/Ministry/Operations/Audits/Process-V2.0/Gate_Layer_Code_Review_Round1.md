Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Round: 1
Truncation check, method 1: direct Read of both L4 templates end to end (Review_File_Header_Template.md ends at line 9 "# Review of <document>"; Probe_Result_Record_Template.md ends at line 42, the empty results row) and tail -n1 of every engine/m10 and engine/m7/turn_readability.py module (each ends on its final return or sys.exit line)
Truncation check, method 2: wc -l, wc -c and a final-newline byte check on both templates (9 lines/206 bytes and 42 lines/2058 bytes, both newline-terminated, git hash-object equal to the committed blob), plus python -m py_compile on every engine/m10, engine/m10/tests, engine/m7 turn-readability, m1 gates, m9 enforce, m4 world_loader and tools module (all compile)

# Review of the gate layer (engine/m10, engine/m7 turn readability, m1/m9/m4 edits, tools, CI, two L4 templates)

Scope: commits 307cc53d and 7951b135 against the pre-work state 7521c09a. Spec: CONVERGED_SPEC "Gate layer" items a–r; Process V2.0 Section 3 and Section 8.

## Verdict

Substantial revision required. The layer is well built and its test suite is green, but eleven substantial findings stand. Three of them pass work the process says must fail (1, 2, 5). Two would turn CI red on legitimate pull requests, including this one (7, 8). One spec item, the per-turn readability hard-fail, exists only as an uncalled function (9).

## Test and tool results

- `python -m pytest engine/m10 engine/m7 engine/m9 engine/m1/tests tools/tests -q`: 624 passed in 694.9 s.
- `python tools/check_paths.py --baseline tools/check_paths_baseline.txt`: exit 0; 0 new, 966 accepted in baseline.
- `python tools/check_live_commentary.py --help`: prints usage with `--base` and `--enforce`; runs with every third-party import blocked (the CI job installs nothing, which is correct).
- `python tools/check_live_commentary.py --base 7521c09a --enforce`: exit 1, 273 REWRITE/ROUTE lines (see finding 8).
- `records <code>` on every world: `fix` and `_fleet` fail, `lpc` fails for lack of a registry entry, the rest pass (see finding 7).
- `python -m pytest engine/m4 engine/m2 -q`, run to test the loader guard for regressions: 649 passed and 7 failed. All 7 failures are environmental. The compiled package files are not restored in this checkout; CI runs `engine.m2.cli restore` first. Six `test_world_loader.py` tests get past `assert_compiled_target` and then stop on "manifest lists 'compiled/capsule.md' but it is missing on disk". `test_restore.py` finds nothing to strip. The guard caused no failure.
- The `engine/api` tests could not run here, because fastapi is not installed locally. Finding 11 argues the loader guard's effect on them from the code.

## Findings

### 1. Handoff treats "Not Approved to proceed" as cleared (substantial)

`engine/m10/handoff.py:21` and `:156-157`. `CLEARED = re.compile(r"approved to proceed")` is searched anywhere in the latest review file. The fleet's own review files write the negative verdict as "Not Approved to proceed" (25 files under `Build/worlds/` carry that phrase). A Step 0–2 review that refused clearance passes checks 2, 3 and 4.

Proof: fixture world with `Doc_01_Review_Round1.md` verdict "Verdict: Not Approved to proceed." → `run_handoff` reports no failing check; expected `handoff-03-step1`.

Fix: require a positive verdict line (for example a `Verdict:` field whose value begins with "Approved to proceed"), and treat any "not … approved to proceed" as uncleared. Add the negative case to `test_handoff.py`.

### 2. An invented quotation passes the quote check when a second project document repeats it (substantial)

`engine/m10/quotes.py:262-273` and `:326-335`. A quotation not found in any `cic/texts` file is exempted when its text appears in any other `.md` under the world's folder, `_cross-world/` or `Build/reference/`. Only the document being checked is excluded. Steps 0–2 are three documents plus the Source Registry, so an invented quotation copied from Doc_01 into Doc_02 exempts itself in both. This is the fabrication case check (b) exists to catch.

Proof: fixture world with the same invented 14-word quotation in Doc_01 and Doc_02 → `handoff-08-quotes` has no finding; the same quotation in Doc_01 alone → `quotes-unverified`.

Fix: exclude every document under check (all Step 0–2 files and the registry) and the world's own later build documents from the exemption set, and report exempted quotations as notes always, not only with `--verbose`.

### 3. `handoff --skip-quotes` exits 0 (substantial)

`engine/m10/handoff.py:432-436` with `common.py` `Report.ok`. The skipped check has no findings, so `emit` returns 0 and the handoff passes with check (b) never run.

Proof: fixture world with an invented quotation: exit 1 with quotes, exit 0 with `quotes=False`.

Fix: a skipped required check makes the run incomplete, not a pass: exit non-zero (or a distinct exit code) whenever any report is `skipped`, and keep `--skip-quotes` for local iteration only.

### 4. The reviewer-is-not-drafter check compares unnormalized model strings (substantial)

`engine/m10/reviewfile.py:118-124`. Independence is tested as `reviewer.lower() == drafter.lower()`. "Drafter model: Opus 5.5" (or "Claude Opus 5.5") against "Reviewer model: claude-opus-5-5" passes. The check also tests the model, not the agent: an Opus-authored `modern_rendering` pass reviewed by a separate Opus agent (CLAUDE.md's rendering rule) is a legitimate review this check fails.

Proof: header with `Drafter model: Opus 5.5` → no `reviewfile-independence` finding.

Fix: normalize both values to a model id (the same way the reviewer value is required to be `claude-opus-5-5`), reject a drafter value that is not a recognized id, and record the independence the process actually requires (a drafter session or agent field that must differ from the reviewer's) rather than inferring it from the model.

### 5. The trigger detector prints `lean` when a trigger cannot be evaluated (substantial)

`engine/m10/validation.py:155-156` and `:303`. The safety-adjacent trigger is always "undetermined", but the verdict is `full` only when a reason fires, so every world without another trigger is declared `lean`. CLAUDE.md: near anything safety-adjacent, default to caution. This fails open on exactly the trigger that most needs to fail closed.

Proof: `detect_triggers({}, [])` → no reasons, one undetermined item, verdict `lean`.

Fix: any undetermined trigger yields verdict `undetermined` and a non-zero exit (or `full`) until the registry field in question 5 exists.

### 6. The new-world waiver rule does not cover the m1 cross-world waivers (substantial; spec item j partly missing)

`engine/m10/regate.py:216-248`, `engine/m1/cross_world.py` `ACCEPTED_OPEN`. The rule is enforced in `engine/m9/enforce.py` (m9 waivers) and, in `records`, only for keys starting `required-record-type/` or `required-site-json/`. Nothing checks the other m1 cross-world waiver keys (`figure-dates-keys/<code>`, `quote-speaker-label/<code>`, `ui-field-leak/<code>`, …) against `GRANDFATHERED_WORLDS`, and `regate` checks no waivers at all, though Process V2.0 Section 3 says the re-gate "confirms a new world carries no waivers and grandfathering stays closed".

Proof: adding `cross_world.ACCEPTED_OPEN["figure-dates-keys/fix"]` (`fix` is not grandfathered) → `run_records("fix")` reports nothing about the waiver.

Fix: one check, run by both `records` and `regate`, over every key of both waiver registries whose world segment is outside `GRANDFATHERED_WORLDS`, with the same owner-plus-lead-approval exception `enforce.new_world_waiver_problem` applies (cross_world's `dict[str, str]` shape needs an approval field to carry that).

### 7. `records` fails every world that is not yet admitted, so the world-gates job fails Phase B pull requests (substantial)

`engine/m10/regate.py:239-245` against `engine/m1/cross_world.py:628-629`. The m1 check requires `world_front`, `facilitator_brief`, `search_record` and the site JSON only for worlds in state `admitted` or `open`. `records` requires them of every world. Process V2.0 authors `facilitator_brief` at B-7a, so every records pull request from B-1 to B-7 fails the new `world-gates` CI job (`.github/workflows/ci.yml:302-326`). The fixture world already fails today.

Proof: `python -m engine.m10.cli records fix` → FAIL: no `facilitator_brief`, no site JSON. `fix` is state `built`.

Fix: apply the required-type findings at the state the m1 gate uses (admitted/open) or behind an explicit `--freeze` mode used at freeze; keep `waiver-not-allowed` unconditional. Decide whether `fix` must carry the three types (then add them) or is exempt by state.

### 8. `live-commentary --enforce` fails this pull request, mostly on false positives (substantial)

`.github/workflows/ci.yml:283-296`, `tools/check_live_commentary.py` `main`. Against the pre-work base the job reports 273 blocking lines in files this branch edits. 232 remain after the engine/m10 rule proposed under question 2. They sit almost entirely in method documents that describe the review process: Process V2.0 (131: 84 of them `change-history-block` hits on the model-routing table), the Voice Style Guide (59), the six skills and four templates. "Reviewer", "round 1" and "open item" are the subject matter of those documents. Made blocking, the job goes red on every future edit to the method library.

Fix: before `--enforce` blocks, either clean the reference surface in its own pull request or scope enforcement to surfaces whose false-positive rate has been measured (the labelled sample in `tools/tests/test_check_live_commentary.py`), with `reference` and `worlds` report-only until a rule separates methodology prose from narration. Changing the scope of enforcement is a governance change for the project lead.

### 9. The per-turn readability hard-fail is never called (substantial; spec item r not implemented)

`engine/m7/turn_readability.py`. Nothing in `engine/`, `tools/` or CI imports it except its own test. No probe runner, live battery, `validation` result check or turn path calls `assert_turn_readable` or `report_turns`, so no turn ever fails on readability. CLAUDE.md line 23 still cites the non-existent `phase2_checkpoint.py`; the spec asked for that reference to be corrected.

Fix: call `report_turns` from the probe and live battery result checks (the `validation` command reading the saved transcripts is the natural home), fail on any entry in `failed`, and correct the CLAUDE.md reference (a CLAUDE.md edit needs the project lead).

### 10. `citations <code>`, as the process documents it, does not run (substantial)

`engine/m10/deployed.py:462-465` and `:477-479`. The subcommand requires an explicit file list; Process V2.0 Section 3 documents `citations <code>` "on every document and every probe file". `python -m engine.m10.cli citations alx` exits 2 with an argparse error. The same table assigns the result-label check to `probes <code>`, but that check lives in `validation`.

Fix: with no files given, check the world's build documents and every `probe_result_files(code)`; correct the Section 3 row for the result-label check (or have `probes` run it).

### 11. The loader guard refuses the default local package-cache layout (substantial)

`engine/m4/world_loader.py:114` calls `assert_compiled_target`, which inside the repository accepts only `packages/<code>/<pin>/compiled/prompt.txt` (`engine/m10/deployed.py:84-87`). `engine/api/config.py:141` defaults `CIC_API_PACKAGE_CACHE_DIR` to `REPO_ROOT/packages`, and `engine/m4/package_fetch.py:47` fetches into `cache_dir / location`, so a fetched world lands at `packages/packages/<code>/<pin>/`. Any local or test run with object storage configured and the default cache refuses every fetched world. Render sets `/data/packages-cache`, outside the repository, so production is unaffected.

Proof: `assert_compiled_target(REPO_ROOT/"packages/packages/fix/2026-09-26T20-12-08Z/compiled/prompt.txt")` → `ProbeTargetRefused`.

Fix: make the guard's in-repo rule "the last four parts are `<code>/<pin>/compiled/prompt.txt` under a `packages` directory, and nothing under `Build/` or `Archive/`", or move the default cache outside the repository. Symlinks and relative paths are handled correctly (see Not findings).

### 12. A list insertion makes untouched failing list items fail the re-gate (minor)

`engine/m10/regate.py:78-82` and `:172`. Fields are matched to the base by `(record id, label)`, and list labels carry the index (`characteristic_concerns[1]`). Inserting an item shifts every later index, so an unchanged item that already failed at the base now counts as edited and fails.

Proof: base `characteristic_concerns: [DENSE]`, head `[CLEAR, DENSE]` → `characteristic_concerns[1]` fails.

Fix: count a field as unedited when its exact text is among the same record's base field texts.

### 13. A flagged living tradition with no `world_core.living_traditions` text is only a note (minor)

`engine/m10/deployed.py:223-224`. Spec item k requires the compiled prompt to carry the confirmed living-traditions item. When the registry sets `living_tradition_flag` and `world_core` has no text, `deployed` passes with a note. 11 of 13 existing worlds lack the field, so a hard failure should apply to non-grandfathered worlds only.

### 14. A known-failing Library test is left non-blocking without a registered gap (minor)

`.github/workflows/ci.yml:355-358`. `tests_corpus_map.py` runs with `continue-on-error: true` because it fails on the current map. CLAUDE.md requires a known defect that is not being fixed now to be registered (an `ACCEPTED_OPEN` waiver or an `Open_Gaps_Tracking.md` entry with its owning finding). None is cited.

## Answers to the lead's questions

### Q1. Does each subcommand do what the spec says?

Each was exercised by the suite (624 passing tests, each with a passing and a failing fixture) and by the fixtures above.

- `handoff`: all twelve checks present and each has pass/fail tests. Defects: findings 1, 2, 3.
- `prereview`: runs m2 build (in memory, same compiler), bar screen, cross-world and holdings in order and stops at the first hard failure; skips when `records/<code>/` does not yet exist, which is right before Phase B.
- `roundcount`: counts distinct round numbers per document; blocks round 4 and any new round once three exist. Correct.
- `reviewfile`: label, five header fields, Opus id, differing truncation methods, round matching the file name. Defect: finding 4.
- `gaps`: open items under open-item headings and inline "Open item:" lines matched against the ledger; bare-number cross-references flagged. Correct at the stated bar.
- `citations`: resolves ids, wrong namespace, wrong type, `cic/texts` paths. Defect: finding 10.
- `deployed`: self-reference hardening, quote and gravity index sets, `[quotation]` counts, staleness. Defect: finding 13.
- `probes`: pin named, pin known, guard dry-run. Correct; the label check is in `validation` (finding 10).
- `validation`: columns, observed/authored, transcript resolves, authored never PASS/FAIL, four grades, RS-1/RS-2 separate, RS-2 PASS only for the Facilitator. Defect: finding 5; trigger definitions under Q5.
- `wiring`: scripted client, no network; control turn reaches the voice; both governed routes produce a Facilitator safety turn with no voice call, in the interview and the table round. Correct.
- `records`: defects 6 and 7.
- `regate`: see Q3.

### Q2. The live-commentary lines in engine/m10 and the header template

Against base 7521c09a the files in scope carry 41 lines: 14 in engine/m10 modules, 26 in engine/m10 tests, 1 in `Review_File_Header_Template.md`. All 41 are classifier false positives; none is commentary.

- `reviewfile.py:12, 70, 72-76`, `fixture_world.py:31`, `test_reviewfile.py:41, 42, 63`, and template line 3: the word "reviewer" is the mandated header field name and the variables that read it.
- `cli.py:110`, `common.py:13` (the "tbd|todo" placeholder regex), `gaps.py:12, 15, 73`, `handoff.py:402`, `matching.py:9`: "open item", "unresolved", "known gaps" and "TODO" are the vocabulary the gate itself detects.
- engine/m10 tests (iso-date, route-cue, one seeded "Revised after Round 2 review by the reviewer" line): seeded fixture strings that exercise the detectors, the same role `fixtures/seeded_defects.yaml` plays.

Rewording cannot fix these: the field names are fixed by the template, and the regexes must contain the words they match.

Recommended rule, scoped narrowly, and tested:

1. In `engine/m10/*.py` (not tests), a hit whose patterns are only `reviewer` or `route-cue` on a line that is code (not a comment or docstring, found with `tokenize`) is KEEP.
2. In `engine/m10/tests/*.py`, a code line (a fixture string) is PROTECTED; comments and docstrings there are still scanned.
3. In any `.md`, a line that is exactly `Reviewer model: <value>` or `Drafter model: <value>` is KEEP.

A general "Python code lines are never commentary" rule would weaken detection. It flips two hand-labelled REWRITE samples that are code lines: `engine/m4/tests/test_turn.py:1131` (an `r27_regenerated` key) and `Build/worlds/don/scripts/wb_don_s21.py:450` (a string literal). The scoped rule was applied as a patch over `scan_file` and the existing suite rerun. All 163 tests in `test_check_live_commentary.py` and `test_check_live_commentary_scope.py` pass. All 41 lines clear. In a whole-tree scan, exactly one line outside engine/m10 changes category: the template's header line. This rule does not touch finding 8's method-document lines.

### Q3. Regate semantics

Verified with a fixture on `compare_world`. An edited field that regresses fails, on both FK and FRE. An untouched field that already failed at the base is counted in a note ("1 unchanged field(s) already failed at the base; not a regression") and does not fail. An edited field that is still over the ceiling fails even if it improved, which matches "re-run on every changed field". The voice-craft budget fails a new record, or one that crosses the ceiling or grows while over it.

Public-facing coverage is every field `engine/m1/spoken_fields.py` gives an instruction, voice-diet, evidence-head or facilitator-spoken role, taken from the M1 gate's own `_readability_checks`. On top of that come the prose keys of `world_front` and `facilitator_brief` (`text`, `teaser`, `note`, `hedge`, `cautions`). The site JSON is compiled from `world_front`, so it is covered at its source. Quote and story originals are excluded by design. Their `modern_rendering` and `tellable_as` companions are graded. Exception: finding 12.

In CI, `--base origin/<base_ref>` is passed and `fetch-depth: 0` makes it resolvable. Locally, the fallback chain ends at `HEAD`, which then compares only uncommitted edits.

### Q4. Can a world be added to GRANDFATHERED_WORLDS silently?

No. `engine/m9/tests/test_enforce.py::test_grandfathered_set_is_fixed` pins the set by exact equality, so growing it means editing that test in the same diff, where review sees it. `test_every_waiver_on_a_new_world_carries_an_owner_and_the_project_leads_approval` scans the real registry.

Two limits remain. `approved_by: "project lead"` is a string an agent can type, so the approval is only as strong as pull-request review; citing the decision-log entry that records the approval would make it checkable. And the m1 cross-world registry has no such guard at all (finding 6).

### Q5. Trigger code today and the changes the lead's definitions need

Today (`engine/m10/validation.py:132-156`):

- Thin evidence fires for any gravity (Primary, Supporting or Tensional) tagged Inferential-Thin, and also for a `world_core` tagged Inferential-Thin.
- Contested fires for a primary gravity whose own `formation_confidence` is Contested, and also for any `contested_claim` that is Contested and has a `relations[].target` naming a primary gravity. On `gallic` all three current triggers come from this second branch.
- Fabrication fires for a FAIL or AMBIGUOUS row whose cells contain the substring "fabricat" anywhere (Notes included).
- Safety-adjacent is always "undetermined" and does not affect the verdict (finding 5).

Changes for the proposed definitions (not implemented):

1. Thin: keep only `record_type == "gravity"`, `classification == "primary"`, `confidence.formation_confidence == "Inferential-Thin"`. Remove the non-primary gravity and `world_core` branches.
2. Contested: keep only the primary gravity's own `formation_confidence == "Contested"`. Remove the `contested_claim` relation branch, which also clears `gallic`'s three current reasons.
3. Safety-adjacent: add `safety_adjacent: true|false` to every `records/worlds/<code>.yaml`, all 13 entries including `fix`. No registry schema file exists today, since the registry is read ad hoc by `engine/m2/builders.py` and `engine/m1/cross_world.py`. So "the registry schema change" means adding the field and a validator: handoff check 1 (`_check_01`) fails when the key is missing or is not a boolean. The trigger fires when it is `true`. Its "undetermined" branch goes away, and a missing key at validation time is a failure, not `lean`.
4. Fabrication: add a `Fabrication` column (`yes` / `no`) to `Probe_Result_Record_Template.md` and to `COLUMNS`. Treat a missing or other value as a finding for graded rows, and fire the trigger on `yes`, whatever the Result (a PASS with a fabrication is still a fabrication). Drop the free-text substring match, and remove "A fabrication finding is named here" from the Notes row and the matching rule line in the template.
5. Update Process V2.0 Section 8's three "defined by: project lead, before the pilot" lines with the decided wording. This is a governance edit that needs the lead's convergence.

### Q6. Truncation and compile checks

Both templates pass two methods (header). The direct read and `wc`/byte counts agree, both end in a newline, and each equals its committed blob. Every engine/m10 module (and its tests), `engine/m7/turn_readability.py` and its test, and the edited m1, m9, m4 and tools modules compile with `py_compile`. Each module's last line is a complete statement.

## Not findings

- `engine/m1/gates.py` refactor: behaviour unchanged. `grade_text` applies the same word floor, and FK and FRE are compared against the same constants, with identical messages and order. `voice_craft_prompt_parts` and `voice_craft_word_ceiling` are verbatim extractions. The one comment rewording ("still open" to "undecided") changes no code.
- `engine/m9/enforce.py`: `new_world_waiver_problem` is correct. It needs a non-blank owner and exactly `approved_by == "project lead"`, and all five new tests cover it.
- `assert_compiled_target` is not bypassable by symlink or relative path. `resolve()` follows a symlink at `packages/zz/p1/compiled/prompt.txt` to the Permanent Prompt file, which is then refused. A `..` path into `packages/` resolves and is accepted, correctly.
- CI dependencies: `world-gates` and `library-validators` install `engine/m1/requirements.txt` (pyyaml, jsonschema, anthropic[bedrock], boto3, pytest), which covers every engine/m10 import. `live-commentary` needs only the standard library and `engine.m1.spoken_fields`. No gate makes a network or paid call: `wiring` uses a scripted client, and `deployed` and `wiring` recompile locally.
- `tools/check_paths_baseline.txt`: 92 stale lines were removed and 17 added. Fifteen of the 17 are citations to the V1.3 Standard and V1.9 Process that this branch archived, in review files, decision logs and append-only gap ledgers. Those are accurate history, so a baseline entry is right for them.
- The package-citation rule in `check_paths.py` reads a replaced pin against the live pin. A mistyped pin therefore resolves, which is a deliberate trade for pin churn.
- `engine-tests` now runs on draft pull requests that touch records, packages, engine or world documents. Process V2.0 Section 3 sanctions this. It does widen Actions minutes on engine drafts, which the lead may want to weigh against the 2026-09-23 billing note.
- `prereview` skipping all steps before `records/<code>/` exists is correct for Doc_03–Doc_10.
- The authored-result rule allows authored `AMBIGUOUS` or `ACCEPTABLE FALLBACK`. The spec forbids only PASS and FAIL, but the template says authored is `NOT SCORED`, so the lead may want the stricter rule.
