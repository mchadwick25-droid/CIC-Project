---
id: pahc.source.ignatius-letters
world_id: post-apostolic-house-church
record_type: source
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: null
sources: []
author: "Ignatius of Antioch (if the traditional attribution holds - see the three-way dispute below)"
work: "The seven letters, middle recension (Ephesians, Magnesians, Trallians, Romans, Philadelphians, Smyrnaeans, To Polycarp); traditional dating c. 107-117 CE, redated 130s-140s by Barnes and Foster, held pseudepigraphic c. 160-180 by Huebner and Lechner - a genuine three-way scholarly split"
edition: "Ante-Nicene Fathers vol. 1 (1885), Roberts-Donaldson series (the volume-level editor-translator credit; no per-work translator credit is printed at this work's own head), vendored as cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml (div1 v). SCOPE: the SHORTER (middle-recension) text of each letter only - the volume prints shorter and longer recensions in parallel and appends the Syriac abridgment and the spurious letters; the longer recension, the Syriac, the spurious letters (div2 v.xiv-v.xxiii), and the Martyrdom of Ignatius (div2 v.xxv) are all OUTSIDE this row's scope"
kind: vendored
rights_status: public-domain
attribution_status: contested
discovery_channel: "prior-build Source Registry row P03 (Doc_02, approved 2026-07-07), re-registered against the vendored corpus; work presence and recension layout verified at div1 v (parallel shorter/longer columns per letter, div2 v.ii-v.viii)"
external_ids: {ccel_volume: "anf01", thml_div: "v"}
---
Rights verified from the file's own DC.Rights header (Public Domain).
Recension discipline is load-bearing: every quote from this row must be
taken from the SHORTER (middle-recension) rendering and checked against
the parallel longer text to confirm which is being quoted - the prior
build's verified quote pass (pahcq001-004, 2026-08-15, branch
claude/table-voice-reset-nufsm4) did exactly this (e.g. Romans 4
distinguished from the longer recension by "the pure bread of Christ"
vs. "pure bread of God").

THE LOAD-BEARING DEPENDENCY (Doc_01 SS6/SS10, Doc_02 SS1.3, SS1.8):
this corpus is Strand A's almost-only evidence, and its dating and
authenticity are a genuine three-way split - traditional Trajanic
(Lightfoot/Zahn/Harnack consensus, Brent), redated-but-authentic
130s-140s (Barnes, Foster - Barnes is a supporting voice for redating,
not an Ignatius specialist), and pseudepigraphic 160-180, Roman
provenance (Huebner/Lechner, the Munich school). If the third position
is right, Strand A's core evidence is not a contemporaneous snapshot of
Antioch/Asia Minor practice at all. Doc_02 SS1.8's aggregate accounting:
three of the seven tested gravities (G01's Strand A content, G04, G05)
and most of this world's vivid quotable material rest on this one
corpus. The middle recension's own authentication was a two-century
critical dispute (Ussher 1644/Vossius 1646 vs. Daille 1666, Pearson
1672; Cureton 1843-45 vs. Zahn 1873/Lightfoot 1885-89), not an unbroken
inheritance. Every downstream record citing this row inherits these
caveats; the Confidence/Gravity Cross-Check items in the gravity records
name them explicitly.
