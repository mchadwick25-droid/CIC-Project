# Recheck Round 2: cappadocian-nicene-pastoral-monastic-tradition

Targeted recheck of the four revised pieces against Review_Round1 findings. `diff <key>.v1.txt <key>.txt` shows only the sentences named in Revision_Round1; nothing else changed. No edits made.

| Piece | Verdict | Grade | Ease |
|---|---|---|---|
| story | PASS | 8.3 | 71.6 |
| legacy | PASS | 8.6 | 63.2 |
| doxology-stand | PASS | 7.4 | 74.7 |
| forty-sebaste | PASS | 7.4 | 77.1 |

Scorer: `python -m engine.m1.profile_readability`, 4 briefs, 0 failing. No quoted spans in any piece (sheets: none). No first person in any revised text.

## Corrections confirmed (PRE-EXISTING)

- **story** (Easter mob sentence deleted). Confirmed right. No record under `records/cappadocian/` holds a mob or attack at Easter. `records/cappadocian/source/cappadocian.source.gregory-nazianzus-de-vita-sua.md` line 45 says only "a liturgical attack -- Easter dating unconfirmed from the vendored corpus", in a source row, not a grounding record named in story.sheet.md. Deletion drops nothing the records hold for this telling. The remaining paragraph still ends cleanly on the Theological Orations.
- **legacy** ("in doubt, since many scholars now think it was written not by Basil but by his brother Gregory"). Confirmed. `records/cappadocian/contested_claim/cappadocian.contested.settlement-historiography.md` lines 57-59: Epistle 38 "attribution-contested between Basil and his brother Gregory of Nyssa - a substantial body of modern scholarship ... reassigns it to Nyssen". "Many scholars now think" matches "a substantial body of modern scholarship" without overstating it as settled. "His brother Gregory" is unambiguous here: Nazianzus was not Basil's brother.
- **doxology-stand** ("Some of his own allies wanted the plain word spoken, while other friends defended his restraint"). Confirmed. `records/cappadocian/gravity/cappadocian.gravity.precision-reserve.md` lines 50-51 ("Allies grew impatient and wanted the word ... a documented argument inside the winning side") and line 82; `records/cappadocian/story/cappadocian.story.doxology-stand.md` line 39 ("open argument among allies") and line 68 ("his own friends defended his restraint"). Motives stay unresolved, as the record requires.

## Own-wording / MINOR changes

- story: 33-word join split into two sentences; content identical, adds nothing.
- legacy: "or did they pursue three related projects"; fixes the referent, adds nothing.
- forty-sebaste: "As the churches of Basil's day remembered it". Supported: the grounding source is Basil's own homily on the Forty (`records/cappadocian/figure/cappadocian.figure.forty-of-sebaste.md` lines 14-17), and the passion details remain credited as tradition. Reads clearly once.

## Note for the record owner

The Easter attack can return only with a grounding record from De vita sua or Letter 77 checked in an edition (as Revision_Round1 says).
