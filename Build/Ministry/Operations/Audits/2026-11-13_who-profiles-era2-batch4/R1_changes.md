# R1 changes: nine Who profiles, era 2 batch 4

What the drafters changed in answer to `R1_review.md`, in three parts by drafter. Each finding was checked against its vendored file before it was taken. The README finding (README-M1) was fixed by the coordinating worker: the README now says its ordering years are the scan's and gives the sources' years where they differ.

## R1 changes: Rufinus of Aquileia, Palladius of Helenopolis, Philostorgius

What the drafter changed in answer to `R1_review.md` (part A, Rufinus; part B, Palladius and Philostorgius). I checked each finding against its vendored file before acting on it. For every new or changed attribution, I opened the file and confirmed who speaks at that line. Edits went to the repo files in `Who-Profiles/era2/batch4/` only. `records.json` was edited by a script run under `flock`, which reloads the file inside the lock and touches only these three ids. Each audio script was rebuilt from its brief, with `[calmly] ` at the start and `[warmly] ` before the closing sentence only. The scratchpad `quotes.tsv` files were regenerated from the repo briefs and cards: 0 misses.

## Blocking

| Profile | Finding | Change |
|---|---|---|
| Palladius | B1: the brief told Jerome's "villainous slave" as settled about this Palladius. Epiphanius and Jerome were not placed as opponents. | Checked at npnf206 l.42611–42618: the note says "Tillemont, however, thinks that another Palladius may be referred to in these passages", and Jerome's text is "Palladius, no better than a villainous slave, tried to impart energy to the same heresy". The brief now reads: "Foes in the quarrel over Origen of Alexandria attacked him. Epiphanius of Salamis, in a letter Jerome of Strido put into Latin, warned that 'Palladius of Galatia' taught 'the heresy of Origen.' Jerome wrote that a Palladius, 'no better than a villainous slave,' tried to revive the same heresy. Notes to W. H. Fremantle's edition of Jerome take both for this Palladius. The historian Tillemont, they report, thought another Palladius may be meant." The notes are given to "Fremantle's edition", following his preface (Lewis and Martley "added most of the notes", l.492–494). In records.json, the Jerome claim and the Epiphanius claim are retagged Contested, their witnesses name the edition's notes, and a new contested_claim was added ("Whether the Palladius of Epiphanius's letter and of Jerome's prologue against the Pelagians is Palladius of Helenopolis"). Its sides are the edition's notes plus Clarke's note 241 (l.1119) for yes, and Tillemont for perhaps another. |

## Minor

- **Rufinus.**
  - M1: Checked at npnf202 l.13741–13742. Socrates speaks only of the attack on the monks. Card uncertain #7 now reads: "Socrates of Constantinople says only that Rufinus called himself a witness, and one of the sufferers, when the monks of Egypt were attacked." The records witness was changed the same way and adds "he says nothing of prison or exile".
  - M2: "the Recognitions of Clement of Rome" (Gennadius, npnf203 l.42472).
  - M3: Card dates now read "…in Sicily in 410, when he wrote his preface to Origen on Numbers; died there in 410, by the notes to Fremantle's edition of Jerome".
- **Palladius.**
  - M1: "follows Cuthbert Butler, who edited the Lausiac History, in giving it to Palladius" (Moore l.903–906).
  - M2: Card uncertain #4 now reads: "The notes to W. H. Fremantle's edition of Jerome take the Palladius of Epiphanius's letter and of Jerome's prologue for this man. They report that Tillemont, author of the Mémoires of 1707, thought 'another Palladius may be referred to in these passages'." The 1707 date is from Fremantle's Prolegomena (npnf206 l.1958), which Fremantle composed himself.
  - Trims to hold length after B1, all lines the card already carries: the Sozomen "disciple of Evagrius" sentence; "It tells of monks and holy women he met or heard of"; "He came from Galatia, he says" (Galatia is still in the Epiphanius quote); and "He made journeys of thirty days on foot to meet them". Two smaller trims: "The next day Palladius" became "Next day he", and "at the emperor's court" became "a court chamberlain". The closing quote is now framed "Its prologue says," so that the speaker stays named. I checked again that it is the Prologue (Clarke l.187) and not the Preface Butler doubts.
- **Philostorgius.**
  - M1: Taken in its shorter form, "against Porphyry of Tyre". The identifier rests on Socrates III.23, where Libanius is quoted saying "the Tyrian", and A. C. Zenos's note there reads "Porphyry" (npnf202 l.11733–11735). The records witness now gives this.
  - M2: Checked at Walford l.316: "him" follows Basil and Apollinaris and is left open. Card uncertain #4 now reads: "Photius reports his story that Eunomius answered a critic in five books, and that the critic died of remorse after reading the first. Walford's English leaves open whether Basil of Caesarea or Apollinaris of Laodicea is meant. Photius calls it falsehood."

## Own fix outside the findings

- **Rufinus, the npnf206 notes.** B1 showed that most notes in Fremantle's Jerome volume are by Lewis and Martley (npnf206 l.492–494). So the Rufinus lines that rested on npnf206 notes now name "the notes to Fremantle's edition of Jerome" in place of "Fremantle".
  - Brief: "Notes to W. H. Fremantle's edition of Jerome take the scorpion for Rufinus."
  - Card: the dates field and uncertain #8.
  - records.json: the scorpion claim, the death claim, and the death and Concordia absent_details.
  - The npnf203 notes and Prolegomena stay "Fremantle", because his title page there reads "Translated with Prolegomena and Notes, by … Fremantle".
  - To hold 405 words: "He also lived at Jerusalem" became "He lived at Jerusalem", and "the narrow strait" became "the strait".

## Not taken, with reasons

- **Philostorgius M1, the longer wording** "a pagan critic of the Gospels". The cited lines say only that Julian attacked the Christian books and outdid "the Tyrian". They do not call Porphyry a critic of the Gospels, so the short form was used.

## Reported, not changed

- Palladius is at 327 words and Philostorgius at 326, both within "about 325", as R1 accepted for Sulpicius.

## After the changes

| Profile | Words | Time @162 wpm | FK | Flesch | briefLength |
|---|---|---|---|---|---|
| Rufinus of Aquileia (MAJOR) | 405 | 2:30 | 7.6 | 61.9 | about 2 minutes 30 seconds |
| Palladius of Helenopolis | 327 | 2:01 | 7.5 | 60.3 | about 2 minutes |
| Philostorgius | 326 | 2:01 | 7.9 | 60.7 | about 2 minutes |

## R1 changes: era 2 batch 4, Pelagius, Paulinus of Milan, Possidius of Calama

What the drafter changed in answer to `R1_review.md`, part A (Pelagius, Paulinus) and part B (Possidius). Before acting on each finding, I checked it in its vendored file. Every changed attribution was opened at its line to confirm who speaks there. No quotation was added or changed. quotecheck finds 0 misses on all three against the repo briefs and cards. Each audio script was rebuilt from its brief, with `[calmly] ` at the start and `[warmly] ` before the closing sentence only. records.json was edited by a script run under `flock`. The script reloads the file inside the lock and touches only `pelagius` and `paulinus-of-milan`. Line numbers point to `cic/texts/`.

## Blocking

None in these three profiles.

## Minor

- **Pelagius.**
  - M1 taken: brief l.1 now reads "Late in 415, by B. B. Warfield's date, fourteen bishops met at Diospolis". Warfield is placed in l.3: "Warfield, who edited Augustine's books in English, takes Augustine's side." That marker moved up from l.9. The record witness notes that the brief gives the date as Warfield's, beside the existing contested_claim.
  - M2 taken: brief l.9 now reads "Innocent's successor Zosimus at first declared Pelagius orthodox, in 417. In 418 the emperor banished the Pelagians from Rome, and Zosimus condemned him." (Warfield, npnf105 l.924–927: "(September, 417), in which Zosimus, with the approbation of the clergy, declared both Pelagius and Cœlestius to be orthodox".) The card `dates` now say "declared orthodox by Zosimus of Rome in September 417, then condemned by him in 418". The keyWorks "about" for the letter to Innocent adds Zosimus's verdict on its arrival (l.924–925, "On the arrival of Pelagius' papers"). The records claim is rewritten to match. l.11 now opens "In a letter to Innocent, Pelagius pointed to his letter to Demetrias". The letter reached Rome after Innocent's death (l.922–923), so the old "told Innocent to read" was dropped.
  - M3 taken: brief l.3 now reads "Augustine of Hippo quoted the synod's record in a book against him. Jerome of Strido, to whom Augustine appealed, wrote against him too." (Fremantle, npnf206 l.1718–1720: "Augustin from Africa and Ctesiphon from Rome appealed to him".) Card uncertain #1 matches. In the record, the claim is restated, the build notes are removed from the witness, and Fremantle is cited at l.1712–1720 and l.42449.
  - To hold the cap after M1 to M3, three things were cut. The Briton sentence (Holmes) was cut; the card's uncertain #4 still carries it. "his own letter" became "his letter". "in the English of B. B. Warfield, editor of Augustine's books against him" became "in Warfield's English", since Warfield is now placed in l.3.
- **Paulinus of Milan.**
  - M1 taken: in the brief and card uncertain #2, "a Latin layman who wrote against the Pelagians" is now "a Latin writer against the Pelagians". This is confirmed: "layman" comes from the vendored file's build header and from Garnier's guess (PL 48 l.488, 561). Mercator himself does not say it.
  - M2 taken: brief l.7 now reads "At Carthage in 412, by B. B. Warfield's date". Warfield's note reads "Early in 412, or, less probably, according to the Ballerini and Hefele 411" (npnf105 l.885). The records witness notes that the brief gives the date as Warfield's.
  - M3 taken: l.1 now reads "Paulinus of Milan was taking it down." and l.3 "Paulinus tells this in his Life of Ambrose". One word was trimmed to hold length: "men who had served Ambrose" became "men who served Ambrose".
  - M4 taken in this form: the claim "The accuser of Caelestius is the author of the Life of Ambrose" is retagged Dominant Modern Reconstruction. The witness now names Kaniecka, and before her the note in the Migne edition of Mercator (PL 48 l.3660–3667). The reviewer calls that note Baronius's identification. At the line, it cites Baronius only as the place where the petition is printed ("Exstat apud Baronium ... libellus"). The argument from style is the note's own ("cujus ex stylo facile quisquis intelliget unum eundemque esse qui et Vitam S. Ambrosii scripserit"). The record says so. The card's wording, "an inference ... Kaniecka takes them to be one man", stands and agrees with the tag.
- **Possidius of Calama.**
  - M1 taken: card uncertain #3 now reads "names Possidius as the bishop that Crispinus, the Donatist bishop of Calama, was charged with trying to kill". The source is Cunningham's heading to Letter 66, npnf101 l.32099: "Crispinus, the Donatist Bishop of Calama."

## Not taken, with reasons

- None declined. Paulinus M4 was taken in another form, for the reason given above.

## Reported, not changed

- README-M1 (batch years) concerns the batch README, which is not one of my files. For the coordinator: Pelagius's census year has no held witness behind it. The cards give "condemned 418, death not given".
- My first report said "the 1411 list" for the 411 Carthage conference list. That was a typo. records.json was already corrected to "411" before the drafts were handed over.
- Paulinus's card tradition is "Ambrosian Milan (standalone)", as the coordinator set it in the repo. It is unchanged here.

## After the changes

| Profile | Words | Time at 162 wpm | FK | Flesch |
|---|---|---|---|---|
| Pelagius (MAJOR) | 405 | 2:30 | 7.2 | 65.3 |
| Paulinus of Milan | 325 | 2:00 | 6.8 | 65.9 |
| Possidius of Calama | 325 | 2:00 | 6.8 | 72.0 |

The Possidius brief is unchanged. `briefLength` stays accurate on all three. Each audio script equals its brief once the tags are removed.

## R1 changes: era 2 batch 4, John Cassian, Sulpicius Severus, Honoratus of Arles

What the drafter changed in answer to `R1_review.md` (part A for Sulpicius and Honoratus, part B for Cassian). Each finding was checked against its vendored file before it was taken. Only the repo files in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/` were edited. `records.json` was changed by a script run under the shared lock. The script reloads the file inside the lock and touches only `honoratus-of-arles` and `john-cassian`. Each changed audio script was rebuilt from its brief, with `[calmly] ` at the start and one `[warmly] ` before the closing sentence. The quotation set did not change, and the scratchpad `quotes.tsv` files were regenerated from the repo briefs and cards with 0 misses. Line numbers point to `cic/texts/`.

## Blocking

| Profile | Finding | Change |
|---|---|---|
| Honoratus | B1: Gibson's reasoning reversed. The card made his dates look like inferences from Cassian's prefaces. | Verified at `npnf211` l.15545–15566. Gibson writes "as Honoratus was raised to the see of Arles in 426, the volume must have been published not later than that year" and "Honoratus died in January, 429": he takes the dates as given and dates the prefaces from them. Card uncertain #3 now reads: "Gibson gives 426 and January 429 without naming a source. He uses them to date Cassian's prefaces, where Honoratus is styled brother in one and bishop in the next. His date of 410 for the founding of Lérins is also his own." The records.json witness for the 426/429 claim now says the same. |

## Minor

- **Sulpicius Severus.**
  - M1: taken as the reviewer worded it. "Alexander Roberts, who translated him, says without naming a source that he gave up a name at the bar after his wife died young." This now matches the Inferential-Thin tag. To hold length, "a Chronicle of the world from the Creation" became "a Chronicle from the Creation". "until he died, to make up for it" became "until death, to atone", which is Gennadius's own word (`npnf203` l.42558).
- **Honoratus of Arles.**
  - M1: taken. Brief first mention: "Honoratus, later bishop of Arles, went in unafraid". The close of paragraph 5: "Edgar Gibson, who translated John Cassian, dates his death to January 429." To hold length, "his successor as bishop of Arles" became "his successor as bishop" (Arles is now named in paragraph 1). "the home country he had left" became "his home country", and "Arles called Honoratus" became "Arles called him".
- **John Cassian.**
  - M1: taken. "Gennadius of Marseilles, who wrote late in the fifth century, calls Cassian..." This rests on Gibson, who gives a.d. 495 (`npnf211` l.14969), and on Richardson, who puts the bulk of the work about 480.
  - M2: taken in another form. "Gennadius, who sides with Cassian, believed an unsigned attack on works 'which the church of God finds salutary' was Prosper's." Gennadius has "I regard as his also an anonymous book" (`npnf203` l.43669). "Sides with" replaces "takes ... side" so that the sentence does not say "take" twice.
  - M3: taken, split to keep sentences under 25 words. "Its speaker is Chaeremon, an old hermit near Panephysis in the Nile delta. He says that grace and free will..." This rests on Gibson: Archebius of Panephysis brought them first to Chaeremon, one of three old anchorites in the salt-marsh district, on a first tour "not extended beyond the Delta" (`npnf211` l.15104 and l.15241, from Conference XI.i–iii).
  - To hold length, the sentence "Gibson says no one can tell how far they keep the fathers' own words" was cut from the brief. Card uncertain #2 carries it with Gibson's own words.
  - M4: taken. Card uncertain #4 now reads: "Gibson, and William Bright whom he quotes, call this teaching Semi-Pelagian. Cassian does not use the word." The records.json contested_claim was reworded to match.
  - M5: taken. Card: "Photius of Constantinople calls him a Roman" (Walford's title page, `philostorgius_ecclesiastical-history_walford1855.txt` l.21, "Photius, Patriarch of Constantinople").

## Not taken, with reasons

- **Honoratus B1, the optional second date.** Migne's note to Hilary's sermon (`hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt` l.1500, "labente an. 436 [sic, OCR for 426] vel ineunte an. 427") was not added. The note does not show who wrote it: it cites Quesnel inside an unsigned editorial note. Giving it a voice would mean naming a role ("the editor"), which the pattern forbids. The review says leaving it out is not a fault.

## Reported, not changed

- The README years (README-M1) belong to the coordinator's README, not to these three profiles.
- Card files keep the repo's form, with no trailing newline after the closing brace.

## After the changes

| Profile | Words | Time @162 wpm | FK | Flesch | briefLength |
|---|---|---|---|---|---|
| John Cassian (MAJOR) | 404 | 2:30 | 7.7 | 64.3 | about 2 minutes 30 seconds |
| Sulpicius Severus | 324 | 2:00 | 6.7 | 69.7 | about 2 minutes |
| Honoratus of Arles | 325 | 2:00 | 6.6 | 70.0 | about 2 minutes |

No brief sentence runs past 25 words. Each audio script equals its brief once the tags are removed. `briefLength` is unchanged and still accurate.
