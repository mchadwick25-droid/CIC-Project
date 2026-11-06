# Offline relevance of automatically retrieved passages (not built into the engine)

Question: if the offer also took passages found by search inside the world's lens, would they be the right ones? Method: for each sealed question's reader-named sub-question (arm C), the query is the sub-question's label plus the `retrieve_when` text of the records routed to it (not the visitor's own words). Search is the index's full-text ranking, restricted to the world, tradition-role rows, passages with their own row (not file-level), English, not apparatus, OCR 0.70 or more, seeds excluded; the top three kept. One blind Opus reader per world rated each passage against the visitor's question: yes (could ground a sentence of the answer), partly, no. lpc and rzg only: alx and syr have nothing in the lens. `relevance_build.py` is the script that made the items.

| World | Passages | yes | partly | no | Questions | with at least one "yes" | with a "yes" or "partly" | Top passage yes/partly/no |
|---|---|---|---|---|---|---|---|---|
| lpc | 78 | 7 | 23 | 48 | 26 | 5 | 15 | 2/8/16 |
| rzg | 81 | 11 | 20 | 50 | 27 | 7 | 16 | 6/4/17 |

Reading: about one retrieved passage in ten could ground a sentence, and about one question in four had any such passage among its top three. One reader per world; the readers judged from the question and the passage text only.
