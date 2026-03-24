# /proje_eksik_tara - Eksik ve Oneri Taramasi

Proje tamamlandiktan veya ara asamada, kodu ve dokumantasyonu tarayip eksikleri otomatik listeler.

---

## Tarama Alanlari

- Fonksiyonel eksikler (ozellik tam mi?)
- TODO uyumsuzluklari (kod var ama TODO isaretlenmemis / tersi)
- Test bosluklari
- Guvenlik aciklari
- Performans iyilestirmeleri
- UI/UX ve erisilebilirlik eksikleri
- Dokumantasyon tutarsizliklari
- Tasarim kalite checklist'i:
  - Sol menulu admin panel var mi?
  - Tema secimleri (dark/soft-dark/light/hepsi) calisiyor mu?
  - Dashboard KPI + en az 3 grafik var mi?
  - Bildirim ve email/mesaj alanlari var mi?
  - Ikon ve renk sistemi yeterince zengin mi?
  - Site tarafi (varsa) premium ve gorsel olarak dolu mu?

---

## Cikti Kurallari

1. Bulgulari `/docs/GAP_REPORT.md` dosyasina yaz.
2. Her bulgu icin:
   - ID
   - Siddet (Kritik / Onemli / Iyilestirme)
   - Etki
   - Onerilen cozum
3. Cozulebilir maddeleri otomatik olarak `/docs/TODO.md` dosyasina gorev olarak ekle.

---

## Son Mesaj

Kullaniciya su sekilde raporla:
- Toplam bulgu
- Kritik bulgu sayisi
- TODO'ya eklenen yeni gorev sayisi
- Sonraki komut onerisi: `/proje_devam`
