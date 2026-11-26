# Card edits: The Second-Century Greek Apologists

Starting card: `Card.existing.json` (the census entry's card fields; a tradition has no `card` field). New card: `greek-apologists-second-century.card.json`. Brief: `greek-apologists-second-century.brief.txt` (final after `Grade2_Fixes_Applied.md`; no `Grade_Fixes_Applied.md` exists in this folder). Every field and item not listed below is word for word, in the same order. The new keys (`uncertain`, `sources`, `quotationOriginals`) come at the end, and each documented story gains `modernWorks`.

## How a tradition's card is shaped here

As for the sibling traditions in this batch (`roman-church-third-century/Card_Edits.md`): `tools/validate-census.mjs` refuses a `card` on anything but a person, and checks `quotationOriginals` only for persons and councils. So the card file keeps the tradition entry's own fields, and:

- `sources`: the tradition entry's own list (`work`, `type`, `note`), with `file` added to each item so each quotation ties to a cited file.
- `quotationOriginals`: the `cyril-and-methodius` format, at the top level. The validator does not check it for a tradition, so a scratch check (the validator's `fold` and `wordingFault`, re-implemented outside the repository) confirms each `modern` is one of the brief's quoted spans, each `printed` and `englishPrinted` stands at its lines, and each file is among `sources`. All pass.
- `uncertain`: a list, as on a person card.
- Each documented story's modern work moves to that story's own `modernWorks`.

For release: no page home and no validator check exist yet for a tradition's `uncertain` and `quotationOriginals`.

## Quotations

The brief quotes three spans; each has one entry. All three run six words or more (29, 43 and 34 words), so none carries `secondReading` and none is "checked at card".

1. **Q1, Melito.** Printed (English; Eusebius's Greek for Book IV is held only in the damaged Otto 1872 scan, so the English stands alone): `npnf201` 25826-25829, "If these things are done by thy command, well and good. For a just ruler will never take unjust measures; and we indeed gladly accept the honor of such a death." Re-read. Work: Church History IV.26.5 (the passage stands in section 5 of the chapter, file line 25818). Its `uncertain` says the English stands alone and the words survive only as Eusebius copied them (Outline, Quotes 1; Who tells it).
2. **Q2, Athenagoras.** Printed (Greek, Otto 1857, clean): `athen-grc` 1546-1550, "Ἀλλ᾿ ἡμεῖς, πλησίον εἶναι ... φονεύειν δυνάμεθα;" (the milestone tag on 1546 is stripped by the check). English printed: `anf02` 13330-13349, "But we, deeming that to see a man put to death is much the same as killing him, have abjured such spectacles. How, then, when we do not even look on, lest we should contract guilt and pollution, can we put people to death?" (the editor's footnote 830, 13332-13347, falls between the two sentences; the check strips notes). The outline gives the English as 13328-13332, which holds only the first sentence. Greek checked by hand: πλησίον, near; ἀπηγορεύσαμεν, we renounced; ἅγος καὶ μίασμα, guilt and pollution. Its `uncertain` keeps the outline's Do not say point ("close to killing", πλησίον).
3. **Q3, Diognetus.** Printed (Greek, Lake 1917, clean): `diog-grc` 312-317, copied from the file with its own colons and the combining mark in πάνθ̓. The outline and sheet give 311-317; 311 is the section tag, and the words stand on 312-317. English printed: `anf01` 2735-2738. Both re-read. Greek checked by hand: πάροικοι, resident foreigners; πολῖται, citizens; ξένοι, strangers.

## Card fields

1. **why (claims the brief no longer makes; a modern date and a modern claim).**
   - Old: "For eighty years, Christian writers" New: "In the second century, Christian writers". Evidence: Outline, Do not say ("most quoted", "eighty years", "a dozen works" → none of these); brief: "In the second century, ... Christians who wrote in Greek put written defenses".
   - Old: "by arguing that Greek philosophy itself had been reaching toward Christ" New: "by asking to be judged by how they lived". Evidence: the approved-before-the-kit brief made this claim ("the best of Greek philosophy had been reaching toward what the church now held"); the finished brief does not, and Outline, Do not say bars "his Logos and seeds" here. New words from the brief: "they asked to be judged by how they lived" (athen-grc 196-198; 1apol-grc 506-516).
   - Old: "was executed for his teaching around 165" New: "was executed under Marcus Aurelius for refusing to sacrifice to the gods and obey the emperor's command". Evidence: brief, "Under Marcus Aurelius, Justin was condemned and put to death for refusing to sacrifice to the gods and obey the emperor's command" (anf01 29396-29398; npnf201 23749-23764); Outline, Do not say ("about 165" → "under Marcus Aurelius"). "for his teaching" contradicts the reason the Acts and the brief give.
   - Old: "A generation later, Theophilus of Antioch, writing to a pagan friend, became the first Christian author on record to call God by the word 'Trinity.'" New: "Theophilus of Antioch, writing to a pagan friend, counted back the years to show that the books of Moses were older than the Greeks' own." Evidence: "first" is only the ANF editor's note (anf02 8994; Source_Sheet §6; Kit Part 1, Rigor: a judgment only a modern work makes stays out of the card); "A generation later" is an order claim the outline bars (Do not say: "later" for Theophilus). New words from the brief (anf02 10155-10160, 10880-10885).

2. **teaser (claims the brief no longer makes).**
   - Old: "Eighty years of Christians" New: "Second-century Christians". Evidence: as edit 1.
   - Old: "that Plato had been half right" New: "that the Greek poets and philosophers had spoken of one God too". Evidence: the brief no longer makes the philosophy-reaching-toward-Christ claim; it says "Poets and philosophers, he said, wrote freely about God, and almost all spoke of one God" (athen-grc 311-318; anf02 11728-11735).

3. **voices[0] (modern date).** Old: "a defense around 124 and" New: "a defense and". Evidence: Outline, Do not say ("in 124" / "around 124" for Quadratus); Source_Sheet §6 (124 rests on a later reckoning by regnal year). Kit Part 1, Rigor.

4. **voices[2] (modern date).** Old: "beheaded about 165" New: "beheaded under Marcus Aurelius". Evidence: Outline, Do not say ("about 165" → "under Marcus Aurelius"); npnf201 23749-23764 (Eusebius places the death under Marcus); anf01 29396-29398 (the sentence: scourged, and led away to be beheaded).

5. **voices[3] (a modern judgment of praise).** Old: "with the most philosophically careful of the defenses" New: "and hailed them, above all, as philosophers". Evidence: no old source ranks the defenses (Kit Part 1, Rigor); athen-grc 72-74, τὸ δὲ μέγιστον Φιλοσόφοις; the brief, "hailed them, above all, as philosophers". This also carries Cut first 12 and 19 in part.

6. **voices[4] (a modern claim).** Old: "and was the first to use the word Trinity of God" New: "and used the word Trinity of God, his Word and his Wisdom". Evidence: anf02 8990-8996 ("types of the Trinity, of God, and His Word, and His wisdom"); "first" is only the editor's note (anf02 8994). Outline, Leave out (Trinity: card) and Do not say ("only a modern note says 'first'").

7. **voices[6] (a modern judgment).** Old: "anonymous, undated, and the most quoted of all of them" New: "anonymous and undated". Evidence: Outline, Do not say ("most quoted" → none of these); anf01 2483-2490 (no ancient testimony to the author).

8. **legacy (claims the brief no longer makes, and modern claims; what the outline sends to the card).**
   Old: "Justin Martyr argued that, before the incarnation, the Word was already sowing seeds of truth in the philosophers. That gave the church a way to deal with the learning it had inherited, and it has never fully put that down. Clement at Alexandria spoke the same way of philosophers receiving 'the seeds of the Truth'. He and Origen took the idea much further. The apologists also settled some of the church's words. Theophilus of Antioch is the first writer whose work survives to use the word Trinity of God. And one line from the Epistle to Diognetus has outlived all the others the movement wrote. It calls Christians resident aliens, at home everywhere and strangers everywhere."
   New: "At Alexandria, Clement praised Tatian, a hearer of Justin's, for his careful account of the age of Moses, the argument Theophilus also made. Theophilus of Antioch called the three days before the lights in the sky were made types of the Trinity, of God, his Word and his Wisdom. And the Epistle to Diognetus calls Christians resident aliens, at home everywhere and strangers everywhere."
   Evidence, sentence by sentence:
   - Sentences 1-4 (Justin's seeds, Clement's seeds, Origen): the claim the finished brief no longer makes (see edit 1); Outline, Do not say and Leave out ("his Logos and seeds" are justin-martyr's). Removed.
   - Sentence 5 ("settled some of the church's words") and 6 ("the first writer whose work survives"): rest on the editor's "first" (anf02 8994). Sentence 6 is now told with Theophilus's own figure, as Outline, Leave out asks ("a passing figure for the three days before the lights; told bare it implies 'first'"): anf02 8990-8992 ("three days which were before the luminaries, are types of the Trinity, of God, and His Word, and His wisdom"). Theophilus's own terms explain the word (Kit Part 1, Explain it; Source_Sheet §3, Trinity).
   - Sentence 7 ("has outlived all the others the movement wrote"): a modern judgment, and "movement" is barred (Outline, Do not say: "a movement", "most quoted"). Removed; sentence 8 kept, with "It" now "the Epistle to Diognetus".
   - New first sentence: Outline, What came of it 3 and Cut first 6 ("card"): anf02 29724-29727 ("the epoch of Moses ... discussed with accuracy by Tatian in his book To the Greeks"); anf01 33664 ("He was a hearer of Justin's"); anf02 10155-10160, 10880-10885 (Theophilus's argument).

9. **documentedStories[0].sources and [1].sources (moved: modern works).**
   Removed, word for word as they stood: `{"work": "Herbert Musurillo, The Acts of the Christian Martyrs (Oxford, 1972)", "type": "reference", "note": "Greek text of all three recensions with translation and dating discussion."}` and `{"work": "Peter Lampe, From Paul to Valentinus: Christians at Rome in the First Two Centuries (Fortress, 2003)", "type": "reference", "note": "Situates the case in Roman social history."}`.
   Added: each story's `modernWorks`, the same words split into `title`, `author`, `year`, `publisher` and `note`. Neither is held, so neither has a `url`. Evidence: the role ("a modern work now listed under the card's `sources` moves there word for word"). The checker may wish to recast Musurillo's note, which says "dating discussion" (what it covers) and stays within the rule.

10. **uncertain (new: what the outline sends to the card).** Six items:
    - Which emperor Aristides addressed. Outline, Do not say ("the Syriac heading and its editor's reading go to the card"); Source_Sheet §6; npnf201 21073-21075; anf09 19005-19008; 1apol-grc 68-69 (Justin's form of Antoninus Pius's names). Harris's modern reading is not given (Kit Part 1, Rigor).
    - What Aristides says of Christian life. Cut first 7 (card); Outline_Check M7 (strangers and the poor go with Aristides to the card); Do not say (fasting only with "the Syriac version adds"); anf09 18960-18964, 19597-19600, 19605-19608, 19589-19592, 18451-18462.
    - What Quadratus saw. Cut first 4 and its partial reversal ("raised from the dead" stays on the card); Do not say; Who tells it (Jerome: card only); npnf201 21056-21068; npnf203 39904-39906.
    - Whether a plot killed Justin. Cut first 3 (card); Source_Sheet §6; 2apol-grc 273-277; anf01 16849-16859; npnf201 23749-23764, 23781-23799.
    - Whether the emperors answered. Do not say ("Eusebius's Chronicle ties Hadrian's letter to Fundanus to a governor's letter, not to Quadratus (card)"); Cut first 5 (the father's letters to the cities: card); Who tells it (the Chronicle: card only); `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` 42525-42545 (the legate is "Serenus Gra-nius" in this print); npnf201 25888-25897.
    - Theophilus as bishop. Source_Sheet §1 (Widely Accepted: only Eusebius, and Jerome after him); npnf201 25228-25231; npnf203 40029-40032.

11. **sources (new: the old sources the brief and the card draw on).** Twelve items, each with `file`. The notes carry the remaining "for the card" items at their source:
    - Justin, First Apology, Greek (`1apol-grc`): the brief's atheism answer and taxes (186-188, 506-516). For the card: "and his sons" (Cut first 22; 68-75), "you can kill, but not harm us" told in plain words (Cut first 17; 94-96), Marcion and his followers not persecuted for their teaching (Cut first 21; 729-743, κἂν διὰ τὰ δόγματα, "still teaching" per Do not say).
    - Justin, Second Apology, Greek (`2apol-grc`): Crescens (Cut first 3; 273-277).
    - ANF 1 (`anf01`): the Apologies' English; Justin's report that servants were tortured (Leave out, "card"; 17182-17186, "our domestics, either children or weak women"); the Martyrdom's sentence at Rome on Justin and his companions (Cut first 11; 29270, "the prefect of Rome"; 29396-29398); Diognetus in English, with the haters who give no reason (Cut first 16; 2763-2765); Irenaeus on Tatian (33664).
    - Athenagoras, Greek (`athen-grc`): ruling together (Cut first 19; 72-74, dative plural), Armenia and Sarmatia (Cut first 12; 72-74), each people's gods and the Egyptians' cats and crocodiles (Cut first 15; 88-95), "with their wives and children" (Cut first 20; 181-182), no one claims to have seen it (Cut first 24; 1537-1538), not one slave has lied so (Cut first 14; 1538-1541), the throne from father to son (Cut first 13; 1601-1602).
    - ANF 2 (`anf02`): Athenagoras in English (13318-13349); Theophilus (7757-7762, 7780-7782, 8241-8246, 10155-10160, 10239-10246, 10880-10885, 10610-10614, 8990-8996); Clement on Tatian (29724-29727).
    - Diognetus, Greek (`diog-grc`): Q3 (312-317), infants (320-321), the haters (386).
    - Eusebius, Church History (`npnf201`): IV.3 Quadratus and Aristides (20992-20995, 21048-21068, 21073-21075), with "raised from the dead" (Cut first 4); IV.16 Justin's death and the plot (23749-23799); IV.24 Theophilus (25228-25231); IV.26 Melito (25471-25476, 25818-25897), with the father's letters to the cities (Cut first 5).
    - Otto 1872 (`otto1872`): second witness only, in a damaged scan (17518-17520, 20996-21029; Source_Sheet, Library sweep).
    - Jerome, Lives (`npnf203`): Who tells it (Jerome: card only); 39892-39906, 40004-40032.
    - Eusebius's Chronicle in Jerome's Latin: Who tells it (card only); 42525-42545.
    - Aristides (`anf09`): Cut first 1 and 7; What came of it 4; 18398-18403 (Harris, the convent of St. Catharine, Mount Sinai), 18416-18421, 18451-18462, 18960-18964.
    - Tertullian, Against the Valentinians 5 (`anf03`): the brief's Tertullian beat (43105, 43155-43163, 43233-43237); translator "Dr. Roberts" (42904).

Every Cut first item marked card is now on the card: 1, 3, 4 (with "raised from the dead"), 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 24. Leave out items marked card: Justin's report of tortured servants (anf01 note) and Theophilus's Trinity (legacy, voices[4], anf02 note). Do not say and Who tells it items marked card: the Aristides headings, the Chronicle and Fundanus, Jerome (uncertain, sources). Fixes_Grade2 item 4 ("Everywhere", for the card) was withdrawn by `Recheck_Grade2.md`, and the brief still says it, so it is not a card item.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **why:** edit 1 above.
2. **teaser:** edit 2 above.
3. **relationsSummary:** no change. It names the house churches, Justin at Rome, Theophilus at Antioch and Melito at Sardis, all of which the brief agrees with.
4. **sourcing, voices, legacy, documentedStories:** edits 3 to 9 above. These live on the entry; the card file holds them.
5. **uncertain, sources, quotationOriginals:** new on the entry, edits 10, 11 and Quotations above.
6. **documentedStories[0].modernWorks and documentedStories[1].modernWorks:** edit 9.
7. **livingEvidence.basis (a claim the brief no longer makes).** Old: "A circle of writers whose works are still read." New: "A number of writers whose works are still read." Evidence: Review B1 (no held source ties these writers to one another); Outline, Do not say ("a circle", "a group", "a movement" → "a number of Christians who wrote"). Not one of the short texts the role names; the checker may hold it back.
8. **modernWorks (new):** the printed editions and translations the outline used to read its old texts (Source_Sheet, header and abbreviations; translators from each file's own headings):

```json
[
 {"title": "Ante-Nicene Fathers 1: The Apostolic Fathers with Justin Martyr and Irenaeus", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1885", "note": "English translations of Justin's Apologies, the Martyrdom of Justin, the Epistle to Diognetus and Irenaeus, with the editors' notes."},
 {"title": "Ante-Nicene Fathers 2: Fathers of the Second Century: Hermas, Tatian, Athenagoras, Theophilus, and Clement of Alexandria", "author": "Alexander Roberts and James Donaldson (ed.); B. P. Pratten, Marcus Dods and William Wilson (tr.)", "year": "1885", "note": "English translations of Athenagoras's Plea, Theophilus's books to Autolycus and Clement's Stromata, with the editors' notes."},
 {"title": "Ante-Nicene Fathers 3: Latin Christianity: Its Founder, Tertullian", "author": "Alexander Roberts and James Donaldson (ed.); Alexander Roberts (tr.)", "year": "1885", "note": "English translation of Tertullian's works, among them Against the Valentinians."},
 {"title": "Ante-Nicene Fathers 9: The Gospel of Peter, The Diatessaron of Tatian, The Apology of Aristides and other works", "author": "Allan Menzies (ed.); D. M. Kay (tr.)", "year": "1896", "note": "English translation of Aristides's Apology from the Syriac and the Greek, with an account of how the Syriac was found."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 1: Eusebius, Church History", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes on its dates, names and sources."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 3: Theodoret, Jerome, Gennadius and Rufinus, Historical Writings", "author": "Ernest Cushing Richardson (tr.)", "year": "1892", "note": "English translation of Jerome's Lives of Illustrious Men."},
 {"title": "S. Iustini Apologiae duae (Florilegium Patristicum 2)", "author": "Gerhard Rauschen (ed.)", "year": "1911", "publisher": "P. Hanstein, Bonn", "note": "The Greek text of Justin's two Apologies."},
 {"title": "Athenagorae Philosophi Atheniensis Opera (Corpus apologetarum christianorum saeculi secundi 7)", "author": "Johann Karl Theodor von Otto (ed.)", "year": "1857", "publisher": "Mauke, Jena", "note": "The Greek text of Athenagoras's Plea."},
 {"title": "The Apostolic Fathers, volume 2 (Loeb Classical Library)", "author": "Kirsopp Lake (ed. and tr.)", "year": "1917", "publisher": "William Heinemann, London", "note": "The Greek text of the Epistle to Diognetus."},
 {"title": "Corpus apologetarum christianorum saeculi secundi 9", "author": "Johann Karl Theodor von Otto (ed.)", "year": "1872", "note": "The Greek fragments of Quadratus, Melito and other apologists, with a Latin translation."},
 {"title": "Eusebii Pamphili Chronici canones, in the Latin of Jerome", "author": "John Knight Fotheringham (ed.)", "year": "1923", "publisher": "Humphrey Milford, London", "note": "The Latin text of Eusebius's Chronicle as Jerome translated and continued it."}
]
```

The ANF years (1885 for volumes 1-3) are the American edition's; the files carry no year, and the sheet gives "ANF 1885-1896". The checker may confirm. Rights: all printed before 1931 (CORPUS-USE.md); the four Perseus Greek files are CC BY-SA 4.0 as digital editions, as on the live justin-martyr and marcion-of-pontus cards. Not added: Otto's Theophilus (1861), used only for its Latin as a second witness; Lucian's Peregrinus, which the sheet keeps for "the card's further reading at most" and which is an old work, not a modern one.

9. **For release, not edited (entry fields outside the role's list):** `dates` "c. 124-200" and `start` 124 carry the modern 124 the outline bars for Quadratus (Do not say; Source_Sheet §6).

## Not found (left in place)

- sourcing: "Roughly a dozen works in hand, which is more than several other traditions here have" (a count no held source gives; the outline bars "a dozen works" in the brief); that Diognetus survives "whole".
- teaser: "emperors who had them killed anyway" (Justin was condemned by the prefect Rusticus for refusing the emperor's command, anf01 29396-29398; no held source says the emperors these men addressed had them killed). The teaser's dash also falls under Kit Part 1, Craft ("no dash for drama"); not an edit this role makes.
- voices[0]: "the earliest" (Eusebius tells Quadratus first, npnf201 20992-20995, but does not call him the earliest).
- voices[1]: "lost for seventeen centuries" (the Greek survived unrecognized inside Barlaam and Josaphat, anf09 18416-18421; not contradicted for the work as a whole).
- voices[5]: Melito's "Paschal homily recovered in the twentieth century" (not held).
- documentedStories[0]: Rusticus "a Stoic, and one of Marcus Aurelius' teachers" (not in a held text used here); `when` "c. 165" and the caveat's three recensions (the caveat says the year is inferred; Musurillo, not held).
- documentedStories[1]: "written within months" (caveat).

## Conflicts

- Q1's `modern` keeps the brief's "honour" (British), as it must match the brief's quoted span; the role asks for American spelling. The printed English has "honor". For release or the brief's owner.

## Validator

A scratch census (outside the repository), with this card merged into the entry, the brief as `longDescription`, the `livingEvidence` change and the `modernWorks` above, through `node tools/validate-census.mjs <copy> --skip-quotes`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries (short names). The full run without `--skip-quotes` was killed for lack of memory; it would add nothing here, since the quote check reads only a person's or council's sources. The quotation check is the scratch fold check above.

## Spelling (2026-11-26)

`Card_Check.md` item 2: "honour" becomes "honor" in the brief and in the card's Q1 `modern` together (American spelling for modern renderings; the print reads "honor"). Applied by hand; backup `greek-apologists-second-century.brief.v6.txt`. Word count unchanged.
