---
id: gallic.quote.martin-funeral-crowd-and-monks
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. The crowd's presence is plausible and public in
    kind, but the specific count - "almost to the number of two thousand" - is explicitly given as
    report ("They are said to have assembled"), not as Sulpitius's own count. Carried as Widely Accepted
    for the scene's general shape; the number itself is the letter's own hearsay, not a fact this record
    asserts.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2487-2495): the crowd that gathered for Martin''s funeral, and the reported number of monks'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how large Martin's funeral was, or who came
  - conversation reaches how quickly a community's memory of a founder could gather crowds
  prefer_instead:
  - participant wants the procession's own ranks and orders, not the crowd's size - retrieve
    gallic.quote.martin-funeral-procession-ranks
text: >-
  But it is hardly credible what a multitude of human beings assembled at the performance of his
  funeral rites: the whole city poured forth to meet his body; all the inhabitants of the district and
  villages, along with many also from the neighboring cities, attended. O how great was the grief of
  all! how deep the lamentations in particular of the sorrowing monks! They are said to have assembled
  on that day almost to the number of two thousand,—a special glory of Martin,—through his example so
  numerous plants had sprung up for the service of the Lord.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  Sulpitius marks his own report as hard to credit even as he gives it, and flags the monks' count as
  what "they are said to have" reached, not a fact he vouches for personally. He reads the size of the
  crowd itself as evidence of Martin's effect: "through his example so numerous plants had sprung up."
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
modern_rendering: >-
  It is hard to believe how many people gathered for his funeral. The whole city poured out to meet
  his body. All the people of the surrounding district and villages came, along with many from
  nearby cities too. Oh, how great was everyone's grief! How deep were the laments of the mourning
  monks above all! It is said that almost two thousand of them gathered that day. This was a special
  glory of Martin's. Through his example, so many plants had sprung up to serve the Lord.
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"hardly credible what a multitude"` returns line 2487; `grep -n "for the service of the Lord"` returns
line 2495. Read in full at lines 2487-2495: one continuous, unbroken run of prose. The em dashes around
"a special glory of Martin" are the source's own punctuation (confirmed with `cat -A` on the raw file:
the byte sequence is U+2014 EM DASH, not a double hyphen), carried here as "—" rather than "--".

The host record's own current wording of this same material uses "--" (double hyphen) in place of the
source's em dash; this record uses the source's actual character. No word was added, dropped,
substituted, or reordered; hard line wraps were joined with single spaces.
