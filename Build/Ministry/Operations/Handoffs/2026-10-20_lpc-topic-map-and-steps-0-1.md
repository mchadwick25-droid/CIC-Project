# Handoff — lpc topic map and Steps 0–1 for Augustine's complete works — 2026-10-20

From session: lpc source-research thread ("Run the Fable vs Opus 5.5 discovery test on lpc") · World or workstream: `lpc` · Branch / PR: `claude/lpc-augustine-sourcing-topic-map`

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Mark decided lpc's records are organized and extended against a topic map, built before new records | `Build/worlds/lpc/lpc_Decision_Log.md`, 2026-10-20 entry, item 1 |
| A proposed topic-map shape (six columns: topic, anchors, voices, where the sources answer, in the build now, gap; thirteen sample rows) | Private Artifact <https://claude.ai/artifact/SzZL2GvTyDWeES3WZ1YQs3>; sample loci come from the 2026-09-24 blind grading (OG-28) |
| Three gap entries from the 2026-09-24 blind test: 108 attested stories against 7 (OG-28); Doc_09 §7 item 5 narrower than stated (OG-29); the Cyprian *Acta* read (OG-30) | `Build/worlds/lpc/Open_Gaps_Tracking.md`; *Acta* line 41589 and Harnack lines 1686 and 1731 re-checked on `main` |

## 2. Not done

- **The full topic map.** It waits for Mark's approval of the shape. When built, it needs a discovery pass over the full lpc shelf and an independent review of every locus.
- **Step 0 and Doc_01 edges for Augustine's complete works.** Name the edges: his pre-clerical and Italian writings (the Milan books of the *Confessions*, the Cassiciacum dialogues) and the works the census also assigns to Pelagianism, Donatism, Manichaeism, the Hieronymian world or Ambrosian Milan. Both documents are approved to proceed, so any edit is a named change order. Cross-world edges go to Mark.
- **Doc_02 and `Source_Registry.md`** belong to the Library thread. See `2026-10-20_augustine-complete-works-library.md`.

## 3. Re-check before you trust it

- The 108-story list (OG-28) was built on a branch cut on 2026-09-24, before the Library sweep of 2026-09-29/30. Re-derive any item at source; sources vendored since were not searched.
- The topic-map Artifact's "in the build now" column cites Doc_09 story numbers. `records/lpc/` holds the same seven stories under `lpc.story.*` ids. Check each row against the records.
- The model-test report (<https://claude.ai/artifact/KpnAvk4CxV6V2Kgb4oyGnA>) is private and not durable; its scratch files are gone.

## 4. Waiting on Mark

- The topic-map shape (the Artifact above).
- Stop point 1 of the V2.0 re-baseline (`build/lpc_Build_State.yaml`, current step L0) — still open; this work does not resolve it.
- Re-tiering `lpcstory006` (OG-7, OG-30).

## 5. Next step

When Mark approves the shape, build the topic map from lpc's lexicon, gravities and forces, the records in `records/lpc/`, OG-28's list, and the full lpc shelf, including the sermons already vendored (Migne PL 38/39, Morin 1917 and 1930, Caillau 1842).

## 6. Spend

Allowance share used: see the companion Library handoff (same session). Metered: none.
