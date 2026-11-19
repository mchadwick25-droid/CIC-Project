# R3 recheck: era 3 batch 8

Round 3, the last, ran in two parts, each by a fresh Opus agent that had not seen the drafting or rounds 1 and 2. The parts follow, unchanged.

## R3 recheck, part A: John Climacus, Liberatus of Carthage, Dionysius Exiguus, Marius of Avenches (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these files. I edited no profile file, made no git writes and made no web, paid or model calls. I used local scripts and read-only git only. The inputs were R2_recheck.md part A, R2_changes.md part A, `git diff 772e88c2` on the batch 8 folder, and a field-by-field card diff against 772e88c2 (script: `scratchpad/r3A_carddiff.py`). For every changed string I opened the cited lines in the vendored file again.

**Mechanical (all four), by script (`scratchpad/r3A_mech.py`).**

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card order, no empty fields |
|---|---|---|---|---|---|---|
| john-climacus (major) | 405 | 2:30 | 6.5 | 76.0 | yes (1 calmly, 1 warmly) | yes |
| liberatus-of-carthage | 325 | 2:00 | 8.4 | 60.9 | yes | yes |
| dionysius-exiguus (major) | 402 | 2:29 | 8.0 | 65.6 | yes | yes |
| marius-of-avenches | 324 | 2:00 | 7.6 | 66.6 | yes | yes |

No brief sentence runs past 24 words, and no card sentence outside `sources` runs past 25. Every `sources` file exists. `records.json` loads as JSON, and its entries for these four match the cards and briefs (the Bellarmine side now says "in 530"; the Oliger claim records the bracket; the Liberatus Garnier claim is in and the false absent_detail is gone). Process note, not a profile finding: the scratchpad copies in `scratchpad/records/` were not updated for john-climacus, liberatus-of-carthage and dionysius-exiguus, so they now differ from `records.json` and are stale. R2 asked for both to be carried. `records.json` is the one that ships.

---

### John Climacus

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-A-M1 (Ewald-Hartmann order; editors' role) | RESOLVED, with a new minor | "in a letter its editors, Paul Ewald and Ludwig Hartmann, date to 600" matches the card's source entry and Ewald-Hartmann l.7718-7719. To save one word, "Gregory's English translator" was cut to "His English translator", which opened a new ambiguity. See R3-A-M1. "If so, he argues" keeps Labbe's condition ("si vera narravit", PG88 l.41486). |
| R2-A-M2 (Rader on Bellarmine; two hard sentences) | RESOLVED | "Proinde vere Bellarminus (a) anno 530 collocavit" (PG88 l.41750-41752). `dates` split, condition kept. `uncertain` 2: "He then turns to the tale ... which brings in the death of Peter" is faithful. |
| R2-A-M3 (Angelo of Cingoli) | RESOLVED | "frater Angelus ... de Cingulo" (oliger1912 l.1790-1792), "Frater Gentilis de Cingulo" (l.1800), "loquitur de Clareno nostro" (l.1798), "[Angelus de Clareno]" in brackets (l.1816), "Angelus de Cingulo" (l.1845). "whom Oliger identifies as Angelo Clareno" holds. "quoted by" is right for these excerpts. |

#### Changed strings checked
- Brief P6, "If so, he argues": PASS. Brief P6, Ewald-Hartmann sentence: PASS. Brief P6, "His English translator": R3-A-M1.
- `knownFor`: PASS. `dates`: PASS ("Vixit ... circa annum 580", l.41328-41329).
- `legacy.traces` 0, 1, 2: PASS.
- `legacy.remembered` 0: the three quoted pieces match kempis l.12186-12190 word for word ("Climacusr" is OCR; the source's comma after "Will" stays outside the card's marks, which is correct). The last sentence lost its witness: R3-A-M2.
- `uncertain` 0: PASS. `uncertain` 1: "Still less, he says" PASS ("multoque minus de profectione ejus in coenobium, de tempore commorationis in eremo, de praefectura", PG88 l.41488-41492). Bellarmine sentence PASS. `uncertain` 3: PASS.

#### New findings
- **R3-A-M1 MINOR (brief P6 and audio; item 4; a pronoun that can point at the wrong man).** "Gregory the Great wrote to a John, abbot of Mount Sinai, in a letter its editors, Paul Ewald and Ludwig Hartmann, date to 600. His English translator, James Barmby, takes this John to be Climacus, still alive then." In a brief about John, heard aloud after three other men, "His" can be taken as John's translator. Barmby translated Gregory's letters (npnf213). The round 2 wording, "Gregory's English translator", was clear. It was cut to save one word. Fix: "Gregory's English translator, James Barmby, takes this John to be Climacus, still alive then." Scored: 405 words (same count), 2:30, FK 6.6, Flesch 75.6.
- **R3-A-M2 MINOR (card `legacy.remembered` 0; items 1, 5; a witness dropped in the split).** "Wise men marveled at how well he understood the book." now stands as the narrator's own statement. Thomas tells it: "so that wise men marvelled that he had so good an understanding of the book" (kempis l.12188-12190). The round 1 text had "Thomas says". Fix: merge the last two sentences: 'Ketel "expounded therefrom sentiments full of spiritual truth", Thomas says, so that wise men marveled at how well he understood the book.' (23 words.)
- **R3-A-M3 MINOR (brief P7 and audio; item 2; punctuation inside a quote; unchanged text, but the rule this round names).** '"Sometimes he read the book of John Climacus," Thomas writes.' The source has no comma there ("Climacusr" then the title, l.12186-12187). Round 2 fixed this on the card and left the brief. It cannot be heard. Fix: '"Sometimes he read the book of John Climacus", Thomas writes.' The score is unchanged.

#### Verdicts
- John Climacus: CLEAR (0 blocking, 3 minor).

---

### Liberatus of Carthage

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-A-B1 (Jean Garnier, a false absence) | RESOLVED | "notat Jo. Garnerius, præf. ad Libera tum" (PG100 l.435-436); "luculenter probavit Joannes Garnerius, Dissert. 4," (PG50 l.7867-7868). The absent_detail is gone and a Documented claim is in `records.json`. Brief P4: "Jean Garnier, whose edition Migne reprints"; card `dates`: "Jean Garnier says he wrote under Justinian". Both are the first mention in their texts. |
| R2-A-M4 ("shared to the end") | PARTLY | R2 gave "which Liberatus shared until his bishop died". R2_changes says it was "taken as worded", but the file reads "which he shared". After "Garnier takes ...", "he" points first at Garnier. See R3-A-M4. "in person" was dropped from P2. "came to speak for Reparatus" still renders "ut apud nos agerent uerbo" (Avellana l.24975). |
| R2-A-M5 (42-word sentence) | RESOLVED, with a new minor | Split as worded; "non nisi tamen post obitum Joannis ... legati solverunt ex Africa" (PL68 l.81394-81396). The "he says" in the new second sentence comes right after "he came to Rome twice", where "he" is Liberatus. See R3-A-M5. |

#### Changed strings checked
- Brief P2, P4, P5: PASS except R3-A-M4.
- `knownFor`: PASS. `keyWorks[0].about`: PASS.
- `dates`: facts PASS (Mommsen: "nam meminit mortis Vigilii c. 20 ... nam scripsit, ut ait ..., vivo Theodosio ... vivo Apollinare", chron-min-2 l.17568-17571). The split cut Mommsen's grounds loose from his dating: R3-A-M6.
- `legacy.traces[1]`: PASS. `legacy.remembered` 0: PASS ("fuit enim schismate implicatus propter tria Capitula obstinatius defensa", PL68 l.75143-75144). `remembered` 1: PASS. Dropping "many of" is closer to "monimenta unde plurima desumpsit magnam partem perierunt" (l.75153-75155). `remembered` 2: PASS ("aequales et conterranei et eiusdem sectae ... acerrimi orthodoxae fidei defensores", chron-min-2 l.17574-17575; the triad is Mommsen's own).
- `uncertain` 2: R3-A-M5. `uncertain` 4: PASS ("who ... lives" is correct). `uncertain` 5: PASS ("politicam episcoporum imperatori adulantium coitionem", PL68 l.74974-74975; "on this view" correctly marks it as the book's view as Garnier reads it).

#### New findings
- **R3-A-M4 MINOR (brief P5 and audio; item 4; the pronoun R2 asked to replace).** "Garnier takes the journey in Liberatus's preface to be this exile, which he shared until his bishop died." The subject is Garnier, so "he" first reads as Garnier. Fix, as R2 worded it: "...to be this exile, which Liberatus shared until his bishop died." Scored: 325 words, 2:00, FK 8.5, Flesch 60.1. That passes, but it is near the floor, so score again after any other change.
- **R3-A-M5 MINOR (card `uncertain` 2; items 1, 5; "he says" can point at Liberatus).** "...or he came to Rome twice. The envoys named in Agapetus's letter, he says, left Africa only after Pope John had died." The last "he" before it is Liberatus, but the reason is Garnier's. Fix: "Garnier says the envoys named in Agapetus's letter left Africa only after Pope John had died."
- **R3-A-M6 MINOR (card `dates`; item 4; Mommsen's grounds made to read as loose facts, in a choppy run).** "Theodor Mommsen dates the Breviarium between 555 and 567. It tells of the death of Pope Vigilius. Liberatus wrote while Theodosius, once bishop of Alexandria, and Apollinaris of Alexandria were alive." The reader no longer sees that the second and third sentences are the reasons for the dates (Mommsen's "nam ... nam", chron-min-2 l.17568-17571). Fix: "Theodor Mommsen dates the Breviarium between 555 and 567, since it tells of the death of Pope Vigilius. He adds that Liberatus wrote while Theodosius, once bishop of Alexandria, and Apollinaris of Alexandria were alive." (17 and 19 words.)

#### Verdicts
- Liberatus of Carthage: CLEAR (0 blocking, 3 minor). R2's one blocking finding is resolved.

---

### Dionysius Exiguus

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-A-M6 ("He asked him then") | RESOLVED | "He asked Dionysius to plead for them, so that those once upheld by his prayers might be helped by his merits." "He" can only be Cassiodorus here. pl70 l.83601-83605. |
| R2-A-M7 (no recorded line for "Jean Garnier") | RESOLVED | The PG50 l.7868 witness is in the Proclus claim in `records.json`. Garnier's "Dissert. 4, post Marium Mercatorem" fits the card's Marius Mercator point. |

#### Changed strings checked
- Brief P13: PASS.
- `knownFor`: PASS. `keyWorks` 0, 1: PASS. `keyWorks` 2: PASS ("numbering the years" is right for his own five cycles, which start where Cyril's last ends).
- `legacy.traces[1]`: R3-A-M8. `legacy.remembered` 0: PASS. `remembered` 2: PASS ("fixed (erroneously, as it now appears) the era ... accepted by all the nations of Christendom", hodgkin1886 l.3431-3434).
- `uncertain` 0: PASS. `uncertain` 1: R3-A-M7. `uncertain` 2: PASS. `uncertain` 5: PASS ("qu'il présente comme la première qui en ait été faite et comme son œuvre personnelle, est tout simplement copiée sur celle de Marius Mercator (Maassen ...)", LP1 l.30095-30099).

#### New findings
- **R3-A-M7 MINOR (card `uncertain` 1; items 1, 7; "he says" on the disputed point can be read as Dionysius).** "Louis Duchesne, after Bruno Krusch, says Nicaea made no such ruling. Dionysius drew it, he says, from the letter of Proterius of Alexandria to Pope Leo." The sentence before names Dionysius as a speaker too ("Dionysius says the bishops of Nicaea fixed..."), so a reader can take "Dionysius drew it, he says" as Dionysius's own admission. It is Duchesne's charge: "c'est Denys qui l'a déduite, par une exégèse habile, de la lettre de Proterius d'Alexandrie au pape saint Léon" (LP1 l.16343-16345). Context favors Duchesne, so this is minor, but this was round 1's blocking dispute. Fix: "Duchesne says Dionysius drew it from the letter of Proterius of Alexandria to Pope Leo." The next sentence, "With Krusch, he calls it a pious fraud...", then reads cleanly as Duchesne.
- **R3-A-M8 MINOR (card `legacy.traces[1]`; item 4; a garden path and a sentence with no content).** "Abbot Ceolfrid writes in a letter that Bede gives in his Ecclesiastical History." This can be parsed as "Ceolfrid writes that Bede gives...". It also says nothing until the next sentence. Fix: "Abbot Ceolfrid wrote a letter that Bede gives in his Ecclesiastical History. In it he says that after Cyril of Alexandria, Dionysius added as many cycles again, reaching down to Ceolfrid's own time." (12 and 21 words.)

#### Verdicts
- Dionysius Exiguus: CLEAR (0 blocking, 2 minor).

---

### Marius of Avenches

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-A-M8 ("His years are disputed." opener; length) | RESOLVED | P7 now opens "From the epitaph and a church Marius dedicated, Mommsen reckons..." It follows on from the epitaph paragraph, and Mommsen has a full name in P1. 324 words, 2:00. The dispute is still shown (chron-min-2 l.20785-20790; pl72 l.59566-59568). The card keeps "His years are disputed." as a field label, which is the card's form. |

#### Changed strings checked
- Brief P7: PASS.
- `dates`: PASS ("obiit a. 594, vitae anno LXIII vel LXIV, id est natus a. 530 vel 531"; "annus autem obitus 601 ... et ... coepti episcopatus a. 581 reiciendi sunt", chron-min-2 l.20776-20786).
- `legacy.traces[1]`: PASS. Krusch's "ita ut vel conici possit" keeps the hedge ("may have been"). "Both tell of" is true of both texts (krusch1888 l.459-464).
- `legacy.traces[2]`: PASS. Gallandi gives the "chronologicis notis satis destitutam" point and the "magnam lucem" point together as "sententia ... Chiffletii" (pl72 l.59608-59613), so "his view" and "Chifflet held" are both right.
- `legacy.remembered[2]`: PASS (l.20787-20789). `uncertain` 0: PASS. `uncertain` 3: PASS ("He" is Mommsen; l.20792-20795).

#### New findings
None.

#### Verdicts
- Marius of Avenches: CLEAR (0 blocking, 0 minor).

---

### Summary
- John Climacus: CLEAR (0 blocking, 3 minor).
- Liberatus of Carthage: CLEAR (0 blocking, 3 minor).
- Dionysius Exiguus: CLEAR (0 blocking, 2 minor).
- Marius of Avenches: CLEAR (0 blocking, 0 minor).

No blocking point is left open for a cap ruling. Every brief fix (R3-A-M1, M3, M4) has to be carried into the audio script. No card fix above is quoted in `records.json`.

---

## R3 recheck, part B: Martin of Braga, Brendan of Clonfert, Barhadbeshabba 'Arbaia of Halwan, Theopistus (era 3 Who batch 8)

Reviewer: independent Opus, seeing these files for the first time. I edited no profile file. I made no git writes and no web, paid or model calls. I used local scripts and read-only git only.

Method:
- I read `git diff --word-diff 772e88c2` for each of the four cards and briefs and for `records.json`. No brief changed except Barhadbeshabba's para 5.
- I opened the vendored lines myself for each R2 finding and each changed string.
- I ran `grade_text` on each brief and checked by script that each audio file equals its brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph. The script also checked card key order, empty fields, source files and card sentences past 25 words.
- I applied the coordinator's framing for Barhadbeshabba and Theopistus, and both hold.

Mechanical results:

| Profile | Words | Time @162 | FK | Flesch | Audio = brief | Card |
|---|---|---|---|---|---|---|
| Martin of Braga | 336 | 2:04 | 7.5 | 67.0 | yes | order pass; no empty fields; files exist; only `place` (a list of places) past 25 |
| Brendan of Clonfert | 331 | 2:03 | 6.5 | 74.4 | yes | order pass (no keyWorks, absent); no empty fields; files exist; only a source title at 26 |
| Barhadbeshabba 'Arbaia of Halwan | 327 | 2:02 | 6.4 | 72.9 | yes | order pass; no empty fields; files exist; none past 25 |
| Theopistus | 304 | 1:53 | 7.3 | 70.0 | yes | order pass; no empty fields; files exist; only `place` (a list) past 25 |

`records.json` loads as JSON and carries the R2 changes for all four ids.

---

### Martin of Braga

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-B-B1 (Dumio/Mondonedo dispute) | RESOLVED | `place` now names only Caspari's "near Braga". New `uncertain` item "Dumio and Mondonedo" checked against arndt-krusch1885 l.18215 ("primo Dumiensis monasterii (Mondonedo), tum Bracarensis") and acta-sanctorum martii-3 l.31808-31821: monks "Dumienses fugisse in Asturicos montes, et non longe a Mindoniensi urbe exiruxisse aliud monasterium, et Dumiense etiam appellasse", after the capture by the Moors ("captos fuisse a Mauris"). Again at l.32027-32030. The body was "in ejus antiqua Dumiensi reconditum ecclesia", raised, reburied, found and "Bracarum anno MDCVI translatum". "Stayed in the old church of Dumio until it was moved to Braga in 1606" is a fair summary. The old contested claim is gone from the records and a plain claim has replaced it. |
| R2-B-M1 (Mommsen's "585?") | RESOLVED | mommsen1894 l.20238 "5b5?" (OCR). The card now says "with a question mark". |
| R2-B-M2 ("is said to have met") | RESOLVED | arndt-krusch1885 l.46022-46025 "simul cum ipsis pignoribus Galliciae portum ingressus sit". |
| R2-B-M3 ("tells of his coming") | RESOLVED | l.46021 "qui ibidem nunc sacerdos habetur". "Wrote of" fixes the ambiguity. |

#### Changed strings checked
- `knownFor`, split at "faith.": R3-B-M1.
- `place`: PASS.
- `uncertain` 1 ("wrote of"): PASS.
- `uncertain` 2, three-way split: R3-B-M2.
- `uncertain` 3, split: PASS. "Hold" and "about twenty" are kept. The R. note is at l.18215-18216: "non 30, sed 20 circiter annis".
- `uncertain` 4, split ("It was held in King Ariamir's third year"): PASS. "It" is the council.
- `uncertain` 6 (new): PASS.
- `uncertain` 8 (Mommsen): PASS.
- `uncertain` 9: PASS.
- records (Dumio claim; Mommsen witness): PASS.

#### New findings
- **R3-B-M1 MINOR (card `knownFor`; item 4; a pronoun pointing at the wrong man after the split).** The text now reads: "Isidore of Seville ties him to the Sueves' turn from the Arian teaching to the Catholic faith. He led the Second Council of Braga…". The subject of the sentence before is Isidore, so "He" reads first as Isidore. Isidore did not lead the council of 572. Fix: "Martin led the Second Council of Braga and wrote a sermon against the pagan customs of country people."
- **R3-B-M2 MINOR (card `uncertain` 2; items 1, 4; the split cut Krusch off from the claim he owns).** "Many have made Chararic and Theudemir one man." now stands as the narrator's own claim. It comes from Krusch's note: "unde plerique Chararicum eundem ac Theudemirum fuisse coniecerunt" (arndt-krusch1885 l.45634-45636). "Coniecerunt" means guessed, and "made … one man" firms it up. Fix: "Many, Krusch says, have guessed that Chararic and Theudemir were one man."

#### Verdicts
- Martin of Braga: CLEAR (0 blocking, 2 minor).

---

### Brendan of Clonfert

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-B-B2 (Williams as a witness to the join) | RESOLVED in the card; records see R3-B-M3 | `uncertain` 2 now ends "setting Brenainn maccu Altai at Clonfert". gildas williams1899 l.9110-9112 is now a plain claim in the records. |
| R2-B-M4 ("saints and patriarchs") | RESOLVED | stokes l.21208-21219 lists Abraham, David, Solomon, Moses, Hieronymus, Augustine, Origen, John, Matthew, Paul, Peter, John the Baptist, Gregory of Rome and Noah. "Figures from the Bible and the church" fits them all. |
| R2-B-M5 (editor's Birr gloss) | PARTLY | The gloss is now marked as the editor's: annales-cambriae l.2501 "Brendan ^ Byror dormitatio"; preface l.884-893 "the death of Brenda, abbot of Birre". The wording "their editor" brings in a new pattern fault, R3-B-B1. |

#### Changed strings checked
- `place` ("of the Altraige Caille."): PASS. stokes l.21224 "Of Ciarraige Luachra was he, of Altraige Caille".
- `remembered` 3, split ("They run from Abraham to Gregory of Rome, and last to Noah."): PASS.
- `uncertain` 2: deletion PASS. The split "John O'Donovan, from the Calendar of the O'Clerys, gives 572." also PASS.
- `uncertain` 4: R3-B-B1.
- records (Annales claim and absent detail name John Williams ab Ithel; Vita c.15 claim no longer carries Williams): PASS.
- records (contested claim side 3): R3-B-M3.

#### New findings
- **R3-B-B1 BLOCKING (card `uncertain` 4; item 5; a role stands in for a named witness).** "…whom their editor takes for Brendan of Birr." The pattern's witness rule says "Never 'his editor', 'the translator' or 'a modern scholar'", and checklist item 5 says the same. The witness is named in the file: "THE REV. JOHN WILLIAMS AB ITHEL" (l.263), whose preface gives "Brenda, abbot of Birre" (l.892-893). The card's own source title also names him. The records already name him, so the fix touches the card only. Fix: "The Annales Cambriae record only the death of a Brendan \"Byror\", whom John Williams ab Ithel, who edited them, takes for Brendan of Birr."
- **R3-B-M3 MINOR (records, contested claim "That Adomnan's Brendan Mocu Alti is the founder of Clonfert", side 3; item 1; the R2 fault moved to a new witness).** Williams was replaced on this side by the Bollandist note "Cluain ferta … a S. Brandano conditum" (acta-sanctorum augusti-1 l.58935-58938). Like Williams, the note says only that a Brendan founded Clonfert. It says nothing of Adomnan or Mocu Alti, as R2_changes itself notes. The card is not affected. Fix: drop the Bollandist note from that side, so the side reads "Book of Lismore story: 'Brenainn maccu Altai was in Clonfert' (stokes lismore1890 l.878-881)". Add the note as a plain claim beside Williams's: "Bollandist note: Cluain ferta founded by S. Brandano; says nothing of Adomnan's Brendan Mocu Alti".

#### Verdicts
- Brendan of Clonfert: NOT CLEAR (1 blocking, 1 minor). The blocking fix is a few words in one card string, so length, readability and audio are unchanged.

---

### Barhadbeshabba 'Arbaia of Halwan

Framing check: the bishop of Halwan is the writer of the Cause. The History goes to "Barhadbeshabba 'Arbaia, a priest of the school of Nisibis", and Nau's one-man view is told as his ("He thinks it not impossible…"). All of this holds in the brief and card.

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-B-M6 ("the school" with no antecedent) | RESOLVED | Brief and audio para 5 now name "the school of Nisibis". Seert (scher1919) l.28671-28673: the students left over Sabrisho's choice of "celle de Hnana". "Environ trois cents" and "Parmi ceux qui sortirent de l'Ecole de Nisibe" are at l.28720-28730. Para 6's "the same school" now has its referent. "It names among them" still points to the Chronicle. |
| R2-B-M7 (Guidi's man) | RESOLVED | guidi1903 l.1975-1976 "Bàr Hadhbésabba urbis Holwan". `dates` now reads "names a Bar Hadbeshabba of Halwan". |
| R2-B-M8 (long card sentences) | RESOLVED; one split hardened a hedge, R3-B-M4 | `remembered` 3 matches Abdisho's five items (BO III.1 l.30771-30794, "de causa Sectatorum Mar Diodori"). `uncertain` 8 was split, see R3-B-M5. |

#### Changed strings checked
- Brief and audio para 5: PASS.
- `knownFor`, split: PASS. "It" is the Cause. Scher: "le premier ouvrage qui nous retrace l'histoire de la plus célèbre de toutes les écoles", scher1908 l.16878-16894.
- `dates`: PASS.
- `keyWorks` `about`, split: PASS.
- `traces` 1, split: PASS. "Très précieux" is at l.16878-16894. "Ayant écrit son traité à la fin du vi siècle", trusted over Sourin on the forty-five years, is at l.21724-21726.
- `remembered` 1, split: PASS.
- `remembered` 3: PASS.
- `uncertain` 1, split: PASS.
- `uncertain` 4: R3-B-M4.
- `uncertain` 9 (Namesakes): R3-B-M5.
- records: PASS.

#### New findings
- **R3-B-M4 MINOR (card `uncertain` 4; items 1, 4; a hedge firmed up by the split).** "If so, he wrote the History young and the Cause in old age." Nau says only that it is enough to suppose this: "Il suffit de supposer qu'il a ecrit « l'Histoire des saints Peres » dans sa jeunesse … et … la Cause … dans sa vieillesse" (po09 l.31601-31607). The old "who would then have written" kept it as his supposition. Fix: "For that, Nau says, it is enough to suppose he wrote the History young and the Cause in old age."
- **R3-B-M5 MINOR (card `uncertain` 9; item 1; the split cut the chronicles off from their claim).** "Sabrisho of Lashom, head of the church, wanted him as his successor." now stands as the narrator's own fact. It is the chronicles' claim. Seert: "avait recommandé aux fidèles de choisir Barhadbsabba le moine" (scher1919 l.29180-29181). Mari: "mandavisset in patriarcham assumi Barhadbsabba monachum" (gismondi1899 l.13591-13592). Fix: "They say Sabrisho of Lashom, head of the church, wanted him as his successor."

#### Verdicts
- Barhadbeshabba 'Arbaia of Halwan: CLEAR (0 blocking, 2 minor).

---

### Theopistus

Framing check: the narrator's account is told as the book's account. Nau's reworking view sits at the center, with his hedges kept ("he thinks", "probably", "in his view", "the most likely answer for now", from "la solution suivante comme la plus probable pour l'instant", l.578-579). This holds.

| R2 finding | Verdict | Evidence |
|---|---|---|
| R2-B-M9 ("those" with no noun; long sentences) | RESOLVED | `uncertain` 1: "the stories in Dioscorus's favor" renders "récits en sa faveur" (l.582). "Probably in Greek" renders "sans doute rédigé en grec". "The Syriac comes from that Greek, in his view" matches "ce remaniement grec fut traduit en syriaque". `uncertain` 3: the Crum note is at l.17172-17176 ("ils serviront à rechercher avec plus de sûreté quel est le texte original"). `uncertain` 6: "C'est le nom Ibérien de Pierre, évêque de Maiouma, près de Gaza" is at l.15346-15347. |

#### Changed strings checked
- `keyWorks` `about`, split: PASS.
- `traces` 2, split: R3-B-M6.
- `uncertain` 1: PASS.
- `uncertain` 2, split ("…after 512, Nau says. Severus was patriarch of Antioch from 512 to 518."): PASS. l.484-487 and note l.498 "Sévère fut patriarche de 512 à 518". The reason still reads clearly from the order of the sentences.
- `uncertain` 3: PASS.
- `uncertain` 6, both splits: PASS. Budge stays on the Sne deacon, and Nau stays on Nabarnougios.
- records: PASS.

#### New findings
- **R3-B-M6 MINOR (card `traces` 2; item 4; "is said" with no owner, made by the split).** "A Coptic sermon … is said to have been spoken by Dioscorus in exile." The sermon's own heading makes the claim: "Eloge que prononça … le saint Dioscore … du temps que le roi Marcien l'avait exilé à Gangres" (Nau l.798-801). R2 raised the same ownerless "is said" on Martin (R2-B-M2). Fix: "A Coptic sermon in praise of Macarius, bishop of Tkow, says in its heading that Dioscorus spoke it in exile."

#### Verdicts
- Theopistus: CLEAR (0 blocking, 1 minor).

---

### Summary

| Profile | Verdict | Blocking | Minor |
|---|---|---|---|
| Martin of Braga | CLEAR | 0 | 2 (R3-B-M1, M2) |
| Brendan of Clonfert | NOT CLEAR | 1 (R3-B-B1, "their editor" for John Williams ab Ithel) | 1 (R3-B-M3, records) |
| Barhadbeshabba 'Arbaia of Halwan | CLEAR | 0 | 2 (R3-B-M4, M5) |
| Theopistus | CLEAR | 0 | 1 (R3-B-M6) |

Every fix above is to card or records text only. No brief, audio, length or readability score changes. Cap note: this is the third review file on these documents. R3-B-B1 is a one-phrase fix that can be applied as worded. If it is left open, it goes to Mark for a cap ruling.

---
