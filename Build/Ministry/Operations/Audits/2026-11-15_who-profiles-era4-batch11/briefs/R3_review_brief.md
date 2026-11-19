# Round 3 review brief: era 4 Who batch 11 (Church Family Tree)

You are a fresh Opus reviewer who has not seen the drafting or rounds 1-2. This is round 3, the last round allowed: a TARGETED RECHECK, at FULL effort. Repo /home/user/CIC-Project. Edit NO repo file; write only your output file.

## Read first
1. CLAUDE.md, all of it ("Trust and source fidelity", "Accessible and rigorous", "No AI tells").
2. Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md, including its review checklist.
3. Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/briefs/lessons.md.
4. Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/R2_review.md (your part's section) and R2_changes.md (your part's section, plus the worker's README log at its end). Read R1_review.md only where a round 2 finding points back to it.
5. The round 2 changes: `git diff a9674142 HEAD -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/` (look at your people's files and records entries, and the README).
6. Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/README.md.

## Scope
Only what changed in round 2, against round 2's findings:
- For every round 2 finding on your people: was it applied, and applied correctly? A "not applied" or "applied with change" needs your ruling.
- Every fix is NEW TEXT. Read each changed string against its source line in context (sed -n with line ranges in cic/texts; grep -n; never read whole source files). Who speaks, under what condition and hedge, which event a date belongs to. Round 2 blocking fixes need your independent re-confirmation: say for each whether it holds. Most blocking points in later rounds come from the previous round's fix wording.
- Re-verify every changed or added quotation verbatim against its file in cic/texts, whitespace- and hyphen-tolerant, inside the cited range. Only held English may stand in quotation marks on brief and card.
- Check every fix for: "X, not Y", "not X but Y", "X and never Y", colon reveals, tails, aphorisms, triads, sentences past ~25 words, pronouns unclear aloud, unintroduced names, namesakes without "of <place>", drafting language ("used here", "held") on reader-facing text, American spelling outside quotes.
- Tightening can drop a side, a hostile marker or a referent: check each contested point keeps its sides.
- Card fix => matching records fix; records ranges include the quoted line; confidence tags right (a single witness is never Widely Accepted).
- Reread every brief of yours that changed in round 2 in full, once, for flow. Flag only what is wrong, not what "could be stronger".
- Length: every brief aims at 2:00, about 325 words (Decision-Log "Who profile length: 2:00 restated, longer only when earned", 2026-11-15). Past about 2:05 (~338 words at 162.5 wpm) needs a README line naming what 2:00 would lose. Score each brief: cd /home/user/CIC-Project && python3 Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/briefs/score.py Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11 (this also rebuilds audio files from briefs; that is fine). FK ≤ 10, Flesch ≥ 60.
- Audio file equals the brief with "[calmly] " at the start and "[warmly] " at the start of the last paragraph.
- Census of release 44 (for README census bullets that changed): /tmp/claude-0/-home-user-CIC-Project/5b00fb58-7032-59fb-a8d1-435a7e47a79e/scratchpad/census.json.

Do not re-review untouched text from scratch. Do raise a blocking point in untouched text only if you trip over one that is plainly wrong (an invented detail, a misquote).

## Output
Write to the output path given below:
"## Era 4 Who batch 11, round 3 review: PART <X>", then **Scope.**, **Method.**, **Quotations.** (each changed quote: verified / not), **Audio.**, **Scores.** (words, minutes, FK, Flesch per brief), **Round 2 findings.** (a line per R2 finding of your part: confirmed applied / problem), then "## <id>" per person with a **Verdict** and new findings labeled **R3-<X>B1 (location: problem).** for blocking and **R3-<X>M1** for minor. Blocking = wrong, unsupported or misleading; a missing held placing; a misquote; a side told as settled; an invented detail; a misattribution; a length breach with no README reason; an AI tell of the forbidden kinds in reader-facing text. Minor = wording, clarity, small citation fixes. "Could be stronger" with nothing wrong is NOT a finding. Each finding: the source line quoted (file:line), and an exact fix: field: "old" → "new" (and the matching records fix), with any replacement text itself checked against its source and the writing rules. Then "## README" findings for your part, and a final **Verdict** with counts. Reply with only the path and your counts.
