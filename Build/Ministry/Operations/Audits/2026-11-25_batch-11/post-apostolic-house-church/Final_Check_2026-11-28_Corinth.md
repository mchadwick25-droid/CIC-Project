# Final check, Corinth fix: post-apostolic-house-church

Review 3 of 3 for the fix under Mark's ruling of 2026-11-28 ("yes"): (1) no saying Corinth asked Rome to write; (2) no saying Dionysius drew counsel "in the quarrel". Roles: `roles/final-check.md` sections 3, 4 and The verdict (no quote changed, so sections 1 and 2 do not apply). Sources read at line ranges: `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` 515-540 (1 Clement 1); `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` 25095-25120 (Church History IV.23.10-11).

## The changed sentences and card lines

| # | Where | Text now | Source | Mark | Reason |
|---|---|---|---|---|---|
| 1 | Brief, paragraph 2 ("Near the end of the first century"), sentence 2 | "The church of Rome wrote to Corinth." | 1 Clement 1, anf01 519-523 ("The Church of God which sojourns at Rome, to the Church of God sojourning at Corinth") | SUPPORTED | Mark's wording, word for word. The sentence before (Corinth removed some of its elders) and after ("Its letter, the only side that survives, blames envy...") say nothing of a request or consultation. |
| 2 | Brief, Dionysius sentence ("Later, Dionysius, bishop of Corinth") | "...that his church still read Rome's letter, written through Clement, and drew advice from it." | Eusebius IV.23.11, npnf201 25109-25117 | SUPPORTED | Eusebius: Dionysius shows "it had been the custom from the beginning to read it in the church"; Dionysius: "we shall always be able to draw advice, as also from the former epistle, which was written to us through Clement." "Still read" rests on Eusebius's framing, "drew advice" on Dionysius's own word. No quarrel is named, as the ruling requires. The sentences either side (Justin's Sunday; the Easter quarrel) do not attach the advice to the Corinth dispute. |
| 3 | Card `entry.tile` | "When the church at Corinth removed some of its elders, the church of Rome wrote to Corinth." | 1 Clement 1, 3, 44, 47 | SUPPORTED | Ruling wording; no request implied. |
| 4 | Card `timeline[0].lines[0].text` | "Rome's letter says sudden troubles at Rome have slowed it in turning to the matters at Corinth." | 1 Clement 1, anf01 524-531 ("Owing ... to the sudden and successive calamitous events which have happened to ourselves, we feel that we have been somewhat tardy in turning our attention to the points ...") | SUPPORTED | "The matters at Corinth" takes neither side of the Greek (peri ton epizetoumenon par' hymin pragmaton), and stands for the "points" and the "sedition" the same sentence names. "At Rome" follows "happened to ourselves" in a letter from the church at Rome. The editor's "asked" note is not carried. |
| 5 | Card `timeline[0].headline` | "Corinth removes some of its elders, and Rome's church writes to Corinth" | as 3 | SUPPORTED | No request implied. `witness` ("the only side of the quarrel that survives") also fine. |

## Other card fields (card list item 7)

Read for any saying or implying that Corinth asked or consulted Rome, or that Dionysius drew counsel in the quarrel: `why`, `entry.tile`, every timeline headline and line, `voices`, `legacy`, `sources` notes, `uncertain`, `quotationOriginals`.

- None says Corinth asked or consulted Rome. `why` ("Rome wrote at length to settle a quarrel in Corinth"), `voices[1]` ("addressing a dispute over deposed leaders") and the 1 Clement `sources` note ("to settle a dispute over deposed leaders") give Rome's purpose, which the letter itself shows (ch. 59, its messengers to return "with news of peace", timeline[0].lines[4]); none implies a request. `legacy`'s "With the apostles no longer there to consult" is about the apostles, not Corinth and Rome. No `quotationOriginals` entry carries "consulted".
- None ties Dionysius's advice to the quarrel.
- `timeline[7].lines[2]`: "Dionysius writes that Corinth read Rome's new letter on the Lord's holy day, and will always draw counsel from it, as from the earlier letter written through Clement." Against Eusebius IV.23.11 ("To-day we have passed the Lord's holy day, in which we have read your epistle. From it, whenever we read it, we shall always be able to draw advice, as also from the former epistle, which was written to us through Clement"): the reading, the day, the two letters and Clement are right, and it says nothing of the quarrel. "Will always draw counsel" drops Dionysius's "be able to", turning what the letter can give into a promise, and its note calls the line Dionysius's own words. **MINOR**: the listener would not take it differently in any way the ruling guards against. The exact change, to match the brief's "advice" and the source:
  - File/field: `cic-website/data/world-census.json`, movement `post-apostolic-house-church`, `timeline[7].lines[2].text`
  - Old: "and will always draw counsel from it, as from the earlier letter written through Clement."
  - New: "and will always be able to draw advice from it, as from the earlier letter written through Clement."

## The whole brief, heard once

Heard once as the listener: the Corinth paragraph now tells that Rome wrote, why the letter says the elders could not be removed, and that only Rome's side survives; the Dionysius sentence tells that Corinth went on reading the letter and drew advice from it. Nothing told twice, no jump back, no new tell. Nothing BLOCKING under the bar.

## Verdict

**PASS.** All four changes stand on their sources and meet both parts of Mark's ruling; no card field says or implies that Corinth asked Rome, or that Dionysius drew counsel in the quarrel. One MINOR exact change is given above (`timeline[7].lines[2]`, "will always draw counsel" → "will always be able to draw advice"). It is not a reason for another round.
