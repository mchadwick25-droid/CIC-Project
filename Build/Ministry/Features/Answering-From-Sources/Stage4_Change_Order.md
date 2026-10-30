# Stage 4 Change Order: bound drafting, verify and rewrite, proved on lpc in shadow

Approved to proceed by Mark, 2026-10-30 (choice box, direct; version 3 of the draft, as written here). Decision-Log entry 31 records the approval. Shadow only on lpc, free in-plan work, no gate retired. It starts when Stage 2 lands on lpc.

## Scope

Shadow means it runs beside today's path and changes nothing a reader sees. Engine and data path only; no layout or screen work.

## What it authorizes

- Bound drafting, a judge check and one rewrite, run in shadow on lpc only, on the saved drafts and on the lpc test set (`S3-Test100/`).
- Free work only: helpers in this plan draft and judge. No metered model call.
- The rigor line (Decision-Log 29 and 30, Mark, 2026-10-30): a drafted sentence is a quotation or a close paraphrase in the author's name. No inference from a passage no reviewed record frames. The voice may be shown the source text around a quote or story, to understand what it was saying; that text never supports a sentence.
- A fit step: every quote or story placed in an answer must fit the question asked, in its source context, and the answer must address the question that was asked.
- A retelling fitted to one question may run on this path, as Stage 3 ruled: each sentence bound to the record sentence it rests on and verified. If it fails, the voice falls back to a reviewed telling.

## What it does not authorize

- No production change and no gate retired. Retiring a gate is a later change order per world, with the numbers attached.
- No world rebuild and no record rewrite.
- No paid run. A production judge or a production fit judge on a paid model needs its own decision and a cap Mark names, raised only if a paid step is absolutely necessary, by name.

## Design

- Judges in shadow: citation-recall is the main judge, the verifier runs beside it for comparison only. This is a coordination-level ruling reviewed by AI, not Mark's own (Decision-Log 29).
- Context reaches the voice as blocks marked context, taken from the source division around each offered quote or story. Context blocks have ids that cannot be bindings. Code rejects a binding to one before any judge runs, and a sentence left with no valid binding is held out of the rewrite.
- The fit step reads the question, each placed quote or story, the record's own statement of what it means, and its context. It returns fits, partly fits, or off-point, with a reason. Off-point comes out, and the next candidate is tried or the answer goes without one. Partly fits stays only if the lead-in states the limit.
- The fit step is calibrated first on twenty planted pairs built from lpc records: a real quote or story, a question on-topic by words and wrong in application. It must catch at least 19 of 20 before its verdicts count. The bar is the coordination thread's call, reviewed by AI, and follows the seeded-defect catch rate already ruled for the specialist.
- Three-level transparency is unchanged: the mark in the text, the hover with brief context, the click to the full page with links to the source references and vendored documents. The full page already links the source division, which contains the text the voice was shown. The log records which context blocks each answer was offered.

## Numbers it must move

Judge results so far are in `Stage1/runs/judge-trial-1/README.md`; held-out half, 385 natural items.

| Measure | Today | Target |
|---|---|---|
| Recall on unsupported sentences, held-out | 0.346 (current gates) | At least 0.95 (ruled 2026-10-29) |
| Precision on unsupported, held-out | 0.415 (current gates) | At least 0.85 (ruled 2026-10-29) |
| False alarms on supported sentences | 12.4% (current gates) | No worse than today |
| Constructed defects caught, per class | The gates never saw them | At least 90% in every class |
| Seed control false alarms | Not measured for the gates | 0 of 60 |
| lpc test set: cuts and orphan flags | 45 cuts and 13 orphan flags on the 28 sealed probes | Fewer, with answer quality no worse |
| Fabrication on retold stories | No shortened retellings yet | Zero added content; every event kept |
| Fit to the question, placed quotes and stories | Not measured | Reported beside the others; no target set until the fit step is calibrated |

The catch and precision targets are ruled. The other rows are proposals.

## Before it starts

- Stage 2 done on lpc (the Library thread's).
- The lpc test set frozen (`S3-Test100/`, Decision-Log 28 and 31).
- The shadow runner (`engine/m3/test100.py` and `engine/m3/reply_client.py`).

## Deferred

The production judge's spend and models, and a production fit judge, are deferred. They are raised only if a paid step is absolutely necessary, by name with a cap, under Mark's standing rule that spend questions are not put to him in advance.
