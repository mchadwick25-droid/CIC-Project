---
id: desert.quote.arsenius-flee-tace-quiesce
world_id: desert-monasticism
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
  formation_confidence: Documented
  divergence_note: The memorable three-word form this saying is known by is a feature of the Latin transmission,
    not of this text. Quoting the triad as Arsenius' own words would be quoting the tradition's compression
    of him.
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: §2, Chapter I (cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt line 47) - Budge's Syriac
    recension; the Greek and Latin traditions render the triad as fuge, tace, quiesce
  license: public-domain
text: Arsenius, flee, keep silence, and lead a life of silent contemplation, for these are the fundamental
  causes which prevent a man from committing sin.
modern_rendering: >-
  Arsenius, flee. Keep silence. Live a life of silent contemplation. These are the basic causes that
  keep a person from sinning.
speaker_or_author: a voice Arsenius reports having heard
license: verbatim
modern_lens_note: '"Flee" risks a modern misreading as anxious avoidance - running from a problem rather
  than facing it, the opposite of what contemporary therapeutic language usually recommends. In this world''s
  own idiom it names a disciplined strategy, not evasion, matching the same risk desert.term.anachoresis''s
  own translational note names for "withdrawal."'
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why anyone would leave people behind to live alone"
  - "participant asks what silence was for and whether it was lonely"
relations:
- type: associated-with
  target: desert.story.arsenius-flee
- type: associated-with
  target: desert.gravity.withdrawal
use_note:
  means: "In Budge's Syriac Sayings, a voice tells Arsenius to flee, keep silence, and live in silent contemplation, as the causes that keep a man from sin."
  not_for:
    - "the Latin triad fuge, tace, quiesce as Arsenius's own words or as this text's wording"
    - "fleeing as anxious avoidance rather than a chosen discipline"
    - "the separate first saying, to flee from men, which stands at §1 and is not quoted here"
    - "the saying as securely datable to Arsenius rather than transmitted in a collection compiled after 430"
  years: {from: 320, to: 430}
  status: reviewed
---
Verified against the vendored Budge at line 47, §2. These are the
voice's words only - the file's
framing ("And when Arsenius was living the ascetic life in the monastery,
he prayed to God the same prayer, and again he heard a voice saying unto
him") precedes them and is not quoted.

THE PARAPHRASE IT REPLACES compressed TWO sayings into one. It read
"Flee the company of men, and you will be saved... Flee, be silent, be
still - these are the roots of a life without sin," joining §1 (the voice
telling Arsenius to flee from men) to §2, in the clipped triad form -
fuge, tace, quiesce - that the Latin tradition made famous. Budge's
Syriac is longer, plainer and less epigrammatic. It is what this world
can actually show, and §1 remains separately available at line 46 if the
first half is ever wanted.

Paraphrase, not verbatim quotation, per desert.source.apophthegmata-
patrum's own hard rule. The Latin systematic collection's own
three-word form ("fuge, tace, quiesce") is well known outside this
corpus but is not itself vendored or independently verified here; this
record carries the saying in English paraphrase only, matching
desert.story.arsenius-flee.

divergence_note carries both halves of desert.source.apophthegmata-patrum's
own confidence pairing, the "Widely Accepted" half and the unconditional
Inferential-Thin bound. speaker_or_author carries no parenthetical
provenance tag; the source is already carried in sources[] and
divergence_note.

`sources[].locus` also compiles into `quotes.json`
(`build_quotes_json()` emits `sources` verbatim), so it is written as a
plain description: it does not name a sibling record id, use
build-process language, or carry a licence-mechanics gloss.
