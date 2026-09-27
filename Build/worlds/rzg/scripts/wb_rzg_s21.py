"""B-1 (S2.1): The Reformed Cities - Zurich & Geneva (rzg) source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents
(Doc_01 through the World Profile, Validation Layer, and full Representative
package - all Approved to proceed, handed off by the build thread)
into WRS records under records/rzg/{source,world_core}/, per the live schema
(engine/m1/schemas.py) and gate battery (engine/m1/gates.py). This is the
FIRST record-authoring pass for this world; no `rzg` records existed anywhere
before this script ran (confirmed: no records/rzg/ directory, no `rzg` entry
in records/worlds/).

Built following the established precedent pattern exactly:
Build/worlds/don/scripts/wb_don_s21.py (read in full before this script was
written) - itself following Build/worlds/cappadocian/scripts/wb_cappadocian_s21.py
and Build/worlds/gallic/scripts/wb_gallic_s21.py. No newer precedent exists as of
this build (records/worlds/ registry checked directly: nine worlds admitted,
don the most recent full B-1-through-S2y compile).

INPUTS, mapped to OUTPUTS, precisely:
  - Build/worlds/rzg/Source_Registry.md (17 rows) -> 17 `source` records. Every
    row carries Boundary Status "Native" - none is Excluded, so unlike
    don's row 29, nothing is deliberately withheld here. Ten rows (1-10)
    are Confidence A/B, vendored primary or confessional texts, each with
    a real file under cic/texts/ (kind: vendored). Two rows (11-12) are
    in-copyright secondary scholarship, consultation-only, never vendored
    (kind: unvendored). Five rows (13-17) are Confidence D/E, Native to
    this world's own boundary but NOT YET ACQUIRED - the Registry's own
    words, carried forward here rather than smoothed into a vendored-style
    record (kind: unvendored). This is a real, disclosed gap this world's
    own Open_Gaps_Tracking.md item 4-6 already names (the Ecclesiastical
    Ordinances, the Genevan Psalter, Geneva's own consistory registers,
    Beza's own works, Marie Dentiere's own works) - not invented here, and
    not silently upgraded to look more complete than the Registry itself
    claims.
  - Build/worlds/rzg/Doc_01_World_Identification_Boundaries_Orientation.md SS "Approximate
    Time Horizon" -> time_window (1519-1650, the census's own Era 7 Freeze
    window, an administrative continues-cap for a living tradition, not a
    historical rupture - Doc_01 states this distinction explicitly and it
    is carried into `horizon` below rather than flattened).
  - Build/worlds/rzg/rzg_World_Capsule_Core.md (9 deployed sections, itself a
    synthesis of Doc_01 through the World Profile) -> horizon,
    formation_logic, thinness, cautions, thin_topics. The Capsule Core is
    written in second-person immersive voice for deployment; world_core's
    own fields are NOT scanned by gate_voice_perspective (engine/m1/gates.py
    - confirmed directly this session, same narrow field scope as
    gate_readability: term.plain_meaning/quick_meaning, honest_limit.statement,
    quote.modern_rendering only), and don's own compiled world_core record
    (records/don/world_core/don.core.donatism.md, read in full this session)
    renders `horizon` in third-person descriptive register, not first-person
    "we" - this script follows that same precedent exactly, translating the
    Capsule Core's immersive "you" into a precise, citation-grounded
    third-person account rather than copying its own second-person prose
    verbatim.

WORLD_ID: `the-reformed-cities-zurich-and-geneva`. This world has no entry
in records/worlds/ at all yet (registry addition is a later admission-track
step, out of scope for this first record-authoring pass, exactly as it was
for don and gallic before it) - `the-reformed-cities-zurich-and-geneva`
matches cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml's own
`atlas_id`, which is the census movement id and the join key, so the record
id prefix (`rzg`), the world_id, and the census join all read consistently.

TIME_WINDOW: start 1519, end 1650. Both years are Doc_01's own confirmed,
unambiguous figures (the census's own already-decided Era 7 Freeze window)
- unlike don's own doubled 311/312 opening, there is no
disclosed date ambiguity to carry into `horizon` here; the only thing
`horizon` must state plainly is that 1650 is an administrative
continues-cap for a still-living tradition, not a historical rupture
(Doc_01 itself insists on this distinction, Article 22).

SHELF_ROW is left unset on every row below, matching the fleet-wide
standard (engine/m9/enforce.py's own ACCEPTED_OPEN waivers: every one of
the nine already-admitted worlds carries an "m9:shelf-row/<world>" waiver
blocked on corpus-map's own CM-1 infrastructure landing - confirmed by
direct read this session, not assumed). Populating it here would require
inventing a row_id CM-1 does not yet provide, which the no-guessing rule
forbids; the corresponding waiver is added to engine/m9/enforce.py once
this script's real finding count is measured against a live gate run,
not guessed in advance.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
OUT_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------- rights ---
RIGHTS_VENDORED_VERIFIED = (
    "public-domain; vendored in cic/texts/ and its identity and provenance directly confirmed by this "
    "compilation pass against the vendored file itself (Source_Registry.md's own Verification Note "
    "column, checked directly against cic/texts/ this pass)."
)
RIGHTS_CONSULTATION_ONLY = (
    "in-copyright modern scholarship; consultation-only, never vendored. Named in the census's own "
    "`sources` field and cited for Author Gravity Assessment background only (Doc_02 SS2), never quoted "
    "as licensed vendored material. Bibliographic record only - the volume itself was not opened by this "
    "compilation pass, matching Source_Registry.md's own Verification Note for this row."
)
RIGHTS_NOT_YET_ACQUIRED = (
    "Native to this world's own boundary but NOT YET ACQUIRED (Source_Registry.md's own words, rows "
    "13-17). Confidence D/E - a real, disclosed acquisition gap (Source_Acquisition_Manifest.md; "
    "Open_Gaps_Tracking.md items 4-6), not a rights refusal and not a claim this compilation pass can "
    "resolve. Nothing is vendored or quoted from this row; every field below states what is currently "
    "known about the work itself, not its content."
)

# ------------------------------------------------------------------ rows ---
# Each entry mirrors Source_Registry.md's own row exactly - author/work/edition/
# rights/attribution/discovery/confidence all traceable back to that table's own
# cells, never re-judged here. `body` carries this compilation's own authoring
# notes (what was mechanical vs. a judgment call), per the fleet's file-discipline
# convention: dated build notes live in the record body, never in an operative
# frontmatter field.
ROWS: list[dict] = [
    dict(
        row=1, slug="calvin-institutes-book1",
        author="John Calvin",
        work="Institutes of the Christian Religion, Book I (Of the Knowledge of God the Creator)",
        edition="English translation by Henry Beveridge (Edinburgh: Calvin Translation Society, 1845), "
                "vendored as cic/texts/calvin_institutes-christian-religion-vol1_beveridge1845.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to John Calvin, 1559 final Latin edition, in the standard-cited Beveridge "
                    "1845 English translation. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 1, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="Calvin's own doctrine of God, creation, and providence - Geneva-strand Author Gravity "
             "(Doc_02 SS2). Verified directly against the vendored file, whole file, per Source_Registry.md's "
             "own Verification Note. Corpus map role: tradition.",
    ),
    dict(
        row=2, slug="calvin-institutes-books2-3",
        author="John Calvin",
        work="Institutes of the Christian Religion, Books II-III (Of the Knowledge of God the Redeemer; "
             "Of the Mode of Obtaining the Grace of Christ)",
        edition="English translation by Henry Beveridge (Edinburgh: Calvin Translation Society, 1845), "
                "vendored as cic/texts/calvin_institutes-christian-religion-vol2_beveridge1845.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to John Calvin, 1559 final Latin edition, in the standard-cited Beveridge "
                    "1845 English translation. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 2, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="Christ the Redeemer; faith, justification, predestination - this world's own load-bearing "
             "doctrinal core (G1). Verified directly against the vendored file, whole file, per "
             "Source_Registry.md's own Verification Note.",
    ),
    dict(
        row=3, slug="calvin-institutes-book4",
        author="John Calvin",
        work="Institutes of the Christian Religion, Book IV (Of the External Means or Helps by Which God "
             "Invites Us into the Society of Christ, and Keeps Us in It)",
        edition="English translation by Henry Beveridge (Edinburgh: Calvin Translation Society, 1845), "
                "vendored as cic/texts/calvin_institutes-christian-religion-vol3_beveridge1845.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to John Calvin, 1559 final Latin edition, in the standard-cited Beveridge "
                    "1845 English translation. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 3, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="The church, sacraments, and civil government - G2 and G4's own doctrinal grounding. "
             "Verified directly against the vendored file, whole file, per Source_Registry.md's own "
             "Verification Note. AUTHORED note: the Registry's Source cell names this volume "
             "'Beveridge 1845' although Institutes Book IV is conventionally bound as the translation's "
             "own third volume; the vendored filename (`...vol3_beveridge1845.txt`) resolves this without "
             "ambiguity and is carried as the `edition` field's own file citation.",
    ),
    dict(
        row=4, slug="calvin-geneva-catechism",
        author="John Calvin",
        work="The Catechism of the Church of Geneva",
        edition="English translation by Elijah Waterman (Hartford, 1815), vendored as "
                "cic/texts/calvin_geneva-catechism_waterman1815.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to John Calvin. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 4, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="Calvin's own catechetical, not systematic-theological, register - Geneva's own strand-specific "
             "enactment of G3 (catechesis). Verified directly against the vendored file, whole file, per "
             "Source_Registry.md's own Verification Note.",
    ),
    dict(
        row=5, slug="consensus-tigurinus",
        author="John Calvin and the Zurich pastors (jointly negotiated and signed)",
        work="Mutual Consent in Regard to the Sacraments (the Consensus Tigurinus, 1549/1554)",
        edition="English translation by Henry Beveridge (1844), vendored as "
                "cic/texts/calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt "
                "(a bounded extract, pp. 195-244 of the printed volume - see the file's own intake header "
                "for the exact boundary against the volume's other, distinct contents)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="jointly authored and signed by representatives of Bullinger's own Zurich and Calvin's "
                    "Geneva - the documented Zurich/Geneva doctrinal bridge itself (Doc_01 SS5, Strand "
                    "Determination evidence). Not to be confused with the same source volume's separate, "
                    "later 'Second Defence of the Sacraments... Against Joachim Westphal' (also Calvin, "
                    "1556), which immediately follows in the source volume and is NOT part of the Consensus "
                    "itself - a different work, not vendored, not licensed for anything under this row "
                    "(Source_Registry.md row 5's own Comparandum Note).",
        discovery="Source_Registry.md row 5, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="The single document most directly evidencing the Zurich/Geneva strand bridge (Doc_01 SS5). "
             "The 9th Head of Agreement carries this world's own CT-tagged contested term (Sign and the "
             "Thing Signified, rzglex008) and T2's own second pole. Verified directly against the vendored "
             "file, whole bounded extract, per Source_Registry.md's own Verification Note.",
    ),
    dict(
        row=6, slug="zwingli-sixty-seven-articles",
        author="Huldrych Zwingli",
        work="The Sixty-Seven Articles (1523)",
        edition="Within the collective volume Selected Works (Jackson 1901), vendored as "
                "cic/texts/zwingli_selected-works_jackson1901.txt, lines approx. 4485-4700 within the Acts "
                "of the First Zurich Disputation",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Huldrych Zwingli. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 6, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="Zwingli's own founding doctrinal statement - Zurich-strand Practice/Authority evidence, and "
             "Article XVIII's own remembrance language is T2's own first, earlier pole. Verified directly "
             "against the vendored file at the cited line range, per Source_Registry.md's own Verification "
             "Note. Carried as its own row, separate from row 7's own collective Selected Works bucket, "
             "since it is independently vendored-and-verified rather than merely named within that "
             "collective volume.",
    ),
    dict(
        row=7, slug="zwingli-selected-works",
        author="Huldrych Zwingli",
        work="Selected Works - letter to Erasmus, the Constance petition, the Acts of the First and Second "
             "Zurich Disputations, the 1527 Refutation of the Tricks of the Baptists (incl. its own 'On "
             "Election' section), other shorter writings",
        edition="Translated and edited by Samuel Macauley Jackson (1901), vendored as "
                "cic/texts/zwingli_selected-works_jackson1901.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Huldrych Zwingli, in Jackson's own 1901 English translation and editorial "
                    "arrangement.",
        discovery="Source_Registry.md row 7, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Documented",
        divergence="This row is a collective bucket, not an itemized table of contents - do not cite it as "
                   "though every named component were independently checked (Source_Registry.md row 7's own "
                   "Comparandum Note). Licensed range is 1522-1527 (the "
                   "Refutation's own dated heading extends past the row's originally-stated 1522-1523 "
                   "range); the Refutation's own 'On Election' section (lines approx. 9591-9762) is "
                   "independently verified against the file directly, distinct from the "
                   "rest of this row's own un-itemized contents.",
        body="Zurich's own reform record, 1522-1527; election/predestination doctrine per Doc_04 SS3.1 - "
             "the 'On Election' passage grounds rzglex001's own Zurich-strand voice. Locus named (whole "
             "file except the Sixty-Seven Articles, carried separately at row 6); individual items within "
             "this row not separately re-verified this pass beyond the Refutation's own Election section - "
             "Doc_01 SS8 item 6's own still-open table-of-contents completeness question, carried forward "
             "rather than silently resolved.",
    ),
    dict(
        row=8, slug="zwingli-latin-works-vol1",
        author="Huldrych Zwingli",
        work="The Latin Works and the Correspondence of Huldreich Zwingli, Vol. I",
        edition="Translated and edited by Samuel Macauley Jackson (1912), vendored as "
                "cic/texts/zwingli_latin-works-correspondence-vol1_jackson1912.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Huldrych Zwingli, in Jackson's own 1912 English translation and editorial "
                    "arrangement; this volume also carries, embedded within it, Oswald Myconius's own "
                    "'Original Life of Zwingli' (Section XII narrates Zwingli's own death at the Second "
                    "Battle of Kappel, 1531, in near-eyewitness detail) - a distinct authorial voice within "
                    "the same vendored file, disclosed rather than merged into Zwingli's own attribution.",
        discovery="Source_Registry.md row 8, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Documented",
        divergence="Multi-work compilation per the file's own intake header - same collective-bucket "
                   "caution as row 7 (Source_Registry.md row 8's own Comparandum Note); not itemized by "
                   "individual work within the file.",
        body="Early treatises and letters, a second independent Zwingli volume; also the source for "
             "Myconius's own eyewitness account of Zwingli's death (rzgstory003) and the one thin, "
             "non-narrative Marburg Colloquy mention (Doc_09 SS6). Locus named (whole file); not itemized "
             "by individual work within the file.",
    ),
    dict(
        row=9, slug="second-helvetic-confession",
        author="Heinrich Bullinger",
        work="The Second Helvetic Confession (1566)",
        edition="Vendored as cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt, "
                "Sec. 55 (original pp. 390-421), within Philip Schaff's compiled Creeds of Christendom "
                "(1919 printing)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Heinrich Bullinger. No attribution dispute exists for this work.",
        discovery="Source_Registry.md row 9, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence=None,
        body="Zurich's own mature confessional statement - this world's own doctrinal-floor text (ch. III "
             "Trinity, ch. XI Christ's full deity and humanity, per Doc_04 SS - directly verified against "
             "this vendored text). Bullinger's own Chapter X carries the CT contest's own pastoral "
             "framing (rzglex008's own Key Sources). Verified directly against the vendored file at the "
             "cited section, per Source_Registry.md's own Verification Note.",
    ),
    dict(
        row=10, slug="heidelberg-catechism",
        author="Zacharias Ursinus and Caspar Olevianus (traditional joint attribution)",
        work="The Heidelberg Catechism (1563)",
        edition="Vendored as cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt, "
                "Sec. 69 (original pp. 529-554), within Philip Schaff's compiled Creeds of Christendom "
                "(1919 printing)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="traditional joint attribution to Ursinus and Olevianus; Olevianus's own share is "
                    "disputed in current scholarship (Doc_01 SS2) - this row does not adjudicate that "
                    "question.",
        discovery="Source_Registry.md row 10, added 2026-09-15; corpus map / "
                  "cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="The Palatinate's own catechetical voice, institutionally distinct from Geneva's - "
                   "doctrinal continuity not independently verified this pass (Doc_02 SS1, SS8). This same "
                   "file's own apparatus (lines 2751, 2869, 2878) quotes the Synod of Dort's 148th Session "
                   "(1 May 1619) verdict approving this Catechism, a real vendored touch-point with Dort "
                   "distinct from the Zurich/Geneva delegation question (Doc_01 SS7). Joint authorship traditional, not independently adjudicated - do not "
                   "cite this row as settling that question.",
        body="Verified directly against the vendored file at the cited section, per Source_Registry.md's "
             "own Verification Note. Corroborating rather than load-bearing: this world's own boundary is "
             "Zurich/Geneva, and this Catechism's own institutional continuity with that boundary is "
             "itself not independently verified (Doc_02 SS1).",
    ),
    dict(
        row=11, slug="gordon-calvin-biography",
        author="Bruce Gordon",
        work="Calvin",
        edition="New Haven: Yale University Press, 2009",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Bruce Gordon. In-copyright modern scholarship.",
        discovery="Source_Registry.md row 11, added 2026-09-15; named in the census's own `sources` field, "
                  "verified directly against that field this pass; not checked against the actual book.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence=None,
        body="Author Gravity Assessment background for Calvin's own biography and Geneva ministry (Doc_02 "
             "SS2) - background only, not itself cited for any specific claim in this world's build. "
             "Consultation-only, per the census's own citation - not a candidate for cic/texts/ "
             "(in-copyright).",
    ),
    dict(
        row=12, slug="manetsch-calvins-pastors",
        author="Scott Manetsch",
        work="Calvin's Company of Pastors",
        edition="Oxford: Oxford University Press, 2013",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Scott Manetsch. In-copyright modern scholarship.",
        discovery="Source_Registry.md row 12, added 2026-09-15; named in the census's own `sources` field, "
                  "verified directly against that field this pass; not checked against the actual book.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence=None,
        body="Background for Geneva's own pastoral/consistorial institutional structure (Doc_01 SS5 "
             "Authority-structure limb) - background only, not itself cited for any specific claim in this "
             "world's build. Consultation-only, per the census's own citation - not a candidate for "
             "cic/texts/ (in-copyright).",
    ),
    dict(
        row=13, slug="geneva-consistory-registers",
        author="Geneva Consistory (contemporary institutional record); this edition trans./ed. Kingdon, "
               "Lambert, and Watt, trans. M. Wallace McDonald",
        work="Registers of the Consistory of Geneva in the Time of Calvin, Vol. 1",
        edition="Grand Rapids: Eerdmans, 2000 - NOT YET ACQUIRED",
        rights=RIGHTS_NOT_YET_ACQUIRED,
        attribution="the underlying registers are Geneva's own contemporary institutional record; this "
                    "specific modern critical edition (Kingdon/Lambert/Watt/McDonald, 2000) is confirmed "
                    "in-copyright and will not be vendored in this edition.",
        discovery="Source_Registry.md row 13, added 2026-09-15; the census's own named archive and stated "
                  "selection rationale for this world (Doc_02 SS5) - its absence from this Registry as an "
                  "actually-usable row is this world's own single largest disclosed source-ecology gap, not "
                  "a minor omission.",
        cite="D", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="A legitimately usable public-domain substitute or excerpt remains a live acquisition "
                   "question (Source_Acquisition_Manifest.md G3) - not resolved by this compilation pass.",
        body="Ordinary-discipline/lived-practice claims, once acquired - not currently usable for any claim "
             "(Confidence D, not-acquired). The census's own named archive for this world; its absence is "
             "the direct cause of this world's own disclosed Absent Stories finding (Doc_09 SS7 item 4: no "
             "Genevan consistory case narrative survives).",
    ),
    dict(
        row=14, slug="ecclesiastical-ordinances-1541",
        author="Geneva city council and John Calvin (jointly promulgated)",
        work="John Calvin's 'Ecclesiastical Ordinances' of 1541",
        edition="No verified public-domain English edition located this pass - NOT YET ACQUIRED",
        rights=RIGHTS_NOT_YET_ACQUIRED,
        attribution="jointly promulgated by Geneva's city council and Calvin; the underlying 1541/1561 "
                    "ordinances themselves are Native to this world, but no specific edition is currently "
                    "held.",
        discovery="Source_Registry.md row 14, added 2026-09-15; Schaff's History of the Christian Church "
                  "Vol. VIII (CCEL) confirmed this pass to be paraphrase/summary only, not a direct "
                  "translation - do not cite Schaff's HCC8 discussion as if it were the Ordinances' own "
                  "text. A 1977 archive.org item carrying an unverified third-party 'Public Domain Mark' "
                  "was not accepted at face value (Doc_02 SS9 item 2).",
        cite="E", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="A genuine public-domain edition, if one exists, has not yet been located (Source_"
                   "Acquisition_Manifest.md G1).",
        body="Consistory authority-structure claims (Doc_01 SS5 Strand Determination limb 2), once "
             "acquired - not currently usable for any claim (Confidence E). T1's own Geneva pole (the "
             "Consistory's own founding instrument) currently rests on Doc_01's general historical account "
             "rather than this text directly.",
    ),
    dict(
        row=15, slug="genevan-psalter",
        author="Clement Marot and Theodore Beza (versification); various (tunes)",
        work="The Genevan Psalter (complete 1562)",
        edition="No edition searched or identified this pass - NOT YET ACQUIRED",
        rights=RIGHTS_NOT_YET_ACQUIRED,
        attribution="versified by Marot and Beza; the underlying Psalter itself is Native to this world, "
                    "but no specific edition is currently held or searched.",
        discovery="Source_Registry.md row 15, added 2026-09-15; not searched this pass beyond the general-"
                  "knowledge citation already in the census's own `sources` field.",
        cite="E", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="This world's own Author Gravity Assessment (Doc_02 SS2) currently characterizes this "
                   "text from the census's own descriptive note and general knowledge only - no vendored "
                   "text backs any specific quotation from it (Source_Acquisition_Manifest.md G2).",
        body="Practice-limb (congregational singing) claims (Doc_01 SS5), once acquired - not currently "
             "usable for any claim (Confidence E). Grounds the World Capsule Core's own Geneva-worship "
             "characterization ('the whole of your praise was set to meter and tune') at general-knowledge "
             "confidence only, disclosed rather than upgraded.",
    ),
    dict(
        row=16, slug="beza-works",
        author="Theodore Beza",
        work="Beza's own works generally (letters, the Tabula praedestinationis, the Genevan Psalter's own "
             "co-authorship)",
        edition="No specific edition identified or searched this pass - NOT YET ACQUIRED",
        rights=RIGHTS_NOT_YET_ACQUIRED,
        attribution="attributed to Theodore Beza; no specific edition currently held or actively searched.",
        discovery="Source_Registry.md row 16, added 2026-09-15; named in the census's own `voices` field; "
                  "a missing-voices item under Article 20 (Doc_02 SS6) - not itself a marginalized-voice "
                  "case in the Constitution's own sense, a straightforward acquisition gap in a prominent "
                  "figure.",
        cite="E", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="Not yet actively searched for a public-domain source (Source_Acquisition_Manifest.md "
                   "G4).",
        body="Direct Beza-strand and Dort-throughline claims (Doc_01 SS7), once acquired - not currently "
             "usable for any claim (Confidence E). Beza's own doctrinal-systematization role (T1's own "
             "Confidence/Gravity Cross-Check divergence, Doc_04) is currently characterized only through "
             "Calvin's own corpus and general scholarly consensus, never through Beza's own words directly.",
    ),
    dict(
        row=17, slug="dentiere-works",
        author="Marie Dentiere",
        work="the 1539 Epistre tres utile (published anonymously) and the 1561 signed preface to Calvin's "
             "sermon on women's apparel",
        edition="No edition identified or searched this pass - NOT YET ACQUIRED",
        rights=RIGHTS_NOT_YET_ACQUIRED,
        attribution="the 1539 work was published anonymously; its attribution to Marie Dentiere rests on "
                    "later scholarly identification, not the work's own title page. No specific edition "
                    "currently held or actively searched.",
        discovery="Source_Registry.md row 17, added 2026-09-15; named in the census's own `voices` field; "
                  "a genuine Article 20 marginalized-voice case (Doc_02 SS6) - the absence itself, not a "
                  "reconstruction from silence, is what this world's build currently records.",
        cite="E", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="Not yet actively searched for a public-domain source (Source_Acquisition_Manifest.md "
                   "G5).",
        body="Direct reconstruction of Dentiere's own argument, once acquired - not currently usable for "
             "any claim (Confidence E). Named here as a real, disclosed absence per Article 20's own "
             "Affirmative Duty regarding the marginalized within the community, not filled by inference or "
             "invention.",
    ),
]

KIND_BY_CONFIDENCE = {"A": "vendored", "B": "vendored", "C": "unvendored", "D": "unvendored", "E": "unvendored"}

# ------------------------------------------------------------ world_core ---
TIME_WINDOW = {"start": 1519, "end": 1650}

HORIZON = (
    "The Swiss branch of the magisterial Reformation, 1519-1650: two cities' own reforms, begun "
    "independently five years apart with no contact between their initiating figures, later bridged "
    "but never merged. Zurich's reform opens 1 January 1519, when Huldrych Zwingli, newly appointed "
    "Leutpriester at the Grossmunster, began preaching in continuous exposition through the Gospel of "
    "Matthew rather than following the fixed lectionary; it proceeds through the First and Second "
    "Zurich Disputations (1523), Zwingli's death at the Second Battle of Kappel (11 October 1531), "
    "and Heinrich Bullinger's four-decade pastorate (1531-1575). Geneva's reform opens with its own "
    "1526 alliance with Bern and 1536 break from Savoy, joined that same year by John Calvin's ministry "
    "and consolidated under the 1541 Ecclesiastical Ordinances; Zwingli and Calvin never met and their "
    "ministries did not overlap. The two cities' own traditions are formally bridged by the Consensus "
    "Tigurinus (1549), a doctrinal agreement on the Lord's Supper mediated by Bullinger's Zurich and "
    "Calvin's Geneva - evidence of a later, deliberate doctrinal bridge, not of prior contact between "
    "the two founding figures. The window's close at 1650 is the census's own administrative "
    "continues-cap for a still-living tradition (Era 7 Freeze), not a historical rupture: "
    "the Reformed pattern this world reconstructs continues unbroken past 1650 into descendant "
    "traditions this world transmits to (Doc_01 SS7), and Doc_01 itself insists this distinction not be "
    "flattened into a false ending. The Synod of Dort (1618-19) falls inside this window as a "
    "transitional development: its international Reformed dimension (the Canons, this world's own "
    "delegate participation, the Beza throughline) remains internal to this world's own transmission; "
    "the specifically Dutch domestic controversy is the actual point of hand-off, to a neighboring, "
    "differently-scoped world (Doc_01 SS7)."
)

FORMATION_LOGIC = (
    "One conviction, tested and enacted two ways. At the center: Scripture alone is sufficient to test "
    "and warrant both doctrine and civic order, and what it does not warrant no church may require "
    "(G3, Confirmed Primary, the strongest cross-strand gravity in this world's build - Doc_04 SS4). At "
    "Zurich, this conviction is enacted through public Disputation: a claim argued aloud before the "
    "whole assembled city until the council itself judges what the text has yielded, binding every "
    "priest in its territory to preach accordingly. At Geneva, the same conviction is enacted through "
    "systematic construction and catechesis: doctrine built up article by article until the whole shape "
    "of what Scripture teaches stands complete, taught to the whole population through the Catechism, "
    "and tested against ordinary conduct by the Consistory (G4, Confirmed Supporting, Geneva-scope-"
    "qualified - Doc_04 SS3.4). Two further convictions organize around this same center with equal "
    "weight: God's own sovereign election, held not as a threat but as the ground of a settled, "
    "untroubled life (G1, Confirmed Primary - Doc_04 SS3.1); and the Supper's own refusal on both "
    "fronts at once, no repeated sacrifice and no body confined to bread, Christ given truly by the "
    "Spirit's own power to whoever receives him believing (G2, Confirmed Primary - Doc_04 SS3.2). Two "
    "tensions run through this same formation without resolving inside the window: T1, Zurich's "
    "council-led civic authority against Geneva's own Consistory, fought and only by 1555 substantially "
    "won as an independent disciplinary institution - a real, permanent, within-window non-convergence, "
    "not a later-resolved disagreement (Doc_04 SS3.5); and T2, Zwingli's own 1523 'remembrance' reading "
    "of the Supper against the 1549 Consensus Tigurinus's own negotiated, fuller language - two dated, "
    "directly-quoted texts this world holds together rather than resolving in favor of either "
    "(Doc_04 SS3.5)."
)

THINNESS = (
    "Richest in confessional and doctrinal content: Calvin's Institutes and Catechism, Zwingli's own "
    "founding statements and later writings, the Consensus Tigurinus, the Second Helvetic Confession - "
    "all directly vendored and verified (Source_Registry.md rows 1-10). Thin to silent on ordinary "
    "lived practice and daily texture: no surviving account exists of what an ordinary Sunday service, "
    "a Consistory summons, or an ordinary citizen's own experience of either Reformation actually felt "
    "like (Doc_05 SS0 item 4; Doc_08 Force 2B-6; Doc_09 SS7 item 1) - a genre asymmetry between richly "
    "vendored doctrinal/confessional content and almost entirely absent daily-practice/first-person "
    "content, not a gap this build fills with invention. No Tier 2 (collected-tradition), Tier 3 "
    "(hagiographic), or Tier 4 (composite-reconstruction, held instead inside this record's own "
    "synthesis per the Framework's own instruction) story material survives or is built (Doc_09 SS3.1) - "
    "this world's own confessional core actively refuses the devotional genre hagiography belongs to "
    "(image veneration, cultic memory), and the absence is evidence the refusal worked, not a missing "
    "source (Doc_07 SS2C, SS2H). Three of this world's own most consequential documented events - the "
    "Marburg Colloquy (1529), the Bolsec controversy (1551), and the Perrinist crisis (1555) - have no "
    "vendored primary narrative source comparable to this world's own three built stories (Doc_09 SS6, "
    "SS7 item 3). Geneva's own specific institutional detail (the Consistory's weekly case-by-case "
    "discipline, the census's own named selection rationale for this world) rests on Confidence D/E, "
    "unacquired evidence (Source_Registry.md row 13) - the general doctrine is Documented, but the vivid, "
    "formation-defining detail this world was selected for is not currently sourceable (Doc_04 SS3.4)."
)

CAUTIONS = (
    "Single-author concentration is real and disclosed at every load-bearing point: Calvin's own corpus "
    "runs roughly four times Zwingli's in this world's vendored base (Force 2B-6, Doc_08), and the "
    "Confidence/Gravity Cross-Check on G1 finds the core doctrine Documented cross-strand while its "
    "fully systematized, later double-predestination form is substantially Calvin/Beza-concentrated "
    "(Doc_04 SS3.1) - not smoothed into an undifferentiated 'both cities teach this equally' claim. "
    "The CT-tagged contested term (Sign and the Thing Signified, rzglex008) rests on no vendored "
    "secondary scholarship on the Consensus Tigurinus specifically - its own contest characterization "
    "draws on the builder's own general knowledge of Reformation historiography, disclosed as such "
    "rather than presented as text-grounded (Doc_03 SS4). T2's own characterization of whether the 1549 "
    "Consensus 'softens' or merely restates Zwingli's 1523 language in fuller form is this build's own "
    "interpretive judgment, not an inherited scholarly finding (Doc_04 SS3.5). Five Native sources "
    "remain unacquired (Source_Registry.md rows 13-17: the Ecclesiastical Ordinances, the Genevan "
    "Psalter, Geneva's own consistory registers, Beza's own works, Marie Dentiere's own works) - none of "
    "this world's own current claims treats any of them as load-bearing (Source_Registry.md's own "
    "priority-review trigger note), but a future revision drawing on any of them should re-check claims "
    "this record currently states at Confidence D/E rather than assume they hold unchanged."
)

THIN_TOPICS = [
    {
        "keywords": ["ordinary", "daily", "Sunday", "lived practice", "consistory summons", "ordinary citizen"],
        "note": "No surviving account of ordinary daily/lay religious practice at either city - the genre "
                "asymmetry Doc_05 SS0 item 4 and Doc_09 SS7 item 1 both name; doctrine and confession are "
                "richly vendored, daily texture is almost entirely absent.",
    },
    {
        "keywords": ["hagiography", "saint", "martyr", "veneration", "cultic memory"],
        "note": "No Tier 3 hagiographic material exists, and none is built to fill the absence - this "
                "world's own confessional core actively refuses the devotional genre from its own "
                "founding statement onward (Doc_05 SS6.2; Doc_07 SS2C, SS2H). The absence is evidence "
                "the refusal worked, not a missing source.",
    },
    {
        "keywords": ["consistory case", "discipline record", "excommunication case", "weekly session"],
        "note": "Geneva's own consistory registers (Source_Registry.md row 13) remain unvendored - "
                "confirmed copyrighted in the one identified edition. This world's own single largest "
                "disclosed source-ecology gap: the census's own named archive and selection rationale "
                "for this world is currently unusable at Confidence D.",
    },
    {
        "keywords": ["Marburg", "Bolsec", "Perrinist", "Perrin"],
        "note": "Three of this world's own most consequential documented events have no vendored primary "
                "narrative source comparable to this world's own three built stories - all three are "
                "Documented as historical fact and function as forces/gravity-tests, but none has a "
                "narrative account meeting this world's own Tier 1 bar (Doc_09 SS6, SS7 item 3).",
    },
    {
        "keywords": ["Beza", "Dentiere", "Ecclesiastical Ordinances", "Genevan Psalter"],
        "note": "Four Native sources named in the census's own `voices`/`sources` fields remain "
                "unacquired (Source_Registry.md rows 14-17) - Beza and Dentiere's own words, the actual "
                "text of the 1541 Ordinances, and the Genevan Psalter's own text. Dentiere's absence is a "
                "genuine Article 20 marginalized-voice case, not merely an acquisition gap (Doc_02 SS6).",
    },
]

WORLD_CORE_SOURCES = [
    {"source_id": f"rzg.source.{slug}", "locus": "whole work, per this record's own body", "license": "see body"}
    for slug in (
        "calvin-institutes-book1", "calvin-institutes-books2-3", "calvin-institutes-book4",
        "calvin-geneva-catechism", "consensus-tigurinus", "zwingli-sixty-seven-articles",
        "zwingli-selected-works", "second-helvetic-confession",
    )
]

WORLD_CORE_BODY = """Grounded in Doc_01 through the World Profile and rzg_World_Capsule_Core.md (all
Approved to proceed), following don.core.donatism.md's own established compile pattern: `horizon`,
`formation_logic`, `thinness`, and `cautions` are this compilation's own third-person, citation-grounded
synthesis of those documents, not a verbatim carry of the Capsule Core's own second-person immersive
prose (that prose is deployment-facing and lives in its own file; world_core's fields are not scanned
by gate_voice_perspective, matching don's own precedent, confirmed directly against engine/m1/gates.py
this session).

AUTHORED, not mechanical: which specific gravity/force/document citations to attach to each field's own
claims (this compilation's own judgment, cross-checked against Doc_04's own confirmed classification
table and Doc_08's own force index before writing); the choice to state T1/T2's own non-resolution
plainly in `formation_logic` rather than folding them into a single flattened account (Doc_04 SS3.5's
own explicit instruction that both are Tensional precisely because they name real, persistent
divergence).

WORLD_ID: `the-reformed-cities-zurich-and-geneva`. This world has no entry in records/worlds/ yet -
registry addition is a later admission-track step, out of scope for this first record-authoring pass.
"""


# ------------------------------------------------------------------ emit ---
def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


def emit_source(r: dict) -> Path:
    rid = f"rzg.source.{r['slug']}"
    conf = {
        "citation_specificity": r["cite"],
        "verification_state": r["verif"],
        "evidentiary_weight": r["weight"],
        "formation_confidence": r["formation"],
        "divergence_note": r.get("divergence"),
    }
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "source",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": [],
        "confidence": conf,
        "sources": [],
        "relations": [],
        "author": r["author"],
        "work": r["work"],
        "edition": r["edition"],
        "rights_status": r["rights"],
        "attribution_status": r["attribution"],
        "discovery_channel": r["discovery"],
        "external_ids": {"rzg_source_registry_row": r["row"]},
        "kind": KIND_BY_CONFIDENCE[r["cite"]],
    }
    path = OUT_ROOT / "source" / f"{rid}.md"
    _write(path, payload, r["body"])
    return path


def emit_world_core() -> Path:
    rid = "rzg.core.the-reformed-cities-zurich-and-geneva"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Dominant Modern Reconstruction",
            "divergence_note": (
                "This record synthesises Doc_01 through the World Profile and rzg_World_Capsule_Core.md "
                "rather than reading a text directly, so verification runs via those documents' own "
                "authority, not via a primary source reopened here. Doc_01 SS4's own close-call finding "
                "(one world, two strands, confirmed by the project lead 2026-09-15 rather than "
                "self-resolved) is this world's own most consequential synthetic judgment, carried into "
                "`formation_logic` above as settled rather than reargued."
            ),
        },
        "sources": WORLD_CORE_SOURCES,
        "relations": [],
        "time_window": TIME_WINDOW,
        "horizon": HORIZON,
        "formation_logic": FORMATION_LOGIC,
        "thinness": THINNESS,
        "cautions": CAUTIONS,
        "thin_topics": THIN_TOPICS,
    }
    path = OUT_ROOT / "world_core" / f"{rid}.md"
    _write(path, payload, WORLD_CORE_BODY)
    return path


def main() -> int:
    slugs = [r["slug"] for r in ROWS]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    rows = [r["row"] for r in ROWS]
    assert rows == sorted(rows), "rows out of order"
    assert len(ROWS) == 17, f"expected 17 Native rows, got {len(ROWS)}"

    written = [emit_source(r) for r in ROWS]
    written.append(emit_world_core())
    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} records written ({len(ROWS)} source + 1 world_core); all 17 Registry rows "
          f"emitted (none Excluded).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
