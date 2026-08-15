# Vendored public-domain source texts

Full text of editions this build's quote records cite, committed so that
wording can be verified *reproducibly* -- by any session, at any time,
without network access. That matters here for a specific reason: the
sandbox this project's agents run in blocks every patristic text host
(ccel.org, newadvent.org, wikisource, archive.org, gutenberg, tertullian.org),
so before these files existed a quote record could not be verified at all
and `gate_quote_fidelity_recording` had nothing honest to record.

**This file is GENERATED, not hand-edited** -- run
`python cic/engine/texts_registry.py --write-readme` after vendoring a new
file or adding an ENTRIES row in that module. Editing this table directly
will be overwritten the next time it runs.

PUBLIC DOMAIN ONLY. Every file here must be out of copyright, and its own
provenance header must say so -- the `rights` column below is read fresh
from each file's own header every time this report runs, not trusted from
a claim made when the file was added. In-copyright editions (Holmes 2007,
Ward 1975) are referenced by `source` record and never vendored --
committing them would be redistribution.

| file | title (from the file's own header) | rights | supplied | added | cited by |
|---|---|---|---|---|---|
| `anf01_apostolic-fathers-justin-irenaeus.xml` | ANF01. The Apostolic Fathers with Justin Martyr and Irenaeus | Public Domain | Mark | 2026-08-15 | `pahcq001`, `pahcq002`, `pahcq003`, `pahcq004` |
| `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` | ANF02. Fathers of the Second Century: Hermas, Tatian, Athenagoras, Theophilus, and Clement of Alexandria (Entire) | Public Domain | Mark | 2026-08-15 | - |
| `anf03_tertullian.xml` | ANF03. Latin Christianity: Its Founder, Tertullian | Public Domain | Mark | 2026-08-15 | - |
| `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` | ANF04. Fathers of the Third Century: Tertullian, Part Fourth; Minucius Felix; Commodian; Origen, Parts First and Second | Public Domain | Mark | 2026-08-15 | - |
| `anf05_hippolytus-cyprian-caius-novatian.xml` | ANF05. Fathers of the Third Century: Hippolytus,
    Cyprian, Caius, Novatian, Appendix | Public Domain | Mark | 2026-08-15 | - |
| `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` | ANF06. Fathers of the Third Century: Gregory
    Thaumaturgus, Dionysius the Great, Julius Africanus, Anatolius,
    and Minor Writers, Methodius, Arnobius | Public Domain | Mark | 2026-08-15 | - |
| `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` | ANF07. Fathers of the Third and Fourth Centuries: Lactantius, Venantius, Asterius, Victorinus, Dionysius, Apostolic Teaching and Constitutions, Homily, and Liturgies | Public Domain | Mark | 2026-08-15 | `pahcq005`, `srcPAHCS63` |
| `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` | ANF08. The Twelve Patriarchs, Excerpts and Epistles, The Clementia, Apocrypha, Decretals, Memoirs of Edessa and Syriac Documents, Remains of the First Age | Public Domain | Mark | 2026-08-15 | - |
| `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` | ANF09. The Gospel of Peter, The Diatessaron of Tatian, The
 Apocalypse of Peter, the Vision of Paul, The Apocalypse of the Virgin
 and Sedrach, The Testament of Abraham, The Acts of Xanthippe and
 Polyxena, The Narrative of Zosimus, The Apology of Aristides, The
 Epistles of Clement (complete text), Origen’s Commentary on John,
 Books 1–10, and Commentary on Matthew, Books 1, 2, and
 10–14. | Public Domain | Mark | 2026-08-15 | - |
| `anf10_bibliographic-synopsis-general-index.xml` | ANF10. Bibliographic Synopsis; General Index | Public Domain | Mark | 2026-08-15 | - |
| `npnf104_augustine-anti-manichaean-anti-donatist.xml` | NPNF1-04. Augustine: The Writings Against the Manichaeans 
and Against the Donatists | Public Domain | Mark | 2026-08-15 | - |
| `npnf201_eusebius-church-history-life-of-constantine.xml` | NPNF2-01. Eusebius Pamphilius: Church History, Life of Constantine, Oration in Praise of Constantine | Public Domain | Mark | 2026-08-15 | `ijcq003`, `srcIJC45` |
| `npnf204_athanasius-select-works-letters.xml` | NPNF2-04. Athanasius: Select Works and Letters | Public Domain | Mark | 2026-08-15 | `ijcq001`, `srcIJC42` |
| `npnf210_ambrose-select-works-letters.xml` | NPNF2-10. Ambrose: Selected Works and Letters | Public Domain | Mark | 2026-08-15 | `ijcq002`, `srcIJC43` |

Notes carried over per file:

- **`anf01_apostolic-fathers-justin-irenaeus.xml`** -- CCEL's native ThML source, SWAPPED IN 2026-08-15 for the plain-text rendering that originally carried this id - same volume, same rights basis, verified byte-identical on all four passages already committed as quote records (pahcq001-004) before the swap. Structurally better for this build's own purposes: shorter/longer/Syriac recensions are addressable by id (e.g. v.v.iv-p1 vs v.v.iv-p4 for Romans 4), and footnotes are their own <note> elements rather than interleaved apparatus text - both real friction points hand-transcribing the plain text had already hit. Extracting text correctly requires walking element trees properly, not naive regex: a lazy `<p>...</p>` match truncates early against nested <note><p class="endnote">...</p></note> structures, and a node's own skip-tag status must not be applied to its `tail` text - both mistakes were made and caught live during this swap, on the Smyrnaeans and Martyrdom-of-Polycarp passages respectively, before anything was recommitted.
- **`anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`** -- Shepherd of Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria. Swapped from the plain-text rendering the same day, as anf01 was - no record cited the old .txt file (this volume's own zero-citation status, unchanged), so this swap needed no re-verification of any existing quote.
- **`anf03_tertullian.xml`** -- Carries Tertullian's Apologeticus, the primary text srcPAHCP15 already cites in pahc ('Tertullian, Apology 39'). No quote record was in this session's worklist, so none was written, but the translation edition is available if one is ever wanted. Swapped from the plain-text rendering the same day, as anf01/anf02 were - zero citations before the swap, so nothing needed re-verification.
- **`anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`** -- Tertullian Pt. 4, Minucius Felix, Commodian, Origen Pts. 1-2. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06/07/08/09 were - zero citations before the swap, so nothing needed re-verification.
- **`anf05_hippolytus-cyprian-caius-novatian.xml`** -- Hippolytus, Cyprian, Caius, Novatian. Carries ~82 of Cyprian's own letters plus On the Lapsed, On the Mortality, and Pontius's Life of Cyprian - primary-source material for the not-yet-built Latin Pastoral-Congregational Christianity world (census: 'Selected - Not Yet Built'). Swapped from the plain-text rendering the same day, as anf01/02/03 were - zero citations before the swap, so nothing needed re-verification. Structured letter/chapter ids here would matter directly once that world is built: Cyprian's ~82 letters are individually addressable rather than needing to be located by reading forward through flowing prose.
- **`anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`** -- This volume's own 'Julius' is Julius Africanus the chronographer, a named author here - NOT Julius I of Rome (srcIJC04/srcIJC42). Swapped from the plain-text rendering the same day, as anf01/02/03/05 were - zero citations before the swap, so nothing needed re-verification.
- **`anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`** -- Carries the Didache, published too late for ANF vol. 1 - closed the deferred gap srcPAHCS62 named. Translator for the Didache specifically: Isaac H. Hall and John T. Napier (Sunday-School Times, 1884), not the volume's general editors. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06 were - unlike those, this one had an existing quote (pahcq005) and source (srcPAHCS63) citing it, so both were re-verified against the XML with the tail-aware element walker before the swap, not just before it was trusted: the committed wording matched exactly.
- **`anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`** -- Carries Abgar/Edessa correspondence material, relevant to syriac world (syrfig005, Addai) - not drawn on so far; that figure's own record already treats him as legend, not history. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06/07 were - zero citations before the swap, so nothing needed re-verification.
- **`anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`** -- Origen's Commentaries on John and Matthew, among others. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06/07/08 were - zero citations before the swap, so nothing needed re-verification.
- **`anf10_bibliographic-synopsis-general-index.xml`** -- NEW, not a swap - this volume was never vendored as plain text. A finding aid, not primary source content: Biographical Synopsis, Index of Subjects, Index of Texts, and the General Index to the whole Ante-Nicene Fathers set - 66KB against the 3-4.5MB of every content volume, 11 top-level divs with no chapter/letter text of its own. Its 'cited by' count will legitimately stay at zero permanently, unlike every other volume here where zero means only 'not yet drawn on' - this one carries nothing a quote record could ever cite as translation_used. Kept for its actual use: faster location of passages across the other nine volumes when authoring future quotes.
- **`npnf104_augustine-anti-manichaean-anti-donatist.xml`** -- NPNF Series I, Vol. 4: Augustine - The Writings Against the Manichaeans (and Against the Donatists). Arrived first labeled 'npnf204' by mistake - its own <DC.Title> read directly from the file caught the mismatch before anything was touched (it is Series I vol. 4, NPNF1-04, not Series II vol. 4 / Athanasius). No quote record cites it and none is planned yet, but it is real, useful primary-source material in its own right: Augustine's own anti-Donatist writings are, per the census's own note on the not-yet-built Donatism world, the primary route by which Donatist voices (Donatus, Petilian, Tyconius) survive at all - 'known only through Augustine's quotations.' A future Donatism world would need this volume's own doubly-mediated quoting discipline, the same shape already proven for Julius's letter (license only the quoted portion, leave the surrounding corpus Excluded).
- **`npnf201_eusebius-church-history-life-of-constantine.xml`** -- NPNF Series II, Vol. 1: Eusebius Pamphilius: Church History, Life of Constantine, Oration in Praise of Constantine. Supplied with no accompanying text, read as continuing 'deepen imperial_juridical' (Julius, then Ambrose, now Eusebius) - ijcq003. Found a real scoping mismatch, not a misattribution: the world's only prior Eusebius source row (srcIJC02) cites 'esp. 4.24' and licenses a different claim ('bishop of those outside') than the vision-under-oath account ijcstory001 actually attests. Rather than stretch srcIJC02 to cover it, the chapter was located independently by title search (Book I, ch. 28) and two new, narrowly-scoped rows written (srcIJC44 primary, srcIJC45 translation); srcIJC02 itself was left untouched. Also notable: this volume's two works have different translators (McGiffert for Church History, a Bagster translation revised by Richardson for Life of Constantine) under one shared <DC.Creator> block - checked per-chapter rather than assumed from the volume-level header, the same discipline that caught srcIJC42's Newman/Robertson split.
- **`npnf204_athanasius-select-works-letters.xml`** -- The volume srcIJC42 was scoped for from the start. Closed the last inert Check B cell in the fleet (ijcq001, Julius I's letter of 341). Swapped from the plain-text rendering the same day as the ANF set - ijcq001's committed wording re-verified against the XML with the tail-aware element walker before the swap; the letter itself is cleanly its own titled sub-division here ('Letter of Julius to the Eusebians at Antioch'), an even cleaner boundary than the paragraph-number locus the plain text required.
- **`npnf210_ambrose-select-works-letters.xml`** -- NPNF Series II, Vol. 10: Ambrose: Select Works and Letters. Supplied for ijcq002 - deepening imperial_juridical past its single Julius quote. Closed reading this volume found a real misattribution risk before it was committed: a strong, verbatim line on 'the Church belongs to God' looked like the obvious candidate for the basilica-standoff quote, found by a raw text search, but tracing its actual element ancestry showed it belongs to a different work entirely - Concerning Repentance, Book II - not the Sermon Against Auxentius. Discarded before use; ijcq002 cites only text confirmed, by walking the tree, to sit inside the correct sermon.

Not records: nothing here is schema-validated or read by the runtime. These are reference copies for verification, cited by the `source`/`quote` records that carry the bibliographic and wording claims.
