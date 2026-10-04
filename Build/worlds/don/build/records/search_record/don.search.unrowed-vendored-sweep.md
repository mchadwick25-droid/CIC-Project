---
id: don.search.unrowed-vendored-sweep
world_id: donatism
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    This sweep contradicts two statements the Source Registry currently makes,
    and the divergence is the point of the record rather than an incidental
    note. (1) Row 39 states as a direct check that "Pars II (CSEL 52, Contra
    litteras Petiliani) is confirmed absent, checked directly -- found only as a
    cross-reference abbreviation, never as body text" in
    augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt. It is
    present, as running header "IIII. Contra litteras Petiliani" at 59+
    occurrences with continuous Latin body text and critical apparatus beneath
    them. Row 39's reasoning rested on that file's terminal errata section
    "explicitly correct[ing] both VOL. LI and VOL. LIII by name"; the errata in
    fact carries three volume headings, and the middle one reads "VOL. LIL" at
    line 101362 -- OCR damage for VOL. LII, sitting exactly where it belongs
    between LI and LIII with its own three corrections beneath it. A single
    mis-OCR'd final I produced the wrong conclusion. (2) Rows 16 and 51, and
    Doc_02 SS9 item 1a(v), carry as an open item that the agonistici
    self-designation's own source passage "remains unidentified." The term is in
    four vendored files, three of which the Registry already rows -- see note
    below. A plain search for "agonistic" matches "antagonistic" and buries the
    real hits, which is the likeliest reason earlier checks missed it. Neither
    divergence is corrected here; this is a review step, and both route to the
    build thread's own next Doc_02 revision pass.
sources: []
relations: []
query: "Every one of the 98 entries under cic/texts/ (the shared vendored-text
  library), triaged for relevance to Donatism and cross-checked against the
  56-row World-Builds/Donatism/Source_Registry.md and the 55 records/don/source/
  files, for any file -- or any work inside a file -- that is relevant to this
  world and has neither a Registry row nor a source record. Run as the B-1a half
  of this world's B-1a/B-1b coverage check, on the model of the Cappadocian and
  HAL unopened-volume sweeps."
channel: "Direct reading of cic/texts/ (full directory listing, 98 entries),
  cic/texts/REGISTRY.yaml (for which world each file was vendored FOR),
  cic/corpus-map/donatism.yaml (for what this world's own corpus map already
  carries), Source_Registry.md's 56 rows, and Doc_02_Source_Ecology.md SS9's own
  open-items list, 2026-09-10. Every surviving candidate was then opened and read
  into its own body text or structural apparatus -- running headers, title pages,
  errata sections, editorial rubrics, div1 headings -- rather than accepted or
  dismissed on a filename or a bare keyword count. Regex searches were run with
  markup stripped and with a (?<!nt) guard where a target string is a substring
  of a common English word. Live WebSearch was available this session and was
  used, but for the companion coverage check's PRESS answers only, not for this
  sweep: B-1a's question is what is already on disk."
result: found
found_sources: []
note: "FIVE FINDINGS. This sweep did NOT come back clean, unlike Cappadocian's,
  which found zero vendored-but-unrowed files.

  FINDING 1 -- SIX FURTHER AUGUSTINE ANTI-DONATIST WORKS SITTING UNROWED INSIDE
  AN ALREADY-CITED FILE. augustini_scripta-contra-donatistas-pars-i-iii_
  petschenig1908-1910.txt (Registry row 39; relied on by rows 17, 18, 37, 56)
  carries a continuous TWELVE-work numbered sequence in its own page running
  headers, not the three-plus-three row 39 describes. Rowed: I Psalmus contra
  partem Donati (row 37), II Contra epistulam Parmeniani (row 18), III De
  baptismo (row 3, via the NPNF English; the Latin is unrowed), VI Contra
  Cresconium (row 17), XII Contra Gaudentium (row 56). UNROWED, all six opened
  at their first running header and read into genuine Latin body text with
  critical apparatus: IIII Contra litteras Petiliani (59+ header occurrences;
  see divergence_note -- row 39 declares this work absent), V Epistula ad
  catholicos de secta Donatistarum (41), VII De unico baptismo contra Petilianum
  (15), VIII Breviculus collationis cum Donatistis (20 -- note a plain search for
  'breviculus' returns zero because the file's OCR renders it 'Breuiculus'),
  VIIII Contra partem Donati post gesta (34), X Sermo ad Caesariensis ecclesiae
  plebem (4), XI Gesta cum Emerito (11). Also present and unrowed: Contra
  (Adversus) Fulgentium Donatistam. The filename's own 'pars-i-iii' means Pars I
  THROUGH III (CSEL 51 + 52 + 53), not Pars I AND III.
  WHY IT MATTERS, not merely that it is true: row 12 (Petilian's letters) sits at
  Confidence C, licensed as this world's fullest surviving primary voice IN THE
  VENDORED CORPUS, noted as 'not independently checkable outside Augustine's own
  quotation' -- and the critical Latin edition of the work preserving that voice
  has been on disk, recorded as absent. Doc_02 SS3 states, from
  Monceaux Tome VI, that the Gesta cum Emerito is 'a different work from the 411
  Collatio, not itself vendored or checked this session'; it is vendored, and has
  been. This world's own corpus map already half-knows all this: donatism.yaml
  carries full entries for De unico baptismo contra Petilianum (role: tradition,
  confidence: assigned) and Contra Fulgentium Donatistam (role: tradition,
  confidence: provisional) against this same file, neither of which has a
  Registry row. The Registry and the corpus map have drifted apart on the
  contents of a file they both cite.

  FINDING 2 -- THE AGONISTICI OPEN ITEM IS CLOSED BY MATERIAL ALREADY ON DISK.
  The term sits in four vendored files, THREE OF WHICH THIS REGISTRY ALREADY
  ROWS. (a) optatus_against-the-donatists.txt, ROW 1's OWN FILE:
  Vassall-Phillips' note 115 on Optatus III.4, 'circumcelliones agonisticos' --
  the term is Optatus's own Latin, in the file row 1 already cites, with the
  translator's note cross-referencing Augustine's Contra Cresconium for the
  etymology. (b) optatus_libri-vii-critical_ziwsa1893.txt, ROW 38: Ziwsa's own
  index records 'agonisticos circumcelliones 81, 19' -- page and line, in the
  critical Latin text. (c) monceaux_histoire-litteraire-afrique-chretienne-
  tome4_1912.txt, ROW 52 (vendored, but read only to title page and
  chapter headings): Monceaux supplies the missing Augustine locus VERBATIM in
  his own footnote -- 'Augustin, Enarr. in Psalm. 132, 6: Milites Christi
  Agonistici appellantur. Utinam ergo milites Christi essent, et non milites
  Diaboli, a quibus plus timetur Deo laudes quam fremitus leonis' -- which names
  Deo laudes, ROW 27's own subject, in the same sentence; his body text at that
  point states the self-designation directly, 'Ils s'appelaient eux-memes les
  Agonistiques (Agonistici), ou les soldats du Christ (milites Christi).' (d)
  monumenta-vetera-donatistarum_migne-pl8.txt, ROWS 19/20/50: 'hic Agonisticos
  (quos vocabat) seu Circumcelliones... armavit.' Two UNROWED files corroborate
  independently: npnf106's editorial note ('By the Donatists called Agonistici,
  St. Augustin, In Ps. 133. 6') and Weiskotten's note in possidius_vita-augustini
  ('They called themselves Milites Christi Agonistici, see Optatus, De Schismate
  Donatistarum, PL ii, 1007').
  HONEST LIMIT ON THIS FINDING: the vendored NPNF English of the Enarrationes
  (npnf108) does NOT carry the term -- searched directly, zero occurrences of
  'Agonistici', 'Milites Christi', or 'soldiers of Christ'. It carries the
  SUBSTANCE of the surrounding passages (the Circumcellion clubs called
  'Israels'; 'Circumcelliones armed everywhere remain not quiet... for the blood
  of innocent men they thirst') but not the self-designation itself, which
  reaches this corpus only through the Latin and through Monceaux. The locus is
  now identified and citable at Confidence A from a vendored text; a verbatim
  English rendering of it is not yet on disk. Stated, not softened.

  FINDING 3 -- THE ANCIENT PROSOPOGRAPHY OF DONATISM'S OWN AUTHORS, VENDORED AND
  UNROWED. npnf203_theodoret-jerome-gennadius-rufinus.xml is rowed by the
  Cappadocian world, never by this one; the Registry contains no reference to
  Jerome or Gennadius at all. Read directly, four notices inside this world's
  boundary and on its open questions: (i) Jerome, De viris illustribus 93,
  'Donatus the heresiarch' -- contemporary notice that 'many of his works, which
  relate to his heresy, are extant, including On the Holy Spirit, a work which is
  Arian in doctrine', i.e. ancient testimony that Donatus himself was an author,
  bearing on Doc_02 SS6's scarcest-category problem. (ii) Jerome, DVI 110, on
  Optatus of Milevis -- he 'wrote in behalf of the Catholic party SIX BOOKS
  against the calumny of the Donatian party.' Row 1's Verification Note leaves
  the Books I-VII / second-edition question open and names only Ziwsa's apparatus
  (row 38, unread for that purpose) and Labrousse (row 44, unacquired) as
  instruments that would settle it; here is a third, ancient, already-vendored
  witness giving a six-book count. (iii) Gennadius, DVI 4, 'Vitellius the
  African' -- a named Donatist author with three titled works (Why the servants
  of God are hated by the world; Against the nations and against us as traditors
  of the Holy Scriptures in times of persecution; On ecclesiastical procedure).
  THE REGISTRY DOES NOT MENTION VITELLIUS ANYWHERE. (iv) Gennadius, DVI 5,
  'Macrobius' -- 'as I learned from the writings of Optatus, afterwards secretly
  bishop of the Donatians in Rome', the ancient source for the identification row
  20 currently takes at second hand from Migne's editorial note; Macrobius is the
  author of row 20's own Passio Isaac et Maximiani, and Gennadius credits him
  with a further work, To confessors and virgins. (v) Gennadius, DVI 18,
  'Tichonius the African' -- the principal ancient notice on Tyconius, naming On
  internal war and Expositions of various causes, recording EIGHT Rules against
  the seven in Burkitt's vendored edition (row 41), and confirming 'he also
  expounded the Apocalypse of John entire, regarding nothing in it in a carnal
  sense, but all in a spiritual sense' -- the ancient attestation of Tyconius'
  Apocalypse commentary, the one partial in this check's own Step 2 recall score.

  FINDING 4 -- THREE FURTHER VENDORED FILES WITH REAL DONATIST CONTENT, NONE
  ROWED. (a) possidius_vita-augustini_weiskotten1919.txt, vendored for
  the Latin Pastoral-Congregational world: a genuinely bilingual critical edition
  with a COMPLETE English translation, so usable as ordinary English primary
  evidence, not merely a Latin second-witness. Direct counts: Donatist(s) plus
  Latin case forms 41+, Crispinus 26 (row 47's own addressee), Emeritus 12,
  Circumcellion(es) 11. Augustine's own companion and biographer, present for much
  of what this world reconstructs. (b) npnf108_augustine-exposition-psalms.xml
  (34 Donatist, 7 Circumcellion) and npnf106_augustine-sermon-mount-harmony-
  gospels-homilies.xml (30, 4): Augustine's PASTORAL anti-Donatist register, as
  against the polemical treatises the Registry rows exclusively -- where the vivid
  contemporary texture lives, and the register Shaw's Sacred Violence (row 24)
  leans on most heavily. Named as a category, not a single source; the right unit
  is a build-thread decision, not this record's. (c) augustine_epistulae-critical_
  goldbacher-csel57-pars4.txt, same sibling-world intake: CSEL 57 =
  Epistulae CLXXXV-CCLXX, i.e. the critical Latin edition of LETTER 185, DE
  CORRECTIONE DONATISTARUM ITSELF -- which is row 5, at Confidence B with no
  critical edition named at all. The pattern rows 38, 39 and 51 already establish
  for this world (row the translation, then row the critical edition beside it)
  has an obvious next instance sitting unrowed. cyprian_opera-omnia-critical_
  hartel-csel3-pars1-2.txt, same intake, stands in the same relation to rows 7-10.

  FINDING 5 -- ONE LIVE CORPUS-MAP RULING THE REGISTRY HAS NOT ANSWERED.
  codex-theodosianus_latinlibrary.txt is a SECOND, independent full text of the
  Theodosian Code, distinct from row 51's Mommsen & Meyer. Donatism's own corpus
  map carries it at confidence: needs-ruling, with a note stating outright that
  whether it belongs in this world's bucket 'is a call for that world's own build
  thread, not asserted here from outside.' The Registry has zero mention of it.
  Correctly NOT a coverage gap -- row 51 holds the better edition -- but a live,
  unanswered ruling the corpus map is explicitly waiting on. Named, not resolved.

  NEAR-MISSES CHECKED AND CLEARED, not waved through on a keyword count.
  npnf214_seven-ecumenical-councils.xml (already rowed at 11 for Carthage 256):
  checked for the Council of Arles 314's own CANONS -- canon 8 on not
  rebaptizing, canon 13 on traditores -- which would be a genuine addition beyond
  row 2's Arles LETTER; 21 'Arles' hits, none resolving to the 314 canons on
  inspection. Cleared. salvian_on-the-government-of-god_sanford1930.txt: Salvian
  on Roman Africa at the Vandal conquest, adjacent to this world's 439 terminus;
  one Donatist hit, editorial; not this world's evidentiary voice. Cleared.
  npnf202 (3 hits), npnf105 (17, Pelagian-context), npnf103 (3), npnf107 (6): all
  incidental or editorial. Cleared.

  HOMONYM TRAPS -- REAL ONES, FOUND BY READING RATHER THAN ASSUMING. The Registry
  already flags two internally and deserves the credit: the two Optatuses (of
  Milevis vs. Gildonianus of Thamugadi, row 4) and the two Maximians (the
  Maximianist-schism deacon vs. row 20's martyr, rows 17/18/20). THREE FURTHER
  TRAPS surfaced here, each the exact shape the Cappadocian precedent warned
  about -- a volume belonging to another world's own domain, reachable by
  keyword. (1) HONORATUS: row 50's Passio Donati turns on Honoratus, bishop of
  Sicilibba; a keyword sweep for that name across cic/texts/ returns 30 files,
  the densest being hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt --
  Honoratus of Arles, the Gallic Monastic world's own founder-subject, no
  connection whatever to North Africa. Precisely Cappadocian's shared-volume trap
  with a different name doing the tripping. (2) GAUDENTIUS: Gaudentius of
  Thamugadi (row 56) against Gaudentius of Brescia, live across npnf203, npnf206,
  npnf204 and npnf214 in Rufinus/Jerome contexts. (3) FULGENTIUS: Fulgentius the
  Donatist (Contra Fulgentium in the Petschenig file; Monceaux Tome VI ch. VI)
  against Fulgentius of Ruspe -- a same-province, same-church, different-century,
  different-party homonym, HARDER to catch than a cross-regional one because every
  contextual signal except the date agrees. And one trap this world is
  structurally exposed to that has not yet caused a problem, named pre-emptively:
  DONATUS -- Donatus the Great, Donatus of Casae Nigrae, Donatus of Bagai, the
  Donatus of row 50's manuscript title (which Monceaux argues is a corruption
  naming the bishop of Advocata), and Aelius Donatus the grammarian, Jerome's own
  teacher and therefore live in npnf206, the Hieronymian world's volume. Row 50
  already handles the third-to-last carefully; the last is not currently a live
  risk only because nothing has run a keyword sweep on the bare name yet.

  SATURATION -- WHAT THIS SWEEP CAN AND CANNOT CLAIM. It is complete over the
  question it asked: all 98 entries under cic/texts/ triaged, every surviving
  candidate opened and read into body text or structural apparatus, nothing
  accepted or dismissed on a filename or bare keyword count, and both findings
  that contradict Registry statements verified twice against primary file content
  with the MECHANISM of the original error named, not just the error. It could
  NOT check: (a) DEPTH inside the vendored files -- Finding 1 proves six works are
  present and are real body text, not what they say; nobody in this build has read
  the Breviculus, the Gesta cum Emerito, or Contra litteras Petiliani's Latin, and
  this pass did not either, reading enough of each to establish presence and
  identity and stopping there per the Registry's own Confidence A calibration
  rule; the same limit applies to the npnf203 notices, read in full as notices but
  with Jerome's and Gennadius's own reliability unassessed. (b) THE PL 11
  VOLUME'S UNRECONCILED CONTENTS -- row 55 names three still-unread items in
  pl11-zeno-optatus-collatio-carthaginiensis_migne.txt (a Historia Donatistarum
  at col. 771, a second Optatus edition at col. 883, and a Monumenta vetera
  section at col. 1170 with a title identical to the already-vendored PL 8 file);
  that reconciliation is a substantial reading task, still open, not attempted
  here. (c) THE WIDER LITERATURE -- this sweep asks what is on disk and cannot ask
  what the field contains; the companion coverage check's Step 3 answers that
  separately and only three items deep, grounded by live web search, and no
  systematic field-bibliography sweep against standard reference instruments was
  run, which remains open exactly as the Registry's own saturation statement
  already says.
  CONFIDENCE, PLAINLY: HIGH for 'nothing further is sitting unrowed in
  cic/texts/' -- a bounded, exhaustively enumerable question, exhaustively
  enumerated. MODERATE for 'the Registry's existing rows accurately describe what
  is in the files they cite' -- two demonstrably did not, and both errors were of
  the same kind: a conclusion drawn from partial reading of an OCR-damaged
  apparatus, then recorded in the Registry as a direct check. That second figure
  is the one worth carrying forward. This world's failure mode is not missing
  sources; it is over-confident description of the sources it already has.

  METHODOLOGICAL NOTE FOR THIS WORLD SPECIFICALLY. This is the FIRST
  Build/worlds/don/build/records/search_record/ this world has ever had. The Source Registry's own
  Discovery methodology note states that no search record was kept during the
  build, that the Discovery column was reconstructed rather than logged
  contemporaneously, and that 'a future pass that wants that discipline for this
  world would need to open Build/worlds/don/build/records/search_record/ going forward, not back-fill
  one for what has already happened.' This record opens it going forward and
  back-fills nothing.

  DISPOSITION. Nothing above is corrected here -- this is a review step, not a
  revision cycle. Findings 1, 2, 3 and 5 route to the build thread's own next
  Doc_02 revision pass (none needs acquisition; all five concern material already
  on disk). Finding 4's three files likewise. The companion write-up at
  World-Builds/Donatism/donatism_B1a_B1b_Coverage_Check.md carries the full
  account including the Step 1-3 recall and PRESS results, whose two acquisition
  targets -- the Vienna corpus of anonymous Donatist sermons (OeNB Ms. Lat. 4147;
  Leroy 1994/1999) and Jesse A. Hoover, The Donatist Church in an Apocalyptic Age
  (Oxford Early Christian Studies, 2018) -- route instead to the pre-freeze
  re-sweep, since both do require acquisition."
---

# Search record — unrowed vendored-library sweep (B-1a)

The B-1a half of this world's B-1a/B-1b coverage check: a triage of all 98
entries under `cic/texts/` against the 56-row Source Registry and the 55
`records/don/source/` files, asking only what is already on disk, relevant to
Donatism, and neither rowed nor recorded.

Five findings, two of which contradict specific statements the Registry
currently makes and one of which closes a long-standing open item. Full detail in the `note` field above; the companion
write-up is `World-Builds/Donatism/donatism_B1a_B1b_Coverage_Check.md`.

No Registry row and no source record is edited by this record.
