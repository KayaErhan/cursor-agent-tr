#!/usr/bin/env python3
"""
Repo-level quality checks for command/docs consistency.

Covers:
- TODO-011 command/docs consistency
- TODO-012 placeholder & local link checks
- TODO-014 TODO format/schema checks
- TODO-015 README/USAGE <-> command contract checks
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_file_exists(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Eksik dosya: {path.relative_to(ROOT)}")


def check_no_placeholders(md_files: list[Path], errors: list[str]) -> None:
    placeholder = "KULLANICI_ADIN"
    for file in md_files:
        text = read_text(file)
        if placeholder in text:
            errors.append(f"Placeholder bulundu ({placeholder}): {file.relative_to(ROOT)}")


def check_local_links(md_files: list[Path], errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for file in md_files:
        text = read_text(file)
        for target in link_re.findall(text):
            t = target.strip()
            if not t or t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = (file.parent / t).resolve() if not t.startswith("/") else (ROOT / t.lstrip("/")).resolve()
            if not local.exists():
                errors.append(f"Kirik lokal link: {file.relative_to(ROOT)} -> {t}")


def check_command_refs(errors: list[str]) -> None:
    command_dir = ROOT / ".cursor" / "commands"
    readme = read_text(ROOT / "README.md")
    usage = read_text(ROOT / "docs" / "USAGE.md")
    refs = set(re.findall(r"/(proje_[a-z_]+)", readme + "\n" + usage))
    for ref in sorted(refs):
        p = command_dir / f"{ref}.md"
        if not p.exists():
            errors.append(f"Referans verilen komut dosyasi yok: .cursor/commands/{ref}.md")


def check_canonical_flow(errors: list[str]) -> None:
    expected = [
        "/proje_incele",
        "Dil/Framework + SQL",
        "/proje_tasarim",
        "/proje_basla",
        "/proje_eksik_tara",
        "/proje_devam",
        "/proje_test",
        "/proje_kalite_kapisi",
        "/proje_guvenlik_tara",
        "/proje_bitir",
    ]
    targets = [
        ROOT / "README.md",
        ROOT / "docs" / "USAGE.md",
        ROOT / ".cursor" / "commands" / "proje_basla.md",
    ]
    for file in targets:
        text = read_text(file)
        pos = -1
        for step in expected:
            i = text.find(step)
            if i == -1:
                errors.append(f"Kanonik akis adimi eksik: {file.relative_to(ROOT)} -> {step}")
                break
            if i < pos:
                errors.append(f"Kanonik akis sirasi bozuk: {file.relative_to(ROOT)} -> {step}")
                break
            pos = i


def check_todo_schema(errors: list[str]) -> None:
    todo = ROOT / "docs" / "TODO.md"
    text = read_text(todo)
    if "## 🚀 DevOps" not in text:
        errors.append("docs/TODO.md icinde DevOps bolumu eksik")

    task_re = re.compile(
        r"^\[(?: |x)\] GOREV-\d{3} \| .+ \| Bagimlilik: .+ \| Oncelik: (?:Yuksek|Orta|Dusuk) \| Durum: (?:Bekliyor|Devam Ediyor|Tamamlandi)$"
    )

    task_lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("[")]
    if not task_lines:
        errors.append("docs/TODO.md icinde gorev satiri bulunamadi")
        return

    for ln in task_lines:
        if not task_re.match(ln):
            errors.append(f"TODO satiri format disi: {ln}")


def check_contract_claims(errors: list[str]) -> None:
    bitir = read_text(ROOT / ".cursor" / "commands" / "proje_bitir.md")
    required = ["/setup", "/config", ".env", "Zorunlu"]
    for token in required:
        if token not in bitir:
            errors.append(f"proje_bitir sozlesme eksigi: '{token}' ifadesi yok")


def main() -> int:
    errors: list[str] = []

    critical_files = [
        ROOT / "README.md",
        ROOT / "docs" / "USAGE.md",
        ROOT / "docs" / "TODO.md",
        ROOT / ".cursor" / "commands" / "proje_basla.md",
        ROOT / ".cursor" / "commands" / "proje_bitir.md",
    ]
    for f in critical_files:
        check_file_exists(f, errors)
    if errors:
        for e in errors:
            print(f"[HATA] {e}")
        return 1

    md_files = list(ROOT.rglob("*.md"))
    check_no_placeholders(md_files, errors)
    check_local_links(md_files, errors)
    check_command_refs(errors)
    check_canonical_flow(errors)
    check_todo_schema(errors)
    check_contract_claims(errors)

    if errors:
        print("Kalite dogrulama basarisiz:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Kalite dogrulama basarili: tum kontroller gecti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
