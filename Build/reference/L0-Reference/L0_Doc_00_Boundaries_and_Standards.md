# L0 Doc_00 — Boundaries and Standards for the Level 0 Reference Archive

**Status: Approved to proceed** (Mark, 2026-07-28). See Section 7 for the companion coach-thread governance decision made in the same conversation.
**Governed by:** Constitution Articles 4, 17, 20, 31, 35; Step 0 Movement-Scope Methodology V1.0; the Step 0 Conclusion (`Build/reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx`); the Pre-Step-0 Survey (`Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`); `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`; `Build/reference/Project-Reference/CiC_Governance_Standing_Rules.md`.

---

## 0. Purpose and Scope of This Document

This document is Level 0's own Doc_01-equivalent: it establishes the temporal and geographic boundary of the first Level 0 build, the sourcing standard every entry must clear, the two-axis confidence/provenance tagging schema, and this archive's relationship to the systems it's built to serve and the systems it must never alter. It is written to the same standard the project already holds its per-world boundary documents to — confidence-tagged, argued rather than asserted, and honest about its own limits.

**Where this archive came from, briefly, for the record:** a same-day silent-gap audit across all six built worlds (this session, 2026-07-28) found that most of the strongest gaps were figures or texts already sitting inside a source a world had already licensed as Native, never extracted into a boundary case — and that a third Registry disposition ("in-scope-in-time, out-of-scope-in-place, never engaged by the primary voice") recurred independently across four worlds. Both findings pointed at the same fix: a standing, cheap, reusable reference layer, rather than a fresh expensive agent sweep every time the question comes up. The scope grew from there once it became clear the Atlas (`cic-website/data/world-census.json`) needed the same kind of sourced backing at a different grain. Full history in the approved plan, `wondrous-plotting-cocoa.md`, kept alongside this document's own revision log for anyone who wants the reasoning that isn't repeated here.

**A fourth existing input, found after Round 1 review and folded in here rather than left for Step 1 to discover on its own:** the project already ran a real "Pre-Step-0 Survey" (`Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`) — a genuinely substantial, era-by-era survey of candidate movements across all ten Atlas eras (70 CE to present), each carrying a sourcing signal, an ecology signal, a floor note in the Methodology's own vocabulary, and relations to other candidates. It states its own purpose directly: to run the Step 0 Methodology's own required "broad survey" step across all of history in advance, "so that when the project opens a new release phase, its Step 0 starts from a maintained candidate pool instead of a blank page." It is explicit and honest about its own limit: "Nothing in this atlas is a disposition... every signal marked as a signal," not a citation-verified claim. It has already been checked once against the actual academic field (`CiC_World_Atlas_External_Review_V0_1.md`, comparing the era periodization against the Cambridge History of Christianity, Noll's *Turning Points*, González, Latourette, MacCulloch, and the World Christian Encyclopedia) — real, substantive, reference-grounded work, though not an Article 31 human-scholar review. See Section 3 for how this changes what Level 0 is actually for.

---

## 1. Temporal Scope

**This first build: 70–451 CE.** This is not a fresh boundary decision — it is Step 0 Conclusion's own stated Phase One window, adopted directly rather than re-derived, because Level 0's job is to back that record with citations, not to re-litigate it. Step 0 Conclusion states the reasoning for these exact endpoints: "70 CE (destruction of the Second Temple) to 451 CE (Council of Chalcedon)... Ending at Chalcedon rather than a death date gives the phase a symmetrical bookend: the Nicene-Constantinopolitan Creed (381 CE) sets the belief floor at one end, and the next landmark ecumenical council sets the temporal ceiling at the other." — **Confidence: Documented** (quoting the governing document directly).

**Named extension path, not attempted in this build:** Era 3 on the Atlas ("The Age of Monks and Empires," 451–622) already carries real, named candidate movements with no Step 0 record yet — the Cyrilline/Miaphysite Egyptian tradition, Syriac Orthodox (West Syriac) Christianity, the Church of the East under Persia, Chalcedonian monasticism in the Judean Desert and Gaza, Early Benedictine/Italian monasticism. This document names Era 3 as the natural next slice, in the same sequence the Step 0 Conclusion itself anticipated ("[Cyrilline/Miaphysite] belongs to whatever phase picks up where this one ends").

**Correction from Round 1 of this document's own thinking, not from the review:** it is not accurate to call Eras 4–10 (622 CE to present) simply "out of scope" — the Pre-Step-0 Survey (see Section 0) already did real, structured candidate-identification work across all ten eras, and that pool is a live input this archive should treat as a lead layer from the start, not ignore until some later phase. What this first build actually bounds is *citation-grounded verification effort*, not the archive's own awareness of what exists: Phase One (70–451) is where this build spends its actual Tier A/B sourcing work, because that's where the primary-text and prosopographical methods in Section 4 are the natural tool and where the six already-built worlds create immediate payoff. Later eras' candidates stay in the archive as unverified leads (tagged `Internal-Survey-Signal`, Section 5) until a later build phase does for them what this one does for Phase One — a scope-of-effort decision, not a scope-of-relevance one.

---

## 2. Geographic Scope

The union of Phase One's nine worlds' own stated regions, per the Step 0 Conclusion: Antioch and wider Roman Syria; Asia Minor; Rome; Alexandria and Egypt (including the Nile Valley and desert); North Africa, centered on Carthage and Hippo Regius; Cappadocia/Anatolia; Constantinople; Milan; Bethlehem (world #9's own stated region, "with ties to Rome"); Aramaic-speaking Mesopotamia (Edessa, Nisibis). — **Confidence: Documented**, drawn directly from the nine worlds' own stated regions in the Step 0 Conclusion itself.

For Aphrahat's own context specifically, the Syriac world's own Doc_01 (not the Step 0 Conclusion, which states world #7's region only as "Aramaic-speaking Mesopotamia") further specifies Sasanian Adiabene as part of this world's working geographic scope. — **Confidence: Documented**, correctly attributed to `Build/worlds/syr/Doc_01_World_Identification_Boundaries_Orientation.md` rather than to the Step 0 Conclusion (Round 1 review caught this misattribution — see Revision Log).

Regions named in Step 0 Conclusion's own "Deferred" and "Possible Future Worlds" lists sit at this archive's boundary, not inside it, for this first build: Armenia, Aksum/Ethiopia, Persian Mesopotamia beyond Adiabene, Jerusalem, Spain. A figure or movement whose own milieu is one of these regions is a candidate for the same "Outside World Milieu" disposition this session's own audit already applied to Paul of Samosata (Antioch, relative to Syriac) — assessed on its own merits when it comes up, not pre-excluded by this list.

---

## 3. What Level 0 Is, and Is Not

**Two linked layers, built and reviewed as separate document types:**

- **Movement layer** — entries at the Atlas's own grain (`world-census.json`): a whole tradition, its dates, region, and (this archive's actual contribution) real citations backing what the census currently states from an unverified spreadsheet.
- **Figure/text/event layer** — the grain this session's own audit worked in: named individuals, specific texts, specific controversies inside or around an already-selected movement's own milieu.

**Division of labor with the Pre-Step-0 Survey, stated plainly so Level 0 doesn't quietly redo work that's already done:** the Survey's own job is candidate identification and signal-level triage — era by era, is a movement worth a Step 0's attention, and roughly how well does it seem sourced. That job is done, and done well; Level 0 does not re-survey the landscape it already covers. Level 0's actual job, relative to it, is narrower and different in kind: (1) take a specific candidate the Survey already flagged and verify its specific claims against real Tier A/B sources, upgrading a signal to a citation; (2) do the work the Survey explicitly never attempts at all — the figure/text/event layer, individual named people and texts living inside an already-selected movement's own milieu, which is a different grain than the Survey's own movement-level entries. An `Internal-Survey-Signal` claim (Section 5) is a lead worth taking seriously — it's careful, real work — but it is not yet a citation, exactly as a Bird Substack post isn't.

**Level 0 is not:**
- A replacement for the Step 0 Conclusion, or for the Pre-Step-0 Survey. The Conclusion is the closed, authoritative record of *which* movements were selected for Phase One and why. The Survey is the maintained candidate pool every future Step 0 draws from. Level 0 extends both with citations; it does not re-run, overturn, or duplicate either one's own determinations.
- A replacement for `world-census.json`, or an automatic editor of it. Level 0 produces a candidate sourced-backing layer; any change to the actual census goes through the Atlas's own established Decision-Log discipline, with the Atlas's own maintainer deciding, the same way every other change to that file has been made.
- An editor of any world's own Doc_01/Doc_02/registry/records. Every world-facing output from Level 0 is read-only and additive — new files under `Build/reference/L0-Reference/`, nothing touched in `worlds/`, `cic-poc/backend/data/`, or `cic-poc/backend/wrs/records/`. This holds without exception, regardless of any individual world's own current build status — as of this document's Round 1 review, Desert (frozen at S5.6), Alexandria, and Syriac have each reached their own freeze declarations, illustrating exactly how quickly that status changes and why the rule itself, not a snapshot of who currently holds which status, is what this document relies on.
- A path into the live conversational/Representative system. Not attempted in this build; explicitly deferred to a separate decision.
- An Article 31 validation. See Section 6.

---

## 4. Sourcing Standard

**Tier A — usable directly by this archive's own build process:**

1. Public-domain primary texts in translation (the Ante-Nicene and Nicene/Post-Nicene Fathers series via ccel.org) and original-language texts (Patrologia Graeca/Latina via Documenta Catholica Omnia; Perseus Digital Library for Greek).
2. Live, officially-released open-access digitizations from a named institutional project (a university press, a learned society, a national academy, or a funded academic consortium) — the confirmed model case is PLRE (*Prosopography of the Later Roman Empire*), currently being digitized by the "Connecting Late Antiquities" project (funded by DFG and AHRC; partners the University of Bonn, University of Exeter, and University of London/SAS; hosted by the Exeter Digital Humanities Lab), with Volume 1 (260–395 CE) already live and freely browsable at `connectinglateantiquities.org`. (Round 1 review corrected an earlier, incorrect attribution of this project to the British Academy and to Cambridge University Press hosting — that framing describes a related but distinct Edinburgh-based project's own stated future plan for PLRE, not Connecting Late Antiquities' current, live arrangement. The underlying fact — Volume 1 is free and live now — is independently confirmed; see Revision Log.)
3. Open-access journal articles, and standard freely-available reference works (e.g., Smith & Wace's *Dictionary of Christian Biography*, 1877–87).
4. Freely-readable posts by credentialed scholars on their own public platforms (confirmed case this session: most of Michael Bird's early-Christianity Substack posts) — used strictly as a **discovery/pointer layer**. What such a post names — a scholar, a monograph, a primary-source citation, a movement — gets chased down and verified against the actual source before it can support an entry. The post's own prose is never itself the citation.

**Tier B — the project lead's own personal research, reported in, never fetched by this build's own process:** paywalled material (JSTOR JPASS, a paid Substack tier, or similar) the project lead reads himself. Verified this session: JPASS's own terms restrict use to "non-commercial, scholarly purposes" and explicitly prohibit using content "to train large language models" or for "web scraping, web harvesting, web data extraction" — clean for the project lead's own individual reading, not for this archive's automated process to draw on directly. Any fact sourced this way is tagged `Human-Verified (Tier B)` (Section 5) and attributed to the project lead's own review, not silently absorbed as if machine-sourced.

**Before any claim is flagged as unverifiable, check in this order** — do not fall back to "unverified" without actually checking all four: (1) does an official open-access digitization project exist for this source class (the PLRE pattern); (2) does a public library system the project lead holds a card with carry it; (3) has a credentialed scholar published freely on it — a lead to chase, not a citation to use; (4) does a public-domain critical edition or translation already cover it.

**What Level 0 will not do, regardless of source:** reproduce substantial verbatim text from any copyrighted work into an entry. Every entry is this archive's own original synthesis, citing its sources, in the same register this project already uses throughout its own Doc_01/Doc_02 work.

---

## 5. Confidence and Provenance Tagging

Every entry, either layer, carries both axes below, and the two are never collapsed into one — extending Article 17's own "historical attestation and formational centrality are distinct axes" discipline to a third pair this archive needs that neither the Constitution nor the Construction Framework has previously had to name.

**Historical Confidence** (Constitution Article 17's fixed vocabulary, about the claim itself): Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin.

**Sourcing Provenance** (new to this archive, about how *this entry* was verified):

| Tag | Meaning |
|---|---|
| `Primary-Open` | Verified against a public-domain or openly-licensed primary text directly. |
| `Standard-Reference-Open` | Verified against a standard, freely-available reference work. |
| `Official-Digital-Release` | Verified against a named institutional open-access digitization project. |
| `Scholar-Public-Writing (pointer only)` | A credentialed scholar's free public post named the lead; the underlying primary/secondary source was then independently verified. Never used alone — always paired with the tag for what was actually checked. |
| `Internal-Survey-Signal (needs upgrade)` | The project's own Pre-Step-0 Survey named this candidate and gave it a sourcing/ecology signal, but the underlying primary/secondary sources have not yet been independently verified by this archive. A real, careful lead — not yet a citation. |
| `Human-Verified (Tier B)` | The project lead read paywalled material himself and reported the finding. |
| `Web-Lead (needs upgrade)` | General web search or a tertiary summary only; not yet upgraded to a citable tier. An entry may carry this tag provisionally but is flagged for follow-up, never presented as settled. |

---

## 6. The Article 31 / Validation Caveat

Per the Constitution's own standing rule (Article 35, Section B, as recorded in `Build/reference/Project-Reference/CiC_Governance_Standing_Rules.md`): every independent review round on this archive's own documents, when conducted by a dispatched agent rather than a human external reviewer, is saved as its own file beginning with the literal line **"Simulated review — informational only, not an Article 31 substitute."**

This archive as a whole carries the same caveat at the top level: it is built and reviewed with real rigor and discipline, but it is not, and does not claim to be, Article 31-validated. That requires review "by at least one qualified human subject-matter reviewer... holding recognized scholarly standing in the specific historical or theological subfield" (Article 31, quoted directly). The aspiration stands and is not abandoned by building this now — the project lead's own Tier B reading (Section 4) is real, if partial, progress toward it, not a substitute for it.

---

## 7. Governance Item — Resolved

The Build Protocol assigns editing authority over framework/methodology-level documents (the Construction Framework, the Representative Construction Framework, the Change Orders Register, the L3B/L4 templates) to a "coach thread," distinct from an ordinary "build thread." This document is exactly that class of artifact, and the thread producing it was never assigned that role — named plainly rather than assumed either way when first raised.

**Resolved (Mark, 2026-07-28, in direct conversation):** this document — and any future addition to Level 0's own governing standards — is coach-thread-governed going forward, matching the exact pattern already established for the Construction Framework, the Representative Construction Framework, the Change Orders Register, and the L3B/L4 templates. This document itself calls itself "Level 0's own Doc_01-equivalent" (Section 0); it is functionally the same kind of artifact as those already-governed documents, not built content, and reuses their already-proven pattern rather than inventing a lighter one.

**Scope, so this does not stall real work:** this applies to *this document's own future revisions* only. The actual Level 0 provenance-upgrade work — new, additive entries under `Build/reference/L0-Reference/` upgrading a movement's or figure's sourcing signal to a citation — never edits this document, is ordinary build-thread work under the Build Protocol's own definition, and was never blocked by this question. It proceeds now that both this and Section 0's disposition are resolved.

See `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`'s own coach-thread list, updated to name this document explicitly.

---

## 8. Open Items Carried Forward to Step 1

- Confirm the coach-thread/build-thread governance question (Section 7) before any registry-normalization work (Step 1, figure layer) begins.
- PLRE/Connecting Late Antiquities' open-access status: **resolved in Round 1 review** — independently confirmed live and free (Section 4), with the institutional attribution corrected. No longer an open item.
- The exact field-by-field cross-walk between this document's Sourcing Provenance tags and `world-census.json`'s own existing fields (`sourcing`, `floorNote`) is Step 1's own job, not resolved here — note that the Pre-Step-0 Survey's own prose fields (Sourcing signal, Ecology signal, Floor note, Relations) are very likely the direct source those census fields were generated from; Step 1 should confirm this rather than assume it, since it changes whether Step 1 treats the Survey document or the census JSON as the primary artifact to cross-walk against.

