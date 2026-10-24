# Live-reply record fixes: independent recheck, round 2, 2026-10-24

A targeted recheck of the seven blocking findings from round 1 (`2026-10-24_live-reply-record-fixes_Independent-Recheck_Round1.md`), plus two Syriac fields Mark added to the scope. The fixes are in PR 1102 (https://github.com/mchadwick25-droid/CIC-Project/pull/1102, head `cfc2da42`, merged as `5a73065c`). Only the changed lines were read, against the round-1 findings and the vendored lines they cite. This thread edited no record.

## Result

All seven blocking findings are cleared. Both added Syriac fields are confirmed. The five non-blocking changes are applied as asked.

| Finding | Record(s) and fix | Checked against | Verdict |
|---|---|---|---|
| B1 | `desert.demo.quiet-head`, `desert.dw.the-heart-and-the-spirit`: "Where they were written is not certain. Some place them in our own desert, others in the monasteries further east." | Mason's case for Egypt, `macarius_fifty-spiritual-homilies_mason1921.txt:566-572`; Contested rating in `desert.source.macarian-homilies` | Cleared. Both views are given and neither is settled. The long sentence is now split. |
| B2 | `alx.dw.jesus`: "in a book usually dated about 318" | `npnf204_athanasius-select-works-letters.xml:12090-12092` | Cleared. The 330s view is logged in alx Open_Gaps, not stated in the record. |
| B3 | `cappadocian.term.philoptochia` divergence_note: only Oration 14 held; Nyssa named, not held | `npnf205_gregory-nyssa-dogmatic-treatises.txt:1528` | Cleared |
| B4 | `cappadocian.quote.basil-against-eunomius-ant`: Contested, divergence_note citing the Nyssa parallel; `cappadocian.dw.want-to-believe` body hedged; `cappadocian.dw.doubt-and-unfinished-growth` names no author in a spoken field | `npnf208_basil-letters-select-works.xml:24124-24151`; `npnf205…:19688-19712` | Cleared. Keeping Basil as speaker is defensible now that the dispute is stated. |
| B5 | `syr.story.choirs-tradition` means: "only later memory, first in Jacob of Serug" | the record's own text; `npnf213…:11250-11254` | Cleared |
| B6 | `witt.quote.second-article-of-the-creed` body: prescribed for every household; uptake Contested | `luther_large-catechism_bente-dau1921.txt:240-242`; `witt.contested.household-catechism-reception` | Cleared |
| B7 | `ijc.story.tome-that-would-not-bend` telling: "Peter has spoken thus through Leo" | `npnf214_seven-ecumenical-councils.xml:20000` | Cleared. The quote now matches word for word. |
| Syriac 1 | `syr.core.syriac` thinness, rewritten in plain sentences | the round-1 Syriac sources; the six thin places match the old list, and the singing is now credited to later accounts | Confirmed |
| Syriac 2 | `syr.limit.f5-women-own-words` divergence_note and locus | vows and service in Aphrahat, Dem. VI (`npnf213…:25839-25845`, `:25929-25930`); singing only in later accounts (`:11250-11254`) | Confirmed. Documented now covers only what it should. |

Non-blocking changes from round 1, all applied: `desert.dw.jesus` positions (credited to Athanasius, Vita 41 and 47); `desert.core.desert` formation_logic (now Life 47's own words); `pahc.force.neronian-persecution` ("office of oversight"); `rzg.source.second-helvetic-confession` (Schaff's condensed translation named); `syr.story.qyama-morning` (the aside moved).

## One small note, not blocking

In `desert.dw.the-heart-and-the-spirit`, "We will not flatten it into his" now follows the sentence about where the homilies were written. So "it" no longer points back to "another current". Writing "We will not flatten this current into his" would fix it. It can go with any later edit to the record.

## Status

Round 2 of at most 3. B1 to B7 and the two Syriac fields are independently re-confirmed. The Open_Gaps entries that keep them open can record this recheck as passed. No round 3 is needed.
