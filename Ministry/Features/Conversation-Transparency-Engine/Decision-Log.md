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
merge, same as Entry 32's own precedent.)

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
discipline Entry 38 (PR #395) applied to Stage 6c. Mark's own number,
once set, is what the renderer fixture test (R17's other engineering
half) will assert against; that test is not yet written. PR #396.
