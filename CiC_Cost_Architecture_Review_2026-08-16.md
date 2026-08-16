# CiC Cost & Architecture Review — 16 August 2026

Independent pass over `cic/records`, `cic/engine`, `cic/runtime/app`.
Single-voice mode. Published view: https://claude.ai/code/artifact/b56d902b-fe88-4705-acbe-d53a5ad091b0

> **Revised 2026-08-16 (second revision) after running 48 turns of real
> traffic through the app.** Everything below that was estimated is now
> measured; see [Measured on real traffic](#measured-on-real-traffic-48-turns-2026-08-16).
> Every projection in this document was too pessimistic, again.
>
> **Revised 2026-08-16 after running the cache verification test.** The first
> version of this document suspected a runtime cache failure. That was wrong —
> the cache works. The root cause is the cost calculator, which was listed
> there as the "most likely benign explanation" and is now confirmed.

## Short version

1. **The prompt cache works.** A live two-turn test returned a clean
   17,565-token `cache_read` on the second call, on both the streaming and
   non-streaming paths, at the 1h TTL.
2. **The cost calculator double-charges cached tokens.** LangChain reports
   `input_tokens` as the *total* input with `cache_read` as a subset;
   the raw Anthropic block reports them as additive. Summing all three
   overstates `main_response` by **2.6x**.
3. **True cost today is $0.372/hour — measured, not modelled.** Not $1.09,
   and not the $0.53 this document estimated before the traffic sample ran.
4. **$0.30/hour is reachable, but only by removing both the relational-safety
   classifier and drift detection.** Every cheap lever together lands at
   $0.349; the last 16% has to come out of the apparatus. That is the
   conscious quality trade-off, stated plainly, with the arithmetic below.
5. **Sonnet 5 pricing is stable at $2/$10.** Verified against the live model
   docs 2026-08-16: flat pricing, no introductory expiry. An earlier draft of
   this review warned of a 2026-08-31 cliff, drawn from a stale cached table;
   **withdrawn**. There is no deadline on the voice-model decision.
6. **Safety mechanisms are ~10% of spend, not 3.2%** — corrected by
   measurement. The dollar figure held ($0.037/hour, estimated $0.035); the
   *share* tripled because the denominator fell. At $0.372/hour they are no
   longer a rounding error, and $0.30 cannot be reached without them.

## Measured on real traffic (48 turns, 2026-08-16)

4 sessions x 12 newcomer questions, 2 worlds x 2 consecutive sessions. 48/48
turns returned 200. Raw log and analyzer output: `tools/cost/samples/`.
Spend: ~$1.49.

**$0.03103/turn — $0.372/hour at 12 turns/hour.** Every estimate in this
document was high. The double-count factor measured **2.39x**, confirming
finding 2 on live data rather than a replica.

| | $/turn | share | $/hour |
|---|---:|---:|---:|
| `main_response` | 0.01360 | 43.8% | 0.163 |
| `over_settling_adjudication` | 0.00478 | 15.4% | 0.057 |
| `relational_safety` | 0.00238 | 7.7% | 0.029 |
| `drift_detection` | 0.00224 | 7.2% | 0.027 |
| `over_settling_screen` | 0.00204 | 6.6% | 0.024 |
| *12 smaller labels* | 0.00599 | 19.3% | 0.072 |
| **TOTAL** | **0.03103** | | **0.372** |

`main_response` is 44% of spend and is the floor: **$0.163/hour before any
apparatus runs at all.** A $0.30 budget leaves $0.137/hour for everything
else; everything else currently costs $0.209.

### The route to $0.30, priced on measurements

| cut | $/turn saved | $/hour | $/yr @1000h | running $/hour |
|---|---:|---:|---:|---:|
| — | | | | 0.372 |
| fold the screen into the adjudicator | 0.00098 | 0.012 | 141 | 0.361 |
| drop groundedness shadow checks | 0.00099 | 0.012 | 143 | 0.349 |
| drop `drift_detection` | 0.00224 | 0.027 | 323 | 0.322 |
| drop `relational_safety` | 0.00238 | 0.029 | 343 | **0.293** |

The first two are free — one is a design simplification that also removes a
class of miss, the other is a shadow check with a graduation date already on
it. They get to **$0.349**. The last two are the apparatus itself. **There is
no arrangement of cheap levers that reaches $0.30.** Taking the last 16%
means deciding that drift detection and the relational-safety classifier are
not worth $0.056/hour between them — which is the trade-off to make
consciously, not a saving to find.

### Two things the sample settles that the model could not

**Cache pooling is structural, not lucky — 16.0x.** Sessions 3 and 5 (the
second on each world) wrote **zero** cache tokens; they read entirely off the
first session's prefix. But sessions 1 and 4, running cold, still pooled
**11x on their own** — the prefix is written once and read by all 12 turns.
Priced honestly: if no session ever pooled with another, cost rises to
**$0.409/hour**, +10%. Pooling is not a concurrency bet.

**Turns per hour is the biggest single uncertainty in this document.** The
$/turn is measured; the 12-turns-per-hour divisor is assumed.

| turns/hour | $/hour |
|---:|---:|
| 8 | 0.248 |
| 10 | 0.310 |
| **12** | **0.372** |
| 15 | 0.465 |
| 20 | 0.621 |

At 20 turns/hour, the full apparatus-cutting programme above still lands at
$0.489. **A faster conversational pace moves the cost more than every lever
in this review combined.**

### What 12 turns/hour actually assumes

`tools/cost/analyze_pacing.py` decomposes a turn from the session event logs,
which already timestamp every event. Measured on the 48-turn sample:

| component | median | how known |
|---|---:|---|
| wait for the answer | 11s | measured |
| post-response classifiers | 9s | measured — overlaps reading, not additive |
| reading the reply | ~51s | estimated: 188 words at 220 wpm |
| **thinking and typing** | **?** | **cannot be derived from a scripted log** |

A turn is `11s + max(reading, 9s) + compose`. Which means:

> **12 turns/hour implies a 300-second turn, and therefore ~238 seconds — four
> minutes — of thinking and typing per question, on every question, for twelve
> questions straight.**

That is the assumption under every $/hour figure in this document. It is a
claim about people, and it has never been checked against any. It is also
robust to the one estimate inside it: at 150 wpm it implies 3.6 minutes, at
260 wpm 4.1 minutes. Reading speed is not what is uncertain here.

| compose time | turn | turns/hour | $/hour | $/yr @1,000h |
|---:|---:|---:|---:|---:|
| 0s | 62s | 57.7 | 1.792 | 21,503 |
| 30s | 92s | 39.0 | 1.210 | 14,517 |
| 60s | 122s | 29.4 | 0.913 | 10,957 |
| 120s | 182s | 19.7 | 0.613 | 7,352 |
| **238s** | **300s** | **11.9** | **0.369** | **4,434** |

The machine floor is 181 turns/hour — nobody can go faster than the system
answers — so the ceiling is not the constraint. The constraint is entirely
human, and entirely unmeasured.

### The unit itself is worth questioning

**$/turn is what the architecture controls. $/hour is $/turn multiplied by how
fast people talk.** A system that looks cheaper per hour may simply be a slower
one, and pace is not waste — a participant who asks thirty questions in an hour
got more conversation than one who asked twelve, and paid for it.

If the budget is really *N conversations*, a twelve-turn conversation costs
**$0.37 at any pace** and this whole uncertainty disappears. If it is really
*hours of access given away*, then pace is the dominant term and no amount of
apparatus-cutting substitutes for knowing it. That is a question about what is
being promised to participants, not a question about the code.

### What unblocks it

Nothing needs building. `app/graph/events.py` already persists every event
with an ISO timestamp to `transcripts/events/<session_id>.jsonl`, in
production as in test. The moment real participants use the app, run:

```
python3 tools/cost/analyze_pacing.py 'cic/runtime/transcripts/events/*.jsonl'
```

It detects a scripted log and refuses to report it as pacing; on real sessions
it prints turns/hour with an interquartile range and the $/hour that follows.
**A single pilot session of a dozen real turns settles it** — this needs one
person, not a sample.

## Verification test (live, ~12 cents)

Replicating `get_llm(max_tokens=1200)` and `_cached_system_message` verbatim
against the real Syriac static prompt; `tools/cost/verify_prompt_cache.py`.

| Call | Path | LangChain `input_tokens` | Raw API `input_tokens` | cache_creation | cache_read |
|---|---|---:|---:|---:|---:|
| A1 | stream, 1h | 17,680 | (not populated) | 17,565 | 0 |
| A2 | stream, 1h | 17,680 | (not populated) | 0 | **17,565** |
| A3 | invoke, 1h | 17,680 | **115** | 0 | **17,565** |

A3 is the decisive row. The raw Anthropic block reports `input_tokens: 115` —
the genuinely uncached remainder. LangChain reports 17,680 for the same call,
because its `input_tokens` is the total with `cache_read` nested inside
`input_token_details`. Streaming never populates the raw block at all, so the
production path only ever exposes LangChain's total.

On A2 a calculator summing the three reports $0.0418; true cost $0.0067
(6.3x, inflated because the test's dynamic block was deliberately small).
On a realistic production turn the overstatement settles at **2.6x**.

## Measured token shape (exact static counts via free `count_tokens`)

| World | Static (cached) | Retrieved (uncached) | Total in | Cacheable |
|---|---:|---:|---:|---:|
| imperial_juridical / Marius | 15,781 | 3,720 | 19,801 | 80% |
| hieronymian / Albina | 16,632 | 3,190 | 20,122 | 83% |
| desert / Papnoute | 16,796 | 2,830 | 19,926 | 84% |
| syriac / Yausep | 17,567 | 5,380 | 23,247 | 76% |
| pahc / Chloe | 17,699 | 5,890 | 23,889 | 74% |
| alexandria / Theon | 22,546 | 7,310 | 30,156 | 75% |
| **fleet mean** | **17,837** | **4,343** | **22,480** | **79%** |

The 22,480 mean independently reproduces the 21,000–23,000 figure observed in
the live round — confirming it is the total, not an uncached remainder.

Model cross-check: `over_settling_adjudication` re-sends permanent prompt +
capsule + a second full retrieval to Haiku (~15,000 tok at $1/MTok) on 78% of
turns => ~$0.0117/turn. The prior session measured 12.7% of $0.091 = $0.0116.
The token model is sound; the caching line is what refuses to reconcile.

## Route to $0.30 (12 turns/hour, output measured at ~330 tok)

| Step | Configuration | $/turn | $/hour |
|---|---|---:|---:|
| R0 | As reported (double-counted) | 0.0910 | 1.09 |
| T0 | **True today**, no changes | 0.0442 | 0.53 |
| T1 | + classifier surgery | 0.0351 | 0.42 |
| T2 | + pilot scale (20 sessions/world) | 0.0295 | 0.35 |
| T3 | + retrieval halved — **Sonnet meets target** | 0.0251 | **0.30** |
| T4 | T1 + Haiku 4.5 voice | 0.0241 | **0.29** |
| T5 | T4 + pilot scale | 0.0212 | **0.25** |

On true numbers the classifier stack is ~$0.022/turn — about half the real
bill, a larger share than the original figures implied. The saving is
concentrated in one line (`over_settling_adjudication`), not spread thin.

Self-correction: the first version dismissed retrieval trimming as worth only
$0.05/hour. That is still the number, but against a corrected $0.53 baseline
where the static block bills at a tenth, retrieval is one of the few
components still paying full freight — and $0.05/hour is exactly the margin
between T2 and T3. The lever was mis-sized, not irrelevant.

## Findings, ranked by money

1. **Cost calculator double-counts cached tokens** (no real spend; makes
   every cost decision wrong by ~2x). Confirmed by live test. `log_llm_usage`
   is correct as logging; the error is downstream, in treating LangChain's
   `input_tokens` as uncached-only. Because streaming never populates the raw
   Anthropic block, there is no signal that anything is off.
2. **Generation model** (~$0.13/hour). Now purely discretionary — not needed
   to reach target and not forced by pricing. Already tried
   and reverted 2026-08-10 — on a Haiku-only *table*-mode transcript
   isolation breach (up to 21% of table turns), not on cost and not on solo
   quality. Single-voice mode builds no public transcript. Chloe's Haiku
   re-certification held every hard bar; the one real regression was
   citations 7/8 -> 3/8.
3. **Classifier stack is 13–15 Haiku calls/turn, not ~10** (~$0.14/hour
   recoverable). Concentrated in `over_settling_adjudication`, which fires on
   78% of turns and confirms on 20%.
5. **Cost/hour falls with concurrency** (~$0.04/hour). The 1h cache entry is
   keyed on prefix, not session, so it is shared across all sessions on a
   world within the window.

## Classifier architecture — necessary at current scope?

Mostly yes. Cut: the two shadow-mode groundedness checks (added 2026-08-15,
gate nothing) once Phase 0 has its sample; tighten the over-settling screen;
re-examine whether the retrieval negative-condition guard vote earns four
Haiku calls per turn on a 10–50 entry corpus. Do **not** cut the pre-turn
intercept chain, drift detection, or citation grounding on cost grounds —
they are cheap and load-bearing for the project's central claim.

## Safety disagreement

Facts, now measured (48 turns, 2026-08-16): `relational_safety` $0.00238/turn
and `frame_breaker` $0.00066/turn — **$0.037/hour, 9.8% of spend**.

The estimate above this line said $0.035/hour and 3.2%, and both halves are
instructive. The dollar figure was right within 6%. The *share* was wrong by
3x, because it was taken against an inflated total. **This strengthens Mark's
argument, not mine.** At $1.09/hour safety was a rounding error and "the cost
argument does not survive contact with the numbers" was fair. At $0.372/hour
it is a tenth of spend, it is the single largest cuttable line after the
adjudicator, and — see the route to $0.30 above — the target is unreachable
while it stays. The cost argument survives now. It just arrives as a
trade-off rather than a saving: $0.037/hour buys the protection, and whether
that is worth 12% of the budget is Mark's call to make with the real number
in front of him.

Substance: declining outright was the wrong move — it is Mark's product and
his duty of care to define. But keyword-triggered distress detection is
empirically weaker here, because people in distress about death and faith
rarely produce trigger keywords ("I don't see the point in going on").

**Uncosted middle path:** the mechanism has two halves.
`classify_relational_safety` is one Haiku call (~$0.0007/turn).
`stream_relational_safety_response` generates freely on Sonnet at full cost.
Keep the classifier; replace the generated response with fixed written text
approved once by Mark and a clinician. Better detection than keywords, no
model improvising in the highest-stakes moment, most of the cost gone.

## Trim ledger at 1,000 conversation-hours/month (12,000 turns)

Cumulative. Baseline = true isolated-session cost, $0.53/hr = $6,369/yr.

| Lever | Quality | $/hr | $/mo | $/yr |
|---|---|---:|---:|---:|
| A · strip builder apparatus from retrieved chunks **(SHIPPED)** | **improves** | 0.031 | 31 | 367 |
| B · gate safety classifiers **(NOT SAFE — see below)** | unsafe | — | — | **~0 available** |
| C · over-settling adjudicator 78% -> 30% **(BLOCKED)** | trades recall | 0.022 | 22 | 261 |
| D · shadow-mode checks — off-switch shipped, **not retired** | neutral | 0.003–0.011 | 3–11 | **39–132** |
| E · trim `_HOW_YOU_ENGAGE` **(DO NOT DO)** | risks the voice | 0.001 | 1 | **90** |
| F · pool cache writes (20 sessions/window) | none | 0.057 | 57 | 682 |
| **Sonnet 5, all of A-F** | — | **0.326** | **326** | **3,907** |
| Haiku 4.5, all of A-F | costs citations | 0.251 | 251 | 3,015 |

**A-F is worth ~$2,330/yr and requires no voice change.** (A came in at $367
rather than the estimated $496 - stories already stripped two of the sections
at index time, which the first estimate double-counted.) Haiku on top saves a
further $892/yr, permanently — the whole price of the Sonnet voice, against a
measured citation regression of 7/8 -> 3/8. **Recommendation: keep Sonnet.**
Grounded citation is the project's central claim and $892/yr is not the right
price for halving it when the target is already met without it.
One penny per hour = $120/year at this volume.

### A · Most of what retrieval sends is builder apparatus — SHIPPED 2026-08-16

Measured across every deployed chunk, as the model receives it after the
existing Key Sources / Quick Meaning excisions:

Story chunks — Story Text 29.5% | Tier Justification 25.0% | Usage Guidance
22.6% | Formation Ecology Connection 16.5% | Source Identification 5.2%

Lexicon chunks — World Meaning 52.5% | Distortion Risk 23.1% | Ecological
Function 15.8%

**Measured after implementation: the retrieved payload falls 34.1%**, 3,291 ->
2,168 tokens/turn, plus ~150 tokens from the retired FLAG-018 instruction =
1,273 uncached tokens/turn, $367/yr at 1,000 hours/month.

**`Distortion Risk` is the section that caused FLAG-018** — the voice read it as a task and opened turns with
unprompted term clarifications; the compensating instruction still ships in
the dynamic prompt on every turn. Strip the apparatus at build time and the
defect source, the compensating instruction, and a third of the uncached
payload all go together. Removed on **coherence** grounds before cost: the
section reads "A modern reader hears X...", handing the voice explicit
knowledge of how a modern participant thinks, which is exactly what the
permanent prompt's Total Embeddedness rule forbids.

Kept, though they read like apparatus by name: **Usage Guidance** and **Absent
Story Note** both carry anti-fabrication constraints the voice needs ("should
receive honest brevity, not an invented timetable"); **Plural-Voices Note**
carries attribution honesty. Tier/confidence remain in front-matter metadata.

#### Two defects found while implementing

1. **`find_section` under-reported fenced sections containing bold
   sub-labels.** `"\n\n**"` is a section-end marker, so `## Distortion Risk`
   ended at its own `**Modern Hearing:**` — reported extent 2.3% of the
   lexicon pool against a true 23%. Excising it would have removed the
   heading and left the body in place. Fenced sections now end only at
   `"\n---"` or `"\n## "`. Verified byte-identical on the existing Quick
   Meaning + Key Sources path across all 118 lexicon chunks.

2. **Eight chunks have no `World Meaning` section, or an empty one** —
   `pahclex012`, `pahclex013`, `syrlex005`, `syrlex008`, `desertlex013`,
   `desertlex017`, `desertlex018`, `ijclex011`. Their entire substance sits
   inside the apparatus, so stripping it shipped a zero-character body: the
   same Article 5 grounding failure `sections.py` was written to prevent.
   `excise_sections` now refuses any excision that would drop a body below
   `MIN_VOICE_BODY_CHARS`. **This is a records defect the guard contains but
   does not fix** — `desertlex018` has literally empty `**World Meaning:**`
   and `**Ecological Function:**` fields. Worth an authoring pass
   independent of cost.

### E · Measured, audited, and rejected — no change made

Two findings, both against my own estimate.

**1. It is worth $90/yr at pilot scale, not $221 — and it double-counts with F.**
`_HOW_YOU_ENGAGE` sits in the *cached* prefix, so most of the saving from
trimming it is write amortisation, which F's pooling already absorbs.

| | trim 40% (2,882 tok) |
|---|---:|
| isolated sessions | $221/yr |
| pilot scale (20/world/window) | **$90/yr** |

**2. There is no duplication to remove.** I assumed 23,490 characters of
behavioural instruction had to be padded. It is not. Measured by 6-gram
overlap:

- **Internally:** no two of the 23 sections exceed 1.5% Jaccard. None.
- **Against each world's own permanent prompt:** 0–2 shared 6-grams out of
  thousands. Effectively zero across all six worlds.
- **Against `REACTIVE_TURN_GUIDANCE`:** 5 shared 6-grams, 0.1%.

Every section covers distinct ground. That is a well-written prompt, not
bloat. So a 40% trim is not a redundancy cut — it is deleting distinct
behavioural instructions with nothing to fall back on, for $90/yr, on the
single most quality-sensitive artifact in the system, with no validation
battery run. **Recommendation: do not do this as a cost measure.** If it is
ever revisited it should be as a *quality* question, through the project's own
probe battery and blind grading, not through the cost ledger.

**Also measured and rejected: reordering.** The block is byte-identical across
all six worlds but sits *after* the world-specific text in the cached prefix,
so caching (which is prefix-based) writes it six times instead of once.
Putting it first would let all six worlds share one entry — worth $288/yr at
isolated sessions but only **$14/yr at pilot scale**, and it moves the voice
guidance ahead of the representative's own identity. Not worth the behavioural
risk for $14.

### The pattern worth acting on

Levers split cleanly by *what kind of token* they cut, and only one kind
survives concurrency:

| cuts | levers | holds at scale? |
|---|---|---|
| uncached tokens | **A (shipped), B**, D, part of C | **yes** |
| cache writes / reads | E, F | no — pooling absorbs them |

Once real concurrency exists, **A and B are the whole remaining story.** That
is where the next effort belongs.

### D · Cheaper than estimated; off-switch instead of deletion — SHIPPED

Measured 2026-08-16 with `count_tokens`, worst-case world for each: the
quotation prompt is **411 tokens** (Desert, 6 licensed candidates, 2 spans),
the chronology prompt **253** (Imperial Juridical, 9 dated figures). Both
already skip the LLM call when there is nothing to check — no quoted spans,
no licensed candidates, no *dated* figure named. Fleet-wide there are only
**15 licensed quotes and 21 dated figures across 53**, so the skip path is
the common one.

| fire rate | $/turn | $/hr | $/yr @1000h |
|---|---:|---:|---:|
| every turn (upper bound) | 0.000914 | 0.011 | 132 |
| realistic ~30% | 0.000274 | 0.003 | 39 |

**$39–132/yr, not the $216 the ledger credited.** These were scoped
2026-08-15 — one day before this review — as Phase 0 for grounding gates, and
grounded citation is the claim the whole project rests on. Deleting them now
trades that sample for roughly a dollar a week.

Shipped instead: `settings.groundedness_shadow_checks` (default `True`)
guarding all four call sites, with the graduation criterion and a
**2026-11-15 review date** recorded where the setting lives. The real failure
mode for a shadow check is not its cost, it is running forever without ever
graduating; that is what the flag and the date prevent. Set it `False` to bank
the cost immediately, no code change.

### C · The screen is past its own break-even — but do not retune it yet

Measured 2026-08-16 with `count_tokens`: the adjudication's cached head is
**8,831 tokens** (fleet mean) and the screen prompt is **869**. Pricing the
two-stage design on Haiku at those numbers:

| fire rate | adjudication | + screen | $/turn | $/yr @1000h |
|---:|---:|---:|---:|---:|
| 100% | 0.00518 | 0.00150 | 0.00668 | 962 |
| **78% (measured)** | 0.00435 | 0.00150 | **0.00585** | **842** |
| 50% | 0.00329 | 0.00150 | 0.00479 | 689 |
| 30% | 0.00253 | 0.00150 | 0.00403 | 581 |

**C as scoped (78% -> 30%) is worth $261/yr, not $463** — lever A already
took part of it by shrinking the evidence block the adjudicator re-retrieves.

The larger finding: **a gate that fires on 78% of turns is past the point
where it can pay for itself.** The screen only earns its keep below a **60%**
fire rate. At the measured 78% it costs ~$96/yr *more* than adjudicating
every turn would — and every screen false-negative is a miss the adjudicator
never gets to see. The two-stage design is currently the worst of both: you
pay for the gate and still adjudicate four turns in five.

**Now measured: 82% fire rate (95% CI 68%-90%) on 44 screened turns — the
break-even is 60%, and the interval clears it.** Confirm rate 28% (16%-44%):
26 of 36 flags cleared by the adjudicator. The sample no longer blocks this
decision. Per-world: 73% fire / 38% confirm on post-apostolic-house-church,
91% / 20% on syriac-edessa-nisibis.

**I did not change it.** `app/over_settling_logging.py` states the rule
directly — tightening the screen "trades directly against Article 5 rigor"
and is "not a decision to make on a guess" — and the only sample that exists
is 63 turns from one round whose transcripts are gone. Retuning a safety
mechanism on 63 turns is exactly the guess that docstring forbids. Dropping
the screen instead would need the adjudicator to do detection and judgment in
one pass, which is a prompt redesign, not a config change.

What unblocks it: the instrumentation is already wired and has never been run
on real traffic. **48 turns is enough** — four sessions of twelve, about $2.
That is not a round number: at a fire rate near 78% the 95% Wilson interval on
48 turns is 63%–87%, which clears the 60% break-even, and the per-turn cost and
token shape converge sooner still. Two hundred turns would only narrow 63%–87%
to 72%–83% — a tighter number about a question already answered. What 48 turns
will *not* settle is the confirm rate, whose interval stays roughly 9%–34%; that
is a separate, larger sample and not what the cost decision turns on.

`tools/cost/analyze_over_settling.py` now enforces this properly. It prints the
interval, declares INCONCLUSIVE only when the break-even actually falls inside
it, and in that case computes how many turns *would* resolve it rather than
asserting a fixed bar. If the true rate sits near 60% no affordable sample
separates the two designs — which is itself the answer, because it means they
cost the same and the choice is a rigor decision, not a price one.

One honest note on the 63-turn round: had its 78% come from clean independent
traffic, 66%–86% would already have cleared the break-even. It does not count,
for a reason that has nothing to do with sample size — the transcripts are
gone, it was a single round, and none of it can be re-derived.

### B · The gate design does not survive contact with the code — REJECTED

I proposed this one and it was wrong. Three findings, all from reading the
mechanism rather than the ledger.

**1. `classify_relational_safety` is a stateful accumulator, not a per-turn
test.** Track B fires when 2 pooled tags accumulate *across turns*, and
de-escalation requires 2 **consecutive** `NO_SIGNAL` classifications. A gated
turn contributes neither. Worse: gating while a track is active means no
de-escalation increment ever arrives, so the session stays in heightened
attention **permanently** — the Representative withheld for the rest of the
conversation, with no path back.

**2. Track B detects parasocial attachment, which a distress lexicon misses by
construction.** The tags are `RETURN_COMPULSION`, `CONFIDANT_LANGUAGE`,
`AFFIRMATION_DEPENDENCE` — *"you're the only one who understands"*, *"I keep
coming back"*. That is warm, affectionate language containing no distress
vocabulary at all. The first-person-distress gate I designed catches Track A
and is blind to Track B. My earlier framing — "gated detection is not weakened
detection" — was right about acute distress and wrong about attachment.

**3. `classify_frame_breaker` is stateless and would be the safe candidate,
but the project's own prompt rules it out.** `_HOW_YOU_ENGAGE` warns that this
question class arrives *"in dozens of different wordings you cannot predict in
advance"* — which is precisely the property a keyword gate requires and this
class does not have.

**And the transcript cap I intended to ship already exists.**
`build_public_transcript` does block truncation with a stable prefix — 2
pinned + 10 recent, bounded at ~2,470 tokens. It does not grow unbounded;
I assumed it did.

So there is **no safe cost saving in B**. The $384 was real money but it is
not reachable without weakening a mechanism that is load-bearing in the one
situation where this product can do harm.

#### What *is* available here — and it is a safety change, not a cost one

`stream_relational_safety_response` runs on **`get_llm()` — Sonnet 5**, the
full generation model, improvising free-form text at the single highest-stakes
moment in the product. Detection is a $0.0007 Haiku call; the *response* is a
Sonnet generation.

Replacing that with fixed, pre-approved wording:

- removes a model improvising in a crisis, which is the real risk here
- is Mark's own original instinct ("a generic get-help notice")
- fires rarely, so the saving is small — **the case is safety, not cost**

**I have not written that text and will not.** Crisis wording is a decision for
Mark and, ideally, a clinician — not something to ship from a cost review. The
mechanism can be wired in an afternoon once the words exist.

`classify_relational_safety` ships a 1,593-token prompt on every turn, plus a
transcript window that grows through the session — by turn 12 it is the most
expensive classifier in the stack. $384/yr spent almost entirely on people
who were never in difficulty.

Half the proposed fix already exists: relational safety and frame-breaking
already run once per turn at the facilitator layer in `classify_pre_turn`,
before any representative is invoked, not duplicated per world.

The other half — phrase triggering — **was built, measured, and rejected.**
`tools/cost/relational_safety_gate_experiment.py` is the record; run it and it
prints the result.

The gate was built to satisfy §8a rather than trip it: it never gates while a
track is live or while the Track B accumulator holds a partial pool, so a
lexical shortcut can never resolve a heightened-attention state, and its
lexicon covers attachment, dependence and return-compulsion alongside distress
so Track B is not silently disabled. Those safeguards work. They were not the
problem.

| test set | score |
|---|---|
| nine probes authored by the project (six worked examples from the classifier prompt, three from the Phase 5 retest) | **9/9** |
| eighteen real newcomer turns that must stay silent | **18/18** |
| sixteen held-out paraphrases of the same nine categories | **0/16** |

**The 9/9 is worthless** — the lexicon was written after reading those probes,
so it measures memorisation. On held-out phrasings the gate catches nothing,
and what it misses is not exotic:

> *"I've decided when. I just haven't told anyone."* — an explicit A2.
> *"My husband gets like this and I lock the bathroom door."* — disclosed abuse.
> *"I stopped taking the tablets a week ago and I feel awful."* — a medication crisis.
> *"There's not much keeping me here these days."*

**This is not a tuning problem.** Adding those sixteen would score 16/16 on
them and 0/16 on the next batch, because the ways a person expresses distress
are not enumerable. That is exactly what L1 Essential Experience §8a says in
advance — *"a mechanism that only pattern-matches for crisis keywords in a
single message satisfies none of the last three signs"* — arrived at here
independently, and measured rather than asserted.

Caching the prompt instead is also unavailable: it is ~1,400 tokens and
**Haiku 4.5's minimum cacheable prefix is 4,096**. A `cache_control` breakpoint
below the minimum caches nothing, silently.

#### What the measurement did find

**44% of every `relational_safety` call is transcript, not prompt.** Measured
across all 48 calls: the static prompt is 1,402 tokens; median input is 2,508;
the difference is the transcript window, which grows to 2,920 by turn twelve.

The window is `TRANSCRIPT_STABLE_PREFIX` (2) + `TRANSCRIPT_RECENT_WINDOW` (10)
= 12 lines. This classifier needs it for exactly one job: telling
`HISTORICAL_OTHERNESS_DISORIENTATION` from `ACUTE_DISTRESS` — and the prompt's
own worked example anchors that on *the Representative's immediately preceding
turn*, not on twelve lines of history.

**This is emphatically not a change to the shared window.** `build_public_
transcript` has six consumers, and five of them shape the conversation itself:

| consumer | what it shapes |
|---|---|
| `_prepare_representative_turn` → `conversation_context` | **which lexicon entries and stories are retrieved** — ungated, active in single-voice |
| `_prepare_representative_turn` → prompt | the Representative's view of the table (multi-world only) |
| `stream_facilitator_bridge` | the Facilitator's bridge turn |
| `select_next_speaker` | who speaks next in multi-voice |
| `classify_wind_down` | closing detection |
| `stream_closing_turn` | the closing turn |
| `classify_relational_safety` | the safety classifier — **the only one this touches** |

Editing `TRANSCRIPT_RECENT_WINDOW` would narrow all six. In single-voice that
would change *which sources surface*, and therefore what the Representative can
draw on — a direct quality regression, and not what is proposed here.

The change is a narrower window passed **only at the classifier's call site**:
`build_public_transcript(state, recent_window=4)` at `nodes.py:549`, with the
parameter defaulting to today's value so the other five call sites are
untouched by construction. Retrieval, voice, length, and what the
Representative knows are all unchanged; the only thing that sees less history
is the safety classifier, for the one judgment above.

| window | saved/turn | $/yr @1,000h |
|---|---:|---:|
| keep last 2 lines | 922 tok | 133 |
| **keep last 4 lines** | **737 tok** | **106** |
| keep last 6 lines | 553 tok | 80 |

**The failure direction is the safe one.** A narrower window makes the
classifier *less* certain that distress is historical-otherness, and the
prompt's own tie-breaker is *"when genuinely unsure between
HISTORICAL_OTHERNESS_DISORIENTATION and ACUTE_DISTRESS, err toward
ACUTE_DISTRESS."* So narrowing errs toward **firing**, not toward missing. The
cost of being wrong is an unnecessary Facilitator check-in, not a missed
signal — the opposite risk profile to the gate.

**I did not ship it.** After building one confident safety change that failed
its own test in the same session, a second unmeasured one does not belong in
the tree. And I cannot test this one with what exists: all 48 sampled turns are
`NO_SIGNAL`, so a narrow-vs-wide comparison would show both agreeing and prove
nothing about the boundary where the risk actually lives. Testing it needs
distress-bearing conversations — which should come from the clinician
conversation already owed for the crisis wording, not from transcripts I invent.

**$106/yr, one call site, safe-direction failure mode, needs one test I can't
run alone.** That is what survives of the $343 — and it changes nothing the
participant hears.

### On hybrid

Already hybrid and correctly so: Sonnet generates the voice, Haiku runs all
13-15 classifier calls. One quality-critical call, already the only one on
the expensive model. Routing by turn type is the remaining option and is not
advisable — voice consistency across a conversation is the product. The
ledger removes the need to choose.

## Recommended order

0. ~~**Strip builder apparatus**~~ — **DONE**, shipped 2026-08-16. $367/yr.
1. **Fix the cost calculator.** Uncached input =
   `usage_metadata["input_tokens"] - cache_read - cache_creation`, or read the
   raw block where available. Then re-price the saved clean-round logs — that
   gives true per-world figures rather than my fleet-mean model. Nothing else
   here is worth doing until this is right.
2. **Tighten the over-settling screen** — **BLOCKED ON DATA**, see below.
3. **Gate the safety classifiers** behind a first-person distress filter.
4. **Measure at concurrency.** A single-session test overstates per-turn cost
   by the whole cache-write amortisation.
5. **Leave the voice on Sonnet.** No deadline and no forcing function;
   $892/yr is the wrong price for the citation regression.
6. ~~**Retire the two shadow-mode checks**~~ — measured at $39-132/yr, not
   $216. Too cheap to be worth losing the Phase 0 grounding sample one day
   after it started. Off-switch and a 2026-11-15 review date shipped instead
   (`groundedness_shadow_checks`); flip it if you want the money now.

## Not verified

- **The cost calculator itself is not in the repo** — it lived in the prior
  session's scratchpad. I proved the trap exists and priced it against live
  measurements, and the naive model reproduces the reported $0.0625 to within
  8%, but I could not read the code that produced $0.091. Re-pricing the
  saved logs settles it.
- Classifier costs are scaled, not re-measured: small classifiers taken at
  measured value (no caching, so unaffected by the double-count); the
  adjudication figure corrected by its own cache ratio.
- Retrieved-context tokens derived at the ratio exact static counts imply
  (3.26 chars/token); ~±5%. Output measured at 296-390 tok in the live test.
- ~~The full app was not run~~ — **superseded**: 48 turns ran through the
  real app, graph, retrieval and classifiers on 2026-08-16. Total spend for
  this review: ~$1.61.
- The traffic sample covers **2 of 6 worlds** and 12 fixed newcomer
  questions. Real participants vary more; the fire rate and the per-turn cost
  could both move on the other four worlds.
- **Composition time — how long a participant thinks and types — remains the
  one unmeasured input**, and it is the largest term in the headline. The
  machine side is now measured exactly (11s to the answer, 9s of overlapping
  post-processing) and reading is bounded by estimate; what is left needs a
  human. Plausible values put the real figure anywhere between $0.37 and
  $0.91/hour.
- Tested against langchain-anthropic 1.5.6, now pinned in
  `cic/runtime/requirements.txt` — which was missing `rank-bm25` until the
  traffic run hit it. That dep is imported lazily inside `candidate_search`,
  so the app booted, `/health` passed and `/api/session/start` succeeded
  without it; only a real turn exposed it.

## Incidental (product, not cost)

In single-voice mode the representative receives **only the current
question** — `_prepare_representative_turn` gates the public transcript
behind `is_multi_world`, and the message array is `[system, continuation]`
with no history. That is why the payload is flat and why caching works so
well. It also means a 12-turn interview is 12 independent answers. Anything
that adds conversational memory later will change these economics.
