# Church Family Tree links, era 7 (P2-L7) — 2026-11-08

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Eras 1 to 5 beside this folder were the precedent, and era 5's lessons were briefed to the drafters: read each movement's four fields directly, keep links joining two other-era movements for their own pass, no build narration in public text, a secondary counts only if the repo already cites it. Era 6 ran in parallel (Mark, 2026-11-08) and merged first.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 34 movements, 258 named relationships, 15 links already on main.
2. **Draft** (Opus, seven groups A-G of three to six movements): `Draft_GroupA.json` to `Draft_GroupG.json`, merged by a separate Opus agent in `Drafting_Record.json`. Eight links were drafted by two groups; the merge kept the better-evidenced version of each and says why (`merge_notes`). The Huguenot link stays "influenced", not "gave rise to": the sources show Geneva sending ministers to French churches that already existed. Six pairs carrying two links were checked; each pair is two separately evidenced relationships.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 11 substantial, 10 minor. The substantial findings: the apply step stripped the locus from secondary sources (fixed at the root, and every apply since rebuilds from main's census); three grades raised by secondaries never read; six outcomes that fail the stricter test; seven notes below the reading target; five continuations named in the text with no link; the Baptist claim stated as fact over a Contested link; two links shared with era 6 at different grades.
4. **Revision** (Opus): `Revision_Round1.json`. All 21 findings fixed: 30 links rewritten, 5 added (continued as, into era 8), 11 prose changes, 13 dispositions corrected. The two links shared with era 6 at different grades took era 6's Documented version exactly.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 1 substantial, 2 minor. All round-1 findings fixed. The substantial finding: era 6 (#1544) and P2-ML had merged to main, so the branch was out of step. The two minor findings tightened one note and shortened one quote.
6. **Revision** (applied by script, the reviewer's text as written, and the merge with main): `Revision_Round2.json`.
7. **Review round 3** (separate Opus agent, targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 1 minor. The minor finding asked for the Vulgate inconsistency below to be recorded for Mark; it is, here and in Open-Gaps ("Outcome test, adoption by vote", 2026-11-08), in the reviewer's words.

All three rounds of the cap used. No finding is open.

## Merge with era 6 and P2-ML

Era 6's pass (#1544) merged first, after P2-ML (data release 10), and took data release 11; this pass took 12. Main's census was the base, and this pass's drafting record and both revisions were applied on top. Both passes drafted eight of the same links (seven era-6/era-7 links and the Humiliati outcome); main's published versions stand and this pass's drafts of them were set aside (`Revision_Round2.json`, `main_stands`). Six agree with this pass on type and grade. Round 3 found no relationship touching era 7 drawn twice under different ids. Era 6's held item for eras 7 and 8 (`czech-churches-last-century` to `the-moravian-church-at-herrnhut`) is now drawn, and the Waldensian union's unsourced clause it flagged is removed.

## Major links

The test is Mark's change order of 2026-11-08 (Decision-Log, "Major links: a switch, and what makes a link major", the change order "Drop 'taken up'"; P2-ML): an "influenced", "argued against" or "in contact with" link is major only when one of its own sources shows an institutional act. Each outcome's locus, and every link judged minor with its reason, is in the drafting record (`outcome_locus`, `outcome_considered`) and the revisions.

Of the 107 links touching an era-7 movement:
- Major by type: 40 (continued as 21, gave rise to 12, broke with 7).
- Major by outcome: 16 (argued against 10, in contact with 4, influenced 2). Fourteen are this pass's. Two are main's: `the-english-reformation-and-elizabethan-settleme--late-medieval-lay-parish-piety` (era 6) and `the-tridentine-church--the-humiliati` (era 6's version stands; this pass drafted the same outcome).
- Minor: 51.

Drafting proposed 21 outcomes; review dropped six. Four were a church body adopting another side's confession, catechism or worship order by its own vote (Uppsala 1593, the Scottish General Assembly 1562, the Paris synod 1559, Emden 1571): a text taken up, which the stricter test excludes. Main (era 6, PR #1544; the P2-ML major-links pass) published an outcome on `hieronymian-ascetic-literary--the-tridentine-church` (Trent's Vulgate decree), the same class. Mark then ruled adoption by vote minor (Decision-Log, "Major links: a church body adopting another's text by vote is minor", 2026-11-08), so that outcome is removed and all six links of the class are treated alike. The other two dropped were Teresa's foundations under a decree of Trent (one person's practice) and the Kyiv synod's verbal judgment of 1628 on Smotrytsky's Apology.

## Counts

- Links touching an era-7 movement: 107. This pass added 78 and changed 8 already on main (six notes rewritten for the reading target, one cleared of build narration, one rewritten to add the 1527 verdict on Manz); 14 came from the era 6 pass, and 7 earlier links stand unchanged. No link retired; every published ID stands.
- Census links in all: 364 at data release 11, 442 after this pass. Data release 12 (2026-11-08).
- Grades of the links this pass added: Documented 59, Widely Accepted 10, Inferential-Thin 7, Contested 1, Dominant Modern Reconstruction 1.
- Types of the links this pass added: influenced 26, argued against 17, continued as 11, gave rise to 11, broke with 7, in contact with 6.
- Dispositions of the named relationships (drafting, 324): link 157, no-entry 67, not-a-relationship 41, qualify 39, remove 14, out-of-scope 6. Revision 1 corrected 13 (misused out-of-scope among them). "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 48 era-7 movement fields changed across drafting and revision. Every changed paragraph, note and outcome scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (scores in the drafting record and revision files). One summary of eleven words is too short to score.
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines. The validator does not check secondary quotes; all 66 era-7 secondary quotes with a locus were checked by hand in revision 1 and review round 2 (Open-Gaps, "The validator does not check secondary quotes", 2026-11-08).

## Two-way check

### Prose to links

Every relationship named in an era-7 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it is not a relationship claim (per-relationship record: `Drafting_Record.json`, `dispositions`, with revision 1's `dispositions_changed`). Round 1 found five continuations named with no link; revision 1 drew all five.

Texts that were wrong, not just unsupported, each fixed in about a sentence: the Jesuits as parent of all the mission-born churches (Kongo, 1491, and New Spain, 1524, came first); the Northeast India churches as heirs of the St Thomas Christians (the era-9 text has Welsh and American missions plant them); the 1552 schism dated to the seventeenth century; the Jesuits' expulsion from Ethiopia in 1632 (Lobo gives 1634); Lucaris's "Greek College ties" (the Greek College men were his enemies); the Remonstrants' "five points" (the wrong five).

Sentences qualified or removed:

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| lutheran-wittenberg-and-its-congregations | relationsSummary | remove | The inventory tied 'late-medieval piety' to Late-Medieval Lay Parish Piety, which is English parish religion; no source ties Wittenberg to it. The vague clause is replaced by the documented Theologia … |
| lutheran-wittenberg-and-its-congregations | relationsSummary | remove | 'Its Catholic houses continued within the Catholic Church': no vendored text shows the order's split house by house. Removed from this field; the Tridentine movement's own summary still carries 'the C… |
| the-reformed-cities-zurich-and-geneva | relationsSummary | qualify | 'Parent of' claims descent; the sources show Geneva's pattern taken up (typed 'influenced'). Field now reads 'shaped'. Also named in the-scottish-reformation-and-kirk. |
| the-reformed-cities-zurich-and-geneva | legacy | qualify | 'Descend from' for the four traditions outruns the sources; now 'took their pattern from them'. Whole field rewritten for reading level. |
| the-reformed-cities-zurich-and-geneva | relationsSummary | qualify | 'Parent of' claims descent; the sources show Geneva's pattern taken up (typed 'influenced'). Field now reads 'shaped'. Also named in the-huguenots. |
| the-reformed-cities-zurich-and-geneva | legacy | qualify | 'Descend from' for the four traditions outruns the sources; now 'took their pattern from them'. Whole field rewritten for reading level. |
| the-reformed-cities-zurich-and-geneva | relationsSummary | qualify | 'Parent of' claims descent; the sources show Geneva's pattern taken up (typed 'influenced'). Field now reads 'shaped'. Also named in dutch-further-reformation-and-refuge-culture. |
| the-reformed-cities-zurich-and-geneva | legacy | qualify | 'Descend from' for the four traditions outruns the sources; now 'took their pattern from them'. Whole field rewritten for reading level. |
| the-reformed-cities-zurich-and-geneva | relationsSummary | qualify | 'Parent of' claims descent; the sources show Geneva's pattern taken up (typed 'influenced'). Field now reads 'shaped'. Also named in puritanism. |
| the-reformed-cities-zurich-and-geneva | legacy | qualify | 'Descend from' for the four traditions outruns the sources; now 'took their pattern from them'. Whole field rewritten for reading level. |
| the-anabaptist-movements | relationsSummary | qualify | Lutheran condemnation is documented (Augsburg Confession IX, XVI); Lutheran persecution on the scale implied is not shown in any vendored text. Now 'condemned them'. |
| the-anabaptist-movements | relationsSummary | qualify | R1-10: the qualification is now carried out in the text. |
| the-anabaptist-movements | longDescription | qualify | No vendored text shows Lutheran authorities executing Anabaptists. Lutheran confessions do treat their teaching as a danger to government (Formula of Concord XII, 'Articles that cannot be tolerated in… |
| the-anabaptist-movements | why | qualify | 'Hunted them down' is not shown for Lutheran authorities. Now 'condemned them for it', which all three links support. |
| the-anabaptist-movements | legacy | qualify | The Brethren are the era-8 Radical Pietism movement. Brumbaugh rejects 'a branch of the Mennonites'; the Ephrata chronicle shows Mennonite-descended members and the martyr book printed. Now 'the later… |
| family-of-love-and-spiritualists-franck-niclaes | relationsSummary | qualify | No census movement is named and no vendored source traces a line from the Familists or Franck to later dissent. William Penn says some Seekers were called 'the Family of Love' by others, which is a na… |
| family-of-love-and-spiritualists-franck-niclaes | legacy | qualify | No census movement named. Vendored prints show reprinting (the Paradoxa, 1559; an English treatise, 1640) and the Martyrs Mirror citing his chronicle, but no later spiritualist text naming him was fou… |
| family-of-love-and-spiritualists-franck-niclaes | legacy | qualify | No vendored text shows Dutch printers; the one printer the host names is at Cologne, and the Dutch Further Reformation movement is unrelated. English readers are shown (Knewstub quotes the Evangelium … |
| family-of-love-and-spiritualists-franck-niclaes | legacy | qualify | No vendored or repo-cited source traces the toleration arguments to the Familists. Now stated as unproven. |
| the-english-reformation-and-elizabethan-settleme | relationsSummary | qualify | The dissenting churches came out of the Puritan wing, not the settlement as such; the same evidence (Baxter, Smyth) would double up on two links. The sentence now routes through Puritanism, carried by… |
| the-english-reformation-and-elizabethan-settleme | legacy | qualify | Routed through the Puritan wing, as in the summary. |
| the-english-reformation-and-elizabethan-settleme | legacy | qualify | Routed through the Puritan wing: Smyth renounced his orders from the bishop of Lincoln and McGlothlin traces the Separatists to Puritans. |
| dutch-further-reformation-and-refuge-culture | relationsSummary | qualify | No census movement for the diaspora churches; no vendored or repo-cited source shows the piety reaching either place (the 1840 American constitution shows the church, not this piety). |
| dutch-further-reformation-and-refuge-culture | legacy | qualify | As in the summary. |
| the-remonstrants-and-dort | legacy | qualify | No census movement for the later Dutch Reformed churches. Supported by the 1840 Reformed Dutch Church constitution (subscription formula); 'worldwide' narrowed to the attested reach. |
| the-remonstrants-and-dort | legacy | remove | Misstates which five points (the Remonstrant articles are what the Canons answer) and has no vendored or repo-cited source for the modern teaching use. |
| the-waldensian-reformed-union | legacy | remove | The union is 1979; the Methodist census movement ends in 1906, so no census movement is the party, and no vendored or repo-cited source carries it. |
| the-waldensian-reformed-union | legacy | remove | No census movement; no vendored or repo-cited source. |
| anti-trinitarian-currents-servetus-polish-brethr | legacy | qualify | Inventory's Further Reformation corrected to the Remonstrants, whom Rees names. Inferential-Thin link; the influence is qualified in the text. |
| anti-trinitarian-currents-servetus-polish-brethr | legacy | qualify | Belsham (1815) names Boston's creeds 'Socinian'. Inferential-Thin; the clause already hedged and is kept as 'may have'. |
| the-society-of-jesus | relationsSummary | qualify | Too wide: Kongo's church began with the Portuguese mission of 1491, before the Society existed, and New Spain's first missions were not Jesuit. Rewritten to name Japan and China, each linked with 'gav… |
| the-society-of-jesus | legacy | remove | No vendored or repo-cited source shows Protestants making the Exercises, or a growing number of them. Removed. |
| tridentine-parish-renewal-borromean-milan | legacy | qualify | Narrowed to what Peña (1610) shows: bishops in many lands followed his example and his councils' decrees. Widely Accepted. |
| carmelite-reform-and-spanish-mystics | longDescription | qualify | The Spanish Inquisition has no census movement (the Tridentine entry covers the Roman Inquisition). Shown for Teresa (her Life denounced in 1574 and examined); not shown for John. Narrowed to Teresa. |
| carmelite-reform-and-spanish-mystics | legacy | remove | No vendored or repo-cited source shows these readers. Replaced with 'translated and read far beyond Spain', which the vendored English translations show. |
| mission-born-christianities-kirishitan-japan-kon | relationsSummary | qualify | The movement is a label over four regions ('A label, not one movement'); the Jesuit origin holds for Japan and China and is drawn there (the-society-of-jesus--kirishitan-japan, the-society-of-jesus--c… |
| mission-born-christianities-kirishitan-japan-kon | relationsSummary | remove | Kongo's church (1491) and the New Spain mission (1524) predate the Council of Trent and the Catholic Reformation; no cited source ties the label as a whole to the Tridentine Church. Removed in the rew… |
| mission-born-christianities-kirishitan-japan-kon | relationsSummary | qualify | Not a tie to a census movement, but overstated: Christianity was already in China, India and Ethiopia. 'the root' becomes 'one root'. |
| mission-born-christianities-kirishitan-japan-kon | legacy | qualify | R1-03: as above. |
| mission-born-christianities-kirishitan-japan-kon | legacy | qualify | No census movement for enslaved Africans in this window (the-black-church-in-america is era 8 and not named). No vendored text, and no repo-cited work on the Atlantic, supports it; qualified to 'may h… |
| mission-born-christianities-kirishitan-japan-kon | legacy | qualify | Not a relationship; overstated (the Church of the East in Tang China, the St Thomas Christians). Now 'among the first steps'. |
| kongo-christianity-afonso-to-1650 | relationsSummary | qualify | The 1547 royal letter sends four Jesuits to help a bishop already in Kongo, so the church did not grow from them. Retyped to 'in contact with' (Documented) and the sentence rewritten. |
| kongo-christianity-afonso-to-1650 | relationsSummary | qualify | R1-02: link regraded to Inferential-Thin; the sentence now says 'may have grown out of it, as one modern study holds'. |
| kirishitan-japan | relationsSummary | qualify | R1-03: link regraded to Inferential-Thin; sentence qualified ('Later studies hold'). |
| kirishitan-japan | why | qualify | R1-03: as above. |
| china-mission-born-christianity | relationsSummary | remove | A pointer to other entries, not a relationship claim, and the Society's own text does not discuss the rites. Build narration; removed. |
| orthodoxy-under-the-ottomans-parish-millet-and-n | relationsSummary | remove | The Tarnovo patriarchate sits in serbian-and-bulgarian-medieval-monasticism (era 5, to 1396), not in a separate movement; no vendored or repo-cited source carries Euthymius's exile, and 'the Balkan de… |
| orthodoxy-under-the-ottomans-parish-millet-and-n | relationsSummary | remove | No census movement for Pec, and no vendored or repo-cited source for 1557 (Evans 1877 mentions only the later suppression of the see at Ipek). Removed; listed in wants. |
| orthodoxy-under-the-ottomans-parish-millet-and-n | legacy | qualify | An influence claim on the era-9 national churches with no vendored or repo-cited source; qualified ('may also have ...') with the reason. The chain runs through orthodoxy-under-the-ottomans-1650-1821,… |
| the-union-of-brest-and-ruthenian-greek-catholic- | relationsSummary | qualify | R1-09(b): in scope (one end era 7). The line is now drawn to the eighteenth-century church by a new 'continued as' link; the twentieth-century Lviv clause, which no source here carries, is removed. |
| the-union-of-brest-and-ruthenian-greek-catholic- | relationsSummary | remove | A note about the map's coverage, not a historical claim. |
| the-union-of-brest-and-ruthenian-greek-catholic- | legacy | remove | No single movement and no vendored or repo-cited source shows later unions modeled on Brest. The 'model' claim is removed; the family membership stays. |
| the-kyiv-mohyla-orthodox-revival | legacy | qualify | New influenced link at Widely Accepted. 'Its educated clergy for a century' is more than Consett and Mouravieff show; replaced with the tsar's request and Yavorsky. |
| the-kyiv-mohyla-orthodox-revival | legacy | qualify | Unsupported as worded and not a sentence; replaced with Yavorsky leading the church under Peter (Mouravieff). |
| armenian-christianity-new-julfa | relationsSummary | qualify | No movement for Safavid Persia. The deportation is supported (Zakaria of Kanaker, lines 1315-1317; Chamich; Seth); the figure of 300,000 and the name are not. Number removed. |
| st-thomas-christians-under-portuguese-pressure-d | relationsSummary | remove | Wrong for Northeast India: the era-9 entry's own description has the hill churches planted by Welsh and American missions. The Kerala half stays, carried by the link to the era-9 entry. |
| church-of-the-east-schism-of-1552 | legacy | qualify | Which line left Rome is disputed in the cited sources (Lamy against Badger and Wigram), and the drift falls after 1650. No 'broke with' link is drawn; the sentence is attributed to the 1877 Catholic l… |
| church-of-the-east-schism-of-1552 | legacy | qualify | The continuity is carried by the continued-as link; which line became Chaldean is qualified as contested. |
| mission-born-christianities-kirishitan-japan-kon | why | qualify | R1-03 (two-way): the same claim in the label's why had no disposition; qualified. |

### Links to prose

Every link touching an era-7 movement, and where its relationship is named:

| Link | Type | Grade | Major | Status | Named in |
|---|---|---|---|---|---|
| `waldensians-in-the-alps--the-waldensian-reformed-union` | continued as | Contested | type | changed | the-waldensian-reformed-union relationsSummary ('Medieval dissent grafted into Reformed Protestantism without losing its own memory') and longDescription ('The Waldensians had already survived three c… |
| `lutheran-wittenberg-and-its-congregations--the-anabaptist-movements` | argued against | Documented |  | changed | the-anabaptist-movements relationsSummary ('Persecuted by Lutheran ... traditions'), longDescription and why (all after prose changes 3-5) |
| `latin-pastoral-congregational-christianity--the-reformed-cities-zurich-and-geneva` | influenced | Documented |  | changed | Not named in the four fields of the-reformed-cities-zurich-and-geneva; published link reviewed because it touches this movement. |
| `the-anabaptist-movements--lutheran-wittenberg-and-its-congregations` | argued against | Documented |  | changed | the-anabaptist-movements relationsSummary (the 'loud tension in the sources'; the Hutterite chronicle's charge against Luther and Zwingli). Not named in the Lutheran texts. |
| `lutheran-wittenberg-and-its-congregations--the-reformed-cities-zurich-and-geneva` | in contact with | Documented |  | changed | lutheran-wittenberg-and-its-congregations relationsSummary ('a sibling rival to the Reformed churches') |
| `lutheran-wittenberg-and-its-congregations--the-reformed-cities-zurich-and-geneva--2` | argued against | Documented |  | changed | lutheran-wittenberg-and-its-congregations relationsSummary ('a sibling rival to the Reformed churches') |
| `the-reformed-cities-zurich-and-geneva--the-anabaptist-movements` | gave rise to | Documented | type | kept | the-anabaptist-movements longDescription ('In January 1525 a handful of men in Zurich ... baptized one another as adults') and why |
| `the-reformed-cities-zurich-and-geneva--the-anabaptist-movements--2` | argued against | Documented | outcome | changed | the-anabaptist-movements relationsSummary ('Persecuted by ... Reformed ... traditions'), longDescription ('Reformed authorities ... executed them') and why ('Reformed ... authorities ... hunted them d… |
| `antiochene-exegetical-christianity-chrysostom-ce--the-reformed-cities-zurich-and-geneva` | influenced | Documented |  | kept | Not named in the four fields of the-reformed-cities-zurich-and-geneva; published link reviewed because it touches this movement. |
| `antiochene-exegetical-christianity-chrysostom-ce--lutheran-wittenberg-and-its-congregations` | influenced | Documented |  | kept | Not named in the four fields of lutheran-wittenberg-and-its-congregations; published link reviewed because it touches this movement. |
| `hieronymian-ascetic-literary--the-tridentine-church` | influenced | Widely Accepted | outcome | kept | Not named in the-tridentine-church's own text (its longDescription says only 'restating Catholic teaching on Scripture and tradition'); named in hieronymian-ascetic-literary's text, era 2. |
| `scandinavian-conversion-christianity--scandinavian-reformation-kingdoms` | continued as | Inferential-Thin | type | changed | scandinavian-reformation-kingdoms relationsSummary ('Two established national churches emerged') |
| `the-carmelites--carmelite-reform-and-spanish-mystics` | influenced | Documented |  | kept | carmelite-reform-and-spanish-mystics relationsSummary ('connects to the medieval Carmelite order'); the-carmelites legacy, era 5. |
| `the-tridentine-church--the-humiliati` | argued against | Documented | outcome | era 6 pass (main stands) | (era 6 version stands; also drafted here) Not named in the-tridentine-church's text; named in the-humiliati's text, era 5. |
| `the-reformed-cities-zurich-and-geneva--latin-papal-church-gregorian` | argued against | Documented |  | kept | Not named in the four fields of the-reformed-cities-zurich-and-geneva; published link reviewed because it touches this movement. |
| `rhineland-mysticism-and-the-friends-of-god--lutheran-wittenberg-and-its-congregations` | influenced | Documented |  | era 6 pass (main stands) | (era 6 version stands; also drafted here) lutheran-wittenberg-and-its-congregations relationsSummary, after prose change 0 ('drew on an old German mystical book, the Theologia Deutsch'), replacing 'gr… |
| `devotio-moderna-brethren-of-the-common-life--the-society-of-jesus` | influenced | Documented |  | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `the-english-mystics-and-devout--recusant-english-catholicism` | influenced | Documented |  | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `the-english-reformation-and-elizabethan-settleme--late-medieval-lay-parish-piety` | argued against | Documented | outcome | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `lollardy--the-english-reformation-and-elizabethan-settleme` | influenced | Documented |  | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `the-hussite-and-bohemian-brethren-movement--czech-churches-last-century` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) czech-churches-last-century longDescription ('the Utraquists ... and the Unity of the Brethren who grew alongside them. Surviving as a tolerated, functioning … |
| `the-hussite-and-bohemian-brethren-movement--lutheran-wittenberg-and-its-congregations` | influenced | Documented |  | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `latin-papal-church-avignon-to-lateran-v--the-tridentine-church` | continued as | Documented | type | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `byzantine-church-palaiologan--orthodoxy-under-the-ottomans-parish-millet-and-n` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) orthodoxy-under-the-ottomans-parish-millet-and-n relationsSummary ('A continuation of Byzantine Orthodoxy after Constantinople fell in 1453') |
| `muscovite-monastic-christianity--russian-church-stoglav-to-nikon` | continued as | Documented | type | era 6 pass | named in the era 6 movement text; see the era 6 audit |
| `church-of-the-east-timur-to-hakkari--church-of-the-east-schism-of-1552` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) relationsSummary: 'Told within the Church of the East, Timur to Hakkari'; longDescription: 'its highest office had become hereditary, passing from uncle to ne… |
| `st-thomas-christians-1300-1517--st-thomas-christians-under-portuguese-pressure-d` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) relationsSummary: 'A continuation of the earlier Thomas Christian tradition'; longDescription/why: 'had for centuries received their bishops from the Church o… |
| `the-ethiopian-monastic-flowering--ethiopian-christianity-gragn-to-fasilides` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) longDescription: 'reasserted itself', 'restored the ancient church'; legacy: 'The Ethiopian Orthodox Tewahedo Church survives' |
| `armenian-cilicia-after-the-kingdom--armenian-christianity-new-julfa` | continued as | Documented | type | era 6 pass (main stands) | (era 6 version stands; also drafted here) armenian-christianity-new-julfa relationsSummary ('Etchmiadzin's catholicoi continue under Safavid rule') and longDescription ('the mother see at Etchmiadzin … |
| `lutheran-wittenberg-and-its-congregations--latin-papal-church-avignon-to-lateran-v` | argued against | Documented |  | new | lutheran-wittenberg-and-its-congregations relationsSummary ('its protest against Rome'; after prose change 0, 'one friar spoke out against the sale of indulgences') and longDescription ('95 theses aga… |
| `lutheran-wittenberg-and-its-congregations--the-tridentine-church` | argued against | Documented |  | new | lutheran-wittenberg-and-its-congregations relationsSummary ('becoming a rival to Rome') |
| `the-tridentine-church--lutheran-wittenberg-and-its-congregations` | argued against | Documented | outcome | new | lutheran-wittenberg-and-its-congregations relationsSummary ('becoming a rival to Rome'); also named in (group D draft): the-tridentine-church relationsSummary and longDescription ('The Catholic Church… |
| `lutheran-wittenberg-and-its-congregations--scandinavian-reformation-kingdoms` | influenced | Documented |  | new | lutheran-wittenberg-and-its-congregations longDescription ('the churches shaped by it spread north and east across Germany and Scandinavia') and legacy ('Lutheran churches ... across ... Scandinavia')… |
| `lutheran-wittenberg-and-its-congregations--schwenckfelders` | broke with | Documented | type | new | schwenckfelders longDescription ('welcomed Luther's reform and then broke with it') and why ('broke with Luther') |
| `lutheran-wittenberg-and-its-congregations--schwenckfelders--2` | argued against | Documented |  | new | schwenckfelders longDescription ('a distinctive doctrine of the glorified, heavenly flesh of Christ that Lutherans and Reformed alike condemned') |
| `the-reformed-cities-zurich-and-geneva--schwenckfelders` | argued against | Documented |  | new | schwenckfelders longDescription ('that Lutherans and Reformed alike condemned') |
| `the-reformed-cities-zurich-and-geneva--the-scottish-reformation-and-kirk` | influenced | Documented |  | new | the-reformed-cities-zurich-and-geneva relationsSummary ('Parent of the Scottish ... traditions'; after prose change 1, 'shaped'), longDescription ('Scotland ... all trace back here') and legacy ('the … |
| `the-reformed-cities-zurich-and-geneva--the-huguenots` | influenced | Documented |  | new | the-reformed-cities-zurich-and-geneva relationsSummary ('Parent of the ... Huguenot ... traditions'; after prose change 1), longDescription ('France ... trace back here') and legacy ('the Huguenots', … |
| `the-tridentine-church--the-anabaptist-movements` | argued against | Documented | outcome | new | the-anabaptist-movements relationsSummary ('Persecuted by ... Catholic traditions'), longDescription ('Catholic ... authorities ... executed them by the hundreds') and why ('Catholic authorities ... h… |
| `the-anabaptist-movements--the-baptists` | influenced | Contested | outcome | new | the-anabaptist-movements relationsSummary ('parent of the free-church line'; after prose change 3, 'they led the way for the free churches that came later, such as the Baptists') |
| `the-anabaptist-movements--radical-pietism-and-the-brethren-dunkers-ephrata` | influenced | Documented |  | new | the-anabaptist-movements legacy ('Mennonites, Amish, Hutterites and Brethren all descend from it'; after prose change 6, 'the later Brethren drew on its beliefs') |
| `the-english-reformation-and-elizabethan-settleme--family-of-love-and-spiritualists-franck-niclaes` | argued against | Documented |  | new | family-of-love-and-spiritualists-franck-niclaes longDescription ('Familists were hunted by royal proclamation in England in 1580') and why ('England hunted them by royal proclamation in 1580') |
| `lutheran-wittenberg-and-its-congregations--the-english-reformation-and-elizabethan-settleme` | influenced | Widely Accepted |  | new | the-english-reformation-and-elizabethan-settleme relationsSummary ('Shaped by Lutheran ... influences taking root in England') |
| `the-reformed-cities-zurich-and-geneva--the-english-reformation-and-elizabethan-settleme` | influenced | Documented |  | new | the-english-reformation-and-elizabethan-settleme relationsSummary ('Shaped by ... Reformed influences taking root in England') |
| `the-english-reformation-and-elizabethan-settleme--restoration-georgian-church-of-england` | continued as | Documented | type | new | the-english-reformation-and-elizabethan-settleme relationsSummary ('the parent of ... the Anglican tradition') and legacy ('It became the Church of England') |
| `the-english-reformation-and-elizabethan-settleme--puritanism` | gave rise to | Documented | type | new | puritanism relationsSummary ('Child of ... the English settlement's tensions'); the-english-reformation-and-elizabethan-settleme legacy ('dissenting traditions ... Puritan ... are equally its children… |
| `puritanism--the-english-reformation-and-elizabethan-settleme` | argued against | Documented |  | new | puritanism longDescription ('thought the Elizabethan settlement had stopped halfway') and why ('thought the English Reformation had stopped halfway') |
| `the-english-reformation-and-elizabethan-settleme--puritanism--2` | argued against | Documented |  | new | puritanism longDescription and why ('Pressed at home') |
| `the-english-reformation-and-elizabethan-settleme--the-tridentine-church` | broke with | Documented | type | new | the-english-reformation-and-elizabethan-settleme longDescription ('Henry VIII's break with Rome in the 1530s'; 'back to Rome under Mary I') |
| `the-scottish-reformation-and-kirk--the-tridentine-church` | argued against | Documented | outcome | new | the-scottish-reformation-and-kirk longDescription ('In 1560 the Scottish Parliament abolished papal authority') |
| `the-huguenots--church-of-the-desert-huguenots` | continued as | Documented | type | new | the-huguenots legacy ('The tradition still exists in France, in the united Protestant church that grew out of it') |
| `the-english-reformation-and-elizabethan-settleme--recusant-english-catholicism` | argued against | Documented | outcome | new | recusant-english-catholicism longDescription and why ('fined as recusants'; 'from 1585 it was treason for a priest ordained abroad even to set foot in the country') |
| `the-reformed-cities-zurich-and-geneva--puritanism` | influenced | Documented |  | new | puritanism relationsSummary ('Child of Geneva'); also named in (group A draft): the-reformed-cities-zurich-and-geneva relationsSummary ('Parent of the ... Puritan traditions'; after prose change 1), l… |
| `puritanism--restoration-georgian-church-of-england` | broke with | Documented | type | new | puritanism longDescription ('after the Restoration of 1660 were ejected from the Church of England altogether') |
| `puritanism--english-old-dissent` | gave rise to | Documented | type | new | puritanism legacy ('English Congregationalism, Presbyterianism ... come straight out of it'); the-english-reformation-and-elizabethan-settleme legacy and relationsSummary ('dissenting ... churches tha… |
| `puritanism--the-baptists` | gave rise to | Widely Accepted | type | new | puritanism legacy ('much of the Baptist tradition come straight out of it'); the-english-reformation-and-elizabethan-settleme legacy ('Baptist ... equally its children') |
| `puritanism--the-evangelical-awakening-in-new-england` | influenced | Documented |  | new | puritanism relationsSummary ('parent of the evangelical line') and legacy ('its insistence on personal conversion runs directly into the evangelical revivals') |
| `dutch-further-reformation-and-refuge-culture--german-pietism-spener-francke-halle` | influenced | Documented |  | new | dutch-further-reformation-and-refuge-culture relationsSummary ('Its practical piety later fed into German Pietism') and legacy ('Translated into German, this Dutch practical divinity fed directly into… |
| `the-reformed-cities-zurich-and-geneva--dutch-further-reformation-and-refuge-culture` | influenced | Documented |  | new | dutch-further-reformation-and-refuge-culture longDescription ('Inside the Reformed church itself a movement of preachers pressed for something beyond correct doctrine'); also named in (group A draft):… |
| `the-reformed-cities-zurich-and-geneva--the-remonstrants-and-dort` | in contact with | Documented |  | new | the-remonstrants-and-dort longDescription ('The Synod of Dort, meeting through the winter of 1618-19 with delegates from Reformed churches across Europe') |
| `the-remonstrants-and-dort--the-methodist-revival` | influenced | Documented |  | new | the-remonstrants-and-dort legacy ('Arminian ... taken up a century later by John Wesley and through him by the whole Methodist family') |
| `the-reformed-cities-zurich-and-geneva--the-waldensian-reformed-union` | influenced | Documented |  | new | the-waldensian-reformed-union relationsSummary ('grafted into Reformed Protestantism') and longDescription ('agreed to join the young Reformed churches. And to pay for a new French translation of the … |
| `czech-churches-last-century--the-moravian-church-at-herrnhut` | gave rise to | Documented | type | new | czech-churches-last-century relationsSummary ('A remnant survived underground and later became the seed of the Moravian Church at Herrnhut') and legacy ('their descendants found refuge ... at Herrnhut… |
| `scandinavian-reformation-kingdoms--the-tridentine-church` | broke with | Widely Accepted | type | new | scandinavian-reformation-kingdoms relationsSummary ('Denmark-Norway's decisive break in 1536/37'), longDescription ('Gustav Vasa took the church's property and its independence'; 'arrested the bishops… |
| `the-reformed-cities-zurich-and-geneva--anti-trinitarian-currents-servetus-polish-brethr` | argued against | Documented | outcome | new | anti-trinitarian-currents-servetus-polish-brethr relationsSummary ('Michael Servetus was burned by Geneva's own council in 1553') and longDescription ('burned at Geneva in 1553 with the city council's… |
| `anti-trinitarian-currents-servetus-polish-brethr--the-remonstrants-and-dort` | influenced | Inferential-Thin |  | new | anti-trinitarian-currents-servetus-polish-brethr legacy ('scattered into the Netherlands and beyond, where their writings fed into Dutch and English rational theology'); after prose change 18 |
| `anti-trinitarian-currents-servetus-polish-brethr--early-american-unitarians-universalists` | influenced | Inferential-Thin |  | new | anti-trinitarian-currents-servetus-polish-brethr legacy ('and, at some distance, into later Unitarianism'); after prose change 18 |
| `the-society-of-jesus--the-tridentine-church` | influenced | Widely Accepted |  | new | the-society-of-jesus relationsSummary ('Spearhead of Catholic reform'; after prose change 20, 'A driving force of Catholic reform. Its theologians spoke at the Council of Trent'); longDescription ('ap… |
| `the-tridentine-church--tridentine-parish-renewal-borromean-milan` | influenced | Documented | outcome | new | tridentine-parish-renewal-borromean-milan longDescription ('The Council of Trent decided what Catholic reform ought to mean; Milan ... showed what it looked like in a parish') and why ('took the Counc… |
| `tridentine-parish-renewal-borromean-milan--the-tridentine-church` | influenced | Widely Accepted |  | new | tridentine-parish-renewal-borromean-milan legacy ('Borromeo's Milan became the template ... a working handbook for bishops'; after prose change 22, 'Borromeo's Milan became a model ... bishops in many… |
| `ambrosian-milan-standalone--tridentine-parish-renewal-borromean-milan` | influenced | Inferential-Thin |  | new | tridentine-parish-renewal-borromean-milan legacy ('his diocese still keeps the Ambrosian rite that long predates him') |
| `the-tridentine-church--carmelite-reform-and-spanish-mystics` | influenced | Documented |  | new | carmelite-reform-and-spanish-mystics relationsSummary ('lives inside the wider Tridentine Catholic reform') |
| `the-tridentine-church--the-post-vatican-ii-parish-world` | influenced | Inferential-Thin |  | new | the-tridentine-church legacy ('That framework governed Catholic life until the Second Vatican Council of 1962-65 revised it') |
| `the-society-of-jesus--kirishitan-japan` | gave rise to | Documented | type | new | kirishitan-japan relationsSummary ('Grew from the Jesuit mission of 1549') and why ('a Jesuit mission from 1549'); mission-born label longDescription ('a Jesuit mission from 1549'); also named in (gro… |
| `the-society-of-jesus--china-mission-born-christianity` | gave rise to | Documented | type | new | china-mission-born-christianity relationsSummary ('Grew from Matteo Ricci's entry in 1583 and the Jesuit China mission') and why ('Jesuits and Chinese converts argued out ...'); mission-born label lon… |
| `kongo-christianity-afonso-to-1650--the-society-of-jesus` | in contact with | Documented |  | new | kongo-christianity-afonso-to-1650 relationsSummary ('the Jesuit missions of the Catholic Reformation'), after prose change 26 |
| `kongo-christianity-afonso-to-1650--the-antonian-movement-in-kongo` | gave rise to | Inferential-Thin | type | new | kongo-christianity-afonso-to-1650 relationsSummary ('the later prophetic movement of Dona Beatriz (1704)'); the-antonian-movement-in-kongo relationsSummary ('Christianity already two centuries African… |
| `kirishitan-japan--japanese-christianity-hidden-emergence-meiji` | gave rise to | Inferential-Thin | type | new | kirishitan-japan relationsSummary ('hidden believers kept a transmitted faith ...') and why ('Hidden believers kept a transmitted faith alive ...'); mission-born label legacy ('The hidden Christians o… |
| `franciscan-order-era-6--new-spain-and-andes-mission-born-christianity` | gave rise to | Documented | type | new | new-spain-and-andes-mission-born-christianity relationsSummary ('Grew from the Franciscan mission of 1524') |
| `new-spain-and-andes-mission-born-christianity--colonial-latin-american-devotional-catholicism` | continued as | Inferential-Thin | type | new | new-spain-and-andes-mission-born-christianity relationsSummary ('colonial Latin American devotional Catholicism continues it'); colonial-latin-american-devotional-catholicism relationsSummary ('This c… |
| `new-spain-and-andes-mission-born-christianity--philippine-catholicism` | gave rise to | Documented | type | new | philippine-catholicism relationsSummary ('Grew directly out of Spanish colonial Catholicism, brought by friars'), after prose change 29 |
| `the-society-of-jesus--philippine-catholicism` | gave rise to | Documented | type | new | philippine-catholicism longDescription ('Augustinians first, then Franciscans, Jesuits, Dominicans and Recollects') |
| `philippine-catholicism--philippine-catholicism-era-8` | continued as | Documented | type | new | philippine-catholicism legacy ('its devotional culture ... descends directly from this period'); philippine-catholicism-era-8 relationsSummary ('This continues the story of Philippine Catholicism'); t… |
| `orthodoxy-under-the-ottomans-parish-millet-and-n--the-reformed-cities-zurich-and-geneva` | argued against | Documented | outcome | new | orthodoxy-under-the-ottomans-parish-millet-and-n relationsSummary ('the church councils that later repudiated his teaching') and longDescription ('repudiated by a succession of church councils after h… |
| `the-reformed-cities-zurich-and-geneva--orthodoxy-under-the-ottomans-parish-millet-and-n` | influenced | Documented |  | new | orthodoxy-under-the-ottomans-parish-millet-and-n relationsSummary and longDescription ('his Calvinist-sounding Confession of 1629') |
| `the-tridentine-church--orthodoxy-under-the-ottomans-parish-millet-and-n` | argued against | Documented |  | new | orthodoxy-under-the-ottomans-parish-millet-and-n relationsSummary ('his Greek College ties', rewritten in prose change 30 as his enemies trained at the Greek College) |
| `orthodoxy-under-the-ottomans-parish-millet-and-n--the-union-of-brest-and-ruthenian-greek-catholic-` | broke with | Documented | type | new | the-union-of-brest-and-ruthenian-greek-catholic- longDescription ('Their opponents met in the same town at the same time and rejected it outright'; 'to the Orthodox it had left') and why |
| `the-tridentine-church--the-union-of-brest-and-ruthenian-greek-catholic-` | in contact with | Documented | outcome | new | the-union-of-brest-and-ruthenian-greek-catholic- longDescription ('accepted communion with Rome'; 'had to explain itself constantly - to Rome') and why |
| `the-kyiv-mohyla-orthodox-revival--the-union-of-brest-and-ruthenian-greek-catholic-` | argued against | Documented |  | new | the-kyiv-mohyla-orthodox-revival relationsSummary ('the response to the Union of Brest') and longDescription ('Orthodox Kyiv answered the Union of Brest'); the-union-of-brest-and-ruthenian-greek-catho… |
| `the-kyiv-mohyla-orthodox-revival--orthodoxy-under-the-ottomans-parish-millet-and-n` | influenced | Documented |  | new | the-kyiv-mohyla-orthodox-revival longDescription ('approved in revised form by a council at Iaşi in 1642') and legacy ('Mohyla's Confession was accepted well beyond Ukraine') |
| `the-kyiv-mohyla-orthodox-revival--russian-church-nikon-to-holy-synod` | influenced | Widely Accepted |  | new | the-kyiv-mohyla-orthodox-revival legacy ('supplied Russia with its educated clergy for a century'; 'Peter the Great's church reforms have a distinctly Kyivan accent'), both rewritten in prose change 3… |
| `the-society-of-jesus--the-kyiv-mohyla-orthodox-revival` | influenced | Dominant Modern Reconstruction |  | new | the-kyiv-mohyla-orthodox-revival longDescription ('turned it into a college on the Jesuit model') and why ('built it on the Jesuit model') |
| `orthodoxy-under-the-ottomans-parish-millet-and-n--russian-church-stoglav-to-nikon` | in contact with | Documented | outcome | new | russian-church-stoglav-to-nikon relationsSummary ('Moscow became a patriarchate in 1589, when the visiting Ecumenical Patriarch Jeremiah II consecrated Job'), longDescription and why |
| `russian-church-stoglav-to-nikon--the-old-believers` | influenced | Documented |  | new | russian-church-stoglav-to-nikon legacy ('a body of liturgical practice widely believed to be untouchably ancient ... the Old Believers who broke away over it') |
| `the-tridentine-church--st-thomas-christians-under-portuguese-pressure-d` | argued against | Documented | outcome | new | longDescription: 'in 1599 Archbishop Aleixo de Menezes convened a synod at Diamper that placed the community under Latin jurisdiction, revised its liturgy, and ordered its Syriac books corrected or bu… |
| `church-of-the-east-schism-of-1552--st-thomas-christians-under-portuguese-pressure-d` | in contact with | Documented | outcome | new | St Thomas longDescription/why: 'received their bishops from the Church of the East'; 1552 relationsSummary: 'kin story: the Coonan Cross Oath in Malabar is the same communion's other seventeenth-centu… |
| `st-thomas-christians-under-portuguese-pressure-d--the-society-of-jesus` | broke with | Documented | type | new | longDescription: 'swore they would no longer obey the Jesuits'; why: 'swore they would no longer obey the Jesuits' |
| `st-thomas-christians-under-portuguese-pressure-d--northeast-india-revivals-and-the-mar-thoma-refor` | continued as | Widely Accepted | type | new | relationsSummary: 'the 1653 oath's lines become today's Kerala churches'; legacy: 'Those who did not are the ancestors of the Malankara Orthodox, Jacobite, Mar Thoma and related churches' |
| `ethiopian-christianity-gragn-to-fasilides--the-society-of-jesus` | broke with | Documented | type | new | relationsSummary: 'Fasilides's restoration and expulsion of the Jesuits (1632)'; longDescription: 'His son Fasilides expelled the Jesuits, restored the ancient church'; legacy: 'a foreign form of the … |
| `the-society-of-jesus--ethiopian-christianity-gragn-to-fasilides` | argued against | Documented |  | new | longDescription: 'That help brought Jesuits, and after decades of argument Emperor Susenyos converted to Catholicism and tried to impose it'; relationsSummary: 'the Jesuit interlude ends in Susenyos's… |
| `church-of-the-east-schism-of-1552--the-tridentine-church` | in contact with | Documented | outcome | new | relationsSummary: 'he professes at Rome (1553), is consecrated in St Peter's'; longDescription: 'sent him to Rome. He made a profession of faith there, was consecrated patriarch in 1553'; why: 'travel… |
| `church-of-the-east-schism-of-1552--church-of-the-east-chaldean-consolidation` | continued as | Widely Accepted | type | new | relationsSummary: 'the Chaldean line begins and the communion carries two rival patriarchates ever after', 'with the Chaldean consolidation as the continuation'; longDescription: 'the ancient communio… |
| `russian-church-stoglav-to-nikon--russian-church-nikon-to-holy-synod` | continued as | Documented | type | new | named in the era 6 movement text; see the era 6 audit |
| `the-union-of-brest-and-ruthenian-greek-catholic---ruthenian-uniate-18th-century` | continued as | Widely Accepted | type | new | named in the era 6 movement text; see the era 6 audit |
| `armenian-christianity-new-julfa--armenian-christianity-era-8` | continued as | Widely Accepted | type | new | named in the era 6 movement text; see the era 6 audit |
| `orthodoxy-under-the-ottomans-parish-millet-and-n--orthodoxy-under-the-ottomans-1650-1821` | continued as | Documented | type | new | named in the era 6 movement text; see the era 6 audit |
| `the-tridentine-church--catholic-church-ancien-regime` | continued as | Documented | type | new | named in the era 6 movement text; see the era 6 audit |


## Escalations and open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08), after era 6's entries:
- Outcome test, adoption by vote: closed by Mark's ruling (Open-Gaps, "'Outcome test, adoption by vote' (2026-11-08) is closed").
- Sentence fragments in era-7 prose. For the census owner, or P2-L11.
- Long link notes, era 7. For P2-L11.
- The validator does not check secondary quotes. For the validator's owner.
- Wanted texts that would lift three era-7 links.
- A label movement with no links of its own. For Mark.
- Page recordings read the old descriptions, era 7: 4 pages. A paid voice run, for Mark.
- "Held for later link passes, from era 6": era 7's part closed.

Four non-relationship claims with no vendored source were left standing under the open method question "Well-known facts with no vendored source": the Scottish records "even denser than Geneva's"; the recusants' legal return and the 1970 canonization; the Huguenot congregations in Berlin, Amsterdam, Cape Town and Charleston; Harvard "to train its ministers".

The commentary check's TODO cue matched the Spanish "Todos" in a verbatim Motolinía quote; the cue now needs a word boundary, with a regression test (`tools/tests/test_check_live_commentary.py`).

## Wanted texts

- A Jesuit letter or relation from Malabar of 1653-54 on the revolt against Archbishop Garcia, for the Jesuit side of st-thomas-christians-under-portuguese-pressure-d--the-society-of-jesus.
- A clean Latin or German text of the Second Helvetic Confession, ch. XI (e.g. Müller, Bekenntnisschriften der reformierten Kirche, 1903), to replace the garbled Niemeyer OCR naming Schwenckfeld
- A cleaner OCR of the Acta Ecclesiae Mediolanensis (another scan of the 1582 or 1599 printing) for the first provincial council's seminary decree.
- A cleaner text of the China mission's beginnings: Ricci's own Italian commentaries (Tacchi Venturi, Opere storiche del P. Matteo Ricci, 1911-13) or a better scan of Trigault 1615.
- A papal or curial document on the Danish or Swedish break (1527-1537), to show Rome's side of the rupture
- A papal or curial response to the Scottish Parliament's act of August 1560, to test a 'broke with' type for the Kirk and Rome.
- A printed source on Kyiv academy graduates in the Russian church, 1650-1750.
- A public-domain source on Central African Christians among the enslaved in the Americas (seventeenth century), for the Atlantic claim in the label's legacy
- A public-domain study of the Ambrosian rite's origins (e.g. L. Duchesne, Christian Worship: Its Origin and Evolution, English 1903) to test which parts of the rite go back to Ambrose's Milan.
- A readable text of Smotrytsky's Apologia (1628) or of the Lithos (1644), to document the union arguing against Orthodox Kyiv.
- A source for Euthymius of Tarnovo's exile (1393) and the Bulgarian church after Tarnovo, if the summary is to name it again.
- A source for the Utraquist consistory's continuity across 1517 (e.g. Utraquist consistory acts), to cover the other half of the Czech movement
- A source for the Waldensian Church in Argentina and Uruguay and for the 1979 Waldensian-Methodist union (twentieth-century, likely out of window)
- A source for the legal return of English Catholicism (Relief Acts 1778-1829; hierarchy 1850) and the canonization of 1970.
- A source for the restoration of the Serbian Patriarchate of Pec in 1557 (e.g. a printed Serbian or Greek chronicle, or a pre-1930 history), for the Ottoman Orthodoxy summary.
- A source on the Augustinian Hermits' German (Saxon) congregation in the 1520s, for what happened to its houses in Lutheran lands
- A source on the reception of the Spiritual Exercises among Protestants and of Teresa and John among Protestant, literary and psychological readers (e.g. William James, The Varieties of Religious Experience, 1902), if the removed claims are to return.
- A source showing later Byzantine-rite unions (Uzhhorod 1646 and after) modeled on Brest.
- A source, if one exists, on the Inquisition and John of the Cross in his lifetime.
- An early record of Further Reformation piety among Dutch Reformed settlers at the Cape or in New Netherland (e.g. Frelinghuysen's sermons)
- Any text of the Shimun (mountain) line before 1600, and Giamil, Genuinae relationes inter Sedem Apostolicam et Assyriorum Orientalium seu Chaldaeorum Ecclesiam (Rome, 1902), for the Roman documents of 1552-53 in full; the dossier records both as not found.
- Arakel of Tabriz, History (Brosset's French, Collection d'historiens armeniens vol. 1, 1874), for the 1604-05 deportation and its numbers.
- Bernard Petitjean's letters of March 1865 on the Urakami Christians (printed in Francisque Marnas, La Religion de Jésus ressuscitée au Japon, 1896), to document the Kirishitan to hidden-Christian descent
- Bernardo da Gallo's and Lorenzo da Lucca's relations on Dona Beatriz (only modern, in-copyright editions known; Antonian dossier section 4)
- Bibliotheca Fratrum Polonorum (Amsterdam, 1665-) or Limborch's writings, to show Socinian influence on the Remonstrants from a primary text
- Coleridge's Xavier quotes checked against the Spanish of Monumenta Xaveriana I (vendored)
- Conrad Grebel's letters (1524-1525), for the Anabaptists' own record of their break with Zwingli's Zurich
- Corpus Schwenckfeldianorum vols. II-III (Schwenckfeld's letters and tracts, 1524-1530), for his own account of the 1525 Wittenberg visit and the 1526 'standing still'
- Court records or opinions of Lutheran authorities punishing Anabaptists (e.g. the Saxon trials of 1530; Melanchthon's opinions on the death penalty), to test the Lutheran part of 'persecuted ... alike'
- Diplomatarium Islandicum vols. 10-11 (Jon Arason's letters) and an account of his execution in 1550
- Evidence of the Acta Ecclesiae Mediolanensis in use outside Milan: later diocesan synods or bishops' letters citing it (for example Francis de Sales's Geneva synods), to raise the Milan-to-Tridentine link above Widely Accepted.
- Evidence on the printers of Hendrik Niclaes's books (e.g. Plantin's correspondence or a bibliography of Familist imprints), to test 'Dutch printers'
- F. M. Esteves Pereira, Chronica de Susenyos, Rei de Ethiopia (Lisbon, 1892-1900), Ge'ez and Portuguese: the Ethiopian court's own account of the conversion and the restoration of 1632; would give the Ethiopian side of ethiopian-christianity-gragn-to-fasilides--the-society-of-jesus.
- Guaman Poma, Nueva corónica y buen gobierno (1615), in a public-domain transcription
- John Milton, Sonnet 18, 'On the Late Massacre in Piedmont' (1655), in a public-domain edition
- Luther's letter to Schwenckfeld of 1526 and his 1543 reply to Schwenckfeld's messenger, in a vendored Luther edition (Weimar Briefwechsel or an English selection), for Luther's own side of the break
- Luther's preface to Romans (1522, or Jonas's Latin of 1523), to set against Tyndale's Prologue line by line.
- Mateus Cardoso's Kikongo Doutrina Christãa (1624), the Jesuit catechism for Kongo, for a possible 'influenced' link from the Jesuits
- Mendes, Expeditio Aethiopica, Books III-IV (Rerum Aethiopicarum Scriptores Occidentales IX), for the 1626 submission and the 1633 expulsion in the patriarch's own words.
- Paul III's bull against Henry VIII (1538) in a clean edition; the Brutum Fulmen copy is Latin only with garbled OCR.
- Records of the French refugee churches (London Threadneedle Street, Berlin, Amsterdam, Cape Town, Charleston) for the Huguenot legacy.
- Second Vatican Council, Sacrosanctum Concilium (4 December 1963), and Paul VI, apostolic constitution Missale Romanum (3 April 1969): to document the Tridentine Missal's revision (named in the era-10 sources file, not vendored).
- Spener, Pia Desideria and letters, or Francke, on Dutch authors read in German (Teellinck, Lodenstein, Brakel in German translation), to document a direct Further Reformation tie to Halle Pietism
- Sylvester Kossov, Exegesis (Kyiv, 1635), or the Mohyla college statutes, for the Jesuit model.
- The Act of Supremacy (1534) and the Act Restraining Appeals (1533), for the English side of the Henrician break.
- The Acta of the Synod of Dort (Latin, 1620), for the foreign deputies' subscriptions to the Canons and the sentence on the Remonstrants
- The Geneva Bible (1560) prefatory matter or the Livre des Anglois of the English congregation at Geneva, for a direct Geneva-to-Puritan line
- The Huarochirí manuscript in a public-domain edition, or Francisco de Ávila's own account of commissioning it
- The Syriac of the 1504 note of the bishops of India (Assemani BO III.1, or the Vatican manuscript), to check Mingana's English.
- The royal chronicle of Fasilides in any public-domain edition, for the expulsion of the Jesuits (1633-34) from the Ethiopian side.
- The royal proclamation of 3 October 1580 against the Family of Love (text in Wilkins, Concilia IV.297, or Steele's Tudor and Stuart Proclamations calendar, 1910), to document the 'royal proclamation in 1580' sentence directly
- The statute 27 Eliz. c. 2 (1585) against Jesuits and seminary priests, in a vendored statute collection.
- Thomas Fuller, The Church History of Britain, vol. IV (Brewer ed., 1845), the Familist passage and its footnote on the 1580 proclamation (named in the readiness dossier, not vendored)
- W. T. Whitley, The Works of John Smyth, vol. I (1915), with Whitley's biography of Smyth's Puritan years at Lincoln and Gainsborough.
