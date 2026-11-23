# Batch 10, the modern pass: the card

Story: **{NAME}**, folder `Build/Ministry/Operations/Audits/2026-11-22_batch-10/{SLUG}/`. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md` and follow it, with these specifics. Do not edit the brief, the census, any file under `tools/`, or any other folder. Write any scratch script in `/tmp/claude-0/-home-user-CIC-Project/30f7ff74-3ed4-5f83-9127-e384c2ec4ddf/scratchpad/cards/{SLUG}/`, never in the repository.

- **The starting card** is `{SLUG}.card.json` as it now stands. First copy it, unchanged, to `Card.pass3.json`: that copy is the starting card and is never edited. Then make every edit below in `{SLUG}.card.json` itself.
- **What changed:** read `{SLUG}.brief.txt`, compare it with `{SLUG}.brief.v4.txt` (`diff`), and read `Outline.md`'s **Modern pass** section (and any fresh-read correction after it), `Modern_Pass.md`, `Fresh_Read_Modern.md` and `Fresh_Read_Modern_Applied.md`.
- **Edits to make:**
  1. Each modern view the pass took out of the story ("to the card"): put it in `uncertain` (or the field it belongs to), credited to its modern source by name and marked as a modern judgment, with no more than its cited lines hold, which you re-read.
  2. Each `briefReferences` entry naming or quoting wording the brief no longer has: trim or remove it. Each new old source the brief now rests on: add its reference, and its file to `sources` if not there.
  3. Quotations: one `quotationOriginals` entry per quoted span in the brief now; none for a span it no longer quotes. A span whose words did not change keeps its entry word for word.
- Keep every other field word for word. American spelling outside printed wording. No audit file named.
- Run `node tools/validate-census.mjs --skip-quotes` against a scratch copy of `cic-website/data/world-census.json` (in your scratch folder) with this card and this brief in place, never the real census, and report its errors for this entry.
- Append to `Card_Edits.md` a section **Fourth pass: no modern opinion (2026-11-23)**: each edit, its field, old → new, and its evidence.

Do not commit. Reply in under 100 words.
