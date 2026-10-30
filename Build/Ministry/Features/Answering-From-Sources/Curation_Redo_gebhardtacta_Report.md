# Curation redo report: acta-martyrum-selecta_gebhardt1902

Drafter: Sonnet 5.5. File: `Sandbox/answering-library/curation/acta-martyrum-selecta_gebhardt1902.yaml` (65,693 words by the brief; 65,892 by the checker's count).

## Time and effort

- Start 2026-10-30T00:25Z, end 2026-10-30T00:30Z. About 5 minutes.
- Check runs: 2 (baseline, after the edit).
- Entries added or changed: 7 `fixes` (5 in `perpetua-greek`, 2 in `pionius`), 4 hand-listed lines added to `perpetua-greek` (3821, 4043, 4191, 4416), 1 `pionius` pattern widened (optional margin number), 1 `expected_gaps` entry, 8 evidence entries. 0 explicit divisions, 0 `ocr_map` entries. Status set to `drafted`.

## What was wrong

Series `perpetua-greek` read 1 to 6, 9 to 11 (with 4128 mis-set), 14 and so on. Greek chapters whose heads the rule did not list or read wrongly:

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
All checks PASS: uniqueness, coverage 100.0%, oversize 0, rules and evidence, word completeness 65892 = 65892, 217 of 217 byte ranges exact. Series perpetua-latin: 21 readings, no defects. Series pionius: 23 readings, first 1, last 23, no defects. Series perpetua-greek: 20 readings, first 1, last 21, one gap (6 to 8 at line 3821), listed in `expected_gaps`. RESULT: PASS.

## Remaining defects

- Greek chapter VII of the Perpetua (Greek text begins at line 3765, `αὐτῇ τῇ νυκτὶ ἐδηλώθη μοι τοῦτο`) shows no numeral in this scan or in the sister scan (line 4054 onward). The numeral is not set; the sequence alone would give VII. The gap is listed in `expected_gaps`, but the evidence is only that the scan prints none: it does not show that the edition prints none. The Greek VII text sits inside the division `piece7/lat-ch7`, so it stays addressable.
- The `warn` lines for `pionius` list hand-listed lines that look like headings and are not: verse numbers inside the Greek text, apparatus lines and running heads. They do not change the result.

## Judgment calls for the Opus reader

- Every set numeral rests on a Latin counterpart or a running head plus the matching text, not on sequence. The one numeral resting on sequence alone (Greek VII) is left unset.
- Running-head hazard: not present. The `pionius` rule starts divisions at chapter heads, not at running heads; the pattern excludes lines beginning `Martyrium`, and running heads that start with a page number do not match. A running head falls at the end of the preceding chapter (for example line 5632 at the end of XXI), and chapter XXII starts at 5638.
- The sister Knopf edition has no Greek Perpetua or Pionius (its Greek is not recoverable), so it gave no second instance; the sister Gebhardt scan was used for the Pionius running heads IX and XX only.
- The expected_gaps entry for Greek VII is a judgment call: it records a scan limit as the explanation for a gap.
