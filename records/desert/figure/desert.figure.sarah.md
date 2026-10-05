---
id: desert.figure.sarah
world_id: desert-monasticism
record_type: figure
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: 'Six sayings is still a small corpus and the old bound holds for everything beyond
    what they state: Inferential/Thin for the narrated encounters'' historicity, and nothing in this corpus
    dates Sarah individually. What has changed is that the sayings themselves are now checkable against
    a vendored file rather than carried on authority. THE RECENSION MATTERS HERE MORE THAN ANYWHERE: Budge
    is the Syriac, and the fuller Greek form of §525 - ''according to nature I am a woman, but not according
    to my thoughts'' - is NOT in it. Syncletica and Theodora, the other two ammas of the tradition, do
    not appear in this recension at all.'
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: 'Budge''s Syriac recension, six sayings under the name "Mother Sarah": §268 (setting death before
    her eyes on the ladder), §276 (the message to Abba Paphnutius), §428 (on alms given for men''s approval),
    §525 ("It is I who am a man"), §566 (seven years against the demon of fornication), and one in the
    Questions and Answers on praying for a pure heart'
  license: public-domain
names:
- name: Sarah
  tag: in-world
- name: Amma Sarah (4th-early 5th c.)
  tag: scholarly
narratable: true
bridge_line: Sarah is one of a small number of women remembered by name in our teaching. Six of her sayings survive. In one she told the brethren that she was a man among them, and they were women.
relations:
- type: associated-with
  target: desert.term.geron-abba-amma
- type: associated-with
  target: desert.gravity.elder-authority
- type: associated-with
  target: desert.force.oral-to-written-shift
- type: associated-with
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.quote.equal-measure-of-strength
- type: associated-with
  target: desert.story.virgin-who-hid-athanasius
---
Two changes follow from the arrival of a vendored edition, and the
first is a correction.

THE BRIDGE LINE ASSERTED SOMETHING THE TEXT DOES NOT. It read that Sarah
was remembered "for telling visiting monks who had come to test her that
she was a woman by nature but not by her thoughts, and that she was the
man among them." That first clause is the GREEK alphabetical form of the
saying. Budge's Syriac §525 does not contain it. The bridge_line is a
participant-facing field - it is what a reader is told about her - so it
has been cut back to what a vendored file supports. The fuller Greek
wording may well be older and better; this world simply cannot show it,
because no public-domain English of the Greek exists
(desert.search.greek-alphabetical-pd-english).

SHE HAS SIX SAYINGS, NOT ONE. The record previously cited a single
saying re-derived from consult-only renderings. Budge carries six under
"Mother Sarah", and they are various: setting her death before her eyes
each time she climbed a ladder; sending a rebuke to Abba Paphnutius for
letting a brother be reviled; on alms given for human approval still
being worth giving; seven years' struggle against the demon of
fornication on her roof; and a prayer that her own heart be pure rather
than that others be edified through her. That is a teaching voice with
range, not a single epigram.

confidence moves from C / verified-via-authority to A / verified-direct
for the sayings themselves. Everything the old divergence_note bounded
beyond them still stands.

Formation significance: desert.term.geron-abba-amma's own evidential
sense already states the asymmetry this record makes concrete - "named
ammas (Syncletica, Theodora, Sarah) are genuinely attested within it;
their surviving material is thin relative to the male bulk, a real
asymmetry this world's record carries rather than hides." This record
is that concreteness for the one amma this corpus can currently trace
to a specific, individually verified saying rather than to bare naming
alone. desert.gravity.elder-authority's own third manifestation names
"the amma tradition (Syncletica, Theodora, Sarah) as the same authority
mode attested for women, thin but genuine in the surviving record" -
this record supplies the one case that authority mode can be shown
rather than only asserted: a woman answering a direct social challenge
to her own standing with the same discernment (diakrisis) the tradition
elsewhere credits to male elders.

Roster note: Syncletica and Theodora are not built as figure records at
this step. Both are named and genuinely attested (Widely Accepted for
existence and general presence, per desert.source.apophthegmata-patrum's
own standing rule), but - unlike Sarah - this corpus currently has no
specific, individually verified saying or narrated encounter for
either, only bare naming; a figure record built on bare naming alone
would carry a bridge_line with nothing concrete to say, risking
invented specificity to fill it. This is a deliberate, logged decision,
not a silent omission - revisit if a later step's own work (a story or
quote record citing either by name, independently verified) supplies
the concrete basis this one currently has for Sarah.

No verbatim quotation is made anywhere in this record: the paraphrase
above ("she was a man among them, and they were women") restates the
saying's substance in this record's own words rather than reproducing
Doc_09a's quoted English, consistent with desert.source.apophthegmata-patrum's
own hard rule that no vendored, machine-checkable file exists for this
source and no citation of it may claim verbatim status.

The scholarly name's "4th-early 5th c." matches desert.source.apophthegmata-patrum's
own dating of the tradition generally, marked as derived, consistent
with this record set's own house style (desert.figure.antony.dates.born,
desert.figure.evagrius.dates.born) - nothing in this corpus dates Sarah
individually. divergence_note states desert.source.apophthegmata-patrum's
own unconditional Inferential-Thin bound in full ("for ANY claim beyond
what the surviving sayings themselves state"), not narrowed to the
narrated encounter's historicity alone. names[] carries only the name
and range, matching "Antony of Egypt (c. 251-356)," "Pachomius of
Tabennesi (c. 292-346)," and "Evagrius Ponticus (c. 345-399)"; the
provenance clause is in divergence_note above.

Doc_08: desert.force.oral-to-written-shift added as a reciprocal
relation - this record is that force's own concrete instance of the
compilers' selection effect on the ammas' own material, per that
force's own Transmission Specificity treatment.
