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

    Quote-verbatim gate note (2026-09-22, resolved by R28 on 2026-09-23): this passage sits inside a
    translator's endnote (id iii.viii.xxxiii-p2.2, a long editorial note identifying Pliny and quoting
    his letter to Trajan in full) rather than in Eusebius's own primary running text. The gate strips
    all `<note>` blocks as editorial apparatus by default, which is right for most notes but not this
    one, where the note's own body IS the primary-source quotation - so this record opted in via its
    own `source_note_id` field, naming the note directly. verification_state restored to
    verified-direct: the gate now verifies this record's text character for character against that
    note's own content (the only difference was "ministrae" for the edition's own ligature "ministræ",
    already corrected below).
sources:
- source_id: pahc.source.pliny-letters
  locus: >-
    Pliny, Letters 10.96, as preserved in the vendored Eusebius volume (npnf201_eusebius-church-history-life-of-constantine.xml)
  license: public-domain
source_note_id: iii.viii.xxxiii-p2.2
text: >-
  I therefore considered it the more necessary to examine, even with the use of torture, two female slaves who were called deaconesses (ministræ), in order to ascertain the truth. But I found nothing except a superstition depraved and immoderate; and therefore, postponing further inquiry, I have turned to thee for advice.
modern_rendering: >-
  So I decided I had to get the truth by questioning two female slaves, the
  ones called deaconesses. I questioned them under torture. I found nothing
  but a crude and excessive superstition. So I have put off any further
  investigation, and I am turning to you for advice.
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
Opened 2026-08-27 for three cells at once - F3-E, F5-E and F6-P were each served without a
quote, and each cited this same letter: pahc.witness.outsider-view for Pliny's own report,
pahc.limit.material-remains for the only outside description of this world's worship, and
pahc.term.ministrae for the word itself.

Deliberately one record rather than three. The office and the torture are in the same sentence in
the source, and splitting them across cells would let a turn reach the ministrae without the
interrogation that produced the word.

MODERN RENDERING AUTHORED (2026-08-29, pahc register pass; Mark's standing quote ruling: spoken form is a modern-English translation, not a summary - original wording stays as text, shown at Level 3).

BAR SWEEP (2026-08-29, Mark: "much better thats the bar" - see Ministry/Technology/CiC_Register_Bar_2026-08-29.md): rendering rewritten to the approved sample's level - short sentences, everyday words, translation fidelity kept; original stays as text for Level 3.
