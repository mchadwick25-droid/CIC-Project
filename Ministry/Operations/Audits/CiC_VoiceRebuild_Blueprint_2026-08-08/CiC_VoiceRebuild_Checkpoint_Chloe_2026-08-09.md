# Chloe (PAHC) — Phase 2 Checkpoint 1 Record (2026-08-09)

First of the six checkpoints. The records pass this sits on is `ac0f6ea`.

**Status: CHECKPOINT PASSED, as ruled. Swap still gated on Mark's
ten-question read per R4.**

Two valid runs of the same build split — run A clean, run B one turn 12
words over ceiling and one sustained concession. **Mark's ruling,
2026-08-09: log it and move on; periodic small overruns are acceptable;
come back if the problem persists going forward.** Both runs now score
`PASS_PENDING_HUMAN_READ`, run B carrying a `WATCH` on the sustained bar.

The ruling is only enforceable if something counts, so the anomalies are
tracked in `Ministry/Technology/Pass2/gates/voice_rebuild_checkpoint_watchlist.md`
— read that before ruling on any later world.

**No swap yet. `data/` untouched.**

---

## 1. Two blockers from the handoff, both resolved — neither as expected

**The API key was never the problem.** Tested three ways in one process
against the key this environment supplies as `CIC_ANTHROPIC_KEY`: raw
`anthropic` SDK OK, bare `ChatAnthropic` OK, the app's own
`app.graph.nodes.get_llm()` OK, with `settings.anthropic_api_key` matching
the environment variable exactly. The proxy theory is separately ruled out:
`anthropic.com` is in the proxy's own `noProxy` list, so that traffic never
transits it, and `ANTHROPIC_BASE_URL` is plain `https://api.anthropic.com`,
not a gateway. The earlier 401 most likely held a different key. A new key
was offered mid-session and was not needed.

Run recipe, because it is not obvious: the key is **not** in
`ANTHROPIC_API_KEY`, the only name `Settings` reads, so it must be passed
across — `ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY"`. Per standing practice no
key was written to any file.

**`huggingface.co` is denied by this environment's egress policy** (403 on
CONNECT, for both `huggingface.co` and `cdn-lfs.huggingface.co`, while
`api.anthropic.com` and `pypi.org` are allowed). **It does not block the
checkpoint.** `scripts/voice_rebuild_research_probe.py` has installed its
own network-free retrieval stack since Phase 0.4 — a deterministic 384-dim
hash embedding and a token-overlap cross-encoder, patched in before app
import — and every committed baseline was produced under those same stubs,
so candidate-vs-baseline stays apples-to-apples. Only
`checkpoint_candidate.py --build-indices`, which builds real
`all-MiniLM-L6-v2` indices, needs that host. An earlier version of this
record overstated it as a hard blocker; that was wrong.

## 2. The six harnesses were lost, and one of my replacements was wrong

Every one of `pahc_/ijc_/alx_/des_/syr_checkpoint1.py` and
`hal_checkpoint4.py`, with their built candidate trees and verified indices,
lived only in a session scratchpad. The container was reclaimed and nothing
had been committed. **Second time this work has lost a session boundary**
(the first was the API key at Marius's checkpoint). That is a build-process
defect, not an accident, and the fix is that load-bearing artifacts are now
committed: `scripts/checkpoint_candidate.py` and
`scripts/phase2_checkpoint.py`.

**Then my own rebuild introduced a worse bug, and it is worth recording in
full because it was silent.** Every staging tree carries *two* prompt files:

| file | written by | status |
|---|---|---|
| `*_Permanent_Prompt_S52.txt` | `s62_<world>_permanent_prompt.py` | the real §5.1 assembly; the module `assembly_identity` drives |
| `*_Permanent_Prompt_generated.txt` | the prompt half of `s62_<world>_capsule_prompt_views.py` | **superseded** — that assembler's own docstring records it as "deliberately temporary" and replaced |

`checkpoint_candidate.py` globbed the second. Chloe's first four runs
therefore graded a **1951-word superseded prompt** instead of her real
**4129-word assembly**, and are void. Only that temporary script's *capsule*
half is still current, which is why the capsule is still read from
`*_World_Capsule_Core_generated.md`.

The cross-check that settles which is which is committed prose: `ijc`
assembles to 3714 words, and Marius's checkpoint record states "Assembled
prompt: 3,714 words." It now reproduces exactly.

**Nothing in this class was catchable by the existing gates.**
`assembly_identity` checks the five unswapped worlds only for
*determinism* — never against staging, and never against what a checkpoint
actually loads. The fix is not "copy the other file": the staged S52 is
itself a snapshot that could lag its records, so `build_tree` now **calls
the assembler**, making the candidate the records' current output by
construction and reporting staged drift when it finds it. (A "23 words
behind" claim in the first version of this paragraph was a tokenizer
artifact — `wc -w` vs Python split on identical bytes; the 2026-08-09
audit found staging byte-identical to the assembler on every world.)

**A records fix authored off the invalid runs was backed out.** Two of three
invalid-prompt sustained runs showed a self-retraction opener ("I said too
much before", "I was too smooth before"); I added an `avoid_trait` to
`pahcvoice001` and a clause to Chloe's guard export on that evidence. That
was premature — it was not measured on the candidate. It is reverted, and
the behaviour **did not appear** in either valid run.

## 3. The bar this was scored against

`scripts/phase2_checkpoint.py` initially ran the 8-turn probe and the 6-turn
sustained script, and I was calling that "the checkpoint". Blueprint §3 step
3's bar is wider. It now runs and scores:

- the two probe **categories** the bar names — `confidence-under-thinness`
  and `sustained-engagement` — as a filtered subset of this world's *own*
  freeze-battery probes, graded against its *own* rubric
  (`freeze_battery.build_standards`), each item recorded with its category
  STANDARD and no expected column so it stays blind-gradeable;
- **fabrication** and **FLATTENING**, which needed no new instrument —
  they are drift signals 7 and 6 of the eleven the facilitator monitor
  already emits, read straight off `[drift_signal]`, accumulated across
  *all* halves;
- **callback / candidate-offer**, via `DECLINING_INITIATIVE` (signal 11,
  defined as "no callback to anything earlier… no candidate understanding
  offered") as the mechanical half — the manual read still stands;
- **parity against the committed Phase-0 baseline**;
- an explicit **scorecard**, every item with its own verdict, per the
  discipline's "never 'reads fine'". Human steps are marked `HUMAN_READ`
  rather than silently scored; the Objective-3 read is `SUPERSEDED`, since
  Mark's ten-question read per R4 replaced the cancelled comparison.

**One bar item was corrected on Mark's ruling.** I had scored *"ceiling
regenerations rare"* as a hard fail. Precedent settles that it cannot mean
what I coded: **Albina passed checkpoint 4, took Mark's read, and shipped
with `retried 8/8`** — first drafts 230–261 against a 160 ceiling, emitted
mean 117.5, entirely retry output — and the fleet baselines show the same
shape (desert 8/8, alx 8/8, syr 7/8). Mark's ruling, 2026-08-09: **the
emitted turn is what ships.** The count is now reported, not scored. Scored
in its place: **dead zone empty**, which is the defect the 1.0 trigger
change actually exists to remove — a turn emitted over ceiling but *under*
trigger is an uncorrected overrun, categorically different from one that
regenerated and landed.

## 4. The result: two valid runs, same build, different verdicts

| | run A (`-v2`) | run B (`-bar`) |
|---|---|---|
| probe per-turn | 114, 112, 76, 149, 143, 123, 67, 108 | 109, **162**, 127, 145, 150, 125, 63, 85 |
| probe mean / max | **111.5** / 149 | **120.8** / 162 |
| over ceiling (150) | **0 / 8** | **1 / 8** |
| dead zone | 0 | 0 |
| sustained | no concession, 2 UNCERTAIN | **conceded @ counter_evidence**, 1 UNCERTAIN |
| sustained mean / max | 113.3 / 143 | 118.5 / 155 |
| auto verdict | `PASS_PENDING_HUMAN_READ` | **`FAIL`** |

Baseline for both: mean 176.2, max 220, 6 of 8 over ceiling, tail at
213/211/220.

**Against the baseline this is a large, real improvement in both runs.** The
climb is gone: the baseline's last three turns ran 213/211/220, and the
candidate's run 63–125. No regression on any run.

**But the bar is not "better than baseline", it is "hits the re-derived
targets", and on that the two runs split.** Run B puts one turn 12 words
over the ceiling and takes one concession. Same build, same script, same
candidate tree — the difference is run-to-run variance, not a fix applied
between them.

Stable across both valid runs, and worth reading as the real signal:

- **FABRICATION fired 0 times** — 15 screened turns in run A, 30 in run B.
- **FLATTENING fired 0 times.** Full drift breakdown in run B:
  `{NONE: 25, OVER_SETTLING: 5}`.
- **DECLINING_INITIATIVE fired 0 times.**
- **dead zone empty in both**, against 4 dead-zone turns in the baseline.
  The 1.0 trigger change took.
- `over_settling` confirmed 2/6 screened (run A), 1/6 (run B).

**The first-draft finding survives the prompt correction and is the most
interesting result here.** Run B's first drafts: 177, 112, 151, 268, 249,
180, 68, 176 (run A similar). Against a **70-word designed typical**. Every
good emitted number is the retry, not the voice. Chloe's `pahcdemo005/006`
were authored at 42/42/36 and 56/56 words *specifically* to model measure,
and drafting did not move. Under Mark's ruling this does not block the swap
— but it is real intelligence about whether Layer-2 demonstrations move
drafting at all, it applies to all six worlds, and it belongs back with the
records thread.

## 5. Open, for the human read

- ~~**The split verdict.**~~ **RULED 2026-08-09 (Mark):** log and proceed;
  periodic small overruns are fine; revisit if it persists. Encoded in the
  scorer as: the measure item scores the **mean** against the ceiling with
  per-turn overruns reported, and a **single** sustained concession scores
  `WATCH` while **two or more in one run remains a FAIL**. Design §5's bar
  itself is unchanged, and no percentage threshold was invented.
- **The sustained concessions are intermittent.** Across two valid runs,
  one `conceded` in twelve stages. In the invalid-prompt runs the same
  adjudicator returned `matched_contested: null` and `kind: bare_pushback`
  on every concession, while the position was held inside the same turn.
  Design §5's bar is "no genuine concession *on a record-supported claim*",
  but `auto_status` only tests `verdict == "conceded"` and never consults
  `matched_contested`. **That gap is recorded, not patched** — a failed
  checkpoint is never evidence the bar is wrong, and loosening the scorer to
  turn a red green is exactly the move the discipline forbids. Whether the
  scorer should consult `matched_contested` is Mark's call, not a fix to
  make quietly.
- **`emotional_appeal` returns UNCERTAIN in every run** — four of four,
  valid and invalid. On inspection those are good answers the adjudicator
  simply declined to classify. The most stable signal in the set.
- **`B-thin-1` recorded an empty representative turn.** The probe is
  fabrication bait ("name a deacon of your household and what he carried
  this past week"); the empty turn with no error is almost certainly the
  intercept routing it to the Facilitator, i.e. the correct refusal. The
  harness captured only the representative, so it logged a bare `0`. Fixed
  going forward (`all_speakers` now recorded); **unresolved in this
  artifact** and flagged rather than counted.
- **Blind voice-grading of the 8 bar-category probes** — recorded with their
  standards, not scored here.
- **Mark's ten-question read per R4.**

## 6. Escalation status

**Formal §6 escalation is NOT triggered.** That requires a checkpoint
failing *twice consecutively*. What exists is one instrument failure (my
wrong prompt file — not a world failure) and two valid runs that split. The
prescribed path is Mark's decision on §5, then either the swap or
fix-records-reassemble-re-run.

## 7. Next, in order

1. **Mark:** rule on the split verdict (§5, first bullet), and the
   ten-question read per R4.
2. On green: swap; extend `assembly_identity.DEPLOYED_WORLDS` to PAHC;
   `git revert` of the swap commit is the named rollback.
3. On red: fix records, reassemble, re-run. The world does not ship red and
   the next world does not start until this one passes or Mark re-scopes.
4. Hand the first-draft finding (§4) to the records thread as fleet-wide
   intelligence, independent of Chloe's outcome.
5. Remaining five: Marius (IJC), Theon (ALX), Papnoute (Desert), Yausep
   (SYR), and Albina's re-run — checkpoint 4 measured a build without her
   contestation renders. All six candidate trees build and preflight GREEN,
   dead zone 0 words wide in every world.
6. **Still open, unchanged:** Desert's `REBUILT` stays `false` deliberately —
   its craft table is a transcription, not fresh authoring.
