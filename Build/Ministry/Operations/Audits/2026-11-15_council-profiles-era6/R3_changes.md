# Round 3 changes: era 6 council profiles (2026-11-15)

## Part A — Council of Constance 1414

Both minor points were applied as the reviewer worded them, under Mark's standing cap ruling of 2026-11-14 for minor round 3 fixes. One targeted check of only these strings by a fresh Opus agent is still to run.

- **A3-M1.** `records.json`, `council-of-constance-1414`, `absent_details` "The burning of Wyclif's bones as carried out": the list of later writers is now "Among them are ...", and Crespin is added. Checked: CRESPIN1 (`crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt`) l.19221-19225, "il fut déterré par le commandement du Pape, fes oz furent bruflez".
- **A3-M2.** Entry `decided[12]`, first sentence, now: "At the last session, the acts say, the words 'Lords, go in peace' came after the Mass and the litanies." (MANSI27 l.129231-129233, "Qua finita, & litaniis cum solitis orationibus finitis & peractis".)

## Part B — Council of Basel–Ferrara–Florence 1431

All four were applied as the reviewer worded them, under Mark's cap ruling (2026-11-15, "Fix + one check (Recommended)"). One targeted check of only these strings by a fresh Opus agent is still to run.

- **B3-B1.** Entry `uncertain`, "Who sent the Ethiopians": the three Ludolf sentences are now "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent in 1439. The Jesuit history of Tellez, in English, also says Zara Yaqob sent Ethiopians to Eugenius. In his Commentarius of 1691, Ludolf denies that Zara Yaqob joined Rome at the council. The Jesuits themselves, he says, show the king stood apart from the Roman church."
  - Entry `record`, Ludolf item: witness "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691) and his History in English (1682), with a Latin version of the oration of the Portuguese patriarch Alphonsus Mendez"; note "Ludolf takes the embassy of 1439 as Zara Yaqob's, but says the king stood apart from the Roman church. The oration, in his Latin, says the emperor and the metropolitan sent the envoys."
  - Entry `sources.writtenLater`: added "A New History of Ethiopia" (Hiob Ludolf, made English by J. P.; `cic/texts/ludolf_new-history-of-ethiopia_jp1682.txt`) and "The Travels of the Jesuits in Ethiopia" (Balthazar Tellez (the title page's attribution; the work is credited to Manuel de Almeida), English translation anonymous; `cic/texts/telles_travels-of-the-jesuits-in-ethiopia_1710.txt`).
  - Records, Ludolf claim: "Ludolf's Commentarius denies that Zara Yaqob joined Rome at the council of Florence. The Jesuit fathers themselves, he says, show the king stood apart from the Roman church" (LUD l.52403-52413; LUD l.52431-52444; later narrative, Contested).
  - Records, added: "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent to Eugenius IV in 1439, toward the end of the council. The Ethiopian Gregory, it says, knew of it only from a painting at Rome" (`ludolf_new-history-of-ethiopia_jp1682.txt l.19489-19496`; later narrative, Contested).
  - Records, added: "Tellez's Jesuit history, in English, says Zara Yaqob wished to bring his empire to the Catholic faith and sent some of his Abyssinians to Eugenius IV" (`telles_travels-of-the-jesuits-in-ethiopia_1710.txt l.6272-6295`; later narrative, Contested).
  - Contested claim "Who sent the Ethiopian envoys": after the Perruchon side, "Zara Yaqob, in 1439, toward the council's end, beyond doubt: Ludolf's History, English of 1682 (ludolf_new-history-of-ethiopia_jp1682.txt l.19489-19496). Zara Yaqob: Tellez, in English (telles_travels-of-the-jesuits-in-ethiopia_1710.txt l.6272-6295)." The Ludolf side is now "Zara Yaqob did not join Rome at the council and stood apart from it: Ludolf's Commentarius (ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt l.52403-52413; ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt l.52431-52444)."
  - `absent_details`, "An Ethiopian-side witness", second sentence now: "Ludolf's Commentarius (1691) and his History in English (1682) were read in context. So were Tellez, Almeida and Mendez, with Beccari's introduction and Innocent X's brief. None is an Ethiopian text of the time."
- **B3-S1.** Records claim "Pope Innocent X's brief of 30 October 1645 ...": `witness_kind` is now `"later narrative"`. Text, witness and confidence unchanged.
- **B3-M1.** Entry `uncertain`: "In Almeida's Portuguese of it, the emperor and the patriarch of that day sent them."
- **B3-M2.** Entry `uncertain`: "Almeida's history names no sender: some Ethiopians, it says, came with the Armenians as the council ended."

Records key now holds 131 claims, 21 contested claims and 12 absent details. Both JSON files parse. No entry sentence is over 25 words, except the reviewer's worded `record` witness label for Ludolf (26 words, a title line, kept as worded). B3-B1 was confirmed against its source before reporting: LUDH (`ludolf_new-history-of-ethiopia_jp1682.txt`) l.19491-19496, "Nor-is there any doubr made of the Embassy | Which Zera-Jacob sent: ro Eugenius the Fourth, in the. year 1439."
