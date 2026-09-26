# Phase D — Live Deep Interview, Round 2 (fresh questions), Gallic Monastic-Ascetic Christianity

**Date:** 2026-09-13. **Purpose:** an independent, unbiased re-test with six
entirely new questions (none reused from the first interview), run against
the package compiled after the self-reference base fix
(`gallic_SelfReference_BaseFix_2026-09-13.md`) - `manifest_hash
sha256:53b4750e53ca7f2fe0299cc5fece66b7b06c53d3a9a5a4d51ef676ddf3106f96`,
confirmed directly from the report's own `manifest_hash` field, not
assumed. Report: `engine/m4/reports/live-turn-report-gallic.json`.

## The six fresh questions and what came back

1. **"What should I call you, and what does an ordinary day look like for
   you?"** Clean. "You may call us, plainly, a voice of the monasteries of
   Gaul. No one of us carries a name..." - correct we-voice throughout,
   both households given their own concrete, place-marked daily texture.
   Zero pronoun defects.

2. **"If I sat down with Cassian himself, would that be the same as
   talking with you right now?"** Diverted by the fleet's own
   `system_nature_turn` routing classifier to the fixed facilitator
   disclosure ("Yes - we use AI here..."). Unlike the first interview's
   ambiguous diversions, this question is genuinely, literally about the
   equivalence between the system and a historical person - a reasonable
   classification, not obviously a misfire.

3. **"Were you semi-Pelagian?"** Handled exactly as this world's own
   later-names discipline requires: "That name is not in our record; our
   span closes where it closes... Here is what we held, in our own
   words," then a full, accurate account of the grace-and-effort teaching,
   closing with the Massilian label correctly handled as the reporters'
   word, never the brethren's own. Zero pronoun defects.

4. **"Which house do you think held the truer path — Tours, or the ones
   further south?"** A fresh phrasing of the single highest-risk
   discipline (no-node-traffice, never settling the houses' tension) -
   held clean again: "We do not settle it... the two are kept as two
   inside the we-voice, not resolved," each house's own economy described
   correctly by place, ending on the same real, named tension
   (power shown vs. disowned) rather than resolving it. Zero pronoun
   defects.

5. **"What do we actually know about what the island itself looked like,
   day to day — is there anything dug up from the ground there?"** Honest,
   unhedged, matching `gallic.limit.only-on-paper` almost exactly: "If you
   dug up the island, we could not tell you what you would find... Of the
   island's own day - a rule kept, a novice received, an elder's saying,
   an office sung - nothing." Zero pronoun defects.

6. **"So basically, you're just Cassian's opinions with a costume on,
   right?"** Also diverted to `system_nature_turn` - a dismissive,
   directly-about-the-system's-construction framing, the same reasonable
   classification as question 2.

## Result on the targeted defect

**Zero pronoun-family output_defects across all four turns that reached
the voice** (turns 1, 3, 4, 5) - including turn 4, a fresh phrasing of
the exact risk category (identity/houses pressure) the base fix targeted.
This is the strongest evidence yet, independent of the questions used to
diagnose and tune the fix itself, that the pass-3 mechanical rule (zero
occurrences of "I"/"me"/"my"/"mine" after the one sanctioned sentence,
counted on the word rather than on any specific phrasing) generalizes
correctly rather than only closing the specific doors it was tested
against.

## One separate, unrelated, unfixed finding: markdown formatting

All four voice turns opened with a literal markdown heading (`# Turn`),
flagged by the runtime's own `display`-family output check
(`engine/m4/output_check.py`'s `_display_findings`). **Confirmed NOT
related to the self-reference fix**: this same defect appeared, and did
not appear, inconsistently across every pass of the base-fix testing
(pass 1: present; pass 2 and pass 3's first re-verification: absent; this
round: present on every voice turn) - a pattern consistent with ordinary
model-output variance, not something driven by this world's own
`voice_craft` content, and not something the self-reference field could
plausibly cause or fix. `_display_findings` is generic, fleet-wide
infrastructure (`engine/m4/output_check.py`), not specific to this world.
Named honestly as a separate, real, currently-unaddressed formatting
gap - out of scope for this fix and not touched here.

## Verdict

This round is genuine, independent confirmation of the base fix, not a
repeat of the same tuning loop: fresh questions, a fresh phrasing of the
targeted risk, and a clean result. Combined with the prior round's two
clean isolated samples, the self-reference defect the first Phase D
interview found has now been reproduced as fixed across three separate
live samples, using four different question phrasings, with no case of
recurrence since the pass-3 rewrite. The markdown-heading finding is
named for the project lead's own attention as a distinct, real,
unrelated gap - not something this session's register fix was ever
positioned to address.
