# Rendering Review: hal quote records, round 2 (4 records)

- **Reviewer:** Opus 5.5 (independent; did not draft, render or review these records before)
- **Date:** 2026-11-03

## Method

This is a targeted recheck of the four renderings that failed in round 1 (`Rendering_Review_Hal_Batch1_2026-11-03.md` and `Rendering_Review_Hal_Batch2_2026-11-03.md`). For each record, the round-1 finding is read first. Then the edition text is read at its span in `cic/texts/` (Jerome's letters in `npnf206`; Palladius in `palladius_lausiac-history_clarke1918.txt`), along with the record's `text`, its new `modern_rendering` (from the working-tree diff), its `use_note` and its `modern_lens_note`. The check covers the round-1 finding and the full bar: every clause rendered, nothing added, editors' supplements kept marked where they add meaning, one thought per sentence, no sentence past about 25 words, no misleading modern word, hedges, tense, reported-speech frames and contrasts kept, plain English. Sentence lengths are counted by script and confirmed by eye. Dashes and ellipses count as no word. Where a note changed, the change is checked against the edition too.

## Results

**4 records: 4 PASS, 0 FAIL.**

| Record id (hal.quote.…) | Round 1 finding | Round 2 check | Verdict |
|---|---|---|---|
| eyes-of-faith | "she protested that" and "eyes of faith" dropped after sentence 1 | every sentence now carries "she declared" and the eyes of faith; all seven items kept; longest sentence 25 words | PASS |
| buried-beneath-the-church | 30-word sentence | split (21, 16 words); the "not merely ... but throughout" contrast is kept | PASS |
| hindered-by-jerome | 28-word sentence joining two thoughts; causal "for" for "having induced" | split (10, 16 words); the participle is restored as "having led her"; "But" keeps the edition's concession; `use_note.means` now follows the edition's order and keeps "having induced" | PASS |
| she-put-on-sackcloth | "Who would believe it?" cut loose, so it doubted the husband's death | the question now points at Fabiola's turn, as Jerome's does; "Yet it was then" keeps its place; "error" restored; Jerome's own parenthesis on the basilica is rendered as his words; longest sentence 18 words | PASS |
