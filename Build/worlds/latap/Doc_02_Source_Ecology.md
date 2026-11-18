# Doc_02 — Source Ecology: The Latin Apologists

**Status:** Approved to proceed (Doc_02 only; self-disposed by the build thread after two review rounds; not Frozen). Latest review: `Review-Artifacts/Doc02_Round2_Review.md`, Clear.
**Companion document:** `Source_Registry.md` (the per-source ledger; "row N" below means a Registry row). Gaps and requests are in `Open_Gaps_Tracking.md`, and this document cites an entry there by its subject.
**Governed by:** Construction Framework V7.4 Part II and Step 2; Constitution V2.3 Article 17 (five-level confidence vocabulary), Article 20 (Ordinary Believer, Source Asymmetry and Marginalized-Voices), Article 26 (Author Gravity and Contested-Tradition Governance); `Source_Registry_Template.md` V1.0; Forces Framework Step 2.
**Forces Framework integration:** Step 2. The forces lens is applied in §6.
**Grounded in:** `Doc_01_World_Identification_Boundaries_Orientation.md`, which is approved to proceed (c. 197–320; Carthage, Rome and Ostia, Sicca, Nicomedia and Trier; strand-singular as a recommendation still waiting on the project lead). This document does not reopen Doc_01. It answers Step 0 §4 items 1, 2, 3, 5, 8 and 9, which bind it, and it carries Doc_01 §9 items 5 to 12.

---

## 1. Primary Sources

Forty-six Registry rows (1–46) hold the works that the corpus map assigns to this world. The map carries them on 116 rows in `cic/corpus-map/latin-apologists.yaml`, because most works have more than one witness: an English translation, a Latin edition, sometimes two. Ninety-seven of those rows have the role `tradition`, three have `transmission`, and sixteen have `context`; the context rows are the scholarship and the ancient testimony. Eighty-six of the tradition rows are `assigned` and eleven are `provisional`. The other 28 Registry rows (47–74) hold scholarship, ancient testimony about the five authors, editors' notices, Excluded comparanda, and leads not yet vendored. The ancient testimony (rows 54 to 61) and the Excluded and lead rows (63 to 72) are typed primary because they are ancient writing, and none of them is a voice of the world.

**How the words were counted.** Step 0 §3 B1 counted the ANF English text of 40 works at 1,203,783 words. This build reproduced that figure exactly with the method Step 0 writes out: take each work's own `<div2>` block, replace every tag with a space, split on whitespace. A second pass used a parser and gave 1,203,489. A third pass removed every `<note>` element first and then counted again: 1,047,034 words. The three figures differ by the editorial footnotes and by tokenising. The counts below use the first and say so when they use the third. Words are the pieces that Python's `str.split()` returns, with no locale setting involved.

**Tertullian (rows 1–32).** Thirty-two works, 731,618 words on the Step 0 method, about 61 percent of the 40 counted works. With the footnotes removed the figure is 638,816 of 1,047,034, also about 61 percent. Thirty-one of the 32 have a Latin witness on the shelf. The Latin comes from three editions: Oehler (1853), which holds 21 of the works in two volumes and is the only public-domain Latin for 15 of them (Step 0 §3 B1); Reifferscheid and Wissowa, CSEL 20 (1890), ten works; and Kroymann, CSEL 47 (1906), six works. The *Appendix* of poems (row 32, 32,001 words) is the one work with no Latin. Its authorship is not attested (§2). *Against Marcion* alone is 187,134 words, and the heresy treatises together are 278,083 (Doc_01 §3).

**Minucius Felix (row 33).** One work, the *Octavius*: 23,819 words in the ANF English (22,305 with footnotes removed). Latin in three editions: Halm's TEI of CSEL 2 (1867), the preferred base for quoting; Boenig (Teubner 1903, with preface and apparatus); and Waltzing (Teubner 1912).

**Cyprian (rows 34–37).** Two works only, *To Demetrianus* and *On the Vanity of Idols*, English in ANF05 and Latin in Hartel's CSEL 3 and in two TEI files. By the Step 0 method the *Address* is 7,823 words (7,301 with footnotes removed) and *On the Vanity of Idols* is 3,395 (2,987). Step 0 did not count them. The rest of Cyprian is another world's (row 65).

**Arnobius (row 38).** *Against the Heathen*, seven books: 140,826 words in the ANF English (104,704 with footnotes removed). Latin in Reifferscheid's CSEL 4 and in a TEI file of the same edition.

**Commodian (rows 39–40).** The *Instructiones*: 15,008 words in the ANF English, and Latin in Dombart's CSEL 15 and a TEI file. The *Carmen apologeticum* is Latin only, with no English text located. Counted in the TEI files, the *Carmen apologeticum* is 7,334 Latin words and the *Instructiones* are 9,434, by two counting methods that agree. The Latin counts cannot be set beside the English ones.

**Lactantius (rows 41–45).** Three genuine works are counted: *The Divine Institutes* (242,005 words, with the *Epitome* inside the same division), *On the Anger of God* (20,397) and *On the Workmanship of God* (18,853), 281,255 together. Latin in Brandt's CSEL 19 and TEI, and in CSEL 27 part 1. **A correction to Step 0.** The ANF07 division headed "Fragments of Lactantius" (row 44) has three parts. Four short prose fragments of his lost works come first, quoted through later authors (509 words). Two poems of uncertain authorship follow: the *Phoenix*, headed "By an Uncertain Author. Attributed to Lactantius", and a poem on the Passion, headed "Formerly Ascribed to Lactantius" (2,285 and 961 words). The editor's General Note closes the division (177 words). The General Note says there is no manuscript authority for ascribing "the above" to Lactantius. It follows the Passion poem, and the file does not say whether it reaches the *Phoenix*. It does not touch the prose fragments. Step 0 counts all 3,932 words as Lactantius's fourth work, which gives its 285,187. The three genuine works are 281,255 words. With the 509 words of his fragments they are 281,764. The Latin of the poems and of the lost-works fragments is in Brandt, CSEL 27 part 2 fascicle 1 (row 45). The ledger carries the finding, and Step 0 is not edited. Doc_01 §3 repeats Step 0's 285,187; the difference changes none of its comparisons.

**The *Passion of Perpetua and Felicitas* (row 46).** 7,325 words in the ANF English. Robinson (1891) carries the Latin and the Greek as a second witness (pages 60–95 of his volume).

**Voice flags.** The flags below say whose words a file holds. A Representative may speak only the world's own voice from a `tradition` row, and the opponent's words stay the opponent's.

- *The Octavius* (row 33) has three voices. Minucius frames the dialogue (chs. I–IV, and the close at XXXIX and XLI on the ANF chapter headings). Caecilius, the pagan, speaks chs. V–XIII, and his words there are the opponent's case. Chapters XIV and XV are an exchange between Minucius and Caecilius, so the speaker is checked line by line. Octavius, the Christian, speaks chs. XVI–XXXVIII. In ch. XL Caecilius says he is won over, so his words there are a convert's.
- *Ad Nationes* (row 2) quotes the pagan writer Varro in Book II, by report.
- *The Prescription*, *Against Marcion*, *Against Hermogenes*, *Against the Valentinians*, *On the Flesh of Christ*, *On the Resurrection of the Flesh* and *Against Praxeas* (rows 13–19) state the opponents' positions in order to refute them. Those statements are the opponents' views as Tertullian reports them. The opponents themselves are an Excluded row (row 67).
- *Arnobius* (row 38) answers objectors in the second person; their questions, for example at Book I ch. 60, are theirs.
- *On the Vanity of Idols* (row 36) is a compilation. On Harnack's report its chapters 1–9 follow the *Octavius* and its chapters 10–15 follow the *Apology* (row 47). Whether it is Cyprian's is Contested: Harnack reports that Benson, Monceaux and Bardenhewer have defended its authenticity (row 47, file line 18930). Its words are not quoted here as Cyprian's argument or as Minucius's or Tertullian's.
- *The Appendix of poems* (row 32) is pseudonymous verse that the ANF file prints with no author. The two poems in the ANF07 "Fragments of Lactantius" (row 44) are of uncertain authorship. The editor's General Note, which follows the Passion poem, says there is no manuscript authority for ascribing "the above" to Lactantius. The prose fragments I to IV in the same division are quotations of his lost works through later authors.
- *The Passion* (row 46) is mixed. Perpetua speaks in the first person in the ANF chapters I–III, Saturus tells his own vision in chapter IV, and a compiler writes the preface and the frame.

**What each kind of file is good for.** The library rule (`cic/texts/INTAKE.md`) is that a clean public-domain original can be primary evidence, and that scan quality decides whether it can be quoted.

| File kind | Files | Use |
|---|---|---|
| ANF and NPNF English, XML with division ids | `anf03`–`anf07`, `npnf203`, `npnf206` | The reading base in English. A quotation is addressed to a division id and checked verbatim. The editors' notes and brackets are part of the file and are not the author's (row 62). |
| TEI Latin, machine-corrected, CC BY-SA 4.0 | Halm (*Octavius*), Reifferscheid (Arnobius), Dombart (*Instructiones* and *Carmen apologeticum*), Brandt (*Institutes*), Hartel (the two Cyprian works) | The preferred base for quoting Latin. Attribution and share-alike travel with any quotation. |
| Raw OCR of critical editions, apparatus interleaved | Tertullian in CSEL 20 and CSEL 47, Boenig, Waltzing, CSEL 4, CSEL 15, CSEL 19, CSEL 27, CSEL 3 | A cross-check on the TEI and the only Latin for most of Tertullian. A quotation is checked against the scan before it is used. |
| Raw OCR of an older recension | Oehler (1853), two volumes | The only public-domain Latin for 15 of Tertullian's works. Where CSEL also has the work, CSEL is the better base. |
| Latin and Greek second witness | Robinson (1891), Gebhardt (1902, no. VII) and Knopf-Krüger (1929, no. 8) for the *Passion* | A second witness to the English. The Robinson header warns of letter confusions. Gebhardt and Knopf-Krüger are listed on row 46; their Latin was not read in this pass. |

**Quotability in the process vocabulary.** ANF and NPNF English and the TEI Latin are verbatim-ready once the quotation is matched to the file. Raw OCR scans and the Latin and Greek second witnesses are second-witness only until the quotation is matched to the scan. Harnack and Schanz–Hosius–Krüger are consultation only. No vendored file read for this document was unusable.

**Primary and cross-check, work by work.** The English is the primary reading text for every work except the *Carmen apologeticum*, for which the Latin is the only text. Where a TEI file exists it is the Latin base. Where only raw OCR exists, which is the case for all 31 of Tertullian's Latin works, the English is the base for the Representative's reading and the Latin is the cross-check, to be matched against the scan before any Latin phrase is quoted. The Registry's Files table lists the file behind each row, and the counts above are this document's own.

**What the shelf still lacks.** No Latin text of the *Appendix* poems. No English of the *Carmen apologeticum*, which a Representative would render from the Latin. No critical text of Jerome's *Chronicle*, which is where Arnobius's dream and bishop appear (row 68). No text of Augustine's *De haeresibus* (row 69). The later critical volumes of Tertullian, CSEL 69 and 70, are in copyright (row 71). Lactantius's letters to Demetrianus are lost (row 72). Ebert and Norden on the *Octavius* are not vendored (row 73). Nothing is on the shelf in a woman's own voice except the visions inside the *Passion*, and nothing from a layperson, a pagan, a Jew or a Roman official in his own words. §6 and §7 state what follows.

---

## 2. Author Gravity Assessment

Five dimensions: Visibility, Representativeness, Influence, Limitations, Transmission History. Dates are tagged with the five-level vocabulary, and each tag names its source.

### Tertullian of Carthage (rows 1–32)

- *Visibility:* Over-visible. He is 61 percent of the counted words (§1) and he wrote in both directions, to outsiders and to Christians. The shelf's first fixed date, the *Apology* at the end of 197, is his (Dominant Modern Reconstruction on Harnack's table at printed pp. 295–296, row 47). Any gravity that rests on his texts alone is an author finding before it is a world finding (Doc_01 §3).
- *Representativeness:* He speaks for himself and for the church of Carthage. He does not speak for the Latin church generally, and nothing on the shelf shows how other Carthaginian Christians thought. His career has two parts, and the disclosure in §7 item 5 binds. The works before the break with the church and the works after it are not one voice. Jerome's notice (row 54) says he was a presbyter until middle life and then lapsed to Montanus.
- *Influence:* Later authors on the shelf use him. Commodian read him, which is Widely Accepted on Dombart's preface (Step 0 §4 item 1). The compiler of *On the Vanity of Idols* copied the *Apology* into chapters 10–15, on Harnack's report (row 47). Lactantius names him, with Minucius Felix and Cyprian, among the earlier Latin writers at *Institutes* V.1, and judges him learned in every kind of literature but unpolished and very obscure (row 43). Jerome's *Letter LXX* lists him among the Christian writers who used pagan learning (row 60). Doc_01 §7 states what the shelf cannot show: who first used a given Latin word. The shelf shows a word in use and cannot show first use.
- *Limitations:* A strong, argumentative, sometimes severe voice, and the prose is a stylistic and doctrinal outlier. The *Appendix* poems are printed under his name, but the file names no author for them (row 32, §6). The seven New Prophecy works are a later, separate stage (§7 item 5). Jerome's notices name works that are not on the shelf: *On persecution* appears on the shelf as *De Fuga*, but *On ecstasy* and *Against Apollonius* (row 54) and *On the hope of the faithful* (row 58) do not.
- *Transmission History:* The Latin of Tertullian reaches us by more than one route. CSEL 20's preface says its first volume holds the works that are kept in the Agobardinus alone, or in no manuscript that survives, so that they rest on the old printed editions (`tertullian_opera-pars1-lat_reifferscheid-wissowa-csel20.txt`, lines 138–145). It calls Paris lat. 1622, the Agobardinus, a ninth-century parchment named for its first owner Agobard, bishop of Lyon, the best of all the manuscripts by age and by worth (lines 158–160). The works in CSEL 47 rest on two eleventh-century manuscripts, one at Montpellier and one called Paterniacensis, and on the first and third editions of Beatus Rhenanus (`tertullian_opera-pars3-lat_kroymann-csel47.txt`, lines 119–123). The English in ANF is a nineteenth-century translation from such editions. Harnack's chronology table is a reconstruction, as his own text says of the order inside one group of works (row 47).

### Minucius Felix (row 33)

- *Visibility:* Thin. One work, 23,819 words, about 2 percent of the counted words. Jerome's notice (row 55) says he was a Roman advocate and that Lactantius mentions him, and that a second work, *On fate*, is ascribed to him. Nothing else about the man is on the shelf.
- *Representativeness:* He speaks for the educated Roman Christian who writes for educated pagans. The frame is a conversation on the beach at Ostia. The dialogue is a literary form, so the pagan speaker's words are a Christian author's presentation of an opponent (§1, voice flags).
- *Influence:* Lactantius names him (row 43). The compiler of *On the Vanity of Idols* copied him into chapters 1–9, on Harnack's report (row 47). Jerome's *Letter LXX* names him (row 60).
- *Limitations:* The date is Contested and cannot be given as one year (§7 item 1; Doc_01 §2). The text is silent on Christ in the author's own prose (§7 item 3).
- *Transmission History:* The *Octavius* rests on a single manuscript. Reifferscheid's preface to Arnobius (CSEL 4) says that the work survives in one old codex, now Paris lat. 1661, and that the *Octavius* is owed to that same codex alone, where it stands as an eighth book after Arnobius's seven (`arnobius_adversus-nationes-lat_reifferscheid-csel4.txt`, lines 249–253). Boenig's preface repeats the codex's number and quotes Reifferscheid's description: written at the start of the ninth century in minuscule, with the words mostly not separated, and copied from an exemplar in cursive script (`minucius-felix_octavius-lat_boenig1903.txt`, lines 147–153). CSEL 4 says that Faustus Sabaeus first edited Arnobius from this codex in 1543 (lines 252–255).

### Cyprian, two works ascribed to him (rows 34–37)

- *Visibility:* Small. The *Address* is 7,823 words and *On the Vanity of Idols* is 3,395. The ANF05 headings give editors' dates of 252 and 247 for the two (row 62 explains how such dates are read). The rest of his writing is another world's (row 65).
- *Representativeness:* The *Address to Demetrianus* is Cyprian's, written to a pagan who blamed Christians for disasters. Harnack dates it to the end of 251 or the start of 252 (row 47). Monceaux II puts it in 252 or 253 during the plague (row 50). *On the Vanity of Idols* is, on Harnack's report, a compilation of the *Octavius* and the *Apology*. Whether Cyprian wrote it is Contested: Harnack says Benson, Monceaux and Bardenhewer have defended its authenticity (row 47, file line 18930), and the ascription is shown here as disputed (§8).
- *Influence:* The compilation is testimony that a later reader drew on Tertullian and Minucius. It shows use and shows nothing more.
- *Limitations:* The *Address* answers the charge that Christians cause disaster, from an author whose pastoral voice belongs to another world (row 65). The other work is a compilation on Harnack's report. Doc_02 does not claim that either is a new apologetic argument.
- *Transmission History:* Both works are in Hartel's CSEL 3 (1868), as OCR and as TEI, and in the ANF05 English. The editors' choice of base manuscripts was not read in this pass.

### Arnobius of Sicca (row 38)

- *Visibility:* One large work, 140,826 words, about 12 percent of the counted words. Jerome's notice (row 56) says he taught rhetoric at Sicca under Diocletian and wrote volumes *Against the nations*. The notice says nothing about a dream or a bishop; those belong to the *Chronicle* (row 68).
- *Representativeness:* He speaks for a teacher of rhetoric in an African provincial town who writes in the first years of the Great Persecution. Nothing shows how many Christians thought as he did. His teaching on the soul is an idiosyncratic position (§7 item 2).
- *Influence:* The tradition that Lactantius was his pupil rests on Jerome alone (row 57, *De viris illustribus* 80; Doc_01 §4). The Registry rows record no passage in which Lactantius uses Arnobius, and none was looked for.
- *Limitations:* The text states a position on the soul that Step 0 §4 item 2 names as idiosyncratic; this document does not smooth it (§7 item 2). Of Book II, chapters XXXI, XXXV and LXII were read for the soul (§7 item 2). Books III to VII were not read in this pass (Registry row 38).
- *Transmission History:* One old codex, Paris lat. 1661, carries all seven books (CSEL 4, lines 245–248). Reifferscheid says the codex was at Rome in the sixteenth century, where Sabaeus printed it in 1543 (lines 252–255). The ANF06 English comes with an introductory notice that gives "[a.d. 297–303.]" and quotes Jerome's *Chronicle* (row 62).

### Commodian (rows 39–40)

- *Visibility:* Thin. Two poems, together 15,008 English words for the *Instructiones* and a Latin-only *Carmen apologeticum* (§1).
- *Representativeness:* He speaks in verse, to pagans, Jews and catechumens. Gennadius's notice (row 59) calls him a convert who wrote in rough verse against the pagans and gives no date. Who he was, where he lived and for whom he wrote are open (§7 item 1).
- *Influence:* He used Cyprian and read Tertullian and Minucius (Widely Accepted, Dombart's preface; Step 0 §4 item 1). That makes him later than they were. Harnack also finds a probable use of Lactantius (row 47). No author on the shelf cites him.
- *Limitations:* His date is Contested over three centuries: a mid-third-century view, a view of the 260s to 313, and Brewer's thesis of 458 to 466 (row 52), which Harnack calls paradoxical (row 47). The thesis is a minority one, and it is disclosed wherever his date is used.
- *Transmission History:* The *Instructiones* survive in one old manuscript, the Cheltenham (Middle Hill) codex, a parchment of the eleventh century, described in Haenel's catalogue and carried to Cheltenham with the Middle Hill library (`commodian_carmina-lat_dombart-csel15.txt`, lines 490–499). Two other copies are paper manuscripts of the seventeenth century, Paris lat. 8304 and a Leiden Vossianus (lines 537–540).

### Lactantius (rows 41–45)

- *Visibility:* The widest of the later authors: three genuine works, 281,255 words, and fragments of lost works (§1). Jerome (row 57) says he taught at Nicomedia, lists his works, and says he was tutor to Crispus in his extreme old age.
- *Representativeness:* He speaks from a teacher's chair at Nicomedia, then, on Jerome's report, from Constantine's court. Dating: *On the Workmanship of God* 303/304, the *Institutes* begun 304 and finished before April 311 (Widely Accepted for 304–311), the *Epitome* after 313, all on Harnack (row 47; Step 0 §4 item 5).
- *Influence:* Jerome's *Letter LXX* lists him (row 60). Commodian shows a probable use of him on Harnack's reading (row 47). Lactantius himself names Minucius and Tertullian among his predecessors (row 43, *Institutes* V.1).
- *Limitations:* Four complications, all disclosed in §7 item 4: Jerome's charge on the Holy Spirit (row 61), the chiliasm that Jerome reports (row 58), the Book II passage on a second being (Doc_01 §8), and the dualist passages that Brandt argues are not his. The two poems printed under "Fragments of Lactantius" are not shown to be his (row 44). *De mortibus persecutorum* is attached to another world's shelf and its authorship is disputed (row 63; §7 item 7).
- *Transmission History:* The oldest manuscript is the Bononiensis, of the sixth or seventh century (`lactantius_divinae-institutiones-epitome-lat_brandt-csel19.txt`, lines 217–219). A Saint Gall palimpsest is badly damaged and the Floriacensis survives only in small fragments of *On the Workmanship of God* (lines 219–221). Brandt says some manuscripts carry two kinds of added passage: addresses to Constantine, and teaching of a dualist kind. He argues that neither kind is Lactantius's (lines 592–603). The dualist passages are therefore a manuscript-tradition question and not a settled part of his text.

### The verse of uncertain authorship

*The Appendix of poems* (row 32) and the two poems in the ANF07 "Fragments of Lactantius" (row 44) are verse of uncertain authorship printed in the English volumes under the names of Tertullian and Lactantius. They are on the shelf so that a reader can reach them. They are not to be quoted as either author's voice. The map keeps the *Appendix* under Tertullian's name and also assigns it to the apocryphal literature bucket. The file heads the second *Appendix* poem "Author Uncertain" and prints no author for the others.

### Jerome and Gennadius, the narrative sources (rows 54 to 61)

Jerome shapes how four of the five authors are known, so he gets the five dimensions.

- *Visibility:* Over-visible as a witness. The biographical notices on Tertullian, Minucius, Arnobius, Lactantius and Commodian come from Jerome, from his continuator Gennadius, or from nothing. The Montanist lapse, the teacher-pupil link between Arnobius and Lactantius and the tutorship of Crispus are his statements (rows 54, 57).
- *Representativeness:* A Latin scholar writing after the window closes, in the 390s to 400s on the NPNF headnotes' reckoning (row 60), for readers who wanted a list of Christian writers. He does not speak for any of the five.
- *Influence:* Harnack prefers his order of Tertullian before Minucius to Lactantius's, because Jerome means to be chronological and Lactantius does not (Step 0 §4 item 1). His charge on the Holy Spirit in *Letter* LXXXIV (row 61) is the sharpest outside judgment on Lactantius's doctrine; Jerome's notice on Papias (row 58) is another.
- *Limitations:* A notice is short. The notice on Arnobius says nothing of the dream and the bishop, which belong to the *Chronicle* (row 68, not vendored). The NPNF glosses of dates (for example "Born about 160" for Tertullian, "Flourished 196?" for Minucius, "Died 325" for Lactantius) are the editor's. The charge in *Letter* LXXXIV is hostile and is Jerome's, not Lactantius's words.
- *Transmission History:* The notices are in the NPNF English (`npnf203`, `npnf206`). The *Chronicle* is not on the shelf in a critical edition (row 68).

Gennadius, the continuator, gets the same five dimensions because he is the sole ancient notice on Commodian.

- *Visibility:* One short notice (row 59), and nothing else on the shelf about the man.
- *Representativeness:* A Latin continuator of Jerome writing in the fifth century, so far from his subject. Harnack puts his writing between 477 and 494 (row 47).
- *Influence:* None shown. No author on the shelf cites him.
- *Limitations:* He calls Commodian a convert who wrote in rough verse against the pagans and gives no date. The NPNF gloss "Flourished about 270" is the editor's.
- *Transmission History:* The notice is in the NPNF English (`npnf203`). The Latin was not read.

### The *Passion of Perpetua and Felicitas* (row 46)

- *Visibility:* One text, 7,325 English words. Robinson's Latin and Greek, Gebhardt's Latin (1902, no. VII) and Knopf-Krüger's Latin (1929, no. 8) are second witnesses; the second and third were not read in this pass (row 46).
- *Representativeness:* The visions of Perpetua and Saturus are their own writing (Widely Accepted). The compiler of the frame is Contested (§7 item 6). Perpetua is the one woman's voice on the shelf, and her words reach us inside a compiler's frame.
- *Influence:* None shown on the shelf.
- *Limitations:* It must not be presented as Tertullian's work.
- *Transmission History:* Robinson's introduction says that the Latin text survives, even approximately intact, in one manuscript only, found by Holsten at Monte Cassino and published at Rome in the seventeenth century (`perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, lines 193–200). A complete Greek text was discovered in 1889 by Rendel Harris (line 219). The Cassino catalogue describes the manuscript as written in a twelfth-century hand and, at another place, as probably of the eleventh century, a judgment that the Archivist of Monte Cassino shares (lines 743–750). Robinson's later chapters compare the Greek and the Latin witnesses (lines 838–850). This build did not read to his conclusion on which is the original.

---

## 3. Secondary Scholarship Assessment

None of these is a voice of the world. Each is consulted for a date or a fact, and each is a reader's reading.

**Harnack, *Die Chronologie der altchristlichen Litteratur bis Eusebius*, Band 2 (1904; row 47).** The dating authority for this shelf. His Tertullian table (printed pp. 295–296) gives a date for every work; his sections on Minucius, Cyprian and the pseudo-Cyprian work, Arnobius, Lactantius and Commodian supply the other dates. *Strengths:* he gives his reasons and flags uncertainty, for example that the order inside Tertullian's 198–202/3 group is only partly certain. *Limits:* 1904; Fraktur-era OCR, so each wording is checked against the scan; many of his dates are contested by others, and several of his figures are one scholar's reconstruction (Dominant Modern Reconstruction). He calls Brewer's date for Commodian paradoxical.

**Schanz, Hosius and Krüger, *Geschichte der römischen Litteratur*, Teil 3 (3rd ed., 1922; row 48).** A handbook. On the *Octavius* it declines to choose between the dates; its text says that a handbook cannot take one subjective standpoint on the dating (page 268, row 48). Consulted for the survey of the proposals. The page numbers 267–269 that Step 0 cites were not each re-read.

**Monceaux, *Histoire littéraire de l'Afrique chrétienne*, Tomes I–III (1901–1905; rows 49–51).** The African church's literary history. Tome I: the dating note for the *Octavius* (pole B, "entre 213 et 250") and the list of scholars for pole A; the *Passion* on 7 March 203. Tome II: the *Address* in 252 or 253. Tome III: Arnobius between 284 and 311, the *Institutes* 307–311, Commodian between 260 and 313. *Limits:* the Tertullian table in Tome I is OCR with its columns separated, so no work is dated from it; Harnack's table is used instead.

**Brewer, *Kommodian von Gaza* (1906; row 52).** The one book-length argument for the fifth-century Commodian. It is on the shelf so that the minority thesis can be named from its author's own words. *Limits:* only the title page, the preface, the contents and the statements of the range at three places were read; Brewer's argument as a whole was not (Step 0 §4 item 1 says the same). It is not to be presented as the settled date.

**Audollent, *Carthage romaine* (1901; row 53).** A city history, in two scans. Consulted for §5.

**The ANF editors (row 62).** Coxe, Wallis and the others supply introductory notices and footnotes that propose dates and attributions: Coxe's "[a.d. 210.]" for the *Octavius*, Wallis's two conditionals, a "[ a.d. 240.]" note for Commodian, the Arnobius notice. They are reported as proposals and are never evidence for a date. One ANF footnote at *Octavius* ch. IX, which names the author as a chief magistrate of Cirta, is a misattribution (Doc_01 §2).

**Not on the shelf.** Ebert (1868/70), Norden (1897), Massebieau, Neumann, Aubé, Allard, Schultze, Kraus, Jülicher, Leimbach, Bardenhewer and Teuffel–Schwabe are known only as the three vendored scholars report them (rows 73–74). Scholarship after 1930 was not consulted. That post-1930 work has revised these dates is UNVERIFIED, from memory, and no name or date is asserted.

---

## 4. Formation Narrative Sources

The shelf has no document in which the movement tells its own origin. What exists is a set of outside notices and a few passing remarks by the authors, all later than the events they describe.

- *The authors on one another.* Lactantius at *Institutes* V.1 lists the earlier Latin defenders he knows, among them Minucius Felix, in terms Step 0 quotes (row 43; Step 0 §4 item 1). That is the one place where a member of the shelf describes the others.
- *Jerome's notices (rows 54–58) and *Letters* LXX and LXXXIV (rows 60–61).* Jerome wrote in the 390s to 400s, a century or more after most of the authors. His notices say what he knew or believed about each man. Where the NPNF editor adds a date or a gloss, the date is the editor's.
- *Gennadius (row 59).* A continuation of Jerome's work, written between 477 and 494 on Harnack's reckoning (row 47), and giving no date for Commodian.
- *Jerome's *Chronicle* (row 68), not vendored.* It carries the year and the story of Arnobius's dream and bishop. Only a 1658 Latin text was found, and the ANF06 notice quotes the passage in English.
- *Augustine, *De haeresibus* ch. 86 (row 69), not vendored.* A second ancient witness to Tertullian's later career.
- *The *Passion* (row 46).* A narrative of martyrdom, compiled by an unknown hand around the martyrs' own writing.
- *Tertullian's own remarks.* His conversion between about 190 and 195 is Harnack's reconstruction from his table and is Dominant Modern Reconstruction. His training as an advocate is the census's statement alone, and no vendored source read in this build says it (Doc_01 §6, Cell 1B).
- *The teacher-pupil link.* Arnobius as the teacher of Lactantius rests on Jerome alone (Doc_01 §4).

So a Representative should not say "we came to be" in a collective voice that no source on the shelf uses. Each author speaks for himself, and the shelf as a whole is a set of occasions, not a founding story.

---

## 5. Material Culture and Daily Life Sources

**What is on the shelf.** Audollent's *Carthage romaine* (row 53) is the one volume assigned to this world for the city. It is a history of Roman Carthage to the Arab conquest, in two scans. Its table of contents (the Ottawa scan, file lines 47640–47710) has a book on the fine arts and industry and, in Livre VII, a chapter headed *Les chrétiens* (pp. 719–748). Passages that cite Tertullian were located by search at lines 3896, 13017, 13751 and 17058 of that scan and were not each re-read. Audollent is a city history and is no witness to any ancient text.

**What is deferred.** *CIL* VIII, the Latin inscriptions of Africa, is on the shelf for another world. The dossier's link is Sicca, Arnobius's town, in Numidia. No inscription was located or read against a claim of this world (ledger entry on the CIL VIII Numidia cross-link). No coin, tomb, church building or amphitheatre is assigned or read.

**What the texts themselves show.** Practice reaches us only through the authors' descriptions: baptism (row 21), prayer (row 22), the refusal of the shows (row 6), the soldier's laurel crown (row 7), the veil (row 28), fasting (row 30). *Apology* chapter 39, on which another world draws for the Christian assembly, was not read here (Doc_01 §7). What these texts give is a speaker's account of what believers did or ought to do. They are prescription and argument. They are not a record of ordinary practice.

**What is missing.** No inscription, grave or building. No papyrus or letter from a believer's household. No evidence for how often anyone followed the rules the authors set. §6 states the asymmetry.

---

## 6. Source Asymmetries and Missing Voices

**Whose voices carry the world.** Every named author on the shelf is a man who wrote Latin prose or verse for readers. Jerome says Minucius was a Roman advocate and Arnobius a teacher of rhetoric (rows 55 and 56). Lactantius taught at Nicomedia (row 57). The census says Tertullian was trained as an advocate; no vendored source read says so (§4). Commodian is a convert who wrote rough verse (row 59). So the world's own voice is the voice of educated men who answer, argue and teach. The people they wrote about are not heard.

**Missing voices.**

- *Women.* Perpetua's visions are the only writing in a woman's voice, and they reach us in a compiler's frame. Tertullian's treatises on dress, marriage and the veil address women and speak about them; they are not women's own words (rows 25–28).
- *Ordinary believers.* No document is by a layperson, a slave, a soldier or a tradesman, apart from Perpetua and Saturus. The soldier in *The Chaplet* is described by Tertullian (row 7).
- *Pagans.* The objector's case reaches us only as the apologists report it: Caecilius in the *Octavius*, Varro in *Ad Nationes*, the objectors Arnobius answers. Pagan words stay the opponent's.
- *Jews.* *An Answer to the Jews* (row 11) is an argument with a Jewish interlocutor, from the Christian side.
- *Rival Christians.* Marcion, Hermogenes, the Valentinians and Praxeas are heard only through Tertullian (row 67).
- *The church at Rome and the bishops.* The bishop attacked in *On Modesty* is Callistus or Zephyrinus, and which is Contested (§7 item 5). No bishop of Rome speaks.
- *Officials.* The Roman side of the persecutions is present only in the *Passion*'s frame and in the apologists' replies. *To Scapula* is a letter to a proconsul, from Tertullian's side (row 3).
- *Later Africa.* After Lactantius the shelf thins (Doc_01 §6, Cell 3B). That is an absence, stated as an honest limit, and not rated.

**The forces lens.** The Forces Framework asks which voices carry each force. Doc_01 §6 gives the preliminary matrix. This table says what source carries each cell.

| Force | Carried by | Not carried |
|---|---|---|
| Initiating, external: the charge of causing disaster, and the Severan persecution | Arnobius I.1, the *Octavius*, the *Passion* (rows 38, 33, 46) | The accusers' own writing |
| Initiating, internal: conversion and the first Latin treatises | Harnack's table (row 47); the census for the advocate's training | Tertullian's own account of his conversion, which no vendored text read gives |
| Ongoing, external: persecution, the plague, the edicts of 303 | The *Passion*; Harnack and Monceaux II on the plague (rows 47, 50); Harnack on Lactantius under the edicts | Any official record |
| Ongoing, internal: rival teachers, the break with the church, the bishop's power to forgive | Tertullian's treatises against Marcion, Hermogenes, the Valentinians and Praxeas (rows 14–19); *On Modesty* (row 31) | The rivals' and the bishop's own words |
| Ending, external: toleration of 311 and Constantine's court | Harnack on the edict of Galerius (row 47); Jerome on Crispus (row 57) | Any imperial text on the shelf |
| Ending, internal | No source. An absence | — |

---

## 7. Required Disclosure

The Article 4 check stands in Doc_01 §8, which quotes the five commitments and states each result at its own strength. This document does not repeat it. Item 3 below adds the source-level fact about the *Octavius*. Each item below is binding on this document and is met where it says. The first six are Step 0 §4 items 1, 2, 3, 5, 8 and 9. The seventh and eighth are items 6 and 7, which do not bind Doc_02 by name and are reported because Doc_01 §9 carries them. Item 4 of Step 0 is resolved and asks nothing of this document.

**1. Minucius Felix and Commodian's dating (Step 0 §4 item 1).** The *Octavius* is dated as two Contested ranges and never as one year: c. 160–192 (pole A, before Tertullian's *Apology*) or c. 200–250 (pole B, after it). Pole A lies wholly before the window and pole B lies inside it. Where the *Octavius* is used, the dispute is stated where the work is used. A `contested_claim` record is warranted. Two outer limits rest on texts: the *Octavius* speaks of Fronto as a familiar figure (`Documented` as a mention; the date it yields, not earlier than about 160, is Dominant Modern Reconstruction), and Lactantius names the book (`Documented`). The ancient order is no help: Jerome places Minucius after Tertullian and Lactantius places him before. Schanz, Hosius and Krüger decline to choose. The census phrases that Doc_01 does not adopt are listed in Step 0 §4 item 1, rule (a). Tertullian's *Apology* is the roster's best-anchored first date and is not the opening of the Latin case.
Commodian's date is Contested. That he used Cyprian and read Tertullian and Minucius is Widely Accepted. The span is Contested: mid-third century (Dombart), 260–313 (Harnack, Monceaux, Aubé), and 458–466 (Brewer), which is a minority thesis and is disclosed wherever his date is used. The tables are in Step 0 §4 item 1 and are not copied here.

**2. Arnobius's anthropology, provenance and date (Step 0 §4 item 2).** His teaching that the soul is not naturally immortal is a real, idiosyncratic position of Book II. It is read here in his own text. Chapter XXXI speaks of "a certain neutral character, then, and undecided and doubtful nature of the soul". Chapter XXXV takes up the objection "if souls are mortal" and of neutral character, and chapter LXII says that no one besides the Almighty can give souls "length of days" (ANF06, Book II). Step 0 asks that the doctrine be attributed on Jerome's report and not on Arnobius's admission. The vendored Jerome notices (rows 56 and 60) say nothing about the soul, so that wording cannot be met from the shelf; the ledger records the mismatch. The dream and the bishop are a separate matter: the story belongs to Jerome's *Chronicle* alone (row 68), and Jerome's notice (row 56) does not tell it. Date: composition c. 296–310, Widely Accepted for the span c. 295–310; the finer order (Books I–II first, the later books after 303) is Dominant Modern Reconstruction. Jerome's 326/327 is Documented as a statement and is rejected as a date of composition.

**3. Minucius Felix's Christological absence (Step 0 §4 item 3).** The author's own prose has zero occurrences of "Jesus", "Son of God" or incarnation language. "Christ" and "crucifi-" together occur four times in the ANF file, all in editorial apparatus: two chapter headings, one footnote and one bracketed gloss, none in Minucius's text. Doc_01 §8 re-counted and confirmed this. It is a disclosed textual fact, bounded by what was counted. It does not decide the live scholarly question of why. That question stays open, and the dating question at item 1 does not change this duty.

**4. Lactantius's pneumatological and eschatological complications (Step 0 §4 item 5).**
- *The Spirit.* Jerome's charge in *Letter* LXXXIV (row 61) is that Lactantius, in his books and particularly in his letters to Demetrianus, denies the subsistence of the Holy Spirit. The charge is aimed at his books generally and so reaches the vendored *Institutes*. The letters, its sharpest instance, are lost (row 72), and no primary text of that instance survives.
- *Chiliasm.* Jerome's notice on Papias (row 58) lists Lactantius among those who hold that the Lord will reign in the flesh with the saints.
- *The Book II passage on a second being* (Doc_01 §8) and *the dualist passages* that Brandt argues are not Lactantius's (§2).
- *The works are dated* between c. 303 and c. 317, inside the window. Tags: *Institutes* Widely Accepted for 304–311; *De mortibus* Contested (Harnack 313–314, Brandt April 315, Seeck 317–321); the tutorship of Crispus Documented as Jerome's statement and Dominant Modern Reconstruction as Harnack's arithmetic for c. 317 (Step 0 §4 item 5).

**5. Tertullian's New Prophecy works (Step 0 §4 item 8).** Seven works are on both this shelf and the New Prophecy shelf: *On Monogamy*, *On Modesty*, *On Fasting*, *On the Veiling of Virgins*, *On Exhortation to Chastity*, *De Fuga in Persecutione* and *Against Praxeas*. Six are shared rows on the map (rows 27–31 and 10), and *Against Praxeas* (row 19) has its own row in that bucket. This is a real, disclosed shift in authority and discipline, not a floor-level divergence. Two of the seven, *On Exhortation to Chastity* and *On the Veiling of Virgins*, are pre-break and transitional on all three dating tables (Harnack 204–206/7). They must not be presented as post-break works, and the map marks both, and *De Fuga*, `provisional`. Tags: the relative order *De Fuga*, *On Monogamy*, *On Fasting*, *On Modesty* is Widely Accepted; the absolute years are Dominant Modern Reconstruction; the identity of the bishop in *On Modesty* (Callistus or Zephyrinus) is Contested. This document does not flatten Tertullian into one voice across his career. The works before the break, the transitional works and the New Prophecy works are different stages, and the date of the break is Contested (207/8 or 213). The full table of the three scholars' dates is in Step 0 §4 item 8.

**6. The *Passion* (Step 0 §4 item 9).** Date: 7 March 202 or 203, under Severus, Widely Accepted. The visions of Perpetua and Saturus are their own writing, Widely Accepted. The compiler of the rest is Contested: Robinson finds it highly probable that Tertullian wrote it, Coxe thinks he was its editor, Harnack, Neumann and Monceaux doubt it, and Harnack says certainty cannot be reached. That the compiler's own colouring is Montanist is Dominant Modern Reconstruction. The *Passion* must not be presented to a Representative as Tertullian's own work.

**7. *De mortibus persecutorum* (Step 0 §4 item 6).** Harnack holds the work Lactantius's and Brandt denied it. The map assigns it to Imperial-Juridical Christianity (row 63, Excluded as a Named Comparandum). Doc_02 names the authorship dispute wherever the work is named and does not use the work as this world's voice.

**8. Overlap with built worlds (Step 0 §4 item 7; Doc_01 §7).** *PAHC* cites Tertullian's *Apology* and *Against Marcion* as etic corroboration, and one of its force records says the *Apology* "opens" a body of Latin defense, a wording this world does not adopt (ledger entry on the overlap sweep). *LPC* shares the two Cyprian works and cites *On Modesty* chapter XXII (ledger entry on that citation). *IJC* holds *De mortibus* only. The requests to the neighbours to confirm the boundary are logged in the ledger entry on neighbour confirmation. Four more items from the dossier are also logged: the I.33 touchpoint through *On Modesty*, the fleet-level source record on *Against Praxeas* that says the ANF03 edition carries no Latin, IJC's dates for the author of *De mortibus*, and the stale references elsewhere. No built world's record is edited here.

---

## 8. Confidence Map

Tags use the five-level vocabulary. "Absence" is not a rating. Sources are Registry rows.

| Claim | Tag | Source |
|---|---|---|
| *Apology* at the end of 197 | Dominant Modern Reconstruction | Harnack's table (row 47) |
| *Ad Martyras*, *Ad Nationes*, *Soul's Testimony* in 197 or soon after | Dominant Modern Reconstruction | Harnack's table |
| Tertullian's 198–202/3 group (*Shows*, *Baptism*, *Patience*, *Prayer*, *Idolatry*, *Prescription*, *Hermogenes*, *Answer to the Jews*, *To His Wife*, *Apparel of Women*) | Dominant Modern Reconstruction | Harnack's table; the order inside the group is only partly certain |
| *Exhortation to Chastity*, *Veiling of Virgins* before the break | Widely Accepted that they are pre-break and transitional; years Dominant Modern Reconstruction | Step 0 §4 item 8 |
| Relative order of *De Fuga*, *Monogamy*, *Fasting*, *Modesty* | Widely Accepted | Step 0 §4 item 8 |
| Date of the break with the church, 207/8 or 213 | Contested | Harnack, Schanz–Hosius–Krüger, Monceaux |
| Bishop in *On Modesty* | Contested | Step 0 §4 item 8 |
| *Octavius*, c. 160–192 or c. 200–250 | Contested | Monceaux I, Harnack, Schanz–Hosius–Krüger, ANF04 |
| Not earlier than about 160 (Fronto) | Dominant Modern Reconstruction | Step 0 §4 item 1 |
| Lactantius names the *Octavius* | Documented | *Institutes* V.1 (row 43) |
| *Address to Demetrianus*, end of 251 to 253 | Dominant Modern Reconstruction | Harnack and Monceaux II differ by about a year (rows 47, 50) |
| *On the Vanity of Idols* compiles the *Octavius* and the *Apology* | Dominant Modern Reconstruction | Harnack's report (row 47) |
| Arnobius c. 295–310 | Widely Accepted | Harnack, Monceaux III, ANF06 notice |
| Arnobius, finer order | Dominant Modern Reconstruction | Step 0 §4 item 2 |
| Commodian used Cyprian and read Tertullian and Minucius | Widely Accepted | Dombart's preface |
| Commodian's span | Contested | Dombart, Harnack, Monceaux, Brewer |
| Lactantius, *Institutes* 304–311 | Widely Accepted | Harnack, Monceaux III |
| *De mortibus* 313–314 or later | Contested | Harnack, Brandt, Seeck |
| Crispus's tutorship, c. 317 | Documented as Jerome's statement; Dominant Modern Reconstruction as a date | Jerome, Harnack |
| *Passion*, 7 March 202 or 203 | Widely Accepted | Harnack, Monceaux I, ANF03 |
| Visions are Perpetua's and Saturus's own | Widely Accepted | Step 0 §4 item 9 |
| Compiler of the *Passion* | Contested | Robinson, Coxe, Harnack, Neumann, Monceaux |
| Teacher-pupil link, Arnobius to Lactantius | Documented as Jerome's statement only | Jerome (row 57) |
| Tertullian trained as an advocate | Inferential-Thin: the census statement alone; no vendored source read says it | `world-census.json` |
| *On the Vanity of Idols* is Cyprian's | Contested | Benson, Monceaux and Bardenhewer defend it; Harnack doubts it (row 47, file lines 18926–18936) |
| Author of the *Appendix* poems and of the *Phoenix* and the Passion poem | Not attested; the files print no author or an uncertain one | `anf04`, `anf07` (an absence, not rated) |
| Internal fracture closing the world | Absence; not rated | Doc_01 §6, Cell 3B |

---

### Thin-evidence map

The claims rated Inferential-Thin or left as absences above are the advocate's training, the authorship of the three verse works, the internal fracture closing the world, and the date of Commodian's *Carmen apologeticum*, which no source on the shelf fixes.

## 9. Search record, field-bibliography sweep, and saturation

**Channels used.** (1) The corpus map and `cic/texts/`: the assigned files, and a full-text search of the whole shelf for the five authors' names. (2) The census entry's `voices` and `sourcing` fields. (3) The Source Readiness Dossier. (4) The scholarship that the vendored Harnack, Monceaux and Schanz–Hosius–Krüger cite for dates. (5) The library's holdings report: 69 files marked "in scope, unread" have a disposition in the Registry; the report marks 2 files "by design" and 95 "out of window" and counts 1,359 with no coverage entry, a library gap that is counted and left. A network check from this build session found archive.org, ccel.org, newadvent.org, tertullian.org, wikisource and gutenberg reachable from this session (ledger entry on the blocked text hosts); the leads in rows 68–74 were not pursued further in this build.

**Three files vendored in this build.** Harnack 1904 (Band 2), Schanz–Hosius–Krüger 1922 (Teil 3) and Brewer 1906, because the dating of every author turns on them. Each was already reachable on archive.org with a public-domain basis, recorded in its file header and in the REGISTRY.

**Not closed.** The V7.4 field-bibliography sweep has not been run against any external instrument. Instruments not reached: the bibliographies of modern work on Tertullian and the Latin apologists after 1930; later handbooks; the *Cambridge History of Early Christian Literature*; the *Dictionary of Christian Biography*. Candidate files assigned to other worlds that hold material on these authors are recorded in the ledger entry on files assigned to other worlds and not used here.

**Cross-world overlaps and candidate pairs.** `PAIRS.yaml` holds no real pairs and this document does not edit it. The candidate pairs are: (a) *On Modesty*, which this world and the New Prophecy world both hold (§7 item 5); (b) the two Cyprian works, which this world and LPC both hold; (c) the *Passion*, which LPC's `world_core` record still assigns to a retired slug (ledger entry on the retired slug). A pairing decision belongs to the project lead.

---

## 10. Open items carried forward

**Carried from Doc_01 and Step 0, and met in this document:**

1. The *Octavius* date, as two Contested ranges, with a `contested_claim` record (§7 item 1).
2. Commodian's date, Contested, with the fifth-century view disclosed (§7 item 1).
3. Minucius Felix's Christological silence, disclosed at the count (§7 item 3).
4. Lactantius's pneumatology, chiliasm, the Book II passage and the dualist passages (§7 item 4).
5. Arnobius's anthropology and the dream-and-bishop story's source (§7 item 2).
6. The seven New Prophecy works and the *Passion* (§7 items 5 and 6).

**New in this document, logged in `Open_Gaps_Tracking.md`:**

7. Doc_01 repeats the Lactantius count that includes the poems (§1), and the finding on the ANF07 "Fragments of Lactantius" needed a correction. Step 0 and Doc_01 are not edited.
8. The saturation statement is not closed (§9).
9. Commodian's Carmen apologeticum has no English text (§1). A Representative's English for it would be rendered from the Latin.
10. Robinson's conclusion on the original of the Passion was not read (§2).

---

## 11. Disposition

Approved to proceed after two review rounds (`Review-Artifacts/Doc02_Round1_Review.md`, Not clear; `Review-Artifacts/Doc02_Round2_Review.md`, Clear). Not Frozen.
