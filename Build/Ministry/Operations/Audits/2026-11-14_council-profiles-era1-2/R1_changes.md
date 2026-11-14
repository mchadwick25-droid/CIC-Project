# Council profiles, eras 1 and 2: changes after review round 1 (2026-11-14)

The answer to `R1_review.md`. Every substantial finding is fixed. Minor findings are fixed, or left with a reason given. After the changes every brief was rescored with `grade_text`, and every audio script was regenerated from its brief. No paid calls were made.

## Substantial

| Finding | Change |
|---|---|
| NIC-1 | The brief now gives Arius's teaching in his own words, from his letter to Eusebius of Nicomedia, kept by Theodoret of Cyrrhus (npnf203 l.6045-6046): "We are persecuted," Arius wrote, "because we say that the Son has a beginning." The council's letter stays as the second witness. The letter is added to `sources.fromThoseThere`, with a new claim in `records.json`. |
| ARI-1 | Brief: "kept by the Nicene side, who wrote most of the histories. The other side speaks through its creeds and a statement by Acacius of Caesarea, which the Nicene writers copied." Entry `uncertain[0]`: Philostorgius is now named as a Eunomian historian hostile to both sides, not as the Homoian side's historian. |
| CON-1 | The brief opens with Gregory of Nazianzus standing before the council's bishops to give up his see. The later paragraph ties back to that moment ("That was when he gave his farewell and withdrew"), so the resignation is told once, in the right place. |
| CON-3 | Timothy of Alexandria is now LISTED, as the supplement Who scan has him. He has no id. |
| CAR-1 | "The record survives in Latin, each speech signed by its speaker. It breaks off in the third session." |
| CHA-1 | "The losing side tells its story in a later Syriac chronicle, known as that of Zachariah of Mitylene, built on a Greek history that ran to 491." |

## Minor

| Finding | Change or reason |
|---|---|
| ROM-1 | The 27-word sentence is split after "near". |
| ARL-1 | The canons are added to what survives. |
| ARL-2 | "led by Marinus, whom Hefele takes as bishop of Arles." |
| ARL-3 | The sentence is shortened to "had handed over the Scriptures." |
| NIC-2 | Left as it is. The reviewer judged "Arius's party" to be within what Eustathius says, and the dispute is in the entry and the records. |
| SAR-1 | "date it by a consulship that their editors take as 347." |
| SAR-2 | "went home in 346, by the index to his Easter letters." |
| ARI-2 | "Socrates of Constantinople says they used its name to pass the creed off as that of Nicaea." |
| ARI-3 | "Jerome" throughout the brief and the entry. |
| ARI-4 | Left as it is. The year 359 rests on the consulate in `datesNote`, and the reviewer rated the risk low. |
| ARI-5 | The quotation marks are dropped: "rejected both homoousion and homoiousion, the words for one substance and like substance." |
| CON-2 | "led them at first, by Hefele's reading". |
| CON-4 | The quotation marks are dropped: "the Pneumatomachi, whose name means fighters against the Spirit". |
| CON-5 | The date "around the year 600" is dropped: "Later, Gregory the Great of Rome …". |
| CON-6 | "Their view reaches us only through opponents, chiefly Gregory and the bishops' letter of the next year." |
| CAR-2 | "the third session" in both places. |
| CAR-3 | "Emeritus of Caesarea in Mauretania" in the brief; "Emeritus of Caesarea (Mauretania)" in `people`, as the scan names him. |
| EPH-1 | "forty-three by their own signed sentence". Cyril's council's "a little more than thirty" stays in the records' `contested_claims`, since the brief had no words to spare. |
| EPH-2 | "John of Antioch's assembly left its own documents too." |
| EPH-3 | The `persian-church-of-the-east-early` note now gives Wigram's view (no corporate action at the time) and Badger's (cut off by the decree), without the flat claim. Barhadbeshabba moves to a new Affected line for `the-church-of-the-east-under-persia`. |
| EPH-4 | The 28-word sentence is split after "Candidian". |
| CHA-2 | "his successor Marcian called a new council, with the empress Pulcheria, Hefele says." |
| CHA-3 | Left as it is. This was optional, and Dioscorus's line is already quoted in the entry. |
| CHA-4 | Severus of Antioch's Select Letters, Book VI, is added to `sources.writtenLater`. |
| CHA-5 | "deposed Flavian, bishop of Constantinople, who had condemned him." The Priscus sentence is split. |

## Cuts made to stay within the 2:30 ceiling

The added words pushed several briefs past 400 words, so these sentences were cut. Each fact stays in the entry or the records.
- Nicaea: "A low golden chair was set for him."; the names of Secundus and Theonas; "Within a few years Eusebius and Theognis were back in their churches."
- Sardica: Socrates's count of 300 Westerners and Hefele's view of it.
- Ariminum: Philostorgius's count of three hundred.
- Constantinople: "Cyril of Jerusalem and Gregory of Nyssa were among them."; the Eunomians and Arians from the list of condemned heresies.
- Carthage: "Guards and clerks stood by."
- Ephesus: "Two assemblies now claimed to be the council."
- Chalcedon: the move from Nicaea to Chalcedon, which stays in `calledBy`.

A few words were also changed to keep reading ease at or above 60. At Carthage, "notaries" became "clerks" and "mandates" became "written orders". At Nicaea, "consulted" became "checked". A few long sentences were split.

## Scores after the changes

| Council | Words | FK | FRE |
|---|---|---|---|
| councils-of-rome-and-carthage-251 | 398 | 7.35 | 63.78 |
| council-of-arles-314 | 399 | 7.75 | 60.21 |
| council-of-nicaea-325 | 393 | 7.73 | 60.59 |
| council-of-sardica-343 | 400 | 7.74 | 61.01 |
| councils-of-ariminum-and-seleucia-359 | 398 | 8.48 | 60.43 |
| first-council-of-constantinople-381 | 400 | 7.82 | 62.06 |
| conference-of-carthage-411 | 397 | 7.97 | 60.59 |
| council-of-ephesus-431 | 399 | 7.64 | 60.53 |
| council-of-chalcedon-451 | 399 | 7.35 | 64.09 |
