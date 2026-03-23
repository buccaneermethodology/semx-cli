from __future__ import annotations

def lint_cross_layer_rules(ucs: dict) -> list[dict]:
    issues = []
    drp_ids = {d["drp_id"] for d in ucs.get("drp_records", [])}
    flow_ids = {f["flow_id"] for f in ucs.get("flow_records", [])}
    mc_ids = {m["mc_id"] for m in ucs.get("mc_records", [])}
    m1_ids = {m["m_id"] for m in ucs.get("m1_records", [])}
    for item in ucs.get("alignments", {}).get("flow_to_drp", []):
        if item["flow_id"] not in flow_ids or item["drp_id"] not in drp_ids:
            issues.append({
                "issue_id": f'{item["flow_id"]}-ALIGNMENT',
                "object_type": "Alignment",
                "object_id": item["flow_id"],
                "rule_id": "ALIGNMENT_INVALID_REFERENCE",
                "severity": "error",
                "message": "flow_to_drp 包含无效引用。",
                "evidence": item,
                "repair_hint": {"type": "repair_alignment", "suggestion": "修正 flow_id 或 drp_id 引用。"}
            })
    for item in ucs.get("alignments", {}).get("mc_to_m1", []):
        if item["mc_id"] not in mc_ids or any(m not in m1_ids for m in item["m_ids"]):
            issues.append({
                "issue_id": f'{item["mc_id"]}-MC-M1-ALIGNMENT',
                "object_type": "Alignment",
                "object_id": item["mc_id"],
                "rule_id": "ALIGNMENT_INVALID_REFERENCE",
                "severity": "error",
                "message": "mc_to_m1 包含无效引用。",
                "evidence": item,
                "repair_hint": {"type": "repair_alignment", "suggestion": "修正 mc_id 或 m_ids 引用。"}
            })
    return issues
