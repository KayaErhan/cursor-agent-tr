# Agent Sozlesmeleri (Orkestra v2)

Ortak kurallar; her `.cursor/agents/*.md` dosyasi buraya referans verir.

## Handoff (zorunlu cikti)

Her subagent gorev sonunda ana orkestratore `docs/AGENT_HANDOFFS.md` formatinda rapor verir.

## TODO tek kaynak

- Gorevler yalnizca `docs/TODO.md` icindedir.
- State dosyasina TODO kopyasi yazma.
- Tamamlama: kod + kabul kriteri + dogrulama komutu + kanit satiri (`Tamamlanma kaniti: ...`).

## Gorev satiri (v2)

```
[ ] GOREV-XXX | Baslik | Agent: implementation-agent | Oncelik: Yuksek | Durum: Bekliyor | Bagimlilik: yok
```

Durumlar: `Bekliyor`, `Hazir`, `Devam Ediyor`, `Incelemede`, `Test Ediliyor`, `Bloke`, `Basarisiz`, `Tamamlandi`.

## Genisletilmis gorev alanlari (proje TODO'su)

Her gorev icin mumkunse ayri satir veya alt madde:

- Kabul kriterleri
- Dogrulama komutu
- Tamamlanma kaniti
- Blocker / retry sayisi

Tamamlama kosulu: kod + kriter + dogrulama + test + denetim (`docs/AGENT_HANDOFFS.md`).

## Dalga kotasi (tek-iki madde durma yasagi)

Ana orkestrator ve `/proje_devam` / `/proje_orkestra`:

- **Devam / implementasyon dalgasinda** en az **3** hazir gorevi isle (bagimlilik ve dosya sahipligi izin veriyorsa **5**'e kadar).
- Tek gorev bitince **durma**; dalga kotasi veya faz DoD'u veya gercek blocker olana kadar devam et.
- Her dalga sonu: build/lint/test (projede varsa) + TODO-kod mutabakati.

## Dosya sahipligi

- Ayni dosyada eszamanli iki yazma agent'i yok.
- Merkezi dosyalar (`TODO.md`, `WORKFLOW_STATE.md`, `STATUS_REPORT.md`) yalnizca `todo-controller-agent`, `progress-state-agent` veya ana orkestrator tarafindan guncellenir.

## Retry

- Ayni hata icin en fazla **3** otomatik duzeltme; sonra `Bloke` + blocker listesi.

## Fallback

Native subagent yoksa ana agent ayni rolleri sirayla simule eder; `WORKFLOW_STATE.orchestration_mode`: `native` | `fallback`.
