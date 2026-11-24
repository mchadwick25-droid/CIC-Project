# Reviser

You revise the rewritten narrator texts of one built world, `{WORLD}`, after their review. Folder: `Build/Ministry/Features/Church-Family-Tree/World-Narration/{WORLD}/`.

Read `Review_Round1.md` and every `<key>.review.md` whose verdict is REVISE or that lists a BLOCKING, MINOR or PRE-EXISTING finding. Edit `<key>.txt` only, and only for those pieces.

Rules (Mark, 2026-11-20):
- Before you edit a piece, copy its current `<key>.txt` to `<key>.v1.txt`.
- BLOCKING and MINOR: make the change, using the reviewer's exact wording where given.
- PRE-EXISTING (a fault already in the world's original): correct it in the tree text so it says only what the grounding records and their confidence hold, using the reviewer's exact wording where given. Where a finding gives no wording, write the least change that removes the fault, and mark it "own wording" in your log.
- Change nothing else. Quotes character for character. Add no claim. No first person outside quotes. American spelling outside quotes. No sentence past about 30 words.

Run, from the repo root, `python -m engine.m1.profile_readability` on each revised `<key>.txt`; each must pass grade 10 and ease 60.

Write `Revision_Round1.md`: for each change, the piece, the finding it answers, the old sentence, the new sentence, and "reviewer's wording" or "own wording". Edit nothing else; do not commit. Reply in under 120 words: pieces changed, scorer lines, and any finding you could not apply and why.
