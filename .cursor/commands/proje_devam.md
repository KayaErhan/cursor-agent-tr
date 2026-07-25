# /proje_devam - Workflow Adiminda Derinlesen Devam

Mevcut **workflow adimina** gore eksiklerden devam et. **`/proje_orkestra` dalga kotasi** gecerli.

---

## Dalga kotasi (ZORUNLU)

- Ayni `current_step` icinde **en az 3** hazir/kritik gorevi arka arkaya isle (uygunsa 5).
- **Tek gorev sonrasi durma** ve "devam edeyim mi?" sorma.
- Durdur: blocker, 3 retry sonrasi `Bloke`, veya hazir gorev kalmadi.

`docs/AGENT_CONTRACTS.md` | State: `docs/WORKFLOW_STATE.md` (`tasks_completed_this_wave` guncelle).

---

## Isleyis

1. Resume: `WORKFLOW_STATE`, `TODO`, git status, son raporlar.
2. `current_step` (dev, gap_scan, continue, test, quality_gate, security):
   - **dev / continue:** implementation-agent; bagimlilik sirasi; dosya sahipligi
   - **gap_scan:** `proje_eksik_tara.md`
   - **test:** `proje_test.md`
   - **quality_gate / security:** ilgili komut dosyalari
3. Her gorev: kod + test + TODO kanit satiri.
4. Dalga sonu: build/lint/test + todo mutabakati.

---

## Durdurma

Yalnizca: mimari coklu secim, secret/API key, odeme, geri donusuz risk, dusuk oncelik disi tum kritik/onemli bitti.

---

## Son mesaj

- Kapatilan gorev **sayisi** (dalga)
- Kalan kritik/onemli
- Sonraki adim otomatik (`/proje_orkestra` veya ayni komut tekrar — yeni slash bekleme)
