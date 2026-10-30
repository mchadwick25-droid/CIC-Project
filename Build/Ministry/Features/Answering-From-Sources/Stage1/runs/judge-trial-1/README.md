# Judge trial 1, in plan

The trial ran on Claude Code subagents, with no metered call (Mark, 2026-10-30, option (a)). The verifier judge ran on the plan's current Haiku, not on Haiku 4.5, the production model. The citation-recall judge ran on Sonnet 5.5. So these numbers say how well the two judge prompts work. They do not yet measure the exact production pair.

The judge prompts are `goldset/trial.py` JUDGE_PROMPTS, unchanged since the gold set was sealed. Nothing was tuned on the calibration half.

## Calibration half, 2026-10-30

Natural items with a supported or unsupported gold label: 368, of which 66 are unsupported. Every count below is out of those 368.

| Decider | Recall on unsupported | Precision | Supported items flagged (false alarms) | Agreement with gold (kappa) |
|---|---|---|---|---|
| Verifier (plan's Haiku) | 0.955 (63/66) | 0.670 | 31/302 (10.3%) | 0.73 |
| Citation-recall (Sonnet 5.5) | 0.818 (54/66) | 0.761 | 17/302 (5.6%) | 0.74 |
| Current gates | 0.212 (14/66) | 0.209 | 53/302 (17.5%) | 0.04 |

Constructed items: 79, all unsupported by construction. Only the catch rate means anything here.

| Class | Items | Verifier caught | Citation-recall caught |
|---|---|---|---|
| Embedded voice | 20 | 20 | 20 |
| False friend | 20 | 18 | 18 |
| Generalisation | 20 | 16 | 18 |
| Negation or modal shift | 19 | 18 | 15 |

The gates never saw the constructed items.

## Incident

Several of the first verifier subagents wrote replies under the wrong file names, and some wrote over citation-recall replies. Every such file was moved aside, unread by the scoring. The 151 prompts affected were re-run with exact paths. The quarantined files are listed in `Quarantined_Replies.txt`.

Two of those subagents also used tools outside their task. One tried to create a session, which was refused. One used a session interrupt.

## Held-out half: not yet run

The held-out run needs helpers that hold only Read and Write. This session's helper types all carry session tools. So the one final scoring on the held-out half waits for a session where a Read/Write-only helper type is loaded. Its prompts are exported (judge prompts unchanged), with the 60 seed controls.
