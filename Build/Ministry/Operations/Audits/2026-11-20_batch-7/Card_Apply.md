# Batch 7: card apply report

Applied by the card-apply step, 2026-11-20. Each change is shown as field, old → new (the changed words only, where the field is long). Cards keep their key order and indentation. No commit; `tools/validate-census.mjs` not run; census and briefs untouched.

## tertullian-s-voice

Changes (13):
- `legacy.remembered[2]`: `and quotes Hilary that by his subsequent error he detracted from the authority of his approved writings.` → `quotes Hilary that by his subsequent error he detracted from the authority of his approved writings, and says he was a great trial in the Church.`
- `uncertain[5]`: `older. For this reason the card says foremost, not first.` → `older.`
- `uncertain[14]`: `alone.` → `alone, except two short lines the scan prints cleanly, the blood of Christians is seed and I am the heir of the apostles, which carry the Latin.`
- `briefReferences[1]`: `Carthage, and chief of the Latin writers after Victor and Apollonius.` → `Carthage. Vincent of Lérins, Commonitory 18: the first place among the Latins.`
- `quotationOriginals[0].uncertain`: `Latin, liceat veritati vel occulta via tacitarum litterarum ad aures vestras pervenire,` → `Latin`
- `quotationOriginals[5].original`: added `"Ego sum haeres apostolorum"`
- `quotationOriginals[5].originalFile`: added `"cic/texts/tertullian_quae-supersunt-t2-polemica-lat_oehler1853.txt"`
- `quotationOriginals[5].originalLines`: added `"2289"`
- `quotationOriginals[5].uncertain`: removed (was `"The Latin, Ego sum heres apostolorum, is held only in a damaged scan, so the English stands alone."`)
- `quotationOriginals[6].original`: added `"alium autem quomodo accipere debeas, iam professus sum, personae, non substantiae nomine, ad distinctionem, non ad diuisionem. ceterum, (etsi) ubique teneo unam substantiam in tribus cohaerentibus"`
- `quotationOriginals[6].originalFile`: added `"cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt"`
- `quotationOriginals[6].originalLines`: added `"12558-12561"`
- `quotationOriginals[6].uncertain`: `follows Kroymann. The card prints the English alone because Kroymann's scan misreads one word inside the span.` → `and the Latin given here follow Kroymann. Kroymann's scan misreads distinctionem, which Oehler's print confirms.`

Scan readings added to `tools/quote_scan_readings.json`:
- `tertullian_opera-pars3-lat_kroymann-csel47.txt` lines 12560: `distmccionem` → `distinctionem`
- `tertullian_opera-pars3-lat_kroymann-csel47.txt` lines 12560: `ubique  20` → `ubique`

Not applied: nothing.

## cyprian-of-carthage

Changes (8):
- `datesNote`: `the Edinburgh` → `A. Cleveland Coxe, the American`
- `keyWorks[1].about`: `the Edinburgh editor's` → `Coxe's`
- `legacy.traces[2]`: `In 533` → `Telling of the year 533,`
- `legacy.remembered[0]`: `the Edinburgh editor` → `Coxe, the American editor,`
- `uncertain[7]`: `the Edinburgh editor` → `Coxe, the American editor,`
- `uncertain[13]`: `he had been Cyprian's secretary as a young man.` → `that as a very young man he had met Cyprian's aged secretary at Rome. Jerome's Latin says so; the English translation wrongly makes Paul himself the secretary.`
- `sources.about`: appended `{"title": "Lives of Illustrious Men, ch. 53, on Tertullian (Migne, Patrologia Latina 23)", "author": "Jerome", "date": null, "language": "Latin", "file": "cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt"}`
- `briefReferences[5]`: `sun, the tree and the spring.` → `one mother from whose womb Christians are born and by whose milk they are fed.`

Scan readings added: none.

Not applied: nothing.

## pontius-the-deacon

Changes (7):
- `briefReferences[0]`: `him, though his living words are silent;` → `him;`
- `briefReferences[1]`: `notable volume` → `volume`
- `briefReferences[2]`: `23 manuscripts;` → `manuscripts;`
- `briefReferences[5]`: `30 August 257,` → `257,`
- `briefReferences[7]`: `year and the delay as church business;` → `year;`
- `briefReferences[9]`: `praise modeled on the Passion of Perpetua.` → `praise.`
- `briefReferences[11]`: `Richardson gives about 260 and Coxe says a martyr, each without a source; no` → `no`

Scan readings added to `tools/quote_scan_readings.json`:
- `harnack_vita-cypriani-commentary-lat-deu_1913.txt` lines 1311: `volebatintellegi` → `volebat intellegi`
- `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` lines 40269: `documentum in lo` → `documentum in`
- `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` lines 41409: `exulto, plus 5` → `exulto, plus`

Not applied: nothing.

## novatian

Changes (13):
- `uncertain[13]`: `three` → `four`
- `uncertain[15]`: `says the same, and that` → `reports the same, says it is not known for certain when he died, and says`
- `sources.about`: appended `{"title": "Church History, Book 1, chapter 10 (Greek, with Valesius's Latin, ed. Robert Hussey)", "author": "Socrates of Constantinople", "date": null, "language": "Greek", "file": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt"}`
- `briefReferences[1]`: `bishop since Fabian's death,` → `bishop,`
- `briefReferences[2]`: `by the tenth hour (EUS` → `(EUS`
- `briefReferences[7]`: `Socrates says no other writer recorded it (SOC 3722-3727). Book 1, chapter 13: Auxanon, a very aged Novatian presbyter` → `Book 1, chapter 13: Auxanon, a very aged man`
- `briefReferences[11]`: `under Valerian (SOC` → `(SOC`
- `briefReferences[12]`: `writings, and On the Trinity as a sort of epitome of Tertullian's work (JER 40886-40897). Harnack on the book's date and its survival under Tertullian's name` → `writings (JER 40886-40897). Harnack on the book's date`
- `quotationOriginals[1].uncertain`: `willing (ἄκων, ἑκών), whose sense Rufinus's Latin and both English prints confirm. "One ought" follows ἔδει. Salmond's English (Ante-Nicene Fathers, vol. 6) reads "If you were carried on against your will, as you say, you will show that such has been the case by your voluntary retirement", and "it would have been but dutiful to have suffered any kind of ill, so as to avoid rending the Church of God". The Greek addresses Novatus;` → `willing, whose sense Rufinus's Latin and both English prints confirm. "One ought" follows ἔδει. Salmond's English (Ante-Nicene Fathers, vol. 6) reads "If you were carried on against your will, as you say, you will show that such has been the case by your voluntary retirement", and "it would have been but dutiful to have suffered any kind of ill, so as to avoid rending the Church of God". Both English prints address Novatus. Schwartz's Greek addresses Novatian (Νοουατιανῷ), and his notes give forms of Novatus from other manuscripts;`
- `quotationOriginals[3].original`: added `"θὲς ὦ ᾿Ακέσιε κλίμακα, καὶ μόνος ἀνάβηθι εἰς τὸν οὐρανόν."`
- `quotationOriginals[3].originalFile`: added `"cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt"`
- `quotationOriginals[3].originalLines`: added `"9912-9913"`
- `quotationOriginals[3].uncertain`: `Greek (θὲς ὦ Ἀκέσιε κλίμακα, καὶ μόνος ἀνάβηθι εἰς τὸν οὐρανόν), which the one held print gives in a scan too damaged to print here.` → `Greek.`

Scan readings added to `tools/quote_scan_readings.json`:
- `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt` lines 9912: `᾿Ακέσιεΐ` → `᾿Ακέσιε`
- `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt` lines 9912: `εἰς τὸν ao` → `εἰς τὸν`
- `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt` lines 9913: `φοὐρανόν` → `οὐρανόν`

Not applied: nothing.

## councils-of-rome-and-carthage-251

Changes (6):
- `sources.writtenLater`: appended `{"title": "Church History, Book IV, chapter 28 (Greek, with Valesius's Latin, ed. Robert Hussey)", "author": "Socrates of Constantinople", "language": "Greek", "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt"}`
- `briefReferences[2]`: `granted to all whose conduct since their fall satisfied him.` → `granted.`
- `quotationOriginals[5].original`: added `"μὴ δέχεσθαι τοὺς ἐπιτεθυκότας εἰς τὰ μυστήρια ἀλλὰ προτρέπειν μὲν αὐτοὺς εἰς μετάνοιαν, τὴν δὲ συγχώρησιν ἐπιτρέπειν Θεῷ, τῷ δυναμένῳ καὶ ἐξουσίαν ἔχοντι συγχωρεῖν ἁμαρτήματα."`
- `quotationOriginals[5].originalFile`: added `"cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt"`
- `quotationOriginals[5].originalLines`: added `"4372-4377"`
- `quotationOriginals[5].uncertain`: `plural. The Greek is held only in a damaged scan, so it is not printed here.` → `plural.`

Scan readings added to `tools/quote_scan_readings.json`:
- `socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt` lines 4372: `μὴ δέχεσθαι 35` → `μὴ δέχεσθαι`
- `socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt` lines 4375: `, - ^ ER A5 , L4` → (dropped)
- `socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt` lines 4376: `kai ἐξουσίαν ἔχοντι avy-` → `καὶ ἐξουσίαν ἔχοντι συγ-`
- `socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt` lines 4377: `εχωρεῖν ἁμαρτήματα` → `χωρεῖν ἁμαρτήματα`

Not applied: nothing.

## pamphilus-of-caesarea

Changes (15):
- `datesNote`: `catalogue` → `catalog`
- `keyWorks[1].about`: `catalogue` → `catalog`
- `legacy.traces[0]`: `catalogue` → `catalog`
- `legacy.remembered[0]`: `read by hand from` → `that stands in`
- `uncertain[4]`: `introduction` → `note on Church History VII.32`
- `uncertain[6]`: `family that held` → `family, and was himself distinguished in`
- `uncertain[7]`: `beheading,` → `a capital sentence,`
- `uncertain[9]`: `the volumes seem to him to be marked with the traces of his own blood, and the English of the Library's Jerome volume follows it.` → `Pamphilus seems to him to have marked them with the traces of his own blood; the English of the Library's Jerome volume has lines that seem traced in his blood.`
- `briefReferences[1]`: `Palestine, today in Israel.` → `Palestine.`
- `briefReferences[3]`: `catalogue of the library in` → `library, and`
- `briefReferences[8]`: `doctrine. Addressed to confessors condemned to the mines of Palestine.` → `doctrine.`
- `briefReferences[9]`: `The longer form in Greek and Photius: by the sword.` → `Photius: by the sword; the longer form in Greek: a capital sentence.`
- `briefReferences[11]`: `introduction:` → `note on Church History VII.32:`
- `quotationOriginals[0].uncertain`: `the volumes seem to him to be marked` → `Pamphilus seems to him to have marked them`
- `quotationOriginals[2].uncertain`: `and read by hand; the neighboring lines of the scan` → `in the scan; the neighboring lines`

Scan readings added: none.

Not applied: nothing.

## eusebius-of-caesarea

Changes (11):
- `uncertain[8]`: `a knee,` → `been hamstrung,`
- `briefReferences[0]`: `earlier writers' fragments, the passages` → `passages`
- `briefReferences[3]`: `the most illustrious of the martyrs of the time.` → `cast into prison, and his martyrdom.`
- `briefReferences[4]`: `persecution, between about 311 and 318; the History finished about 324, most of it` → `persecution; most of the History written`
- `briefReferences[5]`: `in Palestine at the senior emperor's right hand; the vision told under oath;` → `as a young man; what the emperor told him himself;`
- `briefReferences[6]`: `read before the emperor,` → `read,`
- `briefReferences[7]`: `signed and sent his people the creed. Athanasius, Defence of the Nicene Definition 3: he had denied the day before, then signed and excused himself to his church.` → `signed. Athanasius, Defence of the Nicene Definition 3: he had denied the day before, then signed.`
- `briefReferences[9]`: `by the confessors of` → `of`
- `briefReferences[10]`: `Paphnutius and Maximus of Jerusalem at Tyre, with no word of Eusebius. Rufinus, prologue: the Church History put into Latin, and Books X and XI added.` → `a like scene at Tyre, with no word of Eusebius. Rufinus, prologue: the Church History put into Latin.`
- `briefReferences[12]`: `Trajan with Trajan's reply,` → `Trajan,`
- `quotationOriginals[4].original`: `ὁμοούσιος` → `ὁμοούσιος`

Scan readings added: none.

Not applied: nothing. The check names `uncertain[9]` for the eye-and-knee fix; the text stands at `uncertain[8]` (unique match), so the fix was applied there.

## dionysius-of-alexandria

Changes (12):
- `briefReferences[0]`: `Alexandria after Heraclas;` → `Alexandria;`
- `briefReferences[2]`: `250, are lost;` → `250;`
- `briefReferences[5]`: `his hearing before Aemilianus under Valerian and the sending to Cephro in Libya.` → `the second persecution, under Valerian.`
- `briefReferences[6]`: `some before him had rejected the Revelation; he would not reject it; the thought, words and Greek of the Revelation` → `he would not reject the Revelation; its Greek`
- `briefReferences[8]`: `bishop; McGiffert's note puts the death in the eleventh year in both versions of the Chronicle. Chronicle, in Jerome's Latin: Maximus ordained to the Alexandrian church in the eleventh year.` → `bishop.`
- `briefReferences[14]`: `books, and the claim of insertion.` → `books.`
- `quotationOriginals[1].printed`: `Therefore that he was called John, and that this book is the work of one John, I do not deny. And I agree also that it is the work of a holy and inspired man. But I cannot readily admit that he` → `That this person was called John, therefore, and that this was the writing of a John, I do not deny. And I admit further, that it was also the work of some holy and inspired man. But I could not so easily admit that this`
- `quotationOriginals[1].work`: `Eusebius, Church History VII.25.7, quoting Dionysius, On Promises, tr. McGiffert` → `Dionysius, On Promises, Book 2, in Eusebius, Church History VII.25.7, tr. S. D. F. Salmond`
- `quotationOriginals[1].file`: `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` → `cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`
- `quotationOriginals[1].lines`: `41453-41457` → `8119-8124`
- `quotationOriginals[1].uncertain`: `Salmond's English (Extant Fragments and Letters, lines 8119-8125) reads "the writing of a John, I do not deny" and "the work of some holy and inspired man"; McGiffert has "the work of one John". The modern "the writing of a John" follows Salmond and the Greek, which has no word for "one".` → `McGiffert's English (Church History VII.25.7, lines 41453-41457) reads "the work of one John" and "I agree also that it is the work of a holy and inspired man". The modern "the writing of a John" follows Salmond and the Greek, which has no word for "one"; "I agree" follows McGiffert and the Greek.`
- `quotationOriginals[2].uncertain`: `there that neither print renders;` → `there; McGiffert leaves it out, and Salmond gives it as "this very form";`

Scan readings added: none.

Not applied: nothing.

## peter-of-alexandria

Changes (7):
- `uncertain[0]`: `and Theodoret say the same.` → `says the same; Theodoret says only that Peter convicted him of certain crimes and deposed him.`
- `sources.about[4].title`: `6 and 9` → `6, 9 and 15`
- `briefReferences[0]`: `Hawkins: the fourth passover of the persecution, those tortured until they gave way, the marks of Jesus, and the forty more days. The opening words are in Hawkins's English, with the Greek of the 1886 Pedalion beside it.` → `Hawkins, and its Greek in the 1886 Pedalion: the fourth passover of the persecution, those tortured until they gave way, the marks of Jesus, and the forty more days.`
- `briefReferences[1]`: `Alexandria after Theonas,` → `Alexandria,`
- `briefReferences[3]`: `lapsed ask the martyrs for mercy; the two` → `two`
- `briefReferences[10]`: `Maximinus and Peter among its first victims.` → `Maximinus, and reaching Peter.`
- `briefReferences[12]`: `canons, with the notes of Zonaras and Balsamon.` → `canons.`

Scan readings added to `tools/quote_scan_readings.json`:
- `nikodemos-hagiorite_pedalion-canons-grc_1886.txt` lines 49723: `σίγματα` → `στίγματα`
- `epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt` lines 43852: `0` → `ὁ`

Not applied: nothing.

## anatolius-of-alexandria-and-laodicea

Changes (7):
- `legacy.remembered[3]`: `Eusebius` → `Eusebius, bishop of Laodicea,`
- `uncertain[9]`: `Anatolius left for Syria` → `the journey to Syria, at least the deacon Eusebius's, most likely came`
- `briefReferences[0]`: `an Alexandrian by birth, first among the ablest men of his time in learning; the report that the citizens asked him to found a school of Aristotle's philosophy.` → `first among the ablest men of his time in learning.`
- `briefReferences[1]`: `Eusebius, outside the lines,` → `outside the lines`
- `briefReferences[3]`: `Theotecnus of Caesarea in Palestine making him a bishop to succeed him; the synod at Antioch calling him; the believers at Laodicea keeping him after the deacon Eusebius,` → `the bishop of Caesarea in Palestine making him a bishop to succeed him; the synod at Antioch calling him; the believers at Laodicea keeping him after the deacon,`
- `briefReferences[5]`: `new moon that begins the nineteen-year` → `nineteen-year`
- `briefReferences[7]`: `the last bishop of Laodicea before the persecution was Stephen.` → `another man bishop of Laodicea before the persecution.`

Scan readings added: none.

Not applied: nothing. No reading added for the side-note, per the ruling.

## lactantius

Changes (7):
- `legacy.remembered[3]`: `Christ would reign a thousand years on earth after the resurrection.` → `after the resurrection the Lord would reign in the flesh with the saints.`
- `briefReferences[0]`: `and Galerius disputing whether to burn it; Diocletian fearing` → `fearing`
- `briefReferences[1]`: `a disciple of Arnobius, summoned` → `summoned`
- `briefReferences[2]`: `execution with their families,` → `execution, people`
- `briefReferences[4]`: `years followed by a thousand-year reign.` → `years.`
- `quotationOriginals[0].uncertain`: `suspects a word` → `reports that earlier editors thought a word was`
- `quotationOriginals[2].uncertain`: `44985-44987` → `44984-44986`

Scan readings added: none.

Not applied: nothing. No reading added for Fotheringham, per the ruling.

## origen

Changes (7):
- `uncertain[0]`: `preface: "we have either left them out as passages which had been falsified or inserted, or else have changed the expression in accordance with the rule of faith."` → `preface that where he found erroneous definitions of the Trinity, "we have either left them out as passages which had been falsified or inserted, or else have changed the expression in accordance with the rule of faith which the writer again and again lays down."`
- `briefReferences[0]`: `"tenth year"` → `tenth year`
- `briefReferences[1]`: `father: "Take heed not to change your mind on our account."` → `father not to change his mind on their account.`
- `briefReferences[10]`: `"the labour-loving Origen"` → `Origen`
- `briefReferences[13]`: `bodies. Rufinus's Latin is the only form in which we read it, and Rufinus says he changed passages.` → `bodies.`
- `briefReferences[14]`: `On the Resurrection against` → `against`
- `briefReferences[15]`: `"the Defense which we have composed in his behalf".` → `the Defense he composed for Origen, with Pamphilus in McGiffert's note.`

Scan readings added: none.

Not applied: nothing.

## methodius-of-olympus

Changes (3):
- `uncertain[1]`: `Eusebius of Caesarea, as Jerome quotes him, asks how Methodius dared to write against Origen now. Jerome reads this as the same charge, but Eusebius's words do not themselves say that Methodius praised Origen. He names the dialogue in which Methodius of Olympus praised him: Xenon.` → `He names the dialogue in which Methodius of Olympus praised him: Xenon. Eusebius of Caesarea, as Jerome quotes him, asks how Methodius dared to write against Origen now. Jerome reads this as the same charge, but Eusebius's words do not themselves say that Methodius praised Origen.`
- `briefReferences[3]`: entry removed (was `Jerome, Lives of Illustrious Men 54, tr. Richardson: Origen's death under Gallus at sixty-nine, some fifty years before.`)
- `briefReferences[10]`: entry removed (was `Theodoret, Eranistes, editor's note: bishop first of Olympus and then of Patara at the beginning of the fourth century.`)

Scan readings added: none.

Not applied: nothing.
