# Round 2 recheck brief: era 7 council profiles, batch 2 (targeted recheck plus length test, full effort)

You are a fresh Opus reviewer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch2). You have not seen the drafting or the round 1 fixing. You recheck ONE council. Read and grep only: do not edit any repo file, do not run git commands that change anything, and write only your recheck part to the scratchpad path you are given. No paid calls, no network.

## Scope 1: what changed in round 1, against round 1's findings
- Round 1 findings: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch2/R1_review.md` (Part A Regensburg, Part B Trent, Part C Augsburg 1555, Part D Poissy; grep for your part's heading and read only it) and what was done about each: `R1_changes.md` (same parts). Some fixes were applied in corrected form; check the corrected form, not the proposal.
- The changes: `git diff f6c9d034 HEAD -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/` restricted to your council (its brief, audio, entry, its key in records.json, its README line under "Batch 2"). Records are edited in `working/records_<id>.json` and merged into records.json.
- For each round 1 finding: is it closed, and is the fix right? For each changed or added string: read it against its source line in context (who speaks, which council, which year, which side). Every fix is new text; in batch 1 the blocking point after round 3 came from a round 2 fix that overstated its witness.
- Every sentence the fixes split or joined: check each claim still sits with its witness.
- Re-verify EVERY changed or added quote verbatim against its file in cic/texts/ (allow for hyphen line breaks, OCR, long s as f). For a translated quote, check the translation is faithful and adds nothing.
- Do not re-review unchanged text from scratch. You may raise a new point in unchanged text only if it is blocking.

## Scope 2: the length test (Mark: "Keep 2:30 for councils"; the ceiling is never a target)
All four briefs sit at exactly 400 words, and so did every era 7 council so far. Who profiles were pulled back to 2:00 for exactly this drift (Mark: "we were making exceptions for 2 minutes now we are consistantly pushing 2:30"). Test hard, sentence by sentence: would the story lose a decision, a side or a source if this sentence or clause were cut or shortened? If not, propose the cut, worded ready to apply, and the word count after it. Repetition, scene-setting that carries no decision, side or source, double attributions, and clauses that restate the README's reason are cuts. Do not cut a witness tag that places a claim with its source, or a side's own voice. Then say whether the README's length line for your council is still true after your cuts, and propose its corrected wording if not (it must not claim the full length if the brief no longer takes it). Report the brief's word count and spoken time (160 wpm) before and after your proposed cuts. A cut must not break the Flesch floor of 60 or push a sentence past 25 words; check with grade_text on a scratch copy.

## The standard
- `CLAUDE.md` (whole file; above all "Trust and source fidelity" and "Accessible and rigorous", including "No AI tells").
- `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`.
- The original review brief, `working/review_brief_r1.md` in this audit folder, for severity and mistakes to look for.
- For Trent: hostile and friendly historians (Sarpi; Pallavicino) are each given as theirs, never as settled fact.
- Mark: "dont sacrafice quality, expecially the quality of writing." Every changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler, no editors' views told as settled. Sentences at most 25 words; brief at most 400 words.
- False absences: before you accept any new or changed absence ("no held source gives X", "not held"), search all of cic/texts with whitespace- and OCR-tolerant patterns and variant spellings (Latin, Italian, German, French, Spanish, English). Report the searches. Use grep with line ranges; never read whole source files.

## Census
`git show origin/main:cic-website/data/world-census.json` (query with python). Only for changed tradition ids or census claims.

## Severity
Blocking / Substantial / Minor as in `review_brief_r1.md`. A point that only says the text could be stronger, with nothing wrong, is not a finding. A length cut is Substantial when a sentence or clause plainly carries no decision, side or source; Minor when it is a few words.

## Output
Write your part as Markdown in the shape of `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era6/R2_recheck.md` (read its first part for the format): header (files, word count and spoken time at 160 wpm, grade_text FK and Flesch from `python3 -c "import sys;sys.path.insert(0,'/home/user/CIC-Project');from engine.m7.turn_readability import grade_text;print(grade_text(open('PATH').read()))"`, longest sentence), verdict, a table of round 1 findings with status (closed / open / closed with a new point), then new Blocking / Substantial / Minor (ids like A2-B1 or B2-S1; exact text; evidence file:line with source words; a proposed fix worded ready to apply, every sentence within 25 words, each claim with its witness), Length test (sentence-by-sentence verdict, proposed cuts, counts before and after, README line), Verified, Searches run, Counts. Reply with only the path and the counts.
