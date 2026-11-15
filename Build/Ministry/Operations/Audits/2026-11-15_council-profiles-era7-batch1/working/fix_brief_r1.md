# Round 1 fix brief: era 7 council profiles, batch 1

You are a fresh Opus fixer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch1). You apply ONE council's round 1 review. No paid calls, no network. Do not commit.

## Read first
- /home/user/CIC-Project/CLAUDE.md: "Trust and source fidelity" and "Accessible and rigorous" (above all "No AI tells").
- Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md.
- Your review part (path given) in full.

## What you may edit
- `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/<id>.brief.txt` and `<id>.entry.json`.
- Your council's records file `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/records_<id>.json` (the worker merges it into era7/records.json; do not edit records.json).
- Then run `python3 Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/mkaudio.py` to regenerate the audio.
- Do NOT edit README.md, Open-Gaps.md or any other file. If a finding asks for a README or Open-Gaps change, word it ready to apply in your changes file.

## How to apply
- Apply every Blocking, Substantial and Minor finding, unless re-reading the source shows the finding itself is wrong; then do not apply it and say why with file:line.
- Read every fix as NEW TEXT against its source line in context (who speaks, which event, which year). An earlier round 2 rewrite reversed a scholar's view by applying a fix without re-reading. Re-open each cited line yourself (grep -n / sed -n ranges; never whole files).
- When a fix splits or joins a sentence, check each claim still sits with its own named witness.
- The reviewer's scratch copy of the fixed brief (path in the review) is a lead; check each changed sentence yourself.
- Brief limits: at most 400 words (wc -w), every sentence at most 25 words; FK grade 8 is a floor worth staying above but never pad. Check with `python3 Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/grade.py <brief>`. The 400-word ceiling is never a target: if the fixes free words, do not fill them.
- Entry and records must agree with the brief in every fact. Validate JSON with python -m json.tool.

## Output
Write your changes file (path given) in the era 6 R1_changes shape (see Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era6/R1_changes.md, first part): for each finding id, Applied / Applied in corrected form (say how and why, with file:line) / Not applied (why); then the brief's new figures (words, spoken time, FK, Flesch, longest sentence); then "README text proposed" and "For Open-Gaps" lists if any. Reply with only the path, the counts applied / corrected / not applied, and the new brief figures.
