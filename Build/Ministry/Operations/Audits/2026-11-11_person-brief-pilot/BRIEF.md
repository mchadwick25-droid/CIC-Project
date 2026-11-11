# Person-brief pilot — drafting brief (read all of it)

You are rewriting the Church Family Tree "person brief" (the census `longDescription`) for some named people. The current text of each entry, with its other fields (why, sourcing, floorNote, legacy, voices), is in
/tmp/claude-0/-home-user-CIC-Project/6d98dab9-13d8-521f-bb4d-c1b444ee38ce/scratchpad/pilot/entries.json
Read the project rules in /home/user/CIC-Project/CLAUDE.md, sections "Trust and source fidelity" and "Accessible and rigorous". They govern this.

## Mark's standard (the project lead, his words)
- "i want the brief to be both personal (their story) and theological (major stances, they fought for, they developed, they defended ....) ... 60 - 120 [seconds] depending on their size of scope and influence" — about 150–300 words.
- "these are a little flat and ai ish, i want it a little more story telling, not fact giving. the years read as natural not just reading numbers, the sentences flowing together not all short simple sentences for an elementary student".
- Name real witnesses ("Eusebius says…", "Palladius, who knew him, tells…"). NEVER abstract roles ("his editor", "the translator", "a modern scholar", "historians"). When the only account is hostile, or accounts disagree, say so plainly in story terms ("Eusebius is our only witness for this, and he was writing a generation later").
- The card already shows dates, place, tradition, role and works: don't recite them as a list. Don't mention the Library, its shelves, or "sources the Library holds". Don't open with who claims them; open with the person.
- Written for the ear: it will be read aloud by a mature narrator. Years should sound natural ("in the spring of 325", "around the year 230", "when he was about seventeen", "in his last years"), not strings of numbers. Avoid parentheses, abbreviations (no "c.", "CE", "St."), slashes, and lists the ear can't follow.

## Content of each brief
1. Their story: the human life, told as story, with a few concrete moments.
2. What they taught, developed, defended, and fought against — the theology, said plainly but precisely (don't trade the idea for a simpler one).
3. Why it mattered then and after.
4. One line in their own words, where a vendored source file holds it, quoted VERBATIM from that file (an English translation in the file is fine; quote it exactly as printed, character for character; you may trim with "..." only at a clause boundary and must say so in your notes). Weave it in naturally ("In his own words: ..." is acceptable but find something better if you can). If no file holds a usable line, say so in your notes and leave it out — never paraphrase inside quotation marks.

## Fidelity (the hard rule)
- Every factual claim must be traceable to a vendored file in /home/user/CIC-Project/cic/texts/ (or the entry's own cited works). Find the passage. If you cannot find support, drop the claim. Do not draw on memory for facts you have not located in a file — memory is where invention comes from.
- Contested points are told as contested, in story terms. Never present a disputed claim as settled.
- No invented detail, motive, feeling, scene or dialogue. Story-telling comes from arranging and voicing real events, not from adding color.
- The files are large. Use grep -n with distinctive words, then sed -n 'A,Bp' to read the passage. Don't cat whole files.

## Readability (the project's tool)
Score each draft with:
  python3 /tmp/claude-0/-home-user-CIC-Project/6d98dab9-13d8-521f-bb4d-c1b444ee38ce/scratchpad/pilot/score.py FILE
Band: Flesch-Kincaid grade 8 to 10 (8 is a floor, 10 a ceiling), Flesch Reading Ease at least 60. Get there by flowing sentences of varied length (average roughly 15–20 words, none past about 28), plain words, active verbs — not by chopping into short simple sentences and not by long nested ones. American spelling.

## No AI tells
No "a towering figure", "tapestry", "legacy that echoes", "not just X but Y", "in a world where", rhetorical questions, triplet cadences, "Today, ..." closers, summary morals. Endings should land on a fact or the person's own voice, not a sermon.

## Deliverables (in YOUR scratch directory only, named below)
For each person `<id>`:
- `<id>.txt` — the brief only, plain text, paragraphs separated by a blank line. No heading.
- `<id>.notes.md` — a claim table: every claim in the brief → file name + line number(s) + the short supporting phrase from the file. The quote: file, line number, and the exact line as printed. List any contested point and how you marked it. List anything from the coordinator's checklist you DROPPED because you couldn't source it. Paste the score.py output.
Do not write anywhere in the repository. Do not commit. Do not call any model or web API.
When finished, reply with a short summary: per person, words, FK, FRE, the quote's source, and anything dropped or uncertain.
