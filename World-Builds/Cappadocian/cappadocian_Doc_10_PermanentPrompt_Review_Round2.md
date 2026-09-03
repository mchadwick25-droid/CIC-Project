# Doc_10 Permanent Prompt — Independent Round 2 Review (fix verification)

**Artifact:** `cappadocian_Representative_Permanent_Prompt_Eumathios.txt` at commit `fb291957` (27 paragraphs, 3,993 words, ~5,380 est. tokens)
**Baseline:** `e3fca0dd`, reviewed in `cappadocian_Doc_10_PermanentPrompt_Review_Round1.md`
**Method:** every claim below checked against the file and the named ground-truth document; no fix accepted on assertion.

## Item-by-item

**1. H1 — reserve argument / false unanimity — FIXED.**
The doxology paragraph now carries the argument, and it traces. Doc_06 §17 ("defended by his friend and resented by allies") and World Profile §92 ("defended by his friend, resented by others") are both instantiated, and Construction Notes §1's supplied sentence is carried near-verbatim:

> "We were not of one mind about how to answer it. One of our greatest teachers would not call the Spirit God outright... His own closest friend defended him for it. Others among us resented the silence and pressed to say the word plainly, now, whatever it cost. Both sides loved the same Spirit... Through that same argument, unresolved among us, our churches held the song the way farmers hold seed through winter."

"Our churches held the song" is no longer unanimous — it is now explicitly held *through* an unresolved argument. Tensional Gravity 9 is present. One residual on motive-confidence: see NEW-M2.

**2. H2 — two template-mandatory sections — FIXED, and cleanly.**
The five Section 1 backstop paragraphs were diffed word-for-word against template lines 192–261. Paragraphs 1–4 are **byte-identical**; paragraph 5 differs by exactly one token, a hyphenation artifact from the template's own line-wrap (`first- person-singular` → `first-person-singular`). That is the "should not be paraphrased, shortened, or removed" requirement met literally, not loosely.

Placement is correct on both counts. The backstop sits at P4–P8, between the pronoun/disagreement paragraph (P3) and the temporal horizon (P9) — the template's exact order. Section 2A sits at P18, after the formation/world content (P10–P17) and immediately before "When you take up a question..." (P19).

Section 2A's five anchors are all Native, all traceable to specific Source Registry rows: famine homilies (rows 16, 34), the Forty homilies (rows 20, 53), the Asketikon's Q&A (row 18), *Against Eunomius* (rows 14, 42), *Life of Macrina* (row 48). Nothing fabricated; nothing reaching into Named Comparanda. The refusal clause names the three Excluded comparanda from Doc_01 line 50 *obliquely*, as the template requires:

> "...from some other room — a desert not ours, a city not ours, a settlement some later century made its own."

Egyptian desert corpus, Athanasius' Alexandria, Evagrius' later corpus / later Basilian codifications — none named directly. The Macrina anchor even carries its mediation marker ("as her own brother set it down after her death").

**3. M1 — Eupsychius placement — FIXED.**
P16 (the feast/shrine paragraph) now names it plainly: *"Eupsychius' own feast at Caesarea among them, kept every year for the one of us the persecutor still took after the peace had come."* P1 was trimmed from five sentences to one and now runs 154 words / ~208 tokens, back inside the template's 150–200 target. The trim also silently retired the "the last we ever saw" ambiguity the first review flagged under judgment call 1.

**4. M2 — 381–394 own conduct vs. post-394 void — FIXED.**
Two distinct claims, in order, in P23:

> "Even the years just after our victory, while our great ones still lived, are thin in what we can tell you of our own conduct with the power we were given — we say so plainly, rather than claim we used it well or ill. And of the years after our great ones died... we know almost nothing."

Matches Forces §169 ("the world's *own* exercise of power after 381... named as an honest gap") and Construction Notes §3's Critic Finding 7 item, including the refusal to improvise innocence or guilt.

**5. M3 — Macrina over-claim — FIXED.**
> "one woman among them led and taught so well that we called her the Teacher."

"our whole country honored her" is gone. Doc_02 §41's representativeness-nil constraint is now respected; the honor is carried by the title alone.

**6. M4 — tier-register markers — FIXED, all three, at Doc_09's own wording.**
- Forty: *"So the church tells of the Forty, who froze on the lake..."* — Doc_09 #11's required register is "so the church tells of her Forty." Match.
- Constantinople: *"One of our own told of preaching the Trinity in a hostile capital while crowds threw stones at him — his own telling of it, and we have no other's."* — Doc_09 #10's "told with the self-account named." Match.
- Sasima: *"his friend's own telling of the hurt is the one we still have, and no other"* — Doc_09 #4's "one side's telling, said as such." Match.

All five story-derived claims now carry the discipline consistently.

**7. M5 — native vocabulary anchor — FIXED.**
> "We confessed one being — one *ousia*, our own word for it, the fence around the faith rather than a scholar's puzzle."

Plain meaning first, label after — the document's own established form. "The fence around the faith" traces to Construction Notes §2 ("ousia/hypostasis spoken as the faith's fence"). This is exactly the fix the first review prescribed. Two small residuals at LOW-3 and LOW-5.

**8. M6 — Living Traditions list — PARTIALLY FIXED, and it introduced two new problems.**
The flat, itemized, recitable list of four communions survived essentially intact, and the mitigation clause — borrowed from Yausep's phrasing but wrapped around the same list — made two things worse than the text it replaced (see NEW-H1, NEW-M1 below).

## New findings

### HIGH

**NEW-H1 — "the Greek East that kept it whole" is a fidelity verdict on one living communion, delivered from a voice that has just said it cannot know.** A regression from the prior text ("the churches of the Greek East above all," a correspondence-intensity ranking traceable to World Profile §108). "Kept it whole" is a different claim — that one communion preserved the confession entire, with the plain implication that the other three named did not.

- Contradicts P9 directly: *"Nothing after its end is yours at all. You do not know what the churches and the empire later made of our words."*
- Breaches Construction Notes §6's handling rule ("leaves what the living churches have made of it to them") and Section 4's risk-1 bound (does not adjudicate).
- The template marks this section MANDATORY with an explicit participant-harm criterion (receivable "without feeling corrected or diminished"), and World Profile §108 flags this world as carrying the highest identity-stakes of any world in the project's current set.

### MEDIUM

**NEW-M1 — "in places and under names we never knew — the Greek East..., Armenia..., Rome..."** The em-dash made the list appositive to the names the voice says it never knew, then the list was composed of places and names the world knew perfectly well. Failed on either reading — an artifact of importing Yausep's clause in front of a list Yausep does not have. Same sentence as NEW-H1.

**NEW-M2 — the reserve passage stated a Contested motive as settled fact.** Doc_06 §17 and World Profile §92 both flag the reserve-holder's motive as *Contested*. The prompt ruled one reading out and asserted another as the narrating "we"'s own settled judgment, in a document otherwise careful with this exact class of material ("wounded by what one bishop judged necessary"; "his own telling of it, and we have no other's").

### LOW

**NEW-L1 — P16's feast sentence grew to 60 words with a 22-word nested aside**, the document's second-longest sentence, in spoken Section 3 territory. Correct content, wrong shape.

**NEW-L2 — measurable register regression on the newly written spoken material** (not the whole document, which still clears comfortably: FK 6.7 / FRE 77.5 / 17.0 avg words/sentence). The ~543 words of new/changed spoken text alone measured FK 11.9 / FRE 63.7 / 30.2 avg — above the band's ceiling, driven by four new sentences ≥40 words. Not a fail on the aggregate; drift worth watching.

**NEW-L3 — "a scholar's puzzle" was the only hit on the meta-vocabulary sweep.** Traces to Construction Notes §2 ("not as seminar-Greek") but converted a builder-facing register instruction into an in-voice self-characterization.

**NEW-L4 — image triplication introduced by Section 2A** (the frozen lake appears three times, the famine bread twice) — inherent to Section 2A's design and present in the sibling builds too; not a defect, noted only.

**NEW-L5 — *hypostasis* is still unanchored.** M5 is discharged as asked (one insertion at ousia), but the ousia/hypostasis *pair*'s distinction (what God is / who God is) — Voice Configuration §2's stated key testing question — is not rendered. Half the fence is built. Optional.

## Also checked, and clean

- **Placement and flow.** No paragraph order violation, no orphaned transition.
- **No contradiction introduced by the backstop.** Its "our record" usage matches the template's own and the document's pre-existing usage.
- **Fabrication.** Nothing new is unsourced. The Constantinople stone-throwing detail is pre-existing and is now properly marked as self-account. N2's unsourced "his garden" was dropped — the first review's only fabrication flag is closed.
- **Size.** 3,993 words / 27 paragraphs, between Yausep (3,299 / 36) and Marius (4,213 / 112), both of which carry both template sections. Growth is exactly the six mandated paragraphs plus ~300 words of local fixes — no scope creep.
- **Voice Configuration** was updated in the same commit with a recalibration note covering both the *ousia* anchor and the new reserve passage, closing deployment flag 1 from Round 1.

## Overall verdict at time of this review

**Not clean yet, one HIGH and two MEDIUMs, all confined to two sentences** (P27's Living Traditions closing; P12's reserve-motive attribution). Recommended: rewrite P27 to drop the fidelity verdict and resolve the list/"never knew" contradiction (drop the itemized list, per Yausep's own solution, rather than patch around it); a five-word attribution fix at P12 so the Contested motive is carried as the defending friend's own claim, not the "we"'s settled judgment. NEW-L1 and NEW-L3 flagged as cheap optional fixes in the same pass.

## Disposition note (build thread, 2026-08-31, after this review)

All three items this review asked for were applied directly, without a third review round, on the same convergence basis as this session's Source Registry (§10 of the build ledger) and Doc_07/Doc_09 (§11) precedents — each fix was precisely located, the review supplied the exact content and reasoning needed, and the fixes are narrow, mechanical, low-risk edits to two sentences already isolated by this review:

- P12: the reserve-holder's motive ("not doubt but care") is now explicitly attributed to his defending friend's own claim, not stated as the narrating "we"'s settled judgment.
- P27: rewritten to drop "kept it whole" (the fidelity verdict) and the itemized four-communion list entirely, per this review's own recommended solution (matching Yausep's actual pattern rather than importing its framing clause alone) — replaced with "more widely than almost anything else our life produced," which carries Construction Notes §6's "unusually broad correspondence" claim without ranking or itemizing any living communion.
- NEW-L1 (feast-sentence length) and NEW-L3 ("a scholar's puzzle") were also fixed, both one-line changes.

NEW-L2, NEW-L4, and NEW-L5 are left as-is: watch-only per this review's own characterization, none rising to a defect.
