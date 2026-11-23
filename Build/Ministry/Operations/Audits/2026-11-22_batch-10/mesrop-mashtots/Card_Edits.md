# Card edits: Mesrop Mashtots

Card written to `mesrop-mashtots.card.json`. T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`; T12 = `cic/texts/langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`.

## Corrections (clearly wrong)

1. `legacy.traces[0]`
   - Old: "...to Edessa and Constantinople."
   - New: "...to Edessa, and from there to Constantinople."
   - Evidence: T2 3805-3830 (sent to Edessa; "Puis ils passèrent dans le pays des Grecs, à Byzance"); the brief ("sent pupils to Edessa... from there they went to Constantinople").
2. `legacy.remembered[0]`
   - Old: "whom Langlois takes for Mesrop's nephew and pupil"
   - New: "whom the editor of the Armenian text, as Langlois reports, takes for Mesrop's nephew and pupil"
   - Evidence: T2 4455-4465 ("Le savant éditeur du texte... Il ajoute que, parmi les disciples de Mesrob, il n'y a guère que Moïse de Khorène, son neveu"). The view is the Armenian editor's, which Langlois reports; no Langlois line takes it as his own (grep of T2 for neveu/disciple de Mesrob).
3. `uncertain[6]` (the Georgian and Aghouank letters)
   - Old: "...rests on Koriun here."
   - New: "...rests on Koriun here and, later, on Moses of Khoren."
   - Evidence: T2 23913-23933 (Moses: Mesrob composed an alphabet for the Iberians; created the Aghouank letters). The card holds Moses, so "Koriun" alone is contradicted by a held source.

## New: quotations (`quotationOriginals`, three entries, one per quoted span in the brief)

All three print from T12, the cleaner scan of the same print. T2 has scan faults in each ("Anssitât", "c'eÀt été"). Original Armenian not held. No `secondReading` on any entry (all are six words or more).

- Vision: lines 55853-55883. T2 3590-3594, 3620-3621 agrees.
- Tablets: lines 55910-55912. T2 3647-3648 agrees.
- Children: lines 55914-55916. T2 3651-3653 agrees.

## New: sources (`sources.about`, four entries added)

T12 (second scan of Koriun's Life, the file the quotations print from); Armenian Synaxary of Ter Israel, Navasard (the chronicle-of-seert file, PO 5); the same Synaxary, Tré (PO 16); Georgian chronicle with Brosset's notes (KART).

## New: from the outline's "to the card" and "for the card" lists, and from the brief

- `legacy.traces`
  - Lazar: Syriac services the people could not follow (T2 36232-36240); translating given to Sahak; schools, copyists, crowded churches (T2 36473-36496).
  - Moses: Sahak and Mesrop sent him to Alexandria (T2 24738-24740).
  - Koriun: Hemayak and Vahan carry the body to Oshakan, and Vahan builds a church three months later (T2 4262-4312).
- `legacy.remembered`
  - Koriun: learned in civil and military affairs, liked by great and small (T2 3446-3450); lived in caves on herbs, coming down when needed (T2 3954-4011).
  - Synaxary: feast of the Armenian Translators, 25 November (PO 16 file line 6239); Isaac (Sahak) made the letters with the vardapet Mesrob (PO 5 file lines 28862-28866).
- `uncertain`
  - Moses's harder welcome on the Roman side, and his date disputed (T2 24206-24213, 24315-24323; census note on Moses's date).
  - The Borborite punishments in the passive, Armenian not held, and Moses's order for punishment (T2 3779-3787, 24418-24424).
  - The Georgian chronicle's rival claim for Pharnavaz and Brosset's notes (KART 2224-2230, 2263, 7036-7040; the file's header warns the scan is a poor second witness, so nothing is quoted).
  - Who translated: Koriun, Lazar, the Synaxary (T2 3634-3641, 3865-3877, 36473-36488; PO 16 file lines 6297-6301).
  - Mesrop and the see after Sahak (T2 4272-4276 editor's note; T2 25374-25392 Moses).
  - The three-way quarrel over his burial (T2 25356-25370).
- `briefReferences`: fourteen entries, no quotation marks.

## Not added

The two Julian equivalents of the death day (already covered by the two death dates in the card), the full texts of Moses's letters, the demons of Koghten, and Moses's Edessa journey were left out.

## Claims not found

None. Every existing claim was checked and found supported except the three corrected above.

## Open item

The validator reports `secondReading` missing on all three entries, as expected (release sets it). The vision quotation's French is broken by a page of footnotes at T12 55858-55882; the validator fails on `printed` until `tools/quote_scan_readings.json` lists that range as a footnote drop. Tested on a scratch copy: with the drop listed, only the `secondReading` errors remain.
