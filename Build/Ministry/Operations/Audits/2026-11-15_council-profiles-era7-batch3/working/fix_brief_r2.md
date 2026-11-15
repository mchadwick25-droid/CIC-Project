# Round 2 fix brief: era 7 council profiles, batch 2

You are a fresh Opus fixer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch3). You apply ONE council's round 2 recheck. No paid calls, no network. Do not commit.

## Read first
- /home/user/CIC-Project/CLAUDE.md: "Trust and source fidelity" and "Accessible and rigorous" (above all "No AI tells").
- Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md.
- Your round 2 recheck part (path given); for context, your council's parts of ../R1_review.md and ../R1_changes.md (grep its heading; read only that part) in full.

## What you may edit
- `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/<id>.brief.txt` and `<id>.entry.json`.
- Your council's records file `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch3/working/records_<id>.json` (the worker merges it into era7/records.json; do not edit records.json).
- Then run `python3 Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch3/working/mkaudio.py` to regenerate the audio (it regenerates all four batch 3 audio files from their briefs; harmless to the others).
- Do NOT edit README.md, Open-Gaps.md or any other file. If a finding asks for a README or Open-Gaps change, word it ready to apply in your changes file.

## How to apply
- Apply every Blocking, Substantial and Minor finding, unless re-reading the source shows the finding itself is wrong; then do not apply it and say why with file:line.
- Read every fix as NEW TEXT against its source line in context (who speaks, which event, which year). An earlier round 2 rewrite reversed a scholar's view by applying a fix without re-reading. Re-open each cited line yourself (grep -n / sed -n ranges; never whole files).
- When a fix splits or joins a sentence, check each claim still sits with its own named witness.
- The reviewer's scratch copy of the fixed brief (path in the review) is a lead; check each changed sentence yourself.
- Brief limits: at most 400 words (wc -w), every sentence at most 25 words; FK grade 8 is a floor worth staying above but never pad. Check with `python3 Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch3/working/grade.py <brief>`. The 400-word ceiling is never a target: if the fixes free words, do not fill them.
- Entry and records must agree with the brief in every fact. Validate JSON with python -m json.tool.

## Output
Write your changes file (path given) in the era 6 R1_changes shape (see Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/R1_changes.md, first part): for each finding id, Applied / Applied in corrected form (say how and why, with file:line) / Not applied (why); then the brief's new figures (words, spoken time, FK, Flesch, longest sentence); then "README text proposed" and "For Open-Gaps" lists if any. Reply with only the path, the counts applied / corrected / not applied, and the new brief figures.

## Batch 2 additions
- Length (Mark, 2026-11-15): the ceiling is never a target. If the reviewer names a sentence or clause that does not earn its place, cut it and leave the words unused. Do not add sentences that a finding does not need.
- Reading ease 60 or above (Flesch); report it.
- Other councils' fixers are working at the same time on their own files; touch only your council's files.

## Round 2 additions
- Apply the recheck's length cuts unless a cut would lose a decision, a side or a source, or would orphan a witness tag; then say why. Do not refill freed words.
- After the cuts, word the corrected README length line for your council (README text proposed) so it says truly why the brief runs the length it now runs, and gives "about m:ss" from the new word count at 160 wpm.
- Write your changes file in the shape of ../R1_changes.md's parts.
