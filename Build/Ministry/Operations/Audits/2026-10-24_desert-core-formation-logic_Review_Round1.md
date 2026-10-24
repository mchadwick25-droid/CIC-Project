# Review Round 1 — `desert.core.desert` formation_logic rewrite and body-note trim

- **Under review:** uncommitted change to `records/desert/world_core/desert.core.desert.md` (two hunks: (a) `formation_logic` rewritten into plain sentences, with "martyrdom's successor" scoped to Athanasius on Antony; (b) body-note sentence on caution (4) trimmed).
- **Date:** 2026-10-24
- **Reviewer:** independent Opus context (round 1, full review)
- **Method:** clause-by-clause comparison of old and new `formation_logic`; source check of the Life of Antony in the vendored `cic/texts/npnf204_athanasius-select-works-letters.xml` (Vita lines ~30986–33620; every "martyr" occurrence read in context); consistency read of `desert.force.martyrdom-unavailable` and `desert.dw.strangest`; check that the trimmed remark is logged at `Build/worlds/desert/Open_Gaps_Tracking.md` (OG-8, contested-claim routing bullet); `python -m engine.m10.cli regate desert --base origin/main`; proposed wording scored with `engine.m7.turn_readability.score_turn` on an in-memory copy (no record edited).

## Verdict

**PASS WITH FIXES.** One blocking finding (an unsupported strengthening). The rest are minor fidelity losses. The source scoping is correct. Regate passes on the change as it stands (`regate desert: PASS`; `formation_logic` FK 7.2, FRE 60.4). Hunk (b) is clean.

## Source check

- Athanasius ties Antony to martyrdom in Vita §46 ("he longed to suffer martyrdom"; "he prayed himself to be a martyr") and §47 ("daily a martyr to his conscience, and contending in the conflicts of faith").
- The only other "martyr" uses in the Vita are §79 (the martyr's contempt for death, as proof of the faith, in Antony's speech to philosophers) and §90 (burial customs for martyrs' bodies). Neither makes ascetic life a successor to martyrdom for anyone else.
- So "He makes that link for Antony alone" holds for the vendored text. §47 names conscience, not demons. Demonic combat as Antony's contest is Athanasius's own frame elsewhere (§§8–10 and on), so the demons clause is supportable only when scoped to Antony (F2).

## Findings

| # | Severity | Location | Finding | Exact replacement |
|---|---|---|---|---|
| F1 | BLOCKING | (a) "A formal curriculum plays no part." | Old text: meaning travels *chiefly* through the saying and apprenticeship *rather than* formal curriculum. New text makes this absolute. The claim is unsupported, and the cenobitic rule's own reading and Psalter learning make it misleading. | `Both count for more than any formal curriculum.` |
| F2 | MINOR | (a) "With the persecutor gone, the demons of the inner life became the total fight." | This follows "Athanasius presents…", so it reads as Athanasius's claim about the inner life in general. §47 says "conscience", and the source supports the demons point only for Antony. Scope it to him. | `With the persecutor gone, Antony's war with demons became the total fight.` |
| F3 | MINOR | (a) "named officers" | Old: "appointed offices". "Named" is ambiguous: it can mean officers who have names. It also loses "appointed", meaning set by authority, which is the contrast with earned authority. | `appointed officers` |
| F4 | MINOR | (a) "yet makes loose habits formal." | Old: "formalizes what that model leaves informal". "Habits" narrows the object to customs, but what the personal model leaves informal is authority and correction. "Loose habits" also adds a pejorative tone. | `yet makes formal what that model leaves loose.` |
| F5 | MINOR | (a) "This world never settles that tension in its time span." | Drops the old claim "the one tension", which singles this out as the ecology's single unresolved structural tension. | `It is the one tension this world never settles in its time span.` |
| F6 | MINOR (readability margin) | (a) last sentence | F2–F5 together drop FRE to 59.98. This shorter sentence restores the margin with no change in meaning. | `To read it as the whole movement's frame is only an inference.` |

**Accepted as faithful:** "can bear" for "can safely carry"; "wrong" for "actively wrong"; "close company" for "physical proximity"; "to fight idleness" for "as discipline against idleness in its own right" (the purpose is kept, and "in its own right" is only lightly weakened); dropping "invented" (now carried by "Athanasius presents"). Making the world-level frame "only an inference" is the intended scoping. It matches the sibling force record ("This record reads the link as wider, by inference") and `desert.dw.strangest` ("Athanasius reads Antony's life as martyrdom's successor").

**Hunk (b):** It removes the Doc_01 §11/Doc_05 §4 pointers and the "not an oversight" remark. These are process narration. The fact is preserved at OG-8 ("carried instead at its source record and Doc_01 §11/Doc_05 §4"). What remains is true. No finding.

## Readability of the proposed fixes

With F1–F6 applied together, `formation_logic` scores FK 7.28 and FRE 60.18, so it passes. The margin is thin. Apply all six together: F2–F5 without F6 score FRE 59.98, which fails. No AI tells were found. Sentences are short, in active voice, with one idea each.
