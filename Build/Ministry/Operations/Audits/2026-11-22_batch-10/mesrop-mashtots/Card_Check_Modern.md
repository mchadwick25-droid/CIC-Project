# Mesrop Mashtots: card check, the modern pass (2026-11-23)

Check pass of `roles/card.md` on `mesrop-mashtots.card.json`. Starting card: `Card.pass3.json`. Edit list: `Card_Edits.md`, **Fourth pass: no modern opinion (2026-11-23)**. Brief: `mesrop-mashtots.brief.txt` as it now stands. The checker did not write the card. Indexes count from 0. T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`; T12 = `cic/texts/langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`.

## Verdict: FIX

## What holds

- **Nothing else moved.** A JSON diff of `Card.pass3.json` and the card shows only the listed changes: `uncertain[19]` and `uncertain[20]` added, `briefReferences[3]` extended, `briefReferences[5]` added.
- **Cited lines, all re-read.** T2 3596-3597 (Sahak, "de l'an 390 jusqu'à l'an 440"), 3608-3612 (Vramshapuh, "l'an 392 jusqu'à sa mort, en 414"), 3641-3643 ("Théodose le jeune était sur le trône"); T2 13005-13018 and 14132-14135 (Moses on the Aghouank); T2 26944-26946 and 29194-29195 (Eghishe); census `world-census.json` 41218 ("The eastern Caucasus"). `uncertain[19]` matches its lines. `briefReferences[3]` and `[5]` match the brief and their lines.
- **`briefReferences`.** No entry names "early 400s", "eastern", or any other wording the brief has dropped. `briefReferences[6]` says "Greek learning barred on the Persian side". The brief now says "only Syriac learning was allowed" and "because of that ban". That is the same ban, not quoted, so it stands.
- **Quotations.** The brief quotes the same three spans in the same words. The three `quotationOriginals` are unchanged, and each `printed` is verbatim at T12 55853-55883, 55910-55912 and 55914-55916.
- **Card rules.** Keys are the census keys, no audit file is named, and spelling is American outside printed wording.

## What fails

1. `uncertain[19]` credits Langlois but does not mark his dates as modern, as the pass requires.
2. `uncertain[20]` says more than Moses's lines hold. The plain from the Araxes runs "jusqu'à la forteresse qui est appelée Hénaraguerd" (T2 13016-13017). The north-east country "près du Cyrus" is the one given to Aran (T2 13011-13013), not the Aghouank plain.
3. The brief's "a Christian people" now rests on Eghishe (Outline, Words to explain and Modern pass 2: T2 26944-26946, 29194-29195), not on the census. The card gives no reference for Eghishe, and `sources` does not list his work.
4. Older modern views are credited by name but not marked as modern, the same standard the other batch-10 checks applied.

## Changes, exact

### A. The pass's own entries

**A1. `uncertain[19]`**
- Old: `The years for the letters' time come from Langlois's notes, not from Koriun:`
- New: `The years for the letters' time are a modern editor's: they come from Langlois's notes, not from Koriun:`

**A2. `uncertain[20]`, third sentence**
- Old: `Moses of Khoren puts the Aghouank plain and its mountain region from the Araxes toward the Cyrus, in the north-east, and names the people of the mountain of the Caucasus beside the Aghouank and the Iberians.`
- New: `Moses of Khoren gives the house of Sissag the Aghouank plain and its mountain region, from the Araxes to the fortress called Hénaraguerd, and gives Aran, of that house, the great country of the north-east near the Cyrus. He also names the people of the mountain of the Caucasus beside the Aghouank and the Iberians.`
- Evidence: T2 13010-13018, 14132-14135.

**A3. `briefReferences`, new entry after `briefReferences[5]` (the Moses Aghouank entry)**
- Old: (none)
- New: `Eghishe, History of Vartan: the Aghouank among those faithful to the Gospel of Christ, and their general with the province's holy bishop.`
- Evidence: T2 26944-26946 ("des Aghouank, et tous ceux qui étaient fidèles au saint Évangile du Christ"), 29194-29195 ("le général en chef des Aghouank ... avec le saint évèque de la province").

**A4. `sources.about`, new entry after the Lazar of Pharp entry**
- Old: (none)
- New: `{"title": "History of Vartan and the War of the Armenians (Histoire de Vartan et de la guerre des Arméniens)", "author": "Eghishe", "date": null, "language": "French translation", "file": "cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt"}`
- Evidence: T2 25692-25696.

### B. Modern views named but not marked as modern

**B1. `datesNote`**
- Old: `by a note in Victor Langlois's edition`
- New: `by a note in Victor Langlois's modern edition`
- Evidence: T2 3475-3477.

**B2. `legacy.traces[0]`**
- Old: `the French supplies Sahak's name in brackets.`
- New: `Emine's modern French translation supplies Sahak's name in brackets.`
- Evidence: T2 3870-3875 ("[Sahag]").

**B3. `legacy.traces[2]`**
- Old: `Langlois writes that`
- New: `Langlois, the modern editor, writes that`
- Evidence: T2 3050.

**B4. `legacy.remembered[0]`**
- Old: `whom the editor of the Armenian text, as Langlois reports,`
- New: `whom the modern editor of the Armenian text, as Langlois reports,`
- Evidence: T2 4456-4464 ("Le savant éditeur du texte", "Moïse de Khorène, son neveu").

**B5. `uncertain[1]`**
- Old: `come from a note in Langlois's edition.`
- New: `come from a note in Langlois's modern edition.`

**B6. `uncertain[3]`**
- Old: `Langlois, following Luc Indjidji, holds`
- New: `Langlois, a modern editor, following the modern scholar Luc Indjidji, holds`

**B7. `uncertain[4]`**
- Old: `A note citing Saint-Martin, and Langlois's introduction, read Samosata`
- New: `A note citing the modern scholar Saint-Martin, and Langlois's modern introduction, read Samosata`

**B8. `uncertain[5]`**
- Old: `The identification is the bracket's, not Koriun's.`
- New: `The identification is the modern translator's bracket, not Koriun's.`
- Evidence: T2 4098-4110; the source sheet, E21, calls it the translator's bracket.

**B9. `uncertain[7]`**
- Old: `A note in Langlois's edition reports a supposition, by Emin,`
- New: `A note in Langlois's modern edition reports a supposition, by the modern scholar Emin,`
- Evidence: T2 3477-3480.

**B10. `uncertain[9]`**
- Old: `a later historian whose date is disputed`
- New: `a later historian whose date modern scholars dispute`
- Open: no held source names the scholars who dispute it. The only trace is the Library's own note (`cic/corpus-map/armenian-christianity-after-avarayr.yaml`, the Moses row). This marks the view as modern. It cannot credit it by name.

**B11. `uncertain[11]`**
- Old: `Brosset's notes take`
- New: `Brosset's modern notes take`

**B12. `uncertain[13]`**
- Old: `a note in Langlois's edition says`
- New: `a note in Langlois's modern edition says`

**B13. `uncertain[16]`**
- Old: `The notes in Langlois's edition, to Moses and to Lazar, both turn`
- New: `The modern notes in Langlois's edition, to Moses and to Lazar, both turn`

**B14. `uncertain[17]`**
- Old: `Langlois's note makes the link`
- New: `Langlois's modern note makes the link`

## Not changed, noted

- `uncertain[20]` cites "The project's entry for Caucasian Albania" as the modern placing. That entry names no scholar behind "eastern Caucasus" (census line 41218). It is the only held holder of the view, and the card marks the view as modern, so it stands.
- `legacy.remembered[3]` gives the Synaxary as "of the thirteenth century". That date rests only on the Library's file header (SYN16 line 2). It is a dating of the compiler, not a judgment of what happened, so it is not changed here.

After the fix, run `node tools/validate-census.mjs --skip-quotes` again on a scratch census.
