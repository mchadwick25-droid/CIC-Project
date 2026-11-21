# Recheck, round 2: syriac-edessa-nisibis

Targeted recheck of the six revisions in `Revision_Round1.md`. Each `<key>.v1.txt` was diffed against `<key>.txt`; in every piece the only changed sentences are the ones listed, and each new sentence is the reviewer's wording exactly.

| Piece | Verdict | Grade | Ease (names out) |
|---|---|---|---|
| story | PASS | 9.1 | 67.1 |
| legacy | PASS | 9.2 | 61.2 |
| abgar-addai-legend | PASS | 8.1 | 80.3 |
| edessa-flood-201 | PASS | 6.2 | 79.4 |
| ephrem-famine-death | PASS | 6.9 | 79.8 |

`python -m engine.m1.profile_readability` on the five revised files: 0 failing. The two under grade 8 were split sentences, not flattened; both still read with their full detail.

## PRE-EXISTING correction (story)

New: "Later accounts say that women of the covenant sang Ephrem's hymns in choirs."

Confirmed against:
- records/syr/term/syr.term.qyama.md, line 61: "later accounts say the daughters of the covenant were the choirs that ..."
- records/syr/term/syr.term.madrasha.md, line 48: "performed by choirs (later accounts name the daughters of the covenant)".
- records/syr/gravity/syr.gravity.covenant-life.md, line 51: "later accounts report the performance".
- records/syr/world_core/syr.core.syriac.md, line 38 (formation_logic) and line 40 (caution 9): "That choirs of the daughters of the covenant sang his hymns rests on later accounts."

The wording neither overstates (it does not say Ephrem led the choirs, which qyama lines 38, 75, 83 and covenant-life line 57 exclude) nor drops the witness. Correct.

## Other changes

- legacy: "after 410" matches the Story's close (the synod of 410). Adds nothing; clear heard once.
- abgar-addai-legend: "offered to share ... with him" restores the original's claim. Opening line now stands alone, third person. Clear.
- edessa-flood-201: 33-word join split back at the original boundary. Clear.
- ephrem-famine-death: 46-word join split; the longest sentence is now 24 words. Clear.

## Quotes and voice

All quoted spans unchanged character for character (none sits in a changed sentence). First person appears only inside quotes ("my brothers, I picked up"; "Then trust me ... I appoint myself").

## Edits made by the rechecker

None.
