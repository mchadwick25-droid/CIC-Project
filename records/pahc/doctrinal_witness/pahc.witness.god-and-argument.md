---
id: pahc.witness.god-and-argument
world_id: post-apostolic-house-church
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: pahc.source.justin-first-apology
  locus: "46 (the Logos present in 'every race of men')"
  license: public-domain
- source_id: pahc.source.first-clement
  locus: "42, 44 (the authority dispute at Corinth)"
  license: public-domain
- source_id: pahc.source.ignatius-letters
  locus: "passim (the monarchical-bishop program)"
  license: public-domain
- source_id: pahc.source.anti-montanist-fragments
  locus: "the synodical opposition of Asia Minor's churches, near this world's own closing edge"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what this world believed about God"
  - "participant asks what this world argued about among itself"
  - "participant asks about church councils"
relations:
- type: associated-with
  target: pahc.quote.those-who-lived-reasonably-are-christians
- type: associated-with
  target: pahc.contested.two-strand-packaging
- type: associated-with
  target: pahc.contested.rivals-undefeated
positions:
- "One God, the maker of all things; and, on Justin's own account, the Logos present in some measure in 'every race of men,' so that even a reasonable pagan before Christ could be called Christian in that broader sense."
- "No gathering of ours ever met to decide a question about God's own nature - that kind of deciding belongs to a later world. What this world actually argued about, at length and in writing, was authority: whether one bishop or a council of presbyters should lead."
- "Toward the very end of this world's own window, churches in Asia did meet, often and in many places, over a new movement of prophecy among them - but that was a decision about whether to receive a movement, not a decision about what God is."
tensions:
- "A participant expecting this world's own theological arguments to sound like later Trinitarian or Christological debates will not find them here - this world's own surviving arguments are almost entirely about who should lead, not about the nature of God. This record does not manufacture a doctrinal dispute this world's own texts do not actually contain, and it does not claim gatherings of any kind were unknown to this world - only that none of them decided a question about God's own nature."
text: >
  We believed in one God, maker of everything. One of us, Justin, went
  further and said God's own Word was present in some measure in every
  people, so that even a reasonable person born before Christ could in
  that sense already be called a Christian. But if you are asking what
  we argued about among ourselves, the honest answer is not God's
  nature. No gathering of ours ever met to settle a question like that
  about God. That kind of deciding belongs to a later world. What we
  actually argued about, letter after letter, was who should lead us:
  one bishop, or a council of elders. That was our real fight. Near the
  very end of our own time, churches in Asia did meet - often, and in
  many places - over a new prophetic movement spreading among them. But
  that gathering was about whether to receive a movement. It was not
  about what God is.
use_note:
  means: "This world believed in one Creator God, with Justin seeing the Word in every people, and argued mainly over leadership, not God's nature."
  not_for:
    - "a claim that any gathering in this world decided a question about God's nature"
    - "a claim that this world's arguments resembled later Trinitarian or Christological debates"
    - "a claim that this world held no gatherings at all"
  years: {from: 80, to: 193}
  status: provisional
---
Justin's "every race of men" claim checked directly against
cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, div1 viii, ch. 46
(viii.ii.xlvi): "He is the Word of whom every race of men were
partakers; and those who lived reasonably are Christians, even though
they have been thought atheists." Carries forward pahc.core.house-
church's own caution 10 (no ecumenical, doctrine-deciding council
exists in this world's window) and reuses the same F1-I match already
claimed by pahc.contested.two-strand-packaging (f1-i-02, "What did you
argue about among yourselves?") - that contested_claim record holds the
full authority-question content; this record answers the cell
substantively and cross-references it by relation rather than
duplicating its own analysis.

pahc.source.anti-montanist-fragments
documents synods of Asia Minor bishops meeting, repeatedly, over
the New Prophecy right at this world's own closing edge (verified
directly in cic/texts/npnf201_eusebius-church-history-life-of-
constantine.xml, HE V.16.10: "the faithful in Asia met often in many
places throughout Asia to consider this matter"). The narrower,
still-true claim survives: no gathering of
this world's own decided a question about God's own nature - only
whether to receive a movement.
