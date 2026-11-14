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
