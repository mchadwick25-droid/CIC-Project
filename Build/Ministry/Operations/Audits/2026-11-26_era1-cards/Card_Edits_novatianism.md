# Card edits: Novatianism, the Katharoi (`novatianism`, tradition card)

Written to `novatianism.layout.json` (entry fields `shortDescription`, `dates`, `timeline`, `briefSources`, `uncertain`). A new card: batch 11 did not rebuild this tradition, so there is no source sheet, outline or held card field. Sources, as the batch header sets for this case: the census entry (its `longDescription`, the brief, kept as it stands; `why`, `voices`, `people`, `legacy`, `floorNote`, `sourcing`, and its two `documentedStories`), and the held texts they cite, each opened at its lines in `cic/texts/`, with the README's newly held Jerome's Chronicle. The brief has no quoted span, so the card has no `quotationOriginals`. The census name is "Novatianism (the Katharoi)"; the sources' English gives "Cathari", kept where a line reports their words. No visitor field uses "world" in the barred sense.

Short names: HE = `npnf201_eusebius-church-history-life-of-constantine.xml`; ANF5 = `anf05_hippolytus-cyprian-caius-novatian.xml` (Cyprian's letters, ANF numbering, and Novatian, On the Trinity); SOC = `npnf202_socrates-sozomen-ecclesiastical-histories.xml`; NIC = `npnf214_seven-ecumenical-councils.xml`; VI = `npnf203_theodoret-jerome-gennadius-rufinus.xml`; JerChron = `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`; FAUS = `novatian_de-trinitate-lat_fausset1909.txt`.

## Shown dates

Census `dates`: `c. 251-400s`. Proposed: **`c. 251 to after 438`**, a change, by the date rule and the batch header's "Dates from the sources' own clues".

- Start. The Chronicle sets Novatus's coming to Rome, and his joining Novatian and the confessors to himself, in the first year of Gallus and Volusianus (JerChron 43960-43973, under the Olympiad heading at 43960). Decius's death and Gallus's first year are Widely Accepted as 251, so "c. 251", marked as a conversion on the timeline (line 10). No held line gives a year for Cornelius's election or Novatian's consecration; both are told by the record's own phrase.
- End. No source gives one. The last held witness is Socrates. He says the Novatian discipline is kept "to the present day" in Phrygia and Paphlagonia (SOC 14060-14061), and dates the death of Paul, bishop of the Novatians, to 21 July "under the same consulate", the sixteenth of Theodosius (SOC 21469-21471, 21491-21492), so 438, a conversion. So the end is "after 438", in the form the Manichaeism check set (`Card_Check_E.md` N1). The census "400s" would imply an end no source gives.
- `start` 251 stands; `end` 400 falls before Socrates's witnesses (V.10, VII.46). Both only place the entry on the map and are not edited; `end` is flagged for Mark.

## shortDescription

> At Rome, the presbyter Novatian led a church that called itself the Katharoi, the pure. It shut out from communion those who had sacrificed to the gods, left their pardon to God, and spread east to Constantinople and Phrygia.

Two sentences, 39 words. It opens on the place, names Novatian by what he was at the time (a presbyter of Rome), and says what the church did, in the words of its own bishops' rule as Socrates gives it. "Shut out" is what they did, not a denial of something. No contrast, dash or placeholder opening. Readability alone: grade 9.6 (names out 7.4), ease 76.8: pass.

| Phrase | Work | File | Line(s) | Verbatim |
|---|---|---|---|---|
| At Rome, the presbyter Novatian | Jerome, Lives 70 | VI | 40887 | "Novatianus, presbyter of Rome" |
| led a church | Cornelius in Eusebius VI.43; Eusebius VI.43.1 | HE | 38518-38534; 38268 | made bishop; "became leader of the heresy" |
| that called itself the Katharoi, the pure | Eusebius VI.43.1; Nicaea, canon 8 | HE; NIC | 38269-38270 (note: "καθαροί, 'pure'"); 3769-3770 | "call themselves Cathari"; "those who call themselves Cathari" |
| It shut out from communion those who had sacrificed to the gods | Socrates IV.28 | SOC | 14069-14071, 14088-14089 | "received into communion believers who had sacrificed"; "they should not admit to the sacred mysteries those who had sacrificed" |
| left their pardon to God | Socrates IV.28 | SOC | 14089-14090 | "leave the pardoning of their offense to God" |
| and spread east to Constantinople | Socrates II.38 | SOC | 9091 | "the number of the churches which the Novatians have in the city" |
| and Phrygia | Socrates IV.28 | SOC | 14060-14061 | "in the provinces of Phrygia and Paphlagonia" |

"To the gods" glosses "sacrificed": the sacrifices of Decius's persecution (SOC 14070-14071; Dionysius of Alexandria names the idols, HE 38926-38927).

## timeline
Six periods, 27 lines, in time order. Dated only where an old source fixes the date or its own clue gives one: the Chronicle's first year of Decius (about 250) and first year of Gallus (about 251), and Socrates's sixteenth consulate of Theodosius (438), each marked as a conversion. Otherwise the record's own phrase ("after Fabian's death", "in the reign of Valerian", "under Constantine", "under Constantius, when Macedonius was bishop of Constantinople", "under Theodosius") or "date unknown". No editor's year is used: not McGiffert's spring and October 251 for the synods (HE note at 38272), not 325 for Nicaea, not 383 for Theodosius's meeting, not the census story's "c. 358-360". Period placement only: Nicaea under Constantine, Mantinium under Constantius, both Widely Accepted. Names: Eusebius and Socrates write Novatus, Cyprian and Jerome Novatian; each line keeps its witness's name, with a note where Eusebius's copy of Cornelius gives Novatus (lines 5, 7), and `uncertain` 1 sets the two side by side. Each opponent's charge stays in its witness's voice: the forced consecration and the oath (Cornelius, lines 5 and 7), "no hope of salvation" (Eusebius, line 8), bribery (Cyprian, line 15). Socrates's sympathy is shown, not judged: his sources are named (lines 21, 24).

**Period 1.** when: Decius's persecution and after, about 250 to 251 · headline: Decius persecutes the Christians, and Rome divides over those who sacrificed

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 1 | about 250, the first year of Decius | Eusebius's Chronicle, in Jerome's Latin, says that Decius, after killing the two Philips, father and son, began a persecution of the Christians, out of hatred for them. | Eusebius, Chronicle, in Jerome's Latin, cic/texts/jerome_eusebii-chronici-canones-lat_fotheringham1923.txt lines 43895-43899; the year is a conversion from the Chronicle's first year of Decius | Written more than a century later. | jerome_eusebii-chronici-canones-lat_fotheringham1923.txt 43895-43899: "nos persecutionem mouet" |
| 2 | after Fabian's death | The Chronicle says that after the death of Fabian, bishop of Rome, which it calls glorious, Cornelius took up the office of bishop there. | Eusebius, Chronicle, in Jerome's Latin, cic/texts/jerome_eusebii-chronici-canones-lat_fotheringham1923.txt lines 43918-43921 |  | jerome_eusebii-chronici-canones-lat_fotheringham1923.txt 43918-43921: "Fabiani gloriosam mortem" |
| 3 | date unknown | Cyprian of Carthage writes that Cornelius was made bishop by the judgment of God and of Christ, by the witness of nearly all the clergy, by the vote of the people then present, and by the gathering of the senior bishops. | Cyprian, Letter 51, to Antonianus, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 33577-33580 | Cyprian sided with Cornelius. | anf05_hippolytus-cyprian-caius-novatian.xml 33577-33580: "by the suffrage of the people" |
| 4 | date unknown | Socrates writes that Novatus, a presbyter of the church of Rome, broke from it because Cornelius the bishop took back into communion believers who had sacrificed to the gods in the persecution Decius raised. | Socrates, Church History IV.28, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 14061-14082 | Socrates writes the name Novatus; Cyprian and Jerome give Novatian. He wrote in the 5th century. | npnf202_socrates-sozomen-ecclesiastical-histories.xml 14061-14071: "received into communion believers who had sacrificed" |

**Period 2.** when: About 251 · headline: Novatian is made a rival bishop, and a synod at Rome casts his party out

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 5 | date unknown | Cornelius, writing to Fabius, bishop of Antioch, says that Novatian sent two companions to a small corner of Italy to bring three country bishops to Rome. There, he says, Novatian shut them in and, by the tenth hour of the day, forced them to lay hands on him as bishop. | Cornelius to Fabius, in Eusebius, Church History VI.43, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38518-38534; Fabius of Antioch, lines 38819-38820 | An opponent's account. Eusebius's copy gives the name as Novatus. | npnf201_eusebius-church-history-life-of-constantine.xml 38518-38534: "tenth hour" |
| 6 | date unknown | Cornelius writes that one of the three bishops who made Novatian a bishop soon came back to the church, confessing his wrong, and was received as a layman, and that successors were ordained for the other two. | Cornelius to Fabius, in Eusebius, Church History VI.43, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38536-38540 |  | npnf201_eusebius-church-history-life-of-constantine.xml 38536-38540: "communed with him as with a layman" |
| 7 | date unknown | Cornelius writes that when Novatian gives the bread of communion, he holds the receiver's hands and will not let go until he swears by the body and blood of Christ never to turn to Cornelius. | Cornelius to Fabius, in Eusebius, Church History VI.43, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38761-38774 | An opponent's charge. Eusebius's copy gives the name as Novatus. | npnf201_eusebius-church-history-life-of-constantine.xml 38761-38769: "Swear to me by the body" |
| 8 | date unknown | Eusebius writes that Novatus, as he gives the name, a presbyter of the church at Rome, held that the fallen had no more hope of salvation, even if they did all a true change of heart asks. He became leader, Eusebius says, of those who call themselves Cathari, the pure. | Eusebius, Church History VI.43, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38265-38270; the Greek word kathari, pure, the editor's note at line 38270 | Eusebius, an opponent, says they call themselves so in the pride of their imagination. | npnf201_eusebius-church-history-life-of-constantine.xml 38265-38270: "call themselves Cathari"; npnf201_eusebius-church-history-life-of-constantine.xml 38265-38270: "no longer for them a hope of salvation" |
| 9 | date unknown | Eusebius writes that a synod of sixty bishops and many more presbyters and deacons met at Rome. It ruled that Novatus and those who held his opinion were strangers to the church, and that the fallen should be healed with the medicines of repentance. | Eusebius, Church History VI.43, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38272-38299 |  | npnf201_eusebius-church-history-life-of-constantine.xml 38288-38289: "number sixty"; npnf201_eusebius-church-history-life-of-constantine.xml 38292-38299: "medicines of repentance" |
| 10 | in the first year of Gallus and Volusianus, so about 251 | The Chronicle says that Novatus, a presbyter of Cyprian, came to Rome and joined Novatian and the other confessors to himself, because Cornelius had taken back apostates who repented. | Eusebius, Chronicle, in Jerome's Latin, cic/texts/jerome_eusebii-chronici-canones-lat_fotheringham1923.txt lines 43960-43973; the year is a conversion from the Chronicle's first year of Gallus | Jerome's Chronicle gives two men, Novatus of Carthage and Novatian of Rome. | jerome_eusebii-chronici-canones-lat_fotheringham1923.txt 43969-43973: "Cornelius paenitentes apostatas" |

**Period 3.** when: 251 and the years after · headline: Bishops write against the division, and the confessors go back to Cornelius

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 11 | date unknown | Dionysius of Alexandria writes to Novatus that it would be better to suffer anything than to divide the church of God. To die as a martyr to keep it whole, he says, would be no less glorious than to die for refusing to worship idols. | Dionysius of Alexandria, Letter to Novatus, in Eusebius, Church History VI.45, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 38922-38928 |  | npnf201_eusebius-church-history-life-of-constantine.xml 38922-38928: "better to suffer everything, rather than divide the Church of God" |
| 12 | date unknown | Cyprian writes to the Roman confessors, Maximus, Nicostratus and the others, who had confessed the faith under persecution, that it grieves him that they agreed to the making of another bishop. He begs them to come back to the church they came from. | Cyprian, Letter 43, to the Roman confessors, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 32833-32857 |  | anf05_hippolytus-cyprian-caius-novatian.xml 32833-32844: "had consented that another bishop"; anf05_hippolytus-cyprian-caius-novatian.xml 32853-32857: "return to the Mother" |
| 13 | date unknown | Cornelius writes to Cyprian that the confessors Maximus, Urbanus and Sidonius came before the presbyters and said they had been deceived. Before a great gathering of believers, who wept for joy, they confessed Cornelius as bishop. | Cornelius to Cyprian, in Cyprian, Letter 45, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 32952-33019 |  | anf05_hippolytus-cyprian-caius-novatian.xml 32976-32984: "they had been deceived"; anf05_hippolytus-cyprian-caius-novatian.xml 33011-33018: "know that Cornelius is" |
| 14 | date unknown | Maximus, Urbanus, Sidonius and Macharius write to Cyprian that they have made peace with Cornelius their bishop and all the clergy, with the joy of the whole church. | The confessors to Cyprian, in Cyprian, Letter 49, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 33288-33301 |  | anf05_hippolytus-cyprian-caius-novatian.xml 33288-33294: "have made peace with Cornelius" |
| 15 | date unknown | Cyprian writes to Antonianus that whoever is not in the church of Christ is not a Christian. After a bishop had been made by sixteen fellow bishops, he says, Novatian strove by bribery to be made a bishop by the hands of deserters. | Cyprian, Letter 51, to Antonianus, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 33971-33985 |  | anf05_hippolytus-cyprian-caius-novatian.xml 33975-33977: "he who is not in the Church of Christ"; anf05_hippolytus-cyprian-caius-novatian.xml 33980-33985: "sixteen" |

**Period 4.** when: Mid-3rd century · headline: Novatian writes to the churches, and later writers remember his death and his books

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 16 | date unknown | Socrates writes that Novatus, made bishop by those who held his views, wrote to all the churches about those who had sacrificed. The churches should keep them from the mysteries, the sacraments, he wrote, and urge them to repent, leaving their pardon to God, who has power to forgive all sin. | Socrates, Church History IV.28, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 14082-14090 |  | npnf202_socrates-sozomen-ecclesiastical-histories.xml 14082-14090: "God, who has the power to forgive all sin" |
| 17 | in the reign of Valerian | Socrates writes that Novatus suffered martyrdom in the reign of Valerian. | Socrates, Church History IV.28, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 14132-14133 | Socrates alone, of the held witnesses, says so. | npnf202_socrates-sozomen-ecclesiastical-histories.xml 14132-14133: "suffered martyrdom" |
| 18 | date unknown | Jerome writes that Novatian, a presbyter of Rome, tried to seize the chair of Cornelius and set up the teaching of the Novatians, called in Greek the Cathari, by refusing to take back apostates who repented. Among his books he names a great volume On the Trinity. | Jerome, Lives of Illustrious Men 70, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 40887-40897; written in 392, lines 38784-38785, a conversion from the fourteenth year of Theodosius, counting his reign from 379 | Jerome says many wrongly give the book to Cyprian. | npnf203_theodoret-jerome-gennadius-rufinus.xml 40887-40897: "great volume On the Trinity"; npnf203_theodoret-jerome-gennadius-rufinus.xml 40887-40897: "refusing to receive penitent apostates" |
| 19 | date unknown | Novatian's On the Trinity opens on the rule of truth: first of all, to believe in God the Father and Lord almighty, the founder of all things. | Novatian, On the Trinity 1, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 60470-60472; Latin, cic/texts/novatian_de-trinitate-lat_fausset1909.txt lines 2553-2554 | His own words. | anf05_hippolytus-cyprian-caius-novatian.xml 60470-60472: "Rule of truth requires"; novatian_de-trinitate-lat_fausset1909.txt 2553-2554: "Regula" |

**Period 5.** when: 4th century · headline: An emperor and a council deal with the Cathari, and soldiers come to Mantinium

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 20 | under Constantine, date unknown | Constantine's edict to the heretics names the Novatians first, with the Valentinians, Marcionites, Paulians and Cataphrygians, and their private gatherings. | Constantine, edict to the heretics, in Eusebius, Life of Constantine III.64, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 66068-66080 |  | npnf201_eusebius-church-history-life-of-constantine.xml 66071-66073: "ye Novatians, Valentinians, Marcionites" |
| 21 | at the council of Nicaea, under Constantine | Socrates writes that Constantine called Acesius, the Novatian bishop, to the council. Acesius said the council had set down nothing new on the faith or on the date of Easter. Asked why he then stayed apart, he told what had happened in the persecution under Decius. He spoke of the strict rule that those who commit a deadly sin after baptism may be urged to repent, but must look for forgiveness from God, not from the priest. | Socrates, Church History I.10, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 3690-3716 | Socrates says he heard it from a very old man, and that no other writer tells it. | npnf202_socrates-sozomen-ecclesiastical-histories.xml 3690-3697: "Synod has determined nothing"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 3714-3716: "authority to forgive sins"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 3725-3727: "very old" |
| 22 | at the council of Nicaea, under Constantine | Socrates writes that Constantine answered Acesius: Place a ladder, Acesius, and climb alone into heaven. | Socrates, Church History I.10, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 3720-3721 |  | npnf202_socrates-sozomen-ecclesiastical-histories.xml 3720-3721: "climb alone into heaven" |
| 23 | at the council of Nicaea | The council's eighth canon rules that clergy of those who call themselves Cathari may stay in the clergy if they come over to the church. First they must promise in writing to share communion with the twice married, and with those who fell in persecution and have done penance. | Council of Nicaea, canon 8, cic/texts/npnf214_seven-ecumenical-councils.xml lines 3768-3779 |  | npnf214_seven-ecumenical-councils.xml 3769-3777: "twice married" |
| 24 | under Constantius, when Macedonius was bishop of Constantinople | Socrates writes that in Macedonius's time the Novatians had three churches in Constantinople. Macedonius forced those who would not share communion with him to take it. When he had four companies of soldiers sent against the many Novatians of Mantinium in Paphlagonia, the people armed themselves with long reaping hooks and hatchets and met them. Many of the people died, and nearly all the soldiers. | Socrates, Church History II.38, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 9001-9010, 9089-9113 | Socrates says he had it from a peasant of Paphlagonia who was present. | npnf202_socrates-sozomen-ecclesiastical-histories.xml 9091: "number of the churches which the Novatians have in the"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 9103-9113: "reap-hooks, hatchets"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 9008-9010: "refused to communicate with him" |
| 25 | under Theodosius | Socrates writes that when Theodosius approved the creed that Nectarius and Agelius, the Novatian bishop, defended, he gave the Novatians a law securing their own church buildings and equal privileges, and they held their meetings in the city again. | Socrates, Church History V.10, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 15291, 15349-15366 |  | npnf202_socrates-sozomen-ecclesiastical-histories.xml 15360-15366: "Novatians to flourish again" |

**Period 6.** when: 5th century · headline: Socrates writes of Novatian churches in his own day · witness: Socrates of Constantinople

| # | when | text | reference | note | verbatim at the lines (checked by script) |
|---|---|---|---|---|---|
| 26 | in Socrates's own day | Socrates writes that the strict discipline of the Novatian church is kept to his own day in Phrygia and Paphlagonia, where, he says, people are temperate and rarely go to the circus or the theater. | Socrates, Church History IV.28, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 14060-14061, 14109-14115 |  | npnf202_socrates-sozomen-ecclesiastical-histories.xml 14060-14061: "provinces of Phrygia and Paphlagonia"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 14113-14115: "theatrical" |
| 27 | 21 July, in the sixteenth consulate of Theodosius, so 438 | Socrates writes that Paul, bishop of the Novatians, died, and that all the sects followed his body to the grave, singing psalms. Before he died, he named Marcian, a presbyter he had trained, to follow him. | Socrates, Church History VII.46, cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml lines 21490-21535; the consulate, lines 21469-21471, 21491-21492; the year is a conversion from the consulate |  | npnf202_socrates-sozomen-ecclesiastical-histories.xml 21490-21492: "Paul bishop of the Novatians died"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 21496-21498: "chanting psalms together"; npnf202_socrates-sozomen-ecclesiastical-histories.xml 21521-21524: "Marcian" |

## briefSources

The old sources the brief draws on (Decius and the lapsed; Novatian's teaching and consecration; Cornelius; the Katharoi; the churches in the East; Nicaea, its bishop and its eighth canon; Novatian's death) and Novatian's own book.

- Church History, with Cornelius's letter to Fabius, and Life of Constantine, in English | Eusebius of Caesarea | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`
- Letters, with those of Cornelius and the Roman confessors, and Novatian, On the Trinity, in English | Cyprian of Carthage | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`
- Church History, in English | Socrates of Constantinople | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml`
- The canons of the Council of Nicaea, in English | Council of Nicaea | `cic/texts/npnf214_seven-ecumenical-councils.xml`
- Lives of Illustrious Men, in English | Jerome | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`
- Chronicle, in Jerome's Latin | Eusebius of Caesarea | `cic/texts/jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`

## uncertain

New, seven items, each from held lines, in its witness's voice.

1. Novatus or Novatian. Evidence: HE 38265-38270 and 38381 (Novatus); SOC 14061-14069 (Novatus); ANF5 33971-33972 (Novatian); VI 40887-40891 ("Novatianus ... Novatus, author of this doctrine, was a presbyter of Cyprian"); JerChron 43969-43973.
2. How he was made bishop. Evidence: HE 38518-38534 (Cornelius's account). No letter of Novatian on it is held.
3. What he taught about the fallen. Evidence: HE 38265-38268; SOC 14082-14094; SOC 3700-3716.
4. The name. Evidence: HE 38268-38270; NIC 3769-3770, 3785.
5. Their own words. Evidence: ANF5 60470-60474 (On the Trinity); ANF5 33288-33301 (the confessors' letter, written after their return to Cornelius, 33293). The census `voices[4]` says the congregations' story is "told almost entirely by outside historians"; this item gives the held basis.
6. Novatian's death. Evidence: SOC 14132-14133. The brief's "the record on that is not firm" is the census's; no held line gives a second account.
7. Their faith. Evidence: SOC 3694-3697; 15349-15366 (and 15291, Agelius bishop of the Novatians).

## Menu sections: what fills each

| Section | Held now | Field |
|---|---|---|
| Timeline | yes | `timeline` above (new) |
| People and stories | yes | census `people` (Cornelius, Cyprian, `novatian`, `socrates-of-constantinople`), `voices` (5), `documentedStories` (2: "The Confessors Come Back", "The Peasants of Mantinium Take Up Sickles") |
| Kind's own sections | nothing held | a Christian Tradition has no `entry` |
| Connections | yes | census `relationsSummary` and edges |
| Legacy and today | yes | census `legacy`, `why`, `teaser`, `livingEvidence` ("ended"; see Not found) |
| Open questions | yes | `uncertain` above (7); census `floorNote`, `statusDescription` |
| Sources | the short list | `briefSources` above; the census entry has no card `sources` |
| Modern works | proposed | `modernWorks` under Entry fields |

## Entry fields

**`modernWorks` (new on the entry)**, under Mark's ruling "Modern works on the cards" (Header.md): editions held in `cic/texts/`, public domain by date (`CORPUS-USE.md`), titles and publishers from the file headers. Each note says what the work covers. None is the source of a claim, date or identification on the card. The ANF and NPNF translations stand behind the timeline as its English and are not listed, as on the sibling cards.

```json
[
 {"title": "Novatiani Romanae urbis presbyteri De Trinitate liber (Cambridge Patristic Texts)", "author": "W. Yorke Fausset (ed.)", "year": "1909", "publisher": "Cambridge University Press", "note": "The Latin text of Novatian's On the Trinity, with an English introduction."},
 {"title": "Socratis Scholastici Ecclesiastica Historia, volume 1", "author": "Robert Hussey (ed.)", "year": "1853", "publisher": "Oxford University Press", "note": "The Greek text of Socrates's Church History, with a Latin version."},
 {"title": "S. Thasci Caecili Cypriani Opera omnia, part 2: the letters (Corpus scriptorum ecclesiasticorum latinorum 3.2)", "author": "Wilhelm von Hartel (ed.)", "year": "1871", "publisher": "C. Gerold, Vienna", "note": "The Latin text of Cyprian's letters, with those of Cornelius and the Roman confessors."},
 {"title": "Eusebii Pamphili Chronici canones, Latine vertit, adauxit, ad sua tempora produxit S. Eusebius Hieronymus", "author": "John Knight Fotheringham (ed.)", "year": "1923", "publisher": "Humphrey Milford, London", "note": "The Latin text of Jerome's Chronicle, with its entries on Decius, Cornelius and Novatus."}
]
```

The Hartel letters are held as the scan (`cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`) and as a TEI file under CC BY-SA 4.0 (`cyprian_epistulae-lat_hartel1871-csel3-tei.txt`); the entry lists the printed edition, which is public domain by date.

The documented story "The Peasants of Mantinium" lists T. E. Gregory, Vox Populi (1979), in its own `sources` as a reference. It is not on the card and is not moved; whether it may stand in `modernWorks` under the rights rules is for Mark.

**`end` 400**, for Mark or the release: it falls before the card's last witnesses (above). Not changed here (map placement).

`dates` is carried in the layout as a field so its change can be applied.

## Not found, and conflicts with the census entry

The card must not contradict the entry's other fields. Each conflict, and each claim no held line opened supports, is listed for the checker and Mark; none is edited, and the brief is kept as it stands.

- **The brief (`longDescription`):** "Decius ordered every subject of the empire to sacrifice in 250" (no held line opened gives the order or the year; the Chronicle says he began a persecution in his first year, JerChron 43895-43899); "the most learned theologian in the Roman church and the first there to write substantial theology in Latin" (a modern judgment; not held); "one of the earliest such rival consecrations the city had seen" (not held); "At the end of the fourth century they still held several churches in Constantinople and more across Phrygia and Bithynia" (Socrates gives three churches in Constantinople under Constantius, SOC 9091, and Phrygia and Paphlagonia in his own day, SOC 14060-14061; Bithynia is not found); "terms they largely declined" (not held); "though the record on that is not firm" (only Socrates is held, SOC 14132-14133); a dash for drama ("Novatian — the most learned..."; "— terms they largely declined").
- **`why`:** "the church had no authority to forgive such apostasy, however much God might" agrees with Socrates (SOC 14088-14090, 3714-3716). "Decius' order to sacrifice in 250": as above.
- **`teaser`:** "a rival church founded the day a Roman theologian decided" (no held line gives a founding day or a decision); "from 251 CE into the centuries after" (map years).
- **`floorNote`:** "The break was over discipline ... not over belief" is a "not X but Y" turn; the substance agrees with Acesius in Socrates (SOC 3694-3697) and canon 8 (NIC 3769-3779). "accepted the council's creed": Socrates says Acesius agreed the council set down nothing new (SOC 3692-3697).
- **`legacy`:** "the last Novatianist communities faded in the East by around the seventh century" (not held; the card's last witness is Socrates, 438), repeated in `livingEvidence.basis`; "the church is a hospital rather than a society of the already-perfect" (a modern judgment and a "not X but Y" turn); "worked out ... by Augustine at length afterwards" (not held here); "handed down in manuscripts among the works of Tertullian" (not held; Jerome says many wrongly ascribe On the Trinity to Cyprian, VI 40896-40897).
- **`sourcing`:** "Novatian's De Trinitate is broadly orthodox" (a judgment, not a held line).
- **`voices[0]`:** "consecrated rival bishop of Rome in 251" (the year is the Chronicle's clue for Novatus's coming, line 10, not for the consecration).
- **`documentedStories[0]` ("The Confessors Come Back"):** its quotations "circumvented by crafty and deceitful words" and "we were ignorant" are not found at the held lines: Cornelius's letter reads "circumvented and almost deceived and alienated from the Church by the craft and malice of that wily and subtle man" (ANF5 32953-32956), and the confessors' letter (ANF5 33288-33303) has no "we were ignorant". "Nicostratus ... went to Africa with Novatian's party" was not checked (ANF5 33132-33135 names him among the party). Its `verification` already says "primary text not yet read". "two hundred years" is not held.
- **`documentedStories[1]` ("The Peasants of Mantinium"):** "the Homoian bishop" (a modern term; Socrates says Macedonius made them "receive the Arian opinion", SOC 9108-9109); "with wedges driven between their teeth", "Sozomen repeats the story" and "in no imperial source" were not checked; "Most of the troops were killed; so were very many of the farmers" agrees with SOC 9112-9113.
- **`people[0]`:** Cornelius's quote stands at HE 38383-38385.
- Four faults re-read. Where the sources differ, both are told: the names (line 4 note, line 10 note, `uncertain` 1), the teaching on the fallen (Eusebius, line 8, against Socrates, line 16). Opponents' charges stay in their voices (lines 5, 7, 8, 15). No modern view, year or identification: no 250 order, no 325, no 383, no "Homoian", no "orthodox". Dates on their own events: 251 on Novatus's coming (line 10), not on Cornelius's election; 438 on Paul's death. Force kept: the oath at communion (7), the synod's sentence (9), the soldiers and the farmers' dead (24), Cyprian's "is not a Christian" (15).

## The card standard (Header.md)

Re-read after drafting. Each timeline line names its subject and witness and reads alone; none leans on the line before ("one of the three bishops who made Novatian a bishop", line 6; "Constantine answered Acesius", line 22; "in Macedonius's time", line 24). No hook, reveal, arc or closing image. Glossed where first met: Cathari, "the pure" (line 8, the editor's note "καθαροί, 'pure'", HE 38270); confessors, "who had confessed the faith under persecution" (line 12, from "the glory of confession", ANF5 32857); the mysteries, "the sacraments" (line 16); the doxology does not appear. No "Church in Conversation" in any visitor field.

Readability (`python -m engine.m1.profile_readability` on a plain file of the short description, headlines, timeline lines, notes and `uncertain`): 1507 words, grade 9.2 (names out 7.1), reading ease names out 74.3, 16.7 words a sentence: pass. Longest sentence 41 words. The short description alone: grade 9.6 (names out 7.4), ease 76.8: pass.

## Validation

The same census copy as `Card_Edits_ebionite-nazoraean-current.md` (`/tmp/claude-0/cards-era1-w7/census-copy.json`, the three layouts merged, `dates` included), `node tools/validate-census.mjs <copy>`: no error on this entry; 0 errors overall once the Ebionite drop reading is added (that file, Validation). A planted stray timeline key on this entry gave an error, so the entry checks ran. Every timeline line's verbatim was matched at its lines by script: 41 of 41. Nothing in the repository's census or tools was edited.
