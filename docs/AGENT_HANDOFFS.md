# Agent Handoff Sablonu

Subagent ciktisi bu yapida (son handoff dosyaya eklenebilir veya sohbette ozetlenir):

```markdown
## Handoff — {agent-adı} — {tarih}

- **Gorev ID:** GOREV-xxx, ...
- **Incelenen:** path/liste
- **Degistirilen:** path/liste
- **Yapilan:** madde madde
- **Komutlar:** calistirilan komutlar + exit code
- **Test:** sonuc ozeti
- **Acik sorunlar:** ...
- **Yeni gorev onerileri:** ...
- **Sonraki agent:** oneri
- **Durum:** basarili | kismi | bloke | basarisiz
```

Ana orkestrator handoff'u dogrulamadan `[x]` / `Tamamlandi` yazamaz.
