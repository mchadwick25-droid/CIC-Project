---
id: lpc.quote.the-case-set-before-the-bishop
world_id: latin-pastoral-congregational-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
use_note:
  means: "Lucian grants peace to Numeria and Candida in the martyrs' name, if each case goes to the bishop and the sin is confessed openly."
  not_for:
    - "a claim that the grant stands without its condition that each case go before the bishop"
    - "a claim about what the bishop decided for Numeria and Candida"
    - "a claim that 'confession' means a private act before a priest"
    - "a claim about how long reconciliation took or who set its length"
  years: {from: 246, to: 258}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'The text field is the ANF English as printed. modern_rendering follows Hartel''s Latin
    where the English misleads: cum Dominus coeperit is ''when the Lord has begun'', not ''since''; facta
    exomologesi is the sin ''openly confessed''; tractatum, ''tractate'', is the confessors'' own ruling;
    hae and quas are feminine, ''these women'' and ''those''; and ''(all)'' is the translator''s supply,
    left out.'
sources:
- source_id: lpc.source.cyprian-epistles
  locus: Epistle XXI (Oxford Ep. 22), Lucian to Celerinus, section 2; English at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml,
    lines 30728-30732; Latin at cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt, lines 3338-3342
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what Lucian granted to the lapsed women
  - participant asks what condition the confessors set on the peace they gave
  - participant asks whether a confessor could forgive without the bishop
  prefer_instead:
  - participant wants the whole exchange between Celerinus and Lucian -- lpc.story.celerinus-writes-to-lucian
    gives that
claim_guards:
- The speaker must not tell Lucian's grant without its condition, that each case goes before the bishop.
- The passage does not say what the bishop then decided; the speaker must not supply an outcome for Numeria
  and Candida.
relations:
- type: associated-with
  target: lpc.story.celerinus-writes-to-lucian
text: And therefore, brother, as here, since the Lord has begun to give peace to the Church itself, according
  to the precept of Paulus, and our tractate, the case being set forth before the bishop, and confession
  being made, I ask that not only these may have peace, but also (all) those whom you know to be very
  near to our heart.
speaker_or_author: lpc.figure.lucian
license: verbatim
modern_lens_note: 'A modern listener may hear ''confession'' as a private act before a priest. The Latin
  is exomologesis, the sinner''s open confession before the church. Lucian grants peace in the martyrs''
  name, but on a condition: each case goes before the bishop first.'
modern_rendering: And so, brother, I ask that it be done as it is here. When the Lord has begun to give
  peace to the Church itself, let each case be set before the bishop and the sin openly confessed. This
  is as Paulus commanded and as we ruled. Then let not only these women have peace, but also those whom
  you know to be dear to our heart.
---
Lucian to Celerinus, Epistle XXI in the ANF numbering (22 in the Oxford numbering), section 2. English in the ANF translation at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 30728-30732. Latin in Hartel's edition at cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt, lines 3338-3342. A page-break tag inside the passage is stripped. 'These' are Numeria and Candida, named earlier in the section. The passage carries the story lpc.story.celerinus-writes-to-lucian.
