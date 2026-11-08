# Church Family Tree links, era 8 (P2-L8) — 2026-11-08

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`, with step 4b (major links, Mark, 2026-11-08).
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Precedent: `../2026-11-07_links-era-1/` and `../2026-11-07_links-era-5/`; their wanted-texts lists were checked first.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 29 movements, 361 named relationships, 179 naming no census movement, no raw movement IDs in the text. The drafters read each movement's four fields themselves and added the relationships carried by persons that the inventory missed.
2. **Draft** (Opus, six groups of four to six movements): `Draft_GroupA.json` to `Draft_GroupF.json`, merged in `Drafting_Record.json`. Four links were drafted twice. The merge kept one of each and set the other aside (`set_aside`); `merge_notes` give the reasons. Each drafter scored its own notes, outcomes and paragraphs, so there was no separate prose pass.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 4 substantial, 20 minor, no fabrication. The substantial findings: Wesley "called on" the younger Francke (Francke was not in town); Wesley "admitted he had broken" the Church of England's rules (he wrote that he varied from its discipline by constraint); Gregory V's hanging in 1821 with no source on the link; Old Dissent "took up the revival", as broad as the claim it replaced. All 235 quotes were verbatim at their lines. No major call was disputed.
4. **Revision** (Opus): `Revision_Round1.json`. All 24 findings fixed, 9 differently from the reviewer's proposal, each with the reason. Three more tasks: the Moravian description and why no longer claim a mission scale "no other Protestant body approached" (Halle's men reached India in 1706); every "no text we hold" kind of phrase left the era-8 text; the Jesuit links carry a note that the Jesuit movement ends in 1650.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 1 substantial. Two of the round-1 replacements ("no direct tie has been traced", "that line has not been traced") turned a gap in our library into a claim about scholarship.
6. **Revision** (applied by script, the reviewer's own text): `Revision_Round2.json`.
7. **Review round 3** (separate Opus agent, targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`. Pass, 0 findings.

All three rounds of the cap used. No finding is open. `Final.json` is the state applied.

## Counts

- Links touching an era-8 movement: 94. This pass added 64 and rewrote 2 (the Methodist links to the Holiness movement and the Black Church: one note failed the reading target, the other merged two towns); 3 older links were kept as checked; 25 came from the era 6 and era 7 passes. No link retired; every published ID stands.
- The pass drafted 78 new links. At the merges, 14 were dropped because an earlier pass had published the same ID first: 1 with era 6 and 13 with era 7 (see "Merges with other passes").
- Census links in all: 442 before this pass, 506 after. Data release 13 (2026-11-08).
- Types of the links this pass added: influenced 17, argued against 12, gave rise to 10, continued as 10, in contact with 9, broke with 6.
- Grades of the links this pass added: Documented 49, Widely Accepted 9, Dominant Modern Reconstruction 3, Inferential-Thin 3.
- Dispositions of the named relationships (drafting, 367): link 182, no-entry 112, not-a-relationship 39, qualify 21, out-of-scope 7, remove 6. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 38 movement fields changed across 21 movements. Every changed paragraph, note and outcome scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn` (each prose change and revision file carries its scores).
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines. Several quotes keep OCR errors exactly as printed (e.g. "lansenii", "Jefuites", the long s as f); each is noted in the link's drafting flags.

## Major links

Counted over the 66 links this pass added or rewrote.

| | Count |
|---|---|
| Major by type | 27 (gave rise to 11, continued as 10, broke with 6) |
| Major by outcome | 12 (argued against 8, in contact with 4) |
| Outcome kinds | council or law 8, rule changed 3, split 1 |
| Judged minor | 27 (influenced 18, in contact with 5, argued against 4) |

Review left 14 outcomes. At the merge with era 7, two were removed under Mark's ruling that a church body adopting another side's text or worship order by its own vote is minor (Decision-Log, "Major links: a church body adopting another's text by vote is minor", 2026-11-08): the Zamość synod of 1720, which made laws following Trent, and the Moscow council of 1656 on the corrected service book. Their sentences are kept in `Final.json` (`dropped_outcome`).

Twelve is still more than "a few". The reviewer checked every outcome against the test and found none over-called. State acts count where the rule names "law" (the Conventicle Act of 1664; Catherine II's decree of 1795). The Kyiv move of 1686 changed a settlement and was carried out, though no link type names a transfer of jurisdiction (Open-Gaps, "No link type for a transfer of jurisdiction", 2026-11-08). Every outcome's evidence lies inside a quote cited on its link.


## Merges with other passes

- The major-links pass (mchadwick25-droid/CIC-Project#1543, data release 10), era 6 (#1544, release 11) and era 7 (#1546, release 12) merged first; this pass took 13, in the order the era 1 thread set for the open link passes. None of them changed an era-8 movement's text or a link this pass kept or rewrote.
- Era 6 published `hesychasm-and-the-palamite-synthesis--the-hesychast-revival-paisius-and-the-philokalia` first, as this pass drafted it. The published version stands.
- Era 7 published 13 links first on the same IDs. The published versions stand. Ten agree with this pass on type. Three do not (Czech churches to the Moravians; Anabaptists and Baptists; the Russian church before Nikon to the Old Believers), and are logged for P2-L11 (Open-Gaps, "Era 7 and era 8 typed three links differently", 2026-11-08).
- Era 7's `armenian-christianity-new-julfa--armenian-christianity-era-8` rests on the Apostolic catholicoi; the Armenian Apostolic movement Mark ruled for will take it over (Open-Gaps, "The Armenian line after the new movement", 2026-11-08).
- Every dropped draft is in `Final.json` with `action: "drop"` and its reason.

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08):
- No Armenian Apostolic movement for 1650-1815. Ruled by Mark the same day: add one, in its own pull request.
- No movement owns English Unitarianism (with the Swedenborgian exchange with Priestley). For Mark.
- No link type for a transfer of jurisdiction. A method question, for Mark.
- The Society of Jesus ends in 1650. For the era 7 owner and Mark.
- Build wording in other eras' public text, found in era 8. For P2-L11.
- Page recordings read the old descriptions, era 8 (four pages). A paid voice run, for Mark.
- Held for later link passes, from era 8.
- Well-known facts with no vendored source, era 8.
- Era 7 and era 8 typed three links differently. For P2-L11.
- The Armenian line after the new movement.

## Wanted texts

72 in all, in `Drafting_Record.json` (`wants`, tagged by group). Those that would lift a link or restore a claim:
- Bernardo da Gallo's and Lorenzo da Lucca's Capuchin reports on Dona Beatriz (1706-10): the only contemporary record of the Antonian movement.
- The Conventicle Act of 1664 from Statutes of the Realm, to replace Whitley's summary.
- Benedict XIII's briefs of 1725 against the Utrecht election; Clement XI's bull of 1708 against Port-Royal.
- The acts of the Moscow council of 1666-67; the Edinoverie rules of 1800; the patriarchal letters of 1686-87 on Kyiv.
- Benedict XIV's 1742 act for the Armenian Catholic patriarchate; the 1766-67 acts abolishing Peć and Ohrid.
- A Church of England record of the Methodist separation; any nineteenth-century Methodist or Quaker text after 1815.
- Backus's History of New-England (the Separates who became Baptists); Calamy or Palmer on the ministers ejected in 1662.
- Nicole's Réfutation des quiétistes (1695); Wesley's Extract of the Life of Madame Guion (1776).

## Two-way check

Every relationship named in an era-8 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it is not a relationship claim (per relationship: `Final.json`, `dispositions`). Round 1 found no unlinked relationship still stated as fact.

### Major links by outcome (12)

| Link | Type | Kind | Outcome | Evidence |
|---|---|---|---|---|
| `restoration-georgian-church-of-england--the-baptists` | argued against | council-law | A law of 1664 banned any religious meeting of more than four people that did not follow the ways of the Church of England. | `general-baptist-assembly_minutes-v1-1654-1728_whitley1909.txt` 10246-10249 |
| `catholic-church-ancien-regime--port-royal-jansenism` | argued against | council-law | In 1653 Rome condemned five points from Jansen's book, and in 1664 it made people swear to a form that rejected them. | `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` 21920-21922 |
| `catholic-church-ancien-regime--quietist-controversy-molinos-guyon` | argued against | council-law | In 1687 Rome condemned errors drawn from Molinos, and in 1699 it condemned 23 claims from a book by Fénelon. | `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` 22846-22848 |
| `church-of-the-desert-huguenots--camisard-prophetism` | argued against | council-law | In 1715 the first synod of the Cévennes preachers banned women from preaching and threw out the revelations then in vogue. | `french-reformed-synods_synodes-du-desert-t1-fra_hugues1885.txt` 2949-2953 |
| `catholic-church-ancien-regime--the-society-of-jesus` | argued against | council-law | In 1773 Pope Clement XIV shut down the Society of Jesus, after the kings of France, Spain, Portugal and Sicily had thrown it out. | `clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt` 1362-1366 |
| `russian-church-nikon-to-holy-synod--the-old-believers--2` | argued against | council-law | A Moscow church council, with two Eastern patriarchs on it, laid a solemn curse on Avvakum and the priest Lazar. | `subbotin_materialy-dlia-istorii-raskola-v2-dokumenty-rus_1875.txt` 998-999 |
| `russian-church-nikon-to-holy-synod--the-old-believers--3` | in contact with | rule-changed | In 1800 Tsar Paul I approved terms that let Old Believers who joined the official church keep using the old books. | `conybeare_russian-dissenters_1921.txt` 5535-5538 |
| `russian-church-nikon-to-holy-synod--the-kyiv-mohyla-orthodox-revival` | in contact with | rule-changed | Two Eastern patriarchs confirmed by letter that the church of Kyiv now came under the patriarch of Moscow. | `mouravieff_history-of-the-church-of-russia_blackmore1842.txt` 11424-11427 |
| `russian-church-nikon-to-holy-synod--ruthenian-uniate-18th-century` | argued against | council-law | In 1795 Catherine II ruled that all those whose families had joined the union after 1595 must go back to the Russian church. | `pelesz_geschichte-der-union-bd2-deu_1880.txt` 41250-41254 |
| `orthodoxy-under-the-ottomans-1650-1821--the-reformed-cities-zurich-and-geneva` | argued against | council-law | In 1672 the Synod of Jerusalem met against the Calvinists and ruled that their faith could not be the faith of the Eastern Church. | `dositheus_acts-and-decrees-synod-jerusalem_robertson1899.txt` 579-583 |
| `catholic-church-ancien-regime--melkite-greek-catholic-church` | in contact with | rule-changed | In 1729 Rome said Cyril could be patriarch if he swore to change no Greek rites without its leave, and its envoy confirmed him in 1730. | `mansi_sacrorum-conciliorum-collectio-tomus-46-synodi-melchitarum-lat_petit1911.txt` 10444-10455 |
| `armenian-christianity-era-8--catholic-church-ancien-regime` | in contact with | split | In 1742 Pope Benedict XIV gave the Armenians in union with Rome a church of their own, with a patriarch placed under Rome. | `ormanian_church-of-armenia_gregory1912.txt` 4533-4536 |

### Links judged minor (27)

| Link | Type | Why not major |
|---|---|---|
| `german-pietism-spener-francke-halle--the-moravian-church-at-herrnhut` | influenced | Ideas and schooling passed on; no council, split or ruling is shown. |
| `german-pietism-spener-francke-halle--the-methodist-revival` | influenced | Reading and a visit; no institutional act. |
| `the-moravian-church-at-herrnhut--the-methodist-revival` | influenced | Teaching passed person to person; no institutional act. |
| `puritanism--the-methodist-revival` | influenced | Reading and family heritage; no institutional act. |
| `the-methodist-revival--the-holiness-movement` | influenced | A teaching taken up by later writers; no institutional act. |
| `the-evangelical-awakening-in-new-england--the-baptists` | influenced | Carey takes up Brainerd's example in a book; no body acts on it in these sources. |
| `the-methodist-revival--the-evangelical-awakening-in-new-england` | influenced | A practice taken up across parishes; no body or law changed a rule in these sources. |
| `english-old-dissent--the-evangelical-awakening-in-new-england` | influenced | Hymns taken up by readers elsewhere; no institutional act. |
| `the-evangelical-awakening-in-new-england--english-old-dissent` | influenced | London ministers took up and published a text; no institutional act. |
| `english-old-dissent--the-methodist-revival` | in contact with | A single visit; no institutional act. |
| `english-old-dissent--the-baptists` | in contact with | A shared meeting; the meeting had no authority to bind churches, and no split or rule change is shown in this source. |
| `the-methodist-revival--the-welsh-revival-tradition` | in contact with | A meeting of leaders; no institutional act in these sources. |
| `latin-pastoral-congregational-christianity--port-royal-jansenism` | influenced | A teaching taken up by the later side; no institutional act. |
| `port-royal-jansenism--the-society-of-jesus` | argued against | Polemical letters; no council, split or authority's ruling on the link's own sources. |
| `the-society-of-jesus--port-royal-jansenism` | argued against | Sermons and a pamphlet; no institutional act on the link's sources. |
| `port-royal-jansenism--church-of-utrecht` | influenced | Shared teaching and friendships; the institutional break belongs to the link with Rome, not to this one. |
| `port-royal-jansenism--quietist-controversy-molinos-guyon` | in contact with | Private meetings; no institutional act. |
| `quietist-controversy-molinos-guyon--german-pietism-spener-francke-halle` | influenced | A translation; the text was taken up, no institutional act. |
| `quietist-controversy-molinos-guyon--the-quakers-religious-society-of-friends` | influenced | Books sold and read; no institutional act. |
| `quietist-controversy-molinos-guyon--the-methodist-revival` | influenced | A writer read and an extract printed; no institutional act. |
| `camisard-prophetism--the-methodist-revival` | in contact with | A single visit; no institutional act. |
| `camisard-prophetism--shakers` | influenced | A spirit and a way of worship taken up by others; no council, split or authority's ruling is involved. |
| `the-old-believers--russian-church-nikon-to-holy-synod` | argued against | A written protest by prisoners; the cited lines show no council, split into a separate body, or rule changed by the Old Believers' side. |
| `orthodoxy-under-the-ottomans-1650-1821--russian-church-nikon-to-holy-synod` | influenced | A church body adopting another side's text or worship order by its own vote is a text taken up, not a rule changed by an authority (Decision-Log, 'Major links: a church b… |
| `the-tridentine-church--ruthenian-uniate-18th-century` | influenced | A church body adopting another side's text or worship order by its own vote is a text taken up, not a rule changed by an authority (Decision-Log, 'Major links: a church b… |
| `orthodoxy-under-the-ottomans-1650-1821--the-huguenots` | argued against | The synod refutes a French minister's claim about the Eastern Church; its condemnation is of Calvinist teaching as a whole, which the link to Calvin's Geneva carries. |
| `armenian-christianity-era-8--armenian-christianity-zartonk` | influenced | Books and scholarship taken up by a later movement; no council, split or ruling. |

### Prose to links: sentences qualified or removed

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| german-pietism-spener-francke-halle | relationsSummary | qualify | No vendored Pietist text names a Dutch precisian source; Spener's Pia Desideria cites Arndt, not Dutch writers, and the only Dutch tie found (Francke sending Neubauer to… |
| german-pietism-spener-francke-halle | legacy | qualify | Unsupported superlative ('first sustained institutional base') replaced with Halle's documented role in the 1706 Danish mission (Guericke). |
| the-moravian-church-at-herrnhut | relationsSummary | qualify | 'Decades before any other Protestant body' is wrong: Halle's Danish mission reached Tranquebar in 1706. Reworded to 'from 1732 it sent missionaries far overseas'. |
| the-evangelical-awakening-in-new-england | relationsSummary | qualify | No vendored text ties the frontier revivals to the awakening (McNemar's Kentucky Revival, the only vendored text for the later entry, names neither Edwards nor Whitefield… |
| the-evangelical-awakening-in-new-england | relationsSummary | qualify | No vendored text ties the awakening to the first Black congregations. Wheatley's 1770 elegy shows Whitefield's preaching reaching a Black Christian writer, but it falls a… |
| the-evangelical-awakening-in-new-england | longDescription | qualify | 'A great many of them becoming Baptist': no vendored or repo-cited source traces Separates into Baptist churches (Backus's History and the Separate church records are not… |
| the-evangelical-awakening-in-new-england | longDescription | qualify | 'The first substantial body of Christian writing by Black and Native people' is a superlative no vendored source states, and the published works (Occom 1772, Wheatley 177… |
| the-evangelical-awakening-in-new-england | why | qualify | Same correction as the description. |
| the-evangelical-awakening-in-new-england | legacy | qualify | 'Filled the Baptist churches with Separate converts': unsupported, as above. Qualified with the reason. |
| the-evangelical-awakening-in-new-england | legacy | qualify | 'Seeded the first generation of Black and Native Christian writing' reduced to what the texts show; see above. |
| the-welsh-revival-tradition | relationsSummary | qualify | No vendored text from 1904-05 names the eighteenth-century revival or its hymns, and the later entry's own text stresses that its revivals 'none of them descended from th… |
| the-welsh-revival-tradition | legacy | qualify | 'Runs straight on to the revival of 1904-05': qualified, as in the summary. |
| the-baptists | longDescription | qualify | 'Grew explosively out of the awakening': Rippon's 1790 letters show rapid New England Baptist growth (500 added since 1788, lines 8731-8734) but nothing vendored ties it… |
| the-baptists | legacy | qualify | 'Opened the era of Protestant foreign missions' is contradicted by Carey's own Enquiry, which names the Danish mission at Tranquebar (1706), the Moravians and John Eliot… |
| port-royal-jansenism | legacy | qualify | No vendored text ties Jansenism to the Jesuit suppression; the repo-cited Van Kley (1975) is the standard account. Qualified to 'historians hold'. Not linked, for want of… |
| camisard-prophetism | legacy | qualify | 'Later revival movements' named nothing. Qualified to 'may have' with Wesley's 1739 visit to a French prophet, linked at Inferential-Thin. |
| colonial-latin-american-devotional-catholicism | relationsSummary | qualify | No vendored text shows the base communities drawing on colonial piety, and no repo-cited secondary work says so. Qualified as interpretation; no link. |
| colonial-latin-american-devotional-catholicism | legacy | qualify | No vendored text shows the base communities drawing on colonial piety, and no repo-cited secondary work says so. Qualified as interpretation; no link. |
| the-old-believers | legacy | remove | No source in the library for the schism in the nineteenth-century novel. Cut; wants list Melnikov-Pechersky and Dostoevsky. |
| russian-church-nikon-to-holy-synod | legacy | remove | 'The sharp religious searching of Russian literature' has no source in the library; cut, wants listed. |
| the-hesychast-revival-paisius-and-the-philokalia | why | remove | The Way of a Pilgrim is a text, not a movement, and no source in the library shows the tie. Cut; wants list the Kazan edition of 1881. |
| the-hesychast-revival-paisius-and-the-philokalia | legacy | remove | The Way of a Pilgrim and Dostoevsky's novels: no census movements and no source in the library. Cut; wants listed. |
| the-hesychast-revival-paisius-and-the-philokalia | legacy | remove | No source in the library shows the Paris school's use of the Philokalia (twentieth-century texts are outside the public-domain window). Cut rather than linked; the Jesus… |
| orthodoxy-under-the-ottomans-1650-1821 | relationsSummary | remove | The synod answered Calvinists, not Trent; no vendored text has it address Trent. 'Answer to the Council of Trent' removed; the comparison with Western confessions kept. |
| orthodoxy-under-the-ottomans-1650-1821 | legacy | qualify | 'Shaped every Balkan church' has no vendored support and was a fragment. Replaced by Paisii's attested 1762 complaint; no influence link drafted. |
| melkite-greek-catholic-church | legacy | qualify | 'Fixed a pattern' overstated: the pattern predates 1724 (Brest 1596, the Maronites). Now 'one more case of a familiar pattern'. |
| philippine-catholicism-era-8 | legacy | qualify | The national revolution has no entry, and no vendored text ties the clergy question to it; qualified as a common reading. |

### Links to prose

Every link touching an era-8 movement, and where its relationship is named (wording as drafted; the fields named are the current ones).

| Link | Type | Grade | Status | Named in |
|---|---|---|---|---|
| `the-methodist-revival--the-holiness-movement` | influenced | Widely Accepted | rewritten | the-methodist-revival relationsSummary and legacy |
| `the-baptists--the-black-church-in-america` | gave rise to | Widely Accepted | kept | the-baptists relationsSummary ('the Black Baptist churches, which in turn became one of the founding traditions of the Black Church in America') and legacy |
| `the-methodist-revival--the-black-church-in-america` | gave rise to | Documented | rewritten | the-methodist-revival relationsSummary and legacy |
| `melkite-arabic-christianity--melkite-greek-catholic-church` | gave rise to | Dominant Modern Reconstruction | kept | melkite-greek-catholic-church relationsSummary ('the patriarchate of Antioch split'), longDescription ('one Arabic-speaking, Byzantine-rite community') |
| `athonite-and-comnenian-byzantine-monasticism--the-hesychast-revival-paisius-and-the-philokalia` | influenced | Documented | kept | the-hesychast-revival-paisius-and-the-philokalia longDescription and why ('working through its monastery libraries for the old Greek texts on inner prayer') |
| `latin-papal-church-avignon-to-lateran-v--catholic-church-ancien-regime` | influenced | Documented | earlier pass | see that pass's audit |
| `hesychasm-and-the-palamite-synthesis--the-hesychast-revival-paisius-and-the-philokalia` | influenced | Documented | earlier pass | the-hesychast-revival-paisius-and-the-philokalia relationsSummary ('Revival of the Palamite line') (this pass's reading; the published version stands) |
| `muscovite-monastic-christianity--the-old-believers` | influenced | Inferential-Thin | earlier pass | see that pass's audit |
| `the-anabaptist-movements--the-baptists` | influenced | Contested | earlier pass | the-baptists relationsSummary ('historians are divided on how much direct contact there was between the two movements') (this pass's reading; the published version stands) |
| `the-anabaptist-movements--radical-pietism-and-the-brethren-dunkers-ephrata` | influenced | Documented | earlier pass | radical-pietism-and-the-brethren-dunkers-ephrata longDescription and why ('joining Pietist inwardness to Anabaptist convictions'); relationsSummary ('They joined Pietist… (this pass's reading; the published version stands) |
| `the-english-reformation-and-elizabethan-settleme--restoration-georgian-church-of-england` | continued as | Documented | earlier pass | restoration-georgian-church-of-england longDescription and why ('When the monarchy came back in 1660 so did the bishops and the Prayer Book'); the-english-reformation-and… (this pass's reading; the published version stands) |
| `the-huguenots--church-of-the-desert-huguenots` | continued as | Documented | earlier pass | church-of-the-desert-huguenots relationsSummary ('what survived after ... outlawed French Protestantism') and longDescription (this pass's reading; the published version stands) |
| `puritanism--restoration-georgian-church-of-england` | broke with | Documented | earlier pass | see that pass's audit |
| `puritanism--english-old-dissent` | gave rise to | Documented | earlier pass | see that pass's audit |
| `puritanism--the-baptists` | gave rise to | Widely Accepted | earlier pass | the-baptists relationsSummary ('grew out of Puritan-Separatist ferment in England'); puritanism legacy ('much of the Baptist tradition come straight out of it') (this pass's reading; the published version stands) |
| `puritanism--the-evangelical-awakening-in-new-england` | influenced | Documented | earlier pass | the-evangelical-awakening-in-new-england relationsSummary ('grew out of New England Puritanism'); puritanism legacy ('its insistence on personal conversion runs directly… (this pass's reading; the published version stands) |
| `dutch-further-reformation-and-refuge-culture--german-pietism-spener-francke-halle` | influenced | Documented | earlier pass | see that pass's audit |
| `the-remonstrants-and-dort--the-methodist-revival` | influenced | Documented | earlier pass | see that pass's audit |
| `czech-churches-last-century--the-moravian-church-at-herrnhut` | gave rise to | Documented | earlier pass | the-moravian-church-at-herrnhut relationsSummary ('saw itself as the old Bohemian Unity of the Brethren made new', after prose change 4), longDescription and why ('the re… (this pass's reading; the published version stands) |
| `anti-trinitarian-currents-servetus-polish-brethr--early-american-unitarians-universalists` | influenced | Inferential-Thin | earlier pass | see that pass's audit |
| `kongo-christianity-afonso-to-1650--the-antonian-movement-in-kongo` | gave rise to | Inferential-Thin | earlier pass | the-antonian-movement-in-kongo relationsSummary ('Christianity already two centuries African producing its own prophetess'), longDescription and why ('By 1700 the Kingdom… (this pass's reading; the published version stands) |
| `new-spain-and-andes-mission-born-christianity--colonial-latin-american-devotional-catholicism` | continued as | Inferential-Thin | earlier pass | colonial-latin-american-devotional-catholicism relationsSummary ('This continues the earlier missionary Catholicism of Spanish America into its settled, everyday form');… (this pass's reading; the published version stands) |
| `philippine-catholicism--philippine-catholicism-era-8` | continued as | Documented | earlier pass | philippine-catholicism-era-8 relationsSummary ('This continues the story of Philippine Catholicism') (this pass's reading; the published version stands) |
| `the-kyiv-mohyla-orthodox-revival--russian-church-nikon-to-holy-synod` | influenced | Widely Accepted | earlier pass | see that pass's audit |
| `russian-church-stoglav-to-nikon--the-old-believers` | influenced | Documented | earlier pass | the-old-believers relationsSummary ('The Old Believers grew out of Muscovite Christianity') (this pass's reading; the published version stands) |
| `russian-church-stoglav-to-nikon--russian-church-nikon-to-holy-synod` | continued as | Documented | earlier pass | see that pass's audit |
| `the-union-of-brest-and-ruthenian-greek-catholic---ruthenian-uniate-18th-century` | continued as | Widely Accepted | earlier pass | ruthenian-uniate-18th-century longDescription and why ('A century after the Union of Brest, the Greek Catholic church of the Ruthenian lands') (this pass's reading; the published version stands) |
| `armenian-christianity-new-julfa--armenian-christianity-era-8` | continued as | Widely Accepted | earlier pass | see that pass's audit |
| `orthodoxy-under-the-ottomans-parish-millet-and-n--orthodoxy-under-the-ottomans-1650-1821` | continued as | Documented | earlier pass | orthodoxy-under-the-ottomans-1650-1821 relationsSummary ('the second act of Orthodoxy under Ottoman rule', after prose change 0) (this pass's reading; the published version stands) |
| `the-tridentine-church--catholic-church-ancien-regime` | continued as | Documented | earlier pass | see that pass's audit |
| `german-pietism-spener-francke-halle--the-moravian-church-at-herrnhut` | influenced | Documented | new | german-pietism-spener-francke-halle relationsSummary ('It shaped the Moravian Church at Herrnhut', after prose change 0) and legacy ('The Moravians at Herrnhut grew up cl… |
| `german-pietism-spener-francke-halle--the-methodist-revival` | influenced | Documented | new | german-pietism-spener-francke-halle legacy ('John Wesley learned from the Moravians, and in 1738 he went to Halle himself. George Whitefield took Francke's orphan house a… |
| `german-pietism-spener-francke-halle--radical-pietism-and-the-brethren-dunkers-ephrata` | gave rise to | Widely Accepted | new | radical-pietism-and-the-brethren-dunkers-ephrata longDescription ('Where mainstream Pietism stayed inside the Lutheran church, a radical wing walked out of it') and relat… |
| `the-moravian-church-at-herrnhut--the-methodist-revival` | influenced | Documented | new | the-moravian-church-at-herrnhut relationsSummary ('It had a deep effect on John Wesley', after prose change 4) and legacy (Wesley met Moravians at sea and in London); the… |
| `puritanism--the-methodist-revival` | influenced | Widely Accepted | new | the-methodist-revival relationsSummary ('Methodism grew from Puritan piety') |
| `restoration-georgian-church-of-england--the-methodist-revival` | gave rise to | Documented | new | the-methodist-revival relationsSummary ('inside the Church of England') and longDescription ('Church of England priest', 'renew the Church of England from inside') |
| `restoration-georgian-church-of-england--the-methodist-revival--2` | broke with | Widely Accepted | new | the-methodist-revival longDescription ('After his death in 1791 the connexion became a separate church anyway') and legacy ('The British connexion separated from the Chur… |
| `the-methodist-revival--nineteenth-century-methodism` | continued as | Widely Accepted | new | the-methodist-revival legacy ('The British connexion separated ... American Methodism organized itself as a church in 1784'); the census continuesAs field pairs the two |
| `the-quakers-religious-society-of-friends--nineteenth-century-quakerism-separations` | continued as | Widely Accepted | new | the-quakers-religious-society-of-friends legacy ('it divided in the nineteenth century into unprogrammed, evangelical and pastoral branches'); the census continuesAs fiel… |
| `puritanism--the-quakers-religious-society-of-friends` | gave rise to | Documented | new | the-quakers-religious-society-of-friends relationsSummary ('Radical child of the Puritan ferment'; after prose change 3, 'grew out of the most radical edge of the Puritan… |
| `the-baptists--the-missionary-movement-s-native-churches-seramp` | gave rise to | Inferential-Thin | new | the-baptists relationsSummary ('From the Baptists came William Carey's missionary movement'), longDescription and why (Carey's society and his sailing for India); the Ser… |
| `restoration-georgian-church-of-england--the-baptists` | argued against | Documented | new | the-baptists longDescription ('They were persecuted hard under the Restoration — John Bunyan spent twelve years in Bedford gaol') |
| `the-evangelical-awakening-in-new-england--the-baptists` | influenced | Documented | new | the-evangelical-awakening-in-new-england legacy ('the missionary societies ... traced their impulse back to it ... through Edwards's Life of David Brainerd'); the-baptist… |
| `the-methodist-revival--the-evangelical-awakening-in-new-england` | influenced | Documented | new | the-evangelical-awakening-in-new-england longDescription ('When the English preacher George Whitefield toured the colonies from 1739, scattered local revivals became a ge… |
| `english-old-dissent--the-evangelical-awakening-in-new-england` | influenced | Documented | new | english-old-dissent legacy ('Watts's and Doddridge's hymns are sung every week in churches that have never heard of Old Dissent'); longDescription (Watts's hymns) |
| `the-evangelical-awakening-in-new-england--english-old-dissent` | influenced | Documented | new | english-old-dissent relationsSummary and longDescription ('the Congregationalists ... were reinvigorated by the eighteenth-century revival', rewritten in prose changes 7… |
| `english-old-dissent--the-methodist-revival` | in contact with | Documented | new | english-old-dissent relationsSummary and longDescription ('reinvigorated by the eighteenth-century revival', rewritten in prose changes 7 and 8); legacy (Doddridge) |
| `english-old-dissent--restoration-georgian-church-of-england` | broke with | Documented | new | english-old-dissent relationsSummary ('ejected from the Church of England in 1662'), longDescription and why; restoration-georgian-church-of-england relationsSummary and… |
| `english-old-dissent--the-baptists` | in contact with | Documented | new | english-old-dissent relationsSummary ('Together with the Quakers and the Baptists, this tradition makes up the wider family of English Dissent'); Salters' Hall |
| `the-methodist-revival--the-welsh-revival-tradition` | in contact with | Documented | new | the-welsh-revival-tradition relationsSummary ('Sibling of Methodism'); longDescription ('began independently of England') |
| `restoration-georgian-church-of-england--the-welsh-revival-tradition` | broke with | Documented | new | the-welsh-revival-tradition legacy ('It became a church: the Calvinistic Methodists ordained their own ministers in 1811') |
| `restoration-georgian-church-of-england--early-american-unitarians-universalists` | gave rise to | Documented | new | early-american-unitarians-universalists relationsSummary ('King's Chapel in Boston revised its prayer book to remove the Trinity'), longDescription and why ('an Anglican… |
| `early-american-unitarians-universalists--american-unitarianism-universalism-consolidations` | continued as | Documented | new | early-american-unitarians-universalists relationsSummary ('Both threads only became formal denominations later, with the American Unitarian Association founded in 1825'),… |
| `latin-pastoral-congregational-christianity--port-royal-jansenism` | influenced | Documented | new | port-royal-jansenism relationsSummary ('Augustine's long shadow'), longDescription and why ('read Augustine on grace') |
| `port-royal-jansenism--the-society-of-jesus` | argued against | Documented | new | port-royal-jansenism longDescription and why ('Provincial Letters mocked Jesuit moral reasoning'; 'read Augustine on grace harder than the Jesuits ... could tolerate') |
| `the-society-of-jesus--port-royal-jansenism` | argued against | Documented | new | port-royal-jansenism longDescription and why ('harder than the Jesuits ... could tolerate') |
| `catholic-church-ancien-regime--port-royal-jansenism` | argued against | Documented | new | port-royal-jansenism longDescription ('Rome condemned five propositions said to be contained in Jansen's Augustinus ... a formulary') |
| `port-royal-jansenism--church-of-utrecht` | influenced | Widely Accepted | new | church-of-utrecht relationsSummary ('grew out of the Jansenist quarrel') and longDescription ('absorbed a good deal of the Jansenist temper'); port-royal-jansenism legacy… |
| `catholic-church-ancien-regime--church-of-utrecht` | broke with | Documented | new | church-of-utrecht relationsSummary ('without Rome's approval'), longDescription and why ('Rome refused for years to confirm'; 'a permanent breach with the papacy'); port-… |
| `church-of-utrecht--old-catholic-churches-union-of-utrecht` | continued as | Documented | new | church-of-utrecht relationsSummary ('became the root of the later Old Catholic Union of Utrecht') and legacy ('the Declaration of Utrecht in 1889'); port-royal-jansenism… |
| `port-royal-jansenism--quietist-controversy-molinos-guyon` | in contact with | Documented | new | quietist-controversy-molinos-guyon relationsSummary ('Adjacent to Port-Royal's tradition', rewritten in prose change 0) |
| `catholic-church-ancien-regime--quietist-controversy-molinos-guyon` | argued against | Documented | new | quietist-controversy-molinos-guyon longDescription and why ('sixty-eight propositions ... condemned in 1687'; 'an implacable opponent in Bossuet'; 'condemned by Rome in 1… |
| `quietist-controversy-molinos-guyon--german-pietism-spener-francke-halle` | influenced | Documented | new | quietist-controversy-molinos-guyon legacy ('read warmly by Pietists', rewritten in prose change 1) |
| `quietist-controversy-molinos-guyon--the-quakers-religious-society-of-friends` | influenced | Widely Accepted | new | quietist-controversy-molinos-guyon legacy ('read warmly by ... Quakers', rewritten in prose change 1) |
| `quietist-controversy-molinos-guyon--the-methodist-revival` | influenced | Documented | new | quietist-controversy-molinos-guyon legacy ('read warmly by ... Methodists', rewritten in prose change 1) |
| `the-huguenots--camisard-prophetism` | gave rise to | Documented | new | camisard-prophetism relationsSummary ('Aftermath of the Huguenot tradition's suppression'), longDescription and why ('After Louis XIV outlawed Protestantism in 1685') |
| `church-of-the-desert-huguenots--camisard-prophetism` | argued against | Documented | new | church-of-the-desert-huguenots longDescription ('discouraged the prophesying that had led to the Camisard rising') and relationsSummary ('The Camisard prophetic uprising… |
| `camisard-prophetism--the-methodist-revival` | in contact with | Inferential-Thin | new | camisard-prophetism legacy ('echoes reaching later revival movements', made concrete in prose change 3) |
| `catholic-church-ancien-regime--the-society-of-jesus` | argued against | Documented | new | catholic-church-ancien-regime relationsSummary ('the expulsion and suppression of the Jesuits between 1759 and 1773'; 'the Jesuits restored in 1814'), longDescription, wh… |
| `catholic-church-ancien-regime--catholic-church-long-nineteenth-century` | continued as | Documented | new | catholic-church-ancien-regime legacy ('what emerged after 1815'; 'what emerged after 1815'; after prose change 2, 'The same line of popes carried it into the nineteenth c… |
| `restoration-georgian-church-of-england--victorian-church-of-england` | continued as | Documented | new | restoration-georgian-church-of-england legacy ('It continues as the Church of England'; 'the 1662 Prayer Book, still the church's legal standard'); its continuesAs field |
| `camisard-prophetism--shakers` | influenced | Documented | new | shakers relationsSummary (after prose change 0: 'taken up the spirit of the French Prophets'); camisard-prophetism longDescription ('some of the prophets escaped to Londo… |
| `the-quakers-religious-society-of-friends--shakers` | gave rise to | Documented | new | shakers relationsSummary (after prose change 0: 'They had left the Quakers'); longDescription and why ('a small group of dissenters in Manchester') |
| `russian-church-nikon-to-holy-synod--the-old-believers` | broke with | Documented | new | the-old-believers relationsSummary ('the enduring counterpart to the official church's Nikonian reforms') and longDescription ('a great part of the Russian church refused… |
| `russian-church-nikon-to-holy-synod--the-old-believers--2` | argued against | Documented | new | the-old-believers longDescription ('the council of 1666-67 anathematized them') and why ('was anathematized for it in 1666'); russian-church-nikon-to-holy-synod longDescr… |
| `the-old-believers--russian-church-nikon-to-holy-synod` | argued against | Documented | new | the-old-believers longDescription ('a church they concluded had fallen') and why ('refused to accept it as a mere detail') |
| `russian-church-nikon-to-holy-synod--the-old-believers--3` | in contact with | Dominant Modern Reconstruction | new | the-old-believers relationsSummary ('Edinoverie, established in 1800, sits on the boundary shared between the two churches'); russian-church-nikon-to-holy-synod relations… |
| `orthodoxy-under-the-ottomans-1650-1821--russian-church-nikon-to-holy-synod` | influenced | Documented | new | russian-church-nikon-to-holy-synod longDescription ('to correct Russian service books against Greek models'); the-old-believers longDescription ('against contemporary Gre… |
| `russian-church-nikon-to-holy-synod--the-kyiv-mohyla-orthodox-revival` | in contact with | Dominant Modern Reconstruction | new | russian-church-nikon-to-holy-synod relationsSummary ('in 1686 the Kyiv metropolia was transferred into this church's jurisdiction') |
| `russian-church-nikon-to-holy-synod--alaskan-mission-herman-veniaminov` | gave rise to | Inferential-Thin | new | russian-church-nikon-to-holy-synod relationsSummary ('In 1794 it sent the Valaam mission to Alaska, including Herman of Kodiak'), longDescription, why and legacy ('Its Al… |
| `russian-church-nikon-to-holy-synod--the-optina-elders-and-russian-ascetic-renewal` | gave rise to | Documented | new | russian-church-nikon-to-holy-synod legacy (after prose change 1: 'The first elders of Optina, in the following century, were trained in this church's own monasteries'; fo… |
| `russian-church-nikon-to-holy-synod--russian-church-synodal-century` | continued as | Documented | new | russian-church-nikon-to-holy-synod legacy ('The synodal arrangement lasted until 1917') |
| `russian-church-nikon-to-holy-synod--ruthenian-uniate-18th-century` | argued against | Dominant Modern Reconstruction | new | ruthenian-uniate-18th-century relationsSummary ('forced-reversion campaigns of 1794-96 stripped away most of its parishes'), longDescription and why ('campaigns of forced… |
| `the-hesychast-revival-paisius-and-the-philokalia--the-optina-elders-and-russian-ascetic-renewal` | gave rise to | Documented | new | the-hesychast-revival-paisius-and-the-philokalia relationsSummary ('direct source of the Optina tradition'), why and legacy (after prose changes 2 and 3) |
| `ruthenian-uniate-18th-century--ruthenian-greek-catholic-polotsk-to-galicia` | continued as | Documented | new | ruthenian-uniate-18th-century relationsSummary ('Austrian Galicia became the church's real zone of survival') and legacy ('The Galician remnant ... The Ukrainian Greek Ca… |
| `the-tridentine-church--ruthenian-uniate-18th-century` | influenced | Documented | new | ruthenian-uniate-18th-century relationsSummary ('importing Latin devotional practices into its Byzantine rite') and longDescription and why ('importing Roman devotional p… |
| `orthodoxy-under-the-ottomans-1650-1821--the-reformed-cities-zurich-and-geneva` | argued against | Documented | new | orthodoxy-under-the-ottomans-1650-1821 longDescription and why ('answering the Calvinist ideas'), relationsSummary after prose change 0 |
| `orthodoxy-under-the-ottomans-1650-1821--the-huguenots` | argued against | Documented | new | orthodoxy-under-the-ottomans-1650-1821 relationsSummary ('answered French Calvinists', after prose change 0) |
| `orthodoxy-under-the-ottomans-1650-1821--orthodoxy-after-1821-balkan-autocephalies` | continued as | Documented | new | orthodoxy-under-the-ottomans-1650-1821 legacy ('each took its own church with it', after prose change 1); relationsSummary (Gregory V's hanging) |
| `melkite-greek-catholic-church--orthodoxy-under-the-ottomans-1650-1821` | broke with | Documented | new | melkite-greek-catholic-church relationsSummary, longDescription, why ('Constantinople refused to accept him and consecrated a rival'); legacy (the two churches side by si… |
| `catholic-church-ancien-regime--melkite-greek-catholic-church` | in contact with | Documented | new | melkite-greek-catholic-church longDescription ('recognized by the pope in 1729') and why ('Rome recognized Cyril's line in 1729') |
| `armenian-christianity-era-8--catholic-church-ancien-regime` | in contact with | Documented | new | armenian-christianity-era-8 relationsSummary, longDescription, why ('Benedict XIV confirmed Abraham Petros I as Catholic patriarch of Cilicia') |
| `armenian-christianity-era-8--armenian-christianity-zartonk` | influenced | Widely Accepted | new | armenian-christianity-era-8 legacy ('laid much of the groundwork for the nineteenth-century Armenian cultural revival, the Zartonk') |
| `philippine-catholicism-era-8--philippine-catholicism-gomburza-to-aglipay` | continued as | Widely Accepted | new | philippine-catholicism-era-8 relationsSummary ('building toward the crisis of 1872'); legacy (Gomburza, after prose change 4) |
