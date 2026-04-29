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

Varsayilan calisma seviyesi: **Expert Mode**  
Workflow ve kalite kurallari icin: `docs/WORKFLOW_STATE.md` ve `docs/WORKFLOW_DOD.md`

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
git clone https://github.com/KayaErhan/cursor-agent-tr.git
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

### Adım 4 — Docker (isteğe bağlı)

PostgreSQL veya yardımcı araçları konteynerda çalıştırmak için `docker/README.md` dosyasına bakın. Özet:

```bash
copy docker\env.example docker\.env   # Windows: önce .env oluşturun
docker compose -f docker/compose.yml up -d
```

Uygulama projesine `Dockerfile` ve tam Compose düzeni eklemek için chat’te **`/proje_docker`** kullanabilirsiniz.

---

## 📖 Kullanım

### Komut Listesi

| Komut | Açıklama |
|---|---|
| `/proje_incele` | Dökümanı analiz eder, akış şeması çıkarır, risk raporu hazırlar |
| `/proje_workflow` | n8n benzeri uçtan uca workflow'u adım adım yönetir (önerilen süper komut) |
| `/proje_durum` | Anlık ilerlemeyi ve todo listesini gösterir |
| `/proje_calistir` | Geliştirme sunucusunu (npm/pnpm/docker vb.) tespit edip çalıştırır |
| `/proje_docker` | İstenildiğinde Dockerfile / Compose / .dockerignore ve DB servisleri kurar |
| `/proje_test` | Tüm bileşenleri test eder, hataları otomatik düzeltir |
| `/proje_bitir` | Projeyi sonlandırır, config ekranı ve son dokümantasyonu oluşturur |
| `/proje_sifirla` | Mevcut çalışmayı arşivler, yeni proje için temizler |
| `/proje_eksik_tara` | Proje eksiklerini ve iyileştirme önerilerini otomatik tarar |
| `/proje_devam` | Taranan eksiklerden otomatik devam eder ve uygular |
| `/proje_tasarim` | Kurumsal/standart profil + dark/soft-dark/light/hepsi tema seçimi yapar |
| `/proje_kalite_kapisi` | Kurumsal kalite kapılarını puanlayarak geçiş kararı verir |
| `/proje_guvenlik_tara` | Güvenlik ve uyum taraması yapar, kritikleri raporlar |
| `/git_agent_update` | Repoyu çeker; yeni/değişen komut veya kural varsa global kopya için onay sorar |

### Kalite Doğrulama

```bash
python scripts/validate_quality.py
```

Bu komut; komut-dokuman tutarliligi, placeholder/kirik linkler, TODO formati ve sozlesme kontrollerini dogrular.

### Temel kullanım sırası

**Tam komut sırası (tek kaynak):** [docs/CANONICAL_FLOW.md](docs/CANONICAL_FLOW.md)

Kısa özet: Cursor’u aç → `/proje_incele` ve döküman → dil/SQL → `/proje_tasarim` → `/proje_workflow` veya `/proje_basla` → `/proje_eksik_tara` → gerekirse `/proje_devam` → `/proje_test` → `/proje_kalite_kapisi` → `/proje_guvenlik_tara` → `/proje_bitir`.

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
│   │   ├── proje_calistir.md   # Geliştirme sunucusunu çalıştır
│   │   ├── proje_docker.md     # Docker / Compose kurulumu
│   │   ├── proje_test.md       # Test & uyum kontrolü
│   │   ├── proje_bitir.md      # Proje sonlandırma
│   │   ├── proje_sifirla.md    # Temizle & sıfırla
│   │   ├── proje_eksik_tara.md # Eksik ve öneri tarama
│   │   ├── proje_devam.md      # Eksiklerden devam
│   │   ├── proje_tasarim.md    # Tasarım profili yönetimi
│   │   ├── proje_kalite_kapisi.md # Kalite kapısı
│   │   ├── proje_guvenlik_tara.md # Güvenlik taraması
│   │   └── git_agent_update.md   # Repodan komut/rule güncelle
│   └── rules/
│       └── agent.md            # Sistem kuralları ve davranış tanımı
├── docs/
│   ├── CANONICAL_FLOW.md       # Önerilen komut sırası (tek doğruluk kaynağı)
│   ├── USAGE.md                # Detaylı kullanım kılavuzu
│   ├── ENTERPRISE_ROADMAP.md   # Kurumsal olgunlaşma planı
│   ├── STACK_MATRIX.md         # Stack öneri matrisi
│   ├── TODO.md                 # Örnek todo listesi şablonu
│   └── examples/               # Örnek proje dökümanları
│       ├── ecommerce.md
│       └── blog.md
├── docker/                     # İsteğe bağlı Compose (PostgreSQL, pgAdmin profili)
│   ├── compose.yml
│   ├── env.example
│   └── README.md
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
