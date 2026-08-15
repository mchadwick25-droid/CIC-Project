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
| `anf04_tertullian4-minucius-felix-commodian-origen1-2.txt` | ANF04. Fathers of the Third Century: Tertullian, Part Fourth; | Public Domain | Mark | 2026-08-15 | - |
| `anf05_hippolytus-cyprian-caius-novatian.xml` | ANF05. Fathers of the Third Century: Hippolytus,
    Cyprian, Caius, Novatian, Appendix | Public Domain | Mark | 2026-08-15 | - |
| `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` | ANF06. Fathers of the Third Century: Gregory
    Thaumaturgus, Dionysius the Great, Julius Africanus, Anatolius,
    and Minor Writers, Methodius, Arnobius | Public Domain | Mark | 2026-08-15 | - |
| `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` | ANF07. Fathers of the Third and Fourth Centuries: Lactantius, Venantius, Asterius, Victorinus, Dionysius, Apostolic Teaching and Constitutions, Homily, and Liturgies | Public Domain | Mark | 2026-08-15 | `pahcq005`, `srcPAHCS63` |
| `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` | ANF08. The Twelve Patriarchs, Excerpts and Epistles, The Clementia, Apocrypha, Decretals, Memoirs of Edessa and Syriac Documents, Remains of the First Age | Public Domain | Mark | 2026-08-15 | - |
| `anf09_gospel-of-peter-diatessaron-origen-commentaries.txt` | ANF09. The Gospel of Peter, The Diatessaron of Tatian, The | Public Domain | Mark | 2026-08-15 | - |
| `npnf204_athanasius-select-works-letters.txt` | NPNF2-04. Athanasius: Select Works and Letters | Public Domain | Mark | 2026-08-15 | `ijcq001`, `srcIJC42` |

Notes carried over per file:

- **`anf01_apostolic-fathers-justin-irenaeus.xml`** -- CCEL's native ThML source, SWAPPED IN 2026-08-15 for the plain-text rendering that originally carried this id - same volume, same rights basis, verified byte-identical on all four passages already committed as quote records (pahcq001-004) before the swap. Structurally better for this build's own purposes: shorter/longer/Syriac recensions are addressable by id (e.g. v.v.iv-p1 vs v.v.iv-p4 for Romans 4), and footnotes are their own <note> elements rather than interleaved apparatus text - both real friction points hand-transcribing the plain text had already hit. Extracting text correctly requires walking element trees properly, not naive regex: a lazy `<p>...</p>` match truncates early against nested <note><p class="endnote">...</p></note> structures, and a node's own skip-tag status must not be applied to its `tail` text - both mistakes were made and caught live during this swap, on the Smyrnaeans and Martyrdom-of-Polycarp passages respectively, before anything was recommitted.
- **`anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`** -- Shepherd of Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria. Swapped from the plain-text rendering the same day, as anf01 was - no record cited the old .txt file (this volume's own zero-citation status, unchanged), so this swap needed no re-verification of any existing quote.
- **`anf03_tertullian.xml`** -- Carries Tertullian's Apologeticus, the primary text srcPAHCP15 already cites in pahc ('Tertullian, Apology 39'). No quote record was in this session's worklist, so none was written, but the translation edition is available if one is ever wanted. Swapped from the plain-text rendering the same day, as anf01/anf02 were - zero citations before the swap, so nothing needed re-verification.
- **`anf04_tertullian4-minucius-felix-commodian-origen1-2.txt`** -- Tertullian Pt. 4, Minucius Felix, Commodian, Origen Pts. 1-2.
- **`anf05_hippolytus-cyprian-caius-novatian.xml`** -- Hippolytus, Cyprian, Caius, Novatian. Carries ~82 of Cyprian's own letters plus On the Lapsed, On the Mortality, and Pontius's Life of Cyprian - primary-source material for the not-yet-built Latin Pastoral-Congregational Christianity world (census: 'Selected - Not Yet Built'). Swapped from the plain-text rendering the same day, as anf01/02/03 were - zero citations before the swap, so nothing needed re-verification. Structured letter/chapter ids here would matter directly once that world is built: Cyprian's ~82 letters are individually addressable rather than needing to be located by reading forward through flowing prose.
- **`anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`** -- This volume's own 'Julius' is Julius Africanus the chronographer, a named author here - NOT Julius I of Rome (srcIJC04/srcIJC42). Swapped from the plain-text rendering the same day, as anf01/02/03/05 were - zero citations before the swap, so nothing needed re-verification.
- **`anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`** -- Carries the Didache, published too late for ANF vol. 1 - closed the deferred gap srcPAHCS62 named. Translator for the Didache specifically: Isaac H. Hall and John T. Napier (Sunday-School Times, 1884), not the volume's general editors. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06 were - unlike those, this one had an existing quote (pahcq005) and source (srcPAHCS63) citing it, so both were re-verified against the XML with the tail-aware element walker before the swap, not just before it was trusted: the committed wording matched exactly.
- **`anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`** -- Carries Abgar/Edessa correspondence material, relevant to syriac world (syrfig005, Addai) - not drawn on so far; that figure's own record already treats him as legend, not history. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06/07 were - zero citations before the swap, so nothing needed re-verification.
- **`anf09_gospel-of-peter-diatessaron-origen-commentaries.txt`** -- Origen's Commentaries on John and Matthew, among others.
- **`npnf204_athanasius-select-works-letters.txt`** -- The volume srcIJC42 was scoped for from the start. Closed the last inert Check B cell in the fleet (ijcq001, Julius I's letter of 341).

Not records: nothing here is schema-validated or read by the runtime. These are reference copies for verification, cited by the `source`/`quote` records that carry the bibliographic and wording claims.
