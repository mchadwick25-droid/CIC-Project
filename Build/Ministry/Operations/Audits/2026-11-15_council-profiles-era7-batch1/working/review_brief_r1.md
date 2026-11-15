# Round 1 review brief: era 6 council profiles (full review, full effort)

You are a fresh Opus reviewer for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era6). You have not seen the drafting. You review ONE council in full. Do not edit any repo file; write only your review part to the scratchpad path you are given. No paid calls, no network.

## What to review (your council's files)
- `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/<id>.brief.txt` (the spoken brief; the reader-facing text that matters most)
- `.../era6/audio/<id>.audio.txt` (must equal the brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph)
- `.../era6/<id>.entry.json`
- `.../era6/records.json`, key `<id>`
- `.../era6/README.md` (the join of gatherings, where it concerns your council)

## The standard
- `CLAUDE.md` (whole file; above all "Trust and source fidelity" and "Accessible and rigorous", including "No AI tells").
- `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md` (whole), with its checklist C1-C8, and the Who checklist items 1-9, 11 and 13 in `Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md`.
- The model: era 5's `second-council-of-lyon-1274` in `Council-Profiles/era5/`, and the shape of the era 5 review `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era5/R1_review.md` (read its first part to see the format and the kinds of finding).
- Mark's words: "dont sacrafice quality, expecially the quality of writing." The AI-tells and generic-voice check covers every reader-facing string (brief, teaser, knownFor, every entry string): no empty contrasts, no "X and never Y", no summing-up lines, no filler. Every sentence must earn its place. Sentences no longer than 25 words. Grade 8 is a floor worth staying above, but never pad; the brief is at most 2 minutes 30 seconds (about 400 words at 160 wpm).

## Mistakes the earlier reviews caught (look hard for these)
- False absences ("no held source gives X", "not among our sources") where a held file does give it. Before you accept any absence, search all of cic/texts with whitespace- and OCR-tolerant patterns (double-spaced OCR; long s as f; hyphen line breaks; Latin, Greek, German, French, Czech, English spellings). Report the searches you ran.
- A claim that sits with the wrong witness, above all after sentences were split or joined (era 5's round 3 blocking point put a 1309 gift under the wrong writer).
- A reversed source; a wrong-preface citation (an editor's preface or note given as the author's); a contested point told as settled; "Widely Accepted" where a held editor disagrees; a modern editor's date or count told as an ancient witness's.
- A count of an editor's omissions not backed by counting every one.
- A quote not verbatim. Re-verify EVERY quote in the brief and entry against its file and lines (allowing for hyphen line breaks and OCR); for a translated quote, check the translation is faithful and adds nothing. Read each cited line in context: who speaks, which council, which year.

## Census
Live census: `/tmp/claude-0/-home-user-CIC-Project/1796b1ed-67d8-5bb9-8f37-94a4cc60df92/scratchpad/census.json` (a copy of origin/main's cic-website/data/world-census.json). Check the entry's traditions ids and names exist at the date, and where the live tree already says something about this council, that the entry agrees or the difference is real and should be flagged for Open-Gaps. Check for parties at the council with no census tradition at the date.

## Severity
- Blocking: a fabrication, a false absence, a misquote, a claim given to the wrong witness, a contested point told as settled in reader-facing text, or anything else wrong or misleading in the brief.
- Substantial: wrong or unsupported in the entry or records; a missing contested claim; a pattern rule broken.
- Minor: wording, a sentence over 25 words, a small citation slip, an AI tell.
A finding that only says the text could be stronger, with nothing wrong, is not a finding (CLAUDE.md, review cap).

## Output
Write your part as Markdown to the path you are given, in the era 5 R1 shape: header (files, word count and spoken time, grade_text FK and Flesch from `python3 -c "import sys;sys.path.insert(0,'/home/user/CIC-Project');from engine.m7.turn_readability import grade_text;print(grade_text(open('PATH').read()))"`, longest sentence), verdict, Blocking / Substantial / Minor (each with an id like A-B1, the exact text, the evidence file:line with the source words, and a proposed fix worded ready to apply), Verified (what you checked and found right), Searches run (absences), Counts. Proposed fixes to reader-facing text must keep the brief within 400 words and every sentence within 25 words, and must keep each claim with its witness. Reply with only the path and the counts.
