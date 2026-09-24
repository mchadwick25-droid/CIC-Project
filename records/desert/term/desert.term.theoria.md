---
id: desert.term.theoria
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.evagrius-praktikos
  locus: "Praktikos ch. 1 and prologue SS8, VENDORED as of 2026-08-27 - Christianity as ascetical practice, contemplation of nature and theology (ch. 1), and love as the door to knowledge of nature which leads to theology (prologue SS8, desert.quote.the-ladder-from-faith-to-love). The Chapters on Prayer, where the contemplative stage is developed, remains unvendored and consult-only"
  license: cc-by-4.0
- source_id: desert.source.cassian-conferences
  locus: Conf. III ch. VI, the third renunciation and the Song of Songs
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - questions about contemplation or the higher reaches of prayer
  prefer_instead:
  - questions about ordinary daily prayer across the movement - the Psalter, not this term, is that answer
relations:
- type: associated-with
  target: desert.quote.the-ladder-from-faith-to-love
- type: associated-with
  target: desert.term.apatheia
- type: associated-with
  target: desert.term.logismoi
- type: associated-with
  target: desert.gravity.evagrian-systematization
plain_meaning: "Contemplation: in Evagrius's scheme, the seeing of God and of things in God that only a stilled soul reaches."
world_word: theoria
false_friend:
- theory (abstract speculation)
senses:
  informational: "The final stage of Evagrius's scheme - after the practical life, after passionlessness - contemplation, itself graded from the contemplation of created things up to the contemplation of God. The vocabulary of Kellia's learned circle, concentrated in one author; the wider movement prayed the Psalter without this ladder."
  evidential: "Rests on Evagrius's own writings. The historian Socrates, in Zenos's English rendering, names his works and quotes some of his practical sayings, but not this contemplative stage's own teaching; no English of that teaching can be quoted here directly. The wider, non-Evagrian movement's own record has nothing like this ladder at all."
  personal: "Not thinking about God - seeing, in the way a long-trained eye sees. The tradition insisted no one starts here; wanting the summit without the slope was itself one of the thoughts to be fought."
  translational: "'Theory' is the false friend: this is perception, not speculation - the trained sight of a life that has first been stilled."
quick_meaning: "Contemplation - the trained seeing of God that a stilled life may reach."
distortion_risk: high
---
Re-derived from Doc_06 SS2.3 (Tier 2; tags AS TC DR PV;
strand-C-bound, single-author-concentrated per Doc_03 SS1.7/Doc_04
SS3). Serves F4-I (why and how did you pray) for the Strand C register
specifically; the whole-movement prayer answer is the Psalter (carried
by story/ambient material, not this term).

Step3a Review Round 1, Finding 1: reworded the evidential sense to
drop corpus-management vocabulary (vendored/consult-only/directly
checkable) in favor of in-world evidence talk.

Step3a Review Round 2, New Finding 1: the Round 1 rewrite had
overclaimed that Socrates's excerpts make "this stage's teaching"
(contemplation) checkable in English - verified against the vendored
Socrates IV.23 extract in full, which contains Evagrius's practical
sayings and no contemplation doctrine at all. Corrected to state
accurately what the excerpt does and does not cover.

Step3a Review Round 3, Findings S1/J4/C1: the Round 2 fix itself said
the contemplative teaching "stays untranslated," which is false and
contradicted by this world's own Evagrius source record (Bamberger's
1970 English of the Praktikos and Chapters on Prayer exists,
copyrighted, consult-only - not untranslated); it also swapped one
review-process phrase Round 2 had itself flagged as borderline
("a tested finding") for a stronger one ("checked directly against...
sources"). Reworded a third time, checked against the Evagrius source
record's actual edition list, without process language: what Socrates
gives in English is the works named and a few practical sayings, not
this stage's own teaching; the strand-bound claim rests on the wider
movement's own record having no comparable ladder, not on a review
verb. The English attribution is now credited to Zenos's translation,
not to Socrates himself.

Step3a Review Round 4, Findings S1/S4: (1) the informational sense's
"Strand C's vocabulary" used this build's own lettered taxonomy with
no legend in the field - reworded to name Kellia's learned circle.
(2) the Round 3 fix's own "exists in English only in modern,
copyrighted translation" introduced licensing vocabulary into the same
clause, inconsistent with apatheia's sibling clause (fixed the same
round to avoid exactly this) - reworded to state the fact (no English
of the teaching can be quoted here) without naming the reason. On a
second, self-checked pass this same fix's own "genuinely checked" was
caught and removed before this commit - the identical review-process
register the rest of this note is about, introduced and caught within
one editing pass rather than surviving to a Round 5.
