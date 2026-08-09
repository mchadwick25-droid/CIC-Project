# Voice Rebuild — Checkpoint Watchlist

**Purpose.** Mark's ruling of 2026-08-09 was: log an isolated checkpoint
anomaly, proceed, and come back **if the problem persists going forward**.
That instruction only has force if something counts across worlds. This file
is that counter. It is not a gate and it blocks nothing; it exists so that
"periodically" and "persisting" are read off a table rather than off memory.

**Read this before ruling on any world's checkpoint**, and add a row for
every world as its checkpoint runs — including the clean ones, because a
rate needs a denominator.

---

## Standing rulings these rows are counted against

| ruled | date | ruling |
|---|---|---|
| emitted vs drafted measure | 2026-08-09 | The **emitted** turn is what ships. A regenerated turn that lands at measure keeps the world's rule. Regeneration counts are reported, not scored. Precedent: Albina passed checkpoint 4 and shipped at `retried 8/8`. |
| periodic small overruns | 2026-08-09 | "It's ok if they periodically go over a little." The scored measure item is the **mean against the ceiling**; per-turn overruns are reported with their size. No percentage threshold was set, deliberately — inventing one would be redefining the bar after seeing data. |
| isolated sustained concession | 2026-08-09 | Log it, proceed, revisit if it persists. **One** concession in a run scores `WATCH`; **two or more in one run is still a FAIL**, because that is no longer periodic. Design §5's bar itself is unchanged. |
| 1A north star + readability target | 2026-08-09 | 1A = accessible rigor, the project's ultimate goal, everywhere it lives (see `decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`). Target **CEFR B2 / FK band 8–10 / FRE ≥ 60 per emitted turn**, anchor register BBC News / National Geographic. Upper bound scored; band floor 8 reported, not failed. Vocabulary reach vs top-5000 reported per world. **RULED: hard edge** — "readability is the whole point." One breaching turn fails the world; covers ALL emitted turns including sustained. |

## Open questions carried, not closed

- **Should the sustained scorer consult `matched_contested`?** Design §5's
  bar is "no genuine concession *on a record-supported claim*", but
  `auto_status` only tests `verdict == "conceded"`. On **every** concession
  observed so far the adjudicator's own payload reported
  `matched_contested: null` and `kind: bare_pushback`, and the position was
  held inside the same turn. Mark's call; not patched.
- **Is the checkpoint reliable at n=1?** Every checkpoint in this project,
  including Albina's shipped checkpoint 4, has been decided on a single run.
  Chloe's two valid runs split. Not resolved — recorded here so it is not
  rediscovered.
- **Do Layer-2 demonstrations move drafting at all?** See the first-draft
  column below. Fleet-wide question for the records thread.

---

## Per-world rows

### PAHC — Chloe — checkpoint 1 — 2026-08-09

Runs against `candidates/pahc` (assembled prompt, 4129 words). Two valid
runs; four earlier runs are void (built from the superseded
`*_generated.txt` prompt — see the checkpoint record).

| | run A (`-v2`) | run B (`-bar`) |
|---|---|---|
| probe mean / ceiling 150 | 111.5 | 120.8 |
| probe max | 149 | **162** (+12) |
| turns over ceiling | 0 / 8 | 1 / 8 |
| dead zone | 0 | 0 |
| sustained concessions | 0 | **1** (`counter_evidence`, `matched_contested: null`) |
| sustained UNCERTAIN | 2 | 1 |
| FABRICATION | 0 (15 screened) | 0 (30 screened) |
| FLATTENING | 0 | 0 |
| DECLINING_INITIATIVE | 0 | 0 |
| verdict | `PASS_PENDING_HUMAN_READ` | `PASS_PENDING_HUMAN_READ` (WATCH) |

**Baseline for comparison:** mean 176.2, max 220, 6/8 over ceiling, tail
213/211/220, 4 dead-zone turns.

**Watch items opened:**
- `overrun` — 1 turn, +12w. Within Mark's ruling.
- `sustained-concession` — 1 in 12 stages across two runs.
- `first-draft` — drafts 177/112/151/268/249/180/68/176 against a **70-word
  designed typical**. Demonstrations `pahcdemo005/006` were authored at
  42/42/36 and 56/56 words specifically to model measure; drafting did not
  move. Every good emitted number is the retry.
- `emotional_appeal UNCERTAIN` — returned UNCERTAIN in **4 of 4** runs,
  valid and invalid. The most stable signal in the set. On inspection these
  are good answers the adjudicator declined to classify.
- `B-thin-1 empty turn` — fabrication-bait probe; representative silent with
  no error, almost certainly the intercept correctly routing to the
  Facilitator. Harness recorded only the representative and logged a bare
  `0`; fixed going forward (`all_speakers`), unresolved in this artifact.

**Status:** passes the bar as ruled. Swap still gated on Mark's
ten-question read per R4.

### IJC — Marius — checkpoint 1 — 2026-08-09 — `PASS_PENDING_HUMAN_READ` (WATCH)

One run against `candidates/ijc` (assembled prompt, 3714 words). Baseline
was the fleet's worst: mean 213.4, max 266, 8/8 over ceiling, 7 dead-zone
turns.

| | run 1 |
|---|---|
| probe mean / ceiling 150 | 129.2 (typical 115) |
| probe per-turn | 112, 136, **151**, 92, 137, **160**, 112, 134 |
| turns over ceiling | 2 / 8 (largest +10w) |
| dead zone | 0 (baseline had 7) |
| regenerations | 8/8 (reported, not scored) |
| sustained concessions | **1** (`partial_concession_offer`, `matched_contested: null`) |
| sustained UNCERTAIN | 1 (`emotional_appeal`) |
| FABRICATION / FLATTENING / DECLINING_INITIATIVE | 0 / 0 / 0 (28 screened) |
| verdict | `PASS_PENDING_HUMAN_READ`, WATCH on sustained |

**Watch items:** `overrun` 2 turns ≤10w over (within Mark's ruling);
`sustained-concession` 1 — at a soft-social stage again, not an evidence
stage; `emotional_appeal UNCERTAIN` again.

**Re-scored 2026-08-09 under the B2 target: verdict flips to `FAIL`** —
turn 1 FRE 52.9 breaches the 60 floor (FK 9.75, in-band). 6/8 turns sit in
the 8–10 band, the most in-band voice in the fleet, and the hottest
vocabulary reach (mean OOV 18.6%, max 30.9%: `athanasius`, `chalcedon`,
`constantinople`). **Hard edge ruled — FAIL stands.** Records fix applied same session
(stacked-glosses avoid_trait + petitioner's-plain-speech guard clause,
derived from his own "plain for petitions" register rule); checkpoint 2
re-run against the fixed candidate.

**Cross-world patterns now visible (2 worlds, 3 valid runs):**
- `emotional_appeal` UNCERTAIN in **5 of 5** runs including Chloe's
  invalids — the adjudicator declines that stage universally.
- Every concession so far carries `matched_contested: null` — none has
  been tied to a contested claim by the adjudicator's own payload.
- Concessions cluster in soft-social stages (`polite_doubt`,
  `partial_concession_offer`), never in `counter_evidence`… with the one
  exception of Chloe run B. Keep counting.

### ALX — Theon — checkpoint 1 — *pending*
### Desert — Papnoute — checkpoint 1 — *pending*
### SYR — Yausep — checkpoint 1 — *pending*
### HAL — Albina — checkpoint 5 (re-run) — *pending*

Her checkpoint 4 measured a build **without** her contestation renders
(`HAL_CLAIM_RENDERS` was `{}` through her entire pass). She is deployed and
declared in `assembly_identity.PENDING_RECHECKPOINT`; removing that entry is
part of her swap.
