# /proje_orkestra — Orkestra Agent Sistemi v2 (Ana Komut)

**Tek komutla** projeyi planlanmis fazlarda ilerletir; TODO maddelerini **dalga dalga** isler; tek-iki gorev yapip **durmaz**.

Mimari: `docs/ORCHESTRATION_ARCHITECTURE.md` | Sozlesmeler: `docs/AGENT_CONTRACTS.md`

---

## Kim cagirir

Ana agent (Orkestra Sefi) bu komutu alinca asagiyi **ayni oturumda** uygular.

### Subagent cagirma (Cursor native)

1. `.cursor/agents/` altindaki rol dosyasini oku (frontmatter `name` + `description`).
2. Uygun rol icin **Task araci** ile subagent baslat (or. `project-discovery-agent`, `implementation-agent`).
3. Paralel: birbirinden bagimsiz modul gorevlerinde birden fazla Task; **ayni dosyada paralel yazma yok**.
4. Subagent yoksa veya Task basarisiz: `WORKFLOW_STATE.orchestration_mode = "fallback"`; ayni rol talimatini ana agent sirayla uygular.

Native subagent yoksa `orchestration_mode: fallback` ile ayni rolleri simule et.

---

## 0) Resume (her cagrida zorunlu)

1. `git status` — dogrulanmamis degisiklikler
2. `docs/WORKFLOW_STATE.md` (schema v2)
3. `docs/TODO.md` — hazir / devam / kritik sayilari
4. Son `TEST`, `GAP`, `QUALITY`, `SECURITY` raporlari
5. Kod vs TODO mutabakati
6. `progress-state-agent` mantigi: `resume_from` guncelle

---

## 1) Dalga kotasi (KRITIK — tek madde durma yasagi)

Implementasyon / `continue` fazinda:

- **Minimum 3**, uygunsa **5** hazir TODO gorevini **aynı dalgada** isle.
- Bir gorev bittikten sonra kullaniciya "devam edeyim mi?" sorma.
- Durdurma yalnizca:
  - Faz DoD tamamlandi
  - Dalga kotasi doldu **ve** sonraki hazir gorev yok
  - Gercek blocker (veri kaybi, odeme, secret, celisen urun karari)
  - Ayni hata 3 retry sonrasi `Bloke`

Her dalga sonu: build/lint/typecheck/test (projede tanimliysa) + `todo-controller-agent` mutabakat.

---

## 2) Faz sirasi

`analysis` → `design` → `dev` → `gap_scan` → `continue` → `test` → `quality_gate` → `security` → `finish`

| Faz | Subagent / komut mantigi |
|-----|---------------------------|
| analysis | project-discovery-agent + `proje_incele.md` |
| design | ui-ux-design-agent + `proje_tasarim.md` |
| dev | software-architect-agent (plan) + implementation-agent dalgalari |
| gap_scan | `proje_eksik_tara.md` + completion-auditor on tarama |
| continue | implementation-agent; **dalga kotasi 3–5** |
| test | test-qa-agent + `proje_test.md` |
| quality_gate | security-quality-agent + `proje_kalite_kapisi.md` |
| security | `proje_guvenlik_tara.md` |
| finish | completion-auditor onay → documentation-release-agent + `proje_bitir.md` |

DoD: `docs/WORKFLOW_DOD.md`. State guncelleme: `progress-state-agent`.

---

## 3) Otomatik tamamlama dongusu

```
while not verified_complete:
    resume_and_reconcile()
    select_ready_tasks(min=3)
    assign_file_ownership()
    run_subagents_parallel_if_safe()
    integrate_handoffs()
    verify_build_test()
    reconcile_todo()
    gap_scan + completion_audit()
    if critical_or_important_gaps: add_todo; continue
    if gates_fail: fix_tasks; continue
    if exit_criteria: break
    else: continue   # durma
```

Cikis: kritik/onemli TODO sifir (veya onayli blocker), testler, auditor + kalite + guvenlik kapilari — `docs/ORCHESTRATION_ARCHITECTURE.md`.

---

## 4) Paralel calisma

- Bagimsiz modullerde implementation subagent'lari paralel.
- Ayni dosyada eszamanli yazma yok — `docs/FILE_OWNERSHIP.md`.
- Merkezi TODO/state yalnizca todo-controller / progress-state / ana sef.

---

## 5) Handoff

Her subagent: `docs/AGENT_HANDOFFS.md`. Ana sef handoff dogrulamadan `Tamamlandi` isaretlemez.

---

## 6) Cikti

- `docs/WORKFLOW_STATE.md` guncel
- `docs/ORCHESTRA_REPORT.md` kisa dalga ozeti
- Kullaniciya: kapatilan gorev sayisi, kalan kritik, sonraki otomatik adim (yeni slash bekleme)

---

## Eski komutlar

- `/proje_workflow` → bu komutla ayni niyet (orkestraya yonlendir)
- `/proje_devam` → ayni fazda **dalga kotasi** ile derinles
