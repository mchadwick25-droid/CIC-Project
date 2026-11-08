# Era 6 rulings carried out — 2026-11-08

Mark ruled on the seven questions the era 6 links pass logged (`Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, "Rulings on the era 6 open questions", 2026-11-08). Each was shown one at a time with three options and a recommendation; he took the recommendation each time. This folder carries them out. Data release 13.

## What changed, by ruling

1. **The "Hakkari" name.** `church-of-the-east-timur-to-hakkari` is now "The Church of the East — Timur's Catastrophe and the Northern Remnant". Its informal name ("The Northern Remnant of Asia's Great Church"), region and place label ("Upper Tigris · Hakkari-Van-Urmia triangle") follow, as does one phrase in the 1552 schism's status line. The ID and page address are unchanged. The informal name was not named in the ruling; it was changed for the ruling's own reason after review round 1 flagged it, and is reported to Mark.
2. **Authority acts and jurisdiction.** Drawn as "in contact with", with an outcome where the link's own sources show the act (`Draft_Ruling2_Jurisdiction.json`, revised). Re-typed from "influenced": Constantinople and Kyiv (1124 consecration), Innocent IV and the Carmelites. New: Armenia and Caesarea (Nerses consecrated), the Coptic patriarch and Makuria (`--2`), Leo X's division of the Franciscans (`franciscan-order-era-6--latin-papal-church-avignon-to-lateran-v--2`, on the Observant chronicle in Analecta Franciscana II), and the papal acts on the Observants (Constance 1415; Eugenius IV, 1443 and 1446). Outcomes set on three existing in-contact links (the Coptic patriarch and the Zagwe church; the Church of the East and the St Thomas Christians; Numidia and Gregory the Great). Where an "influenced" link also carries real influence evidence, it stays, without the appointment as its evidence.
3. **The councils.** No change.
4. **The Carthusians after 1300.** No data change; a later Carthusian movement is made in P2-G3 (gap sweep candidate 23). Open-Gaps, "The Carthusians after 1300 go to the new-entries batch".
5. **The Free Spirit overlap.** `latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin` retired into the papal church's link to the Free Spirit, which now carries the 1367 case (Wattenbach, 1887: Hartmann, a "beghardus", questioned on all eight articles of Ad nostrum). The era 6 sects movement keeps the Adamites and points to the Free Spirit; its sources moved with the evidence. The Free Spirit text's "the questions supplied the answers" is narrowed, since Wattenbach judged Hartmann's answers genuine.
6. **Well-known facts.** The logged set (Open-Gaps 24, 52, 64): 53 facts. 35 plain, standing, each with its wanted text listed. 18 guarded: 6 sourced from vendored texts (Breslau among them: Nicholas V's commission of 1447 and Lea's index; "preaching" dropped as the cause), 11 restated as what a named witness reports, 1 a relationship the ruling does not reach (Cluny and the Cistercians). Monte Cassino's 1944 bombing was ruled guarded in review round 2 and is stated as reported.
7. **Recordings.** Each recording in `cft-website/audio/tree/manifest.json` carries `text_sha256`, the fingerprint of the text it was made from, backfilled from the commit that last changed each file. The tree pages (`Build/tools/generate_tree_pages.mjs`) and the map cards show the player only when it matches the current text. 143 of 281 were stale when written. New tests cover match, mismatch and a missing fingerprint. The paid re-voicing runs once, after era 9.

## Rounds

1. **Drafts** (Opus): `Draft_Ruling2_Jurisdiction.json`, `Draft_Ruling5_FreeSpirit.json`, `Draft_Ruling6_GuardedFacts.json`. Ruling 1 and the recordings code were done directly; the code by a separate agent, checked by tests.
2. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 7 substantial, 7 minor, no fabrication; 54 quotes rechecked. The substantial findings: a standing rule written up as one replacement (Makuria); two "influenced" links still using the appointment as evidence; Free Spirit evidence left on the era 6 sects; "the questions supplied the answers"; Kempe as "brewer's wife" (she was the brewer); Alfred said to write that Christianity "nearly" died; the Paulician text beyond its source. John Paul II's "apology" (2001) checked and kept.
3. **Revision** (Opus): `Revision_Round1.json`. All 14 fixed; one new link (the papal acts on the Observants). Departures explained in the file.
4. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 1 substantial (Monte Cassino 1944 is a guarded fact), 1 minor (the editors' twin-bull note added as a source on the Observants link).
5. **Revision** (by script, as written): `Revision_Round2.json`.
6. **Merge with main**: era 7 (data release 12) and other work merged first. The census was rebuilt from main's and every record applied again. One revision change (the 1552 schism summary's readability) was superseded by era 7's own rewrite of that field, which meets the reading target.
7. **Review round 3** (separate Opus agent, targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`.

## Checks

`node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors. `node --test Build/tools/*.test.mjs tools/tests/*.test.mjs`: pass. `atlas-check --edges-only`: clean. Tree site: 0 mismatched. Every changed public field and every new note and outcome scores Reading Ease 60 or more and FK 10 or less.

## Open items

Open-Gaps (2026-11-08): "The era 6 open questions are ruled" (closures), "One paid re-voicing batch after era 9", "The Carthusians after 1300 go to the new-entries batch", "Wanted texts from the era 6 rulings". The gap sweep README now marks its candidates 22, 23, 109, 113 (in part), 120, 121 and 122 as already ruled.

Noticed, not touched: `cic-website/data/corpus-coverage.json` is behind the corpus map by three works (two Audollent editions, Brewer's Kommodian). Only its renamed line changed here. For the Library thread.

## Wanted texts

- A present-day description of the Arian Baptistery and Sant'Apollinare Nuovo at Ravenna
- A public-domain account of St Julian's church, Norwich: the bombing in the war and the rebuilding of the cell
- A repo-cited study of the memory of 1204 in the Orthodox churches
- A source for the Allied bombing of Monte Cassino in February 1944, in a repo-cited history or a public-domain official account, so the sentence can drop "is reported".
- A source for the closing of the Devotio Moderna houses during the Reformation
- A source for the earthquake (1349) and the Allied bombing (1944) of Monte Cassino
- A source for the growing use of Coptic in Miaphysite worship after 451 (a public-domain history of the Coptic liturgy, or a repo-cited study)
- A source for the present monastic communities at Mar Saba and Saint Catherine's, Sinai
- A source for the present-day dispute over Kyiv's legacy between Kyiv and Moscow
- A source for the reception of Dorotheus of Gaza as standard monastic reading
- A source showing the Ladder of Divine Ascent read in Orthodox monasteries in Lent (e.g. the Lenten Triodion, fourth Sunday, or a monastic typikon)
- Alfred, preface to the Old English Pastoral Care (Sweet, EETS 45 and 50, 1871): for the decay of learning, the churches ravaged and burned, and 'not even one south of the Thames'.
- An etymological dictionary in the Library (e.g. Skeat, Etymological Dictionary of the English Language, 1882) for 'bugger' from 'Bulgar'
- Faustus of Byzantium, History of Armenia III.12, 16 (Langlois, Collection I), on consecration of Armenia's heads at Caesarea; Langlois tome I is not vendored.
- Lea, A History of the Inquisition of the Middle Ages, vol. II (1888), p. 549 and following, for Capistrano at Breslau (only vol. III, whose index points there, is in the Library)
- Leo X, Ite vos (29 May 1517) and Omnipotens Deus (bull of concord), in a public-domain Latin edition: Bullarium Romanum (Turin ed.) vol. V, or Wadding, Annales Minorum ad an. 1517 nn. XX-XXX (the Glassberger editors cite both, line 37468). Would let the link quote the bull itself and give the day.
- Martin V's bulls on the Observants, including his approval of the Martinian constitutions (1430): Bullarium Franciscanum VII, ed. Eubel (1904). Only Eugenius IV's citation of them is in the Library.
- The Book of Margery Kempe, in a public-domain text or a repo-cited study: for her own brewing (I.2) and her father, mayor of Lynn.
- The Chronicle of Monte Cassino (Leo of Ostia), e.g. ed. Wattenbach, MGH Scriptores VII (1846): for the Saracen attack of 883.
- The Council of Constance's decree on the Observants, Supplicationibus personarum (1415), in full: Wadding, Annales Minorum ad an. 1415, n. VII (the editors' note at Glassberger line 18589); Glassberger prints only its opening.
