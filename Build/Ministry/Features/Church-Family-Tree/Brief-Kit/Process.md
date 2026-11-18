# How a brief is made

Each step is run by a fresh hand with its own prompt in `roles/`. A batch is worked one at a time, and is recorded only once every brief and card in it has finished every step, revisions included.

1. **Research** (`roles/researcher.md`). A source sheet from held texts, then a one-page outline to `Outline_Template.md`.
2. **Outline check** (`roles/checker.md`). Every line tested against the source texts. Blocking faults are fixed and rechecked independently.
3. **Write** (`roles/writer.md`). From the outline, `Shapes.md` and `Standard.md` only.
4. **Review** (`roles/reviewer.md`). First, across the whole batch, `python tools/check_brief_variety.py` counts the moves that repeat; a move in more than a quarter of the batch goes back to those pieces' writers, and the counts are kept with the batch. Then, for each piece, the acceptance test from one hearing, and the separate source check. A clear story can still hold a factual error.
5. **One revision, one recheck.** A brief that still fails comes to Mark with the reason.
6. **Card** (`roles/card.md`). Keep the existing card word for word. Add only what the new brief brings, and correct only what is clearly wrong, with every edit listed with its evidence. The checker confirms each edit is justified, that nothing else moved, and rules on each claim flagged as not found.

## The bar

Block only for unsupported claims, misleading implications, missing essential material, a genuine failure to understand on one hearing, or a stretch that reads as a children's book. "Could be stronger" is not a finding. Scores and counts are warnings, not quotas. The aim is academic soundness, not perfection.

## Keeping the kit clean

- Fix a problem where it starts. An error a writer could repeat goes into that outline's Do not say list. A gap in the method goes into the kit.
- A new ruling rewrites the line it touches. A line is added only when no existing line covers it. `Standard.md` stays one page.
- Make targeted corrections and preserve approved text. Do not reopen finished briefs for optional polishing.
