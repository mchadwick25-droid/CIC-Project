---
id: srcDESsearch002
world_id: desert-monasticism
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: 'Purposive (Booth''s standard) - the FIELD-BIBLIOGRAPHY SWEEP (2026-08-06), run against
  the Academic Rigor Review''s finding #10 recommendation verbatim: Desert against BIBP (free). srcDESsearch001
  logged BIBP as "NOT ACCESSIBLE" at migration time (2026-07-26); this sweep re-attempts it directly rather
  than re-stating the limit. Documents this sweep only.'
types_sought:
- direct access to BIBP (Base d''Information Bibliographique en Patristique) and confirmation of its current
  URL/access path, since the original migration-time attempt left this unresolved rather than confirmed-closed
- if BIBP itself proved reachable, works on Antony, Pachomius, the Apophthegmata Patrum, and Evagrius not
  already in the 26-row registry
- edition/translation detail for rowed P-type works still carrying edition_status none-consulted, surfaced
  incidentally while searching for BIBP access
approaches:
  bibp-direct-access-attempt: 1
  bibp-adjacent-search: 1
  row-cross-check: 1
years_searched:
  from: 1965
  to: 2026
languages_searched:
- en
- fr
inclusion_exclusions: 'Included: any BIBP notice actually reached; any real, checkable critical-edition
  citation surfaced while confirming BIBP''s current access path, cross-checked against the existing 26-row
  registry before being called a gap. Excluded: Guy''s SC editions of the Apophthegmata Patrum (SC 387/474/498)
  - srcDESsearch001''s own EXCLUDED list already names these as "reserved lead for quote work," so their
  reappearance in this sweep confirms rather than adds; general Apophthegmata/Evagrius secondary literature
  not tied to a specific rowed work''s missing edition field.'
terms_tried:
- term: 'https://www.bibl.ulaval.ca/bd/bibp/ and https://www.bibl.ulaval.ca/bd/bibp/infoeng/ (direct WebFetch)'
  productive: false
- term: 'https://www.sourceschretiennes.mom.fr/url/bibp-... and https://aiep-iaps.org/bibliographical-databases
    (direct WebFetch)'
  productive: false
- term: 'WebSearch "Base d''Information Bibliographique en Patristique" access URL'
  productive: true
- term: 'WebSearch site:bibl.ulaval.ca "bd/bibp" notice'
  productive: true
- term: 'WebSearch site:bibl.ulaval.ca bibp "moines" OR "monachisme" egyptien recherche bibliographique'
  productive: false
- term: 'WebSearch bibl.ulaval.ca bd bibp "recherche" formulaire interrogation base cgi'
  productive: false
- term: 'WebSearch BIBP patristique Laval base de donnees 2024 OR 2025 statut fermeture'
  productive: false
- term: 'WebSearch site:sourceschretiennes.org OR site:sourceschretiennes.mom.fr BIBP patristique Egypte
    moines'
  productive: true
- term: 'WebSearch Evagrius Ponticus Antirrheticus / Antirrhetique Sources Chretiennes SC 640 critical edition
    editor'
  productive: true
- term: 'WebSearch Evagrius Ponticus Praktikos Guillaumont Sources Chretiennes SC 170 171 critical edition'
  productive: true
- term: 'WebSearch Evagrius De Oratione / Chapters on Prayer critical edition Philokalia Nilus attribution
    Sources Chretiennes'
  productive: false
instruments:
- 'BIBP (bibl.ulaval.ca/bd/bibp/) - CONFIRMED STILL NOT ACCESSIBLE this session, but for a more specific
  reason than srcDESsearch001 recorded. The site exists, is described by its own host and by outside library
  guides (UW-Madison, Strasbourg, AIEP-IAPS) as free and login-free, and holds a real and large corpus (~29,000-70,000
  notices depending on the year cited). Direct WebFetch to bibl.ulaval.ca, sourceschretiennes.mom.fr, and
  aiep-iaps.org all returned HTTP 403 - and so did a WebFetch to en.wikipedia.org run as a control, confirming
  this is a general tool-level block in this session''s environment, not a BIBP-specific one. Unlike syri.ac,
  WebSearch could NOT substitute: BIBP is a query-driven search database, not a set of static crawled pages,
  so search-indexed individual notices do not exist to be found this way (confirmed by repeated site:bibl.ulaval.ca
  searches returning only help/documentation pages, never actual bibliography notices). BIBP is therefore
  accessed neither directly nor indirectly this session - a harder, more specific negative than the migration-time
  sweep established.'
- 'General web search (Editions du Cerf / sourceschretiennes.org catalogue pages, evagriusponticus.net,
  library catalogues) - NOT BIBP, but used once BIBP proved unreachable, and it surfaced one real, specifically-checkable
  gap: srcDES004 (the Evagrius Praktikos/Chapters on Prayer/Antirrhetikos corpus row) carried edition_status
  none-consulted with no edition field. Two of its three works'' critical editions were confirmed independently
  (Guillaumont & Guillaumont, SC 170-171, 1971, for the Praktikos; Fogielman, SC 640, 2024, for the Antirrhetikos)
  and added to the row. The third (De Oratione / Chapters on Prayer, transmitted pseudonymously under Nilus''s
  name) returned conflicting/unclear signal about its own dedicated critical edition and was left OPEN rather
  than asserted - see the row''s own edition field for the exact caveat.'
- 'L''Annee philologique - NOT ACCESSED this session (out of this sweep''s scope, which the review''s finding
  #10 specified BIBP for Desert); remains a standing coverage limit, unchanged from srcDESsearch001.'
---
Saturation statement (field-bibliography sweep scope, 2026-08-06): the sweep's primary target, BIBP, was not reached - not directly (HTTP 403 on every attempt, matching a general WebFetch block confirmed against a Wikipedia control, not a BIBP-specific one) and not indirectly via search-engine index either, because BIBP is a query-driven database whose individual notices are not crawled/indexed the way syri.ac's static pages are. This is a firmer, more specific confirmation of the migration-time sweep's "NOT ACCESSIBLE" finding, not merely a repetition of it. Redirected to general web search for the same subject matter (Antony, Pachomius, Apophthegmata Patrum, Evagrius) cross-checked against the existing 26-row registry: nothing surfaced a missing WORK - the Vita Antonii, Pachomian corpus, Apophthegmata Patrum, Lausiac History, Historia Monachorum, and Evagrian corpus are all already rowed, and the one apparent lead (Guy's SC editions of the Apophthegmata) turned out to be already known and deliberately reserved per srcDESsearch001's own EXCLUDED list, not a new find. One genuine, narrower gap was found and closed: srcDES004's missing edition citations for two of its three Evagrian works (Praktikos, SC 170-171, 1971; Antirrhetikos, SC 640, 2024), both confirmed through independent publisher/catalogue corroboration. The third work in that same row, De Oratione, was investigated but NOT closed - the search returned an apparently garbled/conflated signal about its critical-edition history that this session could not confidently disentangle, and it is left open in the row's own edition field rather than resolved by guesswork. BIBP and L'Annee philologique remain standing coverage limits.

Provenance: this file is the field-bibliography sweep log, run against the Academic Rigor Review's finding #10 (Ministry/Operations/Audits/CiC_FullSystem_Review_2026-08-05/02_Academic_Rigor_Review.md, ~line 670). srcDES004's edit is the sweep's one direct, low-risk, fully-cited correction; no new source rows were added, and no other existing row was found to need correction or contradiction on the evidence surfaced this session.
