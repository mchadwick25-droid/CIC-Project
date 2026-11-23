# Card edits: John Cassian (`john-cassian`)

Existing card kept word for word except as listed. `briefLength` left out (not an allowed key). Check: `tools/validate-census.mjs` on a test census with this card and the final brief shows no card error except the three missing `secondReading` verdicts, which release sets. The brief's quotations have no entry in `tools/quote_renderings.json` yet, which release also adds.

## New: quotationOriginals (one per quoted span in the brief)

1. Old: none. New: modern "So these two, the grace of God and free will, seem opposed to each other. But really they are in harmony."; printed "These two then; viz., the grace of God and free will seem opposed to each other, but really are in harmony", Gibson, Conferences XIII.11. Evidence: N211 38028-38030. No `secondReading` (21 words).
2. Old: none. New: modern "the Conferencer"; printed "Contra Collatorem" (Gibson's Prolegomena), `secondReading` "checked at card", with a note that collator is the author of the Collationes. Evidence: N211 15774-15775. The Latin title in Mommsen (MOM 42762-42764) is damaged in the scan ("collatorcm") and is not given.
3. Old: none. New: modern "The church of God finds them wholesome, but he brands them as harmful."; printed "which the church of God finds salutary, but which he brands as injurious", Gennadius 85, tr. Richardson. Evidence: N203 43669-43671. The held Latin (MOM 42882-42885) is damaged at the verb, so no original is given. No `secondReading` (13 words).
4. Old: none. New: modern "May we set the men themselves before you, embodied, as it were, in their own rules. And, what matters more, may they be speaking in Latin."; printed "may succeed in setting before you the men themselves incorporated, as it were, in their own Institutes, and what is more to the point, speaking in the Latin tongue", Conferences preface to Part I. Evidence: N211 25949-25952. No `secondReading` (28 words). Note says Institutes here means the elders' rules of life.

## New: briefReferences

Old: none. New: 14 entries, one for each place the brief draws on, with no quotation marks: Part II preface, Gibson on dates, Conference XVII ch. 30, Gennadius 62, Palladius, Institutes preface, Conference XIII chs. 3, 8 and 11, Prosper to Augustine, On the Incarnation, Prosper's book, Gennadius 85, Rule chs. 42 and 73, Cassiodorus, Part I preface. Evidence, by entry: N211 36721-36737, 15544-15552; N211 15062, 15412-15416, 15070-15071, 15544-15569; N211 42239-42249; N203 43243-43272; PAL 2640-2654; N211 16435, PET 7996-8001; N211 37572-37578, 37833-37837, 37995-37999, 38028-38030; GOLD 16932-16936, N211 15722-15726; N211 48484-48487, 48713-48718, 15600; MOM 42762-42764, N211 15774-15785, 15909-15912; N203 43669-43672; RB 6836-6847, 10409-10412, 10444-10448, RB 150, N211 16048-16058; N211 16056-16062 (Cassiodorus as Gibson quotes him), CAS 83928-83945; N211 25950-25952.

## New: sent to the card by the Outline ("Card")

5. Legacy trace added: Gregory of Tours and the monastery that kept the Rule of Cassian beside Basil's (GT-E 22152-22155; Aredius at 22104-22110). Source added: Dalton's Gregory.
6. Legacy trace added: Victor of Martyrites' recension for Africa (N211 16004-16007). No new source (Gibson is already cited).
7. Legacy trace added: the Gallic Chronicle of 452 at the year 429 (MOM 71060-71062; damaged print, sense clear, said so on the card). Source added: Mommsen, Chronica Minora I.
8. Legacy trace added: the Philokalia prints his work to Castor on the eight thoughts under Cassian the Roman (philokalia v1 6184-6190, Greek heading read by hand). Source added: Philokalia v1.
9. Uncertain entry added: the Irish Cursus Scottorum tract, an eighth-century witness by Warren's account (BANG 1581, 1622-1623, 1610). Source added: Warren's Antiphonary of Bangor, part II. Correction to the Source Sheet's I7: the tract names a companion "Honorium", not Honoratus; the card says Honorius.

## Clearly wrong

See the second pass below.

## Not found / not changed

- Not added from the Outline's "Card" list: Benedict of Aniane's concordance, Isidore and Photius (the sheet shows no clean passage, Isidore's debt and Photius's codex are not held); the bishops and monks of Provence the three parts went to (no held line cited beyond the dedications in Gibson, which would reword the Conferences entry).
- Palladius names a deacon "Cassianus" with a question mark in the print (PAL 2641); the identification with John Cassian rests on Moore's note (PAL 2661-2669). The card says the note is the editor's.

## Scan readings to add

None. The checker listed no scan readings.

## Second pass (2026-11-23)

Checker changes:
- `uncertain` entry 5 (Prosper joins the two names): applied word for word. Evidence as the checker gives: MOM 56178-56179, 56194-56197, 56423-56425.
- `sources.about`, Mommsen entry `title`: applied word for word.

Items added from the outline:
- `keyWorks`, The Conferences, `about`, appended: "; Gibson sets out the dedications, the first ten to the bishop Leontius and the brother Helladius, the next seven to Honoratus and Eucherius, and the last seven to Jovinian, Minervius, Leontius and Theodore". From Cut first 5 (the people the three parts went to). Evidence: N211 25881-25915 (Part I preface, "blessed Pope" Leontius and "holy brother Helladius"), N211 15544-15569 (Gibson's account of Parts II and III; Part III dedicated to Jovinian, Minervius, Leontius and Theodore). "Provence" is not at the cited lines, so it is not said.
- `legacy.traces`, new last entry: "The preface to the Philokalia's pieces by Cassian says they are two, on the eight thoughts and on discernment, and says Photius of Constantinople mentions them. It says the Church remembers him on the twenty-ninth of February with honors and praise." From the Outline's Leave out (Read in Greek in the East). Evidence: philokalia v1 6133-6183 (Greek read by hand: "ὁ περὶ τῶν ὀκτὼ λογισμῶν, καὶ ὁ περὶ διακρίσεως"; "Μέμνηται δὲ τούτων καὶ ὁ σοφώτατος Φώτιος"; "κατὰ τὴν κθ΄ τοῦ Φεβρουαρίου μηνὸς μνημονεύουσα, τιμαῖς τε καὶ ἐγκωμίοις καταγεραίρει").

Already held, not added again: Gregory of Tours, Victor's recension (Cut first 1 and 2), the Cursus tract, the Gallic Chronicle, "the blessed Cassian".

Skipped:
- Benedict of Aniane's concordance and Isidore: the Source Sheet records no clean passage (Aniane hits are passages and Migne's notes; Isidore's debt is not shown, only Arevalo's notes). Not held at a citable line.
- Photius's own codex: not held (Source Sheet); only the Philokalia preface's mention is carried, as that preface's claim.
- The 'Cut first 3 and 4' items are marked Leave out, not card.
