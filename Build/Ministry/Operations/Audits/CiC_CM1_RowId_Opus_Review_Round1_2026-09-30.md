Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus independent adversarial reviewer (subagent, session_01Uo1V6v9bcjuAJYtw5vKRr8)
Drafter agent: Sonnet CM-1 implementation thread
Round: 1
Truncation check, method 1: per-file line arithmetic. `git show origin/main:<file> | wc -l` plus added minus removed lines counted from the full `git diff origin/main` output equals `wc -l` of the file on disk for all three files (merge 310+109-1=418, corpus_map 291+15-0=306, tests 118+111-0=229); `git diff --numstat` agrees (109/1, 15/0, 111/0).
Truncation check, method 2: end-anchor read. The final hunk of each diff was matched against the file's actual tail on disk (tests file ends `sys.exit(0 if all(results) else 1)`; merge diff's last hunk is the `--assign-ids` branch in `main()`, read in full from the file), and every function the diff touches (`validate`, `load_staging`, `work_slug`, `assign_ids`, `merge`, `main`) was read end to end from the working tree, not from the diff alone.

# Review of CM-1 row_id (branch `cm1-row-ids`, commit 64accec3)

Scope: `git diff origin/main` of `cic/engine/corpus_map_merge.py`, `cic/engine/corpus_map.py`, `cic/engine/tests_corpus_map.py` only. The staging-data and decision-log changes on the branch were not reviewed.

Method: diff read in full; the functions it touches read in full; `python cic/engine/tests_corpus_map.py` run (all new checks pass; the four failures are the four already failing on main); `python cic/engine/corpus_map_merge.py --assign-ids --check` run on real staging (0 to assign, 837 rows, 837 unique ids); a probe script ran `assign_ids()` against 17 synthetic staging files in a temporary `STAGING` (flow mappings, scalar items, CRLF, missing trailing newline, indented sequences, anchors and aliases, merge keys, `row_id:` null, integer ids, hand ids occupying a future slug); `validate()` probed with synthetic buckets; `tools/check_live_commentary.py --surface cic-engine --base origin/main` run (0 hits).

## Bottom line

The design is sound and the real staging data is correctly ided: every row has a unique id, the run is idempotent on it, and existing ids are never moved by collision handling (probed: a hand id sitting on a future slug pushes the new row to `-2`, the existing id stays). But `assign_ids()` has three real text-edit defects on inputs it explicitly tries to handle, and one of them silently writes a permanent wrong id. None bites the current 837 rows. All three should be fixed before the tool is relied on for new staging files. Verdict: revise.

## Substantial findings (actually wrong)

**S1. A flow-mapping row shifts every later row onto the wrong id, and the file is still written.** `assign_ids()` builds `entries` from the composed nodes but *skips* flow-style and non-mapping items, while `rows` from `yaml.safe_load` keeps every item. The two lists are then paired with `zip(entries, rows)`, so after one skipped item every later line is paired with the previous row's data. Probe input: rows `A` (block), `{work: B, ...}` (flow), `C` (block). Result: the `C` line was written as `row_id: vol1--b`. The run reports a finding and exits 1, but the file has already been rewritten. Because an existing id is never overwritten, the wrong id is permanent, and `validate()` cannot catch it (it only checks that one id always names the same work, which it now does). Fix at the root: pair each sequence node with its own row by index (keep the skipped index in step, or build both from the same node list), and do not write a file that produced a placement finding. Add a test with a flow row between two block rows.

**S2. A non-mapping item in `assignments` crashes the run after earlier files are already rewritten.** A scalar item (`- just a string`) is skipped in `entries` but reaches `row.get("row_id")` in the second loop: `AttributeError: 'str' object has no attribute 'get'`. Files are written one at a time inside that loop, so any staging file sorted before the bad one has already been modified when the traceback fires. The same pass also crashes with `TypeError` when a staging file's top level is a list rather than a mapping (`node.value` items are not key/value pairs). The code clearly intends these to be findings (it tests `isinstance(item, yaml.MappingNode)` and `isinstance(seq, yaml.SequenceNode)`); they should be, and no file should be written until every file has been planned without error.

**S3. Two inputs make the text edit produce a broken or non-idempotent file.**
- *Anchor on its own line.* `- &r` followed by `  work: A` becomes `- row_id: vol1--a-2` / `  &r` / `  work: A`, which PyYAML cannot parse (`could not find expected ':'`). The alias item `- *r` resolves to the same node, so the same line is planned twice (reported as 3 assigned, 1 collision, for 2 real lines); the second plan overwrites the first. Every later run on that file then dies with `ScannerError`.
- *`row_id:` present but null.* `assign_ids()` treats null as absent (as `load_staging` does) and inserts a new `row_id:` line above it. The file now has a duplicate key, and PyYAML keeps the *last* one, so the row still loads with `row_id: None`. Each further run adds another line: the run is not idempotent here, which the spec requires.
Fix: refuse (as a finding) any row whose mapping node carries an anchor or is referenced by an alias, and any row that already has a `row_id` key of any value; or replace a null value in place rather than inserting a second key. Add tests for both.

## Optional findings (could be stronger; nothing wrong)

**O1. The word-boundary test cannot fail on the property it names.** `work_slug("word " * 40)` gives a slug whose 60th character is a hyphen, so a naive `slug[:60].strip("-")` passes it too. The implementation is correct (probed: `"x"*59 + " yy"` cuts to 59 `x`), but the test should use a title whose cut falls mid-word, and assert the exact result.

**O2. `validate()`'s "repeats within this entry" branch only fires when the first sighting was in the same bucket.** If `k` first appears in bucket A, then twice in bucket B, the row_id check says nothing about B. It is not a real hole today: the same id always means the same exact `work` and `source_file`, so the existing "listed twice in this entry" check reports it. Either track sightings per bucket, or drop the branch and let the existing check carry it.

**O3. Non-Latin titles all slug to `work`.** NFKD-to-ASCII drops Greek, Syriac, Coptic and Armenian letters entirely, and ligatures such as Æ (`Æthelred` becomes `thelred`; the test locks this in). Every such title in one volume becomes `<stem>--work`, `-2`, `-3`, and the id no longer says what the row is. The real staging has none today. If non-English-titled volumes are expected, transliterate (or fall back to a title-derived hash) before they arrive.

**O4. CRLF files are silently converted to LF.** `read_text`/`write_text` translate line endings, so the "text edit" rewrites every line of a CRLF file. No staging file is CRLF today. Preserve the original newline (`newline=""` on both sides) if that should matter.

**O5. Docstring wording.** "Two rows of one volume with the same slug take `-2`, `-3` in staging order" is true only when no hand id already holds the base; the rule is really "the first free suffix". Minor, but the docstring is the spec.

**O6. A row that cannot be placed still reserves its id and counts a collision.** The run reports the finding and exits 1, so nothing is lost; the counts in the summary line are just slightly off.

## Commentary check

No change history or process narration was added to the three live files. `check_live_commentary.py` reports 0 hits on `cic-engine`. The new `ROW IDS` docstring section and the `validate()` comment describe behaviour, not history. The test section header `# --- row_id (CM-1) ---` carries a tracking label; this is consistent with the file's existing style and is not a finding.

## Tests

`python cic/engine/tests_corpus_map.py`: all 15 new checks pass. The four failing checks ("every map filename is a census movement id", "every bucket on disk is reproducible from staging", "every author ruling is used", "every transmitted work has its voice") are the four already failing on main. None of the new tests covers the paths in S1 to S3, which is how they got through.
