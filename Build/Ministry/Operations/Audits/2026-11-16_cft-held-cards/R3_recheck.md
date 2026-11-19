# R3 recheck: five edits to two Church Family Tree story cards

Date: 2026-11-16. Round 3, a targeted recheck at low effort of the five rows in `R2_changes.md`, against the round 2 findings in `R2_recheck.md`. Nothing else in the diff was re-reviewed.

Scope: `git diff HEAD -- cic-website/data/world-census.json cft-website/index.html` on `claude/cft-held-cards` (uncommitted).

Held texts:
- AS = `cic/texts/acta-sanctorum_augusti-tomus-1-lat_1750.txt` (Latin OCR, long-s read as f)
- PS = `cic/texts/john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`

Result: **0 BLOCKING, 5 PASS.**

## Rows

| R2 finding | Card, field | Change | Evidence | Verdict |
|---|---|---|---|---|
| N2 | Dominic, text | "told the story again under oath" to "also told the story under oath" | "Also" adds the inquest witnesses to Jordan without putting one telling before the other. The oaths stand: John "juratus" (AS 107807-107808), Stephen "jurat us" (AS 108388). | PASS |
| N4 | Dominic, caveat | "still a layman" to "then still in the world, before he entered religious life" | "quaodo ipfe F. Domioicus erat io feculo, dc ftudebit Palentiz" (AS 107997-107999), i.e. "quando ... erat in saeculo, et studebat Palentiae". "In the world" is the plain sense of in saeculo, and "before he entered religious life" glosses it without saying whether he was a cleric. It still stands against Stephen's "already a canon of Osma" (AS 108395-108396), and neither version is given as settled. No quotation marks. | PASS |
| N7 | Ephesus, caveat | "the only held source" to "our only source" | Same claim with no internal jargon. The counts still differ between chapters (BR 38066-38068, 39043-39046; PS 9006, per R2 J6). | PASS |
| N8 | Ephesus, teaser | 34-word sentence split in two; "on his own account" dropped | Sentence 1 is now 24 words, sentence 2 is 8. The "agent" claim rests on the appointment as "teacher of the heathen in Justinian's time" (PS 11915-11916), funded "by king Justinian" (PS 11955-11956). The text ("John reports the results himself") and the caveat ("our only source for his own mission") still carry the attribution that the dropped phrase gave. | PASS |
| N8 | Ephesus, sources[0].work | "on the trials of pagans" to "on the trials for secret pagan worship" | Now matches the text's "people accused of secret pagan worship". The accused were men who had "served devils, according to all the works of heathenism" (PS 11646-11648) and were found to be "heathens in disguise" (PS 11811); the depositions "relating to the heathen" (PS 11631). | PASS |

## index.html against the census

The added and removed lines in `cft-website/index.html` are identical to those in `world-census.json` once `\uXXXX` escapes are decoded and whitespace is stripped (27 lines each, checked with `diff`). Each of the five new phrases appears once in each file. None of the old phrases remains in either card. The phrases "still a layman", "on his own account" and "the only held source" still occur in three other cards in both files; those cards are outside this review.

## Summary

All five edits are true to the held texts and add nothing unsupported. index.html matches the census for these fields. No new findings.
