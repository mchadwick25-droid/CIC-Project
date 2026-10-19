# Launch prompts and cic-build-cycle skill against CLAUDE.md — 2026-10-19

Read-only audit by an Opus reviewer of five launch prompts and the repo copy of the `cic-build-cycle` skill, against CLAUDE.md as it stands on 2026-10-19. Nothing was edited. The reviewer's findings were not re-confirmed by a second reader; the author spot-checked the three line citations marked (checked). Severity: C could make a thread break a rule; S stale wording; H harmless.

Not covered: three other files in `Build/Ministry/Operations/Standing/Launch-Prompts/` (`CiC_Modern_Term_Bridge_Buildout_Thread_Launch_2026-09-04.md`, `CiC_New_World_Build_Record_Native_Launch_V3_2026-09-08.md`, `CiC_lpc_Build_Launch_Prompt_V2.0_2026-09-29.md`).

## Worst conflicts

1. GoLive l.79-84 (checked): the thread opens the `main` to `live` promotion PR. CLAUDE.md 4.1: never open a PR into `live`; promotion is Mark's call through the runbook.
2. World Build V2.0 l.223-233 (checked) and skill l.145 (checked): live interviews and blind probes are treated as paid bulk runs ("run a small sample, get approval"). CLAUDE.md 3.2: a model call outside a conversation needs a test Mark approved by name, with `--live-test` and `--cap-usd`; the sample is itself a metered call.
3. GoLive l.48-49: the thread runs the M3 admission battery. 3.2 and decisions 56 and 58.
4. GoLive l.75-76 and l.98 (checked): "Never self-merge". CLAUDE.md 4.1: your own green PR is merged into `main`.
5. lpc Representative l.71-72: adversarial reviews to a subagent with no model named; no model for Doc_10 or rendering. 2.2: reviews and rendering on Opus; Doc_10 on Fable.
6. Skill l.104 (checked): "Never write a fourth file." Misses the Cap-ruling exception in 3.4.
7. Voice Alignment l.124: names `CiC_Voice_Style_Guide_and_Scaling_Plan.md` as the one binding readability rulebook. 1.2 names `engine/m7/turn_readability.py` and the VR_1A files.
8. lpc Representative l.16-17 and GoLive l.11-13: run worlds concurrently. 2.3: one world at a time by default.

## By file (other conflicts)

- GoLive: references "Scaling the build" and a "escalation table" that no longer exist (now 3.4 and 4.1); a deploy-branch question the runbook calls settled; restates the escalation categories (3.5 item 4); world-state snapshot; no handoff rule.
- lpc Representative: "CO-022 self-disposition" (retired 2026-09-25); three rounds with no every-file counting or exception; one branch and one PR per document, against Part 5; names Completion_Standard V1.3 (disk holds V1.4); copies never-invent rules; no handoff rule.
- World Build V2.0: "push only on Mark's word" against 4.1 and Part 5; every-file cap with no exception; Fable "diagnoses failures" against the 2.2 reservation; Sonnet and Fable pilot for Doc_10 against the 2.2 table; copies closure, invention, readability and safety rules; summary to the System Hub thread instead of a handoff; no AskUserQuestion rule for the identity ask.
- Website V2: "no PRs unless Mark asks" against Part 5; "merge means live, because Render auto-deploys main" (half true: Render production is on `live`, Cloudflare production is still on `main` per the runbook); "divergent / struggle / convergent" where 4.2 now says groan zone; names Build Process V1.3.
- Voice Alignment: section names that no longer exist ("How we work", "Accessible and rigorous", "Source fidelity"); recommendation rule without AskUserQuestion; "8 built/live worlds" snapshot.
- Skill (repo copy): cap lines mix rounds and files; "metered-spend ceiling" where 3.2 requires approval per named run; output location tension with 2.1 (see below); no pointer to PRs, merge, `live`, handoff or AskUserQuestion.

## Live skill versus repo copy

They are not the same text. The repo description says it enforces a cap of three review files. The claude.ai description (as quoted in this session) uses finaliz- four times and so conflicts with 4.4 in its description alone. The body of the live skill could not be read. Skills are edited on claude.ai, not in the repo.

## The word "finalize"

GoLive 0; lpc Representative 0; World Build V2.0 1 (quoted in order to ban it); Website V2 0; Voice Alignment 0; repo skill 0; live skill description 4.

## Review-cap counting unit (open for Mark)

CLAUDE.md 3.4 holds two phrasings: "three rounds of substantial revision" and "every review file on a document counts toward the three". Example: Review R1 (substantial), Recheck R2 (cosmetic only), SpotCheck R3 is 3 files, so escalate under the every-file rule, but 1 round under the substantial-revision rule. The 2026-09-30 ruling and the `roundcount` gate follow the every-file rule. The cap-ruling exception in CLAUDE.md also omits conditions found in the decision log: a named file is excused only when three counted files precede it, a ruling cannot excuse any of the first three, and a `Cycle reset` header field restarts the count.

## Which prompts are still referenced

- GoLive: no live file references it; archivable.
- lpc Representative: referenced only by `Build/worlds/lpc/lpc_Decision_Log.md` l.1997 as history; Phases 2 to 7 and the Permanent Prompt already exist under `Build/worlds/lpc/Representative/`; archivable.
- World Build V2.0: referenced by `CiC_lpc_Build_Launch_Prompt_V2.0_2026-09-29.md` and three Process-V2.0 audit files; still in use, so edit it.
- Website V2: referenced by `Build/Ministry/Features/Website-V2/Decision-Log.md`; last commit on that workstream 2026-10-15; Mark's call.
- Voice Alignment: no file references it; the workstream folder exists; Mark's call.

## Not verified

Mark's own words quoted in Voice Alignment l.23-24, 70-71 and 104-107; "(Mark's call, 2026-09-16)" in GoLive l.10; the "egress-blocked" claim in GoLive l.103-105; PRs #353, #355, #443, #197 and #246; "Fable 5.1" as a model id; whether the Website V2 routing was Mark's ruling; whether CO-022's retirement covered self-disposition.

## Tension in CLAUDE.md itself

The skill puts review files beside the document in the world's folder, because the gate reads world folders. CLAUDE.md 2.1 says review rounds go to `Build/Ministry/`. This is for Mark to rule; do not edit silently.
