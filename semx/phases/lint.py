from __future__ import annotations
from semx.linter.engine import lint_ucs

def run_lint(ucs: dict) -> dict:
    return lint_ucs(ucs)
