from __future__ import annotations

def build_ucs(manifest: dict, m1_records: list[dict], mc_records: list[dict], flow_records: list[dict], drp_records: list[dict], alignments: dict) -> dict:
    return {
        "schema_version": "ucs_v1.1",
        "metadata": {
            "system_name": manifest["system_name"],
            "extraction_scope": "single repository",
            "source_type": "production_code",
            "schema_family": "semx",
            "generated_at_utc": manifest["generated_at_utc"],
            "repo_path": manifest["repo_path"],
            "source_files": manifest["source_files"],
            "extractor_name": "semx",
            "extractor_version": "v1"
        },
        "m1_records": m1_records,
        "mc_records": mc_records,
        "flow_records": flow_records,
        "drp_records": drp_records,
        "alignments": alignments
    }
