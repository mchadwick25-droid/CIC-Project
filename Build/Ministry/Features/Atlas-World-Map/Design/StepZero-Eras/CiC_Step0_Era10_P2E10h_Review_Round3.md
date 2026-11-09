# Era 10, P2-E10h: adversarial review, Round 3

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 3 of 3 (targeted recheck: only what changed since Round 2, against the Round 2 findings)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json`, on branch `claude/era10-p2e10h` at 0bb2bddb1, against `cic-website/data/world-census.json` (release 24, 307 movements; unchanged since d9b373401). The reviser's response is "Revision after Review Round 2" at the end of `CiC_Step0_Era10_P2E10h_Trace.md`. Previous proposal: `d9b373401`.

**Method.**
- Structural diff of the current proposal against the d9b373401 copy (`e10h-rev2/jdiff.py`, output `e10h-rev3/diff.txt`).
- Structural diff of the current proposal against my own Round 2 tested fix copy (`e10h-rev2/proposal.r2fixed.json`). **No difference.**
- Applied the proposal with my own applier (`e10h-rev3/myapply.py`) to the repo census. Every old string matched once. `node tools/validate-census.mjs applied.json --atlas cft-website/index.html`: 322 movements, 578 edges, 10 eras, **0 errors, 2 warnings** (the same two era 1 shortName warnings, outside this slice).
- Sentence length (`e10h-rev3/len.py`): every sentence in the new rows and edit strings, and every new sentence in an applied, edited field. The only hits over 25 words are two source `work` citation strings (IX.15, 27 words; IX.46, 30 words), unchanged since Round 2 and exempt as citations. No prose sentence passes 25 words.
- Read each changed field in its applied context. No web research was needed: every fix rests on sources already verified in Round 2.
- No repo file was edited. No metered model call was made.

---

## Diff against d9b373401

Every change is one Round 2 gave, as given:

| Location | Round 2 finding | Status |
|---|---|---|
| registerEdits[43], IX.21 `longDescription` | S2-1 | As given |
| registerEdits[55], IX.44 `longDescription` | M2-1 | As given |
| registerEdits[14], IX.24 `relationsSummary` | M2-2 | As given |
| newRows IX.73 `why`, `longDescription`, `relationsSummary`, `legacy` | M2-3 | As given |
| registerEdits[49] and [51], IX.11 `teaser`, `longDescription` | M2-4 | As given |
| newRows IX.72 `teaser`, `voices[1]` | M2-5 | As given |
| registerEdits[17], IX.8 `relationsSummary` | M2-6 | As given |

Nothing else changed. The reviser's note lists the same seven edits and two rows.

## Round 2 findings: status

**S2-1 (IX.21).** Fixed. The applied text reads: "…'Action P'. For forty-three years the Ukrainian church was the largest banned church in the world. It had priests ordained in secret…". The forty-three years now attach to the Ukrainian church, and 1946 to 1989 is forty-three years, which the row's own Lviv and 1989 sentences date. No fact is added. The old 26-word sentence is gone.

**M2-1 (IX.44).** Fixed. "Its own internal arguments" again follows the sentence on the church documenting itself, so "Its" and "that same public record" point where they were written to point. The Titicaca sentences now close the field. Each is under 25 words. The 26-word census sentence is no longer touched by this slice.

**M2-2 (IX.24).** Fixed. "grow in self-reliance" matches the Covenant as quoted in *CT*, November 1974.

**M2-3 (IX.73).** Fixed in all four places. "Most of its church buildings came into Orthodox use" and "took over most of this church's buildings" match Mahieu 2004 (legally not received by the Orthodox Church; the majority used by it). The legacy now opens "Its suppression came two years after the Lviv synod … in 1946", which is correct for 1948, and its "Two years later, in April 1950" is correct for Prešov. The fact of 1989 stays in `why` and `longDescription`.

**M2-4 (IX.11).** Fixed. Both long sentences are split, and every resulting sentence is under 25 words. The longDescription keeps 1911, 1952, 1958 and 1977 and adds nothing.

The teaser sentence the brief asks about, "Its argument over the prosperity gospel is on the record in its own published critiques":
- *Supported.* It rests on the row's existing second source, "the published critiques from within the same Pentecostal family (Lausanne evaluations; African evangelical theologians' rebukes)", and on the same claim in `why`, `longDescription`, `floorNote` and the fourth voice. Release 24's teaser already made it ("carried on the record in the movement's own published critiques"). The new sentence narrows nothing and adds no new fact.
- *Free of commentary.* The map's self-description "rather than described from outside" is gone. What remains is a plain statement of where the argument is recorded. "Its" refers to "Pentecostalism's growing edge", the subject of the sentence before.
- See Observation below on one inherited framing. It is not a finding against this round.

**M2-5 (IX.72).** Fixed. The teaser and Paul VI voice now use "removed … from memory", the Joint Declaration's verb, matching `why` and `longDescription`. The teaser names Rome as a party to the act. "it" refers to the Ecumenical Patriarchate. No "lifted" or "ended" remains in the row.

**M2-6 (IX.8).** Fixed. Medellín (1968) and Puebla (1979) are named inside `relationsSummary`, so it no longer leans on the longDescription for "again" and "both meetings". Both dates are correct.

---

## SUBSTANTIAL findings

None.

## MINOR findings

None.

## Observation (not a finding; outside this round's scope)

IX.11's second source, `floorNote` and fourth voice treat the Lausanne movement's critiques as published "from within the same Pentecostal family". Lausanne is a broader evangelical network, not a Pentecostal body, though Pentecostals took part in it. This framing is in release 24 and was not changed by this round or the last. It is nothing a Round 3 targeted recheck may hold the slice on. If the coordinator wants it tidied, it belongs in a later IX.11 pass, logged in `Open_Gaps_Tracking.md` rather than left here.

---

## Verdict

**Approved to proceed.** S2-1 is fixed as given, and M2-1 to M2-6 are all taken exactly as Round 2 gave them. The current proposal is identical to the fix copy I tested in Round 2. Nothing else changed. No changed text introduces a wrong, unsupported or misleading claim. The applied census validates with 0 errors and the same 2 out-of-slice warnings. No prose sentence in the changed text passes 25 words.
