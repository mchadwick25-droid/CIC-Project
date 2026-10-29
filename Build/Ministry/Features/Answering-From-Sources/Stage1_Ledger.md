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
| S1-02 | Gold set | Human-labelled sentences, bindings and verdicts from the twelve worlds' texts, lpc first, calibration and held-out split, blind labelling | free (human labour) | Whether any judge can be trusted; six failure classes (supported, unsupported, false friend, negation and modal shift, generalisation, embedded voice) | No model spend stated; labour is the specialist's and Mark's | Waits for the specialist [BLANK, Mark] | Fable design thread, with the named specialist | Not metered; the model second labeller is a metered call, see S1-03 | At least 40 labelled items per class; a fifth double-labelled by a model different from both judges; Mark has adjudicated every disagreement; held-out set sealed from tuning |
| S1-03 | Second labeller (model different from both judges) | Labels at least a fifth of the gold set so no judge is measured against its own labels | metered | Judge agreement inflated by self-labelling | Not stated | Waits for Mark's named cap [BLANK] and for S1-02 labels | Fable design thread | Small sample approved by Mark | Labels filed for at least a fifth; disagreements queued for Mark |
| S1-04 | Judge trial in shadow | Runs the verifier and the citation-recall judge (different models) beside the current cut step, silence check and withheld-claim rule, without replacing them | metered | Whether the judge is no worse than the current gates on patristic and Reformation English, Latin and false friends | Judge adds an estimated $0.03 to $0.06 per answer when all sentences pass, $0.06 to $0.10 when the rewrite fires; trial total not stated | Waits for Mark's named cap [BLANK], for the gold set (S1-02, S1-03) and for the baseline (S1-01) | Fable design thread, coordination thread for runs | Small sample approved by Mark, settings printed | On the held-out set, recall on "unsupported" at least 0.95 at precision at least 0.85, published per failure class; compared with the current gates' decisions on the 308 saved drafts scored against gold labels; agreement with the specialist published. No gate retired |
| S1-05 | Contextual indexing of the twelve shelves | Contextual indexing of the union of the twelve shelves (338 files, about 154M tokens) | metered | Reach: whether passage retrieval finds what the records do not | About $150 once, at the vendor's rate of about a dollar per million tokens; lpc's shelf about 47M tokens | Waits for Mark's named cap [BLANK] and sample approval [BLANK]; proposal also ties it to the Library additions (stage 2 tooling) | Library thread | Sample on a small part of lpc's shelf, approved by Mark, settings printed, before the rest | Sample approved, then index built for the union, versioned by hash, outside the live and canonical trees; spend logged against the cap |
| S1-L1 to S1-L7 | The seven learning items | The proposal names "the seven learning items from the landscape" but does not list them | [NOT STATED IN THE PROPOSAL] | [to be supplied] | Not stated | Waits for the list of seven to be supplied from the landscape pages, one line each | Coordination thread to supply the list; Fable design thread to own | If any item is metered: sample and cap as above | Each item's own done-result to be written when its text is supplied |

The proposal also lists what stage 1 is meant to find out (section 13,
"Not known, and found out in stage 1"): whether any judge holds at the
specialist's bar; how many plain-text files segment by script; how often
real first questions recur; how much boundary leakage exists today;
whether an offer of passages raises prompt size beyond what the length
line saves. These are not assigned to ledger lines by the proposal; they
are recorded here for the coordination thread to map to the seven
learning items once the list is supplied.

Not in stage 1 (not authorized): gate retirement, rendering, bundles,
openings, any change to the production path.
