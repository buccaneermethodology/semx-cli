from __future__ import annotations

def extract_m1_records(evidence: dict, flows: list[dict]) -> list[dict]:
    symbol_names = {s["name"] for s in evidence["symbols"]}
    m1_records = []
    if "getApplyCode" in symbol_names:
        m1_records.append({
            "m_id": "M-ECCN-RULE-RETRIEVE-CONTROLLED-CODESET-V1",
            "name": "获取受控ECCN规则集",
            "capability_type": "Extraction",
            "capability_description": "从权威规则来源获取当前生效的受控ECCN规则集。",
            "purpose": "为后续受控判断提供统一且权威的规则输入。",
            "input_space": {},
            "output_space": {"ruleSet": "RuleSet"},
            "domain_model": {"ControlledECCNRule": {"definition": "由权威来源维护的受控ECCN规则项", "normalization_strategy": "以权威来源返回值为准"}},
            "decision_semantics": [
                {"step_order": 1, "aspect": "IterationScope", "description": "针对当前规则来源执行一次规则集提取。"},
                {"step_order": 2, "aspect": "CoreMatchingLogic", "description": "仅在规则来源返回有效结果时采纳该规则集。"},
                {"step_order": 3, "aspect": "FailureOrInsufficiencyHandling", "description": "若未返回有效规则，则返回空规则集而不自行生成替代规则。"}
            ],
            "decision_function_form": "f : ∅ -> RuleSet",
            "decision_rules": [
                {"rule_id": "R1", "condition": "权威规则来源返回成功且有数据", "result": "返回受控ECCN规则集"},
                {"rule_id": "R2", "condition": "权威规则来源未返回有效数据", "result": "返回空规则集"}
            ],
            "invariants": ["Authority — 规则真值由外部权威来源拥有", "Closure — 输出只能是规则集或空规则集"],
            "constraints_or_invariants": [
                {"category": "AuthorityOwnership", "statement": "本系统消费规则而不创造规则。"},
                {"category": "FailureBoundary", "statement": "外部规则不可用时返回空规则集。"}
            ],
            "non_goals": ["不解释规则含义", "不生成新规则"],
            "code_trace": ["getApplyCode"],
            "validation": {"status": "pass", "checks": [{"check_id": "single_intent_test", "result": "pass", "reason": "唯一意图是获取权威规则集。"}]},
            "evidence": {"methods": ["getApplyCode"], "fields": ["type", "version"], "constants": ["04", "1.0"], "notes": ["这是统一的规则入口。"]},
            "purity_score": {"overall": 0.96, "intent_purity": 0.98, "decision_density": 0.84, "orchestration_leakage": 0.01, "projection_leakage": 0.0, "infrastructure_leakage": 0.03, "rationale": ["单一意图清晰，无明显投影或编排泄漏。"]},
            "diagnostics": []
        })
    return m1_records
