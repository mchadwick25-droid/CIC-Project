# Drift: batch 3 against the first twelve (2026-11-18)

Asked by Mark before recording: "can you run a comparison with the first batch to test drift". The first twelve are the briefs as released after the release-50 fixes (`2026-11-17_varied-batch*/<slug>/<slug>.brief.txt`, without "How Nicaea decided"); batch 3 is the finished twelve.

## The five counted moves (`tools/check_brief_variety.py`)

| Move | First twelve | Batch 3, first drafts | Batch 3, finished | All 24 |
|---|---|---|---|---|
| Unnamed opening, then the name revealed | 6 | 3 | 1 | 7 (over 6) |
| Setting slot (time and place stacked early) | 9 | 4 | 1 | 10 (over 6) |
| "Most of what we know" | 0 | 1 | 0 | 0 |
| A sentence opening with "Yet" | 0 | 1 | 1 | 1 |
| Ending on a later writer or institution | 12 | 7 | 0 | 12 (over 6) |

Every move that is over across all 24 is over because of the first twelve.

## Read by hand, not by the detector

The detector finds the later ending by a later time marker in the last two paragraphs, and the setting slot by a year and a place in one early sentence. Read for what the move is:

- **Endings on a later writer, record or institution: 5 of 12** (Justin on Tertullian; Pachomius on Benedict of Aniane; Wyclif on Hus at Constance; Baudonivia on her editor; Alopen on the stele his church carved later). The detector counts 0 because their dates were removed: Benedict of Aniane's century was cut to clear it, and the others never carried one. By the move's meaning, batch 3 is over the limit of 3, though down from 12.
- **The other endings are varied:** his death (Thomas à Kempis, Vardan, Arius, Moses the Black, with its two witnesses), the person's own words (Narsai, Dioscorus for Chalcedon), and a scene at the council (Toledo).
- **Unnamed opening, then the name: 2 to 3 of 12** (Justin "a man from a Roman town"; Vardan "an Armenian general"; Pachomius names him in the second sentence). The detector counts Justin only.
- **Time-first openings: 3 of 12** (Justin "In the middle of the second century", Narsai "In the 400s", Vardan "In 450"); they escape the setting detector by leaving the place out. The first twelve had 2.
- **Openings on a source's words: 4 of 12** (Alopen and Arius on a quotation; Baudonivia and Moses on a reported saying). The first twelve had 3 (Dhuoda, Nicaea, Marcion).

## Wording

- No three-word phrase in content words recurs in four or more batch-3 briefs. The first twelve had "in what is now" (5) and "story comes to us" (3).
- Phrases common in batch 3 and rare before: "the year" (7 against 2), "he died" (5 against 1), "the city" (5 against 0). None is a formula.

## Length and sentences

| | First twelve | Batch 3 |
|---|---|---|
| Median words | 419 | 439 |
| Mean sentence length | 20.2 | 18.5 |
| Quotations in the briefs | 59 | 56 |

## Finding

Drift is much lower than in the first twelve, and the wording shows no new formula. One move survives under the detector: the ending on a later witness, in 5 of 12, partly because writers cut dates to clear it. The detector's two date tests can be passed by dropping a date, which costs the listener information (Open-Gaps 326). Fixing the detector is a kit change, under the standard lock.

## After Mark's ruling (2026-11-18)

Baudonivia now ends on the funeral scene in her own book, and Alopen on Lohan and Kie-leih holding the community together; both passed their targeted check (`Ending_Check.md`). Endings on a later writer, record or institution now stand at **3 of 12** by hand (Justin, Pachomius, Wyclif), within the limit. The variety check is clear.
