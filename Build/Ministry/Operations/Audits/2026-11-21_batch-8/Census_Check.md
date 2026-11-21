# Batch 8: census check of the nine person entries

Checker: independent of the drafter. Prompt: `Census_Entry_Prompt.md`. Evidence: `Census_Entries.md`, each `<slug>.card.json`, `<slug>.brief.txt`, `Outline.md` (Setting), the model `cyril-and-methodius`, the era peers (`bonaventure`, `gregory-vii`, `innocent-iii`, `thomas-a-kempis`, `john-wyclif`, `martin-luther`, `john-calvin`, `ignatius-of-loyola`, `william-tyndale`, `hugo-grotius`) and each tradition entry in `cic-website/data/world-census.json`.

## Checks run on all nine

- **Keys.** All nine have the model's 33 keys, in its order, and no others.
- **Fixed fields.** `kind`, `major`, `beyondFloor`, `status`, `chip`, `glyph`, `statusWord`, `statusDescription`, `living`, `overlayCurrent`, `c2`, `entry`, `reviewStatus` equal the model's values.
- **From the tradition.** `era`, `lane`, `laneLabel`, `laneOrder`, `regions` equal the tradition entry's in every case. No date span runs past its tradition's end; no `modernCountries` record is new to the tree (Germany Q183 and Constantinople Q16869 are copied whole from existing entries).
- **atlasId.** Era 5 persons end at IV.30, era 6 at V.26, era 7 at VI.37 (highest of all `movements` and `retiredMovements` in each series: 30, 26, 37). IV.31-33, V.27-29 and VI.38-40 are on no entry, and follow in README order.
- **longDescription and card.** Each equals its `brief.txt` (final newline removed) and its `card.json`, checked by script.
- **Teasers.** Each is one sentence, place and years then who they were, in the era peers' form ("CE" in era 5 only, as `bonaventure`, `gregory-vii`, `innocent-iii`). Each says no more than the card's `knownFor` and the brief. None contradicts its tradition entry (Franciscans from 1209 and Francis's death in 1226; Bernard joining in 1113; Hus burned at Constance in 1415; Catherine pressing the popes back to Rome; councils of 1341, 1347 and 1351 for Palamas; Zurich under Zwingli from 1519; the Prayer Book of 1549 and 1552; St Joseph's, 1562).
- **Dates and places.** Each `dates`/`start`/`end`/`activeYear`/`region`/`placeLabel` is held by the card line and outline Setting line `Census_Entries.md` cites. Disputed years (Francis's birth, Aquinas's birth, Hus's birth, Palamas's birth and death, Teresa's entry) are kept out; editors' years are marked "c.".
- **Spelling.** American throughout the entry's own text, with one exception (catherine-of-siena, below). British forms that remain are in printed source text or proper names only ("amongst" in Francis's printed Quote 1; William of Tyre; The Bloody Theatre).

## Verdicts

| Entry | Verdict |
|---|---|
| francis-of-assisi | PASS |
| bernard-of-clairvaux | PASS |
| thomas-aquinas | PASS |
| jan-hus | PASS |
| catherine-of-siena | FIX |
| gregory-palamas | PASS |
| huldrych-zwingli | PASS |
| thomas-cranmer | PASS |
| teresa-of-avila | PASS |

## catherine-of-siena: FIX

Quote 1 is the project's own English rendering from Raymond's and Mirbt's Latin ("Ad honorem omnipotentis Dei", Outline.md line 64, Review.md line 81), not a printed English source, so it takes American spelling. The tree's own renderings write "honor" (`nestorius`, `tatian` card `modern`). Two fields carry "honour":

In `longDescription`:

```json
{"old": "\"To the honour of almighty God, I dare to say it.", "new": "\"To the honor of almighty God, I dare to say it."}
```

In `card.quotationOriginals[0].modern`:

```json
{"old": "To the honour of almighty God, I dare to say it.", "new": "To the honor of almighty God, I dare to say it."}
```

The same change goes into `catherine-of-siena.brief.txt` (paragraph 1) and `catherine-of-siena.card.json` (`quotationOriginals[0].modern`), so that the entry still equals both files. Nothing else in the entry changes.
