# Why the OVER_SETTLING check disagrees with itself

`tools/cost/why_unstable.py`, 2026-08-16, monitoring temperature pinned to 0.
Raw output in `2026-08-16_instability.txt`. Total spend ~$2.

The three-draw replay found the check does not reproduce its own verdict on
29–43% of turns — in the two-stage path that runs in production, not only in
the rejected fold. This is the cause.

## The answer

**The model, on byte-identical input.** Nothing upstream of it contributes.

Everything the pipeline can vary between draws was held fixed, one at a time:

| suspect | test | result |
|---|---|---|
| sampling temperature | inspect the request payload | `temperature: 0.0` present, so it is genuinely being sent |
| the model, short prompt | frozen 1k-token **screen** prompt × 8 | **8/8 byte-identical output** |
| the model, long prompt | frozen 12k-token **adjudication** prompt × 8 | **7/8 confirm, 1/8 clear** — flips |
| prompt caching | same bytes, no cache breakpoint × 8 | also flips (4/8) — not a cache artefact |
| retrieval | `_gather_world_evidence` × 8 | **one distinct source block** |
| stage 1 | 56 turns × 3 draws | screen fired identically on **every** turn |

Then at scale — 20 turns, each one's adjudication prompt frozen and replayed
six times:

```
FROZEN-INPUT REPLAY: 6/20 turns (30%) changed their verdict on IDENTICAL bytes
  per-candidate flip rate 7/62 = 11%
```

30% on frozen bytes against 21–43% measured on live traffic. **The pipeline
explains none of the instability.** A later run of the same experiment on
overlapping turns measured 47% turn-level and 15% per-candidate — so the
noise level itself moves between runs, and even the flip rate is not a stable
quantity.

## Why a long prompt and not a short one

Greedy decoding is deterministic given identical logits. A flip on identical
bytes means the top two tokens were near-tied at the position where the
verdict is written, and the tie was broken differently by ordinary numerical
variation in serving. So the check disagrees with itself **exactly where its
judgement is genuinely marginal** — which is what a 12k-token evidence-dense
prompt asking a fine distinction produces, and a 1k-token prompt sorting
plainly-different categories does not.

## The structural amplifier

A turn confirms if **any** candidate confirms. Per-candidate flip rate 11%
compounds across the 3–4 candidates the screen forwards:

```
a 2-candidate turn would flip ~21% of the time from that alone
a 3-candidate turn would flip ~30%
a 4-candidate turn would flip ~38%
```

**The check is structurally noisier than any single ruling it makes.** The
screen's instruction to forward everything worth a look — right on its own
terms, since it cannot rank blind — is also what multiplies the noise.

## The classifier that matters is stable

The obvious next worry: does the relational-safety classifier do this too? It
does not.

Sixteen held-out distress and attachment probes (the ones written to break
the rejected lexicon gate, so not in any prompt) plus three ordinary
questions, six draws each:

```
0/19 probes got more than one answer across 6 draws (0%)
0/19 probes flip between ACTING and STAYING SILENT
```

Every A1 probe read as `ACUTE_DISTRESS:A1`, the A2 as `A2`, every attachment
probe as `HARMFUL_DYNAMIC_SIGNAL` with a tag, every ordinary question
`NO_SIGNAL` — six times each, no variation. Its prompt is ~1.3k tokens and
its categories are far apart. One accuracy note, separate from stability:
*"I don't see a way forward from where I am"* came back
`AMBIGUOUS_LOW_CONFIDENCE` rather than `ACUTE_DISTRESS` on all six draws —
consistently, and still not silent, so sustained attention still engages.

**So this is not "LLM classifiers are unreliable".** It is specific to a long,
source-fed, fine-grained judgement.

## An attempted fix, measured and rejected

The production response format writes the verdict as the **first** token of
each line — `<n>. CLEARED - <because…>` — and then asks the model to apply an
affirmative test *"to yourself"*, silent reasoning the format gives it nowhere
to write. That puts the whole decision on one knife-edge token with no
reasoning to condition on. Moving the verdict to the end of the line, after
the evidence is named, is the cheapest conceivable fix: same call, same
price.

Fifteen turns, six draws, both formats back to back on identical frozen
prompts:

```
                  candidates  flipping  per-cand   turns  flipping
verdict-first             47         7       15%      15        7  (47%)
evidence-first            47        11       23%      15        3  (20%)

majority verdicts agree on 10/15 turns
```

It halves turn-level flipping — and it does it by **confirming far more**.
Eleven of fifteen turns confirm by majority under evidence-first against six
under the shipped format, and four of the five disagreements run
clears → confirms. Its turn-level stability is the OR saturating, not the
judgement steadying: its per-candidate flip rate is *higher*.

That is the failure the check's own asymmetry rule exists to prevent —
*"a false OVER_SETTLED … pushes a representative to hedge a claim its own
world actually held with conviction"*. **Rejected.** Not shipped, and the
prompt is untouched.

## What is actually available

| option | cost | what it buys |
|---|---:|---|
| accept and document | $0 | stop reading single-draw rates as measurements |
| re-draw only on confirm, require 2 of 2 | ~$190/yr | halves flip-driven false confirms; recovers no misses |
| best-of-3 on every adjudication | ~$1,376/yr | more than every other line in the cost review combined |
| forward fewer candidates | free | less compounding, more misses — the retune the project's own rule forbids on a guess |

The recommendation is the first. OVER_SETTLING produces invisible correction
guidance to the representative, not a block on the participant, and the
classifier that *is* load-bearing has now been measured stable. What has to
change is not the mechanism but the confidence placed in any single-draw
number taken from it — including the 82% fire rate and 28% confirm rate this
review's own cost case rests on.
