# Search build brief, 2026-11-03

For a fresh engine session. Read `CLAUDE.md` first. The plan and rulings are below. Do not start a paid step.

## Rulings (Mark, relayed by the coordination thread)

1. Passages found by search may support sentences, as quotation or close paraphrase in the author's name. Every sentence is still checked.
2. Every world has its own library, reached only when that world is called. Search for a world runs only on that world's own shelf, never on another world's rows. The shared index file is storage only.
3. A world speaks only from its defined sources, and from all of them. Records and seeds are not the limit. They only help rank and route. Search reaches every passage on the shelf that passes the lens (narrowed row, in window, English, not apparatus).
4. The new search code goes in a separate folder outside the hashed set (`Sandbox/answering-library/index/*.py` is hashed into every index version), so no index stamp changes.
5. Revert Decision-Log 63 and 64 as commits, after Mark approves the plain-words account. A separate pull request. No third patch on top.
6. Held-out set: every built world, sized by source volume; sizes wait for Mark's approval. Nothing is written before that.
7. Paid steps (an API embedder; a live-model run on the held-out set) are not requested.

## The build (step 3 onward of the plan)

- Lens first, as a hard filter: only passages on the world's own shelf rows, inside the window, with the role and voicing rules the seed builder already applies (`engine/m4/reports/passage_offer_build.py`). Test with a two-world case: a query that matches a passage on world B's shelf only must return nothing for world A.
- Inside the lens, run the existing keyword search (`Sandbox/answering-library/index/retrieve.py`) and a meaning search with a free local embedder behind the `Embedder` interface (`index/embeddings.py`). Fuse the two rankings, then rerank. If no free embedder or reranker holds up, report that; do not drop a step quietly.
- Query is the visitor's own words. Context lines are not built.
- Offer: one list ordered by rank (`passage_offer.interleave` already places passages among the records by rank). A reviewed seed ranks above a searched passage of equal score. Budget stays 6 passages and 1800 words. Every passage keeps its voiceable or outside-the-voice flag and is cited as "[author], in [work], writes"; never "we".
- One draft pull request for the whole slice. Push once after the local checks pass. Opus reviews it.

## Steps 3 and 4 and their measures (fixed in advance)

- Step 3, retrieval bench: re-run the existing S1-05 bench (535 cases, visitor wording) four ways (keyword only, meaning only, fused, fused with seeds), then on rzg. Measure whether the cited passage is in the top 5, 10 and 20. Code decides; no reader. A method is better than another only when it wins more paired cases than it loses beyond a 99% sign test. Report counts with the case total.
- Step 4, known misses: Letter 47.5, City of God XXII.8 and XXI.17, and the q101 quote. Found in the top 10 from the visitor's words: yes or no each. Existence checks, not a rate.
- Stop after steps 3 and 4 and report counts. If meaning search does not lift reach beyond the 99% line, stop and report.

## Facts to start from

- Coverage and reach counts: `Step1_Coverage_Ceiling.md` in this folder. Only the work-and-place key is filled in the index; nothing in the engine reads the index at question time; no embedder implementation exists.
- Built indexes (851, 538, 290 and 257 MB) were in the previous session's scratch area and are rebuilt from `cic/texts` by the Library builder (`answering_library.run`, then `index.cli build-index --world W`).
- Do not edit files under `Sandbox/answering-library/index/` that are hashed, and do not print the shared environment.
- Report to the coordination thread with plain outcomes and counts only.

## Amendment, 2026-11-03 (Mark's direction, Decision-Log 68)

Gating the offer waits for Mark's decision. Steps 3 and 4 do not depend on it and may start now.

- Build the step before drafting that decides what the offer holds as one function, a single seam. Today it returns the current behaviour: records and passages together, interleaved by rank. Records-first with search on a missing or partial record, and a stored-answer match, can be added at that seam later. Do not add either now.
- Long-term direction, not built and not scheduled: stored, reviewed answers served on a match with no generation, and live generation only when nothing matches.
