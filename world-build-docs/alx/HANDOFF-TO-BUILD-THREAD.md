# Alexandria → engineering build thread: handoff

**From:** the Alexandria world-build thread (branch `world/alexandria`)
**Date:** 2026-08-21 · **Authorized by:** Mark, in session ("lets hand it off to cic build")
**State at handoff:** per-world steps 1–5(a–d) complete (spec §4.3); **M1 gate battery 12/12 green, zero findings**, run through `engine/m1`'s own loader/gates against the real fleet canon; **M2 compile smoke-tested in memory: 185-file package, byte-identical across two runs** (manifest sha256 `157ecabc9a2a104d…` at records state `f6fc415`+this commit). Nothing under `engine/`, `canon/sealed_probes/`, or `records/_fleet/sealed_probes/` was modified or read (probes stayed sealed).

## What exists on this branch

- **137 records under `records/alx/`** — 20 sources (rights verified from each vendored file's own header), 15 search records (incl. 4 ruled absences), 10 figures (dates from directly-verified primary loci), 9 gravities / 18 forces / 5 contested claims (re-derived from the prior build's cleared analyses; anchors re-grepped), world_core (draft — see rulings), 14 verbatim quotes (every text machine-verified against the vendored file), 8 tiered stories (no Tier 5 anywhere), 13 terms (FK-gated), 13 doctrinal witnesses, 3 honest limits, voice_craft, 7 demonstrations (all three identity-collision canon questions covered, non-judgment line in-world).
- **Registry:** `alx` in `records/worlds.yaml`, `state: building`, representative **Theon / Catechetical Teacher**.
- **Working docs:** this folder (`world-build-docs/alx/`) — the source-request manifest (moved out of `records/alx/` so `_frozen_records_copy`'s rglob never sweeps a non-record into package hashes) and this handoff.
- **Vendored texts:** `cic/texts/` incl. the Philocalia (supplied 2026-08-21).

## Mark's rulings on record (with where each is written)

1. **Identity:** name Theon, role Catechetical Teacher (2026-08-21) → registry only; never in world records (spec principle 14).
2. **Voice/scope:** the Representative is a whole-window, whole-ecology composite (not a located individual), **strict we-voice** when representing the world; scope confirmed as *this world's* window, not all Christianity → verbatim ruling + interpretation note in `records/alx/voice_craft/alx.voice.craft.md`.
3. **Source gaps G1–G5 accepted as honest absences** ("not retreavable at this point… we need to move on", 2026-08-21) → on each search record + manifest §5; translate-from-Greek noted as future possibility for Stromateis III and Tura-Didymus.
4. **Living tradition:** flag set `true` carrying Mark's prior confirmation (2026-07-17, Coptic Orthodox primary heir); **re-confirmation under the new spec still pending** — flagged in the registry comment.

## What this thread asks of the build thread (in order)

1. **Fleet exemplar transcript** (versioned fleet artifact, spec §4.3.5) — the 7 demonstrations were written directly to the seven register statements and should be re-read against the exemplar when it exists.
2. **Step 5(e) voice validation + step 7 admission** — needs the M3 harness on a **live model (Bedrock)**; the mock won't grade readability/engagement or run fabrication pressure. Sealed probes are ready and untouched. Numeric bars from the fixture baseline per principle 10; Mark's register/admission read follows.
3. **Step 6 official compile** — `compile_world(world_key="alx", …)` works today (see smoke result above); the official run wants your package-id/records-commit conventions, determinism-twice in CI, and the staleness sweep picking `alx` up once `state` advances to `built`. State transitions are registry commits — this thread left `building` deliberately (the transition is your gates-plus-package call).
4. **`texts_registry.py` port** — the README generator lives only on `claude/table-voice-reset-nufsm4`; `cic/texts/README.md` was hand-edited for the Philocalia (flagged inline there). Worth porting before the next vendored text.
5. **`census_id`** — left `null`, never guessed; needs the Atlas `world-census.json` mapping.
6. **Env note:** `engine/m1` needs `jsonschema` (it's in `engine/m1/requirements.txt`; this container needed a pip install).

## Standing cautions your pipeline should keep visible

- **Out-of-horizon trap map**: the c. 399–553 Origenist-controversy material in npnf202/203/206/211/214 must never be cited for this world's voice — `Texts_Scrub_alexandria.md` has the loci; the manifest §0 carries the pointer; `alx.core.alexandria` cautions #4.
- **Eusebius HIGH-risk screen** (institutional/succession claims), **Rufinus transmission** on De Principiis (Philocalia is the Greek control — relation wired), **desert cross-build flags** (Vita Antonii, Lausiac History), **post-325 location** on the anti-Arian corpus.
- **Stratum bias is the world's central honest limit** (`alx.contested.ecology-wide-primacy`): Primary gravities are literate-attested only; the majority's interior is never narrated.

## Definition of done for this handoff

Build thread owns Alexandria from step 5(e) forward: exemplar, real-model validation, official compile + `built` transition, admission battery, then Mark's touchpoints (admission read, freeze, open). This thread remains available for record fixes any gate or audit finding routes back to (fixes re-enter at step 6, never live patches).
