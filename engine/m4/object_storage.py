"""Object storage for compiled world packages (WO-1, Artifact-2 SS5:
"Packages are built by CI, uploaded to object storage (S3, versioned
bucket, private), and referenced by the registry"). Cloudflare R2 by
provider choice (Mark, 2026-09-16) - same account cic-website already
uses, S3-API-compatible so boto3 works unchanged, no egress fees, and
the real fleet-wide package total (13MB across 10 worlds, measured the
same day) sits entirely inside R2's free tier.

R2 is not AWS, so boto3's standard credential chain (the thing
engine.provider.bedrock.make_client() already relies on) does not apply
here - R2's own access key/secret and account endpoint are read
directly from env vars, explicitly, the same "never guess, fail loudly"
posture engine/api/config.py already holds AWS_REGION to.

Never imported by engine/m4/world_loader.py itself - that module stays
a pure local-disk reader with its own unchanged hash verification
(verify_package_dict), regardless of where the bytes it reads came
from. engine/m4/package_fetch.py is the seam: it may call this module
to put bytes on local disk before world_loader.load() ever runs, but
a wrong or malicious fetch here is still caught by that unchanged
verification, not trusted on this module's own say-so.
"""
from __future__ import annotations

import os
from pathlib import Path

import boto3


class ObjectStorageError(Exception):
    """A configured bucket refused a request, or the account/keys were rejected -
    never silently swallowed. A caller that wants "not configured" and "configured
    but failing" to mean different things checks is_configured() first."""


def is_configured() -> bool:
    return bool(os.environ.get("CIC_API_PACKAGE_BUCKET"))


def _client():
    endpoint = os.environ.get("CIC_API_PACKAGE_BUCKET_ENDPOINT")
    if not endpoint:
        raise ObjectStorageError(
            "CIC_API_PACKAGE_BUCKET is set but CIC_API_PACKAGE_BUCKET_ENDPOINT is not - "
            "R2's account endpoint has no default to guess (unlike AWS_REGION for Bedrock, "
            "there is no single well-known R2 endpoint)"
        )
    access_key = os.environ.get("CIC_API_PACKAGE_BUCKET_ACCESS_KEY_ID")
    secret_key = os.environ.get("CIC_API_PACKAGE_BUCKET_SECRET_ACCESS_KEY")
    if not access_key or not secret_key:
        raise ObjectStorageError(
            "CIC_API_PACKAGE_BUCKET is set but its own access key/secret are not - "
            "R2 credentials are never read from AWS's own credential chain, on purpose "
            "(a Bedrock IAM identity granting S3-shaped access it was never scoped for "
            "would be exactly the blast-radius mistake this separation avoids)"
        )
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        # R2 only speaks the "auto" region - a real AWS region name here is rejected.
        region_name="auto",
    )


def upload_package_dir(local_dir: Path, key_prefix: str) -> list[str]:
    """Uploads every file under local_dir (recursively) to
    <key_prefix>/<relative path>. Returns the keys written, for a caller
    (tools/upload_package.py) that wants to print or log them. Overwrites
    any existing object at the same key - packages are content-addressed
    by their own timestamped directory name, so a real collision would
    mean the same package_id built twice with different bytes, which
    world_loader's own hash verification catches downstream regardless."""
    client = _client()
    bucket = os.environ["CIC_API_PACKAGE_BUCKET"]
    written = []
    for path in sorted(local_dir.rglob("*")):
        if not path.is_file():
            continue
        key = f"{key_prefix}/{path.relative_to(local_dir).as_posix()}"
        try:
            client.upload_file(str(path), bucket, key)
        except Exception as e:  # noqa: BLE001 - re-raised as this module's own error, never swallowed
            raise ObjectStorageError(f"upload of {path} to {bucket}/{key} failed: {e}") from e
        written.append(key)
    return written


def download_package_dir(key_prefix: str, dest_dir: Path) -> list[str]:
    """Downloads every object under key_prefix into dest_dir, mirroring
    the relative-path structure upload_package_dir wrote. dest_dir is
    created if absent. Raises ObjectStorageError (never a partial,
    silently-incomplete directory left for a caller to trust) if the
    prefix has no objects at all - that is a real configuration or
    build-vs-registry mismatch, not a package that happens to be empty."""
    client = _client()
    bucket = os.environ["CIC_API_PACKAGE_BUCKET"]
    dest_dir.mkdir(parents=True, exist_ok=True)
    fetched = []
    paginator = client.get_paginator("list_objects_v2")
    try:
        for page in paginator.paginate(Bucket=bucket, Prefix=f"{key_prefix}/"):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                rel = key[len(key_prefix) + 1 :]
                target = dest_dir / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                client.download_file(bucket, key, str(target))
                fetched.append(key)
    except ObjectStorageError:
        raise
    except Exception as e:  # noqa: BLE001
        raise ObjectStorageError(f"download of {bucket}/{key_prefix}/* failed: {e}") from e
    if not fetched:
        raise ObjectStorageError(f"no objects found under {bucket}/{key_prefix}/ - nothing was ever uploaded there, or the prefix is wrong")
    return fetched
