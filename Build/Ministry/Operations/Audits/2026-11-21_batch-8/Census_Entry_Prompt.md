# Batch 8: census person entries for the nine new people

The nine new people (`README.md` in `Build/Ministry/Operations/Audits/2026-11-21_batch-8/`: francis-of-assisi, bernard-of-clairvaux, thomas-aquinas, jan-hus, catherine-of-siena, gregory-palamas, huldrych-zwingli, thomas-cranmer, teresa-of-avila) have no census entry. Each gets one, `major: true`, under the tradition the README names (Decision-Log, "Batch 8: the slate approved", 2026-11-21).

The model is `cyril-and-methodius` in `cic-website/data/world-census.json`, added in 2026-11-19 (Decision-Log, "Cyril and Methodius get one person entry"): the same keys, in the same order, and no others. Read it, and two other person entries of the same era as each new person (for example `bonaventure`, `john-wyclif`, `martin-luther`), to see how each field is filled.

For each of the nine, write the entry to `Build/Ministry/Operations/Audits/2026-11-21_batch-8/<slug>/<slug>.entry.json`:
- `id` = the slug; `kind` "person"; `toldWithin` = the README's tradition; `major` true; `era` the tradition's era.
- `name`, `shortName`: the tree's spelling (Huldrych Zwingli, Teresa of Ávila).
- `atlasId`: the next free id in the series the other person entries of that era use; check no entry already has it.
- `dates`, `start`, `end`, `activeYear`, `region`, `placeLabel`, `modernCountries`, `regions`: from the card's `datesNote` and `placeNote` and the outline's Setting, only what those hold; where the held sources give an active span rather than a lifetime, use it, as the model does. `modernCountries` ids and `regions` names follow the tradition entry and other entries on the tree.
- `lane`, `laneLabel`, `laneOrder`, `beyondFloor`, `status`, `chip`, `glyph`, `statusWord`, `statusDescription`, `living`, `overlayCurrent`, `c2`, `entry`: as the model and other person entries told within another tradition have them.
- `teaser`: one sentence in the form the model uses (place, years, then who they were), from the card's `knownFor` and the brief, saying no more than they do.
- `longDescription` = `<slug>.brief.txt` (final newline removed); `reviewStatus` "AI-checked"; `card` = `<slug>.card.json`.

Write `Census_Entries.md` in the batch folder: for each entry, each field and where its value came from (file and line, or the entry it follows). Never invent; where a field cannot be filled from the held record, say so. Edit nothing else, do not touch the census file, use no scratch file, and do not commit. Reply in under 150 words.
