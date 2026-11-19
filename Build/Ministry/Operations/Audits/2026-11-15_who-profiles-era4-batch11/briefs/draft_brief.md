# Drafting brief: Church Family Tree Who profile (era 4 batch 11)

You draft one Who profile (brief, card, records) from a source dossier. Repo /home/user/CIC-Project. Quality of writing and source fidelity come before everything (Mark: "dont sacrafice quality, expecially the quality of writing").

## Read first, all of it
1. /home/user/CIC-Project/CLAUDE.md, sections "Trust and source fidelity" and "Accessible and rigorous".
2. Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md (the pattern and its 14-item checklist).
3. /tmp/claude-0/-home-user-CIC-Project/2ef7685d-5134-5a22-aa69-e71a985b43f9/scratchpad/lessons.md (mistakes reviewers caught in earlier batches; avoid every one).
4. House form, finished examples: Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch10/peter-of-sicily.brief.txt and .card.json and that file's records.json entry "peter-of-sicily"; and this batch's own drafts in Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/ (stepanos-of-taron.*, ibn-ishaq.* and their records at /tmp/claude-0/-home-user-CIC-Project/2ef7685d-5134-5a22-aa69-e71a985b43f9/scratchpad/rec/*.json). For an outside witness, also batch8/al-baladhuri.card.json (it has "label": "Outside witness" and tradition "Outside the church").
5. Your person's dossier (path below). Treat it as leads, not truth: reopen every line you use with sed -n in cic/texts/ and confirm who speaks, hedges, conditions and dates. Don't read whole files.

## What to write
- `<id>.brief.txt` in Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/: about 325 words (2:00 spoken; aim 320-335, never over ~340), paragraphs separated by one blank line, no audio tags. Opens on one sourced scene; the who-line within the first few sentences; then their story and what mattered, the positions they held or recorded told through events; disputes told in place with witnesses named; a close in their own words if held, else how later readers remembered them. Tighten by writing tighter, never by cutting a story off. Grade: FK ≤ 10 and Flesch ≥ 60 (score with: cd /home/user/CIC-Project && python3 Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/briefs/score.py Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11 — it also writes the audio file; don't edit audio by hand).
- `<id>.card.json`: fields in this order: name, (label only for outside witness), otherNames, knownFor, dates, place, tradition, role, briefLength ("about 2 minutes"), keyWorks (max 3; title, about), legacy {traces, remembered}, uncertain (opens with the brief's own caveat; each item names its witnesses; every held placing of every disputed date), sources {ownWords, about} (each: title, author, date, language, file "cic/texts/<basename>"). Absent fields left out. Every source named on the card is in sources; every source in sources is used. indent=2, ensure_ascii=False, final newline.
- Records: /tmp/claude-0/-home-user-CIC-Project/2ef7685d-5134-5a22-aa69-e71a985b43f9/scratchpad/rec/<id>.json: {"claims":[{claim, witness, formation_confidence}], "contested_claims":[{claim, sides:[...]}], "absent_details":[{detail, note}]}. Claims quote the source verbatim as the scan reads (mark "(scan)" where garbled), witness = "TAG (basename), l.X-Y". One claim for each fact in brief and card. formation_confidence one of: Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential-Thin. A single modern witness is not Widely Accepted. absent_details say what was searched.

## Hard rules
- Never invent: no family, feeling, motive, office, adjective or scene the held lines don't give.
- Only held ENGLISH goes in quotation marks, verbatim. Latin, Greek, German, French, Syriac, Arabic are told in modern words with the source named.
- Name real witnesses ("Duval says"), introduced at first mention with role and time ("Rubens Duval, who edited the letters in 1905"). A partisan or hostile witness is marked once at first use.
- Disputed dates: the brief may give one only with its owner, or the spread; the card gives every held placing by name.
- Common names get "of <place>" or the source's epithet at first mention in each text (brief and card separately).
- No AI tells, no "not X but Y", "X, not Y", "X and never Y", colon reveals, rhetorical questions, triads, tails, aphorisms, quotable closers, hedging filler, unearned adjectives, sentences past ~25 words, pronouns with unclear referents, "the same" without referent, drafting-process words ("used here", "held") in the brief. Every sentence earns its place. American spelling outside quotes. Define terms a listener won't know (catholicos, etc.).
- Card tradition: use the census's own tradition name given below.

## Report back
Reply with: the files written, word count / FK / Flesch, and a short list (max 12 lines) of README material: which census passages agree or differ (from the dossier, re-checked), corrections to the re-score row, name/id calls, any judgment the coordinator should see. Keep it short.
