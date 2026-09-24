---
id: witt.contested.1543-treatise-later-effect
world_id: lutheran-wittenberg-and-its-congregations
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: >-
    Contested at the scholarly level, and doubly so at this build's own remove: neither pole is read from
    its own primary monograph, only from a tertiary intermediary (the Wikipedia article) and, for
    Kaufmann, from published reviews of the 2017 study rather than the study itself. That two-hop distance
    is disclosed on both source records this claim rests on and is not smoothed over here.
sources:
- source_id: witt.source.thomas-luthers-jews-a-journey-into-anti
  locus: "Kaufmann, Luther's Jews: A Journey into Anti-Semitism (Oxford, 2017; German 2014) - 'the current
    specialist treatment... reads the 1543 text as continuous with, not a reversal of, Luther's earlier
    views' (Doc_02 SS12.3); named via the Wikipedia article's own bibliography and published reviews, not
    read directly"
  license: public-domain
- source_id: witt.source.johannes-reception-of-luthers-writings
  locus: "Wallmann, 'The Reception of Luther's Writings on the Jews from the Reformation to the End of the
    19th Century' (Lutheran Quarterly n.s. 1, no. 1, Spring 1987, 72-97) - the treatise 'was in fact
    largely ignored during the 18th and 19th centuries' (Doc_02 SS12.3, quoting the Wikipedia article's own
    summary of Wallmann); named via the same bibliography, not read directly"
  license: public-domain
- source_id: witt.source.wikipedia-on-the-jews-and-their-lies
  locus: "The tertiary intermediary through which both poles reach this library - Doc_02 SS12.3's own
    disclosed basis for the whole debate, 'not from the primary text' on either side"
  license: public-domain
relations:
- type: associated-with
  target: witt.force.absent-inputs-1525-and-1555
claim: >-
  The 1543 treatise Von den Juden und ihren Lügen represents genuine continuity with the founder's own
  earlier antisemitic tendencies and was a real historical contributor to the development of modern German
  antisemitism - not a marginal or forgotten text, but one whose influence reached forward into the
  centuries that followed it.
held_against:
- >-
  A named, specialist counter-reading holds the opposite historical-effect claim: Wallmann's 1987 study of
  the treatise's own reception history across the 18th and 19th centuries concludes it "was in fact largely
  ignored" through most of that span - real, documented, but not the ongoing influence the continuity
  reading asserts. If Wallmann is right, the treatise's later effect was episodic and largely dormant for
  two full centuries, not a continuous throughline from 1543 to the modern era.
- >-
  Neither side of this contest has been read by this build from its own primary text. Kaufmann's 2017
  monograph and Wallmann's 1987 article both reach this library only through a tertiary intermediary (the
  Wikipedia article) and, for Kaufmann, through published reviews of the study rather than the study
  itself (Doc_02 SS12.3). "Contested" here means, precisely: two named scholarly positions exist and
  disagree, at a remove this build has not closed by reading either one directly - not that this build has
  weighed their evidence and found them evenly matched.
- >-
  The question this claim actually asks - what the treatise DID, historically, after 1543 - is a different
  and harder question than what the treatise SAYS. This world's own records are firm on the second (the
  treatise's own seven-point programme, tertiary-sourced but Widely Accepted as to content, disclosed at
  witt.source.luther-von-den-juden-und-ihren-l and witt.force.absent-inputs-1525-and-1555) and silent on the
  first. A downstream effect on later centuries is not established or refuted by anything this library holds
  about the treatise's own 1543 content.
concedes: >-
  Not contested: that Luther wrote and published the treatise in 1543; that it is real, part of this
  world's own history, and not smoothed over or denied; that it recommends a programme against the Jews
  (Widely Accepted as to content, from tertiary sourcing, per Doc_02 SS12.3); and that serious scholarship
  exists and disagrees about what happened to the text's influence after Luther's own lifetime. What is not
  settled from this library: whether the treatise's later historical effect was one of substantial
  continuity into modern antisemitism, or one of long dormancy followed by later rediscovery - and, per
  this world's own Standing determination (Doc_07 SS9/SS12 item 7, Doc_08 SS11 item 7), this is not a
  question the Representative's own voice answers either way; the treatise's content and its downstream
  effect alike are Facilitator-carried disclosure, never Representative-voiced argument. This record exists
  so the contest is written down rather than left as a silence a Representative-voice answer could
  otherwise fill by default.
---
Authored per the go-live adversarial review's M-3 finding: `witt_Doc_02_Source_Ecology.md`
SS12.3 tags the 1543 treatise's later historical effect `[Contested]` and names the dispute specifically
(Kaufmann continuity vs. Wallmann largely-ignored), but no `contested_claim` record existed for it - the
three lower-stakes contests already built (household-catechism-reception, justification-accounted-and-made,
theses-door-posting) left this, the highest-stakes one, as a silence. CLAUDE.md: "Contested or uncertain
claims get tagged with the project's five-level confidence vocabulary... with a `contested_claim` record
where warranted. Never present a disputed claim as settled."

Not compiled into any package (gravity/force/contested_claim/search_record/source are not compiled types,
per engine/m1/gates.py's own comment) - this is scholarly apparatus, not participant-facing content, and
closing this gap changes nothing about what a Representative can say. Its purpose is the one CLAUDE.md
states: so this world's own record shows the contest was seen and written down, not settled by silence, if
B-1 and B-2 are ever both resolved such that this topic reaches a participant.

Sourcing built entirely from three source records already authored and verified at their own authoring
passes (`witt.source.thomas-luthers-jews-a-journey-into-anti`, row 75; `witt.source.johannes-reception-of-
luthers-writings`, row 92; `witt.source.wikipedia-on-the-jews-and-their-lies`, row 83) - not independently
re-opened against any primary text by this record, since neither Kaufmann's nor Wallmann's own monograph
is vendored or has been read by any pass of this build. The two-hop remove (primary text -> tertiary
Wikipedia summary -> this record) is stated on the record's own face (`divergence_note`, `held_against`
item 2) rather than smoothed into an ordinary `Contested` tag that would read as though both positions had
been weighed directly.

`relations` links to `witt.force.absent-inputs-1525-and-1555` - the one existing witt record that already
engages the 1543 treatise as its own subject at any depth - rather than to a gravity or term record, since
no gravity or term record in this world is about the treatise itself. Reciprocal `associated-with` declared
on that force record's own frontmatter in the same edit, per this world's own `gate_reciprocity`
discipline.
