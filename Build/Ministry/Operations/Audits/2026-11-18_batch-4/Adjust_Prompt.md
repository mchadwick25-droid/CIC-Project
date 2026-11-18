# Batch 4 adjustment prompt (change order, Mark 2026-11-18)

You make one targeted adjustment to a finished Church Family Tree story about **{NAME}** in `{FOLDER}/` (slug `{SLUG}`). The story passed review. Fresh listeners found one fault that matters on one hearing. Fix only that.

**The fault:** {FAULT}

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Standard.md` and `{FOLDER}/Outline.md`.
- `{FOLDER}/{SLUG}.brief.txt`, and your piece's entry in `Build/Ministry/Operations/Audits/2026-11-18_batch-4/Essences.md`.
- `{FOLDER}/{SLUG}.card.json`, for its `quotationOriginals`.

Read nothing else. Use no shared or scratch file.

## Do
1. Copy the brief to `{SLUG}.brief.v3.txt`. If that name is taken, use the next free number.
2. Make the smallest change that removes the fault.
   - Keep the essence by about word 150 (130 for the council), the hook of about three sentences, and every "also told" part.
   - Keep the ending on the person.
   - Keep every sentence the fault doesn't touch, word for word.
   - Use only what the outline holds.
   - Prefer quotes already on the card, word for word. A new quoted span needs a blind second reading, so add one only if nothing on the card will do, and list it.
   - Don't let the length grow.
3. Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`. It must pass.
4. Append to `{FOLDER}/Revision.md` a section "Adjustment (change order, 2026-11-18)". List every sentence changed, old and new, with the outline line that holds the new wording, and any new quoted span.

Do not commit. Reply in under 100 words: words before and after, the scorer line, and any new quoted span.
