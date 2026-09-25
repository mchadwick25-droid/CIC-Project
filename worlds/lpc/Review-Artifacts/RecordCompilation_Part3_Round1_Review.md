# Record Compilation, Part 3 (Story/Figure/Quote Records) — Round 1 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`) — `worlds/lpc/scripts/wb_lpc_s24.py` and `records/lpc/{story,figure,quote}/`

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-24 · **Round:** 1 · **Deliverable under review:** 18 uncommitted records (7 `story`, 7 `figure`, 4 `quote`) and the generator script that produced them, drafted cold by a different agent from `Doc_09_Story_Inventory.md`, `lpc_Story_Index.md`, all 7 `Story-Chunks/` files, and `lpc_Representative_Permanent_Prompt_Datus.txt`.

A prior pass this session already independently confirmed: the 18-file count (7+7+4); `engine.m1.gates.run_all` returns clean except the expected, pre-existing `gate-canon-coverage` (28 findings, all "blank cell," pre-existing "no canon-cell tagging work has happened for this world yet"); and 2 of the 4 quote records verified byte-for-byte (`clamour-and-tears`, `shepherd-wounded-in-the-flock`), including the disclosed OCR artifact ("ancf" for "and") correctly reproduced rather than silently fixed. Those points are re-confirmed below by an independent re-run rather than re-litigated, and this review's own new work is the other 2 quotes, the figure/story/schema/cross-reference checks, and the 3 declined quote-candidates.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH · 1 MEDIUM · 2 LOW · 1 COSMETIC.**

This compilation's narrative, biographical, and tier-classification content holds up very well — I found no invented participant, event, biographical detail, or outcome anywhere in the seven stories or seven figures, and every quotation's own **text** is verbatim against the vendored corpus. Both HIGH findings are about the **citation apparatus** (where a quotation is said to live, and whether a claimed search actually failed), not about fabricated content — but both are exactly the class of defect this world's own build has flagged, repeatedly, as its "signature defect": a specific, checkable claim that turns out false. Neither is a "could be stronger" note; both are wrong on their own terms and independently reproducible in under a minute.

---

# Method

I read `CLAUDE.md` in full first. I then read `Doc_09_Story_Inventory.md` and `lpc_Story_Index.md` in full, all 7 `Story-Chunks/` files, `wb_lpc_s24.py`'s own docstring and body in full, `lpc_Representative_Permanent_Prompt_Datus.txt` in full, the relevant `story`/`figure`/`quote` sections of `engine/m1/schemas.py`, and `RecordCompilation_Part2_Round1_Review.md` for reporting format. I read all 18 new record files directly from disk. I independently re-ran `engine.m1.gates.run_all` against the live 245-record `lpc` load and the full fleet (reproducing 0/28 exactly). I independently re-verified, byte-for-byte against the raw vendored files, the two quotes the prior pass had not checked (`ancient-venom-against-my-episcopate`, `bishop-of-bishops`, plus its three corroborating Augustine loci), and then independently re-checked the `sources[].locus` line ranges on all seven story records (not just the two quotes I was asked to focus on), which is how H1 surfaced. I searched `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` directly for the seventh named-and-declined Permanent Prompt image, which is how H2 surfaced. I wrote a small script to cross-check every `sources[]`/`relations[]` target across all 18 new records against all 245 `lpc` record ids (zero misses).

---

# HIGH Findings

## H1 — Two story records give a `sources[].locus` line range that points to the wrong letter entirely, while claiming `verification_state: verified-direct`

**Where:** `lpc.story.numidicus` (`sources[0].locus`: "Ep. XXXIV; ... lines 29200-29260") and `lpc.story.hundred-thousand-sesterces` (`sources[0].locus`: "Ep. LIX SS3 ... lines 33600-33660"), both in `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`.

**What's wrong, shown:**
- Ep. XXXIV (the Numidicus letter) actually begins at line 32085, and the quoted material ("half consumed, overwhelmed with stones," "was found half dead, was drawn out and revived") sits at lines 32095–32120. Lines 29200–29260, as actually printed in the file, are the middle of **Epistle VI** — a different letter, about concubinage and a colleague's reputation, containing no reference to Numidicus, his wife, or his daughter at all.
- Ep. LIX §3 (the ransom letter) actually begins at line 36007 ("Cyprian to Januarius, Maximus, Proculus, Victor, Modianus, Nemesianus, Nampulus, and Honoratus" — the eight named recipients check out exactly), and "one hundred thousand sesterces" sits at line 36082. Lines 33600–33660 are the middle of **Epistle LI**, about Cornelius's own episcopate and the readmission of Trophimus — again, a different letter with no ransom, no sesterces, no Numidian bishops.
- Both records' own `confidence` blocks assert `citation_specificity: A` (the highest band) and `verification_state: verified-direct`, and both trailing body notes state the quoted phrase was "independently re-located this session" — yet the specific line range actually written into the record is roughly 2,000–2,900 lines away from where the passage lives, in each case pointing at unrelated content.
- Neither error is inherited: I checked both source Story-Chunks (`lpcstory003_numidicus.md`, `lpcstory004_hundred-thousand-sesterces.md`) and neither cites any line number at all — the false specificity was introduced fresh by this compilation pass, not carried from an already-reviewed input.
- By contrast, I independently re-checked the other five stories' locus ranges the same way and found four correct (election, plague, death-of-cyprian, psalms-on-the-wall) and one imprecise but in the right neighborhood (celerinus-writes-to-lucian, logged as L1 below).

**Why HIGH:** the quoted *text* in both records is accurate (independently confirmed at the correct, different lines above), so this is not invented content. But `CLAUDE.md` treats a false, specific, checkable source claim as the recurring defect this project cannot tolerate, and a `verified-direct` claim paired with a wrong locus is precisely that — it actively misdirects anyone trying to re-check the record (it very nearly misdirected this review, which first read the stated line ranges and found unrelated content before searching the file directly for the quoted phrases instead).

**Fix is narrow:** correct the two `locus` line ranges (32095–32120 and 36007–36085 respectively, or a wider safe margin around them); no other field needs to change.

## H2 — The "searched and not located" declination for the 7th named-but-undeployed Permanent Prompt image is false; the quote exists verbatim in the exact file named

**Where:** `wb_lpc_s24.py`'s own "QUOTE SET, BOUNDED" section, item 7 (the task specifically asked this be checked).

**What's wrong, shown:** The script states that the image "a preacher naming, to the very people gathered in front of him, that their own waiting is itself a kind of prayer for him" was "searched this session against `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` ... and not located," and is "flagged as unresolved rather than silently dropped." I searched that exact file for "prayer for me" and found, at line 9398, Sermon I (Benedictine LI), Augustine preaching: *"but this your longing expectation is a prayer for me."* This is the described image almost word for word — a preacher, addressing his own gathered congregation, naming their own waiting as a prayer offered on his behalf — sitting in the very file the script says was searched, findable with a single obvious keyword.

**Why HIGH:** this is the same "false absence claim refuted by the very source named" pattern that produced 8 of the 11 HIGH findings across Doc_09's own eight review rounds (documented in that document's own Disposition). It is not a fabricated quote and nothing downstream currently relies on the false claim, but the discipline this project asks for — "if the evidence does not support a story, the story does not exist," and equally, if the evidence *does* support one, it does not get to not exist by an unchecked claim that it was looked for — is violated here. The other two declined images (items 4 and 6, the certificate/wide-door and baptism-outside-the-church contrasts) are genuinely synthesized comparisons with no single quotable sentence behind them, and I found no quotable single-sentence candidate for either on inspection of the named term records — those two declinations are honest. Item 7 is not.

**Fix:** either build `lpc.quote.longing-expectation-is-a-prayer-for-me` (or similarly named) as a fifth quote record from this located line, or, at minimum, correct the script's own accounting so a future reader is not told a search failed when it would have succeeded.

---

# MEDIUM Finding

## M1 — No gate checks a `locus` line range against the vendored file, so H1's class of defect is invisible to automated review

`gate_referential`, `gate_quote_verbatim`, and the rest of the 22-gate battery all check that a cited *source id* resolves and that quoted *text* matches the source's own words verbatim — none of them opens the vendored file at the claimed line number and confirms the passage is actually there. That is a real gap in defense-in-depth (H1 sailed through 0/22 relevant gates), not a defect in this pass specifically, but it is worth naming here since it is the reason two false, specific citations reached committed-file review only through a human re-check rather than a mechanical one.

---

# LOW Findings

## L1 — `celerinus-writes-to-lucian`'s locus range starts about 70 lines late

`sources[0].locus` gives "lines 30640-30720"; Ep. XX (Celerinus to Lucian) actually opens at line 30529, and the opening quoted phrase ("placed in the midst of a great tribulation") sits at line 30570. The independently re-verified detail cited in the quote-set docstring ("put to death by hunger and thirst," line 30706) is exactly right, and the stated range still overlaps both letters correctly — this is an imprecision, not a wrong-letter error like H1.

## L2 — `sources[].locus` citation style is inconsistent about whether a line range is given at all

Some story records give a specific line range (correctly, per above, in 4/7 cases), others cite only a section/chapter with no line number (e.g. figure records' "the whole Life and Passion"). Not a defect — the more specific claims are simply held to a higher, and in two cases unmet, bar — but a future pass should decide whether every `citation_specificity: A` record is expected to carry a checkable line locus, since right now that expectation is implicit rather than stated.

---

# COSMETIC

`lpc.story.hundred-thousand-sesterces`'s trailing body note says "'Hundred thousand sesterces' independently re-located this session," which is true of the *phrase*, but the record's own `sources[].locus` field (the thing actually checked here) was not correctly re-derived from that same relocation. A future pass tightening this discipline should have the trailing note and the `locus` field derive from the same located line, not be authored separately.

---

# What I checked and found solid

- **7 story records ↔ 7 Story-Chunks, exact 1:1 by slug**, tiers matching `Doc_09_Story_Inventory.md` §3 exactly (six Tier 1, one Tier 3 — `lpc.story.the-death-of-cyprian`); the Tier 3 escalation (Doc_09 §8 item 7 / `Open_Gaps_Tracking.md` OG-7) is independently confirmed still open, not stale.
- **7 figure records**, each grounded in Doc_01/Doc_09/Story-Chunk material with no invented biography (e.g. `lpc.figure.augustine`'s Megalius/coadjutor detail traces directly to `Doc_01_World_Identification_Boundaries_Orientation.md` §2, not outside knowledge). The declared exclusions (Numeria/Candida, Numidicus's unnamed wife and daughter, the eight Numidian bishops) match `Doc_09` §7 items 3–4 accurately — I re-read those items directly and the script's reasoning tracks them, rather than being a convenient paraphrase.
- **All 4 quote records verified byte-for-byte** against their cited vendored files this session (2 by the prior pass, 2 by me): `ancient-venom-against-my-episcopate` at line 32372 and `bishop-of-bishops` at line 56872, both exact, including `bishop-of-bishops`'s three independently-checked Augustine corroboration loci (lines 11292, 11626, 12207 of `npnf104_augustine-anti-manichaean-anti-donatist.xml`), all exact.
- **The Representative Permanent Prompt's own paragraph** (line 37, "what our own life actually gave us") does name all seven images the script accounts for, in the order claimed; the 4-built/3-declined split is correctly bounded except for H2 above.
- **Cross-references, checked programmatically over all 18 new records against all 245 `lpc` record ids:** every `sources[].source_id` and `relations[].target` resolves; zero misses.
- **Schema compliance:** `retrieval.prefer_instead`/envelope-level `claim_guards` is confirmed the current live schema (not the drafting agent's own unchecked assumption) — `engine/m1/schemas.py`'s own comment and `gate_retrieval_negatives_structured`'s own docstring both cite the same 2026-09-21 ruling (R11) the script names. `figure.dates.display` (rather than `born`/`died`) matches the live convention already in use across `records/don/figure/*.md`, not a deviation.
- **Register claim:** spot-checked against `records/don/story/don.story.passio-donati-sermon.md`, which does open "Every year... we gather to remember..." — confirming the current live first-person register the script claims to match.
- **Gate battery, independently re-run this session:** 245 lpc records load; 0/22 gates fire except `canon-coverage` (28 findings, all "blank cell," pre-existing and unrelated to this pass).

---

# Recommended disposition

**Substantial revision required, but narrowly scoped and answerable in one fix pass** — this is not the multi-round pattern this project's own review-cycle cap exists to catch. Fix H1 (two `locus` line ranges) and H2 (either build the fifth quote record or correct the script's own claim about the search result) together in a single revision; M1, L1, L2, and the cosmetic note can be folded into the same pass. Nothing here calls the narrative, tier, or biographical content of this compilation into question, and nothing found requires touching `records/lpc/source/` or `records/lpc/term/`.
