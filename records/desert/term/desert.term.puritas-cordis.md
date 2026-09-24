---
id: desert.term.puritas-cordis
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: desert.source.cassian-conferences
  locus: "I.4 ('the end of our profession... is the kingdom of God... but the immediate aim or goal, is purity of heart, without which no one can gain that end' - npnf211 ~line 26109, verified verbatim)"
  license: public-domain
- source_id: desert.source.cassian-institutes
  locus: "IV.43 (the fear-of-the-Lord ladder, passing through purity of heart toward the perfection of apostolic love, ~line 20072, verified verbatim)"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - questions about what all the discipline was FOR, in Cassian's telling
  prefer_instead:
  - do not present as the desert's own Greek vocabulary - this is Cassian's Latin, at the world's edge
relations:
- type: associated-with
  target: desert.term.apatheia
plain_meaning: "Purity of heart: Cassian's Latin name for the goal of this life. He chose it in place of the Greek word apatheia."
world_word: puritas cordis
false_friend:
- a vague devotional phrase
senses:
  informational: "Cassian's rendering of the ascetic goal for his Latin readers, anchored in 'Blessed are the pure in heart': a deliberate substitution for apatheia, whose Stoic sound had become controversial - carrying the same technical content under a scriptural name. It belongs to the tradition's later transmission into Gaul, in the 420s, not to the desert's own Greek-Coptic speech."
  evidential: "Cassian's own Conference I makes purity of heart the immediate goal on which the kingdom-end depends - voiced there as his record of Abba Moses's teaching, not the elder's own verbatim words - and his Institutes' ladder, in Gibson's English rendering, climbs from the fear of the Lord through purity of heart to its own further summit, the perfection of apostolic love. As with everything from Cassian, this is Egyptian teaching remembered and written down decades later, in Latin, for Gaul."
  personal: "As Cassian's elders taught it: everything - fasting, vigils, solitude, labor - is instrument; the one target the eye keeps returning to is a heart clean enough to see God."
  translational: "For a modern hearer this phrase is the desert's own best translation of itself - what apatheia meant without the philosophy: a heart free enough to aim at one thing."
quick_meaning: "Purity of heart - Cassian's name for the one goal all the discipline serves."
distortion_risk: low
---
Re-derived from Doc_06 SS3.2 (Tier 3; tags SC TC PV). Both loci
machine-verified this session against npnf211. Reception-history
status (Cassian at the c. 430 boundary) carried in the informational
sense and the retrieval fence.

Step3a Review Round 1: Finding 1 reworded the evidential sense to drop
"directly verified in the vendored Cassian." Finding 3 corrected the
Conference I line pointer from ~26147 (Chapter V's restatement) to
~26109 (Chapter IV, where the quoted sentence actually sits); the I.4
chapter attribution was already correct.

Step3a Review Round 3, Finding S2: both the locus and the evidential
sense said the Institutes IV.43 ladder ENDS at purity of heart. Reread
against the full chapter (verified again this pass): the actual final
rung is "the perfection of apostolic love"; purity of heart is the
PENULTIMATE step, exactly the immediate-goal-vs-final-end distinction
Conference I already draws elsewhere in this same record. Corrected in
both places so a citation_specificity A / verified-verbatim record
does not misstate what its own verified text says.

Step3a Review Round 4, Finding S3: the evidential sense's "both
checked word for word" was verification-process vocabulary - the
verification status already lives in the confidence block and both
loci ("verified verbatim"); dropped from the sense and replaced with
"in his own words," which does the same descriptive work in register.

Step3a Review Round 5, Finding C1: the informational sense's "this
world's export edge" was build-analytic vocabulary, sibling of the
"compiler screen" family excised elsewhere - reworded to state the
Gaul/420s transmission fact without the label.

Step3a Review Round 5, Finding S4: the Round 4 fix's own "in his own
words" wrongly credited the ladder's English to Cassian/Moses
directly - the fifth consecutive illusory-fix recurrence this lexicon
has caught, and the exact construction Round 4's own Finding C2 had
just removed from antirrhesis in the same commit. Corrected per this
world's Conferences source record's standing rule (a Conferences
quote is voiced as Cassian's record of the elder, never the elder's
own verbatim words) and the Institutes' own English credited to
Gibson's translation, matching antirrhesis's and theoria's sibling
clauses.
