# Round 3 recheck brief: era 7 council profiles, batch 2 (the last round; targeted, full effort)

You are a fresh Opus reviewer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch2). You have not seen the drafting or any fixing. You recheck ONE council. Read and grep only: do not edit any repo file and run no git command that changes anything; write only your part to the scratchpad path you are given. No paid calls, no network.

## Scope: only what round 2 changed
- Round 2 findings for your council: `../R2_recheck.md` (grep your part's heading; read only it) and what was done: `../R2_changes.md` (same part). Some were applied in corrected form; check the corrected form.
- The changes: `git diff 7ad6d2a2 HEAD -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/` restricted to your council (brief, audio, entry, its key in records.json, its README line under "Batch 2").
- For each round 2 finding: is it closed, and is the fix right? Every fix is new text: read each changed or added string against its source line in context (who speaks, which council, which year, which side). In batch 1 the blocking point after round 3 came from a round 2 fix that overstated its witness.
- Where a length cut removed words, check the sentence still says only what its witness says and that no witness tag was orphaned.
- Re-verify EVERY changed or added quote verbatim against its file in cic/texts/ (allow for hyphen line breaks, OCR, long s as f). For a translated quote, check it is faithful and adds nothing.
- Do not re-review unchanged text. Raise a point in unchanged text only if it is blocking.
- For Trent, Sarpi (hostile to the papal court) and Pallavicino (writing against him for Rome) are each given as theirs, never as settled fact.

## The standard
- `CLAUDE.md` (whole file; above all "Trust and source fidelity" and "Accessible and rigorous", including "No AI tells"). `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`. Severity as in `review_brief_r1.md`.
- Mark: "dont sacrafice quality, expecially the quality of writing." Every changed reader-facing string: no empty contrasts, no summing-up lines, no filler. Sentences at most 25 words; brief at most 400 words, and the ceiling is never a target. Flesch at least 60.
- Any new absence: search all of cic/texts with OCR-tolerant patterns and variant spellings before accepting it. Grep with line ranges; never read whole source files.
- A point that only says the text could be stronger, with nothing wrong, is not a finding. This is the last round: for any Minor fix to reader-facing text, word it exactly, ready to apply as worded.

## Output
Markdown in the shape of `../R2_recheck.md`'s parts: header (files, words and spoken time at 160 wpm, grade_text FK and Flesch, longest sentence), verdict, table of round 2 findings with status, new Blocking / Substantial / Minor (ids A3-*, B3-*, C3-*, D3-*; exact text; evidence file:line with source words; fix worded ready to apply), Verified, Searches run, Counts. Reply with only the path and the counts.
