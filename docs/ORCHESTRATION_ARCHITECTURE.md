# Orkestrasyon Mimarisi (v2)

## Ana komut

**`/proje_orkestra`** — kullanicidan ara slash komut beklemeden uctan uca dongu.

Eski komutlar korunur; `/proje_workflow` ve `/proje_devam` orkestraya delegasyon yapar.

Tam spesifikasyon: repo kökündeki `agentv2.md`.

## Fazlar

1. bootstrap / resume
2. discovery → architect → design
3. TODO + bagimlilik + dosya sahipligi
4. implementasyon dalgalari (paralel mumkun)
5. dalga sonu: build, lint, typecheck, test
6. gap_scan + completion_audit
7. security + quality gate
8. documentation-release
9. final smoke + teslim

## Otomatik dongu (pseudo)

```
while not verified_complete:
    resume_and_reconcile()
    select_ready_tasks(min_batch=3)
    assign_agents_with_ownership()
    execute_parallel_where_safe()
    integrate_handoffs()
    run_verification_commands()
    reconcile_todo_with_code()
    gap_scan + completion_audit()
    if critical_or_important_gaps: continue
    if gates_fail: create_fix_tasks(); continue
    if all_exit_criteria: break
    else: continue  # durma; kotaya veya blocker'a kadar
```

## Cikis kriterleri

`docs/WORKFLOW_DOD.md` + completion-auditor onayi. Kritik/onemli TODO sifir (veya onayli blocker).

## Agent haritasi

| Faz | Agent |
|-----|--------|
| Discovery | project-discovery-agent |
| Mimari | software-architect-agent |
| Tasarim | ui-ux-design-agent |
| TODO | todo-controller-agent |
| State | progress-state-agent |
| Kod | implementation-agent (+ frontend/backend/db/integration alt rolleri) |
| Test | test-qa-agent |
| Guvenlik/kalite | security-quality-agent |
| Denetim | completion-auditor-agent |
| Dokumantasyon | documentation-release-agent |

Detay: `.cursor/agents/` ve `docs/FILE_OWNERSHIP.md`.
