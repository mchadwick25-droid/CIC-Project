Simulated review — informational only, not an Article 31 substitute.

# Step 0-2 process and gate fixes (commit 89a9ef62c): independent review

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Step 0-2 process-fix drafting worker (commit 89a9ef62c; commit trailer reads "Claude Sonnet 5.5")
- **Round:** 1
- **Truncation check, method 1:** line-count reconciliation. `git show --numstat 89a9ef62c` sums to 375 insertions and 66 deletions over 15 files, equal to the `--stat` summary line; every hunk of the diff was read to its last line, and the process document still ends on its closing `quote.license` rule line.
- **Truncation check, method 2:** blob hash comparison. `git hash-object <path>` equals `git rev-parse 89a9ef62c:<path>` for 13 of the 15 files. The two that differ, `engine/m10/quotes.py` and `engine/m10/tests/test_quotes.py`, were changed by the later commit e6018b906 (one line in `_norm`, one test); that commit is outside this review's scope.
- **Date:** 2026-09-30
- **Documents:** commit 89a9ef62c on branch `claude/busy-pasteur-4sx229`: `engine/m10/{quotes,rounds,reviewfile,handoff,rebaseline}.py` and their tests, `tools/check_live_commentary.py` and its test, `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`, `Build/reference/L4-Templates/Review_File_Header_Template.md`, `Build/Ministry/Operations/Standing/Launch-Prompts/CiC_World_Build_Launch_Prompt_V2.0.md`, `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Needs fixes before it is relied on.** 0 P0, 4 P1, 9 P2.

Keep the soft-hyphen join, the `.docx` reader, the Library-stage checklist and the handoff items 1 and 12 wording (P2 polish only). Two gate changes weaken a gate beyond what the order needs and should be reworked, not patched: the `Cycle reset` mechanism (P1-1, P1-2) and the Source Registry iso-date exemption (P1-3). One process rule is a fleet-wide methodology change the decision log says was not made (P1-4).

**Project lead confirmation: yes.** The order ("apply fixes to the step 0 - 2 build process") authorises fixes. It does not decide who may restart the three-round cap, or a new Confidence calibration rule for every world. Under CLAUDE.md both are governance or methodology changes, which are "Always ask". The 2026-09-29 ruling says the cap counts from significant new material. It does not say that any builder may declare that material significant by adding a header line, and it notes that it "changes no rule text in the skill".

## Tests and sweeps run

- `python -m pytest engine/m10/tests tools/tests -q`: 474 passed.
- Staleness sweep: every world `False` (alx, cappadocian, desert, don, fix, gallic, hal, ijc, pahc, rzg, syr, witt).
- `python -m engine.m10.cli handoff lpc --skip-quotes`, run at 89a9ef62c^ (a worktree) and at HEAD. Every step and declaration outcome is identical: handoff-02/03/04 accepted findings unchanged, `handoff-declaration: PASS (3 accepted)` in both. The one difference is `handoff-11-narration`, 94 findings before and 26 after. 68 Source Registry row lines are no longer flagged (P1-3).
- `python -m engine.m10.cli roundcount syr 1 --check-new --round 4`: FAIL before, PASS after (P1-1).
- `tools/check_live_commentary.py --base 89a9ef62c^`: the two edited `Build/reference` files carry no REWRITE or ROUTE lines.

## P1 findings

**P1-1. With no `Cycle reset` field, `check_new` behaves differently.** `engine/m10/rounds.py:40` falls back to `min(found)` as the cycle start. Line 60 then tests `new_round - start + 1 > ROUND_CAP` in place of the old `new_round > ROUND_CAP`. For any document whose lowest recorded round is above 1, a fourth-numbered round now passes the guard. Live case: `syr` Doc_01 has rounds 2 and 3 only, and `roundcount syr 1 --check-new --round 4` went from FAIL to PASS. The fallback should be round 1, so that a document with no reset field keeps exactly the old result. `handoff` and `rebaseline.current_state` are unaffected with no field present, because `cycle_rounds` returns every round.

**P1-2. Any non-blank text restarts the cap, and nothing checks the ruling's precondition.** `engine/m10/rounds.py:39` honours a reset on any non-blank value. That includes placeholders such as `TBD` or `<ruling>`, which `reviewfile.py:115` rejects. But `handoff` never runs `check_review_file`, so the placeholder still restarts the count there. The requirement to "cite the ruling" is enforced only as non-empty text. Nothing checks that the cited decision-log entry exists. Nothing checks that the round before the reset cleared review, which is the ruling's own precondition ("a document that has cleared independent review is later changed"). Nothing detects a field added afterwards to an existing review file: commit ee622a57f did exactly this to the hus Round 4 files. As written, a builder at the cap can clear it by adding one line, without escalating. Rework it so a reset counts only when all of the following hold, and otherwise gives a finding that routes to the project lead:
- the value passes `PLACEHOLDER`;
- it names a `LIBRARY-DECISION-LOG.md` entry heading that resolves;
- the round before the reset file has clearance under `has_clearance`.

The project lead should also decide who judges material "significant" (the Opus reviewer, the Library thread, or he himself).

**P1-3. The Source Registry exemption now covers whole rows and hides narration.** `tools/check_live_commentary.py:371-377` returns True for any row with two or more `|` characters in a `*Source_Registry*.md` file. That drops the iso-date cue for every cell in the row, prose cells included. The old cell-shape test was replaced, not narrowed. The lines it newly hides include real narration. lpc `Source_Registry.md:275` reads "would have let a reviewer catch that error at its own root rather than well into Doc_01's own review history". Line 308's Added cell reads "`lpc` Library-thread drafting pass". The new test at `tools/tests/test_check_live_commentary.py:1659` encodes a narrative cell ("2026-09-29 by the Library thread after the vendoring pass") as KEEP. The stated ground at lines 372-374 is also wrong:
- the Source Registry Template (`Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md`) has no Discovery column;
- its Added field is "Date and who/what added it", with no ISO requirement;
- Framework V7.4 Step 2 sets no date column.

The right fix exempts dates only in the columns named in the table's header row (Added, and the discovery channel/date column), in their "date, who" and "channel / path / date" shapes, and keeps every other cell scanned.

**P1-4. A fleet-wide Confidence calibration rule is set in the process document instead of the Template.** `CiC_Record_Native_World_Build_Process_V2.0.md:415-417` says "Each row carries one Confidence letter, A to D. A is given only when the Licensed-For content was read and verified at the source by structure marker." The Template defines A as "Verified this session against an accessible primary source, translation, or authoritative reference", a broader rule. The 2026-09-29 entry "lpc Registry rulings" says: "The Registry's Confidence calibration rule text is not amended; a change to it would be a methodology change that comes from the Template and applies to every world." The new sentence is that change, made in a second place, which forks the Template. Either the project lead approves it and it goes into the Template (with the process document pointing there), or the sentence comes out. The corpus-figures two-method/locale rule on the same lines is new fleet method too, and should be confirmed in the same question.

## P2 findings

1. `engine/m10/quotes.py:39`: `¬\s*` also joins across blank lines and running heads. Institutum v3 gives "Probatio¬ ⏎⏎Regulae" → "ProbatioRegulae". It also strips `¬` inside mojibake in `pl11-…_migne.txt`. Neither creates a false pass: a join can only create a string that is absent from the source. But `¬[ \t]*\r?\n[ \t]*` (one line break) is the exact rule.
2. `engine/m10/quotes.py:118, 216`: the join is applied to the source text but not to the quotation. A quotation that copies the scan's `¬` literally ("tan¬ tum") now fails, which is at odds with the new rule that a scanned quotation "keeps the scan's letters" (process doc line 407). No Step 0-2 document carries `¬` today. Join the quotation too.
3. `engine/m10/quotes.py:247-249`: the `.docx` pool skips the `_REVIEWISH` name filter that the `.md` pool applies. It also includes superseded and draft documents: Framework V7.3 beside V7.4, `CiC_L3D_Facilitator_Governance_V3.7_PROPOSAL.docx`, `CiC_Live_Safety_Testing_Script_2026-07-21.docx` (scripted participant lines), the Corrections Tracker and the Change Orders Register. The match does not depend on attribution, so a quotation credited to a historical author passes if it appears in any of these files. The only trace is a note. The increment is small beside the existing `.md` pool, which already includes the whole `_cross-world` folder and its decision log that quotes world drafts. Limit the `.docx` intake to current, non-proposal versions (or to the named Constitution and Framework). An attribution-aware exemption is separate work.
4. `tools/check_live_commentary.py:368`: the filename pattern widened from `(^|_)source_registry\.md$` to `source_registry[^/]*\.md$`, so it now also matches names such as `Source_Registry_Review_Notes.md`. Match `(^|_)source_registry(_v\d+)?\.md$`.
5. `engine/m10/reviewfile.py:116`: the message says "present but empty" for a placeholder value as well. Say "empty or a placeholder".
6. Process V2.0 Round counter row (line 303): "fails only once a fourth file already exists" should read "a fourth file in the current cycle", to match the sentence added after it.
7. Process V2.0 Section 12 (lines 1522-1527): the change order gives a source but no reason, and does not say whether it binds worlds already stamped V2.0 (jes, hus). Section 12 requires "a named change order with a reason".
8. `LIBRARY-DECISION-LOG.md:16`: the heading repeats the date ("— Step 0-2 process and gate fixes, 2026-09-30").
9. `Review_File_Header_Template.md:13`: the rules comment sits below `# Review of <document>`, so it is copied into every new review file. Put it above the label line or leave it to the process document.

## Checks with no finding

- Launch Prompt V2.0, handoff items 1 and 12, and the checklist agree with each other and with the gate ids in `engine/m10/handoff.py`. "Approved to proceed" is used throughout, and "finalized" nowhere.
- Nothing touches Frozen status, the four escalation categories, or the Facilitator-only redirect rule.
- The Forces-lens requirement matches Framework V7.4 Step 2 ("Apply forces lens: which sources speak to external forces?"). The five-level `formation_confidence` wording, with absence not treated as a sixth level, matches CLAUDE.md.
- `rebaseline.current_state` counts cycle rounds only in `rounds`, and `files` still counts every file. A reset added under a declared cap row makes that row fail loudly ("nothing to accept"), which fails safe. lpc's outcomes are unchanged.
- `docx_text` reads only `word/document.xml` and skips unreadable files. Text boxes may repeat and `w:br` joins words, but neither can make a false match pass.
