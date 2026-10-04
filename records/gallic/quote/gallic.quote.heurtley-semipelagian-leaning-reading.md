---
id: gallic.quote.heurtley-semipelagian-leaning-reading
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
voice: analytic
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as editorial transmission history, not this world's own primary-source voice -
    the NPNF volume's own editorial Appendix III (read at its locus for this record), reading
    Vincent's own handling of Celestine's letter as showing a Semipelagian leaning. Whether Vincent
    actually held that leaning is Contested (carried in the host record's own divergence_note); this
    record carries the editor's own reading as his, not as this record's independent finding.
sources:
- source_id: gallic.source.npnf-editorial-apparatus
  locus: "Appendix III, Note on Section 85, Page 156 (npnf211 div iii.xxxvii, file lines 14887-14900):
    the editor's reading of Vincent's own handling of Celestine's letter"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why modern editors read Vincent's handling of Celestine's letter with suspicion"
  - "participant wants the editor's own reasoning for calling Vincent's reversal a wish to shift blame"
  prefer_instead:
  - "participant wants Vincent's own quotation and reading of the letter directly - retrieve gallic.quote.vincent-celestines-letter-and-its-reading"
text: >-
  The manner in which Vincentius deals with this letter has been very
  commonly thought, and with reason, to indicate a Semipelagian
  leaning. His "si ita est," "if the case be so," emphasized by being
  repeated again and again, quite in an excited manner, as we should
  say, shows an evident wish to shift the charge of novelty from those
  against whom it had been brought, and fix it upon the opposite party.
speaker_or_author: "Charles A. Heurtley, editorial Appendix III"
license: verbatim
modern_lens_note: >-
  The editor is not describing Vincent's argument neutrally - he is naming what he takes it to
  reveal. The repeated Latin phrase Vincent uses, "if the case be so," is read here as a tell: not
  a careful qualification but an "excited" insistence, aimed at moving the charge of novelty onto
  Vincent's own opponents.
modern_rendering: >-
  Very many people have thought, and with good reason, that the way Vincentius handles this letter
  points to a Semipelagian leaning. He stresses his "si ita est," "if this is the case," by
  repeating it again and again. He does so in what we would call quite an excited way. This shows a
  clear wish to shift the charge of novelty off those accused of it and fix it on the opposite
  side.
relations:
- type: associated-with
  target: gallic.force.contest-over-antiquity
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"The manner in which Vincentius deals"` returns line 14887; read with `sed -n '14887,14900p'`,
inside `<div2 title="Appendix III. Note on Section 85, Page 156." ... id="iii.xxxvii">`. The quoted
span is one continuous passage (`<p id="iii.xxxvii-p5">`) of two sentences, "The manner in which
Vincentius deals with this letter..." through "...fix it upon the opposite party.", ending at its
own period. A translator's endnote listing four scholars who share this reading falls between the
two sentences, right after "Semipelagian leaning." and before "His 'si ita est,'" and is excluded
as apparatus per the fleet's own `<note>`-stripping convention.

Normalization: line breaks joined with single spaces; the source's own curly quotation marks around
"si ita est" and "if the case be so" are rendered here as straight double quotes, the same marks in
a different Unicode form. No word was added, dropped, substituted, or reordered.

speaker_or_author is a plain string: this is the NPNF volume's own editorial apparatus (Charles A.
Heurtley's Appendix III), not a figure from within this world.
