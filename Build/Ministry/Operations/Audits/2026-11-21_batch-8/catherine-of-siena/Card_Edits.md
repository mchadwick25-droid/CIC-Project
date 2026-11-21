# Card edits: Catherine of Siena (new card)

New card, so every field is new. Card: `catherine-of-siena.card.json`. Starting list: the Who profile card (`Who-Profiles/era6/batch2/catherine-of-siena.card.json`); each claim re-read in its file below. Short names as in `Source_Sheet.md` (LET, LIB, DIA, RAY, MIRBT, MANSI, DUR, GARD, COVEL, LEA, TER, BARD). RAY lines are damaged OCR, read for sense only.

## Fields

- **otherNames**: Benincasa, LET-ed 1261 and AAS 1926 line 160; Caterina da Siena, LIB 14325; Catharina de Senis, GARD footnote at about line 497; Katherin of Senis, GARD 481; Catharine of Sienna, COVEL 51460. (Dropped from the Who card: Catharina Senensis, not found in a held line.)
- **knownFor**: the brief's sentences 2 to 3 and 12 to 16; E1, E3, E7, E13, E14.
- **datesNote**: LET-ed 1258 and 1394-1395; RAY 211676-211679 (29 April, Sunday, Terce; Raymond at Genoa); BARD 214957; COVEL 51460-51461; LET 6802 (28 June 1376); LET-ed 1337-1339, 1345, 7167-7170; LET-ed 1228-1229; MANSI 53392-53393; DUR 98786-98788; LIB 14324-14327; LET-ed 1371-1374. This also holds the cut-first items on the Sienese copy and on setting out for home with the pope.
- **placeNote**: LET-ed 1258-1261 (Strada dell' Oca, Fontebranda); RAY 194254-194257 and 194261-194265 (the dyes; the cut-first item on her father); LET 4855-4857 (Pisa, Lucca); LET-ed 1337-1339; RAY 209831-209847 (Florence); LET-ed 1371-1374.
- **role**: LET-ed 1279-1282, 1308-1310, 1413-1415; E13.
- **keyWorks** (2): Letters, LET 5166-5168, 5210-5212, 5039, 6782-6791, 7019-7023, 7136-7137, 6448-6449 (the poison letter and the lines "swallow the bitter" and "rise like a man", from the card list, paraphrased); LET-ed 518-522. Dialogue, LIB 170-180, 1526-1530 and DIA 3200-3201 (the bridge, from the card list); LIB-ed 14391-14407; RAY 209850-209875.
- **legacy.traces**: LIB-ed 14467-14472, 14407-14412, 14414-14422, 14503-14511, 14436-14438, 14462-14465; RAY 193196-193198 (Raymond's Latin, cut-first item 5); GARD 481-504; RAY-ed 192580-192582, 192563-192566; COVEL 51460-51461.
- **legacy.remembered**: RAY 205358-205364 and 205372-205377; BARD 214581, 214593-214595; TER 686-696; Teresa's Life (`teresa-of-avila_life_lewis1904.txt`) 2257-2261, 11588-11592; LEA 29390-29392, 29419-29420; AAS 1926 lines 160-162.
- **uncertain** (13): D1 to D5 as listed in the source sheet (RAY 214144-214146; LET-ed 1228, 1343-1344, 7167; DUR 98778-98796; LIB 14342-14344; LET 4830-4831, 7063-7064; MANSI 53395-53409); Raymond as witness (RAY 200969-200972, 201022-201024, 211679; RAY-ed 192640-192641); the audience; the peace at Avignon (RAY 214067-214111; LET 6782-6791, 6859-6862); Florence 1378 (RAY 214194-214200, 209831-209847; LET-ed 1360-1363); arrival day; the Dialogue's date and ecstasy (LIB 14324-14327, 14373-14377, 14391-14402, 14448-14450; LET-ed 2184; DIA 20-24; RAY 209850-209875); her death (RAY 211676-211679; BARD 214951-214958, 214541-214547); family and habit (LET-ed 1258-1261, 1279-1282; RAY 196385-196392); dictation and writing (RAY 193177-193186; LET-ed 518-522, 1353-1354; LIB 14628-14636); the stigmata and the 1374 summons (LET-ed 1311-1315, 1323-1327); the thousand (RAY 205358-205364); not held.
- **sources**: every file the card uses. LET, LIB and DIA are ownWords; the rest are about.
- **briefReferences** (13): the brief's sentences against the lines above. No quotation marks.
- **quotationOriginals** (6, below).
- Not written: `label`; connections to other entries.

## Quoted spans

1. Q1, "To the honour of almighty God ... smell it themselves." Latin printed from MIRBT 13887-13891 (the cleaner print), awaiting second reading. **Two scan faults are resolved in the printed Latin**, so the validator will not match it until `tools/quote_scan_readings.json` has them: MIRBT line 13887 "onmipotentis" reads "omnipotentis" (confirmed by the Acta Sanctorum print, RAY 200985-200986), and the margin number "30" at the start of line 13890 is a stray mark. Under the batch 6 ruling both are allowed; the register entries are for the apply step, and I did not edit the register. Mirbt "quae", RAY "qui": noted in the entry's `uncertain`.
2. "incarnate demons." English LET 5039 (Scudder). 2 words: checked at card.
3. "I tell you: come, come, come. Do not wait for time, because time does not wait for you." English LET 5221-5222. Awaiting second reading. Italian not held.
4. "with her leading him." 4 words: checked at card. **Problem for the checker.** The modern words render Raymond's ipsa eum inducente (RAY 214144-214146), held only in a damaged scan that reads "indiicente", with no other held print (searched `cic/texts/`; no held English of the Life). Under the ruling the Latin is left out, and there is no held English translation of this sentence to print. The entry's `printed` is Scudder's editor's summary of the same claim (LET-ed 1228-1229, "Gregory, swayed by her representations, returns to Italy"), which is not Raymond's wording; the entry's `uncertain` says so. If the checker finds that print too far from the rendering, the options are to give the brief's phrase no quotation marks (a brief change, not mine) or to accept the damaged reading by a register entry.
5. "decided on your return and announced it." English LET 7063-7064. 7 words: awaiting second reading.
6. Guidini, "To hear it told ... And I am one of them." Italian LIB 14405-14407 (clean). Awaiting second reading.

## Conflicts and claims not found

- No Catherine entry exists, so no field of it can conflict.
- The tradition entry's documented story "Be a Man, Father, Arise!" was written from reference summaries (D7): its "nearly four hundred" letters and the needle in her foot are not held; the card uses neither. Its line on Gregory XI echoes LET 6448-6449; not used as a quotation.
- Not found: "Catharina Senensis" (Who card otherName); a Barberini copy of the Dialogue dated 1377 and a Florence copy ending October 1378 (Who card, `uncertain`): no held line in this folder's sheet; left out. Bernardino of Siena born in her death year: Banchi's held line breaks off at "della morte di santa" (Banchi vol. 1, line 160) and does not name her, so left out. The Bollandist note on the stigmata (AASS June, volume 5) was not reopened; its claims are not on the card.
- Scudder's date for Gregory's departure is not stated; the card gives only "September 1376" and the two Scudder lines about her own leaving (LET-ed 1345, 7168-7169), which sit awkwardly together.
- GARD names Raymond's Latin as the source of the 1519 English; Guidini and Maconi say they made Latins too. Both are on the card.
