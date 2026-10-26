# C7 coverage map: baptism, communion, prayer, worship, confession

Read-only pass, 26 October 2026; nothing in the repo was edited. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; paths, line numbers and verification results are in `search/C7/C7-coverage.json`.

## The sub-questions

The 28 C7 questions plus R-32 and R-34 group into eight (ids from `repo/07-subquestions.yaml`):

| id | sub-question | question ids |
|---|---|---|
| S1 | Becoming one of them; baptism: infants, dunking or pouring | C7-01, 06, 15 |
| S2 | The meal: what happened, how often, real presence or symbol, who was refused | C7-03, 07, 09, 17, 23, 28 |
| S3 | Prayer: why and how, set or free, teach me, prayer in anxiety | C7-02, 18, 24, R-32, R-34 |
| S4 | Worship in the room: singing and instruments, buildings, images, posture, preaching | C7-08, 11, 14, 19, 20, 25, 26 |
| S5 | Confession and penance; fasting | C7-04, 10 |
| S6 | The calendar: Sunday or Sabbath, Easter, Christmas, Lent | C7-12, 13 |
| S7 | Mary and the saints; anointing the sick; weddings and funerals; the unbaptised visitor | C7-16, 21, 22, 27 |
| S8 | Did the practices go back to the apostles | C7-05 |

The earlier agent's saved runs use its own split (baptism, meal, prayer, gathering, music, confession, fasting, calendar, saints); the JSON maps them onto these ids.

## Layer table

R = RENDERED (a record speaks to it), R* = only an honest_limit or guard answers, L = LOADED (vendored, mapped, read in context, no record). Second letter is depth: F full, P partial, T thin, judged from reading the records.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R-P | R-P | R-T | R*-T | R-P | L-T | L-T | R-F |
| cappadocian | R-F | R-P | R-F | R-P | R-F | R-P | R-P | R-F |
| desert | R-P | R-P | R-F | R-F | R-P | R-P | R-T | R-F |
| don | R-F | R-P | L-T | R-P | R-P | R-P | R-T | R-F |
| gallic | R-P | R-P | R-F | R-P | R-F | R-T | R-P | R-F |
| hal | R-P | L-T | R-P | R-P | R-P | L-T | R-P | R-F |
| ijc | R-P | R-F | R*-T | R-F | R-P | R-T | R-P | R-F |
| lpc | R-F | R-T | R-F | R-P | R-F | L-T | R-P | R-F |
| pahc | R-F | R-F | R-P | R-F | R-P | R-P | R-P | R-F |
| rzg | R-P | R-F | L-T | R-P | R-P | L-T | R*-T | R-P |
| syr | R-F | L-T | R-P | R-F | R-F | R-P | R*-T | R-F |
| witt | R-F | R-F | R-F | R-P | R-F | L-T | R-P | R-F |

Of 96 cells, 86 have a record and 10 are LOADED; none is IDENTIFIED, OTHER or NOTHING as its top layer, because the vendored library is very large. Only 35 cells answer the main questions. S8 is full in 11 of 12 worlds; S6 and S7 are full in none. `lpc` records are all draft.

**Demonstrations by canon cell.** F4-I: 4 (don baptism-threshold; pahc becoming-one-of-us; witt the-way-in, all f4-i-01; lpc road-back-examined, f4-i-05). F4-T: 2 (don, hal, both born-again). F1-T: 5; only ijc and witt have the bread-and-cup one (f1-t-02); witt, gallic and rzg are f1-t-03 (faith, predestination). F3-I: 3 (gallic, syr, witt), all about authority. No world has a demonstration for prayer (f4-i-02), the meal (f4-i-03), fasting (f4-i-04) or "what happened when you gathered" (f3-i-02). alx, cappadocian and desert have none in any of the four cells.

**Flagged: tags with no question behind them.** The 35-word card list carries Hymns and music (cappadocian, ijc, syr, witt) and Feast days and remembering the dead (cappadocian, don); the only questions are C7-11 and C7-13, both PREDICTED. There is no Icons tag and no Confession tag at all ("Sin and forgiveness" is nearest); C7-14 and C7-10 are PREDICTED too, and no world renders icons. Feast-day support is thin: the don term refuses to call it a calendar, and no Christmas, Easter or Lent record exists anywhere.

Verification: 72 quote records are cited as RENDERED; all 72 MATCH their vendored file (62 exact, 3 spacing-only, 2 section number dropped, 1 hyphen). Four first read MISMATCH and were checked by hand: Basil on work and prayer (scan glyphs), Pachomius's angel tablet (`|113` page marker), the hyena passage (`[p. 687]`), Aphrahat's "warned before baptism" (`~1~` footnote marker). None is a wording change.

## World by world

**Alexandria (alx).** Can say: baptism is a real crossing after long teaching, the bread and cup are thanksgiving, the faith was an apostolic deposit with a gap (S8 full). Thin: infants and mode (`dw.original-sin` guards: "received as custom"), prayer (one definition), any room (`limit.material-remains` only). Library: Dionysius on who may approach the table and the Easter fast (anf06:9724, 9522), Anatolius's Paschal Canon, Origen on prayer (Greek), Mark's liturgy naming Mary (anf07:20549). Sarapion's prayer-book (OTHER) is the missing Egyptian witness.

**Cappadocians.** Best baptism and apostolic-origin cells: triple immersion, delay, infants honestly unknown, unwritten customs. The record admits it does not supply the meal. Basil's Letter 93 (npnf208:29930) answers C7-17, 12 and part of 16: he communicates four times a week (Sunday, Wednesday, Friday, Sabbath) and on saints' days. Nazianzen's Oration 38 on Christmas is vendored. `source.liturgy-of-st-basil` is registered unvendored though the Neale volume is mapped.

**Desert.** Best room picture among monks: silent synaxis, twelve psalms, no kneeling Saturday evening to Sunday evening or Easter to Pentecost. `limit.original-sin-eucharist-faith` honestly refuses babies and the bread. Fasting rests on the Pachomian tablet; the card tag traces only to `desert.core.desert`. Library: Cassian Conf. 2 on disclosing thoughts (npnf211:18790); Basil's Letter 93 says solitaries commune at home (not mapped here).

**Donatists.** Best on baptism (a "first baptism", two demonstrations; unbaptised catechumens present; infants unknown). Worship is only Deo laudes and martyr graves; no prayer, no fasting. The Latin Acta of Saturninus is vendored (PL 8, lines 1781, 2974: "we cannot live without the dominicum"), yet `don.source.acta-saturnini-abitinian-martyrs` says unvendored.

**Gallic monastics.** Strong on prayer (twelve psalms), penance and disclosure of thoughts, and Vincent's test of antiquity. Frequency of communion "rests on an editor's footnote". Unbaptised visitor: Cassian's dismissal of the catechumens (npnf211:24682). Calendar thin.

**Jerome's circle (hal).** Records cover baptism-as-rebirth, Fabiola's public penance and Paula's psalm-filled funeral. Missing: Letter 71 §6 on daily communion and the Sabbath fast (npnf206:16963) and Against Vigilantius on relics (22279). The "Saints and holy places" tag traces to `hal.dw.record`, not a saints record.

**Imperial-juridical (ijc).** Strong on the meal (Ambrose; refusing Theodosius), Milan's hymns, penance, custom. Hazard: `dw.original-sin-transmitted` is tagged to "did you baptise babies" yet is Leo on inherited sin, so that question retrieves nothing about infants. Prayer: a guard only.

**Latin pastoral (lpc, 330 draft records).** Full on baptism, prayer, the road back. No meal or calendar record, while Letter 54 to Januarius (npnf101:29897, 30000) gives the yearly solemnities as apostolic or conciliar custom and says some take it daily while others do not dare to.

**Post-apostolic (pahc).** Most complete: Didache baptism with the pouring fallback, thanksgiving over cup and bread, Justin's Sunday. Unrendered: the Lord's Prayer thrice daily, the Wednesday and Friday fast (anf07:12937) and the baptised-only rule (12970), the vendored answer to C7-27.

**Zurich and Geneva (rzg).** Infants and the Supper are strong. No record on prayer, calendar or the Sunday; the room is Inferential-Thin; saints are a guard. Second Helvetic Confession XXIV (feasts and fasts) and Institutes III.20 are mapped. Its only F1-T demonstration is predestination.

**Syriac (syr).** Strong on baptism as womb, hymns, the women's choirs (later tradition), confession as medicine. No meal record: Aphrahat VII.21 and Addai and Mari are mapped. The Nativity hymn is barred as a date. Weddings are an honest limit.

**Wittenberg (witt).** Fullest. Gaps: calendar (Large Catechism, third commandment, is mapped), anointing the sick (Luther's Works vol. 2, line 10116), order of service (none vendored).

## Other sources (outside the repo; from working knowledge, not fetched)

Sarapion's Euchologion (Wordsworth 1899) for alx; the Didascalia (Gibson 1903) and Aphrahat III and IV (Parisot, Syriac and Latin) for syr; Calvin's Form of Prayers 1542 (Beveridge 1849) for rzg; Luther's Taufbüchlein and German Mass (WA, German) for witt; Origen on infant baptism (Rufinus's Latin, PG 14) for alx; Tilley's Donatist Martyr Stories is in copyright (the Latin is vendored). Editions and licences are per cell in the JSON.

## Not checked

- No model calls, network, or `canon/sealed_probes/`. Canon-cell question numbers come from the saved notes, not a canon file.
- The tool scans whole mapped files, so some hits are editors' notes or other authors in shared volumes (marked per cell).
- The Greek, Latin and French files were counted, not read. OTHER sources were not fetched.
- Dunk-or-pour and instruments were searched; the vendored answers are Didache 7, Basil's triple immersion and Clement's flute at banquets, not worship.
