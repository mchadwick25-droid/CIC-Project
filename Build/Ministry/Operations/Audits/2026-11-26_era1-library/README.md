# Library for the era 1 cards, 2026-11-26

Mark, 2026-11-26: "go ahead and let the library fill in what it needs for era 1". This session fills the
source gaps the era 1 cards need. No model spend; no census, card or brief edits; nothing promoted to `live`.
One pull request into `main`, branch `source-research/era1-library`. The Open-Gaps entry is 440 (439 is
taken on the cards branch, `claude/built-world-short-descriptions-v2`).

## Inputs

- The cards thread's README, "Library gaps" (`Build/Ministry/Operations/Audits/2026-11-26_era1-cards/README.md`
  on its branch). The thread was asked for its current list at the start; no reply had come when the work was done.
- Open-Gaps 429 (timeline years no source gives) and 415 (originals not held for two reference quotes).
- `WANTS-REGISTER.md`: its era 1 rows are modern studies (Fahey, Godoy), out of the rights window. None taken.

## 1. Held, not shelved: now shelved (no download)

**Jerome's Chronicle** (`jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`), held since 2026-10-17 and
shelved only to fourth-century entries. It dates era 1 events by regnal year. The AD year is a conversion,
and manuscripts sometimes place an entry a year apart; Fotheringham's apparatus gives them. Seven new rows, all `context`:

| entry | entry in the Chronicle | regnal year | file lines |
|---|---|---|---|
| greek-apologists-second-century | Quadratus and Aristides give books to Hadrian; Justin; Melito; Apollinaris; Tatian | Hadrian 9-10; Antoninus 4; Marcus 10 | 42531-42534, 42752-42754, 43036-43042, 43059 |
| marcion-marcionism | Valentinus and Cerdo, Marcion's teacher, come to Rome under Hyginus | Antoninus 3 | 42747-42750 |
| montanism-the-new-prophecy | the Phrygian prophecy begins, Montanus, Priscilla, Maximilla | Marcus 11 | 43052-43055 |
| post-apostolic-house-church | Papias, Polycarp, Ignatius; Polycarp and Pionius martyred in Asia | Marcus 6-7 | 42163-42166, 42977-42979 |
| alexandria-catechetical | Demetrius; Clement and Pantaenus; Leonides and Origen; Heraclas; Origen to Caesarea | Commodus to Alexander Severus | 43267, 43374-43377, 43456, 43485, 43699-43702, 43741 |
| latin-apologists | Tertullian famous in all the churches | Severus 16 | 43480-43482 |
| latin-pastoral-congregational-christianity | the plague and On Mortality; Novatus at Rome; Cyprian's letters; Cyprian's martyrdom | Decius to Valerian 3 | 43965-43967, 43969, 43981, 44192 |

**Epiphanius, Panarion, in Holl's Greek** (both volumes held). Three new rows, `context`:

| entry | heresy | what it gives | file lines |
|---|---|---|---|
| marcion-marcionism | 41 Cerdonians, 42 Marcionites | Marcion's origin in Pontus, his coming to Rome | 7149, 7418-7423 (Holl 1922) |
| montanism-the-new-prophecy | 48 Phrygians | its rise "about the nineteenth year of Antoninus Pius" (48.1.2): this differs from the Chronicle's date | 16486, 17007-17019 (Holl 1922) |
| ebionite-nazoraean-current | 29 Nazoraeans, 30 Ebionites | places: Beroea in Coele-Syria, Pella, Kokaba in Basanitis; then Nabataea, Paneas, Moabitis, Cyprus, Asia, Rome. Start after the fall of Jerusalem; no end year | 24391, 25026-25031, 25227, 25334-25343, 26876-26879 (Holl 1915) |

## 2. Vendored (Open-Gaps 415)

| file | what it supports | rights | OCR |
|---|---|---|---|
| `cic/texts/john-chrysostom_homiliae-in-matthaeum-t2-hom-45-90-grc_field1839.txt` | the Greek of Homily 50 on Matthew, the John Chrysostom reference's E1 quote ("golden souls"); file lines 3792-3823 | pd-us-by-date, 1839; host PD Mark | Greek good to fair; Latin unusable. Google preamble, 55 lines, removed as a host addition |
| `cic/texts/jerome_epistulae-1-70-lat_hilberg-csel54-1910.txt` | Letter 51, Epiphanius to John of Jerusalem in Jerome's Latin, the Epiphanius reference's E9 and E10 quotes; file line 19873 on | pd-us-by-date, 1910; host NOT_IN_COPYRIGHT | Latin good; reproduced whole |

Epiphanius's Greek of Letter 51 does not survive; Jerome's Latin is the oldest form. Both came from
archive.org: metadata read, title page read in the OCR, passage found, djvu.txt fetched, byte count equal to the
listed size. REGISTRY rows, queue rows and staging rows are added; the merge ran valid.

## 3. Gaps checked and not fillable from an old source

- **Latin Apologists 205 (Minucius Felix) and 250 (Commodian):** neither is in the Chronicle. Jerome, Lives 58
  (npnf203), names Minucius and the Octavius with no year; the "196?" beside it is the editor's. No held old
  source gives either year.
- **Latin Pastoral, the 240s (Cyprian's election):** the Chronicle and Pontius date his martyrdom, not his
  election. No old year found.
- **Councils of 251, the African bishops' letter (Hefele's 252):** Cyprian's letters are held and give no year.
- **Syriac 410:** the Synodicon (Chabot 1902, held) gives Yazdegerd's eleventh year. That is an old regnal date,
  and the AD figure is a conversion. Nothing to fetch.
- **Alexandria 150 and 400; Apocryphal c. 100-900; Latin Apologists `end` 320:** these are span bounds, not events. The new
  Chronicle rows give Alexandria's dated events. No source gives a bound.
- **The Sister Who Saw Visions, a later witness:** not searched this session; no candidate known.
- **Polycarp's own story:** held already, not newly found: Irenaeus, Against Heresies III.3.4 (anf01), and
  Eusebius, History IV.14, V.20 and V.24 (npnf201). These are for the cards thread to use.

No item blocked automated download.

## 4. After the cards thread's list (it arrived during the work)

Two held files were shelved to `syriac-edessa-nisibis`, for its end year:
- the Synodicon Orientale (Chabot 1902): the synod of Mar Isaac, file lines 16074-17925, "En la 11e année du
  règne de Yezdegerd" at 16155 (`context`; 410 is a conversion);
- the Chronicon Edessenum in Guidi's Latin (Chronica minora I, 1903), from file line 542, dated by the Seleucid era
  (`tradition`; the English, Cowper's, was already shelved).

The rest of the list was checked against what is held:
- Cyprian's Letters 43, 57 and 59 are in Hartel (`cyprian_epistulae-lat_hartel1871-csel3-tei.txt`), and Pontius's
  Life is in Hartel's third part. Both are already shelved to Latin Pastoral. No part of Hartel is missing for
  these letters.
- Panarion 48 in Greek: Holl 1922, now shelved (section 1).
- The anonymous writer against the Montanists (Eusebius, History V.16): the held text's own clue is in V.16.19 (npnf201 29886-29889), that
  more than thirteen years had passed since Maximilla's death without war. "About 192" is the editor's reckoning
  from it. No held source names Gratus's proconsulship.
- The Africa river origin and Alexandria's bounds: nothing new held beyond Eusebius II.16, II.24 and V.10.
- Hallier's Edessa Chronicle (1892): not fetched; Guidi's Latin and Cowper's English are held.

## Resume

Done: everything above. Left: the PR's CI and merge; the message to the cards thread; the final report to
the coordinator.
