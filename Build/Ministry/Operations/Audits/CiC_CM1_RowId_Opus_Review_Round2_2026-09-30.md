Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus independent adversarial reviewer (subagent, session_01Uo1V6v9bcjuAJYtw5vKRr8)
Drafter agent: Sonnet CM-1 implementation thread
Round: 2
Truncation check, method 1: per-file line arithmetic on commit a3fadff9. `git show HEAD~1:<file> | wc -l` plus added minus removed (`git diff --numstat HEAD~1 HEAD`) equals `wc -l` on disk for both engine files (merge 418+53-36=435, tests 229+36-2=263).
Truncation check, method 2: end-anchor read. The full `git show HEAD -- cic/engine` diff was read to its last hunk, the tests file's tail on disk was matched (`sys.exit(0 if all(results) else 1)`), and the rewritten `assign_ids()`, `work_slug()` and the `--assign-ids` branch of `main()` were read in full from the working tree.

# Review of CM-1 row_id, round 2 (branch `cm1-row-ids`, commit a3fadff9)

Scope: targeted recheck of the round-1 findings (`CiC_CM1_RowId_Opus_Review_Round1_2026-09-30.md`) against `git show HEAD -- cic/engine`, plus new defects the `assign_ids()` rewrite may have introduced. Method: the diff read in full; `python cic/engine/tests_corpus_map.py` run (all new checks pass; the same four pre-existing failures as main); `--assign-ids --check` on real staging (0 to assign); a probe script ran `assign_ids()` on 26 synthetic inputs in a temporary `STAGING`, each beside a clean `vol0.yaml` to test all-or-nothing.

## Bottom line

S1 and S2 are fixed, and the all-or-nothing rule holds on every input that produces a finding. S3 is only half fixed: a null `row_id` is now refused, but an anchor on its own line with no alias is still planned, written, and leaves an unparseable file. Verdict: revise (one substantial finding).

## Round-1 findings

| Finding | Status | Evidence |
|---|---|---|
| S1 flow row shifts later ids | Fixed | Rows and nodes now come from one `construct_document` of one node tree, zipped by index. Flow row between two block rows: finding, no file written. |
| S2 non-mapping item / top-level list crash after writes | Fixed | Scalar item, nested list item, top-level list, empty file, multi-document file and unparseable file are all findings, and no file (including the clean `vol0.yaml`) is written. |
| S3a anchor on its own line | **Not fixed** | See R2-S1. The new test passes only because its input also holds `- *r`, which the alias branch refuses. |
| S3b `row_id:` null | Fixed | Null, empty string and integer ids are findings; nothing written. |
| O1 word-boundary test | Not fixed | `"abcdefghi " * 10` cuts exactly on a hyphen (character 60 is `-`), so a naive `slug[:60].strip("-")` still gives the expected result. A title whose cut falls mid-word is still needed. |
| O4 CRLF | Fixed | CRLF file keeps CRLF on every line after assignment and is idempotent. |
| O5 docstring | Fixed | Now "the first free suffix". |
| O6 unplaceable row reserves an id | Fixed | Unplaceable rows never reach the id loop. |

## Substantial findings (actually wrong)

**R2-S1. An anchor or tag on its own line still writes an unparseable file.** Probe input `- &r` / `  work: A` (no alias anywhere). The mapping node starts at the anchor token, so `lines[line_no][col - 2:col]` is still `- ` and the placement check passes. Output: `- row_id: vol1--a` / `  &r` / `  work: A`, returned with no findings and written; `yaml.safe_load` then fails with `ScannerError`, and every later run on the file reports it as unparseable. The same happens with a tag on its own line (`- !!map` / `  work: A`) and with CRLF endings. The docstring and the commit message both say anchored rows are refused, so this is the stated contract failing, not an edge beyond it. Fix at the root: place the id only when the row's first key node starts exactly at `(line_no, col)` of the item (`item.value[0][0].start_mark`); anything else (anchor or tag before the first key, on the same line or its own) is a finding. Add a test with an anchored row and no alias.

## Optional findings (nothing wrong)

**R2-O1. Mixed line endings crash instead of reporting.** A file with LF lines above CRLF lines is split on `\r\n` only, so the YAML line numbers overrun the list: `IndexError` in planning. No file is written (planning precedes all writes), and a variant that does not overrun is caught by the placement check, so no wrong id was produced in any probe. A finding rather than a traceback would match the rest of the function: split with `splitlines(keepends=True)`, or refuse a file whose endings are mixed.

**R2-O2. Duplicate `assignments` key pairs nodes from one list with rows from the other.** `next(...)` takes the first `assignments` node; the loader keeps the last. Probe: row ids from the second list were written into the first (dead) list, and a rerun assigns again. It needs a malformed file, so it is optional; refusing a duplicate top-level key would close it.

**R2-O3. The summary line overstates when nothing was written.** With findings and no `--check`, `main()` prints `assigned N row_id(s)` although no file changed. Exit code 1 and the findings list make the outcome clear, but "would have assigned" or "0 written" would be accurate.

## New-defect checks that came back clean

All-or-nothing (every finding case left both files byte-identical); index pairing (flow, scalar and nested items in the middle of a list); aliases (alias item refused, anchored `assignments` list itself handled correctly); merge keys; indented sequences; missing trailing newline; CRLF; unparseable, empty and multi-document files; real staging idempotent at 0.
