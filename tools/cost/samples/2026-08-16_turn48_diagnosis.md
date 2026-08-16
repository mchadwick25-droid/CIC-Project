# Turn 48: why the fold loses the one finding it stably loses

`diagnose_over_settling.py --only 48 --reps 3`, 2026-08-16, monitoring
temperature pinned to 0. Raw model output in
`2026-08-16_turn48_diagnosis.txt`. Cost $0.03.

Turn 48 (post-apostolic-house-church) is the single **stable regression** in
the temp-0 three-draw comparison: the two-stage pair confirmed a finding on
every draw, the fold on none. It also failed in the very first single-draw
run. Everything else that separated the two paths turned out to be variance;
this did not.

## What the harness could not tell us, and this does

`compare_over_settling.py` reports verdicts. A verdict cannot say *why*, and
the two possible causes need opposite fixes:

- Phase 1 never **enumerated** the claim -> the enumeration instruction is
  wrong.
- Phase 1 enumerated it and Phase 2 **cleared** it -> the ruling is wrong,
  or it ruled against different material.

## Result: Phase 1 is fine. Phase 2 clears it, the same way, every draw.

Both paths list the same four claims. The fold quotes the disputed sentence
verbatim as its own candidate 4:

> "The first meal shared as one of us — that is when a person is truly
> inside the house, not merely washed clean of what came before."

So nothing is lost at enumeration. The loss is entirely in the ruling, and
the fold's clearing rationale repeats across all three draws:

> "The representative speaks from inside a household where this is the lived
> order and does not claim it as universal across all communities."

> "...spoken from lived experience rather than as a doctrinal pronouncement"

> "...without claiming this is how all communities ordered the relationship
> between baptism and the table."

The pair, on the same material, confirms all three draws:

> "The material distinguishes the water as the entry point ... and the table
> as what forms ongoing belonging ..., but does not settle that the meal
> marks true incorporation while the water does not."

## The mechanism, and why it is not a wording bug

Look at what each path writes in the *Concern* line of its own candidate 4.

Blind screen (identical all three draws):

> "The claim that the shared meal, not the water itself, marks true
> incorporation ... is presented as **settled doctrine**, but the
> theological and practical weight given to the meal versus the washing
> **varied across traditions**."

Fold, Phase 1 (all three draws, same shape):

> "Whether the claim ... is **universal across households**, or whether this
> represents one community's understanding."

The fold frames its own concern as a question about universality — and a
universality concern has a stock answer that always works: this
representative speaks for one household and never claimed otherwise.
Phase 2 then answers the question Phase 1 asked, and clears.

The blind screen cannot frame the concern that way, because it has not read
the material. Not knowing what the record holds, all it can name is that the
claim is stated more firmly than a contested thing should be — which is the
question the adjudicator then has to rule on against the sources.

That is the finding: **the screen's value here is not filtering, it is
blindness**, and blindness is not a thing a prompt can restore inside a
single call. `OVER_SETTLING_FOLDED_PROMPT` says "you must finish the first
phase before beginning the second", but one forward pass reads the whole
prompt, sources included, before it writes a word. The phases are named, not
separated.

## Two things this rules out

**Retrieval is not the cause.** All six source-fed calls — both paths, three
draws — retrieved **37 of 37 identical chunks**, pairwise Jaccard 1.00. The
`_gather_world_evidence` instability that was the leading suspect after the
three-draw run does not appear here at all. Both paths ruled on identical
material and disagreed.

**The screen is now deterministic; the source-fed calls are not.** With
temperature pinned to 0 the screen returned byte-identical output on all
three draws. The adjudicator and the fold each produced three textually
different outputs, though the adjudicator's *verdict pattern* was stable
(CLEARED, CLEARED, CLEARED, OVER_SETTLED, three times). Temperature 0 does
not buy determinism on a 12k-token prompt; it did buy it on the 1k-token
screen.

## One correction, from six further draws

Later frozen-input replays (`why_unstable.py --sweep`) put the pair at **5/6**
on this turn, not 6/6. So "the pair confirms on every draw" describes two
three-draw samples, not the check: read it as *the pair confirms on 8 of its 9
draws and the fold on none of its 6*. The mechanism above is unaffected — it
was read directly off the model's own words, three times — but the word
"stable" was doing more work than the sample supports.

## Is the pair right?

Mostly. The response asserts an ordering — the meal, not the water,
completes joining — where the record affirmatively holds a different
distinction (water marks entry, the table forms ongoing belonging). That is
an inference spoken as documentation, which is exactly what this check is
for. It is not an egregious finding, and the adjudicator's own wording
leans on "does not settle", which is the phrasing its affirmative test warns
against. A marginal true positive, then — but a true positive, and the fold
loses it every time.
