# Eutyches: card check

**Verdict: FIX** (four changes, below). Everything else passes.

## What was checked

- **Nothing else moved.** I compared the card as it stands against `Card.existing.json`, field by field and item by item, with a script. Every existing field and list item is word for word and in its old place. The only differences are the appended items in `Card_Edits.md` (traces +5, remembered +1, uncertain +9, sources.about +8) and the new `briefReferences` and `quotationOriginals`. The shared scratch script did not disturb the file.
- **Validator.** I ran `tools/validate-census.mjs` on a scratch census with this card and the brief. It gives four errors, all left for release: `secondReading` on Q1 and Q2, and Q1 and Q2 not yet in the renderings file. Keys are allowed and there is no `briefLength`.
- **Quotations.** There are three, one per quoted span in the brief, and none for a dropped span. Q1's printed text matches Perry 23843-23845. Q2's matches Perry 23494-23495, with the rest at 23504 noted. Q3's matches Leo 5028.
- **Q1 Greek, checked by hand.** It matches Evag-G 2285-2286. The OCR's smooth-breathing `᾿Ομολογῶ` is rightly given its rough breathing, `Ὁμολογῶ`. The closing `ὁμολογῶ` (2288) sits after the garbled line 2287. The card leaves it out and says so, and three other held prints confirm the words (Evag-E 1729-1731, Perry, Leo 5597-5598).
- **Q3, "checked at card".** "This he certainly never did." matches the printed "this he certainly never did" (Leo 5028). It is a word-for-word English print, and no original is held.
- **New traces and uncertain items, re-read at their lines.** These hold: Zach 5985-5991, 6006-6008, 6161-6163; Life of Severus 6855-6858, 7358-7366; Severus letters 711-722; Philoxenus 1569-1573; Ormanian 5305-5310; Councils 30126-30129; Michael 1706-1712; Leo 4470-4489, 4606-4611; Zach 1123-1130, 1185-1213, 1306-1310; Perry 23248-23253, 23289-23293, 24015-24020; Evag-E 1740-1745; Bazaar 18895-18915. The exceptions are fixes 2 and 3 below.
- **Every cited file is in `sources`.** No audit is named.

## The two claims left unchecked by the writer

- **Chrysaphius as godson: found, and stays.** Feltoe's introduction calls him "the eunuch Chrysaphius, Eutyches' godson" (`npnf212_leo-great-gregory-great.xml` 588-589). Liberatus, in a rough scan, says Eutyches received him from baptism: "per Chrysaphium eunuchum ... quem Eutyches susceperat de sacro baptismate" (`liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt` 78116-78117). The editor's note at 77883-77885 says the same. The card's wording is accurate. `Card_Edits.md` should list this as found, not as unchecked.
- **Exile after Chalcedon: overstated.** The only held source is Feltoe's summary of Letter CXXXIV to Marcian, which the edition does not translate. The summary reads "(Suggesting that Eutyches should be banished to a still remoter place, where he cannot do so much harm by his false teaching.)" (Leo 11331-11333). It records Leo's suggestion. It does not say that a further exile happened. It does presuppose that he was already banished. The card's "exiled further" states as fact what the source gives only as a request. The brief's "the record goes quiet" agrees with the corrected reading. See fix 1.

## FIX

1. **`uncertain[5]`** (an existing item, corrected as clearly wrong against Leo 11331-11333)
   - Old: `That he was exiled further after Chalcedon rests on Feltoe's summary of a letter of Leo that the English edition does not translate.`
   - New: `That he was in exile after Chalcedon rests on Feltoe's summary of a letter of Leo that the English edition does not translate, which suggests he be banished to a still remoter place.`

2. **`uncertain[13]`** (new). As worded, it says he asked so that he would suffer shipwreck. Leo 4608-4611 asks that he not be expelled, which would be shipwreck at the end of life.
   - Old: `In his letter to Leo he asked not to be expelled, after seventy years of continence, so that at the very end of life he should suffer shipwreck. The seventy years are his own claim.`
   - New: `In his letter to Leo he asked not to be expelled after seventy years of continence, and so suffer shipwreck at the very end of life. The seventy years are his own claim.`

3. **`uncertain[15]`** (new). Hefele is the historian of the councils whom Percival quotes (Councils 30148, "Hefele."). He is not this text's editor. Other census entries call him "the historian of the councils".
   - Old: `Hefele, an editor, doubts the text of canon 95`
   - New: `Hefele, a historian of the councils, doubts the text of canon 95`

4. **`briefReferences[1]`** (Evagrius). The brief no longer tells that the genuine followers were "reduced to a very small number" (Evag-E 6793-6795). It tells only that later writers on Chalcedon's side called the refusing churches followers of Dioscorus and Eutyches.
   - Old: `the genuine followers of Dioscorus and Eutyches reduced to a small number.`
   - New: `the refusing churches called followers of Dioscorus and Eutyches.`

## Noted, no change

- Q2's `modern` keeps the brief's "grey". The rendering must match the brief exactly, so any change to it belongs to the brief, not the card.
