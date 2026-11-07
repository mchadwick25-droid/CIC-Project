# Church Family Tree links, era 2 (P2-L2) — 2026-11-07

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Era 1's audit (`../2026-11-07_links-era-1/`) was the precedent and its wanted-texts list was checked first.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 22 movements, 373 named relationships, raw movement IDs found in three texts.
2. **Draft** (Opus, five groups of four or five movements): `Draft_GroupA.json` to `Draft_GroupE.json`, merged in `Drafting_Record.json`. One link was drafted twice (Ambrose against the imperial church); the merge notes say which draft was kept and why.
3. **Readability pass** (Opus, four batches): `Prose_Pass_1.json` to `Prose_Pass_3.json` for movement text, `Prose_Pass_Notes.json` for link notes. 49 of the 52 changed paragraphs and 44 of the 54 new or rewritten notes scored below Reading Ease 60 before this pass; each was rewritten whole, keeping every fact.
4. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 1 blocking, 5 substantial, 7 minor, no fabrication. The blocking finding: the Pelagian attack on Jerome's houses at Bethlehem was graded Documented, but every source gives it as report.
5. **Revision** (Opus): `Revision_Round1.json`. All 13 findings fixed: 7 links rewritten, 1 added (the desert to the Philokalia of 1782), 5 prose changes. On six findings the reviser improved on the proposed fix and said why. For Aksum the reviser found a named bishop after 451 (Euprepios, in the Book of the Himyarites), so that link stays Documented.
6. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 1 minor. The minor fix (the 1782 Philokalia was one volume) was applied as written.

Two of the three-round cap used.

## Counts

- Links touching an era-2 movement: 109 (52 new, 3 changed, 54 kept). No link retired; every published ID stands.
- Census links in all: 120 before, 172 after. Data release 6 (2026-11-07). Release 5 was the Philocalia ruling (mchadwick25-droid/CIC-Project#1538).
- Grades of the new links: Documented 47, Widely Accepted 3, Inferential-Thin 2.
- Dispositions of the named relationships (drafting): link 174, no-entry 135, qualify 39, out-of-scope 22, remove 1. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 55 paragraphs changed, every one at Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`); 22 sit below FK grade 8, which the scorer reports but does not fail. Every new or rewritten link note also scores Reading Ease 60 or more. Era 1 scored paragraphs only; its notes are logged as an open item.
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines.

## Two-way check

### Prose to links

Every relationship named in an era-2 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it belongs to another era's movement whose own text names it (per-relationship record: `Drafting_Record.json`, `dispositions`). Round 1 found one gap: the desert legacy newly named the Philokalia of 1782 without a link. It was linked in revision. Two summaries still call their movements children of Alexandria (Aksum, the Cyrilline tradition). No link can carry that, because the census has no entry for the fourth- and fifth-century see of Alexandria; logged for Mark.

Sentences qualified or removed (40):

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| desert-monasticism | longDescription | qualify | Theophilus is a person with no entry. Socrates VI.7 and Cassian Conf. X.2 support the split; the timing ('months before', 'by the year's end') did not fit them. |
| desert-monasticism | legacy | qualify | No census entry for Sinai, and no vendored text shows Sinai's monks tracing their practice to the desert. Sinai is dropped from the sentence; the Chalcedonian J… |
| desert-monasticism | legacy | qualify | No vendored text shows the Athonite houses of 963-1300 tracing their practice to the desert, and the Athonite entry does not name it. Replaced with the document… |
| palestinian-ascetic-monasticism-early | legacy | qualify | No vendored text says Jerome modeled Hilarion's Life on the Life of Antony; the clause is removed in prose change 3. The desert-to-Palestine influence itself st… |
| cyrilline-miaphysite-egyptian-tradition | legacy | qualify | No vendored source; the repo names the 1984 and 1989-1990 statements, not the 1970s, and its own review held the 'only words' reading Contested. |
| cappadocian-nicene-pastoral-monastic-tradition | longDescription | qualify | Grain-hoarders have no census entry. 'By name' is not supported; Gregory of Nazianzus, Or. 43, says Basil opened their stores by his word. |
| antiochene-exegetical-christianity-chrysostom-ce | legacy | qualify | Medieval preaching has no entry and no vendored or repo-cited source; the clause is removed. |
| antiochene-exegetical-christianity-chrysostom-ce | legacy | qualify | No source for the genealogy; restated as a likeness. |
| imperial-juridical-christianity | longDescription | qualify | The Eastern churches have no entry here. Augustine was in the city, not in the basilica (Confessions IX.7); 'eyewitness' and 'through the night' are qualified. |
| persian-church-of-the-east-early | longDescription | qualify | No vendored text shows the pre-451 Persian church in Antioch's idiom. Rewritten to what Barhadbeshabba shows; the documented Antiochene tie is antiochene-exeget… |
| hieronymian-ascetic-literary | longDescription | qualify | The crowd has no census entry. Jerome (Ep. 39) reports whispers, not shouts; sentence corrected and split. |
| hieronymian-ascetic-literary | longDescription | qualify | The pope (Innocent) has no entry. His praise is in his letter to John of Jerusalem, not a reply to Eustochium; corrected. |
| hieronymian-ascetic-literary | legacy | qualify | The Old Latin has no entry. Now supported concretely by Gregory the Great's Moralia preface (he uses 'now the new and now the old'). |
| hieronymian-ascetic-literary | legacy | qualify | No census entry; the descent claim has no vendored or repo-cited support. Recast as a comparison. |
| hieronymian-ascetic-literary | legacy | qualify | No single census entry; kept as a plain statement inside the same rewrite. |
| ambrosian-milan-standalone | legacy | qualify | 'Cited for more than a millennium' unsupported; replaced with Theodoret's retelling and Ambrose's own rule. |
| aquileian-christianity | longDescription | qualify | Era-2 open item: 'presided' removed; 'the last two' corrected. |
| aquileian-christianity | longDescription | qualify | 'Earliest' unsupported; recast on Rufinus's own words. |
| aquileian-christianity | why | qualify | Same as the longDescription. |
| aquileian-christianity | legacy | qualify | 'First attested here' contradicted by the Dated Creed of Sirmium (359); narrowed. |
| aquileian-christianity | legacy | qualify | Contradicted by Rufinus's own preface; replaced with Gennadius's judgment. |
| aquileian-christianity | voices | qualify | Era-2 open item: 'preside' also appears in the voices list; fixed. |
| gallic-nicene-episcopate | legacy | remove | A causal claim no source makes; Hilary died long before the Gothic kingdoms. Removed in the rewrite; no link. |
| donatism | relationsSummary | qualify | A comparison, not a contact or influence; no link. Basil, Ep. 188 canon 1 (npnf208 34825-34826 and 34887-34905) reports the old rule of admitting schismatics' b… |
| donatism | longDescription | qualify | Circumcellions have no census movement. The fine is the 412 law, not the 340s; Optatus names them in the 340s. Dated correctly. |
| donatism | longDescription | qualify | No relationship between the Vandal church and the Donatists is claimed or documented; the Vandal-era survival is not in a vendored text. Narrowed. |
| donatism | legacy | qualify | Not documented for the Vandal period; dropped. |
| donatism | legacy | qualify | No vendored text relates the Byzantine African church as a body to the Donatists beyond Gregory's letters to individual bishops; the Byzantine half is carried b… |
| gallic-monastic-ascetic-christianity | relationsSummary | qualify | Existing Inferential-Thin link was stated as fact; Tours is in none of its sources. |
| priscillianist-asceticism | longDescription | qualify | A charge is not a relationship with Manichaeism; no link. The vendored contemporary charge is 'Gnostics' and magic; the Manichaean likening is later (Leo, Braga… |
| priscillianist-asceticism | longDescription | qualify | Ambrose's objection to the execution is not in a vendored text (Letter 24, wanted). His earlier refusal is documented (Chron. II.48) and is carried by a new arg… |
| priscillianist-asceticism | why | qualify | As in the longDescription. |
| priscillianist-asceticism | why | qualify | As in the longDescription; Ambrose dropped from this sentence. |
| pelagianism | legacy | qualify | Misattribution is not a relationship between the movements; no link. 'Only in modern times' corrected. |
| apollinarian-christianity | relationsSummary | qualify | Imperial councils, but no link: Ephesus and Chalcedon do not name the Apollinarians. Qualified to what their texts say. |
| apollinarian-christianity | relationsSummary | qualify | As above. |
| apollinarian-christianity | longDescription | qualify | Rome has no era-2 entry. Council attested in Sozomen VI.25 (Damasus and Peter); year disputed (374 or 377), qualified. |
| apollinarian-christianity | why | qualify | Date qualified; dangling opening phrase fixed. |
| apollinarian-christianity | legacy | qualify | Ephesus: Cyril's letter read in Session I (npnf214 15669-15677, 15737). Not a link, since the council does not name the Apollinarians. |
| apollinarian-christianity | legacy | qualify | Chalcedon's Definition (20280-20282). Not a link, for the same reason. |

### Links to prose

Each new link and where its movements' text names it:

| Link | Type | Grade | Named in |
|---|---|---|---|
| aksumite-christianity-conversion-era--aksumite-christianity | continued as | Documented | aksumite-christianity-conversion-era continuesAs field and legacy ('This became, and remains ...'); aksumite-christianity relationsSummary ('In commun |
| cyrilline-miaphysite-egyptian-tradition--cyrilline-miaphysite-egyptian-christianity | continued as | Documented | cyrilline-miaphysite-egyptian-tradition continuesAs field and longDescription ('Out of that separation came the Coptic Orthodox Church'); legacy ('Thi |
| cyrilline-miaphysite-egyptian-tradition--imperial-juridical-christianity | broke with | Documented | cyrilline-miaphysite-egyptian-tradition longDescription and why (Chalcedon's wording refused, Dioscorus deposed, imperial authority backing the Chalce |
| desert-monasticism--cyrilline-miaphysite-egyptian-tradition | gave rise to | Documented | cyrilline-miaphysite-egyptian-tradition relationsSummary ('Continuation of ... Desert') and legacy ('a monastic life descended unbroken from the deser |
| desert-monasticism--roman-church-gregorian | influenced | Inferential-Thin | desert-monasticism legacy ('by way of Gregory the Great two centuries later, narrowed into the seven deadly sins') |
| imperial-juridical-christianity--jerusalem-liturgical-pilgrimage-christianity | in contact with | Documented | jerusalem-liturgical-pilgrimage-christianity longDescription and why ('Constantine's builders ... raised a great church complex') |
| hieronymian-ascetic-literary--jerusalem-liturgical-pilgrimage-christianity | in contact with | Documented | jerusalem-liturgical-pilgrimage-christianity relationsSummary ('Comparison-point for the Bethlehem Circle') |
| jerusalem-liturgical-pilgrimage-christianity--palestinian-ascetic-monasticism-early | in contact with | Documented | palestinian-ascetic-monasticism-early longDescription ('Pilgrims passed through all of it ... some of them stayed'); jerusalem-liturgical-pilgrimage-c |
| palestinian-ascetic-monasticism-early--hieronymian-ascetic-literary | influenced | Documented | palestinian-ascetic-monasticism-early longDescription ('Jerome, writing from Bethlehem, gave the movement its literature'), why, legacy |
| cappadocian-nicene-pastoral-monastic-tradition--imperial-juridical-christianity | in contact with | Documented | cappadocian longDescription (Gregory of Nazianzus at Constantinople, 381); imperial-juridical relationsSummary (the creed of 381 and the Cappadocian c |
| homoian-arian-christianity--cappadocian-nicene-pastoral-monastic-tradition | argued against | Widely Accepted | cappadocian longDescription (a hostile imperial church under Valens drove Gregory of Nyssa into exile) |
| hieronymian-ascetic-literary--imperial-juridical-christianity | in contact with | Documented | imperial-juridical relationsSummary (Damasus's secretary was Jerome) |
| ambrosian-milan-standalone--imperial-juridical-christianity | argued against | Documented | imperial-juridical longDescription (Thessalonica; Callinicum); ambrosian why and longDescription (Thessalonica) |
| syriac-edessa-nisibis--armenian-christianity-conversion-era | influenced | Documented | armenian relationsSummary (formed via Syriac Edessa); longDescription and why (catechized at first in Syriac) |
| cappadocian-nicene-pastoral-monastic-tradition--armenian-christianity-conversion-era | influenced | Widely Accepted | armenian relationsSummary (formed via Cappadocia); longDescription and why (catechized at first in Greek) |
| armenian-christianity-conversion-era--armenian-christianity-after-avarayr | continued as | Documented | armenian legacy (the Armenian Apostolic Church as the living descendant) |
| persian-church-of-the-east-early--the-church-of-the-east-under-persia | continued as | Documented | persian legacy (it became the Church of the East); the-church-of-the-east-under-persia longDescription (the 424 synod) |
| antiochene-exegetical-christianity-chrysostom-ce--alexandria-catechetical | argued against | Documented | antiochene relationsSummary and why (Antioch's reading set against Alexandria's allegory) |
| antiochene-exegetical-christianity-chrysostom-ce--imperial-juridical-christianity | in contact with | Documented | antiochene longDescription and why (taken to Constantinople to preach to the imperial court) |
| imperial-juridical-christianity--antiochene-exegetical-christianity-chrysostom-ce | argued against | Documented | antiochene longDescription and why (preaching to the court led to his death in exile) |
| byzantine-imperial-church-justinianic--antiochene-exegetical-christianity-chrysostom-ce | argued against | Documented | antiochene legacy (Theodore condemned at Constantinople in 553); byzantine-imperial-church-justinianic why (the 553 council) |
| antiochene-exegetical-christianity-chrysostom-ce--the-church-of-the-east-under-persia | influenced | Documented | antiochene legacy (Theodore's work preserved in Syriac by the Church of the East) |
| antiochene-exegetical-christianity-chrysostom-ce--the-reformed-cities-zurich-and-geneva | influenced | Documented | antiochene legacy (Reformed preachers claimed Chrysostom) |
| antiochene-exegetical-christianity-chrysostom-ce--lutheran-wittenberg-and-its-congregations | influenced | Documented | antiochene legacy (Lutheran preachers claimed Chrysostom) |
| aquileian-christianity--hieronymian-ascetic-literary--2 | broke with | Documented | hieronymian relationsSummary ('fractured over with Rufinus'); aquileian relationsSummary, longDescription and why (the quarrel) |
| aquileian-christianity--homoian-arian-christianity | argued against | Documented | aquileian longDescription ('a council at Aquileia that deposed ... Homoian bishops') |
| ambrosian-milan-standalone--homoian-arian-christianity | argued against | Documented | aquileian longDescription (Ambrose at the council that deposed the Homoian bishops); the ambrosian text names the basilica conflict with Justina's cou |
| ambrosian-milan-standalone--latin-pastoral-congregational-christianity | influenced | Documented | ambrosian longDescription and legacy (Augustine) |
| hieronymian-ascetic-literary--latin-pastoral-congregational-christianity | in contact with | Documented | hieronymian longDescription (Augustine wrote across the sea to warn Jerome); hieronymian legacy |
| latin-pastoral-congregational-christianity--hieronymian-ascetic-literary | argued against | Documented | hieronymian legacy (Augustine's resistance to the new translation) |
| pelagianism--hieronymian-ascetic-literary | argued against | Inferential-Thin | hieronymian longDescription ('an attack tied to the Pelagian dispute set fire to the Bethlehem monasteries') |
| hieronymian-ascetic-literary--the-tridentine-church | influenced | Widely Accepted | hieronymian legacy ('the text the Council of Trent declared authentic in 1546') |
| palestinian-church-pre-constantinian--aquileian-christianity | influenced | Documented | aquileian legacy (Rufinus's translations: Eusebius) |
| cappadocian-nicene-pastoral-monastic-tradition--aquileian-christianity | influenced | Documented | aquileian legacy (Rufinus's translations: Basil) |
| apocryphal-and-pseudepigraphal-literature--aquileian-christianity | influenced | Documented | aquileian legacy (Rufinus's translations: the Clementine Recognitions) |
| gallic-nicene-episcopate--latin-pastoral-congregational-christianity | influenced | Documented | gallic legacy (Augustine worked with De Trinitate in view) |
| gallic-nicene-episcopate--merovingian-gallic-christianity | influenced | Documented | gallic legacy ('the Frankish conversion two centuries on was to a Nicene church') |
| donatism--latin-pastoral-congregational-christianity--2 | broke with | Documented | donatism relationsSummary ('it split from over the same persecution'); latin-pastoral relationsSummary ('a rival Donatist church stood in the same tow |
| donatism--latin-pastoral-congregational-christianity--3 | influenced | Documented | donatism legacy (Tyconius's book crossed over and shaped how Augustine learned to read Scripture) |
| byzantine-imperial-church-justinianic--donatism | argued against | Documented | donatism longDescription ('survived under ... Byzantine rule ... still legislated against') and legacy ('Byzantine rulers inherited the same divided t |
| roman-church-gregorian--donatism | argued against | Documented | donatism longDescription (Gregory's letters pressing for an inquiry into Donatist rebaptism in Numidia) and legacy |
| gallic-monastic-ascetic-christianity--latin-pastoral-congregational-christianity | argued against | Documented | gallic longDescription ('the monks of Marseilles who resisted Augustine's late teaching on grace') and legacy ('the Gallic objection to Augustine on g |
| latin-pastoral-congregational-christianity--gallic-monastic-ascetic-christianity | argued against | Documented | gallic longDescription ('Augustine answered them in two treatises, after a third one - addressed to a different monastery, in Africa - had first provo |
| pelagianism--latin-pastoral-congregational-christianity | argued against | Documented | pelagianism relationsSummary ('Augustine's great controversy-partner') and longDescription (Caelestius and Julian pushed the argument; Augustine fough |
| imperial-juridical-christianity--priscillianist-asceticism | argued against | Documented | priscillianist longDescription and why (the case carried to the imperial court; Maximus had Priscillian executed at Trier) |
| ambrosian-milan-standalone--priscillianist-asceticism | argued against | Documented | priscillianist longDescription and why (Ambrose of Milan named); the census said he objected to the execution, which no vendored text shows (prose cha |
| gallic-monastic-ascetic-christianity--imperial-juridical-christianity | in contact with | Documented | priscillianist longDescription and why ('Martin of Tours ... objected to churchmen taking a doctrinal quarrel to an executioner') |
| homoian-arian-christianity--gothic-and-vandal-homoian-christianity | gave rise to | Documented | homoian longDescription and why (Ulfila's mission; Goths, Vandals and Lombards in this form; Homoian kingdoms). The Gothic entry's own summary also na |
| imperial-juridical-christianity--homoian-arian-christianity--2 | influenced | Documented | homoian relationsSummary ('the imperial church itself'), longDescription and why (backed by Constantius II and Valens, adopted at the councils of 359  |
| hieronymian-ascetic-literary--homoian-arian-christianity | argued against | Documented | homoian longDescription and why (Jerome's line that the world groaned to find itself Arian) |
| antiochene-exegetical-christianity-chrysostom-ce--anomoean-eunomian-christianity | argued against | Documented | anomoean longDescription and why (Aetius, a deacon at Antioch). Diodore is named in the Antiochene entry's own text as Chrysostom's teacher. |
| desert-monasticism--the-kollyvades-and-greek-renewal | influenced | Documented | desert-monasticism legacy (the Philokalia of 1782, added in revision round 1 as review finding R1-06) |

The three changed links (`anomoean-eunomian-christianity--homoian-arian-christianity`, `imperial-juridical-christianity--pneumatomachian-current`, `cappadocian-nicene-pastoral-monastic-tradition--apollinarian-christianity`) are named in the texts that named them before. The last carried a quote filed under the wrong letter of Gregory of Nazianzus (Letter 202 given as Letter 101); its sources now name both letters correctly.

## Open items

Closed in this pass, in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`:
- "Two movement texts repeat corrected claims": the Aquileia half. Ambrose no longer "presided" at Aquileia in the description or the voices.
- "Raw movement IDs in four later movements' text": the three era-2 movements. `roman-church-gregorian` waits for era 3.

Logged in Open-Gaps (2026-11-07). For Mark, all census-structure or mapping questions; none blocks this release:
- No entry for the church of Alexandria, 4th-5th century.
- Two Egyptian Miaphysite entries from the same year.
- Well-known facts with no vendored source (does "qualify" reach facts that are not relationships?).
- Which entry owns an emperor's act against the Nicenes, 337-378.
- The two early Persian entries overlap.
- Ambrose's Milan and the imperial church overlap.
- Augustine has no movement of his own.

For entry owners and later passes:
- The Homoian and Gothic Homoian entries overlap.
- Era-2 text outside the links pass (eight small items, listed there).
- A Gallic source record is out of date.
- Era 1's link notes were never scored for reading level.
- "Direct heir of Desert Monasticism" (era 3).

Notes:
- Imperial sponsorship of a creed (Constantius's councils of 359-360) is typed "influenced". Both reviewers held that it fits the type as written, so no method change was raised.
- NPNF 11 renders Sulpicius, Chronicle II.47 "Abilensi" as "Arles"; the Latin and the census say Ávila. Never quote that NPNF line.
- Several quotes keep OCR errors exactly as the files print them; each is noted in that link's `drafter_flags` in `Drafting_Record.json`.

## Wanted texts

- A numismatic catalogue or a repo-cited study of Aksumite coinage (e.g. Munro-Hay, named but not acquired in Build/worlds/_cross-world/dossiers/aksumite-christianity_Source_Readiness_Dossier.md), to document Ezana's conversion and the cross replacing the disc and crescent
- A readable edition of Cyril of Scythopolis, Life of Euthymius (ch. 6-8, Euthymius's years in the laura of Pharan). The vendored Cotelier 1681 OCR names Pharan (line 27730) but is too corrupt to quote. A clean text would show a named monk passing from Pharan into the Judean desert foundations and could lift this link.
- A repo-cited modern study of how the eight thoughts became Gregory's seven sins (none found in records/ or Build/); with one, this could be graded Widely Accepted.
- A source for Egeria's date in the early 380s beyond the editors' own argument
- A source for the 1973 and later Oriental Orthodox joint declarations (texts of the 1984 Syriac Orthodox-Catholic declaration and the 1989-1990 agreed statements), to cite the Cyrilline legacy's dialogue sentence directly
- A source for the Ethiopian church's own patriarchate in the twentieth century (1959), if the Aksum legacy's closing sentence is to stay sourced
- Littmann, Deutsche Aksum-Expedition IV (1913; verified but not vendored per the Aksum dossier), for Ezana's own inscriptions
- Rufinus, Church History X.9-10 in English, or a clean read of the vendored Schwartz-Mommsen Latin (lines 27308-27384), as the earliest Frumentius account
- A repo-cited modern study (e.g. Garsoian) on the Armenian church's tie to Caesarea
- A repo-cited modern study of Valens's church policy, to replace the 1894 editors as the secondary for the Homoian reading
- A source for the epithet 'Queen of Translations' for the Armenian Bible (the census uses it; no vendored or repo-cited text does)
- A vendored Syriac-only work of Theodore (e.g. Mingana's Catechetical Homilies, 1932-33, if public domain) to document 'survives only in Syriac' directly
- Agathangelos, History of the Armenians, and Faustus of Byzantium, in Langlois, Collection des historiens de l'Arménie, tome I (1867): verified on archive.org by the Library thread, not vendored
- Calvin's preface to the French edition of Chrysostom's homilies (Calvini Opera 9), to document the claim about expository preaching
- Faustus of Byzantium (Buzand), History III-IV, and Agathangelos, History of the Armenians (Langlois tome I, 1867), which report the consecration of Gregory and his successors at Caesarea; Langlois tome II's note cites Faustus III.12 and 16, but tome I is not vendored
- Frances Young, Biblical Exegesis and the Formation of Christian Culture (1997), actually read, for the modern dispute over how sharp the Antioch-Alexandria contrast was
- Gregory of Nyssa's own letters on his deposition and return (Epp. 6, 18, 22 in later numbering), in a vendored edition, to give his side
- Theodore of Mopsuestia's surviving comments against allegory (e.g. the Commentary on Galatians 4:24, Swete 1880) in a vendored edition
- Rufinus's preface to his Latin translation of Basil's Rule or homilies, to document the Basil translations from Rufinus's own side (now rests on Gennadius, c. 480)
- The Paris synod letter of c. 360 (Hilary, Collectanea antiariana A I) located and quoted in the vendored CSEL 65 Latin, or an English translation, for the Gallic repudiation of Ariminum at Paris
- Hilary, Contra Auxentium in English, or a located passage in the vendored PL 10 (from line 48549), for Hilary's attack on Auxentius
- The Homoian record of the Council of Aquileia (Scholia Arriana / Palladius's dissertation) in a vendored edition, so the 381 links have the condemned party's side
- A repo-cited modern work on the Vulgate's reception, and on Renaissance and Reformation scholars' appeal to Jerome's Hebrew principle, if the stronger 'ancestor of every back-to-the-sources movement' claim is to return
- A repo-cited modern study of the 416 attack on the Bethlehem monasteries and its attribution to Pelagius's followers, to support or lower the Documented grade
- Jerome's Commentary on Ezekiel, preface to Book I ('the scorpion lies buried'), for Jerome's last word on Rufinus
- Ambrose, Letter 24 (Maurist 30), on his second embassy to Maximus, where he refused communion with the bishops who sought the death of heretics: would let the priscillianist text say again that Ambrose objected to the execution
- The Manichaean charge at Priscillian's trial in a contemporary text (e.g. Priscillian's own Würzburg Tractates, Schepss CSEL 18, which deny it): would let the census say he was accused of Manichaeism, not only likened to it later
- Gregory the Great's Register, Books I-VII, in the Ewald-Hartmann Latin (only Books VIII-XIV are vendored), to check the NPNF numbering of the Donatist letters
- A clean text of the Gesta Collationis Carthaginiensis (411), to confirm the 279 and 286 bishop counts (the PL 11 OCR shows 279 only)
- A legible edition of the Passio Marculi, to confirm the parade through towns and the cliff at Nova Petra
- A source for Lérins as a monastery today, and for Martin as patron saint of France with thousands of churches, if those legacy lines are to stay
- A text of Thomas Aquinas on grace (e.g. Summa Theologiae I-II, qq. 109-114), if the Pelagian legacy sentence is to keep naming him
- Cassian, Conference XIII in a vendored edition checked for the Marseilles position in its own words
- Agnellus, Liber Pontificalis Ecclesiae Ravennatis (on Theoderic's building of Sant'Apollinare Nuovo and the Arian Baptistery), to restore 'built for Homoian worship'
- A repo-cited modern work on the Codex Argenteus and Theoderic's court, if that attribution is to come back
- A repo-cited modern work stating that the Gothic Bible is the earliest substantial text in a Germanic language
- A repo-cited modern work on the reception of Basil's argument from prayer and baptism (and of Gregory's 'what is not assumed is not healed'), if those legacy claims are to stand
- A repo-cited modern work on the Gothic Homoian church's continuity from Ulfila to the successor kingdoms (e.g. a study of the Gothic conversion), which would let the 'continued as' link rest on a consensus reading as well as primaries
- A clean Latin text of the Collatio cum Maximino (the PL 42 OCR mangles Maximinus's answer)
- A vendored text or repo-cited study on the Macedonius attribution, if the old 'evidence later writers found thin' is to come back
