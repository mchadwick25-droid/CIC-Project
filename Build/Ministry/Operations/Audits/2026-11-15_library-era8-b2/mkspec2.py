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
        (p,) = glob.glob(S + "dl/" + ident + "__*_djvu.txt")
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


BAPT = "the-baptists"
DISS = "english-old-dissent"
COFE = "restoration-georgian-church-of-england"
VICT = "victorian-church-of-england"
SUND = "the-sunday-school-and-bible-institute-movement"
METH = "the-methodist-revival"
NENG = "the-evangelical-awakening-in-new-england"
UNIV = "early-american-unitarians-universalists"
SGA = "the-second-great-awakening-and-camp-meeting-worl"
STONE = "the-stone-campbell-restoration-movement"
ANCIEN = "catholic-church-ancien-regime"
SJ = "society-of-jesus-1650-1814"
PR = "port-royal-jansenism"
LATAM = "colonial-latin-american-devotional-catholicism"
CHINA = "chinese-catholicism-1650-1906"
SAYFO = "the-sayfo-and-the-syriac-diaspora"

# ---------------- British Isles and Methodists ----------------
I = "bim_eighteenth-century_a-brief-account-of-the-g_dutton-anne_1750"
chk(I, 77, r"1750", 2); chk(I, 242, r"PART\s+I"); chk(I, 19469, r"APPENDIX", 2); chk(I, 23554, r"onour.d Brethren", 2)
add(I, "dutton-anne_brief-account-of-the-gracious-dealings-of-god_1750.txt",
    "A Brief Account of the Gracious Dealings of God, with a Poor, Sinful, Unworthy Creature, in Three Parts",
    "Anne Dutton (title page: 'By A. D.'; the archive.org record gives the name)",
    "London: printed by J. Hart in Popping's Court, Fleet-Street, and sold by J. Lewis in Pater-noster-Row (title page)",
    "1750 (title page, OCR line 77)", 1750, NR, "eng",
    "mostly legible, with the long s kept; the title page and the blank leaves around OCR lines 90-160 are junk characters, and catchwords and margins are mixed into the text.",
    "The three parts of her own account, with her appendix and a letter on printing by a woman. General title page at OCR lines 1-77; her note to the reader at 116-175, saying Parts I and II were printed 'some Years ago'. Part I: title page at 210-241, heading at 242, her preface at 306. Part II: title page from 4159 (its imprint reads 1743 at 4218). Part III: title page from 13871, text from 14005, with her numbered list of 26 tracts at about 18600-18735. Appendix from 19469. Errata at 23455. The letter 'To such of the Servants of Christ, who may have any Scruple about the Lawfulness of Printing any Thing written by a Woman': title at 23481-23547, text from 23554 to the end of the file at 24020. Her own letters, and friends' letters of 1741, are quoted inside Parts II and III.",
    "Anne Dutton", BAPT,
    "Wanted row A135: Anne Dutton's own account of her life (the 1750 printing in three parts).",
    [row("dutton-brief-account-three-parts", "Dutton, A Brief Account of the Gracious Dealings of God, Parts I-III with the Appendix (1750)", "dutton-anne",
         "Part I from OCR line 242; Part II from 4159; Part III from 13871; the Appendix at 19469 to about 23440", [BAPT], "tradition", "provisional", "eng",
         doc((1743, 1750), "Part II's own imprint reads 1743 (OCR line 4218); the general title page reads 1750 (line 77)"),
         "Her own account of God's dealings with her and of the tracts she wrote. Provisional only because the title page gives initials, 'A. D.', and the name is the record's."),
     row("dutton-letter-on-printing-by-a-woman", "Dutton, a letter on the lawfulness of printing any thing written by a woman (1750 printing)", "dutton-anne",
         "the letter at OCR lines 23554-24020, its title at 23481-23547", [BAPT], "tradition", "provisional", "eng",
         doc((1743, 1750), "printed with the 1750 Brief Account; Part III's title page says it is prefixed, and it stands at the end"),
         "Her defense of writing for print as a woman, addressed to ministers who objected. Signed 'A. D.'")])

I = "memoirsofrevisaa00gibb"
chk(I, 66, r"MDCCLXXX"); chk(I, 306, r"CHAP"); chk(I, 15791, r"CHAP", 3); chk(I, 21782, r"FINIS", 2)
add(I, "gibbons-thomas_memoirs-of-isaac-watts_1780.txt",
    "Memoirs of the Rev. Isaac Watts, D.D.",
    "Thomas Gibbons, D.D. (title page)",
    "London: printed for James Buckland, and Thomas Gibbons (title page)",
    "1780 (title page: 'MDCCLXXX', OCR line 66)", 1780, NIC, "eng",
    "legible, with the long s read as f throughout; verse and two-column lists run together in places. Princeton Theological Seminary library plates stand at OCR lines 1-26.",
    "Twelve chapters. Dedication to Mrs. Elizabeth Abney at OCR lines 69-142; preface at 143-227, signed Hoxton-Square, 11 April 1780; contents at 228. Chapter I at 306, II 1176, III 2869, IV 4273, V 5919, VI 7503, VII 9183, VIII 11677, IX 13330, X 14208, XI 15158. Chapter XII, from 15791 to 20910, is 57 numbered letters to or about Watts, by Secker and others, not by Watts. Watts's own letters are quoted inside the chapters (for example to his brother at about 3143). Appendix I, a catalogue of his writings, at 20911; Appendix II at 21337; 'Finis' at 21782; Gibbons's list of his own books follows to the end.",
    "Thomas Gibbons", DISS,
    "Wanted row A136: Gibbons's Memoirs of Isaac Watts, the Life by a friend and fellow minister.",
    [row("gibbons-memoirs-of-watts-chapters-1-11", "Gibbons, Memoirs of the Rev. Isaac Watts: the Life, chapters I-XI (1780)", "gibbons-thomas",
         "chapters I-XI at OCR lines 306-15790", [DISS], "tradition", "provisional", "eng",
         doc((1780, 1780), "title page: 'MDCCLXXX'; the preface is signed 11 April 1780 (about OCR line 205)"),
         "The Life is Gibbons's voice, written in 1780; Watts's letters appear only as he quotes them."),
     row("gibbons-memoirs-of-watts-letters-to-watts", "Gibbons, Memoirs of the Rev. Isaac Watts: chapter XII, letters to Dr. Watts from his correspondents", "gibbons-thomas",
         "chapter XII at OCR lines 15791-20910", [DISS], "context", "provisional", "eng",
         doc((1780, 1780), "title page: 'MDCCLXXX'"),
         "Fifty-seven letters written to or about Watts by bishops, ministers and friends. None is Watts's own; the writers are many and are named at each letter's head.")])

I = "memoirsoflifecha00orto"
chk(I, 71, r"M\.DCCC\.XXV", 2); chk(I, 1348, r"CHAP"); chk(I, 958, r"Russell", 2); chk(I, 1336, r"1765", 2)
add(I, "orton_memoirs-of-philip-doddridge_russell1825.txt",
    "Memoirs of the Life, Character, and Writings of the late Rev. Philip Doddridge, D.D., of Northampton; with an introductory essay by the Rev. David Russell, Dundee",
    "Job Orton (title page); introductory essay by David Russell (title page)",
    "Edinburgh: printed for Waugh and Innes (title page); printed by A. Balfour and Co.",
    "1825 (title page: 'M.DCCC.XXV.', OCR line 71)", 1825, NR, "eng",
    "clean, with occasional slips ('tliat', 'Avhich'); running heads sometimes stand as lines. The Internet Archive's scan notice stands at OCR lines 1-31 and library-card junk after the printer's line at 12096.",
    "An Edinburgh reprint of Orton's Life, first printed in 1766, with a new essay. Contents at OCR line 77. Russell's introductory essay at 165-960, signed Dundee, June 1825. Orton's preface at 963-1336, dated Shrewsbury, 6 November 1765. The Memoirs: chapter I at 1348, II 1900, III 2663, IV 2868, V 3187, VI 3794, VII 4935, VIII 5811 (in eight sections), IX 10668. A poem to Doddridge's memory at 11900; the book ends at 12096. Doddridge's letters and papers are quoted throughout the chapters.",
    "Job Orton", DISS,
    "Wanted row A137: Orton's Memoirs of Doddridge, the Life by his pupil (the 1825 reprint, whose OCR is clean; the 1766 first edition's is not).",
    [row("orton-memoirs-of-doddridge", "Orton, Memoirs of the Life, Character and Writings of Philip Doddridge (1766; Edinburgh, 1825)", "orton",
         "Orton's preface at OCR lines 963-1336; chapters I-IX at 1348-11899", [DISS], "tradition", "provisional", "eng",
         doc((1765, 1766), "Orton's preface is dated Shrewsbury, 6 November 1765 (OCR line 1336); this printing's title page reads 1825"),
         "Orton's Life of Doddridge, with long quotations from Doddridge's letters and papers. Read in a reprint of 1825; whether the reprint changes Orton's text was not checked."),
     row("russell-introductory-essay-to-orton", "David Russell, introductory essay to Orton's Memoirs of Doddridge (1825)", "orton",
         "the essay at OCR lines 165-960", [DISS], "context", "provisional", "eng",
         doc((1825, 1825), "signed 'David Russell. Dundee, June 1825' (OCR lines 958-960)"),
         "An essay of 1825, signed from Dundee, commending the Life. Later than the entry's window and not Orton's voice.")])

I = "memoirslifeandc00moregoog"
chk(I, 171, r"MDCCCXXXV"); chk(I, 157, r"THIRD\s+EDITION"); chk(I, 162, r"VOL"); chk(I, 2908, r"PART\s+I", 2); chk(I, 9688, r"PART\s+II", 2); chk(I, 19356, r"END\s+OF\s+VOL")
add(I, "roberts-william_memoirs-of-hannah-more-v1_3rd-ed1835.txt",
    "Memoirs of the Life and Correspondence of Mrs. Hannah More; third edition, revised, with an additional preface; vol. I",
    "William Roberts, Esq. (title page)",
    "London: R. B. Seeley and W. Burnside, Fleet Street (title page)",
    "1835 (title page: 'MDCCCXXXV.', OCR line 171; the archive.org record says 1834)", 1835, NIC, "eng",
    "clean, with a few damaged words. The scan repeats some pages: part of the front matter and stretches of Part I, chapters I-III, stand twice (for example OCR lines 3936 and 4643; 6924 and 7376). Google's sheet stands at OCR lines 1-47 and a presentation plate at 49-60.",
    "The first of the volumes, to 1785. Title page at OCR lines 139-171. Roberts's three prefaces at 180, 256 and 426; the table of the letters at 1779-2905. Part I, 1745 to 1779: heading at 2908, chapter I at 2919, II 4454, III 6924 (repeated at 7376), IV 8402. Part II, 1779 to 1785: heading at 9688, chapter I at 9699, II 11985, III 13748, IV 17566. 'End of Vol. I.' at 19356. Her letters run through both parts, mixed with letters to her from Garrick, Mrs. Montagu and others and with Roberts's narrative.",
    "William Roberts", COFE,
    "Wanted row A139: Roberts's Memoirs of Hannah More, for her own letters (vol. 1 only; the later volumes were not taken).",
    [row("roberts-memoirs-of-hannah-more-v1", "Roberts, Memoirs of the Life and Correspondence of Mrs. Hannah More, vol. I: 1745-1785 (third edition, 1835)", "roberts-william",
         "Part I at OCR lines 2908-9687; Part II at 9688-19356", [COFE], "context", "provisional", "eng",
         doc((1835, 1835), "title page: 'MDCCCXXXV.', third edition"),
         "A Life built from her letters. Her own letters are a first-hand voice of the years to 1785; the frame, and the choice and cutting of the letters, are Roberts's. Letters to her stand among them.")])

I = "publickspiritil00toddgoog"
chk(I, 188, r"1808", 2); chk(I, 2679, r"DESIGNS|PROCEEDINGS", 3); chk(I, 6880, r"THE\s+END", 2); chk(I, 499, r"1808", 3)
add(I, "todd-henry-john_publick-spirit-life-and-designs-of-thomas-bray_2nd-ed1808.txt",
    "Publick Spirit Illustrated in the Life and Designs of the Reverend Thomas Bray, D.D.; to which are added the designs and proceedings of those who now form the institution called Dr. Bray's Associates; the second edition, revised",
    "The title page names no author; the introduction is signed by Henry J. Todd, who says the Life is supposed to be by Samuel Smith",
    "London: printed for F. C. and J. Rivington, St. Paul's Church-yard (title page)",
    "1808 (title page, OCR line 188)", 1808, NIC, "eng",
    "prose pages show damage ('wi/h', 'tliat', dropped letters) and the title page is badly garbled; tables and name lists are mostly legible. Google's sheet stands at OCR lines 1-47.",
    "The Life of 1746 as re-edited in 1808, with much added. Title page at OCR lines 119-190. Todd's introduction at 207-500, signed 25 January 1808; at about 275-295 it says the Life 'is almost entirely copied' from the Biographia Britannica and is supposed to be the work of Samuel Smith, printed in 1746 without his name. The Life and Designs of Dr. Bray at 578-2367. Todd's additions to the Life, lettered notes, at about 2375-2678. The Designs and Proceedings of the Associates for 1807 from 2679, with an Act of Parliament and rules at about 2850-3350, accounts at 4927, letters of thanks from clergy at 5429-5791, and catalogues of Bray's manuscripts and books from 5792. 'The End' at 6880.",
    "Henry John Todd (editor)", COFE,
    "Wanted row A140: the Life of Thomas Bray of 1746, in Todd's edition of 1808 (the 1746 print's year is garbled in its scan).",
    [row("life-and-designs-of-thomas-bray", "Publick Spirit Illustrated in the Life and Designs of Thomas Bray (1746; second edition, ed. Todd, 1808): the Life", "todd-henry-john",
         "the Life at OCR lines 578-2367; Todd's lettered additions at about 2375-2678", [COFE], "tradition", "provisional", "eng",
         doc((1746, 1808), "Todd's introduction dates the first printing to 1746 (about OCR lines 275-295); this edition's title page reads 1808"),
         "A Life of Bray and of the designs he began, from inside the Church of England. Unsigned; Todd reports the attribution to Samuel Smith and does not prove it. The lettered notes are Todd's."),
     row("bray-associates-designs-and-proceedings-1807", "Dr. Bray's Associates, Designs and Proceedings for the year 1807, with Todd's introduction (1808)", "todd-henry-john",
         "Todd's introduction at OCR lines 207-500; the Designs and Proceedings at 2679-6880", [COFE], "tradition", "provisional", "eng",
         doc((1807, 1808), "the Proceedings are for the year 1807; the introduction is signed 25 January 1808 (OCR lines 498-500)"),
         "The Associates' own report, accounts, clergy's letters of thanks and book lists, edited by Todd. Several hands, all inside the institution.")],
    ruled={"todd-henry-john": ("metadata-omission", "The title page (file lines 131-202) names no author or editor. The introduction is signed 'Henry J. Todd' and dated 25 January 1808 (file lines 510-512). The Life itself is unsigned; Todd says it is supposed to be by Samuel Smith (file lines about 287-307).")})

I = "lifewilliamwilb04wilbgoog"
chk(I, 150, r"MDCCCXXXVIII", 2); chk(I, 407, r"CHAPTER", 3); chk(I, 12909, r"CHAPTER", 3); chk(I, 14842, r"APPENDIX", 3)
add(I, "wilberforce-robert-and-samuel_life-of-william-wilberforce-v1_1838.txt",
    "The Life of William Wilberforce, by his sons; in five volumes; vol. I",
    "Robert Isaac Wilberforce, M.A., and Samuel Wilberforce, M.A. (title page)",
    "London: John Murray, Albemarle Street (title page)",
    "1838 (title page: 'MDCCCXXXVIII', read on the page image, leaf n11, and at OCR line 150)", 1838, NIC, "eng",
    "legible, with small errors ('liUh', 'iHm'); footnotes and note numbers sit inside the text. Google's sheet stands at OCR lines 1-47.",
    "The first of five volumes, 1759 to 1792; the title page reads 'Vol. I.' (page image; the archive.org identifier carries '04'). Directions to the binder at OCR lines 154-190; the sons' preface at 194-341. Chapter I, birth and education, at 407; II, 1780-1783, at 858; III, 1783-4, at 2075; IV, 1784-1786, at 2925; V, 1786-1787, at 4706; VI, 1787-1788, at 5680; VII, 1788-1790, at 7672; VIII, 1790-1791, at 10986; IX, 1791-1792, at 12909. Appendix from 14842, with memoranda Wilberforce dictated at 14850. The scan stops inside the appendix, in a note quoting Mr. Croker, at 15584; there is no end page. His diary and letters are quoted throughout.",
    "Robert Isaac Wilberforce and Samuel Wilberforce", COFE,
    "Wanted row A141: the sons' Life of William Wilberforce, for his diary and letters (vol. 1 only; the later volumes were not taken).",
    [row("wilberforce-sons-life-v1", "R. I. and S. Wilberforce, The Life of William Wilberforce, vol. I: 1759-1792 (1838)", "wilberforce-robert-and-samuel",
         "chapters I-IX at OCR lines 407-14841; appendix at 14842-15584, where the scan stops", [COFE], "context", "provisional", "eng",
         doc((1838, 1838), "title page: 'MDCCCXXXVIII'"),
         "His sons' Life. His diary and letters are first-hand for the years to 1792; the sons chose and cut them, and the narrative is theirs.")],
    ruled={"wilberforce-robert-and-samuel": ("metadata-omission", "The title page (file lines 112-162) reads 'by his sons, Robert Isaac Wilberforce, M.A. ... and Samuel Wilberforce, M.A.'. Two authors, so the slug is not a single name.")})

I = "robertraikesjou00alfrgoog"
chk(I, 105, r"1877", 2); chk(I, 1614, r"1783", 2); chk(I, 1165, r"CHAPTER", 3); chk(I, 6120, r"FINI", 2)
add(I, "gregory-alfred_robert-raikes-journalist-and-philanthropist_1877.txt",
    "Robert Raikes: Journalist and Philanthropist. A history of the origin of Sunday schools",
    "Alfred Gregory (title page)",
    "London: Hodder and Stoughton; Sunday School Union (title page; 'Third thousand')",
    "1877 (title page, OCR line 105)", 1877, NIC, "eng",
    "clean, with minor slips; running heads and page numbers sit inside the text. Google's sheet stands at OCR lines 1-45 and Harvard library plates at 46-85.",
    "Nine chapters. Preface, signed A. G., at OCR lines 127-171; contents at 172. Chapter I at 202, II 501, III, the prison philanthropist, 766; IV, the establishment of Sunday schools, 1165; V, the spread of the movement, 2213; VI 3495; VII 4337; VIII 5305; IX 5833; 'Finis' at 6120; the publisher's catalogue from 6128. Raikes's own words as Gregory prints them: his letter to Colonel Townley, dated Gloucester, 25 November 1783, at 1614-1673; his letter to the Arminian Magazine, dated 5 June 1785, at 1675-1748; his Gloucester Journal notice of 24 May 1784 at 2273-2300. Each is an extract Gregory introduces; none was compared with its first printing.",
    "Alfred Gregory", SUND,
    "Wanted row A159: Robert Raikes and the first Sunday schools, with his letters of 1783 and 1785 as Gregory prints them.",
    [row("gregory-robert-raikes", "Gregory, Robert Raikes: Journalist and Philanthropist (1877)", "gregory-alfred",
         "the whole book at OCR lines 202-6120; Raikes's letters at 1614-1673 and 1675-1748, his newspaper notice at 2273-2300", [SUND, COFE], "context", "provisional", "eng",
         doc((1877, 1877), "title page: 1877"),
         "A Life of Raikes written in 1877, long after the first schools. It prints Raikes's letters of 1783 and 1785 as extracts; quote them as Gregory's printing, not as the originals.")])

I = "taft-biographical-sketches-of-the-lives-and-public-ministry-of-various-holy-women"
chk(I, 133, r"1825", 2); chk(I, 19114, r"1828", 2); chk(I, 20081, r"CROSBY", 2); chk(I, 37056, r"END\s+OF\s+THE\s+SECOND", 2); chk(I, 1011, r"1825", 3); chk(I, 19717, r"1828", 3)
add(I, "taft_biographical-sketches-of-holy-women-v1-v2_1825-1828.txt",
    "Biographical Sketches of the Lives and Public Ministry of Various Holy Women, whose eminent usefulness and successful labours in the Church of Christ have entitled them to be enrolled among the great benefactors of mankind; in which are included several letters from the Rev. J. Wesley never before published; vols. I and II",
    "Zechariah Taft (title pages: 'By Z. Taft')",
    "Vol. I: published for the author, and sold in London by Mr. Kershaw, City Road. Vol. II: printed for the author by H. Cullingworth, Leeds, and sold in London by J. Stephens, City Road (title pages)",
    "1825 (vol. I title page, read on the page image, leaf n6, and at OCR line 133) and 1828 (vol. II title page, OCR line 19114)", 1828,
    "the archive.org item is a reader's upload of 2025 with no rights field; the scan photographs a bound copy from the Thursfield Smith Collection, and the imprint dates are the basis", "eng",
    "readable, with scattered errors and stray margin marks; the front and back leaves, the portrait pages and the contents lists are junk or badly garbled. A library plate and portrait noise stand at OCR lines 1-75.",
    "Two volumes in one scan. Vol. I: title page at OCR lines 76-133; preface at 233-1011, signed New Malton, February 1825; forty-four sketches from Susannah Wesley at 1047 and Mary Fletcher at 1539 to Mary Sewell at 18850, among them Sarah Lawrence 3025, Mary Holder 6196, Elizabeth Evans 8890, Dorothy Ripley 12282 and Ann Cutler 17427; errata at 18991. Vol. II: title page at 19067-19114; preface at 19179-19717, signed Ripon, January 1828; Sarah Crosby at 20081-25350; Elizabeth Collett 25366; Mary Dudley 27174; and about thirty more, to Ann Burrows at 36932; 'End of the second volume' at 37056. Wesley's letters, the women's own journals and letters, and Quaker testimonies are quoted throughout. The headings of two sketches in vol. II were not found.",
    "Zechariah Taft", METH,
    "Wanted row A133: Sarah Crosby and the Methodist women preachers, in Taft's two volumes with Wesley's letters to them.",
    [row("taft-holy-women-sarah-crosby", "Taft, Biographical Sketches of Holy Women, vol. II: Mrs. Sarah Crosby (1828)", "taft",
         "the sketch at OCR lines 20081-25350", [METH], "context", "provisional", "eng",
         doc((1828, 1828), "vol. II title page: 1828"),
         "Taft's memoir of Crosby, built from her journal and letters and from Wesley's letters to her. Her words are first-hand; the selection is Taft's, in 1828."),
     row("taft-holy-women-vols-1-2", "Taft, Biographical Sketches of the Lives and Public Ministry of Various Holy Women, vols. I-II (1825, 1828)", "taft",
         "vol. I sketches at OCR lines 1047-18990; vol. II at 20081-37056; Taft's prefaces at 233-1011 and 19179-19717", [METH], "context", "provisional", "eng",
         doc((1825, 1828), "title pages: 1825 and 1828"),
         "Taft's case for women's preaching, made from short Lives of Methodist and Quaker women. Written after this entry's window. Many voices are quoted; name the woman, not Taft, when quoting a journal or letter.")])

# ---------------- North America ----------------
I = "samsonoccomchris00love"
chk(I, 70, r"Copyright,?\s+1899", 2); chk(I, 65, r"Pilgrim\s+Press", 2); chk(I, 1328, r"Born\s+a\s+Heathen", 2); chk(I, 425, r"CHAPTER", 3); chk(I, 14773, r"APPENDIX", 4)
add(I, "love-william-deloss_samson-occom-and-the-christian-indians-of-new-england_1899.txt",
    "Samson Occom and the Christian Indians of New England",
    "W. DeLoss Love, Ph.D. (title page)",
    "Boston and Chicago: The Pilgrim Press (title page)",
    "1899 (the title page prints no year: page image, leaf n8. The copyright notice on its verso reads 'Copyright, 1899, by W. DeLoss Love': leaf n9 and OCR lines 70-71. The preface is dated October 1899 and the archive.org record's date is c1899)", 1899,
    NIC, "eng",
    "clean; a page of music at about OCR line 8000 is junk. A Princeton Theological Seminary bookplate stands at OCR lines 8-33.",
    "Seventeen chapters and an appendix. Preface at OCR lines 91-163, signed Hartford, October 1899; contents at 164-395. Chapter I at 425, II 1219, III 2116, IV 2668, V 3705, VI 4744, VII 5383, VIII 5813, IX 6691, X 7378, XI 8545, XII 9308, XIII 10364, XIV 10981, XV 12749, XVI 13419, XVII 14107; the text ends at 14772. Appendix, a family history of the Brothertown Indians, at 14773-16553; index from 16554. Love quotes about twenty-five lines of Occom's own narrative of 17 September 1768 at 1328-1355 ('I was Born a Heathen and Brought up in Heathenism'), from the manuscript at Dartmouth; it is an extract, not the whole. Occom's diary, letters and petitions, Wheelock's letters and the Brothertown records are quoted throughout.",
    "W. DeLoss Love", NENG,
    "Wanted row A128: Samson Occom, with the opening of his own narrative of 1768 as Love prints it (the whole narrative was not printed by 1930 so far as found).",
    [row("love-samson-occom", "Love, Samson Occom and the Christian Indians of New England (1899)", "love-william-deloss",
         "chapters I-XVII at OCR lines 425-14772; the appendix at 14773-16553", [NENG], "context", "provisional", "eng",
         doc((1899, 1899), "copyright notice: 'Copyright, 1899' (OCR lines 70-71); preface dated October 1899"),
         "A history written at Hartford in 1899 from manuscripts, a century and more after the events. It runs on past this entry's window to the Brothertown settlement."),
     row("occom-narrative-1768-extract-in-love", "Samson Occom, autobiographical narrative of 17 September 1768: the opening, as Love prints it", "occom",
         "the extract at OCR lines 1328-1355; Love's source note at 1338", [NENG], "tradition", "provisional", "eng",
         doc((1768, 1768), "Love's footnote: 'Wheelock Papers, Dartmouth College, MS., Sept. 17, 1768' (OCR line 1338)"),
         "Occom's own account of his upbringing and conversion, in about twenty-five lines. Love prints only this part; his text was not compared with the manuscript.",
         voice_of="occom")],
    rights="Public Domain (pd-us-by-date: published 1899; the title page prints no year, and the date is the copyright notice on its verso, 'Copyright, 1899', OCR lines 70-71, with which the preface date and the archive.org record's date agree); " + NIC,
    rights_short="published 1899 by its copyright notice, out of US copyright by date")

I = "someaspectsofrel00walk"
chk(I, 46, r"1897", 2); chk(I, 3170, r"whitfeld|pleased\s+god", 3); chk(I, 2931, r"III", 3); chk(I, 7268, r"INDEX", 2)
add(I, "walker-george-leon_some-aspects-of-the-religious-life-of-new-england_1897.txt",
    "Some Aspects of the Religious Life of New England, with special reference to Congregationalists: lectures delivered on the Carew Foundation before Hartford Theological Seminary in 1896",
    "George Leon Walker, D.D. (title page)",
    "New York, Boston, Chicago: Silver, Burdett and Company (title page)",
    "1897 (title page, OCR line 46; copyright notice of 1897 at 49-50)", 1897, NIC, "eng",
    "clean; inside the extract from Nathan Cole the OCR reads h as b in places ('tbat', 'bis'). A Princeton Theological Seminary bookplate stands at OCR lines 1-11.",
    "Five lectures. Preface at OCR lines 56-90, dated Hartford, 1 February 1897. Lecture I, the Puritan period, at 123; II, the Puritan decline, at 1455; III, the Great Awakening, at 2931; IV, the evangelical reawakening, at 4539; V, the current period, at 5981; index from 7268. In lecture III Walker prints part of the farmer Nathan Cole's account of hearing Whitefield, which he calls a 'hitherto unpublished narrative': his introduction at 3156-3169, Cole's words at 3170-3274, in Cole's own spelling.",
    "George Leon Walker", NENG,
    "Wanted row A131: Nathan Cole's account of hearing Whitefield, in the extract Walker printed (no full printing by 1930 was found).",
    [row("walker-religious-life-of-new-england", "Walker, Some Aspects of the Religious Life of New England (1897)", "walker-george-leon",
         "the five lectures at OCR lines 123-7267; lecture III, the Great Awakening, at 2931-4538", [NENG], "context", "provisional", "eng",
         doc((1897, 1897), "title page: 1897"),
         "Lectures given at Hartford Theological Seminary in 1896 on New England's religious history. A late survey from inside the Congregational churches."),
     row("cole-nathan-spiritual-travels-extract-in-walker", "Nathan Cole, 'Spiritual Travels', on hearing Whitefield: the extract Walker prints", "cole-nathan",
         "the extract at OCR lines 3170-3274; Walker's introduction at 3156-3169", [NENG], "tradition", "provisional", "eng",
         doc((1897, 1897), "first printed here, in 1897; Walker calls it a 'hitherto unpublished narrative' and does not say when Cole wrote it"),
         "A Connecticut farmer's own words on going to hear Whitefield and the distress that followed. Walker says Cole was a farmer of Kensington parish who became a Separatist (OCR lines 3156-3169). An extract chosen by Walker from a manuscript; the OCR misreads some letters.",
         voice_of="cole-nathan")],
    ruled={"cole-nathan": ("metadata-omission", "Walker introduces the extract at file lines 3168-3181 as the narrative of Nathan Cole; the title page names only Walker.")})

I = "sketchesoflifech00cool"
chk(I, 65, r"8\s*37", 3); chk(I, 763, r"CHAPTER", 3); chk(I, 4132, r"SERMON|Gen", 6); chk(I, 16044, r"THE\s+END", 2); chk(I, 14862, r"Carpenter|SERMON", 8)
add(I, "cooley_sketches-of-the-life-and-character-of-lemuel-haynes_1837.txt",
    "Sketches of the Life and Character of the Rev. Lemuel Haynes, A.M., for many years pastor of a church in Rutland, Vt., and late in Granville, New-York; with some introductory remarks by William B. Sprague, D.D.",
    "Timothy Mather Cooley, D.D. (title page)",
    "New-York: Harper & Brothers, 82 Cliff-St. (title page)",
    "1837 (title page, OCR lines 56-65; copyright entry of 1837 at 68-71)", 1837, NR, "eng",
    "clean, with stray running heads. A Princeton Seminary stamp stands at OCR lines 1-7 and the Internet Archive's 'Digitized by' notice at 11-17.",
    "Eighteen chapters with Haynes's own sermons and letters set inside them. Cooley's preface at OCR lines 74-117, dated Granville, December 1836; contents at 123-310; Sprague's introductory remarks at 319-760, dated Albany, 28 October 1836. Chapter I at 763, II 1338, III 2218, IV 2725, V 3073, VI 3612, VII 3976, X 5874, XI 6488, XII 6654, XIII 7121, XIV 7575, XV 9582, XVI 11783, XVII 12150, XVIII 12700 (the headings of VIII and IX were not found). Haynes's own writing: six letters at 3284-3539; his sermon on Genesis iii. 4, preached at Rutland in 1805 against universal salvation, at 4132-4465; his letter to Hosea Ballou at 4470-5315; more letters in chapters XII, XIV, XV and XVI; in the appendix, from 14854, selections from his printed sermons, with the funeral sermon for Abraham Carpenter at 14862. An elegy at 14571 and reminiscences at 14654-14853. 'The End' at 16044; the publisher's advertisements follow.",
    "Timothy Mather Cooley", NENG,
    "Wanted row A132: Lemuel Haynes, in Cooley's Life with Haynes's own sermons and letters.",
    [row("cooley-life-of-lemuel-haynes", "Cooley, Sketches of the Life and Character of the Rev. Lemuel Haynes (1837)", "cooley",
         "chapters I-XVIII at OCR lines 763-14570; Sprague's remarks at 319-760", [NENG, "the-black-church-in-america"], "context", "provisional", "eng",
         doc((1837, 1837), "title page: 1837; Cooley's preface is dated December 1836"),
         "The Life of Haynes by the pastor of the First Church in Granville, Massachusetts; Cooley calls him 'a coloured man' (OCR line 822). Most of Haynes's ministry falls after this entry's window; the census names him under it."),
     row("haynes-sermons-and-letters-in-cooley", "Lemuel Haynes, sermons and letters as printed in Cooley's Sketches (1837)", "haynes-lemuel",
         "letters at OCR lines 3284-3539; the Rutland sermon on Genesis iii. 4 at 4132-4465; the letter to Hosea Ballou at 4470-5315; the appendix of sermons at 14854-16044", [NENG, "the-black-church-in-america"], "tradition", "provisional", "eng",
         doc((1805, 1837), "the Rutland sermon is headed 30 December 1805 (about OCR line 4132); printed in 1837"),
         "Haynes in his own words: the sermon that answered Ballou, his letters, and sermons his son added. Printed by Cooley and by W. B. Haynes; the texts were not compared with the first printings.",
         voice_of="haynes-lemuel")],
    ruled={"haynes-lemuel": ("metadata-omission", "The title page (file lines 32-83) names Cooley as author and Haynes as the subject. Haynes's own sermons and letters are headed as his inside the chapters and in the appendix, which his son W. B. Haynes says he appended (file lines 16048-16056).")})

I = "sermonsonimporta179401davi"
chk(I, 68, r"CAMPBELL", 2); chk(I, 2979, r"SERMON", 3); chk(I, 21704, r"SERMON", 3); chk(I, 641, r"Rom", 6)
add(I, "davies_sermons-on-important-subjects-v1_campbell1794.txt",
    "Sermons on Important Subjects, by the late reverend and pious Samuel Davies, A.M., sometime President of the College in New-Jersey; in two volumes; the sixth edition, to which are now added three occasional sermons, memoirs and character of the author, and two sermons on occasion of his death by the Rev. Drs. Gibbons and Finley; volume I; second American edition",
    "Samuel Davies (title page)",
    "Philadelphia: printed for Robert Campbell, bookseller (title page)",
    "1794 (title page: 'M.DCC.XCIV.', read on the page image, leaf n6; the OCR reads 'M.DCC.xeiv-' at line 71)", 1794, NIC, "eng",
    "readable, with the long s read as f everywhere; ornament rows are garbled and the last lines of the file are junk. A Princeton Seminary stamp stands at OCR lines 4-21.",
    "The first of two volumes: the matter on Davies's life, then sermons I-XXIV. Publisher's advertisement at OCR line 77; contents at 101-345. Thomas Gibbons's preface to the first edition at 354-568, dated 14 November 1765, quoting Davies's letters. Samuel Finley's funeral sermon on Romans xiv. 7, 8: title at 570-612, text at 641-1469; an appendix on Davies's life by a friend from 1476. Gibbons's two discourses at Haberdashers-Hall, 29 March 1761, from 1698. David Bostwick's character of the author from 2740. Davies's sermons: I at 2979, II 4272, III 5225, IV 6042, V 6930, VI 7680, VII 8347, VIII 8990, IX 9675, X 10263, XI 11355, XII 11936, XIII 12576, XIV 13447, XV 14284, XVI 14909, XVII 15549, XVIII 16330, XIX 17284, XX 18112, XXI 19346, XXII 20213, XXIII 20901, XXIV 21704.",
    "Samuel Davies", NENG,
    "Wanted row A134: Samuel Davies, with the memoirs of him by Finley, Gibbons and Bostwick (vol. 3 of another edition is held; this is vol. 1).",
    [row("davies-sermons-v1-sermons-1-24", "Davies, Sermons on Important Subjects, vol. I: sermons I-XXIV (Philadelphia, 1794)", "davies",
         "sermons I-XXIV at OCR lines 2979-22770", [NENG], "tradition", "provisional", "eng",
         doc((1794, 1794), "this printing's title page reads 1794; the funeral discourses in it are dated 1761"),
         "Davies in his own sermons. Provisional because the census leaves open whether Virginia belongs to this entry."),
     row("davies-sermons-v1-memoirs-by-finley-gibbons-bostwick", "Finley, Gibbons and Bostwick on Samuel Davies: funeral sermons, memoir and character (1761-1765), in Davies's Sermons, vol. I", "davies",
         "Gibbons's preface at OCR lines 354-568; Finley's sermon at 641-1469 and the appendix from 1476; Gibbons's discourses from 1698; Bostwick's character from 2740 to 2978", [NENG], "context", "provisional", "eng",
         doc((1761, 1765), "Gibbons's discourses are dated 29 March 1761 (OCR lines 1710-1716) and his preface 14 November 1765 (line 568)"),
         "What Finley, Gibbons and Bostwick said of him in the years after his death. Not Davies's voice.")])

GL = [("gleanermiscellan01murr", 1, "I", "essays I-XXXIV",
       "Title page at OCR lines 37-71. Dedication to John Adams at 74-216, dated Boston, 15 March 1797; preface at 222-363; contents at 366-500. Essay No. I at 498, II 705, III 1078, IV 1382, V 1959, VI 2422, VII 3017, VIII 3482, IX 3986, X 4471, XI 5149, XIII 6139, XIV 6435, XV 6741, XVI 7064, XVII 7633, XVIII 8013, XIX 8565, XX 8965, XXI 9532, XXII 10173, XXIII 10377, XXIV 10733, XXVI 12125, XXVII 12579, XXX 14855, XXXI 15542, XXXII 15994, XXXIV 17017; the headings of XII, XXV, XXVIII, XXIX and XXXIII were not found. The story of Margaretta begins in No. II and returns in VII-X, XIII and XX. 'End of volume first' at 17576.",
       "readable, with the long s read as f. Cover scraps stand at OCR lines 1-36.", 498, 17576, 71, r"1798",
       "title page: 'Feb. 1798' (OCR lines 64-71); No. I is dated 27 January 1792 (about line 510)", (1792, 1798)),
      ("bim_eighteenth-century_the-gleaner-a-miscellan_murray-judith-sargent_1798_2", 2, "II", "essays XXXV-LXVIII",
       "Title page at OCR lines 19-50. Contents of the second volume at 87-215, Nos. XXXV to LXVIII. No. XXXV from 217. Headings found: XXXVII at 1152, XXXVIII 1970, XLI 4047, XLV 6564, LI 10497, LIV 12689, LVII 13926, LX 15448, LXII 16305, LXIII 16853, LXVII 18671, LXVIII 19098; the other headings were not found in the OCR. Margaretta's letters are Nos. XLI-XLIV. 'End of the second volume' at 19712.",
       "poor: the long s is kept, and the contents and many headings are heavily garbled; the prose can be followed. Cover junk stands at OCR lines 1-18.", 217, 19712, 50, r"1798",
       "title page: 1798 (OCR lines 43-50); essays in it are dated 1794", (1794, 1798)),
      ("gleanermiscellan03murr", 3, "III", "essays LXIX-C",
       "Title page at OCR lines 21-52. Contents at 55-175. Essay No. LXIX at 176, LXX 528, LXXII 1359, LXXIII 2293, LXXV 3990, LXXVI 4810, LXXVII 5075, LXXVIII 5365, LXXIX 5810, LXXX 6137, LXXXI 6665, LXXXII 7213, LXXXIII 7764, LXXXIV 8169, LXXXV 8774, LXXXVI 9228, LXXXVII 9520, LXXXVIII 9969, LXXXIX 10369, XC 10785, XCI 11338, XCIII 12186, XCIV 12546, XCVI 13410, XCVII 13860, XCVIII 14342, XCIX 14944, C 15420; the headings of LXXI, LXXIV, XCII and XCV were not found. Her two plays stand inside the essays: Virtue Triumphant at 1356-3036 and The Traveller Returned at 6662-8771. 'Observations on Female Abilities', Nos. LXXXVIII-XCI, at 9969-12185. The conclusion, 'The Gleaner Unmasked', at 16036-16224; a note to patrons at 16257; errata; the subscribers' names from 16322 to the end.",
       "readable, with the long s read as f. Cover scraps stand at OCR lines 1-18.", 176, 16224, 52, r"1798",
       "title page: 'Feb. 1798'; the contents say the last essays were written in December 1797", (1794, 1798))]
for ident, v, rom, span, cont, ocr, a, b, tl, tp, dsrc, yrs in GL:
    chk(ident, tl, tp, 4)
    chk(ident, 9969 if v == 3 else a, r"N|GLEANER|Observations", 12)
    rows = [row("gleaner-v%d-essays" % v, "Judith Sargent Murray ('Constantia'), The Gleaner, vol. %s: %s (1798)" % (rom, span), "murray-judith-sargent",
                "the essays at OCR lines %d-%d" % (a, b), [UNIV], "tradition", "provisional", "eng", doc(yrs, dsrc),
                "Essays, a serial story and plays, printed under the name Constantia. The wanted list places her among the Universalists; her faith shows in the essays only in passing, and her life appears indirectly.")]
    if v == 3:
        rows.append(row("gleaner-v3-observations-on-female-abilities", "Judith Sargent Murray ('Constantia'), The Gleaner, Nos. LXXXVIII-XCI: Observations on Female Abilities (1798)", "murray-judith-sargent",
                        "Nos. LXXXVIII-XCI at OCR lines 9969-12185", [UNIV], "tradition", "provisional", "eng", doc((1797, 1798), "title page: 'Feb. 1798'; she says at OCR lines 9972-9990 that these add to her earlier essay on the equality of the sexes"),
                        "Her four essays on women's abilities."))
    add(ident, "murray-judith-sargent_the-gleaner-v%d_1798.txt" % v,
        "The Gleaner: a miscellaneous production; in three volumes; by Constantia; vol. %s" % rom,
        "Judith Sargent Murray (title page: 'By Constantia'; the archive.org record gives the name)",
        "Boston: printed by I. Thomas and E. T. Andrews, Faust's Statue, No. 45, Newbury-Street (title page)",
        "1798 (title page, OCR line %d%s)" % (tl, "; 'Feb. 1798'" if v != 2 else ""), 1798, NR, "eng", ocr, cont,
        "Judith Sargent Murray", UNIV,
        "Wanted row A138: Judith Sargent Murray in her own essays (The Gleaner, three volumes, under the name Constantia).",
        rows,
        ruled={"murray-judith-sargent": ("pseudonymous", "The title page reads 'By Constantia'. The archive.org record names Judith Sargent Murray; in the conclusion of vol. III, 'The Gleaner Unmasked', the author drops the mask (vol. III file lines 16048-16236).")})

I = "posthumousworkso00mcgr"
chk(I, 46, r"1837", 2); chk(I, 222, r"NARRATIVE|REVIVAL", 6); chk(I, 488, r"M.?GREADY", 4); chk(I, 1391, r"SERMON", 3); chk(I, 25534, r"LECTURE|SPIRIT|INTEMPERANCE|LIQUOR", 8)
add(I, "mcgready_posthumous-works_smith1837.txt",
    "The Posthumous Works of the reverend and pious James M'Gready, late minister of the gospel in Henderson, Ky.; edited by the Reverend James Smith; two volumes in one",
    "James McGready (title page: 'James M'Gready'); edited by James Smith (title page)",
    "Nashville, Tennessee: printed and published at J. Smith's steam press (title page)",
    "1837 (title page, OCR lines 45-46; the copyright entry at 49-69 is dated 1833)", 1837, NIC, "eng",
    "fair: modern type with stray errors; scan junk follows the last line.",
    "His account of the revival and forty-two sermons. Title page at OCR lines 19-46; the editor's preface at 72-139; John Andrews's sketch of his character at 140-221. 'A Short Narrative of the Revival of Religion in Logan County', in a letter to a friend dated Logan County, Kentucky, 23 October 1801, at 222-488. Contents at 497-600. Sermon I from 601 (its heading page is missing from the OCR), II at 1391, III 2219, IV 2745, V 3224, VI 3500, VII 4010, VIII 4726, IX 5188, X 5927, XI 6404, XII 6845, XIII 7187, XIV 7476, XV 8263, XVI 8668, XVII 9138, XVIII 9473, XIX 9752, XX 10131, XXI 10938, XXII 11382, XXIII 12095, XXIV 13088, XXV 13763, XXVI 14346, XXVII 15255, XXVIII 15993, XXIX 16529, XXX 16990, XXXI 17489, XXXII 18065, XXXIII 18625, XXXIV 19568, XXXVI 20615, XXXVII 21189, XXXVIII 22443, XXXIX 22810, XL 23400, XLI 23920, XLII 24609; the heading of XXXV and the second volume's title page were not found. A lecture on spirituous liquors at 25534-26568 and an address from 26569 to the end.",
    "James McGready", SGA,
    "Wanted row A157: James McGready, his own narrative of the Logan County revival and his sermons.",
    [row("mcgready-narrative-of-the-revival-1801", "McGready, A Short Narrative of the Revival of Religion in Logan County (letter of 23 October 1801)", "mcgready",
         "the Narrative at OCR lines 222-488", [SGA], "tradition", "assigned", "eng",
         doc((1801, 1801), "headed 'In a Letter to a Friend, dated Logan County, Ky., Oct. 23, 1801' (OCR line 222 onward)"),
         "McGready's own account of the Logan County revival, written in 1801. A bracketed note at about line 456 is the editor's."),
     row("mcgready-sermons", "McGready, Posthumous Works: sermons I-XLII, a lecture and an address (ed. Smith, 1837)", "mcgready",
         "the sermons at OCR lines 601-25533; the lecture and address at 25534-26861", [SGA], "tradition", "provisional", "eng",
         doc((1837, 1837), "title page: 1837; the sermons are not dated in the contents"),
         "His sermons, printed after his death by James Smith. How far Smith edited the manuscripts was not checked.")])

I = "declarationaddre00campiala"
chk(I, 48, r"1906", 1); chk(I, 152, r"I8OQ", 2); chk(I, 174, r"DECLARATION", 2); chk(I, 313, r"ADDRESS", 2); chk(I, 1277, r"APPENDIX", 3); chk(I, 2956, r"POSTSCRIPT", 3)
add(I, "campbell-thomas_declaration-and-address-centennial-edition_1906.txt",
    "Declaration and Address of the Christian Association of Washington; Centennial edition",
    "Thomas Campbell (Centennial title page)",
    "Pittsburgh: Centennial Bureau, 203 Bissell Block; printed by the Record Publishing Company, Coraopolis, Pa. (Centennial title page)",
    "1906 (Centennial title page, OCR line 48; the archive.org record says 1908, a year that stands only in the unsigned introduction, line 100)", 1906, NIC, "eng",
    "clean on the text of 1809; the introduction and the ornamental title page are garbled in places. The Internet Archive's 'Digitized by' notice stands at OCR lines 17-24 and library stamps at the end.",
    "A reprint of the print of 1809 which, by its own title page, 'follows the original, page for page, line for line, letter for letter' (OCR lines 41-45). The unsigned Centennial introduction at 55-123. The 1809 title page at 125-152 (Washington, Pa., printed by Brown and Sample); the preamble, with the meetings of 17 August and 7 September 1809, at 155-170. The Declaration at 174-312. The Address at 313-1276. The Appendix at 1277-2955. The Postscript at 2956; an advertisement of Campbell's planned works and the errata at about 3060-3086. 'Centennial Aims' at 3087 and the Centennial committee's address at 3157 are of 1906.",
    "Thomas Campbell", STONE,
    "Wanted row A158: Thomas Campbell's Declaration and Address of 1809, in the line-for-line reprint of 1906.",
    [row("campbell-thomas-declaration-and-address-1809", "Thomas Campbell, Declaration and Address of the Christian Association of Washington (1809; Centennial reprint, 1906)", "campbell-thomas",
         "the Declaration at OCR lines 174-312; the Address at 313-1276; the Appendix at 1277-2955; the Postscript from 2956", [STONE], "tradition", "assigned", "eng",
         doc((1809, 1809), "the reprinted title page's year stands at OCR line 152, garbled as 'I8OQ.'; the preamble dates the meetings 17 August and 7 September 1809 (lines 155-172)"),
         "The founding paper of the Campbell movement, read in a reprint that claims to follow the first print letter for letter. The claim was not tested against a copy of 1809. The introduction and the two Centennial pieces at the end are of 1906 and are not Campbell's.")],
    ruled={"campbell-thomas": ("metadata-omission", "The Centennial title page (file lines 16-26) names Thomas Campbell. The 1809 title page reprinted inside (file lines 137-164) names the Christian Association of Washington and no author.")})

# ---------------- Catholic Europe and the Jesuits ----------------
I = "bub_gb_S09fcFzVIu4C"
chk(I, 29, r"NAPOLI\s+MDCCLVIII"); chk(I, 11146, r"C A T A", 3); chk(I, 16256, r"APPENDICE", 3); chk(I, 16613, r"ORAZIONE", 3); chk(I, 17812, r"INDICE", 3)
add(I, "soli-muratori_vita-del-proposto-lodovico-antonio-muratori-ita_napoli1758.txt",
    "Vita del proposto Lodovico Antonio Muratori, già bibliotecario del serenissimo signor Duca di Modena, descritta dal proposto Gian-Francesco Soli Muratori suo nipote; con la giunta in questa edizione napoletana di alcune lettere scritte dallo stesso proposto Lodovico Antonio Muratori a diversi letterati napoletani",
    "Gian-Francesco Soli Muratori (title page, read on the page image)",
    "Naples: presso Giuseppe Ponzelli (title page, read on the page image)",
    "1758 (title page: 'IN NAPOLI MDCCLVIII', read on the page image, leaf n4, and at OCR line 29; the OCR drops the first title lines)", 1758, PDM, "ita",
    "readable in the body, with the long s read as f; the first leaves (OCR lines 60-170) are heavily garbled. Google's 'Digitized by' stamp recurs on page breaks, about fifty times.",
    "The nephew's Life, with documents. Soli's preface to the reader at about OCR lines 120-235; table of chapters at 246-460. The Vita from 649: chapter II at 1088, III 1508, IV 2258, V 2403, VII 2633, VIII 2972, IX 3791, X 7762, XI 8122, XII about 8292, XIII 8487, XIV 8993, XV 9546, the last chapter at 10333 (the headings of I and VI are garbled). Catalogue of Muratori's works at 11146. Appendix of documents from about 11532, numbered I to XXXIII and beyond: letters to and from Muratori by Marsigli, Zeno, Querini, Mazzocchi and others. Second appendix, a reply to Fontanini, at 16256. Funeral oration at 16613. Index of matters from 17812 to the end. Where the Naples edition's added letters stand was not found.",
    "Gian-Francesco Soli Muratori", ANCIEN,
    "Wanted row A146: Lodovico Antonio Muratori, in the Life by his nephew (Naples, 1758; the Venice 1756 scan shows no year).",
    [row("soli-muratori-vita-del-muratori", "Soli Muratori, Vita del proposto Lodovico Antonio Muratori (Naples, 1758): the Life", "soli-muratori",
         "the Vita at OCR lines 649-11145; the catalogue of works at 11146", [ANCIEN], "tradition", "provisional", "ita",
         doc((1756, 1758), "this edition's title page reads 1758 and calls itself the Naples edition; the funeral oration it prints is for 23 January 1751"),
         "Muratori's nephew writes the Life soon after his death. A family voice from inside the Italian church of the day."),
     row("soli-muratori-vita-appendix-of-letters", "Soli Muratori, Vita del proposto Lodovico Antonio Muratori (Naples, 1758): the appendices of documents and letters", "soli-muratori",
         "the appendix of documents at OCR lines 11532-16255; the second appendix at 16256; the funeral oration at 16613-17811", [ANCIEN], "context", "provisional", "ita",
         doc((1705, 1758), "the letters run from about 1705 to the 1730s; printed in 1758"),
         "Letters to and from Muratori and pieces by other hands. Each has its own writer, named at its head; none is Soli's.")])

I = "A118051"
chk(I, 35, r"MDCCXLIII", 1); chk(I, 958, r"A\s*P\s*I\s*T\s*O\s*L\s*O|CAPITOLO", 2); chk(I, 9488, r"LET", 3); chk(I, 10978, r"FINE", 2)
add(I, "muratori_il-cristianesimo-felice-nelle-missioni-del-paraguai-ita_1743.txt",
    "Il cristianesimo felice nelle missioni de' padri della Compagnia di Gesù nel Paraguai",
    "Lodovico Antonio Muratori, bibliotecario del serenissimo signor Duca di Modena (title page)",
    "Venice: presso Giambatista Pasquali (title page)",
    "1743 (title page: 'IN VENEZIA, MDCCXLIII', OCR line 35)", 1743, PDM, "ita",
    "readable, with the long s read as f throughout, running heads in the body and words broken at line ends; the opening of chapter I is garbled by a map plate (OCR lines 940-955).",
    "The first part of the work (the title page gives no part number; the second part came out in 1747). To the readers at OCR lines 286-440; the Venetian licence, dated 31 December 1742, at about 440-478; table of chapters at 485-570. Chapter I at 958, II 1173, III 1380, IV 1792, V 2200, VI 2422, VII 2806, VIII 3034, IX 3319, X 3564, XI 3771, XII 3975, XIII 4210, XIV 4429, XV 4696, XVI 4956, XVII 5118, XVIII 5497, XIX 5834, XX 6218, XXI 6615, XXII 6967, XXIII 7485. Then three letters of the Jesuit Gaetano Cattaneo to his brother in Modena: the first at 7786, the second at 9488, the third, from the Reduction of Santa Maria, 25 April 1730, at 9984. 'Il fine' at 10978.",
    "Lodovico Antonio Muratori", SJ,
    "Wanted row A146: Muratori on the Jesuit missions of Paraguay, the book the census names for the Society of Jesus, 1650-1814.",
    [row("muratori-cristianesimo-felice-chapters", "Muratori, Il cristianesimo felice nelle missioni del Paraguai, part 1: chapters I-XXIII (1743)", "muratori",
         "chapters I-XXIII at OCR lines 958-7785", [SJ], "context", "provisional", "ita",
         doc((1743, 1743), "title page: 'MDCCXLIII'; the licence is dated 31 December 1742 (OCR line 465)"),
         "The Duke of Modena's librarian describes the Paraguay reductions from the missionaries' letters and reports. An admirer's account from outside the Society, not its own voice."),
     row("cattaneo-letters-from-paraguay-in-muratori", "Gaetano Cattaneo, S.J., three letters from Buenos Aires and the Paraguay reductions (1729-1730), in Muratori's Cristianesimo felice", "cattaneo-gaetano",
         "the three letters at OCR lines 7786-10978", [SJ], "tradition", "provisional", "ita",
         doc((1729, 1730), "the third letter is dated from the Reduction of Santa Maria, 25 April 1730 (OCR line 9984 onward)"),
         "A Jesuit missionary writes home to his brother about the voyage and the reductions. Printed by Muratori thirteen years later; his editing was not checked.",
         voice_of="cattaneo-gaetano")],
    ruled={"cattaneo-gaetano": ("metadata-omission", "The title page names only Muratori. The three letters are headed as letters of Father Gaetano Cattaneo of the Society of Jesus to his brother (file lines 7798, 9500 and 9996).")})

I = "bim_eighteenth-century_a-relation-of-the-missio_muratori-lodovico-anton_1759"
chk(I, 12, r"MISSIONS"); chk(I, 833, r"CHAP", 3); chk(I, 13619, r"Extra", 4); chk(I, 10217, r"Cajetan", 6)
add(I, "muratori_relation-of-the-missions-of-paraguay_1759.txt",
    "A Relation of the Missions of Paraguay, wrote originally in Italian by Mr. Muratori, and now done into English from the French translation",
    "Lodovico Antonio Muratori (title page: 'Mr. Muratori'); the English and French translators are not named",
    "London: printed for J. Marmaduke in Long-Acre (title page, read on the page image)",
    "1759 (title page: 'M.DCC.LIX.', read on the page image, leaf n0; the OCR reads 'M. Dec. LIX.' at line 39)", 1759, NR, "eng",
    "clean in the body, with the long s kept; the title page and chapter headings are heavily garbled and running heads are often misread. Cover noise stands at OCR lines 1-8.",
    "An English version, made from the French, of the Cristianesimo felice. The French translator's advertisement at OCR lines 62-418, saying he retrenched and rearranged; Muratori's preface at 419-654; to the reader at 655. Twenty chapters: I at 833, II 1111, IV 2199, V 2634, VII 4097, VIII 4593, IX 4881, XI 5424, XII 5654, XV 6620, XVI 7134, XVIII 7981, XX 9082, ending at 10202 (the other headings were not found). Three letters of Father Cajetan Cattaneo: the first, Buenos Ayres, 18 May 1729, at 10217; the second at about 11742; the third, 25 April 1730, at 12324. An extract from the voyage of the Capuchin Florentin de Bourges (1712), from the Lettres édifiantes, at 13619-14274, where it stops short. Table of contents at 14277-14421.",
    "Lodovico Antonio Muratori", SJ,
    "Wanted row A146: Muratori on the Paraguay missions in the English of 1759, for readers without Italian.",
    [row("muratori-relation-of-the-missions-of-paraguay-english", "Muratori, A Relation of the Missions of Paraguay (English from the French, 1759)", "muratori",
         "the chapters at OCR lines 833-10202; Cattaneo's letters at 10217-13618; the extract from Florentin de Bourges at 13619-14274", [SJ], "context", "provisional", "eng",
         doc((1759, 1759), "title page: 'M.DCC.LIX.'"),
         "A translation of a translation: the French translator says he cut and reordered Muratori, and the English follows the French. Use the Italian of 1743 to quote Muratori or Cattaneo; use this to read them in English.")])

for t, ident, tl, cont, rows in [
    (1, "laviededomarmand01mars", 29,
     "Books I-III. Title page at OCR lines 4-31. Epistle to the king at 48-330; the author's avertissement at 341-795; table of chapters from 800. Book I: chapter I at 1175, to 'Fin du premier Livre' at 6605 (twenty-one chapters). Book II at 6612-12204 (fifteen chapters). Book III at 12211-17361 (fifteen chapters). 'Fin du Tome premier' at 17362. Letters and documents are quoted inside the chapters.",
     [("marsollier-vie-de-rance-t1", "Marsollier, La vie de dom Armand-Jean Le Bouthillier de Rancé, tome 1: books I-III (new edition, 1758)", "marsollier",
       "books I-III at OCR lines 1175-17362", "tradition", (1758, 1758), "this edition's title page reads 1758 and 'Nouvelle Edition'; the year of the first edition is not on it",
       "A canon of Uzès writes the Life of the reformer of La Trappe. An admiring Life from inside the French church, read in a new edition of 1758.", None)]),
    (2, "laviededomarmand02mars", 43,
     "Books IV-VI and Rancé's Pensées. Title page at OCR lines 13-45. Table at 61-384. Approbation, Paris, 27 May 1758, at 388; privilege, 11 August 1758, at 401-517. Book IV at 518-7265; Book V at 7273-12451; Book VI at 12460-17855, where the Life ends ('Fin'). Then an avertissement at 17860 and 'Pensées de l'abbé de la Trappe sur divers sujets de piété, tirées de ses lettres spirituelles' at 17913-20952.",
     [("marsollier-vie-de-rance-t2", "Marsollier, La vie de dom Armand-Jean Le Bouthillier de Rancé, tome 2: books IV-VI (new edition, 1758)", "marsollier",
       "books IV-VI at OCR lines 518-17855", "tradition", (1758, 1758), "this edition's title page reads 1758; approbation of 27 May 1758 (OCR line 388)",
       "The second half of the Life, to Rancé's death. See the note on tome 1.", None),
      ("rance-pensees-in-marsollier-t2", "Rancé, Pensées sur divers sujets de piété, tirées de ses lettres spirituelles (in Marsollier's Vie, tome 2, 1758)", "rance",
       "the Pensées at OCR lines 17913-20952; the avertissement before them at 17860", "tradition", (1758, 1758), "printed in 1758; the extracts are from Rancé's letters and are not dated",
       "Rancé's own sentences on the spiritual life, cut from his letters by an editor. The letters they come from are not named line by line.", "rance")])]:
    chk(ident, tl, r"LVII", 1)
    chk(ident, 17362 if t == 1 else 17855, r"Fin|FIN", 2)
    if t == 2:
        chk(ident, 17913, r"PENS", 4); chk(ident, 388, r"APPROBATION", 2)
    add(ident, "marsollier_vie-de-dom-armand-jean-le-bouthillier-de-rance-t%d-fra_1758.txt" % t,
        "La vie de dom Armand-Jean Le Bouthillier de Rancé, abbé régulier et réformateur du monastère de la Trappe, de l'étroite observance de Cîteaux; nouvelle édition; tome %s" % ("premier" if t == 1 else "second"),
        "Jacques Marsollier (title page: 'Par M. l'Abbé de Marsollier, Chanoine de l'Eglise Cathédrale d'Usez')",
        "Paris: chez Savoye, rue Saint Jacques, à l'Espérance (title page)",
        "1758 (title page: 'M. DCC. LVIII.', read on the page image, leaf n6; the OCR reads '%s' at line %d)" % ("M. Dec LVIIL" if t == 1 else "M, Dec. LVIIL", tl), 1758, NR, "fra",
        "clean French with the long s read as f, double-spaced words and running heads in the text.",
        cont, "Jacques Marsollier", ANCIEN,
        "Wanted row A147: Rancé and La Trappe, in Marsollier's Life (two volumes, the edition of 1758).",
        [row(s, w, a, loc, [ANCIEN], role, "provisional", "fra", doc(yrs, dsrc), note, voice_of=vo) for (s, w, a, loc, role, yrs, dsrc, note, vo) in rows])

for t, ident, tl, yl, cont, rows in [
    (1, "memoirespourser01fontgoog", 160, 167,
     "Title page at OCR lines 149-167. The unnamed publisher's avertissement at 173; a short Life of Fontaine at 305-610; a short history of the abbey of Port-Royal from about 613. Antoine Le Maître's memoir on the persons of Port-Royal at 3681-4992; a memoir on the schools of Port-Royal at 4993-5495. Fontaine's own Mémoires, with his preface, from 5496: Première partie at 5617, Seconde partie at 11941. Table of names and matters of the first volume from 24816.",
     [("fontaine-memoires-t1-parts-1-2", "Fontaine, Mémoires pour servir à l'histoire de Port-Royal, tome 1: parts 1 and 2 (1738)", "fontaine-nicolas",
       "Fontaine's Mémoires at OCR lines 5496-24815: part 1 from 5617, part 2 from 11941", "tradition",
       "Fontaine's own memories of Port-Royal and its solitaires. Printed in 1738 by editors who are not named."),
      ("fontaine-memoires-t1-prefatory-pieces", "Mémoires pour servir à l'histoire de Port-Royal, tome 1 (1738): the Life of Fontaine, the short history of Port-Royal, Le Maître's memoir and the memoir on the schools", "fontaine-nicolas",
       "the Life of Fontaine at OCR lines 305-610; the short history from 613; Le Maître's memoir at 3681-4992; the memoir on the schools at 4993-5495", "context",
       "Pieces the editors of 1738 set before Fontaine's text. The Life and the history are unsigned; Le Maître's memoir is his own and belongs to Port-Royal's first generation.")]),
    (2, "memoirespourser00fontgoog", 117, 123,
     "Title page at OCR lines 108-123. Troisième partie from 145; Quatrième partie from 13021. Table of names and matters of the second volume from 26484. No avertissement in this volume.",
     [("fontaine-memoires-t2-parts-3-4", "Fontaine, Mémoires pour servir à l'histoire de Port-Royal, tome 2: parts 3 and 4 (1738)", "fontaine-nicolas",
       "part 3 at OCR lines 145-13020; part 4 at 13021-26483", "tradition",
       "The second half of his memoirs, to the scattering of Port-Royal. See the note on tome 1.")])]:
    chk(ident, tl, r"T\s*O\s*M\s*E", 1); chk(ident, yl, r"XXXV", 1)
    chk(ident, 5617 if t == 1 else 13021, r"PARTIE", 3)
    add(ident, "fontaine-nicolas_memoires-pour-servir-a-l-histoire-de-port-royal-t%d-fra_1738.txt" % t,
        "Mémoires pour servir à l'histoire de Port-Royal, par M. Fontaine; tome %s" % ("premier" if t == 1 else "second"),
        "Nicolas Fontaine (title page: 'Par M. Fontaine')",
        "Cologne: aux dépens de la Compagnie (title page)",
        ("1738 (title page: 'M DCC XXXVIII', OCR line 167; the archive.org record says Utrecht, 1739)" if t == 1 else
         "1738 (title page: 'MDCC XXXVIII', read on the page image, leaf n10; the OCR reads 'MDCG XXXVUl.' at line 123; the archive.org record says Utrecht, 1739)"), 1738, NIC, "fra",
        "moderately clean French with the long s read as f and some ligature errors; marginal references run into the lines. Google's sheet, in English and French, stands among the first %d OCR lines." % (110 if t == 1 else 98),
        cont, "Nicolas Fontaine", PR,
        "Wanted row A148: Fontaine's memoirs of Port-Royal, which the census names for Port-Royal Jansenism.",
        [row(s, w, a, loc, [PR], role, "provisional", "fra", doc((1738, 1738), "title page: 1738; when Fontaine wrote was not read in the volume"), note) for (s, w, a, loc, role, note) in rows],
        ruled={"fontaine-nicolas": ("metadata-omission", "The title page reads 'Par M. Fontaine' and gives no first name; the archive.org record names Nicolas Fontaine.")})

I = "memoirespourser00fossgoog"
chk(I, 133, r"XXXIX", 1); chk(I, 1557, r"LIVRE", 2); chk(I, 20690, r"LIVRE", 2); chk(I, 24422, r"TABLE", 2)
add(I, "du-fosse_memoires-pour-servir-a-l-histoire-de-port-royal-fra_1739.txt",
    "Mémoires pour servir à l'histoire de Port-Royal, par M. du Fossé",
    "Pierre Thomas du Fossé (title page: 'Par M. du Fossé')",
    "Utrecht: aux dépens de la Compagnie (title page)",
    "1739 (title page: 'M DCC XXXIX', read on the page image, leaf n6; the OCR reads 'M Dec XXXIX' at line 133)", 1739, NIC, "fra",
    "readable French with garbles, the long s read as f; a Latin passage in two columns near the end runs together. Google's sheet, in English and French, stands at OCR lines 1-110.",
    "One volume in four books. The editors' avertissement at OCR lines 175-510; a Life of du Fossé at 514-1540. The Mémoires from 1547: Livre premier at 1557, Livre second at 9223, Livre troisième at 14855, Livre quatrième at 20690. Table of chapters from 24422 to the end. Many chapter headings were found and some were not; the books' heading lines are sure.",
    "Pierre Thomas du Fossé", PR,
    "Wanted row A148: du Fossé's memoirs of Port-Royal, which the census names for Port-Royal Jansenism.",
    [row("du-fosse-memoires", "Du Fossé, Mémoires pour servir à l'histoire de Port-Royal (1739)", "du-fosse",
         "books I-IV at OCR lines 1557-24421", [PR], "tradition", "provisional", "fra",
         doc((1697, 1739), "the editors' Life says he began the memoirs at the end of 1697 and died in 1698 (OCR lines 1202 and 1300); title page: 1739"),
         "Du Fossé's own memories of Port-Royal, written at the end of his life. Printed forty years after his death by editors who are not named."),
     row("du-fosse-memoires-editors-life", "Mémoires de du Fossé (1739): the editors' avertissement and Life of du Fossé", "du-fosse",
         "the avertissement at OCR lines 175-510; the Life at 514-1540", [PR], "context", "provisional", "fra",
         doc((1739, 1739), "title page: 1739"),
         "The editors of 1739 on the author. Unsigned; later than the entry's window.")])

I = "bub_gb_GmCin_UcwIcC"
chk(I, 62, r"X\s*C", 1); chk(I, 54, r"TOME\s+PREMIER", 1); chk(I, 5621, r"EVANGILE|MATTH", 10); chk(I, 37306, r"EVANGILE|MARC", 10)
add(I, "quesnel_nouveau-testament-avec-des-reflexions-morales-t1-fra_1693.txt",
    "Le Nouveau Testament en françois, avec des réflexions morales sur chaque verset, pour en rendre la lecture plus utile et la méditation plus aisée; nouvelle édition augmentée; imprimé par l'ordre de Monseigneur l'évêque et comte de Châlons; tome premier",
    "The title page names no author; the archive.org record credits Pasquier Quesnel",
    "Paris: chez André Pralard, rue Saint Jacques, à l'Occasion (title page)",
    "1693 (title page: 'M. DC. XCIII.', read on the page image, leaf n4; the OCR reads 'M. D C. X C 1 1 1.' at line 62)", 1693, PDM, "fra",
    "clean French in single-column pages, the long s mostly read as s; where the Gospel text and the reflections stand in two columns they run together (for example near OCR line 42400). One Google stamp line stands at OCR line 12.",
    "The first volume: Matthew and Mark. Title page at OCR lines 24-63. The mandement of Félix, bishop of Châlons, at 66-142, dated 9 November 1671; the doctors' approbations at 147-236 (Paris, 1687); an extract of the privilege at 238-277. The preface of this new edition, on the Gospels, at 278-1280. Tables of the epistles and Gospels for the church year at 1283-5100; table of chapters at 5107-5614. The Gospel according to Matthew, text and reflections, at 5621-37303. The Gospel according to Mark at 37306-56513. Luke and John are in later volumes, not taken.",
    "Pasquier Quesnel", PR,
    "Open-Gaps 225, Library wanted: Quesnel's Réflexions morales, the book Unigenitus condemned (tome 1, the edition of 1693).",
    [row("quesnel-reflexions-morales-matthew-mark", "Quesnel, Le Nouveau Testament en françois avec des réflexions morales, tome 1: Matthew and Mark (1693)", "quesnel",
         "Matthew at OCR lines 5621-37303; Mark at 37306-56513; the preface at 278-1280", [PR], "tradition", "provisional", "fra",
         doc((1693, 1693), "title page: 'M. DC. XCIII.'"),
         "Verse-by-verse reflections on the Gospels, in the enlarged edition printed by order of the bishop of Châlons. The title page does not name Quesnel; the attribution is the record's."),
     row("quesnel-reflexions-morales-as-condemned-text", "Quesnel, Réflexions morales, tome 1 (1693), as the book condemned by Unigenitus", "quesnel",
         "Matthew at OCR lines 5621-37303; Mark at 37306-56513", [ANCIEN], "context", "needs-ruling", "fra",
         doc((1693, 1693), "title page: 'M. DC. XCIII.'"),
         "The bull Unigenitus (1713) drew 101 propositions from this work. Which edition the bull's wording follows was not checked against this volume.")],
    ruled={"quesnel": ("metadata-omission", "The title page (file lines 36-75) names no author; it says the work is printed by order of the bishop of Châlons. The archive.org record credits Pasquier Quesnel.")})

DOB = [("accountofabipone18221dobr", 1, "I", 89, 476, 15316, "the Prefatory Book on the state of Paraguay",
        "Title page at OCR lines 60-89. The translator's preface at 99-272: a note on the author's life, long quotations from his Latin preface, and the translator's account of what was left out (236-272). Contents at 274-466. The Prefatory Book on the State of Paraguay from 476 to 15316, without numbered chapters or section headings in the body; the thirty Guarany towns from about 871; the herb of Paraguay at about 3845. 'End of Vol. I.' at 15317.",
        "clean English ('pubhcation'-type slips only). A Brown University bookplate stands at OCR lines 1-58.", NIC),
       ("cu31924104090935", 2, "II", 78, 249, 15692, "Part II, chapters I-XLIII: the Abipones' land, customs and beliefs",
        "Title page at OCR lines 46-78. Contents at 91-240. 'History of the Abipones, Part II' from 241: chapter I at 249, II 470, III 593, IV 837, V 1006, VI 1227, VII 1558, VIII 2114, IX 2452, X 3171, and on to XLI at 14553 and the last two chapters at 15054 and 15482. 'End of Vol. II.' at 15693. No preface or index.",
        "clean English; running heads appear in the text. A Cornell University Library gift sheet stands at OCR lines 1-45.", NR),
       ("cu31924104095033", 3, "III", 72, 295, 14333, "Part III, chapters I-XLVI: the wars and the Jesuit colonies",
        "Title page at OCR lines 41-72. Contents at 90-282. 'History of the Abipones, Part III' from 283: chapter I at 295, II 495, III 721, IV 998, V 1225, VI 1730, VII 2099, VIII 2458, IX 2818, X 3383; chapter XI, the Jesuits' attempts to bring the Abipones to the Catholic religion, at 3658; XII, a colony for the Mocobios, at 4033; XIII, the first colony of St. Jeronymo, at 4553; and on to XLV at 13200 and XLVI, the gains from the colonies, at 13733. 'The End' at 14333.",
        "clean English. A Cornell University Library gift sheet stands at OCR lines 1-40.", NR)]
for ident, v, rom, yl, a, b, span, cont, ocr, extra in DOB:
    chk(ident, yl, r"1822", 1); chk(ident, a, r"PREFATORY|CHAPTER", 3)
    add(ident, "dobrizhoffer_account-of-the-abipones-v%d_1822.txt" % v,
        "An Account of the Abipones, an equestrian people of Paraguay; from the Latin of Martin Dobrizhoffer, eighteen years a missionary in that country; in three volumes; vol. %s" % rom,
        "Martin Dobrizhoffer (title page); the translator is not named",
        "London: John Murray, Albemarle Street (title page)",
        "1822 (title page, OCR line %d)" % yl, 1822, extra, "eng", ocr, cont,
        "Martin Dobrizhoffer", SJ,
        "Open-Gaps 181, Library wanted: Dobrizhoffer on the Abipones and the Paraguay missions, in the English of 1822.",
        [row("dobrizhoffer-account-of-the-abipones-v%d" % v, "Dobrizhoffer, An Account of the Abipones, vol. %s: %s (English, 1822)" % (rom, span), "dobrizhoffer",
             "OCR lines %d-%d" % (a, b), [SJ], "tradition", "provisional", "eng",
             doc((1784, 1822), "the Latin was printed at Vienna in 1784; this English title page reads 1822"),
             "A Jesuit missionary's own account of eighteen years in Paraguay, written in exile after the Society's suppression. An English translation whose preface says it leaves passages out (vol. I, OCR lines 236-272); check the Latin before leaning on a sentence.")])

I = "historiadeabipon00dobr"
chk(I, 55, r"784", 1); chk(I, 697, r"PRODROMUS|LIBER", 3); chk(I, 432, r"Prim", 3)
add(I, "dobrizhoffer_historia-de-abiponibus-pars1-lat_1784.txt",
    "Historia de Abiponibus, equestri bellicosaque Paraquariae natione, locupletata copiosis barbararum gentium, urbium, fluminum, ferarum, amphibiorum, insectorum, serpentium praecipuorum, piscium, avium, arborum, plantarum aliarumque eiusdem provinciae proprietatum observationibus; pars prima",
    "Martin Dobrizhoffer, presbyter, for eighteen years a missionary in Paraguay (title page: 'Authore Martino Dobrizhoffer')",
    "Vienna: typis Josephi nob. de Kurzbek (title page)",
    "1784 (title page: 'Anno 1784.', read on the page image, leaf n6, and at OCR line 55)", 1784, NR, "lat",
    "fairly legible Latin with the long s read as f and scattered garbles. A John Carter Brown Library stamp stands at OCR line 4.",
    "The first of three parts; the title page does not number it, and the index is headed 'Index Primae Partis' (OCR line 432). The author's preface to the reader at about 75-430; index of sections at 430-690. 'Liber prodromus de Paraquariae habitu', the introductory book on the state of Paraguay, from 697 to 21249, with no numbered chapters in the body; the thirty Guarani towns at about 1165-1290. Errata from 21260 to the end. Parts 2 and 3, on the Abipones themselves, were not taken.",
    "Martin Dobrizhoffer", SJ,
    "Open-Gaps 181, Library wanted: Dobrizhoffer in his own Latin (part 1 only; it answers to vol. I of the English).",
    [row("dobrizhoffer-historia-de-abiponibus-pars-1", "Dobrizhoffer, Historia de Abiponibus, pars I: Liber prodromus de Paraquariae habitu (Vienna, 1784)", "dobrizhoffer",
         "the preface at OCR lines 75-430; the Liber prodromus at 697-21249", [SJ], "tradition", "provisional", "lat",
         doc((1784, 1784), "title page: 'Anno 1784'"),
         "The missionary's own Latin, the text the English of 1822 shortens. Part 1 describes Paraguay and its missions; the Abipones come in the parts not held.")])

VIE = [("sermoensdopanton01viei", 3, "Terceira parte", "terceira", 1683, 30, r"L\s*X\s*X\s*X\s*I\s*I\s*I", "M. DC. LXXXIII.", 610, 40190,
        "Title page at OCR lines 10-31. Censures by Manoel da Graça, Manoel de Santiago and the archbishop at 46-194, dated February and March 1683; licences at 200-271; errata at 272; the list of the fifteen sermons at 562. Sermon I, of the Blessed Sacrament, at 610; II 2286; III 5197; IV, of St. Augustine, 7373; V 11003; VI 13323; VII, of St. Anthony, 16072; VIII 18670; IX 21586; X, of the Good Thief, 23670; XI, of the Mandato, 26418; XII 29203; XIII 31967; XIV, for the success of the arms of Portugal against Holland, 34809; XV 37110. The text ends at 40190 ('Finis' at 40193); indexes of Scripture and of matters follow to the end.", "A library stamp stands at OCR lines 1-6.", "A cuſta de Antonio Leyte Pereyra"),
       ("sermoensdopanton07viei", 5, "Quinta parte", "quinta", 1689, 65, r"L\s*X\s*X\s*X\s*I\s*X", "M.DC.LXXXIX.", 521, 46831,
        "Title page at OCR lines 42-67. Censures at 85-301; licences at 302-402, dated from Bahia, 12 August 1687, to Lisbon, February 1689; the list of the fifteen sermons at 403; errata at 454. Sermon I, of the first Sunday of Advent, at 521; II 5011; III 7474; IV 10290; V, of the Conception, 13369; VI 16126; VII 19365; VIII, of St. Gonçalo, 23549; IX 27463; X 30141; XI 33428; XII 35564; XIII, of St. Barbara, 38771; XIV 41785; XV, of St. John the Baptist, 43740. The text ends at 46831 ('Finis' at 46834); indexes follow to the end.", "Cover scraps stand at OCR lines 1-41.", ""),
       ("sermoensdopanton00viei", 12, "Parte duodécima", "duodecima", 1699, 51, r"Anno", "Anno de 1699", 563, 32594,
        "Half-title, 'Tomo XII', at OCR lines 12-20; title page at 23-53, dedicated on its face to the Immaculate Conception. Licences at 67-518, dated from Bahia, 20 June 1697, to Lisbon, 1698; the list of the sixteen sermons at 519-558. Sermon I, of the Conception, at 563; II, of St. Roch, 2149; III 4695; IV 6553; V, of St. Anthony, 8840; VI 10902; VII 12073; VIII 13779; IX 16443; X 18492; XI, of St. Anthony, preached at Rome, 20286; XII 23703; XIII, preached in Maranhão, 25344; XIV 27271; XV, of St. Joseph, 28897; XVI 30360. 'Laus Deo' at 32597; indexes from 32618; 'Finis' at 36150 and a colophon dated MDCXCIX at the end.", "Cover scraps stand at OCR lines 1-9.", "")]
for ident, p, pname, pslug, y, yl, ypat, yread, a, b, cont, head, _ in VIE:
    chk(ident, yl, ypat, 1); chk(ident, a, r"S\s*E\s*R\s*M|SACRAMENTO|ADVENTO|CONCEI", 8)
    pim = ", read on the page image, leaf n8; the OCR reads 'i6$9-'" if p == 12 else ""
    add(ident, "vieira_sermoens-parte%d-por_%d.txt" % (p, y),
        "Sermoens do P. Antonio Vieira, da Companhia de Jesu, prégador de Sua Magestade; %s" % pname.lower(),
        "António Vieira, S.J. (title page)",
        "Lisbon: na officina de Miguel Deslandes, à custa de Antonio Leyte Pereyra (title page)",
        "%d (title page: '%s', OCR line %d%s)" % (y, yread, yl, pim), y, NR, "por",
        "legible but rough Portuguese: the two columns of each page run into one stream, the long s is read as f, accents are garbled and marginal citations are mixed in. " + head,
        cont, "António Vieira", LATAM,
        "Wanted row A123 and the era 8 handover: Vieira's sermons in the first printing he oversaw (three of the parts; the others were not taken).",
        [row("vieira-sermoens-parte-%d" % p, "Vieira, Sermoens, %s (Lisbon, %d)" % (pname.lower(), y), "vieira",
             "the sermons at OCR lines %d-%d" % (a, b), [LATAM, SJ], "tradition", "provisional", "por",
             doc((y, y), "title page: %d; the sermon headings give the years they were preached" % y),
             "The Jesuit preacher's sermons in the Lisbon edition printed in his lifetime; the Society's licences in the front matter are dated from Bahia. A printed text may differ from what was preached.")])

# ---------------- Volumes that complete held works ----------------
I = "twohundredyearso02pasc"
chk(I, 70, r"1901", 1); chk(I, 97, r"CHAPTER|MADRAS", 4); chk(I, 13997, r"CHAPTER|CEYLON", 4); chk(I, 70486, r"INDEX", 2); chk(I, 61668, r"CHAPTER|CHARTER", 8)
add(I, "pascoe_two-hundred-years-of-the-spg-v2_1901.txt",
    "Two Hundred Years of the S.P.G.: an historical account of the Society for the Propagation of the Gospel in Foreign Parts, 1701-1900 (based on a digest of the Society's records); vol. II",
    "C. F. Pascoe, assistant secretary of the Society (title page)", "London: published at the Society's Office, 19 Delahay Street, Westminster (title page)", "1901 (title page, OCR line 70)", 1901, NR, "eng",
    "clean prose; the roll of missionaries breaks into short column lines and the reference lists are dense and abbreviated. Stray marks stand at the head of the file.",
    "The second of the two volumes as bound, chapters LXXVI to CIV. Asia: chapter LXXVI, Madras, at OCR line 97, opening with the Danish mission at Tranquebar from 1705 and Schwartz; LXXVII Bombay 6165; LXXVIII 7783; LXXIX 9097; LXXX Assam 9175; LXXXI Punjab 9674; LXXXII Burma 11381; LXXXIII 13613; LXXXIV 13828; LXXXV 13896; LXXXVI Ceylon 13997; Borneo and the Straits from 15403; LXXXVIII China 17229; LXXXIX Korea 18495; XC Manchuria 19107; XCI Japan 19227; XCII Western Asia 20777; XCIII Europe 21776. Then the colonial and missionary episcopate at 22505; education 25113; books and translations 28114; medical work 29899; emigrants 31343; intercession 31488; funds and home organization 31590; the bicentenary, church property, anniversary sermons and the Society's offices at 37260-38121 (their numbers are garbled); the roll of the Society's missionaries at 38122-61667; the Charter of 1701 and the Supplemental Charter of 1882, with notes, from 61668; the list of references from 62964; index from 70486. The title page prints 'All rights reserved' at line 72.",
    "C. F. Pascoe", VICT,
    "The era 8 handover's list: the second half of Pascoe's digest, whose vol. 1 is held (Asia, the Society's home work, the roll of missionaries and the Charter of 1701).",
    [row("pascoe-spg-v2-asia-and-europe", "Pascoe, Two Hundred Years of the S.P.G., vol. II: the Asian and European fields", "pascoe",
         "chapters LXXVI-XCIII at OCR lines 97-22501", [VICT], "context", "provisional", "eng",
         doc((1901, 1901), "title page: 1901"),
         "The Society's own digest of its records, field by field. Nearly all of it is the nineteenth century; the opening of the Madras chapter looks back to Tranquebar and Schwartz. A summary written in 1901 by the Society's assistant secretary."),
     row("pascoe-spg-v2-charter-of-1701", "Society for the Propagation of the Gospel, Charter of 1701 and Supplemental Charter of 1882, with notes (in Pascoe, vol. II)", "pascoe",
         "the charters and notes at OCR lines 61668-62963", [COFE], "context", "provisional", "eng",
         doc((1701, 1901), "the Charter is of 1701; printed with notes in 1901"),
         "The Society's founding charter as its own historian prints it, with later marginal notes. Not compared with an earlier printing."),
     row("pascoe-spg-v2-home-work-and-roll", "Pascoe, Two Hundred Years of the S.P.G., vol. II: the episcopate, education, translations, funds and the roll of missionaries", "pascoe",
         "OCR lines 22505-61667", [VICT, COFE], "context", "provisional", "eng",
         doc((1901, 1901), "title page: 1901"),
         "Reference chapters and the roll of every missionary from 1701 to 1900, with places and years. Useful for checking a name or a date.")])

I = "cihm_54002"
chk(I, 177, r"TOME\s+TROISI", 1); chk(I, 183, r"1894", 3); chk(I, 193, r"CHAPITRE|1836", 4); chk(I, 47600, r"TABLE", 2)
add(I, "launay_histoire-generale-de-la-societe-des-missions-etrangeres-t3-fra_1894.txt",
    "Histoire générale de la Société des Missions-Étrangères; tome troisième",
    "Adrien Launay, of the same Society (the title page's author line is not legible in the OCR; the archive.org record gives the name)",
    "Paris: Téqui, libraire-éditeur, 33, rue du Cherche-Midi (title page)",
    "1894 (title page, OCR line 183)", 1894, NR, "fra",
    "clean French prose, but fragments of the marginal summaries run in as short lines. The Canadian Institute for Historical Microreproductions' sheet, in English and French, stands at OCR lines 1-104.",
    "The third and last volume, 1836 to 1892. Title page at OCR lines 105-183, with the author's declaration of submission to the Holy See at 114. Chapter I, 1836-1838, at 193; II, 1839-1842, at 5433; III, 1843-1844, at 10394; IV, 1845-1847, at 13999; V, 1847-1853, at 18549; VI, 1853-1856, at 23428; VII, 1857-1859, at 28117; VIII, 1860-1862, at 31201; IX, 1862-1871, at 36339; X, 1871-1892, at 40016. The text ends with 'Fin' before the table of matters at 47600; the publisher's catalogue follows. Missionaries' letters and reports are quoted throughout.",
    "Adrien Launay", CHINA,
    "The era 8 handover's list: the last volume of Launay's history, whose tomes 1 and 2 are held (the missions of China, Vietnam, Korea, Japan and India from 1836).",
    [row("launay-histoire-generale-missions-etrangeres-tome-3-1836-1892", "Launay, Histoire générale de la Société des Missions-Étrangères, tome III: 1836-1892", "launay",
         "chapters I-X at OCR lines 193-47599", [CHINA], "context", "provisional", "fra",
         doc((1894, 1894), "title page: 1894"),
         "The Society's history from 1836 to 1892, by one of its priests. A later account from the mission's side, covering Vietnam, Korea, Japan and India as well as China.")])

I = "bub_gb_rG8lStorjTwC"
chk(I, 47, r"D\s*C\s*C", 1); chk(I, 17, r"CONTINUATIO"); chk(I, 3210, r"FINIS", 2); chk(I, 3224, r"VINDICI|SECUND", 4); chk(I, 7017, r"FINIS", 2)
add(I, "historia-cultus-sinensium_continuatio-lat_1700.txt",
    "Continuatio Historiae cultus Sinensium, seu varia scripta de cultibus Sinarum, inter vicarios apostolicos Gallos aliosque missionarios et patres Societatis Jesu controversis, oblata Innocentio XII. pontifici maximo et Sacrae Congregationi eminentissimorum cardinalium dirimendae huic causae praepositorum",
    "The title page names no author; the pieces are headed as the work of Nicolas Charmot, procurator of the French vicars apostolic",
    "Cologne ('Coloniae'), no printer named (title page)",
    "1700 (title page: 'M. DCC.', read on the page image, leaf n4, and at OCR line 47)", 1700, PDM, "lat",
    "readable Latin with the long s read as f; the Italian passages and the Chinese words are garbled. Google's 'Digitized by' stamp recurs on page breaks, about 136 times, and its sheets stand at OCR lines 5-14.",
    "A second volume of papers from the Chinese Rites case, following the Historia cultus Sinensium of the same year. Title page at OCR lines 17-47; the printer's note to readers at 73-100. First piece: 'Vindiciae scriptorum Nicolai Charmot' against the Jesuits' Italian 'Dilucidationes', offered to the Holy Office on 2 September 1699, from 123 to 'Finis' at 3210; inside it a letter of the Paris Seminary at 2948 and an 'Expositio' at 3059. Second piece: 'Secundae vindiciae', offered 14 November 1699, from 3224: preface at 3251; answers to four Jesuit writings at 3502, 5089, 5625 and 6556, the first on the Chinese words Tien and Xangti; 'Finis' at 7017. A letter of the superior and directors of the Paris Seminary, dated 16 November 1699, at 7031. Index from 7186. Maigrot's Mandate of 1693 is discussed (for example at 296-300 and 4781), not printed; the main volume holds it.",
    "Nicolas Charmot", CHINA,
    "The era 8 handover's list: the Continuatio of the Historia cultus Sinensium, whose main volume is held (the French vicars' side of the Chinese Rites case in 1699).",
    [row("charmot-vindiciae-1699", "Charmot, Vindiciae scriptorum and Secundae vindiciae against the Jesuits' Dilucidationes (1699), in the Continuatio Historiae cultus Sinensium (1700)", "charmot",
         "the first Vindiciae at OCR lines 123-3210; the second at 3224-7017; the Paris Seminary's letter at 7031-7185", [CHINA], "tradition", "needs-ruling", "lat",
         doc((1699, 1700), "the pieces were offered to the Holy Office on 2 September and 14 November 1699 (OCR lines 123-127, 3222-3250); title page 'M. DCC.'"),
         "The agent of Maigrot and the French vicars apostolic argues at Rome against the Jesuits' defense of the Chinese rites. One party's brief in a quarrel among missionaries; the Jesuit writings appear only as he quotes them. The shelf ruling follows the main volume's row for Charmot.")],
    ruled={"charmot": ("metadata-omission", "The title page (file lines 29-59) names no author. The first piece is headed 'Vindiciae scriptorum Nicolai Charmot' (file lines 135-139).")})

I = "sixmonthsinasyr00parrgoog"
chk(I, 105, r"189", 1); chk(I, 101, r"HORACE\s+COX", 1); chk(I, 13400, r"OLD\s+SYRIAN\s+CHURCH", 3); chk(I, 5356, r"CHAPTER|DEIR", 4); chk(I, 17283, r"APPENDIX", 3)
add(I, "parry_six-months-in-a-syrian-monastery_1895.txt",
    "Six Months in a Syrian Monastery: being the record of a visit to the head quarters of the Syrian Church in Mesopotamia, with some account of the Yazidis or devil worshippers of Mosul and El Jilwah, their sacred book",
    "Oswald H. Parry, B.A., of Magdalen College, Oxford (title page); prefatory note by the Lord Bishop of Durham (title page)",
    "London: Horace Cox, Windsor House, Bream's Buildings, E.C. (title page)",
    "1895 (title page, read on the page image, leaf n9; the OCR misreads the year as '1896.' at line 105)", 1895, NIC, "eng",
    "mostly clean English; proper names are often misread ('Mabdin' for Mardin) and footnote marks and running heads sit in the text. Google's sheet stands at OCR lines 1-47 and its back sheets after the index.",
    "A travel narrative and an account of the church. The Bishop of Durham's prefatory note at OCR lines 140-399, dated Auckland Castle, 8 December 1894; Parry's introduction at 400-500. Nineteen chapters of travel: I at 635; IV, Diarbekr, 2520; V, Mardin and the Patriarch's diwan, 3434; VI and VII, Mardin and its Syrian inhabitants, 4052 and 4549; IX, Deir-el-Za'afaran, 5356; X, life in the monastery, 6200; XI 7137; XIII, Jebel Tur, 8425; XV, Midhiat, 10111; XVII 11595; XVIII, the Yazidis, 12174; XIX, the monastery of Mar Mattha, 12678. Then 'The Old Syrian Church' from 13400: chapter I, the church of Antioch, at 13404; II, the modern history of the Old Syrians, 14434; III, clergy and churches, 15021. Appendix on the Yazidis, with a translation of an Arabic manuscript, at 17283-18942; itinerary 18943; glossary 19279; index 20690.",
    "Oswald H. Parry", SAYFO,
    "CFT-Wants batch 2 (ME-7) and the era 8 handover: Parry's visit to the Syriac Orthodox patriarch at Deir-el-Za'afaran in 1892 (the Google scan; the Columbia scan was dropped for its permission line).",
    [row("parry-six-months-in-a-syrian-monastery", "Parry, Six Months in a Syrian Monastery (1895)", "parry",
         "the travel chapters at OCR lines 635-13399; 'The Old Syrian Church' at 13400-17282", [SAYFO], "context", "needs-ruling", "eng",
         doc((1895, 1895), "title page: 1895 (page image); the prefatory note is dated 8 December 1894; the visit was in 1892"),
         "An English visitor sent by a society that aided the patriarch's schools describes the Syriac Orthodox of Mardin and Tur Abdin twenty years before the Sayfo. An outsider's friendly account. The census has no entry for this church between 1650 and 1906, so the shelf is the nearest one and needs a ruling.")])

for f in FAILS:
    print("ANCHOR FAIL", f)
assert not FAILS
json.dump(items, open(S + "work/spec2.json", "w"), ensure_ascii=False, indent=1)
print(len(items), "items")
for it in items:
    assert len(it["filename"]) < 120 and it["filename"].endswith(".txt"), it["filename"]
    for k in ("title", "creator", "publisher", "pubdate", "rights", "ocr", "content"):
        assert "\n" not in it[k]
