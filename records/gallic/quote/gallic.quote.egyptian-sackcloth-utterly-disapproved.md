---
id: gallic.quote.egyptian-sackcloth-utterly-disapproved
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes I.2, read at its locus for this record) -
    Cassian's own account of the Egyptian fathers' rule on dress, offered as this world's own
    counter-example to Martin's sackcloth worn as a visible sign.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes I.2 (npnf211 div iv.iii.i, file lines 16650-16663): the Egyptian fathers'
    rejection of sackcloth as conspicuous dress"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks whether monks were supposed to look distinctive or plain"
  - "participant asks why a monk's clothing mattered at all"
  prefer_instead:
  - "participant wants the north's own opposite practice - retrieve gallic.quote.martin-exorcism-without-touch-or-reproach, where Martin wears sackcloth"
text: >-
  And, therefore, whatever models we see were not taught either by the
  saints of old who laid the foundations of the monastic life, or by
  the fathers of our own time who in their turn keep up at the present
  day their customs, these we also should reject as superfluous and
  useless: wherefore they utterly disapproved of a robe of sackcloth as
  being visible to all and conspicuous, and what from this very fact
  will not only confer no benefit on the soul but rather minister to
  vanity and pride, and as being inconvenient and unsuitable for the
  performance of necessary work for which a monk ought always to go
  ready and unimpeded.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  The objection is not to sackcloth as penance - it is to sackcloth as spectacle. Anything that
  draws attention to the wearer, on this rule, works against the soul rather than for it, and gets
  in the way of ordinary labor besides. The same garment Martin wears as a visible weapon, this
  rule rejects for being visible at all.
modern_rendering: >-
  And so we too should reject some models as unnecessary and useless. These are any models that
  we see were not taught by the saints of old, who laid the foundations of the monastic life. Nor
  were they taught by the fathers of our own time, who in their turn keep up their customs today.
  For this reason they completely disapproved of a robe of sackcloth. They disapproved of it
  because it is seen by everyone and stands out. For that very reason, it will not only do the
  soul no good, but will rather feed vanity and pride. They also disapproved of it because it is
  awkward and unsuitable for doing necessary work. A monk should always go to that work ready and
  unhindered.
relations:
- type: associated-with
  target: gallic.force.power-displayed-disowned
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"disapproved"` returns line 16656; read with `sed -n '16648,16663p'`, inside the Institutes Book
I chapter on dress (`iv.iii.i`). The quoted span is one continuous sentence, "And, therefore,
whatever models..." through "...ready and unimpeded.", ending at its own period; the host record's
own prior wording used a bare "..." mid-sentence where the source needed none - the four words it
skipped ("of a robe of sackcloth") sit directly adjacent, with nothing to elide.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.

This span was previously carried, with an unnecessary mid-sentence ellipsis, inside
gallic.force.power-displayed-disowned's own `description` field. The host
record now paraphrases it in its own voice and points here for the verbatim, unabridged wording.
