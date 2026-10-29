# Engine change ledger, 2026-10-29 (branch claude/engine-cut-repair)

Source: `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md`, finding E1 (engine, brief #1186). Replay of the cut step on fleet graded run 1: 308 saved drafts, 11 worlds, `apply_net` re-run with no model call.

## Bench and commands

The bench is the replay of `engine.m4.turn.apply_net` on the saved drafts. It reproduced the shipped answers byte for byte, 308 of 308, on the old code. `replay_branch.py` is `replay.py` with the repo path and the output path taken from the environment, so the same bench runs against this branch's `engine/`. Every command ran with all `AWS*` and `ANTHROPIC*` variables unset; the network SDKs are replaced by the no-call stubs.

```
unset $(env | grep -E '^(AWS|ANTHROPIC)' | cut -d= -f1)
BENCH_REPO=/home/user/fr1-records BENCH_OUT=<out>.jsonl python <bench>/replay_branch.py
```

- Before (branch at 5c08e090, `engine/` identical to the bench copy): `results_before.jsonl`: 308 of 308 match the shipped text, 297 sentences cut, 145 answers with at least one cut. Same output as the original `replay_results.jsonl`.
- Tests: `PYTHONPATH=<scratchpad>/pylib:/home/user/fr1-records python -m pytest engine/m4/tests engine/m3/tests -q -p no:cacheprovider` (pytest, anthropic, httpx, boto3, pyyaml installed into a scratchpad directory with `pip install --target`; no call is made by any test).
- Gates: `python -m engine.m6.cli check`, `python -m engine.m9.cli check` (see the end).

Counts of "before" below are from `results_before.jsonl`.

---

## L1. Stop the net cutting sentences grounded in their own cited record

**Failure targeted.** E1: the rule "gives a quote record's words without placing it" (`REASON_QUOTE_WORDS`) cuts sentences that are word for word in the witness, story or term record they cite. The replay found 30 cut sentences that are verbatim in a record they cite, and 44 that contain a quoted span verbatim in the records.

**What the 30 and 44 are, by the rule that cut them (measured before any code change).**
- Only 1 of the 30 verbatim sentences was cut by the quote-words rule (gallic c-t, `gallic.term.grace`). The rest were cut by: quotation typed by the voice (17), words after an attribution (6), tells an offered story without placing it (4), tagged to an unplaced quote record (1), lead-in names no speaker (1).
- The 20 sentences cut by the quote-words rule: 6 sentences are 55 percent or more in the words of a quote record and in the cited record's own wording only inside the cited record's quotation marks (lpc f6-t, gallic c-t, gallic f4-e, gallic f6-t, and two more), 14 cite no record that holds the words.
- The existing rule already lets a witness, story or term retell its own wording: `_quote_words_of` ignores shared words that the sentence's own tagged records state outside their quotation marks (`_words_of`, `_sequence_of`). What is left firing is a sentence whose shared words stand in the cited record only inside a quotation of a quote record's words.

**Candidate change (the only narrowing that fits E1).** In `QuotationIndex._quote_words_of`, count the words of a cited witness, story or term anywhere in its text (inside its quotation marks too) as explaining the shared words.

**Exact answers that should change.** gallic:c-t, gallic:f4-e, gallic:f6-i, gallic:f6-t, lpc:f6-t (the five sentences that the candidate lets through, found by running it).

**Expected effect.** Those five sentences survive.

**Must NOT change.** Words of a quote record still reach a participant only if code placed them. Zero new shipped sentences may contain words of a quote record.

**Order note.** This entry was written after the candidate had been run once on the bench, because the candidate was never committed (it was undone with `git checkout` before any commit).

**Measured result (candidate run on the bench).** Cuts 297 to 292. Five sentences survive that were cut before:

| world:probe | cited record | verbatim in it? | words of a quote record? |
|---|---|---|---|
| lpc:f6-t-probe-01 "He told him plainly what awaits those who will not believe: on the day of judgment, an ever-burning Gehenna will burn up the condemned, with no respite or end to their torments" | `lpc.witness.no-salvation-outside-the-church` | no (ratio 0.93) | yes: 10 of 13 words in `lpc.quote.an-ever-burning-gehenna` |
| gallic:c-t-probe-01 "Grace always co-operates with our will, and assists, protects, and defends it" | `gallic.term.grace` | yes | yes: 6 of 6 words in `gallic.quote.chaeremon-grace-requires-our-effort` |
| gallic:f4-e-probe-01 "What Cassian carried to us was Egypt's, not theirs: the customs of the monasteries ..., as they were delivered to him by the fathers" | `gallic.term.customs-of-the-monasteries` | no (ratio 0.91) | yes: 8 of 10 in `gallic.quote.customs-delivered-to-us-by-the-fathers` |
| gallic:f6-i-probe-01 "He held that a secular ruler judging a Church cause was a foul and unheard-of thing" | none (untagged) | no | yes: 7 of 9 in `gallic.quote.secular-ruler-judge-in-ecclesiastical-cause` |
| gallic:f6-t-probe-01 "Grace works with the will, assisting and defending it, in a relation that cannot be fully grasped by the mind and reason of man" | `gallic.term.grace` | no (ratio 1.0) | yes: 8 of 11 in `gallic.quote.chaeremon-three-stages-of-grace` |

All five newly shipped sentences contain words found in a quote record and none was placed by code. The rule fires only on a sentence that gives a quote record's words, so any exemption for it lets those words through. Five of five fail the "zero" condition.

**Decision: reverted** (never committed). The rule cannot be made narrower without letting quote-record words through. A witness's own paraphrase is already exempt. What the replay counted as "grounded sentences cut" are, by reason, typed quotations and words after an attribution (31 and 6 of the 44 and 30), which are the quotation-placement policy (only code sets a quote), not the quote-words rule; loosening them would weaken a gate, and is not done here.

**Commit.** none (code undone before commit; this entry is the record).

**For the project lead (not changed).** 22 of the 30 verbatim sentences and 31 of the 44 quoted-span sentences were cut as "quotation typed by the voice" or "words after an attribution". In about half of them no quote record holds the words; only a witness or story does, inside its own quotation marks. Whether the voice may type such a span is a policy decision on the typed-quotation rule, not an engine fix.

---

## L2. Orphan guard

**Failure targeted.** E1 residue: after the net or placement removes a sentence, the next shipped sentence can open with a pronoun, demonstrative or connective whose referent was in the removed one (register-8 "these gifts", source-awareness-1, scholarly-1, register-6, DI-9, DI-10).

**Design.** A pure function (`engine/m4/orphan_guard.py`) takes the voice's draft (markdown stripped), the removed sentences with their drafts, and the net's final sentences. It lists each sentence that (a) is the first surviving sentence after a removed run in the voice's own text, (b) opens with an unresolved anaphor (he, she, it, they, his, her, its, their, him, them, this, that, these, those, such, the same, so, yet, but, then, and, with "and" counting only before a pronoun) and (c) has no surviving sentence before it in its own paragraph of the voice's draft. Stage 1 exposes the list as `net_result["reply_shape"]["orphaned"]` and changes no text. Stage 2 (drop) happens only if the hand-checked precision of the list is at least about 85 percent.

**Exact answers that should change.** None in stage 1 (text unchanged, 308 of 308 identical). Candidate list from the prototype: 15 sentences in the answers lpc:c-p, lpc:f1-e, lpc:f1-p, lpc:f2-i, lpc:f3-i, desert:f2-e, ijc:f1-e, ijc:f2-t, alx:c-p, alx:f2-i, witt:f1-i, witt:f6-t, pahc:c-i, pahc:f3-e, pahc:f6-p.

**Expected effect.** `orphaned` lists those sentences. A second prototype rule (any sentence after a removal that opens with an anaphor, 93 sentences) is the replay's rule; it is not used.

**Must NOT change.** Shipped text, citations, `removed`, `placed`. No answer emptied.

**Measured result (stage 1, flag only).** After: 308 of 308 shipped texts identical to before and to the shipped answers; 297 cuts unchanged; 0 empty answers. `orphaned` lists 14 sentences in 14 answers (the 15 of the prototype less "And we called him God", which the final rule does not count: "and" counts only before a pronoun). Hand-check of every one, with the text that comes before it in the shipped answer:

| # | world:probe | sentence | truly broken? |
|---|---|---|---|
| 1 | lpc:c-p | That restlessness is not a failure on your part. | yes: the cut sentence was the restless-heart quotation |
| 2 | lpc:f1-e | These are real differences, and we do not resolve them. | no: the paragraph before sets out two views |
| 3 | lpc:f1-p | He told them their longing expectation was itself a prayer for him. | yes: speaker and audience cut |
| 4 | lpc:f2-i | Yet Scripture was not our only authority. | no: reads on the paragraph before |
| 5 | lpc:f3-i | These are real, substantial differences. | no: the paragraph before sets out two rules |
| 6 | desert:f2-e | This turn's ground teaches the right instinct: name the mediations. | no: not a back-reference (a build note spoken aloud; a separate defect) |
| 7 | ijc:f1-e | But that same council, before it broke up, granted Constantinople equal privileges ... | no: the council is named in the paragraph before |
| 8 | ijc:f2-t | So scripture was our authority, yes - but always read inside the church's own confession ... | no: stands on its own |
| 9 | alx:c-p | It was love for the Holy Word, and for the man who taught him. | yes: the cut sentence was Gregory's spark quotation |
| 10 | alx:f2-i | That is the center. | yes: first sentence of the answer |
| 11 | witt:f1-i | He is also a gracious God, and we could not doubt it. | no: God is the subject of the paragraph before |
| 12 | witt:f6-t | That condition, inherited and real, is where the judgment begins. | yes: the condition is never stated |
| 13 | pahc:f3-e | He meant it as mockery. | yes: the satirist sentence was cut |
| 14 | pahc:f6-p | That was the instruction we have. | yes: the marriage instruction was cut |

Precision 7 of 14 (50 percent), below the 85 percent bar. The replay's wider rule (93 sentences after any cut, mid-paragraph included) was hand-labelled too: about 35 of 78 mid-paragraph cases truly broken (45 percent); a word-overlap test with the removed sentence raised that to 13 of 19 (68 percent), still below the bar. Dropping would have emptied no answer and cost no answer its only cited sentence (checked on all 14), but would have removed 7 sentences that read fine.

**Decision: keep the flag, do not drop.** Text unchanged. No deterministic rule found at or above the bar; dropping stays off.

**Not found by the guard.** It cannot see a pronoun that now points at the wrong person (pahc f3-e) or a dependent sentence with no anaphor ("Grief itself was allowed.").

**Commit.** b9bfd4baa (`engine: report sentences orphaned by a removal`).

---

## Tests and gates

- New: `engine/m4/tests/test_orphan_guard.py`, 7 tests: orphan after a cut flagged and text kept; a pronoun with a kept sentence before it in its paragraph not flagged; nothing cut, nothing flagged; a name opener not flagged; the function reads only its arguments; a witness sentence with its own inline words survives; a sentence giving a quote record's words without placing it still goes. `test_quote_placement.py` line 265 now expects the new `orphaned` key in `reply_shape` (an exact-equality assertion on the dict).
- Before (branch as found): `engine/m4/tests` 10 failed, 1043 passed. After: `engine/m4/tests engine/m3/tests` 14 failed, 1118 passed on the first run; the one new failure (the exact-equality test above) was fixed, leaving the same failures as before. The remaining failures are not caused by these changes: 6 in `test_world_loader.py` and 3 in `test_live_turn_report.py` (no `packages/` in this sparse checkout), and 3 in `engine/m3/tests` (`test_stage4_selftest_passes`, two in `test_live_admission_run.py`; PackageRefused: no manifest under `packages/`), which fail the same way on the branch without these changes.
- `python -m engine.m6.cli check` could not run: it needs `cic-website/data/world-census.json`, absent from this sparse checkout. `python -m engine.m9.cli check` could not run: it imports `texts_registry`, absent here. Neither was run.
