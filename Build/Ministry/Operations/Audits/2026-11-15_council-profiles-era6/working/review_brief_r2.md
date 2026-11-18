# Round 2 recheck brief: era 6 council profiles (targeted recheck, full effort)

You are a fresh Opus reviewer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era6). You have not seen the drafting or the round 1 fixing. You recheck ONE council. Do not edit any repo file; write only your recheck part to the scratchpad path you are given. No paid calls, no network.

## Scope: what changed in round 1, against round 1's findings
- Round 1 findings: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era6/R1_review.md` (Part A Constance, Part B Florence) and what was done about each: `R1_changes.md` (same parts). Some fixes were applied in corrected form; check the corrected form, not the proposal.
- The changes: `git diff d583e23e HEAD -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/` (your council's brief, audio, entry, and your key in records.json).
- For each round 1 finding: is it closed, and is the fix right? For each changed or added string: read it against its source line in context (who speaks, which council, which year). Every fix is new text; in recent batches most round 2 blocking points came from round 1's own fix wording.
- Every sentence the fixes split or joined: check each claim still sits with its witness.
- Re-verify EVERY changed or added quote verbatim against its file in cic/texts/ (allow for hyphen line breaks, OCR, long s as f). For a translated quote, check the translation is faithful and adds nothing.
- Do not re-review unchanged text from scratch. You may raise a new point in unchanged text only if it is blocking.

## The standard
- `CLAUDE.md` (whole file; above all "Trust and source fidelity" and "Accessible and rigorous", including "No AI tells").
- `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`.
- The original review brief, `working/review_brief_r1.md` in the same audit folder, for severity and mistakes to look for.
- Mark: "dont sacrafice quality, expecially the quality of writing." Every changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler, no editors' views told as settled. Sentences at most 25 words; brief at most 400 words.
- False absences: before you accept any new or changed absence ("no held source gives X"), search all of cic/texts with whitespace- and OCR-tolerant patterns and variant spellings (Latin, Greek, German, French, Czech, English). Report the searches. Use grep with line ranges; never read whole source files.

## Census
`/tmp/claude-0/-home-user-CIC-Project/32884fc0-bbef-57f8-b700-3dcb6b3c59ab/scratchpad/census.json` (origin/main's world-census.json). Only for changed tradition ids or census claims.

## Severity
Blocking / Substantial / Minor as in `review_brief_r1.md`. A point that only says the text could be stronger, with nothing wrong, is not a finding.

## Output
Write your part as Markdown in the shape of `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era5/R2_recheck.md` (read its first part for the format): header (files, word count and spoken time at 160 wpm, grade_text FK and Flesch from `python3 -c "import sys;sys.path.insert(0,'/home/user/CIC-Project');from engine.m7.turn_readability import grade_text;print(grade_text(open('PATH').read()))"`, longest sentence), verdict, a table of round 1 findings with status (closed / open / closed with a new point), then new Blocking / Substantial / Minor (ids like A2-B1 or B2-S1; exact text; evidence file:line with source words; a proposed fix worded ready to apply, keeping the brief within 400 words, every sentence within 25 words, each claim with its witness), Verified, Searches run, Counts. Reply with only the path and the counts.
