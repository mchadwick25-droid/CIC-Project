# Source Library — Decision Log

Append-only, workstream-local. One entry per ruling made and per PR merged. The
project-level record of the founding decisions is the 2026-10-14 entry in
`Build/Ministry/Technology/CiC_FrontEnd_Decision_Log.md`; this file does not repeat it.

---

## 2026-10-14 — Founding decisions recorded; design of record filed

**Decided (Mark, 2026-10-14).** Seven questions converged one at a time after a
four-stream research pass. Full text in `Design.md` §2 and in the Front-End Decision
Log entry of the same date.

**Filed.** `Design.md`, `Research.md`, this log, and the workstream row in
`Build/Ministry/Features/README.md`. The 160 citation entries whose loci still show
machine apparatus to participants are logged as a known gap in
`Build/Ministry/Operations/Standing/CiC_Cross_System_Analysis_Tracking.md`, not fixed.

**Not done.** No code, no record edits, no package rebuild. The CCEL letter is Mark's, at
the opening of Stage 1.

### Next action

Nothing before the pilot launches. After it launches: Stage 1 for desert, per
`Design.md` §11, opening with Mark's live read of CCEL's copyright page and the letter.

## 2026-11-06 — Change order: the reader lives on the Church Family Tree's domain

**Decided (Mark, 2026-11-06, Church Family Tree convergence).** `Design.md` §7 places the
reader "on the public site under its own directory", which is Church in Conversation's
site. Under the Church Family Tree plan, the Library is the shelf behind both products, and
its public face is the tree. The reader therefore lives on `https://www.churchfamilytree.com`.
A citation in a conversation opens it in the app's existing side panel. Shelves on movement
pages open when their text assignments pass a Library check, whether or not a world is built.

**Why.** Everything citable then lives under one domain. Nothing is built yet, so the change
costs one section of the design and no code.

**Not changed.** The record shape, anchors, gates, rights, hosting on R2 and the staged plan
all stand. Stage 1 still starts after the pilot launches, desert first.

### Next action

When Stage 1 starts, rewrite `Design.md` §7 and §10 (hosting) to the new home. Full record:
`Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`.

## 2026-11-10 — Church Family Tree wants, batch 1: the later-worlds people gate

**Charter (Mark, 2026-11-10).** A Library thread to find the sources the tree needs, public domain
in any language. The wants list is `CFT-Wants.md` in this folder. It is rendered for Mark as an
Artifact.

**Done.** Seven files vendored: Pamphilus's Apology (Lommatzsch 1846, and Migne PG 17), Priscillian
(CSEL 18), Francis (Robinson 1906 and the 1904 Opuscula), Bonaventure (Salter 1904 and Quaracchi
1911). For each, the rights were read on the archive.org record, the title page was read, and the
work was located inside. Truncation was checked two ways: the byte count against the host's listed
size, and the end of the volume read. The Ecthesis was found already held in Mansi X and is now
shelved. Shelf defects from Open-Gaps were fixed where the fix was the Library's own; two
cross-world moves are listed for the coordinator.

**Decided here.** Where a text was in two scans, both are vendored if one scan is garbled where the
other is clean (the Apology: Lommatzsch's end of Book I is garbled, Migne's is clean). The large
Quaracchi Bonaventure volumes (4-6 MB) were located but not vendored, because the English Legenda
and the 1911 Latin opuscula serve the want. Each is a seed row.

**Searches.** Sonnet workers searched in their own scratch directories; the coordinator re-read every
host record, title page, boundary and ending before vendoring. No model was called outside this
conversation. Nothing was paid for.

### Next action

Batch 2, on a fresh branch from main: the eras 8-9 holds and the Brosset chronicle volumes.

## 2026-11-10 — Ruling: Bell Part II and the Pedalion, as carried out

**Decided (Mark, 2026-11-10, relayed by the coordinator).** On the two cross-world moves from
batch 1: "take both recommendations". On Bell Part II, once the gate question came up: "if the
source is consurant of past and they could likcly know it they can point to it". The coordinator
reads this as: if the source is contemporary and the world's people could likely have known it,
the world can point to it.

**How it was carried out.**
- **Bell 1924, Part II.** The first recommendation was to take the row off the `desert` shelf.
  That cannot be done: `engine/m9/confinement.py` (`gate_shelf_row`) requires every vendored
  desert source record to name a row on desert's own shelf. `desert.source.bell-jews-christians-egypt`
  names this row. So the row stays on desert's shelf, now as `context`, which matches the record's
  own `register: etic`. The Melitian community's own-voice row stays `tradition` on
  `melitian-schism`. Under Mark's rule desert may point to it: the papers are contemporary and
  come from the same desert. No desert package went stale (`engine.m2.cli staleness-check`).
- **The Pedalion.** It leaves the 1453-1650 shelf once the census person row for Nikodemos the
  Hagiorite stops pointing at that shelf's row. The people worker moves the pointer to the
  1650-1821 row; the shelf row is removed after that lands on main. Done in batch 2: data release
  32 (#1578) points the census row at the Philokalia rows, so nothing names the 1453-1650 row.

**Flagged, not done.** The desert voice_craft record mentions Bell as "a newly-registered source".
That phrase sits inside a long namesake rationale (five men named Paphnutius) whose other clauses
narrate process the same way. Cutting the one phrase would leave the rest, so the record's own
cleanup goes to its owner (CLAUDE.md: doc hygiene on another thread's content is flagged).

## 2026-11-10 — Church Family Tree wants, batch 2: the eras 8-9 holds

**Done.** Twenty-two files vendored for the eras 8-9 rows held for sources. Whitehouse 1873 was
already held, and a Thrissur row was added to it. The file list, rights and what each fill unblocks
are in `CFT-Wants.md`. Each host record was re-read, the title page read, the wanted passage
located, the byte count matched to the host, and the body confirmed to be the full host text after
the header.

**Decided here.** Where the entry a text serves does not exist yet, the row goes on the nearest
existing entry as `confidence: needs-ruling` (INTAKE §6): the Transylvanian Unitarians on the
anti-Trinitarian entry, Korean Protestants and Holly's Haiti on the missionary-movement entry,
Marsden on the Georgian Church of England. A text is placed on the shelf of its date of writing,
not of its subject: Adoratskii (1887) is on the synodal-century shelf. Ullathorne (1837) was not
vendored, because its only scan is a 1963 facsimile with its own front matter. Lang (1834) was
located but not vendored.

**Corrected before writing.** I had drafted a wrong title for Claret's Apuntes, and places of
printing the title pages do not show for the Historia Bethlehemitica and The Spirit of Missions.
All three were checked against the OCR and corrected. No header carries a date or place the source
does not give.

### Next action

Batch 3: ME-21 (Rabinowitz) by another route, the AP10 Spanish pass, and the first eras of
Open-Gaps 158. Then remove the Pedalion row once the census pointer has moved.

## 2026-11-10 — Church Family Tree wants, batch 3: the earliest named gaps

**Done.** Twenty files vendored for thirteen of Open-Gaps 158's named gaps (the earliest, eras 3-6)
and for AP10 (Hermano Pule). Four gaps are answered by texts already held: Paul of Aleppo for
Antioch and the Arabic Melkites, Dositheus for Jerusalem, and George of Choziba for the Judean
desert. Each host record was re-read and the title page read, and the byte count was matched to
the host. Truncation was checked two ways: the full host text follows each header, and each
volume's end was read where the OCR has one. File by file, with what each unblocks:
`CFT-Wants.md`, batch 3.

**Decided here.** A text that fills a named gap is shelved only where an existing entry covers
its date of writing. Otherwise it is vendored and listed, and the shelf waits for the new entry.
Putting it on the entry that ends before it would repeat the out-of-window fault found in
Nikodemos. By that rule the two Ferencz rows from batch 2 (on the anti-Trinitarian entry,
1517-1650) were wrong, and they are removed rather than patched. Batch 2's other `needs-ruling`
rows (the Korean Repository, Underwood and Holly on the missionary-movement entry, 1793-1906;
Marsden on the Restoration Church of England, 1660-1815) fall within their entries' windows and
stay.

**ME-21.** The six Google Books items are full view, but Google refuses this host's downloads (the
Books API quota is zero, and the PDF and text routes return its "sorry" page). The ids are
-L8pAAAAYAAJ, DBkHAAAAQAAJ and klEWGBQiW44C (Delitzsch, Documente, 1884-85), u5YtAAAAYAAJ (Neue
Documente, with Rabinowitz's autobiography and sermons, 1887), r5YtAAAAYAAJ (Zwei Predigten, 1885)
and nYotAAAAYAAJ (Bikure ta'anah, the Hebrew letters, 1885). Mark could download them in a browser
and push them to `cic/texts/_intake/`.

### Next action

Batch 4, in a fresh session (handover: `HANDOVER-batch4.md` in this folder).

## 2026-11-10 — Church Family Tree wants, batch 4: the religious orders

**Done.** Twenty-seven files were vendored for eleven named gaps of Open-Gaps 158. These are the
orders (Athos, the Carthusians, Cistercians, canons regular, Hospitallers, Carmelites, Franciscans,
Dominicans, Jesuits and Discalced Carmelites) and the Maronites. Five gaps are also answered in part
by texts already held: Georgirenes, the Port-Royal acts, Kempis's Chronicle of Mount St Agnes, Busch
and the Compiegne Carmelites. For each file:
- the host record was re-read;
- the title page was read;
- the wanted passage was located;
- the byte count was matched to the host's listed size.
For the second truncation check, the body after each header was compared byte for byte with the host
text, ending included. File by file, with shelves and what each unblocks: `CFT-Wants.md`, batch 4.

**Decided here.** The batch 3 rule holds: a text is shelved only where an entry covers its date of
writing. For the Latin orders, that entry is the church-wide one of the text's date (Gregorian, Avignon
to Lateran V, Tridentine, ancien regime, long nineteenth century). Those entries run without a break,
and an order is part of that church. The Compiegne history already sat on one this way. For Athos,
the entry is the Ottoman one. The Maronites have no entry after 1517, so al-Duwayhi is vendored with
no shelf. Data release 33 landed while the batch was open and added the Society of
Jesus 1650-1814 and Chinese Catholicism 1650-1906. The Jesuit texts were moved onto those entries,
since an order's own entry comes before the church-wide one. The release's Maronite entry (1815-1906) does not
cover al-Duwayhi's century. Meyer's typikon of 1394 is `needs-ruling` on the hesychast entry: the dates and place fit,
but the tree has not ruled on whether a monastic rule belongs to the hesychast movement.

**Corrected before writing.** Several host records give a date the title page does not: the Dominican
vols. II and VI say 1898, the title pages say 1899 and 1902; the Reforma tome II says 1644 for 1655;
the Memoires de la Chine say 1780 for 1781; the Premonstratensian statutes say 1628, and the title page
says 1626. Each header gives the title page and names the difference. Rance's name is not on his title
page, so his headers say the attribution is the host record's. Al-Duwayhi's printing has no year on
its title page; the header gives the editor's preface (June 189-, last digit lost). I had drafted a
flag that the Port-Royal acts were out of window. They were written in the 1660s, inside it, so the
flag was dropped.

**Flagged for the census owner.** The Compiegne history (1836) is on the ancien-regime shelf (to
1815), where a census story rests on it. It was not moved; the long-nineteenth-century shelf was added
beside it.

### Next action

Batch 5: the rest of Open-Gaps 158's early modern gaps (the St Thomas Christians 1665-1836, the Kongo
church after 1650, Japanese Christians 1650-1865, Chinese Catholics 1650-1906), then the Protestant gaps.

## 2026-11-10 — Church Family Tree wants, batch 5: Rabinowitz, and the early modern mission gaps

**Done.**
- **ME-21.** Mark's five Google Books PDFs were processed through INTAKE:
  - the Google id was read from each PDF's own links, and the title page was read;
  - the text was extracted with `pdftotext -layout`, as earlier PDF intakes were;
  - truncation was checked two ways: the extracted text has one page break per PDF page, and each
    file's end was read;
  - the PDFs and `NOTES-rabinowitz.md` were cleared from `_intake/`.
  The Fortgesetzte Documente (Google's "Bikure ta'anah") prints no Hebrew text, so the Hebrew letters
  stay wanted.
- **Twelve archive.org files** for six named gaps of Open-Gaps 158, checked as before: host record,
  title page, wanted passage, byte count, and body identical to the host text.
- **Held texts shelved.** The census entries for the St Thomas Christians (1665-1815), Kongo after 1650,
  and Chinese Catholics (1650-1906) cite texts the Library held but had not shelved there. They are now
  shelved.

**Decided here.**
- A book written after an entry's window but about it goes on that entry as `context`, which is the
  practice already on the earlier Malabar and Kongo shelves. Own-voice text written inside the window
  goes on as `tradition`.
- Ukrainian Orthodox texts of the 1700s are `needs-ruling` on the Russian church's 1652-1815 entry. The
  Kyiv metropolis then lay inside that church, but whether the tree tells Ukrainian Orthodoxy there is
  its own question.
- New France after 1650 has no entry, so the Quebec texts after 1650 go on the ancien-regime church.

**Corrected.** Batch 4 recorded al-Duwayhi as a new find, but a scan of the same edition had been held
since October 2026 (the Bibliotheca Alexandrina copy). The holdings check had grepped "douaih" and
"maron" and caught neither spelling. Batch 4's file stays as a second scan, and its header line and
registry entry now name the first. The line count is unchanged. The other twenty-six batch 4 files were
re-checked by archive id and by title, and none is a duplicate. From this batch on, the holdings check
also greps the registry by title words and transliteration variants.

**Corrected before writing.** I had drafted a first name for Pastor Faltin that the Fortgesetzte
Documente does not give, and it was removed. The Akty of the Kyiv Academy has a host date of 1904, but
its own notes cite publications of 1909. Its header gives the evidence and dates the printing between
1909 and about 1918, not 1904.

### Next action

Batch 6, in a fresh session after the weekly reset (Mark, 2026-11-10: stop after the handover).
The handover, with the candidates batch 5's session already found: `HANDOVER-batch6.md`. Batch 6 covers
Europe 1650-1815 (the Transylvanian Unitarians, the Nordic Lutherans, the Hutterites,
Waldensians and Schwenkfelders, the French Reformed, English Catholics, the Church of Scotland, the
Remonstrants, the Delaware Swedes).

## 2026-11-11 — Church Family Tree wants, batch 6: Europe, 1650-1815 and after

**Done.** Twenty-five archive.org files for ten named gaps of Open-Gaps 158: the Transylvanian
Unitarians, Hutterites, Waldensians, Schwenkfelders, Remonstrants, Nordic state churches, Church of
Scotland, English Catholics, French Reformed and Delaware Swedes. Each was checked the batch 4 way:
the host record was re-read, the title page read (by two Opus reviewers, then the doubtful ones by
me), the wanted passage located and the volume's end read. The byte count matches the host's listed
size, and for the second truncation check each body after its header is byte for byte the host text.
File by file: `CFT-Wants.md`, batch 6.

**Decided here: the shelf rule and Marsden (the coordinator asked for a ruling on P2-G89c).** The rule
reads by the date the shelved words were written, not the date the book was printed. P2-G89c read it
that way. But its application was incomplete: the 1913 Life prints Marsden's letters from 1810 on, and
the letters of 1810 and 1814 fall before the Victorian entry's window. So the book now has two rows,
one per entry. The letters from 1815 are on the Victorian Church of England; those before 1815 are on
the Restoration and Georgian Church of England, both `tradition`. Batch 3's note that the old Georgian
row "falls within" its window was right for those letters. The same reading is applied through this
batch: the Acts of the General Assembly have a row only for the acts of 1638-1650, the Holy Trinity
records only for those to 1786, and Clay only for the documents of 1684-1765 as tradition. For the
census owner: the Victorian entry quotes the two 1814 letters.

**Decided here: held back.** The Schwenkfelder sacrament rules (`lehre-und-ordnungs-regeln`, drafted
1838, approved 1858) were not vendored. The text is public domain by date, but the 2024 upload carries
a CC BY-NC-ND licence that does not say whether it covers the scan or the text. A no-derivatives
licence would bar modern renderings, so this is Mark's call.

**Corrected before writing.** Several host records give dates or names the books do not. Helweg I's
title page reads 1851 on the page image (the OCR says 1831, the host 1854); Helweg II says 1855, not
1854; Milner's title page reads 1818 on the page image (OCR "1S16"); Cornelius part 2 is 1887; the
Főtanács volume binds five sets of minutes of 1909-1913, not one of 1912; Muston's record carries
fields from a 1978 reprint and a copyright note that the 1866 title page does not. Limborch's title
page is missing from the scan, so his header gives the date and place as the host's only. I had drafted
office or place details from memory (Cornelius a bishop, Milner a bishop, Vincent of Nîmes, Muston a
Waldensian pastor, Wolkan Austrian, Limborch a Remonstrant professor, the 1872 synod the first since the
1650s). None is on the title pages, so all were removed before writing.

### Next action

Batch 7, in a fresh session: the gaps after 1815. Handover: `HANDOVER-batch7.md`.

## 2026-11-13 — Church Family Tree wants, era 4 (622-1054)

**Done.** Fifty-one archive.org files for the era 4 rows of the combined wanted list (Open-Gaps 220 and
222): 41 person sources and 7 councils. Each was checked the batch 4 way. The host record was re-read and the
title page read; six doubtful years were read on page images (Macler 1917, not the record's 1897; Anglia 13
1891, not 1877; the Paterik 1911; Gorskii 1844; Swoboda 1900; Wüstenfeld 1858). The byte count matches the
host's listed size, and each body after its header is byte for byte the host text. Two Opus reviewers took
23 and 28 files, and a third rechecked their corrections. File by file: `CFT-Wants.md`, era 4. The search
record, with every host and language, is `Build/Ministry/Operations/Audits/2026-11-13_library-era4/Search_Log.md`.

**Decided here.**
- A Life whose date of writing the volume does not give goes on its subject's entry as `needs-ruling`. Five
  are shelved this way: John of Jerusalem's Life of John of Damascus, Michael's Life of Theodore, the Life of
  Stephen the Younger, the Vita Euthymii, and the Iviron Lives. The subject's own works in the same volume are
  shelved by the audit's dating of the subject.
- Muslim historians (al-Tabari, Ibn Ishaq) are outside witnesses. They are shelved as `context` on the entries
  they write about, as Baladhuri is.
- Where a scan binds two volumes, the shelf row's locus covers only the volume the want names: Mansi XVII
  (bound with XVIII), Duval's Latin version (bound with the Syriac textus).

**Corrected before writing.** I drafted these from memory, and all were removed before the first write:
- Brussels as the Analecta's place (the title page later confirmed it, so it is now cited);
- "Osbern and Eadmer after the Conquest";
- "the Ramsey Life" and "a Winchester-trained monk";
- three "disciple" Lives;
- "a Catholic historian";
- the tetragamy affair;
- the March days of the Acta Sanctorum volume.

**Corrected after review.** The reviewers found:
- Mansi XVII also holds all of tomus XVIII, so it was renamed and its locus restricted;
- the printer of XVI and XVIII is Reinecke of Berlin, not Geidel;
- the ranges of XIV and XV were wrong (814-856 and 855-868, by their title pages);
- Waitz's scan stops in chapter 23 of the Life of Rimbert;
- Sweet's announced Latin text never appeared;
- Macler's volume is book III only;
- Duval's file binds the Syriac textus;
- the Analecta volume appeared in 1922;
- four PL Creator lines named people the title pages do not;
- about twenty passage lines were wrong;
- person dates were cited to the census when they are in the era 4 audit.

All were fixed and rechecked.

**For the tree, not the Library.** The Paulicians remain known only through enemies. Peter of Sicily and
Theophanes Continuatus are both hostile, so the choice of edition does not change that. The census
should keep the two-witness caveat it already carries.

### Next action

The era 5 wants (1054-1300, 44 person sources, 12 major) in a fresh session, the same way.

## 2026-11-13 — Church Family Tree wants, era 5 (1054-1300)

**Done.** Seventy-one archive.org files for the era 5 rows of the combined wanted list (Open-Gaps 220 and 222):
42 of the 44 person sources have a held text (some in part, and two already held: Nestor and George the Hagiorite),
the four outside witnesses, and three of the four councils. Walter Daniel and Hadewijch have none. Each file was checked the batch 4 way. The host record was
re-read, the title page read, and the doubtful years were read on page images (PL 152 and PL 182, both 1879;
Hefele-Leclercq V.2, 1913; Matthew Paris IV, 1877). Every body after its header is byte for byte the host text.
Two Opus reviewers took 36 and 35 files, and a third rechecked their corrections. File by file: `CFT-Wants.md`, era 5.
The search record is `Build/Ministry/Operations/Audits/2026-11-13_library-era5/Search_Log.md`.

**Decided here.**
- Every modern edition the audits named is in copyright (Powell, Matarasso, Waddell, Tugwell, Armstrong, Upton-Ward,
  Duggan, Sewter, Tschan, Babcock and Krey, Brooke and the rest). Each was replaced by an older
  public-domain edition of the same text, usually the Migne, Rolls Series, Acta Sanctorum or Recueil edition, or
  reported not found.
- Hostile and outside witnesses are shelved as `context` on the entry they write about: Stephen of Bourbon,
  Rainerius, Döllinger's documents (the Waldensians and the Cathars), Anna Komnene and Zigabenos (the Bogomils),
  William of Tyre on the Maronite union, the Muslim and Jewish travellers and historians on Outremer, Marco Polo on
  the Church of the East under the Mongols.
- A later hagiographer or annalist whose words fall after the window is `context` (Tocco, Le Couteulx,
  Seton's Agnes Legend). A text whose date of writing the volume does not settle goes in as `needs-ruling`: the
  Cistercian founding texts, the Speculum perfectionis (placed as the held Evans is), Joachim's Tractatus (the
  volume's series page files it under the twelfth century), Pakourianos's Typikon (the editor prints a later Greek
  version), Norbert's Life (the fit of the Premonstratensians to the canons regular entry), Brother Leo's Scripta.
- The Mirror of Simple Souls is shelved as an anonymous work (`needs-ruling`). The 1927 volume does not name
  Marguerite Porete, so the header does not either; the shelf note records that scholars attribute it to her.
- Rows 68 (Nestor) and 90 (George the Hagiorite) are held already, so their wanted-list rows say HELD with the held
  files' own lines. The Primary Chronicle and the Paterik now also sit on `kievan-rus-christianity-1054-1240`
  (the chronicle as tradition, the Paterik as context). Nestor's authorship of the chronicle stays Contested.
- No Language line was written for English files; mixed volumes name their languages after the code.

**For Mark.** Two finds were not vendored because their rights are a real question.
- Hadewijch (row 73): the editions of 1875, 1895 and 1924-25 are only on dbnl.org, which gives no per-item licence and
  warns that books under 140 years old may be protected. The Library thread did not take them.
- Anna Komnene in English (row 88): Dawes's 1928 translation is on archive.org as a transcription from the Internet
  Medieval Sourcebook, whose notice says it is presented solely for non-commercial educational and research
  purposes. The text is public domain by date, but the notice is not. The Greek (Reifferscheid 1884) is held.

**Corrected after review.** The reviewers found these, and all were fixed and rechecked:
- Bruno's letter to Raoul le Verd was cited at a line that is Guigo's letter; the volume prints only an excerpt of it
  and sends the reader elsewhere for the whole.
- The Mirror of Simple Souls was headed with Porete's name; the title page says "an unknown French mystic".
- Two Migne headers (PL 159 and PL 190) said Petit-Montrouge where the title pages read Garnier, Avenue du Maine.
- "Zygabeni" for the title page's "Zygadeni"; a note on the burning of Basil that the volume does not carry.
- The Alexias scan binds volumes I and II; the Commentationes scan binds volumes IV to VI; Röhricht's article is the
  first instalment (letters I-II); PL 195 and PL 170 are shared volumes.
- About a dozen line citations pointed at running heads, chapter lists or footnotes.

**For the tree, not the Library.** The Waldensians, the Cathars and the Bogomils remain known mostly through hostile
writers; the choice of edition does not change that. The Library now holds both the Greek of Zigabenos and the
Latin and Greek of Anna Komnene for the Bogomils, and Stephen of Bourbon, Rainerius and Döllinger for the sects.

### Next action

The era 6 wants (1300-1517, 14 person sources, 4 major) in a fresh session, the same way.

## 2026-11-15 — Church Family Tree wants, eras 1-3 (70-622)

**Done.** Twenty-five archive.org files for the eras 1-3 rows of the combined wanted list: person rows 1-13,
council rows 1-8 and Library-label correction 19. Mark restarted the Library on 15 November, eras 1-7 first, in a
fresh session per batch. File by file: `CFT-Wants.md`, eras 1-3. The search record is
`Build/Ministry/Operations/Audits/2026-11-15_library-eras1-3/Search_Log.md`; the review is `R1_review.md` beside it.

**Decided here.**
- Rights: only a printed imprint of 1930 or earlier, read on the title page. Two finds whose title-page OCR could
  not be read (Harnack 1904, de Boor 1887) were left out, since Holl and Bekker fill the same wants.
- Three wants were held already and are marked HELD: Malalas (PG 97), the Roman synod of 377 (the notice in Mansi
  III) and the Donatist council against Tyconius (Augustine, in PL 43). The held Malalas now has a shelf row.
- Mani: the followers' texts the audit named are in copyright. The Library took the Manichaean texts printed
  before 1931 (Turfan, Dunhuang) and two Muslim witnesses who quote Mani's books (the Fihrist, al-Biruni). The
  Manichaean texts are `needs-ruling`: the manuscripts are later than the entry's window. The witnesses are `context`.
- A text earlier than its entry's window is `antecedent`: Ezana's inscriptions on the Aksumite entry (451-615) and
  Theodoret's chapter on Maron on the Maronite entry (1100-1300).
- A text whose date or author is disputed is `needs-ruling`: the fragments of Paul of Samosata, Agathangelos, Nau's
  Maronite texts, and the Latin Life of Sabas, which its own volume says may be Metaphrastes's paraphrase.
- A later historian is `context`: Ukhtanes on the break with the Georgians, Simocatta, Malalas.
- Naironus (1679) is vendored with no shelf: no Maronite entry covers its date.
- Unreadable originals were not taken: the Armenian Book of Letters (1901) and the Armenian Shushanik (1853).

**Corrected after review.** All 25 rights rows passed. The reviewer found eleven points, all fixed: Genesius in
the Simocatta volume is Lachmann's edition; three OCR notes were too generous (the Greek in Lagarde and Bardy, the
Latin in PG 82); the acts of 536 in Mansi VIII end before the volume does; the Christian reading of Ezana's last
inscription is disputed in Littmann's own addenda; four smaller wordings. The list is `R1_changes.md`.

**For the tree, not the Library.**
- Melito's Peri Pascha cannot be filled from the public domain: it was first printed in 1940.
- The Life of Sabas is held only in a Latin version that may not be Cyril's wording. A profile should say so.
- Shushanik, and the whole History of Movses Daskhurantsi, stay wanted.

## Eras 4-5, second fill (2026-11-15)

Forty-six files for the rows the first era 4 and era 5 passes left open and for the Library wants of Open-Gaps
263, 265, 266, 268 and 272. Record: `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5/Search_Log.md`;
the rows are in `CFT-Wants.md`, "Eras 4-5, second fill".

**Decided here.**
- Rights: only a printed imprint of 1930 or earlier, read on the title page. Where the OCR could not give the
  year, it was read on the scan's page image (Mansi XII; the Acta Sanctorum, March II). Where neither gave it, the
  file was left out: Mansi XX, whose scan has no imprint leaf, and PL 148.
- Hadewijch: the 1875 edition is vendored from dbnl.org. dbnl marks that title "Auteursrechtvrij" and says its
  copyright has run out. This is the edition Mark's ruling allows.
- Powicke's offprint on Walter Daniel has no year on its title page. Its reprint line and its prefatory note
  (March 1922) date it, and it is taken on that printed evidence.
- Two wants were held already: Berno's testament (PL 133) and the Lyon I sentence in Matthew Paris. The first era 4
  log's "PL 133 does not print the testament" was wrong.
- Ibn Hayyan: his book cannot be filled before 1937. Gayangos's al-Maqqari is taken as `context`, a later writer
  who quotes him by name.
- A scan whose wanted passage cannot be read is not taken: the Kyiv archive volume, Cummian in Ussher, the Tale of
  Boris and Gleb, Cosmas the Priest, Akropolites, the Greek Life of Euthymius.
- A translation printed in place of the author's words is `needs-ruling` and says so: Clare's letters in Tanner's
  Latin. Her Process survives in an Italian version and is shelved as tradition with that said.
- Lives with no date of writing in the volume, or written by another house, are `needs-ruling`: the Life of
  Tarasius; the Life of Robert of Molesme. Raymond of Capua's Life of Catherine came with the April volume and is
  `needs-ruling` until era 6 places it.
- A modern study is `context` (Hefele in English) or not taken (Hefele-Leclercq; Robinson's article on Clare).
- Shelf rows name the file's own prefix as author where the corpus author index has no other name (Mansi, the
  Acta Sanctorum, the Recueil). George Metochites, bound in the Mai volume, has no shelf row; the header names him.

**For the tree, not the Library.**
- No English printed by 1930 exists for Theophanes, the Life of Stephen the Younger, Nikephoros, Nicholas
  Mystikos, Peter of Sicily, Ilarion or the trial of Maximus. Those wants cannot be filled under the date rule.
- The Life of Constantine is held in Latin translation only; the Slavonic cannot be read in any scan found.

## Era 6 fill (2026-11-15)

Twenty-seven files for the era 6 rows of the wanted list and the Library wants of Open-Gaps 264, 267 and 271.
Record: `Build/Ministry/Operations/Audits/2026-11-15_library-era6/Search_Log.md`; the rows are in `CFT-Wants.md`,
"Era 6 (1300-1517), filled".

**Decided here.**
- Rights: only a printed imprint of 1930 or earlier. Ten years were read on the scan's page image where the OCR
  title page gave none; the leaf is named in each header.
- A scan that is a modern reprint is out, whatever the year of the text it reproduces: Gibb's Ibn Battuta (a 1992
  reprint), the Zeitschrift für Kirchengeschichte volume with Ockham's letter (a Johnson Reprint), Kałużniacki's
  Tsamblak (Variorum, 1971). The last two are held for Mark, since the text reproduced is of 1884 and 1901.
- The host's own date is not trusted against the title page: the Acta Sanctorum for October X is the Brussels
  printing of 1861, where the host names Paris, 1863.
- Three wants were held already. The Perruchon header, registry note and shelf note said the chronicle of Zara
  Yaqob had no French translation in the volume; it has one, and the three are corrected. The header of the
  Recueil's first Oriental volume now names its extract from Abu'l-Fida.
- A retelling is not taken in place of a Life: Stephen of Perm (1896), Zosima and Savvatii (1897).
- A printing whose wanted passage cannot be read is not taken: Kempis's Life of Gerard in the 1615 and 1728 Opera.
- A selection is taken where the full edition is not to be had, and says so: Naumann's Tauler after Vetter.
- The Muslim outside witnesses are held in their translators' French and German and shelved `context`,
  `needs-ruling`: no census entry covers Mamluk Egypt and Syria or the Maghreb after 1300, so Ibn Khaldun and
  al-Qalqashandi sit on `coptic-christianity-fatimid-to-mamluk` until a ruling; Ibn Battuta on the Palaiologan and
  Saint Thomas entries. None was read in depth.
- Euthymius of Tarnovo is `needs-ruling`: no census entry is the Bulgarian church of his day.
- Birch's Ockham carries the imprint 1930, the last year the date rule admits.

**For the tree, not the Library.**
- Nothing printed by 1930 was found for Estifanos, for Zara Yaqob's own books or for the full Book of Margery
  Kempe. The Gadla Ewostatewos, the Prosvetitel and the Lives of Stephen of Perm, Kirill of Beloozero, Zosima and
  Savvatii, and Theodosius of Tarnovo exist in print before 1931 but are not on archive.org.

### Next action

Era 7 wants in a fresh session, the same way.

## Era 7 fill (2026-11-15)

Fifty-seven files for the era 7 rows of the wanted list (person rows 113-120, outside-witness rows 10-27), the two
council rows queued in `CFT-Wants.md` (Marburg and Worms) and the Library items of Open-Gaps 273 and 278. Record:
`Build/Ministry/Operations/Audits/2026-11-15_library-era7/Search_Log.md`; the rows are in `CFT-Wants.md`,
"Era 7 (1517-1650), filled".

**Decided here.**
- Rights: only a printed imprint of 1930 or earlier. Sixteen years were read on the scan's page image where the
  OCR title page gave none or a doubtful one; the leaf is named in each header.
- The title page decides, not the host's record. The one scan of Schirrmacher's Briefe und Acten is catalogued
  by the host as the Amsterdam reprint of 1968. The scan is the Gotha printing of 1876: the title page, old
  library stamps, the printer's line on the last leaf, and no reprint leaf. It was taken, and the header says why.
  The same reading set aside the host's dates for Füsslin (1741 for 1753), the Reichstagsakten (1893 for 1896),
  Förstemann (1833 for 1835) and The Chinese Repository (1832 for 1850).
- A scan with no title page is not taken on its companions' imprint: the first scan of Machiavelli's fourth
  volume gave way to one that has its title page; de Thou's De vita sua was not taken.
- A scan that is a modern reprint is out: the Kraus reprint of The Chinese Repository, the Burt Franklin Leo
  Africanus, the facsimiles of Bodin (1962) and Kidd (1967). The single monthly number of the Repository with Xu
  Guangqi's memorial is an original of 1850 and was taken.
- A notice on reuse is held for Mark: the scan of the Olivetan Bible carries the French national library's
  notice on commercial reuse. Access-restricted volumes (the Miscellanea Ehrle) were not taken.
- An abridged or partial own text is taken and says so: Dentière's Epistre with the editor's cuts; Kâtib Çelebi's
  four chapters; Gracián's treatise in place of his Peregrinación.
- One want was held already: the Colloquy of Poissy, in Beza's Histoire ecclésiastique.
- Long sets were located and not taken: de Thou (seven and sixteen volumes) and Vasari (five and ten).
- The Library holds no notes: shelf notes and content notes describe the text only (Mark, 2026-11-15). Why a
  row sits where it does is said here; what was not read is said in the cautions of `CFT-Wants.md`.
- Reu carries the imprint 1930, the last year the date rule admits; his preface is dated 15 December 1930.
- Shelves. Rows for Luther's own texts sit on `lutheran-wittenberg-and-its-congregations`; the person entry
  `martin-luther` has no shelf. Katharina Zell is `needs-ruling` on the same entry: Strasbourg has none of its
  own. The Ottoman witnesses and Busbecq sit on `orthodoxy-under-the-ottomans-parish-millet-and-n`; the Jewish
  chroniclers, Guicciardini and Machiavelli on `the-tridentine-church` (the last two also on
  `latin-papal-church-avignon-to-lateran-v`); Bodin and Montaigne on `the-huguenots`; Leo Africanus on
  `the-coptic-church-under-the-ottomans`. All of these are `context`, `needs-ruling`: no census entry is the
  Ottoman state, the Jews of Europe, Italy's politics or North Africa. None was read in depth.
- Two built worlds' shelves gained rows and lost none: `lutheran-wittenberg-and-its-congregations` and
  `the-reformed-cities-zurich-and-geneva`.

**For the tree, not the Library.**
- Marburg now has a record of the sessions and the signed articles, so the held-back profile can be written.
- Nothing printed by 1930 was found for Fabian Fucan or Guaman Poma. Zell's Entschuldigung, Dentière's whole
  Epistre, Gracián's Peregrinación, Seler's Sahagún and the Colloquios exist in print before 1931 but are not
  on archive.org, or not open there.

### Next action

Era 8 wants in a fresh session, when era 7's Whos begin.

## 2026-11-15 — Era 10 rights rulings: eleven questions answered

**Decided (Mark, 2026-11-15).** Eleven rights questions from the era 10 scoping page, answered
one at a time. Mark's picked option is in quotes.

- **R1, Vatican texts: "Old print, link the rest".** Hold the Latin from the *Acta* printed by
  1930 and render it ourselves. Everything later is cite and link only. One letter asks
  permission for the Vatican II documents.
- **R2, texts whose owners say they are free: "Take all three".** A new class beside public
  domain, with the owner's own words copied into each file header: the Dictionary of African
  Christian Biography (CC BY 4.0; skip entries marked as reprinted "with permission"), the
  Catholic Worker paper ("not copyrighted"), and the Cape Town Commitment (quoted word for word
  only, no modern rendering).
- **R3, "non-commercial use only" permissions: "Don't hold, cite and link".** Hold nothing on a
  non-commercial permission. Write for permission where a text matters.
- **R4, church statements with no stated terms: "Cite and link, then write".** Letters to each
  body, starting with Barmen and Lausanne.
- **R5, quoting a work we do not hold: "Keep the rule".** Facts and a citation, no quotation.
- **R6, the date rule: "Keep the one test".** The imprint on the title page. Barth's 1919 book is
  noted as a known exposure (free in the US, protected in Europe until 2038). The line moves each
  January.
- **R7, American books of 1931 to 1963 whose copyright was never renewed: "Allow it generally".**
  Mark chose this over the case-by-case recommendation. Any such book counts as free, with the
  renewal search recorded in the file header. Asked whether it applies to the running era 8 and 9
  Library threads, Mark chose "Yes, all eras now". R7 widens the "imprint of 1930 or earlier"
  rule for American books of 1931 to 1963, and settles the non-renewal proposal in the 27 October
  rights audit (`Build/Ministry/Operations/Audits/2026-10-27_post-1930-files_Rights-Audit.md`).
- **R8, old works whose only scan is locked: "Log them, open HathiTrust later".** Record as
  "located, not obtainable here". Opening HathiTrust in the network settings stays an open item
  for Mark.
- **R9, court and government records: "By imprint, like a book".** A printed record counts by its
  imprint date. Unprinted archive records are cite only. US federal government works are free.
- **R10, Martin Luther King Jr.: "Cite and link only".** No quotation, no rendering.
- **R11, translating from an old original ourselves: "Yes, with a second check".** Holds for era
  10. Where no old English translation exists, a second independent rendering checks the first,
  and differences are marked uncertain on the card.

**Changed.** The rights rule in `cic/texts/INTAKE.md` §2 and `Design.md` §9. The letters and the
HathiTrust item are in the Church Family Tree `Open-Gaps.md`.

**Not done.** No text vendored, no file header edited, no letter sent. The nine Church in
## 2026-11-15 — Era 10, batch 1: the major people, the conferences and the Acts to 1930

**Done.** 94 files (10,208,969 words) for the era 10 wants, under the rights rulings of 2026-11-15. The files, their
rights bases and the rows not filled are in `CFT-Wants.md` ("Era 10 ... batch 1"). The search record, the refused
hosts and the cautions for writers are in `Build/Ministry/Operations/Audits/2026-11-15_library-era10/Search_Log.md`.

**Decided during the batch.**

- **R12, a title page with no year (Mark, 2026-11-15: "Copyright notice yes, preface with a check").** Where a title
  page prints no year, a copyright notice dated 1930 or earlier counts. A dated preface counts only when the library
  catalog's date agrees. The header records the date used and where it was found. The ruling came with the Library
  threads' briefs and is recorded here and in `cic/texts/INTAKE.md` section 2. Nineteen files of this batch rest on it.
- **The Dictionary of African Christian Biography is CC BY-NC (Mark, through the coordinator, 2026-11-15).** R2 was
  made on the site footer's words, "openly licensed via CC BY 4.0". The site's usage page
  (https://dacb.org/about/usage/) says: "DACB is licensed under a Creative Commons Attribution-NonCommercial 4.0
  International License ... Posting on websites containing advertising and all other commercial uses require the
  express written consent of the DACB." R2's line on the dictionary is superseded by R3: cite and link, nothing held.
- **The Catholic Worker: "Original paper scans only" (Mark, through the coordinator, 2026-11-15).** The owner's
  sentence, "Content from The Catholic Worker paper is not copyrighted", stands on a page that also puts the site's
  content under a non-commercial license. Scans of the printed paper are taken on the sentence; the site's own
  transcriptions are cite and link. Held so far: the issue of June 1969, and Maurin's Catholic Radicalism (1949),
  whose own title-page verso says its contents are not copyrighted.
- **A year printed only inside the work's title (coordinator, 2026-11-15; Mark may overrule).** Taken where the
  publisher and place on the title page are the first printing's, nothing in the scan names a later printing, and the
  library catalog date agrees. Eleven files: the Edinburgh 1910 report, Lambeth 1930, the Shanghai report of 1922.
- **A permission notice on a library's film (this thread, under the base rule).** Loisy's L'Évangile et l'Église
  (1902) exists only as a scan of a Columbia University preservation film whose target reads "Reproductions may not be
  made without permission from Columbia University Library". Not taken; held for Mark.
- **R7, first uses.** Niebuhr's Moral Man and Immoral Society (copyright 1932) is held: no renewal in either database.
  Houteff's Shepherd's Rod, volume 2 (1932) is not held: renewed in 1959.
- **The registry accepts "Owner-declared free" (Mark, through the coordinator, 2026-11-15: "Allow it
  (Recommended)").** `cic/engine/texts_registry.py` clears a Rights line that begins with those words, the class
  `cic/texts/INTAKE.md` section 2 names.

**Not done.** The Azusa Street paper, the African-Initiated Churches people, Rātana, the Russian council's own prints
and most Orthodox patriarchs have no held source: the reasons are row by row in `CFT-Wants.md`. The nine Church in
Conversation design questions (D1 to D9) stay open.

### Next action

Mark sends the letters. Library threads for eras 8 and 9 apply R7 from their next intake.

## Eras 4-5, third fill (2026-11-15)

Seven public-domain files for the Library items of Open-Gaps 269 and 279 (era 4 Who batches 9 and 11). Search
record: `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5-b/Search_Log.md`. Wants table and cautions:
`CFT-Wants.md`, "Eras 4-5, third fill".

**Decided here.**
- Rights, as in the second fill: a printed imprint of 1930 or earlier read on the title page or its page image.
  Matthew of Edessa's year was read on the page image because the OCR garbles the numeral.
- A title page with no year is not taken, even where the preface is dated: Bacha's French of Abu Qurrah (preface
  1905) is held for Mark, as Mansi XX was.
- An own-language text whose script the OCR cannot give is taken only where a readable translation stands in the
  same file (Arendzen's Arabic with Latin). The Armenian uploads of Stepanos and Matthew and Chabot's Syriac
  tome IV were not taken.
- From this batch each shelf row states its language and a date field. Where the file itself does not date the
  writing, the date is `unknown` and says what was read. Each file's word count is in its header and registry
  note.
- Shelves. Matthew of Edessa is `needs-ruling` on `armenian-cilicia` (tradition) and on
  `bagratid-armenian-christianity` (context): Dulaurier's preface calls him an Armenian monk of the twelfth century, a native of Edessa, and no entry is his own.
  John of Damascus's sermons on the Assumption are `needs-ruling` on `melkite-arabic-christianity`. Mendham's
  English of Nicaea II sits where Mansi XII-XIII sit, as the council's own acts.
- The review was done by a Fable reader in place of Opus, on Mark's instruction of 2026-11-15 as relayed by the
  Church Family Tree coordinator ("use our free fable and stop all opus work except the rewrite process").

**For the tree, not the Library.**
- Nothing by Clement of Ohrid, no short Life of him and no Life of Methodius beyond the held texts was found.
- No English of Eulogius, Alvarus or Abu Qurrah was printed by 1930.

### Next action

Era 8 (1650-1815), by region, each batch in its own pull request.

## 2026-11-15 — Shelf rulings: the 39 `needs-ruling` groups answered

Mark ruled on the `needs-ruling` shelf rows of eras 1-10. He picked items 1 to 4 himself, one by one, then said:
"follow your recomondations for all shelfs". The coordinator's recommendations are therefore his rulings.

**The principle used.** A tradition's own text with a doubt about date or authorship stays tradition, with the
doubt stated in the shelf row's note. A later reworking or compilation by others is context. A work written before
an entry's window that the entry grows from is antecedent. Outside witnesses with no census entry of their own stay
context on the nearest entry where they now sit, and each missing entry is logged as a census gap (Open-Gaps
288). No new census entry was made.

**The rulings.** Every row below now carries confidence `assigned`.
1. Manichaean texts (4 files), `manichaeism`: tradition; the manuscripts are of the 8th-10th centuries.
2. Agathangelos (Lagarde 1887; Langlois 1867-69), `armenian-christianity-conversion-era`: tradition; the version is usually dated after 451 and its date is not settled.
3. Nau's Maronite texts (2 files), `maronite-christianity`: antecedent; the date and John Maron's authorship are disputed.
4. Latin Life of Sabas (Surius 1880), `chalcedonian-monasticism-judean-desert-and-gaza`: context; a possible Metaphrastes reworking, and Cyril is quoted only from Cyril's own edition.
5. Paul of Samosata fragments (Loofs 1924; Bardy 1923), `antiochene-church-third-century`: tradition; which fragments are his is disputed.
6. Naironus 1679: no shelf for now; census gap logged.
7. Life of Tarasius (PG 98), `byzantine-imperial-church-heraclian-iconoclast`: tradition; the volume gives no date of writing.
8. Life of Robert of Molesme (PL 157; Acta Sanctorum April III), `cistercian-monasticism`: tradition; Molesme's telling, not Cîteaux's, and later than Robert.
9. Clare's letters in Tanner's Latin (Acta Sanctorum March I), `the-franciscan-movement`: tradition, marked as a translation (a `translator` field), never quoted as Clare's own Latin.
10. Raymond of Capua, Life of Catherine (Acta Sanctorum April III): tradition on `latin-papal-church-avignon-to-lateran-v`, the entry Catherine of Siena's Who profile (era 6 batch 2) sits on. Nothing moved.
11. George Metochites, Historia dogmatica (the Mai volume): a new shelf row on `byzantine-church-after-1054`, tradition, as Bekkos is there. The author index had no slug for him, so the staging file carries an `authors_ruled` block (`george-metochites`).
12. Euthymius of Tarnovo (Kaluzniacki 1901), `serbian-and-bulgarian-medieval-monasticism`: tradition; no entry is the Bulgarian church of his day.
13-15. Ibn Battuta (4 vols), Ibn Khaldun (7 files), al-Qalqashandi (2 files): context where they sit.
16. Katharina Schütz Zell (Füsslin 1753 tradition; Röhrich 1855 context), `lutheran-wittenberg-and-its-congregations`: as placed.
17. Ottoman witnesses and Busbecq vol. 1 (5 files), `orthodoxy-under-the-ottomans-parish-millet-and-n`: context, as placed.
18. Jewish chroniclers (5 files), `the-tridentine-church`: context, as placed.
19. Guicciardini (4) and Machiavelli (4), `the-tridentine-church` and `latin-papal-church-avignon-to-lateran-v`: context, as placed.
20. Bodin, Montaigne, Busbecq vol. 2 (6 files), `the-huguenots`: context, as placed.
21. Leo Africanus (3 vols), `the-coptic-church-under-the-ottomans`: context, as placed.
22. Matthew of Edessa (Dulaurier 1858): tradition on `armenian-cilicia`; context on `bagratid-armenian-christianity`.
23. John of Damascus, sermons on the Assumption (Allies 1898), `melkite-arabic-christianity`: tradition.
24. John of Jerusalem, Life of John of Damascus (PG 94), `melkite-arabic-christianity`: tradition; no date of writing in the volume.
25. Michael the Monk, Life of Theodore the Studite (PG 99), `iconophile-byzantine-monasticism`: tradition; same note.
26. Life of Stephen the Younger (PG 100), `iconophile-byzantine-monasticism`: tradition; same note.
27. Vita Euthymii (de Boor 1888), `byzantine-imperial-church-macedonian`: tradition; same note.
28. The Iviron Lives (Peeters 1917-19), `georgian-revival-tao-klarjeti` and `the-georgian-golden-age`: tradition on both; their dates of writing against the two windows are not settled.
29. Stephen Harding, Charta caritatis and Exordium (PL 166), `cistercian-monasticism`: tradition; authorship and date are disputed.
30. Norbert of Xanten, Vita B (PL 170), `canons-regular-victorine-school`: tradition; the Premonstratensians are canons regular but a distinct order.
31. Bruno of Cologne (PL 152), `carthusian-life`: the one row is split in two. The Acta S. Brunonis becomes context (a later compilation); the Commentarium in Psalmos, printed under Bruno's name, stays tradition.
32. Brother Leo's Scripta (Lemmens 1901) and the Speculum perfectionis (Sabatier 1898; Evans 1899): tradition where placed; date and attribution to Leo are contested.
33. Agnes of Prague's Legend (Seton 1915), `the-franciscan-movement`: context, as placed; Seton dates it 1282-1328.
34. Joachim of Fiore, Tractatus (Buonaiuti 1930), `joachimite-current`: antecedent. The Life of Joachim (Acta Sanctorum May VI): context.
35. The Mirror of Simple Souls (1927 English), `free-spirit-heresy` and `the-beguines`: tradition on both; scholars attribute it to Marguerite Porete and the volume does not name her.
36. Gregory Pakourianos, Typikon (Mousaios 1890), `the-georgian-golden-age`: tradition; the editor prints a later Greek version, not the original.
37. Meyer's typikon of 1394, `hesychasm-and-the-palamite-synthesis`: context (a monastic rule of the right time and place, not a hesychast teaching text).
38. Ukrainian Orthodoxy after 1700 (2 files), `russian-church-nikon-to-holy-synod`: tradition; Kyiv then lay inside that church.
39. Underwood, The Call of Korea (1908): moved from `the-missionary-movement-s-native-churches-seramp` to `korean-protestantism-twentieth-century` (1907-c. 2010), tradition. AP15 (G89-34 b) is a hold on a gap of 1884-1906 ("hold for sources, then named lines"), not a ruling on this shelf, so it did not block the move.

**Changed.** The staging files in `cic/corpus-map/_staging/` and the buckets the merge regenerates;
`UNATTRIBUTED.yaml` (the `george-metochites` ruling); `CFT-Wants.md` rows that said `needs-ruling`.

**Not changed.** The older world-build rows in `Build/worlds/_cross-world/NEEDS-RULING.md`, the other `needs-ruling`
shelf rows not named in the 39, and `cic-website/data/corpus-coverage.json` (its generator already differs from
the committed copy on `main`, so it is left to the pass that owns it).

### Next action

Mark weighs the census-gap candidates (Open-Gaps 288) for future census entries.

## Era 9, batch 1: the major figures (2026-11-15)

Ninety-nine files for the 63 person rows marked major in the wanted list (rows 163-225). Record:
`Build/Ministry/Operations/Audits/2026-11-15_library-era9/Search_Log.md`; the rows are in `CFT-Wants.md`,
"Era 9 (1815-1906), batch 1".

**Ruled by Mark during the batch (15 November, through the coordinator).**
- On title pages that print no year, verbatim: "Copyright notice yes, preface with a check". A copyright notice
  dated 1930 or earlier counts as the date. A dated preface counts only when the library catalogue's date
  agrees. The header's rights line names the date used and where it stands. The rule is now in
  `cic/texts/INTAKE.md`, section 2. Six files came in under it.
- The wider rights rule of the same day (American books of 1931 to 1963 never renewed; United States
  government works; owner-stated free texts) and the leave to strip the host's own additions at intake were
  received during the batch and not used in it. They apply from the next batch.

**Decided here.**
- Every imprint was checked again by the Library thread after the searchers. Eighteen years were read on the
  scan's page image; the leaf is named in each header.
- Content notes say only what the file shows. The first review found details from outside the files in the
  searchers' notes, so every note and locus of the batch was checked against its text by fresh checkers and
  written again. Search narration stays in the search log.
- Lives told by another are shelved as `context`; the person's own writings as `tradition`. A text written
  outside its entry's window is `needs-ruling` on the nearest entry.
- OCR that cannot be read is not taken, even where the imprint is good: Wichern's Denkschrift (1889),
  Friedrich's Life of Dollinger, Dollinger's Briefe und Erklarungen, Khrimian's Armenian works, Waldenstrom in
  Swedish. They are listed as located.
- Ellis's History of Madagascar, vol. 2, prints no date of its own. It was taken on vol. 1's preface and the
  catalogue's date, and its header says so.

**Held for Mark.**
- Os Sertoes, third edition (1905): the host record carries the Public Domain Mark, but the Brasiliana USP
  notice inside the file asks for non-commercial use and no republication without leave.
- The Doctrine and Covenants of 1852 (an Intellectual Reserve copyright line) and two Swedish printings of
  Waldenstrom under NC licenses were not taken.

### Next action

Era 9, batch 2, in a fresh session: the person rows not marked major (226-330), the era 9 outside witnesses and
council records, the held eras 8-9 items, and the texts of this batch still owed a date check.
Era 10, batch 2: a second pass by region for the rows marked not found (Africa, Oceania, the Orthodox churches), more
original scans of the Catholic Worker paper, and the council leads not yet searched.

## 2026-11-15 — Era 10, batch 2: Africa, Oceania, the Orthodox and Oriental churches

**Done.** 71 files (4,273,101 words) for the era 10 rows batch 1 left open, all public domain by their printed dates.
The files and the rows not filled are in `CFT-Wants.md` ("Era 10 ... batch 2"). The search record, the calls and the
cautions are in `Build/Ministry/Operations/Audits/2026-11-15_library-era10-b2/Search_Log.md`; the items Mark can fetch
by hand are in `Hand_Fetch_List.md` beside it.

**Decided during the batch (this thread, under the rulings already recorded; the coordinator or Mark may overrule).**

- **A digitizing library's page-foot stamp is a host addition.** The 25 numbers of Путь carried the line "Библиотека
  «Руниверс»" at the foot of each page. It was stripped at intake and counted in each header.
- **A year printed in both eras on a leaf inside an issue counts as a printed year.** One Malayalam monthly was taken
  on its calendar leaf ("1922" and the Malayalam-era year "1098"). Issues that print only Malayalam-era numerals, not
  read with certainty, were not taken.
- **A host record that claims copyright in a scan of an old print is held for Mark,** as batch 1 of era 9 did with the
  same claimant. Three Māori and Tongan prints of 1897-1916 were not taken.
- **A second edition dated by its foreword and its catalog record.** Jabavu's The Black Problem is taken under R12
  on a foreword of December 1920 and a catalog date of 1920, though the author's preface to the second edition is
  dated January 1921. The header gives all three.
- **A tradition's own writer after its entry's window, with no later entry.** Placed as tradition on the entry that
  closes in 1906, with the date in the note (Tucker, the Zulu hymnal, Kyriakos Mikhail, Jabavu, the Arabic history of
  the Coptic Church). The shelf principle does not name this case; the missing later entries are logged as gaps.
- **Batch 1's shelf rows at `needs-ruling`.** All twelve are settled by the principle of the shelf rulings above
  (antecedent, context or tradition, with the doubt in the row's note). The table is in the Search_Log.

**Not done.** No further scan of the New York Catholic Worker exists on archive.org. No first-hand print of William
Wadé Harris, Kimbangu, Kivebulaya, Rātana, Surma, Balakian, Kyrion II or Habib Girgis was found; the original prints
of the Moscow council of 1917-18 are on hosts that refuse automated clients.

### Next action

Mark works the hand-fetch list. Batch 3 (American books of 1931-1963 under R7; the remaining people and council
leads) goes to a fresh session.

## 2026-11-15 — The coverage feed regenerated, and a CI check added

**Decided (Mark, 2026-11-15: "yes fix the coverage file").** `cic-website/data/corpus-coverage.json` is a live
public feed, so it must match what `cic/engine/corpus_coverage.py` writes from `main`.

**Cause.** The file last matched its generator on 2026-11-09, at the merge of P2-G2 (`b9ed351d7`). It then went
stale: about 38 merges after that date changed the census (307 entries to 619, through the Church Family Tree data
releases 30 to 44), the corpus map and the vendored texts, and none regenerated the file. The generator itself has
not changed since 2026-09-26. Nothing checked the file: `cic/corpus-map/README.md` lists the command, but no CI
step or Library finish step required it. The Era 6 rulings and the shelf rulings of today each noted the file
as behind and left it for another pass.

**Done.** The file is regenerated from `main`: 619 entries (all in census order), 289 with coverage, 330 at zero.
The diff is explained by the inputs. All 307 earlier entries remain. 312 entries are new. 569 work rows are new.
13 old rows differ, each from a map change: shelf rulings changed a role or confidence (the Mirror of Perfection,
the Georgian chronicles), and the Pedalion and the two Synaxaristes left the Ottoman Orthodoxy 1453-1650 shelf
(`d398ed5c8`). Every entry's works carry a rights line read from the vendored file.
`.github/workflows/ci.yml` gains a step in `library-validators` that regenerates the file and fails on any
difference. The `library` path filter now also fires on `world-census.json` and `corpus-coverage.json`, since a
census change alone had been enough to make the file stale.

The enforced commentary check failed on one rights line the feed copies from a vendored header: the Hadewijch 1875
edition's header named Mark's ruling. On the coordinator's direction the sentence is reworded on its own line
(no line numbers moved), the generated `cic/texts/README.md` row is regenerated, and no other header carries the
cue.

**Not done.** The generator is unchanged.

### Next action

A Library batch runs `python cic/engine/corpus_coverage.py` after its last map or text change, and commits the
result, before its pull request, then runs `tools/check_live_commentary.py --base origin/main --enforce`.
## Era 9, batch 2b: rows 227-245, 249-262, 267-278, 323 and 327-330 (2026-11-15)

Sixty-one files for 49 person rows of the wanted list, and the date check left on row 223. Record:
`Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2b/Search_Log.md`, with `R1_review.md` and
`R1_changes.md` beside it; the rows and the cautions are in `CFT-Wants.md`, "Era 9 (1815-1906), batch 2b".

**Decided here.**
- Host additions are stripped at intake for the first time: Google's own preamble, from the twelve files that
  come from Google scans, and nothing else. Each header's Provenance note gives the lines and bytes removed.
  Because of this, line numbers in this batch's headers are the vendored file's own lines.
- Every content note and locus was written from the staged text by fresh checkers. Searchers supplied
  title-page facts and downloads only.
- An undated later printing is not taken on the first edition's date. Two picks were replaced by dated scans on
  this ground: the Life of Elder John Smith (the Cincinnati printing of 1870) and Cartwright's Autobiography
  (Carlton & Porter, 1857).
- A "First published" line under the imprint, with a dated introduction and the catalogue's date agreeing, is
  treated like a dated preface (Marchant's Life of Clifford, 1924). The header says so.
- Christendom Astray prints no year on its title page, and no library catalogue record stands behind the
  scan (a reader's upload, which gives 1884). It is dated 1883 from its preface (18 December 1883, read on the
  page image) and from the text's own closing date (7 December 1883). The header states this, and the point is
  put to the coordinator.
- OCR that cannot be read is not taken: Lohe's Neuendettelsau history in German (1907).
- Shelves follow the principle of 15 November. Nothing is left at `needs-ruling`. Dialogues on Prophecy (1828)
  is `antecedent` on the Catholic Apostolic Church. A church's history by its own officer inside the entry's
  window (Payne, Rush, Hamilton) is `tradition`.

**Held for Mark.**
- `collectionofsacr00smit`, Emma Smith's hymnbook of 1835 in a scan with an Intellectual Reserve copyright
  line. Not taken; the microfilm copy, which carries no such line, was taken in its place.

### Next action

Batch 3: the era 9 outside witnesses, the council records and the held eras 8-9 items.
## Era 9, batch 2a: Africa, Asia, Oceania, Latin America, the Caribbean and the Eastern churches (2026-11-15)

Seventy-one files for the era 9 person rows outside Britain, Europe and North America, with batch 1's
not-found rows tried again and its owed date checks done. Three files vendored here were dropped before the
merge because another batch had put the same scan on main first: Aglipay's Catequesis (era 10 batch 1),
Launay's Histoire générale, tome 2 (era 8 batch 1) and Neatby's History of the Plymouth Brethren (era 9 batch
2b). The map rows for Minh Mang's edict in Launay and for Darby in Neatby now stand on main's files. Record:
`Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2a/Search_Log.md`; the rows are in `CFT-Wants.md`,
"Era 9 (1815-1906), batch 2a".

**Ruled by Mark (15 November, given to this thread in the coordinator's brief).**
- On shelves, verbatim: "follow your recomondations for all shelfs". The principle, as the brief states it: a
  tradition's own text with a doubt about date or authorship is `tradition`, with the doubt in the row's note.
  A later reworking, compilation, biography or other witness written by others is `context`. A work written
  before an entry's window that the entry grows from is `antecedent`. An outside witness with no census entry
  of its own is `context` on the nearest entry, with the missing entry logged as a census gap.
- On scope, verbatim: "but add the church family needs and global and any language peices".

**Calls by the coordinator under Mark's rights rulings, applied here.** A printed licence or approbation leaf
counts like a dated preface. A year printed in the title on the title page counts when the catalogue agrees and
the publisher and place match the first printing. The Dictionary of African Christian Biography is cite and
link only (CC BY-NC 4.0, under R3).

**Decided here.**
- Batch 1's eighteen `needs-ruling` rows are decided by the principle. `tradition`: Finney's Memoirs, Irving's
  Collected Writings vol. 5, Bavinck's two books of 1909, Disselhoff's jubilee memoir. `antecedent`: Briggs's
  Defence, the Hodge and Warfield article of 1881, McAuley's Transformed. `context`: the two parts of the case
  against Briggs, Noyes's Religious Experience (a compilation of 1923), Offord's McAuley, Phillips's Evan
  Roberts, Lindley vol. 1, Page's Crowther, the two Howard Taylor volumes, Cunninghame Graham. Each row's note
  says why, and each now carries confidence `assigned`, as the rows of the shelf-rulings entry above do. None is
  left at `needs-ruling`.
- The same principle for this batch. A missionary's own first-hand book is `tradition` on the mission church's
  entry (Casalis, Jessup, Hannington's journals, Bleby, Mary Mead Clark). A history or Life compiled by
  another is `context` (Ellis, Freeman and Johns, Louvet, Launay, Dawson, Bond). Captives, consuls and soldiers
  are `context` (Stern, Blanc, Wylde, Meadows, Brine, Macedo Soares). A text of the tradition printed a few
  years after its entry's window stays `tradition`, with the year in the note (Sheptytsky 1911, Jessup 1910). No outside witness in this batch lacks a census entry, so no census gap is logged.
- A copyright notice or a dated preface stands for the date only where the rule's test is met in full. Kuyper's
  Stone Lectures, A Retrospect, Walsh and the London sermon of Aggressive Christianity fail it and stay out.
  A censor's leaf without a catalogue record to agree (Makary Glukharev's Mysli, 1894) stays out too.
- Where the catalogue's two date fields differ by a year, the scan was not taken on a preface; another scan
  whose title page prints the year was found (Ellis's Martyr Church, MDCCCLXX).
- One host file holds two volumes with different dates: the Chronicle of Menelik II, tome I (1930) and tome II
  (1932). Only tome I is held. The file is cut before tome II's title page, and the header says so.
- At intake the host's own additions are removed by rule, not by hand: Google's preamble and lines that hold
  only the scanner's page mark. One preamble that the OCR read as Greek letters was removed by its line range.
  Each header says what was removed. Line numbers in headers and shelf rows are the file's own.
- dbnl.org is treated as a host that refuses automated clients: its robots file disallows all but two named
  search engines, and a search request was answered 429. Nothing was fetched from it.
- A lending-library scan is not taken even where the book is old (Jessup, vol. 1); another scan was found.

**Held for Mark.**
- Os Sertoes: no printing of 1902 to 1911 other than the 1905 one with the non-commercial notice was found.
- The hand-fetch list in the search log: eight wants on hosts that need a browser.

### Next action

Era 9, batch 2b, in a fresh session: rows 227-245, 249-262, 267-278, 323 and 327-330 (Britain, Europe, North
America), and the Kaiserswerth date check. Then batch 3: the outside witnesses, the council records and the
held eras 8-9 items.

## Era 8, batch 2: the British Isles, North America, Catholic Europe and the Jesuits (2026-11-15)

**Done.** 37 files (5,346,333 words) for the era 8 wants of Britain, North America and Catholic Europe, and the
volumes batch 1 found and left. The files and the rows not filled are in `CFT-Wants.md` ("Era 8 (1650-1815),
batch 2"). The page-image reads, the calls and the cautions for writers are in
`Build/Ministry/Operations/Audits/2026-11-15_library-era8-b2/Search_Log.md`.

**Scope, by the coordinator's instruction.** The era 8 rows of the cards' "Texts to fetch" list were not taken.
That list came from the legend check and is dropped for every era. Gobat's New York printing of 1850 is left
out as a later printing of a held text. No quote, story or lexicon entry was rendered; rendering waits until
Mark has seen a proposal and a sample.

**Decided during the batch.**
- **Love's Samson Occom is taken under R12.** The title page prints no year; the copyright notice on its verso
  reads 1899, and the preface and the catalog agree.
- **Taft's Holy Women is taken on its printed years.** The scan is a reader's upload with no catalog record; it
  photographs an old bound copy whose title pages print 1825 and 1828.
- **Valentijn, deel 2, and the Code noir of 1743 are not taken.** Both pass on rights. Neither adds church
  matter to what is held (Valentijn's deel 3; the Code noir collection of 1767).
- **The shelf principle, applied.** A person's own text is `tradition` on that person's entry (Dutton, Davies,
  McGready, Campbell, Murray, Fontaine, du Fossé, Quesnel, Vieira, Dobrizhoffer). A Life written inside the
  tradition and inside the entry's window is `tradition` (Gibbons on Watts, Orton on Doddridge, the Life of
  Bray, Marsollier on Rancé, Soli on Muratori). A later Life or history is `context`, with the subject's own
  letters named in the note (Roberts, the Wilberforce sons, Gregory, Taft, Love, Walker, Cooley, Pascoe,
  Launay). A first-hand piece printed inside a later book has its own `tradition` row under its writer (Occom,
  Cole, Haynes, Cattaneo, Rancé's Pensées). Muratori on Paraguay is `context` on the Jesuits' entry: the census
  names the book there, and he was not a Jesuit.
- **Three rows are `needs-ruling`.** Parry on `the-sayfo-and-the-syriac-diaspora` (the census has no entry for
  the Syriac Orthodox between 1650 and 1906); Charmot's Vindiciae on `chinese-catholicism-1650-1906` (it
  follows the main volume's row for Charmot); Quesnel's Réflexions as the condemned text on
  `catholic-church-ancien-regime`.
- **Two corrections of year, both made on the page image.** Parry's title page prints 1895; the OCR reads
  "1896.". Campbell's Centennial reprint is of 1908, printed on the leaf after a title page that has no year;
  the OCR reads "1906". The first notes followed the OCR in both. The review caught the second.
- **A first-hand piece by another hand has its writer's slug**, with an `authors_ruled` entry in the staging
  file (Finley, Gibbons and Bostwick on Davies; Russell's essay on Doddridge).
- Host bytes are kept whole. Nothing was stripped at intake, so line numbers in headers and shelf rows are the
  host's, with 12 added for the file's own.

### Next action

Era 9 batch 2b's "located, not yet taken" volumes; then era 10 batch 2's follow-on list; then era 8 batch 3.

## Era 9, the located volumes: the follow-on to batch 2b (2026-11-16)

**Done.** 27 files (4,092,114 words): the further volumes and other witnesses that era 9 batch 2b located and
did not take. The files and the rows not filled are in `CFT-Wants.md` ("Era 9 (1815-1906), the located
volumes"). The page-image reads, the corrections to the list, the calls and the cautions for writers are in
`Build/Ministry/Operations/Audits/2026-11-16_library-era9-located/Search_Log.md`. Seven works are now held
whole: the Dialogues on Prophecy, Drummond's Speeches, Froude's Remains, and the Lives of Samuel Wilberforce,
Shaftesbury, Maurice and Wiseman.

**Scope, by the coordinator's instruction.** Only the "Located, not yet taken" volumes. The 134 card rows of
batch 2b's list were not taken; that list came from the legend check and is dropped. Later printings of held
texts are not taken again (In His Steps, 1899; Newton's Thoughts on the Apocalypse, 1904). No rendering.

**Decided during the batch.**
- **A dated report with no year on its cover is not taken on its own text.** The Pacific Garden Mission's
  statement for the year ended 15 September 1916 has no printed year, no copyright notice and no catalog date,
  only an auditor's letter of 17 November 1916. That is none of the bases the rights rule and R12 list, so the
  file was vendored and then taken out after the review, and is held for Mark.
- **A reader's upload with no catalog record is taken on its printed year** where every date in it is a
  century before the line (Dialogues on Prophecy, vol. II, 1828), as Taft's volumes were in era 8 batch 2.
- **A year is read on the page image wherever the OCR's year is garbled or missing, or differs from the host's
  date.** Fifteen leaves were read, and the reviewer read nine more. Two years the OCR had dropped altogether were on the page (Cox, 1888;
  Mott, 1892), so neither file needed R12.
- **Further volumes keep the shelf, role and author slug of the held volume**, except where the later volumes
  have another writer on their title page (R. G. Wilberforce for vols. 2 and 3 of the Life Ashwell began).
- **A volume of several histories gets a shelf row only for the wanted one** (Hamilton's Moravian history in
  the American Church History volume).
- Host bytes are kept whole; line numbers in headers and shelf rows are the host's, with 12 added for the
  file's own.

### Next action

Era 10 batch 2's follow-on list (Open-Gaps 300); then era 8 batch 3 (Open-Gaps 301).

## Era 10, batch 2b, the periodicals: the follow-on to batch 2 (2026-11-16)

**Done.** 45 files (4,325,430 words): 31 numbers of The Christian East and 14 volumes of The International
Review of Missions, which era 10 batch 2 found and did not take. The files are in `CFT-Wants.md` ("Era 10,
batch 2b, the periodicals"). The page-image reads, the calls and the cautions for writers are in
`Build/Ministry/Operations/Audits/2026-11-16_library-era10-b2b-periodicals/Search_Log.md`. Every number of The
Christian East's vols. I-X is now held, and every volume of the International Review from 1914 to 1930.

**Scope, by the coordinator's instruction.** The three periodicals of batch 2's follow-on list, as listed. The
books of that list are the next batch. The International Review for 1912 and 1913 and the Proceedings of the
Church Missionary Society for 1906-1909 are a later batch of era 10; the Proceedings before 1906 are era 9's.
No rendering.

**Decided during the batch.**
- **A scan of a microfilm that carries the film maker's copyright line and a prohibition is not taken.** The
  Proceedings of the Church Missionary Society for 1910-1921 were scanned from a film whose target leaf reads
  "© MM 1967 / Reproduction of this film prohibited". The prints are dated 1910 to 1921, but such a notice on
  the scan is not a basis the rights rule or R1 to R12 list. The twelve volumes were held, and Mark then ruled
  (see "Three rights rulings" below): they stay out.
- **A number dated across two years is not taken on its first year.** The Christian East's "Winter, 1930-31"
  cites a letter of March 1931; it is held for Mark and is past the line until January 2027.
- **A number filmed without its cover is taken on its masthead date**, and its header says that no publisher
  or editor is printed in the number as scanned. The publisher and editors are given only for the eleven
  numbers whose cover was filmed and read.
- **A periodical gets one shelf row for the whole number or volume, and further rows only for documents whose
  first and last lines were found.** A church leader's own document goes on that church's entry as tradition;
  an outside report goes on the entry it reports as context.
- **The International Review before 1921 goes on the Student Volunteer Movement and Edinburgh 1910 entry**,
  and from 1921 on the ecumenical movement entry, where the held volumes are.
- Host bytes are kept whole; line numbers in headers and shelf rows are the host's, with 12 added for the
  file's own.

**Three rights rulings, passed on by the coordinator (2026-11-16).** Each came to this thread in a coordinator
message that quotes Mark's answer to a question the coordinator put to him; the words in quotation marks are
his, and the statement of each rule is the coordinator's. They are recorded in `cic/texts/INTAKE.md` section 2.

- **The film-notice ruling (Mark, 2026-11-16: "Yes, keep them held (Recommended)").** A microfilm maker's notice
  on a scan blocks taking it, even when the print itself is old. The Proceedings of the Church Missionary
  Society from that film stay out for every year. Another scan of the same print with no notice may be taken
  where one can be found. Searched on 16 November: archive.org has no other scan of the Proceedings for 1906 to
  1921 (it has Google scans of volumes of 1819 to 1834 and one of 1855-56); HathiTrust's catalog search refused
  the request (HTTP 403) and the Google Books search refused it for quota (HTTP 429). The coordinator gave this
  ruling no number.
- **R13, an institution's dated report (Mark, 2026-11-16: "Yes, with a page-image check (Recommended)").** An
  institution's report (an annual statement, a proceedings) counts by a date printed in its own text, when that
  date is read on the page image and the header records where it was found. Under it the Pacific Garden
  Mission's statement of 1916, left out of the era 9 located volumes, can be taken; it goes with the next batch.
- **R14, a host's own additions (Mark, 2026-11-16: "Allow it, with a note (Recommended)").** A host's own
  additions (page-foot stamps, watermark text, host banners) may be removed at intake, but never anything of the
  printed work. Each file header records what was removed: the exact text, how many lines, and the host URL with
  the original byte count. The raw copies are not kept in the repo. The files of Путь on main give the stamp's
  text, the line count, the item and the byte count, and not a URL; their headers are to be brought to R14 in
  the next pull request. Nothing was removed from any file of this batch.

### Next action

The books of era 10 batch 2's follow-on list, with the Pacific Garden Mission's statement of 1916 and the
headers of Путь (Open-Gaps 302); then era 8 batch 3 (Open-Gaps 301); then the International Review for 1912 and
1913 (Open-Gaps 303).
