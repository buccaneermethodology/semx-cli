from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from semx.phases.manifest import build_manifest
from semx.phases.evidence import extract_evidence
from semx.phases.flow import extract_flows
from semx.phases.m1 import extract_m1_records
from semx.phases.mc import derive_mc_records
from semx.phases.drp import derive_drp_records
from semx.phases.align import build_alignments
from semx.phases.ucs import build_ucs
from semx.phases.lint import run_lint
from semx.phases.repair import run_repair

class SemxRunner:
    def __init__(self, repo_path: Path, out_dir: Path, strict: bool = False) -> None:
        self.repo_path = repo_path.resolve()
        self.out_dir = out_dir.resolve()
        self.strict = strict
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def _dump(self, name: str, obj: Any) -> Path:
        path = self.out_dir / name
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def build(self, auto_repair: bool = False) -> None:
        manifest = build_manifest(self.repo_path)
        self._dump("00_manifest.json", manifest)
        evidence = extract_evidence(self.repo_path, manifest)
        self._dump("01_evidence.json", evidence)
        flows = extract_flows(evidence)
        self._dump("03_flow_records.json", flows)
        m1_records = extract_m1_records(evidence, flows)
        self._dump("05_m1_records.json", m1_records)
        mc_records = derive_mc_records(flows, m1_records)
        self._dump("06_mc_records.json", mc_records)
        drp_records = derive_drp_records(flows, evidence)
        self._dump("07_drp_records.json", drp_records)
        alignments = build_alignments(flows, drp_records, mc_records, m1_records)
        self._dump("08_alignments.json", alignments)
        ucs = build_ucs(manifest, m1_records, mc_records, flows, drp_records, alignments)
        self._dump("09_unified_schema.json", ucs)
        lint_report = run_lint(ucs)
        self._dump("10_lint_report.json", lint_report)
        if self.strict and lint_report["summary"]["status"] == "fail":
            raise SystemExit("Lint failed in strict mode.")
        if auto_repair:
            repair_result = run_repair(ucs=ucs, lint_report=lint_report, mode="full")
            self._dump("11_repair_report.json", repair_result)
            self._dump("12_repaired_schema.json", repair_result["repaired_schema"])

    def lint_only(self, ucs_file: Path, out_file: Path) -> None:
        ucs = json.loads(ucs_file.read_text(encoding="utf-8"))
        lint_report = run_lint(ucs)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(json.dumps(lint_report, ensure_ascii=False, indent=2), encoding="utf-8")

    def repair_only(self, ucs_file: Path, lint_file: Path, out_file: Path) -> None:
        ucs = json.loads(ucs_file.read_text(encoding="utf-8"))
        lint_report = json.loads(lint_file.read_text(encoding="utf-8"))
        repair_result = run_repair(ucs=ucs, lint_report=lint_report, mode="full")
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(json.dumps(repair_result["repaired_schema"], ensure_ascii=False, indent=2), encoding="utf-8")
