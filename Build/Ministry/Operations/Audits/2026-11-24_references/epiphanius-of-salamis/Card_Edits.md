# Card edits: Epiphanius of Salamis

Card: `epiphanius-of-salamis.card.json`, from `Card.existing.json` (the census entry's `card`, copied unchanged before any edit). Every field not listed here is word for word. No `briefLength`. Brief: `epiphanius-of-salamis.brief.txt` (744 words by the scorer, approved by Mark as it stands).

File short names as in `Source_Sheet.md`: HOLL1 = `cic/texts/epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`; PG42 = `cic/texts/epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt`; J6 = `cic/texts/npnf206_jerome-principal-works.xml`; J3 = `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`; SS = `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml`; MEN = `cic/texts/mendham_seventh-general-council-second-of-nicaea_1850.txt`; AUG = `cic/texts/augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt`.

Validator, on a scratch copy of the census with this card and the brief (final newline removed) as `longDescription`: `--skip-quotes`, 0 errors. With the Library quote check, run on a copy in which the other entries' `sources` were removed to keep memory down: no error for this entry (the errors reported are the other entries', from their removed sources).

## quotationOriginals

Unchanged. The brief quotes the same two spans as before, word for word: Q1 (Proem I) and Q2 (the Euphrates). Re-read: HOLL1 12387-12391 (the Greek as printed, with the three scan slips the entry's `uncertain` names, each listed in `tools/quote_scan_readings.json`); J6 10920-10922 ("I have drunk also from the great river Euphrates, not spiritual but actual water, such as you can touch with your hand and imbibe with your mouth."). Both carry their existing `secondReading`. The brief no longer quotes anything else, and the card had no other entry. Q1's Greek is held only in Holl's scan, but its slips are trivial, named and read, and no printed English exists to stand alone, so the Greek stays as the earlier checks left it.

## Clearly wrong, or against Part 1 of the kit

Part 1 keeps a date, identification or judgment that only a modern work makes off the card, and the outline's Who tells it lists these as "kept out of the story and the card".

1. `knownFor`. Old: "in the quarrels of the 390s and early 400s." New: "in the quarrels of his old age." Evidence: the decade rests on an editor's chronology only (Source_Sheet S5; J6 3042, 40439-40440); the outline's Do not say bars "in the 390s"; the brief says "In old age he carried the same fight to Jerusalem and Constantinople".
2. `datesNote`. Old: "Born about 310, bishop about 368 or 369, died in 403 (Ernest Cushing Richardson's note to the Lives of Illustrious Men by Jerome of Strido)". New: "The fourth century. No held ancient source gives the year of his birth or death. He dates the Panarion himself to the eleventh year of Valentinian and Valens and the seventh of Gratian, about 375. He died at sea in old age, sailing home from Constantinople". Evidence: the old years are Richardson's (J3 41528) and the editors disagree with each other (Source_Sheet S5); outline Setting ("in the fourth century"; the Panarion "about 375" from his own regnal date, HOLL1 13424-13426); death at sea, SS 18227-18228, 43622-43623; old age, J3 41531-41533 ("in his extreme old age"). The brief: "He wrote the Panarion about 375."
3. `legacy.traces[2]`. Old: "Augustine, in On Heresies, written about 428 by its editors' date, says". New: "Augustine, in On Heresies, says". Evidence: the year is the PL editors' only (AUG 1098); outline Who tells it and Fixes item 4.
4. `uncertain[2]`. Old: "Socrates says. A. C. Zenos, in a note to his translation of Socrates, says Epiphanius himself rejected that view, on Jerome's testimony." New: "Socrates and Sozomen say. Jerome, who was there, says Epiphanius condemned that view in public at Jerusalem." Evidence: the second sentence used a modern note as the witness; the old witness it points to is Jerome, J6 41000-41015 ("my voice, too, condemns that heresy"); outline Do not say ("Jerome shows him condemning that teaching in public"). Sozomen added because the outline sends the charge "in Socrates and Sozomen" to the card (For the card, last item): SS 43502-43508 ("although he had formerly blamed him for asserting that God possessed a human form").
5. `uncertain[11]`. Old: "The Caroline Books, written at Charlemagne's order, answered". New: "The Caroline Books, a reply to the council, answered". Evidence: Charlemagne's order is on Mendham's title page only (MEN header line 1); outline Do not say ("written at Charlemagne's order"); what the book was, MEN 26283-26291. The brief: "A book written to answer the council's argument".

## New: what the outline sends to the card

Each from the outline's **For the card, not the story**, appended at the end of its field.

6. `legacy.traces` [5], new: "In heresy 77 of the Panarion he lists the followers of Apollinaris of Laodicea, whom he calls always dear to him, for teaching that Christ took flesh and a soul but no human mind." Evidence: PG42 48828-48833 ("σάρκα ἔλαβεν ... καὶ ψυχήν, νοῦν δὲ οὐκ ἔλαβε", in the scan's spelling), 48853-48857 ("ὁ ἀεὶ ἡμῖν ἀγαπητός ... Ἀπολλινάριος ὁ ἀπὸ Λαοδικείας"). Cut first 14.
7. `legacy.remembered` [8], new: "Sozomen says he made his home near the village of Besauduc, his birthplace, in the district of Eleutheropolis, and that the people of Cyprus chose him as bishop of the chief city of their island. Jerome calls his house there the old monastery." Evidence: SS 39793-39799 ("fixed his abode near the village of Besauduc, which was his birthplace, in the government of Eleutheropolis ... chosen by the inhabitants of Cyprus to act as bishop of the metropolis of their island"); J6 18736-18738 ("the monastery of the reverend pope Epiphanius—called the old monastery"). Cut first 13. The card's `placeNote` already gives Besauduc; the choice by the Cypriots and the monastery were not on it.
8. `uncertain` [14], new: "Jerome, who was there and on his side, says that while Epiphanius preached against Origen in the church at Jerusalem, the bishop of Jerusalem's party mocked him as a silly old man, and that crowds pressed to meet him and kiss his feet." Evidence: J6 40982-40996 ("We were present ... talked of the “silly old man.” ... a crowd of all ages ... was flowing to meet him ... kissing his feet"). Cut first 12. Placed under `uncertain` because it is a partisan's account (outline beat 4). No quotation marks.

Already on the card, so not added: Photius's verdict (`legacy.traces[3]`), Hilarion (`traces[4]`), thirty-six years (`remembered[6]`), monks from all parts of the world (`remembered[5]`), Augustine's fifty-seven heresies and the great among the Greeks (`traces[2]`), Jerome on the learned and the plain people (`remembered[1]`), the tomb (`remembered[0]`), his training (`remembered[3]`), his giving (`remembered[4]`), Theophilus's change of view (`uncertain[3]`, `remembered[7]`), Q3's farewell (`uncertain[10]`, a paraphrase with no quotation marks), Theophilus's earlier charge (`uncertain[2]`, with Sozomen now added).

## New: references the brief draws on

9. `sources.about[2].title`. Old: "Letter 57, to Pammachius;". New: "Letter 57, to Pammachius; Letter 82, to Theophilus; Letter 90, from Theophilus to Epiphanius;". Evidence: the new `remembered` line cites Letter 82 (J6 18736-18738); the brief's "His letter said he had driven monks who followed Origen out of Egypt" draws on Letter 90 (J6 19716-19733). Same file, already cited.

`briefReferences`, rebuilt to what the brief now tells. Entries [0], [3] (Panarion 33) and [11] (the census tradition) are word for word.

10. New [1]: "Panarion, Proem I, the list of the heresies: twenty before Christ's coming and sixty after." Brief: "twenty from before Christ's coming and sixty after". HOLL1 12510-12527.
11. [1] → [2], edited. Old: "Panarion, Proem II: some heresies known from study". New: "Panarion, Proem II: a heresy as a wrong belief spread by people led astray since man was formed on earth; some heresies known from study"; the rest word for word. Brief: "A heresy, to Epiphanius, was a wrong belief held by people led astray ever since Adam, the first man." HOLL1 13420-13425.
12. Old [3] removed: "Panarion 77: Apollinaris, always dear to him, and his followers listed." The brief no longer tells it (now `legacy.traces[5]`).
13. Old [4] edited. Old: "Sozomen, Church History 6.32: his birth near Eleutheropolis and his choice as bishop by the people of Cyprus." New: "Sozomen, Church History 6.32: a monk in Palestine and Egypt, chosen bishop of the chief city of Cyprus, a seaport." Brief: "a monk from Palestine who became bishop of Salamis, the chief city and port of Cyprus." SS 39793-39802. The birthplace is no longer told.
14. Old [5] edited. Old: "Jerome, Against John of Jerusalem 11: his sermon against Origen at Jerusalem, the mockery of the bishop's party, and the crowds pressing to kiss his feet." New: "Jerome, Against John of Jerusalem 11: his sermon against Origen in the church at Jerusalem." The mockery and crowds are no longer told (now `uncertain[14]`).
15. Old [6] edited. Added after "the seizing and ordination of Jerome's brother": ", with his reasons, the monks' year of complaint that no one celebrated the sacraments for them and his fear that they would be turned from the Church"; and after "the curtain at Anablatha": ", and his reason, that an image of a man in Christ's church went against the Scriptures". Brief: "The monks there had complained for a year that no one celebrated the sacraments ... and he feared they would drift from the church"; "Holding that an image of a man in church went against Scripture". J6 10655-10659, 10704-10705, 11105-11107.
16. New [7]: "Theophilus's letter to Epiphanius (Jerome's Letter 90), tr. Fremantle: the monks who followed Origen cut down and driven from Egypt, and the call to gather the bishops of Cyprus." Brief: "His letter said he had driven monks who followed Origen out of Egypt." J6 19716-19733.
17. Old [7] → [8], edited. "Theophilus and the ban in Cyprus, the voyage" becomes "Theophilus and the ban in Cyprus; Socrates on Theophilus's revenge on the monks he had driven out and on Epiphanius's piety and simple mind and manners, Origen dead long before; Sozomen on Epiphanius's long aversion to Origen's books and Theophilus following his example because the people praised him; the voyage"; the rest word for word. Brief: the Socrates and Sozomen sentences, and "Origen, a Christian teacher who had died long before". SS 17884-17899 ("who had been dead nearly two hundred years"); SS 43510-43520.
18. Old [8] → [9], edited. Old: "Augustine, On Heresies: Epiphanius's twenty heresies before Christ and sixty after, and his order followed." New: "Augustine, On Heresies: his order followed." The brief now tells the twenty and sixty from Epiphanius's own list (entry [1]), as the outline's Do not say requires. AUG 2414-2415.
19. Old [9] → [10], edited. Old: "the ruling that the passage against images was none of his, and the reply from his letter on the curtain." New: "the quarrel over images of Christ and the saints in churches; the writings against images quoted under his name; the ruling that they were none of his, since his eighty chapters list no heresy of making images; and the reply from his letter on the curtain." Brief: "when Christians quarreled over pictures of Christ and the saints in churches ... opponents of images quoted writings under his name ... ruled that those writings were not his, arguing that his eighty chapters never listed the making of images". MEN 8494-8495, 26231-26239, 26273-26281, 26282-26316.

## Entry fields

For release, if the checker passes them. The card is not touched by these.

- `teaser`. Old: "Bishop of Salamis in Cyprus, author of the Panarion against the heresies, and a leading accuser of Origen in the quarrels of the 390s and early 400s." New: "Bishop of Salamis in Cyprus, author of the Panarion against the heresies, and a leading accuser of Origen in the quarrels of his old age." Same evidence as edit 1.
- `longDescription`: the brief, final newline removed (release).
- `modernWorks`, new (the entry has none). The outline's Who tells it, "Modern, clarifying an old text", names the editions and notes it used; none of the card's `sources` is a modern work, so nothing moves from there. All are public domain by date (file headers). Proposed, in this order:

```json
[
  { "title": "Epiphanius, erster Band: Ancoratus und Panarion haer. 1-33 (Die griechischen christlichen Schriftsteller 25)", "author": "Karl Holl (ed.)", "year": "1915", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of the Ancoratus and of Panarion 1 to 33, with notes on the text, the biblical allusions and the date of the Panarion." },
  { "title": "The Principal Works of St. Jerome (Nicene and Post-Nicene Fathers, series 2, volume 6)", "author": "W. H. Fremantle, with G. Lewis and W. G. Martley (tr.)", "publisher": "T&T Clark, Edinburgh; Wm. B. Eerdmans, Grand Rapids", "note": "English of Jerome's letters, among them Epiphanius's letter to John of Jerusalem and Theophilus's letters, and of Against John of Jerusalem, with notes on names and places." },
  { "title": "Socrates and Sozomenus, Ecclesiastical Histories (Nicene and Post-Nicene Fathers, series 2, volume 2)", "author": "A. C. Zenos and Chester D. Hartranft (tr.)", "publisher": "T&T Clark, Edinburgh; Wm. B. Eerdmans, Grand Rapids", "note": "English of the two church histories, with notes on names, places and the church rules on ordaining." },
  { "title": "The Dialogue of Palladius Concerning the Life of Chrysostom", "author": "Herbert Moore (tr.)", "year": "1921", "publisher": "Society for Promoting Christian Knowledge, London", "note": "English of the Dialogue, with an introduction and notes." },
  { "title": "The Seventh General Council, the Second of Nicaea, held A.D. 787", "author": "John Mendham (tr.)", "year": "1850", "publisher": "William Edward Painter, London", "note": "English of the acts of the council of 787, with notes from the Caroline Books." }
]
```

  NPNF years are not printed in the held files, so none is given. Names from the held title pages: Zenos (SS, "Revised, with Notes, by The rev. A. C. Zenos"), Hartranft (SS 21654, "Chester d. Hartranft"), Fremantle, Lewis and Martley (J6 title page), Holl, Moore and Mendham (file headers, from their title pages).
- `dates` "c. 310-403", `start` 310, `end` 403 and `activeYear` 368 rest on the editors' years only (Richardson, J3 41528). They feed the timeline, so no change is proposed here; flagged for Mark, since a rule for timeline years drawn only from editors is a fleet-level call.

## Claims not found

- `uncertain[11]`, "the council of 754": no held line gives the year 754 (MEN has no "754"); the council's own text calls it the present heresy's definition, read out at MEN 26229-26241. Left in place.

## Considered, left as they are

- `uncertain[3]` and `sources.about[3]`: "which Herbert Moore gives to Palladius of Helenopolis" / "as Herbert Moore identifies him". An identification credited to Moore, not stated as content; the sources line needs an author. Left.
- `uncertain[5]`: "His dates are Richardson's reckoning." Still true of the entry's `dates`, which the page shows. Left.
- `uncertain[10]`: Hartranft's and Moore's English for the Greek word. Translation notes on an old text. Left.
