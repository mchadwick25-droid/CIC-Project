# Round 1 review brief: era 4 Who batch 11 (Church Family Tree)

You are a fresh reviewer who has not seen the drafting. Review at FULL effort. Repo /home/user/CIC-Project. Edit NO repo file; write only your output file.

## Read first, all of it
1. CLAUDE.md (all of it: "Trust and source fidelity", "Accessible and rigorous", "No AI tells").
2. Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md, including its 14-item review checklist.
3. Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/briefs/lessons.md (what earlier batches' reviewers caught).
4. Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/README.md.
5. One finished profile for house form: Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch10/peter-of-sicily.* (and its records.json entry).
6. The re-score rows: Build/Ministry/Operations/Audits/2026-11-14_who-rescore-eras4-5/Rescore.md (the rows for your people).
7. Length rule (Decision-Log, "Who profile length: 2:00 restated, longer only when earned", 2026-11-15): every brief aims at 2:00, about 325 words; longer only where the README names the scene or source a 2:00 version would lose. Tighten by writing tighter, never by cutting a story off. Shorter where sources are thin. Test each brief's length.

## What to check, for each of your profiles (brief, card, records entry in batch11/records.json, audio/<id>.audio.txt)
- Every sentence of the brief and every card field: reopen the cited lines in cic/texts with sed -n (don't read whole files; use grep -n and line ranges). Who speaks, under what condition and hedge, which event a date belongs to. Does the source establish at least what the sentence says?
- Every quotation verbatim against its file, whitespace- and hyphen-tolerant, inside the cited range. Only held English may be in quotation marks in the brief and card.
- Before accepting any "no source gives X" or "only", search ALL of cic/texts for the person's name variants (OCR may double-space names). Look for the held editor who disagrees before accepting a settled claim. Every held placing of every disputed date must be on the card (died vs buried are different dates).
- Contested claims told with both sides by name, with a contested_claim record; confidence tags right (a single modern witness is not Widely Accepted).
- Partisan or hostile witnesses marked once at first use. Hagiography marked.
- Names: "of <place>" or the source's epithet at first mention in each text, for anyone a listener could confuse (namesakes!). Witnesses introduced with role and time.
- Writing (CLAUDE.md "No AI tells", Pattern checklist item 4): AI tells and generic polished voice; "not X but Y", "X, not Y", "X and never Y", colon reveals, rhetorical questions, triads, tails, aphorisms, empty contrasts, unearned adjectives, sentences past ~25 words, all-short choppy rhythm, pronouns whose referent is unclear when heard aloud, "the same" without referent, drafting-process language ("used here", "held") on reader-facing text, undefined terms. Every sentence must earn its place. American spelling outside quotes. Applies to the card too.
- Score each brief: cd /home/user/CIC-Project && python3 -c "import sys;sys.path.insert(0,'.');from engine.m1.gates import grade_text;print(grade_text(open(sys.argv[1]).read()))" <brief path>  (FK ≤ 10, Flesch ≥ 60; grade 8 is a floor worth staying above, never pad).
- Audio file equals the brief with "[calmly] " at the start and "[warmly] " at the start of the last paragraph.
- Card structure per the Pattern: field order, absent fields omitted, `uncertain` opens with the brief's own caveat, every source named on the card is in `sources` and every source listed is used, files exist.
- Records: every brief/card fact has a claim; claims quote verbatim with right line ranges.
- README: its bullets for your people (census mentions, other profiles, sources, re-score corrections, names, traditions) are accurate. For the census, the census of release 44 is at /tmp/claude-0/-home-user-CIC-Project/2ef7685d-5134-5a22-aa69-e71a985b43f9/scratchpad/census.json: walk it for every spelling and check nothing is missed and "agrees" is true.

## Output
Write to the output path given below, in this form:
"## Era 4 Who batch 11, round 1 review: PART <X>", then **Scope.**, **Method.**, **Quotations.**, **Audio.**, **Scores.** (words, minutes at ~162 wpm, FK, Flesch per brief), then "## <id>" per person with a **Verdict** line and findings labeled **R1-<X>B1 (location: problem).** for blocking and **R1-<X>M1 (...)** for minor. Blocking = something wrong, unsupported or misleading, a missing held placing, a misquote, a side told as settled, an invented detail, a misattribution, a length breach with no README reason. Minor = wording, clarity, small citation fixes. A note that something "could be stronger" with nothing wrong is NOT a finding. Each finding: the source line quoted (file:line), and an exact fix: field: "old" → "new" (and the matching records fix). Then "## README" findings, and a final **Verdict** with counts. Reply with only the path and your counts.
