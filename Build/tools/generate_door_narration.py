#!/usr/bin/env python3
"""Narrate the Facilitator's welcome for each world's one-to-one conversation.

The welcome is the fixed `door` turn in engine.m4.facilitator_turns, filled
per world with its Representative's name and role and the world's card name.
The text is built by door_turn itself, so the audio cannot drift from what the
conversation screen shows. One file per admitted world, spoken once and served
as a static file.

Output: cic-poc/frontend/public/audio/door/<world-key>.mp3 and manifest.json,
which records a fingerprint of each text with the voice, model and settings it
was made with, so a change to the door text or a world's name or role shows
which audio is stale. Idempotent: a file whose fingerprint matches is skipped
unless --force.

Usage:
  ELEVENLABS_API_KEY=... python3 Build/tools/generate_door_narration.py \\
    --voice-id <id> --model <model_id> --output-format <fmt> \\
    --settings-json '{"stability":0.55,...}' [--only a,b] [--dry-run] [--force]

Every paid setting is named on the command and printed before the requests.
"""
import argparse
import hashlib
import json
import os
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.m4.facilitator_turns import door_turn  # noqa: E402

REGISTRY_DIR = ROOT / "records" / "worlds"
AUDIO_DIR = ROOT / "cic-poc" / "frontend" / "public" / "audio" / "door"
MANIFEST = AUDIO_DIR / "manifest.json"


def fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def door_entries(registry_dir: Path = REGISTRY_DIR) -> list[dict]:
    """One entry per admitted world that has a Representative, in key order."""
    entries = []
    for path in sorted(registry_dir.glob("*.yaml")):
        world = yaml.safe_load(path.read_text(encoding="utf-8"))
        rep = world.get("representative") or {}
        if world.get("state") != "admitted" or not rep.get("name"):
            continue
        text = door_turn(
            representative_name=rep["name"],
            role_label=rep["role_label"],
            world_name=world.get("card_name") or world["display_name"],
        )["text"]
        entries.append({"key": path.stem, "text": text, "hash": fingerprint(text)})
    return entries


def plan(entries: list[dict], manifest: dict, only=None, force=False, exists=None):
    exists = exists or (lambda key: (AUDIO_DIR / f"{key}.mp3").exists())
    chosen = [e for e in entries if not only or e["key"] in only]
    up_to_date, to_generate = [], []
    for e in chosen:
        fresh = exists(e["key"]) and manifest.get(e["key"], {}).get("hash") == e["hash"]
        (up_to_date if fresh and not force else to_generate).append(e)
    return up_to_date, to_generate


def synthesize(text, *, api_key, voice_id, model, output_format, settings):
    request = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format={output_format}",
        data=json.dumps({"text": text, "model_id": model, "voice_settings": settings}).encode(),
        headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return response.read(), int(response.headers.get("character-cost") or 0)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--voice-id")
    parser.add_argument("--model")
    parser.add_argument("--output-format")
    parser.add_argument("--settings-json")
    parser.add_argument("--only")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)

    entries = door_entries()
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    only = args.only.split(",") if args.only else None
    up_to_date, to_generate = plan(entries, manifest, only, args.force)
    total = sum(len(e["text"]) for e in to_generate)
    print(f"=== Door narration {'(dry run)' if args.dry_run else ''} ===")
    print(f"{len(entries)} worlds; {len(up_to_date)} up to date; {len(to_generate)} to generate, {total} characters")
    if args.dry_run:
        for e in to_generate:
            print(f"  would generate: {e['key']} ({len(e['text'])} chars)")
        return 0
    if not to_generate:
        print("Nothing to do.")
        return 0
    for flag, value in [("--voice-id", args.voice_id), ("--model", args.model),
                        ("--output-format", args.output_format), ("--settings-json", args.settings_json)]:
        if not value or value.startswith("--"):
            raise SystemExit(f"{flag} is required and is never read from the environment.")
    settings = json.loads(args.settings_json)
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise SystemExit("ELEVENLABS_API_KEY is not set.")
    print("=== PAID RUN, settings as actually used ===")
    print(f"voice id      : {args.voice_id}")
    print(f"model         : {args.model}")
    print(f"output format : {args.output_format}")
    print(f"settings      : {json.dumps(settings)}")
    print(f"worlds        : {len(to_generate)}, {total} characters")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    for e in to_generate:
        audio, cost = synthesize(e["text"], api_key=api_key, voice_id=args.voice_id, model=args.model,
                                 output_format=args.output_format, settings=settings)
        (AUDIO_DIR / f"{e['key']}.mp3").write_bytes(audio)
        manifest[e["key"]] = {"hash": e["hash"], "voiceId": args.voice_id, "model": args.model,
                              "outputFormat": args.output_format, "settings": settings, "chars": len(e["text"])}
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"  {e['key']}: {len(e['text'])} chars, {cost} credits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
