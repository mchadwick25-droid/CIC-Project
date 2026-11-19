# Batch 6: era 1, the second century and the outside witnesses

Mark's rulings: Decision-Log, "Batch 6: era 1 first, the slate, an outside-witness shape, and the stories approved before the kit" (2026-11-19). Kit: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, with that entry's three changes. The slate as Mark approved it: https://claude.ai/artifact/4cgx8VUgM7piGeR4bkYrSy (version 5).

Each folder holds `Source_Sheet.md` and `Outline.md` from the researcher, and `Card.existing.json`, the census `card` field, where the entry has one. Irenaeus has no card.

## The twelve and their jobs

| Census id | Job | Siblings and links |
|---|---|---|
| `pliny-the-younger` | The governor's letter from Bithynia: how he tried Christians, what they told him of their worship before dawn, and Trajan's answer that they were not to be hunted out. Outside witness. | `tacitus`, `suetonius`. Link: `tertullian-s-voice` (answered Trajan's ruling). |
| `tacitus` | Nero's fire: the fullest outside account of Christians punished at Rome, and Christus named as executed under Pilate, told by a historian who despised them. Outside witness. | `suetonius`: Nero is told here; there it is a clause. |
| `suetonius` | Two short lines in the lives of the emperors: Claudius expelling Jews over "Chrestus", and Nero punishing Christians; how little they say, and why they are still read. Outside witness. | `tacitus` has the fire. `pliny-the-younger`, if held. |
| `josephus` | A Jewish priest and commander who went over to Rome and wrote his people's history; his lines on John the Baptist, James and Jesus, and how Christians kept them and argued over the passage on Jesus. Outside witness. | Links: `eusebius-of-caesarea` quoted him; `origen` said he did not believe in Jesus. |
| `ignatius-of-antioch` | The bishop taken under guard to Rome, and his seven letters on the road: keep to your bishop, Christ truly suffered, and do not save me from the beasts. Martyr. | `polycarp-of-smyrna` (approved; met at Smyrna, gathered his letters): here a sentence. |
| `irenaeus-of-lyon` | From Polycarp's Smyrna to Lyon after the martyrs of 177: Against Heresies, answering the Valentinians with the apostles' churches, one rule of faith and four Gospels. Teacher. | `polycarp-of-smyrna` already says Irenaeus heard him as a boy and tells his letter to Victor: here each is a clause. `valentinus` (here the answer, there the teaching); `polycrates-of-ephesus`; `marcion-of-pontus`, `justin-martyr`. |
| `polycrates-of-ephesus` | The Easter quarrel: the bishops of Asia keeping the fourteenth day, his letter to Victor of Rome naming the great dead buried in Asia, and Victor's attempt to cut them off. Leader. | `polycarp-of-smyrna` already tells the visit to Anicetus, Victor's threat and Irenaeus's reminder: here the quarrel is told from Asia's side, through Polycrates's own letter. `irenaeus-of-lyon`: a clause. |
| `hermas` | A freed slave's visions at Rome: the Shepherd's call to repent, one repentance after baptism, and a book some read as Scripture and others set aside. Teacher. | Link: `tertullian-s-voice` rejected it. |
| `valentinus` | The teacher who nearly became bishop at Rome and founded a school of paired heavenly powers, told from his few surviving words and credited openly to his opponents. Teacher. | `irenaeus-of-lyon`; `marcion-of-pontus` and `clement-of-alexandria`: each a clause. |
| `tatian` | Justin's pupil who turned on Greek learning in his Address, broke with the church, and went east with the Diatessaron, the one gospel the Syriac churches read for centuries. Teacher. | `justin-martyr` already tells Tatian as hearer, his break, and the Diatessaron at Edessa: here Tatian's own book carries it. `bardaisan-of-edessa`. |
| `bardaisan-of-edessa` | The Syriac teacher at Edessa who argued, in a pupil's dialogue, that people are free and not ruled by the stars; later called a heretic, and answered in song by Ephrem. Teacher. | `tatian`; link `ephrem-the-syrian`. |
| `hippolytus-of-rome` | The Greek-writing teacher at Rome who attacked bishop Callistus as too lax in his Refutation of All Heresies, and was exiled to Sardinia in 235 with the bishop of Rome; whether he led a rival church is disputed. Teacher. | `valentinus` (the Refutation); link `novatian`. |

`polycarp-of-smyrna` is not researched again. Its approved text (`Audits/2026-11-16_polycarp-clean-write/Polycarp_approved.brief.txt`, copied into its folder) joins the batch at review (step 4), under the change order of 2026-11-19, "the stories approved before the kit go through review in their era's batch": approved wording is kept wherever it passes. Its new card is drafted.

## Quotes barred
- Every quote in the approved Polycarp story.
- `marcion-of-pontus`: "Do you know me?" / "I do know you: the firstborn of Satan"; Justin's "There is a certain Marcion, from Pontus"; Tertullian's "Separating the law from the gospel" and "the defenders of Judaism".
- `justin-martyr`: the trial exchange.
- Inside the batch: Ignatius keeps "I fight with beasts"; Irenaeus keeps his memory of where Polycarp sat; Valentinus keeps Tertullian's account of the bishopric he missed. A batch 6 quote that a batch 7 old story also holds stays with batch 6.

## Order of research
1. Pliny, Tacitus, Josephus, Ignatius, Hermas, Tatian.
2. Suetonius (after Tacitus), Irenaeus (after Ignatius), Bardaisan (after Tatian).
3. Polycrates and Valentinus (after Irenaeus).
4. Hippolytus (after Valentinus).

## Steps
0. Slate: set by Mark.
1. Research (`Researcher_Prompt.md`). Then the hearts go to Mark.
2. Outline check.
3. Write.
4. Review, after `tools/check_brief_variety.py` and `tools/check_tree_overlap.py`.
5. One revision, one recheck.
6. Card.
7. Second readings (`tools/list_second_readings.py`).
8. Recording, with Mark's approval and a credit cap first; then release.

## At release
- One Open-Gaps entry for the batch, and one that updates "The stories approved before the kit: a consistency check when eras 1 and 2 are finished" (2026-11-19) with the change order of the same day.
- Once Polycarp's reviewed text is in the census, his entry leaves `Build/Ministry/Features/Church-Family-Tree/Earlier-Approved.yaml`; then `python tools/list_story_status.py --write`.
- The batch 7 launch prompt in `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/`, carrying the ledger step and Origen and Methodius under review.

## Status (2026-11-19)
Steps 0 to 8 are done. The twelve and Polycarp are authored, reviewed, carded, read blind (`Second_Readings.md`), in the census and the tree pages (`Release.md`), and recorded (`recording/`, 20,824 credits). Open points: Open-Gaps 333 and 334.
