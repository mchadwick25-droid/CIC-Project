# Writer

You write one Church Family Tree text about **{NAME}**, heard aloud (a connection note is read). Write from these files and nothing else in the repository:
- `{FOLDER}/Outline.md`
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Part 1 only (the standard)
- the kind kit the story header names (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/<kind>.md`)
- the reference stories the kind kit names, each `*.brief.txt` in its folder under `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/reference/`, read once for voice. Do not copy their order, openings, endings or moves.

Write `{FOLDER}/{SLUG}.brief.txt`: plain text, no title, a blank line between paragraphs. Follow the standard and the outline's Do not say list. Use only what the outline holds, and only its quotes, word for word. The length is the outline's, at about 150 words a minute, 130 for a council; to meet it, drop only from its cut-first list, in order, and if it still runs long, stop and say so.

Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`. It must pass the limits. Run `python tools/check_brief_craft.py {FOLDER}/{SLUG}.brief.txt` and judge each line it lists by Part 1: fix what breaks a rule, and leave what does not. If the grade is under 8, look for runs of short one-act sentences and link them; never simplify to move the score. Then hear it once as the standard's listener and fix anything that would lose them or talk down. Before you hand on, re-read your own work for the four faults in Part 1 of the kit. Fix what you find, and say in your reply that you checked. Use American spelling outside the outline's quotes.

Do not commit or edit anything else. Reply with the word count, the scorer line, and how you opened and ended.
