#!/usr/bin/env python3
"""PreToolUse hook: refuse any pull request into `live` and any push to `live`.

Promotion from `main` to `live` is Mark's, through
Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md.
Exit code 2 blocks the tool call and shows the message to the model.
"""
import json
import re
import sys

MESSAGE = (
    "Blocked: `live` is production. A thread never opens a pull request into "
    "`live` or pushes to it. Target `main` instead. Promotion to `live` is "
    "Mark's call, through Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md "
    "(CLAUDE.md 4.1)."
)


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    tool = event.get("tool_name", "")
    args = event.get("tool_input", {}) or {}

    if tool in ("mcp__github__create_pull_request", "mcp__github__update_pull_request"):
        if str(args.get("base", "")).strip() == "live":
            print(MESSAGE, file=sys.stderr)
            return 2

    if tool == "Bash":
        command = str(args.get("command", ""))
        if re.search(r"\bgit\s+push\b[^|;&]*(\s|:)(refs/heads/)?live(\s|$)", command):
            print(MESSAGE, file=sys.stderr)
            return 2
        if re.search(r"\bgh\s+pr\s+(create|edit)\b[^|;&]*--base[ =]live\b", command):
            print(MESSAGE, file=sys.stderr)
            return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
