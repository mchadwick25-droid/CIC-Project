# Alopen — Card edits 2

Card: `alopen.card.json` (overwrites the first batch card), built from the census's current `card` object for `alopen` in `cic-website/data/world-census.json`. Brief: `alopen.brief.txt` (rewritten, final). Every field not listed below is word for word the census card. No `briefLength` (the census does not accept it). Line numbers are the files' own in `cic/texts/`. MAL = `malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt`; LEGGE = `legge_nestorian-monument-of-hsi-an-fu_trubner1888.txt`; YULE = `marco-polo_book-of-ser-marco-polo-v2_yule-cordier1903.txt`; BUDGE = `yahballaha-sauma_monks-of-kublai-khan_budge1928.txt`.

## New

1. **`quotationOriginals`, entry removed.** Old: the clouds-and-winds entry ("Watching the blue clouds, he carried the true sacred books. …", MAL 13688–13689). Reason: the new brief no longer quotes it (dropped by the project lead, 2026-11-18; Outline.md, Quotes).
2. **`quotationOriginals`, entry added.** Modern: "It helps every creature, and it does people good. Let it spread freely through the empire." (the brief's one quoted span, exact). Printed: "(the system) is helpful to (all) creatures, and profitable for men : — let it have free course throughout the empire", re-read at LEGGE 1252–1254, verbatim. Work: the Xi'an stele (781), the decree of 638, tr. James Legge (1888). `secondReading`: "same" (Second_Readings_3.md, S3-01, SAME; Second_Reading_Key_3.md S3-01 = alopen, LEGGE 1252–1254, no line correction). No original-language fields: the outline renders from Legge's English, and the Chinese is not held. No `uncertain`: neither the outline nor the second reading notes a doubt on this span.
3. **`briefReferences`, replaced** (six plain-text entries, no quotation marks):
   - Legge's stele, parts II.7–11 (LEGGE 1008–1012, 1227–1257, 1477, 1633–1647, 1863–1871): Taizong, the arrival in 635, the minister sent to receive him, the translation in the Library, the orders to spread it, the decree of 638, the monastery for twenty-one priests, Gaozong's monasteries in a hundred cities, the opposition of 698–699 and 712, Lo-han and Chi-lieh.
   - Wylie's stele (MAL 13687–13695, 13738–13751, 14141–14142): arrival, translation, orders, opposition of 699 and 713, Lohan and Kie-leih, the stone erected in 781.
   - Legge's lecture (LEGGE 3662–3710, 3876–3877, 4251–4253, 4346–4350): the finding in 1625, the copy sent to the Jesuits and their circulating it as proof, the stone's account of the faith's first entrance, the slight traces after 781, the edict of 845.
   - Yule and Cordier (YULE 2908–2916, 2929–2932): Chang-an; the stone found by workmen in 1625, the cross at its top; its discovery disclosing the churches' forgotten existence.
   - Budge, Appendix B, after Saeki (BUDGE 5174–5177): the minister bringing him to the palace.
   - World census: his tradition.
   Removed from the old references: the clouds phrase in quotation marks (no longer in the brief).

## Clearly wrong

None. Checked against the new brief and held sources:
- `knownFor` "A decree of 638 ordered a monastery built": Wylie puts the building inside the decree (MAL 13709–13711); Legge has the officers build it after (LEGGE 1256–1257). The brief's "Officials built a monastery" does not contradict it.
- `legacy.traces` first item (churches in every province, every city full of churches): Wylie's rendering, attributed to the stele (MAL 13739–13744); the brief's "monasteries filled a hundred cities" follows Legge (LEGGE 1636–1640). A translators' difference, not a contradiction.
- `legacy.traces` second item (699, 713, a later emperor restoring its buildings): MAL 13744–13757.
- `legacy.traces` third item (845 edict): matches the brief's "more than three thousand foreign teachers, Christians and others" (LEGGE 4346–4350).

## Not found

None.

## After Mark's ruling on the stone image (2026-11-18, coordinator)

- `quotationOriginals`: the clouds-and-winds entry is restored word for word from the census card as it stood before this rework (Wylie in Malech 13688-13689, blind second reading "same", `Second_Readings.md`). The brief quotes it again as Quote 3.
- `briefReferences`: one line added for it.
