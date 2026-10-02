# Source Readiness Dossier — Syriac Orthodox (West Syriac) Christianity

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** II.2
**Corpus-map slug:** `syriac-orthodox-west-syriac-christianity`
**Time window:** 451-636 CE
**Region(s):** Syria, Mesopotamia
**Dossier author / date:** wsyr library-stage build thread, 2026-09-25
(Revision 2, following an independent Opus adversarial review of Revision 1
— `worlds/wsyr/Review-Artifacts/Step0_Doc01_Doc02_Round1_Review.md` — that
corrected several claims in this dossier's own §1 and §3, noted inline
below)
**Corpus-map / `cic/texts/` state as of:** this session (2026-09-25) — the
seven files in Table 1 and the corpus-map assignments in §1 below were
added by this same session; nothing here predates a checkable commit.

## 1. Already assigned

**Newly vendored and assigned this session** (full detail and verification
loci: `worlds/wsyr/Doc_02_Source_Ecology.md` §2 Table A):

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Lives of the Eastern Saints | john-of-ephesus | tradition | assigned | 58 chapters, ~1.38 MB OCR | `john-of-ephesus_lives-of-the-eastern-saints_brooks1923.txt` |
| Ecclesiastical History, Part III | john-of-ephesus | tradition | assigned | **Books I-VI in translation** (corrected Revision 2 — a Revision 1 error described this as "1 book + index" and hid real Tritheist-controversy and Paulite-schism material as a result), ~790 KB OCR | `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` |
| Select Letters, Book VI (Parts I-II) | severus-of-antioch | tradition | assigned | 123 letters, ~785 KB OCR combined | `severus-of-antioch_select-letters-book6-part1_brooks1903.txt`, `...part2_brooks1904.txt` |
| The Discourses of Philoxenus, **plus the same volume's own Creed, Confession of Faith, and anti-Nestorian doctrinal texts** (corrected Revision 2 — Revision 1 described this volume as ascetic-only) | philoxenus-of-mabbug | tradition | assigned | 13 discourses + several doctrinal texts, ~1.3 MB OCR | `philoxenus-of-mabbug_discourses_budge1894.txt` |
| The Chronicle of Joshua the Stylite | joshua-the-stylite | context (open, see below) | provisional | 1 chronicle, ~316 KB OCR | `joshua-the-stylite_chronicle_wright1882.txt` |
| The Syriac Chronicle known as that of Zachariah of Mitylene (**Books III-VI: own-voice, Severus-sympathetic material — corrected Revision 2, reversed from a Revision 1 finding that wrongly called this material Chalcedonian/opponent-voice; Books I-II, VII-XII: unassessed continuator material**) | pseudo-zachariah-rhetor | tradition (open, see below) | provisional | 1 compilation, ~718 KB OCR | `zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` |

**Already in the bucket before this session** (inherited, reviewed at
Doc_02 §2 Table B, not recreated):

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Arabic Gospel of the Infancy of the Saviour | arabic-gospel-of-the-infancy | transmission | assigned | `anf08_...` |
| The Chronicle of Edessa | chronicle-of-edessa | context | provisional | `chronicle-of-edessa_cowper.txt` |
| A Canticle of Mar Jacob the Teacher on Edessa | jacob-of-sarug | tradition | assigned | `anf08_...` |
| The Divine Liturgy of James | liturgy-of-st-james | tradition | provisional | `anf07_...` |

Total: 11 work-rows, 8 distinct vendored files (7 new this session, 3
shared with other worlds' own buckets: `anf07`, `anf08`,
`chronicle-of-edessa_cowper.txt`).

## 2. Cross-link opportunities

Checked this session, not exhaustively (a fuller sweep of every corpus-map
staging file mentioning Antioch/Syria/Chalcedon/miaphysite terms was not
run — flagged as a real gap in this dossier pass, not claimed as done):

- **`syr`'s own corpus** (Ephrem, Aphrahat) was checked directly for any
  explicit engagement with this world's own post-451 controversy — none
  found; `syr`'s own window (200-410) ends four decades before this
  world's own opens (Doc_01 §8), so no direct cross-link is expected and
  none was forced.
- **`ijc`'s own corpus** (Imperial and Juridical Christianity, 312-451) —
  not checked this session for pre-451 material touching this movement's
  own antecedents (e.g., the Christological build-up to Chalcedon itself,
  Cyril of Alexandria's own "mia physis" language, which this world's own
  theology directly descends from). A real, named gap: whoever next works
  this dossier should check `ijc`'s own bucket for Cyril-adjacent material
  before assuming none exists.
- No cross-link to a not-yet-built Egyptian miaphysite world was pursued
  (no such world's corpus-map bucket exists yet to check against) — named
  per Doc_01 §8's own B3 discussion (the two candidates share a
  theological family but differ structurally) as worth a joint check once
  such a bucket exists.

## 3. Verified acquisition leads

Public-domain editions not yet vendored anywhere, each independently
confirmed against its actual host this session (archive.org, via its own
`/metadata/<id>` API and direct file download, not title-matching):

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Sixth Book of the Select Letters of Severus of Antioch, Vol. I (Syriac text) | Severus of Antioch | E. W. Brooks (editor) | 1902 (per the parallel translation volumes' own dating) | https://archive.org/details/selectlettersse00broogoog (and sibling scans — several duplicate archive.org items exist for this volume, not yet disambiguated) | pd-us-by-date | Located via archive.org search, 2026-09-25; metadata fetched, NOT downloaded or vendored this session (original-language Syriac text, lower priority than the translation volumes already vendored — see `cic/texts/INTAKE.md` §"original-language texts" for why this is a real, not merely optional, acquisition path if a future session wants Severus's own Syriac text as primary evidence rather than only in English translation) |
| Zacharias Scholasticus, *Life of Severus* (Vie de Sévère) | Zacharias Scholasticus of Gaza | **Corrected Revision 2, uncertain — not confirmed as Kugener.** The Brooks 1903 introduction itself names "M. Nau" as the French translator; a separate Kugener translation of the same Life (Patrologia Orientalis 2, 1907) is also real and well known in the scholarship, but Revision 1 of this dossier wrongly presented the Brooks quote as supporting the Kugener edition specifically. Not disambiguated this session — either or both may be real, independent translations. | Nau: not independently checked. Kugener/PO 2: 1907 | not checked against a specific archive.org identifier for either translator this session | pd-us-by-date (likely, not independently confirmed for either) | Named in the Brooks 1903 introduction as the primary biographical source for Severus's own early life. A real, named, not-yet-verified acquisition lead — Mark should independently confirm which translator/edition and its archive.org identifier before this is treated as a cleared lead. |
| Severus of Antioch, Cathedral Homilies (selections) | Severus of Antioch | Maurice Brière (French, Patrologia Orientalis, various volumes) | early-to-mid 20th c. | not checked this session | pd-us-by-date (likely for the earliest volumes; needs per-volume date check) | Named here as a real target for Severus's own doctrinal voice (Doc_02 §11 item 8's own gap), not independently verified this session — French translation, not English, which the project's own intake rule (`INTAKE.md`) treats as acceptable primary evidence but a harder verification task for an English-reading build thread. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Pseudo-Zachariah Rhetor, *Chronicle* (Greatrex, Phenix & Horn, Translated Texts for Historians 55, 2011) | Named in the census's own pre-existing source list as this world's own third primary source | Published 2011 — in copyright, not public domain. Closed for vendoring; the older 1899 Hamilton & Brooks translation of the same underlying compilation was vendored instead (see Doc_02 §2), with the 2011 edition's own authorship analysis used (citing it, not copying its text) to correctly attribute the compilation as composite/pseudonymous. |
| `sixthbookofselec0022seve` (archive.org item) | Appeared in the same archive.org search results as the two Severus Select Letters volumes actually vendored, same apparent title/volume | OCR quality is markedly worse (badly garbled title page and running text, per this session's own direct check) and its exact volume/part identity within the four-part set (2 volumes x 2 parts) was not cleanly resolved. Not vendored; the two cleaner-OCR volumes (`selectletterssix01seveuoft`, `sixthbookofselec0000ewbr`) were used instead. If a future session needs to disambiguate the full four-part set precisely, this item is where to start, not where to stop. |
| `discoursesphilo00budggoog` (archive.org item) | Same title as the Philoxenus Discourses volume actually vendored | Not independently distinguished from `discoursesofphil02philuoft` (the volume actually used, confirmed as Vol. II, the translation) this session — likely a duplicate or alternate scan, not separately verified. Not closed with certainty; flagged as unresolved-not-pursued rather than confidently ruled out. |

## 5. Open cross-world questions

- **The Chronicle of Edessa's own role** (`chronicle-of-edessa_cowper.txt`,
  already in this bucket before this session): inherited unresolved from
  `worlds/_cross-world/NEEDS-RULING.md` — whether a Chalcedonian
  composition-era (c. 540s) civic chronicle documenting this world's own
  ground "from the rival side of 451" belongs here at all, and at what
  role. Named, not decided, by this dossier.
- **The Chronicle of Joshua the Stylite's own role** (newly assigned this
  session, `context` at `provisional`): the chronicler's own confessional
  allegiance was not established either way this session (Doc_02 §2, §8).
  A genuinely open characterization question, not a sourcing gap. A new
  lead, Revision 2: the chronicler praises Flavian II of Antioch (line
  3895 of the vendored file) — the Chalcedonian patriarch Severus replaced
  in 512 — which may bear on this question; not yet pursued to a
  conclusion.
- **The Zachariah Rhetor compilation's own continuator material** (Books
  I-II, VII-XII, assembled c. 569 by a writer distinct from Zacharias
  Scholasticus): unassessed for own-voice/opponent-voice status. Books
  III-VI, Zacharias's own material, were corrected this revision to
  own-voice/Severus-sympathetic (see §1 above) — the continuator books
  remain a genuinely open task, not decided by this dossier.
- **Whether this world and a not-yet-built Egyptian miaphysite world
  should share any corpus-map entries** (e.g., a future vendored Cyril of
  Alexandria doctrinal text, since Severus's own Christology explicitly
  builds on Cyril's "mia physis" language) — not assessable until such a
  world's own bucket exists; named for whoever builds it next.
