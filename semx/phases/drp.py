from __future__ import annotations

def derive_drp_records(flows: list[dict], evidence: dict) -> list[dict]:
    records = []
    flow_ids = {f["flow_id"] for f in flows}
    if "FLOW-ECCN-CONTROLLED-JUDGMENT" in flow_ids:
        records.append({
            "drp_id": "DRP-AUTHORITY-RULE-NORMALIZED-MATCH",
            "name": "权威规则驱动的标准化命中判定",
            "pattern": ["获取外部权威规则", "对输入编码做标准化", "按固定匹配语义判定是否命中", "返回命中集合"],
            "validation": {"status": "warning", "checks": [{"check_id": "cross_flow_reusability_test", "result": "warning", "reason": "当前仅在一个 Flow 中观察到，后续可复用性待验证。"}]},
            "evidence": {"flows": ["FLOW-ECCN-CONTROLLED-JUDGMENT"], "methods": ["getApplyCode", "resolveEccnNos"], "notes": ["已抽象为领域模式，而非代码调用链复述。"]},
            "diagnostics": []
        })
    return records
