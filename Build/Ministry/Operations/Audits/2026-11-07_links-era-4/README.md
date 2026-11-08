# Church Family Tree links, era 4 (P2-L4) — 2026-11-07

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Eras 1 and 2 (`../2026-11-07_links-era-1/`, `../2026-11-07_links-era-2/`) were the precedent, and their wanted-texts lists were checked first. The Philocalia ruling (Decision-Log, "The Philocalia's compilers", 2026-11-07) was kept; no era-4 link touches it.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 25 movements, 264 named relationships, no raw movement IDs in reader text. Three movements (medieval Irish, medieval Welsh, the Abbasid Church of the East) are one-line stubs.
2. **Draft** (Opus, five groups of five movements, each drafter scoring its own prose and notes): `Draft_GroupA.json` to `Draft_GroupE.json`, merged in `Drafting_Record.json`. The drafters added the named relationships the inventory missed; each disposition's reason says so. Three links were drafted twice; the merge notes say which draft was kept and why. While drafting ran, the era 3 pass merged (data release 7) and published 9 links with the same IDs as era-4 drafts. Each is kept as era 3 published it; the era-4 draft is filed under `superseded_draft` in the record.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 7 substantial, 11 minor, no fabrication. Every quote verbatim. The substantial findings: the Anglo-Saxon text still called itself the Carolingian reform's parent; four Slavic and Rus' links used a 1549 retelling (Herberstein) as a primary, two of them at a higher grade than the other two; the St Thomas continuation showed only the later side; a Benedictine link whose sources did not touch it; a Contested note that settled its own dispute; a Paulician note that used a source against itself; and a Scandinavian continuation that claimed an unbroken line across Denmark's break of 1536-37.
4. **Revision** (Opus): `Revision_Round1.json`. All 18 findings fixed: 11 links rewritten, 2 regraded, 1 removed (`early-benedictine-italian-monasticism--late-anglo-saxon-christianity`, never published), 12 prose changes. On three findings the reviser improved on the proposed fix and said why (R1-03, R1-11, R1-14): the post-1580 Malabar chronicle was not used as a primary, and the canon of Patriarch Theodosius (853-858) carries the St Thomas links instead.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 3 minor. The two wording fixes (the Uppsala council of 1530; Maximus and Heraclius's compromise) were applied as written. The third asked for two source rules to be written down; they are below and in Open-Gaps.

Two of the three-round cap used.

### Two source rules applied in this era

Neither changes the method; both reviewers agreed. Logged for Mark and for P2-L11 in Open-Gaps, "Two source rules applied in era 4" (2026-11-08).

- A retelling written centuries later is not a primary for the events it retells. Herberstein (1549), the Kyiv Synopsis (1674) and the Malabar chronicle (after 1580) are listed as secondary sources for ninth- and tenth-century events.
- A canon's own text carried in a later collection counts as a primary. The canon of Theodosius (853-858), in Assemani's printing, is graded Widely Accepted, not Documented, because it reaches us only in Latin translation.

## Counts

- Links touching an era-4 movement: 68 (41 new, 0 changed, 27 kept). No link retired; every published ID stands.
- Census links in all: 225 before, 266 after. Data release 8 (2026-11-08). Release 7 was era 3 (mchadwick25-droid/CIC-Project#1540).
- Grades of the new links: Documented 18, Widely Accepted 5, Dominant Modern Reconstruction 12, Contested 2, Inferential-Thin 4.
- Types of the new links: continued as 17, influenced 9, gave rise to 6, argued against 5, in contact with 4.
- Dispositions of the named relationships (drafting): link 120, no-entry 121, qualify 17, out-of-scope 13, remove 1. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 30 fields changed. Every scored field reaches Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (`Readability_Scores.json`); 22 of them scored below 60 before. One, the nine-word iconophile summary, is too short to score. 17 sit below FK grade 8, which the scorer reports but does not fail. All 41 new link notes also score Reading Ease 60 or more.
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines. The validator collapses whitespace but does not join hyphen breaks, so quotes keep printed hyphens and OCR errors exactly as the files print them; each is noted in that link's `drafter_flags`.

## Two-way check

### Prose to links

Every relationship named in an era-4 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it belongs to another era's movement whose own text names it (per-relationship record: `Drafting_Record.json`, `dispositions`). Round 1 found the one gap that mattered: the Anglo-Saxon text still claimed descent where the link says influence. It was fixed in revision. The three stubs name their continuation only through their dates (each starts where its earlier entry ends).

- Medieval Irish Christianity: 1 named (1 link).
- Medieval Welsh Christianity: 1 named (1 link).
- The Church of the East on the Silk Road: 11 named (8 link, 3 no-entry).
- The Church of the East under the Abbasids: 2 named (2 link).
- Melkite Arabic Christianity: 14 named (6 link, 2 out-of-scope, 5 no-entry, 1 qualify).
- Coptic Christianity under Early Islam: 11 named (2 link, 2 out-of-scope, 7 no-entry).
- Anglo-Saxon Christianity: 16 named (1 qualify, 12 link, 3 no-entry).
- Carolingian Reform Christianity: 10 named (4 link, 1 qualify, 5 no-entry).
- Iconophile Byzantine Monasticism: 12 named (1 no-entry, 2 qualify, 9 link).
- Cyrillo-Methodian Slavic Christianity: 13 named (4 link, 9 no-entry).
- Kievan Rus' Christianity: 8 named (4 link, 4 no-entry).
- Mozarabic Christianity: 15 named (2 link, 12 no-entry, 1 qualify).
- Cluniac Reform Monasticism: 12 named (4 qualify, 8 no-entry).
- St. Thomas Christians of India: 7 named (1 qualify, 3 link, 2 no-entry, 1 out-of-scope).
- Paulicians: 14 named (11 link, 3 no-entry).
- Bogomils: 12 named (5 link, 4 no-entry, 3 out-of-scope).
- Scandinavian Conversion Christianity: 14 named (1 qualify, 10 no-entry, 3 link).
- The Byzantine Imperial Church (Heraclian & Iconoclast Eras): 13 named (9 no-entry, 4 link).
- The Byzantine Imperial Church (Macedonian Era): 19 named (9 no-entry, 10 link).
- Bagratid Armenian Christianity: 10 named (1 out-of-scope, 6 no-entry, 2 qualify, 1 link).
- Syriac Orthodox Christianity under Islam: 12 named (6 no-entry, 1 remove, 3 link, 2 out-of-scope).
- Makurian Nubian Christianity: 7 named (4 no-entry, 3 link).
- Late Anglo-Saxon Christianity: 14 named (9 no-entry, 4 link, 1 qualify).
- Georgian Revival — Tao-Klarjeti and Athos: 10 named (7 link, 1 no-entry, 2 qualify).
- Post-Aksumite Ethiopian Christianity: 14 named (11 link, 2 out-of-scope, 1 no-entry).

### Links to prose

Each link touching an era-4 movement, and where era-4 text names it. A dash means the link is named in the other movement's own text, by an earlier era's pass. Twelve of those were published by era 3 while this era drafted. Each was checked against the era-4 prose as it now reads, and none contradicts it. Cluny's summary now says only that it kept the Rule of Benedict, which fits era 3's Benedictine link.

- `desert-monasticism--iconophile-byzantine-monasticism` (influenced, Inferential-Thin; earlier): Iconophile Byzantine Monasticism relationsSummary
- `desert-monasticism--coptic-christianity-under-early-islam` (influenced, Documented; earlier): —
- `coptic-christianity-under-early-islam--alexandria-catechetical` (argued against, Documented; earlier): —
- `roman-church-gregorian--anglo-saxon-christianity` (gave rise to, Documented; earlier): Anglo-Saxon Christianity longDescription; Anglo-Saxon Christianity why
- `insular-irish-monastic-christianity--anglo-saxon-christianity` (gave rise to, Documented; earlier): Anglo-Saxon Christianity longDescription; Anglo-Saxon Christianity why
- `anatolian-church-third-century--byzantine-imperial-church-heraclian-iconoclast` (influenced, Documented; earlier): —
- `cyrilline-miaphysite-egyptian-christianity--coptic-christianity-under-early-islam` (continued as, Documented; earlier): Coptic Christianity under Early Islam relationsSummary
- `aksumite-christianity--post-aksumite-ethiopian-christianity` (continued as, Widely Accepted; earlier): Post-Aksumite Ethiopian Christianity relationsSummary; Post-Aksumite Ethiopian Christianity longDescription; Post-Aksumite Ethiopian Christianity why
- `nubian-christianity--makurian-nubian-christianity` (continued as, Widely Accepted; earlier): —
- `latin-africa-under-byzantium--byzantine-imperial-church-heraclian-iconoclast` (argued against, Documented; earlier): —
- `syriac-orthodox-west-syriac-christianity--syriac-orthodox-under-islam` (continued as, Documented; earlier): Syriac Orthodox Christianity under Islam longDescription
- `byzantine-imperial-church-justinianic--byzantine-imperial-church-heraclian-iconoclast` (continued as, Documented; earlier): —
- `the-church-of-the-east-under-persia--the-church-of-the-east-on-the-silk-road` (continued as, Documented; earlier): The Church of the East on the Silk Road relationsSummary; The Church of the East on the Silk Road longDescription
- `the-church-of-the-east-under-persia--st-thomas-christians-of-india` (influenced, Inferential-Thin; earlier): —
- `armenian-christianity-before-the-bagratids--bagratid-armenian-christianity` (continued as, Widely Accepted; earlier): —
- `georgian-christianity--georgian-revival-tao-klarjeti` (continued as, Widely Accepted; earlier): —
- `early-benedictine-italian-monasticism--carolingian-reform-christianity` (influenced, Documented; earlier): —
- `early-benedictine-italian-monasticism--cluniac-reform-monasticism` (influenced, Dominant Modern Reconstruction; earlier): —
- `roman-church-gregorian--carolingian-reform-christianity` (influenced, Widely Accepted; earlier): —
- `roman-church-gregorian--late-anglo-saxon-christianity` (influenced, Dominant Modern Reconstruction; earlier): Late Anglo-Saxon Christianity longDescription
- `merovingian-gallic-christianity--carolingian-reform-christianity` (continued as, Widely Accepted; earlier): Carolingian Reform Christianity relationsSummary
- `anglo-saxon-christianity--british-welsh-christianity` (in contact with, Documented; earlier): —
- `anglo-saxon-christianity--british-welsh-christianity--2` (argued against, Documented; earlier): —
- `british-welsh-christianity--anglo-saxon-christianity` (influenced, Documented; earlier): —
- `british-welsh-christianity--medieval-welsh-christianity` (continued as, Documented; earlier): Medieval Welsh Christianity why
- `nicene-visigothic-iberia--mozarabic-christianity` (continued as, Documented; earlier): Mozarabic Christianity relationsSummary; Mozarabic Christianity longDescription
- `anglo-saxon-christianity--insular-irish-monastic-christianity` (argued against, Documented; earlier): Anglo-Saxon Christianity relationsSummary; Anglo-Saxon Christianity longDescription; Anglo-Saxon Christianity why
- `insular-irish-monastic-christianity--medieval-irish-christianity` (continued as, Documented; new): Medieval Irish Christianity why
- `anglo-saxon-christianity--late-anglo-saxon-christianity` (continued as, Documented; new): Anglo-Saxon Christianity legacy
- `carolingian-reform-christianity--scandinavian-conversion-christianity` (gave rise to, Documented; new): Scandinavian Conversion Christianity relationsSummary; Scandinavian Conversion Christianity longDescription
- `late-anglo-saxon-christianity--scandinavian-conversion-christianity` (gave rise to, Inferential-Thin; new): Scandinavian Conversion Christianity relationsSummary
- `scandinavian-conversion-christianity--scandinavian-reformation-kingdoms` (continued as, Inferential-Thin; new): Scandinavian Conversion Christianity legacy
- `anglo-saxon-christianity--carolingian-reform-christianity` (influenced, Documented; new): Anglo-Saxon Christianity relationsSummary; Anglo-Saxon Christianity legacy; Carolingian Reform Christianity relationsSummary; Carolingian Reform Christianity longDescription
- `carolingian-reform-christianity--cluniac-reform-monasticism` (influenced, Inferential-Thin; new): Carolingian Reform Christianity relationsSummary; Cluniac Reform Monasticism relationsSummary
- `carolingian-reform-christianity--latin-papal-church-gregorian` (influenced, Widely Accepted; new): Carolingian Reform Christianity legacy
- `cluniac-reform-monasticism--latin-papal-church-gregorian` (in contact with, Documented; new): Cluniac Reform Monasticism legacy
- `cyrillo-methodian-slavic-christianity--kievan-rus-christianity` (influenced, Dominant Modern Reconstruction; new): Cyrillo-Methodian Slavic Christianity relationsSummary; Cyrillo-Methodian Slavic Christianity legacy; Kievan Rus' Christianity relationsSummary
- `kievan-rus-christianity--kievan-rus-christianity-1054-1240` (continued as, Dominant Modern Reconstruction; new): Kievan Rus' Christianity legacy
- `byzantine-imperial-church-heraclian-iconoclast--byzantine-imperial-church-macedonian` (continued as, Documented; new): The Byzantine Imperial Church (Heraclian & Iconoclast Eras) legacy; The Byzantine Imperial Church (Macedonian Era) longDescription
- `byzantine-imperial-church-macedonian--byzantine-church-after-1054` (continued as, Documented; new): The Byzantine Imperial Church (Macedonian Era) legacy
- `byzantine-imperial-church-heraclian-iconoclast--iconophile-byzantine-monasticism` (argued against, Documented; new): Iconophile Byzantine Monasticism longDescription; Iconophile Byzantine Monasticism why; The Byzantine Imperial Church (Heraclian & Iconoclast Eras) relationsSummary
- `iconophile-byzantine-monasticism--byzantine-imperial-church-heraclian-iconoclast` (argued against, Widely Accepted; new): Iconophile Byzantine Monasticism longDescription; The Byzantine Imperial Church (Heraclian & Iconoclast Eras) longDescription
- `iconophile-byzantine-monasticism--byzantine-imperial-church-macedonian` (influenced, Documented; new): Iconophile Byzantine Monasticism longDescription; Iconophile Byzantine Monasticism legacy
- `iconophile-byzantine-monasticism--athonite-and-comnenian-byzantine-monasticism` (continued as, Inferential-Thin; new): Iconophile Byzantine Monasticism relationsSummary; Iconophile Byzantine Monasticism legacy
- `iconophile-byzantine-monasticism--kievan-rus-christianity-1054-1240` (influenced, Dominant Modern Reconstruction; new): Iconophile Byzantine Monasticism legacy
- `byzantine-imperial-church-heraclian-iconoclast--paulicians` (argued against, Dominant Modern Reconstruction; new): Paulicians relationsSummary; Paulicians longDescription; Paulicians why
- `byzantine-imperial-church-macedonian--paulicians` (argued against, Dominant Modern Reconstruction; new): Paulicians relationsSummary; Paulicians longDescription; Paulicians why
- `paulicians--bogomils` (influenced, Contested; new): Paulicians legacy; Bogomils longDescription
- `bogomils--cathars-albigensians` (influenced, Contested; new): Bogomils relationsSummary; Bogomils why; Bogomils legacy
- `bogomils--balkan-bogomil-continuation` (continued as, Dominant Modern Reconstruction; new): Bogomils longDescription; Bogomils why; Bogomils legacy
- `byzantine-imperial-church-macedonian--cyrillo-methodian-slavic-christianity` (gave rise to, Dominant Modern Reconstruction; new): Cyrillo-Methodian Slavic Christianity relationsSummary; Cyrillo-Methodian Slavic Christianity longDescription; The Byzantine Imperial Church (Macedonian Era) relationsSummary; The Byzantine Imperial Church (Macedonian Era) legacy
- `byzantine-imperial-church-macedonian--kievan-rus-christianity` (gave rise to, Dominant Modern Reconstruction; new): Kievan Rus' Christianity longDescription; Kievan Rus' Christianity why; The Byzantine Imperial Church (Macedonian Era) longDescription; The Byzantine Imperial Church (Macedonian Era) why
- `the-church-of-the-east-on-the-silk-road--church-of-the-east-under-the-abbasids` (continued as, Documented; new): The Church of the East on the Silk Road longDescription; The Church of the East on the Silk Road why; The Church of the East on the Silk Road legacy; The Church of the East under the Abbasids why
- `church-of-the-east-under-the-abbasids--church-of-the-east-under-the-mongols` (continued as, Documented; new): The Church of the East on the Silk Road why; The Church of the East on the Silk Road legacy; The Church of the East under the Abbasids why
- `church-of-the-east-under-the-abbasids--st-thomas-christians-of-india` (in contact with, Widely Accepted; new): St. Thomas Christians of India relationsSummary; St. Thomas Christians of India longDescription; St. Thomas Christians of India why
- `st-thomas-christians-of-india--st-thomas-christians-1300-1517` (continued as, Widely Accepted; new): St. Thomas Christians of India legacy
- `chalcedonian-monasticism-judean-desert-and-gaza--melkite-arabic-christianity` (gave rise to, Dominant Modern Reconstruction; new): Melkite Arabic Christianity relationsSummary; Melkite Arabic Christianity longDescription; Melkite Arabic Christianity why
- `byzantine-imperial-church-heraclian-iconoclast--melkite-arabic-christianity` (argued against, Documented; new): Melkite Arabic Christianity longDescription; Melkite Arabic Christianity why
- `melkite-arabic-christianity--melkite-greek-catholic-church` (gave rise to, Dominant Modern Reconstruction; new): Melkite Arabic Christianity legacy
- `syriac-orthodox-under-islam--syriac-renaissance` (continued as, Documented; new): Syriac Orthodox Christianity under Islam longDescription; Syriac Orthodox Christianity under Islam legacy
- `coptic-christianity-under-early-islam--coptic-christianity-fatimid-to-mamluk` (continued as, Documented; new): Coptic Christianity under Early Islam legacy
- `coptic-christianity-under-early-islam--makurian-nubian-christianity` (influenced, Widely Accepted; new): Makurian Nubian Christianity longDescription; Makurian Nubian Christianity why
- `coptic-christianity-under-early-islam--post-aksumite-ethiopian-christianity` (in contact with, Documented; new): Post-Aksumite Ethiopian Christianity relationsSummary; Post-Aksumite Ethiopian Christianity longDescription; Post-Aksumite Ethiopian Christianity why
- `makurian-nubian-christianity--terminal-christian-nubia` (continued as, Documented; new): Makurian Nubian Christianity legacy
- `post-aksumite-ethiopian-christianity--zagwe-and-early-solomonic-ethiopian-christianity` (continued as, Documented; new): Post-Aksumite Ethiopian Christianity relationsSummary; Post-Aksumite Ethiopian Christianity longDescription; Post-Aksumite Ethiopian Christianity why; Post-Aksumite Ethiopian Christianity legacy
- `bagratid-armenian-christianity--armenian-cilicia` (continued as, Documented; new): Bagratid Armenian Christianity legacy
- `georgian-revival-tao-klarjeti--the-georgian-golden-age` (continued as, Dominant Modern Reconstruction; new): Georgian Revival — Tao-Klarjeti and Athos relationsSummary; Georgian Revival — Tao-Klarjeti and Athos legacy
- `athonite-and-comnenian-byzantine-monasticism--georgian-revival-tao-klarjeti` (in contact with, Dominant Modern Reconstruction; new): Georgian Revival — Tao-Klarjeti and Athos relationsSummary; Georgian Revival — Tao-Klarjeti and Athos longDescription; Georgian Revival — Tao-Klarjeti and Athos why; Georgian Revival — Tao-Klarjeti and Athos legacy

## Open items

Closed in this pass, in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`:
- "No 'continued as' link from the Irish monasteries to medieval Ireland" (2026-11-07).
- "Whitby in the Anglo-Saxon text" (2026-11-07).

Added to existing Open-Gaps entries (2026-11-08): "Well-known facts with no vendored source" (the late Anglo-Saxon, Scandinavian, Cluniac and Byzantine cases), "No link type for communion" (jurisdiction: the St Thomas Christians' bishops), "Caucasian Albania's end date" (the Bagratid summary held).

Logged in Open-Gaps (2026-11-08). For Mark, census-structure or method questions; none blocks this release:
- No medieval English or Scandinavian successor entry.
- Two "continues as" fields name entries the evidence only influenced (Carolingian, Cyrillo-Methodian).
- Links the sources support but no text names (Alcuin against Elipandus; the Salzburg clergy; Cluny and the Mozarabic rite).
- The Bogomil entries overlap.
- No Melkite entry between 1009 and 1724.
- Dominant Modern Reconstruction on old secondary works.
- Two source rules applied in era 4.

For entry owners:
- The Abbasid Church of the East is a stub.
- The Georgian Golden Age says "silent since 622" (era 5).
- Era-4 text outside the links pass (two broken sentences, Peter the Venerable outside the Cluny window, three dates the sources give differently).

Notes:
- Two links rest on the 754 council's curse on "Mansur", John of Damascus: the imperial church against the iconophile monks, and against the Melkite church. Round 1 held that each stands separately, because John is a named voice in both movements.
- The 1054 schism stays on `byzantine-church-after-1054`'s existing links. The Macedonian summary no longer says it "receives" the schism.

## Wanted texts

- A Danish-side source naming the Reformation superintendents in the old sees (the vendored 1537 Ordinatio ecclesiastica is in heavy long-s OCR)
- A clean edition or translation of the Annales Cambriae (the Rolls Series OCR is rough)
- A medieval list of the bishops of Skara or Lund (e.g. the Skara bishop list Anjou cites, or Scriptores rerum Suecicarum / Danicarum medii aevi)
- A modern study of Boniface and the Frankish reform synods (e.g. Levison, England and the Continent in the Eighth Century, 1946), if one is cited in the repo; none is
- A public-domain reading of the Jelling stone inscription (Harald Bluetooth's 'made the Danes Christian')
- A repo-cited modern study of the English mission to Scandinavia (none found)
- A repo-cited modern study of the tenth-century English Benedictine reform (none found)
- A vendored Irish annal (the Annals of Ulster or of Tigernach, in a public-domain edition) showing named Irish houses and their abbots on both sides of 664
- Adam of Bremen, Gesta Hammaburgensis ecclesiae pontificum (c. 1075), in a public-domain edition or translation, for the English bishops in Norway and Sweden
- Adam of Bremen, Gesta Hammaburgensis, for the sees founded before 1104
- Alcuin's letters to Bishop Higbald and to King Æthelred on the raid, located and quoted in the vendored PL 100 Latin or an English translation
- Alfred's Old English Pastoral Care with his preface (ed. H. Sweet, Early English Text Society, 1871; named in the NPNF 12 note at file line 24035), which would document this directly
- An Irish-side text on the Easter question, such as Cummian's letter De controversia paschali (c. 632), so the dispute has a voice from both sides
- Ari Þorgilsson, Íslendingabók (c. 1130), in a public-domain edition or translation, for the Althing decision of 1000
- Asser, Life of King Alfred, in a public-domain edition or translation (e.g. Stevenson 1904; Cook 1906)
- Brut y Tywysogion in a public-domain edition, for the Welsh sees after 954
- Rimbert, Life of Anskar (Vita Anskarii, c. 870), in a public-domain translation (e.g. Robinson, 1921), to document Anskar's mission from his own disciple
- Rimbert, Vita Anskarii, in a public-domain translation (e.g. C. H. Robinson, Anskar, the Apostle of the North, 1921)
- Snorri Sturluson, Heimskringla (Olaf Tryggvason's and Olaf Haraldsson's sagas), in a public-domain translation (e.g. Laing, 1844), for the English clergy with the two Olafs
- The Anglo-Saxon Chronicle (D and E texts) in a public-domain edition, for the raid on Lindisfarne and its date
- The Anglo-Saxon Chronicle in a public-domain edition (e.g. Plummer-Earle, Two of the Saxon Chronicles Parallel, 1892-99), for the raid on Lindisfarne and its date, the Viking wars, and the Danish invasions of 1013-1016
- The Annales Bertiniani entries naming Anskar and Hamburg, located in the vendored Waitz 1883 Latin (prudentius-troyes_annales-bertiniani_waitz1883.txt; not searched to a quote this pass)
- The Annales regni Francorum entry for 750/751 on Boniface anointing Pippin, in a clean text (the vendored Kurze OCR breaks the sentence across a page and its apparatus, file lines 1357 and 1446)
- The Regularis Concordia (c. 970) in a public-domain edition or translation
- Ælfric's Catholic Homilies (ed. Thorpe, 1844-46) and Wulfstan's Sermo Lupi ad Anglos (1014), in public-domain editions
- Æthelwold's Old English account of King Edgar's establishment of monasteries, or his Old English translation of the Rule
- A Cistercian foundation text (Exordium parvum or Carta caritatis) or Bernard of Clairvaux's Apologia to William of Saint-Thierry (PL 182; Eales's English, 1889-96), to document the Cistercian break with Cluny; with it the qualified Cluny sentences could be restored and a link drafted
- A Life of Clement of Ohrid (the Greek Life by Theophylact), for the schools at Ohrid and Preslav
- A public-domain text of the Cluny foundation charter (910), e.g. Henderson, Select Historical Documents (1892), already cited in Build/worlds/_cross-world/dossiers/merovingian-gallic-christianity_Source_Readiness_Dossier.md
- A repo-cited modern study of Cluny's origins (Rosenwein, Rhinoceros Bound, 1982, is named in the census sources but has not been read), which could lift this to Widely Accepted
- A repo-cited modern study of the Pseudo-Isidorian Decretals and their use by the Gregorian reformers (e.g. Fuhrmann); the ANF notice is an 1886 polemic and Mirbt gives only the identification
- A repo-cited modern work on Cluny and the Gregorian reform (the old 'Cluny made the reform' thesis and its critics), before any 'influenced' link is drafted
- A repo-cited source on Renaissance humanists' use of Carolingian minuscule, and on cathedral schools as the seed-bed of the universities, if those legacy lines are to be sourced
- A source on Cardinal Cisneros endowing the Mozarabic chapel at Toledo (Ferotin gives the 1500 missal and the chapel, not the endowment)
- Eulogius of Córdoba, Memoriale sanctorum, and Paulus Alvarus, Indiculus luminosus (PL 115 and 121), to support the martyrs' sentences
- John VIII's letter Industriae tuae (880) on the Slavonic liturgy, to support 'the pope approved the Slavonic books'
- John of Salerno, Life of Odo, and the Cluny foundation charter of 910 in a vendored edition (Sitwell 1958 is in copyright; Henderson 1892, cited in Build/worlds/_cross-world/dossiers/merovingian-gallic-christianity_Source_Readiness_Dossier.md, gives the charter), to show Berno and Odo coming to Cluny out of the reformed Frankish houses
- Odilo of Cluny's statute on All Souls and the 1041 Truce of God letter (MGH Constitutiones I), to support the Odilo sentences
- Peter the Venerable's letters or the Toledan Collection preface, to support the Qur'an translation and the shelter of Abelard
- The Cluny foundation charter (910) in a vendored edition, to document the direct papal subjection from the house's own side
- The Kyiv Caves Paterik or the Primary Chronicle (s.a. 1051) in a vendored edition, to document Ilarion's cave and Anthony's settling in it from the chronicle's own side; either would make this Documented
- The Life of Constantine and the Life of Methodius in a vendored edition (Kantor 1983 is in copyright; a public-domain translation or the Old Church Slavonic text, e.g. Lavrov or Miklosich), to document the emperor's sending of the brothers directly. With it this would be Documented.
- The Russian Primary Chronicle (Laurentian text) in a vendored edition, for the envoys' report (s.a. 987) and Vladimir's baptism (s.a. 988) in the chronicle's own words
- A clean edition of Nikephoros Kallistos's Enarratio (the PG 147 Latin and Greek OCR is badly garbled)
- Anna Comnena, Alexiad XV (Reifferscheid 1884, or Dawes's English of 1928) and Euthymius Zigabenus on the trial of Basil, for the Bogomil name carried into Constantinople c. 1100
- Cerularius's own synodal edict of July 1054 (in C. Will, Acta et scripta, 1861), for the see's own side in 1054
- Cerularius's synodal edict of 1054 and the 1965 joint declaration of Paul VI and Athenagoras, if the macedonian legacy's 1965 sentence is to be sourced
- Conybeare, The Key of Truth (1898), for the Paulician legacy's sentence on it
- Cosmas the Priest, Sermon against the Heretics, in a readable public-domain edition (Popruzhenko, 1907); Rački quotes it only in OCR-damaged Church Slavonic
- Euthymius Zigabenus, Panoplia dogmatica tit. 27 / Narratio de Bogomilis (Gieseler, 1842), for the medieval writers who tie the Bogomils to the Paulicians
- Genesios or Theophanes Continuatus (Bonn, 1834/1838) for the fall of Tephrike in 878; no vendored text dates it
- Life of Stephen the Younger (Greek in PG 100, or another public-domain edition), for the 765 martyrdom both texts name
- Patriarch Nicephorus, Antirrhetici (PG 100)
- Peter of Sicily, Historia Manichaeorum (Gieseler 1846 / PG 104), and Photius, Contra Manichaeos (PG 102), for the polemic in the church's own words
- Peter of Sicily, Historia Manichaeorum (Gieseler, 1846), for the planned mission from Tephrike to Bulgaria in his own words
- Peter of Sicily, Historia Manichaeorum (Gieseler, 1846, or PG 104), the principal Greek account
- Photius, Homily 17 (on the apse mosaic of Hagia Sophia, 867) in a public-domain edition, for the macedonian text's 'imposters ... had now been answered'
- Rainerius Sacconi, Summa de Catharis in a modern edition (Dondaine 1939) or an English translation (Wakefield and Evans 1969, if it clears rights); the vendored witness is Rački's 1869 reprint with variants in brackets
- Symeon the New Theologian's Life by Niketas Stethatos (Hausherr 1928, if public domain), for Symeon's own Stoudite training
- The Lives of Constantine and of Methodius (Old Church Slavonic; e.g. Pastrnek 1902, or Miklosich), for the embassy of 862 and the emperor's choice of the brothers
- The Russian Primary Chronicle (Laurentian text, PSRL vol. 1) or the Kievan Caves Paterik / Nestor's Life of Theodosius in a public-domain edition; with it this could be Documented
- The Russian Primary Chronicle (Laurentian text, PSRL vol. 1, 1846 or 1926) for Vladimir's baptism at Cherson and the Greek clergy
- The Synodikon of Orthodoxy (843) in a public-domain text, for the feast and the restoring synod from the church's own side
- Theodore the Studite, Letters (Fatouros 1992 is not public domain; PG 99 is), for his beatings, imprisonment and exiles
- Theodore the Studite, letters or Antirrhetici in a public-domain edition (PG 99), for a monk writing against the iconoclast emperors by name; would lift this to Documented
- Theophanes, Chronographia (de Boor, 1883), for Constantine V's measures against the monks
- Theophanes, Chronographia (de Boor, 1883), for Michael I's measures against the Paulicians and Constantine V's transfer of them to Thrace
- Typikon of Athanasios the Athonite and his Life (P. Meyer, Die Haupturkunden für die Geschichte der Athosklöster, 1894), for the Stoudite rule on Athos
- An English translation of the Xi'an stele (Legge 1888 or Saeki 1916/1937, if public domain), to quote the arrival in 'the ninth year of Zhenguan' (635) and the edict of toleration; the vendored Assemani Latin and the Budge and Bar Hebraeus editors' notes give 636
- An edition and translation of the Tarisappalli (Kollam) copper plates with the modern dating to c. 849, so the bishop's name and the grant can be quoted from the plates and not from Mingana's 1926 reading (he dates them about 824)
- Any text from 1054-1300 naming the Christians of Kollam or Malabar, or a bishop sent to them
- The Greek Life of John of Damascus, or another early text placing him at the laura of Sabas
- John of Damascus, On the Divine Images (Allies 1898, named in NPNF 14), to document his argument against the iconoclast emperors from his own side
- The acts of the Second Council of Nicaea (787), session 7 acclamations (Mansi XIII), if the legacy is to say again that the council honored John of Damascus by name
- Theodore Abu Qurrah's works in a vendored translation, for the 'mixed audience of Christians and Muslims' claim
- A text of the Melkite patriarchs of Antioch between 1009 and 1724 (patriarchal list or chronicle), to show the see continuing to the 1724 split
- A source for the Ethiopian church's own patriarchate in 1959 (repeated from the era-2 wants), if the post-Aksumite legacy's closing sentence is to stay sourced
- A vendored text or repo-cited study on the Georgian Balavariani and Euthymius of Athos as the source of the Greek Barlaam and Josaphat, to lift the 'may have'
- A vendored text placing Georgian monks on Sinai and at the Black Mountain near Antioch before 1000
- Any dated text naming a bishop of Aksum or Ethiopia between 615 and 900, to show the see itself on the later side of the Aksum split
- George the Hagiorite, Life of John and Euthymius, and Actes d'Iviron I (Lefort et al., 1985), both named in the census's own story sources, in a vendored or read edition, to document Iviron's founding from its own side
- Giorgi Merchule, Life of Grigol of Khandzta, in a vendored edition (Lang 1956 is in copyright; named in the census's own story sources)
- History of the Patriarchs, Part II (Evetts's later volumes, or the Atiya-Abd al-Masih-Burmester edition), for the ninth- to eleventh-century patriarchs' dealings with Ethiopia and Nubia, including the bishops they sent
- Matthew of Edessa's complete Chronicle (Dulaurier's 1858 French, public domain), for the 1045 annexation and the catholicoi between Peter and Gregory III; the vendored RHC volume gives only extracts
- Old Nubian texts in an edition whose own letters are quotable (the vendored Griffith OCR garbles the Old Nubian), to show the Coptic letters from the texts themselves
- Stephen H. Rapp Jr., Studies in Medieval Georgian Historiography (2003), named in the census's own story sources, read and cited by page
- Stephen of Taron (Asoghik), Universal History III, in a vendored edition (Dulaurier's 1883 French or Macler's 1917 French, both public domain; Greenwood 2017 is named in the census's own story sources), for Trdat's repair of the dome of Hagia Sophia
- Tamara Grdzelidze, Georgian Monks on Mount Athos (2009), named in the census's own story sources, read and cited by page
- The Georgian Annals themselves (Kartlis Tskhovreba) in a vendored translation: the vendored Brosset file holds only his introduction, charters and index, not the chronicle text
- The Anglo-Saxon Chronicle (s.a. 964) in a vendored edition
- A medieval list of the bishops of Skara (Scriptores rerum Suecicarum medii aevi)
- A vendored source for Norway's and Iceland's sees across the Reformation
