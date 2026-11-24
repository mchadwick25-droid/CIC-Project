## Batch header

- **Story:** John Chrysostom (`john-chrysostom`), kind: person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`).
- **Folder:** `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/`. **Card:** the `card` field of the entry `john-chrysostom` in `cic-website/data/world-census.json`.
- **Batch:** a fix to live texts, run as a batch of its own (Kit, Part 3): the three person reference stories brought to the kit of 2026-11-24 (Open-Gaps 406). Job: the third person reference for `kinds/person.md` (Mark: "a, three references, use Chrysostom as the third"), read by every later person writer for voice. Siblings: `epiphanius-of-salamis` (in this batch; it tells the Constantinople visit from Epiphanius's side only) and any the researcher finds on the tree, such as `palladius-of-helenopolis`.
- **Heart:** The approved heart is batch 10's, in `Outline.batch10.md` and the census entry's `why`: a preacher at Antioch and then bishop of Constantinople, who spoke plainly about money, cruelty and the poor, rebuked the powerful, was deposed and exiled, and died on the road into a second exile; his body was later brought back to Constantinople and his followers reconciled.
- **Length:** approved by Mark as it stands, 742 words (2026-11-24: "keep them as they are, approved").
- **Ruling for this batch (Mark, quoted):** "we are not pursuing perfection, just reliability, appreciation for rigor. we cant pursue loops of minor tweeks." Keep approved wording wherever it passes the kit; change only what fails it.
- **Your step: the card check pass** (the role's last section). The starting card is `Card.existing.json` in this folder.

## Role prompt (`Brief-Kit/roles/card.md`, filled)

# Card writer

You update the card for **John Chrysostom** to go with its finished brief. The existing card, `the card field of entry john-chrysostom in cic-website/data/world-census.json`, comes from earlier Library builds that were checked more than once. Keep it word for word, and make only two kinds of edit.

1. **New.** Add what the new brief brings: its quotations, each with the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. Add the references the brief draws on. For the format, see the `card` of `cyril-and-methodius` in `cic-website/data/world-census.json`. Re-read each cited line in its file.
2. **Clearly wrong.** Correct a statement only when a held source contradicts it, or when it contradicts the finished brief. Change the fewest words that put it right. A claim you cannot find support for is not wrong: leave it in place and list it as not found.

Do not reword, reorder, expand or shorten anything else. Leave connections to other entries out for now.

The card goes into the census, so it must pass `tools/validate-census.mjs`. Use only the keys it allows, and no `briefLength`. Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes. Leave out `secondReading` for a quotation of six words or more: release sets it from the second readings, never inventing one. A quotation under six words is not read blind: give it `"checked at card"`, and the card checker checks its rendering against its original and print. In card prose, put quotation marks only around a source's own words, as a cited file or the brief's quotations give them, since the census validator looks for every quoted span there. Give the brief's narration without them. The card is a live surface: name no audit file, review or ruling in it. Use American spelling, except in printed wording quoted verbatim.

Part 1 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` governs the card too, its short texts included: the card's `legacy` and `uncertain`, and the census entry's `why`, `relationsSummary` and `teaser`. None may repeat a claim the brief no longer makes, or name a thing without the explanation Part 1 requires. You do not edit the entry: list each change an entry field needs under **Entry fields** in `Card_Edits.md`, and release applies the ones the checker passes. Each story carries two reference lists: the old sources in the card's `sources`, and modern works in the entry's `modernWorks` (or a documented story's), `title` and `author` required, `year`, `publisher`, `url` and `note` as held, within the project's rights rules (`Build/worlds/_cross-world/CORPUS-USE.md`). Each modern work the outline used to clarify an old text or find one goes there, and a modern work now listed under the card's `sources` moves there word for word; list both under **Entry fields**. Whatever else the outline, review or fresh read sends to the card goes under `uncertain` or the field it belongs to. A quote whose original is held only in a damaged scan prints its English alone unless another held print confirms the reading. Check Greek by hand.

Read Part 1 of the kit and the kind kit, then the brief `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt`, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Outline.md`, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Source_Sheet.md`, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Review.md` and `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Fresh_Read.md`. Write the card to `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.card.json`, and list every edit in `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Card_Edits.md`: the old words, the new words, and the evidence (file and lines, or the brief's sentence). Do not edit the census, the existing card or the brief, and do not commit. Keep any scratch script or census copy outside the repository, in a folder for this story alone, and never run another hand's script. Reply in under 120 words: each edit in one line, and any claim not found.

## A new card

Where there is no existing card, build one with every field the other cards carry that the sources hold, in the format above. Every claim comes from the source sheet or outline at a cited line, or from the finished brief. Where the census entry already has other fields (`voices`, `legacy`, `why`, `sourcing` and the like), the card must not contradict them: list each conflict. In `Card_Edits.md`, list each field with its evidence.

## A new person's census entry

Where the person has no census entry, also write `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.entry.json`, `major: true`, told within the tradition the slate names. Follow `cyril-and-methodius` in `cic-website/data/world-census.json`: the same keys, in the same order, and no others, filled as the other person entries of that era fill them. `atlasId` is the next free one in that era's series. Dates, places and regions come only from the card and the outline's Setting. The `teaser` is one sentence in the model's form, saying no more than the card's `knownFor` and the brief. `longDescription` is the brief, final newline removed; `reviewStatus` is "AI-checked"; `card` is the card. List each field and its source in `Card_Edits.md`.

## The check pass

The card checker did not write the card. Read `CLAUDE.md` ("Trust and source fidelity"), Part 1 of the kit, the kind kit and this role, then the brief, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Outline.md`, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Review.md`, `Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/Fresh_Read.md`, the card, `Card_Edits.md`, the starting card if there is one, and the entry if there is one. Check:
1. Each edit or field is justified by its evidence, and each item the outline, review or fresh read sends to the card is on it. No modern opinion, date or identification is stated as content anywhere on the card; a modern work appears only in `modernWorks`, its `note` saying what it covers, never what it argues.
2. With a starting card, nothing else moved: every field not listed in `Card_Edits.md` is word for word.
3. A `briefReferences` entry that names something the brief no longer tells is removed.
4. The census rules above: allowed keys, one `quotationOriginals` entry per quoted span and none for a dropped one, each `printed` verbatim at its file and lines, each cited file in `sources`, no audit named, American spelling. Where the outline renders from a held original, the card carries it.
5. Each quotation marked "checked at card": its rendering against its original and print.
6. Each claim listed as not found, and anything clearly wrong left in.
7. A census entry: each field against its source, no `atlasId` already in use.

Write `Card_Check.md`: PASS, or FIX with each change exact (the field, the old text, the new text). Edit nothing. Reply in under 120 words.
