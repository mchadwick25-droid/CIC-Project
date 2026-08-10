# Update for the Voice Rebuild handoff thread — 2026-08-09

**From:** the API-cost / provider-options thread (branch `claude/api-cost-alternatives-upbipe`)
**Why you're getting this:** a change shipped today that moves the ground the voice work stands on. Nothing in the voice records is wrong; the model they were measured against is no longer the model in production.

> **Scope note, stated up front so it can be corrected:** this was written without visibility into the Voice Rebuild thread's own current state — I could not find its launch prompt or decision log in the repo (searched `Ministry/Operations/Standing/Launch-Prompts/`, `Ministry/Communication/`, `Ministry/Features/`, and the Task Board). So this reports what changed on my side and what it implies for voice work generally. If the thread is further along than this assumes — or already re-measuring — say so and I'll re-aim it.

---

## 1. The one thing that matters

**Representative generation moved from `claude-sonnet-5` to `claude-haiku-4-5-20251001` today.** Deployed via `render.yaml`; also changed in `app/config.py` and `.env.example`. Reverting is one line.

**Every voice measurement in this repository was taken on Sonnet.** That includes all six `native_measure` blocks:

| World | Record | `typical_words` | Measured from |
|---|---|---|---|
| Syriac | `syrvoice001` | 98 | Phase-5 live-test transcript, 19 responses, mean 98, range 41–165 |
| Hieronymian | `halvoice001` | 94 | two live-test transcripts, 22 responses, mean 94, range 41–157 |
| Alexandria | `alexvoice001` | 140 | Phase-5 Round-2 retest, 123/138/166/136 words, mean ~141 |
| Imperial-Juridical | `ijcvoice001` | 120 | battery-measured 251–256 mean, 389 max |
| PAHC | `pahcvoice001` | 70 (designed) | battery measured runtime at 246–272 mean |
| Desert | `desertvoice001` | 60 | — |

These are empirical observations of **how a specific model rendered these prompts**. They are not properties of the voice design. On a different model they are hypotheses again.

The same applies to the S6.2 `s27_voice` gates and voice demos for ALX, SYR, IJC, PAHC and HAL — all graded against Sonnet output.

---

## 2. The concrete mechanism this breaks first

`HARD_CEILING_WORLDS` (`app/graph/nodes.py:1617`) — every ceiling was frozen against a Sonnet-measured profile, and several were set *deliberately at* the measured maximum so the solo register would never trigger:

| World | Ceiling | Trigger × | How it was set |
|---|---|---|---|
| Desert | 60 | 1.5 | stated measure; code comment records uncorrected drafts at 175–180 |
| Hieronymian | 160 | 1.2 | S6.2/HAL freeze — "just above the voice profile's measured solo max" |
| Alexandria | 160 | 1.2 | set at measured solo max |
| Syriac | 165 | 1.2 | S6.2/SYR freeze — "= the voice profile's measured max… so the solo register never triggers" |
| PAHC | 150 | 1.5 | *enforcing*, not a backstop — pulls 246–272 measured toward a 70w design |
| Imperial-Juridical | 180 | 1.5 | moderate enforcing; measured 251–256 mean / 389 max |

**A ceiling set precisely at one model's measured maximum has zero margin against a different model.** Three of six (HAL, ALX, SYR) are in exactly that position.

When a draft exceeds ceiling × trigger, the **whole turn is regenerated at full price** — and the retry re-sends the entire prompt *plus* the discarded draft, so it costs more than the original. Desert already regenerated on **80% of turns** on Sonnet, at 23.9% of that conversation's cost.

Two consequences, and the second is the one worth flagging:

1. **Cost.** If Haiku's length adherence is worse, extra regenerations eat the saving the switch was made for. That's a budget problem and it self-reports.
2. **Voice.** Regeneration is not neutral to the thing you're rebuilding. A silently-regenerated turn is the *second* draft, produced with the discarded first one in context. If the rate moves materially, the register participants actually experience shifts with it — and that shift is invisible in the transcript, which shows only the surviving draft. **If the voice rebuild is calibrating against live output, it needs to know which turns were regenerated.**

`app/length_ceiling_logging.py` already emits a machine-parseable line per outcome — fire rate, dead-zone rate, and first-draft word distribution, per world. **The instrument exists; nobody has read it since the switch, because the switch is hours old.**

---

## 3. What I'd ask the voice thread to decide

Not for me to call, but these are the forks I can see:

- **Re-measure `native_measure` on Haiku, or treat the existing numbers as the design target and let the ceilings enforce toward them?** These are genuinely different strategies. PAHC and IJC are already the second kind (enforcing ceilings pulling runtime toward a *designed* measure); SYR/HAL/ALX are the first kind (descriptive ceilings set at what the model actually did). The switch makes that split unstable — the descriptive ones are now describing a model that isn't running.
- **Does the rebuild re-baseline before or after the Haiku quality battery?** They need the same live run. Doing them separately spends the key twice and risks two incompatible measurement bases.
- **Is `typical_words` a voice-design property or a model-behaviour observation?** The records currently read as both. The switch forces the question.

---

## 4. Decisions from today that the voice thread should hold as fixed

Recorded so nobody re-opens them in your thread:

- **Quality tolerance is set.** Mark, 2026-08-09: *"im ok with a cheaper and a small drop after 15 turns."* An ambiguous battery result is a **PASS**, not a re-run. The battery measures *how large* the drop is, not whether any drop is acceptable.
- **No participant-facing defect notice.** Mark, same day: *"we don't need a notice, we will use the best tool we can afford, if there is feedback that we are having problems we will look at it, but no reason to get them looking for things they wouldn't notice."* Settled — the disclosure question raised earlier today is closed, and the voice thread should not re-litigate it. The operative consequence is that **the feedback path is now the detection mechanism**, so it needs to actually reach someone (`cic-website/pilot-feedback.html` exists; whether anything watches it is worth confirming once).
- **The tolerance covers voice and constraint adherence. It does not cover the acute-distress path.** Relational-safety and distress remain pass/fail with no tolerance band.

---

## 5. Two corrections to numbers that may have reached your thread

If either of these was quoted into the voice rebuild, they've moved:

- **The "delete the dead retrieval calls, −33%" item was wrong.** That saving was already banked at S3.4; the code was uncalled. Correct magnitude ~11%, already realised. Deleted today for hygiene, worth $0.
- **Cache writes were priced on the wrong basis** in my analysis (1h rate applied to a 5m-measured baseline). All figures re-derived; movements of 1–5 points, no conclusion changed.

**And one basis warning that affects any `$/hr` figure crossing between threads:** my analysis and `cost_floor_model.py` price at **30 turns/hr solo, 24 table**. The cost-reduction scope and the funding model price at **6 turns/hr reflective**. Those denominators differ by 4–5×. A `$/hr` from one is not comparable to a `$/hr` from the other. Worth settling which pacing the $0.25–1.00/hr target band was set against before anyone declares in-band or out.

---

## 6. Suggested single next action

**Fold the voice re-baseline into the Haiku quality battery run.** One live key, one session, three outputs: the blind-graded voice/constraint result, fresh `native_measure` data for all six worlds, and the regeneration rate per world read off `length_ceiling_logging`. Splitting them costs more and produces two bases that can't be compared.

If the voice thread would rather hold Sonnet until it has re-baselined, **that is a one-line revert** — `LLM_MODEL` in `render.yaml`. Cheap to reverse, and worth saying explicitly so it doesn't feel like a fait accompli.

---

**Reference:** `Ministry/Technology/CiC_LLM_Provider_Cost_Options_2026-08-09.md` · `Ministry/Technology/Pass3/provider_repricing.py` · `Ministry/Funding/CiC_Org_Funding_Decision_Log.md` (2026-08-09 entries) · `render.yaml` (the reasoning lives beside the value)
