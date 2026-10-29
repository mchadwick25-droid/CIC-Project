# Answering From the Sources: Stage 1 Ledger

Companion to `Decision-Log.md`, entry 1 (2026-10-29). One line per stage 1
item. No line starts a paid run on its own. All costs are the proposal's
estimates, stated only where the proposal gives a figure; "not stated"
means the proposal gives none and none is invented. Owners are thread
names. Tiers: free / package check / metered.

Rule for every metered line: runs only as a live test Mark approves by
name with a cap, settings printed first, stops at the cap, and a paid bulk
run needs a small sample first, approved by Mark.

| Id | Item | What it does | Tier | Targets | Expected cost (estimate) | Blocker | Owner | Sample gate | Done when |
|---|---|---|---|---|---|---|---|---|---|
| S1-01 | Baseline live-path run on the 12 built worlds | Runs today's live path with a run manifest and saved reader outputs, before anything changes | metered (conversations) | Unknown starting numbers: shippable rate and cost per shippable answer on the live path, boundary leakage today, prompt size | Today $0.018 to $0.040 per answer, measured in fleet run 1; run total not stated | Waits for Mark's named cap [BLANK] | Coordination thread | Small sample approved by Mark, settings printed | Manifest and saved reader outputs filed; reviewer-shipped and outside-referee numbers reported for the live path, with cost per shippable answer |
| S1-02 | Gold set | Human-labelled sentences, bindings and verdicts from the twelve worlds' texts, lpc first, calibration and held-out split, blind labelling | metered (AI domain specialist, third lineage) plus Mark's adjudication time | Whether any judge can be trusted; six failure classes (supported, unsupported, false friend, negation and modal shift, generalisation, embedded voice) | Specialist cost not stated; waits for a named cap | Specialist ruled 2026-10-29 (AI specialist, Decision-Log entry 2). Waits for the two spend caps [BLANK, Mark] and Mark's weekly adjudication budget [BLANK, Mark] | Fable design thread, with the AI domain specialist | Not metered; the specialist and the second labeller are metered calls, see S1-03 | At least 40 labelled items per class; a fifth double-labelled by a model different from both judges; specialist passed the seeded-defect test (catch rate published, proposed at least 19 of 20) before its labels count; Mark has adjudicated every key-class disagreement plus a random sample; held-out set sealed from tuning |
| S1-03 | Second labeller (model different from both judges) | Labels at least a fifth of the gold set so no judge is measured against its own labels | metered | Judge agreement inflated by self-labelling | Not stated | Waits for Mark's named cap [BLANK] and for S1-02 labels | Fable design thread | Small sample approved by Mark | Labels filed for at least a fifth; disagreements queued for Mark |
| S1-04 | Judge trial in shadow | Runs the verifier and the citation-recall judge (different models) beside the current cut step, silence check and withheld-claim rule, without replacing them | metered | Whether the judge is no worse than the current gates on patristic and Reformation English, Latin and false friends | Judge adds an estimated $0.03 to $0.06 per answer when all sentences pass, $0.06 to $0.10 when the rewrite fires; trial total not stated | Waits for Mark's named cap [BLANK], for the gold set (S1-02, S1-03) and for the baseline (S1-01) | Fable design thread, coordination thread for runs | Small sample approved by Mark, settings printed | On the held-out set, recall on "unsupported" at least 0.95 at precision at least 0.85, published per failure class; compared with the current gates' decisions on the 308 saved drafts scored against gold labels; agreement with the specialist published. No gate retired |
| S1-05 | Contextual indexing of the twelve shelves | Contextual indexing of the union of the twelve shelves (338 files, about 154M tokens) | metered | Reach: whether passage retrieval finds what the records do not | About $150 once, at the vendor's rate of about a dollar per million tokens; lpc's shelf about 47M tokens | Waits for Mark's named cap [BLANK] and sample approval [BLANK]; proposal also ties it to the Library additions (stage 2 tooling) | Library thread | Sample on a small part of lpc's shelf, approved by Mark, settings printed, before the rest | Sample approved, then index built for the union, versioned by hash, outside the live and canonical trees; spend logged against the cap |
| S1-L1 | ALCE-style scoring of fleet run 1 | Scores the saved fleet run 1 answers for citation recall and precision, the per-answer grounding number CiC lacks | not stated | Per-answer grounding number | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L2 | Deterministic quoting on the replay | Tries selection-and-insertion quoting on the 308 saved drafts | free (replay bench, no model call) | Quotation errors from typed quotes | none | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L3 | Index one shelf and measure against the coverage maps | Indexes one world's shelf and compares what retrieval reaches with the coverage maps | not stated | Reach: whether passage retrieval finds what the records do not | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L4 | Cross-lingual test on Latin and Greek | Tests retrieval across Latin and Greek against English questions | not stated | Whether cross-lingual retrieval holds on the Library's languages | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L5 | Boundary benchmarks on one Representative | Runs the time-boundary benchmarks (TimeChara, CHARM) on one Representative | not stated | Boundary leakage, measured | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L6 | Recurrence of real questions | Measures how often real first questions recur | not stated | Whether reviewed openings pay for themselves | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |
| S1-L7 | Lazy-graph trial on three whole-shelf questions | Tries a lazy graph structure on three questions that need the whole shelf | not stated | Whether whole-shelf questions need a graph | not stated | Tier and cost to be confirmed by the Fable design thread before any run; if metered, waits for Mark's named cap [BLANK] | Fable design thread | If metered: small sample approved by Mark | Result filed with its numbers |

The proposal also lists what stage 1 is meant to find out (section 13,
"Not known, and found out in stage 1"): whether any judge holds at the
specialist's bar; how many plain-text files segment by script; how often
real first questions recur; how much boundary leakage exists today;
whether an offer of passages raises prompt size beyond what the length
line saves. These are not assigned to ledger lines by the proposal; they
are recorded here for the coordination thread to map to the seven
learning items above.

The seven learning items (S1-L1 to S1-L7) are as listed in the Fable design
thread's message of 2026-10-29 15:06 UTC about the landscape survey
(https://claude.ai/artifact/DuLhPWdET5RPvc9dwHyK3u). They have not been
confirmed against the survey page, and only S1-L2 is stated to be free;
the tier and cost of the others are for the Fable design thread to confirm
before any run.

Priority build line (Mark, 2026-10-29): Antiochene (Chrysostom), Latin
Apologists (Tertullian), Rome in the Age of Gregory the Great, Hussite and
Bohemian, Society of Jesus. Methodist and Franciscan: named for later, not
queued. Their record stage is outside stage 1.

Not in stage 1 (not authorized): gate retirement, rendering, bundles,
openings, any change to the production path.

## Caps, threads and elapsed time (2026-10-29, Decision-Log entry 3)

| Item | Cap in force | Thread | Started | Finished | Elapsed |
|---|---|---|---|---|---|
| Harness parity (prerequisite to S1-01): the admission harness runs the live path | none: free, hermetic tests only | Engine | 2026-10-29 17:11Z | 2026-10-29 17:23Z (local checks green; review round 1 pending) | 12 min |
| S1-01 baseline live-path run | none: both approvals withdrawn 2026-10-29; no metered call without Mark. The sample ran once before the withdrawal reached the thread: guard-priced $0.8275, all 4 voice calls failed, no answers. Free measures filed in `S1-01-free/` | Engine | 2026-10-29 18:16Z | not completed | 19 s of wall clock (sample) |
| S1-L2 deterministic quoting on the replay bench | none: free, no model call | Engine | 2026-10-29 17:23Z | 2026-10-29 17:29Z (review round 1 pending) | 6 min |
| S1-02 gold set and AI specialist | none yet [BLANK, Mark]; Mark adjudicates 2 h/week | Specialist and gold set | | | |
| S1-03 second labeller | none yet [BLANK, Mark] | Specialist and gold set | | | |
| S1-04 judge trial in shadow | $25 ceiling, sample first | Specialist and gold set | | | |
| S1-05 no-context index of the twelve shelves (paid context lines not authorized, Decision-Log entry 10) | none: free, no model call | Library | 2026-10-29 17:12Z | 2026-10-29 19:23Z (union index 354,589 passages built and verified; lpc retrieval bench filed; free retrieval trials running) | 2 h 11 min |
| Library stage 2, segmenter and union measurement (twelve shelves, 338 files) | none: free | Library | 2026-10-29 17:16Z | 2026-10-29 18:58Z (PR 1284 merged; report `Stage2_Segmentation_Report.md`) | 1 h 42 min |
| Library stage 2, source records fold into the corpus map (`shelf_row` pointers, twelve pull requests) | none: free | Library | 2026-10-29 17:16Z | not completed | |
| Library stage 2, curation layer and the 237 partial or unmarked plain-text files | none: free, in-plan | Library | 2026-10-29 18:55Z | layer merged 2026-10-29 19:35Z (PR 1291); wave 1 (lpc, 64 files) running | layer 40 min |
| Library stage of the five priority worlds | none: free, in-plan | Library | 2026-10-29 17:17Z | not completed (rcg and aec second reviews and latap Doc_02 in review) | |
| S1-L1, S1-L3 to S1-L7 | per item, when confirmed | Fable design thread is finished; engine thread confirms tier and cost | | | |

Dates and elapsed time are filled in by the thread that finishes the item.

