# Model assignment — 2026-09-24

Thread E, tech-readiness program. PR #480.

Mark's question: *"i still want to analyse what are the right llm for each task, but also take advantage of the more robust opus 5.5 and its writing skills"*.

These are recommendations only. Every decision is Mark's.

Two budgets are kept separate throughout:

- **Thread work** is paid from Claude Code session credits (the Max-200 pool).
- **Engine runtime** is Bedrock spend on each participant conversation.

## What was measured, and what could not be

| Study | Status | Bedrock spend |
|---|---|---|
| 1. Rendering grader: Haiku 4.5 vs a stronger model, on the R43 labeled set | **Done**, with Sonnet 4.6 standing in for Sonnet 5 | $1.77 |
| 2. Voice: Sonnet 4.5 vs Opus 5.5 | **Blocked. Nothing ran.** | $0 |
| Model availability probe | Done | about $0.01 |

**The blocker.** Opus 5.5 and Sonnet 5 are both listed as Bedrock inference profiles in us-east-1 and us-west-2. But every call to them returns this error:

> `Error code: 403 - anthropic.claude-opus-5-5 is not available for this account` (the same error for `claude-sonnet-5`)

This was recorded on 2026-09-24. The reviewer thread reports that Mark saw the same error in the Bedrock console at about 15:30Z. Models now switch on at first use, so this is a gate on the AWS account itself, not a permissions setting in this repo. Opus 5, Opus 4.8, Opus 4.7 and Fable 5 are gated the same way.

What this account can call today: Haiku 4.5, Sonnet 4.5, Sonnet 4.6, Opus 4.5 and Opus 4.6. The evidence is in `engine/provider/reports/model-availability-2026-09-24.json`. No provider or key was added.

**Sonnet 5 is still the target grader.** Every Sonnet 4.6 number below is a stand-in until AWS opens Sonnet 5 on this account. Study 1 can then re-run as-is with `--models haiku,sonnet5` once a `sonnet5` entry is added back.

## Study 1 — rendering grader

### Method

The labeled set is `R43-Labeled-Set.csv` in this folder, 69 rows. It was rebuilt from the R43 list on #465, the bodies of #466 to #475, and Decision-Log entries 19 to 28.

| Label | Rows | Graded text | What the human decided |
|---|---|---|---|
| Defect fixed on the grader's finding | 52 | the version before the PR | defective |
| Grader stricter than the text, kept as-is | 5 | the version before the PR | fine |
| Defect the grader missed, caught on the human read | 12 | the **round-one** version the human rejected | defective |

The misses are graded at round one for a reason. Each of those defects entered in the round-one rewrite, so the text before the PR never contained it.

Each version was graded **3 times per model** through `engine.m1.rendering_fidelity.grade_rendering`. The system prompt, tool schema and provider path were unchanged. Timeout was 60 s, so latency could be measured without calls being cut off.

The harness is `engine/m1/reports/rendering_grader_model_study.py`. Raw results are in `engine/m1/reports/rendering-grader-model-study-2026-09-24.json`.

**Bias warning.** The 52 fixed defects were chosen *because Haiku flagged them*. That inflates Haiku's catch rate on them. The 12 misses were never chosen by any grader, so they are the fair test of what a grader finds. The 5 kept records are the only "fine" examples. That is too few to give a reliable false-positive rate.

### Results

"Flagged" means any verdict other than `translation`. "Majority" means at least 2 of the 3 runs.

| | Haiku 4.5 | Sonnet 4.6 (stand-in) |
|---|---|---|
| 52 fixed defects, flagged by majority | 45 | 34 |
| 12 human-caught misses, flagged by majority | 3 | 6 |
| 12 misses, flagged **and naming the defect the human found** | 1 | 3 |
| 5 kept records, wrongly flagged by majority | 1 | 2 |
| Same flag on all 3 runs (69 records) | 48 (70%) | 64 (93%) |
| Same verdict on all 3 runs | 32 (46%) | 58 (84%) |
| Latency p50 / p95 / max | 2.2 / 3.4 / 5.3 s | 3.2 / 5.2 / 8.2 s |
| Calls over the grader's production 8 s timeout | 0 of 207 | 2 of 207 |
| Cost per call (about 1.2k in / 180 out tokens) | $0.0022 | $0.0064 |

On the 52 fixed defects:
- Both graders flagged 33.
- Haiku alone flagged 12.
- Sonnet 4.6 alone flagged 1.
- **Neither flagged 6** by majority. Haiku flagged all 6 in the R43 sweep, but does not flag them today.

Haiku's instability shows most clearly on the kept records. Haiku flagged all 5 in R43 (that is how they entered the set), yet 4 of them now read `translation` on all 3 runs.

The current birth-condition rule asks for "translation on two consecutive runs". With Haiku, whether a record passes that rule depends heavily on which run you get.

### The 12 misses, read one by one

The verdict alone overstates what either grader found. Each grader's reasoning was read against what the human caught.

| Kind of defect | Records | Haiku 4.5 | Sonnet 4.6 |
|---|---|---|---|
| **Fragment** (verbless or subjectless sentence) | cappadocian basil-canon-to-amphilochius, basil-on-the-doxology-challenge; pahc melito-no-phantom; hal dispute-to-learn | none caught. It flags melito and dispute-to-learn, but for a different clause both times | none caught. It flags basil-canon and dispute-to-learn, but for small word additions |
| **Archaic register** | rzg signs-and-things-signified; hal ever-let-the-bridegroom; pahc ignatius-truly-born, polycrates-to-victor | none caught | none caught. It flags ignatius, but for a different clause |
| **Meaning drift** (paraphrase, small add or drop) | cappadocian what-is-the-written-source; syr warned-before-baptism, tatian-barbaric-writings; alx the-grades-here-in-the-church | 1: alx, the dropped "in the Church" qualifier | 3: what-is-the-written-source (names the paraphrase), warned-before-baptism (names the closing clause), alx |

**Neither grader would have caught the fragments, and neither catches register.** This is not a model weakness. The grader's prompt asks only whether every clause carries over. It never asks about grammar or register, so no model will flag them.

Thread C's report-only sentence-completeness check is the right tool for fragments. Register still depends on the human read.

### Recommendation: grading

1. **At authoring time, run both graders and treat a flag from either as a flag.** Then keep the human read.
   - Both together caught 46 of the 52 fixed defects and every meaning-drift catch either grader made.
   - They cost about $0.009 per record per run, under 2 cents for the two-run rule.
   - The price of this is more false flags: 2 of the 5 kept records get flagged. The human read already sorts those out.
2. **When Sonnet 5 is enabled, re-run this study before swapping it in.** Its rate-card price ($2/$10) is below Sonnet 4.6's ($3/$15), but its quality is unmeasured here.
3. **If a stronger model becomes the only grader, raise the 8 s timeout.** Sonnet 4.6 went over it on 2 of 207 calls.
4. **Leave fragments and register out of this grader.** Handle them with thread C's deterministic check and the human read. Adding them to the grader prompt would be a methodology change, which is Mark's call.

## Study 2 — voice (held)

**Status: blocked on 2026-09-24.** Opus 5.5 returns 403 on this account, as described above. No voice turn ran and no voice spend occurred. The plan below is kept so it can run unchanged once AWS opens the model. It still needs the reviewer's go before any turn.

- **Worlds:** pahc (70–200, early), rzg (1519–1650, Reformation), cappadocian (the most R43 changes: 12).
- **Battery:** 7 single-turn prompts per world, each in a fresh session, on both voice models. That is 42 turns, plus 3 turns with Opus 5.5 as a straight swap into the current call.
- **Grading:** the reader and gate stay on Haiku. The rendering grader runs on every quote the voice uses. Then a human-style read of each model's best and worst 3 turns against:
  - R34: translation, not summation;
  - R26 and R37: knows only what it would have known;
  - whole-sentence modern register.
- **Engine change needed first:** Opus 5.5 cannot turn thinking off. The voice call's `max_tokens=1024` limit would then cover both thinking and answer, which risks blank or cut-off answers. A fair test needs an optional effort / max_tokens passthrough on `run_turn`. It must be additive, keep defaults unchanged, and have a test pinning the default path byte-identical. This goes in this PR, after thread A's merge.
- **Spend estimate:**
  - Sonnet 4.5: $1–2.
  - Opus 5.5 at low effort: $2.50–5. It costs $4/$20 per MTok and may use 1.0–1.35× the tokens for the same text.
  - Straight-swap turns: about $0.75.
  - Total ceiling: **$12**.

## Recommended assignments

### Engine runtime (Bedrock, per participant conversation)

| Task | Today | Recommended | Evidence | Cost |
|---|---|---|---|---|
| Voice | Sonnet 4.5 | **Keep Sonnet 4.5.** Re-decide after Study 2. | None new: Study 2 is blocked. | $0.017–0.070 per turn including gate and reader (engine/m8 live cost report, alx/ijc) |
| Reader | Haiku 4.5 | **Keep Haiku 4.5.** | Not measured here. | Part of the per-turn figure above |
| Facilitator gate / safety calls | Haiku 4.5 | **Keep. No change without its own safety battery.** | Not measured here. The safety path is the last place to swap a model on indirect evidence. | Part of the per-turn figure above |
| Rendering grader (authoring time, not per conversation) | Haiku 4.5, one model | **Haiku 4.5 plus Sonnet 4.6, a flag from either counts; Sonnet 5 once enabled and re-measured** | Study 1 above | about $0.009 per record per run |

### Thread work (Claude Code session credits)

No thread-side measurement was run in this PR. The rows below are recommendations with the evidence available. Relative token prices come from the rate card, per MTok in/out: Haiku 4.5 $1/$5, Sonnet 5 $2/$10, Opus 5.5 $4/$20, Fable 5.1 $10/$50.

| Task | Recommended | Evidence | Relative cost |
|---|---|---|---|
| Authoring worlds and `modern_rendering` text | **Opus 5.5 — a proposed change, Mark's call.** CLAUDE.md today says to draft with Sonnet and keep Opus for the final review gate. | Round one's 12 misses were writing defects (fragments, register, paraphrase), exactly what a stronger writer should cut. Not yet measured. The cheap test is below. | 2× Sonnet 5 per token. Worth it only if it saves a review round, and one round costs more than the difference. |
| Engine logic | Sonnet 5; Opus 5.5 for design-heavy or cross-module changes | Existing practice; today's loader change needed a test to catch a key-order regression, which is routine work | 1× / 2× |
| Mechanical ops (package rebuilds, citation and log fixes, indexing) | Haiku 4.5 | The CLAUDE.md rule stands; nothing here argues against it | lowest |
| Batteries (running) | Sonnet 5 in the thread. The model under test is whatever the battery names. | Running them is scripting and bookkeeping | 1× |
| Grading and the adversarial review gate | Opus 5.5 | The CLAUDE.md rule stands. Study 1 shows the stronger model is far more consistent (93% vs 70% same flag). | 2× |
| Framing research (Doc_02, Doc_04, redesigns) | Fable 5.1 | The CLAUDE.md rule stands | 5× Sonnet 5 |

**A cheap way to answer Mark's writing question without waiting on AWS.** In Claude Code, re-author the 12 round-one-rejected renderings twice, once with Sonnet 5 and once with Opus 5.5. Give both the same brief and sources. Then grade them blind with the human read against R34 and whole-sentence register, plus thread C's fragment check.

This runs on session credits, not Bedrock. It measures exactly the writing skill in question, on records where we already know what went wrong. The result would settle the authoring row above with evidence.

## Open items

- AWS account access for Opus 5.5 and Sonnet 5: Mark with AWS. Study 2 and the Sonnet 5 re-run of Study 1 both wait on this.
- Authoring-model change: needs Mark's ruling, because it changes a CLAUDE.md usage rule. The proposed 12-record re-authoring test would give the evidence first.
- Grader scope (grammar and register): stays out of the grader unless Mark rules otherwise. Thread C's check covers fragments.

## Addendum — authoring test results (2026-09-24)

This reports the results only. The choice of authoring model, and any change to the CLAUDE.md usage rule, is Mark's.

**What ran.**
- Two fresh subagents re-wrote the 12 renderings that the round-two human read had rejected.
- Both got the same brief (`Authoring-Brief-12-Records.md`). It held each record's verbatim `text`, with no prior rendering, no grader verdict and no hint of what went wrong.
- They reported their own model ids as `claude-sonnet-5` and `claude-opus-5-5`.
- The 24 renderings were blinded as A and B per record, and read against the bar: every clause present, nothing added, modern English, whole sentences of one thought each, nothing past about 25 words, and no word whose modern sense misleads.
- The key was sealed by SHA-256 before the read and opened after it.
- Full verdicts and the unsealed table: `Authoring-Test-Blind-Read.md`.

| | Opus 5.5 | Sonnet 5 |
|---|---|---|
| Passed the blind read | 12 of 12 | 3 of 12 |
| Preferred, of 10 records that were not ties | 9 | 1 |
| Flagged by either grader (Haiku 4.5, Sonnet 4.6), by majority | 3 | 1 |
| Sentence-completeness flags | 0 | 1 (a misparse) |

- Sonnet 5 failed mainly on sentence length: 8 renderings kept sentences of about 45 to 90 words.
- Its other failures were three word choices whose modern sense misleads or loses something: "sick of love", "too godly", and "these words" for "syllables".
- The graders pointed the other way from the human read. They are not asked about sentence length.
- The reader raised three rule questions for Mark:
  - whether an editor's bracketed supplement may be voiced (both authors did);
  - a small restructuring by Opus 5.5 in the Polycrates record;
  - dropping a leading "Since" where the excerpt has no main clause (both authors did).
- **Limits of the test:**
  - It is 12 records, one run per author.
  - Each author's style is consistent, so the reader could have grouped renderings by author, though not named the model.
  - The authoring ran on session credits.
  - $0.63 of Bedrock spend graded the 24 renderings, under the earlier brief.
