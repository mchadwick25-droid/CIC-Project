# Card edits: John Chrysostom (`john-chrysostom`)

Starting card: `Card.existing.json` (the `card` field of the census entry, copied before any edit). New card: `john-chrysostom.card.json`. Unchanged word for word: `knownFor`, `role`, `keyWorks`, `sources.ownWords`, the six old `sources.about` entries, every old `legacy.traces` and `uncertain` item, and three of the four old `legacy.remembered` items. Old items keep their order; new ones are inserted beside the item they belong with.

File short names are those of `Source_Sheet.md` (SS, PALL, PG47, PG52, N109, N110, PHOT, THDT, CASS, SOZG). MARC = `cic/texts/chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`.

## Clearly wrong (corrected)

1. `legacy.remembered`, the Origen item.
   - Old: "... while John Chrysostom was restored to communion in the thirty-fifth year after his deposition."
   - New: "... while John Chrysostom was restored to communion in the thirty-fifth year after his death."
   - Evidence: the item credits Socrates, whose own words are "the latter was restored to communion by Proclus in the thirty-fifth year after his death!" (SS 21476-21479). The outline also notes the two readings (Ending 1).
2. `briefReferences`, the Palladius death entry: "in 407" taken off Palladius. Outline Do not say: "Do not date the march to Pityus, and do not give Palladius a year. Palladius gives none." The year now stands on its own entry, Socrates VI.21 (SS 18609-18612).
3. `briefReferences`, the Socrates VI.15 entry: "in 403" taken out. Outline Do not say: "Do not give the Synod of the Oak a year. No held old source dates it" (Source_Sheet S5: 403 is Freese's note, PHOT 3862-3864).
4. `briefReferences`, the Marriott entry ("Homilies on Matthew, Preface to the Oxford Edition, by C. Marriott: the homilies were delivered at Antioch") replaced by John's own words. It gave a modern editor's statement as content; the homily itself carries it (Source_Sheet S4; N110 5301-5303).

## briefReferences (rebuilt to the finished brief, in its order)

Removed, since the brief no longer tells them (role, check 3): the Diodore entry (Sozomen VIII.2; Socrates VI.3 on the literal sense); the Egyptian monks in the Socrates VI.7 and VI.9 entry (cut back to Theophilus's resolve, which the brief keeps: "and that he resolved to unseat him"); "the people rising" in the VI.15-16 entry (brief: "The emperor ordered him into exile, and John gave himself up, but he was soon called back").

Kept word for word: VI.5 rebukes and grudge; VI.3 native of Antioch; VI.2 (with "the court's choice of John" added, brief: "the court chose him"); Palladius on the hospital; Photius on the charges; the two VI.18 entries; the census tradition entry.

Edited or added, each with the brief's sentence and its lines:
- VI.5 Eutropius: "his fall" became "his fall in his own consular year, 399" ("Soon after, in 399, he fell from favor"; SS 17362-17365).
- Homily I on Eutropius: now gives the Greek and Stephens, and the quote as spoken (Q1; PG52 822-827; N109 17722-17727).
- New, Socrates VI.4: sermons published and taken down in shorthand ("He published some of his sermons, and shorthand writers took down others"; SS 17303-17308).
- New, Socrates VII.45: the followers brought back (essence, "the followers who left the church over his fall came back only when his body came home"; SS 21459-21469).
- New, the Dialogue: twelve years a priest at Antioch ("as a priest there for twelve years"; PALL 3443-3446).
- Homily 50: adds the gold cup and gold cloths of the table and the rest of the quote ("They decked the altar ... with gold cups and silk", Q2; N110 29907-29914, 29931-29933, 29959-29965).
- New, Homily 7 on Matthew: places the sermons at Antioch (N110 5301-5303).
- New, Socrates VI.4 and Sozomen VIII.3, VIII.8: the clergy ("He corrected his clergy sharply ... many came to hate him"; SS 17261-17276, 42798-42800, 43185-43191).
- Gainas entry: adds Sozomen VIII.4 ("John spoke against it before the emperor"; SS 42884-42905).
- Socrates VI.9: Theophilus's resolve (SS 17838-17840).
- Socrates VI.15: adds his demand for a general council ("asked for a council of the whole church"; SS 18286-18293).
- New, Photius: the counts examined and the forty-five ("some charges were heard, and then all forty-five bishops voted to remove him"; PHOT 3946, 4028-4032).
- VI.15-16: the decree, his surrender, the recall (SS 18302-18307, 18341-18365).
- New, VI.18: barred from the church by two synods, the baths, the exile by force ("Since two councils had condemned him ... In 404 he was taken into exile by force"; SS 18486-18502).
- New, Sozomen VIII.22: Cucusus in Armenia ("He was first exiled to Armenia"; SS 44066-44069).
- Palladius entry rewritten to the brief's paragraph: the bishops of Syria, Pityus, the soldiers, Comana, white clothes, Communion, the last words, with the two Greek prints (PALL 6339-6353, 6399-6406, 6439-6442, 6457-6460, 6495-6499; PG47 11682-11683, 5813-5814).
- New, Socrates VI.21: death on 14 September 407 ("He died there, in September 407"; SS 18609-18612).
- VII.45 entry: adds the emperor's leave, Comana, the procession and the Church of the Apostles, and that the history ends with these years ("Socrates, a church historian of the city writing a generation later"; SS 21459-21471).

## quotationOriginals

One entry for each of the brief's three quoted spans.
- Q1, new. "When everyone ignored him ... unbearable hatred." Printed: Stephens's English, N109 17722-17727. The note inside 17724-17725 is left out. The only held Greek, PG52 822-827, is a damaged scan ("δείδεται" for φείδεται, "υἷσος" for μῖσος, chi for kappa), and no other Greek print is held, so the English print stands alone (role). Greek checked by hand against the rendering: πάντων αὐτὸν ἐν ἐρημίᾳ παριδόντων / μόνη καθάπερ μήτηρ φιλόστοργος / ὑπὸ τὰ παραπετάσματα αὑτῆς ἔκρυψε / πρὸς βασιλικὴν ὀργὴν ἔστη, πρὸς δήμου θυμὸν, καὶ πρὸς μῖσος ἀφόρητον. Every clause holds. No `secondReading` (24 words).
- Q2, new. "Do you want to honor Christ's body? ... dying of cold and nakedness." Printed: Prevost's English, N110 29931-29933 (the sheet's 29934 ends a line later; the words end on 29933). Greek not held. No `secondReading` (32 words).
- Q3, kept word for word ("Glory to God for all things."; Moore, PALL 6498-6499; `secondReading` "same"). Added: `original` "Δόξα τῷ Θεῷ πάγτων ἔγεχεν", PG47 11682-11683, as the scan prints it, and an `uncertain` note. The outline renders Q3 from this Greek, and a second held print confirms it (PG47 5813-5814, "Δόξα τῷ Θεῷ πάντων ἕνεχεν"). Hand check: Δόξα τῷ Θεῷ πάντων ἕνεκεν, "Glory to God for all things".

## legacy.traces (added)

- After the Palladius item: the further hospitals, with two priests, doctors and cooks (outline, For the card; PALL 3773-3775).
- At the end: the captives bought back in Armenia, and the visitors from Antioch and Syria (outline Leave out, Cucusus; SS 44455-44465).
- At the end: Cassian, whom he made a deacon, holding him up against Nestorius (outline Cut first 2, For the card; CASS 55076-55091 (addressed to the bishop the city took from Antioch, as it had taken John), 55143-55144, 55167-55172; Gennadius, THDT 43243-43245).

## legacy.remembered (added)

- Sozomen: his boldness pleased the people and grieved the wealthy and the powerful (outline Cut first 8; SS 42723-42728).
- Socrates: his clergy turned on him over his correction of their lives, Serapion's words, and the expulsions (outline Leave out, "Serapion ... card"; SS 17261-17276).
- Theodoret: the West's refusal of Communion until his name was put back, and Alexander at Antioch (outline Cut first 13; THDT 17765-17777, 17832). "Named in the church's prayers" is the custom of the list, as the outline's Words to explain gives it (Jackson's note, THDT 17833-17842, clarifies).
- Theodoret: the emperor at the coffin (outline Cut first 7; THDT 17864-17867). The outline's "son of the rulers who had exiled him" is left off: the held line says only that he prayed for his parents.

## uncertain (added)

- First: the name Chrysostom, golden-mouthed (outline Cut first 1, Do not say; PALL 734-736; PG47 7070; SOZG 26525; SS 43264-43267).
- Second: Libanius, Diodore and the literal sense, and the expected career at law (outline Cut first 17, Leave out; SS 17132-17133, 17170-17185; SS 42690-42698).
- Third: taken from Antioch in secret (Source_Sheet E2, "Card"; SS 42739-42748).
- After the Eutropius threat: Gainas by name, Socrates's "it is said", Sozomen's palace scene and the law of Theodosius (outline Cut first 6, 11, For the card; SS 17368-17374; SS 42884-42905).
- Before Theophilus's resolve: the monks from Egypt, their quarrel, Theophilus's own teaching, and John's postponement of their Communion (outline Cut first 10, 16, For the card; SS 17578-17592, 17655-17693, 17825-17836). The old item names "the Egyptian monks", which the brief no longer explains; this item gives the explanation.
- After the Oak's two accounts: the causes of the recall, Socrates against Theodoret (outline Leave out; SS 18316-18342; THDT 17687-17704).
- After the sermon against women: the charge that he called the empress Jezebel (Source_Sheet §5, "Card"; PALL 5205-5207; 1 Kings 18:4 for the gloss).
- At the end: the fire, with Sozomen's account beside Socrates's (Source_Sheet §5, E11; SS 44059-44065).
- At the end: Cucusus, and Marcellinus against Socrates on whose will the exile was (outline Cut first 12; Source_Sheet §5, §7; SS 44066-44069; MARC 5353-5361; SS 18496-18502).
- At the end: the Dialogue's and Sozomen's reasons for the move to Pityus, its desolation and the three months (outline Cut first 5, 12, Leave out, Rome's envoys; PALL 6339-6353, 6399-6401, 6421-6422; SS 44475-44496).

## sources.about (added)

Sozomen, Book 8, chapters 3, 4, 8, 10, 22, 27 and 28 (SS); Sozomen's Greek chapter headings (SOZG); Theodoret, Book 5 (THDT); Gennadius on Cassian (THDT); Cassian, On the Incarnation, Book 7 (CASS); Marcellinus, Chronicle (MARC). Each is a file a new item cites.

## Not carried

- The Liturgy of St John Chrysostom: the outline says "Leave out".
- "Again Herodias raves": its authenticity is doubted (outline Leave out, "card at most").
- The punishment of his friends after the fire: no lines on the sheet; the Olympias page tells it.
- Sozomen's reasons for his eating alone: no lines on the sheet. The card already gives Palladius's reasons.
- Links to other entries (Olympias, Epiphanius and others): the role leaves them out for now.

## Not found (left in place)

- `legacy.traces`: "called Johannites by their opponents". Socrates says only that they "were from him denominated 'Johannites'" (SS 18494-18496). No held line says their opponents gave the name.

## Entry fields

- `longDescription`: replace with the finished brief, `john-chrysostom.brief.txt`, final newline removed.
- `modernWorks` (new): five translations whose notes the outline used to clarify the old texts. These are the consular years, Sozomen's independence from Socrates, the curtain before the altar, the place of the Matthew homilies, the Dialogue's title and author, and the custom of the lists. All are public domain (1888-1921) and held in `cic/texts/`. No modern work was listed under the card's `sources`, so none moves. Freese's Photius is left off: the outline used his note only for the 403 it keeps out. Hefele and Duchesne were "used for nothing" (Source_Sheet §7).
  ```json
  [
    {"title": "Socrates and Sozomenus: Ecclesiastical Histories (Nicene and Post-Nicene Fathers, Second Series, volume 2)", "author": "A. C. Zenos and C. D. Hartranft (tr.)", "year": "1890", "note": "English translations of the church histories of Socrates and Sozomen, with notes that turn their consular years into years of the common era and compare the two accounts."},
    {"title": "St. Chrysostom: On the Priesthood; Ascetic Treatises; Select Homilies and Letters; Homilies on the Statutes (Nicene and Post-Nicene Fathers, First Series, volume 9)", "author": "W. R. W. Stephens and others (tr.)", "year": "1889", "note": "English translations of John's treatises, letters and sermons, among them the two homilies on Eutropius, with a note on the curtain before the altar."},
    {"title": "St. Chrysostom: Homilies on the Gospel of Saint Matthew (Nicene and Post-Nicene Fathers, First Series, volume 10)", "author": "George Prevost (tr.), revised by M. B. Riddle", "year": "1888", "note": "English translation of John's ninety sermons on Matthew, with notes on the Bible passages they cite."},
    {"title": "The Dialogue of Palladius Concerning the Life of Chrysostom", "author": "Herbert Moore (tr.)", "year": "1921", "publisher": "Society for Promoting Christian Knowledge", "note": "English translation of the Dialogue on John's life, with an introduction on its title, its author and its date."},
    {"title": "Theodoret, Jerome, Gennadius, & Rufinus: Historical Writings (Nicene and Post-Nicene Fathers, Second Series, volume 3)", "author": "Blomfield Jackson and others (tr.)", "year": "1892", "note": "English translations of Theodoret's Church History and Gennadius's Lives of Illustrious Men, with a note on the lists of dead bishops read at the Eucharist."}
  ]
  ```
- `why`, `relationsSummary`, `teaser`, `legacy`: checked against the brief. Each is the approved heart or agrees with the brief, so no change. `voices` and `sourcing` call Palladius "a bishop who stood by him". The brief now says "took his side", following the Do not say against "stood by John to the end". The shorter claim stands on PHOT 3946-3948, where the Oak tries "the bishops Heraclides and Palladius of Helenopolis". It is not changed; it is listed here for the checker.

## For release

- Q1 and Q2 are renderings, so they need listings in `tools/quote_renderings.json` before the census validates. Q1's original is PG52 822-827 (Greek). Q2's is N110 29931-29933 (English).
- `secondReading` for Q1 and Q2 comes from the second readings.
- Check run on a scratch copy of the census (the brief as `longDescription`, this card, the `modernWorks` above): `node tools/validate-census.mjs` gives exactly four errors for this entry. Two are the missing `secondReading`s and two are the missing rendering listings. Every `printed` and `original` stands at its lines, and every quoted span in the card's prose is found.
