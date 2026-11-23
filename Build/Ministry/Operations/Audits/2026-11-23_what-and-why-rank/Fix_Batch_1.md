# What-and-why fix batch 1: the Crucial pieces and the out-of-date recordings

Run 2026-11-23, in the order Mark approved ("option 1", Decision-Log, "The re-recording order approved"): the 57 recorded pieces whose worst finding is Crucial, and the 35 recordings whose text had already changed since recording (free queue, fixed first).

## What was fixed

- **79 pieces passed review and are applied**: 34 briefs (census `longDescription`), 36 documented stories (census `documentedStories[i].text`, with title or teaser where a cut made them wrong), 8 built-world pieces (`Build/Ministry/Features/Church-Family-Tree/World-Narration/`), 1 map story (`cft-website/index.html`, Hugeburc of Heidenheim, teaser revised).
- Of the 57 Crucial pieces, 55 are applied and 2 wait for Mark (below). Of the 35 out-of-date recordings, John Chrysostom and Ephrem belong to batch 10 and were left to that thread; 9 were clear on reading; 24 are applied.
- **72 modern works** moved out of the texts onto `modernWorks` (shape agreed with the audio completion thread, Open-Gaps 401). One map story's works are not stored, because a map story has no census entry.

## How

- Writers (Sonnet): `Fix_Prompt.md`. Reviewers (Opus): `Fix_Review_Prompt.md`; rounds 2 and 3 were targeted rechecks of what changed. Every added claim was checked against the cited file and lines. Replies and reviews: `fixes/round1-3/` and `fixes/stale1-2/`.
- Rounds: of 79, 33 passed in round 1, most of the rest in round 2, and 4 needed a third round (Union of Brest, Caucasian Albania, Liturgical Movement, Latin Africa). None reached the cap.
- Rules applied during the run, each from Mark's rulings that day: the reader's "heart" line is a working note, never reviewed; a source-bound modern work may support a fact unnamed (Mark: "more current scholors can be used as sources if they are historical and source bound, but not referenced in the text"); a modern work's title, author or year must come from a file, never from memory; a writer's own rendering of a Greek or Latin word is not a source.
- Applied with `apply_fixes.py` (scratch), then `python -m engine.m6.cli atlas-sync`, `node tools/build_tree_site.mjs`, `node Build/tools/generate_tree_pages.mjs`.

## Waiting for Mark

- `worlds-tree/syriac-edessa-nisibis/docstory-syr.story.qyama-morning`: the piece is a morning scene that no old source describes. The fix told the same ground from three old witnesses, which changes what kind of piece it is.
- `worlds-tree/lutheran-wittenberg-and-its-congregations/docstory-witt.story.speratus-hymn-under-the-window`: only a modern writer holds the story. With him out, about 20 words remain.

## Not done in this batch

- The 218 Supporting and 356 Passing recorded pieces, and the free-queue scan of the unrecorded pieces (Open-Gaps).
- Re-recording: the fixed recorded pieces are text only until their turn (Decision-Log, option A).
