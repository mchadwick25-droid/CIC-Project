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
TEXTS_DIR = ROOT / "texts"
RECORDS_DIR = ROOT / "records"

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
              "srcHAL009's own cross-reference note. Not acted on here - no translation row or quote "
              "drawn from it yet, but both gaps flagged for this volume are now closeable."),
    TextEntry("npnf102_augustine-city-of-god-christian-doctrine.xml", "Mark", "2026-08-15",
              "NPNF Series I, Vol. 2: St. Augustine's City of God and Christian Doctrine. Supplied "
              "with no accompanying text. Completes the full 8-volume NPNF1 Augustine set (01-08, all "
              "now vendored). No built world currently cites City of God or De Doctrina Christiana "
              "directly (a title-text search turned up only unrelated modern secondary sources whose "
              "titles happen to share the phrase 'Christian Doctrine' - srcIJC33, srcPAHCS25 - not "
              "Augustine's work). Vendored for future reference, most plausibly for the "
              "not-yet-built Latin Pastoral-Congregational and Donatism worlds flagged earlier this "
              "session; no quote or source record cites it yet."),
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
