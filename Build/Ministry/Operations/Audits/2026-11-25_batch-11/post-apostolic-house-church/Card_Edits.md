# Card edits: The Post-Apostolic House Churches

Starting card: `Card.existing.json` (the census entry's card fields; a tradition has no `card` field). New card: `post-apostolic-house-church.card.json`. Brief: `post-apostolic-house-church.brief.txt` (final after `Grade_Fixes_Applied.md` and `Grade2_Fixes_Applied.md`). Every field and item not listed below is word for word, in the same order. The new keys (`uncertain`, `quotationOriginals`) come at the end; six new items come at the end of `sources`.

## How a tradition's card is shaped here (for the checker and release)

As for this batch's `roman-church-third-century` card: `tools/validate-census.mjs` refuses a `card` on anything but a person, and runs `checkQuotationOriginals` and the quotation check only for persons and councils. So the card file keeps the tradition entry's own fields:

- `sources`: the entry's own list (`work`, `type`, `note`, `url`), with `file` added to each item, after `type`, so each quotation ties to a cited file. The page ignores `file`.
- `quotationOriginals`: the `cyril-and-methodius` format, at the top level.
- `uncertain`: a list, as on a person card.

For release: a page home and a validator check for a tradition's `uncertain` and `quotationOriginals` do not exist yet.

## Quotations

The brief quotes three spans (`grep -o '"[^"]*"'`); each has one entry. All three run six words or more, so none carries `secondReading`. Each `printed` and `englishPrinted` was re-read in its file and found at its lines by a scratch fold check (the validator's `fold`, tags and notes stripped), and each file is among `sources`.

1. **Pliny (Quote 1).** Printed (Latin): `mirbt_...1911.txt` 2790-2791, "quod essent sohti stato die ante lucem convenire carmenque Christo quasi deo dicere secum invicem" (OCR as printed, spacing normalized). The scan is damaged ("sohti" for soliti), but a second held print of the same clause confirms the reading: `anf05_...xml` 60209-60211, "Soliti essent Christiani, stato die, ante lucem convenire, carmenque Christo, quasi Deo, dicere secum invicem" (an editor's endnote). So the Latin prints, as the role allows, and its `uncertain` names the misreading and the confirming print, as `cyril-and-methodius` does for its OCR spellings. English printed: `npnf201_...xml` 19492-19494, "they had been accustomed to come together on a fixed day before daylight and to sing responsively a song unto Christ as God". The outline cites 19493-19494; "they had" stands on 19492. The `uncertain` also keeps the outline's note that quasi deo is a pagan's phrase, "as to a god" (Outline, Do not say), against the 1890 English "as God".
2. **Justin (Quote 2).** Printed (Greek), checked by hand letter by letter: `justin-martyr_first-apology-grc_rauschen1911.txt` 1759-1762, "Καὶ τῇ τοῦ ἡλίου λεγομένῃ ἡμέρᾳ πάντων κατὰ πόλεις ἢ ἀγροὺς μενόντων ἐπὶ τὸ αὐτὸ συνέλευσις γίνεται, καὶ τὰ ἀπομνημονεύματα τῶν ἀποστόλων ἢ τὰ συγγράμματα τῶν προφητῶν ἀναγινώσκεται, μέχρις ἐγχωρεῖ." Each clause of the rendering stands on it: "on the day named after the Sun" (τῇ τοῦ ἡλίου λεγομένῃ ἡμέρᾳ), "all who live in the towns or in the country" (πάντων κατὰ πόλεις ἢ ἀγροὺς μενόντων), "gather in one place" (ἐπὶ τὸ αὐτὸ συνέλευσις γίνεται), "the memoirs of the apostles or the writings of the prophets are read" (τὰ ἀπομνημονεύματα … ἀναγινώσκεται), "for as long as time allows" (μέχρις ἐγχωρεῖ); nothing added. English printed: `anf01_...xml` 16502-16505, "And on the day called Sunday, all who live in cities or in the country gather together to one place, and the memoirs of the apostles or the writings of the prophets are read, as long as time permits;" (an endnote falls inside it; the note-stripped reading holds it).
3. **The Didache (Quote 3).** Printed (English; the Greek is not held, Source_Sheet, Short names): `anf07_...xml` 12700-12706, "There are two ways, one of life and one of death; but a great difference between the two ways. 2. The way of life, then, is this: First, thou shalt love God who made thee; second, thy neighbour as thyself;" (footnotes fall inside it). Its `uncertain` says the English stands alone. The modern rendering keeps the brief's "neighbour" exactly, as the role requires; the card's own prose uses "neighbor".

## Card fields

1. **why (a claim the brief no longer makes).**
   Old: "held together with no fixed hierarchy and no finished New Testament - Ignatius of Antioch wrote seven letters while under armed guard on his way to execution,"
   New: "held together through letters and messengers carried between them: Ignatius of Antioch wrote seven letters while under armed guard,"
   Evidence: Outline, Do not say: "no central body ruled them", "no finished New Testament" (entry texts) are "absence-only claims; say what they had: their own leaders in each city, letters between them". The approved-before-the-kit brief said "no single leadership structure" and "no fixed collection"; the finished brief says neither, and holds instead "Letters and messengers carried between their churches held them together" (the essence). The approved brief said "tradition has it that Ignatius met the same end"; the finished brief tells no death for him (Outline, Do not say: "Ignatius was killed in Rome → not told here"). The dash is replaced by the colon the new wording needs. "seven letters" and "under armed guard" stay (not contradicted).

2. **voices[1] (a date the old sources do not fix).**
   Old: "around the year 96"
   New: "near the end of the first century"
   Evidence: Outline, Do not say: "'in 96' → 'near the end of the first century'"; Setting: the letter placed in Clement's time (npnf201 16634-16636; anf01 39833-39836), Widely Accepted only for "near the end of the first century". Brief: "Near the end of the first century, the church at Corinth…". Kit Part 1, Rigor: a date that rests on an editor's reckoning is told only as roughly as the old sources allow. (`voices` is not one of the role's named short texts; the checker may hold this back.)

3. **voices[6] (the same).**
   Old: "around the year 112"
   New: "early in the second century"
   Evidence: Outline, Do not say: "'Pliny, around 112' → 'under the emperor Trajan'"; Setting: "early in the second century" (mirbt 2768; npnf201 16977; jerome-chron 42193-42262), Widely Accepted. Brief: "Early in the second century, Pliny governed a Roman province." The held dating "110 or 111" is McGiffert's (npnf201 19457). (As edit 2.)

4. **legacy (new: What came of it 1 and 3, which the outline sends to the card).**
   Old ends: "… were preserved and read for generations to come."
   New adds a paragraph: "In the early 300s, Eusebius says that the letter Rome sent to Corinth had been "publicly used in a great many churches both in former times and in our own." In 367, Athanasius set "the Teaching of the Apostles, and the Shepherd" among the books "appointed by the Fathers to be read by those who newly join us.""
   Evidence: Outline, What came of it 1 and Who tells it (Eusebius "beside 'publicly used in a great many churches' (card)"): npnf201 16683-16684, "this epistle also has been publicly used in a great many churches both in former times and in our own" (the epistle of 16679-16680, "in the name of the church of Rome to the church of Corinth"). What came of it 3 ("Card"): npnf204 68817-68823, "appointed by the Fathers to be read by those who newly join us … and that which is called the Teaching of the Apostles, and the Shepherd". All three quoted spans re-read at those lines.

5. **sources: `file` added to each of the nine items (new).** anf01 for Ignatius's Ephesians (4703, 4793-4794), 1 Clement, the Martyrdom of Polycarp (3744-4310), Polycarp's Philippians, Justin's First Apology and the Martyrdom of Justin (29295-29320); anf07 for the Didache; anf02 for Hermas; mirbt for Pliny 10.96. Evidence: Source_Sheet, Short names and Library sweep ("all nine read in full where held"). No other word of these items moves, except edits 6 to 11.

6. **sources[1], 1 Clement (a date, as edit 2; and new: Cut first 15 and 24).**
   Old: "around 96"
   New: "near the end of the first century"
   Added at the end: "It went by three messengers, Claudius Ephebus, Valerius Bito and Fortunatus, who were to be sent back quickly with news of peace. It speaks of the same leaders as holding the bishop's office and as elders."
   Evidence: as edit 2; Cut first 15 ("for the card"), anf01 2395-2398, "Send back speedily to us in peace and with joy these our messengers to you: Claudius Ephebus and Valerius Bito, with Fortunatus: that they may the sooner announce to us the peace"; Cut first 24 ("for the card"), anf01 1916-1943 (Source_Sheet C4, "the episcopate" and "presbyters" of the same leaders).

7. **sources[2], the Didache (new: What came of it 4; Cut first 11, 12, 13, 18, 19, 28; Leave out, the travelling apostles).**
   Added at the end: "It was found in 1873, in a manuscript copied in 1056, and published in 1883. Its way of life also teaches: whatever you would not want to happen to you, do not do to another; bless those who curse you; give to anyone who asks; share everything with your brother. The one to be baptized fasts a day or two first, and is baptized in living water, which its editor reads as running water, or in other water if there is none. Its prayers give thanks first over the cup, then over the bread: as this broken bread was scattered over the hills and gathered into one, so may the church be gathered into God's kingdom. On every Lord's day they confess their sins before the thanksgiving, and no one at odds with a neighbor comes until they are reconciled. It has them appoint their own bishops and deacons, and test the traveling apostles and prophets who come to them: one who stays three days, or asks for money, is a false prophet."
   Evidence: What came of it 4 ("Modern event. Card"), anf07 12524 ("In 1873 … 6564 = a.d. 1056"), 12585 ("At the close of 1883 he published"); Cut first 19, 12706-12708 ("all things whatsoever thou wouldst should not occur to thee, thou also to another do not do"); Cut first 11, 12712-12716, 12728-12730, 12827; Cut first 13, 12910-12920 and the editor's footnote 12918, "Probably running water" (Words to explain, living water: a modern note that clarifies a word); Cut first 18, 12960-12970; Cut first 12, 13087-13095; Cut first 28 and Review (Length), 13112-13116; Leave out ("The Didache's travelling apostles and prophets … card"), 13018-13022. The existing first sentence stays, including "from a single surviving manuscript" (listed below).

8. **sources[4], Polycarp to the Philippians (new: Cut first 4 and 10).**
   Added at the end: "It opens in the name of "Polycarp, and the presbyters with him." Its elders are to visit the sick and not neglect the widow, the orphan or the poor. Polycarp grieves for Valens, once an elder at Philippi, who "so little understands the place that was given him," warns against love of money, and asks the Philippians to call Valens and his wife back. He sends them the letters of Ignatius his church holds, as they asked, and offers to send their own letter on to Syria."
   Evidence: Cut first 10 ("for the card"), anf01 3232-3235, 3403-3405, 3531-3534, 3557-3562, 3608-3618; Cut first 4 ("card"), 3608-3618 ("if any one went [from this] into Syria, he should carry your letter with him"). Outline, Do not say: "Valens stole from the church" → his own words, then the warning; Polycarp is not called bishop in his own letter's voice.

9. **sources[5], Justin's First Apology (clearly wrong; and new: Cut first 5, 31; Leave out, "not as common bread").**
   Old: "the earliest detailed outside description"
   New: "the earliest detailed description"
   Added at the end: "Before baptism, those who believe pray and fast, the community fasting with them; then they are led to water. After the prayers, the believers greet one another with a kiss. They receive the bread and cup "not as common bread and common drink," and Justin gives Jesus's words over them from the apostles' memoirs. Those who are well off give what each chooses, and the one who presides uses it for orphans and widows, the sick, prisoners and strangers."
   Evidence: the brief, "Justin, a Christian, wrote to the emperor Antoninus Pius what Christians did each week"; Outline, Quote 2's job: "the gathering in its own words, from inside". Justin is no outsider. Cut first 5 ("card"), anf01 16232-16240 (J1) and 16413 ("we salute one another with a kiss"); Leave out ("Justin's 'not as common bread' and his account of Jesus's words … card"), 16450-16451 and 1apol-grc 1734-1745; Cut first 31 ("for the card"), 1apol-grc 1772-1779, anf01 16518-16526. The fuller wording of the collection (Cut first 17) and the presider's talk and the standing prayer (Cut first 20, 29, 34) are Leave out, so are not added.

10. **sources[7], Hermas (new: Cut first 2 and 7; Names).**
    Added at the end: "In a vision, Hermas writes, the Church as an old woman told him to make two copies of her words: one for a man named Clement, who would send it to cities abroad, and one for a woman named Grapte, who would teach the widows and orphans, while he read it in Rome with "the presbyters who preside over the Church." Elsewhere in his book, bishops gladly take God's servants into their houses."
    Evidence: Cut first 7 ("card"), anf02 1005-1026; Cut first 2 ("card"), anf02 4946-4952; Names ("Clement and Grapte in Hermas … card"); Who tells it ("Hermas's vision stays in his voice (card only)"); Do not say: no identification of Clement, and not "Grapte, a deaconess" (the editor's guess, 1011-1024).

11. **sources[8], Pliny (two modern words that contradict the brief; and new: Cut first 9, 21).**
    Old: "investigating Christians in Bithynia, including the torture of two enslaved women called ministrae — deaconesses."
    New: "investigating Christians in his province, including the torture of two enslaved women called ministrae, servers."
    Added at the end: "Those who had left told him that they also bound themselves by oath against theft, robbery and adultery, and came together again later for everyday, innocent food, which they gave up after his edict against clubs. Under torture, he wrote, he found only a depraved superstition without measure."
    Evidence: the brief, "Pliny governed a Roman province" and "They were called ministrae, servers". Outline, Do not say: Pliny "the Roman governor of Bithynia" or any named province → the place rests only on McGiffert's note (npnf201 19457); "two deaconesses" → "ministrae, servers" ("the 1890 translator's word"). Kit Part 1, Rigor: an identification only a modern work makes stays out of the card. Cut first 9 ("for the card"), mirbt 2791-2795, npnf201 19494-19502; Cut first 21 ("for the card"), mirbt 2797, npnf201 19505-19506. Worded apart from the pliny-the-younger story's sentences (Do not say).

12. **sources, six new items (references the brief draws on; and Cut first 3, 6, 14, 22, 23).** Each with `type` "primary" and `file`:
    - Ignatius, Epistles to the Magnesians, Philadelphians and Smyrnaeans, and to Polycarp (anf01): the brief's "act as one around its bishop", "greeted households", "messengers or letters to Antioch" and "wrote to the churches of Asia" (5851-5856, 8274-8276, 8503-8508, 8854-8869; from Smyrna, 6221, and Troas, 7914, 8467). For the card: the bishop in the place of God and the elders in the place of the apostles' council (Cut first 22), a proper thanksgiving the bishop's (Cut first 14, 8274-8289), Tavias and the wife of Epitropus (Cut first 3).
    - Justin, First Apology in Greek, Rauschen (1apol-grc): Quote 2's original.
    - Eusebius, Church History, Books III-V, tr. McGiffert (npnf201): the brief's Dionysius sentence (25109-25117) and Easter sentences (31136-31140, 31217-31222, 31262-31265, 31415-31419, 31527-31553); Pliny's English (McGiffert's note, 19457-19512); Rome's letter in Clement's time and its public reading (16634-16636, 16679-16684). For the card: Rome's gifts to churches in every city and to Christians in the mines, with no reason given (Cut first 6, 23; Words to explain, the mines; 25099-25107), Rome's new letter read on the Lord's day and Soter's name (Cut first 23; 25082-25094, 25113-25116).
    - Irenaeus, Against Heresies III.3 (anf01): the brief's "Rome's line of bishops, which carried the apostles' teaching to his day" (39823-39853). The "twelfth place" line is not quoted (barred, irenaeus-of-lyon).
    - Athanasius, Festal Letter 39 (npnf204): edit 4.
    - Jerome, Chronicle, Latin, Fotheringham (jerome-chron): the brief's "early in the second century" and "governed a Roman province" (42193-42262, 42246-42247: "Plinius Secundus, cum quandam prouinciam regeret", after the entries for Trajan's tenth year).
    Not added: anf05 (its endnote only confirms Quote 1's Latin; named in that entry's `uncertain`), anf09 (1 Clement complete; nothing on the card rests on it alone), routh (Dionysius in Greek, OCR damaged and not checked against a page image; the card gives Dionysius in English only).

13. **uncertain (new: the debates among the old sources, Kit Part 1, Accessibility; Source_Sheet §5; Outline, Ending).** Five items:
    - Who led them: Ignatius, Rome's letter, Polycarp, Hermas and Irenaeus each name the leaders differently (Source_Sheet §5, "Who led"; I1, C4, P1, S6, H1, H2, V1, V2). No modern view (Lampe's) is given: Outline, Who tells it, "stays out of the story and card wording".
    - The thanksgiving: the manual's cup first, Justin's bread and mixed cup with Jesus's words, Ignatius's bishop (Source_Sheet §5, "The thanksgiving"; D8, J3, J6, I3).
    - Who wrote Rome's letter: in the church's name; Dionysius first names Clement; Irenaeus and Eusebius follow (Source_Sheet §5; S1, R2, S2, S3; Outline, Beat 7).
    - Pliny's sources: people who had left, and two women under torture (Source_Sheet §5; Outline, Who tells it; L3, L5). Cut first 16 left this out of the story only.
    - How the Easter quarrel ended: only the bishops' rebuke and Irenaeus's peacemaking are held (Outline, Ending 1 and Do not say; npnf201 31431-31434, "the things of peace", and 31659-31666).

Every Cut first item marked for the card is now on it: 2, 3, 4, 5, 6, 7 (edits 6 to 12); 9, 10, 11, 12, 13, 14, 15, 18, 19, 21, 22, 23, 24, 28, 31. Item 32 was sent to the card by `Fixes_Grade2.md`, but `Recheck_Grade2.md` withdrew it and the brief keeps the words; the outline now marks it Leave out. Cut first 8 is Leave out. The outline's Leave out items marked "card" (the travelling apostles; "not as common bread") are in edits 7 and 9; the modern dispute over Ignatius's letters is already in `sourcing`. Nothing in `Fresh_Read.md` or `Review.md` sends anything else to the card: the review's "appoint their own bishops" cut is Cut first 28.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **why:** edit 1.
2. **relationsSummary:** no change. "The earliest layer on the map, which most later traditions claim as their root" is a statement about the tree; the brief does not contradict it. Its second half is listed below as not found.
3. **teaser:** the entry has none; none is added.
4. **sourcing, floorNote:** no change (listed below where a claim is not found).
5. **voices, legacy, sources:** edits 2 to 12. These live on the entry; the card file holds them.
6. **uncertain, quotationOriginals:** new on the entry (edit 13 and Quotations).
7. **entry.tile, entry.intro, entry.summary, entry.recordHolds:** in `Entry_Texts.md`.
8. **modernWorks (new):** the printed editions and translations the outline used to read its old texts (Source_Sheet, Short names). No modern work is now in the card's `sources`, so none moves.

```json
[
 {"title": "The Apostolic Fathers with Justin Martyr and Irenaeus (Ante-Nicene Fathers, volume 1)", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1885", "note": "English translations of Rome's letter to Corinth, the letters of Ignatius and Polycarp, Justin's First Apology and Irenaeus's Against Heresies, with the editors' notes."},
 {"title": "Fathers of the Second Century: Hermas, Tatian, Athenagoras, Theophilus, and Clement of Alexandria (Ante-Nicene Fathers, volume 2)", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1885", "note": "English translation of the Shepherd of Hermas, with notes."},
 {"title": "Fathers of the Third and Fourth Centuries: Lactantius, Venantius, Asterius, Victorinus, Dionysius, Apostolic Teaching and Constitutions, Homily, and Liturgies (Ante-Nicene Fathers, volume 7)", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1886", "note": "English translation of the Didache, with an introduction on its discovery and notes on its words."},
 {"title": "Eusebius Pamphilius: Church History, Life of Constantine, Oration in Praise of Constantine (Nicene and Post-Nicene Fathers, second series, volume 1)", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes on its dates and sources, among them an English version of Pliny's letter on the Christians."},
 {"title": "Athanasius: Select Works and Letters (Nicene and Post-Nicene Fathers, second series, volume 4)", "author": "Archibald Robertson (ed.)", "year": "1892", "note": "English translations of Athanasius's works and festal letters, among them the thirty-ninth, on the books to be read."},
 {"title": "S. Iustini Apologiae duae (Florilegium Patristicum 2)", "author": "Gerhard Rauschen (ed.)", "year": "1911", "publisher": "Peter Hanstein, Bonn", "note": "The Greek text of Justin's two Apologies."},
 {"title": "Quellen zur Geschichte des Papsttums und des römischen Katholizismus, third edition", "author": "Carl Mirbt (ed.)", "year": "1911", "note": "A source book in Latin and German that prints Pliny's letter on the Christians and Trajan's reply."},
 {"title": "Eusebii Pamphili Chronici canones, latine vertit, adauxit, ad sua tempora produxit S. Eusebius Hieronymus", "author": "John Knight Fotheringham (ed.)", "year": "1923", "note": "The Latin text of Jerome's version of Eusebius's Chronicle, with its table of years."}
]
```

Titles, years and editors are taken from each Library file's own title (`DC.Title`) or header, and the Source_Sheet's Short names; Robertson's role in NPNF2 4 is given as the sheet does not name it, and should be confirmed. Routh, anf05 and anf09 are left out, since nothing on the card rests on them alone. Rights: the Rauschen Greek is a CC BY-SA 4.0 digital edition (its file header) of a 1911 public-domain print; quoting one sentence of it in `quotationOriginals` carries the Perseus attribution with it (Build/worlds/_cross-world/CORPUS-USE.md governs), which release should confirm the page gives. Every other work listed is public domain by date.

## Not found (left in place)

- why: "Rome wrote at length" (1 Clement is long; no old source says "at length"; not contradicted).
- sourcing: "c. 107–117 CE traditionally" (Jerome's Chronicle puts Ignatius's death after Trajan's tenth year, jerome-chron 42193-42262, which is not a range); "its most vivid material leans on one contested corpus" (the finished brief's most vivid material is Pliny, the manual and Justin; a judgment, not contradicted by a held source); "no non-literate believer — the majority of this movement" (a modern judgment). The checker may judge the first against Kit Part 1, Rigor.
- floorNote: "two centuries before the Nicene Creed" (the brief runs to near the end of the second century; Nicaea is 325; a rough figure).
- relationsSummary: "which most later traditions claim as their root".
- voices[0]: "c. 107-117" (as sourcing); "seven letters to congregations" (one of the seven is to Polycarp, anf01 8529).
- voices[1]: "the earliest Christian writing outside the New Testament to survive" (the date of the Didache is unknown, anf07 12668-12672).
- voices[2]: "put to death at Smyrna around 155" (polycarp-of-smyrna's story; no held old source in this folder gives the year).
- voices[5]: "The gatherings met in their homes" (Outline, Do not say: "Do not say where they met"; the held sources show greetings to households, anf01 8503-8508, Hermas's bishops taking servants of God into their houses, anf02 4946-4952, and the Acts of Justin's meeting at his lodging, anf01 29302-29312, but no line says the gatherings met in members' homes). Not corrected, since no held source contradicts it; the checker may judge it against the Do not say.
- voices[6]: "it is the earliest outside evidence that women here held a formal title at all" (a judgment; Pliny says only "quae ministrae dicebantur").
- legacy: "Almost every Christian tradition claims a root in these early gatherings"; "trying to live out those instructions under local pressures gave the offices more concrete form"; "it was through this regular use in worship—not by an early decree—that these writings came to be heard alongside the ancient Jewish Scriptures". The last also carries a "not X but Y" turn, a dash and the stock word "enduring" (Kit Part 1, Craft); not an edit this role makes.
- sources[0]: "along his route to execution in Rome, c. 107–117".
- sources[1]: "the earliest Christian letter outside the New Testament" (as voices[1]).
- sources[2]: "from a single surviving manuscript".
- sources[3]: "around 155"; sources[6]: "c. 165".
- sources[7]: "by some congregations nearly treated as Scripture" (not checked here; the hermas story tells it, Outline, Do not say).

## Validator

A scratch copy of the census, with this card's fields merged into the entry and the brief as `longDescription`, run through `node tools/validate-census.mjs --skip-quotes`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries (short names). The full run with the quotation check was stopped by the machine for memory; that check runs only for persons and councils, so it does not reach this entry. The quotation check here is the scratch fold check under Quotations, and the same check found every quoted span in the card's prose (`legacy`, `uncertain`, the `sources` notes) in a cited file. The entry-level `modernWorks` above was not in the scratch run.
