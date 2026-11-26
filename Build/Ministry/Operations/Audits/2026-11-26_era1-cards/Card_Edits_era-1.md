# Card edits: era 1 (The Early Church Era)

Writer: card writer 3, 2026-11-26. Rule: `Header.md` in this folder; Stage-Two-Kit sections 1 to 3; `Brief-Kit/kinds/era.md` (an era may also draw on the broad scholarship; here every line still rests on a held line opened and read). The era has no brief yet, so the card has no `briefSources` and no `quotationOriginals`.

## Fields written

`era-1.layout.json` is the census `eras` entry with `num` 1, every existing field word for word, and three fields added: `shortDescription`, `timeline`, `uncertain`. No existing field changed.

Validation: merged into a copy of the census at `/tmp/claude-0/cards-era1-w3/census.json` and run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (all four are shortName warnings on other entries, already present).

## Dates

Years shown (70, 177, 250, 303, 311, 312) are each either fixed by the old source's own reckoning (Vespasian's second year; the seventeenth year of Antoninus Verus; the nineteenth year of Diocletian) or Widely Accepted. Every other line gives the record's own phrase ("in Trajan's reign", "in the reign of Severus") or "date unknown". The period heads "About 200 to the 250s" and "Under Valerian and Gallienus" are spans for grouping only.

## Evidence

Line numbers are the file's own lines. Quotes are copied from the file with XML tags and footnotes removed and line breaks joined.

### shortDescription

| Claim | Work | File | Line | Quote |
|---|---|---|---|---|
| Temple burned in 70 (year Widely Accepted) | Josephus, Jewish War VI.4.7 (Whiston) | `cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt` | 126019-126020 | "thus was the holy house burnt" |
| Jerusalem taken in Vespasian's second year | Josephus, Jewish War VI.10.1 | `cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt` | 127565-127566 | "thus was Jerusalem taken, in the second year of the reign of Vespasian" |
| Constantine's victory at Rome (312, Widely Accepted) | Eusebius, Church History (McGiffert, NPNF 2.1) IX.9.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 48390-48392 | "Maxentius was defeated at Rome by Constantine" |
| Churches at Lyons | Eusebius, Church History (McGiffert, NPNF 2.1) V.1.1-2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 26796-26804 | "Lyons and Vienne" |
| Church at Rome (its bishop) | Eusebius, Church History (McGiffert, NPNF 2.1) VI.39.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37414-37415 | "Fabianus suffered martyrdom at Rome" |
| Church at Carthage | Eusebius, Church History (McGiffert, NPNF 2.1) VII.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39310 | "Cyprian, pastor of the parish of Carthage" |
| Churches at Alexandria | Eusebius, Church History (McGiffert, NPNF 2.1) VI.35 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37079-37080 | "received the episcopate of the churches of Alexandria" |
| Christians in Asia (Asia Minor) | Eusebius, Church History (McGiffert, NPNF 2.1) V.16.10 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 29721-29722 | "the faithful in Asia met often in many places throughout Asia" |
| A church at Edessa | Chronicle of Edessa 8 (Cowper) | `cic/texts/chronicle-of-edessa_cowper.txt` | 53 | "they destroyed the temple of the church of the Christians" |
| Emperors ordered Christians punished | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19542-19543 | "when found should be punished" |
| ...and churches torn down | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43487-43488 | "commanding that the churches be leveled to the ground" |

### timeline

| Claim | Work | File | Line | Quote |
|---|---|---|---|---|
| Pella: the Jerusalem church leaves by revelation before the war | Eusebius, Church History (McGiffert, NPNF 2.1) III.5.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 15291-15294 | "commanded by a revelation, vouchsafed to approved men there before the war, to leave the city and to dwell in a certain town of Perea called Pella" |
| 70: Temple burned | Josephus, Jewish War VI.4.7 | `cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt` | 126019-126020 | "thus was the holy house burnt" |
| 70: Jerusalem taken in Vespasian's second year | Josephus, Jewish War VI.10.1 | `cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt` | 127565-127566 | "in the second year of the reign of Vespasian" |
| Pliny, a governor, troubled by the martyrs | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19448-19449 | "Plinius Secundus, one of the most noted of governors, being disturbed by the great number of martyrs" |
| Christians sing hymns to Christ at dawn | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19535-19537 | "they arose at dawn and sang hymns to Christ as a God" |
| Trajan: not sought, punished if found | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19541-19543 | "the race of Christians should not be sought after, but when found should be punished" |
| No great persecutions; local ones by people or rulers | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19546-19549 | "Sometimes the people, sometimes the rulers in various places" |
| (same) | Eusebius, Church History (McGiffert, NPNF 2.1) III.33.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 19548-19549 | "no great persecutions took place, local persecutions were nevertheless going on in particular provinces" |
| Asia: met often, examined, profane | Eusebius, Church History (McGiffert, NPNF 2.1) V.16.10 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 29721-29736 | "examined the novel utterances and pronounced them profane" |
| Asia: expelled, barred from communion | Eusebius, Church History (McGiffert, NPNF 2.1) V.16.10 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 29736-29738 | "expelled from the Church and debarred from communion" |
| 177: seventeenth year of Antoninus Verus | Eusebius, Church History (McGiffert, NPNF 2.1) V, Introduction 1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 26706-26707 | "In the seventeenth year of the Emperor Antoninus Verus" |
| Crowds in the cities | Eusebius, Church History (McGiffert, NPNF 2.1) V, Introduction 1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 26737-26738 | "an insurrection of the masses in the cities" |
| Lyons and Vienne churches send an account | Eusebius, Church History (McGiffert, NPNF 2.1) V.1.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 26803-26804 | "The most celebrated churches in that country sent an account of the witnesses" |
| Edessa flood in Severus's reign, year 513 | Chronicle of Edessa 8 | `cic/texts/chronicle-of-edessa_cowper.txt` | 53 | "In the year 513, in the reign of Severus" |
| Flood breaks the wall | Chronicle of Edessa 8 | `cic/texts/chronicle-of-edessa_cowper.txt` | 53 | "the waters broke down the western wall of the city" |
| Destroys the church | Chronicle of Edessa 8 | `cic/texts/chronicle-of-edessa_cowper.txt` | 53 | "they destroyed the temple of the church of the Christians" |
| Tertullian from Carthage, Africa | Jerome, Lives of Illustrious Men 53 (NPNF 2.3) | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 40496 | "was from the city of Carthage in the province of Africa" |
| Under Severus and Caracalla, many volumes | Jerome, Lives 53 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 40498-40499 | "he flourished chiefly in the reign of the emperor Severus and Antoninus Caracalla and wrote many volumes" |
| Writes in Latin (Jerome: chief of the Latin writers) | Jerome, Lives 53 | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` | 40495 | "now regarded as chief of the Latin writers" |
| 250: Decius succeeds Philip | Eusebius, Church History (McGiffert, NPNF 2.1) VI.39.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37383-37384 | "After a reign of seven years Philip was succeeded by Decius." |
| Decius begins persecution; Fabianus at Rome | Eusebius, Church History (McGiffert, NPNF 2.1) VI.39.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37413-37415 | "he commenced a persecution of the churches, in which Fabianus suffered martyrdom at Rome" |
| Dionysius at Alexandria: a year before the decree | Eusebius, Church History (McGiffert, NPNF 2.1) VI.41.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37808-37809 | "did not begin with the royal decree, but preceded it an entire year" |
| Stephen succeeds as bishop of Rome | Eusebius, Church History (McGiffert, NPNF 2.1) VII.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39212-39232 | "transmitted his office to Stephen" |
| Cyprian: baptize those from heresy | Eusebius, Church History (McGiffert, NPNF 2.1) VII.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39310-39311 | "should not be received except they had been purified from their error by baptism" |
| Stephen: no innovation against tradition | Eusebius, Church History (McGiffert, NPNF 2.1) VII.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39312-39313 | "unnecessary to add any innovation contrary to the tradition" |
| Valerian friendly at first | Eusebius, Church History (McGiffert, NPNF 2.1) VII.10.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39931-39933 | "he had been mild and friendly toward the men of God" |
| Valerian persuaded to persecute | Eusebius, Church History (McGiffert, NPNF 2.1) VII.10.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 39957-39959 | "persuaded him to change his course, urging him to slay and persecute pure and holy men" |
| Valerian enslaved by barbarians | Eusebius, Church History (McGiffert, NPNF 2.1) VII.13.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 40489 | "Valerian was reduced to slavery by the barbarians" |
| Gallienus stops persecution by proclamation | Eusebius, Church History (McGiffert, NPNF 2.1) VII.13.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 40494-40495 | "He immediately restrained the persecution against us by public proclamations" |
| Bishops free in their duties | Eusebius, Church History (McGiffert, NPNF 2.1) VII.13.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 40506-40507 | "directed the bishops to perform in freedom their customary duties" |
| Others to leave places of worship | Eusebius, Church History (McGiffert, NPNF 2.1) VII.13.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 40527-40528 | "that they may depart from the places of religious worship" |
| Plague after war | Eusebius, Church History (McGiffert, NPNF 2.1) VII.22.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 41026-41027 | "a pestilential disease followed the war" |
| War and famine | Eusebius, Church History (McGiffert, NPNF 2.1) VII.22.5 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 41065-41066 | "war and famine followed" |
| Christians nursed the sick fearlessly | Eusebius, Church History (McGiffert, NPNF 2.1) VII.22.7 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 41084-41087 | "visited the sick fearlessly" |
| Many died with them | Eusebius, Church History (McGiffert, NPNF 2.1) VII.22.7 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 41087-41088 | "they died with them most joyfully" |
| 303: Diocletian's nineteenth year, March, near Easter | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43460-43485 | "It was in the nineteenth year of the reign of Diocletian, in the month Dystrus, called March by the Romans, when the feast of the Saviour’s passion was near at hand" |
| Churches leveled, Scriptures burned | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43487-43489 | "commanding that the churches be leveled to the ground and the Scriptures be destroyed by fire" |
| Eusebius saw it himself | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43432-43433 | "when we saw with our own eyes the houses of prayer thrown down to the very foundations" |
| Scriptures burned in marketplaces | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43434-43435 | "committed to the flames in the midst of the market-places" |
| The persecutor struck by illness | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.16.3-5 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 45403-45428 | "intolerable sight to those who came near" |
| He orders the persecution stopped, churches built, prayers for the emperor | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.17.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 45446-45450 | "stop the persecution of the Christians, and should by law and royal decree, urge them forward to build their churches" |
| Decree in the name of Galerius (311, Widely Accepted) | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.17.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 45456-45457 | "Galerius Valerius Maximinus" |
| 312: Constantine advances on Rome | Eusebius, Church History (McGiffert, NPNF 2.1) IX.9.2-3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 48415-48433 | "was already very near Rome" |
| Maxentius defeated at Rome | Eusebius, Church History (McGiffert, NPNF 2.1) IX.9.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 48390-48392 | "Maxentius was defeated at Rome by Constantine" |
| Bridge of boats, the bridge breaks | Eusebius, Church History (McGiffert, NPNF 2.1) IX.9.5-7 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 48462-48475 | "the bridge over the river being broken" |

### uncertain

| Claim | Work | File | Line | Quote |
|---|---|---|---|---|
| Pella, no year | Eusebius, Church History (McGiffert, NPNF 2.1) III.5.3 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 15292-15293 | "before the war" |
| Mark's founding given as report | Eusebius, Church History (McGiffert, NPNF 2.1) II.16.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 11851-11853 | "they say that this Mark was the first that was sent to Egypt" |
| Thomas sent Thaddeus to Edessa | Eusebius, Church History (McGiffert, NPNF 2.1) I.13.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 9482-9487 | "sent Thaddeus" |
| From the archives of Edessa | Eusebius, Church History (McGiffert, NPNF 2.1) I.13.5 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 9500 | "taken from the archives of Edessa" |
| Hunts ordered by emperors: Decius | Eusebius, Church History (McGiffert, NPNF 2.1) VI.39.1 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 37413-37414 | "he commenced a persecution of the churches" |
| Hunts ordered by emperors: Diocletian | Eusebius, Church History (McGiffert, NPNF 2.1) VIII.2.4 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 43487-43488 | "royal edicts were published everywhere" |

## Sections not held as era fields

The validator allows only `shortDescription`, `briefSources`, `timeline`, `uncertain`, `modernWorks` and `quotationOriginals` for an era's card. The rest of the full section set has no era field:
- **Direct line, People and stories, Connections:** the era 1 traditions, people, councils and stories, which the site can draw from the census entries with `era` 1. Nothing written here.
- **Legacy and today:** nothing held yet for the era as a whole; it waits for the era brief.
- **Sources:** each timeline line carries its own. **Modern works:** none used, so `modernWorks` is left out.

## Re-read for the four faults

1. Differing sources or wonders: Constantine's victory is told as a battle and a broken bridge, without Eusebius's reading of it as God's act (lines 48435-48448); the persecutor's illness is told as Eusebius gives it, without his reading of it as judgment. The Pella line credits the revelation to Eusebius.
2. Modern views: none; "first empire-wide persecution", a modern judgment, was taken out of a draft headline. "Great Persecution" is the era's own `keyEvents` label.
3. Dates on the wrong event: Decius 250 sits on his accession and persecution; 311 on the decree; the plague sits under Gallienus, where Eusebius tells it (VII.22, after VII.13).
4. Force softened: the hunts, the burning of Scriptures, and the deaths of a bishop of Rome and of Christians nursing the sick are all kept.

## Not found, or flagged

- Nothing on the era card is unsupported. The era record's existing `tag` ("The apostles' children, under an empire that could turn on them") and `keyEvents` agree with the lines above.
