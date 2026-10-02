# Doc_06 (Full Lexicon Development) — Round 1 Independent Adversarial Review
## The Reformed Cities — Zurich & Geneva

**Reviewed:** `Doc_06_Full_Lexicon_Development.md`, six built chunks (`rzglex001`, `004`, `005`, `007`, `008`, `012`), `Lexicon_Deployment_Index.xlsx`.
**Reviewer stance:** independent adversarial review per `cic-build-cycle`. Every quotation cited below was re-verified directly against the vendored `.txt` file at the exact line(s) claimed — not accepted on the chunk's own "independently re-verified" assertion.

---

## Verdict: **Substantial revision required**

No fabricated quotation and no regression on any of this world's three previously-caught, specifically-flagged defects ("beatifies," the Second Helvetic "mirror" line-677→684 correction, Institutes IV.3.9→IV.3.8) was found — all four re-verify clean. That is real, checked good news. But the review surfaces four **High**-severity defects that repeat this world's own established defect *pattern* (misattributed/inapposite cross-references; an unvendored institutional-history claim narrated as if grounded; a master index that has already drifted from the chunk files it is supposed to derive from) rather than inventing a new category of problem. Given this project's explicit "no fix on a fix" / "find and fix the root cause" discipline and this world's now three-time-repeated history of exactly this class of defect, these findings warrant a real revision pass, not a cosmetic patch, before this document proceeds.

---

## Findings

### Finding 1 — HIGH — Doc_06's "carried inside" claim for Providence is false; the built chunk does not actually carry it

**Checked:** Doc_06 §1, row 3 (Providence), claims: *"Providence's own doctrinal content is carried inside the `rzglex001` entry's own World Meaning section rather than separately promoted, the same 'carried inside, not separately promoted' pattern Donatism used for closely related Tier-2 terms."* I checked this claim against the actual built `rzglex001_predestination-election.md` file, not just Doc_06's assertion of it.

**Found:** `grep -in "providence" rzglex001_predestination-election.md` returns exactly three hits, and none of them is doctrinal content about Providence:
1. The front-matter `Related-Terms` list (just the word, no content).
2. The front-matter `Do-Not-Retrieve-When` line: *"participant is asking generally about God's own providence over ordinary events without reference to salvation specifically (see Providence)"* — which explicitly **routes Providence-related questions away** from this chunk to a not-yet-built entry, the opposite of "carried inside."
3. The Related-Terms Reciprocity Note, which lists Providence as "Not yet built as chunks."

The chunk's actual `World Meaning`, `Ecological Function`, and `Distortion Risk` sections contain no discussion of God's continuous governance of creation, Institutes Book I, or anything else that is Providence's own doctrinal content per Doc_03 §1's definition ("God's own continuous, active governance of all created things, not a distant first cause"). Doc_06's own table makes a specific, checkable claim about a companion artifact's contents, and the claim is false.

**Why it matters:** this is not merely a documentation nicety — it has a real retrieval consequence. A participant asking about Providence is, per this chunk's own `Do-Not-Retrieve-When` line, supposed to be directed to a "Providence" entry that does not exist yet (Tier 2, unbuilt). Providence's doctrinal content is currently **nowhere** in the deployed lexicon, contrary to Doc_06's explicit representation that it is "carried inside" `rzglex001`. This is exactly the misattributed-content-claim pattern already caught twice in this world's build (Doc_03 Round 1's fabricated cross-references) recurring in a new form.

**Fix required:** either (a) add an actual paragraph on Providence's own doctrinal content to `rzglex001`'s World Meaning (matching Doc_06's own claim), reconciling the `Do-Not-Retrieve-When` line with that content, or (b) correct Doc_06 §1 row 3 to honestly state that Providence's content is *not yet built anywhere*, not "carried inside" — a disclosed deferral rather than a false completeness claim. Do not leave the current contradiction standing.

---

### Finding 2 — HIGH — Both cited "established practice" precedents for the two Tier-1 merges and the Sola Scriptura promotion are inapposite or overstated

**Checked:** Doc_06 justifies (a) the Predestination/Election merge by appeal to *"this project's own established practice for tightly-paired terms (e.g. Donatism's `donlex001` 'Traditor / Traditio')"* and (b) the Sola Scriptura promotion by appeal to *"the same reasoning Donatism's own Doc_06 used to promote Refusal of Imperial Legitimacy."* I pulled Donatism's actual Doc_03 and Doc_06 to verify both precedents rather than accepting the citation at face value, given this world's own history of misattributed cross-references.

**Found, precedent (a) — false analogy.** Donatism's Doc_03 lists "Traditor / Traditio" as **one single candidate row** from the very start — one tier, one tag set, one one-line definition, one AG-risk entry (`Doc_03 §1`: *"Traditor / Traditio | 1 | AS DR TC RT | One who surrendered scripture..."*). It was never two independently-tracked Doc_03 candidates that Doc_06 later merged. This is fundamentally different from `rzg`'s own Predestination/Election, which Doc_03 tracked as **two separate numbered rows**, each with its own tier, tag set, one-line world-meaning, and AG-risk assessment, and which Doc_03 §5 explicitly named among the terms "most likely to need full three-level treatment and deployment chunks." There is no actual Donatism precedent for merging two independently-tracked Tier-1 candidates into one chunk — the citation names a precedent that, on inspection, does not establish what Doc_06 says it establishes.

**Found, precedent (b) — overstated.** Donatism's Doc_04 §7 **explicitly forwarded** the Refusal of Imperial Legitimacy reconsideration to its own Doc_06 (quoted directly in Donatism's own Doc_06: *"Doc_04 §7 explicitly forwards this reconsideration ('supports reconsidering [Refusal of Imperial Legitimacy's Tier 2 status]... alongside the other five terms just named')"*). By contrast, `rzg`'s own Doc_04 §7 and Doc_05 §11 forwarding notes to Doc_06 **both** list the confirmed Tier-1 set as "Predestination, Election, Disputation, The Lord's Supper, Sign and the Thing Signified, Consistory" — Sola Scriptura is not in either list. Doc_06 itself is honest that this is a decision "Doc_04/Doc_05 did not make explicitly," but then reaches for a precedent that had a *materially stronger* evidentiary basis (an explicit prior-document recommendation) than `rzg`'s own case actually has (an after-the-fact inference from G3's classification alone). Presenting this as "the same reasoning" overstates how analogous the two situations are.

**Why it matters:** none of this makes the underlying decisions wrong on their own terms — see Findings 3 and 4 below, both of which find the merges and the promotion independently defensible on Doc_03's and Doc_04's own definitions. The problem is specifically that Doc_06 leans on borrowed procedural legitimacy from precedents that do not actually hold up, instead of owning these as first-of-their-kind interpretive calls for this world — precisely the misattributed/inapposite-cross-reference pattern this world's build has now been caught on three separate times (Doc_03 Round 1, Doc_04 Round 1, now here).

**Fix required:** either drop the two precedent citations and argue the decisions on this world's own Doc_03/Doc_04 evidence directly (which, per Findings 3–4, is available and reasonably strong), or correct the citations to state accurately what each Donatism precedent actually shows and does not show.

---

### Finding 3 — MEDIUM — The two merges are defensible on Doc_03's own definitions but are a real interpretive choice in tension with Doc_03's own signals, not a foregone reading

**Checked:** whether merging Predestination+Election (`rzglex001`) and The Lord's Supper+Spiritual Presence (`rzglex007`) is a defensible reading of Doc_03 §1's own one-line definitions, per the review brief, and whether it loses distinctions Doc_03 intended to keep separate.

**Found — supports the merge:** Doc_03 §1's own definitions do read as "one gravity, two angles." Election is defined there as *"the positive term Predestination's own decree names from the chosen side"* (quoted accurately by Doc_06), and Spiritual Presence is defined as *"the mature Reformed answer negotiated between Zwingli's earlier... reading and Calvin's own developed position"* (also quoted accurately). Doc_04's own gravity *names* reinforce this independently and more strongly than anything Doc_06 actually cites: G1 is named "**Sovereignty of God / Predestination and Election**" and G2 is named "**Spiritual Presence and the Rejection of Corporeal/Sacrificial Mediation**" — both gravities are already named as compounds in Doc_04, without Doc_04 ever treating the two lexicon terms as separately organizing forces.

**Found — cuts against treating the merge as obviously mandated:** Doc_03 §5 explicitly flagged **seven** separate Tier-1 candidates for "full three-level treatment and deployment chunks," listing Predestination, Election, The Lord's Supper, and Spiritual Presence as four of the seven named items, not as two compound items. Doc_03 §6 also names an anticipated four-way cross-reference cluster — "Sign and the Thing Signified↔Spiritual Presence↔Memorial↔Mutual Consent" — that reads Spiritual Presence as its own cross-referenced node sitting alongside Sign and the Thing Signified, not as content folded inside a Lord's Supper entry. Doc_06 does not address this tension anywhere; it quotes Doc_03's one-line definitions but not Doc_03 §5/§6's own listing behavior, which points the other way.

**Assessment:** the merge is a reasonable, disclosed judgment call, not a violation of anything Doc_03 explicitly forbids — but it is exactly the kind of decision the review brief warned "none of them were explicitly mandated... and could each be wrong." Doc_06 presents it as more obviously correct than the record actually shows by omitting the Doc_03 §5/§6 counter-signal. This should be named explicitly in a revision, not left for a future reader to discover on their own.

**Fix required:** add one sentence acknowledging Doc_03 §5/§6's own separate-listing behavior and stating explicitly why Doc_06 judges the compound-gravity-naming evidence (Doc_04) to outweigh it. This costs little and closes the gap.

---

### Finding 4 — MEDIUM — Sola Scriptura's promotion rests on real Tier-1-quality gravity evidence, but the built chunk's own Key Sources are asymmetric and partly recycled, not fresh Tier-1-strength grounding

**Checked:** whether the Sola Scriptura promotion is well-reasoned per Doc_04 (item 1 of the review brief), and whether `rzglex005`'s own built content actually supports Tier-1 depth or reads thin.

**Found:** the promotion's headline quote is accurate — Doc_04 §4's index table does say, verbatim, of G3: *"Documented, no significant divergence — the strongest cross-strand candidate in this document"* (independently confirmed against Doc_04 §4, row 3). G3 genuinely is Doc_04's cleanest Primary gravity. On that basis, the promotion argument is sound in principle.

However, the built chunk's own Key Sources section is not symmetric in the way a promoted, cross-strand-anchoring Tier-1 term should be: it offers a specific, line-pinpointed, freshly re-verified quotation for the **Zurich** side (the Sixty-Seven Articles preface, lines 4487–4493) — but this is the *identical* quotation, at the *identical* citation, already used as `rzglex004`'s (Disputation's) own Key Source. For the **Geneva** side — the half of the cross-strand claim the promotion specifically rests on — the chunk offers only an unpinpointed, generic reference: *"Calvin's Geneva Catechism and the Institutes throughout (Registry rows 1–4)."* No specific line, no specific quotation, grounds the Geneva enactment this term is promoted to represent. For a term whose promotion argument is explicitly "this is the strongest *cross-strand* gravity," a Key Sources section with a precise Zurich citation and an imprecise, non-committal Geneva citation is thinner than the claim it is meant to support.

**Fix required:** add at least one specific, line-cited, independently re-verified quotation from Calvin's Geneva Catechism or Institutes illustrating the Geneva-strand enactment of Sola Scriptura (catechesis-as-scriptural-authority), parallel in specificity to the Zurich-side citation already present.

---

### Finding 5 — HIGH — `rzglex012` (Consistory) narrates specific Geneva institutional/political history that its own Key Sources section says it does not have grounds to narrate

**Checked:** per the review brief's explicit instruction (item 7), whether the Consistory chunk has let Geneva-specific institutional detail creep back in as though vendored — an exact overclaim this world's build has already caught and fixed twice (Doc_03, Doc_05).

**Found:** the chunk's own Key Sources section states, carefully and correctly: *"Geneva's own specific 1541 institutional practice — actual composition, weekly sessions, real case history — rests entirely on the still-unacquired 1541 Ecclesiastical Ordinances... and is not narrated here beyond what the general doctrine itself supports."*

But the World Meaning section's second paragraph then does exactly this: *"The council itself tried, at points, to claim the authority to judge who might come to the Lord's own table — and the Consistory did not yield that judgment... That fight, the Perrinist crisis, was substantially resolved in the Consistory's own favor only by 1555, a full generation after Calvin's own 1541 recall."* This is a specific historical/political narrative about the Consistory's actual case history (a named dispute, a named resolution date) — precisely the category ("real case history") the chunk's own Key Sources section says is not narrated here. Nothing in the chunk's Key Sources cites a source for this narrative; its only two cited sources are two Institutes quotations that say nothing about the Perrinist crisis.

Tracing it back: the Perrinist-crisis/1555 claim does exist in already-approved upstream material (Doc_01 §2's "Historical Catalysts," restated in Doc_04's T1 discussion) — so this is not invention from nothing, and Doc_01/Doc_04 are correctly out of scope to reopen here. But the chunk itself does not disclose that lineage; a chunk consulted in isolation (the standard this project holds every chunk to, per its own Related-Terms Reciprocity Note discipline) presents this specific institutional-history claim with no source at all, directly beside a Key Sources paragraph that says exactly this kind of claim is *not* supported. That is an internal contradiction inside one chunk file, and it is the same overclaim category flagged for this exact term twice before, now recurring in a new location (World Meaning narrative rather than a Key Sources mischaracterization).

**Fix required:** either (a) add an explicit citation in Key Sources to the Doc_01 §2 / Doc_04 §3.4/T1 lineage for the Perrinist-crisis sentence, naming it plainly as carried-forward general-historical-background rather than vendored-primary-source content, or (b) remove the specific case narrative from World Meaning and confine World Meaning to the general doctrine the Key Sources section actually supports, consistent with the chunk's own stated discipline.

---

### Finding 6 — HIGH — `Lexicon_Deployment_Index.xlsx`'s Lexicon sheet has already drifted from the built `rzglex007` chunk's own front-matter tags, and this propagates into the By Tag sheet

**Checked:** per the review brief's item 10 and the lexicon-index skill's own top review question ("Is the master index actually derived from the same chunk files, not a separately-maintained list that's already drifted from them?"), whether the xlsx's per-term rows match each built chunk's own declared front-matter, read directly with `openpyxl`.

**Found:** `rzglex007_the-lords-supper-spiritual-presence.md`'s own front matter declares `Tags: SC, DR, TC, RT, PV` (five tags). The Lexicon sheet's row for `rzglex007` ("The Lord's Supper," Chunk-File-Built = yes) shows `AS=no, SC=yes, DR=yes, TC=no, RT=yes, PV=no, CT=no` — **missing both TC and PV**, which the actual built chunk carries. (The reserved-merged `rzglex009` row does carry `TC=yes`, but that row is marked "merged into 007," not the live built entry, and still doesn't carry `PV`. No row in the sheet reflects the chunk's actual, combined tag set.) All five other built chunks (`001`, `004`, `005`, `008`, `012`) were checked the same way and match their own front matter exactly — this is an isolated but real drift specific to the merged Supper entry.

This is not cosmetic: the "By Tag" sheet is computed from the Lexicon sheet's own rows, so its **TC** list (14 terms) and **PV** list (2 terms: "Memorial / Commemoration, Mutual Consent") both silently omit "The Lord's Supper" even though the live, built chunk actually carries both tags. Anyone using the By Tag sheet to answer "show me every TC-tagged term" or "every PV-tagged term" — the exact use case the lexicon-index skill names as the whole point of building these views — gets an answer that is wrong for this one entry.

**Fix required:** update the Lexicon sheet's `rzglex007` row to `TC=yes, PV=yes` (matching the built chunk's own front matter), regenerate the By Tag sheet from the corrected row, and add a build-script check that a merged entry's Lexicon-sheet tag row is the union of, or is explicitly re-derived from, the actually-built chunk's own front matter rather than either original Doc_03 candidate row.

---

### Finding 7 — MEDIUM — `rzglex008`'s Author-Gravity-Risk value in the master index is inconsistent in format and appears unsupported

**Checked:** per the lexicon-index skill's instruction that "the Author-Gravity-Risk column in the index actually match[es] what each chunk's Key Sources section says," each Tier-1 row's Author-Gravity-Risk value against its chunk's own Key Sources.

**Found:** every other Tier-1 row in the Lexicon sheet carries either `None` (no concentration) or a descriptive value naming the dominant source (e.g., `"Calvin/Beza (systematized form)"`, `"Calvin (fullest statement)"`). `rzglex008`'s row alone carries the bare string `"yes"` — a different, boolean-style format not used anywhere else in the column. Checked against the actual chunk: `rzglex008`'s Key Sources section discloses no single-source dominance at all (its two cited sources are the Consensus Tigurinus itself — explicitly the one document in this world's corpus *jointly authored across the strand boundary*, the opposite of single-source concentration — and the document's own title page). Doc_03's own AG-risk column for this candidate was `"—"` (none). Nothing supports marking this row `"yes"`.

**Fix required:** correct `rzglex008`'s Author-Gravity-Risk cell to blank/`None` (or a substantive "no concentration — jointly authored" note), and normalize the column to one consistent format across all rows.

---

### Finding 8 — LOW / COSMETIC — Two quotation-practice nitpicks (not fabrication, but worth tightening given this world's zero-tolerance history)

**8a.** `rzglex007`'s Key Sources quotes Zwingli's Sixty-Seven Articles Art. XVIII as *"Christ, having sacrificed himself once, is to eternity a certain and valid sacrifice..."* The vendored text actually reads *"That Christ, having sacrificed himself once..."* — the leading word "That" (part of the article's own numbered-clause grammar) is dropped without an ellipsis or bracket marking the elision. The remainder is verbatim. Not a meaning-changing edit, but per this world's own "every quotation re-verified character-for-character" standard, a silent word-drop at the start of a quotation should be marked, not silent.

**8b.** `rzglex001`'s "beatifies" quotation is cited as "(line 9678, verbatim)." Independently re-verified: the quoted sentence in fact begins on line 9677 ("...you will ever say : God's election, predestination or marking out, calling,") and the word "beatifies" itself falls on line 9678. The quotation is accurate and the fabrication this world was previously caught on ("[justification]" for "beatifies," Doc_04 Round 1) has **not** regressed — but the line citation identifies only where the quotation's most distinctive word falls, not where the quoted sentence starts. A precise citation would read "lines 9677–9678."

**8c.** `rzglex005`'s Sixty-Seven Articles preface citation gives "lines 4487–4493"; the quoted material (independently re-verified, content accurate) actually runs lines 4487–4492 in the vendored file. Off by one line at the boundary.

None of these affect the substance of any claim; they are flagged only because this world's own build history treats citation precision as load-bearing, and a reviewer should not wave off small drifts in a world with this specific track record.

---

## What checked clean (stated explicitly, not left implicit)

- **No regression on any of the three specifically-flagged prior defects.** The "beatifies" quotation (`rzglex001`) reads correctly, not "[justification]." The Second Helvetic "mirror" quotation is cited at line 684 (independently confirmed exact), not the previously-wrong 677. The Institutes citation in `rzglex012` correctly reads IV.3.8 with lines 2831–2832, not the previously-wrong IV.3.9.
- **Every other direct quotation in all six chunks re-verified character-for-character** against the actual vendored file at the cited line(s): the Consensus Tigurinus 9th Head of Agreement (lines 768–770, exact), Article XVIII "About the Mass" (lines 4564–4568, exact modulo Finding 8a), the Sixty-Seven Articles preface (lines 4487–4492/93, exact modulo Finding 8c), and the four "sacrifice of the mass" locus citations in Institutes vol. 3 (all confirmed present at the cited lines).
- **CT Contest Type (item 8 of the brief):** `rzglex008` states a real, specific contest under the "Meaning" type (per the template's four types), matching Doc_06 §2 and Doc_03 §4 exactly — not left as filler.
- **No analytical-distance markers found in any World Meaning section** across all six chunks. The one "scholarly contest" phrasing found is inside `rzglex008`'s CT Contest Type section, which the brief explicitly permits to use that register.
- **rzglex002/009 reserved-not-reused numbering** is applied consistently between Doc_06's own narrative and the xlsx Lexicon sheet (both mark "merged into 001"/"merged into 007").
- **8/7/4 Tier breakdown**: the xlsx's own "By Tier" sheet independently computes 8/7/4/19, matching Doc_06 §1's table row-by-row exactly (verified by reading the xlsx directly with openpyxl, not by trusting Doc_06's narrative claim).
- **Related-Terms reciprocity (item 9 of the brief):** every pair Doc_06/the chunks claim as "Mutual" is genuinely mutual, checked both directions across all five built-chunk pairs (Predestination/Election↔Sola Scriptura; Predestination/Election↔Lord's Supper/Spiritual Presence; Disputation↔Sola Scriptura; Lord's Supper/Spiritual Presence↔Sign and the Thing Signified). The one claimed one-directional pair (Consistory→Sola Scriptura) is genuinely one-directional: `rzglex012` lists Sola Scriptura, but `rzglex005`'s own Related-Terms field does not list Consistory back — confirmed by reading both chunk files directly, and this matches the xlsx's own Related-Terms Reciprocity sheet exactly.
- **CT Contest-Type Check sheet** (xlsx) matches the chunk and Doc_06 exactly: 1 of 1 CT-tagged term, contest specified.

---

## Summary

Doc_06's citation discipline holds up well where this world has been burned before (no regressed fabrication on any of the three specifically-flagged prior defects), and its arithmetic and CT/reciprocity bookkeeping are genuinely accurate, not merely asserted. But four High findings recur in the *same family* of defect this world's build has now shown three times — misattributed/inapposite cross-references (Finding 2), a false claim about a companion artifact's own content (Finding 1), unvendored Geneva-specific institutional narrative slipping past its own chunk's stated limits (Finding 5), and a master index already out of sync with a built chunk's own front matter (Finding 6) — plus two Medium findings on the substantive strength of the merge and promotion decisions themselves (Findings 3–4) and one Medium index data-quality issue (Finding 7). This pattern, not any single finding in isolation, is why the verdict is substantial revision rather than cosmetic cleanup.

**Escalation categories:** none apply. This is ordinary sourcing-fidelity and structural-consistency work — no Representative identity/title/voice question, no cross-world/portfolio-level decision (Donatism material was consulted only to verify a citation, not to make a decision about it), no governance/methodology change, and no unresolved tension the pipeline itself cannot close (every finding above has a concrete, closeable fix named).
