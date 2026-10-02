**Simulated review — informational only, not an Article 31 substitute.**

# Doc_06 (Full Lexicon Development) — Round 1 Independent Adversarial Review
## Alexandria (Catechetical-School) Formation World

**Reviewer stance:** independent adversarial. Did not author the material under review. Scope: `Doc_06_Full_Lexicon_Development.md`; the 10 deployment chunk files in `Lexicon-Chunks/`; `Lexicon_Deployment_Index.xlsx`. Cross-checked against Doc_01, Doc_03, Doc_04, the Deployment Lexicon Chunk Template, and (for facts) general patristic scholarship.

---

## VERDICT: **SUBSTANTIAL REVISION REQUIRED**

Six substantial findings. The lexicon *content* is strong — the from-inside register is well sustained in 9 of 10 chunks, all six CT contests are specified, and no Theon/Representative content leaked. The failures are concentrated in (a) internal number/tier drift between Doc_06 §2 and the master index, (b) a reciprocity check that reports links as mutual when the chunk files are not, (c) one analytical-distance marker leaked into a World Meaning, (d) one citation mislocation, and (e) a documented index sheet that does not exist. None is fatal to the build; all are correctable in a revision pass.

---

## SUBSTANTIAL FINDINGS

### [SUBSTANTIAL] S1 — Doc_06 §2 CT numbers contradict the master index (the declared numbering authority), and 046 is double-assigned inside Doc_06
**Location:** Doc_06 §2 CT table (`alexlex` column) vs `Lexicon_Deployment_Index.xlsx!Lexicon` and §1.
Doc_06 §4/§5 declare the master index "the numbering authority." Doc_06 §2's parenthetical numbers do not match it:

| Term | Doc_06 §2 says | Index says |
|---|---|---|
| Apokatastasis | `046` | `alexlex051` |
| Logikos / Rational Nature | `047` | `alexlex090` |
| Fall / Descent | `048` | `alexlex074` |
| Homoousios | `049` | `alexlex081` |
| Catechetical School / Didaskaleion | `050` | `alexlex059` |

The index numbers Tier-2 alphabetically from 047 (Agape Feast=047 … Apokatastasis=051 …), which is internally coherent; §2's 046–050 block is stale/invented. Worse: **§1 assigns `alexlex046` to Worship/Latreia while §2 assigns `046` to Apokatastasis** — a direct internal contradiction within Doc_06.
**Fix:** Replace §2's parenthetical numbers with the index values (051, 090, 074, 081, 059). Confirm 046 = Worship/Latreia only.

### [SUBSTANTIAL] S2 — Didaskaleion mis-tiered in Doc_06 §2 (Tier-3), contradicting both Doc_03 and the index (Tier-2); no Tier-3 terms exist
**Location:** Doc_06 §2 ("Catechetical School / Didaskaleion … (Tier-3, `050`)") vs Doc_03 line 203 (`| Catechetical School / Didaskaleion | 2 | AS TC CT |`) and `Index!By Tier` / row `alexlex059` (Tier 2).
Doc_03 and the index agree it is **Tier-2**; Doc_06 §2 calls it Tier-3. Downstream, §3 and §5 refer to "Tier-2/Tier-3 chunks" and "Tier-2/3," but the index contains **zero Tier-3 terms** (`By Tier`: Tier 1 = 46, Tier 2 = 84, total 130). There is no Tier-3 referent anywhere in the build.
**Fix:** Change §2 to "(Tier-2, `alexlex059`)"; drop or reconcile the "Tier-2/3" phrasing in §3/§5 (the roster is Tier-1 and Tier-2 only).

### [SUBSTANTIAL] S3 — Related-Terms reciprocity is falsely reported; several built-chunk links are one-directional
**Location:** `Index!Related-Terms Reciprocity` sheet and Doc_06 §4; chunk front-matter `Related-Terms` lines.
The reciprocity sheet marks built-chunk pairs "Reciprocal ✓" that are **not** mutual in the actual files:
- **Theosis → Knowledge/Gnosis**, but the Gnosis chunk's Related-Terms (`Logos, Divine Pedagogy, Illumination, Wisdom, Participation`) omits Theosis. Sheet claims Theosis "Reciprocal ✓ for built (Logos, Participation, Gnosis)."
- **Participation → Illumination**, but the Illumination chunk (`Logos, Divine Pedagogy, Catechesis, Knowledge/Gnosis, Wisdom, Baptism`) omits Participation. Sheet claims reciprocal.
- **Nous → Illumination** and **Nous → Gnosis**, but neither Illumination nor Gnosis lists Nous. Sheet claims Nous "Reciprocal ✓ for built (Illumination, Gnosis)" — both false.
- **Scripture → Divine Pedagogy / Illumination / Nous**, but none of those three list Scripture back (only Logos does). Sheet claims all four reciprocal.
- **Transformation → Participation / Theosis / Divine Pedagogy**, but none of those list Transformation back.

Doc_06 §4's illustrative claim — "Logos↔Divine Pedagogy↔Illumination↔Gnosis↔Participation↔Theosis all list one another" — is false: Divine Pedagogy, Illumination, and Gnosis each omit Participation and Theosis. Only the spokes to **Logos** are genuinely mutual.
**Fix:** Either add the missing back-links to the chunk front-matter (make the built cluster actually mutual) or rewrite the reciprocity sheet to report the true non-reciprocal pairs. Correct the §4 example. The reciprocity check is a stated QC deliverable; as written it produces false passes.

### [SUBSTANTIAL] S4 — Analytical-distance marker leaked into World Meaning (Nous chunk)
**Location:** `alexlex011_nous.md` → `## World Meaning`, ¶2: "Whether Origen's own account is the same thing that was condemned is **exactly the live scholarly contest** (see CT Contest Type)"; also "propositions later condemned."
The template's Final-Assembly step 3 forbids analytical-distance markers in World Meaning ("scholars believe," "the evidence suggests," etc.). "the live scholarly contest" is exactly that register, and the contest already lives — correctly and in full — in this chunk's `## CT Contest Type` section, which is where it belongs. The surrounding from-inside framing ("the world holds … as inheritance under real question, not as settled teaching") is good; the meta/scholarly sentence is the leak.
**Fix:** Recast ¶2 purely from-inside (e.g., "This further layer the world holds as contested inheritance, under real question rather than as settled teaching — see CT Contest Type"), removing "live scholarly contest" from World Meaning.

### [SUBSTANTIAL] S5 — Citation mislocation of the Athanasian formula (Participation chunk)
**Location:** `alexlex007_participation.md` → `## Key Sources`: "Athanasius, *On the Incarnation* 1–10 … ('God became human that humanity might become god')."
The deification formula is *De Incarnatione* **54** (54.3), not chapters 1–10 (which cover creation, fall, and the divine dilemma). The Theosis chunk cites it correctly at "ch. 54," so the two built chunks are also internally inconsistent on the same quotation.
**Fix:** Attribute the formula to *On the Incarnation* 54; if 1–10 is retained, cite it separately for the participatory grounding, not for the quoted formula.

### [SUBSTANTIAL] S6 — Documented "Cross-Build" index sheet does not exist
**Location:** Doc_06 §4: "Additional sheets: **By Tier**, **By Tag**, **CT Contest-Type Check** …, **Cross-Build**, and a **Related-Terms Reciprocity** note."
Actual workbook sheets: `Lexicon, By Tier, By Tag, CT Contest-Type Check, Related-Terms Reciprocity, README`. There is **no Cross-Build sheet**. Cross-build data exists only as a `Cross-Build` column on the Lexicon sheet and a "CB (cross-build)" row on `By Tag` (12 terms).
**Fix:** Add the Cross-Build sheet or delete it from the §4 sheet list.

---

## COSMETIC FINDINGS

### [COSMETIC] C1 — Template version-label mismatch
`Build/reference/L4-Templates/Deployment_Lexicon_Chunk_Template.md` header reads "Version 1.0" though its own Version History includes v1.1 and Doc_06 cites "V1.1." Header should read V1.1. (Template file, not a chunk.)

### [COSMETIC] C2 — Theosis World Meaning provenance aside
`alexlex008_theosis.md` World Meaning ¶1: "It was not Athanasius's coinage — Clement already speaks of the *gnostikos* 'becoming god,' and Origen of the soul's ascent." Not on the forbidden-marker list, but the provenance/authorship aside verges on analytical distance; consider recasting as the tradition's own memory rather than a claim about coinage.

### [COSMETIC] C3 — "Layer One / Layer Two" terminology collision
`alexlex011_nous.md` uses "Layer One / Layer Two" for Origen's nous-cosmology strata. This is **not** a Theon leak (it does not denote deployment layers), but it collides with the deployment "Layer One" vocabulary; a one-clause gloss ("layers of Origen's account of the nous") would prevent misreading.

### [COSMETIC] C4 — §0 overstates chunk sections
Doc_06 §0 item 4 lists "Reported-Experience Status" among sections the chunks carry; none of the 10 chunks include that (template-optional) section. §3's "Each carries:" list is accurate; §0 is loosely worded.

### [COSMETIC] C5 — John Prologue verse range
`alexlex014_scripture.md` cites "John 1:1–14" while `alexlex001_logos.md` cites "John 1:1–18." The Prologue runs 1:1–18; minor internal inconsistency.

---

## Required explicit statements

- **Are all 10 chunks template-compliant?** **No — 9 of 10.** All 10 carry the required sections (retrieval front-matter; the verbatim `## Quick Meaning` heading, non-empty and non-template; from-inside `## World Meaning`; Ecological Function; a two-line Modern-vs-World Distortion Risk; Key Sources with Author-Gravity notes where a source dominates; Related-Terms), and the Nous chunk's `## CT Contest Type` is completed. The single non-compliance is **S4**: an analytical-distance marker ("the live scholarly contest") leaked into the Nous World Meaning.
- **Are all 6 CT contests specified?** **Yes.** Doc_06 §2 and `Index!CT Contest-Type Check` both specify all six — Apokatastasis, Nous, Logikos/Rational Nature, Fall/Descent, Homoousios, Catechetical School/Didaskaleion — with 0 gaps. **Restoration is correctly resolved NON-CT** (separable from Origen's condemned *apokatastasis*; Athanasius attests restoration without universalism — a sound, mainstream distinction) and is absent from the CT set (index CT count = 6; `By Tag!CT` lists exactly those six). The Didaskaleion contest is correctly mapped (van den Broek 1995 / van den Hoek 1997 deny a formal pre-Origen institution; Scholten 1995 affirms an institution but as a theological, not catechumen, school) and is consistent with Doc_01 §1.2 and Doc_03.
- **Did any Theon/Representative content leak?** **No.** No "Theon," "the ache," "deployment status," "always-present," or "inhabits Layer One" language appears in any of the 10 chunks. (The Nous "Layer One/Two" denotes Origen's nous-cosmology, not deployment layers — C3.)
- **Does the index match Doc_06 and the chunk files?** **No — core counts match, but there are four drifts.** Matching: 130 terms; 46 Tier-1; 6 CT with Restoration excluded; 10 `Chunk-File-Built = Yes` flags on exactly the 10 built terms (001, 002, 004, 005, 007, 008, 011, 014, 021, 036); the full 001–046 Tier-1 roster numbers agree with Doc_06 §1. Drifting: S1 (§2 CT numbers vs index), S2 (Didaskaleion tier), S3 (false reciprocity reporting), S6 (missing Cross-Build sheet).

---

## Summary count

- **Substantial:** 6 (S1 numbering drift/double-assignment; S2 Didaskaleion tier; S3 false reciprocity; S4 analytical marker in Nous World Meaning; S5 Athanasius citation mislocation; S6 missing index sheet)
- **Cosmetic:** 5 (C1–C5)
- **Total:** 11 findings.

*End Doc_06 Round 1 review (simulated — informational only, not an Article 31 substitute).*
