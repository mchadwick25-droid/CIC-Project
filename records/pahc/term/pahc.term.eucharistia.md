---
id: pahc.term.eucharistia
world_id: post-apostolic-house-church
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
- F1-T
- C-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: "Documented for the baseline practice - thanksgiving over bread and cup, independently attested across every strand. Contested specifically for whether Justin's fuller account represents a network-wide template or one community's own elaboration (the term's own CT contest, Historical scope). The two-level split is the approved lexicon's own calibration; this record's top-level field states the baseline level, and the Contested layer is carried in the evidential sense and the CT note below rather than flattened into one word."
sources:
- source_id: pahc.source.didache
  locus: "9-10, 14 (cup before bread, no institution narrative)"
  license: public-domain
- source_id: pahc.source.ignatius-letters
  locus: "Philadelphians 4 (the one-eucharist instruction); Smyrnaeans 7-8 (the flesh of our Saviour; bishop-validated)"
  license: public-domain
- source_id: pahc.source.justin-first-apology
  locus: "65-67 (the fullest account - one Roman writer's own)"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - the Lord's Supper, communion, the eucharist, what happens at the table
  - the meal that forms the community
  prefer_instead:
  - modern eucharistic theology debates with no connection to this period
relations:
- type: associated-with
  target: pahc.quote.first-concerning-the-cup
- type: associated-with
  target: pahc.term.ekklesia
- type: associated-with
  target: pahc.term.episkopos
- type: associated-with
  target: pahc.term.agape-label
plain_meaning: 'The thanksgiving: the meal of bread and cup over which thanks is given. The
  community returns to this table again and again, to be formed once more into one body.'
world_word: eucharistia
distortion_risk: high
false_friend:
- a uniform ritual with fixed prayers (the form varies community to community)
- transubstantiation and later presence-theology (later categories)
senses:
  informational: 'Whatever else is decided or left open, these communities gather to give thanks
    over bread and cup, and that table does more of the ongoing forming than anything else they do.
    The form varies: one handbook gives thanks cup-first for vine and knowledge with no supper story
    told at all; Rome''s account runs reading, discourse, prayer, thanksgiving, and a collection for
    the needy; the letters from Antioch bind the table to the bishop. The constancy is the table
    itself.'
  evidential: 'Three independent voices across all three regions - the Didache, Ignatius, Justin -
    each attest a genuinely different order. The fullest account (Justin''s) must not be read as
    the most representative simply for being the most explained; which order was oldest or most
    widely kept, the record does not say.'
  personal: 'The table was where belonging was enacted: who presided, who could eat, and whom you
    refused to eat with were never merely liturgical questions. To hold to your own community''s
    table was, in the same breath, worship and belonging.'
  translational: '''Is that what we call transubstantiation?'' - the later word answers a question
    this world had not yet asked in that form. What it held is strong enough in its own words:
    Ignatius calls the eucharist ''the flesh of our Saviour Jesus Christ, which suffered for our
    sins'' - against those who denied the body''s reality - and the Didache''s prayers give thanks
    for life and knowledge. Between those two registers no single doctrine of the elements is yet
    settled.'
quick_meaning: The thanksgiving - the bread-and-cup meal at the center of the community's life; its form varied from church to church.
use_note:
  means: "The thanksgiving: the meal of bread and cup over which thanks is given, to which the community returns to be formed again into one body."
  not_for:
    - "a uniform ritual with fixed prayers"
    - "transubstantiation or later presence-theology"
  years: {from: 70, to: 200}
  status: reviewed
---
Re-derived from the approved lexicon (Doc_03/Doc_06, term 4, Tier 1 -
resolved from the borderline by G07's Primary classification; CT
contest: Historical scope, the Bradshaw-vs-Ferguson representativeness
question). The diversity content is held in
pahc.contested.table-diversity at the contested-claims step. Citation
discipline: "one eucharist" belongs to Philadelphians 4, NOT Smyrnaeans
8 (the prior build's corrected misattribution, kept correct here);
Smyrnaeans 7's flesh-language and 8's bishop-validation are separate
instructions.

This world's center-cell material adds to C-I: the same pilot conversation's first answer already described giving thanks over the cup in its own words - the term whose plain meaning is that thanksgiving belongs where the question about Jesus is actually asked.
