---
id: pahc.quote.asia-rejected-new-prophecy
world_id: post-apostolic-house-church
record_type: quote
schema_version: 2
status: ready
register: etic
canon_cells:
- F3-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Contested
  divergence_note: "Doubly-mediated hostile testimony, same discipline as pahc.source.anti-montanist-
    fragments itself: an anonymous opponent, preserved only in Eusebius's later quotations, printed by
    ANF under the conjectural name 'Asterius Urbanus,' which this build does not treat as a real
    attribution. The dating (c. 192-193) follows the fragment's own internal chronology, not the ANF
    introduction's Tillemont-derived 'circa A.D. 232.'"
sources:
- source_id: pahc.source.anti-montanist-fragments
  locus: "Book I, from the Anonymous's own account of the Asia-wide synodical response to the New
    Prophecy (anf07 line 11308), the same passage preserved at Eusebius HE V.16.10"
  license: public-domain
text: For when the faithful throughout Asia met together often and in many places of Asia for
  deliberation on this subject, and subjected those novel doctrines to examination, and declared them
  to be spurious, and rejected them as heretical, they were in consequence of that expelled from the
  Church and debarred from communion.
modern_rendering: >-
  Believers all over Asia kept meeting for deliberation on this. This
  happened again and again, in many different places. They subjected
  these new teachings to examination. They declared them false, and
  rejected them as heresy. Because of that, they were expelled from the
  Church and debarred from communion.
speaker_or_author: "The Anonymous anti-Montanist writer (c. 192-193 CE), addressing Avircius
  Marcellus; printed by ANF under the conjectural name 'Asterius Urbanus,' not treated as a real
  attribution here"
license: verbatim
modern_lens_note: >-
  This is not Ignatius, and it is not about docetism - it is a separate Asia Minor voice, roughly
  three generations after Ignatius, describing a different contemporary rival (the New Prophecy /
  Montanism) being examined and rejected by gathered bishops rather than by one man's letters. It
  corroborates that this world's boundary-drawing against contemporary rivals was a real, live,
  multi-voiced pattern - not that this specific gravity's anti-docetic claim has a second voice.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether other Christian groups besides this one were considered dangerous or false"
  - "participant asks how disputes with rival Christian movements were actually settled"
  prefer_instead:
  - "participant asks specifically about the docetic controversy - this passage does not address it"
relations:
- {type: illustrates, target: pahc.gravity.boundary-drawing}
---
Discovered 2026-09-09 in a supplemental source review: pahc.source.anti-
montanist-fragments was registered at this build's Step 2 to answer Doc_01
SS8.3's Montanism disclosure obligation, but no quote or gravity record had
drawn on it since. Text verified directly against cic/texts/anf07_lactantius
-apostolic-constitutions-didache-liturgies.xml at line 11308, no elisions.
The quoted
text was independently re-diffed against the vendored file and
confirmed byte-for-byte accurate throughout.

WHAT THIS DOES AND DOES NOT DO FOR G05. pahc.gravity.boundary-drawing's own
record states plainly that Doc_01's naming of Marcion, Valentinian teaching,
and the New Prophecy as live contemporary rivals is "comparative/contextual
analysis, not itself an independent primary-voice evidence stream," and
that the record does not let that synthesis substitute for the Repetition
test's own requirement. This quote changes that fact for exactly one of the
three named rivals: it is a primary-voice evidence stream, not Doc_01's own
synthesis, attesting that the New Prophecy was actively, synodically
opposed within this same broad window. What it does not do is supply a
second voice for the anti-docetic claim itself - opposing prophetic
authority and opposing docetic christology are different content, and this
record does not let the general pattern substitute for the specific claim's
own Repetition score, for the same reason Doc_04 already refused to let
Doc_01's synthesis do that work.
