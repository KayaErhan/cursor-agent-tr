#!/usr/bin/env python3
"""Orkestra v2 yapisal dogrulama."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_AGENTS = [
    "project-discovery-agent.md",
    "todo-controller-agent.md",
    "progress-state-agent.md",
    "software-architect-agent.md",
    "ui-ux-design-agent.md",
    "implementation-agent.md",
    "test-qa-agent.md",
    "security-quality-agent.md",
    "completion-auditor-agent.md",
    "documentation-release-agent.md",
]

REQUIRED_DOCS = [
    "docs/AGENT_CONTRACTS.md",
    "docs/AGENT_HANDOFFS.md",
    "docs/ORCHESTRATION_ARCHITECTURE.md",
    "docs/FILE_OWNERSHIP.md",
    "docs/ORCHESTRA_REPORT.md",
    "docs/DECISIONS.md",
]

STATE_V2_KEYS = {
    "schema_version",
    "run_id",
    "orchestration_mode",
    "project_status",
    "current_step",
    "implementation_wave",
    "completed_steps",
    "active_agents",
    "agent_tasks",
    "file_ownership",
    "blocked_by",
    "retry_counts",
    "last_successful_checkpoint",
    "last_failed_command",
    "resume_from",
    "build_status",
    "lint_status",
    "typecheck_status",
    "test_status",
    "quality_gate_status",
    "security_gate_status",
    "completion_audit_status",
    "wave_quota_min",
    "wave_quota_target",
    "tasks_completed_this_wave",
    "updated_at",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_todo_gorev_ids(errors: list[str]) -> None:
    todo = ROOT / "docs" / "TODO.md"
    if not todo.exists():
        return
    ids = re.findall(r"GOREV-\d{3}", read_text(todo))
    if len(ids) != len(set(ids)):
        errors.append("docs/TODO.md icinde duplicate GOREV-ID var")


def collect_orchestra_errors(errors: list[str]) -> None:
    agents_dir = ROOT / ".cursor" / "agents"
    if not agents_dir.is_dir():
        errors.append("Eksik klasor: .cursor/agents/")
        return

    for name in REQUIRED_AGENTS:
        if not (agents_dir / name).exists():
            errors.append(f"Eksik agent: .cursor/agents/{name}")

    names: list[str] = []
    for p in agents_dir.glob("*.md"):
        text = read_text(p)
        m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
        if m:
            names.append(m.group(1).strip())
        if "description:" not in text:
            errors.append(f"Agent description eksik: {p.name}")
        if len(text.strip()) < 80:
            errors.append(f"Agent aciklama cok kisa (delegasyon yetersiz): {p.name}")

    if len(names) != len(set(names)):
        errors.append("Agent name alanlari benzersiz degil")

    orkestra_path = ROOT / ".cursor" / "commands" / "proje_orkestra.md"
    if not orkestra_path.exists():
        errors.append("Eksik komut: .cursor/commands/proje_orkestra.md")
    else:
        orkestra = read_text(orkestra_path)
        for token in ("Minimum 3", "while not verified_complete", "AGENT_CONTRACTS", "subagent"):
            if token.lower() not in orkestra.lower() and token not in orkestra:
                errors.append(f"proje_orkestra eksik icerik: {token}")

    workflow = read_text(ROOT / ".cursor" / "commands" / "proje_workflow.md")
    if "proje_orkestra" not in workflow:
        errors.append("proje_workflow orkestraya yonlendirme icermiyor")

    devam = read_text(ROOT / ".cursor" / "commands" / "proje_devam.md")
    if "en az 3" not in devam.lower() and "min 3" not in devam.lower():
        errors.append("proje_devam dalga kotasi (min 3) tanimli degil")

    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).exists():
            errors.append(f"Eksik dokuman: {rel}")

    dod = read_text(ROOT / "docs" / "WORKFLOW_DOD.md")
    if "validate_orchestra" not in dod:
        errors.append("WORKFLOW_DOD validate_orchestra referansi eksik")

    state_path = ROOT / "docs" / "WORKFLOW_STATE.md"
    if state_path.exists():
        try:
            data = json.loads(read_text(state_path))
        except json.JSONDecodeError as e:
            errors.append(f"WORKFLOW_STATE.json gecersiz: {e}")
        else:
            missing = STATE_V2_KEYS - set(data.keys())
            if missing:
                errors.append(f"WORKFLOW_STATE v2 alanlari eksik: {sorted(missing)}")
            if data.get("schema_version") != 2:
                errors.append("WORKFLOW_STATE schema_version 2 olmali")
            if data.get("wave_quota_min", 0) < 3:
                errors.append("WORKFLOW_STATE wave_quota_min en az 3 olmali")

    readme = read_text(ROOT / "README.md")
    usage = read_text(ROOT / "docs" / "USAGE.md")
    if "/proje_orkestra" not in readme:
        errors.append("README /proje_orkestra icermiyor")
    if "fallback" not in readme.lower():
        errors.append("README orkestra fallback aciklamasi eksik")
    if "/proje_orkestra" not in usage:
        errors.append("USAGE /proje_orkestra icermiyor")

    rules = read_text(ROOT / ".cursor" / "rules" / "agent.md")
    if "orkestra" not in rules.lower():
        errors.append("agent.md orkestra sefi roli tanimli degil")

    git_up = read_text(ROOT / ".cursor" / "commands" / "git_agent_update.md")
    if ".cursor/agents" not in git_up:
        errors.append("git_agent_update .cursor/agents senkronu eksik")

    check_todo_gorev_ids(errors)


def main() -> int:
    errors: list[str] = []
    collect_orchestra_errors(errors)
    if errors:
        print("Orkestra dogrulama basarisiz:")
        for e in errors:
            print(f"- {e}")
        return 1
    print("Orkestra dogrulama basarili.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
