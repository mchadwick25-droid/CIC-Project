# Place labels — PL1 record (2026-11-07)

Chunk PL1 of `Build/Ministry/Features/Church-Family-Tree/Build-Plan.md`. Each of the 300
census movements and the 62 gap stories on the map gains a `placeLabel`: a short place line
drawn only from its own `region` text.

## Method

1. **Draft (Sonnet).** Rules: only places the region text names, in its order; at most two,
   joined by " · "; " and beyond" when the text names more or reaches further; shorten by
   dropping words, never by rewording; never add a place, a country, a modern name or an
   empire; a containing region that only locates a kept place may be dropped.
2. **Mechanical check.** Every place in every label is a word-for-word substring of its region
   text, in order, and no label names more than two places. 362 of 362 passed.
3. **Independent check (Opus).** A separate reviewer saw only each region text and its label.
   361 of 362 were faithful. One fix: `joachimite-current`, region "Calabria, then Franciscan
   circles", had "Calabria · Franciscan circles"; a religious group is not a place, so it
   became "Calabria and beyond". The reviewer's record is `independent-review.json`.
4. **Kept in force.** `tools/validate-census.mjs` now fails any movement without a
   `placeLabel`, any label with more than two places, and any place not found in its own
   region text. Given `--atlas`, it applies the same rules to the gap stories. CI runs it
   that way.

## Where the labels are

- `labels.json` in this folder: the final 362 labels, by id.
- `cic-website/data/world-census.json`: `placeLabel` beside `region` on each movement.
- `cic-website/atlas-v3.html`: the same field on the map's embedded movements (292 present
  there) and on all 62 gap stories, whose only copy is the map's embedded data.
  `engine/m6/census_atlas_sync.py` now counts `placeLabel` as a synced field.

## Question for Mark's PL2 ruling

Where the region text gives an ancient or period name with the familiar one in brackets, the
label keeps the name the text gives first: 57 entries, for example "Lugdunum (Lyon) and
Vienne" became "Lugdunum · Vienne", and "Streanæshalch (Whitby)" became
"Streanæshalch · Northumbria". Both choices are faithful to the text. The alternative is to use
the bracketed familiar name wherever the text supplies one. Listed for one ruling with the
disputed borders, not changed case by case.
