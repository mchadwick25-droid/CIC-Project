# System Hub update — Faithways Studio, Inc. is now real, not just drafted; full alignment check needed

Paste this into the System Hub thread. This comes from the separate Funding/Formation thread,
where a huge amount of ground moved today — the entity went from "drafts exist" to **actually
incorporated and operating**. System Hub's standing job (keeping the Gantt/task board/dashboard
current, and more broadly keeping the whole repo's files aligned with reality) has real work to
do here, on top of the cleanup thread already dispatched earlier today.

---

## The headline fact: Faithways Studio, Inc. is real

**Entity ID 20261874960**, filed and accepted by the Colorado Secretary of State on **July 21,
2026**. This isn't a draft anymore — it's an operating company with its own EIN, signed governing
documents, a bank application in progress, and business email live on two domains. Any file
anywhere in the repo that still talks about entity formation as future/planned/draft is now
stale.

## Everything that happened today, in order

1. **Three independent, adversarial research passes** stress-tested the nonprofit-vs-PBC decision
   itself (not just the paperwork) — one re-testing whether nonprofit was really infeasible (it
   found real comparables, BibleProject and Desiring God, proving donor-funded nonprofit works at
   CiC's scale), one testing PBC revenue realism, one checking hybrid alternatives. The real fork
   came down to one question: does Mark want to preserve the option of a future personal sale?
   Asked directly, he confirmed: **"i want to keep the option to sell at some point."** PBC is now
   a **final decision**, not provisional. Full account:
   `Ministry/Organization/CiC_Nonprofit_Formation_Decision_Log.md`, 2026-07-21 (final) entry.
2. **Articles of Incorporation filed and accepted.** Entity ID 20261874960, Transaction #
   20261874960. `CiC_PBC_Articles_of_Incorporation_V0_4_FILING_READY.md` updated with the
   confirmed date/entity ID in place of the old "planned" placeholders.
3. **EIN obtained** from the IRS.
4. **Organizational Resolutions, IP Assignment Agreement, and Shareholder Buy-Sell Agreement all
   executed** — signed by both Mark and Susan Chadwick, copies given to Susan. Signable PDFs:
   `Faithways_Studio_Bylaws_and_Resolutions_SIGNABLE.pdf`,
   `Faithways_Studio_IP_Assignment_Agreement_SIGNABLE.pdf`,
   `Faithways_Studio_Shareholder_Agreement_SIGNABLE.pdf` (all in `Ministry/Organization/`).
5. **Founder stock purchase reduced from $700 to $40** ($20 each) — Mark and Susan only have a
   joint personal account and $700 was a real hardship, not a formality. All four documents (live
   Bylaws, signable PDF, combined formation-documents PDF) were corrected and **re-signed** to
   match. If any other file anywhere cites the old $700/$350 figures, they're stale — the correct
   number is **$40 total, $20 each**.
6. **Banking and payment processor decided: Relay (not Novo) + Stripe (not PayPal).** Relay
   chosen specifically because it supports genuine joint ownership — both Mark and Susan as true
   co-owners, not one primary + an added user, matching Susan's real 50% shareholder/Treasurer
   status. Stripe chosen to keep the payment experience on-site/on-brand and because its
   subscription tooling fits the "gating" tier of the monetization ladder. **Status: in progress,
   currently paused** — the CO SOS public business-search record hadn't caught up to today's
   filing yet, so the application is waiting on that (checked back tomorrow). Full reasoning:
   decision log, 2026-07-21 "DECIDED — Banking and payment processor" entry.
7. **Business email is live on two separate domains, via two separate free Zoho Mail
   organizations** (Zoho's free tier is one domain per org):
   - `mark@faithwaysstudio.com` and `susan@faithwaysstudio.com` — the corporate/entity-level
     identity (2 mailboxes).
   - `info@churchinconversation.com` — the product-facing identity (1 mailbox, room for 4 more on
     the free tier if ever needed).
   Both domains verified (DNS/MX confirmed working).
8. **churchinconversation.com is now the primary domain, replacing .org.** Reasoning: a .org
   suffix reads nonprofit-coded, which no longer fits now that Church in Conversation is a DBA of
   a for-profit PBC. **.org stays registered** (not abandoned), with a planned redirect to .com
   once the live site actually moves. **This directly affects `cic-website/`** — see the
   already-dispatched cleanup prompt below, which now includes this as an explicit item.
9. **Desktop shortcuts fixed and branded.** `CiC Dashboard.lnk` and `CiC Schedule.lnk` on Mark's
   OneDrive-redirected desktop — the Schedule shortcut was found broken (pointing to a pre-reorg
   path from before the 2026-07-20 filing audit moved `CiC_Gantt_Visual.html` into `Standing/`),
   fixed; Dashboard shortcut was missing entirely, created. Both now use the actual CiC "Arriving"
   mark as their icon (`Ministry/Communication/Brand-Assets/CiC_icon.ico`, generated from
   `CiC_Logo_Arriving_Favicon.svg`), and the same favicon was added to both
   `CiC_Dashboard.html` and `CiC_Gantt_Visual.html` directly (`<link rel="icon">`, relative path
   `../../Communication/Brand-Assets/CiC_icon.ico`) — **worth System Hub knowing this favicon
   pattern exists now**, in case other Standing/Operations HTML pages should get the same
   treatment for consistency. **One technical note for whoever touches this icon again:** the
   master SVG uses `pathLength="360"` for its dasharray/dashoffset math, which some SVG
   rasterizers (including the `sharp`/librsvg pipeline used to generate the .ico) don't support
   correctly, causing the mark to render rotated. The .ico was regenerated from a corrected
   version with the dasharray/dashoffset converted to real circumference units instead of
   pathLength-normalized ones — the master SVG file itself was never changed and remains correct
   for browser rendering.

## What's still NOT done — don't assume completion

- **#620 (Relay account)** — paused, waiting on CO SOS record catch-up.
- **#622 (Notice of Uncertificated Shares)** — blocked on #620.
- **#623 (file the "Church in Conversation" CO trade name/DBA)** — also blocked on the same CO
  SOS record catch-up; the existing name *reservation* does not automatically become the trade
  name — this is a fresh $20 filing once the record updates.
- **#18 (federal trademark filing, both marks)** — explicitly **deferred for budget reasons**
  (~$550-2,200 depending on scope), not urgent. Knockout searches already confirmed both names
  clear; common-law rights exist from use. Revisit only when real budget exists.
- **#22 (Organizational Covenant — CiC's own product-level commitments)** — still not formalized;
  this is where "always-free core access" and similar CiC-specific promises live now that they're
  deliberately not hard-locked at the parent-entity level.
- **#24 (domain/trademark/registrar transfers reflecting Faithways Studio as owner)** — depends on
  both the IP Assignment (done) and the trade name filing (not done yet).

## The cleanup thread already dispatched — still the priority, now with more context

`Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Nonprofit_to_PBC_Cleanup_2026-07-21.md`
was dispatched earlier today and is **still the active, priority piece of work** — it has not
been confirmed executed. It covers: the urgent live-site fix (`cic-website/support.html` making
false nonprofit/tax-deductible claims to real visitors), a full system review (not just a keyword
sweep) for nonprofit-era language across the ~37+ files a first-pass grep found, the three-bucket
sort discipline (decision logs untouched, standalone obsolete docs marked superseded, live/mixed
docs get surgical fixes), and the .org→.com domain switch. **Read that file in full before
starting** — it has the exact grep pattern, the bucket-sort rules, and the completion criteria
(a dated audit entry in this decision log, plus a direct report to Mark on the support.html fix
specifically).

## What "ensure all files are aligned" means concretely, right now

1. Execute the cleanup thread above if it hasn't been started.
2. While doing that pass, also verify against everything in this update — especially the
   **$40/$20 stock purchase figure** (not $700/$350) and the **Relay/Stripe** banking decision
   (not Novo/PayPal) — in case any file references the earlier, superseded numbers or choices.
3. Confirm the Gantt/task board/dashboard (already resynced multiple times today from the
   Funding/Formation thread directly) still read correctly after any further edits — spot-check
   rather than assume, since this update itself may already be slightly behind by the time it's
   read.
4. Report back with a real audit entry, same discipline as every other cross-file pass this
   project has done — which files were touched, which were left alone and why.
