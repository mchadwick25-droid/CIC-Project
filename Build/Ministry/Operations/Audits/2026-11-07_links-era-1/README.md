# Church Family Tree links, era 1 (P2-L1) — 2026-11-07

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 21 movements, 190 named relationships.
2. **Draft** (Opus, five groups of four or five movements): `Draft_GroupA.json` to `Draft_GroupE.json`, merged in `Drafting_Record.json`. Two links were drafted twice (Tertullian against Marcion; the New Prophecy's influence on Tertullian); the merge notes say which draft was kept and why.
3. **Readability pass** (Opus, three batches): `Prose_Pass_0.json` to `Prose_Pass_3.json`. Most changed paragraphs scored below Reading Ease 60 before this pass, many of them long before it; each was rewritten whole, keeping every fact.
4. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 1 blocking, 4 substantial, 10 minor, no fabrication. The blocking finding was a wrong year (519 for 522) in a Syriac link note.
5. **Revision** (Opus): `Revision_Round1.json`, plus `Revision_Round1_Followup.json` for the Syriac Orthodox descent the reviser left open. All 15 findings fixed; 2 links added, 13 rewritten.
6. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 6 minor. The six minor fixes were applied as written (two quotes made whole, one note made self-standing, two prose wordings, and the open items logged).

Two of the three-round cap used.

## Counts

- Links touching an era-1 movement: 64 (34 new, 1 changed, 29 kept). No link retired; every published ID stands.
- Census links in all: 86 before, 120 after. Data release 4 (2026-11-07).
- Grades of the new links: Documented 33, Inferential-Thin 1.
- Dispositions of the named relationships (drafting): qualify 29, out-of-scope 39, no-entry 30, link 97, remove 3. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 45 paragraphs changed. Every one scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`). 33 sit below FK grade 8, which the scorer reports but does not fail: the names these paragraphs carry pull Reading Ease under 60 as soon as sentences lengthen. Round 1 asked for the choppiest ones to be re-joined, and they were.
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines.

## Two-way check

### Prose to links

Every relationship named in an era-1 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement (per-relationship record: `Drafting_Record.json`, `dispositions`). Round 1 found six gaps; all were closed in revision (Justin against Marcion and the Valentinians named in the Greek apologists' text; Jerome and the Banquet linked; the Syriac "parent" wording; Eusebius on the Ebionites linked; Tertullian's Augustine line softened to what the source shows), except the Irenaeus no-entry gap, which is logged (Open-Gaps, "Irenaeus has no movement of his own", 2026-11-07).

Sentences qualified or removed (32):

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| post-apostolic-house-church | relationsSummary | qualify | Only one documented line runs out of this movement (to roman-church-third-century); parenthood of most later movements is not shown by any vendored text. Rewritten as wha… |
| post-apostolic-house-church | legacy | qualify | Same as the relationsSummary: stated as descent, not documented beyond Rome. Rewritten as a claim the traditions make; FRE 51.7 before, 53.6 after. |
| greek-apologists-second-century | relationsSummary | qualify | Overlap/identity is not one of the six link types (link removed 2026-11-06 for asserting identity). Rewritten to the documented overlap (Justin, Theophilus, Melito; sourc… |
| greek-apologists-second-century | longDescription | qualify | Greek philosophy is no movement. 'Most of them' is not supported (Diognetus 8 and Tatian are hostile); narrowed to 'several of them, Justin above all'. FRE 35.1 before, 4… |
| greek-apologists-second-century | legacy | qualify | The movement link exists (Clement praising Tatian, Documented). The Justin-specific line of descent is not in the vendored texts, so the sentence now states the parallel … |
| latin-apologists | longDescription | qualify | Diocletian's government is no movement. Pupil: DVI 80, 'a disciple of Arnobius' (npnf203 41034). Teaching at Nicomedia when the church was destroyed: Div. inst. V.2.2. 'L… |
| alexandria-catechetical | legacy | qualify | The flat claim contradicts the existing Contested link and the desert entry's own summary. Rewritten to state the dispute (Rubenson's reading vs. Athanasius, Vita Antonii… |
| anatolian-church-third-century | relationsSummary | qualify | Basil says only that Macrina taught him Gregory's words, kept in memory (npnf208 37062-37065); no vendored text says she was formed by his disciples. The precedent half i… |
| anatolian-church-third-century | legacy | qualify | No vendored text shows Ambrose using the Banquet. 'Foundation' and 'began there' are contradicted by earlier vendored works: Tertullian, On the Veiling of Virgins (anf04 … |
| anatolian-church-third-century | legacy | qualify | Jerome names the Banquet in a catalogue (DVI 83, npnf203 41096-41099); no vendored text shows him using it on virginity (his Methodius references in npnf206 9759, 16539 c… |
| anatolian-church-third-century | legacy | qualify | No vendored text shows Gregory of Nyssa using the Banquet; the one editor's mention (npnf205 1174) concerns resurrection, not virginity. |
| apocryphal-and-pseudepigraphal-literature | relationsSummary | qualify | 'Every' cannot be shown, and 'entry' is internal language. One reader is now documented by a new link (Origen, Comm. Matt. X.17, anf09 30601-30607). |
| apocryphal-and-pseudepigraphal-literature | longDescription | qualify | Judaism is not a movement. For the Testaments the Jewish origin is disputed: the ANF08 editor reads the author as a Christian (lines 632-655), and the project's own river… |
| apocryphal-and-pseudepigraphal-literature | longDescription | qualify | The sentence dates a text; it does not relate the Carolingian reform movement to this one, so no link. 'Carolingian' is in no vendored or repo-cited source; ANF08 (35995-… |
| apocryphal-and-pseudepigraphal-literature | why | qualify | As the longDescription item: the example swapped for the Life of Adam and Eve. |
| apocryphal-and-pseudepigraphal-literature | legacy | qualify | No movement party. The deaths are in the vendored Acts (anf08 47557-47561 Peter head down; 48752 Philip by the ankles); the medieval reception is not in any vendored text… |
| apocryphal-and-pseudepigraphal-literature | legacy | qualify | Judaism is not a movement. Narrowed to what the collection shows; the wider claim has no vendored or repo-cited source. |
| syriac-edessa-nisibis | relationsSummary | qualify | Transmission route, not a movement. As written it makes this 200-410 community the channel; the Arabic translations came centuries later from its heirs. Rewritten. |
| bardaisanite-current | longDescription | qualify | Ephraim complained of sweetened poison, not of better hymns, and his earliest hymns predate the controversy. Rewritten; the hymn contest itself is carried by the new infl… |
| roman-church-third-century | why | qualify | Open item from the 2026-11-06 pass. Hippolytus's charge was about forgiving grave sin after baptism (Ref. IX.7, anf05 lines 13873-13875); 'the lapsed' are those who sacri… |
| roman-church-third-century | legacy | remove | The Donatist dispute (from 311) turned on whether a bishop ordained by a traditor could give valid sacraments (donatism longDescription), not on restoring the lapsed; and… |
| montanism-the-new-prophecy | legacy | qualify | Inventory said no census entry; Pentecostal entries exist (azusa-street-and-early-pentecostalism, charismatic-renewal-and-the-jesus-movement). No link: the text itself de… |
| novatianism | relationsSummary | remove | Internal cataloguing note, not a historical claim; no relationship between the two is claimed or documented here. |
| latin-pastoral-congregational-christianity | relationsSummary | remove | 'Confirmed distinct from' is a cataloguing decision about entries, not a historical relationship. |
| latin-pastoral-congregational-christianity | legacy | qualify | No census entry. No vendored text shows Latin Christianity ending 'altogether' with the conquest; softened to a slow end afterwards, as latin-africa-under-byzantium itsel… |
| valentinian-and-other-gnostic-christianities | longDescription | qualify | Adv. Val. 4 (anf03 43109-43114): Valentinus 'had expected to become a bishop' and broke with the church when another won it on a confessor's claim. 'Nearly elected' and '… |
| antiochene-church-third-century | longDescription | qualify | Not a movement relationship, but the attribution overstates. The synodal letter says only that Paul preferred the title ducenarius (HE VII.30.8, npnf201 42104-42105). The… |
| antiochene-church-third-century | why | qualify | Nicaea is a council, not a movement. The only vendored witness is Athanasius, On the Councils 43-45 (npnf204 58972-59060), written c. 359, reporting what bishops wary of … |
| antiochene-church-third-century | legacy | qualify | Same evidence as the why-field sentence. The second half (later unease) is supported by On the Councils 43; the first (contention at Nicaea) is not, so it goes. |
| antiochene-church-third-century | legacy | qualify | The existing link is Inferential-Thin: no vendored source ties Lucian to Diodore, Theodore or Chrysostom, and no repo-cited secondary states the 'usually traced' consensu… |
| danubian-latin-christianity | legacy | qualify | The reading did survive Jerome's revision: the received text says what recurs in the bowls 'is not said as if it occurred twice' (anf07, Victorinus on Apoc. 8). But it ca… |
| danubian-latin-christianity | legacy | qualify | Augustine describes Tyconius's rule of recapitulation (De doctrina III.36, npnf102 53403) but names no debt to Victorinus, so no influenced link. The prose now says they … |

### Links to prose

Every link touching an era-1 movement, and where its relationship is named:

| Link | Type | Grade | Status | Named in |
|---|---|---|---|---|
| `alexandria-catechetical--desert-monasticism` | gave rise to | Contested | kept | alexandria relationsSummary and legacy (legacy rewritten in prose change to match the Contested grade); desert-monasticism relationsSummary |
| `alexandria-catechetical--hieronymian-ascetic-literary` | influenced | Documented | kept | alexandria relationsSummary ('scholarship parent of the Bethlehem Circle') and legacy (Jerome read him); hieronymian relationsSummary ('Descends scripturally from Alexand… |
| `syriac-edessa-nisibis--the-church-of-the-east-under-persia` | influenced | Documented | kept | Named in both: syriac-edessa-nisibis relationsSummary ('Parent of the Church of the East') and the-church-of-the-east-under-persia relationsSummary ('a direct heir of the… |
| `coptic-christianity-under-early-islam--alexandria-catechetical` | argued against | Documented | kept | not named in either text; proposed a two-sentence addition to the alexandria legacy (prose change on the desert sentence, second paragraph) |
| `latin-pastoral-congregational-christianity--the-reformed-cities-zurich-and-geneva` | influenced | Documented | kept | not named in either text; prose change 11 adds one sentence to latin-pastoral-congregational-christianity legacy. |
| `tertullian-s-voice--modalist-monarchianism` | argued against | Documented | kept | tertullian-s-voice longDescription (Against Praxeas); modalist-monarchianism text also names Tertullian / D: modalist-monarchianism longDescription, why, legacy (Against … |
| `roman-church-third-century--modalist-monarchianism` | argued against | Documented | kept | modalist-monarchianism relationsSummary and longDescription (Hippolytus and Callistus). |
| `syriac-edessa-nisibis--bardaisanite-current` | argued against | Documented | kept | Named in both: syriac-edessa-nisibis longDescription ('answering by name the teachings of the philosopher Bardaisan'); bardaisanite-current relationsSummary ('Ephraim's p… |
| `post-apostolic-house-church--roman-church-third-century` | continued as | Widely Accepted | kept | roman-church-third-century longDescription ('Between the house-church world that ends around 200 and the Novatian schism of 251, the Roman church ...'); not named in post… |
| `roman-church-third-century--novatianism` | gave rise to | Documented | kept | novatianism longDescription (rival consecration against Cornelius); roman-church-third-century longDescription, legacy and rewritten relationsSummary. |
| `greek-apologists-second-century--alexandria-catechetical` | influenced | Documented | kept | greek-apologists-second-century legacy ('Clement and Origen at Alexandria') / B: greek-apologists longDescription ('Clement and Origen at Alexandria took much further'). … |
| `anatolian-church-third-century--cappadocian-nicene-pastoral-monastic-tradition` | influenced | Documented | changed | anatolian relationsSummary and legacy (Macrina; Basil citing Gregory's practice as precedent) |
| `alexandria-catechetical--anatolian-church-third-century` | influenced | Documented | kept | anatolian relationsSummary, longDescription and why (Gregory as Origen's pupil) |
| `alexandria-catechetical--palestinian-church-pre-constantinian` | influenced | Documented | kept | alexandria longDescription (move to Caesarea c. 231); palestinian relationsSummary, longDescription and why |
| `palestinian-church-pre-constantinian--jerusalem-liturgical-pilgrimage-christianity` | continued as | Inferential-Thin | kept | palestinian relationsSummary ('which begins where this ends'); the prose claims succession in time, consistent with the Inferential-Thin grade |
| `palestinian-church-pre-constantinian--imperial-juridical-christianity` | influenced | Documented | kept | palestinian longDescription and legacy (Eusebius wrote the Church History from Pamphilus's and Alexander's shelves) |
| `danubian-latin-christianity--hieronymian-ascetic-literary` | influenced | Documented | kept | danubian-latin-christianity relationsSummary, why and longDescription (Jerome's judgment of Victorinus and his edition) |
| `danubian-latin-christianity--homoian-arian-christianity` | gave rise to | Widely Accepted | kept | danubian-latin-christianity longDescription (Valens of Mursa, Ursacius of Singidunum) and relationsSummary |
| `alexandria-catechetical--aquileian-christianity` | influenced | Widely Accepted | kept | aquileian relationsSummary (Rufinus and Origen in Latin); not in the alexandria text, which is enough under the either-side rule |
| `antiochene-church-third-century--antiochene-exegetical-christianity-chrysostom-ce` | influenced | Inferential-Thin | kept | antiochene-church-third-century legacy (Lucian and Diodore, Theodore, Chrysostom); the prose change makes the text as tentative as the link |
| `antiochene-church-third-century--homoian-arian-christianity` | gave rise to | Documented | kept | antiochene-church-third-century longDescription (Lucian's students, Arius among them) and legacy (Arius to Eusebius of Nicomedia as fellow Lucianists) |
| `greek-apologists-second-century--latin-apologists` | influenced | Documented | kept | latin-apologists relationsSummary ('the Latin counterpart to the Greek apologists ... a generation later'); the text names the pair, the link carries the documented conta… |
| `tertullian-s-voice--latin-apologists` | influenced | Documented | kept | tertullian-s-voice relationsSummary and latin-apologists relationsSummary |
| `latin-apologists--imperial-juridical-christianity` | influenced | Inferential-Thin | kept | latin-apologists relationsSummary, longDescription and why (Lactantius tutoring Constantine's son); the thin grade matches the text's own 'clearest link ... runs through … |
| `anatolian-church-third-century--alexandria-catechetical` | argued against | Documented | kept | anatolian relationsSummary, longDescription and why (Methodius as Origen's critic) |
| `hieronymian-ascetic-literary--alexandria-catechetical` | argued against | Documented | kept | hieronymian relationsSummary ('the same legacy this circle later fractured over with Rufinus'); alexandria legacy only hints ('careful about saying so') |
| `latin-pastoral-congregational-christianity--pelagianism` | argued against | Documented | kept | pelagianism longDescription, why, legacy (Augustine fought them). |
| `latin-pastoral-congregational-christianity--donatism` | argued against | Documented | kept | donatism why ('Augustine chief among them') and legacy; latin-pastoral rewritten relationsSummary. |
| `donatism--latin-pastoral-congregational-christianity` | argued against | Widely Accepted | kept | donatism relationsSummary ('Rival-sibling of the Latin pastoral congregational tradition'); latin-pastoral rewritten relationsSummary. |
| `latin-pastoral-congregational-christianity--donatism--2` | influenced | Documented | kept | not named in either text; prose change 10 adds one sentence to latin-pastoral-congregational-christianity legacy. |
| `tertullian-s-voice--latin-pastoral-congregational-christianity` | influenced | Documented | new | tertullian-s-voice why ('Cyprian ... read him every day and called him simply "the master"') and legacy ('Cyprian, Jerome and Augustine all read him closely') |
| `tertullian-s-voice--hieronymian-ascetic-literary` | influenced | Documented | new | tertullian-s-voice legacy ('Cyprian, Jerome and Augustine all read him closely'); hieronymian-ascetic-literary does not name Tertullian, which needs nothing added |
| `alexandria-catechetical--cappadocian-nicene-pastoral-monastic-tradition` | influenced | Documented | new | alexandria-catechetical legacy (Basil and Gregory of Nazianzus and Origen's writings); not named in the Cappadocian text, which is enough under the either-side rule |
| `alexandria-catechetical--ambrosian-milan-standalone` | influenced | Documented | new | alexandria-catechetical legacy ('Ambrose ... read him closely even when they were careful about saying so') |
| `palestinian-church-pre-constantinian--hieronymian-ascetic-literary` | influenced | Documented | new | palestinian-church-pre-constantinian legacy (Jerome and the Caesarea library; sentence rewritten in prose change 1) |
| `anatolian-church-third-century--byzantine-imperial-church-heraclian-iconoclast` | influenced | Documented | new | anatolian legacy ('Gregory's Canonical Epistle entered the received canon-law collections of the East'); the Heraclian text names 'the canons issued at Constantinople in … |
| `apocryphal-and-pseudepigraphal-literature--alexandria-catechetical` | influenced | Documented | new | apocryphal relationsSummary (rewritten in prose change 2 to name Origen and the Book of James) |
| `syriac-edessa-nisibis--marcion-marcionism` | argued against | Documented | new | syriac-edessa-nisibis longDescription: 'answering by name the teachings ... of Marcion'. |
| `syriac-edessa-nisibis--manichaeism` | argued against | Documented | new | syriac-edessa-nisibis longDescription: 'answering by name the teachings ... of Mani'. manichaeism's own text does not name Ephraim or Edessa; the link stands on the Syria… |
| `bardaisanite-current--marcion-marcionism` | argued against | Documented | new | bardaisanite-current longDescription and why: 'He wrote against Marcion'. |
| `bardaisanite-current--syriac-edessa-nisibis` | influenced | Documented | new | bardaisanite-current legacy ('Ephraim's decision to answer them in the same form gave the Syriac church the madrasha tradition') and why. syriac-edessa-nisibis's own text… |
| `latin-pastoral-congregational-christianity--manichaeism` | argued against | Documented | new | manichaeism longDescription ('Augustine of Hippo was a Hearer for roughly nine years ... arguing against the teachers he had once sat under') and relationsSummary. latin-… |
| `alexandria-catechetical--ebionite-nazoraean-current` | argued against | Documented | new | ebionite-nazoraean-current longDescription: 'Later heresy-hunting writers — Irenaeus, Origen, ... describe them'. alexandria-catechetical's text names Origen but not the … |
| `hieronymian-ascetic-literary--ebionite-nazoraean-current` | argued against | Documented | new | ebionite-nazoraean-current longDescription: '... Epiphanius, Jerome — describe them'. hieronymian-ascetic-literary's text names Jerome but not the Ebionites; member-to-co… |
| `syriac-edessa-nisibis--persian-church-of-the-east-early` | continued as | Documented | new | syriac-edessa-nisibis relationsSummary ('Parent of the Church of the East'), its continuesAs field, and its longDescription close (the synod of 410); persian-church-of-th… |
| `syriac-edessa-nisibis--syriac-orthodox-west-syriac-christianity` | gave rise to | Inferential-Thin | new | syriac-edessa-nisibis relationsSummary ('Parent of ... the Syriac Orthodox Church') and legacy ('descend from this tradition'); syriac-orthodox-west-syriac-christianity r… |
| `post-apostolic-house-church--montanism-the-new-prophecy` | argued against | Documented | new | montanism-the-new-prophecy longDescription ('Asian synods condemned it') and rewritten relationsSummary (prose change 5). The house-church world's own records already tre… |
| `montanism-the-new-prophecy--tertullian-s-voice` | influenced | Documented | new | montanism-the-new-prophecy longDescription ('Tertullian of Carthage became its most articulate Latin advocate'); tertullian-s-voice longDescription and why ('aligned hims… |
| `imperial-juridical-christianity--montanism-the-new-prophecy` | argued against | Documented | new | montanism-the-new-prophecy longDescription ('later imperial law suppressed it'). |
| `byzantine-imperial-church-justinianic--montanism-the-new-prophecy` | argued against | Documented | new | montanism-the-new-prophecy legacy ('Imperial suppression under Justinian'), as rewritten in prose change 6. |
| `latin-pastoral-congregational-christianity--novatianism` | argued against | Documented | new | novatianism legacy ('worked out by Cyprian in the moment and by Augustine at length afterwards'). |
| `imperial-juridical-christianity--novatianism` | argued against | Documented | new | novatianism longDescription ('the council's eighth canon set out terms for receiving Novatianist clergy'). |
| `imperial-juridical-christianity--novatianism--2` | in contact with | Documented | new | novatianism longDescription and why ('Their bishop attended the Council of Nicaea in 325 and accepted its creed'). |
| `tertullian-s-voice--marcion-marcionism` | argued against | Documented | new | marcion-marcionism longDescription ('above all Tertullian, whose Against Marcion runs to five books') and relationsSummary; also latin-apologists longDescription |
| `greek-apologists-second-century--marcion-marcionism` | argued against | Documented | new | marcion-marcionism voices field ('Justin Martyr - wrote against him within Marcion's own lifetime') and relationsSummary ('the proto-orthodox defined themselves against')… |
| `post-apostolic-house-church--marcion-marcionism` | argued against | Documented | new | marcion-marcionism longDescription and why ('the Roman church expelled him and returned his money'); relationsSummary ('the proto-orthodox') |
| `tertullian-s-voice--valentinian-and-other-gnostic-christianities` | argued against | Documented | new | valentinian-and-other-gnostic-christianities longDescription ('according to Tertullian') and relationsSummary |
| `post-apostolic-house-church--valentinian-and-other-gnostic-christianities` | argued against | Documented | new | valentinian-and-other-gnostic-christianities relationsSummary ('Rivals the early churches cast out and wrote against', after the prose change) and longDescription ('came … |
| `greek-apologists-second-century--valentinian-and-other-gnostic-christianities` | argued against | Documented | new | valentinian-and-other-gnostic-christianities relationsSummary ('the early churches ... wrote against') and longDescription (Basilides); Justin is not named in its text |
| `antiochene-church-third-century--anomoean-eunomian-christianity` | influenced | Documented | new | antiochene-church-third-century relationsSummary ('the seedbed of the controversy the Homoian and Anomoean disputes', rewritten to name Aetius's teachers) |
| `anatolian-church-third-century--antiochene-church-third-century` | in contact with | Documented | new | antiochene-church-third-century longDescription ('the bishops of Syria and Asia Minor met at Antioch'); not named in anatolian-church-third-century's text |
| `antiochene-church-third-century--roman-church-third-century` | in contact with | Documented | new | antiochene-church-third-century longDescription and why ('in communion with the bishops of Italy and Rome'); not named in roman-church-third-century's text |
| `anatolian-church-third-century--hieronymian-ascetic-literary` | influenced | Documented | new | anatolian-church-third-century, legacy: "Jerome knew the Banquet by name" (added in revision, R1-15). |
| `imperial-juridical-christianity--ebionite-nazoraean-current` | argued against | Documented | new | ebionite-nazoraean-current, longDescription: names Eusebius among the writers who describe the Ebionites (added in revision, two-way gap). |

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-07):
- Irenaeus has no movement of his own.
- Montanism's end date ("c. 165-400s") against its own sixth-century evidence. For the census entry's owner.
- Raw movement IDs in four era-2 and era-3 movements' text. For those eras' passes.
- Who compiled the Philocalia: the records disagree. Ruled by Mark after the merge: the tree credits Basil and Gregory, and the records stay as they are (Decision-Log, "The Philocalia's compilers", 2026-11-07; data release 5).
- The roman-church-third-century half of "Two movement texts repeat corrected claims" is fixed; the Aquileia half (era 2) stays open.

Notes:
- Two Manichaean claims were softened because no vendored or repo-cited source carries them: the Jewish-Christian baptizing sect of Mani's youth, and the Uyghur adoption as a state religion in the 760s. Both are standard scholarship; the wanted texts below would restore them.
- `imperial-juridical-christianity--ebionite-nazoraean-current` files Eusebius's Church History (finished c. 324) under the Constantinian church, not the pre-Constantinian church of Caesarea that ends in 312. Round 2 agreed.
- Three new quotes keep the source file's `<i>` markup because the titles they need stand in italics in the file (Jerome, On Illustrious Men 83; Jerome, Letter 84.7; McGiffert on the date of the Church History). Tree pages do not print quotes; any future page that does must render or strip it. A link already on main carries the same markup.

## Wanted texts

- A clean critical text of the Codex Theodosianus 16.5 laws naming the Montanists (16.5.34, 16.5.48); the vendored Mommsen-Meyer OCR is rough
- A clean edition of Augustine, De haeresibus 86, to replace the PL 42 OCR
- A clean text of Eusebius HE VII.28.1 without footnote breaks, to quote Hymenaeus of Jerusalem and Theotecnus of Caesarea at the Antioch synods (would allow a palestinian-church-pre-constantinian contact link)
- A modern English translation of the Cologne Mani Codex (e.g. Cameron and Dewey 1979, or Koenen and Römer), to document Mani's upbringing among the baptizers (the Elchasaite 'Jewish-Christian' identification) beyond the Fihrist via Newman.
- A primary or scholarly source for the Uyghur khagan Bögü's adoption of Manichaeism in 762/3 (e.g. the Karabalgasun inscription in translation), to replace the Yule-Cordier report of von Le Coq.
- A readable text of Epiphanius, Panarion 73.12, or Hilary, De synodis 81 and 86, quoting the Ancyra/Homoiousian appeal to the council against Paul (Panarion 65-80 is vendored only as PG Greek-Latin OCR)
- A repo-cited modern work dating the Gospel of the Nativity of Mary (the 'Carolingian abridgement')
- A repo-cited modern work on Pentecostal and charismatic Christianity being compared with Montanism, if that claim is to come back
- A repo-cited modern work on the origin of the Testaments of the Twelve Patriarchs (Jewish with Christian additions, or Christian on Jewish sources)
- A repo-cited secondary on Victorinus's reception by Tyconius and Augustine (none found)
- A repo-cited secondary work stating the Nisibis-to-Persian-church continuity directly
- A source for the Uyghur khagan's adoption of Manichaeism in the 760s (e.g. the Karabalgasun inscription in translation)
- A text by Ambrose, Jerome or Gregory of Nyssa that uses or names Methodius's Banquet on virginity
- A text documenting Latin Christian communities in North Africa after the Arab conquest (e.g. Gregory VII's letters of 1076 to Carthage), to date the end
- A text in which Jerome says he consulted the Hexapla at Caesarea (Commentary on Titus 3.9, or his Psalms commentary), and any source for the Hexapla surviving there until the Arab conquest
- A text or repo-cited secondary showing that Lactantius lost his chair at Nicomedia when the persecution began
- A vendored Alexandrian text that names Justin for the 'seeds of the Word' argument (still wanted from 2026-11-06)
- Ambrose's Hexaemeron or Exposition of Luke in a vendored edition, to show his use of Origen from his own side
- An edition of Victorinus of Poetovio's Commentary on the Apocalypse giving both his own text and Jerome's recension, to document the reissue directly.
- Any text saying Basil's grandmother Macrina was taught by Gregory Thaumaturgus's disciples (Basil says only that she kept his words)
- Codex Justinianus 1.5.20 (530), or John of Ephesus on the Montanists at Pepuza, for a non-hostile account of Justinian's campaign
- Cornelius's letter to Fabius (Eusebius HE VI.43.5-20) read for Novatian's consecration, to give the Roman rupture its own quote
- Ephraim's Hymns against Heresies in a full vendored translation, to quote his complaint about Bardaisan's hymns directly rather than through Gwynn's 1898 introduction
- Epiphanius, Panarion 29-30 (Nazoraeans and Ebionites); the vendored Holl volume begins at haer. 34
- Jerome's Chronicle (for Arnobius and his bishop), if the story is to be cited
- Jerome's prologue to Anatolius on his revision of Victorinus's Commentary on the Apocalypse (would document 'Jerome edited it' and his objection to the millenarian ending)
- Menze (2008) or Frend (1972) on the making of the Syriac Orthodox Church: named in Build/worlds/wsyr/Doc_02_Source_Ecology.md, never consulted
- Sebastian Moll, The Arch-Heretic Marcion (2010), read for the 144 arrival-versus-expulsion argument (named in the pahc Doc_01 but not read)
- The Cologne Mani Codex in a vendored edition or a repo-cited study, to support 'a Jewish-Christian baptizing sect' (Elchasaites)
- The Golden Legend or another medieval text, to document the medieval reception of the apocryphal Acts' martyrdoms, the Dormition narratives and the Revelation of Paul
- The Greek text of Gregory of Nazianzus, Letter 115, in clean form, to quote 'and the same from holy Basil' (in NPNF 8 it is split one word per line)
- Theodoret, Haereticarum fabularum compendium I.22 (names Bardaisan's dialogues against Marcion and Harmonius)
- Theophanes, Chronographia (AM 6214), if the Montanists' survival into the eighth century is to be stated
- Volker L. Menze, Justinian and the Making of the Syrian Orthodox Church (2008), read and cited by page, before syriac-edessa-nisibis--syriac-orthodox-west-syriac-christianity can be regraded above Inferential-Thin.
- W. H. C. Frend, The Rise of the Monophysite Movement (1972), read and cited by page, for the same link.
