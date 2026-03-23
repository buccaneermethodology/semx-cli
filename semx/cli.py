from __future__ import annotations
from pathlib import Path
import typer
from semx.core.runner import SemxRunner

app = typer.Typer(help="semx - Semantic Stack Extractor CLI")

@app.command()
def build(repo: Path, out: Path = Path(".semx/latest"), strict: bool = False, auto_repair: bool = False) -> None:
    runner = SemxRunner(repo_path=repo, out_dir=out, strict=strict)
    runner.build(auto_repair=auto_repair)

@app.command()
def lint(ucs_file: Path = Path(".semx/latest/09_unified_schema.json"), out: Path = Path(".semx/latest/10_lint_report.json")) -> None:
    runner = SemxRunner(repo_path=Path("."), out_dir=Path(".semx/latest"))
    runner.lint_only(ucs_file=ucs_file, out_file=out)

@app.command()
def repair(
    ucs_file: Path = Path(".semx/latest/09_unified_schema.json"),
    lint_file: Path = Path(".semx/latest/10_lint_report.json"),
    out: Path = Path(".semx/latest/12_repaired_schema.json"),
) -> None:
    runner = SemxRunner(repo_path=Path("."), out_dir=Path(".semx/latest"))
    runner.repair_only(ucs_file=ucs_file, lint_file=lint_file, out_file=out)

if __name__ == "__main__":
    app()
