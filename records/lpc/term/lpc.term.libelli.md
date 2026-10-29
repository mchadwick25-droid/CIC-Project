---
id: lpc.term.libelli
world_id: latin-pastoral-congregational-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
relations:
- type: associated-with
  target: lpc.term.certificates-letters-of-peace
- type: associated-with
  target: lpc.term.libellatici-sacrificati
- type: associated-with
  target: lpc.term.reconciliation-penitential-discipline
- type: associated-with
  target: lpc.term.the-lapsed
use_note:
  means: "A libellus said you had made the pagan offering; some bought one without making it, and Cyprian still held them fallen."
  not_for:
    - "a claim that it was a modern identity document or licence"
    - "a claim that the Latin word appears in the English volume, which renders it certificates"
    - "a claim that Latin libellus names only this paper"
    - "a claim that Celerinus's sister bought a certificate, since the letter about her says she sacrificed"
  years: {from: 246, to: 258}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: Cyprian uses the word himself, in De Lapsis and in his letter to Antonianus. The English
    translation renders libelli as certificates, so the Latin headword is absent from the vendored English
    volume apart from one occurrence in the Introductory Notice to the anonymous treatise against Novatian.
    The Latin witnesses carry it. Latin libellus in Cyprian also names the martyrs' petitions, so the split
    between this term and lpc.term.certificates-letters-of-peace separates the English word and is not
    a distinction the Latin makes.
sources:
- source_id: lpc.source.cyprian-de-lapsis
  locus: De Lapsis 27 -- 'libellis tamen conscientiam miscuerunt' (defiled their conscience with certificates);
    De Lapsis 28 -- 'nullo sacrificii aut libelli facinore constricti' (bound by no crime of sacrifice
    or of certificate)
  license: public-domain
- source_id: lpc.source.cyprian-epistles
  locus: Epistle LI (to Antonianus) 13 and 14 -- those who receive certificates are not to be put on
    a par with those who have sacrificed; the plea of one who obtained a certificate and paid a price
    for it
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how the persecution was actually administered
  - participant asks what a certificate was, or how someone could lapse without sacrificing
  prefer_instead:
  - the participant is asking about the category of persons rather than the document itself -- ask about
    the lapsed instead
  - 'also: this corpus uses the bare word certificate for two different documents travelling in opposite
    directions -- this is the one the empire issued, which made a person lapsed'
  - the confessors' own letter of peace, which asks the church to take a person back, is a separate term
    (certificates) and a participant asking simply what a certificate was should be pointed to both
plain_meaning: 'Rome ordered a sacrifice. Some people paid for a paper saying they had made it, without
  sacrificing at all. Cyprian called that paper a denial: their hands were clean, but their conscience
  was not.'
world_word: libelli
distortion_risk: low
false_friend:
- a formal identity document or licence, in the modern administrative sense
senses:
  informational: 'The empire asked for a sacrifice, and then wrote down that one had been made. A demand
    satisfied with money rather than incense produced a class of people who had not, in their own minds,
    worshipped anything, and who nonetheless held a document saying they had. This is the administrative
    fact underneath the lapsed, and therefore underneath our whole penitential discipline and the confessor-authority
    tension: the crisis was documentary rather than merely moral.'
  evidential: Our own bishop Cyprian names this paper. In De Lapsis he speaks of those who have defiled
    their conscience with certificates, and in his letter to Antonianus he writes of those who receive
    certificates and sets them beside those who sacrificed. The English calls it a certificate. The Latin
    word is libellus.
  translational: A modern listener may picture a formal identity document or licence. We mean a compliance
    record produced by an empire-wide administrative demand, whose existence is exactly what made failure
    documentary and public rather than private.
quick_meaning: The libelli were papers saying a person had sacrificed. Some people bought one and never
  sacrificed. Holding that paper made a person one of the lapsed.
---
Derived from Doc_06 §2.3 and Lexicon-Chunks/lpclex017_libelli.md.
