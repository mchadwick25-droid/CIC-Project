#!/usr/bin/env python3
"""The vendored-text registry - what's sitting in cic/texts/, verified, not asserted.

WHY. Vendoring CCEL's public-domain volumes solved a real, total blocker this
session hit repeatedly: every patristic text host (ccel.org, newadvent.org,
wikisource, archive.org, gutenberg.org, tertullian.org) is blocked by this
sandbox's egress policy, so without a local copy no quote could be verified
at all - Check B's whole grounding claim (`verified-direct`) had nothing to
stand on. Vendoring fixed that. But by the time this registry was built,
10 volumes (38MB) were already sitting in cic/texts/ with only 3 ever linked
to a record that cites them - a real, measured fact (found 2026-08-15 by
hand-grepping, the trigger for building this) with no earlier structure that
would have surfaced it on its own. That is the SAME shape of problem
mechanism_dependencies.py (T3-A) and gate_mechanism_coverage (T3-B) exist to
catch at the record layer - a resource sitting present with no declared
need - just one layer up, at the reference-text layer instead.

WHAT THIS VERIFIES, NOT ASSERTS. Two facts about a vendored file are
worth checking every run rather than trusting a claim written when the file
arrived: (1) does its OWN header actually state a public-domain rights
basis - checked by reading the file, not by re-trusting whatever note
accompanied it when vendored, and (2) which records actually cite it -
computed by scanning cic/records/ for the literal file path, not read off a
static "covers" field that could drift out of date the moment a new quote
record is authored. A registry that just repeated hand-typed claims would
be exactly the kind of self-certified report this build's own review
discipline (CO-020/CO-022) already distrusts.

ENTRIES below carries only what CANNOT be recovered by reading the file or
scanning the records: when it arrived, who supplied it, and free-form notes
(the editorial content that used to live only in the hand-maintained
README - e.g. "this volume's own Julius is Africanus, not Rome" - preserved
here so it survives being folded into a generated document instead of a
hand-edited one).

Usage:
  python cic/engine/texts_registry.py                 # report
  python cic/engine/texts_registry.py --write-readme   # regenerate cic/texts/README.md
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
REPO_ROOT = ROOT.parent  # PORT NOTE (2026-08-21, world/alexandria handoff): this script
# originated on claude/table-voice-reset-nufsm4, where records lived at cic/records/ -
# this redesign moved the records tree to <repo_root>/records/ (Artifact-1), one level
# above cic/, while cic/texts/ itself did not move. RECORDS_DIR below is the one line
# that changed for the port; citing_records()'s logic (grep every *.md under RECORDS_DIR
# for the literal "cic/texts/<filename>" path string) needed no change at all - it was
# already schema-agnostic, a dumb full-text scan, not a YAML-aware records reader.
TEXTS_DIR = ROOT / "texts"
RECORDS_DIR = REPO_ROOT / "records"

# Two conventions seen across what's actually been vendored, both CCEL's
# own: the plain-text export's "Rights: Public Domain" line, and ThML XML's
# own <DC.Rights>Public Domain</DC.Rights> Dublin-Core element - found only
# by reading the real anf01 XML header, not assumed from the .txt
# convention. Order matters (first alternative wins the same group number
# either way, since only one can match a given header).
_RIGHTS_LINE = re.compile(r"Rights:\s*(.+)|<DC\.Rights>\s*([^<]+)")
_TITLE_LINE = re.compile(r"Title:\s*(.+)|<DC\.Title>\s*([^<]+)")


@dataclass(frozen=True)
class TextEntry:
    filename: str
    supplied_by: str
    date_added: str
    notes: str = ""


# What CANNOT be read off the file itself or computed from the records.
ENTRIES: tuple[TextEntry, ...] = (
    TextEntry("anf01_apostolic-fathers-justin-irenaeus.xml", "Mark", "2026-08-15",
              "CCEL's native ThML source, SWAPPED IN 2026-08-15 for the plain-text rendering that "
              "originally carried this id - same volume, same rights basis, verified byte-identical "
              "on all four passages already committed as quote records (pahcq001-004) before the "
              "swap. Structurally better for this build's own purposes: shorter/longer/Syriac "
              "recensions are addressable by id (e.g. v.v.iv-p1 vs v.v.iv-p4 for Romans 4), and "
              "footnotes are their own <note> elements rather than interleaved apparatus text - both "
              "real friction points hand-transcribing the plain text had already hit. Extracting text "
              "correctly requires walking element trees properly, not naive regex: a lazy `<p>...</p>` "
              "match truncates early against nested <note><p class=\"endnote\">...</p></note> "
              "structures, and a node's own skip-tag status must not be applied to its `tail` text - "
              "both mistakes were made and caught live during this swap, on the Smyrnaeans and "
              "Martyrdom-of-Polycarp passages respectively, before anything was recommitted."),
    TextEntry("anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml", "Mark", "2026-08-15",
              "Shepherd of Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria. Swapped from "
              "the plain-text rendering the same day, as anf01 was - no record cited the old .txt file "
              "(this volume's own zero-citation status, unchanged), so this swap needed no "
              "re-verification of any existing quote."),
    TextEntry("anf03_tertullian.xml", "Mark", "2026-08-15",
              "Carries Tertullian's Apologeticus, the primary text srcPAHCP15 already cites in pahc "
              "('Tertullian, Apology 39'). No quote record was in this session's worklist, so none "
              "was written, but the translation edition is available if one is ever wanted. Swapped "
              "from the plain-text rendering the same day, as anf01/anf02 were - zero citations before "
              "the swap, so nothing needed re-verification."),
    TextEntry("anf04_tertullian4-minucius-felix-commodian-origen1-2.xml", "Mark", "2026-08-15",
              "Tertullian Pt. 4, Minucius Felix, Commodian, Origen Pts. 1-2. Swapped from the plain-text "
              "rendering the same day, as anf01/02/03/05/06/07/08/09 were - zero citations before the "
              "swap, so nothing needed re-verification."),
    TextEntry("anf10_bibliographic-synopsis-general-index.xml", "Mark", "2026-08-15",
              "NEW, not a swap - this volume was never vendored as plain text. A finding aid, not "
              "primary source content: Biographical Synopsis, Index of Subjects, Index of Texts, and "
              "the General Index to the whole Ante-Nicene Fathers set - 66KB against the 3-4.5MB of "
              "every content volume, 11 top-level divs with no chapter/letter text of its own. Its "
              "'cited by' count will legitimately stay at zero permanently, unlike every other volume "
              "here where zero means only 'not yet drawn on' - this one carries nothing a quote record "
              "could ever cite as translation_used. Kept for its actual use: faster location of "
              "passages across the other nine volumes when authoring future quotes."),
    TextEntry("anf05_hippolytus-cyprian-caius-novatian.xml", "Mark", "2026-08-15",
              "Hippolytus, Cyprian, Caius, Novatian. Carries ~82 of Cyprian's own letters plus On the "
              "Lapsed, On the Mortality, and Pontius's Life of Cyprian - primary-source material for "
              "the not-yet-built Latin Pastoral-Congregational Christianity world (census: "
              "'Selected - Not Yet Built'). Swapped from the plain-text rendering the same day, as "
              "anf01/02/03 were - zero citations before the swap, so nothing needed re-verification. "
              "Structured letter/chapter ids here would matter directly once that world is built: "
              "Cyprian's ~82 letters are individually addressable rather than needing to be located "
              "by reading forward through flowing prose."),
    TextEntry("anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml", "Mark",
              "2026-08-15",
              "This volume's own 'Julius' is Julius Africanus the chronographer, a named author here - "
              "NOT Julius I of Rome (srcIJC04/srcIJC42). Swapped from the plain-text rendering the same "
              "day, as anf01/02/03/05 were - zero citations before the swap, so nothing needed "
              "re-verification."),
    TextEntry("anf07_lactantius-apostolic-constitutions-didache-liturgies.xml", "Mark", "2026-08-15",
              "Carries the Didache, published too late for ANF vol. 1 - closed the deferred gap "
              "srcPAHCS62 named. Translator for the Didache specifically: Isaac H. Hall and John T. "
              "Napier (Sunday-School Times, 1884), not the volume's general editors. Swapped from the "
              "plain-text rendering the same day, as anf01/02/03/05/06 were - unlike those, this one "
              "had an existing quote (pahcq005) and source (srcPAHCS63) citing it, so both were "
              "re-verified against the XML with the tail-aware element walker before the swap, not "
              "just before it was trusted: the committed wording matched exactly."),
    TextEntry("anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml", "Mark", "2026-08-15",
              "Carries Abgar/Edessa correspondence material, relevant to syriac world (syrfig005, "
              "Addai) - not drawn on so far; that figure's own record already treats him as legend, "
              "not history. Swapped from the plain-text rendering the same day, as anf01/02/03/05/06/07 "
              "were - zero citations before the swap, so nothing needed re-verification."),
    TextEntry("anf09_gospel-of-peter-diatessaron-origen-commentaries.xml", "Mark", "2026-08-15",
              "Origen's Commentaries on John and Matthew, among others. Swapped from the plain-text "
              "rendering the same day, as anf01/02/03/05/06/07/08 were - zero citations before the "
              "swap, so nothing needed re-verification."),
    TextEntry("npnf104_augustine-anti-manichaean-anti-donatist.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 4: Augustine - The Writings Against the Manichaeans (and Against the "
              "Donatists). Arrived first labeled 'npnf204' by mistake - its own <DC.Title> read directly "
              "from the file caught the mismatch before anything was touched (it is Series I vol. 4, "
              "NPNF1-04, not Series II vol. 4 / Athanasius). No quote record cites it and none is "
              "planned yet, but it is real, useful primary-source material in its own right: Augustine's "
              "own anti-Donatist writings are, per the census's own note on the not-yet-built Donatism "
              "world, the primary route by which Donatist voices (Donatus, Petilian, Tyconius) survive "
              "at all - 'known only through Augustine's quotations.' A future Donatism world would need "
              "this volume's own doubly-mediated quoting discipline, the same shape already proven for "
              "Julius's letter (license only the quoted portion, leave the surrounding corpus Excluded)."),
    TextEntry("npnf204_athanasius-select-works-letters.xml", "Mark", "2026-08-15",
              "The volume srcIJC42 was scoped for from the start. Closed the last inert Check B cell "
              "in the fleet (ijcq001, Julius I's letter of 341). Swapped from the plain-text rendering "
              "the same day as the ANF set - ijcq001's committed wording re-verified against the XML "
              "with the tail-aware element walker before the swap; the letter itself is cleanly its own "
              "titled sub-division here ('Letter of Julius to the Eusebians at Antioch'), an even "
              "cleaner boundary than the paragraph-number locus the plain text required."),
    TextEntry("npnf210_ambrose-select-works-letters.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 10: Ambrose: Select Works and Letters. Supplied for ijcq002 - "
              "deepening imperial_juridical past its single Julius quote. Closed reading this volume "
              "found a real misattribution risk before it was committed: a strong, verbatim line on "
              "'the Church belongs to God' looked like the obvious candidate for the basilica-standoff "
              "quote, found by a raw text search, but tracing its actual element ancestry showed it "
              "belongs to a different work entirely - Concerning Repentance, Book II - not the Sermon "
              "Against Auxentius. Discarded before use; ijcq002 cites only text confirmed, by walking "
              "the tree, to sit inside the correct sermon."),
    TextEntry("npnf201_eusebius-church-history-life-of-constantine.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 1: Eusebius Pamphilius: Church History, Life of Constantine, "
              "Oration in Praise of Constantine. Supplied with no accompanying text, read as continuing "
              "'deepen imperial_juridical' (Julius, then Ambrose, now Eusebius) - ijcq003. Found a real "
              "scoping mismatch, not a misattribution: the world's only prior Eusebius source row "
              "(srcIJC02) cites 'esp. 4.24' and licenses a different claim ('bishop of those outside') "
              "than the vision-under-oath account ijcstory001 actually attests. Rather than stretch "
              "srcIJC02 to cover it, the chapter was located independently by title search (Book I, "
              "ch. 28) and two new, narrowly-scoped rows written (srcIJC44 primary, srcIJC45 "
              "translation); srcIJC02 itself was left untouched. Also notable: this volume's two works "
              "have different translators (McGiffert for Church History, a Bagster translation revised "
              "by Richardson for Life of Constantine) under one shared <DC.Creator> block - checked "
              "per-chapter rather than assumed from the volume-level header, the same discipline that "
              "caught srcIJC42's Newman/Robertson split."),
    TextEntry("npnf202_socrates-sozomen-ecclesiastical-histories.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 2: Socrates and Sozomenus Ecclesiastical Histories. Supplied with "
              "no accompanying text. Socrates Scholasticus and Sozomen were both named earlier this "
              "session as figures in Mark's wider CCEL listing not yet connected to any of the six "
              "built worlds' figure registries - this volume is their primary text, vendored for "
              "future use rather than an immediate quote request. No quote or source record cites it "
              "yet."),
    TextEntry("npnf203_theodoret-jerome-gennadius-rufinus.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 3: Theodoret, Jerome, Gennadius, & Rufinus: Historical Writings. "
              "Supplied with no accompanying text, continuing the NPNF2 church-historian run "
              "(npnf201 Eusebius, npnf202 Socrates/Sozomen). Theodoret and Rufinus were both named "
              "earlier this session as figures in Mark's wider CCEL listing not yet connected to any "
              "of the six built worlds' figure registries. Vendored for future reference; no quote or "
              "source record cites it yet."),
    TextEntry("npnf206_jerome-principal-works.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 6: Jerome: The Principal Works of St. Jerome (Letters, Against "
              "Jovinianus, Against the Pelagians, and more). Supplied with no accompanying text. "
              "Distinct from npnf203, which carries Jerome's much shorter Lives of Illustrious Men - "
              "this is his own major corpus. Vendored for future reference; no quote or source record "
              "cites it yet."),
    TextEntry("npnf207_cyril-jerusalem-gregory-nazianzen.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 7: Cyril of Jerusalem, Gregory Nazianzen. Supplied with no "
              "accompanying text. Gregory Nazianzen is one of the three Cappadocian Fathers named in "
              "the census's 'Cappadocian Nicene Pastoral-Monastic Tradition' world (Selected, Not Yet "
              "Built) - primary text for that world's own figures, not yet built. Vendored for future "
              "reference; no quote or source record cites it yet."),
    TextEntry("npnf208_basil-letters-select-works.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 8: Basil: Letters and Select Works. Supplied with no accompanying "
              "text alongside npnf207. Basil of Caesarea is a second of the three Cappadocian Fathers "
              "named in the same not-yet-built world - between this volume and npnf207, two of the "
              "three Cappadocians now have primary text vendored (Gregory of Nyssa, NPNF2-05, does "
              "not yet). Vendored for future reference; no quote or source record cites it yet."),
    TextEntry("npnf211_sulpitius-severus-vincent-lerins-cassian.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 11: Sulpitius Severus, Vincent of Lerins, John Cassian. Supplied "
              "with no accompanying text. John Cassian (Institutes, Conferences) is desert's own "
              "srcDES026 - a Latin primary-source row never independently re-collated, cited "
              "load-bearingly by four of that world's build documents (Doc_01, Doc_03, Doc_08, "
              "Doc_09c) per its own verification_note. This volume supplies the standard English "
              "translation of exactly that corpus - the first vendored file this session that maps "
              "directly onto an EXISTING world's already-cited source row rather than adding a fresh "
              "one. FOLLOW-UP (2026-08-15, same day): srcDES027 now cites this volume as srcDES026's "
              "translation row (translator: Rev. Edgar C. S. Gibson, confirmed from the volume's own "
              "Cassian-specific title page, distinct from the shared volume-level header). Honestly "
              "marked NOT wording-verified in srcDES027 - srcDES026 is a corpus-level citation with no "
              "single locus pinned down yet, so there is nothing to check this translation's wording "
              "against. No quote drawn from it."),
    TextEntry("npnf213_gregory-great-ephraim-syrus-aphrahat.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 13: Gregory the Great (II), Ephraim Syrus, Aphrahat. A second file "
              "that maps directly onto an EXISTING world's already-cited primary sources: Ephraim "
              "Syrus (syriac's syrfig002) and Aphrahat (srcSYR010/srcSYR013, Demonstrations 1-23) are "
              "both major syriac figures. Notable: srcSYR010's currently-cited English translations "
              "(Lehto, Gorgias Press 2010; Valavanolickal, Gorgias Press 2005) are BOTH modern and "
              "in-copyright - Gwynn's translation in this volume (1898) is public domain, the same "
              "shape as pahc's earlier Holmes-to-ANF swap this session, given the 'free tools, no "
              "budget' constraint. FOLLOW-UP (2026-08-15, same day): srcSYR065 now cites this volume "
              "(div1 iii) as a public-domain translation alternative, display_permitted true - added "
              "alongside srcSYR010, not replacing it. Honestly marked NOT wording-verified (no desert "
              "or syriac quote currently cites Ephraim or Aphrahat text at all); a specific passage "
              "still needs to be found before any quote can cite it."),
    TextEntry("npnf205_gregory-nyssa-dogmatic-treatises.txt", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 5: Gregory of Nyssa: Dogmatic Treatises, Etc. Supplied as plain "
              "text, not ThML - Mark reported the ThML export 'not working' for this volume. The "
              "registry has handled both formats since its first vendored files (before the anf01-10/"
              "npnf104/204 ThML swap); no special-casing was needed. The third of the three Cappadocian "
              "Fathers (after npnf207 Gregory Nazianzen and npnf208 Basil) now has primary text "
              "vendored for the not-yet-built 'Cappadocian Nicene Pastoral-Monastic Tradition' world."),
    TextEntry("npnf212_leo-great-gregory-great.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 12: Leo the Great, Gregory the Great. A third file this session "
              "that maps directly onto an EXISTING built world's already-cited primary source: Leo I "
              "is imperial_juridical's ijcfig007, and this volume carries the standard English "
              "translation of his letters and sermons - including the Tome to Flavian (srcIJC12, "
              "Epistula 28, source_type P, no translation row cited yet) and the Canon 28 rejection "
              "letters (srcIJC13). Same shape as npnf211/Cassian/desert and npnf213/Aphrahat-Ephraim/"
              "syriac. FOLLOW-UP (2026-08-15, same day): srcIJC12's Tome to Flavian was covered "
              "separately via srcIJC46, scoped to its text as preserved in npnf214's Acts of "
              "Chalcedon (see ijcq004). srcIJC13's Canon 28 correspondence got srcIJC47, a translation "
              "row citing this volume (translator: Charles Lett Feltoe, confirmed from the volume's "
              "own preface signature) - but srcIJC47 is honestly marked NOT wording-verified, since no "
              "specific letter among the many to Marcian/Pulcheria/Anatolius has been individually "
              "pinned down and checked. That remains future work before any quote can cite it."),
    TextEntry("npnf214_seven-ecumenical-councils.xml", "Mark", "2026-08-15",
              "NPNF Series II, Vol. 14: The Seven Ecumenical Councils (Percival ed./trans.). Completes "
              "the full NPNF2 set (01-14). The most direct hit yet: THREE of imperial_juridical's own "
              "load-bearing primary sources are Acts and Canons rows with no English translation cited "
              "- srcIJC09 (Council of Nicaea, 325, 'initiating event'), srcIJC10 (Constantinople I, "
              "381, Canon 3, 'Strand B founding evidence'), and srcIJC11 (Chalcedon, 451, Canon 28, "
              "'the world's own closing event'). This volume is the standard English translation of "
              "all three. Not acted on here - no translation row or quote drawn from it yet, but this "
              "is the strongest candidate in the vendored set so far for deepening imperial_juridical "
              "further, given how central all three councils are to the world's own gravity/figure/"
              "contested-claim structure (per a broad grep, not just the source rows)."),
    TextEntry("npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 3: St. Augustine: On the Holy Trinity, Doctrinal Treatises, Moral "
              "Treatises. Part of a five-file Augustine batch supplied together ('here are the "
              "augustine sources'), continuing npnf104 (Anti-Manichaean/Anti-Donatist, vendored "
              "earlier this session). Vendored for future reference; no quote or source record cites "
              "it yet."),
    TextEntry("npnf105_augustine-anti-pelagian-writings.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 5: St. Augustine: Anti-Pelagian Writings. Part of the same batch. "
              "Vendored for future reference; no quote or source record cites it yet."),
    TextEntry("npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 6: St. Augustine: Sermon on the Mount; Harmony of the Gospels; "
              "Homilies on the Gospels. Part of the same batch. Vendored for future reference; no "
              "quote or source record cites it yet."),
    TextEntry("npnf107_augustine-homilies-john-soliloquies.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 7: St. Augustine: Homilies on the Gospel of John; Homilies on the "
              "First Epistle of John; Soliloquies. Part of the same batch. Vendored for future "
              "reference; no quote or source record cites it yet."),
    TextEntry("npnf108_augustine-exposition-psalms.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 8: St. Augustine: Exposition on the Book of Psalms. Part of the "
              "same batch. Two existing load-bearing citations are close but not fully covered by this "
              "batch: hieronymian's srcHAL009 (the Jerome-Augustine correspondence, Jerome's Ep. 112 = "
              "Augustine's Ep. 75) needs Augustine's Letters, and imperial_juridical's srcIJC08 "
              "(Augustine, Confessions 9.7) needs the Confessions - both live in NPNF1-01, which none "
              "of these five volumes is; NOT among the files supplied this round. Vendored for future "
              "reference; no quote or source record cites any of the five yet."),
    TextEntry("npnf101_augustine-confessions-letters.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 1: The Confessions and Letters of St. Augustine. Supplied with no "
              "accompanying text, closing the gap flagged in the npnf108 ENTRIES note. TRANSLATOR "
              "checked per-work at the volume's own section headers, not assumed: J.G. Pilkington for "
              "the Confessions, Rev. J.G. Cunningham for the Letters - two distinct translators, the "
              "same per-work check that caught srcIJC42's and srcIJC45's translator splits. Confirmed "
              "content for BOTH flagged citations: imperial_juridical's srcIJC08 (Confessions 9.7, "
              "Ambrose's antiphonal singing) is in the Confessions section; hieronymian's srcHAL009 "
              "(Jerome's Ep. 112 = Augustine's Ep. 75) is present as Letter LXXV, div3 id="
              "\"vii.1.LXXV\", titled \"From Jerome\" in Augustine's own numbering - confirming "
              "srcHAL009's own cross-reference note. FOLLOW-UP (2026-08-15, same day): srcIJC08 "
              "closed via srcIJC48 and ijcq008 ('add a quote from Confessions 9.7') - a new figure, "
              "ijcfig010 (Augustine, narratable: false, voice-only), was created since none existed. "
              "FINAL UPDATE, same day: hieronymian's srcHAL009 closed too, via srcHAL027 and halq002 "
              "('add a quote from Letter LXXV to close srcHAL009') - the Oea 'ivy/gourd' incident, "
              "Jerome's own defense of his Hebrew-based translation. Attributed to the world's "
              "existing Jerome figure (halfig001); this world's first verbatim quote (the only prior "
              "quote, halq001, is paraphrase-only)."),
    TextEntry("npnf102_augustine-city-of-god-christian-doctrine.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 2: St. Augustine's City of God and Christian Doctrine. Supplied "
              "with no accompanying text. Completes the full 8-volume NPNF1 Augustine set (01-08, all "
              "now vendored). No built world currently cites City of God or De Doctrina Christiana "
              "directly (a title-text search turned up only unrelated modern secondary sources whose "
              "titles happen to share the phrase 'Christian Doctrine' - srcIJC33, srcPAHCS25 - not "
              "Augustine's work). Vendored for future reference, most plausibly for the "
              "not-yet-built Latin Pastoral-Congregational and Donatism worlds flagged earlier this "
              "session; no quote or source record cites it yet."),
    TextEntry("npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 9: St. Chrysostom: On the Priesthood; Ascetic Treatises; Select "
              "Homilies and Letters; Homilies on the Statutes. Begins the NPNF1 Chrysostom set "
              "(vols. 9-14, the other half of NPNF1 alongside the now-complete 8-volume Augustine "
              "set). CHECKED, not assumed: John Chrysostom has zero citations across all six built "
              "worlds' source and figure records - confirmed by grep, matching the earlier finding "
              "this session that he, like the Cappadocians, has no organic tie to any of the six "
              "worlds' own time_windows. Vendored purely for future world-building; no quote or "
              "source record cites it."),
    TextEntry("npnf110_chrysostom-homilies-matthew.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 10: St. Chrysostom: Homilies on the Gospel of Saint Matthew. Same "
              "status as npnf109 - no built world cites Chrysostom. Vendored for future reference."),
    TextEntry("npnf111_chrysostom-homilies-acts-romans.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 11: St. Chrysostom: Homilies on the Acts of the Apostles and the "
              "Epistle to the Romans. Same status as npnf109 - no built world cites Chrysostom. "
              "Vendored for future reference."),
    TextEntry("npnf112_chrysostom-homilies-corinthians.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 12: St. Chrysostom: Homilies on the Epistles of Paul to the "
              "Corinthians. Same status as npnf109 - no built world cites Chrysostom. Vendored for "
              "future reference. Four of six NPNF1 Chrysostom volumes now vendored (09-12); vols. "
              "13 and 14 not yet supplied (their contents corrected below, at npnf114 - the original "
              "guess here for vol. 14's title was wrong, caught when the actual file arrived)."),
    TextEntry("npnf113_chrysostom-homilies-galatians-philemon.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 13: St. Chrysostom: Homilies on Galatians, Ephesians, Philippians, "
              "Colossians, Thessalonians, Timothy, Titus, and Philemon. Re-checked: still zero "
              "citations across all six built worlds' source and figure records. Vendored for future "
              "reference."),
    TextEntry("npnf114_chrysostom-homilies-john-hebrews.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 14: St. Chrysostom: Homilies on the Gospel of St. John and the "
              "Epistle to the Hebrews. Completes the full NPNF1 set (01-14) - the 8-volume Augustine "
              "set and the 6-volume Chrysostom set are both now entirely vendored. CORRECTION: the "
              "npnf112 ENTRIES note above guessed this volume's contents as 'Hebrews; Gregory "
              "Thaumaturgus; Apollinaris' - wrong on both counts (that description belongs to a "
              "different collection entirely, not this one); the volume's own title, read directly "
              "rather than assumed from memory, is the actual record here. Still zero citations "
              "across all six built worlds. Vendored for future reference."),
    TextEntry("palladius_lausiac-history_clarke1918.txt", "Mark", "2026-08-15",
              "Palladius of Galatia, The Lausiac History, trans. W.K. Lowther Clarke (SPCK, "
              "'Translations of Christian Literature' series, 1918), from Roger Pearse's 'morefathers' "
              "CCEL collection - identified as the essential item closing desert's srcDES007 (a "
              "primary-source row, Greek original, no translation cited, cited load-bearingly across "
              "desert's search_record/story/ambient/force). Supplied first as pasted chat text (too "
              "long to safely retype through model output; withdrawn), then as an actual RTF file "
              "attachment, converted mechanically to plain text via the striprtf library - no content "
              "passed through model-generated output at any point, avoiding both the practical "
              "output-length problem and any reproduction concern. Structural integrity confirmed "
              "(142 CHAPTER markers = 71 in the table of contents + 71 in the body). Public domain: "
              "Clarke's translation was published 1918, long out of US copyright; Pearse's own "
              "transcriptions of his 'morefathers' pages are separately declared public domain "
              "site-wide (confirmed explicitly on the companion Doctrine of Addai page from the same "
              "collection, sent in the same conversation: 'transcribed by Roger Pearse... all material "
              "on this page is in the public domain - copy freely'). A short bibliographic header "
              "(title/creator/rights, matching npnf205's plain-text header convention) was prepended "
              "to the file after gate_texts_registry correctly flagged it as unverifiable - the RTF "
              "conversion carried no such header of its own, unlike the CCEL page exports used "
              "elsewhere in this registry."),
    TextEntry("chronicle-of-edessa_cowper.txt", "Mark", "2026-08-18",
              "The Chronicle of Edessa (anonymous Syriac, composed c. 540s CE), translated by B. H. "
              "Cowper as 'Selections from the Syriac, No. 1' in the Journal of Sacred Literature - "
              "from Roger Pearse's 'morefathers' collection. Acquired to close srcSYR021, which the "
              "corpus bridge recorded as coverage:none: the Chronicle is the sole surviving witness "
              "for much of Edessa's own civic chronology and this world had no English of it on disk. "
              "RTF attachment converted mechanically by the same purpose-written reader used for the "
              "Ephraim and Aphrahat files; no content passed through model-generated output. "
              "ATTRIBUTION is from the file itself rather than inferred: the piece is signed 'B.H.C.' "
              "and cites J.S.L. Third Series Vol. VII (July 1858) as recent, plus Cowper's own Syrian "
              "Miscellanies. RIGHTS: public domain BY DATE - a mid-19th-century periodical "
              "translation, which clears the 'to ~1929' rule outright. Worth stating explicitly "
              "because the file vendored immediately before it, the Hallock Aphrahat, does NOT: that "
              "one rests on the transcriber's declaration alone under a project-lead ruling, and this "
              "one does not need to. Pearse's declaration is present here too, as confirmation rather "
              "than as the basis."),
    TextEntry("aphrahat_demonstrations-2-7_hallock1932.txt", "Mark", "2026-08-18",
              "Aphrahat the Persian Sage, Demonstration VII (On Penitents) and Demonstration II (On "
              "Love), trans. Frank H. Hallock, Journal of the Society of Oriental Research 16 (1932), "
              "pp. 43-56 and the companion piece - from Roger Pearse's 'morefathers' collection. "
              "Acquired to close the split named on srcSYR010's scope determination: NPNF2-13 carries "
              "eight of the 23 Demonstrations, and syrlex007 cites 'Dem. 6:8 and 7:20' in one breath, "
              "6 being in that eight and 7 not. Demonstration II is a bonus - no record cites it yet. "
              "RTF attachment converted mechanically by the same purpose-written reader used for the "
              "Ephraim file; no content passed through model-generated output.\n"
              "\n"
              "RIGHTS - THE FIRST FILE IN THIS CORPUS THAT DOES NOT CLEAR THE DATE RULE, so the basis "
              "is recorded here rather than assumed. Every other file here is public domain by "
              "publication date alone (ANF/NPNF, Mitchell 1912/1921, Clarke 1918, Phillips 1876), "
              "which is the 'to ~1929' line the Presence Gate Spec's own path table states. Hallock's "
              "translation is 1932: in the US, works published 1930-1963 are public domain only where "
              "copyright was not renewed, and no renewal check has been performed. What this file "
              "rests on instead is the transcriber's own explicit declaration, present verbatim in the "
              "file - Roger Pearse, Ipswich, 2006, declaring all material on the page public domain - "
              "the same declaration the Palladius and Doctrine of Addai files already rest on, and "
              "there confirmed by grep on the page itself.\n"
              "\n"
              "The gap was flagged before vendoring and the file was HELD rather than vendored while "
              "it was open. Mark ruled on 2026-08-18, in these words: 'vendor it, pearse's declaration "
              "is enough.' Recorded as a project-lead act, with the reasoning visible, so that a later "
              "reader can see this file's basis differs in kind from its neighbours' and can revisit "
              "it without having to rediscover why."),
    TextEntry("ephraim_prose-refutations_mitchell1912-1921.txt", "Mark", "2026-08-18",
              "Ephraim the Syrian, Prose Refutations of Mani, Marcion and Bardaisan, transcribed and "
              "translated by C. W. Mitchell from the palimpsest B.M. Add. 14623 - Vol. I, The "
              "Discourses Addressed to Hypatius (Williams and Norgate for the Text and Translation "
              "Society, 1912); Vol. II, The Discourse Called 'Of Domnus' and Six Other Writings "
              "(1921), completed by A. A. Bevan and F. C. Burkitt after Mitchell's death. From Roger "
              "Pearse's 'morefathers' CCEL collection, the same source as the Palladius and Doctrine "
              "of Addai files above and on the same rights basis: Mitchell's translation was published "
              "1912 and 1921, long out of US copyright, and Pearse's transcriptions are declared "
              "public domain site-wide. Supplied as an RTF attachment and converted mechanically - no "
              "content passed through model-generated output. CONVERTER NOTE: striprtf (used for "
              "Palladius) is not installed here and LibreOffice would not load the file, so the "
              "conversion used a purpose-written RTF reader. Its first output shattered words across "
              "lines ('Teache/r/s', 'long p/eriod') because it emitted the source file's own "
              "line-wrapping; in RTF a bare CR/LF is insignificant whitespace and only \\par marks a "
              "break. Fixed and re-run, then verified by locating a broken token intact. That mattered "
              "here more than usual: a vendored text exists to have quotations LOCATED in it, and one "
              "with words split mid-token would have failed silently at exactly that job. Structural "
              "integrity confirmed: both volumes present in the one file, with the five Discourses to "
              "Hypatius and Vol. II's 'Of Domnus', Against Marcion I-III, Against Bardaisan, On "
              "Virginity and Against Mani all located by their own section headings. A bibliographic "
              "header (title/creator/rights, matching the Palladius convention) was prepended - the "
              "RTF carried none. This is the acquisition that reverses srcSYR007's paraphrase-only "
              "determination of 2026-08-18, by the route that determination itself named."),
    TextEntry("addai_doctrine-of-addai.txt", "Mark", "2026-08-15",
              "The Doctrine of Addai, from Roger Pearse's 'morefathers' collection - identified as "
              "essential for closing syriac's srcSYR020 (the Abgar-Addai foundation legend, cited "
              "across gravity/figure/source/story/world_core records, currently consulted_as: "
              "secondary-report-only, citing only modern in-copyright editions - Howard 1981, Lollar "
              "2023). Supplied first as pasted chat text (withdrawn, same reason as Palladius), then "
              "as an actual DOCX file attachment, converted mechanically via python-docx - no content "
              "passed through model-generated output. The page's own explicit public-domain "
              "declaration ('transcribed by Roger Pearse... copy freely') is present in the file "
              "itself, confirmed by grep. TRANSLATOR NOTE: unlike Palladius, this page does not credit "
              "a translator within its own text; the 1876 Phillips attribution rests on external "
              "bibliographic grounds only and is flagged as such in the file's own prepended header, "
              "not asserted as independently confirmed. A short bibliographic header was prepended for "
              "the same reason as npnf205/Palladius - the DOCX conversion carried none of its own, and "
              "the page's own rights line sits at the file's end, past gate_texts_registry's read "
              "window."),
    TextEntry("optatus_against-the-donatists.txt", "Mark", "2026-08-15",
              "Optatus of Milevis, Against the Donatists, trans. O.R. Vassall-Phillips (Longmans, "
              "Green & Co., 1917), from Roger Pearse's 'morefathers' collection. THE single most "
              "strategically valuable item identified in the 'which CCEL resources would be "
              "essential' survey earlier this session: not a fix for any built world, but THE primary "
              "source for Donatism, one of the census's three 'Selected - Not Yet Built' worlds. No "
              "built world currently cites Optatus or the Donatists at all (confirmed by grep) - pure "
              "future world-building material. Converted mechanically via python-docx, no content "
              "passed through model-generated output. RIGHTS: the DOCX conversion itself carried no "
              "rights statement (unlike Palladius and the Doctrine of Addai, whose transcriptions "
              "included one); Mark confirmed the source page's own footer directly, 2026-08-15: "
              "'This text was transcribed by Roger Pearse, Ipswich, UK, 2006. All material on this "
              "page is in the public domain - copy freely.' Now recorded in the file's own header "
              "alongside the 1917-publication-date grounds already noted. Translator name still not "
              "found within the transcription itself; attributed to Vassall-Phillips on "
              "external bibliographic grounds only."),
    TextEntry("origen_philocalia_lewis1911.txt", "Mark", "2026-08-21",
              "Origen, The Philocalia (the Greek anthology of Origen's own writing compiled by Basil "
              "the Great and Gregory Nazianzen), trans. George Lewis (T. & T. Clark, Edinburgh, 1911), "
              "from Roger Pearse's tertullian.org transcription. Identified and flagged for "
              "acquisition by the Alexandria world-build thread's own step-2 search "
              "(alx.search.origen-philocalia-lewis, 2026-08-20) - valuable specifically because it "
              "preserves passages in Greek unfiltered by Rufinus's Latin softening of De Principiis. "
              "Supplied 2026-08-21 as a DOCX file attachment, converted mechanically via a zip/XML "
              "text extraction (paragraph boundaries preserved from </w:p> splits) - no content passed "
              "through model-generated output. RIGHTS: the docx's own last paragraph carries Pearse's "
              "declaration verbatim - 'This text was transcribed by Roger Pearse, 2003. All material "
              "on this page is in the public domain - copy freely' - matching the same transcriber and "
              "site already relied on for addai/optatus/palladius above. TRANSLATOR NOTE: unlike those "
              "three, this transcription does not name George Lewis or T. & T. Clark, 1911 anywhere "
              "inline; that identification is carried over from the search record's own independent "
              "cross-check against archive.org (archive.org/details/philocaliaoforig00orig), not "
              "reconfirmed within this file itself. A bibliographic header (title/creator/print-basis/"
              "rights/source-collection, matching the palladius/npnf205 convention) was prepended, "
              "since the extraction carried none of its own. This ENTRIES row (and this script's own "
              "presence on this branch) closes the tooling gap the build-thread handoff flagged: "
              "texts_registry.py lived only on claude/table-voice-reset-nufsm4 and cic/texts/README.md "
              "had been hand-edited once for this file as a result."),
    TextEntry("npnf209_hilary-poitiers-john-damascus.xml", "Mark", "2026-08-18",
              "NPNF Series II, Vol. 9: Hilary of Poitiers; John of Damascus. Supplied the same day "
              "Texts_Acquisition_Wantlist.md named it as the one series volume missing from the "
              "vendored set - 37 of 38 were already here - and as the want-list's only Tier 1 entry. "
              "CCEL ThML, DC.Rights 'Public Domain', print source Edinburgh: T&T Clark, 1898. "
              "CORRECTION TO THE ASK THAT REQUESTED IT: the Imperial-Juridical scrub (finding 7) and "
              "the want-list both predicted this volume would carry Ad Constantium and Contra "
              "Auxentium. It does not. Reading its own division titles, the NPNF selection is De "
              "Synodis, De Trinitate, three Homilies on Psalms, and John of Damascus's Exposition of "
              "the Orthodox Faith; Hilary's historical/polemical works are not translated here. "
              "Auxentius appears 64 times but in the editor's Introduction, not as Contra Auxentium "
              "text. WHAT IT DOES CARRY, which is worth more than what was asked for: Hilary's De "
              "Synodis reproduces the Eastern creeds verbatim with their numbered anathemas ('If any "
              "man says that the Father and the Son are two Gods: let him be anathema') across a "
              "167,000-character span, plus the Homoean formula that the Son is 'like the Father in "
              "all things, as Scripture says.' That resolves the caveat on the imperial scrub's "
              "finding 4: those creeds were previously reachable only through npnf204 (Athanasius's "
              "De Synodis), and srcIJC24 excludes the Athanasius corpus beyond the single Julius "
              "quotation. Hilary is an independent Latin transmitter of the same texts, so the "
              "exclusion does not apply and no owner decision is needed to use them. Vendored for "
              "future reference; no quote or source record cites it yet."),
    TextEntry("webbe_world-english-bible-british-edition.xml", "Claude (at Mark's direction)",
              "2026-08-19",
              "THE FIRST BIBLE IN THIS CORPUS, and it is here for one narrow job: the SPOKEN layer "
              "of a quote record whose figure is quoting scripture. Mark's two-layer wording ruling "
              "(2026-08-19) gives each quote a historical wording and a plain modern one; where the "
              "father is quoting scripture, the modern layer may not carry this build's own "
              "paraphrase of a verse, so it needs a modern translation that is genuinely free. Three "
              "records were held pending this file: halq003 (Matt 6:21), ijcq010 (Ps 116:15), "
              "pahcq005 (Deut 6:5, Lev 19:18, Matt 22:37/39). NOTE WHAT THIS DOES NOT CHANGE: the "
              "Bible remains outside the six worlds' EVIDENCE base by design - these worlds are "
              "post-apostolic and are reconstructed from what they themselves wrote. This file is a "
              "wording source for verses a father already quotes, never a source of evidence about "
              "a world. "
              "WHICH EDITION AND WHY. The British Edition (WEBBE), not the main WEB, because the "
              "main edition renders the divine name 'Yahweh' and the British and Messianic editions "
              "render it 'LORD' - Mark chose LORD, and Ps 116:15 is one of the three held verses, so "
              "the difference was live rather than theoretical. The cost is British spelling "
              "('neighbour' in Lev 19:18 and Matt 22:39), which is the trade the only LORD-rendering "
              "non-Messianic edition carries. "
              "PROVENANCE. ebible.org is blocked by this sandbox's egress policy - the same "
              "condition this module's own WHY records for every patristic host, and the reason the "
              "corpus is vendored at all - so the file came through the seven1m/open-bibles mirror "
              "of eBible.org's USFX distribution. It authenticates itself rather than resting on the "
              "mirror: it names itself the World English Bible British Edition, references "
              "eBible.org's usfx.xsd schema, and carries the WEB preface's own public-domain "
              "declaration, which is what rights_declared() reads. A bibliographic header was "
              "prepended for the same reason as Palladius and the Doctrine of Addai - the "
              "distribution carries no 'Rights:' line of its own and its prose declaration sits far "
              "past the 100-line read window - but written as an XML COMMENT rather than plain text, "
              "so the file stays valid XML for ElementTree."),
    TextEntry("morison_st-basil-and-his-rule_1912.txt", "Mark", "2026-08-30",
              "E. F. Morison, 'St. Basil and His Rule: A Study in Early Monasticism' (Oxford: Henry "
              "Frowde, 1912), The S. Deiniol's Series III - supplied as a DOCX attachment (a Google "
              "Books scan of the University of California copy), converted mechanically via zip/XML "
              "text extraction (paragraph boundaries from </w:p> splits, entities unescaped) - no "
              "content passed through model-generated output. Identified while cross-checking the "
              "Nicene-Cappadocian world's Source Acquisition Manifest against this registry: Mark "
              "supplied it in response to that manifest's ask for Clarke's 1925 Ascetic Works "
              "translation, but it is a DIFFERENT work - not a substitute, a related find. THIS IS "
              "MORISON'S OWN SECONDARY STUDY of Basil's Rule (14 thematic chapters: Introductory/"
              "Historical, the Retreat in Pontus, Basil's Ascetic Writings, the Inspiration of the "
              "Monastic Life, the Practice of Asceticism, the Community Life, Obedience and "
              "Discipline, the Monk at Prayer, the Monk at Work, Vocation and Vows, Women/Children/"
              "and Slaves, Food and Clothing, Hospitality and Charity, Conclusion), NOT a translation "
              "of the complete Longer and Shorter Rules - Clarke's 1925 translation remains a "
              "separate, still-needed acquisition for the Q&A-form primary text itself. It does carry "
              "two genuine primary-source excerpts in its own right: Appendix A is a translated "
              "excerpt of Basil's own Introduction/Proem to the Longer Rules (continuous first-person "
              "primary text, not commentary); Appendix B is the analogous Introduction to the Shorter "
              "Rules. Appendix C covers the Synod of Gangra's decrees - likely redundant with the "
              "canons already in npnf214_seven-ecumenical-councils.xml, not independently checked "
              "against it. RIGHTS: 1912 publication date clears this registry's own 'to ~1929' rule "
              "independent of the Google Books scan's own public-domain declaration, present in the "
              "original scan but stripped along with the UC library return-slip boilerplate before "
              "vendoring; the bibliographic header prepended to the file records both bases. The "
              "chapter on 'Women, Children, and Slaves' (ch. XI) is likely directly useful for the "
              "Cappadocian build's Article 20 against-the-grain evidence work, not yet drawn on."),
    TextEntry("gregory-nazianzen_first-invective-against-julian_king1888.txt", "Mark", "2026-08-30",
              "Gregory Nazianzen, Oration 4 (First Invective Against Julian), trans. C. W. King, from "
              "'Julian the Emperor' (Bohn's Ecclesiastical Library, 1888) - supplied as a DOCX "
              "attachment (Roger Pearse's tertullian.org transcription), converted mechanically via "
              "zip/XML text extraction, same method as the Morison file above - no content passed "
              "through model-generated output. Closes a real gap the Nicene-Cappadocian world's "
              "Source Acquisition Manifest named: the vendored "
              "npnf207_cyril-jerusalem-gregory-nazianzen.xml (NPNF2 vol. 7, Select Orations) does NOT "
              "include Orations 4-5, confirmed by direct structural check of that file. ONLY Oration "
              "4 is in THIS file - King's volume also carries Oration 5 (the Second Invective) and "
              "Libanius' Monody on Julian, neither supplied here and both still an open acquisition "
              "if wanted. Pearse's own public-domain declaration survives at the file's end, "
              "preserved rather than stripped; a bibliographic header was prepended since the DOCX "
              "conversion carried none of its own."),
    TextEntry("basil_ascetic-works-longer-shorter-rules_clarke1925.txt", "Mark", "2026-08-30",
              "Basil of Caesarea, 'The Ascetic Works of Saint Basil', trans. W. K. L. Clarke, D.D. "
              "(SPCK / Macmillan, 1925, Translations of Christian Literature Ser. I) - supplied as a "
              "DOCX attachment (a scan of the School of Theology at Claremont / USC Library copy), "
              "converted mechanically via zip/XML text extraction, same method as the Morison and "
              "Nazianzen-invective files above - no content passed through model-generated output. "
              "Closes the Nicene-Cappadocian world's single highest-priority remaining source gap: "
              "the world's best window on the brotherhoods' own legislation (Doc_02 sec 1.1, sec 8). "
              "Confirmed COMPLETE per its own table of contents - not just the two Rules, but the full "
              "Ascetica: the scholarly Introduction, the Praevia Institutio Ascetica, the Sermo de "
              "Renuntiatione Saeculi, the Sermo de Ascetica Disciplina, De Iudicio Dei, De Fide, the "
              "MORALIA, THE LONGER RULES (Regulae Fusius Tractatae), and THE SHORTER RULES (Regulae "
              "Brevius Tractatae). This is the GREAT Asketikon; the earlier, non-Greek SMALL Asketikon "
              "(Rufinus' Latin, Syriac) remains unfilled and has no known open English translation. "
              "RIGHTS: 1925 publication date clears this registry's own pre-1929 rule; independently "
              "confirmed by the scan's own trailing library catalog card (preserved at the file's "
              "end), which gives author, translator, publisher, and date verbatim. Clarke also "
              "translated this project's already-vendored palladius_lausiac-history_clarke1918.txt, "
              "and (per this book's own back-cover listing) 'The Life of St. Macrina' - a separate, "
              "still-needed acquisition for this world."),
    TextEntry("gregory-nazianzen_second-invective-against-julian_king1888.txt", "Mark", "2026-08-30",
              "Gregory Nazianzen, Oration 5 (Second Invective Against Julian), trans. C. W. King, from "
              "'Julian the Emperor' (Bohn's Ecclesiastical Library, 1888) - supplied as a DOCX "
              "attachment (Roger Pearse's tertullian.org transcription), converted mechanically via "
              "zip/XML text extraction, same method as the companion Oration 4 file above - no "
              "content passed through model-generated output. Completes the pair the Nicene-"
              "Cappadocian world's Source Acquisition Manifest asked for: gregory-nazianzen_first-"
              "invective-against-julian_king1888.txt (Oration 4) plus this file (Oration 5) together "
              "cover both orations NPNF2 vol. 7's Select Orations volume omits. King's volume also "
              "carries Libanius' Monody on Julian, not supplied in either file and still an open "
              "acquisition if wanted. Pearse's own public-domain declaration survives at the file's "
              "end, preserved rather than stripped; a bibliographic header was prepended since the "
              "DOCX conversion carried none of its own."),
    TextEntry("gregory-nyssa_life-of-macrina-introduction-only_clarke1916.txt", "Mark", "2026-08-30",
              "W. K. Lowther Clarke's INTRODUCTION to his 1916 translation of Gregory of Nyssa's Life "
              "of St. Macrina (SPCK, Early Church Classics) - supplied as a DOCX attachment (Roger "
              "Pearse's tertullian.org transcription), converted mechanically via zip/XML text "
              "extraction - no content passed through model-generated output. IMPORTANT: this is the "
              "introduction ONLY, not the translated Vita narrative itself - the file's own trailing "
              "'Previous Page / Table Of Contents / Next Page' navigation confirms it is one page of "
              "a multi-page site transcription, and the actual biography (Macrina's deathbed, her "
              "teaching, the community at Annesi) is on a page not supplied here. Still a real, "
              "useful acquisition: carries genuine biographical facts about Gregory of Nyssa (birth "
              "c. 335; his marriage to a Theosebeia -- possibly, not certainly, the same Theosebia "
              "named in Doc_02's sec 6 via Gregory of Nazianzus' Ep. 197, not to be conflated without "
              "checking; his forged reconciliation letter, Basil's Ep. 58; his 376-378 deposition and "
              "exile; his 379 visit to Macrina after Basil's death and the Council of Antioch; death "
              "'about 395'), the double-monastery arrangement at Annesi (Peter over the men, Macrina "
              "over the women), and the Pontus monasteries' background. SUPERSEDED 2026-08-30 by "
              "gregory-nyssa_life-of-macrina_clarke1916.txt, which carries the complete work; kept "
              "per this registry's no-deletion practice but redundant with the complete file below."),
    TextEntry("gregory-nyssa_life-of-macrina_clarke1916.txt", "Mark", "2026-08-30",
              "W. K. Lowther Clarke's COMPLETE 1916 translation of Gregory of Nyssa's Life of St. "
              "Macrina (SPCK, Early Church Classics), introduction and narrative together - supplied "
              "as a second, larger DOCX attachment (Roger Pearse's tertullian.org transcription), "
              "converted mechanically via zip/XML text extraction, same method as every other file "
              "vendored this session - no content passed through model-generated output. SUPERSEDES "
              "gregory-nyssa_life-of-macrina-introduction-only_clarke1916.txt (vendored earlier the "
              "same day from a first, shorter upload that turned out to carry only Clarke's "
              "introduction, confirmed by its own trailing site-navigation footer) - that file is "
              "kept per this registry's no-deletion practice, but this file is the one to cite for "
              "any Macrina narrative content going forward. Confirmed complete by internal content: "
              "opens with Clarke's introduction (as before), then continues into Gregory's own "
              "epistolary narrative to the monk Olympius - Naucratius' death and Macrina comforting "
              "their mother, Emmelia's own death, Macrina's final illness and deathbed teaching, her "
              "death and funeral (Bishop Araxius of the district presiding) - ending 'THE END' with "
              "the volume's own printer's colophon (Richard Clay & Sons). Pearse's public-domain "
              "declaration survives mid-file at the introduction/narrative boundary, preserved "
              "rather than stripped; a bibliographic header was prepended since the DOCX conversion "
              "carried none of its own. This is the world's entire primary-text basis for Macrina "
              "(Doc_02 sec 1.4) - the single most load-bearing text for this world's 'primary voice "
              "with no primary text' finding and for the female-voice question at the G2 identity "
              "decision."),
    TextEntry("philostorgius_ecclesiastical-history_walford1855.txt", "Mark", "2026-08-31",
              "Photius' Epitome of Philostorgius' lost Ecclesiastical History, trans. Edward Walford "
              "(Bohn's Ecclesiastical Library, 1855) - supplied as a DOCX attachment (Roger Pearse's "
              "tertullian.org transcription, 2002), converted mechanically via zip/XML text "
              "extraction, same method as every other file vendored this session - no content "
              "passed through model-generated output. Confirmed complete: all twelve books present "
              "(Philostorgius' original does not survive independently - everything here is "
              "Photius' hostile epitome), Walford's translator's Biographical Notice, Pearse's 2002 "
              "note quoting Quasten's Patrology on manuscript transmission, and the full set of 241 "
              "numbered footnotes, ending with the volume's own 'THE END'. Pearse's public-domain "
              "declaration survives at the file's end, preserved rather than stripped; a "
              "bibliographic header was prepended since the DOCX conversion carried none of its "
              "own. This is the world's one surviving Eunomian narrative voice (Doc_02 sec 1.6) - "
              "the project's rare control on the losing side's own frame, filtered through a hostile "
              "epitomizer, a caveat this world's use of the text must carry forward."),
)


def read_header(path: Path, lines: int = 100) -> str:
    """The file's own first N lines - generous on purpose, and widened twice
    now for two different real reasons. Two of the ten plain-text files have
    titles that wrap across 4-6 lines before the Rights: line appears; an
    8-line window (this module's first draft) missed both and would have
    false-flagged two genuinely public-domain files as unverified. Then the
    anf01 XML swap: ThML's own <DC.Rights> Dublin-Core element sits at line
    68 in that file's real header, well past the 30-line window that had
    covered every plain-text file fine - widened to 100 with margin for
    other ThML files' own varying metadata-block length.
    """
    out = []
    with path.open(encoding="utf-8", errors="replace") as f:
        for _ in range(lines):
            line = f.readline()
            if not line:
                break
            out.append(line)
    return "".join(out)


def rights_declared(header: str) -> str | None:
    """The file's own stated rights basis, or None if it cannot be found -
    checked fresh every run, not trusted from whatever note accompanied the
    file when it was vendored."""
    m = _RIGHTS_LINE.search(header)
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()  # exactly one alternative matches


def title_declared(header: str) -> str | None:
    m = _TITLE_LINE.search(header)
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()


def discovered_files() -> list[str]:
    """What is ACTUALLY sitting in cic/texts/ right now, not what ENTRIES
    claims - the two are cross-checked in report(), not assumed to agree."""
    # Both plain-text renderings and CCEL's native ThML XML source live here
    # now (the anf01 swap, 2026-08-15) - a *.txt-only glob went blind to the
    # first .xml file added and silently reported it as a missing file, a
    # real bug caught live while doing that swap, not a hypothetical one.
    return sorted(p.name for p in TEXTS_DIR.iterdir()
                  if p.is_file() and p.suffix in (".txt", ".xml"))


def citing_records(filename: str) -> list[str]:
    """Every record under cic/records/ whose own text mentions this vendored
    file by path - source records typically for the translation-edition
    claim, quote records typically for the transcription itself. Computed by
    scanning the records, not read off a static field: a citation this
    session actually has to catch lives in the QUOTE record's body prose for
    anf01, not in its source record at all (srcPAHCS62 never repeats the
    path; pahcq001-004 do) - a coverage-only source-record scan would have
    silently under-counted a real, already-verified citation.
    """
    needle = f"cic/texts/{filename}"
    hits = []
    for p in sorted(RECORDS_DIR.rglob("*.md")):
        try:
            if needle in p.read_text(encoding="utf-8"):
                hits.append(p.stem)
        except Exception:  # noqa: BLE001
            continue
    return hits


@dataclass
class Row:
    entry: TextEntry | None
    filename: str
    exists: bool
    rights: str | None
    title: str | None
    citing: list[str] = field(default_factory=list)


def registry_problems(entries: tuple, discovered: list, headers: dict) -> list:
    """PURE - no file I/O, no import of anything that touches disk. entries:
    TextEntry tuples (what's declared). discovered: filenames actually found
    under cic/texts/ (what's real). headers: {filename: its own header text},
    already read by the caller. Returns violation strings.

    Split out from report()/the live gate deliberately, for T3-G's own
    reason: "a gate that never fails checks nothing" only means something if
    the gate can be handed a KNOWN-BROKEN case and shown to catch it. A
    version of this logic that always reads the real cic/texts/ directory
    can only ever be fixture-tested against whatever that directory's real
    state happens to be right now (today, genuinely clean) - which proves
    nothing about whether the CHECK is correct, only that nobody has broken
    anything yet. This function takes plain data instead, so gate_fixtures.py
    can hand it a literal broken case with no real file on disk at all.

    THREE integrity checks, deliberately not four. Missing rights line,
    undeclared file, orphaned ENTRIES row are real mistakes with a knowable
    right answer - today's baseline is genuinely zero, so any of the three
    appearing is new, current-moment state worth catching immediately, not
    legacy debt to grandfather (the reasoning that made mechanism_coverage
    advisory does not apply here). Whether a vendored file has been CITED
    YET is deliberately NOT a fourth check here: an unexploited volume is
    not a mistake, and turning it into a violation would be inventing a
    threshold nobody asked for - exactly the "assume the floor" move
    mechanism_coverage's own docstring already refuses for the same reason.
    Citation counts stay in report()'s informational output only.
    """
    problems = []
    declared = {e.filename for e in entries}
    found = set(discovered)
    for name in sorted(declared - found):
        problems.append(f"{name}: declared in ENTRIES but no file present in cic/texts/")
    for name in sorted(found - declared):
        problems.append(f"{name}: file present in cic/texts/ but no ENTRIES row - "
                        f"undeclared vendoring")
    for name in sorted(declared & found):
        r = rights_declared(headers.get(name, ""))
        if not (r and "public domain" in r.lower()):
            problems.append(f"{name}: no verifiable public-domain rights line found in its "
                            f"own header ({r!r}) - do not treat as cleared for use")
    return problems


def registry_problems_live() -> list:
    """The real check: ENTRIES against whatever is actually sitting in
    cic/texts/ right now, headers read fresh. This is what gate_texts_registry
    (gates.py) and report() below both call - one place this logic lives,
    so the CLI report and the gate's verdict can never quietly disagree."""
    discovered = discovered_files()
    headers = {name: read_header(TEXTS_DIR / name) for name in discovered}
    return registry_problems(ENTRIES, discovered, headers)


def build_rows() -> list[Row]:
    by_name = {e.filename: e for e in ENTRIES}
    names = sorted(set(by_name) | set(discovered_files()))
    rows = []
    for name in names:
        path = TEXTS_DIR / name
        exists = path.exists()
        header = read_header(path) if exists else ""
        rows.append(Row(
            entry=by_name.get(name),
            filename=name,
            exists=exists,
            rights=rights_declared(header) if exists else None,
            title=title_declared(header) if exists else None,
            citing=citing_records(name) if exists else [],
        ))
    return rows


def report() -> int:
    rows = build_rows()
    namecol = max(len(r.filename) for r in rows) + 2
    print(f"{'file':<{namecol}}{'rights':<16}{'cited by':<10}")
    print("-" * (namecol + 26))
    for r in rows:
        if not r.exists:
            print(f"{r.filename:<{namecol}}{'MISSING FILE':<16}")
            continue
        ok = bool(r.rights and "public domain" in r.rights.lower())
        rights_mark = r.rights if ok else f"UNVERIFIED ({r.rights!r})"
        print(f"{r.filename:<{namecol}}{rights_mark:<16}{len(r.citing):<10}")

    uncited = [r.filename for r in rows if r.exists and not r.citing]
    print(f"\n{len(rows)} vendored file(s), {len(uncited)} with zero citing record(s):")
    for name in uncited:
        print(f"  - {name}")

    problems = registry_problems_live()
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nOK: every vendored file has a header-verified public-domain rights line, "
          "an ENTRIES row, and no ENTRIES row points at a missing file.")
    return 0


def write_readme() -> int:
    rows = build_rows()
    lines = [
        "# Vendored public-domain source texts",
        "",
        "Full text of editions this build's quote records cite, committed so that",
        "wording can be verified *reproducibly* -- by any session, at any time,",
        "without network access. That matters here for a specific reason: the",
        "sandbox this project's agents run in blocks every patristic text host",
        "(ccel.org, newadvent.org, wikisource, archive.org, gutenberg, tertullian.org),",
        "so before these files existed a quote record could not be verified at all",
        "and `gate_quote_fidelity_recording` had nothing honest to record.",
        "",
        "**This file is GENERATED, not hand-edited** -- run",
        "`python cic/engine/texts_registry.py --write-readme` after vendoring a new",
        "file or adding an ENTRIES row in that module. Editing this table directly",
        "will be overwritten the next time it runs.",
        "",
        "PUBLIC DOMAIN ONLY. Every file here must be out of copyright, and its own",
        "provenance header must say so -- the `rights` column below is read fresh",
        "from each file's own header every time this report runs, not trusted from",
        "a claim made when the file was added. In-copyright editions (Holmes 2007,",
        "Ward 1975) are referenced by `source` record and never vendored --",
        "committing them would be redistribution.",
        "",
        "| file | title (from the file's own header) | rights | supplied | added | cited by |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        if not r.exists:
            continue
        e = r.entry
        cited = ", ".join(f"`{c}`" for c in r.citing) if r.citing else "-"
        supplied = e.supplied_by if e else "?"
        added = e.date_added if e else "?"
        lines.append(f"| `{r.filename}` | {r.title or ''} | {r.rights or 'UNVERIFIED'} "
                     f"| {supplied} | {added} | {cited} |")

    lines.append("")
    lines.append("Notes carried over per file:")
    lines.append("")
    for r in rows:
        if r.entry and r.entry.notes:
            lines.append(f"- **`{r.filename}`** -- {r.entry.notes}")
    lines.append("")
    lines.append(
        "Not records: nothing here is schema-validated or read by the runtime. These "
        "are reference copies for verification, cited by the `source`/`quote` records "
        "that carry the bibliographic and wording claims."
    )
    lines.append("")

    (TEXTS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {TEXTS_DIR / 'README.md'}: {sum(1 for r in rows if r.exists)} file(s) listed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-readme", action="store_true")
    args = ap.parse_args()
    if args.write_readme:
        return write_readme()
    return report()


if __name__ == "__main__":
    sys.exit(main())
