---
id: gallic.quote.martin-sackcloth-and-ashes-reply
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. The saying itself rests on the same
    witness-testimony basis as the rest of the deathbed scene in this letter - Sulpitius was not
    present. Widely Accepted rather than Documented for that reason, though the saying is the letter's
    single clearest statement of formation by named example, and load-bearing for that theme regardless
    of the underlying event's own attestation.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2464-2466): Martin refusing straw for his deathbed, replying to his disciples'' request'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks why sackcloth and ashes mattered, or what a good death looked like in this world
  - participant asks about formation by named example, or why Martin's own choices were treated as
    binding on others
  - participant uses "example," "deathbed," or "sackcloth"
  prefer_instead:
  - participant wants the south's Egyptian teaching on visible asceticism generally, not this one
    deathbed scene - retrieve gallic.term.sackcloth-and-ashes
text: >-
  It is not fitting that a Christian should die except among ashes; and I have sinned if I leave you a
  different example.
speaker_or_author: gallic.figure.martin
license: verbatim
modern_lens_note: >-
  Martin refuses a small mercy - a little straw under his failing body - and gives a reason that is not
  about his own comfort at all. He treats his own death as instruction: if he dies soft, he has taught
  something false by his own example. The word "sinned" is doing real work here - failing to set the
  right example is, for Martin, a moral failure, not just a missed opportunity.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.gravity.named-example
modern_rendering: >-
  It is not right for a Christian to die anywhere but among ashes. If I leave you a different
  example, I have sinned.
use_note:
  means: "Martin, as Sulpitius reports in Letter III, refuses straw on his deathbed, saying a Christian should die among ashes and he must not leave another example."
  not_for:
    - "an eyewitness report, when Sulpitius was not present at the death"
    - "ordinary deathbed practice among Gallic Christians rather than one saint's example"
    - "the rebuke of the devil and the witnesses' report, which sit in gallic.quote.martin-rebukes-the-devil-and-dies"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "I
have sinned if I leave you a different example"` returns line 2466. Read in context at lines
2463-2466: "And when his disciples begged of him that at least he should allow some common straw to be
placed beneath him, he replied: "It is not fitting that a Christian should die except among ashes; and
I have sinned if I leave you a different example."" The quoted reply matches the host record's current
wording exactly; verified independently rather than trusted on that basis. No word was added, dropped,
substituted, or reordered; the edition's own curly quotation marks are dropped as its own punctuation,
not part of the quoted prose.

This same sentence's closing clause also appears, unquoted, in the host record's own `tellable_as`
field as a short teaser phrase; that field was paraphrased to remove the raw quotation and now points
to this record instead of repeating the verbatim wording a second time.
