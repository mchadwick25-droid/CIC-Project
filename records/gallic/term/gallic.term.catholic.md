---
id: gallic.term.catholic
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-T
- F2-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    No Author Gravity as a word - all three founding voices, both nodes (Vincent's faith, Cassian's
    "approved Catholic fathers" and "Catholic rule" of custom, Sulpitius's party name against the
    Priscillianists). The definition - "comprehends all universally"; "everywhere, always, by all"
    - is Vincent's alone. "Roman Catholic" is a modern-hearing gap carried as distortion risk, not
    as a recorded live contest (Doc_06 section 3; no CT tag). No Latin lemma sought; Vincent's own
    Latin for "rule" is not given in the vendored translation.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 2 [4-6] ("the truth of Catholic faith from the falsehood of heretical pravity"; "everywhere, always, by all"; "comprehends all universally"; "universality, antiquity, consent"); ch. 3 [7] ("the communion of the universal faith"); ch. 9 [26] (the Pelagians "to Catholics"); ch. 20 [48] ("he is the true and genuine Catholic who ...")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'I.2 ("the Catholic rule. For the opinion of a few ought not to be preferred")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'I.20 ("the approved Catholic fathers")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'XIII.5, 18 ("the value of the Catholic faith"; "all the Catholic fathers")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.7 ("the need of the Catholic faith compelled me to visit")'
  license: public-domain
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.51 ("revolted from the Catholics") - II.46-51 only read'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what "Catholic" meant to these writers
  - whether they were "Roman Catholics"
  - how one told a Catholic from a heretic
  - why Cassian calls a monastic custom "Catholic"
  - participant uses "Catholic," "catholicity," "universal," "orthodox," "the Church"
  - Vincent's definition; "the approved Catholic fathers"; Inst. I.2's "Catholic rule"; the Priscillianists' revolt "from the Catholics"
  prefer_instead:
  - the question is about the rule itself (retrieve the rule)
  - the question is about the axis of novelty and antiquity (retrieve novelty vs. antiquity)
  - the question is about the Roman see (retrieve Apostolic See / Pope)
  - later confessional identity, which we do not have
relations:
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.tradition
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
- type: tension-with
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.the-deposit
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.apostolic-see-pope
- type: associated-with
  target: gallic.term.anathema
plain_meaning: >-
  What "comprehends all universally" - the faith believed everywhere, always, by all. A rule of
  the many and the old against the few and the new, not a confession.
world_word: Catholic ("the Catholic faith"; "true and genuine Catholic")
false_friend:
- '"Roman Catholic" - a confession, a denomination, or a communion under the bishop of Rome, contrasted with "Protestant" or "Orthodox"'
senses:
  informational: >-
    Vincent's whole book answers one question: by what "universal rule" may one "distinguish the
    truth of Catholic faith from the falsehood of heretical pravity"? The answer defines the word by
    its meaning: we hold "that faith which has been believed everywhere, always, by all. For that
    is truly and in the strictest sense 'Catholic,' which ... comprehends all universally. This rule
    we shall observe if we follow universality, antiquity, consent." A Catholic is therefore a kind
    of person - one who resolves to believe "that, and that only, which he is sure the Catholic
    Church has held universally and from ancient time." Cassian uses the word of the same authority
    in a monk's room: a thought is tested for the stamp of "the approved Catholic fathers"; a
    garment is rejected as "not in accordance with the Catholic rule. For the opinion of a few ought
    not to be preferred." At Tours it is a party name: Priscillian's clergy "revolted from the
    Catholics."
  evidential: >-
    Attested in all three founding voices: Vincent (Comm. 2, 3, 9, 20), Cassian (Inst. I.2; Conf.
    I.20, XIII.5, XIII.18, XVIII.7), Sulpitius (Sacred History II.51). The word is shared; the
    definition is Vincent's alone.
  personal: >-
    One word, three rooms - a rule, a stamp, a side - and in each the same test of the many and
    the old against the few and the new. A Gallic monk could call a girdle "Catholic" and mean what
    Vincent means by the faith.
  translational: >-
    A modern hearer hears "Roman Catholic" - a denomination set against Protestant or Orthodox. We
    had no confessions to be set against. "Catholic" for us is defined by a rule - universality,
    antiquity, consent - and applied to a monastic custom as readily as to the faith.
quick_meaning: >-
  The faith "believed everywhere, always, by all." For us a rule, not a confession. The test is
  what all held, from of old, by consent. Cassian even calls a monk's custom "Catholic."
distortion_risk: high
---
Built from Doc_06 entry 055 (`galliclex055_catholic.md`, Tier 2, tags SC DR TC RT; Doc_03 7.1).
Pruned from Doc_03's Tier-1 estimate at Doc_06 section 2.3 (its defining content is the rule).
The "Roman Catholic" hearing is carried as the single false_friend and distortion_risk: high,
not as a CT (Doc_06 section 3).

Relation typing: `tension-with` gallic.term.heretic-heresy (its opposite, per the chunk).

Related-Terms also names the rule, novelty vs. antiquity, the Fathers / elders, tradition, grace (of
God), and the customs of the monasteries / Institutes - cross-batch at authoring time, added as
relations (typed associated-with) at the reconciliation pass once all 81 term records existed. The
chunk also names Pelagians as foil (in-batch); not made a relation, since no dependency is stated
beyond the Pelagians' address "to Catholics."
