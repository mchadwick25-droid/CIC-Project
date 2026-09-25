#!/usr/bin/env python3
"""The action `.github/workflows/repin-on-library-change.yml` runs after a
push to main touches `cic/corpus-map/**` or `cic/texts/**` (Library Access
Gate D3 SS6.3, increment 5): the library itself changed, so every world
whose shelf drew from what changed is stale and needs a new package pinned
to the new bytes.

For every world `engine.m2.checks.staleness_sweep` finds stale: rebuild its
package, repoint `records/worlds/<code>.yaml` at the new one, retire the
manifest.json the old pin left behind, and open one PR per world on its own
`repin/<code>` branch - never a bulk PR. The registry split (increment 1)
is what buys that: two worlds' repins never touch the same file, so an
active world thread's own branch conflicts with at most its own repin.

Not engine code - this is CI automation with real git and GitHub API side
effects, run only from the workflow above, never imported by anything under
engine/.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GH_API = "https://api.github.com"
BOT_NAME = "github-actions[bot]"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


def _run(cmd: list[str]) -> str:
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=True, text=True, capture_output=True)
    return result.stdout


def _stale_worlds() -> dict[str, dict]:
    from engine.m2.checks import staleness_sweep

    return {w: r for w, r in staleness_sweep().items() if r.get("stale")}


def _current_location(world_key: str) -> str | None:
    from engine.m1.registry import load_registry

    entry = load_registry().get(world_key, {})
    return (entry.get("package") or {}).get("location")


def _repoint_registry(world_key: str, *, manifest_hash: str, location: str) -> Path:
    path = REPO_ROOT / "records" / "worlds" / f"{world_key}.yaml"
    text = path.read_text(encoding="utf-8")
    text, n_hash = re.subn(r'(?m)^(  manifest_hash: ")[^"]*(")$', rf"\g<1>{manifest_hash}\g<2>", text, count=1)
    text, n_loc = re.subn(r'(?m)^(  location: ")[^"]*(")$', rf"\g<1>{location}\g<2>", text, count=1)
    if n_hash != 1 or n_loc != 1:
        raise RuntimeError(
            f"{world_key}: expected exactly one package.manifest_hash and one package.location "
            f"line in {path.relative_to(REPO_ROOT)}, found {n_hash}/{n_loc} - repin refuses to "
            "guess which line to edit"
        )
    path.write_text(text, encoding="utf-8")
    return path


def repin_one_world(world_key: str, reason: str) -> dict:
    branch = f"repin/{world_key}"
    _run(["git", "checkout", "-B", branch, "origin/main"])
    old_location = _current_location(world_key)

    build_out = _run([sys.executable, "-m", "engine.m2.cli", "build", world_key])
    build_result = json.loads(build_out)
    registry_path = _repoint_registry(world_key, manifest_hash=build_result["manifest_hash"], location=build_result["location"])

    new_manifest = REPO_ROOT / build_result["location"] / "manifest.json"
    _run(["git", "add", "--", str(new_manifest), str(registry_path)])
    if old_location:
        old_manifest = REPO_ROOT / old_location / "manifest.json"
        if old_manifest.is_file():
            _run(["git", "rm", "--quiet", "--", str(old_manifest)])

    _run([
        "git", "-c", f"user.name={BOT_NAME}", "-c", f"user.email={BOT_EMAIL}",
        "commit", "-m",
        f"Repin {world_key}: library changed\n\n{reason}\n\n"
        "Auto-repin, Library Access Gate D3 SS6.3 (increment 5).",
    ])
    _run(["git", "push", "--force-with-lease", "-u", "origin", branch])

    return {
        "world_key": world_key,
        "branch": branch,
        "old_location": old_location,
        "new_location": build_result["location"],
        "new_manifest_hash": build_result["manifest_hash"],
        "reason": reason,
    }


def _api(method: str, path: str, token: str, body: dict | None = None) -> dict | list:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        f"{GH_API}{path}", data=data, method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Content-Type": "application/json"} if data is not None else {}),
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def _existing_open_pr(branch: str, *, token: str, repo: str, owner: str) -> dict | None:
    matches = _api("GET", f"/repos/{repo}/pulls?head={owner}:{branch}&state=open", token)
    return matches[0] if matches else None


def open_or_update_pr(info: dict, *, token: str, repo: str, owner: str) -> str:
    body = (
        f"Auto-repin: `{info['world_key']}`'s pinned package was built against the library "
        f"as it stood before this push changed `cic/corpus-map/**` or `cic/texts/**`.\n\n"
        f"**Why:** {info['reason']}\n\n"
        f"- old package: `{info['old_location']}`\n"
        f"- new package: `{info['new_location']}`\n"
        f"- new manifest hash: `{info['new_manifest_hash']}`\n\n"
        "Opened by `repin-on-library-change` (Library Access Gate D3 SS6.3, increment 5). "
        "`m2-staleness-check` passing on this branch is the proof the repin is correct - "
        "merge once CI is green."
    )
    existing = _existing_open_pr(info["branch"], token=token, repo=repo, owner=owner)
    if existing:
        _api("PATCH", f"/repos/{repo}/pulls/{existing['number']}", token, {"body": body})
        return existing["html_url"]
    created = _api("POST", f"/repos/{repo}/pulls", token, {
        "title": f"Repin {info['world_key']}: library changed",
        "head": info["branch"],
        "base": "main",
        "body": body,
    })
    return created["html_url"]


def _early_exit(stale: dict[str, dict], token: str | None) -> int | None:
    """Decides whether main() should stop before doing any repin work, and
    with what exit code - or return None to mean "keep going". Split out
    of main() so the two exit paths (nothing stale; something stale but no
    token) are each a plain function of their inputs, testable without git
    or network."""
    if not stale:
        print("no stale worlds - nothing to repin")
        return 0

    if not token:
        print(
            f"{len(stale)} world(s) stale ({', '.join(sorted(stale))}) but REPIN_PR_TOKEN is not "
            "set - refusing to repin.\n\n"
            "The default GITHUB_TOKEN cannot be used here: a PR it opens never triggers the "
            "pull_request workflow, so it would sit with zero CI checks and never clear branch "
            "protection (D3 SS6.3's own flagged, build-time-only fact). Add a repository secret "
            "named REPIN_PR_TOKEN - a fine-grained PAT scoped to this repo with Contents: Read "
            "and write plus Pull requests: Read and write, or an equivalent GitHub App "
            "installation token - then re-run this workflow.",
            file=sys.stderr,
        )
        return 1

    return None


def main() -> int:
    repo = os.environ["GITHUB_REPOSITORY"]
    owner = repo.split("/", 1)[0]

    _run(["git", "fetch", "origin", "main"])
    stale = _stale_worlds()
    token = os.environ.get("REPIN_PR_TOKEN")

    early = _early_exit(stale, token)
    if early is not None:
        return early
    assert token is not None  # _early_exit already returned above if it were falsy

    failures = []
    for world_key, result in sorted(stale.items()):
        reason = result.get("reason", "staleness sweep found it stale")
        try:
            info = repin_one_world(world_key, reason)
            url = open_or_update_pr(info, token=token, repo=repo, owner=owner)
            print(f"{world_key}: {url}")
        except (subprocess.CalledProcessError, RuntimeError, urllib.error.HTTPError) as exc:
            print(f"{world_key}: FAILED - {exc}", file=sys.stderr)
            failures.append(world_key)

    _run(["git", "checkout", "main"])
    if failures:
        print(f"{len(failures)} world(s) failed to repin: {', '.join(failures)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
