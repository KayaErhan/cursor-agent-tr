# /proje_workflow - n8n Benzeri Super Workflow Komutu

> **v2:** Bu komut **`/proje_orkestra` ile ayni niyetle** calisir. Yeni projelerde `/proje_orkestra` tercih edin.

Kullanici `/proje_workflow` yazdiginda **`.cursor/commands/proje_orkestra.md`** kurallarini uygula:
- Resume + otomatik dongu
- Dalga kotasi (min 3 TODO)
- Subagent delegasyonu veya fallback

Detay: `docs/ORCHESTRATION_ARCHITECTURE.md`.

---

## Geriye donuk ozet

1. `docs/WORKFLOW_STATE.md` oku (schema v2).
2. `current_step` icin ilgili komut/subagent (asagidaki tablo).
3. DoD: `docs/WORKFLOW_DOD.md`. Faz bitmeden durma; kotaya kadar devam.

| Faz | Referans |
|-----|----------|
| analysis | `proje_incele.md` / project-discovery-agent |
| design | `proje_tasarim.md` / ui-ux-design-agent |
| dev, continue | implementation-agent; **dalga min 3 gorev** |
| gap_scan | `proje_eksik_tara.md` |
| test | `proje_test.md` / test-qa-agent |
| quality_gate | `proje_kalite_kapisi.md` |
| security | `proje_guvenlik_tara.md` |
| finish | completion-auditor + `proje_bitir.md` |

`/proje_devam`: ayni fazda dalga kotasi ile derinles.
