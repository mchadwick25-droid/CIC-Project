---
id: syr.source.bar-hebraeus-chronicon-ecclesiasticum
world_id: syriac-edessa-nisibis
record_type: source
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Contested
  divergence_note: >-
    A 13th-century compiler's own chronicle, itself drawing on earlier (largely lost) sources for
    events nine centuries before his own time - the same "chronicle-derived and hagiographically
    inflected, not contemporary attestation" caveat Doc_02 SS11 already applies to this succession
    material generally applies here specifically, now to a primary text rather than only to Fiey's
    modern reconstruction of it. Does NOT resolve the Simeon bar Sabbae dating dispute (341 vs. the
    Kosinski/Burgess c. 344 redating) - that argument rests on external regnal-year/astronomical
    reasoning a 13th-century chronicle cannot itself adjudicate either way.
sources: []
author: "Bar Hebraeus / Gregory Abu'l-Faraj (1226-1286), Maphrian of the Church of the East's
  Jacobite counterpart tradition and historian"
work: "Chronicon Ecclesiasticum (the ecclesiastical chronicle, distinct from his separate secular
  Chronography/Chronicon Syriacum), Volume III of 3 - the Eastern Church section: the Nestorian
  Catholicoi from Papa bar Aggai through Isaac, then the Jacobite Maphrians. Registered here for the
  early Catholicoi entries (Papa, entry 10, through Simeon bar Sabbae's martyrdom, entry 11) that
  fall inside this world's own 340s-410 window"
edition: "Abbeloos-Lamy critical edition with facing Latin translation (Louvain: Peeters, 1872-1877),
  vendored as cic/texts/barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt (Sectio
  II opens at file line 304; the Papa entry at line 1670; the Simeon bar Sabbae entry at line 2061,
  running to his martyrdom account closing at line ~2189)"
kind: vendored
rights_status: public-domain
attribution_status: attributed
discovery_channel: "genuine acquisition research, 2026-09-09: Doc_02 SS11 and syr.contested.papa-
  primacy both named the Persian episcopal succession as chronicle-derived (Chronicle of Seert, Bar
  Hebraeus, as reconstructed by Fiey) but no primary edition of either chronicle had been vendored -
  this session verified a public-domain edition was findable on archive.org and vendored it directly
  (see cic/texts/REGISTRY.yaml's own entry for the unusual supplied_by disclosure: this build session,
  not Mark, per this session's own atypical live web access)"
external_ids: {archive_org: "BarHebraeusChroniconEcclesiasticumVol.3"}
---
LANGUAGE DISCIPLINE: this is a Latin translation of a Syriac original -
a second-witness, original-language-adjacent source per this project's
own rule (cic/texts/INTAKE.md), never primary evidence for a
Representative on its own (this project's evidence language is
English). Used here DESCRIPTIVELY, in English, in the builder's own
words - never as a verbatim English "quote" record, since the source
itself is not English. OCR QUALITY: the vendored file's own header
discloses that ABBYY OCR handles the Latin translation itself
reasonably well but renders the Syriac original as unusable noise
throughout, and that footnote text OCRs measurably worse than the main
narrative - any specific wording drawn from this file should be
independently re-verified before being treated as settled, especially
from a footnote.

WHAT THIS ADDS. syr.contested.papa-primacy's own `sources[]` previously
held only syr.source.gedsh, an in-copyright, consultation-only
encyclopedia entry (verification_state: named-not-rechecked). This
record lets that contested claim, and Doc_02 SS11's fuller succession
narrative, cite an actual primary chronicle text directly
(verification_state: verified-direct) for the first time - confirming,
against the vendored Latin itself, that Papa bar Aggai's chronicle
entry names Simeon bar Sabbae as his own disciple and immediate
successor (entry 11, "Post Papam Simeon Barsabob... ejus discipulus"),
that Simeon is credited with instituting antiphonal (two-choir) prayer
in the Eastern churches - explicitly modeled, per this text, on a
practice attributed to "the fiery Ignatius, disciple of John the
Evangelist" in the West - and with decreeing that clerics recite the
Davidic psalms in the offices from memory rather than from a book, and
that he is reported to have held office thirteen years before his
martyrdom under Shapur II ("Officio functus est Simeon tredecim
annos"), arrested alongside four bishops and ninety-nine priests,
deacons, and laity ("episcopi quatuor ac nonaginta novem presbyteri,
diaconi et fideles"), all martyred with him. The volume continues with
entries 12-15 (Shahdost,
Barba'shmin, Tomarsa, Qayyoma), corroborating the fuller succession
Doc_02 SS11 already names from Fiey's reconstruction - not yet
individually verified against the Latin locus by locus; a future pass
citing those later entries should re-verify each against this file
directly rather than assuming the pattern holds.

RAW OCR, DISCLOSED PLAINLY (matching the same scrupulousness this
commit applies to the Odes of Solomon's OCR disclosure): the three
Latin fragments quoted above are silently normalized from the file's
own visible OCR text, which carries recognizable errors. As they
actually appear at the cited lines: "Post Papam Simeon Barsabob...
ejus discipulus" is OCR'd at file line 2059-2060 as "11 .Po5i Fapam
Simeon Barsabob 9 , * / ejus discipulus." ("Po5i" for "Post," "Fapam"
for "Papam," a stray "9" and "*"). "Officio functus est Simeon
tredecim annos" is OCR'd at line 2183 essentially as printed, only
split across the page's own line-wrap ("Officio functus est Simeon
tredecim / annos"). "Episcopi quatuor ac nonaginta novem presbyteri,
diaconi et fideles" is OCR'd at lines 2166-2167 as "copi quatuor 1 ac
nonaginta novem / presbyteri, diaconi et fideles" - the leading
"epis-" is lost across a page/column break (with a stray footnote
marker "1" inserted) and has been silently restored here from the
word's own unambiguous continuation; no other correction was made.
None of this changes the substance of what any fragment says; it is
disclosed so a future verification pass checks the file's own OCR
directly rather than trusting this record's normalized wording.

WHAT THIS DOES NOT DO. Bar Hebraeus writes nine centuries after these
events, compiling earlier (largely lost) sources; nothing here upgrades
this succession from "chronicle-derived and hagiographically inflected"
to contemporary attestation, and nothing here settles the Simeon
bar Sabbae redating dispute - nowhere does this text engage the
regnal-year/astronomical argument Kosinski and Burgess make for c. 344,
because that argument did not exist for Bar Hebraeus to engage. Its
value is narrower and real: an actual primary chronicle a reader can
open and check, in place of relying solely on a modern scholar's own
secondary reconstruction of what that chronicle says.
