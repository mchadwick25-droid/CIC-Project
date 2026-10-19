# Usage discipline — Mark's own account practices

The thread-facing cost rules live in `CLAUDE.md` (2.2 models, 2.3 budget, 3.2 spending, 3.3 context). This page holds the account-level practices Mark follows himself. They moved out of `CLAUDE.md` on 2026-10-19 because they are things Mark does, not rules a thread follows.

## The plan

- The account is on Max-200. $200 a month is a real financial stretch, so treat it as a hard cap. The goal is to get everything possible from the flat fee, never to fall back on paid overage.
- Max-200 draws Claude chat, Claude Code, and Cowork from one shared usage pool. When more than one surface is in use, watch the total burn, not one session.

## Settings to keep

- Keep "extra usage" OFF in Settings → Usage, or capped at $0. Hitting the weekly ceiling means spend less, not turn on overage. Don't leave it on "just in case."
- If overage is ever needed for something unavoidable, turn it on deliberately, do the one thing, and turn it back off.
- A session's own cost telemetry (what the work would cost at raw API rates) is not a bill. Only actual overage usage is.

## Habits

- Check `/usage` periodically to catch a runaway pattern before it costs the rest of the week.
- Use `/compact` or `/clear` between unrelated pieces of work. Reach for these before reaching for a cheaper model.
- Batch related work into one longer session instead of many short restarted ones. Short sessions lose the prompt cache and pay for context again every time.
- Spread heavy build and review days across the week instead of bursting a week's work into one or two days.
- Use Plan Mode before implementation on anything with uncertain scope.
