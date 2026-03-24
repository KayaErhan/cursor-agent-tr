# /proje_sifirla — Projeyi Temizle & Sıfırdan Başlamaya Hazırla

Bu komut mevcut projeyi arşivler ve temiz bir başlangıç için hazırlar.

---

## Adımlar

### 1. Mevcut Durumu Arşivle
- `/docs/` klasörünü `/archive/[tarih]/docs/` olarak kopyala.
- `/docs/TODO.md` ve `/docs/ANALYSIS.md` dosyalarının yedeğini al.

### 2. Çalışma Dosyalarını Temizle
- `/docs/TODO.md` → Boşalt, sadece başlık bırak.
- `/docs/ANALYSIS.md` → Boşalt.
- `/docs/TEST_REPORT.md` → Boşalt.
- `/docs/STATUS_REPORT.md` → Boşalt.

### 3. Kullanıcıyı Bilgilendir
Temizlik tamamlandığında:
> "Proje sıfırlandı. Arşiv `/archive/[tarih]/` dizinine kaydedildi. Yeni projeye başlamak için dökümanı ver ve `/proje_basla` komutunu çalıştır."

---

⚠️ **Uyarı:** Bu komut mevcut ilerlemeyi siler. Kullanmadan önce yedek aldığından emin ol.
