# CiC Governance Rationale Log

The "why" behind rules stated plainly in `CLAUDE.md`. CLAUDE.md keeps the
rule itself; this file keeps the worked example or incident that justifies
it, so the rule file stays lean without losing the reasoning trail. Each
entry names the CLAUDE.md rule it backs.

## Kaner model — the Website V2 worked example

Backs: "How we work — Sam Kaner's model," CLAUDE.md.

This isn't a new process being imported — it's Mark's own established
practice. The Website V2 workstream (`Build/Ministry/Features/Website-V2/`,
opened 2026-09-01) names it directly in its own charter:
*"divergent/struggle/convergent process in a sandbox."* Its real shape is
the worked template for any comparable design or strategy workstream:

- **D1 (divergent)** drafted six full, independent homepage directions in
  parallel — not one direction refined six times. Closed on the finding
  that "no two converge."
- **D2 (groan zone)** reviewed and defended each direction independently.
  The goal wasn't crowning a survivor: every direction died at the
  whole-site level, and every direction left real salvage. Convergence
  doesn't have to mean picking one whole option intact — Mark's own call
  here was "Option A: hybridize," combining the salvaged pieces of multiple
  directions into a new synthesis, not selecting one as-is.
- **D3** built the converged hybrid out, then had it independently checked
  against the charter, the constitution, and the struggle record —
  explicitly *"not a ruling"*: the check reports back, only Mark's own word
  freezes it. Here that was a named, itemized verdict ("ready to freeze
  with eleven required fixes"), fixes applied and spot-checked, then Mark's
  direct ruling: *"Freeze it."*
- After freeze, changes are a **change order, not a quiet edit** — named
  and reasoned, the same discipline "no fix on a fix" already asks for
  elsewhere in CLAUDE.md. D4 (the real build) proceeded under that rule,
  incrementally, exactly as CLAUDE.md's "auto mode" describes.

## Review-cap rule — why three rounds, not open-ended

Backs: "Scaling the build" → "Review cycles are capped, not open-ended,"
CLAUDE.md.

This is not theoretical: an uncapped "repeat until it passes" loop ran two
world builds overnight and burned most of a week's usage credits
(2026-09-16).

## Source fidelity — why re-verification is mandatory, not a formality

Backs: "Source fidelity — never invent" → "Every quote must be
re-verified verbatim...," CLAUDE.md.

Misattributed and mis-transcribed quotes have been a real, recurring
defect here — a record's own "quotes verified" flag has been wrong before,
which is why the rule treats it as a claim to re-check rather than a fact
to trust.

## Paid-bulk-run gate — why a sample comes first, and why settings are never inherited

Backs: "Usage/credit discipline" → "Paid bulk runs are gated," CLAUDE.md.

On 2026-09-29 a full re-narration of 282 Church Family Tree movements
(268,144 characters of paid ElevenLabs text-to-speech) ran with the wrong
voice. The script read the voice id from an environment variable, the
new id was never passed, and the run used the old voice. The run's own log
said "Daniel voice" only because that text was hard-coded. The run was
called verified on evidence that showed the deployed files matched the
local files, which said nothing about which voice made them. Mark found it
by listening to the live result, after the money was spent. An earlier
narration run had also spent before checking that the audio matched the
text the site displays. Both were bulk spends made before a cheap human
check, and both were declared done on evidence that did not test the thing
paid for. The rule puts the sample and Mark's ear before the spend, makes
paid settings explicit and printed, and requires the check to test what was
paid for.
