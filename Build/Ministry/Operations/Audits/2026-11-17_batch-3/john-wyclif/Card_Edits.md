# Card edits: John Wyclif

No statement on the card corrected. Every field of `john-wyclif.original.card.json` is kept word for word, except `briefLength` and the two sources added below.

## New

1. **briefLength.** Old: "about 2 minutes 30 seconds". New: "about 2 minutes 50 seconds". Evidence: `john-wyclif.brief.txt` is 423 words (`wc -w`), at the writer's rate of about 150 words a minute (`Brief-Kit/roles/writer.md` line 8), which is 2 minutes 49 seconds.
2. **sources.about, added.** Peter of Mladoňovice's account in Palacký's *Documenta Mag. Joannis Hus* (1869), `cic/texts/palacky_documenta-mag-joannis-hus-lat-ces_1869.txt`. Evidence: the file the quotation cites; Hus's hearing of 7 June 1415 at lines 15240-15250 (page heads "De M. J. Hus audientia die 7 Junii", 15185 and 15282).
3. **sources.about, added.** Raynaldus, *Annales ecclesiastici* vol. 28, ed. Theiner (1874), `cic/texts/raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt`. Evidence: the brief's "Pope Martin V later ordered them burned"; Martin V to the bishop of Lincoln, lines 7971-8025 ("facias exhumari ... et igne publice concremari", 8013-8015; "Dat. Romae apud SS. Apostolos V id. Decembris, anno xi", 8018-8019).
4. **briefReferences, added** (none before). Sixteen entries, one per source the brief draws on, each re-read at the outline's lines: fasciculi 11579-11585, 11406-11408, 11450-11457, 11669-11684, 1635-1637, 2694-2706, 2743-2755, 27423-27433; lechler 694-700; wycliffite-bible 979-981, 1025-1031, 2407-2420; pollard 840-845, 7210-7220; matthew 35791-35795; knighton 16932-16934, 16948-16969; schaff 1514-1516; mansi t.27 65527-65560, 132795-132800; raynaldus 7971-8025; palacky 15240-15250; census tradition `lollardy`.
5. **quotationOriginals, added** (none before). The brief's one quotation, Hus at Constance. Modern words exactly as the brief has them. Printed: "Nescio, ubi est anima ipsius Joan. W.; spero, quod sit salvatus et timeo, ne sit damnatus; vellem tamen in spe, quod anima mea esset ibi, ubi est anima Joannis W.", palacky 15246-15249, re-read in the file ("dam- / natus" joined at the line end). Second reading: "minor", from `Outline_Check.md` line 11, whose independent rendering keeps "John W." where the brief gives the full name; the passage names him "Joannis Wiclef" just before (15242-15243). The note also records that Hus says he first spoke these words twelve years earlier (15243-15245).

## Left alone

- legacy.traces: "Jan Hus of Prague, in a sermon of probably 1408, hoped his soul would be where Wyclif's soul rests." Not wrong. Workman and Pope give "probably in June 1408" (`cic/texts/hus_letters_workman-pope1904.txt` 4510-4512). Mladoňovice's record has Hus date his first saying of the words twelve years before 1415 (palacky 15243-15245), but the card credits the 1408 date to the editors, and the brief gives no year.
- uncertain, the bones: the entry gives Constance's order and Foxe's account, and does not name Martin V's 1427 order that the brief now tells. Nothing in it is contradicted; only the source was added (edit 3).
- The other brief paraphrases in indirect speech (the letter to Urban, Knighton's pearl, Thorpe) carry no quotation marks, so they have no quotationOriginals entry.

## Not found

None. Every claim checked against the brief was supported in the held files.
