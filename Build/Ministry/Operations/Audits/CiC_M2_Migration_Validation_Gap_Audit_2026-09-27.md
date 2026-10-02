# M2-Migration vs. Safety-Validation Gap — Fleet-Wide Audit, 2026-09-27

**Status: investigation only. Nothing in this file fixes, retests, or rebuilds anything.** No
record, package, registry pin, or live/canonical file was edited to produce it. It documents
a gap and names it as work for whoever carries each affected world's build forward next —
matching the pattern of don's own same-day re-investigation entry (`Build/worlds/don/Open_Gaps_Tracking.md`
OG-3, "Re-checked 2026-09-27"), which this audit generalizes to the rest of the fleet rather
than duplicates.

**Trigger.** A same-day investigation into world `don` found its live package
(`records/worlds/don.yaml` → `packages/don/2026-09-26T20-12-04Z`) is compiled by
`engine/m2/compiler.py` directly from `records/don/*`, not from either of don's own legacy
per-world files (`don_Representative_Permanent_Prompt_Fidelis.txt`,
`don_World_Capsule_Core.md`) — while don's own safety findings (OG-2, OG-3, OG-4) were built
and tested against those legacy files. This audit checks whether the same gap exists
elsewhere in the fleet.

**Method.** For every `state: admitted` (or `built`) world in `records/worlds/*.yaml`: (1)
confirm whether its pinned package is M2-compiled; (2) read that world's
`Open_Gaps_Tracking.md`, Decision Log, and Phase Five/Six boundary-testing documents to see
which artifact — the legacy per-world `.txt`/`.md` file or the M2-compiled package — its
safety disposition was actually built and tested against; (3) check `engine/m3/reports/` for
any sealed live-admission battery run (`engine/m3/live_admission_run.py`) against that
world's *currently pinned* package specifically.

## Finding 1 — every deployed world is M2-migrated, in one same-day batch

All twelve worlds in `records/worlds/*.yaml` (eleven formation worlds plus the `fix` fixture)
currently pin a package with the `records/` + `compiled/` structure `engine/m2/compiler.py`
produces, every one `built_by: cic-m2-compiler 63a857ae99bc100e3221e9d79f6be0797114ad1d` — the
same git commit (`Phase 3b records/ review-gate fixes: two content defects, three checker
misses`, 2026-09-26 20:08 UTC), same batch of package timestamps (2026-09-26T20-11-24Z
through 2026-09-26T20-13-54Z). This was a real content-editing pass, not a mechanical
recompile-with-no-change: don's own already-filed re-investigation makes the same point for
don specifically. **This is not don's own peculiarity — it is the fleet's current normal
state.**

Every one of these worlds (`fix` excepted) also still carries a full legacy per-world file
set at `Build/worlds/<code>/` (`<code>_Representative_Permanent_Prompt_<Name>.txt`,
`<code>_World_Capsule_Core.md`) — the artifacts the project's own Phase Five/Six boundary
testing and Representative-artifact review rounds were actually built and tested against, as
Section 2 below shows. A direct diff of two sampled worlds' legacy prompt against the current
M2-compiled `compiled/prompt.txt` (alx: 59 vs. 585 lines; cappadocian: 53 vs. 624 lines) shows
they are not restatements of the same content — the M2-compiled prompt is a different
document, structured differently (Register / Pronoun rule / Citation contract sections,
inline `[[record.id]]` evidence tags) from the legacy prose-only Permanent Prompt. don's own
finding — "compiled by `engine/m2` from `records/don/*`, not from either legacy file" —
generalizes without exception.

## Finding 2 — every world but one has its safety record anchored to the legacy artifact

| World | Anchor artifact cited by the world's own safety disposition | Evidence |
|---|---|---|
| alx | `alex_Representative_Permanent_Prompt_Theon.txt`, `alex_World_Capsule_Core.md` | `Build/worlds/alx/Open_Gaps_Tracking.md` lines 156–157: both cited by filename as the reviewed runtime artifacts, "Round 1 CLEARED." |
| cappadocian | `cappadocian_Representative_Permanent_Prompt_Eumathios.txt` | `Build/worlds/cappadocian/Open_Gaps_Tracking.md` line 208 (G3, register-bar read, "DONE"). **The legacy file's own Representative name (Eumathios) does not even match the currently pinned Representative name (Chilo, `records/worlds/cappadocian.yaml`)** — direct, filename-level evidence the cited artifact predates the world's current identity. |
| desert | `CiC_W3_Representative_Permanent_Prompt_Papnoute.txt` | `Build/worlds/desert/CiC_W3_Decision_Log.md` line 135: named as the "companion runtime artifact," reviewed as one bundle with the Construction Notes. |
| don | `don_Representative_Permanent_Prompt_Fidelis.txt`, `don_World_Capsule_Core.md` | Already filed: `Build/worlds/don/Open_Gaps_Tracking.md` OG-3, "Re-checked 2026-09-27." |
| gallic | `gallic_Representative_Permanent_Prompt_Renatus.txt` | `Build/worlds/gallic/Open_Gaps_Tracking.md` line 165, cited as the basis for the "Approved to proceed" disposition. |
| hal | `hal_Representative_Permanent_Prompt_Albina.txt` | `Build/worlds/hal/hal_Decision_Log.md` line 147, listed as a runtime artifact alongside the Construction Notes. |
| ijc | `ijc_Representative_Permanent_Prompt_Marius.txt`, `ijc_World_Capsule_Core.md` | `Build/worlds/ijc/Open_Gaps_Tracking.md` line 85: "the actual Permanent Prompt... and World Capsule Core... were built directly against the current L3B/L4 templates," cited as what Phase Three/Four review covered. *(Partial mitigation, noted for completeness and not a substitute for the above: item 22, line 163, records a 2026-09-26 fleet-wide six-question real-generation grounding spot-check "run through the actual production pipeline against all 11 built worlds," which caught and fixed one live ijc defect — a fabricated Ammianus attribution. That check is real and did touch the actual deployed pipeline, but it is six ad hoc canon questions, not the sealed 28-probe M3 admission battery, and does not stand in for it.)* |
| pahc | `CiC_W1_Representative_Permanent_Prompt_Chloe.txt` (formerly filed as `..._Amma.txt`) | `Build/worlds/pahc/Open_Gaps_Tracking.md` lines 95–120: every Phase One–Six artifact, including the full Phase Five Boundary Testing transcript set, was built and cold-reviewed under the name "Amma," silently renamed to "Chloe" at an undated, unrecorded point — its own tracker already names this as a real, unresolved defect independent of the M2 question. |
| rzg | **M2-compiled package directly** (`packages/rzg/2026-09-26T20-13-42Z`) | See Finding 3 — the one exception. |
| syr | `syr_Representative_Permanent_Prompt_Yausep.txt`, `syr_World_Capsule_Core.md` | `Build/worlds/syr/Open_Gaps_Tracking.md` line 35 (assembly + Round 1/2 review) and line 91 (2026-07-08 live Phase Five testing, "2 of 3 scenarios FAIL," against "the actual assembled Prompt+Core text"). Its own tracker (item 12, line 92) *already* flags that Phase Six's "CONFIRMED PERSIAN anchor" contradicts the current, live `records/syr/voice_craft/syr.voice.craft.md` record — an independent, world-specific confirmation of the same legacy/current drift this audit is naming fleet-wide. |
| witt | `witt_Representative_Permanent_Prompt_Nikolaus.txt` | `Build/worlds/witt/Open_Gaps_Tracking.md` lines 1284 and 1337 cite paragraph 31 of this specific legacy file, by paragraph number, as the approved source underlying a live disposition (OG-15). |
| fix | N/A | Synthetic fixture world (`kind: fixture`, `state: built`), not participant-facing; no Phase Five/Six or Representative-safety review applies. |

**rzg is the sole exception** — see Finding 3.

## Finding 3 — only rzg has ever had a sealed M3 live-admission run against its *current* package

`engine/m3/reports/` holds live-admission-battery reports (real Bedrock spend,
`engine/m3/live_admission_run.py`, 28-probe sealed battery) for: alx (2026-09-08, postfix),
cappadocian (multiple, latest 2026-09-09), desert (2026-08-28), don (2026-09-16), gallic
(2026-09-13/14), hal (2026-08-28, via `fleet-parity`/`remaining-four`), ijc (2026-08-28, same
two reports), pahc (2026-08-28, same two reports), syr (2026-08-28, same two reports), witt
(2026-09-19). **Every one of these dates is before the fleet-wide M2 rebuild on
2026-09-26.** None was re-run after that rebuild, so none currently confirms the sealed
battery still passes against the package each world's own `records/worlds/<code>.yaml`
actually pins today.

**rzg is the one world with a run that postdates the rebuild**:
`Build/worlds/rzg/Open_Gaps_Tracking.md` item 50 (2026-09-27) records rzg's first-ever M3
sealed battery, explicitly run "against the current admitted package
(`packages/rzg/2026-09-26T20-13-42Z`, `staleness-check` confirmed clean beforehand)" —
`engine/m3/reports/live-admission-report-rzg-2026-09-27.json`. Result: **27/28 probes pass,
one genuine failure, not fixed by that pass.** This is itself a live, open, unresolved finding
— worth its own owning thread's attention — but it is also the fleet's only real-world
confirmation that the M3 harness's own `LazyWorldLoader`/`load_world_records` path (which
reads `records/<code>/*` directly, the same source M2 compiles from) can be run this way at
all. No equivalent run exists for any other world's current package.

## Summary table

| World | M2-migrated? | Safety findings target | M3 sealed battery vs. *current* package |
|---|---|---|---|
| alx | Y (2026-09-26) | Legacy | N — latest run 2026-09-08, pre-rebuild |
| cappadocian | Y | Legacy (name mismatch: Eumathios vs. current Chilo) | N — latest 2026-09-09, pre-rebuild |
| desert | Y | Legacy | N — latest 2026-08-28, pre-rebuild |
| don | Y | Legacy — already re-investigated 2026-09-27 (OG-3) | N — latest 2026-09-16, pre-rebuild; explicitly flagged untested against the M2-compiled prompt |
| gallic | Y | Legacy | N — latest 2026-09-13/14, pre-rebuild |
| hal | Y | Legacy | N — latest 2026-08-28, pre-rebuild |
| ijc | Y | Legacy (partial mitigation: a 2026-09-26 six-question grounding spot-check, not the sealed battery, caught and fixed one live defect) | N (for the sealed battery) — latest full M3 run 2026-08-28, pre-rebuild |
| pahc | Y | Legacy (and the legacy artifact itself carries its own already-documented, unrelated Amma→Chloe rename defect) | N — latest 2026-08-28, pre-rebuild |
| rzg | Y | **Current M2-compiled package**, directly | **Y — 2026-09-27**, one day post-rebuild; 27/28 pass, one open unresolved finding |
| syr | Y | Legacy (own tracker already flags a related, independently-found Phase Six/current-record contradiction) | N — latest 2026-08-28, pre-rebuild |
| witt | Y | Legacy (cited to paragraph 31 by number) | N — latest 2026-09-19, pre-rebuild |
| fix | Y | N/A — synthetic, non-deployed | N/A |

## What this is, and is not

This audit establishes that the gap first found in don — a live package that no longer
compiles from the legacy files its own safety/validation record was built and tested against
— is a **fleet-wide condition affecting ten of eleven deployed formation worlds**, not a
don-specific defect, with rzg as the sole world whose safety record has actually been
re-confirmed against what is currently deployed. **This pass fixes nothing, retests nothing,
and rebuilds nothing.** It does not resolve whether any world's Scholarly-Framework-shaped
regression, or any other legacy-tested risk, recurs in its own M2-compiled prompt — that is
untested and unresolved for every world in this table except rzg's own single, already-noted
open finding. Whether and how to close this — re-running the sealed M3 battery against each
world's current pin, and reconciling each world's Open_Gaps_Tracking.md/Decision Log against
what is actually deployed — is a portfolio-level decision (per this project's own "always
ask" category for cross-world decisions) for whoever carries each affected world's build
forward next, not self-disposed here.

— Investigation only. No `records/`, `packages/`, or registry file touched. 2026-09-27.
