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

## Held-out half, 2026-10-30

This is the one final scoring on the sealed held-out half. The judge prompts and the goldset code were not changed before it. Every helper was the `judge-reader` type, which holds only Read and Write.

The verifier ran on the plan's current Haiku, not on Haiku 4.5. The citation-recall judge ran on Sonnet 5.5. So, as on the calibration half, these numbers measure the judge prompts. They do not yet measure the exact production models.

Natural items with a supported or unsupported gold label: 385. Of these, 78 are unsupported and 307 supported. Every count below is out of those 385.

| Decider | Recall on unsupported | Precision | Supported items flagged (false alarms) | Agreement with gold (kappa) |
|---|---|---|---|---|
| Verifier (plan's Haiku) | 0.885 (69/78) | 0.711 | 28/307 (9.1%) | 0.73 |
| Citation-recall (Sonnet 5.5) | 0.885 (69/78) | 0.873 | 10/307 (3.3%) | 0.85 |
| Current gates | 0.346 (27/78) | 0.415 | 38/307 (12.4%) | 0.24 |

Constructed items: 93, all unsupported by construction. Only the catch rate means anything here.

| Class | Items | Verifier caught | Citation-recall caught |
|---|---|---|---|
| Embedded voice | 27 | 27 | 26 |
| False friend | 24 | 20 | 22 |
| Generalisation | 20 | 18 | 16 |
| Negation or modal shift | 22 | 21 | 22 |
| All | 93 | 86 (92.5%) | 86 (92.5%) |

The gates never saw the constructed items.

### Seed controls

The 60 seed controls are sentences their records state outright. A judge that calls one of them unsupported raises a false alarm.

| Judge | False alarms |
|---|---|
| Verifier (plan's Haiku) | 0/60 |
| Citation-recall (Sonnet 5.5) | 0/60 |

### Files set aside

1,112 prompts went out: 496 held-out items and 60 controls, for each judge. One reply was set aside, unread by the scoring:

- `replies/cx-4494962e8f6e.verifier.txt`. A verifier helper misspelled the item id of `cx-449496308e6f`. No prompt has that name.

One citation-recall reply, for `gs-42afe776bef0`, was never written. Both prompts were re-run once, the same way, and both replies passed the check. Every one of the 1,112 replies then matched its prompt and held one JSON object with the right fields.

### Elapsed time

- Export and list building: about 1 minute.
- 20 helpers in parallel, 56 prompts each (52 in the last list per judge): the fastest list took 2 min 10 s, the slowest 3 min 33 s. About 4.5 minutes from launch to the last reply.
- Check and re-run of the two prompts: under 1 minute.
- Import and scoring: seconds.

From export to score, the run took about 7 minutes.
