# Batch 10, the "what it was about" pass: the card

Story: **{NAME}**, folder `Build/Ministry/Operations/Audits/2026-11-22_batch-10/{SLUG}/`. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md` and follow it, with these specifics. Do not edit the brief, the census, any file under `tools/`, or any other folder. Write any scratch script inside your own folder and delete it when you are done.

- **The starting card** is `{SLUG}.card.json` as it now stands (already checked twice in this batch). Copy it to `Card.pass2.json` first, and keep it word for word except for the edits below.
- **What changed:** the brief was changed by this pass. Read `{SLUG}.brief.txt`, compare it with `{SLUG}.brief.v3.txt` (`diff`), and read `Outline.md`'s **What it was about** and **Room for it** sections, `Writer_About_Reply.md`, `Fresh_Read_About.md` and `Fresh_Read_About_Applied.md` (and `Pelagius_Clause_Fix.md` and `Pelagius_Clause_Check.md` where they exist).
- **Edits to make:**
  1. Each new explanation the brief now tells, with its source: add its reference (`briefReferences`, and `sources` for any newly cited file), saying no more than the brief and its cited lines, which you re-read.
  2. Each item this pass marked "to the card", "card", or "leave it out" with the card as its home: add it in the field it belongs to (`uncertain`, `legacy.traces`, `legacy.remembered`, `sources.about`; for the council `attended`, `decided`, `outcome`, `record`, `calledBy`), worded as plainly as the outline gives it, credited where the outline credits.
  3. Each `briefReferences` entry naming something the brief no longer tells (a cut event, a name no longer named): remove it.
  4. Quotations: `quotationOriginals` one entry per quoted span in the brief now, and none for a span it no longer quotes. A changed quote takes its new rendering exactly as the brief has it, with its printed and original wording verbatim from file and lines. Follow the role on `secondReading`.
  5. Anything `Fresh_Read_About_Applied.md` says the card must correct.
- Keep every other field word for word. American spelling outside printed wording. No audit file named.
- Run `node tools/validate-census.mjs --skip-quotes` against a scratch copy of `cic-website/data/world-census.json` with this card in place (never the real census), and report its errors for this entry.
- Append to `Card_Edits.md` a section **Third pass: what it was about (2026-11-23)**: each edit, its field, old → new text, and its evidence (file and lines, or the brief's sentence); each item skipped and why.

Do not commit. Reply in under 100 words: edits made, items skipped, validator errors.
