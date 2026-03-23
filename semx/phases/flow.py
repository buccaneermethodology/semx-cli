from __future__ import annotations

def extract_flows(evidence: dict) -> list[dict]:
    flows = []
    symbol_names = {s["name"] for s in evidence["symbols"]}
    if "getControlledEccnNosByEccn" in symbol_names:
        flows.append({
            "flow_id": "FLOW-ECCN-CONTROLLED-JUDGMENT",
            "name": "ECCN受控判定",
            "start": "用户提交一组待判断ECCN",
            "main_steps": [
                "系统获取当前受控规则",
                "对每个ECCN做标准化处理",
                "将标准化ECCN与受控规则逐一比对",
                "收集命中的ECCN"
            ],
            "decision_points": ["ECCN是否超过标准长度", "是否命中任一受控规则"],
            "end": "返回受控ECCN集合",
            "backed_by_mc": [],
            "validation": {"status": "warning", "checks": [{"check_id": "mc_grounding_test", "result": "warning", "reason": "Mc 尚未绑定，将在 derive mc 后完成。"}]},
            "evidence": {"methods": ["getControlledEccnNosByEccn", "resolveEccnNos"], "notes": ["由代码入口方法和判定辅助方法共同支撑。"]},
            "diagnostics": []
        })
    return flows
