from __future__ import annotations

def lint_flow_rules(ucs: dict) -> list[dict]:
    issues = []
    for flow in ucs.get("flow_records", []):
        if not flow.get("backed_by_mc"):
            issues.append({
                "issue_id": f'{flow["flow_id"]}-MC-GROUNDING',
                "object_type": "Flow",
                "object_id": flow["flow_id"],
                "rule_id": "FLOW_MC_GROUNDING",
                "severity": "error",
                "message": "Flow 未锚定到任何 Mc。",
                "evidence": {"name": flow["name"]},
                "repair_hint": {"type": "rebind_flow_to_mc", "suggestion": "将该 Flow 绑定到最匹配的 Mc。"}
            })
    return issues
