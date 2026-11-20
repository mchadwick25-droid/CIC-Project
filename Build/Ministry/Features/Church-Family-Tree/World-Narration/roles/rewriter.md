# Rewriter

You rewrite the narrated texts of one built world, `{WORLD}`, from the world's own voice into the Church Family Tree narrator's voice. The tree will show and play them. Folder: `Build/Ministry/Features/Church-Family-Tree/World-Narration/{WORLD}/`.

Read first, and nothing else in the repository: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Parts 1 and 2 only; then, for each piece `<key>` in the folder, `<key>.sheet.md` (the original text, its grounding records with confidence and notes, and each quoted span with its quote record). `<key>.orig.txt` is the same original text.

For each piece write `<key>.txt`: plain text, a blank line between paragraphs, no title.

What the rewrite does (Mark, 2026-11-20: "change the voice, and link the prose"):
1. **Voice.** The original speaks as the world itself: "our communities", "our tradition", "us", "we cannot be sure", "this world's own…", a Representative's address to the listener. The narrator stands outside every church. First person becomes third person ("these churches", "the monks", "the reformers"). "This world" phrasing becomes the plain historical subject. A world's emic hedge becomes the narrator's plain statement of uncertainty ("No source says…", "Historians dispute whether…", "It is not certain that…"), at exactly the same strength of doubt. No build vocabulary ("gravity", "option", "formation", "record") a listener could not follow.
2. **Link the prose.** Join runs of short one-act sentences the way an adult documentary narrator does, with cause, contrast and time. A "so" or "because" that implies cause or motive must already be in the original or its sheet. No sentence past about 30 words.
3. **Keep everything else.** Same content, same order. Every claim stays at its confidence; every qualifier and doubt keeps its strength; every witness stays credited. Add no claim, detail, feeling, name or date. Never soften a hostile view or the record's force or conflict. A wonder stays in its witness's voice. Do not re-tell to the kit's full craft (no new hook, no reordering); fix only a real failure: an event told twice, or a passage a listener could not follow.
4. **Quotes word for word.** Every quoted span stays exactly as in the original, character for character, credited to the same speaker. Add no quote; paraphrase nothing inside quote marks.
5. American spelling outside quotes. Plain modern words; simplify the language, never the thought.

Run, from the repo root, `python -m engine.m1.profile_readability` on your `<key>.txt` files only (not `.orig.txt`). Each must pass the hard limits (grade 10, ease 60). Under grade 8, link any remaining runs of one-act sentences; never simplify the thought to move a score.

Before you finish, re-read each rewrite against its original sentence by sentence for: a witness's claim told as fact; an editor's view given to the source; a date or detail moved onto the wrong event; force or conflict softened by leaving it out; any "we/our/us" left outside quotes. Fix what you find. If you see a claim in the original that its sheet does not hold, keep it, and name it in your reply.

Write only the `<key>.txt` files; do not commit. Reply in under 200 words: grade and ease per piece, any link word you were unsure of, any original claim you think is unsupported, and that you ran the final check.
