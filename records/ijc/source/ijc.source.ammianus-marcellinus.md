---
id: ijc.source.ammianus-marcellinus
world_id: imperial-juridical
record_type: source
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources: []
author: "Ammianus Marcellinus (c. 330-c. 391), pagan Roman historian"
work: "Res Gestae, Book 27.3 - the 366 election riot between Damasus's and Ursinus's parties, with a
  casualty figure for the basilica of Sicininus and a remark on the wealth at stake in the Roman
  bishopric, from outside the church entirely"
edition: "Yonge (1862, Bohn's Standard Library) - public domain in the US; VENDORED 2026-09-13
  (cic/texts/ammianus-marcellinus_roman-history_yonge1862.txt, from the Internet Archive, identifier
  romanhistoryofam00ammiiala); Book XXVII.3.12-13 directly confirmed present and read against this file"
kind: vendored
rights_status: "public-domain; vendored - the file's own header states the rights basis and is checked
  fresh, per this build's texts-registry discipline"
attribution_status: attributed
discovery_channel: "requested in world-build-docs/ijc/SOURCE-REQUEST-MANIFEST.md (search:
  ijc.search.ammianus-english); a copy was located on the Internet Archive and vendored 2026-09-13 by
  a fleet cross-world research thread's handoff, acted on and verified directly by this thread"
external_ids: {}
---
Previously FAILED CLOSED FOR QUOTATION, per this build's own convention
for a found-but-unvendored source (see ijc.source.paulinus-vita-ambrosii
for the identical case, closed the same day): everything drawn from
Ammianus in this build had been Tier 3 attributed tradition via the
standard scholarship, never a verbatim quotation. Registered originally
so that ijc.search.ammianus-english's result: found was backed by an
actual source_id rather than an empty found_sources list, corrected at
review (Opus quote-fidelity pass, 2026-08-21) for consistency with the
Paulinus precedent.

VENDORED 2026-09-13: the fleet's own cross-world research thread
independently found and verified the Yonge edition on the Internet
Archive (reachable from this sandbox even where ccel.org/newadvent.org/
tertullian.org are not) and handed the lead to this thread, which
fetched, verified, and vendored it directly (see
cic/engine/texts_registry.py's own ENTRIES note). Book XXVII.3.12-13 -
the casualty figure this build had previously carried only via
npnf202's own editorial endnote quoting Ammianus (see
ijc.quote.socrates-damasus-election and ijc.figure.damasus) - is now
confirmed present in Ammianus's own words and carries its own verbatim
quote record, ijc.quote.ammianus-sicininus-massacre. Confidence
upgraded accordingly: this is no longer Tier-3-only via the standard
scholarship for that specific fact, though the source's own register
(etic, a hostile pagan witness writing from outside the church) is
unchanged and still named as such wherever it is drawn on.
