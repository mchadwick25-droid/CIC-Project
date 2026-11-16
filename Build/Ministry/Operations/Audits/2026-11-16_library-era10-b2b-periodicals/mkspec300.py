import json, re, sys, glob

S = sys.argv[1].rstrip("/") + "/"
NR = "the archive.org record carries no rights field, so the printed date is the basis"
A12 = "; add 12 to OCR line numbers"
items = []
_cache = {}
FAILS = []
NCHK = [0]


def lines(ident):
    if ident not in _cache:
        (p,) = glob.glob(S + "dl/" + ident + "__*_djvu.txt")
        _cache[ident] = (p, open(p, encoding="utf-8", errors="replace").read().split("\n"))
    return _cache[ident]


def chk(ident, n, pat, span=2):
    """The host line n (1-based), or a neighbor within span, must match pat."""
    NCHK[0] += 1
    ls = lines(ident)[1]
    win = " ".join(re.sub(r"\s+", " ", x) for x in ls[max(0, n - 1 - span): n + span])
    if not re.search(pat, win, re.I):
        FAILS.append((ident[-24:], n, pat, win[:200]))


def pd(y, extra):
    return "Public Domain (pd-us-by-date: published %s); %s" % (y, extra)


def row(slug, work, author, locus, atlas, role, conf, lang, date, note, voice_of=None):
    r = dict(slug=slug, work=work, author=author, locus=locus if locus == "whole" else locus + A12, atlas_ids=atlas, role=role, confidence=conf, language=lang, date=date, note=note)
    if voice_of:
        r["voice_of"] = voice_of
    return r


def doc(y, src):
    return dict(start=y[0], end=y[1], source=src, fc="Documented")


def add(ident, filename, title, creator, publisher, pubdate, year, extra, lang, ocr, content, seed_author, world, want, rows):
    p = lines(ident)[0]
    it = dict(src=p, filename=filename, title=title, creator=creator, publisher=publisher, pubdate=pubdate,
              rights=pd(year, extra), rights_short="published %s, out of US copyright by date" % year, lang=lang, item=ident,
              djvu_name=p.split("__", 1)[1], ocr=ocr, content=content, seed_title=title, seed_author=seed_author, year=str(year), world=world,
              why=want, contents_note=content, want=want, rows=rows)
    items.append(it)


ANG = "the-anglican-communion-twentieth-century"
GRK = "the-greek-church-and-the-ecumenical-patriarchate"
RUS = "the-russian-orthodox-church-council-patriarchate-and-reunion"
NM = "the-russian-new-martyrs-and-the-catacomb-church"
EMI = "emigre-orthodoxy-and-the-paris-school"
BALK = "orthodoxy-in-the-communist-balkans"
SAYFO = "the-sayfo-and-the-syriac-diaspora"
ECU = "the-ecumenical-movement-and-the-wcc"
SVM = "the-student-volunteer-movement-and-edinburgh-191"
AIC = "african-initiated-churches-harrist-aladura-zioni"
MART = "northeast-india-and-mar-thoma-twentieth-century"
INDO = "indonesian-christianity-the-independent-century"
LAP = "protestantism-in-latin-america"
JAP = "japanese-christianity-after-1906"
W = "Era 10 batch 2, found and not yet taken: "
ROM = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI"}
COVER = "Published for the Anglican & Eastern Churches Assocn. by the Faith Press, Ltd. (cover, read on the page image, leaf n0)"
EDS = "The Christian East (many writers); edited by the Rev. Canon J. A. Douglas and the Rev. R. M. French (cover, read on the page image, leaf n0)"
NOCOVER_P = "Not printed in the number as scanned, which has no cover leaf"
NOCOVER_C = "The Christian East (many writers); the number as scanned has no cover leaf and names no editor"


def ce(sfx, vol, no, label, year, mast, pubnote, cover, ocr, parts, end, docs, extra_content=""):
    """One number of The Christian East. mast=(line, pattern). parts=[(text, line, pattern)].
    end=(line, pattern, text). docs=[(slug, work, a, apat, b, bpat, atlas, role, lang, (y0,y1), datesrc, note)]."""
    ident = "per_christian-east_the-christian-east_" + sfx
    chk(ident, mast[0], mast[1])
    for t, n, pat in parts:
        chk(ident, n, pat)
    chk(ident, end[0], end[1])
    title = "The Christian East, volume %s, number %d (%s)" % (ROM[vol], no, label)
    stem = "christian-east_v%d-no%d-%s" % (vol, no, re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-"))
    content = "One number of the quarterly. Masthead at OCR line %d. Contents, by the OCR line of each heading: %s. %s%s" % (
        mast[0], "; ".join("%s (%d)" % (t, n) for t, n, _ in parts), end[2], (" " + extra_content) if extra_content else "")
    rows = [row("whole", title, "christian-east", "whole", [ANG], "tradition", "assigned", "eng",
                doc((year, year), "masthead: '%s'" % label),
                "One number of the quarterly, by many writers. The Eastern documents it prints are in the journal's English unless a row says otherwise.")]
    for slug, work, a, apat, b, bpat, atlas, role, lang, ys, dsrc, note in docs:
        chk(ident, a, apat); chk(ident, b, bpat)
        rows.append(row(slug, work + ", in The Christian East", "christian-east", "OCR lines %d-%d" % (a, b), atlas, role, "assigned", lang, doc(ys, dsrc), note))
    add(ident, stem + ".txt", title, EDS if cover else NOCOVER_C, COVER if cover else NOCOVER_P,
        "%d (%s)" % (year, pubnote), year, NR, "eng", ocr, content, "The Christian East", ANG,
        W + "The Christian East, the issues to 1930 not yet held.", rows)
CLEAN = "Mostly clean English prose; running heads, page numbers and footnotes sit in the text, Greek is garbled, and plate leaves leave runs of junk lines."
OWN = "His own words in the journal's English; the print names no translator."

ce("1920-03_1_1", 1, 1, "March, 1920", 1920, (1, r"MARCH, 1920"), "masthead: 'March, 1920', OCR line 1", False, CLEAN,
   [("the Archbishop of Canterbury's Foreword, dated Lambeth, February 2, 1920", 13, r"FOREWORD|ARCHBISHOP|NOW, as"),
    ("G. K. A. Bell, 'War-Time Correspondence between the Archbishop of Canterbury and the Church of Russia'", 70, r"WAR-TIME"),
    ("Constantine Ageiev, on the Russian Orthodox Church and the Russian people under the Bolsheviks", 1439, r"RUSSIAN ORTHODOX"),
    ("'The Doctrine of the Holy Images'", 2959, r"HOLY IMAGES"),
    ("'Prospects of Union between the Eastern and Anglican Churches', by the Editor", 3437, r"PROSPECTS OF UNION"),
    ("'Review of Four Years'", 4456, r"REVIEW OF FOUR"),
    ("'The Christians of Turkey'", 5081, r"CHRISTIANS OF TURKEY"),
    ("the American bishops' message to the Archbishop of Canterbury", 5345, r"AMERICAN BISHOPS")],
   (5415, r"March 3, 1920", "The text ends at 5415 with cables taken from the Times of March 3, 1920; junk lines from a plate leaf follow."),
   [("patriarch-tikhon-reply-to-the-archbishop-of-canterbury-1918", "Patriarch Tikhon, reply to the Archbishop of Canterbury (1918)", 518, r"following reply, in English", 613, r"Patriarch of All Russia",
     [RUS, NM], "tradition", "eng", (1918, 1918), "the letter is dated January 12/25, 1918 (OCR line 610)",
     "His own letter, which Bell's article says he sent in English. It stands inside Bell's narrative.")])

ce("1920-06_1_2", 1, 2, "June, 1920", 1920, (1, r"JuNE, 1920"), "masthead: 'June, 1920', OCR line 1", False, CLEAN,
   [("the Archbishop of Canterbury's letter to the locum tenens of the Ecumenical Patriarchate, March 4, 1920", 7, r"LETTER FROM ARCHBISHOP"),
    ("'Letter from Constantinople', the encyclical 'Unto all the Churches of Christ wheresoever they be'", 147, r"LETTER FROM CONSTANTINOPLE"),
    ("the committee on relations with the Eastern churches", 489, r"COMMITTEE ON OUR RELATIONS"),
    ("'Relations of the Constantinopolitan and Anglican Churches', Metropolitan Chrysanthos of Trebizond's report, translated from the Greek of Ecclesiastike Aletheia", 670, r"RELATIONS OF THE"),
    ("J. A. Douglas, 'The Importance of St. Sophia'", 1293, r"IMPORTANCE OF ST"),
    ("'The Mansfield Resolutions'", 2662, r"MANSFIELD"),
    ("'A Russian Layman on Reunion'", 2793, r"RUSSIAN LAYMAN"),
    ("Madame Romalo, 'A Few Words about the Church of Rumania'", 3584, r"FEW WORDS ABOUT"),
    ("Patriarch Tikhon, 'A Letter to the Russian Rulers, 1918'", 3867, r"RUSSIAN RULERS"),
    ("'Notes on Recent Events'", 4082, r"NOTES ON RECENT"),
    ("'Some Books on Armenia'", 4482, r"BOOKS ON ARMENIA"),
    ("a list of the Eastern Churches Committee", 5279, r"EASTERN CHURCHES COMMITTEE")],
   (5381, r"Fynes-Clinton", "The text ends at 5381 with the committee list; junk lines follow."),
   [("ecumenical-patriarchate-encyclical-unto-all-the-churches-of-christ-1920", "The Ecumenical Patriarchate, encyclical 'Unto all the Churches of Christ wheresoever they be' (January 1920)", 155, r"UNTO.? ALL THE CHURCHES", 460, r"CHRYSOSTOM",
     [GRK], "tradition", "eng", (1920, 1920), "dated 'in the month of January, in the year of Grace one thousand nine hundred and twenty' (OCR lines 440-443)",
     "The synod's own encyclical, signed by the locum tenens Dorotheus and eleven metropolitans, in English; the print names no translator."),
    ("patriarch-tikhon-a-letter-to-the-russian-rulers-1918", "Patriarch Tikhon, 'A Letter to the Russian Rulers, 1918'", 3867, r"RUSSIAN RULERS", 4072, r"Press, with the exception",
     [RUS, NM], "tradition", "eng", (1918, 1918), "the heading gives 1918",
     OWN + " The OCR of the heading and of the last lines is damaged.")])

ce("1920-12_1_4", 1, 4, "December, 1920", 1920, (1, r"DECEMBER, 1920"), "masthead: 'December, 1920', read on the page image, leaf n0, and at OCR line 1, where the volume number is lost", False, CLEAN,
   [("'The Massacre of Nicaea': a covering letter from Archimandrite Dionysios E. Menas, October 8, 1920, and the Bishop of Nicaea's report", 7, r"MASSACRE"),
    ("J. A. Douglas, 'Nicaea and its Church'", 508, r"ITS CHURCH"),
    ("R. M. French, 'Our Part in the Future of Yougoslavia'", 856, r"OUR PART IN THE FUTURE"),
    ("Harold Buxton, 'Armenia'", 1512, r"ARMENIA"),
    ("J. A. Douglas, 'The Eastern Orthodox and Anglican Orders'", 2163, r"EASTERN ORTHODOX AND"),
    ("'The League of Churches', by the Secretary of the Holy Synod, Constantinople", 3223, r"LEAGUE OF CHURCHES"),
    ("'Notes on Recent Events'", 3479, r"ON RECENT EVENTS")],
   (3770, r"inevitable", "The book notices end at 3770. A memorial leaf for Dorotheos of Brusa, who 'died in London, Friday, March 17th, 1921', stands at 3920-3933, later than the number's date."),
   [("basil-of-nicaea-report-on-the-massacre-of-nicaea-1920", "Basil, Bishop of Nicaea, report to the locum tenens Dorotheos on the destruction at Nicaea (1920)", 39, r"DOROTHEOS, LOCUM TENENS", 505, r"25th, 1920",
     [GRK], "tradition", "eng", (1920, 1920), "signed at Kios, September 25th, 1920 (OCR lines 500-505)",
     "A bishop's own report to his synod, in English; the print names no translator.")])

ce("1921-04_2_1", 2, 1, "April, 1921", 1921, (1, r"APRIL, 1921"), "masthead: 'April, 1921', OCR line 1", False, CLEAN,
   [("Editorial, opening with a message of Dorotheos, locum tenens, to the English clergy", 7, r"EDITORIAL"),
    ("on the death of the locum tenens of the Ecumenical Throne", 411, r"DEATH.{0,3} OF THE"),
    ("'The Funeral', by an English priest", 590, r"FUNERAL"),
    ("'The Betrayal of Saint Sophia'", 1142, r"BETRAYAL"),
    ("the Great Protosynkellos Athenagoras, 'St. Sophia and its Last Liturgy', translated from Ekklesiastike Aletheia", 1240, r"SOPHIA AND ITS LAST"),
    ("Emily J. Robinson, 'The Armenian Church and People'", 1637, r"ARMENIAN CHURCH"),
    ("T. Papaporphyriou, 'The Church of Cyprus'", 1907, r"CHURCH OF CYPRUS"),
    ("Euphrosyne Kephala, 'Monasteries in Greece'", 2226, r"MONASTERIES"),
    ("'The Syrian Christians of India', signed Karimpankal V. Thomas", 3084, r"SYRIAN CHRISTIANS"),
    ("'The Russian Church under Bolshevik Persecution'", 3470, r"RUSSIAN CHURCH UNDER"),
    ("D. S. Maric, 'Serbian Church Notes'", 3697, r"SERBIAN CHURCH NOTES"),
    ("'A Chronicle and Causerie'", 3865, r"CHRONICLE"),
    ("'Our Bookshelf'", 4272, r"OUR BOOKSHEL")],
   (4658, r"fall to him", "The book notices end at 4658; a plate caption and junk lines follow."),
   [], "An advertisement for another periodical, with the Society for Promoting Christian Knowledge's imprint, stands at about 240-264; it is not this journal's imprint.")

ce("1921-09_2_3", 2, 3, "September, 1921", 1921, (1, r"SEPTEMBER, 1921"), "masthead: 'September, 1921', OCR line 1", False, CLEAN + " The Greek hymn texts are heavily garbled.",
   [("Editorial", 7, r"EDITORIAL"),
    ("'The Armenian Patriarchate of Jerusalem', signed Abel, Vardapet", 113, r"ARMENIAN PATRIARCHATE"),
    ("Professor P. Comnenos, 'Anglican Ordinations', in translation, with an introduction and bracketed notes by J. A. Douglas", 149, r"ANGLICAN ORDINATIONS"),
    ("Cheddo Miyatovic, 'King Peter'", 861, r"KING PETER"),
    ("D. S. Maritch, 'Serbian Church Notes'", 996, r"SERBIAN CHURCH NOTES"),
    ("Emily J. Robinson, 'The Position in Armenia'", 1157, r"POSITION IN ARMENIA"),
    ("'Hymns of the Greek Church', translated by G. R. Woodward", 1305, r"HYMNS"),
    ("'A Short History of the Serbian Church'", 2955, r"A SHORT .{0,10}OF THE SERBIAN"),
    ("a summary of the report of the commission on the dissensions in the Orthodox Patriarchate of Jerusalem", 3314, r"SUMMARY|REPORT OF THE COMMISSION|DISSENSIONS"),
    ("'The Czecho-Slovak Church'", 4007, r"CZECHO"),
    ("'Constantinople Letter'", 4114, r"STANTINOPLE LETTER"),
    ("'Jerusalem Letter'", 4177, r"JERUSALEM LETTER"),
    ("'A Chronicle and Causerie'", 4281, r"CHRONICLE")],
   (4380, r"spiritual fathers", "The text ends at 4380."),
   [("comnenos-anglican-ordinations-1921", "P. Comnenos, 'Anglican Ordinations' (1921)", 149, r"ANGLICAN ORDINATIONS", 860, r"KING PETER",
     [GRK], "tradition", "eng", (1921, 1921), "printed in the number of September, 1921",
     "A Greek professor's monograph in translation. The introduction and the notes in brackets are J. A. Douglas's, and he says the translation was checked by Miss E. Kephala (OCR lines 232-236).")])

ce("1921-12_2_4", 2, 4, "December, 1921", 1921, (1, r"DECEMBER, 192"), "masthead: 'December, 1921', read on the page image, leaf n0; the OCR reads '192T' at line 1", False, CLEAN + " The hymn pages are heavily garbled; the French is clean apart from accents.",
   [("'St. George of the Phanar'", 7, r"GEORGE OF THE PHANAR"),
    ("H. J. Fynes-Clinton, 'A Visit to Serbia'", 32, r"VISIT.? TO SERBIA"),
    ("'The Gleaning of Asia Minor'", 855, r"GLEANING"),
    ("'Meditations on Cilicia and the Near East', by an Armenian ecclesiastic", 959, r"MEDITATIONS"),
    ("J. A. Douglas, 'Relations with Mar Ignatios'", 1091, r"MAR IGNATIOS"),
    ("'An Archbishop in a Cellar', translated from Sevodnia", 1792, r"ARCHBISHOP IN A CELLAR"),
    ("'A Chronicle and Causerie'", 1902, r"CHRONICLE"),
    ("hymns of the Greek church, January to March, translated by G. R. Woodward", 2413, r"JANUARY"),
    ("Bishop Gorazd, 'The Czecho-Slovak Church and the Serbs', translated from the Belgrade Politika by R. M. French", 3560, r"CZECHO"),
    ("'The Church Waxen Candle'", 3748, r"WAXEN CANDLE"),
    ("'Memorial to the League of Nations', by the Metropolitan of Caesarea, in French", 3850, r"MEMORIAL TO THE LEAGUE"),
    ("'Constantinople Letter'", 4046, r"CONSTANTINOPLE LETTER"),
    ("'Our Bookshelf'", 4136, r"BOOKSHELF")],
   (4164, r"outposts of the Greek", "The last book notice breaks off at 4164; a plate caption and junk lines follow."),
   [("nicolas-of-caesarea-memorial-to-the-league-of-nations-1921", "Nicolas, Archbishop of Caesarea, locum tenens of the Ecumenical Patriarchate, memorial to the League of Nations (1921)", 3850, r"MEMORIAL TO THE LEAGUE", 4043, r"13/26 .ovembre, 1921",
     [GRK], "tradition", "fra", (1921, 1921), "dated '13/26 novembre, 1921' (OCR line 4043)",
     "The locum tenens's own memorial, printed in French with no English.")])

ce("1922-03_3_1", 3, 1, "March, 1922", 1922, (1, r"Marc., 1922"), "masthead: 'March, 1922', OCR line 1, where the volume number reads 'Il.'", False, CLEAN + " The Greek of the Patriarch's letter and of the hymns is garbled.",
   [("'Letter from the Oecumenical Patriarch' Meletios to the editors, in Greek and in English, dated London, January 21, 1922", 7, r"LETTER FROM THE"),
    ("'Report of the Delegation of the Patriarchate sent to the Conference at Lambeth, 1920'", 89, r"REPORT OF THE DELEGATION|CONFERENCE AT LAMBETH"),
    ("Professor Nicholas Gloubokovsky, 'Eastern Orthodoxy and Anglicanism'", 1483, r"EASTERN ORTHODOXY AND"),
    ("hymns of the Greek church, April to June, translated by G. R. Woodward", 2154, r"APRIL"),
    ("'Jerusalem Letter'", 3448, r"JERUSALEM LETTER"),
    ("a memorandum on the sale of Orthodox patriarchal properties", 3541, r"MEMORANDUM"),
    ("J. A. Douglas, 'Relations with Mar Ignatios'", 3658, r"MAR IGNATIOS"),
    ("'A Chronicle and Causerie'", 3988, r"CHRONICLE"),
    ("a list of the Constantinople delegation to the Lambeth Conference", 4314, r"CONSTANTINOPLE DELEGATION")],
   (4318, r"Metropolitan of Demotica", "The list, garbled, ends the text at about 4327."),
   [("ecumenical-patriarchate-report-of-the-delegation-to-the-lambeth-conference-1920", "Report of the Delegation of the Ecumenical Patriarchate sent to the Lambeth Conference, 1920", 89, r"REPORT OF THE DELEGATION|CONFERENCE AT LAMBETH", 1482, r"EASTERN ORTHODOXY AND",
     [GRK], "tradition", "eng", (1920, 1922), "the report is of the delegation to the Lambeth Conference of 1920 and is printed in the number of March, 1922",
     "The delegation's own report to its synod, in an English the Chronicle says 'was officially forwarded to us from the Phanar' (OCR lines 4201-4202).")])

ce("1922-12_3_4", 3, 4, "December, 1922", 1922, (1, r"DECEMBER, 1922"), "masthead: 'December, 1922', read on the page image, leaf n0, and at OCR line 1, where the volume number is lost", False, CLEAN,
   [("Editorial, 'The Work of Lausanne'", 7, r"EDITORIAL|WORK OF LAUSANNE"),
    ("'Constantinople and Anglican Orders', the Archbishop of Canterbury's reply to the Ecumenical Patriarch, September 15, 1922, with a Greek version", 379, r"CONSTANTINOPLE AND ANGLICAN"),
    ("'The Smyrna Holocaust'", 485, r"SMYRNA"),
    ("Professor N. Glubokovsky, 'The Church in the New European States'", 879, r"NEW EUROPEAN STATES|CHURCH IN THE NEW"),
    ("a memorandum of twelve Orthodox bishops of the Russian Patriarchate on an autocephalous church in the Warsaw metropoly", 1056, r"MEMORANDUM|POLAND"),
    ("F. Gavin, 'The Greek Orthodox Church and Biblical Criticism'", 1254, r"BIBLICAL CRITICISM|GREEK ORTHODOX CHURCH"),
    ("'Open Letter of the Patriarch of Jugo Slavia', translated from Glasnik by R. M. French", 2039, r"OPEN LETTER"),
    ("'The Metropolitan of Thyatira at the A. and E.A. Anniversary'", 2193, r"THYATIRA"),
    ("W. A. Wigram, 'Among the Refugees'", 2421, r"REFUGEES"),
    ("J. A. Douglas, 'Roman Controversialists and Anglican-Orthodox Friendship'", 2828, r"ROMAN CONTROVERSIALISTS"),
    ("'The Serb Patriarchate', translated from Ekklesiastike Aletheia", 3072, r"SERB PATRIARCHATE"),
    ("'A Chronicle and Causerie'", 3143, r"CHRONICLE")],
   (3439, r"Theological", "The Chronicle ends at 3439; junk lines follow."),
   [("patriarch-dimitri-of-serbia-open-letter-1922", "Dimitri, Patriarch of Serbia, open letter (1922)", 2039, r"OPEN LETTER", 2156, r"PATRIARCH OF SERBIA",
     [BALK], "tradition", "eng", (1922, 1922), "printed in the number of December, 1922; the letter's own date was not found",
     "The Patriarch's own appeal, in an English 'made from Glasnik by the Rev. R. M. French' (OCR line 2043).")])
CV = "The cover leaf's OCR at the head of the file is garbled. "

ce("1924-02_5_1", 5, 1, "February, 1924", 1924, (1, r"FEBRUARY, 1924"), "masthead: 'February, 1924', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie'", 7, r"CHRONICLE"),
    ("letters between the Patriarch of Constantinople, Gregory VII, and the Archbishop of Canterbury, December 1923 and January 1924", 559, r"FROM THE PATRIARCH OF CONSTANTINOPLE"),
    ("'Bishop Bury in Moscow'", 716, r"BURY IN MOSCOW"),
    ("on the position of Patriarch Tikhon and the church in Russia after his liberation from prison, translated from the organ of the Russian synod in Belgrade, October 15/28, 1923", 1396, r"POSITION OF HIS HOLINESS"),
    ("the Metropolitan Anthony of Kiev, 'The Orthodox Church and the Papacy', the journal's translation of his own summary of a lecture", 1757, r"ORTHODOX CHURCH AND THE PAPACY"),
    ("Mar Timotheos, Archbishop of Malabar, 'The Present Position of the Assyrian Church'", 1832, r"PRESENT POSITION"),
    ("Pierre Batiffol, 'Papal Rome and the Orthodox East'", 2008, r"PAPAL ROME"),
    ("'The Kalendar'", 2690, r"KALENDAR"),
    ("'The Syrian Church of Malabar'", 3363, r"SYRIAN CHURCH OF MALABAR"),
    ("'Athens Letter'", 3610, r"ATHENS LETTER")],
   (3610, r"ATHENS LETTER", "The Athens Letter breaks off near 3690, and plate-leaf junk follows; the scan lacks the end of the number."),
   [("gregory-vii-of-constantinople-letter-to-the-archbishop-of-canterbury-1923", "Gregory VII, Patriarch of Constantinople, letter to the Archbishop of Canterbury (1923)", 559, r"FROM THE PATRIARCH OF CONSTANTINOPLE", 603, r"GREGORIUS CONSTANTINOPOLITANUS",
     [GRK], "tradition", "eng", (1923, 1923), "signed and dated December 21, 1923 (OCR line 603)",
     "The Patriarch's own letter in English; the print names no translator."),
    ("anthony-of-kiev-the-orthodox-church-and-the-papacy-1923", "Anthony, Metropolitan of Kiev, 'The Orthodox Church and the Papacy' (1923)", 1757, r"ORTHODOX CHURCH AND THE PAPACY", 1831, r"PRESENT POSITION",
     [EMI], "tradition", "eng", (1923, 1923), "the editors' note: translated from his synod's publication of 15/28 October (OCR lines 1770-1771), in the number of February, 1924",
     "His own summary of a lecture given in Belgrade, in the journal's translation; a summary, not the lecture.")])

ce("1924-05_5_2", 5, 2, "May, 1924", 1924, (1, r"May, 1924"), "masthead: 'May, 1924', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie'", 7, r"CHRONICLE"),
    ("in the Chronicle, a letter of Evdokim's synod to the Metropolitan Anthony of Kiev, September 12, 1923, and Anthony's answer", 520, r"OF THE RUSSIAN ORTHODOX CHURCH. PRESIDENT"),
    ("in the Chronicle, on Patriarch Tikhon", 984, r"PATRIARCH TIKHON"),
    ("Bishop Gore, 'Papal Rome and the Orthodox East'", 1234, r"PAPAL ROME"),
    ("Jules Scriban, 'La Réunion des Églises en Roumanie', in French", 1654, r"REUNION DES EGLISES"),
    ("'The War against Religion in Georgia'", 1784, r"WAR AGAINST RELIGION"),
    ("W. S. Hunt, on relations between the Anglican and the Syrian churches of South India", 1953, r"RELATIONS BETWEEN THE ANGLICAN"),
    ("'The Anglo-Catholic Pilgrimage'", 2246, r"ANGLO-CATHOLIC PILGRIMAGE"),
    ("'American Letter'", 2526, r"AMERICAN LETTER"),
    ("'Athens Letter'", 2860, r"ATHENS LETTER"),
    ("'Our Bookshelf'", 3132, r"OUR BOOKSHELF"),
    ("'A Dedication Service'", 3857, r"DEDICATION SERVICE")],
   (3857, r"DEDICATION SERVICE", "The report of the dedication service seems to break off before the junk lines that end the file."),
   [("anthony-of-kiev-answer-to-evdokim-1923", "Anthony, Metropolitan of Kiev, answer to the Metropolitan Evdokim (1923)", 596, r"following answer was sent", 678, r"Metropolitan of Kiev",
     [EMI], "tradition", "eng", (1923, 1923), "it answers a letter dated September 12th, 1923 (OCR lines 520-521); the answer's own date was not found",
     "His own answer to the synod that had replaced the Patriarch's administration, in English; the print names no translator. Evdokim's letter stands before it at OCR lines 520-594.")])

ce("1924-09_5_3", 5, 3, "September, 1924", 1924, (55, r"SEPTEMBER, 1924"), "cover: 'September, 1924', read on the page image, leaf n0; masthead at OCR line 55", True, CV + CLEAN,
   [("G. Napier Whittingham, 'The Anglo-Catholic Pilgrimage to Palestine', with addresses of welcome from Eastern prelates and a reply of Photios, Patriarch of Alexandria, dated 10th May, 1924 (2437-2497)", 61, r"ANGLO-CATHOLIC PILGRIMAGE"),
    ("Professor Nicholas Glubokovsky, 'The Modern Papacy and the Reunion of the Orthodox East with the Roman Catholic West'", 2518, r"MODERN PAPACY"),
    ("W. S. Hunt, on relations between the Anglican and the Syrian churches", 3150, r"RELATIONS BETWEEN THE ANGLICAN"),
    ("'Our Bookshelf'", 3636, r"OUR BOOKSHELF"),
    ("'Chronicle and Causerie'", 3775, r"CHRONICLE"),
    ("'Church Questions in Hellas'", 4158, r"CHURCH QUESTIONS IN HELLAS")],
   (4158, r"CHURCH QUESTIONS", "The last article runs to about 4400; an advertisement leaf follows."),
   [])

ce("1924-12_5_4", 5, 4, "December, 1924", 1924, (128, r"DECEMBER, 1924"), "cover: 'December, 1924', read on the page image, leaf n0; masthead at OCR line 128", True, CV + CLEAN + " The French is clean.",
   [("J. H. Greig, Bishop of Gibraltar, 'Some Notes on the Position in Serbia'", 134, r"POSITION IN.? SERBIA"),
    ("'Chronicle and Causerie'", 634, r"CHRONICLE"),
    ("'Papal Rome and the Orthodox East', Professor Glubokovsky's criticism of Mgr. Batiffol, signed at 1881", 962, r"PAPAL ROME"),
    ("'Mgr. Pierre Batiffol's Rejoinder', in French", 1918, r"REJOINDER"),
    ("on an autograph of St. Athanasius", 3268, r"AUTOGRAPH"),
    ("'Athens Revisited', signed E. Kephala", 3381, r"ATHENS REVISITED")],
   (3895, r"warm welcome", "The text ends at 3895; advertisement leaves follow."),
   [])

ce("1925-03_6_1", 6, 1, "March, 1925", 1925, (55, r"MARCH, 1925"), "cover: 'March, 1925', read on the page image, leaf n0; masthead at OCR line 55", True, CV + CLEAN,
   [("'Designation and Consecration of a Russian Bishop', by a Russian Berlin correspondent", 61, r"CONSECRATION|DESIGNATION"),
    ("John A. Douglas, 'The Oecumenical Patriarchate'", 244, r"PATRIARCHATE"),
    ("'Chronicle and Causerie'", 2340, r"CHRONICLE"),
    ("Professor Hamilcar Alivisatos, 'Administrative Reform in the Orthodox Church of Greece'", 2831, r"ADMINISTRATIVE REFORM"),
    ("'Remember Russia'", 3418, r"REMEMBER RUSSIA")],
   (3469, r"dumbly patient", "'Remember Russia' stops at 3469 and seems cut off; advertisements follow."),
   [("alivisatos-administrative-reform-in-the-orthodox-church-of-greece-1925", "Hamilcar Alivisatos, 'Administrative Reform in the Orthodox Church of Greece' (1925)", 2831, r"ADMINISTRATIVE REFORM", 3417, r"REMEMBER RUSSIA",
     [GRK], "tradition", "eng", (1925, 1925), "printed in the number of March, 1925",
     "An Athens professor's account of the Greek church laws of 1923, with summaries of the laws.")])

ce("1925-06_6_2", 6, 2, "June, 1925", 1925, (64, r"JUNE, 1925"), "cover: 'June, 1925', read on the page image, leaf n0; masthead at OCR line 64", True, CV + CLEAN,
   [("'The Council of Nicaea, A.D. 325'", 70, r"COUNCIL OF NIC"),
    ("'Nicaea, the City of the Creed'", 1231, r"CITY OF THE CREED"),
    ("'Tikhon, Patriarch of Russia'", 1731, r"TIKHON"),
    ("a panegyric upon the Patriarch Tikhon delivered by J. A. Douglas, April 24th, 1925", 2130, r"PANEGYRIC"),
    ("'The Present Danger to the Oecumenical Patriarchate'", 2466, r"PRESENT DANGER"),
    ("'Historical Scholarship and the Reunion of Christendom'", 2914, r"HISTORICAL SCHOLARSHIP"),
    ("'Metropolitan Michael: the Greatest Serbian Prelate'", 3502, r"METROPOLITAN MICHAEL"),
    ("'The Phenomenal Renewal of Eikons in Russia', with a translated letter from Kiev", 3662, r"RENEWAL OF EIKONS|PHENOMENAL"),
    ("the Anglo-Catholic pilgrims' addresses to the Eastern patriarchs", 4243, r"PILGRIMAGE")],
   (5086, r"larger circulation", "The text ends near 5100; advertisement leaves follow from 5132."),
   [])

ce("1925-09_6_3", 6, 3, "September, 1925", 1925, (86, r"SEPTEMBER, 1925"), "cover: 'September, 1925', read on the page image, leaf n0; masthead at OCR line 86", True, CV + CLEAN,
   [("'The Nicaean Commemoration'", 92, r"COMMEMORATION"),
    ("'Eirenikon from the Oecumenical Patriarch to the Archbishop of Canterbury', with the Archbishop's reply at 293-360", 186, r"EIRENIKON"),
    ("G. Napier Whittingham, an official account of the second Anglo-Catholic pilgrimage", 363, r"OFFICIAL ACCOUNT"),
    ("Madame Alexeiev, 'The Grand Duchess Elizabeth Theodorovna of Russia'", 4585, r"GRAND DUCHESS"),
    ("W. K. Lowther Clarke, 'Literature Work in the Near East'", 4831, r"LITERATURE WORK"),
    ("'The Russian White Cross Society and Mother Eugenia'", 4967, r"WHITE CROSS"),
    ("'Chronicle and Causerie'", 5654, r"CHRONICLE")],
   (6159, r"note with satisfaction", "The Chronicle stops at 6159; advertisements follow from 6184."),
   [("basil-iii-of-constantinople-eirenikon-to-the-archbishop-of-canterbury-1925", "Basil III, Patriarch of Constantinople, eirenikon to the Archbishop of Canterbury (1925)", 186, r"EIRENIKON", 290, r"July, 1925",
     [GRK], "tradition", "eng", (1925, 1925), "signed 'Basil of Constantinople' and dated 22nd July, 1925 (OCR lines 289-290)",
     "The Patriarch's own letter in English; the print names no translator.")])

ce("1926-01_6_4", 6, 4, "January, 1926", 1926, (73, r"JANUARY, 1926"), "cover: 'January, 1926', read on the page image, leaf n0; masthead at OCR line 73", True, CV + CLEAN + " The Latin is clean.",
   [("on the anniversary of the Anglican and Eastern Churches Association", 79, r"ANNIVERSARY"),
    ("'The Princess's Speech', the speech of Lady Surma d'Bait Mar Shimun in Syriac as interpreted by Fr. Heazell", 233, r"PRINCESS"),
    ("a sermon on the Council of Nicaea", 351, r"COUNCIL OF NIC"),
    ("'East and West', a sermon", 619, r"EAST AND WEST"),
    ("H. Harold Buxton, 'The Armenian Church'", 921, r"ARMENIAN CHURCH"),
    ("E. Kephala, 'The Saint of Corfu'", 1318, r"SAINT OF CORFU"),
    ("C. B. Moss, on the Old Catholic churches", 1688, r"OLD CATHOLIC"),
    ("'Old Catholic Documents', with the Archbishop of Utrecht's Latin letter to the Archbishop of Canterbury, 1925", 1802, r"OLD CATHOLIC DOCUMENTS"),
    ("in the Chronicle, a rescript of the Episcopal Synod of the Russian Church outside of Russia to Athelstan Riley, 11/24th October, 1925", 2311, r"RESCRIPT|Synod"),
    ("'Our Bookshelf'", 2462, r"OUR BOOKSHELF"),
    ("'The Alexandrian Election'", 3009, r"ALEXANDRIAN ELECTION")],
   (3505, r"Anglicans", "The text ends at 3505; an advertisement leaf follows."),
   [("russian-synod-abroad-rescript-to-athelstan-riley-1925", "The Episcopal Synod of the Russian Church outside of Russia, rescript to Athelstan Riley (1925)", 2311, r"RESCRIPT|Synod", 2348, r"MAKHAROBLIDZE",
     [EMI], "tradition", "eng", (1925, 1925), "dated 'Serbia, 11/24th October, 1925. No. 3304.' (OCR line 2340)",
     "The synod's own rescript over the Metropolitan Anthony's name, in English; the print names no translator."),
    ("surma-speech-at-the-anniversary-1925", "Lady Surma d'Bait Mar Shimun, speech at the Association's anniversary (1925)", 233, r"PRINCESS", 350, r"COUNCIL OF NIC",
     [SAYFO], "tradition", "eng", (1925, 1926), "the anniversary is reported in the number of January, 1926",
     "Her speech as the journal prints it in English; it says she spoke in Syriac and was interpreted by Fr. Heazell (OCR lines 234-235).")])
ce("1926-04_7_1", 7, 1, "April, 1926", 1926, (277, r"APRIL, 1926"), "cover: 'April, 1926', read on the page image, leaf n0; masthead at OCR line 277", True, CV + CLEAN,
   [("a contents leaf for the whole of volume VII", 106, r"VOLUME VII|No\. 1|CONTENTS"),
    ("on the use of ikons and their making", 283, r"IKONS"),
    ("Prof. Bulgakoff, 'Does Orthodoxy Possess an Outward Authority of Dogmatic Infallibility?', translated from the Russian by R. M. French", 909, r"DOES ORTHODOXY POSSESS"),
    ("'A Cruise in Greek Waters'", 1867, r"CRUISE IN GREEK"),
    ("'Chronicle and Causerie', with two letters of the Metropolitan Evlogios dated Paris, 2/15 January, 1926 (2868-2993)", 2321, r"CHRONICLE"),
    ("the third Anglo-Catholic pilgrimage", 3035, r"ANGLO-CATHOLIC PILGRIMAGE"),
    ("'The Assyrian Appeal', with a speech of Lady Surma (3600-3670)", 3369, r"ASSYRIAN APPEAL")],
   (3670, r"Lord.s Prayer in Aramaic", "The text ends at about 3719; scraps of an advertisement leaf follow."),
   [("bulgakoff-does-orthodoxy-possess-an-outward-authority-of-dogmatic-infallibility-1926", "Prof. Bulgakoff, 'Does Orthodoxy Possess an Outward Authority of Dogmatic Infallibility?' (1926)", 909, r"DOES ORTHODOXY POSSESS", 1866, r"CRUISE IN GREEK", 
     [EMI], "tradition", "eng", (1926, 1926), "printed in the number of April, 1926",
     "His article 'translated from the Russian by the Rev. R. M. French' (OCR line 912)."),
    ("evlogios-two-letters-1926", "Evlogios, Metropolitan, two letters from Paris (1926)", 2868, r"Rue Daru", 2993, r"METROPOLITAN",
     [EMI], "tradition", "eng", (1926, 1926), "each is dated Paris, 2/15 January, 1926 (OCR lines 2869 and 2923)",
     "Two letters of thanks, numbered 25 and 27, printed in the Chronicle in English; the print names no translator."),
    ("surma-speech-for-the-assyrian-appeal-1926", "Lady Surma, speech for the Assyrian appeal (1926)", 3600, r"Lady Surma", 3670, r"Lord.s Prayer in Aramaic",
     [SAYFO], "tradition", "eng", (1926, 1926), "printed in the number of April, 1926",
     "Her own speech as the journal prints it in English.")])

ce("1926-06_7_2", 7, 2, "June, 1926", 1926, (318, r"JUNE, 1926"), "cover: 'June, 1926', read on the page image, leaf n0; masthead at OCR line 318", True, CV + CLEAN,
   [("the Bishop of Gloucester, on the Serbian church", 324, r"SERBIA"),
    ("'Chronicle and Causerie'", 754, r"CHRONICLE"),
    ("the official account of the third Anglo-Catholic pilgrimage, with replies of Archbishop Anastassy (1596-1679), Patriarch Damianos of Jerusalem (1967-2008) and Metropolitan Cleopas of Nazareth (2368-2450) in English", 813, r"PILGRIMAGE"),
    ("J. A. Douglas, 'Reservation in the Eastern Orthodox Church'", 3107, r"RESERVATION")],
   (3913, r"Moscow|Ispovedanie", "The text ends at 3913; scraps follow."),
   [])

ce("1926-09_7_3", 7, 3, "September, 1926", 1926, (156, r"SEPTEMBER, 1926"), "cover: 'September, 1926', read on the page image, leaf n0; masthead at OCR line 156", True, CV + CLEAN,
   [("'The Patriarch Meletios' Enthronistic to the Archbishop of Canterbury', a translation, dated Alexandria, 16/29 June, 1926, with the Archbishop's reply", 392, r"ENTHRONISTIC"),
    ("on Bishop Bury's tour", 552, r"BURY|TOUR"),
    ("J. A. Douglas, 'The Old Paths of Nicaea'", 1003, r"OLD PATHS|NIC"),
    ("'The Canonical Position in Russia', documents of the locum tenens Peter of Krutitz and the Metropolitan Sergios, December 1925 and January 1926", 1994, r"CANONICAL POSITION"),
    ("'Chronicle and Causerie'", 2339, r"CHRONICLE"),
    ("Sonia E. Howe, 'The Great Schism in the Russian Church'", 2839, r"GREAT SCHISM"),
    ("'Our Bookshelf'", 3481, r"BOOKSHELF")],
   (3885, r"serve us to go on", "The text ends at 3885; advertisements follow."),
   [("peter-of-krutitsy-and-sergius-documents-on-the-canonical-position-in-russia-1925-26", "Peter of Krutitz, locum tenens, and Sergios, Metropolitan of Novgorod, documents on the canonical position in Russia (1925-26)", 2053, r"PETER OF KRUTITZ", 2332, r"Jan., 1926",
     [RUS, NM], "tradition", "eng", (1925, 1926), "the documents are dated from 23 Nov./6 Dec., 1925 to 1/14 Jan., 1926 (OCR lines 2053-2332)",
     "Their own letters and a draft constitution, in English with no translator named. A notice of a Soviet state body stands among them at about OCR lines 2124-2148.")])

ce("1926-12_7_4", 7, 4, "December, 1926", 1926, (6, r"DECEMBER. 1926"), "masthead: 'December, 1926', OCR line 6", False, CLEAN,
   [("'Orthodox Gift to St. David's Cathedral'", 12, r"ORTHODOX GIFT"),
    ("J. A. Douglas, on the Jerusalem Patriarchate", 116, r"JERUSALEM"),
    ("C. T. Bridgeman, on Syrian Orthodox consecrations", 1270, r"SYRIAN ORTHODOX|CONSECRATION"),
    ("W. A. Wigram, 'Present-Day Problems'", 1435, r"PROBLEMS"),
    ("'Russia and Her Church', a lecture by E. Makharoblidze, Secretary of the Russian Synod of Sremsky-Karlowicz, November 27, 1926", 2024, r"RUSSIA AND HER CHURCH"),
    ("Sonia E. Howe, 'The Great Schism in the Russian Church and the Protopope Avvakum'", 2650, r"GREAT SCHISM")],
   (3453, r"godless form of worship", "The text ends at 3453; a plate caption follows."),
   [("makharoblidze-russia-and-her-church-1926", "E. Makharoblidze, 'Russia and Her Church', a lecture (1926)", 2024, r"RUSSIA AND HER CHURCH", 2647, r"THE CHRISTIAN EAST",
     [EMI], "tradition", "eng", (1926, 1926), "the heading dates the lecture November 27, 1926 (OCR line 2028)",
     "A lecture by the secretary of the Russian synod at Sremsky-Karlowicz. The editors say they 'do not take responsibility for all' he said (OCR lines 2031-2032).")])

ce("1927-03_8_1", 8, 1, "March, 1927", 1927, (1, r"MARCH, 1927"), "masthead: 'March, 1927', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie', with a letter of Seraphim, Archbishop of Uglitch, to the prelates, priests and laity of the Russian church (119-166)", 10, r"CHRONICLE"),
    ("F. H. Marshall, 'Some Debts to Byzantinism'", 433, r"BYZANTINISM"),
    ("G. Maklakoff, 'Orthodoxy and the Living Church'", 1059, r"LIVING CHURCH"),
    ("'My Visit to the Russian Orthodox Academy at Paris', signed V. Korenchevsky", 2225, r"MY VISIT"),
    ("Sonia E. Howe, 'The Great Schism'", 2477, r"GREAT SCHISM"),
    ("'A. and E.C.A. Notes'", 2882, r"E\.C\.A\. NOTES")],
   (2990, r"members of the Association", "The text ends at 2990; a plate caption and scraps follow."),
   [("seraphim-of-uglich-letter-to-the-prelates-priests-and-laity-1927", "Seraphim, Archbishop of Uglitch, letter 'To the Prelates, Priests and Laity of the Orthodox Russian Church'", 119, r"TO THE PRELATES", 166, r"SERAPHIM",
     [RUS, NM], "tradition", "eng", (1926, 1927), "the letter prints no date; it stands in the number of March, 1927",
     "His own letter, in English with no translator named. The Chronicle says the guiding of the Russian church then lay upon him (OCR lines 102-106).")])

ce("1927-06_8_2", 8, 2, "June, 1927", 1927, (1, r"JUNE, 1927"), "masthead: 'June, 1927', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie', with translated letters from Moscow (125-312)", 7, r"CHRONICLE"),
    ("the Metropolitan Anthony, President of the Synod of Karlovtsi, 'Why Anglican Clergy Could be Received in Their Orders'", 875, r"WHY ANGLICAN CLERGY"),
    ("the Archpriest Chernavin, 'A Famous Russian Monastery'", 1457, r"FAMOUS RUSSIAN MONASTERY"),
    ("L. Parressos, 'Protestantism and Orthodoxy'", 2050, r"ANTISM AND ORTHODOXY"),
    ("Euphrosyne Kephala, 'Modern Activities in the Church of Greece'", 2513, r"MODERN ACTIVITIES"),
    ("C. B. Moss, on the place of Constantinople in church history", 2711, r"CONSTANTINOPLE"),
    ("'A. and E.C.A. Notes'", 3256, r"E\.C\.A\. NOTES")],
   (3256, r"NOTES", "The notes and notices run to the end of the file."),
   [("anthony-of-karlovtsi-why-anglican-clergy-could-be-received-in-their-orders-1927", "Anthony, Metropolitan, 'Why Anglican Clergy Could be Received in Their Orders' (1927)", 875, r"WHY ANGLICAN CLERGY", 1440, r"local bishops and the Councils",
     [EMI], "tradition", "eng", (1927, 1927), "printed in the number of June, 1927",
     "His own statement, in English with no translator named; the by-line calls him President of the Synod of Karlovtsi. The OCR leaves a gap of junk lines between its last lines and the next heading.")])
ce("autumn-1927_8_3", 8, 3, "Autumn, 1927", 1927, (102, r"AUTUMN, 1927"), "cover and masthead: 'Autumn, 1927', read on the page images, leaves n0 and n4; masthead at OCR line 102, where the OCR reads the volume as 'VII'", True, CV + CLEAN,
   [("'Chronicle and Causerie', with a letter of the Patriarch Meletios of Alexandria dated March 5-18, 1927 (114-189)", 108, r"CHRONICLE"),
    ("J. A. Douglas, on the World Conference on Faith and Order", 421, r"WORLD CONFERENCE ON FAITH"),
    ("Stephan, Archbishop of Sofia, 'Fundamental Conditions for the Unification of the Christian Churches'", 1816, r"FUNDAMENTAL CONDITIONS"),
    ("Chrysostom, Metropolitan of Athens, 'The Nature of the Church'", 3173, r"NATURE OF THE CHURCH"),
    ("'The Declaration of the Orthodox at Lausanne'", 3683, r"DECLARATION OF THE"),
    ("H. C. Luke, 'The Present Position of the Orthodox Church in Albania'", 3895, r"PRESENT POSITION"),
    ("R. M. French, 'The Children of Russia'", 4074, r"CHILDREN OF RUSSIA"),
    ("letters and speeches of Orthodox prelates to the Anglo-Catholic Congress of 1927", 4652, r"CONGRESS OF 1927"),
    ("'A. and E.C.A. Notes'", 4990, r"E\.C\.A\. NOTES")],
   (5200, r"Pepler", "The book notices end at 5200; scraps follow."),
   [("stephan-of-sofia-fundamental-conditions-for-the-unification-of-the-christian-churches-1927", "Stephan, Archbishop of Sofia, 'Fundamental Conditions for the Unification of the Christian Churches' (1927)", 1816, r"FUNDAMENTAL CONDITIONS", 3170, r"justice and love",
     [BALK], "tradition", "eng", (1927, 1927), "printed in the number of Autumn, 1927",
     "A Bulgarian archbishop's own paper, in English with no translator named."),
    ("chrysostom-of-athens-the-nature-of-the-church-1927", "Chrysostom, Metropolitan of Athens, 'The Nature of the Church' (1927)", 3173, r"NATURE OF THE CHURCH", 3680, r"DECLARATION OF ORTHODOX",
     [GRK], "tradition", "eng", (1927, 1927), "printed in the number of Autumn, 1927",
     "His own paper, in English with no translator named."),
    ("declaration-of-the-orthodox-at-lausanne-1927", "The Declaration of the Orthodox delegates at the Lausanne Conference on Faith and Order (1927)", 3683, r"DECLARATION OF THE", 3866, r"different Faiths",
     [GRK], "tradition", "eng", (1927, 1927), "the editors' note: read to the conference by the Archbishop of Thyatira on Thursday, August 18 (OCR lines 3687-3690)",
     "The delegates' joint statement; the note says all the Orthodox delegates signed it."),
    ("declaration-of-the-orthodox-at-lausanne-1927-ecumenical", "The Declaration of the Orthodox delegates at the Lausanne Conference on Faith and Order (1927): for the ecumenical movement", 3683, r"DECLARATION OF THE", 3866, r"different Faiths",
     [ECU], "context", "eng", (1927, 1927), "the editors' note: read to the conference by the Archbishop of Thyatira on Thursday, August 18 (OCR lines 3687-3690)",
     "The Orthodox delegates' statement of what they could and could not accept at the conference.")])

ce("spring-1928_9_1", 9, 1, "Spring, 1928", 1928, (1, r"SPRING, 1928"), "masthead: 'Spring, 1928', OCR line 1, where the volume and number are garbled", False, CLEAN,
   [("'Chronicle and Causerie'", 10, r"CHRONICLE"),
    ("the Metropolitan of Thyatira, 'The Orthodox Delegation at Lausanne and its Declaration'", 673, r"ORTHODOX DELEGATION AT LAUSANNE"),
    ("J. A. Douglas, 'Economy and the Communion at Belgrad'", 1322, r"ECONOMY AND THE COMMUNION"),
    ("'The New Hearth in Russian Monasticism'", 2019, r"RUSSIAN MONASTICISM|NEW HEARTH"),
    ("C. G. Harrison, 'Re-union and the Holy See'", 2343, r"HOLY SEE"),
    ("Sonia E. Howe, 'The Role of the Russian Church during the Mongol Period'", 3053, r"MONGOL PERIOD|ROLE OF THE RUSSIAN"),
    ("'Our Bookshelf'", 3465, r"BOOKSHELF"),
    ("'A. and E.C.A. Notes'", 4118, r"A\. & ECA")],
   (4199, r"few words.at the close", "The file ends within the notes."),
   [("germanos-of-thyatira-the-orthodox-delegation-at-lausanne-and-its-declaration-1928", "The Metropolitan of Thyatira, 'The Orthodox Delegation at Lausanne and its Declaration' (1928)", 673, r"ORTHODOX DELEGATION AT LAUSANNE", 1319, r"THE CHRISTIAN EAST",
     [GRK], "tradition", "eng", (1928, 1928), "printed in the number of Spring, 1928",
     "His own defense of the Orthodox declaration at Lausanne. The declaration itself is in the number of Autumn, 1927. The last lines before the next article are garbled.")])

ce("summer-1928_9_2", 9, 2, "Summer, 1928", 1928, (1, r"SUMMER"), "masthead: 'Summer, 1928', read on the page image, leaf n0; the OCR at line 1 loses the year", False, CLEAN + " The first hundred lines or so are badly garbled.",
   [("'Chronicle and Causerie', with letters between the Archbishop of Canterbury and the Patriarch Meletios of Alexandria, February and March 1928", 7, r"CHRONICLE"),
    ("on the consecration of the holy chrism at Constantinople, translated from Orthodoxia", 523, r"CHRISM"),
    ("extracts from the Soviet press on the Easter campaign of 1928, from about 871", 875, r"EASTER"),
    ("Prof. N. Arsentiev, 'Russian Types of Devotion'", 2127, r"RUSSIAN TYPES"),
    ("Nikolai, Bishop of Okhrida, 'The Sacraments from the Point of View of the Eastern Church'", 2482, r"SACRAMENTS FROM"),
    ("Athelstan Riley, 'A Visit to Jerusalem'", 2728, r"VISIT TO JERUSALEM"),
    ("Sonia E. Howe, 'The Role of the Russian Church during the Mongol Period'", 2957, r"MONGOL|ROLE OF THE RUSSIAN"),
    ("Euphrosyne Kephala, 'The Church of Corinth and its Bishop during the Earthquake'", 3187, r"CHURCH OF CORINTH"),
    ("'Our Bookshelf'", 3387, r"BOOKSHELF")],
   (3693, r"R\.M\.F", "The book notices end at 3693, signed R.M.F.; scan debris follows."),
   [("nikolai-of-okhrida-the-sacraments-from-the-point-of-view-of-the-eastern-church-1928", "Nikolai, Bishop of Okhrida, 'The Sacraments from the Point of View of the Eastern Church' (1928)", 2482, r"SACRAMENTS FROM", 2725, r"penitent children of God",
     [BALK], "tradition", "eng", (1928, 1928), "printed in the number of Summer, 1928",
     "A Serbian bishop's own paper, in English with no translator named.")])

ce("autumn-1928_9_3", 9, 3, "Autumn, 1928", 1928, (1, r"AUTUMN, 1928"), "masthead: 'Autumn, 1928', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie'", 7, r"CHRONICLE"),
    ("Mother Edith, 'An Ancient Church and a New Venture'", 500, r"ANCIENT CHURCH"),
    ("'The Influence of the Church on Russian Culture', a speech of A. Kartashev at the Sorbonne, translated by L. Patterson", 960, r"INFLUENCE OF THE CHURCH"),
    ("Prof. S. Bulgakov, 'The Papal Encyclical and the Lausanne Conference'", 1505, r"PAPAL ENCYCLICAL"),
    ("Prof. Hamilcar Alivisatos, 'Roma Locuta Est'", 2349, r"ROMA LOCUTA"),
    ("N. von Arsentev, on the Slavophil doctrine of the church", 2638, r"SLAVOPHIL"),
    ("'Prayer'", 3130, r"PRAYER"),
    ("'A. and E.C.A. Notes'", 3660, r"E\.C\.A\. NOTES")],
   (3884, r"earthquake at Corinth", "The text ends at 3884."),
   [("kartashev-the-influence-of-the-church-on-russian-culture-1928", "A. Kartashev, 'The Influence of the Church on Russian Culture' (1928)", 960, r"INFLUENCE OF THE CHURCH", 1502, r"blaze of light", 
     [EMI], "tradition", "eng", (1928, 1928), "printed in the number of Autumn, 1928",
     "The footnote calls it the substance of a speech at the Sorbonne, 'Translated by L. Patterson, D.D.' (OCR lines 1011-1012)."),
    ("bulgakov-the-papal-encyclical-and-the-lausanne-conference-1928", "S. Bulgakov, 'The Papal Encyclical and the Lausanne Conference' (1928)", 1505, r"PAPAL ENCYCLICAL", 2346, r"Mariology",
     [EMI], "tradition", "eng", (1928, 1928), "printed in the number of Autumn, 1928",
     "His own article, in English with no translator named.")])

ce("winter-1928_9_4", 9, 4, "Winter, 1928", 1928, (1, r"WINTER, 1928"), "masthead: 'Winter, 1928', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie', with an address of the Greek Orthodox community in London to the Archbishop of Canterbury (from 109)", 7, r"CHRONICLE"),
    ("Kenneth Mackenzie, 'The Orthodox Mind and Re-union'", 610, r"ORTHODOX MIND"),
    ("'Holiday Impressions in the Near East'", 1111, r"HOLIDAY IMPRESSIONS"),
    ("C. B. Moss, 'The Place of the Old Catholics in the Work of Unity'", 1924, r"OLD CATHOLICS"),
    ("'Penance', the substance of an article in Glasnik by Milosh Parenta, translated by L. Patterson", 2160, r"PENANCE"),
    ("'A. and E.C.A. Notes'", 2351, r"E\.C\.A\. NOTES")],
   (2351, r"NOTES", "The notes run to about 2630; photograph captions follow."),
   [("parenta-penance-1928", "Milosh Parenta, 'Penance' (1928)", 2160, r"PENANCE", 2345, r"society",
     [BALK], "tradition", "eng", (1928, 1928), "the heading: 'an article in Glasnik, October, 1928' (OCR line 2163)",
     "The heading calls it 'the substance of an article', translated by L. Patterson; a summary in translation, not the article whole.")])

ce("summer-1929_10_2", 10, 2, "Summer, 1929", 1929, (1, r"SUMMER, 1929"), "masthead: 'Summer, 1929', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie', opening with an account of the Archbishop of Canterbury in Athens taken from Ekklesia of April 20", 7, r"CHRONICLE"),
    ("the Archbishop of Canterbury's enthronistic letter to the Ecumenical Patriarch", 251, r"ENTHRONISTIC|Archbishop"),
    ("'Reply of the Oecumenical Patriarch', translated from Orthodoxia, 30th April, 1929", 310, r"Reply of the"),
    ("the Bishop of Gibraltar, impressions of a first official visit to the Near East", 444, r"IMPRESSIONS|NEAR EAST|GIBRALTAR"),
    ("J. A. Douglas, 'The Fifth Anglo-Catholic Pilgrimage'", 786, r"PILGRIMAGE"),
    ("'The Wilderness of Jerusalem'", 1897, r"WILDERNESS"),
    ("C. A. Manning, 'Religion and the Soviets', reprinted from the American Church Monthly", 2370, r"RELIGION AND THE SOVIETS"),
    ("'Our Bookshelf'", 2789, r"BOOKSHELF"),
    ("H. M. Hyatt, 'The Church of Abyssinia'", 3094, r"ABYSSINIA"),
    ("'Jacob's Ladder'", 3424, r"JACOB")],
   (3424, r"JACOB", "The file ends with a frontispiece caption."),
   [("basil-iii-of-constantinople-reply-to-the-archbishop-of-canterbury-1929", "Basil, Patriarch of Constantinople, reply to the Archbishop of Canterbury's enthronistic letter (1929)", 310, r"Reply of the", 411, r"BASIL OF CONSTANTINOPLE",
     [GRK], "tradition", "eng", (1929, 1929), "the heading: 'Translated from Orthodoxia, 30th April, 1929' (OCR line 311)",
     "The Patriarch's own letter, translated by the journal from the Patriarchate's paper.")])

ce("autumn-1929_10_3", 10, 3, "Autumn, 1929", 1929, (1, r"AUTUMN 19.9"), "masthead: 'Autumn 1929', read on the page image, leaf n0; the OCR reads '1949' at line 1", False, CLEAN,
   [("'Chronicle and Causerie', with a letter of the Metropolitan Germanos to the editor of The Church Times (88-224)", 7, r"CHRONICLE"),
    ("Fedotov, 'The Orthodox Church and Her History'", 564, r"ORTHODOX CHURCH AND HER HISTORY"),
    ("'The Wilderness of Jerusalem', continued", 1230, r"WILDERNESS"),
    ("'Religion and the Soviets', concluded", 1532, r"RELIGION AND THE SOVIETS"),
    ("C. F. L. St. George, 'The Development of Russian Ikon-Painting'", 1825, r"IKON"),
    ("'A. and E.C.A. Notes'", 2141, r"E\.C\.A\. NOTES")],
   (2224, r"complete recovery", "The notes end at 2224; a frontispiece caption follows."),
   [("germanos-of-thyatira-letter-to-the-editor-of-the-church-times-1929", "The Metropolitan Germanos, letter to the editor of The Church Times (1929)", 88, r"letter is as follows", 224, r"them\.",
     [GRK], "tradition", "eng", (1929, 1929), "printed in the Chronicle of the number of Autumn, 1929; the letter's own date was not found",
     "His own letter, written to an English paper; it stands inside the Chronicle."),
    ("fedotov-the-orthodox-church-and-her-history-1929", "Fedotov, 'The Orthodox Church and Her History' (1929)", 564, r"ORTHODOX CHURCH AND HER HISTORY", 1227, r"THE CHRISTIAN EAST",
     [EMI], "tradition", "eng", (1929, 1929), "printed in the number of Autumn, 1929",
     "The by-line gives the surname only; in English with no translator named.")])

ce("winter-1929_10_4", 10, 4, "Winter, 1929", 1929, (1, r"WINTER, 1929"), "masthead: 'Winter, 1929', OCR line 1", False, CLEAN,
   [("'Chronicle and Causerie', with an eirenic letter from the new Ecumenical Patriarch to the Archbishop of Canterbury, October, 1929, and the Archbishop's reply", 7, r"CHRONICLE"),
    ("D. J. Chitty, 'The Spirit of Orthodox Christianity'", 384, r"SPIRIT OF ORTHODOX"),
    ("P. B. Anderson, 'The New Law on Religion in Russia'", 1035, r"NEW LAW"),
    ("'The Attitude of the Orthodox Church to the Faith and Order Movement', a speech at the Maloja meeting of the Continuation Committee by a professor whose surname the OCR drops ('Pror. Hamiccar S. D.D.', line 1457)", 1453, r"ATTITUDE OF THE ORTHODOX"),
    ("C. B. Moss, 'An Impression of Valamo'", 1733, r"VALAMO"),
    ("on the ideas of Leo Tolstoi, translated from Naroden Straj by L. Patterson", 1839, r"TOLSTOI"),
    ("'Pannykhida: or Office for the Faithful Departed', in W. J. Birkbeck's translation", 2247, r"PANNYKHIDA"),
    ("'Our Books'", 3029, r"OUR BOOK"),
    ("'A. and E.C.A. Notes'", 3505, r"E\.C\.A\. NOTES")],
   (3632, r"other assemblies also", "The text ends at 3632; advertisement leaves and an appeal follow, with '1930' at 3766 and 3844."),
   [("ecumenical-patriarch-eirenic-letter-to-the-archbishop-of-canterbury-1929", "The Ecumenical Patriarch, eirenic letter to the Archbishop of Canterbury (1929)", 69, r"Eirenic Letter", 146, r"October, 1929",
     [GRK], "tradition", "eng", (1929, 1929), "dated October, 1929 (OCR line 146)",
     "The new Patriarch's own letter, in English with no translator named; the Archbishop's reply at OCR line 151 addresses him as 'the Lord Photios'."),
    ("the-attitude-of-the-orthodox-church-to-the-faith-and-order-movement-1929", "'The Attitude of the Orthodox Church to the Faith and Order Movement', a speech at the Maloja meeting (1929)", 1453, r"ATTITUDE OF THE ORTHODOX", 1730, r"THE CHRISTIAN EAST",
     [GRK], "tradition", "eng", (1929, 1929), "printed in the number of Winter, 1929",
     "A speech by an Orthodox professor at the Maloja meeting of the Continuation Committee; the OCR drops his surname from the by-line (OCR line 1457).")])

ce("autumn-1930_11_3", 11, 3, "Autumn, 1930", 1930, (152, r"AUTUMN, 1930"), "cover: 'Autumn, 1930', read on the page image, leaf n0; masthead at OCR line 152", True, "An advertisement leaf and a photograph caption stand before the masthead. " + CLEAN,
   [("J. A. Douglas, 'The Purport of the Recent Orthodox Delegation'", 158, r"PURPORT"),
    ("Dr. Stefan Zankov, 'The General Position of the Eastern Orthodox Churches at the Present Time'", 2392, r"GENERAL POSITION"),
    ("'The Funeral of the Serbian Patriarch, Dmitri'", 2668, r"FUNERAL OF THE SERBIAN"),
    ("Donald A. Lowrie, 'Russians Confer on Christian Culture'", 2906, r"RUSSIANS CONFER"),
    ("J. A. Douglas, 'The Oecumenical Patriarchate and Nationality'", 3347, r"PATRIARCHATE AND +NATIONALITY")],
   (3684, r"peace of Europe", "The last article ends at 3684; advertisements follow."),
   [("zankov-the-general-position-of-the-eastern-orthodox-churches-1930", "Stefan Zankov, 'The General Position of the Eastern Orthodox Churches at the Present Time' (1930)", 2392, r"GENERAL POSITION", 2665, r"FUNERAL OF THE SERBIAN",
     [BALK], "tradition", "eng", (1930, 1930), "printed in the number of Autumn, 1930",
     "His own article, in English with no translator named.")])
ORD = {3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Tenth", 13: "Thirteenth", 14: "Fourteenth", 15: "Fifteenth", 16: "Sixteenth", 18: "Eighteenth", 19: "Nineteenth"}
IRMOCR = "Clean in the articles; running heads and page numbers sit in the text, the bibliography is telegraphic and noisy, and non-Latin scripts are garbled. The OCR often reads a 3 as an 8 in years."
CHN = "the-chinese-church-indigenous-and-suffering"
PUB = {
    "frowde": "Edinburgh: The International Review of Missions, 1 Charlotte Square; London, Toronto, Melbourne, and Bombay: Henry Frowde, Oxford University Press; New York: Missionary Education Movement (title leaf)",
    "milford-edin": "Edinburgh: The International Review of Missions, 1 Charlotte Square; London, Toronto, Melbourne, and Bombay: Humphrey Milford, Oxford University Press; New York: Missionary Education Movement (title leaf)",
    "victoria": "London: The International Review of Missions, 117 Victoria Street; Humphrey Milford, Oxford University Press; New York City: Committee of Reference and Counsel, 25 Madison Avenue (title leaf)",
    "edinhouse": "London: The International Review of Missions, Edinburgh House, Eaton Gate, Sloane Square; Humphrey Milford, Oxford University Press; New York City: Committee of Reference and Counsel, 25 Madison Avenue (title leaf)",
    "edinhouse419": "London: The International Review of Missions, Edinburgh House, Eaton Gate, Sloane Square; Humphrey Milford, Oxford University Press; New York City: Committee of Reference and Counsel, 419 Fourth Avenue (title leaf)",
}


def irm(year, vol, yl, editor, pub, pubpat, nums, parts, index, endtxt, docs, shelf, wholenote, extra_ocr=""):
    ident = "sim_international-review-of-mission_%d_%d" % (year, vol)
    chk(ident, yl, str(year), 1); chk(ident, yl - 1, "VOLUME THE " + ORD[vol].upper(), 1)
    chk(ident, pubpat[0], pubpat[1], 3)
    for n in nums:
        chk(ident, n, r"INTERNATIONAL|REVIEW OF MISSIONS", 4)
    for t, n, pat in parts:
        chk(ident, n, pat, 4)
    chk(ident, index, r"INDEX", 4)
    title = "The International Review of Missions, Volume the %s (%d)" % (ORD[vol], year)
    stem = "international-review-of-missions_v%d_%d" % (vol, year)
    content = "One whole volume of the quarterly; many writers. Title leaf from OCR line 1, with the year at line %d. The four numbers begin at OCR lines %s (January, April, July, October). Among the contents, by the OCR line of each heading or by-line: %s. The index to the volume begins at %d. %s" % (
        yl, ", ".join(str(n) for n in nums), "; ".join("%s (%d)" % (t, n) for t, n, _ in parts), index, endtxt)
    rows = [row("whole", title, "international-review-of-missions", "whole", [shelf], "tradition", "assigned", "eng",
                doc((year, year), "title leaf: '%d'" % year), wholenote)]
    for slug, work, a, apat, b, bpat, atlas, role, ys, dsrc, note in docs:
        chk(ident, a, apat, 4); chk(ident, b, bpat, 4)
        rows.append(row(slug, work + " (International Review of Missions, %d)" % year, "international-review-of-missions", "OCR lines %d-%d" % (a, b), atlas, role, "assigned", "eng", doc(ys, dsrc), note))
    add(ident, stem + ".txt", title, "The International Review of Missions (many writers); %s (title leaf)" % editor, PUB[pub],
        "%d (title leaf, OCR line %d)" % (year, yl), year, NR, "eng", IRMOCR + extra_ocr, content, "The International Review of Missions", shelf,
        W + "The International Review of Missions, the volumes for 1914-1921, 1924-1927, 1929 and 1930.", rows)


N1 = "A missionary quarterly edited by J. H. Oldham; each article is its writer's own."
N2 = "A missionary quarterly edited by J. H. Oldham. The title leaf says that an article which speaks for the Continuation Committee will say so, and that otherwise the writer alone is responsible."
N3 = "The quarterly the title leaf says 'is published by the International Missionary Council'; each article is its writer's own."

irm(1914, 3, 15, "edited by J. H. Oldham", "frowde", (23, r"FROWDE"), [68, 14144, 27570, 41343],
    [("'A Missionary Survey of the Year 1913'", 75, r"SURVEY OF THE YEAR 1913"),
     ("the fourth meeting of the Continuation Committee, at The Hague", 9346, r"CONTINUATION COMMITTEE|FOURTH MEETING"),
     ("'The C.M.S. and Native Church Organization'", 17222, r"NATIVE CHURCH"),
     ("on co-operation in Madagascar, signed Daniel Couve", 19876, r"MADAGASCAR"),
     ("'Church and Mission in Japan'", 21790, r"JAPAN"),
     ("'The War and Missions'", 41349, r"WAR")],
    53143, "The file ends with the printer's line, Morrison & Gibb, Edinburgh, at 54196. Articles in this volume carry no by-line at their head; the writers are named in the notes on contributors at 10085, 21953, 36019 and 48785.",
    [], SVM, N1)

irm(1915, 4, 15, "edited by J. H. Oldham", "frowde", (23, r"FROWD"), [67, 11377, 23035, 34485],
    [("'A Missionary Survey of the Year 1914'", 71, r"SURVEY OF THE YEAR 1914"),
     ("'Black and White in South Africa'", 11383, r"BLACK AND WHITE"),
     ("on self-support in the church", 16187, r"SELF-SUPPORT"),
     ("on the presentation of Christianity to primitive peoples, in Kavirondo, with 'A Statement by Christian Converts in Kavirondo addressed to their Heathen Friends' at 24773", 24769, r"KAVIRONDO|PRIMITIVE"),
     ("on church and mission", 38131, r"CHURCH AND MISSION")],
    45926, "The index is damaged in the OCR at the end of the file. Articles in this volume carry no by-line at their head; the writers are named in the notes on contributors at 7640, 18693, 29851 and 41647.",
    [], SVM, N1)

irm(1916, 5, 18, "edited by J. H. Oldham", "milford-edin", (25, r"MILFORD"), [88, 11110, 23326, 34795],
    [("'A Missionary Survey of the Year 1915'", 95, r"SURVEY OF THE YEAR 1915"),
     ("Chengting T. Wang, 'The Importance of Making Christianity Indigenous'", 4559, r"INDIGENOUS|WANG"),
     ("a conference with Chinese leaders", 12584, r"CHINESE LEADERS|CONFERENCE"),
     ("on the strategic lines of missions in Africa", 23332, r"AFRICA"),
     ("on the secret of vitality in the Pauline churches", 34798, r"PAULINE")],
    45617, "The file ends with the printer's line at 47053.",
    [], SVM, N2)

irm(1917, 6, 15, "edited by J. H. Oldham", "milford-edin", (22, r"MILFORD"), [73, 10811, 21668, 31000],
    [("'A Missionary Survey of the Year 1916', which at 2835-2843, with a footnote at 2864-2875, tells of the 'prophet' Garrick Sokari Braid of Bakana", 80, r"SURVEY OF THE YEAR 1916"),
     ("Bishop Frank W. Warne, on India's mass movements in the Methodist Episcopal Church", 11797, r"MASS MOVEMENT"),
     ("John Matthai, on the education of Christian students in India", 17706, r"MATTHAI"),
     ("Masumi Hino, 'Recent Movements in Japanese Thought'", 21674, r"HINO|JAPANESE THOUGHT"),
     ("Herbert Anderson, on the national spirit, the Indian church and missions", 24264, r"ANDERSON|INDIAN CHURCH")],
    39637, "The file ends with the printer's line at 40874.",
    [("survey-of-1916-the-prophet-movement-of-garrick-braid", "The survey of the year 1916 on the 'prophet' Garrick Sokari Braid", 2835, r"political character", 2875, r"Church Missionary Review, 1916|Bible i",
      [AIC], "context", (1916, 1917), "the survey of the year 1916, printed in the number of January 1917",
      "A missionary journal's short report, with a footnote that gives the movement 'as presented by the African Bishop Johnson' and cites the Church Missionary Review of 1916. An outside account at second hand. Lines 2848-2863 between the text and the footnote are on Kamerun.")],
    SVM, N2)

irm(1918, 7, 15, "edited by J. H. Oldham", "milford-edin", (22, r"MILFORD"), [74, 9598, 18905, 27805],
    [("'A Missionary Survey of the Year 1917'", 81, r"SURVEY OF THE YEAR 1917"),
     ("on an awakening among the middle classes of South India", 18911, r"SOUTH INDIA|AWAKENING"),
     ("Sydney Cave, 'A Typical Mass Movement'", 29778, r"MASS MOVEMENT"),
     ("Bishop J. J. Willis, 'The Organization of the Anglican Church in Uganda'", 30383, r"ORGANIZATION OF THE"),
     ("on industrial training in Africa", 30947, r"INDUSTRIAL TRAINING")],
    36389, "The file ends with the printer's line.",
    [("willis-the-organization-of-the-anglican-church-in-uganda", "J. J. Willis, 'The Organization of the Anglican Church in Uganda'", 30383, r"ORGANIZATION OF THE", 30946, r"INDUSTRIAL TRAINING",
      [ANG], "tradition", (1918, 1918), "printed in the number of October 1918",
      "The by-line reads 'Bishop J. J. Willis'; his own account of the church's constitution and synod.")],
    SVM, N2)

irm(1919, 8, 15, "edited by J. H. Oldham", "milford-edin", (22, r"MILFORD"), [69, 8951, 17669, 26577],
    [("the January number, on the missionary enterprise and 'the man of 1919'", 266, r"ETERNAL SOURCE|MISSIONS"),
     ("C. H. Bandy, on a North Indian Presbyterian mass movement", 11686, r"MASS +MOVEMENT"),
     ("on the building of the Uganda cathedral", 13345, r"UGANDA"),
     ("on the missionary situation in Congo", 18987, r"CONGO"),
     ("K. T. Paul, 'How Missions Denationalize Indians'", 32311, r"DENATIONALI|PAUL")],
    36469, "The file ends with the printer's line at 37517.",
    [], SVM, N2)

irm(1920, 9, 15, "edited by J. H. Oldham", "victoria", (19, r"VICTORIA STREET"), [77, 10435, 20834, 31211],
    [("the last chapters of 'A Survey of the Effect of the War upon Missions', with movements towards church union at 1824", 83, r"SURVEY OF THE EFFECT"),
     ("'Official Documents relating to Movements towards Church Union': the plan of union of the United Church of Christ in China (7567), the constitution of the Alliance of Missionary Societies in British East Africa (7775) and the South India proposals (8139), with a statement from the Malabar Suffragan and other members of the Mar Thoma Syrian Church (8277)", 7557, r"OFFICIAL DOCUMENTS"),
     ("on the vision of the Indian church", 15420, r"INDIAN CHURCH|VISION"),
     ("W. McCarthy, on Chinese leadership in the Christian church", 24273, r"CHINESE LEADERSHIP|McCARTHY"),
     ("on labour conditions in Africa", 34764, r"AFRICA|LABOUR")],
    41283, "The file ends with the printer's line at 42116.",
    [("mar-thoma-statement-on-church-union-in-south-india-1919", "Statement from the Malabar Suffragan and other members of the Mar Thoma Syrian Church on church union in South India", 8277, r"MALABAR SUFFRAGAN", 8432, r"SEPTEMBER 29",
      [MART], "tradition", (1919, 1920), "it stands among the South India proposals with a statement of the South India United Church of September 29, 1919 (OCR line 8433); printed in the number of January 1920",
      "The Mar Thoma members' own statement, printed whole among the official documents on union."),
     ("plan-of-union-of-the-church-of-christ-in-china", "Plan of union and doctrinal basis for the United Church of Christ in China", 7567, r"PLAN OF UNION", 7774, r"CONSTITUTION OF ALLIANCE",
      [CHN], "context", (1918, 1920), "printed as Appendix A of the official documents in the number of January 1920; the plan's own date was not read",
      "A union plan of mission-founded churches, printed whole; it comes before the entry's window opens.")],
    SVM, N2)

irm(1921, 10, 13, "Editor, J. H. Oldham; Associate Editor, Miss G. A. Gollock", "edinhouse", (17, r"EDINBURGH HOUSE"), [76, 10361, 19728, 29216],
    [("'A Missionary Survey of the Year 1920'", 84, r"SURVEY OF THE YEAR 1920"),
     ("Cripps, 'An Africa of the Africans'", 5632, r"AFRICA OF THE AFRICANS|CRIPPS"),
     ("'Acts and Public Documents', with the text of the Treaty of Sèvres", 6845, r"PUBLIC DOCUMENTS|ACTS"),
     ("Oldham, 'Christian Missions and African Labour'", 11570, r"AFRICAN LABOUR|OLDHAM"),
     ("Eddy, 'The Christian Approach in the Near East'", 15964, r"NEAR EAST|EDDY")],
    36900, "The index here is to the first ten volumes. The file ends with the printer's line at 41274.",
    [], ECU, "A missionary quarterly edited by J. H. Oldham; each article is its writer's own. The volume is of the year the entry opens.")

irm(1924, 13, 13, "edited by J. H. Oldham and G. A. Gollock", "edinhouse", (17, r"EDINBURGH HOUSE"), [71, 11366, 22581, 34054],
    [("Gairdner, 'Islam in Africa'", 78, r"ISLAM"),
     ("Mediwaka, 'Christianity and Nationalism'", 2948, r"NATIONALISM|MEDIWAKA"),
     ("Cumaraswamy, 'The Indian Christian Church and the Spirit of Nationality'", 3407, r"INDIAN CHRISTIAN CHURCH"),
     ("Willoughby, 'Khama'", 4203, r"KHAMA|WILLOUGHBY"),
     ("'The National Christian Council of China', by the Secretaries", 5095, r"NATIONAL CHRISTIAN"),
     ("Macnicol, 'Narayan Vaman Tilak'", 25708, r"TILAK|MACNICOL"),
     ("Anna Kong Mei, 'The Modern Chinese Woman'", 39069, r"CHINESE WOMAN|KONG MEI")],
    44738, "The file ends with the printer's line.",
    [("the-national-christian-council-of-china-by-the-secretaries", "'The National Christian Council of China', by the Secretaries", 5095, r"NATIONAL CHRISTIAN", 5730, r"KRAEMER",
      [CHN], "context", (1924, 1924), "printed in the number of January 1924",
      "The council's secretaries on its first work; the by-line gives no names.")],
    ECU, N3)

irm(1925, 14, 11, "edited by J. H. Oldham and G. A. Gollock", "edinhouse", (15, r"EDINBURGH HOUSE|EATON GATE"), [72, 11398, 22887, 34715],
    [("Williams, on relations with government in education in the British colonies", 84, r"EDUCATION|WILLIAMS|GOVERNMENT"),
     ("Koo, 'Chinese Education and Religious Work amongst Students'", 11410, r"KOO|CHINESE EDUCATION"),
     ("Mathew Thomas, on the development of the rural church in China", 28379, r"THOMAS|RURAL CHURCH"),
     ("Robert E. Speer, 'The Congress on Christian Work in South America'", 35804, r"CONGRESS ON CHRISTIAN WORK"),
     ("Hodgkin, 'The Church in China at the Cross Roads'", 38540, r"HODGKIN|CROSS ROADS"),
     ("the 'Quarterly Notes', the bulletin of the International Missionary Council, bound at the end of each number, the last from 46119", 46119, r"QUARTERLY NOTES|BULLETIN|INTERNATIONAL MISSIONARY")],
    45191, "The file ends with the printer's line at 46802 and junk lines.",
    [("speer-the-congress-on-christian-work-in-south-america", "Robert E. Speer, 'The Congress on Christian Work in South America'", 35804, r"CONGRESS ON CHRISTIAN WORK", 36695, r"AFRICAN EDUCATION",
      [LAP], "context", (1925, 1925), "printed in the number of October 1925; the article says the congress met at Montevideo from March 29 (OCR lines 35811-35812)",
      "A North American mission secretary's report of the Montevideo congress.")],
    ECU, N3)

irm(1926, 15, 13, "edited by J. H. Oldham and G. A. Gollock", "edinhouse", (17, r"EDINBURGH HOUSE"), [87, 11977, 23794, 43452],
    [("de Vargas, on the religious problem in the Chinese renaissance", 100, r"CHINESE RENAISSANCE|VARGAS"),
     ("Gollock, 'Fifteen Years' Growth'", 3473, r"FIFTEEN YEARS|GOLLOCK"),
     ("the July number, on Africa: D. D. T. Jabavu, 'The South African Problem', third paper", 26861, r"SOUTH AFRICAN PROBLEM"),
     ("Willoughby, 'Building the African Church'", 31307, r"AFRICAN CHURCH|WILLOUGHBY"),
     ("C. T. Loram, 'The Separatist Church Movement'", 32800, r"SEPARATIST CHURCH"),
     ("P. H. J. Lerrigo, 'The Ministry of Health and Welfare Work'", 35024, r"MINISTRY OF HEALTH"),
     ("Thompson, on the Melbourne missionary conference of April 1926", 46439, r"MELBOURNE|THOMPSON")],
    54128, "The 'Quarterly Notes' of the International Missionary Council follow the index from 55133.",
    [("loram-the-separatist-church-movement", "C. T. Loram, 'The Separatist Church Movement'", 32800, r"SEPARATIST CHURCH", 33193, r"PHELPS-STOKES",
      [AIC], "context", (1926, 1926), "printed in the number of July 1926",
      "An outside account, from the side of race relations in South Africa, of the churches that left the missions.")],
    ECU, N3)

irm(1927, 16, 13, "Editor, J. H. Oldham; Associate Editor, M. M. Underhill", "edinhouse", (17, r"EDINBURGH HOUSE"), [71, 11486, 23061, 35057],
    [("Oldham, on the Christian mission in Africa as seen at the international conference at Le Zoute", 1322, r"LE ZOUTE|OLDHAM|AFRICA"),
     ("Paton, 'The Indigenous Church'", 2490, r"INDIGENOUS CHURCH|PATON"),
     ("Ed. Kriele, 'The Nias Revival: the Story of a Spiritual Awakening'", 5441, r"NIAS REVIVAL"),
     ("A. S. Moore Anderson, 'Chinese Diaspora: the Chinese Church of Malaya'", 6185, r"CHINESE DIASPORA"),
     ("Roland Allen, on the use of the term 'indigenous'", 17529, r"INDIGENOUS|ALLEN"),
     ("Hume, Yui and Bray, 'The Future of Christianity in China'", 23073, r"FUTURE OF CHRISTIANITY|HUME"),
     ("Zwemer, 'The Moslems of South-Eastern Europe'", 35950, r"MOSLEMS|ZWEMER")],
    45765, "The 'Quarterly Notes' follow from 46718; the file ends in index fragments.",
    [("kriele-the-nias-revival", "Ed. Kriele, 'The Nias Revival: the Story of a Spiritual Awakening'", 5441, r"NIAS REVIVAL", 6184, r"CHINESE DIASPORA",
      [INDO], "context", (1927, 1927), "printed in the number of January 1927",
      "A missionary's account of the awakening on Nias.")],
    ECU, N3)

irm(1929, 18, 13, "Editor, William Paton; Associate Editor, M. M. Underhill", "edinhouse419", (22, r"419 FOURTH AVENUE"), [62, 11610, 22976, 34426],
    [("'A Missionary Survey of the Year 1928'", 71, r"SURVEY|YEAR 1928"),
     ("Frimodt-Moller, 'Medical Missions and the Indigenous Churches'", 6204, r"INDIGENOUS CHURCHES|FRIMODT"),
     ("Oomman Philip, on experiments in Indian expression of Christian service", 13159, r"PHILIP|INDIAN EXPRESSION"),
     ("Erasmo Braga, 'Following up the Jerusalem Meeting in Brazil'", 17467, r"JERUSALEM"),
     ("Cairns, on the Christian message in 1910 and in 1928", 22990, r"CHRISTIAN MESSAGE|CAIRNS"),
     ("K. T. Paul", 28639, r"PAUL"),
     ("the Bishop of Dornakal, 'Living Forces behind Mass Movements'", 35978, r"LIVING FORCES"),
     ("Michio Kozaki, 'Dr Kagawa and the Kingdom of God Movement'", 39616, r"KAGAWA")],
    44243, "The 'Quarterly Notes' follow from 45476; the file ends with an errata leaf in garbled lines. A leaf on the illness of King George V stands in the title leaves.",
    [("braga-following-up-the-jerusalem-meeting-in-brazil", "Erasmo Braga, 'Following up the Jerusalem Meeting in Brazil'", 17467, r"JERUSALEM", 17717, r"UNDERHILL",
      [LAP], "tradition", (1929, 1929), "printed in the number of April 1929",
      "A Brazilian Protestant leader's own report; the notes on contributors call him Executive Secretary of the Committee on Co-operation in Brazil (OCR line 20901)."),
     ("bishop-of-dornakal-living-forces-behind-mass-movements", "The Bishop of Dornakal, 'Living Forces behind Mass Movements'", 35978, r"LIVING FORCES", 36472, r"MISSIONARY AND THE RYAT",
      [ANG], "tradition", (1929, 1929), "printed in the number of October 1929",
      "An Anglican bishop in India on the mass movements in his own diocese; the by-line gives his see and not his name."),
     ("kozaki-dr-kagawa-and-the-kingdom-of-god-movement", "Michio Kozaki, 'Dr Kagawa and the Kingdom of God Movement'", 39616, r"KAGAWA", 40255, r"VAUGHAN",
      [JAP], "tradition", (1929, 1929), "printed in the number of October 1929",
      "A Japanese writer on Kagawa and the Kingdom of God Movement in Japan.")],
    ECU, N3)

irm(1930, 19, 13, "Editor, William Paton; Associate Editor, M. M. Underhill", "edinhouse419", (22, r"FOURTH AVENUE"), [73, 10941, 22336, 33820],
    [("'A Survey of the Year 1929'", 77, r"SURVEY OF THE YEAR 1929"),
     ("Lootfy Levonian, 'The Criticism of Religion in Islam'", 4811, r"LEVONIAN|ISLAM"),
     ("Inman, 'Young Churches in Old Lands'", 5766, r"YOUNG CHURCHES|INMAN"),
     ("S. K. Datta, 'Inter-racial Relationships in the Far East'", 26879, r"DATTA|INTER-RACIAL"),
     ("Latourette, 'Lands of the Younger Churches'", 39033, r"YOUNGER CHURCHES|LATOURETTE")],
    43757, "The 'Quarterly Notes' follow from 44853 and speak of plans for 1931 (44895, 45144, 45461); the file ends in index fragments.",
    [], ECU, N3)
for f in FAILS:
    print("ANCHOR FAIL", f)
assert not FAILS
json.dump(items, open(S + "work/spec300.json", "w"), ensure_ascii=False, indent=1)
print(len(items), "items", sum(len(i["rows"]) for i in items), "rows", NCHK[0], "anchors")
names = set()
for it in items:
    assert len(it["filename"]) < 120 and it["filename"].endswith(".txt"), it["filename"]
    assert it["filename"] not in names; names.add(it["filename"])
    slugs = [r["slug"] for r in it["rows"]]
    assert len(slugs) == len(set(slugs)), slugs
    for k in ("title", "creator", "publisher", "pubdate", "rights", "ocr", "content"):
        assert "\n" not in it[k]
