# Chloe (PAHC) — Phase 2 Checkpoint Record (2026-08-09)

First of the six checkpoints, per the handoff order. This document is the
running record for the checkpoint attempt itself; the records pass it sits
on top of is commit `ac0f6ea`.

**Status: candidate tree REBUILT, preflight GREEN, checkpoint NOT RUN —
blocked on the environment's egress policy, not on the API key.**

The two blockers named in the handoff have swapped places. The one that
was expected to stop this run is gone. A different one, not previously
seen, stops it instead.

---

## 1. The API key blocker is resolved — no new key is needed

The handoff carried this forward from Marius's checkpoint as the standing
blocker, with the suspicion that the agent proxy rather than the credential
was at fault, and the instruction not to spend a battery on a new key
before testing a minimal `ChatAnthropic` call.

Tested three ways, in one process, against the key this environment
supplies as `CIC_ANTHROPIC_KEY`:

| path | result |
|---|---|
| raw `anthropic` SDK | **OK** |
| bare `ChatAnthropic` (key passed explicitly) | **OK** |
| the app's own `app.graph.nodes.get_llm()` | **OK** |

`settings.anthropic_api_key` matched the environment variable exactly, and
`llm_provider`/`mock_llm` were at their real values (`anthropic`, `False`).
So the LangChain client is not the problem and the proxy is not the problem.

The proxy theory can also be ruled out directly: `anthropic.com`,
`.anthropic.com` and `*.anthropic.com` are all in the proxy's own `noProxy`
list, so Anthropic traffic never transits it. `ANTHROPIC_BASE_URL` is set in
this environment, but to plain `https://api.anthropic.com` — not a gateway.

The most likely reading of the earlier 401 is simply that the key that
session held was not this one. **Nothing further is needed here.**

**The run recipe** — the key is NOT in `ANTHROPIC_API_KEY`, which is the
only name `Settings` reads, so it must be passed across:

```
ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY" python scripts/<battery>.py
```

Per standing practice the key was not written to any file.

## 2. The new blocker: huggingface.co is denied by the egress policy

`app/rag/embeddings.py` builds every world's FAISS index from
`all-MiniLM-L6-v2`, downloaded from HuggingFace on first use. In this
session that download fails:

```
httpx.ProxyError: 403 Forbidden
  connect_rejected  huggingface.co:443
  connect_rejected  cdn-lfs.huggingface.co:443
  "gateway answered 403 to CONNECT (policy denial or upstream failure)"
```

`api.anthropic.com` and `pypi.org` are allowed from the same session, so
this is a per-host policy denial, not a broken proxy. A fresh container has
no model cache, and `vector_store/` is gitignored, so there is nothing local
to fall back to.

This blocks the battery completely, not partially. `TestClient(app)` runs
the startup lifespan, which builds every world's retrievers; no probe turn
can be sent at all.

**This was NOT worked around, deliberately.** The proxy's own guidance is to
report a policy denial rather than route around it. It is also the right
call on the merits here: the whole content of Chloe's Phase 2 pass — 13
rewritten term chunks, 13 story chunks — reaches the model *only* through
retrieval. A checkpoint run with retrieval stubbed would not be measuring
the thing that changed.

**What is needed from Mark:** allow `huggingface.co` and
`cdn-lfs.huggingface.co` in this environment's network policy (Claude Code
on the web → environment settings). One download then caches for the
session and unblocks all six checkpoints.

## 3. The scratchpad loss, and what was done about it

The handoff pointed to six built harnesses — `pahc_`, `ijc_`, `alx_`,
`des_`, `syr_checkpoint1.py`, `hal_checkpoint4.py` — each with a built
candidate tree and verified indices, all preflighted clean. **None of it
survived.** They lived in a session scratchpad, the container was reclaimed,
and nothing had been committed. The directory is empty.

This is the second time the Phase 2 work has lost a session boundary (the
first was the API key itself, at Marius's checkpoint). It is a build-process
defect, not an accident, and the fix is to stop keeping load-bearing
artifacts in the scratchpad.

`cic-poc/backend/scripts/checkpoint_candidate.py` is committed as the
durable replacement for the lost trees. It rebuilds any world's candidate
tree from committed material alone and runs the preflight assertions:

- **Candidate tree**: full copy of `data/` (so the other five worlds stay
  exactly as deployed) with one world's assembled prompt, generated capsule,
  and rewritten lexicon/story chunks overlaid from `wrs/views/staging/`.
  Selected at runtime via `DATA_BASE_PATH` / `VECTOR_STORE_BASE_PATH`.
  **`data/` is never written to.**
- **Preflight**: the same configuration facts the six lost harnesses
  asserted before their first API call.

Indices are rebuilt per tree rather than reused, for the reason Marius's
pass recorded: `app/rag/retriever.py` calls `load_index()` first and only
falls back on failure, so a stale index survives a records change silently.

Candidate trees are gitignored — they are always reproducible from `data/`
plus `staging/`, and are not a source of truth.

## 4. Chloe's preflight, green against the candidate tree

```
[cfg] data_base_path = .../candidates/pahc/data
[cfg] prompt words   = 1951
[cfg] capsule words  = 1702
[cfg] ceiling        = 150 (from voice_profile.native_measure)
[cfg] per-world guard export ACTIVE for post-apostolic-house-church
[cfg] retry trigger multiple = 1.0
[cfg] enforced threshold = 150w (dead zone 0w wide)
[cfg] PREFLIGHT GREEN
```

The dead zone is the one to read. Chloe's ceiling was set as an **enforcing**
one, deliberately, and had never fired once: at 1.5 the retry sat at 225
against a baseline max of 223, so all six over-ceiling turns were dead-zone.
At 1.0 the enforced threshold sits on the ceiling itself and the dead zone
is **0 words wide**. That is the change the checkpoint exists to test.

Both gates re-verified independently in this session (neither needs the
embedding model):

- **Leak gate** (`--data-dir wrs/views/staging`): `HARD-FAIL: 0` —
  **GATE PASSED**, no hard-fail apparatus in any serialized chunk body.
  51 report-only, 33 files, non-blocking.
- **Assembly identity**: all six worlds PASS, with Desert (−240 words) and
  Albina (+663 words) correctly reported as PENDING RE-CHECKPOINT.

## 5. What the checkpoint still has to decide

Nothing about Chloe's voice has been measured. Everything above is
derivation, construction, and configuration. The numbers to beat, from
`pahcvoice001.native_measure`:

| | designed | streaming re-baseline (2026-08-08) |
|---|---|---|
| typical | 70 | mean **179** |
| ceiling | 150 | max **223**, 6 of 8 turns over ceiling |

Per-turn, the baseline climbs through the run — 148, 167, 135, 172, 156,
**216, 215, 223** — so the last three turns are roughly three times measure.
This is the widest designed-to-observed gap in the fleet.

**How to read the result**, carried from the handoff:

1. **The measure is the headline.** A good mean with a bad tail is still a
   fail — the defect is the climb, not the average.
2. **Ceiling fires should be non-zero for the first time.** If they are
   zero, the enforcement change did not take, and that is the finding
   regardless of what the mean says.
3. **Verdicts come from the `challenge_adjudicated` event** in `EVENT_STORE`
   — *not* from `run_repair_intercept()`, which returns `None` on every stage
   and reports zero concessions *and* zero holds. This is one of the two
   harness bugs already found and fixed at Albina's checkpoints; the other is
   that the sustained retry helper must call `sdb._stream_turn`, not the
   probe module's same-named function with a different return shape.

## 6. The battery a rebuilt harness has to compose

Recorded so the next session rebuilds rather than rediscovers. Both halves
are committed instruments; the lost harnesses wired them together and
captured the loggers.

- **Probe half** — `scripts/voice_rebuild_research_probe.py`: eight turns per
  world, all six worlds defined, plus `analyze_turn()`, which already emits
  exactly the `turn_analyses` fields the artifact carries. Note it runs at
  import (no `main()`), so it is copied from rather than imported.
- **Sustained half** — `scripts/sustained_disagreement_battery.py`: PAHC's
  case is `pahcclaim003`, setup plus six escalation stages, and it already
  reads verdicts from `challenge_adjudicated` correctly. It also carries a
  `_NetworkFreeCrossEncoder` stand-in — prior evidence that the cross-encoder
  download was hit before; the *embedding* model has no such stand-in.
- **Loggers to capture**: `cic.length_ceiling` (world_id, ceiling,
  trigger_multiple, first_draft_words, outcome ∈
  `under_ceiling`/`dead_zone`/`retried`, retry_words, request_id,
  session_id), `cic.over_settling_decision`, `cic.drift_signal`.
- **Artifact schema** — as in
  `Ministry/Technology/Pass2/batteries/hal_phase2_checkpoint4_full_2026-08-08.json`:
  `{world_id, checkpoint, candidate, probe:{turn_analyses, transcript,
  errors, over_settling, length_ceiling, length_ceiling_records,
  drift_records}, sustained:{claim_id, turns, conceded_stages,
  uncertain_stages, auto_status, words_mean, words_max, over_ceiling,
  words_<rep>_mean, words_<rep>_max, over_ceiling_<rep>, drift_records}}`.

## 7. Next, in order

1. **Mark:** allow `huggingface.co` + `cdn-lfs.huggingface.co` in the
   environment's network policy. Everything else below is blocked on it.
2. Rebuild the checkpoint harness per §6 and run Chloe's checkpoint
   (probe + sustained halves) against the candidate tree from
   `scripts/checkpoint_candidate.py --world pahc`.
3. Mark's ten-question read per R4.
4. Swap on green; extend `assembly_identity.DEPLOYED_WORLDS` to PAHC.
5. Remaining five checkpoints: Marius (IJC), Theon (Alexandria), Papnoute
   (Desert), Yausep (Syriac), and Albina's re-run (checkpoint 4 measured a
   build without her contestation renders).
6. **Still open for Mark's call, unchanged:** Desert's `REBUILT` stays
   `false` deliberately — its craft table is a transcription, not fresh
   authoring.
