# Pachomius: source sheet

All files are in `cic/texts/`. Line numbers are the file's own lines (not the host OCR lines). Quoted text is verbatim from the file; the only change is that the OCR's runs of double spaces are closed to single spaces. OCR misreadings are kept and the reading is given in square brackets. Amélineau's Coptic and Arabic columns are unreadable OCR, so every Coptic Life is cited from his French of 1889, a second witness; any line used on air should be checked against the scan.

Witness kinds: **own** (his own words), **contemporary**, **later** (with rough gap), **late legend**, **editor** (a modern editor's note or judgment, never a witness to his life).

Confidence (project's five levels). How they are applied here: **Documented** for an act recorded by the person who did it (Jerome on his own translation); **Widely Accepted** for what both Lives (Bohairic and Greek) carry without contradiction, or what one Life carries and no held witness contradicts (so marked); **Contested** where held witnesses disagree; **Inferential-Thin** for claims resting on a single late or editorial source.

## The main witnesses

| Short name | File | What it is | Kind |
|---|---|---|---|
| Bohairic Life | `amelineau_histoire-de-saint-pakhome-annales-guimet-17_leroux1889.txt`, lines 4889-14805 | The koinonia's own Coptic Life (Vatican codex), anonymous, in Amélineau's French. It breaks off mid-story at 14796: **it holds no account of his death.** | later; date not fixed in what I read (the Library's corpus-map row calls these Lives "fourth to fifth centuries", an editorial judgment) |
| Greek Life | `acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt`, Prologue 80690, chapters from 80934 to about 88520 | The Greek Life in Daniel Cardon's Latin (17th c.), printed by the Bollandists, headed "Auctore suppari ... monacho" (80681), "by an author nearly contemporary". Passages in square brackets are, by the Bollandists' own note (82214-82217), not in their Greek manuscript but taken from Dionysius Exiguus's Latin, who "seems to have woven" the rule in from Palladius. | later, near-contemporary (the "suppar" description is the Bollandists'; Robertson's note at `npnf204_athanasius-select-works-letters.xml` 30455-30456 says "written late in the fourth century, but by a person who had known Pachomius", editor) |
| Arabic Life | Amélineau, lines about 20374-38712 | A later, fuller Arabic Life in Amélineau's French | later, date not fixed; later than both above |
| Life of Theodorus | Amélineau, lines 14805-20372 | Coptic Life of his disciple Theodore, French | later |
| Palladius | `palladius_lausiac-history_clarke1918.txt`, ch. XXXII-XXXIII, lines 397-415 | Lausiac History, a visitor's account, c. 419-420 (corpus-map row) | later, about 70 years |
| Sozomen | `npnf202_socrates-sozomen-ecclesiastical-histories.xml`, 31680-31763 | Church History III.14, follows Palladius closely | later, about a century |
| Jerome | `jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`, preface 4324-4500, Rule from 4506 | His Latin of the Pachomian rules, with his preface | later; contemporary with the federation's third generation (about 404 by the corpus-map row) |
| Gennadius | `npnf203_theodoret-jerome-gennadius-rufinus.xml`, 42250-42267 | On Illustrious Men ch. 7 | later, about 130 years (Gennadius "wrote c. 480", census) |
| Ethiopic Rules | `pachomius_rules-ethiopic_schodde1885.txt`, 162-206 | Ge'ez rules in Schodde's English (1885). Part I is the same text as Palladius ch. 32 (compare 170 with Clarke 399). | later; Part II undated; Part III late (Schodde, 162) |

## Setting

**S1. Birth in Upper Egypt, to pagan parents.** Bohairic Life, Amélineau 4954-4957. Later. Widely Accepted (the Greek Life has him say "e Gentilibusnatus sim parentibus", 86417).
> "11 [Il] y avait dans le nome d’Esneli [Esneh] 1 quelqu’un, nommé Pakhôme, dont les parents étaient hellénisants : il obtint une grande miséricorde de la part de Dieu, il devint chrétien dans le nome de Diospolis2, dans un village appelé Schénésît3"

Amélineau's own note (editor, 4968-4969): Schénésît is a small village on the east bank, "le -/v;voêô<rxtov [Chenoboskion] des Grecs". The Greek Life names the place of baptism "Chenoboscia" (81024-81027), so the two Lives agree on the place.

**S2. Place: the Thebaid; Tabennisi a deserted village by the river.** Bohairic 6013-6015; Greek 81341-81343. Widely Accepted.
> Bohairic: "il marcha environ la distance d’un mille jusqu’à ce qu’il arrivât à un village désert, (situé) sur les bords du fleuve (et) nommé Tabennisi"
> Greek (Cardon): "ad vieum [vicum] quemdam desertum, Tabennesin nomine, forte pervenit"

Do not call it an island: Clarke's note (editor, 1029) "The error that Tabennisi was an island goes back to some MSS. of Sozomen". Sozomen's text does say "the island of Tabenna" (31758); so does Vallarsi's note to Jerome (editor, jerome file, after 4387).

**S3. Head house later at Phbôou (Pabau), not Tabennisi.** Bohairic 9597-9599; Clarke note 897 and 1063 (editor) say Palladius erred in placing the head house at Tabennisi. Widely Accepted.
> "il l’établit économe à Tabennisi, afin qu’il administrât aussi les autres : quant à lui, notre père Pakhôme, il resta dans le monastère de Phbôou, lieu où se trouvait l’administration commune1 des huit monastères."

**S4. Dates.** Contested.
- Birth "about 292" rests only on editors: Richardson's note to Gennadius (`npnf203` 42254, "Born about 292, died 348") and Schodde (`pachomius_rules-ethiopic_schodde1885.txt` 136, "born in 292 ... died in 348"). Inferential-Thin as a fact about him.
- Death 14 Pachon: Greek Life 86646 ("decimoquarto die mensis Pachon") and Arabic Life 35674 ("le quatorzième jour de Paschons, au milieu du jour") agree. Widely Accepted.
- Year of death: the Bollandists reckon 348 (annotations g and h, 86728 and 86730: "unde colligas anno 348 gesta hzc esse"; "nno 348 celebratum fuit Pascha"). Robertson (`npnf204` 5643) gives "May 9, 346", reckoned from the letter of Ammon (70553-70560). Contested.
- Age: the Arabic Life alone gives "soixante ans; il se fit moine à l’âge de vingt et un ans et demeura, dans la vie monacale, trente-neuf ans" (35770-35771). Inferential-Thin.

**S5. Tradition (census).** `pachomius` is told within `desert-monasticism`: name "Desert Monasticism", informalName "Desert Fathers and Mothers", shortName "The Desert", dates "c. 320–430 CE", place "Nile Valley & Desert · Egypt". Census `aliases` gives "Koinonia" as "Pachomius's own name for his linked houses". The Coptic church's own calendar keeps his feast (I4, below).

## Events

**E1. Conscripted at about twenty; Christians feed the locked-up recruits.** Both Lives. Later. Widely Accepted for the event; Contested for the town.
> Bohairic 5100-5101: "le jeune Pakliôme [Pakhôme], fut pris alors qu’il avait vingt ans"
> Bohairic 5139-5146: "Lorsqu’ils furent arrivés à Esneh, la ville de l’ancien royaume, on mena les hommes à la ville et on les jeta en prison. Le soir venu, quelques hommes de la ville apportèrent des pains et des mets à la prison, ils forcèrent ceux qu'on y avait enfermés à les manger, parce qu’ils les voyaient dans une grande tristesse. Et lorsque le jeune Pakhôme les vit, il parla avec ses compagnons et leur dit : « Pourquoi ces hommes font-ils avec nous une si grande charité ; ils ne nous connaissent pas. » — On lui dit : « Ce sont des gens chrétiens : ils agissent ainsi avec nous, par amour pour le Dieu du ciel. »"
> Greek 80981-80988: "ipse quoque in militiam abreptus est Pachomius, vigesimum tunc circiter agens ztatis [aetatis] suce [suae] annum. Impositos vero navibus tirones, qui delectum curabant milites appulerunt ad civitatem Thebaorum, ibique incluserunt : vergente autem in vesperuni die, non exigua erga eos commiseratione moti Christiani, ciburn [cibum] miseris et potum ... suppeditarunt."

The Lives disagree on the town: Esneh (Latopolis) in the Bohairic, the city of the Thebans (Thebes) in the Greek. The war: Bohairic 5093-5096 says Constantine was attacked by "un tyran des Perses"; the Greek 80979-80980 says "adversus Tyrannum". Neither names the enemy; do not supply one.

**E2. His vow in the night.** Both Lives. Widely Accepted.
> Bohairic 5147-5148, 5182-5183: "il passa toute la nuit à prier Dieu disant: «Mon Seigneur Jésus le Christ, Dieu de tous les Saints, que ta bonté me secoure en toute hâte1, sauve-moi de cette détresse, et moi aussi je servirai les hommes tous les jours de ma vie. »"
> Greek 81009-81013: "quamdiu. in terra hac vieturussum [victurus sum], non aliam quam (uam [tuam] solius voluntatem venerabunde respiciam ; ae [ac] singulari omnes homines amore complectens, secundum tuam praeceptionem, nihil non erga eos oflieii [officii] studebo exhibere."

**E3. Released, settles at Schénésît, baptized, serves villagers in an epidemic.** Bohairic 5191-5196, 5230-5241, 5283-5291. Later. Widely Accepted (baptism also Greek 81023-81027; the epidemic is Bohairic only).
> 5240-5241: "on le baptisa afin qu’il fût digne de recevoir les saints mystères, c’est-à-dire le corps et le sang du Christ."
> 5283-5291: "il y eut dans ce village une grande maladie pestilentielle- et une foule d’habitants moururent. Pour lui, il allait, il les servait, il apportait de grandes charges de combustible des épinaies et il les leur distribuait ... il tint conseil en lui-même disant : « Cette œuvre, à savoir soigner les malades dans les villages, ce n’est pas l’œuvre d’un moine, mais celle des clercs et des [vieillards fidèles seulement]"

**E4. Learns the monk's life from the hermit Palamon.** Bohairic 5331-5480 (and Greek ch. I, from 81030). Widely Accepted. Palamon tells him the life is an inherited rule, so Pachomius did not invent monastic discipline.
> Bohairic 5424-5427: "La règle de la vie monacale telle que nous l’ont apprise ceux qui nous ont précédés est celle-ci : en tout temps, passer la moitié de la nuit en veille, en méditant la parole du Seigneur"
> Bohairic 5574-5575 (Palamon, finding oil on the salt at Easter): "« On a crucifié mon Seigneur pour moi, et moi je mangerais de l’huile qui fortifie le corps ! »"

**E5. The voice at Tabennisi.** Both Lives. Widely Accepted (as the Lives' account; the voice stays in their voice).
> Bohairic 6018-6021: "une voix lui vint du ciel, disant : « Pakhôme, Pakhôme, combats etresteence [et reste en ce] lieu : bâtis pour toi une cellule et des multitudes d’hommes viendront à toi pour se faire moines près de loi [toi] et trouveront profit pour leurs âmes. »"
> Greek 81345-81349: "vox ad eum defertur ... ita dicens ; Subsistehic [Subsiste hic], et monasterium extrue : plurimi namque monasticee vitee amplectendie avidi huc. ad te accedent."

**E6. The angel's charge: serve the human race.** Both Lives agree word for word in sense. Widely Accepted (as the Lives' account).
> Bohairic 6246-6248: "un ange du Seigneur lui apparut et lui dit par trois fois: « Pakliôme, Pakhôme, Pakhôme, la volonté de Dieu est que lu [tu] serves la race humaine et que Iules [tu les] unisses àLui [à Lui]. »"
> Greek 81972-81974: "Ita autem edixit Angelus : Dei voluntas est, ut servias hominum generi, ipsos ei conciliando"

**E7. The tablet: where the witnesses disagree.** Contested.
- Palladius 399: the angel "gave him a brass tablet on which this was inscribed"; the rule follows (400-403), with the twenty-four lettered groups (400).
- Sozomen 31706-31712: "A tablet was then given to him, which is still carefully preserved."
- Ethiopic Part I 170: "he handed him a tablet of iron". This Part is the same text as Palladius's chapter (Tabennesis, the cave, the angel, "Few are these prayers", 176), so it is not an independent witness.
- Gennadius 42257-42259: an Order of discipline "which he received by angelic dictation".
- Jerome's preface 4344-4347: they laid the foundations "juxta preceptum Dei, et angeli, qui ad eos ob hanc ipsam institutionem missus venerit ?." (4345-4347)
- **The Bohairic Life has the voice and the angel's charge (E5, E6) but no tablet.** In the Greek Life the tablet passages (81348-81360, 81974 onward) are in square brackets, and the Bollandists note (82214-82217, editor): "Qui sequuntur de Regula non inveniuntur in MS. Veneto, sed apud Dionysium, qui videtur ipsam vitz [vitae] textui, qualem in Vitis Patrum apud Palladium vel Heraclidem Ponticum legerat, intexuisse."
- Clarke's note (editor, 1033) reports Ladeuze: "The angel here seems to him legendary, since he is not mentioned in the Lives". Ladeuze's further view (1047) that the lettered groups are Palladius's invention is a scholar's view, not a witness.

**E8. The first disciples; he serves them alone; then gives them rules.** Bohairic 6252-6300, 6333-6336. Widely Accepted (Bohairic only in this detail).
> 6290-6299: "« Ce sont des plantes nouvelles, ils 11e [ne] sont pas encore parvenus à cet étal [état] de (pouvoir) servir les autres; » ... « Quel est l’homme qui attellera son bœuf dans un champ et l'oubliera au point qu’il tombe et meure. De même pour moi, si le Seigneur voit que je me fatigue, il nous enverra d’autres (frères) qui auront la force de nous aider en toute œuvre bonne. »"
> 6299-6300, 6335-6336: "Et il leur donna des règles et une forme (de vie) où il n’y avait point de pierre d’achoppement, ainsique ... des traditions utiles pour leurs âmes, des habits et une nourriture exactement semblables avec une couche décente"

**E9. How the houses ran.** Bohairic 6385-6482. Widely Accepted.
> 6385-6391: "lorsque les frères furent au nombre de cent hommes, il leur bâtit une église dans son monastère ... car certes notre père Pakhôme ne désirait pas qu’il y eût des clercs dans ses monastères à cause de l’envie et de la vaine gloire."
> 6431-6434: "11 [Il] est bon que nous nous soumettions avec humilité à l’Église de Dieu, et celui que nous trouverons à chaque fois ayant été ordonné par nos pères les évêques nous suffira pour cela."
> 6477-6479: "il les chargea d’acheter et de vendre. Toutes les trois semaines, on changeait les frères qui faisaient le service"
> Petronius gives everything to the community, 8455-8460: "tout ce qui leur appartenait, soit brebis, soit boucs, soit vaches, soit chameaux, soit ânes, soit chars, soit barques, Pétronios le donna à la communauté de notre père Pakhôme."
> The twice-yearly gatherings, 9640-9644: "Les frères allaient à Phbôou deux fois chaque année, pour faire la Pâque les uns avec les autres selon la parole de Dieu, et à la saison des fruits, vers le vingtième jour de Mésoré, pour rendre leurs comptes à l’économe en chef"
> Jerome's preface confirms both gatherings from outside: Easter (4477-4479, "ut quinquaginta millia fere hominum Passionis Dominice $6 simul cele- brent festivitatem") and Mesore (4481-4483, "Mense, cui vocabulum est Mesore, id est Au- gusto, instar Jubilei remissionis dies exercentur"). So does Gennadius (42264-42267, the Passover at "Bau" and "the day of remission ... in the month of August").

**E10. His sister Mary and the women's house.** Contested in the details.
> Bohairic 6523-6528: "Lorsqu’une sœur qu’il avait, elle se nommait Marie et était vierge depuis son enfance, eut appris (tout) cela, elle se leva, elle alla vers lui au nord jusqu’à Tabennîsi, désirant le voir. Lorsqu’on lui eut appris qu’elle (était arrivée), il lui envoya le frère qui veillait à la porte, disant: « Voici, sache que je suis en vie ; mais ne sois point attristée de ne pas m’avoir vu."
> Bohairic 6572-6573: "il envoya les frères qui lui bâtirent une cellule dans le village, à quelque distance de son monastère"
> Bohairic 6576-6581: "il chargea un vieillard, nommé abba Pierre, d’ètre leur père ... Il écrivit les règles des frères dans un livre et les leur envoya, afin qu’elles les apprissent."
> Ethiopic Part II 206: "made a dwelling-place for her alone on the opposite side of the river at the distance of a mile ... [the women] reached the number of one hundred and eighty, and these [the men] three hundred and forty; and he commanded them that they should be exceedingly careful not to see their [the women's] faces nor hear their voices."
> Palladius 409: "some 400 members ... the women are on the far side of the river, the men opposite them."

The Bohairic puts her cell "in the village", with no river; the Ethiopic and Palladius put the women across the river. Burials also differ: Bohairic 6619-6628, chosen brothers sing under the portico and the body goes "sur un char ... vers la montagne"; Palladius 409 and Ethiopic 206 have the brothers ferry the body across and bury it in their own place. The Bohairic alone names her (Mary). Numbers of women: 400 (Palladius), 180 (Ethiopic).

**E11. Athanasius visits; Pachomius hides from ordination.** Both Lives. Widely Accepted.
> Bohairic 6670-6674: "abba Sarapamon, évêque des habitants de Denderah 1 , prit la main de l’archevêque, la baisa et lui dit : « J’en prie ta divine charité, ordonne prêtre Pakhôme, le père des moines, afin qu’il ait autorité sur tous les moines de mon diocèse, car c'est un homme de Dieu et c’est la seule chose en laquelle il ne m'ait pas obéi. » Aussitôt Pakhôme se cacha parmi la foule nombreuse afin qu’on ne le trouvât pas."
> Bohairic 6718-6720 (Athanasius's message): "Puisque lu [tu] t’es caché de nous et que lu [tu] as fui ce qui cause les envies, les luttes et les haines, que tu as choisi la suprême dignité qui durera éternellement avec le Christ et as fui la dignité vaine qui ne dure qu’un temps"
> Greek 82514-82520: the bishop of Tentyra asks Athanasius "ut omnibus eum Monachis ... Patrem jubeas esse et Presbyterum. Ille vero hoc audiens, donec transisset Papa, delitescere inter Fratres studuit."
> Robertson's introduction (editor, `npnf204` 4491-4493) says Athanasius "appears to have ordained Pachomius to the presbyterate". Both Lives say the opposite. Do not use Robertson here.

**E12. Questioned by monks and bishops at Latopolis; a man tries to kill him.** Greek Life only (the Bohairic text breaks off before this point). Widely Accepted as the Greek Life's account; uncontradicted.
> 86393-86400: "Cumque aliquando sermones incidissent dubii, eo quod diceretur dignoscere occulta, et in Ecclesia Latorum non pauci in unum convenissent Monachi et Episcopi; ipse etiam Pachomius ... adfuit, vocatus ut hoc manifestaret. ... Tandem ab Episcopis Philone et Mobe, ut se suaque defenderet, jussus"
> 86416-86425 (his answer): "An non frequenter ex me audistis, quod e Gentilibusnatus sim parentibus quid Deus esset omnino ignorans? ... nos autem, qui tanta modo sumus multitudine, et novem omnino monasteria complemus"
> 86463-86466: "Vix autem sermonem finierat, cum ἃ [a] malo genio actus quispiam et machera armatus, virum santum interfecturus irrumpit : sed auxilio presentium salvavit eum Dominus."

**E13. Plague, death, succession.** Greek Life and Arabic Life (the Bohairic holds no death). Widely Accepted for plague, illness, naming Petronius, 14 Pachon.
> Greek 86510-86512 and 86573-86574 (margin notes intervene): "morbus insolitus, divino nutu, Fratres invasit, ita utin omnibus monasteriis centum ac plures, qui e ... malo obierant, numerarentur : ipse etiam Pachomius infirmabatur."
> Greek 86612-86614: "Petronium, si modo in vivis permaneat, Fratrum regimini haud fore ineptum."
> Greek 86619-86633 (the blanket): "dies quippe nunc sunt elapsi quadraginta, ex. quibus gravi hac infirmitate pre- mor ... Istud, inquit, straguli absque mora hine [hinc] aufer; non enim iequum [aequum] est ut in re quapiam melius mihi sit quam Fratribus ceteris."
> Greek 86636: "Cum ossa mea absconderint, transfer ea inde" (OCR "transfer en inde")
> Greek 86646, 86655-86658: died "decimoquarto die mensis Pachon"; Theodore and three brothers "corpus refossum in alium locnm [locum] deportarunt, in quo in hunc usque diem servatur."
> Arabic Life 35621-35628 gives a reason the Greek does not: Theodore "pensa qu’il lui parlait ainsi de peur que des gens n’allassent enlever son corps, pour lui bâtir une église, comme cela se pratiquait pour les martyrs; car souvenles fois il avait blâmé ceux qui agissaient de la sorte". Later; Inferential-Thin.
> Arabic Life 35733-35734: "Et jusqu’à ce jour, personne n’a su l’endroit où il avait été enterré."
> Petronius dies within days; Horsiesius succeeds: Greek 86660-86672; Arabic 35825-35877.
> The deathbed charge in the Greek, "INulla sit. vobis conjunctio cum sectatoribus. Meletii vel Arii vel. Origenis" (86594-86595), is inside square brackets, so by the Bollandists' convention it may come from Dionysius, not the Greek manuscript. Inferential-Thin; do not use.

## Impact, heaviest first (what later witnesses carried on and used)

**I1. A shared life under one written rule, copied across languages and centuries.** This is what the most later witnesses carry.
- Palladius 405: "there are a number of these monasteries which have observed this rule, amounting to 7000 men." (c. 420; later, Widely Accepted that the federation was large; the figure is Palladius's.)
- Sozomen 31751-31763: "They all observed one and the same rule of life, and possessed everything in common." (follows Palladius)
- Jerome 4336-4354 (Documented, his own act): Silvanus sent him the books; Latins in the Thebaid houses and at Metanoia "ignorarent /Egyptiacum | Grecumque sermonem, quo Pachomii et Theodori et Orsiesii precepta conscripta sunt" (4342-4344); "ut erant de JEgyptiaca in Grecam linguam versa, nostro ser- mone dictavi" (4352-4354). Jerome's Latin, by his own account, is a translation of a Greek translation of Egyptian.
- Cassian, Institutes IV.1 (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml` 18521-18531): "adding some things from the rule of the Egyptians, some from that of the monks of Tabenna". Later, about 70-80 years. Widely Accepted.
- Ardo's Life of Benedict of Aniane (`benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt` 28948-28951; author line 28361; Benedict "obiit anno 821", 28836, editor): "Regulam quoque beati Benedicti ti- ronibus seu infirmis positam fore contestans, ad beati Basilii dicta nec non Pachomii regulam scan- dere nitens" (line-end hyphens as printed). Later, nearly 500 years. Documented that a Carolingian abbot used it. The same volume's Codex regularum lists "VII S. Pachomii, 2vbatis [Abbatis] Tabennensis, cum refatione [praefatione] sancti flieronymiin [Hieronymi in] eamdem" (34229-34230) and the editor Ménard's catalogue of rules cited in the Concordia puts Pachomius second after Benedict (58597-58601, editor).
- Ethiopic Rules (Schodde 162): the Ge'ez church kept three parts; Part III "really no collection of rules at all, but only a kind of symbolical homily" (Schodde's judgment).
- Gennadius 42256-42258: "founder of the Egyptian monasteries, wrote an Order of discipline suited to both classes of monks" (later; keep the title in his voice).

**I2. The federation outlived him under his named successors.** Greek 86660-86672 (Petronius, then Horsiesius); Gennadius 42277-42286 on Theodore's letters, which urge "to restore to harmony and unity those who, a dissension having arisen after the death of the Abbot, had broken the unity". Athanasius wrote to Horsiesius and the brothers (`npnf204` 70505-70560; letters preserved in the Greek Life §§92, 96 per Robertson). Life of Theodorus: Theodore had Athanasius's Easter letter on the books of Scripture translated and placed in the monastery "pour leur servir de loi" (Amélineau 16034-16037). Widely Accepted.

**I3. What he defended (marked).**
- *Defended:* equality in the common life, to his deathbed: the blanket (Greek 86631-86632). Same clothes, same food (Bohairic 6335-6336).
- *Defended:* monks without clerical rank, under the bishops: no clergy in his houses "à cause de l’envie et de la vaine gloire" (Bohairic 6390-6391); submission to "nos pères les évêques" (6431-6434); hid from ordination (E11).
- *Defended:* his house's work against his critics at Latopolis (E12).

**I4. Remembered in the Coptic and Ethiopian churches.**
- Arabic Jacobite Synaxary, 14 Bashons (`patrologia-orientalis-tomus16_synaxaire-arabe-jacobite-barmahat-bachons-synaxaire-armenien-tre-fra_graffin-nau1922.txt` 19256-19328): "En ce jour mourut notre pere Pachome {Bakhoumyous)" ... "11 [Il] demeura a la tete de la communaute pendant qiiarante [quarante] ans ... il leur etablit quelqu'un pour les gouverner apres lui et mourut en paix." Late (church calendar). Widely Accepted that the Coptic church keeps his feast; the "forty years" is the calendar's.
- Ethiopic Synaxarium, Genbot 14 (`ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt` 29128-29179): "he made his disciple Theodore abbot over them; and after this he died in peace." Late; contradicts the Lives (Petronius was named). Contested.
- Life of Pisentius by John the Elder, 7th c. (`coptic-apocrypha-upper-egypt-life-of-pisentius_budge1913.txt` 17344-17347): "even as was the holy man Apa Pahomd (Pachomius), the father of the coenobite life." Later, about 300 years.
- Abu Salih (`abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt` 12782-12783): "The body of Saint Pachomius and the body of Sinuthius lie in two chests in a church to the south of Butij." Late (Ayyubid period, header); contradicts the Arabic Life's "no one knows the place". Contested.

## Possibly his own words

**W1. The Instructions of Apa Pachomius**, Sahidic, BM Or. 7024, in Budge's English (`coptic-apocrypha-upper-egypt-life-of-pisentius_budge1913.txt`, title 19811-19826, text 19827-20600). The manuscript's title assigns it to him; Budge accepts it (2176-2183). No other held source tests the attribution. Inferential-Thin as his own words. It is the only held text that speaks in his voice at length.
> 19920-19923, 19927-19936: "For, O my son, all the spirits from my youth up have on many occasions made me weak, and [when] I came into the desert they used to afflict me to such a degree that my heart failed me ... But when we took refuge at the feet of God with weeping and with humility, and with fasting, and with vigils by night, the Enemy and all his spirits also became powerless in respect of me"

The Ethiopic Rules Part I is not his own words (it is Palladius's chapter). Jerome's Rule is Pachomian legislation in a Latin of a Greek version, not his Coptic words (Library_Fill call).

## Links to other people

- **Athanasius of Alexandria** (on the tree): met him; Pachomius hid from the ordination Athanasius was asked to perform (E11). Athanasius later wrote to Horsiesius (I2).
- **Antony** (on the tree): never met, by the Greek Life. Told of his death, Antony says (86799-86820, right-hand column, run together with the left in the OCR): "Equidem serio et sape [saepe] volui illum corporali presentia cernere, sed forte dignus haud fui: per Dei gratiam in regno [coelorum] invicem videbimus".
- **Palladius** (on the tree): wrote of him and his houses; visited the Panopolis house (405); heard of him from Arsisius (Clarke 227).
- **Sozomen** (on the tree): wrote of him, following Palladius.
- **Jerome** (on the tree): translated his rule into Latin.
- **John Cassian** (on the tree): drew on the Tabennesiot rule.
- **Gennadius** (on the tree): wrote his notice.
- Theodore, Horsiesius, Petronius, Palamon, his sister Mary: not checked as tree entries.

## Where sources disagree or come late (summary)

1. Tablet: Palladius, Sozomen, Ethiopic (copying Palladius), Gennadius; not in the Bohairic, and in the Greek only in bracketed material the Bollandists say came via Dionysius from Palladius.
2. Town of the recruits' prison: Esneh (Bohairic) or Thebes (Greek).
3. Women's house: in the village (Bohairic) or across the river (Palladius, Ethiopic); burial by cart to the mountain or by ferry to the men's cemetery.
4. Numbers: 7000 monks (Palladius, Sozomen), 5000 (Ethiopic 182), "nearly fifty thousand" at Easter (Jerome 4477-4479); first house 1300 (Palladius 405) or 1400 (Clarke 309, ch. XVIII) or 300 (Ethiopic 182); nine monasteries (Greek 86424), eight under the common administration plus Phbôou (Bohairic 9599).
5. Year of death: 346 (Robertson) or 348 (Bollandists, Richardson).
6. Successor: Petronius (Greek, Arabic) or Theodore (Ethiopic Synaxarium).
7. Grave: moved in secret and kept elsewhere "to this day" (Greek); "no one has known the place" (Arabic); "in two chests in a church to the south of Butij" (Abu Salih).

## Library sweep

- **Card sources** (starting list only): Schodde's Ethiopic Rules, Palladius (Clarke), Sozomen, Gennadius. All read at the cited lines.
- **Corpus-map:** `desert-monasticism.yaml` (the census `toldWithin`) read for every Pachomian row: the Amélineau Bohairic, Theodorus and Arabic rows, the Acta Sanctorum rows, the Jerome rows, the Ladeuze row, the three Ethiopic rows, Gennadius, Palladius (Clarke and Syriac). Coptic buckets listed (`coptic-christianity-under-early-islam`, `cyrilline-miaphysite-egyptian-christianity`, `coptic-christianity-fatimid-to-mamluk`, and others); Pachomius has no row of his own in them, but files they hold (Pisentius, Abu Salih, synaxaries) mention him and were searched directly. `WORKS.yaml`, `AUTHOR-IDS.yaml` and `RETRIEVAL-HINTS.md` have **no entry** for Pachomius or any name form (searched "pach", "pakh").
- **Text search:** `cic/texts/` for pachom, pakhôme/pakh.me, pacôme, tabenn, bakhum/bakhom. **182 files** mention the subject (excluding the index and registry).
- **Used:** Amélineau (Bohairic Life, Life of Theodorus, Arabic Life, all in French); Acta Sanctorum May III (Cardon's Greek Life and the Bollandist notes, marked editor); Jerome PL 23 (preface and Rule); Palladius (Clarke, with Clarke's notes marked editor); Sozomen; Gennadius; Schodde's Ethiopic Rules; Cassian's Institutes (NPNF); Ardo and Ménard in PL 103; the Arabic Jacobite and Ethiopic synaxaries; the Pisentius volume (Life of Pisentius; the Instructions of Apa Pachomius); Abu Salih; Athanasius's letters to Horsiesius and Robertson's notes (NPNF 4, marked editor).
- **Set aside, and why:**
  - Ladeuze 1898: a modern study; used only as reported through Clarke's notes, never as a witness.
  - Amélineau's introduction (4889 and before) and the Bollandists' commentary (from 78843): editors' apparatus; used only for the note on the bracketed tablet.
  - The Paralipomena (Acta, from 88527): miracle anecdotes; nothing a two-minute story needs that the Lives lack.
  - Nau's Greek "Histoire de saint Pacôme" (Asceticon redaction) with French, inside the Patrologia Orientalis IV file (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt`, about 22000-29300): held but not worked through. Its §6 has the angel give "la tablette" (23135-23136), and Nau says it was compiled partly from Lausiac material (22128-22136), so it does not change the tablet finding. A later pass could use it.
  - The Syriac Paradise (`palladius_paradise-v1-syriac_budge1907.txt` 1081-1103): the same tablet chapter as the Greek Palladius.
  - Dionysius Exiguus's Latin Life: not held (Library_Fill 2b, located in Rosweyde 1628, not taken).
  - Benedict's Rule (Gasquet): Pachomius appears only in Gasquet's introduction (277-298), not in the Rule. Do not claim Benedict of Nursia used him.
  - Modern histories that mention him (Duchesne, Harnack, Butcher, Morison, Hefele): modern, not witnesses.
  - Later chronicles, councils and Byzantine texts with one to a few mentions (Mansi, Pachymeres, Bekker volumes, Athos charters, and the like): mostly the name as a model or a different Pachomius; nothing that carries his story further than the witnesses above.
