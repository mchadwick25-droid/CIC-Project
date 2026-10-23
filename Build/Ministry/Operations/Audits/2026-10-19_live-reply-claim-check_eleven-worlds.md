# Live-reply claim check, eleven worlds — 2026-10-19

Round 1 of an Opus claim check of the recorded 13 October live-turn replies (`engine/m4/reports/live-turn-report-<code>-2026-10-13-eleven-world-test.json`, six replies per world). Each reply was split into claims and each claim checked against that world's records under `records/<code>/` and, where it mattered, the vendored texts in `cic/texts/`. Read only; no model calls; nothing in `records/` was changed.

Status: findings from reviewers, not yet independently re-confirmed (CLAUDE.md 4.4). The replies are from 13 October and may not reflect later record or engine changes. Classes: A tradition's own voice; B outsider's report voiced as the tradition's own; C outsider's report marked as such; D unsupported or contradicted; U unverified.

## Totals

| World | A | B | C | D | U |
|---|---|---|---|---|---|
| Alexandria | 26 | 3 | 0 | 5 | 0 |
| Cappadocia | 35 | 2 | 0 | 4 | 3 |
| Desert | 13 | 20 | 0 | 6 | 2 |
| Donatism | 24 | 11 | 2 | 10 | 2 |
| Gaul | 33 | 0 | 5 | 9 | 2 |
| Bethlehem circle (hal) | 43 | 1 | 1 | 8 | 0 |
| Roman empire (ijc) | 35 | 1 | 0 | 4 | 0 |
| Household churches (pahc) | 38 | 0 | 2 | 8 | 0 |
| Syriac | 28 | 4 | 1 | 7 | 2 |
| Zurich and Geneva (rzg) | 37 | 0 | 0 | 4 | 2 |
| Wittenberg | 34 | 2 | 0 | 4 | 0 |

## Cross-world patterns

1. Every world has unsupported claims (4 to 10 each).
2. Many errors start in the records: a confident summary line written by the builders and stored as the tradition's own voice.
3. Contested or Inferential-Thin material is repeatedly stated as plain fact.
4. Desert: Athanasius's Life of Antony is tagged `register: emic` but is a bishop's account; nearly all of the Representative's Jesus content rests on it.
5. In Alexandria and Cappadocia, sentences marked `verdict: withhold` in the reply's grounding were shipped in the final text. Not investigated; to be checked as an engine question.
6. Some source records say `kind: vendored` for texts that are not in the vendored files (Cappadocia), or carry `sources: []` while marked `verified-direct` (rzg).

## Records to fix, by world (reviewer findings)

### Donatism (see also the 19 Oct entry on the card line)
- `don.dw.who-jesus-was-among-us` line 78 and a story record repeat "279 ... stood for three days" with no locus; the acts show the larger body had been sent out and seven per side pleaded.
- `don.dw.the-creed-we-shared` line 60: "in the same Latin words" is unsupported; the same record rests the shared creed on Augustine, Letter 185.
- `don.demo.death-wish` line 34 and `don.dw.not-a-death-wish` line 61: "the account spends its whole length" contradicts the Passio Marculi's own "a few things must be said".
- `don.contested.maximianist-reception` conflicts with `don.dw.becoming-one-of-us` on whether a Donatist justification survives.
- `don.dw.becoming-one-of-us` cites Augustine, On Baptism I.5.6; the passage is V.5.6.
- `don.core.donatism` around line 87 says "calls itself the Church of the Martyrs"; `don.term.church-of-the-martyrs` says the phrase is a modern summary, not a quoted title.

### Desert
- `desert.dw.god` line 31 ("our ordinary way of holding it was refusal"): one figure in Athanasius, generalised.
- `desert.dw.jesus`: Athanasius's narrative voiced as "we argued, we told".
- `desert.dw.the-heart-and-the-spirit` line 28 ("we carried"): no record shows desert monks carried these homilies in the window.
- `desert.dw.strangest` line 34: "did not return to his father's house"; the Vita says "outside his house".
- `desert.force.martyrdom-unavailable`: rated Documented; its own note says no source states the equivalence.

### Gaul
- `gallic.force.army-and-rank-before` lines 85 to 86 ("a man who changes service does not leave the service; he can be posted"): the builders' argument in the world's voice.
- `gallic.dw.christ-in-the-beggar-and-the-guest` lines 76 to 79 ("only one man's private word survives").
- `gallic.dw.the-christ-who-bears-the-wounds` lines 19, 77, 99: the hours-of-prayer teaching said to come from Egypt; Cassian, Institutes III.2 to III.3 says the Egyptians keep no separate day hours and the reasoning is Cassian's own.

### Bethlehem circle
- `hal.dw.suffering` lines 48 and 56 ("grief honored, never condemned as unbelief"): contradicted by Jerome, Letter 39 ("unbelieving tears").
- `hal.core.hieronymian` lines 44 to 45 and `hal.voice.craft` line 25: fasting comparison with no source.
- `hal.dw.record` line 29 ("the Hebrew we held truest") conflicts with the Hebraica-veritas term record.
- `hal.limit.f5-women-own-words` line 28 states Epistle 46 authorship as settled.

### Roman empire
- `ijc.dw.jesus` lines 33 to 34: unsourced line about what the Son gives.
- `ijc.story.tome-that-would-not-bend` lines 56, 68, 73: "settled who Christ is" contradicts `ijc.force.chalcedon-failed-consensus`; line 68 also puts the Tome and Canon 28 in the same session, against the record's own rule.

### Household churches
- `pahc.quote.the-memoirs-of-the-apostles-are-read` line 32: "he does not call them that"; Justin, 1 Apology 66, says "which are called Gospels".
- `pahc.story.quintus-recantation` lines 35, 38, 57: "names a different man first" is false; Polycarp and Germanicus precede Quintus.
- `pahc.witness.god-and-argument` lines 56 to 57 ("our real fight was who should lead") conflicts with `pahc.force.boundary-drawing` line 29.
- `pahc.force.neronian-persecution` lines 38 to 43: unsourced "world's own experience" prose retrieved as emic.

### Syriac
- `syr.story.choirs-tradition` line 42, `syr.gravity.covenant-life` line 51, `syr.limit.f5-women-own-words` line 24: women's choirs "in every church" and "what our own years attest" with no in-window source.
- `syr.core.syriac` line 40: "in verse rather than treatise" needs scoping to Ephrem; Aphrahat wrote prose.
- `syr.term.ihidaya`: the deliberate double sense is a modern scholars' reading, not the world's own speech.

### Zurich and Geneva
- `rzg.contested.anabaptist-schism-legitimacy` lines 44 to 45 misdescribes Zwingli's 1527 Refutation (it records the drowning decree).
- `rzg.limit.marburg-bolsec-perrinist-narrative` line 39: "found no mention of Bolsec" is false; Calvin's vendored letters discuss him.
- `rzg.witness.triple-refusal` line 18 and `rzg.limit.hagiography-refused` line 18: attribute the image polemic to Article XVIII; it is in Second Helvetic Confession ch. IV.
- `rzg.term.providence` line 42: Zwingli's providence treatise (over 100 pages) is not acknowledged.
- Two force records carry `sources: []` while marked `verified-direct`.

### Wittenberg
- `witt.term.sacrament-of-the-altar` line 90 and `witt.dw.born-in-sin-fed-at-the-table` line 53 ("we did not dispute the how"): contradicted by Luther's 1520 iron-and-fire argument.
- `witt.dw.born-in-sin-fed-at-the-table` lines 56 to 57 ("no other teaching appears in so many of our writings"): a project word-list statistic stated as history.
- `witt.quote.second-article-of-the-creed` lines 18 and 120: household uptake stated as fact against `witt.contested.household-catechism-reception` (Contested).
- `witt.story.brussels-martyrs`: the 1523 date comes from editors, not the hymn.

### Alexandria
- `alx.dw.jesus` lines 32 to 33: "Athanasius closes the era with the same conviction" misleads on chronology (De Incarnatione dates to about 318).
- `alx.figure.gregory-thaumaturgus` line 27 conflicts with `alx.source.gregory-address-to-origen` line 17 on whether the Address's authorship is doubted.

### Cappadocia
- `cappadocian.force.movement-institutionalized` line 33 ("the young no longer remembered"): no source.
- `cappadocian.source.gregory-nyssa-love-of-the-poor-lepers-consolation` lines 20 to 23: says vendored in npnf205; the homilies are not in that file.
- `cappadocian.source.basil-against-eunomius`: line 32 "no open edition acquired" contradicts line 39 "kind: vendored".
- `cappadocian.term.epektasis` lines 21 to 22: only source is "unacquired text", yet rated Widely Accepted.

## Notes

Reply-level errors that start in the model's wording rather than a record are not listed here; they bear on the voice prompt and the grounding check. The Donatism entry above also stands as an open gap for `Build/worlds/don/Open_Gaps_Tracking.md`.
