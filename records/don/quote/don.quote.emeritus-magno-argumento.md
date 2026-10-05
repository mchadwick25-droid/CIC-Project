---
id: don.quote.emeritus-magno-argumento
world_id: donatism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted rather than Documented, because the vendored Migne PL11 scan is poor at this act. The Latin
    here matches the cleaner Mansi facsimile, where the long s is scanned as f. It is given in corrected
    spelling, so it cannot be matched character for character against either scan. That is why
    verification_state is verified-via-authority. No clean vendored transcription exists.
sources:
- source_id: don.source.migne-pl11-collatio-carthaginiensis
  locus: "Act 50 of the 411 Conference of Carthage; cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, lines 126834-126837 (garbled OCR). The same sentence reads cleanly in cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-4-410-431-lat_welter-facsimile1901.txt, lines 19492-19495."
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how a Donatist bishop argued procedure before an imperially-convened tribunal
  - conversation reaches the 411 Conference of Carthage and needs a specific, directly-quoted moment of
    a Donatist bishop's own voice, not only a description of the event
  prefer_instead:
  - participant wants the Conference's own outcome or scale (this quote is one procedural objection at
    one act, not a summary of the whole three-day proceeding, which this world's own build has not yet
    read in full -- Doc_09 SS8 item 2)
relations:
- type: associated-with
  target: don.figure.emeritus
text: '"Magno argumento veritas occultatur; ut cum ad inquisitionem nostram modicum quid ex parte adversa
  prolatum sit, cetera sileantur."'
speaker_or_author: don.figure.emeritus
license: verbatim
modern_lens_note: 'A modern reader may hear a procedural objection like this as a stalling tactic, a lawyer
  avoiding the real question. Emeritus''s own point is closer to the opposite: he is refusing to let the
  case proceed to its substance at all until the opposing advocates disclose their own names, rank, and
  mandate to the court -- treating procedural standing itself as the truth the other side is trying to
  keep hidden, not a distraction from it.'
modern_rendering: Truth is hidden by a great argument. When, in response to our inquiry, only a small
  thing is brought forth from the other side, the rest is passed over in silence.
use_note:
  means: "At the 411 Carthage conference, Emeritus protested that truth was hidden while the other side withheld its envoys' names, rank and mandate."
  not_for:
    - "a claim that Emeritus was merely stalling to avoid the real question"
    - "a claim about the outcome or scale of the whole 411 conference"
    - "a claim resting on this Latin as a settled critical-edition text"
  years: {from: 411, to: 411}
  status: reviewed
---
Emeritus speaks at act 50 of the 411 Conference. His point is procedural: the other side has not named its envoys, their rank or their mandate. The Gesta reaches us in two vendored Latin scans, both rough, and the divergence note says how the quoted sentence relates to each.
