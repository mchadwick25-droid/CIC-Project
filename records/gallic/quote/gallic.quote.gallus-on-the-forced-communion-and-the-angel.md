---
id: gallic.quote.gallus-on-the-forced-communion-and-the-angel
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-P
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text (Dialogues III.12-13, read at its locus for this
    record). Widely Accepted at the narrative level. Contested for the angel's speech and for the
    diminution of power specifically - these are Martin's own reported experience ("he at once confessed
    to us with tears"), transmitted by Gallus and carried at Contested strength as the tradition's own
    self-understanding, not as independently established fact.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.12-13 (npnf211 divs ii.iv.iii.xii-xiii, file lines 5145-5219): the bishops' terror before Maximus, the executioners appointed, Martin's night plea, the forced communion at Felix's ordination, the mourning at Andethanna, the angel's rebuke, and the diminished power that followed"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what happened after Martin's plea, whether he actually took communion with the Ithacians, or what the angel said to him"
  - "participant asks why Martin never attended a synod again, or what it cost him to compromise"
  - "conversation reaches a bishop's power being weakened by a wrong he judges himself to have shared in"
  prefer_instead:
  - "participant is asking what Martin originally petitioned for at Treves, before the communion - retrieve gallic.quote.gallus-on-the-tribunes-for-the-spains"
  - "participant is asking about Martin's healing power in general rather than its one attested loss - retrieve gallic.story.raising-of-the-catechumen or gallic.term.virtus"
text: >-
  In the meantime, those bishops with whom Martin would not hold communion went in terror to the king,
  complaining that they had been condemned beforehand; that it was all over with them as respected the
  status of every one of them, if the authority of Martin was now to uphold the pertinacity of
  Theognitus, who alone had as yet condemned them by a sentence publicly pronounced; that the man ought
  not to have been received within the walls; that he was now not merely the defender of heretics, but
  their vindicator; and that nothing had really been accomplished by the death of Priscillian, if Martin
  were to act the part of his avenger. Finally, prostrating themselves with weeping and lamentation, they
  implored the emperor to put forth his power against this one man. And the emperor was not far from
  being compelled to assign to Martin, too, the doom of heretics. But after all, although he was disposed
  to look upon the bishops with too great favor, he was not ignorant that Martin excelled all other
  mortals in faith, sanctity, and excellence: he therefore tries another way of getting the better of the
  holy man. And first he sends for him privately, and addresses him in the kindest fashion, assuring him
  that the heretics were condemned in the regular course of public trials, rather than by the
  persecutions of the priests; and that there was no reason why he should think that communion with
  Ithacius and the rest of that party was a thing to be condemned. He added that Theognitus had created
  disunion, rather by personal hatred, than by the cause he supported; and that, in fact, he was the only
  person who, in the meantime, had separated himself from communion: while no innovation had been made by
  the rest. He remarked further that a synod, held a few days previously, had decreed that Ithacius was
  not chargeable with any fault. When Martin was but little impressed by these statements, the king then
  became inflamed with anger, and hurried out of his presence; while, without delay, executioners are
  appointed for those in whose behalf Martin had made supplication. When this became known to Martin, he
  rushed to the palace, though it was now night. He pledges himself that, if these people were spared, he
  would communicate; only let the tribunes, who had already been sent to the Spains for the destruction
  of the churches, be recalled. There is no delay: Maximus grants all his requests. On the following day,
  the ordination of Felix as bishop was being arranged, a man undoubtedly of great sanctity, and truly
  worthy of being made a priest in happier times. Martin took part in the communion of that day, judging
  it better to yield for the moment, than to disregard the safety of those over whose heads a sword was
  hanging. Nevertheless, although the bishops strove to the uttermost to get him to confirm the fact of
  his communicating by signing his name, he could not be induced to do so. On the following day, hurrying
  away from that place, as he was on the way returning, he was filled with mourning and lamentation that
  he had even for an hour been mixed up with the evil communion, and, not far from a village named
  Andethanna, where remote woods stretch far and wide with profound solitude, he sat down while his
  companions went on a little before him. There he became involved in deep thought, alternately accusing
  and defending the cause of his grief and conduct. Suddenly, an angel stood by him and said, "Justly, O
  Martin, do you feel compunction, but you could not otherwise get out of your difficulty. Renew your
  virtue, resume your courage, lest you not only now expose your fame, but your very salvation, to
  danger." Therefore, from that time forward, he carefully guarded against being mixed up in communion
  with the party of Ithacius. But when it happened that he cured some of the possessed more slowly and
  with less grace than usual, he at once confessed to us with tears that he felt a diminution of his
  power on account of the evil of that communion in which he had taken part for a moment through
  necessity, and not with a cordial spirit. He lived sixteen years after this, but never again did he
  attend a synod, and kept carefully aloof from all assemblies of bishops.
speaker_or_author: "Gallus, Martin's disciple, narrating within Sulpitius Severus's Dialogues (Book III), quoting an angel's words to Martin"
license: verbatim
modern_lens_note: >-
  Martin does not celebrate the outcome. He gets the tribunes recalled, but Gallus's account gives equal
  weight to what it cost him: a communion he could not bring himself to sign his name to, a private
  breakdown in the woods, and an angel's answer that does not absolve the choice so much as insist he
  could not have done otherwise - "you could not otherwise get out of your difficulty." The diminished
  healing power that follows, reported years later "with tears," and the sixteen years he then spends
  avoiding every synod, read this one yielding as a wound rather than a victory.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.story.trier-and-the-ithacian-communion
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "went in terror to the king"`
returns one hit, line 5146; `grep -n "kept carefully aloof"` returns one hit, line 5218. The divs are
`<div4 title="Chapter XII." ... id="ii.iv.iii.xii">` (line 5141) and `<div4 title="Chapter XIII." ...
id="ii.iv.iii.xiii">` (line 5180). The quoted span runs continuously from "In the meantime, those bishops
with whom Martin would not hold communion went in terror to the king" (line 5145) through "...kept
carefully aloof from all assemblies of bishops." (line 5219) - the whole of Chapters XII and XIII, with no
material omitted.

Normalization: hard-wrapped lines joined with single spaces. The source sets the angel's speech in curly
single quotation marks ('Justly, O Martin...'); these are rendered here as straight double quotation
marks to distinguish the angel's own words from the surrounding narration, consistent with how this
record's sibling (gallic.quote.martin-on-the-christ-with-wounds) treats an embedded speech inside a
narrator's frame. No word was added, dropped, substituted, or reordered.

speaker_or_author names both the narrating voice (Gallus) and that the passage itself quotes a second
speaker, the angel, whose words are given as Gallus reports them - not converted to indirect speech,
since the angel's exact wording is what the host story and this record both carry as load-bearing.
