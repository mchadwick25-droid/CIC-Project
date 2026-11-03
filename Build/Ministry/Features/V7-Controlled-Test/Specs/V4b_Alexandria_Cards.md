# V4b: reading cards for Alexandria

**Owner:** card thread, a fresh Opus session. It never opens `../Set/`. **Model:** Opus drafts and Opus reviews. The review follows the build cycle, capped at three rounds.

**Purpose.** Write the 35 alx cards: 26 quotes and 9 stories.

**How each card is drafted.**
- The author reads the cited lines and their context in `cic/texts/`, the record itself, and the alx construction documents in `Build/worlds/alx/`.
- Each line is drafted only from the source it names.
- `historians_conclude` uses the five-level confidence vocabulary.
- `whose_view` says whose view the passage gives and how widely it was shared, with the reason. Influence is not treated as representativeness.
- `reads_differently_today` rewrites the record's existing modern-lens note so the voice can say it.
- A line with no traceable source is left out.

**Review.** An Opus reviewer re-checks every line against its named source, verbatim where it quotes. The reviewer also flags:
- any line that presents one author as the world;
- any line that settles what is disputed;
- any line that adds a detail not in the source.

The review file goes in `Build/worlds/alx/Review-Artifacts/`.

**May touch.** The `reading_card` field of `records/alx/quote/*` and `records/alx/story/*`, and the review file. **Must not touch.** Any other field, any other world, `../Set/`.

**Tests written first.** These are V4a's gates, run on every alx record. A check confirms each card's word count and source names.

**Done when.** All 35 cards pass the gates and the review clears within three rounds. Otherwise the cards escalate to Mark. The alx package is rebuilt and stays byte-equal.

**Cost.** Allowance only.
