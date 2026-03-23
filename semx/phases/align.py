from __future__ import annotations

def build_alignments(flows: list[dict], drp_records: list[dict], mc_records: list[dict], m1_records: list[dict]) -> dict:
    mc_ids = {mc["mc_id"] for mc in mc_records}
    drp_ids = {drp["drp_id"] for drp in drp_records}
    m1_ids = {m["m_id"] for m in m1_records}
    flow_to_drp = []
    if "MC-ECCN-JUDGE-CONTROLLED-ECCNS-V1" in mc_ids and "DRP-AUTHORITY-RULE-NORMALIZED-MATCH" in drp_ids:
        flow_to_drp.append({"flow_id": "FLOW-ECCN-CONTROLLED-JUDGMENT", "drp_id": "DRP-AUTHORITY-RULE-NORMALIZED-MATCH", "reason": "该流程本质上是权威规则 + 标准化 + 命中判定。"})
    mc_to_m1 = []
    if "M-ECCN-RULE-RETRIEVE-CONTROLLED-CODESET-V1" in m1_ids:
        mc_to_m1.append({"mc_id": "MC-ECCN-JUDGE-CONTROLLED-ECCNS-V1", "m_ids": ["M-ECCN-RULE-RETRIEVE-CONTROLLED-CODESET-V1"]})
    return {"flow_to_drp": flow_to_drp, "mc_to_m1": mc_to_m1}
