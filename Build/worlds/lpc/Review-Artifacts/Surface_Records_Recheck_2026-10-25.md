# lpc Surface Records Recheck, Round 2, 2026-10-25

**Scope.** This is a targeted recheck of commit 47a71f2f (`git diff b09d3df7 47a71f2f -- Build/worlds/lpc/surface`) against findings F1–F13 in `Surface_Records_Review_2026-10-25.md`. Only the changed text was checked. Every new claim and every new `grounded_in` ID was read against its record.

**Reviewer.** Opus 5.5, independent. No model API was called.

**Mechanical checks.**

- Both files still parse.
- Every new `grounded_in` ID resolves to a record.
- The rebuilt site JSON in the same commit carries the new text.
- Every changed field scores between FK 5.0 and 8.2, with Reading Ease 60.6 or higher. None is outside the band.

## Findings

| ID | Round-1 sev | Status | Note |
|---|---|---|---|
| F1 | P1 | **Fixed in the text. New issue in the grounding (R2-1).** | The new sentence is supported. "Nine old sermons, printed in a scholarly edition in 1917, may date from those years. They have not yet been assessed in building this world" matches `lpc.limit.the-silent-century`: nine tractatus in Morin 1917, at `cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt`, "not yet assessed". It also matches the world_core horizon: "Nine sermons in Morin's 1917 edition may come from those years." Calling the tractatus "sermons" follows world_core's own wording and the edition's title, "Tractatus sive Sermones". The front does not name Optatus, and it does not need to. The added `grounded_in` ID is the wrong record, though. See R2-1. |
| F2 | P1 | Fixed | world_identity now says "This build reads its core conviction as…" and "this build's synthesis, rated Inferential-Thin". That matches `lpc.witness.answerability-as-ground` and world_core's divergence_note. |
| F3 | P1 | Fixed | The siege is gone. "The Pelagian view of grace … reached ordinary believers as teaching" is supported by world_core formation_logic ("Pelagian teaching about human nature produces thirteen works … reaches the ordinary believer … as a sermon, as teaching") and by `lpc.force.manichaeism-and-pelagian-anthropology` ("A bishop had to answer them from the pulpit"). Both records are now in `grounded_in`. |
| F4 | P1 | Fixed | The Numidicus retrieval note is now limited to grief below the Facilitator's threshold. The caution adds that "Acute distress or trauma is the Facilitator's turn, and Datus is not called." That is consistent with cautions[1] and CLAUDE.md. |
| F5 | P2 | Fixed | The caution now says "The redirect and its resources follow the fleet template". The world-specific point is limited to the Facilitator's own words around the template. The no-conditional rule is kept. The status line is gone. This sets no new policy. |
| F6 | P2 | Fixed (cut) | The "bishop leaving them" caution and the referral prohibition are both removed. No ungrounded claim is left. redirect_notes still bars filling the silence from the Donatist record, which world_core caution 2 supports. |
| F7 | P2 | Fixed | The teaser now says Lucian "grants it to the two women by name". That matches `lpc.story.celerinus-writes-to-lucian`. |
| F8 | P2 | Fixed | "one pastoral letter" and "take those rites for granted and do not describe them on their own terms" match the world_core thinness text and thin_topics. |
| F9 | P2 | Fixed | "The Western church rejected Cyprian's rebaptism, though it honours him." This matches `lpc.force.transmission-institutionally-dominant-side`. |
| F10 | P2 | Fixed | "Four disputes are held as Contested, beside the Contested silence noted above." |
| F11 | P2 | Fixed | `lpc.limit.ordinary-interior-life`, which carries Milan, has been added to both units. |
| F12 | P2 | Fixed | All four phrases are rewritten as proposed. The meaning is preserved and nothing was added. |
| F13 | P2 | Fixed | "keeps more of its own words than most" is supported by, and weaker than, world_core: "the largest and most direct base of primary sources of any world we have built so far". "this record does not invent one" and the untested-status line are gone. |

## New findings

| ID | Sev | File:field | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| R2-1 | P1 | front: `orientation.story[8].grounded_in` | The F1 fix added `lpc.source.morin-sermones-post-maurinos-reperti` as grounding. That record is a **different Morin edition**: *Sermones post Maurinos reperti*, Miscellanea Agostiniana vol. 1, Rome 1930. It is in copyright, never vendored, rated citation_specificity D and `named-not-rechecked`. It says nothing about the nine tractatus or about 1917. The sentence's real grounding is the 1917 *Sermones Guelferbytani* edition, cited inside `lpc.limit.the-silent-century`. No lpc source record for that edition exists; it appears only in corpus-map rows 1536 and 2615. As it stands, the unit cites a record that does not support it, and the compiled JSON exports that wrong citation. | `records/lpc/source/lpc.source.morin-sermones-post-maurinos-reperti.md` (work, edition, divergence_note). `lpc.limit.the-silent-century` why_sources_cannot_answer. `cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt` title page (1917, "accedunt SS. Optati Milevit[ani]…"). | Remove `lpc.source.morin-sermones-post-maurinos-reperti` from this unit's `grounded_in`, then rebuild the JSON. `lpc.limit.the-silent-century` already grounds the sentence in full, including "1917" and "nine". If a source record for the 1917 edition is wanted, that belongs to the records thread, not this file. |

## Verdict

**Revise.** All thirteen round-1 findings are fixed. One new P1, R2-1, comes from the F1 fix: the added source ID points to the 1930 Morin edition, not the 1917 one. The fix is to delete one ID and rebuild the JSON. After that, a one-line recheck of that unit is enough to reach Approved to proceed.
