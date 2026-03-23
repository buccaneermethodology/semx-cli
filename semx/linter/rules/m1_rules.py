from __future__ import annotations

def lint_m1_rules(ucs: dict) -> list[dict]:
    issues = []
    for m1 in ucs.get("m1_records", []):
        name = m1["name"]
        m_id = m1["m_id"]
        if len(m1.get("decision_semantics", [])) < 3:
            issues.append({
                "issue_id": f"{m_id}-DECISION-CLOSURE",
                "object_type": "M1",
                "object_id": m_id,
                "rule_id": "M1_DECISION_CLOSURE",
                "severity": "error",
                "message": "decision_semantics 未形成完整闭环。",
                "evidence": {"name": name},
                "repair_hint": {"type": "strengthen_decision_semantics", "suggestion": "补足 iteration / normalization / matching / threshold 等步骤。"}
            })
        if "构建" in name or "封装" in name:
            issues.append({
                "issue_id": f"{m_id}-PROJECTION-LEAK",
                "object_type": "M1",
                "object_id": m_id,
                "rule_id": "M1_PROJECTION_LEAK",
                "severity": "warning",
                "message": "该对象可能是 projection / DTO 包装，而非真正的 M1。",
                "evidence": {"name": name},
                "repair_hint": {"type": "convert_to_projection_step", "suggestion": "考虑将其移为 Mc 中的 Projection step。"}
            })
    return issues
