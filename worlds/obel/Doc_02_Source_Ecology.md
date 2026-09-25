# Doc_02 — Source Ecology

**World: The Old Believers** (`the-old-believers`, file-code `obel`)

**Status: Draft, Round 2 — pending re-review.**

**Built together with:** `obel_Source_Registry.md` (the Registry — the
same pass, per the Source Registry Template V1.0's own instruction not to
build these as two separate steps).

**Built from:** `Doc_01_World_Identification_Boundaries_Orientation.md`;
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_
Dossier.md`; `cic/corpus-map/the-old-believers.yaml`; the
`python -m engine.m9.cli holdings obel` report; `python
cic/engine/corpus_index.py --entry the-old-believers` searches;
`reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`; and
this world's own two vendored files, read in full.

---

## 0. The library as it actually stands

**This is this project's first Slavic/Russian-Orthodox-schism world.**
Before this pass, nothing was vendored for it. This session vendored two
files, both bearing on the same single work — Avvakum's autobiography —
in two languages:

1. `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` — the
   1924 Hogarth Press first English translation (Jane Harrison & Hope
   Mirrlees, preface D. S. Mirsky). Runs to at least p. 156. Verbatim-ready.
2. `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
   — the same work, in a modernized Russian reading edition (§7).
   Second-witness-only.

This is a genuinely thin library — one work, two witnesses to it. §6
names, at length, what it cannot yet settle.

---

## 1. Primary Voices

### 1.1 Avvakum Petrov (Archpriest Avvakum, c. 1620/21-1682) — the
movement's central and, in this library, only inside voice

Avvakum is present in exactly one work, in two language witnesses: his
own autobiography (*Zhitie*, "Life"), written c. 1673 at Pustozersk. This
is a first-person narrative covering his own ministry, his exile to
Siberia (1653-1664) under voevoda Afanasy Pashkov, his return to Moscow,
his final imprisonment, and — within the narrative itself — his own
direct argument over the wording of the Nicene Creed's own eighth
article (p. 34) and his own direct account of disputing the corrected
rite before the Eastern patriarchs at the Chudov Monastery (pp. 120-121)
— both quoted in full at Doc_01 §9.

**Own-voice flag: whole work is Avvakum's own first-person voice, with
one genuine internal contradiction between the two vendored witnesses
about a single passage's own authorship:**

- The English edition's own footnote at p. 33, attached to the opening
  dedication, reads: "In the original manuscript this is in the writing
  of Epiphanius" — read on its own, this suggests the dedication was
  physically penned by Avvakum's confessor Epiphanius.
- The Russian witness, at the equivalent point, has Avvakum say the
  opposite about the same sentence: "По благословению отца моего старца
  Епифания **писано моею рукою грешною** протопопа Аввакума" — "by the
  blessing of my father the elder Epiphanius, **written by my own sinful
  hand**, [I,] the archpriest Avvakum."

The two witnesses disagree with each other about who held the pen for
this passage. This is very likely a signature of a genuine redaction
difference between the manuscript traditions the two editions descend
from (§7 — this document does not yet know which redaction of the
*Zhitie* either witness represents, which is itself a real gap), not a
simple error in either one. It is recorded here as an open, disclosed
contradiction, not resolved by preferring either witness.

The vendored English edition's own apparatus also carries at least one
internal error, disclosed rather than silently relied upon: its own
Chronological Table gives Avvakum's execution as "1681, April," while
the census's own `documentedStories` text and the secondary literature
agree on 14 April 1682 (Doc_01 §1 uses 1682, the correct date). This
document does not know why the vendored edition's own table carries the
earlier year, and flags it as a caution about this edition's own
apparatus rather than about the historical date, which is not in serious
doubt.

**Quotable passages, exact loci** (English file; page numbers established
from this file's own pagination convention: printed at the **foot** of
each page, immediately followed by the **next** page's own running head,
confirmed independently at two separate page breaks in this file):

| Passage | Locus | Quotability | Own-voice/opponent-voice |
|---|---|---|---|
| The Creed-wording dispute: "It were better in the Creed not to pronounce the word Lord... for in that name is contained the essence of God" | p. 34 | Verbatim-ready | Own-voice |
| Opening dedication: "Avvakum, archpriest, was bidden by the monk Epiphanius... to write down my life" | p. 33 | Verbatim-ready | Own-voice, with the authorship contradiction above disclosed |
| The Markovna passage: "How long, archpriest, are these sufferings to last?" / "Markovna! till our death" | p. 80 | Verbatim-ready | Own-voice (both Avvakum's own narration and his wife Anastasia Markovna's quoted speech, as reported by Avvakum) |
| The Chudov Monastery dialogue (two/three fingers; "Nikon, the wolf, together with the devil...") | pp. 120-121 (the patriarchs' own question spans both pages, Avvakum's own reply is entirely on p. 121) | Verbatim-ready | Mixed in one passage: the patriarchs' own words are quoted by Avvakum as opponent-voice, directly followed by his own reply as own-voice — do not attribute the patriarchs' words to Avvakum or vice versa |
| Closing devotional passage ("...When we die, then shall this be read...") | p. 156 (the passage falls after the printed "155" marker and a fresh running head; p. 155 is not the file's own last page) | Verbatim-ready | Own-voice |

**Quotable passage, exact locus** (Russian original file — no internal
page numbers; located by exact string search against the vendored file):

| Passage | Locus | Quotability | Own-voice/opponent-voice |
|---|---|---|---|
| The Creed-wording dispute (Russian text of the p.34 passage above) | Located by direct string search, verified exact | Second-witness-only (§7) | Own-voice |
| Opening declaration on plain speech vs. "philosophical verses" | First paragraph of the vendored file, verified exact | Second-witness-only (§7); not usable as free-standing evidence — see Doc_01 §4 and §7 below for how this document uses it | Own-voice |
| The authority list for the two-fingered sign ("Мелетия антиохийскаго и Феодора Блаженнаго...") | Located by direct string search, verified exact | Second-witness-only (§7) | Own-voice |

**Author Gravity Assessment, preliminary — Doc_04's own work is
authoritative:**

- **Transmission history:** the English translation (1924) is one
  specific editorial choice, not this world's only possible primary
  text — the census's own `sources[]` field names two different modern
  scholarly translations of this same work (Brostrom, 1979; Gluck &
  Brostrom, 2021) that this world's library does not hold, because they
  are not public domain (§7). The original-language witness is an
  undated, modernized reading edition of uncertain critical lineage,
  carrying its own editor's interpolated glosses (§7). **This world's
  whole evidentiary base currently rests on a transmission chain with
  real, disclosed weak links at both ends**, not a clean, single-hop
  primary artifact.
- **What becomes over-visible because this source survives:** Avvakum's
  own voice, his own sufferings, and his own theological framing of the
  dispute dominate this world's current evidentiary base totally, because
  it is the only inside voice this library holds.
- **What becomes under-visible:** every other voice in this world —
  Nikon's own reasoning; the Solovetsky petitioners' own case in their own
  words; the priestless/bezpopovtsy theological argument in its own
  mature form (Pomorian Answers); any woman's own words in her own voice
  (Boyarynia Morozova is named in the census but no primary text of hers,
  or about her in period language, is vendored); Evfrosin's internal
  dissent against self-immolation, in his own words. **This is a severe
  single-source asymmetry** (§11).

### 1.2 Opponent voices — present only inside Avvakum's own quotation

The Eastern patriarchs and Nikon himself are not vendored as independent
voices. The only words attributed to them in this library are Avvakum's
own quotations of them (pp. 120-121) — reported opponent-speech, inside
an own-voice narrative, never a source in its own right. Any future
document quoting "what the patriarchs said" must attribute it as
Avvakum's own report of their words.

### 1.3 Lay and non-founder voices

None vendored. Boyarynia Feodosia Morozova (named in the census as
numerically central to the priestless communities' own memory) has no
primary text in this library (§10).

---

## 2. Secondary Voices

Two works are cited, at the confidence they actually support (named in
the census, not independently re-checked this session), and are not
vendored (secondary scholarship is not vendored into `cic/texts/`, per
project convention — Registry R3, R4):

- Robert O. Crummey, *The Old Believers and the World of Antichrist*
  (1970/2011) — the Vyg community and the Russian state.
- Georg B. Michels, *At War with the Church* (1999) — reconstructs the
  early schism from the state's own archives, specifically noted (census)
  as complicating the movement's own self-narrative of early coherence: a
  methodological check for Doc_05/Doc_07 not to read Avvakum's own
  account, or any Old Believer martyrology, as an uncontested historical
  record without Michels's own corrective in view.

A reference-level work (*Cambridge History of Christianity* vol. 5, the
Dixon chapter) is cited at low confidence (Registry R5) with its own
chapter-numbering inconsistency disclosed rather than resolved.

The *Pomorskie otvety* (Pomorian Answers, 1723) are, per the standard
literature, primarily authored by **Andrei Denisov** (1664-1730), the
Vyg community's own leader, with Trifon Petrov and Semyon Denisov (his
younger brother) as participants. Semyon Denisov's own independent works
are the *Istoriia ob ottsakh i stradal'tsakh solovetskikh* and the
*Vinograd rossiiskii* (Registry R8).

---

## 3. Author Gravity — cross-check against corpus-map

`cic/corpus-map/the-old-believers.yaml` (generated this session,
`corpus_map_merge.py --write-only avvakum`, `--check` clean) carries two
rows, both `role: tradition`, `confidence: assigned`, for the two
vendored files. Both rows carry `source_file`, `role`, and `confidence`
per the corpus-map schema as `corpus_map_merge.py` actually emits it
today (its own `_KEEP` tuple: `work, author, source_file, locus, role,
confidence, note`).

Own-voice/opponent-voice discipline is demonstrated directly in this
document's own prose (§1.1's table), not in the corpus-map YAML's own row
fields: `row_id` and `voice_of` are real, named, in-progress schema
fields (per `cic/corpus-map/fixture-synthetic.yaml`'s own header,
"CM-1/CM-2/CM-4/CM-8") that no real world's own bucket carries yet,
proven so far only against synthetic fixture data by a separate
corpus-map thread. This is a fleet-wide tooling state, not specific to
this world, logged at `Open_Gaps_Tracking.md` entry 9.

---

## 4. Institutional Evidence

None vendored. The 1666-1667 Moscow council's own acts and anathemas, and
the state's own 1685 persecution decrees, are named in the census but not
independently verified against a primary source this pass.

---

## 5. Holdings disposition

`python -m engine.m9.cli holdings obel` was run this session. Result: 140
vendored files fleet-wide, of which this world's own two new files both
show `no coverage entry`: they are not yet in the hand-maintained
COVERAGE table `engine/m1/cross_world.py` reads from, a real, separate,
pre-existing table this world was never added to (it predates this
world's own corpus-map bucket). Whether that omission should be treated
as a defect to fix now or a gap to log and defer is a judgment call
logged at `Open_Gaps_Tracking.md` for the coach thread or whoever owns
that table to resolve, since the module's own disclosed practice
elsewhere in the fleet treats a missing COVERAGE key as a defect to be
corrected rather than an accepted gap.

For the record, the arithmetic itself is correct: 140 vendored files =
102 `.txt` + 38 `.xml`; 2 (`by design`) + 93 (`out of window`) + 45 (`no
coverage entry`) = 140.

---

## 6. Thin-evidence map

| Question | Evidence in this library | Confidence |
|---|---|---|
| Why did the schism happen? (Nikon's corrections; the anathema) | Avvakum's own narrative frames this but does not narrate the council itself | Widely Accepted (secondary-corroborated, not primary-verified) |
| Did the dispute reach the Creed's own wording, not only ritual practice? | Avvakum's own p. 34 argument, directly evidenced | Documented (§1.1; Doc_01 §9) |
| Was self-immolation the movement's own uncontested practice? | Avvakum's own approving epistles are named (census) but not vendored; Evfrosin's dissenting tract is named but not vendored | Contested — genuinely thin, both sides of the internal argument currently un-vendored |
| What was daily communal/liturgical life actually like in a priestless community? | Nothing vendored | Inferential-Thin |
| Women's own voice/experience | Nothing vendored (Morozova named, not sourced) | Inferential-Thin |
| The Solovetsky monks' own self-understanding, in their own words | Not vendored | Inferential-Thin |
| The mature priestless (bezpopovtsy) theological argument | Pomorian Answers named, not vendored | Inferential-Thin |
| Who physically wrote the Life's own opening dedication? | The two vendored witnesses disagree with each other (§1.1) | Contested |

---

## 7. Edition and original-language notes

The vendored English file is rights-clean and identified as a specific
1924 printing — but that is traceable to a first *printing*, not
necessarily to a *text*: the 1924 translators' own Russian source
manuscript is nowhere named, and §1.1 shows the translation demonstrably
omits real material (the plain-speech apologia; Doc_01 §4).

**Edition substitution, disclosed:** `cic-website/data/world-census.json`'s
own `sources[]` field names this world's primary Avvakum editions as
Kenneth Brostrom's 1979 translation (Michigan Slavic) and the Gluck &
Brostrom 2021 translation (Columbia Russian Library) — modern scholarly
translations, neither public domain and neither vendored here. The
vendored 1924 Hogarth Press text is a substitute, chosen because it is
public domain, not because it is the census's own first-choice edition.

**Redaction identity, unresolved and named as a real gap:** the *Zhitie*
survives in several redactions, and §1.1's own authorship contradiction
between the two vendored witnesses (who held the pen for the opening
dedication) is exactly the kind of divergence a redaction difference
produces. Neither the English nor the Russian vendored file states which
redaction it represents — an open bibliographic question for a future
pass, not a settled detail.

**The original-language file's own real character:**

- The vendored file contains roughly **ninety** bracketed modern-Russian
  editorial glosses interpolated directly into Avvakum's own running
  sentences (e.g. `[правое]`, `[потому что]`, `[так]`, `[чаша, кубок]`) —
  a modern annotated reading edition's own apparatus, not Avvakum's
  words. **Any future quotation from this file must strip these
  bracketed glosses before quoting**; failing to do so quotes a modern
  editor's gloss as Avvakum's own sentence.
- The file is in modernized Russian orthography (no final ъ, no ѣ,
  normalized endings) — an annotated modern reading edition of a
  seventeenth-century text, not an Old East Slavic diplomatic
  transcription. The ISO 639-3 tag `orv` used in this file's own name and
  elsewhere in this world's package is loose at best for what the file
  actually is (see `Open_Gaps_Tracking.md` for the disclosed naming
  exception — not renamed this pass, since a rename touches every
  reference to it).
- Its own transcription chain (manuscript → critical edition → az.lib.ru
  → this Wikisource copy) remains unverified hop-by-hop.

**How this document uses the two witnesses:** the English 1924
translation is this world's evidentiary text, chosen for its clean,
single-hop public-domain status, with the substitution above disclosed.
The Russian text is a second witness only, per INTAKE.md's own real rule
(2026-09-02: an original-language text is never itself primary
evidence) — used here to identify what the English translation omits
(Doc_01 §4's edition-comparison finding), never as a free-standing
source for a claim the English cannot also support.

---

## 8. Cross-world overlaps and pairs

`cappadocian-nicene-pastoral-monastic-tradition` is the one other Built
& Live world in this fleet's "Greek East & Orthodoxy" lane. Fourth-
century Cappadocia's own Trinitarian-doctrinal formation register, its
different century, empire, and language, and the absence of any figure,
text, or controversy shared with this world together support no genuine
cross-world overlap. `cic/corpus-map/PAIRS.yaml` was not modified this
pass; no pairing candidate was identified with any other world's own
corpus, built or candidate.

---

## 9. Material and archaeological sources

Not consulted this pass. The census's own `legacy` field (icon-painting
styles, znamenny chant, manuscript practices preserved in Old Believer
communities) is the only lead on record, not independently verified
against a material-culture source.

---

## 10. Missing Voices Assessment (Constitution Article 20)

- **Women.** Boyarynia Feodosia Morozova is named repeatedly (census; the
  documented-stories record) as numerically central to the priestless
  communities' own memory, and as a specific, named martyr (starved to
  death, 1675) — no primary text by her or about her in period language
  is vendored. A verified acquisition lead exists (the Tale of Boyarynya
  Morozova, 17th-century, public domain by date) but was not
  successfully downloaded this session (a Wikimedia Commons fetch
  returned HTTP 429, a rate-limit, not a rights or existence problem) —
  a live lead, not closed.
- **Ordinary believers, priestless communities' own daily life.** Nothing
  vendored (§6).
- **The movement's own internal dissent (Evfrosin against
  self-immolation).** Named, not vendored (§1.1, §6; Registry R9,
  flagged for priority acquisition).

---

## 11. Source Asymmetry Assessment

This world's current library is a maximal case of founder/single-voice
asymmetry: one man's own autobiography, in two language witnesses of the
same work, is the entire primary-source base. Any claim about "the
movement's" own experience, belief, or practice beyond what Avvakum's own
text can settle should be treated as Contested or Inferential-Thin until
this library grows, regardless of how confidently the census or secondary
scholarship states it.

---

## 12. Forces Lens Applied to Source Ecology (Forces Framework V1.1 §4,
Step 2)

Preliminary. The initiating force (refusal of liturgical and textual
correction, Doc_01 §7) is directly evidenced in Avvakum's own words at
both p. 34 and pp. 120-121; the ongoing force (suffering/testimony under
persecution) is directly evidenced; the contested ending-force candidate
(self-immolation as final refusal) is currently evidenced only by the
census's own secondary characterization, not by either side's own
primary voice in this library — a caution for Doc_08's own six-cell
matrix.

---

## 13. Confidence Calibration and Propagation

Every confidence tag used in Doc_01 and this document follows the
project's five-level `formation_confidence` vocabulary. Claims resting
only on the census itself, with no primary source consulted, are tagged
Widely Accepted rather than Documented — a project-internal record is
not itself a primary source. Death-toll figures for self-immolation
incidents remain Contested. The p. 34 Creed-wording dispute is tagged
Documented (§1.1, §6), directly verified.

---

## 14. Disposition of Doc_01's open items

Doc_01 §10 names seven open items. This document does not resolve any of
them but confirms each is correctly carried to `Open_Gaps_Tracking.md`.

---

## 15. Open items from this revision

`Open_Gaps_Tracking.md` carries the full, current, append-only record of
every open question this world's build has raised, including this
revision's own findings.

---

## 16. Escalation check

Two matters raised by this world's own construction meet the
governance/methodology escalation category and are not
self-dispositioned by this build thread: a fabricated citation to a
nonexistent INTAKE.md ruling, found to have propagated into `cic/texts/
REGISTRY.yaml` and `cic/corpus-map/` outside this world's own folder
before being caught; and three canonical documents having been built
citing a specification (V1.8) not present in this checkout. Both go to
Mark directly. The census's own `floorNote`/`statusDescription`, which
carry an overstated absolute floor claim this world's own vendored
source contradicts, are cited approvingly at a Frozen portfolio gate;
correcting the census itself is portfolio-level and also goes to Mark.
Correcting this world's own documents, which this revision does, is
within this thread's own authority.

---

## 17. Document log

- **Round 1 draft**, 2026-09-25, this build thread, together with
  `obel_Source_Registry.md`.
- **Round 1 self-review**, 2026-09-25, applied directly before
  independent review landed.
- **Round 1 independent review** (`obel_Step0_Doc01_Doc02_Review_
  Round1.md`, plus its own reconciliation addendum): **substantial
  revision required.** Findings against this document: 6, 7, 8 (three of
  four quotable-passage loci wrong, from a page-numbering method that
  was backward), 9 (a false claim that no Orthodox-lane world is built),
  11 (a misattributed primary text, via the Registry), 12 (systematically
  misapplied Registry confidence tiers), 13 (an undisclosed quotation
  hazard — ~90 editorial glosses in the Russian file), 15 (an overstated
  edition-provenance claim and an undisclosed edition substitution), 16
  (an uncaught error in the vendored edition's own apparatus), 17 (a
  contradiction between the two vendored witnesses, read but not
  cross-checked), 20 (blocking — citing V1.8, a specification not
  present in this checkout), 24 (a docstring citation that said the
  opposite of what the actual module says), 25 (partial delivery against
  V1.8's own stated requirements), plus shared findings 1 (blocking — the
  floor claim), 2/3 (blocking — the fabricated INTAKE.md citation), and
  29 (process narration embedded in canonical text).
- **Round 2 revision**, 2026-09-25, this build thread. Every finding
  fixed: the p. 34 Creed-wording passage is added as a quotable, directly
  evidenced passage; all four loci are corrected against the file's own
  real pagination convention; the Pomorian Answers' authorship is
  corrected to Andrei Denisov; the Registry's confidence tiers are
  corrected per the Source Registry Template's own definitions; the
  bracket-gloss hazard and the loose `orv` tag are disclosed in full; the
  edition substitution against the census's own preferred modern
  translations is disclosed; the vendored edition's execution-date error
  and the two witnesses' authorship contradiction are both disclosed as
  open findings rather than silently resolved; the holdings-disposition
  section's docstring citation is corrected to what the module actually
  says, and the finding it was dismissing is left open rather than
  re-dismissed on a different unverifiable authority; the fabricated
  INTAKE.md citation is removed from this document (and from `cic/
  texts/REGISTRY.yaml` and `cic/corpus-map/`, outside this world's own
  folder); and citations are re-grounded on V1.5, the specification
  actually present in this checkout. Process narration and a full
  self-assessment section are removed from the body text; this log
  entry, together with `Open_Gaps_Tracking.md`, is where that history now
  lives.
