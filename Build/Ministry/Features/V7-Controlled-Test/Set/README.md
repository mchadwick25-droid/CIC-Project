# Arm A, frozen (Spec V1)

Arm A is fleet graded run 1 for alx, pahc and syr. These files are copied from branch claude/fleet-run-1-analysis at commit 4973efc8287e13ffcc775c198c1ca0f94234904d, folder fleet-graded-run-1 in the engine's m3 reports. That folder is not on `main`.

`../tools/extract_a.py` writes every file here except this one. `../tools/test_extract_a.py` checks them. No file here holds probe text, a draft or a request. Probes are named by probe id and cell.

## The files

| File | What it holds | Copied from |
|---|---|---|
| `A_alx.jsonl`, `A_pahc.jsonl`, `A_syr.jsonl` | One line per probe: probe id, cell, question id, `answer_text`, citations, citation entries, usage, `seconds_to_first_text`, `seconds_total`, stop reason, `priced_usd` | `<world>.json` and `ledger-<world>.jsonl` |
| `A_run_settings.json` | Per world: run commit, model id, region, max tokens, package hashes, shape and seal hashes, ledger total | `<world>.json` run settings and the ledger |
| `A_reviews_<world>.json` | The second-pass grades for all 28 probes, and the outside-referee findings for the 10 probes each referee read, by probe id | second-pass and outside-referees in analysis-2026-10-29 |
| `repeat_draw.json` | The seed (20261103) and the 42 probes B answers twice | drawn by the script |
| `SHA256SUMS` | SHA-256 of every other file here, this README included | written last by the script |

Question ids (`q_id`) come from `../../Answering-From-Sources/Cross-World-Test_2026-11-02/alx/set.yaml`. The mapping is the same in every world.

## Verified

- 28 lines per world, 84 in all. Each `answer_text` is byte-equal to the run file's.
- Every probe has one hold line and one settle line in its world's ledger. Settle lines are in probe order, and each one's usage equals its probe's usage. So `priced_usd` is that probe's own call.
- Priced cost by world, from the ledger: alx $0.6857, pahc $0.6587, syr $0.6554. Total $1.9998.
- The gate replay reproduces every answer, 84 of 84. Its shown sentences (removed=false), in order, tile `answer_text` exactly. Between sentences there is one space or one blank line.
- The repeat draw: 14 probes per world, 2 from each family (C, F1 to F6). Within each world, two registers are drawn 4 times and two 3 times.
- The outside-referee item numbers map to probes through the referees' KEY.json. Each mapped probe's answer appears in that item of the referee packet.

## What did not match

- **Offered record ids were not saved.** The run's `request` field holds only the model id and max tokens. It has no evidence block. So `offered_record_ids` is null on every line. The `draft_marker_ids` field lists the `[[id]]` markers in the saved draft instead. These are the ids the voice cited, not the set it was offered. The offered set could be rebuilt without a model call by replaying evidence assembly at each world's run commit, the way the engine's gate replay does. That needs engine work, which V1 may not do. Test Plan §3, item 1 now says so and gives the replay. A's run commits have the same engine, records and packages as the `live` tree.
- **The gate replay does not keep paragraph breaks.** Joining its sentences with one space gives `answer_text` byte for byte in 1 of 84 answers (one syr answer). The other 83 have blank lines between some sentences: 95 in alx, 71 in pahc and 67 in syr. The test checks the tiling, with only a space or a blank line between sentences.
- **The report's own spend is lower than the ledger.** Each run file's `actual_usd_spent` (alx $0.6233, pahc $0.5989, syr $0.5958) is the ledger total divided by 1.10, the Bedrock regional rate. `priced_usd` uses the ledger. Both are kept in `A_run_settings.json`.
- **The referee packets are not copied.** Each world's referee packet holds the question wording. Only its SHA-256 is kept.
