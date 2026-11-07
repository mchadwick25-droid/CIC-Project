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

## Familiar names (Mark, 2026-11-07: "use the familiar names")

Where the region text gives two names for one place, the label shows the one a general reader
knows. Of the 50 labels whose kept place is followed by a bracket, seven brackets are a more
familiar name for the same place, and those labels changed: Lugdunum to Lyon, Streanæshalch to
Whitby, Pozsony to Bratislava, Khanbaliq to Beijing, Sebaste to Sivas, Imkullu to Massawa,
Baviaanskloof to Genadendal. The other 43 brackets are sub-places, containing regions or notes,
not other names. Kept as written, because the first name is already the familiar one or neither
is widely known: Paris (Lutetia), Mérida (Emerita Augusta), Squillace (Scolacium), Scetis (Wadi
al-Natrun), Hierapolis (Koçhisar), Telanissos (Deir Sem'an). Every changed label still passes the
validator: the familiar name is in the entry's own region text.

## PL2 — modern countries

Every country comes from a Wikidata query made on 2026-11-07, never from memory. From the build
sandbox, Wikidata's entity API refused requests (HTTP 429); its query service answered, and every
lookup went through it under a named client.

1. **Lookup (Sonnet).** Each of the 308 distinct places was matched to a Wikidata item, using its
   region text to tell namesakes apart, and given that item's "country" property (P17). A
   Pleiades ID is kept where the item carries one (P1584).
2. **Re-query (mechanical).** Every chosen item and country item was queried again: 263 items, no
   mismatch. Every country is a sovereign-state item, and every recorded country is among the
   place's own P17 values.
3. **From the entry's own words.** Where Wikidata had no usable item but the region text names a
   modern place, that place was looked up instead (for example "Telanissos … Syria", "Ruthenia
   (today's Ukraine & Belarus)", "Shahabdike village, Sialkot District"). The `basis` field says so.
4. **Independent check (Opus).** 240 places in use; 230 passed. Fixed from sources: Aksum (the
   text names Ethiopia and Eritrea), Caucasian Albania (the text names Dagestan, a republic of
   Russia), Bithynia-Pontus (matched to Bithynia rather than all of Asia Minor). Armenia moved to
   the historical regions. Kept as Wikidata gives them: Upper Lusatia (Poland, Germany, Czech
   Republic), the Ethiopian Highlands (Ethiopia).
5. **Not given a country:** 34 broad areas (for example "Global", "Mediterranean"); 28 historical
   regions whose Wikidata items name only dissolved states, or a single country that understates
   them; and 7 places under disputed sovereignty. The last two groups wait for Mark's ruling.

`countries-by-place.json` holds every place, its item, its countries and the basis.
`modernCountries` on each census movement and each gap story lists, per place on its label, the
country, the country's Wikidata ID, the place, and the place's Wikidata ID. The validator requires
both IDs and that the place is on the label.
