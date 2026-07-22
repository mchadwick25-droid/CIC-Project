# Launch prompt / update — System Hub: strip nonprofit-era material, repo-wide

Paste this into the System Hub thread (or hand it to a fresh thread if System Hub isn't
currently active) as a new, bounded piece of work. This is a cross-repo cleanup job, not a
feature build — closer in shape to the 2026-07-20 Filing System Audit than to a normal
feature-thread handoff.

---

## Why this exists

On 2026-07-21, in a separate Funding/Formation thread, Mark pivoted CiC's legal entity from a
planned 501(c)(3) nonprofit to a Colorado Public Benefit Corporation — **"Faithways Studio,
Inc.," d/b/a "Church in Conversation,"** owned 50/50 by Mark and Susan Chadwick. Full reasoning
lives in two decision logs; **read both before touching anything**:

- `Ministry/Funding/CiC_Org_Funding_Decision_Log.md` — why the nonprofit path was abandoned
  (couldn't make the academic-review-gated nonprofit funding model work financially).
- `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md` — the full PBC build: entity
  name split (Faithways Studio vs. the "Church in Conversation" trade name), three independent
  review rounds, the final governance/tax structure.

**The current, correct, filing-ready state of the entity** is these four documents, already
drafted and reviewed — treat them as the source of truth for what's accurate now:
- `Ministry/Organization/CiC_PBC_Articles_of_Incorporation_V0_4_FILING_READY.md`
- `Ministry/Organization/CiC_PBC_Bylaws_and_Organizational_Resolutions_V0_1.md`
- `Ministry/Organization/CiC_PBC_IP_Assignment_Agreement_V0_1_DRAFT.md`
- `Ministry/Organization/CiC_PBC_Shareholder_Buy-Sell_Agreement_V0_1_DRAFT.md`

The Gantt/task board/dashboard were already resynced to this pivot (2026-07-21 entry, this
same decision log). **What's still stale is everywhere else in the repo** — nonprofit-era
language, structure, and status claims left over from before the pivot, scattered across
branding, funding, marketplace, and public-facing website copy.

## Do this first — a live, public, donor-facing accuracy problem, not just tidiness

**`cic-website/support.html` is a real, live page making false claims right now, and Mark has
confirmed: fix it, and rework the giving/ask mechanics themselves — don't just patch the
wording.** Checked directly (2026-07-21):

> "Church in Conversation is incorporated as a Colorado nonprofit corporation. Federal 501(c)(3)
> tax-exempt determination from the IRS is a separate, later step, still in progress... a gift
> given now would likely become deductible after the fact, once that determination lands."

None of this is true anymore — there is no nonprofit incorporation, no 1023-EZ ever getting
filed, no IRS determination ever coming, and gifts will **never** retroactively become
tax-deductible under this structure. **Fix this page before doing anything else in this cleanup
pass**, on two levels:

1. **Factual correction:** rewrite the "Nonprofit Status" section to accurately describe the
   PBC/for-profit structure and state plainly that contributions are not, and will not become,
   tax-deductible under this entity — a PBC has no retroactive path to that at all, unlike the
   nonprofit's "later, once determination lands" story this page currently tells.
2. **Real rework of the ask itself**, not just the disclosure paragraph — since "gift"/"donate"
   language built around eventual tax-deductibility no longer fits a for-profit structure. **Use
   the monetization ladder and ask copy already drafted for exactly this transition** —
   `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` has the finalized ask language ("$10/month
   keeps the Table open for ten more seekers..." / "Contributions go toward the real cost of
   running and growing this...") built specifically for a paid-support model, not a charitable
   one. Bring the page's actual structure in line with that ladder (tip jar → subscription →
   gating → institutional licenses) rather than inventing new copy from scratch. This is public
   copy, so it also falls under `Ministry/Communication/CiC_Messaging_Branding_Kit_V0_1_DRAFT.md`'s
   governance — check tone/protected-language rules before publishing, but don't wait on a
   separate go-ahead from Mark for this specific rework; he's already confirmed it directly.
   **Payment processor decided, 2026-07-21: Stripe, built directly into the site** (not a
   link-out tool like Ko-fi/Patreon, and not PayPal) — chosen specifically so the payment
   experience stays fully on-brand and on-page rather than redirecting to a third party, and
   because Stripe's subscription/billing tooling fits the "gating" tier and Stripe's
   invoicing/ACH options fit the "institutional licenses" tier better than the alternatives. Full
   reasoning: `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md`, 2026-07-21. The
   corporate bank account is at Relay (relayfi.com); Stripe payouts land there via standard ACH,
   no special integration needed beyond entering the account/routing number (bank name shows as
   "Thread Bank," Relay's partner bank).

## The rest of the repo — do a full system review, not just a keyword sweep

Mark's direction: don't scope this to the one grep pattern below — **run this as a genuine full
system review**, the same rigor as the 2026-07-20 Filing System Audit or the L1-L5 systematic
audit, so it catches nonprofit-era drift the keyword list itself might miss (structural
assumptions, board-of-directors language, funder-facing framing, anything that assumes a
501(c)(3) reader) — not just the literal terms below.

A repo-wide search (2026-07-21) for nonprofit-specific terms — `501(c)(3)`, `1023-EZ`, `CCSA`,
`nonprofit`/`non-profit`, `charitable solicitation`, `D&O insurance`, `tax-exempt`, `IRS
determination` — turned up **37 files** referencing this material, spanning Communication
(branding/messaging), Funding, Marketplace, Operations (audits, markup queue), Organization,
and the live website. Treat this as a starting map only — the full review should go wider:

```
grep -rl "501(c)(3)\|1023-EZ\|1023EZ\|CCSA\|nonprofit\|non-profit\|charitable solicitation\|D&O insurance\|D and O insurance\|tax-exempt\|IRS determination" --include="*.md" --include="*.html" --include="*.docx" .
```

**Sort every hit into one of three buckets — do not treat them all the same way:**

1. **Decision logs and dated historical records — do NOT rewrite.** Files like
   `CiC_Org_Funding_Decision_Log.md`, `CiC_Nonprofit_Formation_Decision_Log.md`,
   `CiC_System_Hub_Decision_Log.md`, `CiC_Branding_Messaging_Analysis_Decision_Log.md` are
   append-only, dated records of what was true and decided *at the time*. The nonprofit-era
   entries in them are correct history, not errors. Leave them exactly as written; if a
   specific claim needs a correction pointer, add a dated addendum (this project's standing
   convention — see how the 2026-07-21 PBC-pivot entries themselves were added), never edit or
   delete the original entry.
2. **Standalone, entirely-nonprofit-specific documents — mark superseded, don't delete.**
   Files like `CiC_Articles_of_Incorporation_V0_2_FILING_READY.md` and
   `CiC_Colorado_State_Filing_Package_V0_1.md` in `Ministry/Organization/` are wholesale
   nonprofit-path artifacts with no PBC content mixed in. Add a clear header banner —
   `**SUPERSEDED 2026-07-21 — entity pivoted to Faithways Studio, Inc. (PBC). See
   CiC_PBC_Articles_of_Incorporation_V0_4_FILING_READY.md for the current entity.**` — and leave
   the rest of the file in place as historical reference, same pattern already used for the
   V0.2 nonprofit Articles when the PBC draft first superseded it.
3. **Live/current documents that mix valid material with stale nonprofit references — surgical
   fix, not a rewrite.** This is most of the branding/messaging/marketplace/funding files and
   any public-facing copy — they likely have a paragraph or a status line describing CiC as
   "pursuing 501(c)(3) status" or similar, sitting inside content that's otherwise current and
   correct. Find and fix just the stale claim; don't touch what's actually still accurate.
   **`cic-website/README.md` and any other still-live site file** in this bucket get the same
   public-accuracy scrutiny as `support.html` above — check for anything donor- or
   status-facing, not just internal planning docs.

**Explicitly out of scope for this pass:** rewording brand voice, redesigning messaging, or
opening any new content decisions — this is strictly "make factual entity/tax-status claims
accurate," not a broader copy edit. If a file needs a real content decision beyond a factual
correction (e.g., how to now frame the "ask" on the support page now that gifts aren't
donations), flag it to Mark rather than deciding it yourself.

## New, related item: churchinconversation.com is now the primary domain, not .org

Mark's direct decision (2026-07-21): **churchinconversation.com is now the primary domain for
Church in Conversation, replacing .org.** Reasoning: a .org suffix reads nonprofit-coded, which
no longer fits now that Church in Conversation is a DBA of a for-profit PBC — same logic as the
rest of this cleanup. **Keep .org registered (don't let it lapse)** and set up a redirect from
.org → .com once the live site actually moves, so old links still resolve. As part of this
cleanup pass, check `cic-website/` for any hardcoded references to the .org domain (canonical
URLs, meta tags, internal links, sitemap) and update them to .com — fold this into the same pass
rather than treating it as a separate cleanup later. Business email for Church in Conversation
(3 mailboxes, Zoho free tier) is being set up on @churchinconversation.com to match.

## Put this on the actual task list, not just in this prompt

Before starting the file-by-file work, add these as real, trackable items across all three
tracking artifacts (`CiC_Acceleration_Gantt_2026.gan`, `CiC_Task_Board_2026.md`,
`CiC_Dashboard.html`) — same discipline this hub already applies to every other dispatched
thread's task set:
- The `support.html` fix + giving-page rework (urgent, do first).
- The full system review itself, as its own tracked item.
- Whatever additional stale-file fixes the review turns up, added as they're found — don't wait
  until the whole review is finished to start logging individual fixes.

## The entity decision is now final — no longer pending

The nonprofit→PBC pivot has been through a genuine deep-research stress-test (three
independent, adversarial research passes — one re-testing whether nonprofit was really
infeasible, one testing PBC revenue realism, one checking hybrid alternatives) and a direct
confirmation from Mark. Full account: `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md`,
2026-07-21 (final) entry. **The research surfaced a real fork — the whole case for PBC over
nonprofit came down to whether Mark actually wants to preserve the option of a personal sale
someday, since two close comparables (BibleProject, Desiring God) prove the donor-funded
nonprofit model genuinely works at CiC's scale.** Asked directly, Mark confirmed: *"i want to
keep the option to sell at some point."* PBC stands, final, not provisional. Proceed with this
cleanup pass on that basis — no need to hedge language as "current plan, subject to change."

## When done

Produce a dated audit entry in `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
listing every file touched and which bucket it fell into — same pattern as the 2026-07-20
Filing System Audit entry. Report back to Mark directly on the `support.html` fix specifically,
since that's the one with real external-facing consequence, before considering this closed.
