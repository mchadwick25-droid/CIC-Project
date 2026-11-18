# R3 recheck: ten Who profiles, era 2 batch 5

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git diff HEAD~1` at `7c6b7d8f` on `era2/batch5/`), against `R2_recheck.md` and `R2_changes.md`. Four files changed: the Cyril brief and its audio script, the Alexander card and `records.json`. Unchanged text was not re-reviewed. Each changed sentence was opened at its line in the vendored file, with XML tags stripped, to confirm who is speaking. No drafts were edited and no paid, model or web calls were made.

## 1. The R2 blocking findings

None were raised in R2.

## 2. The R2 minor findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Cyril, brief l.9: "he" and "His" fell on Nestorius | RESOLVED | "In 433 Cyril made peace with John. His letter begins, 'Let the heavens rejoice, and let the earth be glad.'" "His" now falls on Cyril, the nearest subject. The letter is Cyril's: "Letter of Cyril to John of Antioch … Cyril to my lord, beloved brother, and fellow minister John, greeting in the Lord. 'Let the heavens rejoice, and let the earth be glad'" (npnf214 l.19420–19428). The quotation is unchanged and exact. The 433 date was already in the R1 and R2 text. |
| N2 Alexander, card `uncertain` #1: closed list of Arius-side sources | RESOLVED | "the held sources include Arius's own letter to Eusebius of Nicomedia, kept by Theodoret, and a letter from Arius and his fellow clergy to Alexander himself, kept by Athanasius. Philostorgius, also on that side, survives only in a hostile summary by Photius." "Include" opens the list. Theodoret I.4: "The Letter of Arius to Eusebius, Bishop of Nicomedia" (npnf203 l.6002–6006). Athanasius, De Synodis 15–16: "Arius and those with him thought and …", then "what they wrote by letter to the blessed Alexander, the Bishop, runs as follows:— To Our Blessed Pope and Bishop, Alexander, the Presbyters and Deacons send health in the Lord" (npnf204 l.56997, 57093–57099), closed by "This is a part of what Arius and his fellows vomited" (l.57198). "Arius and his fellow clergy" is a fair short form of "Arius and those with him" and "the Presbyters and Deacons"; the speaker is Athanasius, who keeps the letter. The Philostorgius sentence is unchanged in substance. No new attribution, pronoun or hedge problem. The card parses as JSON. |
| N3 Ossius, `records.json`: honest limit on his kinsfolk dropped | RESOLVED | New absent detail "Names of his kinsfolk", note "Athanasius speaks of conspiracies against his kinsfolk (npnf204 l.36614-36615); no source used here names them." Athanasius, Defence of his Flight 5: "the repeated stripes above measure that were inflicted upon him, and the conspiracies that were formed against his kinsfolk, he yielded" (l.36613–36615). The speaker is Athanasius, and no name is given there. It now backs card `uncertain` #5. `records.json` parses. |

## 3. Gates on the changed brief

| Brief | Words | Cap | FK | Flesch | Audio = brief less `[calmly] ` and one `[warmly] ` |
|---|---|---|---|---|---|
| Cyril of Alexandria (MAJOR) | 404 | 405 | 7.2 | 64.1 | Yes |

`grade_text` passes (FK at most 10, Flesch at least 60). The script carries one `[calmly]` and one `[warmly]` (checked by script).

## 4. New findings

None. The changed text adds nothing wrong, unsupported, misleading or not verbatim, and no witness swap, loose pronoun, dropped hedge or new wrong attribution was found.

## Verdict

N1 to N3 are all resolved and hold against the sources. No new finding. The batch clears review at round 3.
