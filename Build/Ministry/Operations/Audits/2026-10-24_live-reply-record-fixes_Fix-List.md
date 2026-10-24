# Live-reply claim check: fix list for independent recheck, 2026-10-24

This lists every record fix made for the 19 October claim check (`2026-10-19_live-reply-claim-check_eleven-worlds.md`), with the vendored source each fix rests on. It is the input for a separate Opus recheck thread. None of these findings is cleared until that recheck confirms it (CLAUDE.md: a blocking finding needs independent re-confirmation).

PR: https://github.com/mchadwick25-droid/CIC-Project/pull/1094 (branch `claude/exciting-bardeen-sr4a1i`).

Reviews already done inside the fixing session (Opus subagents with separate contexts, not the drafter):
- `2026-10-23_live-reply-record-fixes_Review_Round1.md` (PASS WITH FIXES, 9 blocking, resolved)
- `2026-10-23_live-reply-record-fixes_Review_Round2.md` (PASS WITH FIXES, 1 blocking, resolved)
- `2026-10-24_desert-core-formation-logic_Review_Round1.md` (PASS WITH FIXES, 1 blocking, resolved)

Source line numbers are in the vendored files under `cic/texts/` as of 2026-10-23.

## Already fixed before this PR (no change made; recheck that they still hold)

| World | Finding | Where it now stands |
|---|---|---|
| don | "279 … stood for three days" | `don.dw.who-jesus-was-among-us`; Collatio, `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt:134887-134889` |
| don | "spends its whole length" | `don.demo.death-wish`, `don.dw.not-a-death-wish`; Passio Marculi, `monumenta-vetera-donatistarum_migne-pl8.txt:896-897` |
| don | On Baptism I.5.6 | now V.5.6; `npnf104_augustine-anti-manichaean-anti-donatist.xml:12744` |
| don | "calls itself the Church of the Martyrs" | `don.core.donatism` now frames it as a modern summary |
| desert | "our ordinary way … was refusal" | `desert.dw.god`; Life of Antony 68, `npnf204_athanasius-select-works-letters.xml:32915-32919` |
| desert | "did not return to his father's house" | `desert.dw.strangest`; `npnf204…:31272`, `:31286-31287` |
| gallic | hours of prayer "from Egypt" | `gallic.dw.the-christ-who-bears-the-wounds`; Cassian Inst. III.2-3, `npnf211_sulpitius-severus-vincent-lerins-cassian.xml:17802-17804`, `:17848-17849` |

## Fixed in this PR

### Donatism
1. `don.dw.the-creed-we-shared`: "There was no doctrinal difference to point at" → the creed was not what the two churches fought over. Source: Augustine, Letter 185, `npnf104…:19321` ("if some even of them have said that the Son was inferior to the Father…").
2. `don.dw.becoming-one-of-us` (tensions) and `don.contested.maximianist-reception`: Cresconius's reason reaches us only through Augustine's answer; the quoted words are marked as the NPNF editor's summary of Contra Cresconium III. Source: `npnf104…:10353`; Latin, `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt:47029-47033`.

### Desert
3. `desert.demo.quiet-head`: "homilies we carried" → Greek homilies from the eastern monasteries, not from our own desert. Source: `macarius_fifty-spiritual-homilies_mason1921.txt:554-555`.
4. `desert.dw.jesus`: collective "we" generalisations credited to Antony as Athanasius reports him. Sources: Life 80, `npnf204…:33169-33170`; Life 47, `npnf204…:32399-32400` ("daily a martyr to his conscience, and contending in the conflicts of faith").
5. `desert.force.martyrdom-unavailable` (description), `desert.dw.strangest`, `desert.core.desert` (`formation_logic`, full plain-sentence rewrite): the martyrdom-successor link is scoped to Athanasius on Antony; the wider reading is marked as inference. Source: Life 46-47, `npnf204…:32399`.

### Gaul
6. `gallic.force.renunciation-that-stays`, `gallic.force.office-temptation-destiny`: "posted" sentences removed. Source: Cassian Inst. XI.18, `npnf211…:24728-24729`.
7. `gallic.dw.christ-in-the-beggar-and-the-guest`, `gallic.dw.one-person-two-substances` (loci): "the one private word that survives" → "in our record". Source: Sulpicius Ep. III, `npnf211…:2429-2430`.
8. `gallic.dw.christ-in-the-beggar-and-the-guest`: build narration "Cassian wrote books on the Incarnation, but our record has not read them" removed (text and positions).
9. `gallic.limit.only-on-paper` (locus): Institutes I-IV are the customs of Egypt and the East. Source: `npnf211…:17802-17804`, `:17848-17849`.

### Alexandria
10. `alx.dw.jesus`: "Athanasius closes the era" → writing about 318, still a young man; use_note endpoint framing removed; date added to `alx.source.athanasius-de-incarnatione`. Source: `npnf204…:12090-12092` ("in or shortly before 318 A.D.").
11. `alx.figure.gregory-thaumaturgus`, `alx.source.gregory-address-to-origen`: both now say Nautin disputed the Address's authorship and date, rated Contested. No consensus claim either way (none checkable in vendored texts).

### Cappadocia
12. `cappadocian.force.movement-institutionalized`: unsourced "The young no longer remembered…" deleted.
13. Love-of-the-poor homilies are not in `npnf205_gregory-nyssa-dogmatic-treatises.txt` (only a prolegomena mention at :1528-1529). New `cappadocian.source.gregory-nyssa-de-pauperibus-amandis` (unvendored). The existing record now covers On Infants' Early Deaths (:32849) and On Pilgrimages (:33740). `cappadocian.term.philoptochia` and `cappadocian.story.poorhouse-famine-month` repointed.
14. `kind: vendored` → `unvendored` (rights and discovery aligned) on `basil-against-eunomius`, `gregory-nyssa-in-xl-martyres-ii`, `gregory-nazianzus-de-vita-sua`, `gregory-nazianzus-on-the-mamas-festival`. Check: none is in `cic/texts/` (e.g. zero "Mamas" hits in `npnf207_cyril-jerusalem-gregory-nazianzen.xml`).
15. `cappadocian.quote.basil-against-eunomius-ant`: re-sourced to `basil-letters-general-corpus`, Letter XVI. Source: `npnf208_basil-letters-select-works.xml:24124-24151`.
16. `cappadocian.term.epektasis`: re-sourced to Nyssa, Against Eunomius VIII (NPNF numbering). Source: `npnf205…:18784-18787`.

### Bethlehem circle
17. `hal.dw.suffering`, `hal.dw.doubt`: grief allowed; grief without limit rebuked as unbelief. Source: Jerome, Letter 39, `npnf206_jerome-principal-works.xml:8125-8127` ("Yours are detestable tears, sacrilegious tears, unbelieving tears; for they know no limits").
18. `hal.core.hieronymian`, `hal.voice.craft`: fasting comparison rests on Letter 125 §12; new `hal.source.jerome-ep125`. Source: `npnf206…:25505-25514`.
19. `hal.dw.record`: the Gospels were revised against the Greek; the Old Testament was translated from the Hebrew, "which Jerome held truest". Sources: `npnf206…:46712-46716`, `:1329-1331`; `hal.term.hebraica-veritas` not_for.
20. `hal.limit.f5-women-own-words`: Letter 46 "is held to be Jerome's own work". Source: `hal.contested.ep46-authorship`.

### Roman empire
21. `ijc.dw.jesus`, `ijc.demo.who-was-jesus`: unsourced "what he gives is not truly God's to give" replaced by the Tome's own reasoning. Source: Leo Ep. XXVIII, `npnf212_leo-great-gregory-great.xml:5487-5490`.
22. `ijc.story.tome-that-would-not-bend`, `ijc.demo.never-settled`: "settled" → "defined"; Egypt rejected it at once. Source: `ijc.force.chalcedon-failed-consensus:31-33`.
23. Same story: Tome and Canon 28 no longer in one session. Source: `npnf214_seven-ecumenical-councils.xml:19992-20000` (Session II), `:14473-14475` (sixteenth session).

### Household churches
24. `pahc.quote.the-memoirs-of-the-apostles-are-read` (modern_lens_note): in ch. 66 Justin says the memoirs "are called Gospels". Source: `anf01_apostolic-fathers-justin-irenaeus.xml:16477-16478`.
25. `pahc.story.quintus-recantation`: Quintus is told of before Polycarp's flight and arrest, not "first". Source: `anf01…:3758-3767` (ch. 1), `:3813-3820` (ch. 3).
26. `pahc.witness.god-and-argument`: two fights, leadership and whether Christ truly suffered in the flesh. Sources: Ignatius, Trall. 9, `anf01…:6612-6621`; Smyrn. 7, `:8220-8224`.
27. `pahc.force.neronian-persecution`: structural point cites 1 Clement 44 (paraphrased as "strife over the office of oversight", the translator's literal note); unsourced urgency sentence cut. Source: `anf01…:1916-1922`.

### Syriac
28. Women's choirs: "in every church" / "what our own years attest" → later accounts say they sang in the churches. Records: `syr.limit.f5-women-own-words`, `syr.demo.woman-authority` (now Widely Accepted), `syr.story.choirs-tradition`, `syr.gravity.covenant-life`, `syr.term.qyama`, `syr.term.madrasha`, `syr.story.qyama-morning`, `syr.core.syriac`. Source: the only vendored statement is the 1898 editor's introduction, `npnf213_gregory-great-ephraim-syrus-aphrahat.xml:11253-11254`.
29. `syr.core.syriac`: "in verse rather than treatise" scoped to Ephrem's hymns. Sources: `aphrahat_demonstrations-2-7_hallock1932.txt`; `ephraim_prose-refutations_mitchell1912-1921.txt:20-22`.
30. `syr.term.ihidaya`: the pairing kept as Aphrahat's own (paraphrased); "deliberate" moved to divergence_note. Source: `npnf213…:25929-25930`.

### Zurich and Geneva
31. `rzg.contested.anabaptist-schism-legitimacy`: the Refutation records the drowning decree. Source: `zwingli_selected-works_jackson1901.txt:5568-5569`.
32. `rzg.limit.marburg-bolsec-perrinist-narrative`, `rzg.core.the-reformed-cities-zurich-and-geneva`: Calvin's letters cover Bolsec and the earlier Perrin quarrels up to 1553; only Marburg lacks a primary narrative. New `rzg.source.calvin-letters-vol2`. Source: `calvin_letters-vol2_bonnet1858.txt:15085-15092` (CCLXXXV), :2850 (CLXIV), :3488 (CLXXIII).
33. Image polemic re-cited from Article XVIII (the Mass, `zwingli_selected-works…:4565-4569`) to the Second Helvetic Confession ch. IV in `rzg.witness.triple-refusal`, `rzg.limit.hagiography-refused`, `rzg.witness.a-narrow-true-church`, `rzg.witness.what-a-stranger-would-notice`, `rzg.limit.material-culture-and-worship-space`, `rzg.ambient.emptied-worship-space`. Source: `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt:479-480`.
34. `rzg.term.providence`: names Zwingli's On the Providence of God (not held) and quotes the Commentary; new `rzg.source.zwingli-latin-works-vol3`. Sources: `zwingli_latin-works-correspondence-vol3_heller1929.txt:3419-3420`, `:13583`.

### Wittenberg
35. "We did not dispute the how" → we bind no one to a theory of how, though the founder offered the iron-and-fire picture. Records: `witt.term.sacrament-of-the-altar`, `witt.term.transubstantiation`, `witt.dw.born-in-sin-fed-at-the-table`, `witt.demo.bread-and-cup`, `witt.voice.craft`. Source: `luther_works-v2-selected_jacobs-spaeth1916.txt:7121-7125`, `:7145-7146`.
36. `witt.dw.born-in-sin-fed-at-the-table`, `witt.term.faith`: project word-count claim cut.
37. `witt.quote.second-article-of-the-creed`: "prescribed for every household"; uptake Contested. Sources: `luther_large-catechism_bente-dau1921.txt:242`; `witt.contested.household-catechism-reception:53-55`.
38. `witt.story.brussels-martyrs`, `witt.dw.true-priests-of-gods-own-making`: date given plainly; the heading's 1522 and the editor's 1 July 1523 are kept in metadata. Source: `luther_hymns_bacon-allen.txt:149-151`.

## Not fixed (escalated or logged)

- Audit item 5 (withheld sentences shipped): engine behaviour by design; questions for the project lead.
- Audit item 6 (`sources: []` with `verified-direct`): fleet-wide, over 300 records; methodology question.
- Desert Life of Antony quote records' `register: emic` and `speaker_or_author`: fleet-wide question.
- Logged in each world's `Open_Gaps_Tracking.md`: two Syriac leftovers, nine pahc force records with unsourced prose, Cappadocian records citing the four newly unvendored sources.
