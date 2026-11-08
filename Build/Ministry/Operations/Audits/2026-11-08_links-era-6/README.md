# Church Family Tree links, era 6 (P2-L6) — 2026-11-08

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Eras 1 to 5 (`../2026-11-07_links-era-1/` to `../2026-11-07_links-era-5/`) were the precedent. Era 7 ran at the same time in a sibling session (Mark, 2026-11-08).

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 23 movements, 353 named relationships, 153 naming no census movement. The drafters were told to read each movement's four fields themselves, since the inventory misses relationships carried by persons; they added rows of their own.
2. **Draft** (Opus, five groups of four to six movements): `Draft_GroupA.json` to `Draft_GroupE.json`, merged in `Drafting_Record.json`. No link ID or movement pair was drafted by two groups. Each drafter scored its own notes and paragraphs and grepped its public text for build narration before handing in.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 5 substantial, 20 minor, no fabrication; 150 quotes rechecked, all verbatim. The substantial findings: two over-grades (the Mongol-era Church of the East and the St Thomas Christians, now Inferential-Thin; the papacy against the Bosnian Church, now Widely Accepted, since the papal letters do not name that church); an outcome that failed the test and a note that left out its source's verdict (the papacy and the inquisition-record sects); and plain facts removed against the practice of eras 2 to 5.
4. **Revision** (Opus): `Revision_Round1.json`. All 25 findings and 5 two-way gaps fixed: 14 links rewritten or regraded (no ID changed), 54 field changes, including a reading-level rewrite of every era-6 field that missed the target. Four removed facts restored. Where the reviser departed from a proposed fix (OCR kept as printed, line numbers corrected, one more year taken out of a note), it says why.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 0 substantial, 4 minor. The four were small claims that crept in during the reading-level rewrites. Its grep of all public text touching era 6 for build narration found none.
6. **Revision** (applied by script, as written): `Revision_Round2.json`.
7. **Review round 3** (separate Opus agent, targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`. Pass: 0 findings.

All three rounds of the cap used. No finding is open.

## Counts

- Links touching an era-6 movement: 69. This pass added 43; 26 were already on main from earlier passes (the era 5 pass drew 18 of them). No published link changed or retired; every ID stands.
- Census links in all: 321 before this pass, 364 after it. Data release 10 (2026-11-08).
- Grades of the links this pass added: Documented 40, Inferential-Thin 2, Widely Accepted 1.
- Types of the links this pass added: influenced 13, argued against 12, continued as 9, in contact with 6, gave rise to 2, broke with 1.
- Dispositions of the named relationships (drafting, 399): link 119, not-a-claim 102, no-entry 79, existing 38, qualify 36, remove 13, out-of-scope 12. "no-entry" means the other party has no census movement; its claim was still checked.
- Prose: 90 movement fields changed across drafting and both revisions. Every changed field scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn`, and so does every new link note and outcome (scores in each draft and revision file).
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Several quotes keep OCR errors exactly as printed (e.g. Evans's "Poman"); each is noted in the link's drafting flags.

## Major links

The rule: "gave rise to", "continued as" and "broke with" are major by type. An "influenced", "argued against" or "in contact with" link is major only when one of its own sources shows an institutional act: (a) a council, canon, synod or law condemning, deposing or excluding a group or its teaching; (b) a split into a separate church or body; (c) a rule, practice or settlement changed by an authority. A teaching or text merely taken up does not count. This is the narrower test the era 1 thread (P2-ML) relayed on 2026-11-08 as Mark's ruling; the launch prompt's earlier wording also counted a teaching taken up by the other side. The narrower test was used throughout, since it can only give fewer outcomes, never an overstated one.

Of the 69 links touching era 6, 37 are major:
- By type, 25: continued as 19, gave rise to 5, broke with 1.
- By outcome, 12: argued against 7, in contact with 4, influenced 1. By basis: (a) 5, (c) 7, (b) 0.

Outcome links, with the lines that show the act:
- `latin-papal-church-avignon-to-lateran-v--rhineland-mysticism-and-the-friends-of-god`: basis (a), a council, canon, synod or law condemning a group; shown at `cic/texts/denzinger_enchiridion-symbolorum-lat_bannwart1911.txt:15306-15311`.
- `the-english-reformation-and-elizabethan-settleme--late-medieval-lay-parish-piety`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/church-of-england_visitation-articles-injunctions-v2-1536-1558_frere-kennedy1910.txt:6313-6317`.
- `the-hussite-and-bohemian-brethren-movement--taborite-radicalism--2`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/lutzow_bohemia-historical-sketch_1920.txt:10138-10149`.
- `latin-papal-church-avignon-to-lateran-v--the-hussite-and-bohemian-brethren-movement--2`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/palacky_urkundliche-beitraege-hussitenkrieg-v2-deu-lat_1873.txt:18611-18640`.
- `latin-papal-church-avignon-to-lateran-v--waldensians-in-the-alps`: basis (a), a council, canon, synod or law condemning a group; shown at `cic/texts/morland_history-evangelical-churches-piemont_1658.txt:22808-22866; cic/texts/perrin_history-ancient-christians-valleys-alps_1847.txt:4593-4645`.
- `franciscan-order-era-6--fraticelli-spiritual-franciscan-rigorists--2`: basis (a), a council, canon, synod or law condemning a group; shown at `cic/texts/ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd3-deu-lat_1887.txt:1634-1637`.
- `latin-papal-church-avignon-to-lateran-v--fraticelli-spiritual-franciscan-rigorists`: basis (a), a council, canon, synod or law condemning a group; shown at `cic/texts/bullarium-franciscanum_v5-lat_eubel1898.txt:25393-25399`.
- `latin-papal-church-avignon-to-lateran-v--franciscan-order-era-6`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/bullarium-franciscanum_v5-lat_eubel1898.txt:38692-38696`.
- `hesychasm-and-the-palamite-synthesis--byzantine-church-palaiologan`: basis (a), a council, canon, synod or law condemning a group; shown at `cic/texts/palamas_opera-omnia-pg151-grc-lat_migne1865.txt:14786-14823`.
- `byzantine-church-palaiologan--latin-papal-church-avignon-to-lateran-v`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt:14276-14278`.
- `byzantine-church-palaiologan--muscovite-monastic-christianity`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/mouravieff_history-of-the-church-of-russia_blackmore1842.txt:3946-3957`.
- `latin-papal-church-avignon-to-lateran-v--maronite-christianity-era-6`: basis (c), a rule, practice or settlement changed by an authority; shown at `cic/texts/assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt:29209-29216`.

The reviewer checked every outcome against its locus in round 1 (one removed: the papacy and the inquisition-record sects, whose council predates the movement) and rechecked the reworded ones in round 2.

Influenced, argued-against and in-contact links judged minor, with the reason:
- `rhineland-mysticism-and-the-friends-of-god--lutheran-wittenberg-and-its-congregations`: Luther printed and praised the book, which shows a text taken up by the other side; no source on this link shows a council, a split or a changed rule.
- `rhineland-mysticism-and-the-friends-of-god--devotio-moderna-brethren-of-the-common-life`: The sources show reverence for Suso and borrowing from his books, not a council, a split or a changed rule.
- `devotio-moderna-brethren-of-the-common-life--the-society-of-jesus`: The sources show the Imitation set as reading and kept by Ignatius, a text taken up by the other side; that does not meet the test.
- `the-english-mystics-and-devout--recusant-english-catholicism`: The sources show the books copied, explained and printed by English Catholics abroad, a text taken up by the other side; that does not meet the test.
- `taborite-radicalism--inquisition-record-sects-adamites-and-kin`: The sources show the band killed, but no council, split or changed rule; the destruction of a group is not one of the kinds the test counts.
- `latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin`: The council's decree of 1311-12 was laid on beguines and beghards, before this group's time, and is carried on their own links. The 1367 hearing questioned one man and changed no rule.
- `lollardy--the-english-reformation-and-elizabethan-settleme`: The sources show trials of Lollards and later Protestant writers claiming them as forerunners. None shows a council, law, split or settlement between the two.
- `the-hussite-and-bohemian-brethren-movement--lutheran-wittenberg-and-its-congregations`: Luther's letter judges Hus and proposes union with the Bohemians, but it records no council, law, split or settlement that followed from it.
- `franciscan-order-era-6--latin-papal-church-avignon-to-lateran-v`: The sources show the appeal changed nothing, and the flight led to sentences on single men, not a ruling that changed the order or the papacy.
- `latin-papal-church-avignon-to-lateran-v--catholic-church-ancien-regime`: The Articles take up Constance's decrees, which is a teaching taken up and does not count. The 1690 condemnation is Rome's act against the Articles, not a result of the influence.
- `hesychasm-and-the-palamite-synthesis--the-hesychast-revival-paisius-and-the-philokalia`: The sources show texts gathered into an anthology and translated. That is a text taken up by the other side, not an institutional act.
- `hesychasm-and-the-palamite-synthesis--muscovite-monastic-christianity`: The sources show Nil following another writer and copying a way of life. No council, split or ruling by an authority is shown.
- `hesychasm-and-the-palamite-synthesis--the-optina-elders-and-russian-ascetic-renewal`: The sources show texts printed and read, not an institutional act.
- `muscovite-monastic-christianity--the-old-believers`: The only source is a modern history's reading; it shows no council, split or ruling linking the two.
- `muscovite-monastic-christianity--the-optina-elders-and-russian-ascetic-renewal`: The source shows a text printed and praised, not an institutional act.
- `latin-papal-church-avignon-to-lateran-v--the-bosnian-church`: Urban V's letter orders excommunications, but it is a ruling in a letter and no source shows it carried out; Nicholas V's act targets one lord.
- `church-of-the-east-timur-to-hakkari--st-thomas-christians-1300-1517`: The sources show bishops sent and a letter sent back within one church. They show no council, no split and no rule changed by the exchange.
- `church-of-the-east-under-the-mongols--st-thomas-christians-1300-1517`: A scribe's closing note shows that the patriarch was recognized. It records no council, no split and no changed rule.
- `latin-papal-church-avignon-to-lateran-v--armenian-cilicia-after-the-kingdom`: The 1342 council answered the charges, but no source here shows a lasting union, a split or a changed rule. The editor says Rome found the answer wanting and sent new envoys in 1346.

The 20 era-5 links that reach into era 6 were judged by the era 5 pass and are not rejudged here; a later pass covers outcomes on links drawn before the rule.

## Merge with era 7

Era 7 ran at the same time. This pass drew 14 links with an era-7 end: continuations to the Tridentine church, Ottoman-era Orthodoxy, the Stoglav-era Russian church, the 1552 schism, the Portuguese-era St Thomas Christians, the Ethiopian church from Gragn to Fasilides, New Julfa and the Czech churches' last century; Lollardy and the English Reformation; the English Reformation against parish piety; the Hussites and the Rhineland mystics to Lutheran Wittenberg; the Devotio Moderna to the Jesuits; the English mystics to recusant English Catholicism. Where both eras drafted the same link, the one already published on main stands; the merge outcome is recorded below when it happens.

## Two-way check

### Prose to links

Every relationship named in an era-6 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it is not a relationship claim (per-relationship record: `Drafting_Record.json`, `dispositions`; changes in `Revision_Round1.json`). Round 1 found five gaps; all were closed in revision.

Texts that were wrong, not just unsupported, each fixed in about a sentence: Eckhart "condemned in his own lifetime" (the bull of 1329 came after his death); John XXII "ruled owning nothing heretical" (the 1323 decree condemns insisting that Christ and the apostles owned nothing); a "major trial at Rome in the 1460s" ending the fraticelli (the source has a public penance in 1467); a "mountain village" patriarch the sources place at Gazarta and Mosul.

Sentences qualified or removed in drafting:

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| the-english-mystics-and-devout | longDescription | qualify | Overstated. Vendored texts show Carthusian copies of the Cloud and the Scale only (McCann 1924; Underhill 1923). Rewritten to say so. No in-window Carthusian movement exists (see the summary row). |
| the-english-mystics-and-devout | why | qualify | No vendored text ties the Carthusians to Julian or Kempe. Replaced with Cressy's 1670 printing of Julian, which the sources show. |
| the-english-mystics-and-devout | legacy | qualify | Julian among the Carthusians: unsupported, removed. The extracts are supported (Gardner 1910, lines 513-524). |
| the-english-mystics-and-devout | legacy | remove | The present-day Church of England is not the era-7 movement (inventory's guess corrected). No vendored or repo-cited source carries the calendar commemoration, so the clause is removed (wants: Common … |
| devotio-moderna-brethren-of-the-common-life | relationsSummary | qualify | No vendored or repo-cited source shows Luther's schooling with the Brethren. Qualified as uncertain. Wants: Luther's own later letter on his Magdeburg year. |
| devotio-moderna-brethren-of-the-common-life | why | remove | No source; removed from this field and kept, qualified, in the legacy. |
| devotio-moderna-brethren-of-the-common-life | legacy | qualify | No vendored or repo-cited source; 'may have ... the tie is unsure'. A link would join the movement to a 1517 church through a boy's school year, which is not what the six types describe in any case. |
| lollardy | legacy | qualify | Narrowed to what Foxe's Lincoln registers show. 'Exactly where and when the first English evangelicals appear' and 'some of the same families turn up in both sets of records' have no vendored or repo-… |
| the-hussite-and-bohemian-brethren-movement | legacy | qualify | 'We are all Hussites without knowing it' (letter to Spalatin, 1520) is not vendored. Replaced with Luther's own 1520 words in the Open Letter, carried by a new Documented influenced link. |
| taborite-radicalism | longDescription | qualify | Bartošek shows Catholic lords and Plzeň in the alliance at Lipany; the sentence now says so. |
| taborite-radicalism | longDescription | qualify | 'Its bishop died in confinement': no vendored or repo-cited source. Lützow 1920 (lines 10149-10151) has the priest Wenceslas Koranda imprisoned by George; the sentence now says that. |
| taborite-radicalism | why | qualify | 'Moderate Hussites themselves destroyed' made exact: 'an alliance led by moderate Hussites' (Bartošek). |
| taborite-radicalism | legacy | qualify | No census movement for 'central Europe'. 'Studied and copied across central Europe for a century afterward' has no vendored or repo-cited source; Lützow 1914 (lines 1496-1498) supports only Žižka's ce… |
| taborite-radicalism | legacy | qualify | A claim that Tabor's example pushed the Unity of the Brethren into pacifism. Lützow 1920 (lines 10008-10012) says only that the horrors of the Hussite wars 'may have confirmed' Chelčický's belief; Cra… |
| waldensians-in-the-alps | legacy | qualify | 'The one medieval dissenting movement still here' conflicts with the Hussite entry (the Unity lives on as the Moravian Church). Now 'one of the very few', matching the era-5 Waldensian entry. |
| waldensians-in-the-alps | legacy | remove | The union with Italy's Methodists (1975/1979) is a modern event of the successor church, with no vendored or repo-cited source; removed, as era 5 removed the same clause from the earlier Waldensian en… |
| waldensians-in-the-alps | legacy | remove | The sister church in Argentina and Uruguay and the emigrant congregations in the United States: no census movement and no vendored or repo-cited source. Removed. |
| latin-papal-church-avignon-to-lateran-v | legacy | remove | 'In later Catholic reform movements' names no movement and has no vendored or repo-cited source; clause removed. |
| franciscan-order-era-6 | legacy | qualify | No movement for the modern Friars Minor, Conventuals or Capuchins (no-entry). 'The Capuchins broke away from the Observants' has no vendored source for the breakaway; Trent (Waterworth lines 22140-221… |
| franciscan-order-era-6 | legacy | qualify | 'Fed into later Western thinking about property' names no movement and has no vendored or repo-cited source. Qualified to what Ockham's vendored writings show (Scholz 1914). |
| franciscan-order-era-6 | legacy | qualify | 'One of the main engines of Catholic renewal' (the Tridentine church) has no vendored or repo-cited source; no link. Replaced by what Lea shows: the Observants given the order's head under Leo X (line… |
| observant-reform-and-popular-preaching | relationsSummary | remove | 'A merge/split test vs. the mendicant traditions, in the Phase One record's own style' is a build note, not a claim; removed. |
| observant-reform-and-popular-preaching | legacy | qualify | Capuchins: no movement. 'The reforming impulse ran on into the Capuchins' has no vendored source; qualified to what Trent's decree shows (Waterworth lines 22140-22146). |
| observant-reform-and-popular-preaching | legacy | remove | 'Observant houses became a seedbed of the Catholic reform' has no vendored or repo-cited source; clause removed. |
| fraticelli-spiritual-franciscan-rigorists | longDescription | qualify | 'A major trial at Rome in the 1460s effectively ended them' goes past the evidence: Lea (lines 8493-8497, 8505-8508) has a public penance at Rome in 1467 under Paul II and a last trace in 1471. Rewrit… |
| fraticelli-spiritual-franciscan-rigorists | why | qualify | As in the long description: the 1467 penance, not a trial that ended them. |
| fraticelli-spiritual-franciscan-rigorists | legacy | qualify | 'Fed directly into later Western thinking about property' names no movement and has no vendored or repo-cited source; removed. |
| hesychasm-and-the-palamite-synthesis | legacy | qualify | No vendored or repo-cited source for the spread 'into Russia and Romania' as such; replaced by what the Optina books show: Paisius, an elder in Moldavia, put Palamas into Slavonic, and Optina printed … |
| hesychasm-and-the-palamite-synthesis | legacy | remove | The Way of a Pilgrim has no census movement and no vendored or repo-cited source; the clause (also a broken sentence) is removed. |
| byzantine-church-palaiologan | relationsSummary | qualify | Before 1453 the patriarchal church itself proclaimed the union in the City (Leonard of Chios, PG 159 lines 54517-54518); it was monks, clergy and people who rejected it (Leonard 54757-54758). Rewritte… |
| byzantine-church-palaiologan | legacy | qualify | A formal repudiation has no vendored or repo-cited source (wanted: the synod usually dated 1484). Leonard of Chios supports 'never truly took up'. Rewritten. |
| muscovite-monastic-christianity | longDescription | qualify | No vendored or repo-cited source for a council of 1503 deciding the quarrel. Mouravieff (lines 4479-4489) shows the outcome: soon after Simon became metropolitan in 1496, the grand prince meant to tak… |
| muscovite-monastic-christianity | why | qualify | As in the long description. |
| the-bosnian-church | legacy | qualify | No movement for Islam; Catholicism and Orthodoxy name no single movement. Evans (1877, lines 2456-2462) supports the turn to Islam; nothing vendored or repo-cited shows the rest. Qualified. |
| the-bosnian-church | legacy | remove | 'Part of Bosnian national self-understanding in the twentieth century' has no vendored or repo-cited source; that clause is removed and 'the argument is still running' kept (Rački, Truhelka and the mo… |
| the-ethiopian-monastic-flowering | longDescription | qualify | 'Harried for generations' has no vendored or repo-cited source. Kept: the Ewostathians' double Sabbath. The court chronicle shows only the king's order (zara-yaqob file lines 7360-7362). |
| the-ethiopian-monastic-flowering | longDescription | qualify | 'Conceded the point at a council in 1450': no vendored or repo-cited source for the council or its date (Shared-Events candidates list it as 'no sources at all'). Rewritten to what Zara Yaqob's chroni… |
| the-ethiopian-monastic-flowering | why | qualify | 'Persecuted for generations' unsupported; removed, as in the longDescription. |
| the-ethiopian-monastic-flowering | why | qualify | 'Finally conceded the point in 1450' unsupported; replaced by the chronicle's order on the Sabbath. |
| church-of-the-east-timur-to-hakkari | longDescription | qualify | Link drafted (LA). The clause 'a patriarch who now governed from a mountain village' is contradicted by the sources: the 1490 history puts the patriarch at Gazarta on the upper Tigris and buries his s… |
| church-of-the-east-timur-to-hakkari | why | qualify | Link drafted (LA). 'A patriarch who now governed from a mountain village' replaced, as in the longDescription. |
| church-of-the-east-timur-to-hakkari | legacy | qualify | Link drafted (LC). 'The hereditary patriarchate that formed in the mountains': no source shows the patriarchate formed in the mountains in this window; reworded to 'held by one family' (Masius and Ass… |
| maronite-christianity-era-6 | relationsSummary | remove | Mamluk raids on the Kesrwan around 1305 'displaced Christian populations': no vendored or repo-cited source (the Maronite dossier lists the Mamluk sources as not searched). Removed from all three fiel… |
| maronite-christianity-era-6 | longDescription | remove | Kesrwan campaigns: unsupported; removed. 'Survived largely by remoteness' kept as description. |
| maronite-christianity-era-6 | longDescription | qualify | 'A self-understanding that this era's documents put on paper' is wrong: the bull of 1445 says the Cypriot Maronites had held Macarius's teaching of one will (raynaldus file lines 62516-62519), and the… |
| maronite-christianity-era-6 | why | remove | Kesrwan: unsupported; removed. |
| st-thomas-christians-1300-1517 | longDescription | qualify | 'Privileges from Hindu rulers and a headman of its own': no vendored source shows the privileges or a headman in this window. What a source shows is kept: Marignolli at Kollam found the Christians of … |
| st-thomas-christians-1300-1517 | why | qualify | As the longDescription: 'privileges from local Hindu rulers' replaced by what Marignolli shows, the pepper gardens. |
| armenian-cilicia-after-the-kingdom | relationsSummary | remove | Build narration ('in the record') in a public field, and wrong: the census carries Armenian movements for eras 7, 8 and 9, and Zakaria of Kanaker (vendored) writes of the 1600s. Removed. |

Twelve relationships join two movements of other eras and are held for those passes (Open-Gaps, "Held for later link passes, from era 6", 2026-11-08).

### Links to prose

Every link touching an era-6 movement, and where its relationship is named:

| Link | Type | Grade | Outcome | Status | Named in |
|---|---|---|---|---|---|
| `waldensians-in-the-alps--the-waldensian-reformed-union` | continued as | Contested |  | on main (earlier) | — |
| `the-waldensians--waldensians-in-the-alps` | continued as | Widely Accepted |  | on main (era 5 pass) | — |
| `latin-papal-church-avignon-to-lateran-v--lollardy` | argued against | Documented |  | on main (earlier) | — |
| `latin-papal-church-avignon-to-lateran-v--the-hussite-and-bohemian-brethren-movement` | argued against | Documented |  | on main (earlier) | — |
| `the-hussite-and-bohemian-brethren-movement--latin-papal-church-avignon-to-lateran-v` | argued against | Documented |  | on main (earlier) | — |
| `lollardy--the-hussite-and-bohemian-brethren-movement` | influenced | Widely Accepted |  | on main (earlier) | — |
| `st-thomas-christians-of-india--st-thomas-christians-1300-1517` | continued as | Widely Accepted |  | on main (earlier) | — |
| `makurian-nubian-christianity--terminal-christian-nubia` | continued as | Documented |  | on main (earlier) | — |
| `cistercian-monasticism--the-english-mystics-and-devout` | influenced | Documented |  | on main (era 5 pass) | — |
| `canons-regular-victorine-school--the-english-mystics-and-devout` | influenced | Documented |  | on main (era 5 pass) | — |
| `carthusian-life--the-english-mystics-and-devout` | influenced | Inferential-Thin |  | on main (era 5 pass) | — |
| `athonite-and-comnenian-byzantine-monasticism--hesychasm-and-the-palamite-synthesis` | influenced | Documented |  | on main (era 5 pass) | — |
| `the-franciscan-movement--fraticelli-spiritual-franciscan-rigorists` | gave rise to | Documented |  | on main (era 5 pass) | — |
| `the-franciscan-movement--franciscan-order-era-6` | continued as | Documented |  | on main (era 5 pass) | — |
| `the-dominican-order--rhineland-mysticism-and-the-friends-of-god` | gave rise to | Documented |  | on main (era 5 pass) | — |
| `latin-papal-church-avignon-to-lateran-v--the-beguines` | argued against | Documented |  | on main (era 5 pass) | — |
| `latin-papal-church-avignon-to-lateran-v--free-spirit-heresy` | argued against | Documented |  | on main (era 5 pass) | — |
| `joachimite-current--franciscan-order-era-6` | influenced | Documented |  | on main (era 5 pass) | — |
| `latin-papal-church-gregorian--latin-papal-church-avignon-to-lateran-v` | continued as | Documented |  | on main (era 5 pass) | — |
| `latin-papal-church-avignon-to-lateran-v--military-religious-orders-templars-hospitallers` | argued against | Documented |  | on main (era 5 pass) | — |
| `armenian-cilicia--armenian-cilicia-after-the-kingdom` | continued as | Documented |  | on main (era 5 pass) | — |
| `byzantine-church-after-1054--byzantine-church-palaiologan` | continued as | Documented |  | on main (era 5 pass) | — |
| `kievan-rus-christianity-1054-1240--muscovite-monastic-christianity` | gave rise to | Documented |  | on main (era 5 pass) | — |
| `church-of-the-east-under-the-mongols--church-of-the-east-timur-to-hakkari` | continued as | Documented |  | on main (era 5 pass) | — |
| `zagwe-and-early-solomonic-ethiopian-christianity--the-ethiopian-monastic-flowering` | continued as | Documented |  | on main (era 5 pass) | — |
| `the-franciscan-movement--observant-reform-and-popular-preaching` | influenced | Documented |  | on main (era 5 pass) | — |
| `rhineland-mysticism-and-the-friends-of-god--lutheran-wittenberg-and-its-congregations` | influenced | Documented |  | new | rhineland relationsSummary ('(via Theologia Deutsch) Luther'); why ('a book Martin Luther printed twice and said had taught him more about God than almost anything but the Bible and Augustine'); legacy ('the Theologia… |
| `rhineland-mysticism-and-the-friends-of-god--devotio-moderna-brethren-of-the-common-life` | influenced | Documented |  | new | rhineland relationsSummary ('feeds Devotio Moderna'); legacy ('The Devotio Moderna in the Low Countries grew in its wake', rewritten in prose change 4 as 'honored Henry Suso and drew on his books') |
| `latin-papal-church-avignon-to-lateran-v--rhineland-mysticism-and-the-friends-of-god` | argued against | Documented | yes | new (revised) | rhineland longDescription ('got him put on trial for heresy ... in 1329 a papal bull condemned twenty-eight propositions'); why ('tried for heresy and, after his death, condemned by papal bull'); legacy ('the church t… |
| `devotio-moderna-brethren-of-the-common-life--the-society-of-jesus` | influenced | Documented |  | new | devotio relationsSummary ('Jesuit pedagogy'); why ('fed into Jesuit formation'); legacy ('fed into Jesuit formation a century later'); all rewritten in prose changes 5-7 |
| `the-english-mystics-and-devout--recusant-english-catholicism` | influenced | Documented |  | new | english-mystics legacy ('circulated quietly among Carthusians and English exiles'; rewritten in prose change 3 to name Cressy's printing); relationsSummary as rewritten in prose change 0 ('English Catholics in exile c… |
| `taborite-radicalism--inquisition-record-sects-adamites-and-kin` | argued against | Documented |  | new | inquisition longDescription ('the Taborites destroyed them'); why ('wiped out by the Taborites') |
| `latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin` | argued against | Documented |  | new (revised) | inquisition longDescription ('A list of errors condemned at the Council of Vienne circulated among inquisitors as a template'); why (the same) |
| `the-english-reformation-and-elizabethan-settleme--late-medieval-lay-parish-piety` | argued against | Documented | yes | new | late-medieval-lay-parish-piety legacy ('The English Reformation abolished the guilds and chantries, whitewashed the paintings and broke up the images') |
| `lollardy--the-english-reformation-and-elizabethan-settleme` | influenced | Documented |  | new | lollardy relationsSummary ('Contested influence line to the English Reformation') and legacy ('Historians still argue over whether Lollardy fed straight into the English Reformation ... before Luther's name was heard … |
| `the-hussite-and-bohemian-brethren-movement--czech-churches-last-century` | continued as | Documented |  | new | the-hussite-and-bohemian-brethren-movement relationsSummary ('Its stricter branch, the Unity of the Brethren, lived on into the 1600s', after prose change 1), longDescription ('Out of that settlement two bodies grew. … |
| `the-hussite-and-bohemian-brethren-movement--taborite-radicalism` | gave rise to | Documented |  | new | taborite-radicalism relationsSummary ('The radical wing of the Hussite movement'), longDescription and why ('In 1420 the most radical wing of the Hussite movement founded a fortified town') |
| `the-hussite-and-bohemian-brethren-movement--taborite-radicalism--2` | argued against | Documented | yes | new | taborite-radicalism longDescription ('In the end it was fellow Hussites who destroyed it ... In 1452 George of Poděbrady, himself a Utraquist, took the town', after prose change 3), why ('an alliance led by moderate H… |
| `latin-papal-church-avignon-to-lateran-v--the-hussite-and-bohemian-brethren-movement--2` | in contact with | Documented | yes | new | the-hussite-and-bohemian-brethren-movement longDescription ('in 1436 the Compacts of Basel conceded ... legal recognition'), why ('in 1436 Bohemia won ... legal recognition for its own church') |
| `the-hussite-and-bohemian-brethren-movement--lutheran-wittenberg-and-its-congregations` | influenced | Documented |  | new | the-hussite-and-bohemian-brethren-movement legacy ('And in 1520 Luther wrote that he had not yet found any errors in Hus's writings', after prose change 2); relationsSummary ('a century before Luther') is a date compa… |
| `latin-papal-church-avignon-to-lateran-v--waldensians-in-the-alps` | argued against | Documented | yes | new | waldensians-in-the-alps relationsSummary ('survived Pope Innocent VIII's 1487 crusade bull and the Cattaneo crusade that followed it'), longDescription ('in 1487 Innocent VIII proclaimed a crusade against them, and th… |
| `franciscan-order-era-6--observant-reform-and-popular-preaching` | gave rise to | Documented |  | new | franciscan-order-era-6 relationsSummary ('Conventual/Observant polarization'; 'the Observant wing are its two named branches'), longDescription and why ('Observants, who from 1368 built up reformed houses'); observant… |
| `franciscan-order-era-6--fraticelli-spiritual-franciscan-rigorists` | broke with | Documented |  | new (revised) | fraticelli-spiritual-franciscan-rigorists relationsSummary ('Rupture inside the Franciscan family'); franciscan-order-era-6 relationsSummary ('the Spirituals crisis'; 'the Fraticelli ... its two named branches') and l… |
| `franciscan-order-era-6--fraticelli-spiritual-franciscan-rigorists--2` | argued against | Documented | yes | new (revised) | franciscan-order-era-6 longDescription ('The Spirituals, who wanted the Rule kept to the letter, were ordered to conform'); fraticelli-spiritual-franciscan-rigorists relationsSummary ('Rupture inside the Franciscan fa… |
| `latin-papal-church-avignon-to-lateran-v--fraticelli-spiritual-franciscan-rigorists` | argued against | Documented | yes | new | fraticelli-spiritual-franciscan-rigorists longDescription and why ('John XXII ordered the strictest friars to conform'; 'Those who would not submit became the fraticelli'; 'A ... trial at Rome in the 1460s'); francisc… |
| `latin-papal-church-avignon-to-lateran-v--franciscan-order-era-6` | argued against | Documented | yes | new (revised) | franciscan-order-era-6 longDescription and why ('in 1323 John XXII declared it heretical ... which put the order's own official self-understanding on the wrong side of the law'; 'Michael of Cesena fled the papal court… |
| `franciscan-order-era-6--latin-papal-church-avignon-to-lateran-v` | argued against | Documented |  | new | franciscan-order-era-6 longDescription and why ('Michael of Cesena fled the papal court with William of Ockham rather than accept it'); fraticelli-spiritual-franciscan-rigorists legacy ('the friars who fled the papal … |
| `latin-papal-church-avignon-to-lateran-v--the-tridentine-church` | continued as | Documented |  | new | latin-papal-church-avignon-to-lateran-v legacy ('the same church, reorganized by the Council of Trent a generation later'); the movement's continuesAs points to the-tridentine-church |
| `latin-papal-church-avignon-to-lateran-v--catholic-church-ancien-regime` | influenced | Documented |  | new (revised) | latin-papal-church-avignon-to-lateran-v legacy ('The conciliar claim ... resurfacing in Gallicanism') |
| `hesychasm-and-the-palamite-synthesis--byzantine-church-palaiologan` | influenced | Documented | yes | new (revised) | hesychasm longDescription ('settled by councils at Constantinople in 1341, 1347 and 1351, which vindicated Palamas') and why ('a case that church councils upheld'); byzantine-church-palaiologan relationsSummary ('rece… |
| `hesychasm-and-the-palamite-synthesis--the-hesychast-revival-paisius-and-the-philokalia` | influenced | Documented |  | new | hesychasm relationsSummary ('parent of the Philokalia line', after prose change 0) and legacy ('gathered into one book, the Philokalia ... Paisius Velichkovsky ... put Palamas on prayer into Slavonic', after prose cha… |
| `hesychasm-and-the-palamite-synthesis--muscovite-monastic-christianity` | influenced | Documented |  | new | muscovite relationsSummary ('Child of Kievan + hesychast lines', kept after prose change 4) and legacy ('the hesychast prayer this generation received from the Greeks'); movement sources note Nil's writings as 'the he… |
| `hesychasm-and-the-palamite-synthesis--the-optina-elders-and-russian-ascetic-renewal` | influenced | Documented |  | new | hesychasm legacy ('into the nineteenth-century monastic revival', after prose change 1 'In the 1800s the monks of Optina printed his work for Russian readers'); hesychasm relationsSummary after prose change 0 |
| `byzantine-church-palaiologan--latin-papal-church-avignon-to-lateran-v` | in contact with | Documented | yes | new (revised) | byzantine-church-palaiologan relationsSummary ('signs Florence (1439)'), longDescription ('in 1439 signed a union with Rome at the Council of Florence ... Mark of Ephesus refused to sign'), why (the same) and legacy (… |
| `byzantine-church-palaiologan--orthodoxy-under-the-ottomans-parish-millet-and-n` | continued as | Documented |  | new | byzantine-church-palaiologan relationsSummary ('hands directly to Ottoman-era Orthodoxy, which begins in 1453', after prose change 2 'went on, under a new patriarch, as the church of the Orthodox under Ottoman rule') … |
| `byzantine-church-palaiologan--muscovite-monastic-christianity` | in contact with | Documented | yes | new (revised) | muscovite longDescription ('in 1448, Russian bishops chose their own metropolitan without waiting on Constantinople', after prose change 5) and legacy ('the hesychast prayer this generation received from the Greeks') |
| `muscovite-monastic-christianity--russian-church-stoglav-to-nikon` | continued as | Documented |  | new (revised) | muscovite legacy ('Almost everything that follows in Russian Christianity runs back through here'); russian-church-stoglav-to-nikon longDescription ('In the century and a half after 1517 the Russian Church became some… |
| `muscovite-monastic-christianity--the-old-believers` | influenced | Inferential-Thin |  | new | muscovite relationsSummary ('parent of the Old Believers' tradition', after prose change 4 'The Old Believers' schism may also have roots in its church, though only one modern history draws that line'); the-old-believ… |
| `muscovite-monastic-christianity--the-optina-elders-and-russian-ascetic-renewal` | influenced | Documented |  | new | muscovite relationsSummary ('later renewal', after prose change 4 'the nineteenth-century elders of Optina') and legacy ('resurfaced in the elder movement of the nineteenth century'); the-optina-elders relationsSummar… |
| `latin-papal-church-avignon-to-lateran-v--the-bosnian-church` | argued against | Widely Accepted |  | new (revised) | the-bosnian-church relationsSummary ('condemned by Rome as heretical'), longDescription ('Rome repeatedly condemned it as heretical and periodically sent friars against it') and why ('Rome repeatedly condemned them as… |
| `church-of-the-east-timur-to-hakkari--st-thomas-christians-1300-1517` | in contact with | Documented |  | new | church-of-the-east-timur-to-hakkari relationsSummary ('along with the community in India, the one province Timur's armies never reached'), longDescription and why ('went on receiving bishops from a patriarch'), legacy… |
| `church-of-the-east-under-the-mongols--st-thomas-christians-1300-1517` | in contact with | Inferential-Thin |  | new (revised) | st-thomas-christians-1300-1517 relationsSummary ('A note in a book copied in 1301 shows the community still tied to its patriarch in Mesopotamia', after the round-1 revision), longDescription and why ('names the patri… |
| `church-of-the-east-timur-to-hakkari--church-of-the-east-schism-of-1552` | continued as | Documented |  | new | church-of-the-east-timur-to-hakkari relationsSummary ('In 1552 the church split when part of it entered communion with Rome'), legacy ('The hereditary patriarchate ... split in 1552'); church-of-the-east-schism-of-155… |
| `st-thomas-christians-1300-1517--st-thomas-christians-under-portuguese-pressure-d` | continued as | Documented |  | new | st-thomas-christians-1300-1517 legacy ('The centuries after 1517 brought Portuguese pressure, the Synod of Diamper in 1599 and the Coonan Cross revolt of 1653') |
| `the-ethiopian-monastic-flowering--ethiopian-christianity-gragn-to-fasilides` | continued as | Documented |  | new | the-ethiopian-monastic-flowering legacy ('The tradition carried on through the wars and upheavals of the century that followed'; 'still traces its great monastic houses to the founders of these centuries') |
| `armenian-cilicia-after-the-kingdom--armenian-christianity-new-julfa` | continued as | Documented |  | new | armenian-cilicia-after-the-kingdom relationsSummary ('a national council elects a catholicos at Etchmiadzin (1441) - the seat moves home'), longDescription, why, legacy ('Etchmiadzin has been the Mother See of the Arm… |
| `latin-papal-church-avignon-to-lateran-v--armenian-cilicia-after-the-kingdom` | argued against | Documented |  | new (revised) | armenian-cilicia-after-the-kingdom longDescription ('repeated attempts to seal a union with Rome, pressed by kings who needed western help, were resisted'), why ('a Latin Europe pressing for union with Rome, a union i… |
| `latin-papal-church-avignon-to-lateran-v--maronite-christianity-era-6` | in contact with | Documented | yes | new (revised) | maronite-christianity-era-6 relationsSummary ('received into union at the Council of Florence on 7 August 1445, and affirmed again during the Fifth Lateran Council in 1516'), longDescription and why (the same), legacy… |
| `maronite-christianity--maronite-christianity-era-6` | continued as | Documented |  | new | maronite-christianity-era-6 longDescription ('Its relationship with Rome, claimed since the crusader period'); maronite-christianity legacy ('The union begun here has held for eight centuries') |

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08):
- The Franciscan order and the Observants is drawn (closes the item held for P2-L6).
- Well-known facts with no vendored source, era 6: the era's cases added to Mark's open method question.
- The Church of the East's "Hakkari" name. For Mark.
- No link type for an authority's acts on another body's own order. A method question for Mark.
- The Council of Basel sits under the papacy. For Mark, low urgency.
- No Carthusian movement after 1300. For Mark.
- The inquisition-record sects and the Free Spirit overlap. For the census owner and Mark.
- Held for later link passes, from era 6.
- The Maronites' unbroken communion with Rome. For the Maronite world's owner.
- "Entry" in status descriptions. For P2-L11 or the census owner.
- Page recordings read the old descriptions, era 6: all 23 pages. A paid voice run, for Mark.

Notes:
- `lollardy--the-english-reformation-and-elizabethan-settleme` stays Documented: the later side names and uses the earlier one's work. No listed source gives the skeptical reading, and Hudson's study is named, not rechecked.
- Some links rest on one nineteenth-century secondary read at the cited lines (Mouravieff, 1842; Evans, 1877; Lea). Secondary works the repo names but this pass did not read carry `verification_state` `named-not-rechecked` and raise no grade.

## Wanted texts

- A Utraquist source that runs across 1517 (e.g. the Utraquist consistory's acts or the Bohemian Confession of 1575 in a vendored edition), so the Utraquist half of the continuation is shown in a primary as the Unity's half is
- A clean Greek text of the Florentine Definition with its signatures (Mansi 31's Greek columns are garbled in the vendored OCR)
- A clean edition of the Franciscan vicariate of Bosnia's founding documents
- A clean edition of the Franciscan vicariate of Bosnia's founding documents, for 'sent friars against it'
- A clean edition or translation of the tomes of 1347 and 1351 (Norman Russell's Translated Texts for Byzantinists volume is in copyright) to document the later councils' rulings in quotable form
- A dated witness to the 1341 synod at Constantinople (John Kantakouzenos's History or Nikephoros Gregoras), to carry the year on hesychasm-and-the-palamite-synthesis--byzantine-church-palaiologan
- A full English translation of the bishops of India's letter of 1504 (Latin in Assemani III.1).
- A papal letter of the 1230s-1300 on the Bosnian heretics (Gregory IX's crusade letters), for the condemnation before 1300 that belongs to the Gregorian papacy
- A primary for the 1448 election: the Russian chronicles (PSRL) or Grand Prince Basil II's letter to Constantinople, so the 1448 step does not rest on Mouravieff alone
- A primary for the capture of Tabor in 1452 (e.g. Aeneas Sylvius's letters of 1451-52, or the Old Czech Annals), so the outcome rests on a contemporary text as well as Lützow
- A public-domain modern study that argues against a Lollard contribution to the English Reformation, so the disagreement the note names can be sourced on both sides
- A public-domain primary for the Capuchins' break from the Observants (e.g. Boverius, Annales Capuccinorum, 1632), for the Franciscan and Observant legacy sentences
- A public-domain primary for the Dominican Observance (Raymond of Capua's reform letters of 1390), for the Observant text's Dominican clause
- A repo-citable source for the community's privileges and headman in 1300-1517
- A repo-cited Mamluk source or modern study (e.g. Salibi) for the Kesrwan campaigns of 1305
- A source for the Mamluk campaigns against the Kesrwan around 1305 (Arabic chronicles in translation, or Lammens, La Syrie, 1921, which the Maronite dossier found and did not vendor).
- A source for the formal repudiation of Florence at Constantinople (the synod usually dated 1484)
- A source for the formal repudiation of the union of Florence (synod at Constantinople usually dated 1484)
- A source showing the St Thomas Christians' privileges from Hindu rulers and their own headman in 1300-1517 (the 'privileges' sentence was replaced for want of one).
- Ad nostrum in the Clementines (Friedberg, Corpus iuris canonici II, 1881), not on the host per the source dossier
- An English translation of Březová's Historia Hussitica (none public-domain is known), to let a reader check the Latin
- An Old Believer text appealing to the Muscovite fathers or the Stoglav (e.g. Avvakum's Life) in a vendored edition
- An edition of the 1317 Dongola inscription
- An edition of the Dongola throne-hall inscription of 1317 (Arabic), for the mosque conversion.
- Any source for the council of Debre Mitmaq (1450) on the Sabbath; none is vendored or repo-cited.
- Duwayhi's history of the Maronite patriarchs in a clean scan, for the patriarchal line across 1300.
- Epiphanius's Life of Sergius in a vendored edition, for the hesychast side of Sergius's own circle
- Erasmus's own account of his Deventer schooling (the Compendium vitae, in a public-domain edition), to lift the Erasmus claim from editors' notes to a primary witness
- Gadla Ewostatewos (the Life of Ewostatewos), in a public-domain edition or translation; the CSCO 1955 text is in copyright. Would let the Ewostathians' side of the Sabbath quarrel return to the Ethiopian text.
- Gadla Ewostatewos; the acts of the 1450 council; a repo-cited modern study (e.g. Taddesse Tamrat)
- Gennadios Scholarios's own account of his election (his writings in PG 160 hold the confessions for Mehmed II; the election passage was not located)
- George Morel's memoir and letter to Oecolampadius (1530), in a vendored edition, for the Alpine Waldensians' outward conformity as Catholic parishioners
- John of Capistrano's report and the Breslau trial records of 1453
- John of Capistrano's report and the Breslau trial records of 1453 (or Peter Eschenloer's Breslau chronicle) in a public-domain edition, for the Observant persecution of the Jews of Breslau
- Kaminsky (1967) and Fudge (2002) on the Adamites are in copyright; a public-domain English version of Březová's 1421 chapter would let a participant read it
- Lea, History of the Inquisition, vol. II (1887), which treats the Free Spirit and the Adamites; the shelf holds vol. III only
- Leo X, Ite vos (29 May 1517), in a public-domain Latin edition (Bullarium Romanum, Turin edition, vol. V, or Wadding, Annales Minorum, vol. XVI), for the division of the order
- Lollard and early evangelical records that show the same families in both (e.g. W. H. Summers, The Lollards of the Chiltern Hills, 1906, public domain, located but not fetched; Strype, Ecclesiastical Memorials, for the 1520s Essex cases), to test the 'same families' claim before it returns
- Luther's letter to Spalatin of February 1520 ('we are all Hussites without knowing it'; WA Br 2, 42), in a vendored edition, before that saying returns to the text
- Luther's own later account of his school year at Magdeburg (his letter of 1522, in a public-domain edition of his letters), to test the Brethren tie before it is stated as fact
- Martin V's crusade bull against the Hussites (1420), in a vendored edition, as a direct source for the papacy's crusades
- Masius's letter to Busbecq on the events of 1552, in a clean edition; Sulaqa's profession of 1553.
- Michael of Cesena's appeals of 1328 and his protest of 1338 in a public-domain Latin text (Carlini 1912 prints some; the Goldast Monarchia is a verified lead), for the minister general's own voice
- Miklosich and Müller, Acta patriarchatus, vol. 2 (1402 onward), for Constantinople's own record of the Rus' metropolitans after 1402
- Papal letters sending Franciscans to Bosnia (the vicariate of 1340), in a clean edition
- Stefano Infessura, Diario della città di Roma (1467), for Paul II's public penance of the fraticelli at Rome, which Lea cites; would let the end of the fraticelli rest on a primary
- The Book of Margery Kempe in full (the 1934 manuscript's text; modern editions are in copyright), with a public-domain description of the manuscript's Mount Grace ownership, for the Kempe facts and any Carthusian tie
- The Cambrai and Paris copies of Julian's Long Text and their provenance among the English Benedictine nuns (e.g. a public-domain description of Paris BN Anglais 40 and Sloane 2499), to document Julian's circulation among the exiles directly
- The Chantries Act 1547 (1 Edw. VI c. 14) in a public-domain Statutes of the Realm volume, to document the dissolution of the guilds from the act itself
- The Church of England's Common Worship calendar (or a public-domain list of its commemorations), before any Julian commemoration returns
- The Cologne trial acts (Théry's edition, Archives d'histoire doctrinale 1926) and the full bull In agro dominico in a public-domain edition with English, to document the Cologne stage directly
- The Common Worship calendar
- The Syriac of the 1301 Cranganore colophon (Vat. Syr. 22), to settle 'Yahb Alaha V.' (Mingana) against 'Yahballaha III'.
- The Syriac text of the 1301 colophon (Vat. Syr. 22)
- The Venice 1782 first edition of the Philokalia (title page and Nikodemos's prooimion naming the fourteenth-century fathers)
- The Way of a Pilgrim in a public-domain edition, if the hesychasm legacy is to name it again
- The bull 'Benedictus sit Deus' of 7 August 1445 in a clean edition with its dating clause.
- The bull Id nostri cordis (27 April 1487) in a critical edition (e.g. Bullarium Romanum, Turin ed., vol. V), to check Morland's copy and his English
- The text of the Compacts themselves (Archiv český III, 398-444, or Mansi XXIX-XXX) in a vendored edition, for the chalice concession in the council's own words
- Thomas of Metsoph's own chronicle and his appendix on the 1441 move to Etchmiadzin, in any public-domain edition or translation.
- Wadding, Annales Minorum, ann. 1368 (nos. 10-13), the source Lea cites for Brugliano; a public-domain edition is a verified lead in the Franciscan dossiers and would give the 1368 grant a primary text
