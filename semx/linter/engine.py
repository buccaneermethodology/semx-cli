from __future__ import annotations
from semx.linter.rules.m1_rules import lint_m1_rules
from semx.linter.rules.mc_rules import lint_mc_rules
from semx.linter.rules.flow_rules import lint_flow_rules
from semx.linter.rules.cross_layer_rules import lint_cross_layer_rules

def lint_ucs(ucs: dict) -> dict:
    issues = []
    issues.extend(lint_m1_rules(ucs))
    issues.extend(lint_mc_rules(ucs))
    issues.extend(lint_flow_rules(ucs))
    issues.extend(lint_cross_layer_rules(ucs))
    error_count = sum(1 for i in issues if i["severity"] == "error")
    warning_count = sum(1 for i in issues if i["severity"] == "warning")
    status = "fail" if error_count > 0 else ("warning" if warning_count > 0 else "pass")
    return {
        "linter_version": "usl_v1.0",
        "summary": {
            "status": status,
            "total_objects": len(ucs.get("m1_records", [])) + len(ucs.get("mc_records", [])) + len(ucs.get("flow_records", [])) + len(ucs.get("drp_records", [])),
            "error_count": error_count,
            "warning_count": warning_count
        },
        "issues": issues
    }
