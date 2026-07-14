# Session Notes — 2026-07-13 backend/frontend upgrade pass

**Branch:** `claude/cic-poc-backend-facilitator-upgrade`
**Remote:** `origin` → `https://github.com/mchadwick25-droid/CIC-Project.git`
**Commits on this branch (on top of `main`):**
1. `Backend: representative voice discipline, facilitator governance, and orchestration fixes`
2. `Frontend: multi-world lexicon highlighting, scroll behavior, tile copy`

Scope of this branch is strictly `cic-poc/` (backend + frontend) and this notes file. Nothing under `World-Builds/`, `L1-Foundation/`, `L3B-World-Build-Methodology/`, `L3C-Representative-Methodology/`, or `L3D-Encounter-Methodology/` was touched, committed, or pushed from this thread, even though some of those files show as modified/untracked in the working tree (pre-existing, owned by the content-review thread).

---

## The single most important thing to know before testing

**The Acute-Distress/Harmful-Dynamic relational-safety mechanism (crisis-signal classifier, Track A/Track B, two-presence routing) is NOT implemented anywhere in `facilitator_prompts.py` or `nodes.py`.** Verified by direct search across the whole backend app directory - zero references to "acute," "distress," "harmful dynamic," "Track A," or "Track B." The only Section 12 trigger that got implementation tonight was the **frame-breaker** trigger (see below). Section 12's other four triggers (decontextualization/claim-laundering, acute distress, past capacity, harmful dynamic, sustained fidelity failure) remain governance-doc-only, not code.

---

## What changed, by bucket

### REPRESENTATIVE (voice, identity, individual formation)
File: `cic-poc/backend/app/prompts/representative_prompts.py`, plus world data files.

- Pronoun discipline ("we" for collective experience/history, "I" only for present-tense conversational stance) and the fabrication guardrail (no inventing a specific unattested scene, even under the correct pronoun) are now one correctly-ordered rule in `_HOW_YOU_ENGAGE`, rather than two rules where the weaker one (pronoun swap) was stated before the stronger override, letting a model apply the weaker fix first.
- Anti-enumeration/anti-menu restraint (no stacked "He is... He is..." lists, no "which door would you like opened" menu-close) lives in the "Formation Deepens Over Time" section; a duplicated statement of the same restraint elsewhere in the file was consolidated into one.
- "Avoid the Generic Register" section refuses the generic AI-hedge voice.
- **Amma → Chloe rename**: permanent prompt file renamed (`pahc_Representative_Permanent_Prompt_Amma.txt` → `..._Chloe.txt`), self-identification line updated ("Your name is Chloe"), all downstream references (config, facilitator info, frontend) updated to match. This should be consistent with the content-repo rename decision on `claude/vigilant-babbage-a04f38` (`World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Representative_Rename_Amma_to_Chloe_Decision_2026-07-13.md`) - **not independently cross-checked against that file's exact reasoning from this thread**, only that the same rename direction (Amma → Chloe) was applied here.

**Not done:** Mar Yausep's and Papnoute's permanent prompts/world capsules were not rewritten this session, only referenced/renamed-adjacent (Chloe). Any richer/"upgraded" construction-methodology content sitting in Archive or World-Builds tracks has not been pulled into the live `cic-poc/backend/data/*` files - that integration is still pending, separate work.

### FACILITATOR (governance, monitoring, threshold voice)
Files: `cic-poc/backend/app/prompts/facilitator_prompts.py`, monitoring/correction logic in `cic-poc/backend/app/graph/nodes.py`.

- Fixed a drift-signal whitelist bug: `over_producing`, `temporal_bleed`, `flattening` detections were silently relabeled "smoothing" because the whitelist array had gone out of sync with the prompt's actual signal list.
- Extended three signals: OVER_PRODUCING now covers answer *shape* (enumeration, menu-close), not just epistemic stance; FIRST_PERSON now catches present-perfect phrasing ("I have sat with..."); FABRICATION now covers the compound case (invented scene + claimed as personal witness).
- Deleted a block that duplicated representative-side correction wording inside the facilitator's own detector prompt - the detector's job is to classify, not re-teach correct speech; that belongs in `FACILITATOR_REROOT_PROMPT` or the representative prompt itself.
- Fixed a self-contradicting instruction in the monitor's closing paragraph ("be conservative" immediately followed by "but not too conservative").
- **New capability, not a fix:** frame-breaker classifier (`classify_frame_breaker`, `stream_frame_breaker_response`, two new prompts `FACILITATOR_FRAME_BREAKER_CLASSIFIER_PROMPT`/`FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT`). Implements the decoupled classify-then-route design from Governance V3.6 Section 10/12: a narrow Haiku call decides frame-breaker vs. substantive before any representative generation is invoked; genuine frame-breakers ("Are you an AI?", "Who made this?", "drop the act") get answered by the Facilitator alone in "surface, answer, recede" posture, and never reach a representative. Verified 12/12 on a mix of real frame-breakers and hard-but-legitimate adversarial questions that must NOT be intercepted.
- Drift correction routing fixed: monitoring now runs on every turn completed in a round (previously only the last speaker's turn was checked), and any correction routes through `pending_guidance[world_id]` - keyed to the specific representative who drifted - instead of a global `requires_reroot` flag that could leak a correction meant for one representative into a different one's next turn.
- Found and fixed a real bug while verifying the above: the monitor can return a compound label like "FABRICATION + FIRST_PERSON" (per the compound-case rule), and the whitelist parser was defaulting anything not an exact single-signal match to "smoothing" - silently hiding exactly the compound violation the prompt exists to catch. Fixed to search for known signal names within a compound label, preferring `fabrication` when present.
- Handoff introduction text (`get_facilitator_handoff_prompt`/`get_multi_world_handoff_prompt`) now sources each representative's short intro clause from `world_manifest.py`'s `representative_intro` field instead of a hardcoded dict - **text content is unchanged, only its location moved**. This is the piece most directly relevant to testing "the facilitator handoff upgrade."

### TABLE (orchestration, retrieval, plumbing, frontend)
Files: `cic-poc/backend/app/main.py`, `nodes.py`, `rag/batch_evaluate.py`/`retriever.py`/`story_retriever.py`, new `world_manifest.py`, new `table_discourse.py`, frontend components.

- Retrieval short-circuit: a world's own Tier-1 ("center of gravity") lexicon/story terms now retrieve deterministically when they rank among the closest semantic matches for the query, bypassing an LLM vote that was found (via three separate prompt-engineering attempts, all logged in code comments) to revert to literal keyword-matching once real conversation context was present.
- Governance moved off the participant-facing critical path: the `done` SSE event (which re-enables the participant's input) now fires as soon as a round's messages are committed, with dominance/convergence/drift monitoring continuing to run afterward in the background rather than blocking the participant - since that monitoring is post-hoc by design (it can only shape a *later* turn, never the one just streamed) there was no reason to make the participant wait for it. Guarded by its own try/except so a monitoring failure can't surface as a broken response.
- Selector call skipped when forced continuation (`must_continue=True`) leaves exactly one possible next speaker - previously a decorative LLM call that could only ever confirm the one candidate.
- Lexicon and story retrieval parallelized (previously sequential, doubling combined latency for no reason).
- **New `world_manifest.py`**: single source of truth for per-world/representative metadata (name, period, region, description, color, file paths, representative name/title/description/intro clause). Replaces three previously hand-synced copies: `config.py`'s `Settings.worlds`, `facilitator_prompts.py`'s `REPRESENTATIVE_INFO`, and `main.py`'s `AVAILABLE_WORLDS`. Frontend still has its own separate copies (`MessageBubble.tsx`'s `REPRESENTATIVE_INFO`, `types/conversation.ts`'s `SpeakerName` union) since TypeScript can't read the Python manifest at build time - those remain manual sync points, noted in the manifest's own docstring.
- **New `table_discourse.py`**: `reactive_turn_guidance` (rules for how any voice behaves when other voices are also at the table - naming what was said, disagreement shapes, keeping the participant addressed, refusing manufactured resolution) promoted out of an inline `nodes.py` string literal into its own versioned, reviewable file. Now also its own Anthropic prompt-caching breakpoint (previously it rode in the uncached dynamic prompt segment despite being byte-identical on every reactive turn).
- World tile copy rewritten (`main.py`'s `AVAILABLE_WORLDS` entries, now sourced from the manifest): dates/places restored into the description prose (not just the separate period/region badges), gender de-emphasized in Chloe's description, all three representative descriptions reframed as "is a voice of [the world], speaking as a [role]" rather than reading like individual biography, and each world's description now closes naming real documented influencers (Ignatius/Polycarp/Justin Martyr/Hermas; Ephrem/Aphrahat/Jacob of Nisibis; Antony/Amma Sarah/Pachomius) - checked against the live lexicon/story corpus for each world rather than assumed.
- Frontend: multi-world lexicon highlighting merge, first-occurrence-only highlighting (fixed a real React StrictMode bug in an earlier version), and a scroll-behavior fix (`.messages-container` is now a real height-capped internal scroll region via `table.css`, paired with a plain React `onScroll` handler in `TheTable.tsx` that only keeps the view pinned to the live edge while the participant is already there). **The scroll fix is not yet confirmed working by live testing** - an earlier attempt at the same fix had a confirmed-broken listener-attachment bug; the current version is simpler (no custom ref/effect timing) but hasn't had a clean live confirmation yet.

---

## New files (not present before this session, now committed)
- `cic-poc/backend/app/world_manifest.py`
- `cic-poc/backend/app/prompts/table_discourse.py`
- `cic-poc/backend/app/rag/batch_evaluate.py`, `story_retriever.py`, `story_indexer.py`, `source_registry.py`
- `cic-poc/backend/data/desert_world/` (full world data directory)
- `cic-poc/backend/data/pahc_world/pahc_Representative_Permanent_Prompt_Chloe.txt`, `source_registry.json`, `story_chunks/`
- `cic-poc/backend/data/syriac_world/source_registry.json`, `story_chunks/`
- `cic-poc/backend/scripts/extract_source_registries.py`, `index_stories.py`

## Modified files
See the two commits on this branch for the exact file list; broadly: `config.py`, `main.py`, `graph/nodes.py`, `graph/state.py`, `prompts/__init__.py`, `prompts/facilitator_prompts.py`, `prompts/representative_prompts.py`, `rag/__init__.py`, `rag/indexer.py`, `rag/retriever.py`, syriac world lexicon chunks + permanent prompt, and the frontend files listed in the frontend commit message.
