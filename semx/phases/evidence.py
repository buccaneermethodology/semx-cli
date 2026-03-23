from __future__ import annotations
import re
from pathlib import Path

METHOD_PATTERN = re.compile(r"(public|private|protected)\s+[A-Za-z0-9_<>,\[\]\s]+\s+([A-Za-z0-9_]+)\s*\(")

def extract_evidence(repo_path: Path, manifest: dict) -> dict:
    symbols = []
    conditions = []
    domain_terms = set()
    for file_str in manifest["source_files"]:
        path = Path(file_str)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in METHOD_PATTERN.finditer(text):
            symbols.append({"file": str(path), "kind": "method", "visibility": match.group(1), "name": match.group(2)})
        for line in text.splitlines():
            if "if (" in line or "else" in line:
                conditions.append({"file": str(path), "condition_summary": line.strip()})
        for term in ["ECCN", "controlled", "material", "component", "rule", "ticket", "queue"]:
            if term.lower() in text.lower():
                domain_terms.add(term)
    return {
        "files": manifest["source_files"],
        "symbols": symbols,
        "conditions": conditions,
        "domain_terms": sorted(domain_terms),
        "external_dependencies": [],
        "diagnostics": [],
    }
