---
id: gallic.quote.salvian-free-men-in-seeming-captivity
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
    Documented as Salvian's own text (Gov. V.5, read at its locus for this record). Named Tension
    carried at full strength (see gallic.force.barbarian-fiscal-ruin's own divergence_note):
    Salvian's is a preacher's indictment, Dominant Modern Reconstruction as to scale; this record
    carries the claim as Salvian states it.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "V.5 (Sanford p. 142): Romans fleeing to the Goths and the Bagaudae, preferring barbarian
    rule to Roman injustice"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Romans would flee to the very barbarians overrunning Gaul"
  - "participant asks how Salvian judged Roman rule against barbarian rule"
  prefer_instead:
  - "participant wants the tax-injustice claim this flight is a response to - retrieve gallic.quote.salvian-rich-murdering-the-poor"
text: >-
  For they would rather live as free men, though in seeming captivity,
  than as captives in seeming liberty.
speaker_or_author: Salvian of Marseilles, On the Government of God
license: verbatim
modern_lens_note: >-
  The paradox is the whole point: life among the barbarians looks like captivity, but Salvian
  calls it freedom, because Roman rule, in his account, has made citizenship itself a form of
  captivity in fact if not in name.
modern_rendering: >-
  For they would rather live as free men, though in seeming captivity, than as captives in seeming
  freedom.
relations:
- type: associated-with
  target: gallic.force.barbarian-fiscal-ruin
use_note:
  means: "Salvian, in On the Government of God, says Romans fleeing to the Goths and Bagaudae preferred freedom in seeming captivity to captivity in seeming liberty."
  not_for:
    - "a measured estimate of how many Romans fled, when Salvian is a preacher indicting Rome"
    - "the tax burden itself, which sits in gallic.quote.salvian-rich-murdering-the-poor"
    - "a view shared by the monastic writers of this world generally"
  years: {from: 439, to: 450}
  status: reviewed
---
Verified directly against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n
"free men"` and `grep -n "seeming captivity"` both return line 6458; read with `sed -n
'6446,6461p'`, on the page numbered "142 THE FIFTH BOOK." The wider sentence this clause sits in
("So you find men passing over everywhere...") carries two OCR artifacts this edition's
REGISTRY.yaml apparatus entry does not yet cover - a bare closing curly quote (U+201D) glued to
"anywhere," with no matching open quote (the same defect class already disclosed, for a different
point in this same file, in `gallic.quote.salvian-on-the-unburied-dead`'s own trailer), and a
stray period glued mid-clause in "they do not repent. of their expatriation" (line 6457) - neither
a safe pattern to strip edition-wide off one occurrence each. This record's own quoted span is
narrowed to the one continuous, artifact-free sentence that carries the load-bearing claim - "For
they would rather live as free men..." through "...captives in seeming liberty.", ending at its
own period - rather than carrying an artifact-bearing `text` field or inventing an unevidenced
edition-wide rule.

Normalization: hard line-wraps rejoined with single spaces, including a hyphenated line-break word
("seem-\ning"); "For" capitalized to open this record's own `text` field (a case difference
`engine.m1.quote_verbatim` tolerates), the source's own word at that position being lowercase
"for" mid-sentence. No word was added, dropped, substituted, or reordered within the quoted span
itself.