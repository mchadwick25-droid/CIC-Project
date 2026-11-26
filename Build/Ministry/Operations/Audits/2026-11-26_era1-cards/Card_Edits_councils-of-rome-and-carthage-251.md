# Card edits: councils-of-rome-and-carthage-251 (council)

Layout fields for the census entry's `council`, written to `councils-of-rome-and-carthage-251.layout.json` beside this file. Worked from the census entry (its brief `longDescription`, its `council` and `people`), the batch-7 folder `Build/Ministry/Operations/Audits/2026-11-20_batch-7/councils-of-rome-and-carthage-251/` (`Outline.md`, `Source_Sheet.md`; its brief and card are identical to the census), and the held texts at their lines. The brief is not touched. Every quote below was re-read at its line by a script that strips the XML tags and editors' notes.

## Shown dates (date rule)

- **`dates`: unchanged**, "251". The year of the two councils is Widely Accepted (Decius's persecution and Cornelius's election; Outline Setting, "Plain words: in 251"); Cyprian's own letter of the next year speaks of the council's letter as written "last year" (ANF 34763-34764: "wrote to you last year").
- **`council.datesNote`: change proposed.** Census: "251. Carthage probably in May and Rome probably in October, both by Charles Joseph Hefele's dating; no held source of the time gives the month". The months rest on one modern historian, which Part 1 keeps off shown dates. Proposed: **"251. The council at Carthage met first, and Cornelius's council at Rome then agreed with it; no held source of the time gives either month"** (order: ANF 33524-33529, Cyprian wrote to Cornelius, "who himself also holding a council ... concurred"). Hefele's months stay in `uncertain`, item 3, as his reconstruction. Checked by merging into a census copy: it validates.
- `start`, `end` unchanged.

## Short description

"Two councils of bishops, first at Carthage and then at Rome, decided how Christians who had given way in the persecution under the emperor Decius could come back to the church: through long penance, with each case examined. The council at Rome also cut off Novatian, a rival bishop of Rome, and his followers."

Rulings met: no negative or contrast; opens on the subject, not a placeholder; "given way" is the brief's own plain gloss of the lapsed, heard once with "in the persecution under the emperor Decius" so it stands clear; Novatian named by what he was then, a rival bishop of Rome. "Cut off" rests on the decree's "strangers" (EUS 38292-38294) and Eusebius's own "cutting off from the Catholic Church the leader of the heresy" (EUS 38324-38359). No quotation marks.

## Timeline

Six periods. A witness carrying a period is named once at its head (Cyprian for periods 1 and 3; Eusebius from Cornelius's letters for period 4). Lines without an old-source year say "Date unknown" or the record's own phrase ("In Socrates's day"). Notes mark the enemy's charge, the late and sympathetic witness, the lost book, the modern year for the African bishops' letter, and the absent link from Nicaea to 251.

1. **250: "Decius's order, and the many who gave way."**
2. **Before the councils of 251: "A lax party at Carthage, and two bishops at Rome."**
3. **251: "The council at Carthage chooses a middle way."**
4. **251: "The council at Rome agrees, and cuts off Novatian's party."**
5. **After the councils: "A charge against Cyprian, rival bishops at Carthage, and peace for all who kept repenting."** The 252 letter is "Date unknown" with Hefele's year in its note, as the outline's Do-not-say requires (a historian's dating, never "the next year" as fact).
6. **325 and after: "Novatian's church lives on."** Nicaea 325 is Widely Accepted.

Left out, as the outline leaves them out: the wonder stories of On the Lapsed 26; the 252 council's other business (Fidus); the roll of forty-two names.

## briefSources

The old works the brief draws on, each file under `cic/texts/`: On the Lapsed (Hartel's Latin); Cyprian's letters in Hartel's Latin and in the ANF English; Eusebius, Church History VI.43; Socrates IV.28 in English and in Hussey's Greek; Nicaea's canon 8. Hefele and Leclercq are modern and are not listed (they belong under Modern works).

## uncertain

The existing twelve items are kept word for word; none contradicts the brief (checked one by one; "The terms for those who had taken certificates" matches "Certificate holders were taken back case by case"). One new item:

- **"The year after."** The synodal letter gives no year (ANF 34273-34275 opens "We had indeed decided some time ago"); Hefele dates the council to "the Ides of May 252" (HEF 6504-6507). The brief already credits the year to "a historian's reckoning".

## Evidence for every field and line

| Field | Claim | Work | File | Line | Quote (verbatim at the line) |
|---|---|---|---|---|---|
| Short description | Carthage first, then Rome; Cornelius with very many bishops agreed | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33524-33529 | "who himself also holding a council with very many bishops, concurred in the same opinion as we had held" |
| Short description | Long penance, each case examined | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33519-33522 | "that repentance should be long protracted" |
| Short description | Each case examined | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33521-33522 | "the necessities of individuals be examined into" |
| Short description | Rome cut off Novatian and his followers | Eusebius VI.43.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38292-38294 | "should be considered by the" |
| Short description | Cut off from the church (Eusebius's own summary) | Eusebius VI.43 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38324-38359 | "cutting off from the Catholic Church" |
| Timeline P1 | The persecution the emperor Decius raised | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14069-14082 | "the Emperor Decius" |
| Timeline P1 | A very great number gave up their faith at the first threats | Cyprian, On the Lapsed 7 | `cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt` | 303-304 | "maximus fratrum numerus fidem suam prodidit" |
| Timeline P1 | They ran to the forum of their own accord | Cyprian, On the Lapsed 8 | `cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt` | 349-350 | "ultro ad forum currere" |
| Timeline P1 | Put off by the officials as evening pressed, and begged not to be | Cyprian, On the Lapsed 8 | `cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt` | 351-352 | "quot illic a magistratibus uespera urgente dilati sunt" |
| Timeline P1 | Certificate-holder paid a price so as not to sacrifice | Cyprian, Letter to Antonianus 14 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33705-33708 | "that I pay a price for this purpose, that I may not do what is not lawful for me to do" |
| Timeline P1 | Thousands of papers a day, no examination | Cyprian, Letter to the clergy at Rome 2 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 30201-30205 | "thousands of certificates were daily given" |
| Timeline P1 | Confessors pressed | Cyprian, Letter to the clergy at Rome 2 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 30201-30203 | "corrupting the confessors with importunate and excessive entreaties" |
| Timeline P1 | Confessors grant peace to all whose conduct satisfies him | Letter of the confessors | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 30385-30391 | "we have granted peace" |
| Timeline P1 | Ask him to make it known to the other bishops | Letter of the confessors | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 30388-30391 | "made known by you to the other bishops also" |
| Timeline P1 | Cyprian put off deciding until the bishops met | Cyprian, Letter to Antonianus 4 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33476-33477 | "But I put off deciding what was to be arranged about the case of the lapsed" |
| Timeline P1 | Anyone who gave communion first would be withheld | Cyprian, Letter to Antonianus 4 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33484-33487 | "he himself should be withheld from communion" |
| Timeline P1 | Roman clergy, Novatian writing: peace for the sick at the point of death | Cyprian, Letter to Antonianus 5 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33498-33502 | "that peace ought to be granted to the lapsed who were sick and at the point of departure" |
| Timeline P2 | The faction of Felicissimus | Cyprian, Letter to the people of Carthage 2 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32383-32384 | "the faction of Felicissimus" |
| Timeline P2 | A false peace; leaving off prayers | Cyprian, Letter to the people of Carthage 2 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32396-32397 | "leaving off prayers and supplications" |
| Timeline P2 | Five presbyters | Cyprian, Letter to the people of Carthage 3 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32403-32404 | "Those five presbyters" |
| Timeline P2 | Another persecution | Cyprian, Letter to the people of Carthage 3 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32402-32403 | "This is another persecution" |
| Timeline P2 | Nothing new until all meet; tempered with discipline and mercy | Cyprian, Letter to the people of Carthage 3 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32425-32429 | "tempered alike with discipline and with mercy" |
| Timeline P2 | Cornelius made bishop by sixteen bishops | Cyprian, Letter to Antonianus 24 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33981-33983 | "when a bishop has been made in the Church by sixteen" |
| Timeline P2 | Novatian elevated by like-minded bishops | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14069-14084 | "elevated to the episcopacy by such bishops as entertained similar sentiments" |
| Timeline P2 | Novatian's rule, to all the churches | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14084-14090 | "leave the pardoning of their offense to God" |
| Timeline P2 note | Socrates's distance and sympathy: rule reported from letters | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14084-14086 | "he wrote to all the churches" |
| Timeline P2 | Envoys from Novatian at Carthage | Cyprian, Letter to Cornelius (Ep. 40 ANF / 44 Hartel) 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32596-32597 | "we considered at once that they must be restrained from communion with us" |
| Timeline P2 | Bishops gathered with him | Cyprian, Letter to Cornelius 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 32599 | "I and several of my colleagues, who had come together to me" |
| Timeline P3 | A large number of bishops met | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33508-33510 | "a large number of bishops" |
| Timeline P3 | Scriptures on both sides; hope of peace not wholly denied | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33510-33516 | "neither should hope of communion and peace be wholly denied to the lapsed" |
| Timeline P3 | Certificate-holders admitted in the meantime; sacrificed helped at death | Cyprian, Letter to Antonianus 17 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33780-33783 | "that the receivers of certificates should in the meantime be admitted, that those who had sacrificed should be assisted at death" |
| Timeline P3 | Those who ask only in sickness refused | Cyprian, Letter to Antonianus 23 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33964-33968 | "if they begin to beg for them in the midst of sickness and peril" |
| Timeline P3 | The little book of decisions | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33522-33524 | "according to what is contained in a little book" |
| Timeline P3 note | The book is lost | Hefele, History of the Councils I (modern) | `cic/texts/hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt` | 6374-6378 | "but unfortunately — it is lost" |
| Timeline P3 | Felicissimus and the five cut off | Cyprian, Letter to Cornelius on Fortunatus 9 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34758-34770 | "was excommunicated by them here" |
| Timeline P3 | The five presbyters excommunicated by fellow-bishops | Cyprian, Letter to Cornelius on Fortunatus 9 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34758-34759 | "were lately excommunicated by the judgment of our fellow-bishops" |
| Timeline P3 | Carthage wrote to Cornelius lest the number seem unsatisfactory | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33524-33526 | "lest perchance the number of bishops in Africa should seem unsatisfactory" |
| Timeline P4 | Sixty bishops, many presbyters and deacons; other provinces | Eusebius VI.43.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38288-38291 | "number sixty, and a great many more presbyters and deacons" |
| Timeline P4 | Novatian and followers strangers | Eusebius VI.43.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38292-38294 | "his brother-hating and inhuman opinion" |
| Timeline P4 | Heal with the medicines of repentance | Eusebius VI.43.2 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38299 | "minister to them with the medicines of repentance" |
| Timeline P4 | Cornelius agreed with Carthage | Cyprian, Letter to Antonianus 6 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33526-33529 | "concurred in the same opinion as we had held" |
| Timeline P5 | Antonianus shaken by Novatian's letters | Cyprian, Letter to Antonianus 2 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33428 | "influenced by the letters of Novatian, had begun to waver" |
| Timeline P5 | Cyprian clears himself of turning from severity | Cyprian, Letter to Antonianus 3 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 33450-33457 | "turned my mind from discipline and from its former severity of judgment" |
| Timeline P5 | Dionysius: the dying who ask receive remission | Dionysius, in Eusebius VI.44 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38857 | "persons at the point of death" |
| Timeline P5 | Serapion, who had sacrificed | Dionysius, in Eusebius VI.44 | `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` | 38841-38848 | "a certain Serapion" |
| Timeline P5 | Fortunatus, one of the five, pseudo-bishop by a few | Cyprian, Letter to Cornelius on Fortunatus 9 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34752-34753 | "that pseudo-bishop, constituted by a few" |
| Timeline P5 | Fortunatus one of the five presbyters | Cyprian, Letter to Cornelius on Fortunatus 9 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34756-34757 | "who is one of the five presbyters" |
| Timeline P5 | Novatian's party made Maximus bishop | Cyprian, Letter to Cornelius on Fortunatus 9 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34776-34780 | "Novatian’s party is also said to have now made Maximus the presbyter" |
| Timeline P5 | New trouble drawing near | Synodal letter to Cornelius 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34287-34288 | "the day of another trouble is again beginning to draw near" |
| Timeline P5 | Peace to those who never left and kept repenting from the first day | Synodal letter to Cornelius 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34295-34297 | "have not ceased from the first day of their lapse to repent" |
| Timeline P5 | Armed for the battle | Synodal letter to Cornelius 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34298-34299 | "armed and equipped for the battle which is at hand" |
| Timeline P5 | Not to those who sleep (the letter's words) | Synodal letter to Cornelius 3 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34332-34333 | "we grant peace, not to those who sleep, but to those who watch" |
| Timeline P5 note | Hefele: May 252 | Hefele, History of the Councils I (modern) | `cic/texts/hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt` | 6504-6507 | "Ides of May 252" |
| Timeline P6 | Nicaea canon 8: Cathari who come over | Nicaea, canon 8 | `cic/texts/npnf214_seven-ecumenical-councils.xml` | 3769-3770 | "Concerning those who call themselves Cathari, if they come over" |
| Timeline P6 | Communicate with the lapsed who had penance laid on them | Nicaea, canon 8 | `cic/texts/npnf214_seven-ecumenical-councils.xml` | 3775-3777 | "with those who having lapsed in persecution have had a period [of penance] laid upon them" |
| Timeline P6 | Canon 13: ancient canonical law, last Viaticum | Nicaea, canon 13 | `cic/texts/npnf214_seven-ecumenical-councils.xml` | 4503-4506 | "the ancient canonical law is still to be maintained" |
| Timeline P6 | Strict discipline kept in Phrygia and Paphlagonia | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14059-14061 | "even to the present day, in the provinces of Phrygia and Paphlagonia" |
| Timeline P6 | Cruel and merciless to some, just to others | Socrates IV.28 | `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 14099-14101 | "this appeared to some a cruel and merciless course" |
| Uncertain (new) | The synodal letter gives no year | Synodal letter to Cornelius 1 | `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` | 34273-34275 | "We had indeed decided some time ago" |
`HEF` above is `cic/texts/hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt`, a modern historian, cited only for the lost book and the year 252, both shown as his.

## The menu sections (Stage-Two-Kit section 1), and what fills each

| Section | Filled from | Held? |
|---|---|---|
| On screen: short description | new `council.shortDescription` | yes |
| On screen: direct line | `council.traditions` (Cyprian of Carthage and The Roman Church in the Third Century gathered; Novatianism condemned) and `council.rivers` | yes; no census `edges` touch this entry |
| Below: the brief (Read along) and its old sources | `longDescription`; new `council.briefSources` | yes |
| Timeline | new `council.timeline` | yes |
| People and stories | entry `people` (Cyprian, Cornelius, Novatian, Dionysius). Documented stories held elsewhere on the same events: "The Confessors Come Back" (`novatianism`) and "Cyprian's Flight and the Letter from Rome" (`latin-pastoral-congregational-christianity`); none is told under the council | people yes; no story of its own |
| What happened | `council.issue`, `calledBy`, `attended`, `decided`, `howItWorked` (absent), `record` | yes |
| Connections | `council.traditions`; `people` | yes, as parts; no edge records |
| Legacy and today | `council.outcome` | yes; nothing on "today" (Source_Sheet I4: no held source says who keeps these rules today) |
| Open questions | `council.uncertain` (13 items with the new one) | yes |
| Sources | `council.sources.fromThoseThere`, `writtenLater` | yes |
| Modern works | none: no `modernWorks`. Hefele (English and Leclercq's French) sits in `council.sources.writtenLater` | nothing held; see Entry fields |

## Entry fields (for release to apply if the checker passes)

- `council.datesNote`: as above.
- `modernWorks`: none listed. The two Hefele items in `council.sources.writtenLater` ("A History of the Councils of the Church, vol. 1"; "Histoire des conciles, tome 1, part 1, section 5") are modern works under the role's rule and would move there word for word. Flagged, not moved.
- `council.issue` item 3 and `council.outcome` items 1 and 5 carry Hefele's views as content ("Hefele ... says the party took up the charge"; "The next year, by Hefele's dating"; "By Hefele's account"). Credited, but on shown fields. Flagged for the checker; not rewritten here.

## Not found

Nothing in the new fields lacks a held line.

## Four faults, re-read

1. Differences credited: Felicissimus's party in Cyprian's voice (note); Novatian's rule in Socrates's, with his distance and sympathy (note); the rival bishops as Cyprian's account; Cornelius's practice left to `uncertain` item 6. 2. No modern view as the record: Hefele's months leave the shown datesNote; his year for the letter stays a credited note; the Nicaea line says no held source ties canon 13 to 251. 3. Dates on the right event: 252 is never reckoned from the line before; Cornelius's election and Novatian's rival election sit before the Carthage council (outline Do-not-say). 4. Force kept: the run to the forum, the deathbed refusal, the cut-off of Felicissimus, "strangers", and the charge Cyprian answered are all on the timeline.
