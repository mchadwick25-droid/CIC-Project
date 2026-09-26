---
id: pahc.quote.two-female-slaves-who-were-called-deaconesses
world_id: post-apostolic-house-church
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-E
- F5-E
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Pliny's own report to Trajan, c. 112, and it is the outside witness this world's record most depends on. It is a governor explaining his own procedure to an emperor, written by a man who says plainly he had never handled such a case before; what he reports of Christian practice he got under interrogation and torture.

    This passage sits inside a translator's endnote (id iii.viii.xxxiii-p2.2, a long editorial note
    identifying Pliny and quoting his letter to Trajan in full) rather than in Eusebius's own primary
    running text. The gate strips `<note>` blocks as editorial apparatus when checking the running
    text, which is right for most notes but not this one, where the note's own body IS the
    primary-source quotation - so the gate falls back to checking every `<note>` body in the same
    source file once the running text fails, rather than relying on a per-record field naming the
    note (a hand-set pointer would not scale across a hundred-world fleet). verification_state is
    verified-direct: the gate verifies this record's text character for character against that
    note's own content (the only difference was "ministrae" for the edition's own ligature
    "ministræ", already corrected below).
sources:
- source_id: pahc.source.pliny-letters
  locus: >-
    Pliny, Letters 10.96, as preserved in the vendored Eusebius volume (npnf201_eusebius-church-history-life-of-constantine.xml)
  license: public-domain
text: >-
  I therefore considered it the more necessary to examine, even with the use of torture, two female slaves who were called deaconesses (ministræ), in order to ascertain the truth. But I found nothing except a superstition depraved and immoderate; and therefore, postponing further inquiry, I have turned to thee for advice.
modern_rendering: >-
  I therefore considered it all the more necessary to examine two
  female slaves, called deaconesses. I did this even with torture, to
  find out the truth. But I found nothing except a superstition,
  depraved and immoderate. And so, putting off further inquiry, I have
  turned to you for advice.
speaker_or_author: Pliny the Younger, governor of Bithynia, to the emperor Trajan
license: verbatim
modern_lens_note: >-
  Two things a reader should hold together and usually cannot. This is the earliest outside evidence that women held a titled office in these communities - ministrae, which Pliny reaches for a Latin word to render - and the only reason we have it is that two enslaved women were tortured. The office is attested by the interrogation. There is no version of this evidence without that.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what outsiders said about these people"
  - "participant asks whether women held office or leadership here"
  - "participant asks what physical or documentary evidence survives about this world"
  - "participant asks about the hardest thing in this world's record"
relations:
- type: associated-with
  target: pahc.witness.outsider-view
- type: associated-with
  target: pahc.term.ministrae
- type: associated-with
  target: pahc.limit.material-remains
---
This quote serves three cells at once - F3-E, F5-E and F6-P - each of which cites this same
letter: pahc.witness.outsider-view for Pliny's own report, pahc.limit.material-remains for the
only outside description of this world's worship, and pahc.term.ministrae for the word itself.

Deliberately one record rather than three. The office and the torture are in the same sentence in
the source, and splitting them across cells would let a turn reach the ministrae without the
interrogation that produced the word.

The modern rendering is a modern-English translation, not a summary; the original wording stays as text, shown at Level 3. It follows the project's approved register: short sentences, everyday words, translation fidelity kept.
