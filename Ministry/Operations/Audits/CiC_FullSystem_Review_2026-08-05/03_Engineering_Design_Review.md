# Engineering & Design Review — Would an Engineer Recognize This as Well-Built?

Opus review pass, 2026-08-05, following `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`:
source-level verification (every claim below was checked by opening the actual file and, where
possible, running the actual code — never inferred from a filename or a docstring), the fixed
P0/P1/P2 severity vocabulary, and a plain bottom-line verdict at the end. The reading was done
directly; no sub-agents were dispatched (per the note at the bottom of
`Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/00_INDEX.md`).

**Angle:** architecture, code quality, testing/eval discipline, efficiency, and `atlas-v3.html`
on its own terms. Not conversation quality, not historical rigor, not accessibility — those are
docs 01, 02, and 04 of this series.

---

## 1. What I read, and what I deliberately did not

### Read in full, line by line

| File | Lines | Notes |
|---|---|---|
| `cic-website/atlas-v3.html` | 1,601 | Whole file, CSS + JS + markup |
| `cic-poc/backend/app/main.py` | 2,008 | Whole file |
| `cic-poc/backend/app/graph/events.py` | 391 | The new event-sourcing core |
| `cic-poc/backend/app/graph/governance.py` | 377 | The new shared governance layer |
| `cic-poc/backend/app/graph/builder.py` | 120 | |
| `cic-poc/backend/app/rag/pipeline.py` | 201 | |
| `cic-poc/backend/app/rag/retriever.py` | 241 | |
| `cic-poc/backend/app/rag/hybrid.py` | 221 | |
| `cic-poc/backend/app/rag/cross_encoder.py` | 94 | |
| `cic-poc/backend/app/{config,auth,session_auth,session_cap,message_cap,usage_logging,transcript_logging,answer_bank,giving,mock_llm}.py` | ~800 total | All read in full |
| `cic-poc/backend/app/agents/{facilitator,representative}.py` | 44 | |
| `cic-poc/backend/retrieval_eval/run_eval.py` | 263 | |
| `cic-poc/backend/app/graph/replay/parity_suite.py` | 205 | + `recorder.py` header |
| `cic-poc/backend/scripts/s43_adjudicator_battery.py` | 171 | |
| `cic-poc/backend/scripts/s56_freeze_battery.py` | 357 | |
| `cic-poc/backend/scripts/cost_baseline_runner.py` | first 200 of 627 | Enough to judge the method |
| `Ministry/Features/Atlas-World-Map/Design/tools/{shoot.mjs,validate-census.mjs}` | 218 | |
| `cic-poc/frontend/src/hooks/useConversation.ts` | 391 | |
| `cic-poc/Dockerfile`, `render.yaml`, `requirements.txt`, `pyproject.toml`, `.env.example`, `.gitignore`, `supabase_schema.sql` (partial) | — | |
| `cic-poc/docs/langgraph-architecture.md` | 161 | |

### Prior audits read first (per practice item 4)

`02_Codebase_Mining.md`, `15_Retrieval_Architecture_Best_Practices.md`,
`16_MultiParty_Dialogue_Architecture.md` (through §6b), plus the Atlas
`Decision-Log.md` orientation set (`HANDOFF_2026-08-03.md`,
`CiC_Atlas_V3_Build_Blueprint_V1_0.md`, the increment table and Loop Protocol).

### Verified by execution, not by reading

- Ran `node Design/tools/validate-census.mjs` → 257 movements, 21 edges, 10 eras, **0 errors / 0
  warnings**. It passes today.
- Ran Playwright against `atlas-v3.html` at 390px and 1280px: 257 nodes render, **zero JS
  errors**, **zero node-vs-node overlaps**, and **zero node-vs-foreign-tail overlaps** (I wrote
  the box-vs-tail check the harness doesn't have — see P1-8). The packer works.
- Measured a full `layout()` relayout at **308ms desktop / 392ms mobile**.
- Reproduced the theme-toggle filter bug empirically (P0-3): with a lane filter active, one theme
  click takes visible nodes from 76 → **0**.
- Confirmed Playwright's viewport emulation *does* set `screen.width`, so `shoot.mjs`'s 390px run
  genuinely exercises the `is-mobile` branch. My initial suspicion that it didn't was wrong, and
  I'm recording that rather than quietly dropping it.

### Deliberately not read

- **`app/graph/nodes.py` in full (3,981 lines).** I read ~600 lines targeted at specific claims
  (`build_public_transcript`, the lane-ceiling block, `signal_rank`, the `_migrated_world_ids`
  call sites) and relied on doc 02 + doc 16 for the rest. **This is the largest coverage gap in
  this review.** A file that has grown 42% since the last full read (2,797 → 3,981) is exactly
  where an unreviewed defect would live. Anything I say about nodes.py internals is second-hand
  unless I name the line.
- **`app/prompts/*` (1,035 lines)** — prompt content is docs 01/02/04's territory, not
  engineering.
- **`app/graph/{modern_term_bridge, epistemology_bridge, closing_sequence, repair_classifier,
  world_sources}.py`** — skimmed for structure and call signatures only.
- **`wrs/` (records, schema, views, migrate, gates)** — ~1,300 files. I read `parameters.yaml`'s
  head and the directory shape. The data-repository layer is doc 02's angle.
- **The frontend components** — surveyed structure and read `useConversation.ts` in full;
  did not read `TheTable.tsx` (417 lines) or the other components line by line.
- **Most of `scripts/`** — read 3 in full, sampled 6 more structurally, and measured duplication
  mechanically across all 43.
- **The 5,686-line Atlas `Decision-Log.md`** — I read the orientation documents and the Loop
  Protocol, not all 346KB. My judgment of `atlas-v3.html` rests on the code itself plus the
  ~200 lines of in-file commentary that carry the same history.
- I did **not** send any request to the live deployment at `cic-poc.onrender.com`. P0-1 is
  therefore verified by code and deployment-config reading, not by exploitation.

---

## 2. Genuine engineering strengths, named specifically

I went looking for reasons to discount the prior audits' praise. Most of it held. These are the
things I'd defend to a skeptical senior engineer.

### 2.1 The comments are the best technical documentation in the project — and they are load-bearing

This is unusual enough to name first. Across the backend and `atlas-v3.html`, the dominant
comment style is not "what this does" but **"what we tried, what broke, what the measurement
said, and why the current shape is the one that survived."** Examples I verified:

- `usage_logging.py:95-109` records a real bug the module itself found — streamed calls silently
  logging `cache_read` as 0 under the wrong metadata key — names the diagnostic script that
  proved it, and explains why the fallback is a fallback and not a replacement.
- `hybrid.py:108-119` explains why the BM25 corpus deliberately *excludes* the Related line
  ("every term name appearing in many docs' Related lists flattens that name's idf to nothing —
  measured on 'What is theosis?'"). That is a negative result preserved in code.
- `hybrid.py:47-53` sets `MMR_LAMBDA = 0.85`, "not the textbook 0.7," and names the exact case
  that forced it (`HAL-RT-01`, vulgata vs hebraica-veritas).
- `cross_encoder.py:26-38` gives the actual score distributions behind `RELEVANCE_THRESHOLD =
  -4.0` (must-docs ≥ 1.2, noise median -10.7) *and* honestly records the regime where no
  threshold separates.
- `atlas-v3.html:35-54` documents a two-round fix to a dark-mode contrast problem, including the
  round-one failure ("passed a strict luminance check but pixel-sampled a real box on mobile and
  it rendered as a single, barely-there transition pixel").
- `atlas-v3.html:771-806` (`MAP_ZOOM`) records six failed rounds and then correctly diagnoses
  the root cause as a web-platform limitation rather than a bug in this page — and rebuilds
  scoped to eliminate the whole class structurally.

Most codebases record what the code does. This one records **what was tried and failed**, which
is the expensive half and the half that prevents a maintainer from re-running a dead end. It is
also what made this review possible at the depth it reached.

### 2.2 `retrieval_eval/run_eval.py` — a deterministic, zero-API-cost retrieval harness that brackets its own non-determinism

`retrieval_eval/run_eval.py:1-38` and `:117-133`. This is the single most sophisticated piece of
evaluation design in the repo. It evaluates retrieval by **stable chunk ID**, with no judge
model and no API cost, over 105 hand-authored golden cases across six worlds in six named
categories (`verbatim-term`, `thematic`, `de-dup`, `negative-condition`, `reactive-turn`,
`cross-world-isolation`). Where one pipeline stage is genuinely non-deterministic (the retained
LLM guard vote), it does not fudge it — it runs **two fixed policies** (`vote=retrieve`,
`vote=skip`) and reports both, then makes the explicit observation that "the bracket width itself
is a measurement: it is exactly how much of today's retrieval outcome hangs on the LLM vote R6
replaces." That is a genuinely clever instrument, and it converted a subjective argument into a
falsifiable number. It also asserts cross-world isolation **structurally** on every case (line
169) rather than trusting the per-world index invariant.

### 2.3 Doc 15's recommendations were actually implemented — with the audit's own identifiers as code comments

This is the strongest signal in the whole review that the review process here is real rather than
ceremonial. Doc 15 (2026-07-25) issued R0–R10. Verified in code today:

| Rec | Status | Evidence |
|---|---|---|
| R0 ID-based eval harness | **Done** | `retrieval_eval/` |
| R1 embed the retrieval surface, body as payload | **Done** | `retriever.py:195-198` (`page_content` is the surface; body in `metadata["content"]`) |
| R3 BM25 + weighted RRF | **Done** | `hybrid.py:27-29`, `:153-165` |
| R4 ID-keyed session exclusion + MMR | **Done** | `pipeline.py:90-105`; `hybrid.py:193-221` |
| R5 relevance floor; em-dash sentinel | **Done** | `hybrid.py:45-46, 142-145`; `batch_evaluate._evaluable_negative_condition` |
| R6 local cross-encoder replaces the batched LLM vote | **Done** | `cross_encoder.py`; `pipeline.py:107-151` |
| R7 Quick Meaning into the cached prefix | **Done** | `retriever.py:205-226` |
| R8 one-hop `Related-Terms` traversal | **Done** | `hybrid.py:167-179` |
| R9 conversational query rewrite replaces string concat | **Done** | `rag/query_rewrite.py`; `cross_encoder.py:40-44` |

Doc 16's findings landed too: its finding 6 (the `pending_guidance` last-writer-wins bottleneck
that "structurally deprioritizes exactly the multi-party table signals") is now a real priority
queue behind one gate — `governance.queue_guidance` (`governance.py:197-220`), with the
projection folding through the *same* function (`events.py:220-224`) so the live writer and the
replay path cannot diverge. Its finding 1e (Facilitator turns excluded from the Representatives'
shared record, "the highest-severity grounding gap found") is fixed and the fix is documented at
`nodes.py:894-905`. Its finding 1f (the naive 10-line sliding window) is now block truncation
with a stable prefix (`nodes.py:878-880, 932-937`). Its §5b (event sourcing) is
`app/graph/events.py`.

An audit whose recommendations get implemented, by identifier, within days, is rare. Credit where
it's due.

### 2.4 The replay-parity harness (`app/graph/replay/`)

`parity_suite.py` + `recorder.py`. To prove that extracting `governance.py` out of the two
endpoint bodies was behavior-preserving, they built a record/replay rig that **tapes every
LLM-dependent boundary function in call order**, records real API outputs before the refactor,
replays them after, and asserts both the outcome snapshot *and* the call order (a tape underrun
or label mismatch is a loud failure). Eight cases covering both endpoints, all four intercepts
actually firing, and multi-world selection. The **one** intended behavior delta is *declared* in
code (`parity_suite.py:169-177`) rather than tolerated silently. 32 committed fixture files.

The recorder docstring even explains why `mock_llm` is the *wrong* tool for this specific proof:
"mock_llm's placeholder text deliberately omits every format marker, so under mock_llm every
classifier takes its no-fire default and ordering is unobservable, not proven (its own docstring
says so)." That is a level of self-awareness about your own test double that most production
teams never reach.

### 2.5 The freeze batteries have a real train/test split and blind grading

`s56_freeze_battery.py:118-238`. Trial A is resampled from **development** probes; Trial B is
**held-out novel** probes authored fresh and never used in that world's development. Every probe
runs in a fresh session against the **real system** through `TestClient(app.main)` — full
intercept chain, real retrieval, real event log — not against a mock. Output is a **masked**
file (seeded shuffle, IDs hidden, expected column withheld, but the category standard shown) plus
a **sealed key** with the mechanical evidence (who spoke, safety/repair/bridge events, parroting
scores) so routing facts are applied *after* blind voice grading. That is held-out evaluation
with blinding and a pre-registered rubric. It is better methodology than most ML teams ship.

### 2.6 `session_auth.py` — the best-reasoned 80 lines in the repo

`session_auth.py:1-81`. It states the gap ("a session_id is a UUID, and a UUID leaks: a shared
link, a Referer header, a log line, a screenshot"), explains why the obvious fix (identity)
cannot work given the project's own optional-sign-in commitment, chooses possession-based auth
with a named justification, uses `secrets.compare_digest` with the timing rationale stated, and
**names its own deliberate non-application** (`/audit`) with the reason applying it there would
break the endpoint's purpose. It even bounds its own fail-open (pre-token sessions) and says why.
This is what a security decision record should look like.

### 2.7 Real single-source-of-truth discipline where it counts

`world_manifest.py:1-19` names the five places world metadata used to be hand-synced and collapses
three of them, then **honestly declares the two it cannot reach** (the frontend's TypeScript
union and its rep-info dict). `atlas-v3.html:556-557` replaced a hand-maintained 11-pair
succession array with a live derivation from the census's own `continuesAs` field, and the comment
records that the stale array had been "silently missing 60 of the 71 real pairs on record."
`atlas-v3.html:1166-1180` generates the page glossary *from* the `CATS`/`REGIONS` arrays so it
cannot drift. `pipeline.py:1-18` names duplication explicitly as "not a tidiness problem, a
correctness problem with a track record" and gives the track record.

### 2.8 The census validator earns its place in the loop

`validate-census.mjs` is a genuine contract validator, not a schema stub: it checks edge-endpoint
integrity, edge type and confidence against a closed vocabulary, `continuesAs` same-or-adjacent-era,
`start ≤ end`, `Built & Live` implies an `entry` block, and — the good one — **`meta` counter
consistency against the actual arrays** (lines 63-77), with an inline note that this caught a
stale count at the Era 5 survey. It exits non-zero. It passes today with 0/0.

### 2.9 42 labeled, instrumented LLM call sites

Every real model call in the backend logs `label`, `model`, `request_id`, `session_id`,
input/output/cache-creation/cache-read tokens. `cost_baseline_runner.py` then attaches a handler
to that logger and produces a deterministic, cache-aware cost report with per-turn attribution,
including `pause_before_s` steps that deliberately observe the 5-minute cache TTL. Most teams
discover their inference bill from the invoice. This project can attribute it to the call site.

---

## 3. Findings

### P0 — must fix

---

#### P0-1. Arbitrary file read on the production deployment via the SPA catch-all route

**Where:** `cic-poc/backend/app/main.py:1994-2002`

```python
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    candidate = _FRONTEND_DIST / full_path
    if full_path and candidate.is_file():
        return FileResponse(candidate)
    return FileResponse(_FRONTEND_DIST / "index.html")
```

**The problem.** `full_path` is attacker-controlled and is joined to a base directory with no
containment check. Two independent exploit shapes:

1. **Absolute path.** `Path("/frontend/dist") / "/etc/passwd"` evaluates to `PosixPath('/etc/passwd')`
   — `pathlib` discards the left operand when the right is absolute. Starlette's route regex for
   `/{full_path:path}` is `^/(?P<full_path>.*)$`, so a request for `//etc/passwd` yields
   `full_path = "/etc/passwd"`. No `..` traversal and no percent-encoding is required, so nothing
   an intermediate proxy normalizes will stop it.
2. **Traversal.** Starlette percent-decodes path params and does not normalize `..` segments;
   `is_file()` and `FileResponse` resolve them at the OS layer. `/%2e%2e/%2e%2e/proc/self/environ`
   reaches `/proc/self/environ`.

**Why this is P0 and not theoretical.** `cic-poc/Dockerfile` builds `frontend/dist` in stage 1
and copies it to `/frontend/dist` in the runtime image, so `_FRONTEND_DIST.is_dir()` is **true in
production** and this route is live. The container runs as root with no `USER` directive.
`/proc/self/environ` in that container holds `ANTHROPIC_API_KEY`, and — once configured —
`SUPABASE_SERVICE_KEY` (the service-role key, explicitly documented in `.env.example` as the one
that must stay server-side) and `STRIPE_SECRET_KEY`. Also readable: every `transcripts/events/*.jsonl`
conversation log, and the whole `data/` corpus.

Note the contrast one line above: the `/assets` mount at line 1992 uses Starlette's `StaticFiles`,
which **does** implement traversal containment. The framework-provided path is safe; the
hand-rolled one beside it is not.

**Confidence.** High on the code path and the deployment configuration (both read directly).
I did not send a request to the live host, so the end-to-end exploit is unconfirmed by execution.
Confirm with one `curl` before and after the fix.

**Fix.** Resolve and contain, and never serve outside the root:

```python
BASE = _FRONTEND_DIST.resolve()

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    if full_path:
        candidate = (BASE / full_path).resolve()
        if candidate.is_file() and candidate.is_relative_to(BASE):
            return FileResponse(candidate)
    return FileResponse(BASE / "index.html")
```

`Path.is_relative_to` is 3.9+; the project requires 3.11. Add a regression case to the parity
suite (`GET //etc/passwd` → 200 with `index.html`, not `root:x:0:0`).

---

#### P0-2. The per-user session cap has never been able to fire, and its own docstring asserts a caller that does not exist

**Where:** `cic-poc/backend/app/session_cap.py:32-53`, against `main.py:330-455` and
`transcript_logging.py:60-75`.

**The problem.** `check_and_reserve_session_slot` counts rows in the Supabase `sessions` table:

```python
count_response = client.table("sessions").select("id", count="exact").eq("user_id", user.user_id).execute()
```

Its docstring states the reservation is implicit because "the caller inserts a new row into
`sessions` immediately after this returns True." **That caller does not exist.** I read
`start_session` in full: after the cap check it mints a session token and appends to
`EVENT_STORE`. It never touches the `sessions` table.

A repo-wide grep finds exactly two references to that table: the count in `session_cap.py:48`, and
an upsert in `transcript_logging.py:66` — which is gated on `settings.pilot_logging_enabled and
supabase_configured()`. `pilot_logging_enabled` defaults to `False`, and `.env.example:33-36`
explicitly instructs against enabling it for a general/public deployment.

So on the intended public configuration (Supabase on, pilot logging off), the count is
permanently 0 and **the session cap can never fire for anyone, including a signed-in user.** Even
with pilot logging on, the row is written per *round*, not at session start, so a session that is
created and abandoned never counts — the cap is a lagging approximation of a metric it claims to
reserve against.

The module's docstring already concedes the cap "only actually bites for a participant who chose
to sign in." What it does not say — and what is true — is that it does not bite then either.
This is the exact class of defect this project's review practice exists to catch: a docstring that
sounds right and does not survive being checked against the code it names.

**Fix.** Insert the row where the docstring says it is inserted — in `start_session`, right after
the cap check, unconditionally when Supabase is configured (independent of `pilot_logging_enabled`,
because session *counting* is not transcript *capture* and conflating them is what caused this):

```python
if supabase_configured() and user.user_id is not None:
    try:
        _get_client().table("sessions").insert({
            "id": session_id, "user_id": user.user_id,
            "world_ids": world_ids, "phase": state.phase, "turn_count": 0,
        }).execute()
    except Exception:
        logger.exception("session row insert failed for %s", session_id)
```

Then correct `transcript_logging.py`'s upsert to be an update of that row, and fix
`session_cap.py`'s docstring to describe what actually happens.

---

#### P0-3. `atlas-v3.html`: toggling the theme with any filter active blanks the entire map

**Where:** `cic-website/atlas-v3.html:1592-1596`

```js
tb.addEventListener('click',()=>{ti=(ti+1)%3;const t=themes[ti];
  ...
  tb.textContent="theme: "+t;layout();});
```

**The problem.** `layout()` removes and re-creates every `.node` element (line 611, 767). The
filter systems mark *elements* with `.lane-on` / `.region-on` / `.match` classes while marking
*body* with `.lanefiltering` / `.regionfiltering` / `.filtering`. Fresh nodes have none of the
element classes; body keeps its class. CSS at lines 104, 123, and 341 then reads:

```css
body.lanefiltering .node:not(.lane-on){opacity:.13}
```

…and drives **every node on the page to 13% opacity**. The `resize` handler gets this right —
line 1213 calls `layout(); applyLaneToggle(); applyRegionToggle(); applyFilter();` — the theme
handler calls only `layout()`.

**Verified empirically**, both viewports, with Playwright: open the filter panel, click the
"Catholic" category button (76 nodes visible), click the theme button → **0 nodes visible**,
`document.body.className` still `lanefiltering`. On mobile it compounds: `layout()` also calls
`initMobileMapZoom` (line 769), which resets `mapScale` to minimum and `scrollTop` to 0, so the
participant loses their zoom and position at the same moment the map appears to empty.

This is a participant-facing regression on the one participant-facing page in this repo outside
`cic-poc/frontend`, on a page whose Decision-Log documents dozens of rounds of exactly this class
of bug. It is a P0 because it is trivially reachable (two clicks) and looks like total failure.

**Fix.** One line:

```js
tb.textContent="theme: "+t;layout();applyLaneToggle();applyRegionToggle();applyFilter();
```

Better: extract `function relayout(){layout();applyLaneToggle();applyRegionToggle();applyFilter();}`
and make it the only thing anything ever calls, so a third call site cannot reintroduce this.
Add a `shoot.mjs` case: set a filter, toggle theme, assert `.node.lane-on` count is unchanged.

---

#### P0-4. `docs/langgraph-architecture.md` — the only architecture document in the codebase — is wrong in nearly every particular

**Where:** `cic-poc/docs/langgraph-architecture.md` (whole file), against `app/graph/builder.py`
and `app/main.py`.

**The problem.** Checked claim by claim:

| The doc says | The code does |
|---|---|
| `WAIT → representative_engages → facilitator_monitors → {reroot, wait, close}` loop (lines 35-44) | The graph is invoked **once**, at `main.py:402`, running `facilitator_receives → facilitator_handoff → END`. Neither message endpoint ever calls `graph.invoke()`. The real orchestration is hand-wired in `main.py`'s two endpoint bodies plus `governance.py`. |
| "Introduce Mar Yausep" (lines 16, 66, 80) | Six worlds and six representatives (`world_manifest.py`) |
| Seven drift signals (lines 84-101) | 17+ emitted types (doc 16 §5c counted 17 in July; `governance.run_table_checks` has since added `manufactured_resolution`, `misattribution`, `closing_synthesis`, and the repair intercept) |
| "Anachronism — Speaking beyond 410 CE" (line 96) | A Syriac-specific boundary presented as the universal rule; the bridge derives boundaries per world from `origin_year` vs the world's parsed end-year |
| `ConversationState` with 11 fields (lines 106-120) | 39 declared fields (`state.py`), including the entire relational-safety block, `closing_stage`, `pending_guidance`, `surfaced_chunk_ids`, `private_directive`, `register_note`, `session_token` |
| RAG: `similarity_search` → **loop: LLM evaluates each candidate** → context (lines 139-161) | BM25+dense weighted RRF → one-hop related-terms expansion → adaptive dense floor → MMR → **local CPU cross-encoder** → one Haiku call only for evaluable guards. The per-candidate LLM loop is **two generations obsolete** (batched in July, deleted at S3.4). |
| — | No mention at all of the event log, the governance layer, the five-intercept chain, the repair classifier, the answer bank, the repository endpoints, or the two-endpoint split |

`builder.py`'s own 40-line ASCII docstring diagram (lines 22-59) describes the same
never-executed loop, and line 12 imports `route_after_input`, which the function body never uses.

**Why P0.** The task asks what a new engineer would immediately flag. This is it. The single
document titled "Architecture" would give a new engineer an actively false mental model of the
control flow, the state, the drift taxonomy, the world count, and the retrieval stack. Doc 02
established the graph-is-vestigial fact on 2026-07-25; the document has not been touched since.
The in-code comments are excellent (§2.1) but there is **no map** — and a wrong map is worse than
none.

**Fix.** Cheapest honest option, today: replace the file with a one-page truth — "the LangGraph
graph runs once at session start and is otherwise vestigial; live conversation is orchestrated by
`main.py`'s two endpoints through `app/graph/governance.py`" — plus a module map
(`events.py` = state, `governance.py` = intercepts + table checks, `nodes.py` = generation +
signals, `rag/pipeline.py` = the one retrieval path) and a pointer to the prompt files. Then
either delete `builder.py`'s docstring diagram or annotate it as historical. Bigger fix
(P1-scale): decide whether the graph should be deleted or actually used — carrying a
never-executed `StateGraph` plus a false diagram is a permanent tax.

---

### P1 — materially improves

---

#### P1-1. `_validate_redirect_url` is a prefix match and does not bound the host

**Where:** `main.py:620-630`

```python
_ALLOWED_REDIRECT_PREFIXES = ("https://churchinconversation.com", ..., "http://localhost", ...)

def _validate_redirect_url(url: str) -> None:
    if not url.startswith(_ALLOWED_REDIRECT_PREFIXES):
        raise HTTPException(status_code=400, detail="Invalid redirect URL.")
```

`https://churchinconversation.com.attacker.example/steal` starts with
`https://churchinconversation.com` and passes. So does `http://localhost.attacker.example`.
The comment directly above correctly identifies the threat ("a real, working Stripe Checkout
Session that redirects a paying participant's browser wherever an attacker's request asked") and
the check does not close it.

**Fix.** Parse and compare hosts exactly:

```python
from urllib.parse import urlparse
_ALLOWED_HOSTS = {"churchinconversation.com", "www.churchinconversation.com",
                  "churchinconversation.org", "localhost", "127.0.0.1"}

def _validate_redirect_url(url: str) -> None:
    u = urlparse(url)
    if u.scheme not in ("https", "http") or u.hostname not in _ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail="Invalid redirect URL.")
```

---

#### P1-2. `wrs/parameters.yaml` — the "canonical parameters file" — is not in the production image, so its one runtime consumer silently falls back

**Where:** `main.py:57-77` and `cic-poc/Dockerfile`

`_multi_world_turn_floor()` reads `Path(__file__).resolve().parents[1] / "wrs" / "parameters.yaml"`
→ `/app/wrs/parameters.yaml` in the container. The Dockerfile copies **only**
`backend/wrs/glosses/` (line: `COPY backend/wrs/glosses/ ./wrs/glosses/`), with a comment
explaining that "the rest of `wrs/` … is dev/build-time only and deliberately not copied — this is
the one file under it that's now a genuine runtime dependency." That comment was true when
written and is now false: `parameters.yaml` became a second runtime dependency at S4.4a.

The function's `except Exception: return 2` fail-open means production silently runs the hardcoded
historical value. Behaviour is identical **today** because the file also says 2 — so nothing is
broken. But the F9 wiring that the parameters file exists to provide does not exist in
production: change `turn_floor_multi_world` to 3, deploy, and production keeps 2, with no error,
no log line, and no way to notice.

Secondary: `import yaml` at line 69, but **PyYAML is not in `requirements.txt`**. It works only as
a transitive dependency of langchain.

**Fix.** `COPY backend/wrs/parameters.yaml ./wrs/parameters.yaml` in the Dockerfile; add `PyYAML`
to `requirements.txt`; and change the bare `except Exception` to log at WARNING before falling
back, so a missing canonical parameter file is visible instead of invisible.

---

#### P1-3. No CI. Every harness this project built is opt-in and manual.

**Where:** repo root — no `.github/workflows/`, no `Makefile`, no `.pre-commit-config.yaml`, no
`ruff`/`flake8`/`setup.cfg`, and `cic-poc/frontend` has an eslint **script** with **no eslint
config file** (so `npm run lint` cannot do what it claims).

This project has built, at real cost: a census contract validator that exits non-zero, a
deterministic zero-API retrieval harness with 105 golden cases, a record/replay parity suite with
32 committed fixtures, a Playwright geometric/interaction harness, and a cost-baseline runner.
**None of them run automatically.** Every one depends on a human remembering, in the right order,
per the Loop Protocol.

Three consequences already visible in this review: P0-3 (a two-click participant-facing regression
`shoot.mjs` could have caught with one assertion), P1-6 (rubric drift across six copies), and
`builder.py:12`'s dead import (any Python linter would flag it in a second).

`retrieval_eval/` also has **no committed `baseline.json`**, which doc 15's R0 named explicitly
("`baseline.json` — committed; every change diffs against it"). The harness therefore measures but
does not gate: there is nothing for a change to regress *against*.

**Fix, in order of value per hour:**
1. One GitHub Actions workflow that runs `node validate-census.mjs` and `npm run build` (tsc) on
   every push. Both are fast, hermetic, and need no secrets. This alone would have caught the
   dead import and any census/type break.
2. Commit `retrieval_eval/baseline.json` and add a `--check baseline.json` mode to `run_eval.py`
   that exits non-zero on regression. Zero API cost, so it can run in CI — but it does need the
   two sentence-transformer models, so cache them or accept a slow job.
3. Add an eslint flat config to the frontend and turn on `react-hooks/exhaustive-deps` (which
   would flag P2-6).
4. Add `ruff` with a minimal ruleset (F401 unused imports, F841 unused locals) to the backend.
5. Run `shoot.mjs` in CI on every `cic-website/**` change.

---

#### P1-4. The event log grows without bound in a 512MB container that already has an OOM history

**Where:** `app/graph/events.py:280, 287-300, 338-340`; `render.yaml` (`plan: starter`)

`EventStore._events` is a `dict[str, list[Event]]` that is only ever appended to. `clear()` is
called exactly once, in `main.py`'s `lifespan` teardown. There is no TTL, no LRU, no per-session
cap, and no eviction of a finished session. Every session started in a process's lifetime keeps
its full message text, retrieval-audit blobs, and classifier payloads resident.

`render.yaml` selects the 512MB `starter` plan, and its own comment records a prior status-137
OOM. The runtime now loads **two** transformer models on that instance — `all-MiniLM-L6-v2` for
embeddings and `cross-encoder/ms-marco-MiniLM-L-6-v2` (added at S3.4, after the plan choice) —
both on top of torch. `CONVERSATION_TURN_CAP_TABLE = 100` allows a single table session to
accumulate several hundred events with multi-kilobyte payloads.

**Related, and worth naming honestly:** `main.py:1653-1658` says the audit endpoint "survives a
process restart instead of dying with the in-memory dict." That is true for a *process* restart
within a container. It is **not** true for a redeploy or instance replacement: `render.yaml`
declares no persistent disk, so `transcripts/events/*.jsonl` lives on an ephemeral filesystem, and
the Supabase mirror (`events.py:373-387`) is gated on `pilot_logging_enabled`. In the intended
public configuration, the entire durable audit trail is lost on every deploy.

**Fix.** (a) Evict from `_events` on session close, or bound the store (LRU by last-touch, e.g.
200 sessions) and re-hydrate from JSONL on miss — `_read_jsonl` already exists and `has()` already
falls back to it, so the machinery is there. (b) Measure real RSS under a three-world table
before assuming `starter` still fits with two models loaded. (c) Either attach a Render disk or
un-gate the Supabase event mirror from `pilot_logging_enabled` — those two flags answer different
questions, same conflation as P0-2.

---

#### P1-5. `retrieval_eval/run_eval.py` re-implements the pipeline it is supposed to be testing

**Where:** `retrieval_eval/run_eval.py:65-133` (`replay()`) against `app/rag/pipeline.py:81-196`

The harness's docstring claims it "replays every deterministic stage by calling the REAL code."
It calls the real `candidate_search`, the real `score_candidates`, the real `threshold_for`, and
the real `_evaluable_negative_condition`. But the **decision loop** — session exclusion, the
cross-encoder sort, the rank-guard (`if s >= rel_threshold or rank < k`), the guard partition,
and the k-truncation — is a **second, parallel implementation** of `run_retrieval`.

Compare `run_eval.py:107-132` with `pipeline.py:127-196`: same logic, written twice. A change to
`pipeline.py`'s rank-guard or exclusion order would leave the harness green while production
changed. The harness would then be measuring a system that no longer exists.

This is precisely the failure class `pipeline.py`'s own docstring names, one file over: "That
duplication was not a tidiness problem, it was a correctness problem with a track record. The
adjudication-guard fix had to be written twice, in two files, in identical form… A maintainer who
fixed one and missed the other would have left adjudication half-guarded, and nothing would have
failed." The project diagnosed this correctly in the runtime and then reproduced it in the harness.

**Fix.** Have `replay()` call `run_retrieval` directly with `mode=TURN`, and obtain the two
bracket policies by injecting a stub `filter_llm` that returns all-RETRIEVE or all-SKIP. That
removes ~40 lines from the harness, makes the "measures the real pipeline" claim literally true,
and means a pipeline change cannot silently escape measurement.

**Also:** `run_eval.py`'s docstring lines 8-17 still describe the *pre-S3.2* pipeline
("FAISS similarity search (k*2 candidates) → partition_tier1_short_circuit → evaluate_batch")
while lines 89-96 describe the current one. It contradicts itself. Rewrite the head.

---

#### P1-6. Six copies of the freeze battery, and the grading rubric has already drifted between them

**Where:** `scripts/s56_freeze_battery.py`, `s62_{alx,hal,ijc,pahc,syr}_freeze_battery.py`
(357/371/416/419/534/386 lines)

Measured mechanically:
- `_stream_turn` is **byte-identical** across **ten** scripts (`diff` returns no output).
- The `STANDARDS` dict — **the grading rubric itself** — is copy-pasted in six, and the six copies
  have **diverged**: 64/72/90/80/127/78 lines, six different checksums.
- `s62_ijc` has a **different category key**: `fabrication-pressure` where the other five have
  `confidence-under-thinness`. That world's freeze battery grades a different set of ten
  categories from the other five.

Some divergence is legitimate — the pahc anachronism standard's "nearer-edge discipline" (the
rumor-of-Marcion class) is a genuinely better formulation than s56's, and world-specific closing
dates obviously must differ. That is exactly the problem: **there is no shared core standard with
declared per-world specialization; there are six independent rubrics, and no mechanism records
which differences are intentional.** Two consequences: (a) cross-world comparability of freeze
results is asserted but not established, and (b) the pahc improvement reaches one world out of
six, forever.

**Fix.** One `scripts/freeze_battery.py` taking `--world`, with `STANDARDS_CORE` plus a per-world
`STANDARDS_OVERRIDE` in a YAML file beside the probes — so a divergence is a *declared* delta
(exactly the discipline `parity_suite.py:169-177` already uses for its own behavior delta) rather
than an accident of copy-paste. Extract `_stream_turn` and the mask/key writer into a shared
`scripts/_battery.py`. This deletes roughly 1,500 lines and makes a rubric improvement propagate.

---

#### P1-7. `atlas-v3.html`: `layout()` is a ~350ms synchronous relayout bound to an unthrottled `resize`, and it destroys mobile zoom state

**Where:** `atlas-v3.html:1212-1214`, `:714-715`, `:769`, `:808-816`

Measured: 308ms desktop, 392ms mobile for one full `layout()`. The cost is dominated by
`tryPack`'s widening loop (line 715): `while(attempt.fb>0 && W<viewW*5){W+=60; attempt=tryPack(W);}`
— up to 26 full re-packs, each O(rows × slots log slots) with `endRowOf`→`lastRowStartingBy`
re-scanning all 257 rows per call.

That is bound to a bare `addEventListener('resize', ...)` with no debounce. On mobile, the browser
fires `resize` when the URL bar collapses or expands and on every orientation change; each one
costs ~400ms of main-thread jank **and** calls `initMobileMapZoom` (line 769), which resets
`mapScale` to the minimum and `scrollTop` to 0 — throwing away the participant's pinch-zoom and
position. On a page whose Decision-Log records six rounds of work to make that zoom feel right,
a URL-bar collapse silently undoes it.

**Fix.** Three cheap, independent steps:
1. Debounce the resize handler (150-250ms trailing).
2. Early-return from `layout()` when the packing inputs (`viewW`, `rh`, `head`) are unchanged —
   which makes the theme toggle (P0-3) free, since a theme change never needs a re-pack, only a
   re-color.
3. Preserve and restore `mapScale` / `scrollTop` / `scrollLeft` across `initMobileMapZoom`
   instead of resetting.
4. Memoize `lastRowStartingBy` (it is a pure function of `m.end` over a fixed `rows` array) —
   removes the inner O(n) from the packer's hot loop for free.

---

#### P1-8. `shoot.mjs` has two assertions that cannot fail, and does not check the thing the packer is actually hard at

**Where:** `Design/tools/shoot.mjs:106-109, 38-56, 68-116`

1. **The sheet-open assertion is vacuous:**
   ```js
   return !!(sheet && sheet.classList.contains('open') || (sheet && sheet.getBoundingClientRect().width > 0 && ...))
   ```
   The atlas uses class `on`, not `open` (`atlas-v3.html:1364`), so the first clause is always
   false. The fallback checks `width > 0` — but on desktop `#sheet` is `transform:translateX(105%)`
   with `width:min(430px,92vw)`, so its bounding-box width is > 0 whether it is open or closed, and
   `#sheetBody.innerHTML` is populated by `openSheet()` before the class is added. **The assertion
   reports `true` for a sheet that never opened.** Fix: assert `sheet.classList.contains('on')`.

2. **The overlap check does not check what the Blueprint asked for.** Blueprint §L specifies
   "geometric no-overlap check (box vs foreign tails)." `shoot.mjs:39-56` checks `.node` vs
   `.node` only. The hard invariant in `tryPack` — that a box never sits on **another family's
   living ribbon** (`atlas-v3.html:676-682`) — has no automated check at all. I wrote one for this
   review (node bounding-box vs every `#art path.tail` with a different `data-mid`) and it returns
   **0 hits at both viewports**, so the packer is correct today. But the invariant that took the
   most iteration to get right is the one nothing guards.

3. **Mobile interaction has zero coverage.** The 390px run takes a screenshot and counts overlaps,
   but `newPage` is created without `hasTouch`, so `matchMedia('(hover: none)')` is false and the
   tap→tap→document path never runs; and no touch events are synthesized, so **the pinch-zoom
   system that cost six rounds has no automated test whatsoever.** Playwright supports
   `hasTouch: true` and `page.touchscreen` / CDP `Input.dispatchTouchEvent`.

4. Minor: at 390px the map renders inside `#mapViewport` scaled by `minMapScale ≈ 0.32`, so the
   `EPS = 1` px tolerance is ~3.2px in content space — the mobile overlap check is 3× less
   sensitive than the desktop one. Divide `EPS` by `mapScale`, or run the check in content
   coordinates.

**Fix.** Add the box-vs-foreign-tail check, fix the sheet assertion, add a `hasTouch` mobile
context with a pinch and a two-tap case, and make the harness **exit non-zero** on any failure
(it currently only prints JSON) so it can be wired into P1-3's CI.

---

#### P1-9. Fail-open governance is silent, so a permanently broken check would never be noticed

**Where:** 11 `except Exception: pass` sites; the load-bearing ones are `main.py:963-964`,
`governance.py:358-361`, `governance.py:375-376`, `rag/retriever.py:225-226`.

Fail-open is the right *policy* here and is well argued in each case ("invisible governance fails
silently by design — the participant already has their response"). The problem is that it is
silent as well as non-fatal. If `run_table_checks` starts throwing on every turn — a typo in a
signal name, a langchain API change, a `None` where a string was expected — the participant sees
a perfect conversation, the drift log stays empty, and **nothing anywhere reports it**. The whole
table-governance layer could be dead for weeks.

Note that `main.py:1553-1556` gets this right for the analogous case: a degraded multi-world round
calls `logger.exception` with the turn count and session. The pattern exists in the codebase; it
just is not applied to the governance tail.

`retriever.py:225-226` is the sharpest instance: it silently swallows a failure whose effect is
that every migrated world's Quick Meaning section gets duplicated into every retrieved chunk —
a real token-cost and register-leak regression that would be invisible.

**Fix.** Replace every `except Exception: pass` in a logic path (not the logging modules, where
it is correct) with `except Exception: logger.exception("<what was being attempted>")`. Same
fail-open behaviour, now diagnosable. Consider a counter per site so "governance skipped N turns
today" is answerable.

---

#### P1-10. Unpinned dependencies plus reliance on a langchain private attribute

**Where:** `requirements.txt` (all 16 entries are bare `>=`), `pyproject.toml` (drifted from it),
`hybrid.py:72`.

`hybrid.py:72` reads `vector_store.docstore._dict` — a private attribute of a third-party class —
to enumerate documents for BM25. `hybrid.py:91-94` similarly walks `vector_store.index_to_docstore_id`
and calls `vector_store.index.reconstruct`. Combined with `langchain-community>=0.3.0` and no
lockfile, a `docker build` six months from now can resolve a langchain version where `_dict`
no longer exists — and the failure lands inside `HybridSearcher.__init__`, which is constructed
lazily inside a request, not at startup.

`pyproject.toml` is also stale relative to `requirements.txt`: it omits `supabase`, `rank-bm25`,
and `stripe`. Neither declares `PyYAML` (P1-2).

**Fix.** Generate a `requirements.lock` (`pip-compile` or `uv pip compile`) and install from it in
the Dockerfile; keep `requirements.txt` as the human-readable input. Make `pyproject.toml` the
single source and generate `requirements.txt` from it, or delete one. For `_dict`: wrap the
enumeration in a small adapter with a documented fallback to
`vector_store.similarity_search("", k=len(...))`, and add an import-time smoke assertion so a
library break surfaces at container start, not on a participant's turn.

---

#### P1-11. Frontend: a page refresh permanently orphans the conversation

**Where:** `frontend/src/hooks/useConversation.ts:46-57, 172-199`

`sessionId` and `sessionToken` live only in React state. A refresh, a tab crash, or a
backgrounded mobile tab that gets evicted loses the token — and `session_auth.require_session_access`
then returns 403 on every subsequent request for that session, permanently. Nothing writes either
value to `sessionStorage`/`localStorage`, and the backend's `GET /api/session/{id}` endpoint —
which exists and whose docstring says "Useful for reconnection" — is never called by the frontend.

Given the app's own `CONVERSATION_TURN_CAP_TABLE = 100` (i.e. sessions designed to run long) and
the mobile-first framing elsewhere in the project, this is a real participant-facing loss, not a
theoretical one.

**Fix.** Persist `{sessionId, sessionToken, worldIds}` to `sessionStorage` on session start; on
mount, if present, `GET /api/session/{id}` with the token and rehydrate `messages`/`phase`/
`turnCount`; clear on `resetConversation` and on any 403/404.

---

### P2 — polish

---

**P2-1. `atlas-v3.html` dead code and a comment that describes behaviour the code no longer has.**
- `header.bar` CSS (lines 77-83, 266) styles an element that does not exist in the document; the
  page's header is `header.site-header` + `#controls`. Consequently `document.querySelector('header.bar .s')`
  at line 719 is always `null` and the whole subtitle computation at lines 719-722 is dead.
- `bandBottom` (line 863), `clampX` (861), and `anchorX` (862) are declared inside `drawArt` and
  never used.
- `m._off = 0` (line 717) is written and never read.
- `m._segMap` (line 871) sets **every** era index to the same `m._x`, so `tailXAt` (915-918) is an
  identity function returning `m._x`. The comment above it (913-914) claims threads "depart the
  parent's tail WHERE IT ACTUALLY IS at the child's birth row (post-drift)" — describing a
  per-era drift mechanism that no longer exists. That is worse than dead code: it is a comment
  that will mislead the next person who tries to change thread routing.
- `window.__TW`, `window.__isCapped`, `window.__endRowOf` (lines 623, 635) pass values from
  `layout()` to `drawArt()` through the global object, although both functions are in the **same
  `boot()` closure** and `drawArt` is called directly by `layout()` with three arguments already.

*Fix: delete the first four; convert the three globals to parameters or closure-scoped `let`.*

**P2-2. `esc()` does not escape quotes but is used in ~15 attribute contexts.**
`atlas-v3.html:485` escapes only `& < >`. It is interpolated into `aria-label="${esc(...)}"`
(762), `title="${esc(...)}"` (1046-1047), `href="${esc(x.url)}"` (1320, 1330), and others. A `"`
in a census field breaks out of the attribute; a `javascript:` URL in `experienceToday[].url` or
`sources[].url` executes on click. The census is trusted, first-party, and validator-checked, so
this is P2 and not higher — but it is one `.replace(/"/g,"&quot;")` plus a scheme allowlist on the
two URL sites, and the validator could assert `^https?://` on every `url` field.

**P2-3. `tryPack`'s failure mode is silent.** `atlas-v3.html:709, 714-715`. If the widening loop
exhausts `W < viewW*5` with `fb > 0`, the remaining boxes are placed by the fallback at line 709
with no slot reservation — i.e. they can overlap — and nothing logs, warns, or surfaces it. Today
`fb` reaches 0 (verified: 0 overlaps at both viewports), but the failure is one crowded era away
and would ship silently. *Fix: `if(attempt.fb>0)console.warn(...)` plus a `shoot.mjs` assertion
on a page-exposed `window.__packFallbacks === 0`.*

**P2-4. `tryPack` is the most fragile thing in the file and its invariants are undocumented.**
The comments explain *intent* well (the free-gap idea, the lean limit, succession slot
inheritance) but not the *invariants a modifier must preserve*: that `rows` must be iterated in
strictly increasing `_row` order for `busy[k] >= m._row` to be a correct occupancy test; that
`ribbons` is append-only and scanned in full per row; that `okbx`'s strict `>`/`<` is what makes
the `iv[0]-0.5` / `iv[1]+0.5` probes legal; that `maxOff` couples box width `NW` to tail width
`TWb`. The Decision-Log's repeated warnings about this function's fragility are, on my reading,
accurate. *Fix: a 15-line invariant block above `tryPack` stating those four preconditions
explicitly, so a new engineer knows what they are allowed to change.* Given the file's history,
this is the highest-value comment anyone could add to it.

**P2-5. Dead modules and dead code in the backend.**
- `app/agents/facilitator.py` and `app/agents/representative.py` — imported nowhere (verified by
  grep). `representative.py` describes "Mar Yausep from the Syriac tradition" against a six-world
  manifest, and lists seven drift signals against 17+. `facilitator.py`'s docstring says "four
  functions" and lists five. Doc 02 flagged these in July.
- `builder.py:12` imports `route_after_input`, never used in the module.
- `cross_encoder.py:84-94` `relevance_partition` is now dead — `pipeline.py` does its own
  rank-aware partition. New dead code created by the S3.4 change.
- `nodes.py:882` `build_public_transcript(state, exclude_world_id=None)` — the parameter is still
  never referenced in the body, four months and two audits after doc 16 §1f named it.
- `nodes.py:3257-3275, 3306-3309` — the `_LANE_LENGTH_CEILINGS` / `participant_role` system is
  **still** fully authored and structurally unreachable (`participant_role` is not a field on
  `ConversationState` and is set by nothing). Doc 02 flagged it 2026-07-25.

*Fix: delete `app/agents/`, the dead import, `relevance_partition`, and `exclude_world_id`. For
the lane system, make a decision and record it: either add `participant_role` to
`ConversationState` and wire it, or delete the block and note in the Decision Log that role-mode
was deferred. Carrying permanently-dormant, heavily-rationalized code is a standing invitation for
someone to assume it works.*

**P2-6. `useConversation`'s callbacks omit `sessionToken` from their dependency arrays.**
`useConversation.ts:305, 353` — `sendMessage` and `endConversation` read `state.sessionToken`
but depend only on `[state.sessionId]`. Benign today because both are set in the same `setState`,
but it is exactly what `react-hooks/exhaustive-deps` exists to catch — and the plugin is installed
while the config that would enable it does not exist (P1-3).

**P2-7. `write_transcript` persists bridge-reframe sentinels into the human-readable transcript.**
`transcript_logging.py:86` slices `state.messages` and serializes everything, including the
`additional_kwargs={"bridge_reframe": True}` sentinel that `state_to_messages` (`main.py:291-292`)
and `_message_events` (`main.py:84-85`) both filter out. So the `messages` table Mark reviews
contains a Facilitator line that was never spoken to the participant, indistinguishable from one
that was. *Fix: apply the same filter, or persist a `kind` column.*

**P2-8. `_persist_jsonl` runs outside the append lock and `_read_jsonl` does not sort by seq.**
`events.py:289-300, 356-371`. Sequence numbers are assigned under the lock; the file write is
not, and `project()` folds in **file order**, not `seq` order. Two concurrent appends to the same
session could therefore produce a JSONL whose replay order differs from the in-memory order — and
`project_fresh` / post-restart projection would use the wrong one. Low probability (one
participant per session), trivially fixed: `sorted(out, key=lambda e: e.seq)` in `_read_jsonl`.

**P2-9. `_migrated_world_ids` lives in the wrong module and crosses a layer.**
`repair_classifier.py:133` owns the registry of which worlds have been migrated to the record
repository. It is imported by `nodes.py:1150` and — the layering problem —
`rag/retriever.py:222`, so the retrieval layer reaches up into the graph layer, for a fact that
has nothing to do with repair classification, inside a bare `except Exception: pass` (P1-9).
*Fix: move it to `world_manifest.py` as a manifest field or a module-level function; both callers
already import from there.*

**P2-10. Stale doc strings after successful cleanups.** `world_manifest.py:12-14` still names
"MessageBubble.tsx's own REPRESENTATIVE_INFO" as a manual frontend sync point; that dict no longer
exists (verified by grep). The `SpeakerName` union at `types/conversation.ts:70` **is** in sync
with the six manifest representatives. Good state, stale comment.

**P2-11. Two ID fields on every census movement.** `world-census.json` movements carry both `id`
(slug) and `atlasId` (`I.1`), and `atlas-v3.html` uses `id` everywhere except the alias search
(`:1477`), which keys on `atlasId`. Both are validator-required so neither is going away, but a
one-line comment at the `ALIASES` table saying "these are `atlasId`, not `id`" would prevent the
obvious mistake.

**P2-12. `applyFilter`/`applyLaneToggle`/`applyRegionToggle` run 257 `document.querySelector`
calls each, on every keystroke.** `atlas-v3.html:1012, 1124, 1480`. Not a measured problem at 257
nodes, but caching `el` on the movement object during `layout()` is two lines and removes a
per-keystroke O(n) DOM query.

---

## 4. Now vs. over time

### This week (small, high-value, low-risk)

1. **P0-1** — fix the path traversal. Five lines. Nothing else on this list matters if a key leaks.
2. **P0-3** — add three function calls to the theme handler. One line.
3. **P1-1** — replace the prefix match with a host allowlist. Ten lines.
4. **P1-2** — one `COPY` line in the Dockerfile, `PyYAML` in requirements, log the fallback.
5. **P0-4** — rewrite `docs/langgraph-architecture.md` as an honest one-pager. Two hours, and it
   is the difference between a new engineer being oriented and being misled.
6. **P1-3 step 1** — one CI workflow running `validate-census.mjs` + `tsc`. Half a day, and it is
   the first automated check this project has ever had.

### This month

7. **P0-2** — insert the `sessions` row; decouple session counting from pilot logging; fix the
   docstring.
8. **P1-9** — replace all eleven silent `except: pass` in logic paths with `logger.exception`.
   Cheap, and it converts an entire class of invisible failure into a visible one.
9. **P1-5** — make `run_eval.py` call `run_retrieval` instead of re-implementing it; commit
   `baseline.json`; add `--check`.
10. **P1-8** — fix the vacuous sheet assertion, add the box-vs-foreign-tail check, add a
    `hasTouch` mobile context with one pinch case, make `shoot.mjs` exit non-zero.
11. **P1-7** — debounce resize; early-return `layout()` when packing inputs are unchanged;
    preserve mobile zoom/scroll across relayout.
12. **P1-11** — persist the session token to `sessionStorage` and rehydrate.
13. **P2-4** — write the `tryPack` invariant block. Fifteen lines of comment on the most fragile
    function in the participant-facing frontend.

### Over time (structural)

14. **P1-6** — collapse the six freeze batteries into one harness with a declared per-world
    override file. ~1,500 lines deleted; rubric improvements start propagating.
15. **P1-4** — bound the event store; measure real RSS with two transformer models loaded; decide
    on a persistent disk or an un-gated Supabase event mirror before treating the audit trail as
    durable.
16. **P1-10** — lock dependencies; adapt away from `docstore._dict`.
17. **P2-5** — delete the dead modules, and *decide* the lane/role system's fate rather than
    letting it sit dormant for a third audit cycle.
18. **The graph question.** Decide whether `app/graph/builder.py`'s `StateGraph` should be deleted
    or actually used. Today it runs two nodes once per session and carries a 40-line diagram of a
    loop that never executes; `langgraph` remains a top-level dependency for that. Either is
    defensible; the current state is not.
19. **The `nodes.py` question.** 3,981 lines, up 42% since the last full read, containing
    generation, streaming, turn selection, five heuristic table checks, two adjudicators, the
    monitor, the reroot generator, retriever caching, and length ceilings. `governance.py` and
    `pipeline.py` show this team knows how to extract a layer and prove the extraction was
    behavior-preserving. Apply that same move — with the same replay-parity proof — to split
    `nodes.py` into generation / selection / signals. **This is the biggest structural debt in
    the backend and the least urgent; do it after CI exists, not before.**

---

## 5. Bottom line

**Would a competent engineer joining this project recognize it as well-built?**

Yes — after about a day, and with two specific caveats they would raise on day one.

The day-one impression will be mixed, because the first two things a new engineer opens are
`docs/langgraph-architecture.md` (wrong in nearly every particular — P0-4) and `main.py`
(2,008 lines) or `nodes.py` (3,981 lines). Both signal "prototype that grew." A new engineer would
immediately flag: no CI, no linter config, no tests in the conventional sense, no dependency lock,
a 4,000-line module, and an architecture doc that describes a control flow the code does not have.

Then they would read the comments, and the impression would invert. What is actually here is
unusually disciplined: an append-only event log replacing a hand-patched read-modify-write race,
with a state-parity instrument proving the replacement equivalent; a governance layer extracted
from two divergent endpoints with a **record/replay parity harness that asserts call order** and
declares its one intended behavior delta in code; a retrieval stack that is BM25+dense RRF with
graph expansion, adaptive relevance floor, MMR, and a local cross-encoder — every constant
carrying the measurement that set it and, in several cases, the failed alternative that preceded
it; a deterministic zero-cost retrieval harness with 105 golden cases that **brackets its own
non-determinism and treats the bracket width as a measurement**; freeze batteries with a genuine
held-out probe set and blind grading with a sealed mechanical-evidence key; and 42 labeled LLM
call sites feeding a cache-aware cost baseline.

**The testing/eval discipline is real, and I want to be precise about what kind of real it is.**
These are not ad hoc one-off scripts. They are *instruments*: carefully designed measurement
apparatus with stated methodology, provenance for every case, and honest declaration of what they
cannot measure. `s43`'s cases each trace to a specific recorded live incident. `s56` has a
train/test split. `run_eval.py` is better-designed than most commercial RAG eval tooling. That is
a genuine and unusual strength and it deserves the credit.

But an instrument is not a gate. **Nothing runs automatically.** There is no CI, no committed
retrieval baseline, no exit code on `shoot.mjs`, no assertion in the battery scripts. Every check
depends on a human executing the Loop Protocol correctly, and the evidence that this is not
sufficient is in this report: a two-click participant-facing regression that blanks the map
(P0-3), a grading rubric that has silently forked six ways (P1-6), a "canonical parameters file"
that is not in the production image (P1-2), a session cap that has never been able to fire
(P0-2), and a dead import that any linter would catch in a second. Each is small. Together they
describe a system whose quality depends on the sustained attention of one person, and degrades
exactly when that attention is elsewhere — which the Atlas HANDOFF's own "Fable hit ~97% of the
weekly window two days in" note says is a live constraint.

`atlas-v3.html`, judged on its own terms as a deliberate single-file no-build-step artifact, is a
success. The packing algorithm demonstrably works — I measured zero node-vs-node and zero
node-vs-foreign-tail overlaps at both viewports across 257 movements — the accessibility work is
real (focus trap, focus restoration, `inert`, `aria-live`, reduced-motion, print styles, verified
contrast ratios), and the mobile pinch-zoom rebuild is architecturally correct: making the sheet a
structural *sibling* of the zoomable region rather than fighting `position:fixed` during an active
gesture is the right diagnosis of a genuine platform limitation, and it closes all six prior
rounds at once. The file has one live bug (P0-3), a real performance/UX coupling on resize
(P1-7), and a handful of dead fragments with one actively misleading comment (P2-1). Its
Decision-Log is right that `tryPack` is fragile — and the single most useful thing anyone could
add to that file is fifteen lines stating the four invariants a modifier must preserve (P2-4).

**The single biggest lever: put the harnesses that already exist behind an automatic gate.**

Not "write tests" — the hard, expensive, genuinely good work of building the instruments is
already done, and rebuilding it as pytest would be a waste. The lever is one CI workflow and four
small changes: `validate-census.mjs` + `tsc` on every push (half a day, no secrets, no models);
`shoot.mjs` exiting non-zero on every `cic-website/**` change; `run_eval.py --check baseline.json`
with the baseline committed; and the replay parity suite runnable from its committed tapes. That
converts five carefully-built measurement instruments into five regression gates, and it is the
difference between a system that is well-built *right now, by one person who is holding it all in
their head*, and a system that stays well-built when they are not.
