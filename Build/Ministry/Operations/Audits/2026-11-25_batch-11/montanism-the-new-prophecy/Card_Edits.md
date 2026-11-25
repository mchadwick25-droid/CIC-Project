# Card edits: Montanism, the New Prophecy (`montanism-the-new-prophecy`, tradition)

Card written: `montanism-the-new-prophecy.card.json`, from `Card.existing.json`. Every field not listed below is word for word. File abbreviations as in `Source_Sheet.md` (HE, ANF03, ANF04, ANF07, CSEL20, PanH, PanO, Proc).

**For release, placement.** This is the first tradition through the card step. A tradition has no `card` key, and `tools/validate-census.mjs` runs `checkCard` and `checkQuotes` only for a person or a council; the tree pages render a tradition's top-level `sources` as a list of `{work, type, note}`. The new fields `sources` (in the `cyril-and-methodius` form, `ownWords` and `about`), `briefReferences`, `quotationOriginals` and `uncertain` are written in the card format the role names; where they live on a tradition entry, and whether the validator and the page read them there, is release's call. With the card fields merged into a scratch copy of the census, the validator was run (result in the reply).

## Clearly wrong (corrections)

| # | Field | Old words | New words | Evidence |
|---|---|---|---|---|
| 1 | documentedStories[1].text (Zoticus) | Maximilla had said, in words the writer quotes: ‘After me there will be no more prophecy, but the end.’ He then counts the years | Maximilla had said, in words Epiphanius later quotes: ‘After me there will be no prophet any more, but the end.’ The writer, recalling her predictions of wars and anarchy, counts the years | Source sheet G7. The oracle is not in Eusebius; it is Epiphanius, Panarion 48.2.4, PanH 17218-17219, reading »μετ᾽ ἐμὲ προφήτης οὐκέτι ἔσται, ἀλλὰ συντέλεια« (no prophet). What the elder counts against is her prophecy of wars and anarchy, HE 29880-29890. The brief: "Maximilla also said, in words a later opponent kept, that after her there would be no prophet any more". |
| 2 | documentedStories[1].text | Julian of Apamea traveled to Pepuza to ‘test | Julian of Apamea came to ‘test | G7. The elder names no place (HE 29823-29878: "then present"); only Apollonius puts Zoticus at Pepuza (HE 30461-30464). Outline, Do not say. |
| 3 | documentedStories[1].caveat | All from a hostile source | All but the oracle of the end from a hostile source | Follows from 1: the oracle comes from Epiphanius, not the elder in Eusebius. |
| 4 | documentedStories[1].caveat | transmitted by an opponent. | transmitted by a later opponent, Epiphanius. | Follows from 1 (PanH 17218-17219; Epiphanius writes about 375, PanH 17224-17226). |
| 5 | documentedStories[1].sources[0].note | Themiso, the oracle, and | Themiso, her predictions of wars, and | Follows from 1: HE V.16.18-19 (HE 29880-29890) holds her predictions of wars, not the oracle of the end. |
| 6 | documentedStories[1].sources | (no Epiphanius line) | added `{"work": "Epiphanius, Panarion 48.2.4", "type": "primary", "note": "Maximilla’s oracle of the end."}` | Follows from 1: the story now cites Epiphanius. |
| 7 | documentedStories[0].text (the sister) | in order that their truth may be proved.’ | in order that their truth may be probed.’ | G7. ANF03 15819-15820: "in order that their truth may be probed". |
| 8 | floorNote | is not what its opponents objected to — as far as the surviving evidence shows, it held | is not, Tertullian says, what its opponents objected to — by his account, and Hippolytus's for most of them, it held | A held source contradicts the unqualified claim: Hippolytus, ANF05 13136-13138, "some of these assent to the heresy of the Noetians"; Jerome, NPNF206 8318-8325, "force the Trinity into the narrow limits of a single personality". Tertullian's own claim, CSEL20 15495-15499 (Q2); Hippolytus for the rest, ANF05 13127-13130. Outline, Do not say ("they held the same doctrine as the church" as the narrator's fact). G2. |

## New

- **quotationOriginals** (three; the brief has three quoted spans, each one entry; each six words or more, so no `secondReading`):
  1. Q1, modern = printed, HE 29849-29852 (the McGiffert English is the held print, re-read: the note between "wolf." and "I am not" is an endnote). `uncertain`: the Greek is not held; the second English is ANF07 11336.
  2. Q2, printed Latin CSEL20 15495-15499 (re-read; "Maxi-/milla" broken at 15497-15498), from "nouae prophetiae recusantur", the rendering beginning after "propter hoc" as the outline says; `englishPrinted` ANF04 9773-9777 (re-read, double space after the colon as printed).
  3. Q3, printed Greek PanH 18758-18764, copied as the scan reads (χ for κ; the last word "χατιέ-/νγαις"); checked by hand against the rendering: ἐν ἰδέᾳ γυναικός, ἐν στολῇ λαμπρᾷ, ἦλθε πρός με Χριστὸς, ἐνέβαλεν ἐν ἐμοὶ τὴν σοφίαν, ἀπεκάλυψέ μοι τουτονὶ τὸν τόπον εἶναι ἅγιον, ὧδε τὴν Ἱερουσαλὴμ ἐκ τοῦ οὐρανοῦ κατιέναι. `uncertain` names the OCR spellings and the second print, PanO 3281-3287 (re-read: τύπον for τόπον), with its Latin at PanO 3357-3358. The original is held in a print with scan slips confirmed by a second held print, so it is printed (Card role).
  A scratch fold of each `printed` and `englishPrinted` against its lines, as the validator folds, matches; each `modern` matches its span in the brief.
- **sources**: `ownWords` CSEL20, ANF04, ANF03 (Tertullian, the movement's own side, Source sheet "own side"); `about` HE, ANF07, PanH, PanO, Proc. Every file a quotation cites is listed.
- **briefReferences**: thirteen lines, one per run of the brief, each with the lines the outline cites for it (beats 1-7, Words to explain, Quotes, Setting).
- **uncertain**: fifteen items, each what the outline sends to the card, told in its witness's voice:
  1. Start date and the Lyons letter as dating only (Setting; G1; Leave out, Lyons letter).
  2. Belief about God (Cut first 1, Hippolytus; G2; Leave out, Montanus's first-person oracles and the lyre oracle).
  3. Who the Paraclete spoke through (Do not say, first line; G3).
  4. Apollonius's charges (Cut first 5 and 10; Brief cuts 4; Leave out, Alexander and Themiso's letter).
  5. The Thracian bishop and Priscilla (Cut first 2).
  6. Martyrs at Apamea (Cut first 3).
  7. Rome's letters of peace, with the gloss (Cut first 4; one partisan witness).
  8. Prisca's oracle, the Spirit's oracle on martyrdom, the city in the sky (Leave out, both lines; Cut first 11).
  9. Holl against Oehler on "prophet" (beat 4: card).
  10. Quintilla or Priscilla (Do not say; G5).
  11. Women clergy, the seven virgins, the Artotyrites (Brief cuts 3; Leave out; Revision, Brief cuts 3).
  12. Cyril's child-murder charge, with Jerome's doubt and Cyril's own remark (Leave out: card; E5).
  13. Constantine's law, baptism refused (Firmilian, Basil), Jerome on Pepuza's patriarchs, Sozomen on Phrygia and Easter by the sun (Cut first 6 and 8; What came of it 4 and 5; Leave out).
  14. Their books, and Tertullian's lost On Ecstasy (What came of it 2: the lost books card; ANF05 13117-13119; NPNF203 40315-40318).
  15. Justinian's threat on property, Novel 45, Michael the Syrian's bones at Pepuza (Cut first 7; Leave out; Ending 2 not used).
  Cut first 9 (the foretold wars and the thirteen years) and 12 (the sister's visions) are already on the card, in the two documented stories.

## Entry fields

| Field | Old | New | Evidence |
|---|---|---|---|
| why | In a Phrygian village around 165, a man | In a village on the edge of Phrygia, in the second century, a man | Ardabau lay "in that part of Mysia, which borders upon Phrygia" (HE 29577-29579); "around 165" is an editor's reckoning (Source sheet A4; Do not say); the brief: "in the second century". |
| why | and together they expected the New Jerusalem to descend on their own village of Pepuza. Lost for over a thousand years, that village was located by archaeologists only in 2000. | and their followers came to expect the New Jerusalem to descend on the small town of Pepuza. | Pepuza a small town (HE 30275; PanH 18512 πόλιν; Do not say). The expectation is told by Epiphanius of the believers of his day (PanH 18512-18513), not of the three together. The 2000 finding: no held source (G6; the batch header's slate line); the brief no longer makes it (the approved brief did). |
| teaser | from around 165 CE into | from the second century into | As above (A4; brief). |
| teaser | which named the village where | which named the town where | HE 30275. |
| floorNote | see correction 8 | | |
| documentedStories | corrections 1-7 | | |
| documentedStories[0].sources | the Trevett line | removed to `documentedStories[0].modernWorks`, word for word: `{"title": "Montanism: Gender, Authority and the New Prophecy", "author": "Christine Trevett", "year": "1996", "publisher": "Cambridge", "note": "On women prophets in the movement and this passage."}` | Card role: a modern work under sources moves to modernWorks. |
| documentedStories[1].sources | the Heine line | removed to `documentedStories[1].modernWorks`, word for word: `{"title": "The Montanist Oracles and Testimonia", "author": "Ronald Heine (ed.)", "year": "1989", "publisher": "Mercer", "note": "Collects and translates all the surviving oracles and testimonies."}` | As above. |
| modernWorks (new) | none | Holl 1922, Oehler 1860, Reifferscheid and Wissowa 1890, Kroymann 1906, Routh 1846, each with a note on what it covers | Outline, Who tells it: "modern editions; clarify the texts". Title, publisher and year from each file's header. All public domain by date (`CORPUS-USE.md`). |
| dates | c. 165-400s | 2nd-6th c. | G7: Sozomen has them many in Phrygia in his own day (NPNF202 30574-30577), Procopius burning their churches under Justinian (Proc 2195-2197); the start year rests on an editor's reckoning (A4). |
| end | 400 | not changed | No held source gives a year for the end: the brief and Setting say "in the sixth century, under Justinian". 400 is contradicted by Sozomen (NPNF202 30574-30577) and Procopius (Proc 2195-2197). The axis needs a year: flagged for Mark, with start. |
| start | 165 | not changed | No held source gives a year (Gratus, no year; Epiphanius about 156/7). The axis needs one; flagged, not changed. |
| relationsSummary | not changed | | "met many times" is close to "met often in many places" (HE 29721-29722; G7: close, keep). |

## Not found (left in place)

- documentedStories[1].text: the quoted ‘test and refute the spirit that spoke in her’ and ‘hindered by those who were with her’: no held print has these words (HE 29823-29878, 30461-30464 and ANF07 11336 word it otherwise; the Greek is not held).
- documentedStories[1].text: Maximilla "outlived Montanus and Priscilla"; "survived ... by two centuries; what it could not survive was becoming ... a movement whose promised end had not arrived" (a judgment).
- documentedStories[0].text: "defending the New Prophecy against the charge of disorder" (De anima 9 names no such charge). Its ‘tender and lucid and of the colour of air’ is not the ANF English but stands as a rendering of CSEL20 17500-17501, "tenera et lucida et aerii coloris".
- documentedStories `when` "c. 207–212" and "c. 175–180": no held source gives these years.
- legacy: "Its own writings were destroyed"; the Phrygian graves and inscriptions. sourcing: "Phrygian inscriptions" (none held, G8). Charles Chauncy in 1743 was found (`chauncy_seasonable-thoughts-on-the-state-of-religion-in-new-england_1743.txt` 6292-6304).
- relationsSummary: "In the late second century" (no held source dates the meetings).
