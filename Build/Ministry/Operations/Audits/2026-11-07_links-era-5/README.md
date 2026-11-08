# Church Family Tree links, era 5 (P2-L5) — 2026-11-07

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Method unchanged from `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`. Eras 1 and 2 (`../2026-11-07_links-era-1/`, `../2026-11-07_links-era-2/`) were the precedent; their wanted-texts lists were checked first. The work ran on 2026-11-07 and 2026-11-08; later files carry the second date.

## Rounds

1. **Inventory** (Haiku): `Inventory.json`. 27 movements, 241 named relationships, no raw movement IDs in the text. It left out relationships carried by persons; the drafters were told to read each movement's four fields themselves and added those.
2. **Draft** (Opus, six groups of four or five movements): `Draft_GroupA.json` to `Draft_GroupF.json`, merged in `Drafting_Record.json`. Two links were drafted twice (the papacy and the Franciscans; Athos and the Georgian golden age), and one link no text field names was dropped. The merge notes say which draft was kept and why. Each drafter scored its own notes and paragraphs, so there was no separate prose pass.
3. **Review round 1** (separate Opus agent, full review): `Opus_Review_Round1.json`. Revise: 0 blocking, 7 substantial, 14 minor, no fabrication. The substantial findings were three over-grades (Dominicans and Carmelites; Cilicia across 1300; Lyon 1274), a second "argued against" on the papacy and Byzantine pair, two prose overstatements (Serbian and Bulgarian "grew out of Athos"; build narration in the Coptic legacy) and the Observants with no link.
4. **Revision** (Opus): `Revision_Round1.json`. All 21 findings and 5 two-way gaps fixed: 1 link added, 16 rewritten, 1 dropped, 18 prose changes. On five findings the reviser improved on the proposed fix and said why. For Cilicia, a primary the reviewer had not used (the continuation of Sempad's chronicle, 1321-22) shows the see at Sis after 1300, so that link stays Documented.
5. **Review round 2** (separate Opus agent, targeted recheck): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 1 substantial, 3 minor. The substantial finding: the Observant link drawn in revision joined two era-6 movements, outside this pass. It was dropped and held for P2-L6 (Open-Gaps, "The Franciscan order and the Observants, held for P2-L6", 2026-11-08). The era-5 Franciscan text now rests on a new Documented link from the Franciscan movement to the Observants. The minor findings removed "we hold" wording from 16 notes and paragraphs.
6. **Revision** (applied by script, as written): `Revision_Round2.json`.
7. **Review round 3** (separate Opus agent, targeted recheck): `Opus_Review_Round3_TargetedRecheck.json`. 0 blocking, 0 substantial, 1 minor: two more notes with "we hold", missed by round 2's list. The two replacements were applied as the reviewer wrote them, a straight string swap, with no further round.

All three rounds of the cap used. No finding is open.

## Counts

- Links touching an era-5 movement: 73. This pass added 55 and changed 2; 15 came from the era 4 pass (merged first, as data release 8), and 1 was already on main. No link retired; every published ID stands.
- Census links in all: 225 before era 4, 266 after it, 321 after this pass. Data release 9 (2026-11-08).
- Grades of the links this pass added: Documented 35, Dominant Modern Reconstruction 9, Inferential-Thin 5, Widely Accepted 4, Contested 2.
- Dispositions of the named relationships (drafting, 340): link 163, out-of-scope 82, no-entry 56, qualify 29, remove 10. "no-entry" means the other party has no census movement; its claim was still checked, and qualified where no vendored or repo-cited source supports it.
- Prose: 57 movement fields changed across drafting and both revisions. Every changed paragraph scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn`; so does every new or rewritten link note (`Readability_Scores.json`, drafting scores; the revision files carry their own).
- Quote check: `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors. Every primary quote appears verbatim at its stated lines. Several quotes keep OCR errors exactly as printed (e.g. "pefiit", Denzinger's margin numbers); each is noted in the link's drafting flags.

## Merge with era 4

Era 4's pass (mchadwick25-droid/CIC-Project#1541) merged first and took data release 8; this pass took 9. Both passes drafted the same nine links between an era-4 and an era-5 movement. Era 4's versions were already published, so they stand and this pass's drafts of them were set aside. Eight agree with this pass on type; the ninth, from the iconophile monks to Athos, is "continued as" in era 4's version and was "influenced" here, both at Inferential-Thin. The Athonite summary ("Perhaps heir of the monks who fought for icons, though the tie is thin") fits either. Era 4 also logged "The Georgian Golden Age says 'silent since 622'"; this pass had already removed the claim, and Open-Gaps records the closure.

## Two-way check

### Prose to links

Every relationship named in an era-5 movement's `relationsSummary`, `longDescription`, `why` or `legacy` has a link, or its sentence was qualified or removed, or it names no census movement, or it is not a relationship claim (per-relationship record: `Drafting_Record.json`, `dispositions`). Round 1 found five gaps (the Observants; the Dominican and Carmelite link named in neither text; the emperor's backing of the Lavra stated as fact; the Cluny disagreement with era 4; the Dominican-Carmelite note). All were closed in revision, or logged where they belong to another era's entry.

Five texts were wrong, not just unsupported, and each was fixed in about a sentence: the Cistercians as "reform child of Cluny"; the Athonite rules adapted by Georgian, Serbian, Bulgarian and Russian founders; the Greek patriarch of Jerusalem "expelled in 1099"; Sava joining his father on Athos (it was the other way round); Ghazan's conversion "within a generation" of Yahballaha's death (it was 1295, in his lifetime).

Sentences qualified or removed in drafting:

| Movement | Field | Disposition | Reason |
|---|---|---|---|
| cistercian-monasticism | relationsSummary | remove | Descent from Cluny misstates the founding (the founders left Molesme) and no vendored text supports any Cistercian-Cluny tie. Wanted: Bernard's Apologia, Exordium Parvum. |
| cistercian-monasticism | longDescription | remove | 'Cluny and the other rich houses above all' removed; no vendored source. |
| cistercian-monasticism | why | remove | 'Left Cluny's own tradition behind' removed; the founders left Molesme and no vendored text ties them to Cluny. |
| carthusian-life | relationsSummary | remove | No vendored text links the Carthusians to the desert monks. Wanted: Guigo I, Consuetudines (PL 153). |
| athonite-and-comnenian-byzantine-monasticism | legacy | remove | No vendored text shows Serbian or Bulgarian founders adapting Athonite charters (the Miklosich charters are vendored but the OCR is too poor to locate or quote). Removed from this entry; the Serbian … |
| the-beguines | longDescription | qualify | Inventory's 'no census entry' corrected: the council was Clement V's, so the Avignon papal church carries it. Vendored texts show only the condemnation of errors laid on beguines and beghards; the de… |
| the-beguines | why | qualify | As in the long description. |
| free-spirit-heresy | longDescription | qualify | New Documented argued-against link from the decree's own errors (Denzinger 471-478). The sentence quoted 'sect of the Free Spirit' as the decree's words; the vendored edition names beguines and begha… |
| free-spirit-heresy | why | qualify | As in the long description; paragraph rewritten whole for reading level. |
| the-humiliati | relationsSummary | qualify | The condemning party is the papacy (Lucius III), not the Waldensians; the Waldensians are a fellow defendant, so no Humiliati-Waldensian link (no meeting or exchange is claimed). The naming of the Hu… |
| the-humiliati | longDescription | qualify | As in the summary. |
| the-humiliati | why | qualify | As in the long description. |
| the-waldensians | longDescription | qualify | 'Without a break' outruns the Contested Alps-to-1532 step and the census's own note of a 1300-1517 gap. |
| the-waldensians | why | qualify | The joining is carried by the chain; 'straight into' claimed unbroken continuity and is qualified. The inventory's second row for this sentence ('the Reformation', no entry) is the same claim. |
| the-waldensians | legacy | remove | Italy's Methodists have no census entry, and no vendored or repo-cited source carries the union. The clause is removed (see the prose change). |
| joachimite-current | legacy | remove | The Florensians have no census entry, and their absorption is in no vendored or repo-cited source. Clause removed. |
| maronite-christianity | legacy | qualify | An influence claim on later Eastern Catholic churches (no single census movement; the Melkite Greek Catholic entry of era 8 calls the Maronite union 'kin-shape'). No vendored or repo-cited source sho… |
| latin-papal-church-gregorian | longDescription | qualify | No census movement for the emperors. Dictatus Papae 12 (Mirbt line 11202-11203) says the pope may depose emperors; 'alone' is not in that clause. Made exact. |
| latin-papal-church-gregorian | longDescription | qualify | No census movement for Henry IV. Gregory VII's own report (Mirbt no. 236, lines 10429-10431) has Henry, then king, barefoot and in wool for three days before the castle gate; no vendored text mention… |
| latin-papal-church-gregorian | longDescription | qualify | The plural takes in the Dominicans. No vendored or repo-cited source shows Innocent III approving them; their own entry dates their approval to 1216, after Innocent's death. The sentence now names Fr… |
| latin-papal-church-gregorian | why | qualify | As in the description: 'may depose emperors', and barefoot for three days with no snow. |
| latin-church-of-outremer | legacy | qualify | 'Eastern Christians' as a whole has no movement, and the vendored witnesses disagree: Michael the Syrian (the Greek patriarch thrown out of Antioch) and Kirakos (friendship of the Franks of Jerusalem… |
| byzantine-church-after-1054 | longDescription | qualify | What the two men believed has no vendored or repo-cited source. Rewritten to 'It was not yet a final break', which the documented union talks of 1274 support. |
| serbian-and-bulgarian-medieval-monasticism | relationsSummary | qualify | 'Children of Byzantium' beyond Athos has no vendored source (Sava's consecration in 1219 at Nicaea is not in a text we hold). The rewritten sentence names Byzantine monasticism on Athos only. |
| serbian-and-bulgarian-medieval-monasticism | relationsSummary | qualify | 'Carried hesychasm into the Slavic lands': no vendored or repo-cited source. Qualified with the reason ('may also have ... no text we hold yet shows it'). |
| serbian-and-bulgarian-medieval-monasticism | relationsSummary | remove | 'Fixes the Slavic lane's Kyiv-to-Moscow jump' is a note about the map's layout, not a historical claim. Removed. The inventory's two 'contact' rows (Kyiv, Moscow) come from this phrase. |
| serbian-and-bulgarian-medieval-monasticism | longDescription | qualify | Hesychast prayer passing from Greek into Slavonic: no vendored or repo-cited source. Qualified with the reason. |
| serbian-and-bulgarian-medieval-monasticism | longDescription | qualify | 'And from there eventually to Russia': no vendored or repo-cited source. Qualified in the same sentence. |
| serbian-and-bulgarian-medieval-monasticism | why | qualify | Hesychast prayer into the Slavic world: qualified, no source. |
| serbian-and-bulgarian-medieval-monasticism | why | qualify | 'Eventually reaching Russia': qualified, no source. |
| serbian-and-bulgarian-medieval-monasticism | legacy | qualify | 'Traveled north and shaped Russian church life for centuries': no vendored or repo-cited source. Qualified with the reason. |
| serbian-and-bulgarian-medieval-monasticism | legacy | qualify | 'The hesychast spirituality carried inside them': qualified in the same sentence. |
| the-georgian-golden-age | relationsSummary | remove | 'Restoring a tradition silent since 622' comes from the map survey written before the census had any Georgian entry after 609. The Tao-Klarjeti entry now covers c. 780-1000, so the claim is wrong as … |
| zagwe-and-early-solomonic-ethiopian-christianity | longDescription | qualify | Jerusalem here is a place, not a movement; jerusalem-liturgical-pilgrimage-christianity (325-450) is not the party (inventory's guess corrected). The 'unreachable' claim has no vendored support; narr… |
| zagwe-and-early-solomonic-ethiopian-christianity | why | qualify | As in the longDescription. |
| coptic-christianity-fatimid-to-mamluk | legacy | qualify | Ethiopian reception: the Ethiopian party is unclear (the date of the Ge'ez Fetha Nagast is in no vendored text, so neither the-ethiopian-monastic-flowering nor a later Ethiopian movement can be chose… |
| syriac-renaissance | legacy | qualify | 'The Syriac churches' is no single movement. No vendored or repo-cited source shows the works staying standard for centuries; the reception clause is removed and the works kept. |
| syriac-renaissance | legacy | remove | 'Later Syriac writers kept looking back' has no vendored or repo-cited support and names no movement; removed. The 'last great flowering' judgment is kept as a general reckoning. |
| church-of-the-east-under-the-mongols | legacy | qualify | Islam is no census movement. The timing was wrong: Ghazan turned to Islam in 1295, in Yahballaha's lifetime (History, Budge 8449-8460 and 8768; Chabot 1895 note, line 7040). Corrected. |

### Links to prose

Every link touching an era-5 movement, and where its relationship is named:

| Link | Type | Grade | Status | Named in |
|---|---|---|---|---|
| `latin-papal-church-gregorian--byzantine-church-after-1054` | argued against | Documented | changed | latin-papal-church-gregorian relationsSummary ('the western side of the Great Schism ... in lasting tension with the Byzantine church') |
| `byzantine-church-after-1054--latin-papal-church-gregorian` | broke with | Documented | changed | latin-papal-church-gregorian relationsSummary ('the western side of the Great Schism') |
| `the-waldensians--waldensians-in-the-alps` | continued as | Widely Accepted | kept | the-waldensians relationsSummary ('joins the Reformed tradition in 1532'), longDescription ('survived in the Alpine valleys ... for three and a half centuries'), why, legacy ('never disappeared'); co… |
| `carolingian-reform-christianity--latin-papal-church-gregorian` | influenced | Widely Accepted | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `cluniac-reform-monasticism--latin-papal-church-gregorian` | in contact with | Documented | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `kievan-rus-christianity--kievan-rus-christianity-1054-1240` | continued as | Dominant Modern Reconstruction | era 4 pass | (era 4 version stands; also drafted here) kievan-rus-christianity-1054-1240 relationsSummary ('A continuation of Rus' Christianity's first generations') and longDescription; kievan-rus-christianity l… |
| `byzantine-imperial-church-macedonian--byzantine-church-after-1054` | continued as | Documented | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `iconophile-byzantine-monasticism--athonite-and-comnenian-byzantine-monasticism` | continued as | Inferential-Thin | era 4 pass | (era 4 version stands; also drafted here) athonite relationsSummary ('Likely heir of the monks who fought for icons', after prose change 7); iconophile-byzantine-monasticism relationsSummary ('parent… |
| `iconophile-byzantine-monasticism--kievan-rus-christianity-1054-1240` | influenced | Dominant Modern Reconstruction | era 4 pass | (era 4 version stands; also drafted here) kievan-rus-christianity-1054-1240 longDescription and why ('gave it a Byzantine rule'); iconophile-byzantine-monasticism legacy ('Theodore's reorganization o… |
| `bogomils--cathars-albigensians` | influenced | Contested | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `bogomils--balkan-bogomil-continuation` | continued as | Dominant Modern Reconstruction | era 4 pass | (era 4 version stands; also drafted here) balkan-bogomil-continuation relationsSummary ('A continuation of an earlier Bogomil current'), longDescription and why ('The Bogomils began in tenth-century … |
| `church-of-the-east-under-the-abbasids--church-of-the-east-under-the-mongols` | continued as | Documented | era 4 pass | (era 4 version stands; also drafted here) church-of-the-east-under-the-mongols longDescription and why ('had spread far into Central Asia centuries earlier ... the Kerait ... already Christian in thi… |
| `syriac-orthodox-under-islam--syriac-renaissance` | continued as | Documented | era 4 pass | (era 4 version stands; also drafted here) syriac-renaissance relationsSummary ('The West Syriac church's intellectual summit') and longDescription/why ('The Syriac Orthodox Church lived under Muslim … |
| `coptic-christianity-under-early-islam--coptic-christianity-fatimid-to-mamluk` | continued as | Documented | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `post-aksumite-ethiopian-christianity--zagwe-and-early-solomonic-ethiopian-christianity` | continued as | Documented | era 4 pass | (era 4 version stands; also drafted here) zagwe relationsSummary ('Continuation of Aksum') and longDescription ('After the old Aksumite kingdom faded ... went on doing what it had done for eight hund… |
| `bagratid-armenian-christianity--armenian-cilicia` | continued as | Documented | era 4 pass | (era 4 version stands; also drafted here) armenian-cilicia relationsSummary ('The Armenian church in exile became a kingdom's church: the catholicosate moved to the fortress of Hromkla in 1151') and … |
| `georgian-revival-tao-klarjeti--the-georgian-golden-age` | continued as | Dominant Modern Reconstruction | era 4 pass | (era 4 version stands; also drafted here) the-georgian-golden-age relationsSummary ('A continuation of the Georgian church'); georgian-revival-tao-klarjeti relationsSummary and legacy ('leads directl… |
| `athonite-and-comnenian-byzantine-monasticism--georgian-revival-tao-klarjeti` | in contact with | Dominant Modern Reconstruction | era 4 pass | named in the era 4 movement text; see the era 4 audit |
| `cistercian-monasticism--the-english-mystics-and-devout` | influenced | Documented | new | cistercian-monasticism relationsSummary ('Bernard's writings fed later Western prayer') and legacy ('the English writers Richard Rolle and Walter Hilton still quoted Bernard by name'), both after pro… |
| `canons-regular-victorine-school--the-english-mystics-and-devout` | influenced | Documented | new | canons-regular-victorine-school legacy ('so did the English mystics of the fourteenth century', after prose change 6; the old 'nearly everyone who wrote on prayer in the later Middle Ages' is kept an… |
| `canons-regular-victorine-school--the-franciscan-movement` | influenced | Widely Accepted | new | canons-regular-victorine-school legacy ('Bonaventure followed Richard closely', after prose change 6; the old text read 'Bonaventure most of all') |
| `carthusian-life--the-english-mystics-and-devout` | influenced | Inferential-Thin | new | carthusian-life legacy ('put into English in the fourteenth century ... The author of The Cloud of Unknowing seems to have known them', after prose change 5) |
| `early-benedictine-italian-monasticism--cistercian-monasticism` | influenced | Inferential-Thin | new | cistercian-monasticism longDescription and why ('to keep the Rule of St Benedict'), relationsSummary ('A plainer reform of Benedictine life', after prose change 0); early-benedictine-italian-monastic… |
| `athonite-and-comnenian-byzantine-monasticism--hesychasm-and-the-palamite-synthesis` | influenced | Documented | new | athonite relationsSummary ('its way of prayer fed hesychasm'), longDescription and why (the disciplines 'the following century would gather up and name hesychasm'), legacy ('fed straight into hesycha… |
| `athonite-and-comnenian-byzantine-monasticism--the-hesychast-revival-paisius-and-the-philokalia` | influenced | Documented | new | athonite legacy ('and in time the Philokalia'); the-hesychast-revival-paisius-and-the-philokalia text (Paisius on Athos; Macarius and Nicodemus on Athos assembling the anthology) |
| `byzantine-imperial-church-macedonian--athonite-and-comnenian-byzantine-monasticism` | influenced | Inferential-Thin | new | athonite longDescription ('with the backing of a Byzantine emperor') and why ('with imperial backing'); not in the inventory |
| `athonite-and-comnenian-byzantine-monasticism--kievan-rus-christianity-1054-1240` | influenced | Dominant Modern Reconstruction | new | athonite legacy ('Anthony, who began the Caves Monastery at Kyiv, had taken his vows on the Holy Mountain', after prose change 8, which replaces 'Russian founders'); kievan-rus-christianity-1054-1240… |
| `athonite-and-comnenian-byzantine-monasticism--the-georgian-golden-age` | influenced | Dominant Modern Reconstruction | new | athonite legacy ('At Iviron, the Georgian house on Athos, monks put scripture and Greek books of theology into Georgian', after prose change 8, which replaces 'Georgian ... founders') |
| `the-carmelites--carmelite-reform-and-spanish-mystics` | influenced | Documented | new | the-carmelites legacy ('The sixteenth-century Spanish reform ... grew directly out of this rule'); carmelite-reform-and-spanish-mystics relationsSummary ('connects to the medieval Carmelite order') |
| `latin-papal-church-gregorian--the-carmelites` | influenced | Documented | new | the-carmelites relationsSummary ('later approved as a formal Rule in 1247'), longDescription and why ('Innocent IV approved the revised Rule in 1247') |
| `the-dominican-order--the-carmelites` | influenced | Inferential-Thin | new | the-carmelites relationsSummary and longDescription ('adapted into a mendicant order alongside the Franciscans and Dominicans') |
| `latin-church-of-outremer--the-carmelites` | influenced | Documented | new | the-carmelites relationsSummary ('received a rule of life from Albert, patriarch of Jerusalem'), longDescription ('asked Albert, the patriarch of Jerusalem — who kept his seat at Acre') |
| `the-dominican-order--the-franciscan-movement` | in contact with | Widely Accepted | new | the-franciscan-movement relationsSummary ('Sibling-rival of the Dominicans'); the-dominican-order relationsSummary ('Sibling-rival of the Franciscans') |
| `latin-papal-church-gregorian--the-franciscan-movement` | in contact with | Documented | new | the-franciscan-movement longDescription ('Pope Innocent III gave the group verbal approval'); latin-papal-church-gregorian longDescription ('authorized the new friars') |
| `the-franciscan-movement--fraticelli-spiritual-franciscan-rigorists` | gave rise to | Documented | new | the-franciscan-movement relationsSummary ('parent of ... Spirituals') and longDescription ('split it into Spirituals and Conventuals'); fraticelli-spiritual-franciscan-rigorists relationsSummary ('Ru… |
| `the-franciscan-movement--franciscan-order-era-6` | continued as | Documented | new | franciscan-order-era-6 relationsSummary ('between the earlier Franciscan movement (ending 1300) and the 1517 division'); the-franciscan-movement relationsSummary (the Observants, via the prose change… |
| `the-dominican-order--rhineland-mysticism-and-the-friends-of-god` | gave rise to | Documented | new | the-dominican-order relationsSummary ('parent of the German convent-mysticism tradition') and legacy ('Their German convents fed the mystical writing associated with Meister Eckhart, Johannes Tauler … |
| `the-dominican-order--cathars-albigensians` | argued against | Documented | new | the-dominican-order longDescription and why ('losing the argument with dissenters' in Languedoc) and legacy ('supplied the church with much of its inquisitorial personnel'). The text does not name th… |
| `latin-papal-church-avignon-to-lateran-v--the-beguines` | argued against | Documented | new | the-beguines relationsSummary ('suppression pressure is part of its own story'), longDescription and why ('the Council of Vienne moved against the beguine life itself', now qualified); free-spirit-he… |
| `latin-papal-church-avignon-to-lateran-v--free-spirit-heresy` | argued against | Documented | new | free-spirit-heresy longDescription and why (the decree of 1312 and its eight errors) |
| `the-beguines--free-spirit-heresy` | gave rise to | Contested | new | free-spirit-heresy relationsSummary ('Beguine suppression used it as a charge'), longDescription and why ('much of it among beguines and beghards') and legacy ('against religious women living outside… |
| `the-tridentine-church--the-humiliati` | argued against | Documented | new | the-humiliati longDescription, why and legacy ('suppressed by papal bull in 1571') |
| `latin-papal-church-gregorian--the-humiliati` | argued against | Inferential-Thin | new | the-humiliati relationsSummary, longDescription and why ('condemned alongside the Waldensians in 1184') |
| `latin-papal-church-gregorian--the-humiliati--2` | in contact with | Dominant Modern Reconstruction | new | the-humiliati longDescription and why ('Pope Innocent III reconciled them in 1201'); latin-papal-church-gregorian longDescription (Innocent III's reign) |
| `latin-papal-church-gregorian--the-waldensians` | argued against | Documented | new | the-waldensians longDescription ('in 1184 the bull Ad abolendam condemned him and his followers'), why ('condemned in 1184 only for preaching without a license'), legacy ('condemned by Rome') |
| `latin-papal-church-gregorian--cathars-albigensians` | argued against | Documented | new | cathars-albigensians relationsSummary ('Target of crusade and inquisition'), longDescription and why ('in 1209 the papacy launched a crusade against them ... then inquisition'), legacy ('the papal in… |
| `balkan-bogomil-continuation--cathars-albigensians` | influenced | Contested | new | balkan-bogomil-continuation relationsSummary ('claimed parent of the Cathars - a claim, not an established line of descent'), legacy ('treated the Bogomils as the source of the Western dualist moveme… |
| `byzantine-church-after-1054--balkan-bogomil-continuation` | argued against | Dominant Modern Reconstruction | new | balkan-bogomil-continuation relationsSummary ('Basil burned in the Hippodrome under Alexios I, Zigabenos wrote against them'), longDescription and why (the Alexios, Anna Komnene and Zigabenos sentenc… |
| `joachimite-current--the-franciscan-movement` | influenced | Documented | new | joachimite-current longDescription ('it spread especially among Franciscans, who found in it a description of their own movement'), why ('spread especially among Franciscans'); not named in the Franc… |
| `joachimite-current--franciscan-order-era-6` | influenced | Documented | new | joachimite-current relationsSummary ('Where it became communal, it lives inside the Franciscan Spirituals' story'), longDescription and why ('carried the expectation on into the bitter Franciscan qua… |
| `latin-papal-church-gregorian--joachimite-current` | argued against | Documented | new | joachimite-current longDescription ('In 1254 a young friar published an Introduction to the Eternal Gospel ... and it was condemned'), why ('a 1254 book making the claim explicit was condemned') |
| `latin-papal-church-gregorian--latin-papal-church-avignon-to-lateran-v` | continued as | Documented | new | latin-papal-church-gregorian legacy ('The same institution continued into the next era through Avignon and the Fifth Lateran Council.') |
| `latin-papal-church-gregorian--latin-church-of-outremer` | gave rise to | Widely Accepted | new | latin-papal-church-gregorian longDescription ('called crusades'); latin-church-of-outremer relationsSummary ('A transplanted Latin church with its own hierarchy') |
| `the-reformed-cities-zurich-and-geneva--latin-papal-church-gregorian` | argued against | Documented | new | latin-papal-church-gregorian legacy ('The Reformation would later protest against these same claims. John Calvin ...', after prose change 3) |
| `cistercian-monasticism--military-religious-orders-templars-hospitallers` | influenced | Dominant Modern Reconstruction | new | military-religious-orders-templars-hospitallers relationsSummary, longDescription and why ('Bernard of Clairvaux wrote their defense, In Praise of the New Knighthood') |
| `latin-papal-church-avignon-to-lateran-v--military-religious-orders-templars-hospitallers` | argued against | Documented | new | military-religious-orders-templars-hospitallers longDescription and why ('In 1312 Pope Clement V abolished the order', after prose changes 9 and 10); latin-papal-church-avignon-to-lateran-v relations… |
| `armenian-cilicia--byzantine-church-after-1054` | in contact with | Documented | new | armenian-cilicia relationsSummary, longDescription and why (Nerses Shnorhali's correspondence with Manuel I about reuniting the Armenian and Greek churches) |
| `armenian-cilicia--latin-church-of-outremer` | in contact with | Documented | new | armenian-cilicia longDescription and why ('negotiating ... with the neighboring Latin crusader states'); latin-church-of-outremer longDescription (its mostly non-Latin population, 'Armenian' among th… |
| `armenian-cilicia--armenian-cilicia-after-the-kingdom` | continued as | Documented | new | armenian-cilicia legacy ('the catholicosate seated here still exists as the Catholicosate of Cilicia', after prose change 11); armenian-cilicia-after-the-kingdom legacy ('The see at Sis ... continues… |
| `latin-church-of-outremer--byzantine-church-after-1054` | argued against | Documented | new | latin-church-of-outremer relationsSummary ('a later one was thrown out in 1170 ... the Schism lived on the ground', after prose change 4), longDescription and why |
| `latin-church-of-outremer--maronite-christianity` | in contact with | Dominant Modern Reconstruction | new | maronite-christianity longDescription and why ('when the crusaders arrived, the Maronites entered into communion with Rome: William of Tyre describes the union around 1182') |
| `latin-papal-church-gregorian--maronite-christianity` | in contact with | Dominant Modern Reconstruction | new | maronite-christianity relationsSummary ('unique early union with Rome'), longDescription and why (Jeremiah al-Amshitti at the Fourth Lateran Council) |
| `byzantine-church-after-1054--byzantine-church-palaiologan` | continued as | Documented | new | byzantine-church-after-1054 legacy ('The same church continued into the next era through the Palaiologan period'); continuesAs |
| `byzantine-church-after-1054--latin-papal-church-gregorian--2` | in contact with | Widely Accepted | new | byzantine-church-after-1054 relationsSummary ('the union with Rome offered at the Council of Lyon in 1274 and then rejected'), longDescription and why |
| `byzantine-church-after-1054--kievan-rus-christianity-1054-1240` | influenced | Dominant Modern Reconstruction | new | kievan-rus-christianity-1054-1240 relationsSummary ('the usual Greek ones sent from Constantinople'), longDescription ('formally a metropolitanate of Constantinople') and why |
| `kievan-rus-christianity-1054-1240--muscovite-monastic-christianity` | gave rise to | Documented | new | kievan-rus-christianity-1054-1240 legacy ('the Muscovy that later claimed it'); muscovite-monastic-christianity relationsSummary ('Child of Kievan + hesychast lines') |
| `athonite-and-comnenian-byzantine-monasticism--serbian-and-bulgarian-medieval-monasticism` | gave rise to | Dominant Modern Reconstruction | new | serbian-and-bulgarian-medieval-monasticism relationsSummary ('Children of Byzantium/Athos'), longDescription, why and legacy (Hilandar); athonite-and-comnenian-byzantine-monasticism legacy ('Athonite… |
| `church-of-the-east-under-the-mongols--latin-papal-church-gregorian` | in contact with | Documented | new | church-of-the-east-under-the-mongols relationsSummary (embassy to Europe), longDescription and why (reaching Rome and the courts of France and England). The latin-papal-church-gregorian text does not… |
| `church-of-the-east-under-the-mongols--church-of-the-east-timur-to-hakkari` | continued as | Documented | new | church-of-the-east-under-the-mongols continuesAs field and legacy ('a mountain remnant in Hakkari'); church-of-the-east-timur-to-hakkari relationsSummary ('Patriarch Yahballaha III died in 1317 ...'). |
| `syriac-orthodox-west-syriac-christianity--syriac-renaissance` | influenced | Documented | new | syriac-renaissance longDescription and why (Michael's chronicle 'quotes at length from earlier writers whose own books are otherwise lost'). Inventory missed it. syriac-orthodox-west-syriac-christian… |
| `coptic-christianity-fatimid-to-mamluk--zagwe-and-early-solomonic-ethiopian-christianity` | in contact with | Documented | new | zagwe relationsSummary ('formal dependence on the Coptic patriarchate'), longDescription and why (the abun sent from the Coptic patriarchate). The Coptic text does not name Ethiopia's bishop, which t… |
| `zagwe-and-early-solomonic-ethiopian-christianity--the-ethiopian-monastic-flowering` | continued as | Documented | new | zagwe continuesAs field, longDescription and why (Yekuno Amlak displacing the Zagwe in 1270; the Solomonic line and the Kebra Nagast); the-ethiopian-monastic-flowering relationsSummary ('A continuati… |
| `the-franciscan-movement--observant-reform-and-popular-preaching` | influenced | Documented | new | the-franciscan-movement relationsSummary ('Later the Observants kept its rule to the letter'), revision round 2 |

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08), after era 4's entries:
- Cistercians and Cluny: the era 4 Cluny text disagrees. For the era 4 owner.
- Well-known facts with no vendored source, era 5: the era's cases added to Mark's open method question.
- No movement for the Bulgarian church of the Second Empire. For Mark.
- Long-gap links to modern churches (Georgia, Serbia and Bulgaria). For Mark.
- No link type for church jurisdiction. A method question for Mark.
- No Syriac Orthodox movement after 1300. For Mark.
- The Abbasid Church of the East has no continuesAs. For the era 4 owner.
- Humiliati sources wanted.
- The Franciscan order and the Observants, held for P2-L6.
- Two more out-of-era link notes use "we hold". For P2-L11.
- Page recordings read the old descriptions: 16 era-5 pages. A paid voice run, for Mark.
- "Silent since 622" is fixed (closes the era 4 entry).

Notes:
- Several Dominant Modern Reconstruction and Inferential-Thin links rest on one vendored nineteenth-century secondary (Mouravieff, 1838; Brosset, 1849), read at the cited lines in this pass. Seven rest on secondary works the repo names but this pass did not read; those carry `verification_state` `named-not-rechecked`.

## Wanted texts

- A Byzantine synodal or patriarchal text of 1054-1240 naming a metropolitan of Kyiv
- A repo-cited modern study of the Latin patriarchate of Constantinople, to replace Mouravieff as the secondary for the consensus reading
- A repo-cited modern work on the Bogomil-Cathar question read and cited by page (e.g. the Stoyanov and Hamilton chapters of Sennis, ed., Cathars in Question, 2016), for both sides of the dispute.
- A repo-cited modern work on the reception of William of Tyre's history, if the Outremer legacy line is to be sourced
- A repo-cited source on the Protestant orders of St John and the founding of St John Ambulance, if that legacy line is to be sourced
- A source for the Carmelite hermits' move west in the 1230s and 1240s (e.g. the order's early chronicles, or a repo-cited modern history), and for Albert keeping his seat at Acre
- A source for the Florensian order's merger into the Cistercians (1570), if the clause is to return
- A source for the Waldensian Church's union with the Italian Methodists (1975-1979), if the clause is to return
- A source for the twenty-first-century dispute over the Kyiv Pechersk Lavra between rival Ukrainian churches
- A source placing Nikephoros the Monk (On Sobriety, PG 147) on Mount Athos in the thirteenth century
- A text placing Gregory VII's see at Sis after 1293 (e.g. the continuation of Sempad's chronicle, RHC Doc. arm. I from line 67474, read for the move), to show the step from Hromkla to Sis directly
- A vendored source for the Treaty of Paris (1229) or the crown's annexation of Languedoc, if the Cathar legacy's 'attached Languedoc to the French crown' is to be sourced
- A vendored text of the crusade's own sources: Innocent III's letters of 1208-1209 calling the crusade, or Peter of Vaux-de-Cernay's Historia Albigensis, to document 1209 from a primary side (Perrin, the only vendored narrative, is a seventeenth-century Protestant history).
- A vendored text on Montségur (1244) and Bélibaste (1321), e.g. the Fournier register; neither is in any vendored file I found beyond Lea's index.
- Abdisho of Nisibis, preface to the synod of Timothy II (1318), readable edition
- Adam of Eynsham, Magna Vita S. Hugonis (Rolls Series 37, ed. Dimock 1864), named in the Carthusian entry's sources
- Alexander IV's letters of 1255 condemning the Introductorius (D'Argentré, Collectio judiciorum I, 163-166), in a vendored edition: the vendored Protocol of Anagni (Ehrle-Denifle Bd 1, from line 5719) records the commission's examination but not the verdict, and its OCR is too corrupt to quote.
- Anna Komnene, Alexiad, book 15 (e.g. Dawes's English translation, 1928), in a vendored edition, to make this Documented.
- Anna Komnene, Alexiad, book 15 (e.g. Dawes's English translation, 1928), in a vendored edition: it would document Basil's community and its age from a primary side and could lift this to Widely Accepted.
- Bar Hebraeus, Chronography (Budge, 1932): the Mongol queens (Sorghaghtani Beki, Doquz Khatun) and the Kerait
- Bar Hebraeus, Ecclesiastical Chronicle vol. II (Abbeloos and Lamy, 1874; public domain): the patriarchs of Antioch after 1083, including Michael and Dionysius bar Salibi. Also check the vendored vol. I, whose header says it reaches the thirteenth century but whose OCR stops at 1083
- Bernard of Clairvaux, Apologia ad Guillelmum (PL 182; English in Eales, Life and Works of St Bernard, 1889-96), and Peter the Venerable, Letter 28 to Bernard (PL 189), to document a Cistercian-Cluniac link from both sides before any Cluny claim returns
- Bernard of Clairvaux, De laude novae militiae (PL 182), also for the relationsSummary's 'something the church had never authorized before' (Bernard's 'novum militiae genus')
- Bernard of Clairvaux, De laude novae militiae (PL 182, Migne 1854, or the Leclercq-Rochais Opera vol. 3), to document Bernard's defense of the Templars and the 'malicide' passage directly; with it this link could be Documented
- Bernard of Clairvaux, Sermons on the Song of Songs and De diligendo Deo (PL 182-183 or Eales), to check the sayings Rolle and Hilton credit to him
- Bonaventure, De reductione artium ad theologiam (Quaracchi vol. 5, 1891), where he names Hugh and Richard of St Victor; would lift the Victorine-Franciscan link to Documented
- Cum de quibusdam mulieribus (Clementines III.11.1), the Vienne decree against the beguine status itself, in any vendored edition: would let the beguine text again say the council moved against the beguine life itself
- Dante, Divina Commedia, Paradiso 12 (Joachim 'di spirito profetico dotato'), in a vendored edition
- Domentijan's or Teodosije's Life of Sava
- Domentijan's or Teodosije's Life of Sava (e.g. Daničić's editions, 1860s), or Sava's Karyes and Hilandar typika in a readable text, before a Serbian adaptation of Athonite charters can be stated (the vendored Miklosich, Monumenta Serbica, is too garbled to quote)
- Euthymios Zigabenos, Panoplia dogmatica, title 23 (PG 130), or Gieseler's Narratio de Bogomilis (1842), in a vendored edition.
- Euthymios Zigabenos, Panoplia dogmatica, title 23, 'Against the Bogomils' (PG 130), in a vendored edition.
- Euthymius of Tarnovo's writings or the 14th-century Slavonic translations of hesychast texts, or a repo-cited modern study of the South Slavic books reaching Russia, so the 'traveled north to Russia' claims can stand unqualified
- Francis of Assisi, Testament ('the Lord Pope confirmed it for me'), in a vendored edition
- Gadla Lalibela (Perruchon, 1892; public domain): the Zagwe king's Life, for the Jerusalem programme of the churches
- George Pachymeres or Nikephoros Gregoras (vol. 1, Book V) for the refusal of the union in Constantinople, so the Byzantine side has its own record
- Gregory Palamas, Triads in Defence of the Holy Hesychasts, in a clean text or translation, for his own appeal to Athonite teachers (I.2.12 on Nikephoros)
- Guigo I, Consuetudines Cartusiae (PL 153), to test whether the Carthusian founders tied their life to the desert fathers, before 'the desert revived' can return
- Guigo II, Scala claustralium (PL 184 or PL 40) and the Middle English 'ladder of four rungs' (MS Douce 322), to test the Cloud's ch. 35 reference directly
- History of the Patriarchs of the Egyptian Church, vols. 2-4 (Cairo, 1943-1974): Cyril II's mission of Severus to Ethiopia (to date it), the metropolitans of the Zagwe years, and Cyril III ibn Laqlaq; check rights
- Honorius III's bulls of 1216-1217 confirming the Order of Preachers, in a vendored edition, if the Latin papal text is to name the Dominicans' approval again
- Humbert of Romans and John of Parma's joint letter of 1255 urging peace between the two orders, as documentary evidence of contact and rivalry
- I. Guidi, Il Fetha Nagast o Legislazione dei Re (1897-1899; public domain): to check the Fetha Nagast's derivation from al-Safi ibn al-Assal's Nomocanon
- Innocent III's bull to the Maronite patriarch Jeremiah (1215), in a vendored edition (e.g. Anaissi, Bullarium Maronitarum, 1911, if public domain), to document the union's terms
- Innocent III's letters of 1201 to the Humiliati (Incumbit nobis; Non omni spiritui; Diligentiam pii patris), e.g. in Tiraboschi, Vetera Humiliatorum monumenta II (1767), for the date and the three orders
- Innocent III's letters on the election of Thomas Morosini as Latin patriarch (Register VII-VIII), and Villehardouin, for the crusaders' side
- John XXII's condemnation of Olivi's Apocalypse commentary (1326), if vendored in the Bullarium Franciscanum v5, to show the papacy treating the Spirituals' Joachite reading as one.
- Jordan of Saxony, Libellus de principiis ordinis praedicatorum, for Dominic's preaching against the heretics of Languedoc from 1206
- Kallistos's Life of Gregory of Sinai (ed. Pomjalovskij, 1894), for Paroria and Gregory's Bulgarian disciples, so the hesychast sentences of the Serbian and Bulgarian entry can be restored
- Kartlis Tskhovreba (the Georgian Chronicles) in a vendored translation, e.g. Brosset's French text volume (Histoire de la Géorgie, part I, text) or Thomson, Rewriting Caucasian History (1996), for the catholicoi and the Bagratid union
- Lateran IV, canon 68, in a vendored edition (Mansi XXII or another public-domain text), for the dress rule for Jews and Muslims
- Lea, A History of the Inquisition of the Middle Ages, vol. 1 (1888), which narrates the Albigensian crusade and the founding of the inquisition in the 1230s; only vol. 3 is vendored.
- Lerner 1972 actually read, for the exact shape of his conclusion
- Lucius III, Ad abolendam (Verona, 1184), which names 'eos qui se Humiliatos vel Pauperes de Lugduno falso nomine mentiuntur': Mansi 22 or Friedberg, Corpus iuris canonici II (X 5.7.9). With it this becomes Documented and the qualified sentences can be restored.
- Mansi, Sacrorum conciliorum collectio vol. 24 (Lyon 1274 acta, Michael VIII's letter at col. 70-71); only vols 25 onward are vendored
- Marguerite Porete, The Mirror of Simple Souls, in a vendored edition (Babinsky 1993 is cited, not vendored; the Old French is not vendored), to set the condemned propositions beside her own words
- Michael the Syrian, Chronicle Books XII-XXI (Chabot, Chronique de Michel le Syrien vol. III, 1905; public domain): Michael's own patriarchate, his dealings with the Latin patriarchs of Antioch and Jerusalem (would test a syriac-renaissance / latin-church-of-outremer contact link), and the Theodore bar Wahbun schism told in the documentedStories
- Michael the Syrian, Chronique, tome 3 (Chabot 1905), for Michael's own dealings with the Latin church of Outremer (would let the Syriac Orthodox side of the crusader states be linked)
- Michael the Syrian, Chronique, tome 3 (Chabot 1905), the Syriac original's account of Athanasius and Aimery at Antioch; only the Armenian version's extract is vendored
- Nerses Shnorhali's letters to Manuel I (the Encyclical and letters, Armenian ed. St Petersburg 1788, or a public-domain translation), so the correspondence can be quoted from Nerses's own side
- Nestor's Life of Theodosius of the Caves, or the Primary Chronicle under 1074, in a vendored edition, for the Studite rule's arrival in Kyiv
- Nicholas IV's letters of 1288 to Arghun and to Yahballaha III (Langlois, Registres de Nicolas IV)
- Niketas Choniates, History, on the sack of 1204 (the movement's own documented story cites it; not vendored)
- Niketas Stethatos, Life of Symeon the New Theologian, in a vendored edition
- Pachymeres or Gregoras, Book V and after (Gregoras vol. 1 is not vendored), for the patriarchs between 1261 and 1300 in a narrative source
- Peter John Olivi, Lectura super Apocalypsim, in any vendored edition (the Franciscan dossiers found none), to document Olivi's use of Joachim from his own text rather than through Ehrle's extracts.
- Rainier Sacconi's Summa (1250) in a vendored edition (e.g. Dondaine, Un traité néo-manichéen, 1939, if public domain) or a public-domain translation, to quote him directly rather than through Rački.
- Richard of St Victor, Benjamin Minor and Benjamin Major (PL 196)
- Salimbene de Adam, Chronicle, in a vendored edition (Holder-Egger, MGH SS 32, 1905-13, or Parma 1857), for a Franciscan's own account of Joachite expectation in the friaries and of Gerard.
- Sava's Life of Symeon (Stefan Nemanja) and the Hilandar and Karyes typika in a vendored edition or translation
- Stefan Nemanja's Hilandar founding charter in a quotable text (Miklosich, Monumenta Serbica, 1858, is vendored but its OCR is marked second witness only, not to be quoted)
- Tamara Grdzelidze (trans.), Georgian Monks on Mount Athos: Two Eleventh-Century Lives of the Hegoumenoi of Iviron (2009), cited in the movement's sources, for Giorgi the Hagiorite and Iviron in this period
- Tauler's sermons in a vendored text that names his Dominican profession in his own or a contemporary's words (Winkworth 1907 says so only in the editor's life)
- The 'charter of Niquinta' (Saint-Félix council, 1167; Besse 1660, cited by Rački from Bouquet XIV, 448), for the Balkan bishop Niquinta among the Languedoc Cathars.
- The Byzantine synodal edict of 1054 against the legates (Will, Acta et scripta, 1861, or another public-domain edition), so this break has a primary from the Greek side as well
- The Evergetis typikon and Sava's Hilandar typikon side by side (e.g. Byzantine Monastic Foundation Documents), to document 'Athonite charters adapted for Serbian monasteries'
- The Exordium Parvum, Exordium Cistercii and Carta Caritatis in a public-domain edition (e.g. Guignard, Les monuments primitifs de la règle cistercienne, Dijon 1878), for the founders' leaving Molesme to keep the Rule of St Benedict; would lift early-benedictine-italian-monasticism--cistercian-monasticism to Documented
- The Georgian Life of John and Euthymius of Athos, in a vendored translation, for the Iviron translators
- The Hospitallers' Rule of Raymond du Puy in a public-domain edition (e.g. Delaville Le Roulx, Cartulaire général des Hospitaliers, 1894), for 'our lords the sick' and the hospital in Jerusalem
- The Interrogatio Iohannis in a vendored edition with the Carcassonne colophon (e.g. Benoist 1691, or Döllinger, Beiträge II, 1890).
- The Kyiv Primary Chronicle (entry for 1051; e.g. PSRL vol. 1, 1846) and the Kyiv Caves Paterikon, for Anthony's tonsure on Athos
- The Life of Grigol of Khandzta by Giorgi Merchule, for the Tao-Klarjeti side
- The Rule of the Temple in a public-domain edition (Henri de Curzon, La Règle du Temple, 1886), for the Council of Troyes in 1129
- The Russian Primary Chronicle (Povest' vremennykh let), PSRL vol. 1 or 2, or an English translation, for the metropolitans sent from Constantinople
- The Russian Primary Chronicle and the Kyiv Caves Paterik in a vendored edition, for the Caves community and the metropolitans of Kyiv on both sides of 1054
- The Studite Hypotyposis (rule) itself, to tie the rule Kyiv received to Theodore's house
- The Toulouse canonization testimonies of 1233 (Lehner 1964 is cited in the census but not vendored)
- The Typikon of Athanasios for the Great Lavra and the Lives of Athanasios (e.g. Meyer, Die Haupturkunden für die Geschichte der Athosklöster, 1894), for the founding, imperial patronage and any Studite model
- The acts of the Fourth Lateran Council (Mansi XXII, not vendored; only Mansi tomes 2-7, 10, 25-27, 31-32, 35 and 46 are), for the patriarch's presence
- The decretal Ad abolendam (Lucius III, Verona 1184; Liber Extra 5.7.9) in a vendored edition that prints the clause naming the 'Humiliati' and 'Poor of Lyon' (e.g. Friedberg, Corpus Iuris Canonici II, 1881). Denzinger's vendored excerpt (no. 402) prints only the sacramental clause and does not name the Waldensians.
- The full text of Ad nostrum (its opening names 'begardi' and women 'quae beguinae vulgariter appellantur'), e.g. Friedberg, Corpus iuris canonici II, Clementines V.3.3
- The surviving excerpts of Gerard's Introductorius outside the Protocol of Anagni, whose vendored OCR (Ehrle-Denifle Bd 1, from line 5719) is too corrupt to quote.
- The text of Pope John Paul II's address in Athens (4 May 2001) on the sack of 1204, before the Byzantine legacy's 'offered an apology' is kept or reworded
- The typikon of Gregory Pakourianos for Petritsoni (1083), in Byzantine Monastic Foundation Documents (Dumbarton Oaks, 2000), cited in the movement's sources
- Thomas of Celano, First Life 32-33, for the 1209/1210 audience with Innocent III
- Thomas of Celano, Second Life of Francis 148-150, the earliest telling of the meeting, in a vendored edition
- Tsar Boril's Synodikon (1211) in a vendored edition or translation, for the Tarnovo anathema
- Valdes's profession of faith (1180) in a vendored edition, to document the census's 'entirely orthodox' confession from Valdes's own side.
- William of Tyre, Book XV ch. 18, in RHC Historiens occidentaux I (1844), for the Latin council at Jerusalem attended by the Armenian catholicos, from the Latin side
- William of Tyre, Historia rerum in partibus transmarinis gestarum, in RHC Historiens occidentaux I (1844), for the election of the first Latin patriarchs of Jerusalem and Antioch in his own words (Dulaurier cites Book VI, ch. 23)
- William of Tyre, Historia, Book XXII ch. 8, in RHC Historiens occidentaux I (1844, public domain), for the Maronite union with the Latin patriarch of Antioch in William's own words
- al-Safi ibn al-Assal, Nomocanon (al-Majmu' al-Safawi), any edition
