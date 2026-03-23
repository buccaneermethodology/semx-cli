from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path

def build_manifest(repo_path: Path) -> dict:
    source_files = [str(p) for p in repo_path.rglob("*.java") if p.is_file()]
    return {
        "schema_version": "ucs_v1.1",
        "system_name": repo_path.name,
        "repo_path": str(repo_path),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_files": source_files,
        "source_type": "production_code",
        "schema_family": "semx",
    }
