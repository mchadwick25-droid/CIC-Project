# Doc_02 — Source Ecology

**World: The Old Believers** (`the-old-believers`, file-code `obel`)

**Status: Approved to proceed.** One named item waits — §15.

**Built together with:** `Source_Registry.md` (the Registry), built in
one pass with this document, per the Source Registry Template V1.0's own
instruction not to build these as two separate steps.

**Built from:** `Doc_01_World_Identification_Boundaries_Orientation.md`;
`Build/worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`;
`cic/corpus-map/the-old-believers.yaml`; the holdings figures at §5 below,
from `python -m engine.m9.cli holdings obel`; `python
cic/engine/corpus_index.py --build` followed by `python
cic/engine/corpus_index.py "<query>" --entry the-old-believers` searches;
`Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`;
`cic/texts/INTAKE.md`'s rule on original-language primary evidence; and
this world's own two vendored files, read in full.

---

## 0. The library as it actually stands

**This is this project's first Slavic/Russian-Orthodox-schism world.**
Two files are vendored for it, both bearing on the same single work —
Avvakum's autobiography — in two languages:

1. `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` — the
   1924 Hogarth Press first English translation (Jane Harrison & Hope
   Mirrlees, preface D. S. Mirsky). Runs to at least p. 156. Verbatim-ready.
2. `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
   — the same work, in a modernized Russian reading edition (§7).
   Primary evidence in its own right, per INTAKE.md's rule; two
   quotability caveats independent of language remain (§7).

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
  Епифания **писано моею рукою грешною** протопопа Аввакума" — in
  English, by the blessing of my father the elder Epiphanius, written by
  my own sinful hand, [I,] the archpriest Avvakum.

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
| The Creed-wording dispute: Avvakum says it would be better not to pronounce the word Lord than to cut out the word True, for in that name is contained the essence of God (quoted at Doc_01 §9) | p. 34 | Verbatim-ready | Own-voice |
| Opening dedication: "Avvakum, archpriest, was bidden by the monk Epiphanius... to write down my life" | p. 33 | Verbatim-ready | Own-voice, with the authorship contradiction above disclosed |
| The Markovna passage: "How long, archpriest, are these sufferings to last?" / "Markovna! till our death" | p. 80 | Verbatim-ready | Own-voice (both Avvakum's own narration and his wife Anastasia Markovna's quoted speech, as reported by Avvakum) |
| The Chudov Monastery dialogue (two/three fingers; "Nikon, the wolf, together with the devil...") | pp. 120-121 (the patriarchs' own question spans both pages, Avvakum's own reply is entirely on p. 121) | Verbatim-ready | Mixed in one passage: the patriarchs' own words are quoted by Avvakum as opponent-voice, directly followed by his own reply as own-voice — do not attribute the patriarchs' words to Avvakum or vice versa |
| Closing devotional passage ("...When we die, then shall this be read...") | p. 156 (the passage falls after the printed "155" marker and a fresh running head; p. 155 is not the file's own last page) | Verbatim-ready | Own-voice |

**Quotable passage, exact locus** (Russian original file — no internal
page numbers; located by exact string search against the vendored file):

| Passage | Locus | Quotability | Own-voice/opponent-voice |
|---|---|---|---|
| The Creed-wording dispute (Russian text of the p.34 passage above) | Located by direct string search, verified exact | Verbatim-ready — primary evidence, cross-corroborated by the English witness (§7) | Own-voice |
| Opening declaration on plain speech vs. "philosophical verses" | First paragraph of the vendored file, verified exact | Verbatim-ready — primary evidence in its own right, clean of the file's own bracketed glosses at this specific locus (§7; Doc_01 §4) | Own-voice |
| The authority list for the two-fingered sign ("Мелетия антиохийскаго и Феодора Блаженнаго...") | Located by direct string search, verified exact | Verbatim-ready — primary evidence, cross-corroborated by the English witness (§7) | Own-voice |

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
the census, not independently re-checked at this stage), and are not
vendored (secondary scholarship is not vendored into `cic/texts/`, per
project convention — Registry rows 3 and 4):

- Robert O. Crummey, *The Old Believers and the World of Antichrist*
  (1970/2011) — the Vyg community and the Russian state.
- Georg B. Michels, *At War with the Church* (1999) — reconstructs the
  early schism from the state's own archives, specifically noted (census)
  as complicating the movement's own self-narrative of early coherence: a
  methodological check for Doc_05/Doc_07 not to read Avvakum's own
  account, or any Old Believer martyrology, as an uncontested historical
  record without Michels's own corrective in view.

A reference-level work (*Cambridge History of Christianity* vol. 5, the
Dixon chapter) is cited at low confidence (Registry row 5) with its own
chapter-numbering inconsistency disclosed rather than resolved.

The *Pomorskie otvety* (Pomorian Answers, 1723) are, per the standard
literature, primarily authored by **Andrei Denisov** (1664-1730), the
Vyg community's own leader, with Trifon Petrov and Semyon Denisov (his
younger brother) as participants. Semyon Denisov's own independent works
are the *Istoriia ob ottsakh i stradal'tsakh solovetskikh* and the
*Vinograd rossiiskii* (Registry rows 8 and 12).

---

## 3. Author Gravity — cross-check against corpus-map

`cic/corpus-map/the-old-believers.yaml` (generated by
`corpus_map_merge.py` from the two staging files; `--check` is valid)
carries two rows, both `role: tradition`, `confidence: assigned`, for the
two vendored files. Each row carries `row_id`, `source_file`, `role` and
`confidence`, per the corpus-map schema as `corpus_map_merge.py` emits it.
The Library issued the `row_id` values with `--assign-ids`.

Own-voice/opponent-voice discipline is demonstrated directly in this
document's own prose (§1.1's table and §1.2), not in the corpus-map
rows: `voice_of` is a named schema field for a file that mixes voices,
and neither row sets it. The English edition carries the patriarchs'
reported speech inside Avvakum's own narrative (pp. 120-121), and §1.2
and the quotation paragraphs of Doc_01 §9 name the speaker. The state of
the `voice_of` field across the fleet is logged at `Open_Gaps_Tracking.md`
(the `row_id` and `voice_of` entry).

---

## 4. Institutional Evidence

None vendored. The 1666-1667 Moscow council's own acts and anathemas, and
the state's own 1685 persecution decrees, are named in the census but not
independently verified against a primary source at this stage.

---

## 5. Holdings disposition

`python -m engine.m9.cli holdings obel` runs against the whole vendored
library. It reports 433 vendored files, counted two ways: `ls cic/texts`
filtered to `.txt` and `.xml` gives 395 `.txt` files and 38 `.xml` files,
and `find cic/texts -maxdepth 1` filtered to the same extensions gives
433. The report's dispositions are 2 `by design`, 145 `out of window` and
286 `no coverage entry`, and 2 + 145 + 286 = 433. This world's own two
files both show `no coverage entry`: they are not in the hand-maintained
COVERAGE table that `engine/m1/cross_world.py` reads. Whether to add them
is a judgment for whoever owns that table, logged at
`Open_Gaps_Tracking.md`. The report marks no file `in scope, unread`, so
no other vendored file needs a disposition here.

Corpus figures for this world's two files, counted two ways. The English
file holds 36,763 words by `wc -w` under the `POSIX` locale and 36,938
under `C.UTF-8`; splitting the text on whitespace in Python 3 gives
36,938. The Russian file holds 5,330 words by `wc -w` under `POSIX`, which
miscounts Cyrillic, and 20,660 under `C.UTF-8` and in Python 3. Both
counts include each file's provenance header. The Russian file's 116
bracketed glosses are counted by a Python 3 regular expression and by
`grep -o` on the body (below the header) under both locales; the whole
file, header included, shows 118.

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

**Transcription convention, stated once for every quotation drawn from
either vendored witness in this world's documents:** the English 1924
printing's OCR carries stray hyphens at line-wraps, `zs` for `is` in at
least one place, stray marks and page-break running heads inside
sentences, and British punctuation printed outside the closing quotation
mark. A quotation changes no word of the file. Where a stray mark or a
page break falls inside a quoted sentence, the quotation is given in
segments joined by an ellipsis, or a garbled word is supplied in square
brackets. The Russian Wikisource transcription's own bracketed editorial
variant readings (distinct from the modern-editorial glosses below) are
carried through exactly as the file prints them wherever a quotation does
not need to cross one. This convention governs every quotation in this
document, Doc_01, Step 0 and the Source Registry; it is not restated at
each one.

**The original-language file's own real character:**

- The vendored file contains **116** bracketed modern-Russian
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
  exception — not renamed, since a rename touches every
  reference to it).
- Its own transcription chain (manuscript → critical edition → az.lib.ru
  → this Wikisource copy) remains unverified hop-by-hop.

**How this document uses the two witnesses:** per INTAKE.md's current
rule, language does not decide whether a source is primary; credibility
and truth do. Both vendored witnesses are this world's own primary
evidence. In practice, this world
treats the English 1924 translation as the more fully verified working
text (its own transcription lineage is traced to a specific, dated,
rights-clean first printing) and the Russian text as equally primary in
principle but currently constrained by two real, disclosed quotability
caveats independent of language: its own transcription chain is
unverified hop-by-hop, and it carries the bracketed editorial glosses
above, which must be stripped from any passage that contains them before
quoting. Where a specific Russian passage is clean of those caveats (no
glosses, and cross-corroborated by the English witness or otherwise
independently checked), it is directly quotable in its own right, as at
Doc_01 §4 and §9. A quote record built from this world's own library
should hold the original-language text as the quoted material, per the
rule's own instruction, with a public-domain English rendering
(where the translation actually carries the same passage) as a useful,
not required, cross-check.

---

## 8. Cross-world overlaps and pairs

`cappadocian-nicene-pastoral-monastic-tradition` is the one other Built
& Live world in this fleet's "Greek East & Orthodoxy" lane. Fourth-
century Cappadocia's own Trinitarian-doctrinal formation register, its
different century, empire, and language, and the absence of any figure,
text, or controversy shared with this world together support no genuine
cross-world overlap. `cic/corpus-map/PAIRS.yaml` is not modified;
no pairing candidate was identified with any other world's own
corpus, built or candidate.

---

## 9. Material and archaeological sources

Not consulted at this stage. The census's own `legacy` field (icon-painting
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
  Morozova, 17th-century, public domain by date) but is not
  yet downloaded (a Wikimedia Commons fetch returned HTTP 429, a
  rate-limit, not a rights or existence problem) — a live lead, not
  closed.
- **Ordinary believers, priestless communities' own daily life.** Nothing
  vendored (§6).
- **The movement's own internal dissent (Evfrosin against
  self-immolation).** Named, not vendored (§1.1, §6; Registry row 9,
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
them but confirms each is correctly carried to `Open_Gaps_Tracking.md`,
which carries the full, current, append-only record of every open
question this world's build has raised.

---

## 15. The one item that waits

The census's own `floorNote` states an absolute — "no question of doctrine
arises here at all" — that this world's own vendored primary source
contradicts at p. 34 (§1.1; Doc_01 §9). Correcting the census is
portfolio-level, not this world's. It is registered at
`Open_Gaps_Tracking.md` (the census floor entry) and in
`Build/worlds/_cross-world/NEEDS-RULING.md`.

That item does not hold this document. A named escalated item holds a
document only where it would change the document's own conclusions;
correcting the census moves it toward what this document already says,
and none of this document's sourcing conclusions, confidence tiers or
quotability flags turns on its wording.
