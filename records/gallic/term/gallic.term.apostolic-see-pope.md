---
id: gallic.term.apostolic-see-pope
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice in referent: Vincent's "Apostolic See" is Rome (Lerins); Cassian's "Pope" is a
    Gallic bishop - Castor of Apta Julia, Leontius (Marseilles). The two do not conflict, because
    the word is a title in one and a see in the other. The Marseilles resistance to Celestine's
    letter ("clung to their views in spite of the authority of the Pope") is known only at editorial
    strength, through Gibson's prolegomena. Latin papa is supplied by Gibson's editorial footnote,
    which itself states the title "was not limited to the Bishop of Rome till a later date."
    Sulpitius calls Liberius simply "bishop of the city of Rome," in a chapter located by grep and
    not read in full.
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Preface ("most blessed Pope Castor" - Gibson''s footnote on Papa is editorial); V.1 ("O most blessed Pope Castor, more than ever")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Preface I ("blessed Pope, Leontius"); X.1 ("the commands of Pope Castor of blessed memory, and your wishes, O blessed Pope Leontius and holy brother Helladius")'
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 6 [15-16] ("Pope Stephen of blessed memory, Prelate of the Apostolic See"; "Let there be no innovation"); ch. 32 [84] ("the twofold authority of the Apostolic See, first, that of holy Pope Sixtus")'
  license: public-domain
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.39 ("Liberius, too, bishop of the city of Rome") - located by grep; not read in full'
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: 'Gibson''s prolegomena on Celestine''s letter to the Gallican bishops ("Venerius of Marseilles"; "clung to their views in spite of the authority of the Pope") - editorial transmission history'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether these writers recognized the Pope
  - why Cassian calls a Provencal bishop "Pope"
  - what "Apostolic See" means in Vincent
  - how Rome related to the grace argument
  - participant uses "Pope," "papacy," "Rome," "Apostolic See," "papal authority"
  - Comm. ch. 6 and ch. 32; Inst. Preface's dedication; Celestine's letter to the Gallican bishops
  prefer_instead:
  - the question is about bishops in general (retrieve bishop / the monk-bishop)
  - the question is about councils (retrieve council / synod)
  - the papacy as a later constitutional office - the title's later restriction to Rome is exactly the hearing this entry corrects
  - Celestine's letter's content - known here only through an editor's prolegomena
relations:
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.apostolic-authority
- type: associated-with
  target: gallic.term.massilians
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
plain_meaning: >-
  "Pope" is a title of honour we give to bishops we revere - Cassian's Pope Castor of Apta Julia.
  "The Apostolic See" is Vincent's Rome, foremost in refusing novelty. Not the same relation.
world_word: Apostolic See / "Pope" (papa) as address
false_friend:
- '"Pope" as the bishop of Rome exclusively, with the later constitutional office read back'
- Vincent as a proof-text for papal supremacy
- Cassian's "Pope Castor" as an error
senses:
  informational: >-
    Cassian's books are written to Popes who are bishops of Provence. The Institutes open to "most
    blessed Pope Castor," at whose request they were written for his new monastery; the first
    Conferences honour "Pope Castor of blessed memory" and "blessed Pope Leontius and holy brother
    Helladius." The word is what one calls a bishop one reveres. The same word in Vincent's mouth
    belongs to Rome, and to Rome as the keeper of antiquity: Pope Stephen, "Prelate of the Apostolic
    See," resisted rebaptism with the rule "Let there be no innovation - nothing but what has been
    handed down"; and Vincent closes his case with "the twofold authority of the Apostolic See,"
    Sixtus and Celestine. Rome's weight, for Vincent, is that it was foremost in refusing novelty.
    In the same decade, on the editor's account, the Marseilles clergy to whom Celestine wrote
    "clung to their views in spite of the authority of the Pope."
  evidential: >-
    Both usages are directly attested: Cassian (Inst. Preface, V.1; Conf. Preface I, X.1) and
    Vincent (Comm. 6, 32). The Marseilles resistance to Celestine is known only through Gibson's
    editorial prolegomena. Sulpitius's one reference calls Liberius "bishop of the city of Rome,"
    one bishop among those the Arians exiled.
  personal: >-
    "Pope Castor" is not a slip; it is how we address a bishop we love. Rome is invoked at Lerins
    as antiquity's guardian and, in the same years, resisted at Marseilles on that very account.
    Vincent's Rome and Cassian's Rome are not the same relation, and we do not pretend they are.
  translational: >-
    A modern hearer hears "Pope" and thinks of one office in one city. Among us the title was a
    Western bishop's honour, and Rome's claim, when Vincent makes it, is that its bishops were
    foremost in guarding what was handed down - not a constitutional supremacy read back from later
    centuries.
quick_meaning: >-
  "Pope" is how we honour any revered bishop - Cassian writes to Pope Castor of Provence. "The
  Apostolic See" is Vincent's Rome, weighty because it refused novelty. Two words, two relations.
distortion_risk: high
---
Built from Doc_06 entry 062 (`galliclex062_apostolic-see-pope.md`, Tier 2, tags SC DR TC; Doc_03
7.12). The two referents are kept apart in every field per the chunk's voice note; the
editorial-strength status of the Marseilles resistance to Celestine is stated in divergence_note.
canon_cells: F3-T because "did you recognize the Pope?" is the form the "is there a church today
that's yours?" question takes for this world.

Related-Terms also names bishop / the monk-bishop, the rule, novelty vs. antiquity, the Fathers /
elders, grace (of God), and the customs of the monasteries / Institutes - cross-batch at authoring
time, added as relations (typed associated-with) at the reconciliation pass once all 81 term records
existed. The chunk also names heretic / heresy (in-batch); not made a relation, since no dependency
is stated.
