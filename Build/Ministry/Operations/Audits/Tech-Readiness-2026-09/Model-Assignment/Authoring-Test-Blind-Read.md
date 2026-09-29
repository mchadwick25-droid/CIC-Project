# Authoring test: blind read and unsealed results

## The blind read

This is the managing thread's read of the blind set at `abd2aa5f`. It was posted before the key was opened and is copied here verbatim.

> The bar for each rendering, as-is: every clause present, nothing added, modern English, whole sentences of one thought each, nothing past about 25 words, and no word whose modern sense misleads.
>
> Per record (A / B):
> 1. basil-canon-to-amphilochius: pass / pass. B reads more naturally.
> 2. basil-on-the-doxology-challenge: FAIL / pass. A has sentences of 45 to 60 words, and "these words" loses "syllables", which Basil's argument turns on.
> 3. what-is-the-written-source: FAIL / pass. A keeps a conditional of more than 50 words.
> 4. signs-and-things-signified: pass / pass. The source's own cut-off, so the ellipsis is right.
> 5. dispute-to-learn: pass / pass.
> 6. ever-let-the-bridegroom: pass / FAIL. B keeps "sick of love", which a modern reader hears as "tired of love". A's "sick with love" is the translation.
> 7. melito-no-phantom: FAIL / pass. A's last sentence is about 90 words.
> 8. ignatius-truly-born: pass / FAIL. B runs on at about 55 words. Both speak the editor's supplement "[truly] died" as "truly died". Flag this for Mark as a question about what may be added, not as a fault of either author.
> 9. polycrates-to-victor: pass, with a flag / FAIL. B keeps a sentence of about 70 words. A restructures "in accordance with the tradition of my relatives" into "follow the tradition", which is a small syntactic reinterpretation. Flag it for Mark.
> 10. warned-before-baptism: FAIL / pass. A keeps "let him..." and closes on a run-on of about 50 words.
> 11. tatian-barbaric-writings: pass / FAIL. B's "too godly" shifts "too divine", and its first sentence runs long.
> 12. the-grades-here-in-the-church: FAIL / pass, with a flag. A is one sentence of about 50 words. Both drop "Since", which turns a subordinate reason into an assertion. Flag it for Mark.
>
> Tally: A passes 7 of 12, B passes 8 of 12. Preferred per record: B for 1, 2, 3, 7, 10, 12; A for 6, 8, 9, 11; ties for 4 and 5.

## The key, unsealed

`Authoring-Test-Key.json` has SHA-256 `6a3871e7b83393d19fb8f86349c382af47fc2444be2209286cd5f87e070e7392`, which matches `Authoring-Test-Key-Seal.md`.

Each author reported its own model id: `claude-sonnet-5` and `claude-opus-5-5`.

| # | Record | A | B | Read (A / B) | Preferred |
|---|---|---|---|---|---|
| 1 | basil-canon-to-amphilochius | Opus 5.5 | Sonnet 5 | pass / pass | B, Sonnet 5 |
| 2 | basil-on-the-doxology-challenge | Sonnet 5 | Opus 5.5 | FAIL / pass | B, Opus 5.5 |
| 3 | what-is-the-written-source | Sonnet 5 | Opus 5.5 | FAIL / pass | B, Opus 5.5 |
| 4 | signs-and-things-signified | Opus 5.5 | Sonnet 5 | pass / pass | tie |
| 5 | dispute-to-learn | Sonnet 5 | Opus 5.5 | pass / pass | tie |
| 6 | ever-let-the-bridegroom-sport-with-you | Opus 5.5 | Sonnet 5 | pass / FAIL | A, Opus 5.5 |
| 7 | melito-no-phantom | Sonnet 5 | Opus 5.5 | FAIL / pass | B, Opus 5.5 |
| 8 | ignatius-truly-born | Opus 5.5 | Sonnet 5 | pass / FAIL | A, Opus 5.5 |
| 9 | polycrates-to-victor | Opus 5.5 | Sonnet 5 | pass (flag) / FAIL | A, Opus 5.5 |
| 10 | warned-before-baptism | Sonnet 5 | Opus 5.5 | FAIL / pass | B, Opus 5.5 |
| 11 | tatian-barbaric-writings | Opus 5.5 | Sonnet 5 | pass / FAIL | A, Opus 5.5 |
| 12 | the-grades-here-in-the-church | Sonnet 5 | Opus 5.5 | FAIL / pass (flag) | B, Opus 5.5 |

## Tally by model

| | Opus 5.5 | Sonnet 5 |
|---|---|---|
| Passed the blind read | 12 of 12 | 3 of 12 |
| Preferred, of the 10 records that were not ties | 9 | 1 |
| Flagged for Mark by the reader | 2 (records 9, 12) | 0 |
| Blind-read reasons for failing | none | sentences running long (8 records; about 45 to 90 words where the reader gave a count); "sick of love" kept; "too godly" for "too divine"; "these words" for "syllables" |
| Flagged by either grader, by majority (Haiku 4.5, Sonnet 4.6, 3 runs each) | 3 (melito, ignatius, warned-before-baptism) | 1 (basil-canon) |
| Sentences flagged by the sentence-completeness check | 0 | 1 (basil-on-the-doxology-challenge) |

Notes on the machine scores:
- The graders flagged more Opus 5.5 renderings than Sonnet 5 renderings. The human read found the reverse. The grader prompt asks only about clause coverage, never about sentence length, and sentence length was the most common reason for failing.
- The one sentence-completeness flag is on a sentence that has a subject and a finite verb ("You, though, ... have said that ..."). It reads as the checker's misparse of a sentence broken up by dashes, not as a real fragment.

## Questions for Mark raised by the reader

These are questions about the rules, not faults of either author.

1. **Record 8:** both authors spoke the editor's supplement "[truly] died" as "truly died". The question is whether an editor's bracketed supplement may be voiced.
2. **Record 9:** Opus 5.5 turned "in accordance with the tradition of my relatives" into "follow the tradition", a small change to the sentence's structure.
3. **Record 12:** both authors dropped "Since", which turns a subordinate reason into an assertion. The source excerpt has no main clause.

## Cost

- **Authoring:** Claude Code session credits, two subagents, one run each.
- **Bedrock:** $0.63, for grading the 24 blind renderings with Haiku 4.5 and Sonnet 4.6, 3 runs each. This ran under the earlier brief (reviewer thread, 2026-09-24), before the managing thread's rule of no new Bedrock spend without a go. No other Bedrock spend.
