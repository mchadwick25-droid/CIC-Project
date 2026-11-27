# Applied card-check changes (2026-11-26)

Source: `Card_Check_A.md`, `Card_Check_B.md`. Each change was applied word for word to the card's `<id>.layout.json`. All eight files still load (`python3 -m json.tool`). Nothing committed.

## Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| montanism-the-new-prophecy | M1 | shortDescription |
| montanism-the-new-prophecy | M2 | timeline, period 5, line 2, text (Firmilian) |
| montanism-the-new-prophecy | M3 | timeline, period 7, line 1, text (Sozomen II.32) |
| montanism-the-new-prophecy | M4 | timeline, period 3, headline |
| montanism-the-new-prophecy | M5 | timeline, period 1, headline |
| montanism-the-new-prophecy | M6 | timeline, period 6, line 4, text (Epiphanius) |
| montanism-the-new-prophecy | M7 | timeline, period 4, line 6, text (On the Soul) |
| montanism-the-new-prophecy | M8 | timeline, period 7, lines 2 and 3 (VII.18, VII.19), when |
| alexandria-catechetical | A1 | shortDescription (added as first key) |
| alexandria-catechetical | A2 | timeline, period 9, line 1, note |
| alexandria-catechetical | A3 | timeline, period 9, headline |
| alexandria-catechetical | A5 | timeline, period 4, when |
| alexandria-catechetical | A6 | timeline, period 4, line 6, text (Porphyry) |
| polycarp-of-smyrna | P1 | timeline, period 3, line 11: text changed, note added |
| polycarp-of-smyrna | P2 | uncertain: item 13 removed |
| polycarp-of-smyrna | P3 (only the Martyrdom 9 example, as worded) | timeline, period 3, line 7 ("Martyrdom of Polycarp 9"), reference |
| councils-of-rome-and-carthage-251 | C1 | shortDescription |
| councils-of-rome-and-carthage-251 | C2 | timeline, period 6 last line text; period 2 Novatian line text |
| councils-of-rome-and-carthage-251 | C3 | timeline, period 2 Novatian line, note |
| councils-of-rome-and-carthage-251 | C4 | timeline, period 5, Maximus line, text |
| councils-of-rome-and-carthage-251 | C5 | timeline, period 5, synodal letter line, note |
| councils-of-rome-and-carthage-251 | C6 | briefSources, Hartel letters, title |
| era-1 | E1 | shortDescription |
| era-1 | E2 | timeline, period 1, headline |
| era-1 | E3 | timeline, period 3, Decius line, text |
| era-1 | E4 | timeline, period 5, 303 line, text and reference |
| era-1 | E5 | timeline, period 3, Dionysius line: when changed, line moved before the "250" Decius line |
| era-1 | E6 | uncertain, item 4 |
| the-sister-who-saw-visions-during-the-service | S1 | shortDescription |
| the-sister-who-saw-visions-during-the-service | S2 | dates |
| the-sister-who-saw-visions-during-the-service | S3 | timeline, period 1, "on one occasion" line, text |
| post-apostolic-house-church--montanism-the-new-prophecy | K1 | shortDescription |
| post-apostolic-house-church--montanism-the-new-prophecy | K2 | legacyAndToday, item 2 |
| post-apostolic-house-church--montanism-the-new-prophecy | K3 | timeline, period 1, Ardabau line, text |
| river-africa | R1 | shortDescription |
| river-africa | R2 | dates |
| river-africa | R3 | timeline, period 6, Peter's death line: when, reference, note removed |
| river-africa | R4 | timeline, period 4, Dionysius line, when |

## For existing texts, not applied here (card, finding, the exact change as the checker gave it)

**councils-of-rome-and-carthage-251** (Entry fields, "Items flagged for a fix in existing texts")

- `modernWorks` move: the two Hefele items in `council.sources.writtenLater` move to `modernWorks` word for word, each with a `note` saying what it covers (for example "A nineteenth-century history of the councils; its volume 1 covers these councils" and "The French edition with Leclercq's notes, on Cyprian, the Novatians and the baptism quarrel").
- `council.issue` item 3. Old: "At Carthage, the deacon Felicissimus and five presbyters had broken with Cyprian. Charles Joseph Hefele, the historian of the councils, says the party took up the charge that the bishop was too strict with the lapsed." New: "At Carthage, the deacon Felicissimus and five presbyters had broken with Cyprian. Cyprian says they offered the lapsed a false peace, telling them to leave off their prayers, and he called it another persecution (Cyprian, Letter to the people of Carthage)."
- `council.outcome` item 1. Old: "The next year, by Hefele's dating, the African bishops offered peace to all the lapsed who had kept on repenting, because a new persecution seemed near." New: "In a letter that gives no year, the African bishops offered peace to all the lapsed who had kept on repenting, because a new persecution seemed near (Cyprian and the African bishops, synodal letter to Cornelius)."
- `council.outcome` item 5. Old: "By Hefele's account, Novatian's party at Carthage then put a bishop, Maximus, at its head, and the lax party was given the presbyter Fortunatus as its bishop. Cyprian, who is our witness, calls Fortunatus a false bishop set up by a few (Cyprian, Letter to Cornelius on Fortunatus and Felicissimus)." New: "Cyprian writes that the lax party at Carthage had the presbyter Fortunatus, one of the five, as its bishop, and that Novatian's party is said to have made the presbyter Maximus its bishop. He calls Fortunatus a false bishop set up by a few (Cyprian, Letter to Cornelius on Fortunatus and Felicissimus)."
- `council.attended` item 1. Old: "At Carthage, \"a large number of bishops,\" Cyprian writes; Hefele adds some presbyters and deacons. No list of their names is held." New: "At Carthage, \"a large number of bishops,\" Cyprian writes. No list of their names is held."
- `council.record` item 1 note. Old: "Cyprian says the heads of the decisions were collected in a little book. It is lost. Henri Leclercq, in his edition of Hefele: nothing of this council remains." New: "Cyprian says the heads of the decisions were collected in a little book. It is lost."
- `council.record` item 4 note. Old: "Written by about 439. The fullest statement of Novatian's own rule, which he reports from Novatian's letters. A. C. Zenos, who edited him in English, finds him favorable to the Novatians." New: "Written by about 439. The fullest statement of Novatian's own rule, which he reports from Novatian's letters."
- `briefReferences` item 11. Old: "Hefele, History of the Councils I: Felicissimus as deacon; the dates of the councils and of the year after." New: "Cyprian, Letter to Cornelius (Letter 52 in Hartel's Latin; Letter 48 in the English): Felicissimus made a deacon."

**the-sister-who-saw-visions-during-the-service** (story text and teaser, census)

- Text: "she reads hearts" generalizes "some men's hearts she understands". Suggested: "she reads some people's hearts".
- Story `teaser`. Suggested: "In Carthage a woman receives revelations in church, reports them after the people have gone, and then submits them to be examined."
- Items 1 to 9 of the story-text list were confirmed at their lines, with no new wording given.

**post-apostolic-house-church--montanism-the-new-prophecy** (edge, census)

- Edge `note`: "the faithful of Asia". Suggested: "Christians of Asia".
- Edge `outcome`: "Meetings of the faithful across Asia". Suggested: "Meetings of Christians across Asia".

**polycarp-of-smyrna** (census `card.datesNote`)

- P4. New `card.datesNote`: "No ancient source gives a year for his birth or his death. His church's account dates his death to a great Sabbath, the second day of the month Xanthicus, and gives no year. Irenaeus says he was at Rome when Anicetus was bishop there, and Eusebius and Jerome put his death in the reign of Marcus Aurelius. The second century comes from the modern dating of those reigns." (The layout has no `datesNote`; this is the census card's existing field.)

**river-africa**: the origin record is the census record; the checker proposes no change to it.

## Could not place (card, finding, why)

- alexandria-catechetical, A4 (`dates` "c. 180 to 4th c."): the layout has no `dates` field. The change is to the census `dates` and to Drafts_A.md's line, neither of which is in this folder's layout.
- polycarp-of-smyrna, P3 (every other timeline reference): the checker says to append ", cic/texts/<file> lines <n>" from "that row's file and lines" in Card_Edits. Most lines have several rows, so the choice of file and lines is not given. Only the one example worded in full (Martyrdom 9) was applied.
- polycarp-of-smyrna, P3 (line 2, Ignatius from Smyrna): the extra reference "; Eusebius, Church History III.36.4-5, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 19945-19962" is to be added after the line's own appended reference, which is not given. Not applied.
- Card_Check_A, note "not a card change" (Card_Edits shows ANF03 47250-47251 as "On Monogamy"; it is On the Resurrection of the Flesh): the error is in Card_Edits prose, not in any layout.json. Not applied.

## Check C

Source: `Card_Check_C.md`. Each change was applied word for word to the card's `<id>.layout.json` (and L10 to `tools/quote_scan_readings.json`). The three layouts and the tools file still load as JSON. A scratch census copy with the three layouts merged in (`/tmp/claude-0/apply-c/census-copy.json`; the real census was not edited), run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (the four standing shortName warnings). Nothing committed. Line numbers are the checker's (before S3 and L11 changed the counts).

### Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| post-apostolic-house-church | PA1 | shortDescription |
| post-apostolic-house-church | PA2 | timeline, line 40 (Hegesippus): when, text, reference |
| post-apostolic-house-church | PA3 | timeline, period 7 when; line 38 note and reference |
| post-apostolic-house-church | PA4 | timeline, period 7 headline; line 32 text |
| post-apostolic-house-church | PA5 | timeline, line 41, when |
| post-apostolic-house-church | PA6 | timeline, line 24, text |
| post-apostolic-house-church | PA7 | timeline, period 10 headline |
| syriac-edessa-nisibis | S1 | timeline, line 4, note |
| syriac-edessa-nisibis | S2 | timeline, line 6, text |
| syriac-edessa-nisibis | S3 | timeline, line 7 removed |
| syriac-edessa-nisibis | S4 | shortDescription |
| syriac-edessa-nisibis | S5 | timeline, period 1, witness |
| syriac-edessa-nisibis | S6 | timeline, lines 18 and 19, text |
| syriac-edessa-nisibis | S7 | timeline, line 32: text, reference |
| syriac-edessa-nisibis | S8 | timeline, line 35, text |
| syriac-edessa-nisibis | S9 | dates; period 8 when; line 30 when and reference |
| latin-pastoral-congregational-christianity | L1 | shortDescription |
| latin-pastoral-congregational-christianity | L2 | timeline, line 2: text, note added, reference |
| latin-pastoral-congregational-christianity | L3 | timeline, line 9, text |
| latin-pastoral-congregational-christianity | L4 | timeline, period 3, when |
| latin-pastoral-congregational-christianity | L5 | timeline, line 22, when |
| latin-pastoral-congregational-christianity | L6 | timeline, line 30, text |
| latin-pastoral-congregational-christianity | L7 | timeline, line 39, text |
| latin-pastoral-congregational-christianity | L8 | timeline, line 52, reference |
| latin-pastoral-congregational-christianity | L9 | timeline, period 10 headline |
| latin-pastoral-congregational-christianity | L10 | `tools/quote_scan_readings.json`: two entries added as in Card_Edits, `kind` "OCR misread margin line number run into the line" |
| latin-pastoral-congregational-christianity | L11 | dates; period 1 when and headline; new first line of period 1 |

### For existing census texts, not applied here

None. Card_Check_C gives no change to a census text. The census `dates` of the three entries ("70–200 CE", "200–410 CE", "c. 240s-430") were not touched; the layouts carry the card's own `dates`.

### Could not place

None.

## Check D

Source: `Card_Check_D.md`. Each change was applied word for word to the card's `<id>.layout.json`. The three layouts still load as JSON. A scratch census copy with the three layouts merged in (`/tmp/claude-0/apply-d/census-copy.json`; the real census was not edited), run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (the four standing shortName warnings). Nothing committed. Line numbers are the checker's.

### Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| greek-apologists-second-century | G1 | timeline, line 37 (Tatian), text |
| greek-apologists-second-century | G2 | timeline, line 6: when, reference |
| greek-apologists-second-century | G3 | timeline, line 7, note |
| greek-apologists-second-century | G4 | timeline, line 17, text |
| greek-apologists-second-century | G5 | timeline, line 31, note removed |
| greek-apologists-second-century | G6 | timeline, period 5 when; line 32: when, reference |
| greek-apologists-second-century | G7 | timeline, line 42, reference |
| greek-apologists-second-century | G8 | timeline, line 45, reference |
| latin-apologists | L1 | shortDescription |
| latin-apologists | L2 | timeline, period 4: when, headline |
| latin-apologists | L3 | timeline, line 12, note |
| apocryphal-and-pseudepigraphal-literature | P1 | timeline, period 1, when |
| apocryphal-and-pseudepigraphal-literature | P2 | timeline, line 17, text |
| apocryphal-and-pseudepigraphal-literature | P3 | timeline, line 2, text |
| apocryphal-and-pseudepigraphal-literature | P4 | timeline, line 27, reference |

### For existing census texts, not applied here

None. Card_Check_D gives no change to a census text.

### Could not place

None. G9 gives no change to a card (record only, in `Card_Edits_greek-apologists-second-century.md`, rows 7 and 8 "verbatim" cells swapped); not applied.

## Check E

Source: `Card_Check_E.md`. Each change was applied word for word to the card's `<id>.layout.json`. The three layouts still load as JSON. A scratch census copy with the three layouts merged in (`/tmp/claude-0/apply-e/census-copy.json`; the real census was not edited), run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (the four standing shortName warnings). Nothing committed. Line numbers are the checker's.

### Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| marcion-marcionism | M1 | timeline, line 11, text |
| marcion-marcionism | M2 | timeline, line 25, text |
| marcion-marcionism | M3 | timeline, line 34, text |
| marcion-marcionism | M4 | timeline, line 31: when, reference |
| valentinian-and-other-gnostic-christianities | V1 | uncertain, item 3 |
| valentinian-and-other-gnostic-christianities | V2 | timeline, period 2, when |
| valentinian-and-other-gnostic-christianities | V3 | timeline, period 1, headline |
| valentinian-and-other-gnostic-christianities | V4 | timeline, line 13, text |
| valentinian-and-other-gnostic-christianities | V5 | timeline, line 14, text |
| valentinian-and-other-gnostic-christianities | V6 | timeline, line 15, text |
| valentinian-and-other-gnostic-christianities | V7 | timeline, line 26, when |
| valentinian-and-other-gnostic-christianities | V8 | timeline, line 28, text |
| manichaeism | N1 | dates |
| manichaeism | N2 | timeline, line 10, text |
| manichaeism | N3 | timeline, line 33, text |

### For existing census texts, not applied here

- N4 (manichaeism, `uncertain` item 5, tail "The Acts of Archelaus, a staged debate of the 300s, ..."): left for the release, which applies it with the census field and the batch-11 card's copy.

### Could not place

None.

## Check F

Source: `Card_Check_F.md`. Each change was applied word for word to the card's `<id>.layout.json`; the drop entry was added as given to `tools/quote_scan_readings.json`. All files still load as JSON. A scratch census copy with the three layouts merged in (`/tmp/claude-0/apply-f/census-copy.json`; the real census was not edited), run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (the four standing shortName warnings). Nothing committed. Finding numbers are the checker's.

### Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| ebionite-nazoraean-current | E1 | timeline, period 4, line 2: when |
| ebionite-nazoraean-current | E1 | timeline, period 4, line 3: when, reference |
| ebionite-nazoraean-current | E2 | timeline, period 4, line 6: reference |
| ebionite-nazoraean-current | E3 | timeline, period 2, line 1: text |
| ebionite-nazoraean-current | E4 | timeline, period 7, line 2: reference |
| ebionite-nazoraean-current | E5 | timeline, period 1: headline |
| ebionite-nazoraean-current | drop entry | `tools/quote_scan_readings.json`, new reading for `augustine_epistulae-1-123-lat_goldbacher-csel34.txt` lines 23238-23271 |
| novatianism | N1 | timeline, period 1, line 1: text |
| novatianism | N2 | timeline, period 1, line 1: reference |
| novatianism | N2 | timeline, period 2, line 6: reference |
| novatianism | N3 | uncertain, item 2 |
| novatianism | N4 | uncertain, item 5 |
| novatianism | N5 | timeline, period 5: headline |
| novatianism | N6 | timeline, period 6, line 1: text |
| anatolian-church-third-century | A1 | shortDescription |
| anatolian-church-third-century | A2 | timeline, period 1, line 2: reference |
| anatolian-church-third-century | A3 | timeline, period 3, line 6: text |
| anatolian-church-third-century | A4 | timeline, period 4, line 5: when |

### For existing census texts, not applied here

None. (The checker's "marked, not edited" notes on `start` and `end` are not findings.)

### Could not place

None.

## Check G

Source: `Card_Check_G.md`. Each change was applied word for word to the card's `<id>.layout.json`; the two scan readings were added as given to `tools/quote_scan_readings.json` (the check names no change to them). All files still load as JSON. A scratch census copy with the three layouts merged in (`/tmp/claude-0/apply-g/census-copy.json`; the real census was not edited), run with `node tools/validate-census.mjs`: 0 errors, 4 warnings (the four standing shortName warnings). Nothing committed. Finding numbers are the checker's.

### Applied (card, finding, field)

| Card | Finding | Field |
|---|---|---|
| palestinian-church-pre-constantinian | P1 | shortDescription |
| palestinian-church-pre-constantinian | P2 | timeline, period 4, line 30: text |
| palestinian-church-pre-constantinian | P3 | timeline, period 4: headline |
| palestinian-church-pre-constantinian | P4 | timeline, period 4, line 32: text |
| palestinian-church-pre-constantinian | P5 | timeline, period 3: when |
| palestinian-church-pre-constantinian | P6 | timeline, period 3, line 20: text |
| palestinian-church-pre-constantinian | P7 | timeline, period 2, line 15: text, reference |
| palestinian-church-pre-constantinian | P8 | timeline, period 2, line 12: reference |
| palestinian-church-pre-constantinian | P9 | reference spacing, lines 17, 25, 27, 29, 32 (12 and 15 are covered by P8 and P7) |
| palestinian-church-pre-constantinian | P10 | uncertain, item 3 |
| roman-church-third-century | R1 | timeline, period 2, line 10: text, reference |
| roman-church-third-century | R2 | timeline, period 6, line 2: when, reference |
| roman-church-third-century | R3 | timeline, period 6, line 3: note (new), reference |
| roman-church-third-century | R4 | timeline, period 1, line 6: text |
| roman-church-third-century | R5 | reference spacing, lines 3, 7, 12, 48, 52 (10 is covered by R1) |
| antiochene-church-third-century | A1 | shortDescription |
| antiochene-church-third-century | A2 | timeline, period 7, line 8: text, reference |
| antiochene-church-third-century | A3 | timeline, period 4, line 1: text |
| antiochene-church-third-century | A4 | timeline, period 2, line 1: reference |
| antiochene-church-third-century | A5 | reference spacing, lines 36, 42, 43 (44 is covered by A2) |
| antiochene-church-third-century | scan readings | `tools/quote_scan_readings.json`: Eusebius Schwartz-Mommsen line 11897, Epiphanius Oehler line 45745 (drop) |

### For existing census texts, not applied here

None.

### Could not place

None. One count differs from the checker's: the P9 and R5 lists name eight double-spaced references each, but the files hold seven (Palestinian; line 18 has none) and six (Roman). All that exist were fixed.
