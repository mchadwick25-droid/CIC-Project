# Rechecker (round 2, targeted)

You recheck the revised narrator texts of one built world, `{WORLD}`. You wrote none of them and did not write the review. Folder: `Build/Ministry/Features/Church-Family-Tree/World-Narration/{WORLD}/`. Check only what changed, against the prior findings; do not re-review from scratch.

Read `Review_Round1.md`, the `<key>.review.md` files for the revised pieces, and `Revision_Round1.md`. For each revised piece compare `<key>.v1.txt` with `<key>.txt`.

Check:
1. Each finding was answered as worded, and no other sentence changed.
2. Each PRE-EXISTING correction (Mark's rule: the tree text says only what the record's sources and confidence hold) is itself right: open the grounding record under `records/` named in `<key>.sheet.md` and, where needed, its cited source in `cic/texts/`, and confirm the new wording neither overstates nor drops what they hold. This is the correction's independent check.
3. Each "own wording" change adds nothing and reads clearly heard once.
4. Quotes unchanged character for character; no first person outside quotes. Run, from the repo root, `python -m engine.m1.profile_readability` on the revised `<key>.txt` files (hard limits grade 10, ease 60).

If a change is wrong, give exact replacement wording and apply it yourself to `<key>.txt` only when it is a fix you are certain of; list it. Anything you cannot settle is REVISE for Mark.

Write `Recheck_Round2.md`: per revised piece PASS or REVISE, each correction confirmed with its record and line, and any edit you made (old and new). Edit nothing else; do not commit. Reply in under 120 words.
