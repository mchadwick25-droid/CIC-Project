**cic-poc measurement;** superseded by the M8 reconciliation (`engine/m8/reports/`).

---

# CiC Cost Structure — Grounded Technical Report

**2026-07-30 · Funding Strategy thread · Opus agent, background dispatch, codebase-grounded**

**Status: research to react to, not a decision.** Everything below is measured from real code and
the one committed instrumented run — not web research, not generic modeling. Two findings change
the frame before the numbers, so they come first.

---

## Finding 1: the $1.25–1.50/hour anchor does not hold up

This was given to the research agent as tested ground truth. The codebase and the project's own
records say otherwise, so it's flagged rather than anchored to.

- It originates in this thread's own `Decision-Log.md` (2026-07-22) — eight days old at the time
  of this report, not fresh. The Business Roadmap repeats it with the phrase "this week," which is
  what made it read as current.
- **No measurement artifact backs it.** Its only stated support is an arithmetic cross-check
  against a prior per-conversation estimate ($0.20–0.75 ÷ 15–25 min ≈ $1.20–1.50/hr) — consistent
  with back-derivation from a projection, not a fresh test.
- **A later entry contradicts it.** `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
  (2026-07-24): "Mark's funding assumptions were built around $1.00/hour; real (if still
  incomplete) data puts current cost around **$2/hour**." That same entry records a literal $1.25
  as a *single pilot session total* for a single-world 3-round sitting — a plausible origin for a
  session total drifting into a per-hour rate.
- The ~$2/hour figure, not $1.25–1.50, is what got carried into the engineering work.

Bottom-up math in this report lands on **$2.16–3.60/hour for a 3-Representative table** and
**$0.78–1.56/hour for 1:1**. The $2/hour figure reconciles; $1.25–1.50 only reconciles for 1:1 at
a slow pace.

## Finding 2: the only real measurement is stale

The B-COST baseline (`cost_baseline_2026-07.md`, run 2026-07-26, 689 calls / 40 turns / $6.6173)
is the sole instrumented cost data. Since then, 25+ commits touched `app/`. Two confirmed removals
(replaced by a local CPU cross-encoder, −$0.55/run) and two confirmed additions (both per-turn
Haiku calls, added 2026-07-27). **33 instrumented call sites exist in current code; only 20 fired
in the measured run.** Net cost direction since the baseline is genuinely unknown.

---

## 1. Cost per transaction (one participant turn)

**Documented.** Per turn the system fires **1 Sonnet call + 8–10 Haiku calls** at a 1:1 table.

- Representative generation: `claude-sonnet-5`
- All classifiers/selector/monitors: `claude-haiku-4-5-20251001`

Always-on per turn regardless of table size: frame-breaker detection, relational-safety
screening, the epistemology bridge, the modern-term bridge, the repair classifier (migrated worlds
only). Per *sub-turn*: drift detection, over-settling screen.

**Prompt size — measured, and it does not grow.** Mean total prompt per response:
**31,200–39,700 tokens**; output only 154–416 tokens. Context does **not** accumulate turn over
turn — the system rebuilds a bounded public transcript rather than appending indefinitely.

**Caching is real and load-bearing, but the TTL is short.** Two cache breakpoints exist (static
prompt, reactive-turn guidance). Measured effect: cache-warm turns average **$0.111**; cache-cold
turns average **$0.179** — a **61% penalty** when the 5-minute cache window lapses. At any human
conversation pace slower than one turn per 5 minutes, most turns are cache-cold. A 1-hour cache
option exists in the code but isn't applied.

| Table | $/turn (standard rate) | $/turn (introductory rate) |
|---|---|---|
| 1 Representative | $0.107–0.183 (mean **$0.130**) | $0.082–0.133 (mean $0.097) |
| 3 Representatives | $0.247–0.549 (mean **$0.360**) | $0.197–0.398 (mean $0.272) |

---

## 2. Cost per conversation by table size

**The scaling is not linear, and this is the single most useful finding in this report.**

A Living Table round is capped at 2–6 sub-turns *per round*, not per world — a 3-Representative
table can complete a round with only 2 of 3 worlds actually speaking. Adding a third
Representative therefore buys more Haiku governance overhead (more selector/cross-checking calls)
rather than proportionally more Sonnet generation. Single-world conversations never invoke that
overhead at all.

| Table | Sonnet generations/turn | $/turn (standard) | Basis |
|---|---|---|---|
| 1 Rep | 1 (2 if a length-retry fires) | **$0.13** | **Measured** |
| 2 Reps | 2–6 | **~$0.29** | **Inferential-Thin — never directly measured** |
| 3 Reps | 2–6 (mean 3.5) | **$0.38** | **Measured** |

**The 2-Representative case has never actually been measured.** The existing baseline set contains
three 1-world conversations and one 3-world conversation — no 2-world data point exists anywhere.
The $0.29 above is interpolated, not observed.

Per 20-turn conversation, standard rates: **1 Rep ≈ $2.60 · 2 Reps ≈ $5.80 · 3 Reps ≈ $7.20.**

**A concrete cost bug worth knowing about, tangential to funding but real:** the Desert world has
a 60-word response ceiling; exceeding it triggers a *complete second Sonnet generation*. In the
measured run, Desert regenerated on 8 of 10 turns, making it 74% more expensive per turn than
House-Church purely from this retry mechanism — invisible in any metric, only visible via debug
output. Worth a note to whichever thread owns `cic-poc` engineering.

---

## 3. Cost per hour

The turn cap counts Representative turns, not participant turns — at a 3-Representative table
burning multiple sub-turns per round, the cap binds after roughly 7–20 participant turns rather
than the full count. No document anywhere states an assumed turns-per-hour pace.

**Standard rates (in force from 2026-09-01):**

| Pace | 1 Rep | 2 Reps | 3 Reps |
|---|---|---|---|
| 6 turns/hr (10 min/turn) | $0.78 | $1.74 | $2.16 |
| 10 turns/hr (6 min/turn) | $1.30 | $2.90 | $3.60 |
| 15 turns/hr (4 min/turn) | $1.95 | $4.36 | $5.41 |

**Reconciliation with the $1.25–1.50/hour figure:** reachable only at **1 Representative**,
requiring 9.6–11.5 turns/hour. A 3-Representative table only reaches that band at a 15-minute-
per-turn pace. The stated figure is best read as a 1:1-only number; the project's own $2/hour
figure (System Hub, 2026-07-24) is the better general planning anchor.

---

## 4. Current model pricing — verified live 2026-07-30

| Model | Input | 5m cache write | 1h cache write | Cache read | Output |
|---|---|---|---|---|---|
| Sonnet 5, **through 2026-08-31** | $2.00 | $2.50 | $4.00 | $0.20 | $10.00 |
| Sonnet 5, **from 2026-09-01** | $3.00 | $3.75 | $6.00 | $0.30 | $15.00 |
| Haiku 4.5 | $1.00 | $1.25 | $2.00 | $0.10 | $5.00 |

**The Sonnet 5 introductory discount expires in 32 days.** Input and output both rise 50%. Sonnet
accounts for 74.2% of dollars on only 11.0% of calls in the measured run, so the blended cost
increase on this system is **roughly +37%, with zero code change, arriving September 1.**

Model routing confirmed accurate to prior documentation: Sonnet for generation, Haiku for
classifiers. Local embeddings (HuggingFace, CPU) remain genuinely free — zero API cost for
retrieval, and the same is now true of the reranker (also moved local).

---

## Free-tier time budget: no hook exists yet

**Documented, not a gap in this report — a gap in the product.** A designed-but-unused `api_usage`
table exists in the database schema, explicitly commented as "the real per-user credit meter" —
but nothing in the running application writes to it. The existing 40-turn cap is per-conversation
and identity-free; nothing meters time or spend per person yet. This confirms the Business
Roadmap's Phase 2/3 plan (set the real free-tier cap from pilot data) is still fully open — no
code has been built toward it either way.

One correction worth making elsewhere: the original Go-Live Cost Model's "60-turn cap" figure is
outdated — the real current cap is 40 turns, raised recently from 20, and counts differently by
table size as described above.

---

## Synthesis — a recommendation to react to, not a decision

**The $10 / $8 giving structure holds for 1:1 conversation and does not hold for the Living
Table.** At standard September rates, $8/month buys roughly 4.4–7.4 hours at 1 Representative, but
only 1.5–3.2 hours at 3 Representatives — the "$8/month buys ~5–6 hours" framing already in this
thread's own records is a 1:1-only number, off by 2–3× for the Living Table.

**Recommendation: keep $10 / $8 as market-validated, and let table size — not time — be the
variable the free tier actually governs.** Three reasons: it's the real cost driver (a third
Representative roughly triples per-turn cost while the participant experience is still "one
conversation"); it needs no new metering to build, since table size is already capped and chosen
at session start; and it preserves the giving amounts already validated against real market data
rather than reopening that question.

**Two things worth treating as genuinely time-sensitive, independent of that recommendation:**

1. **The September 1 pricing step is currently unbudgeted anywhere in this project's funding
   documents.** Every current cost figure is priced at the introductory rate. A ~37% blended
   increase lands in 32 days with no code change required to trigger it.
2. **A full cost-baseline re-run is overdue, and the one real gap (a 2-Representative data point)
   is cheap to close** — a few hours of compute against a decision worth getting right, and a
   study with this same scope was apparently dispatched by another thread earlier and never
   returned.

**One small, high-leverage technical note, not this thread's to act on but worth passing along:**
switching the cache TTL from 5 minutes to 1 hour is already identified as a one-line change. At a
reflective human conversation pace, most turns currently fall outside the 5-minute window and pay
the measured 61% cold-cache penalty; the 1-hour option costs more on the first write but breaks
even after just 3 reads, which a real sitting comfortably exceeds.
