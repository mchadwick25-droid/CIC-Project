# R2 changes: era 3 batch 8

Each part's findings were applied by the drafter of those profiles, who opened every cited line before changing it. After the findings, every card sentence over 25 words was split, with no fact, witness or hedge lost; those splits are listed in each part. The worker also restored the source punctuation in the John Climacus card's Thomas à Kempis quotations, where a split had ended a quoted fragment with a period inside the marks: the fragments now close outside the marks. The parts follow, unchanged.

## R2 changes, part A: John Climacus, Liberatus of Carthage (era 3 batch 8)

I opened every cited line again before each change. Audio scripts were rebuilt by script from their briefs and checked by script: each equals its brief plus `[calmly] ` at the start and `[warmly] ` before the closing paragraph. `records.json` was edited by a script that re-loaded the file just before writing. It replaced only `john-climacus` and `liberatus-of-carthage` (indent=1, ensure_ascii=False). Card sentences were checked by script: none now runs past 25 words. To meet that rule, 16 older card sentences in the two cards were split, with no change of content.

| Finding | Done |
|---|---|
| R2-A-M1 (Climacus brief: inverted order; editors given no role) | Taken. Ewald-Hartmann l.7718-7719 confirmed. Brief and audio: "Gregory the Great wrote to a John, abbot of Mount Sinai, in a letter its editors, Paul Ewald and Ludwig Hartmann, date to 600." The fix took the brief to 406, past the cap. To hold it, "Gregory's English translator" became "His English translator", and Labbe's "If it is true, he argues" became "If so, he argues". The condition is kept. 404 words. |
| R2-A-M2 (Climacus: Rader on Bellarmine; two hard sentences) | Taken as worded. PG88 l.41750-41752 ("Proinde vere Bellarminus (a) anno 530 collocavit", right after refuting Trithemius) confirmed. (a) Card `uncertain` 2: "Matthew Rader says Robert Bellarmine was right to place him in 530." The records' Bellarmine side and claim now say "in 530" and record that Rader endorses it. (b) Card `dates` split as worded. (c) Card `uncertain` 2: "He then turns to the tale as Antonius Magister retells it, which brings in the death of Peter, patriarch of Jerusalem." |
| R2-A-M3 (Climacus: Angelo of Cingoli is Oliger's identification) | Taken as worded. oliger1912 l.1788-1804 ("frater Angelus" and "Frater Gentilis de Cingulo"), l.1816 ("[Angelus de Clareno]", bracketed) and l.1845-1848 ("Angelus de Cingulo") confirmed. Card `legacy.traces` 2: "…credit the translation to Angelo of Cingoli, whom Oliger identifies as Angelo Clareno." The records' Oliger claim now records the bracket and Oliger's identification. |
| R2-A-B1 (Liberatus: "Jean Garnier" is held; a false absence) | Taken. PG100 l.435-436 ("notat Jo. Garnerius, præf. ad Liberatum") and PG50 l.7868 ("Joannes Garnerius, Dissert. 4, post Marium Mercatorem") confirmed. The false absent_detail was deleted from the records, and a Documented claim with both lines was added. Brief P4 and audio: "Jean Garnier, whose edition Migne reprints…". Card `dates`, Garnier's first mention in the card: "Jean Garnier says he wrote under Justinian." |
| R2-A-M4 (Liberatus brief: "shared to the end") | Taken as worded. PL68 l.75566-75568 ("non nisi post episcopi mortem ab Euchayda recesserit") and Avellana l.24976-24977 ("ut apud nos agerent uerbo") confirmed. Brief and audio: "…to be this exile, which he shared until his bishop died." To hold the length, "in person" was dropped from P2. |
| R2-A-M5 (Liberatus card: a 42-word sentence naming Garnier twice) | Taken as worded. PL68 l.81390-81395 confirmed. Card `uncertain` 3 is now two sentences. |

| Profile | Words | Time at 162 wpm | FK | Flesch |
|---|---|---|---|---|
| john-climacus (major, cap about 405) | 404 | 2:30 | 6.5 | 76.0 |
| liberatus-of-carthage (recorder) | 325 | 2:00 | 8.4 | 60.9 |

---

## R2 changes, part A: Dionysius Exiguus and Marius of Avenches (era 3 batch 8)

Each finding for these two ids, what was done, and where. Every cited line was opened in its vendored file before the change was made. Audio scripts were rebuilt by script from their briefs (`[calmly] ` at the start, `[warmly] ` before the closing paragraph). The script confirmed each one matches its brief once the two tags are removed, with one of each tag. Each final brief is identical to the reviewer's scored copy in `scratchpad/r2A/`.

`records.json` (in batch8) was edited by a script that re-loaded the file just before writing. It changed only `dionysius-exiguus` (indent=1, ensure_ascii=False). The `marius-of-avenches` record needed no change.

| Finding | Done |
|---|---|
| R2-A-M6 (Dionysius: "He asked him then" misleads) | Taken as worded in the brief and audio: "He asked Dionysius to plead for them, so that those once upheld by his prayers might be helped by his merits." pl70 l.83601-83605 ("Interveniat pro nobis … nunc meritis adjuvari") confirmed. |
| R2-A-M7 (Dionysius: no recorded line for "Jean Garnier") | Taken. PG50 l.7868 ("quod luculenter probavit Joannes Garnerius, Dissert. 4, post Marium Mercatorem") confirmed. It was added to the witness of the records' Proclus claim. No card text changes. |
| R2-A-M8 (Marius: "His years are disputed." thesis opener; length) | Taken as worded in the brief and audio. P7 now begins "From the epitaph and a church Marius dedicated, Mommsen reckons …". The dispute still shows in the paragraph (Mommsen against Conon, the annals and Gallandi; chron-min-2 l.20712-20786, pl72 l.59566-59568). Card `uncertain` 1 keeps its own wording, "His years are disputed.", as a card label. |

### Length and readability

From `engine.m1.gates.grade_text`, run from the repo root on the final briefs.

| Profile | Words | Time | FK | Flesch |
|---|---|---|---|---|
| dionysius-exiguus (major, cap about 405) | 402 | 2:29 | 8.0 | 65.6 |
| marius-of-avenches (recorder, about 325) | 324 | 2:00 | 7.6 | 66.6 |

### Sentence splits (before round 3)

`longsent.py` listed 20 card sentences over 25 words for these two ids (none in the briefs). Each was split with no fact, witness or hedge lost. Afterwards `longsent.py` lists none for either id. No records string quotes the changed card text, so `records.json` is unchanged.

| Card | Field | New wording |
|---|---|---|
| dionysius-exiguus | `knownFor` | Monk at Rome who put the church's canons into Latin from Greek copies and gathered the rulings of past popes. His Easter tables number the years from the Incarnation of Christ instead of from the emperor Diocletian. |
| dionysius-exiguus | `keyWorks[0].about` | Then come the canons of Nicaea and of the councils before and after it up to the council of Constantinople. Those of Chalcedon follow, and last the Latin canons of Sardica and of Africa |
| dionysius-exiguus | `keyWorks[1].about` | the decrees of past bishops of Rome, gathered for Julian, priest of the church of Saint Anastasia. William Cave says it runs from Siricius to Anastasius II |
| dionysius-exiguus | `keyWorks[2].about` | He set first the last cycle of Cyril of Alexandria, of which six years remained. Then he added five cycles of his own, numbering the years from the Incarnation |
| dionysius-exiguus | `legacy.traces[1]` | Abbot Ceolfrid writes in a letter that Bede gives in his Ecclesiastical History. After Cyril of Alexandria, he says, Dionysius added as many cycles again, reaching down to Ceolfrid's own time. |
| dionysius-exiguus | `legacy.remembered[0]` | Bede's On the Reckoning of Time is quoted in Migne's testimonia. There Bede calls him the venerable abbot of the city of Rome, learned in Greek and Latin. |
| dionysius-exiguus | `legacy.remembered[2]` | Thomas Hodgkin says Dionysius fixed the era of Christ's birth wrongly, as it now appears. His reckoning, Hodgkin adds, was accepted by all the nations of Christendom. |
| dionysius-exiguus | `uncertain[0]` | Janus also reports Jean Hardouin's view that the era was in use across the Christian world early in the fifth century, before Dionysius. Janus argues against it. |
| dionysius-exiguus | `uncertain[1]` | Louis Duchesne, after Bruno Krusch, says Nicaea made no such ruling. Dionysius drew it, he says, from the letter of Proterius of Alexandria to Pope Leo. |
| dionysius-exiguus | `uncertain[2]` | Johann Wilhelm Janus, in a letter printed in Migne's volume, says Cassiodorus was nearly the only one of his time to keep his memory. All later writers on his life followed him, Janus says. |
| dionysius-exiguus | `uncertain[5]` | William Cave lists Latin versions of Proclus of Constantinople under his name. He reports that Jean Garnier gave the sermon on the Mother of God to Marius Mercator instead. |
| dionysius-exiguus | `uncertain[5]` | Dionysius presents his Latin version of the Alexandrian council's letter against Nestorius as the first and as his own. Louis Duchesne, after Friedrich Maassen, says it is copied from that of Marius Mercator. |
| marius-of-avenches | `dates` | Theodor Mommsen reckons from his epitaph and from a church he dedicated that he became bishop in 574 and died in 594. That makes him sixty-three or sixty-four at death, born in 530 or 531. |
| marius-of-avenches | `dates` | Conon of Lausanne puts the start of his rule in 581. A later hand in the annals of Lausanne puts his death in 601. Mommsen rejects both. |
| marius-of-avenches | `legacy.traces[1]` | Bruno Krusch thinks the annals behind the Chronicle called Fredegar's may have been written at Avenches, where Marius wrote. Both tell of the duke Theudefrid and of the Lombards breaking into Burgundy. |
| marius-of-avenches | `legacy.traces[2]` | Andrea Gallandi reports his view that Gregory of Tours's History is poor in dates. Anyone who set the Chronicle beside it, Chifflet held, would find great light shed on Gregory. |
| marius-of-avenches | `legacy.remembered[2]` | Theodor Mommsen notes a book of the dead from Lausanne cathedral, written about 1510. It marks a procession on his day to the church of Saint Marius. |
| marius-of-avenches | `uncertain[0]` | Theodor Mommsen reckons 574 for his consecration and 594 for his death. He works from the epitaph and from the fourteenth year of his rule, when Conon says he dedicated a church at Paterniacum. |
| marius-of-avenches | `uncertain[0]` | Conon gives 581 for the start of his rule, and a later hand in the Lausanne annals gives 601 for his death. Mommsen thinks both come from an error about the year King Guntram died. |
| marius-of-avenches | `uncertain[3]` | Since Marius signs at Mâcon only for Avenches, Mommsen thinks it moved after him. He leaves open whether Marius wrote at Avenches or at Lausanne. |

---

## R2 changes, part B: Martin of Braga, Brendan of Clonfert (era 3 Who batch 8)

This table lists each finding for these two profiles, what was done, and where. Every cited line was opened in its vendored file before the change was made.

No brief changed in this round. The audio scripts still equal their briefs once `[calmly] ` and `[warmly] ` are removed, as checked by script.

The records changes are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch8/records.json`, under `martin-of-braga` and `brendan-of-clonfert` only. They were made by a script that re-loaded the file just before writing it (indent=1, ensure_ascii False).

A script check found no card sentence past 25 words after the changes. Three sentences found by that check were split: Martin `uncertain` 4, Brendan `place` and Brendan `remembered` 3. No git, web or paid calls were made.

| Finding | Done |
|---|---|
| R2-B-B1 (Martin: the Dumio/Mondonedo dispute that the sources do not make) | Taken as worded. The C-M7 change was replaced outright, not patched. Confirmed: arndt-krusch1885 l.18215 ("primo Dumiensis monasterii (Mondonedo)"); acta-sanctorum martii-3 l.31812-31821 ("non longe a Mindoniensi urbe exiruxisse aliud monasterium, et Dumiense etiam appellasse"; the body "in ejus antiqua Dumiensi reconditum ecclesia", moved to Braga "anno MDCVI") and l.32027-32030. Card `place` is now as worded. A new `uncertain` item 6, "Dumio and Mondonedo", is as worded. Records: the contested claim "Where Dumio was" was removed and a plain claim with these lines was added. |
| R2-B-M1 (Martin: Mommsen's "585?") | Taken as worded in card `uncertain` 8 (now numbered 8 after the insertion). Confirmed: mommsen1894 l.20238 (OCR "5b5?"). Records: the John of Biclaro witness notes the question mark. |
| R2-B-M2 (Martin: "is said to have met") | Taken as worded in card `uncertain` 9. Confirmed: arndt-krusch1885 l.46021-46025 ("simul cum ipsis pignoribus Galliciae portum ingressus sit"). |
| R2-B-M3 (Martin: "tells of his coming while…") | Taken as worded in card `uncertain` 1. Confirmed: arndt-krusch1885 l.46022 ("qui ibidem nunc sacerdos habetur"). |
| R2-B-B2 (Brendan: Williams made a witness to the Mocu Alti join) | Taken as worded in card `uncertain` 2. Confirmed: gildas williams1899 l.9110-9112, which names only "Brendan, who founded Clonfert". Records: Williams was removed from the contested side and replaced there by the Bollandist Clonfert note (acta-sanctorum augusti-1 l.58936-58941), which also does not name Adomnan. Williams stays as a plain claim that a Brendan founded Clonfert, and the Vita c.15 claim no longer carries his line. |
| R2-B-M4 (Brendan: "saints and patriarchs") | Taken as worded in card `remembered` 3, split at "church." for length. Confirmed: stokes lismore1890 l.21208-21219. |
| R2-B-M5 (Brendan: the editor's gloss of "Byror" as Birr) | Taken as worded in card `uncertain` 4. Confirmed: annales-cambriae l.2501 ("Brendan ^ Byror dormitatio") and l.892-893 ("Brenda, abbot of Birre"). Records: the absent detail and the Annales Cambriae claim now name the gloss as the editor's, John Williams ab Ithel's. |

No finding was declined.

#### Sentence-length pass (coordinator's scan, which counts a sentence joined by a semicolon as one)

| Sentence | Done |
|---|---|
| Brendan `uncertain` 2 ("Huyshe says the two must be kept apart…", 29 words) | Split at the semicolon into two sentences: Huyshe's 573, then "John O'Donovan, from the Calendar of the O'Clerys, gives 572." The wording is otherwise unchanged. |
| Martin `knownFor` ("Isidore of Seville ties him…", 35 words) | Split at the semicolon: "…to the Catholic faith. He led the Second Council of Braga and wrote a sermon…". The wording is otherwise unchanged. |
| Martin `uncertain` 2 ("Bruno Krusch says no one but Gregory…", 29 words) | Split into three sentences: Krusch's point that only Gregory names a King Chararic; "Many have made Chararic and Theudemir one man."; "Krusch judges Theudemir more likely Chararic's son." "Judges" and "more likely" are kept. |
| Martin `uncertain` 3 ("The Bollandists hold that a copyist…", 27 words) | Split at "and" into two sentences. "Hold" and "about twenty" are kept, and both witnesses are still named. |

A re-scan by the same rule finds no card sentence past 25 words except Martin's `place` (34 words). That field is a list of places separated by semicolons, in the form batch 6 uses for `place`, so I left it as it is.

---

## R2 changes, part B: Barhadbeshabba 'Arbaia of Halwan

I opened each cited line in its vendored file before making the change. The audio was rebuilt by script from the brief and matches it once the two tags are removed (checked with `diff`). `records.json` in batch 8 was edited only at `barhadbeshabba-arbaya`, by a script that reloaded the file just before writing (indent=1, ensure_ascii=False).

| Finding | Done |
|---|---|
| R2-B-M6 ("the school" with no antecedent) | Taken, in the reviewer's split form, because the one-sentence form runs to 26 words. Seert l.28707 ("environ trois cents") and l.28720 ("Parmi ceux qui sortirent de l'Ecole de Nisibe") confirmed. The brief and audio now read: "The Chronicle of Seert tells of a walk-out from the school of Nisibis. Some three hundred students left when the head of the church took Henana's side." The records claim on the walk-out now notes this. |
| R2-B-M7 (Guidi's man told as this man) | Taken as worded. guidi1903 l.1975-1976 ("Bàr Hadhbésabba urbis Holwan") confirmed. `dates` now says the chronicle "names a Bar Hadbeshabba of Halwan in the vacancy". The records claim on Guidi notes this. |
| R2-B-M8 (card sentences past about 25 words) | Taken as worded in `remembered` 3, `uncertain` 4 and `uncertain` 9. I left the unchanged long sentences that the reviewer listed but did not count as a finding. |

| Profile | Words | Time | FK | Flesch |
|---|---|---|---|---|
| barhadbeshabba-arbaya (before) | 323 | 1:59 | 6.5 | 72.3 |
| barhadbeshabba-arbaya (after) | 327 | 2:01 | 6.4 | 72.9 |

### Long-sentence pass (card)

Sentences that `longsent.py` listed, each split to 25 words or fewer with no fact, witness or hedge changed. No records string quotes this card text, so `records.json` is unchanged.

| Field | New wording |
|---|---|
| `knownFor` | Addai Scher calls it the first history of the school of Nisibis. It names the school's masters from Narsai of Nisibis to the author's own master, Henana of Adiabene. |
| `dates` | A chronicle Ignazio Guidi edited names a Bar Hadbeshabba of Halwan in the vacancy after Gregory's death. François Nau and Scher give that vacancy as 609 to 628. |
| `keyWorks[0].about` | the schools through which God taught angels and people, from Adam to the apostles and the schools of Alexandria and Antioch. It ends with the schools of Edessa and Nisibis, and the masters of Nisibis down to Henana of Adiabene. |
| `legacy.traces[0]` | Addai Scher calls the Cause's account of the schools of Edessa and Nisibis very precious. He calls it the first work to trace the history of the school of Nisibis. Since it was written at the end of the sixth century, he trusts it over later accounts on two points. These are Narsai's forty-five years at Nisibis, and Elisha, Narsai's successor, never being a bishop. |
| `legacy.remembered[0]` | An anonymous chronicle that Ignazio Guidi edited tells of the years after Gregory of Prat died. In those years, it says, Bar Hadbeshabba of Halwan won fame for writing books. |
| `uncertain[0]` | It rests on the title and words of the Cause and a signature in the synod of 605. It also rests on a line in the Chronicle of Seert and one in the chronicle Guidi edited. |

---

## R2 changes, part B: Theopistus (era 3 batch 8)

Before each change I re-opened the cited lines in `cic/texts/theopistus_histoire-de-dioscore-journal-asiatique-1903-fra_nau1903.txt` and confirmed them: l.578-595 (Nau's solution, "récits en sa faveur", "l'un des rhéteurs", "semble être une traduction du grec"), l.17175-17176 (the Crum note) and l.15346-15347 (Maiouma near Gaza). I also re-opened `coptic-apocrypha-upper-egypt-life-of-pisentius_budge1913.txt` l.1925 and 1969 (the Sne deacon, 985). The brief and audio are unchanged. The `theopistus` entry in `records.json` was edited by a script that reloaded the file just before writing (indent=1, ensure_ascii=False); no other id was touched.

| Finding | Done |
|---|---|
| R2-B-M9 (card `uncertain` 1: "those" with no noun; sentences past 25 words in `uncertain` 1, 3, 6) | Taken as worded, with one further split. In `uncertain` 1 the reviewer's last sentence ran to 28 words, so it now reads "After 512, he thinks, a writer trained in rhetoric, of the school of Peter the Iberian, reworked it, probably in Greek. The Syriac comes from that Greek, in his view." `uncertain` 3 is split as worded. In `uncertain` 6, sentence 2 is split as worded, and sentence 1 (34 words) is split the same way: "...as E. A. Wallis Budge reports. He is also a different man from the martyr Theopistus, son of Eustathius." The records claim on Nau's solution now notes the card wording. |

Card sentences still over 25 words, which the finding does not name and which were left as they are: `keyWorks` 1 `about` (29), `legacy.traces` 2, sentence 1 (27), and `uncertain` 2, sentence 1 (29). `place` is a list of places rather than a sentence. I can split any of these if the coordinator wants.

### Long card sentences split (coordinator's request)

Every fact and witness is kept. `place` is unchanged.

| Field | Done |
|---|---|
| `keyWorks` 1 `about` (29 words) | Split: "...to his death in exile at Gangra. A narrator who names himself Theopistus tells it." |
| `legacy.traces` 2, sentence 1 (27 words) | Split: "A Coptic sermon in praise of Macarius, bishop of Tkow, is said to have been spoken by Dioscorus in exile. It names the deacons Peter and Theopistus as its writers." (l.798-808) |
| `uncertain` 2, sentence 1 (29 words) | Split: "...puts the present text after 512, Nau says. Severus was patriarch of Antioch from 512 to 518." (Nau l.484-487, note l.498) |

---
