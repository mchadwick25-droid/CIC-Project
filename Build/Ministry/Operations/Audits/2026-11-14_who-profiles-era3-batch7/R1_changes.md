# R1 changes: eight Who profiles, era 3 batch 7

Every finding of `R1_review.md` was applied, as worded by its reviewer unless noted. Brief changes were made by the drafter and re-scored with `engine.m1.gates.grade_text`; the audio scripts were rebuilt from the briefs. Card, `records.json` and README changes are listed per finding below. Every quotation added or changed was checked against its file, and every cited line read.

## Briefs after round 1

| Profile | Words | Length at 162 wpm | FK | Flesch |
|---|---|---|---|---|
| Boethius (major) | 401 | 2:29 | 8.1 | 60.5 |
| Philoxenus of Mabbug (major) | 402 | 2:29 | 7.2 | 68.6 |
| Fulgentius of Ruspe (major) | 404 | 2:30 | 7.4 | 68.6 |
| Avitus of Vienne | 325 | 2:00 | 6.6 | 68.6 |
| Eugippius | 324 | 2:00 | 6.9 | 69.0 |
| John of Beth Aphthonia | 321 | 1:59 | 6.0 | 72.7 |
| Ciaran of Clonmacnois | 323 | 2:00 | 6.5 | 73.5 |
| Primasius of Hadrumetum | 321 | 1:59 | 8.4 | 60.7 |

## Brief changes

- A-B1, Boethius: "The Bollandists, in their Acta Sanctorum of saints' days, list him as a martyr at Pavia." replaces the Roman Martyrology sentence.
- A-M1, Boethius: "in the year Mommsen dates to 524".
- A-M2, Boethius: the senator and letter paragraphs joined; "Ptolemy the astronomer".
- A-B2, Philoxenus: "Michael the Syrian says a Syriac version of the New Testament was made at Mabbug through his care."
- A-M7, Philoxenus: the chronicle under Zachariah's name is marked "from his own side".
- A-M8, Philoxenus: the border clause cut from the birth sentence.
- A-M10, John: "a worker in lead" for "a plumber".
- A-M11, John: "J.-B. Chabot and Rubens Duval write of the Life as John bar Aphthonia's, and E. W. Brooks names him its author."
- A-M12, John: "Zachariah Rhetor wrote another Life of Severus."
- A-M13, John: Jacob of Edessa "became a monk at the monastery of Aphthonia and studied the Psalms there in Greek."
- B-M1, Fulgentius: "Augustine of Hippo"; "Theodoric, the Ostrogothic king"; "in Africa" cut for length.
- B-M2, Fulgentius: "by a Catholic monk who lived with him, tells this from what Fulgentius told him."
- B-M4, B-M5, B-M6, B-M7, B-M8, Primasius: "The rest is told only by Victor"; "agreed to condemn the Three Chapters so that he might take his place"; "wherever truth shines, it should be won back for the Catholic Church"; "Augustine of Hippo"; the Mommsen year in its own sentence.
- B-M14, B-M15, B-M16, Avitus: the death paragraph opens on the Life ("His Life says he died under the emperor Anastasius, and gives no year"); "Once Gundobad was lost in his unbelief, Agobard says"; "Peiper tentatively dates".
- C-M1 to C-M4, Eugippius: "forced the Romans out of Noricum's Danube towns", with the opening split; Paschasius's answer that teachers are best portrayed by their pupils; "the Roman deacon Paschasius"; "Augustine of Hippo"; the brief's absence sentence dropped (the card keeps it).
- C-B1, C-M9, C-M10, Ciaran: "The Life then takes him to Enda of Aran. Before Clonmacnois he led a house on the island of Inis Angin for three years."; "It is a saint's Life"; the Stokes sentence split; "and the brethren running out to meet him" cut for length.

## Card, records and README changes


Briefs and audio were not touched. All JSON was reloaded with json.load after every write; key order and formatting (indent 2, UTF-8, trailing newline) are kept. Quotes added were checked with vq.py, or by eye where a hyphen break with a trailing space defeats it (noted).

## Part A
- A-B1: Card `legacy.remembered` 3 and `uncertain` "His faith" now carry the reviewer's text. Records: the Acta Sanctorum claim is rewritten to the Bollandists' own 27 May list (l.8030, 8150-8155). A new claim gives the Ferrarius catalog "eorum qui non sunt in Martyrologio Romano" (l.16492-16497; the reviewer's l.16489-16493 is off by three, as read). It is marked as reconstructed from heavy OCR and kept Inferential-Thin. I also fixed the contested claim (martyr) and the absent-detail note. Spelling change: the reviewer's "catalogue" is "catalog" on the card and in my records text (American spelling).
- A-M1: Brief only, applied by the drafter. Records: the Marius claim now says the margin 'a. 524' is Mommsen's, which supports "in the year Mommsen dates to 524".
- A-M2: Brief only, applied by the drafter. Records claim (Var. i.45, "Ptolemy the astronomer") already supports it. No card change.
- A-M3: Card `uncertain` 1, last sentence, replaced with the reviewer's first option. Records: the Bollandist doubt claim is rewritten with the answer "Sed hoc non legitur apud Procopium…" (l.16339-16343, reconstructed from heavy OCR), and contested claim 0 is updated to match.
- A-M4: Card `legacy.traces` 3 replaced with the reviewer's text.
- A-M5: No change. The review marks it for the coordinator (tradition).
- A-M6: Card `uncertain` "His family" now reads "the Paraenesis of Ennodius, bishop of Pavia" (Hodgkin's index, l.23579).
- A-B2: Card `keyWorks` 2 now reads "after the earlier version made at Mabbug through Philoxenus's care". Records: the Michael and Bar Hebraeus claim now notes that "first" means the earlier version Thomas revised (Budge on the Peshitta, l.2806-2819). It also notes that this supports the brief's "a Syriac version".
- A-M7: Brief only, applied by the drafter. Records: the chronicle claim on the march (l.8895-8901) is now marked "Friendly witness, from his own side, as the brief and card mark it".
- A-M8: Brief only, applied by the drafter. No card change; the records claim already cites l.399-403 and 415-416.
- A-M9: Philoxenus card `uncertain` 3 now reads "which Budge quotes from J. S. Assemani's Bibliotheca Orientalis". John card `uncertain` 1 now reads "J. S. Assemani, in his Bibliotheca Orientalis, names two Johns".
- A-B3: John card `dates` 2nd sentence and `uncertain` 3 now carry the reviewer's text (849 of the Greeks, Brooks's 538, Elias "the next year of that count"). Records: a new claim states the count. The extract's own "En l'an 823" for Sidon (l.19739) matches Hamilton-Brooks's "823rd year of the Greeks", note 512 (l.8851-8855, 8888). Elias's "Annus 849 … die 8° sabat" (l.5368-5373) and Brooks's "On Feb. 8, 538 Severus died in Egypt" (Select Letters I l.240-241) are cited with it. Contested claim 1 now states the count and Brooks's year.
- A-B4: John card `legacy.traces` 1 replaced with the reviewer's text. Records: the Crum claim is rewritten. It now separates Crum's heading (l.19898-19900), the sherd's own opening "From: the Life of the ….- Apa Severus" (l.19903) and the Rylands 99 and Munich note (l.19912-19914).
- A-M10: Brief only, applied by the drafter. Records claim 1 now glosses "worker in lead" and cites Kugener's note 2, μολυβδουργός (OCR 'morußdoupyös', l.13196).
- A-M11: Brief only, applied by the drafter. The card `uncertain` 1 already had it right, so no card change. Records: the Chabot and Duval claims, and the contested claim's "same man" side, now say their "probablement" concerns the fragment's source. Both write of the Life as bar Aphthonia's (l.14078-14079; l.33829-33830). I added Nau's held note giving the full name "Rubens Duval" (PO 13 l.10524). The README was changed to match.
- A-M12: Brief only, applied by the drafter. Records: a new claim says Zachariah Rhetor wrote another Life (Hamilton-Brooks l.362-365; Kugener's heading l.76, 140). The "two Lives in the volume" claim now notes the Ethiopic Life by Athanasius (PO 4 l.663-665, 32888-32889).
- A-M13: Brief only, applied by the drafter. Records: the Jacob claim now says he "took the habit" and studied there (l.36363-36366; OCR hyphen breaks checked by eye), and points to the contested claim on the house.
- A-M14: John card `legacy.traces` 3 now opens "John bar Aphthonia's house at Kenneshre…".
- A-M15: John card `otherNames` 2 ("Jean, supérieur…") dropped.
- John "Near death": records claim 8 now cites "Il prévit dès lors que la fin de sa vie était proche" (l.16604).

## Part B
- B-M1: Fulgentius card `knownFor` now reads "Augustine of Hippo". The brief was applied by the drafter. Records: the Psalm 36 claim cites Fulgentius's own "Augustinum Hipponensem" (De veritate praedestinationis II, l.42467). The Rome claim cites Dalton's "Theodoric the Great, king of the Ostrogoths" (l.23889-23890).
- B-M2: Brief only, applied by the drafter. Records: the Life-author claim now ties the brief's "a Catholic monk … from what Fulgentius told him" to "omnia quae memoriter…" (l.8003-8004) and "sicut ipse nobis postea referebat" (l.8501).
- B-M3: Fulgentius card `legacy.traces` 0 replaced with the reviewer's text. Records: the Facundus claim and the absent-details note on the lost books now say that Facundus names no books.
- B-B1: Primasius card `uncertain` 1 replaced with the reviewer's text. Records: the Kihn claim is rewritten as worded (l.12673-12675, 12690), and the contested claim now reads "Kihn names no monastery (l.12675, l.12690)".
- B-M4: Brief only, applied by the drafter. No card change; the card already gives both placings.
- B-M5: Brief only, applied by the drafter. Records: the Victor claim glosses "memoratae damnationi protinus assensit" as the brief's "agreed to condemn the Three Chapters".
- B-M6: Brief only, applied by the drafter. Records: the gem claim now carries on to "Huic enim soli competit … cum verae matri fuerit redditum" (l.62681-62685), which supports "won back for the Catholic Church".
- B-M7: Primasius card `knownFor` now reads "Augustine of Hippo". Records: the prologue claim notes the placing.
- B-M8: Brief only, applied by the drafter. The records claim on Mommsen's 551 already supports it.
- B-M9: Primasius `keyWorks` 1 `about` replaced with the reviewer's text. Records: the "lost" claim is rewritten as the Cave notice's view, with the Reichenau manuscript and the notice's doubt (l.34982-34986, 35021-35031). It is now Contested.
- B-M10: Primasius card `dates` replaced with the reviewer's text.
- B-M11: Primasius `knownFor` now reads "a commentary on the Apocalypse of John".
- B-M12: Deleted "The two are different men." and "It is a guess." from the card.
- B-M13: Records: the claims on the sixteen signers and 5 May, and on the Three Chapters, now cite Kihn as witness (l.12603-12604, 12652-12657; l.12648-12652). The council profile is kept as a cross-reference.
- B-M14: Brief only, applied by the drafter. The card keeps the wider absence, and records claim 31 supports the new brief line.
- B-M15: Brief only, applied by the drafter. Records: the Agobard claim now renders "in sua perfidia perdito" as "once Gundobad was lost in his unbelief".
- B-M16: Brief only, applied by the drafter. Records: the conversion-letter claim now says "with a query" and that the query is why the brief says "tentatively". I corrected the table line to l.43290 (the file reads "513 — 510?"; it was cited as l.43288).
- B-M17: Avitus card `dates` and `uncertain` 0 (Zeno) carry the reviewer's text. Records: the Life claim notes "Tempore Zenonis".

## Part C
- C-M1: Brief only, applied by the drafter. Records: the grave claim now adds Onoulf's "all the Romans" (l.3927-3928, hyphen break checked by eye), the Danube towns (l.3976-3977) and Robinson's note on Jung (l.3979-3986).
- C-M2: Card `uncertain` 1 now has the Paschasius sentence. Records: a new Documented claim covers l.4255-4260, and Paschasius is added to the "For" side of the contested claim.
- C-M3: Card `dates` now reads "the Roman deacon Paschasius". The brief was applied by the drafter. Records: Robinson's index (l.5838) is now cited.
- C-M4: Card `keyWorks` 2 now reads "Augustine of Hippo". I also changed `knownFor`, which is the card's first mention of Augustine. Records: the Cassiodorus claim cites Sigebert's "Augustini episcopi Hipponensis" (PL 67 l.68093-68094).
- C-M5: Card `uncertain` 1 now carries the reviewer's text. Records claim 15 now quotes the full sentence with "than those I have related" and what he related (l.446-448). I corrected its line to l.477-479 (it was cited as 474-476), here and in the contested claim.
- C-M6: Card `uncertain` 2 now carries the reviewer's text.
- C-M7: Card `uncertain` 3 now carries the reviewer's text (Miraeus, Bollandus and Cave; Sigebert of Gembloux). Records: the Gallandi claim notes that he does not name Fabricius, and cites "Sigeb. Gembl." (l.67956).
- C-M8: Card `legacy.remembered` 3 now carries the reviewer's text.
- C-B1: Brief applied by the drafter. Card `uncertain` 6 (teachers) now carries the reviewer's text. Records: the "sends him on" claim adds Isel, the Inis Angin abbacy (l.22640-22650) and "no one after Findian his teacher". The Findian claim adds "his tutor" (l.22512). The contested claim's Lismore side now has the reviewer's wording, and a Bollandist "suo magistro / sui Abbatis Endei" side is added (l.76789, 76803).
- C-B2: Card `uncertain` 1 now carries the reviewer's text. Records: a new Documented claim covers the Lismore baptism by Justus (l.22098-22100, 22145). It matches Tirechan, whose line is l.3476-3477 as read (the review cites 3477-3479).
- C-M9: Brief only, applied by the drafter. Records: the hagiography claim now notes "a saint's Life".
- C-M10: Brief only, applied by the drafter. No card change.
- C-M11: Card `knownFor` now carries the reviewer's text.
- C-M12: Card `legacy.remembered` 1 now reads "Columba, Colum Cille in Irish".
- C-M13: Card `uncertain` 4 now carries the reviewer's text. Records: the Gilla Coemain claim adds the dating note (Tripartite l.15790-15797).
- C-M14: Card `uncertain` 3 now reads "in their commentary on the Life of Enda", and `uncertain` 7 now reads "The index to Stokes's Tripartite Life".
- C-M15: Records: the footnote claim is now pinned to "this city" (l.22755-22756), and the footnote itself is l.22789.
- C-M16: The README Avitus wording is as the reviewer gave it. I also added the death window to the Avitus card: `dates` and `uncertain` 0 now give Peiper's index (before 533 because Julian signs at Orléans; after late 525 or early 526 by Binding's homily date; Peiper's preface puts the Geneva pieces at 513 to 516). I split those sentences to stay under about 25 words. Records: a new claim covers Peiper's index l.30143-30149 and the prooemium l.3377-3378 and 3380-3381. The `absent_details` note now names those lines, and the Peiper window is added to the contested claim on the emperor.
- C-M17: The README John and Boethius owners are as the reviewer gave them. I also made the README's Chabot/Duval sentence match the brief ("write of the Life as his"). To match A-M12, "the second Life" now reads "the later of the two Lives … that M.-A. Kugener edits".

## Not changed

- A-M5, Boethius's card tradition, "The Byzantine Imperial Church (Justinianic)", for a man who died in 524, before Justinian's reign. It is a census movement name and the scan's first placing; it goes to the coordinator with the placing (Open-Gaps entry for this batch).
