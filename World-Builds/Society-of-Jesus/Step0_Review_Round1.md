# Step 0 Review, Round 1 — The Society of Jesus

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` (Revision 1, drafted 2026-09-15).

## Verdict

**Substantial revision needed.** Section A's floor conclusion is correct, but four findings each change a claim's substance, a sourcing conclusion, or a scope boundary — this project's own bar for substantial revision.

## Findings

### Substantial

**F1. The sourcing record is stale.** B1, B2, the Section B conclusion, the Tier 1 rationale, and §4 items 1–2 all describe the Constitutions, Nadal's *Adnotationes*, Canisius, and Faber's material as absent, unmentioned, or closed leads. The dossier was updated 2026-09-24; REGISTRY.yaml and the corpus-map now show all ten works vendored as of that date — the 1606 Latin Constitutions and 1595 Latin Nadal as PRIMARY content, Canisius's 1622 English *Summe*, Xavier Vol. 2, and Boero's *Life of Faber* (context, provisional). "No PD English translation of the Constitutions" is still correct; "absent from the available PD corpus" is not. The real remaining gap is narrower — the institutional voice exists only in Latin, and Nadal's file carries a disclosed severe-OCR flag — and needs rewriting around that, not around absence. The Faber lead is only partly resolved: Boero's volume is a biography, and how much of the Memoriale it quotes verbatim is unchecked per the corpus-map's own note — §4 item 2 should say that, not "closed."

**F2. The Chinese/Malabar Rites "out-of-window" claim (A3, §4 item 4) is factually wrong.** The document states the controversies are "well past this candidate's own 1650 close." Inside the window: Ricci's China accommodation method (from the 1580s), de Nobili's Madurai accommodation (from 1606), Gregory XV's 1623 ruling on Malabar practices, the internal Jesuit Jiading conference (1627–28), and Propaganda Fide's 1645 decree condemning the Chinese rites as Morales presented them. The cited condemnation date "1774" matches no actual Rites condemnation (Benedict XIV's Malabar condemnation is 1744; 1773 is the Society's suppression — likely conflated). "First-generation figures predate the dispute" is true of Ignatius/Xavier/Nadal individually, but the census defines this world as reaching China, Japan, India, Brazil, and Canada — a live controversy sits inside the window and needs handling as an actual scope boundary, not an exclusion. This claim was inherited unverified from the dossier's own §6.

**F3. "Trent's own canons explicitly reaffirm the Nicene Creed and Chalcedonian Christology by name" (A1) is false.** Session III recites the Niceno-Constantinopolitan Creed in full but calls it "the Symbol of faith which the holy Roman Church makes use of" — "Nicene" appears only in a footnote citation. "Chalcedon" appears in the decrees exactly once, as a disciplinary citation (Session XXIII, ch. XVI, ordination canon), not a doctrinal reaffirmation; no passage reaffirms Chalcedonian Christology by name. The A1 verdict itself stands — the Session III creed recital matches Article 4's five commitments almost clause for clause, better evidence than the false claim as written — but the source-content claim needs correcting here and in the sibling Tridentine Step 0 document, which repeats the same error.

**F4. Global/missionary claims (B2, B4, B5) rest on sources concentrated in 1521–1556.** B5 claims "worldwide reach by the window's close"; B4 rests the "only real missionary/global dimension" claim entirely on Xavier (d. 1552). Every vendored primary voice is first-generation (Ignatius, Xavier, Faber, Nadal, Canisius); nothing covers roughly 1560–1650 — Ricci, de Nobili, the 1599 Ratio Studiorum, the colleges, the New France missions. The census names the Jesuit Relations as a core primary source (a plausible PD lead, Thwaites 1896–1901) that was never checked — grep of `cic/texts/` confirms nothing vendored. The census's own "founder-corpus gravity needs standard discipline" warning is also missing from this document's framing of the founder corpus as simply "well covered." Either the sourcing conclusion or the scope claim needs to change.

### Moderate/minor (real, not independently substantial)

- **F5.** Trent is called "this order's own doctrinal charter" (B1, A1) — the Society's actual charter is the 1540/1550 Formula of the Institute; the corpus-map itself sets Trent's role as `context` precisely because "it is not the Society's own composed voice." "Doctrinal anchor implemented" (the dossier's phrasing) is accurate; "charter" is not.
- **F6.** The §0/A4 claim that Mark selected this world partly for a "desert-monastic/Evagrian echo" has no findable record in `Ministry/`, `worlds/_cross-world/`, or `World-Builds/` — cite a record or mark as reported-not-yet-on-file.
- **F7.** No cross-reference to Devotio Moderna's own Step 0, which explicitly flags a "both-directions ancestor" influence relationship on Jesuit pedagogy and asks for it to be named in whichever Doc_02 runs for the Jesuits.
- **F8.** Superlative claims (B4 "only entry with a real missionary/global dimension"; A1 "cleanest clearance in the batch") conflict with sibling documents' own claims (Tridentine's Propaganda Fide; Tridentine's own "reference point" framing).
- **F9.** A1's "no deviation" claim rests on rights-verification, not a content read — positive evidence exists and should be cited (the Autobiography's Trinity devotion at Manresa, the Exercises' Incarnation contemplation, the Session III creed).
- **F10.** Boilerplate "no figure word-extracted from vendored XML" line is inapplicable (files are .txt); real word counts are now available (~1.39M words across the ten files).

### Confirmed accurate

Death dates (Ignatius 1556, Xavier 1552, Nadal 1580); 1540 papal approval; Letters Vol. 1's 24-letter, 1524–47 range; the Ganss/Homann copyright status; Atlas VI.11 and window/status fields; batch composition.

## Disclosed complications flagged, not fixed by this review

- **Trent/Tridentine overlap is worse than described.** The Tridentine corpus-map carries a verbatim copy of this document's own Waterworth note, including "not the Society's own composed voice," and sets `role: context` there too — so neither world currently holds the text as "native," contradicting both Step 0 documents' own native/implementing split claim. This is a corpus-map defect outside this document's own scope — flagged, not corrected here.
- The dossier's own §3 scale estimate still says "nothing is vendored," contradicting its own updated §1. Flagged, not corrected here.

## Disposition

Per `cic-build-cycle`: F1–F4 each change a sourcing conclusion, a scope boundary, or a claim's substance — meets the project's own bar for substantial revision. Revision 2 should rebuild B1/B2/Tier/§4 against the 2026-09-24 record, rewrite A3/§4 item 4 as an in-window scope question, correct the Trent/Chalcedon claim, and either narrow or condition the B4/B5 global claims (including checking the Jesuit Relations). F5–F8 should be addressed in the same pass; a round-2 review can be a targeted recheck of these items only.
