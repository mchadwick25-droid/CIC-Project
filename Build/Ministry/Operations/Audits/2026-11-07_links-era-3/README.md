# Church Family Tree links, era 3 (P2-L3) — 2026-11-07

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`; this era's addendum is `Drafting_Brief_Era3.md`.

Run beside era 2 (P2-L2). Every relationship between an era-3 and an era-2 movement that the era-2 movement's own text names was left to era 2 (`out-of-scope`, "era 2 owns it"). Steps 1 to 6 wrote only to this folder. Step 7 began after era 2 merged (data release 6, mchadwick25-droid/CIC-Project#1539): the branch was rebased onto the new `main`, every era-2/era-3 pair was checked against it (no clash; era 2's new link from the Homoian church to the Gothic churches closes a gap this pass had flagged), and the pass was applied as data release 7.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 19 movements, 293 named relationships.
2. **Draft** (Opus, five groups by region): `Draft_GroupA.json` to `Draft_GroupE.json`, merged in `Drafting_Record.json`. Five links were drafted by two groups; the merge notes say which draft was kept and what was carried over from the other.
3. **Readability pass** (Opus, three batches): `Prose_Pass_1.json` to `Prose_Pass_3.json`. 38 of 45 changed paragraphs scored below Reading Ease 60 before it.
4. **Review round 1** (separate Opus 5.5 agent, full review): `Opus_Review_Round1.json`. Revise: 2 blocking, 11 substantial, 15 minor, no fabrication. The blocking findings: a note put the patriarch Benjamin in hiding at Wadi Habib, which the source says he left; and a Gothic-to-Visigothic "gave rise to" link misstated the relationship.
5. **Revision** (Opus): `Revision_Round1.json`. All 28 findings dealt with; two partly declined on the evidence (R1-05, R1-07), upheld in round 2. Three unpublished links dropped, one added (Whitby).
6. **Review round 2** (targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 2 substantial, 3 minor. Both substantial findings were one fault in the merge script, not the drafting: it matched disposition rows on movement, field and sentence, ignoring the other party, so rows sharing a sentence were overwritten. The merge was undone and redone keyed on the other party too (`Revision_Round2.json`).
7. **Review round 3** (targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 1 minor (an open item not yet logged; now logged below).

All three rounds of the cap used; the last passed.

8. **Link-note readability** (Opus, two batches, after round 3): `Note_Readability_Pass.json`. Era 2 scored its link notes, so era 3's were scored too: 40 of 55 new or rewritten notes were below Reading Ease 60. Each was rewritten for readability only. A script checked every number and proper name against the old note, and the rest were read by hand. One note stays at 57.7 (the Chalcedon break), because every shorter version dropped a fact. These rewrites came after the last review round, so they were not independently reviewed; P2-L11 should recheck them.

9. **Apply and rebuild:** links and prose written to `cic-website/data/world-census.json` (data release 7); `atlas-sync`; tree pages regenerated; tree site built, 0 mismatched copies. Checks: `validate-census.mjs --base` (main's census, release 6) `--atlas --tree` 0 errors; `engine.m6.cli check` pass; `atlas-check --edges-only` no difference; tree-page tests pass; commentary (`--enforce`), spelling and paths checks clean. The map (225 links drawn, no console errors) and two tree pages (`roman-church-gregorian`, `church-of-caucasian-albania`) were opened in a browser; link anchors resolve and scroll into view.

## Counts

- Census links in all: 172 before (release 6), 225 after (release 7).
- Links touching an era-3 movement in this pass: 67 (53 new, 2 rewritten, 12 kept). No published link retired.
- Grades of the new links: Documented 34, Widely Accepted 11, Inferential-Thin 4, Dominant Modern Reconstruction 4.
- Types of the new links: influenced 15, continued as 12, argued against 12, in contact with 11, broke with 2, gave rise to 1.
- Dispositions of the named relationships: link 121, no-entry 103, qualify 37, kept-as-is 23, out-of-scope 12, remove 1 (297 rows; a sentence naming several parties has a row per party). "no-entry" means the other party has no census movement (a person, a state, a council); its claim was still checked, and qualified where unsupported.
- Prose: 47 fields changed, 47 paragraphs scored. Every one scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`); 11 sit below FK grade 8, which the scorer reports but does not fail.
- Quote check: every primary quote was checked verbatim against its vendored file and lines by script (the validator's rule) after drafting and after each revision: 0 failures.

## Two-way check

### Prose to links

Every relationship named in an era-3 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or era 2 owns it (per-row record: `Drafting_Record.json`, `dispositions`). Round 1 found five gaps (Whitby; the Vandal persecution rows; the re-pointing after three dropped links; Montanism; the era-2 Homoian descent); rounds 2 and 3 confirm them closed or logged.

Sentences qualified or removed (38):

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| cyrilline-miaphysite-egyptian-christianity | relationsSummary | qualify | alexandria-catechetical is the catechetical school world (c. 150-400), not the see of Alexandria; no text shows this church continuing the school, and its own History co… |
| cyrilline-miaphysite-egyptian-christianity | legacy | qualify | No vendored text shows this church passing Cyril to Armenia in 451-642; Timothy Aelurus's Refutation survives in Armenian but the translation is undated. Restated as a s… |
| aksumite-christianity | relationsSummary | qualify | No vendored text of 451-615 shows Aksum rejecting Chalcedon; Procopius (Wars I.20) has Justinian appeal to the kingdoms' 'community of religion'. No link to the imperial… |
| aksumite-christianity | longDescription | qualify | As in the relationsSummary; restated as 'no text from inside these years shows where its church stood on Chalcedon'. |
| latin-africa-under-byzantium | relationsSummary | qualify | No text shows this church using Tertullian; Facundus and Ferrandus's own text (PL 67) cite Cyprian and Augustine, and the Tertullian references in that file are Migne's … |
| latin-africa-under-byzantium | longDescription | qualify | A person, not a movement relationship. 'Formative years' is wrong: he came to Africa as an adult monk. Restated as the 645 disputation with Pyrrhus held in Africa (PG 91… |
| latin-africa-under-byzantium | legacy | qualify | 'Hardened a Western conviction' is a reception claim no vendored text shows; restated as what Facundus and Victor show. The Three Chapters link carries the relationship. |
| latin-africa-under-byzantium | legacy | qualify | Council, not a movement. 'Fed straight into' is causal and not shown; restated as the sequence the vendored texts show (646 letters read at Rome in 649; Constantinople I… |
| syriac-orthodox-west-syriac-christianity | longDescription | qualify | Comparison, not a relationship, so no link. The contrast 'inside the Roman Empire' fails, since Egypt was inside it too; rewritten to the documented loss of Antioch (Eva… |
| the-church-of-the-east-under-persia | longDescription | qualify | Era-2 movement, but only this text names the relationship, so it is ours. No link: the 424 act is a one-sided declaration about Western bishops, not a rupture both sides… |
| the-church-of-the-east-under-persia | legacy | qualify | The link for this period is Inferential-Thin (Cosmas only reports a church and a Persian-appointed bishop). The later tie is shown by Geddes 1694 (bishops from the 'Patr… |
| chalcedonian-monasticism-judean-desert-and-gaza | relationsSummary | qualify | Sinai has no movement. Moschus visits Sinai elders (Pratum, 14276) and Climacus was abbot there (PG 88, 41597), but no text shows these houses forming him; narrowed to m… |
| chalcedonian-monasticism-judean-desert-and-gaza | relationsSummary | qualify | No single movement. 'All later Orthodox practice' narrowed to what Charon (1911) shows of the Typikon of Saint Sabas. |
| chalcedonian-monasticism-judean-desert-and-gaza | longDescription | qualify | Ours (Byzantine imperial church, era 3), but the claim is about the monks' stance, not a link type. 'Firm supporters' is untrue of part of this movement: Cyril's Life of… |
| chalcedonian-monasticism-judean-desert-and-gaza | legacy | qualify | Generic; 'a great deal ... comes from here' softened to 'draws on', supported by the Typikon evidence (Charon 22562-22568). |
| chalcedonian-monasticism-judean-desert-and-gaza | legacy | qualify | No single movement. Narrowed to Charon (1911): the Typikon 'dit de saint Sabas', printed at Venice from 1515, fragments in the Triodion (22562-22568). |
| byzantine-imperial-church-justinianic | legacy | qualify | Region, no movement; no vendored text shows the Balkans export, so it goes. |
| byzantine-imperial-church-justinianic | legacy | qualify | Era-4 movement. No link from this era: the Rus' received their church order from the later Byzantine church (Mouravieff 1842, 1426-1431, 1463-1467). Sentence narrowed to… |
| church-of-caucasian-albania | relationsSummary | qualify | 'Absorbed into the Armenian catholicosate' overstates it: the see lived on inside the Armenian church until the early nineteenth century (Ormanian p. 132; Hasan-Jalalian… |
| church-of-caucasian-albania | longDescription | qualify | Monastery, not a movement. 'Found ... in 1996' is reworded to 'were found in 1996 to preserve', true whether 1996 is the year of discovery or of identification. Authorit… |
| church-of-caucasian-albania | why | qualify | 'Absorbed' overstates it (the see lived on until the early nineteenth century); qualified to 'came under the Armenian church's authority'. Link L8. |
| church-of-caucasian-albania | why | qualify | Palimpsest date reworded as in the longDescription change. |
| church-of-caucasian-albania | legacy | qualify | The see was not absorbed out of existence after 705: a 92nd catholicos of Aghovanie was installed in 1701/2 with the Armenian catholicos's investiture (Brosset 1876, lin… |
| church-of-caucasian-albania | legacy | qualify | 'Its separate identity dissolved into its neighbors'' becomes 'its people merged with the Armenians': Ormanian (p. 132) speaks of 'the fusion of the Caspio-Albanian or A… |
| church-of-caucasian-albania | legacy | remove | No vendored or repo-cited source says Albania's identity dissolved into Georgia's; Ormanian names only the Armenian fusion. The Georgian half of 'its neighbors'' is drop… |
| church-of-caucasian-albania | legacy | qualify | 'Recovered at Sinai in 1996' reworded to 'were found in 1996 to preserve', as in the longDescription change. |
| early-benedictine-italian-monasticism | relationsSummary | qualify | No single movement; 'the whole Latin monastic line' overstates what Gasquet shows (Columban's rule stood apart). Rewritten to 'the norm for most later Latin monasteries'… |
| early-benedictine-italian-monasticism | longDescription | qualify | The older rule (the Rule of the Master) has no census movement. Its priority over Benedict's Rule is the majority modern view, not shown by a vendored text; said as what… |
| early-benedictine-italian-monasticism | why | qualify | As the longDescription: the older text's priority is the majority scholarly view, now said so. |
| early-benedictine-italian-monasticism | legacy | qualify | No census movements. Cistercians supported by Hunter Blair's notes on Cistercian legislation; Benedictine congregations today by the Rule's two Benedictine editors (1907… |
| insular-irish-monastic-christianity | relationsSummary | qualify | The link is kept as Inferential-Thin. 'Contested' overstates: no vendored or repo-cited source argues the other side; the evidence is one eighth-century tract read by Wa… |
| insular-irish-monastic-christianity | legacy | qualify | 'Dozens of monasteries across Gaul and Italy' is not shown: Jonas names five houses founded under the rule (Palatium, the Jura house, Flavia's nunnery, Ado's and Dado's … |
| insular-irish-monastic-christianity | legacy | qualify | Columbanus's penitential was written on the Continent, not 'here' in Ireland, and it was the model for a long line of Frankish penitentials (Wasserschleben 1851, lines 1… |
| nicene-visigothic-iberia | longDescription | qualify | 'All of it ended' contradicts the legacy field, which says the same institution continued under Muslim rule. The 754 chronicle shows the kingdom ended ('regno ablato vec… |
| british-welsh-christianity | relationsSummary | qualify | 'Distinct from' is a cataloguing statement no link type expresses. Bede II.4 shows likeness, not separation: Laurentius found that 'the Scots in no way differ from the B… |
| british-welsh-christianity | relationsSummary | qualify | 'Did not conform at Whitby' implies the British were a party there; Bede's list of those present has no British clergy (bede 7963-7970). What the sources show is that th… |
| british-welsh-christianity | legacy | qualify | Kept in substance: the Welsh church carried on under its own bishops after 768 (Annales Cambriae: Elbodug archbishop d. 809, annales 3102-3104; Nobis bishop in Miniu, 33… |
| british-welsh-christianity | legacy | qualify | No vendored or repo-cited source shows the Welsh bishops coming under Canterbury in the twelfth century (searched cic/texts, Build, records). The clause is cut and the s… |

### Links to prose

| Link | Type | Grade | Status | Named in |
|---|---|---|---|---|
| `desert-monasticism--cyrilline-miaphysite-egyptian-christianity` | influenced | Documented | new | cyrilline-miaphysite-egyptian-christianity relationsSummary ('Continues ... Desert') and longDescription ('carried by the monasteries of the Egyptian desert'); the deser… |
| `syriac-orthodox-west-syriac-christianity--cyrilline-miaphysite-egyptian-christianity` | influenced | Documented | new | cyrilline-miaphysite-egyptian-christianity longDescription ('Severus of Antioch ... who became the movement's great theologian'). |
| `cyrilline-miaphysite-egyptian-christianity--nubian-christianity` | gave rise to | Documented | new | nubian-christianity relationsSummary ('Child of Egypt'), longDescription ('a Miaphysite priest named Julian sent with the empress Theodora's backing'), why ('rival missi… |
| `byzantine-imperial-church-justinianic--nubian-christianity` | in contact with | Documented | new | nubian-christianity relationsSummary ('both rival communions' missions'), longDescription ('a Chalcedonian effort sent with Justinian's'). |
| `cyrilline-miaphysite-egyptian-christianity--coptic-christianity-under-early-islam` | continued as | Documented | new | cyrilline-miaphysite-egyptian-christianity legacy ('the same institution continued under Muslim rule as Coptic Christianity') and its continuesAs field; coptic-christian… |
| `aksumite-christianity--cyrilline-miaphysite-egyptian-christianity` | in contact with | Inferential-Thin | new | aksumite-christianity relationsSummary ('In communion with Alexandria'), longDescription and why ('Its church stayed in communion with Alexandria'); cyrilline-miaphysite… |
| `aksumite-christianity--post-aksumite-ethiopian-christianity` | continued as | Widely Accepted | new | aksumite-christianity relationsSummary ('parent of the later medieval Ethiopian church'), legacy ('The same institution continued without interruption'), and its continu… |
| `nubian-christianity--makurian-nubian-christianity` | continued as | Widely Accepted | new | nubian-christianity legacy ('Christian Nubia outlasted this window by many centuries') and its continuesAs field. |
| `latin-pastoral-congregational-christianity--latin-africa-under-byzantium` | influenced | Documented | new | latin-africa-under-byzantium relationsSummary ('heir to the earlier African Christian tradition of Tertullian, Cyprian and Augustine'), longDescription and legacy (Cypri… |
| `latin-africa-under-byzantium--byzantine-imperial-church-justinianic` | argued against | Documented | new | latin-africa-under-byzantium relationsSummary ('one of the principal voices resisting Justinian's condemnation of the Three Chapters'), longDescription ('the most stubbo… |
| `latin-africa-under-byzantium--byzantine-imperial-church-heraclian-iconoclast` | argued against | Documented | new | latin-africa-under-byzantium longDescription ('African councils in 646 rejected the empire's next attempted compromise about the wills of Christ'), legacy ('its part in … |
| `syriac-edessa-nisibis--syriac-orthodox-west-syriac-christianity` | gave rise to | Inferential-Thin | kept | syriac-orthodox-west-syriac-christianity relationsSummary ('Heir of the Syriac tradition's Roman side'), rewritten in prose change 0 to match the thin grade; syriac-edes… |
| `syriac-edessa-nisibis--the-church-of-the-east-under-persia` | influenced | Documented | kept | the-church-of-the-east-under-persia relationsSummary ('a direct heir of the Syriac Christian tradition'); syriac-edessa-nisibis relationsSummary |
| `palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza` | continued as | Inferential-Thin | kept | chalcedonian-monasticism-judean-desert-and-gaza longDescription (the laura form); the era-2 movement's own text also names it |
| `byzantine-imperial-church-justinianic--montanism-the-new-prophecy` | argued against | Documented | kept | montanism-the-new-prophecy legacy ('Imperial suppression under Justinian'); not named in the Byzantine imperial church's own text |
| `byzantine-imperial-church-justinianic--cyrilline-miaphysite-egyptian-christianity` | broke with | Documented | changed | byzantine-imperial-church-justinianic relationsSummary ('the rival imperial context against which Miaphysite Egypt ... defined themselves'), longDescription ('without re… |
| `byzantine-imperial-church-justinianic--syriac-orthodox-west-syriac-christianity` | broke with | Documented | new | byzantine-imperial-church-justinianic relationsSummary ('the rival imperial context against which ... the Syriac Orthodox church defined themselves') and longDescription… |
| `byzantine-imperial-church-justinianic--syriac-orthodox-west-syriac-christianity--2` | argued against | Documented | new | syriac-orthodox-west-syriac-christianity longDescription ('for long stretches under Justinian without legal standing at all') and why ('no legal right to exist under Jus… |
| `cyrilline-miaphysite-egyptian-christianity--syriac-orthodox-west-syriac-christianity` | in contact with | Documented | new | syriac-orthodox-west-syriac-christianity longDescription ('Severus ... wrote from exile in Egypt'), kept in prose change 1 as 'He withdrew to Egypt, as many of his bisho… |
| `syriac-orthodox-west-syriac-christianity--syriac-orthodox-under-islam` | continued as | Documented | new | syriac-orthodox-west-syriac-christianity legacy ('The same institution is still here. It continued under Muslim rule'); syriac-orthodox-under-islam longDescription ('For… |
| `byzantine-imperial-church-justinianic--byzantine-imperial-church-heraclian-iconoclast` | continued as | Documented | new | byzantine-imperial-church-justinianic legacy ('The same institution continued unbroken into the Byzantine centuries that followed'); byzantine-imperial-church-heraclian-… |
| `the-church-of-the-east-under-persia--the-church-of-the-east-on-the-silk-road` | continued as | Documented | new | the-church-of-the-east-under-persia legacy ('The same institution continued without a break ... its missions reaching Central Asia and China') and longDescription ('the … |
| `the-church-of-the-east-under-persia--syriac-orthodox-west-syriac-christianity` | argued against | Documented | new | the-church-of-the-east-under-persia longDescription ('It gave a different answer to the question of Christ than either Chalcedon or the Miaphysites') |
| `the-church-of-the-east-under-persia--st-thomas-christians-of-india` | influenced | Inferential-Thin | new | the-church-of-the-east-under-persia relationsSummary, longDescription and why ('the St Thomas Christians of India belonged to its communion'), all rewritten in prose cha… |
| `desert-monasticism--chalcedonian-monasticism-judean-desert-and-gaza` | influenced | Documented | new | chalcedonian-monasticism-judean-desert-and-gaza relationsSummary ('Direct heir of Desert Monasticism'), rewritten in prose change 7 to 'drew on ... quoting the Egyptian … |
| `byzantine-imperial-church-justinianic--chalcedonian-monasticism-judean-desert-and-gaza` | in contact with | Documented | new | chalcedonian-monasticism-judean-desert-and-gaza longDescription ('they were pulled hard into the empire's doctrinal fights, including the purge of Origenist teaching in … |
| `armenian-christianity-after-avarayr--armenian-christianity-before-the-bagratids` | continued as | Widely Accepted | new | armenian-christianity-after-avarayr legacy ('the same institution continued through the medieval Bagratid centuries into the present'); armenian-christianity-before-the-… |
| `armenian-christianity-before-the-bagratids--bagratid-armenian-christianity` | continued as | Widely Accepted | new | armenian-christianity-after-avarayr legacy ('continued through the medieval Bagratid centuries'); armenian-christianity-before-the-bagratids why ('to the start of the Ba… |
| `georgian-christianity--georgian-revival-tao-klarjeti` | continued as | Widely Accepted | new | georgian-christianity legacy ('the same institution continued through the medieval revival centuries into the present') and its continuesAs field. |
| `armenian-christianity-after-avarayr--byzantine-imperial-church-justinianic` | argued against | Dominant Modern Reconstruction | new | armenian-christianity-after-avarayr relationsSummary ('rejects Chalcedon at Dvin'), longDescription ('at the second council of Dvin in 554 the church formally set itself… |
| `armenian-christianity-before-the-bagratids--georgian-christianity` | broke with | Widely Accepted | new | georgian-christianity relationsSummary ('Jerusalem and Armenian lines; takes the Chalcedonian side (609)'), longDescription ('In 609, at the third council of Dvin, its c… |
| `armenian-christianity-after-avarayr--georgian-christianity` | in contact with | Widely Accepted | new | georgian-christianity relationsSummary ('Jerusalem and Armenian lines'); the Shushanik sentences (an Armenian princess married into Kartli). |
| `armenian-christianity-after-avarayr--church-of-caucasian-albania` | in contact with | Widely Accepted | new | church-of-caucasian-albania relationsSummary and longDescription ('beside Armenia and Georgia'), why (the same). |
| `armenian-christianity-before-the-bagratids--church-of-caucasian-albania` | argued against | Dominant Modern Reconstruction | new | church-of-caucasian-albania relationsSummary ('absorbed into the Armenian catholicosate after 705'), longDescription ('when its catholicosate was placed under the Armeni… |
| `byzantine-imperial-church-justinianic--georgian-christianity` | influenced | Widely Accepted | new | georgian-christianity relationsSummary ('takes the Chalcedonian side'), longDescription ('took the Chalcedonian side'), why and legacy ('placed it permanently in the Eas… |
| `jerusalem-liturgical-pilgrimage-christianity--georgian-christianity` | influenced | Inferential-Thin | new | georgian-christianity relationsSummary ('Jerusalem ... lines'), longDescription ('Georgian manuscripts preserve the worship of fifth- to eighth-century Jerusalem') and l… |
| `desert-monasticism--early-benedictine-italian-monasticism` | influenced | Widely Accepted | kept | early-benedictine relationsSummary ('Receives the desert via Cassian'); desert-monasticism's own era-2 text names Benedict's Rule |
| `gallic-monastic-ascetic-christianity--early-benedictine-italian-monasticism` | influenced | Widely Accepted | kept | early-benedictine relationsSummary ('Receives the desert via Cassian'); the Gallic movement's own era-2 text names Benedict's Rule commending Cassian |
| `gallic-monastic-ascetic-christianity--merovingian-gallic-christianity` | influenced | Widely Accepted | kept | merovingian relationsSummary ('Receives Martin of Tours's line'); the Gallic movement's own era-2 text calls itself the seedbed of the Merovingian church |
| `early-benedictine-italian-monasticism--roman-church-gregorian` | influenced | Documented | changed | early-benedictine longDescription ('Gregory the Great ... wrote the only account we have of Benedict's life'); roman-church-gregorian relationsSummary ('wrote the only l… |
| `early-benedictine-italian-monasticism--carolingian-reform-christianity` | influenced | Documented | new | early-benedictine legacy ('Carolingian reformers made it the norm across the Frankish empire'); carolingian-reform text names 'one monastic rule for the whole realm' |
| `early-benedictine-italian-monasticism--cluniac-reform-monasticism` | influenced | Dominant Modern Reconstruction | new | early-benedictine legacy ('it stands behind the Cluniacs') |
| `roman-church-gregorian--anglo-saxon-christianity` | gave rise to | Documented | kept | roman-church-gregorian relationsSummary (letters reach the English church), longDescription and why ('in 596 he sent a party of his own monks to Kent'), legacy ('The mis… |
| `roman-church-gregorian--byzantine-imperial-church-justinianic` | argued against | Documented | kept | roman-church-gregorian longDescription ('He refused the title of universal bishop when Constantinople's patriarch used it') |
| `byzantine-imperial-church-justinianic--roman-church-gregorian` | in contact with | Documented | new | roman-church-gregorian longDescription ('was sent to Constantinople as the pope's representative'); relationsSummary (its letters reach the imperial church) |
| `merovingian-gallic-christianity--roman-church-gregorian` | in contact with | Documented | new | roman-church-gregorian relationsSummary (letters reach the Frankish church) and longDescription ('He told bishops in Gaul ... what he thought they were doing wrong') |
| `nicene-visigothic-iberia--roman-church-gregorian` | in contact with | Documented | new | roman-church-gregorian longDescription ('He told bishops in Gaul, Spain ...') |
| `latin-africa-under-byzantium--roman-church-gregorian` | in contact with | Documented | new | roman-church-gregorian longDescription ('He told bishops in ... Africa ... what he thought they were doing wrong') |
| `roman-church-gregorian--carolingian-reform-christianity` | influenced | Widely Accepted | new | roman-church-gregorian legacy ('Carolingian councils legislated that bishops should own it and read it') |
| `roman-church-gregorian--late-anglo-saxon-christianity` | influenced | Dominant Modern Reconstruction | new | roman-church-gregorian legacy ('Alfred translated it into English'); late-anglo-saxon text also names 'Gregory the Great's Pastoral Care' |
| `merovingian-gallic-christianity--carolingian-reform-christianity` | continued as | Widely Accepted | new | merovingian relationsSummary ('parent of Carolingian Christianity') and legacy ('The same institution continued directly into Carolingian Christianity'); the census cont… |
| `merovingian-gallic-christianity--gothic-and-vandal-homoian-christianity` | argued against | Documented | new | merovingian longDescription ('he brought his people into the same church as the Gallo-Roman bishops rather than into the Homoian one most other barbarian kings held') |
| `byzantine-imperial-church-justinianic--gothic-and-vandal-homoian-christianity` | argued against | Documented | new | gothic longDescription ('In Africa and Ostrogothic Italy it was destroyed by Byzantine reconquest') |
| `desert-monasticism--insular-irish-monastic-christianity` | influenced | Inferential-Thin | kept | insular-irish-monastic-christianity relationsSummary ('Contested line from Gallic/Eastern asceticism'); the desert entry's own text does not name it |
| `gallic-monastic-ascetic-christianity--insular-irish-monastic-christianity` | influenced | Inferential-Thin | kept | insular-irish-monastic-christianity relationsSummary; gallic-monastic-ascetic-christianity relationsSummary ('through Lérins and Tours - of Irish monasticism') |
| `insular-irish-monastic-christianity--anglo-saxon-christianity` | gave rise to | Documented | kept | insular-irish-monastic-christianity relationsSummary ('parent of Anglo-Saxon Christianity') and legacy ('Iona-trained missionaries carried the faith into Northumbria'); … |
| `insular-irish-monastic-christianity--merovingian-gallic-christianity` | influenced | Documented | new | insular-irish-monastic-christianity longDescription ('Columbanus into Gaul and Italy, where he founded Luxeuil'), why ('deep into Gaul and Italy') and legacy (Columbanus… |
| `insular-irish-monastic-christianity--roman-church-gregorian` | argued against | Documented | new | insular-irish-monastic-christianity longDescription ('Its own way of calculating Easter and its distinctive tonsure eventually collided with Roman practice'); the Gregor… |
| `insular-irish-monastic-christianity--ecumenical-community-worlds-taize-and-iona` | influenced | Inferential-Thin | new | insular-irish-monastic-christianity legacy ('Iona has a working religious community again'); ecumenical-community-worlds-taize-and-iona relationsSummary ('Iona literally… |
| `british-welsh-christianity--insular-irish-monastic-christianity` | influenced | Documented | new | british-welsh-christianity relationsSummary, as rewritten in prose change 3 (the old text said only 'distinct from Irish Christianity') |
| `anglo-saxon-christianity--british-welsh-christianity` | in contact with | Documented | new | british-welsh-christianity relationsSummary ('older than the Gregorian mission it later met; rejected Augustine's authority'), longDescription ('When Augustine of Canter… |
| `anglo-saxon-christianity--british-welsh-christianity--2` | argued against | Documented | new | british-welsh-christianity longDescription ('they declined to accept his authority or to join his mission to the Saxons') and why ('keeping their own dating of Easter'):… |
| `british-welsh-christianity--anglo-saxon-christianity` | influenced | Documented | new | british-welsh-christianity legacy ('Gildas's account ... reaching Bede') |
| `british-welsh-christianity--medieval-welsh-christianity` | continued as | Documented | new | british-welsh-christianity legacy, as rewritten in prose change 4 ('The Welsh church carried on under its own bishops after 768'); medieval-welsh-christianity why ('Wale… |
| `nicene-visigothic-iberia--gothic-and-vandal-homoian-christianity` | argued against | Documented | new | nicene-visigothic-iberia relationsSummary ('The Homoian kingdom that crossed to Nicaea from inside'), longDescription and why (Reccared brought the Gothic bishops with h… |
| `nicene-visigothic-iberia--mozarabic-christianity` | continued as | Documented | new | nicene-visigothic-iberia legacy ('The same institution continued under Muslim rule as the Mozarabic Christianity of al-Andalus'; 'Its liturgy went with it'); mozarabic-c… |
| `anglo-saxon-christianity--insular-irish-monastic-christianity` | argued against | Documented | new | insular-irish-monastic-christianity longDescription ('at Whitby in 664 the Northumbrian king ruled against the Irish reckoning'); anglo-saxon-christianity longDescriptio… |

Two links are named in no era-3 row: `byzantine-imperial-church-justinianic--montanism-the-new-prophecy` (named by the era-1 Montanism text) and `palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza` (era 2 owns it).

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-07): items 20 and 33 closed; additions to 23 and 24; new items 34 to 40. The working list:

- R1-27 (data fields, not changed here): armenian-christianity-after-avarayr.continuesAs names bagratid-armenian-christianity and should name armenian-christianity-before-the-bagratids. armenian-christianity-before-the-bagratids has no continuesAs (should be bagratid-armenian-christianity) and its relationsSummary is empty. british-welsh-christianity has no continuesAs, although the continued-as link to medieval-welsh-christianity is drafted. The empty relationsSummary goes in Open_Gaps_Tracking.
- For Mark, A3: two Egyptian Miaphysite movements for the same years (cyrilline-miaphysite-egyptian-tradition, era 2, and cyrilline-miaphysite-egyptian-christianity, era 3). This is a portfolio and census-structure question, already marked needs-ruling in the corpus-map dossier.
- For Mark, A4: none of the six link types means 'in communion with'. The Aksum-Alexandria and Egypt-Syriac Orthodox cases show the need. Until he rules, they are held as 'in contact with' at the grade their evidence supports.
- For Mark, B1 and D1, as one ruling: present-day and monument facts with no vendored text are left standing. They are the Lenten reading of the Ladder, Dorotheus as standard reading, Mar Saba and Saint Catherine's still inhabited, Monte Cassino bombed in 1944, and the Ravenna buildings. The question is whether the qualify rule covers them.
- For Mark, C1: Caucasian Albania's end date (705) and the Bagratid summary ('absorbs ... after 705'). The year 705 is now gone from the Albanian prose (R1-12), but the dates field still reads 705.
- Open_Gaps_Tracking, era 2: no link joins homoian-arian-christianity to gothic-and-vandal-homoian-christianity, although both texts say the second descends from the first (D2).
- Open_Gaps_Tracking, era 4: no continued-as link from insular-irish-monastic-christianity to medieval-irish-christianity (E2).
- Open_Gaps_Tracking: Sebeos's 'catholicos de Géorgie et d'Albanie' on Chalcedon's side c. 614 (C3). Wants: Thomson's Sebeos (1999).
- The anglo-saxon-christianity longDescription also names Whitby. That movement has no rows in this era's inventory, so whoever owns it should cite the new Whitby link in its disposition.
- Wants carried forward: the Book of Letters (Dvin 554); Alfred's preface to the Pastoral Care in Sweet's EETS edition; a Cluniac customary or Cluny's foundation charter (D3). These go through the source-research thread.
- Era 2 (handoff): the published link palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza has the internal phrase 'No text we hold' in its note. Proposed: 'No source from the time ties the later monks to the earlier, so this rests on place and sequence alone.' Era 2 owns the link (round 2, R2-05; round 3, R3-01).

## Merge notes

- byzantine-imperial-church-justinianic--cyrilline-miaphysite-egyptian-christianity: drafted by A and B; B kept (two-sided note), with A's Evagrius locus correction and John of Ephesus source added.
- cyrilline-miaphysite-egyptian-christianity--syriac-orthodox-west-syriac-christianity (in contact with): drafted by A and B; B kept: the exchanged letters of communion (Pseudo-Zachariah IX.23-24) show the contact directly; A's History of the Patriarchs evidence is later and Egyptian-only.
- byzantine-imperial-church-justinianic--nubian-christianity (in contact with): drafted by B and A; A kept: same John of Ephesus passages; A's note states the single partisan witness and the king's written answer.
- latin-africa-under-byzantium--byzantine-imperial-church-justinianic (argued against): drafted by B and A; A kept: the movement is group A's, and its note carries Reparatus's deposition as well as the 550 letters.
- roman-church-gregorian--byzantine-imperial-church-justinianic (argued against): drafted by B and D; D kept (identical keep; the movement is group D's).

## Wanted texts (would let a link be graded higher)

- A Chalcedonian-side account of the 540s embassy, if any survives; John of Biclarum (s.a. 569, Mommsen line 19834) records only that the Makurians 'accepted the faith of Christ'.
- A Georgian or Greek text of c. 600 recording the Georgian church's acceptance of Chalcedon
- A Georgian-side text recording the break (Brosset says the Georgian annals pass over it)
- A Latin or English text of the Disputation with Pyrrhus with a clean Latin column (PG 91 OCR is unreadable in Greek), to quote its African setting.
- A Life of a Scetis abbot from 451-642, or Zachariah Rhetor read for the Egyptian monks' refusal of Chalcedon, to document the desert monasteries' role from inside the window.
- A clean edition (ACO ser. 2, vol. 1, Riedinger) of the Lateran acts of 649, to replace the long-s Welter OCR.
- A clean edition of Victor of Tunnuna's Chronicle (Mommsen OCR is rough).
- A clean edition of Victor of Tunnuna's Chronicle (the Mommsen OCR reads 'lustiniano', 'inipetitus', 'assensimi').
- A clean edition of Victor of Tunnuna's Chronicle; the vendored MGH text is rough OCR ('Romanuni', 'triuni', 'sechidunt' for 'Romanum', 'trium', 'secludunt').
- A clean edition of the Annales Cambriae (the Rolls Series OCR is rough), or the Harleian text in Phillimore's edition
- A clean edition or translation of Sebeos (Thomson 1999 is in copyright; Patkanian's Armenian 1879) to replace Macler's OCR
- A cleaner Annales Cambriae and a cleaner Chronicle of 754
- A dated witness to the Armenian translation of Timothy Aelurus's Refutation, or the Armenian Book of Letters (Girk' T'ght'ots), to show Egyptian anti-Chalcedonian texts reaching Armenia in 451-554.
- A primary text dated between 554 and 600 that names the catholicos at Dvin by name (e.g. the Book of Letters, Girk' T'łt'oc')
- A public-domain English of the Toledo III acts (none exists, per the file header); the NPNF II.14 Filioque excursus renders only the creed decree
- A public-domain English or a cleaner Latin of the Chronicle of 754 (Lopez Pereira's edition is in copyright)
- A repo-cited modern work on the Rule of the Master's priority over Benedict's Rule (e.g. RB 1980, named in the Benedictine dossier but not read)
- A repo-cited modern work on the Typikon of Saint Sabas in later Orthodox worship, if the stronger legacy claim is to come back.
- A repo-cited secondary work on the Georgian lectionary and Jerusalem worship (none found in the repo)
- A repo-cited secondary work on the penitentials and the rise of private, repeatable confession (McNeill and Gamer 1938, after its renewal check, would serve)
- A seventh- or eighth-century text showing the Aksumite church's clergy after 615.
- A source for the Welsh bishops' professions of obedience to Canterbury in the twelfth century (for example Eadmer, Historia novorum, or Gerald of Wales, De invectionibus)
- A text from inside 451-642 (e.g. a Life of a Scetis abbot, or Zachariah Rhetor on the Egyptian monks' refusal of Chalcedon, read for the purpose) naming the desert monasteries as the anti-Chalcedonian party's base.
- A text from the seventh or eighth century showing the Aksumite church's bishops or clergy after 615 (none vendored).
- A text giving Novel 42's date in its own words; the year 536 rests on the editor's apparatus (the law is preserved in the acts of the Constantinople council of 536, file line 56024), so the note leaves the year out.
- A text showing the Nubian church itself between 652 and 697 (e.g. the Faras bishop list in a vendored edition); none vendored.
- A vendored English or clean Greek text of Dorotheus's Instructions; PG 88 is two-column Greek-Latin OCR.
- A vendored primary text placing Sergius in office both before and after 622 (e.g. the Chronicon Paschale on the coronation of 610, or Theophanes), which would let this be Documented.
- A vendored source for Dongola and the year 652 of the Baqt (e.g. al-Maqrizi's Khitat on the Baqt, or Welsby 2002 read and cited by page).
- A vendored text of Ibn Ishaq's account (via Ibn Hisham) of the first Muslim emigration to Aksum, to restore the 615 sentence as fact rather than tradition.
- A vendored text tying the Kerala Christians of 849-1054 to the Persian church before 651 (e.g. Ishoyahb III's letter on the metropolitan of Rev-Ardashir and India, or the Chronicle of Seert on bishops sent to India).
- ACO ser. 2, vol. 1 (Riedinger), the Lateran acts of 649, to replace the long-s Mansi X OCR for the African letters of 646.
- Agnellus of Ravenna, Liber pontificalis ecclesiae Ravennatis (MGH SRL, 1878): for the Gothic churches of Ravenna, their reconsecration and the altered palace mosaic
- Aldhelm's letter to Geraint of Dumnonia on the British Easter
- Aldhelm's letter to Geruntius (Geraint), king of Dumnonia, on the British Easter and tonsure, which is the book Bede means
- Alfred's prose preface to the Pastoral Care, in Sweet's EETS edition (1871, public domain), which would make this Documented
- Alfred's prose preface to the Pastoral Care, in Sweet's EETS edition (1871, public domain): would make the Gregory-to-Alfred link Documented
- An earlier witness to John of the Sedre's patriarchate across the conquest (e.g. the Syriac account of his colloquy with the emir, or the Chronicle of 1234), so the continuity does not rest on a twelfth-century chronicle alone.
- Antiochus Strategos, The Capture of Jerusalem (614), in a vendored translation (e.g. Conybeare 1910), for 'the survivors wrote down what had been lost'.
- Any text from 451-615 naming a bishop of Aksum consecrated by Alexandria.
- Any text of 451-615 naming a bishop of Aksum consecrated by Alexandria, or stating Aksum's stand on Chalcedon.
- Bernard's or Ulrich's customary of Cluny (Ordo Cluniacensis), which Hunter Blair cites
- Boniface's letter to Pope Zacharias of 742 in a full edition (Tangl 1916, or Emerton's English), and the Clausula de unctione Pippini in full (MGH SRM 1)
- Boniface's letter to Zacharias in a full vendored edition (Tangl 1916, or Emerton's English), rather than through the capitulary headnote
- Cluny's foundation charter of 909/910 (Bruel, Recueil des chartes de l'abbaye de Cluny I, 1876, public domain), or a Cluniac customary: would document the Benedictine-to-Cluny link
- Cluny's foundation charter of 909/910, which places the house under the Rule of Saint Benedict (Bruel, Recueil des chartes de l'abbaye de Cluny I, 1876, public domain)
- Columbanus, Letter II to the Gallic synod and Letter V to Boniface IV (Latin, MGH Epp. III, Gundlach), not located; the letter to the Gallic bishops is the fuller record of the Easter dispute in Gaul
- Columbanus, Letters II and V (MGH Epp. III, Gundlach), not located
- Cyril of Scythopolis, Life of Sabas, for Sabas's own embassies to Anastasius and Justinian and the Origenist split at the New Laura (only the Life of Euthymius is vendored).
- Cyril of Scythopolis, Life of Sabas, in a vendored edition (Sabas's embassies to Constantinople; the Origenist split at the New Laura).
- Early Cistercian documents (Exordium parvum, Carta caritatis) in a public-domain edition, for 'the Cistercians' in the Benedictine legacy
- Ewald-Hartmann, Gregorii I Registrum epistolarum tomus I (Books I-VII, 1891): with the vendored tomus II, to check the 'more than 850 letters' count
- For Italy: a vendored text on the Gothic church's end after 554 (e.g. Agnellus, Liber pontificalis ecclesiae Ravennatis, on the reconsecration of the Gothic churches)
- George MacLeod's own writings on the founding of the Iona Community, or Ferguson 1988, vendored or verified, to show what the community claimed from Columba
- George MacLeod's writings, or Ferguson 1988 verified, for the Iona Community's claim on Columba
- Giorgi Merchule, Life of Grigol of Khandzta, in a public-domain edition (e.g. Marr 1911), to show the revival from inside the Georgian church
- Gippert, Schulze, Aleksidze and Mahé, The Caucasian Albanian Palimpsests of Mount Sinai (2008), read for the 1996 identification and the Udi connection (in copyright; named in the Albania dossier)
- Gregory the Great's Register XIII.47-50 (603) on the Spanish depositions, read in the vendored Latin, if the 'doing wrong' wording for Spain is to stand on Gregory's own words
- Ishoyahb III's letters (ed. Duval, CSCO), for the catholicate across the conquest in his own words.
- John Catholicos (Hovhannes Draskhanakerttsi), History of Armenia, in Saint-Martin's French (1841), for the same event
- John Catholicos (Hovhannes Draskhanakerttsi), History of Armenia, in a public-domain translation (e.g. Saint-Martin's French, 1841), to show the catholicate across the 880s in one narrative
- John of Beth Aphthonia's or Zacharias's Life of Severus (vendored, Syriac with French, Kugener 1903) read for Severus's own years in Egypt and his death there; not checked in this pass.
- Jonas, Life of Columban, Book II (Council of Macon; Luxeuil under Eustasius), in English or a vendored Latin (MGH SRG 37)
- Jonas, Life of Columban, Book II (the Council of Macon, 626/7, and Luxeuil under Eustasius), which would show the Frankish church debating and adopting the rule; the Munro translation covers Book I only
- Kartlis Tskhovreba for the seventh and eighth centuries in a readable vendored translation
- Kekelidze's 1912 Russian edition of the Georgian Jerusalem lectionary (public domain by date), or any public-domain edition, vendored
- Lang, Lives and Legends of the Georgian Saints (1956), or any edition of the Martyrdom of Shushanik, for the husband's apostasy and the date (in copyright)
- Leo of Ostia, Chronicle of Monte Cassino (MGH SS 7): for the Saracen destruction of 883
- Michael the Syrian, Chronicle (Chabot), book X: the Peter of Callinicus-Damian schism and the 616 reunion, to give the Syriac side of the break the History of the Patriarchs records.
- Movses Dasxuranci, History of the Caucasian Albanians, Book III (the deposition of Nerses Bakur), in a vendored edition
- Movses Dasxuranci, History of the Caucasian Albanians, in a usable edition (Dowsett 1961 is in copyright)
- Munro-Hay (1991), Phillipson (2012) and Welsby (2002) read and cited by page, before the two 'continued as' links from Aksum and Nubia can be checked against them.
- Stephen H. Rapp Jr., The Sasanian World through Georgian Eyes (2014), read for the 609-780 gap
- Tacitus, Agricola 24, or another vendored text stating that Ireland lay outside the Roman Empire
- The Book of Letters (Girk' T'łt'oc'), for the acts and signatures of the council of Dvin of 506
- The Book of Letters (Girk' T'łt'oc'), for the council of Dvin of 506
- The Book of Letters (Girk' T'łt'oc'), the Abraham-Kiwrion correspondence, in a readable translation
- The Book of Letters (Girk' T'łt'oc'), the acts and letters of the council of Dvin of 554, in a readable translation (Garsoian 1999 translates the key documents; in copyright)
- The Book of Letters (Girk' T'łt'oc'), which holds Elias's letters on the affair
- The Carolingian councils of 813 (MGH Concilia aevi Karolini I, Werminghoff 1906) and the Aachen capitularies of 816-817: would document the Pastoral Rule and Rule of Benedict legislation directly
- The Clausula de unctione Pippini in full (MGH SRM 1, p. 465)
- The Faras bishop list, or another text of the Nubian church between 652 and 697, in a vendored edition.
- The Gildas fragments as cited by Columbanus, and the Irish catalogue of saints that names him, to show the wider Irish reception the corpus map flags as needs-ruling
- The Martyrium Arethae (Greek acts of the Najran martyrs), which Moberg (1924) says has Timothy of Alexandria urging the Aksumite king to war.
- The Martyrium Arethae (Greek acts of the Najran martyrs), which Moberg says describes Timothy of Alexandria urging the Aksumite king to war; not vendored.
- The Xi'an stele of 781 in a reliable translation of its Syriac lines, which name the catholicos; the vendored copy (Malech 1910, after Kircher) renders the name as 'John Joshua'.
- The canons of the Aachen councils of 816-817 (Benedict of Aniane's reform), for the empire-wide imposition itself
- The councils of 813 (Mainz preface; Reims II c. 10; Tours III c. 3; Chalon II c. 1) in MGH Concilia aevi Karolini I (Werminghoff, 1906), to document the legislation directly
- The letter of the council of Carthage of 535 (Reparatus) on Arian clergy, in a vendored edition.
- The letter of the council of Carthage of 535 (Reparatus) on receiving Arian clergy, in a vendored edition; the Source Readiness Dossier places it in the Collectio Avellana, but I did not find it in the vendored pars I.
- Ukhtanes of Edessa, History of the Separation of the Georgians from the Armenians, in Brosset's French translation (1870, public domain by date), which Brosset's 1876 note cites
- Volker L. Menze, Justinian and the Making of the Syrian Orthodox Church (2008), read and cited by page (still wanted from era 1).
