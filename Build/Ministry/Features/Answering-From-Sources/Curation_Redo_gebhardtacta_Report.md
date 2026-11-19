# Curation redo report: acta-martyrum-selecta_gebhardt1902

Drafter: Sonnet 5.5. File: `Sandbox/answering-library/curation/acta-martyrum-selecta_gebhardt1902.yaml` (65,693 words by the brief; 65,892 by the checker's count).

## Time and effort

- Start 2026-10-30T00:25Z, end 2026-10-30T00:30Z. About 5 minutes.
- Check runs: 2 (baseline, after the edit), plus 1 after the Greek VII head at 3729 was added (second pass, 2026-10-30T00:39Z to 00:41Z).
- Entries added or changed: 8 `fixes` (6 in `perpetua-greek`, 2 in `pionius`), 5 hand-listed lines added to `perpetua-greek` (3729, 3821, 4043, 4191, 4416), 1 `pionius` pattern widened (optional margin number), 0 `expected_gaps` entries, 9 evidence entries. 0 explicit divisions, 0 `ocr_map` entries. Status set to `drafted`.

## What was wrong

Series `perpetua-greek` read 1 to 6 (VII at 3729 was missed), 9 to 11 (with 4128 mis-set), 14 and so on. Greek chapters whose heads the rule did not list or read wrongly:

- VII, line 3729, printed `25 VIL Καὶ μετ’ ὀλίγας ἡμέρας προσευχομένων ἡμῶν` (final I read as L): set to 7. Three instances: the Latin counterpart VII at 3709 (`Post dies paucos, dum uniuersi oramus`), the running heads VII at 3698 and 3746, and the sister scan line 4048 (`25 VII. Kai ...`).
- VIII, line 3821, printed `25 VII Kai`: set to 8. Second instance: the Latin counterpart VIII at 3800 (`VIII. Die quo in neruo mansimus`) and running heads VIII at 3789.
- XI, line 4043, printed in Greek letters `ΧΙ. ᾿λλὰ`: set to 11. Counterpart: Latin XI at 4025 (`Sed et Saturus benedictus`), running heads XI at 4019 and 4062.
- XII, line 4128, printed `XI. Ko` (the dropped I): set to 12. Counterpart: Latin XII at 4112 (`Et uenimus prope locum`), running head XII at 4109.
- XIII, line 4191, printed `20 XII.`: set to 13. Counterpart: Latin XIII at 4173 (`Et exiuimus`), running head XIII at 4161.
- XVIII, line 4416, printed `XVII.` a second time: set to 18. Counterpart: Latin XVIII at 4397 (`Inluxit dies uictoriae`), running heads XVIII at 4384 and 4428.

Series `pionius` lacked three chapters:

- IX, line 5132, printed in Greek letters `ΙΧ. Εἶτα`: set to 9. Running head at 5125 `Martyrium S. Pionü IX. 103`; the sister scan has the same running head (line 5529).
- XVII, line 5465, printed `15 XVII. Kai`: the pattern now accepts a margin line number, no fix. Running head at 5445 `Pionii XVII. XVIII.`.
- XX, line 5558, printed `AX. Σιωπῶντε`: set to 20. Running head at 5533 `112 ... Martyrium S. Pionii XX.`; the sister scan has `Martyrium S. Pionii XX.` at line 5991.

The unexplained line 4356 (`piece7/lat-ch17`) is a correct Latin XVII head (`XVII. Pridie quoque`, running head XVII at 4343). Its sample line carries Greek text on the same line, which is the scan's own mixing; no change was needed.

## Final check output

class after: curated (was partial). Divisions 88 (86 body, 2 apparatus). Rule hits: perpetua-latin 21, perpetua-greek 20, pionius 23.
All checks PASS: uniqueness, coverage 100.0%, oversize 0, rules and evidence, word completeness 65892 = 65892, 218 of 218 byte ranges exact. Divisions 89 (87 body, 2 apparatus). Rule hits: perpetua-latin 21, perpetua-greek 21, pionius 23. Series perpetua-latin, perpetua-greek and pionius: no repeats, backward steps or gaps (greek 1 to 21, pionius 1 to 23). RESULT: PASS.

## Remaining defects

None in the numbering. The `warn` lines for `pionius` list hand-listed lines that look like headings and are not: verse numbers inside the Greek text, apparatus lines and running heads. They do not change the result.

## Judgment calls for the Opus reader

- Every set numeral rests on a Latin counterpart or a running head plus the matching text, not on sequence. No numeral rests on sequence alone.
- Running-head hazard: not present. The `pionius` rule starts divisions at chapter heads, not at running heads; the pattern excludes lines beginning `Martyrium`, and running heads that start with a page number do not match. A running head falls at the end of the preceding chapter (for example line 5632 at the end of XXI), and chapter XXII starts at 5638.
- The sister Knopf edition has no Greek Perpetua or Pionius (its Greek is not recoverable), so it gave no second instance; the sister Gebhardt scan was used for the Pionius running heads IX and XX only.
