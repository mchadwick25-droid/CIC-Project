Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: round-3 recheck subagent, Opus 5.5 at medium effort, fresh context, independent of every drafting and revising agent, session_01L5xhWKCzK96CZGy1fPzqGp
Drafter agent: Process V2.0 drafting and revision agents (the main thread and its Sonnet 5.5 subagents), session_01L5xhWKCzK96CZGy1fPzqGp
Round: 3
Truncation check, method 1: direct read of the final lines of every file rechecked. V2.0 ends in Appendix B on "`quote.license` is `verbatim`, `paraphrase-only` or `do-not-voice`." V1.4 ends "Doc_05 and Doc_07 carry this spine." The launch prompt ends "Mark decides Frozen status." The Naming Discipline ends "...not a default that took effect on its own." The build-cycle skill ends "...say so plainly to Mark instead of forcing the cycle." The validation skill ends "Flag it on structural grounds." The Construction Framework's edited paragraph was read whole from the extracted `word/document.xml` text and ends "(b)/(c) are closed or explicitly accepted before freeze." Every file ends on a finished sentence or list item.
Truncation check, method 2: bash at commit 1dec3f57. `wc -l` gives V2.0 1495, V1.4 248, launch prompt 247, ARSP 27, Naming 91, build-cycle skill 153, validation skill 93, handoff manifest template 59. `tail -c1` is a newline on all eight. `grep -c '^## '` gives 16 in V2.0, as in round 2. md5 prefixes: V2.0 34445fcfa76b, V1.4 b6cf3dc5aa48, launch prompt 8fda19458762. The Framework docx before (commit 07245847) and after both extract to 722 paragraphs, and `diff -rq` on the two unzipped packages differs only in `word/document.xml`.

# Review of Build Process V2.0, Completion Standard V1.4, the launch prompt, skills, templates, the Construction Framework and the gate layer: round 3 targeted recheck

Verdict: SUBSTANTIAL FINDINGS REMAIN. This is round 3 of 3. Under the cap there is no round 4, so each remaining finding below goes to Mark, stated as a decision or as a defect with its minimal fix. The round-3 fixes are good work. Findings B, C, D, F and K are closed, and so is the real commentary in the ARSP. None of the remaining findings is a fabrication or a safety fail-open.

Scope: the diff 07245847..1dec3f57, measured against `Round2_Recheck.md` and the converged spec of 2026-09-29. The recheck covers only what round 2 left open and any regressions from the round-3 fixes. Read-only runs were made against `cappadocian`, `hal`, `rzg`, `gallic`, `pahc` and `fix`. No repository file other than this one was edited.

## 1. The six items round 2 left PARTIAL or OPEN

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | V2.0 round-1 finding 1 (lean single-trial against the Framework's two-trial rule; round 2 finding G) | PARTIAL | The Framework's Representative-freeze paragraph is the only text that changed in the docx. The before and after `word/document.xml` text differ at one paragraph (582 of 722). It now matches V1.4 §C: lean freeze by default, single-trial blind probes, continuity regression, and two trials plus the Table Readiness Round when a trigger fires. The Framework's own Validation Protocol Rigor subsection did not change. It still "governs every testing category below" and requires "at least two independent generation trials" before a round may be reported "confirmed," "clean" or "closed." It also bars a single-sample check from "satisfying a Freeze Criterion" (extracted text, paragraphs 529-533). The contradiction has moved inside the Framework. See R3-2. |
| 2 | V2.0 round-1 finding 3 (trigger definitions; round 2 finding A) | CLOSED | V2.0:1073-1092 and V1.4:188-200 state the four definitions as the rule. They match `engine/m10/validation.py:279-282` word for word in substance. V2.0:415-418 (handoff check 1), the manifest template (:7 and check 1), launch prompt step 5 and build-cycle skill:74 all say Mark sets `safety_adjacent` at handoff. `handoff.py:180-182` enforces it for non-grandfathered worlds. The §13 placeholder item is gone. Round 2's minimal fix also asked for a decision-log addendum, and it was not written. See R3-5. |
| 3 | V2.0 round-1 finding 8 (B-8 two-trial dropped; round 2 finding H) | OPEN | V2.0:836 still reads "Two trials when the world is on full validation. One trial on the lean path." No decision records this: the V2.0 entry in `CiC_System_Hub_Decision_Log.md` did not change this round. See R3-3. |
| 4 | Preservation R37, Record Integrity (round 2 finding E) | PARTIAL | The documents are fixed. V2.0:297 and 1166-1178, V1.4:111-117, the launch prompt and build-cycle skill:74 all say the fourth part is "`deployed` passes at the pinned package". They also give "each fix a document calls applied is found in the deployed artifact" to the reviewer. The code still says the opposite. The `integrity.py:8-10` docstring reads "a fix described as applied is found there or is a finding". The `integrity --help` text (`integrity.py:117`) reads "the deployed artifact holds what was applied". See R3-4. |
| 5 | Contradiction 14 (ARSP routes the largest passes to Fable) | CLOSED | ARSP:5 no longer names a model tier. ARSP:27 routes drafting "as Build Process V2.0, Section 2, routes them", and that matches V2.0:219 and 244. |
| 6 | Gate-layer round-1 finding 8 (blocking `live-commentary` fails this pull request; round 2 finding I) | OPEN | `python tools/check_live_commentary.py --enforce --base 7521c09a` exits 1 with 34 REWRITE or ROUTE lines. Round 2 counted 291. The new narrow rule is in place and tested. Section 3 classifies the 34 lines. See R3-1. |

**Counts:** 2 CLOSED, 2 PARTIAL, 2 OPEN.

### Round 2's other findings, rechecked

| Finding | Status | Evidence |
|---|---|---|
| B, `prereview` and `roundcount` usage | CLOSED | The docs now give `prereview <code> --doc N` and `roundcount <code> N --check-new` (V2.0:284, 286, 809; launch prompt:88-93; all five build skills). `roundcount <w> N --check-new` exits 1 on hal 8, hal 1, rzg 2, gallic 1 and pahc 6, all of which have three rounds. It exits 0 without the flag, as documented. `prereview cappadocian --doc 10` runs, and `--doc Doc_04` exits 2, as documented. |
| C, `records --freeze` | CLOSED | V2.0:292, V1.4:139-141, launch prompt:101-102 and the validation skill:22. `records fix` gives exit 0 with a note. `records fix --freeze` fails on `facilitator_brief` and the site JSON. |
| D, `source_anchor` | CLOSED | V2.0:833 now says "`gate_readability` grades `source_anchor` like the other four fields". That matches `spoken_fields.py:91`. |
| F, R27 and R41 rows | CLOSED | V2.0:873 uses the paragraph as the citation unit. V2.0:876 puts the modern sense on the hover card. Both agree with the validation skill (:42-43). |
| J, ARSP half | CLOSED | The review-history narration is gone (ARSP:3, 13, 17, and "What it catches" at :21-23). The ARSP lines that still show as blocking are false positives (Section 3). |
| J, Voice Style Guide half | Decision (R3-6) | The file was restored to its base text. The pull request no longer edits it, so the edit-scope rule no longer applies. The restore leaves a broken path. |
| K, Naming Discipline labels | CLOSED | No G2 or G3 is left (`grep`). The document now says M1 at :3, :18, :25 and :81, and names the Register Bar at :43-44. |

## 2. Doc-vs-code: the CLI

`python -m engine.m10.cli --help` lists the 14 subcommands of V2.0's gate table. Each changed subcommand's `--help` matches the documents, with one exception:

- `prereview [--doc DOC] world_code`: matches. See the minor item on a missing document file.
- `roundcount [--check-new] [--round ROUND] world_code doc`: matches. `doc` is an integer.
- `records [--freeze] world_code`: matches.
- `reviewfile paths...`: matches. It passes `Round2_Recheck.md` and this file.
- `gaps world_code`: read-only. On cappadocian it fails with 41 unmatched open items, the known legacy debt.
- `integrity`: **does not match.** The help text still reads "the deployed artifact holds what was applied" (R3-4).

## 3. The 34 remaining blocking lines

| Lines | Kind | Class |
|---|---|---|
| V2.0:830 (the "(R33)" in B-4), 839 (R11), 860 (R26), 872-876 (R26, R27 and R42, R31-C, R37, R41 as table row names), 883 (R16), 1325 (R16); lexicon skill:26 (R41); validation skill:41 (R26, R37), 42 (R27-A, R36, R38), 43 (R41) | ruling number | Vocabulary. Each number names a live runtime ruling. The existing tests require a bare ruling number in a method document to stay flagged, so clearing them is Mark's call. |
| V2.0:166 (`Decision-Log.md`), 867 (`Rulings-Pending.md`) | backticked path pointer | Vocabulary. Each points to where the rulings live. |
| V2.0:1163, V1.4:112 ("still open in `Open_Gaps_Tracking.md`") | status-cue false positive | Vocabulary. Each states a rule about open items and is not a status report. |
| V2.0:1284 ("no longer passes, stop and file the regression") | history-word false positive | Vocabulary. |
| build-cycle skill:48 ("Mark's own recorded decision") | marks-word | Vocabulary. It names a role. |
| ARSP:1, 3, 9, 13, 17, 27 | reviewer, change-history cue | Vocabulary. The ARSP is outside the narrow rule's path scope. |
| Backlog:24, 40 ("Entry 1") | entry number | Vocabulary. |
| Naming:1 (title "(2026-09-08)") | date | Vocabulary. The title repeats the file name. |
| SOURCE-READINESS:95, 96, 105 | route cue ("unresolved mapping decision", "open question") | Vocabulary. |
| **Backlog:54** ("needs assessment, not yet resolved") | status | **Real.** Open status on a live file. Rewrite: "### Entry 2 — Athanasius of Alexandria". Log the open assessment in Ministry. |
| **Validation skill:42** ("because of a known exemption-asymmetry bug") | status | **Real, but minor.** The rule is load-bearing. Rewrite: "`inherited_ungrounded` stays report-only." Register the defect as an `ACCEPTED_OPEN` waiver or tracking entry if it is not one already. |
| **V2.0:1037** ("the System Hub Decision Log's entry for the 2026-09-26 fleet ...") | dated pointer | **Borderline.** It is a subject-and-date citation to where the rule was decided. Keep the rule and drop the pointer, or keep it as a citation if Mark allows that. |

Of the 34 lines, 2 are real, 1 is borderline and 31 are vocabulary.

**The Register Bar** (`Build/reference/method/CiC_Register_Bar_2026-08-29.md`). This pull request does not edit it, so it does not block. It carries real commentary. The minimal rewrites:

| Line | Now | Rewrite |
|---|---|---|
| 1 | "# The Register Bar (2026-08-29, Mark's ruling)" | "# The Register Bar" |
| 3 | "Mark's words, the evening the bar was fixed:" | "The standard, in Mark's words:" |
| 34-38 | "Added 2026-09-04 (Cross-System Analysis finding, not Mark's own words like the rest of this document - see CiC_Cross_System_Analysis_Tracking.md ...): the sample already had this property from the start: naming it here closes the one gap ..." | Delete from "Added" to the end of that clause, and keep the property sentence before it. The provenance goes to Ministry. |
| 52 | "(engine/m1/gates.py, added 2026-09-04)" | "(engine/m1/gates.py)" |
| 69 | "(Mark, 2026-08-30: "i don't want a series of rules ...")" | Keep the quotation as the stated standard and drop the date: "(Mark: "...")". |

## 4. Remaining substantial findings, for Mark

**R3-1. The blocking `live-commentary` job still fails this pull request (defect, needs a decision).**
Of the 34 lines, 2 are real, so rewrite those under Section 3: Backlog:54 and the validation skill:42. The other 32 need one of three rulings from Mark:
- (a) Drop the bare ruling numbers from the method documents and keep the rules. This is a drafting edit that clears 17 lines.
- (b) Relabel the two tests that require ruling numbers to stay flagged. This is a change to what the classifier enforces.
- (c) Widen the narrow rule's path scope to the ARSP and the Naming Discipline.

The route cues in SOURCE-READINESS, the backticked path pointers and the history-word false positive still need either a rewrite or a rule. Recommendation: (a), plus rewording the 11 other lines. That clears the gate with no classifier change.

**R3-2. The Construction Framework now contradicts itself on the lean freeze (decision).**
The freeze paragraph makes single-trial validation the default. The unchanged Validation Protocol Rigor says it governs every testing category below it. It also says a round cannot count toward a Freeze Criterion without two trials.

This ties to the open item already on Mark's list: may a lean result be called "confirmed" or "clean"?

Minimal fix, a change order to a governing document: add one sentence to the Protocol's scope. "For a Representative-freeze, the lean default in the freeze criteria below applies; this protocol binds full validation and any report of 'confirmed', 'clean' or 'closed'."

The edit to the Framework paragraph is itself a change to a governing document. No change-order record was found for it (R3-5). Mark should confirm it.

**R3-3. B-8 probe parity on the lean path (decision, carried unchanged from round 2 H).**
Mark chooses one of two:
- record that B-8 runs single-trial on lean, in the V2.0 decision-log entry;
- or restore "two trials" at V2.0:836.

**R3-4. `integrity` overclaims in its own help text and docstring (defect).**
Minimal fix:
- `engine/m10/integrity.py:117` help: "... stated counts match, `deployed` passes at the pinned package".
- `integrity.py:8-10`: replace the last clause with "`deployed` passes at the pinned package (confirmed items, rule counts, source anchor); whether each fix a document calls applied is in the artifact is a reviewer check".

This is a text-only change to a gate module.

**R3-5. Governance changes made this cycle have no decision-log record (defect).**
`CiC_System_Hub_Decision_Log.md`, in the V2.0 entry's "Open" list, still says the trigger definitions are "Proposed to the project lead, not yet answered". It also says "The World Profile generated view is not built".

No entry records any of these:
- Mark's acceptance of the trigger definitions, T22 and T5;
- the Framework paragraph change order;
- adoption of the narrow commentary rule, which changes what a blocking CI job enforces and which round 2 routed to Mark;
- the B-8 disposition.

CLAUDE.md requires a change to a settled document to be a named change order, never a quiet edit.

Minimal fix: append one addendum to that entry, recording each item with Mark's disposition. Where Mark has not given one, list the item as open.

**R3-6. Restoring the Voice Style Guide left a broken path, now accepted in the baseline (decision).**
This branch moved V1.9 to `Archive/Superseded-Method/`. The Voice Style Guide, restored to its base text, cites `Build/reference/method/CiC_Record_Native_World_Build_Process_V1.9.md` at :1233, and that path no longer exists. `tools/check_paths_baseline.txt` gained that entry this round, so `check_paths` passes while the reference is broken.

That is a live reference file with a known dead link. It is not one of the 13 historical documents the decision log accepts. Mark decides between two options:
- route the Voice Style Guide to Ministry (a structural move, with a README entry and a tracking entry);
- or clean it in place, which fixes the path and removes its 58 real commentary lines.

## 5. Minor (not blocking)

- V2.0:284 says `--doc N` "only checks that its file exists". A missing file gives only a note, and the step passes (`prereview.py:89-90`; `--doc 99` on cappadocian gives PASS). Say "notes whether its file exists".
- `gates.py:705` and `builders.py:459` still say "The four voice_craft fields". The count is now five with `source_anchor`.
- `roundcount` counts distinct round numbers, not files (`rounds.py:34`). A spot-check and a recheck with the same round number count once. The documents say "counts every review file".
- The two replacement hand labels (`engine/api/anon_cap.py:5` and `:37`) are real commentary, correctly labelled. They pin the precision sample to lines that should themselves be cleaned one day.

## 6. Test status

- `python -m pytest tools/tests -q -p no:cacheprovider`: 192 passed. This includes the four new tests for the method-file rule and the precision and recall sample.
- `python tools/check_paths.py --baseline tools/check_paths_baseline.txt`: exit 0, with 0 new unresolved paths and 965 accepted. One of those 965 is the new Voice Style Guide entry (R3-6).
- `python tools/check_live_commentary.py --enforce --base 7521c09a`: exit 1, with 34 blocking lines (Section 3).
- `python -m engine.m10.cli` and every changed subcommand's `--help`: they match V2.0's gate table, except the `integrity` help (R3-4). Spot runs: `roundcount` (5 worlds, with and without `--check-new`), `prereview --doc`, `records` and `records --freeze` (cappadocian and fix), `reviewfile`, and `gaps` (cappadocian, read-only). Every run behaved as the documents now describe.
- The working tree was clean after every run.
