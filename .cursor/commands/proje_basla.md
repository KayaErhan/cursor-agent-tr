# /proje_basla — Projeyi Sıfırdan Başlat

Kullanıcının sağladığı proje dökümanını al ve aşağıdaki adımları **sırayla, kullanıcıdan ek komut beklemeden** otomatik olarak yürüt.

---

## Aşama 1 — Döküman Analizi

Dökümanı derinlemesine analiz et ve şunları çıkar:

- Projenin amacı ve hedef kitlesi
- Teknik gereksinimler (dil, framework, veritabanı, vb.)
- Kapsam ve özellik listesi
- Potansiyel riskler ve teknik zorluklar

Analiz özetini `/docs/ANALYSIS.md` dosyasına yaz ve kullanıcıya göster.

---

## Aşama 2 — Akış Şeması

Proje mimarisini ve bileşenler arası veri akışını gösteren bir akış şeması oluştur:

- Sistem bileşenlerini tanımla (frontend, backend, veritabanı, servisler)
- Veri akışını ve bileşenler arası ilişkileri göster
- Kullanıcı yolculuklarını (user flows) ASCII veya Mermaid formatında çiz
- `/docs/FLOWCHART.md` dosyasına kaydet

---

## Aşama 3 — İş Planı & Yapılacaklar Listesi

Projede yapılacak **tüm görevleri** öncelik sırasına göre listele.

Her görev için şu bilgileri içer:

```
[ ] GÖREV-001 | Görev Adı | Bağımlılık: YOK | Öncelik: YÜKSEK
[ ] GÖREV-002 | Görev Adı | Bağımlılık: GÖREV-001 | Öncelik: YÜKSEK
```

- Listeyi `/docs/TODO.md` dosyasına kaydet.
- Görevleri kategorilere ayır: Altyapı, Backend, Frontend, Admin Paneli, Test, Dokümantasyon.

---

## Aşama 4 — Otomatik Geliştirme Döngüsü

Her görevi sırayla işle:

1. Görevi tamamla.
2. `/docs/TODO.md` dosyasında ilgili satırı `[x]` olarak işaretle.
3. Bir sonraki göreve geç.

**Bağımlılık kontrolü:** İki veya daha fazla görev birbiriyle ilişkiliyse, ilgili görevler tamamlandıktan sonra **uyum kontrolü ve entegrasyon testi** yap; testler geçerse devam et.

**Tasarım kuralı:** Tüm arayüzlerde **Tailwind CSS** kullan. Yüksek UX kalitesi zorunludur. Her projede tam işlevsel **admin paneli** oluştur (`/admin` rotası).

---

## Aşama 5 — Genel Analiz & Ek Öneriler

Tüm görevler tamamlandıktan sonra:

- Projenin genel durumunu değerlendiren analiz raporu oluştur → `/docs/ANALYSIS.md` güncelle.
- Güvenlik, performans, ölçeklenebilirlik açısından eksik alanları tespit et.
- Her öneri için değerlendirme yap:
  - **Gerçekten gerekli mi?** → Evet ise TODO listesine ekle ve otomatik geliştir.
  - **Gerekli değil mi?** → Rapora not düş, uygulama.

---

## Aşama 6 — Yapılandırma Arayüzü

Başka yapılacak görev kalmadığında, kullanıcının sisteme özel bilgileri girebileceği bir yapılandırma ekranı oluştur.

Ekran şunları içermeli (projeye göre özelleştir):

- Veritabanı bağlantı bilgileri (host, port, kullanıcı adı, şifre, db adı)
- SMTP / e-posta yapılandırması (host, port, kullanıcı, şifre)
- API anahtarları veya diğer ortam değişkenleri

Girilen bilgiler `/config/.env` veya `.env` dosyasına güvenli şekilde yazılmalı.

---

## Aşama 7 — Son Dokümantasyon

- `/README.md` → Proje özeti, kurulum adımları, hızlı başlangıç, katkı kılavuzu
- `/docs/USAGE.md` → Detaylı kullanım kılavuzu, ekran açıklamaları, örnek senaryolar
- `/CHANGELOG.md` → Tüm aşamalarda yapılan değişikliklerin geçmişi

---

**Başlamak için dökümanı analiz et ve Aşama 1'i uygula.**
