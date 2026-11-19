# Opus check of the era 4 and era 5 WANTED re-score (drafts G1-G4)

The drafts it checks are `Draft_G1.md` to `Draft_G4.md` in this folder, and the drafting brief (its "BRIEF.md") is `Drafting_Brief.md`. The results, after this check, are the tables of `Rescore.md`.

Read-only. Nothing in the repo was changed. No paid or model calls; no agents.

Method. For every row I opened each cited range in `cic/texts/` with sed/grep and read it. Tolerance is ±5 lines.
Most small slips in the drafts are the header's "OCR line" numbers used without adding 12. I list them as
"wrong" with the right lines. I also checked each verdict against the rules in BRIEF.md, the rulings blocks
(Era4 l.15-21, Era5 l.15-23, Supplement l.35-52) and the Decision-Log precedents the rows rely on.
"ok (x-y)" means the text is there, at x-y. "not opened" means I did not read that range; no verdict here rests on it.

Result kinds. CONFIRMED: citations hold and the verdict follows. CORRECTED: something must change before use;
the tag says what: (lines) a citation is off; (minor) a small misquote; (substance) a misread or a wrong claim;
(verdict) or (flag) the verdict or a flag changes. UNSUPPORTED: none.

File key (all in `cic/texts/`):
PG94 john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt · THEOPH theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt ·
NPNF14 npnf214_seven-ecumenical-councils.xml · WAITZ rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt ·
ROBANS rimbert_anskar-the-apostle-of-the-north_robinson1921.txt · SWEET alfred-the-great_west-saxon-version-of-gregorys-pastoral-care-ang-eng_sweet1871.txt ·
COOK asser_life-of-king-alfred_cook1906.txt · STUBBS dunstan_memorials-of-saint-dunstan-rolls-series-63-lat_stubbs1874.txt ·
AELF aelfric_vita-s-aethelwoldi-in-chronicon-monasterii-de-abingdon-v2-lat_stevenson1858.txt · WULF wulfstan-winchester_vita-s-ethelwoldi-pl137-lat_migne1853.txt ·
RC regularis-concordia_de-consuetudine-monachorum-in-anglia-13-lat-ang_logeman1891.txt · RAINE byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt ·
PLUM bede_opera-historica-v1-historia-abbatum-lat_plummer1896.txt · WILC bede_lives-of-the-first-five-abbots-of-wearmouth-and-jarrow_wilcock1910.txt ·
ARI ari-thorgilsson_islendingabok-and-kristni-saga-in-origines-islandicae-v1-non-eng_vigfusson-powell1905.txt · PL103 benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt ·
PL115 eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt · PL121 paulus-alvarus_confessio-epistolae-indiculus-luminosus-pl121-lat_migne1852.txt ·
CLU cluny_recueil-des-chartes-t1-802-954-lat-fra_bernard-bruel1876.txt · PL133 odo-cluny_opera-with-john-of-salerno-vita-odonis-pl133-lat_migne1853.txt ·
PL142 odilo-cluny_opera-with-jotsald-vita-odilonis-pl142-lat_migne1853.txt · PG100 nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt ·
PG99 theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt · GINZEL ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt ·
PG126 theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt · PAT kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt ·
CROSS russian-primary-chronicle_cross1930.txt · PSRL russian-primary-chronicle_psrl-t1-lavrentevskaia-letopis-orv_1926.txt ·
GORSKII ilarion-kiev_slovo-o-zakone-i-blagodati-chu-rus_gorskii1844.txt · PETER peter-of-sicily_historia-manichaeorum-seu-paulicianorum-grc-lat_gieseler1846.txt ·
TC theophanes-continuatus_historiae-byzantinae-scriptores-post-theophanem-pg109-grc-lat_migne1863.txt · ODZUN john-odzun_opera-arm-lat_aucher1834.txt ·
WILL will_acta-et-scripta-de-controversiis-ecclesiae-graecae-et-latinae-saec-xi-grc-lat_1861.txt · PSELL psellos_chronographia-and-orations-in-mesaionike-bibliotheke-v4-grc_sathas1874.txt ·
PG111 nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt · DEBOOR vita-euthymii-patriarchae_anecdoton-zur-geschichte-leos-des-weisen-grc-deu_de-boor1888.txt ·
TAB4/TAB5 tabari_annales-prima-series-iv-ara-lat_de-goeje1890.txt / tabari_annales-prima-series-v-ara-lat_de-goeje1893.txt · BAL baladhuri_origins-of-the-islamic-state-v1_hitti1916.txt ·
WATT wattenbach_secte-der-brueder-vom-freien-geiste-sitzungsberichte-berlin-deu_1887.txt · WEIL ibn-ishaq_leben-mohammeds-nach-ibn-hischam-deu_weil1864.txt ·
MACLER stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt · GELZER stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt ·
GRAF theodore-abu-qurrah_arabischen-schriften-deu_graf1910.txt · PG97 theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt ·
ASMAR3 acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt · PEET peeters_histoires-monastiques-georgiennes-in-analecta-bollandiana-36-37-lat-fra_1917-1919.txt ·
DUVAL ishoyahb-iii_liber-epistularum-versio-lat_duval-csco1905.txt · PL214 innocent-iii_opera-with-gesta-innocentii-pl214-lat_migne1853.txt ·
DOM domentijan_zivot-svetoga-simeuna-i-svetoga-save-chu_danicic1865.txt · MEYER athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt ·
PL185 bernard-clairvaux_opera-t5-with-vita-prima-pl185-lat_migne1855.txt · PL182 bernard-clairvaux_opera-t1-pl182-lat_migne1879.txt · EALES1 bernard-clairvaux_life-and-works-v1_eales1889.txt ·
PL166 stephen-harding_charta-caritatis-and-exordium-in-pl166-lat_migne1894.txt · PL195 aelred-rievaulx_opera-pl195-lat_migne1855.txt ·
PL152 bruno-cologne_opera-omnia-with-acta-pl152-lat_migne1879.txt · LECOUT le-couteulx_annales-ordinis-cartusiensis-v1-lat_1887.txt ·
DIMOCK adam-eynsham_magna-vita-sancti-hugonis-lat_dimock1864.txt · PL170 norbert-xanten_vita-b-and-sermons-in-pl170-lat_migne1894.txt ·
ASJUN5 acta-sanctorum_junii-tomus-5-lat_palme1867.txt · LANGLOIS porete_marguerite-in-revue-historique-54-fra_langlois1894.txt ·
MIRROR mirror-of-simple-souls_english-version-kirchberger1927.txt · CLARE clare-assisi_life-of-saint-clare-ascribed-to-thomas-of-celano_robinson1910.txt ·
LEMMENS leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt · DALENCON thomas-celano_vita-et-miracula-sancti-francisci-lat_d-alencon1906.txt ·
HOWELL thomas-celano_lives-of-st-francis_howell1908.txt · SETON agnes-prague_some-new-sources-for-the-life-of-blessed-agnes-of-bohemia_seton1915.txt ·
ASAUG1 acta-sanctorum_augusti-tomus-1-lat_1750.txt · ALTANER jordan-saxony_die-briefe-lat-deu_altaner1925.txt · REICHERT gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt ·
LEON4 thomas-aquinas_opera-omnia-t4-summa-theologiae-lat_leonine1888.txt · ASMAR1 acta-sanctorum_martii-tomus-1-lat_1735.txt ·
BUON joachim-fiore_tractatus-super-quatuor-evangelia-lat_buonaiuti1930.txt · ASMAI6 acta-sanctorum_maii-tomus-6-lat_1739.txt ·
COULTON salimbene_from-st-francis-to-dante_coulton1907.txt · BOURBON stephen-bourbon_anecdotes-historiques-lat_lecoy-de-la-marche1877.txt ·
DOELL doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt · MARTENE martene-durand_thesaurus-novus-anecdotorum-v5-lat_1717.txt ·
WT1/WT2 william-tyre_historia-rerum-in-partibus-transmarinis-gestarum-v1-lat-fra_rhc1844.txt / -v2-lat-fra_rhc1844.txt ·
PL158 anselm-canterbury_opera-with-eadmer-vita-anselmi-pl158-lat_migne1864.txt · PL190 thomas-becket_epistolae-with-vitae-pl190-lat_migne1893.txt ·
ROHR jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt · JDVH jacques-de-vitry_historia-orientalis-et-occidentalis-lat_1597.txt ·
CURZON templars_la-regle-du-temple-fra-lat_curzon1886.txt · SCHN templars_die-urspruengliche-templerregel-lat-deu_schnuerer1903.txt ·
STEIN adam-bremen_hamburgische-kirchengeschichte-deu_steinberg1926.txt · SCHM adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt ·
ALEX anna-komnene_alexias-grc_reifferscheid1884.txt · ZIG euthymios-zigabenos_narratio-de-bogomilis-grc-lat_gieseler1842.txt ·
MOUS pakourianos_typikon-in-commentationes-philologae-ienenses-4-grc-lat_mousaios1890.txt · REN renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt ·
POLO1 marco-polo_book-of-ser-marco-polo-v1_yule-cordier1903.txt · BERTH1 humbert-romans_opera-de-vita-regulari-v1-lat_berthier1888.txt ·
PL178 abelard_opera-pl178-lat_migne1885.txt · RHC1/RHC2 rhc-historiens-orientaux_t1-fra_academie1872.txt / rhc-historiens-orientaux_t2-pt1-fra_academie1887.txt ·
HITTI usama-ibn-munqidh_arab-syrian-gentleman-and-warrior_hitti1929.txt · WRIGHT ibn-jubayr_rihla-ara_wright1852.txt · ADLER benjamin-tudela_itinerary-heb-eng_adler1907.txt

---

## Era 4, draft G1 (Who_Scan_Era4.md l.82-103)

### John of Damascus (Era4:82)
- Draft verdict: WHO (thin life; tenth-century Life; cut-hand miracle Contested)
- Check: CORRECTED (substance)
- Lines verified: PG94 53476 ok · 30216-30222 ok (30218-30222) · 30331 ok · 31338-31350 ok (Cosmas the tutor) · 31872-31880 wrong: these lines send *Cosmas*, the dismissed tutor, "ad lauram sancti Sabae", and then make John chief counsellor (31877-31880); John's own entry to Mar Saba is at 33032-33038 ("divini Sabae lauram ... Joannes a pastore monasterii excipitur") · 616-621 ok, but l.617 says death "non ante a. C. 756", not "after 749" · 30258-30275 ok (garbled) · THEOPH 73728-73734 ok (73733-73734) · NPNF14 39463-39471 ok · PG94 7283-7285 ok.
- Verdict after check: WHO (thin life flagged; the only full Life is a 10th-c. retelling, l.621 "post medium saeculi decimi"; cut-hand miracle Contested)
- Note: The Melanchthon route holds: his own works plus the early witnesses (Theophanes, the 754 anathema, Nicaea II). Fix the Mar Saba line and the death note before the life is told.

### Anskar (Era4:83)
- Draft verdict: WHO (Life by his disciple; no own writings)
- Check: CORRECTED (lines)
- Lines verified: WAITZ 855-1030 ok (incipit 867) · 205-212 ok (207-208) · 209-211 ok (213-214) · running heads ok (203, 853, 1026) · ROBANS 1121 ff. wrong: l.1121 is a bibliography entry; the English Life begins at 1133 · 645-648 ok · 1355-1370 ok · 4795-4800 ok, but Robinson's own footnote at 4813-4816 says "It is not clear whether this Rimbert is to be identified with the author" · 227-231 ok (228-229) · WAITZ 213-245 ok.
- Verdict after check: WHO (following, plus an early Life by his disciple and successor; no own words held)
- Note: The draft's "within about a decade" is supported by a line it did not cite: WAITZ 182-184 (the book was written at Hamburg in the reign of Louis the German, who died in 876).

### Rimbert (Era4:84)
- Draft verdict: WHO (recorder; own life thin; Life of Rimbert held only to ch. 23)
- Check: CORRECTED (lines)
- Lines verified: WAITZ 4367-4425 ok (heading 4379; Pertz 4388-4395) · 4432-4448 wrong: that is Waitz's note on Adam of Bremen and interpolation; the author's aim ("quae offitii eius primitus occasio ... fideliter enarramus") is at 4452-4455 · 4844 ok · 855-1030 and 4300-4320 ok (the end of his Life of Anskar) · 5188-5268 ok (5259-5268, the horse given to ransom a captive) · ROBANS 4795-4800: text ok, but Robinson doubts this is the author (4813-4816) · Pertz 4390-4395 ok.
- Verdict after check: WHO (recorder; thin own life; Life of Rimbert written while Adalgar lived, held only to ch. 23)
- Note: Better support exists than the draft cites. WAITZ 4790-4799: the Life of Rimbert says the Life of Anskar was edited by Rimbert and a fellow disciple. WAITZ 5080 ff. prints his own letter to nuns ("Rimbertus, gregis Dei vilis servus"), so some of his own words are held. Drop the Robinson 4797 line as evidence for him.

### Alfred the Great (Era4:85)
- Draft verdict: WHO (ruler with own voice; Asser Contested)
- Check: CONFIRMED
- Lines verified: SWEET 183-215 ok (Old English greeting at 195) · 455-480 ok (English 464-475) · 472 ok · COOK 586-592 ok · 2725 ok · 1823-2550 not opened · 124-133 ok (126-135) · 2079 ok.
- Verdict after check: WHO (ruler with his own voice; Asser's Life written in his lifetime; authenticity Contested)
- Note: The ruler rule is applied rightly: the preface is in his own person.

### Dunstan (Era4:86)
- Draft verdict: WHO (author "B."; later Lives)
- Check: CONFIRMED
- Lines verified: STUBBS 8056-8110 ok (8066-8075) · 488-497 ok (492-494) · 1693 ok · 8385 ok · 9523 ok (a note: Athelstan's death) · 10183-10207 ok (Eadred's death).
- Verdict after check: WHO (early Life by "B."; Osbern and Eadmer later, so tag them)
- Note: STUBBS 505-511 adds that the Life dates "approximately ... the year 1000" and that the writer claims to be an eyewitness.

### Æthelwold of Winchester (Era4:87)
- Draft verdict: WHO (two early Lives by pupils; no own words)
- Check: CONFIRMED
- Lines verified: AELF 19886-19898 ok (19888-19900) · 19873-19880 ok · WULF 6230-6245 ok (6242-6248) · 5811-5830 ok · RC 21583-21600 ok · 21847-21849 ok (Dunstan at 21851).
- Verdict after check: WHO (two early Lives; Regularis Concordia not his in his own person)
- Note: Stevenson (AELF 19874-19878) notes that Ælfric's "heard from Æthelwold himself" line also appears in Wulfstan's Life.

### Oswald of Worcester and York (Era4:88)
- Draft verdict: WHO (author unnamed; date of writing "not stated")
- Check: CORRECTED (substance)
- Lines verified: RAINE 29596-29660 ok · 29723 ok · 2420-2430 ok (2421-2426) · 32148-32149 ok · 32582 ok · 34818-34840 ok (Oswald at Worcester 34831-34834).
- Verdict after check: WHO (early Life by an anonymous monk of Ramsey, written 995-1005)
- Note: The draft says no line dates the Life. RAINE 3854-3871 does: the author "must have been a monk of Ramsey", knew Oswald, and cites Archbishop Elfric, which "places the date of this biography between A.D. 995 and 1005"; Oswald died in 992. The file name's "Byrhtferth" is still not in the volume.

### Benedict Biscop and Ceolfrid, paired (Era4:89)
- Draft verdict: WHO (pair)
- Check: CORRECTED (lines)
- Lines verified: PLUM 30360-30375 ok (30372) · 31544 ff. wrong: 31544 is the end of Bede's History; the anonymous Life of Ceolfrid begins at 31562 · 734-777 ok · 825-832 ok, but the note concerns Bede's commentary on Samuel, not the Lives · WILC 2398-2425 ok (2410-2426) · 2455-2462 ok · 4098-4102 ok (4102) · BEDE 14333-14360 not opened (the scan's citation).
- Verdict after check: WHO (pair; Bede and the anonymous Life, both early; pair is a judgment call)
- Note: Verdict unchanged.

### Þorgeir Ljosvetningagodi (Era4:90)
- Draft verdict: LISTED (later-retelling rule)
- Check: CORRECTED (verdict)
- Lines verified: ARI 20486-20490 ok · 20488-20495 ok · 20495-20520 ok · 20300 ok · 20622 ok · 19787-19788 ok · 19674 ok · 19911-19915 ok · 20527 ok · 20690-20698 ok · 19885-19890, 22577, 27185-27345 not opened.
- Verdict after check: STORY (an office-holder with no voice of his own; one witness, Ari, about 120 years later; judgment call, alternative LISTED)
- Note: The citations hold. The rule does not. Ari wrote about 120 years later, not "centuries" later. In the Vladimir and Olga ruling (Era4 l.125-126, 356), Mark waits for the Primary Chronicle (c.1113, a similar gap) as the source to rescore on. So Ari counts as the early source here. Þorgeir is a Law-speaker who gave the ruling in Ari's report. He has no own words, no body of work and no following. That makes him STORY under the ruler rule, not WHO. The draft's own doubt already points to STORY.

### Benedict of Aniane (Era4:91)
- Draft verdict: WHO (Ardo's early Life; compilations)
- Check: CONFIRMED
- Lines verified: PL103 28361-28402 ok · 28575-28600 ok · 28836 ok · 32236 ff. ok (inside the Codex; heading 32248) · 58274 ff. ok (Concordia heading at 58280).
- Verdict after check: WHO (pupil's Life written in Louis's lifetime; his own works are compilations)
- Note: none.

### Eulogius of Cordoba (Era4:92)
- Draft verdict: WHO
- Check: CORRECTED (lines)
- Lines verified: PL115 56723-56735 ok (56725-56738) · 56760-56790 wrong: Alvarus's "passionem disponens scribere, prius vitam ejus" is at 56752-56754 · 59137, 67748, 68559 not opened (header pointers) · 65875 ok · 67764 ok · 62898 ok.
- Verdict after check: WHO (own works plus a Life by his friend, written at his death)
- Note: Verdict unchanged.

### Paulus Alvarus (Era4:93)
- Draft verdict: WHO (thin own life)
- Check: CORRECTED (lines)
- Lines verified: PL121 30860-31040 ok (notice from 30870; "Profiteor" 30983; "Conjugio ... astrictum" 30993) · 31697 ok · 32816 ok · 36802 ok · 38278 ok · 30905-30955 ok (30902-30917) · 40461 ff. wrong: the Indiculus luminosus heading is at 40473 · PL115 67764 ok · 68018 ok.
- Verdict after check: WHO (Melanchthon rule; thin own life; ancestry Contested)
- Note: Verdict unchanged.

### Flora and Maria, paired (Era4:94)
- Draft verdict: STORY (pair)
- Check: CONFIRMED
- Lines verified: PL115 62886-63062 ok (passage from 62898) · 63074 ok · 65875 ff. ok · 66764 ok · 66855 ok · 67481 ok.
- Verdict after check: STORY (pair; women rule; one eyewitness, Eulogius)
- Note: none.

### Berno, first abbot of Cluny (Era4:95)
- Draft verdict: LISTED
- Check: CORRECTED (substance)
- Lines verified: CLU 828-832 ok (830-832) · 8122-8126 ok · 14265-14268 ok (14267) · 14675-14677 ok (incipit only: "Ex quo divina dispensatio, etc.", 14681) · PL133 2944-2948 ok · 3728-3735 ok · 4073-4075 ok · 4318 ok · 4358 ok · 360/459/683/762 ok.
- Verdict after check: LISTED (judgment call; alternative WHO, thin life, following = Cluny)
- Note: The draft says "no early Life of Berno exists". No held line says so. Restate it as "none is held or was found" (CFT-Wants: not found). The verdict follows from the WANTED rule: the named Testament would carry his words, not a life.

### Odo of Cluny (Era4:96)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PL133 2783-2800 ok · 2938-2948 ok · 49541 ok · 40341, 55719 not opened (header pointers) · Occupatio file present · 296-312 ok (302-303) · 6654 header.
- Verdict after check: WHO (own works plus his disciple John's Life)
- Note: Keep Nalgod's later Life out, as the draft says.

### Odilo of Cluny (Era4:97)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PL142 79844-79860 ok (79856-79861) · 82363-82385 ok (82373-82384) · 81377, 74093-74110, 87721 not opened (header pointers).
- Verdict after check: WHO (own sermons plus his pupil Jotsald's Life)
- Note: The Life's date is still not stated in the lines read. Its prologue is addressed "ad Stephanum pontificem" (79859).

### Gerald of Aurillac (Era4:98)
- Draft verdict: STORY
- Check: CONFIRMED
- Lines verified: PL133 49541-49560 ok · 49562-49590 ok.
- Verdict after check: STORY (lay count with no own voice; Odo's Life from informants)
- Note: none.

### Ibn Hayyan (Era4:99), kept WANTED
- Draft verdict: WANTED
- Check: CONFIRMED (spot-check)
- Lines verified: file names searched (hayy, muqtab, idhari, maqqari): none. A text grep found only BAL 6290, 10764, 15523, 19592: other men named "ibn-Haiyan".
- Verdict after check: WANTED (would be WHO, OUTSIDE WITNESS; CFT-Wants: no edition before 1937)
- Note: Nothing held carries him.

### Stephen the Younger (Era4:100)
- Draft verdict: WHO (single Life, 42 years after death)
- Check: CORRECTED (lines)
- Lines verified: PG100 88560-88575 ok (88570-88573) · 88578-88582 ok (the "quadragesimo secundo ... anno ... ut auctor ipse testatur" quote is at 88585-88588) · 88618-88640 ok (88630-88638) · 88600-88612 wrong: "ex qua suam ipse Metaphrastes collegit" is at 88590.
- Verdict after check: WHO (early hagiographer's Life, dated by the volume; no own words)
- Note: Verdict unchanged.

### Theodore the Studite (Era4:101)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PG99 18804-18815 ok (18809-18816) · 3720-3726 ok (3725) · 76286 ok · 154784 ok · 3312-3318 ok (3314-3318) · 93676, 27047 not opened (header pointers).
- Verdict after check: WHO
- Note: none.

### Patriarch Nikephoros I (Era4:102)
- Draft verdict: WHO
- Check: CORRECTED (lines)
- Lines verified: PG100 1842-1850 ok · 1895-1900 wrong: "S. Nicephori parentes eximia pietate, et exsilio pro fide ... clari" is at 2111 · 1745-1760 ok (1746-1748) · 302-308 ok · 216 ok (214-220) · 2584 ok (also 1668-1669: born "circa annum 758") · 14713/45158/71724/82607 not opened (header pointers).
- Verdict after check: WHO
- Note: PG100 1746-1748 calls Ignatius Nikephoros's contemporary ("eidemque Nicephoro [a]equali"), which supports an early Life.

### Cyril (Constantine) and Methodius, paired (Era4:103)
- Draft verdict: WHO (pair)
- Check: CONFIRMED
- Lines verified: GINZEL 11219-11500 ok · 11488-11500 ok · 11982-12470 ok (11982-11998) · 11997 ok · 12994-13030 ok · 13728 ff. and 13845-13856 ok (13851-13857) · 12195-12225 not opened.
- Verdict after check: WHO (pair; contemporary witnesses held; the Lives' dates not stated in the lines read)
- Note: The draft's aside that the Legenda Italica "is a Latin original" is not in any held line; drop it. The codex also lists the hostile Salzburg Anonymous of 873 on Methodius (GINZEL 864-866), a further early witness.

## Era 4, draft G2 (Who_Scan_Era4.md l.104-124)

### Clement of Ohrid (Era4:104)
- Draft verdict: WHO (needs-ruling; date disputed)
- Check: CONFIRMED
- Lines verified: PG126 96725-96740 ok · 96740-96750 ok · 96758 ff. ok · 96770-96780 ok (96776-96785) · 97380-97395 ok (97382-97383) · 98426, 99371, 99594, 99649, 100270-100272 ok · GINZEL 12576-12577 ok · 1681-1700 ok.
- Verdict after check: WHO (needs-ruling: the heading ascribes the Life to Theophylact, d. 1107; the Monitum argues for a 10th-c. Bulgarian contemporary, "judicium penes Lectorem"; later-retelling question open)
- Note: The draft handles the needs-ruling case as the brief asks.

### Antony and Theodosius of the Caves, paired (Era4:105)
- Draft verdict: WHO (pair)
- Check: CORRECTED (lines)
- Lines verified: PAT 1248-1250 ok · 1254-1260 ok · 4241-4250 ok (4239-4252) · 1658-1664 ok · CROSS 11760-11790 ok · 12552-12700 ok · 15097 wrong: Sylvester's 6624 colophon is at 15109-15110 · 4670-4686 ok (4676-4678) · 4620-4640 ok.
- Verdict after check: WHO (pair; Nestor's Life of Theodosius marked in the held Paterik; the Primary Chronicle; pair is a judgment call)
- Note: Verdict unchanged.

### Boris and Gleb, paired (Era4:106)
- Draft verdict: STORY (pair)
- Check: CONFIRMED
- Lines verified: CROSS 10980-10990 ok (10986) · 11066-11082 ok (11076) · 11105-11125 ok (11120) · 11205-11240 ok (11214, 11235) · 11300-11322 ok (11305) · PSRL 5760-5765 ok · 5838-5860 ok · PAT 1254-1258 ok.
- Verdict after check: STORY (pair; princes with no own voice; judgment call)
- Note: none.

### Ilarion of Kyiv (Era4:107)
- Draft verdict: WHO (thin life)
- Check: CONFIRMED
- Lines verified: GORSKII 1124-2217 ok (title 1136-1146) · 2486-2500 ok (the Confession begins at 2502) · 178-190 ok · 741-760 ok · CROSS 11738-11748 ok (11741-11751).
- Verdict after check: WHO (Melanchthon rule; thin life)
- Note: none.

### Constantine-Silvanus (Era4:108)
- Draft verdict: LISTED (hostile; one witness for the teaching)
- Check: CONFIRMED
- Lines verified: PETER 2430-2440 ok · 2535-2546 ok (2538-2548) · 2644-2651 ok · 3396-3404 ok · 3466-3484 ok (3473-3481) · TC 14938-14960 ok · PETER 260-306 ok (see note).
- Verdict after check: LISTED (hostile witnesses; judgment call)
- Note: Gieseler (PETER 260-275) says one writer used the other's book (Engelhardt: Peter followed Photius), not that they "share a source". Either way Photius would not be an independent second witness. One more held witness exists: John of Odzun's Sermo contra Paulicianos (ODZUN 231, 322, running head 4061). It is an independent Armenian witness on Paulician teaching, but names neither founder. Whether it counts is Mark's call.

### Sergius-Tychicus (Era4:109)
- Draft verdict: LISTED (alternative WHO)
- Check: CONFIRMED
- Lines verified: PETER 3005-3024 ok · 3296-3310 ok · 3395-3404 and 3466-3484 ok · 3548-3560 ok (Greek extracts) · 3690-3700 ok · TC: no Sergius, as stated.
- Verdict after check: LISTED (hostile; the teaching rests on Peter's quotations; alternative WHO, Mark's call)
- Note: Same notes on Gieseler and John of Odzun as the row above.

### Karbeas and Chrysocheir, paired (Era4:110)
- Draft verdict: STORY (pair)
- Check: CONFIRMED
- Lines verified: TC 14950-14975 ok (14955-14968) · 24540-24548 ok (24544) · 25290-25296 ok · 25200-25206 ok · 97219-97573 ok (spot) · PETER 3757 ok · 3822-3830 ok (3825-3829).
- Verdict after check: STORY (pair; war leaders, no own voice; two hostile witnesses)
- Note: none.

### Peter of Sicily (Era4:111)
- Draft verdict: WHO (recorder, hostile, thin own life)
- Check: CONFIRMED
- Lines verified: PETER 785-797 ok (787-797) · 3825-3830 ok · 143-160 ok · 190-214, 236-262, 640-650 not opened (editor's reasoning, used only in the doubt).
- Verdict after check: WHO (recorder; hostile; thin own life; embassy 868)
- Note: none.

### Michael Keroularios (Era4:112)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: WILL 16715-16732 ok (16727-16730) · 17818-17826 ok (17822-17823) · 14954-14972 ok (14962-14965) · PSELL 20513-20516 ok (20511-20512) · 23852-23862 ok (23855-23861) · 3906-3913 ok (3909-3912) · 4056-4066 ok (4061-4064).
- Verdict after check: WHO (own letters; hostile legates; partisan encomium)
- Note: none.

### Nicholas I Mystikos (Era4:113)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PG111 1108-1135 ok · DEBOOR 4438-4443 ok · 4462-4466 ok · 5361-5365 ok · 4670-4680 ok (4672-4676) · 5214, 5356 not opened.
- Verdict after check: WHO (own letters; the Vita Euthymii is from the opposing side, written in or after 921)
- Note: de Boor (4660-4670) also says the biographer drew on those who lived with Euthymius.

### Theophanes the Confessor (Era4:114)
- Draft verdict: WHO (recorder)
- Check: CONFIRMED
- Lines verified: THEOPH 3714-3724 ok (3710-3714) · 640-700 ok · 1255-1262 ok (1259-1260) · 1405-1413 ok (1410) · 1705-1712 ok (1706-1710) · 336-345 ok (342, 345) · 2716 not opened.
- Verdict after check: WHO (recorder)
- Note: The volume does name candidate authors: the Life is "a Metaphraste, vel ex Baronii judicio a Theodoro Studita conscripta" (318-319). The date is still open. Theophanes also writes about himself in the Chronographia (the editor at 335-336: "de seipso scribit").

### al-Tabari (Era4:115)
- Draft verdict: WHO (OUTSIDE WITNESS, thin life)
- Check: CONFIRMED
- Lines verified: TAB4 header and content note ok (Arabic OCR fair, e.g. 3700-3706) · TAB5 content note ok · BAL 911-915 ok (910-914) · WATT 15786 ok.
- Verdict after check: WHO (OUTSIDE WITNESS; thin life, from two passing notes)
- Note: none.

### Ibn Ishaq (Era4:116)
- Draft verdict: WHO (OUTSIDE WITNESS; held text is Ibn Hisham's recension)
- Check: CONFIRMED
- Lines verified: WEIL 140-150 ok (139-144) · 150-170 ok · 986-1000 ok · 1240-1400 ok (Abyssinia 1240-1255) · BAL 666-668 ok (664-668) · Himyarites 2638 not opened (the scan's citation).
- Verdict after check: WHO (OUTSIDE WITNESS; thin life; recension flagged; judgment call)
- Note: none.

### Stepanos of Taron (Era4:117)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: MACLER 396-402 ok · 800-840 ok (798-842) · 918-925 ok (916-926) · GELZER 3695-3730 ok (3708-3721) · 14465 ok · MACLER 440-444, 1753 not opened.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Theodore Abu Qurrah (Era4:118)
- Draft verdict: WHO (thin life)
- Check: CONFIRMED
- Lines verified: GRAF 1148-1160 ok · 470-480 ok · 505-515 ok · 896-998 ok (915, 947, 989) · PG97 121450-121498 ok (121462-121474).
- Verdict after check: WHO (Melanchthon rule; thin life; dates uncertain)
- Note: none.

### Stephen Mansur (Era4:119)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: ASMAR3 50472 ok (50470) · 50496 ok (50492-50496) · 50535-50541 ok · 50440-50472 ok · 50619 ok.
- Verdict after check: WHO (recorder; very thin own life; "Mansur" is not in the volume)
- Note: The volume's dates are as the draft says: the Acts give 788 by their own count, and the Bollandists reckon 796 (50455).

### Grigol Khandzteli (Era4:120)
- Draft verdict: WHO (Life written about 90 years after his death)
- Check: CORRECTED (substance)
- Lines verified: PEET 11982-11990 wrong: the heading "IV. VIE DE S. GRÉGOIRE DE KHANDZTHA" is at 11994-11997 · 12090-12100 ok · 12105-12125 ok (12111-12117) · 14860-14880 misread: "mater Febronia" is the abbess of Mere (13505-13509, 14810), not Grigol's mother. Grigol arranges the life of his own, unnamed, mother (14869-14870), who dies at Mere (14873-14875) · 15242-15314 misread: this stretch is the career and death of Matoi, priest of Mere ("quibus Merae sacerdotio functus est", 15241-15256), not Grigol · 12281 wrong (12284-12288).
- Verdict after check: WHO (founder with a following; Life of 951, written 90 years after his death)
- Note: Grigol's own death is at PEET 16976-16988 (§71: he reached his 102nd year) and 17590-17594 (§89, which also says the Life was written in the 90th year after his death). Use these lines instead.

### Giorgi Merchule (Era4:121)
- Draft verdict: LISTED (alternative WHO)
- Check: CORRECTED (verdict)
- Lines verified: PEET 12111-12130 ok · 12130-12150 ok (§49, 12146-12150) · 12090-12125 ok.
- Verdict after check: WHO (recorder; very thin own life; name in doubt; alternative LISTED)
- Note: The rule says recorders (hagiographers) are WHO, with a thin own life flagged. The Life itself names him as its redactor and gives its date, 951. He speaks in his own person in §49. None of that is inferred. The scan treated him as a recorder-WHO if the Life were held, and it is now held. LISTED departs from the recorder rule. Peeters's chaplaincy guess stays a guess, so flag the life as very thin.

### John the Iberian and John Tornike, paired (Era4:122)
- Draft verdict: WHO (pair)
- Check: CONFIRMED
- Lines verified: PEET 402-425 ok · 740 ok (742) · 1005-1020 ok (1009, 1015) · 1109-1116 ok · 1180-1206 ok · 746 ok · 1104 ok · 590-640 ok · 628-632 ok · MEYER 1486, 4780 not opened (the scan's citations).
- Verdict after check: WHO (pair; Life c.1042; judgment call)
- Note: "About 40 years after John" is not in a held line. John's death (§20, PEET 1666-1671) has no year, but it comes before Euthymius's death in 1028, so the Life is still within a few decades.

### Euthymius the Athonite (Era4:123)
- Draft verdict: WHO (fold into the pair or separate: Mark's call)
- Check: CORRECTED (substance)
- Lines verified: PEET 3367-3371 ok (3366-3370; the editor adds "Haec omnia in annum 1028 aptissime quadrant") · 2020 ok · 3258 ok · 12090 ok · 3411 misread: the man who "ad Graecos se convertit" is George, his successor. By then Euthymius had resigned and given himself to translating (3373-3398; "librorum divinorum interpretatione se oblectabat", 3397-3398).
- Verdict after check: WHO (translator; following; Life c.1042; pairing Mark's call)
- Note: Verdict unchanged. Drop the 3411 "career as abbot" claim.

### Ishoyahb III (Era4:124)
- Draft verdict: WHO
- Check: CORRECTED (lines)
- Lines verified: DUVAL 100-150 ok · 3522-3530 wrong: the Arabs passage is at 3538 · 8618-8632 ok (8623-8630) · 9132-9224 ok · Seert 28727, Mingana 437-442 not opened (the scan's citations).
- Verdict after check: WHO (own letters plus Duval's life; flag that the life is a 1905 summary)
- Note: Verdict unchanged.

## Era 5, draft G3 (Who_Scan_Era5.md l.52-73)

### Innocent III (Era5:52)
- Draft verdict: STORY
- Check: CONFIRMED
- Lines verified: PL214 1075-1076 ok (1072-1073) · 1157-1172 ok (origin at 1176) · 1196-1203 ok (1195-1202) · 1395-1411 ok (1403-1408) · 1066-1068 ok (1066-1070) · 18381-18382 ok (18380-18383) · 640-660 ok.
- Verdict after check: STORY (pope rule; contemporary Gesta held; live profile flagged, as Heraclius was)
- Note: The special check is answered: none of his own non-chancery works is held anywhere in cic/texts. PL214 holds only the Gesta and the Registers. "De miseria" appears only in the Gesta's list of his works (1199). A Library-wide grep for De miseria, De contemptu mundi, De missarum mysteriis, De quadripartita specie nuptiarum and the consecration sermon ("minor Deo", "citra Deum") finds only a citation of De sacro altaris mysterio in Charon (charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt 31674). The sermons named in the Gesta (1201) are not held.

### Sava of Serbia (Era5:53)
- Draft verdict: WHO
- Check: CORRECTED (substance)
- Lines verified: DOM 231-232 ok (230-231) · 246-249 ok (251) · 17086-17101 ok · 6413-6416 ok (6415) · 396-399 misread: Daničić says the lament of King Vladislav at Sava's grave in Trnovo is *not* in this text ("у овом нема н. п. прекраснога плача ..."). It is in the reworked text printed in 1860. So it does not show that the held Life carries his death · MEYER 10172-10176 ok (10170-10172) · 10185-10188 ok (10181-10183).
- Verdict after check: WHO (own Typikon in the first person; early Life by his pupil Domentijan; death not shown in a readable line)
- Note: The draft's doubt about which text this volume prints is answered at DOM 287-297. It is the text Šafařík held to be genuine Domentijan, "as is written in the work itself", printed from a later copy. The colophon (17086-17101) calls Domentijan Sava's last pupil, writing at Karyes.

### Bernard of Clairvaux (Era5:54)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PL185 15360-15368 ok (15357-15368) · 15612-15620 ok (15614-15617) · 16330-16335 ok (16331-16334) · 23604-23606 ok · PL182 4861 ok · EALES1 8573-8592 ok · PL182 44357-44360 ok · 89957 ok · 91391 ok · EALES1 4360-4368 ok (4362-4364) · PL185 23993-24082 and PL183 not opened.
- Verdict after check: WHO
- Note: none.

### Robert of Molesme (Era5:55)
- Draft verdict: WHO (thin; Contested; needs-ruling; alternative LISTED)
- Check: CONFIRMED
- Lines verified: PL166 109184-109200 ok (109188-109193) · 109235-109245 ok · 109262-109294 ok (109264-109297) · 109398-109412 ok (109399-109405) · 109472-109490 ok (109472-109476) · 109536 ok (109534-109536) · 98833-98840 ok (98835-98836).
- Verdict after check: WHO (founder plus record; thin; the Exordium's date Contested; alternative LISTED)
- Note: No April volume of the Acta Sanctorum is held (only Martii 1 and 3, Maii 6, Junii 5, Augusti 1). The Exordium's prologue presents itself as by "Nos Cistercienses primi hujus ecclesie fundatores" (109219-109221). That is a claim made by the text, so the date stays Contested.

### Aelred of Rievaulx (Era5:56)
- Draft verdict: WHO (thin; the held Life is a later abridgement)
- Check: CONFIRMED
- Lines verified: PL195 14122-14128 ok · 14199 ok · 14241-14260 ok (14245) · 14296-14330 ok (14327-14330) · 14399-14412 ok (14406) · 14708-14714 ok (14714) · 47463-47478 ok (47466-47477) · 14772-14790 ok (14781).
- Verdict after check: WHO (Melanchthon rule; thin life; held Vita late, from Capgrave)
- Note: The Aelred volume does not name Walter Daniel. The "Walterum" (462) and "Gualtero Especo" (14140) hits are other men.

### Walter Daniel (Era5:57), kept WANTED
- Draft verdict: WANTED
- Check: CONFIRMED (spot-check)
- Lines verified: file names and text searched (walter daniel, gualterus daniel, vita ailredi, life of ailred): nothing.
- Verdict after check: WANTED (his Life of Ailred is not held)
- Note: Nothing held carries him.

### Bruno of Cologne (Era5:58)
- Draft verdict: WHO (thin early life; later Lives)
- Check: CORRECTED (substance)
- Lines verified: PL152 40452-40510 ok (encyclical 40452-40462; creed and 1101) · 227-232 ok (228-231) · 395-412 ok, but misdated (see note) · 4067-4072 ok (4066-4072) · 30722-30735 ok · 30838-30846 ok · LECOUT 11810-11829 ok (11814-11832) · 1743 not opened.
- Verdict after check: WHO (own letters, the 1101 encyclical, an early elogium; full Lives are 16th-c.; thin life flagged)
- Note: Two fixes. First, both of Bruno's letters are held in full in PL152. The letter to his brothers is at 29931 ff. ("Fratribus suis unice dilectis in Christo F. Bruno salutem") and the letter to Raoul le Verd at 30031 ff. ("Domino suo venerando Radulpho, Remensi praeposito ... Bruno salutem"), so his own words are not second-hand. Second, the editors date the Chronicon elogium to Guigo's lifetime, before 1138, by an author "synchrono" (PL152 378-396). The c.1400 writer (260-264) is a later annalist who cites the older chronicles. Both fixes strengthen the WHO.

### Hugh of Lincoln (Era5:59)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: DIMOCK 576-584 ok · 4171-4195 ok · 27628-27640 ok (27631-27637) · 1952-1961 ok (1950-1958).
- Verdict after check: WHO (early Life by his chaplain, built on his own talk)
- Note: none.

### Adam of Eynsham (Era5:60)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: DIMOCK 1774-1790 ok · 1989-2000 ok · 2205-2225 ok · 4171-4175 ok.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Norbert of Xanten (Era5:61)
- Draft verdict: WHO (founder plus record; needs-ruling; "no own words")
- Check: CORRECTED (substance)
- Lines verified: PL170 93204-93212 wrong: "VITA S. NORBERTI AUCTORE CANONICO PRAEMONSTRATENSI COAEVO" is at 93217-93220. Lines 93205-93210 are about another author, who wrote until 1241 · 93326-93340 ok · 100335-100356 ok (100337-100350) · 94494 ok (94492-94494) · 93502 not opened.
- Verdict after check: WHO (founder; needs-ruling on the Life's date; own words held but attribution to flag)
- Note: Own words are held. PL170 prints "Sancti Norberti Magdeburgensis archiepiscopi Sermones duo ad populum" (101359-101365 ff., printed from Hugo's Vie of 1704, so flag the attribution) and his diplomas ("ego Norbertus, Dei [gratia]", 101258-101260). The file name itself says "and-sermons".

### Hadewijch (Era5:62), kept WANTED
- Draft verdict: WANTED
- Check: CONFIRMED (spot-check)
- Lines verified: no Hadewijch or dbnl file in cic/texts or _intake. The only grep hits are namesakes: ASJUN5 61137, 78744 ("Hadewige", Hedwig) and the Welsh "hadewych" in the Rees volume (10311).
- Verdict after check: WANTED (Mark allows only the 1875 dbnl edition; it is not vendored)
- Note: Nothing held carries her.

### Marie d'Oignies (Era5:63)
- Draft verdict: WHO (hagiography flagged)
- Check: CONFIRMED
- Lines verified: ASJUN5 120156-120160 ok (120157-120160) · 121082-121095 ok (121088-121093) · 121749-121790 ok (121749; CAPUT I 121771-121775) · 124889-124892 ok · 125085-125140 ok (125100-125116).
- Verdict after check: WHO (women rule; early Life by Jacques de Vitry, c.1216; no own words)
- Note: The G3 drafter's Acta Sanctorum line numbers all hold. "Taught" has a firmer line than the counsel passage: Jacques says she, "de discipula in magistram subito conversa", read them many lessons (ASJUN5 123717-123719).

### Marguerite Porete (Era5:64)
- Draft verdict: WHO (hostile witnesses; Mirror link needs-ruling)
- Check: CONFIRMED
- Lines verified: LANGLOIS 16058-16072 ok · 16105-16115 ok (16104-16116) · 16135-16165 ok (articles 1 and 15 at 16162-16166) · MIRROR 3633 ok · 1744-1760 ok · "Porete" in MIRROR: 0 hits, as stated.
- Verdict after check: WHO (women rule: she taught by her book; life and teaching through hostile records; Mirror link not in any held line; alternative LISTED)
- Note: Judgment call, honestly flagged. The record shows her teaching others (LANGLOIS 16110-16112: she shared her writings with the bishop of Châlons and "pluribus aliis personis simplicibus, beghardis").

### Clare of Assisi (Era5:65)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: CLARE 1280-1290 ok (1278-1289) · 2406-2416 ok · 5689-5699 ok (5699) · 5628-5640 ok (5634-5635) · 9613 ok · 7270-7280 ok (7272-7277) · 4154-4300 not opened.
- Verdict after check: WHO (founder; Life of 1255-61; her own Rule in the first person)
- Note: none.

### Brother Leo (Era5:66)
- Draft verdict: WHO (recorder; attributions Contested)
- Check: CONFIRMED
- Lines verified: LEMMENS 103-135 ok (the quote is from the Chronica XXIV Generalium, death year from Wadding) · 176-192 ok (179-187) · 1416 ok · 949-1004 ok (945-1004) · 2800-2830 ok (2809-2820).
- Verdict after check: WHO (recorder; thin own life; Contested attributions)
- Note: none.

### Thomas of Celano (Era5:67)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: DALENCON 6484-6498 ok (6495-6496) · 199-250 ok · HOWELL 66-85 ok · 140-148 ok.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Agnes of Prague (Era5:68)
- Draft verdict: WHO (needs-ruling)
- Check: CONFIRMED
- Lines verified: SETON 297-300 ok (296-299) · 1822-1862 ok · 3408-3440 ok (3426) · 3020 ok (Clare's fourth letter, 3016-3024) · 4211, 716 not opened.
- Verdict after check: WHO (founder, women rule; Legend dated 1282-1328 by the editor's argument; needs-ruling)
- Note: none.

### Dominic (Era5:69)
- Draft verdict: WHO
- Check: CORRECTED (minor)
- Lines verified: ASAUG1 92238-92265 ok (92236-92240) · 92270-92300 ok (92282-92286) · 94619-94650 ok (94617-94633) · 61920-62030 ok (Humbert's Legenda discussed 61941-62032) · 109442-109452 ok (109443-109445).
- Verdict after check: WHO (founder; Jordan's and Bartholomew of Trent's early Lives)
- Note: The G3 Acta Sanctorum line numbers all hold. One misquote: the Vita altera reads "patre Felice, matre Joanna editus", so his father was Felix, not "patre Joanne".

### Jordan of Saxony (Era5:70)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: ALTANER 278-290 ok (278-283) · 4551-4553 ok · 1255-1270 ok (1260-1264) · 4488-4492 ok (4489-4491) · ASAUG1 92238-92265 ok · REICHERT 7788, 7829 ok.
- Verdict after check: WHO
- Note: none.

### Diana d'Andalo (Era5:71)
- Draft verdict: WHO (thin; alternative LISTED or pair with Jordan)
- Check: CORRECTED (substance)
- Lines verified: ALTANER 4425-4440 ok (4426-4438) · 4479-4510 ok (4483-4497) · 4532-4543 ok (4536-4542) · 1255-1270 ok · 4650-4662 ok (4658-4660) · 6043 misread: the note says Caecilia was not the first prioress, and that the prioress in letter VIII is Agnesia. It says nothing about Diana's office.
- Verdict after check: WHO (women rule: she led a circle of women and is asked to instruct her sisters; thin life, much of it Altaner's 1925 summary; judgment call, alternative LISTED)
- Note: Drop the 6043 claim. Whether she held office is simply not in the lines read.

### Gerard de Frachet (Era5:72)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: REICHERT 608-620 ok · 631-633 ok · 660-683 ok (661-667) · 863-872 ok (865-872) · 796-800 ok (see note).
- Verdict after check: WHO (recorder; thin own life)
- Note: The 1271 act (797-800) recalls suffrages to be said "post obitum eorum". It does not state that he had died. The draft already treats the death as inferred.

### Thomas Aquinas (Era5:73)
- Draft verdict: WHO
- Check: CORRECTED (minor)
- Lines verified: LEON4 861-866 ok (858-863) · ASMAR1 109140-109152 ok (109143-109152) · 109147-109150 ok · 109106-109112 ok (109105-109108) · 109207 ok (Bernard Gui at 109209-109212) · 109847-109848 ok · 114040 ok · 114891: text ok, but there a witness names Tocco as a promoter of the cause; he is not listed as a witness.
- Verdict after check: WHO
- Note: The G3 Acta Sanctorum line numbers all hold.

## Era 5, draft G4 (Who_Scan_Era5.md l.74-94; Supplement l.218; outside witnesses)

### Joachim of Fiore (Era5:74)
- Draft verdict: WHO (thin life; needs-ruling)
- Check: CONFIRMED
- Lines verified: BUON 3033 ok · 551-570 ok (541-560) · 586-590 ok (584-589) · 1182-1190 ok (1185) · 1400-1412 ok (1405-1406) · ASMAI6 78880-78882 ok · 78533 ok · 79081 ok (79082).
- Verdict after check: WHO (Melanchthon rule; thin life; Greco's Vita not used; needs-ruling)
- Note: none.

### Salimbene de Adam (Era5:75)
- Draft verdict: WHO (recorder; own life not thin)
- Check: CONFIRMED
- Lines verified: COULTON 1092-1100 ok (1097-1101) · 1672 ok · 2548 ok · 6971 ok · 7944-7950 ok · 2078-2082 ok.
- Verdict after check: WHO (recorder; life in his own words; extracts only)
- Note: The birth sentence (1097) is Coulton's voice. "My father was Guido" (1100) is Salimbene's.

### Valdes of Lyon (Era5:76)
- Draft verdict: WHO (two witnesses for the teaching)
- Check: CONFIRMED
- Lines verified: BOURBON 13340-13344 ok · 13374-13392 ok (13374-13393; informants 13351-13376) · 13349 ok (the note at 13355-13361) · 13415-13432 not opened · DOELL 2236-2250 ok (2244-2252) · 2410-2445 ok (2440) · 611-630 ok · MARTENE 134505-134545 ok (134500-134510) · CFT-Wants l.30 ok.
- Verdict after check: WHO (founder through enemies; Stephen of Bourbon plus the Bergamo record of 1218 by his followers; life on Stephen)
- Note: The Martène tractatus is not wholly a copy of Stephen. From 134570 its author writes from what he heard "a quibusdam ipsorum qui videntur ad fidem reversi, dum eorum interessem examinationibus". It is a possible further witness on the movement.

### Rainerius Sacconi (Era5:77)
- Draft verdict: WHO (recorder; own life in his own words; no thin flag)
- Check: CORRECTED (flag)
- Lines verified: MARTENE 133094 ok · 133107-133135 ok · 133316-133320 ok (133316) · 133354-133356 ok (133355) · 133140-133158 ok (133131-133151) · 133160-133215, 133746 not opened.
- Verdict after check: WHO (recorder; thin own life flagged)
- Note: The own-life core is one turn: 17 years a Cathar heresiarch, then a Dominican priest. The rest is from Sixtus (16th c.) and Martène. The recorder rule asks for the thin-life flag. The scan made the same point ("his life is only one turn").

### William of Tyre (Era5:78)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: WT1 3889-3893 ok · WT2 24903 ok · 26915-26930 ok (26914) · WT1 35664-35690 ok · 40273 ok.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Anselm of Canterbury (Era5:79)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PL158 3436-3470 ok (3434-3436) · 3510 ok (3507-3509) · 9555-9556 ok · 16866-16872 ok (16869) · 3773-3804 not opened.
- Verdict after check: WHO
- Note: none.

### Thomas Becket (Era5:80)
- Draft verdict: WHO
- Check: CORRECTED (substance)
- Lines verified: PL190 l.2 ok · 770 ok (768-770) · 14186-14192 ok (14189-14191) · 28735-28737: text ok, but it is not inside a Life. It is the "Narratio Thomae archiepiscopi Cantuariensis de ampulla olei sancti" in the Documenta historica (heading 28728-28731) · 54832 wrong: "EPISTOLA I." there is the first letter of Gilbert Foliot ("EPISTOLAE GILBERTI FOLIOT", 54829).
- Verdict after check: WHO (own letters, early Lives, following)
- Note: Becket's own letters are at PL190 31724-31730 ff. ("SANCTI THOMAE CANTUARIENSIS ARCHIEPISCOPI EPISTOLAE. EPISTOLA PRIMA. AD PAPAM ALEXANDRUM"). Cite those. Treat the Narratio as a document ascribed to him, not as his letters.

### Jacques de Vitry (Era5:81)
- Draft verdict: WHO (recorder)
- Check: CONFIRMED
- Lines verified: ROHR 5625-5633 ok (5636-5637) · 5859-5861 ok · 6283-6296 ok · JDVH 8706 ok · 10004 ok · 20-45, 847-960 not opened.
- Verdict after check: WHO (recorder; own letters)
- Note: none.

### Hugh de Payens (Era5:82)
- Draft verdict: WHO (founder; thin life)
- Check: CONFIRMED
- Lines verified: CURZON 2327 ok · 2371 ok · WT1 35664-35690 ok · 40273 ok · SCHN 2907-2913 ok · 3552-3553 ok · 6330-6332 ok · PL182 91440-91448 ok · 3874 ok.
- Verdict after check: WHO (founder with a following; near-contemporary witnesses; thin life)
- Note: The death date has firmer ground than Schnürer's "wahrscheinlich". Curzon's note (2375-2377) gives 24 May 1136 from the obituary of the Temple at Reims. PL182 91458 also cites Bernard's letter 31 addressed to him.

### Adam of Bremen (Era5:83)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: STEIN 564-612 ok · SCHM 3681-3688 ok (3679-3685) · STEIN 674 not opened.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Anna Komnene (Era5:84)
- Draft verdict: WHO (recorder, thin own life; no OUTSIDE WITNESS label)
- Check: CONFIRMED
- Lines verified: ALEX 1068-1079 ok · 25070-25196 ok · 25263-25277 ok (25262-25272) · Who_Scan_Era5 l.84 ("Call: WANTED without the label") ok · Opus_Check_Notes l.109 ok · Decision-Log l.2446 ok.
- Verdict after check: WHO (recorder; thin own life; Greek only; no label)
- Note: The label question is settled by the standing precedent as well as by l.2446. The era 8 entry (Decision-Log l.2333) applies the era 7 Herberstein precedent: "a Christian writer is inside Christianity, whatever the church". Procopius (era 3) predates that precedent; the difference is worth noting to Mark.

### Basil the Physician (Era5:85)
- Draft verdict: LISTED (one record)
- Check: CORRECTED (substance)
- Lines verified: ALEX 25092-25114 ok (25093-25110) · 25110 ok · 25188-25196 ok (25188-25192) · 25263-25277 ok · ZIG 404-415 ok (402-415) · 433-448 ok (Latin 447-449) · ZIG preface 244-262 ok (244-256) · 262-275 ok (256-280).
- Verdict after check: LISTED (founder through enemies; both held witnesses rest on the one interrogation; hostile; alternative WHO, Mark's call)
- Note: The draft says Anna gives no doctrine. She gives some: Basil as "Satanael's arch-satrap" (25109); he called the churches temples of demons and held the Eucharist worthless (25172-25176); the Bogomils believe angels will snatch them from the pyre (25188-25190). These come from the same session the scribe recorded behind a curtain (25150-25160), which Zigabenos used (ZIG 244-256). So there is still one witness for the teaching, and LISTED follows, as the scan foresaw.

### George the Hagiorite (Era5:86)
- Draft verdict: WHO (Life in Latin; own works not held)
- Check: CONFIRMED
- Lines verified: PEET 3823 ok · 3985-4010 ok (3998-4010) · 4172-4180 ok (4176) · 3905-3912 ok (3909-3910) · 613 ok · 661 ok · 3826-3835 not opened.
- Verdict after check: WHO (early Life by his disciple, 1066-1072; translated by Peeters, volume issued 1922)
- Note: none.

### Gregory Pakourianos (Era5:87)
- Draft verdict: WHO (own-voice typikon; thin life; needs-ruling)
- Check: CONFIRMED
- Lines verified: MOUS 142-143 ok (140-143) · 7187 ok · 7312-7318 ok (7316) · 7836-7842 ok (7835-7840) · 8132 ok · 8346-8378 ok · 7018-7030, 7090-7200, 10062 not opened.
- Verdict after check: WHO (founder's typikon in his own person, in a later Greek version; thin life; needs-ruling)
- Note: The draft's doubt is answered in the volume. The Greek is a later metaphrast's version, which Mousaios copied as he found it (7879-7885). The heading says it was written "in Greek, Iberian and Armenian" under Alexios Komnenos, "ἐν ἔτει σωτηρίῳ" (OCR "anxd'"), indiction 7, in December (7893-7901); Mousaios reads the year as 1084 (7316).

### Domentijan and Teodosije, paired (Era5:88)
- Draft verdict: WHO (pair; only Domentijan's half held)
- Check: CORRECTED (verdict)
- Lines verified: DOM l.1 ok · 231-262 ok (230-251) · 305-320 ok (317) · 345-375 ok (349, 370-371).
- Verdict after check: split. Domentijan: WHO (recorder; thin own life; Sava's last pupil, colophon 17086-17101). Teodosije: WANTED (his reworked Life, printed 1860, is not held; Daničić dates it to the first half of the 14th c., which would make him an era 6 row by date of work). Pairing is Mark's call.
- Note: A pair WHO would give Teodosije a WHO with no held source. The held preface also undercuts the pairing: Daničić says Teodosije reworked Domentijan's Life about a century later (370-371). The scan's premise was two 13th-c. writers of the same Life.

### Nestor the chronicler (Era5:89)
- Draft verdict: WHO (recorder; thin; chronicle authorship Contested)
- Check: CORRECTED (substance)
- Lines verified: CROSS 4333-4340 ok (4332-4336) · 4494-4504 ok (4493-4498) · 4520-4530 ok (4520-4526) · PAT 6452 ok · 4500 ok · 16704-16708 ok (16706-16708).
- Verdict after check: WHO (recorder; thin own life; Contested authorship of the whole chronicle)
- Note: The draft could not find his Life of Theodosius. It is held: PAT 1249-1251 is headed "Списано Нестеромъ, мнихомъ того-же Печерьскаго монастыря. Слово 8-ое". His own first-person preface is at 1253-1262 ("азъ грешный Нестеръ"), and it names his earlier Boris and Gleb work. Slovo 9, his account of the translation of the relics, is at 4239-4241. His own life in his own words is quoted in CROSS 4668-4675: received, tonsured and made deacon under Prior Stephen.

### Cyril III ibn Laqlaq (Era5:90)
- Draft verdict: LISTED (later retelling)
- Check: CONFIRMED
- Lines verified: REN 34576-34584 ok (34576-34586) · 34934-34968 ok (34930-34970) · 35524-35530 ok (35524-35533) · 35086-35092, 35146-35158 not opened.
- Verdict after check: LISTED (the Kuntsevych precedent: a later retelling held, the early source not held)
- Note: Renaudot (1713) summarizes "Autor quem sequimur", which Makrizi abridged (35533-35535). That author is not named or held, so the held text is a later retelling. The precedent is Decision-Log l.2443.

### Marco Polo (Era5:91)
- Draft verdict: WHO (OUTSIDE WITNESS)
- Check: CORRECTED (verdict: label)
- Lines verified: POLO1 18130-18143 ok · 17414-17418 ok (17414-17416) · 5025-5056 ok (5035-5045) · 9362, 7636, 10274 not opened.
- Verdict after check: WHO (recorder/traveller; thin own life; no OUTSIDE WITNESS label)
- Note: The label conflicts with the standing calls. Era 7: "Western envoys and travellers carry no OUTSIDE WITNESS label (Herberstein is a Catholic imperial envoy, inside Christianity)" (Decision-Log l.2267; era 7 Opus_Check_Notes l.50, 110). Era 8 restates it: "a Christian writer is inside Christianity, whatever the church" (l.2333). Polo is a Venetian Catholic. The era 5 scan applied the label before those calls, so flag the change to Mark.

### William of St Thierry (Era5:92)
- Draft verdict: WHO (recorder, thin own life)
- Check: CONFIRMED
- Lines verified: PL185 l.2 ok · 15486 ok · 15503 ok (15497-15500) · 15353-15364 ok (15357-15360) · 15540-15572 ok.
- Verdict after check: WHO (recorder; thin own life)
- Note: none.

### Stephen Harding (Era5:93)
- Draft verdict: WHO (thin; needs-ruling)
- Check: CONFIRMED
- Lines verified: PL166 99000-99040 ok · 99636-99690 ok (1109 at 99652-99653; resignation 99681-99688) · 99694 ok · 99858 ok · 99920-99976 ok · 109184-109213 ok.
- Verdict after check: WHO (Melanchthon rule; thin; needs-ruling on the Exordium's date)
- Note: none.

### Humbert of Romans (Era5:94)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: BERTH1 l.1 ok · 690-712 ok (692-712) · 945-956 ok (953-954) · 1180-1190 ok (1184) · 395, 766-776 not opened.
- Verdict after check: WHO (own works, following, life from early witnesses quoted by Berthier)
- Note: BERTH1 709-710 also has his own word that he travelled the Holy Land ("ipsemet peragrasse testatur").

### Peter Abelard (Supp:218)
- Draft verdict: WHO
- Check: CONFIRMED
- Lines verified: PL178 header ok · 7112-7125 ok · 7154 ok (7123-7125) · 7246 ok · 3228-3240 ok (3226-3239).
- Verdict after check: WHO (own Historia calamitatum; own works; following)
- Note: none.

### Ibn al-Athir (outside witness 1)
- Draft verdict: WHO (OUTSIDE WITNESS)
- Check: CONFIRMED
- Lines verified: RHC1 24620-24650 ok · 24912-24915 ok (24911-24914) · 28456-28461 ok · 29720 ok · 31030 ok (31033) · 52960-52984 ok · RHC2 147-150 ok · 160-170 ok (155-162).
- Verdict after check: WHO (OUTSIDE WITNESS; partisan toward his patrons, as the editors say)
- Note: The held OCR is the French translation. The Arabic is not captured (Wanted_Sources l.548), so "Arabic with the French" overstates what is held.

### Usama ibn Munqidh (outside witness 2)
- Draft verdict: WHO (OUTSIDE WITNESS)
- Check: CONFIRMED
- Lines verified: HITTI 530-536 ok (533) · 1103 ok (1103-1105) · 1433-1436 ok (1435) · 8508-8530 ok (8510-8528) · 6146-6164 ok · 8335-8349 ok · 8417 not opened.
- Verdict after check: WHO (OUTSIDE WITNESS; memoir, English translation)
- Note: none.

### Ibn Jubayr (outside witness 3)
- Draft verdict: WHO (OUTSIDE WITNESS; thin life)
- Check: CONFIRMED
- Lines verified: WRIGHT l.2, l.9 ok · 2674 ok · 2734 ok (2734-2735) · 2406 ok · 2800 ok · 2138 ok · 13962-13968 ok (13964-13967).
- Verdict after check: WHO (OUTSIDE WITNESS; thin life; poor OCR)
- Note: The Arabic quotes are where the draft says.

### Benjamin of Tudela (outside witness 4)
- Draft verdict: WHO (OUTSIDE WITNESS; thin life)
- Check: CONFIRMED
- Lines verified: ADLER 336-350 ok (341) · 1015-1022 ok (1019) · 1085 ok · 993-1012 ok (993) · 1385-1390 ok (1386).
- Verdict after check: WHO (OUTSIDE WITNESS; thin life)
- Note: none.

---

## Summary table

| Person | draft | after check | result |
|---|---|---|---|
| John of Damascus | WHO (thin) | WHO (thin; 10th-c. Life) | CORRECTED (substance) |
| Anskar | WHO | WHO | CORRECTED (lines) |
| Rimbert | WHO (recorder, thin) | WHO (recorder, thin) | CORRECTED (lines) |
| Alfred the Great | WHO | WHO | CONFIRMED |
| Dunstan | WHO | WHO | CONFIRMED |
| Æthelwold | WHO | WHO | CONFIRMED |
| Oswald | WHO | WHO (Life dated 995-1005) | CORRECTED (substance) |
| Benedict Biscop and Ceolfrid | WHO (pair) | WHO (pair) | CORRECTED (lines) |
| Þorgeir | LISTED | STORY (alt LISTED) | CORRECTED (verdict) |
| Benedict of Aniane | WHO | WHO | CONFIRMED |
| Eulogius | WHO | WHO | CORRECTED (lines) |
| Paulus Alvarus | WHO (thin) | WHO (thin) | CORRECTED (lines) |
| Flora and Maria | STORY (pair) | STORY (pair) | CONFIRMED |
| Berno | LISTED | LISTED (alt WHO thin) | CORRECTED (substance) |
| Odo of Cluny | WHO | WHO | CONFIRMED |
| Odilo of Cluny | WHO | WHO | CONFIRMED |
| Gerald of Aurillac | STORY | STORY | CONFIRMED |
| Ibn Hayyan | WANTED | WANTED | CONFIRMED (spot-check) |
| Stephen the Younger | WHO | WHO | CORRECTED (lines) |
| Theodore the Studite | WHO | WHO | CONFIRMED |
| Nikephoros I | WHO | WHO | CORRECTED (lines) |
| Cyril and Methodius | WHO (pair) | WHO (pair) | CONFIRMED |
| Clement of Ohrid | WHO (needs-ruling) | WHO (needs-ruling) | CONFIRMED |
| Antony and Theodosius | WHO (pair) | WHO (pair) | CORRECTED (lines) |
| Boris and Gleb | STORY (pair) | STORY (pair) | CONFIRMED |
| Ilarion of Kyiv | WHO (thin) | WHO (thin) | CONFIRMED |
| Constantine-Silvanus | LISTED | LISTED | CONFIRMED |
| Sergius-Tychicus | LISTED | LISTED (alt WHO) | CONFIRMED |
| Karbeas and Chrysocheir | STORY (pair) | STORY (pair) | CONFIRMED |
| Peter of Sicily | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Michael Keroularios | WHO | WHO | CONFIRMED |
| Nicholas I Mystikos | WHO | WHO | CONFIRMED |
| Theophanes the Confessor | WHO (recorder) | WHO (recorder) | CONFIRMED |
| al-Tabari | WHO (OW) | WHO (OW, thin) | CONFIRMED |
| Ibn Ishaq | WHO (OW) | WHO (OW, thin) | CONFIRMED |
| Stepanos of Taron | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Theodore Abu Qurrah | WHO (thin) | WHO (thin) | CONFIRMED |
| Stephen Mansur | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Grigol Khandzteli | WHO | WHO | CORRECTED (substance) |
| Giorgi Merchule | LISTED | WHO (recorder, very thin; alt LISTED) | CORRECTED (verdict) |
| John the Iberian and John Tornike | WHO (pair) | WHO (pair) | CONFIRMED |
| Euthymius the Athonite | WHO | WHO | CORRECTED (substance) |
| Ishoyahb III | WHO | WHO | CORRECTED (lines) |
| Innocent III | STORY | STORY | CONFIRMED |
| Sava of Serbia | WHO | WHO | CORRECTED (substance) |
| Bernard of Clairvaux | WHO | WHO | CONFIRMED |
| Robert of Molesme | WHO (thin) | WHO (thin; alt LISTED) | CONFIRMED |
| Aelred of Rievaulx | WHO (thin) | WHO (thin) | CONFIRMED |
| Walter Daniel | WANTED | WANTED | CONFIRMED (spot-check) |
| Bruno of Cologne | WHO (thin) | WHO (thin) | CORRECTED (substance) |
| Hugh of Lincoln | WHO | WHO | CONFIRMED |
| Adam of Eynsham | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Norbert of Xanten | WHO (needs-ruling) | WHO (needs-ruling) | CORRECTED (substance) |
| Hadewijch | WANTED | WANTED | CONFIRMED (spot-check) |
| Marie d'Oignies | WHO | WHO | CONFIRMED |
| Marguerite Porete | WHO | WHO (alt LISTED) | CONFIRMED |
| Clare of Assisi | WHO | WHO | CONFIRMED |
| Brother Leo | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Thomas of Celano | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Agnes of Prague | WHO (needs-ruling) | WHO (needs-ruling) | CONFIRMED |
| Dominic | WHO | WHO | CORRECTED (minor) |
| Jordan of Saxony | WHO | WHO | CONFIRMED |
| Diana d'Andalo | WHO (thin) | WHO (thin; alt LISTED) | CORRECTED (substance) |
| Gerard de Frachet | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Thomas Aquinas | WHO | WHO | CORRECTED (minor) |
| Joachim of Fiore | WHO (thin) | WHO (thin) | CONFIRMED |
| Salimbene de Adam | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Valdes of Lyon | WHO | WHO | CONFIRMED |
| Rainerius Sacconi | WHO (recorder) | WHO (recorder, thin own life) | CORRECTED (flag) |
| William of Tyre | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Anselm of Canterbury | WHO | WHO | CONFIRMED |
| Thomas Becket | WHO | WHO | CORRECTED (substance) |
| Jacques de Vitry | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Hugh de Payens | WHO (thin) | WHO (thin) | CONFIRMED |
| Adam of Bremen | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Anna Komnene | WHO (no label) | WHO (no label) | CONFIRMED |
| Basil the Physician | LISTED | LISTED | CORRECTED (substance) |
| George the Hagiorite | WHO | WHO | CONFIRMED |
| Gregory Pakourianos | WHO (needs-ruling) | WHO (needs-ruling) | CONFIRMED |
| Domentijan and Teodosije | WHO (pair) | split: Domentijan WHO; Teodosije WANTED (era 6 candidate) | CORRECTED (verdict) |
| Nestor the chronicler | WHO (recorder) | WHO (recorder) | CORRECTED (substance) |
| Cyril III ibn Laqlaq | LISTED | LISTED | CONFIRMED |
| Marco Polo | WHO (OW) | WHO (recorder, no label) | CORRECTED (verdict: label) |
| William of St Thierry | WHO (recorder) | WHO (recorder) | CONFIRMED |
| Stephen Harding | WHO (thin) | WHO (thin) | CONFIRMED |
| Humbert of Romans | WHO | WHO | CONFIRMED |
| Peter Abelard | WHO | WHO | CONFIRMED |
| Ibn al-Athir | WHO (OW) | WHO (OW) | CONFIRMED |
| Usama ibn Munqidh | WHO (OW) | WHO (OW) | CONFIRMED |
| Ibn Jubayr | WHO (OW) | WHO (OW, thin) | CONFIRMED |
| Benjamin of Tudela | WHO (OW) | WHO (OW, thin) | CONFIRMED |

OW = OUTSIDE WITNESS.

**Counts.**
- Era 4 (43 rows: G1 22, G2 21): confirmed 27, corrected 16 (lines 9, substance 5, verdict 2), unsupported 0.
- Era 5 (48 rows: G3 22, G4 26, including Abelard and the four outside witnesses): confirmed 36, corrected 12 (substance 7, minor 2, verdict 2, flag 1), unsupported 0.
- All 91 rows: confirmed 63, corrected 28, unsupported 0.

**Verdicts that change after the check (4):** Þorgeir LISTED to STORY; Giorgi Merchule LISTED to WHO; Domentijan and Teodosije split (Domentijan WHO, Teodosije WANTED); Marco Polo loses the OUTSIDE WITNESS label. One flag is added (Rainerius: thin own life). All other verdicts stand, some with corrected lines or claims.
