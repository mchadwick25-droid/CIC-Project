Simulated review — informational only, not an Article 31 substitute.

Round: 2
Reviewer model: Opus 5.5
Reviewer agent: independent subagent, fresh context, read-only, not the round 1 reviewer
Drafter model: Opus 5.5
Drafter agent: the session's own Opus thread
Truncation check, method 1: last line is "3. `engine.m9.cli check` did not finish while I was reviewing. I started it at the stated scope and it was still running when I wrote this. Its result is not part of this verdict."
Truncation check, method 2: 15 items judged (2 blocking + 10 non-blocking rechecks + readability + 2 new defects)

Verdict: FAIL. Both round-1 blocking items are CLEARED. One new blocking item: the edit trips the CI commentary gate.

Scope note: the fixes moved from the working tree into commit 36b657992 while I was reviewing. It touches the same 14 record files plus the new reviewfile test. I read the files as committed.

## Blocking items from round 1

**1. cappadocian.source.gregory-nyssa-on-the-holy-spirit: CLEARED (one leftover wording point, see new defect B).**
- `cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt:27918-27920` reads "On the Holy Spirit. / Against the Followers of Macedonius. [1221]", and the treatise follows. The new `edition` line number is correct.
- The Deity sermon is not in npnf205. A grep for "deity of the son" finds nothing. Grepping for money-changer and bath finds only Against Eunomius at :25424 ("bathing-attendants" naming words), which is not the complaint.
- A grep across `cic/texts/` for "deity of the son", "deitate filii" and "money-changer" finds only unrelated volumes (Suetonius, ANF/NPNF 1, 2, 5, 8, NPNF 1.1, 2.1, 2.2, 2.9). So "not ... elsewhere in the Library" holds.
- Its only citing record is story.money-changers-unbegotten. Its locus is "the money-changers/bath-attendants complaint, on the deity of the Son and Spirit", so `kind: unvendored` is justified as the record explains.
- `edition`, `citation`, `discovery_channel` and `work` now agree with each other and with the Library. The citation no longer names a volume that lacks the sermon.

**2. cappadocian.source.gregory-nyssa-life-of-gregory-thaumaturgus: CLEARED.**
- npnf205 only refers to the Life: at :1246 ("notably Gregory himself in the Life of Gregory Thaumaturgus") and in footnote [1017] at :21346. Its other Thaumaturgus hits (:475, :566, :30196) are also references, not the text.
- `citation` is now the bare work. `discovery_channel` no longer claims the Life is vendored.
- The seventeen-to-seventeen pointer is correct: `anf06_...xml:839-840` reads "only seventeen Christians in the whole city ... only seventeen pagans".

## Non-blocking fixes rechecked

3. figure.gregory-thaumaturgus and force.thaumaturgan-inheritance are now `named-not-rechecked`, a valid value (`engine/m1/schemas.py:43`). Their divergence notes are only re-wrapped; the text is the same. Sound.
4. dw.customs-from-the-apostles `positions[1]` now reads "Our teachers held that ...". This is attributed, not asserted. Sound.
5. force.gentry-household: "and made vows for her children" is gone. Sound.
6. gravity.martyrs-land: "the festival calendar". Sound.
7. force.eunomian-movement:
   - (a) "This world said he claimed to know God as God knows himself" is restored. It is framed as the world's own report, which is acceptable as hostile-report attribution. "trembling" is not restored. That is acceptable.
   - (b) "those who came over from other groups" now matches Basil Ep. 188 c.1.
   - Sound.
8. gravity.hesychia-summons now reads "every other pull in this world", and the scoring sentence is cut. gravity.renunciation-order has its two ranking sentences cut and ends cleanly. Sound.
9. dw.psalms-teach-the-singer `tensions[0]` and dw.not-a-death-wish `positions[0]` and `sources[0].locus`: the "honestly" and "named, not filled" wording is gone. A leftover "carried forward honestly" sits in that record's confidence note (line 19). That is etic metadata and was not touched, so it is not counted. Sound.
10. core.cappadocian `living_traditions` now reads "We do not judge them, or the filioque dispute ...". The contradiction is resolved. Sound.
11. voice.craft `identity`: the repeated "across its whole span" is cut. Sound.
12. The new test `test_a_full_reviewer_id_of_another_generation_is_still_rejected` is present. `pytest engine/m10/tests/test_reviewfile.py` passes 23 tests.

## Readability (engine.m1.gates.grade_text, on the field set from `_readability_checks`)

All 12 changed spoken or evidence fields pass (FK ≤ 10, FRE ≥ 60). One more changed field, dw.psalms `tensions[0]`, is 11 words, below the 12-word floor, so the gate skips it. Tensions are excluded by design anyway.

| Changed field | FK | FRE |
|---|---|---|
| customs positions[1] | 5.1 | 79.0 |
| not-a-death-wish positions[0] | 3.0 | 92.9 |
| not-a-death-wish locus | 3.1 | 96.0 |
| eunomian description | 6.9 | 66.7 |
| gentry description | 7.0 | 66.3 |
| hesychia description | 6.0 | 72.7 |
| martyrs-land description | 8.0 | 60.5 (thin margin) |
| renunciation description | 6.8 | 64.8 |
| voice.craft identity | 5.2 | 72.8 |
| living_traditions | 6.6 | 70.0 |
| Source discovery_channels | 6.3–6.8 | 73.8–74.1 |

Some fields in the same records fail but were not changed: thaumaturgan description, customs positions[0], psalms positions[0–1], voice.craft concerns[4], and core horizon, formation_logic, thinness and cautions. They predate this change. The source `edition` fields score FRE 49.5–54.0, but they are etic registry fields the gate does not grade.

## New defects

**A. BLOCKING: the CI commentary gate now fails.** Fix 3 edited force.thaumaturgan-inheritance. Its untouched `description` still carries build commentary:
- "(Doc_08 Cell 1B, Force 1B-1)"
- "WORLD'S OWN EXPERIENCE (Layer 2)"
- "FORMATION IMPACT (Layer 3)"
- "Doc_06 §4"
- "Doc_07 2F"

`python3 tools/check_live_commentary.py --base origin/main --enforce` exits 1. It reports 4 REWRITE lines at that file's lines 28, 29, 33 and 34. This is the step CI runs on a pull request (`.github/workflows/ci.yml:310`). Under the repo's rules, a PR that edits a live file also removes the commentary already in it.

Fix: rewrite that `description` as plain world prose, without build codes or layer labels. That rewrite should also bring it under the readability bar; it scores FK 15.8, FRE 35.6 today. Re-grade it afterwards.

**B. NON-BLOCKING: two source fields still describe the earlier state.**
- On the Holy Spirit, `rights_status`: "not yet acquired as an open text" is now half untrue, since the treatise is in npnf205 (public-domain NPNF). Fix: say the treatise is held in npnf205 and the sermon is not acquired.
- Life of Gregory Thaumaturgus, `discovery_channel`: "Earlier marked as held in cic/texts/npnf205, but ..." is change-history narration inside a canonical record. Fix: state the present fact only, e.g. "npnf205 only refers to it; not acquired". Put the history in Build/Ministry if it needs keeping.

**C. NOTE, not a defect in the records.**
1. The newest cappadocian package (`packages/cappadocian/2026-10-13T17-32-54Z/`) predates these edits. It still holds "Their authority came from the apostles", "made vows for her children" and "touches nearly every other gravity" in its records and in `compiled/repository.json`. It needs a rebuild and repin after A and B are fixed.
2. If the rebuild re-flows the waivers, recheck the counts (readability 203, shelf-row 52, emic-vendored-only 66).
3. `engine.m9.cli check` did not finish while I was reviewing. I started it at the stated scope and it was still running when I wrote this. Its result is not part of this verdict.