import json, sys
S = sys.argv[1].rstrip("/") + "/"
NR = "the archive.org record carries no rights field, so the imprint date is the basis"
PDM = "the archive.org record carries the Public Domain Mark"
A12 = "; add 12 to OCR line numbers"
items = []


def pd(y, extra):
    return "Public Domain (pd-us-by-date: published %s); %s" % (y, extra)


def row(slug, work, author, locus, atlas, role, conf, lang, date, note, voice_of=None):
    r = dict(slug=slug, work=work, author=author, locus=locus + A12, atlas_ids=atlas, role=role, confidence=conf, language=lang, date=date, note=note)
    if voice_of:
        r["voice_of"] = voice_of
    return r


def doc(y, src):
    return dict(start=y[0], end=y[1], source=src, fc="Documented")


def unk(checked):
    return dict(checked=checked)


def add(ident, djvu, filename, title, creator, publisher, pubdate, year, extra, lang, ocr, content, seed_author, world, want, rows, rights=None, rights_short=None, seed_title=None, contents_note=None):
    items.append(dict(src=S + "dl/" + ident + "__" + djvu, filename=filename, title=title, creator=creator, publisher=publisher, pubdate=pubdate,
                      rights=rights or pd(year, extra), rights_short=rights_short or ("published %s, out of US copyright by date" % year), lang=lang, item=ident,
                      ocr=ocr, content=content, seed_title=seed_title or title, seed_author=seed_author, year=str(year), world=world,
                      why=want, contents_note=contents_note or content, want=want, rows=rows))


KONGO = "kongo-christianity-after-1650"
COPT = "the-coptic-church-under-the-ottomans"
ETH = "ethiopian-christianity-gondar-to-the-zemene-mesafint"
LATAM = "colonial-latin-american-devotional-catholicism"
SJ = "society-of-jesus-1650-1814"
VIET = "vietnamese-catholicism-to-1815"
CHINA = "chinese-catholicism-1650-1906"
CEYLON = "catholics-of-dutch-ceylon"
VOC = "protestant-churches-of-the-voc-world"
CAPE = "the-dutch-reformed-church-at-the-cape"
COFE = "restoration-georgian-church-of-england"

# ---------------- Africa ----------------
add("histoiredeloango00proy_0", "histoiredeloango00proy_0_djvu.txt", "proyart_histoire-de-loango-kakongo-et-autres-royaumes-d-afrique-fra_1776.txt",
    "Histoire de Loango, Kakongo, et autres royaumes d'Afrique; rédigée d'après les mémoires des préfets apostoliques de la mission françoise; enrichie d'une carte utile aux navigateurs",
    "Liévin-Bonaventure Proyart (title page: 'Par M. l'Abbé Proyart')",
    "Paris: C. P. Berton and N. Crapart; Lyon: Bruyset-Ponthus (title page)", "1776 (title page: 'M. DCC. LXXVI.')", 1776, NR, "fra",
    "readable French with the long s read as f; several chapter headings are garbled. A John Carter Brown Library plate stands at OCR lines 1-4.",
    "Two parts. Part 1, the country and its people: Chapitre premier at OCR line 134 to about 7224. Part 2, the history of the French mission: half-title at 7225-7237, 'Chapitre premier. Origine de la Mission' at 7242, eighteen chapters, ending 'FIN' at 13287. Editorial matter: the dedicatory letter at about 50-118; remarks on the map for pilots at 12915-13286; table at 13292-13430; approbation (the OCR reads 26 May 1770) at 13573; privilege at 13587-13670. Letters of the prefects are quoted inside Part 2 and were not mapped.",
    "Liévin-Bonaventure Proyart", KONGO,
    "Open-Gaps 175 (AF-3), Library wanted: Proyart for Kongo after 1650, in the mission's own French (the English of Pinkerton XVI is held).",
    [row("proyart-histoire-de-loango-part-2-the-french-mission", "Proyart, Histoire de Loango, Kakongo: part 2, the French mission (1776)", "proyart",
         "part 2 at OCR lines 7242-13287", [KONGO], "context", "provisional", "fra",
         doc((1776, 1776), "title page: 'M. DCC. LXXVI.'"),
         "A French priest's history of the French mission to Loango and Kakongo, drawn up from the prefects' memoirs. A mission's view, not a Kongolese voice."),
     row("proyart-histoire-de-loango-part-1-the-country", "Proyart, Histoire de Loango, Kakongo: part 1, the country and people (1776)", "proyart",
         "part 1 at OCR lines 134-7224", [KONGO], "context", "needs-ruling", "fra",
         doc((1776, 1776), "title page: 'M. DCC. LXXVI.'"),
         "The description of the kingdoms and their people, as the missionaries reported them.")])

add("twohundredyearso01pasc", "twohundredyearso01pasc_djvu.txt", "pascoe_two-hundred-years-of-the-spg-v1_1901.txt",
    "Two Hundred Years of the S.P.G.: an historical account of the Society for the Propagation of the Gospel in Foreign Parts, 1701-1900 (based on a digest of the Society's records); vol. I",
    "C. F. Pascoe, assistant secretary of the Society (title page)", "London: published at the Society's Office, 19 Delahay Street, Westminster (title page)", "1901 (title page)", 1901, NR, "eng",
    "clean English; chapter numerals are sometimes garbled and footnote markers and page heads recur. A library stamp and frontispiece plates stand at OCR lines 1-60.",
    "The first of the two volumes as bound; it stops inside the chapters on India (the last is chapter LXXV, Bengal, from OCR line 49402; the last line refers forward to p. 730). Chapter I, the Society's origin, at 4911. The older North American colonies: chapters II-XII at 5444-10688. British North America: 10689 to about 19395. West Indies from 19396. Africa: introduction at 25549, chapter XXXV West Africa at 25566-26626, with Thomas Thompson and Philip Quaque at about 25620-25860; Cape of Good Hope from 26627. Editorial matter: preface and guide at about 246-2183, contents from 2184. Missionaries' letters and reports are quoted throughout. Several chapter headings were not found.",
    "C. F. Pascoe", COFE,
    "CFT-Wants batch 2 (AF-8) and Open-Gaps 175, Library wanted: a pre-1931 source for Philip Quaque and the S.P.G. in West Africa.",
    [row("pascoe-spg-west-africa-thompson-and-quaque", "Pascoe, Two Hundred Years of the S.P.G., vol. I: West Africa (Thompson and Philip Quaque)", "pascoe",
         "chapter XXXV at OCR lines 25566-26626; Quaque at about 25620-25860", [COFE], "context", "provisional", "eng",
         doc((1901, 1901), "title page: 1901"),
         "The Society's own digest of its records on the West African mission from 1751. Written in 1901; Quaque's words appear only as the digest quotes them."),
     row("pascoe-spg-north-american-colonies", "Pascoe, Two Hundred Years of the S.P.G., vol. I: the older North American colonies", "pascoe",
         "chapters II-XII at OCR lines 5444-10688", [COFE], "context", "provisional", "eng",
         doc((1901, 1901), "title page: 1901"),
         "The Society's digest of its colonial missions, colony by colony. A later summary by the Society's assistant secretary.")])

add("dutchreformedchu00mcca", "dutchreformedchu00mcca_djvu.txt", "mccarter_dutch-reformed-church-in-south-africa_1869.txt",
    "The Dutch Reformed Church in South Africa, with notices of the other denominations: an historical sketch",
    "Rev. John M'Carter, Ladysmith, Natal (title page)", "Edinburgh: W. & C. Inglis; London: J. Nisbet and Co.; Capetown: N. H. Marais (title page)", "1869 (title page)", 1869,
    "the archive.org record says the Library of Congress is unaware of any copyright restrictions", "eng",
    "very clean English.",
    "Seven chapters: I, the period of the Dutch rule, at OCR line 213; II, the Cape becomes an English colony, at 990; III, growth of the church 1806-1868, at 1248; IV at 1686; V at 2634; VI at 3553; VII at 4366; 'The End' at 4995. Editorial matter: preface at 34-100, contents at 106-212. The appendix at 4998-5204 prints the Church Ordinance, which is not the author's voice.",
    "John McCarter", CAPE,
    "Open-Gaps 175 (AF-4), Library wanted: McCarter (1869), the census entry's own source for the Dutch Reformed Church at the Cape.",
    [row("mccarter-dutch-reformed-church-in-south-africa", "McCarter, The Dutch Reformed Church in South Africa (1869)", "mccarter",
         "the whole book at OCR lines 213-4995; chapters I-II (213-1247) cover the years to 1806", [CAPE], "tradition", "provisional", "eng",
         doc((1869, 1869), "title page: 1869"),
         "A minister in Natal writes the church's history in English; his preface speaks of 'several years' pastoral labour among the South African Dutch colonists' (OCR lines 75-77). Chapters I and II cover the Dutch period; the rest is the nineteenth century.")])

for v, ident, bk, lines, extra_note in [
    (2, "travelstodiscov02bruc", "Books III and IV, the annals of Abyssinia",
     "Book III, the annals from Icon Amlac, from about OCR line 596 to about 18101 (the words 'Book III' are not legible); Book IV at 18102-31720, from Facilidas (18121) to Joas (29158). The reign of David, 1714-1719, at 25626, with the clergy's convocation and the stoning of the Capuchin missionaries at about 25654-25953. 'End of the second volume' at 31721. Contents at 367-520. Scan noise at 1-82.",
     "the long s is read as f, punctuation is scattered and many headings are garbled; the text can be followed but needs care."),
    (3, "travelstodiscov03bruc", "Books V and VI, the journey to Gondar and the stay there",
     "Book V, from Masuah to Gondar, from OCR line 415: reception at Gondar at 8903, transactions at Gondar at 10406, chapter XII on the state of religion at 13781-15739 (the Abuna at about 13928-13965). Book VI at 15773 to the weather tables; 'End of the third volume' at 33321. Contents at 70-200. Several chapter headings were not found.",
     "the long s is read as f and many chapter headings are garbled; the running text is readable.")]:
    add(ident, ident + "_djvu.txt", "bruce_travels-to-discover-the-source-of-the-nile-v%d_1790.txt" % v,
        "Travels to Discover the Source of the Nile, in the Years 1768, 1769, 1770, 1771, 1772, and 1773; in five volumes; vol. %s" % ("II" if v == 2 else "III"),
        "James Bruce of Kinnaird (title page)", "Edinburgh: printed by J. Ruthven, for G. G. J. and J. Robinson, Paternoster-Row, London (title page)",
        "1790 (title page: 'M.DCC.XC.'%s)" % (", read on the page image, leaf n12; the OCR garbles the first letter" if v == 2 else ""), 1790,
        "the archive.org record says 'Not in copyright'", "eng", extra_note, bk[0].upper() + bk[1:] + ". " + lines,
        "James Bruce", ETH,
        "Wanted_Sources row 151 and Open-Gaps 175, Library wanted: Bruce's Travels, vols 2 and 3 (1790), the census entry's source for Gondar.",
        [row("bruce-travels-vol-%d" % v, "Bruce, Travels to Discover the Source of the Nile, vol. %d (1790): %s" % (v, bk), "bruce",
             ("Book III from about OCR line 596, Book IV at 18102-31720; David's reign and the stoning of the missionaries at about 25626-25953" if v == 2 else "Book V at OCR lines 415-15772, the chapter on religion at 13781-15739; Book VI from 15773"),
             [ETH], "context", "provisional", "eng", doc((1790, 1790), "title page: 'M.DCC.XC.'; the travels are dated 1768-1773 on the title page"),
             ("A Scottish traveler's annals of the kings of Abyssinia down to his own visit, with his own judgments. An outsider's version." if v == 2 else
              "A Scottish traveler's account of his journey to Gondar, his stay there and the church as he saw it. An outside witness."))])

add("storyofchurchofe02butc", "storyofchurchofe02butc_djvu.txt", "butcher_story-of-the-church-of-egypt-v2_1897.txt",
    "The Story of the Church of Egypt: being an outline of the history of the Egyptians under their successive masters from the Roman conquest until now; in two volumes, vol. II",
    "E. L. Butcher (title page)", "London: Smith, Elder, & Co. (title page)", "1897 (title page)", 1897, NR, "eng",
    "clean English; marginal year notes run into the text. A library catalog card stands at OCR lines 1-12.",
    "Chapters XIII to XLIII, from the Fatimid conquest (969) to 1897. The Ottoman years: chapter XXXII at OCR line 9081 (1517 at 9476) through chapter XL, ending at 15241; chapter XLI, from 1854, at 15242. The first Roman Catholic metropolitan (1741) at 12592-12622. Ibrahim al-Jawhari ('Moallem Ibrahim-el Johari') in a footnote at 13292-13299. Main text ends at about 17335; a note on new bishops at 17337-17395; index at 17397-20049.",
    "E. L. Butcher", COPT,
    "Wanted_Sources row 152 and Open-Gaps 175, Library wanted: Butcher, The Story of the Church of Egypt, vol. 2 (1897), the census entry's source.",
    [row("butcher-story-of-the-church-of-egypt-vol-2-ottoman-years", "Butcher, The Story of the Church of Egypt, vol. II: the Ottoman years, 1517-1854", "butcher",
         "chapters XXXII-XL at OCR lines 9081-15241", [COPT], "context", "provisional", "eng", doc((1897, 1897), "title page: 1897"),
         "An English writer's history of the Copts down to 1897. A secondary account by an outsider.")])

add("bub_gb_m3GZP6sZZJMC", "bub_gb_m3GZP6sZZJMC_djvu.txt", "vansleb_histoire-de-l-eglise-d-alexandrie-fra_1677.txt",
    "Histoire de l'Église d'Alexandrie, fondée par S. Marc, que nous appelons celle des Jacobites-Coptes d'Égypte; écrite au Caire même, en 1672 et 1673",
    "Johann Michael Wansleben (title page: 'Par le P. J. M. Vansleb, Dominicain')", "Paris: chez la veuve Clousier, and chez Pierre Promé (title page)",
    "1677 (title page: 'M. DC. LXXVII.', confirmed on the page image, leaf n4; the OCR reads 'M. pC. LXXVII.')", 1677, PDM, "fra",
    "readable French with the long s read as f; roman numerals in chapter headings are often garbled and marginal headings run into the text. Google's stamp lines stand at OCR lines 1-7 and at the end.",
    "Seven parts: I, the hierarchy, at OCR line 1202; II, customs, at 3168; III, belief, at 6234; IV, ceremonies, at 7381; V, canons and councils, at 11361; VI, a catalog of the Coptic patriarchs from St Mark to 1673, drawn, its heading says, from Arabic authors (the first name is garbled there; 'Abulbaracat' is named often elsewhere in the book), at 14095; VII, a catalog of famous men, at 15436, ending at about 16316. Editorial matter: dedication from 98; Vansleb's foreword at 585-860; royal privilege (28 August 1677) at 1083-1175; table of chapters at 16357-16750; index from 16751. Chapters inside the parts were not fully mapped.",
    "Johann Michael Wansleben (Vansleb)", COPT,
    "Open-Gaps 175, Library wanted: Vansleb, Histoire de l'Église d'Alexandrie (1677), for the Coptic patriarchate under the Ottomans.",
    [row("vansleb-histoire-de-l-eglise-d-alexandrie", "Vansleb, Histoire de l'Église d'Alexandrie (1677)", "vansleb",
         "parts I-VII at OCR lines 1202-16316; the catalog of patriarchs at 14095-15435", [COPT], "context", "provisional", "fra",
         doc((1672, 1677), "title page: 'Écrite au Caire même, en 1672 et 1673' and 'M. DC. LXXVII.'"),
         "A Dominican who lived in Cairo in 1672-1673 describes the Coptic church from its own Arabic books and from what he saw. A Catholic outsider's digest; the Arabic sources are his to report.")])

add("bub_gb_8n2JTTnOoMIC", "bub_gb_8n2JTTnOoMIC_djvu.txt", "vansleb_nouvelle-relation-d-un-voyage-fait-en-egypte-fra_1677.txt",
    "Nouvelle relation en forme de journal, d'un voyage fait en Égypte, par le P. Vansleb, R. D., en 1672 et 1673",
    "Johann Michael Wansleben (title page: 'Par le P. Vansleb, R. D.')", "Paris: chez Estienne Michallet, rue S. Jacques (title page)",
    "1677 (title page: 'M. DC. LXXVII.', confirmed on the page image, leaf n6)", 1677, PDM, "fra",
    "readable French with the long s read as f; side notes are mixed into the lines. Google's stamp lines stand at OCR lines 1-19 and after the text.",
    "One dated journal with no parts or chapters. Dedication to Cardinal d'Estrées at OCR lines 55-120; Vansleb's notice at 242-330; errata at about 320-360. The journal from 379 ('Estant à Marseille le 8 de May 1671') to 'FIN' at 17991. The account of the Copts in the opening description of Egypt at about 518-940; Coptic churches of Cairo at about 5536; the monasteries of St Macarius from 9437; Old Cairo at about 10400; St Antony's monastery at about 12997. Index at 18041-18830; privilege extract at 18837-18853.",
    "Johann Michael Wansleben (Vansleb)", COPT,
    "Open-Gaps 175, Library wanted: Vansleb on the Copts under the Ottomans (his journal, beside the Histoire).",
    [row("vansleb-nouvelle-relation-voyage-en-egypte", "Vansleb, Nouvelle relation d'un voyage fait en Égypte (1677)", "vansleb",
         "the journal at OCR lines 379-17991", [COPT], "context", "provisional", "fra",
         doc((1671, 1677), "the journal opens 'le 8 de May 1671' (OCR line 389-390); title page 'M. DC. LXXVII.'"),
         "The Dominican's travel journal, which opens in May 1671, with visits to Coptic churches and desert monasteries. An outside witness.")])

add("presentstateofeg00wans", "presentstateofeg00wans_djvu.txt", "vansleb_present-state-of-egypt_1678.txt",
    "The Present State of Egypt; or, A New Relation of a Late Voyage into that Kingdom, performed in the years 1672 and 1673, by F. Vansleb, R. D.; Englished by M. D., B. D.",
    "Johann Michael Wansleben; translated by 'M. D., B. D.' (title page; the archive.org record names Marius D'Assigny, the print does not)",
    "London: printed by R. E. for John Starkey, at the Miter in Fleet-street, near Temple-Bar (title page)", "1678 (title page)", 1678, NR, "eng",
    "readable English with the long s read as f; some ligatures and marginal glosses are garbled.",
    "The English of Vansleb's Nouvelle relation. Licence at OCR line 1; title page at 6-42; 'To the Reader', signed M. D., at 50-135. The journal at 139-11188. Topical sections inside it: Upper Egypt at 670; the Nile at 1263; 'Of the Christians' (Greeks and Copts) at 3084; Coptic churches of Cairo at about 3427-3660; the journey to the monasteries at 5843-6140. Table at 11197-11772; the bookseller's catalog at 11774-11994.",
    "Johann Michael Wansleben (Vansleb); M. D. (tr.)", COPT,
    "Open-Gaps 175, Library wanted: Vansleb on the Copts, in an English printed by 1930 beside the French.",
    [row("vansleb-present-state-of-egypt-english-1678", "Vansleb, The Present State of Egypt, English (1678)", "vansleb",
         "the journal at OCR lines 139-11188", [COPT], "context", "provisional", "eng",
         doc((1671, 1678), "the journal opens 'In the Year 1671' (OCR line 151); title page 1678"),
         "The English translation of the travel journal, printed a year after the French. An outside witness; the translator signs only with initials.")])

add("merveillesbiogra05jaba", "merveillesbiogra05jaba_djvu.txt", "jabarti_merveilles-biographiques-et-historiques-t5-fra_1890.txt",
    "Merveilles biographiques et historiques, ou Chroniques du cheikh Abd-el-Rahman el Djabarti, traduites de l'arabe par Chefik Mansour Bey, Abdulaziz Kahil Bey, Gabriel Nicolas Kahil Bey et Iskender Ammoun Effendi; tome V",
    "Abd al-Rahman al-Jabarti; translated by Chefik Mansour Bey, Abdulaziz Kahil Bey, Gabriel Nicolas Kahil Bey and Iskender Ammoun Effendi (title page)",
    "Le Caire: Imprimerie nationale (title page)", "1890 (title page; the archive.org record's date field reads 1888)", 1890, NR, "fra",
    "mostly clean French; Arabic names are in Latin letters. Internet Archive credit lines stand at OCR lines 1-20.",
    "The chronicle of Egypt for the Hijri years 1202 to 1212 (1787-1798), each year with its events and its obituaries. Year headings: 1202 at OCR line 96; 1203 at 2059; 1204 at 2851; 1205 at 3314; 1206 at 6490; 1207 at 7584; 1208 at 8412; 1209 at 8994; 1210 at 9431; 1211 and 1212 at 9790. The obituary of the Copt Ibrahim al-Jawhari ('Moallem Ibrahim el Djohari'), under 1209, at 9397-9428. 'Fin du tome cinquième' at 10498; the translators' calendar table at 10501-10694. Other 'El Djohari' passages concern a Muslim sheikh.",
    "Abd al-Rahman al-Jabarti; Chefik Mansour Bey and others (tr.)", COPT,
    "Wanted_Sources row 152, Library wanted: al-Jabarti's obituary of Ibrahim al-Jawhari; also Open-Gaps 225 (no Muslim chronicler of 1650-1906 held).",
    [row("jabarti-chronicle-1202-1212-french-with-obituary-of-ibrahim-al-jawhari", "al-Jabarti, Aja'ib al-athar, the years 1202-1212 AH, French (Cairo 1890), with the obituary of Ibrahim al-Jawhari", "jabarti",
         "the volume at OCR lines 92-10498; the obituary at 9397-9428", [COPT], "context", "provisional", "fra",
         unk("the title page (OCR lines 22-61) and the year headings give the years narrated (1202-1212 AH), not a year of writing; the volume has no preface"),
         "A Muslim scholar of Cairo gives the obituary of the leading Coptic official of his day. An outside witness from the Muslim majority, in French translation.")])

add("journalathreeye00leegoog", "journalathreeye00leegoog_djvu.txt", "gobat_journal-of-a-three-years-residence-in-abyssinia_1834.txt",
    "Journal of a Three Years' Residence in Abyssinia, in furtherance of the objects of the Church Missionary Society; to which is prefixed, A Brief History of the Church of Abyssinia, by the Rev. Professor Lee, D.D.",
    "Samuel Gobat; with a history by Samuel Lee (title page)", "London: Hatchard & Son; and Seeley & Sons (title page)",
    "1834 (title page, read on the page image, leaf n9; the OCR does not give the year)", 1834, "the archive.org record is tagged NOT_IN_COPYRIGHT", "eng",
    "poor: words are often broken ('tliat', 'edifj-ing') and the contents and index pages are largely garbled; the journal can be followed. Google's sheet stands at OCR lines 1-47.",
    "Three voices. The Church Missionary Society's unheaded preface, with extracts of Gobat's letters, at OCR lines 222-660. Professor Lee's Brief History of the Church of Abyssinia at 663-2822. Gobat's journal at 2823-13762 (it opens 25 February 1830). Gobat's general remarks at 13763-15178 (religion at 14002). Index from about 15180. Chapter headings in the journal were not found.",
    "Samuel Gobat; Samuel Lee", ETH,
    "Census VII.38 and VII.34 name Gobat's Journal (London, 1834) as a source; Open-Gaps 175 (AF-1), Library wanted for Ethiopia in the Zemene Mesafint.",
    [row("gobat-journal-of-a-three-years-residence-in-abyssinia", "Gobat, Journal of a Three Years' Residence in Abyssinia (1834)", "gobat",
         "the journal at OCR lines 2823-13762, the general remarks at 13763-15178", [ETH], "context", "provisional", "eng",
         doc((1830, 1834), "the journal opens 'Feb. 25, 1830' (about OCR line 2830); title page 1834"),
         "A missionary of the Church Missionary Society keeps a journal of his stay in Abyssinia from 1830. An outside witness."),
     row("lee-brief-history-of-the-church-of-abyssinia", "Samuel Lee, A Brief History of the Church of Abyssinia (in Gobat 1834)", "lee-samuel",
         "OCR lines 663-2822", [ETH], "context", "needs-ruling", "eng",
         doc((1834, 1834), "title page: 1834, read on the page image, leaf n9"),
         "Professor Lee's short history, which quotes older authorities. Secondary, and not Gobat's voice.")])

# ---------------- Ethiopia own voice ----------------
add("annalesregumiysu01guid", "annalesregumiysu01guid_djvu.txt", "annales-regum-iyasu-ii-et-iyoas_versio-fra_guidi1912.txt",
    "Annales regum Iyāsu II et Iyo'as; interpretatus est Ignatius Guidi (Corpus Scriptorum Christianorum Orientalium, Scriptores Aethiopici, Versio, series altera, tomus VI)",
    "Anonymous royal chronicles (the title page names no author); translated into French by Ignazio Guidi (title page: 'interpretatus est Ignatius Guidi')", "Romae: excudebat Karolus de Luigi; Parisiis: Carolus Poussielgue; Lipsiae: Otto Harrassowitz (title page)",
    "1912 (title page: 'MDCCCCXII', read on the page image, leaf n8; the archive.org record's date field reads 1910)", 1912, NR, "fra",
    "mostly clean French with regular errors (q read as d: 'dui' for 'qui'); Ethiopic words in the notes are garbled. Cover-scan noise stands at OCR lines 1-160.",
    "The translation is in French; only the editor's note on the manuscripts (OCR lines 322-364) is in Latin. The history of Iyasu II (Adyam Sagad) and the queen Berhan Mogasa from the heading at 393, chapter I at 897, to the king's burial at about 10555. The history of Iyo'as from 10557 to about 15790. Guidi's 'Observation' at 15792 and additions to tome V at 15802-15825. Footnotes run throughout; there is no index.",
    "Ignazio Guidi (tr.)", ETH,
    "Open-Gaps 175 (AF-1), Library wanted: Guidi's Annales for Ethiopia after Gondar's high years; the tradition's own chronicle in a readable translation.",
    [row("annals-of-iyasu-ii-french-guidi-1912", "Annals of Iyasu II, French (Guidi 1912)", "ethiopian-royal-chronicles",
         "OCR lines 393-10555", [ETH], "tradition", "provisional", "fra",
         unk("the title page (OCR lines 221-293) and the opening of the Latin note (322-364) were read; the note was not read through for the chronicler or a year of writing"),
         "The chronicle of King Iyasu II (Adyam Sagad) and Queen Berhan Mogasa. The kingdom's own telling, in a scholar's French."),
     row("annals-of-iyoas-french-guidi-1912", "Annals of Iyo'as, French (Guidi 1912)", "ethiopian-royal-chronicles",
         "OCR lines 10557-15790", [ETH], "tradition", "provisional", "fra",
         unk("the heading at OCR line 10557 gives no year; the Latin note (322-364) was not read through for a year of writing"),
         "The chronicle of King Iyo'as, in French.")])

add("annalesregumiysu02guid", "annalesregumiysu02guid_djvu.txt", "annales-regum-iyasu-ii-et-iyoas_textus-gez_guidi1910.txt",
    "Annales regum Iyāsu II et Iyo'as; edidit Ignatius Guidi (Corpus Scriptorum Christianorum Orientalium, Scriptores Aethiopici, Textus, series altera, tomus VI)",
    "Anonymous royal chronicles (the title page names no author); edited by Ignazio Guidi (title page)", "Parisiis: e Typographeo Reipublicae; Carolus Poussielgue; Lipsiae: Otto Harrassowitz (title page)",
    "1910 (title page: 'MDCCCCX', read on the page image, leaf n6; the OCR garbles the numeral)", 1910, NR, "gez",
    "the Ge'ez came through in Ethiopic letters and reads as running text with scattered errors (wrong letter forms, merged words, stray Latin letters); it has not been checked against the print letter by letter. The text turns to noise from about OCR line 16990. Cover-scan noise stands at 1-120.",
    "The Ge'ez text. Latin preface at about OCR lines 177-250. The history of Iyasu II from the heading at 272-274, first line at 277. The history of Iyo'as from the heading at 11283, chapter I at 11284, readable to about 16975. A Latin apparatus of variant readings stands at the foot of most pages. There is no index.",
    "Ignazio Guidi (ed.)", ETH,
    "Open-Gaps 175 (AF-1), Library wanted: Guidi's Annales; the chronicle in its own language.",
    [row("annals-of-iyasu-ii-and-iyoas-geez-guidi-1910", "Annals of Iyasu II and of Iyo'as, Ge'ez text (Guidi 1910)", "ethiopian-royal-chronicles",
         "Iyasu II at OCR lines 272-11282; Iyo'as at 11283 to about 16975", [ETH], "tradition", "provisional", "gez",
         unk("the title page (OCR lines 121-165) and the headings at 272 and 11283 give no year of writing; the Latin preface (177-250) was not read through"),
         "The two chronicles in Ge'ez. A second witness beside the French until the OCR is checked against the print.")])

# ---------------- Latin America ----------------
VW = "Wanted_Sources row 123 (major), Library wanted: Vieira's Maria Rosa Mystica (1686), a Life (Barros 1746) and the Cartas."
add("mariarosamystica00viei", "mariarosamystica00viei_djvu.txt", "vieira_maria-rosa-mystica-parte1-por_1686.txt",
    "Maria Rosa Mystica: excellencias, poderes, e maravilhas do seu Rosario, compendiadas em trinta sermoens asceticos, e panegyricos sobre os dous Evangelhos desta solennidade, novo, e antigo; I. parte",
    "António Vieira (title page)", "Lisboa: na Officina de Miguel Deslandes, na Rua da Figueyra; a custa de Antonio Leyte Pereyra (title page)", "1686 (title page: 'M. DC. LXXXVI.')", 1686, NR, "por",
    "readable Portuguese with the long s read as f; two columns are run together in places and some heading numerals are garbled.",
    "Sermons I to XV on the Rosary. Licences and censures at OCR lines 45-232; errata from 235. Sermon I at 311; II at 3384; III at 7896; IV at 11464; V at 13636; VI at 16603; VII at 20260; VIII at 22938; IX at 25156; X at 27909; XI at 30197; XII at 34001; XIII at 37627; XIV at 40117, headed as preached in Bahia to the brotherhood of the Blacks of a sugar mill in 1633; XV not found by its heading (its epigraph at 43442). Text ends at 45951. Scripture index from 45959 and a subject index to the end.",
    "António Vieira", LATAM, VW,
    [row("vieira-maria-rosa-mystica-part-1-sermons-i-xv", "Vieira, Maria Rosa Mystica, part 1: sermons I-XV (1686)", "vieira",
         "sermons at OCR lines 311-45951; sermon XIV at 40117", [LATAM, SJ], "tradition", "provisional", "por",
         doc((1633, 1686), "sermon XIV's heading: 'Anno de 1633' (OCR lines 40119-40121); title page 'M. DC. LXXXVI.'; licences of 1685-1686 at 83-232"),
         "The preacher's Rosary sermons in his own Portuguese. Sermon XIV is headed as preached to the brotherhood of the Blacks of a sugar mill in Bahia.")])
add("mariarosamystica01viei", "mariarosamystica01viei_djvu.txt", "vieira_maria-rosa-mystica-parte2-por_1688.txt",
    "Maria Rosa Mystica: excellencias, poderes, e maravilhas do seu Rosario, compendiadas em trinta sermoens asceticos, e panegyricos, sobre os dous Evangelhos desta solennidade, novo, e antigo; II. parte",
    "António Vieira (title page)", "Lisboa: na Impressão Craesbeeckiana; a custa de Antonio Leyte Pereyra (title page)", "1688 (title page: 'Anno M. DC. LXXXVIII')", 1688, NR, "por",
    "readable Portuguese with the long s read as f; columns are merged in places and heading numerals are garbled. Blank-scan debris and a library plate stand at OCR lines 1-60.",
    "Sermons XVI to XXX. Licences and censures at about OCR lines 113-330; errata from 382. Sermon XVI at 458; XVII at 3608; XVIII at 6182; XIX at 9269; XX at 12831; XXI at 15803; XXII at 18452; XXIII at 21201; XXIV at 23800; XXV at 27496; XXVI at 30365; XXVII at 33001; XXVIII at 36371; XXIX at 38725; XXX at 41173. Sermons XX and XXVII speak of the Blacks and their brotherhood of the Rosary in the body of the text (XX at about 12870-14235; XXVII at about 33105-33613), not in their headings. Scripture index at 43755-46962; index of notable things from 46963.",
    "António Vieira", LATAM, VW,
    [row("vieira-maria-rosa-mystica-part-2-sermons-xvi-xxx", "Vieira, Maria Rosa Mystica, part 2: sermons XVI-XXX (1688)", "vieira",
         "sermons at OCR lines 458 to about 43754; sermon XX at 12831, XXVII at 33001", [LATAM, SJ], "tradition", "provisional", "por",
         doc((1688, 1688), "title page: 'Anno M. DC. LXXXVIII'; licences of 1686-1687 at about OCR lines 113-330"),
         "The second half of the Rosary sermons. Sermons XX and XXVII speak of the Blacks, the enslaved and their brotherhood.")])
add("vidadoapostolico00barr", "vidadoapostolico00barr_djvu.txt", "barros_vida-do-apostolico-padre-antonio-vieyra-por_1746.txt",
    "Vida do apostolico padre Antonio Vieyra da Companhia de Jesus, chamado por antonomasia o Grande",
    "André de Barros, S.J. (title page)", "Lisboa: na nova Officina Sylviana (title page)",
    "1746 (title page: 'M.D.CC.XLVI.', read on the page image, leaf n2; the OCR garbles the numeral)", 1746, NR, "por",
    "readable Portuguese with the long s read as f; the index lines are noisy.",
    "A Life in five books. Dedication to the Infante D. António at OCR lines 84-160; licences (1745-1746) at about 166-870. Livro I at 1099; II at 6662; III at 13684; IV at 18246; V at 25277, ending at 32571. The author's reflection at 32572; corrections at 32964; index of notable things at 32981-34641.",
    "André de Barros", LATAM, VW,
    [row("barros-vida-do-padre-antonio-vieyra", "André de Barros, Vida do apostolico padre Antonio Vieyra (1746)", "barros",
         "Livros I-V at OCR lines 1099-32571", [LATAM, SJ], "tradition", "provisional", "por",
         doc((1745, 1746), "licences of 21 May 1745 and November 1746 (about OCR lines 166-870); title page 'M.D.CC.XLVI.'"),
         "A Jesuit's Life of Vieira in five books. Its subject is Vieira; its voice is Barros.")])
for t, ident, body in [
    (1, "cartasdopantonio00viei", "Tomo 1. A library plate at OCR lines 7-12; title page at 38-72. Dedication, signed by the Conde da Ericeira, at 78-132; prologue at 141-322, which says the Conde began the collection; licences (1734-1735) at 323-870. Carta I at 873 (dated September 1647 at 919) to Carta CXXXXI at 16243 (Rome, 3 June 1674); 'Fim do Primeiro Tomo' at 16398. All the letters are Vieira's; none addressed to him was found. No index was found."),
    (2, "cartasdopantonio01viei", "Tomo 2. Title page at OCR lines 23-54; notice to the reader at 59-72; licences (1734) at 83-375. The numbering starts again: Carta I at 377, Carta CXXXXII at 15706, one more letter from 16127; 'Fim do segundo Tomo' at 16219. All the letters are Vieira's; none addressed to him was found. No index was found.")]:
    add(ident, ident + "_djvu.txt", "vieira_cartas-tomo%d-por_1735.txt" % t,
        "Cartas do P. Antonio Vieyra da Companhia de Jesu; tomo %s" % ("primeiro" if t == 1 else "segundo"),
        "António Vieira, S.J.; the collection begun by the Conde da Ericeira (dedication and prologue of tomo 1)", "Lisboa Occidental: na Officina da Congregação do Oratorio (title page)", "1735 (title page: 'M.DCC.XXXV.')", 1735, NR, "por",
        "clean Portuguese with the long s read as f.", body, "António Vieira", LATAM, VW,
        [row("vieira-cartas-tomo-%d" % t, "Vieira, Cartas, tomo %d (1735)" % t, "vieira",
             ("Cartas I-CXXXXI at OCR lines 873-16398" if t == 1 else "the letters at OCR lines 377-16219"), [LATAM, SJ], "tradition", "provisional", "por",
             (doc((1647, 1674), "the first letter is dated September 1647 (OCR line 919) and the last Rome, 3 June 1674 (16243)") if t == 1 else
              unk("the title page and licences (OCR lines 23-375) date the print to 1734-1735; the dates of the first and last letters were not read")),
             "Vieira's own letters to ministers, nobles and fellow Jesuits, first printed in 1735. His voice; the editors' choice of letters.")])

add("culturaeopulenci00anto", "culturaeopulenci00anto_djvu.txt", "antonil_cultura-e-opulencia-do-brasil-por_1711.txt",
    "Cultura e opulencia do Brasil por suas drogas, e minas, com varias noticias curiosas do modo de fazer o assucar; plantar, e beneficiar o tabaco; tirar ouro das minas; e descubrir as da prata",
    "André João Antonil (title page)", "Lisboa: na Officina Real Deslandesiana (title page)", "1711 (title page: 'Anno de 1711')", 1711, NR, "por",
    "readable Portuguese with the long s read as f; accents and spaced capitals in headings are garbled.",
    "Four parts. Dedication to the mill owners at OCR lines 107-182; preface at 216-285; licences (1710-1711) at 296-424. Part I, sugar, at 187 and from chapter I at 442; Part II, tobacco, at 4965; Part III, the gold mines, at 5910; Part IV, cattle and royal contracts, at 8260; text ends at 8754. Part I, chapter IX, how the mill owner should deal with his slaves, at 1318-1579; the chaplain's duty to teach the household and slaves in chapter IV at about 862-882. Index at 8783-9192.",
    "André João Antonil", LATAM,
    "Open-Gaps 176 (LA8-4), Library wanted: Antonil (1711), named in the census entry for colonial Brazil.",
    [row("antonil-cultura-e-opulencia-do-brasil", "Antonil, Cultura e opulencia do Brasil (1711)", "antonil",
         "the four parts at OCR lines 187-8754; on the slaves and their teaching at 828-882 and 1318-1579", [LATAM], "tradition", "provisional", "por",
         doc((1710, 1711), "licences of 12 December 1710 to 6 March 1711 (OCR lines 351-410); title page 'Anno de 1711'"),
         "A handbook of Brazil's sugar, tobacco, gold and cattle, with counsel to mill owners on the teaching and treatment of the enslaved.")])

add("BSG_8F403_7INV2830RES", "BSG_8F403_7INV2830RES_djvu.txt", "code-noir_recueil-des-reglemens-colonies-francoises-fra_prault1767.txt",
    "Le Code noir, ou Recueil des règlemens rendus jusqu'à présent, concernant le gouvernement, l'administration de la justice, la police, la discipline et le commerce des nègres dans les colonies françoises, et les conseils et compagnies établis à ce sujet",
    "The kings of France (edicts, declarations and ordinances of 1675 to 1762)", "Paris: chez Prault, imprimeur-libraire (title page and privilege)", "1767 (title page: 'M. DCC. LXVII.')", 1767,
    "the archive.org record's rights field reads 'Domaine public' (Bibliothèque Sainte-Geneviève)",
    "fra", "readable French with the long s read as f; headings and numerals are often garbled.",
    "A collection of royal acts of 1675 to 1762, not the edict alone. Table at OCR lines 111-210; privilege (24 May 1759) at 215-317. The Edict of March 1685, the Code noir proper, in 60 articles: heading at 1272, Article I at 1331, Article LX at 2342, date and signatures at 2381-2385, registration at Saint-Domingue (6 May 1687) at 2389-2393. The Edict of March 1724 for Louisiana, in 55 articles, at 11063-12459. The last act, an ordinance of 1762, at about 17100-17735; a list of registrations at 17748-17829.",
    "France (royal edicts)", LATAM,
    "Open-Gaps 176 (LA8-6), Library wanted: the Code noir (1685), for Haiti before 1804.",
    [row("code-noir-edict-of-march-1685", "Le Code noir: the Edict of March 1685 (Prault 1767 collection)", "code-noir",
         "OCR lines 1272-2393", [LATAM], "context", "needs-ruling", "fra",
         doc((1685, 1685), "the edict's own date line: 'au mois de Mars mil six cens quatre-vingt cinq' (OCR lines 2381-2385)"),
         "The king's edict on the policing of the French islands of America, in 60 articles. The crown's voice, not the church's."),
     row("code-noir-edict-of-march-1724-louisiana", "Le Code noir: the Edict of March 1724 for Louisiana (Prault 1767 collection)", "code-noir",
         "OCR lines 11063-12459", [LATAM], "context", "needs-ruling", "fra",
         doc((1724, 1724), "the edict's own date line: 'au mois de Mars ... mil sept cens vingt-quatre' (OCR lines 12456-12459)"),
         "The same law recast for Louisiana.")])

# ---------------- Asia ----------------
LW = "Wanted_Sources rows 124 and 125 (major), Library wanted: Launay, Histoire générale de la Société des Missions-Étrangères (1894), for Pallu, Lambert de la Motte and Maigrot; also the Synod of Tonkin (1670) council lead."
add("cihm_54000", "cihm_54000_djvu.txt", "launay_histoire-generale-de-la-societe-des-missions-etrangeres-t1-fra_1894.txt",
    "Histoire générale de la Société des Missions-Étrangères; tome premier", "Adrien Launay, of the same Society (title page)", "Paris: Téqui, libraire-éditeur (title page)", "1894 (title page)", 1894, NR, "fra",
    "mostly clean French; some pages are broken into columns and garbled (for example near OCR lines 13765 and 38000) and a few pages are scanned twice. Several chapter numerals are misprinted or misread.",
    "The years 1658 to 1754. A letter from the Seminary's superior from about OCR line 49; Launay's preface at 246-395. Chapters from 619 (1658); chapter IV at 7502 (1664-1665), with the Instructions known as the Monita summarized at about 9402-9604; the first synod of Tonkin (14 February 1670) at 12409-12420, on a page that appears twice (again at 13771-13792; the first copy's OCR reads the year as 1679); chapter XII at 34493 (1692-1700), with Bishop Maigrot's Mandate discussed at 34849-35060 and its articles quoted in French at about 35075-35382. 'Fin du tome premier' at 49946; table at 49957-50732. Letters and documents are quoted throughout and were not mapped one by one.",
    "Adrien Launay", VIET, LW,
    [row("launay-histoire-generale-missions-etrangeres-tome-1-1658-1754", "Launay, Histoire générale de la Société des Missions-Étrangères, tome I: 1658-1754", "launay",
         "chapters at OCR lines 619-49946; the synod of Tonkin at 12409-12420; Maigrot's Mandate at 34849-35382", [VIET, CHINA], "context", "provisional", "fra",
         doc((1894, 1894), "title page: 1894"),
         "A member of the Society tells its history from 1658 to 1754. Written in 1894; the founders speak only in the letters he quotes.")])
add("cihm_54001", "cihm_54001_djvu.txt", "launay_histoire-generale-de-la-societe-des-missions-etrangeres-t2-fra_1894.txt",
    "Histoire générale de la Société des Missions-Étrangères; tome deuxième", "Adrien Launay, of the same Society (title page)", "Paris: Téqui, libraire-éditeur (title page)", "1894 (title page)", 1894, NR, "fra",
    "mostly clean French; some chapter headings are garbled.",
    "The years 1754 to 1836. Chapter I at OCR line 68 (1754-1760); II at 3621; III at 8372; IV at 12937; V at 18559 (1780-1789); VI at 23070; VII at 27365; VIII at 30673 (1799-1805); IX at 36323 (1805-1815); X at 39801, the missionaries' voyages; XI at 42904 (1815-1823); XII at 45857 (1823-1836). 'Fin du tome' at 50731; table from 50781. Letters are quoted throughout.",
    "Adrien Launay", VIET, LW + " Tome 2 carries the same history to 1815 and beyond.",
    [row("launay-histoire-generale-missions-etrangeres-tome-2-1754-1836", "Launay, Histoire générale de la Société des Missions-Étrangères, tome II: 1754-1836", "launay",
         "chapters I-IX (1754-1815) at OCR lines 68-39800; chapters X-XII at 39801-50731", [VIET, CHINA], "context", "provisional", "fra",
         doc((1894, 1894), "title page: 1894"),
         "The Society's history from 1754 to 1836. A later account from the mission's side.")])

add("relationabregeed00pall", "relationabregeed00pall_djvu.txt", "pallu_relation-abregee-des-missions-et-des-voyages-des-evesques-francois-fra_1682.txt",
    "Relation abrégée des missions et des voyages des évesques françois, envoyez aux royaumes de la Chine, Cochinchine, Tonquin, et Siam",
    "François Pallu, bishop of Heliopolis (title page)", "Paris: chez Charles Angot, rue Saint Jacques, au Lion d'Or (title page, read on the page image, leaf n2; the OCR drops these lines)",
    "1682 (title page: 'M. DC. LXXXII.', read on the page image, leaf n2; the OCR garbles the numeral)", 1682, NR, "fra",
    "clean French for a print of its age, with the long s read as f.",
    "In order: an extract of a privilege and an approbation of 1665-1666 that name Jacques de Bourges's Relation, at OCR lines 7-36; the title page at 39-58; a scan notice at 61-69; Pallu's dedication to the archbishops, bishops and clergy of France, dated April 1668, at 74-157; a second privilege extract and approbation (April 1666) at 162-195; the Relation at 197-2429, with no chapter headings. Letters from Tonkin and elsewhere are quoted at length inside it.",
    "François Pallu", VIET,
    "Wanted_Sources row 125 (major), Library wanted: Pallu's and Lambert de la Motte's own Relations.",
    [row("pallu-relation-abregee-des-missions", "Pallu, Relation abrégée des missions et des voyages des évesques françois (Paris 1682)", "pallu",
         "the Relation at OCR lines 197-2429; the dedication at 74-157", [VIET, CHINA], "tradition", "provisional", "fra",
         doc((1668, 1682), "the dedication is dated 'ce mois d'Avril 1668' (OCR line 156); title page 'M. DC. LXXXII.'"),
         "The bishop of Heliopolis reports to the clergy of France on the missions and journeys of the French bishops sent to China, Cochinchina, Tonkin and Siam. His own voice.")])

RW = "Wanted_Sources row 126 (major) and Open-Gaps 178, Library wanted: Rhodes's own account of his missions, and the Cathechismus of 1651 with its teaching."
add("bub_gb_74U28QLld2UC", "bub_gb_74U28QLld2UC_djvu.txt", "rhodes_divers-voyages-de-la-chine-et-autres-royaumes-de-l-orient-fra_1682.txt",
    "Divers voyages de la Chine, et autres royaumes de l'Orient; avec le retour de l'autheur en Europe, par la Perse et l'Arménie; le tout divisé en trois parties",
    "Alexandre de Rhodes (the archive.org record; the title page names no author and says only 'le retour de l'Autheur'; the narrator is addressed as 'Pere Alexandre' at OCR line 6289)", "Paris: chez Christophe Journel, au dernier pillier de la grand'salle du Palais (title page)", "1682 (title page: 'M. DC. LXXXII.')", 1682, PDM, "fra",
    "clean French; some chapter numerals are wrong. Google's stamp lines stand among the first 109 OCR lines and from 14867.",
    "A printing of 1682. Privilege extract at OCR lines 71-80; preface at 134. Part 1, from Rome to China, at 253 (chapter I at 263). Part 2, the kingdom of Annam, Tonkin and Cochinchina, at 2604, chapter I at 2651 to chapter LI at 11140. Part 3, the return by Persia and Armenia, at 11354 to chapter XXI at 14505.",
    "Alexandre de Rhodes", VIET, RW,
    [row("rhodes-divers-voyages-et-missions", "Rhodes, Divers voyages de la Chine et autres royaumes de l'Orient (1682 printing)", "rhodes",
         "parts 1-3 at OCR lines 253 to about 14866; Tonkin and Cochinchina in part 2 at 2604-11353", [VIET], "tradition", "needs-ruling", "fra",
         unk("the title page (OCR lines 32-58) gives 'M. DC. LXXXII.' for this printing; the narrative opens with the departure of 1618 (OCR line 374); a year of writing was not read"),
         "The missionary tells his own journeys from 1618, with the missions of Tonkin and Cochinchina. The title page names no author. The missions he describes come before this entry's window, which is why the shelf needs a ruling.")])
add("bub_gb_GxWRJap5LkMC_3", "bub_gb_GxWRJap5LkMC_djvu.txt", "rhodes_tunchinensis-historiae-libri-duo-lat_1652.txt",
    "Tunchinensis historiae libri duo, quorum altero status temporalis huius regni, altero mirabiles evangelicae praedicationis progressus referuntur; coeptae per patres Societatis Iesu, ab anno 1627 ad annum 1646",
    "Alexandre de Rhodes, S.J. (title page)", "Lugduni: sumptibus Ioan. Bapt. Devenet, in vico Mercatorio, sub signo Crucis Aureae (title page)",
    "1652 (title page: 'M. DC. LII.', read on the page image, leaf n4; the OCR does not give the numeral)", 1652, PDM, "lat",
    "readable Latin with the long s read as f and c often read for e. Google's stamp lines stand among the first 122 OCR lines.",
    "Two books. Dedication to Innocent X from OCR line 69; to the reader at 158 and 224; chapter lists at 254 and 433; the Society's permission to print (Avignon, 1 May 1651) at about 627-641. Liber primus, the kingdom, at 657 (Caput I at 662) to 4425. Liber II, the preaching of the Gospel from 1627 to 1646, at 4449 (Caput I at 4477); 'Finis' at 12679.",
    "Alexandre de Rhodes", VIET, RW,
    [row("rhodes-tunchinensis-historiae-libri-duo", "Rhodes, Tunchinensis historiae libri duo (Lyon 1652)", "rhodes",
         "Liber I at OCR lines 657-4425; Liber II at 4449-12679", [VIET], "tradition", "needs-ruling", "lat",
         doc((1651, 1652), "the Society's permission to print, dated Avignon, 1 May 1651 (about OCR lines 627-637); title page 'M. DC. LII.'"),
         "The missionary's Latin history of Tonkin and of its mission from 1627 to 1646. The years it tells come before this entry's window, so the shelf needs a ruling.")])
add("bub_gb_p8UC5ZZ21Q8C", "bub_gb_p8UC5ZZ21Q8C_djvu.txt", "rhodes_cathechismus-in-octo-dies-divisus-lat-vie_1651.txt",
    "Cathechismus pro iis, qui volunt suscipere Baptismum, in octo dies divisus (Latin and Vietnamese in parallel columns)",
    "Alexandre de Rhodes, S.J. (title page)", "Romae: typis Sacrae Congregationis de Propaganda Fide (title page)",
    "1651 (the title page prints no year; the licence of Goswinus Nickel, vicar general of the Society, on the leaf after it is dated 'Romae 8. Iulij 1651', read on the page image, leaf n6; the archive.org record's date field also reads 1651)", 1651, None, "lat-vie",
    "the Latin reads as running text with the long s read as f. The Vietnamese is badly garbled, its tone marks lost, and can serve only to find a place. Each page is given as its Latin half and then its Vietnamese half; marginal letters are mixed into the lines.",
    "Title page at OCR lines 5-28, with the Vietnamese title garbled at 20-21. The Society's licence at 68-80 and the imprimatur at 83-86. Day 1 at 109 (Vietnamese at 136); Day 2 at 1839; Day 3 at 4291; Day 4 at 7084; Day 5 at 11186; Days 6 and 7 not found by a clean heading (page heads at 14297 and 17224); Day 8 at 21293 (Vietnamese at 21326). The text ends at 25890; errata at 25898; noise to the end.",
    "Alexandre de Rhodes", VIET, RW,
    [row("rhodes-cathechismus-in-octo-dies-divisus", "Rhodes, Cathechismus in octo dies divisus, Latin and Vietnamese (Rome 1651)", "rhodes",
         "the eight days at OCR lines 109-25890", [VIET], "tradition", "needs-ruling", "lat-vie",
         doc((1651, 1651), "the Society's licence, dated 'Romae 8. Iulij 1651' (OCR line 78, confirmed on the page image, leaf n6)"),
         "A catechism for those preparing for baptism, in eight days, in Latin beside Vietnamese in Roman letters. Only the Latin can be read in this file. Printed in 1651, as this entry's window opens; the mission it was made for is earlier, so the shelf needs a ruling.")],
    rights="Public Domain (pd-us-by-date: published 1651; the title page prints no year, and the date is taken from the printed licence on the next leaf, 'Romae 8. Iulij 1651', with which the archive.org catalog date agrees); " + PDM,
    rights_short="published 1651 by the printed licence date, out of US copyright by date")

add("bub_gb_vW4zWSxsvhIC", "bub_gb_vW4zWSxsvhIC_djvu.txt", "historia-cultus-sinensium_varia-scripta-de-cultibus-sinarum-lat_1700.txt",
    "Historia cultus Sinensium, seu varia scripta de cultibus Sinarum, inter vicarios apostolicos Gallos aliosque missionarios, et patres Societatis Jesu controversis, oblata Innocentio XII. pontifici maximo",
    "Several authors: Nicolas Charmot's notes, Charles Maigrot's Mandate, bishops' letters, and writings of the Jesuits in an appendix (the title page names no author)", "Coloniae (title page; no printer named)",
    "1700 (first title page: 'Coloniae, M. DCC.', read on the page image, leaf n6, where the OCR drops the imprint; the second title page gives 'COLONIAE' and 'M. D C C.' at OCR lines 15962 and 15971)", 1700, PDM, "lat",
    "clean Latin with the long s read as f. Google's stamp lines stand among the first 88 OCR lines and at the end.",
    "A collection of the writings laid before the Pope in the Chinese rites case. Printer to the reader at OCR lines 48-80; Nicolas Charmot's notes on the Jesuits' observations on the Mandate (29 July 1698): title at 126-157, preface from 171, five sections at 254, 5148, 5599, 6377 and 7104; a brief of Innocent XII to Maigrot at 7941; Charmot's Notationes at 8194-13133; further pieces at 13134 and 14632. Maigrot's Declaratio seu Mandatum provisionale: heading at 15623, text from 15643, dated at Chang-lo in Fujian on 26 March (the year is garbled in the OCR), signed at 15920. A second title page follows at about 15925-15971. A later piece signed by Maigrot 'in Metropoli Fokiensi' on 10 November 1693 ends at 18820. Bishops' letters at about 19234-19938; replies and memorials from 23424; Jesuit observations at 27431-32074; index from 32210; 'Finis' at 32504. The pieces between 15922 and 23424 were not mapped one by one.",
    "Charles Maigrot; Nicolas Charmot; others", CHINA,
    "Wanted_Sources row 124 (major), Library wanted: Maigrot's Mandate of 1693 in a printing of the time.",
    [row("maigrot-mandatum-provisionale-1693", "Charles Maigrot, Declaratio seu Mandatum provisionale (26 March 1693), Latin (Cologne 1700)", "maigrot",
         "OCR lines 15623-15921", [CHINA], "tradition", "provisional", "lat",
         doc((1693, 1693), "the Mandate's date line, 'die vigesima sexta mensis Martii anni Domini' (about OCR lines 15914-15918); the year is garbled there and is read 1693 from the later piece in the same volume dated 'decima Novembris 1693' (18817, where the OCR prints '16931')"),
         "The vicar apostolic of Fujian's provisional ruling for the priests of his vicariate on the disputed Chinese rites. His own text, printed in 1700."),
     row("charmot-notae-and-notationes-on-the-jesuit-observations", "Nicolas Charmot, Notae and Notationes on the Jesuits' observations on Maigrot's Mandate (in Historia cultus Sinensium, Cologne 1700)", "charmot",
         "the Notae at OCR lines 126-7940; the Notationes at 8194-13133", [CHINA], "tradition", "needs-ruling", "lat",
         doc((1698, 1700), "Charmot's notes are dated 29 July 1698 and 7 October 1698 (OCR lines 120-170, 8194); title page 'M. DCC.'"),
         "Charmot's answers to the Jesuits' observations on the Mandate, laid before the Holy Office. The Jesuits' own writings stand later in the volume (from about OCR line 27431) and are not part of this row.")])

add("ASketchOfTheRiseAndProgress", "ASketchOfTheRiseAndProgress_djvu.txt", "ceylon-catholic-church_sketch-of-the-rise-and-progress_1848.txt",
    "A Sketch of the Rise and Progress of the Catholic Church in Ceylon", "Anonymous (no author is named anywhere in the print; the archive.org record credits Simon Casie Chitty)",
    "Colombo (title page; no printer named)", "1848 (title page)", 1848, PDM, "eng",
    "clean English with scattered misreadings. Google's sheet stands at OCR lines 1-46 and its stamp after the text.",
    "Continuous prose with no chapters, from OCR line 112 to 1334. The Dutch years and the placards of 1658 and 1715 against Catholic priests at about 596-642. Father Joseph Vaz of the Goa Oratory from 754 to his death at Kandy (17 January 1711) at about 895-910. A government regulation of 27 May 1806 at 1062-1130 and a minute of 1819 at 1186-1200 are printed inside the text. Footnotes quote other writers.",
    "Anonymous", CEYLON,
    "Wanted_Sources row 127 (major) and Open-Gaps 178, Library wanted: the Sketch (Colombo, 1848) named in the census for Joseph Vaz.",
    [row("sketch-of-the-catholic-church-in-ceylon-1848", "A Sketch of the Rise and Progress of the Catholic Church in Ceylon (Colombo 1848)", "ceylon-catholic-church",
         "the text at OCR lines 112-1334; Joseph Vaz at about 754-910; the Dutch placards at about 596-642", [CEYLON], "context", "needs-ruling", "eng",
         doc((1848, 1848), "title page: 'Colombo 1848'"),
         "An unsigned history of the Catholic church in Ceylon, printed at Colombo forty years after this entry's window closes. The host's attribution to Simon Casie Chitty is not in the print.")])

BW = "Wanted_Sources row 156 and Open-Gaps 178, Library wanted: Baldaeus (Amsterdam, 1672), a Dutch Reformed account of the Ceylon church."
add("naauwkeurigebesc00bald", "naauwkeurigebesc00bald_djvu.txt", "baldaeus_naauwkeurige-beschryvinge-van-malabar-en-choromandel-en-ceylon-nld_1672.txt",
    "Naauwkeurige beschryvinge van Malabar en Choromandel, der zelver aangrenzende ryken, en het machtige eyland Ceylon; nevens een omstandige en grondigh doorzochte ontdekking en wederlegginge van de afgoderye der Oost-Indische heydenen",
    "Philippus Baldaeus (title page)", "Amsterdam: by Johannes Janssonius van Waasberge, en Johannes van Someren (title page)", "1672 (title page: 'Anno 1672')", 1672, NR, "nld",
    "legible Dutch with the long s read as f; ornaments are garbled and side notes are mixed into the lines.",
    "Three parts. Privilege (1669) at about OCR line 126; dedication, dated Geervliet, 15 August 1671, at 137-275; preface at 283. Part 1, Malabar and Choromandel, chapters from 587; a short Tamil grammar ('Malabaarsche Spraak-konst') at about 29827-30500. Part 2, Ceylon, at 30628, chapters I-LI from 30634: Manaar at 52404; the siege of Jaffna at 53425; the provinces of Jaffnapatnam and their churches and schools at about 54380-55692; to 62794. Part 3, the idolatry of the East Indian heathen, with its own title page dated 1672, at 62797-87039. Indexes at 87042-88794.",
    "Philippus Baldaeus", VOC, BW,
    [row("baldaeus-beschryvinge-ceylon-and-the-jaffna-churches", "Baldaeus, Naauwkeurige beschryvinge: Ceylon, with the churches of Jaffnapatnam (1672)", "baldaeus",
         "part 2 at OCR lines 30628-62794; the Jaffna churches at about 54380-55692", [VOC], "tradition", "provisional", "nld",
         doc((1671, 1672), "dedication dated 'Geervliet den 15 Aug. 1671' (OCR line 275); title page 'Anno 1672'"),
         "A Dutch minister in Ceylon describes the island and the churches and schools of Jaffnapatnam. The VOC church's own voice."),
     row("baldaeus-beschryvinge-as-witness-to-ceylon-catholics", "Baldaeus, Naauwkeurige beschryvinge: Ceylon, as a witness to its Catholics (1672)", "baldaeus",
         "part 2 at OCR lines 30628-62794", [CEYLON], "context", "provisional", "nld",
         doc((1671, 1672), "dedication dated 15 August 1671 (OCR line 275); title page 'Anno 1672'"),
         "The Reformed minister's account, read for the Catholics of Jaffna and Manaar. An opponent's view."),
     row("baldaeus-beschryvinge-malabar-choromandel-and-afgoderye", "Baldaeus, Naauwkeurige beschryvinge: Malabar and Choromandel, and the Afgoderye (1672)", "baldaeus",
         "part 1 from OCR line 587 to about 30627; part 3 at 62797-87039", [VOC], "tradition", "needs-ruling", "nld",
         doc((1671, 1672), "title pages 'Anno 1672'"),
         "The minister's description of the Indian coasts and of Hindu religion as he understood it.")])
add("trueexactdescrip00bald", "trueexactdescrip00bald_djvu.txt", "baldaeus_true-and-exact-description-of-malabar-and-coromandel-and-ceylon_churchill1703.txt",
    "A True and Exact Description of the Most Celebrated East-India Coasts of Malabar and Coromandel, as also of the Isle of Ceylon; translated from the High-Dutch printed at Amsterdam, 1672 (A Collection of Voyages and Travels, vol. III)",
    "Philippus Baldaeus; the translator is not named (title page)", "London: printed for Awnsham and John Churchill, at the Black Swan in Pater-Noster-Row (engraved title)",
    "1703 (the engraved title: '1703', read on the page image, leaf n12; the letterpress title, leaf n14, carries no imprint and marks the part 'Vol. III.')", 1703, NR, "eng",
    "readable English with the long s read as f, in short lines. OCR lines 1-559 are noise from blank leaves.",
    "The English translation, the part of Churchill's third volume that holds Baldaeus and nothing else. Engraved title at about OCR lines 600-661; letterpress title at 667-709 (the OCR reads the Dutch year as 1572); preface at 804. Malabar and Coromandel at 1045 (chapter I at 1067); Ceylon at 21284, with Manaar at about 42270-42540 and the provinces and churches of Jaffnapatnam at about 43514-45522; the idolatry of the East-India pagans at 47930. The text ends at 58273, 'Finis' at 58276; an index to the volume follows.",
    "Philippus Baldaeus", VOC, BW + " The English printed by 1930, beside the Dutch.",
    [row("baldaeus-description-of-ceylon-english-1703", "Baldaeus, A True and Exact Description: Ceylon, English (Churchill 1703)", "baldaeus",
         "Ceylon at OCR lines 21284-47929; the Jaffna churches at about 43514-45522", [VOC], "tradition", "provisional", "eng",
         doc((1672, 1703), "letterpress title: 'Translated from the High-Dutch printed at Amsterdam, 1672'; engraved title 1703"),
         "The English of the Reformed minister's account of Ceylon and its parishes. A translation; the Dutch is held."),
     row("baldaeus-description-english-as-witness-to-ceylon-catholics", "Baldaeus, A True and Exact Description: Ceylon, as a witness to its Catholics, English (Churchill 1703)", "baldaeus",
         "Ceylon at OCR lines 21284-47929", [CEYLON], "context", "provisional", "eng",
         doc((1672, 1703), "letterpress title names the Dutch print of 1672; engraved title 1703"),
         "The same account, read for the Catholics the Dutch found in Jaffna and Manaar. An opponent's view.")])

add("oudennieuwoostin03vale", "oudennieuwoostin03vale_djvu.txt", "valentijn_oud-en-nieuw-oost-indien-deel3-nld_1726.txt",
    "Oud en Nieuw Oost-Indiën, derde deel: Omstandig verhaal van de geschiedenissen en zaaken het kerkelyke ofte den godsdienst betreffende, zoo in Amboina, als in alle de eylanden, daar onder behoorende; mitsgaders een beschryving van Banda, Timor en Solor, Celebes ofte Macassar, Borneo en Bali, Tonkin, Cambodia en Siam",
    "François Valentyn (title page)", "Dordrecht: Joannes van Braam; Amsterdam: Gerard onder de Linden (title page)",
    "1726 (title page: 'MDCCXXVI', read on the page image, leaf n4; the archive.org record's date field reads 1724, the year of the first deel)", 1726,
    "the archive.org record is tagged NOT_IN_COPYRIGHT", "nld",
    "legible Dutch with the long s read as f; headings and some words are garbled and side notes are mixed into the lines. A library bookplate stands at OCR lines 67-77.",
    "The third deel, in two stukken. Foreword at OCR line 151. First stuk: the church affairs of Amboina, heading at 399; Eerste Boek at 422; Tweede Boek at 7858, with Leidekker and the Malay Bible in its fourth chapter at about 13377-15027; Derde Boek at 15028-29073, with the dispute over the Malay Bible translation at about 16611-21829 and the lists of ministers at about 26632-29073. Vierde and Vyfde Boek, the trees and animals of Amboina, at 29074 to about 91530. Second stuk, with its own title page at about 91531: Banda at 105318; Solor and Timor at 126531; Macassar at 127660; Borneo at 146036; Tonkin at 150101; Cambodia at 155831; Siam at 158873; text ends at about 165214. Index from 165219. Bali was not found as its own division.",
    "François Valentijn", VOC,
    "Open-Gaps 178, Library wanted: Valentijn, Oud en Nieuw Oost-Indiën, for the Protestant churches of the VOC world (census VII.43, which had no file).",
    [row("valentijn-ambonsche-zaaken-van-den-godsdienst", "Valentijn, Oud en Nieuw Oost-Indiën, deel 3: the church affairs of Amboina (1726)", "valentijn",
         "Eerste to Derde Boek at OCR lines 399-29073; the Malay Bible dispute at about 13377-21829; the ministers' lists at about 26632-29073", [VOC], "tradition", "provisional", "nld",
         doc((1726, 1726), "title page: 'MDCCXXVI'"),
         "A Dutch minister's history of the church of Amboina and its ministers, with the dispute over the Malay Bible translation. The VOC church's own voice."),
     row("valentijn-deel-3-other-lands", "Valentijn, Oud en Nieuw Oost-Indiën, deel 3: Banda, Timor, Macassar, Borneo, Tonkin, Cambodia, Siam (1726)", "valentijn",
         "the second stuk at OCR lines 91531-165214", [VOC], "tradition", "needs-ruling", "nld",
         doc((1726, 1726), "title page: 'MDCCXXVI'"),
         "The minister's descriptions of other lands of the Company's trade. Church matters there were not mapped.")])

RULED = {
    "annales-regum-iyasu-ii-et-iyoas_versio-fra_guidi1912.txt": {"ethiopian-royal-chronicles": ("anonymous", "The title page (file lines 233-305) names the kings whose annals these are and Ignazio Guidi as translator; it names no author.")},
    "annales-regum-iyasu-ii-et-iyoas_textus-gez_guidi1910.txt": {"ethiopian-royal-chronicles": ("anonymous", "The title page (file lines 133-177) names the kings whose annals these are and Ignazio Guidi as editor; it names no author.")},
    "gobat_journal-of-a-three-years-residence-in-abyssinia_1834.txt": {"lee-samuel": ("metadata-omission", "The title page (file lines 81-109) reads 'A Brief History of the Church of Abyssinia, by the Rev. Professor Lee, D.D.'; the history stands at file lines 675-2834.")},
    "historia-cultus-sinensium_varia-scripta-de-cultibus-sinarum-lat_1700.txt": {
        "maigrot": ("metadata-omission", "The Mandate is headed with his name (file lines 15645-15657, 'Carolus Maigrot Sacerdos Vicarius Apostolicus Fokiensis') and signed 'Carolus Maigrot' at file line 15932."),
        "charmot": ("metadata-omission", "The notes on the Jesuits' observations on the Mandate are headed 'a Nicolao Charmot' (heading at file lines 138-169, his name at 158); the title pages name no author.")},
    "rhodes_divers-voyages-de-la-chine-et-autres-royaumes-de-l-orient-fra_1682.txt": {"rhodes": ("metadata-omission", "The title page (file lines 44-70) names no author; the archive.org record credits Alexandre de Rhodes, and the narrator is addressed as 'Pere Alexandre' at file line 6301. The attribution is the record's.")},
}
for it in items:
    if it["filename"] in RULED:
        it["authors_ruled"] = {k: dict(kind=v[0], evidence=v[1]) for k, v in RULED[it["filename"]].items()}
json.dump(items, open(S + "spec1.json", "w"), ensure_ascii=False, indent=1)
print(len(items), "items")
for it in items:
    assert len(it["filename"]) < 120 and it["filename"].endswith(".txt")
