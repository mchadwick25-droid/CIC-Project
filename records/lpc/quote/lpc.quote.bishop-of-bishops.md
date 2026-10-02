---
id: lpc.quote.bishop-of-bishops
world_id: latin-pastoral-congregational-christianity
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: lpc.source.cyprian-seventh-council-of-carthage
  locus: the 256 Council preface; independently re-located and re-read this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml,
    line 56872
  license: public-domain
- source_id: lpc.source.augustine-on-baptism-against-the-donatists
  locus: Augustine's own three independent quotations of the identical proposition while arguing against
    it at length; cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 11292, 11626, 12207
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks whether one bishop could overrule another
  - participant asks about church government, councils, or the origins of papal authority
  - participant asks how disputes between bishops were settled
  - conversation reaches conciliar authority theory
  prefer_instead:
  - participant is asking about a bishop's own authority over his own congregation rather than about bishops'
    authority over each other -- ask about the flock instead
claim_guards: []
relations:
- type: associated-with
  target: lpc.figure.cyprian
text: For neither does any of us set himself up as a bishop of bishops, nor by tyrannical terror does
  any compel his colleague to the necessity of obedience; since every bishop, according to the allowance
  of his liberty and power, has his own proper right of judgment, and can no more be judged by another
  than he himself can judge another. But let us all wait for the judgment of our Lord Jesus Christ, who
  is the only one that has the power both of preferring us in the government of His Church, and of judging
  us in our conduct there.
speaker_or_author: lpc.figure.cyprian
license: verbatim
modern_lens_note: A modern listener may hear this as an early anti-papal manifesto, or a constitutional
  principle about separated powers among equal branches. We mean neither. It is a working statement of
  how a council among us proceeds, said by the man presiding, inside a shared conviction that the episcopate
  is one undivided office rather than a hierarchy of ranks.
modern_rendering: None of us sets himself up as a bishop over other bishops, and none of us uses a tyrant's
  terror to force a colleague into obedience. Every bishop has his own right to judge, in keeping with
  the freedom and power allowed to him. He can no more be judged by another bishop than he himself can
  judge another. Instead, let us all wait for the judgment of our Lord Jesus Christ. He is the only one
  who has the power both to place us in the government of His Church and to judge how we conduct ourselves
  there.
---
Named directly in the Permanent Prompt's own 'what our own life actually gave us' paragraph (line 37, and quoted at greater length at line 29): 'Neither of us set himself up as a bishop of bishops.' The line is also the sole cited locus of the already-built lpc.term.bishop-of-bishops (records/lpc/term/, B-2/B-3, read but not touched this pass) -- this record supplies a quote-record name-bridge and a modern_rendering for the same already-established text, not a duplicate finding. Independently re-located and re-read this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 56872, and independently corroborated at three further points in the same vendored file where Augustine quotes the identical proposition back at Cyprian's own successors while arguing against it (lines 11292, 11626, 12207) -- the strongest cross-attested single line in this world's whole corpus, matching don's own precedent of preferring a quote independently corroborated by a second, differently-motivated witness over one attested only once.
