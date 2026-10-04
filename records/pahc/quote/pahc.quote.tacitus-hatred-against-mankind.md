---
id: pahc.quote.tacitus-hatred-against-mankind
world_id: post-apostolic-house-church
record_type: quote
schema_version: 2
status: ready
register: etic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented FOR THE TEXT. That Tacitus wrote this is not seriously disputed. WHETHER A DISCRETE,
    FIRE-LINKED PERSECUTION OF CHRISTIANS AS A NAMED GROUP HAPPENED IN 64 IS A LIVE, NON-FRINGE
    DISPUTE (Brent Shaw against Christopher Jones), and quoting the passage settles nothing about
    it - Shaw's case is precisely that Tacitus, writing c. 116, retrojected a later and more
    general memory onto the fire. A record using this quote must carry that and must not let the
    verbatim wording stand in for the event. The translation is the one standardly identified as
    Church and Brodribb (1876); the vendored file's own text names no translator, and the
    attribution is made on internal evidence, stated in its header.
sources:
- source_id: pahc.source.tacitus-annals
  locus: >-
    Annals 15.44, in the translation standardly identified as Church and Brodribb (1876)
    (cic/texts/tacitus_annals-15-44_church-brodribb1876.txt)
  license: public-domain
text: >-
  Consequently, to get rid of the report, Nero fastened the guilt and inflicted the most exquisite
  tortures on a class hated for their abominations, called Christians by the populace. Christus,
  from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at
  the hands of one of our procurators, Pontius Pilatus, and a most mischievous superstition, thus
  checked for the moment, again broke out not only in Judaea, the first source of the evil, but
  even in Rome, where all things hideous and shameful from every part of the world find their
  centre and become popular. Accordingly, an arrest was first made of all who pleaded guilty; then,
  upon their information, an immense multitude was convicted, not so much of the crime of firing
  the city, as of hatred against mankind.
modern_rendering: >-
  So, to get rid of the rumor, Nero blamed a group hated for their vile acts. The people
  called them Christians. He put them through the most exquisite tortures. Christus, from
  whom the name came, was executed under Tiberius. One of our governors, Pontius Pilate,
  carried out the execution. This harmful superstition was checked for a moment. But it
  broke out again. It broke out not only in Judea, where the evil began, but even in Rome.
  In Rome, every horrible and shameful thing from the whole world gathers and becomes
  popular. So those who confessed were arrested first. Then, from their information, a
  huge number were convicted. They were convicted not so much for burning the city as for
  hatred of mankind.
speaker_or_author: Tacitus, in the Annals
license: verbatim
modern_lens_note: >-
  Two things a modern reader is likely to mis-hear. "Superstition" (superstitio) is not credulity
  here; in Roman usage it is a foreign, excessive and socially corrosive religious practice, the
  opposite of religio, which is the ancestral kind - the charge is disloyalty, not silliness. And
  "hatred against mankind" (odium humani generis) is a specific accusation about withdrawal from
  the ordinary religious life of the city, not a claim that Christians were personally malicious.
  Note also what Tacitus does NOT say: he does not say they set the fire. He says they were
  convicted of something else instead.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether it was really dangerous to be a Christian"
  - "participant asks what a Roman writer said about them and why they were disliked"
  - "participant asks whether they were blamed for things they had not done"
relations:
- type: associated-with
  target: pahc.story.nero-scapegoating
- type: associated-with
  target: pahc.force.neronian-persecution
- type: illustrates
  target: pahc.gravity.state-pressure
use_note:
  means: "Tacitus, writing about fifty years later, says Nero blamed Christians for Rome's fire and convicted many less for arson than for hatred of mankind."
  not_for:
    - "proof that a discrete, fire-linked persecution of Christians as a named group happened in 64"
    - "a claim that Tacitus says Christians set the fire"
    - "a claim that Christians were personally malicious rather than charged with withdrawal from civic religion"
    - "a claim about what Romans called the group, resting on this translation's spelling"
  years: {from: 110, to: 120}
  status: reviewed
---
Text is verified verbatim against the vendored file.

This world had carried Tacitus since the prior build as a
paraphrase-only row, because no public-domain English was in the corpus.
pahc.story.nero-scapegoating said so in its own divergence_note and told
the event in paraphrase for that reason. It can now be quoted.

WHAT IS VENDORED IS ONE CHAPTER, 375 words. Nothing here reaches the rest
of the Annals, which is not in this corpus.

The Medicean manuscript reads "chrestianos", corrected by a later hand to
"christianos". This English prints "Christians" and gives no note. No
claim about what Romans actually called this group may rest on the
spelling in this quote.
