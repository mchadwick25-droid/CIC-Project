import json, re, sys, glob

S = sys.argv[1].rstrip("/") + "/"
NR = "the archive.org record carries no rights field, so the imprint date is the basis"
PDM = "the archive.org record carries the Public Domain Mark"
NIC = "the archive.org record is tagged NOT_IN_COPYRIGHT"
A12 = "; add 12 to OCR line numbers"
items = []
_cache = {}
FAILS = []


def lines(ident):
    if ident not in _cache:
        (p,) = glob.glob(S + "b299/dl/" + ident + "__*_djvu.txt")
        _cache[ident] = (p, open(p, encoding="utf-8", errors="replace").read().split("\n"))
    return _cache[ident]


def chk(ident, n, pat, span=1):
    """The host line n (1-based), or a neighbor within span, must match pat."""
    ls = lines(ident)[1]
    win = " ".join(re.sub(r"\s+", " ", x) for x in ls[max(0, n - 1 - span): n + span])
    if not re.search(pat, win, re.I):
        FAILS.append((ident, n, pat, win[:260]))


def pd(y, extra):
    return "Public Domain (pd-us-by-date: published %s); %s" % (y, extra)


def row(slug, work, author, locus, atlas, role, conf, lang, date, note, voice_of=None):
    r = dict(slug=slug, work=work, author=author, locus=locus + A12, atlas_ids=atlas, role=role, confidence=conf, language=lang, date=date, note=note)
    if voice_of:
        r["voice_of"] = voice_of
    return r


def doc(y, src):
    return dict(start=y[0], end=y[1], source=src, fc="Documented")


def add(ident, filename, title, creator, publisher, pubdate, year, extra, lang, ocr, content, seed_author, world, want, rows, rights=None, rights_short=None, ruled=None):
    p = lines(ident)[0]
    it = dict(src=p, filename=filename, title=title, creator=creator, publisher=publisher, pubdate=pubdate,
              rights=rights or pd(year, extra), rights_short=rights_short or ("published %s, out of US copyright by date" % year), lang=lang, item=ident,
              djvu_name=p.split("__", 1)[1], ocr=ocr, content=content, seed_title=title, seed_author=seed_author, year=str(year), world=world,
              why=want, contents_note=content, want=want, rows=rows)
    if ruled:
        it["authors_ruled"] = {k: dict(kind=v[0], evidence=v[1]) for k, v in ruled.items()}
    items.append(it)


IRV = "catholic-apostolic-church-irvingites"
VICT = "victorian-church-of-england"
RC19 = "catholic-church-long-nineteenth-century"
OXF = "the-oxford-movement-and-anglo-catholic-revival"
UNI = "american-unitarianism-universalism-consolidations"
CHR = "christadelphians"
PB = "plymouth-brethren-and-dispensational-formation"
RESC = "the-rescue-mission-movement"
SVM = "the-student-volunteer-movement-and-edinburgh-191"
MOR = "moravian-church-after-1815"
LDS = "latter-day-saints-lds"
SAF = "southern-african-mission-churches"
W = "Era 9 batch 2b, located and not yet taken: "

# ---------------- Dialogues on Prophecy and the Morning Watch ----------------
I = "dialogues-on-prophecy"
chk(I, 55, r"MDCCC\s+XXVIII"); chk(I, 339, r"EIGHTH", 3); chk(I, 11170, r"THIRTEENTH"); chk(I, 14321, r"END\s+OF\s+VOL")
add(I, "dialogues-on-prophecy_v2_1828.txt",
    "Dialogues on Prophecy; vol. II",
    "The title page names no author",
    "London: James Nisbet, Berners Street (title page)",
    "1828 (title page: 'MDCCC XXVIII.', OCR line 55; the OCR reads the volume number as 'VOL, IIl.', and the running heads and the end line read 'Vol. II.')", 1828,
    "the archive.org item is a reader's upload of three Google scans with no rights field or library catalog record, and the imprint date is the basis", "eng",
    "clean prose; the cover leaves and the last page are junk, and running heads sit in the text. Google's reproduction notice stands at OCR lines 1-9, its stamp at 34, 37 and 14337.",
    "The second of three volumes. Title page at OCR lines 40-55. Preface, headed 'Extract from a MS.' and unsigned, at 58-329. Conversation the Eighth, on the order of events at the Second Coming, at 339; the Ninth, on Armageddon, at 3058; the Tenth, on the restoration of the two and ten tribes, at 5631; the Eleventh, on the time-state of the church, at 8234; the Twelfth, on types of the God-man, at 10547; the Thirteenth, on practical duties, at 11170. 'End of Vol. II.' at 14321; the printer's line, L. Dennett, Leather Lane, at 14324. The speakers have Greek names (Aristo, Crito, Theologus, Philalethes).",
    "anonymous", IRV,
    W + "wanted row 257, Dialogues on Prophecy, the later volumes (vol. 1 is held).",
    [row("dialogues-on-prophecy-v2", "Dialogues on Prophecy, vol. II: conversations 8-13 (1828)", "dialogues-on-prophecy",
         "the conversations at OCR lines 339-14321; the preface at 58-329", [IRV], "antecedent", "provisional", "eng",
         doc((1828, 1828), "title page: 'MDCCC XXVIII.'"),
         "Conversations on unfulfilled prophecy among speakers under Greek names. The volume names no author and no place of meeting.")])

I = "10410364bsb"
chk(I, 39, r"XXIX"); chk(I, 32, r"VOL,?\s+III"); chk(I, 1519, r"THIRTEENTH"); chk(I, 5743, r"FOURTEENTH"); chk(I, 18438, r"EIGHTEENTH"); chk(I, 1513, r"1829")
add(I, "dialogues-on-prophecy_v3_1829.txt",
    "Dialogues on Prophecy; vol. III",
    "The title page names no author",
    "London: James Nisbet, Berners Street (title page)",
    "1829 (title page: 'M. DCCC, XXIX,', OCR line 39; the word 'Dialogues' is lost from the OCR's title lines)", 1829, NR, "eng",
    "clean prose; the title page's ornaments are garbled. The Bavarian State Library's stamp stands at OCR lines 1-9 and its card at 20961-20979.",
    "The third of three volumes. Title page at OCR lines 10-39. Preface at 83-1513, unsigned and dated January 1829; it speaks of friends who began to meet about three years before to study prophecy. Conversation the Thirteenth (so headed here, though vol. II also ends with a Thirteenth) at 1519; the Fourteenth at 5743; the Fifteenth at 7975; the Sixteenth at 12213; the Seventeenth at 17525; the Eighteenth at 18438. 'The End' at about 20927; the printer's line, J. Dennett, Leather Lane, at 20930.",
    "anonymous", IRV,
    W + "wanted row 257, Dialogues on Prophecy, the later volumes (vol. 1 is held).",
    [row("dialogues-on-prophecy-v3", "Dialogues on Prophecy, vol. III: conversations 13-18 (1829)", "dialogues-on-prophecy",
         "the conversations at OCR lines 1519-20927; the preface at 83-1513", [IRV], "antecedent", "provisional", "eng",
         doc((1829, 1829), "title page: 'M. DCCC, XXIX,'; the preface is dated January 1829 (OCR line 1513)"),
         "The last volume of the conversations. The preface says the friends began to meet about three years before.")])

for ident, v, rom, y, fn, tl, ypat, pub, sheet, cont, issues in [
    ("morningwatchorq02hendgoog", 1, "I", 1830, "morning-watch_v1-1829_1830.txt", 102, r"1830",
     "1830 (title page, read on the page image, leaf n8, and at OCR line 102; the title page also prints 'Vol. I.-1829.' at line 87, and the archive.org record says 1829)", "1-46",
     "The four numbers of 1829. Title page at OCR lines 61-102; contents at 115-218. No. I, March 1829, from 229, opening with 'On the Study of Prophecy' at 240; No. II, June 1829, from 7225; No. III, September 1829, from 14868; No. IV, December 1829, from 28925. Among the articles: on the interpretation of the Old Testament prophecies quoted in the New (755, 8069, 17136, 31685); the first resurrection (3436); the doctrine of the apostasy (5441); a review of Irving's Last Days (6273); the human nature of Christ (13052) and its true humanity (23167); a defense of the Athanasian Creed (24511); the interpretation of the Apocalypse (29871); signs of the times (35081). Index to vol. I at 40239-40637; 'End of Vol.' at 40638.",
     "the four numbers at OCR lines 229-40238"),
    ("morningwatchorq01hendgoog", 3, "III", 1831, "morning-watch_v3_1831.txt", 91, r"18",
     "1831 (title page, read on the page image, leaf n8; the OCR reads '18SL' at line 91)", "1-46",
     "The numbers of 1831. Title page at OCR lines 55-91; contents of vol. III at 97-168. The March 1831 number from 170 and the June 1831 number from 13786; the headings of the later numbers were not found. Among the articles: the prophetic aspect of the church (179); a commentary on the seven Apocalyptic epistles (913, 14426); the human nature of Christ (6102); miracles, signs and powers (7504); miraculous powers (11457); Tertullian on the humanity of our Lord (12517); the restoration of the twelve tribes (17801); the gifts of the Holy Ghost (near 26471). The last pages are badly garbled; 'To correspondents' at 28214 ends the file.",
     "the numbers at OCR lines 170-28225")]:
    chk(ident, tl, ypat, 1); chk(ident, 229 if v == 1 else 170, r"MORNING|WATCH|MARCH", 8)
    add(ident, fn,
        "The Morning Watch; or Quarterly Journal on Prophecy, and Theological Review; vol. %s" % rom,
        "The title page names no editor or author",
        "London: published by James Nisbet, Berners Street; printed by Ellerton and Henderson, Gough Square (title page)",
        pub, y, NIC, "eng",
        "mostly clean, with long-s slips" + ("; the last pages are badly garbled" if v == 3 else "") + ". Google's sheet stands at OCR lines %s." % sheet,
        cont, "anonymous", IRV,
        W + "wanted row 257, the Morning Watch, the journal of the Albury circle (two of its volumes).",
        [row("morning-watch-v%d" % v, "The Morning Watch; or Quarterly Journal on Prophecy, vol. %s (%s)" % (rom, "1829" if v == 1 else "1831"), "morning-watch",
             issues, [IRV], "antecedent", "provisional", "eng",
             doc((1829, 1830) if v == 1 else (1831, 1831), "the numbers are headed March to December 1829; title page 1830" if v == 1 else "the numbers are headed March and June 1831; title page 1831"),
             "A quarterly on prophecy and theology, with unsigned articles, reviews and letters to the editor. Articles are by many hands and few are signed.")],
        ruled={"morning-watch": ("anonymous", "The title page (file lines %s) names the journal, its printer and its publisher, and no editor; the articles are unsigned or signed with initials." % ("73-114" if v == 1 else "67-103"))})

# ---------------- Further volumes of held Lives ----------------
for ident, v, rom, y, yl, pre, cont, end, img in [
    ("a614417002ashwuoft", 2, "II", 1881, 55, "the preface at 66-206, signed R. G. Wilberforce, Lavington, March 1881; it says Canon Ashwell died as the first volume went to press",
     "chapter I, 1848-49, at 695; II 1849; III, 1850-52, 3644; IV 5626; V, 1853, 7358; VI, 1854, 10450; VII, 1855, 12155; VIII 13464; IX, 1856, 14162; X, 1857-59, 15164; XI, 1858, 16750; XII, 1859, 18462; XIII, 1860, 19348. 'End of the second volume' at 20706; Murray's list of books follows from 20715", (695, 20706), "n10"),
    ("lifeoftherightre03ashwuoft", 3, "III", 1882, 64, "the preface at 73-165, dated Lavington, October 1882",
     "chapter I at 701; II 2850; III 4205; IV 5346; V 6608; VI 7862; VII 9174; VIII 10785; IX 11703; X 13333; XI 14207; XII 15541; XIII 16214; XIV 17788; XV 19350. Appendices at 20926; index from 21320 to 'The End' at 26825", (701, 20925), "n10")]:
    chk(ident, yl, str(y), 1); chk(ident, end[0], r"CHAPTER", 3)
    add(ident, "wilberforce-reginald_life-of-samuel-wilberforce-v%d_%d.txt" % (v, y),
        "Life of the Right Reverend Samuel Wilberforce, D.D., Lord Bishop of Oxford and afterwards of Winchester, with selections from his diaries and correspondence; in three volumes, vol. %s" % rom,
        "Reginald G. Wilberforce (title page: 'by his son Reginald G. Wilberforce')",
        "London: John Murray, Albemarle Street (title page)",
        "%d (title page, read on the page image, leaf %s, and at OCR line %d%s)" % (y, img, yl, "; the '1880' at line 7 is a library call-number slip" if v == 3 else ""), y, NR if v == 2 else NIC, "eng",
        "clean, with occasional damaged figures; running heads carry garbled page numbers. A University of Toronto slip stands at the %s." % ("end" if v == 2 else "head (OCR lines 1-14) and the end"),
        "Vol. %s of three. Title page at OCR lines %s; %s. A table of the bishops of the English sees follows the preface. Then %s. The bishop's diaries and letters are quoted throughout, with his son's linking narrative. The title page prints 'All rights reserved'." % (rom, "27-57" if v == 2 else "29-67", pre, cont),
        "Reginald G. Wilberforce", VICT,
        W + "wanted row 272, Samuel Wilberforce, the Life with his diaries and letters, vols. 2 and 3 (vol. 1, by Ashwell, is held).",
        [row("wilberforce-reginald-life-of-samuel-wilberforce-v%d" % v, "R. G. Wilberforce, Life of Samuel Wilberforce, vol. %s (%d)" % (rom, y), "wilberforce-reginald",
             "the chapters at OCR lines %d-%d" % end, [VICT], "context", "provisional", "eng",
             doc((y, y), "title page: %d" % y),
             "The bishop's son continues the Life from his father's diaries and letters. The diary and letters are first-hand; the choice and the narrative are the son's.")],
        ruled={"wilberforce-reginald": ("metadata-omission", "The title page reads 'by his son Reginald G. Wilberforce' (file lines %s)." % ("54-56" if v == 2 else "58-60"))})

for ident, v, rom, y, yl, ypat, img, a, b, cont, sheet in [
    ("lifeworkofsevent02hodduoft", 2, "II", 1887, 93, r"1.87", "n10", 370, 22165,
     "Chapters XII to XXII, 1844 to 1855. Title page at OCR lines 64-95; contents at 107-369. Chapter XII, 1844, at 370; XIII 3641; XIV 5438; XV 7977; XVI 8947; XVII 9841; XVIII 11553; XIX 12932; XX 15041; XXI 17100; XXII, 1854-1855, 19124. 'End of Vol. II.' at 22167; Cassell's catalogue follows to the end. No preface or index in this volume.",
     "Library junk stands at OCR lines 1-40."),
    ("india.history.resource.86561", 3, "III", 1886, 87, r"1886", None, 486, 23864,
     "Chapters XXIII to XXXVII, 1856 to 1885. Title page at OCR lines 56-88; contents at 101-467. Chapter XXIII, the inner life, at 486; XXIV 1545; XXV 3958; XXVI 5599; XXVII 7149; XXVIII, Lord Palmerston and church appointments, 8635; XXIX 9560; XXX 10903; XXXI 12035; XXXII 13998; XXXIII 14896; XXXIV 16898; XXXV 18679; XXXVI, word and work, 20987; XXXVII, last years, 22078. Appendix, the institutions represented at the memorial service of 8 October 1885, at 23867; index at 24382-28122; 'The End' at 28123.",
     "An Asiatic Society of Bombay library sheet stands at OCR lines 1-32, with a line saying the scan was made with the Government of Maharashtra's aid, repeated at 28132.")]:
    chk(ident, yl, ypat, 1); chk(ident, a, r"CHAPTER|INNER", 4)
    add(ident, "hodder_life-and-work-of-seventh-earl-of-shaftesbury-v%d_%d.txt" % (v, y),
        "The Life and Work of the Seventh Earl of Shaftesbury, K.G.; vol. %s" % rom,
        "Edwin Hodder (title page)",
        "London, Paris, New York and Melbourne: Cassell & Company, Limited (title page)",
        ("1887 (title page, read on the page image, leaf n10; the OCR reads '1387.' at line 93)" if v == 2 else "1886 (title page, OCR line 87)"), y, NIC if v == 2 else NR, "eng",
        "clean, with minor errors and running heads in the text. " + sheet,
        cont + " Shaftesbury's diary and letters are quoted throughout. The title page prints 'All rights reserved'.",
        "Edwin Hodder", VICT,
        W + "wanted row 271, Lord Shaftesbury, the Life with his diaries, vols. 2 and 3 (vol. 1 is held).",
        [row("hodder-shaftesbury-v%d" % v, "Hodder, The Life and Work of the Seventh Earl of Shaftesbury, vol. %s (%d)" % (rom, y), "hodder",
             "the chapters at OCR lines %d-%d" % (a, b), [VICT], "context", "provisional", "eng",
             doc((y, y), "title page: %d" % y),
             "A Life built on Shaftesbury's diaries, which are quoted at length. The diary entries are first-hand; the frame is Hodder's.")])

I = "lifeoffrederickd02maur"
chk(I, 32, r"1884"); chk(I, 30, r"MAC\s*MILL\s*AN"); chk(I, 459, r"CHAPTER", 3); chk(I, 28586, r"INDEX", 2)
add(I, "maurice-f_life-of-frederick-denison-maurice-v2_1884.txt",
    "The Life of Frederick Denison Maurice, chiefly told in his own letters; edited by his son Frederick Maurice; in two volumes, vol. II",
    "Frederick Maurice (title page: 'edited by his son Frederick Maurice')",
    "Macmillan and Co. (title page; no place is printed)",
    "1884 (title page, OCR line 32)", 1884, NIC, "eng",
    "clean, with small slips. A library stamp stands at OCR lines 1-7 and a library sheet at the end.",
    "The second of two volumes, from the latter half of 1849. Title page at OCR lines 10-32; contents at 41-458. Chapter I at 459; II 2575; III 4941; IV 6511; V 7571; VI 9660; VII 11663; VIII 12983; IX 14112; X 14889; XI 16128; XII 17925; XIII 18909; XIV 20450; XV 21711; XVI 22719; XVII 23514; XVIII 24206; XIX 25213; XX 26010; XXI 27127; XXII 28187. The text ends at 28577; index from 28586; printer's line at 39580. Maurice's letters make up most of the text, with remembrances by others.",
    "Frederick Maurice", VICT,
    W + "wanted row 273, Frederick Denison Maurice, the Life told in his letters, vol. 2 (vol. 1 is held).",
    [row("maurice-f-life-of-f-d-maurice-v2", "F. Maurice, The Life of Frederick Denison Maurice, chiefly told in his own letters, vol. II (1884)", "maurice-f",
         "chapters I-XXII at OCR lines 459-28577", [VICT], "context", "provisional", "eng",
         doc((1884, 1884), "title page: 1884"),
         "His son's Life, made chiefly of Maurice's own letters. The letters are first-hand; the selection and the links are the son's.")])

I = "lifeandtimescar03wardgoog"
chk(I, 107, r"1897"); chk(I, 96, r"VOL\s+II"); chk(I, 186, r"CHAPTER|SEQUEL", 4); chk(I, 28477, r"INDEX", 3)
add(I, "ward-wilfrid_life-and-times-of-cardinal-wiseman-v2_1897.txt",
    "The Life and Times of Cardinal Wiseman; in two volumes, vol. II",
    "Wilfrid Ward (title page)",
    "London, New York and Bombay: Longmans, Green, and Co. (title page)",
    "1897 (title page, OCR line 107)", 1897, NIC, "eng",
    "clean, with running heads in the text. Google's sheet stands at OCR lines 1-41 and library stamps at 44-70 and at the end.",
    "The second of two volumes, chapters XIX to XXXI. Title page at OCR lines 73-109; contents at 118-175. Chapter XIX, the sequel to Wiseman's Appeal, at 186; XX, 1851-54, at 1763; XXI, Fabiola, 3641; XXII 5026; XXIII 6579; XXIV 9194; XXV 11072; XXVI, Ireland in 1858, 12580; XXVII 13993; XXVIII 17370; XXIX 19685; XXX, death and funeral, 22232; XXXI, an epilogue, 23520, ending at 25496. Appendices from 25499, with extracts from a statement by Dr. Errington at 25611-28475; index from 28477; the publisher's catalogue from 31204. Letters of Wiseman, Manning, Errington and others are quoted throughout. The title page prints 'All rights reserved'.",
    "Wilfrid Ward", RC19,
    W + "wanted row 278, Nicholas Wiseman, the Life by Ward, vol. 2 (vol. 1 is held).",
    [row("ward-wiseman-v2", "Ward, The Life and Times of Cardinal Wiseman, vol. II (1897)", "ward-wilfrid",
         "chapters XIX-XXXI at OCR lines 186-25496; the appendices at 25499-28475", [RC19], "context", "provisional", "eng",
         doc((1897, 1897), "title page: 1897"),
         "A Life written thirty years after Wiseman's death, with many of his letters. The letters are first-hand; the account is Ward's.")])

I = "memoirofralphwal02caboiala"
chk(I, 22, r"1895"); chk(I, 25, r"Copyright,?\s+1887"); chk(I, 31, r"EIGHTH"); chk(I, 116, r"CHAPTER|XI", 4); chk(I, 10462, r"APPENDIX", 2)
add(I, "cabot_memoir-of-ralph-waldo-emerson-v2_8th-ed1895.txt",
    "A Memoir of Ralph Waldo Emerson; in two volumes, vol. II; eighth edition",
    "James Elliot Cabot (title page)",
    "Boston and New York: Houghton, Mifflin and Company; The Riverside Press, Cambridge (title page)",
    "1895 (title page, OCR line 22; copyright notice of 1887 at 25-26; 'Eighth edition' at 31)", 1895, NIC, "eng",
    "clean. A University of California library line stands at OCR lines 1-2 and a return slip at the end.",
    "The second of two volumes, chapters XI to XVII. Title page at OCR lines 5-35; contents at 41-115. Chapter XI at 116; XII 1434; XIII 2652; XIV 4159; XV 6255; XVI 8005; XVII 9502; the text ends at 10459. Appendix from 10462: A, Emerson's letter to the Second Church, 22 December 1832, at 10465; B, the correspondence with Ware, 10599; C, his contributions to the Dial, 10807; D, the letter to Van Buren, 10869; E 11081; F, a chronological list of his lectures, 11330. Index from 14741. The title page prints 'All rights reserved'.",
    "James Elliot Cabot", UNI,
    W + "wanted row 261, Ralph Waldo Emerson, Cabot's Memoir, vol. 2 (vol. 1 is held in the printing of 1887; this is the eighth edition of 1895).",
    [row("cabot-memoir-of-emerson-v2", "Cabot, A Memoir of Ralph Waldo Emerson, vol. II (eighth edition, 1895)", "cabot",
         "chapters XI-XVII at OCR lines 116-10459; the appendices at 10462-14740", [UNI], "context", "provisional", "eng",
         doc((1887, 1895), "copyright notice of 1887; this printing's title page reads 1895, eighth edition"),
         "A Memoir with Emerson's letters and journals quoted throughout. Appendices A to E print his own documents, among them the letter of 1832 to the Second Church.")])

# ---------------- Froude's Remains ----------------
FR = [("remainsoflaterev21frou", "pt1-v2", 1838, 58, "n6", "in two volumes, vol. II",
       "London: printed for J. G. & F. Rivington, St. Paul's Church Yard, and Waterloo Place, Pall Mall (title page)", NR,
       "The second volume of the first part: sermons and papers. The title page does not print 'Part the First'; the volumes of 1839 call themselves 'Part the Second'. Title page at OCR lines 27-58; contents at 67-376. Sermons I to XX from 377 to 10860; portions of sermons at 10861-12062. Miscellaneous papers: on the poetry of rude ages, 12063; on mathematics at Oxford, 12840; church architecture, 13236 and 14351; a thought on shortening the Prayer Book, 14885; the antiquity of the existing liturgies, 15185; forms of consecration in the primitive church, 16400. 'The End' at 17740. No preface in this volume.",
       "clean, with small slips and running heads in the text. A Princeton Seminary card stands at OCR lines 1-16 and the Internet Archive's 'Digitized by' notice at 18-24.",
       "the sermons at OCR lines 377-12062; the papers at 12063-17740", "Froude's sermons and papers on the liturgy and church architecture, printed two years after his death by editors who are not named in the volume.", 377, r"SERMON"),
      ("remainsoflaterev12frouuoft", "pt2-v1", 1839, 34, "n8", "part the second; in two volumes, vol. I",
       "Derby: printed by Henry Mozley and Sons, and sold by J. G. & F. Rivington, London (title page)", NIC,
       "Essays and papers. Title page at OCR lines 1-34. The editors' preface, unsigned, at 37-2037; contents at 2054-2077. Essay on Rationalism from 2081 (a note says it was written in Barbados in 1834); a collection of texts, 8314; remarks on state interference in matters spiritual, 9781; remarks on church discipline, 13094; remarks on the grounds of orthodox belief, 14802; on the principles to be observed in interpreting Scripture, 16366; fragments, 17345. The text ends at 18346.",
       "clean English; the Greek is garbled. A University of Toronto slip stands at the end.",
       "the essays and papers at OCR lines 2081-18346; the editors' preface at 37-2037", "Froude's essays on rationalism, church and state, and discipline, with a long unsigned preface by the editors answering the first part's critics.", 2081, r"ESSAY|RATIONALISM"),
      ("a5826854rs02frouuoft", "pt2-v2", 1839, 34, "n6", "part the second; in two volumes, vol. II",
       "Derby: printed by Henry Mozley and Sons, and sold by J. G. & F. Rivington, London (title page)", NIC,
       "One work: the 'History of the Contest between Thomas à Becket, Archbishop of Canterbury, and Henry II., King of England', made chiefly of translated letters. Title page at OCR lines 1-34; the work's title at 37-51. The editors' advertisement at 54-90 says the large type of pages 113-534 and the bracketed notes are not the author's. Contents at 93-190; Froude's preface, from the British Magazine, at 191-392. Chapters I to XXII from 393 to 22559. Appendices at 22560, 23863 and 25015; errata at 26404.",
       "clean, with minor slips.",
       "the History at OCR lines 393-22559; the appendices at 22560-26403", "Froude's history of Becket's quarrel with Henry II, built from the letters. The editors say parts in large type and the bracketed notes are another hand's.", 393, r"CHAPTER")]
for ident, tag, y, yl, img, voltxt, pub, extra, cont, ocr, locus, note, a, apat in FR:
    chk(ident, yl, str(y), 1); chk(ident, a, apat, 6)
    add(ident, "froude_remains-%s_%d.txt" % (tag, y),
        "Remains of the late Reverend Richard Hurrell Froude, M.A., Fellow of Oriel College, Oxford; " + voltxt,
        "Richard Hurrell Froude (title page); the editors are not named",
        pub, "%d (title page, read on the page image, leaf %s, and at OCR line %d)" % (y, img, yl), y, extra, "eng", ocr, cont,
        "Richard Hurrell Froude", OXF,
        W + "wanted row 267, Richard Hurrell Froude, his Remains: the three volumes after part 1, vol. 1, which is held.",
        [row("froude-remains-" + tag, "Froude, Remains, %s (%d)" % (voltxt.replace("; in two volumes,", ","), y), "froude",
             locus, [OXF], "tradition", "provisional", "eng", doc((y, y), "title page: %d" % y), note)])

# ---------------- Drummond, Colenso, Cox ----------------
I = "speechesinparlia02drumuoft"
chk(I, 22, r"1860"); chk(I, 12, r"LO.D\s+LOVAINE"); chk(I, 8972, r"REMARKS|CHURCHES", 30); chk(I, 17325, r"THE\s+END", 2)
add(I, "drummond-henry_speeches-in-parliament-v2_lovaine1860.txt",
    "Speeches in Parliament and Some Miscellaneous Pamphlets of the late Henry Drummond, Esq.; edited by Lord Lovaine; in two volumes, vol. II",
    "Henry Drummond (title page); edited by Lord Lovaine (title page)",
    "London: Bosworth & Harrison, 215 Regent Street (title page)",
    "1860 (title page, OCR line 22)", 1860, NIC, "eng",
    "clean. A University of Toronto slip stands at the end.",
    "The second volume: the pamphlets. Title page at OCR lines 1-32; contents at 35-94. Elementary propositions on the currency from 98; a letter to the King against the repeal of the Test Act (1829) from 2362; a dialogue between a sceptical physician and his patient, 3204; Reform, not a New Constitution (1831), 3902; an address to the people, 5777; on corn, 6655; on a Bank Restriction Bill, 7300; a letter to Thomas Phillips (1840), 7774; remarks on the Churches of Rome and England (1841), 8972; reasons wherefore a clergyman of the Church of England should not become a Roman Catholic, 9891 (its own leaf says 1843, the contents 1842); on government by the Queen, 11365; a letter to Inglis (1845), 15280; reasons for rejecting the claims of Romish priests (1851), 16813; a speech to the West Surrey electors, 16963. 'The End' at 17325; the publisher's list follows. No editor's preface in this volume.",
    "Henry Drummond", IRV,
    W + "wanted row 257, Henry Drummond, his speeches and pamphlets, vol. 2 (vol. 1 is held).",
    [row("drummond-pamphlets-v2", "Drummond, Speeches in Parliament and Some Miscellaneous Pamphlets, vol. II: the pamphlets (ed. Lovaine, 1860)", "drummond-henry",
         "the pamphlets at OCR lines 98-17317; the church pamphlets of 1841-1843 at 8972-11364", [IRV], "tradition", "provisional", "eng",
         doc((1829, 1860), "the pamphlets' own leaves are dated from 1829 to 1853; title page 1860"),
         "Drummond's own pamphlets on currency, reform and the churches, gathered after his death. None is titled as a statement of the Catholic Apostolic Church; the church pamphlets speak of its fourfold ministry in passing.")])

I = "pentateuchandbo01colegoog"
chk(I, 212, r"1863"); chk(I, 205, r"PART\s+III"); chk(I, 2468, r"CHAPTER", 3); chk(I, 2123, r"1863", 2)
add(I, "colenso_pentateuch-and-book-of-joshua-pt3_1863.txt",
    "The Pentateuch and Book of Joshua Critically Examined; part III",
    "John William Colenso, D.D., Bishop of Natal (title page)",
    "London: Longman, Green, Longman, Roberts, & Green (title page)",
    "1863 (title page, OCR line 212)", 1863, NIC, "eng",
    "clean English; the Hebrew is garbled and footnote numbers run into the text. Google's sheet stands at OCR lines 1-47.",
    "Part III only, on the book of Deuteronomy; parts I and II appear only in the publisher's notices at the front. Title page at OCR lines 169-212. Preface at 227-2123, signed J. W. Natal, 3 June 1863, with letters from others quoted in it. Contents at about 2127-2260. 'Part III. The Book of Deuteronomy' at 2452; chapter I at 2468; and on through chapter XXI, the results, at 13429, and XXII, concluding remarks, at 13793. The text ends at 14378; Longman's list of works follows from 14397.",
    "John William Colenso", VICT,
    W + "wanted row 274, John William Colenso, The Pentateuch and Book of Joshua (the list called this scan part 2; its title page prints part III; part I is held and part II was not found).",
    [row("colenso-pentateuch-part-3-deuteronomy", "Colenso, The Pentateuch and Book of Joshua Critically Examined, part III: Deuteronomy (1863)", "colenso",
         "the preface at OCR lines 227-2123; chapters I-XXII at 2468-14378", [VICT], "tradition", "provisional", "eng",
         doc((1863, 1863), "title page: 1863; the preface is signed 3 June 1863 (OCR line 2123)"),
         "The Bishop of Natal's own argument on the date and authorship of Deuteronomy, with a long preface answering his critics.")])

I = "lifeofjohnwillia01coxg"
chk(I, 274, r"RIDGWAY"); chk(I, 271, r"VOL"); chk(I, 715, r"CHAPTER", 3); chk(I, 30890, r"END\s+OF\s+VOL", 2); chk(I, 619, r"1887", 1)
add(I, "cox-george-w_life-of-john-william-colenso-v1_1888.txt",
    "The Life of John William Colenso, D.D., Bishop of Natal; in two volumes, vol. I",
    "Sir George W. Cox, Bart., M.A., Rector of Scrayingham (title page)",
    "London: W. Ridgway (title page, read on the page image)",
    "1888 (title page, read on the page image, leaf n6; the OCR drops the place and the year, between lines 274 and 278; the preface is dated 10 December 1887 at line 619)", 1888, NIC, "eng",
    "clean, with minor slips. Junk from the binding pattern stands at OCR lines 1-249 and from about 31100 to the end.",
    "The first of two volumes. Title page at OCR lines 252-285. Cox's preface at 288-619, dated Scrayingham Rectory, 10 December 1887; contents at 635-714. Chapter I at 715; II 2920; III 3920; IV 6204; V 8023; VI 9832; VII 12466; VIII 14903; IX 18331; X 21312; XI 23286; XII 25939. Appendix A, a letter, at 30174; Appendix B, a list of bishops, at 30628. 'End of Vol. I.' at 30890; a list of Colenso's works follows. Colenso's letters, and letters of Bishop Gray and others, are quoted throughout. The title page prints 'All Rights Reserved'.",
    "George W. Cox", VICT,
    W + "wanted row 274, John William Colenso, the Life by Cox, vol. 1.",
    [row("cox-life-of-colenso-v1", "Cox, The Life of John William Colenso, vol. I (1888)", "cox-george-w",
         "chapters I-XII at OCR lines 715-30173", [VICT, SAF], "context", "provisional", "eng",
         doc((1888, 1888), "title page: 1888 (page image); preface dated 10 December 1887"),
         "A friend's Life, written to defend the bishop, with many of his letters. The letters are first-hand; the argument is Cox's.")],
    ruled={"cox-george-w": ("metadata-omission", "The title page reads 'by the Rev. Sir George W. Cox, Bart., M.A.' (file lines 275-277).")})

# ---------------- The Student Volunteer Movement ----------------
I = "historyofstudent00mott"
chk(I, 48, r"ORIGIN", 2); chk(I, 344, r"DEVELOPMENT", 2); chk(I, 1458, r"1892", 1)
add(I, "mott_history-of-the-student-volunteer-movement_1892.txt",
    "History of the Student Volunteer Movement for Foreign Missions",
    "John R. Mott (title page)",
    "No place or publisher is printed on the title page",
    "1892 (title page, read on the page image, leaf n2; the OCR drops the year from the title lines at 22-38. A list at the end says later numbers of the series are 'ready after December 1, 1892', line 1458)", 1892, NR, "eng",
    "clean; a statistics table is lost.",
    "A pamphlet of 48 pages in five parts. Title lines at OCR lines 4-38. I, Origin, at 48; II, Development, at 344; III, Achievements, at 870, with an endorsement by the Presbyterian board's secretaries, dated New York, 6 November 1890, at 1097-1119; IV, Present status, at 1207; V, Purpose, at 1220. The text ends at 1404. A list of the Student Volunteer Series follows at 1407-1460.",
    "John R. Mott", SVM,
    W + "Mott's history of the Student Volunteer Movement (1892).",
    [row("mott-history-of-the-student-volunteer-movement", "Mott, History of the Student Volunteer Movement for Foreign Missions (1892)", "mott",
         "the five parts at OCR lines 48-1404", [SVM], "tradition", "provisional", "eng",
         doc((1892, 1892), "title page: 1892 (page image); the text speaks of 14 July 1892 at OCR lines 837-838"),
         "The movement's own account of its first six years, from the Mount Hermon conference of 1886, by one of its leaders.")])

I = "pledgeofstudentv00wild"
chk(I, 40, r"1890"); chk(I, 37, r"WILDER"); chk(I, 446, r"Pledge", 3)
add(I, "wilder_pledge-of-the-student-volunteer-movement_1890.txt",
    "The Volunteer Pledge of the Student Volunteer Movement for Foreign Missions (Student Volunteer Series, No. 3)",
    "Robert P. Wilder (title page)",
    "No place or publisher is printed on the title page; a note at the end says the series may be had of Walter J. Clark, New York City",
    "1890 (title page: 'June, 1890.', OCR line 40, where the OCR reads 'Fune')", 1890, NR, "eng",
    "clean, with small errors.",
    "A short pamphlet. Title page at OCR lines 1-51. I, the necessity for a pledge, at 54; II, what shall the pledge be, at 304; III, the meaning of the pledge, at 443, with its wording at 446-448: 'We are willing and desirous, God permitting, to become foreign missionaries'; IV, use of the pledge, at 560; V, who shall use the pledge, at 616. The text ends at 700; the order note at 708-711.",
    "Robert P. Wilder", SVM,
    W + "Wilder's pledge pamphlet (1890).",
    [row("wilder-volunteer-pledge", "Wilder, The Volunteer Pledge of the Student Volunteer Movement (June 1890)", "wilder",
         "the whole pamphlet at OCR lines 54-700; the pledge's wording at 446-448", [SVM], "tradition", "provisional", "eng",
         doc((1890, 1890), "title page: 'June, 1890.'"),
         "One of the movement's founders explains its pledge and how to use it.")])

# ---------------- Moravians, Lourdes, Christadelphians, Brethren, Latter-day Saints, rescue missions ----------------
I = "ahistoryunitasf00hamigoog"
chk(I, 118, r"MDCCCXCV"); chk(I, 133, r"Copyright,?\s+1894", 1); chk(I, 17819, r"HISTORY|UNITAS", 6); chk(I, 9261, r"REFORMED|HISTORY", 4); chk(I, 21131, r"INDICES", 2)
add(I, "corwin-dubbs-hamilton_american-church-history-v8-reformed-and-moravian_1895.txt",
    "A History of the Reformed Church, Dutch, the Reformed Church, German, and the Moravian Church in the United States (American Church History Series, vol. VIII)",
    "E. T. Corwin, D.D., Professor J. H. Dubbs, D.D., and Professor J. T. Hamilton (title page)",
    "New York: The Christian Literature Co. (title page)",
    "1895 (title page: 'MDCCCXCV', OCR line 118; copyright notice of 1894 at 133-134)", 1895, NIC, "eng",
    "clean, with some damaged names and running heads in the text. Google's sheet stands at OCR lines 1-46 and a Harvard library stamp at 48-66.",
    "Three histories bound as one volume of the series. Title page at OCR lines 89-118; contents at 137-460. Corwin's history of the Dutch Reformed Church from 454 to about 9255. Dubbs's history of the German Reformed Church from 9261, in nineteen chapters, to about 17818. Hamilton's 'History of the Unitas Fratrum, or Moravian Church, in the United States of America' from 17819: prefatory note at 18056; chapter I at 18104; III 18622; IV 18986; V 19255; VI 19508; VII 19822; VIII 19998; IX 20282; X 20472; XII 20909 (the headings of II and XI were not found); the text ends at 21128. Indices from 21131, the Moravian index from 22743.",
    "E. T. Corwin, J. H. Dubbs and J. T. Hamilton", MOR,
    W + "wanted row 323, J. Taylor Hamilton, his history of the Moravians in the United States (1895).",
    [row("hamilton-history-of-the-unitas-fratrum-in-the-united-states", "Hamilton, A History of the Unitas Fratrum, or Moravian Church, in the United States of America (1895)", "hamilton-j-taylor",
         "Hamilton's history at OCR lines 17819-21128; the Moravian index from 22743", [MOR], "tradition", "provisional", "eng",
         doc((1895, 1895), "title page: 'MDCCCXCV'; copyright notice of 1894"),
         "A Moravian professor at Bethlehem writes his church's American history. The two Reformed histories bound with it are by other hands and have no shelf row.")],
    ruled={"hamilton-j-taylor": ("metadata-omission", "The title page names three authors (file lines 101-121); Hamilton's history has its own title, 'by J. Taylor Hamilton, Professor of Church History in the Moravian Theological Seminary at Bethlehem, Pa.' (file lines 17831-17841).")})

I = "ourladylourdest00monzgoog"
chk(I, 88, r"SISK"); chk(I, 62, r"Copyright"); chk(I, 778, r"BOOK", 4); chk(I, 484, r"September", 2)
add(I, "lasserre_our-lady-of-lourdes_sisk1872.txt",
    "Our Lady of Lourdes: the history of the miraculous sanctuary of Our Lady of Lourdes, in the department of the Upper Pyrenees, France; translated from the French of Henry Lasserre, with his special permission",
    "Henri Lasserre (title page: 'Henry Lasserre'); translated by the Rev. F. Ignatius Sisk, O.C., of St. Bernard's Abbey, Leicestershire (title page)",
    "London: Thomas Richardson and Son; Dublin and Derby (title page, read on the page image)",
    "1872 (title page: 'MDCCCLXXII.', read on the page image, leaf n7; the OCR reads 'UDOCOLZZU.' at line 114)", 1872, NIC, "eng",
    "mostly readable, with scattered damage ('Bemadette'); running heads and Google's 'Digitized by' stamp, about 440 times, sit in the text. Google's sheet stands at OCR lines 1-66.",
    "A second English version of Lasserre, by a named translator. Half-title at OCR line 62, with '(The Copyright is reserved.)', a notice of 1872; title page at 74-114. Sisk's dedication to a Cistercian prioress at 126-201; contents at 209-330. The brief of Pius IX to the author, in Latin at 337-401 and in English at 411-485, given at Rome, 4 September 1869. Lasserre's preface at 571-761. Book I at 778; II 3210; III 6223; IV 8642; V 10900; VI 12839; VII 14854; VIII 16856; IX 18086; X 20294; XI 21577. The text ends at 21998; the publisher's advertisements follow.",
    "Henri Lasserre", RC19,
    W + "wanted row 277, Bernadette Soubirous: Lasserre in Sisk's English of 1872 (another English version, of 1870, is held).",
    [row("lasserre-our-lady-of-lourdes-sisk", "Lasserre, Our Lady of Lourdes, translated by F. Ignatius Sisk (1872)", "lasserre",
         "books I-XI at OCR lines 778-21998; the Pope's brief at 337-485", [RC19], "context", "provisional", "eng",
         doc((1869, 1872), "the Pope's brief to the author is dated 4 September 1869 (OCR lines 484-485); this translation's title page reads 1872"),
         "A devout layman's history of the apparitions and the shrine, in an English monk's translation. Bernadette's words reach the reader through Lasserre and then through the translator.")])

I = "thetrialofthemos00robeuoft"
chk(I, 47, r"1.08"); chk(I, 45, r"WALKER"); chk(I, 1525, r"SECOND", 3); chk(I, 13427, r"TWELFTH", 3); chk(I, 14712, r"trial\s+ends", 1)
add(I, "roberts-robert_the-trial_1908.txt",
    "The Trial: the most notable lawsuit of ancient or modern times. The Incorporated Scientific Era Protection Society v. Paul Christman and others, in the Court of Common Reason. Issue: 'Did Christ rise from the dead?' Verbatim report by a shorthand writer",
    "The title page names no author; the preface is signed 'The Author', and the archive.org record credits Robert Roberts",
    "Birmingham: C. C. Walker, 21, Hendon Road, Sparkhill (title page)",
    "1908 (title page, read on the page image, leaf n6; the OCR reads '1008.' at line 47)", 1908, NIC, "eng",
    "clean, with small errors. A University of Toronto presentation slip stands at OCR lines 1-9.",
    "An argument for the resurrection in the form of a trial in twelve sittings. Title page at OCR lines 15-48; the preface, signed 'The Author', at 51-69; contents at 72-628. The first sitting from 630 (it has no heading in the body); the second at 1525; third 2873; fourth 4472; fifth 5611; sixth 7074; seventh 8041; eighth 9028; ninth 9971; tenth 11324; eleventh 12470; twelfth, the summing-up and verdict, at 13427. The text ends at 14712. An advertisement 'by the same author' for Christendom Astray follows.",
    "Robert Roberts", CHR,
    W + "wanted row 254, Robert Roberts: The Trial, in the printing of 1908.",
    [row("roberts-the-trial", "Roberts, The Trial (Birmingham, 1908)", "roberts-robert",
         "the twelve sittings at OCR lines 630-14712", [CHR], "tradition", "provisional", "eng",
         doc((1908, 1908), "title page: 1908 (page image); the preface carries no date"),
         "A defense of the resurrection cast as a court case, with counsel, witnesses and a verdict. The title page gives no author; the last leaf advertises Christendom Astray as 'by the same author'.")])

I = "isbibledivineas00robegoog"
chk(I, 148, r"BIBLE\s+DIVINE"); chk(I, 826, r"DISCUSSION", 2); chk(I, 9913, r"REVIEW", 2); chk(I, 8698, r"JUNE|June|22", 6)
add(I, "roberts-bradlaugh_is-the-bible-divine-six-nights-discussion_1876.txt",
    "Is the Bible Divine? A six nights' discussion between Mr. Charles Bradlaugh, of London, and Mr. Robert Roberts, of Birmingham, in Leicester and Birmingham, on June 13th, 14th, 15th, 20th, 21st and 22nd, 1876; with a review of the discussion by Mr. Roberts",
    "Charles Bradlaugh and Robert Roberts (title page)",
    "London: F. Pitman, 20, Paternoster Row; Birmingham: Robert Roberts, Athenaeum Rooms, Temple Row (title page)",
    "1876 (title page, read on the page image, leaf n6; the OCR garbles the year at line 193 and reads '1878' on the damaged first title at line 101)", 1876, NIC, "eng",
    "clean in the debate; running heads, signature marks and the title pages are garbled, and Google's 'Digitized by' stamp stands on nearly every page. Google's sheet stands at OCR lines 1-43.",
    "A shorthand report of a public debate, printed by one of the two speakers. Title page at OCR lines 148-193, with the proposition: 'That the Scriptures are the reliable and authentic record of Divine revelation'; Roberts affirms and Bradlaugh denies. Preface with the correspondence that arranged the debate, at 219-825. The six nights: the first, Leicester, 13 June 1876, from 826; the second from 2458; the third from 4019; the fourth, Birmingham, 20 June, from 5874; the fifth from 7433; the sixth, 22 June, from 8698. The debate ends at 9893. Roberts's review of the discussion at 9913-12885; he says there that Bradlaugh did not revise the report and declined to write a reply. Printer's line at 12893; index and the publisher's list follow.",
    "Robert Roberts and Charles Bradlaugh", CHR,
    W + "wanted row 254, Robert Roberts: his debate with Bradlaugh (1876).",
    [row("roberts-bradlaugh-debate-six-nights", "Is the Bible Divine? The six nights' discussion between Bradlaugh and Roberts (June 1876)", "roberts-robert",
         "the six nights at OCR lines 826-9893", [CHR], "tradition", "provisional", "eng",
         doc((1876, 1876), "title page: 1876; the nights are dated 13 to 22 June 1876"),
         "Roberts's side is the Christadelphian case for the Bible; Bradlaugh's speeches are an opponent's, taken down in shorthand and, by Roberts's own account, not revised by Bradlaugh. Quote each speaker as himself."),
     row("roberts-review-of-the-discussion", "Roberts, A Review of the Discussion with Mr. Bradlaugh (1876)", "roberts-robert",
         "the review at OCR lines 9913-12885; the preface and correspondence at 219-825", [CHR], "tradition", "provisional", "eng",
         doc((1876, 1876), "title page: 1876"),
         "Roberts's own afterword on the six nights, answering Bradlaugh point by point.")])

I = "minorprophets00bell"
chk(I, 50, r"1870"); chk(I, 33, r"BELLETT"); chk(I, 82, r"HO\s*SEA", 3); chk(I, 3200, r"MALACHI", 3)
add(I, "bellett_minor-prophets_1870.txt",
    "The Minor Prophets",
    "J. G. Bellett, author of 'The Moral Glory of the Lord Jesus' (title page)",
    "London: Robert L. Allan, 15 Paternoster Row, and Glasgow; with Dublin, Guernsey and Boston sellers (title page)",
    "1870 (title page, OCR line 50)", 1870, NIC, "eng",
    "clean, with typical slips ('lie' for He); running heads sit in the text. A Princeton Theological Seminary bookplate stands at OCR lines 1-10.",
    "Short meditations on the twelve prophets. Title page at OCR lines 25-50; contents at 53-79. Hosea at 82; Joel 375; Amos 642; Obadiah 723; Jonah 957; Micah 1353; Nahum 1681; Habakkuk 1847; Zephaniah 2145; Haggai 2427; Zechariah 2716; Malachi 3200. The text ends at 3556. No preface or index.",
    "John Gifford Bellett", PB,
    W + "wanted row 260, J. G. Bellett: The Minor Prophets (1870).",
    [row("bellett-minor-prophets", "Bellett, The Minor Prophets (1870)", "bellett",
         "the whole book at OCR lines 82-3556", [PB], "tradition", "provisional", "eng",
         doc((1870, 1870), "title page: 1870"),
         "Bellett's own meditations on Hosea to Malachi.")])

I = "11604936bsb"
chk(I, 78, r"1886"); chk(I, 71, r"Edition"); chk(I, 62, r"JOHN"); chk(I, 681, r"CHAP|I", 4)
add(I, "bellett_evangelists-gospel-by-st-john_7th-ed1886.txt",
    "The Evangelists: papers on the four Gospels; the Gospel by St. John; seventh edition",
    "J. G. Bellett (the part's title page; the collective title page reads 'By J. G. B.')",
    "London: W. H. Broom and Rouse, 25, Paternoster Square (the part's title page)",
    "1886 (the part's title page, OCR line 78; the collective title page at lines 4-23 prints no year)", 1886, NR, "eng",
    "clean, with minor slips; running heads sit in the text. The Bavarian State Library's card stands at OCR lines 7149-7168 and marks the scan as 'Bd. 1'.",
    "The first part only, on John. The collective title page at OCR lines 4-23 and its contents at 32-47 list four parts (John, Luke, Matthew, Mark) and a conclusion; the scan holds John alone. The publisher's note at 50-59; the part's title page at 62-78. Bellett's introduction at 85-673. On the Gospel by St. John: chapters I-IV at 681; V-XII at 1682; XIII-XVII at 3670; XVIII-XXI at 5404. The text ends at 7143.",
    "John Gifford Bellett", PB,
    W + "wanted row 260, J. G. Bellett: The Evangelists (1886; the scan holds the part on John only).",
    [row("bellett-evangelists-john", "Bellett, The Evangelists: the Gospel by St. John (seventh edition, 1886)", "bellett",
         "the introduction at OCR lines 85-673; the papers on John at 681-7143", [PB], "tradition", "provisional", "eng",
         doc((1886, 1886), "the part's title page: 1886, seventh edition"),
         "Bellett's meditations on the fourth Gospel. A late edition; the year of the first is not printed in the scan.")])

I = "biographyfamilyr00snow"
chk(I, 62, r"1884"); chk(I, 48, r"SNOW"); chk(I, 996, r"CHAPTER", 3); chk(I, 24812, r"SUPPLEMENT", 3); chk(I, 6173, r"Southampton|June|1850", 6)
add(I, "snow_biography-and-family-record-of-lorenzo-snow_1884.txt",
    "Biography and Family Record of Lorenzo Snow, one of the Twelve Apostles of the Church of Jesus Christ of Latter-day Saints; written and compiled by his sister",
    "Eliza R. Snow Smith (title page)",
    "Salt Lake City, Utah: Deseret News Company, printers (title page)",
    "1884 (title page, OCR line 62)", 1884, NR, "eng",
    "clean, with stray page numbers and running heads. Brigham Young University library stamps stand at OCR lines 1-17 and the Internet Archive's 'Digitized by' notice at 20-25.",
    "Sixty-three chapters and a supplement. Title page at OCR lines 28-62; preface, signed E. R. S. S., at 65-93; contents at 96-974. Chapter I at 996; X 3252; XX 6683; XXX 11449; XL 15258; L 18952; LX 22041; LXIII, the genealogies, at 24210. Supplement, the tour of Palestine begun in October 1872, from 24812, with fifteen letters to the end at 29276. Lorenzo Snow's own words: his letter from Southampton, 14 June 1850, at 6173-6410; extracts from his journal introduced at about 1403, 2174, 7173 and 14648; letters signed by him at 9812, 10741, 11104, 13712 and in the supplement. Letters to him and a kinsman's journal are also quoted.",
    "Eliza R. Snow Smith", LDS,
    W + "wanted row 252, Eliza R. Snow: her Life of her brother Lorenzo Snow (1884).",
    [row("snow-biography-of-lorenzo-snow", "Eliza R. Snow Smith, Biography and Family Record of Lorenzo Snow (1884)", "snow",
         "chapters I-LXIII at OCR lines 996-24811; the supplement at 24812-29276", [LDS], "tradition", "provisional", "eng",
         doc((1884, 1884), "title page: 1884"),
         "A Latter-day Saint woman writes her brother's life from his journals and letters and her own memory. His letters and journal extracts are first-hand; name him when quoting them.")])

for ident, n, y, fn, title, pub, pubdate, cont, a, b in [
    ("annualreportpaci1907paci", "thirty-first", 1908, "pacific-garden-mission_thirty-first-annual-report_1908.txt",
     "Thirty-One Years of Rescue Work at Pacific Garden Mission: thirty-first annual report, September 15, 1908",
     "Chicago: Pacific Garden Mission, 100 E. Van Buren St. (cover)",
     "1908 (title leaf: 'September 15, 1908', read on the page image, leaf n2, and at OCR line 30; the archive.org identifier carries '1907')",
     "The report for the year ended 15 September 1908. Cover and title lines at OCR lines 3-30. Salutatory at 47; a great need, a home for homeless girls, at 96; the men's department at 221; how we reach the masses at 255; three converts' own testimonies at 322, 366 and 411; contributions and church collections from 453; the endowment fund at 804; the treasurer's account at 869; the board of trustees at 906; thanks, signed by Sarah D. Clarke and Harry Monroe, at 926-940.", 47, 940),
    ("annualreportpaci1915paci", "fortieth", 1916, "pacific-garden-mission_fortieth-annual-statement_1916.txt",
     "Everlastingly At It: the Cross of Christ exalted 40 years in the Loop of Chicago. Pacific Garden Mission, fortieth annual statement",
     "Chicago: Pacific Garden Mission, 67 W. Van Buren St. (cover and title leaf)",
     "1916 (the cover and the title leaf print no year: page images, leaves n0 and n2. The statement opens 'The close of our fiscal year ending Sept. 15th, 1916', OCR lines 43-44, and the auditor's letter is dated 17 November 1916, line 430; the library shelf mark on the cover reads 1915/16)",
     "The statement for the year ended 15 September 1916. Cover and title lines at OCR lines 4-24. 'Our Fortieth Annual Statement' at 40, signed by Sarah D. Clarke and Melvin E. Trotter at 119-120; subscriptions from 126; church offerings from 180; the auditor's letter, 17 November 1916, at 430-470; balance sheet at 480; income and expense at 581; endowment and general funds at 638 and 654; form of bequest at 672; the board of trustees at 693.", 40, 717)]:
    chk(ident, a, r"Salutatory|Fortieth|Annual", 4)
    rights = None; rshort = None
    if y == 1916:
        chk(ident, 44, r"1916", 1); chk(ident, 430, r"November\s+17,\s+1916", 1)
        rights = "Public Domain (pd-us-by-date: published 1916; the cover and title leaf print no year, and the date is the statement's own, 'fiscal year ending Sept. 15th, 1916', OCR lines 43-44, with the auditor's letter of 17 November 1916 at line 430 and the library's shelf mark agreeing); " + NR
        rshort = "published 1916 by its own dated statement, out of US copyright by date"
    else:
        chk(ident, 30, r"1908", 1)
    add(ident, fn, title, "Pacific Garden Mission (cover)", pub, pubdate, y, NR, "eng",
        "clean in the prose; the lists of names and sums run together. The Internet Archive's 'Digitized by' notice stands at OCR lines 32-38.",
        cont, "Pacific Garden Mission", RESC,
        W + "the Pacific Garden Mission's annual reports (the list named 1895, 1907 and 1915; the two found report the years ended September 1908 and September 1916, and the report of 1895 was not found).",
        [row("pacific-garden-mission-%s-annual-report" % n, "Pacific Garden Mission, %s annual %s (%d)" % (n, "report" if y == 1908 else "statement", y), "pacific-garden-mission",
             "the report at OCR lines %d-%d" % (a, b), [RESC], "tradition", "provisional", "eng",
             doc((y, y), "the report is for the year ended 15 September %d" % y),
             "The mission's own yearly account of its work and money" + (", with three converts' testimonies in their own words." if y == 1908 else "."))],
        rights=rights, rights_short=rshort,
        ruled={"pacific-garden-mission": ("anonymous", "A corporate report; the cover names the mission and no author (file lines %s)." % ("15-42" if y == 1908 else "16-36"))})

for f in FAILS:
    print("ANCHOR FAIL", f)
assert not FAILS
json.dump(items, open(S + "b299/work/spec299.json", "w"), ensure_ascii=False, indent=1)
print(len(items), "items")
for it in items:
    assert len(it["filename"]) < 120 and it["filename"].endswith(".txt"), it["filename"]
    for k in ("title", "creator", "publisher", "pubdate", "rights", "ocr", "content"):
        assert "\n" not in it[k]
