# Batch 10, the modern pass: the release

Read `Build/Ministry/Operations/Audits/2026-11-22_batch-10/About-Pass/G_Release.md` and `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/release.md`, and follow them with these differences. This is a third release of the same twelve stories, after the modern pass (Decision-Log, "No modern opinion, guess or reconstruction in a story", Mark, 2026-11-23, "yes go ahead, option A stricter"). Read `Release_About.md` for how the last one handled each tool.

1. **Checks already applied.** Every card check of this pass (`<slug>/Card_Check_Modern.md`) is applied, as `<slug>/Card_Check_Modern_Applied.md` records, and verified by script. Do not re-apply anything.
2. **The census.** For all twelve, `longDescription` becomes `<slug>.brief.txt` with its final newline removed, and `card` becomes `<slug>.card.json` (for Ephesus, `council`). Change no other field. Edit by exact string replacement of each value, never by re-dumping the file; a field-by-field diff against HEAD must show only these 24 fields changed.
3. **`tools/quote_renderings.json` and `tools/quote_scan_readings.json`.** No quoted span changed in this pass; confirm every listing for these twelve still stands word for word in its brief, and change nothing unless one does not.
4. **Rebuild, checks and ledger** as before, each check with its output line, including `python tools/check_live_commentary.py --base origin/main --enforce`, `python tools/check_spelling.py --enforce --base origin/main`, `python tools/check_standard_lock.py --base origin/main`, `python tools/check_open_gaps_numbers.py`, and the readability check on all twelve briefs. Run `python tools/list_story_status.py --write`.
5. Write `Release_Modern.md` in the batch folder: what changed, judgment calls, the checks with their output lines, and what is not done.

Write any scratch script in `/tmp/claude-0/-home-user-CIC-Project/30f7ff74-3ed4-5f83-9127-e384c2ec4ddf/scratchpad/release3/`, never in the repository. Do not record audio. Do not commit. Reply in under 150 words.
