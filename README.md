# 🤖 Cursor Otonom Geliştirme Ajanı

> Cursor IDE için tam otomatik yazılım geliştirme sistemi. Proje dökümanını ver, gerisini ajan halleder.

[![Cursor IDE](https://img.shields.io/badge/Cursor-IDE-blue?style=flat-square)](https://cursor.sh)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=flat-square)](https://tailwindcss.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## ✨ Ne Yapar?

Cursor IDE'ye proje dökümanını verdiğinde, ajan otomatik olarak:

1. 📋 **Dökümanı analiz eder** — Kapsam, teknik gereksinimler, riskler
2. 🗺️ **Akış şeması çıkarır** — Sistem mimarisi ve bileşen diyagramları
3. 📝 **İş planı oluşturur** — Önceliklendirilmiş, bağımlılıklı görev listesi
4. ⚙️ **Otomatik geliştirir** — Tamamlanan görevleri işaretleyerek ilerler
5. 🧪 **Test yapar** — Entegrasyon ve uyum kontrolleri
6. 📊 **Analiz raporu üretir** — Ek öneriler ve iyileştirmeler
7. ⚙️ **Config ekranı oluşturur** — Veritabanı, SMTP vb. ayarlar
8. 📚 **Dokümantasyon yazar** — README, kullanım kılavuzu, changelog

**Her projede zorunlu olarak şunları üretir:**
- ✅ Tam işlevsel **Admin Paneli** (`/admin`)
- ✅ **Tailwind CSS** ile yüksek kaliteli, responsive arayüzler
- ✅ **Kullanım kılavuzu** ve **README** (her aşamada güncellenir)
- ✅ Sol menülü admin panel, bildirim/email alanı ve detaylı dashboard grafikleri
- ✅ Gerekli durumlarda `lucide-react`, `recharts`, `framer-motion` ile zengin UI deneyimi

---

## 🚀 Kurulum

### Gereksinimler

- [Cursor IDE](https://cursor.sh) v0.40 veya üzeri
- Git

### Adım 1 — Projeyi İndir

```bash
git clone https://github.com/KULLANICI_ADIN/cursor-agent-tr.git
cd cursor-agent-tr
```

### Adım 2 — Cursor'a Kopyala

**Seçenek A — Mevcut projenize ekleyin:**
```bash
# Proje klasörünüze kopyalayın
cp -r cursor-agent-tr/.cursor /senin-projen/
```

**Seçenek B — Tüm projelerinizde kullanın (Global):**
```bash
# macOS / Linux
cp -r .cursor/commands ~/.cursor/commands
cp -r .cursor/rules ~/.cursor/rules

# Windows (PowerShell)
Copy-Item -Recurse .cursor\commands $env:USERPROFILE\.cursor\commands
Copy-Item -Recurse .cursor\rules $env:USERPROFILE\.cursor\rules
```

### Adım 3 — Cursor'u Açın

Cursor IDE'yi açın ve chat penceresini başlatın (`Ctrl+L` / `Cmd+L`).

---

## 📖 Kullanım

### Komut Listesi

| Komut | Açıklama |
|---|---|
| `/proje_incele` | Dökümanı analiz eder, akış şeması çıkarır, risk raporu hazırlar |
| `/proje_basla` | Baştan sona tam otomatik geliştirme döngüsünü başlatır |
| `/proje_durum` | Anlık ilerlemeyi ve todo listesini gösterir |
| `/proje_test` | Tüm bileşenleri test eder, hataları otomatik düzeltir |
| `/proje_bitir` | Projeyi sonlandırır, config ekranı ve son dokümantasyonu oluşturur |
| `/proje_sifirla` | Mevcut çalışmayı arşivler, yeni proje için temizler |
| `/proje_eksik_tara` | Proje eksiklerini ve iyileştirme önerilerini otomatik tarar |
| `/proje_devam` | Taranan eksiklerden otomatik devam eder ve uygular |
| `/proje_tasarim` | Kurumsal/standart profil + dark/soft-dark/light/hepsi tema seçimi yapar |
| `/proje_kalite_kapisi` | Kurumsal kalite kapılarını puanlayarak geçiş kararı verir |
| `/proje_guvenlik_tara` | Güvenlik ve uyum taraması yapar, kritikleri raporlar |

### Temel Kullanım Akışı

```
1. Cursor'u aç → Chat'i başlat (Ctrl+L)
2. /proje_incele yaz → Dökümanı sürükle bırak → Enter
3. Yazılım dili/framework ve SQL tercihini belirt (ajan stack matrisine göre paket önerir)
4. /proje_tasarim ile profil ve tema seç (kurumsal/standart + dark/soft-dark/light/hepsi)
5. /proje_basla yaz → Enter
6. İlk sürümden sonra /proje_eksik_tara çalıştır
7. /proje_devam ile eksikleri otomatik kapat
8. /proje_test ile kaliteyi doğrula
9. /proje_kalite_kapisi ile kalite kapısını geç
10. /proje_guvenlik_tara ile güvenlik temizliğini doğrula
11. /proje_bitir ile teslim al
```

### Döküman Ekleme Yöntemleri

```
# Yöntem 1: Sürükle bırak
Dosyayı chat penceresine sürükle

# Yöntem 2: @ ile referans ver
@proje_dokumani.pdf /proje_basla

# Yöntem 3: Yapıştır
Döküman içeriğini kopyala, chat'e yapıştır, komutu yaz
```

---

## 📁 Proje Yapısı

```
cursor-agent-tr/
├── .cursor/
│   ├── commands/               # Slash komutları
│   │   ├── proje_basla.md      # Ana geliştirme komutu
│   │   ├── proje_incele.md     # Döküman analizi
│   │   ├── proje_durum.md      # İlerleme raporu
│   │   ├── proje_test.md       # Test & uyum kontrolü
│   │   ├── proje_bitir.md      # Proje sonlandırma
│   │   ├── proje_sifirla.md    # Temizle & sıfırla
│   │   ├── proje_eksik_tara.md # Eksik ve öneri tarama
│   │   ├── proje_devam.md      # Eksiklerden devam
│   │   ├── proje_tasarim.md    # Tasarım profili yönetimi
│   │   ├── proje_kalite_kapisi.md # Kalite kapısı
│   │   └── proje_guvenlik_tara.md # Güvenlik taraması
│   └── rules/
│       └── agent.md            # Sistem kuralları ve davranış tanımı
├── docs/
│   ├── USAGE.md                # Detaylı kullanım kılavuzu
│   ├── ENTERPRISE_ROADMAP.md   # Kurumsal olgunlaşma planı
│   ├── STACK_MATRIX.md         # Stack öneri matrisi
│   ├── TODO.md                 # Örnek todo listesi şablonu
│   └── examples/               # Örnek proje dökümanları
│       ├── ecommerce.md
│       └── blog.md
├── scripts/
│   └── install.sh              # Otomatik kurulum scripti
├── README.md                   # Bu dosya
├── CHANGELOG.md                # Versiyon geçmişi
└── LICENSE                     # MIT Lisansı
```

---

## 🎯 Örnek Senaryo

```
Kullanıcı: @eticaret_projesi.pdf /proje_tasarim
Kullanıcı: kurumsal
Kullanıcı: /proje_basla

Ajan:
  ✅ Aşama 1: Döküman analiz edildi
  ✅ Aşama 2: Akış şeması oluşturuldu → /docs/FLOWCHART.md
  ✅ Aşama 3: 24 görev oluşturuldu → /docs/TODO.md
  ✅ Otomatik eksik tarama tamamlandı → /docs/GAP_REPORT.md
  ✅ 9 yeni eksik görevi TODO'ya eklendi

  🔄 GÖREV-001: Proje altyapısı kuruluyor...
  ✅ GÖREV-001: Tamamlandı
  🔄 GÖREV-002: Veritabanı şeması oluşturuluyor...
  ✅ GÖREV-002: Tamamlandı
  ...
  ✅ GÖREV-024: Admin paneli tamamlandı

  📊 Final analizi hazırlandı
  ⚙️ Config ekranı → /setup adresinde hazır
  📚 README.md ve USAGE.md güncellendi

  🚀 Proje teslime hazır!
```

---

## 🤝 Katkıda Bulun

1. Fork et
2. Feature branch oluştur (`git checkout -b feature/yeni-komut`)
3. Değişikliklerini commit et (`git commit -m 'feat: yeni komut eklendi'`)
4. Branch'i push et (`git push origin feature/yeni-komut`)
5. Pull Request aç

---

## 📄 Lisans

MIT © 2025 — Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

---

## 🙋 Sık Sorulan Sorular

**S: Harici API gerekiyor mu?**  
C: Hayır. Sistem tamamen Cursor IDE içinde çalışır, harici bağlantı gerekmez.

**S: Hangi proje türleri destekleniyor?**  
C: Web uygulamaları, API'ler, mobil (React Native), CLI araçları ve daha fazlası.

**S: Komutlar neden .md formatında?**  
C: Cursor IDE, `.cursor/commands/*.md` dosyalarını otomatik olarak slash komutu olarak tanır.

**S: Global kurulum ile proje bazlı kurulum arasındaki fark nedir?**  
C: Global kurulumda komutlar tüm projelerinizde çalışır. Proje bazlı kurulumda sadece o projede geçerlidir.
