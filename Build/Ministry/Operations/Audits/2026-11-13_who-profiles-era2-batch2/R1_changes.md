# R1 changes: nine Who profiles, era 2 batch 2

What the drafter changed in answer to `R1_review.md`, in the same two parts.

## R1 changes: era 2 batch 2, part A (Ulfila, Auxentius of Durostorum, Eunomius of Cyzicus, Macrina the Younger)

This file lists what the drafter changed in answer to `R1_review.md, part A`. I checked every finding against its vendored file before acting on it. Every new or changed quotation was searched again (quotecheck: 0 misses on all four). Each audio script was rebuilt from its brief, with `[calmly] ` at the start and `[warmly] ` before the closing sentence only. The records.json edits were made by a script that reloads the file just before writing and touches only these four ids.

## Blocking

| Profile | Finding | Change |
|---|---|---|
| Macrina | B1: card cited Blomfield Jackson as following Gregory of Nyssa, and hid Gregory of Nazianzus | Verified at npnf208 l.1252-1264. Jackson gives "his friend Gregory" (Or. xliii): Basil "had already determined to renounce the world". He then gives Gregory of Nyssa, and reads Macrina as giving Basil "the resolution, with which he now carried out the determination". The card trace now gives Gregory of Nyssa, Gregory of Nazianzus (Basil's friend) and Jackson's reading. In records.json the claim is now Contested with both witnesses, and a new contested_claim "Whether Macrina turned Basil to the ascetic life" names all three. The brief's attributed line ("Gregory says") stands. |

## Minor

- **Ulfila.**
  - M1: the arrival is now Kauffmann's account, not Bessell's: "In 383, by Kauffmann's date, the emperor summoned the bishops to Constantinople. Ulfila went, meaning to debate a rival party, but fell ill there and died." Kauffmann l.3702-3706, and n. 2 at l.3718-3719. The record now names Sievers against Bessell.
  - M2: on the card, "forty years in all, the span of the saints he followed". Auxentius 60 has "quorum sanctorum imitator erat" (l.15278-15280) and no Moses.
  - M3: Photius is now "a later patriarch of Constantinople who was hostile to it" (to the history: Walford l.52, "The author is a liar").
  - M4: the opener is gone. The paragraph now starts "Socrates, a Nicene historian, says", then "Sozomen, another Nicene historian". Card uncertain #1 now opens on Auxentius, without "is told three ways".
  - M5: the card now reads "Eusebius and the other bishops with him", after Walford l.120. A sentence says no source in the Library names his see in this account. The gap is logged in `absent_details`. Kauffmann ties the Antioch synod of 341 to Eusebius of Nicomedia (l.2754) but never names the consecrator's see (l.3767-3769, 3809-3811), so I gave no identifier.
- **Auxentius.**
  - M1: the first mention is now "Auxentius of Durostorum"; the second paragraph uses "Auxentius".
  - M2: "Homoian" is dropped from the brief. It now reads "in the party its foes called Arian", and Maximinus is "a bishop of the same party", so a listener hears one party throughout. Kauffmann says the party refused the name Arian (l.3813). Hilary's letter is titled "adversum Auxentium Arrianum" (l.503). The card's knownFor reads "Homoian ('Arian')", matching the Ulfila card.
  - M3: the letter is now in "a fifth-century manuscript now in Paris, in the margins of Ambrose's On the Faith" (Kauffmann l.509-512, l.683-692). Card uncertain #6 and the record match.
  - M4: "the span of the saints he followed", in the brief and on the card (as for Ulfila M2).
  - M5: card uncertain #2 is rewritten as the reviewer proposed. Kauffmann's "mit Bessell" covers only place and time; the Moesian readers are his own view (l.3474-3477). The record's witness line says so.
  - M6: (a) the paragraph now opens "In Kauffmann's day, W. Luft held". (b) The one-sided readers sentence is cut from the brief and left to card uncertain #2, which gives both sides. The card's #1 opener is changed the same way.
- **Eunomius.**
  - M1: "Socrates, a Nicene opponent, says". This is borne out at npnf202 l.12466-12483, "blasphemous heresies" and "a great scarcity of sense".
  - M2: the brief adds "Philostorgius says he was later moved to Tyana" (Walford l.410). records.json now splits the burial at Dacora (Documented) from Eutropius's move to Tyana (Documented, one partisan witness). "God knows no more" is retagged Documented as a one-witness hostile report, noting that the held Apology is silent on it. Part of this is not taken: see below.
  - M3: the card's `dates` now has "Socrates of Constantinople". Uncertain #2 has "Theodoret of Cyrus, another church historian". The place is from npnf203 l.2337 ("Bishop of Cyrus"), a file not in this card's sources. Uncertain #3's opener "is told three ways" is also gone.
  - M4: the bishopric date is one sentence; the accounts of the leaving are joined where they connect. The brief's mean sentence length rose.
  - Own fix: "His own clergy" is now "Some of his clergy". Walford l.246 says "SOME individuals of the clergy".
- **Macrina.**
  - M1: "dreams and healings" in the brief and on card uncertain #1. Uncertain #4 adds the soldier's story of his daughter's eye (Clarke l.350-378). It also says Gregory leaves out more wonders, among them the corn that did not run out in the famine (l.380-384).
  - M2: uncertain #5 now gives the Life (l.132, l.212), Clarke ("ten children, of whom four sons and five daughters survived infancy", l.44) and Moore and Wilson (l.490-492). A new contested_claim "The size of the family" records it. I kept the item because Clarke does not resolve it. Clarke has nine surviving infancy; Moore and Wilson have the father leaving ten, five sons and five daughters.
  - M3: `[warmly]` now sits before "'Thou, O Lord ...' she began." only.
  - M4: "Peter of Sebaste" (Clarke l.44), in the brief and in card trace #2.
  - M5: the sentence is split after "double monastery".

## Own fix outside the findings

- **Ulfila brief, Sozomen sentence.** The draft put the hedge on the wrong reason ("perhaps for help with an embassy, or 'thinking...'"). Sozomen gives the compulsion plainly and hedges only the conviction: "Compelled by the urgency of the occasion, or, possibly, thinking..." (npnf202 l.40168-40169). The brief now reads "pressed by the needs of an embassy. Or he was 'possibly, thinking that it was better to hold such views concerning the Divine nature.'" This also splits a 30-word sentence. The record now matches.

## Not taken, with reasons

- **Eunomius M2, the burial as "contested".** I did not add a contest, and I removed the existing contested_claim "Where his body lay". The two witnesses do not conflict; they tell a sequence. Sozomen has him buried at Dacora (npnf202 l.41530-41533). Philostorgius has Eutropius "transfer Eunomius from the Dacoroenian territory to Tyana" (Walford l.410), which assumes he lay at Dacora first. The brief gives both in that order, and card uncertain #8 keeps the move as Philostorgius's alone.
- **Eunomius M2, contested_claim for the Socrates quotation.** Not added. The Apology's silence is not a counter-witness, so a contest would be invented. I retagged it as the reviewer's alternative allows.

## Reported, not changed

- Eusebius (Ulfila card): no vendored see. The gap is logged in records.json `absent_details`.
- Theodoret of Cyrus: the place comes from npnf203 (l.2337), which is not among the Eunomius card's sources. The coordinator may want it listed.
- "In Kauffmann's day" (Auxentius): Luft's articles are cited by Kauffmann at l.3478 (Zeitschr. f. d. A. 42).

## After the changes

| Profile | Words | Time @162 wpm | FK | Flesch | briefLength |
|---|---|---|---|---|---|
| Ulfila (MAJOR) | 405 | 2:30 | 8.3 | 60.4 | about 2 minutes 30 seconds |
| Auxentius of Durostorum | 317 | 1:57 | 8.0 | 62.3 | about 2 minutes |
| Eunomius of Cyzicus (MAJOR) | 403 | 2:29 | 8.0 | 60.2 | about 2 minutes 30 seconds |
| Macrina the Younger | 324 | 2:00 | 6.4 | 76.7 | about 2 minutes |

## R1 changes: five Who profiles, era 2 batch 2, part B

What the drafter changed in answer to `R1_review.md, part B`, for `damasus-of-rome`, `priscillian`, `tyconius`, `cyril-of-jerusalem` and `apollinaris-of-laodicea`. Every finding was checked again in its vendored file before it was taken. Every new or changed quotation was searched again (quotecheck: 0 misses on all five). Only these five ids were touched in `records.json`, by a script that reloads the file just before it writes. Line numbers point to `cic/texts/`.

## Blocking

| Profile | Finding | Change |
|---|---|---|
| Damasus | B1: 366 told as settled while the records contest it | Brief: "followed Liberius as bishop, in 366 or 367". Card dates: "Bishop from 366, by the Avellana account's date, or 367, by Jerome of Strido's Chronicle as A. C. Zenos cites it". knownFor "from 366 or 367". The label "The election of 366 is told from three sides" was removed. Record claim 1 no longer carries the year and points to the contested record (Gesta l.5098 "Gratiano et Dagalaifo consulibus"; Zenos's note `npnf202` l.14181 to 14184). |
| Priscillian | B1: card dates tell the Saragossa condemnation plainly | Card dates: "Sulpicius Severus says he was condemned at Saragossa, which he denied; put to death at Trèves under Maximus; Ernest Cushing Richardson dates him flourished 379, died 385" (Sulpicius `npnf211` l.11504 to 11508; Tractate II l.4381 to 4384). |
| Priscillian | B2: Orosius and Braga given as neutral; the card's caveat missing from the brief | Brief adds "His teaching comes to us mostly through his enemies." Orosius is now "a Spanish priest who wrote to Augustine of Hippo against the Priscillianists" (the Commonitorium "de errore Priscillianistarum", Schepss l.10186). Braga is "Long after, in 561". The card's first uncertain item now opens with the same sentence. |
| Tyconius | B1: Augustine not placed | Brief: "Augustine of Hippo, a Catholic bishop who wrote against the Donatists" at first mention. The card places him the same way at its first mention (legacy) and in the first uncertain item. Record witness note updated. |
| Cyril | B1: the Theodoret heading quoted inexactly, from a work not in Sources | Card now says, without quotation marks, "Theodoret of Cyrus, in his Dialogues, cites the fourth lecture as a testimony of Cyril, bishop of Jerusalem" (`npnf203` l.24428 to 24431, in Dialogue 2, "The Unconfounded", l.21085). The Theodoret source title adds "the Dialogues (Eranistes), Dialogue 2". |
| Cyril | B2: "No source gives his birth, family or schooling" is false | Card: "No source used here gives his birth, parents or schooling. Gifford names one relative, his sister's son Gelasius, whom Cyril made bishop of Caesarea" (`npnf207` l.586 to 588). The absent_details record was corrected to match and cites Theodoret's Gelasius of Caesarea (`npnf203` l.15861). |

## Minor

- **All (G-M1).** Sozomen is now "a church historian of the fifth century" at his first mention in the Damasus, Cyril and Apollinaris cards. Hartranft's introduction says Sozomen's history runs to 439 (`npnf202` l.1227 to 1229).
- **Damasus.** M1: "An account from Ursinus's side" (brief). The card's source author is "Anonymous, from Ursinus's party", and the card and records say anonymous (the Gesta names no author; its partisanship shows at l.5150 "Ursinus uir uenerabilis" and l.5103 "periuri"). M2: "Zenos's note calls him 'a Spaniard by race, native of Mantua'" (`npnf202` l.14195), in the card and the record. M3: "a soldier and historian, most likely a pagan" (brief), and "a historian and most likely a pagan" (card) (Yonge's preface l.750 to 752). The record notes say the same. M4: card: "Socrates of Constantinople blames Ursinus ... Sozomen ... tells it the same way after him" (Hartranft's note, `npnf202` l.38775). The record witness notes the dependence. M5: "One comfort was that" (`npnf206` l.46645 "two consoling reflections").
- **Priscillian.** M1: "did not deny that he had given himself up to lewd teachings", in the brief and the card (`npnf211` l.11668). M2: "bold, talkative and given to pleasure" (l.11645 to 11646). M3: "a council at Braga named him when it cursed the teaching that souls were cast into bodies and bound to the stars" (Bruns l.2512 to 2515, 2529 to 2531, "Si quis ... anathema sit"). M4: the record is now tagged Documented, with the note "Sulpicius II.50 only; hostile; reports the court of Evodius". M5: Martin of Tours was dropped from the card's remembered list. The brief still tells it.
- **Tyconius.** M1: the 29-word sentence is now two: "F. C. Burkitt edited the Book of Rules. He says ...". M2: the "council around 380" sentence was dropped from the card. It stays in absent_details. M3: the one-sided contested_claim was removed. Augustine's verdict is now a Documented claim in his name. "Tyconius's own case for staying a Donatist" is a new absent detail (Bellum Intestinum perished, Burkitt l.376 to 402).
- **Cyril.** M1: "Jerome says he held his see eight years under Theodosius. Gifford dates his death to 386." (`npnf203` l.41502 to 41504; `npnf207` l.1360 to 1364). The card dates add "by Gifford's reckoning from Jerome's eight years under Theodosius". M2: the label sentences "How he became bishop is disputed." and "Why Acacius deposed him." were removed. Both items now open on their witnesses.
- **Apollinaris.** M1: the brief now reads "Sozomen names only one of them. He gives him an epic of Hebrew history, plays and odes." The card adds "whom Lietzmann takes for the son". The contested_claim says Sozomen does not mention the Moses verse or the Gospel dialogues (`npnf202` l.36685 to 36707). M2: the card dates now say "377, by Lietzmann's date". A new uncertain item reads "Chester Hartranft, who translated Sozomen, notes two dates for it, 377 after Rade and 374 after Hefele" (`npnf202` l.39034 to 39035). The record witness was updated. M3: "which Jerome of Strido says were generally counted among his best works" (`npnf203` l.41396 to 41397). M4: the three label openers were removed. Each item now leads with its witness.

## Trims (to hold length after the fixes)

- **Priscillian.** The Ydacius of Emerita and Gratian sentence was cut from the brief; Ydacius stays on the card. "Sulpicius thought his teaching the heresy of the Gnostics" lost "him a heretic and". The Orosius sentence (29 words) was split in two.
- **Cyril.** "Gifford counts three exiles, about 357, in 360, and about 367". "Socrates says" became "he adds" in the sentence straight after Socrates is named.
- **Apollinaris.** "in a Roman council" and "under the emperor Theodosius". The Sozomen sentence was split to hold Flesch at 60 or above.

## Not taken, or taken in another form

- **Apollinaris M1.** The reviewer's wording "Sozomen names only the son" was not taken. Sozomen V.18 says "Apolinarius the Syrian" and does not say father or son (`npnf202` l.36685). Taking him for the son is Lietzmann's reading (l.2572 to 2575). So the brief says "only one of them", and the card names Lietzmann for the identification.
- **Damasus M4.** Taken in substance. The reviewer's fix was "Socrates ... and Sozomen after him". Rufinus, Socrates's source by Zenos's note (l.14181), is left out of the card, because it would need context and adds a name a general listener does not need. The record names him.
- **Damasus B1, brief.** "In 366 or 367" was used in place of "by the date of the Ursinian account". The Gesta is not yet introduced at that point in the brief. Both witnesses are named on the card.
- **Priscillian B1.** Richardson's "condemned 380" was dropped from the card dates, as the reviewer's fix does. It restates Sulpicius's side.

## Drafter's own additions (checked in the files)

- **Apollinaris.** The death item adds "Richardson's note gives about 390" (`npnf203` l.41393, "died about 390"), so that the unknown year does not stand on one witness. The record was updated.
- **Damasus.** The verbless label "The election is told from three sides" was removed for the same reason as Cyril M2.

## Reported, not changed

- Site list lines: the census holds no people row for Damasus ("Imperial and Juridical Christianity") or for Priscillian. These belong to the map Who build.
- Sozomen has no "of <place>" form in the vendored files. He is given the clause of context instead.
- A checkpoint commit ("R1 fixes in progress (pre-recheck)", 3df8723a) landed during this work, made by someone else. This fixer made no commit.

## After the changes

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| Damasus of Rome (MAJOR) | 402 | 2:29 | 8.2 | 60.4 |
| Priscillian (MAJOR) | 405 | 2:30 | 7.6 | 63.6 |
| Tyconius | 323 | 2:00 | 7.4 | 65.1 |
| Cyril of Jerusalem (MAJOR) | 405 | 2:30 | 7.3 | 66.0 |
| Apollinaris of Laodicea (MAJOR) | 403 | 2:29 | 8.2 | 60.3 |

`briefLength` stays accurate on all five ("about 2 minutes 30 seconds" for the four majors, "about 2 minutes" for Tyconius). Each audio script equals its brief once the tags are removed, with `[calmly] ` at the start and one `[warmly] ` before the closing sentence. quotecheck finds 0 misses on all five.
