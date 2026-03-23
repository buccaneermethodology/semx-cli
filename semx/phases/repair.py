from __future__ import annotations
from semx.repairer.engine import repair_ucs

def run_repair(ucs: dict, lint_report: dict, mode: str = "full") -> dict:
    return repair_ucs(ucs, lint_report, mode=mode)
