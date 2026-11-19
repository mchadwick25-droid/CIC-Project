"""Shared plumbing for the gold-set tools: the repository root on the import
path, reads of files as they stood at a given commit, the records a world's
package was compiled from, stable ids and JSON-lines files."""
import functools
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import yaml  # noqa: E402

GOLD_DIR = REPO_ROOT / "canon" / "gold_set"
WORK_DIR = REPO_ROOT / "Build" / "Ministry" / "Features" / "Answering-From-Sources" / "Stage1"


@functools.lru_cache(maxsize=4096)
def git_show(commit: str, path: str) -> str | None:
    """The file at `path` as it stood at `commit`, or None when it did not exist."""
    done = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=REPO_ROOT, capture_output=True)
    if done.returncode != 0:
        return None
    return done.stdout.decode("utf-8", errors="replace")


@functools.lru_cache(maxsize=64)
def git_ls(commit: str, path: str) -> tuple[str, ...]:
    done = subprocess.run(["git", "ls-tree", "-r", "--name-only", commit, path], cwd=REPO_ROOT, capture_output=True, text=True)
    return tuple(done.stdout.split()) if done.returncode == 0 else ()


def parse_record(raw: str) -> dict:
    """A record file's front matter as a dict, with its body under "_body"."""
    _, front, body = raw.split("---", 2)
    record = yaml.safe_load(front) or {}
    record["_body"] = body.strip()
    return record


@functools.lru_cache(maxsize=64)
def records_at(commit: str, world: str) -> dict:
    """Every record of `world` as it stood at `commit`, by id."""
    out = {}
    for path in git_ls(commit, f"records/{world}"):
        if not path.endswith(".md"):
            continue
        raw = git_show(commit, path)
        if raw is None or not raw.startswith("---"):
            continue
        record = parse_record(raw)
        if record.get("id"):
            record["_path"] = path
            out[record["id"]] = record
    return out


def package_for_manifest_hash(world: str, manifest_hash: str) -> dict:
    """The stored manifest of the package a run pinned (by the sha256 of its
    manifest file), with its location."""
    want = manifest_hash.removeprefix("sha256:")
    for path in sorted((REPO_ROOT / "packages" / world).glob("*/manifest.json")):
        payload = path.read_bytes()
        if hashlib.sha256(payload).hexdigest() == want:
            return {**json.loads(payload), "_location": str(path.parent.relative_to(REPO_ROOT))}
    raise LookupError(f"{world}: no package manifest hashes to {manifest_hash}")


def stable_id(prefix: str, *parts: str, length: int = 12) -> str:
    digest = hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()
    return f"{prefix}-{digest[:length]}"


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
