# Census lineage rigor pass — 2026-11-06

Decision: `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`, entry of 2026-11-06.

**Rounds.** Sonnet drafted by era (six groups) against `Drafting_Brief.md`. A script checked every quote verbatim against its vendored file and lines (now enforced by `tools/validate-census.mjs`). Opus round 1 (`Opus_Review_Round1.json`): revise — 2 blocking, 10 substantial, 8 minor, no fabrication. Sonnet revised. Opus round 2, targeted recheck (`Opus_Review_Round2_TargetedRecheck.json`): pass, every round-1 blocking and substantial finding resolved; its seven note rewrites and three minor fixes applied. Two rounds of the three-round cap used.

**Result.** 69 links became 86: 7 removed as unsupported, 22 added. Every link has a type from the six, a grade from the five, sources with a vendored locus and verbatim quote where primary, citation specificity and verification state. Per-link reasons: `Drafting_Record.json`.

**Open after the pass (movement text, not links; owner: whoever next edits these census entries):**
- `aquileian-christianity` says Ambrose "presided" over the Council of Aquileia (381) in two places. The Acts do not say so; the link note was corrected.
- `roman-church-third-century` has Callistus leading arguments over "whether the gravely lapsed could ever be restored". Hippolytus's charge concerned penance for other sins; the lapsed crisis follows Decius (250). The link note was corrected.

**Ruling kept from the drafts (old #64, Tertullian → Latin Apologists).** A member-to-container "influenced" link is kept where the member is a separate census entry and the container is a different entry whose own texts name the member (Lactantius naming Tertullian). Old #42 (house churches → apologists) was removed because it asserted identity ("the same Christians"), not influence, and had no text naming the relation.

**Wanted texts (would let a link be graded higher):**
- 1906 US Religious Census listing
- 1906 US Religious Census listing of the Churches of Christ, and David Lipscomb's letter to the Census Bureau
- A Coptic or miaphysite source on the Egyptian side of the rupture, such as Theopistus's History of Dioscorus (vendored in French, not yet read for this link)
- A Donatist-authored text (or Petilian's letter in a clean edition) directed at the Catholic church by name; Contra litteras Petiliani is vendored but its OCR is too degraded to quote
- A Homoian-side account of the break, so the rupture is recorded from both sides (none is vendored)
- A Waldensian or inquisitorial text from c. 1300-1400 placing a named community in the Alpine valleys
- A Wittenberg-side text of the colloquy, such as the Marburg Articles or Luther's own report, to show the meeting from both sides
- A clean edition of the Constitutions with Arundel's papal legation named
- A clean text of the Vita Caesarii or of Fortunatus's verse; the vendored OCR is rough.
- A critical edition of that commentary that shows Jerome's recension
- A critical text of Codex Theodosianus 16.5.11 (the Latin Library transcription is unverified against Mommsen-Meyer)
- A critical text of Codex Theodosianus 16.5.14
- A critical text of the Codex Theodosianus (Mommsen-Meyer) to confirm the two law quotations; the Latin Library transcription is marked as unverified against a critical edition
- A dated text from the 190s or 200s that links the Roman congregation of Victor's day to Zephyrinus's, such as Eusebius HE V.28, read in full
- A dated text naming people who carried Christianity from Antioch, Asia Minor or Rome to Edessa (none known)
- A dated text placing the Protevangelium of James or the Infancy Gospel of Thomas in a named household-church community
- A dated text showing Greek apologists leaving the household-church communities, which would make 'gave rise to' true
- A dated text that sets Paul of Samosata and the modalists in contact, such as Eusebius HE VII.30 read for any mention of Sabellius
- A legible text of Basil's Against Eunomius (the vendored PG 29 volume is too garbled to quote)
- A legible text of Hilary's Contra Auxentium and De Trinitate to quote his answers to the Homoian case directly
- A modern account of the schism and the debate over its dating (not cited anywhere in the repo)
- A repo-cited modern secondary confirming that Benedict's Collationes and Instituta are Cassian's works (none found); Chadwick, John Cassian (1950) is named in the Gallic records but was never read.
- A repo-cited modern secondary on Lérins and the Frankish episcopate (Mathisen is named in the Gallic records but its full text was never read there).
- A repo-cited modern secondary on the Rule's sources (none found); Gasquet (1909 introduction) and Hunter Blair's glosses are the only reading offered.
- A repo-cited secondary on Byzantine monasticism and its Egyptian roots (none found in records/, Build/ or cic/).
- A repo-cited secondary work on how the Latin apologists inherit the Greek apologists' arguments
- A repo-cited secondary work that states the 'Lucian origin of Antiochene exegesis' claim and its critics
- A secondary work on Lactantius and Constantine that the repo already cites
- A secondary work on the Danubian Church the repo already cites
- A secondary work on the Jerusalem church's continuity across 312-326 that the repo already cites
- A source for the claim that some of Origen's works survive only in Rufinus's Latin
- A text by Jerome or Rufinus that names the Aquileian ascetic company itself
- A text listing the bishops of Jerusalem from Alexander to Macarius
- A text that ties Gregory's own monastery on the Caelian to Benedict's Rule
- A vendored Alexandrian text that names Justin and uses his 'seeds of the Word' argument; I found none in the vendored English (Justin is named only in editors' notes in ANF02 and ANF04)
- A vendored text placing Ursacius and Valens at the head of the Homoian party (Hilary, Fragmenta historica, in readable text)
- AME Zion origins (1821), if the old note's claim is to be kept
- Aladura founding records (Cherubim and Seraphim 1925; CAC 1930)
- Antony's letters in a vendored edition, to check Rubenson's Origenist reading against the text
- Any dated text from before 190 describing the Christian community of Alexandria
- Any text naming Chariton and the laura of Pharan.
- Arundel's Constitutions in the original Latin (Wilkins, Concilia, vol. 3) to replace Foxe's English version
- Cameron, The Reformation of the Heretics, for the continuity argument
- Cerularius's synodal edict against the legates (Will, Acta et scripta de controversiis ecclesiae graecae et latinae, 1861)
- Constantine's Oration to the Assembly of the Saints, to test for use of Lactantius
- Constantine's letters themselves, quoted directly: the Latin appendix of ten documents is vendored (optatus_appendix-decem-monumentorum-lat_ziwsa1893-csel26-tei.txt) but its line-end markup makes clean quotation unsafe
- Critical edition of the Cursus Scottorum tract itself.
- Critical text of the Cursus Scottorum tract.
- Cyprian, Epistle 55 (to Antonianus), read for the Roman schism of 251; the Latin text is vendored (cyprian_epistulae-lat_hartel1871-csel3-tei.txt) but I did not read it
- Cyril of Scythopolis, Life of Chariton and Lives of Euthymius and Sabas, in a readable text (the vendored Vita Euthymii is unusable two-column OCR).
- Cyril of Scythopolis, Life of Chariton, or another early account of Palestinian monasticism, to test Jerome's claim that Hilarion was first.
- Diodore of Tarsus, Theodore of Mopsuestia or Chrysostom naming Lucian as a teacher of method
- Early Pentecostal press reports from Africa
- Eusebius, Martyrs of Palestine, if it is to be cited for his own experience of the persecution (not vendored)
- Fosdick, 'Shall the Fundamentalists Win?' (21 May 1922)
- Gregory's own letter sending the mission (Registrum VI.52 is vendored in the Turchi edition, but a line number is printed inside the sentence, so it was not quoted)
- Hilary, Ad Constantium II
- Hilary, Liber contra Constantium imperatorem, in a legible text (vendored PL 10 OCR is poor)
- Holiness texts naming Wesley, such as Phoebe Palmer's The Way of Holiness (1843) and the Guide to Holiness, which would allow Documented
- Holiness-movement texts of the 1890s-1900s naming the move to Pentecostal teaching
- Hus's own De ecclesia text and Wyclif's De ecclesia side by side (Loserth, Wiclif and Hus), to quote the parallel paragraphs
- Jerome's own note on his revision of Victorinus's Commentary on the Apocalypse
- Latin apologists naming Greek apologetic works: Minucius Felix or Tertullian naming Aristides, Athenagoras or Theophilus (none found)
- Luther's own writing against Zwingli on the Supper in a quotable edition (the 1528 Confession concerning Christ's Supper), to show the arrow from Luther himself
- Machen, Christianity and Liberalism (1923)
- Methodius, On the Resurrection, in a text that names Origen directly (Epiphanius and Photius preserve extracts)
- Modern secondary on Gaul-to-Ireland monastic links (none found in the repo).
- Modern secondary survey of Irish monasticism and its Egyptian models (none found in the repo).
- Narsai's own homilies or an East Syrian source dated close to 489
- Raboteau passage on the Baptist roots, with page
- Rufinus's prefaces to the Origen translations made at Aquileia (Genesis to Joshua homilies, Romans commentary), not vendored in this volume
- Schleitheim Articles (1527) and Menno Simons passages naming Luther or the Lutherans, if a second Anabaptist wing's text is wanted
- Silver Bluff founding date evidence (the c. 1773-75 date is not in the vendored lines)
- Statutes of the School of Nisibis (vendored, Syriac with Italian) read for its own account of its origin
- Sulpicius Severus, Chronica 2.39-45, in a readable text (the vendored CSEL OCR is too rough to quote)
- Texts of Theodore the Studite (Letters, Catechetical Orations) or Studite rules naming the desert fathers; not in cic/texts/ as far as I found.
- The 377 Roman synod's own record of its condemnation of Apollinarius (not vendored)
- The Apostolic Faith (Los Angeles, 1906-1908)
- The Auburn Affirmation (9 January 1924)
- The Chanforan decisions of 1532 in a critical edition (they survive only in later copies)
- The Christian Church (Disciples of Christ) 'Design' of 1968 and the Independent churches' yearbook records
- The Doctrinal Deliverance of 1910 (Presbyterian General Assembly)
- The Gospel Advocate and Firm Foundation for the wing's own account
- The Greek or Latin text of Gregory of Nazianzus, Oration 27, with the opening sentences naming the Eunomians
- The letter of the Council of Paris (361) to the Eastern bishops, Feder CSEL 65 Fragment I (OCR too poor to quote)
- Timothy Aelurus's own Refutation of Chalcedon in German or English: the vendored file is Classical Armenian OCR and I cannot quote it safely
- William J. Seymour, The Doctrines and Discipline of the Azusa Street Apostolic Faith Mission (1915)
- Zionist/ZCC early records and Zion City links

**Links considered and not proposed:**
- **Church of the East and the imperial church after Ephesus (431).** No vendored text I could quote shows a dated relationship between the two after 431. The Synodicon orientale (Chabot, French) has later synods, but the 544 note that the 'Nestorians accepted Chalcedon in so far as it condemned Eutyches' is Chabot's 1902 editorial note, and the letter of Gewargis (c. 679) attacking Cyril and Justinian is too late for the imperial entries in the census. The 410 meeting is proposed instead.
- **Lollards against the late-medieval papal church (the Lollard side).** The vendored Lollard-authored texts are OCR-degraded (Twelve Conclusions in Fasciculi Zizaniorum; Todd's Apology for Lollard Doctrines), so no verbatim quote is safe.
- **Anabaptists against Zurich (Hubmaier / Grebel).** The vendored Hubmaier Gesprech (1526) is poor OCR and its own header says nothing is quotable until read on the page images. Zwingli quotes an attack attributed (not certainly) to Grebel.
- **Wittenberg and Zurich at Marburg: rupture recorded by both sides.** No Wittenberg-side Marburg text is vendored (the Marburg Articles, Luther's report). The contact link is Documented; a 'broke with' link needs both sides.
- **Timothy Aelurus against Chalcedon, from the Egyptian side.** The only vendored full text is Classical Armenian OCR (Ter-Mekerttschian 1908); I could not check an Armenian quotation.
- **Hussites influenced by Lollardy / Wyclif.** Out of the assigned scope and it depends on whether Wyclif belongs to the Lollardy entry; no link drafted.
- **Donatism and the Conference of Carthage (411) as a separate 'in contact with' link.** Omitted as redundant with the 'argued against' link, which already cites the Conference through Augustine.
