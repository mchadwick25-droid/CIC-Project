# "What the record holds" lines — draft and review — 2026-10-19

Step 3 of the conversation chooser build (`../Build-Plan.md`). One line per live world for the back of its card. Each is derived only from that world's `thinness_statement` in `records/worlds/<code>.yaml`. Drafted by Sonnet 5.5; reviewed by Opus 5.5 in two rounds (CLAUDE.md 2.2, 3.4).

## Status

Cleared round 2 review. **Not entered in `records/`.** The plan (Build-Plan step 3) holds a world's back text until the record fixes in `Build/Ministry/Operations/Audits/2026-10-19_live-reply-claim-check_eleven-worlds.md` are done and the text is re-checked against the records. None of those fixes is done yet. Until they are, each world's `card:` block carries no `record_holds`, and the card back shows no record line.

The Wittenberg wording was changed after round 2 (the one new finding, below). That one clause has not been re-reviewed.

## Final lines and scores

Scored with `engine.m1.gates.grade_text`, the scorer behind `engine/m7/turn_readability.py`. The ceilings are FK 10 and FRE 60; all eleven pass. No sentence runs past 25 words.

| World | Line | FK | FRE |
|---|---|---|---|
| Post-apostolic household churches (`pahc`) | Rich in letters, church order and worship. Thin on women's own words, enslaved members, the many who could not write, and any physical remains. | 6.8 | 67.8 |
| Alexandria (`alx`) | Rich in teaching, argument, and writing on how Christians grow in the faith. Thin on women's own words, ordinary believers and rural Egypt. | 7.4 | 62.7 |
| Syriac Edessa and Nisibis (`syr`) | Rich in hymns, teaching and the self-denying life of the covenant's vowed members, through Ephrem and Aphrahat. Thin on ordinary believers, women's own words and the years after Ephrem died. | 8.7 | 60.1 |
| Desert monasticism (`desert`) | Rich in the sayings of the elders and their disciples, and in Antony's Life. Thin on ordinary people the sayings never recorded, and on life inside the Pachomian houses after their founding. Only a few sayings come from women elders, called ammas. | 8.1 | 61.7 |
| Donatism (`don`) | Rich in its teaching on purity and its martyr stories. Almost all of it comes through its Catholic opponents. Thin on what ordinary believers felt. Two women appear, but only in hostile accounts. None of their own words survive. | 6.2 | 64.4 |
| Cappadocia (`cappadocian`) | Rich in the letters, sermons and treatises of Basil, Gregory of Nazianzus and Gregory of Nyssa. Thin on women's own words, which do not survive. Thin on ordinary believers, on those who did not speak Greek, and on the enslaved. The losing sides are known almost only through their enemies. | 7.5 | 63.9 |
| Imperial and juridical Christianity (`ijc`) | Rich in councils, canons, letters and the fight over who holds the last word in the church. Thin on ordinary believers' daily lives, on women's own words, and on the losing Homoian side's own voice. They held that the Son is like the Father. | 6.2 | 76.6 |
| Bethlehem circle (`hal`) | Rich in Jerome's letters and book prefaces, and in the remembered lives of the Roman women who backed his work. None of their own words survive. Thin on ordinary residents of the monasteries, and on daily life beyond one letter. | 8.2 | 60.1 |
| Gaul (`gallic`) | Rich in a saint's life written about one bishop, and in the Egyptian fathers' teaching as Cassian carried it west. Thin on daily customs on the island of Lérins and on women's own words, which do not survive. A later editor also removed material on sexual discipline from the one edition this record can read. | 9.4 | 61.0 |
| Wittenberg (`witt`) | Rich in Luther's own catechisms, treatises and statements of faith, and in the movement's account of its first decade, 1517 to 1531. Thin on households' and parishes' own reports of receiving that teaching. Records of the Saxon church inspections exist but are not in this library. No text by a woman survives here. Thin on the years after 1531. | 6.9 | 65.5 |
| Zurich and Geneva (`rzg`) | Rich in what the churches taught, from Calvin's Institutes to the Second Helvetic Confession. Thin on daily life. No account survives of what a Sunday service felt like. | 6.6 | 64.4 |

## Round 1 (Opus 5.5, full)

16 findings in 8 lines; `pahc`, `hal` and `rzg` had none. All were applied except where noted.

- **alx.** "What women wrote" narrowed "words" to writing; "what common believers said" narrowed "ordinary believers". Restored to "women's own words" and "ordinary believers".
- **syr.** "The covenant's life" read as God's covenant. Now "the self-denying life of the covenant's vowed members" (`syr.story.qyama-morning` supports "vowed").
- **desert.** "Ordinary monks" was narrower than the statement; "beyond its founding" was dropped; "few recorded sayings come from women elders" over-claimed. All three restored or reworded.
- **don.** "The church that opposed it" was overbroad. "Only one named woman appears" was unfaithful: `don.limit.womens-own-voice` says two women stand at the centre and neither one's own words survive. Now "Two women appear, but only in hostile accounts. None of their own words survive."
- **cappadocian.** Women's own words, not women as a subject; Greek speakers listed separately from ordinary believers; "almost only through their enemies" restored.
- **ijc.** "Own voice" restored. "Homoian" glossed as "the Son is like the Father" (`ijc.term.homoios` supports it).
- **gallic.** "A bishop's life story" hid that it is hagiography. Now "a saint's life written about one bishop".
- **witt.** "Own reports" and the caveat that the inspection records exist but are not in this library restored. "Confessions" changed to "statements of faith" so it is not read as admitting guilt.

Readability forced some wording to be plainer than the statements. Donatism's line no longer names Optatus and Augustine or rebaptism; Zurich and Geneva's no longer names Zwingli, the Consensus Tigurinus or the Consistory. Dropping detail is allowed; each dropped item is still in the world's own record.

## Round 2 (Opus 5.5, targeted recheck of the eight changed lines)

Every round 1 finding resolved. One new low-severity finding: **witt, "visitation records"** is a term a non-native adult reader may not work out. Reworded to "Records of the Saxon church inspections exist but are not in this library", using the census's own description of visitors sent "to inspect Saxon parishes". Not re-reviewed.

Two points the reviewer did not count, recorded here:
- **witt** drops the caveat that the 1525 tract against the peasants and the 1543 treatise against the Jews are real parts of the world's history but not available to quote. The line does not claim to be complete.
- **cappadocian** uses "sermons" for the statement's "orations".

## Open

- Each line goes into its world's `card.record_holds` once the world's audit fixes are done and the line is re-checked against the fixed records.
- The taglines and longer summaries are not part of this record. They stay under their own review.
