# Card writer

You update the card for **{NAME}** to match its finished brief. Start from the existing card, `{CARD}`. Keep what is good, change only what the new brief and its source sheet require, and keep the card's existing fields and shape.

Read the brief `{FOLDER}/{SLUG}.brief.txt`, then `{FOLDER}/Outline.md`, `{FOLDER}/Source_Sheet.md` and the existing card. For the format of a card's quotations and references, look at `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`.

1. Correct any claim on the card that the source sheet contradicts, and give its confidence plainly where it is uncertain. If you cannot find support for a claim, leave it in place and list it in your reply as not found; the checker decides whether it stays.
2. Make the card agree with the brief. Its known-for, role, dates, place, tradition, legacy and uncertainties tell the same story. The card can carry fuller qualifications than the brief, never different facts.
3. **Quotations and references.** For every quote the brief uses, give the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. List the references the brief draws on. Re-read each cited line in its file.
4. Set `briefLength` to the brief's real length.
5. Leave connections to other entries out for now.

Write the updated card to `{FOLDER}/{SLUG}.card.json`. Do not edit the census, the existing card or the brief, and do not commit. Reply in under 120 words: what you kept, what you changed and why, and any claim you could not find support for.
