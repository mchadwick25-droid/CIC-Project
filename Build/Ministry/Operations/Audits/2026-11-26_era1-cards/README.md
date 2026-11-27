# Era 1 cards — batch README

**ON HOLD (Mark, 2026-11-26, verbatim: "when it finishes, lets hold we are at 98% now").** Work resumes after Friday's 2:00 pm reset, from this README, when Mark says. No pull request is open. To resume: read `Header.md` (every ruling), then step 2a below; the next action is the era 1 people (2b), in batches of three, using the same writer prompt as writers D and E (role `card.md`, models in this folder, faults in `Card_Check_*.md`), then an independent check F, then the checker's exact changes applied word for word (`Applied.md`). Done so far: all 20 traditions (14 released in #1829, 6 waiting for the next release); the person, council, era, story, connection and river first-set cards.

Owner: the one era 1 cards thread (coordinator session `session_01JMNsSDxiDjhkPh1K48BmfL`). Rule and scope: `Header.md` in this folder. Branch: `claude/built-world-short-descriptions-v2`.

## Step

1. **First set for Mark** (one card of each of eight kinds; table in `Header.md`). Written (`<id>.layout.json`, `Card_Edits_<id>.md`), checked (`Card_Check_A.md`, `Card_Check_B.md`), exact changes applied word for word (`Applied.md`), evidence gathered and every quote re-found at its lines (`Evidence.json`, 231 of 231). Page sent to the coordinator 2026-11-26: https://claude.ai/artifact/CVzArtefSKCkoRRyC23ZfB (built by `build_first_set_page.py`). **Approved** (Mark, 2026-11-26: "yes, but let say church in conversation world instead of built world"; Decision-Log).
2. The rest of era 1, kind by kind, on the approved cards (same process: one write, one independent check by a hand that wrote none, the checker's exact changes applied word for word, `Evidence.json` with every quote re-found by script). No public "world" anywhere a visitor or Mark reads: "Christian Tradition", and "Church in Conversation Tradition" for the eleven built ones (Decision-Log, 2026-11-26). Internal names stay. Work order and state, updated after each card:
   - **2a. Traditions** (20 in era 1; Bardaisanites, modalist Monarchianism and Danubian Latin get cards built from what is held, brief kept as it stands): Montanism and Alexandria done. post-apostolic-house-church, syriac-edessa-nisibis, latin-pastoral-congregational-christianity: done (written, `Card_Check_C.md`, 26 changes applied verbatim, `Applied.md` "Check C"; `tools/quote_scan_readings.json` gained Latin's two scan readings; census copy validates 0 errors). greek-apologists-second-century, latin-apologists, apocryphal-and-pseudepigraphal-literature: done (`Card_Check_D.md`, 15 changes applied verbatim, `Applied.md` "Check D", census copy 0 errors). marcion-marcionism, valentinian-and-other-gnostic-christianities, manichaeism: done (`Card_Check_E.md`, 15 applied verbatim; N4, Manichaeism's held `uncertain` "staged debate", left for release). ebionite-nazoraean-current, novatianism, anatolian-church-third-century: done (Mark: "do Ebionites, Novatianism and Antolian church"; `Card_Check_F.md`, 17 applied verbatim; the Ebionite drop entry added to `tools/quote_scan_readings.json`; census copy 0 errors). 14 of 20 done. palestinian-church-pre-constantinian, roman-church-third-century, antiochene-church-third-century: done (Mark: "go ahead, do Palestinian, Roman and Antiochene"; `Card_Check_G.md`, 20 applied verbatim; both Antiochene scan readings added to `tools/quote_scan_readings.json`; census copy 0 errors). 17 of 20 done. danubian-latin-christianity, modalist-monarchianism, bardaisanite-current: done (Mark: "go ahead, do Danubian, Monarchianism and Bardaisanites"; `Card_Check_H.md`, 14 applied verbatim; D6 and B6, two `modernWorks` notes, left for release). **All 20 traditions done.** Six (Palestinian, Roman, Antiochene, Danubian, Modalist, Bardaisanite) are checked but not yet in the census: they go in the next release. Next, when Mark says: the people (2b). danubian-latin-christianity, modalist-monarchianism, bardaisanite-current. Then greek-apologists-second-century, latin-apologists, apocryphal-and-pseudepigraphal-literature, marcion-marcionism, valentinian-and-other-gnostic-christianities, manichaeism, ebionite-nazoraean-current, novatianism, anatolian-church-third-century, antiochene-church-third-century, palestinian-church-pre-constantinian, roman-church-third-century, danubian-latin-christianity, modalist-monarchianism, bardaisanite-current. Batch-11 folders hold sheets and held fields for the twelve it rebuilt.
   - **2b. People** (28 in era 1, all of them, from the briefs they have now): Polycarp done.
   - **2c. Council** (1): done.
   - **2d. Era 1**: done.
   - **2e. Stories** (26 documented stories on era 1 entries, plus the map stories in era 1): one done.
   - **2f. Connections** (82 edges touching an era 1 entry): one done.
   - **2g. Rivers** (6 in era 1: Origin, Syriac East & Asia, Greek East & Orthodoxy, Africa, Latin West & Catholicism, Non-Nicene Traditions): Africa done.
   - **2h. Existing-text fixes** flagged in `Applied.md` (story text, connection note, council fields, river origin record): to apply by the same process, worded by a checker.
3. Site code (look: the live `cft-website/` design, dark screen, fonts, colors and card styling as they stand; never the review page's styling; Mark, 2026-11-26): branch `claude/built-world-short-descriptions` handed over (coordinator, 2026-11-26) and merged into this branch at its head 9711baa7. Still to build: a field home, validator keys, atlas-sync carriage, map open functions, MENU_ORDER folds, tree pages and tests for story, connection and river cards; `timeline` for rivers. Two phone tests in `Build/tools/tree_map_view.test.mjs` already fail on main.
4. Release: part 1 (Mark, "1", 2026-11-26): the 14 traditions, Polycarp, the councils of 251 and era 1 written into the census by `release_part1.py`, with the two public "world" lines (Alexandria's `livingEvidence.basis` and its search-names row, Desert's `sourcing`); validator 0 errors, atlas-check 0 changes, tree build 0 mismatched. The rest of era 1 goes in a later pull request.
   - **Part 1 merged** to `main` as pull request #1829 (merge 14c09882, 2026-11-26), every CI check green after three CI fixes: the census job now fetches the texts that entry and era `quotationOriginals` and `briefSources` cite; `corpus-coverage.json` regenerated for the Katharoi name; the card layout test plants faults only on traditions with no layout fields; and two "Saviour" lines became "Savior". `live` (www.churchfamilytree.com) is unchanged until Mark promotes `main` through the promotion runbook.

## Cards

| Card | Kind | Step |
|---|---|---|
| montanism-the-new-prophecy | tradition | checked, fixes applied, shown to Mark |
| alexandria-catechetical | Church in Conversation Tradition | checked, fixes applied, shown to Mark (short description drafted in `Build/Ministry/Features/Church-Family-Tree/Short-Descriptions/2026-11-26_built-worlds-v2/Drafts_A.md`) |
| polycarp-of-smyrna | person | checked, fixes applied, shown to Mark |
| councils-of-rome-and-carthage-251 | council | checked, fixes applied, shown to Mark |
| era-1 | era | checked, fixes applied, shown to Mark |
| The Sister Who Saw Visions During the Service | story | checked, fixes applied, shown to Mark |
| post-apostolic-house-church--montanism-the-new-prophecy | connection | checked, fixes applied, shown to Mark |
| river-africa | river | checked, fixes applied, shown to Mark |

Short descriptions also drafted, unchecked: post-apostolic-house-church and syriac-edessa-nisibis (same Drafts_A.md). The halted 12-built-worlds task's records are in `Short-Descriptions/2026-11-26_built-worlds-v2/`.

## Open items

- Public "world" sweep (Decision-Log 2026-11-26): fixed the four map card strings in `cft-website/index.html` ("This world's sources", "No further orientation content recorded for this world yet.", "This world's fuller record could not be loaded", "Loading this world's fuller record…" now say "tradition"), and the Africa river card's legacy line. Still in the census, for the era 1 release: `alexandria-catechetical` `livingEvidence.basis` "The world built from this entry names the Coptic…", and one field reading "the next richest built world's 37". "Throughout the world" and similar ordinary uses, and quotations, stay.

- First set, left open by the checks: Polycarp's timeline references need file and lines added (P3, minor); the existing texts flagged for a fix (story text, connection note, council fields, river origin record; listed in `Applied.md`) are not changed until Mark rules; shown dates for Alexandria ("c. 180 to 4th c.") and Polycarp ("2nd c.") are proposed, not applied.

- Syriac's shown end date 410 is given as a Widely Accepted event, with no held line opened (Drafts_A.md).
- Open-Gaps 429 (years no source gives), 428 (where a tradition's card lives), 437, 438, 410 and 422 (connection notes and map stories, hold lifted for era 1).
- Two phone tests already fail on main (card site build thread's note).

## Mark's rulings in this batch

All are quoted verbatim in `Header.md`: the short-description rulings, and the widened scope of 2026-11-26.

## Library gaps (for the era 1 Library thread)

**Sections with nothing held**
- The Sister Who Saw Visions (Tertullian, On the Soul 9), Legacy and today: no later old writer found who keeps or quotes the passage.
- Era 1, Legacy and today: waits for the era brief.
- Polycarp: no documented story of his own; no `modernWorks`.
- Councils of 251: no documented story told under them; no `modernWorks`.
- Africa river: no river leaves it in era 1.

**Claims flagged as unsourced or modern**
- Story text ("The Sister Who Saw Visions"): "the charge of disorder", "She does not interrupt", "elders", "valued", "one of the very few descriptions… not the frenzy"; the rendering "tender and lucid…" (not the held English); census date "c. 207–212".
- Connection note (House Church → Montanism): "about 192" (translator's footnote); "the faithful" (the hostile writer's word, in the narrator's voice).
- Africa river origin record: "first seen clearly".
- Councils of 251: three council fields with Hefele's dates or views; the African bishops' letter granting peace has no old year (Hefele gives 252).
- Polycarp: `teaser` and `sourcing` carry modern years (c. 110-155).

**Years no old source gives**
- Alexandria: 150 and 400 (shown "c. 180 to 4th c.").
- Syriac: 410 for the synod of Seleucia-Ctesiphon (the acts give Yazdegerd's 11th year; 410 is Chabot's reckoning).
- Latin Pastoral: the 240s (Cyprian's election rests on modern reckoning; shown "250 to 430").
- Open-Gaps 429's list: Latin Apologists `end` 320 and the years 205 and 250; Apocryphal c. 100-900; Marcionism `start` 140; Ebionites dates, start, end and region; Greek Apologists 124.
- Montanism: the start (Gratus's proconsulship has no held year; Epiphanius gives about the 19th year of Antoninus Pius).

## Newly held (Library thread, 2026-11-26, PR #1828, branch `source-research/era1-library`)

Record: `Build/Ministry/Operations/Audits/2026-11-26_era1-library/README.md`. Every AD year from a regnal or Seleucid year is a conversion: say so on the card.
- Jerome's Chronicle (`cic/texts/jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`): Quadratus and Aristides to Hadrian, Hadrian year 9-10 (42531-42534); Justin, Antoninus year 4 (42752-42754); Valentinus and Cerdo at Rome under Hyginus, Antoninus year 3 (42747-42750, Cerdo, not Marcion); Montanism begins, Marcus year 11 (43052-43055), against Epiphanius, Panarion 48.1, about Antoninus year 19 (`epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 17019): the two disagree; Polycarp martyred, Marcus year 6-7 (42977-42979); Alexandria's teachers (43267, 43374-43377, 43456, 43485, 43699-43702, 43741); Tertullian famous, Severus year 16 (43480-43482); Cyprian's plague, Novatus, letters, martyrdom in Valerian year 3 (43965-44192), no election year.
- Epiphanius, Panarion 29-30 (`epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`): Ebionites' places (25026-25031), "after the capture of Jerusalem" (25334-25343), spread (26876-26879); no end year. Marcion, heresies 41-42 (Holl 1922, 7149, 7418-7423).
- Syriac end: Synodicon Orientale, Chabot 1902, French, synod of Mar Isaac 16074-17925, "En la 11e année du règne de Yezdegerd" at 16155; Chronicon Edessenum, Guidi's Latin (`chronica-minora-pars-prior-versio-lat_guidi1903.txt`) from 542.
- The anonymous writer against the Montanists: his own clue, HE V.16.19 (npnf201 29886-29889), "more than thirteen years since the woman died"; "about 192" is McGiffert's reckoning from it.
- Cyprian, Letters 43, 57, 59 and Pontius: all in Hartel (`cyprian_epistulae-lat_hartel1871-csel3-tei.txt`); Letter 57 gives no AD year.
- Polycarp's stories already held: Irenaeus, Against Heresies III.3.4 (anf01); Eusebius HE IV.14, V.20, V.24 (npnf201).
- Not found by the Library: years for Minucius (205) and Commodian (250); Gratus's proconsulship; a later keeper of On the Soul 9; old bounds for Alexandria and the Africa river.
- Also new (Open-Gaps 415): Chrysostom, Homily 50 on Matthew in Greek (Field 1839); Jerome, Letter 51 in Latin (Hilberg).
- Modern works that reckon the years (Modern works only, never content; Library README section 5): 252, Hefele, History of the Councils I (1872), `hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt` 6506; Cyprian's election June 248 to April 249, Benson, Cyprian (1897), `benson_cyprian-his-life-his-times-his-work_1897.txt` about 4284-4290; 410, Chabot 1902 from Yazdegerd's accession in 399, Synodicon line 16427. Minucius 205 and Commodian 250 are no modern work's single year (Monceaux 1901, Harnack 1904, Dombart 1887 give disputed ranges): leave them off the cards.
