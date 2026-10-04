---
id: don.story.acta-purgationis-felicis
world_id: donatism
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-E
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Documented: a formal judicial verdict, ordered by the emperor, conducted by a named
    proconsul, with named deponents on record and a confession obtained under threat of torture. The confession
    was extracted under that threat, which is stated here rather than left implicit - a modern reader is
    entitled to weigh what that does to its reliability, and this record does not treat torture-adjacent
    testimony as though it were free testimony. The proceeding is preserved inside Optatus''s own appendix
    and its outcome is unfavourable to our founding accusation, which is the honest position and is not
    reframed.'
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: Acta Purgationis Felicis (314/315); cic/texts/optatus_against-the-donatists.txt, Appendix I, lines
    5467-5585
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how the traditio accusation against Felix of Aptungi - the root of the whole dispute
    over Caecilian's legitimacy - was actually investigated
  - participant asks for the strongest documented evidence on the founding legal question
  - participant asks directly whether the case against Felix held up
  prefer_instead:
  - participant is asking about the Lucilla and treasury strand - don.story.lucilla-affair and don.story.gesta-apud-zenophilum
    cover that
  - participant wants why the traditio question mattered doctrinally rather than what one inquiry found
    about one man
relations:
- type: associated-with
  target: don.figure.felix-of-aptungi
- type: associated-with
  target: don.figure.caecilian
- type: associated-with
  target: don.figure.constantine
- type: associated-with
  target: don.figure.optatus-of-milevis
narrative_tier: 1
narrative_tier_justification: Tier 1 of the strongest kind available in this corpus - a formal judicial
  proceeding, ordered by the emperor himself, conducted by a named Roman official, with named deponents
  testifying on record, producing a documented confession and a stated verdict. Every element of the definition
  is satisfied at full strength. The caveat Tier 1 asks for the author's perspective and genre applies
  in a specific and unusual direction here, and is stated rather than smoothed - the proceeding survives
  because Optatus included it in his own appendix, and its outcome tells against our founding accusation.
  That placement does not make the record less credible as a judicial document; a forged-letter confession
  under threat of torture is not the sort of detail a hostile compiler would need to invent, and its presence
  in the opponent's own dossier argues for its reliability rather than against it. What it does mean is
  that this is a documented setback, and a Representative carrying it should say so.
tellable_as: An imperial inquiry into whether the bishop who consecrated Caecilian had handed over the
  scriptures ends with a notary confessing, under threat of torture, that he forged the letter proving
  it - and that he did it working for our side.
text: >-
  The whole schism turns, at its root, on a single accusation: that
  Felix, the bishop of Aptungi who consecrated Caecilian as bishop of
  Carthage, had himself been a traditor - that he had handed over the
  scriptures during the persecution, and so had no standing to consecrate
  anyone, which would make Caecilian's office invalid from its first day.

  Constantine ordered the matter investigated. The proconsul Aelianus
  opened a formal inquiry and took testimony on record from named
  witnesses: Alfius Caecilianus, Maximus, Apronianus, Claudius
  Saturianus, Superius, and a notary named Ingentius. At the centre of
  the case was a letter, supposedly written by Felix himself and read
  aloud in the proceeding, that seemed to prove the accusation.

  Under questioning, and under the threat of torture, Ingentius broke. He
  confessed that he had forged the letter himself, and that he had done
  it as an agent working for our party, moving through Numidia and
  Mauritania in that service. With the forgery exposed, the case against
  Felix collapsed. The proceeding records his vindication as complete -
  finally and triumphantly, in the text's own words.
absent_detail: Nothing survives of what Felix himself said, or of what Ingentius said before the threat
  was made. No account of this inquiry from our own side exists at all - not a defence of the accusation,
  not a challenge to the proceeding, not an explanation of who sent Ingentius or on whose authority.
modern_contrast: >-
  A modern reader will reach immediately for the fact that the confession
  came under threat of torture, and should. That is a real reason to hold
  the finding loosely, and it is not the reason our own tradition
  eventually gave for holding it loosely - which was, rather, that the
  wider traditio dispute involved far more people and incidents across
  that founding decade than this one proceeding settles, and that the
  principle at stake did not stand or fall on one man's case. Both things
  can be said at once. What cannot honestly be said is that the inquiry
  found in our favour.
use_note:
  means: "An inquiry into whether Felix of Aptungi handed over the scriptures ended with a notary confessing, under threat of torture, that he forged the letter for the Donatist side."
  not_for:
    - "a claim that the inquiry settled the wider traditio dispute"
    - "a claim that an account of the inquiry from the Donatist side survives"
  years: {from: 314, to: 315}
  status: provisional
---
Compiled from World-Builds/Donatism/Story-Chunks/donstory006_acta-
purgationis-felicis.md (Doc_09 story index row donstory006, Tier 1),
whose narrative text is carried forward rather than re-derived.

THE UNFAVOURABLE FINDING IS THE POINT OF KEEPING THIS RECORD. Doc_09
leaves standing (L2) the chunk's own handling of Ingentius's
torture threat; this record keeps it and adds it to modern_contrast,
where a modern reader's first objection belongs. The story must not be
retrieved defensively. A Representative asked directly how strong the
case against Felix was should reach this record and say what it found.

TWO NAMED FELIXES - see don.story.lucilla-affair's own body note and
don.figure.felix-of-aptungi. The deacon Felix who hides in Mensurius's
house in the Lucilla story is a different man entirely.

TWO NAMED CAECILIANS, ALSO IN THIS STORY. Alfius Caecilianus, the first
deponent named above, is not Caecilian of Carthage, the bishop whose
consecration is what the inquiry is about. The transcript names both
within a few lines of each other.
