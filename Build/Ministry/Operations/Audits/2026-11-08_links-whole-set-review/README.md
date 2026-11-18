# Whole-set review of the links, eras 1 to 9 (P2-L11), 2026-11-08

Each era's links were reviewed only inside that era. This pass looked across all of eras 1 to 9 for what no single era could see. Base: `main` at 6fd6b43a (data release 16), after eras 6 to 9, the era 9 split, the major-links pass (#1543) and the Armenian Apostolic follow-up (#1551) had merged. Era 10 is out of scope (Decision-Log, "The link work covers eras 1 to 9", 2026-11-08). Output: data release 17.

## Steps and rounds

1. **Inventory** (a script): `Inventory.json`. 575 links touch eras 1 to 9, each with type, grade, outcome, note, sources and the era folder that drafted it. A second script ran the mechanical cross-checks: `Mechanical_Checks.json` (pairs with more than one link, quotes shared between links, "continued as" chains, `continuesAs` mismatches, reading scores, long sentences).
2. **Cross-era drafts** (Opus, one agent per theme, each in its own scratch directory): `Draft_A_structure.json` (duplicates, contradictions, chains), `Draft_B_grades.json` (type and grade consistency), `Draft_C_major.json` (major links and outcomes), `Draft_D_notes.json` (register, reading level, spelling), `Draft_E_quotes.json` (44 quotes read in context). Merged in `Findings_Record.json` with the fix list that was applied.
3. **Review round 1** (a separate Opus 5.5 agent, full): `Opus_Review_Round1.json`. Revise: 0 blocking, 2 substantial, 9 minor. Applied: `Revision_Round1.json`.
4. **Review round 2** (separate Opus 5.5, targeted): `Opus_Review_Round2_TargetedRecheck.json`. Revise: 0 blocking, 1 substantial, 2 minor. Applied: `Revision_Round2.json`.
5. **Review round 3** (separate Opus 5.5, targeted): `Opus_Review_Round3_TargetedRecheck.json`. **Pass**: 0 findings. All three rounds of the cap were used; the pass cleared on the third.

No model call was metered. All drafting and review ran in-session.

## Counts

- Links in scope: 575 at the start; 575 at the end (one retired, one restored).
- Findings in the cross-era drafts: 43 (20 substantial, 23 minor, none blocking). Applied: 30. Held for Mark: 7. Logged for the census owner: 4. Logged with no change: 2.
- Review findings: 14 in rounds 1 and 2, all applied.
- Links changed: 138. Fields changed: 118 notes, 21 source lists, 13 citation specificities, 10 outcomes, 2 types.
- Retired: `puritanism--restoration-georgian-church-of-england`, replaced by the English Old Dissent link (`retiredLinks`).
- Restored: `russian-church-stoglav-to-nikon--the-old-believers--2` (gave rise to, Documented), drafted and reviewed in era 8 but dropped at its merge by an ID collision.
- Major links by outcome: 91 to 92 (three added, where the sources show a council or papal act; two removed as adoption by vote).

## Findings by kind

| Kind | Found | What was done |
|---|---|---|
| Note (reading level, internal language, spelling, self-standing) | 8 | 82 early-era notes that failed Reading Ease 60 or FK 10 rewritten, every fact kept; 15 notes that spoke of "texts we hold" rewritten; 5 long sentences split; 2 British spellings. House punctuation (quote marks) logged for the owner. |
| Major-link inconsistency | 7 | Outcomes added where the link's own sources show a council act (Constance on Hus and on Wyclif; the 1540 approval of the Jesuits). Two removed under "adoption by vote is minor" (the 410 Persian synod; Trullo canon 2). One sentence split. One held for Mark. |
| Outcome not shown by its own sources | 5 | Verbatim quotes added from the same works (Paul of Samosata, Aquileia, Whitby, four more); the Carmelite Outremer and Diamper outcomes narrowed; the recusant outcome corrected. |
| Duplicate or overlap | 4 | The 1662 ejection retired from one of its two links; the 451 rupture and a Macarius quote no longer told twice. The Bogomil-to-Cathar pair held for Mark. |
| Type or grade inconsistency | 4 | One "influenced" retyped to "in contact with", as seven like links are; 13 citation specificities set to A where a line-located quote stands. Two held for Mark. |
| Other | 7 | Source shape for vendored secondaries held for Mark; four editors' statements relabeled secondary, as other eras label them. |
| Quote in context | 3 | A clipped Sotelo quote that reversed its sense is replaced, and the note now says what the source says. The Palestine-to-Jerusalem note now gives the real reason it is thin. One logged. |
| continuesAs | 3 | Logged for the census owner. |
| Chain | 1 | The St Thomas Christians link into era 9 retyped from "continued as" to "gave rise to", with the 1847 letter added. |
| Contradiction | 1 | The Old Believers' "grew out of" claim had no link; the era-8 link restored. |

Every finding, with its evidence and status: `Findings_Record.json`.

## Checks

- Every changed note and outcome scores Reading Ease 60 or more and FK 10 or less with `engine.m7.turn_readability.score_turn`; none has a sentence past 25 words.
- `validate-census.mjs --base` (release 16) `--atlas --tree`: 0 errors; no link ID gone without a `retiredLinks` entry.
- `engine.m6.cli check` and `atlas-check --edges-only`: clean. `build_tree_site.mjs`: 0 mismatched.

## Open items

Held for Mark (each needs a reading of a method rule or a census question, not a fix this pass could make):

1. **A lone nineteenth-century account (GRD-04).** A link resting only on one 19th- or early-20th-century account that states the tie is Dominant Modern Reconstruction in 10 links (Mouravieff, Brosset, Rački, Lutzow; eras 4-5) and Inferential-Thin in 4 (Curzon, Anjou, Conybeare, Rees; eras 4-7). The reviewer recommends Inferential-Thin for all.
2. **What "verified-direct" means, and the shape of a vendored secondary source (GRD-06, GRD-01 to 03).** The Drafting Brief has verified-direct mean the quote shows the relationship; most eras use it to mean the lines were read and match. The Brief gives secondary sources no file, lines or quote; eras 4, 7, 8 and 9 keep them on vendored secondaries, and era 5 removed them, which leaves six secondary-only links marked A and verified-direct with nothing behind them.
3. **A bishop deposed by a ruler, no council named (MAJ-06).** Major in era 3 (Reparatus of Carthage, Nerses Bakur), minor in era 8 (Avedik).
4. **The Bogomil-to-Cathar link drawn twice (STR-02).** Part of "The Bogomil entries overlap" (Open-Gaps, 2026-11-08).

For the census owner (movement fields, not links):

- Six `continuesAs` fields name a successor the links type as "influenced" or "gave rise to"; 21 "continued as" links start at a movement with no `continuesAs`; the Armenian after-Avarayr field skips the movement between (STR-07 to STR-09).
- The Old Believers' summary says "grew out of Muscovite Christianity"; the restored link runs from the Russian church before Nikon.
- The Anomoean summary says the council "formally cursed" that party; the links now say "condemned".
- House punctuation: 131 notes quote with single marks, 7 with double; the full stop sits outside the closing mark in about 88 places and inside in about 19.
- No entry covers the Malankara church between 1665 and 1912 (STR-03).

Logged, no change: the Lutheran confessional revival link rests on Jacobs's 1911 preface, after the movement's end (an era 9 call, QUO-03); P2-ML's wanted-texts line asking to re-judge the 585 synod link as major is now ruled out by "adoption by vote is minor" (MAJ-15).

## Wanted texts, merged across eras 1 to 9

Source: the "Wanted texts" section of each of the twelve audit READMEs, and every `wants` array in their Draft, Drafting_Record, Revision, Final and Draft_Era JSON files (Build/Ministry/Operations/Audits/, 2026-11-07 to 2026-11-08).

Counts: 2932 raw want entries (JSON wants plus README bullets, repeated across drafts, revisions and finals, plus 7 README-only items); 625 merged texts in the groups below; 10 texts already vendored under cic/texts/ (listed last).

Links are the link ids each want was attached to. "no link id" means the want was not tied to a link in its source.


### Would raise links to Documented (438)

- 1846 bull of excommunication and 1846 covenant of the Evangelical Church of Armenians; Missionary Herald reports 1846-47. Unlocks: would document the 1846 break. Links: no link id. Eras: era 9 part 2.
- 1847 and 1876 Malankara documents, in full. Unlocks: would document the Malankara split from the church's own texts. Links: no link id. Eras: era 9 part 1.
- 1883 law on Old Believers; Synod or state texts on the Old Believers (1815-1906). Unlocks: would document the state's treatment of the Old Believers. Links: russian-church-synodal-century--the-old-believers. Eras: era 9 part 2.
- 1931 Seventh-day Adventist Yearbook statement of twenty-two beliefs. Unlocks: would document the Adventist statement of belief. Links: restorationist-apocalyptic-ferment-and-adventism--seventh-day-adventist-church-twentieth-century. Eras: era 9 part 1.
- 1961 Initiative Group letters; Council of Prisoners' Relatives bulletins (1964-). Unlocks: would document the Initsiativniki split from their own side. Links: russian-evangelicals-stundists--persecuted-church-worlds-of-the-communist-era-in. Eras: era 9 part 1.
- A Debate on the Roman Catholic Religion between Alexander Campbell and John B. Purcell (1837). Unlocks: would document the Campbell-Purcell debate. Links: the-stone-campbell-restoration-movement--catholic-church-long-nineteenth-century. Eras: era 9 part 1.
- Abdisho of Nisibis, preface to the synod of Timothy II (1318), readable edition. Unlocks: would document the 1318 synod. Links: church-of-the-east-under-the-mongols--church-of-the-east-timur-to-hakkari. Eras: era 5.
- Abraham Kuyper, Het conflict gekomen (1886) and Lectures on Calvinism (1898). Unlocks: would document the Doleantie and sphere sovereignty. Links: no link id. Eras: era 9 part 1.
- ACO ser. 2, vol. 1 (Riedinger), the Lateran acts of 649. Unlocks: would replace the long-s OCR for the African letters of 646. Links: latin-africa-under-byzantium--byzantine-imperial-church-heraclian-iconoclast. Eras: era 3, major links era 3.
- Act of Supremacy (1534) and Act in Restraint of Appeals (1533). Unlocks: would document the English side of the break. Links: no link id. Eras: era 7.
- Acta Ecclesiae Mediolanensis in later use outside Milan, and a cleaner OCR of the 1582 or 1599 printing. Unlocks: would raise the Milan-to-Trident link and fix the seminary decree. Links: no link id. Eras: era 7.
- Acta et decreta Concilii Plenarii Americae Latinae (1899/1900). Unlocks: would document the 1899 council. Links: catholic-church-long-nineteenth-century--nineteenth-century-latin-american-catholicism. Eras: era 9 part 2.
- Acta of the Synod of Dort (Latin, 1620). Unlocks: would document the foreign deputies' subscriptions. Links: no link id. Eras: era 7.
- Acts of the 2000 Jubilee Council canonization of the Optina elders and monks. Unlocks: would document the canonization. Links: the-optina-elders-and-russian-ascetic-renewal--the-russian-new-martyrs-and-the-catacomb-church. Eras: era 9 part 2.
- Acts of the Council of Constantinople, September 1872, the definition on phyletism. Unlocks: would document the phyletism definition. Links: no link id. Eras: era 9 part 2.
- Acts of the Fourth Lateran Council (Mansi XXII), including canon 68 on dress. Unlocks: would document the patriarch's presence and the dress rule. Links: latin-papal-church-gregorian--maronite-christianity. Eras: era 5.
- Acts of the Moscow council of 1666-67 (Dopolneniia k Aktam istoricheskim, vol. V). Unlocks: would give the council's own anathema and revocation of the Stoglav. Links: russian-church-stoglav-to-nikon--the-old-believers. Eras: era 8.
- Acts of the Second Council of Nicaea (787), session 7 acclamations (Mansi XIII). Unlocks: would document the council's honor of John of Damascus. Links: no link id. Eras: era 4.
- Ad nostrum, full text (Clementines V.3.3). Unlocks: would show the decree naming the beguines. Links: latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin, latin-papal-church-avignon-to-lateran-v--the-beguines. Eras: era 5, era 6.
- Adam of Bremen, Gesta Hammaburgensis. Unlocks: would document English bishops in Norway and Sweden and the sees before 1104. Links: late-anglo-saxon-christianity--scandinavian-conversion-christianity, scandinavian-conversion-christianity--scandinavian-reformation-kingdoms. Eras: era 4.
- Adam of Eynsham, Magna Vita S. Hugonis (Dimock 1864). Unlocks: would document the Carthusian founding. Links: no link id. Eras: era 5.
- Agnellus, Liber Pontificalis Ecclesiae Ravennatis. Unlocks: would document the Arian Baptistery, Theoderic's churches and Gothic reconsecration. Links: byzantine-imperial-church-justinianic--gothic-and-vandal-homoian-christianity. Eras: era 2, era 3.
- Aldhelm's letter to Geraint of Dumnonia on the British Easter and tonsure. Unlocks: would document the letter Bede means. Links: anglo-saxon-christianity--british-welsh-christianity--2. Eras: era 3.
- Alexander IV's letters of 1255 condemning the Introductorius (D'Argentré I). Unlocks: would document the condemnation. Links: latin-papal-church-gregorian--joachimite-current. Eras: era 5, major links era 5.
- Alexander Mackay and CMS letters from Buganda (1877-1890), or Mackay by his sister (1890). Unlocks: would document Buganda from the CMS side. Links: victorian-church-of-england--east-african-christianity-uganda-martyrs. Eras: era 9 part 2.
- Alexandrian text naming Justin for the 'seeds of the Word' argument. Unlocks: would document the Justin link from a vendored source. Links: no link id. Eras: era 1.
- Alfred's prose preface to the Pastoral Care (Sweet, EETS 1871). Unlocks: would make the Gregory-to-Alfred link Documented. Links: roman-church-gregorian--late-anglo-saxon-christianity. Eras: era 3, era 4, major links era 3.
- Ambrose's Hexaemeron or Exposition of Luke, vendored edition. Unlocks: would show Ambrose's own use of Origen. Links: alexandria-catechetical--ambrosian-milan-standalone. Eras: era 1.
- Ambrose, Jerome or Gregory of Nyssa naming Methodius's Banquet on virginity. Unlocks: would document a Methodius reception link. Links: no link id. Eras: era 1.
- Ambrose, Letter 24 (Maurist 30), on his embassy to Maximus. Unlocks: would document Ambrose's objection to the execution of heretics. Links: ambrosian-milan-standalone--priscillianist-asceticism. Eras: era 2.
- AME General Conference minutes or Doctrines and Discipline from both sides of 1906. Unlocks: would show the same church before and after 1906. Links: the-black-church-in-america--the-black-church-in-the-twentieth-century. Eras: era 9 part 1.
- American Unitarian Association, First Annual Report (Boston, 1826). Unlocks: would document the founding of 25 May 1825. Links: no link id. Eras: era 9 part 2.
- Andrew Jackson Davis, The Principles of Nature (1847); Emma Hardinge Britten, Modern American Spiritualism (1870). Unlocks: would give Spiritualism's own record. Links: no link id. Eras: era 9 part 2.
- Anglo-Saxon Chronicle (D and E texts; Plummer-Earle 1892-99). Unlocks: would document Lindisfarne, the Danish invasions and s.a. 964. Links: anglo-saxon-christianity--late-anglo-saxon-christianity, early-benedictine-italian-monasticism--late-anglo-saxon-christianity. Eras: era 4.
- Anna Komnene, Alexiad XV (Reifferscheid 1884; Dawes 1928). Unlocks: would document the Bogomil name at Constantinople and Basil's trial. Links: bogomils--balkan-bogomil-continuation, byzantine-church-after-1054--balkan-bogomil-continuation. Eras: era 4, era 5, major links era 5.
- Annales regni Francorum entry for 750/751 on Boniface anointing Pippin (clean text). Unlocks: would document the anointing sentence. Links: anglo-saxon-christianity--carolingian-reform-christianity. Eras: era 4.
- Antiochus Strategos, The Capture of Jerusalem (614), vendored translation. Unlocks: would document the survivors writing down the losses. Links: no link id. Eras: era 3.
- Any papal document on Haiti before 1860. Unlocks: would document the Haitian papal record. Links: catholic-church-long-nineteenth-century--haitian-church-rupture-to-concordat. Eras: era 9 part 2.
- Arakel of Tabriz, History (Brosset 1874), on the 1604-05 deportation. Unlocks: would document the deportation and its numbers. Links: no link id. Eras: armenian-apostolic era 8, era 7.
- Archbishop Victor Sadkowski's encyclical of 26 May 1794 and the Holy Synod's orders of 1794-95. Unlocks: would document the 1794 step from the Orthodox side. Links: russian-church-nikon-to-holy-synod--ruthenian-uniate-18th-century. Eras: era 8.
- Ari Þorgilsson, Íslendingabók, public-domain edition or translation. Unlocks: would document the Althing decision of 1000. Links: no link id. Eras: era 4.
- Armenian National Constitution (1860/1863). Unlocks: would document the constitution's text. Links: no link id. Eras: era 9 part 2.
- Armenian patriarchate of Constantinople's eighteenth-century registers and encyclicals. Unlocks: would document the Constantinople patriarchate's own record. Links: no link id. Eras: armenian-apostolic era 8.
- Asser, Life of King Alfred (Stevenson 1904; Cook 1906). Unlocks: would document Alfred's life from Asser. Links: no link id. Eras: era 4.
- Augustine, De haeresibus 86, clean edition. Unlocks: would replace the PL 42 OCR so the census quote can be checked. Links: no link id. Eras: era 1.
- Augustinian Hermits' Saxon congregation in the 1520s. Unlocks: would document what happened to its houses in Lutheran lands. Links: no link id. Eras: era 7.
- Bar Hebraeus, Ecclesiastical Chronicle vol. II (Abbeloos and Lamy 1874). Unlocks: would document the patriarchs of Antioch after 1083. Note: Vols I and III are vendored; vol. II is not. Links: syriac-orthodox-under-islam--syriac-renaissance. Eras: era 5.
- Bardaisan's dialogues against Marcionites, or Theodoret, Haer. fab. I.22. Unlocks: would document Bardaisan against Marcion. Links: bardaisanite-current--marcion-marcionism. Eras: era 1.
- Barton W. Stone, The Biography of Eld. Barton Warren Stone (1847), Cane Ridge. Unlocks: would show the Stone wing from its own leader's pen. Links: the-second-great-awakening-and-camp-meeting-worl--the-stone-campbell-restoration-movement. Eras: era 9 part 1.
- Bedford church book (Bunyan Meeting), public-domain edition. Unlocks: would document the congregation's record of persecution. Links: restoration-georgian-church-of-england--the-baptists. Eras: era 8.
- Benedict XIII's briefs of 1725 on Steenoven's election and Barchman Wuytiers. Unlocks: would show the rupture from Rome in its own words. Links: catholic-church-ancien-regime--church-of-utrecht. Eras: era 8.
- Benedict XIV's 1742 act confirming Abraham Ardzivian as Catholic patriarch of Cilicia. Unlocks: would rest the founding act on its own text. Links: armenian-apostolic-church-era-8--armenian-christianity-era-8, armenian-christianity-era-8--catholic-church-ancien-regime. Eras: armenian-apostolic era 8, era 8.
- Benson's 1886 letter of instruction to the Assyrian Mission. Unlocks: would document the 1886 instruction in Benson's words. Links: church-of-the-east-chaldean-consolidation--victorian-church-of-england. Eras: era 9 part 2.
- Bernard of Clairvaux, Apologia ad Guillelmum; Peter the Venerable, Letter 28. Unlocks: would document the Cistercian break with Cluny. Links: no link id. Eras: era 4, era 5.
- Bernard of Clairvaux, De laude novae militiae (PL 182). Unlocks: would document Bernard's defense of the Templars and the 'novum militiae genus'. Links: cistercian-monasticism--military-religious-orders-templars-hospitallers. Eras: era 5.
- Bernard Petitjean's letter of March 1865 reporting the Oura meeting. Unlocks: would document the Oura meeting. Links: catholic-church-long-nineteenth-century--japanese-christianity-hidden-emergence-meiji. Eras: era 9 part 2.
- Bernard Petitjean's letters of March 1865 on the Urakami Christians. Unlocks: would document the Kirishitan to hidden-Christian link. Links: no link id. Eras: era 7.
- Bernard's or Ulrich's customary of Cluny (Ordo Cluniacensis). Unlocks: would show Cluny living by the Rule. Links: early-benedictine-italian-monasticism--cluniac-reform-monasticism. Eras: era 3, major links era 3.
- Bernardo da Gallo's and Lorenzo da Lucca's relations on Dona Beatriz (1706-10). Unlocks: would document the Antonian movement from its only contemporary record. Links: kongo-christianity-afonso-to-1650--the-antonian-movement-in-kongo. Eras: era 7, era 8.
- Bishops of India's 1504 letter to the patriarch, full English translation and Syriac. Unlocks: would document the 1504 letter. Links: church-of-the-east-timur-to-hakkari--st-thomas-christians-1300-1517. Eras: era 6, era 7.
- Bishops Seabury and Provoost's refusal to ordain James Freeman (1787), and the congregation's ordination. Unlocks: would show the departure from both sides. Links: restoration-georgian-church-of-england--early-american-unitarians-universalists. Eras: era 8.
- Bonaventure, De reductione artium ad theologiam (Quaracchi 1891). Unlocks: would document Bonaventure's naming of Hugh and Richard of St Victor. Links: canons-regular-victorine-school--the-franciscan-movement. Eras: era 5.
- Bonaventure, Itinerarium mentis in Deum. Unlocks: would document Bonaventure's Victorine debt. Links: canons-regular-victorine-school--the-franciscan-movement. Eras: era 5.
- Boniface's letter to Pope Zacharias of 742 (Tangl 1916) and the Clausula de unctione Pippini (MGH SRM 1). Unlocks: would document the Pippin anointing from the sources. Note: Kylie 1911 (English Boniface letters) is vendored; check whether it carries the 742 letter. Links: merovingian-gallic-christianity--carolingian-reform-christianity. Eras: era 3.
- Book of Letters (Girk' T'łt'oc'): Dvin 554, Dvin 506, Abraham-Kiwrion correspondence, Elias's letters. Unlocks: would document the Armenian councils and letters in a readable translation. Links: armenian-christianity-after-avarayr--armenian-christianity-before-the-bagratids, armenian-christianity-after-avarayr--byzantine-imperial-church-justinianic, armenian-christianity-after-avarayr--church-of-caucasian-albania, armenian-christianity-after-avarayr--georgian-christianity, armenian-christianity-before-the-bagratids--church-of-caucasian-albania, armenian-christianity-before-the-bagratids--georgian-christianity. Eras: era 3.
- Boverius, Annales Capuccinorum (1632). Unlocks: would document the Capuchins' break from the Observants. Links: no link id. Eras: era 6.
- Brut y Tywysogion, public-domain edition. Unlocks: would document the Welsh sees after 954. Links: british-welsh-christianity--medieval-welsh-christianity. Eras: era 4.
- Bull 'Benedictus sit Deus' (7 August 1445), clean edition with its dating clause. Unlocks: would document the bull's date and terms. Links: latin-papal-church-avignon-to-lateran-v--maronite-christianity-era-6. Eras: era 6.
- Bull Id nostri cordis (27 April 1487), critical edition. Unlocks: would check Morland's copy. Links: latin-papal-church-avignon-to-lateran-v--waldensians-in-the-alps. Eras: era 6.
- Březová's 1421 chapter on the Adamites, in a public-domain English; Kaminsky and Fudge (in copyright). Unlocks: would let a reader check the Adamite account. Links: taborite-radicalism--inquisition-record-sects-adamites-and-kin, the-hussite-and-bohemian-brethren-movement--taborite-radicalism. Eras: era 6.
- C. I. Scofield, The Scofield Reference Bible (1909). Unlocks: would document the dispensational notes. Links: plymouth-brethren-and-dispensational-formation--dispensational-prophecy-culture. Eras: era 9 part 1.
- Cambrai and Paris copies of Julian of Norwich's Long Text and their provenance. Unlocks: would document Julian's text and its nuns' provenance. Links: the-english-mystics-and-devout--recusant-english-catholicism. Eras: era 6.
- Canons of the Aachen councils of 816-817 and of the councils of 813 (MGH Concilia aevi Karolini I). Unlocks: would document the empire-wide Benedictine and Pastoral Rule legislation. Links: early-benedictine-italian-monasticism--carolingian-reform-christianity, roman-church-gregorian--carolingian-reform-christianity. Eras: era 3.
- Cassian, Conference XIII, in a vendored edition. Unlocks: would give the Marseilles position in its own words. Links: gallic-monastic-ascetic-christianity--latin-pastoral-congregational-christianity. Eras: era 2.
- Cathedral chapter's acts of 1723-1725 and Varlet's Apologie (1727). Unlocks: would document the Utrecht chapter's acts from its own side. Links: catholic-church-ancien-regime--church-of-utrecht. Eras: era 8.
- Catherine Booth, Female Ministry; or, Woman's Right to Preach the Gospel (1859). Unlocks: would document the Booths' Holiness argument. Links: nineteenth-century-methodism--the-salvation-army, the-holiness-movement--the-salvation-army. Eras: era 9 part 1.
- Cerularius's synodal edict of July 1054, and the Byzantine synodal edict against the legates (Will 1861). Unlocks: would give the see's own side of 1054 and the 1965 sentence. Links: byzantine-church-after-1054--latin-papal-church-gregorian, byzantine-imperial-church-macedonian--byzantine-church-after-1054. Eras: era 4, era 5.
- Chantries Act 1547 (1 Edw. VI c. 14), public-domain Statutes of the Realm. Unlocks: would document the guild dissolution from the act. Links: the-english-reformation-and-elizabethan-settleme--late-medieval-lay-parish-piety. Eras: era 6.
- Charles Dallet, Histoire de l'Église de Corée (1874). Unlocks: would document the Korean church's origins and persecutions. Links: no link id. Eras: era 9 part 2.
- Charter of Niquinta (Saint-Félix council, 1167). Unlocks: would document the Balkan bishop among the Languedoc Cathars. Links: balkan-bogomil-continuation--cathars-albigensians. Eras: era 5.
- Christopher Rush, A Short Account of the Rise and Progress of the African M. E. Church (1843). Unlocks: would document the AME Zion separation of 1821. Links: nineteenth-century-methodism--the-black-church-in-america. Eras: era 9 part 1.
- Church of England record of the Methodist separation (1790s charge or visitation return). Unlocks: would show the rupture from both sides. Links: restoration-georgian-church-of-england--the-methodist-revival--2. Eras: era 8.
- Church of England response to the 1811 ordinations. Unlocks: would show the rupture from both sides. Links: restoration-georgian-church-of-england--the-welsh-revival-tradition. Eras: era 8.
- Citable source for the Iglesia Filipina Independiente's 1961 concordat with the Episcopal Church. Unlocks: would document the 1961 concordat. Links: no link id. Eras: era 9 part 2.
- Clean Annales Cambriae and clean Chronicle of 754. Unlocks: would replace rough OCR for two annals. Note: A rough Rolls Series text is vendored. Links: british-welsh-christianity--medieval-welsh-christianity, nicene-visigothic-iberia--mozarabic-christianity. Eras: era 3, era 4.
- Clean edition of Nikephoros Kallistos's Enarratio. Unlocks: would replace the garbled PG 147 OCR. Links: byzantine-imperial-church-heraclian-iconoclast--byzantine-imperial-church-macedonian. Eras: era 4.
- Clean edition of the 1737 London Faithful Narrative with the Watts-Guyse preface. Unlocks: would replace the garbled preface scan. Links: the-evangelical-awakening-in-new-england--english-old-dissent. Eras: era 8.
- Clean edition of Victor of Tunnuna's Chronicle. Unlocks: would replace the rough MGH and Mommsen OCR. Note: A rough MGH text is vendored; the clean edition is not. Links: latin-africa-under-byzantium--byzantine-imperial-church-justinianic. Eras: era 3.
- Clean edition or translation of Sebeos (Thomson 1999 or Patkanian 1879). Unlocks: would replace Macler's OCR. Note: Macler's 1904 OCR is vendored; a clean text is not. Links: no link id. Eras: era 3.
- Clean Greek text of the Florentine Definition with its signatures. Unlocks: would give the Florence step a clean primary. Links: byzantine-church-palaiologan--latin-papal-church-avignon-to-lateran-v. Eras: era 6.
- Clean Latin text of the Collatio cum Maximino. Unlocks: would fix the Maximinus answer the PL 42 OCR mangles. Links: no link id. Eras: era 2.
- Clean text of Eusebius HE VII.28.1 (Hymenaeus and Theotecnus at the Antioch synods). Unlocks: would document a Palestinian contact link. Links: no link id. Eras: era 1.
- Clean text of the Gesta Collationis Carthaginiensis (411). Unlocks: would confirm the 279 and 286 bishop counts. Links: no link id. Eras: era 2.
- Clement XI's bull of 1708 suppressing Port-Royal des Champs and the 1709 dispersal orders. Unlocks: would document the suppression text. Links: catholic-church-ancien-regime--port-royal-jansenism. Eras: era 8.
- Cluny's foundation charter of 909/910 (Bruel 1876). Unlocks: would show the house placed under the Rule of Saint Benedict. Links: carolingian-reform-christianity--cluniac-reform-monasticism, cluniac-reform-monasticism--latin-papal-church-gregorian, early-benedictine-italian-monasticism--cluniac-reform-monasticism. Eras: era 3, era 4, major links era 4.
- Codex Justinianus 1.5.20 and John of Ephesus on the Montanists at Pepuza. Unlocks: would document Justinian's campaign against the Montanists. Links: byzantine-imperial-church-justinianic--montanism-the-new-prophecy. Eras: era 1.
- Coleridge's Xavier quotes checked against Monumenta Xaveriana I. Unlocks: would check the quotes against the Spanish. Links: no link id. Eras: era 7.
- Cologne trial acts (Théry, Archives d'histoire doctrinale 1926) and the bull In agro dominico. Unlocks: would document the Cologne stage directly. Links: latin-papal-church-avignon-to-lateran-v--rhineland-mysticism-and-the-friends-of-god. Eras: era 6.
- Columbanus, Letters II and V (MGH Epp. III, Gundlach). Unlocks: would document the Easter dispute in Gaul. Links: insular-irish-monastic-christianity--roman-church-gregorian. Eras: era 3.
- Committee of Ministers decision of 4 July 1894 on the Stundist sect, with the Synod's request. Unlocks: would document the Orthodox state act against the Stundists. Links: russian-church-synodal-century--russian-evangelicals-stundists, russian-church-synodal-century--russian-evangelicals-stundists--2. Eras: era 9 part 1.
- Concordat between the Holy See and Haiti (28 March 1860); Haitian state acts on clergy, 1804-1860. Unlocks: would document the Haitian church's status. Links: catholic-church-long-nineteenth-century--haitian-church-rupture-to-concordat. Eras: era 9 part 2.
- Conrad Grebel's letters (1524-1525). Unlocks: would give the Anabaptists' own record of the break with Zwingli. Links: no link id. Eras: era 7.
- Constitution and first annual report of the American Unitarian Association (1825-26). Unlocks: would document the Unitarian thread. Links: early-american-unitarians-universalists--american-unitarianism-universalism-consolidations. Eras: era 8.
- Contemporary record of Avedik's fall (French embassy dispatches or the patriarchate's own account). Unlocks: would document Avedik's fall from a contemporary record. Links: armenian-christianity-era-8--armenian-apostolic-church-era-8. Eras: armenian-apostolic era 8.
- Contemporary reports on the massacres of 1894-96 (British parliamentary papers, 1895-96). Unlocks: would document the 1894-96 massacres. Links: no link id. Eras: era 9 part 2.
- Continuation of Sempad's chronicle (RHC Doc. arm. I) on the see at Sis after 1293. Unlocks: would show the step from Hromkla to Sis. Links: armenian-cilicia--armenian-cilicia-after-the-kingdom. Eras: era 5.
- Conventicle Act of 1664 (16 Car. II c. 4) and Act of 1670, Statutes of the Realm vol. V. Unlocks: would replace Whitley's summary with the statute's words. Links: restoration-georgian-church-of-england--the-baptists. Eras: era 8.
- Cornelius's letter to Fabius (Eusebius HE VI.43.5-20). Unlocks: would document the Roman rupture over Novatian. Links: no link id. Eras: era 1.
- Corpus Schwenckfeldianorum vols II-III (1524-1530). Unlocks: would give Schwenckfeld's account of the 1525 visit. Links: no link id. Eras: era 7.
- Cosmas the Priest, Sermon against the Heretics (Popruzhenko 1907). Unlocks: would document Cosmas's attack on the Bogomils. Links: bogomils--balkan-bogomil-continuation. Eras: era 4, major links era 4.
- Cum de quibusdam mulieribus (Clementines III.11.1), Vienne decree. Unlocks: would show the council moving against the beguine status. Links: latin-papal-church-avignon-to-lateran-v--the-beguines. Eras: era 5.
- Cummian's De controversia paschali (c. 632). Unlocks: would give the Irish side of the Easter dispute. Links: anglo-saxon-christianity--insular-irish-monastic-christianity. Eras: era 4.
- Cyril IV's mission to Tewodros, 1856-57. Unlocks: would document the mission. Links: coptic-revival-under-cyril-iv--ethiopian-christianity-tewodros-to-menelik. Eras: era 9 part 2.
- Cyril IV's own reforms, in an Arabic or translated edition. Unlocks: would document Cyril IV's reforms from his own side. Links: no link id. Eras: era 9 part 2.
- Cyril IV's patriarchal school (1855), majlis milli (1874) and al-Watan (1877-) records. Unlocks: would document Cyril IV's reforms. Links: coptic-revival-under-cyril-iv--the-coptic-monastic-and-sunday-school-revival. Eras: era 9 part 2.
- Cyril of Scythopolis, Life of Euthymius, readable edition (ch. 6-8, Pharan). Unlocks: would show a named monk moving from Pharan to the Judean desert foundations. Note: The Cotelier 1681 text is vendored but too corrupt to quote. Links: palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza. Eras: era 2.
- Cyril of Scythopolis, Life of Sabas. Unlocks: would document Sabas's embassies and the Origenist split. Links: byzantine-imperial-church-justinianic--chalcedonian-monasticism-judean-desert-and-gaza. Eras: era 3.
- Danish 1537 Ordinatio ecclesiastica in readable text, naming the old-see superintendents. Unlocks: would document the superintendents in the old sees. Links: scandinavian-conversion-christianity--scandinavian-reformation-kingdoms. Eras: era 4.
- Danish Church Ordinance of 1537/1539 drawn up with Bugenhagen. Unlocks: would document the Danish-Norwegian side of the Scandinavian link. Links: no link id. Eras: era 7.
- Dated Stundist record of the break; Stundist petitions of 1894-1905 (Bonch-Bruevich, Materialy). Unlocks: would give the Stundist break in its own words. Links: russian-church-synodal-century--russian-evangelicals-stundists. Eras: era 9 part 1.
- Dated witness to the 1341 synod (Kantakouzenos's History or Gregoras). Unlocks: would carry the year on the palamite link. Links: hesychasm-and-the-palamite-synthesis--byzantine-church-palaiologan. Eras: era 6.
- Diplomatarium Islandicum vols 10-11 (Jon Arason's letters) and an account of his execution (1550). Unlocks: would document Arason's execution. Links: no link id. Eras: era 7.
- Disputation with Pyrrhus, Latin text with a clean column. Unlocks: would quote its African setting. Links: no link id. Eras: era 3.
- Doddridge's Correspondence and Diary (Humphreys 1829-31). Unlocks: would give Doddridge's side of his dealings with Wesley and Whitefield. Links: english-old-dissent--the-methodist-revival. Eras: era 8.
- Dongola throne-hall inscription of 1317 (Arabic), edition. Unlocks: would document the mosque conversion. Links: no link id. Eras: era 6.
- Dorotheus's Instructions in a clean English or Greek text. Unlocks: would document the Dorotheus Instructions directly. Links: desert-monasticism--chalcedonian-monasticism-judean-desert-and-gaza. Eras: era 3.
- Duwayhi's history of the Maronite patriarchs in a clean scan. Unlocks: would document the patriarchal line across 1300. Links: maronite-christianity--maronite-christianity-era-6. Eras: era 6.
- Döllinger's letter to Archbishop Scherr (28 March 1871) and the Munich excommunication decree (17 April 1871). Unlocks: would document the 1871 rupture. Links: catholic-church-long-nineteenth-century--old-catholic-churches-union-of-utrecht. Eras: era 9 part 2.
- Early record of Further Reformation piety among Dutch settlers (Frelinghuysen's sermons). Unlocks: would document Dutch piety in the Americas. Links: no link id. Eras: era 7.
- Edition of Victorinus's Commentary on the Apocalypse with Jerome's recension. Unlocks: would document the reissue directly. Links: no link id. Eras: era 1.
- Edmund Calamy, An Account of the Ministers ... Ejected or Silenced (1702/1713). Unlocks: would document the ejected ministers. Links: english-old-dissent--restoration-georgian-church-of-england. Eras: era 8.
- Edwards, An Humble Attempt (1747) and Sutcliff's 1789 reprint. Unlocks: would document the Baptist prayer concert. Links: the-evangelical-awakening-in-new-england--the-baptists. Eras: era 8.
- Emerson, Divinity School Address (Boston, 1838); Andrews Norton, A Discourse on the Latest Form of Infidelity. Unlocks: would document the Transcendentalist break. Links: no link id. Eras: era 9 part 2.
- Ephraim's Hymns against Heresies, full vendored translation. Unlocks: would quote Ephraim's complaint about Bardaisan directly. Links: bardaisanite-current--syriac-edessa-nisibis. Eras: era 1.
- Epiphanius's Life of Sergius (vendored edition). Unlocks: would document the hesychast side of Sergius's circle. Links: hesychasm-and-the-palamite-synthesis--muscovite-monastic-christianity. Eras: era 6.
- Epiphanius, Panarion 29-30 (Nazoraeans and Ebionites). Unlocks: would document the Ebionite sources. Links: no link id. Eras: era 1.
- Epiphanius, Panarion 73.12, or Hilary, De synodis 81 and 86 (Ancyra appeal against Paul). Unlocks: would quote the Ancyra appeal from a readable text. Note: PG 42 Greek-Latin OCR is vendored; the readable text is not. Links: no link id. Eras: era 1.
- Erast, Istoricheskoe opisanie Kozel'skoi Optinoi pustyni (1902). Unlocks: would document the founding of the Optina skete in 1821. Links: russian-church-synodal-century--the-optina-elders-and-russian-ascetic-renewal. Eras: era 9 part 2.
- Esteves Pereira, Chronica de Susenyos (Lisbon 1892-1900). Unlocks: would give the Ethiopian court's account of the conversion and the 1632 restoration. Links: no link id. Eras: era 7.
- Eulogius, Memoriale sanctorum; Paulus Alvarus, Indiculus luminosus. Unlocks: would support the Córdoba martyr sentences. Links: no link id. Eras: era 4.
- Euthymius Zigabenus, Panoplia dogmatica (titles 23 and 27) and Gieseler's Narratio de Bogomilis. Unlocks: would document the medieval tie between Bogomils and Paulicians. Links: bogomils--balkan-bogomil-continuation, byzantine-church-after-1054--balkan-bogomil-continuation, paulicians--bogomils. Eras: era 4, era 5.
- Excerpts of Gerard's Introductorius outside the Protocol of Anagni. Unlocks: would quote Gerard in his own text. Links: joachimite-current--the-franciscan-movement. Eras: era 5.
- Exordium Parvum, Exordium Cistercii and Carta Caritatis (Guignard 1878). Unlocks: would document the founders' aim to keep the Rule of Saint Benedict. Links: early-benedictine-italian-monasticism--cistercian-monasticism. Eras: era 3, era 5, major links era 3.
- Father Bernard Meynier, Le Port-Royal et Genève (1656). Unlocks: would show the Jesuit side in its own words. Links: the-society-of-jesus--port-royal-jansenism. Eras: era 8.
- Faustus of Byzantium and Agathangelos, Langlois tome I (1867). Unlocks: would document the consecration of Gregory's successors at Caesarea. Links: cappadocian-nicene-pastoral-monastic-tradition--armenian-christianity-conversion-era. Eras: era 2.
- First edition of Thomas Ellwood's History of the Life (1714). Unlocks: would check the Spiritual Guide report. Note: Crump's 1900 edition is vendored; the 1714 first edition is not. Links: quietist-controversy-molinos-guyon--the-quakers-religious-society-of-friends. Eras: era 8.
- First Observant hermitage at Brugliano (Paoluccio Trinci, 1368). Unlocks: would document the 1368 grant. Links: franciscan-order-era-6--observant-reform-and-popular-preaching. Eras: era 5.
- Fliedner's Kaiserswerth annals; contemporary account of Nightingale's 1851 stay. Unlocks: would document Kaiserswerth. Links: no link id. Eras: era 9 part 1.
- Francis of Assisi, Testament. Unlocks: would document the papal confirmation of the Rule. Links: latin-papal-church-gregorian--the-franciscan-movement. Eras: era 5.
- Gadla Ewostatewos, the acts of the 1450 council of Debre Mitmaq, and modern study. Unlocks: would document the Ewostathian side of the Sabbath quarrel. Links: no link id. Eras: era 6.
- Gadla Lalibela (Perruchon 1892). Unlocks: would document the Zagwe king's Life and the Jerusalem churches. Links: coptic-christianity-fatimid-to-mamluk--zagwe-and-early-solomonic-ethiopian-christianity. Eras: era 5.
- Genesios or Theophanes Continuatus on the fall of Tephrike (878). Unlocks: would date the fall of Tephrike. Links: byzantine-imperial-church-macedonian--paulicians. Eras: era 4.
- Geneva Bible (1560) prefatory matter or Livre des Anglois of the Geneva English congregation. Unlocks: would document the Geneva-to-Puritan line. Links: no link id. Eras: era 7.
- Gennadios Scholarios's own account of his election. Unlocks: would document the 1448-1450s election from his side. Links: byzantine-church-palaiologan--orthodoxy-under-the-ottomans-parish-millet-and-n. Eras: era 6.
- George Morel's memoir and letter to Oecolampadius (1530). Unlocks: would document the Alpine Waldensians' outward conformity. Links: no link id. Eras: era 6.
- George the Hagiorite, Life of John and Euthymius; Actes d'Iviron I (Lefort 1985). Unlocks: would document Iviron's founding from its own side. Links: athonite-and-comnenian-byzantine-monasticism--georgian-revival-tao-klarjeti, athonite-and-comnenian-byzantine-monasticism--the-georgian-golden-age. Eras: era 4, era 5, major links era 5.
- Georgian or Greek text of c. 600 recording the Georgian church's acceptance of Chalcedon. Unlocks: would document the Georgian Chalcedon acceptance. Links: byzantine-imperial-church-justinianic--georgian-christianity. Eras: era 3.
- Giorgi Merchule, Life of Grigol of Khandzta. Unlocks: would show the revival from inside the Georgian church. Links: georgian-christianity--georgian-revival-tao-klarjeti, georgian-revival-tao-klarjeti--the-georgian-golden-age. Eras: era 3, era 4, era 5.
- Gorham judgment (1850), Essays and Reviews (1860), Lambeth Conference encyclical (1867). Unlocks: would give the Victorian Church of England's own texts. Links: no link id. Eras: era 9 part 1.
- Gottfried Arnold, Unparteiische Kirchen- und Ketzer-Historie (1699-1700). Unlocks: would document the radical Pietists' manifesto. Links: german-pietism-spener-francke-halle--radical-pietism-and-the-brethren-dunkers-ephrata. Eras: era 8.
- Greek Catholic or Roman account of the Polotsk act of 1839. Unlocks: would hear the other side of the Polotsk act. Links: russian-church-synodal-century--ruthenian-greek-catholic-polotsk-to-galicia. Eras: era 9 part 2.
- Greek royal decree of 1833 declaring the Church of Greece autocephalous. Unlocks: would document the Greek autocephaly. Links: no link id. Eras: era 9 part 2.
- Gregory of Nazianzus, Letter 115, clean Greek text. Unlocks: would quote 'and the same from holy Basil' correctly. Note: PG 37 Greek-Latin is vendored; check its Letter 115 text. Links: no link id. Eras: era 1.
- Gregory of Nyssa's own letters on his deposition and return (Epp. 6, 18, 22). Unlocks: would give Gregory's side of the deposition. Links: homoian-arian-christianity--cappadocian-nicene-pastoral-monastic-tradition. Eras: era 2.
- Gregory Palamas, Triads in Defence of the Holy Hesychasts (I.2.12). Unlocks: would document Palamas's appeal to Athonite teachers. Note: PG 150 Greek-Latin OCR is vendored; a clean text is not. Links: athonite-and-comnenian-byzantine-monasticism--hesychasm-and-the-palamite-synthesis. Eras: era 5.
- Gregory the Great's Register I-VII (Ewald-Hartmann Latin), with Register tomus II. Unlocks: would check the numbering of the Donatist letters and the count of letters. Note: Books VIII-XIV are vendored; I-VII are not. Links: no link id. Eras: era 2, era 3.
- Gregory the Great's Register XIII.47-50 on the Spanish depositions. Unlocks: would test the 'doing wrong' wording from Gregory's own words. Links: no link id. Eras: era 3.
- Grigoris Balakian, Armenian Golgotha (1922). Unlocks: would give an eyewitness of 1915 from inside the church. Links: armenian-christianity-zartonk--the-armenian-church-after-the-genocide-medz-yegh. Eras: era 9 part 2.
- Guaman Poma, Nueva corónica y buen gobierno (1615), public-domain transcription. Unlocks: would document the Andean Christian witness. Links: no link id. Eras: era 7.
- H. B. Kendall, Primitive Methodist Church (1905-06), or Hugh Bourne's writings. Unlocks: would document Mow Cop and the Primitive Methodist connexion. Links: no link id. Eras: era 9 part 1.
- Habib Girgis's writings and General Sunday School Committee records (c. 1918). Unlocks: would document the Arabic Sunday-school movement. Links: coptic-revival-under-cyril-iv--the-coptic-monastic-and-sunday-school-revival. Eras: era 9 part 2.
- Harford (ed.), The Keswick Convention (1907). Unlocks: would document Keswick's British wing. Links: no link id. Eras: era 9 part 1.
- Hendrik de Cock's Verdediging (1833); Acte van Afscheiding (Ulrum 1834). Unlocks: would document the Dutch secession. Links: no link id. Eras: era 9 part 1.
- Herman of Alaska's letters and Semyon Yanovsky's letter of 1865. Unlocks: would document the Alaska mission from primary letters. Links: no link id. Eras: era 9 part 2.
- Hilary, Contra Auxentium, in English or a located passage in PL 10. Unlocks: would document Hilary's attack on Auxentius. Links: no link id. Eras: era 2.
- History of the Patriarchs of the Coptic Church, later continuations (14th-19th centuries). Unlocks: would document the line of patriarchs. Links: coptic-christianity-fatimid-to-mamluk--coptic-revival-under-cyril-iv. Eras: era 9 part 2.
- History of the Patriarchs of the Egyptian Church, vols 2-4, and Life of Cyril II. Unlocks: would document the patriarchs' dealings with Ethiopia and the Zagwe-era metropolitans. Links: coptic-christianity-fatimid-to-mamluk--zagwe-and-early-solomonic-ethiopian-christianity, coptic-christianity-under-early-islam--post-aksumite-ethiopian-christianity, post-aksumite-ethiopian-christianity--zagwe-and-early-solomonic-ethiopian-christianity. Eras: era 4, era 5.
- History of the Russian diocese in America to 1970 (seat moves 1872 and 1905; Metropolia). Unlocks: would document the diocese's history. Links: alaskan-mission-herman-veniaminov--american-orthodoxy-autocephaly-and-the-convert-wave. Eras: era 9 part 2.
- HKBP church order of 1881; Rhenish Mission reports from the Batak field. Unlocks: would document the church's own order and the Batak mission. Links: indonesian-christianity--indonesian-christianity-the-independent-century. Eras: era 9 part 1.
- Hochmann von Hochenau's Confession of Faith (1702), clean edition. Unlocks: would let Hochmann's Halle awakening rest on his own words. Links: german-pietism-spener-francke-halle--radical-pietism-and-the-brethren-dunkers-ephrata. Eras: era 8.
- Homoian record of the Council of Aquileia (Scholia Arriana, Palladius). Unlocks: would give the condemned party's side of the 381 links. Links: no link id. Eras: era 2.
- Honorius III's bulls of 1216-1217 confirming the Order of Preachers. Unlocks: would document the papal approval of the Dominicans. Links: no link id. Eras: era 5.
- Horatio W. Dresser, ed., The Quimby Manuscripts (1921). Unlocks: would document New Thought's descent from Quimby. Links: no link id. Eras: era 9 part 2.
- Hospitallers' Rule of Raymond du Puy (Delaville Le Roulx 1894). Unlocks: would document the hospital's rule. Links: no link id. Eras: era 5.
- Huarochirí manuscript, public-domain edition, or Francisco de Ávila's account. Unlocks: would document the manuscript's commissioning. Links: no link id. Eras: era 7.
- Humbert of Romans and John of Parma's joint letter of 1255. Unlocks: would document the rivalry between the two orders. Links: the-dominican-order--the-franciscan-movement. Eras: era 5.
- Hymns Ancient and Modern (1861); J. M. Neale, Hymns of the Eastern Church (1862). Unlocks: would document the Oxford hymn translations. Links: no link id. Eras: era 9 part 1.
- Imperial firman of 1870 creating the Bulgarian Exarchate. Unlocks: would document the Exarchate. Links: no link id. Eras: era 9 part 2.
- Innocent III's bull to the Maronite patriarch Jeremiah (1215), Anaissi 1911. Unlocks: would document the union terms. Links: latin-papal-church-gregorian--maronite-christianity. Eras: era 5, major links era 5.
- Innocent III's letters of 1201 to the Humiliati (Tiraboschi 1767). Unlocks: would document the 1201 letters. Links: latin-papal-church-gregorian--the-humiliati--2. Eras: era 5.
- Innocent III's letters of 1208-1209 calling the crusade, or Peter of Vaux-de-Cernay's Historia Albigensis. Unlocks: would document 1209 from a primary side. Links: latin-papal-church-gregorian--cathars-albigensians. Eras: era 5.
- Innocent III's letters on Thomas Morosini as Latin patriarch (Register VII-VIII); Villehardouin. Unlocks: would give the crusaders' side of the Latin patriarchate. Links: latin-papal-church-gregorian--byzantine-church-after-1054--2. Eras: era 5.
- Interrogatio Iohannis with the Carcassonne colophon. Unlocks: would document the Interrogatio in a vendored edition. Links: balkan-bogomil-continuation--cathars-albigensians. Eras: era 5.
- Ioann Veniaminov's writings and reports: Notes on the Islands of the Unalaska District (1840), Aleut catechism, Synod act creating the diocese of Kamchatka. Unlocks: would document Veniaminov and the diocese from primary texts. Links: russian-church-synodal-century--alaskan-mission-herman-veniaminov. Eras: era 9 part 2.
- Isaac Backus, A History of New-England (1777-96). Unlocks: would document the Separates who became Baptists. Links: no link id. Eras: era 8.
- Ishoyahb III's letters (ed. Duval, CSCO). Unlocks: would document the catholicate across the conquest in his own words. Links: the-church-of-the-east-under-persia--the-church-of-the-east-on-the-silk-road. Eras: era 3.
- J. F. Schön and Samuel Crowther, Journals of the Niger Expedition of 1841 (1842). Unlocks: would document the 1841 Niger expedition. Links: the-missionary-movement-s-native-churches-seramp--african-initiated-churches-harrist-aladura-zioni. Eras: era 9 part 1.
- J. L. Krapf, Travels, Researches and Missionary Labours (1860). Unlocks: would document the East African coast mission from 1844. Links: no link id. Eras: era 9 part 2.
- J. N. Darby, Collected Writings (ed. Kelly), prophetic volumes; W. B. Neatby, History of the Plymouth Brethren (1901). Unlocks: would document the Darby line. Links: plymouth-brethren-and-dispensational-formation--dispensational-prophecy-culture, plymouth-brethren-and-dispensational-formation--the-sunday-school-and-bible-institute-movement. Eras: era 9 part 1.
- J. P. Thoonen, Black Martyrs (1941), or the 1920 beatification acts. Unlocks: would document the Catholic martyrs. Links: catholic-church-long-nineteenth-century--east-african-christianity-uganda-martyrs. Eras: era 9 part 2.
- James Sibree, Madagascar and its People (1870). Unlocks: would document the church after 1869. Links: no link id. Eras: era 9 part 2.
- Jelling stone inscription, public-domain reading. Unlocks: would document Harald Bluetooth's 'made the Danes Christian'. Links: no link id. Eras: era 4.
- Jerome on consulting the Hexapla at Caesarea (Commentary on Titus 3.9; Psalms commentary), and the Hexapla's survival there. Unlocks: would document the Hexapla step of the Palestinian contact. Links: palestinian-church-pre-constantinian--hieronymian-ascetic-literary. Eras: era 1.
- Jerome's Chronicle (Arnobius and his bishop). Unlocks: would document the Arnobius story if it is cited. Links: no link id. Eras: era 1.
- Jerome's Commentary on Ezekiel, preface to Book I ('the scorpion lies buried'). Unlocks: would document Jerome's last word on Rufinus. Links: no link id. Eras: era 2.
- Jerome's prologue to Anatolius on Victorinus's Commentary on the Apocalypse. Unlocks: would document Jerome's revision of Victorinus. Links: no link id. Eras: era 1.
- Jesuit letter or relation from Malabar, 1653-54, on the revolt against Archbishop Garcia. Unlocks: would give the Jesuit side of the Malabar pressure. Links: no link id. Eras: era 7.
- Joe Church, Quest for the Highest (1981). Unlocks: would document the Gahini revival from the missionary side. Links: east-african-christianity-uganda-martyrs--the-east-african-revival-balokole. Eras: era 9 part 2.
- Joeli Bulu, The Autobiography of a Native Minister in the South Seas (1871). Unlocks: would document the Wesleyan line into the Pacific churches. Links: the-methodist-revival--the-missionary-movement-s-native-churches-seramp. Eras: era 9 part 1.
- John Catholicos (Hovhannes Draskhanakerttsi), History of Armenia (Saint-Martin 1841). Unlocks: would give the catholicate across the 880s and the Albanian event in one narrative. Links: armenian-christianity-before-the-bagratids--bagratid-armenian-christianity, armenian-christianity-before-the-bagratids--church-of-caucasian-albania. Eras: era 3.
- John Henry Newman, Apologia Pro Vita Sua (1864). Unlocks: would give the movement's own account of its start and its older high-church debts. Links: restoration-georgian-church-of-england--the-oxford-movement-and-anglo-catholic-revival, victorian-church-of-england--the-oxford-movement-and-anglo-catholic-revival. Eras: era 9 part 1.
- John Humphrey Noyes, Bible Communism (1848); History of American Socialisms (1870); Oneida First Annual Report (1849). Unlocks: would give the community's own record. Links: no link id. Eras: era 9 part 2.
- John of Beth Aphthonia's or Zacharias's Life of Severus. Unlocks: would document Severus's years and death in Egypt. Links: cyrilline-miaphysite-egyptian-christianity--syriac-orthodox-west-syriac-christianity. Eras: era 3.
- John of Capistrano's report and the Breslau trial records of 1453 (Eschenloer). Unlocks: would document the Observant persecution of Breslau's Jews. Links: no link id. Eras: era 6.
- John of Damascus, On the Divine Images (Allies 1898). Unlocks: would document the argument from John's side. Links: byzantine-imperial-church-heraclian-iconoclast--melkite-arabic-christianity. Eras: era 4.
- John R. Mott, The Evangelization of the World in This Generation (1900). Unlocks: would document the mission movement's own statement. Links: the-student-volunteer-movement-and-edinburgh-191--the-ecumenical-movement-and-the-wcc. Eras: era 9 part 1.
- John VIII's letter Industriae tuae (880) on the Slavonic liturgy. Unlocks: would support the papal approval of Slavonic books. Links: no link id. Eras: era 4.
- John Wesley, An Extract of the Life of Madame Guion (1776), with his preface. Unlocks: would document the 1776 step from Wesley's own text. Links: quietist-controversy-molinos-guyon--the-methodist-revival. Eras: era 8.
- John XXII's 1326 condemnation of Olivi's Apocalypse commentary (Bullarium Franciscanum). Unlocks: would show the papacy treating the Spirituals' reading. Note: Bullarium Franciscanum v5 is vendored and mentions Olivi often; check for the 1326 condemnation. Links: joachimite-current--franciscan-order-era-6. Eras: era 5.
- Jonas, Life of Columban, Book II (Council of Macon, Luxeuil). Unlocks: would show the Frankish church adopting the rule. Links: insular-irish-monastic-christianity--merovingian-gallic-christianity. Eras: era 3.
- Jordan of Saxony, Libellus de principiis ordinis praedicatorum. Unlocks: would document Dominic's preaching against Languedoc heretics. Links: the-dominican-order--cathars-albigensians. Eras: era 5.
- Joseph John Gurney's and John Wilbur's writings (Wilbur's Journal, 1859). Unlocks: would document the second Quaker division. Links: no link id. Eras: era 9 part 1.
- Joseph Smith, The Book of Mormon (1830) and the Doctrine and Covenants (1835). Unlocks: would document the founding texts. Links: no link id. Eras: era 9 part 2.
- Journal of the General Conference of the Methodist Episcopal Church, 1844. Unlocks: would document the 1844 split from the American side. Links: the-methodist-revival--nineteenth-century-methodism. Eras: era 9 part 1.
- Kabale convention revival testimonies (from 1935). Unlocks: would document the revival testimonies. Links: east-african-christianity-uganda-martyrs--the-east-african-revival-balokole. Eras: era 9 part 2.
- Kartlis Tskhovreba for the seventh and eighth centuries, readable translation. Unlocks: would document the Georgian annals in translation. Links: georgian-christianity--georgian-revival-tao-klarjeti, georgian-revival-tao-klarjeti--the-georgian-golden-age. Eras: era 3, era 4, era 5.
- Keble's 1836 edition of Hooker, vol. 1, with the editor's preface. Unlocks: would document the Tractarian reading of the older divines. Note: The vendored Keble printing is 1850 and omits the 1836 preface. Links: restoration-georgian-church-of-england--the-oxford-movement-and-anglo-catholic-revival. Eras: era 9 part 1.
- Kekelidze's 1912 Russian edition of the Georgian Jerusalem lectionary. Unlocks: would document the Georgian lectionary. Links: jerusalem-liturgical-pilgrimage-christianity--georgian-christianity. Eras: era 3.
- Kyiv Caves Paterikon and Primary Chronicle (s.a. 1051), vendored edition. Unlocks: would document Ilarion's cave and Anthony's settling from the Rus' side. Links: athonite-and-comnenian-byzantine-monasticism--kievan-rus-christianity-1054-1240, kievan-rus-christianity--kievan-rus-christianity-1054-1240. Eras: era 4, era 5, major links era 5.
- Lactantius's loss of his chair at Nicomedia (text or repo-cited secondary). Unlocks: would document the Lactantius claim. Links: no link id. Eras: era 1.
- Lea, A History of the Inquisition of the Middle Ages, vol. 1 (1888). Unlocks: would narrate the Albigensian crusade and the 1230s inquisition. Note: Vol. III is vendored; vol. I is not. Links: latin-papal-church-gregorian--cathars-albigensians. Eras: era 5.
- Lea, A History of the Inquisition, vol. II (1887), on the Free Spirit and the Adamites. Unlocks: would document the Free Spirit and Adamites. Links: latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin. Eras: era 6.
- Legible edition of the Passio Marculi. Unlocks: would confirm the parade through towns and the cliff at Nova Petra. Links: no link id. Eras: era 2.
- Leo of Ostia, Chronicle of Monte Cassino (MGH SS 7). Unlocks: would document the Saracen destruction of 883. Links: no link id. Eras: era 3.
- Leo X, Ite vos (29 May 1517), Bullarium Romanum vol. V. Unlocks: would document the division of the order. Links: no link id. Eras: era 6.
- Leo XIII, Quae mari sinico (1902). Unlocks: would document the Philippine reorganization. Links: catholic-church-long-nineteenth-century--philippine-catholicism-gomburza-to-aglipay. Eras: era 9 part 2.
- Leo XIII, Rerum Novarum (1891); brief Universalis Ecclesiae (1850). Unlocks: would document the English hierarchy's restoration. Links: no link id. Eras: era 9 part 2.
- Letter of the council of Carthage of 535 (Reparatus) on receiving Arian clergy. Unlocks: would document the African reception of Arian clergy. Links: latin-africa-under-byzantium--gothic-and-vandal-homoian-christianity. Eras: era 3.
- Liang Fa, Good Words to Admonish the Age (1832). Unlocks: would document the tract Hong read. Links: the-missionary-movement-s-native-churches-seramp--taiping-heavenly-kingdom. Eras: era 9 part 1.
- Life of Clement of Ohrid (Theophylact). Unlocks: would document the Ohrid and Preslav schools. Links: no link id. Eras: era 4.
- Life of Constantine and Life of Methodius (Old Church Slavonic), public-domain text. Unlocks: would document the emperor's sending of the brothers in 862. Links: byzantine-imperial-church-macedonian--cyrillo-methodian-slavic-christianity. Eras: era 4.
- Life of John of Damascus at the laura of Sabas (Greek Life). Unlocks: would place John of Damascus at Mar Saba. Links: chalcedonian-monasticism-judean-desert-and-gaza--melkite-arabic-christianity. Eras: era 4.
- Life of Stephen the Younger (PG 100 or public-domain text). Unlocks: would document the 765 martyrdom. Links: byzantine-imperial-church-heraclian-iconoclast--iconophile-byzantine-monasticism. Eras: era 4.
- Littmann, Deutsche Aksum-Expedition IV (1913), for Ezana's inscriptions. Unlocks: would document Ezana's own inscriptions. Links: no link id. Eras: era 2.
- Lucius III, Ad abolendam (Verona 1184), naming the Humiliati and Poor of Lyon. Unlocks: would document the Humiliati condemnation. Links: latin-papal-church-gregorian--the-humiliati, latin-papal-church-gregorian--the-waldensians. Eras: era 5, major links era 5.
- Luther's letters to Schwenckfeld (1526, 1543) in a vendored edition. Unlocks: would give Luther's side of the break. Links: no link id. Eras: era 7.
- Mamluk sources or modern study on the Kesrwan campaigns of 1305 (Lammens, Salibi). Unlocks: would document the 1305 campaigns. Links: no link id. Eras: era 6.
- Manichaean-era Theodosian Code 16.5 laws naming the Montanists (clean critical text). Unlocks: would document the Montanist laws from a clean text. Links: imperial-juridical-christianity--montanism-the-new-prophecy. Eras: era 1.
- Mansi 24, Michael VIII's letter to Gregory X and the Lyon II acts. Unlocks: would name the emperor and council in a primary. Links: byzantine-church-after-1054--latin-papal-church-gregorian--2. Eras: era 5.
- Margaret Oliphant, Life of Edward Irving (1862); Robert Baxter, Narrative of Facts (1833); Catholic Apostolic liturgy (1842-). Unlocks: would document the Irvingite and Catholic Apostolic line. Links: no link id. Eras: era 9 part 1.
- Marguerite Porete, The Mirror of Simple Souls, vendored edition. Unlocks: would set the condemned propositions beside her words. Links: the-beguines--free-spirit-heresy. Eras: era 5.
- Martin V's crusade bull against the Hussites (1420). Unlocks: would document the papal crusade. Links: no link id. Eras: era 6.
- Martyrium Arethae (acts of the Najran martyrs). Unlocks: would document Timothy of Alexandria urging the Aksumite king to war. Links: aksumite-christianity--cyrilline-miaphysite-egyptian-christianity. Eras: era 3.
- Mary Baker Eddy, Science and Health (1875). Unlocks: would document the founding text. Links: no link id. Eras: era 9 part 2.
- Masius's letter to Busbecq and Sulaqa's profession of 1553. Unlocks: would document the 1552-1553 events from primary letters. Links: church-of-the-east-timur-to-hakkari--church-of-the-east-schism-of-1552. Eras: era 6.
- Matteo Ricci, Tianzhu shiyi (1603), with a record of its reading in Chosŏn Korea. Unlocks: would document the Korean reading of Ricci. Links: china-mission-born-christianity--korean-catholic-origins. Eras: era 9 part 2.
- Matthew of Edessa's complete Chronicle (Dulaurier 1858). Unlocks: would document the 1045 annexation and the catholicoi. Links: bagratid-armenian-christianity--armenian-cilicia. Eras: era 4.
- Medieval bishop lists of Skara or Lund; Scriptores rerum Suecicarum; Norway's and Iceland's sees. Unlocks: would document the sees across the Reformation. Links: scandinavian-conversion-christianity--scandinavian-reformation-kingdoms. Eras: era 4.
- Mendes, Expeditio Aethiopica, Books III-IV. Unlocks: would document the 1626 submission and 1633 expulsion. Note: Books I-II are vendored; III-IV are not. Links: no link id. Eras: era 7.
- Menno Simons or the Dordrecht Confession (1632) beside Mack; Durnbaugh 1958. Unlocks: would show which Anabaptist teaching the Brethren took up. Note: Menno Simons's complete works (Funk 1871) are vendored; Durnbaugh is not. Links: the-anabaptist-movements--radical-pietism-and-the-brethren-dunkers-ephrata. Eras: era 8.
- Methodist Episcopal Discipline of 1784 and Asbury's journal. Unlocks: would document the Methodist founding texts behind the American links. Note: Asbury's journal (1821) is vendored; the 1784 Discipline is not. Links: no link id. Eras: era 9 part 1.
- Methodist Episcopal record of the Bethel dispute from the white elders' side (John Emory's circular). Unlocks: would give the Bethel break from the white elders' side. Links: nineteenth-century-methodism--the-black-church-in-america. Eras: era 9 part 1.
- Methodist New Connexion Conference minutes for 1861 (Booth's resignation). Unlocks: would document the New Connexion break. Links: nineteenth-century-methodism--the-salvation-army. Eras: era 9 part 1.
- Metropolitan Andrey Sheptytsky's pastoral letters (1899-1906). Unlocks: would carry the church across 1906-1946. Links: ruthenian-greek-catholic-polotsk-to-galicia--the-ukrainian-greek-catholic-underground. Eras: era 9 part 2.
- Mexican Reform laws (Ley Lerdo 1856; Constitution of 1857; laws of 1859-60). Unlocks: would document the Reform laws. Links: no link id. Eras: era 9 part 2.
- Michael of Cesena's appeals of 1328 and protest of 1338. Unlocks: would give the minister general's own voice. Links: franciscan-order-era-6--latin-papal-church-avignon-to-lateran-v. Eras: era 6.
- Michael the Syrian, Chronicle Books XII-XXI (Chabot vol. III 1905). Unlocks: would document Michael's own patriarchate. Note: Book X is in vendored tome 2; Books XII-XXI are not. Links: syriac-orthodox-west-syriac-christianity--syriac-renaissance. Eras: era 5.
- Michael the Syrian, Chronique tome 3 (Chabot 1905), on Athanasius and Aimery at Antioch and Outremer. Unlocks: would give the Syriac side of the Latin states. Links: latin-church-of-outremer--byzantine-church-after-1054. Eras: era 5.
- Minutes and epistles of the Philadelphia and Ohio Yearly Meetings (1827-28); Elias Hicks, Sermons (1828) and Journal (1832). Unlocks: would document the Quaker separation from both parties. Links: no link id. Eras: era 9 part 1.
- Minutes of the Millerite conferences. Unlocks: would document the Millerite movement from its own decisions. Links: no link id. Eras: era 9 part 1.
- Missouri Synod's 1847 constitution or Walther's Der Lutheraner. Unlocks: would document the movement's subscription to the confessions. Links: lutheran-wittenberg-and-its-congregations--confessional-lutheran-revival-emigrations. Eras: era 9 part 1.
- Modern English translation of the Cologne Mani Codex. Unlocks: would document Mani's upbringing among the baptizers. Links: no link id. Eras: era 1.
- Movses Dasxuranci, History of the Caucasian Albanians, usable edition. Unlocks: would document the removal of Nerses Bakur. Links: armenian-christianity-after-avarayr--church-of-caucasian-albania, armenian-christianity-before-the-bagratids--church-of-caucasian-albania. Eras: era 3, major links era 3.
- Mrs Howard Taylor, Pastor Hsi: One of China's Christians (1903). Unlocks: would document Pastor Xi's self-led congregations. Links: the-missionary-movement-s-native-churches-seramp--the-chinese-church-indigenous-and-suffering. Eras: era 9 part 1.
- National Baptist Convention proceedings (c. 1895-1915). Unlocks: would document the Baptist side and the 1915 split. Links: the-black-church-in-america--the-black-church-in-the-twentieth-century. Eras: era 9 part 1.
- National Camp Meeting Association reports; Penuel (1869). Unlocks: would document the first camp meetings. Links: the-second-great-awakening-and-camp-meeting-worl--the-holiness-movement. Eras: era 9 part 1.
- Neercassel's correspondence with Arnauld. Unlocks: would document the friendship from the letters. Links: port-royal-jansenism--church-of-utrecht. Eras: era 8.
- Nerses Shnorhali's letters to Manuel I. Unlocks: would quote the correspondence from Nerses's side. Links: armenian-cilicia--byzantine-church-after-1054. Eras: era 5.
- Nestor's Life of Theodosius of the Caves or Primary Chronicle under 1074. Unlocks: would document the Studite rule arriving in Kyiv. Links: iconophile-byzantine-monasticism--kievan-rus-christianity-1054-1240. Eras: era 5.
- Nicholas IV's letters of 1288 to Arghun and Yahballaha III (Langlois). Unlocks: would give the papal side of the meeting. Links: church-of-the-east-under-the-mongols--latin-papal-church-gregorian. Eras: era 5.
- Niketas Choniates, History, on the sack of 1204. Unlocks: would document the 1204 sack. Links: latin-papal-church-gregorian--byzantine-church-after-1054--2. Eras: era 5.
- Niketas Stethatos, Life of Symeon the New Theologian. Unlocks: would document Symeon's Stoudite training. Links: iconophile-byzantine-monasticism--athonite-and-comnenian-byzantine-monasticism. Eras: era 4, era 5.
- Nikolai of Japan's diaries (1870-1911), reports to the Synod, pre-1930 English account of the Japan mission. Unlocks: would document the Japan mission from Nikolai's side. Links: russian-church-synodal-century--japanese-christianity-hidden-emergence-meiji. Eras: era 9 part 2.
- Nineteenth-century account of the Saxon emigration of 1838-39 (Vehse 1840). Unlocks: would document the Saxon company's own cause. Links: no link id. Eras: era 9 part 1.
- Nineteenth-century cofradía book or pastoral visitation from Spanish America or Brazil. Unlocks: would show continuity beyond Mexico. Links: colonial-latin-american-devotional-catholicism--nineteenth-century-latin-american-catholicism. Eras: era 9 part 2.
- Nineteenth-century Quaker text (Elias Hicks, Joseph John Gurney, 1827-28 separation minutes). Unlocks: would document the Quaker separation. Links: the-quakers-religious-society-of-friends--nineteenth-century-quakerism-separations. Eras: era 8.
- Nozaleda's decree excommunicating Aglipay (29 April 1899) and the Iglesia Filipina Independiente's founding proclamation (1902). Unlocks: would document the schism's start. Links: catholic-church-long-nineteenth-century--philippine-catholicism-gomburza-to-aglipay. Eras: era 9 part 2.
- Numismatic catalog or study of Aksumite coinage (Munro-Hay). Unlocks: would document Ezana's conversion through coinage. Links: no link id. Eras: era 2.
- Odilo of Cluny's All Souls statute and the 1041 Truce of God letter (MGH Const. I). Unlocks: would support the Odilo sentences. Links: no link id. Eras: era 4.
- Old Believer text appealing to the Muscovite fathers or the Stoglav (Avvakum's Life). Unlocks: would document the Old Believers' appeal. Links: muscovite-monastic-christianity--the-old-believers. Eras: era 6.
- Old Catholic synodal acts on clerical celibacy and the vernacular liturgy. Unlocks: would document the Old Catholic positions. Links: no link id. Eras: era 9 part 2.
- Old Nubian texts in a clean edition. Unlocks: would show the Coptic letters from the Nubian texts. Links: coptic-christianity-under-early-islam--makurian-nubian-christianity. Eras: era 4.
- Oneida announcement ending complex marriage (American Socialist, 28 August 1879) and the 1880-81 papers. Unlocks: would settle the 1880 vote. Links: no link id. Eras: era 9 part 2.
- Oriental Orthodox joint declarations (1984 Syriac Orthodox-Catholic statement; 1989-1990 agreed statements). Unlocks: would cite the Cyrilline dialogue sentence directly. Links: no link id. Eras: era 2.
- Pachymeres or Gregoras, Book V and after; Gregoras vol. 1. Unlocks: would give the Byzantine record of the patriarchs and the refusal of union. Note: Gregoras vols 2-3 are vendored; vol. 1 and Pachymeres are not. Links: byzantine-church-after-1054--byzantine-church-palaiologan, byzantine-church-after-1054--latin-papal-church-gregorian--2. Eras: era 5.
- Papal act confirming John Hormizd as patriarch of Babylon (1830). Unlocks: would date the confirmation. Links: catholic-church-long-nineteenth-century--church-of-the-east-chaldean-consolidation. Eras: era 9 part 2.
- Papal letters on recognizing the new republics' bishops (Leo XII, Gregory XVI). Unlocks: would document Rome's slow recognition. Links: catholic-church-long-nineteenth-century--nineteenth-century-latin-american-catholicism. Eras: era 9 part 2.
- Papal letters on the Bosnian heretics (Gregory IX) and the Franciscan vicariate of Bosnia (1340). Unlocks: would document the condemnation and the friars' founding documents. Links: latin-papal-church-avignon-to-lateran-v--the-bosnian-church. Eras: era 6.
- Papal or curial document on the Danish or Swedish break (1527-1537). Unlocks: would show Rome's side of the rupture. Links: no link id. Eras: era 7.
- Paris Parlement's arrêt and other public-domain primaries on the expulsion of the Jesuits (1757-1765). Unlocks: would document the expulsion from a primary. Links: no link id. Eras: era 8.
- Paris-school text naming Optina, once public domain. Unlocks: would document the Paris school's Optina. Links: the-optina-elders-and-russian-ascetic-renewal--emigre-orthodoxy-and-the-paris-school. Eras: era 9 part 2.
- Patriarchal acts (sigillia) of 1766 and 1767 abolishing Peć and Ohrid. Unlocks: would document the abolitions from a primary. Note: Gedeon vol. 1 is vendored; vol. 2 is not. Links: no link id. Eras: era 8.
- Patriarchal letters of 1686-87 transferring the Kyiv metropolia (Dionysius IV; Dositheus). Unlocks: would lift the Kyiv entry to Documented. Links: russian-church-nikon-to-holy-synod--the-kyiv-mohyla-orthodox-revival. Eras: era 8.
- Patriarchs of Antioch between 1009 and 1724 (patriarchal list or chronicle). Unlocks: would show the Melkite see continuing to 1724. Links: melkite-arabic-christianity--melkite-greek-catholic-church. Eras: era 4.
- Patriarchs' circular letter of 1724-25 deposing and excommunicating Cyril VI Tanas (Greek text). Unlocks: would give the deposition in its Greek text. Links: melkite-greek-catholic-church--orthodoxy-under-the-ottomans-1650-1821. Eras: era 8.
- Paul III's bull against Henry VIII (1538), clean edition. Unlocks: would give the Brutum Fulmen text in a readable copy. Links: no link id. Eras: era 7.
- Periodical Accounts of the Baptist Missionary Society (from 1800); Carey and Ward's Serampore letters. Unlocks: would document the first Serampore baptisms. Links: the-baptists--the-missionary-movement-s-native-churches-seramp. Eras: era 8.
- Peter Cartwright, Autobiography (1856); James B. Finley, Autobiography (1853). Unlocks: would give the circuit riders' own account of the camp meetings. Links: the-methodist-revival--the-second-great-awakening-and-camp-meeting-worl. Eras: era 9 part 1.
- Peter John Olivi, Lectura super Apocalypsim. Unlocks: would document Olivi's use of Joachim from his own text. Links: joachimite-current--franciscan-order-era-6. Eras: era 5.
- Peter the Venerable's letters or Toledan Collection preface. Unlocks: would support the Qur'an translation and the Abelard shelter. Links: no link id. Eras: era 4.
- Philadelphia Baptist Association minutes (Gillette, 1851), 1800-1830. Unlocks: would show the association on both sides of 1815. Links: the-baptists--nineteenth-century-baptists. Eras: era 9 part 1.
- Phoebe Palmer, The Way of Holiness (1843), Entire Devotion to God (1845); Guide to Holiness (1839-). Unlocks: would let the Holiness links from Methodism be re-graded. Links: nineteenth-century-methodism--the-holiness-movement, the-second-great-awakening-and-camp-meeting-worl--the-holiness-movement. Eras: era 9 part 1.
- Photius, Homily 17 (apse mosaic, 867), public-domain edition. Unlocks: would document the 'imposters had been answered' line. Links: byzantine-imperial-church-heraclian-iconoclast--byzantine-imperial-church-macedonian. Eras: era 4.
- Pierre Nicole, Réfutation des principales erreurs des quiétistes (1695). Unlocks: would document an 'argued against' link from Port-Royal's side. Links: port-royal-jansenism--quietist-controversy-molinos-guyon. Eras: era 8.
- Pierre Poiret's editions of Guyon or Tersteegen's translations. Unlocks: would document German Pietist reading of Guyon. Links: quietist-controversy-molinos-guyon--german-pietism-spener-francke-halle. Eras: era 8.
- Premillennial Essays of the 1878 New York prophetic conference; the Niagara Creed (1878). Unlocks: would document the 1878 prophetic conference. Links: plymouth-brethren-and-dispensational-formation--dispensational-prophecy-culture. Eras: era 9 part 1.
- Primary account of the Kodiak mission of 1794 (mission letters; Valaam's history). Unlocks: would support the 1794 date and the Valaam origin. Links: russian-church-nikon-to-holy-synod--alaskan-mission-herman-veniaminov. Eras: era 8.
- Primary for the capture of Tabor in 1452 (Aeneas Sylvius; Old Czech Annals). Unlocks: would give the outcome a contemporary text. Links: the-hussite-and-bohemian-brethren-movement--taborite-radicalism--2. Eras: era 6.
- Primary witnesses for the 1448 election (Russian chronicles, Basil II's letter) and Acta patriarchatus vol. 2. Unlocks: would give the 1448 step and the Rus' metropolitans primary witnesses. Links: byzantine-church-palaiologan--muscovite-monastic-christianity. Eras: era 6.
- Priscillian's Würzburg Tractates on the Manichaean charge at his trial. Unlocks: would document the accusation at the trial. Links: no link id. Eras: era 2.
- Proceedings of the Society for Psychical Research, vol. 1 (1882-83). Unlocks: would document the Society's founding. Links: no link id. Eras: era 9 part 2.
- Prussian Union documents of 1817 and the Old Lutheran persecution record. Unlocks: would document the Prussian merger and the 1838 emigration. Links: no link id. Eras: era 9 part 1.
- Quaker writer of the period naming Guyon or Molinos in his own words. Unlocks: would document a Quaker reading of the quietists. Links: quietist-controversy-molinos-guyon--the-quakers-religious-society-of-friends. Eras: era 8.
- R. P. Ashe, Two Kings of Uganda (1889); Mackay of Uganda (1890). Unlocks: would document Buganda and the martyrs from the missionary side. Links: victorian-church-of-england--east-african-christianity-uganda-martyrs. Eras: era 9 part 2.
- Rainerius Sacconi, Summa de Catharis (Dondaine 1939 or public-domain translation). Unlocks: would quote Sacconi directly. Links: balkan-bogomil-continuation--cathars-albigensians, bogomils--cathars-albigensians. Eras: era 4, era 5.
- Raymond of Capua's reform letters of 1390. Unlocks: would document the Dominican Observance. Links: no link id. Eras: era 6.
- Record of Innocent Veniaminov's election as Metropolitan of Moscow (1868). Unlocks: would document the election. Links: russian-church-synodal-century--alaskan-mission-herman-veniaminov. Eras: era 9 part 2.
- Regularis Concordia (c. 970), public-domain edition or translation. Unlocks: would document the English Benedictine reform rule. Links: early-benedictine-italian-monasticism--late-anglo-saxon-christianity. Eras: era 4.
- Reuben Briggs Davenport, The Death-Blow to Spiritualism (1888). Unlocks: would document Margaret Fox's 1888 confession. Links: no link id. Eras: era 9 part 2.
- Reusch's official reports of the 1874 and 1875 Bonn conferences. Unlocks: would list the Greek participants and whom they represented. Links: old-catholic-churches-union-of-utrecht--orthodoxy-after-1821-balkan-autocephalies. Eras: era 9 part 2.
- Review and Herald (1850-), 1863 General Conference records, 1872 Declaration of Fundamental Principles. Unlocks: would document the Adventist bodies from their own records. Links: restorationist-apocalyptic-ferment-and-adventism--seventh-day-adventist-church-twentieth-century. Eras: era 9 part 1.
- Ricci's Italian commentaries (Tacchi Venturi 1911-13) or a better scan of Trigault 1615. Unlocks: would give a cleaner text of the China mission's beginnings. Links: no link id. Eras: era 7.
- Richard of St Victor, Benjamin Minor and Benjamin Major (PL 196). Unlocks: would set the Victorine text beside the Cloud author's Benjamin. Links: canons-regular-victorine-school--the-english-mystics-and-devout. Eras: era 5.
- Rimbert, Vita Anskarii, public-domain translation (Robinson 1921). Unlocks: would document Anskar's mission from his own disciple. Links: carolingian-reform-christianity--scandinavian-conversion-christianity. Eras: era 4.
- Robert Roberts, Christendom Astray (1862; 1884) and the Birmingham Statement of Faith (1886). Unlocks: would document the Birmingham statement. Links: no link id. Eras: era 9 part 2.
- Rosenius's Pietisten (from 1842); Paavo Ruotsalainen's letters. Unlocks: would document the wider Nordic revivals. Links: no link id. Eras: era 9 part 1.
- Royal chronicle of Fasilides, public-domain edition. Unlocks: would document the 1633-34 expulsion from the Ethiopian side. Links: no link id. Eras: era 7.
- Royal chronicle of Menelik II (Gabra Sellase), church and court across 1900. Unlocks: would document the court's church. Links: ethiopian-christianity-tewodros-to-menelik--modern-ethiopian-and-eritrean-christianity. Eras: era 9 part 2.
- Royal chronicle of Yohannes IV (four bishops from Alexandria, 1881); Tewodros II; Boru Meda council (1878). Unlocks: would document the Ethiopian court's account. Links: coptic-revival-under-cyril-iv--ethiopian-christianity-tewodros-to-menelik. Eras: era 9 part 2.
- Royal proclamation of 3 October 1580 against the Family of Love. Unlocks: would document the 1580 proclamation directly. Links: no link id. Eras: era 7.
- Rufinus's preface to his Latin translation of Basil. Unlocks: would document the Basil translations from Rufinus's side. Links: cappadocian-nicene-pastoral-monastic-tradition--aquileian-christianity. Eras: era 2.
- Rufinus, Church History X.9-10, or a clean read of the Schwartz-Mommsen Latin. Unlocks: would document Frumentius's earliest account. Note: The Schwartz-Mommsen Latin is vendored; the English is not. Links: no link id. Eras: era 2.
- Rule of the Temple (Henri de Curzon, 1886), for the Council of Troyes (1129). Unlocks: would document the Templars' rule. Links: no link id. Eras: era 5.
- Rules of Edinoverie approved by Paul I (27 October 1800), with Metropolitan Plato's replies. Unlocks: would lift the Edinoverie entry to Documented. Links: russian-church-nikon-to-holy-synod--the-old-believers--3. Eras: era 8.
- Russian acts of the 1875 Chełm reunion; Gregory XVI's allocution of 22 November 1839 against the Polotsk act. Unlocks: would document the two reunions from their own texts. Links: russian-church-synodal-century--ruthenian-greek-catholic-polotsk-to-galicia. Eras: era 9 part 2.
- Russian Baptist accounts of the 1884 founding congress; Modest Korff, Am Zarenhof (1927). Unlocks: would document the failed St Petersburg union. Links: no link id. Eras: era 9 part 1.
- Russian Holy Synod's acts of 1839, in their own edition. Unlocks: would document the Synod's 1839 act from its own text. Links: no link id. Eras: era 9 part 2.
- Russian Primary Chronicle (Laurentian text), vendored public-domain edition. Unlocks: would document the Slavonic letters (s.a. 898), the envoys (987), Vladimir's baptism (988), the Greek clergy and the metropolitans. Links: byzantine-church-after-1054--kievan-rus-christianity-1054-1240, byzantine-imperial-church-macedonian--kievan-rus-christianity, cyrillo-methodian-slavic-christianity--kievan-rus-christianity, iconophile-byzantine-monasticism--kievan-rus-christianity-1054-1240. Eras: era 4, era 5, major links era 4.
- Sacrosanctum Concilium (1963) and Missale Romanum (1969). Unlocks: would document the Tridentine Missal's revision. Links: no link id. Eras: era 7.
- Salimbene de Adam, Chronicle (MGH SS 32). Unlocks: would give a Franciscan's account of Joachite expectation. Links: joachimite-current--the-franciscan-movement. Eras: era 5.
- Sava's Life of Symeon (Stefan Nemanja) and the Hilandar and Karyes typika; Domentijan's or Teodosije's Life of Sava. Unlocks: would document Athonite charters adapted for Serbian monasteries. Links: athonite-and-comnenian-byzantine-monasticism--serbian-and-bulgarian-medieval-monasticism. Eras: era 5.
- Second Helvetic Confession ch. XI, clean Latin or German text. Unlocks: would replace the garbled OCR that names Schwenckfeld. Links: no link id. Eras: era 7.
- Serampore Form of Agreement (1805) and Carey's Serampore letters (public-domain edition). Unlocks: would show the Moravian model at work in the Serampore church. Links: the-moravian-church-at-herrnhut--the-missionary-movement-s-native-churches-seramp. Eras: era 9 part 1.
- Sergii Chetverikov, Optina Pustyn' (Paris, 1926). Unlocks: would document Optina's history. Links: the-optina-elders-and-russian-ascetic-renewal--emigre-orthodoxy-and-the-paris-school, the-optina-elders-and-russian-ascetic-renewal--the-russian-new-martyrs-and-the-catacomb-church. Eras: era 9 part 2.
- Simeon of Erevan's Partavjar and letters or encyclicals of the catholicoi of Etchmiadzin. Unlocks: would document the Etchmiadzin side of the 1700s. Links: armenian-apostolic-church-era-8--catholic-church-ancien-regime. Eras: armenian-apostolic era 8.
- Smotrytsky's Apologia (1628) or the Lithos (1644). Unlocks: would document the union's case against Orthodox Kyiv. Links: no link id. Eras: era 7.
- Snorri Sturluson, Heimskringla (Olaf sagas), public-domain translation. Unlocks: would document the English clergy with the two Olafs. Links: late-anglo-saxon-christianity--scandinavian-conversion-christianity. Eras: era 4.
- Source for AME Zion Church's founding in 1821 (Christopher Rush, 1843). Unlocks: would document the founding. Links: no link id. Eras: era 8.
- Soviet or church record of Optina's closure (1918 or 1923) and its monks' fate. Unlocks: would document Optina's closure. Links: the-optina-elders-and-russian-ascetic-renewal--the-russian-new-martyrs-and-the-catacomb-church. Eras: era 9 part 2.
- Spener, Pia Desideria and letters; Dutch authors read in German (Teellinck, Lodenstein, Brakel). Unlocks: would document a direct Further Reformation tie to Halle. Links: no link id. Eras: era 7.
- Statute 27 Eliz. c. 2 (1585) against Jesuits and seminary priests. Unlocks: would document the statute. Links: no link id. Eras: era 7.
- Stefan Nemanja's Hilandar founding charter, quotable text (Miklosich 1858). Unlocks: would document the founding charter. Links: athonite-and-comnenian-byzantine-monasticism--serbian-and-bulgarian-medieval-monasticism. Eras: era 5.
- Stefano Infessura, Diario della città di Roma (1467). Unlocks: would document Paul II's penance of the fraticelli. Links: latin-papal-church-avignon-to-lateran-v--fraticelli-spiritual-franciscan-rigorists. Eras: era 6.
- Stephen of Taron (Asoghik), Universal History III (Dulaurier 1883; Macler 1917). Unlocks: would document Trdat's repair of the dome. Links: no link id. Eras: era 4.
- Subscribing side's account of Salters' Hall (1719). Unlocks: would show the subscribing side's account. Links: english-old-dissent--the-baptists. Eras: era 8.
- Sulaqa's profession of 1553 and the Roman consistorial acts. Unlocks: would document the profession from the Roman side. Links: church-of-the-east-timur-to-hakkari--church-of-the-east-schism-of-1552. Eras: era 6.
- Surma d'Mar Shimun, Assyrian Church Customs and the Murder of Mar Shimun (1920). Unlocks: would give an inside witness for 1915-18. Links: church-of-the-east-chaldean-consolidation--the-sayfo-and-the-syriac-diaspora. Eras: era 9 part 2.
- Sylvester Kossov, Exegesis (Kyiv, 1635), or the Mohyla college statutes. Unlocks: would give a primary witness to the Jesuit model. Links: the-society-of-jesus--the-kyiv-mohyla-orthodox-revival. Eras: era 7.
- Synod at Constantinople usually dated 1484 formally repudiating Florence. Unlocks: would document the formal repudiation. Links: byzantine-church-palaiologan--latin-papal-church-avignon-to-lateran-v. Eras: era 6.
- Synod's own minute of 21 August 1715, or the earliest extant rules (1716-1717). Unlocks: would document the first synod's rule. Links: church-of-the-desert-huguenots--camisard-prophetism. Eras: era 8.
- Synodikon of Orthodoxy (843), public-domain text. Unlocks: would document the restoring synod from the church's own side. Links: iconophile-byzantine-monasticism--byzantine-imperial-church-macedonian. Eras: era 4, major links era 4.
- Tacitus, Agricola 24, or a vendored text saying Ireland lay outside the Empire. Unlocks: would document the Irish outside-the-Empire claim. Links: no link id. Eras: era 3.
- Tamara Grdzelidze, Georgian Monks on Mount Athos (2009), read and cited by page. Unlocks: would document Georgian monks on Athos. Links: athonite-and-comnenian-byzantine-monasticism--georgian-revival-tao-klarjeti, athonite-and-comnenian-byzantine-monasticism--the-georgian-golden-age. Eras: era 4, era 5.
- Tauler's sermons naming his Dominican profession. Unlocks: would document Tauler's Dominican profession. Links: the-dominican-order--rhineland-mysticism-and-the-friends-of-god. Eras: era 5.
- Text of the Compacts (Archiv český III; Mansi XXIX-XXX). Unlocks: would quote the chalice concession from the council's words. Links: latin-papal-church-avignon-to-lateran-v--the-hussite-and-bohemian-brethren-movement--2. Eras: era 6.
- Text recording Joseph Hubert Reinkens's 1873 consecration by an Utrecht-line bishop. Unlocks: would document 'Utrecht supplied them'. Links: church-of-utrecht--old-catholic-churches-union-of-utrecht. Eras: era 8.
- The Apostolic Faith (Los Angeles, 1906-1908) and Frank Bartleman, How Pentecost Came to Los Angeles (1925). Unlocks: would let both links into Azusa Street be re-graded. Links: the-black-church-in-america--azusa-street-and-early-pentecostalism. Eras: era 9 part 1.
- The Book of Margery Kempe in full, with a description of the Mount Grace manuscript. Unlocks: would document the Kempe facts. Links: no link id. Eras: era 6.
- Theodore Hamberg, The Visions of Hung-Siu-tshuen (Hong Kong, 1854). Unlocks: would document Hong's reading of Liang Fa's tract. Links: the-missionary-movement-s-native-churches-seramp--taiping-heavenly-kingdom. Eras: era 9 part 1, era 9 part 2.
- Theodore of Mopsuestia's surviving comments against allegory (Galatians 4:24, Swete 1880). Unlocks: would document Theodore's stance from his own text. Links: antiochene-exegetical-christianity-chrysostom-ce--alexandria-catechetical. Eras: era 2.
- Theodore Parker, A Discourse of the Transient and Permanent in Christianity (1841). Unlocks: would test how far the Transcendentalists left Christian doctrine. Links: no link id. Eras: era 9 part 2.
- Theodore the Studite, letters or Antirrhetici (PG 99); Patriarch Nicephorus, Antirrhetici (PG 100). Unlocks: would document a monk and patriarch writing against the iconoclasts. Links: iconophile-byzantine-monasticism--byzantine-imperial-church-heraclian-iconoclast. Eras: era 4.
- Theodore's Syriac-only works (Mingana, Catechetical Homilies, 1932-33). Unlocks: would document 'survives only in Syriac' directly. Links: antiochene-exegetical-christianity-chrysostom-ce--the-church-of-the-east-under-persia. Eras: era 2.
- Theophan the Recluse, Dobrotolubie v russkom perevode (1877-90). Unlocks: would document the Russian Philokalia. Links: the-kollyvades-and-greek-renewal--russian-church-synodal-century. Eras: era 9 part 2.
- Theophanes, Chronographia (de Boor 1883), on Constantine V and Michael I (Paulicians, monks). Unlocks: would document the iconoclast measures. Links: byzantine-imperial-church-heraclian-iconoclast--iconophile-byzantine-monasticism, byzantine-imperial-church-heraclian-iconoclast--paulicians. Eras: era 4, major links era 4.
- Thomas Campbell, Declaration and Address (1809). Unlocks: would document the Campbell wing's separate origin. Links: the-second-great-awakening-and-camp-meeting-worl--the-stone-campbell-restoration-movement. Eras: era 9 part 1.
- Thomas Charles's account of the Welsh Sunday schools (Jones's Cofiant, 1816), in English. Unlocks: would document Sunday-school literacy. Links: no link id. Eras: era 8.
- Thomas Fuller, The Church History of Britain, vol. IV (1845), Familist passage. Unlocks: would document the 1580 proclamation in Fuller's text. Links: no link id. Eras: era 7.
- Thomas Helwys, A Declaration of Faith (1611) and A Short Declaration (1612), clean edition. Unlocks: would give the Helwys side of the passage out of Separatism. Links: puritanism--the-baptists. Eras: era 8.
- Thomas of Celano, First Life 32-33. Unlocks: would document the 1209/1210 audience with Innocent III. Links: latin-papal-church-gregorian--the-franciscan-movement. Eras: era 5.
- Thomas of Celano, Second Life of Francis 148-150. Unlocks: would document the earliest telling of the meeting. Links: the-dominican-order--the-franciscan-movement. Eras: era 5.
- Thomas of Metsoph's own account of the 1441 council and his chronicle. Unlocks: would give the 1441 move a primary witness. Links: armenian-cilicia-after-the-kingdom--armenian-christianity-new-julfa. Eras: era 6.
- Thomas Shepard, The Parable of the Ten Virgins (1660). Unlocks: would set Shepard beside Edwards's citations. Links: puritanism--the-evangelical-awakening-in-new-england. Eras: era 8.
- Toledo III acts, public-domain English or cleaner Latin. Unlocks: would document the Filioque council. Links: nicene-visigothic-iberia--gothic-and-vandal-homoian-christianity. Eras: era 3.
- Tomes of 1347 and 1351 (Palamite councils), clean edition. Unlocks: would quote the later councils' rulings. Links: hesychasm-and-the-palamite-synthesis--byzantine-church-palaiologan. Eras: era 6.
- Tomos of 1970 granting autocephaly to the Orthodox Church in America. Unlocks: would document the autocephaly. Links: alaskan-mission-herman-veniaminov--american-orthodoxy-autocephaly-and-the-convert-wave. Eras: era 9 part 2.
- Toulouse canonization testimonies of 1233 (Lehner 1964). Unlocks: would document Dominic's Languedoc preaching. Links: the-dominican-order--cathars-albigensians. Eras: era 5.
- Tracts for the Times (1833-41), Tracts 1 and 90; Keble's Assize Sermon 'National Apostasy' (1833). Unlocks: would document the Oxford Movement's own texts. Links: victorian-church-of-england--the-oxford-movement-and-anglo-catholic-revival. Eras: era 9 part 1.
- Travancore Royal Court judgment of 1889 (Seminary case); Abraham Malpan's revised liturgy (1836). Unlocks: would document the final rupture and the Mar Thoma side. Links: northeast-india-revivals-and-the-mar-thoma-refor--the-malankara-churches-orthodox-and-jacobite. Eras: era 9 part 1.
- Troitski, Refutation of the errors of Stundism (Kiev 1890); Rozhdestvenski (St Petersburg 1889). Unlocks: would give the Orthodox texts themselves. Links: russian-church-synodal-century--russian-evangelicals-stundists--2. Eras: era 9 part 1.
- Tsar Boril's Synodikon (1211). Unlocks: would document the Tarnovo anathema. Links: no link id. Eras: era 5.
- Typikon and Life of Athanasios the Athonite (Meyer 1894). Unlocks: would document the Stoudite rule on Athos and Nikephoros Phokas as patron. Links: byzantine-imperial-church-macedonian--athonite-and-comnenian-byzantine-monasticism, iconophile-byzantine-monasticism--athonite-and-comnenian-byzantine-monasticism. Eras: era 4, era 5, major links era 4.
- Typikon of Gregory Pakourianos for Petritsoni (1083), Dumbarton Oaks 2000. Unlocks: would document the Georgian Athonite typikon. Links: athonite-and-comnenian-byzantine-monasticism--the-georgian-golden-age. Eras: era 5.
- U.S. Bureau of the Census, Religious Bodies: 1906 (Washington, 1910), and Lipscomb's letters. Unlocks: would document the separate listing of the Churches of Christ. Links: the-stone-campbell-restoration-movement--churches-of-christ-twentieth-century, the-stone-campbell-restoration-movement--disciples-of-christ-and-independent-christian-churches. Eras: era 9 part 1.
- Ukhtanes of Edessa, History of the Separation of the Georgians from the Armenians (Brosset 1870). Unlocks: would document the break as the Brosset note cites it. Links: armenian-christianity-before-the-bagratids--georgian-christianity. Eras: era 3.
- Uppsala decree of 1593 in its own text. Unlocks: would document 'the unaltered Augsburg Confession'. Links: no link id. Eras: era 7.
- Utraquist source across 1517 (consistory acts or Bohemian Confession of 1575). Unlocks: would show the Utraquist half of the continuation. Links: the-hussite-and-bohemian-brethren-movement--czech-churches-last-century. Eras: era 6, era 7.
- Utrecht dossier pieces citing Arnauld (Recueil de divers témoignages, 1763). Unlocks: would document the 1725 citations of Arnauld. Note: The Recueil de divers témoignages (1763) is vendored; check whether it meets the clean-text want. Links: port-royal-jansenism--church-of-utrecht. Eras: era 8.
- Uyghur khagan Bogu's adoption of Manichaeism (Karabalgasun inscription in translation). Unlocks: would replace a secondhand report for the Uyghur adoption. Links: no link id. Eras: era 1.
- Valdes's profession of faith (1180). Unlocks: would document the orthodox confession from Valdes's side. Links: latin-papal-church-gregorian--the-waldensians. Eras: era 5.
- Vatican I constitutions (1870), public-domain edition. Unlocks: would document the 1870 definitions the Old Catholic entry names. Links: no link id. Eras: era 9 part 2.
- Vendored history of the Russian Baptist and Evangelical Christian unions, 1884-1944. Unlocks: would document the unions. Links: russian-evangelicals-stundists--persecuted-church-worlds-of-the-communist-era-in. Eras: era 9 part 1.
- Vendored Irish annal (Ulster or Tigernach) naming Irish houses and abbots on both sides of 664. Unlocks: would document Irish houses across the Easter settlement. Links: insular-irish-monastic-christianity--medieval-irish-christianity. Eras: era 4.
- Vendored Methodist text after 1815 (Wesleyan Conference Minutes or Methodist Episcopal Discipline, 1820s). Unlocks: would carry the same bodies into the later period. Links: the-methodist-revival--nineteenth-century-methodism. Eras: era 8.
- Vendored primary text placing Sergius in office before and after 622 (Chronicon Paschale, Theophanes). Unlocks: would document Sergius in office on both sides of 622. Links: byzantine-imperial-church-justinianic--byzantine-imperial-church-heraclian-iconoclast. Eras: era 3.
- Vendored text on Montségur (1244) and Bélibaste (1321), e.g. the Fournier register. Unlocks: would document the last Cathar strongholds. Links: latin-papal-church-gregorian--cathars-albigensians. Eras: era 5.
- Vendored Victorian Church of England text naming the 1662 Prayer Book in force after 1815. Unlocks: would document the Prayer Book's use after 1815. Links: restoration-georgian-church-of-england--victorian-church-of-england. Eras: era 8.
- Venice 1782 first edition of the Philokalia (title page and prooimion). Unlocks: would document the fourteenth-century fathers named there. Links: hesychasm-and-the-palamite-synthesis--the-hesychast-revival-paisius-and-the-philokalia. Eras: era 6.
- W. E. B. Du Bois (ed.), The Negro Church (1903). Unlocks: would survey the same bodies on the eve of 1906. Links: the-black-church-in-america--the-black-church-in-the-twentieth-century. Eras: era 9 part 1.
- W. H. Burgess, John Smith the Se-Baptist, Thomas Helwys (1911). Unlocks: would give a secondary account of the contact. Links: the-anabaptist-movements--the-baptists. Eras: era 8.
- W. T. Whitley, The Works of John Smyth, vol. I (1915). Unlocks: would document Smyth's Puritan years. Links: no link id. Eras: era 7.
- Wadding, Annales Minorum, ann. 1368 (nos. 10-13), on Brugliano. Unlocks: would give the 1368 grant a primary. Links: franciscan-order-era-6--observant-reform-and-popular-preaching. Eras: era 6.
- Waterlander church minutes on the English applicants; Hans de Ries's correspondence. Unlocks: would show the Mennonite side of the contact. Links: the-anabaptist-movements--the-baptists. Eras: era 8.
- Welsh bishops' professions of obedience to Canterbury (Eadmer; Gerald of Wales). Unlocks: would document the twelfth-century Welsh obedience. Links: no link id. Eras: era 3.
- Welsh Calvinistic Methodist foreign mission reports for the Khasi hills (nineteenth century). Unlocks: would document the hill churches' side. Links: northeast-india-revivals-and-the-mar-thoma-refor--northeast-india-and-mar-thoma-twentieth-century. Eras: era 9 part 1.
- Wesley's Christian Library (1749-55), vendored edition. Unlocks: would show Methodist preachers reading the Puritans. Links: puritanism--the-methodist-revival. Eras: era 8.
- White Fathers' Buganda diaries or Lourdel's letters (1879-1890). Unlocks: would document the Catholic side of Buganda. Links: catholic-church-long-nineteenth-century--east-african-christianity-uganda-martyrs. Eras: era 9 part 2.
- Whitefield's Journal for March 1739 (Cardiff). Unlocks: would give Whitefield's side of the meeting. Note: Whitefield's 1756 'Two First Parts ... with Journals' is vendored; check for the March 1739 journal. Links: the-methodist-revival--the-welsh-revival-tradition. Eras: era 8.
- William Booth, In Darkest England and the Way Out (1890). Unlocks: would document the Army's founding text. Links: no link id. Eras: era 9 part 1.
- William Ellis, History of Madagascar (1838) and Madagascar Revisited (1867). Unlocks: would document the 1835 ban and the persecution. Links: no link id. Eras: era 9 part 2.
- William Miller, Evidence from Scripture and History of the Second Coming of Christ (Troy, 1836). Unlocks: would document Miller's own argument. Links: the-second-great-awakening-and-camp-meeting-worl--restorationist-apocalyptic-ferment-and-adventism. Eras: era 9 part 1.
- William of Tyre, Historia rerum in partibus transmarinis gestarum (RHC 1844). Unlocks: would document the first Latin patriarchs, the Armenian catholicos at Jerusalem, and the Maronite union. Links: armenian-cilicia--latin-church-of-outremer, latin-church-of-outremer--maronite-christianity, latin-papal-church-gregorian--latin-church-of-outremer. Eras: era 5.
- World Missionary Conference, 1910, Report of Commission VIII and vol. IX (Edinburgh, 1910). Unlocks: would document the Continuation Committee and the Azariah and Chinese delegates. Links: the-student-volunteer-movement-and-edinburgh-191--the-ecumenical-movement-and-the-wcc. Eras: era 9 part 1.
- Xi'an stele of 781, reliable translation of its Syriac lines (Legge or Saeki). Unlocks: would quote the catholicos's name and the 635 arrival from the stele. Links: the-church-of-the-east-under-persia--the-church-of-the-east-on-the-silk-road. Eras: era 3, era 4.
- Zartonk-era Armenian text naming Mekhitarist editions or dictionaries as its basis. Unlocks: would lift the entry to Documented. Links: armenian-christianity-era-8--armenian-christianity-zartonk. Eras: era 8.
- Zinzendorf's writings on Herrnhut's founding; Brotherly Agreement and Statutes of Herrnhut (1727). Unlocks: would show the Spener debt in the Herrnhut documents. Links: czech-churches-last-century--the-moravian-church-at-herrnhut, german-pietism-spener-francke-halle--the-moravian-church-at-herrnhut. Eras: era 8.
- Ælfric's Catholic Homilies (Thorpe 1844-46) and Wulfstan's Sermo Lupi (1014). Unlocks: would document the Anglo-Saxon homiletic witnesses. Links: no link id. Eras: era 4.
- Æthelwold's Old English account of King Edgar's monasteries; Wulfstan of Winchester's Life of Æthelwold. Unlocks: would document Edgar's monastic foundations. Links: early-benedictine-italian-monasticism--late-anglo-saxon-christianity. Eras: era 4.

### Would test a contested or thin claim (109)

- 1834 Act of Secession (Acte van Afscheiding) and da Costa's Bezwaren (1823). Unlocks: would test how far the Dutch awakening and the secession were linked. Links: no link id. Eras: era 9 part 1.
- Any text from 1054-1300 naming Christians of Kollam or Malabar. Unlocks: would close the gap in the Kollam link. Links: st-thomas-christians-of-india--st-thomas-christians-1300-1517. Eras: era 4.
- Any text saying Basil's grandmother Macrina was taught by Gregory Thaumaturgus's disciples. Unlocks: would test a thin claim about Macrina's teachers. Links: no link id. Eras: era 1.
- Balavariani and Euthymius of Athos as the source of Barlaam and Josaphat. Unlocks: would test the 'may have' link. Links: no link id. Eras: era 4.
- Bernard of Clairvaux, Sermons on the Song of Songs and De diligendo Deo. Unlocks: would test whether the sayings Rolle and Hilton credit to Bernard are his. Links: cistercian-monasticism--the-english-mystics-and-devout. Eras: era 5.
- Bibliotheca Fratrum Polonorum or Limborch's writings. Unlocks: would test Socinian influence on the Remonstrants. Links: no link id. Eras: era 7.
- Bociurkiw (1996), read and cited by page, for the 1946 Lviv synod. Unlocks: would test the 1946 Lviv synod claim. Links: ruthenian-greek-catholic-polotsk-to-galicia--the-ukrainian-greek-catholic-underground. Eras: era 9 part 2.
- Byzantine synodal or patriarchal text of 1054-1240 naming a metropolitan of Kyiv. Unlocks: would test the metropolitan line. Links: byzantine-church-after-1054--kievan-rus-christianity-1054-1240. Eras: era 5.
- C. H. Spurgeon, the Down-Grade articles (The Sword and the Trowel, 1887). Unlocks: would test the Down-Grade account. Links: no link id. Eras: era 9 part 1.
- Carmelite hermits to friars in the 1240s; Albert keeping his seat at Acre. Unlocks: would test the Carmelite move west and the friars' change. Links: the-dominican-order--the-carmelites. Eras: era 5.
- Chalcedonian-side account of the 540s embassy to the Makurians (John of Biclarum). Unlocks: would test the Nubian embassy claim. Links: byzantine-imperial-church-justinianic--nubian-christianity. Eras: era 3.
- Charles Taze Russell, Zion's Watch Tower (1879-) and Studies in the Scriptures vol. 1 (1886). Unlocks: would test the circle's sources. Links: no link id. Eras: era 9 part 2.
- Contemporary record of the Wardley society in the 1740s-1760s, or a Quaker record naming the Wardleys. Unlocks: would test the Shakers' account of a French Prophet origin. Links: camisard-prophetism--shakers, the-quakers-religious-society-of-friends--shakers. Eras: era 8.
- Court and tribunal reports (Jehovah's Witnesses, Christian Science, objector tribunals), twentieth century. Unlocks: would test the legal side of the claim. Links: no link id. Eras: era 9 part 2.
- Dated witness to the Armenian translation of Timothy Aelurus's Refutation or the Book of Letters (451-554). Unlocks: would test the transmission of Egyptian texts to Armenia. Links: no link id. Eras: era 3.
- David Gaunt, Massacres, Resistance, Protectors (2006), read and cited by page. Unlocks: would test the 1915 flight of the Hakkari Assyrians. Links: church-of-the-east-chaldean-consolidation--the-sayfo-and-the-syriac-diaspora. Eras: era 9 part 2.
- Dongola and the year 652 of the Baqt (al-Maqrizi on the Baqt; Welsby 2002). Unlocks: would test the 652 date for Dongola. Links: no link id. Eras: era 3.
- Earlier witness to John of the Sedre's patriarchate across the conquest. Unlocks: would test the patriarchal continuity across the conquest. Links: syriac-orthodox-west-syriac-christianity--syriac-orthodox-under-islam. Eras: era 3.
- Early history of the Geneva awakening naming its Moravian contacts (Bost, Mémoires). Unlocks: would test the Moravian contacts of the Geneva awakening. Links: the-moravian-church-at-herrnhut--the-reveil-and-inner-mission-awakening. Eras: era 9 part 1.
- Erasmus's Compendium vitae (Deventer schooling). Unlocks: would test the Erasmus-Brethren link from a primary. Links: no link id. Eras: era 6.
- Faras bishop list or other text of the Nubian church, 652-697. Unlocks: would test the Nubian church between 652 and 697. Links: nubian-christianity--makurian-nubian-christianity. Eras: era 3.
- Finney, Lectures on Revivals of Religion (1835). Unlocks: would test 'parent of later American revival culture'. Links: no link id. Eras: era 9 part 1.
- Finney, Lectures on Revivals of Religion (1835), or another text naming Edwards and Whitefield. Unlocks: would test 'parent of later American revival culture'. Links: no link id. Eras: era 8.
- Frances Young, Biblical Exegesis and the Formation of Christian Culture (1997), read. Unlocks: would test the modern view of the Antioch-Alexandria contrast. Links: antiochene-exegetical-christianity-chrysostom-ce--alexandria-catechetical. Eras: era 2.
- Frend, The Rise of the Monophysite Movement (1972), read and cited by page. Unlocks: would test the same Syriac Orthodox link. Links: no link id. Eras: era 1.
- Garsoian or other modern study of the Armenian church's tie to Caesarea. Unlocks: would test the Armenian-Caesarea tie. Links: cappadocian-nicene-pastoral-monastic-tradition--armenian-christianity-conversion-era. Eras: era 2.
- Georgian-side text recording the break. Unlocks: would test the Armenian-Georgian break from the Georgian side. Links: armenian-christianity-before-the-bagratids--georgian-christianity. Eras: era 3.
- German Pietist text naming a Dutch precisian source (Teellinck, Lodenstein, Voetius, Labadie). Unlocks: would test the Dutch clause before it returns as fact. Links: no link id. Eras: era 8.
- Gildas fragments as cited by Columbanus, and the Irish catalog of saints. Unlocks: would test the wider Irish reception of Columbanus. Links: british-welsh-christianity--insular-irish-monastic-christianity. Eras: era 3.
- Gippert et al., The Caucasian Albanian Palimpsests of Mount Sinai (2008), read. Unlocks: would test the 1996 identification and the Udi connection. Links: no link id. Eras: era 3.
- Gregory VII's letters of 1076 on Latin Christian communities in North Africa. Unlocks: would test the date of the end of North African Latin churches. Links: no link id. Eras: era 1.
- Guidi, Il Fetha Nagast (1897-1899); al-Safi ibn al-Assal, Nomocanon. Unlocks: would test the Fetha Nagast's derivation. Links: no link id. Eras: era 5.
- Guigo I, Consuetudines Cartusiae (PL 153). Unlocks: would test whether the Carthusians tied their life to the desert fathers. Links: no link id. Eras: era 5.
- Guigo II, Scala claustralium, and the Middle English Ladder of four rungs (MS Douce 322). Unlocks: would test the Cloud's chapter 35 reference. Links: carthusian-life--the-english-mystics-and-devout. Eras: era 5.
- Hiram Edson's manuscript account of 23 October 1844. Unlocks: would test the Edson account of the 1844 disappointment. Links: no link id. Eras: era 9 part 1.
- J. R. Graves and J. M. Pendleton, An Old Landmark Re-set (1854). Unlocks: would test the Landmark succession teaching. Links: no link id. Eras: era 9 part 1.
- John Thomas, Elpis Israel (London, 1849). Unlocks: would test the 1848 date and Thomas's break. Links: no link id. Eras: era 9 part 2.
- Lang, Lives and Legends of the Georgian Saints (1956), or the Martyrdom of Shushanik. Unlocks: would test the husband's apostasy and the date. Links: no link id. Eras: era 3.
- Lerner 1972, read for the exact shape of his conclusion. Unlocks: would test the Lerner conclusion. Links: the-beguines--free-spirit-heresy. Eras: era 5.
- Levison, England and the Continent in the Eighth Century (1946). Unlocks: would test Boniface and the Frankish reform synods. Links: anglo-saxon-christianity--carolingian-reform-christianity. Eras: era 4.
- Luther's letter of 1522 on his Magdeburg year. Unlocks: would test the Brethren-of-the-Common-Life tie. Links: no link id. Eras: era 6.
- Lutheran court records and opinions punishing Anabaptists (Saxon trials 1530; Melanchthon). Unlocks: would test the Lutheran part of the persecution sentence. Links: no link id. Eras: era 7.
- Mateus Cardoso, Kikongo Doutrina Christãa (1624). Unlocks: would test a possible 'influenced' Jesuit link. Links: no link id. Eras: era 7.
- Menze, Justinian and the Making of the Syrian Orthodox Church (2008). Unlocks: would test the Syriac Orthodox link beyond Inferential-Thin. Links: syriac-edessa-nisibis--syriac-orthodox-west-syriac-christianity. Eras: era 1, era 3.
- Modern account of the Herrnhut refugees' origins (Atwood, Community of the Cross). Unlocks: would test the refugee origins before any higher grade. Links: czech-churches-last-century--the-moravian-church-at-herrnhut. Eras: era 8.
- Modern study of how the eight thoughts became Gregory's seven sins. Unlocks: would test the eight-thoughts claim and could raise a link to Widely Accepted. Links: desert-monasticism--roman-church-gregorian. Eras: era 2.
- Modern study of penitentials and the rise of private confession (McNeill and Gamer 1938). Unlocks: would test the confession claim. Links: no link id. Eras: era 3.
- Modern study of the 416 attack on the Bethlehem monasteries. Unlocks: would test the attribution to Pelagius's followers. Links: no link id. Eras: era 2.
- Modern study of the Gothic Homoian church's continuity from Ulfila. Unlocks: would test the 'continued as' link against a consensus reading. Links: no link id. Eras: era 2.
- Modern study of the Pseudo-Isidorian Decretals and their use by the Gregorian reformers. Unlocks: would test the Decretals claim beyond the 1886 polemic. Links: carolingian-reform-christianity--latin-papal-church-gregorian. Eras: era 4.
- Modern study of Valens's church policy. Unlocks: would test the Homoian reading of Valens. Links: homoian-arian-christianity--cappadocian-nicene-pastoral-monastic-tradition. Eras: era 2.
- Modern work comparing Pentecostal Christianity with Montanism. Unlocks: would test the Montanism comparison, if the claim returns. Links: no link id. Eras: era 1.
- Modern work dating the Gospel of the Nativity of Mary (Carolingian abridgement). Unlocks: would test the dating of the Nativity of Mary. Links: no link id. Eras: era 1.
- Modern work on the Codex Argenteus and Theoderic's court. Unlocks: would test the Codex Argenteus attribution. Links: no link id. Eras: era 2.
- Modern work on the origin of the Testaments of the Twelve Patriarchs. Unlocks: would test the Jewish or Christian origin claim. Links: no link id. Eras: era 1.
- Moody Bible Institute founding records (1886) and early curricula (1886-1900); Emma Dryer's letters. Unlocks: would test the Bible-institute founding claim. Links: plymouth-brethren-and-dispensational-formation--the-sunday-school-and-bible-institute-movement. Eras: era 9 part 1.
- Munro-Hay (1991), Phillipson (2012) and Welsby (2002), read and cited by page. Unlocks: would test the 'continued as' links from Aksum and Nubia. Links: no link id. Eras: era 3.
- Nikephoros the Monk, On Sobriety, placed on Athos in the thirteenth century. Unlocks: would test the Athonite date of Nikephoros. Links: athonite-and-comnenian-byzantine-monasticism--hesychasm-and-the-palamite-synthesis. Eras: era 5.
- Otkrovennye rasskazy (The Way of a Pilgrim), Kazan 1881. Unlocks: would test its use of the Philokalia. Links: no link id. Eras: era 8.
- Papal or curial response to the Scottish Parliament's act of August 1560. Unlocks: would test a 'broke with' description for the Kirk and Rome. Links: no link id. Eras: era 7.
- Peter of Sicily, Historia Manichaeorum, and Photius, Contra Manichaeos. Unlocks: would test the polemic on the Paulicians and the planned mission to Bulgaria. Links: byzantine-imperial-church-heraclian-iconoclast--paulicians, byzantine-imperial-church-macedonian--paulicians, paulicians--bogomils. Eras: era 4, major links era 4.
- Printed source on Kyiv academy graduates in the Russian episcopate, 1650-1750. Unlocks: would test 'supplied Russia with its educated clergy'. Links: the-kyiv-mohyla-orthodox-revival--russian-church-nikon-to-holy-synod. Eras: era 7.
- Printers of Hendrik Niclaes's books (Plantin correspondence, Familist imprints). Unlocks: would test the 'Dutch printers' claim. Links: no link id. Eras: era 7.
- Proceedings of the Southern Baptist Convention (Augusta, 1845). Unlocks: would test the slavery cause of the split. Links: no link id. Eras: era 9 part 1.
- Public-domain modern study arguing against a Lollard contribution to the English Reformation. Unlocks: would test the disagreement on both sides. Links: lollardy--the-english-reformation-and-elizabethan-settleme. Eras: era 6.
- Public-domain study of the Ambrosian rite's origins (Duchesne, Christian Worship). Unlocks: would test which parts of the rite go back to Ambrose. Links: no link id. Eras: era 7.
- Rapp, Studies in Medieval Georgian Historiography (2003). Unlocks: would test the Georgian historiography claim. Links: georgian-revival-tao-klarjeti--the-georgian-golden-age. Eras: era 4.
- Rapp, The Sasanian World through Georgian Eyes (2014). Unlocks: would test the 609-780 gap. Links: georgian-christianity--georgian-revival-tao-klarjeti. Eras: era 3.
- Raymond Kévorkian (2011), read and cited by page. Unlocks: would test the fate of the Patriarchate of Constantinople in 1915. Links: armenian-christianity-zartonk--the-armenian-church-after-the-genocide-medz-yegh. Eras: era 9 part 2.
- Record of the 1890-91 Niger crisis and the Lagos 'African Church' secessions of 1891. Unlocks: would test the claimed reaction to the Niger crisis. Links: the-missionary-movement-s-native-churches-seramp--african-initiated-churches-harrist-aladura-zioni. Eras: era 9 part 1.
- Repo-cited modern study of the English mission to Scandinavia. Unlocks: would test the English mission claim (none found). Links: late-anglo-saxon-christianity--scandinavian-conversion-christianity. Eras: era 4.
- Repo-cited modern study of the Latin patriarchate of Constantinople. Unlocks: would test the consensus reading against Mouravieff. Links: latin-papal-church-gregorian--byzantine-church-after-1054--2. Eras: era 5.
- Repo-cited modern study of the tenth-century English Benedictine reform. Unlocks: would test the reform claim (none found). Links: early-benedictine-italian-monasticism--late-anglo-saxon-christianity. Eras: era 4.
- Repo-cited secondary on the Georgian lectionary and Jerusalem worship. Unlocks: would test the Georgian lectionary link. Links: jerusalem-liturgical-pilgrimage-christianity--georgian-christianity. Eras: era 3.
- Repo-cited study on the Rule of the Master's priority over the Rule of Benedict. Unlocks: would test the priority claim. Links: no link id. Eras: era 3.
- Repo-cited work on the Bogomil-Cathar question (Sennis, ed., Cathars in Question, 2016). Unlocks: would test both sides of the Bogomil-Cathar dispute. Links: balkan-bogomil-continuation--cathars-albigensians. Eras: era 5.
- Repo-cited work on the reception of William of Tyre's history. Unlocks: would test the Outremer legacy line. Links: no link id. Eras: era 5.
- Robert Raikes's Gloucester Journal notice (1783) and Arminian Magazine letter (1785). Unlocks: would test the 1780 start and the four women teachers. Links: no link id. Eras: era 9 part 1.
- Rosemary Moore, The Light in Their Consciences (2000). Unlocks: would test the modern reading before the note adds it. Links: puritanism--the-quakers-religious-society-of-friends. Eras: era 8.
- Rosenwein, Rhinoceros Bound (1982), or a modern study of Cluny's origins. Unlocks: would test whether Cluny's origins can be graded Widely Accepted. Links: carolingian-reform-christianity--cluniac-reform-monasticism, cluniac-reform-monasticism--latin-papal-church-gregorian. Eras: era 4.
- Sarah Edwards's narrative as first printed (1742) and the Watts passages. Unlocks: would check the Watts passages against the 1742 text. Links: english-old-dissent--the-evangelical-awakening-in-new-england. Eras: era 8.
- Sebastian Moll, The Arch-Heretic Marcion (2010), on the 144 arrival or expulsion. Unlocks: would test the Marcion arrival-versus-expulsion argument. Links: no link id. Eras: era 1.
- Secondary on Victorinus's reception by Tyconius and Augustine. Unlocks: would test the reception claim (none yet found). Links: no link id. Eras: era 1.
- Secondary work stating the Nisibis-to-Persian-church continuity directly. Unlocks: would test the Nisibis-to-Persia continuity. Links: syriac-edessa-nisibis--persian-church-of-the-east-early. Eras: era 1.
- Seventh- or eighth-century text on the Aksumite church's clergy after 615. Unlocks: would test the post-615 Aksumite claim. Links: aksumite-christianity--post-aksumite-ethiopian-christianity. Eras: era 3.
- Shimun line text before 1600 and Giamil, Genuinae relationes (1902). Unlocks: would test the Roman documents for the Shimun line. Links: no link id. Eras: era 7.
- Source for Egeria's date in the early 380s beyond the editors' argument. Unlocks: would test the date of Egeria's travels. Links: no link id. Eras: era 2.
- Source for Euthymius of Tarnovo's exile (1393) and the Bulgarian church after Tarnovo. Unlocks: would test the Tarnovo summary. Links: no link id. Eras: era 7.
- Source for St Thomas Christians' privileges from Hindu rulers in 1300-1517. Unlocks: would test the privileges sentence. Links: no link id. Eras: era 6.
- Source for the restoration of the Serbian Patriarchate of Pec in 1557. Unlocks: would test the Ottoman Orthodoxy summary. Links: no link id. Eras: era 7.
- Source on later Byzantine-rite unions (Uzhhorod 1646) modeled on Brest. Unlocks: would test the modeled-on-Brest claim. Links: no link id. Eras: era 7.
- Source on the Inquisition and John of the Cross in his lifetime. Unlocks: would test the Inquisition claim. Links: no link id. Eras: era 7.
- Studite Hypotyposis (rule) itself. Unlocks: would tie the Kyiv rule to Theodore's house. Links: iconophile-byzantine-monasticism--kievan-rus-christianity-1054-1240. Eras: era 5.
- Syriac text of the 1301 Cranganore colophon (Vat. Syr. 22). Unlocks: would test Mingana's 'Yahb Alaha V.' numbering against Yahballaha III. Links: church-of-the-east-under-the-mongols--st-thomas-christians-1300-1517. Eras: era 6.
- Tarisappalli (Kollam) copper plates in an edition and translation, with the c. 849 dating. Unlocks: would test the dating of the bishop's grant. Links: church-of-the-east-under-the-abbasids--st-thomas-christians-of-india. Eras: era 4.
- Text giving Novel 42's date in its own words. Unlocks: would test the year 536 for Novel 42. Links: byzantine-imperial-church-justinianic--syriac-orthodox-west-syriac-christianity--2. Eras: era 3.
- Text naming a bishop of Aksum or Ethiopia between 615 and 900. Unlocks: would test the Aksumite see on the later side. Links: aksumite-christianity--post-aksumite-ethiopian-christianity. Eras: era 4.
- Text of 451-615 naming a bishop of Aksum consecrated by Alexandria. Unlocks: would test the Aksumite consecration claim. Links: aksumite-christianity--cyrilline-miaphysite-egyptian-christianity. Eras: era 3.
- Text tracing the London French Prophets' circle from the Camisard exiles (1706-1730s). Unlocks: would test whether this woman belonged to the circle. Links: camisard-prophetism--the-methodist-revival. Eras: era 8.
- Theodore Abu Qurrah's works, in translation. Unlocks: would test the mixed-audience claim and the Mar Saba link. Links: chalcedonian-monasticism-judean-desert-and-gaza--melkite-arabic-christianity. Eras: era 4.
- Theophanes, Chronographia AM 6214, on Montanist survival into the eighth century. Unlocks: would test the claim that Montanism survived to the eighth century. Links: no link id. Eras: era 1.
- Uniform Lesson records (1872). Unlocks: would test the Sunday-school lesson claim. Links: no link id. Eras: era 9 part 1.
- Vendored Ibn Ishaq account of the first Muslim emigration to Aksum. Unlocks: would restore the 615 sentence as fact. Links: no link id. Eras: era 3.
- Vendored text or study on the Macedonius attribution. Unlocks: would test the attribution. Links: no link id. Eras: era 2.
- Vendored text placing Georgian monks on Sinai and at the Black Mountain before 1000. Unlocks: would test the pre-1000 Georgian presence. Links: no link id. Eras: era 4.
- Vendored text tying the Kerala Christians of 849-1054 to the Persian church. Unlocks: would test the Kerala link before 651. Links: the-church-of-the-east-under-persia--st-thomas-christians-of-india. Eras: era 3.
- W. H. Summers, The Lollards of the Chiltern Hills (1906); Strype. Unlocks: would test shared families between Lollards and early evangelicals. Links: lollardy--the-english-reformation-and-elizabethan-settleme. Eras: era 6.
- W. T. Stead, The Revival in the West (1905); Western Mail reports 1904-05. Unlocks: would test the Welsh revival's tie to 1735-1815. Links: no link id. Eras: era 8.
- Whitney R. Cross, The Burned-over District (1950). Unlocks: would test the classic reading of the Millerite link. Links: the-second-great-awakening-and-camp-meeting-worl--restorationist-apocalyptic-ferment-and-adventism. Eras: era 9 part 1.

### Would test a major-link outcome (33)

- 1255 Anagni protocol or Alexander IV's condemnation of the Introductorius. Unlocks: would test the Joachite condemnation link. Links: no link id. Eras: major links era 5.
- A text of the African councils of 416 and 418, or Zosimus's letter, condemning Pelagius. Unlocks: would test the Augustine-Pelagius lines. Links: no link id. Eras: major links era 1.
- Acts of the Council of Aquileia (381), with its sentence on Palladius. Unlocks: would test the Ambrose line on Palladius. Links: no link id. Eras: major links era 2.
- Acts of the Lateran synod of 649 condemning Paul of Constantinople. Unlocks: would test the African link to Paul. Links: no link id. Eras: major links era 3.
- Anna Komnene, Alexiad 15, on the trial and burning of Basil the Bogomil. Unlocks: would test the Bogomil trial in the major link. Links: no link id. Eras: major links era 5.
- Bernard Gui, Liber sententiarum (sentences against Cathars). Unlocks: would test the Dominican-Cathar link. Links: no link id. Eras: major links era 5.
- Cluny's foundation charter (910) and the Carolingian reform. Unlocks: would test whether Cluny took the Rule through the Carolingian reform. Links: no link id. Eras: major links era 4.
- Cluny's own customaries showing Cluny living by the Rule of Benedict. Unlocks: would test the Cluny-Benedict claim. Links: no link id. Eras: major links era 3.
- Confessions IX.6 or Paulinus's Life of Ambrose naming Ambrose as Augustine's baptizer. Unlocks: would test the Ambrose-Augustine link. Links: no link id. Eras: major links era 1.
- Cosmas the Priest, Sermon against the Bogomils; Interrogatio Iohannis. Unlocks: would test what passed from Paulicians to Bogomils to Cathars. Links: no link id. Eras: major links era 4.
- Dated text of the Armenian custom of consecration at Caesarea, independent of Moses of Khoren. Unlocks: would test the Caesarea consecration custom. Links: no link id. Eras: major links era 2.
- Early Cistercian foundation texts on keeping the Rule of Benedict. Unlocks: would test the Cistercian Rule claim. Links: no link id. Eras: major links era 3.
- Eusebius, Church History VII.30.19 on Aurelian's ruling for the church house at Antioch. Unlocks: would test the Antioch church-house claim. Links: no link id. Eras: major links era 1.
- Gratian's Decretum or a later canon collection taking the False Decretals into church law. Unlocks: would test the Decretals' reception. Links: no link id. Eras: major links era 4.
- Innocent III's bull Quia divinae sapientiae (1216) to the Maronites. Unlocks: would test the Maronite union link. Links: no link id. Eras: major links era 5.
- Justinian's edict against Origen (543) or the anathemas of 553. Unlocks: would test the Jerome, Methodius and Coptic lines against Origen. Links: no link id. Eras: major links era 1.
- Law against the Manichaeans (Diocletian's rescript; Theodosian Code XVI.5). Unlocks: would test the Ephraim and Augustine lines against Mani. Links: no link id. Eras: major links era 1.
- Lucius III, Ad abolendam (1184), naming the Humiliati and Poor of Lyon. Unlocks: would test the Humiliati condemnation link. Links: no link id. Eras: major links era 5.
- Paterik of the Kyiv Caves on Anthony and Athos. Unlocks: would test the Athonite origin of Anthony. Links: no link id. Eras: major links era 5.
- Peter of Sicily's History of the Paulicians and Anna Comnena's Alexiad on the Paulician settlers at Philippopolis. Unlocks: would test the Philippopolis settlement. Links: no link id. Eras: major links era 4.
- Primary for Kievan Rus' adopting Slavonic letters and books. Unlocks: would test the Slavonic books claim in the major link. Links: no link id. Eras: major links era 4.
- Primary Georgian witness (Life of John and Euthymius) for the Iviron translators. Unlocks: would test the Iviron translators link. Links: no link id. Eras: major links era 5.
- Source for what Paul and Macarius's mission to Africa (347) imposed on the Donatists. Unlocks: would test the 347 mission claim. Links: no link id. Eras: major links era 2.
- Source showing Caesarius of Arles's Rule drawing on Lérins practice. Unlocks: would test the Lérins line in the major link. Links: no link id. Eras: major links era 2.
- Synodikon of Orthodoxy (843), to test the iconophile feast in the Macedonian-era church. Unlocks: would test the Macedonian-era claim. Links: no link id. Eras: major links era 4.
- Syriac or Greek source naming the Philocalia's compilers. Unlocks: would test the Philocalia's compilers beyond the NPNF prolegomena. Links: no link id. Eras: major links era 1.
- Text recording the result of Pope Gregory's ordered council on the Donatists in Numidia. Unlocks: would test the Donatist council claim. Links: no link id. Eras: major links era 2.
- Text showing the Merovingian church adopting Hilary's teaching or practice. Unlocks: would test the Hilary claim beyond praise. Links: no link id. Eras: major links era 2.
- Theophanes' Chronicle on the Paulicians under Michael I (811-813). Unlocks: would test the persecution claim. Links: no link id. Eras: major links era 4.
- Typikon of Athanasius for the Great Lavra; Athonite foundation acts. Unlocks: would test imperial founding of Athonite houses. Links: no link id. Eras: major links era 4.
- Vendored Movses Dasxuranci (Dowsett) for the removal of Nerses Bakur. Unlocks: would test the Nerses Bakur removal. Links: no link id. Eras: major links era 3.
- Vendored Sweet's edition of Alfred's preface to the Pastoral Care. Unlocks: would test the Alfred link in the major link. Links: no link id. Eras: major links era 3.
- Verdict of Marcellinus after the 411 Carthage conference, or the Theodosian Code laws against the Donatists. Unlocks: would test the Donatist lines in the major link. Links: no link id. Eras: major links era 1.

### Would support a movement's prose (38)

- Byron's letters of 1816-17 on his study at San Lazzaro. Unlocks: would support the Armenian legacy's stated fact. Links: no link id. Eras: era 8.
- Calvin's preface to the French Chrysostom homilies (Calvini Opera 9). Unlocks: would support the expository-preaching sentence in the Reformed-cities prose. Links: antiochene-exegetical-christianity-chrysostom-ce--the-reformed-cities-zurich-and-geneva. Eras: era 2.
- Central African Christians among the enslaved in the Americas (seventeenth century). Unlocks: would support the Atlantic claim in the legacy. Links: no link id. Eras: era 7.
- Church of England's Common Worship calendar. Unlocks: would settle the Julian commemoration. Links: no link id. Eras: era 6.
- Conybeare, The Key of Truth (1898). Unlocks: would support the Paulician legacy sentence. Links: no link id. Eras: era 4.
- Dante, Paradiso 12 (Joachim). Unlocks: would support the Joachim sentence. Links: no link id. Eras: era 5.
- Euthymius of Tarnovo's writings or Slavonic translations of hesychast texts. Unlocks: would restore the 'traveled north to Russia' sentence. Links: no link id. Eras: era 5.
- George MacLeod's writings or Ferguson 1988 on the Iona Community's claim on Columba. Unlocks: would support the movement's prose on Columba. Links: insular-irish-monastic-christianity--ecumenical-community-worlds-taize-and-iona. Eras: era 3.
- Hauge's own writings (Betragtning over Verdens Daarlighed, 1796; Testament, 1821). Unlocks: would support the Pietist-forebears prose if the sentence is restored. Links: german-pietism-spener-francke-halle--the-haugean-awakening. Eras: era 9 part 1.
- José Burgos, Manifiesto (1864), or another Filipino secular clergy text. Unlocks: would show the era-8 to era-9 continuity in the clergy's words. Links: philippine-catholicism-era-8--philippine-catholicism-gomburza-to-aglipay. Eras: era 8.
- José Rizal, El Filibusterismo (1891), dedication to Gómez, Burgos and Zamora. Unlocks: would support the Filipino clergy prose. Links: no link id. Eras: era 9 part 2.
- Kallistos's Life of Gregory of Sinai (Pomjalovskij 1894). Unlocks: would restore the hesychast sentences of the Serbian and Bulgarian entry. Links: no link id. Eras: era 5.
- Laestadius's sermons (postillas) and Ens Ropandes Röst i Öknen (1852-54). Unlocks: would support the Pietist-writers sentence. Links: german-pietism-spener-francke-halle--laestadianism-and-the-nordic-revivals. Eras: era 9 part 1.
- Luther's letter to Spalatin, February 1520 ('we are all Hussites'). Unlocks: would support the Hussite-Luther line in the prose. Links: the-hussite-and-bohemian-brethren-movement--lutheran-wittenberg-and-its-congregations. Eras: era 6.
- Luther's preface to Romans (1522) set against Tyndale's Prologue. Unlocks: would support the prose comparing the two prefaces. Links: no link id. Eras: era 7.
- Milton, Sonnet 18, 'On the Late Massacre in Piedmont' (1655). Unlocks: would support the Piedmont prose. Links: no link id. Eras: era 7.
- Modern work on the Gothic Bible as the earliest substantial Germanic text. Unlocks: would support the Gothic Bible sentence. Links: no link id. Eras: era 2.
- Modern work on the reception of Basil's argument from prayer and of Gregory's 'what is not assumed'. Unlocks: would support two legacy claims. Links: no link id. Eras: era 2.
- Modern work on the Vulgate's reception and Hebrew principle. Unlocks: would support the 'back-to-the-sources' claim if it returns. Links: no link id. Eras: era 2.
- Moravian mission-scale claims ('more missionaries in twenty years'). Unlocks: would support the comparative mission sentence. Links: no link id. Eras: era 8.
- Reception of the Spiritual Exercises among Protestants; Teresa and John among Protestant readers. Unlocks: would support the legacy line on reception. Links: no link id. Eras: era 7.
- Records of French refugee churches (London, Berlin, Amsterdam, Cape Town, Charleston). Unlocks: would support the Huguenot legacy. Links: no link id. Eras: era 7.
- Relief Acts 1778-1829, hierarchy of 1850, canonization of 1970. Unlocks: would support the return of English Catholicism sentence. Links: no link id. Eras: era 7.
- Repo-cited source on Renaissance humanists' use of Carolingian minuscule and cathedral schools. Unlocks: would support two legacy lines. Links: no link id. Eras: era 4.
- Repo-cited source on the Protestant orders of St John and St John Ambulance. Unlocks: would support the legacy line. Links: no link id. Eras: era 5.
- Repo-cited work on the Typikon of Saint Sabas in later Orthodox worship. Unlocks: would support the legacy claim. Links: no link id. Eras: era 3.
- Source for Lérins as a monastery today and Martin as patron saint of France. Unlocks: would support two legacy lines. Links: no link id. Eras: era 2.
- Source for the epithet 'Queen of Translations' for the Armenian Bible. Unlocks: would support the Armenian Bible sentence. Links: no link id. Eras: era 2.
- Source for the Ethiopian church's own patriarchate in 1959. Unlocks: would keep the post-Aksumite closing sentence sourced. Links: no link id. Eras: era 2, era 4.
- Source for the Florensian order's merger into the Cistercians (1570). Unlocks: would support the Florensian legacy clause. Links: no link id. Eras: era 5.
- Source for the Waldensian Church's union with the Italian Methodists (1975-1979). Unlocks: would support the Waldensian legacy clause. Links: no link id. Eras: era 5.
- Source on Cardinal Cisneros endowing the Mozarabic chapel at Toledo. Unlocks: would support the Mozarabic sentence. Links: no link id. Eras: era 4.
- Source showing the 1960s-1990s base communities drawing on colonial popular piety (Cardenal, Solentiname). Unlocks: would support the base-community prose. Links: no link id. Eras: era 8.
- Text of John Paul II's Athens address (4 May 2001) on the sack of 1204. Unlocks: would settle the wording of the apology sentence. Links: no link id. Eras: era 5.
- The Way of a Pilgrim, public-domain edition. Unlocks: would support the hesychasm legacy line. Links: no link id. Eras: era 6.
- Thomas Aquinas on grace (Summa I-II, qq. 109-114). Unlocks: would keep the Pelagian legacy sentence's citation. Links: no link id. Eras: era 2.
- Vendored source for the Treaty of Paris (1229) or the crown's annexation of Languedoc. Unlocks: would support the Cathar legacy sentence. Links: no link id. Eras: era 5.
- Wichern's Denkschrift on the Inner Mission (1849); Merle d'Aubigné and Malan texts. Unlocks: would support the awakening's Pietist forebears prose. Links: german-pietism-spener-francke-halle--the-reveil-and-inner-mission-awakening. Eras: era 9 part 1.

### Other (7)

- Bar Hebraeus, Chronography (Budge 1932): the Mongol queens and the Kerait. Unlocks: Other: Mongol-court detail. Links: no link id. Eras: era 5.
- Bonn Agreement of 1931 (text). Unlocks: Other: falls after both movements' dates. Links: old-catholic-churches-union-of-utrecht--victorian-church-of-england. Eras: era 9 part 2.
- Dostoevsky, The Brothers Karamazov (1880; Garnett 1912). Unlocks: Other: monastic world in the novel. Links: no link id. Eras: era 8.
- Golden Legend or other medieval text on reception of apocryphal Acts, Dormition narratives and Revelation of Paul. Unlocks: Other: reception of apocrypha, not a stated claim. Links: no link id. Eras: era 1.
- Melnikov-Pechersky, V lesakh and Na gorakh. Unlocks: Other: Old Believers in the novel. Links: no link id. Eras: era 8.
- Source for the dispute over the Kyiv Pechersk Lavra. Unlocks: Other: recent dispute, not a stated claim. Links: no link id. Eras: era 5.
- Waldensian Church in Argentina and Uruguay; 1979 Waldensian-Methodist union. Unlocks: Other: out of window, not a stated claim. Links: no link id. Eras: era 7.

### Already vendored under cic/texts/ (met)

Dropped from the main list. Each named work is vendored under cic/texts/ in the edition the want names, or the want only asks to locate and quote a vendored text. Partial matches stay in the main list with a note.

- Annales Bertiniani entries naming Anskar and Hamburg. prudentius-troyes_annales-bertiniani_waitz1883.txt (Waitz 1883) is vendored; locate and quote only. Links: carolingian-reform-christianity--scandinavian-conversion-christianity. Eras: era 4.
- Michael the Syrian, Chronicle book X, on the Peter of Callinicus-Damian schism and the 616 reunion. michael-the-syrian_chronique-tome2-livres-viii-xi (Chabot 1901, books VIII-XI) is vendored; book X is covered. Links: cyrilline-miaphysite-egyptian-christianity--syriac-orthodox-west-syriac-christianity. Eras: era 3.
- Wesley's Queries humbly proposed to Count Zinzendorf (1755). wesley-j_queries-humbly-proposed-to-count-zinzendorf_1755.txt is vendored. Links: the-moravian-church-at-herrnhut--the-methodist-revival. Eras: era 8.
- Paris synod letter c. 360 (Hilary, Collectanea antiariana A I). hilary_collectanea-antiariana-parisina (Feder 1916, CSEL 65) is vendored; locate and quote only. Links: no link id. Eras: era 2.
- Alcuin's letters to Higbald and to King Æthelred on the raid. alcuin_opera-omnia-letters_migne-pl100-101 is vendored; locate and quote only. Links: anglo-saxon-christianity--late-anglo-saxon-christianity. Eras: era 4.
- Life of a Scetis abbot, or Zachariah Rhetor, on Egyptian monks' refusal of Chalcedon (451-642). zachariah-rhetor_chronicle_hamiltonbrooks1899.txt is vendored; the reading remains. Links: desert-monasticism--cyrilline-miaphysite-egyptian-christianity. Eras: era 3.
- Armenian councils of Sis (1307) and Adana (1316), Mansi 25. Mansi 25 (vendored) holds the Sis and Adana councils; this is a citation, not an acquisition. Links: latin-papal-church-avignon-to-lateran-v--armenian-cilicia-after-the-kingdom. Eras: era 6.
- Allen, Life, Experience and Gospel Labors (1880). allen-richard_life-experience-and-gospel-labors_1880.txt is vendored; this is a README-only item for the African Methodist break. Links: no link id. Eras: era 9 part 1.
- Declaration of Utrecht 1889 (Mirbt no. 588). Vendored in mirbt_quellen (Mirbt no. 588); the Döllinger letter of 1871 and the 1871 excommunication decree remain wanted (kept in the main list). Links: no link id. Eras: era 9 part 2.
- Cite canon 2 of the 585 synod (lines 26710-26718 of its vendored file). Vendored; a citation to add to the re-judgement, not a text to acquire. Links: no link id. Eras: major links.
