# /proje_test — Uyum Kontrolü & Kapsamlı Test

Şu ana kadar tamamlanan tüm bileşenler üzerinde kapsamlı test yürüt ve sonuçları raporla.

---

## Test Kategorileri

### 1. Birim Testleri (Unit Tests)
- Her fonksiyon ve bileşeni bağımsız olarak test et.
- Edge case'leri ve hata durumlarını kontrol et.

### 2. Entegrasyon Testleri
- Tüm modüllerin birbirleriyle uyumunu doğrula.
- API endpoint'lerinin doğru çalıştığını test et.
- Veritabanı bağlantılarını ve CRUD işlemlerini kontrol et.

### 3. UI/UX Kontrolü
- Tüm sayfaların responsive olduğunu doğrula.
- Form validasyonlarını test et.
- Erişilebilirlik (accessibility) standartlarını kontrol et.
- Tailwind class'larının doğru uygulandığını doğrula.

### 4. Güvenlik Kontrolü
- Input validasyonu ve sanitization kontrolü.
- Authentication/Authorization akışlarını test et.
- SQL injection ve XSS açıklarını kontrol et.

### 5. Admin Paneli Testi
- Tüm admin panel özelliklerinin çalıştığını doğrula.
- Yetki kontrolleri (authorization) doğru mu?
- Raporlama ve CRUD işlemleri çalışıyor mu?

---

## Hata Yönetimi

Bulunan her hata için:
1. Hatayı kaydet (konum, açıklama, şiddet)
2. Şiddetine göre sınıflandır: 🔴 Kritik | 🟡 Orta | 🟢 Düşük
3. Kritik ve orta hatalar için **otomatik düzeltme** yap.
4. Düzeltme sonrası testi tekrarla.
5. `/docs/TODO.md` içindeki ilgili maddedeki `[x]` işaretini güncelle.

---

## Çıktı

Test sonuçlarını `/docs/TEST_REPORT.md` dosyasına kaydet:

```markdown
# Test Raporu — [Tarih]

## Özet
- Toplam Test: XX
- Geçen: XX ✅
- Başarısız: XX ❌
- Atlanan: XX ⏭️

## Hatalar
...

## Öneriler
...
```
