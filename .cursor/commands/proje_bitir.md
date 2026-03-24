# /proje_bitir — Projeyi Sonlandır & Teslim Et

Tüm geliştirme tamamlandıktan sonra bu komutu çalıştır. Projeyi sonlandır, eksikleri gider ve teslime hazır hale getir.

---

## Aşama 1 — Final Analizi

- `/docs/TODO.md` dosyasını oku — tüm maddeler `[x]` mi?
- Eksik madde varsa önce tamamla.
- Genel proje kalitesini değerlendir.
- `/docs/ANALYSIS.md` dosyasını güncelle.

---

## Aşama 2 — Ek Öneri Değerlendirmesi

Şu alanlarda projeyi incele ve eksik bulunanları tespit et:

| Alan | Kontrol Noktaları |
|---|---|
| Güvenlik | HTTPS, rate limiting, input sanitization, auth |
| Performans | Caching, lazy loading, query optimizasyonu |
| Ölçeklenebilirlik | Modüler yapı, API versiyonlama |
| SEO / Erişilebilirlik | Meta tags, ARIA labels, semantic HTML |
| Hata Yönetimi | Global error handler, logging, monitoring |

Her eksiklik için:
- **Gerçekten gerekli mi?** → Evet → `/docs/TODO.md`'ye ekle ve otomatik geliştir.
- **Gerekli değil mi?** → `/docs/ANALYSIS.md`'ye not düş.

---

## Aşama 3 — Yapılandırma Arayüzü

Kullanıcının sisteme özel bilgileri girebileceği bir **Config Setup Ekranı** oluştur.

Ekran `/setup` veya `/config` rotasında açılmalı ve şunları içermeli:

### Veritabanı Ayarları
- Host, Port, Veritabanı Adı, Kullanıcı Adı, Şifre
- Bağlantı test butonu

### E-posta (SMTP) Ayarları
- Host, Port, Kullanıcı, Şifre, Gönderici Adı
- Test e-postası gönder butonu

### Uygulama Ayarları
- Uygulama adı, URL, timezone, dil
- Diğer projeye özgü ortam değişkenleri

Kaydet butonuna basıldığında bilgiler `.env` ve `/config/settings.json` dosyalarına yazılmalı.

---

## Aşama 4 — Son Dokümantasyon

Şu dosyaların eksiksiz ve güncel olduğunu doğrula:

- **`/README.md`** → Proje adı, açıklama, özellikler, kurulum, kullanım, katkı kılavuzu, lisans
- **`/docs/USAGE.md`** → Adım adım kullanım, her ekranın açıklaması, örnek senaryolar, sık sorulan sorular
- **`/docs/FLOWCHART.md`** → Güncel sistem mimarisi ve akış şeması
- **`/docs/ANALYSIS.md`** → Final analiz raporu
- **`/docs/TEST_REPORT.md`** → Son test sonuçları
- **`/CHANGELOG.md`** → Tüm versiyonlar ve değişiklikler

---

## Aşama 5 — Teslim Özeti

Her şey tamamlandığında kullanıcıya şu formatta özet sun:

```
✅ Proje teslime hazır!

📦 Toplam Dosya     : XX
✅ Tamamlanan Görev : XX / XX
🧪 Test Sonucu      : XX geçti, XX başarısız
📄 Dokümantasyon    : Tamamlandı
⚙️  Config Ekranı   : /setup adresinde hazır

🚀 Kurulum için: README.md → "Kurulum" bölümüne bakın.
```
