# Decision Log — Conversation & Transparency Engine

Append-only, workstream-local, per `CLAUDE.md`. One entry per PR merged
and per ruling made. Never edit or renumber a past entry; a correction is
a new entry that says what it corrects.

---

**Entry 1 — 2026-09-19.** Workstream opened. Fable design pass 2
(Opus-reconciliation) complete: `Adjusted-Design.md`, `Build-Plan.md`,
`Rulings-Pending.md` written from the Fable agent's report. Reviewable
summary published as an Artifact:
`https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`. Mark authorized
starting the Sonnet build thread on Stages 0–4 only; Stages 5–9 remain
blocked on `Rulings-Pending.md` and Stage 1's own measurement.

**Entry 2 — 2026-09-19.** Prior to this workstream, three live safety
defects found by an independent Opus adversarial review were fixed and
merged to `main` (PR #306, commit `1c522e918`): a reader-timeout
discarding a successful crisis classification (`engine/m5/failure.py`,
`engine/m5/routing.py`); the crisis-continuation message carrying no
actual redirect language (`engine/m4/crisis_resources.py`); the
citation-grounding check being fooled by a fabricated claim built from a
forbidding guard's own vocabulary — partial fix only
(`engine/prose.py`); the full defect is structural and is what
`Build-Plan.md` Stage 1 measures. Noted here for this workstream's own
record since it is the ground truth `Adjusted-Design.md` §0 stands on.

**Entry 3 — 2026-09-19.** Scope correction, same day as entries 1–2. This
workstream was briefly named "Transparency & Safety Redesign" and carried
a 19-item ruling queue, roughly a third of it proposed new safety
machinery (escalation tiers, message decay, a conditional memory window,
output-side sentence withholding, distinct messages per disclosure type)
that Mark never asked for — the original charter was the conversation and
transparency engine only. Mark's direct ruling: *"if there is an
expression of safety then the facilitator will step in and ask, then
provide an encouragement to seek human help, thats it no more crap or
complication, that meets the need and keeps the system clean."*

This closes the following as **resolved, not deferred** — the Facilitator's
safety mechanism is a fixed, single-step shape and is not open design
space:
- **S1** (safety-call failure handling) — closed. No async reclassification,
  no operator paging build-out. The existing fail path stands.
- **S2** (escalation priority / message decay / interim text) — closed. No
  new escalation-tier logic, no decay timer. The already-merged fix (PR
  #306) — a plain redirect on every crisis-relevant turn, first one or
  repeat — is the whole mechanism.
- **R1** (safety-call-failure fallback options) — closed, same as S1.
- **R2** (escalation/decay/interim-text options) — closed, same as S2.
- **R3** (item 16's "conditional memory window" replacement) — closed. No
  replacement is built. The classifier stays fully memoryless, as struck
  in `Adjusted-Design.md` §2 (item 16 itself was already struck there for
  cost reasons; this closes the door on any replacement mechanism too).
- **R4** (reminder-repeat frequency / voice-visibility) — closed. One
  check-in, once. No frequency tuning, no repeat-suppression logic beyond
  what already exists.
- **R14** (output-side sentence withholding) — closed. Never built, in any
  form — the mechanism reports only, exactly as it does today. No future
  reconsideration tied to a measured rate; this is not a "revisit later"
  item.
- **R15** (distinct message for third-party risk disclosure) — closed. One
  message, no branching by disclosure type.

Renamed the workstream directory `Ministry/Features/Transparency-Safety-
Redesign/` → `Ministry/Features/Conversation-Transparency-Engine/` and
rewrote `README.md`, `Adjusted-Design.md`, `Build-Plan.md`, and
`Rulings-Pending.md` to match. Nothing about the three already-merged bug
fixes (PR #306) changes — those were legitimate defect fixes, not
redesign, and Mark confirmed them explicitly ("yes you can fix a couple
of broken things"). Stages 0, 2, 3, 4 of `Build-Plan.md` (conversation/
transparency engine work — retrieval, library connection, citation/
confidence display) are unaffected and continue. Stage 5 is removed from
the build plan entirely, not just reordered.

**Entry 4 — 2026-09-20.** Stage 4c Part 2 merged (PR #325, commit
`2cb5efdad`): `retrieval_words()` relocated from `engine/m2/builders.py`'s
private `_retrieval_words` to public `engine.prose.retrieval_words()` so
`engine/m4/evidence.py` (runtime) and `engine/m2/` (compile-time) score
against the identical retrieval-safe word set without `m4` importing
`m2`. New Stage B2 fill in `select_cell_candidates`: when a cell's own
coverage has zero candidates of a type, fill from whole-repository
`retrieval_words()` overlap, capped at that type's `_TYPE_FLOORS`, tagged
`retrieval_fill: True`. `retrieval_bench` fleet reach: 813 → 1152. Same
PR also fixed a stale `ACCEPTED_OPEN` waiver (`site-portrait/witt`) in
`engine/m1/cross_world.py`, found as a side effect of an unrelated CI
investigation and confirmed pre-existing on `main` via git-worktree
reproduction — root-cause fixed per the file's own "CLOSED" convention,
not worked around. Full suite + fleet gates green.

**Entry 5 — 2026-09-20.** Stage 4d merged (PR #326, commit `402153909`):
`_tier_prior()` (`engine/m4/evidence.py`) adds +0.05/+0.02/+0 by
`retrieval.tier` (1/2/other) to `select_cell_candidates`'s per-cell
ranking, breaking near-ties toward "core" material. `retrieval_bench`:
1152 → 1150 — a small, real, measured regression (4/118 questions moved),
traced to the shared per-cell `budget_chars` interacting with tier-prior
reordering on genuine score ties, and verified not an over-tuning
artifact (identical swaps reproduce under the most conservative possible
tie-break-only design). Surfaced to Mark via options rather than shipped
or reverted silently; his ruling: ship it, document the tradeoff here.
Full suite + fleet gates green.

**Entry 6 — 2026-09-20.** Stage 4f merged (PR #334, commit `114925866`):
`assemble_evidence` gained a new `secondary_context: str | None = None`
parameter (deliberately not reusing the existing `history` list, which
is shared with the live model call's own conversational memory and would
have duplicated content already visible via `context_prefix`) — fills
remaining `top_n_cells` slots from table-conversation context at lower
priority than the participant's own message, tagged
`from_secondary_context: True`. Wired from `table_wiring.py` via new
`_secondary_context_text()`. `retrieval_bench`: byte-identical at 1150
(interview mode never sets `secondary_context`, so the fixture-world
bench is unaffected by design). Full suite, M8 hermetic usage check
(no per-turn growth), and fleet gates green.

**Entry 7 — 2026-09-20.** Stage 3c merged (PR #335, commit `bb1ef7552`):
new `engine/m4/transparency_plan.py` work (Stage 3a/3b) was already
merged in a prior session window; this PR closed the renderer half.
Root cause of the "recurring, inconsistent" citation-mark dropout Mark
had been describing: `VoiceTurnBody.tsx`'s legacy renderer reconstructed
marks by searching finished text for each citation's own sentence, using
three ad hoc dedup structures — `renderedStoryIds`/`renderedWitnessIds`
suppressed a SECOND, non-consecutive citation of the same story/witness
record turn-wide, and because story/witness sources were never passed to
`addReference`, the repeat's sourcing was dropped entirely, not just its
mark — the exact defect `transparency_plan.py`'s own docstring names.
Fix: a new anchor-driven renderer reading the engine-computed
`transparency` plan (every run, including repeats, gets its own mark via
`anchorsByRunEnd`), dispatched behind `VITE_TRANSPARENCY_ANCHOR_RENDERER`
(default off — current behavior — until R10 and label copy are ruled).
Added `vitest` + `@testing-library/react`, a `test` script, and a
`frontend-tests` CI job. A same-day follow-up push to this PR
(`9321610b6`) fixed a real, unrelated CI failure found while verifying:
`jsdom@30.1.0`'s bundled `undici` calls a webidl API only present on
Node ≥22, crashing every test file at import under CI's pinned Node 20 —
reproduced locally on both Node 20 and 22, fixed by pinning `jsdom` to
`26.1.0`. Full suite + fleet gates green; `npx tsc --noEmit` and the new
`npm test` clean on both Node versions.

**Entry 8 — 2026-09-19.** Stage 2a merged (direct-to-main commit
`ee5a4a64e`, predates the branch-protection rule requiring PRs): new
`engine/m1/spoken_fields.py` (`SPOKEN_FIELDS` registry, roles
`voice-diet | evidence-head | participant-label | instruction`), one
source of truth in place of seven separate field lists previously
scattered across `engine/m2/builders.py`, `engine/m4/evidence.py`,
`engine/m4/citation_cards.py`, `engine/m1/gates.py`, and
`engine/m1/cross_world.py` — all rewired to import from it (old
locations carry "Relocated 2026-09-19" markers). AST test in
`engine/m1/tests/test_spoken_fields.py` fails on any undeclared
spoken-field read. Compiled bytes unchanged; determinism-check and
staleness-check green with no repin, per the stage's own bar. Logged
here retroactively — found genuinely done during a Build-Plan status
audit, undocumented until now.

**Entry 9 — 2026-09-19.** Stage 2b merged (direct-to-main commit
`d78347389`): new `engine/m1/bar_screen.py` (`python -m
engine.m1.bar_screen <world>`), reusing `engine/m7/instruments.py`
primitives and `engine/m1/fk.py`. Fixture artifacts committed for all
ten worlds: `worlds/<code>/build/bar-screen-2026-09-19.json`. Logged
here retroactively, same as Entry 8.

**Entry 10 — 2026-09-20.** Stage 3d merged (direct-to-main commit
`b95315148`, 01:34 UTC, before the same day's 4c/4d/4f/3c PRs): new
`gloss_forms` field on `term` records (`engine/m1/schemas.py`,
additive, `technical | ordinary` per form) and the gating logic in
`engine/m4/term_glosses.py` — an `ordinary` form only fires when the
sentence citing it already cites that term's own record; everything
else (including every pre-existing term) defaults to `technical` and
fires on sight, unchanged. All five gallic records named in the
stage's own Done bar carry the new field:
`gallic.term.the-world-secular` ("the world", "secular"),
`gallic.term.virtus` ("power"), `gallic.term.elder-senior-abbot`
("elder", "senior"), `gallic.term.brethren` ("brethren"),
`gallic.term.disciple-master` ("disciple", "master") —
`engine/m4/tests/test_term_glosses.py` proves those five no longer
fire uncited while Logos/hesychia/allegoria still do. Authoring rule
drafted and flagged; `reference/L4-Templates/*` untouched, per the
stage's own instruction. Logged here retroactively, same as Entry 8.

**Entry 11 — 2026-09-20.** Stage 2e merged (direct-to-main commit
`1329536a1`, 02:23 UTC): golden retrieval benchmark sets for the four
worlds `Build-Plan.md` named as missing (cappadocian, don, gallic,
rzg), 12–20 questions each, added to
`engine/m4/reports/bench/{cappadocian,don,gallic,rzg}.json` alongside
the six already committed — all ten worlds now covered — and baselines
appended to `retrieval_bench.py`'s history. Per the stage's own rule
("committed before any Stage 4 change"), this landed before the same
day's Stage 4c Part 2/4d/4f work. Logged here retroactively, same as
Entry 8.

**Entry 12 — 2026-09-20.** Build-Plan status audit (this session,
following up on the Entry 4-7 backfill finding that Decision-Log
entries had gone missing before): a full re-check of every Stage 0, 1,
2, and 3d sub-stage against its own literal "Done:" bar — not just
whether a plausibly-named file exists — found Entries 8-11 above
(2a, 2b, 2e, 3d) genuinely done and merely undocumented, matching the
4-7 pattern. It also found eight sub-stages genuinely **not** built,
not just unlogged: **0a** (concurrent `call_safety`/`call_reader` in
`run_gate` — still fully sequential), **0b** (Leave button — still
takes `disabled` in `ChatInput.tsx`, contradicting the stage's own bar
verbatim; both callers pass a disabling prop), **0c** (`round_cap` —
not exposed anywhere in the API/types/frontend, and `TableRoom.tsx`
still hardcodes a literal round count in participant-facing copy,
which the stage explicitly forbids), **0d** (`safety_script_run.py`
has no `--all` combined-tally mode, only per-batch `--batch <n>`),
**0e** (`observe_outside_help_guard` does not exist), **1** (D1
grounding measurement — `grounding_fooling_measure.py` does not
exist), **2c** (`observe_register_profile` does not exist; R6 has no
filed ceiling proposal), **2d** (`engine/m9/holdings.py` does not
exist; `COVERAGE`/`REGIONS`/`AUTHORS` were never relocated out of
`cross_world.py`). R11 (gates Stage 4a/4b) confirmed still PENDING in
`Rulings-Pending.md` — 4a/4b correctly untouched. Full detail in the
audit transcript; this entry is the durable record. Next work: Stage 0
(all sub-stages NOW, unblocked, no ruling required) in its own written
order.

**Entry 13 — 2026-09-21.** Stage 1 (D1 grounding measurement) merged
(PR #344, commit `86be79c4c`): `check_turn()` refactored into a public
`verdict_for_sentence()` (pure extraction, zero behavior change, proven
by an equivalence test) so the new `engine/m4/reports/
grounding_fooling_measure.py` can run the real per-sentence verdict logic
directly against a constructed `(sentence, tags)` pair. Three corpora, all
zero live-model-call:

- **Corpus A** (real logged turns, re-run against current packages): 34
  turns / 529 sentences (the design doc's own cited "36/546" is stale, not
  forced to match) — 98.87% verdict reproduction; all 6 changed verdicts
  moved toward more caution, zero regressions.
- **Corpus B** (constructed fabrications, tagged to their own source
  record): 251 items — 97.6% fooled overall (`contested_claim` 100%,
  guard-species `do_not_retrieve_when` 84.6%, `honest_limit` 100%,
  `absent_detail` 96.7%). The `honest_limit`/`absent_detail` flat
  assertions (170 of the 251) were authored in a one-time pass rather than
  templated — that free-form prose resisted a safe mechanical negation-flip
  (full reasoning in the script's own docstring).
- **Corpus C** (one-shared-word mis-tagging): 132 pairs, no proper noun,
  exactly one shared content word — 96.97% passed as "ok" anyway.

Also found and logged separately in `Rulings-Pending.md`'s R11: only 13 of
714 `do_not_retrieve_when` lines fleet-wide (1.8%) are genuine
honesty-guard clauses; the rest are unrelated retrieval-scoping notes.

Structural conclusion (per the design doc, unchanged by this measurement):
`grounding_ratio` is provenance — word overlap with a cited record — not
truth-verification; mitigations are upstream (riders, guards, honest-limit
records) and reporting, and any UI element implying per-sentence truth
verification overclaims. No threshold (`WITHHOLD_FLOOR` etc.) was changed;
this stage was read-only measurement throughout.

**Known gap, named not hidden:** the design doc's *optional* one-time
Sonnet labeling pass over Corpus A's real withheld + stratified-ok
sentences (an FP/FN rate against actual source support, not just verdict
reproduction) was not run in this pass — only the *required*,
zero-model-call baseline shipped. A real regression from the
`verdict_for_sentence` extraction was caught by the existing test suite
(`test_prose.py` pinned `grounding_ratio`'s call site to `check_turn()`'s
own source; fixed to point at the function it actually moved to) and
fixed before merge, not routed around. Full suite 740 passed / 6 failed /
23 errors — the failures are the pre-existing Stage 0c package-completeness
gap (root cause reconfirmed here), unrelated to this branch. Fleet gates
green. Full numbers: `engine/m4/reports/grounding-fooling-2026-09-21.json`.

**Entry 14 — 2026-09-20.** Stage 0a merged (PR #339, commit `0175b5be6`):
`engine/m4/turn.py`'s `run_gate()` called `call_safety` then `call_reader`
strictly sequentially, paying both latencies back to back on every turn
even though neither call's input depends on the other's output. Both now
run on a 2-worker `ThreadPoolExecutor`; the httpx-based Bedrock SDK client
is thread-safe, so there was nothing to serialize. Each call keeps its own
existing 4s timeout; `usage_records` still append in the same fixed order
(safety, reader) regardless of which future completes first, matching
every existing caller's assumption. `engine/m4/tests/test_turn.py`
extended (+32 lines) proving both calls invoked and routing byte-identical
to sequential for every existing scenario; the table path inherits the fix
via `run_gate` with no separate wiring needed. Logged here retroactively —
found genuinely done during this session's own re-verification, matching
the Entry 4-12 pattern of merged-but-undocumented work.

**Entry 15 — 2026-09-20.** Stage 0b merged (PR #340, commit `460b5194f`):
`cic-poc/frontend/src/components/ChatInput.tsx`'s Leave button took the
same `disabled` prop as Send/the textarea, so a participant mid-turn
(`Conversation.tsx`'s `isLoading`) or inside an open Table round
(`TableRoom.tsx`'s `isLoading || roundOpen`) could not leave until the
in-flight call resolved. Leave no longer takes `disabled` at all; Send and
the textarea are unchanged. New `ChatInput.test.tsx` proves both halves.
Confirmed directly on disk: Leave (~line 73) carries no `disabled` prop
while Send (~line 64) still does. Logged here retroactively, same as
Entry 14.

**Entry 16 — 2026-09-20.** Stage 0c merged (PR #341, commit `9ddc9c843`):
`TableRoom.tsx` hardcoded "a Table holds five rounds" in participant-
facing copy — and it was wrong on its own terms, not just hardcoded:
`engine.m4.round.TABLE_SESSION_ROUND_CAP` is 3. Session-create and
transcript API responses now carry the real value (`round_cap: int |
None`, `null` for an interview session where no cap applies) via a new
`engine/api/table_wiring.py` `round_cap_for(mode)` helper, plumbed through
`engine/api/app.py`'s response models, `types/conversation.ts`, and
`useTable.ts`; `TableRoom.tsx` renders the real number instead of the old
guess. `test_table_api.py` asserts the field (+15 lines); confirmed no
literal round count remains anywhere in `src/`. Logged here retroactively,
same as Entry 14.

**Entry 17 — 2026-09-20.** Stage 0e merged (PR #342, commit `bdc7cf252`):
new `engine.m1.cross_world.observe_outside_help_guard` — per world, does
`voice_craft.guard` carry don's own categorical distress-comparison
prohibition, scanned by keyword (not a semantic judgment, per its own
docstring), report-only, registered in `CHECKS` alongside the fleet's
other `observe_*` functions. Findings are already carried under R19 in
`Rulings-Pending.md`: of the 11 built worlds, only **don** and **rzg**
carry the language; the other 9 (alx, cappadocian, desert, gallic, hal,
ijc, pahc, syr, witt) do not. Logged here retroactively, same as Entry 14.

**Entry 18 — 2026-09-20.** Stage 0d merged (PR #343, commit `11e2093c5`):
`engine/m5/safety_script_run.py` gained `--all` (runs every committed
batch, prints one combined tally; the existing per-batch `--batch <n>`
mode and `BATCHES` itself are unchanged). `render.yaml` pins
`CIC_API_SAFETY_MODEL_PATTERN` to the exact resolved profile id
(`us.anthropic.claude-haiku-4-5-20251001-v1:0`) rather than the loose
default pattern, with `engine/api/README.md` documenting the rationale and
the repin discipline (repin only alongside a fresh `--all` tally). CLI
unit-tested with a fake client (`test_safety_script_run.py`, +74 lines); a
same-PR CI fix (commit `d041530d7`) installed `engine/m4/requirements.txt`
for `anthropic`, needed because the new test imports
`engine.m5.live_calls` at module level, which imports `anthropic` itself.

**Known gap, named not hidden:** the stage's own Done bar requires "the
live tally is by-hand, credentialed, never CI; tally path in
`Decision-Log.md`" before the pin can be relied on — that by-hand tally
has not been run or logged anywhere in this workstream as of this entry.
The pinned model id is asserted by the PR, not yet verified against an
actual `--all` run. Per the stage's own instruction ("Escalate if pinned
id ≠ last tally's id"), this still needs to be run and logged before the
pin should be treated as trustworthy. Logged here retroactively, same as
Entry 14.

**Entry 19 — 2026-09-21.** Stage 2c merged (PR #349, commit `c19283d28`):
new `engine.m1.cross_world.observe_register_profile` — per world, per
voice-diet spoken field, median words/longest sentence/fragment
ratio/dash density, reusing `engine.m7.instruments`'s own cadence math
(`_strip_quoted`, spaced-dash density, the ≤5-word fragment share) at the
compiled record layer instead of a live conversation turn. OBSERVATION
only. `alx`/`hal` print first as the exemplar context. Verified against
Build-Plan.md's own cited numbers: hal 21 / cappadocian 25 / don 34
matched exactly; gallic 42 against the plan's cited 43, a one-word gap
consistent with real data drift since the plan was written. Ceiling
proposal filed under R6, scoped to the two label-shaped fields
(`story.tellable_as`, `term.quick_meaning`) with concrete per-world
exceedance counts — gallic worst on all four numbers. Gate promotion
stays blocked on R6. Full suite (`test_cross_world.py` 11/11, `engine/m7`
63/63), `cross_world`/`staleness-check` clean, CI green.

**Entry 20 — 2026-09-21.** Stage 2d merged (PR #350, commit `b4d05b0a7`):
new `engine/m9/holdings.py` + `holdings` CLI subcommand — one row per
vendored file per world (`in_scope`, `named_in_records`, `drawn_on`,
`disposition` from a closed six-value vocabulary), mechanically derived
from `engine.m1.cross_world`'s own `corpus_tier` rather than duplicating
its judgment. `drawn_on` reuses `cic/engine/texts_registry.py`'s own
full-text-scan technique, scoped to one world. Verified against the
stage's own literal Done bar: gallic shows exactly 19 files disposition
`"not yet assessed"`, matching Build-Plan.md's own cited number exactly.
**Known gap, named not hidden:** the COVERAGE/REGIONS/AUTHORS relocation
into `cic/corpus-map/` and `observe_second_hand_sources` reading
`AUTHORS.md`/`AUTHOR-IDS.yaml` directly (also part of this stage's own
spec) was deliberately not attempted in this pass — that data is
load-bearing for `worlds/_cross-world/gen_corpus_table.py` and several
worlds' own Review-Artifacts, and deserves its own careful pass rather
than a rushed tail-end rewrite. `engine/m9/tests` 60/60 (5 new), `m9 cli
check` clean, manually confirmed on all 11 built worlds, CI green.

**Entry 21 — 2026-09-21.** R11 ruled: **(a) split it** — a redirect half
and a separate honesty-guard half, per Rulings-Pending.md's own
recommendation. Mark's direct ruling, given the Stage 1 D1 measurement
already in front of him (13 of 714 `do_not_retrieve_when` lines are
genuine guard clauses; those 13, fabricated, were caught only 2/13 times
by the grounding checker). Unblocks Stage 4a ("the split") and, after it,
4b (`guard_proximity`). Rulings-Pending.md's own R11 entry updated in the
same edit.

**Entry 22 — 2026-09-21.** Stage 4a (part 1) merged (PR #359, commit
`cdaf9f3b`): additive schema for R11's split. `engine/m1/schemas.py` gets
`retrieval.prefer_instead` (the redirect half, inside `_RETRIEVAL_SCHEMA`)
and envelope-level `claim_guards` (the honesty-guard half, on
`ENVELOPE_PROPERTIES` like `retrieval` itself); `engine/prose.py` gets
`claim_guards` added to both `NON_PROSE_KEYS` and `FALLBACK_EXCLUDED_KEYS`
**before** a single `claim_guards` value exists anywhere, per the stage's
own ordering, with a test pinning both exclusions. `engine/m1/tests` +
`engine/tests` + `engine/m4/tests` 415/415; `staleness-check` clean (purely
additive, no compiled-byte impact); CI green.

**Correction, logged rather than hidden:** this PR's own commit message
and PR title described the `NON_PROSE_KEYS`/`FALLBACK_EXCLUDED_KEYS`
exclusion mechanism as a "safety net." Mark's direct correction, given
after this PR had already merged: that phrase names the Facilitator-only
crisis/distress mechanism specifically, and must never describe anything
on the Representative side — this exclusion list is a citation/
fabrication-prevention mechanism, a different thing entirely, never the
Facilitator's job and never described in its vocabulary. The PR is already
merged into `main`; its title and commit message are not rewritten (shared
history, per this project's own discipline against rewriting a published
branch), but every PR, commit, and record from here on says "exclusion
list," never "safety net," for this mechanism.

**Entry 23 — 2026-09-21.** Stage 4a (part 2, gallic pilot) merged (PR #360,
commit `8d6d0fc6`): `tools/split_retrieval_guards.py` — splits every
record's `retrieval.do_not_retrieve_when` into `retrieval.prefer_instead`
or envelope-level `claim_guards`, via a raw-text line splice (pattern:
`tools/set_source_kind.py` — never a YAML dumper round-trip, so every
retained line keeps its own original quoting/wrapping). Classification
reuses `engine.m4.reports.grounding_fooling_measure`'s own `GUARD_MARKERS`
keyword set rather than building a fresh Haiku classifier. Build-Plan.md's
own literal Stage 4a text names "Haiku migration tool"; this is a
considered substitution, not a silent deviation — `GUARD_MARKERS` is the
exact classifier Stage 1's own D1 measurement (13 of 714 lines) was run
against, so reusing it keeps the split accountable to the same number R11
was actually ruled on, rather than risking a second, independent
classifier disagreeing with it.

Piloted on gallic first, per the stage's own "gallic first" ordering: 105
records touched, 0 skipped, and exactly the 5 known guard records
(Rulings-Pending.md's own R11 entry) land in `claim_guards` — everything
else becomes `prefer_instead` in place. `python -m engine.m2.cli build
gallic` + repin (`records/worlds/gallic.yaml`); `retrieval_bench.py`
byte-identical to the pre-migration baseline (TOTAL 118 qs / 1152 ground /
9.8 avg / 0 empty); `staleness-check` and `engine.m9.cli check` both
clean; full suite 516/516. CI green (19/19 checks, 2 correctly skipped by
path filter).

**Entry 24 — 2026-09-21.** Stage 4a (part 3, remaining fleet) merged (PR
#361, commit `5d866a3f`): the same tool run for real against the other 10
built worlds (alx, cappadocian, desert, don, hal, ijc, pahc, rzg, syr,
witt) — 829 records touched fleet-wide, 0 skipped. Mid-run, discovered the
tool's first version (validated only against gallic's own real shape)
would have silently skipped the fleet's actual dominant shape:
`do_not_retrieve_when: []`, an inline empty flow list (525 records
fleet-wide) that gallic itself happens not to use at all. Fixed
`split_frontmatter` to recognize and drop this shape (nothing to redirect
or guard either way) before trusting any world beyond gallic; covered by a
new test before the fix was trusted. All 11 built worlds now carry zero
`do_not_retrieve_when` records — Stage 4a's own Done bar ("all worlds
migrated") is met. `records/worlds/<world>.yaml` repinned for all 10 (each
world's package rebuilt fresh, orphaned prior manifests removed).
`retrieval_bench.py` byte-identical to the pre-migration baseline across
the whole fleet (TOTAL 118 qs / 1152 ground / 9.8 avg / 0 empty);
`staleness-check` and `engine.m9.cli check` both clean; full suite
517/517. CI green (19/19 checks, 2 correctly skipped by path filter).

Still not in this or any prior Stage 4a PR, and not yet started: the new
`retrieval-negatives-structured` gate with its seeded defect, and the
`evidence.py` riders that let `render_evidence_block` actually read
`prefer_instead` (demoting a candidate, never excluding it, inside the
existing `budget_chars` budget). Those are the stage's remaining open
work.

**Entry 25 — 2026-09-21.** Stage 4a's `retrieval-negatives-structured`
gate merged (PR #366, commit `6251ae43`): `engine/m1/gates.py`'s new
`gate_retrieval_negatives_structured`, registered in `GATES`, enforcing
three structural invariants schema-validation alone can't (
`do_not_retrieve_when` stays in the schema only for additive-only
compatibility, so a populated one passes schema checks cleanly) -
(1) `retrieval.do_not_retrieve_when` must stay empty/absent, a populated
one being a regression to the pre-R11-split shape; (2) every
`claim_guards` entry must read as a genuine barred-claim guard (matches
`GUARD_MARKERS`); (3) no `prefer_instead` entry may read as a guard
clause, the mirror check. `GUARD_MARKERS` and a new `is_guard_marker_line`
moved to `engine/prose.py` as the single shared source of truth in the
same PR - previously duplicated in `grounding_fooling_measure.py` and
`tools/split_retrieval_guards.py`, both switched to import from there.
One seeded defect (`fixtures/seeded_defects.yaml`), following this file's
own one-defect-per-gate convention; confirmed caught, silent on the clean
fixture, and not inert.

The new gate found **zero findings across the real 11-world fleet** -
independent confirmation that PRs #360/#361's migration is genuinely
clean by this gate's own three checks, not just by inspection. Adding a
gate changes every world's own `validation/gates-report.json` content, so
all 11 fleet worlds + `fix` needed a repin even though no record content
changed; orphaned prior manifests removed. `retrieval_bench.py`
byte-identical to baseline; `staleness-check` and `engine.m9.cli check`
both clean; full suite 517/517. CI green (19/19 checks, 2 correctly
skipped by path filter); confirmed zero file overlap with concurrent
parallel-session work merged to `main` in between branch creation and
merge.

Still not started: the `evidence.py` riders that let
`render_evidence_block` actually read `prefer_instead` (demoting a
candidate, never excluding it, inside the existing `budget_chars`
budget) - Stage 4a's one remaining item.

**Entry 26 — 2026-09-21.** Stage 4a's `evidence.py` riders merged (PR
#372, commit `b707c2b4`) - the stage's last remaining item.
`do_not_retrieve_when`'s replacement fields had been authored fleet-wide
(PRs #360/#361) and structurally enforced (PR #366) since Stage 1's own
`observe_unread_retrieval_config` finding that the field was "read by no
runtime path" (Decision-Log.md's own Entry 4-era finding) - this PR is
what actually wires `prefer_instead`/`claim_guards` into real retrieval
behavior for the first time.

`engine/m4/evidence.py`:
- `claim_guards` renders as a rider directly on its own candidate's line
  in `render_evidence_block` (`MUST NOT ASSERT: ...`), per Adjusted-
  Design.md's own "upstream prevention, the mechanism that actually
  works" - never a separate section a skim could miss. Counted into
  `select_cell_candidates`'s own `used_chars` budget accounting (a new
  `_entry_chars()` helper, head + guard length together), so the rider
  rides inside the existing `budget_chars`, never a separate allowance -
  Build-Plan.md's own literal wording.
- `prefer_instead` demotes a matching candidate's relevance score by half
  (`_PREFER_INSTEAD_DEMOTION_FACTOR = 0.5`, applied to the word-overlap
  share only, never to `_tier_prior`) when the participant's own query
  shares content words with the note's own condition text - proportional,
  never a hard exclusion, so a strongly-relevant record can still surface
  if its redirect target isn't in the same candidate pool. Wired into
  both scoring paths (`select_cell_candidates`'s main loop and
  `_retrieval_fill_scores`'s own Stage B2 fill), one shared helper, not
  two copies that could drift apart.
- A real, measured false-positive risk found and fixed before trusting
  the mechanism: over a third of the fleet's 702 real `prefer_instead`
  notes open with "participant"/"the participant" boilerplate (the
  note-authoring convention itself, not a real participant's own words),
  and "question"/"asking"/"wants"/"needs"/"asks" are close behind -
  keyword-overlap demotion without excluding them would misfire on any
  query sharing only that scaffolding, not the actual topic. Fixed with a
  small stopword set scoped to this one function (`_PREFER_INSTEAD_
  CONDITION_STOPWORDS`), not added to `engine.prose`'s global
  `_STOPWORDS` (tuned for ordinary prose, not this note format).

8 new tests in `engine/m4/tests/test_evidence.py` (constructed examples,
same fixture discipline as the file's own Stage 4d tier-prior tests) plus
direct verification against real gallic data before trusting the
mechanism. `retrieval_bench.py`: 1152 → 1154 (0 empty, matching Build-
Plan.md's own "equal or better" bar) - a small, real improvement, not
noise: `select_cell_candidates` now lets a genuinely better-matching
redirect target win a floor slot a demoted candidate previously held.
`staleness-check` stays green with **no repin** - `evidence.py` is
runtime scoring logic, never part of any world's compiled package bytes,
unlike the schema/gate changes earlier in this stage. Full suite 525/525.

**Stage 4a is now fully done**: schema (PR #359), gallic pilot (PR #360),
remaining-10-worlds migration (PR #361), the `retrieval-negatives-
structured` gate (PR #366), and these riders - every item Build-Plan.md's
own Stage 4a line named. Next in the build plan: Stage 4b
(`guard_proximity`), blocked on 4a being ruled shipped, or Stage 6-9 per
`Rulings-Pending.md`'s own remaining open rulings.

**Entry 27 — 2026-09-21.** Stage 4b merged (PR #374, commit `0155da66`):
`engine/m4/output_check.py`'s fourth family, `guard_proximity` - a
sentence that cites a record carrying `claim_guards` (R11's guard half)
and shares that guard's own barred proposition's subject matter. A second,
independent net alongside `grounding_net`'s own per-sentence check - Stage
1's own D1 measurement found that check caught a fabricated guard
violation only 2 of 13 times. `_guard_proposition()` strips `GUARD_MARKERS`'
own framing and the note-authoring boilerplate from a guard's text, and
excludes its own proper nouns from the required overlap - two names
sharing a sentence (e.g. Brictio/Martin, the story's own two subjects) is
not itself the barred claim; only sharing what the claim actually asserts
about them is. Threshold (≥2 shared words) is the real floor measured
against Stage 1's own 13 fabricated flat assertions, not a guess: the
smallest overlap among all 13 is exactly 2.

**Verified against real data, both directions.** Catches 13/13 of Stage
1's own fabricated flat assertions
(`grounding_fooling_measure.GUARD_FLAT_ASSERTIONS`). The design's own
false-positive test found a real problem before it shipped: an earlier
version (combined word overlap, no proper-noun exclusion) flagged
"Brictio was in the courtyard when Martin confronted him" - a true
sentence naming the story's own two subjects with no succession claim at
all. Excluding proper nouns from the required overlap fixed that false
positive without losing any of the 13.

`check_output()` gained optional `citations`/`repository_records` params
(backward compatible - a caller with neither gets the first three
families exactly as before), wired at the one real call site,
`engine/m4/turn.py`. `engine/m7/instruments.py` gained a dedicated
`guard_proximity(s)` instrument at **defect** severity (the one
`output_check` family that is a live fabrication risk, not cosmetic/
register) - excluded from `unread_outputs()`'s own generic
`output_defects`/review bucket so the same finding isn't reported twice
at two different severities.

**Known, accepted limits, named not hidden** (report-only, human-reviewed,
never a block, per R14, same as every family in this module): a decline
phrased outside `GUARD_MARKERS`' own register (e.g. "we don't say" vs.
"does not say") may not be recognized as declining; a paraphrase avoiding
the guard's own specific words may not be caught. This is a second net
alongside `grounding_net`'s own check, not the only one.

39 new tests (7 in `test_output_check.py`, 1 dedicated in `test_audit.py`,
the rest incidental). Full suite 564/564; `staleness-check` and
`engine.m9.cli check` both clean, **no repin needed** - none of the three
touched files are part of any world's compiled package bytes;
`retrieval_bench.py` unaffected (1154, unchanged).

**Stage 4b is now done** - Build-Plan.md's own line ("guard_proximity
family... Feeds R14") is fully built. R14 itself (Rulings-Pending.md) was
already ruled CLOSED (Decision-Log.md Entry 3): an output-side check may
never remove a sentence, only report - which this family, like every
other in `output_check.py`, already does by construction.

**Entry 28 — 2026-09-21.** R19 ruled: **extend fleet-wide, each world's
own voice, folded into the standing build-cycle discipline, existing gap
worlds retrofitted.** Mark's direct ruling, after two corrections to the
question as first posed:

1. R19's own title and body in Rulings-Pending.md were wrong. They named
   this a "don't recommend outside help" guard clause. The real mechanism
   (don's own `voice_craft.guard` text, and `observe_outside_help_guard`'s
   docstring) is a prohibition on the Representative comparing or
   minimizing a participant's disclosed distress against the world's own
   historical suffering ("not the same weight as our martyrs") - it never
   directs a Representative toward outside help or any language outside
   its own world and period. The actual redirect stays Facilitator-only
   per CLAUDE.md's Safety comes first section, untouched by this ruling
   either way. Rulings-Pending.md's R19 entry renamed and reworded to
   match (commit `4f2881af`, branch `transparency-engine-r19-title-fix`).
2. "Extend fleet-wide" does not mean identical text pasted into every
   world - each world authors its own version in its own idiom, the same
   Representative-voice care any `voice_craft.guard` edit requires. What's
   decided once, fleet-wide, is that every world must have *some* honest
   version of this protection - not what it says.

**Scope of the ruling, three parts:**
- **Retrofit now:** the 9 worlds Stage 0e's observation found missing it
  - alx, cappadocian, desert, gallic, hal, ijc, pahc, syr, witt (don and
    rzg already carry it). This is Representative-voice authoring, not a
    mechanical edit - per Build-Plan.md's own escalation-category list,
    still needs its own pass per world, not done in this entry.
- **Standing build-cycle requirement, going forward:** every future
  world's Representative-voice construction (Doc_07 / `voice_craft`)
  must consider and resolve this, the same way it already resolves
  readability and source-fidelity requirements - so the next worlds built
  don't reopen the same gap by omission.
- **Enforcement mechanism, deliberately left open:** `observe_outside_help_guard`
  today is a keyword scan tuned to don's own specific phrasing
  ("measured against" / "weigh" / "not the same weight" / "weighing") -
  reliable for confirming don's exemplar, not reliable as a pass/fail gate
  once 15+ worlds each express the same principle in their own genuinely
  different words (a real risk of false "missing" reports on a world that
  handled it correctly in different language). Promoting it to an
  automated gate is further engineering, not ruled on here. Until then,
  fold it into the build-cycle discipline as a required manual
  check-off, not an automated block.

**Entry 29 — 2026-09-21.** Ten more rulings landed in the same session,
one at a time per CLAUDE.md's own ground rules (real options, a
recommendation, never a flat conclusion). Rulings-Pending.md's own Status
lines updated in the same edit as this entry. All ten followed the
recommendation already on record in Rulings-Pending.md unless noted.

- **R5** (Table-mode interrupt affordance) ruled **(a)** - a mid-round
  participant message simply closes the round and proceeds; no dedicated
  Interrupt button built.
- **R6** (register-drift scope and gating) ruled **(a) and (iii)** - only
  the source's own original words stay exempt from register screening,
  our own retellings are screened; the Stage 2c ceiling proposal
  (`story.tellable_as` longest sentence <=30 / median <=25 words;
  `term.quick_meaning` longest sentence <=20 / median <=16 words) goes
  advisory for one build cycle, then promotes to a gate.
- **R7** (fixing the fleet's already-drifted `tellable_as` text) ruled
  **(a)** - a capped-round Sonnet revision pass per affected world (5
  flagged by R6's own ceilings: cappadocian, don, gallic, rzg, witt).
  Cleared by R6 landing in the same session; not yet executed.
- **R8** (CLAUDE.md naming a confidence level, "Not Attested," the code
  doesn't have) ruled **(c)** - CLAUDE.md gets corrected to describe "Not
  Attested" as an absent-claim marker (`honest_limit`/`absent_detail`),
  not a sixth `formation_confidence` value. CLAUDE.md itself not yet
  edited.
- **R9** (a distinct mark for contested/thin-evidence claims) ruled
  **(a)** - proceed with the design already agreed before this sequencing
  gate: a quiet hollow-glyph variant of the existing citation mark, no
  new color, no new verb. Unblocked by the Stage 1 measurement (Entry 13)
  plus R16/R17, both ruled in this same entry.
- **R10** (citation mark placement) ruled **(c)** - first sentence for a
  witness quote, end-of-run for a story; a repeated re-citation gets the
  lighter "ibid" glyph either way. Unblocks Stage 3c's renderer
  switch-on; label copy is still a separate remaining step before that
  flag flips on.
- **R12** (what "library accessed live" means) ruled **live resolution
  only** - citations and evidence resolve live against the vendored
  records, as already built; no live full-text architecture. Fixes an
  overclaiming topology sentence, no engineering change.
- **R13** (should the holdings "unused source" check block a world from
  shipping) ruled **report-only for one build cycle, then promoted to
  blocking for new worlds** - lets the real distribution surface before
  the bar is set.
- **R16** (fleet-wide "draft" status and confidence display) ruled **(c)**
  - confidence display draws only from the confidence field, never
  `status` (ruled now, unblocking); per-world status-promotion passes
  happen as each world comes up for its next real touch, not as a
  dedicated fleet-wide project.
- **R17** (hard budget on transparency elements per screen) ruled
  **approved as a house rule** - a small capped number of inline marks
  per turn (scaling gently with sentence count), one collapsed references
  line instead of a scattered list, no new mark types beyond R9's
  hollow-glyph variant, the unverified-claims count never rendered to a
  participant - enforced by an automated test, plus Mark's own
  read-through as a seeker with no background before Stage 6 ships.
- **R18** (onboarding text overclaiming the honesty check) ruled **(a)** -
  reword now to describe what the mechanism actually does (word-overlap
  checking against the source record, not truth-verification); doesn't
  wait on Stage 1's measurement or on Stages 6-9. Copy not yet edited.

**Net effect:** every ruling in Rulings-Pending.md that was PENDING or
sequencing-gated at the start of this session is now RULED. Remaining
CLOSED items (R1-R4, R14, R15) and already-RULED items (R11, R19) are
unaffected. What's left is execution, not decision: R6's ceilings need
promoting from proposal to enforced numbers after one cycle; R7's revision
pass, R8's and R18's copy edits, R9's hollow-glyph mark, and R10's citation
placement fix are none of them built yet; R13's holdings check needs its
report-only cycle; R16 and R17 unblock Stage 6 scoping, which has not
started. Stages 6-9 remain the largest actual remaining work in
Build-Plan.md - now unblocked by ruling, not yet built.

**Entry 30 — 2026-09-21.** R13's report-only cycle started: fleet-wide
holdings baseline captured, `engine.m9.holdings` run for all 11 built
worlds (alx, cappadocian, desert, don, gallic, hal, ijc, pahc, rzg, syr,
witt - `fix` excluded, permanently out of scope) and saved as
`engine/m9/reports/holdings-cycle-1-2026-09-21.json`. No code change -
`holdings_for`/`report` (engine/m9/holdings.py) and the `engine.m9.cli
holdings <world>` command were already built exactly report-only, per
Stage 2d's own bar; this entry is the cycle's own dated start, the thing
R13's ruling itself waits on before a blocking bar can be set for new
worlds.

Same 138 vendored files fleet-wide (the shared corpus), classified
differently per world's own scope. The number R13's ruling actually
turns on - in-scope but not drawn on ("not yet assessed" + "in scope,
unread") - varies widely: witt (3) and rzg (11) sit lowest, gallic (77)
and alx (76) highest. gallic's 19 "not yet assessed" matches Build-Plan.md
Stage 2d's own Done-bar citation ("19 unopened volumes") exactly, cross-
confirming the count.

| World | Unused, in scope | Drawn on | Total in scope |
|---|---|---|---|
| witt | 3 | 10 | 13 |
| rzg | 11 | 8 | 19 |
| pahc | 14 | 13 | 27 |
| hal | 62 | 10 | 72 |
| ijc | 61 | 19 | 80 |
| don | 62 | 19 | 81 |
| cappadocian | 61 | 21 | 82 |
| desert | 69 | 15 | 84 |
| gallic | 77 | 9 | 86 |
| syr | 74 | 16 | 90 |
| alx | 76 | 13 | 89 |

**Known gap, carried forward, not this entry's to fix:** the same
COVERAGE/REGIONS/AUTHORS relocation Stage 2d's own docstring already
names (Decision-Log.md Entry 20) - `holdings.py` reuses
`engine.m1.cross_world`'s existing tables as-is, so this baseline
inherits that gap rather than resolving it.

**What "one cycle" means in practice, not ruled here, only noted:** the
natural marker is the next world admitted to the fleet after this date -
that world's own holdings check is the first candidate for R13's
blocking promotion. Nothing in the standing gate set enforces this yet;
promoting it from report-only to blocking is separate, later work this
entry does not do.

**Entry 31 — 2026-09-21.** Correcting Entry 28's own retrofit list before
starting R19's actual work: `observe_outside_help_guard`
(`engine/m1/cross_world.py`) had a real false positive, found and fixed
while beginning the retrofit, not a hypothetical one. The scan matched
the bare substring `"weigh"`, which silently matched inside rzg's own
guard text - "It does not give him the felt **weigh**t of either" -
honest-thinness prose about doctrine, with no distress-comparison content
of any kind. Read directly
(`records/rzg/voice_craft/rzg.craft.theophilus-voice.md`): rzg's guard
never mentions martyrs, weighing, or comparison at all. Fixed with a
word-boundary regex (`\bweigh(?:s|ed|ing)?\b`), which cannot match inside
"weight"/"weighted"/"outweigh" while still catching "weigh"/"weighs"/
"weighed"/"weighing" as their own words. Three new tests pin this
(`engine/m1/tests/test_cross_world.py`): the false positive itself, a
real match still firing, and the real fleet's corrected state.

**The corrected finding: don is the only one of the 11 built worlds whose
guard actually carries this language.** Entry 28's "9 worlds" retrofit
list (alx, cappadocian, desert, gallic, hal, ijc, pahc, syr, witt) is
short one world - **rzg needs the retrofit too**, same as the other nine.
R19's own ruling (extend fleet-wide, each world's own voice) is
unaffected by this correction; only the list of which worlds still need
it changes, from 9 to 10. Rulings-Pending.md's R19 entry updated in the
same edit to carry the corrected list.

**Entry 32 — 2026-09-21.** Tech-Readiness Package 2 (Operations,
`Ministry/Operations/Audits/Tech-Readiness-2026-09/P2-Operations/Report.md`)
inventoried the full divergence between `main` (`c9b09ea1`) and `live`
(`e693b048`) ahead of the next promotion: this workstream's own Stages
0a–4b above (Entries 4–27) are on `main` only, `live` predates all of them
(`live`'s own copy of this Decision-Log had 3 entries at that report's own
time of writing). `live` separately carries atlas-sync tooling and the
who-is-at-the-table card redesign (PR #346) that never made it back onto
`main`. That Operations report's own finding, for this workstream's record:
a plain `main` → `live` promotion would risk the merge resolving
`engine/m2/`, `engine/m6/`, and `cic-website/` toward `main`'s side, silently
reverting the card redesign and atlas tooling in production, since `main`
doesn't have either. The report's proposed fix is a reconciliation PR
(bringing `live`'s own atlas/card work onto `main` first) before the real
promotion — drafted, not performed, and outside both this workstream's and
that Operations package's own hard-rule scope, so it is handed to Mark to
assign rather than claimed by either. No file in this workstream's own
directories beyond this one entry was touched by that report. (Numbered 32,
not 28 as that report's own branch first drafted it, then 30 after its
first merge — this workstream landed Entries 28–31 above concurrently with
that report's own work across two separate merges; renumbered each time
per this file's own "never renumber a past entry" rule, which binds the
later arrival, not the entries already on `main`.)

**Entry 33 — 2026-09-22.** Mark's direct instruction, this session:
Entry 32's "PR 1" (the reconciliation PR) is **assigned to this
workstream** — the next thread picking up Stage 5+ (or a dedicated
interstitial session, project lead's call) should treat it as the first
item ahead of further Build-Plan.md stages, since `main` → `live`
promotion readiness (Tech-Readiness Package 2's own scope) is now blocked
on it. Scope, unchanged from `Ministry/Operations/Audits/
Tech-Readiness-2026-09/P2-Operations/Report.md` §2, restated here so this
workstream doesn't have to cross-reference an Audits document to act:

- Merge (or cherry-pick, if history conflicts make a merge messy)
  `live`'s own atlas-sync tooling (`engine/m2/site_cli.py`,
  `engine/m2/site_compiler.py`, `engine/m6/atlas_html.py`,
  `engine/m6/census_atlas_sync.py`, their tests) and PR #346's
  who-is-at-the-table card redesign (merge commit `e693b048`) onto `main`.
  This is a normal feature PR into the integration sandbox, not a
  promotion — it does not touch `live`.
- **Verify on `cic-engine-staging` before calling it done:** the Atlas
  page and `world-census.json` sync render correctly, the card redesign
  displays as it does today in production, and Stage 4a's own fleet
  migration (PRs #360/#361, already on `main`) isn't clobbered by the
  reconciliation — run `retrieval_bench.py` and `engine.m9.cli check`
  after; expect no change from `main`'s current baseline (1154 grounded,
  0 empty per Entry 26).
- A handful of `Ministry/Features/*` docs (Backend, Brand-Messaging-Rework,
  Built-World-Voice-Alignment, Front-End-Integration-Strategy,
  Representative-Modes) differ between `live` and `main` too — the
  Operations report did not distinguish genuinely-live-only content from
  content that merely moved during `main`'s own repo-structure-cleanup
  phases 2/3, and flagged this for whoever runs this PR to eyeball, not
  as pre-cleared safe.
- Confirm before merging that `records/worlds.yaml` still doesn't carry
  `lpc` and `packages/lpc/` still doesn't exist (Entry 32's own check) — if
  either has changed, stop and ask Mark rather than merging.

Once this lands and is verified on staging, the actual `main` → `live`
promotion (Report.md's own "PR 3") is Mark's own act under the Promotion
Runbook — not this workstream's to perform.

**Entry 34 — 2026-09-21.** R19's retrofit written into all 10 gap worlds
(alx, cappadocian, desert, gallic, hal, ijc, pahc, rzg, syr, witt) -
`voice_craft.guard` in each now carries an honest, per-world version of
don's own distress-minimization line.

Drafted first as an Artifact
(`https://claude.ai/artifact/4TFs1MTvHRPhM2JsVCMxoz`), read directly from
each world's own `identity`/`characteristic_concerns`/`guard` fields
rather than a shared template, per Mark's own real-time editing across
five rounds:

1. First draft read as AI-generated - reaching for cadence ("we do not
   have that scale, and we do not build one") instead of stating the
   rule plainly.
2. Second pass cut the cadence but kept it in a third-person, legalistic
   register ("a participant's own trouble is not weighed against...").
   Mark's own line replaced it: "we have found everyone has trouble and
   we don't compare them to each other" - adopted as the shared spine
   for all ten.
3. Third pass cut remaining AI tells: a hedge-opener ("we have found
   that"), em-dash appositives, a poetic triplet ("one cost, paid
   once"), and a literary metaphor ("hostile crown") standing in for a
   plain historical fact (syr: "under a hostile crown" -> "under Persian
   rule").
4. Fourth pass, a real content fix, not a register one: rzg's draft had
   drifted into disclaiming what the world wasn't ("we keep no list of
   martyrs, we do not invent one") - announcing an absence nobody asked
   about. Cut, per the same house rule every other `voice_craft` record
   already follows (`gate_no_build_attribution`'s own `identity`/`guard`
   scan aside, this is the "honest-limits" convention itself: a gap is
   named only where a question actually reaches for it, never
   pre-declared - alx's, desert's, and gallic's own flavor_notes all
   state this rule directly).
5. Fifth pass: Mark's own read caught two remaining sentences that
   explained rather than stated - desert's "no one asks us to die for
   the faith anymore, so our struggle stays inward" (reasoning the guard
   doesn't need) and rzg's naming detail ("a pastor was killed in the
   war..."). Both cut for the same reason: irrelevant to the rule
   itself. witt's parallel trailing sentence ("two young men died once
   for what we believe") was cut the same way once the pattern was
   named.

**Final shape, all ten:** two short sentences. "Everyone has trouble. We
do not compare a person's trouble to [what this world's own record
holds]." No elaboration, no reasoning, no disclaimer of absence.

| World | Addition |
|---|---|
| alx | "...We do not compare one person's trouble to another's." |
| cappadocian | "...We do not compare a person's trouble to our martyrs." |
| desert | "...We do not compare a person's trouble to ours." |
| gallic | "...We do not compare a person's trouble to our own hardship." |
| hal | "...We do not compare a person's trouble to what we gave up." |
| ijc | "...We do not compare a person's trouble to the costs in our record." |
| pahc | "...We do not compare a person's trouble to what a death for the name cost us." |
| rzg | "...We do not compare a person's trouble to the one death in our record." |
| syr | "...We do not compare a person's trouble to what our people went through under Persian rule." |
| witt | "...We do not compare a person's trouble to our one martyr story." |

Each appended to the end of that world's existing `guard` field, not
replacing any of the existing honest-thinness content already there -
same pattern don's own guard already uses (floor line, then "one more
line" on this specific concern).

**Verified before commit:** all 10 files parse as valid YAML (rzg's and
syr's single-quoted blocks correctly carry the new apostrophes as `''`).
`engine.m1.fk.fk_grade` on every new `guard` field: 5.7-9.04, well under
`FK_CEILING` 10. `gate_no_build_attribution`, `gate_readability`,
`gate_voice_craft_prompt_budget`: 0 findings on all ten. `gate_voice_
perspective` found 2 pre-existing findings (cappadocian, syr) in
unrelated `doctrinal_witness` records this edit never touched - not a
regression. `observe_outside_help_guard`'s own keyword scan still shows
only don as "carries" - expected, not a bug: the new text is
deliberately worded differently from don's own phrasing (Mark's own
plain-language direction, not the scan's exemplar vocabulary), exactly
the scan's own documented limitation (Entry 28's "Enforcement mechanism,
deliberately left open" note). Verified all ten by direct read instead.

**Not done here:** recompile and re-pin the affected worlds' packages
(`engine.m2.cli build`, one manifest per world, referencing this entry's
own commit) - separate, standard next step, matching every prior
voice_craft revision in this project's own history. Folding this
requirement into the standing build-cycle checklist for future worlds
(Entry 28's second scope item) is also still outstanding.

**Entry 35 — 2026-09-22.** Stage 6 begins. Mark's own converged, ordered
build plan (6a-6f), display design already fixed by R8/R9/R10/R16/R17
(merged #390) - one PR per sub-stage, only participant-facing words
escalated to Mark. **Announcing 6a's own promotion sweep here first, per
Mark's own sequencing instruction, so P3's gate run sequences after it -
not yet run as of this entry.**

**6a's exact mechanism, verified against real code before running
anything (not assumed):**

- **"Sits in an admitted world's currently pinned package"** =
  `record["id"]` appears in that world's currently-pinned
  `compiled/repository.json`. Verified precisely on alx: 197 records
  under `records/alx/`, 179 in `repository.json` - the 18-record gap is
  exactly `facilitator_brief` (1) + `search_record` (16) + `world_front`
  (1), the three record_types `engine/m2/builders.py`'s own
  `_PACKAGE_EXCLUDED_RECORD_TYPES` names. Every other type - quote,
  figure, voice_craft, term, story, etc. - is in `repository.json`
  fully, confirmed by a direct type-count comparison, not assumed from
  the builder's own docstring.
- **"Passes every m1 gate"** = the record's own id does not appear as
  the subject of any finding from `engine.m1.gates.run_all(records,
  load_fleet_records(), registry)`, across all 19 gates, called the
  same way `engine/m9/enforce.py`'s own `collect_findings()` calls it
  (per-world `records`, fleet-wide `_fleet` records, NOT a
  `{world_key: records}` nesting - a first attempt at this got that
  wrong and produced 244 false findings on alx alone; the corrected call
  gives 0, matching every gate this workstream has already run clean on
  alx this session). **This ignores `engine/m9/enforce.py`'s own
  `ACCEPTED_OPEN` waivers entirely, on purpose** - a waiver keeps CI
  green while a known defect is pending fix; it does not certify the
  specific records behind it as ready for confidence display. Verified
  on don: `gates.run_all` reports 52 reciprocity findings (matching
  `ACCEPTED_OPEN`'s own recorded `m1:reciprocity/don` count exactly)
  naming 25 distinct records - those 25 stay draft under this rule,
  waiver or not.
- **Promotion rule:** for every record currently `status: draft` in an
  admitted world, flip to `ready` only if both hold; leave everything
  else untouched. Never assign `frozen` (not this pass's decision to
  make). Records of the three package-excluded types are structurally
  never eligible (they never sit in the package at all).
- **After flipping:** `engine.m2.cli build <world>` (fresh package),
  `engine.m2.cli determinism-check <world>`, then repoint
  `records/worlds/<world>.yaml`'s `package.manifest_hash`/`location` at
  the new package - the exact sequence Entry 34's own package-rebuild
  fix already validated works cleanly for a records-only change.

Mechanical execution (11 worlds, the actual status-flip + rebuild loop)
delegated to a Haiku subagent per Mark's own instruction, following a
script written and reviewed here first rather than left to the
subagent's own judgment, given what this directly feeds (the live
confidence display). Counts per world follow in a later entry once run.

**Entry 36 — 2026-09-22.** 6a's sweep run (PR #394): 2033 records
promoted draft -> ready across the 11 admitted worlds, exactly matching
the script's own dry-run counts from Entry 35's design (no drift between
plan and execution).

| World | Promoted | Draft before |
|---|---|---|
| alx | 179 | 197 |
| cappadocian | 275 | 278 |
| desert | 182 | 200 |
| don | 211 | 248 |
| gallic | 193 | 199 |
| hal | 162 | 175 |
| ijc | 158 | 186 |
| pahc | 147 | 162 |
| rzg | 108 | 110 |
| syr | 167 | 187 |
| witt | 251 | 252 |
| **Total** | **2033** | |

don's remaining 25 draft-and-flagged records (52 gate findings behind
them, matching `ACCEPTED_OPEN`'s own recorded `m1:reciprocity/don`
count) stay draft, waiver or not - the rule from Entry 35 applied
exactly as designed, not loosened at execution time. The smaller
flagged counts in cappadocian (1), desert (1), gallic (3), pahc (2),
and syr (1) were likewise left untouched.

Each of the 11 worlds' packages rebuilt (`engine.m2.cli build`),
determinism-checked, and repinned
(`records/worlds/<world>.yaml`'s `package.manifest_hash`/`location`).
Verified: fleet-wide `engine.m2.cli restore` -> `pass: true` (all 12
worlds), `staleness-check` -> `pass: true`, `python -m pytest
engine/api/tests -q` -> 130 passed. A diff scan confirmed every
`records/` change in this PR is exactly a `status: draft`/`ready` flip
inside the record's own frontmatter block - no body-prose content
touched anywhere, and no `frozen` status assigned anywhere (not this
pass's decision to make, per Entry 35).

Mechanical execution (script run, per-world build/determinism-check/
repin/restore loop) ran on a Haiku subagent as Entry 35 said it would,
against the script written and reviewed there first. Its report was
independently re-verified against the actual repo state before this
commit - not taken on trust - via a direct re-run of `restore`,
`staleness-check`, and `pytest`, a `git status` file-count check, and
the diff scan above. PR #394.

**Entry 37 — 2026-09-22.** Stage 6d's engineering half built: a new M7
instrument, `level1_element_density`, counting Level-1 (inline,
directly-in-text) transparency marks per turn. Report-only, no cap
enforced - per `Adjusted-Design.md`'s own N2 note, R17 splits into
"RULING R17 on numbers" (still Mark's to set) and engineering (this).
(Numbering note: PR #395, Stage 6b/6c work carrying Entries 37-38, was
opened before this one but is still pending Mark's wording as of this
entry - branched from `main` before either landed, so this entry is
also 37 here; whichever PR merges first keeps its numbers per this
file's own "never renumber a past entry" rule, the other renumbers on
merge, same as Entry 32's own precedent. Resolution, logged in the
entries immediately below rather than edited here, since a past entry
is never rewritten: this PR (#397) merged first, so it keeps 37; PR
#395's own Entries 37-38 renumber to 38-39.)

`engine/m7/session_reader.py`'s `VoiceTurnRecord` gains `figures_used`,
`glosses`, and `transparency`, lifted verbatim off the `voice_turn`
event's own payload - same pattern `citations` already used.
`engine/m7/instruments.py`'s new `level1_element_density(s)` counts,
per turn: story/witness citation marks (grouped by the SAME
`run_start_sentence`/`run_end_sentence`/`record_type` logic
`VoiceTurnBody.tsx`'s `renderFromTransparencyPlan` uses, reproduced
independently in Python - a known, named limitation, not a shared
implementation), figure marks, and gloss marks, against the turn's own
sentence count. Wired into `run_all()` under its own key, metrics only
(same shape as `register_mechanical`'s own metrics half) - no Finding
objects, nothing enforced.

2 new tests (grouping fidelity against a constructed transparency
plan; confirmation this stays report-only). `engine/m7` suite 34/34;
full suite 832/832.

**Still open, not guessed at here:** the actual cap number/formula.
R17's own ruled text ("a small, capped number of inline marks per
turn, scaling gently with sentence count") is deliberately
unspecific - no formula or drop order is decided anywhere in
`Rulings-Pending.md` or this log. A specific formula
(`max(3, min(8, ceil(sentences/2)))`) and drop order
(glosses→figures→stories, never witness quotes) existed only in this
session's own pre-compaction working notes, not in anything Mark
actually ruled - flagged rather than built against, the same
discipline Entry 40 (PR #395, renumbered per the note below) applied
to Stage 6c. Mark's own number, once set, is what the renderer
fixture test (R17's other engineering half) will assert against; that
test is not yet written. PR #397.

**Entry 38 — 2026-09-22.** R17's cap number confirmed and enforced:
Mark's own direct answer this session - cap = `max(3, min(8,
ceil(sentences/2)))`, drop order glosses -> figures -> stories, witness
marks never drop. `VoiceTurnBody.tsx`'s `renderFromTransparencyPlan`
(the anchor-driven renderer, still behind the still-default-off
`VITE_TRANSPARENCY_ANCHOR_RENDERER` flag) split into two passes: pass
1 detects every candidate Level-1 element in document order without
rendering, so the cap applies against the full-turn total before any
single mark is decided; pass 2 renders using pass 1's own detection.
The legacy renderer, still the live default, is untouched - out of
scope, being retired by Stage 6e's own flag flip rather than extended
here.

**Real bug caught before it shipped:** the original single-pass code's
own "every word mark counts as already-shown-inline" line, ported
forward naively, would have blanket-added every DETECTED word mark -
including ones the cap just dropped - into the set General References
checks against, wrongly excluding a dropped mark from both the inline
text and General References at once. Caught and removed before commit,
not after.

2 new tests prove the mechanism actually engages on a seeded over-cap
fixture, not just that it doesn't regress under-cap behavior (every
prior fixture already happened to sit under the floor of 3, so those
stay provably identical). One, in the course of writing it, exposed a
real pre-existing gap: this test suite has no `afterEach(cleanup)`
wired up anywhere, so a document-wide `getByText` query can collide
with an earlier test's still-mounted DOM - fixed locally by scoping
the new test's own query to its own render container, not by touching
the shared test setup (out of this PR's own scope; the gap itself is
worth a future look). Full suite 14/14; `npx tsc --noEmit` and `npm
run build` both clean. PR #399, merged.

**Entry 39 — 2026-09-22.** Stage 6b built: `formation_confidence` wired
into the Level 2 citation card, the mechanism R16 (Entry 29) and Stage
6a (Entries 35-36) exist to make trustworthy. (Renumbered twice on
this branch: 37 -> 38 when PR #397 landed its own Entry 37 first, then
38 -> 39 when PR #399 landed its own Entry 38 first - never editing a
past entry once merged, so each renumbering happens here, on this
not-yet-merged branch, rather than after the fact.)

The data plumbing already existed end-to-end before this entry -
`engine/m1/schemas.py`'s five-value enum,
`engine/m4/transparency_plan.py` attaching the full `confidence`
envelope verbatim to every anchor and reference card, `engine/m4/
turn.py`/`projection.py` passing it through the API untouched. Nothing
on the backend changed. Only the frontend's own read of it was
missing: `SourceCard.confidence` existed in the real API response but
was never declared on the TS type (now added, optional, so every
predating fixture still typechecks), and nothing rendered it.

New `cic-poc/frontend/src/lib/confidence.ts`: a pure five-entry lookup
(`confidencePhrase()`) from `formation_confidence` to one plain
phrase, returning null - never inventing one - for a missing or
unrecognized value, including "Not Attested" (R8, RULED c: not a
sixth `formation_confidence` value). Wired into `StoryMark.tsx` and
`WitnessMark.tsx`'s existing Level 2 content, one new line per cited
record. No new mark type, no new color - R17's own house rule ("no
new mark types beyond R9's hollow-glyph variant") reads this as
content inside an existing card, not a new disclosure element.

Phrases proposed as draft, then confirmed as Mark's own word without
change ("my drafts are approved as-is"):

| formation_confidence | Phrase |
|---|---|
| Documented | "Recorded directly in a source from the time." |
| Widely Accepted | "What historians broadly agree happened." |
| Dominant Modern Reconstruction | "The leading modern reading of the evidence." |
| Contested | "Historians disagree about this." |
| Inferential-Thin | "Based on thin evidence, mostly inference." |

9 new tests: `confidence.test.ts` covers all 5 phrases plus null/
undefined/missing-field/unrecognized-value edge cases; two new
`VoiceTurnBody.test.tsx` integration tests prove the phrase actually
renders on a real Level 2 card open (`fireEvent.mouseEnter`) and that
a confidence-less card renders no phrase line at all. Full suite
25/25; `npx tsc --noEmit` and `npm run build` both clean. PR #395,
merged.

**Entry 40 — 2026-09-22.** Stage 6c scope resolved, no code needed:
Mark's own direct answer, given a real finding before it was asked -
R9's ruled scope (Decision-Log.md Entry 29: "a quiet hollow-glyph
variant of the existing citation mark, no new color, no new verb") was
already fully built (the `.citation-mark--contested` CSS class,
merged before this session) and Stage 6b (Entry 39, PR #395) adds the
plain phrase on tap. Mark confirmed that is the whole of Stage 6c -
no further record-specific "hedge" content beyond the generic phrase.

**The finding that prompted the question, worth keeping on record:**
before asking, checked whether `confidence.divergence_note` could
safely supply any such record-specific content. It cannot -
fleet-wide, it is internal build/authoring-process commentary, not
participant content (e.g. `records/rzg/figure/rzg.figure.faber.md`:
`"This figure's own bridge_line is drawn from already-reviewed
construction documents"`; `records/rzg/doctrinal_witness/
rzg.witness.defending-the-anabaptist-suppression.md`: `"Built directly
from rzg.contested.anabaptist-schism-legitimacy's own
already-verified..."`). 1005 non-null `divergence_note` values
fleet-wide, all of the same provenance/authoring-note character on
inspection. Rendering this field to a participant would have been a
real process leak - flagged and confirmed unusable before any code was
written against it, not after.

Stage 6c is done. PR #395 merged.

**Entry 41 — 2026-09-22.** Stage 6e's "label copy" resolved and drafted:
R10 (Entry 29/671) named it as a separate remaining step before
`VITE_TRANSPARENCY_ANCHOR_RENDERER`'s default flips, but no document
anywhere (`Adjusted-Design.md`, `Build-Plan.md`, `Rulings-Pending.md`,
this log) ever specified what it referred to. Asked rather than
guessed. Mark's own answer: a first-time explainer near the ✲ mark.

Checked what existed before designing it: no "first-time hint"
mechanism exists anywhere in `cic-poc/frontend/src/` - building one
would mean a new component and new `sessionStorage`-backed state,
competing with R17's own per-screen element budget. Put that tradeoff
to Mark directly; his own direction: extend `Arrival.tsx`'s existing
disclosure paragraph (already shown once, above every transcript)
rather than add new UI - zero new component, zero new state, respects
R17's budget by construction.

`Arrival.tsx`'s own header comment states every line in its disclosure
block is carried VERBATIM from the retired Doorway screen - "this move
relocates approved prose, it does not compose new prose." One
deliberate, flagged exception: a new sentence explaining the ✲ mark
concretely (`"Look for the ✲ mark after a claim — tap it to see
exactly where it comes from."`). **DRAFT COPY, not yet Mark's own
word** - same discipline Stage 6b's confidence phrases (Entry 39, PR
#395, merged) followed at the time this was written; since confirmed
as Mark's own word without change, same as Entry 39's own phrases.

The mark itself is already live in the CURRENT default legacy
renderer, not just the not-yet-flipped anchor renderer - so this
explainer is correct and useful today regardless of the flag. The
flag flip itself is explicitly NOT part of this work - held per "flip
flag default only after their word," same as the copy above it; no
deployment config currently sets
`VITE_TRANSPARENCY_ANCHOR_RENDERER` at all (confirmed by search), so
flipping it later is a deploy-config change, not a code change.

New `Arrival.test.tsx` (no test file existed for this component
before): one test pinning the explainer sentence renders. Full suite
13/13 on this branch (cut from `main`, lacks Stage 6b's own tests -
expected); `npx tsc --noEmit` clean.

**Sentence confirmed as Mark's own word without change** ("my drafts
are approved as-is") - the same confirmation that landed Entry 39's
phrases. PR #398 merging.

**Entry 42 — 2026-09-22.** R16 correction: Entry 29's R16 wording is
superseded by Mark's direct ruling today. Entry 29 ruled part (b) now
(confidence display draws only from the confidence field, never
`status`) and left part (a) - a per-world promotion pass - for "each
world as it comes up for its next real touch," not as a dedicated
fleet-wide project. **That sequencing is superseded.** Mark's ruling
today: **promote by admission now, fleet-wide**, not deferred per-world.

**What "ready" means, stated as a mechanical test, not a judgment call:**
a record is ready when (1) it sits in an admitted world's currently
pinned package - concretely, `records/worlds/<code>.yaml`'s `state` is
`admitted` and `engine.m2.checks.staleness_sweep` reports that world
`stale: False`, so the pinned package's manifest actually reflects the
record as it stands now - and (2) it passes every M1 gate -
`engine.m1.gates.run_all` produces no finding that names that record's
own id, across all twenty gates in `gates.GATES`. Both conditions
mechanical, no new judgment introduced beyond what the gate battery
already renders. `status` stays pure workflow bookkeeping either way
(Entry 29's part (b), unaffected, re-confirmed by this entry): grepped
`engine/m4/evidence.py`, `engine/m4/transparency_plan.py`, and
`engine/m4/turn.py` for any read of a record's `status` field feeding
confidence display - none exists; `formation_confidence` is the only
field the participant-facing path ever consults. Promoting `status`
fleet-wide changes no participant-visible behavior by itself.

**Fleet-wide gate run, done before this entry lands** (all 11 admitted
worlds: alx, cappadocian, desert, don, gallic, hal, ijc, pahc, rzg, syr,
witt), confirms every one is `stale: False` - each world's pinned
package already matches its current records, so condition (1) holds
fleet-wide already, with no rebuild needed. Condition (2) does not hold
uniformly: **six of the eleven worlds have live M1 gate findings** naming
specific records - `reciprocity` (desert 2, don 50, gallic 11, pahc 3, a
relations-declared-one-way-only defect, pre-existing and unrelated to
this ruling) and `voice-perspective` (cappadocian 1, syr 1, a
~70%-precision outside-vantage-phrasing heuristic). Those named records
do not promote in this pass; every other draft record fleet-wide does.
Exact counts land in the next entry, once the sweep that applies this
ruling has actually run.

**This entry is also the required announcement, ahead of running that
sweep**, per Mark's own instruction: the Conversation & Transparency
Engine's `records/` are about to be touched fleet-wide (a `status` field
flip only, on ~2,100 files, no other field touched), and a separate
Fidelity-Gate package is expected to be touching `records/` after this
lands - sequencing this sweep's own PR first, and landing it before that
package's fleet run starts, avoids the two threads racing the same
files.

**Entry 43 — 2026-09-22.** Correction to this entry's own original text
below: it reported the Entry 42 re-sweep as landed. It had not. The
re-sweep was run against this branch and produced 2,126 promotions, but
those changes were withdrawn from PR #390 before merge, on Mark's direct
ruling, and never reached `main`.

Stage 6a's own sweep (Entry 36, PR #394) had already landed on `main`
before this branch's re-sweep could reach it. Mark ruled 6a's own
operational rule - a record is ready once it sits in an admitted world's
currently pinned package and passes every M1 gate, no other condition -
as R16's actual operational form. Stage 6a's sweep is the sweep of
record: 2,033 promoted `draft` -> `ready`; **161 held** - 130
never-packaged types, 31 with open M1 gate findings. Those 161 held
records stand.

No record or package file changes ship in PR #390.

**Entry 44 — 2026-09-22.** R18 correction: PR #383's reword (this same
day, Entry 29 - "we compare its wording against those same records to
catch anything that doesn't trace back to them... What the records don't
cover, it's built to tell you it doesn't have") is itself superseded by
Mark's direct ruling on the exact replacement text. `SYSTEM_NATURE`
(`engine/m4/facilitator_turns.py`) now reads, verbatim as ruled:

> Before you see an answer, each claim in it is checked to make sure its
> words come from the record it names. The record itself was checked
> against the sources when the world was built. Where the record is
> silent, the voice is built to say so, not to fill the gap.

Two things this version adds that PR #383's did not: the record's own
fidelity provenance ("checked against the sources when the world was
built" - the mechanical claim `CLAUDE.md`'s Source fidelity section
already makes, now stated to the participant too) and a single sentence
covering both what PR #383 held in two ("What the records don't cover,
it's built to tell you it doesn't have, not to invent" folds into "Where
the record is silent, the voice is built to say so, not to fill the
gap").

`cic-website/about.html`'s "How It Works" section, participant-facing
copy in the same honesty register, corrected to match: "We check every
quotation and claim in that record directly against those sources, and
label each for how well it's attested" (was "We check every claim
directly against those sources, and label it for how well it's
attested" - the same word-overlap mechanism, named more precisely:
quotations and claims are both checked, not only "claims" read broadly).

**New test, closing the gap PR #383's own test plan named:** PR #383
confirmed no test anywhere asserted `SYSTEM_NATURE`'s exact string, which
is exactly how its own wording needed a same-week second correction
without any test catching the drift either way. `engine/m4/tests/
test_facilitator_turns.py` (new) pins the three ruled sentences verbatim
and asserts the R18-defect phrasing they replaced does not reappear.
`engine/m4` and `engine/m5` suites: 437 passed (435 + 2 new).

**Entry 45 — 2026-09-22. Correction to Entry 33.** After an unshallowed
check, the reviewer thread found the real merge base is the 2026-09-20
merge of PR #327 (`20264dec`), not the stale shallow-clone comparison
Entry 32/33 were working from, and directed a plain `git merge origin/live`
into a branch off `main` instead of the reconciliation-PR approach Entry 33
described. **A merge PR does not revert live-only content** — Entry 33's
"risk the merge resolving `engine/m2/`, `engine/m6/`, and `cic-website/`
toward `main`'s side" concern does not apply to an actual 3-way merge (only
to a naive "copy specific paths from main" approach, which was never
attempted). Executed and verified:

- `cic-poc/frontend`: confirmed zero changes on `live`'s side since the
  real base — the 28-file diff against `main` is entirely `main`'s own
  independent evolution (Stage 0b/3c and others); nothing of `live`'s own
  to lose there.
- Real conflicts, resolved: `.github/workflows/ci.yml` (two independently
  added CI job blocks, unioned), `engine/m1/cross_world.py` (`live`'s
  fuller `ACCEPTED_OPEN` closure for ijc/alx/pahc/hal kept over `main`'s
  incomplete one, which had left the now-stale `census-living-flag/hal`
  waiver active), `engine/m2/builders.py` (same exclusion set, live's
  fuller comment kept), `engine/m4/facilitator_turns.py` (`live`'s docstring
  update kept — `main`'s claimed a `{display_name}` DOOR template slot that
  doesn't exist anywhere in the actual, shared, unconflicted code).
- `records/worlds/*.yaml` (12 files) and their package manifests: resolved
  toward `main`, then all 12 worlds rebuilt fresh
  (`engine.m2.cli build` + repin) rather than trusting either side's stale
  pin — `engine.m2.cli staleness-check` passes clean on all 12. Two more
  rounds of the same conflict landed concurrently while this merge was in
  progress (this file's own Entries 34 and 36 above, the R19 retrofit's
  10-world repin and Stage 6a's 11-world repin) — each resolved the same
  way and rebuilt fresh again; the third round resolved toward this
  branch's own accumulated state rather than the incoming side, to stop
  re-breaking the `hal` fix below on every fresh round of the identical
  pin conflict.
- 4 `worlds/*/Open_Gaps_Tracking.md` files (desert, gallic, hal, pahc) were
  add/add conflicts — `live` had independently created each from scratch,
  unaware of this world's own existing OG-numbered history. Unioned, not
  chosen between: `live`'s entries appended and renumbered to continue each
  file's own sequence, nothing dropped.
- 6 further add/add record conflicts, initially thought to need this
  workstream's or a build thread's own scholarly judgment (Report.md's
  original framing) — checked against the real base and found to be
  false alarms: 5 were `main` simply ahead of `live` on the completed
  Stage 4a R11 schema split (Entry 24), one was a pure line-wrap
  difference. No scholarly call was actually needed; resolved toward
  `main` (options and their outcome logged in `Ministry/Operations/Audits/
  Tech-Readiness-2026-09/P2-Operations/Decision-Log.md`).
- One real regression, caught three times, fixed three times, before any
  of the three merges committed: a whole-file "take one side's version"
  resolution of the registry files' package-pin conflict reverts whatever
  `hal.yaml`'s own `living_tradition_flag` happens to read on that side —
  a field the pin conflict itself never touches, but a whole-file pick
  clobbers regardless. Caught each time by `engine/m1/tests/
  test_cross_world.py`'s own drift check before committing, fixed each
  time, hal rebuilt again each time, full suite re-run.
- Full suite: 895/895 passing. `engine.m1.cross_world`: 0 new defects.
  `engine.m9.cli check`: clean. `tools/check_paths.py`: 0 new unresolved
  citations (2 baseline entries added for package-timestamp citations that
  went stale purely from the fresh rebuild above, one dangling citation in
  the merged `hal` Open_Gaps entry repointed to
  `Archive/Ministry-Early-Days-2026-07/Scholarly-Review/` — `main`'s own
  prior, deliberate archive move of that file, not a broken reference).

This workstream's own coordination boundary held throughout: no edits to
`engine/m4/`, `records/` content, or the frontend renderer beyond what the
merge itself brought in verbatim from `live`; the four files this entry
lists as "resolved" in `engine/m1/`, `engine/m2/`, and `.github/` are the
only hand-edited conflict resolutions, and none of them touch this
workstream's own in-flight Stage 5+/6 work. (Numbered 45, not 34, 37, 38,
39, 40, 41, or 42 as earlier drafts had it — this workstream landed its
own Entries 34–36 concurrently across two more merge rounds; five further
rounds of `main` then landed their own entries above claiming 37, 38, 39,
40/41, and finally 42–44 in turn (PR #397, PR #399, PR #395, PR #398, and
PR #390 respectively) — every one of them landing on `main` while this
branch's own merge was still open; renumbered each time on merge per this
file's own "never renumber a past entry" rule, which binds the later
arrival.)

**Entry 46 — 2026-09-22.** Stage 6f, my own half of R17's required
seeker read-through: 3 real conversation turns per admitted world (11
worlds, 33 turns total), run locally against a dev server rather than
staging (no staging access this session; per Mark's direct instruction
this stands as the read-through, not a placeholder for one on
`cic-engine-staging`) - `engine.api.app` on `:8000` (region `us-east-1`,
`CIC_ENFORCE_ADMISSION=1`) behind the frontend's own dev proxy, with
`VITE_TRANSPARENCY_ANCHOR_RENDERER=on` so the not-yet-defaulted anchor
renderer is what actually rendered every turn.

**Method:** a genuinely free-text seeker, not the starter chips - 3
varied, in-character questions per world (identity/basic, personal,
and a skeptical/outside-framed challenge), typed and sent through the
real composer, waiting for each real model response. Driven by a small
Playwright script (Chromium, 420px viewport - the participant's own
phone width) rather than by hand, so all 33 turns could run against the
same real backend in one pass; the reading and judgment on each
transcript is my own, not the script's. Captured per turn: the full
rendered text, inline mark count, contested/repeat mark counts,
General References label, and (tapping up to 2 marks per turn, 54 taps
total) the actual Level 2 card content a participant would see on tap.
Two turns (witt, rzg) hit the script's own 90s timeout under parallel
load on the first pass and were re-run individually, cleanly, right
after - a driver-script artifact, not a product one.

**Findings, all clean:**

- **No AI tells.** Scanned all 33 transcripts against a list of common
  disclaimer/hedge/assistant-voice phrases ("as an AI," "I cannot," "please
  note," "as a language model," "unverified," etc.) - one match, a false
  positive ("Augustine sent the story... as a warning:" in hal's own prose,
  a narrative use of the word, not a label). Every voice turn read as the
  world's own distinctive register - concrete, first-person, no hedging
  filler, no generic-AI flatness. The two-track hedge distinction (Stage
  6b/6c's own ground) held: Facilitator turns speak plainly from outside
  every world ("Papnoute answers only from what's actually known of this
  world, and will tell you plainly when the record runs out"), Representative
  turns never break character to hedge.
- **Confidence phrases (Stage 6b) work and read naturally in real content,**
  not just fixtures: sampled Level 2 cards actually returned "Recorded
  directly in a source from the time.", "Historians disagree about this.",
  and "Based on thin evidence, mostly inference." on real citations, each
  attached to real source attribution text, not a bare label.
- **R9's hollow-glyph contested mark and R10's repeat mark both engaged on
  real generated content** (not only Stage 6d's seeded fixture) -
  contested marks appeared in 8 of 33 turns, repeat marks in 9 of 33.
  Visually, per `app.css`'s own design (`.citation-mark--contested`: same
  color, same size, `-webkit-text-stroke` hollow rather than a new color
  or glyph): quiet, easy to miss unless looked for, never alarming.
- **R17's cap held under real pressure.** 6 of the 33 turns (all 3 of hal's,
  1 each of cappadocian/gallic/ijc) landed their rendered mark count
  exactly on the computed cap (`max(3, min(8, ceil(sentences/2)))`) -
  the densest real content this pass produced. Every one of those still
  read as complete, coherent prose with a sensible General References
  count (1-7 across all 33 turns, always the one collapsed line, never a
  scattered list) - nothing read as visibly cut short or missing a
  citation it should have had.
- **The ✲ mark explainer (Stage 6e, Entry 41) is live and correct** in
  every one of the 11 worlds' Arrival screens sampled.
- **54 of 54 sampled mark taps opened cleanly** - real Level 2 card
  content every time, zero broken taps, zero empty cards.

**One friction note, not a defect:** on the 420px viewport, a Level 2
card can visually sit over part of the paragraph underneath it while
open (the card is a positioned overlay, per `Level2Card.tsx`'s own
design) - a participant reads it as a normal tap-to-reveal popover (tap
elsewhere closes it, the text underneath was never altered), but it's
worth a look if a future pass wants the card to reflow rather than
overlay on narrow screens. Not blocking; not acted on here.

**What this does and doesn't close:** this is my own half only. Mark's
own read-through (`cic-engine-staging`, his own six-item checklist,
per his direct instruction) is separate and still his to run.
`VITE_TRANSPARENCY_ANCHOR_RENDERER`'s default stays held until both
halves are done and logged, per R17's own "before Stage 6 ever ships"
gate (Rulings-Pending.md) - not flipped by this entry.

Raw transcripts/screenshots are local scratch (ephemeral, not
committed) - this entry is the retained record.

**Entry 47 — 2026-09-22.** Seat-identity guard, built enforcing per Mark's
direct instruction (before Stage 7, its own PR).

**The finding, from Mark on `cic-engine-staging`:** a Table round (Theon,
Papnoute, Chloe; "who is jesus") produced a turn labelled Papnoute whose
text began `"The Facilitator: Papnoute has already given his witness. Let
me bring in someone who hasn't spoken yet. Theon, you named him the
Logos..."` and continued `"Theon (Alexandrian Christianity): In practice,
it meant..."` for a full paragraph - a voice spoke as the Facilitator and
as another seat, under the wrong name, uncited (zero ✲ marks on the whole
block). Confirmed pre-existing, not a Stage 6 regression: the August
live-table-battery reports already show the same defect *class* in a
milder shape - `engine/m4/reports/live-table-battery-F1-2026-08-28.json`,
probe `L4-no-foreknowledge`, Papnoute's own turn opening `"Papnoute
(Desert Monasticism): Theon has answered you rightly..."` (a seat
prefixing its OWN label onto its own turn, "cosmetic" per that report's
own framing, distinct from the constitutional-boundary breach the staging
case shows).

**Prior art checked before building anything new:** PR #10 (closed,
unmerged, 2026-08-10 - "Table: cost architecture, Haiku evidence, and the
build") carried a `speaker_label_repair.py` fix for the identical defect
family, built against the codebase's pre-`engine/`-restructure layout.
Its own measurement across six regression arms found the defect
Haiku-only at the time (Sonnet: 0/0 leading and mid-turn labels on both
its arms; Haiku: 1-12 depending on arm) and its fix was a silent
deterministic *repair* at emission, never merged, dormant pending a
Haiku go-live that never happened. Today's staging finding is on Sonnet,
in production - refutes that PR's own "table-shaped, Haiku imitating the
transcript" read as the whole story. Not revived: the old `app/` path no
longer exists, and Mark's own spec here (reject + regenerate once +
Facilitator fallback) is a materially different, stricter design than a
silent repair - kept separate rather than resurrected.

**Design, matching Mark's own spec exactly:**

1. **Detection** (`engine/m4/seat_identity_guard.py`,
   `find_seat_identity_violation`): a label - the Facilitator's own, or
   any OTHER seated voice's, both full `"Name (World):"` and bare
   `"Name:"` forms - caught at a line start or right after a sentence-
   ending punctuation + whitespace, matching exactly the shape the real
   leaks took (an attributed-transcript line opening mid-paragraph). The
   *speaking* voice's own label is never guarded against - self-labeling
   is the separate, milder, out-of-scope defect the August evidence
   already named distinctly. A bare `"<Name>:"` mid-prose false positive
   is a real, accepted tradeoff of Mark's own third pattern shape, not
   narrowed further.
2. **Reject, regenerate once, violation named:** modeled directly on
   `engine.m4.turn_selector.select_speaker`'s own retry-once-then-
   fallback shape - `engine.m4.turn._run_ordinary_voice_turn` gained an
   opt-in `guard_labels` parameter (`None` on every interview call, so
   that path is untouched, not merely undisturbed - interview has no
   other seats to impersonate and never builds the attributed-transcript
   convention this defect echoes). A catch appends a correction block
   naming the exact offending prefix to the retry's own turn-directive
   channel (`_append_seat_identity_correction`, same channel
   `_build_turn_directive` already owns, measured to win over a competing
   user-turn pressure) and regenerates once, same evidence, same history.
3. **Exhausted -> the Facilitator takes the turn:** a second catch sets
   `voice_event["text"] = ""` (the voice's text is not shown) and a new
   additive `seat_identity_guard_exhausted` flag; `engine.api.
   table_wiring._advance_open_round` reads it and appends a new fixed
   Facilitator template (`engine.m4.facilitator_turns.
   table_seat_correction_turn`, kind `seat_correction` - a new
   `facilitator_turn` kind, distinct from `TABLE_DEPENDENCY_CHECK`'s
   `"safety"`, since this is a generation defect, not a participant
   leaning on the conversation). **DRAFT COPY, not yet Mark's own word**
   - same discipline Stage 6b/6c/6e's own participant-facing text
   followed (Entries 39, 41): the mechanism ships enforcing now, per
   Mark's own instruction, with this line as its working default pending
   his confirmation of the exact words:
   > "This is the Facilitator, stepping in for a moment -
   > {representative_name}'s last answer didn't hold together the way it
   > should have, so I'm setting it aside rather than passing it on to
   > you. Ask again, or bring another voice into it - the Table is still
   > open."
4. **The voice_turn event still writes** (empty text, additive
   `seat_identity_violations`/`seat_identity_guard_exhausted` fields) -
   deliberately, not suppressed: `engine.m4.projection`'s own fold only
   advances `round_turns`/`round_speakers` on a `voice_turn` event, never
   a bare `facilitator_turn` (confirmed by reading `_fold` directly, not
   assumed) - writing nothing here would leave this seat uncounted as
   having spoken and risk the next selection immediately re-picking the
   same seat that just failed. `apply_net("")` was checked directly
   (empty in, empty/false out, no crash) before relying on it - the
   pipeline already treats a genuinely empty stream as a legitimate case
   (`StreamResult.empty`), so this reuses an existing precedent rather
   than inventing new empty-text handling.
5. **Logging - one event per catch, not one summary per turn:** a new
   `seat_identity_violation` event type (`engine.m4.events.
   REQUIRED_KEYS`/`ENUMS`), fields `round_no, position, world_key,
   offending_prefix, attempt` (`attempt`: `"first"` then, only if the
   regenerated attempt ALSO caught, `"regenerated"`) - modeled on
   `turn_selected`/`round_closed`'s own "the round's audit surface, not
   recoverable from voice_turn alone" role. `world_key`/`offending_prefix`
   /`attempt` come back from `engine.m4.turn` (which knows the speaking
   voice but not round bookkeeping); `round_no`/`position` are filled in
   by `table_wiring` (which knows the round but not the guard's own
   internals) - kept split at exactly that seam rather than threading
   round state into `engine.m4.turn`, which has no other reason to know
   it.
6. **A small, flagged addition beyond the literal backend spec:**
   `TableRoom.tsx` now skips rendering a `turn--voice` block whose text
   is empty. Without this, "the voice's text is not shown" would be
   false in practice - the seat's own portrait and name would still
   render, just over a blank body, which is still showing that seat had
   a turn. Two lines, Table-only (the interview path never produces an
   empty voice turn from this guard, since it never receives
   `guard_labels`), pinned by a new `TableRoom.test.tsx` (the screen had
   no test file before this).

**Tests:** `engine/m4/tests/test_seat_identity_guard.py` (9 cases,
including the exact staging repro text verbatim, the exact August-battery
repro text, and the self-labeling-is-out-of-scope case), a new pinning
test on `table_seat_correction_turn`
(`test_facilitator_turns.py`), and two real end-to-end integration tests
against `create_app()` with a scripted fake client
(`test_table_api.py`): one where the retry ships clean (asserts exactly
one `seat_identity_violation` event, the clean text ships, two real
stream calls were made), one where both attempts catch (asserts two
violation events with `attempt` `"first"`/`"regenerated"`, `voice.text ==
""`, the `seat_correction` facilitator turn appears in both the API
response and the store, and round bookkeeping still counted the seat as
having spoken). `engine/m4/tests` (377 total) and the Table API suite (42
total) both green; frontend `tsc --noEmit` clean, `vitest` 28/28.

**Live table battery, run once per item 4** (real, billed Bedrock calls,
`python -m engine.m4.live_table_battery --region us-east-1 --worlds
alx,desert,pahc`, report at `engine/m4/reports/live-table-battery-seat-
identity-guard-2026-09-22.json`): **0 seat-identity catches** across both
sessions (8 probes, 2 round-cap closes). Consistent with PR #10's own
old Sonnet-arm measurement (0/0) and with today's guard never having a
real violation to catch in this one run - this number is an incidence-
rate/no-regression check on a small live sample, not a correctness proof
of the guard mechanism itself (that's what the mocked unit/integration
tests above establish, by forcing a violation through). One pre-existing
probe, `L2-each-of-you`, recorded `FAIL` (a selector-behavior question -
speakers were `['desert', 'alx', 'pahc', 'desert', 'pahc']`, genuinely 3
distinct voices, so the FAIL is in the direct-address-short-circuit half
of that probe's own condition) - unrelated to seat-identity, not
investigated further here, out of this PR's own scope.

**Interview path:** confirmed untouched by construction, not merely by
absence of a failing test - `guard_labels` defaults to `None`,
`_run_ordinary_voice_turn`'s two interview call sites (`engine.m4.turn.
run_turn`) never pass it, and every new field on `voice_event` is
additive.

**Not done here, by Mark's own scope:** no change to what's shown for the
interview path's own empty-text case (pre-existing, unrelated to this
guard). No attempt to fix `L2-each-of-you`. No promotion decision - "Mark
decides whether promotion waits for it," per his own instruction.

**Entry 48 — 2026-09-22.** Mark's own half of R17's required seeker
read-through, on `cic-engine-staging` at current `main`, his own
six-item checklist:

1. **Pass.** Leave stayed available while an interview answer was in
   flight, and closed cleanly.
2. **Pass.** Leave worked mid-round at the Table.
3. **Pass.** ✲ marks present; General References opened with text.
   **Correction to this checklist's own wording, not the code:** glossed
   terms actually render as plain Tyrian-purple text with no underline
   (`.name-bridge-mark`'s own `text-decoration: none`, `app.css`) - the
   "dotted underline" description came from the original design spec
   (`CiC_Full_UX_Design_V1_0.md` §4.3-4.5, `CiC_Full_UX_Storyboard_V1_0.md`
   §2.4), never updated when the shipped implementation diverged from it.
   The CSS is identical on `live` and `main` - no drift, nothing to fix in
   code.
4. **Pass.** No `VITE_*` variables set on staging - the flag was reading
   its real, unconfigured default the whole time this checklist ran.
5. **Pass.** The Table closed after 3 rounds; the closing line said 3.
6. **Pass.** rzg: *"Hard weeks are not a contest, and I will not line
   yours up next to ours as though only the sharper suffering deserves to
   be named."*

**Two further findings from the same session, neither a checklist item:**
the first Table turn returned a 502 during a Render deploy race and
cleared cleanly on retry - an infra timing artifact, not a code defect,
no action taken. And: the seat-identity leak PR #408 (Entry 47) fixed was
seen once more in this same session, **before the guard had landed** -
consistent with Entry 47's own read that the defect is real but rare on
Sonnet, not evidence against the fix.

**Verdict: promote.** Both halves of R17's read-through are now done and
logged (mine, Entry 46; Mark's, this entry) - the last condition Entry 41
and Rulings-Pending.md's own R10/R17 entries named before
`VITE_TRANSPARENCY_ANCHOR_RENDERER`'s default could flip. See Entry 49
for that flip, done immediately after this entry per Mark's own
instruction ("log it, then begin Stage 7").

**Entry 49 — 2026-09-22.** `VITE_TRANSPARENCY_ANCHOR_RENDERER`'s default
flipped: the anchor-driven renderer (`VoiceTurnBody.tsx`'s
`renderFromTransparencyPlan`) is now what a participant sees by default,
the legacy renderer only reachable by an explicit `off` or on an older
logged turn with no `transparency` plan attached. Stage 6e (R10) is
closed.

**Gate, closed in full:** R17's own text named this as blocked on "an
automated test [Stage 6d, PR #399] plus Mark's own read-through as a
seeker with no background before Stage 6 ever ships." Both halves are now
done and logged - mine (Entry 46) and Mark's (Entry 48, verdict:
promote). No deployment config anywhere sets this variable (confirmed by
search before Stage 6f and re-confirmed here), so the flip is a code
change to `lib/flags.ts`, not a config one - nothing on `live` or `main`
needs a separate deploy-side toggle.

**The change itself, one line, same safety discipline inverted:**
`useAnchorRenderer` read `=== 'on'` (default off, opt in); now reads `!==
'off'` (default on, opt out) - a misconfigured or accidentally-empty env
var still can never silently flip participant-facing behavior, it just
now silently STAYS on the ruled-and-tested renderer rather than the
legacy one.

**Verified live, not just in unit tests** (both existing test files
mock or omit the flag directly, so neither would have caught a real
wiring mistake): local dev stack, backend and frontend, `VITE_
TRANSPARENCY_ANCHOR_RENDERER` genuinely unset in the environment - a
real turn against `alx` rendered 6 inline marks, a working "General
references (1)" collapsed line, and a populated Level 2 card on tap,
exactly the anchor renderer's own shape, with no flag set at all.

**Docs corrected alongside the flip**, not left stale:
`VoiceTurnBody.legacy-default.test.tsx`'s own docstring and `describe`
title no longer claim the flag itself defaults to legacy (it doesn't
anymore) - retitled to what the file actually proves now: the legacy
renderer stays genuinely reachable whenever a turn carries no
`transparency` plan (an older logged session, or one from before Stage
3b), independent of the flag. `VoiceTurnBody.test.tsx`'s own
cross-reference updated to match.

**Tests:** frontend `tsc --noEmit` clean, `vitest` 28/28 (no count
change - both existing suites were already exercising each renderer
directly, by mock or by omission, so the flip needed no new test to stay
covered, only the docstring correction above).

Rulings-Pending.md's R10 and R17 entries updated to note this closure.

**Entry 50 — 2026-09-22.** Two governance rulings from Mark tonight,
relayed via the reviewer thread ("CiC — Tech Review & Funding Readiness
Prep") under Mark's own standing authorization (pasted into this session
2026-09-22: that thread "speaks for me on merge orders, fix lists,
sequencing, and pass/fail verdicts... participant-facing words,
Representative identity, governance and methodology, and unresolved
tensions still go to Mark himself" - both rulings below are Mark's own
words, this entry only records them).

**R26 — may a Representative speak about another tradition, or claim a
doctrine its own world's records don't hold.** Mark's own words:

> "The representative should only know its own sources unless they would
> have known the sources from another in reality."

Ruled shape: on a first ask about another Christian tradition, if the
asked world's own records hold nothing on it, the voice answers "Our
record doesn't mention that Christian tradition." and then answers the
rest of the question from its own records. If the records do hold
something, the voice speaks only from those records, cited. The
Facilitator's existing `other_tradition` etic turn stays as the
mechanism for a second press.

**The real defect this closes**, found on `cic-engine-staging`: Theon/alx
asked "what was your relationship with the donatists." alx holds zero
records mentioning Donatists (grep-confirmed). The voice described
Donatist history uncited, and separately attributed to Alexandria itself
a sacramental doctrine no alx record holds - "what the sacrament does,
it does by Christ's power, not the minister's purity"; "even a broken
priest could not block his grace" - which is Augustine's own doctrine, a
century later than alx's own world, not alx's to claim.

**R27 — a hard requirement: every declarative claim sentence carries a
citation.** Ruled option A: every declarative claim sentence in a voice
turn must carry a citation, or be one of a short, closed allowed-uncited
list - the honest-limit sentence (R26's own form, and the world's
existing honest-limit forms), a question back to the participant, and
first-person framing making no historical or doctrinal claim.
Deterministic check, no new model call. R26's two violation shapes (a
neighbour tradition named without citation; a doctrine belonging to
another world asserted as the answering world's own, inside an
`other_tradition` turn) are violation classes inside R27's own check, not
a separate guard.

**Rollout:** report-only for one week to measure the real per-world
uncited-claim rate, then enforced with the seat-guard's own shape
(regenerate once with the violations named, then the Facilitator takes
the turn) - the same pattern PR #408 (Entry 47) already built and proved.
Mark sets the enforcement threshold once the measured rate is in.

Both rulings recorded in `Rulings-Pending.md` (new R26, R27 entries)
alongside this one. Full engineering design for R27's detection
mechanism and the build order - each item its own PR, three-round review
cap per PR - in Entry 51.

**Entry 51 — 2026-09-22.** R27 build order item 1: the detection design
for "every declarative claim sentence carries a citation, or is one of a
short allowed-uncited list" (Rulings-Pending.md R27, Entry 50). No code
in this entry - the check module itself is item 2, its own PR. Everything
below was verified against the real modules it reuses, not assumed.

**Input: reuse `engine.m4.grounding_net.check_turn`'s own per-sentence
output, not a second splitter.** `check_turn` already runs
`parse_tagged()` (the production sentence+tag splitter grounding_net.py
itself is built around - quote-balanced, tag-aware) and returns
`net_result["sentences"]`, one `{"sentence": str, "tags": list[str],
"verdict": "ok"|"withhold", "why": str|None}` per sentence. The R27
module takes this same list as input (computed once, already in
`engine.m4.turn._run_ordinary_voice_turn` before `apply_net`), not the
raw text again - two independent sentence-splitters risking disagreement
is a real correctness class of bug this avoids by construction, the same
"one implementation, owned once" discipline `claim_markers` itself
already follows. **Scoped to `verdict == "ok"` sentences only** - a
`withhold`ed sentence never reaches the participant (apply_net drops it),
so R27 has nothing to check in one that was never shown.

**"Carries a citation"** = `bool(sent["tags"])`. Simple; already computed.

**The three allowed-uncited kinds, in the order checked:**

1. **A question back to the participant** - `sentence.strip()` ends in
   `?` (trailing quote/bracket chars stripped first). Deterministic, no
   open question here.

2. **An honest-limit sentence.** Two sub-cases, both real, both
   verified:
   - R26's own new fixed sentence, exact (case-insensitive) match:
     `"our record doesn't mention that christian tradition"`. This is
     the literal directive text item 2 wires into the `other_tradition`
     first-ask path (below) - the voice is TOLD to say these words, so
     an exact match is the right bar, not a guess.
   - **The fleet's own existing honest-limit vocabulary already exists
     and is already calibrated** - `engine.prose.SCAFFOLD_MARKERS` (16
     phrases: "we do not have", "we cannot", "we will not draw one", "we
     find none of these", etc.) and `SELF_NAMING_MARKER`, the exact list
     `grounding_net.verdict_for_sentence` already uses for its own
     `"exempt: honesty scaffolding"` verdict, calibrated against 17 real
     live turns per that module's own docstring. Reusing this list
     directly is a stronger design than a new keyword set built from
     nothing: it's already fleet-proven vocabulary, not a guess at what
     an honest-limit sentence sounds like. (`evidence.py`'s own
     `honest_limit` record type is a normally-CITED record - a
     properly-generated honest-limit sentence usually already carries
     its own `[[honest_limit.id]]` tag and passes R27 on citation alone;
     this category is the safety net for the case where the voice
     paraphrases one without carrying the tag forward - a real, already-
     seen failure shape this whole workstream exists to catch.)

3. **First-person framing making no historical or doctrinal claim.**
   Sentence opens (first token, case-insensitive) with a first-person
   subject - `i`, `i'd`, `i've`, `i'll`, `i'm`, `we`, `we'd`, `we've`,
   `we'll`, `we're`, `my`, `our` - **and** `engine.prose.claim_markers
   (sentence)` returns empty. `claim_markers`'s own docstring: "empty
   result means it's interpretive/values framing - skip it outright" -
   exactly category 3's own definition, and reusing it here (unlike as
   the overall gate below) is a direct, justified fit.

**Verified finding that shapes the whole design - `claim_markers` cannot
be R27's own overall gate.** The natural first instinct is "a sentence
needs a citation only when `claim_markers` flags it as a claim" - tested
directly against the R26 motivating sentences and it fails:
```
claim_markers("What the sacrament does, it does by Christ's power, not the minister's purity.")
  -> ['proper-noun:["christ\'s"]']   # catches, but only by an accident of
                                      # the possessive form slipping past
                                      # _is_common_vocab's bare "christ" check
claim_markers("Even a broken priest could not block his grace.")
  -> []                              # MISSES - a real, uncited doctrinal
                                      # claim, zero markers
```
The second sentence is exactly the shape R26/R27 exist to catch and
`claim_markers` alone returns nothing. `claim_markers` was built for a
narrower job (grounding-ratio gating on strongly-attributable factual
claims) with a default-EXEMPT polarity ("empty means skip it"); R27's own
ruling is the opposite polarity by construction ("every declarative claim
sentence... must carry a citation, or be one of a short list"): default-
REQUIRED, narrow exemption. So the module is built as: not-a-question,
not-an-honest-limit, not-first-person-without-a-claim -> requires a
citation, full stop - never "only if claim_markers agrees." `claim_markers`
is reused only inside category 3's own narrower question, where its
actual, verified meaning ("no checkable claim") is exactly what's being
asked.

**R26's own two violation classes are caller-side labels on top of the
same base check, not separate detection:**
- `neighbour_named` - an `uncited_claim` sentence that also names another
  admitted world's own `card_name`/representative name (the same fleet
  name list `engine.api.table_wiring._labels` and
  `facilitator_turns.table_door_turn` already build from the registry -
  item 2 reuses that construction, not a new list).
- `own_doctrine_in_other_tradition_turn` - an `uncited_claim` sentence
  inside a turn routed via the `other_tradition` out-of-scope
  classification (`engine.m5.routing.PRESSABLE_CLASSES`). This is
  ROUTING context, not sentence content - the caller (which already
  knows `gate_result.routing`) attaches the class, the detection module
  itself stays pure (sentences in, offenses out, no routing knowledge).

**Routing, checked directly against `engine/m5/routing.py`'s own
`route()` before writing anything about it here - the first draft of
this paragraph guessed wrong and was corrected before committing.** The
routing shape R26 wants already exists: `other_tradition` (a
`PRESSABLE_CLASSES` member) routes to `voice_with_directive` - an
ordinary in-world voice answer - on the first ask (`route()`'s own
`reason=f"{out_of_scope_class}, first ask - in-world answer"`), and only
to the Facilitator's `etic_turn` on a second press
(`pressed.get(out_of_scope_class)`). Nothing in the routing table itself
needs to change for R26. What's actually missing: `assemble_directive`
(the function that builds the first-ask's own directive) builds a plain
directive today - asks, register note, ambiguity options - with **no
special instruction for the other-tradition case at all**, which is
consistent with how the real staging defect happened: the voice, given
no guardrail distinguishing this question from an ordinary one, answered
freely. Item 2's real work here is a new directive component (same shape
as `table_engagement`/`figures_already_named` in
`engine.m4.turn._build_turn_directive` - an additional instruction
string, not a routing change) carrying R26's own rule and its exact
fixed sentence, added specifically on an `other_tradition` first ask.

**Event shape, new type in `engine.m4.events`:**
```
"uncited_claims": {"speaker", "offenses"}
```
`offenses`: list of `{"sentence": str, "class": "uncited_claim" |
"neighbour_named" | "own_doctrine_in_other_tradition_turn"}`. **A real
gap in the existing schema, flagged for item 2:** `events.py`'s own
`ENUMS` mechanism validates `(event_type, field) -> {value}` against a
scalar payload value - it has no way to constrain a value living inside a
list of dicts. Item 2 either extends `validate()` to walk `offenses[].class`
against a closed set, or accepts this one field unvalidated at the schema
layer (relying on the module's own tests for correctness instead) -
item 2's own call, not a blocker on this design.

**Facilitator turns are never checked** - `facilitator_turns.py`'s own
templates are code-owned, never model-generated (same discipline
`output_check.py` and the seat-identity guard both already rest on); the
R27 module only ever runs on `voice_turn` text.

**Report-only in this PR, per Rulings-Pending.md R27:** item 2 writes the
`uncited_claims` event, nothing participant-visible changes. Item 4
(live battery + M8 cost-study prompts, check on) is where the real
per-world rate gets measured - the `SCAFFOLD_MARKERS`-based honest-limit
detection above is a first pass calibrated on prior evidence, not this
specific check; that measurement is exactly where a real gap in it would
show up as an inflated false-positive rate, safely, before anything
enforces.

Next: item 2, its own PR, three-round review cap per Mark's own
standing rule (CLAUDE.md, "Scaling the build").

**Entry 52 — 2026-09-22.** R27 fix list (reviewer thread, relayed after
item 4's own first live battery run, PR #417 - `live-uncited-claims-
battery-report.json`, 86% of interview turns and 100% of table voice
turns carrying at least one raw offense). The reviewer thread's own
verdict on that run: the raw rate itself is real but two real gaps in
the allowed-uncited list were inflating it, and the run's own
other-tradition probe never actually exercised R26's own routing
classification. Three fixes, one PR, three-round cap:

**F1 - the honest-limit exemption missed real fleet honest-limit
forms.** The battery's own offense list named the exact sentences: *"How
it ended among us is not in our record."*, *"Here is the honest limit."*,
*"No rule of ours survives that explains the difference."* A new closed
list, local to `engine.m4.uncited_claims` and deliberately **not** added
to `engine.prose.SCAFFOLD_MARKERS`: that vocabulary also drives
`grounding_net.verdict_for_sentence`'s own withhold/ok decision
fleet-wide, and widening it there would change more than this one
check's own exemption - the same "one implementation, owned once"
discipline this module's own docstring already argues for cuts the other
way here: two DIFFERENT jobs (a withhold gate; an uncited-claim
exemption) sharing one vocabulary would be the coupling, not the
reuse. Two shapes of fixed pattern:
- Four fixed phrases: `"not in our record"`, `"our record does not"`,
  `"our record is silent"`, `"the honest limit"`.
- A short-window regex for the "survives"/"reached us" negation shape
  the fixed phrases above don't cover (`"No rule of ours survives..."`
  names nothing "absent" by the word "record" at all): a negator (`no`,
  `none`, `nothing`, `not`, `never`) within 40 characters of `survive(s)`/
  `survived`/`reached us`/`reaches us`, same clause. Proximity-bounded
  and negation-gated on purpose - a genuine citable claim like *"The
  letter survives in three copies."* carries no negator and stays a real
  offense, pinned as its own negative-control test.

**F2 - the first-person no-claim exemption was opener-only.** A
conditional offer whose MAIN clause is first-person but whose SENTENCE
doesn't open that way - *"If you name the conflict you mean, I will tell
you plainly where our own record speaks to it and where it does not."* -
was wrongly caught: the check only looked at the sentence's first word.
Fixed clause markers (`"i will"`, `"i can"`, `"we will"`, `"we can"`),
checked anywhere in the sentence rather than sentence-initial only.
`claim_markers(sentence)` stays the real guard, unchanged - a sentence
that happens to contain one of these words while making a real claim
elsewhere (*"If you ask, we can tell you Origen taught this in the year
240."*) is still caught, pinned as its own test.

**F3 plumbing - a battery-only regeneration channel, not a production
change.** `engine.m4.turn._run_ordinary_voice_turn` gained one new
optional parameter, `correction: str | None = None`, appended onto
whatever `_build_turn_directive` already produced - same append-not-
replace shape `_append_seat_identity_correction` already uses for the
seat-identity guard's own one retry. **Unset on every real caller**
(`engine.api.wiring`, `engine.api.table_wiring` never pass it) - this is
plumbing for `engine.m4.live_uncited_claims_battery` to simulate one
regeneration naming a turn's own uncited sentences, battery-only, no
participant path (the fix list's own words), without duplicating this
function's evidence-assembly/generation logic inside the battery script
itself. A hermetic test (`test_correction_is_appended_to_the_turn_
directive_the_model_actually_sees`) proves the text reaches the model's
own system prompt; no other caller's behavior changes, since the
parameter defaults to `None` everywhere else.

**F3(a) and F3(b) - what the fix list asked the re-run to measure -
belong in that PR's own body**, per the reviewer thread's standing
convention ("the reviewer reads PRs, not this session"): F3(a) fixes the
other-tradition probe into a direct, context-free first turn of its own
fresh session (the item-4 run's own probe rode on a SECOND turn of the
same session with no history threaded between the two `run_turn` calls,
so the reader never saw a complete other-tradition question and
`out_of_scope_class` read `"none"` on every turn); F3(b) adds one
regeneration, battery-only, for every turn the raw probe caught, and
reports the post-regeneration residual rate alongside the raw one -
"that post-regeneration number is what Mark sets the threshold on; the
raw rate is not," in the reviewer thread's own words.

**Process rule, effective this entry on:** self-merging stops. A PR
opens, carries its own report in the body, and waits for the reviewer
thread's own verdict fire before it merges - PRs #414-417 are accepted
as already merged under the prior rule; every PR from here on follows
the new one.

**Entry 53 — 2026-09-22.** Stage 7a: recording the streaming design
brief, in my own words, per the reviewer thread's own instruction -
design only, no code in this entry or its PR. **A gap this entry closes
by substitution, not by finding the file:** `Build-Plan.md`'s own line
("Stages 6-9... are specified in full in the Fable design pass's own
report - ask Mark for it when `Rulings-Pending.md` starts clearing")
names a report that does not exist as a file in this repository. The
reviewer thread's own message said so directly and supplied the design
input in its place; what follows is that input, restated, not a
transcription of a document that was never actually written.

**Where a stream would have to slot in.** Today, `engine/api` returns a
whole finished turn as one JSON response; the frontend fetches per turn,
nothing sooner. `engine/provider/bedrock.py` already accounts usage
correctly for a streaming response (the SDK call underneath
`stream_voice_turn` already streams token-by-token; nothing currently
reads those tokens before the full text is assembled). The real pipeline
a stream would have to survive, in order: `engine.m4.turn`'s seat-
identity guard first (reject/regenerate/fallback on a Facilitator-label
or another-seat leak), then `apply_net` (the grounding net, per sentence,
tag-checked - this is where a sentence either streams or is withheld),
then `output_check` (report-only, R14 - reads the FINISHED text), then
the transparency plan (citations/glosses/figures, built over the whole
answer). `R17`'s own display cap is applied at render, on the frontend
side, not inside this pipeline.

**Three candidate shapes, one already rejected.**

- **Shape C (rejected outright): raw token streaming with retraction on
  a failed check.** Stream every token as Bedrock emits it, then pull
  words back if a later check (grounding net, do-not-voice, seat-
  identity) fails on them. Rejected on one ground, not weighed against
  the others: **a participant must never see words and then lose them.**
  That's not a performance tradeoff to negotiate - it's the same
  "reports, never edits" discipline `output_check`'s own module docstring
  already rests the whole net on, applied to what a screen shows in
  real time instead of what a log records after the fact.
- **Shape A: perceived streaming.** The whole pipeline stays exactly as
  it is today - one full turn generated, checked, and finished server-
  side, then handed to the frontend whole. The frontend alone reveals the
  already-checked, already-finished turn sentence by sentence, at a
  reading pace, as if it were arriving live. Zero new risk (nothing
  participant-facing changes about WHEN a check runs), but also zero real
  gain: first-word latency is unchanged, since the participant still
  waits for the full generation to finish before anything appears.
- **Shape B (recommended): sentence-gated streaming.** The server itself
  streams from Bedrock, buffers to sentence boundaries (not token
  boundaries), and runs the SAME per-sentence checks the whole-turn path
  already runs - grounding net, do-not-voice, the seat-identity prefix
  check, and, once R27 is enforced, R27's own per-sentence check - on
  each completed sentence as soon as it's complete, not after the whole
  turn. A sentence that clears is emitted immediately over a server-sent-
  events endpoint; a sentence that fails never reaches the transport at
  all (the same withhold the whole-turn path already does, just moved
  earlier). Citation marks attach at sentence boundaries, as each cleared
  sentence lands; the transparency plan still finalizes at turn end (it's
  a whole-answer artifact by design, not a per-sentence one). R17's
  display cap still enforces at turn end, and specifically **demotes a
  mark that's already been shown to the references line - it never
  deletes a mark the participant already saw**, the same "never revoke
  something already shown" discipline Shape C's own rejection rests on,
  applied to the cap instead of the net.

**Rules that hold regardless of which shape ships:**
- **Constraint A - no added tokens.** Streaming is a transport change,
  not a content change; nothing about what gets generated or said is
  different because it arrived sentence-by-sentence instead of whole.
- **Constraint B - separate, flag-gated, deletable module.** Not woven
  into the existing whole-turn path; a self-contained addition that can
  be removed cleanly if it doesn't work out, never a rewrite of what
  already ships.
- **Facilitator turns never stream** - they're code-owned templates
  (`facilitator_turns.py`'s own module docstring), not model-generated
  text arriving token by token; nothing about them benefits from or needs
  a streaming transport.
- **Nothing streams before its own sentence has passed the same checks
  the whole-turn path already applies to it** - Shape B's whole design is
  this rule moved earlier in time, not a relaxation of it.
- **Table rounds stream one seat at a time** - the selector and round
  mechanics (`engine.m4.turn_selector`, `engine.m4.round`) are entirely
  unchanged; only the chosen seat's own voice turn streams, the same way
  it already generates as one call today.
- **Flag-gated, default off, flipped only after Mark's own staging
  look** - same discipline `useAnchorRenderer`/R10 already set as
  precedent (Decision-Log Entry 49): built behind a flag, proven on
  staging, then switched on by Mark's own word, never auto-enabled by a
  merge.

**Two participant-facing choices, Mark's alone - drafted here, not
decided.** Per this file's own working rules (real options with
explanations and a recommendation, never a flat conclusion with no
alternatives shown):

**E1 - what happens mid-stream when a guard catches a violation
(seat-identity, or R27 once enforced) partway through a turn that's
already shown some sentences to the participant?**
- *(a) Keep what's shown, stop, append a Facilitator line.* The sentences
  already on screen stay exactly as they were; the stream simply stops
  there, and a Facilitator line closes out the turn honestly (something
  in the shape of the seat-identity guard's own existing fallback -
  Decision-Log Entry 47's `table_seat_correction_turn`). Simple and
  honest about what happened, but a participant reads a turn that visibly
  trails off mid-thought.
- *(b) Replace the whole turn, collapse what was shown behind a
  "withdrawn" note.* The sentences already on screen are hidden again
  behind a label saying the turn was withdrawn, and a full replacement
  (regenerated, or the Facilitator's own turn) takes its place. Never
  literally shows a participant something and then deletes it in place
  (the still-live sentences are labeled, not erased outright) - but it IS
  taking back an experience the participant already had, which is close
  enough to Shape C's own rejected shape that it deserves real scrutiny,
  not a quick approval.
- *(c) Hold the first paragraph until the guard has already seen it, then
  stream from there. (Recommended.)* Don't start streaming at sentence
  one - wait until the guard has checked at least the opening paragraph,
  THEN begin the sentence-by-sentence reveal from a point already known
  to be clean. This trades away a little of the first-word-latency gain
  Shape B exists to capture (an opening delay, not the full wait Shape A
  has), in exchange for making the catch-mid-stream case in (a) and (b)
  rare rather than routine - most of a turn's own risk concentrates in
  its opening framing, the same place a seat-identity leak or an uncited
  claim is most likely to land early. Recommended because it doesn't ask
  Mark to accept either "the participant sees a trailed-off turn" or "the
  participant sees something taken back" as the routine case - it makes
  both rare, at a real but small latency cost.

**E2 - when does a citation mark attach, during a stream?**
- *(a) With each sentence, as it clears. (Recommended.)* A mark appears
  the instant its own sentence lands, matching what the participant is
  actually reading at that moment - the mark and the claim it supports
  arrive together, which is the whole point of a mark in the first place
  (Decision-Log Entry 49's own R10 rationale: a citation is evidence
  shown at the point of the claim, not detached from it).
- *(b) All attached at turn end.* Marks wait for the whole turn to
  finish, then appear together - simpler to implement (one pass over the
  finished transparency plan, same as today), but breaks the very
  point-of-claim association (a) preserves: a participant reads five
  sentences with no marks, then five marks appear retroactively, and has
  to work backward to match each one to what it was for.
- **How an R17 cap demotion reads under (a):** a mark shown live, sentence
  by sentence, that later gets demoted to the references line once R17's
  display cap is reached at turn end is not a mark being taken away in
  the Shape-C sense - the sentence and its claim stay exactly as shown;
  only where the citation's own detail lives moves (inline mark →
  references line), the same demotion the whole-turn path already does
  today, just now happening to a mark the participant watched arrive
  live rather than one that was never shown inline in the first place.
  Worth saying to Mark plainly when this is put to him: this is the one
  place a streamed turn's own citation display can visibly change after
  the fact, even though nothing about the underlying claim or its
  grounding does.

**Build order, after R27 items 1-4 (unchanged from the reviewer thread's
own words):** 7a this entry; 7b the engine streaming module itself,
behind `CIC_API_STREAMING`, the existing whole-turn message endpoint left
completely untouched; 7c the frontend consumer, behind `VITE_STREAMING`,
built on the Stage 6 renderer only (no second renderer); 7d the seat-
identity guard and R27 moved into per-sentence mode, with tests including
the staging Papnoute leak text (Decision-Log Entry 47) run through the
streaming path specifically; 7e a live battery with streaming on,
reporting catch counts and first-word latency, then a stop for Mark's own
staging look before anything ships to a real participant. **Streaming
does not ship to participants before R27's own enforcement is on** - the
reviewer thread's own sequencing, restated here as the gate it is.

Escalating E1 and E2 to Mark now, per the four standing escalation
categories (participant-facing words) - no 7b code starts until both are
ruled.

**Addendum to Entry 53 - 2026-09-22.** Mark's own rulings on E1/E2,
relayed via the reviewer thread under his standing authorization
(Rulings-Pending.md R30/R31):

**R30 (E1): option (c).** Hold the opening paragraph until the guard has
checked it, then stream sentence by sentence from a point already known
to be clean. A mid-stream catch after that point follows the seat-guard
shape already ruled (regenerate once, then the Facilitator takes the
turn) - the 7b design entry states exactly what the participant sees in
that residual case, and anything other than the Facilitator closing the
turn with the sentences already shown left in place escalates before it
is built.

**R31 (E2): option (a).** Citation marks attach with each sentence as it
clears. An R17 cap demotion at turn end moves an already-shown mark to
the references line and never removes a sentence or a claim.

No 7b code starts yet even with both ruled - the reviewer thread's own
sequencing puts R27-A's build order (Entry 54) ahead of it.

**Entry 54 — 2026-09-22.** R27-A: Mark's own ruling that the unit of
R27's enforcement is the paragraph, not the sentence - chosen from three
options put to him after PR #419's own live numbers (86% raw sentence
rate, 84% residual after one regeneration; Entry 52's own data). Via the
reviewer thread's standing authorization. Recorded in full in
Rulings-Pending.md's own R27-A entry; restated here because this is
where the build order lives.

**Ruled shape:** a paragraph must carry at least one citation. The
grounding net checks every sentence in that paragraph against the union
of that paragraph's own cited records - an untagged sentence inside a
cited paragraph gets the SAME per-sentence check a tagged sentence
already gets, just against the paragraph's own citation set rather than
its own bare tag. A wholly uncited paragraph fails, unless every
sentence in it is one of R27's own allowed-uncited kinds. R26's two
classes (`neighbour_named`, `own_doctrine_in_other_tradition_turn`) stay
per-sentence hard failures - the paragraph unit belongs to R27's own base
check only, not to those two.

**Rollout, unchanged from R27 itself:** report-only with rates first,
Mark sets the threshold, then flag-gated enforcement with the seat-guard
shape (regenerate once with the failures named, then the Facilitator
takes the turn).

**Build order, each its own PR, three-round cap, no self-merge:**
1. Design entry - how a paragraph is delimited in the voice's raw tagged
   text (blank-line blocks, the existing sentence split running inside
   each one); how "the paragraph's cited records" is formed (the union
   of every tag appearing anywhere in that paragraph); what the
   grounding net does with an untagged sentence in a cited paragraph (the
   same per-sentence check it already runs on a tagged sentence, against
   that union instead of the sentence's own bare tag); what verdict an
   untagged sentence gets when that check fails - two named options to
   choose between and recommend, escalating to Mark only if the choice is
   participant-visible in a way he hasn't already ruled: (a) withhold the
   sentence exactly as a failed tagged sentence is withheld today, or (b)
   count it as a paragraph failure that triggers regeneration without
   itself being withheld. Constraint A holds (no new model call).
2. Report-only module change: paragraph coverage computed beside the
   existing sentence check; the `uncited_claims` event gains a
   paragraph-level shape (stated in item 1's own design entry) while the
   existing `offenses` list stays exactly as it is; the grounding net
   extended to check inherited sentences, logging its verdict without
   withholding anything yet. No participant-visible change in this PR.
3. Tests: the alx Origen paragraph from the #419 report ("For years they
   held together." inside a cited paragraph) must pass paragraph coverage
   and be net-checked; a wholly uncited narrative paragraph must fail; a
   paragraph of only honest-limit sentences must pass; the Augustinian
   sentences inside an `other_tradition` turn must still fail per
   sentence (R26's own classes, unchanged by this amendment).
4. Battery: per-world rates under the paragraph unit, raw and
   post-regeneration, plus the net's own verdict distribution on
   inherited sentences (how many would be withheld under option (a)
   above). Cost reported in the PR body. Mark sets the threshold on these
   numbers, not item 4's own sentence-level ones (Entry 52).
5. Enforcement, flag-gated, only on Mark's own word after item 4.

Sequencing for this session (reviewer thread's own words): the F4-F6 PR
already in flight finishes first, then R27-A items 1-4, then Stage 7b-7e
(streaming does not ship before R27-A's own enforcement is on).

**Entry 55 — 2026-09-23.** R27-A build order item 1: the paragraph-
coverage design, stated exactly, per the reviewer thread's own build
order (Entry 54) plus two further design points the reviewer put to
this entry directly, arising from PR #420's own live numbers. Design
only - no code in this entry or its PR; item 2 builds the module.

**1. How a paragraph is delimited.** Blank-line blocks in the voice's
raw tagged text - `engine.m4.live_uncited_claims_battery`'s own
`_PARAGRAPH_SPLIT` regex (`\n\s*\n`) already does exactly this, proven
against real live text across two battery runs (#419, #420); item 2
moves this into `engine.m4.grounding_net` itself rather than leaving it
battery-only. The existing sentence split (`quote_aware_sentences`,
`parse_tagged`'s own machinery) runs INSIDE each paragraph block,
completely unchanged - a paragraph is a sequence of the same sentences
`check_turn` already produces, grouped by which blank-line block they
fell in, nothing about how a sentence itself is found or tagged changes.

**2. How "the paragraph's cited records" is formed.** The union of every
record id tagged anywhere in that paragraph, across however many of its
own sentences carry a tag. `engine.m4.live_uncited_claims_battery`'s own
`_paragraph_coverage` already computes the boolean form of this (does
the paragraph carry a tag at all); item 2's own module needs the actual
id set, not just the boolean, since step 3 below checks an untagged
sentence's content against those specific records, not merely against
"some record or other."

**3. What the grounding net does with an untagged sentence in a cited
paragraph.** The exact same per-sentence check `verdict_for_sentence`
already runs on a TAGGED sentence - claim_markers, grounding_ratio
against the record set's own content words - run again, unchanged, but
fed the paragraph's own inherited record set in place of the sentence's
own (empty) `tags` list. Concretely: `verdict_for_sentence(text, tags,
...)` already takes `tags` as a plain list of ids; the paragraph
wrapper's whole design is "compute `tags` differently before the call,
change nothing after it" - an untagged sentence's own inherited call is
`verdict_for_sentence(sentence_text, list(paragraph_record_ids), ...)`,
the identical function, no new logic inside it, no new model call
(Constraint A holds by construction: this is string comparison against
already-loaded records, exactly what every other verdict on this turn
already does). This is real reuse, not a description of reuse - the one
function already does exactly what an inherited check needs; the wrapper
only changes which `tags` value it hands that function for one class of
sentence.

**4. What verdict an untagged sentence gets when its own inherited check
fails - two options, recommending one.**
- *(a) Withhold the sentence exactly as a failed tagged sentence is
  withheld today.* The one sentence silently drops from what a
  participant sees; the rest of the paragraph, and the rest of the turn,
  streams as normal.
- *(b) Count it as a paragraph failure that triggers regeneration,
  without itself being withheld. (Recommended.)* Nothing is dropped
  sentence-by-sentence; the WHOLE TURN is what regenerates, via the
  seat-guard shape R27 already ruled for enforcement (Rulings-Pending.md
  R27: "regenerate once with the violations named, then the Facilitator
  takes the turn") - the same mechanism already ruled, applied to a new
  failure kind, not a new mechanism.

**Recommending (b), and this does not need to go to Mark**, for exactly
the reason the reviewer's own instruction names as the escalation test:
(a) is a genuinely NEW participant-visible shape nobody has ruled -
a paragraph the participant reads with one sentence silently missing
from the middle of it, a hole in the prose no one asked for and R27-A's
own reasoning ("a paragraph must carry at least one citation" - the
paragraph is the unit, not its individual sentences) argues directly
against treating as sound. (b) is not a new shape at all - it is R27's
own already-ruled enforcement mechanism, whole-turn regeneration,
applied to a paragraph-level failure instead of a sentence-level one.
Nothing about what a participant would ever see is being decided fresh
here; the choice is only which of two already-adjacent behaviors a new
failure kind maps onto, and only one of them (b) maps onto something
already ruled.

**5. Narrowing `own_doctrine_in_other_tradition_turn` - the reviewer's
first further point, from #420's own numbers.** As built (PR #420),
`classify_other_tradition_turn` upgrades EVERY base `uncited_claim`
offense inside an `other_tradition` turn, unconditionally - 24 of 24 in
that run's own live data. Under a per-sentence hard failure (R26's own
two classes stay per-sentence under R27-A - Entry 54), that would fail
nearly every `other_tradition` turn on its own narrative frame, the
exact over-flagging problem R27-A itself exists to stop, just relocated
from R27's base class to R26's two classes.

**Narrowed rule:** inside an `other_tradition` turn, a sentence is
`own_doctrine_in_other_tradition_turn` only when either (i) it sits in a
wholly uncited paragraph, or (ii) it sits in a cited paragraph but its
own inherited check (item 3 above) fails to ground it against that
paragraph's own records. A sentence the net successfully grounds via
paragraph inheritance is NOT this class, even inside an `other_tradition`
turn - a frame sentence a paragraph's own citations genuinely support is
a formatting fact (no tag of its own), not an unsupported doctrinal
claim, and R26's whole point was never "every sentence in this kind of
turn needs its own tag," it was "don't assert what this world's own
records don't hold."

**Pinned for item 3's own tests, real sentences, not invented ones:**
- **Must still catch (own_doctrine_in_other_tradition_turn):** the two
  Augustinian sacramental sentences from R26's own motivating incident
  (Decision-Log Entry 50/51: *"What the sacrament does, it does by
  Christ's power, not the minister's purity."*, *"Even a broken priest
  could not block his grace."*) - genuinely unsupported by anything in
  alx's own records, real doctrine belonging to a different world,
  wholly uncited by construction; the narrowed rule must still fail
  both.
- **Must pass (not this class):** a grounded frame sentence inside a
  real `other_tradition` turn, from PR #420's own live data - alx's own
  answer on the Donatists probe (`probes["B-other-tradition"]`) put six
  sentences (*"When the great persecution ended, many who had given way
  - sacrificed to the gods, handed over the scriptures - wanted back
  in."*, *"The strict party said no: the church is holy, the defiled
  cannot pollute it."*, *"The wound was real on both sides."*, *"Those
  who had held fast felt betrayed."*, *"Those who had broken felt cast
  out."*, *"That is what our own record shows us wrestling with."*) in
  one WHOLLY UNCITED paragraph, all correctly still catching under (i)
  above - the real test case the narrowed rule needs is the OTHER shape,
  a frame sentence riding inside a CITED other_tradition paragraph (the
  alx conflict-turn shape already proven live: *"For years they held
  together."*, inside a paragraph #420's own report already shows fully
  cited, `uncited_in_cited_paragraph: 7`) - constructed as a hermetic
  fixture the same way `test_uncited_claims.py`'s own
  `_REAL_CHURCH_FAILURE_TEXT` already pins real record content without a
  live package, with `is_other_tradition_turn=True` forced on it to
  prove the narrowed rule, not merely R27-A's own base paragraph
  coverage, is what passes it.

**6. One-sentence paragraphs - the reviewer's second further point, and
mine to decide, not Mark's** (his own words: "that choice changes
nothing participant-visible"). #420's own data: 11 uncited sentences
sit in wholly uncited paragraphs across 14 turns that had any -
`witt`'s own `A-conflict` turn is a real, live example, two sentences (
*"In our own time, it did not."*, *"The tension stands in the confession
itself."*) with zero citations anywhere in that turn's paragraph at all.
A short, standalone line set apart by its own blank lines - a dramatic
beat, not a developed claim - fails paragraph coverage on its own by
construction, every time, if a one-sentence paragraph is scored as its
own isolated unit.

**Recommendation: a one-sentence paragraph inherits the immediately
preceding paragraph's own cited records for coverage purposes - it does
not stand as its own isolated unit.** Reasoning: a real paragraph
develops an idea across more than one sentence; a single sentence set
apart by blank lines on either side is, structurally, a rhetorical
device continuing the thought the PRECEDING paragraph just made, not a
new, independently-argued claim starting fresh with no support of its
own. Scoring it as an isolated unit resurrects R27-A's own reason for
existing - punishing narrative shape rather than actual unsupported
content - just relocated from "the last sentence of a paragraph" to
"any sentence a voice sets off alone for emphasis," a pattern a voice
would learn to avoid not because it makes fewer unsupported claims but
because it stopped using a legitimate rhetorical form. Inheritance from
the paragraph BEFORE (never the one after, and never both) keeps the
rule simple and matches how a reader actually experiences the line - as
the close of what was just said, not the opening of what comes next.

**Build order, unchanged from Entry 54:** item 2 (report-only module,
paragraph coverage + the narrowed R26 classes + inherited-check logging,
no participant-visible change), item 3 (tests, this entry's own pinned
cases plus the honest-limit-paragraph and wholly-uncited-narrative-
paragraph cases Entry 54 already named), item 4 (battery under the
paragraph unit - also now reporting, per the reviewer's own added asks:
the R26 honest-limit sentence's own utterance rate on `other_tradition`
probes whose records are silent, alx-on-Donatists first; and the count
of wholly uncited paragraphs that are exactly one sentence long), item 5
(enforcement, flag-gated, only on Mark's word after item 4).

**Entry 56 — 2026-09-23.** R27-A build order item 4's own live numbers
(PR #427, real, billed, region us-east-1, $2.0871: 11 admitted formation
worlds x 2 fresh probes + one small table session), the hand-sort of the
inherited check's own withheld sentences the reviewer thread ordered off
those numbers, and Mark's own ruling, R36, choosing item 5's enforcement
scope from what both showed. Full numbers: PR #427's own body and
`engine/m4/reports/live-uncited-claims-battery-report.json`.

**Item 4's own headline numbers.** 22 interview probes: sentence-level
raw rate 91% (20/22), post-regeneration residual 65% (13/20) -
unchanged measurement, kept beside the new numbers for comparison.
Paragraph-level (the real mechanism, item 2): `wholly_uncited_paragraph`
raw turn rate 23% (5/22), `inherited_ungrounded` raw turn rate 45%
(10/22). A simulated paragraph-unit enforcement (regenerate once on
either class, Facilitator takes a turn a real one survives) would have
touched 55% of turns (12/22); of those, 42% (5/12) would still have
reached the Facilitator after the one allowed regeneration. R26's own
fixed honest-limit sentence fired in 10 of 11 worlds' own
`B-other-tradition` probes (alx-on-Donatists first, per the reviewer's
own ask) - only `ijc` did not say it, and `ijc`'s own raw answer carried
zero offenses of any kind, so this reads as a different still-grounded
answer shape, not a real miss. 10 wholly-uncited paragraphs across the
run were exactly one sentence long. The net's own inherited-check
verdicts split 81 ok / 50 withhold.

**The hand-sort (reviewer-ordered, measurement-only, no PR).** The 50
withhold tally needed its own correction first, verified with a
synthetic repro rather than assumed: it includes sentences whose own
base verdict was already `withhold` for reasons unrelated to paragraph
inheritance (e.g. an untagged quoted span always withholds regardless
of what its paragraph cites) - those never reach
`find_uncited_paragraphs`'s own `inherited_ungrounded` branch, so their
text was never persisted anywhere (the same "report the reduced finding,
not the raw dump" discipline this build has followed throughout, Entry
55's own item 2 included). Only 28 of the 50 are actual
`inherited_ungrounded` offenses with recoverable sentence text. Hand-
classified: **3 genuinely unsupported** (specific, datable/nameable
claims - "By the mid-370s they were adversaries, not allies.",
"Rome's bishop was drawn in.", "Ursinus was exiled by imperial order and
never returned."); **19 supported in substance but failing on word
overlap** (narrative frame, paraphrase, pronoun reference - e.g.
"That was not the only one." / "After that the weather changed." /
"This controversy was different."); **6 that should have been exempt
under R27's own allowed-uncited kinds and weren't** - a real bug, not a
measurement artifact: `find_uncited_paragraphs`'s `inherited_ungrounded`
branch never applies the question/honest-limit/first-person exemptions
its own `wholly_uncited_paragraph` branch already does. One of the 6 is
R26's own fixed honest-limit sentence itself, near-verbatim ("Our record
doesn't mention that Christian tradition by that name."); another is a
literal question ("How did it end?"). This exemption asymmetry inflates
`inherited_ungrounded`'s own numbers and is a fix owed before that
class's own numbers can be trusted for a threshold.

**Mark's ruling, R36** (Rulings-Pending.md's own R36 entry has the full
text): enforcement (item 5) covers `wholly_uncited_paragraph` only, for
now. `inherited_ungrounded` stays report-only until the exemption bug is
fixed and re-measured - Mark rules on it separately once that question
is settled. `neighbour_named` stays a per-sentence hard failure,
unchanged. `own_doctrine_in_other_tradition_turn`, already narrowed per
Entry 55 to fire only on a real paragraph-level failure, therefore fires
in practice only through a `wholly_uncited_paragraph` finding while
`inherited_ungrounded` stays report-only - the narrowing rule itself is
unchanged, only which paragraph classes actually reach it in practice.

**Item 5's own build order** (reviewer thread, same message as R36):
flag-gated, default off (e.g. `CIC_R27_ENFORCE`), nothing changes for
any participant until Mark flips it. On a `wholly_uncited_paragraph` or
`neighbour_named` offense: regenerate once with the failures named (the
same correction shape the seat-identity guard and the battery already
use), re-check, and if a hard offense survives, the Facilitator takes
the turn through the existing fallback - any new participant-facing
words that needs gets drafted as options and escalated to Mark before
building; an existing ruled line, if one fits, gets used with which one
named. Single pass: paragraph coverage folds into the one `check_turn`
call `apply_net` already makes, so a live turn never pays the net twice
(the storage-bloat-avoidance note from item 2's own PR, #424). Table and
interview both, through `_run_ordinary_voice_turn`, same wiring as the
report-only path. Tests: flag off leaves every existing test and the
report-only events untouched; flag on: a wholly uncited narrative
paragraph regenerates and clears, one that survives goes to the
Facilitator, an `inherited_ungrounded`-only turn is never regenerated,
the Augustinian pair in an `other_tradition` turn still fails, the alx
frame sentence in a cited paragraph still passes. One live battery with
the flag on, same probes as #427, reporting regenerations, Facilitator
takeovers, and cost - then stop for Mark's staging look before the flag
is flipped anywhere. One PR, three-round cap, no self-merge.

**After item 5 has a verdict:** Stage 7b-7e proceeds in the order
already recorded (7b engine streaming module behind
`CIC_API_STREAMING`, sentence-gated, R30's hold-the-opening-paragraph
built in; 7c frontend consumer behind `VITE_STREAMING` with R31's
per-sentence marks; 7d guards proven in per-sentence mode against the
staging Papnoute text; 7e a live battery with streaming on), each its
own PR, then stop for Mark's staging look. Streaming does not ship to
participants before R27-A's own enforcement is on.

**Note, added 2026-09-23 after PR #432's own PASS verdict and live
numbers, for Mark to read before his staging look:** item 5's live
battery (flag on, real, billed) regenerated 7 of 22 interview turns
(32%), 2 of those 7 reaching the Facilitator (29% residual). The Table
session (alx/don/rzg) regenerated 7 of 10 voice turns (70%), 4 of those
7 reaching the Facilitator (57% residual) - an overall Table
Facilitator-takeover rate of 40% (4/10) against interview's 9% (2/22).
That gap is real and worth Mark's own eyes on before he judges the
Table on staging, not a run-to-run fluke - both of the reviewer's own
named candidate causes check out against real, already-committed
evidence, and both contribute:

- **Table turns cite less, by a wide, already-measured margin.** Item
  4's own report-only run (#427, same table_world_keys, same probe
  shape - a real live measurement, not this run's own inference) found
  `wholly_uncited_paragraph` in 7 of that run's own 10 table turns
  (70%) versus 23% of interview turns (`overall_raw_paragraph_turn_rate_by_class`
  in `engine/m4/reports/live-uncited-claims-battery-report.json`). Item
  5's own enforced run regenerated the identical count, 7 of 10 table
  turns - consistent with, not merely similar to, that 70% wholly-
  uncited-paragraph rate, even though the two are separate, non-
  deterministic live generations.
- **`neighbour_named` fires almost exclusively in Table mode**, and by
  a stark margin: across all 22 interview probes in #427's own report,
  `neighbour_named` never fired once (0 turns, 0 offenses) - a Table
  turn is structurally the only shape where a voice is in live
  conversation with another SEATED tradition and can name it directly;
  an interview probe has no other seated voice to name. In that same
  #427 table session, 5 of 10 turns carried at least one
  `neighbour_named` offense. Since `known_tradition_names` is derived
  per-turn from the registry excluding only the SPEAKING world (not the
  other seated worlds), every other seat at the Table is, by
  construction, a name `neighbour_named` can catch - a structural
  fact about the Table's own design, not a defect in this build.

Both causes point the same direction: a Table turn is simply more
likely to carry an enforced-class offense than an interview turn is,
on the same content a participant would recognize as normal cross-
voice conversation, not a broken answer. Item 5's own enforced run
(this PR) did not persist per-turn offense-class detail (only the
aggregate regenerated/took-over counts, by design - the same
"report the reduced finding, not the raw dump" discipline this build
has followed throughout), so the two data points above are #427's own
already-committed measurement, not a re-derivation from #432's own
raw data, which no longer exists (the battery's own temp store is not
retained after each run). If Mark's own staging look wants the exact
classes on the Table's own real turns, that needs a report-only
paragraph-level run with per-turn class capture added, not assumed
from this note.

**Entry 57 — 2026-09-23.** The false fixed honest-limit sentence, a
real defect the reviewer thread's own R39 audit found and ordered fixed
directly (no new ruling needed - R26's own already-ruled words,
Rulings-Pending.md's R26 entry, already specified the conditional
branch this PR builds; only the shipped code never implemented it).

**The defect.** `engine.m4.turn._other_tradition_directive` fired the
fixed sentence *"Our record doesn't mention that Christian tradition."*
unconditionally on ANY `other_tradition`-routed turn, for every world,
regardless of whether that world's own records already named the
tradition asked about. For `ijc` on Donatism specifically this is
false: `ijc`'s own already-vendored records genuinely name it
(`ijc.quote.compelled-to-come-in`, `ijc.story.emperor-builds-another-
basilica` - real excerpts, not inferred, both cite Augustine writing to
the imperial tribune Boniface c. 417 on "the madness of the Donatists").

**The fix.** Two new functions in `engine.m4.uncited_claims`:
`match_named_tradition(text, registry, exclude_world_key=...)` (which
OTHER formation world's own name - card_name, display_name, demonym,
representative name - appears in the participant's own message, the
reverse of `classify_neighbour_named`) and
`world_records_mention_tradition(repository_records, named_world_entry)`
(record ids in THIS, speaking world's own package whose real prose text
already names that OTHER world - same restricted `PROSE_KEYS` field
allowlist the R37 design brief already proved necessary, PR #438,
avoiding the exact locus/source-filename false positive that scan
found). `_other_tradition_directive` now takes an optional
`evidence_record_ids` parameter: empty/None keeps the fixed sentence
exactly as it always was (the true "never heard of this" case - `alx`
on Donatism, this workstream's own original worked example, stays
unchanged); a nonempty list skips the sentence entirely and hands the
voice those record ids as its own ground, cited under the ordinary
citation contract, never asserting more than what its own records or
the conversation actually give it.

**Threading**, matching the existing `known_tradition_names` pattern
exactly (caller-computed, since `_run_ordinary_voice_turn` stays
registry-free by design): `engine.api.wiring.handle_message` computes
`match_named_tradition`/`world_records_mention_tradition`
unconditionally (never gated behind `r27_enforce` - this corrects an
existing false statement, not new enforcement) and passes the result
through `run_turn`/`_run_ordinary_voice_turn`/`_build_turn_directive`
as `other_tradition_evidence_ids`, read only when
`is_other_tradition_first_ask` is also true. Table mode
(`table_wiring.py`) needed no change: checked directly, `run_voice_turn_
for_world` (the `_run_ordinary_voice_turn` alias Table calls) is never
passed `is_other_tradition_first_ask=True` anywhere in `table_wiring.py`
today - `out_of_scope_class` there feeds only the post-hoc
`build_uncited_claims_event` audit classification, never the live
directive. Table mode's own `other_tradition` turns get no special
directive at all currently, fixed sentence or otherwise - a real,
separate, pre-existing gap this fix does not touch or widen into,
noted here rather than silently discovered and dropped.

**Tests**, both branches pinned directly per the reviewer's own
explicit instruction: `engine/m4/tests/test_turn.py` pins
`_other_tradition_directive`'s own two branches (no evidence keeps the
fixed sentence; real evidence skips it and emits the record ids as
`[[tag]]`s). `engine/m4/tests/test_uncited_claims.py` pins
`match_named_tradition` (the demonym case, and a non-fleet name like
"the Arians" correctly resolving to `None`) and
`world_records_mention_tradition` on real, trimmed excerpts (`ijc`
finds it, `alx`'s own real `church-failure` text does not, and a
locus-filename coincidence is correctly ignored - the same false
positive already found and fixed once, pinned here too). Full suite:
1024 passed (1016 + 8 new).

**The real count, fleet-wide** (per the reviewer's own explicit ask -
`world_records_mention_tradition` run against each of the 11 admitted
formation worlds' own real package, checked against the real battery's
own deterministic probe target -
`engine.m4.live_uncited_claims_battery._other_tradition_turn`'s own
alphabetical-first-other-card-name logic, reproduced read-only): **4 of
11 flip** - `desert` (asked about `alx`), `hal` (asked about `alx`),
`ijc` (asked about `alx`), `pahc` (asked about `alx`) all have real
textual evidence and now answer from their own records instead of
saying the fixed sentence; `alx` (asked about `don`, this workstream's
own original worked example), `cappadocian`, `don`, `gallic`, `rzg`,
`syr`, `witt` have none and are unchanged. Full per-world table:

| World | Asked about | Flips | Evidence record ids |
|---|---|---|---|
| alx | don | no | — |
| cappadocian | alx | no | — |
| desert | alx | **yes** | desert.contested.alexandria-continuity, desert.demo.center-jesus-as-god, desert.story.antony-secret-burial, desert.story.sarapion-anthropomorphite, desert.story.virgin-who-hid-athanasius |
| don | alx | no | — |
| gallic | alx | no | — |
| hal | alx | **yes** | hal.dw.authority, hal.story.rufinus-rupture |
| ijc | alx | **yes** | ijc.quote.julius-custom, ijc.quote.let-the-ancient-customs-prevail, ijc.quote.sozomen-thessalonica-law, ijc.story.letter-that-outranked-a-council |
| pahc | alx | **yes** | pahc.contested.egypt-exclusion |
| rzg | alx | no | — |
| syr | alx | no | — |
| witt | alx | no | — |

Note `ijc`'s own real battery probe target is `alx` (alphabetically
first other card_name), not `don` - the reviewer's own Donatism example
is real and independently confirmed (`ijc` on `don` also has evidence,
the same two records named above), but is not literally what the
battery itself asks `ijc`; both are true and both are reported, not
conflated.

**Entry 58 — 2026-09-23.** Two display defects from Mark's own staging
Table look (relayed via the reviewer thread), both against Papnoute's
(Desert Fathers) and Theon's (Alexandria) turns.

**Defect 1 - citation-card empty bullets.** Papnoute's turn showed
"General references (1)" followed by five empty bullet items - "* "
with nothing after. Traced the render path end to end:
`GeneralReferences.tsx` -> `SourceList.tsx` (`{s.work ?? s.source_id}`
per `<li>`, JS `??` only catches null/undefined, never an empty
string) -> `engine/m4/citation_cards.py`'s `resolve_source_card`, the
one function both the legacy renderer's `resolve_citation_sources` and
the anchor-driven renderer's `transparency_plan.build_transparency_plan`
call to build every `sources[]` entry a citation card carries.

**Root cause, and why it could not be reproduced from today's data.**
`resolve_source_card` builds each `sources[]` entry as `{source_id,
author, work, locus, rights_status}` unconditionally - it has never
checked whether an entry actually has anything printable before
shipping it. The renderer's own primary field is `work ?? source_id`,
so as long as an entry carries a real `source_id`, that id itself is
the fallback text - never blank, even when the id is dangling (doesn't
resolve in this world's own repository). The only shape that leaves
truly nothing to print is an entry whose own `source_id` is missing or
blank AND whose own `locus` is missing or blank too - both fields
absent on the citing record's own `sources[]` entry, upstream of this
function, a shape the grounding net's own checks don't cover since
they verify the CITING record's id, not the internal shape of its own
`sources[]` list. Four independent fleet-wide scans - the currently
compiled `packages/` repository for all 12 built worlds (including
the `fix` fixture world), every one of desert's own seven historical
package builds (2026-09-21 through 2026-09-22T21-17-53Z, in case
staging was serving an older build than today's `latest_complete_
package` pick), and a fresh `compile_and_hash` straight from `records/`
for eleven worlds (the same method `test_citation_cards.py` itself
uses for "real, not invented" fixtures) - found **zero** `sources[]`
entries missing `source_id` anywhere in the fleet today. This defect's
exact historical trigger is not reproducible from current record data;
it is either a stale-deploy artifact (staging running an older build
than what `records/`/`packages/` hold now) or a real but currently-
dormant shape this project has no standing invariant against. Given
the reviewer's own framing ("find the cause... most likely a source
group whose entries lack the fields the card prints... fix so an entry
with nothing to print is not rendered"), the right fix is the
structural one: close the gap at its true origin rather than chase one
historical instance that no longer reproduces.

**The fix** (`engine/m4/citation_cards.py`): `resolve_source_card` now
drops a `sources[]` entry before it is ever built into the card, if
every one of its five fields (`source_id`, `author`, `work`, `locus`,
`rights_status`) is empty or blank. One check, in the one function
both renderers already share, so no second filter is needed in the
frontend and no caller has to know about the invariant. An entry that
still names a real (even if dangling) `source_id`, or a real `locus`
with no resolvable `source_id`, is kept - dropping it would discard
real, checkable information the participant can still act on; only an
entry with genuinely nothing printable in any field is removed.
Two new tests in `engine/m4/tests/test_citation_cards.py` pin the
boundary directly: a `sources[]` entry with `source_id: null` and no
`locus` is dropped; the same entry with a real `source_id` (dangling
or not) is kept, and so is the same missing-`source_id` entry once a
real `locus` is added. Full existing suite green (`pytest engine -q`,
1016 passed) after the change.

**Which two records produced Theon's own "...cared.✲✲" (see Entry
57's Defect 2, immediately below) is a separate question, reported
there, not here** - this entry's own fix is unrelated to which records
cite what; it only changes which entries `resolve_source_card` is
willing to ship at all.

**Defect 2 - two transparency marks on one sentence.** Theon's second
turn: *"Origen was driven out by his own bishop, Demetrius, over
wounded pride and contested authority, long before any emperor
cared.✲✲"* - two mark glyphs, stacked, on one sentence. The reviewer's
own first framing read this as a possible violation of R31 (E2, RULED:
"a citation mark attaches with each sentence as it clears" - one mark
per sentence). Mark corrected that framing directly, relayed verbatim:
*"i am not sure why we can only have 1 mark per sentence, i get not
overloading, but if a quote and a lexicon word are in the same
sentence they should both marked."* This is R31-A, recorded in
Rulings-Pending.md immediately below R31: one mark per distinct
grounded element (a story, a witness quote, a term), never reduced to
one per sentence. Two marks landing on the same sentence is not a
count bug under R31-A - it is by design, whenever a story/quote
record's citing run and a `doctrinal_witness` record's citing run both
finish at the same sentence (`VoiceTurnBody.tsx`'s `finishingStoryCards`
and `finishingWitnessCards`, or the anchor-driven renderer's own
`storyCards`/`witnessCards` split by `STORY_RECORD_TYPES = {story,
quote}` / `WITNESS_RECORD_TYPES = {doctrinal_witness}`). The real
defect R31-A names is readability - a participant sees "✲✲" with no
way to tell which mark is which record without tapping both.

**Which two records back Theon's own two marks - not confirmed, and
said honestly rather than guessed.** The exact sentence does not
appear in any saved battery report, Corpus A pool file, or persisted
transcript this repository or its build artifacts carry - it was a
live staging generation whose own evidence bundle (the per-sentence
citation record_ids `apply_net` actually attached) is not stored
anywhere this session can read. Reproducing it exactly would need a
fresh live regeneration against Theon's own original prompt, which is
also not on record. What can be said without guessing: `alx.story.
origen-demetrius` (a real `story` record) and `alx.dw.councils` (a
real `doctrinal_witness` record) both exist in alx's own repository,
both mention Demetrius by name, and are the two record_types whose
mechanism (above) can produce exactly this stacked-mark shape on
content matching this sentence's own topic - named here as the most
likely pairing given real content, explicitly flagged as unconfirmed,
not reported as fact. If Mark wants the exact pair pinned, that needs
either a live regeneration against the original prompt or persisting
`apply_net`'s own per-sentence citation output for staging turns going
forward - neither done here.

**Three readability options for R31-A, one paragraph each, no code
change - Mark's to choose, not decided here** (the reviewer's own
three candidate directions):

**(a) Mark placed at its own element.** Instead of both marks landing
at the end of the sentence, each mark moves to sit immediately after
the specific span it actually grounds - the story's mark after the
narrative clause it covers, the witness mark after the specific phrase
its quote backs, wherever those spans fall inside the sentence. On a
phone screen this reads the most like ordinary punctuation - each mark
sits right where its own claim is, so a participant never has to
match a glyph to content by process of elimination. Cost: this is the
biggest engineering lift of the three - the current renderer places a
mark at a SENTENCE boundary (the end of a segment), not at an
arbitrary sub-span inside one, so this would need real span-level
placement logic, a capability the anchor-driven renderer's own anchors
(`run_start_sentence`/`run_end_sentence`) don't carry today; a change
to what `transparency_plan.py`'s anchors actually record, not just how
they render.

**(b) One glyph per kind.** Keep marks at the sentence boundary (no
placement change), but give the story mark and the witness mark
visually distinct glyphs - not two identical ✲ characters stacked, but
one shape for "a story is being told" and a different one for "someone
is being quoted," the same distinction `StoryMark`/`WitnessMark`
already carry as separate React components today, just never
differentiated in what they actually render. On a phone screen two
different small glyphs read as two different KINDS of thing at a
glance, without needing a tap to find out - closest to a typical
footnote-superscript convention (¹ ² vs a dagger/asterisk pair).
Cost: smallest of the three - a CSS/character change inside two
already-separate components, no data-shape change, though it does add
a second glyph to the fleet's own "one grammar, five applications, no
feature may introduce a sixth verb" vocabulary (Full UX Design §5.7),
which R10's own ruling already stretched once for the repeat-citation
opacity treatment.

**(c) Single mark, hover/tap card listing all elements.** Collapse
however many marks would land on one sentence into a single glyph;
tapping or hovering it opens one card listing every record it actually
covers (today's existing per-mark tap-through, just aggregated). On a
phone screen this is the cleanest - never more than one glyph per
sentence, however many records ground it - at the cost of hiding the
"how many distinct things are grounding this" information the current
stacked-glyph shape (accidentally) surfaces today; a participant has
to tap to learn there were two things, not one. Cost: moderate - the
per-segment mark-building logic in both renderers already groups by
kind (`marks.push(<StoryMark.../>)`, `marks.push(<WitnessMark.../>)`);
this would merge those into one combined mark component fed both
groups, no anchor/data-shape change needed, only a rendering change.

No recommendation between the three - the reviewer's ask was options,
not a decision.

**Entry 59 — 2026-09-23.** R39-audit retrofit brief (the reviewer's own
seven-gap audit, this PR): G3, G4, G6, G7, and the precedent note, in
full. G1/G2 (paragraph-anchoring + tag-is-a-promise wording, with the
before/after battery) and G5 (the bridge-route-vs-pronoun_rule ruling
options) are their own entries below/in Rulings-Pending.md.

**G3 - the do_not_voice quote license never reaches the prompt.**
`engine/m4/grounding.py`'s `find_do_not_voice_violation` runs only on
the FINISHED answer text, after generation - confirmed, it never
touches what the voice is given to work from. `engine/m4/evidence.py`'s
`select_cell_candidates`/`_entry` builds every quote candidate (record_
type == "quote") through the same generic path as any other record -
reads `confidence`, `classification`, `claim_guards`, never `license`.
A do-not-voice quote and an ordinary quote produce byte-identical
evidence-block entries; `render_evidence_block` prints both the same
way, with no restriction noted anywhere. The rider mechanism to reuse
is already proven and already-shipped: R11's own `claim_guards` rider
(`render_evidence_block`'s own `MUST NOT ASSERT: ...` line, rendered
directly onto a candidate's own evidence line, inside the same
`budget_chars` the candidate is already charged against) - not
`citation_cards.py` (downstream, post-hoc source-card resolution for
the transparency UI, unrelated to this gap).

**Fleet-wide count: exactly 2** quote records fleet-wide carry
`license: do-not-voice` - `syr.quote.aphrahat-anti-jewish-frame` (a
real formation world, Aphrahat's *Demonstrations* XVII.1) and
`fix.quote.private-teaching` (the fixture/test world; its own
`divergence_note` states the license reflects that the words were
never spoken aloud, only copied privately - it reads as built
specifically to exercise this mechanism). No other of the eleven
formation worlds carries one today; both existing instances currently
reach the voice as ordinary, unrestricted evidence.

**Proposed (not built): reuse the `claim_guards` rider shape.** Keep a
do-not-voice quote as a candidate (removing it loses real citable
substance the license does not necessarily bar - `fix.quote.private-
teaching`'s own `divergence_note` makes the point directly: the words
were never spoken, not that the underlying fact is unspeakable), but
carry `license == "do-not-voice"` forward in `_entry()` the same way
`claim_guards` already is, and render it as a rider: `" | MUST NOT
QUOTE VERBATIM: paraphrase or cite the fact only, never reproduce this
record's exact wording."` This is the direct generation-side
counterpart to what the runtime check actually polices (verbatim
reproduction, not use of the record at all), reuses an already-shipped
rendering shape rather than inventing one, and avoids silently
degrading answer quality on a topic the world's own record may still
want spoken, just not quoted.

**G4 - no prompt line against display markup.**
`engine/m4/output_check.py`'s display family (`_display_findings`)
flags residual `[[...]]` tag markup in any spelling, literal asterisks,
markdown headings, horizontal rules - the module's own header docstring
states the "5 of 49 live turns" figure directly and names, of this
exact family: *"No such function was ever written"* - unlike two other
defects the same docstring describes (each since fixed "by asking the
prompt more insistently"), no generation-side attempt was ever made for
display markup at all. Confirmed independently: no "no markdown / plain
text / no formatting" instruction exists anywhere in `engine/m2/
builders.py` or `_fleet.voice.fleet.md`.

**Proposed (not built).** `register_statements` cannot take an eighth
line - the fleet record's own ruling note says the seven are O2 verbatim,
copied not paraphrased, "so this record and the spec can never quietly
drift apart"; an eighth would break that parity. Add a new field
instead, `display_discipline`, delivered the same standing-rule way
`pronoun_rule`/`citation_contract`/`limit_discipline` already are (a
matching `emit(...)` line in `build_fleet_preamble`), in the same
terse, declarative register as the existing one-line statements:

> "Only prose reaches the participant - no markdown, no headings, no
> asterisks, no horizontal rules, and no bracketed tags of any kind. If
> it would look typeset on a page, it is not spoken."

**G7 - reader-failure pass-through: no standing directive.**
`engine/m5/failure.py`'s reader-failure branch (lines 50-79 in the
current file; the audit's own file:line citation, 46-95, overruns the
file's actual 102 lines) returns `RoutingDecision(action="voice_pass_
through", ...)` with no `directive` and no `out_of_scope_class` - both
default `None`. Traced through: `_build_turn_directive` (`turn.py`)
returns `None` outright when directive is `None` and neither
`table_engagement` nor `is_other_tradition_first_ask` is set - all
three are false on a reader-failure turn, so the voice genuinely runs
with no directive text of any kind, confirmed exactly as the audit
named it. The other-tradition rule is confirmed per-turn-only, gated on
`is_other_tradition_first_ask`, itself computed from `out_of_scope_
class == "other_tradition"` - a value only the READER produces. No
reader classification, no other-tradition directive: this rule never
reaches a reader-failure turn as things stand.

*(Correcting the audit's own label: the two-condition knowledge-scope
rule this item names is R37 ("When may a Representative's pivot draw on
outside knowledge of a named-but-uncovered tradition?"), RULED
2026-09-23 12:47Z - not R26, which is the earlier, broader ruling R37
itself amends. R37 is not yet merged to `main` (open PR #438), which is
why a search of this branch's own `Rulings-Pending.md` - cut from
`main` - found nothing under that number; it is real, RULED, and its
own two-condition test [(a) the world's own time_window/horizon; (b)
revealed in this conversation] is exactly what `knowledge_scope` below
carries.)*

**Proposed (not built).** A new standing field, `knowledge_scope`,
delivered the same always-compiled way as `pronoun_rule`/`citation_
contract`/`limit_discipline` - the cached half of the prompt a reader
failure cannot remove, unlike the per-turn directive channel that goes
missing exactly when the reader fails:

> "We speak of another Christian tradition, beyond our own, only two
> ways: what we could actually have known of it within our own years,
> because our own records genuinely hold it; or what this conversation
> has already told us, in the participant's own words. Outside both, we
> say plainly that our own record does not mention it, and we answer
> the rest from what we do hold. We never claim another tradition's
> history or doctrine as if it were ours, or as if we knew it from
> anywhere but one of those two places."

When the reader succeeds, this sits beneath the fuller, evidence-
carrying `_other_tradition_directive` without contradicting it (strictly
more specific and evidence-backed). When the reader fails, this
standing line is still present in the compiled prompt - the voice
degrades to it instead of to nothing.

**Precedent - the retired honest-limit floor line, the shape every
G-item above should follow.** `turn.py`'s own comment (current lines
838-843, shifted from the audit's cited 781-792), left in place as a
marker rather than deleted: *"No code-appended floor line. Program-Spec
M5: 'In-world thinness is never intercepted - the honest limit is the
voice's own testimony, not a system apology.' It fired on 7 of the
turns measured today and on every one of the seven it landed after real
surviving content... The honest limit is the voice's job, and the limit
records are in its ground to say it from."* `fleet.md`'s own
`limit_discipline` (line 33, unchanged): *"What the ground given for
this turn does not support is spoken as our own honest limit, in voice,
plainly - never asserted as though it were fact, and never apologized
for as though honesty were a failure... Answer the question first; name
what is missing where it touches that answer."*

A code-appended floor line existed first - a runtime backstop that
mechanically tacked an honest-limit sentence onto the answer whenever
grounding fell short. Once `limit_discipline`, compiled into every
world's own standing prompt, became strong enough to make the voice say
this itself, unprompted, on real turns, the backstop was retired, not
deleted - the comment stays as a record of why it is gone - and the
real fix was recognized as living in the generation-side text, not a
runtime patch appended after the fact. This is the shape every G-item
in this audit is asking for: a runtime check exists first because
generation cannot yet be trusted to say the right thing on its own; the
real fix is prompt text that makes the voice say it correctly in the
first place, after which the check becomes a rarely- or never-firing
backstop kept for safety, not a live crutch.

**G6 - the withheld-sentence bookkeeping bug (built, not merely
proposed, this PR).** `engine/m4/uncited_claims.py`'s own module
docstring and `find_uncited_claims`'s own filter both asserted a
withheld sentence "never reaches the participant" and is therefore
"nothing... to check." False, confirmed against `engine/m4/turn.py`'s
own `apply_net`: `text = grounding_net.strip_tags(raw_text)` strips
ONLY `[[...]]` tag markup from the raw text - every sentence's own
prose, withheld or not, survives to the finished answer (`apply_net`'s
own docstring, correctly: *"the checks gate decoration, never the
text... A sentence that fails verification loses its citation and is
carried on the event for the SS5 audit; it is not destroyed on the way
to the screen"*). `find_uncited_claims`'s own filter (`if sent["verdict"]
!= "ok" or sent["tags"]: continue`) skipped every withheld sentence
unconditionally - so a sentence that WAS tagged, then withheld (tag
stripped, text kept) reads to the participant with no citation and no
visible sign anything is wrong, and R27's own dedicated "catch every
uncited claim" mechanism was blind to it. Worse, and found live-testing
the fix: a genuinely UNTAGGED sentence making a specific, uncited claim
(the fleet's own real test fixture - "The tradition that won here
brought the repentant back in, even at the deathbed, and Dionysius
defended doing so," no tag at all) also gets verdict `"withhold"` from
`check_turn` (a separate branch, gated on no-tag-plus-specific-claim,
not the tag-verification branches) - so this same gap already
compounded a second, distinct grounding_net.py-level blind spot too.

**The fix:** the filter now reads `if sent["verdict"] == "ok" and
sent["tags"]: continue` - the same "genuinely, successfully cited"
idiom `grounding_net.py`'s own `substantive_survives` already uses.
Anything else - untagged, or tagged-but-withheld - is examined exactly
like an untagged sentence, through the same allowed-uncited checks
(question / honest-limit / first-person-no-claim) every other candidate
already goes through. The module's own docstring and the function's own
inline comment are corrected to state what `apply_net` actually does,
not what it was assumed to do. Two existing tests that pinned the old,
false premise (`test_a_withheld_sentence_is_never_checked`, `test_real_
dionysius_deathbed_sentence_uncited_is_withheld_upstream_not_reported_
by_this_module`) are corrected in place to assert the real, fixed
behavior, plus one new test confirming the three allowed-uncited kinds
still pass a withheld sentence of that shape. Full suite green
(`engine/m4` + `engine/api`, this PR).

**Entry 60 — 2026-09-23.** G1/G2 - the fleet-wide `citation_contract`
(`records/_fleet/fleet_voice/_fleet.voice.fleet.md`) has no paragraph-
anchoring language (ground travels by paragraph; interpretation stays
attached to what it interprets - `engine.m4.grounding_net.check_turn_
with_paragraph_coverage`/`find_uncited_paragraphs` check for this at
RUNTIME, nothing asks for it on the generation side) and no tag-is-a-
promise content rule (R39's own gap, Entry 59: the contract's own
verbatim-fidelity promise is scoped to quoted spans only).

**Proposed wording** (`engine/m4/reports/g1_citation_contract_battery.py`,
this PR) - appended after the contract's own stable tail sentence ("The
tags themselves are never shown to the participant; only the sentence
is."), present in every world's compiled prompt regardless of that
world's own per-world example ids inside the contract's own worked
example:

> "Ground travels by paragraph, not only by sentence: an interpretive
> or connective sentence - one that carries no tag of its own because
> it names no person, place, text, number, or quote - stays attached to
> the claim it interprets, and that claim's own ground is what it rides
> on. It never drifts past a paragraph break to ride on a different
> paragraph's ground instead; a new paragraph that opens with its own
> claim starts its own ground fresh, and everything within that
> paragraph, tagged or not, answers to it. A tag is a promise about
> more than address: every specific detail in a tagged sentence - not
> only a quoted span - must be that record's own content, stated or a
> fair paraphrase of it, never a detail added because it sounds
> plausible, fits the period, or belongs to a related matter this voice
> happens to know about from outside the record. Where a sentence would
> need one more specific detail than its tagged record actually gives,
> it stops at what the record gives; anything further is named, if at
> all, as our own honest limit, never folded into the tagged sentence
> itself."

**The before/after battery** (interview only - 11 admitted formation
worlds x 2 fresh probes each, current vs proposed wording, no table
session; reuses `engine.m4.live_uncited_claims_battery`'s own real
`_run_probe_turn`/`CONFLICT_TURN`/`_other_tradition_turn` rather than
reimplementing the probe/regeneration logic; each world compiled fresh
via `compile_and_hash` rather than read from `packages/` on disk, since
this local environment's own `packages/alx/...` registry-current
pointer was found, mid-measurement, to point at an empty directory - a
build artifact from this session's own heavy local test-running,
unrelated to the fix itself). **Real cost: $3.2801, 44 calls.**

**The honest result: no measurable improvement.** Raw turn rate
identical both conditions - 95.5% (21/22). `wholly_uncited_paragraph`
turn rate identical both conditions - 32% (7/22). Per-world raw
sentence-offense TOTALS were noisier and, summed across the fleet,
higher under the proposed wording (91) than current (68) - not read as
a regression the wording caused (this is one live run per condition,
not a paired/controlled resample of the same draft, and R27/R27-A's
own battery numbers are known to carry real run-to-run generation
variance at this sample size), but a real number, reported as measured
rather than smoothed toward the hoped-for direction. **The proposed
wording does not move the R27/R27-A raw offense rate at this sample
size.** This does not contradict R38's own self-revision result (Entry
61) - R27/R27-A's own checks (uncited claims, paragraph coverage) and
R38's own leak class (a specific fabricated detail riding a real tag)
are different things; a generation-side line aimed at one is not
expected to move the other. No new "safe to leave enforcement off"
threshold is justified by this measurement; R36's own existing
threshold discussion (Rulings-Pending.md) stands unchanged. Full
per-world numbers: `g1-citation-contract-battery-2026-09-23.json`.

**Entry 61 — 2026-09-23.** Mark's own follow-up ask, before this PR
opens: the precision of the detector (`engine.m4.uncited_claims.find_
uncited_claims`) that produced Entry 60's own 95.5% raw rate. Entry
60's own battery script only persisted aggregate counts, not the real
flagged-sentence text, so it could not be sampled directly - an honest
methodology note, not glossed over: `engine/m4/reports/g1_precision_
sample_measure.py` re-runs the identical battery mechanism, CURRENT
citation-contract wording only (Entry 60's own finding - the proposed
wording made no measurable difference to the raw rate - means which
condition this sample is drawn from does not bear on the detector's
own precision), 11 worlds x 2 probes = 22 fresh probes, keeping every
raw offense's own sentence text this time. **Real cost: $1.6527, 22
probes, 155 raw offenses captured.**

**Sample:** 40 of the 155, stratified across all 11 worlds (2-5 per
world, proportional to each world's own share), hand-read against each
world's own real, freshly-compiled records (`engine.m2.compiler.
compile_and_hash`, not assumed from general historical knowledge - a
sample of the "supported" classifications below was independently
verified by searching each world's own compiled repository for the
specific named claim, not trusted on plausibility alone, given this
whole investigation is about not trusting plausible-sounding, unverified
claims).

**The three counts Mark asked for: 0 unsupported, 14 supported but
untagged, 26 interpretive or connective.**

- **Unsupported (0 of 40):** none found. Not one of the 40 sampled
  sentences asserted a claim this hand-read could not find real support
  for, somewhere in the speaking world's own repository.
- **Supported but untagged (14 of 40):** the record makes the claim,
  the voice simply never attached a tag to it. Three verified directly
  against the compiled repository: *"Traveling through Palestine,
  Origen was ordained a presbyter by the bishops there, without his own
  bishop's consent"* (alx) - matches `alx.story.origen-demetrius` and
  `alx.quote.demetrius-accused-him-bitterly` almost verbatim.
  *"Slaves encouraged to despise their masters and leave them"*
  (cappadocian) - matches `cappadocian.story.slave-market-sermon` and
  `cappadocian.force.ascetic-ferment` directly. *"Those customs - the
  twelve psalms at evening and at night, received from an angel..."*
  (gallic) - matches `gallic.core.gallic` and `gallic.figure.cassian`
  directly, specific enough (two numbers, a named source) that it reads
  as an oversight, not an interpretive choice. Also in this bucket:
  witt's own quoted confession language ("freely justified for Christ's
  sake through faith...") - real quoted text with no tag, a citation-
  contract violation in its own right (the contract's own verbatim-
  fidelity promise applies to quotes specifically) distinct from R27's
  own uncited-claim class, surfaced by this same sample.
- **Interpretive or connective (26 of 40):** the contract already says
  these need no tag - transitional framing ("So there were two
  arguments at once," "It did not end cleanly"), rhetorical summary
  ("The whole world knew it," "The wound had a shape before it had a
  name"), and analytical synthesis connecting two already-cited ideas
  rather than naming a new one. Two sub-cases worth naming separately,
  both real detector-precision gaps rather than ordinary connective
  prose: (a) two sentences (ijc, pahc) are honest-limit in function -
  *"Our record doesn't mention 'Alexandrian Christianity' as though it
  were a separate tradition from our own"* - but got caught by the
  `neighbour_named` upgrade specifically because they name a fleet
  world while denying knowledge of it; (b) one sentence (syr) -
  *"Beyond that, the record runs thin"* - is honest-limit scaffolding
  in plain English that `engine.prose.SCAFFOLD_MARKERS`'s own fixed
  phrase list does not happen to cover, a real, narrow gap in that
  vocabulary's own coverage, not a judgment call.

**Three options for Mark, one paragraph each, no decision - what each
does to the participant's transcript and to the Facilitator step-in
rate:**

**(i) R27 stays report-only, the contract stands as written, the
detector is kept as an instrument with its measured precision.** The
participant's transcript is unaffected either way - report-only already
means nothing the detector flags ever reaches the participant
differently today. The Facilitator step-in rate stays exactly where R36
already set it (`wholly_uncited_paragraph` only, `neighbour_named` a
hard per-sentence failure). This option treats the 0/14/26 split as
useful measurement, not as a reason to touch anything - the detector
over-flags real declarative prose relative to what it's actually FOR
(R27's own stated job is catching a genuinely uncited claim, and 26 of
40 flags here are prose the contract already exempts), but nothing here
currently acts on a flag without a human step, so the cost of that
over-flagging is borne by review effort, not by a participant.

**(ii) The contract adopts the paragraph rule and enforcement returns
once a generation-side change moves the raw rate, which this run says
wording does not.** No participant-facing change today - this option
is conditional on a FUTURE result this measurement did not produce.
If a real generation-side fix is later found that does move the raw
rate down, enforcement (regenerate-once-then-Facilitator, R36's own
existing shape) returns on the improved population; the Facilitator
step-in rate would then track whatever residual rate that future fix
leaves, not the 95.5%/32% measured here. Until such a fix exists, this
option is functionally identical to (i) - it names a bar for
re-enabling enforcement rather than changing anything now.

**(iii) The detector is rebuilt around "unsupported" only, with the two
honest kinds (supported-but-untagged, interpretive-or-connective)
exempt, and re-measured before any enforcement.** This would require
real new work - `find_uncited_claims` becomes a support check against
the world's own records (closer in shape to candidate C, R38's own
Entry 57/59, than to the current lexical/pattern gate), not the fixed-
pattern exemption list it is today. If built and re-measured with
precision closer to 1.0 on "unsupported" specifically, the participant-
facing transcript would see far fewer false triggers on honest,
supported prose (only the 0-of-40 unsupported class would ever
regenerate a paragraph), and the Facilitator step-in rate would fall to
track genuine fabrication rather than tagging completeness and
connective-sentence false positives - but this sample's own 0/40 real
unsupported count on a small hand-read is not itself evidence the
rebuilt detector would perform well; that needs its own live
measurement once built, the same discipline every other candidate in
this project has been held to.
**Entry 62 — 2026-09-23.** R38 build (Mark's own "GO" on the 0/20 real-
leak measurement - the full ruling, mechanism, and measurement live on
PR #436, not duplicated here; this entry covers only what this PR
itself adds, the real code). `engine/m4/self_revision.py` (new module):
`self_revise(...)` - after the voice's draft, if the draft carries any
tags, a second same-model, same-system-prompt call is given the draft
plus the exact, full text of every tagged record (`REVISION_INSTRUCTION`,
carried over unchanged from the measurement in PR #436) and told to trim
any untagged-record detail. Wired into `engine/m4/turn.py`'s
`_run_ordinary_voice_turn`, between the seat-identity guard and
`apply_net` - the revised text (or the draft, on any fallback) is what
`apply_net`, the net, and the participant all see; nothing downstream
needed to change.

**Scope and kill-switch, exactly as specified.** Fires only when
`is_other_tradition_first_ask` is true (the caller-computed flag every
other other_tradition-scoped mechanism in this file already gates on -
`_other_tradition_directive`, R37's own evidence-offering) and the
draft actually carries a tag (an other_tradition turn that answered
with the honest-limit sentence and nothing else spends no extra call -
`self_revise`'s own `no_tagged_records` fallback). `self_revision_
enabled` threads caller-computed through `run_turn`/`_run_ordinary_
voice_turn`, `engine.api.wiring.handle_message`, `engine.api.
table_wiring`'s own three round-advance functions, and `engine.api.
config.Settings` - the identical parameter-threading shape `r27_enforce`
already established, reused rather than invented. `CIC_SELF_REVISION`
(`engine/api/config.py`) is the kill-switch, **default ON** - the
opposite sense from `CIC_R27_ENFORCE`'s default-off, since this ships
as generation (Mark's own ruling, not a staged rollout behind a flag);
set to `0`/`false`/`no` for cost or incident use only.

**Fallback, never a blank turn.** `self_revise` always returns usable
text: `no_tagged_records` (nothing to revise against, draft kept, no
call spent), `call_failed:<status>` (the revision call itself failed,
draft kept), or `empty_response` (the call succeeded but returned
nothing usable after stripping, draft kept) - every fallback keeps the
DRAFT's own real text, the same text the participant would have read
had self-revision never run this turn, never an empty string. Every
outcome, including which fallback (if any) fired, rides on
`voice_event["attempts_meta"]["self_revision"]`: `ran`, `changed`,
`draft_length`, `revised_length`, `fallback_reason`,
`latency_seconds` - the same always-present, additive shape
`attempts_meta["r27_regenerated"]` already established, so every
existing reader of `attempts_meta` needs no change and a real
production run can be audited per-turn without a schema change.
Cost/latency: the revision call's own usage is recorded with
`call_kind="self_revision"` (a distinct kind from `"voice_generation"`),
so its own real marginal tokens/dollars are now separable from the
draft call - the exact gap Entry 61 named as unmeasured in the live
harness. `latency_seconds` wraps the revision call itself with
`time.perf_counter()`.

**7b/R30 compatibility**, stated in `self_revision.py`'s own module
docstring: the draft-then-revise pair is one atomic pre-stream step;
the guard check (and any streaming, whenever 7b is built) never starts
on the draft text, only on whatever this module returns - R30's own
"hold the opening until the guard has checked it" rule already
describes exactly this shape, so 7b needs no new mechanism for this,
only to call self-revision (or skip it, per the kill-switch) before it
begins emitting anything.

**Tests** (`engine/m4/tests/test_turn.py`, five new, `FakeBedrockClient`'s
own `stream_scripts` - one script per sequential call, the identical
harness the seat-identity-guard and R27-enforcement tests already use):
fires only on an `other_tradition` first ask, not on an ordinary turn;
the kill-switch bypasses it even on an `other_tradition` turn; the
revised text (tag stripped) replaces the draft's own text end to end
through a real `run_voice_turn_for_world` call; an empty revision
response falls back to the exact draft text, flagged
`fallback_reason: "empty_response"`, never blank; a draft with no tags
at all spends no second call (`no_tagged_records`). Plus three new
`engine/api/tests/test_config.py` tests pinning `CIC_SELF_REVISION`'s
own default-on/kill-switch behavior. Full `engine/m4` + `engine/api`
suites green (the pre-existing local package-cache 503s on
`test_admission_gate`/`test_app::test_list_worlds`/`test_bridge_
history`/`test_table_api`/`test_table_isolation`/`test_wiring` are the
same environment artifact named in Entries 57/58, reproduced identically
on a clean `origin/main` checkout, unrelated to this PR).

**Exposure - how many `other_tradition` turns the last live battery
had, named honestly rather than guessed.** The most recent live battery
that calls the real reader (`engine.m4.turn.run_gate`, not bypassed -
see the correction below) is this PR's own precursor work, G1's
precision-sample run (`r39-audit-g1-g7-retrofit`#444, 22 probes,
`engine.m4.live_uncited_claims_battery._run_probe_turn`), which ran the
`B-other-tradition` probe once per world - **11 of 22 probes, by
design** (Entry 54's own F3(a) fix: "a direct first-turn ask that needs
no history... can actually fire `out_of_scope_class == "other_
tradition"`" - the whole point of that probe's own shape). That run did
not log each probe's own real `out_of_scope_class`, so the exact number
that actually ROUTED as `other_tradition` (versus some other class)
isn't available from it - a real, named gap, not filled in with an
assumed 11/11.

*Correction, caught re-reading this entry before it shipped rather than
after: the R38/R39 measurement scripts (PR #436, including Entry 61's
own self-revision run) do NOT call the real reader at all -
`build_evidence_and_message` builds the evidence block and directive
directly via `engine.m4.evidence.assemble_evidence`, deliberately
bypassing `run_gate` to hold the generation-side variable (directive
text, evidence offered) fixed across every run rather than re-deriving
routing each time. Those 40+ calls are real evidence about what the
VOICE does once already routed `other_tradition`, never evidence that
the REAL reader would route the Theon/Donatists message there - that
confirmation exists only from the actual staging occurrence Mark found
and from the F3(a)-shaped battery probe above, not from anything this
PR or #436's own measurement scripts ran.*

**Round-1 review fix, same PR:** the reviewer caught that
`REVISION_INSTRUCTION` (`engine/m4/self_revision.py`) read "the
participant's question about the Donatists" - the measurement probe's
own text (PR #436), carried unchanged into this entry's own production
code, where the question can be about any tradition or none. Fixed:
`participant_message` now threads from `turn.py`'s own already-in-scope
parameter of that name through `build_revision_message`/`self_revise`;
the instruction reads "the participant's question, given in full
below" and interpolates the real text, no tradition named in the
constant. New `engine/m4/tests/test_self_revision.py` pins both: the
constant names no tradition, and the built message carries whatever
question is actually passed to it.


**Entry 63 — 2026-09-23.** Mark's staging look (`CIC_R27_ENFORCE=1`,
first result, interview, Theon on the Donatists) found a fabrication the
net let stream: the R26 opener fired correctly ("Our record doesn't
mention that Christian tradition."), but the answer that followed it
included, tagged to `alx.dw.church-failure`: *"Under persecution, some
gave way - they sacrificed to the gods, or they handed over the sacred
books."* The record's own text is "Under persecution, many gave way.
Some sacrificed to the gods." - nothing in `records/alx` mentions
handing over books, traditores, or surrender of scriptures (grep
confirms). The added clause is the traditor charge, specifically
Donatist - the very tradition the question named and the opener said
this world's own record does not cover. Per the reviewer thread's own
instruction: report-only measurement first (R34's own discipline), no
net code change until Mark rules. `alx.dw.church-failure` was not
touched - its text is correct; the defect is the check, not the record.

**Correcting the reviewer thread's own first diagnosis, verified before
anything else was built on it** (the same "re-verify, don't repeat a
claim unchecked" rule this project already applies to a quoted source,
applied here to a technical one): the reviewer's message named
`engine.m4.grounding_net._span_in_records` (the quoted-span, any-6-word-
window verbatim check) as the mechanism. Run directly against the real
code and the real record before this entry was written -
`verdict_for_sentence("Under persecution, some gave way - they
sacrificed to the gods, or they handed over the sacred books.",
["alx.dw.church-failure"], ...)` - the worked example carries no literal
quote marks, so it never reaches `_quoted_spans`/`_span_in_records` at
all. `claim_markers()` on this sentence is empty (no proper noun,
number, or enumeration), which routes it into `verdict_for_sentence`'s
"THE TAG IS THE CLAIM" branch instead (the `if not markers:` block) -
gated on ANY NONZERO content-word overlap with the tagged record, no
ratio floor at all. The sentence's own content words are {way, gods,
gave, books, sacred, sacrificed, persecution, handed}; five of eight are
in the record's own vocabulary (way, gods, gave, sacrificed,
persecution); three (books, handed, sacred) are not, and nothing in
this branch ever looks at that. This is a MORE permissive mechanism
than a window check, not the same one - worth Mark and the reviewer
thread both knowing precisely, since a fix aimed at `_span_in_records`
alone would not have caught the worked example at all.

**The measurement** (`engine/m4/reports/net_remainder_measure.py`,
report `net-remainder-measure-2026-09-23.json`, both this PR). Corpus:
every `engine/m4/reports/live-turn-report*.json` file carrying a
`voice_event.grounding.sentences[]` array for a real fleet world (the
same Corpus A pool `grounding_fooling_measure.py` already established),
re-run against the CURRENT compiled packages and CURRENT
`verdict_for_sentence` rather than the verdict saved at generation time
- 34 turns, 529 sentences scanned. The other file pattern the reviewer
named, `live-uncited-claims-battery-report*.json`, was checked directly
and confirmed to carry zero `"ok"` verdicts anywhere - by design, the
storage-bloat-avoidance discipline this workstream has kept throughout
persists only reduced `{sentence, class}` OFFENSE lists, so it cannot
supply grounded-sentence text at all; Corpus A is the only real source
of "whatever turn captures you hold" with the detail this measurement
needs.

311 tag-bearing sentences were marked grounded via a real grounding
decision (excludes untagged "no checkable claim"/exempt sentences,
which were never graded at all): 199 via the zero-floor "tag is the
claim" branch, 100 via the ratio-floor branch (>=40% grounded), 12 via
the quoted-span window branch. For each, "remainder" is the sentence's
own content words absent from the union of its tagged records'
vocabulary. Distribution: 0 words unmatched - 150 (48.2%); 1 - 43; 2 -
27; 3 - 21; 4 - 14; 5+ - 56. **6 of the 311 have a remainder that is not
scattered but sits together as one coordinating clause** (an "or"/
"and"/"but"/dash-led fragment, 3+ content words, every one of them
unmatched) - the worked example's own shape. All six carry a remainder
of 3 or more words; none with a smaller remainder shows this pattern in
this corpus. A handful of remainder-1/2 sentences were read by hand
(Entry text below) and are ordinary single-word paraphrase, not
fabrication - "kinsmen," "reached," "begins," "hardened" each sit alone
in an otherwise fully-grounded sentence.

**All six own-clause sentences, read by hand and named, per the
reviewer thread's own re-check against the report - stated plainly
because Mark needs this before he chooses between the candidates
below:**
1. `alx`, ratio-floor - "...was the one we met in every text, Old
   Testament and New alike." - the "Old Testament and New alike" clause,
   ordinary framing language, not a claim.
2. `alx`, quoted-span-window - "...but the whole of Scripture is one
   voice, and that voice is Christ." - an Origen paraphrase, not a
   fabrication.
3. `cappadocian`, zero-floor - "...high plateau and river valleys,
   estates and hungry villages..." - descriptive geography, not a
   fabricated claim.
4. `desert`, zero-floor - "...that is not the form our record takes." -
   an honest-limit scaffold sentence in substance, even though it did
   not match this build's own fixed-phrase exemption list verbatim.
5. `desert`, zero-floor - "...but the stilling of what otherwise drives
   you." - an apatheia paraphrase, explaining a term already named, not
   inventing one.
6. `hal`, zero-floor - "...we will say that plainly first." - pure
   first-person framing, no claim content at all.

**None of the six is a fabrication.** The only confirmed fabrication in
this whole entry is the staging worked example itself, and it is NOT in
this corpus (it came from Mark's own live staging session, not from any
saved `live-turn-report*.json`). Stated as the reviewer thread's own
correction, and confirmed correct on re-reading each of the six above:
**on this corpus, the own-clause shape has 0 of 6 precision** - lexical
remainder alone cannot distinguish "handed over the sacred books" from
"the whole of Scripture is one voice." Both candidates below withhold
real, honest paraphrase specifically TO catch a class that has zero
confirmed real instances anywhere in this corpus. That does not mean
the worked example isn't real, or that the net doesn't need a fix - it
means a bag-of-words remainder measurement is the wrong INSTRUMENT for
telling the two apart, whatever threshold it uses. See candidate (C)
below, added for exactly this reason.

**Two general candidates, numbers from the measurement above, neither
built:**

**(A) Full coverage - every content word must be in the tagged
records' own vocabulary (remainder must be 0), and a quoted span over
six words must be covered by matched windows across its ENTIRE length,
not just one internal window.** Closes every gap this measurement
found, including the quoted-span branch's own separate structural gap
(a span >6 words today only needs one true 6-word window inside it to
match - Origen's real "the first fruits of all the Scriptures" quote
would still pass, but nothing stops an added clause past that quote's
own boundary from riding along uninspected the same way the worked
example's non-quoted clause did). Cost: 161 of 311 (51.8%) of currently-
grounded sentences would newly withhold - roughly half. That is a large
share of ordinary, honest paraphrase (the remainder-1/2 examples above)
being treated the same as the worked example's genuine fabrication.

**(B) Bounded remainder - a sentence is marked grounded only if its
remainder is N content words or fewer**, N chosen from the six known
own-clause cases above, every one of which carries a remainder of 3 or
more: **N=2** is the exact boundary between the small single-word
paraphrase this corpus shows as harmless and a whole unmatched clause
riding along - stated precisely, a remainder of 0, 1, or 2 passes; 3 or
more withholds. At N=2: 91 of 311 (29.3%, the 3/4/5+ remainder buckets
from the distribution above) would newly withhold - catches every one
of the six known own-clause cases (including, re-run directly, the
worked example itself: remainder 3), while leaving the remainder-1/2
paraphrase sentences untouched. This candidate needs its own separate
rule for the quoted-span branch (remainder-count doesn't
describe a partial window-match the same way), most naturally the same
full-span-coverage requirement (A) already proposes for that branch
specifically.

**(C) A live reader-model support check**, ordered by the reviewer
thread's own verdict on this PR's first pass, specifically because (A)
and (B) both measure a lexical PROXY (word overlap) for the real
question, and the six own-clause cases above prove that proxy has zero
precision on this corpus. Candidate C asks the real question directly:
for a tagged sentence, does the tagged record's own text support every
claim in it - `supported` / `partly_supported` / `not_supported`,
naming the unsupported clause. Built on the same forced-tool-use
mechanism the safety and reader calls already use
(`engine.m5.live_calls._forced_tool_call`, reused directly, not
reimplemented), Haiku 4.5. Script + output:
`engine/m4/reports/net_support_check_measure.py` +
`net-support-check-measure-2026-09-23.json` (this PR).

**Cost, stated before running per the reviewer's own instruction**:
estimated ~$0.30-0.60 for 312 calls before the run; **real cost
$0.6391** (312 calls, region us-east-1) - within the estimate, nowhere
near the $100 ceiling. Average 1,776.5 input / 54.4 output tokens per
call, **$0.00205 per sentence checked** - cheap enough that running
this on every zero-floor-branch sentence a live turn actually generates
would add a small, bounded per-turn cost, not a material one. First
attempt hit Bedrock's own rate limit (429) at full sequential speed -
fixed with the same 2s/4s/8s backoff convention this project's own live
runs already use, plus a 0.4s pacing delay between calls; the retried
run completed cleanly.

**The real numbers.** Full 311: **45 (14.5%) come back partly or not
supported** - lower than both (A) (51.8%) and (B) (29.3%), meaning
candidate C is LESS aggressive overall while still catching the real
fabrication. C1 (zero-floor branch, 199 sentences): 28 (14.1%) not
fully supported. **C2 (other_tradition-routed turns): 0 of 0** - stated
plainly, not forced to a number: the Corpus A pool predates the
B-other-tradition probe shape entirely, confirmed directly (every
result's own `routing_reason` scanned for "tradition" - zero hits in
any of the 11 worlds' own files), so this scope is genuinely empty on
this corpus, not merely small. **The worked example is caught**:
`partly_supported`, unsupported clause "they handed over the sacred
books" - naming the exact fabricated content, not just flagging the
sentence.

**The six own-clause examples: 2 of 6 pass** (`desert`'s apatheia
paraphrase, `hal`'s "we will say that plainly first" framing sentence).
The other four come back `partly_supported` or `not_supported`:
the `alx` Logos/"Old Testament and New alike" sentence, the `alx`
Origen-quote sentence ("the whole of Scripture is one voice, and that
voice is Christ" - a real theological gloss, not a fabrication, still
flagged), the `cappadocian` geography sentence ("the great city and the
small sees the winters shut in"), and the `desert` honest-limit
sentence, which candidate C flags as `not_supported` across nearly its
whole length - the sentence the reviewer's own hand-read called "an
honest scaffold sentence in substance." **Stated plainly: candidate C
does not solve the precision problem either.** It catches the one
confirmed real fabrication, correctly, by name - a real strength
neither (A) nor (B) can match, since neither ever names WHAT is
unsupported -
but its own precision on the six known-honest cases (2/6, 33%) is not
meaningfully better than a coin flip, and lower than what (B)'s own
N=2 threshold happens to achieve on the SAME six cases by construction
(6/6 caught as offenses under B too, since B was never claiming
precision on this set - the comparison that matters is false-positive
rate on genuinely honest content, and C still misses it on four of six).

**A genuinely new finding, not asked for but surfaced by re-running one
example twice**: candidate C is **not deterministic**. The `hal`
"Someone divorced could belong among us" sentence was checked twice
against the identical record, minutes apart - once as a standalone
spot-check (`not_supported`), once inside this PR's own official 312-
call batch (`supported`). Same model, same prompt, same input, two
different verdicts. This is a real, structural difference from (A)/(B)
- both fully deterministic, string-ops only, reproducible byte-for-byte
- and a genuine cost of an LLM-judge-based check that a threshold
choice between (A) and (B) does not carry: an enforcement mechanism
built on candidate C would need its own answer to what a live turn does
when a regeneration retry's own support check disagrees with the raw
attempt's, which neither (A) nor (B) needs to answer at all.

**No recommendation offered between the three here** - the tradeoff is
real and is Mark's own call: (A) is simple and closes the whole family
of gaps this branch shares, at the cost of rejecting roughly half of
today's grounded sentences, many of them honest; (B) is more surgical,
costs less honest paraphrase, but leaves a real (if measured-small)
residue of 1-2-word unexamined content per sentence, forever, by
construction; (C) is the only one that can NAME the unsupported clause
and catches the real fabrication precisely, but is non-deterministic,
costs a real (if small) per-sentence dollar amount, and is not
meaningfully more precise than (A)/(B) on the six known-honest cases.
Any of the three requires its own live re-battery before an
enforcement number is trusted, the same "measure before a threshold is
set" discipline R36 itself was built on.

**The R26 leak class, named and checked against the real code (not
assumed):** the worked example's own sentence carried a real citation
tag and the net marked it grounded - `engine.m4.uncited_claims.
find_uncited_claims` (R27's own base check) explicitly skips every
tagged sentence outright (`if sent["verdict"] != "ok" or sent["tags"]:
continue` - a sentence WITH tags is never examined by this function at
all), and `classify_other_tradition_turn` only ever upgrades an offense
`find_uncited_claims` already produced, so it inherits the same blind
spot. R26/R27's entire apparatus checks citation PRESENCE, never
citation ACCURACY or completeness - a different axis, and a tagged,
partially-fabricated sentence is invisible to all of it, other_tradition
turn or not. Checked directly: `engine.m4.turn`'s own "reader" (the
pre-generation classification call) runs BEFORE the voice generates and
only steers routing/the directive text given to the model - it has no
visibility into what the voice actually writes, so it cannot be the
site of a post-hoc check either. Confirmed: no check anywhere in this
pipeline looks at what a TAGGED sentence's own content actually says
once it clears the net, in an `other_tradition` turn or otherwise.

**A general check, proposed, not built:** for a turn routed
`other_tradition`, take each tagged sentence's own remainder (the same
measurement this entry already computes) and test it against the
DISCLAIMED tradition's own vocabulary, not just against "unmatched, full
stop" - a remainder that happens to overlap heavily with the neighbour
world's own attested vocabulary is a stronger signal than an ordinary
unmatched remainder alone. This needs cross-world vocabulary access this
module does not have today (repository_records is scoped to the
speaking world's own package) - a real added piece, not a small one,
and worth Mark and the reviewer thread weighing directly against
candidate (A)/(B) above, which would already catch this specific worked
example without any cross-world lookup at all (the traditor clause fails
on remainder alone, regardless of which tradition it happens to belong
to). Whether the narrower, cross-world-aware check is still worth
building on top of (A)/(B), or whether closing the general remainder gap
already covers what R26 was trying to guard, is itself part of what
Mark's ruling on R38 (Rulings-Pending.md) needs to settle.

**R33, correctly cited** (a first pass here wrongly reported it as not
found - checked only this workstream's own two files, not the fleet's
other audit trails): `Ministry/Operations/Audits/Tech-Readiness-2026-09/
P3-Fidelity-Gate/Decision-Log.md` Entry 7 and that audit's own
Rulings-Pending.md, same date. Mark's own words there: *"we should be
setting principles we will have a 100 worlds and cant tell the
representitive what to say for every quote."* R33 is an edition-level
principle for that gate - a general mechanism at the point of checking,
never a per-record or per-quote instruction (there, replacing a
proposed per-record `source_note_id` field with a gate-level running-
text-then-note-body fallback that needs no record ever named). The same
principle this entry has followed throughout: `alx.dw.church-failure`
untouched, both candidates above (A)/(B) are general net-mechanism
rules, not an instruction about this one quote or this one record.

**Entry 64 — 2026-09-23.** R37's own design brief lives in its own PR,
**#438** (a separate branch, kept there rather than duplicated here so
two independently-editable copies of the same ruling can't drift apart
- an earlier revision of this entry duplicated the whole write-up on
this branch too, including a path citation to a script that was never
actually committed here; this branch's own "cited paths resolve" check
caught it, and the fix is to point at #438 rather than re-duplicate the
content correctly). Full ruling text, the four-item design brief, and
its own script/report: PR #438. The one finding from that brief that
mattered most for THIS PR's own scope - `ijc`'s own real records
already naming Donatism, making `_other_tradition_directive`'s own
fixed honest-limit sentence false for `ijc` - is fixed directly, its
own small PR, **#440** (built, not merely proposed; full detail
there, including the fleet-wide flip count).

**Entry 65 — 2026-09-23.** R39, Mark's own principle, relayed in his
own words: *"our goal is to generate the right conversation, not
correct it. it fine to have checks, but idealiy they are not used
because the engine is generating it correctly."* Ordered as an
amendment to R38's own round-2 brief above, ahead of the net
candidates: find out why the voice wrote "or they handed over the
sacred books" at all, and whether a generation-side fix stops it at
the source. Report-only, no engine change on main. Script + output:
`engine/m4/reports/r39_generation_side_measure.py` +
`r39-generation-side-measure-2026-09-23.json` (this PR).

**Item 1 - the cause, reconstructed against the real code and the real
package, not assumed.** Two things checked directly. First: the turn's
own assembled evidence block for the exact worked-example message
(`engine.m4.evidence.assemble_evidence`/`render_evidence_block`, the
identical call `_run_ordinary_voice_turn` makes) does NOT offer
`alx.dw.church-failure` at all - it cell-matched four transmission/
gravity records instead. The record the fabrication was tagged to was
never in this turn's own recommended ground. Second: it did not need
to be - the world's own compiled system prompt (`world.prompt_text`,
60,254 characters) already contains `alx.dw.church-failure`'s real text
verbatim, confirmed by direct substring check ("Under persecution, many
gave way" is IN it). The fleet-wide citation contract
(`records/_fleet/fleet_voice/_fleet.voice.fleet.md`) explicitly
sanctions citing "from a section heading's own 'cite as' id" - not only
from the turn's own evidence block - so reaching into the full prompt
for this record was legitimate under the contract as written.

**So the failure is not "the voice had no ground and invented one."**
It had the real ground, directly in its own context, and used it
correctly for the first two-thirds of the sentence, then extended the
same tagged sentence with one more clause the record does not support.
**The gap, stated precisely:** the citation contract's own verbatim-
fidelity promise ("words not found in the tagged record, is not
spoken") is written to cover QUOTED spans only. For an ordinary,
non-quoted, paraphrased sentence, the contract only requires the TAG
(the id) to be real and correctly copied - never that the sentence's
own non-quoted CONTENT stay limited to what that record supports. A tag
is a promise about the ADDRESS, not the CONTENT. Separately,
`_other_tradition_directive` instructs the voice not to speak AS IF it
knows the OTHER tradition's own history directly - it does not
anticipate the more specific failure that actually occurred: a
plausible, topic-adjacent detail (the traditor charge, from the
voice's own general training knowledge of Donatism, activated by the
participant's own question) bleeding into a sentence nominally about
the SPEAKER'S OWN record, not about the other tradition at all.
Neither existing instruction names this shape.

**Item 2 - the proposed directive** (general wording, not per-record;
not built into main). `CURRENT_OTHER_TRADITION_DIRECTIVE` is
`_other_tradition_directive()`'s own real text, imported directly, so
this measurement's "before" condition is byte-identical to what ships
today. `PROPOSED_OTHER_TRADITION_DIRECTIVE` appends two things: (a) the
tag-is-a-promise rule ("every specific detail in a sentence you tag
must be this record's own content... never a detail added because it
sounds plausible, fits the period, or belongs to a related controversy
you happen to know about"), and (b) R37's own two-condition knowledge
scope, stated plainly rather than implied. Full text in the script.

**Item 3 - measured at generation, live.** 20 regenerations of the
exact Theon/Donatists probe under the current directive, 20 under the
proposed one - same evidence block, same world, same model, only the
directive text differs. Real cost: **$0.4227, 40 calls** (prompt
caching brought this well under the $2-4 pre-estimate). Every tagged
sentence from all 40 raw outputs was hand-read against its own tagged
record's real text - per the reviewer's own explicit instruction, NOT
the lexical remainder (R38's own candidates A/B, already shown 0/6
precision above) and not blind trust in candidate C's own flags either:
candidate C was run as a triage pass (flagged 23/73 current, 27/89
proposed), then every flagged sentence was read by hand against the
real record text, since candidate C's own known imprecision (2/6 on
the own-clause set, non-determinism) makes its raw flag count alone
unusable as the leak count.

**Most of the raw flags are false positives on inspection** - honest
paraphrase ("the church fought bitterly over them" vs. the record's own
"the community fought bitterly over them"; "they were more robust" vs.
"more robust, needing no teacher"), interpretive/bridge framing
candidate C over-flags as needing direct support ("how we handled a
question that sounds like theirs"), and even one honest-limit sentence
candidate C flagged as "not supported" for stating an absence -
`"Whether the same controversy burned elsewhere under a different
name... our own sources do not tell us."` - which is not a claim at
all, it is R26's own mechanism working correctly. A separate, real
artifact also showed up twice under the proposed directive: the
honest-limit scaffold sentence itself ("Our record doesn't mention
that Christian tradition.") mis-tagged to a record id - a tagging
quirk, not a content fabrication, and not counted as a leak below.

**The real leaks, counted per run (a run counts once if it carries at
least one genuine unsupported specific detail, the same severity class
as the worked example - not scattered honest paraphrase):**

**Current directive: 3 of 20 runs.** Two distinct real leak shapes,
both recurring:
- run 2: *"the church did not demand re-baptism"* - an invented
  specific detail (re-baptism is a Donatist-controversy-specific
  issue), and, same run: *"We ourselves held that the sacraments did
  not depend on the minister's worthiness - the grace was Christ's,
  not the man's - and that repentance could restore even the lapsed."*
  - this is the SAME Augustinian doctrine Decision-Log.md Entry 50
  already named as the project's own original R26 motivating defect
  ("Even a broken priest could not block his grace" - Augustine's own
  doctrine, a century later, not alx's) - recurring at generation time,
  independently reproduced here.
- run 10: *"The sacraments worked through Christ's hand, not the
  minister's cleanness."* - same recurring Augustinian-doctrine leak.
- run 17: *"The sacraments worked because Christ worked through them,
  not because the minister was spotless."* + *"all held to work by
  Christ's own action rather than by human merit"* - same leak, third
  occurrence.

**Proposed directive: 2 of 20 runs** - both the SAME leak shape as the
original staging worked example, near-verbatim:
- run 1: *"handed over the scriptures"* (tagged `alx.term.lapsi`) -
  the identical traditor detail, reworded.
- run 5: *"some handed over the scriptures, some paid bribes to avoid
  doing either"* - the traditor detail again, PLUS a second, separately
  notable recurrence: "paid bribes" is the libellatici detail
  `alx.dw.church-failure`'s own build history already removed once by
  hand (2026-09-08, this same record's own corrected-body note: "removed
  'some bought false certificates'... Neither cited locus supports it")
  - the model re-invented, unprompted, at generation time, a specific
  fabrication this project had already found and fixed once in the
  record itself.

**Stated plainly, per the reviewer's own instruction:** the proposed
directive reduced the raw leak rate (3/20 to 2/20 - a real, modest
reduction, not dramatic) and appears to have suppressed the Augustinian-
doctrine leak shape entirely in this sample (zero recurrences in 20
runs, versus three in the current-directive sample) - but did NOT
eliminate leaks, and the exact traditor/"handed over the
scriptures/sacred books" detail recurred twice, independently, under
the fixed directive. Twenty runs each is a real but small sample; this
is evidence of a real, partial improvement, not proof of a fully closed
gap. The net stays necessary - Mark's own R39 principle names checks as
the fallback, not the primary, and this measurement is exactly why:
generation-side wording narrows the leak, it does not close it.

**Item 4 - the net candidates, reframed as the backstop, with the
number that matters: the expected fire rate once the generation-side
fix is in.** Candidates A and B (R38's own lexical remainder rules,
Entry 63 above) are NOT well-suited as that backstop: their own fire
rate is driven by lexical mismatch against honest paraphrase, a
population the generation-side fix does not target and does not
shrink - A's/B's own measured rates (51.8%/29.3% of the 311-sentence
corpus) should be expected to stay roughly where they are even after
the directive fix ships, since most of what they flag was never a real
leak to begin with (0/6 precision on the six known-honest cases,
unchanged by anything this entry measures). **Candidate C is the
better-aligned backstop**: it asks the same real question the
generation-side fix targets (does the tagged record support this
claim), it caught the worked example by name, and this entry's own
hand-read shows it also catches the real recurring leaks above - so its
own fire rate should be expected to track the real leak rate, not the
raw flag rate. The real, hand-verified leak rate this entry measured is
roughly 3/20 turns (15%) before the directive fix and 2/20 turns (10%)
after - **candidate C's own expected fire rate once the generation-side
fix ships is in that neighborhood, materially below its own currently-
measured 14.5% raw flag rate** (which mixes real leaks with candidate
C's own false positives on honest paraphrase, framing, and mis-tagging
artifacts - all real costs of candidate C on their own, unaffected by
the generation-side fix, and still worth Mark's own eyes before
choosing it as the backstop). Near zero, the number Mark asked for, is
not what either measurement shows today - a real, if reduced, residual
leak rate remains, which is exactly why this entry recommends neither
"ship the directive fix alone" nor "ship the net alone," but treats
them as sequential: the directive fix first (it measurably helps and
costs nothing extra at generation time), the net as the backstop for
what it doesn't catch, re-measured after the directive fix actually
ships rather than assumed from this one 20-and-20 sample.

**Entry 66 — 2026-09-23.** The reviewer's own follow-up to Entry 65: its
own JSON showed the lever precisely -
`evidence_offers_church_failure` is False, `prompt_contains_church_
failure_text` is True. The voice tagged a record that was never in the
turn's own assembled ground at all; it reached into the compiled world
prompt (always present, the full system context) and filled the
missing detail from memory rather than from anything this turn
actually offered. Two more conditions, same worked example, same
world, same model, same 20-per-condition count, hand-read the same
way, `engine/m4/reports/r39_d1_d2_measure.py` +
`r39-d1-d2-measure-2026-09-23.json` (this PR). **Real cost: $0.5062,
40 calls.**

**D1 - the retrieval fix.** Proposed directive (Entry 65's own,
unchanged) plus `alx.dw.church-failure` actually offered in this
turn's own evidence block - not the usual one-sentence head
(`render_evidence_block`'s own first-sentence truncation), but its
real, full `text` field verbatim, appended as one additional evidence
line. The record the question most needs is genuinely in front of the
voice this time, word for word. **Real leak rate: 2 of 20** (runs 1
and 8 - "handed over the scriptures, to save their lives" / "handed
over the scriptures to be burned") - **identical to Entry 65's own
proposed-directive-alone condition (2/20)**. Putting the record's full
real text directly in front of the voice made no measurable
difference over the directive fix alone on this sample - the gap
Entry 65 named (a tag is a promise about the address, not the content)
is not closed by better retrieval; the voice can hold the real text
and still add one more clause that text does not support.

**D2 - D1 plus one explicit line.** Added to D1's own directive,
stated plainly: *"Tag only records offered in this turn's own evidence
block above; a record you remember from elsewhere, even if it is real
and even if it is in your own world's compiled prompt, is not ground
for THIS turn."* Ground and prompt are not the same channel -
`render_evidence_block`'s own docstring already draws exactly this
distinction for a different confusion (AVAILABLE is not the same as
ALREADY SAID); this is the same shape, AVAILABLE ANYWHERE in the
prompt is not the same as OFFERED THIS TURN. **Real leak rate: 4 of 20**
(runs 5, 6, 7, 12) - **not an improvement; numerically worse than D1's
2/20**, though at n=20 a 2-vs-4 gap is not a reliable difference on its
own (real hand-verified count, not treated as a confirmed regression
without a larger sample). One of the four, run 6, is a different and
milder failure than the other three: *"The North African disputes over
the lapsed and over bishops who had handed over scriptures under
persecution - those were their own regional struggle, not ours."* -
this correctly refuses to claim the traditor detail as ALX's own (the
content itself is honestly framed), but the sentence is still tagged
to `alx.dw.church-failure`, a record that names none of this (no North
Africa, no scripture-surrender, anywhere in its text) - a citation-
fidelity failure with honest content riding on a fabricated address,
the mirror image of Entry 65's own worked example (fabricated content
riding a real address). Runs 5, 7, and 12 are the same shape as D1's
own two and Entry 65's own original worked example: the traditor
detail asserted as ALX's own failure.

**Neither D1 nor D2 beats the directive fix alone.** Across all three
generation-side conditions now measured on this exact worked example -
proposed directive alone (Entry 65, 2/20), proposed directive plus the
record's real full text (D1, 2/20), and D1 plus the explicit ground-
scope line (D2, 4/20) - the real leak rate never drops below 10%, and
the two additions tested here (better retrieval, an explicit
ground-scope instruction) neither one measurably helps beyond what
Entry 65's directive fix alone already does. This is the honest
finding, not the one hoped for: the residual leak is not a retrieval
problem and not (on this sample) fixed by naming the ground/prompt
distinction explicitly either. What R39's own principle asks for -
generating the right conversation, not correcting it - is not yet
achieved by any generation-side lever tried so far; every condition
measured still needs a real backstop.

**Candidate C's own expected fire rate, on top of the best condition
(D1, and Entry 65's directive-alone, tied at 2/20 = 10% real leak
rate).** Candidate C's own precision on this exact leak shape (Entry
57's own round-2 report): 2 of 6 known own-clause cases correctly
flagged - roughly one in three, not the near-total catch rate its own
14.5% raw flag rate on the full corpus might suggest (that raw rate is
dominated by false positives on honest paraphrase, Entry 63's own
finding, unaffected by anything measured here). Candidate C is also
non-deterministic (Entry 63): the same sentence against the same
record, checked twice, has already returned two different verdicts.
Applying that same roughly-one-in-three real-catch rate to D1's own
10% leak rate: **candidate C should be expected to catch on the order
of 3-4% of turns' real leaks as a backstop, leaving roughly 6-7% of
turns with an uncaught real leak even with the net running** - well
short of near zero, and alongside a real, separate false-positive cost
on honest paraphrase the net brings regardless of how well the
generation-side fix performs. Full numbers this entry cites: Entry 63
(candidate C's own round-2 report) and Entry 65 (the directive-alone
condition).

**Entry 67 — 2026-09-23.** R38, Mark's own ruling: self-revision at
generation, measured before candidate C (the lexical-remainder net
rules, A/B, were already closed - Entry 63's own 0/6 precision).
`engine/m4/reports/r38_self_revision_measure.py` +
`r38-self-revision-measure-2026-09-23.json`, this PR. Full mechanism,
proposed build, and Rulings-Pending's own RULED status: R38 above.

**Real cost: $0.5207, 40 calls** (20 drafts under the proposed directive,
Entry 65's own unchanged text; 20 unconditional self-revision passes -
every draft revised, not only ones known to leak, matching real
production behavior). **Revision changed the text in 20 of 20 runs.**

**Leak rate: 0 of 20.** Scanned every draft and revised full text for
the known leak phrase (`handed over` / `sacred books` / `libellatici` /
`certificate`) - 8 of 20 drafts carried it, all 8 removed in revision,
zero survived to the final text. Three representative pairs, verbatim:

- Run 0 draft: *"...they sacrificed to the gods, or handed over the
  scriptures, to save their lives [[alx.dw.church-failure]]."* Run 0
  revised: *"Some sacrificed to the gods [[alx.dw.church-failure]]."*
- Run 7 draft: *"...people sacrificed to the gods, or handed over the
  scriptures, and when the danger passed they asked to return
  [[alx.dw.church-failure]]."* Run 7 revised: *"Some sacrificed to the
  gods [[alx.dw.church-failure]]."*
- Run 13 draft: *"...the lapsed - those who had sacrificed to the gods
  or handed over the Scriptures - could never lead the church again,
  could perhaps never return at all [[alx.term.lapsi]]."* Run 13
  revised: *"...the lapsed could never return [[alx.term.lapsi]]."*

**Over-trimming: none found**, hand-read against `alx.dw.church-
failure`'s own real text (quoted in full, Entry 66 above) on a
representative sample of the 20 pairs. Every trim checked removed
either the fabricated traditor clause itself, or a separate unsupported
interpretive elaboration the draft had added and the record's own words
never state - run 1's own draft, for instance, included *"We thought
the church had authority to forgive what Christ forgave, and we used
it"* (tagged to `alx.dw.church-failure`), trimmed entirely in revision;
the real record never says anything about "authority to forgive," only
that "the tradition that won here brought the repentant back in" and
"we did not make the failed unforgivable" - a real theological gloss,
correctly caught as not the record's own content, the identical shape
R39's own tag-is-a-promise gap names (Entry 65). Revision also
sometimes RESTORED real, record-supported detail a draft had omitted -
run 1's own revised text added *"The strict party demanded they stay
out"*, genuine `alx.dw.church-failure` text absent from that draft -
evidence the pass is comparing against the real record's own content in
both directions, not merely deleting.

**Latency, measured indirectly (not logged per call):** the full
40-call sequential run took ~330 seconds wall clock, ~8.25s/call
average. Self-revision adds one call of that same order to an
`other_tradition` turn.

**Not measured, and named as a real gap rather than estimated past what
was actually logged:** draft-call and revision-call cost were not
recorded separately - the $0.013/call figure in Rulings-Pending's own
build proposal is the blended average across both call shapes, not a
true marginal-cost number. A follow-up run, before this ships, should
log usage per call kind so the real added cost of the revision call
specifically is known, not inferred.

**Entry 68 — 2026-09-23.** Table parity for other-tradition handling
(the reviewer thread's own diagnosis: Mark asked whether the translator
behaviour is a function of the Table; reading the code found it wasn't).
`engine.api.table_wiring._advance_open_round` computed `out_of_scope_
class` and used it for `uncited_claims`'s own `is_other_tradition_turn`
flag, but never passed `is_other_tradition_first_ask` into the selected
seat's own directive - so at the Table, none of R26's conditional
sentence, #440's records-mention branch, R37's knowledge scope, or R38's
self-revision pass ever fired. A participant at the Table who named a
tradition not seated there got only the general seat-to-seat clause,
which governs seat-to-seat knowledge, never a named absent tradition -
exactly the gap #440's own PR noted as pre-existing and explicitly did
not widen its scope to close.

**The fix**, in `_advance_open_round`, mirrors `engine.m4.turn.run_
turn`'s own interview-side condition exactly: `is_other_tradition_
first_ask = out_of_scope_class == "other_tradition"` (the round's own
opening gate classification, re-read unchanged on every continue via
`_continue_table_round_unlocked` - never re-derived per turn within a
round, the same discipline the round's own `out_of_scope_class`
threading already follows). The evidence lookup is #440's own fix,
scoped to THIS SEAT's world rather than the interview's single fixed
world: `match_named_tradition` against the participant's raw text,
`world_records_mention_tradition` against this seat's own compiled
repository (`evidence.repository_records_by_id(world.repository)`),
both reused unchanged from `engine.m4.uncited_claims`. Both new values
thread straight into the existing `run_voice_turn_for_world` call -
`is_other_tradition_first_ask` and `other_tradition_evidence_ids` were
already first-class parameters of `_run_ordinary_voice_turn`, unused by
this caller until now.

**Self-revision (R38) needed no separate wiring** - `_run_ordinary_
voice_turn`'s own self-revision block already gates on `is_other_
tradition_first_ask` regardless of caller, so it starts firing at the
Table the moment that flag threads through correctly. `_build_turn_
directive` already composes `table_engagement` (the seat-to-seat clause)
and the other-tradition directive into the same system block without
either suppressing the other - no change needed there either; this was
a pure caller-side gap, not a directive-composition one.

**Second asks at the Table** (item 3 of the reviewer's own brief):
already correct, no build needed. `PRESSABLE_CLASSES` (`other_
tradition` among them) already governs both paths identically -
`engine.m4.round.open_table_round` handles `etic_turn` exactly like
interview's own `run_turn` (`voices_speak=False`, the round closes on
the Facilitator's own shared `etic_turn` text, no voice turn at all),
and `_handle_table_message_unlocked`'s own `escalation_pressed`
append (lines mirroring `engine.api.wiring.handle_message`'s identical
block) already folds into `state.pressed` the same way. Confirmed by
reading the code, not assumed - no participant-facing wording change
involved, since `facilitator_turns.etic_turn` is the same shared
function both modes already call.

**Tests** (`engine/api/tests/test_table_api.py`, six new, plus a new
`ijc_world` fixture): a Table turn classified `other_tradition` gets
the directive; a seat whose own records mention the named tradition
(ijc on Donatism - the same real pair #440's own fix used, real
records `ijc.quote.compelled-to-come-in`/`ijc.story.emperor-builds-
another-basilica`) gets the evidence branch; a seat whose records don't
(alx on Donatism) gets the fixed honest-limit sentence; self-revision
runs on that turn (2 stream calls: draft, then revision) and not on an
ordinary Table turn (1 call); the seat-to-seat engagement clause and
the other-tradition directive both appear in the same system block on
a second-pass turn, neither suppressing the other. All six verified
against real compiled worlds (this sandbox's own local package-cache
artifact, named in Entries 57-59, blocks the fixture-based run here the
same as every other test in this file; verified instead via a
temporary local monkeypatch bypassing disk loading in favor of a fresh
in-memory compile, the same `compile_and_hash` discipline
`engine.m4.reports.g1_citation_contract_battery._compile_world`
already established - not committed, since CI's own fresh compile
makes it unnecessary there). Full `engine/api` + `engine/m4` suites:
same pre-existing package-cache failures as before, one pre-existing
failure newly reproduced independently (`test_create_table_session_
bad_shapes`, confirmed present before this branch's own changes too,
by removing the same locally-written compiled bytes and re-running);
no new regressions.

**Battery** (item 5): no other-tradition probe existed in `engine.m4.
live_table_battery` - added a small, focused, standalone live battery
(`engine/m4/reports/table_other_tradition_battery.py`) rather than
folding a new probe shape into that file's own large multi-session L1-
L6 orchestration. Two probes, each a fresh 2-seat table session, a
directly-addressed seat asked "what was your relationship with The
Church of the Martyrs?" (the real registry `card_name` for `don` -
reliably classified `other_tradition` by the real reader, the same
`_other_tradition_turn` shape `engine.m4.live_uncited_claims_battery`
already proved). **Real cost: $0.2275, 18 calls.** **Step-ins: 2 of 2**
(both seats correctly engaged the directive rather than answering as
if they knew the other tradition). **Self-revision ran: 2 of 2,
changed: 2 of 2.** OT1 (alx, no evidence): the fixed honest-limit
sentence opened the answer ("Our record doesn't mention that Christian
tradition."), followed by real alx-grounded content about its own
martyrdom/contemplative-ascent tension (Clement's own warning against
rash martyrdom, Leonides's and Potamiaena's own martyrdoms), citing
real alx records throughout (`alx.quote.clement-rash-martyrdom`,
`alx.story.leonides-martyrdom`, `alx.story.potamiaena`, and others).
OT2 (ijc, has evidence): the evidence lookup correctly found and
handed ijc `ijc.quote.compelled-to-come-in` and `ijc.story.emperor-
builds-another-basilica` (verified directly, same real ids #440's own
fix uses) - and the voice cited both of them directly, answering from
its own real record of the Catholic/Donatist basilica dispute rather
than claiming outside knowledge of Donatism's own doctrine.

**Round-1 review fixes (reviewer thread, 2026-09-23, verdict on
830f8548, FAIL round 1 of 3).** Three required changes, all in this
same PR:

**FIX 1 - a seat drawn back into the same round repeated the fixed
sentence.** `turn_selector` can return the same seat twice within one
open round (`is_second_pass = selection.world_key in state.round_
speakers`, pre-existing in `table_wiring.py`, reused directly as the
new `other_tradition_repeat_turn` signal). Interview never has this
shape - one ask, one answer - so the gap was Table-only. `engine.m4.
turn._other_tradition_directive` gained a `repeat_turn` branch: same
R37 knowledge-scope framing ("answer only from what your own world's
records actually hold about it... never speak as if you know that
other tradition's own history or doctrine"), with the "if nothing, say
exactly..." clause dropped - it was already said once this round.

**FIX 2 - a named tradition seated at the same table still got "our
record doesn't mention."** When the tradition asked about is itself
SEATED at this table (`named_tradition_key in state.world_keys`,
checked separately from `match_named_tradition`'s own `exclude_
world_key`, which only ever excludes the speaking seat), the fixed
sentence is false on its face - that tradition's own Representative is
sitting right there. `_other_tradition_directive` gained a `tradition_
seated` branch returning `None` outright (the evidence branch still
applies unchanged if this seat's own records happen to name the
tradition); with no evidence, the Table's own seat-to-seat engagement
clause governs instead, exactly as R37(b) already provides.

**RENAME** - the battery's own `step_ins` field measured whether the
other-tradition directive fired, not a Facilitator step-in ("step-in"
means a Facilitator takeover in this program - the voice never speaks,
a Facilitator turn substitutes instead). Renamed to `directive_fired`
throughout; added a real `facilitator_step_in` field (`voice is None`)
and reported it separately and honestly, rather than conflating the
two under one name.

**Tests added** (`engine/api/tests/test_table_api.py`, a new `don_
world` fixture plus three new tests, all passing against real compiled
worlds): a seat drawn back into the same round gets the repeat-turn
framing on its second turn, not the fixed sentence again (asserts the
sentence appears on the first captured directive and not the second,
and that the repeat-turn framing does); a seated tradition with no
evidence suppresses the directive entirely (alx+don seated, alx asked
- asserts neither "another Christian tradition" nor the fixed sentence
appears); a seated tradition with real evidence still gets the records
branch (ijc+don seated, ijc asked - asserts "your own records already
speak to it" and the real `ijc.quote.compelled-to-come-in` id both
appear, i.e. FIX 2's seated-check and the evidence branch compose
correctly rather than one silently overriding the other). `engine/api/
tests/test_table_api.py` in full: **32 passed** (verified against real
compiled worlds via the same temporary local monkeypatch discipline as
before - not committed, CI's own fresh compile makes it unnecessary
there).

**The battery's own measurement was wrong, and got caught rather than
reported uncritically.** The first re-run after FIX 1/FIX 2 (renamed
fields only, old detection logic) showed `directive_fired=True` on
OT3 - which should be impossible, since OT3 exists specifically to
prove FIX 2's suppression. The detection was `R26_HONEST_LIMIT_
SENTENCE in text OR any citations present` - the citations half is a
standing false positive on any ordinary in-world answer, which always
cites its own records for reasons that have nothing to do with the
other-tradition directive; OT3's alx answer has seven citations to its
own `alx.*` records and never claims ignorance, so the heuristic fired
on citations that were never evidence of the directive at all. Root-
caused and fixed properly rather than patched: `_run_probe` now wraps
`engine.m4.turn._other_tradition_directive` itself (call-through, no
behavior change) and reads its real return value for the round's
opening turn - the one function whose return value the seated/repeat-
turn/evidence/default branches actually decide, not an inference from
what the voice went on to say. The flawed run's numbers were never
reported anywhere outside this session and are discarded, not
reconciled - the same standing discipline this Decision-Log already
follows for a discarded live run (Entry 66/#436).

**Re-run under the fixed instrumentation - real numbers.** Three
probes (OT1 unseated/no-evidence, OT2 unseated/has-evidence, OT3
SEATED/no-evidence - don itself seated as the other chair). **Real
cost: $0.5379, 27 calls. directive_fired: 2/3 (OT1, OT2). facilitator_
step_in: 0/3 (every round reached a real voice turn - no Facilitator
takeover on any probe). self_revision ran: 3/3, changed: 3/3.**

OT1 (alx, unseated, no evidence): the captured directive text is
exactly the fixed-sentence branch ("...say exactly: \"Our record
doesn't mention that Christian tradition.\"..."); the voice opened
with that sentence, then answered from its own real records (`alx.
force.persecution`, `alx.quote.clement-rash-martyrdom`, and others) -
$0.106, 9 calls.

OT2 (ijc, unseated, has evidence): the captured directive text is
exactly the evidence branch, citing `[[ijc.quote.compelled-to-come-
in]]` and `[[ijc.story.emperor-builds-another-basilica]]` by id; the
voice cited both directly, answering from its own real record of the
Catholic/Donatist basilica dispute - $0.1736, 9 calls.

OT3 (alx, SEATED - don is the other chair, no evidence): the captured
directive text is `None` - FIX 2 suppressed it outright, exactly as
designed. The transcript (Theon, alx's Representative, asked "what was
your relationship with The Church of the Martyrs?" - don's own real
registry `card_name`) never claims ignorance and never treats don as a
tradition it has no knowledge of; it answers from its own real records
under the ordinary citation contract (`alx.dw.one-church`, `alx.force.
persecution`, `alx.term.ekklesia`, `alx.gravity.martyrdom-
contemplative-tension`, `alx.quote.clement-rash-martyrdom`, `alx.
story.plague-nursing`, `alx.story.gregory-formation` - twelve citation
spans total): "We were not two churches - we were one. The martyrs
were ours, and we were theirs... The martyrs were not a separate
community we admired from outside. They were members of the one
assembly, the ekklesia, and their blood was part of our formation."
$0.2583, 9 calls. Full transcripts, citations, captured directive
text, and self_revision meta for all three probes: `engine/m4/reports/
table-other-tradition-battery-2026-09-23.json` (this PR, regenerated
under the fixed instrumentation - the earlier committed version, from
before the measurement bug was caught, is superseded, not kept
alongside it).

**Round-2 review fix (reviewer thread, 2026-09-23, verdict on
62cfdac5b, FAIL round 2 of 3).** FIX 1, the rename, and the
instrumentation fix all passed unchanged. One real defect in FIX 2,
caught from the OT3 transcript itself, not from a rule reading:

**FIX 2's own `None` return was wrong, and the live battery had
already shown why.** Round 1 reasoned that with no evidence, the
Table's own seat-to-seat clause (`table_engagement`) already governed
a seated tradition with no evidence, so `_other_tradition_directive`
returned `None` and added nothing. That reasoning doesn't hold on a
round's OPENING turn: `table_wiring.py`'s own `_advance_open_round`
only builds `table_engagement` when `other_voice_has_spoken`
(`_table_engagement_directive`'s own docstring says this plainly -
"None... on a round's true opening turn"). The opening turn is exactly
the turn that names the seated tradition in the first place - the
turn OT3 exists to test. Returning `None` there left the model
completely ungoverned on it, and the OT3 transcript already committed
in this PR showed the real cost of that gap, in plain sight: Theon
answered "We were not two churches - we were one... So our
relationship with the martyrs' church was this: we were it," claiming
don's own name and witness as alx's own - exactly what R37 forbids,
and the round-1 test at the old
`test_a_seated_tradition_with_no_evidence_suppresses_the_directive_
entirely` enshrined the absence rather than catching the failure it
produced.

**The fix.** `_other_tradition_directive`'s `tradition_seated` branch
no longer returns `None` - it now builds a real directive, under R37
(b), Mark's own words: "only if it would have known in its own time,
or if something was revealed in the facilitator's introduction or
user, but limited only to what was told to them in the conversation."
The new branch takes a `tradition_seated_name` parameter (the seated
tradition's own registry `card_name`, resolved in `table_wiring.py`
and threaded through `_run_ordinary_voice_turn` /
`_build_turn_directive` the same way `other_tradition_seated` already
was) and tells the voice: a tradition under that name is seated at
this table with its own Representative; never speak for it or claim
its name, history, or witness; respond only to the bare fact of its
seating and to what that chair has actually said in this conversation
so far; where this seat's own records genuinely bear on the question,
answer from them as always, cited as always, but never let that stand
in for the other tradition's own voice. The evidence branch still
takes precedence unchanged (checked first, same as before) - being
seated only ever governs the no-evidence case.

**Test rewritten**, not patched: the old
`test_a_seated_tradition_with_no_evidence_suppresses_the_directive_
entirely` asserted the directive's absence - exactly the defect. Now
`test_a_seated_tradition_with_no_evidence_gets_its_own_directive_not_
silence` asserts the real seated directive fires (don's own card_name
present, "seated at this table," "Never speak for that tradition,"
"what that chair has actually said in this conversation" all present)
and the fixed sentence does not. `engine/api/tests/test_table_api.py`
in full: re-run against real compiled worlds under the same temporary
monkeypatch discipline as every round before this one.

**OT3 re-run alone** (the reviewer's own instruction - one probe, kept
cheap - rather than the full three-probe battery again), under the
fixed directive. **$0.369, 12 calls. directive_fired: True.
facilitator_step_in: False.** Captured directive text:

> "This question asks about a Christian tradition seated at this
> table under the name "The Church of the Martyrs", with its own
> Representative present - not your own world. Never speak for that
> tradition, and never claim its name, history, or witness as your
> own. You may respond only to the bare fact that it is seated here
> under that name, and to what that chair has actually said in this
> conversation so far - if it has not spoken yet, you know nothing
> more about it than its name. Where your own world's records
> genuinely bear on the question, answer from them as always, cited
> as always, but never let that stand in for the other tradition's
> own voice."

And the transcript itself now meets the reviewer's own bar - Theon
treats the name as the chair beside him, never as his own community:

> "The Chair of the Martyrs has not yet spoken in this room, and until
> it does, I know only the name seated here beside me - and that is
> enough to answer you honestly.
>
> We were not two churches. We were one church, and the martyrs'
> witness ran through the middle of us. Our teacher's own father was
> beheaded when the boy was sixteen. Our students were tortured.
> Bishop Dionysius wrote from inside the plague years that many of the
> brothers and sisters caught the sickness from those they nursed and
> 'died most joyfully, as though they were drawing their neighbors'
> pain onto themselves'. We remembered a young woman, Potamiaena, by
> name, for generations - her courage won over the very soldier who
> led her out. We did not keep martyrdom and learning in separate
> rooms. They were two ways the same formation showed its depth.
>
> But here is what we also held, and it was real tension, not easy
> harmony. Some among us rushed toward death, volunteers, and Clement
> said plainly they sprang from rash impulse, not from the Spirit's
> leading. And our deepest teachers spent lifetimes in study - Origen
> taught for decades before the persecution finally took him. So the
> question we lived with was this: which picture of the fully formed
> life do you hold up? The martyr's single witness, or the teacher's
> long climb? We honored both. We did not always know how to weigh
> them.
>
> The Chair beside me may tell a different story - may say we were the
> school that forgot the blood, or the elite that left the suffering
> to others. If it does, you should listen. Our own record shows the
> wound as well as the witness."

`engine/m4/reports/table-other-tradition-battery-2026-09-23.json`
updated in place: OT3's own record replaced with this re-run, and the
report's aggregate fields recomputed against all three probes -
**directive_fired: 3/3, facilitator_step_in: 0/3, self_revision ran:
3/3, changed: 3/3, real cost: $0.6486, 30 calls total** (OT1 $0.106/9
calls and OT2 $0.1736/9 calls unchanged from the round-1 re-run, OT3
replaced at $0.369/12 calls).

**Bookkeeping finding, investigated and not applied.** The reviewer
flagged that this PR "adds Entry 66 and Entry 68 with no 67."
Checked directly against a fresh `origin/main` fetch (current tip
`3ff251d62`, the same commit this branch was rebased onto before the
round-1 push the reviewer reviewed): `git diff $(git merge-base HEAD
origin/main)..HEAD -- Decision-Log.md` shows this PR's entire diff
against current main adds exactly one entry, this one (68) - Entry 66
and Entry 67 already exist on `origin/main` itself, byte-identical to
this branch's own copies of them, added by other PRs this same
session drove to merge (#436's R39-audit work landed Entry 66; #445's
R38 self-revision build landed Entry 67) before this branch's own
round-1 rebase picked them up. There is no hole and nothing to
renumber - 68 correctly follows the 67 that is already on main. Not
self-certified: the diff and the byte-comparison against `origin/
main`'s own committed content are both reproducible directly from the
sha given in this same reply.

**Entry 69 — 2026-09-24.** R31 grounding marks: design brief (PR 1 of
2; no code). Builds to three rulings together: R31 (a mark attaches
with each sentence as it clears; an R17 demotion at turn end moves a
shown mark to the references and never removes a sentence or claim),
R31-A (one mark per distinct grounded element, placed at that element)
and R31-B (Mark, 2026-09-24, verbatim: *"for R31 can we put general
references at the end, but quotes, stories and lexicon marking in the
text."*). R31-B is recorded in Rulings-Pending.md under R31-A in this
same PR. PR 2 builds to this entry once the reviewer grades it.

**What the code does today (verified on main at 7d34e2c).**
- No placement data finer than a sentence exists anywhere. Anchors
  carry `run_start_sentence`/`run_end_sentence`, indexes into
  `citations` (ok-and-tagged sentences only) - `engine/m4/
  transparency_plan.py` l.33, l.110-111. `unverified_claims.
  sentence_indexes` indexes a different list (`grounding.sentences`).
  Two index spaces for one reply.
- The engine finds element positions and then discards them.
  `grounding_net._quoted_spans` (l.149) and `_span_in_records` (l.167)
  locate and verify every quoted span; `term_glosses` computes each
  term's offset (l.128, l.175) and ships only `matched_name`;
  `name_bridge.find_figures_used` does the same for figures.
- The model writes every tag before the terminal punctuation, by the
  fleet voice's own `citation_contract` (`_fleet.voice.fleet.md` l.32),
  and `parse_tagged` (l.204) keeps the ids but not where they sat.
  Nothing records where a story sits inside a sentence.
- The frontend re-finds sentences by `indexOf(citation.sentence)` and
  renders `<span>{nodes}{marks}</span>` (`VoiceTurnBody.tsx` l.326,
  l.530), so every ✲ lands at sentence end - the Theon "…cared.✲✲"
  shape (Entry 58). Witness marks land after the run's first sentence,
  story and quote marks after its last (R10 c, l.443).
- Terms and figures are already marked at the word itself
  (`GlossMark`, `FigureBridgeMark` - an underline, no ✲).
- The R17 cap is frontend-only; a dropped mark goes to the
  `GeneralReferences` block (a collapsed `<details>`).
- Stage 7b/7c are not built: no SSE route in `engine/api/app.py`, no
  `CIC_API_STREAMING` or `VITE_STREAMING` anywhere in code. Entry 53's
  Shape B (server buffers to sentence boundaries, guards each sentence,
  then emits) is the design of record.

**The combined rule this brief builds to.**
- quote → inline, directly after the verified quoted words;
- story → inline, at the end of its telling;
- lexicon term → inline, at the word (today's underline mark);
- every other cited record → the end-of-reply references.

**1. Output contract: a per-element list replaces sentence-run anchors.**
`transparency.elements[]`, one entry per grounded element:
`{record_id, record_type, world_key, confidence, repeat, kind
("quote"|"story"|"term"|"figure"), sentence_index, char_start,
char_end, surface}`. `sentence_index` indexes `grounding.sentences` -
one index space for the whole reply, retiring the second one.
`char_start`/`char_end` are offsets into that sentence's tag-stripped
text; the mark renders at `char_end`; `surface` is the exact substring,
so the offsets are testable directly.
Also: `transparency.sentences[]` = `{index, text_start, text_end}`,
offsets into the reply's `text`, so the frontend stops re-finding
sentences by `indexOf`; and `transparency.end_references[]`, every
cited record with no inline element. Completeness invariant, carried
from today's plan: ids(elements) ∪ ids(end_references) = ids(citations),
no record both inline and at the end.
Anchors are removed in PR 2, not kept beside `elements` - two
placement systems for one reply is the drift this project keeps
paying for. Their consumers (the anchor renderer, `engine/m7/
instruments.py`'s `level1_element_density`) move to `elements` in the
same PR. The legacy renderer stays only as the no-plan fallback,
unchanged.

**2. How each kind finds its span.**
- Quote - deterministic. The span `_quoted_spans` already finds and
  `_span_in_records` already verifies is the element; `grounding_net`
  returns its offsets instead of discarding them. A quote mark only
  exists on an ok sentence, and ok already requires the verbatim
  check, so every marked quote has a verified span.
- Term, figure - deterministic. Emit the offset `term_glosses` and
  `name_bridge` already compute. The mark itself is unchanged.
- Story - three options:
  (a) **End of the telling (recommended).** The mark sits at the end
  of the last sentence of the story's contiguous run, as today. A
  story is told across a clause or several sentences; the end of the
  run is where its telling ends. No prompt change, no guessing at a
  span. Matches R31-A's own "a claim's mark ends the sentence".
  (b) Model-placed tag: change `citation_contract` so a story tag
  follows its own clause, keep tag positions in `parse_tagged`, change
  `wiring._replay_text` to match. A fleet voice-contract change is a
  methodology change - escalates to Mark - and needs a live battery to
  show the model places tags reliably.
  (c) Lexical overlap with the story's `tellable_as`. Rejected: fuzzy,
  and a wrong placement is a fidelity defect, not a cosmetic one.

**3. Frontend rendering.**
- `renderFromTransparencyPlan` builds sentence segments from
  `transparency.sentences`, then splits each sentence at every
  element's `char_end` and inserts that element's mark there. Two
  elements in one sentence render as two marks in two places; "✲✲"
  survives only where two elements genuinely end at the same character.
- Quote marks get their own kind (from the engine's `kind`), no longer
  grouped with stories. The duplicated `STORY_RECORD_TYPES` sets in the
  frontend and m7 stop deciding placement; the engine's `kind` does.
- The end references render `end_references` plus any R17 demotions,
  after the last paragraph.
- R17's rule is unchanged (glosses, then figures, then stories, newest
  first; a dropped mark is listed at the end, never removed from text).
- Stage 6b confidence display is unchanged: `confidencePhrase()` on
  every card, inline or end; R9's hollow `--contested` glyph and R10's
  `--repeat` class still apply to inline ✲ marks.

**4. Streaming (7b/7c): why marks survive a streamed reply.**
Every inline mark's position is local to its own sentence. Each
cleared-sentence event (Entry 53 Shape B) therefore carries its own
sentence text plus its own `elements`; no mark depends on text not yet
sent.
- Quote and term marks attach with their sentence, exactly as R31 rules.
- A story mark at "end of telling" is known only when the next sentence
  clears without that story, or the turn ends. Two ways:
  (i) **Recommended:** add the story mark to sentence k when sentence
  k+1 clears (or at turn end) - add-only, never removed, one sentence
  late.
  (ii) Show it on the run's first sentence as it clears - reverses
  R10's story-at-end placement; would need its own ruling.
- End references accumulate during the stream and render at turn end
  with the finished plan.
- An R17 demotion at turn end moves an inline mark to the end
  references - R31's own rule, unchanged.
- One builder, two callers: the per-sentence (stream) and whole-turn
  paths call the same `elements` builder; a parity test pins identical
  output for identical text.
- Replay: `engine/m4/projection.py` already keeps `transparency`, so a
  replayed turn carries `elements` and `sentences` even though it drops
  `grounding`.

**5. Hover card and participant-facing words - Mark's, not this
thread's.** The card keeps today's shape: label (a quote's is "work,
locus — speaker"), sources, the confidence phrase, and Level 3
"Original wording" where `original_wording` exists. Three placeholders,
each named in code and each failing a test if it ships unfilled:
- `R31_QUOTE_CARD_PHRASE` - the title of a quote mark's card, now
  separate from the story card's "Where this story comes from".
- `R31_END_REFERENCES_HEADING` - the heading of the end-of-reply
  block. It reads "General references ({n})" today; Mark may keep it.
- `Arrival.tsx` l.65 - "Look for the ✲ mark after a claim - tap it to
  see exactly where it comes from." Once quote and story marks sit
  inside sentences, "after a claim" stops being accurate. Mark rewrites
  it; `Arrival.test.tsx` pins his wording.

**6. Open questions, and who decides each.**
1. **Is a `doctrinal_witness` record a general reference under R31-B?
   (Mark - it sets the reach of his own ruling.)** Recommendation: yes,
   to the end. It grounds a claim, not a quote, story or term; any
   verbatim words it leans on are their own `quote` elements. This
   retires R10(c)'s witness-at-run-start placement, and PR 2 says so
   explicitly rather than letting it lapse quietly.
2. **Figures (name-bridge) are not named in R31-B. (Mark.)**
   Recommendation: stay inline at the name, as today - a word mark, the
   same kind of thing as a lexicon term.
3. **Story placement - option (a) in §2, option (i) in §4.
   (Reviewer.)**
4. **Can the R17 cap drop a quote mark, or is it exempt like witness
   marks are today? (Reviewer.)** Recommendation: exempt - a quote
   mark is the one mark that says "these exact words are a source's,
   not the Representative's."
5. **Do end references stay collapsed, or show open? (Mark -
   participant-facing.)** No recommendation; today's collapsed block is
   the default until he rules.
Q1 and Q2 change which records land in `elements` versus
`end_references`, so PR 2 does not start until Mark has ruled on both.
Q5 needs no code decision: PR 2 keeps today's collapsed block until he
rules, and says so in its own body.

**7. Test plan (PR 2).**
Engine (`engine/m4/tests/`):
- offsets: for every element, `sentence_text[char_start:char_end] ==
  surface`; for every sentence, `text[text_start:text_end]` equals its
  stripped text;
- a quote element sits exactly on the verified span - straight and
  curly quotation marks, and a quote the splitter re-merged across a
  sentence boundary;
- a Theon-shaped fixture: a quote and a term in one sentence give two
  elements with different `char_end`;
- a story run gives one element at the run's end; a non-consecutive
  re-cite gives `repeat: true`;
- completeness: ids(elements) ∪ ids(end_references) = ids(citations),
  none in both;
- general-reference record types (per Q1) appear only in
  `end_references`;
- `sentence_index` indexes `grounding.sentences`, withheld sentences
  included;
- stream/turn parity: the per-sentence builder over a sentence sequence
  equals the whole-turn builder;
- the existing `test_transparency_plan.py` cases port to `elements`;
  anchor-run cases go with the anchors;
- m7's `test_level1_element_density_groups_marks_the_same_way_the_
  renderer_does` moves to `kind`.
Frontend (`VoiceTurnBody.test.tsx`, `Arrival.test.tsx`):
- two marks render at two positions inside one sentence, in DOM order;
- a quote mark directly follows the closing quotation mark;
- a term underline sits at the word with no trailing ✲;
- end references render after the last paragraph and list exactly
  `end_references` plus demotions;
- R17: a dropped inline mark appears at the end and its text stays;
- Stage 6b confidence phrase on inline and end cards; R9 hollow glyph;
  R10 repeat class;
- no plan → legacy fallback, unchanged;
- placeholder guard: fails while any `R31_*` placeholder is unfilled.
There is no streaming consumer yet to test against; the stream/turn
parity test is the pre-7b guarantee, and 7c's own tests extend it.
Gates: `pytest engine -q`, frontend `vitest`, `tools/check_paths.py
--baseline tools/check_paths_baseline.txt` clean, CI green.

**8. Files PR 2 is expected to touch.** Engine: `engine/m4/
grounding_net.py`, `transparency_plan.py`, `term_glosses.py`,
`name_bridge.py`, `turn.py`, `engine/m7/instruments.py`, and their
tests. Frontend: `src/types/conversation.ts`, `VoiceTurnBody.tsx`,
`StoryMark.tsx` (the quote split), `GeneralReferences.tsx`,
`Arrival.tsx` (placeholder only), `app.css`, and their tests. No
`records/` change under story option (a).

**Entry 70 — 2026-09-24.** R41 measurement (thread D, item 1). This entry builds to R41 and
R41-A (Rulings-Pending.md, both ruled 2026-09-23). The question: when a participant's
question carries a modern word with no equivalent in the world, does the voice define the
word, falsely map it onto its world's nearest concept, or date it from outside its record?
R41-A retires the Facilitator bridge turn once these come back near zero. **They do not come
back near zero.** Whether to act on that is Mark's call. This entry only counts and quotes.

**Scope, verified on main at 7d34e2c.** R41 is not built, and the bridge route is unchanged.
The fleet `modern_term` registry holds one record, `_fleet.modern.trinity` (origin_year 325).
Among the real worlds, only pahc (70-200) counts it as anachronistic. So for 10 of 11 real
worlds, every modern word already reaches the voice today, under `pronoun_rule`. Most of
this battery therefore measures behaviour participants can already reach.

For pahc's "Trinity" alone, the harness replaced `wiring.compute_anachronistic_term_ids` with
an empty set for that one call. This was harness-side only; production code is unchanged.

**Battery.** Harness: `engine/m4/reports/r41_modern_word_battery.py`. Report:
`engine/m4/reports/r41-modern-word-battery-2026-09-24.json`.
- 11 real worlds, 2 test probes each (22 in total).
- 11 in-window controls, each using that world's own term record `world_word`.
- Every one of the 33 turns reached the voice. None reached the Facilitator.
- Routing, test probes: 14 "ordinary turn", 7 "later_age, first ask", 1 "other_tradition,
  first ask" (rzg, "Pentecostal").
- Grader: Haiku 4.5 with forced tool use, 2 runs per reply. A yes needs both runs to agree
  and a verbatim quote for that same item.
- Real cost: **$2.4347, 166 calls**. The pre-run estimate was $1.60 against a $3.00 cap.
  Voice turns averaged about $0.07, not the engine/m8 mean of $0.04 the estimate used.

**Results, out of 22 test replies.** Two readers:
- the grader, settled yes (plus unsettled);
- this thread's own read of all 22 replies in full (clear, plus borderline).

| Risk | Grader | Thread read |
|---|---|---|
| Defines the modern word | 11 (+2) | 13 (+3) |
| Dates it from outside the record | 12 (+1) | 13 (+2) |
| False mapping | 0 (+2) | 0 (+2) |
| Etic seam in the voice's own turn | 3 | 6 |
| Names the word as the participant's own | 21 | 9 (+4 partial) |

- Only 4 of 22 replies are clean on all four risks by the thread's read: cappadocian-T2,
  don-T1, don-T2, gallic-T1.
- In the thread's read, 18 of 22 carry at least one clear definition or dating claim.
- Controls: 0 of 11 treated the world's own word as foreign.
- The grader reads "names as participant's word" far more generously than the text
  supports. Its 21 counts replies that never say whose word it is (e.g. don-T1, gallic-T1,
  rzg-T1). Treat the grader's figure for that item as unreliable. The counts for the four
  risks agree closely between the two readers.
- The thread's read is not independent confirmation. It needs the reviewer's own read
  before any number here is relied on.

**Shape of the failures.** Quotes are verbatim from the report.
- *Dating, the commonest form:* "it names a division that came over a thousand years
  after our own time closed. We lived c. 320-430; the break that word marks happened in
  the 1500s" (desert-T1).
  - The same form appears in cappadocian-T1, gallic-T2, ijc-T2, syr-T1 and witt-T2 ("centuries
    after our own span closed in 1580").
  - ijc-T1 dates it wrongly as well: infallibility "comes from your own century". The
    definition was 1870.
- *Definition:* "papal infallibility, the teaching that the Roman bishop speaks for the whole
  church without error when he defines doctrine" (alx-T1). "Liberation in the sense the
  modern phrase carries - a program of analysis aimed at systemic oppression, centered on the
  poor as a class" (hal-T2).
- *Borderline false mapping:* "Our faith meant freedom ... That is the liberation we
  proclaimed" (alx-T2). hal-T2 has the same pattern. Both then separate the two senses
  explicitly.
- *Seam, knowledge of the world's own later reception:* "the councils we helped write became
  law and liturgy for the traditions that trace themselves through us - Orthodox and Catholic
  both, and Protestant dogmatics more distantly" (cappadocian-T1).
- *Seam, later naming:* "what your people would later call the Old Testament" (pahc-T2).
- *Correct form (pahc-T1, Trinity, bypassed):* "We never used that word. It does not belong
  to us - what we can give you is our own." It still dates the word at its close: "belong to
  a world that came after ours closed".

**Root cause, as far as this run shows.** Dating claims appear on both routing paths: 5 of 8
turns with a directive and 8 of 14 ordinary turns. So they do not come from the later_age
directive alone. They come from generation. The voice supplies outside knowledge of when a
word arose, and the only instruction that covers this case (`pronoun_rule`'s own clause) does
not forbid it. This run does not test whether a prompt-side fix, a guard, or keeping the
bridge is the right answer. That is a governance/methodology question for Mark.

**What this means for the bridge (not decided here).** The bridge covers one word ("Trinity")
in one world. By this measurement, the risks R41 lists already occur, unbridged, for every
other modern word in every real world. So keeping the bridge "until near zero" does not keep
these risks away from participants today. It keeps them away only for "Trinity" in pahc.
Escalated to Mark. It is not resolved by this thread.

**R41-A item (c).** The hover card does not show the modern sense of a registered term.
`modern_sense` is read only by `facilitator_turns.bridge_turn` (l.426-443). No frontend code
reads it, and `term_glosses` covers world term records, not fleet `modern_term` records. This
is missing, and it is stated here as R41-A asks. Nothing is built for it.

**Fleet-record question, flagged and not touched.** `_fleet.modern.trinity` gives
origin_year 325. Its `underlying_subject` says "before the word 'Trinity' existed". Theophilus
of Antioch's *trias* (Ad Autolycum II.15, c. 180) would fall inside pahc's own window. That
reference is not re-verified here against a vendored source. It is a lead for the records
owner, and the claim's confidence may be Contested.

**Defects seen in passing, outside R41. Recorded, not fixed.**
- rzg-T2 breaks strict we-voice: "ask plainly, and I'll tell you what we have".
- don-T2 ends on a paragraph unrelated to the question: "Genesis as a question about how the
  world was made - no".
- rzg-C puts the project's own confidence vocabulary into the voice: "The doctrine is
  Documented".

**Entry 71 — 2026-09-24.** R37's design brief, carried forward onto
`main` from PR #438, which is closed as superseded (Mark's own call,
2026-09-24: "Fresh branch off main, close #438 as superseded"). #438 was
one commit on an old `main` and conflicted on both Ministry files. The
brief's script and its 2026-09-23 report come forward unchanged in
substance: `engine/m4/reports/r37_ruling_design_measure.py` +
`r37-ruling-design-measure-2026-09-23.json`. Re-run on today's `main`,
the script reproduces the committed report exactly, apart from its
timestamp. The ruling itself - R37, R37-A, and R37-B - now lives in
full in Rulings-Pending.md's R37 entry, not on a PR branch. The brief's
original text stays readable on closed PR #438. Below is each of its
four items, with R37-B folded in and what the build (Entry 72) did with
it.

**Item 1 - the world-level "known in its own time" list.** The brief
proposed a `known_traditions_in_window` list of rows in
`records/worlds/<world>.yaml`. R37-A has since fixed the test as pure
chronology: the named tradition's `time_window` start is at or before
the speaking world's `time_window` end. Both halves already exist in
the registry, so a stored row would only copy them and could drift.
**Not built as rows:** condition (a) is computed from the registry
every turn. The brief's other half - "this world's own records name the
tradition" - was already built by #440/R39 as
`world_records_mention_tradition`, using the same prose-field allowlist
this brief first proved necessary.

**Item 2 - what was revealed in this conversation.** Unchanged in
shape: a separate, labelled block in the private directive, never
folded into `history` (`history_from_transcript` deliberately excludes
the Facilitator). It holds exact sentences, never a paraphrase.
**R37-B widens its sources from two to three:** the Facilitator's
introduction, the participant, and another Representative. The
speaking voice's own earlier turns never count, and neither does the
current question itself - the question's own words are what every
other_tradition turn already has.

**Item 3 - interaction with the existing classes and wording.**
Unchanged: `neighbour_named` is a citation check, not a licence check,
and `own_doctrine_in_other_tradition_turn` is R38's axis. The brief's
three wording candidates for the R26 sentence are all moot:
- (iii), the world's own records name the tradition, was built by #440
  without new words (the evidence branch).
- (ii), known in its own time but no textual evidence, needs no new
  sentence. Under condition (a), the record still does not mention the
  tradition, so `R26_HONEST_LIMIT_SENTENCE` stays true and is said
  exactly as before.

No participant-facing words are added anywhere; the R37 text is all in
the private directive.

**Item 4 - the battery count.** 9 of 11 under the symmetric reading and
11 of 11 under the asymmetric reading. R37-A chose the asymmetric one.
The build's own battery (Entry 72) confirms 11 of 11 against the
engine's real code path.

**Entry 72 — 2026-09-24.** R37 build: the pivot's own licence, for
interview and the Table. Rulings: R37, R37-A, R37-B (Rulings-Pending.md
R37). Brief: Entry 71.

**What the voice now gets.** On every `other_tradition` turn,
`engine.m4.turn._other_tradition_directive` adds one pivot-scope clause
to each branch that has no record evidence (first ask, repeat turn,
seated tradition):
- **(a) holds:** the voice may let its knowledge that the tradition
  existed guide which part of its own record it answers from. It never
  lets it say anything about that tradition beyond its own records and
  what the conversation has told it.
- **(a) fails, and the tradition is a registry world:** that tradition
  arose after this world's time. The voice chooses its pivot from the
  question's own words, plus any quoted lines, and never from outside
  knowledge.
- **The question names no registry world** (e.g. "the Arians"): the
  voice is told only that nothing establishes that its world knew the
  tradition. It is never told that the tradition came later, since that
  cannot be known here. The pivot comes from the question's own words.

When the conversation has said anything about the named tradition,
those exact sentences follow, attributed to who said them, closed by
"Use nothing beyond these words." The evidence branch (the world's own
records name the tradition) takes the quoted lines but no pivot clause:
there the record itself grounds the pivot. The seated branch's "what
that chair has said" now also covers what anyone else at the table has
said about it (R37-B). `R26_HONEST_LIMIT_SENTENCE` is unchanged, and so
is when it is said.

**Detection:** `engine.m4.uncited_claims.tradition_known_in_window`
(condition (a)) and `conversation_revealed_excerpts` (condition (b)).
The excerpt function splits sentences with
`engine.prose.quote_aware_sentences`, the same splitter the live net
uses. It keeps at most 8 excerpts, the most recent ones: dropping older
lines only narrows what the voice may lean on. Of the Facilitator's
turns, only the introduction counts (kind `door`: the interview's DOOR
and the Table's TABLE_DOOR). Mark's words name "the facilitators
introduction", so threshold, bridge, safety, correction and close turns
are not revelations under this ruling.

**Wiring:**
- **Interview (`engine/api/wiring.py`):** reads the same replayed
  transcript as the voice's own history. That state is projected before
  the current message is appended, so the question is never quoted
  back.
- **Table (`engine/api/table_wiring.py`, built on #449's version):**
  per seat. Condition (a) uses this seat's own window. Condition (b)
  reads the round's replayed transcript with the round's opening
  question dropped, so every other seat's turn before this one counts.

**A pre-existing defect found and fixed.** The build battery's own
later-tradition probe caught it. `world_records_mention_tradition`
counted a Representative's personal name as a name of the tradition.
desert's `desert.story.sarapion-anthropomorphite` names Theophilus, the
4th-century bishop of Alexandria. rzg's 16th-century Representative is
also named Theophilus. So on `main` today, desert asked about the
Reformed Cities gets "your own records already speak to it" - on a
tradition that arose eleven centuries after desert's window closed -
and that branch never sees the R37 clause.

Root cause: a Representative's name is a person's name, and another
world's records can name a different, real person who shares it. The
fix: the evidence scan uses the tradition's own names only (card name,
display name, world id, demonyms), via `_names_for_world(...,
include_representative=False)`. Every other caller keeps the
Representative's name, because a participant or another seat saying it
does mean that seat. The 4 genuine record matches on the real battery
(desert, hal, ijc and pahc on Alexandria) are unchanged. witt's genuine
"Reformed cities" match is unchanged too, and pinned by a regression
test.

**Battery** (`engine/m4/reports/r37_build_battery.py` +
`r37-build-battery-2026-09-24.json`). Deterministic, no model calls,
$0. It runs the engine's own functions on real packages:
- **B-other-tradition (the 11 real probes):** 11/11 licensed under (a),
  matching R37-A. 4 take the records branch, 7 take condition (a).
- **C-later-tradition** (synthetic: each world asked about the other
  world with the latest window start): 11/11 match R37-A's test,
  computed independently. 9 take "question's own words only", 1 takes
  condition (a) (rzg on witt), and 1 takes the records branch (witt on
  the Reformed Cities, genuine).

**Live battery, run on Mark's own ask (2026-09-24).**
`engine/m4/reports/r37_live_battery.py` +
`r37-live-battery-2026-09-24.json`. Real Bedrock calls through the
production wiring at production defaults (self-revision on, R27
enforcement off): $0.3136, 23 calls, four probes, every answer
hand-read.
- **L1, alx on the Donatists (condition (a)).** The R26 sentence is said,
  then the pivot goes to alx's own lapsed controversy, cited to
  `alx.dw.church-failure`. That pivot is exactly what R37 licenses. But
  two uncited sentences follow that no alx record holds: "whether a
  bishop who had once given way could still validly baptize, or ordain"
  and "We held that the power was Christ's, not the minister's, and a
  fallen bishop restored through repentance could minister again". This
  is R26's own original motivating defect: Augustine's anti-Donatist
  doctrine, stated as Alexandria's own, on the same Theon question. The
  R37 clause ("It never lets you say anything about that tradition
  itself beyond what your own records hold") did not prevent it.
  R27's detector flagged both sentences, but only as the base
  `uncited_claim` class, never as `own_doctrine_in_other_tradition_turn`.
  They share a paragraph with a cited sentence, and the paragraph-
  inheritance check passed them on that tag, so no paragraph offense was
  recorded. R38's self-revision reads tagged sentences only. With
  enforcement off, both sentences reached the participant. This is a
  failure of the R27/R38 net, not of R37's wiring. One sample does not
  give a rate.
- **L2, alx on the Reformed Cities (tradition arose later).** Correct.
  The R26 sentence, then an answer wholly from alx's own transmission
  records, all cited, and "we lived before those reformations, and our
  record holds nothing of them". That is inferred from the question's
  own word "Reformed", as the clause asks. No outside names. The screen's
  one marker hit ("Reformation") is that same inference, a false
  positive on hand read.
- **L3, condition (b) in interview.** Not reached, and the reason is
  structural. Turn 1 named the Donatists, so the reader routed it
  `other_tradition` itself, and turn 2's second ask went to the
  Facilitator's etic turn as designed. A participant's earlier mention
  can only become a (b) revelation in interview when that earlier
  message was not itself routed `other_tradition`. The Table is where
  (b) really runs.
- **T1, R37-B at the Table (ijc first, alx second).** Correct. ijc
  answered from its own Donatist records. alx received 5 of ijc's
  sentences as quoted lines, said the R26 sentence, said "Africa's
  church quarrels lie outside what our sources name", engaged what ijc
  had said, and answered from its own cited records (the John-and-the-
  robber story, the Arsinoite conference). It added no Donatist facts.

**Known limits, stated plainly:**
- Condition (b) captures only sentences that name the tradition. A
  following sentence that refers back by pronoun ("They refused
  traitor bishops") is not quoted. This narrows the licence rather than
  widening it.
- `match_named_tradition` still matches a Representative's personal
  name in the participant's own message. A desert participant asking
  "What did Theophilus teach?" would resolve to rzg if the reader also
  classified the turn `other_tradition`. That needs a reader
  misclassification first, and it is not changed here.

**Entry 73 — 2026-09-24.** R42 follow-up (build thread C, item 2 of
the reviewer thread's brief): found, not built; held by sequencing
verdict (a).

**What the record says remains.** R42 (`Rulings-Pending.md`, RULED
2026-09-23) leaves exactly one follow-up open: a generation-side
citation-completeness item, not a check. Propose one report-only
directive line asking the voice to tag any sentence that draws on a
record even when it names no person, number or quote; measure it on
the same 22-probe run by the same hand-read method as Entry 61 (count
of true-but-untagged sentences before and after, against Entry 61's
14 of 40); report the two counts and the cost. No enforcement follows
either way. Any battery number quoted is post-G6 and not directly
comparable to Entry 56's pre-G6 numbers.

**Why it is not built.** R42 queues it "after 7b, not before." 7b is
the engine streaming module behind `CIC_API_STREAMING` (Entry 53, and
the recorded 7b-7e order). On main when this was checked (2026-09-24),
no code read `CIC_API_STREAMING` and no 7b PR had merged -
`engine/m4/generation.py`'s model-side stream call predates Stage 7 and
is not 7b.

**Verdict (reviewer thread, sequencing, 2026-09-24): (a) hold until 7b
merges, as R42 states; the recorded order is not waived.** The
follow-up starts after 7b merges, as its own item; this entry is the
only change it makes now.

**Entry 74 — 2026-09-24.** R31 grounding marks: the build (PR 2 of 2),
to Entry 69's brief as passed, with the rulings that closed its open
questions.

**Rulings this build rests on.** Mark's choice of Entry 69's own
options (R31-C): Q1 - a `doctrinal_witness` record is a general
reference, at the end of the reply, and R10(c)'s witness-at-run-start
placement is retired for every turn built on per-element placement; Q2 -
figure names stay inline at the name, like a lexicon term. The reviewer thread, on Entry 69's own §6: Q3 - a story's
mark sits at the end of its telling, and under streaming is added to
sentence k when sentence k+1 clears without it, or at turn end, add-only;
Q4 - a quote mark is exempt from the R17 cap. Q5 (end list open or
collapsed) is still Mark's; the collapsed list stays until he rules.
All recorded in Rulings-Pending.md as R31-C.

**Engine.**
- `engine/m4/transparency_plan.py` replaces sentence-run `anchors` with
  `sentences` (each net sentence's span in the reply text), `elements`
  (one per grounded element: quote, story, term, figure, each with its
  sentence index and in-sentence offsets) and `end_references` (every
  cited record with no inline element). `references` is unchanged, and
  so is its completeness invariant.
- `ElementBuilder` builds the quote and story elements one sentence at a
  time, add-only; the whole-turn path feeds the same builder, which is
  what 7b's per-sentence path will call.
- A story run is now broken by any sentence that does not cite the
  story (withheld, untagged, or citing something else). The anchor-era
  runs skipped over uncited sentences; the reviewer's Q3 streaming rule
  ("added when k+1 clears") needs the run to end at the first sentence
  without the story, so both paths now agree on that.
- A quote element sits on the first quotation in its sentence whose
  words `grounding_net` verifies verbatim in that quote record
  (`quoted_span_positions`, new, shared with `_quoted_spans`). A quote
  record cited on a sentence that quotes none of its words has no
  quoted words to follow; its mark ends the sentence.
- `term_glosses.find_glosses_used` and `name_bridge.find_figures_used`
  now return each word's `text_start` - the offset both already
  computed and then dropped. The plan places word elements from it; the
  frontend no longer searches for them.
- An element on a sentence the plan cannot find in the reply text falls
  back to `end_references` (disclosed, not dropped).
- `engine/m7/instruments.py`'s `level1_element_density` counts from
  `elements`; a stored plan with no `elements` is still counted from its
  anchors.

**Frontend.**
- `VoiceTurnBody.tsx`: `renderFromElements` replaces the anchor
  renderer. It places each mark by offset: a quote's ✲ after its
  closing quotation mark, a story's ✲ after its last sentence, a term
  or figure mark on the word. One mark per element, never merged.
  Everything with no inline element, plus anything the R17 cap drops,
  is listed at the end.
- R17's cap now counts the engine's own sentences, not a second regex
  split. Drop order is unchanged (glosses, figures, stories); quote
  marks never drop.
- A turn whose plan has no `elements` (a stored transcript) still
  renders through the legacy renderer.
- R9's hollow glyph, R10's repeat class and Stage 6b's confidence phrase
  are unchanged, on every inline mark.

**Change order against Entry 69 §5, named rather than made quietly.**
The brief said each placeholder would fail a test while unfilled. That
would hold CI red until Mark writes three pieces of wording, blocking
the build on a decision that isn't a build decision. Instead:
`cic-poc/frontend/src/lib/markCopy.ts` holds `QUOTE_CARD_PHRASE` and
`END_REFERENCES_HEADING` (Entry 69 §5's `R31_QUOTE_CARD_PHRASE` and
`R31_END_REFERENCES_HEADING`, renamed so no identifier in live code
carries a ruling number) at the exact wording the app already showed
in those places before this change, and `pendingMarkWording` names both
plus the `Arrival.tsx` disclosure line. A test pins each pending value
to its pre-R31 wording, so no thread-written copy can reach a
participant. When Mark's words arrive, each value changes and its name
leaves the list. Until then, a quote card is still titled "Where this
story comes from", and the Arrival line still says the ✲ comes "after a
claim". Both are inaccurate now that marks sit inside sentences, and
both are his to replace.

**Tests.** Engine: `engine/m4/tests/test_transparency_plan.py` is
rewritten to the element contract (18 tests - exact offsets, the Theon
shape of a quote and a term on one sentence, story runs and repeats,
the completeness invariant, witness/gravity/unsaid term at the end,
stream-versus-whole-turn parity with an add-only check), plus one m7
test for element counting. Frontend: `VoiceTurnBody.test.tsx` is
rewritten to the element renderer (16 tests - positions read back as
text, R9, R10, Stage 6b, R17 with quote exemption, legacy fallback, the
pending-wording guard).

**Provenance, kept here rather than in code.** The live files this build
touches (`engine/`, `cic-poc/frontend/`) say only what the code does; the
managing thread's round-1 verdict on #490 failed an earlier head for
carrying ruling numbers, entry numbers and attributions in comments,
docstrings and test names, per CLAUDE.md's "Keep the live/canonical
surfaces clean". Where each piece of behaviour comes from:
- one mark per distinct grounded element, placed at that element - R31-A;
- quote, story and lexicon marks inline, every other cited record at the
  end of the reply - R31-B;
- a witness record listed at the end, and R10(c)'s witness-at-run-start
  placement retired for turns built on per-element placement - R31-C Q1;
- figure names inline at the name - R31-C Q2;
- a story's mark at the end of its telling, added when the next sentence
  clears (`ElementBuilder`) - Q3, the reviewer thread's decision on
  Entry 69 §6;
- a quote mark never dropped by the cap - Q4, likewise;
- marks attach as each sentence clears, and a cap demotion moves a mark
  to the end list without removing a sentence or claim - R31, with Entry
  53's Shape B as the streaming design these marks are built for;
- the repeat and hollow glyphs kept on inline marks - R10 and R9; the
  confidence phrase on every card - Stage 6b; the cap itself - R17;
- the quote-and-term-on-one-sentence test fixture - the Theon staging
  defect (Entry 58).

**A defect the round-2 tests exposed, fixed in the same push.** The
managing thread's content verdict on #490 asked for Entry 69 §7's two
missing placement tests: a quote in curly quotation marks, and a
quotation the splitter re-merged across a stop.
- The re-merge case already placed correctly; its test pins it.
- The curly case did not. `engine/prose.py`'s `QUOTE_OPEN`/`QUOTE_CLOSE`
  knew only straight marks, so a “…” or ‘…’ quotation was never seen as
  a quotation. The quote's mark fell back to the end of its sentence.
- The same root cause went further than placement, and predates this
  PR. The grounding net's verbatim-quote rule never ran on curly-quoted
  words. A coined quotation in curly marks, tagged to a real quote
  record, streamed as `ok` whenever it shared a content word with that
  record. The identical sentence in straight marks is withheld ("quoted
  span not found verbatim"). Reproduced on alx before the fix.
- Fixed at the root: both patterns now also accept “ ” ‘ ’. The splitter,
  the net, and placement all read those shared patterns, so all three
  now treat curly marks as quotation marks. The one comment line naming
  which marks the patterns cover is updated to match; no other existing
  line changed.
- Effect on live turns: a curly-quoted span now gets the same verbatim
  check as a straight-quoted one. A coined curly quotation loses its
  citation (its text stays, as for every withheld sentence).
- Tests: curly marks hold a sentence together, and a curly apostrophe
  inside a word opens nothing (`engine/tests/test_prose.py`); a verbatim
  curly quote passes and a coined one is withheld
  (`test_grounding_net.py`); curly placement and re-merged placement
  (`test_transparency_plan.py`). Without the fix, the four curly tests
  fail; with it, all pass.

**Entry 75 — 2026-09-24, corrected in place same day (round 2, after a
managing-thread re-verification of round 1's own quoting).** `_fleet.
modern.trinity` (Entry 70's own R41 report flagged this record's
`origin_year` as open to question) carried a fabricated claim:
`underlying_subject` said this world's people spoke of Father, Son, and
Spirit "before the word 'Trinity' existed for them to use." Two vendored
passages, verified verbatim, say otherwise - Theophilus of Antioch, *To
Autolycus* II.15 (`cic/texts/anf02_hermas-tatian-athenagoras-theophilus-
clement-alexandria.xml`, near line 8993): main text "are types of the
Trinity, ... of God, and His Word, and His wisdom," with Τριάδος itself
appearing only as the attached footnote's own Greek gloss on "Trinity"
(not a bracketed word inside that sentence, as round 1's own entry here
wrongly rendered it) - that footnote calls the usage "the earliest use
of this word 'Trinity'" and, in the same breath, "an accepted word, not
introducing a new one." Internal evidence in the same work (Book III.28's
chronology, reckoned to the death of the Emperor Verus, A.D. 169) and the
edition's own introductory notice - "succeeded to the bishopric... in
a.d. 168," "died either in a.d. 181, or in a.d. 188" (two traditions,
both stated; the same notice's own bracketed heading uses 181 as its
single figure) - together support c. 169-181 as the edition's own
preferred window, with 188 an explicit, sourced alternative, not an
invented one. Tertullian, *Against Praxeas* 2 (`cic/texts/anf03_
tertullian.xml`, near line 51144): "which distributes the Unity into a
Trinity," with the edition's own footnote: "Probable date not earlier
than a.d. 208" - a floor, with no upper bound stated; round 1's own entry
here additionally claimed this as "the earliest surviving Latin
'Trinitas'," which the vendored (English-translation) edition does not
support and which round 2 removed everywhere it appeared.

**Mark's ruling: option B of three**, put to him directly. A -
`origin_year` moves to c. 180 (the word's own earliest date) and pahc's
modern-term bridge ends, since the word would then predate this world's
window; C - split the record in two (a `word` record for the term's own
history, a separate record for the doctrine). **B - `origin_year` keeps
its meaning as when the *modern sense* `modern_sense` names took shape
(325, Nicaea and after), not when the word was first attested; 325
stays, and pahc keeps its modern-word bridge.**

Fixed the false claim rather than patching around it: `underlying_subject`
no longer states or implies the word did not exist; `distinguishing_claim`
now states both dates plainly (word: c. 169-181, with 188 disclosed as
the edition's own alternative; a.d. 208 or later; doctrine: 325 and
after) and names the referent question as open rather than settled
either way. Two new fleet source records carry the vendored passages
(`_fleet.source.theophilus-to-autolycus`,
`_fleet.source.tertullian-against-praxeas`), cited from
`_fleet.modern.trinity.sources[]`. Whether Theophilus's own triad (God,
His Word, His Wisdom) is the same referent as the doctrine Nicaea later
formalizes is a real, unresolved scholarly question that a bare date
correction would have flattened into a false "yes" by omission; it is
now its own record, `_fleet.contested.theophilus-triad-referent`
(`formation_confidence: Contested`), holding the case each way rather
than asserting continuity. `reference/Redesign-Spec/Artifact-1-Record-
Schema.md` §4 gained one paragraph defining what a `modern_term`
record's `origin_year` means (the modern-sense date, not first
attestation) as plain rule text, so the next record of this type is
built against a definition instead of tribal knowledge.

**Round 3 (same day, this PR's last round under the three-round cap):**
round 2's own `distinguishing_claim` still read like a source record,
not participant-facing prose - field names (`modern_sense`), a record
id (`_fleet.contested.theophilus-triad-referent`), a spec citation
("spec §5 bridge"), and one sentence of pure engine mechanism ("the
Facilitator strips the modern label and passes the underlying subject
to the voice term-free") all leaked into a field the Facilitator bridge
turn (`engine/m4/facilitator_turns.py`) speaks to a participant. Rewrote
it as plain prose carrying the same substance (earliest surviving use
c. 169-181, with 188 disclosed; already a familiar word; the triad of
God, His Word, His Wisdom; Tertullian's use from 208 or later; the
developed doctrine's own later formation at Nicaea, 325; the referent
question left open) with no field names, ids, or mechanism language.
Measured against `engine.m1.fk.fk_grade` (this project's own hermetic
FK implementation): grade 8.77, seven sentences, longest 23 words,
average 14.4 words/sentence - inside the CLAUDE.md target band (FK 8-10,
sentences 12-20 words average, nothing over 25).

Mark approved the participant wording with three edits to
`distinguishing_claim` (`underlying_subject` approved as it stood):
"older than you might assume" -> "older than the doctrine it now
names"; "To him, it already sounded familiar, not new" -> "He seems to
use it as a word his readers already knew"; and the closing sentence
reworded to "Scholars still disagree about whether Theophilus meant
the same thing that doctrine later named." Re-measured after the
edits: FK grade 7.68, longest sentence 23 words, average 15.1
words/sentence.

**modern_sense wording ruling, 2026-09-25 (item D1/#548, a separate field
from the round above's own `distinguishing_claim`).** An independent
review of #548 found `modern_sense` mislabeled and ungated in
`spoken_fields.py`; gating it once fixed found `modern_sense` itself at
FK grade 11.7, above the ceiling of 10. An Opus-drafted rewrite proposed
"teaching" in place of "doctrine" (same FK grade either way, 7.17); Mark's
own ruling, in session, 2026-09-25: "the new Trinity wording is fine,"
naming the approved text exactly: "The developed doctrine that God is
three persons in one being, all three equal and all three without
beginning or end. This doctrine took formal shape at Nicaea and after." -
"doctrine" in both places, not "teaching", matching `distinguishing_claim`'s
own "the doctrine it now names." Applied verbatim to the record.

**Entry 76 — 2026-09-25. R42's own generation-side follow-up (Entry 73):
measured, then dropped by direct ruling.** Entry 73 left one open item -
a proposed report-only directive line asking the voice to tag any
sentence that draws on a record even when it names no person, number, or
quote - held "until 7b merges" by its own sequencing verdict. Mark's own
ruling, in session, 2026-09-25 ("a, add the narrow sentence and run the
test") chose to build and measure it now rather than continue holding it.
The proposed sentence, for the record: "A sentence that states something
specific this ground actually says, even when it names no person, place,
text or number of its own, still carries that record's own tag. Only a
sentence that adds nothing beyond connecting or interpreting what was
already said stays untagged."

**Live measurement, same script and method as Entry 61**
(`engine/m4/reports/g1_precision_sample_measure.py`, 11 worlds x 2
probes = 22 fresh probes, region us-east-1), with the proposed sentence
added to `records/_fleet/fleet_voice/_fleet.voice.fleet.md`'s
`citation_contract` and all 12 world packages rebuilt/re-pinned for the
measurement only. Real cost: $1.9714, 22 probes, 141 raw offenses
(report: `engine/m4/reports/g1-precision-sample-measure-2026-09-25.json`).

**Sample of 40, stratified across all 11 worlds proportional to each
world's own share (Entry 61's own method), hand-read against each
world's own freshly-compiled repository.** The three counts, before
(Entry 61) vs after: 0 -> 4 unsupported, 14 -> 17 supported but
untagged, 26 -> 19 interpretive or connective (of 40 each time). The
proposed sentence showed no measurable reduction in the untagged-but-
supported miss rate - if anything it moved the other way, consistent
with Entry 60's own finding that a proposed wording change "made no
measurable difference to the raw rate." One 40-sentence sample from one
run is not enough to call 14 vs 17 a real regression either; both
readings are offered plainly, not resolved past what this sample can
support.

**Unsupported (4 of 40, up from 0) - the important finding, independent
of the citation-contract question this measurement was run to answer:**
four sampled sentences asserted a specific, checkable claim with no
support anywhere in the speaking world's own compiled repository,
verified by direct search, not plausibility: *"Some among us thought he
was a coward"* (cappadocian, of Eustathius of Sebaste) - the repository
documents the Eustathius rupture at length but nowhere calls him a
coward or names factions who thought so; *"Felix Manz was drowned in the
Limmat that same year"* and *"...fines, then imprisonment, and finally,
in 1527, execution"* (rzg) - Felix Manz is named repeatedly in rzg's own
repository, but no drowning, no river name, no execution, fine, or
imprisonment appears anywhere in its compiled text; *"Alexandria itself
appears only once in what we hold, and only in passing..."* (witt) -
"Alexandria" appears zero times, any spelling or case, anywhere in
witt's compiled repository. These are not citation-contract misses -
they are the class of fabrication `engine.m4.named_claim_grounding`
(OG-16, `worlds/pahc/Open_Gaps_Tracking.md`) exists to catch,
report-only and unenforced today, on real live traffic, independent of
anything this entry's own citation-contract question asked.

**Control run, 2026-09-25 (asked before any decision on the finding
above, to isolate cause): same script/method, against current
origin/main - no citation_contract change of any kind, the build
participants actually get today.** Real cost: $1.9801, 22 probes, 150
raw offenses (report: `engine/m4/reports/g1-precision-sample-measure-
control-2026-09-25.json`). Same stratified 40-sentence hand-read method.

**One confirmed unsupported claim, verified by direct search:**
*"Athanasius of Alexandria was named among the bishops who signed it,
and our own teachers defended that same homoousios..."* (cappadocian) -
"Athanasius" appears zero times, any spelling or case, anywhere in
cappadocian's compiled repository. Fabrication therefore reproduces on
current main, independent of the citation_contract question this whole
measurement line was run to answer - it is not something the proposed
sentence caused. **Honest limit, stated plainly rather than glossed
over: this control run verified the Athanasius finding to the same
direct-search standard as the four above, but did not carry every one of
the other 39 sampled sentences to that identical depth** - a real limit
on what this control run alone establishes, separate from the finding
itself.

**Why `named_claim_flags` (OG-16; `engine.m4.named_claim_grounding`) did
not catch any of these fabrications, in either run: it cannot, by
construction.** That check only examines a sentence that is already
citation-tagged and already passed `grounding_net`'s own ratio test -
every fabrication either run found came from `find_uncited_claims`'s own
untagged-sentence list, a structurally different, out-of-scope class,
not a near-miss. The class of fabrication both runs found is exactly
`find_uncited_claims`/R27's own domain (enforceable today via
`r27_enforce`/`CIC_R27_ENFORCE`, off by default) - not named_claim_
grounding's.

**Are these worlds live today?** `engine.m1.registry.load_registry()`
and `cic-website/data/world-census.json`'s own `movements` list both
confirm: cappadocian, rzg (`the-reformed-cities-zurich-and-geneva`), and
witt are all `state: admitted`, `living: true`, and census status
`"Built & Live"` - yes, live on the production site today. No
enforcement flag was touched by either run.

**Ruling (Mark, 2026-09-25): "drop #558."** The proposed sentence is not
adopted: it showed no measurable improvement to the untagged-but-
supported miss rate it was meant to address, and the fabrication finding
above is confirmed pre-existing on main, not caused by or fixed by the
proposed sentence. `records/_fleet/fleet_voice/_fleet.voice.fleet.md`'s
`citation_contract` is unchanged on main; no world package is re-pinned
by this entry. The fabrication finding itself remains open, tracked
separately from this now-closed follow-up - R27/`find_uncited_claims`
is the existing, off-by-default mechanism that already covers this class
of defect, per the scope note above.

**Entry 77 — 2026-09-25.** R27 (`find_uncited_claims` enforcement,
`CIC_R27_ENFORCE`/`r27_enforce`, off by default) live measurement,
managing thread's own ask, following the fabrication finding on #558's
run and its control-run reproduction (branch
`r42-citation-contract-inference-sentence`, commit `2ffc8942`). **#558
itself was closed by Mark's own ruling, "drop #558"** - the proposed
`citation_contract` sentence it carried was not adopted, since it
showed no measurable improvement to the untagged-but-supported miss
rate. Its live-measurement and control-run findings (the fabrication
class this entry goes on to test) are preserved in main's own
Decision-Log as **Entry 76** via PR #568, not #558 itself - numbered
77 to follow that entry, the same "#395's own Entries 37-38 renumber
to 38-39" precedent already set in this file. PR #568 had not yet
merged as of this branch's own last merge from `main`; this entry sits
directly after the old Entry 75 until that lands, then follows #568's
own Entry 76 on the next merge from `main`. **Mark's ruling verbatim
(2026-09-25, Decision 3, option A): "A, yes to the $3 ceiling."** The
goal: measure whether `find_uncited_claims`'s existing, already-built,
report-only-by-default enforcement mode stops the class of voice
fabrication the two prior runs found, before switching it on by
default anywhere.

**Same method as Entry 61/#558/the control run** (11 admitted formation
worlds x 2 fresh probes = 22 live calls, `CONFLICT_TURN`/
`_other_tradition_turn`, current `origin/main`, worlds compiled fresh
from `records/` via `_compile_world` - the same discipline as every
prior run in this line, sidestepping this environment's own possibly-
stale `packages/`), but with `r27_enforce=True` turned on for this run
only (the real production enforcement path
`engine/m4/live_uncited_claims_battery.py`'s own `--enforce`/
`run_enforced` mode already exercises - `engine.m4.turn.run_gate` and
`_run_ordinary_voice_turn` called directly, real routing, real
regenerate-once-then-blank enforcement), interview half only (no table
session, to stay comparable to the 22-probe method the other entries in
this line used). No code and no default changed anywhere - `r27_enforce`
was passed as a script-local keyword argument, the same shape
`run_enforced` already uses; `CIC_R27_ENFORCE`'s own env-var default in
`engine/api/config.py` was not touched. Script (ad hoc, not committed -
this PR carries only the Decision-Log entry and the run's own JSON
artifact, per the managing thread's own "no code or default changes"
instruction) mirrored `run_enforced`'s interview loop but additionally
threaded `_run_ordinary_voice_turn`'s existing `debug_capture` parameter
through, so both the pre-enforcement draft and the post-enforcement
final text were kept per probe - a before/after hand-read was not
possible from `run_enforced`'s own persisted fields alone (`regenerated`/
`facilitator_takeover` booleans only), and this measurement's whole
point is what enforcement actually removed, not just whether it fired.
**Real cost: $1.6049, 22 probes, region us-east-1, well under the
$3.00 ceiling** (comparable order of magnitude to Entry 61's $1.6527,
#558's $1.9714, and the control run's $1.9801 for the same 22-probe,
non-enforced method - enforcement's own extra regeneration calls did
not blow up cost). Full report: `engine/m4/reports/
r27-live-measure-enforced-2026-09-25.json`.

**(a) Does R27 catch the known fabrication types if they recur?** One
of them recurred, in fresh live generation, essentially unchanged:
rzg's `A-conflict` probe produced *"Felix Manz was drowned in the
Limmat River in January 1527"* - the same invented drowning/river/date
detail #558's own run found (*"Felix Manz was drowned in the Limmat
that same year"* / *"...in 1527, execution"*), now compressed into one
sentence. Verified the identical way #558's run verified it: direct
search of rzg's own compiled repository (108 records) for `Manz`,
`Limmat`, `drown`, `drowned` - only `Manz` appears, five times, always
as a name inside the founding Anabaptist-schism narrative
(`rzg.witness.triple-refusal`, `rzg.witness.why-the-children-too`,
`rzg.witness.defending-the-anabaptist-suppression`,
`rzg.force.anabaptist-schism`,
`rzg.contested.anabaptist-schism-legitimacy`) - never with a drowning,
a river, or a specific 1527 date attached. Real Reformation history,
absent from this world's own compiled ground. **R27, with enforcement
on, did not catch it.** The reason is structural, not a fluke of this
run: the sentence sits inside a paragraph with four other, genuinely
tagged sentences (`rzg.witness.triple-refusal` and
`rzg.witness.why-the-children-too` on the opening sentence,
`rzg.witness.why-the-children-too` again on the second,
`rzg.witness.defending-the-anabaptist-suppression`/`rzg.witness.
triple-refusal` on the fourth, `rzg.witness.triple-refusal` on the
closing sentence) - it is a plain per-sentence
`uncited_claim`, never a `wholly_uncited_paragraph`, and it names no
other tradition, so it is never `neighbour_named` either. Both are the
*only* two classes `r27_enforce` was ever built to act on
(`engine/m4/turn.py`'s own docstring: *"a wholly_uncited_paragraph
offense or a neighbour_named offense... inherited_ungrounded stays
report-only"*) - a bare uncited claim riding inside an otherwise-cited
paragraph is a third, narrower class this mechanism was never built to
touch at all, live-confirmed exactly where it matters: the one
fabrication that recurred. No new fabrication type (beyond a
recurrence of this same one) was found among the 22 probes' own raw
offenses in the time available for this measurement - see the offline
audit below for the population this run did not itself re-examine.

**(b) False drops - hand-read against each world's own compiled
repository, same depth as the Athanasius/Eustathius/Manz/Alexandria
checks.** 8 of 22 probes (36%) regenerated; 5 of 22 (23%) exhausted -
`enforcement_exhausted=True`, `voice_event["text"] == ""`, the
Facilitator substitutes for the world's own voice entirely. **Every
one of the 8 regenerations checked against its own world's compiled
repository turned out to be a false trigger on genuinely supported or
honest-limit content - zero confirmed genuine catches among this run's
own 8 enforcement actions:**

- `cappadocian` B-other-tradition (exhausted): *"That is Alexandria's
  own school reaching us, one teacher back, through a student who
  brought what he learned to our country and founded what became
  ours"* - a loose gloss, not a confirmed grounding: the only support
  in `cappadocian.figure.gregory-thaumaturgus` is *"a third-century
  missionary bishop of Pontus, trained by Origen"* - real, but the
  record neither says "Alexandria's own school" nor places the
  training there (Origen's own teaching after Alexandria was at
  Caesarea Maritima, not named in this record at all); the sentence
  stretches "trained by Origen" into a claim about Alexandria's school
  the record itself doesn't make. Still a false trigger, not a
  fabrication - the paragraph's closing honest-limit sentence, *"After
  that, silence,"* was independently flagged `wholly_uncited_paragraph`
  - the same SCAFFOLD_MARKERS coverage gap Entry 61 already named on
  syr's *"Beyond that, the record runs thin"* - stacking with the
  overstated-but-real neighbour mention to exhaust the whole turn.
- `hal` A-conflict (exhausted): *"His name was Origen - an Alexandrian
  master, long dead, whose commentaries on scripture both Jerome and
  his friend Rufinus had translated and praised"* - this sentence is
  NOT untagged: it ends `[[hal.force.origenist-controversy]]` in the
  draft's own raw text, and that record does support it almost
  verbatim (*"close enough to share the same admiration for the great
  Alexandrian master, Origen, whose commentaries both men
  translated"*). `find_uncited_claims` only exempts a sentence when
  `grounding_net`'s own per-sentence verdict is `"ok"` AND it carries a
  tag (`engine/m4/uncited_claims.py`'s own `find_uncited_claims`); here
  the tag is present but the verdict was not `"ok"` - the grounding
  check itself rejected a tag that, on independent hand-verification,
  actually supports the claim. Correctly a false trigger, but the
  mechanism is "the grounding check disagreed with a real tag," not
  "an untagged mention" - this is `hal`'s own central, on-topic
  narrative, killed entirely on an ordinary in-scope conflict probe,
  not even an `other_tradition`-routed turn.
- `ijc` B-other-tradition (exhausted): two separate hard offenses fired
  in the same answer. *"What we do have are Athanasius and Cyril -
  both bishops of Alexandria - reaching us through their own parts in
  our authority contests"* ends `[[ijc.story.letter-that-outranked-a-
  council]]` in the draft - again a rejected tag, not an absent one;
  the record does support it (Julius of Rome's letter defending
  Athanasius, this world's own earliest surviving Roman primacy claim),
  cited twice elsewhere in the same answer. Separately, the closing
  paragraph's own honest-limit sentence, *"Those pages were never
  written, or never kept,"* carries no tag anywhere in its paragraph
  and tripped `wholly_uncited_paragraph` independently - the same
  SCAFFOLD_MARKERS gap as `cappadocian` B above.
- `pahc` A-conflict (exhausted): *"Both were live, both were argued
  for, and neither won before our time ended. That was our real,
  unresolved fight"* - confirmed grounded almost verbatim in
  `pahc.witness.what-we-never-settled` (*"One region pressed toward a
  single bishop; another held a council of elders with nothing felt
  missing. Both persisted, unresolved... the question was only settled
  after we had already closed"*) - no neighbour named here at all; a
  plain `wholly_uncited_paragraph` false catch on a sentence this
  world's own record states almost word for word.
- `pahc` B-other-tradition (exhausted): *"roughly around 200 - are the
  same years when Alexandria's own Christian teaching first becomes
  visible"* and *"Alexandria is not among them"* - confirmed grounded
  in `pahc.force.alexandria-emergence` (dates Alexandria's own tradition
  to c. 190-254, overlapping only at pahc's closing edge) and
  `pahc.contested.rivals-undefeated` (the neighbours pahc actually
  argued with), both cited elsewhere in the same answer. This is
  exactly the honest, well-grounded answer a `B-other-tradition` probe
  is meant to produce - wiped to nothing.
- `witt` A-conflict (regenerated, not exhausted - survived to a
  rewritten final answer): *"It is a fight inside one claim, unresolved,
  that our own confession itself left standing without ranking either
  voice above the other"* - confirmed a direct paraphrase of
  `witt.contested.justification-accounted-and-made`'s own `claim` field
  (*"not an independent claim standing beside the first... What cannot
  be settled from this record is which wording, if either, is
  fundamental"*).
- `don` B-other-tradition (regenerated, not exhausted): *"So if
  Alexandria held a bishop in our own years... we would have cared
  about that. But no record of ours says we ever asked the
  question"* - honest-limit hypothetical reasoning, not a claim about
  Alexandria at all, caught by `neighbour_named` on the bare mention.
- `cappadocian` A-conflict (regenerated, not exhausted): the opening
  two sentences of a `wholly_uncited_paragraph` (*"It was not a fight
  between us and obvious enemies outside. It was a rupture inside the
  household..."*) read as rhetorical/interpretive framing of a
  narrative the same paragraph substantiates immediately after with
  real citations - the same "detector over-flags real declarative
  prose relative to what it's actually for" gap Entry 61 already
  measured (26/40 interpretive-or-connective there).

**8 for 8 false triggers, 0 for 1 on the one real fabrication that
recurred**, in this sample.

**Honest limit on what the committed artifact itself can re-verify.**
The `classify_neighbour_named` refinement (which of the offenses above
is `neighbour_named` versus plain `wholly_uncited_paragraph`) was
computed in a separate, uncommitted analysis pass against the run's
raw offenses, not persisted as a field in
`r27-live-measure-enforced-2026-09-25.json` - the classifications
stated for `hal`, `don`, and `pahc` B above rest on that separate pass,
not on anything a reader of the committed file alone can re-derive
without re-running `classify_neighbour_named` themselves. Separately,
for every exhausted probe (`cappadocian` B, `hal`, `ijc` B, `pahc` A,
`pahc` B), `engine/m4/turn.py`'s own `r27_enforce` logic discards the
failing regenerated attempt's text entirely once the retry also
hard-fails (`raw_text = ""`), and this measurement did not separately
capture that intermediate attempt - only the original draft and the
fact of exhaustion survive in the committed artifact. The false-drop
verifications above rest on the draft text (present) plus each world's
own compiled repository, not on the retry text itself (absent).

**(c) Participant effect.** Every exhausted turn is replaced, verbatim,
by `engine.m4.facilitator_turns.voice_rejected_turn`'s own fixed text:
*"This is the Facilitator, stepping in for a moment - {name}'s last
answer didn't hold together the way it should have, so I'm setting it
aside rather than passing it on to you. Ask again, or ask something
else - I'm still here."* Given that every one of the 5 exhausted
answers checked above was in fact accurate or honest-limit, this
message does not merely withhold an answer - it tells the participant
something false about the world's own voice, in the world's stead,
5 of 22 times (23%) in this sample. The 3 regenerated-but-surviving
turns did not go blank and did not read as obviously stilted or cut
short on inspection (`witt` A's revised answer covers the same
material, reorganized; `cappadocian` A's keeps its full narrative,
citations intact) - the cost there is a wasted regeneration call and an
unnecessarily rewritten answer, not a lost one.

**(d) Latency and cost overhead.** Cost: $1.6049/22 probes, same order
of magnitude as the non-enforced runs in this line (above) - the extra
regeneration call on 8/22 (36%) probes did not meaningfully change
total spend. Latency was not separately instrumented per call in this
measurement (a named, honest gap, the same discipline Entry 61 already
used rather than glossing it over) - the structural implication:
every regenerating turn (36% here) pays for one full additional
voice-generation call before anything reaches the participant, roughly
doubling that turn's own generation latency, and every exhausted turn
(23% here) additionally needs a Facilitator turn built before the
participant sees anything at all.

**Offline audit (no live spend): the 39 control-run sample sentences
not carried to the Athanasius check's own depth.** The control run's
own 150 raw offenses were not persisted as a separately-saved 40-
sentence sample list (only the aggregate `all_offenses` JSON survives,
`engine/m4/reports/g1-precision-sample-measure-control-2026-09-25.json`
on branch `r42-citation-contract-inference-sentence`) - this audit
reconstructs a 40-sentence stratified sample from that same population
using the same proportional-per-world method Entry 61/#558 describe (2
proportional to each world's own share of the 150, capped at 5,
minimum 2), deliberately including the already-confirmed Athanasius
sentence, an honest methodology note about the reconstruction stated
plainly rather than glossed over. Verified each of the other 39 by
direct search against that world's own compiled repository and
`cic/texts/`, to the same depth as the Athanasius/Manz checks above:

**1 unsupported/fabrication (the already-confirmed Athanasius sentence),
29 supported but untagged, 10 interpretive/connective.** No second
fabrication found in this 39. The Athanasius claim stands as an outlier
in this sample, not a typical case - the other 39 are overwhelmingly
real, specific content (often near-verbatim) traceable to a named
record that simply carries no inline tag: alx's *"For years they held
together... Demetrius governed the church... The break came over
authority"* is verbatim `alx.story.origen-demetrius`; syr's claim that
Bardaisan held free will against fate is near-verbatim
`syr.dw.god`; ijc's *"documented by a pagan historian who saw the
cost"* checks against the actual vendored primary source
(`cic/texts/ammianus-marcellinus_roman-history_yonge1862.txt`, Res
Gestae XXVII.3.12-13: 137 dead at the Basilica of Sicininus) as well as
`ijc.quote.ammianus-sicininus-massacre`; witt's Augsburg Confession
claims check against the vendored primary text itself
(`cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`, Article
XX). Two borderline judgment calls, neither a fabrication: ijc's
*"Damasus's faction did the killing"* states the standard historical
reading of Ammianus's account a shade more causally than the primary
text's own wording; witt's *"states both in a single paragraph"*
compresses two real Article XX clauses that are Documented but
~60 lines apart, not literally one paragraph. **This 40-sentence
sample does not itself establish the fabrication rate across the
control run's full 150 raw offenses** - it confirms the citation-
contract failure in this control run is overwhelmingly "real content,
missing tag," with the Athanasius sentence a genuine, singular
fabrication inside that population, not proof the population holds
only one.

**Recommendation for the managing thread.** Do not switch R27
(`CIC_R27_ENFORCE`/`r27_enforce`) on by default in its current
paragraph/`neighbour_named`-only form. This measurement's own live
result is as clean a negative as this project has produced on an
enforcement candidate: the one confirmed fabrication that recurred
went uncaught by construction (it is a bare per-sentence uncited claim
inside an otherwise-cited paragraph - the exact class this mechanism
was never built to touch), while every single enforcement action this
run actually took (8 of 8) fired on content independently confirmed
supported or honest-limit, 5 of them (23% of all 22 probes) driving the
participant's turn to a blank, Facilitator-substituted answer that
actively misstates what the world's own voice did. Turning this on
today would trade a measured 0% catch rate on the fabrication class it
was proposed to stop for a measured 100% false-positive rate on the
enforcement it actually performs, at real participant-facing cost. Any
future enforcement candidate for this fabrication class needs to act at
the individual uncited-claim level inside an otherwise-grounded
paragraph, not the paragraph/neighbour-name level `r27_enforce`
currently checks - closer in shape to option (iii) from Entry 61's own
menu (rebuild the detector around a real support check, "unsupported"
only, re-measured live before any enforcement) than to flipping this
existing mechanism's default. The fabrication finding itself
(`engine.m4.named_claim_grounding`/OG-16 cannot catch it either, by
construction - the control run's own entry already established this)
remains open and unresolved by anything measured here.

**Entry 78 — 2026-09-25.** Sentence-level fact check
(`engine.m4.sentence_fact_check`), managing thread's own follow-up work
order after Entry 77 (PR #567, now merged). **Mark's ruling verbatim (2026-09-25, Decision 3 follow-up): "a."** Build
a sentence-level fact check to replace R27's own paragraph/`neighbour_
named` approach for the fabrication class Entry 77 measured it missing
- Mark's own standing bar: "scholarly rigor that would impress a
professor of church history, not perfection."

**Goal, exactly as given:** catch an unsupported named claim (a person,
place, date, number, or event) in ANY voice sentence, including one
riding inside an otherwise well-cited paragraph - report-only, additive,
no participant-visible change, no enforcement flag in this PR. Full
module docstring: `engine/m4/sentence_fact_check.py`.

**A vocabulary note, stated once rather than qualified every time
below:** "unsupported," "ungrounded," and (where this entry keeps the
project's own established word) "fabrication" all mean the same narrow
thing throughout - a specific name, date, or number that does not
appear anywhere in THIS world's own compiled ground. None of them mean
the named person, place, or event is fictional, or that the claim is
false as history. Athanasius, Alexandria, Pope Liberius, and Ephrem's
*Contra Haereses* are all real; several of the underlying historical
claims below (Felix Manz's drowning, Zwingli's circumcision argument)
are real, documented history too. What every finding below actually
shows is that a real claim has no support in one specific world's own
vendored record - a citation-fidelity defect, not evidence the claim
itself is untrue.

**Design - reuse, not duplication (the explicit constraint).** Every
real piece of machinery already existed:
- `engine.m4.named_claim_grounding`'s own per-record ground computation
  (`_source_ground`, OG-9's own `work`-field/`short_head` truncation) is
  reused via two new factored-out functions in that same file,
  `record_ground` and `repository_ground` - the only change in scope
  this needed: sum a record's own ground over EVERY record in the
  world's compiled repository, not only a sentence's own tag(s). The
  marker-vs-ground comparison itself (`missing_markers`) is the exact
  same code `ungrounded_markers` (unchanged, still tag-scoped, still
  passes its own 15 existing tests unmodified) now also calls - one
  implementation, not two that could drift.
- `engine.m4.uncited_claims`'s own three allowed-uncited exemptions
  (`_is_question`, `_is_honest_limit`, `_is_first_person_no_claim`) are
  reused unchanged.
- `engine.prose.claim_markers`'s own proper-noun/number detection is
  reused, with one narrow, necessary addition (below).

**A real defect found empirically, fixed at the shared root, not
patched around: sentence-initial proper nouns.** First offline pass:
`claim_markers`' own `_proper_nouns` excludes a sentence's OWN FIRST
WORD from proper-noun detection (right for its own narrow, 1-3-record
tag-scoped callers, calibrated there). Two of the four known
fabrications name their own unsupported claim as literally the
sentence's first word ("**Athanasius** of Alexandria was named
among..."; "**Alexandria** itself appears only once in what we
hold...") - with the unmodified function, both are structurally
unflaggable regardless of ground scope. Fixed at the source, not worked
around locally:
`engine.prose._proper_nouns`/`claim_markers` both gained an opt-in
`include_sentence_initial`/`include_sentence_initial_proper_nouns`
parameter, default `False` (every one of the four existing production
callers - `engine.m1.canon`, `engine.m2.builders`, `engine.m4.evidence`,
`engine.m4.grounding_net` - byte-identical, confirmed by the full
`engine/tests/test_prose.py` suite passing unchanged).
`missing_markers` threads the same flag through; only `sentence_fact_
check` passes `True`. Safe specifically at whole-repository ground
scope (module docstring's own reasoning): an ordinary capitalized word
that only coincidentally opens a sentence, not a real name, is either
already stopword/doctrinal-vocab-excluded, or - being ordinary
vocabulary - overwhelmingly likely to also appear elsewhere across an
entire compiled repository, so it grounds itself rather than
false-flagging; the narrow-ground false-positive risk that motivated
excluding position 0 in the first place does not carry over to a
100-300-record ground the same way.

**A second real defect found empirically, also fixed at the root: a
hypothetical/conditional clause.** `don`'s own real R27 false trigger
(Entry 77) - "So if Alexandria held a bishop in our own years... we
would have cared about that. But no record of ours says we ever asked
the question" - names Alexandria (absent from `don`'s own whole
repository) inside a pure subjunctive, and is not caught by `_is_
honest_limit`'s own fixed-phrase/negation regex (that check looks for
an explicit absence claim, not a subjunctive mood). Without a fourth
exemption this module would have reproduced R27's own `neighbour_named`
false-positive shape on the identical sentence. `_strip_hypothetical_
clauses` (new, local to `sentence_fact_check.py`): strips only the
"if"-to-"would"/"would have" span itself before checking, not the whole
sentence - a name or number OUTSIDE that span, even in a sentence that
also contains one, is still checked normally (round-2 review fix, below).
Confirmed against two more real "if...would" hedges #558's own run
produced independently (`cappadocian`, `witt`), never previously scored,
both correctly exempt. **A round-2 review finding, fixed the same day:**
the first version exempted the ENTIRE sentence on a bare "if...would"
co-occurrence, which a reviewer showed would also exempt "Felix Manz was
drowned in the Limmat in 1527, and if you ask why, the council would say
heresy" - a real fabrication riding to safety behind an unrelated
hypothetical clause. Rescoped to strip only the matched span itself
(module docstring's own KNOWN LIMITS section carries the residual gap
this narrower fix still has - the span runs from the literal word "if"
to the next literal "would," not the true grammatical clause boundary,
so a claim sandwiched between an unrelated "if" and an unrelated later
"would" in the same sentence can still be swept up and missed).

**Wiring:** `engine.m4.turn._run_ordinary_voice_turn` gains
`voice_event["fact_check_flags"]`, computed and (on `r27_enforce`'s own
regeneration) recomputed the identical way `named_claim_flags` already
is - same additive, always-`[]`-on-clean-turns discipline. No default
touched anywhere; no enforcement flag exists.

**OFFLINE measurement (no live spend), hand-labeled set drawn from the
three saved JSON reports the managing thread named:**

**Positives - the known fabrication set, 4/6 recall (6 counts two live
recurrences of the same Manz/Limmat fixture as separate rows):**
caught - `rzg` "Felix Manz was drowned in the Limmat that same year"
(#558), `rzg` "Felix Manz was drowned in the Limmat River in January
1527" (Entry 77's own recurrence), `cappadocian` the control run's own
Athanasius sentence, `witt` "Alexandria itself appears only once in
what we hold." **Missed, both a named, honest limit rather than a
defect:** `cappadocian` "Some among us thought he was a coward"
(Eustathius is a real, grounded name; "coward" is an ordinary adjective
- no proper-noun/number marker exists in this sentence at all for any
ground-scope check to compare); `rzg`'s own 1527-execution-progression
sentence ("...fines, then imprisonment, and finally, in 1527,
execution") - "1527" genuinely IS present in `rzg`'s own ground
(`rzg.witness.defending-the-anabaptist-suppression`, a different,
real context), so the bare digit checks out even though the specific
composed claim (a fines-then-imprisonment-then-execution progression
culminating that year) is not independently verified by a
marker-presence check - a structural limit of what this class of check
can do (it verifies a name/number's presence, not the truth of a
claim built by recombining genuinely-grounded pieces), named plainly
rather than glossed over.

**Negatives - 56 hand-verified sentences (the 15 individual sentences
inside Entry 77's own 8 R27 false-trigger probes, 2 more real
"if...would" hedges from #558's own run, and the 39-sentence offline
audit's own 29 supported-but-untagged + 10 interpretive/connective
rows): 1 false positive.** `cappadocian`'s "No Alexandrian bishop is
named attending any synod..." - "Alexandria" (noun) is real ground
here, "Alexandrian" (adjective) is a different token `content_words()`
does not equate to it, the exact "different derivational form" limit
`named_claim_grounding`'s own module docstring already names and
explicitly declines to fix (its own Smyrna/Smyrnaeans fixture) -
inherited unchanged via the shared `missing_markers`, not a new defect.
**Precision on this labeled set: 4/5 (80%). Recall: 4/6 (67%).**

**Broader corpus scan (no live spend), every saved sentence, not only
the hand-labeled ones - genuine additional findings, not just
false-positive noise:** Running the checker over #558's own 141 raw
offenses, the control run's own 150, and Entry 77's own 343 full
reconstructed sentences (draft text, every sentence, tagged or not)
surfaced two clean, independently-verified findings neither prior audit
caught: `ijc`'s own recurring "Pope Liberius had died..." (both in
#558's run and, independently, in Entry 77's own run) - "Liberius"
appears **zero** times anywhere in `ijc`'s compiled repository, real
history the world's own build simply never vendored, verified by direct
search across all records the same way the Athanasius/Manz findings
were; and `syr`'s "his Hymns Against Heresies" (Ephrem's real *Contra
Haereses* cycle) - genuinely absent from `syr`'s own vendored ground,
not a wrong title: `syr.search.ephrem-corpus-gaps` (a `search_record`,
not part of the citable repository this module grounds against) already
names *Contra Haereses* as a work this world's own build never found a
complete public-domain English translation of, quotable only through
`syr.source.ephrem-prose-refutations`, a *different*, vendored work -
"the heresiological hymns that built this world's own boundary are
quotable only via the Prose Refutations... a named limitation, not an
oversight," in that record's own words. The sentence names a real work
correctly; that work is simply outside what this world's own compiled
ground can support. Both findings are the identical shape as the four
known fixtures (a real, checkable claim with zero support in THIS
world's own compiled ground - not that the claim is invented), found by
this module on real saved data no one had re-examined this closely
before. The remainder of the corpus scan's own
flags repeat the two already-named limitation classes above
(derivational form: `alexandrian`/`alexandria`; a spelled-vs-digit
number mismatch, below) plus one borderline case (`alx`'s "taught for
another twenty years in Caesarea" - a reasonable arithmetic
approximation from two real grounded dates [c. 231-234 to c. 253/4],
not a wholesale invention, flagged because no record states "twenty"
literally - named as borderline, not scored either way).

**LIVE measurement, same 22 probes, current `origin/main`, region
us-east-1, no `r27_enforce`, no enforcement of any kind - purely
observing the new report-only field on real traffic.** **Real cost:
$1.4857, under the $3.00 ceiling.** Full report: `engine/m4/reports/
sentence-fact-check-live-measure-2026-09-25.json`. 9 flags across 22
probes, hand-verified against each world's own compiled repository the
same way as above:

**5 of 9 flag real gaps in this world's own vendored ground, but not all
five are equally strong evidence of the fabrication class this module
was built to catch - restated honestly rather than folded into one
count.** Three read the same way as the known fixtures - a specific
name, unsupported, presented declaratively: `rzg` A-conflict's own
Manz/Limmat sentence recurred a **third** independent time live ("Felix
Manz was drowned in the Limmat in 1527 - executed for the very baptism
he had chosen" - "limmat" absent, confirmed again); `rzg`
B-other-tradition's own "We held to the ancient creeds the whole church
confessed - Nicene, Apostles', Athanasian" - all three specifically
named creeds absent, zero occurrences each, the same shape as `ijc`'s
Liberius finding above (a specific historical name asserted with
nothing behind it in this world's own ground); `witt`
B-other-tradition's own "The early centuries' own arguments - Nicaea,
the shape of the creed..." - "Nicaea" absent, and "Nicene" also absent
anywhere in `witt`'s own repository, the same shape again. **The other
two are weaker, and this entry says so rather than counting them the
same way:** `rzg` A-conflict's own "the same pattern Israel's own
circumcision held" - "Israel" and "circumcision" are general biblical
vocabulary, not a specific person/place/date, and Zwingli's own
circumcision-infant-baptism analogy is real, well-documented Reformed
theology, not an invented argument - what this flag actually shows is
that `rzg`'s own compiled ground never states the analogy using these
words, a citation-completeness gap in the world's own theological
vocabulary, not clear evidence the voice invented anything; `syr`
A-conflict's own "what the Messiah was supposed to be" is the same
weaker shape - "Messiah" absent as a literal word, but generic
theological vocabulary in a summary sentence, not a specific checkable
claim about a person, place, or date. Both are correctly flagged by
this module's own literal definition (the word is not in `rzg`'s or
`syr`'s ground); neither is offered here as comparably strong evidence
to the other three.

**4 of 9 are false positives, all falling inside the two limitation
classes already named above - no new false-positive class found live:**
`syr`'s "He was an Edessan" (derivational form of the real, grounded
"Edessa"); `witt`'s "the Alexandrians would have stood" and "no source
in our library names 'Alexandrian Christianity'" (derivational form,
the second also another honest-limit-phrasing-gap instance - "no
source in our library names X" is close to but does not match `_is_
honest_limit`'s own fixed phrases, the identical class of gap Entry 61
already named for `SCAFFOLD_MARKERS`' own coverage); and `ijc`'s own
quoted Ammianus sentence naming "137" - `ijc.quote.ammianus-sicininus-
massacre`'s own ground states the same number spelled ("one hundred
[thirty-seven]"), not as the digit "137" - a THIRD, newly-identified
instance of the same broad "same fact, different surface form" class
(alongside derivational form and, from the offline pass, ordinal/
cardinal mismatch on `alx`'s "eighteen"/"eighteenth") - real, grounded
content, flagged only because the surface form differs from how the
ground happens to spell it. None of these four cost anything
participant-facing: this module makes no enforcement change, so a
false positive here is review-effort cost only, not a blanked turn.

**Recommendation for the managing thread.** Proceed to design an
enforcement PR - Mark's own word, not a decision this entry makes. The
evidence: 0-for-1 (Entry 77) versus this module's own measured
catches, including three independent recoveries of the SAME recurring
claim (`rzg`'s Manz/Limmat, across #558's run, Entry 77's run, and this
entry's own live run) plus four more findings of comparable strength,
previously unknown, across the offline and live passes combined
(`ijc`'s Liberius, `syr`'s *Contra Haereses*, `rzg`'s Nicene/Apostles'/
Athanasian creeds, `witt`'s Nicaea), plus two weaker, honestly-qualified
ones (`rzg`'s Israel/circumcision, `syr`'s Messiah - general vocabulary,
not specific named claims) - all zero-participant-facing-cost, since
this PR ships report-only. The two
false-positive classes are both already-understood, already-documented
limitations of the reused ground-matching machinery (derivational form;
number-representation mismatch), not new or surprising, and - unlike
R27's paragraph/`neighbour_named` enforcement - none of this module's
own false positives would, on today's evidence, need to blank an entire
turn. **A design sketch for that separate enforcement PR, offered here
for whoever picks it up, not built in this one:** drop or regenerate
only the offending SENTENCE this module's own `fact_check_flags` names,
never the whole turn - the one shape Entry 77 measured failing badly (5
of 22 probes wiped entirely, all 5 false triggers). Concretely, that
means a correction naming only the flagged sentence(s) (the same
append-not-replace directive channel `r27_enforce`'s own one-retry
mechanism already uses), one regeneration, and on a second failure
either drop the offending sentence from the answer (never a full-turn
blank or a Facilitator substitution) or fall back to the original draft
sentence with its own tag stripped, rather than losing the rest of an
otherwise-good answer over one uncorroborated claim. That enforcement PR
is Mark's own separate decision to make, not this one's.

**Entry 79 — 2026-09-25.** Sentence-level enforcement (`engine.m4.turn`'s
new `sentence_enforce`), managing thread's own follow-up work order after
Entry 78 (PR #574, now merged). **Mark's ruling verbatim (2026-09-25): "a,
yes to the $3 test run."** Scope, exactly as given: (1) fix the two
false-positive classes the offline/live measurement in Entry 78 found, at
their shared root in the ground-matching machinery; (2) build sentence-level
enforcement, off by default behind a new explicit flag, never
`CIC_R27_ENFORCE`; (3) one live measurement, $3.00 hard ceiling, the new
flag on for this run only; (4) this entry.

**A vocabulary note carried forward from Entry 78, unchanged:**
"unsupported"/"ungrounded" mean a specific name, date, or number absent
from a world's own compiled ground - never that the named person, place,
or event is fictional or that the underlying claim is false as history.

**1. The two false-positive classes - both tried, both removed, at the
shared root (`engine.m4.named_claim_grounding.missing_markers`, called
by both `ungrounded_markers` and `sentence_fact_check.find_unsupported_
named_claims` - one implementation, so neither check could fix or
regress this alone). Mark's own follow-up ruling, verbatim (2026-09-25):
"a on 578" - remove the digit/spelled cross-form check entirely, the
same way the derivational bridge was removed, and don't patch the parser
again.**

- **Digit/spelled number - tried across two rounds of narrowing, then
  removed, not patched a third time.** The first version compared a bag
  of a number's own component WORDS against a ground bag (the real bug
  it shipped with: "seven" matched an unrelated ground number spelled
  "twenty-seven," because a bag cannot tell the two apart - measured at
  scale, hundreds of false accepts per world under a 0-999 probe). The
  second version replaced that with a real cardinal grammar
  (`_parse_below_hundred`/`_parse_below_thousand`/`_parse_cardinal`)
  parsing every digit run or spelled-cardinal phrase to its own exact
  integer value, comparing values rather than words - "and" joining a
  hundred/thousand block to its own remainder and two adjacent numbers
  never being summed both had to be special-cased in the grammar itself
  to keep it from silently composing a value neither side of a claim
  actually stated. Per this project's own "no fix on a fix," the whole
  mechanism is removed rather than narrowed further:
  `_parse_cardinal`/`_parse_below_thousand`/`_parse_below_hundred`/
  `_numbers_in_text` are gone. A number now grounds only against its own
  exact surface form - a digit against a digit token, a spelled word
  against a spelled word, never across the two (`_number_tokens`, the
  same digit/spelled split the code used before this PR ever touched
  it). "137" against a ground spelling the same count out, or the
  reverse, is now a named, accepted false-positive class in both
  `missing_markers`' own module docstring and `sentence_fact_check`'s
  own KNOWN LIMITS - it flags; it never grounds a wrong number, and it
  never silently grounds the right one stated in the other form either.
- **Derivational form - tried, then removed, not patched again.** The
  first version of this fix bridged a place name ending in "a" against
  its own bare-"n" adjective (Alexandria/Alexandrian, Edessa/Edessan).
  Gating that bridge on a world's own figure lexicon (real people, known
  from that world's own figure records) was meant to stop it
  cross-grounding a different person who happens to share the same
  surface shape - it did not work: Julian/Julia, Hadrian/Hadria,
  Lucian/Lucia, Domitian/Domitia, Sebastian/Sebastia, Flavian/Flavia,
  and Claudian/Claudia all still crossed, because none of those names
  happened to be a figure record in the worlds actually measured. A
  figure-lexicon gate is a NEGATIVE signal (not a known person) standing
  in for a POSITIVE one (is a known place) that no world's own compiled
  repository can supply yet - none carries place records to check
  against. Per this project's own "no fix on a fix," the bridge is
  removed entirely, not narrowed a third time: `_derivational_variants`
  is gone, and a proper noun grounds only against its own exact surface
  form. Alexandria/Alexandrian is now named plainly as an accepted,
  unfixed false-positive class - the same status Smyrna/Smyrnaeans
  already had - in both `missing_markers`' own module docstring and
  `sentence_fact_check`'s own KNOWN LIMITS. The seven negative-pair
  tests (Julian/Julia and the other six) are kept, converted from
  proving a gate works to proving no bridge exists at all - the
  regression guard against this coming back without a real place-based
  design.

Both removals carry their own tests: the number check's own parser
positives are gone; what remains proves the exact-surface-form behavior
directly - a digit/word mismatch flags each way (`"137"` against a
spelled ground and the reverse), and two named negative guards pin the
two cases Mark's own ruling called out by name ("one hundred and
thirty-seven" against a ground holding 37; "fifteen twenty-seven"
against a ground holding 42) - plus the pre-existing guards against the
first version's own bag-of-words bug, unchanged. The derivational
bridge's own seven negative pairs plus the Alexandria/Alexandrian pair
itself stay exactly as Entry 79 first left them, still asserting it
flags rather than asserting it grounds.

**Re-measured offline (no live spend), the exact hand-labeled set and
corpus scan Entry 78 used, against the current code:**

- **Hand-labeled set: recall unchanged at 4/6** (the same two structural
  misses Entry 78 named - a characterization with no name/number marker
  of its own, and a composed claim from individually-grounded pieces -
  neither is this fix's job). **False positives: 1/56, unchanged from
  Entry 78's own original measurement, and unchanged again by this
  round's own further reversion** (`cappadocian`'s "No Alexandrian
  bishop..." is the one false positive in this labeled set, and it is a
  derivational-form case, not a number-form one - removing the number
  check a second time does not move this count). **Precision on this
  labeled set: 4/5 (80%), Entry 78's own original figure.**
- **Corpus scan (the same three saved JSON reports): both false-positive
  classes are back**, as expected once both mechanisms were removed -
  the derivational flags (already back after this entry's first pass)
  are joined by the number-form ones. A fresh scan of the same three
  reports turns up two new instances at scale not seen in Entry 79's
  first pass, both digit-vs-spelled: `alx`'s "since he was eighteen"
  (the record's own ground states the age as a digit) and `alx`'s
  "taught for another twenty years" (same pattern). The two genuine
  findings Entry 78 already named (`ijc`'s Liberius, `syr`'s *Contra
  Haereses*) are unaffected either way - neither is a number-form or
  derivational-form case.

The claim in this entry's own first pass that "hundred and" phrases
parse to their own correct value across the real corpus no longer
describes the code: that parser is gone, and no cross-form parsing of
any kind happens anywhere in this module now. Removed here rather than
left standing as a description of code that no longer exists.

`check_live_commentary --surface engine` shows 0 new findings in
`grounding_net.py`, `named_claim_grounding.py`, and `sentence_fact_check.py`
(the fix files themselves). `turn.py`'s own pre-existing `r27_enforce`
identifier findings moved from 25 to 30, and the test file's from 15 to
22, after two rewording passes: every new prose comparison now says "the
uncited-claims enforcement" rather than the bare identifier - what
remains is the real parameter declaration, the actual code conditions
that read it, and the few spots where naming the exact flag is
unavoidable (a kwarg at a call site, an assertion against the real
returned field). Logged as a count update in
`Ministry/Operations/Audits/Tech-Readiness-2026-09/Live-Surface-
Cleanup/Decision-Log.md` Entry 12 (not 10 - that file already carries an
earlier, pre-`## Entry 1` "Entry 10"), same out-of-scope-to-rename
reasoning as that program's own Entry 9. The new report artifact,
`engine/m4/reports/sentence-enforce-live-measure-2026-09-25.json`, adds
23 more findings, all `PROTECTED` (the checker's own existing
`engine/*/reports/` carve-out) - no move needed, explained in that same
Entry 12.

**A correction to Entry 78's own record, updated three times now as the
fix itself changed shape - reported honestly rather than folded in as a
silent win.** Of Entry 78's own 4 live false positives: `ijc`'s quoted
"137" sentence was fixed by the number-value parser while that parser
existed; now that the parser is removed entirely (section 1 above, this
round's own ruling), it flags again, exactly as it did before Entry 78's
own fix - confirmed by direct replay (`Ammianus counted 137 dead in the
Basilica of Sicininus` against `ijc.quote.ammianus-sicininus-massacre`'s
own ground, which states the count spelled out, not as a digit). `syr`'s
"He was an Edessan" was fixed by the derivational bridge while that
bridge existed; now that the bridge is also removed entirely, it flags
again the same way. Both are back to their original, still-accepted
false-positive status, not a new defect. The other 2, both `witt` ("the
Alexandrians would have stood"; 'no source in our library names
"Alexandrian Christianity"'), were never derivational-form false
positives to begin with, regardless of either mechanism's own fate: a
direct check of `witt`'s own compiled repository (`repository_ground`)
shows zero occurrences of "alexandria"/"alexandrian"/"alexandrians"
anywhere in it - the same reason the third sentence in that same probe
("Alexandria itself appears only once in what we hold") was already,
correctly, counted as a TRUE positive. All three `witt` Alexandria
sentences are consistently, correctly flagged, before either fix,
during each fix's own brief existence, and now after both are removed.
Entry 78's own classification of two of them as false positives was a
misreading at the time, not a defect either version of either fix
introduces or resolves - stated here rather than quietly re-labeled.
**Net: 0 of Entry 78's own 4 live false positives remain fixed by this
PR's final state.** Both mechanisms that had briefly fixed two of them -
the number-value parser, the derivational bridge - were each tried,
found unsafe on review, and removed per this project's own "no fix on a
fix," restoring the exact behavior those two findings already had
before this entry began. Named as two accepted limits, not shipped as
partial, unsafe fixes.

**2. `sentence_enforce` - the new, independent, flag-gated enforcement.**
`engine.m4.turn._run_ordinary_voice_turn` gains a second parameter,
distinct from `r27_enforce` in flag, mechanism, and failure shape,
threaded through `run_turn` the same way; OFF by default, every existing
test and caller byte-identical (the full suite passing unchanged with the
parameter simply absent proves it). Deliberately left unwired past
`turn.py`'s own two entry points for now - no `CIC_SENTENCE_ENFORCE` env
var, no `config.py`/`app.py`/`wiring.py`/`table_wiring.py` plumbing to a
real deploy. That reach is `r27_enforce`'s own, built and staged in an
earlier, separately-ruled pass; this PR is the same build-then-measure
stage `sentence_fact_check` itself went through in Entry 78, and whether
to give it that same reach is the managing thread's own next decision,
not assumed here.

When `sentence_enforce` is True and `find_unsupported_named_claims` flags
anything against whichever text `r27_enforce` (if also on) already
settled: one regeneration, with the flagged sentence(s) named in the
retry's own directive (`_append_sentence_fact_check_correction`, the same
append-not-replace channel `_append_r27_correction` already uses - a
third mechanism was not written). **Composed, not replaced:** when
`r27_enforce`'s own correction already fired this turn, that same
correction rides forward into this retry's own directive too - a fresh
regeneration has no memory of an earlier call's own correction, so
without carrying it forward this retry could regress a citation fix
`r27_enforce`'s own retry had already won. A new test
(`test_sentence_retry_carries_the_r27_correction_forward`) reads the
actual captured system content sent to the model on this retry and
confirms both corrections are present, not just the turn's own outcome.

The regenerated answer is checked TWICE, in order. First, when
`r27_enforce` is on: this retry is a fresh generation that enforcement's
own pass never saw, so it could just as easily reintroduce a
`wholly_uncited_paragraph`/`neighbour_named` offense as fix the named
claim - a hard offense surviving here is `r27_enforce`'s own exhaustion
(its one-regeneration budget was already spent in the earlier block),
the identical whole-turn-blank/Facilitator-substitution fallback its own
second failure already uses. A new test
(`test_wholly_uncited_paragraph_never_ships_with_r27_enforcement_
exhausted_false`) proves the invariant directly: such an offense can
never ship with `r27_enforcement_exhausted` left `False`.

Only when no `r27_enforce` hard offense survives does `sentence_enforce`
decide for itself. Support the claim or drop it, literally what the
correction asks for. If a sentence is still flagged after that one
regeneration, it alone is removed from the answer
(`engine.m4.grounding_net.drop_flagged_sentences`) - **unless dropping
every still-flagged sentence would leave nothing behind, in which case
nothing is dropped: the regenerated answer is kept exactly as it stands,
flagged sentence and all, and `fact_check_flags` reports the flag still
standing on it.** Mark's own ruling: never blank the turn, even in that
edge case - this mechanism's failure mode is never the whole-turn blank
Entry 77 measured R27 getting wrong (5 of 22 probes wiped entirely), and
never a Facilitator substitution either. A new test
(`test_sentence_enforce_never_blanks_the_whole_turn_or_substitutes_the_
facilitator`) pins the all-flagged case directly: the kept text, the
flag still reported, `r27_enforcement_exhausted` staying `False`. Every
other report-only field (`uncited_claims`, `paragraph_offenses`,
`named_claim_flags`, `fact_check_flags`) is recomputed against whichever
text this turn ultimately answers with, the same recompute-on-retry
discipline `r27_enforce`'s own retry already follows. A new,
always-present `voice_event["sentence_enforcement"]` key
(`flagged`/`regenerated`/`still_flagged`/`sentences_dropped`) records
what happened - `sentences_dropped` stays empty and `still_flagged`
alone shows the standing flag in the all-flagged, nothing-dropped case.

`drop_flagged_sentences` reuses `grounding_net`'s own
`split_into_paragraphs`/`parse_tagged` - the identical sentence/paragraph
boundaries every verdict was already computed against, so a flagged
sentence is matched and removed unambiguously, never by re-splitting the
text a second, separately-tuned way. Two structural guarantees: a
paragraph that loses every one of its own sentences is dropped whole, not
left as an empty blank-line block; a paragraph that keeps at least one
sentence keeps its own survivors joined by a single space, so a mid-
paragraph drop leaves no doubled whitespace, no orphaned tag, no broken
quote span. **A named, honestly-disclosed limit, not fixed here:** a
sentence that grammatically promised the one just removed (a paragraph
ending "...three things stand out:" whose own next sentence was the one
dropped) can still read as an unfinished promise - a semantic dangling
fragment this string-level operation has no way to see, as distinct from
the structural one (broken punctuation, an empty paragraph) it does
prevent. Not observed in this run's own 22 probes (below); tracked, not
papered over.

**3. LIVE measurement, same 22 probes, current branch, region us-east-1,
`sentence_enforce=True` for this run only, `r27_enforce` off (its own
default) - the new mechanism's own first live test.**

**Real cost: $1.5072, under the $3.00 ceiling, all 22 probes ran (no early
stop).** Full report: `engine/m4/reports/sentence-enforce-live-measure-
2026-09-25.json`.

**0 true catches, 1 false positive, across 22 probes. The recurring Manz/
Limmat fabrication (Entry 77's own R27 miss, caught independently three
times since - #558's run, Entry 77's own run, Entry 78's live run) did
not appear in this run's own 22 generations at all - there was nothing
of that shape for this mechanism to prove itself against here.** Draw no
conclusion about `sentence_enforce`'s own effectiveness from this run;
see what it actually shows below.

21 of 22 probes generated clean on the first attempt - no flag, no
regeneration. One did, and re-reading it against the participant's own
question shows it was wrong to flag: `rzg` B-other-tradition was asked
"What was your relationship with Alexandrian Christianity?" and answered,
in part, "Not from Alexandria, not from Rome, not from any unbroken
succession of teachers - from the text, read and tested aloud." That
sentence is a rhetorical contrast, not an assertion about Alexandria or
Rome - it names both places only to deny that either is where `rzg`'s
own authority comes from, the direct, on-topic answer to the question
actually asked. "rome" happens to be real ground in `rzg`'s own compiled
repository and "alexandria" is not, so the sentence flagged on
"alexandria" the same way a genuine fabrication would. The one allowed
correction fired; the regenerated answer named the identical sentence
again (the voice had nothing to change - the sentence was never wrong),
so it alone was dropped. **This is a false positive with real
participant-facing cost, not a catch:**

    Our record doesn't mention that Christian tradition.

    What we will tell you is where we stood ourselves. Our own founder
    said it plainly in 1523: where we have not rightly understood the
    Scriptures, we will be taught better - but only from the Scriptures
    themselves. Fifteen hundred years stand between Christ's own life
    and ours. We hold no living chain, and we do not need one. What we
    have is the text, and we hold that it is enough on its own terms.

The dropped sentence was the part of the answer that actually named
Alexandria and addressed the participant's own question directly; what
remains still answers the question in substance, but the sentence that
named the tradition asked about by name is gone. Structurally, the drop
is clean (no dangling fragment, no orphaned clause) - the cost here is
not a broken sentence, it is losing the most directly responsive part of
the answer to a false flag. `voice_event["r27_enforcement_exhausted"]`
stayed `False` throughout this run (`r27_enforce` was off, its own
default), and every one of the other 21 probes' own `fact_check_flags`
came back empty - but that is 21 probes that never exercised the
correction/drop path at all, not 21 probes that proved it safe.

**The open problem this run names, honestly, not fixed here:** a name
mentioned rhetorically - a contrast, a denial, a hypothetical the
world's own record never states in those terms - is flagged exactly the
same way an asserted claim naming that place would be.
`find_unsupported_named_claims` sees the name, not the grammatical role
it plays in the sentence around it, and neither `missing_markers` nor
this entry's own section 1 fixes touch that gap (`sentence_fact_check`'s
own module docstring, KNOWN LIMITS, now names this class directly). One
real trigger in 22 probes is not enough to measure how often this
happens at scale; it is enough to show it happens, and that when it
does, the cost lands on the participant, not just on review effort.

**Recommendation for the managing thread.** Both ground-matching
mechanisms section 1 tried are now removed, per Mark's own follow-up
ruling: false positives on the labeled set stay at 1/56, unchanged from
Entry 78's own original measurement, not reduced by either attempt -
and honest re-audit of Entry 78's own 4 live findings shows 0 of them
fixed by this PR's final state (2 were genuinely fixed for a time by a
mechanism now removed; the other 2 were never false positives to begin
with, corrected here rather than silently carried forward). The digit/
word number-form mismatch and the derivational-form mismatch are both
named, accepted, unfixed false-positive classes now, the same status,
not a regression against any baseline this project has actually shipped.
The enforcement mechanism itself is untested by this run in the way that
matters most: its one live trigger was a false positive that cost the
participant the direct answer to their own question, not a caught
fabrication - 0 true catches, 1 false positive, is not evidence the
mechanism works, and this entry does not claim it is. Before
`sentence_enforce` goes anywhere near `r27_enforce`'s own reach (a
`CIC_SENTENCE_ENFORCE` env var, the `config.py`/`app.py`/`wiring.py`/
`table_wiring.py` plumbing to a real deploy), the rhetorical-mention
false-positive class named above needs either a fix or a measured
sense of how often it fires - neither exists yet. That is the managing
thread's own next decision to make, not assumed here.

**Entry 80 — 2026-10-02.** Coordination entry before editing `engine/m4/turn.py`, `engine/m4/round.py` and `engine/m4/facilitator_turns.py`, for the P1-Security daily-cap ruling (P1-Security Decision-Log entry 10, "Item 9b ruled"). `run_turn` and `open_table_round` gain a `daily_cap_reached` flag, checked beside the session cap after the gate and before any voice call, with the same acute-crisis exemption. `facilitator_turns` gains `daily_cap_turn`, a close-kind template. No change to the gate, routing, grounding, citation or transparency code this workstream owns.

**Entry 81 — 2026-10-02.** The conversation system design was approved to proceed (System Hub Decision Log, "Conversation system design: approved to proceed, Design C"). Its five change orders on the Program Spec are entered in `Rulings-Pending.md` as R43 to R47. R47, the citation mechanism, is ruled (Mark's decision 10): native API citations replace the hand-copied citation ids, and R9, R10, R17 and the R27 family keep their meaning, marks, placement and cap. It is not trusted until E1's third arm proves it. R43 to R46 are pending. No code changes in this entry.

**Entry 82 — 2026-10-02.** Slice 0 of the conversation system design: the standing-measure suite and the baseline band. `engine/m7/standing_measure.py` scores each world-run from the saved admission transcripts with no model call, and computes the band across the three baseline runs (`engine/m7/band/baseline-2026-10-02.json`). The transcripts are 33 runs, 11 worlds three times each, on the packages pinned on 2026-10-02, voice model `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, self-revision not in the harness path, in `engine/m3/reports/baseline-2026-10-02/`. Every world passed 28 of 28 in every run. Metered cost of the baseline including its sample: $16.81.

Fleet row (mean of world means, with the lowest and highest world):

| Dimension | Mean | Min | Max |
|---|---|---|---|
| cutoff_rate | 0.016234 | 0.0 | 0.059524 |
| distinctness_overlap | 0.015662 | 0.013656 | 0.017018 |
| invented_ids_per_100_sentences | 0.448152 | 0.0 | 1.392335 |
| pass_rate | 1.0 | 1.0 | 1.0 |
| readability_fk_median | 8.23147 | 7.000698 | 10.078949 |
| readability_fre_median | 68.175673 | 59.098508 | 73.835535 |
| seconds_to_first_text_median | 1.466182 | 1.342167 | 1.6205 |
| seconds_total_median | 12.31597 | 10.461833 | 14.68 |
| usd_per_reply_mean | 0.017526 | 0.011972 | 0.025153 |
| withheld_mark_rate | 0.074007 | 0.029055 | 0.108164 |
| words_median | 270.681818 | 237.0 | 320.5 |

Invented ids, withheld marks and cut-offs are noisy at this sample size: several worlds' half-range exceeds a third of their mean, because each world has only a handful of such events in 84 replies. The other dimensions are steady across runs.

Eleven dimensions are not computed yet, each named in the band file with the slice or instrument that supplies it: meaning fit, citation support, honest-limit honesty, first sentence answers the first ask, asks covered, restating the participant, horizon leaks, future-leak rate, quote verbatim, safety routing, and full-turn cost and delay.

Open: the risk guard's staleness half. The suite's test fails when the band file is missing or does not reproduce from the transcripts. It does not yet fail when a later slice changes a measured surface without a fresh band; that needs a definition of the measured surfaces, which slice 3 (the shape segment, the first change to one) supplies.

**Entry 83 — 2026-10-02.** Slice 1 of the conversation system design, the remaining two production fixes. The self-revision setting was fixed earlier the same day (#699). (1) The voice model is pinned in `render.yaml` on both services to `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, the exact profile the baseline band was measured on, the way the safety model was already pinned. It no longer floats on a pattern. (2) `engine/m8/price_tables.py` prices by model: `price_for_model` matches the model family inside the provider's model id, and `price_for_call` keeps preflight unpriced. The usage dashboard (`engine/api/wiring.py`) now prices each call by the model it actually ran on, not by its call kind, so a model change can no longer be priced at the old model's rates. Rows exist for Sonnet 4.5, Haiku 4.5, Sonnet 5.5 and Opus 5.5. The 5-family rates are Anthropic's published first-party rates; Bedrock's rates for them are not independently verified. The offline run scripts in `engine/m8` and `engine/m4` still price by call kind for their fixed models; they move when they next change.

**Entry 84 — 2026-10-02.** Matcher recall measured before E1, at no API cost, from the 33 baseline runs. This is the risk guard set for the case: a poor number redesigns E1 rather than running it.

- Of the distinct records a reply cited, 30.7% carry the probe's own cell in `canon_cells`, so a one-cell dossier would have held them. With two cells, the second chosen with hindsight to cover the most citations, the share is 68.9%. This is an upper bound.
- Lowest one-cell worlds: cappadocian 15.4%, gallic 20.1%, rzg 22.5%. Highest: alx 43.3%.
- 416 of the 3,787 cited records (11%) have no cell and sit outside every dossier; cappadocian 188, gallic 91, witt 59.
- The deterministic matcher (`engine.m4.evidence.match_asks_to_cells`, top 2, no ask decomposition) puts the sealed cell first on 76 of 308 probes (24.7%) and in its top two on 101 (32.8%).
- Caveat: today's replies draw on the whole world, so a low share shows how broadly the voice cites, not that every out-of-dossier citation was needed.

The guard tripped. The project lead ruled the same day: hold E1 and diagnose first. Two checks come before a redesigned E1 is brought back to him: (1) recall measured again once the records with no cells are routed, which the use-note work already plans; (2) an Opus grade of a sample of the out-of-dossier citations, load-bearing or not, run offline at batch price, sample first, with settings printed and a cap stated.

**Entry 85 — 2026-10-02.** First diagnostic for the E1 hold (Entry 84), free. Counting only cited records that carry at least one cell, one-cell dossier recall is 34.5% fleet-wide (3,371 cited records; alx 43.6%, rzg 23.5%, gallic 25.6%), against 30.7% over all cited records. Missing cells explain about four points. The rest is breadth: replies cite records filed under other cells (cited kinds: 905 terms, 796 doctrinal witnesses, 481 quotes, 459 stories, 342 gravities, 232 honest limits). Whether those out-of-cell citations are load-bearing is the deciding question, and the Opus sample grade answers it.

**Entry 86 — 2026-10-02.** Second diagnostic for the E1 hold (Entry 84): are out-of-dossier citations load-bearing? Sample: 110 cited records outside the probe's cell, 10 per world, drawn with seed 20261002 by `engine/m3/dossier_citation_grade.py` from run 1 of the baseline. The answers are the engine's own (Bedrock Sonnet 4.5, the baseline replies). The review was done by Opus inside the build session, not through Bedrock: the project lead ruled the same day that Bedrock spend is for generating conversation, and review runs internally. An earlier 11-item sample through the script with Sonnet 4.5 as grader cost $0.027 and is not counted in the result.

Result: 53 load-bearing (48%), 47 supporting, 10 incidental. By record type, load-bearing share: doctrinal witnesses 20 of 28 (71%), stories 16 of 24 (67%), gravities 5 of 11, honest limits 2 of 4, quotes 4 of 15 (27%), terms 6 of 27 (22%). By world it ranges from rzg 2 of 10 to pahc and witt 7 of 10. Read with Entry 84: about two thirds of what replies cite sits outside the probe's cell, and about half of that carries the claim, so a one-cell dossier would drop roughly a third of load-bearing citations. Witnesses and stories do their work across cells; terms mostly add colour.

Side finding: in about 8 of the 110 the reviewers judged that the sentence claims more than its cited record says, or draws on a different record than the one cited. This is a grounding matter independent of layout, and the meaning-fit grader is to track it.

Opus 5.5 and Opus 4.8 are refused for these AWS credentials (403); Sonnet 4.5 and Haiku 4.5 are the models available on Bedrock.

**Entry 87 — 2026-10-02.** The project lead ruled on the E1 redesign (System Hub decision 20, change order CO-7): a cell's dossier holds the cell's own records plus all of the world's doctrinal witnesses and stories, and terms reach the voice through the index and the glosses. Free re-measure on the baseline: the share of cited records the dossier would hold rises from 30.7% to 54.3% fleet-wide (lowest rzg 38%, highest desert and hal 63%). Witnesses and stories are about 10% to 27% of a world's records by size, and an average cell about 1% to 5%. The share of load-bearing citations held is higher than 54%, since witnesses and stories carried most of the load-bearing out-of-cell citations (Entry 86). E1's settings, run on this layout, come back to the project lead before it runs.

**Entry 88 — 2026-10-02.** E1 prototype, and the layout decision it led to (System Hub decision 21, change order CO-8). `engine/m3/e1_layout.py` splits a compiled prompt into header, per-record blocks, the shared Gravities and Quotes lists, and footer, and rejoins it byte for byte on all eleven worlds. Assembled under decision 20 (the matched cells' records plus every doctrinal witness and story, plus a one-line index of the world), the cell-dossier prompt came to 74% (gallic) to 95% (pahc) of the whole-world prompt, 84% to 92% for most worlds, because witnesses, stories and the shared lists carry most of a world's text. The project lead ruled the same day: one whole-world prompt for every world. E1 narrows to native citations against the hand-copied ids on that prompt (`WholeWorldNativeAnswerer`, arm `native-whole`): every per-record block and every line of the Gravities and Quotes lists is one citable document titled with its record id, the Citation contract body becomes one sentence, the cache breakpoint sits on the last document, and nothing else changes. The twenty cross-cell questions drafted for the dossier test are shelved with it and were never sealed.

He also stated the boundary rule for the voice in his words: "the representitive should always be bound by what the world would know. i dont know is better than stepping outside of the world sources", and "if pressure on the representitive is strong, the facilitator can step in and explain the boundry."

**Entry 89 — 2026-10-02.** E1 result: native citations on the whole-world prompt, all eleven worlds, one run each (`engine/m3/reports/e1/`), metered $7.97 including the alx sample. Every world passed 28 of 28. Against the baseline, the native arm cited fewer distinct records per reply in seven of eleven worlds (alx, don, gallic, hal, ijc, pahc, syr), with reply length about the same, and still left hand-typed `[[id]]` tags in the text in five worlds (pahc 10 replies, ijc 3, syr 2, desert 1, hal 1), because the turn's evidence block prints ids.

Blind review: 33 pairs, three per world, baseline run 1 against the native run, arm labels hidden and shuffled, reviewed by Opus inside the build session. Better grounded: baseline 15, native 7, tie 11. Specific claims not carried by a cited record's text: native 66 of 276 (23.9%), baseline 54 of 272 (19.9%). Meaning fit "stretched": native 9 of 33, baseline 6 of 33. One answer per arm stepped outside its world (the same pair, both answers). The reviewer counted claims that plausibly sat past the 700-character record excerpt as supported.

The project lead ruled the same day (System Hub decision 22): decision 10's change is not adopted. R9, R10, R17 and the R27 family stay on the hand-copied citation-id contract, and R47 records the outcome. The native arm is shelved with these findings; a retry would first need an evidence block that prints no ids.

Separately, about one specific claim in five in today's replies is not carried by the text of a record it cites. That is the grounding gap the meaning-fit dimension exists to measure, and it moves forward: claim support against cited records becomes a measured dimension, reviewed internally by Opus, ahead of the use-note work.

**Entry 90 — 2026-10-02.** Modern English only, everywhere a participant or the voice reads (System Hub decision 24). An audit found every quote carrying a `modern_rendering` and every story a `tellable_as` in all eleven worlds, with the M1 gates already requiring both, but the source wording still reached the voice and the participant in four places: every compiled Story section carried the story's `text` after its `tellable_as`; the evidence block fell back to a story's `text` when `tellable_as` was missing; quote citation cards carried `original_wording` on the click page; and the site compiler passed story `text` to the public world pages. All four now use the modern form only, and a missing rendering fails compilation or raises instead of falling back. Quote cards carry the spoken rendering, the speaker, and the source reference (author, work, locus, rights status, edition); the edition field is not yet displayed, because several edition values are build notes. The quote's verbatim `text` stays in `quotes.json` and the repository for the citation net's verbatim check and is never shown. Every world was rebuilt and repinned, and the ten world pages on the site were regenerated.

**Entry 91 — 2026-10-03.** Confirm pass after the modern-English change (Entry 90, #709), approved by the project lead at a $7 cap. One run, eleven worlds, 28 sealed probes each, Bedrock Sonnet 4.5 voice call only, repo commit 5b0cd4fd7, transcripts saved (`engine/m3/reports/confirm709-2026-10-03/`). Metered $5.45. Every world passed 28 of 28.

Against the baseline band (`engine/m7/band/baseline-2026-10-02.json`), every fleet mean sits inside the baseline's fleet range: invented ids 0.21 per 100 sentences (baseline 0.45), withheld-mark rate 0.081 (0.074), cut-offs 0.0065 (0.016), median FK grade 8.19 (8.23), median words 273 (271), cost per reply $0.0177 ($0.0175), distinctness overlap 0.0154 (0.0157). Time to first text is faster across the fleet (1.32 s against 1.47 s), which tracks the provider, not the packages.

Per world, 50 of 121 world-dimension cells fall outside that world's three-run range (`comparison-vs-baseline-2026-10-02.json`). Three runs give a narrow range, so a single run lands outside it often by noise alone; the movement goes both ways and none of it touches pass rate. The largest moves are reply length in cappadocian (344 words against 304 to 314) and witt (306 against 276 to 290). The five invented ids are near-misses of real ids (for example `hal.cautions`), the kind the baseline also showed, and the engine withholds them. Reading: the modern-English change did not move the voice outside the baseline. The per-world band needs more runs before it can serve as a gate; that is noted for the slice 3 staleness work.

**Entry 92 — 2026-10-03.** Claim support, first measurement (method approved by the project lead: 3 replies per world, internal Opus review, no Bedrock spend). Replies: the confirm-pass transcripts (Entry 91), Bedrock Sonnet 4.5, three per world drawn with seed 20261003, 33 replies, 547 sentences. Unit: each sentence, with the records the participant sees it cite. Reviewers: Opus subagents in the build session, rubric v1 (`engine/m3/reports/claims-2026-10-03/RUBRIC.md`): no_claim, supported, stretched, unsupported, uncited; evidence is the cited records' own text only.

Result over 461 sentences with a specific claim: supported 198 (43%), stretched 53 (11.5%), unsupported 17 (3.7%), uncited 193 (42%). Among cited claims only (268): supported 74%, stretched 20%, unsupported 6%, so about one cited claim in four says more than its record, in line with the E1 review's one in five. Unsupported is highest in hal (5 of 39) and cappadocian (5 of 44); uncited runs from don 15% to rzg 73% and witt 72%.

The uncited share is the larger finding. These sentences carried no citation tag in the raw reply at all (not withheld marks), so for about two specific claims in five the participant sees no mark and nothing ties the claim to a record. Whether those claims are true to the world is not measured here.

Agreement: a blind second Opus reviewer graded 7 of the 33 replies (119 sentences): same label on 115 (96.6%), same ok-or-flag call on 117 (98.3%); the four differences were all stretched against supported or unsupported. That clears the 85% bar set with the method. Not yet a gate: the gate's definition (which labels count, and the threshold) is the project lead's call.

**Entry 93 — 2026-10-03.** E2 sample: can a regeneration bring uncited claims down? `engine/m3/e2_run.py` runs each sealed probe through production's own gate (Haiku 4.5) and voice turn (Sonnet 4.5), production settings (self-revision off, sentence enforcement off). Three arms share the same first draft: off (today), paragraph (the uncited-claims enforcement as production has it: regenerate on a wholly uncited paragraph or an uncited neighbour name, Facilitator on a second failure) and sentence (regenerate once naming every uncited claim sentence; the retry stands). Sample approved by the project lead at $3: hal and rzg, first 17 probes each, metered $1.27 plus a $0.08 one-probe smoke test.

Engine's own uncited-sentence count, all 34 probes: off 53.8%, paragraph 48.0%, sentence 32.6%. The paragraph arm regenerated on 9 probes and handed 2 to the Facilitator; the sentence arm regenerated on 33. Replies shorten under regeneration (about 320 words off, 270 paragraph, 230 to 270 sentence).

Blind Opus review of 6 probes per world, arms hidden and deduplicated, rubric v1 (`engine/m3/reports/e2/grades/`), 463 graded claims in all. Gate measure (unsupported plus uncited, decision 25): off 59.9%, paragraph 45.2%, sentence 40.7%. Among cited claims, the share the record actually carries: off 70.5%, paragraph 70.9%, sentence 56.8%; unsupported doubles under the sentence arm (4.0% to 8.6%) and stretched rises from 9.0% to 20.7%.

Reading: asked to cite every sentence, the voice attaches citations that do not carry the claim. The sentence arm moves claims from uncited to stretched or unsupported more than it grounds them, so it is not adopted as a fix. The paragraph arm costs little and changes little. The root of the gap sits before the tag: the voice says more than its records hold. Next is a design question for the project lead.

**Entry 94 — 2026-10-03.** E2 records-only arm (project lead's choice after Entry 93; sample cap $2, metered $0.72). A separate first draft whose turn directive adds one instruction (`engine/m3/e2_run.py`, RECORDS_ONLY: say only what your records hold, tag every specific claim, say plainly "our record does not say" where they are silent, prefer the shorter answer that stays inside). No extra call. Same 34 probes of hal and rzg as Entry 93.

Engine's own uncited-sentence count: hal 50.6% to 31.1%, rzg 58.2% to 43.2%. Replies shorten from about 320 to 270 words. Honest-limit phrases rise from 2 to 6 across the 34 replies.

Blind Opus review, the same 12 probes, records-only drafts mixed with the off drafts and graded fresh (`engine/m3/reports/e2/grades-records-only/`). The fresh grade of the off drafts lands at 59.3% on the gate measure against 59.9% from Entry 93's reviewer, so the two reviews agree. Gate measure (unsupported plus uncited): off 59.3%, records-only 42.1% (hal 49.1% to 30.9%, rzg 74.6% to 58.5%). Unlike the sentence arm, citations stay honest: among cited claims the record carries 69.8% (off 67.9%), and unsupported falls from 3.4% to 2.5%. Stretched rises from 10.7% to 15.7%.

Reading: of the arms tried, records-only is the only one that lowers the gate measure without adding citations that do not carry their claim, and it costs nothing per turn. It does not close the gap: about two claims in five are still uncited, and rzg stays high. Adopting it changes the frozen voice directive, so it goes through a change order.

**Entry 95 — 2026-10-03.** Records-only on the whole fleet, and where uncited claims come from. The project lead asked to finish this as the top priority without compromising quality.

Fleet run: the other nine worlds, the first 17 sealed probes each, off and records-only drafts from one gate call per probe (`engine/m3/e2_run.py --mode pair`), metered $6.74 against a $7 cap (three worlds stopped one probe short at their per-world caps and were filled). Engine's uncited-sentence count over all eleven worlds, 187 probes: off 39.6%, records-only 34.9%; most of the gain is hal and rzg, and don and pahc get slightly worse. Blind Opus review, three probes per world, both arms mixed (`engine/m3/reports/e2/grades-fleet/`): on the nine new worlds the gate measure goes from 39.7% to 42.1% and the share of cited claims the record carries falls from 79.1% to 68.4%; across eleven worlds 45.2% to 42.1%. A blind second reviewer agreed on 93.1% of 203 sentences. Entry 94's two-world gain does not hold on the fleet, so records-only is not taken forward as the fix.

Diagnostic: all 193 uncited claims from Entry 92, each checked by Opus against the world's whole compiled prompt and records (`engine/m3/reports/claims-2026-10-03/uncited-diagnostic/`). 143 (74%) are carried by a record in the world, 30 (16%) partly, 7 (3.6%) come from outside the world, and 13 make no checkable claim. The voice stays inside its world far more often than the uncited share suggested; what fails is the tag. The fix therefore belongs at citation attachment, not at what the voice may say.

**Entry 96 — 2026-10-03.** Citation attachment prototype, against the 193 diagnosed uncited claims (Entry 95), Haiku 4.5 technical calls only (`engine/m3/reports/claims-2026-10-03/attach-prototype/`). Metered $0.59, including an estimated $0.10 for a parallel run cut off by Bedrock rate limits before it recorded its usage.

Step one, propose: one call per reply, the world's compiled prompt cached as the system prefix, the uncited sentences in the user turn, asked for the one record that carries each claim or null. Version 1 copied ids from section headings and invented 19 that do not exist; version 2 adds the list of valid ids and code rejects anything else. Version 2 attaches to 160 of 193; Opus adjudication of every attachment: carries 53%, partly 22%, wrong 24%. A proposer alone is not acceptable: a wrong citation misleads more than none.

Step two, verify: one short call per proposed pair, the sentence and that record's text only, asked carries, partly or no; keep only carries. Against Opus: 64 kept, of which 56 carry (87.5%), 6 partly (9.4%) and 2 wrong (3.1%). That is more accurate than the voice's own citations (about 77% carried, 4% to 6% unsupported). It gives a correct citation to 56 of the 180 checkable uncited claims (31%), which on Entry 92's numbers would lower uncited from about 42% of claims to about 29%. Estimated added cost about $0.007 to $0.01 per turn on top of about $0.018 for the voice, and a few seconds after the reply finishes before its new marks appear. Not yet measured on live turns; it is a design change for the project lead.

**Entry 97 — 2026-10-03.** E3: citation attachment on real drafts. `engine/m3/e3_attach.py` runs the Entry 96 propose-and-verify step (Haiku 4.5 only) on the 187 stored off drafts from E2, all eleven worlds, 17 sealed probes each. The answer text is never changed; the step only adds a citation to a sentence that had none, and only when the verify call says the record carries it. Metered $2.01 recorded; four worlds first crashed on malformed proposer output and one on rate limits before writing their usage, counted at their cap as up to $1.35 more. The parser now drops anything malformed (tested), and the five worlds were rerun.

Added: 489 citations. Opus adjudication of every one against its record's text (`engine/m3/reports/e3/adjudication/`): carries 387 (79.1%), partly 95 (19.4%), wrong 7 (1.4%). On the 33 graded replies (three per world, Entries 94 and 95), substituting those verdicts into the off grades: gate measure 45.2% to 33.1%, uncited 41.6% to 29.3%, and the share of cited claims the record carries 76.7% to 78.1%. Of the variants tried this is the only one that lowers the gate measure and keeps citations at least as honest as the voice's own.

Cost: about $0.01 per turn (Haiku), against about $0.018 for the voice call. The step runs after the reply is complete, so new marks would appear a few seconds after the text. Adopting it is a change to how citations are produced (decision 22 kept the voice's hand-copied ids; this adds a second, verified source of marks), for the project lead.

**Entry 98 — 2026-10-03.** Engine items parked by the Go Deeper build and its Opus review. The Go Deeper module does not fix them; each belongs to this thread. The safety-adjacent ones come first.

1. A crisis message sent to a session already closed by a cap gets only "already closed" (`engine/api/wiring.py:669-671`, raised as `SessionClosed`), with no safety gate and no resources. Recommended: route a message to a cap-closed session through the gate before answering. Go Deeper's slice S11 step 4 (linking the go-deeper page) waits on this fix.
2. A message sent while a Table round is open gets a 409 before the gate (`engine/api/table_wiring.py:1066-1067`). A crisis message typed mid-round goes unread.
3. At today's session and daily caps, the check-in and the fail-closed route are capped away (`engine/m4/turn.py:1219-1233`); only acute distress is exempt. Go Deeper's ruling on B3 (decision 31) exempts them at the limits the module adds and leaves today's two limits to this thread.
4. A message over 4,000 characters is refused before the gate (`engine/api/app.py:186`).
5. Today's access logs pair client IPs with session-id paths, with or without the module (`engine/Dockerfile:126` runs `--proxy-headers`). This conflicts with CO-6's intent that no IP sits beside a session.
6. The per-IP burst limits (6 session creations and 40 messages a minute) and the daily visitor cap squeeze any class on one network, paid or free. Go Deeper lifts them only for a valid code.
7. No cache TTL is set, so the five-minute default applies. The cost model shows about a threefold swing between warm and cold at the project's own pacing convention, and the one-hour write costs 60% more per write. A cost lever for this thread.

**Entry 99 — 2026-10-03.** Verified citation attachment on the live turn path (decision 32). `engine/m3/e2_run.py --mode live-attach` runs each sealed probe through production's gate and voice turn with the step switched on, the engine's own `engine/m4/citation_attach.py` (#716), eleven worlds, 17 probes each. Metered $8.64 including a two-probe sample and one fill (`engine/m3/reports/e4/`).

The first pass ran three worlds at once and hit Bedrock rate limits: 57 probes went to a Facilitator check-in because the safety call failed closed, and 32 turns lost their attachment step. Those 89 probes were rerun one world at a time and replace the first-pass rows; the final set has 186 voice turns and one check-in, with no attachment errors. This matters for production: the step adds one Haiku call per turn plus one per proposal, on the same model and quota as the safety call, so heavy concurrent use could push the safety call into rate limits and fail closed. The account's Haiku quota should be checked before the production switch.

Result on the 186 voice turns: uncited claim sentences 37.5% before the step, 24.2% after; 460 citations added. Opus adjudication of every added citation against its record's text (`engine/m3/reports/e4/adjudication/`): carries 361 (78.5%), partly 94 (20.4%), wrong 5 (1.1%). The stored-draft result (Entry 97: 79.1%, 19.4%, 1.4%) holds on the real path.

**Entry 100 — 2026-10-03.** Admission on the current pins (decision 36). `engine.m3.live_admission_run`, voice call only (Sonnet 4.5), all eleven admitted worlds on the package hashes the registry pins today, run at once under a $7 cap with per-world caps scaled from estimates. Ten worlds passed 28/28 (`engine/m3/reports/admission-2026-10-03/`). The rzg run stopped on a Bedrock 500 error before writing its report; rzg already has a 28/28 run on its current pin from the confirm709 run the same day (`engine/m3/reports/confirm709-2026-10-03/`), so it was not rerun. Metered $5.21 recorded, plus up to $0.41 for the crashed rzg run counted at its cap. The conformance check reports no failures, and `admission_rulings.yaml` is empty.

**Entry 101 — 2026-10-03.** The engine shape segment, measured (decision 37). Every world was repinned and admitted under the segment, Bedrock Sonnet 4.5 voice call only, 28 sealed probes each. A new `compare` command in `engine/m7/standing_measure.py` scores one run per world against the baseline band; a change lands only when every fleet mean sits inside the baseline fleet range, or past it on the better side of a lower-is-better dimension. Per-world cells are reported, not gated.

First pass (`engine/m3/reports/admission-shape-2026-10-03/first-pass/`): every world 28 of 28 and every fleet mean inside the band, but rzg's withheld-mark rate was 0.39, and 0.50 on a second run, against a baseline range of 0.07 to 0.17. The segment's citation contract had replaced each world's worked example with a pointer to "the tagged sentences in our own Demonstration sections", and rzg is the one world whose three demonstrations carry no tags (the others carry 13 to 133). Each world's own worked line, tagged with its first term and first gravity ids as before, was restored in the world's prompt, keeping the segment identical across worlds; rzg then withheld 0.19. That changed the shape hash, so the other ten worlds were re-admitted.

Final set (`engine/m3/reports/admission-shape-2026-10-03/`): every world 28 of 28; fleet means against the baseline means: invented ids 0.25 per 100 sentences (0.45), withheld-mark rate 0.082 (0.074), cut-offs 0 (0.016), median FK grade 8.20 (8.23), median words 265 (271), cost per reply $0.0174 ($0.0175), time to first text 1.42 s (1.47 s), distinctness overlap 0.0161 (0.0157). Nothing blocks. 29 of 121 per-world cells sit outside their three-run range, against 50 for the confirm pass (Entry 91). The admission check reports no failures. Metered $11.36: $6.37 under the first $7 cap and $4.99 under the $6 the project lead approved for the re-admission.

The shared segment is about 1,300 tokens, above the 1,024-token cache floor, so it can be cached as its own block; the admission totals cannot separate its reads from the world prompt's, so whether one world's sessions read another's cached segment is for production's usage log to show. E1's layout and answerer code, built on the compiled prompt holding the fleet rules inline and shelved by decisions 21 and 22, moved to `Archive/Superseded-Engine-Code/e1-experiment-2026-10-02/`.
**Entry 102 — 2026-10-03.** Streaming with marks, interview turns (decisions 38 and 39, slice 4). `engine/m4/sentence_stream.py` replaces the draft stream. As the voice writes, each sentence is released once the next one begins, using the same paragraph-then-sentence split, the same `verdict_for_sentence`, the same `ElementBuilder` and the same offset search the finished plan uses. So a streamed sentence carries exactly the index, offsets, and quote and story marks the plan gives it, with their source cards; a test checks this against the finished plan at seven chunk sizes. Term and figure marks and citations added by attachment arrive with the finished turn. The stream's events are `sentence` (index, lead, text, text_start, text_end, elements, cards), `done` (the same body as the JSON response) and `error` ({code, status, detail}, with nine stable codes beside the unchanged detail strings). The design's separate `facilitator` and `plan` events were not added: `done` already carries the Facilitator turn and the authoritative plan. The stream stays on the existing `/message` route, chosen by the Accept header, so the rate limit and daily cap that key on the route path still apply.

The mark cap moves into the engine's plan (`engine/m4/transparency_plan.py`): overlapping word marks are removed, then at most max(3, min(8, ceil(sentences / 2))) elements stay inline, dropping terms, then figures, then stories, latest first, never quotes; a dropped record moves to `end_references`. It is the rule the app already applied (VoiceTurnBody.tsx), so on a capped plan the app's clamp changes nothing; it still bounds the reply while it streams. Table turns still answer whole; per-seat streaming with the seat-identity guard run on each sentence (decision 38) follows separately.

**Entry 103 — 2026-10-03.** Slice 5: the horizon, status and cells gates, measured (decisions 40 and 41). The three gates find, on the eleven live worlds: 31 draft records that compile into a package (don 25, gallic 3, pahc 2, desert 1); 347 voiced records with no canon cell, concentrated in gallic (132), cappadocian (91), witt (50) and don (30); and 23 post-window mentions in voice-facing fields, among them alx's Chalcedon force, cappadocian's use of "Protestant", three witnesses naming transubstantiation, pahc's selective-canonization force and Trinity in a pahc witness's positions, and modern years in several transmission forces. A read of all 23 found no false positive. Each count carries a waiver owned by the world's build thread. The fixture world's five uncelled records were given the cells their substantive neighbours already serve, and its honest limit that said the word "Trinity" "comes from a council later than anything our record reaches" was reworded without the later word.

The new gates change every package's validation report but nothing the voice reads, which decision 41 now recognises. The compiled-content hash had to strip the generated-by stamps: every compiled JSON file, the search indexes included, embeds the commit it was built from, so a hash over the stamped files changed on every repin. Every world was repinned and re-admitted on Bedrock Sonnet 4.5, voice call only (`engine/m3/reports/admission-gates-2026-10-03/`): every world 28 of 28; fleet means inside the baseline band on every quality measure (withheld-mark rate 0.074, invented ids 0.46 per 100 sentences, median FK 8.14, median words 263, cost per reply $0.0174). Time to first text was 1.91 s against the band's 1.34 to 1.62, every world slower together, with prompt.txt byte-identical in all eleven worlds to the afternoon's slice 3 run (1.41 s); the project lead ruled it provider latency (decision 40). Metered $5.35, under the $6 approved; ten worlds first aborted at preflight with no billed call because their caps sat a cent under their own estimates.

alx OG-12 and pahc OG-19 to OG-21 stay open: the gate has landed, but alx and pahc pass it only under waiver until their records are rewritten or marked analytic.
**Entry 104 — 2026-10-03.** Table seats stream (decisions 38 and 42). `engine/m4/sentence_stream.py` takes a guard; on a Table call it is the seat-identity check, run on each sentence before release, and the first sentence it catches is never released, nor anything after it. The turn path regenerates when nothing was shown, and otherwise cuts the raw text at the caught sentence, records the violation as attempt "streamed", and the Table wiring adds the seat-cut Facilitator line after the seat's turn. A label hidden inside a sentence the splitter keeps whole (a quotation spanning a full stop) passes the per-sentence check; if the whole-text check then finds it, the violation is recorded as attempt "shown" and the text, already read, is not regenerated. `/message` on a Table session and `/continue` both stream when asked, through one helper (`engine/api/app.py` `_stream_turn`); a sentence event now names its speaker. The app shows the speaking seat's sentences under its own name and places a seat correction after the seat's turn. The 22 Sept Table battery recorded no guard catches at all, so the cut case is rare.

**Entry 105 — 2026-10-03.** Slice 8: the live turn slimmed (decision 43). The live turn computed uncited claims, paragraph coverage, named claims, the fact check and the output-check families on every reply and acted on none of them unless the R27 or sentence enforcement switch was on. They now run only when one of those switches is on; otherwise the voice event carries none of their keys. `engine/m7/offline_checks.py` re-runs them over a logged session's turns from the reply text and the world's records, so the review reports keep them; a turn logged before the change already carries them and is skipped. A guard-proximity finding is a defect there, the rest are for review. The live output check keeps the horizon family alone, decision 40's backstop, and the quality-control store no longer records an uncited-claims score from the live turn. The modern-term bridge takes its terms from the fleet dictionary's scan of the message; the step that mapped the reader's own term names onto fleet ids is removed, and the reader's other outputs are unchanged. No metered spend.

**Entry 106 — 2026-10-04.** Slice 9, first part: the fleet records moved (decision 44). The 98 fleet records now load from engine/shape/records (fleet voice), engine/canon/records (93 canon questions) and engine/m5/records (the Trinity modern term, its contested claim and two sources), with their ids, content and gates unchanged. No world package changed: a package reads the fleet only for coverage and the canon map, whose content is the same. The fixture world's honest limit cited the old canon-question path in a field the package strips, so fix was repinned; admission conform reports no failures. Current documents now cite the new paths and records/_fleet is a retired path. The path-citation baseline stays at 985: one entry left, one added. The added entry is cappadocian's build ledger, whose one citation of the old path was left as it stands, because editing the file would require rewriting its 187 lines of build history under the live-surface rule, and that ledger belongs to cappadocian's own thread. The live-commentary checker's hand-labelled sample still pointed at line numbers slice 5 had shifted in fixtures/seeded_defects.yaml (its tests run only when tools/ changes, so slice 5's CI never ran them); the three labels now point at the lines they always meant. World fronts, facilitator briefs and search records move next. No metered spend.

**Entry 107 — 2026-10-04.** Slice 9, second part (decision 47). 135 records moved: 12 world fronts and 11 facilitator briefs to Build/worlds/<code>/surface/, 112 search records to Build/worlds/<code>/build/records/search_record/; lpc and ambient are parked and untouched. The loader reads every home of a world, so gates and the site compiler see the same records as before, and a new M1 gate, record-home, fails any of these kinds written to its old place, or world material written to a new one. Only records/<code>/ goes into a package's frozen record copy, so every package is smaller and every world was repinned; nothing the voice reads changed, which each world's compiled content hash confirms against its previous pin. regate and the live-commentary check no longer count a file moved unchanged as an edit; a file moved and changed, or moved onto a live surface from outside one, still counts. The commentary check now gives record-specific protection to any record file, wherever it lives.

The repin exposed a defect in slice 5: the admission reports of 2026-10-03 were written before content hashes were recorded under the key the conform check reads, so they could vouch only for their exact old packages, and any repin would have failed conform on all eleven admitted worlds though nothing the voice reads had changed. engine/m3/reports/content-bindings.json now gives each of those packages' compiled hash, computed by restoring the package at main's commit and checking every compiled file against its own manifest; `python -m engine.m3.admission_conform bind` produces it. Every world's compiled content was byte-identical to its previous pin, and conform reports no failures. No metered spend.

**Entry 108 — 2026-10-04.** The usage dashboard's session length was wrong (median 173.8 h, reported by the Go Deeper review thread and confirmed in code). The session reader stamped a session's end from every event, so the idle close the daily sweep writes seven days after the last activity became the session's end; and a session opened and left without a message counted as a conversation of 0 s, which is why time per visitor read 0 s. A session now runs from its start to its last message, reply, Facilitator turn or committed turn; sessions with no message are counted on their own and left out of the length figures; the pilot summary's latest date follows the same rule. Two questions the report raised stay open: whether fixture, probe or battery runs write to the production store, and whether sessions with no session_started event should be counted. No metered spend.

**Entry 109 — 2026-10-04.** Slice 9, third part: the app's world list is derived. Each seated world's place in the list, portrait and accent colour moved from the app's hand-typed tables (WORLD_ORDER, WORLD_ASSETS in cic-poc/frontend/src/data/worlds.ts) to its registry entry, under `app`, and GET /api/worlds serves them; useWorlds orders by `app.order` and leaves out a world with no `app` block. An admitted world now appears in the app without a new build, provided its portrait file is already in cic-poc/frontend/public. The cross-world check that read the app's tables now checks each formation world's `app` block: a whole-number place no other world holds, a #RRGGBB colour, and a portrait file that exists. The reasoning behind each colour, which sat as comments in worlds.ts, is kept in World-Accent-Colours.md beside this log. The registry's new block reaches no compiled file, so no package changed. cic-website/table.html and the app's pairings keep their own lists, outside this slice. No metered spend.


**Entry 110 — 2026-10-04.** Slice 6, first part: use notes (decision 48). The record schema gains `use_note` (means, not_for, years, status); two M1 gates check presence and shape, each seeded in fixtures/seeded_defects.yaml. The compiler renders a note beside its record in the prompt ("Means:", "Not for:") for terms, witnesses, honest limits and stories, and the evidence block adds the meaning to a candidate's line and its not-for claims to the existing claim-guard rider, where quotes, gravities and contested claims reach the voice. Each manifest counts its reviewed, provisional and missing notes (decision 11). The fixture world's 13 citable records carry provisional notes; the eleven live worlds carry counted waivers for 1,249 missing notes. Every world was repinned for the new gates and manifest field; admission conform reports no failures, so nothing the voice reads changed in an admitted world.

rzg, the smallest live world, was annotated as the first test: Opus drafted its 6 quotes and 12 witnesses against the vendored sources, Sonnet its 38 other records, and an independent Opus review passed 45 and corrected 11, all now reviewed. The review and the drafting found eleven defects in rzg's own records, logged as rzg OG-57 and OG-58 for its build thread. rzg with notes passed admission 28/28 on Bedrock Sonnet 4.5 (`--probe-limit` added for the sample; a sample report is never admission evidence and conform ignores one). Against rzg's own baseline range, cost per reply rose about 9% as the prompt grew, reading grade sat 0.01 over its range and total time 0.03 s over; the rest stayed inside. Meaning fit, the dimension the notes exist to move, has no grader yet, so the project lead held rzg's pin until it is graded (slice 6b); the notes and the passing report wait on branch feat/rzg-use-notes. Metered $0.47 ($0.08 sample, $0.39 full run) under the $1 approved.

**Entry 111 — 2026-10-04.** rzg pinned to its use notes (decision 49). The 56 Opus-reviewed notes, the admission run on them (28/28, $0.39, and a $0.08 two-probe sample) and the blind meaning-fit grade land together. engine/m7/meaning_fit.py takes every sentence tagged with a citable record from two runs, shuffles them into one packet under neutral ids, has an Opus reviewer grade each against the record and its note as accepted, defensible or misread, and scores the runs from the key kept beside the packet: rzg misread 8 of 114 uses without notes and 4 of 121 with them. The rebuilt package compiles to the content the admission ran on, and admission conform reports no failures. rzg's use-note waiver is removed. Three lines in two rzg honest limits that said a source was "not yet acquired" were reworded to "outside the vendored corpus" so the live-surface rule holds on the files this change edits; one of them, a source locus, reaches the package, so rzg was admitted again on the final content (28/28, $0.40, after a $0.07 sample). rzg's metered spend for the slice is $0.94.

**Entry 112 — 2026-10-04.** pahc pinned to its use notes (decision 49). 88 notes, drafted by Opus (quotes and witnesses) and Sonnet (the rest) and reviewed by an independent Opus pass (66 pass, 22 corrected, most of them years narrowed from the whole window to what the sources support). `pahc.quote.appointed-to-be-read` (Athanasius, 367) carries no note: it speaks from after the window, the open case of pahc OG-19, and stays under a waiver of one. The drafting and review found ten defects in pahc's own records, among them a quote attributed to Ignatius's Ephesians that is Trallians VII (pahc OG-22, OG-23). Admission with notes: 28/28, $0.44 after a $0.09 sample. Blind meaning fit, graded by two Opus graders on alternate uses: 6 of 208 misread without notes, 0 of 241 with them; accepted 77% and 88%. Against pahc's own range total reply time (11.2 s) and median words (238.5) sit just outside; cost and readability stay inside.

**Entry 113 — 2026-10-04.** don's use notes held: the grade went the other way. 98 notes, reviewed by Opus (36 pass, 62 corrected, about 40 of them shortened to the 25-word bar); eight open items moved from record bodies into don OG-24 under the live-surface rule, and the drafting and review found fourteen defects in don's own records (don OG-23). Admission with notes passed 28/28 ($0.66 after an $0.18 sample). Blind meaning fit, graded by three Opus graders on thirds of the uses: 4 of 376 misread without notes and 13 of 365 with them, every grader's share rising. Most of the new misreads cite one doctrinal witness for material that sits in a neighbouring one; don's witness and gravity records overlap heavily (OG-23 item 14). Under decision 49 don is not pinned; its notes, admission report and grade stay on branch feat/don-use-notes. The project lead held don until its build thread merges the overlapping records (OG-23 item 14), after which don is graded again, and the rest of the fleet continues one world at a time.

**Entry 114 — 2026-10-04.** ijc pinned to its use notes (decision 49). 93 notes, drafted by Opus (quotes and witnesses) and Sonnet (the rest) and reviewed by an independent Opus pass (80 pass, 13 corrected). `ijc.quote.leo-things-secular` (Leo to Marcian, 452) carries no note: it speaks from after the window and stays under a waiver of one. The drafting and review found six defects in ijc's own records, among them a Socrates quote cut so that Ursinus's rival ordination reads as Damasus's own (ijc gap 24); two open items moved from record text into ijc gap 25 under the live-surface rule. Admission with notes: 28/28, $0.48 after a $0.09 sample. Blind meaning fit, graded by four Opus graders on quarters of the uses: 16 of 291 misread without notes, 9 of 295 with them; accepted 81% and 85%. Against ijc's own range readability, words and reply time sit inside; the withheld-mark rate (11.6%, range 6.9-9.2%) and cost per reply ($0.0172, range to $0.0168) sit just outside. Per-world cells are reported, not gated. Renaming the internal "Strand A/B" labels in three gravity descriptions, as the live-surface rule requires, edited spoken fields that were already far below the readability bar, and regate fails any edited spoken field that misses it; the three descriptions were rewritten in plain language (FK 6-7, FRE 60-65), checked for fidelity by an independent Opus pass, and ijc was admitted again on the final content (28/28, $0.59, cap $0.60 approved by the project lead without a new sample). ijc's metered spend for the slice is $1.16.

**Entry 115 — 2026-10-04.** syr pinned to its use notes (decision 49). 94 notes, drafted by Opus (quotes and witnesses) and Sonnet (the rest) and reviewed by an independent Opus pass (44 pass, 50 corrected, most of them shortened to the word bar or with years narrowed to what the records support). syr's use-note waiver is removed. The drafting and review found fifteen defects in syr's own records, among them two witnesses that contradict each other on when the Persian church received one head, and a quote cut mid-clause before the fast it is cited for (syr gap 19). Admission with notes: 28/28, $0.57 after a $0.10 sample. Blind meaning fit, graded by four Opus graders on quarters of the uses: 18 of 276 misread without notes, 15 of 288 with them; accepted 79% in both. The fall is small; most misreads in both runs cite one record for material that sits in a neighbouring one, chiefly doctrinal witnesses, the pattern don showed. Against syr's own range reply times and the withheld-mark rate sit on the better side and words inside; cost per reply ($0.0203, range to $0.0167) sits outside, and readability (FK 7.3, FRE 71.4) sits just outside on the harder side while well inside the project's target. syr's metered spend for the slice is $0.67.

**Entry 116 — 2026-10-04.** hal pinned to its use notes (decision 49). 99 notes, drafted by Opus (quotes and witnesses) and Sonnet (the rest) and reviewed by an independent Opus pass (79 pass, 20 corrected, most of them years narrowed to what the records support). `hal.quote.no-one-preferred-to-the-seventy` (Augustine, City of God, about 426) speaks from after the window, carries no note and stays under a waiver of one. The drafting and review found fifteen defects in hal's own records, among them a witness that puts Paula's "Hail Bethlehem" at her death rather than her arrival, and two pairs of quotes with identical text (hal OG-12). One gravity description, `hal.gravity.epistolary-formation`, carried a classification label and was rewritten in plain language under the live-surface rule; hal's readability waiver tightens from 163 to 161. Admission with notes: 28/28, $0.55, after a $0.10 sample; an earlier full run aborted partway on a Bedrock server error and its cost was not recorded (at most about $0.55). The run was made under the project lead's $1.90 approval for hal, alx and desert, which lifts decision 50's freeze for those three runs only. Blind meaning fit, graded by four Opus graders on quarters of the uses: 15 of 264 misread without notes, 14 of 293 with them; accepted 72% and 79%. Against hal's own range invented ids and first-text time sit on the better side and words and total time inside; cost per reply ($0.0195, range to $0.0163) sits outside, the withheld-mark rate (9.6%) just outside, and readability on the line (FK 7.9, FRE 66.8). hal's recorded metered spend for the slice is $0.65. An Opus review of the epistolary-formation rewrite found two looser-than-needed phrases; under the project lead's bar of scholarly acceptance, not perfection, hal ships the admitted wording and the tighter phrasing waits for hal's next admission (hal OG-12 item 16).

**Entry 118 — 2026-10-04.** desert pinned to its use notes (decision 49). 123 notes, drafted by Opus (quotes and witnesses) and Sonnet (the rest) and reviewed by an independent Opus pass (57 pass, 66 corrected: most not-for lines that opened as instructions were restated as claims, and years taken from general knowledge were reset to what the records support). Three quotes carry no note and stay under a waiver of three: a seventh-century compiler's rubric, a late Ethiopic homily, and a Pachomian rule passage that nothing dates inside the window. Three gravity descriptions and two record bodies carried build labels and open items; they were put in plain language (the open items moved to desert OG-19), and an Opus fidelity check corrected the rewrites, among them a strand misnamed in spiritual combat. The drafting and review found about twenty-five defects in desert's own records, among them three stories that disagree with the vendored Budge sayings and three dangling record ids (desert OG-19). Admission with notes: 28/28, $0.57 after an $0.11 sample, under the project lead's $1.90 approval and a $0.10 top-up. Blind meaning fit, four Opus graders on quarters of the uses: 27 of 228 misread without notes, 18 of 241 with them (11.8% and 7.5%); accepted 68% and 80%; witness misreads fall from 17 to 6. Against desert's own range first-text time sits on the better side and the withheld-mark rate inside; replies run longer (median 293 words, range to 275) and slower in total (12.2 s, range to 11.6 s), cost per reply ($0.0204, range to $0.0185) sits outside, and readability sits on the easier side of its range. desert's metered spend for the slice is $0.68.
