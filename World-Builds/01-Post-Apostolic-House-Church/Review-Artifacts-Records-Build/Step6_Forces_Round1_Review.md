# Step 6 (Doc_08 — Forces) — Round 1 Independent Cold Review

**Scope:** the 14 `records/pahc/force/*.md` records, the five gravity records that received new back-links, `world-build-docs/pahc/FORCES-INDEX.md`, `world-build-docs/pahc/generate_forces_index.py`, and `world-build-docs/pahc/GRAVITY-INDEX.md`, checked against the approved `CiC_W1_Doc08_Forces_Document.md` read in full, against `engine/m1/schemas.py` + `engine/m1/gates.py`, against all 86 `records/_fleet/canon_question/*.md`, against the 18 `records/pahc/source/*.md` rows, and — for every string presented as a quotation — against the vendored ThML texts under `cic/texts/`.

**Reviewed at commit** `5718c55a` ("pahc Step 6 (Doc_08 Forces): draft all 14 force records + index"). No prior conversation about this work was visible to this review.

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED — narrow in scope.**

Nothing in the six-cell matrix is fabricated. All 14 forces are present, correctly cell-assigned against Doc_08, correctly `kind`-typed, and every declared relation traces to a specific Doc_08 §4 or §5 statement — I checked each one individually and found no manufactured connection. The full gate battery runs clean except the 18 pre-existing canon-coverage blank cells, which this batch neither caused nor could have fixed (`canon.substantive_types()` counts only doctrinal_witness/term/story/quote, so force and gravity `canon_cells` are invisible to that gate by design). Relation reciprocity is genuinely complete in both directions — I verified all 26 edges by hand rather than trusting the generated claim — and the five gravity records received additions only, with no deletion, duplication, or misdirection. Both generated indexes regenerate byte-identical, so neither has been hand-edited.

The revision call rests on a narrow but real cluster: **three strings presented as quotations of primary texts are not what the named editions say**, and one of them is drawn from the longer Ignatian recension that `pahc.source.ignatius-letters` puts explicitly *outside* its own scope under a discipline that record calls "load-bearing." Alongside those, one gravity record now asserts and denies the same relationship in the same file, one record's canon-cell rationale is contradicted by its own sibling record, and the Gravity Index carries a statement about the build state that this step made false. All seven are locally fixable without disturbing any force's substance; this is the same "substantial, narrow" shape this project has calibrated before, not a defect in the underlying analysis.

---

## SUBSTANTIVE findings

### 1. `pahc.gravity.boundary-drawing` now asserts and denies the same relationship

**Files:** `records/pahc/gravity/pahc.gravity.boundary-drawing.md`; cross-checked against `world-build-docs/pahc/GRAVITY-INDEX.md` and `world-build-docs/pahc/FORCES-INDEX.md`.

**What's wrong.** This step added `associated-with → pahc.force.state-pressure` to the record's `relations[]`. The same record's `description` says, unchanged:

> "No demonstrated relationship with translocal-network or **state-pressure** — Doc_04's own Interaction Matrix traces neither directly (the state-pressure cell was carried as Reshaping through four review rounds before Doc_04's own round 5 found it had no textual grounding anywhere and corrected it to No demonstrated relationship — **this record follows that corrected state, not the earlier error**)."

`FORCES-INDEX.md` line 93 states that `pahc.force.state-pressure` **IS** `pahc.gravity.state-pressure`, so this new edge is functionally an edge to G03 — the exact cell the description says has no demonstrated relationship and that the record promises not to manufacture. The regenerated `GRAVITY-INDEX.md` interaction matrix (line 28) still prints `boundary-drawing × state-pressure = no demonstrated relationship`, so the record now reads three different ways depending on which field you look at.

**What I checked.** Read both records in full; read `git diff HEAD~1 HEAD -- records/pahc/gravity` to confirm the edge is new in this batch; read Doc_08 §4 Connection 5 and §5 (G05), which authorize the link but disclose it as "this document's own new synthesis, not an inherited Doc_04 finding"; confirmed `pahc.force.state-pressure`'s trailing body *does* carry that disclosure, so the asymmetry is one-sided — the gravity record carries none.

**Suggested fix.** Amend `pahc.gravity.boundary-drawing`'s description (or its trailing body) to state that the `associated-with pahc.force.state-pressure` edge realizes Doc_08 Connection 5, disclosed there and here as this build's own interpretive extension, and that the gravity-level G03↔G05 cell remains "No demonstrated relationship" per Doc_04's round-5 correction. Do not drop the edge — reciprocity requires it, and Doc_08 authorizes it; the missing thing is the disclosure that already exists on the force side.

---

### 2. `pahc.force.apostolic-testimony-inheritance` quotes the out-of-scope Ignatian recension, at the wrong chapter

**File:** `records/pahc/force/pahc.force.apostolic-testimony-inheritance.md` (`manifestations[1]`, and the `sources[].locus` that supports it).

**What's wrong.** The record reads:

> `- "Ignatius urging submission to the presbytery 'as to the apostles of Jesus Christ' (Trallians 3)"`

Two errors in one line. (a) The phrase is in **Trallians chapter II**, not III. (b) The *plural* "as to the apostles of Jesus Christ" occurs **only in the longer recension**. The middle (shorter) recension — the only text in scope — reads "as to **the apostle** of Jesus Christ," singular.

**What I checked.** Grepped `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` directly and located both parallel columns of Trallians ch. II:
- shorter: "…without the bishop ye should do nothing, but should also be subject to the presbytery, **as to the apostle of Jesus Christ**, who is our hope, in whom, if we live, we shall [at last] be found."
- longer: "…And be ye subject also to the presbytery, **as to the apostles of Jesus Christ**, who is our hope, in whom, if we live, we shall be found in Him."

Trallians ch. III in the middle recension says something else entirely: "…let all reverence the deacons as an appointment of Jesus Christ, and the bishop as Jesus Christ… and the presbyters as the sanhedrim of God, and assembly of the apostles."

`records/pahc/source/pahc.source.ignatius-letters.md` binds this: its `edition` field reads "SCOPE: the SHORTER (middle-recension) text of each letter only … the longer recension … [is] OUTSIDE this row's scope", and its body: "Recension discipline is load-bearing: every quote from this row must be taken from the SHORTER (middle-recension) rendering and checked against the parallel longer text to confirm which is being quoted." This manifestation is also not in Doc_08 at all — Doc_08 Force 1B-1 cites no primary loci — so it was added at record-generation and never checked.

**Suggested fix.** Replace with the middle-recension wording and correct locus: `"Ignatius urging that the community 'be subject to the presbytery, as to the apostle of Jesus Christ' (Trallians 2)"`, and change `sources[].locus` to `"Trallians 2, 3; Magnesians 13 (…)"`. (Magnesians 13 and 1 Clement 42/44 both check out — verified verbatim.)

---

### 3. `pahc.force.two-ways-catechetical-inheritance` misquotes Didache 1:1

**File:** `records/pahc/force/pahc.force.two-ways-catechetical-inheritance.md` (`manifestations[0]`).

**What's wrong.** The record quotes: `"There are two ways, one of life and one of death; and great is the difference between the two ways"` (Didache 1:1). The edition this record's own source row names — ANF vol. 7 (Hall & Napier), vendored as `cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` — reads: "There are two ways, one of life and one of death; **but a great difference** between the two ways."

**What I checked.** Grepped the vendored file: the record's phrasing returns **zero** hits; the ANF phrasing returns one, at the Didache's own "First Commandment" opening. Read `records/pahc/source/pahc.source.didache.md` to confirm the named edition and to confirm this row already has a verbatim-checking precedent ("the prior build's verified quote pass … already checked Didache 1:2 wording verbatim against this vendored file"). Note the record's `sources[].locus` quotes only the first clause and *is* verbatim — so the defect is confined to the manifestation.

**Suggested fix.** Restore the edition's wording, or truncate the quotation at "one of life and one of death" (which is verbatim) and let the rest run as unquoted prose.

---

### 4. `pahc.force.martyrdom-meaning` presents a paraphrase as a quotation, and its own manifestation contradicts it

**File:** `records/pahc/force/pahc.force.martyrdom-meaning.md` (`description`).

**What's wrong.** The description reads "(ch. 18, describing the community collecting Polycarp's bones as **'more precious than the finest jewels'** and marking his dies natalis)". `manifestations[1]` of the same record quotes the same passage as **"more precious than the most exquisite jewels"**. Only the second is the text.

**What I checked.** `cic/texts/anf01…xml`, *Martyrdom of Polycarp* ch. XVIII: "we afterwards took up his bones, as being **more precious than the most exquisite jewels**, and more purified than gold." The string "more precious than the finest" returns zero hits in the file. Chapter number confirmed from the ThML heading ("Chapter XVIII.—The body of Polycarp is burned").

This wording is inherited verbatim from Doc_08 Force 2B-3, so Doc_08 carries the same slip — but the record does not need Doc_08 reopened to be fixed, and it already contains the correct string 20 lines below.

**Suggested fix.** In the description, change "finest jewels" → "most exquisite jewels". (Worth a one-line note to the project lead that Doc_08 §3 Force 2B-3 carries the same paraphrase-in-quote-marks, for a future Doc_08 touch — not a reason to hold this step.)

---

### 5. `pahc.force.boundary-drawing` upgrades the evidentiary claim on this world's thinnest gravity, under a false "mirrors exactly" disclosure

**File:** `records/pahc/force/pahc.force.boundary-drawing.md` (`confidence.divergence_note` and trailing body).

**What's wrong.** The body states: "sources and **confidence mirror that gravity record exactly**." They do not. The gravity twin's `divergence_note` ends:

> "…No level of grain — coarse or fine — clears the Documented bar martyrdom-meaning clears at its own narrowest scope: this gravity's own Formation test reads only 'Plausible… unestablished,' never 'Clearly.'"

The force record replaces that with:

> "…the underlying phenomenon (a real, live, unsettled boundary) **is well-evidenced**, but the evidence for it is substantively one voice."

"Well-evidenced" appears nowhere in Doc_08's characterization of Force 2B-4 / G05. In Doc_08 §5 (G05) "well-evidenced" attaches specifically to the *external* condition — "the tension is between **a well-evidenced external condition (rival movements, Documented)** and a thin, single-voice internal response (Ignatius alone, Inferential-Thin)" — i.e. it is exactly the half of the asymmetry that is *not* this force. The substitute sentence is also self-contradicting on its face ("well-evidenced, but… substantively one voice").

**What I checked.** Diffed the two `divergence_note` strings word by word; read Doc_08 Force 2B-4's Layer 1 confidence tag, §5's G05 entry, and §7's Inferential/Thin paragraph. The `formation_confidence` value itself (`Inferential-Thin`) is correct and matches both Doc_08 §7 and the gravity twin — only the note drifted.

**Suggested fix.** Restore the gravity twin's `divergence_note` verbatim (which the body already promises). If a shorter form is wanted, delete "is well-evidenced" and keep Doc_08's own framing: the external condition is Documented, the internal response is one voice, and that asymmetry is what keeps this Tensional.

---

### 6. `pahc.force.transmission-network`'s empty-`canon_cells` rationale is factually wrong and contradicted by its own sibling record

**File:** `records/pahc/force/pahc.force.transmission-network.md` (trailing body, and `canon_cells`).

**What's wrong.** The body concludes: "**No other cell in the fleet canon asks this force's specific question** (a participant would not ask 'why did your letters survive' the way they would ask about daily life, doctrine, or suffering), so this is left uncovered rather than forced onto a near-but-not-quite cell."

That is not true, and this build already knows it is not true: `_fleet.canon.f2-e-03` is "**Where is your own record thinnest?**", and `pahc.force.selective-canonization` — the Cell-3B counterpart to this very mechanism — claims **F2-E** on exactly that ground ("a close, direct match to this force's own content"). `_fleet.canon.f2-e-02` ("Isn't most of what's said about you legend, collected centuries later?") and `f2-e-04` ("What about the gospels that didn't make it in — were they suppressed?") are also on-topic. This record's own FORMATION IMPACT layer says the network "determined which portions of this world's own self-understanding are recoverable today at all" — which *is* the F2-E question.

**What I checked.** Read all 86 `records/_fleet/canon_question/*.md` records grouped by cell; read both transmission force records side by side. The record's separate F5-E reasoning is sound and should be kept: `GRAVITY-INDEX.md` line 63 does reserve F5-E for a future honest_limit/contested_claim tied to the G06 household rejection, and **no force record in this batch claims F5-E** — I confirmed the batch's full cell set is `{F2-E, F3-I, F3-T, F4-E, F4-I, F6-E}`.

**Suggested fix.** Either add `F2-E` to this record's `canon_cells` (the more consistent option — the two transmission forces are the same mechanism at two stages), or rewrite the body to explain why the ongoing-stage half is excluded from a cell its ending-stage half claims. Either way, delete the "no other cell in the fleet canon asks this" sentence; keep the F5-E paragraph.

---

### 7. `GRAVITY-INDEX.md` carries a statement this step made false, and regeneration will not fix it

**Files:** `world-build-docs/pahc/GRAVITY-INDEX.md` (§ "tension-with coverage"); root cause at `world-build-docs/pahc/generate_gravity_index.py` lines ~166–176.

**What's wrong.** The index reads: "**Doc_08 (not yet built for this world)** proposes state-pressure and boundary-drawing converge on a shared formative lesson… flagged for human review per the experimental tension-coverage gate's own discipline, **not resolved by inventing a relation here**."

Both halves are now stale. Doc_08 is approved *and* re-derived into records as of this step, and a relation from `pahc.gravity.boundary-drawing` to `pahc.force.state-pressure` now exists in the record (finding 1). Because the sentence is a hardcoded string in the generator rather than derived from the records, regenerating the index reproduces the stale text unchanged.

**What I checked.** Regenerated both indexes and diffed — byte-identical, confirming neither is hand-edited *and* confirming this string is generator-resident. Read `generate_gravity_index.py` lines 159–176 to locate the hardcoded text.

**Suggested fix.** Update the hardcoded string in `generate_gravity_index.py` and regenerate: state that Doc_08 is built and re-derived, that the schema edge now exists at `pahc.gravity.boundary-drawing → pahc.force.state-pressure`, and that it carries Doc_08's own interpretive-extension disclosure rather than a Doc_04 finding. Land this together with finding 1 so the record and the index say the same thing.

---

## COSMETIC findings

### 8. FORCES-INDEX confidence table overstates where its tiers come from

`FORCES-INDEX.md` line 72: "## Confidence summary (**Doc_08 Section 7 tiers**, restated per-force)". Four of fourteen rows do not match Doc_08 §7's tier placement:

| record | index/record value | Doc_08 §7 places it under |
|---|---|---|
| `martyrdom-meaning` (2B-3) | Contested | Inferential/Thin only |
| `alexandria-emergence` (3A-2) | Documented | Inferential/Thin only |
| `monepiscopacy-consolidation` (3B-1) | Contested | Documented or Widely Accepted |
| `selective-canonization` (3B-2) | Documented | Inferential/Thin only |

No record's value is *wrong* — each traces cleanly to that force's own Layer-1 confidence tag in Doc_08 §3, which is a legitimate source. The heading's provenance claim is what's inaccurate. Related and worth a decision: the batch has no stated rule for which half of a split Layer-1 tag becomes `formation_confidence` — three records took the higher half (2A-2, 3A-2, 3B-2), three took the lower (2A-1, 2B-3, 3B-1). **Fix:** retitle to "(each force's own Doc_08 §3 Layer-1 confidence tag)" and, optionally, record the split-tag rule in the generator's header comment.

### 9. FORCES-INDEX identity-pair attribution is right for one of four

All four lines in "## Identity pairs" read "per **Doc_08 Section 5's own explicit framing**, not a separate finding." Doc_08 §5 states the identity explicitly only for G03 ("This gravity *is* Force 2A-1 itself, per Doc_04's own framing"). For G01, G04 and G05, §5 lists connected forces and says nothing about identity — the identity is carried by the `(G01)` / `(G04)` / `(G05)` tags on the §3 Cell-2B force headings. The same overstatement sits in `generate_forces_index.py`'s `IDENTITY_PAIRS` comment. **Fix:** "per Doc_08 §3's own force headings (G01/G04/G05), and §5's explicit framing for state-pressure (G03)."

### 10. `generate_forces_index.py` — four internal inconsistencies, none affecting today's output

- Line 106 mixes a computed count with a hardcoded one: `f"**Total force records:** {len(ids)} (Doc_08 names 14; this index carries all 14)."` Add or remove a force and the sentence contradicts itself.
- Lines 57–61: the `NAMED_CONNECTIONS` comment claims "the schema's `relations[]` already carries these as `associated-with` edges" — which the generator's own output flatly contradicts for five of six ("NOTE ONLY (not a schema relations[] edge on both records)"). The output is correct; the comment is not.
- Lines 85–87: `kind_of()` is dead code, never called — and it is precisely the parse that would let `CELL_MAP` be *derived* from each record's own `name` suffix rather than hardcoded. I checked all fourteen name suffixes against `CELL_MAP` and they match exactly, so nothing has drifted yet; the duplication is the standing risk.
- Lines 195–199: the reciprocity line prints "checked against the full pahc record set, not force records alone", but the loop scans only force records' *outbound* relations. A gravity→force edge with no force-side reciprocal would still print "All force relations reciprocate." No such edge exists today — I verified all thirteen gravity→force edges reciprocate, and `gate_reciprocity` covers the full set — so the claim is currently true, just broader than the check behind it.

### 11. `pahc.force.neronian-persecution`'s empty-`canon_cells` reason is inaccurate

The body says "the Nero/persecution QUESTIONS the canon does ask — **F3-E**, F6-E — are answered by the state-pressure gravity and martyrdom records." `pahc.gravity.state-pressure` claims **F3-I**, not F3-E; F3-E is currently a blank cell in the coverage gate and contains no Nero or persecution question at all (its three are catacombs, Constantine, and "what would an outsider have found strangest about you?"). Leaving `canon_cells` empty here is still the right call; the stated reason isn't. **Fix:** cite `F3-I-03` ("Was it actually dangerous to be a Christian, day to day, or is that exaggerated?") and `F6-E` in place of F3-E.

### 12. One string in the batch reads as project scaffolding rather than world content

`pahc.force.alexandria-emergence.description` opens "HISTORICAL EVENT: **the Step 0 Conclusion** independently dates the Alexandrian Catechetical/Christian-Platonist Tradition (**World #2**)…". It is faithful to Doc_08 Force 3A-2's Layer 1, and nothing mechanical is violated: force/gravity `description` is deliberately outside `gate_no_build_attribution`'s `_ATTRIBUTION_FIELDS` map and outside `build_prompt()`'s compiled set, and I confirmed by scan that **no record in this batch carries an ISO date, a person's name, a "ruled by" attribution, or a stale status marker** in any field or body. Gravity descriptions already carry comparable build vocabulary ("per Doc_04's own final Interaction Matrix (round 7)"), so this is house style, not a leak. It is simply the one string that reads as build scaffolding rather than history. **Optional fix:** "a distinct neighbouring formation world centred on Alexandria, independently dated c. 190–254 CE," leaving the Step 0 provenance in `divergence_note`, where it already sits. The trailing-body process language elsewhere (e.g. `roman-mediterranean-world`'s "correcting an earlier draft pass") is sanctioned — the loader documents bodies as "provenance/build notes only."

### 13. "Mirrors exactly" is an overclaim in the other three identity records too

- `pahc.force.martyrdom-meaning` ("sources and confidence mirror that gravity record exactly") drops "on the Formation test's own terms ('Clearly formation-shaping')" and swaps "what the Formation test itself supports" → "what the evidence itself supports."
- `pahc.force.authority-consolidation` ("sources and core confidence … exactly") drops the gravity's closing Cross-Check sentence, and drops the Didache 15:1 manifestation while keeping `pahc.source.didache` in `sources[]` — so that row is now cited but unused in the record's own prose.
- `pahc.force.state-pressure` ("sources and core confidence … exactly") swaps the gravity's six-test caveat for the Decius date (which is itself faithful to Doc_08 Force 2A-1 Layer 1).

Each substitution is individually defensible and traceable; only the word "exactly" is wrong, and unlike finding 5 none of these changes an evidentiary claim. **Fix:** soften to "mirror … with the gravity-specific six-test/Cross-Check language dropped."

### 14. `pahc.force.selective-canonization` hedges only in `divergence_note`, not inline

Doc_08 Force 3B-2 flags "the specific causal claim that the settlement itself drove these particular selection outcomes" as "this document's own synthesis rather than directly attested." The record's `description` asserts it flatly ("as monepiscopacy and apostolic succession became this wider tradition's own settled self-understanding, later transmission favored the texts that supported that settlement… this is the direct mechanism behind…"). The disclosure is present and correct, but only in `divergence_note`. `pahc.force.contemporary-rival-movements` shows the house pattern of carrying exactly this kind of disclosure inline in the description ("though this reading is disclosed as this build's own interpretive extension"). **Fix:** add a matching clause to the FORMATION IMPACT layer.

### 15. Small additions beyond Doc_08 — noted, no fix required

`neronian-persecution` adds "theatrical" to Doc_08's "brutal executions" (defensible from Tacitus, but not Doc_08's word) and carries an editorial judgment as `manifestations[2]` ("the closest thing this world has to an origin event") rather than a manifestation. `monepiscopacy-consolidation` and `systematic-theological-mode-elsewhere` flatten Doc_08's "a Strand A or Strand B member" to "a member." `contemporary-rival-movements` keeps Doc_08's "already a mature concern by 177 CE" but drops the anchor that dates it (the Lyons/Vienne martyrs' letter to Bishop Eleutherus). None changes a claim's meaning or confidence.

---

## What I checked and found clean

Recorded so a later reviewer does not repeat it:

- **Gate battery** (`gates.run_all` over `load_world_records("pahc")` + `load_fleet_records()`): clean on all thirteen gates except `canon-coverage`, which reports the same 18 blank cells as before this batch. Those cells are structurally untouchable by force records — `canon.substantive_types()` is `{doctrinal_witness, term, story, quote}` — so this is the unchanged Step 7/8 backlog, not a new gap.
- **Reciprocity, verified by hand in both directions**, not taken from the generated claim: 13 force-record outbound edges and 13 gravity-record outbound edges to forces, every one reciprocated, no duplicates, no dangling or misdirected targets. `git diff HEAD~1 HEAD -- records/pahc/gravity` confirms the five gravity records received **additions only** — nothing deleted or reordered.
- **Completeness and placement:** all 14 Doc_08 forces present; cell assignment (1A-1/1A-2, 1B-1/1B-2, 2A-1/2A-2, 2B-1…2B-4, 3A-1/3A-2, 3B-1/3B-2) matches Doc_08 §3 exactly; `kind` (`initiating`/`ongoing`/`ending`) correct for every record; `CELL_MAP` in the generator matches every record's own `[nX - …]` name suffix.
- **No invented connections:** every `relations[]` edge checked against Doc_08 §5's per-gravity connected-force lists or §4's named connections — G02←{1A-1, 2B-2, 1A-2}, G07←{2B-1, 2B-4}, G01←{1A-2, 1B-1, 2A-1}, G04←{2A-1, 2B-1, 1A-1}, G05←{2A-2, 2A-1, 2B-1}, plus Connection 6 as the one force↔force edge. `monepiscopacy-consolidation → gravity.authority-consolidation` is not in a §5 list but is stated directly in Doc_08 Force 3B-1's Layer 3 ("the resolution … of G01's own defining tension") — traceable, not manufactured.
- **The six Named Connections' realization status** as printed in FORCES-INDEX ("NOTE ONLY" ×5, "declared" ×1) is accurate to the records as written.
- **All six chosen `canon_cells` are genuine close matches** to real canon-question text: F4-E↔`f4-e-01`, F4-I↔`f4-i-01`, F3-T↔`f3-t-02`, F3-I↔`f3-i-01`/`f3-i-03`/`f3-i-04`, F6-E↔`f6-e-02`, F2-E↔`f2-e-03`. The quoted question text in each record's body matches the fleet record verbatim.
- **F5-E is not claimed by any force record** — the reservation for the future G06-linked honest_limit/contested_claim is intact.
- **Both indexes regenerate byte-identical** — no hand-editing of either generated file.
- **Quotations and loci verified verbatim against the vendored ThML** (beyond the three defects above): Ignatius *Ephesians* 4 (harp — and confirmed shorter recension by "worthy of God" vs the longer's "being worthy of God"); *Trallians* 9 ("Stop your ears…"; "He was truly persecuted under Pontius Pilate; He was truly crucified"); *Smyrnaeans* 7 (eucharist/flesh); *Romans* 4 (confirmed shorter recension by the "pure bread of **Christ**" discriminator the source row itself names); *Martyrdom of Polycarp* 18 and 4 (Quintus; "those who give themselves up"); Hermas *Vision* 2.4.3 ("presbyters who preside over the Church"); 1 Clement 5 and 42; Polycarp *Philippians* 13 (forwarding at the Philippians' request); Barnabas 18–20; Didache 15:1; Tertullian *Adv. Marcionem* 1.19 (chapter heading confirms "Some CXV. Years After Christ" — the c. 144 computation, correct locus); Irenaeus *Adv. Haer.* 3.11.8 (four-Gospel argument).
- **Source-record use disciplines honoured:** `contemporary-rival-movements`' claim that all three of its witnesses are hostile-or-later "per each source's own USE DISCIPLINE" is true — all three rows carry one, and the anti-Montanist row independently supports the "synods of Asia Minor bishops" language the manifestation uses. `systematic-theological-mode-elsewhere` uses Irenaeus within permitted use (3) of that row's discipline ("his mode itself as the closing marker").
- **Deliberate thinness honestly disclosed:** `alexandria-emergence` (empty `sources[]`/`relations[]`) and `monepiscopacy-consolidation` (Roman half unsourced) both state plainly, in `divergence_note` *and* body, that no primary text in this world's registry evidences the claim. Neither passes a comparative or secondary claim off as directly sourced.

---

## Round-2 verification

Performed by this build thread directly (Read/Grep/Bash), not re-dispatched as a second agent — the same precaution taken at Steps 4 and 5 after the Step 4 round-2 agent hit a session-limit API failure mid-run: same discipline, check each fix against the actual file content, don't trust a fix-list summary.

**All 7 SUBSTANTIVE findings, fixed and verified:**

1. **`pahc.gravity.boundary-drawing` assert/deny contradiction** — fixed. The description's Interaction paragraph now separates the unchanged Doc_04 gravity-level "no demonstrated relationship with state-pressure" finding from the new Doc_08 Connection-5 force-level edge, and states explicitly that the two are different grains, not a contradiction. The trailing body adds a matching disclosure. `GRAVITY-INDEX.md`'s hardcoded tension-with-coverage string (finding 7) was fixed in the same pass so both the record and the index now say the same thing — confirmed by grep, no remaining "not yet built for this world" or undisclosed-edge language anywhere in either file.
2. **`apostolic-testimony-inheritance` wrong recension/locus** — fixed. `sources[].locus` now reads "Trallians 2 (shorter recension)"; the description and `manifestations[1]` now quote the shorter recension's actual singular wording ("as to the apostle of Jesus Christ"). Grepped for the old "Trallians 3" and longer-recension plural string — zero live hits (only in the trailing FIXED-note describing the correction itself).
3. **Didache 1:1 misquote** — fixed. `manifestations[0]` now reads "but a great difference between the two ways," matching the vendored ANF wording exactly. Grepped for the old "and great is the difference" — zero live hits.
4. **`martyrdom-meaning` "finest jewels"/"most exquisite jewels" contradiction** — fixed. The description now reads "most exquisite jewels," matching `manifestations[1]` and the vendored text. Grepped the live YAML fields — zero remaining "finest jewels" outside the trailing FIXED-note.
5. **`boundary-drawing` false "well-evidenced" divergence_note** — fixed. Parsed the record's actual YAML (not just grepped prose) to confirm `confidence.divergence_note` itself was restored to the gravity twin's own framing ("No level of grain... clears the Documented bar... never 'Clearly.'"), removing the self-contradicting "well-evidenced... substantively one voice" sentence. Confirmed via direct `yaml.safe_load` of the field, not a text search that could miss a field-vs-body distinction.
6. **`transmission-network` false "no other cell" claim** — fixed. `canon_cells` now includes `F2-E`, matching its sibling `selective-canonization`. The trailing body no longer claims no cell matches; it now cites `_fleet.canon.f2-e-03` directly and explains the F2-E/F5-E distinction that remains correct (F5-E still reserved, still unclaimed by any force record — reconfirmed by cell-set scan below).
7. **Stale `GRAVITY-INDEX.md` hardcoded string** — fixed together with #1 above.

**Regression checks:**
- Full YAML parse sweep: all 72 pahc record files parse cleanly (no syntax regressions from the fix edits).
- Full gate battery (`gates.run_all` over `load_world_records("pahc")` + `load_fleet_records()`): clean on all 13 gates except `canon-coverage`, reporting the exact same 18 pre-existing blank cells as before this step's first commit — no new gaps, no new false-positive coverage claims. The batch's covered-cell set is confirmed unchanged in kind (`{F2-E, F3-I, F3-T, F4-E, F4-I, F6-E}`) and F5-E remains uncovered by any force record.
- Both indexes regenerate byte-stable given the fixed records (re-ran `generate_gravity_index.py` and `generate_forces_index.py`); `FORCES-INDEX.md` reports `non-reciprocal: 0` and `unplaced: 0`; `GRAVITY-INDEX.md` reports `isolated: 0` and `non-reciprocal: 0`.
- Reviewer's cosmetic findings 8, 9, 10 (confidence-summary heading provenance, identity-pair attribution overstatement, `generate_forces_index.py`'s dead `kind_of`/stale comments/narrower-than-claimed reciprocity check), 11 (`neronian-persecution`'s wrong F3-E citation), 13 (the "mirrors exactly" overclaim in `martyrdom-meaning`, `authority-consolidation`, `state-pressure`), and 14 (`selective-canonization`'s hedge missing inline) were also addressed: the generator's confidence-summary heading and identity-pairs section now state their actual provenance, `kind_of` was replaced with a used `cell_of` that cross-checks `CELL_MAP` against each record's own name suffix at generation time (drift now surfaces automatically rather than needing manual review), the reciprocity check now genuinely scans both force→gravity and gravity→force directions to match its own printed claim, `neronian-persecution` now cites F3-I-03 instead of the nonexistent match at F3-E, the three identity records' trailing bodies now say "mirror" rather than "mirror exactly" and name what was condensed or added, and `selective-canonization`'s causal-synthesis hedge is now stated inline in the description as well as in `divergence_note`. Cosmetic findings 12 and 15 were left as-is per the reviewer's own "optional"/"no fix required" framing.

**Verdict: All 7 SUBSTANTIVE and all addressed COSMETIC findings LANDED CORRECTLY, confirmed against live file content and a clean re-run of the full gate battery. Step 6 ready for disposition.**
