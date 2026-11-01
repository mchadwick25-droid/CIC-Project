---
id: lpc.term.confessor
world_id: latin-pastoral-congregational-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
relations:
- type: associated-with
  target: lpc.term.certificates-letters-of-peace
- type: associated-with
  target: lpc.term.communion
- type: associated-with
  target: lpc.term.reconciliation-penitential-discipline
- type: associated-with
  target: lpc.term.the-flock
- type: associated-with
  target: lpc.term.the-lapsed
use_note:
  means: "In Cyprian's time a confessor, who kept faith when questioned and lived, could rival a bishop."
  not_for:
    - "a claim that a confessor was a priest who hears confessions"
    - "a claim that the word carries this sense in Augustine's phase"
    - "a claim that confessors speak for themselves beyond a few letters"
  years: {from: 246, to: 258}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'The evidence base for this term is essentially one Registry row (the Epistles) read
    through one lexicon entry, disclosed at generation rather than discovered afterwards (Author-Gravity-Risk:
    Yes). A phase bound was established by a check, not assumed: a sweep of all eight vendored Augustine
    volumes returns twenty occurrences of the stem against roughly 150 in Cyprian''s one volume, and none
    carries this sense -- this term belongs to Cyprian''s phase and does not cross into Augustine''s.'
sources:
- source_id: lpc.source.cyprian-epistles
  locus: the Epistles are the primary evidence, including Epistles XX-XXI, whose own title-line the
    Registry gives as 'the confessors'; Epistle XVI, the confessors to Cyprian -- 'we have granted peace;
    and we have desired that this rescript should be made known by you to the other bishops also'; verified
    directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 30386-30391; Latin
    at cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt, lines 3389-3391
  license: public-domain
- source_id: lpc.source.cyprian-de-lapsis
  locus: De Lapsis 2 -- 'We look with glad countenances upon confessors illustrious with the heraldry
    of a good name... The white-robed cohort of Christ's soldiers is here'; verified directly against
    cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 43650-43661; Latin at cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt,
    lines 124-131 and 142
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks who the confessors were, or about martyrs versus survivors
  - participant asks who had authority besides bishops
  - participant asks whether someone who held firm under arrest could rival a bishop's authority
  prefer_instead:
  - the participant is using confessor in the later sense of a priest who hears confession -- a different
    office entirely -- ask about the later, sacramental sense instead
  - or the participant is asking about a martyr, who died, rather than a confessor, who survived
plain_meaning: For us, a confessor is one who was interrogated for the Name, did not deny it, and lived.
  In Cyprian's time, that standing could rival a bishop's own authority.
world_word: confessor
distortion_risk: high
false_friend:
- a priest whose office is to hear other people's confessions, the later, Western, sacramental sense of
  the word
- a vague honorific for any saintly figure, with no specific claim on church authority attached
senses:
  informational: 'You were taken, you were asked, and you did not say what they wanted. Then, unlike the
    others, you came back. Everyone knows which of us it is, because it happened where people could see.
    What follows is not a quiet honour -- it is a claim. Someone who stood in front of a magistrate and
    held will not easily accept that they have nothing to say about the ones who did not hold, so they
    write letters naming a lapsed person who may come back, and the people named expect to be received.
    Against that stands the conviction that the church''s own peace is not any one person''s to give out
    of their own suffering, however real. Both positions are held in earnest, and this is our named tension
    point: the reason penitential discipline takes the insistent, repeatedly restated form it does --
    built against a claim that already existed and had to be answered, not invented in a vacuum. It is
    bounded: it belongs to the persecution and does not outlive it.'
  evidential: The Epistles are our primary evidence, including Epistles XX-XXI, whose own title-line the
    Registry gives as 'the confessors'; De Lapsis carries the regulating argument, directly quoted --
    'We look with glad countenances upon confessors illustrious with the heraldry of a good name.' A full
    sweep returns roughly 150 occurrences of 'confessor' in Cyprian's own corpus -- our single most frequent
    crisis-specific term, ahead of communion, schism, and the lapsed individually -- with 128 inside the
    Epistles alone. The evidence base is essentially one Registry row read through one lexicon entry.
  translational: 'A modern listener will almost certainly hear ''confessor'' as a priest who hears confessions
    -- the later, Western, sacramental sense -- or a vague honorific for a saintly figure. We mean the
    opposite direction entirely: not one who hears confession, but one who made confession, under interrogation,
    at real risk, and survived. The word names what was done to us and what we did not say, and it carries
    a claim on the church''s own decisions rather than an office within its ministry.'
quick_meaning: For us, a confessor is someone who was asked to deny the faith, did not, and lived. In
  Cyprian's time, that standing could rival a bishop.
---
Re-derived from Doc_06 SS2.1 (lpclex004, Tier 1, G8 Tensional -- 'Doc_05 SS9.2 names it the ecology's tension point, and it is load-bearing for the two entries above') and Lexicon-Chunks/lpclex004_confessor.md. Relations: five terms per this term's own Related-Terms line.
