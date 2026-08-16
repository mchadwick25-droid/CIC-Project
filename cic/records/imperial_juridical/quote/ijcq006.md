---
id: ijcq006
world_id: imperial-juridical-christianity
record_type: quote
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
speaker_or_author: ijcfig007
text_translation: Let him not disdain a city which is royal, though he cannot make it an Apostolic
  See. And let him on no account hope that he can rise by doing injury to others.
locus: Leo I, Letter CIV, to Marcian Augustus (22 May 452)
translation_used: srcIJC47
license: verbatim
confidence:
  citation_specificity: A
  verification_state: verified-direct
  verification_date: '2026-08-16'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
---
Added 2026-08-15 at Mark's explicit request ("add a quote from Letter CIV to Marcian too"), completing
a matched pair with ijcq005 from Leo's dated dispatch of 22 May 452 rejecting Canon 28 - Letter CIV to
Marcian and Letter CVI to Anatolius, both now quoted; Letter CV to Pulcheria remains identified but not
yet quoted.

A GENUINE HEADER-VS-BODY MISTAKE WAS CAUGHT before this text was chosen: this letter's own section III
carries an editorial summary line (paragraph id="ii.iv.xcix-p11", class="c27", one of Percival/Feltoe's
own marginal-summary headers throughout this edition) reading "The city of Constantinople, royal though
it be, can never be raised to Apostolic rank" - a strong, punchy, almost quote-ready sentence that
looked like an obvious candidate. But it is the EDITOR'S paraphrase heading the section, not Leo's own
translated words - checking the very next paragraph (id="ii.iv.xcix-p12", the actual letter body)
showed Leo's real sentence expresses the same thought differently: "Let him not disdain a city which is
royal, though he cannot make it an Apostolic See." This record quotes the body text, not the editorial
header - the same category of error the Ambrose misattribution (ijcq002) and the srcIJC02 scoping
mismatch (srcIJC44/45) caught by different routes: verify what a passage actually IS before trusting
that it reads well.

Wording transcribed directly (tail-aware ElementTree walker) from
cic/texts/npnf212_leo-great-gregory-great.xml, div3 id="ii.iv.xcix", paragraph id="ii.iv.xcix-p12".
Thematically distinct from ijcq005: that quote makes Leo's procedural/constitutional argument (a
council's decree contrary to Nicaea is "ipso facto null and void"); this one makes his status
distinction (a city's secular, royal rank is not the same kind of thing as apostolic rank) - two
different arguments from the same dispatch, not a restatement.

srcIJC47's verification_note is updated alongside this record: Letter CIV (div3 ii.iv.xcix) is now
wording-verified, at the same standard Letter CVI reached with ijcq005.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text_translation
above at FK grade 12.7 / FRE 63.1. Per Mark's "re-select simpler verbatim excerpts first" decision, the
single semicolon joining the two clauses is rendered as a period instead - no wording changed, only the
sentence boundary. Re-scored: FK 6.2 / FRE 79.9, clearing both thresholds. license stays verbatim.
