"""Lists the live inference profiles for one region and says whether a
global counterpart exists for each configured model pattern. One control-plane
call, no model spend; run it from the live-tests environment.

A listed profile is not proof of invoke access (the 2026-09-24 report found
listed profiles that were denied), so selecting a global profile is a
settings change (CIC_API_VOICE_MODEL_PATTERN / CIC_API_SAFETY_MODEL_PATTERN
set to the global id) followed by the capped live test, never an automatic
switch.

    python -m engine.provider.list_profiles --region us-east-1 --out report.json
"""
import argparse
import json
import sys

import boto3

from engine.api.config import _DEFAULT_SAFETY_MODEL_PATTERN, _DEFAULT_VOICE_MODEL_PATTERN


def global_counterparts(profile_ids: list[str], pattern: str) -> list[str]:
    stem = pattern.lower()
    for prefix in ("us.", "eu.", "apac.", "global."):
        stem = stem.removeprefix(prefix)
    return sorted(i for i in profile_ids if i.lower().startswith("global.") and stem in i.lower())


def build_report(profile_ids: list[str], region: str, patterns: dict[str, str]) -> dict:
    return {
        "region": region,
        "profiles": sorted(profile_ids),
        "global_profiles": sorted(i for i in profile_ids if i.lower().startswith("global.")),
        "patterns": {role: {"pattern": p, "global_counterparts": global_counterparts(profile_ids, p)} for role, p in patterns.items()},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--region", required=True)
    parser.add_argument("--out")
    args = parser.parse_args(argv)
    summaries = boto3.client("bedrock", region_name=args.region).list_inference_profiles(maxResults=1000)["inferenceProfileSummaries"]
    report = build_report(
        [p["inferenceProfileId"] for p in summaries],
        args.region,
        {"voice": _DEFAULT_VOICE_MODEL_PATTERN, "safety": _DEFAULT_SAFETY_MODEL_PATTERN},
    )
    text = json.dumps(report, indent=2)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
