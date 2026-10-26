#!/usr/bin/env python3
"""Build the two worklists from the sixteen coverage reports (C1 to C16).
Read-only against the repo; writes only into this folder."""
import os, json, collections

REPO = '/home/user/CIC-Project'
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- vendored file short names -> paths under cic/texts ----------
T = {
 'anf01': 'anf01_apostolic-fathers-justin-irenaeus.xml',
 'anf02': 'anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml',
 'anf03': 'anf03_tertullian.xml',
 'anf04': 'anf04_tertullian4-minucius-felix-commodian-origen1-2.xml',
 'anf05': 'anf05_hippolytus-cyprian-caius-novatian.xml',
 'anf06': 'anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml',
 'anf07': 'anf07_lactantius-apostolic-constitutions-didache-liturgies.xml',
 'anf08': 'anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml',
 'anf09': 'anf09_gospel-of-peter-diatessaron-origen-commentaries.xml',
 'npnf101': 'npnf101_augustine-confessions-letters.xml',
 'npnf102': 'npnf102_augustine-city-of-god-christian-doctrine.xml',
 'npnf103': 'npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml',
 'npnf104': 'npnf104_augustine-anti-manichaean-anti-donatist.xml',
 'npnf105': 'npnf105_augustine-anti-pelagian-writings.xml',
 'npnf106': 'npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml',
 'npnf107': 'npnf107_augustine-homilies-john-soliloquies.xml',
 'npnf108': 'npnf108_augustine-exposition-psalms.xml',
 'npnf109': 'npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml',
 'npnf201': 'npnf201_eusebius-church-history-life-of-constantine.xml',
 'npnf203': 'npnf203_theodoret-jerome-gennadius-rufinus.xml',
 'npnf204': 'npnf204_athanasius-select-works-letters.xml',
 'npnf205': 'npnf205_gregory-nyssa-dogmatic-treatises.txt',
 'npnf206': 'npnf206_jerome-principal-works.xml',
 'npnf207': 'npnf207_cyril-jerusalem-gregory-nazianzen.xml',
 'npnf208': 'npnf208_basil-letters-select-works.xml',
 'npnf209': 'npnf209_hilary-poitiers-john-damascus.xml',
 'npnf210': 'npnf210_ambrose-select-works-letters.xml',
 'npnf211': 'npnf211_sulpitius-severus-vincent-lerins-cassian.xml',
 'npnf212': 'npnf212_leo-great-gregory-great.xml',
 'npnf213': 'npnf213_gregory-great-ephraim-syrus-aphrahat.xml',
 'npnf214': 'npnf214_seven-ecumenical-councils.xml',
 'philocalia': 'origen_philocalia_lewis1911.txt',
 'basil-rules': 'basil_ascetic-works-longer-shorter-rules_clarke1925.txt',
 'macarius': 'macarius_fifty-spiritual-homilies_mason1921.txt',
 'budge2': 'anan-isho_paradise-v2-sayings_budge1907.txt',
 'salvian': 'salvian_on-the-government-of-god_sanford1930.txt',
 'optatus': 'optatus_against-the-donatists.txt',
 'pl11': 'pl11-zeno-optatus-collatio-carthaginiensis_migne.txt',
 'pl8': 'monumenta-vetera-donatistarum_migne-pl8.txt',
 'calvin1': 'calvin_institutes-christian-religion-vol1_beveridge1845.txt',
 'calvin2': 'calvin_institutes-christian-religion-vol2_beveridge1845.txt',
 'calvin3': 'calvin_institutes-christian-religion-vol3_beveridge1845.txt',
 'geneva-cat': 'calvin_geneva-catechism_waterman1815.txt',
 'calvin-gen2': 'calvin_commentaries-genesis-vol2_king1847.txt',
 'calvin-opera8': 'calvin_opera-omnia-vol8-lat-fra_baum-cunitz1870.txt',
 'bonnet1': 'calvin_letters-vol1_bonnet1858.txt',
 'bonnet2': 'calvin_letters-vol2_bonnet1858.txt',
 'bonnet4': 'calvin_letters-vol4_bonnet1858.txt',
 'zwingli3': 'zwingli_latin-works-correspondence-vol3_heller1929.txt',
 'zwingli-sel': 'zwingli_selected-works_jackson1901.txt',
 'schaff-helv': 'schaff_second-helvetic-confession-heidelberg-catechism_1919.txt',
 'ordonnances': 'calvin-geneva-council_ordonnances-ecclesiastiques-fra_tournes1735.txt',
 'beza-job': 'beza_job-expounded_legatt1589.txt',
 'rilliet': 'rilliet_calvin-and-servetus_tweedie1846.txt',
 'ac': 'melanchthon_augsburg-confession_anon-pg275.txt',
 'apology': 'melanchthon_apology-augsburg-confession_bente-dau1921.txt',
 'boc': 'book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt',
 'luther-v1': 'luther_works-v1-selected_jacobs-spaeth1915.txt',
 'luther-v2': 'luther_works-v2-selected_jacobs-spaeth1916.txt',
 'luther-v3': 'luther_works-v3-selected_various1930.txt',
 'table-talk': 'luther_table-talk_bell1886.txt',
 'luther-hymns': 'luther_hymns_bacon-allen.txt',
 'large-cat': 'luther_large-catechism_bente-dau1921.txt',
 'bondage': 'luther_bondage-of-the-will_cole1823.txt',
 'hallock': 'aphrahat_demonstrations-2-7_hallock1932.txt',
 'ephrem-prose': 'ephraim_prose-refutations_mitchell1912-1921.txt',
 'harris-odes': 'harris_odes-and-psalms-of-solomon_harris1911.txt',
 'lausiac': 'palladius_lausiac-history_clarke1918.txt',
 'pall-dial': 'palladius_dialogue-life-of-chrysostom_moore1921.txt',
 'evagrius': 'evagrius_praktikos_dysinger.txt',
 'hefele2': 'hefele_history-of-the-councils-v2-326-429_oxenham1876.txt',
 'cyprian-ep-lat': 'cyprian_epistulae-lat_hartel1871-csel3-tei.txt',
 'cyprian-mort-lat': 'cyprian_de-mortalitate-lat_hartel1868-csel3-tei.txt',
 'aug-sermones-lat': 'augustine_sermones-1-340-lat_migne-pl38.txt',
 'aug-fide-op': 'augustine_de-fide-et-operibus-lat_zycha1900-csel41-tei.txt',
 'aug-pl40': 'augustine_opera-minora-catechetica-lat_migne-pl40.txt',
 'aug-csel57': 'augustine_epistulae-critical_goldbacher-csel57-pars4.txt',
 'pelagius-dem': 'pelagius_epistula-ad-demetriadem-lat_migne.txt',
 'faustus': 'faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt',
 'athan-pg26': 'athanasius_opera-omnia-pg26-grc-lat_migne1857.txt',
 'origen-orat': 'origen_de-oratione-grc_koetschau1899.txt',
 'naz-pg37': 'gregory-nazianzen_epistulae-carmina-pg37-grc-lat_migne1857.txt',
 'chrys-pg47': 'john-chrysostom_opera-pg47-palladius-dialogus-grc-lat_migne1863.txt',
 'chrys-pg52': 'john-chrysostom_opera-pg52-epistulae-grc-lat_migne1862.txt',
 'codex-theod': 'codex-theodosianus_latinlibrary.txt',
 'possidius': 'possidius_vita-augustini_weiskotten1919.txt',
 'tacitus': 'tacitus_annals-15-44_church-brodribb1876.txt',
 'lucian': 'lucian_works-vol4-peregrine_fowler1905.txt',
 'addai': 'addai_doctrine-of-addai.txt',
 'amphilochius-src': None,  # record, not a text
 'greg-dial': 'gregory-great_dialogues_gardner1911.txt',
 'hus-eccl': 'hus_de-ecclesia-the-church_schaff1915.txt',
 'xavier2': 'francis-xavier_life-and-letters-v2_coleridge1872.txt',
 'ignatius-ex': 'ignatius-loyola_spiritual-exercises_mullan1914.txt',
 'avvakum': 'avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt',
 'npnf112': 'npnf112_chrysostom-homilies-corinthians.xml',
 'trent': 'council-of-trent_canons-and-decrees_waterworth1848.txt',
 'wesley-c1780': 'wesley-c_hymns-methodists_1780.txt',
 'pachomius': 'pachomius_rules-ethiopic_schodde1885.txt',
 'eucherius': 'eucherius-lyon_de-contemptu-mundi_vaughan1654.txt',
}
def P(short):
    if short is None: return None
    if short in T: return 'cic/texts/' + T[short] if T[short] else None
    return short  # already a repo-relative path

def exists(rel):
    return rel is not None and os.path.exists(os.path.join(REPO, rel))

# =====================================================================
# 1. ACQUISITION WORKLIST
# =====================================================================
# cells: list of "world:Cn/Sm". priority = len(set(cells)).
A = []
def acq(work, author, edition, hosted, licence, cells, unlocks_note='', english_copyright=False,
        identified_as=None, notes='', only_original_pd=False):
    A.append(dict(work=work, author=author, edition=edition, hosted=hosted, licence=licence,
                  english_in_copyright=english_copyright, identified_as=identified_as or [],
                  cells=sorted(set(cells)), notes=notes))

# ---- C1 ----
acq('Antiquities XVIII.3.3 and XX.9.1 (the Testimonium and the James passage)', 'Josephus',
    'trans. William Whiston (1737)', 'Project Gutenberg #2848; Perseus', 'public domain',
    ['alx:C1/S5', 'pahc:C1/S5'],
    notes="C1 fleet hole 1: 'did he really exist' retrieves in no world; Josephus is not vendored in his own right and reaches the worlds only through Eusebius HE I.11 (alx, ijc, pahc, syr) and Jerome De viris 13 (seven worlds). Serves any world asked C1-08/C1-16.")
acq('Muratorian fragment', 'anon. (2nd c.)', "B.F. Westcott, A General Survey of the History of the Canon of the New Testament (Macmillan 1875), appendix C", 'archive.org', 'public domain',
    ['pahc:C1/S7'])
acq('Evangelion da-Mepharreshe: the Curetonian Version of the Four Gospels, with the readings of the Sinai palimpsest (Old Syriac Gospels)', 'ed. F.C. Burkitt',
    'Cambridge 1904', 'archive.org', 'public domain', ['syr:C1/S7'])
acq('The Earliest Life of Christ ... the Diatessaron of Tatian', 'J. Hamlyn Hill', 'T&T Clark 1894', 'archive.org', 'public domain',
    ['syr:C1/S7'], notes='anf09 already carries the Arabic harmony (Hill/Hogg) and is cited by syr records; this is the separate 1894 volume.')
acq('The Apocryphal New Testament (Acts of John 88-93; Gospel of Peter; full Ethiopic Apocalypse of Peter pp. 505-524; Apocalypse of Paul / Visio Pauli)', 'M.R. James',
    'Oxford 1924; Latin Visio Pauli also in James, Apocrypha Anecdota, Texts and Studies II.3 (1893)', 'archive.org',
    'public domain in the US since 2020 (1924); UK term expired 2007; 1893 Latin PD',
    ['pahc:C1/S6', 'pahc:C3/S1', 'gallic:C3/S1'],
    notes='Also Grenfell & Hunt, Logia Iesou (1897, PD) for the Oxyrhynchus sayings (C1 other list). anf09 vendors only the Akhmim fragment of the Apocalypse of Peter.')
acq('Harmony of the Evangelists', 'John Calvin', 'trans. William Pringle, Calvin Translation Society 1845-46', 'CCEL', 'public domain', ['rzg:C1/S6'])
acq('Commentary on Galatians (1535), esp. 3:13 (the penal locus)', 'Martin Luther', 'trans. Middleton 1575, rev. 1850', 'CCEL', 'public domain', ['witt:C1/S3'])
acq('Dass Jesus Christus ein geborener Jude sei / That Jesus Christ Was Born a Jew (1523)', 'Martin Luther',
    'German: WA 11; English: LW 45 (1962)', 'archive.org (Weimarer Ausgabe)', 'German public domain; English LW 45 (1962) in copyright',
    ['witt:C1/S2', 'witt:C1/S6'], english_copyright=True, identified_as=['witt.source.luther-that-jesus-christ-was-born (kind: unvendored; WANTS-REGISTER row)'],
    notes="The one text in the fleet whose title answers C1-19; the single IDENTIFIED cell in the C1 table.")
acq('Vorrede auf das Neue Testament / Preface to the New Testament (1522)', 'Martin Luther',
    'German: WA DB 6; English: Works of Martin Luther vol. 6 (Holman 1932)', 'archive.org', 'German public domain; Holman English US-PD only from 2028',
    ['witt:C1/S7'], english_copyright=True, identified_as=['witt.source.luther-das-newe-testament-deutzsch (kind: unvendored)'],
    notes="Ranks John first; the natural text for 'which gospels'.")
acq('On the Deity of the Son and the Spirit', 'Gregory of Nyssa', 'not stated in report', 'not stated in report', 'not stated in report',
    ['cappadocian:C1/S2'], identified_as=['cappadocian.source.gregory-nyssa-on-the-deity-of-the-son-and-spirit (kind: unvendored)'])
acq('Creed (Expositio fidei)', 'Gregory Thaumaturgus', 'not stated in report', 'not stated in report', 'not stated in report',
    ['cappadocian:C1/S2'], identified_as=['cappadocian.source.gregory-thaumaturgus-creed (kind: unvendored)'])
acq('The Bible in Christian North Africa: the Donatist World', 'Maureen Tilley', 'Fortress 1997 (modern monograph)', 'not stated in report', 'in copyright',
    ['don:C1/S7'], english_copyright=True, identified_as=['don.source.tilley-bible-in-christian-north-africa (kind: unvendored, in copyright)'])
acq("Tatian's Diatessaron: Its Creation, Dissemination, Significance, and History in Scholarship", 'William L. Petersen', 'Brill 1994 (modern monograph)', 'not stated in report', 'in copyright',
    ['syr:C1/S5'], english_copyright=True, identified_as=['syr.source.petersen-diatessaron (kind: unvendored, in copyright)'])
acq("Commentary on the Diatessaron", 'Ephrem', 'trans. Carmel McCarthy (1993), named in syr Doc_02', 'not stated in report', 'in copyright',
    ['syr:C1/S7'], english_copyright=True, identified_as=['named in syr Doc_02; no source record cited'])

# ---- C3 ----
acq('Homilies on Jeremiah XVIII-XX (corrective punishment; the fire God lights)', 'Origen',
    'Greek: GCS 6, ed. E. Klostermann (Leipzig 1901); English: Smith, FOTC 97 (1998)', 'archive.org (GCS vol. 6)',
    'public domain (Greek); English not PD', ['alx:C3/S3'], english_copyright=True)
acq('De mortuis oratio (On the Dead): the soul after death and purgation', 'Gregory of Nyssa',
    'Greek: PG 46:497-537 (Migne 1863); no public-domain English', 'archive.org / documentacatholicaomnia', 'public domain (Greek)',
    ['cappadocian:C3/S5'], english_copyright=True)
acq('Apophthegmata Patrum, Latin systematic collection (Verba Seniorum of Pelagius and John), incl. Macarius and the skull of the pagan priest', 'anon.',
    "PL 73 (Migne 1849), Latin; Helen Waddell's 1936 English", 'archive.org (PL 73)', 'public domain (Latin); Waddell 1936 English in copyright',
    ['desert:C3/S1', 'desert:C3/S5'], english_copyright=True,
    notes="The Syriac form is already vendored in Budge's Paradise vol. 2 (anan-isho_paradise-v2-sayings_budge1907.txt line 436 holds the skull-adjacent Macarius story); the famous skull saying itself was not found there by the terms used.")
acq('Letter to Melania; Kephalaia Gnostika (the desert\'s own apokatastasis strand)', 'Evagrius Ponticus',
    'Syriac: W. Frankenberg, Euagrius Ponticus (Berlin 1912); English: Parmentier 1985, Casiday 2006, Ramelli 2015', 'archive.org (Frankenberg 1912)',
    'public domain (Syriac/Greek retroversion); English not PD', ['desert:C3/S3'], english_copyright=True)
acq("Historia Monachorum in Aegypto (Rufinus's Latin)", 'Rufinus (trans.)', 'PL 21 (Migne); English: Russell 1980', 'archive.org',
    'public domain (Latin); Russell 1980 English in copyright', ['desert:C3/S5'], english_copyright=True,
    identified_as=['desert.source.historia-monachorum (kind: unvendored)'])
acq('Liber Regularum (the Donatist Book of Rules; Rule VII on the devil and his body)', 'Tyconius',
    'F.C. Burkitt, Texts and Studies III.1 (Cambridge 1894), Latin; English: Babcock 1989', 'archive.org',
    'public domain (Latin); Babcock 1989 English in copyright', ['don:C3/S3', 'don:C3/S8'], english_copyright=True,
    notes='The nearest Donatist theology; would complicate the "end of the world we cannot speak to at all" limit.')
acq('Donatist martyr acts (Passio Marculi; Passio Maximiani et Isaac; Sermo de passione Donati) in English', 'anon. (Donatist)',
    'English: Maureen Tilley, Donatist Martyr Stories, TTH 24 (Liverpool 1996); Latin PL 8 (Migne)', 'not stated (Tilley); archive.org (PL 8)',
    'Latin public domain; Tilley English in copyright', ['don:C3/S1', 'don:C3/S2', 'don:C3/S6', 'don:C14/S3'], english_copyright=True,
    identified_as=['don.source.tilley-donatist-martyr-stories (kind: unvendored); WANTS unclassified'],
    notes='The Latin PL 8 text is ALREADY vendored (cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, Passio Marculi at line 666); only an English is missing, and the only English is in copyright. The crown-of-martyrdom eschatology in the movement\'s own voice; lament rhetoric for C14/S3.')
acq('Le dossier du donatisme', 'J.-L. Maier', 'Berlin 1987-89 (modern edition); not stated in report', 'not stated in report', 'not stated in report (modern; presumably in copyright)',
    ['don:C3/S2'], identified_as=['don.source.maier-le-dossier-du-donatisme (kind: unvendored)'])
acq('Loca sanctorum Africae: le culte des martyrs en Afrique du IVe au VIIe siecle', 'Yvette Duval', 'Rome 1982 (modern); not stated in report', 'not stated in report', 'not stated in report (modern; presumably in copyright)',
    ['don:C3/S5'], identified_as=['don.source.duval-loca-sanctorum-africae (kind: unvendored)'],
    notes='Martyr-cult archaeology; modern, not a period voice.')
acq('De vocatione omnium gentium (On the Call of All Nations), incl. the fate of infants who die', 'Prosper of Aquitaine',
    'Latin: PL 51 (Migne); English: De Letter, ACW 14 (1952)', 'archive.org (PL 51)', 'public domain (Latin); ACW 14 English in copyright',
    ['gallic:C3/S7'], english_copyright=True, notes='Facilitator-adjacent cell (unbaptised infants).')
acq('Commentary on Jonah 3:6-9 (whether the devil can repent); Commentary on Ephesians (the passages Rufinus threw back)', 'Jerome',
    'Latin: PL 25 and PL 26 (Migne); English: Hegedus 1991, Heine 2002', 'archive.org', 'public domain (Latin); English in copyright',
    ['hal:C3/S3', 'hal:C3/S7'], english_copyright=True, notes='C3/S7: suicide question; the Jonah commentary is the only Jerome text named for it (Latin only).')
acq('De bono mortis (On the Good of Death)', 'Ambrose', 'Latin: PL 14 (Migne); English: McHugh, FOTC 65 (1972)', 'archive.org / CCEL',
    'public domain (Latin); FOTC 65 English in copyright', ['ijc:C3/S5'], english_copyright=True,
    notes='De excessu fratris Satyri, named in the same row, is already vendored in npnf210 (de Romestin 1896).')
acq('Codex Theodosianus in English (XVI.5, IX.17, 16.7: heretics\' burial and tombs; apostates)', 'Clyde Pharr (trans.)',
    'The Theodosian Code (Princeton 1952); Latin: Mommsen-Meyer (Berlin 1905)', 'archive.org (Mommsen)', 'Latin public domain; Pharr English in copyright',
    ['ijc:C3/S7', 'ijc:C14/S7'], english_copyright=True, identified_as=['cappadocian.source.pharr-theodosian-code-translation (kind: unvendored)'],
    notes='The Latin is ALREADY vendored (cic/texts/codex-theodosianus_latinlibrary.txt, cited by C14 ijc S7).')
acq('Care of the Dead in Late Antiquity', 'Eric Rebillard', 'Cornell 2009 (modern monograph); not stated in report', 'not stated in report', 'not stated in report (modern; presumably in copyright)',
    ['lpc:C3/S5'], identified_as=['lpc.source.rebillard-care-of-the-dead-in-late-antiquity (no kind field in record)'])
acq('Sibylline Oracles II.330-338 (the righteous may beg God to rescue the damned)', 'anon.', 'Milton S. Terry, The Sibylline Oracles translated into English blank verse (New York 1899)',
    'archive.org / sacred-texts', 'public domain', ['pahc:C3/S3'])
acq('Fidei expositio / A Short and Clear Exposition of the Christian Faith (1531: the company of heaven incl. Hercules, Socrates, the Catos); Fidei ratio (1530); Sermon on the Providence of God (1530)', 'Huldrych Zwingli',
    'The Latin Works of Huldreich Zwingli, vol. 2, ed. W.J. Hinke (Heidelberg Press, Philadelphia 1922), pp. 235-293 and 33-61', 'archive.org',
    'public domain in the US (1922)', ['rzg:C3/S6', 'rzg:C3/S7', 'rzg:C4/S3', 'rzg:C4/S6'],
    notes='Vols. 1 and 3 are vendored; vol. 2 is the one volume missing. C4 fleet note: rzg has no answer to "people who never heard" unless this is vendored.')
acq('Psychopannychia (against soul-sleep; the soul between death and resurrection)', 'John Calvin', "Calvin's Tracts, vol. 3, trans. Henry Beveridge (Calvin Translation Society, Edinburgh 1851)",
    'archive.org / CCEL', 'public domain', ['rzg:C3/S4', 'rzg:C3/S5'])
acq('Registers of the Consistory of Geneva in the Time of Calvin, vol. 1', 'ed. Robert Kingdon et al.', 'Eerdmans 2000; the French Droz edition also in copyright', 'not stated in report', 'in copyright',
    ['rzg:C3/S7', 'rzg:C4/S5', 'rzg:C14/S4', 'rzg:C14/S5', 'rzg:C14/S6', 'rzg:C14/S7'], english_copyright=True,
    identified_as=['rzg.source.geneva-consistory-registers (kind: unvendored); WANTS'],
    notes="What ordinary doubters said when examined; where Geneva's practice on suicide would show; the only case material for 'were your people judgmental'. Copyright blocks it.")
acq('Tabula praedestinationis (Summa totius Christianismi)', 'Theodore Beza', 'not stated in report', 'not stated in report', 'not stated in report',
    ['rzg:C4/S3'], identified_as=['rzg.source.beza-works (kind: unvendored)'])
acq('The Decades (Decade I sermons 4-6 on faith, justification, good works)', 'Heinrich Bullinger', 'Parker Society, 4 vols (Cambridge 1849-52)', 'archive.org', 'public domain',
    ['rzg:C4/S1'], identified_as=['not in the rzg registry (C4: "unvendored; not in registry")'],
    notes='The exact Decades sermon on predestination was not located; Decade I.4-6 is secure.')
acq("Concerning the Eternal Predestination of God (De aeterna Dei praedestinatione, 1552) in English", 'John Calvin', "trans. Henry Cole, Calvin's Calvinism (1856)", 'archive.org', 'public domain',
    ['rzg:C4/S3'], notes='The Latin/French is already vendored (calvin_opera-omnia-vol8-lat-fra_baum-cunitz1870.txt L170).')
acq('Hymns on Paradise', 'Ephrem', 'Latin/Syriac: T.J. Lamy, Sancti Ephraem Syri Hymni et Sermones, 4 vols (Mechelen 1882-1902); English: Brock (SVS 1990)', 'archive.org (Lamy)',
    'public domain (Lamy); Brock English in copyright', ['syr:C3/S2', 'syr:C3/S6'], english_copyright=True)
acq('Carmina Nisibena, full cycle (incl. the Death-and-Satan hymns beyond Gwynn\'s NPNF selection)', 'Ephrem', 'G. Bickell, S. Ephraemi Syri Carmina Nisibena (Leipzig 1866), Syriac with Latin', 'archive.org', 'public domain',
    ['syr:C3/S2'])
acq("Letters of consolation, incl. the letter to Hans von Rechenberg (1522, no. 540) on whether God can save one who dies without faith", 'Martin Luther',
    "Preserved Smith and C.M. Jacobs, Luther's Correspondence and Other Contemporary Letters, 2 vols (Philadelphia 1913, 1918); Margaret A. Currie, Letters of Martin Luther (Macmillan 1908); Tappert LCC 18 (1955)",
    'archive.org', 'Smith-Jacobs and Currie public domain in the US; Tappert in copyright',
    ['witt:C3/S7', 'witt:C14/S2', 'witt:C14/S8'], notes='C3 witt: "a decision on the Rechenberg letter" (unbaptised infants / died without faith; Facilitator-adjacent).')
acq('Ein Trost den Weibern, welchen es ungerade gegangen ist mit Kindergebaren (Comfort for Women Who Have Had a Miscarriage, 1542)', 'Martin Luther with Bugenhagen',
    'German: WA 53:205-208 (Weimar 1920); English: LW 43 (1968)', 'archive.org (Weimarer Ausgabe)', 'public domain (German); LW English in copyright',
    ['witt:C3/S7'], english_copyright=True, notes="Luther's pastoral softening of the confession's words on the unbaptised; Facilitator-adjacent.")
acq('Ein Sermon von der Bereitung zum Sterben (A Sermon on Preparing to Die, 1519)', 'Martin Luther', 'Works of Martin Luther, Holman ed., vol. 1 (Philadelphia 1915), pp. 99-116', 'archive.org', 'public domain',
    ['witt:C3/S5'], notes='The vendored luther_works-v1-selected_jacobs-spaeth1915.txt names "Of Preparation for Death" only in a contents line (6314); the C3 report says the text itself is not in the vendored selection. Confirm before downloading.')

# ---- C4 ----
acq('Homilies on Leviticus 8.3; Commentary on Romans 5.9 (infant baptism "for the remission of sins")', 'Origen',
    'Latin: PG 12/14 (Migne); English: Barkley FOTC 83 (1990), Scheck FOTC 103-104 (2001-02)', 'archive.org', 'public domain (Latin); English in copyright',
    ['alx:C4/S2', 'alx:C3/S7'], english_copyright=True, notes='C3 alx S7: "Origen\'s infant-baptism homilies are Latin, unvendored"; the dead-baby question (Facilitator-adjacent).')
acq('Contra Collatorem', 'Prosper of Aquitaine', 'Latin: PL 51 (Migne 1861); English: de Letter, ACW 32 (1963)', 'archive.org', 'public domain (Latin); ACW 32 English in copyright',
    ['gallic:C4/S1', 'gallic:C4/S3', 'gallic:C3/S7'], english_copyright=True, identified_as=['gallic.source.prosper-contra-collatorem (kind: unvendored)'])
acq('Pro Augustino responsiones (ad capitula Gallorum; ad capitula obiectionum Vincentianarum)', 'Prosper of Aquitaine', 'Latin: PL 51 (Migne); not otherwise stated', 'archive.org (PL 51)', 'public domain (Latin); no PD English named',
    ['gallic:C4/S1', 'gallic:C3/S7'], identified_as=['gallic.source.prosper-pro-augustino-responsiones (kind: unvendored)'])
acq('Carmen de ingratis', 'Prosper of Aquitaine', 'Latin: PL 51 (Migne); not otherwise stated', 'archive.org (PL 51)', 'public domain (Latin)',
    ['gallic:C4/S1'], identified_as=['gallic.source.prosper-carmen-de-ingratis (kind: unvendored)'])
acq('Epistulae 225-226 (Prosper and Hilary to Augustine; omitted by NPNF)', 'Prosper; Hilary of Marseille', 'Latin: CSEL 57 (Goldbacher 1911); English: FOTC 32 (1956)', 'archive.org', 'public domain (Latin); FOTC 32 English in copyright',
    ['gallic:C4/S1'], english_copyright=True, identified_as=['gallic.source.augustine-letters-221-226-absence (no kind field in record)'],
    notes='CHECK FIRST: cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt is vendored (CSEL 57 pars IV covers Epp. 185-270); confirm whether 225-226 are in it before downloading.')
acq('Historia Pelagiana', 'Enrico Noris', 'Padua 1673 (Latin); not otherwise stated', 'not stated in report', 'public domain by age (Latin)',
    ['gallic:C4/S1'], identified_as=['gallic.source.noris-historia-pelagiana (kind: unvendored; WANTS-REGISTER row)'])
acq('Commentary on Romans (the opponent\'s own voice)', 'Pelagius', 'Latin: Souter, Texts and Studies IX (Cambridge 1922-31); English: de Bruyn (OUP 1993)', 'archive.org',
    'public domain in the US (Latin); de Bruyn English in copyright', ['hal:C4/S1', 'lpc:C4/S1', 'gallic:C4/S1'], english_copyright=True,
    notes='hal, lpc and gallic build the Pelagian controversy from the opponents\' side only. The Letter to Demetrias is already vendored in Latin but mapped only to the unbuilt pelagianism world (see drift list).')
acq('Council of Orange (529), canons', 'council', 'English: Hefele, History of the Councils vol. 4 (T&T Clark 1895)', 'archive.org', 'public domain',
    ['gallic:C4/S3'], notes='Outside every window; Facilitator context only (closed the argument after the Gallic window). Hefele vols 1-3 are vendored, vol. 4 is not.')
acq('De libero arbitrio diatribe (1524)', 'Erasmus', 'Latin 1524; English: Rupp/Watson, LCC 17 (1969)', 'not stated in report', 'public domain (Latin); LCC 17 English in copyright',
    ['witt:C4/S3'], english_copyright=True, identified_as=['witt.source.erasmus-de-libero-arbitrio-diatribe (kind: unvendored; WANTS-REGISTER)'])
acq('Loci communes (1521)', 'Philip Melanchthon', 'Latin: Kolde ed. (1900); English: Pauck, LCC 19 (1969)', 'archive.org', 'public domain (Latin); LCC 19 English in copyright',
    ['witt:C4/S1'], english_copyright=True)
acq('Unterricht der Visitatoren / Instructions for the Visitors (1528)', 'Melanchthon (with Luther)', 'German: WA 26; also Sehling, Evangelische Kirchenordnungen Bd. 1 (1902); English: LW 40', 'archive.org',
    'public domain (German); LW 40 English in copyright', ['witt:C14/S6', 'witt:C14/S7'], english_copyright=True,
    identified_as=['cited as witt.source.melanchthon-instructions-for-the-visitors (unvendored) in C14 and as a WANTS-REGISTER row in C4; NOTE no record file of that name exists under records/witt/source/'])
acq('Saxon visitation protocols (1527-29)', 'Saxon visitors', 'German: Sehling, Die evangelischen Kirchenordnungen des XVI. Jahrhunderts, Bd. 1 (Leipzig 1902)', 'archive.org', 'public domain (German)',
    ['witt:C14/S6', 'witt:C14/S7'], identified_as=['witt.source.saxon-visitation-protocols (kind: unvendored)'], notes='"The drift, measured": the bishop/visitation accountability question is only identified.')

# ---- C14 ----
acq('Homily "That God is not the author of evils" (Quod Deus non est auctor malorum)', 'Basil of Caesarea', 'Greek: PG 31; English: Way, FOTC 46 (1963)', 'not stated in report',
    'public domain (Greek); no PD English known', ['cappadocian:C14/S1'], english_copyright=True)
acq('To Stagirius (on despondency); On Providence / To those who are scandalized', 'John Chrysostom', 'Greek: PG 47 and PG 52 (both ALREADY vendored); French: Bareille, Oeuvres completes (1865-73)', 'archive.org (Bareille)',
    'Greek PD; French Bareille PD; no PD English', ['ijc:C14/S1', 'ijc:C14/S8'], english_copyright=True,
    notes='The Greek is vendored (john-chrysostom_opera-pg47-palladius-dialogus-grc-lat_migne1863.txt; john-chrysostom_opera-pg52-epistulae-grc-lat_migne1862.txt). The missing item is a public-domain modern-language version; Bareille\'s French is the only one named.')
acq('Commentary on the Psalms (the Reformed lament text)', 'John Calvin', 'trans. James Anderson, Calvin Translation Society 1845-49', 'CCEL; archive.org', 'public domain', ['rzg:C14/S3'])
acq('Sermons on Job', 'John Calvin', 'trans. Arthur Golding (1574)', 'EEBO / archive.org', 'public domain', ['rzg:C14/S1'])
acq('Letters of John Calvin, vol. 3', 'ed. Jules Bonnet', 'Edinburgh 1858', 'archive.org', 'public domain', ['rzg:C14/S1', 'rzg:C14/S2'],
    notes='Vols. 1, 2 and 4 are vendored; vol. 3 is the missing one.')
acq('Pestlied (Plague Hymn, 1519)', 'Huldrych Zwingli', 'English in S.M. Jackson, Huldreich Zwingli (1901)', 'archive.org', 'public domain', ['rzg:C14/S1'],
    notes='Not in the vendored zwingli_selected-works_jackson1901.txt (grep for the hymn found nothing); the 1901 biography is a different volume.')
acq('Excuse a Messieurs les Nicodemites (1544)', 'John Calvin', 'French in Calvini Opera; no PD English located', 'not stated in report', 'French public domain; no PD English',
    ['rzg:C14/S7'], english_copyright=True, notes='Quiet conformers; Calvin\'s letters against the Nicodemites in Bonnet are vendored (vols 1, 2, 4).')

# ---- C3 rows for worlds that have no records yet ----
acq('Homilies on the Gospels (Hom. 12 the five foolish virgins; Hom. 40 Dives and Lazarus)', 'Gregory the Great', 'Latin: PL 76 (Migne); English: Hurst, CS 123 (1990)', 'archive.org',
    'public domain (Latin); Hurst English in copyright', ['rcg:C3/S1'], english_copyright=True, notes='rcg has no records yet (building).')
acq("Hymns (James of Edessa's recension), incl. the hymns on the departed", 'Severus of Antioch', 'E.W. Brooks, Patrologia Orientalis 6.1 and 7.5 (Paris 1909-1911), Syriac with English', 'archive.org',
    'public domain in the US', ['wsyr:C3/S5'], notes='wsyr has no records yet.')
acq('Memre on the resurrection and on the departed', 'Jacob of Serugh', 'Syriac: P. Bedjan, Homiliae selectae Mar-Jacobi Sarugensis, 5 vols (Paris 1905-1910); English: Hansbury (Gorgias 2008)', 'archive.org (Bedjan)',
    'public domain (Syriac); Hansbury English in copyright', ['wsyr:C3/S6'], english_copyright=True, notes='wsyr has no records yet.')
acq('Catechetical Homilies; Pauline commentary fragments (the Antiochene restorationist strand)', 'Theodore of Mopsuestia',
    'A. Mingana, Woodbrooke Studies 5-6 (Cambridge 1932-33), Syriac with English; Latin fragments H.B. Swete (Cambridge 1880-82)', 'archive.org',
    'Swete public domain; Mingana 1932-33 rights unclear in the US', ['aec:C3/S3'], notes='aec has no records yet.')
acq("Taborite chiliast articles of 1420 and the Prague masters' replies, in Lawrence of Brezova, Historia Hussitica", 'Lawrence of Brezova',
    'Fontes Rerum Bohemicarum V, ed. J. Goll (Prague 1893), Latin and Czech; English: Kaminsky 1967', 'archive.org / Czech digital library',
    'public domain; Kaminsky English in copyright', ['hus:C3/S8'], english_copyright=True, notes='hus has no records yet; Taborite chiliasm is also in the vendored Hofler Latin.')
acq('Summa doctrinae christianae / A Summe of Christian Doctrine (English 1588)', 'Peter Canisius', 'EEBO / Early English Books', 'EEBO', 'public domain', ['jes:C3/S5'],
    notes='jes has no records yet; Trent Session 25 (Waterworth 1848) is already vendored.')
acq("Sermons 15 'The Great Assize' (1758), 73 'Of Hell' (1782), 106 'On Faith' (1788), 'The General Deliverance'", 'John Wesley', 'Works of John Wesley, ed. Thomas Jackson, 14 vols (London 1872), vols 5-7',
    'archive.org / CCEL / Wesley Center Online', 'public domain', ['meth:C3/S1'], notes="meth has no records yet; the vendored 1771 Sermons vol. 1 holds 'The Great Assize' but not 'Of Hell'.")
acq("Funeral Hymns (1746; 2nd series 1759)", 'Charles Wesley', 'Osborn, Poetical Works vol. 6 (London 1870)', 'archive.org', 'public domain', ['meth:C3/S6'],
    notes='meth has no records yet; the 1780 Collection is vendored.')
acq('Pomorskie otvety (The Pomorian Answers, 1723)', 'Andrei Denisov et al.', 'Russian, Moscow 1911 (Preobrazhenskoe reprint); English: Crummey 1970', 'archive.org / Russian State Library digital',
    'public domain (Russian); Crummey English in copyright', ['obel:C3/S8'], english_copyright=True, notes='obel has no records yet.')

# ---- registry drift: registered unvendored (or mis-mapped) but the text is in cic/texts ----
DRIFT = [
 dict(id='gallic.source.cassian-de-incarnatione', finding='Registered kind: unvendored and on WANTS-REGISTER, but Cassian, On the Incarnation against Nestorius is in the vendored npnf211 (heading at line 48467).',
      file=P('npnf211'), line=48467, reports=['C1 gallic S2', '00-summary'], fix='source-record fix (kind, file) and remove the WANTS row'),
 dict(id='witt.source.book-of-concord', finding='Registered kind: unvendored although Jacobs 1911 Book of Concord is vendored and mapped to witt; witt.term.free-will says the library carries no developed predestination doctrine, but Formula of Concord XI is at lines 25390 and 27478.',
      file=P('boc'), line=25390, reports=['C4 witt S3', '00-summary'], fix='source-record fix and a term correction (or map fix)'),
 dict(id='rzg.source.ecclesiastical-ordinances-1541', finding='Registered kind: unvendored while calvin-geneva-council_ordonnances-ecclesiastiques-fra_tournes1735.txt (a 1735 printing) is mapped to rzg; check it is the 1541 text.',
      file=P('ordonnances'), line=None, reports=['C4 findings', 'C14 rzg S5'], fix='source-record fix after confirming the printing'),
 dict(id='pelagius_epistula-ad-demetriadem-lat_migne.txt (corpus map)', finding="Vendored in Latin but mapped only to the unbuilt 'pelagianism' world (cic/corpus-map/pelagianism.yaml); hal, lpc and gallic build the controversy from the opponents' side only.",
      file=P('pelagius-dem'), line=None, reports=['C4 hal S1', 'C4 findings'], fix='corpus-map fix: add rows for hal, lpc, gallic'),
 dict(id='don.source.tilley-donatist-martyr-stories (Latin side)', finding='Registered unvendored (the English, Tilley 1996, is in copyright), but the Latin passions (Passio Marculi etc.) are vendored in monumenta-vetera-donatistarum_migne-pl8.txt and the C14 report already cites them for don S2/S3.',
      file=P('pl8'), line=666, reports=['C3 don S1/S6', 'C14 don S2/S3'], fix='registry note: Latin held, English blocked; no download possible'),
 dict(id='cappadocian.source.pharr-theodosian-code-translation (Latin side)', finding='Pharr\'s English is unvendored and in copyright, but the Latin Codex Theodosianus is vendored (codex-theodosianus_latinlibrary.txt) and cited by C14 ijc S7.',
      file=P('codex-theod'), line=None, reports=['C3 ijc S7', 'C14 ijc S7'], fix='registry note; no download possible for the English'),
 dict(id='witt.source.melanchthon-instructions-for-the-visitors', finding='Cited by the C14 report as a source record (unvendored) but no file of that name exists under records/witt/source/; the work is a WANTS-REGISTER row in C4.',
      file=None, line=None, reports=['C14 witt S6', 'C4 identified'], fix='confirm the record id or create the source record when the text is acquired'),
]

# ---- listed as OTHER in a report but already in cic/texts (no download; read and render) ----
VENDORED_ALREADY = [
 dict(work='Origen, De Principiis II.10-11 and III.6 (Crombie, ANF 4)', file=P('anf04'), line=4985, cells=['alx:C3/S2'], note='Butterworth 1936 (from Koetschau) is the better witness but its rights are unclear outside the UK.'),
 dict(work='Basil, Shorter Rules 267 (Clarke 1925)', file=P('basil-rules'), line=11714, cells=['cappadocian:C3/S2'], note='US-PD (pre-1930); UK term ran to 2038. Vendored and mapped; the C3 S1 cell confirms it.'),
 dict(work="Gregory of Nyssa, On Infants' Early Deaths (NPNF 2/5)", file=P('npnf205'), line=32849, cells=['cappadocian:C3/S7'], note='other.json lists it only to show it is the same volume; LOADED, not OTHER.'),
 dict(work='Faustus of Riez, De gratia and Epistulae (CSEL 21, Engelbrecht 1891)', file=P('faustus'), line=None, cells=['gallic:C3/S5', 'gallic:C4/S1'], note='Latin only; no public-domain English exists.'),
 dict(work='Jerome, Letter 124 to Avitus; Dialogue against the Pelagians I.28 (NPNF 2/6)', file=P('npnf206'), line=40528, cells=['hal:C3/S2'], note='LOADED; listed for completeness.'),
 dict(work='Ambrose, De excessu fratris Satyri (NPNF 2/10)', file=P('npnf210'), line=819, cells=['ijc:C3/S5'], note='Only De bono mortis in the same row is missing (see acquire list).'),
 dict(work='Augustine, De octo Dulcitii quaestionibus (PL 40)', file=P('aug-pl40'), line=10141, cells=['lpc:C3/S3'], note='The report lists PL 40 as OTHER; the vendored augustine_opera-minora-catechetica-lat_migne-pl40.txt carries it (heading at line 10141). Latin only; FOTC 16 English in copyright.'),
 dict(work='Possidius, Life of Augustine ch. 31 (Weiskotten 1919)', file=P('possidius'), line=None, cells=['lpc:C3/S5'], note='Vendored; C14 says "cited elsewhere".'),
 dict(work='Augustine, Sermons 172-173 (Latin, PL 38)', file=P('aug-sermones-lat'), line=None, cells=['lpc:C3/S5'], note='Latin vendored; Hill WSA III/5 (1992) English in copyright.'),
 dict(work='Augustine, De fide et operibus (CSEL 41)', file=P('aug-fide-op'), line=None, cells=['lpc:C4/S1'], note='Latin only; Lombardo ACW 48 (1988) in copyright; no PD English. DOWNLOAD-QUEUE also holds Opera t. VI (Migne) and CSEL 42.'),
 dict(work='Optatus of Milevis, Against the Donatists (Vassall-Phillips 1917)', file=P('optatus'), line=None, cells=['don:C3/S7'], note='C3 report: "now confirmed vendored".'),
 dict(work='Papias fragments; Justin, Dialogue 80-81 (ANF 1)', file=P('anf01'), line=None, cells=['pahc:C3/S8'], note='Vendored.'),
 dict(work='Second Helvetic Confession ch. 26 (burial; purgatory rejected; apparitions as deceits)', file=P('schaff-helv'), line=1475, cells=['rzg:C3/S4', 'rzg:C3/S5'], note='The report names Schaff, Creeds vol. 3 (1877) as OTHER, but the vendored 1919 Second Helvetic file has "Chap. XXVI. Of the Burial of the Faithful" at line 1475.'),
 dict(work='Odes of Solomon 42 (Harris 1911)', file=P('harris-odes'), line=714, cells=['syr:C3/S5'], note='The report names Harris 1909 / Bernard 1912 as OTHER; Harris 1911 is vendored (syr.source.odes-of-solomon, 0 citing records).'),
 dict(work='Athanasius, Letters to Serapion IV.8-23 (PG 26, Greek/Latin)', file=P('athan-pg26'), line=None, cells=['alx:C4/S8'], note='No PD English (Shapland 1951 in copyright).'),
 dict(work='Origen, On Prayer (Koetschau 1899, Greek)', file=P('origen-orat'), line=None, cells=['alx:C14/S2'], note='No PD English (Jay 1954, Greer 1979 in copyright); Greek PG 11 is PD.'),
 dict(work='Gregory Nazianzen, Carmina de se ipso; Sasima letters 48-50 and Ep. 58 (PG 37, Greek/Latin)', file=P('naz-pg37'), line=None, cells=['cappadocian:C14/S3', 'cappadocian:C14/S6'], note='No complete PD English (Meehan FOTC 75, 1987 in copyright); the letters are "WANTS unclassified".'),
 dict(work='Chrysostom, Homilies on 1 Corinthians 41.8 (NPNF 1/12)', file=P('npnf112'), line=25428, cells=['aec:C3/S5'], note='aec has no records yet.'),
 dict(work='Gregory the Great, Dialogues IV.39-41, IV.55-57 (Gardner 1911)', file=P('greg-dial'), line=11361, cells=['rcg:C3/S5'], note='rcg has no records yet; "the world most people would ask about purgatory".'),
 dict(work='Hus, De ecclesia ch. 1 (Schaff 1915)', file=P('hus-eccl'), line=3036, cells=['hus:C3/S5'], note='hus has no records yet.'),
 dict(work='Francis Xavier, letter from Cochin 29 Jan 1552 (Coleridge 1872 vol. 2)', file=P('xavier2'), line=18876, cells=['jes:C3/S7'], note='jes has no records yet.'),
 dict(work='Ignatius, Spiritual Exercises, First Week fifth exercise (Mullan 1914)', file=P('ignatius-ex'), line=451, cells=['jes:C3/S1'], note='jes has no records yet.'),
 dict(work='Council of Trent, Session 25 decree on purgatory (Waterworth 1848)', file=P('trent'), line=None, cells=['jes:C3/S5'], note='jes has no records yet.'),
 dict(work='Avvakum, Life (Harrison and Mirrlees 1924)', file=P('avvakum'), line=None, cells=['obel:C3/S1'], note='obel has no records yet.'),
 dict(work="Charles Wesley, 1780 Collection sections 'Describing Death', 'Judgment', 'Heaven', 'Hell'", file=P('wesley-c1780'), line=2709, cells=['meth:C3/S6'], note='meth has no records yet.'),
]

# =====================================================================
# 2. RECORDS BY WORLD
# =====================================================================
R = []
def rec(world, cells, rtype, source, file=None, line=None, reason='', fac=False, group='loaded'):
    R.append(dict(world=world, cells=cells if isinstance(cells, list) else [cells], record_type=rtype,
                  source_text=source, file=P(file) if file else None, line=line, reason=reason,
                  facilitator_adjacent=fac, group=group))

# ---------------- alx ----------------
w='alx'
rec(w,['C1/S6'],'quote',"Origen, Contra Celsum VI.75 'little, and ill-favoured'",'anf04',57478,"C1 fleet hole 2: nothing rendered anywhere on what Jesus looked like; 'the two best ancient texts on appearance are both mapped to this world and unrendered'.")
rec(w,['C1/S6'],'quote',"Clement, Paedagogus III.1 'the Lord Himself was uncomely in aspect'",'anf02',24488,"Same gap; second-century consensus from Isaiah 53, already in hand.")
rec(w,['C1/S5'],'quote','Origen, Contra Celsum I.47 (and II.13), Josephus on James','anf04',None,"C1 alx: 'No record answers did he exist or had anyone known an eyewitness. No C-E demonstration.'")
rec(w,['C1/S4'],'quote',"Origen, Contra Celsum II.55 (Celsus: the story grew)",'anf04',None,"'Contra Celsum II.55 (story grew) is loaded and unrendered'; the fleet's best-argued resurrection cell lacks the objection itself.")
rec(w,['C1/S2'],'quote',"Origen, Contra Celsum I.28-39 (Celsus's 'mere man'; the Panthera charge; virgin birth)",'anf04',None,"'Celsus's mere man objection and Origen's reply are loaded but no record carries them'; C1 fleet hole 3, the outsider's 'prophet or God'.")
rec(w,['C1/S3'],'demonstration','C-T witness on the cross (De Incarnatione 6-10, 20-25; Origen Comm. Matt XVI.8 ransom)','npnf204',None,"'No C-T demonstration'; 'no witness states a position on penal substitution or personal Lord and Savior (C-T-02/03 unanswered)'.")
rec(w,['C3/S1'],'quote','Clement, Stromateis VII on corrective punishment','anf02',None,"C3 must add: 'a second quote so the voice is not Origen-only'.")
rec(w,['C3/S2'],'quote','Origen, De Principiis II.10-11 (and III.6) on whether punishment ends','anf04',24311,"C3: whether hell ends, 'the voice can only defer; De Principiis II.10-11 is vendored in anf04 and unquoted'.")
rec(w,['C3/S5'],'quote or honest_limit',"Origen, De Principiis II.11.6 'school of souls'; Clement, Stromateis VI.6 (descent-preaching)",'anf04',10782,"C3 must add: 'a quote or honest_limit on the interim state'; nothing on the soul between death and resurrection, prayer for the dead, or Hades. Clement at anf02 line 19398.",fac=True)
rec(w,['C4/S1'],'quote',"Clement, Who is the Rich Man that Shall be Saved? (the literal 'what must I do to be saved')",'anf02',56126,"C4 alx: 'No record on faith-versus-works'; quote record from Quis Dives.")
rec(w,['C4/S5'],'quote','Clement, Quis Dives 39-42 (the one repentance after baptism; the robber restored)','anf02',None,"'No quote record on the once-only repentance; Quis Dives 39-40 would supply it.'")
rec(w,['C4/S3'],'quote','Origen, De Principiis III.1 On the Freedom of the Will; the potter and the clay (Rom 9)','anf04',27830,"'Romans 9 (C4-21) is answered at length in De Principiis III.1 and is vendored; no quote record yet.' Potter at line 28834; Philocalia XXI/XXIII also vendored.")
rec(w,['C4/S6'],'quote','Clement, Stromateis I.5 (philosophy as covenant); VI.6 (gospel preached in Hades to righteous Gentiles)','anf02',46951,"'Alexandria has the most distinctive patristic answer to C4-08/C4-22 and none of it is rendered.'")
rec(w,['C14/S1','C14/S3'],'quote','Origen, Philocalia chs. 21-27 on providence','philocalia',None,"C14 add: 'a quote from Philocalia on providence'; only the punishment-heals passage is quoted.")
rec(w,['C14/S7'],'quote','Peter of Alexandria, Canonical Epistle on the lapsed','anf06',None,"C14 add: 'Peter of Alexandria's canons on the lapsed (anf06) for S7'; alx.source.alexandrian-canonical-answers is cited only for Timothy's answers.")
rec(w,['C4/S1'],'honest_limit',"'faith alone' is a later framing",None,None,"C4 alx add: 'an honest_limit on faith alone'; fleet section lists alx among worlds missing it as a record.",group='no_text')
rec(w,['C3/S4'],'honest_limit','no Alexandrian teacher taught that the lost are destroyed',None,None,"C3 must add: 'an honest_limit on annihilation (the vendored hits are Arnobius and Methodius, not Alexandrians)'.",group='no_text')
rec(w,['C4/S4'],'honest_limit',"'assurance' as felt certainty",None,None,"C4 alx: \"'Assurance' needs an honest_limit; falling and coming back is well covered.\"",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences (anachronism)',None,None,"C4 alx S7: 'Indulgences: honest_limit (anachronism)'.",group='no_text')
rec(w,['C14/S3','C14/S8'],'honest_limit',"no lament or anger-at-God record; no despair vocabulary: 'Alexandria's surviving voice is the teacher's, not the mourner's'",None,None,"C14 add: 'an honest_limit for S3/S8'. FAC follow-up has the plague-nursing presence story and 'nothing on grief by name'.",fac=True,group='no_text')
rec(w,['C3/S7','C4/S2'],'quote','Origen, Homilies on Leviticus 8.3; Commentary on Romans 5.9 (infant baptism)',None,None,"Unbaptised infants and suicide: 'NOTHING in records and nothing found vendored for this world (Origen's infant-baptism homilies are Latin, unvendored)'. Needs acquisition (Latin PD; English in copyright).",fac=True,group='acquire')

# ---------------- cappadocian ----------------
w='cappadocian'
rec(w,['C3/S3','C3/S2'],'quote','Gregory of Nyssa, Catechetical Oration 26 (restoration of all; harmony of thanksgiving from all creation)','npnf205',44415,"C3 must add: quote record, Documented, renderings on Opus. Confirmed in context lines 44408-44422; Open_Gaps item 3 (line 787) logs the probe that said Nyssa 'never made the claim plain'.")
rec(w,['C3/S7','C4/S2'],'quote',"Gregory Nazianzen, Oration 40.23: infants who die unbaptised 'neither glorified nor punished'",'npnf207',38494,"C3 must add (Documented, renderings on Opus); C4: 'the two best patristic texts on babies who die (C3-15/16) are vendored and unrendered'. Lines 38478-38496.",fac=True)
rec(w,['C3/S7','C4/S2','C14/S1'],'quote',"Gregory of Nyssa, On Infants' Early Deaths (whole treatise)",'npnf205',32849,"C4 'unrendered gold'; C14: 'the only patristic text on a dead child', source record cappadocian.source.gregory-nyssa-love-of-the-poor-lepers-consolation has 0 citing records.",fac=True)
rec(w,['C3/S2'],'contested_claim','how far Basil and Nazianzen shared Nyssa\'s hope: Basil Shorter Rule 267 holds punishment eternal (Clarke 1925 lines 7722, 11714) against Nyssa, Cat. Or. 26 and On the Soul and Resurrection','basil-rules',11714,"C3: 'The world argued with itself ... the right build is a contested_claim, not one quote.'")
rec(w,['C3/S5'],'term','purgation (katharsis): On the Soul and Resurrection, the purgatorial fire','npnf205',39606,"C3 must add: 'a lexicon term for purgation (katharsis)'; purgation passage lines 39606-39618 vendored and unquoted. Caution: the npnf207 prayers-for-the-dead hit (line 2866) is Cyril of Jerusalem.",fac=True)
rec(w,['C3/S6'],'quote','Gregory Nazianzen, Oration 7 on Caesarius (reunion with the dead)','npnf207',None,"C3 S6: 'Reunion with the dead: Nazianzen's Oration 7 on Caesarius is vendored (npnf207) and unquoted.'")
rec(w,['C1/S2'],'quote',"Gregory Nazianzen, Oration 30.7 ('the Father is greater than I')",'npnf207',None,"C1 add: 'Or. 30.7 answers the Father is greater than I directly; loaded, unrendered'; also the outsider framing (Or. 29-30).")
rec(w,['C1/S3'],'quote','Gregory of Nyssa, Catechetical Oration 22-26 (ransom to the devil; the fish-hook)','npnf205',None,"C1: 'Thin: no quote on the cross'; the witness distinguishes ransom/healing from penal substitution without a quote.")
rec(w,['C1/S7'],'quote or term',"Amphilochius, Iambics to Seleucus, canon list (held only as an editor's prose epitome)",'records/cappadocian/source/cappadocian.source.amphilochius-iambics-to-seleucus.md',None,"C1 add: Amphilochius's canon list; the witness 'names no gospel'. Vendored only as an epitome; check what can be quoted.")
rec(w,['C4/S3'],'term','free will from the Philocalia (XXI Free Will; XXIII fate and foreknowledge), Basil and Gregory\'s own anthology','philocalia',36,"C4: 'No record. The Philocalia is this circle's own compilation on free will; a term record would be cheap and sound.'")
rec(w,['C4/S8'],'quote',"Basil, Shorter Rules: no sin beyond forgiveness, 'Despair can never be justified'",'basil-rules',3990,"C4: 'Basil's rule that no sin is beyond forgiveness is the pastoral answer; unrendered.'")
rec(w,['C14/S1','C14/S3'],'quote',"Gregory Nazianzen, Oration 16 'On his Father's Silence, because of the Plague of Hail'",'npnf207',27542,"C14 add: 'the world's one direct theodicy sermon, no record'; Gregory speaks the people's complaint to God in their mouth. S1 has no quote record.")
rec(w,['C14/S7'],'quote or story','Basil, Longer Rules 14 and 36; Shorter Rules on brothers who leave the brotherhood','basil-rules',None,"C14 add: 'Basil's Longer Rules on brothers who leave'; 'wanting to leave, and what was said to one who left, is not' rendered. Source cited by 14 records, none on leaving.")
rec(w,['C3/S4'],'honest_limit','annihilation: Nyssa teaches the annihilation of evil, not of persons; nothing in the world\'s own words answers C3-08',None,None,"C3 must add: 'an honest_limit on annihilation'.",group='no_text')
rec(w,['C3/S8'],'honest_limit','end-times: Cappadocian material thin; the strong Antichrist hits (npnf207 line 1208) are Cyril of Jerusalem',None,None,"C3 must add: honest_limit on end-times; Open_Gaps line 667 says the F4-T end-times variant is unanswered.",group='no_text')
rec(w,['C4/S4'],'honest_limit',"'assurance' as felt certainty (canons answer falling and returning)",None,None,"C4: 'Needs honest_limit on assurance'.",group='no_text')
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 cappadocian S6: 'Honest_limit.'",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences (almsgiving as love of the poor, not payment)',None,None,"C4: 'indulgences honest_limit'.",group='no_text')
rec(w,['C4/S3'],'honest_limit',"'predestination, did it frighten you'",None,None,"C4 fleet section lists cappadocian among worlds with nothing on predestination as dread.",group='no_text')

# ---------------- desert ----------------
w='desert'
rec(w,['C3/S5'],'quote or story',"Vita Antonii 65-66: Antony's vision of souls ascending past the accuser",'npnf204',None,"C3 must add: 'a quote or story for Vita 65-66'; section cited, line not pulled in the pass.",fac=True)
rec(w,['C4/S5'],'quote','Cassian, Conference XX (Pinufius), On the End of Penitence and the Marks of Satisfaction','npnf211',43946,"C4 add: 'the answer to I keep falling into the same sin' (C4-26); unrendered.")
rec(w,['C4/S4'],'quote (Contested; Messalian flag) plus honest_limit','Macarian Homilies on felt assurance','macarius',None,"C4: 'the Macarian homilies felt assurance is the nearest patristic material to C4-19 and is flagged Messalian in the records'; fleet section: assurance honest_limit for all patristic worlds.")
rec(w,['C14/S7'],'story or quote','Palladius, Lausiac History 25-27 (Valens, Heron, Ptolemy: monks who fell or went back)','lausiac',None,"C14 add for S7; also Cassian Conference XIX (Abbot John who left the desert) in npnf211.")
rec(w,['C14/S2'],'quote','Macarian Homilies on dryness and the withdrawal of grace','macarius',None,"C14 add: 'Macarian Homilies on dryness for S2'.")
rec(w,['C1/S5'],'honest_limit','no record states that no one knew an eyewitness (silence rather than honest limit)',None,None,"C1 add: 'an honest_limit for S5'.",group='no_text')
rec(w,['C3/S2','C3/S3','C3/S4'],'honest_limit (absence records)','forever/ends, restoration, annihilation: nothing in the desert\'s own vendored voice',None,None,"C3 must add: 'absence records for S2-S4 in the shape of the existing limit, after reading the Sayings and not only the Vita' (anan-isho_paradise-v2-sayings_budge1907.txt).",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences',None,None,"C4 desert S7: 'Honest_limit on indulgences.'",group='no_text')
rec(w,['C1/S6'],'decision','whether anything on appearance belongs in this world (Contra Celsum VI.75 is mapped here)',None,None,"C1 add: 'consider whether anything on appearance belongs in this world (probably not)'.",group='no_text')
rec(w,['C3/S5'],'check','the Macarius-and-the-skull saying was not found in Budge vol. 2 by the terms used','budge2',436,"C3: 'check before citing it'; line 436 holds the skull-adjacent Macarius story.",fac=True,group='fix')
rec(w,['C3/S7','C3/S2'],'check',"npnf204 line 37049 ('to kill themselves') and line 18851 ('everlasting fire') need their work identified before use",'npnf204',37049,"C3: the file holds Athanasius's whole corpus; identify the work before citing.",fac=True,group='fix')
rec(w,[],'quote fix','two Macarian quote records failed the verbatim match on the second pass',None,None,"C1 fleet note: 'Six quotes not relevant to C1 (desert Macarian x2, gallic Salvian x4) still did not match on the second pass and should be rechecked by their worlds.'",group='fix')

# ---------------- don ----------------
w='don'
rec(w,['C1/S1'],'demonstration','C-I demonstration (Petilian or Emeritus at Carthage 411)','pl11',None,"C1: 'C-I served by a propositional record alone (Program Spec: never only propositional records)'; no demo and no quote.")
rec(w,['C1/S1'],'quote','Petilian or Emeritus at the Conference of Carthage 411 (Latin)','pl11',None,"C1 add: 'at least one quote (Petilian or Emeritus at Carthage 411 from pl11)'.")
rec(w,['C1/S6'],'quote','Cyprian, Testimonia II.13 (Christ without comeliness)','anf05',None,"C1 add: 'a quote from Testimonia II.13 for S6'; Cyprian is this world's own father.")
rec(w,['C3/S7'],'contested_claim',"voluntary death among the Circumcellions: Augustine's charge that they 'throw themselves over precipices'",'npnf104',16889,"C3 must add; R-20 'is a live hazard': the charge is vendored and no record frames it; 'a participant asking about suicide could pull it unguarded'.",fac=True)
rec(w,['C3/S1','C3/S2','C3/S5','C3/S6'],'honest_limit',"the movement's own afterlife voice (the martyr acts) is not in the library in English; everything vendored on Donatist hell-talk is the other side (Optatus, Augustine)",None,None,"C3 must add: honest_limit that don.source.tilley-donatist-martyr-stories is unvendored. Note the Latin passions ARE vendored (monumenta-vetera-donatistarum_migne-pl8.txt).",group='no_text')
rec(w,['C4/S3','C4/S6','C4/S7'],'honest_limit (extend don.limit.questions-we-never-argued)','predestination, the unevangelised, indulgences: no record and no Donatist text',None,None,"C4: 'extend the limit to name them'; 'the limit record names three questions never argued and could name this fourth'.",group='no_text')
rec(w,['C4/S4'],'honest_limit',"'assurance' as felt certainty",None,None,"C4 fleet section: all patristic worlds.",group='no_text')
rec(w,['C14/S8'],'honest_limit','F4-P-01 despair in Donatist voice: no record on despair, a restless mind, or anyone the way of life broke',None,None,"C14: 'S8 is NOTHING ... The build should add an honest_limit for F4-P-01'; FAC follow-up 'thin ... nothing on despair'.",fac=True,group='no_text')
rec(w,['C14/S3','C3/S1','C3/S6'],'quote','Donatist martyr acts (Passio Marculi; Passio Isaac et Maximiani; Sermo de passione Donati): lament rhetoric; the crown of martyrdom','pl8',666,"C14 don S3: 'nothing in English; the passions are Latin, Tilley's translation in copyright'. Latin is vendored; an English quote needs a rendering decision or Tilley (copyright).",group='acquire')

# ---------------- gallic ----------------
w='gallic'
rec(w,['C1/S1'],'demonstration','C-I demonstration',None,None,"C1: 'No C-I demonstration.'")
rec(w,['C1/S2','C1/S6'],'quote','Cassian, On the Incarnation against Nestorius (De Incarnatione; true flesh)','npnf211',48467,"C1 add: 'a quote from De Incarnatione for S2/S6'; the work is vendored despite the registry (see fix).")
rec(w,['C3/S1'],'quote',"Cassian, Conference XI.6 'fear of hell and the recollection of that terrible judgment'",'npnf211',35548,"C3 must add; 'hell itself sits only in the gravity and two terms'.")
rec(w,['C3/S1'],'quote',"Salvian, 'in time to come Gehenna will be in flames for the punishment of the wicked'",'salvian',2677,"C3 must add.")
rec(w,['C3/S5'],'story or quote',"Vita Martini 7: the dead catechumen 'brought before the tribunal of the Judge, and being assigned to gloomy regions and vulgar crowds', then sent back",'npnf211',1014,"C3 must add: 'the best unrendered story in the cluster'; lines 1014-1016. Correction: npnf211 line 5547 is Sulpitius's letter and 'fire of purgatory' there is the editor Clericus's note, not Cassian.",fac=True)
rec(w,['C3/S2'],'quote','Sulpitius, "doomed to eternal fire" (npnf211 line 6018); Salvian, "escape the torture of eternal fire" (line 4223)','npnf211',6018,"C3 gallic S2: 'No record states duration.'")
rec(w,['C4/S5'],'quote','Cassian, Conference XX On the End of Penitence (C4-26, the same sin again)','npnf211',43946,"C4 gallic: 'Conference XX for C4-26' unrendered.")
rec(w,['C14/S1','C14/S3'],'quote',"Cassian, Conference VI 'On the slaughter of some holy persons' (Abbot Theodore on why God permitted monks to be massacred)",'npnf211',None,"C14 add: 'the pastoral theodicy, no record'.")
rec(w,['C14/S2'],'quote','Cassian, Conference IX.34-36 on prayers heard, delayed or refused','npnf211',None,"C14 add; 'unanswered prayer has no record though Cassian treats it directly' (F4-P-03 has no demo in any world).")
rec(w,['C14/S8','C14/S3'],'quote or term',"Cassian, Institutes IX 'Of the spirit of dejection'",'npnf211',None,"C14 add: 'named inside a term and nothing more'.")
rec(w,['C4/S2'],'honest_limit','infants and inherited guilt: the brethren never argued them; Augustine (npnf105) is the outside voice the record carries',None,None,"C4: 'an honest_limit is the right build, pointing to Augustine as the outside voice'.",fac=True,group='no_text')
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 gallic S6: 'honest_limit'.",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences',None,None,"C4 gallic S7: 'Indulgences: honest_limit.'",group='no_text')
rec(w,['C4/S1'],'honest_limit',"'faith alone' as a record (the demo answers it in substance)",None,None,"C4 fleet section lists gallic among worlds missing the record.",group='no_text')
rec(w,['C3/S7'],'quote','Prosper, De vocatione omnium gentium (fate of infants who die); Prosper\'s anti-Cassian works',None,None,"C3: 'infants belong to Prosper (registered unvendored; De vocatione omnium gentium is OTHER)'. Needs acquisition.",fac=True,group='acquire')
rec(w,['C4/S1','C4/S3'],'quote or contested_claim','Prosper, Contra Collatorem; Pro Augustino responsiones; Carmen de ingratis; Augustine Epp. 225-226',None,None,"C4 gallic: 'Identified, not vendored'; the other side of the grace argument in its own words. Check CSEL 57 pars 4 (vendored) for Epp. 225-226 first.",group='acquire')
rec(w,['C4/S3'],'Facilitator note (not a Representative record)','Council of Orange 529 canons (Hefele vol. 4, 1895)',None,None,"C4: 'outside every window, Facilitator context only'.",fac=True,group='acquire')
rec(w,[],'source-record fix','gallic.source.cassian-de-incarnatione marked unvendored and on WANTS-REGISTER, but the work is in the vendored npnf211 (heading at line 48467)','npnf211',48467,"C1 finding; also 00-summary drift.",group='fix')
rec(w,['C3/S3','C3/S7'],'not_for fix',"gallic.term.predestination ('God wills all to be saved; to think otherwise is blasphemy', Conf. XIII.7) can be misread as universalism",None,None,"C3 must add: 'a not_for on the predestination term'.",group='fix')
rec(w,['C4/S3'],'duplicate fix','gallic.quote.grievous-blasphemy-not-all-men-to-be-saved and gallic.quote.without-grievous-blasphemy-all-men-to-be-saved carry the same Conf. XIII.7 sentence',None,None,"C4 findings: duplicates.",group='fix')
rec(w,[],'quote fix','four Salvian quote records failed the verbatim match on the second pass',None,None,"C1 fleet note: recheck by the owning world.",group='fix')

# ---------------- hal ----------------
w='hal'
rec(w,['C1/S7'],'quote','Jerome, Preface to the Four Gospels (to Damasus, 383)','npnf206',None,"C1 add: 'Damasus preface quote'; 'the best Latin world for C1-25; the Damasus preface is loaded and unrendered'.")
rec(w,['C1/S5'],'quote','Jerome, De viris illustribus 13 (Josephus on Christ)','npnf203',None,"C1 add: 'De viris 13 quote'; Jerome's own book, mapped and unrendered.")
rec(w,['C1/S2'],'quote','Jerome, Against Helvidius (perpetual virginity; virgin birth)','npnf206',None,"C1 add: 'Against Helvidius for the virgin birth'; 'no quote on divinity itself'.")
rec(w,['C3/S3'],'quote',"Jerome, Apology against Rufinus II: 'that the devil, will be saved; a thing which no man even though he had taken leave of his senses ... could say'",'npnf203',53776,"C3 must add.")
rec(w,['C3/S3'],'quote',"Jerome, Letter 124 to Avitus, the list of Origen's errors ('that the devil may be saved')",'npnf206',40528,"C3 must add.")
rec(w,['C3/S1','C3/S2'],'quote',"Jerome, Letter 39: 'mourn for the dead, but only for him whom Gehenna receives, whom Tartarus devours, and for whose punishment the eternal fire burns'",'npnf206',7903,"C3 must add; the only verified quote today is the Ciceronian dream.")
rec(w,['C3/S5'],'quote','Jerome, Letters 39, 60, 75, 108; Against Vigilantius (the dead hear prayers at the martyrs\' tombs)','npnf206',None,"C3 hal S5: 'No record on the interim state or prayer for the dead'; all in npnf206. Reunion in Letter 75 unquoted (S6).",fac=True)
rec(w,['C4/S1'],'quote','Jerome, Dialogue against the Pelagians I-III (line 42432); Letter 133 to Ctesiphon (line 27640)','npnf206',42432,"C4: 'No quote record from Against the Pelagians, which is vendored in full.'")
rec(w,['C4/S8'],'quote',"Jerome, Letter 42 to Marcella: what 'the sin against the Holy Ghost' is, against Novatian",'npnf206',8389,"C4: 'A whole vendored letter answers C4-25 and nothing is rendered.'")
rec(w,['C14/S7'],'quote','Jerome, Ep. 14 to Heliodorus, who left the desert (no source record)','npnf206',4634,"C14 add; 'leaving is only Fabiola's way back'. Needs a source record too.")
rec(w,['C14/S2'],'quote','Jerome, Ep. 60 to Heliodorus on Nepotian; Ep. 123 to Ageruchia (consolation; no source records)','npnf206',None,"C14 add.")
rec(w,['C14/S8'],'quote','Jerome, Ep. 125 to Rusticus (incl. 125.16 the solitary who lost his mind); Ep. 22.7 the desert torments','npnf206',None,"C14 add: 'Ep. 125 (source record, 0 citing records) for S8'.")
rec(w,['C3/S2'],'honest_limit','duration of punishment, which hal.dw.hell never states',None,None,"C3 must add: 'an honest_limit on duration'.",group='no_text')
rec(w,['C4/S3'],'honest_limit',"predestination: not Jerome's argument",None,None,"C4 hal S3: 'honest_limit'; fleet section lists hal for predestination dread.",group='no_text')
rec(w,['C4/S4'],'honest_limit','assurance as certainty',None,None,"C4 hal S4: 'assurance as certainty: honest_limit'.",group='no_text')
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 hal S6: 'honest_limit'.",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences (giving total, not tithed)',None,None,"C4 hal S7: 'indulgences honest_limit'.",group='no_text')
rec(w,['C4/S1'],'honest_limit',"'faith alone' as a record",None,None,"C4 fleet section lists hal among worlds missing the record (the witness holds grace and works together).",group='no_text')
rec(w,['C4/S1'],'quote (opponent\'s voice)','Pelagius, Letter to Demetrias (Latin vendored, mapped to pelagianism only); Commentary on Romans (Souter, unvendored)','pelagius-dem',None,"C4: 'hal, lpc and gallic build the controversy from the opponents' side only'. Map fix for Demetrias; acquisition for Romans.",group='acquire')
rec(w,['C14/S8'],'use_note / not_for check',"hal.quote.she-put-on-sackcloth (Ep. 77.3, Fabiola left a violent husband)",'npnf206',17449,"C14: for C14-16 'it must be used only as warmth after the Facilitator redirect, never as advice'; 'history, never counsel'. Confirm the record's guard says so.",fac=True,group='fix')

# ---------------- ijc ----------------
w='ijc'
rec(w,['C1/S3'],'demonstration','C-T demonstration (Leo, Sermons on the Passion)','npnf212',None,"C1: 'no atonement witness (C-T-02/03 unanswered)'.")
rec(w,['C1/S3'],'quote','Leo, Sermons on the Passion','npnf212',None,"C1 add: 'Leo's Passion sermons for S3'.")
rec(w,['C1/S7'],'quote','Eusebius, HE III.25 (recognised and disputed books)','npnf201',None,"C1 add: 'an HE III.25 quote'; 'the single most useful loaded text for C1-25 ... mapped to four worlds, rendered by none'.")
rec(w,['C3/S1','C3/S2'],'quote',"Leo, Sermon IX: 'Who then would not tremble at this doom of eternal torment? ... since this severity is only denounced in order that we may seek for mercy'",'npnf212',13585,"C3 must add: 'a Leo quote'; lines 13585-13587; 'states endless punishment and immediately turns it to mercy'.")
rec(w,['C3/S5'],'quote','Ambrose, De excessu fratris Satyri (prayer for the dead brother); On the Belief in the Resurrection','npnf210',819,"C3: 'Ambrose on his dead brother (npnf210) is unquoted'; S6 'No record beyond the creed'.",fac=True)
rec(w,['C4/S5'],'quote','Ambrose, Two Books Concerning Repentance (against the Novatians: there is repentance after baptism)','npnf210',33355,"C4: 'C4-06 is answered head-on by Ambrose's De paenitentia, vendored, unrendered.'")
rec(w,['C4/S4'],'quote','Nicaea canons 11-14 (the lapsed, penance, viaticum for the dying)','npnf214',None,"C4: 'The conciliar discipline of the lapsed is this world's own genre and is unrendered.'")
rec(w,['C4/S8'],'quote',"Ambrose, On the Holy Spirit (line 10428: the sin against the Spirit never forgiven); Concerning Repentance II.10 on 'sin unto death' (line 34155)",'npnf210',10428,"C4 ijc S8 unrendered.")
rec(w,['C4/S7'],'quote','Leo, Sermons on the Collections','npnf212',13503,"C4 ijc S7 thin: 'Leo: giving as duty'; indulgences honest_limit separately.")
rec(w,['C14/S2','C14/S8','C14/S3'],'quote or witness','Chrysostom, Letters to Olympias (consolation to a woman in despondency; no source record)','npnf109',None,"C14 add: 'the era's great text on despondency, no source record'. Needs a source record.",fac=True)
rec(w,['C14/S1'],'demonstration and quote','Chrysostom, Homilies on the Statues 1-21 (a city under terror, "why does God permit")','npnf109',None,"C14: 'S1 is LOADED only: no theodicy witness; the F6-P-02 cell is unforced here.'")
rec(w,['C14/S6'],'story','Palladius, Dialogue on the Life of Chrysostom (Theophilus and the Synod of the Oak: a bishop bullied out of office)','pall-dial',None,"C14 add for S6.")
rec(w,['C4/S3'],'honest_limit',"free will, election, predestination: 'every election hit is a bishop's'",None,None,"C4 ijc S3: 'Needs honest_limit'; fleet section lists ijc for predestination dread.",group='no_text')
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 ijc S6: 'honest_limit'.",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences',None,None,"C4 ijc S7: 'Indulgences honest_limit.'",group='no_text')
rec(w,['C4/S4'],'honest_limit',"'assurance' as felt certainty",None,None,"C4 fleet section: all patristic worlds.",group='no_text')
rec(w,['C3/S1','C3/S2','C3/S3','C3/S4','C3/S5','C3/S6','C3/S7','C3/S8'],'decision','whether this world answers afterlife questions at all',None,None,"C3 must add: 'a decision whether this world answers afterlife questions at all'.",group='no_text')

# ---------------- lpc ----------------
w='lpc'
rec(w,['C1/S1','C1/S3','C1/S8'],'demonstration','C-I, C-T, C-P demonstrations',None,None,"C1: 'Three demonstrations in the whole world, none for C cells.'")
rec(w,['C1/S6'],'quote',"Augustine, De Trinitate VIII.4.7 'the countenance of our Lord Himself in the flesh is variously fancied'",'npnf103',10455,"C1: 'the one patristic text that answers what did he look like by saying nobody knows'.")
rec(w,['C1/S7'],'quote','Augustine, Harmony of the Gospels I; De doctrina christiana II.8 canon list (npnf102)','npnf106',None,"C1 add: 'quotes from ... Harmony I'; S7 LOADED only.")
rec(w,['C1/S3'],'quote','Augustine, Enchiridion 33-41 (Mediator, sacrifice)','npnf103',None,"C1 add: 'Enchiridion 33-41'.")
rec(w,['C3/S6'],'quote',"Cyprian, De mortalitate 26: 'There a great number of our dear ones is awaiting us, and a dense crowd of parents, brothers, children, is longing for us'",'anf05',47279,"C3: reunion passage (C3-12) confirmed in context, lines 47279-47280, unrendered; the force record names De Mortalitate but says nothing of its afterlife content.")
rec(w,['C3/S7'],'quote','Cyprian to Fidus (Ep. 58): infants ought not to be kept from baptism until the eighth day','anf05',35892,"C3: infants vendored and confirmed; 'this is the world most likely to be asked' C3-15.",fac=True)
rec(w,['C3/S3','C3/S2'],'quote',"Augustine, City of God XXI.17: the 'tender-hearted Christians' who decline to believe that any shall suffer eternally; 'Origen was even more indulgent'",'npnf102',43953,"C3: 'Augustine's misericordes are the natural ground for C3-07 and C3-17'; XXI.17-27 defends eternity of punishment (S2).")
rec(w,['C3/S5'],'quote','Augustine, Enchiridion 69: whether some believers pass through a kind of purgatorial fire (open question)','npnf103',22300,"C3 must add; lines 22300-22312.",fac=True)
rec(w,['C3/S5'],'quote',"Augustine, Enchiridion 110: 'thank-offerings for the very good, propitiatory offerings for the not very bad'",'npnf103',23576,"C3 must add; lines 23570-23582.",fac=True)
rec(w,['C3/S5'],'quote',"Monica: 'remember me at the Lord's altar, wherever you be' (Confessions IX)",'npnf101',14194,"C3 must add.",fac=True)
rec(w,['C3/S5'],'quote','Augustine, On Care to Be Had for the Dead','npnf103',43492,"C3 lpc S5 source hits: confirmed in context, none rendered.",fac=True)
rec(w,['C3/S7'],'quote','Augustine, City of God I.17, Of Suicide Committed Through Fear of Punishment or Dishonor','npnf102',2426,"C3 must add; R-20 'the most pastorally loaded questions in the cluster, and this is the world most likely to be asked them'.",fac=True)
rec(w,['C3/S7'],'contested_claim',"infants: Cyprian's practice (Ep. 58) against Augustine's 'mildest condemnation' (De peccatorum meritis I)",'npnf105',2558,"C3 must add: 'a contested_claim on infants'.",fac=True)
rec(w,['C3/S1','C3/S2'],'quote','Cyprian, Ep. 54 (the eternal punishments of Gehenna; Antichrist); City of God XXI','anf05',35191,"C3: '330 records and not one on hell, judgment or the dead'; richest vendored material in the fleet.")
rec(w,['C3/S4'],'quote',"Augustine: the 'second death' is not annihilation (City of God XIII.2, XXI.3; Enchiridion)",'npnf103',2316,"C3 lpc S4: 'Unrendered.'")
rec(w,['C3/S8'],'quote','Augustine, City of God XX (the thousand years)','npnf102',46,"C3 lpc S8: 'No record.'")
rec(w,['C4/S4'],'quote',"Augustine, On Rebuke and Grace 40: 'No One is Certain and Secure of His Own Predestination and Salvation'",'npnf105',20590,"C4: 'the sharpest patristic answer to C4-19 (no, you cannot know) is vendored and unrendered'.")
rec(w,['C4/S2'],'quote','Augustine, On the Merits and Forgiveness of Sins and on Infant Baptism','npnf105',541,"C4: 'No record states inherited guilt itself in Augustine's words; the fullest text in the whole Library is vendored here.'")
rec(w,['C4/S6'],'quote','Augustine, Letter 102 to Deogratias, question 2: why Christ came so late and what of those before him','npnf101',41687,"C4 lpc S6: 'Unrendered.' Also City of God XVIII.47.")
rec(w,['C4/S7','C4/S8'],'quote','Augustine, Enchiridion 69-70 (alms do not buy licence to sin); 83 (despising God\'s mercy is the sin against the Holy Ghost)','npnf103',22747,"C4 lpc add.")
rec(w,['C14/S3'],'quote','Augustine, Enarrationes in Psalmos on Pss. 21/22, 41/42, 87/88 and "how long, Lord" (the totus Christus lament)','npnf108',None,"C14: 'S3 is LOADED at high value ... the richest lament text in the corpus and no record touches it' (source record has 0 citing records).")
rec(w,['C14/S1'],'quote',"Cyprian, De mortalitate / 'On the Mortality' (why the plague takes Christians too)",'anf05',None,"C14 add; Latin also vendored (cyprian_de-mortalitate-lat_hartel1868-csel3-tei.txt).")
rec(w,['C14/S2'],'quote','Augustine, Ep. 130 to Proba on prayer; Confessions IV.4-12 (grief for the friend) and IX.12 (Monica\'s death)','npnf101',None,"C14 add; 'lpc.source.augustine-confessions exists but no grief record'.")
rec(w,['C4/S1'],'honest_limit',"'faith alone' as a record (De fide et operibus is Latin only)",None,None,"C4 fleet section lists lpc among worlds missing the record.",group='no_text')
rec(w,['C4/S4'],'honest_limit',"'assurance' as felt certainty",None,None,"C4 fleet section: all patristic worlds (On Rebuke and Grace 40 is the doctrinal ground).",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences themselves (redemptive almsgiving is rendered)',None,None,"C4 lpc S7: 'Indulgences themselves: honest_limit'.",group='no_text')
rec(w,['C4/S1'],'quote (Latin only; no PD English)','Augustine, De fide et operibus (James 2 head-on)','aug-fide-op',None,"C4: 'C4-20 (James) has a dedicated Augustine treatise vendored in Latin only'; no public-domain English exists.",group='acquire')
rec(w,['C4/S8'],'retrieve_when fix','lpc.quote.pardon-through-a-wicked-clergyman (Sermon 71 on Matt 12:32) is indexed only for the wicked-minister question','npnf106',13008,"C4: 'Add a retrieve_when for the unforgivable-sin question, or a second quote from the same sermon' (whole sermon at line 12412).",group='fix')

# ---------------- pahc ----------------
w='pahc'
rec(w,['C1/S2','C1/S6'],'quote',"Justin, Dialogue with Trypho 48-49 ('some of your race say he was a man'); the Dialogue on Jesus as Jew",'anf01',None,"C1 add: 'Trypho quote'; 'the fleet's one period-native prophet or God exchange; loaded, unrendered'.")
rec(w,['C1/S7'],'quote',"Justin, 1 Apology 66-67 ('memoirs ... called Gospels'); Irenaeus AH III.11.8 (line 41046); Papias (HE III.39)",'anf01',None,"C1 add: 'Justin 1 Apol 66 quote'; these are 'the right texts' for S7 in place of the Athanasius quote.")
rec(w,['C1/S6'],'quote','Justin, Dialogue 14, 88; 1 Apology 52 (without beauty); Clement Paed. III.1 (anf02 line 24488); Tertullian De carne Christi 9 (anf03 lines 27282, 28082)','anf01',None,"C1: 'Three loaded period texts on appearance; none rendered.'")
rec(w,['C3/S4','C3/S5'],'quote',"Justin, Dialogue 5: 'The soul is not in its own nature immortal'",'anf01',17704,"C3 must add: 'the fleet's only real ground for C3-08'; also Tatian Or. 13 (anf02), Irenaeus AH II.34.")
rec(w,['C3/S5'],'quote','Hermas, Similitude 9.16: the apostles preaching and baptising the dead; "The seal, then, is the water"','anf02',4660,"C3 must add; lines 4660-4672.",fac=True)
rec(w,['C3/S8'],'story','Didache 16 or Justin, Dialogue 80 (the millennium)','anf07',1802,"C3 must add: 'a story from Didache 16 or Justin Dial. 80 for the millennium'; Papias also vendored (anf01).")
rec(w,['C3/S1'],'quote','2 Clement 17; Ignatius Eph. 16; Mart. Pol. 11; Apocalypse of Peter (anf09 line 12618, "I will show unto thee the lake of fire")','anf01',None,"C3 pahc S1 partial: the Two Ways not_for forbids using it as an afterlife threat; these are vendored and unquoted.")
rec(w,['C3/S2'],'quote',"Justin, Dialogue 130: 'consumed by the worm and unquenchable fire, remaining immortal'",'anf01',24766,"C3 pahc S2: 'No record.'")
rec(w,['C4/S5'],'quote',"Hermas, Mandate 4.3 'there is but one repentance to the servants of God' (anf02 line 1933); Tertullian, On Repentance 7-9 (anf03 line 55926)",'anf02',1933,"C4: 'The STARTER question (C4-06) is this world's own; the Hermas sentence is vendored and not yet a quote record.'")
rec(w,['C4/S1'],'quote','1 Clement 32-34 (justified by faith, yet zealous for good works)','anf01',None,"C4: '1 Clement 32-33 is the earliest text that holds both halves in one breath; cheap to render.'")
rec(w,['C4/S3'],'quote','Justin, 1 Apology 43 (free will against fate); Dialogue 141 (line 25255)','anf01',17001,"C4: 'Unrendered; a quote record would carry C4-09.'")
rec(w,['C4/S7'],'quote','Hermas, Similitude 2 (elm and vine, anf02 line 2938); 2 Clement 16.4; Didache 4.6 (redemptive almsgiving)','anf02',2938,"C4 pahc S7: 'redemptive almsgiving unrendered'.")
rec(w,['C14/S3','C14/S8'],'quote',"Hermas, Mandate X: sadness 'the sister of doubt and anger'",'anf02',None,"C14 add for S3/S8.")
rec(w,['C14/S7'],'quote or story','Hermas, Similitudes VIII-IX (classes of apostates and of those who returned)','anf02',None,"C14 add for S7.")
rec(w,['C4/S2','C3/S7'],'honest_limit','infants: silence is the finding',None,None,"C4 pahc S2: 'Silence is the finding: honest_limit.' C3: infants nothing (Tertullian De baptismo 18 is outside the window's own voice).",fac=True,group='no_text')
rec(w,['C4/S4'],'honest_limit','assurance as certainty',None,None,"C4 pahc S4: 'Assurance as certainty: honest_limit.'",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences',None,None,"C4 pahc S7: 'Indulgences honest_limit'.",group='no_text')
rec(w,['C4/S1'],'honest_limit',"'faith alone' as a record",None,None,"C4 fleet section lists pahc among worlds with nothing on the faith-alone question.",group='no_text')
rec(w,['C4/S3'],'honest_limit',"'predestination, did it frighten you'",None,None,"C4 fleet section lists pahc.",group='no_text')
rec(w,['C14/S6'],'honest_limit','abuse of children and cover-up: nothing; Didache 2.2 and Barnabas 19.5 (the prohibition of paidophthoria) are the one adjacent text','anf07',None,"C14 add: 'an honest_limit on abuse, with Didache 2.2 as the one adjacent text'.",fac=True,group='no_text')
rec(w,['C1/S5'],'retrieve_when fix',"existence lines on pahc.quote.tacitus-hatred-against-mankind, the Pliny and Lucian records ('did he exist')",'tacitus',None,"C1: 'no record's retrieve_when says did he exist; the Tacitus quote retrieves on persecution'.",group='fix')
rec(w,['C1/S7'],'source/record fix','pahc.quote.appointed-to-be-read quotes Athanasius\'s Festal Letter 39 (367) inside a 70-200 world: replace or re-home','npnf204',None,"C1 add: 'replace or re-home the Athanasius quote'; 00-summary drift.",group='fix')
rec(w,['C3/S6'],'retrieve_when fix',"pahc.quote.polycrates-to-victor ('great luminaries ... shall rise again') is filed under F3-I, so retrieval on an afterlife question is not guaranteed",None,None,"C3 pahc S6.",group='fix')
rec(w,['C4/S6'],'duplicate fix','pahc.quote.justin-reasonable-livers and pahc.quote.those-who-lived-reasonably-are-christians carry the same Justin sentence',None,None,"C4 findings; 00-summary.",group='fix')

# ---------------- rzg ----------------
w='rzg'
rec(w,['C4/S1'],'quote','Calvin, Institutes III.11 Of Justification by Faith; Second Helvetic XV-XVI; Heidelberg 60-64','calvin2',13893,"C4: 'BIGGEST HOLE: the Reformed world has no record on justification by faith at all'.")
rec(w,['C1/S3'],'quote',"Calvin, Institutes II.16.5-7, 10 (penal substitution in its native language, 'in our place')",'calvin1',None,"C1: 'The one world whose own idiom is in our place has it loaded and unrendered.' Institutes Book II is in Beveridge vol. 1; confirm the volume.")
rec(w,['C1/S1','C1/S3','C1/S4'],'quote','Second Helvetic Confession XI (Christ; his death; resurrection)','schaff-helv',None,"C1 add: 'Second Helvetic XI quotes'.")
rec(w,['C1/S1'],'quote','Zwingli, Sixty-Seven Articles 2-5','zwingli-sel',None,"C1 add: 'a C-I quote from the Sixty-Seven Articles 2-5'; S1 has one witness, no quote.")
rec(w,['C1/S2'],'quote','Calvin, Institutes I.13 (Trinity; against Servetus); II.14; Second Helvetic III','calvin1',None,"C1: 'no divinity record'; S2 LOADED.")
rec(w,['C1/S4'],'quote','Calvin, Institutes III.25 (the final resurrection); II.16.13','calvin2',None,"C1: 'no resurrection record'.")
rec(w,['C1/S7'],'quote','Second Helvetic I-II (canon of Scripture)','schaff-helv',None,"C1 rzg S7 LOADED: the record 'reading straight through Matthew' does not say which gospels.")
rec(w,['C3/S5','C4/S7'],'quote','Calvin, Institutes III.5 Indulgences and Purgatory (prayer and oblation for the dead)','calvin2',11000,"C3 must add; C4: nothing on indulgences though III.5 is vendored.",fac=True)
rec(w,['C3/S7'],'quote',"Calvin, Institutes IV.16, heading 'Error of those who adjudge all who die unbaptized to eternal destruction'",'calvin3',15757,"C3 must add: 'Calvin's own heading is the answer to C3-15/16 and is unrendered'.",fac=True)
rec(w,['C3/S5'],'quote',"Zwingli on purgatory: Commentary on True and False Religion (vol. 3, 'Purgatory' at line 332); Sixty-Seven Articles, purgatory 'man's invention' (zwingli_selected-works line 2530)",'zwingli3',332,"C3 must add: 'Zwingli on purgatory'; 'purgatory rejected is fully vendored in both cities' own words; nothing rendered'.",fac=True)
rec(w,['C3/S1','C3/S5'],'quote',"Geneva Catechism on 'descended into hell' (pains of hell on the Cross)",'geneva-cat',900,"C3 must add: 'Geneva Catechism on the descent'.")
rec(w,['C3/S1','C3/S2'],'quote',"Calvin, Institutes: 'doomed to eternal punishment, that fire is prepared for them' (vol. 1 line 13919); 'hell and the horrors of eternal death' (vol. 2 line 3044)",'calvin1',13919,"C3 rzg S1: 'Nothing in records says what Zurich or Geneva taught about hell'; the one F6-T record is a guard.")
rec(w,['C3/S8'],'quote','Calvin, Institutes IV.7 (the papacy as Antichrist, vol. 3 line 1765); III.25.5 against the chiliasts (vol. 2 line 2000)','calvin3',1765,"C3 rzg S8: 'No record.'")
rec(w,['C4/S5'],'demonstration or witness (F4-T)',"'born again' / regeneration as a distinct Reformed doctrine: Institutes III.3-4 (vol. 2 line 4069); IV.15-16",'calvin2',4069,"C4: 'no born again record although regeneration is a distinct Reformed doctrine'; F4-T demos exist only in don and hal.")
rec(w,['C4/S8'],'quote',"Zwingli, 'The Sin Against the Holy Ghost' (Commentary on True and False Religion, section 11); Institutes III.3.22 (vol. 2 line 7014)",'zwingli3',7958,"C4: nothing on the unforgivable sin though vendored.")
rec(w,['C4/S2'],'witness or quote','Calvin, Institutes II.1 (original sin; inherited guilt itself)','calvin1',None,"C4: 'Inherited guilt itself (C4-02) has no record; the infant-baptism half does.'")
rec(w,['C4/S3'],'quote',"Zwingli, 'On Election' (1527), working through Romans 8-9",'zwingli-sel',None,"C4 rzg S3 note (Romans 9 / C4-21).")
rec(w,['C14/S1'],'quote',"Calvin, Institutes III.viii 'Of bearing the cross'; I.xvi-xviii (providence)",'calvin2',None,"C14 add; 'only a providence term is rendered; the pastoral texts on suffering are loaded and unused'. I.xvi-xviii in vol. 1.")
rec(w,['C14/S1','C14/S3'],'quote','Beza, Job Expounded (1589)','beza-job',None,"C14 add; rzg.source.beza-job-expounded has 0 citing records.")
rec(w,['C14/S1','C14/S2','C14/S8'],'quote','Calvin, letters of consolation (to the prisoners of Lyon 1553; to bereaved nobles), Bonnet vols. 1, 2, 4','bonnet2',None,"C14 add: 'Calvin's consolation letters'; 'grief has no record at all'.")
rec(w,['C14/S2'],'quote','Calvin, Institutes III.xx.51-52 (persevering when God seems not to hear)','calvin2',None,"C14 rzg S2 loaded_extra; F4-P-03 unforced in every world.")
rec(w,['C14/S6'],'witness, honest_limit or demonstration','Servetus (1553): Rilliet, Calvin and Servetus; Calvin\'s letters on Servetus 1553 (Bonnet vol. 2)','rilliet',None,"C14: 'Servetus, the hardest true thing about Geneva, appears in no witness, limit or demo' though the text is vendored and mapped.")
rec(w,['C14/S7'],'quote','Calvin, letters against the Nicodemites (quiet conformers), Bonnet','bonnet1',None,"C14 rzg S7 loaded_extra; S7 is a limit with no case and no recorded words.")
rec(w,['C14/S5'],'quote or story','Ordonnances ecclesiastiques (French, 1735 printing)','ordonnances',None,"C14: 'Were your people judgmental is this world's defining question and it is answered only as doctrine plus an honest limit; no case, no recorded words.' Confirm the printing is the 1541 text (see fix).")
rec(w,['C4/S6'],'honest_limit (unless the Exposition of the Faith is vendored)','the unevangelised; Zwingli\'s saved pagans',None,None,"C4 fleet section: 'People who never heard: ... rzg (unless Zwingli's Exposition is vendored)'.",group='no_text')
rec(w,['C3/S6','C3/S7','C4/S3','C4/S6'],'quote','Zwingli, Exposition of the Faith (Hercules and Socrates in heaven); Sermon on Providence (Latin Works vol. 2)',None,None,"C3/C4: 'in the unvendored Latin Works vol. 2'. Needs acquisition.",group='acquire')
rec(w,['C3/S4','C3/S5'],'quote','Calvin, Psychopannychia (against soul-sleep)',None,None,"C3 rzg S4: 'Psychopannychia (OTHER) is the direct text.' Needs acquisition.",fac=True,group='acquire')
rec(w,['C4/S3','C4/S1'],'quote','Calvin, Concerning the Eternal Predestination of God (Cole 1856); Bullinger, Decades I.4-6; Beza, Tabula praedestinationis',None,None,"C4 identified/other for rzg; the Latin of Calvin's treatise is vendored (calvin_opera-omnia-vol8 line 170).",group='acquire')
rec(w,['C14/S1','C14/S2','C14/S3','C14/S7'],'quote','Calvin, Commentary on the Psalms; Sermons on Job; Bonnet vol. 3; Zwingli Pestlied; Excuse aux Nicodemites',None,None,"C14 other list for rzg (all PD except no PD English for the Nicodemite tract).",group='acquire')
rec(w,['C14/S4','C14/S5','C14/S6','C14/S7','C3/S7','C4/S5'],'story (blocked)','Registers of the Consistory of Geneva (Kingdon 2000)',None,None,"C14: 'what ordinary doubters said when examined'; C3: where Geneva's practice on suicide would show. In copyright; cannot be vendored.",fac=True,group='acquire')
rec(w,['C1/S1','C1/S3'],'canon tag fix + demonstration',"rzg.demo.why-we is tagged canon_question_id c-t-03 but its exchange is 'what are you' (C16); rzg has no Jesus demonstration",None,None,"C1 add: 'C-I/C-T demos'; 00-summary drift.",group='fix')
rec(w,['C3/S7'],'check',"the Zwingli hit 'nor the unbaptized infants are under condemnation' (vol. 3 line 1523) is the editor Heller's summary, not Zwingli's words",'zwingli3',1523,"C3 caution: do not quote it as Zwingli.",fac=True,group='fix')
rec(w,['C14/S5'],'source-record fix','rzg.source.ecclesiastical-ordinances-1541 is registered unvendored while the 1735 French printing is mapped; check it is the 1541 text','ordonnances',None,"C4 findings; C14 identified.",group='fix')

# ---------------- syr ----------------
w='syr'
rec(w,['C1/S2'],'quote',"Aphrahat, Demonstration XVII 'Of Christ the Son of God', written against the Jewish objection 'you call a man God'",'npnf213',None,"C1 add: 'Dem. XVII quote for the outsider'; 'the fleet's best period answer to R-24 and only its opening line is rendered'.")
rec(w,['C1/S5'],'quote',"Mara bar Serapion: 'the Jews by the murder of their Wise King'",'anf08',69289,"C1 add: 'Mara bar Serapion quote for S5'; a Syriac-milieu outside witness, mapped and unrendered.")
rec(w,['C3/S5'],'quote','Aphrahat, Demonstration VIII Of the Resurrection of the Dead (the sleep of the soul until the resurrection)','npnf213',26376,"C3 must add: 'Dem. VIII quote'; 'the distinctive Syriac interim-state teaching and is unrendered'.",fac=True)
rec(w,['C3/S1'],'quote with a careful not_for',"Ephrem's Testament: 'may he be cast into Gehenna of fire!' (a will's curse on a rich burial, not doctrine)",'npnf213',11642,"C3: 'they would change tone, not teaching, and need a careful not_for if quoted'; lines 11642-11644.")
rec(w,['C4/S3'],'quote','Ephrem, First Discourse to Hypatius: the Freewill argument against Bardaisan and Mani','ephrem-prose',232,"C4: 'Ephrem's defence of free will against fate is vendored and unrendered'; lines 232-295.")
rec(w,['C14/S3','C14/S1'],'quote','Ephrem, Nisibene Hymns I-III: the city pleading with God under siege','npnf213',None,"C14 add: 'lament in the city's own mouth'; source cited by 14 records, none a lament quote.")
rec(w,['C14/S7'],'quote','Aphrahat, Demonstration VII On Penitents in full (the one who fell in the contest received back without exposure)','hallock',None,"C14 add: 'Demonstration VII On Penitents in full for S7'.")
rec(w,['C1/S6'],'honest_limit','appearance',None,None,"C1 add: 'an honest_limit on appearance'.",group='no_text')
rec(w,['C3/S3','C3/S4'],'honest_limit','restoration and annihilation: nothing in Ephrem or Aphrahat as vendored',None,None,"C3 must add.",group='no_text')
rec(w,['C4/S2'],'honest_limit','infants',None,None,"C4 syr S2: 'Infants: nothing; honest_limit.'",fac=True,group='no_text')
rec(w,['C4/S4'],'honest_limit','assurance',None,None,"C4 syr S4: 'assurance honest_limit'.",group='no_text')
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 syr S6: 'honest_limit'.",group='no_text')
rec(w,['C4/S7'],'honest_limit','indulgences',None,None,"C4 syr S7: 'Indulgences honest_limit.'",group='no_text')
rec(w,['C4/S8'],'honest_limit','the unforgivable sin',None,None,"C4 syr S8: 'honest_limit'.",group='no_text')
rec(w,['C4/S1'],'honest_limit',"'faith alone' as a record (not_for already bars 'faith alone suffices')",None,None,"C4 fleet section lists syr.",group='no_text')
rec(w,['C4/S3'],'honest_limit',"'predestination, did it frighten you'",None,None,"C4 fleet section lists syr.",group='no_text')
rec(w,['C3/S2','C3/S6'],'quote','Ephrem, Hymns on Paradise (the geography of Paradise; reunion; the fate of the departed)',None,None,"C3: 'nothing states duration ... Hymns on Paradise (OTHER) carry the Syriac picture'; reunion OTHER. Lamy Latin PD; Brock in copyright.",group='acquire')
rec(w,['C1/S7'],'quote','Old Syriac Gospels (Burkitt 1904); Hill, Earliest Life of Christ (1894)',None,None,"C1 other list for syr S7 (already the best world for C1-25).",group='acquire')
rec(w,['C3/S7'],'not_for check',"the anti-Jewish polemic records (syr.quote.aphrahat-anti-jewish-frame, syr.term.anti-jewish-polemic) hold the polemic without a damnation verdict; C3-26 ('all Jews damned?') lands on them",None,None,"C3: 'check their not_for before relying on that'.",group='fix')

# ---------------- witt ----------------
w='witt'
rec(w,['C1/S1','C1/S8'],'demonstration','C-I demonstration (and C-P)',None,None,"C1: 'no C-I or C-P demo'.")
rec(w,['C1/S1','C1/S3'],'quote',"Augsburg Confession Art. III ('a sacrifice ... for all actual sins')",'ac',None,"C1 add: 'Augsburg Art. III quote'.")
rec(w,['C3/S5'],'quote',"Apology XXIV: 'the ancients speak of prayer for the dead, which we do not prohibit'",'apology',9481,"C3 must add: 'the nuance C3-10 needs and is unquoted'.",fac=True)
rec(w,['C3/S4'],'quote',"Luther, Defense of the Articles (1521) on the soul dying with the body / Lateran V's decree",'luther-v2',3362,"C3 witt S4 partial: 'the clause rejects an end to punishment, not annihilation by name. Luther's 1521 remark on the soul's immortality decree is vendored.'")
rec(w,['C4/S5'],'quote',"Augsburg Confession XII: remission 'whenever they are converted ... The Novatians also are condemned, who would not absolve such as had fallen after Baptism'",'ac',339,"C4: 'C4-06 (one chance) is answered verbatim by AC XII; add the quote.' Lines 339-355.")
rec(w,['C4/S4'],'quote',"Augsburg Confession XII condemns 'the Anabaptists, who deny that those once justified can lose the Holy Ghost'",'ac',355,"C4: 'C4-07 (can you lose it): the confession says yes, in a sentence not yet rendered.'")
rec(w,['C4/S1'],'quote','Apology IV on James 2 (C4-20)','apology',None,"C4: 'Luther's preface to James is not in the library; the Apology IV's handling of James 2 is vendored.'")
rec(w,['C14/S1','C14/S2','C14/S8'],'quote','Luther, The Fourteen of Consolation (1520)','luther-v1',59,"C14: 'the one text written for a suffering person ... vendored, has a source record and 0 citing records. Add it.'")
rec(w,['C14/S1','C14/S3','C14/S4','C14/S8'],'quote',"Luther, Table Talk, 'Of Temptation and Tribulation' (Anfechtung)",'table-talk',None,"C14 add; 'Anfechtung is the world's own word for despair and is rendered only as the catechism's three temptations'.")
rec(w,['C14/S1','C14/S8'],'quote',"Luther, 'Aus tiefer Not' (and 'Mitten wir im Leben sind')",'luther-hymns',None,"C14 add.")
rec(w,['C14/S7'],'quote','Large Catechism preface on negligent pastors and people','large-cat',None,"C14 witt S7 loaded_extra; 'drift is reported by the founder's complaints only'.")
rec(w,['C3/S7'],'check (quote)',"Luther, Table Talk on suicides 'overcome by the devil' (not located by line)",'table-talk',None,"C3: 'Suicide (R-20): Table Talk is vendored and unread for this.'",fac=True)
rec(w,['C4/S6'],'honest_limit','the unevangelised',None,None,"C4 witt S6: 'honest_limit'.",group='no_text')
rec(w,['C4/S8'],'honest_limit',"the Matt 12 question itself; 'mortal/venial is rendered nowhere' (luther_works-v1 line 618; Large Catechism line 1014)",None,None,"C4 witt S8.",group='no_text')
rec(w,['C1/S2','C1/S6'],'quote','Luther, That Jesus Christ Was Born a Jew (1523)',None,None,"C1 add: 'the 1523 treatise (German PD)'; the single IDENTIFIED cell in the C1 table.",group='acquire')
rec(w,['C1/S7'],'quote','Luther, Preface to the New Testament (1522)',None,None,"C1: 'Luther's 1522 preface ranks John first and is the natural text'; German PD, Holman English from 2028.",group='acquire')
rec(w,['C1/S3'],'quote','Luther, Commentary on Galatians 3:13 (the penal-substitution locus)',None,None,"C1 other list for witt S3.",group='acquire')
rec(w,['C3/S7'],'decision (then quote)','Luther, letter to Hans von Rechenberg (1522); Ein Trost den Weibern (1542)',None,None,"C3 must add: 'a decision on the Rechenberg letter'; the confession's words on the unbaptised 'are rendered without Luther's pastoral softening'.",fac=True,group='acquire')
rec(w,['C3/S5'],'quote','Luther, A Sermon on Preparing to Die (1519)',None,None,"C3: 'not in the vendored Holman vol. 1 (OTHER)'; confirm (contents line 6314 names it).",group='acquire')
rec(w,['C4/S3','C4/S1'],'quote or contested_claim','Erasmus, De libero arbitrio (1524); Melanchthon, Loci communes (1521)',None,None,"C4 identified/other for witt.",group='acquire')
rec(w,['C14/S6','C14/S7'],'quote or story','Saxon visitation protocols; Melanchthon, Instructions for the Visitors (1528)',None,None,"C14: 'the bishop/visitation accountability question is only identified'; German PD in Sehling and WA 26.",group='acquire')
rec(w,['C14/S2','C14/S8'],'quote','Luther\'s letters of consolation (Currie 1908; Smith and Jacobs 1913/1918)',None,None,"C14 other list for witt S2/S8.",group='acquire')
rec(w,['C4/S3'],'term fix + source-record fix',"witt.term.free-will says the library carries no developed predestination doctrine, but Formula of Concord XI is in the vendored and mapped Jacobs 1911 Book of Concord (lines 25390, 27478); witt.source.book-of-concord is registered unvendored",'boc',25390,"C4 findings: 'Fix the record or the map.'",group='fix')


# =====================================================================
# 16-CLUSTER EXTENSION: acquisition rows from C2, C5-C13, C15, C16
# (merge helpers: one work, one row; cells from every cluster)
# =====================================================================
T.update({
 'npnf202': 'npnf202_socrates-sozomen-ecclesiastical-histories.xml',
 'npnf110': 'npnf110_chrysostom-homilies-matthew.xml', 'npnf111': 'npnf111_chrysostom-homilies-acts-romans.xml',
 'npnf113': 'npnf113_chrysostom-homilies-galatians-philemon.xml', 'npnf114': 'npnf114_chrysostom-homilies-john-hebrews.xml',
 'tyconius': 'tyconius_liber-regularum_burkitt1894.txt', 'odes-hm': 'odes-of-solomon_harris-mingana1920.txt',
 'collatio': 'augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt',
 'ammianus': 'ammianus-marcellinus_roman-history_yonge1862.txt', 'egeria': 'egeria_pilgrimage-of-etheria_mcclure-feltoe1919.txt',
 'marot': 'marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt', 'neale-lit': 'liturgies-eastern_mark-james-clement-chrysostom-basil-malabar_neale-1870s.txt',
 'julian-letters': 'julian_letters-1-73_wright1923.txt', 'gerlach': 'gerlach_tage-buch-deu_1674.txt', 'lucaris': 'lucaris_lettres-anecdotes-fra_amsterdam1718.txt',
 'jeremias': 'acta-et-scripta-wirtembergensium_jeremias-ii-correspondence-lat_1584.txt', 'paulinus-amb': 'paulinus-milan_vita-ambrosii_kaniecka1928.txt',
 'ac-file': 'melanchthon_augsburg-confession_anon-pg275.txt', 'sc': 'luther_small-catechism_smith1994.txt',
 'basil-address': 'basil_address-to-young-men_padelford1902.txt', 'paradise-v1': 'palladius_paradise-v1-syriac_budge1907.txt',
 'perpetua': 'perpetua-scillitan-martyrs-lat-grc_robinson1891.txt', 'nyssa-macrina': 'gregory-nyssa_life-of-macrina_clarke1916.txt',
 'arndt': 'arndt_true-christianity_boehm-schaeffer1868.txt', 'hefele3': 'hefele_history-of-the-councils-v3-431-451_clark1883.txt',
 'diogn': 'pseudo-justin_epistle-to-diognetus-grc_lake1917.txt', 'enarr-lat': 'augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt',
 'consensus-tig': 'calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt',
})

def TX(fn):
    return 'cic/texts/' + fn
NS = 'not stated in report'
SEARCH_DIR = None

MERGE_LOG = []
A_OLD_COUNT = len(A)
def addc(substr, cells, note='', ident=None):
    MERGE_LOG.append((substr, list(cells)))
    hits = [a for a in A if substr.lower() in a['work'].lower()]
    assert len(hits) == 1, (substr, len(hits))
    a = hits[0]
    a['cells'] = sorted(set(a['cells']) | set(cells))
    if note:
        a['notes'] = (a['notes'] + ' ' + note).strip()
    if ident:
        a['identified_as'] = list(a['identified_as']) + (ident if isinstance(ident, list) else [ident])

# ---- a row the 4-cluster list carried that a later report found already vendored ----
A = [a for a in A if not a['work'].startswith('Liber Regularum')]
A_OLD_COUNT = len(A)   # rows from the 4-cluster list; rows after this index are new in the 16-cluster list
STALE_ACQ_MOVED = [dict(work='Liber Regularum (the Donatist Book of Rules; Rule VII on the devil and his body)',
    file=P('tyconius'), line=None, cells=['don:C3/S3', 'don:C3/S8', 'don:C5/S2'],
    note='Listed as an acquisition in the 4-cluster list (from C3). The C5 report found it vendored (tyconius_liber-regularum_burkitt1894.txt, Latin) and unread, and calls Tyconius the Donatist world\'s only interpreter. Moved out of the acquire list. English (Babcock 1989) is in copyright.')]

# ---- merges into rows that already exist ----
addc('Registers of the Consistory', ['rzg:C6/S1', 'rzg:C6/S8', 'rzg:C13/S6'],
     'C6: the ordinary practice of the consistory; C13: sorcery and the plague-spreaders of 1545. Egli, Actensammlung (1879) and Calvini Opera 21 are the public-domain route for part of the C13 material.')
addc('Donatist martyr acts', ['don:C6/S1', 'don:C7/S2', 'don:C9/S1', 'don:C9/S2', 'don:C13/S5'],
     'C7, C9, C13: the Acta Saturnini (Abitinian martyrs: "we cannot live without the dominicum") are registered unvendored as don.source.acta-saturnini-abitinian-martyrs although the Latin is vendored in PL 8 (lines 1781, 2974); C9 and C13 name the cult at the graves.',
     ['don.source.acta-saturnini-abitinian-martyrs (kind: unvendored; Latin vendored)'])
addc('Le dossier du donatisme', ['don:C6/S1'])
addc('Loca sanctorum Africae', ['don:C7/S7', 'don:C13/S5'])
addc('Fidei expositio', ['rzg:C2/S3', 'rzg:C11/S5', 'rzg:C11/S6', 'rzg:C11/S8'],
     'C2: the Trinity in the Exposition; C11: Socrates, Hercules, Theseus and Cato among the saved. Latin Works vol. 2 (Hinke 1922) is the one Zwingli volume not vendored.')
addc('Dass Jesus Christus', ['witt:C2/S2', 'witt:C11/S1'], 'C2 also names Bibliander, Machumetis ... (Basel 1543) with Luther\'s preface.')
addc('Apophthegmata Patrum', ['desert:C13/S2'], 'C13: Macarius and the skull; Moses and the demons; Theodore of Pherme on the demons.')
addc('Codex Theodosianus in English', ['cappadocian:C9/S5', 'ijc:C11/S1', 'ijc:C11/S3', 'don:C13/S6', 'ijc:C13/S6'],
     'C11: CTh 16.8 (Jews) and 16.10 (pagans); C13: IX.16 (magic, divination) and XVI.5. Pharr (Princeton 1952) is in copyright; the Latin (Mommsen-Meyer 1905) is vendored.')
addc('Homilies on Leviticus 8.3', ['alx:C7/S1'], 'C7: also Homilies on Luke XIV (infants baptised by the apostles\' tradition).')
addc('Saxon visitation protocols', ['witt:C6/S8', 'witt:C10/S6', 'witt:C12/S3'],
     'C12 adds Sehling, Die evangelischen Kirchenordnungen (German public domain) as the route to the ordinary parish.')
addc('The Decades', ['rzg:C2/S2', 'rzg:C13/S5'], 'C13: Decades IV-V on angels, devils, saints and images.')
addc('Vorrede auf das Neue Testament', ['witt:C5/S1', 'witt:C5/S5', 'witt:C5/S6'],
     'C5: registered as witt.source.luther-das-newe-testament-deutzsch (unvendored; the prefaces on James, Jude, Revelation); Philadelphia Works vol. 6 is the English.',
     ['witt.source.luther-das-newe-testament-deutzsch (kind: unvendored)'])
addc('The Bible in Christian North Africa', ['don:C5/S6'])
addc('Care of the Dead', ['lpc:C13/S7'])
addc('Carmina Nisibena', ['syr:C13/S1'], 'C13: Bickell (Leipzig 1866), Syriac with Latin, is the public-domain route; Beck, CSCO 169-170 and 218-219 is in copyright.')
addc('Historia Monachorum', ['desert:C13/S2'], 'C13: Latin PL 21 (Migne 1849); Greek Preuschen (1897).')
addc('On the Deity of the Son', ['cappadocian:C2/S3'])
addc('Antiquities XVIII', ['fleet:C11/S8'],
     'C11 finding 1: no vendored text in the Library is a Jewish voice (no Josephus, no rabbinic text, no Philo). The report names Whiston\'s Josephus (1737) for S8 without naming a world, so the cell is recorded against "fleet".')

# ---- new rows: C2 ----
acq('Letters (God\'s goodness, knowledge of God)', 'Antony the Great', 'Latin of the Arabic, Migne PG 40:977-1000; English Rubenson 1995 and Chitty 1975 in copyright', 'not stated in report',
    'Latin: public domain', ['desert:C2/S2', 'desert:C2/S6'], english_copyright=True, identified_as=['desert.source.antony-letters (kind: unvendored); Build/worlds/_cross-world/WANTS-REGISTER.md L70'],
    notes='C13 also lists "Antony Letters" as identified for desert without naming a sub-question.')
acq('Against Eunomius; Homily on Psalm 33', 'Basil of Caesarea', 'Migne PG 29:497-669 (1857), Greek with Latin; English only in DelCogliano and Radde-Gallwitz, FOTC 122 (2011), in copyright', 'not stated in report',
    'Greek: public domain', ['cappadocian:C2/S3', 'cappadocian:C13/S4'], english_copyright=True,
    identified_as=['cappadocian.source.basil-against-eunomius (kind: unvendored); Build/worlds/_cross-world/WANTS-REGISTER.md L54'],
    notes='C13: Against Eunomius III.1 (the angel set over each believer) and the Homily on Psalm 33; the Letters\' editor cites both (npnf208 lines 5369, 7862).')
acq('Epiphanius on Eustathius and the Pneumatomachians', 'Epiphanius', NS, NS, NS, ['cappadocian:C2/S4'],
    identified_as=['cappadocian.source.epiphanius-on-eustathius-pneumatomachians (kind: unvendored); Build/worlds/_cross-world/WANTS-REGISTER.md L98'])
acq('Five Theological Orations', 'Gregory of Nazianzus', '"Mason" per Build/worlds/_cross-world/download-queue-seed.yaml', 'Build/worlds/_cross-world/download-queue-seed.yaml; not yet downloaded', NS, ['cappadocian:C2/S4'],
    identified_as=['Build/worlds/_cross-world/download-queue-seed.yaml row: Five Theological Orations (Mason)'], notes='Queued, not downloaded.')
acq('Apology for the Apology; Confession of 383', 'Eunomius', NS, NS, NS, ['cappadocian:C2/S5'],
    identified_as=['cappadocian.source.eunomius-apology-for-the-apology, eunomius-confession-of-383 (kind: unvendored); Build/worlds/_cross-world/WANTS-REGISTER.md L112-113'])
acq('Letter on the life and death of Ulfila', 'Auxentius of Durostorum', NS, NS, NS, ['ijc:C2/S5', 'ijc:C5/S6'],
    identified_as=['ijc.source.auxentius-letter-ulfila (kind: unvendored)'], notes='C2: Homoian self-testimony.')
acq('Gothic Bible (Ulfila)', 'Ulfila', 'Streitberg 1908', NS, NS, ['ijc:C5/S6'])
acq('The Luminous Eye; Symbols of Church and Kingdom', 'Sebastian Brock; Robert Murray', 'secondary scholarship', 'not stated in report', 'in copyright (modern scholarship)',
    ['syr:C2/S6'], english_copyright=True, identified_as=['syr.source.brock-luminous-eye, murray-symbols (kind: unvendored)'],
    notes='C13 also lists Brock, The Luminous Eye, as identified for syr.')
acq('Marburg Articles (1529), art. 1', 'Martin Luther', 'German, WA 30/3:160-171; English in Luther\'s Works vol. 38 (1971)', 'not stated in report', 'German: public domain; LW 38 in copyright',
    ['witt:C2/S3'], english_copyright=True, identified_as=['witt.source.marburg-articles (kind: unvendored); Build/worlds/_cross-world/WANTS-REGISTER.md L189'])

# ---- C5 ----
acq('Homilies on Joshua (Rufinus Latin)', 'Origen', 'GCS 30, Baehrens 1921', NS, NS, ['alx:C5/S7'])
acq('Homilies on the Song of Songs, Ecclesiastes (Hom. 4, the slave-market) and the Beatitudes', 'Gregory of Nyssa', 'Greek PG 44; Hall 1993 translation in copyright', NS,
    'Greek: public domain', ['cappadocian:C5/S2', 'cappadocian:C5/S8', 'cappadocian:C8/S3'], english_copyright=True,
    identified_as=['cappadocian.source.gregory-nyssa-song-of-songs-ecclesiastes-beatitudes-homilies (kind: unvendored)'],
    notes='C8: cappadocian.story.slave-market-sermon rests on this unvendored homily; the line is a paraphrase.')
acq('Commentary on Revelation (Beatus recension)', 'Tyconius', 'CCSL 107A, Gryson', NS, NS, ['don:C5/S5'], notes='The lost commentary survives in the Beatus recension. The Liber Regularum is already vendored.')
acq('Hexameron', 'Ambrose', 'Savage, FOTC 42', NS, NS, ['ijc:C5/S4'])
acq('Vetus Latina', 'anon.', 'Beuron edition', NS, NS, ['lpc:C5/S1'])
acq('Olivetan Bible (1535)', 'Pierre Robert Olivetan', NS, NS, NS, ['rzg:C5/S6'])
acq('Peshitta', 'anon. (Syriac)', NS, NS, NS, ['syr:C5/S6'])
acq('Lectures on Genesis', 'Martin Luther', 'WA 42-44', NS, NS, ['witt:C5/S4'])

# ---- C6 / C7 / C8: shared church-order sources ----
acq('The Apostolic Tradition', 'Hippolytus (attrib.)', 'B.S. Easton (Cambridge 1934); Dix (SPCK 1937) in copyright', 'archive.org / HathiTrust',
    'rights to be confirmed (1934 US renewal not checked); the ancient witnesses are public domain',
    ['alx:C6/S1', 'alx:C6/S6', 'alx:C10/S7', 'pahc:C7/S1'],
    notes='C6: the bishop "chosen by all the people", ordination of presbyters and deacons, the deaconess not ordained; C7: order of baptism, bread and cup, hours of prayer, fasting; C10: ch. 16, trades barred to catechumens (Egyptian and Latin witnesses); C9 names ch. 16 on soldiers and magistrates without a world.')
acq('Didascalia Apostolorum', 'anon. (Syria, 3rd c.)', 'M.D. Gibson, The Didascalia Apostolorum in English (Horae Semiticae 2, London 1903); R.H. Connolly (Oxford 1929) is the better text', 'archive.org',
    'Gibson 1903 public domain; Connolly 1929 US public domain, other territories unchecked',
    ['syr:C6/S1', 'syr:C6/S5', 'syr:C6/S6', 'pahc:C6/S1', 'pahc:C6/S5', 'pahc:C6/S6', 'syr:C7/S1', 'syr:C7/S2', 'syr:C8/S2', 'alx:C8/S2', 'pahc:C8/S2'],
    notes='C6: bishop as judge of the community, presbyters, deacons, deaconesses, widows, penance and exclusion; C7: penance and readmission, the fast before Pascha, who is refused the offering; C8: deaconesses, widows, separation.')
acq('Own works (canons, Creed)', 'Amphilochius of Iconium', NS, NS, NS, ['cappadocian:C6/S1', 'cappadocian:C7/S5'],
    identified_as=['cappadocian.source.amphilochius-of-iconium-own-works (kind: unvendored)'])
acq('Imperial communion law of 381', 'Theodosius I', NS, NS, NS, ['cappadocian:C6/S7', 'cappadocian:C9/S3'],
    identified_as=['cappadocian.source.imperial-communion-law-of-381 (kind: unvendored)'])
acq("Julian's measures against Caesarea", 'Julian', NS, NS, NS, ['cappadocian:C6/S7', 'cappadocian:C11/S3'],
    identified_as=['cappadocian.source.julians-measures-against-caesarea (kind: unvendored)'])
acq('Pachomius and the Idea of a Saintly Institution', 'Philip Rousseau', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['desert:C6/S1'],
    english_copyright=True, identified_as=['desert.source.rousseau-pachomius (kind: unvendored)'])
acq('Pachomian Koinonia', 'Armand Veilleux', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['desert:C6/S1'],
    english_copyright=True, identified_as=['desert.source.veilleux-koinonia (kind: unvendored)'])
acq('Optatus of Milevis: Against the Donatists (TTH 27)', 'Mark Edwards (trans.)', 'Liverpool UP, TTH 27', NS, NS, ['don:C6/S2'],
    identified_as=['don.source.edwards-optatus-against-the-donatists-tth27 (kind: unvendored)'],
    notes='The Vassall-Phillips 1917 English is already vendored.')
acq('Authority and Asceticism from Augustine to Gregory the Great', 'Conrad Leyser', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['gallic:C6/S8'],
    english_copyright=True, identified_as=['gallic.source.leyser-authority-and-asceticism (kind: unvendored)'])
acq('Ecclesiastical Factionalism and Religious Controversy in Fifth-Century Gaul', 'Ralph Mathisen', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['gallic:C6/S8'],
    english_copyright=True, identified_as=['gallic.source.mathisen-ecclesiastical-factionalism (kind: unvendored)'])
acq('Ordonnances ecclesiastiques (1541)', 'John Calvin', 'Opera Calvini vol. 10/1 (Brunswick 1871), French; English: Reid translation (1954), and Calvin: Theological Treatises', 'not stated in report',
    'public domain (French); Reid translation (1954) in copyright', ['rzg:C6/S1', 'rzg:C6/S6', 'rzg:C10/S4', 'rzg:C10/S6'], english_copyright=True,
    identified_as=['rzg.source.ecclesiastical-ordinances-1541 (kind: unvendored)'],
    notes='C6: the 1576 council revision is vendored in French, the 1541 text is only named; see registry drift below.')
acq('Roman Confutation of the Augsburg Confession', 'Catholic theologians (1530)', NS, NS, NS, ['witt:C7/S2'],
    identified_as=['witt.source.roman-confutation-of-the-augsburg-confession (kind: unvendored)'])
acq("Bishop Sarapion's Prayer-Book (Euchologion)", 'Sarapion of Thmuis', 'J. Wordsworth (SPCK, London 1899)', 'archive.org', 'public domain (US)',
    ['alx:C7/S2', 'alx:C7/S7'], notes='C7: prayers for baptism, the bread and cup, the oil of the sick, burial (Egypt, c. 350). "The missing Egyptian witness."')
acq('Homilies on the Forty Martyrs, Gordius, Julitta and Mamas', 'Basil of Caesarea', 'Greek PG 31 (Migne); no public-domain English; Leemans et al., Let Us Die That We May Live (Routledge 2003) in copyright', 'archive.org / documentacatholicaomnia',
    'Greek: public domain', ['cappadocian:C7/S6', 'cappadocian:C9/S1', 'cappadocian:C13/S5'], english_copyright=True,
    identified_as=['cappadocian.source.basil-martyr-homilies-forty-gordius-julitta-mamas (kind: unvendored)'])
acq('In XL Martyres I-II; On Theodore the Recruit; Life of Gregory Thaumaturgus', 'Gregory of Nyssa', 'Greek PG 46 (Migne 1863); no public-domain English', 'archive.org / documentacatholicaomnia',
    'Greek: public domain', ['cappadocian:C7/S7', 'cappadocian:C9/S1', 'cappadocian:C13/S5'], english_copyright=True,
    identified_as=['cappadocian.source.gregory-nyssa-forty-martyrs-theodore-recruit-homilies (kind: unvendored)'],
    notes='C13: the shrine, the relics touched "as if still alive", the painted passion on the walls.')
acq('Kellia excavation reports (EK series; Kasser, Rassart-Debergh)', 'various', 'consult-only', NS, NS, ['desert:C7/S4', 'desert:C12/S8'],
    identified_as=['desert.source.kellia-excavations (kind: unvendored)'])
acq('Sermons', 'Caesarius of Arles', 'Sources Chretiennes (Delage) in copyright; Latin CCSL 103-104 (Morin 1953) in copyright; older Latin in PL 39', 'archive.org (PL 39)',
    'Latin of PL public domain; modern editions not', ['gallic:C7/S1'], notes='C7: baptism, communion, Lent, feast days in Gaul (early 6th c.).')
acq('Form of Prayers and Manner of Ministering the Sacraments (Geneva 1542)', 'John Calvin', 'Tracts and Treatises vol. 2, tr. H. Beveridge (Calvin Translation Society, Edinburgh 1849)', 'archive.org', 'public domain', ['rzg:C7/S3'],
    notes='The Sunday order, baptism, the Supper, set prayers, the Psalms sung.')
acq('Demonstrations III (On Fasting), IV (On Prayer), XI-XIX, XIV and XX (Syriac with Latin)', 'Aphrahat', 'J. Parisot, Patrologia Syriaca I.1 (Paris 1894) and I.2/II (1907); English only in Lehto (Gorgias 2010) and Neusner (Brill 1971), in copyright', 'archive.org (Patrologia Syriaca)',
    'Syriac and Latin public domain; English not', ['syr:C7/S3', 'syr:C7/S5', 'syr:C11/S1', 'syr:C11/S2', 'syr:C10/S2', 'syr:C10/S4'], english_copyright=True,
    notes='NPNF 13 holds only Dem. I, V, VI, VIII, X, XVII, XXI, XXII and Hallock 1932 only II and VII. C7: Dem. III and IV; C10: XX (helping the poor) and XIV; C11: XI-XIX (circumcision, Passover, Sabbath, foods, the peoples).')
acq('Order of Baptism (Taufbuechlein, 1523, rev. 1526) and German Mass (1526)', 'Martin Luther', 'Weimarer Ausgabe vol. 12 and 19, German; English in Luther\'s Works 53 (Fortress 1965)', 'archive.org',
    'German public domain; LW 53 in copyright', ['witt:C7/S1', 'witt:C7/S4'], english_copyright=True)
acq('Epistre tres utile (1539) and the 1561 preface', 'Marie Dentiere', 'French; modern translations in copyright', NS, 'French: public domain', ['rzg:C8/S2'], english_copyright=True,
    identified_as=['rzg.source.dentiere-works (kind: unvendored)'])
acq('Letters (1523)', 'Argula von Grumbach', 'German (WA); Matheson translation in copyright', NS, 'German: public domain', ['witt:C8/S1'], english_copyright=True,
    identified_as=['witt.source.argula-womans-voice-in-the-reformation (kind: unvendored)'])
acq('Estate of Marriage (1522); writings of Katharina Zell', 'Martin Luther; Katharina Zell', 'German; English LW 45 and McKee 1999 in copyright', 'not fetched; working knowledge',
    'German public domain', ['witt:C8/S4'], english_copyright=True)
acq('Rules for the covenanters (Syriac)', 'Rabbula of Edessa', 'Overbeck 1865', 'not fetched; working knowledge', 'public domain', ['syr:C8/*'],
    notes='C8 names the source for syr without naming a sub-question.')

# ---- C9 ----
acq('Marian exiles; Geneva refugee records', 'various', 'not checked', 'not stated in report', NS, ['rzg:C9/S1'])
acq('Admonition to Peace; Against the Robbing and Murdering Hordes (1525)', 'Martin Luther', NS, NS, NS, ['witt:C9/S6'],
    identified_as=['witt.source.luther-admonition-to-peace (kind: unvendored)'])
acq('The Libelli of the Decian Persecution (Harvard Theological Review 1923)', 'J.R. Knipfing', 'HTR 1923', 'not fetched; working knowledge', NS, ['alx:C9/S2', 'lpc:C9/S2'])
acq('Acts of Maximilian and Marcellus (Ruinart)', 'anon.', 'Ruinart', 'not fetched; working knowledge', NS, ['fleet:C9/S4'], notes='C9: for soldiers; the report names no world.')
acq('Letters; Damascius (Hypatia and the Serapeum)', 'Synesius', NS, 'not fetched; working knowledge', NS, ['alx:C9/S5'])
acq('Oration 30 (temples)', 'Libanius', NS, 'not fetched; working knowledge', NS, ['fleet:C9/S5'], notes='C9: for temples; the report names no world.')

# ---- C10 ----
acq('De pauperibus amandis I-II (On the Love of the Poor)', 'Gregory of Nyssa', 'Greek, PG 46:453-489 (Migne); English is Holman (OUP 2001), in copyright', NS,
    'Greek public domain; English not', ['cappadocian:C10/S1', 'cappadocian:C10/S4'], english_copyright=True,
    identified_as=['cappadocian.source.gregory-nyssa-de-pauperibus-amandis (kind: unvendored)'])
acq('Oration 14 On the Love of the Poor', 'Gregory of Nazianzus', 'Greek, PG 35:857-909; English Vinson, FOTC 107 (2003), in copyright', NS,
    'Greek public domain; English not', ['cappadocian:C10/S1', 'cappadocian:C10/S4'], english_copyright=True,
    identified_as=['cappadocian.source.gregory-nazianzus-oration-14-love-of-poor (kind: unvendored)'])
acq('Homily on Psalm 14 (against usurers) and Homily on Luke 12:18 (I will pull down my barns); the famine homilies', 'Basil of Caesarea', 'Greek, PG 29:263-280 and PG 31:261-277', NS,
    'Greek public domain', ['cappadocian:C10/S1', 'cappadocian:C10/S5'],
    identified_as=['cappadocian.source.basil-moral-famine-homilies (kind: unvendored)'],
    notes='The public-domain English is only the Jackson extracts already in npnf208 (lines 5069-5284, 6236-6290, 6926). The quote records in the records list do not need this acquisition.')
acq('Ad ecclesiam (Four Books to the Church, against avarice)', 'Salvian', 'Latin, CSEL 8, ed. Pauly (Vienna 1883); Walsh, FOTC 3 (1947) in copyright', NS, 'Latin public domain', ['gallic:C10/S1', 'gallic:C10/S6'], english_copyright=True)
acq('Zurich poor-relief mandates; Von goettlicher und menschlicher Gerechtigkeit (1523, tithes)', 'Huldrych Zwingli; Zurich council', 'German, Corpus Reformatorum, Zwingli Werke vol. 2 (Leipzig 1908); Egli, Actensammlung zur Geschichte der Zuercher Reformation (Zurich 1879)', 'archive.org (Egli 1879)',
    'public domain; English in Bromiley, LCC 24 (1953), in copyright', ['rzg:C10/S4', 'rzg:C10/S6', 'rzg:C13/S6'], english_copyright=True,
    notes='C13: Zurich\'s mandates on soothsaying.')
acq('Long Sermon on Usury (1520); Trade and Usury (1524); Ordinance of a Common Chest (1523)', 'Martin Luther', 'WA 6:33-60, 15:293-322, 12:11-30 (Weimar, German); English in Works of Martin Luther, Holman vol. 4 (Philadelphia 1931)', 'not stated in report',
    'German public domain; the 1931 English enters the US public domain only on 1 Jan 2027', ['witt:C10/S5', 'witt:C10/S6'], english_copyright=True)
acq('De Nabuthae (wealth and the poor)', 'Ambrose', 'Latin, PL 14:731-756, CSEL 32.2 (Schenkl 1897); English FOTC (1972) in copyright', NS, 'Latin public domain', ['ijc:C10/S1', 'ijc:C10/S4'], english_copyright=True)
acq("Caesarea's poorhouse and hospital complex (the Basileias)", 'archaeology and sources', NS, NS, NS, ['cappadocian:C10/S4', 'cappadocian:C12/S4', 'cappadocian:C12/S8'],
    identified_as=['cappadocian.source.caesareas-poorhouse-hospital-complex (kind: unvendored)'])
acq('Nepheros archive (Melitian rival)', 'papyri', NS, NS, NS, ['desert:C10/S6', 'desert:C11/S8', 'desert:C12/S3', 'desert:C12/S8'],
    identified_as=['desert.source.nepheros-archive (kind: unvendored)'])

# ---- C11 ----
acq('Commentary on Matthew (series) and Homilies on Jeremiah on the Jews', 'Origen', 'GCS 38/40 (Klostermann 1933/1935), Greek/Latin', 'archive.org',
    'public domain in the US for the 1933 volume only if not renewed; verify', ['alx:C11/S1'])
acq('Ad quaestiones et obiecta Iudaei cuiusdam responsio', 'John Calvin', 'Calvini Opera 9 (Baum, Cunitz, Reuss 1870), Latin', 'archive.org (CO 9)', 'public domain (Latin); no PD English', ['rzg:C11/S1'])
acq('Tractatus adversus Iudaeos', 'Augustine', 'PL 42 (Migne 1865), Latin', 'archive.org / documentacatholicaomnia', 'public domain (Latin); FOTC 27 (1955) in copyright', ['lpc:C11/S1'], english_copyright=True)
acq('Epistula de conversione Iudaeorum (418)', 'Severus of Minorca', 'PL 20 / PL 41 (Migne), Latin; Bradbury 1996 English in copyright', 'archive.org', 'public domain (Latin); Bradbury 1996 in copyright',
    ['lpc:C11/S1', 'lpc:C11/S7', 'gallic:C11/S1'], english_copyright=True, notes='A forced conversion in the Latin West; C11 says it sits on the Gallic world\'s southern edge too.')
acq('Against the Galilaeans', 'Julian', 'Wright, Loeb Julian vol. 3 (1923)', 'archive.org', 'public domain (US, 1923)', ['ijc:C11/S3'],
    notes='The vendored julian_letters-1-73_wright1923.txt cites it in footnotes but does not contain it.')
acq('Testimonia adversus Iudaeos (attribution disputed)', 'Gregory of Nyssa', 'PG 46 (Migne 1863), Greek', 'archive.org', 'public domain (Greek); no PD English', ['cappadocian:C11/S1'])
acq('Dialogue and Disputation: Aphrahat, Ephrem and the Jews (Koltun-Fromm)', 'Naomi Koltun-Fromm', 'secondary scholarship (2010/2011)', 'WANTS-REGISTER rank 3', 'in copyright (modern scholarship)', ['syr:C11/S1'], english_copyright=True,
    identified_as=['syr.source.koltun-fromm-dialogue (kind: unvendored)'], notes='C11: "the only route to the content of Demonstrations XI-XIX".')
acq('Bardaisan studies (Drijvers; Possekel)', 'H.J.W. Drijvers; Ute Possekel', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['syr:C11/S8'], english_copyright=True,
    identified_as=['syr.source.drijvers-bardaisan, syr.source.possekel-bardaisan (kind: unvendored)'])
acq("Julian's Hellenic reclamation project", 'secondary', NS, NS, NS, ['cappadocian:C11/S3'], identified_as=['cappadocian.source.julians-general-hellenic-reclamation-project (kind: unvendored)'])
acq('Libanius and the paideia witness', 'Libanius (secondary)', NS, NS, NS, ['cappadocian:C11/S3'], identified_as=['cappadocian.source.libanius-paideia-witness (kind: unvendored)'])
acq('Virgins of God, Sons of Hellenism (Elm)', 'Susanna Elm', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['cappadocian:C11/S3'], english_copyright=True,
    identified_as=['cappadocian.source.elm-virgins-of-god-sons-of-hellenism (kind: unvendored)'])
acq("Luther's Jews: A Journey into Anti-Semitism (Kaufmann 2017); Wallmann, reception of Luther's writings (1987)", 'Thomas Kaufmann; Johannes Wallmann', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['witt:C11/S1'], english_copyright=True,
    identified_as=['witt.source.thomas-luthers-jews-a-journey-into-anti, witt.source.johannes-reception-of-luthers-writings, witt.source.wikipedia-on-the-jews-and-their-lies (kind: unvendored)'],
    notes='C11: the secondary chain the 1543 contested_claim rests on.')
acq('Von den Juden und ihren Luegen (1543); Against the Sabbatarians (1538)', 'Martin Luther', 'Weimarer Ausgabe 53 (1920) and 50 (1914), German', 'archive.org (WA)',
    'German public domain; English LW 47 (1971) in copyright', ['witt:C11/S1', 'witt:C9/S6', 'witt:C15/S8'], english_copyright=True,
    identified_as=['witt.source.luther-von-den-juden-und-ihren-l (kind: unvendored; WANTS-REGISTER rank 0)'],
    notes='C11: the Sabbatarians text is not registered anywhere in the repo; C15: the 1543 text on the Jews is named, not vendored.')
acq('Vom Kriege wider die Tuerken (1529); Verlegung des Alcoran (1542); preface to Bibliander\'s Qur\'an (1543)', 'Martin Luther', 'WA 30/2 (1909) and 53 (1920); Holman Works of Martin Luther vol. 5 (1931) has "On War Against the Turk" in English', 'archive.org',
    'WA public domain; Holman vol. 5 (1931) PD-US only if its copyright was not renewed (check)', ['witt:C11/S4'], notes='Not registered in the repo.')
acq("Sale's Koran (1734)", 'George Sale', '1734', 'not fetched; working knowledge', NS, ['rzg:C11/S4', 'witt:C11/S4'])
acq('The Mishnah (Danby 1933) or Schechter\'s Talmud extracts', 'Herbert Danby / Solomon Schechter', NS, 'not fetched; working knowledge', 'editions and licences need the Library thread to confirm', ['fleet:C11/S1'],
    notes='C11 finding 1: the Library holds no rabbinic text.')

# ---- C12 ----
acq('Egyptian papyri for daily life (Oxyrhynchus, Karanis, Tebtunis; Bagnall)', 'various', NS, 'not fetched', NS, ['alx:C12/*', 'desert:C12/*'], notes='The report names the worlds, not a sub-question.')
acq('Carthaginian cemeteries and epitaphs, English reports (Delattre; Gsell)', 'various', 'vendored in French; English reports not', 'not fetched', NS, ['lpc:C12/*', 'don:C12/*'], notes='The report names the worlds, not a sub-question.')
acq('Whether one may flee from a deadly plague (1527; Works vol. 43)', 'Martin Luther', NS, 'not fetched', NS, ['witt:C12/S4'], notes='The report names witt without a sub-question; S4 (sickness, plague) is the cell the title fits.')
acq('Holy Women of the Syrian Orient; Edessa (Segal)', 'Sebastian Brock and Susan Harvey; J.B. Segal', 'secondary scholarship', 'not fetched', 'in copyright (modern scholarship)', ['syr:C12/*'], english_copyright=True)
acq('Orations 7 and 8 (funeral orations) and his will', 'Gregory of Nazianzus', 'in English', 'not fetched', NS, ['cappadocian:C12/S5'],
    identified_as=['cappadocian.source.gregory-nazianzus-will-manumission (kind: unvendored)'], notes='Registered source covers the will and manumission.')
acq('Annisa estate shrine (Vita Macrinae)', 'archaeology and sources', NS, NS, NS, ['cappadocian:C12/S8', 'cappadocian:C13/S5'], identified_as=['cappadocian.source.annisa-estate-shrine (kind: unvendored)'])
acq('Numidian basilica archaeology', 'archaeology', NS, NS, NS, ['don:C12/S8'], identified_as=['don.source.numidian-basilica-archaeology (kind: unvendored)'])
acq('Nisibis cathedral report (Kayaalp)', 'Elif Kayaalp', NS, NS, NS, ['syr:C12/S8'], identified_as=['syr.source.kayaalp-nisibis-cathedral (kind: unvendored)'])

# ---- C13 ----
acq('Homilies on Luke (incl. Hom. 35 on the angel and the demon that attend each soul) and Homilies on Numbers', 'Origen', 'Latin (Jerome\'s and Rufinus\'s versions), GCS Origenes Werke 9 (Rauer 1930) and 7 (Baehrens 1921); Hom. in Numeros Latin is already vendored (rufinus-aquileia_origenes-werke-bd7), Luke is not', 'archive.org (GCS)',
    'public domain (Latin/Greek); Lienhard FOTC 94 (1996) English in copyright', ['alx:C13/S2'], english_copyright=True)
acq('Excerpta ex Theodoto and Eclogae propheticae (angels assigned to persons and nations)', 'Clement of Alexandria', 'Greek, GCS Clemens 3 (Staehlin 1909); English of the Excerpta in R.P. Casey, Studies and Documents 1 (1934)', 'archive.org',
    'public domain (Greek); Casey 1934 PD-US', ['alx:C13/S4'])
acq('Orations 24 (on Cyprian) and 8 (on Gorgonia)', 'Gregory of Nazianzus', 'Greek with Latin, PG 35 (Migne 1857); not among the NPNF 2/7 selection vendored; English Vinson, FOTC 107 (2003) in copyright', 'archive.org (PG 35)',
    'public domain (Greek/Latin)', ['cappadocian:C13/S6'], english_copyright=True)
acq('Antirrhetikos and On Thoughts (Peri logismon)', 'Evagrius Ponticus', 'Syriac Frankenberg, Euagrius Ponticus (Berlin 1912) with Greek retroversion; On Thoughts Greek PG 79 and 40 under Nilus; Brakke (2009) and Sinkewicz (2003) English in copyright', 'archive.org (Frankenberg 1912)',
    'public domain (Syriac/Greek)', ['desert:C13/S3'], english_copyright=True, notes='desert.term.antirrhesis already says "no vendored text exists".')
acq('Demons and the Making of the Monk', 'David Brakke', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['desert:C13/*'], english_copyright=True)
acq('Natalicia (Carmina 12-29); Letters 31 and 32', 'Paulinus of Nola', 'Latin CSEL 29-30 (Hartel 1894); English Walsh, ACW 35-36 and 40 (1966-1975) in copyright', 'archive.org (CSEL 29-30)',
    'public domain (Latin)', ['gallic:C13/S5'], english_copyright=True, notes='The shrine of St Felix; a relic of the cross sent to Sulpitius.')
acq('De laude sanctorum (396)', 'Victricius of Rouen', 'Latin PL 20 (Migne 1845), critical ed. CCSL 64 (1985); English Clark, JECS 7 (1999) in copyright', 'archive.org (PL 20)',
    'public domain (Latin)', ['gallic:C13/S5'], english_copyright=True, notes='The theology of relics, written for Gaul in the window.')
acq('De obitu Theodosii 40-48 (Helena and the True Cross)', 'Ambrose', 'De obitu Theodosii: Latin CSEL 73 (Faller 1955) in copyright, PL 16 (Migne 1845) public domain; Mannix (CUA 1925) English PD-US', 'archive.org (PL 16; Mannix 1925)',
    'public domain (Latin PL 16); Mannix 1925 PD-US', ['ijc:C13/S5'],
    notes='Paulinus, Vita Ambrosii is vendored (paulinus-milan_vita-ambrosii_kaniecka1928.txt) but mapped only via ijc.source.paulinus-vita-ambrosii.')
acq('Treatise on Relics (Traite des reliques, 1543)', 'John Calvin', 'English, Calvin\'s Tracts vol. 1, trans. Henry Beveridge (Calvin Translation Society, Edinburgh 1844), pp. 287-341; French, Opera 6', 'archive.org / CCEL', 'public domain', ['rzg:C13/S5'])
acq('A Short Christian Instruction (1523); Answer to Valentin Compar (1525)', 'Huldrych Zwingli', 'Latin Works vol. 2 (Hinke 1922), not vendored (vols. 1 and 3 are)', 'archive.org', 'public domain in the US (Hinke 1922)', ['rzg:C13/S5'])
acq('The Acts of Thomas (Wright 1871, from the Syriac)', 'anon.', 'Wright, Apocryphal Acts of the Apostles (London 1871)', 'archive.org (Wright 1871)', 'public domain', ['syr:C13/S2'],
    notes='The ANF 8 Greek-based version is vendored; the Persian martyr acts are vendored only in German (Braun 1915, Hoffmann 1880).')
acq('Hymns against Heresies (demons, astrology, Bardaisan\'s planets)', 'Ephrem the Syrian', 'Beck, CSCO 169-170 (1957) and 218-219 (1961), in copyright', NS, 'in copyright', ['syr:C13/S1'], english_copyright=True)
acq('Ephrem memory dossier (Jacob of Serug)', 'Jacob of Serug', NS, NS, NS, ['syr:C13/*'], identified_as=['syr.source (Ephrem memory dossier; kind: unvendored)'])
acq('The Table Talk of Martin Luther (Hazlitt, Bohn 1857; Of the Devil and His Works)', 'Martin Luther', 'trans. William Hazlitt (Bohn, London 1857; from Aurifaber); German WA Tischreden 1-6 (1912-1921)', 'archive.org', 'public domain', ['witt:C13/S2'],
    notes='The vendored luther_table-talk_bell1886.txt is Bell\'s 1646 selection (43 "devil" hits) and does not carry these chapters.')
acq('Sermon on the Ten Commandments (1518, Decem praecepta)', 'Martin Luther', 'Latin WA 1:394-521 (1883); no public-domain English', 'archive.org (WA 1)', 'public domain (Latin)', ['witt:C13/S6'],
    notes='The Treatise on Good Works is already vendored (luther_works-v1, lines 7820-7892).')
acq('Luther: Man between God and the Devil', 'Heiko Oberman', 'secondary scholarship', NS, 'in copyright (modern scholarship)', ['witt:C13/*'], english_copyright=True)

# ---- C15, C16 ----
acq('Commentary on Exodus 21:22 (Harmony of the Last Four Books of Moses)', 'John Calvin', NS, NS, NS, ['rzg:C15/S7'],
    notes='C15: "Calvin\'s Exodus 21:22 comment ... not vendored"; the nearest text for the abortion question.')
acq('Secondary scholarship on the Consensus Tigurinus', 'various', NS, NS, NS, ['rzg:C16/S4'],
    notes='C16: the only S4 record concedes "No secondary scholarship on the Consensus Tigurinus specifically is vendored".')

# ---- listed as OTHER in a report but already in cic/texts (16-cluster additions) ----
VENDORED_ALREADY += [
 dict(work='Augustine, Collatio cum Maximino (PL 42)', file=P('collatio'), line=None, cells=['lpc:C2/S3'], note='C2 lists it as OTHER; the vendored augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt carries it. Latin only.'),
 dict(work='Odes of Solomon (Harris and Mingana 1916-1920; the spirit as dove and milk)', file=P('odes-hm'), line=None, cells=['syr:C2/S4'], note='C2 lists it as OTHER; odes-of-solomon_harris-mingana1920.txt is in cic/texts, as is the Harris 1911 file. Whether the 1920 file is mapped to syr was not checked.'),
 dict(work='Tertullian, De baptismo and De corona (ANF 3)', file=P('anf03'), line=None, cells=['pahc:C7/S1'], note='C7: already vendored as anf03 but mapped only to pahc.'),
 dict(work='Chrysostom, Homily 20 on Ephesians (wives and slaves)', file=P('npnf113'), line=None, cells=['ijc:C8/S2', 'hal:C8/S2'], note='C8: vendored and mapped only to the Antiochene-Chrysostom bucket, none of the twelve worlds. A corpus-map fix, not a download.'),
 dict(work='Augustine, Letters 22 and 29 (laetitia at the martyrs\' tombs) and Possidius, Life ch. 29', file=P('npnf101'), line=None, cells=['don:C13/S5', 'lpc:C13/S5'], note='C13: NPNF 1/1 vendored and mapped; Possidius (weiskotten 1919, line 591) vendored and mapped.'),
 dict(work='Sulpitius Severus, Dialogues I (Postumianus on Egypt)', file=P('npnf211'), line=None, cells=['gallic:C13/S3'], note='C13: vendored and mapped; the world\'s records draw on Dialogues II-III and cite Dialogue I in none.'),
 dict(work='Cassian, Conferences VII and VIII (demons; On Principalities)', file=P('npnf211'), line=32132, cells=['gallic:C13/S2', 'gallic:C13/S4'], note='C13: lines 32132 and 33442, mapped; cited by no gallic record.'),
 dict(work='Jerome, Against Vigilantius and Letter 109 to Riparius; Life of Hilarion; Letter 108 on Paula', file=P('npnf206'), line=22262, cells=['hal:C13/S5', 'hal:C13/S6', 'hal:C13/S2'], note='C13: Against Vigilantius near line 22255, Letter 109 at 22262, Hilarion 29725, Paula 21340; cited by no hal record.'),
 dict(work='Ammianus Marcellinus XXIX.1-2 (the magic trials at Antioch), Yonge 1862', file=P('ammianus'), line=None, cells=['ijc:C13/S6'], note='C13 lists the Bohn edition as OTHER; the Yonge 1862 file is vendored (C16 cites it at line 23176).'),
 dict(work='Augustine, On Care to Be Had for the Dead; City of God XXII.8; Tractates on John 7', file=P('npnf103'), line=43492, cells=['lpc:C13/S3', 'lpc:C13/S6', 'lpc:C13/S7'], note='C13: vendored and mapped to lpc; cited only by a consult-only source record.'),
 dict(work='Justin, 2 Apology 6 and Dialogue 30, 76, 85; Irenaeus II.32.4; Hermas Mandate 6.2; Ignatius Ephesians 19', file=P('anf01'), line=16966, cells=['pahc:C13/S2', 'pahc:C13/S4', 'pahc:C13/S6'], note='C13: vendored and mapped to pahc; no pahc record mentions exorcism.'),
 dict(work='Luther, Treatise on Good Works (1520), second commandment', file=P('luther-v1'), line=7820, cells=['witt:C13/S6'], note='C13: vendored and mapped (lines 7820-7892).'),
 dict(work='Barnabas 9-16 (circumcision, Sabbath, temple)', file=P('anf01'), line=None, cells=['pahc:C11/S1'], note='C11: already vendored in anf01; no acquisition needed.'),
 dict(work='Athanasius, Contra Gentes (gods as demons; idols)', file=P('npnf204'), line=None, cells=['alx:C11/S3'], note='C11: already vendored in npnf204 (Robertson 1892).'),
 dict(work='Gerlach, Tage-Buch (Istanbul, 237 hits) and Lucaris, Lettres', file=P('gerlach'), line=None, cells=['witt:C11/S4', 'rzg:C11/S4'], note='C11: firsthand Ottoman material mapped to witt and rzg that no record uses.'),
 dict(work='Jeremias II correspondence with the Tuebingen theologians (1576-81, Latin)', file=P('jeremias'), line=None, cells=['witt:C15/S4'], note='C15: meets the East-West split question; Latin, counted not read.'),
 dict(work='Gregory Nazianzen, First and Second Invectives against Julian (King 1888)', file=TX('gregory-nazianzen_first-invective-against-julian_king1888.txt'), line=None, cells=['cappadocian:C11/S3'], note='Vendored; C11 renders Julian\'s own words for cappadocian and notes Basil\'s Address (basil_address-to-young-men_padelford1902.txt) as vendored and unquoted.'),
]
VENDORED_ALREADY += STALE_ACQ_MOVED

# ---- registry drift: 16-cluster additions ----
DRIFT += [
 dict(id='cappadocian.source.liturgy-of-st-basil', finding='Registered kind: unvendored although the Neale volume of Eastern liturgies is vendored and mapped.',
      file=P('neale-lit'), line=None, reports=['C7 cappadocian S2'], fix='source-record fix (kind, file)'),
 dict(id='don.source.acta-saturnini-abitinian-martyrs', finding='Registered kind: unvendored although the Latin Acta of Saturninus is vendored in monumenta-vetera-donatistarum_migne-pl8.txt (lines 1781, 2974: "we cannot live without the dominicum"). Only the English (Tilley 1996) is blocked.',
      file=P('pl8'), line=1781, reports=['C7 don S2', 'C9 don S1', 'C13 don S5'], fix='registry note: Latin held, English blocked'),
 dict(id='rzg.source.genevan-psalter', finding='Record says unvendored while marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt is mapped.',
      file=P('marot'), line=None, reports=['C5 rzg S6'], fix='source-record fix (kind, file)'),
 dict(id='tyconius_liber-regularum_burkitt1894.txt (4-cluster acquire row)', finding='The 4-cluster acquire list carried Tyconius, Liber Regularum as an acquisition; C5 found it vendored and unread.',
      file=P('tyconius'), line=None, reports=['C3 don S3/S8', 'C5 don S2'], fix='row moved out of acquire.yaml; no download needed'),
 dict(id='npnf113 Chrysostom homilies (corpus map)', finding='Chrysostom\'s Homily 20 on Ephesians (wives and slaves) is vendored but mapped to none of the twelve worlds.',
      file=P('npnf113'), line=None, reports=['C8 ijc/hal', 'C14 FAC'], fix='corpus-map fix: add rows for ijc and hal if the world is to speak to it'),
 dict(id='npnf110, npnf112, npnf113, npnf114 Chrysostom verse-by-verse homilies (corpus map)', finding='Scripture-commentary-tagged homilies on Matthew, John, Corinthians, Galatians-Philemon are mapped only to the Antiochene world.',
      file=P('npnf110'), line=None, reports=['C5 passage-index feasibility'], fix='corpus-map fix'),
 dict(id='hefele v3 Synod of Orange 441, canon 26 (corpus map)', finding='Canon 26 ("Deaconesses shall no longer be ordained", hefele v3 line 8855) is in ijc\'s map only; gallic cannot reach it.',
      file=P('hefele3'), line=8855, reports=['C6 gallic S6'], fix='corpus-map fix: add a row for gallic'),
 dict(id='Basil Letter 93 (npnf208, corpus map)', finding='Letter 93 (solitaries commune at home) is not mapped to the desert world.',
      file=P('npnf208'), line=29930, reports=['C7 desert S2'], fix='corpus-map fix'),
 dict(id='Jerome Ep. 146 (corpus map)', finding='Ep. 146 (Alexandrian presbyters named their bishop) sits in hal\'s map, not alx\'s.',
      file=P('npnf206'), line=None, reports=['C6 alx S1'], fix='corpus-map fix: add a row for alx'),
 dict(id='Persian martyr acts (Braun 1915, Hoffmann 1880) and Anabaptist sources (Hubmaier, Menno, Martyrs Mirror) (corpus map)', finding='Vendored but mapped to the Church of the East movements (martyr acts) and to another movement (Anabaptist), not to syr and rzg.',
      file=None, line=None, reports=['C9 syr S2', 'C9 rzg S5', 'C13 syr'], fix='corpus-map fix'),
 dict(id='ijc.source.paulinus-vita-ambrosii', finding='paulinus-milan_vita-ambrosii_kaniecka1928.txt is vendored but reaches ijc only through the source record, not the corpus map.',
      file=P('paulinus-amb'), line=None, reports=['C13 ijc S5'], fix='corpus-map check'),
]

# =====================================================================
# 16-CLUSTER EXTENSION: records rows (C2, C5-C13, C16 by hand; C15 generated below)
# =====================================================================
import glob as _glob
T.update({
 'calvin-gen1': 'calvin_commentaries-genesis-vol1_king1847.txt',
 'cassian-inst': 'cassian_institutes-and-contra-nestorium_petschenig1888.txt',
 'ps-justin': 'pseudo-justin_epistle-to-diognetus-grc_lake1917.txt',
})
def _extend(world, line, cells, note='', group=None, fac=None):
    hits = [r for r in R if r['world'] == world and r['line'] == line and (group is None or r['group'] == group)]
    assert len(hits) == 1, (world, line, group, len(hits))
    r = hits[0]
    r['cells'] = sorted(set(r['cells']) | set(cells))
    if note: r['reason'] = r['reason'] + ' ' + note
    if fac: r['facilitator_adjacent'] = True

def RP(rid):
    """Path of a record file under records/ (any world, any type), or a marked guess if absent."""
    m = _glob.glob(os.path.join(REPO, 'records', '*', '*', rid + '.md'))
    if m:
        return os.path.relpath(m[0], REPO)
    return 'records/%s/_not-found_/%s.md' % (rid.split('.')[0], rid)

R = [r for r in R if not (r['record_type'] == 'quote fix' and ('Macarian' in r['source_text'] or 'four Salvian' in r['source_text']))]   # superseded: see the gallic C1 row below

# ---------------- alx ----------------
w = 'alx'
rec(w,['C2/S4'],'quote',"Athanasius, Tome to the Antiochenes (the Spirit not a creature; hypostases not to be pressed)",'npnf204',60054,"C2 alx add; no plain Trinity answer, nothing on tongues or healing.")
rec(w,['C2/S1','C2/S7'],'quote',"Athanasius, De Incarnatione 3 (God is good, the source of goodness)",'npnf204',16165,"C2 alx add: 'is God real' and 'where does evil come from' have no record.")
rec(w,['C5/S1'],'quote',"Eusebius, HE III.25 and Serapion on the Gospel of Peter (suppressed gospels)",'npnf201',17817,"C5 alx add: the 367 tiers are rendered; the suppressed gospels are loaded.")
rec(w,['C5/S8'],'quote',"Origen on Matt 16:28 (the Luke 9:27 'some standing here' verse)",'anf09',34066,"C5: the pilot's Luke 9:27 gap stands in all twelve worlds; alx has Origen on Matthew 16:28 loaded.")
rec(w,['C6/S1'],'quote',"how a bishop was chosen: Athanasius's election ('by general consent'; Egyptian bishops)",'npnf204',4429,"C6 alx: 'nothing rendered' on choosing a bishop; Jerome Ep. 146 (presbyters named the Alexandrian bishop) sits in hal's map.")
rec(w,['C7/S2','C7/S5'],'quote',"Dionysius of Alexandria on who may approach the table and on the Easter fast",'anf06',9724,"C7 alx: loaded and unrendered; the Easter fast text is at 9522. Thin on the meal.")
rec(w,['C7/S6'],'quote',"Anatolius, Paschal Canon",'anf06',14759,"C7 alx: loaded and unrendered; no calendar record (C12 gives the same line).")
rec(w,['C7/S7'],'quote',"Mark's liturgy naming Mary",'anf07',20549,"C7 alx: loaded, no record on Mary and the saints.")
rec(w,['C8/S1','C8/S2','C8/S4'],'quote',"Clement, Stromateis IV.8 'Women as Well as Men, Slaves as Well as Freemen'; 'women are therefore to philosophize equally with men'; Strom. II.23 On Marriage",'anf02',38538,"C8 alx: vendored in English and unrecorded; lines 38643 and 34787. alx.limit.marriage and the silence on women are contradicted. Strom. III is Latin only, so the limit is right about that.")
rec(w,['C9/S5'],'honest_limit',"Hypatia and the Serapeum (Socrates V.16, VII.15)",'npnf202',15667,"C9 alx add: nothing in any record; VII.15 is at 19548.")
rec(w,['C9/S4'],'quote',"Origen, Against Celsus VIII.73 ('we fight on his behalf')",'anf04',63038,"C9 alx: the only soldier answer, unquoted.")
rec(w,['C9/S1'],'quote',"Origen, Against Celsus III.8 (martyrs 'easily numbered'); the Thyestean charge (npnf201 line 27024)",'anf04',42965,"C9 alx: no catacombs, counts or accusations answer though both are vendored.")
rec(w,['C10/S7'],'quote',"Origen's four obols a day",'npnf201',32818,"C10 alx: work and class have no evidence beyond this.")
rec(w,['C11/S2','C11/S3'],'quote',"Origen, Against Celsus VII-VIII (gods as demons, festivals, idol-meat)",'anf04',None,"C11 alx add; thin on gods as demons, festivals and idol-meat; the Serapeum is in no record.")
rec(w,['C11/S1'],'contested_claim',"Jewish blame: Origen, Against Celsus (line 62905) and Athanasius (npnf204 line 36486) laid the Jews' losses on their guilt",'anf04',62905,"C11 alx add: 'a Jewish-blame contested_claim'; alx has no anti-Jewish polemic record.")
rec(w,['C12/S1','C12/S2'],'quote',"Clement, Paedagogus II (drinking, laughter, clothes); baths",'anf02',22382,"C12 alx add: a Clement quote on food and clothes with the not_for already used; lines 21673, 22382, 23729, 25254.")
rec(w,['C12/S1'],'story',"Doc_05 sec 6.2-6.3: the rhythm of the day, week and year, and the martyrs' era",None,None,"C12: never became records.")
rec(w,['C13/S3'],'quote',"Origen against Celsus on telling a true miracle from a false one",'anf04',None,"C13 alx must add: 'a miracle-discernment record'; no devil, demon, miracle, angel or saint record in 179.")
rec(w,['C13/S4'],'quote',"Hermas, Mandate 6.2: the two angels with every person",'anf02',2196,"C13 alx must add an angel record; lines 2196-2231.")
rec(w,['C13/S2','C13/S6'],'quote',"Antony on the weakness of magic and charms; Antony healing 'by the name'",'npnf204',33129,"C13 alx must add a demons record; lines 33129-33161 and 33320.")
rec(w,['C16/S5'],'quote',"figure quotes for Pantaenus, Demetrius, Heraclas, Didymus",None,None,"C16: zero quotes for each; Clement 9, Origen 6, Athanasius 4, Dionysius 3.")
rec(w,['C2/S4'],'honest_limit',"tongues",None,None,"C2 alx add: honest_limit for tongues.",group='no_text')
rec(w,['C6/S2'],'honest_limit',"Rome: a note that no Alexandrian record speaks to it",None,None,"C6 alx add: 'a Rome note'.",group='no_text')
rec(w,['C7/S1','C7/S3','C7/S4'],'honest_limit',"infants and mode; prayer; the room",None,None,"C7 alx: 'infants and mode' guarded only by dw.original-sin; prayer is one definition; the room is limit.material-remains only.",group='no_text')
rec(w,['C16/S2'],'contested_claim',"legend: alx's legend answer rests on one divergence note",None,None,"C16 alx: legend as such rests on one divergence note.",group='no_text')
rec(w,['C2/S1','C2/S2','C2/S6'],'fix',"several alx witnesses have empty retrieve_when",None,None,"C2 alx: 'Several alx witnesses have empty retrieve_when'; C2 not-checked: whether canon-cell routing reaches them.",group='fix')
rec(w,['C11/S1'],'not_for fix',"alx.quote.clement-schoolmaster: the not_for does not name the supersession reading, and the quote retrieves on 'whether people outside the church had anything true'",RP('alx.quote.clement-schoolmaster'),None,"C11 Jewish visitor: guard does not hold; bare, 'as the law [was] to the Hebrews' tells the visitor the Law was a custodian that has done its work. alx.term.christological-reading invites 'Jews read the same text without Christ'.",group='fix')
rec(w,['C8/S3'],'honest_limit',"the enslaved are only a guard in alx.term.oikos",None,None,"C8 alx: thin on the enslaved; abortion and rearing.",group='no_text')

# ---------------- cappadocian ----------------
w = 'cappadocian'
rec(w,['C2/S4'],'quote',"Gregory Nazianzen, Oration 31.26 (the Spirit's Godhead revealed by stages; Pentecost tongues)",'npnf207',34656,"C2 cappadocian add; lines 34656-34673.")
rec(w,['C2/S3'],'quote',"Gregory of Nyssa, On Not Three Gods",'npnf205',29315,"C2 cappadocian add: the 'three gods' objection.")
rec(w,['C2/S7'],'quote',"Gregory of Nyssa, Catechetical Oration V-VI ('no evil other than wickedness')",'npnf205',43116,"C2 cappadocian add; lines 43116-43124.")
rec(w,['C2/S8'],'honest_limit',"Basil's 'honour to the image' concerns the Son",None,None,"C2 cappadocian add.",group='no_text')
rec(w,['C5/S4'],'quote',"Basil, Hexaemeron I-III and Making of Man; Nyssa on Genesis 1",'npnf208',15203,"C5 cappadocian: 'registered, vendored, unquoted'; Nyssa at npnf205 line 33984. Add a Hexaemeron quote on days.")
rec(w,['C5/S5'],'honest_limit',"the end (Revelation)",None,None,"C5 cappadocian add: an honest_limit on the end. The canon list at npnf207 line 8395 is Cyril of Jerusalem's, not theirs.",group='no_text')
rec(w,['C6/S2'],'contested_claim',"Rome: Basil's appeals to Damasus",'npnf208',8159,"C6 cappadocian add: a Rome contested_claim.")
rec(w,['C6/S6'],'term',"deaconess (Lampadia in the Life of Macrina)",'nyssa-macrina',278,"C6 cappadocian add: a deaconess term; unrendered. The 381 communion law is named, not vendored.")
rec(w,['C7/S2'],'quote',"Basil, Letter 93: communion four times a week (Sunday, Wednesday, Friday, Sabbath) and on saints' days",'npnf208',29930,"C7 cappadocian: answers C7-17, 12 and part of 16; the record admits it does not supply the meal.")
rec(w,['C7/S6'],'quote',"Gregory Nazianzen, Oration 38 on Christmas",'npnf207',None,"C7 cappadocian: vendored; no Christmas record anywhere.")
rec(w,['C8/S3','C8/S7'],'quote',"Life of Macrina: a girl raised on Wisdom and the Psalter (L120); slave girls 'as if they were sisters' (L138, L158)",'nyssa-macrina',120,"C8 cappadocian: vendored and unrecorded.")
rec(w,['C8/S2'],'quote',"Gregory Nazianzen, Oration 37: 'They who made the Law were men'",'npnf207',35864,"C8 cappadocian.")
rec(w,['C8/S5'],'quote',"Basil's canons on abortion",'npnf208',34979,"C8 cappadocian (C15 gives the same canon at npnf214 line 43454, ten years' penance).")
rec(w,['C8/S4'],'quote',"Basil: marriage without a master's consent; Gangra canon 3",'npnf208',36510,"C8 cappadocian; Gangra can. 3 at npnf214 line 8641.")
rec(w,['C8/S8'],'quote',"Basil: a man who raises a hatchet against his wife in rage is a murderer, intent weighed",'npnf208',35123,"C8 S8 (Facilitator ground): a voice could say this truthfully after the redirect; do not speak it as advice.",fac=True)
rec(w,['C9/S4'],'quote',"Basil, Letter 188, canon 13: 'Homicide in war is not reckoned ... as homicide'",'npnf208',35312,"C9 cappadocian: soldiers are the gap; the Forty were serving soldiers.")
rec(w,['C10/S1','C10/S4','C10/S5'],'quote',"Basil's homilies in English extracts: Homily on Psalm 14 against usury (5069-5284), Homily VI on Luke 12 (6272), Homily VIII on the famine (6926); name the Prolegomena translator",'npnf208',5069,"C10: the biggest unused asset; records call the homilies 'unverified' and 'unacquired' but English extracts are vendored.")
rec(w,['C11/S3'],'quote',"Basil's Address to Young Men on Greek literature",'basil-address',None,"C11 cappadocian: vendored, unquoted.")
rec(w,['C11/S5'],'honest_limit',"whether a good pagan is saved",None,None,"C11 cappadocian: nothing, and Open_Gaps line 667 already says so; Nazianzen and Nyssa as the loaded ground.",group='no_text')
_extend('cappadocian', 32849, ['C12/S4'], "C12 cappadocian: gap on child death (the C12 report cites the treatise as npnf205 L443, the other reports as 32849).")
rec(w,['C12/S2'],'story',"Doc_05 sec 1: cold plateau, indigenous speech beside church Greek, charms, slave-exporting region",None,None,"C12 cappadocian: none recorded.")
rec(w,['C13/S2','C13/S6'],'quote',"Laodicea canon 36; Nazianzen's exorcism notes",'npnf214',12513,"C13 cappadocian: nothing on demons, angels or magic though both are vendored; Nazianzen at npnf207 lines 1654-2054.")
rec(w,['C16/S5'],'quote',"Gregory Nazianzen (Theological Orations) and Macrina in her own words",'npnf207',None,"C16 cappadocian: Basil 17 quotes, Nyssa 3, Nazianzen 0, Macrina 0, with the Theological Orations vendored.")
rec(w,['C13/S5'],'term fix',"cappadocian.term.martys-martyrion: the not_for says this world 'denied' worship of martyrs, with the Basil and Nyssa martyr homilies unacquired",RP('cappadocian.term.martys-martyrion'),None,"C13: 'Must add: a source for that denial, or soften the line'.",group='fix')
rec(w,['C8/S3'],'fix',"cappadocian.story.slave-market-sermon rests on Nyssa's Ecclesiastes homily, which is unvendored; the line is a paraphrase",RP('cappadocian.story.slave-market-sermon'),None,"C8 finding 2.",group='fix')
rec(w,['C10/S1','C10/S4'],'source-record fix',"cappadocian.dw.wealth-answerable-to-the-poor / term.pleonexia say the famine homilies are 'unverified' and 'unacquired' although English extracts are vendored",RP('cappadocian.dw.wealth-answerable-to-the-poor'),None,"C10: the source records are stale against npnf208.",group='fix')
rec(w,['C7/S2'],'source-record fix',"cappadocian.source.liturgy-of-st-basil registered unvendored, but the Neale volume is mapped",RP('cappadocian.source.liturgy-of-st-basil'),None,"C7 cappadocian S2: the registration is stale.",group='fix')

# ---------------- desert ----------------
w = 'desert'
rec(w,['C2/S7'],'quote',"Vita Antonii 22: 'God made nothing evil'",'npnf204',31789,"C2 desert add; lines 31789-31792.")
rec(w,['C2/S2'],'quote',"Cassian, Conference X.4: anger ascribed to God is figurative",'npnf211',22581,"C2 desert add; the same line serves gallic.")
rec(w,['C5/S6'],'quote',"Vita Antonii 3 (access to Scripture)",'npnf204',31296,"C5 desert add.")
rec(w,['C6/S4','C6/S6','C6/S7'],'honest_limit',"absence records for tradition and succession, married clergy, the emperor",None,None,"C6 desert add: absence records for S4, S6 and S7. Loaded: Paphnutius of the Thebaid at Nicaea (npnf202 line 3763); Constantine's letter to Antony (Vita 81, npnf204 line 33185).",group='no_text')
rec(w,['C7/S5'],'quote',"Cassian, Conference 2 on disclosing thoughts",'npnf211',18790,"C7 desert; Basil Letter 93 (solitaries commune at home) is not mapped to this world.")
rec(w,['C9/S3'],'quote',"Vita Antonii 81: emperors write to Antony",'npnf204',33185,"C9 desert: no empire answer; unrendered.")
rec(w,['C9/S4'],'honest_limit',"soldiers: nothing in the desert world",None,None,"C9 desert: 'nothing on soldiers'.",group='no_text')
rec(w,['C10/S7'],'quote',"Palladius ch. XXXII: the Panopolis trades (15 tailors, 7 smiths, 4 carpenters, 15 fullers)",'lausiac',405,"C10 desert: unrendered.")
rec(w,['C11/S2'],'quote',"the heathen-priest sayings",None,None,"C11 desert: loaded and unrendered; nothing on Jews or pagans otherwise.")
rec(w,['C12/S4'],'quote',"Pachomian Rules: the prior serving the sick",'pachomius',194,"C12 desert: no record on sickness.")
rec(w,['C12/S8'],'honest_limit',"archaeology: the Kellia excavation (1,500 structures) is unvendored; desert.term.kellion names the dig",None,None,"C12 desert: S8 has no honest_limit.",group='no_text')
rec(w,['C12/S3','C12/S6'],'story',"Doc_05 sec 4-5: Nitria-Kellia one day's walk (19 km); the weekly synaxis ends in a shared meal",None,None,"C12 desert: unrecorded.")
rec(w,['C13/S2'],'quote',"the Sayings: a demon or a vision (Sisoes)",'budge2',82,"C13 desert must add a story from the Sayings (anan-isho_paradise-v2 line 82); Lausiac History also unused for demons.")
rec(w,['C13/S5'],'honest_limit',"relics beyond Antony's secret burial",None,None,"C13 desert must add.",group='no_text')
rec(w,['C13/S2'],'honest_limit',"whether the desert fathers took the beast-demons literally",None,None,"C13 desert must add 'an honest_limit on literal belief' (C13-19).",group='no_text')
rec(w,['C13/S2'],'fix',"desert.story.antony-tomb-combat: the absent_detail calls the beasts 'this world's own chosen register for interior struggle ... not a claim about literal events'",RP('desert.story.antony-tomb-combat'),None,"C13: a modern reading; no vendored line settles it; gallic.term.the-devil-demons says real and visible.",group='fix')
rec(w,['C10/S2'],'overstated honest_limit',"desert.limit.tithe (Documented) says no source names a tithe; its check covered only the Vita and Palladius",RP('desert.limit.tithe'),None,"C10: Cassian Conference XXI (npnf211 44550-44680), mapped to this world, discusses tithes and first-fruits and says renouncers go beyond them. Narrow the limit or add the passage.",group='fix')
rec(w,['C5/S4','C5/S8'],'overstated honest_limit',"desert.limit.f2-scripture-detail says no source records a desert voice on Genesis",RP('desert.limit.f2-scripture-detail'),None,"C5: Cassian Conference X (npnf211 line 35878), which its own Sarapion story uses, is that debate.",group='fix')
rec(w,['C6/S8','C9/S6'],'status fix',"desert.limit.communal-wrong-unrepaired is still draft",RP('desert.limit.communal-wrong-unrepaired'),None,"C6 and C9 desert.",group='fix')
rec(w,['C7/S5'],'tag fix',"the fasting card tag traces only to desert.core.desert",RP('desert.core.desert'),None,"C7 desert: fasting rests on the Pachomian tablet.",group='fix')

# ---------------- don ----------------
w = 'don'
rec(w,['C2/S4'],'quote',"Parmenian's 'third Endowment, the Spirit, in the water'",'optatus',1397,"C2 don add; read in the editor's context.")
rec(w,['C2/S1','C2/S2','C2/S7','C2/S8'],'honest_limit',"God's nature and evil",None,None,"C2 don add: S1, S2, S7, S8 empty.",group='no_text')
rec(w,['C5/S2'],'quote',"Tyconius, Liber Regularum (the world's only interpreter)",'tyconius',247,"C5 don: vendored and unread. The 4-cluster acquire list carried it as a download; it is not one.")
rec(w,['C6/S2'],'quote',"Optatus on Peter's keys and chair",'optatus',145,"C6 don: unrendered; lines 145, 153.")
rec(w,['C6/S2'],'honest_limit',"Rome: one note (the primate was no pope)",None,None,"C6 don add.",group='no_text')
rec(w,['C7/S2'],'quote',"Acta of Saturninus: 'we cannot live without the dominicum'",'pl8',1781,"C7 don: vendored in Latin (lines 1781, 2974) although the source record says unvendored.")
rec(w,['C8/S3'],'contested_claim',"Augustine, Ep. 185: Donatist protection let slaves destroy their debt papers and 'depart in freedom'",'npnf104',19482,"C8 don: the only vendored word on the enslaved is hostile; needs a contested_claim, not a witness.")
rec(w,['C9/S2','C9/S5'],'contested_claim',"Circumcellion martyr-seeking: Augustine Letter 133 and City of God XIX.6 (the torturing judge)",'npnf101',45893,"C9 don: mapped and unframed; the world cannot answer. CoG XIX.6 at npnf102 line 38301. Also bears on C3 R-20.",fac=True)
rec(w,['C10/S5','C10/S7'],'contested_claim',"Optatus III.4: Axido and Fasir wiping out debts (hostile)",'optatus',2002,"C10 don: loaded, unused.")
rec(w,['C12/S2'],'quote',"Punic as the common language at Fussala",'npnf104',10597,"C12 don: unrecorded and vendored.")
rec(w,['C12/S4'],'quote',"epitaphs with ages at death (CIL VIII Suppl.)",None,None,"C12 don: unrecorded and vendored; the report gives line 420 of a CIL file without naming the file.")
rec(w,['C13/S5'],'honest_limit',"the martyr cult: what happened at the graves",None,None,"C13 don must add; the church of the martyrs is this world's centre and no record says.",group='no_text')
rec(w,['C16/S5'],'quote',"Augustine, Optatus, Tyconius, Parmenian in the Donatist world",'optatus',None,"C16 don: worst S5 world: 26 figure records, 5 quotes; Donatus, Petilian, Emeritus one each; those four zero.")
rec(w,['C13/S5'],'duplicate fix',"don.story.macrobius-letter and don.story.macrobius-letter-isaac-maximianus are one story twice",RP('don.story.macrobius-letter'),None,"C13: 'duplicate drift to fix, not a second witness'.",group='fix')
rec(w,['C6/S7','C9/S2'],'status fix',"don.quote.donatus-quid-est-imperatori is draft and half verified: English at Vassall-Phillips line 1904, Latin found only in Ziwsa's word index (optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt line 3357 per C9; critical-edition index line 23707 per C15)",RP('don.quote.donatus-quid-est-imperatori'),None,"C6, C9, C15: the verbatim check is PARTIAL.",group='fix')
rec(w,['C16/S5'],'quote fix',"don.quote.emeritus-magno-argumento: Latin not findable in the OCR-noisy pl11 file ('argumento' occurs nine times, never with 'veritas occultatur')",RP('don.quote.emeritus-magno-argumento'),None,"C16 verification: UNRESOLVED; hand check needed by the don thread.",group='fix')
rec(w,['C9/S2'],'status fix',"the Bagai violence limit is draft",RP('don.limit.bagai-violence-no-account'),None,"C9 don.",group='fix')
rec(w,['C7/S2'],'source-record fix',"don.source.acta-saturnini-abitinian-martyrs registered unvendored; the Latin is vendored",RP('don.source.acta-saturnini-abitinian-martyrs'),None,"C7, C9, C13.",group='fix')

# ---------------- gallic ----------------
w = 'gallic'
rec(w,['C2/S1'],'quote',"Salvian: 'deny his very existence'",'salvian',5236,"C2 gallic add.")
rec(w,['C2/S2'],'quote',"Cassian, Conference X.4",'npnf211',22581,"C2 gallic add.")
rec(w,['C5/S2'],'quote',"Cassian, Conference XIV: the four senses",'npnf211',38874,"C5 gallic add: nothing on how they read.")
rec(w,['C5/S3','C5/S7'],'honest_limit',"reliability of Scripture; violence in the texts",None,None,"C5 gallic add: honest_limits.",group='no_text')
rec(w,['C6/S6'],'quote',"Synod of Orange 441, canon 26: 'Deaconesses shall no longer be ordained'",'hefele3',8855,"C6 gallic: in ijc's map only; add a map row.")
rec(w,['C7/S7'],'quote',"Cassian: the dismissal of the catechumens",'npnf211',24682,"C7 gallic: the unbaptised visitor.")
rec(w,['C8/S2'],'quote',"Martin and the queen",'npnf211',4187,"C8 gallic: loaded, no record on women's authority.")
rec(w,['C8/S3'],'quote',"Salvian on slaves and concubines",'npnf211',4048,"C8 gallic: loaded; the second place is L4930 (the report cites the npnf211 file for both).")
rec(w,['C10/S2'],'quote',"Cassian, Conference XXI on tithes",'npnf211',44550,"C10 gallic: nothing on tithes; Conference XXI is loaded.")
rec(w,['C10/S5'],'quote',"Cyprian, De lapsis: bishops 'multiplying usuries'",'anf05',43784,"C10 gallic.")
rec(w,['C10/S6'],'honest_limit',"who paid for bishops",None,None,"C10 gallic: nothing on who paid.",group='no_text')
rec(w,['C11/S5'],'quote',"a good pagan's fate",None,None,"C11 gallic: nothing; LOADED.")
rec(w,['C11/S1'],'honest_limit',"Jews: the Gallic voices say almost nothing",None,None,"C11: gallic has no record on Jews; Severus of Minorca (418) sits on the world's southern edge.",group='no_text')
rec(w,['C12/S1','C12/S2'],'story',"Doc_05 sec 1.2: dress, food, sleep, cell, labour, climate",None,None,"C12 gallic: the richest daily-life text in the fleet became only a handful of records. Caution: Cassian's dress and food rules describe Egypt, not Gaul.")
rec(w,['C13/S2','C13/S4'],'quote',"Cassian, Conferences VII and VIII (demons; On Principalities)",'npnf211',32132,"C13 gallic: vendored and cited by no record; VIII at 33442.")
rec(w,['C13/S7'],'quote',"Agnes, Thecla and Mary visiting Martin",'npnf211',4554,"C13 gallic: the only near-S7 material.")
rec(w,['C16/S5'],'quote',"Honoratus",None,None,"C16 gallic: zero quotes.")
_extend('gallic', 48467, ['C2/S3'], "C2 gallic names the same stale record.", group='fix')
rec(w,['C1/*'],'quote fix',"gallic.quote.salvian-free-men-in-seeming-captivity: failed the verbatim match on the second C1 pass and was not re-verified by any later report",RP('gallic.quote.salvian-free-men-in-seeming-captivity'),None,"C1 pass 2: MISMATCH. The sentence is in salvian_on-the-government-of-god_sanford1930.txt at line 6458 across a line-end hyphen ('seem-ing'); found by grep while building this list, not a formal check. The other three Salvian quotes and both Macarian quotes from the same C1 note were matched in C2, C3, C4, C10 and C12.",group='fix')

# ---------------- hal ----------------
w = 'hal'
rec(w,['C2/S3'],'quote',"Ep. XV to Damasus on three hypostases",'npnf206',5002,"C2 hal add; written c.376, before the 382 window.")
rec(w,['C2/S4'],'quote',"Ep. XLI on Montanism",'npnf206',8270,"C2 hal add.")
rec(w,['C2/S8'],'quote',"Epiphanius and the painted curtain",'npnf206',11100,"C2 hal add.")
rec(w,['C2/S7','C2/S2'],'honest_limit',"evil and God's character",None,None,"C2 hal add.",group='no_text')
rec(w,['C5/S7','C5/S8'],'quote',"Jerome Ep. 22.6: Psalm 137 'dash the little ones' read as crushing evil thoughts",'npnf206',5607,"C5 hal add: the ready answer to Psalm 137.")
rec(w,['C6/S2'],'quote',"Jerome: 'I communicate with none but your blessedness, that is with the chair of Peter'",'npnf206',5050,"C6 hal add.")
rec(w,['C6/S1'],'quote',"Jerome Ep. 146: presbyters chose the bishop",'npnf206',None,"C6 hal add; vendored and unquoted.")
rec(w,['C7/S2','C7/S6'],'quote',"Letter 71 section 6: daily communion and the Sabbath fast",'npnf206',16963,"C7 hal.")
rec(w,['C7/S7'],'quote',"Against Vigilantius on relics",'npnf206',22279,"C7 hal.")
rec(w,['C8/S4'],'quote',"Jerome Ep. 55: a wife left an adulterer and sodomite and remarried; 'he is still her husband'",'npnf206',12992,"C8 hal: stricter than the Fabiola story; lines 12992-13029. hal.dw.marriage-ending is gentler than Jerome's own answer.")
rec(w,['C8/S5'],'quote',"Ep. 22 on potions for barrenness",'npnf206',5787,"C8 hal: unrecorded.")
rec(w,['C11/S3'],'quote',"Ep. 70 on quoting pagan authors",'npnf206',None,"C11 hal (C11-21): loaded and unrendered.")
rec(w,['C11/S1'],'quote',"Jerome's own lines on the Jews",'npnf206',8405,"C11 hal: unrendered.")
rec(w,['C12/S5'],'quote',"Letter 39 on Blesilla; Letter 60 (consolation on Nepotian's death)",'npnf206',7763,"C12 hal: vendored and unrecorded.",fac=True)
rec(w,['C12/S1'],'quote',"Letter 22 on wine",'npnf206',None,"C12 hal.")
rec(w,['C13/S5'],'quote',"Letter 109 to Riparius; Letter 108 on Paula at the holy places",'npnf206',22242,"C13 hal must add a relics and intercession record; Ep. 108 at line 20791. The Paula quote is about pilgrimage, not relics.")
rec(w,['C13/S6'],'quote',"Life of Hilarion: demons at Gaza, the magician's spells",'npnf206',29725,"C13 hal: hal.story.desert-romances names the work and quotes none of it.")
rec(w,['C16/S1'],'doctrinal_witness',"where the record as a whole is thinnest",None,None,"C16 hal: no record says it.",group='no_text')
rec(w,['C16/S5'],'quote',"Paula, Marcella, Pammachius",None,None,"C16 hal: zero quotes; Jerome 19, Augustine 2.")
rec(w,['C2/S5'],'retrieve_when fix',"hal.dw.authority retrieves only on 'who appointed bishops', not on the council-vote question",RP('hal.dw.authority'),None,"C2 hal add.",group='fix')
rec(w,['C7/S7'],'tag fix',"the 'Saints and holy places' card tag traces to hal.dw.record, not a saints record",RP('hal.dw.record'),None,"C7 hal.",group='fix')
rec(w,['C11/S1'],'not_for fix',"hal.story.oea-gourd: the Jewish residents answered 'whether from ignorance or spite' (Augustine Ep. 71.5, line 32546) and the not_for does not stop that",RP('hal.story.oea-gourd'),None,"C11 Jewish visitor: guard fails.",group='fix')

# ---------------- ijc ----------------
w = 'ijc'
rec(w,['C2/S5'],'quote',"the 381 creed",'npnf214',13393,"C2 ijc add; the only in-window filioque text is Ambrose below.")
rec(w,['C2/S5'],'quote',"Ambrose on the Spirit 'from the Father and the Son'",'npnf210',12068,"C2 ijc add; lines 12068-12070.")
rec(w,['C5/S3','C5/S4','C5/S5','C5/S7'],'honest_limit',"honest_limits for reliability, Genesis, Revelation and violence",None,None,"C5 ijc add: 'Everything else is loaded and unrecorded'.",group='no_text')
rec(w,['C5/S8'],'quote',"Leo, Sermon 51 on Luke 9:27",'npnf212',17800,"C5 ijc add.")
rec(w,['C6/S6'],'term',"deaconess (Chrysostom on a deaconess; Orange 441)",'hefele3',8855,"C6 ijc add; no term for presbyter or deacon.")
rec(w,['C8/S4'],'quote',"CTh 3.7.2 (no Jew to take a Christian woman: 'adulterii vicem') and 3.7.1 (young widows)",'codex-theod',942,"C8 ijc: vendored and unrecorded; 3.7.1 at line 940.")
rec(w,['C8/S3','C8/S7'],'quote',"CTh 4.7.1 (freedom given in church) and 5.10.1 (a bought foundling may be kept in servitude)",'codex-theod',1182,"C8 ijc; 5.10.1 at line 1496.")
rec(w,['C8/S2'],'quote',"Sozomen's deaconess",'npnf202',43214,"C8 ijc.")
rec(w,['C10/S5'],'quote',"Leo's letter on usury",'npnf212',1549,"C10 ijc.")
rec(w,['C10/S4'],'quote',"Ambrose on ransoming captives",'npnf210',None,"C10 ijc.")
rec(w,['C11/S1'],'quote',"Ambrose Ep. 40 ('a home of unbelief')",'npnf210',43280,"C11 ijc: unrendered.")
rec(w,['C12/S5'],'quote',"CTh 9.17 on tomb violation; Ambrose's grief for Satyrus (npnf210 line 651)",'codex-theod',3332,"C12 ijc.",fac=True)
rec(w,['C13/S5'],'quote',"Ambrose Ep. 22: the finding of Gervasius and Protasius",'npnf210',42690,"C13 ijc must add an Ambrose relics record.")
rec(w,['C16/S5'],'quote',"Damasus, Pulcheria, Marcian",None,None,"C16 ijc: zero quotes; Ambrose 6, Leo 5, Constantine 3.")
rec(w,['C13/S5'],'retrieve_when fix',"ijc.quote.jerome-damasus-verses is retrieved on 'tombs of the martyrs' but its text is about verse-making",RP('ijc.quote.jerome-damasus-verses'),None,"C13: a trap; fix the Damasus retrieve_when.",group='fix')
rec(w,['C7/S1'],'retrieve_when fix',"ijc.dw.original-sin-transmitted is tagged to 'did you baptise babies' yet is Leo on inherited sin",RP('ijc.dw.original-sin-transmitted'),None,"C7 ijc: that question retrieves nothing about infants.",group='fix')
rec(w,['C11/S1'],'not_for fix',"ijc.limit.earlier-windows says 'our own bishop kept unpunished'; ijc.story.callinicum-synagogue has the Callinicum bishop urging it and Ambrose shielding it",RP('ijc.limit.earlier-windows'),None,"C11 Jewish visitor: one blur.",group='fix')
rec(w,['C12/S7'],'not_for fix',"ijc.quote.happy-christian-emperors is about rulers; do not use it for 'were you happy'",RP('ijc.quote.happy-christian-emperors'),None,"C12 ijc.",group='fix')

# ---------------- lpc ----------------
w = 'lpc'
rec(w,['C2/S7'],'quote',"Confessions VII 'Whence is evil?'",'npnf101',10384,"C2 lpc add (when the world is built).")
rec(w,['C2/S1'],'quote',"Augustine on Psalm 14",'npnf108',2608,"C2 lpc add.")
rec(w,['C2/S3'],'quote',"the Maximinus debate",'collatio',None,"C2 lpc add; the Latin is vendored (augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt).")
rec(w,['C5/S1'],'quote',"Augustine, De Doctrina Christiana II: the canon and the Apocrypha",'npnf102',None,"C5 lpc add.")
rec(w,['C5/S8'],'quote',"Tractate 1 on John (npnf107 line 498); Sermon on the Mount II.25 (npnf106 line 3117)",'npnf107',498,"C5 lpc add: quotes for Tractate 1 and Sermon on the Mount II.25.")
rec(w,['C5/S7','C5/S8'],'quote',"Augustine on Psalm 137",'npnf108',27073,"C5 lpc add.")
rec(w,['C7/S2','C7/S6'],'quote',"Letter 54 to Januarius: the yearly solemnities; some take communion daily, some do not dare",'npnf101',29897,"C7 lpc: no meal or calendar record; line 30000 also.")
rec(w,['C8/S3'],'quote',"City of God XIX.15: 'the condition of slavery is the result of sin'",'npnf102',38914,"C8 lpc: loaded.")
rec(w,['C8/S7'],'quote',"Cyprian to Fidus on infants",'anf05',35860,"C8 lpc: lines 35860-35947.")
rec(w,['C8/S1'],'quote',"Augustine Ep. 211 to the nuns; Perpetua's own prison account",'npnf101',54738,"C8 lpc: Perpetua (anf03 line 59560) is mapped to lpc and excluded as pre-246.")
rec(w,['C9/S4','C9/S5'],'quote',"Letter 133 on sparing the Circumcellions; City of God XIX.6 on the torturing judge",'npnf101',45893,"C9 lpc: mapped and unframed; they answer the death penalty and the torturer's side. CoG XIX.6 at npnf102 line 38301.")
rec(w,['C10/S2','C10/S3','C10/S5','C10/S6','C10/S7'],'quote',"Cyprian on usury, stipends and Acts 4; Augustine on tithes, the common life, and actors and trades",'anf05',None,"C10 lpc: the loaded library is richest here and unrendered; all draft.")
rec(w,['C11/S1','C11/S3','C11/S5'],'quote',"Cyprian, Ad Quirinum; City of God (Jews, gods, philosophy)",'anf05',None,"C11 lpc: none on Jews, gods or philosophy; hostile text mapped.")
rec(w,['C12/S5'],'quote',"Augustine, On Care to Be Had for the Dead; Monica's death",'npnf103',43495,"C12 lpc; Monica's death at npnf101 line 13842.",fac=True)
rec(w,['C12/S1','C12/S4'],'quote',"Cyprian on virgins and mixed baths (Latin); Perpetua's nursing infant (Latin)",'anf05',None,"C12 lpc: Latin.")
rec(w,['C13/S3','C13/S5'],'quote',"City of God XXII.8: the miracles at Hippo; relics of Stephen",'npnf102',45632,"C13 lpc: lines 45632-45679; belongs to the LPC thread.")
rec(w,['C13/S6'],'quote',"Augustine: amulets and incantations with Christ's name",'npnf107',1649,"C13 lpc: lines 1649, 1701.")
rec(w,['C13/S7'],'quote',"Augustine, On Care for the Dead: the dead appearing in dreams",'npnf103',44050,"C13 lpc.",fac=True)
rec(w,['C16/S3'],'source-record fix',"lpc's 210 source records carry an edition but no citation field or kind",None,None,"C16 lpc.",group='fix')
rec(w,['C16/S2'],'doctrinal_witness',"the legend question in the visitor's wording",None,None,"C16 lpc: no witness meets it; Pontius, Celerinus, Lucian, Numidicus zero quotes.",group='no_text')
rec(w,['C6/S1','C9/S1','C15/*'],'status fix',"all 330 lpc records are status: draft, with no use_note, so no guards exist",None,None,"C6, C9, C12, C15: nothing is packaged (not checked); C15: every lpc cell is NL or LO until this changes.",group='fix')
rec(w,['C9/S6'],'canon tag fix',"lpc.demo.compel-three-phase (status draft) carries canon_question_id f3-p-02 but its participant line is the hypocrites question",RP('lpc.demo.compel-three-phase'),None,"C9.",group='fix')
rec(w,['C11/S1'],'honest_limit',"Jews: lpc has no record while Cyprian Ad Quirinum and Augustine's witness-people are mapped",None,None,"C11 Jewish visitor: the voice would improvise.",group='no_text')

# ---------------- pahc ----------------
w = 'pahc'
rec(w,['C2/S1'],'quote',"Tatian: 'He alone is without beginning'",'anf02',5833,"C2 pahc add; lines 5833-5836.")
rec(w,['C2/S3'],'quote',"Theophilus: 'types of the Trinity'",'anf02',8992,"C2 pahc add.")
rec(w,['C2/S4'],'quote',"Justin, Dialogue 82; Irenaeus V.6.1 'speak all kinds of languages'",'anf01',22231,"C2 pahc add; Irenaeus at line 51060.")
rec(w,['C2/S8'],'quote',"Tertullian, On Idolatry",'anf03',4962,"C2 pahc add.")
rec(w,['C5/S8'],'quote',"Irenaeus III.11; 2 Clement 4; Tertullian against Marcion IV on the Sermon",'anf01',40845,"C5 pahc: unrecorded; 2 Clement 4 at anf09 line 17831, Tertullian at anf03 line 30694.")
rec(w,['C6/S4'],'quote',"Irenaeus III.3 succession lists",'anf01',None,"C6 pahc: vendored and unrendered.")
rec(w,['C7/S3','C7/S5','C7/S7'],'quote',"the Lord's Prayer thrice daily; the Wednesday and Friday fast; the baptised-only rule",'anf07',12937,"C7 pahc: unrendered; the baptised-only rule at line 12970 is the vendored answer to C7-27.")
rec(w,['C8/S5','C8/S7'],'quote',"Justin 1 Apology 27 and 29 (exposed children; a petition to a surgeon); Athenagoras 35 (abortion is murder)",'anf01',14973,"C8 pahc: Justin at 14973 and 15045; Athenagoras at anf02 line 13350.")
rec(w,['C8/S2'],'quote',"Acts of Paul and Thecla: 'Go, and teach the word of God'",'anf08',48096,"C8 pahc: Thecla is mapped here.")
rec(w,['C9/S4'],'quote',"Justin on swords into ploughshares",'anf01',15403,"C9 pahc: soldiers; unrendered.")
rec(w,['C9/S3'],'quote',"Justin on taxes",'anf01',14581,"C9 pahc.")
rec(w,['C10/S7'],'quote',"Tertullian, De idololatria on barred trades (schoolmasters 5484; military service 6145)",'anf03',4968,"C10 pahc: lines 4968-6200.")
rec(w,['C10/S2'],'quote',"Polycarp 10: 'alms delivers from death'",'anf01',3512,"C10 pahc.")
rec(w,['C11/S1'],'quote',"Justin, Dialogue 47: Jewish Christians 'will be saved'; Barnabas; the Dialogue with Trypho",'anf01',None,"C11 pahc: unrendered.")
rec(w,['C12/S5'],'quote',"Diognetus ('common table, but not a common bed'); Aristides on burying a poor man; Tertullian on funeral incense",'anf01',2735,"C12 pahc: Aristides at line 2853; Tertullian at anf03 line 4148.",fac=True)
rec(w,['C13/S7'],'quote',"Perpetua's vision of her dead brother Dinocrates",'anf03',59700,"C13 pahc: the best S7 text in the fleet, unrecorded; lines 59700-59740.",fac=True)
rec(w,['C13/S2'],'quote',"Justin on exorcism; Irenaeus II.32.4",'anf01',16966,"C13 pahc: no pahc record mentions exorcism.")
rec(w,['C13/S6'],'quote',"Ignatius, Ephesians 19: 'all magic was dissolved'",'anf01',5496,"C13 pahc.")
rec(w,['C16/S5'],'quote',"Polycarp and Papias",'anf01',None,"C16 pahc: zero quotes; the Martyrdom and Polycarp's letter are vendored.")
rec(w,['C11/S1'],'not_for fix',"pahc.quote.polycrates-to-victor has no Jewish guard (Passover date)",RP('pahc.quote.polycrates-to-victor'),None,"C11 Jewish visitor.",group='fix')
rec(w,['C6/S6','C15/S6'],'source-record fix',"pahc.quote.two-female-slaves-who-were-called-deaconesses: verbatim at npnf201 lines 19502-19506 but inside the NPNF editor's endnote; the record names a Pliny source that is not vendored",RP('pahc.quote.two-female-slaves-who-were-called-deaconesses'),None,"C15 verification: needs a hand check; C6 warns the title is Pliny's.",group='fix')

# ---------------- rzg ----------------
w = 'rzg'
rec(w,['C2/S3','C2/S5'],'quote',"Second Helvetic Confession ch. 3 (Trinity, filioque) with a not_for for the line condemning 'the Jews and Mohammedans'",'schaff-helv',458,"C2 rzg add; lines 458-472.")
rec(w,['C2/S8'],'quote',"Second Helvetic Confession ch. 4 on images",'schaff-helv',479,"C2 rzg add: images are the one cell rendered (refusal) but no record states the doctrine.")
rec(w,['C2/S3'],'quote',"Calvin, Institutes I.13.5",'calvin1',11242,"C2 rzg add.")
rec(w,['C2/S7'],'quote',"Second Helvetic Confession ch. 7 on evil",'schaff-helv',534,"C2 rzg add.")
rec(w,['C5/S4','C15/S2'],'quote',"Calvin on Genesis 1: accommodation ('Moses wrote in a popular style')",'calvin-gen1',4428,"C5 rzg: nothing on canon, translation or Genesis; accommodation passages at lines 4104 and 4428; C15: the strongest science-and-Scripture text in the library, unquoted.")
rec(w,['C6/S2'],'quote',"Calvin Institutes IV.6 on 'Thou art Peter'",'calvin3',4943,"C6 rzg: Rome appears only as the foil for sola scriptura; Zwingli on Matt. 16 also unrendered.")
rec(w,['C6/S6'],'quote',"Zwingli's petition for married priests; Calvin on deacons",'zwingli-sel',968,"C6 rzg: add quotes for Calvin on the papacy and on deacons.")
rec(w,['C7/S6'],'quote',"Second Helvetic Confession XXIV (feasts and fasts)",'schaff-helv',None,"C7 rzg: no record on prayer, calendar or the Sunday.")
rec(w,['C7/S3'],'quote',"Institutes III.20 on prayer",'calvin2',None,"C7 rzg.")
rec(w,['C8/S4','C10/S1'],'quote',"Calvin Institutes (vol1 line 25853; vol3 line 11100) and Second Helvetic ch. XXIX on marriage",'calvin1',25853,"C8 rzg: vendored; the limit says the teaching cannot be given.")
rec(w,['C9/S5'],'contested_claim',"Servetus: the hardest true thing about Geneva",'rilliet',None,"C9 and C14: named only in a parenthesis; Tweedie, Calvin and Servetus (550 hits), Calvin Opera vol. 8 and Letters vol. 2 are vendored and mapped. Add a Servetus record.")
rec(w,['C9/S4','C9/S5'],'quote',"Second Helvetic Confession XXX ('punish ... incorrigible heretics'; wars 'only in self-defense'); Institutes IV.20",'schaff-helv',1568,"C9 rzg: unquoted.")
rec(w,['C10/S4'],'quote',"Calvin Institutes (vol. 3) on deacons and the poor",'calvin3',2436,"C10 rzg.")
rec(w,['C10/S2','C10/S5','C10/S3'],'quote',"Zwingli on tithes, usury and Anabaptist community of goods",'zwingli-sel',5519,"C10 rzg: also zwingli_latin-works vol. 3 line 5478.")
rec(w,['C11/S4'],'honest_limit',"Muslims: no record in an Islamic-era world",None,None,"C11 rzg: in window (1519-1650) and no Muslim record; Lucaris letters are mapped and unused.",group='no_text')
rec(w,['C11/S1'],'honest_limit',"Jews: no record while Calvin's 'whose blindness is well known' is mapped",None,None,"C11 Jewish visitor: hostile text mapped, no record.",group='no_text')
rec(w,['C12/S4'],'quote',"Calvin's letters on plague; the Ordonnances' visitation of the sick",'bonnet1',217,"C12 rzg: sickness, burial and the 'point' are L only.",fac=True)
rec(w,['C12/S7'],'quote',"Geneva Catechism, first question",'geneva-cat',229,"C12 rzg.")
rec(w,['C13/S1','C13/S4'],'quote',"Calvin Institutes I.14 on the devil and angels",'calvin1',12881,"C13 rzg must add records for S1, S4, S5, S6; lines 12881-12932.")
rec(w,['C13/S5'],'quote',"Calvin Institutes ch. XX on the intercession of saints; Zwingli on invocation of saints",'calvin3',23294,"C13 rzg.")
rec(w,['C13/S6'],'honest_limit',"magic, amulets, curses",None,None,"C13 rzg must add; Treatise on Relics is OTHER.",group='no_text')
rec(w,['C16/S1'],'doctrinal_witness',"what the record holds and where it thins",None,None,"C16 rzg: thin across the row; no witness says it.",group='no_text')
rec(w,['C16/S5'],'quote',"Beza, Farel (figure records, zero quotes)",None,None,"C16 rzg: six quotes in all (Zwingli 2, Calvin 2, Bullinger 1, Myconius 1).")
rec(w,['C8/S4','C10/S1','C15/S1'],'overstated honest_limit',"rzg.limit.no-teaching-on-wealth-or-marriage",RP('rzg.limit.no-teaching-on-wealth-or-marriage'),None,"C8, C10, C15: true of the records but not of the library; Calvin's Institutes, the Second Helvetic ch. XXIX and Zwingli on tithes, usury and community of goods are vendored. C15 asks to reconcile with Calvin's commentary.",group='fix')
rec(w,['C9/S6','C16/S1'],'canon tag fix',"the three rzg demonstrations (rzg.demo.consensus-contest, rzg.demo.predestination-and-dread, rzg.demo.why-we) all carry empty canon_cells; consensus-contest is the f2-e-01 demonstration",RP('rzg.demo.consensus-contest'),None,"C9 and C16; rzg.demo.why-we is also the mis-tagged c-t-03 row in the 4-cluster list.",group='fix')
rec(w,['C5/S6'],'source-record fix',"rzg.source.genevan-psalter says unvendored; marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt is mapped",RP('rzg.source.genevan-psalter'),None,"C5 rzg S6.",group='fix')

# ---------------- syr ----------------
w = 'syr'
rec(w,['C2/S1'],'quote',"Tatian",'anf02',5835,"C2 syr add.")
rec(w,['C2/S4'],'quote',"Ephrem on fire and the Spirit at baptism",'npnf213',20580,"C2 syr add.")
rec(w,['C5/S7'],'quote',"Ephrem against Marcion on the violence of the God of the Old Testament",'ephrem-prose',1854,"C5 syr.")
rec(w,['C6/S2'],'quote',"Doctrine of Addai: the ordination chain from Cephas through Rome and Antioch to Palut",'addai',89,"C6 syr add: the fleet's only Syriac Rome text, unrendered.")
rec(w,['C7/S2'],'quote',"Aphrahat VII.21; Addai and Mari",'hallock',None,"C7 syr: no meal record.")
rec(w,['C8/S1','C8/S4'],'quote',"Egeria on Edessa (L3339-3403); Aphrahat Dem. VI.4-7 (celibate men and women under one roof); the Book of the Laws of Countries ('in Edessa' they do not kill an unchaste wife or sister 'but they withdraw from them')",'egeria',3339,"C8 syr: loaded against the limits; Aphrahat at npnf213 line 25834-25951; Laws of Countries at anf08 line 68966-68985.")
rec(w,['C9/S2'],'quote',"Aphrahat, Demonstration V, Of Wars",'npnf213',24534,"C9 syr: C9-08 'does honouring endurance teach people to accept a killing king?' has no answer; mapped, unrendered.")
rec(w,['C10/S2'],'quote',"Aphrahat Dem. VII on alms",'hallock',44,"C10 syr.")
rec(w,['C11/S8'],'quote',"Bardaisan on the Brahmans",'anf08',7420,"C11 syr: unrendered.")
rec(w,['C11/S1'],'quote',"the Addai legend ('destroy those Jews who crucified Him'); Sozomen's 'co-operation of the Jews'",'anf08',None,"C11 syr: unrendered; use only with the existing guards (the syr guards hold).")
rec(w,['C12/S2'],'quote',"Bardaisan's Laws of Countries (houses, clothes, speech)",'anf08',67888,"C12 syr: mapped, unrecorded.")
rec(w,['C13/S5'],'quote',"Egeria on the shrine of Thomas at Edessa",'egeria',None,"C13 syr: vendored and mapped (152 hits), no record.")
rec(w,['C16/S7'],'honest_limit',"'you sound too polished': hymn, not analysis, was the fitting register",None,None,"C16 syr: the only partial ground for S7 (dw.jesus, dw.was-jesus-god).",group='no_text')
rec(w,['C16/S5'],'quote',"Rabbula, Marutha, Simeon bar Sabbae",None,None,"C16 syr: zero quotes; Aphrahat 12, Ephrem 11, Tatian 2.")
rec(w,['C8/S1','C8/S4'],'overstated honest_limit',"syr.limit.marriage and syr.demo.marriage-ending say no text speaks to Christian marriage or its ending; the report also says no woman's line survives",RP('syr.limit.marriage'),None,"C8 finding 2: contradicted by the Book of the Laws of Countries (anf08 L68966-68985, mapped to syr), Aphrahat VI and Egeria on Edessa and Marthana.",group='fix')
rec(w,['C8/S3'],'honest_limit check',"syr.limit.f5-enslaved is a guard with no loaded text",RP('syr.limit.f5-enslaved'),None,"C8 syr S3: R* with no loaded passage found.",group='fix')

# ---------------- witt ----------------
w = 'witt'
rec(w,['C2/S3'],'quote',"Augsburg Confession I (Nicaea's decree on the Three Persons)",'ac-file',168,"C2 witt: missing though vendored; lines 168-177.")
rec(w,['C2/S1','C2/S4'],'quote',"Small Catechism first and third articles",'sc',171,"C2 witt: lines 171, 209-219.")
rec(w,['C2/S2'],'quote',"Large Catechism: 'how angry God is ... how good and gracious'",'large-cat',584,"C2 witt.")
rec(w,['C2/S7'],'quote',"Augsburg Confession XIX, Of the Cause of Sin",'ac-file',483,"C2 witt; lines 483-489.")
rec(w,['C6/S2'],'quote',"Treatise on the Power and Primacy of the Pope",'boc',17482,"C6 witt: unquoted though vendored.")
rec(w,['C6/S1','C6/S6'],'quote',"Augsburg Confession XXVIII (line 1271) and XXIII on priests' marriage (line 707); Apology XXIII",'ac-file',1271,"C6 witt: add three quotes; AC XXIII at line 707.")
rec(w,['C7/S6'],'quote',"Large Catechism, third commandment (the calendar)",'large-cat',None,"C7 witt.")
rec(w,['C7/S7'],'quote',"Luther on anointing the sick",'luther-v2',10116,"C7 witt.")
rec(w,['C8/S2'],'quote',"Luther: 'the men, priests, the women, priestesses'",'luther-v1',11754,"C8 witt: women's authority is one sentence.")
rec(w,['C9/S4'],'quote',"Augsburg Confession XVI ('sit as judges ... engage in just wars, serve as soldiers')",'ac-file',414,"C9 witt: vendored and unrendered.")
rec(w,['C10/S3'],'quote',"Apology on 'community of property'",'apology',7025,"C10 witt.")
rec(w,['C10/S5'],'quote',"Luther on usury",'luther-v1',6560,"C10 witt.")
rec(w,['C11/S4'],'story',"Gerlach's Istanbul diary (237 hits) and Luther on the Turks",'gerlach',None,"C11 witt: the only Muslim material; loaded and unused.")
rec(w,['C12/S4','C12/S5'],'quote',"morning and evening blessings (SC 543-607); the calamity list with pestilence; the churchyard as resting place",'sc',543,"C12 witt: unrecorded.",fac=True)
rec(w,['C13/S5'],'quote',"Apology of the Augsburg Confession XXI, Of the Invocation of Saints",'apology',7377,"C13 witt: lines 7377-7491, unrecorded.")
rec(w,['C16/S5','C16/S6'],'quote',"quotes attributed to Luther and Melanchthon by name",None,None,"C16 witt: seven quotes, every one spoken by the Augsburg Confession or the catechism; none attributed to Luther or Melanchthon. 'One line from one of your own writers' has no named writer.")
rec(w,['C11/S1','C11/S4'],'not_for fix',"witt.term.the-turk: the world_word files Jews with the Turk as 'one of the devil's instruments'; the not_for covers only the modern-political reading",RP('witt.term.the-turk'),None,"C11 Jewish visitor: weak edge.",group='fix')

# =====================================================================
# generated and fleet-level rows
# =====================================================================
import json as _json
SEARCH = os.path.join(os.path.dirname(OUT), 'search')


# ---- small additions found on a second read of the reports ----
for w, why in [('hal', "C9 hal: 'Nothing on soldiers or the death penalty.'"), ('ijc', "C9 ijc: 'Gap: soldiers and the death penalty.'"),
               ('don', "C9 S4 don is LOADED only; the report names no passage"), ('syr', "C9 S4 syr is LOADED only; the report names no passage")]:
    rec(w, ['C9/S4'], 'honest_limit', 'soldiers, war, the death penalty, "render unto Caesar": no record', None, None, why, group='no_text')
rec('desert', ['C8/S1'], 'quote', "Egeria's Marthana", 'egeria', 3790, "C8 desert: loaded, unrecorded. (The report lists Egeria as mapped to desert and syr.)")
rec('desert', ['C8/S3', 'C8/S7'], 'honest_limit', "slaves (Antony 'an owner of slaves', paradise-v1 line 617) and children", 'paradise-v1', 617, "C8 desert: 'Nothing on slaves ... or children.'", group='no_text')
for w in ['don', 'hal', 'pahc']:
    rec(w, ['C12/S7'], 'honest_limit', '"Were you happy?" and "what is the point of life": nothing found', None, None, "C12 layer table: S7 is '-' for don, hal and pahc.", group='no_text')
rec('ijc', ['C12/S1'], 'quote', "Chrysostom on the theatre", 'npnf109', None, "C12 ijc: loaded (the report names Chrysostom on the theatre without a line).")

# ---- C11: ten worlds are out of window for Muslims and none says so ----
for w in ['alx', 'cappadocian', 'desert', 'don', 'gallic', 'hal', 'ijc', 'lpc', 'pahc', 'syr']:
    rec(w, ['C11/S4'], 'honest_limit', 'Muslims lie outside this world\'s window (it ends by 451)', None, None,
        "C11 finding 3: 'Ten worlds are out of window for Muslims and none says so.'", group='no_text')
for w in ['desert', 'don']:
    rec(w, ['C11/S1'], 'honest_limit', 'Jews: no record and no mapped work addresses them', None, None,
        "C11 Jewish visitor: nothing to quote bare; 'the risk is the voice improvising'.", group='no_text')

# ---- C8/S6 and C15/S1 (gay marriage / same-sex relations): never faced as asked ----
NEAREST_S6 = {
 'alx': ("Clement, Paedagogus III.3 and III.8: practices 'contrary to nature'; Sodom burned as an example", 'anf02', 24945),
 'cappadocian': ("Basil Ep. 188 canon 7 (npnf208 L35084) and Canon VII, a penance rule (npnf214 L43481)", 'npnf208', 35084),
 'desert': ("none found: no Desert Sayings passage read", None, None),
 'don': ("none found: no Donatist passage read", None, None),
 'gallic': ("Salvian quotes Romans 1:26-27 of Africa (unframed)", 'salvian', 9524),
 'hal': ("Jerome Ep. 55: a husband described as 'an adulterer and sodomite'", 'npnf206', 12992),
 'ijc': ("Augustine, City of God, Rom 1:26 cited", 'npnf102', 27010),
 'lpc': ("Augustine, Confessions III.8: offences 'contrary to nature' to be held in detestation and punished", 'npnf101', 6021),
 'pahc': ("Barnabas 10 (anf01 L12629); Justin 1 Apol. 27 (L14973); the Didache list carries the word 'pederasty'", 'anf01', 12629),
 'rzg': ("none found in the C8 pass; C15 notes the nearest text is not framed", None, None),
 'syr': ("Book of the Laws of Countries: 'The brethren who are in Gaul do not take males for wives' (anf08 L68980)", 'anf08', 68980),
 'witt': ("none found: C8 layer N (nothing)", None, None),
}
_c15 = _json.load(open(os.path.join(SEARCH, 'C15', 'C15-coverage.json')))
for w, (txt, f, ln) in NEAREST_S6.items():
    cell = _c15['worlds'][w]['S1']
    rec(w, ['C15/S1', 'C8/S6'], 'honest_limit (frame not ours; sources and silences only)',
        'nearest: ' + txt, f, ln,
        "C8 S6: no record in any world treats it. C15 S1 (%s; limit built: %s): %s Whether to name condemnatory or penal text as 'nearest' is Mark's decision (C15 finding 3)." % (
            cell['layer_best'], 'yes' if cell['limit_built'] else 'no', cell['note']), group='no_text')

# ---- C15: one honest_limit per world and sub-question where the report says no limit is built ----
S_LABEL = {'S2': 'evolution, science, climate', 'S3': 'AI and talking to a machine', 'S4': 'which church; Catholic church and pope now; megachurches; Reformation and East-West split',
           'S5': 'Christians in politics and voting; religion causes wars', 'S6': 'women pastors today',
           'S7': 'abortion laws; an ageing church; a burnt-out pastor; the Bible on a phone',
           'S8': 'are we what you hoped for; Christians and Jews together; Sunday; the world now; would you still believe'}
def _parse_loaded(s):
    import re as _re
    m = _re.match(r'^(\S+?\.(?:xml|txt)):(\d+)', s)
    if m: return m.group(1), int(m.group(2))
    m = _re.match(r'^(\S+?\.(?:xml|txt))', s)
    if m: return m.group(1), None
    return None, None
for w, wv in _c15['worlds'].items():
    for s, cell in wv.items():
        if s == 'S1' or cell['limit_built']:
            continue
        near = []
        if cell['records']: near.append('records: ' + ', '.join(cell['records'][:3]))
        f = ln = None
        if cell['loaded']:
            f, ln = _parse_loaded(cell['loaded'][0])
            near.append('loaded: ' + cell['loaded'][0][:120])
        if not near: near.append('no nearest material named')
        fn = TX(f) if f else None
        rec(w, ['C15/' + s], 'honest_limit (C15 shape %s: %s)' % (s, S_LABEL[s]), '; '.join(near), fn, ln,
            "C15 %s %s (best %s / worst %s; limit built: no): %s" % (w, s, cell['layer_best'], cell['layer_worst'], cell['note'] or 'no note'),
            fac=(s == 'S3'), group='no_text')

# ---- _fleet rows: engine, site, product and cross-world items ----
w = '_fleet'
rec(w, ['C16/B'], 'facilitator template or routing decision',
    'C16-10, 11, 13, 16, 19, 20, 26 and R-23 fall through to the Representative: only "Are you real" and "How were you made" match _SYSTEM_NATURE_SHAPE (one of nine reaches SYSTEM_NATURE)',
    'engine/m5/routing.py', 56, "C16 Part B: either widen the regex shapes (what are you really, who made you, is this private, who is behind this) or give these questions templates. Governance change: Mark's call. Routing at lines 172-181; template in engine/m4/facilitator_turns.py lines 64-76.", fac=True, group='fix')
rec(w, ['C16/B'], 'facilitator template',
    'C16-20 ("Who wrote your answers?") and C16-26 ("Is my conversation private?"): the voice holds no facts and is forbidden to explain, so its answer will be improvised; the privacy and "who is behind this" answers exist on the site and are unreachable from the conversation',
    'engine/shape/records/fleet_voice/_fleet.voice.fleet.md', 33, "C16 Part B. rzg.demo.why-we takes C16-10 verbatim and answers with the two cities' history; it never says AI.", fac=True, group='fix')
rec(w, ['C16/B'], 'site and code fix',
    'privacy page against code: the page says the scrubbed review copy is deleted after 90 days, but the QC store keeps marks, scores, routing and flags indefinitely; two back-to-back cookie paragraphs ("one job" and "two jobs"); nothing inside the conversation app links to or states any of this',
    'cic-website/privacy.html', None, "C16 privacy facts. Code: engine/m7/qc_store.py; engine/m4/store.py purge_inactive; engine/api/app.py lines 1147-1162; engine/api/db_backup.py. The only 'privacy' string in the app is account-deletion copy at cic-poc/frontend/src/lib/accountsCopy.ts line 132.", fac=True, group='fix')
rec(w, ['C16/S3'], 'product fix',
    '"Show me the page": edition is in the payload but cic-poc/frontend/src/components/SourceList.tsx never prints it, and a source record with a citation sets edition to None; display_locus strips the vendored file name; the quote card sends the rendering, not the verbatim text; no API route serves cic/texts',
    'engine/m4/citation_cards.py', 167, "C16 product check. Lines 178 (edition in payload), 186-188 (verbatim text not sent); engine/prose.py line 233; cic-website/traditions/*.html carry no per-tradition source list. Verdict in the report: a checkable citation for every cited claim, yes; the page, no.", group='fix')
rec(w, ['C16/S5'], 'figure records and quotes',
    'Irenaeus and Tertullian have no figure record and no quote in any world (Irenaeus is named only inside pahc.figure.papias); Luther, Melanchthon, Gregory of Nazianzus, Polycarp, Augustine in the Donatist world and Beza have figure records and zero quotes',
    'anf01', None, "C16 fleet thin spots 2; the texts are vendored (anf01, anf03).", group='loaded')
rec(w, ['C16/S7'], 'decision',
    '"You sound too polished": S7 is empty in every world; the honest answer ("we sang; we argued in letters; this is a rendering") exists only as syr\'s register tensions and the quotes\' modern_lens notes',
    None, None, "C16 fleet thin spots 4.", fac=True, group='no_text')
rec(w, ['C16/S1'], 'demonstration', 'F2-E demonstrations exist in four worlds; none for f2-e-04 (the suppressed-gospels question)',
    None, None, "C16 canon F2-E.", group='no_text')
rec(w, ['C15/S2', 'C15/S3', 'C15/S1'], 'engine fix and modern_term records',
    'the horizon scan misses every modern topic (evolution, internet, AI, podcast, gay marriage, the bare word "Reformation" pass clean); a first-ask later_age question goes to the voice with no Facilitator text; no modern_term record exists for any C15 term (the fleet has one, Trinity)',
    'engine/m1/horizon.py', None, "C15 finding 2. check_horizon at engine/m4/output_check.py lines 397-415; routing at engine/m5/routing.py lines 177-190; etic and bridge texts at engine/m4/facilitator_turns.py lines 139-148, 194, 433; modern_term record at engine/m5/records/modern_term/_fleet.modern.trinity.md. Governance: Mark's call.", fac=True, group='fix')
rec(w, ['C12/S1'], 'decision',
    'nine ambient records (don 3, lpc 3, rzg 3) state a scale or an object, never a day; all carry canon_cells [], tier 3, retrieve_when [], formation_claim_barred true; nothing routes to them',
    'engine/m1/gates.py', 1547, "C12 finding 1. System Hub Decision Log line 6044 parks them untouched; engine/m4/evidence.py gives tier 3 zero priority. rzg.ambient.emptied-worship-space is Inferential-Thin. A decision, not a quiet edit.", group='fix')
rec(w, ['C7/S4', 'C7/S7'], 'card-tag fix',
    'card tags with no question behind them: "Hymns and music" (cappadocian, ijc, syr, witt) and "Feast days and remembering the dead" (cappadocian, don) rest on C7-11 and C7-13, both PREDICTED; no Icons tag and no Confession tag exist (C7-14, C7-10 PREDICTED)',
    None, None, "C7 flags.", group='fix')
rec(w, ['C5/S8'], 'decision',
    'full per-world passage index: feasible in two tiers (script the 32 ThML volumes: 76,551 scripRef tags and 626 scripCom tags; hand-curate the 281 plain-text files for a fixed passage list)',
    'cic/texts/STRUCTURE.md', None, "C5 passage_index_feasibility. Not feasible as one automatic index.", group='no_text')
rec(w, ['C8/S8', 'C14/S8'], 'facilitator-governed note',
    'a husband\'s violence: no record in any world addresses it; the vendored texts that touch it (Augustine Conf. IX.9, Basil Ep. 188 can. 9, Chrysostom Hom. 20 Eph. in npnf113) counsel endurance',
    'npnf101', None, "C8 S8 and C14 FAC: they belong, if anywhere, in a Facilitator-governed note, not in a Representative's mouth. hal.quote.she-put-on-sackcloth (Ep. 77.3) is history, never counsel.", fac=True, group='no_text')
rec(w, ['C11/S1'], 'governance question',
    'the Adversus Judaeos acquisition-and-disclosure obligation: how a Representative handles its own world\'s anti-Jewish polemic',
    None, None, "C11: Build/worlds/aec/Open_Gaps_Tracking.md item 6 (2026-10-02) calls it 'a live governance/methodology question'. Governance: always ask.", group='no_text')
# demonstration gaps by cluster, one row each
DEMO_GAPS = [
 (['C1/S1', 'C1/S3', 'C1/S5'], 'C1: C-I demonstrations exist in 7 of 12 worlds (missing don, gallic, lpc, rzg, witt); C-T in 3 (cappadocian, desert, pahc); C-E in 2 (desert, pahc); C-P in 9 (missing gallic, lpc, witt)'),
 (['C4/S1', 'C4/S2', 'C4/S5'], 'C4: F1-T demonstrations only in gallic, ijc (bread and cup) and witt; F4-T only in don and hal; eight of twelve worlds have neither'),
 (['C6/S3', 'C6/S4'], 'C6: F3-I demonstrations in 3 worlds (gallic, syr, witt); F1-E and F3-T in none of 12'),
 (['C7/S3', 'C7/S2', 'C7/S5'], 'C7: no demonstration for prayer (f4-i-02), the meal (f4-i-03), fasting (f4-i-04) or what happened when you gathered (f3-i-02); alx, cappadocian and desert have none in any of the four cells'),
 (['C8/S3', 'C8/S7'], 'C8: F5-T none; f6-e-01 (the two tortured enslaved women) none; none for children (f5-i-04) or the enslaved (f5-i-05); divorce f6-t-03 in 5 worlds'),
 (['C9/S1', 'C9/S2', 'C9/S5'], 'C9: no demonstration for C9-01 (danger), C9-02 (catacombs) or C9-05 (temples) in any world'),
 (['C10/S1', 'C10/S2', 'C10/S7'], 'C10: no demonstration for money (f5-t-02), tithe (f4-t-02) or work (f5-i-07) in any world'),
 (['C11/S5', 'C11/S2'], 'C11: no demonstration for f6-t-02 ("too narrow") or f3-p-03 (temples and the old gods)'),
 (['C12/S1', 'C12/S3', 'C12/S4'], 'C12: 10 of 13 F5 canon questions have no demonstration; cappadocian, desert, don, lpc, rzg and syr have none'),
 (['C14/S2', 'C14/S5', 'C14/S6', 'C14/S7'], 'C14: none for F4-P-03 (unanswered prayer), F6-P-04 (what to say to one who left), F4-P-02 (forgiving the unrepentant) or F3-P-01 (failing to hold your own accountable)'),
]
for cells, txt in DEMO_GAPS:
    rec('_fleet', cells, 'demonstration', txt, None, None, "The canon cells are not forced per world; the Answer-the-Canon pass and its gate do not produce one answer per cell per world.", group='no_text')
rec('_fleet', ['C17/*'], 'note', 'C17 (challenging the system) was not mapped: 16 questions (3 EXISTS as sealed-probe items, 13 PREDICTED); five are flagged FAC: C17-04, 05, 06, 13, 16',
    None, None, "From repo/06-cluster-17.yaml in the scratchpad. C17-05/06 overlap the C16 Part B fall-through.", fac=True, group='no_text')

# ---- acquisition-dependent rows for acquisitions new in the 16-cluster list ----
_NOREC = {'fleet', 'aec', 'hus', 'jes', 'meth', 'obel', 'rcg', 'wsyr'}
_added = 0
for a in A[A_OLD_COUNT:]:
    byw = {}
    for c in a['cells']:
        wc, sc = c.split(':', 1)
        if wc in _NOREC: continue
        byw.setdefault(wc, []).append(sc)
    for wc, scs in byw.items():
        rec(wc, scs, 'record (depends on acquisition)', '%s, %s' % (a['work'], a['author']), None, None,
            "Needs: %s. %s" % (a['licence'] if a['licence'] != NS else 'licence not stated in report', a['notes'] or 'Registered or named in the report; see acquire.yaml.'),
            group='acquire')
        _added += 1
for substr, cells in MERGE_LOG:
    a = [x for x in A if substr.lower() in x['work'].lower()][0]
    byw = {}
    for c in cells:
        wc, sc = c.split(':', 1)
        if wc in _NOREC: continue
        byw.setdefault(wc, []).append(sc)
    for wc, scs in byw.items():
        rec(wc, scs, 'record (depends on acquisition)', '%s, %s' % (a['work'], a['author']), None, None,
            "Further cells for a work already on the 4-cluster acquire list. Needs: %s." % (a['licence'] if a['licence'] != NS else 'licence not stated in report'), group='acquire')

# =====================================================================
# verify paths, compute, write (16 clusters)
# =====================================================================
import re as _re
for r in R:
    r['path_exists'] = exists(r['file']) if r['file'] else None
for d in DRIFT:
    d['path_exists'] = exists(d['file']) if d['file'] else None
for v in VENDORED_ALREADY:
    v['path_exists'] = exists(v['file']) if v['file'] else None
for a in A:
    a['worlds'] = sorted({c.split(':')[0] for c in a['cells']})
    a['unlocks'] = sorted({c.split(':')[1] for c in a['cells']}, key=lambda x: (int(_re.match(r'C(\d+)', x).group(1)), x))
    a['priority'] = len(set(a['cells']))
A.sort(key=lambda a: (-a['priority'], a['work']))
for i, a in enumerate(A, 1): a['rank'] = i

_names = collections.Counter(a['work'].lower() for a in A)
DUP_ACQ = [k for k, n in _names.items() if n > 1]

def ckey(c):
    w_, _, rest = c.rpartition(':') if ':' in c and not c.startswith('C') else ('', '', c)
    m = _re.match(r'C(\d+)/(.*)', rest)
    sub = m.group(2) if m else rest
    sm = _re.match(r'S(\d+)', sub)
    return (w_, int(m.group(1)) if m else 99, int(sm.group(1)) if sm else (50 if sub == 'B' else 99), sub)
for r in R: r['cells'] = sorted(set(r['cells']), key=ckey)
for a in A: a['cells'] = sorted(set(a['cells']), key=ckey)
GROUP_ORDER = {'loaded': 0, 'no_text': 1, 'acquire': 2, 'fix': 3}
WORLDS = ['alx','cappadocian','desert','don','gallic','hal','ijc','lpc','pahc','rzg','syr','witt']
ALLW = WORLDS + ['_fleet']
def _cnum(cell):
    m = _re.match(r'(?:\w+:)?C(\d+)', cell)
    return int(m.group(1)) if m else 99
R.sort(key=lambda r: (ALLW.index(r['world']), GROUP_ORDER[r['group']], min([_cnum(c) for c in r['cells']] or [99])))
counts = collections.OrderedDict((w, collections.Counter(r['group'] for r in R if r['world'] == w)) for w in ALLW)
CL = ['C%d' % i for i in range(1, 17)] + ['C17']
def r_clusters(r):
    return sorted({'C%d' % _cnum(c) for c in r['cells']}, key=lambda x: int(x[1:]))
def a_clusters(a):
    return sorted({'C%d' % _cnum(c) for c in a['cells']}, key=lambda x: int(x[1:]))
rec_cluster = collections.OrderedDict()
for c in CL:
    rows = [r for r in R if c in r_clusters(r)]
    rec_cluster[c] = dict(rows=len(rows), **{g: sum(1 for r in rows if r['group'] == g) for g in GROUP_ORDER}, facilitator_adjacent=sum(1 for r in rows if r['facilitator_adjacent']))
rec_cluster['(no cluster)'] = dict(rows=sum(1 for r in R if not r['cells']), **{g: sum(1 for r in R if not r['cells'] and r['group'] == g) for g in GROUP_ORDER}, facilitator_adjacent=sum(1 for r in R if not r['cells'] and r['facilitator_adjacent']))
acq_cluster = collections.OrderedDict()
for c in CL:
    rows = [a for a in A if c in a_clusters(a)]
    cells = {x for a in rows for x in a['cells'] if _cnum(x) == int(c[1:])}
    acq_cluster[c] = dict(rows=len(rows), cells_unlocked=len(cells), english_in_copyright_rows=sum(1 for a in rows if a['english_in_copyright']))
acq_world = collections.OrderedDict()
for w in sorted({x for a in A for x in a['worlds']}, key=lambda x: (x == 'fleet', x not in WORLDS, x)):
    rows = [a for a in A if w in a['worlds']]
    acq_world[w] = dict(rows=len(rows), cells_unlocked=len({c for a in rows for c in a['cells'] if c.startswith(w + ':')}))
all_cells = {c for a in A for c in a['cells']}
fac_total = sum(1 for r in R if r['facilitator_adjacent'])

# ---- YAML writer (no dependency) ----
def y(v, ind=0):
    pad = '  '*ind
    if isinstance(v, dict):
        out=[]
        for k,val in v.items():
            if isinstance(val,(dict,list)) and val:
                out.append(f'{pad}{k}:'); out.append(y(val, ind+1))
            else:
                out.append(f'{pad}{k}: {ys(val)}')
        return '\n'.join(out)
    if isinstance(v, list):
        out=[]
        for it in v:
            if isinstance(it,(dict,)):
                body = y(it, ind+1).split('\n')
                out.append(f'{pad}- ' + body[0].strip()); out.extend(body[1:])
            else:
                out.append(f'{pad}- {ys(it)}')
        return '\n'.join(out)
    return pad+ys(v)
def ys(v):
    if v is None: return 'null'
    if isinstance(v,bool): return 'true' if v else 'false'
    if isinstance(v,(int,float)): return str(v)
    if isinstance(v,list): return '[]' if not v else '[' + ', '.join(ys(x) for x in v) + ']'
    if isinstance(v,dict) and not v: return '{}'
    return json.dumps(str(v), ensure_ascii=False)
def md_esc(s): return str(s).replace('|','\\|').replace('\n',' ')

hdr = ("# Generated 2026-10-26 from the sixteen coverage reports C1 to C16 (scratchpad/search/). Read-only extraction; "
       "nothing in the repo was changed. Wording is the reports' own.\n")

# ---------------- acquire ----------------
acq_counts = dict(acquire_rows=len(A), distinct_world_by_subquestion_cells_unlocked=len(all_cells),
                  english_in_copyright_rows=sum(1 for a in A if a['english_in_copyright']),
                  registry_drift_rows=len(DRIFT), listed_as_other_but_already_vendored=len(VENDORED_ALREADY),
                  rows_new_since_4_cluster_list=len(A) - A_OLD_COUNT, rows_moved_out_as_already_vendored=len(STALE_ACQ_MOVED),
                  paths_checked=sum(1 for d in DRIFT + VENDORED_ALREADY if d['file']), paths_missing=sum(1 for d in DRIFT + VENDORED_ALREADY if d['file'] and not d['path_exists']),
                  per_cluster=acq_cluster, per_world=acq_world)
acq_doc = dict(
  _about=("Every source named as IDENTIFIED (registered, not vendored) or OTHER (outside the repo) in the sixteen coverage reports, one row per work, deduplicated across clusters. "
          "priority = number of distinct world x sub-question cells it unlocks (cells listed with cluster ids; 'fleet' = the report names no single world; '*' = the report names the world but not a sub-question). "
          "english_in_copyright marks rows where only the Latin/Greek/German/Syriac/French is public domain, or the whole work is in copyright. "
          "Licences are as stated in the reports (edition dates and hosts), not re-verified online; 'not stated in report' means the report gave none. "
          "The 4-cluster list is kept as acquire-4cluster.*. One 4-cluster row (Tyconius, Liber Regularum) was moved out because C5 found it vendored."),
  counts=acq_counts,
  acquire=[dict(rank=a['rank'], priority=a['priority'], work=a['work'], author=a['author'], edition=a['edition'], hosted=a['hosted'], licence=a['licence'],
                english_in_copyright=a['english_in_copyright'], worlds=a['worlds'], unlocks=a['unlocks'], cells=a['cells'], identified_as=a['identified_as'], notes=a['notes']) for a in A],
  registry_drift_not_downloads=DRIFT,
  listed_as_other_but_already_vendored=VENDORED_ALREADY)
open(os.path.join(OUT,'acquire.yaml'),'w').write(hdr + y(acq_doc) + '\n')

L=[]
L.append('# Acquisition worklist (IDENTIFIED + OTHER sources from the C1 to C16 coverage reports)\n')
L.append('Generated 2026-10-26, read-only. One row per work, deduplicated across the sixteen reports. **Priority** = number of distinct world x sub-question cells the work unlocks (cells listed). **Copyright flag** = the report said the English is in copyright and only the original language (or an older edition) is public domain, or the work is modern scholarship. `fleet` = the report names no single world; `*` = world named, sub-question not. Licences are as stated in the reports, not re-verified. The 4-cluster list is kept as `acquire-4cluster.md`.\n')
L.append('## Counts\n')
L.append(f'- Acquisition rows: **{len(A)}** ({len(A) - A_OLD_COUNT} new since the 4-cluster list of {A_OLD_COUNT + len(STALE_ACQ_MOVED)}; one old row moved out as already vendored).')
L.append(f'- Distinct world x sub-question cells unlocked fleet-wide: **{len(all_cells)}**.')
L.append(f'- Copyright-flagged rows: **{sum(1 for a in A if a["english_in_copyright"])}**.')
L.append(f'- Registry-drift rows: **{len(DRIFT)}**; listed as OTHER but already vendored: **{len(VENDORED_ALREADY)}**.')
L.append(f'- Paths checked (drift and already-vendored files): {acq_counts["paths_checked"]}; missing: {acq_counts["paths_missing"]}.\n')
L.append('| Cluster | Rows touching it | Cells unlocked | Copyright-flagged rows |')
L.append('|---|---|---|---|')
for c, v in acq_cluster.items():
    L.append('| %s | %d | %d | %d |' % (c, v['rows'], v['cells_unlocked'], v['english_in_copyright_rows']))
L.append('\n| World | Rows touching it | Cells unlocked |')
L.append('|---|---|---|')
for wv, v in acq_world.items():
    L.append('| %s | %d | %d |' % (wv, v['rows'], v['cells_unlocked']))
L.append('\nA row that serves several clusters is counted in each, so the cluster rows do not sum to the total.\n')
L.append('## Acquisitions, by priority\n')
L.append('| # | Pri | Work | Author | Edition / translator / year | Hosted | Licence as stated | Copyright flag | Worlds | Unlocks (cells) | Registered as | Notes |')
L.append('|---|---|---|---|---|---|---|---|---|---|---|---|')
for a in A:
    L.append('| %d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        a['rank'], a['priority'], md_esc(a['work']), md_esc(a['author']), md_esc(a['edition']), md_esc(a['hosted']), md_esc(a['licence']),
        'YES' if a['english_in_copyright'] else '', ', '.join(a['worlds']), ', '.join(a['cells']), md_esc('; '.join(a['identified_as'])), md_esc(a['notes'])))
L.append('\n## Already vendored but registered unvendored (or mis-mapped): registry fixes, not downloads\n')
L.append('| Record / item | Finding | Vendored file | Line | Path exists | Reports | Fix |')
L.append('|---|---|---|---|---|---|---|')
for d in DRIFT:
    L.append('| %s | %s | %s | %s | %s | %s | %s |' % (md_esc(d['id']), md_esc(d['finding']), d['file'] or '', d['line'] or '', '' if d['path_exists'] is None else ('yes' if d['path_exists'] else 'NO'), md_esc('; '.join(d['reports'])), md_esc(d['fix'])))
L.append('\n## Listed as OTHER in a report but already in cic/texts (no download; read and render)\n')
L.append('| Work | Vendored file | Line | Path exists | Cells | Note |')
L.append('|---|---|---|---|---|---|')
for v in VENDORED_ALREADY:
    L.append('| %s | %s | %s | %s | %s | %s |' % (md_esc(v['work']), v['file'] or '', v['line'] or '', 'yes' if v['path_exists'] else 'NO', ', '.join(v['cells']), md_esc(v['note'])))
open(os.path.join(OUT,'acquire.md'),'w').write('\n'.join(L)+'\n')

# ---------------- records ----------------
per_world = {w: dict(total=sum(c.values()), **{g: c.get(g,0) for g in GROUP_ORDER}, facilitator_adjacent=sum(1 for r in R if r['world']==w and r['facilitator_adjacent'])) for w,c in counts.items()}
tot = {g: sum(1 for r in R if r['group']==g) for g in GROUP_ORDER}
rec_counts = dict(fleet_total=len(R), by_group=tot, facilitator_adjacent=fac_total,
                  paths_checked=sum(1 for r in R if r['file']), paths_missing=sum(1 for r in R if r['file'] and not r['path_exists']),
                  rows_in_world_sections=sum(1 for r in R if r['world'] != '_fleet'), rows_fleet_level=sum(1 for r in R if r['world'] == '_fleet'),
                  per_world=per_world, per_cluster=rec_cluster)
rec_doc = dict(
  _about=("Every 'must add' or 'fix' item from the sixteen coverage reports, one row per item, for the twelve worlds with records, plus a _fleet section for engine, site, product and cross-world items. "
          "group (order within a world): loaded = the answering text is already vendored (LOADED to RENDERED); no_text = honest_limit / contested_claim / term / decision that needs no new text; "
          "acquire = depends on a source acquired first (see acquire.yaml); fix = registry drift, stale or overstated limits, mis-indexed or duplicate records, not_for guards, status and tag fixes. "
          "facilitator_adjacent marks rows the reports mark as Facilitator ground or adjacent (infants, suicide, interim state, grief and despair follow-up, abuse, a violent husband, system-nature questions, Facilitator-only context). "
          "path_exists is os.path.exists under /home/user/CIC-Project; null when no file applies; a record path under records/<code>/_not-found_/ means the record id was not found in the repo. "
          "Cells: Cn/Sm = cluster and sub-question; '*' = the report does not name a sub-question. The 4-cluster list is kept as records-by-world-4cluster.*; two of its rows (the Macarian and Salvian verbatim notes) were revised in the 16-cluster version because later reports matched those quotes. Wording is the reports' own; no theology added."),
  counts=rec_counts,
  records=R)
open(os.path.join(OUT,'records-by-world.yaml'),'w').write(hdr + y(rec_doc) + '\n')

L=[]
L.append('# Records worklist by world (from the C1 to C16 coverage reports)\n')
L.append('Generated 2026-10-26, read-only. One row per item. **Group**: `loaded` = text already vendored (LOADED to RENDERED); `no_text` = honest_limit / contested_claim / term / decision needing no new text; `acquire` = needs a source first (see acquire.md); `fix` = registry drift, stale or overstated limits, mis-indexed or duplicate records, not_for guards, status and tag fixes. Within each world: loaded, no_text, acquire, fix. **FAC** = the report marks it Facilitator-adjacent (infants, suicide, interim state, grief or despair follow-up, abuse, a violent husband, system-nature questions, Facilitator-only context). **Path** = `os.path.exists` under `/home/user/CIC-Project` (blank when no file applies; MISSING when it does not exist). Line numbers are the reports\' own and were not re-opened here. Wording is the reports\' own.\n')
L.append('## Counts: per world\n')
L.append('| World | Total | loaded | no_text | acquire | fix | FAC |')
L.append('|---|---|---|---|---|---|---|')
for w2, c in counts.items():
    L.append('| %s | %d | %d | %d | %d | %d | %d |' % (w2, sum(c.values()), c.get('loaded',0), c.get('no_text',0), c.get('acquire',0), c.get('fix',0), per_world[w2]['facilitator_adjacent']))
L.append('| **fleet** | **%d** | %d | %d | %d | %d | %d |' % (len(R), tot['loaded'], tot['no_text'], tot['acquire'], tot['fix'], fac_total))
L.append('\n`_fleet` holds %d engine, site, product and cross-world rows; the twelve world sections hold %d.\n' % (rec_counts['rows_fleet_level'], rec_counts['rows_in_world_sections']))
L.append('## Counts: per cluster\n')
L.append('| Cluster | Rows touching it | loaded | no_text | acquire | fix | FAC |')
L.append('|---|---|---|---|---|---|---|')
for c, v in rec_cluster.items():
    L.append('| %s | %d | %d | %d | %d | %d | %d |' % (c, v['rows'], v['loaded'], v['no_text'], v['acquire'], v['fix'], v['facilitator_adjacent']))
L.append('\nA row that serves several clusters is counted in each, so the cluster rows do not sum to the total. C17 was not mapped; its only row is a note.\n')
L.append('Paths checked: %d; missing: %d.\n' % (rec_counts['paths_checked'], rec_counts['paths_missing']))
for w2 in ALLW:
    L.append(f'\n## {w2}\n')
    L.append('| Group | Cells | Record type | Source text | File | Line | Path | Reason | FAC |')
    L.append('|---|---|---|---|---|---|---|---|---|')
    for r in R:
        if r['world']!=w2: continue
        L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            r['group'], ', '.join(r['cells']), md_esc(r['record_type']), md_esc(r['source_text']), r['file'] or '', r['line'] if r['line'] else '',
            '' if r['path_exists'] is None else ('ok' if r['path_exists'] else 'MISSING'), md_esc(r['reason']), 'FAC' if r['facilitator_adjacent'] else ''))
open(os.path.join(OUT,'records-by-world.md'),'w').write('\n'.join(L)+'\n')

print('acquire rows', len(A), 'new', len(A) - A_OLD_COUNT, 'copyright-flagged', acq_counts['english_in_copyright_rows'], 'cells', len(all_cells), 'drift', len(DRIFT), 'vendored-already', len(VENDORED_ALREADY))
print('duplicate acquire names:', DUP_ACQ)
print('records total', len(R), 'fac', fac_total, tot)
for w2, c in counts.items(): print(' ', w2, sum(c.values()), dict(c))
for c, v in rec_cluster.items(): print(' ', c, v)
missing = [(r['world'], r['file']) for r in R if r['file'] and not r['path_exists']] + [('drift', d['file']) for d in DRIFT if d['file'] and not d['path_exists']] + [('vend', v['file']) for v in VENDORED_ALREADY if v['file'] and not v['path_exists']]
print('missing paths:', missing)
