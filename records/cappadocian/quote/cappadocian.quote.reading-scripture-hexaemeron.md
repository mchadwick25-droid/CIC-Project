---
id: cappadocian.quote.reading-scripture-hexaemeron
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-hexaemeron-homilies
  locus: "Hexaemeron, Homily VIII (The creation of fowl and water animals), sec. 8 (npnf208_basil-letters-select-works.xml)"
  license: public-domain
text: >-
  If we simply read the words of Scripture we find only a few short
  syllables. "Let the waters bring forth fowl that may fly above the
  earth in the open firmament of heaven," but if we enquire into the
  meaning of these words, then the great wonder of the wisdom of the
  Creator appears. What a difference He has foreseen among winged
  creatures! How He has divided them by kinds! How He has characterized
  each one of them by distinct qualities!
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader might hear "we find only a few short syllables" as
  Basil shrugging off the text's brevity, or hear "if we enquire into
  the meaning" as license to hunt for a hidden, coded significance
  behind the words - the move allegorizing readers actually made with
  this same book. Basil means something narrower and more disciplined:
  take the plain sentence at face value (waters producing flying
  creatures), then let sustained, attentive looking at that very same
  created thing - not a symbol standing in for something else - disclose
  the Creator's wisdom. The "deeper meaning" he is after is wonder at
  what God actually made, not a second, secret text hiding underneath
  the first.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how this world's teachers actually read Genesis - for bare facts, for hidden codes, or something else"
  - "participant asks how looking closely at ordinary created things counts as real theology in this tradition"
relations:
- type: associated-with
  target: cappadocian.dw.reading-scripture
modern_rendering: >-
  If we simply read the words of Scripture, we find only a few short syllables: "Let the
  waters bring forth flying creatures that fly above the earth in the open firmament of
  heaven." But if we ask what these words mean, the great wonder of the Creator's wisdom
  appears. What a difference he foresaw among the winged creatures! How he divided them by
  kinds! How he marked each one with its own distinct qualities!
use_note:
  means: "Basil's eighth Hexaemeron homily says the few syllables about the creation of birds disclose the Creator's wisdom once their meaning is closely examined."
  not_for:
    - "licence for allegory or hidden codes, which Basil sets against plain attentive reading"
    - "the psalms as the unlettered believer's education, which sits in cappadocian.dw.reading-scripture through cappadocian.term.psalmodia"
    - "this world's canon list, which the homily does not address"
  years: {from: 360, to: 379}
  status: provisional
---
Verified verbatim directly against the vendored
npnf208_basil-letters-select-works.xml. Located with `grep -n -i "if we
simply read the words of Scripture"`, which hits line 21217, inside the
Hexaemeron's own `id="viii.ix"` div (header at lines 20497-20500 reads
"Homily VIII" / "The creation of fowl and water animals"); the quoted
sentences run lines 21217-21224, ending just before the homily pivots to
a new topic ("But the day will not suffice me..."). Double-spacing in
the source file's own typesetting normalized to single spaces; the
source's curly quotation marks rendered as straight quotes; no wording
added, dropped, or reordered.

Chosen over the Hexaemeron's other well-known interpretive-method
passage (Homily IX's explicit "I know the laws of allegory... for me
grass is grass... I take all in the literal sense," aimed at Origen's
allegorizing) because cappadocian.dw.reading-scripture's own claim is
not simply "Basil read literally" - it is the fuller two-part claim
that this world's own record makes: a plain reading of the words
themselves, paired with inquiry into what those plain words teach about
the God who made the thing described, not chiefly facts to defend and
not license to allegorize the text into something else. This passage
states exactly that method in Basil's own words and then performs it in
the same breath (the plain sentence about waters and fowl, immediately
followed by what studying real birds discloses about the Creator's
wisdom), which is why it backs the dw's "plain, attentive reading"
claim more precisely than the pure anti-allegory passage would on its
own.

The spoken form is a modern-English translation, never the archaic original; the original stays as the record's own text field, shown at Level 3.
