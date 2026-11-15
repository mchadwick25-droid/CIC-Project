# Round 1 review brief: era 4 Who batch 12 (Church Family Tree)

You are a fresh reviewer who has not seen the drafting. Review at FULL effort. Repo /home/user/CIC-Project. Edit NO repo file; write only your output file.

## Read first, all of it
1. CLAUDE.md (all of it: "Trust and source fidelity", "Accessible and rigorous", "No AI tells").
2. Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md, including its 14-item review checklist.
3. Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch12/briefs/lessons.md (what earlier batches' reviewers caught).
4. Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch12/README.md.
5. One finished profile for house form: Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/eulogius-of-cordoba.* (and its batch11/records.json entry).
6. The re-score rows: Build/Ministry/Operations/Audits/2026-11-14_who-rescore-eras4-5/Rescore.md (the rows for your people).
7. Length rule (Mark, 2026-11-15, replacing the same day's 2:00 restatement): "They should be 1 to 2:30 not three"; his pick, "A brief can run anywhere from 1:00 to 2:30 as its story needs, not aim at 2:00." No target inside the range. Test that each brief's length fits its story: padding of a thin life, or filling toward 2:30 for its own sake, is a finding; so is a story cut off. The README gives each brief's length and one line on why.

## What to check, for each of your profiles (brief, card, records entry in batch12/records.json, audio/<id>.audio.txt)
- Every sentence of the brief and every card field: reopen the cited lines in cic/texts with sed -n (don't read whole files; use grep -n and line ranges). Who speaks, under what condition and hedge, which event a date belongs to. Does the source establish at least what the sentence says?
- Every quotation verbatim against its file, whitespace- and hyphen-tolerant, inside the cited range. Only held English may be in quotation marks in the brief and card.
- Before accepting any "no source gives X" or "only", search ALL of cic/texts for the person's name variants (OCR may double-space names). Look for the held editor who disagrees before accepting a settled claim. Every held placing of every disputed date must be on the card (died vs buried are different dates).
- Contested claims told with both sides by name, with a contested_claim record; confidence tags right (a single modern witness is not Widely Accepted).
- Partisan or hostile witnesses marked once at first use. Hagiography marked.
- Names: "of <place>" or the source's epithet at first mention in each text, for anyone a listener could confuse (namesakes!). Witnesses introduced with role and time.
- Writing (CLAUDE.md "No AI tells", Pattern checklist item 4): AI tells and generic polished voice; "not X but Y", "X, not Y", "X and never Y", colon reveals, rhetorical questions, triads, tails, aphorisms, empty contrasts, unearned adjectives, sentences past ~25 words, all-short choppy rhythm, pronouns whose referent is unclear when heard aloud, "the same" without referent, drafting-process language ("used here", "held") on reader-facing text, undefined terms. Every sentence must earn its place. American spelling outside quotes. Applies to the card too.
- Linked profiles in this batch: Dunstan, Æthelwold and Oswald share events (Edgar's reform, Glastonbury, Abingdon, Fleury, Ramsey, the Regularis Concordia); Odo of Cluny, Odilo and Benedict of Aniane share the reform of monasteries; Oswald's kinsman Odo of Canterbury is not Odo of Cluny. Where two profiles in the batch tell a shared event or dispute, check they agree, each from its own cited lines; report a mismatch against both.
- Score each brief: cd /home/user/CIC-Project && python3 -c "import sys;sys.path.insert(0,'.');from engine.m1.gates import grade_text;print(grade_text(open(sys.argv[1]).read()))" <brief path>  (FK ≤ 10, Flesch ≥ 60; grade 8 is a floor worth staying above, never pad).
- Audio file equals the brief with "[calmly] " at the start and "[warmly] " at the start of the last paragraph.
- Card structure per the Pattern: field order, absent fields omitted, `uncertain` opens with the brief's own caveat, every source named on the card is in `sources` and every source listed is used, files exist.
- Records: every brief/card fact has a claim; claims quote verbatim with right line ranges.
- README: its bullets for your people (census mentions, other profiles, sources, re-score corrections, names, traditions) are accurate. For the census, the census of release 44 is at /tmp/claude-0/-home-user-CIC-Project/a6a70c47-631c-5a34-8705-fed970b2e30a/scratchpad/census.json: walk it for every spelling and check nothing is missed and "agrees" is true.

## Output
Write to the output path given below, in this form:
"## Era 4 Who batch 12, round 1 review: PART <X>", then **Scope.**, **Method.**, **Quotations.**, **Audio.**, **Scores.** (words, minutes at ~162 wpm, FK, Flesch per brief), then "## <id>" per person with a **Verdict** line and findings labeled **R1-<X>B1 (location: problem).** for blocking and **R1-<X>M1 (...)** for minor. Blocking = something wrong, unsupported or misleading, a missing held placing, a misquote, a side told as settled, an invented detail, a misattribution, a length breach with no README reason. Minor = wording, clarity, small citation fixes. A note that something "could be stronger" with nothing wrong is NOT a finding. Each finding: the source line quoted (file:line), and an exact fix: field: "old" → "new" (and the matching records fix). Then "## README" findings, and a final **Verdict** with counts. Reply with only the path and your counts.
