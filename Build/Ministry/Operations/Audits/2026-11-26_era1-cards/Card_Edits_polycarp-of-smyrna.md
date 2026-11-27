# Card edits: polycarp-of-smyrna (person)

Layout fields for the census entry's `card`, written to `polycarp-of-smyrna.layout.json` beside this file. Worked from the census entry (its brief `longDescription` and its `card`), the batch-6 folder `Build/Ministry/Operations/Audits/2026-11-19_batch-6/polycarp-of-smyrna/` (brief and card there are identical to the census), the source sheet `Build/Ministry/Operations/Audits/2026-11-16_polycarp-clean-write/Source_Sheet.md`, and the held texts at their lines. The brief is not touched. Every quote below was re-read at its line by a script that strips the XML tags and the editors' notes (the editors' note lines are cited only where the quote is the editor's).

## Shown dates (date rule)

- **`dates`: change.** Census `"c. 110-155"` to **`"2nd c."`**. No old source gives a year for his birth or death (Martyrdom 21 gives a day and month only, ANF 4284-4290; Source_Sheet N1, N2). 110 and 155 are modern reckonings (McGiffert's note, EUS 23049: "probably in 155"). The second century follows from the reigns the old sources name (Anicetus; Verus, EUS 23043; Marcus Antoninus, JER 39850-39851), dated by Widely Accepted chronology, as the Epiphanius ruling did ("4th c.").
- **`card.datesNote`: change proposed.** Drop its fourth sentence, "Modern editors differ: Arthur Cushman McGiffert dates the death to 155 or 156, and a note in the Ante-Nicene Fathers to about 167." It shows modern dates on the card, which Part 1's Rigor rule keeps off; the same facts stay in `uncertain` ("The visit to Rome", "The eighty-six years"), where they are named as modern. The rest stands word for word.
- `start`, `end`, `activeYear` (110, 155, 155) only place it on the map: unchanged.

## Short description

"Polycarp was bishop of the church in Smyrna and wrote a letter to the church at Philippi. As an old man he was put to death at Smyrna, after telling the governor he had served Christ for eighty-six years."

Rulings met: two sentences, simpler than the Montanism model; no negative or contrast (the refusal to curse is told as what he said); opens on his name, not a placeholder; he is named by what he was at the moment (bishop; an old man); "governor" is the brief's word for the proconsul; every claim on a held line (table, rows "Short description"). No quotation marks: the eighty-six years are narrated.

## Timeline

Four periods, built after the brief from the source sheet, the census card and the held texts. Where one witness carries a period it is named once at the head (Irenaeus for period 2; the church of Smyrna for period 3). Lines are "Date unknown" or the record's own phrase where no old source gives a year (Open-Gaps 429). Notes mark a wonder, a contested point or a later source.

1. **Date unknown: "Bishop of Smyrna, and a friend of Ignatius."** His appointment; Ignatius at Smyrna and Troas; his letter to Philippi.
2. **In the time of Anicetus, bishop of Rome: "A visit to Rome, and a boy who listened."** Irenaeus hears him; the Easter difference and the peace; the heretics turned away; Marcion.
3. **Date unknown; a great Sabbath, the second day of the month Xanthicus: "Hunted, tried and put to death at Smyrna."** The Martyrdom, chapters 3 to 21.
4. **After his death: "Remembered, copied and cited."** Irenaeus, Polycrates and Victor, Tertullian, the copyists, Eusebius, Jerome.

Left out of the timeline as the brief and card leave them out: the dove, the burning pillow, the voice from heaven, the sweet smell (wonders the card's `uncertain` already sets aside), and the late epilogue's trumpet voice (Source_Sheet M37, Inferential-Thin).

## briefSources

The old works the brief draws on, each file held under `cic/texts/`: the Martyrdom in English (anf01) and Greek (Gebhardt, for "Let the will of God be done" and "to train and prepare", the card's `quotationOriginals`); the Epistle to the Philippians (anf01); Irenaeus, Against Heresies III.3.4 and the letter to Florinus (anf01); Eusebius IV.14 and V.24 with Irenaeus's letter to Victor (npnf201); Jerome, Lives 17 (npnf203). Tertullian is not listed: the brief does not draw on him (he stays in the card's `sources`).

## uncertain

The existing eleven items are kept word for word; none contradicts the brief (checked item by item: the arrest at the second farm matches "he withdrew to a farm, and then to another. There searchers seized"; the visit-to-Victor span matches "Decades after that visit"). Two new items, for points the timeline now shows:

- **"Marcion."** Irenaeus gives no place (ANF 39882-39883, "who met him on one occasion"); Jerome puts it at Rome in Anicetus's time (JER 39843-39849). Source_Sheet D13.
- **"The twelve martyrs."** Martyrdom 19 (ANF 4239-4240) against Eusebius (EUS 23608-23610). Source_Sheet D7.

## Evidence for every field and line

| Field | Claim | Work | File | Line | Quote (verbatim at the line) |
|---|---|---|---|---|---|
| Short description | Bishop of the church in Smyrna | Martyrdom of Polycarp 16 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4167-4169 | "bishop of the Catholic Church which is in Smyrna" |
| Short description | Wrote a letter to the church at Philippi | Polycarp, Epistle to the Philippians, opening | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3233-3234 | "to the Church of God sojourning at Philippi" |
| Short description | An old man | Martyrdom of Polycarp 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3925-3926 | "so godly and venerable an old man" |
| Short description | Put to death at Smyrna | Martyrdom of Polycarp 19 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4238-4239 | "the twelfth that was martyred in Smyrna" |
| Short description | Told the governor he had served Christ eighty-six years | Martyrdom of Polycarp 9 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3990 | "Eighty and six years have I served Him" |
| Timeline P1 | Made bishop by apostles in Asia, Irenaeus says | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39859-39860 | "by apostles in Asia, appointed bishop of the Church in Smyrna" |
| Timeline P1 note | Tertullian: Smyrna's records name John | Tertullian, Prescription 32 | `cic/texts/anf03_tertullian.xml` | 21462-21463 | "records that Polycarp was placed therein by John" |
| Timeline P1 note | Jerome: John ordained him | Jerome, Lives 17 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 39840-39841 | "disciple of the apostle John and by him ordained bishop of Smyrna" |
| Timeline P1 | Ignatius writes from Smyrna, loving Polycarp | Ignatius, Ephesians 21 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 5581-5583 | "whence also I write to you, giving thanks unto the Lord, and loving Polycarp even as I do you" |
| Timeline P1 | Ignatius a prisoner on his way to Rome | Eusebius, Church History III.36.5 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19961-19962 | "So when he came to Smyrna, where Polycarp was" |
| Timeline P1 | Ignatius has seen his blameless face | Ignatius to Polycarp 1 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 8551-8552 | "thy blameless face" |
| Timeline P1 | Ignatius asks him to call a council and send a messenger | Ignatius to Polycarp 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 8813-8818 | "to assemble a very solemn" |
| Timeline P1 | Ignatius sails from Troas and asks him to write to the nearby churches | Ignatius to Polycarp 8 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 8860-8861 | "wilt write to the adjacent Churches" |
| Timeline P1 | Polycarp and the presbyters with him write to Philippi | Philippians, opening | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3232-3233 | "Polycarp, and the presbyters" |
| Timeline P1 | Philippi had invited him to write about righteousness | Philippians 3 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3306-3307 | "concerning righteousness, not because I take anything upon myself, but because ye have invited me to do so" |
| Timeline P1 | Warns against deniers of Christ in the flesh, resurrection and judgment | Philippians 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3438-3439 | "says that there is neither a resurrection nor a judgment" |
| Timeline P1 | The word handed down from the beginning | Philippians 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3442-3443 | "let us return to the word which has been handed down to us from" |
| Timeline P1 | Grieves over Valens, once a presbyter there | Philippians 11 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3531-3532 | "I am greatly grieved for Valens, who was once a presbyter among you" |
| Timeline P1 note | Chapters 10 to 12 survive only in Latin | ANF note to Philippians | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3501-3503 | "preserved only in a Latin version" |
| Timeline P1 | Sends Ignatius's letters and all the others | Philippians 13 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3614-3618 | "and all the rest [of his Epistles] which we have by us, we have sent to you" |
| Timeline P1 | Promises to carry their letter to Syria if he finds an opportunity | Philippians 13 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3609-3611 | "which request I will attend to if I find a fitting opportunity" |
| Timeline P2 witness | Irenaeus heard him as a boy | Irenaeus, letter to Florinus | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 54568-54569 | "while I was yet a boy, I saw thee in Lower Asia with Polycarp" |
| Timeline P2 | Irenaeus can describe the place he sat; John and others who had seen the Lord | Irenaeus, letter to Florinus | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 54576-54581 | "the place where the blessed Polycarp used to sit and discourse" |
| Timeline P2 | Spoke of John and those who had seen the Lord | Irenaeus, letter to Florinus | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 54579-54581 | "his familiar intercourse with John, and with the rest of those who had seen the Lord" |
| Timeline P2 | At Rome under Anicetus; neither persuades the other | Irenaeus to Victor, Eusebius V.24.16 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31591-31612 | "neither could Polycarp persuade Anicetus to observe it" |
| Timeline P2 | Polycarp kept what he had kept with John and the apostles | Irenaeus to Victor, Eusebius V.24.16 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31603-31606 | "what he had always observed with John the disciple of our Lord, and the other apostles" |
| Timeline P2 | Anicetus the customs of the presbyters before him | Irenaeus to Victor, Eusebius V.24.16 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31607-31609 | "the customs of the presbyters that had preceded him" |
| Timeline P2 | They share communion | Irenaeus to Victor, Eusebius V.24.17 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31609-31610 | "they communed together" |
| Timeline P2 | They part in peace | Irenaeus to Victor, Eusebius V.24.17 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31655-31657 | "And they parted from each other in peace" |
| Timeline P2 note | Eusebius names the paschal feast | Eusebius IV.14.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 22849-22869 | "paschal" |
| Timeline P2 | Turned many away from the heretics at Rome | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39872-39874 | "caused many to turn away from the aforesaid heretics to the Church of God" |
| Timeline P2 | Marcion: first-born of Satan | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39882-39884 | "I do know thee, the first-born of Satan" |
| Timeline P2 note | Jerome puts the meeting at Rome | Jerome, Lives 17 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 39846-39849 | "when Marcion met him by chance" |
| Timeline P3 when | Second day of Xanthicus, great Sabbath, no year | Martyrdom 21 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4284-4290 | "on the great Sabbath, at the eighth hour" |
| Timeline P3 | Germanicus and the beasts; Away with the Atheists; Polycarp sought out | Martyrdom 3 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3819-3835 | "Away with the Atheists; let Polycarp be sought out!" |
| Timeline P3 | Quintus the Phrygian sacrifices; no praise for those who give themselves up | Martyrdom 4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3843-3849 | "we do not commend those who give themselves up" |
| Timeline P3 | At the wish of many, to a country house; prays for all and the churches | Martyrdom 5 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3860-3865 | "in deference to the wish of many" |
| Timeline P3 | Another house; two youths seized; one confesses under torture | Martyrdom 6 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3878-3881 | "they seized upon two youths [that were there], one of whom, being subjected to torture, confessed" |
| Timeline P3 | Friday evening, the day of the preparation | Martyrdom 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3899-3901 | "on the day of the preparation" |
| Timeline P3 | He could have escaped; the will of God be done | Martyrdom 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3905-3909 | "from which he might have escaped into another place" |
| Timeline P3 | Food and drink; two hours of prayer | Martyrdom 7 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3918-3925 | "for two full hours" |
| Timeline P3 | On a donkey into the city on the great Sabbath | Martyrdom 8 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3938-3940 | "they set him upon an ass" |
| Timeline P3 | Herod the Irenarch and Nicetes urge Lord Caesar and sacrifice | Martyrdom 8 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3940-3951 | "What harm is there in saying, Lord Cæsar" |
| Timeline P3 | Thrown from the carriage; hurts his leg | Martyrdom 8 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3957-3960 | "he dislocated his leg" |
| Timeline P3 | Proconsul: swear and I will set thee free, reproach Christ | Martyrdom 9 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3988-3990 | "Swear, and I will set thee at liberty, reproach Christ" |
| Timeline P3 | Threatened with fire; fire that burns for an hour | Martyrdom 11 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4035-4036 | "Thou threatenest me with fire which burneth for an hour" |
| Timeline P3 | Teacher of Asia, overthrower of our gods | Martyrdom 12 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4055-4058 | "the overthrower of our gods" |
| Timeline P3 | Philip the Asiarch; beast shows over; burnt alive | Martyrdom 12 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4061-4065 | "seeing the shows" |
| Timeline P3 | Fire like a ship's sail around the body | Martyrdom 15 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4142-4144 | "like the sail of a ship when filled with the wind" |
| Timeline P3 note | The church as witness, no eyewitness named | Martyrdom 15 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4140-4141 | "we, to whom it was given to witness it" |
| Timeline P3 | Body not consumed; executioner with a dagger | Martyrdom 16 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4158-4160 | "pierce him through with a dagger" |
| Timeline P3 | Nicetes asks the governor not to give up the body | Martyrdom 17 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4190-4191 | "entreat the governor not to give up his body" |
| Timeline P3 | Centurion burns it; bones in a fitting place; birthday of his martyrdom | Martyrdom 18 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4217-4224 | "deposited them in a fitting place" |
| Timeline P3 | The twelfth martyred in Smyrna, with Philadelphia | Martyrdom 19 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4239-4240 | "reckoning those also of Philadelphia" |
| Timeline P3 | Account sent on to the brethren farther away | Martyrdom 20 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4266-4268 | "send it to the brethren at a greater distance" |
| Timeline P3 | Addressed to Philomelium | Martyrdom, address | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 3750 | "Church of God sojourning in Philomelium" |
| Timeline P3 note | Eusebius: under Verus | Eusebius IV.15 heading | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 23043 | "Under Verus," |
| Timeline P3 note | Marcus Aurelius Verus followed Antoninus Pius | Eusebius IV.14.10 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 23032-23036 | "Marcus Aurelius Verus, his son, who was" |
| Timeline P3 note | Jerome: reign of Marcus Antoninus and Lucius Aurelius Commodus | Jerome, Lives 17 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 39850-39851 | "during the reign of Marcus Antoninus and Lucius Aurelius Commodus" |
| Timeline P4 | More steadfast witness of truth than Valentinus and Marcion | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39870-39871 | "a more stedfast witness of truth, than Valentinus, and Marcion" |
| Timeline P4 | Irenaeus commends the letter | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39889-39893 | "Epistle of Polycarp written to the Philippians" |
| Timeline P4 | Victor tries to cut off Asia | Eusebius V.24.9 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31415-31417 | "attempted to cut off from the common unity the parishes of all Asia" |
| Timeline P4 | Polycrates writes to Victor | Eusebius V.24.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31314-31316 | "a letter which he addressed to Victor" |
| Timeline P4 | Great lights of Asia | Eusebius V.24.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31325-31326 | "great lights have fallen asleep" |
| Timeline P4 | Polycarp in Smyrna, bishop and martyr | Eusebius V.24.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31338 | "in Smyrna, who was a bishop and martyr" |
| Timeline P4 | Irenaeus a peacemaker | Eusebius V.24.18 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 31662-31663 | "became a peacemaker in this matter" |
| Timeline P4 | Tertullian: placed there by John | Tertullian, Prescription 32 | `cic/texts/anf03_tertullian.xml` | 21462-21463 | "records that Polycarp was placed therein by John" |
| Timeline P4 | Copy chain: Gaius, Socrates, Pionius | Martyrdom, closing note | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4315-4321 | "I Socrates transcribed them at Corinth from the copy of Caius" |
| Timeline P4 note | The note is not part of the letter | Martyrdom, closing note | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4313-4316 | "What follows is, of course, no part of the original Epistle." |
| Timeline P4 | Eusebius copies most of it | Eusebius IV.15.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 23078-23079 | "There is a letter, written in the name of the church over which he himself presided" |
| Timeline P4 | Jerome: read in the meetings in Asia | Jerome, Lives 17 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 39853-39855 | "read to the present day in the meetings in" |
| Uncertain: Marcion | Irenaeus gives no place | Irenaeus, Against Heresies III.3.4 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 39882-39883 | "who met him on one occasion" |
| Uncertain: Marcion | Jerome: at Rome, while Anicetus ruled | Jerome, Lives 17 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 39843-39849 | "went to Rome in the time of the emperor Antoninus Pius while Anicetus ruled the church in that city" |
| Uncertain: twelve martyrs | Twelfth, reckoning Philadelphia | Martyrdom 19 | `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` | 4239-4240 | "being the twelfth that was martyred in Smyrna (reckoning those also of Philadelphia)" |
| Uncertain: twelve martyrs | Eusebius: with eleven from Philadelphia | Eusebius IV.15.45 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 23608-23610 | "eleven" |
## The menu sections (Stage-Two-Kit section 1), and what fills each

| Section | Filled from | Held? |
|---|---|---|
| On screen: short description | new `card.shortDescription` | yes |
| On screen: direct line | `toldWithin` (`post-apostolic-house-church`) and its `people` row for him; `relationsSummary` | yes, one step up; no census `edges` touch this entry |
| Below: the brief (Read along) and its old sources | `longDescription`; new `card.briefSources` | yes |
| Timeline | new `card.timeline` | yes |
| People and stories | No person entries act beside him on the tree in his card. Documented stories: none told under him. Nearest held: "The Marcionites Who Died Beside the Catholics" (`marcion-marcionism`), which mentions the Smyrna martyrdoms Eusebius appends to his story; not his own | nothing held for him yet |
| Key works | `card.keyWorks` (Epistle to the Philippians) | yes |
| Connections | `relationsSummary`; `voices`; the direct line above. No census edge names him | thin: prose only |
| Legacy and today | `card.legacy.traces`, `card.legacy.remembered`; entry `legacy` (Socrates, Sozomen, the Martyrs' Mirror) | yes; nothing on "today" |
| Open questions | `card.uncertain` (13 items with the two new) | yes |
| Sources | `card.sources.ownWords`, `card.sources.about` | yes |
| Modern works | none: the entry has no `modernWorks`. McGiffert's and the ANF editors' notes sit in `card.sources.about` ("Editors' notes ..."), and McGiffert is named in `uncertain` | nothing held; see Entry fields |

## Entry fields (for release to apply if the checker passes)

- `dates`: "c. 110-155" to "2nd c." (above).
- `teaser`: "Smyrna, c. 110 to 155 CE: ..." shows the modern years. Proposed: "Smyrna, in the second century: an old bishop who told the proconsul he had served Christ eighty-six years, and would not curse him." Only the date clause changes.
- `sourcing`: "Most scholars now say about 155. Jerome and the Chronicle of Eusebius point to 167." states modern dates and a "most scholars" judgment on a shown field. Flagged for the fix, not rewritten here.
- `modernWorks`: none listed. The card's `sources.about` item "Editors' notes to Polycarp, the Martyrdom and Irenaeus, in Ante-Nicene Fathers vol. 1" is a modern work under the role's rule and would move there word for word; McGiffert's notes ride inside the Eusebius item. Flagged, not moved (layout fields only in this task).

## Not found

Nothing in the new fields lacks a held line. Carried, not mine: the existing `datesNote` sentence "The second century comes from the modern dating of those reigns" is consistent with the date rule and kept.

## Four faults, re-read

1. Differences credited: who made him bishop (note, period 1), the feast's name (note, period 2), Marcion's place (note), the death's reign (note, period 3). 2. No modern view as the record: the only modern date is gone from the shown dates; McGiffert stays only in `uncertain`. 3. Dates on the right event: the Sabbath and Xanthicus sit with the death; "In Victor's time" with Victor's attempt; nothing dated by a reckoning from a neighbor. 4. Force kept: the betrayal under torture, the fire, the dagger, the crowd's cry, Quintus's fall and the church's word against volunteering are all on the timeline; the wonder stays in the church's voice.
