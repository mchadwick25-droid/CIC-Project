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
