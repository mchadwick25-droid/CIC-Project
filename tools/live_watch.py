#!/usr/bin/env python3
"""The scheduled check on the production engine (.github/workflows/live-watch.yml).

Fails, so GitHub emails the repository owner, when any of these holds:
- /health does not answer twice in a row;
- the engine runs a commit other than the head of the `live` branch, and that
  head is older than a deploy normally takes;
- the last database backup did not reach the bucket, or is more than a day old.

Reads only the public /health route and the public GitHub API. Makes no model
call and sends nothing to the engine but that one GET.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

DEPLOY_GRACE = timedelta(minutes=30)
BACKUP_MAX_AGE = timedelta(hours=26)
HEALTH_ATTEMPTS = 2
HEALTH_RETRY_SECONDS = 30
TIMEOUT_SECONDS = 20


def fetch_json(url: str, headers: dict | None = None) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "cic-live-watch", **(headers or {})})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_health(engine_url: str, attempts: int = HEALTH_ATTEMPTS, wait: float = HEALTH_RETRY_SECONDS) -> dict | None:
    for attempt in range(attempts):
        try:
            return fetch_json(f"{engine_url.rstrip('/')}/health")
        except (urllib.error.URLError, TimeoutError, ValueError, OSError):
            if attempt + 1 < attempts:
                time.sleep(wait)
    return None


def fetch_live_head(repo: str, token: str | None) -> tuple[str, datetime]:
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    commit = fetch_json(f"https://api.github.com/repos/{repo}/commits/live", headers)
    committed = commit["commit"]["committer"]["date"]
    return commit["sha"], datetime.fromisoformat(committed.replace("Z", "+00:00"))


def problems(health: dict | None, head_sha: str, head_at: datetime, now: datetime) -> list[str]:
    if health is None:
        return [f"The engine did not answer /health on {HEALTH_ATTEMPTS} tries."]
    found: list[str] = []
    running = health.get("commit") or "unknown"
    if running == "unknown":
        found.append("The engine does not report which commit it runs (RENDER_GIT_COMMIT is not set).")
    elif running != head_sha and now - head_at > DEPLOY_GRACE:
        found.append(
            f"The engine runs {running[:12]}, but live has been at {head_sha[:12]} since "
            f"{head_at:%Y-%m-%d %H:%M} UTC. The newer deploy has not gone live; check Render's deploy log."
        )
    backup = health.get("backup")
    if not isinstance(backup, dict):
        found.append("The engine does not report a backup result.")
        return found
    last_run = backup.get("last_run_at")
    if not last_run:
        found.append("No database backup has run yet.")
    else:
        ran_at = datetime.fromisoformat(last_run.replace("Z", "+00:00"))
        if now - ran_at > BACKUP_MAX_AGE:
            found.append(f"The last database backup ran at {ran_at:%Y-%m-%d %H:%M} UTC, more than a day ago.")
    if last_run and not backup.get("uploaded"):
        found.append("The last database backup did not reach the backup bucket. Is CIC_API_BACKUP_BUCKET set in Render?")
    return found


def main() -> int:
    engine_url = os.environ["ENGINE_URL"]
    repo = os.environ["REPO"]
    health = fetch_health(engine_url)
    head_sha, head_at = fetch_live_head(repo, os.environ.get("GITHUB_TOKEN"))
    found = problems(health, head_sha, head_at, datetime.now(timezone.utc))
    lines = [f"- {p}" for p in found] or ["- All clear: the engine answers, runs the head of live, and last night's backup uploaded."]
    report = "\n".join([f"## Live watch: {engine_url}", *lines])
    print(report)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report + "\n")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
