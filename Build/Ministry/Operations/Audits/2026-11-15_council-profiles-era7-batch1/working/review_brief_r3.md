# Round 3 recheck brief (the last round): era 7 council profiles, batch 1 (targeted recheck, full effort)

You are a fresh Opus reviewer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch1). You have not seen the drafting or any fixing. You recheck ONE council. Do not edit any repo file; write only your recheck part to the scratchpad path you are given. No paid calls, no network.

## Scope: what changed in round 2, against round 2's findings
- Round 2 findings: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/R2_recheck.md` (Part A Worms, Part B Augsburg, Part C Chanforan) and what was done about each: `R2_changes.md` (same parts; its preface lists the worker's own brief fixes). Some fixes were applied in corrected form; check the corrected form, not the proposal.
- The changes: `git diff 7e0ce987c HEAD -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/` (your council's brief, audio, entry, your key in records.json, and your council's README line). 
- For each round 2 finding: is it closed, and is the fix right? For each changed or added string: read it against its source line in context (who speaks, which council, which year). Every fix is new text; in recent batches most round 2 blocking points came from round 1's own fix wording.
- Every sentence the fixes split or joined: check each claim still sits with its witness.
- Re-verify EVERY changed or added quote verbatim against its file in cic/texts/ (allow for hyphen line breaks, OCR, long s as f). For a translated quote, check the translation is faithful and adds nothing.
- Do not re-review unchanged text from scratch. You may raise a new point in unchanged text only if it is blocking.

## The standard
- `CLAUDE.md` (whole file; above all "Trust and source fidelity" and "Accessible and rigorous", including "No AI tells").
- `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`.
- The original review brief, `working/review_brief_r1.md` in the same audit folder, for severity and mistakes to look for.
- Mark: "dont sacrafice quality, expecially the quality of writing." Every changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler, no editors' views told as settled. Sentences at most 25 words; brief at most 400 words. Length (Mark: the ceiling is never a target): if the fixes left a sentence that does not earn its place, say so.
- False absences: before you accept any new or changed absence ("no held source gives X"), search all of cic/texts with whitespace- and OCR-tolerant patterns and variant spellings (Latin, Greek, German, French, Czech, English). Report the searches. Use grep with line ranges; never read whole source files.

## Census
`git show origin/main:cic-website/data/world-census.json` (query with python). Only for changed tradition ids or census claims.

## Severity
Blocking / Substantial / Minor as in `review_brief_r1.md`. A point that only says the text could be stronger, with nothing wrong, is not a finding.

## Output
Write your part as Markdown in the shape of `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era6/R2_recheck.md` (read its first part for the format): header (files, word count and spoken time at 160 wpm, grade_text FK and Flesch from `python3 -c "import sys;sys.path.insert(0,'/home/user/CIC-Project');from engine.m7.turn_readability import grade_text;print(grade_text(open('PATH').read()))"`, longest sentence), verdict, a table of round 2 findings with status (closed / open / closed with a new point), then new Blocking / Substantial / Minor (ids like A3-B1 or B3-S1; exact text; evidence file:line with source words; a proposed fix worded ready to apply, keeping the brief within 400 words, every sentence within 25 words, each claim with its witness), Verified, Searches run, Counts. Reply with only the path and the counts.


This is round 3, the last under the review cap. Raise a Blocking point only for something wrong or misleading; anything else is Minor or not a finding.
