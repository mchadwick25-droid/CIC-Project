# Card edits: Antony the Great

Card writer, 2026-11-18. Worked from the census card for `antony-the-great` (`cic-website/data/world-census.json`, its `card` object), `antony-the-great.brief.txt`, `Outline.md` and `Source_Sheet.md`. Output: `antony-the-great.card.json`. Keys as the census has them (`datesNote`, `placeNote`); no `briefLength`, which the census check does not allow. Every other field is kept word for word and in order.

## New

| # | Old words | New words | Evidence |
|---|---|---|---|
| N1 | (none) | `sources.about`, last: Oration 21, On the Great Athanasius, §5 (the Life as the laws of the monastic life); Gregory of Nazianzus; English translation; `cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml` | Brief: "Gregory of Nazianzus called it the laws of the monastic life, set out as a story." npnf207 29433 (Oration XXI heading), 29544-29554: "as he himself wrote the life of the divine Antony, and set forth, in the form of a narrative, the laws of the monastic life." Source_Sheet A1. |
| N2 | (none) | `briefReferences`: "Gregory of Nazianzus, Oration 21 §5: the Life sets out the laws of the monastic life as a story." | As N1. |
| N3 | (none) | `briefReferences`: "Sozomen, Ecclesiastical History I.13: his disciples in Egypt, Libya, Palestine, Syria and Arabia." | Brief: "his disciples flourished in Egypt, Libya, Palestine, Syria and Arabia." npnf202 27392-27394: "some flourished in Egypt and Libya, others in Palestine, Syria, and Arabia". Chapter XIII heading at 27308. The Sozomen file is already among the card's sources. |
| N4 | `quotationOriginals[1]`, modern "For I had heard this of Antony. ... spoken to him.", lines 13470-13472, secondReading "minor" | modern: the brief's whole quoted span, "For I had heard this of Antony. He had come in by chance during the Gospel reading, and was urged on by it. It was as though the words read were spoken to him. 'Go, sell all that you have, give to the poor, and you will have treasure in heaven. And come, follow me.' By such a divine word he was at once turned to you."; printed: "audieram enim de Antonio, quod ex euangelica lectione, cui forte superuenerat, admonitus fuerit, tamquam sibi diceretur quod legebatur: uade, uende omnia, quae habes, da pauperibus et habebis thesaurum in caelis; et ueni, sequere me, et tali oraculo confestim ad te esse conuersum."; lines 13470-13501; no `secondReading` | The brief's quotation now runs on through the Gospel words and "turned to you". Re-read in `augustine_confessiones-lat_knoll-csel33.txt` 13470-13473 and 13501; lines 13474-13500 are footnotes, apparatus and page head, a listed drop in `tools/quote_scan_readings.json`, and "euangelica 20" at 13470 is a listed line-number reading. Rendering as in Outline.md Q3. Pilkington English re-read at npnf101 13117-13124. **Awaiting second reading** (changed span). |
| N5 | `uncertain`: "... (npnf101, lines 13117-13121) reads \"he received the admonition as if what was read were addressed to him\"." | "... (npnf101, lines 13117-13124) reads \"he received the admonition as if what was read were addressed to him\". \"Divine word\" renders oraculum, which Pilkington gives as \"oracle\"; \"you\" is God, to whom the Confessions are addressed. The footnotes and page head between lines 13473 and 13501 are left out." | The span now reaches "by such oracle was he forthwith converted unto Thee" (npnf101 13123-13124). Outline.md Q3 note on oraculum and on "you". |

## Removed: a span the brief no longer quotes

| # | Old words | New words | Evidence |
|---|---|---|---|
| R1 | `quotationOriginals[0]`: modern "the desert became a city of monks.", printed "καὶ ἡ ἔρημος ἐπολίσθη ὑπὸ μοναχῶν", PG 26 lines 70548-70549, secondReading "same" | (removed) | The brief says "until the desert became a city of monks." without quotation marks. Its only quoted span is the Augustine passage (N4). The phrase stays in `briefReferences` in quotation marks, since those words stand verbatim in the brief. |

## Clearly wrong: `briefReferences` that name what the brief no longer says

| # | Old words | New words | Evidence |
|---|---|---|---|
| W1 | "Life of Antony §1–2: his Christian parents of good family and wealth; their death when he was about eighteen or twenty; the Gospel reading, ..." | "Life of Antony §1–2: the apostles who left all; the Gospel reading, ..." | The brief gives neither his parents nor his age. It says he "walked into church thinking of the apostles who left everything" (npnf204 31236-31240, "how the Apostles left all"). |
| W2 | "Life §3–4, §7: the hermits near the villages, the old man of the next village, work with his hands, bread and salt once a day." | "Life §3, §7: work with his hands, prayer, bread and salt once a day." | The brief has no hermits and no old man (§3-4). It says "to live by prayer, work with his hands, and fasting" (npnf204 31288-31293, "constant in prayer"; 31421-31422). |
| W3 | "Life §12, §14: the deserted fort across the river, the walled door, bread twice a year; the door forced after nearly twenty years; ..." | "Life §12, §14–15: the deserted fort, the walled door; the door forced after nearly twenty years, when many wished to live as he did; he persuaded many and directed them as a father; ..." | The brief has no river and no bread. It says: "When many wanted to live as he did, his friends forced the door. He persuaded many to take up that life and directed them as a father." npnf204 31600-31606, 31623, 31637-31638. |
| W4 | "Life §49–50: ... to the mountain with a spring." | "Life §49–50: ... to the mountain." | Brief: "three days further into the desert, to a mountain." No spring. |
| W5 | "Life §89–91: near a hundred and five; burial in secret, against the Egyptian custom of keeping the holy dead in houses." | (removed) | The brief gives neither his age at death nor his burial. |
| W6 | "Life, prologue and §93: a pattern for monks abroad; heard of in Spain, Gaul, Rome and Africa." | "Life, prologue: a pattern for monks abroad." | The brief names no Spain, Gaul, Rome or Africa. It says "It was written for monks in other lands, as a pattern for their own life" (npnf204 31184-31185). |

## Left alone

- `knownFor`, `datesNote`, `placeNote`, `role`, `keyWorks`, `legacy`, `uncertain`: nothing in the brief or a held source contradicts them. "the desert was colonised by monks" in `legacy.traces` is the 1892 English quoted (npnf204 31625), not the narrator's word.
- The Sozomen source title, "Book 1, chapter 13 (Antony's birthplace of Coma)", is still true; the disciples (N3) come from the same chapter.
- `briefReferences` on the authorship and date, the Arians (§69), the Latin by Evagrius (Robertson's introduction), the emperors' letters (§81) and Augustine (VIII.6.14-15, VIII.12.29) match the brief.

## Not found

None.

## Second readings

- Awaiting second reading: `quotationOriginals[0]`, the Augustine passage (N4). Its span and modern wording changed, so no verdict is copied.
- No span is carried over unchanged, so no `secondReading` is copied.
