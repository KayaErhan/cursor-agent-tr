# Dosya Sahipligi

Orkestra calisirken `docs/WORKFLOW_STATE.md` icindeki `file_ownership` guncellenir.

## Kurallar

| Dosya / alan | Yazar |
|--------------|--------|
| `docs/TODO.md` | todo-controller-agent veya ana orkestrator |
| `docs/WORKFLOW_STATE.md` | progress-state-agent veya ana orkestrator |
| `docs/STATUS_REPORT.md`, `docs/ORCHESTRA_REPORT.md` | progress-state-agent / documentation-release-agent |
| `src/**`, `app/**` vb. | implementation-agent (atanan modul) |
| Raporlar (`GAP`, `TEST`, `SECURITY`, `QUALITY`) | ilgili uzman agent |

- Paralel implementation: farkli modul/dizin; **ayni dosya yok**.
- Merge/onay: ana orkestrator.

## Ornek state parcasi

```json
"file_ownership": {
  "src/app/admin/**": "implementation-agent-frontend",
  "src/server/**": "implementation-agent-backend"
}
```
