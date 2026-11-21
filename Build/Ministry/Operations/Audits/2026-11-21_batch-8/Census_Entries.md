# Batch 8: census entries for the nine new people

Prompt: `Census_Entry_Prompt.md`. Each entry is at `<slug>/<slug>.entry.json` in this folder. The census file is not touched.

## What every entry shares

- **Keys and order.** The 33 keys of `cyril-and-methodius` (`cic-website/data/world-census.json`, line 43100), in its order, and no others. Peer entries carry more keys (`informalName`, `sourcing`, `floorNote`, `relationsSummary`, `why`, `voices`, `legacy`, `documentedStories`); none is added.
- **`id`** = the slug (README, "The thirteen and their jobs"). **`kind`** "person", **`major`** true (prompt; Decision-Log, "Batch 8: the slate approved", 2026-11-21, item 1).
- **`toldWithin`**: the tradition the README names for each.
- **`era`, `lane`, `laneLabel`, `laneOrder`, `regions`**: copied from the tradition entry (census lines below).
- **`beyondFloor`** false, **`status`** "Within Another World (A5)", **`chip`** "exc", **`glyph`** "a5", **`statusWord`**, **`statusDescription`**, **`living`** false, **`overlayCurrent`** false, **`c2`** null, **`entry`** null: as the model has them. Every peer below has the same values.
- **`atlasId`**: the next free numbers after the highest person id of each era. Era 5 persons end at IV.30 (`bonaventure`), era 6 at V.26 (`john-wyclif`), era 7 at VI.37 (`hugo-grotius`). IV.31 to IV.33, V.27 to V.29 and VI.38 to VI.40 are on no entry in `movements` or `retiredMovements`. They are assigned in README order.
- **`dates`, `start`, `end`**: an active span where the card's `datesNote` gives one, as the model (863, the arrival in Moravia, to 885) and the era peers do (`bonaventure` 1257-1274, `martin-luther` 1517-1546, `john-calvin` 1536-1564, `william-tyndale` c. 1525-1536). "c." marks a year that is an editor's reckoning, as in `john-wyclif`.
- **`activeYear`**: the start of the span, as the model, `martin-luther`, `john-calvin` and `william-tyndale` have it, except where noted.
- **`modernCountries`**: only place records already on the tree, copied whole. No Wikidata id is new. Places with no record on the tree (Assisi, Clairvaux, Naples, Cologne, Prague, Constance, Siena, Zurich, Ávila, Oxford) are not given ids; the country-level record is used where one exists. The model itself has `[]`, as `thomas-a-kempis` does; the prompt asks the ids to follow the tradition entry and other entries, so the tradition's records are used.
- **`name`**: the tree's spelling (Decision-Log, "Batch 8: the slate approved", item 2, for Huldrych Zwingli and Teresa of Ávila; the README for the rest). **`shortName`**: the surname for people known by one (`Luther`, `Calvin`, `Wyclif`, `Tyndale`), the first name for people named "of" a place (`Ignatius` for Ignatius of Loyola).
- **`teaser`**: one sentence, "Place, years: who they were", from the card's `knownFor` and the brief. The model's own teaser does not take this form: it is its card's `knownFor`, two sentences, with no place-and-years opening. The form the prompt describes is the era peers': era 5 adds "CE" (`bonaventure`, `gregory-vii`, `innocent-iii`); eras 6 and 7 do not (`john-wyclif`, `thomas-a-kempis`, `martin-luther`, `john-calvin`). The peers' colon (`bonaventure`) keeps it to one sentence.
- **`longDescription`** = `<slug>.brief.txt` with its final newline removed; checked equal by script. **`reviewStatus`** "AI-checked". **`card`** = `<slug>.card.json`, unchanged; checked equal by script.

Tradition entries in `cic-website/data/world-census.json` (line of `"id"`): `the-franciscan-movement` 45780, `cistercian-monasticism` 45327, `the-dominican-order` 45965, `the-hussite-and-bohemian-brethren-movement` 49788, `latin-papal-church-avignon-to-lateran-v` 50952, `hesychasm-and-the-palamite-synthesis` 49431, `the-reformed-cities-zurich-and-geneva` 52251, `the-english-reformation-and-elizabethan-settleme` 52674, `carmelite-reform-and-spanish-mystics` 56983. Peers: `bonaventure` 87323, `gregory-vii` 86796, `innocent-iii` 86850, `thomas-a-kempis` 83604, `john-wyclif` 83921, `martin-luther` 84243, `john-calvin` 84567, `ignatius-of-loyola` 84837, `william-tyndale` 83424.

## francis-of-assisi

- `atlasId` IV.31. `era` 5, lane 5 Latin West & Catholicism, `regions` ["Mediterranean"]: tradition.
- `name` "Francis of Assisi", `shortName` "Francis".
- `dates` "c. 1205-1226", `start` 1205, `end` 1226: card line 7 (Howell's table puts his turn from the world in 1204 to 1206; died October 1226); `Outline.md` line 23 ("say ... 'about 1205'"). The outline's line 27 suggests the lifetime "about 1182–1226"; the prompt's active-span rule is followed instead, since 1182 is an editor's table.
- `activeYear` 1209: `Outline.md` line 27 (1209, the Rule's approval, or 1223). Not the span's start, because the outline names it and the tradition begins in 1209. 1209 is Robinson's year; Howell gives 1210 (card line 7).
- `region` "Assisi, Italy", `placeLabel` "Assisi": card line 8; `Outline.md` lines 24 and 27 ("place Assisi, Italy").
- `modernCountries`: the tradition's Italy record. Assisi has no record on the tree.
- `teaser` "Assisi, c. 1205 to 1226 CE: a trader's son who gave up his family's wealth, served the lepers, and founded the Friars Minor, brothers who were to own nothing.": card line 6; brief paragraph 3.

## bernard-of-clairvaux

- `atlasId` IV.32. `era` 5, lane 5, `regions` ["Mediterranean"]: tradition.
- `name` "Bernard of Clairvaux", `shortName` "Bernard".
- `dates` "1113-1153", `start` 1113, `activeYear` 1113: card line 7 (entered Cîteaux in 1113; died 18 August 1153); `Outline.md` line 23.
- `region` "Cîteaux and Clairvaux, eastern France", `placeLabel` "Cîteaux · Clairvaux": card line 8; `Outline.md` line 24 ("Today: eastern France (Burgundy and Champagne)").
- `modernCountries`: the tradition's France/Burgundy record (Fontaines and Cîteaux are in Burgundy, card line 8). Clairvaux has no record on the tree.
- `teaser` "Cîteaux and Clairvaux, 1113 to 1153 CE: a young Burgundian noble who became a monk with his brothers and, as abbot of Clairvaux, was asked for his word by popes and kings.": card line 6 ("made popes and kings ask his word"); brief paragraphs 1 to 3.

## thomas-aquinas

- `atlasId` IV.33. `era` 5, lane 5, `regions` ["Mediterranean", "North Europe"]: tradition.
- `name` "Thomas Aquinas", `shortName` "Aquinas".
- `dates` "c. 1243-1274", `start` 1243, `activeYear` 1243, `end` 1274: card line 8 (entry into the Dominicans in 1243 by the Bollandists, an editors' reckoning, hence "c."; death 7 March 1274 by Tocco). The outline (line 17) gives no year for his joining; the year is the card's.
- `region` "Naples, Cologne and Paris", `placeLabel` "Naples · Paris and beyond" (the form of `bonaventure`'s label): card line 9; `Outline.md` line 18.
- `modernCountries`: Italy (as `bonaventure`), Germany (country record of `german-pietism-spener-francke-halle` and others), France/Paris (tradition). Naples and Cologne have no record on the tree.
- `teaser` "Naples and Paris, c. 1243 to 1274 CE: a Dominican friar and master of theology whose Summa of Theology, a summary of the whole faith, sets out the case against each point and then answers it.": card line 7; brief paragraph 2. It keeps the researcher's essence, not the slate's (Decision-Log, "Batch 8 hearts approved", item 6).

## jan-hus

- `atlasId` V.27. `era` 6, lane 5, `regions` ["North Europe"]: tradition.
- `name` "Jan Hus", `shortName` "Hus".
- `dates` "1402-1415", `start` 1402, `activeYear` 1402, `end` 1415: card line 9 (preacher at the Bethlehem Chapel from 1402; died 6 July 1415); `Outline.md` line 26. His birth year is disputed (1369, 1373, 1373-75) and is not used.
- `region` "Prague, Bohemia, and Constance", `placeLabel` "Prague · Constance": card line 10; `Outline.md` line 27.
- `modernCountries`: the tradition's Czech Republic/Bohemia record, and the Germany country record for Constance. Prague and Constance have no record on the tree.
- `teaser` "Prague and Constance, 1402 to 1415: a priest and master of Prague's university who preached in Czech, would not condemn John Wyclif, and was burned at Constance.": card line 8; brief paragraph 2.

## catherine-of-siena

- `atlasId` V.28. `era` 6, lane 5, `regions` ["Mediterranean"]: tradition.
- `name` "Catherine of Siena", `shortName` "Catherine".
- `dates` "1347-1380", `start` 1347, `end` 1380: card line 10 (Scudder's chronology); `Outline.md` line 24. A lifetime: the held sources give no start for her public life, only events from 1375 on.
- `activeYear` 1376: card line 10 (Avignon, June to September 1376), the heart of the story. Not the span's start, which is her birth.
- `region` "Siena, Avignon and Rome", `placeLabel` "Siena · Avignon and beyond": card line 11; `Outline.md` line 25.
- `modernCountries`: the tradition's Avignon and Rome records. Siena has no record on the tree.
- `teaser` "Siena, Avignon and Rome, 1347 to 1380: a dyer's daughter who joined no convent, dictated letters to popes, cities and rulers, and pressed the pope to take his court back from Avignon to Rome.": card line 9; brief paragraph 2.

## gregory-palamas

- `atlasId` V.29. `era` 6, lane 3 Greek East & Orthodoxy, `regions` ["Asia Minor", "Mediterranean"]: tradition (the same regions as `athonite-and-comnenian-byzantine-monasticism`, which also holds Constantinople).
- `name` "Gregory Palamas", `shortName` "Palamas".
- `dates` "1341-1351", `start` 1341, `activeYear` 1341, `end` 1351: card line 8 (the councils of 1341, 1347 and 1351); `Outline.md` line 22. No early witness gives his birth or death year (card line 8): the editor's 1359 and 1362 are not used. The span is the councils', not his whole public life, and the entry cannot say more.
- `region` "Constantinople, Athos, Thessalonica", `placeLabel` "Athos · Thessalonica" (the tradition's label): card line 9; `Outline.md` line 23.
- `modernCountries`: the tradition's Athos and Thessalonica records, and the Constantinople record used across the tree (for example `agathias`).
- `teaser` "Athos, Thessalonica and Constantinople, 1341 to 1351: a monk of Mount Athos, later archbishop of Thessalonica, who defended the monks of silent prayer and was upheld by three councils.": card line 7; brief paragraphs 2, 7 and 11.

## huldrych-zwingli

- `atlasId` VI.38. `era` 7, lane 6 Protestant & Evangelical, `regions` ["North Europe"]: tradition.
- `name` "Huldrych Zwingli" (Decision-Log, "Batch 8: the slate approved", item 2), `shortName` "Zwingli".
- `dates` "1519-1531", `start` 1519, `activeYear` 1519, `end` 1531: card line 8 (admitted people's priest 1 January 1519; died 11 October 1531); `Outline.md` line 24.
- `region` "Zurich", `placeLabel` "Zurich": card line 9; `Outline.md` line 25.
- `modernCountries`: the tradition's Switzerland/Swiss lands record. Zurich has no record on the tree.
- `teaser` "Zurich, 1519 to 1531: the people's priest of the Great Minster who preached the Bible book by book, defended his preaching before the city council, and died with Zurich's army at Kappel.": card line 7; brief paragraph 3.

## thomas-cranmer

- `atlasId` VI.39. `era` 7, lane 6, `regions` ["North Europe"]: tradition.
- `name` "Thomas Cranmer", `shortName` "Cranmer".
- `dates` "1533-1556", `start` 1533, `activeYear` 1533, `end` 1556: card line 7 (consecrated archbishop 30 March 1533; burned 21 March 1556); `Outline.md` line 26.
- `region` "Canterbury, Lambeth and Oxford, England", `placeLabel` "England" (the tradition's label, as `john-wyclif` and `william-tyndale` use England): card line 8; `Outline.md` lines 27 and 28 ("Region for the entry: England").
- `modernCountries`: the tradition's United Kingdom/England record; `Outline.md` line 27.
- `teaser` "Canterbury and Oxford, 1533 to 1556: an archbishop of Canterbury who led the making of the English Book of Common Prayer and, under Queen Mary, was burned at Oxford.": card line 6; brief paragraphs 1 and 2.

## teresa-of-avila

- `atlasId` VI.40. `era` 7, lane 5 Latin West & Catholicism, `regions` ["Mediterranean"]: tradition.
- `name` "Teresa of Ávila" (Decision-Log, "Batch 8: the slate approved", item 2), `shortName` "Teresa".
- `dates` "1562-1582", `start` 1562, `activeYear` 1562, `end` 1582: card line 7 (St. Joseph's founded 24 August 1562; died 4 October 1582); `Outline.md` line 22. The founding opens the span, as it opens the tradition (1562). Her entry into the convent is disputed (1533 or 1535) and is not used.
- `region` "Ávila, Castile", `placeLabel` "Ávila and beyond": card line 8; `Outline.md` line 23.
- `modernCountries`: the tradition's Spain/Castile record (Ávila, Toledo and Alba de Tormes are in Castile, `Outline.md` line 23). Ávila has no record on the tree.
- `teaser` "Ávila, 1562 to 1582: a Carmelite nun who founded a small, poor house of nuns living by the order's old rule, then many more, and pictured the soul as a castle of many rooms.": card line 6; brief paragraph 2.

## What the held record cannot fill

- Exact place ids for the towns named above: none on the tree, so none given.
- Palamas's birth and death years, Hus's birth year, and the year of Aquinas's master's degree: disputed or not held, so not in `dates`.
- Still open from the hearts ruling (item 4): the tradition entry's account of how Teresa's Life reached the Inquisition goes to the census pass. That is the tradition entry, not hers, and is not touched here.
