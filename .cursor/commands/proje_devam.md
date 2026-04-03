# /proje_devam - Workflow Adiminda Derinlesen Devam

Mevcut **workflow adimina** gore eksiklerden devam et. `docs/WORKFLOW_STATE.md` icindeki
`current_step` degerini baz alir ve ayni adimda daha fazla ilerleme saglamayi hedefler.

---

## Isleyis

1. `docs/WORKFLOW_STATE.md` dosyasini oku.
2. `current_step` degerini belirle (ornegin `dev`, `gap_scan`, `continue`, `test`, `quality_gate`, `security`).
3. Adima gore davran:
   - `dev` icin:
     - `docs/TODO.md` uzerindeki `Durum: Devam Ediyor` veya kritik/onemli gorevleri sec.
     - Kod gelistir, ilgili testleri calistir, gorev durumlarini guncelle.
   - `gap_scan` icin:
     - `docs/GAP_REPORT.md` ve `docs/TODO.md` uzerinde tespit edilen eksikleri daha da derinlestir.
   - `continue` icin:
     - Kritik ve onemli eksikleri kapatmaya odaklan.
   - `test` icin:
     - Ek testler ekle, bosluklari doldur, `docs/TEST_REPORT.md`'i guncelle.
   - `quality_gate` icin:
     - `docs/QUALITY_GATE_REPORT.md` icerisindeki zayif kalan alanlari (dusuk puanli kisimlar) iyilestir.
   - `security` icin:
     - `docs/SECURITY_REPORT.md` icindeki kritik/yuksek sorunlari duzeltmeye calis.
4. `docs/TODO.md`, ilgili rapor dosyalari ve gerekirse `docs/STATUS_REPORT.md` uzerinden degisiklikleri isleyerek devam et.

---

## Durdurma Kurali

Sadece su durumlarda dur:
- Coklu mimari karar gerekiyor.
- Kullaniciya ozel bilgi gerekiyor (API key, servis hesabi vb.).
- Kalan eksikler yalnizca dusuk oncelikli iyilestirme niteliginde.

Bunlar disinda otomatik devam et.

---

## Son Mesaj

- Uzerinde calisilan `current_step` adiminda:
  - Kapatilan eksikler
  - Kalan kritik/onemli maddeler
- Genel proje resmi icin:
  - Onerilen sonraki komut (`/proje_workflow`, `/proje_test`, `/proje_kalite_kapisi` veya `/proje_bitir` adima bagli olarak)

