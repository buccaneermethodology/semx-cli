from __future__ import annotations

def lint_mc_rules(ucs: dict) -> list[dict]:
    issues = []
    for mc in ucs.get("mc_records", []):
        has_anchor = any(step["ref_type"] in {"M1", "ExternalCapability"} for step in mc.get("composition", []))
        if not has_anchor:
            issues.append({
                "issue_id": f'{mc["mc_id"]}-GROUNDING',
                "object_type": "Mc",
                "object_id": mc["mc_id"],
                "rule_id": "MC_GROUNDED_IN_M1",
                "severity": "error",
                "message": "Mc 缺少真实能力锚点。",
                "evidence": {"composition": mc.get("composition", [])},
                "repair_hint": {"type": "repair_alignment", "suggestion": "补充 M1 或 ExternalCapability 作为核心事实/判断来源。"}
            })
    return issues
