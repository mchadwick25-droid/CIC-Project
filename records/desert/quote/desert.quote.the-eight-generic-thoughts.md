---
id: desert.quote.the-eight-generic-thoughts
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-P]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "Contested. The Praktikos is securely Evagrius's own work and the wording is verbatim from the vendored file, but three bounds ride with it. Evagrius is this world's most atypical participant by education - a Cappadocian-formed theologian at Kellia, not a Coptic-speaking villager - so his system is the most systematic thing this world produced and the least representative of it. His speculative works were condemned in 553, well outside this world's own window, which shaped what survives and in which language. And the English is Luke Dysinger's, held under the Guide to Evagrius Ponticus's CC BY 4.0 licence, not a public-domain text - see desert.source.evagrius-praktikos."
sources:
- source_id: desert.source.evagrius-praktikos
  locus: "Praktikos ch. 6, in Luke Dysinger's English (cic/texts/evagrius_praktikos_dysinger.txt)"
  address: "cic:evagrius_praktikos_dysinger.txt:6"
  license: cc-by-4.0
text: "There are eight generic [tempting-] thoughts (logismoi), that contain within themselves every [tempting-]thought: first is that of gluttony; and with it, sexual immorality; third, love of money; fourth, sadness; fifth, anger; sixth acedia; seventh, vainglory; eighth, pride. Whether these thoughts are able to disturb the soul or not is not up to us; but whether they linger or not, and whether they arouse passions or not; that is up to us."
modern_rendering: >-
  There are eight basic tempting thoughts, called logismoi, and every tempting thought
  comes from one of these eight. The first is gluttony. With it comes sexual immorality.
  The third is love of money. The fourth is sadness. The fifth is anger. The sixth is
  acedia. The seventh is vainglory. The eighth is pride. Whether these thoughts can
  disturb the soul is not up to us. But whether they stay, and whether they stir up
  strong desires, is up to us.
speaker_or_author: Evagrius Ponticus, in the Praktikos
license: verbatim
modern_lens_note: "The list is not a catalogue of sins. A logismos is an intruding thought, and the closing clause is the whole ethic: whether it arrives is not up to you, whether it stays is. A modern reader who hears 'eight deadly sins' has already lost the distinction this chapter is drawing. 'acedia' is left untranslated because no English word carries it - see desert.quote.the-noonday-demon for what it actually looks like. The vendored file reads 'sixth acedia' without the comma the other seven have; that is the file, not a silent edit here."
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what thoughts or temptations this world fought"
  - "participant describes unwanted thoughts they cannot stop, or thoughts they hate having"
  - "participant asks where the seven deadly sins came from"
  - "participant asks whether a bad thought is already a sin"
relations:
- type: associated-with
  target: desert.term.logismoi
- type: associated-with
  target: desert.quote.the-noonday-demon
use_note:
  means: "Evagrius's Praktikos names eight generic tempting thoughts, from gluttony to pride, and says their arrival is not up to us but their lingering is."
  not_for:
    - "Equating the list with the later seven deadly sins or calling the thoughts sins"
    - "Taking Evagrius's system as what ordinary desert monks taught, since he is this world's least typical author"
    - "Conflating it with Cassian's Latin list, which sits in desert.quote.eight-principal-faults"
  years: {from: 385, to: 399}
  status: provisional
---
The source of the list the Latin West later reworked into the seven deadly sins, in the words of the
man who made it, in a world this corpus already claimed him for. desert.term.logismoi carried this
taxonomy with the locus "the eight-fold taxonomy (Strand C's systematization; consult-only)" - named
but unshowable - from the build's start until this file was vendored.

The closing clause is why the record is load-bearing rather than decorative. "Whether these thoughts
are able to disturb the soul or not is not up to us; but whether they linger or not, and whether they
arouse passions or not; that is up to us." That single sentence is the charter for
desert.term.nepsis and desert.term.antirrhesis alike: the discipline is not about having no thoughts,
it is about what happens in the seconds after one arrives.

Cassian's Conference V ch. II carries the same eight in Latin, and desert.quote.eight-principal-faults
already held them from there. This is the Greek original the Latin is working from, which makes the
pair a transmission witness as well as a doctrinal one.
