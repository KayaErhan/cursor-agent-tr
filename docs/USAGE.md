# 📖 Kullanım Kılavuzu — Cursor Otonom Geliştirme Ajanı

> Bu kılavuz, Cursor Otonom Geliştirme Ajanı'nı nasıl kuracağınızı, yapılandıracağınızı ve verimli şekilde kullanacağınızı adım adım açıklar.

---

## İçindekiler

1. [Sistem Gereksinimleri](#1-sistem-gereksinimleri)
2. [Kurulum](#2-kurulum)
3. [İlk Kullanım](#3-ilk-kullanım)
4. [Komut Referansı](#4-komut-referansı)
5. [Proje Dökümanı Nasıl Hazırlanır?](#5-proje-dökümanı-nasıl-hazırlanır)
6. [Geliştirme Akışı](#6-geliştirme-akışı)
7. [Üretilen Dosyalar](#7-üretilen-dosyalar)
8. [İpuçları & En İyi Pratikler](#8-ipuçları--en-iyi-pratikler)
9. [Sorun Giderme](#9-sorun-giderme)

---

## 1. Sistem Gereksinimleri

| Gereksinim | Minimum Versiyon | Notlar |
|---|---|---|
| Cursor IDE | v0.40+ | [cursor.sh](https://cursor.sh) adresinden indirin |
| Git | Herhangi | Kurulum için gerekli |
| İşletim Sistemi | Windows 10, macOS 12, Ubuntu 20.04 | |

---

## 2. Kurulum

### 2.1 Repoyu Klonlayın

```bash
git clone https://github.com/KULLANICI_ADIN/cursor-agent-tr.git
cd cursor-agent-tr
```

### 2.2 Kurulum Seçeneğini Belirleyin

#### Seçenek A: Mevcut Bir Projeye Ekleyin (Proje Bazlı)

```bash
# macOS / Linux
cp -r .cursor /yolunuz/projenizin-adı/

# Windows (PowerShell)
Copy-Item -Recurse .cursor C:\Projeler\projenizin-adı\
```

Bu yöntemde komutlar **yalnızca o proje** klasöründe çalışır.

#### Seçenek B: Tüm Projelerinizde Kullanın (Global Kurulum)

```bash
# macOS / Linux
mkdir -p ~/.cursor/commands ~/.cursor/rules
cp .cursor/commands/* ~/.cursor/commands/
cp .cursor/rules/* ~/.cursor/rules/

# Windows (PowerShell)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.cursor\commands"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.cursor\rules"
Copy-Item .cursor\commands\* "$env:USERPROFILE\.cursor\commands\"
Copy-Item .cursor\rules\* "$env:USERPROFILE\.cursor\rules\"
```

Bu yöntemde komutlar **tüm projelerinizde** otomatik olarak çalışır.

### 2.3 Kurulumu Doğrulayın

1. Cursor IDE'yi açın.
2. Herhangi bir proje klasörünü açın.
3. `Ctrl+L` (macOS: `Cmd+L`) ile chat panelini açın.
4. `/` yazın — komutların listede göründüğünü doğrulayın.

```
/proje_basla     ✅ görünüyor
/proje_incele    ✅ görünüyor
/proje_durum     ✅ görünüyor
/proje_test      ✅ görünüyor
/proje_bitir     ✅ görünüyor
/proje_sifirla   ✅ görünüyor
/proje_eksik_tara ✅ görünüyor
/proje_devam     ✅ görünüyor
/proje_tasarim   ✅ görünüyor
/proje_kalite_kapisi ✅ görünüyor
/proje_guvenlik_tara ✅ görünüyor
```

---

## 3. İlk Kullanım

### Adım 1: Cursor'u Açın

Cursor IDE'yi başlatın ve çalışmak istediğiniz proje klasörünü açın (`File → Open Folder`).

### Adım 2: Chat Panelini Açın

```
Windows / Linux : Ctrl + L
macOS           : Cmd + L
```

### Adım 3: Dökümanı Ekleyin

Üç yöntemden birini kullanabilirsiniz:

**Yöntem 1 — Sürükle Bırak:**
Proje dökümanı dosyasını (`.pdf`, `.md`, `.txt`, `.docx`) doğrudan chat penceresine sürükleyin.

**Yöntem 2 — @ ile Referans:**
```
@proje_dokumani.pdf
```

**Yöntem 3 — Yapıştır:**
Döküman içeriğini kopyalayıp chat'e yapıştırın.

### Adım 4: Komut Çalıştırın

```
/proje_incele
```
veya doğrudan başlamak için:
```
/proje_basla
```

---

## 4. Komut Referansı

### `/proje_incele`

**Ne yapar:** Proje dökümanını derinlemesine analiz eder, geliştirmeye başlamadan önce kapsamlı bir ön değerlendirme sunar.

**Çıktılar:**
- Proje özeti ve teknik gereksinimler
- Seçilen yazılım dili/framework
- Seçilen SQL/veritabanı
- Sistem mimarisi akış şeması
- Risk analizi tablosu
- Önerilen teknoloji stack'i
- Tahmini görev sayısı ve kategoriler

**Oluşturulan dosyalar:** `/docs/ANALYSIS.md`, `/docs/TECH_STACK.md`, `/docs/STACK_MATRIX.md`

**Ne zaman kullanılır:** Geliştirmeye başlamadan önce, dökümanın kapsamını anlamak istediğinizde.

---

### `/proje_basla`

**Ne yapar:** Proje dökümanını alır ve baştan sona tam otomatik geliştirme sürecini başlatır. 7 aşamalı süreci kullanıcıdan ek komut beklemeden yürütür.

**Aşamalar:**
1. Döküman analizi
2. Akış şeması oluşturma
3. İş planı ve todo listesi
4. Otomatik geliştirme döngüsü
5. Genel analiz ve ek öneriler
6. Yapılandırma arayüzü
7. Son dokümantasyon

**Oluşturulan dosyalar:** Tüm proje dosyaları, `/docs/TODO.md`, `/docs/FLOWCHART.md`, `/docs/ANALYSIS.md`, `/README.md`, `/docs/USAGE.md`

**Ne zaman kullanılır:** Döküman analizi onaylandıktan sonra, geliştirmeye başlamak istediğinizde.

---

### `/proje_durum`

**Ne yapar:** `/docs/TODO.md` dosyasını okuyarak projenin anlık durumunu gösterir.

**Çıktılar:**
- Genel ilerleme yüzdesi ve ilerleme çubuğu
- Tamamlanan, devam eden ve bekleyen görev sayıları
- Aktif görev bilgisi
- Sıradaki 3 görev
- Engelleyen sorunlar (varsa)
- Oluşturulan dosyalar listesi

**Oluşturulan dosyalar:** `/docs/STATUS_REPORT.md`

**Ne zaman kullanılır:** Geliştirme sürecinde ilerlemeyi takip etmek için istediğiniz zaman.

---

### `/proje_test`

**Ne yapar:** Tüm tamamlanan bileşenler üzerinde kapsamlı test yürütür, hataları tespit eder ve kritik hataları otomatik düzeltir.

**Test kategorileri:**
- Birim testleri
- Entegrasyon testleri
- UI/UX kontrolü (responsive, erişilebilirlik)
- Güvenlik kontrolü (injection, XSS, auth)
- Admin paneli testleri

**Oluşturulan dosyalar:** `/docs/TEST_REPORT.md`

**Ne zaman kullanılır:** İlgili görev grupları tamamlandığında veya geliştirme bitmeden önce.

---

### `/proje_bitir`

**Ne yapar:** Projeyi sonlandırır, eksikleri giderir ve teslime hazır hale getirir.

**Adımlar:**
1. Final analizi
2. Ek öneri değerlendirmesi (güvenlik, performans, ölçeklenebilirlik)
3. Yapılandırma arayüzü oluşturma (`/setup` veya `/config`)
4. Son dokümantasyon güncellemesi
5. Teslim özeti

**Ne zaman kullanılır:** Tüm görevler tamamlandıktan sonra.

---

### `/proje_sifirla`

**Ne yapar:** Mevcut proje çalışmasını arşivler ve yeni bir proje için temiz başlangıç hazırlar.

⚠️ **Dikkat:** Bu komut mevcut ilerlemeyi temizler. Önce yedek alındığını doğrulayın.

**Ne zaman kullanılır:** Tamamen farklı bir projeye geçerken.

---

### `/proje_eksik_tara`

**Ne yapar:** Projeyi tamamlanma sonrası veya ara aşamada tarar; eksikleri, riskleri ve iyileştirme önerilerini sınıflandırır.

**Çıktılar:**
- Gap analizi (kritik/önemli/iyileştirme)
- TODO'ya otomatik eklenen yeni görevler
- Önceliklendirilmiş aksiyon listesi

**Oluşturulan dosyalar:** `/docs/GAP_REPORT.md`, `/docs/TODO.md` (güncel)

**Ne zaman kullanılır:** İlk çalışan sürümden hemen sonra ve teslim öncesi.

---

### `/proje_devam`

**Ne yapar:** `/proje_eksik_tara` ile bulunan eksiklerden otomatik devam eder, uygular ve test eder.

**Çıktılar:**
- Kapatılan eksik listesi
- Güncel TODO durumu
- Kalan maddeler ve önerilen sonraki komut

**Oluşturulan dosyalar:** `/docs/STATUS_REPORT.md`, `/docs/TODO.md` (güncel)

**Ne zaman kullanılır:** Eksik tarama sonrası iyileştirme döngüsünde.

---

### `/proje_tasarim`

**Ne yapar:** Tasarım profilini (`kurumsal` / `standart`) ve tema modunu (`dark` / `soft-dark` / `light` / `hepsi`) kullanıcıdan alır; tüm UI katmanını Tailwind CSS ile buna göre uygular.

**Çıktılar:**
- Seçilen tasarım profili
- Seçilen tema modu
- Renk/typography/spacing sisteminin profile göre uygulanması
- Tasarıma ait eksiklerin TODO'ya otomatik eklenmesi
- Sol menülü admin panel yapısının kurulması
- Bildirim, email/mesaj alanları, detaylı dashboard ve grafiklerin üretilmesi
- Onerilen UI paketlerinin uygulanmasi (duruma gore):
  - `lucide-react` (ikon)
  - `recharts` (grafik)
  - `framer-motion` (mikro-animasyon)

**Oluşturulan dosyalar:** `/docs/DESIGN_PROFILE.md`

**Ne zaman kullanılır:** `/proje_basla` öncesi veya proje ortasında tasarım revizyonu gerektiğinde.

---

### `/proje_kalite_kapisi`

**Ne yapar:** Build, test, güvenlik, tasarım ve dokümantasyon kapılarını puanlayarak geçiş kararı verir.

**Çıktılar:**
- Toplam kalite puanı (100)
- Geçen/kalan kalite kapıları
- Bloke eden maddeler

**Oluşturulan dosyalar:** `/docs/QUALITY_GATE_REPORT.md`

**Ne zaman kullanılır:** `/proje_test` sonrasında, teslimden önce.

---

### `/proje_guvenlik_tara`

**Ne yapar:** Güvenlik ve uyum kontrollerini tarar; kritik/yüksek açıkları TODO'ya yazar.

**Çıktılar:**
- Güvenlik bulgu listesi
- Şiddet dağılımı
- Düzeltme önerileri

**Oluşturulan dosyalar:** `/docs/SECURITY_REPORT.md`, `/docs/TODO.md` (güncel)

**Ne zaman kullanılır:** Kalite kapısı sonrası ve `/proje_bitir` öncesi.

---

## 5. Proje Dökümanı Nasıl Hazırlanır?

İyi bir proje dökümanı ajanın daha doğru çalışmasını sağlar. Aşağıdaki şablonu kullanabilirsiniz:

```markdown
# Proje Adı

## Genel Açıklama
[Projenin ne yaptığını 2-3 cümleyle açıklayın]

## Hedef Kitle
[Bu sistemi kimler kullanacak?]

## Temel Özellikler
- Özellik 1: [Açıklama]
- Özellik 2: [Açıklama]
- Özellik 3: [Açıklama]

## Teknik Tercihler (Opsiyonel)
- Dil/Framework: [Örn: Next.js, Laravel, Django]
- Veritabanı: [Örn: PostgreSQL, MySQL, MongoDB]
- Özel gereksinimler: [Varsa belirtin]

## Kullanıcı Rolleri
- Admin: [Ne yapabilir?]
- Kullanıcı: [Ne yapabilir?]
- [Diğer roller...]

## Ekranlar / Sayfalar
- Ana Sayfa
- Kullanıcı Girişi
- Dashboard
- [Diğer sayfalar...]

## Kapsam Dışı (Opsiyonel)
- [Bu projede olmayacak özellikler]
```

---

## 6. Geliştirme Akışı

### Standart Akış (Önerilen)

```
📄 Döküman Hazırla
        ↓
🔍 /proje_incele  →  Analizi İncele & Onayla
        ↓
🧱 Dil/Framework + SQL seçimi
        ↓
🎨 /proje_tasarim →  profil + tema seç (kurumsal/standart + dark/soft-dark/light/hepsi)
        ↓
🚀 /proje_basla   →  Otomatik Geliştirme Başlar
        ↓
🔎 /proje_eksik_tara → Eksikleri ve önerileri tara
        ↓
🛠️ /proje_devam   → Eksikleri otomatik kapat
        ↓
📊 /proje_durum   →  İlerlemeyi Takip Et (isteğe bağlı, istediğin zaman)
        ↓
🧪 /proje_test    →  Testleri Çalıştır (kritik aşamalar sonrası)
        ↓
🧩 /proje_kalite_kapisi → Kalite puanını doğrula
        ↓
🔐 /proje_guvenlik_tara → Güvenlik açıklarını temizle
        ↓
🏁 /proje_bitir   →  Sonlandır & Teslim Al
```

### Hızlı Başlangıç Akışı

Analiz aşamasını atlamak istiyorsanız:

```
📄 Döküman Hazırla
        ↓
🚀 /proje_basla   →  Direkt Başla (analiz dahil)
        ↓
🏁 /proje_bitir   →  Teslim Al
```

---

## 7. Üretilen Dosyalar

Her proje sonunda şu dosyalar oluşturulur:

```
proje-klasoru/
├── src/                        # Kaynak kodlar
│   ├── components/             # UI bileşenleri (Tailwind CSS)
│   ├── pages/                  # Sayfalar
│   │   └── admin/              # Admin paneli (zorunlu)
│   ├── api/                    # API endpoint'leri
│   └── config/                 # Yapılandırma dosyaları
├── docs/
│   ├── ANALYSIS.md             # Genel analiz raporu
│   ├── FLOWCHART.md            # Akış şeması ve mimari
│   ├── TODO.md                 # Görev listesi (tamamlananlar işaretli)
│   ├── TEST_REPORT.md          # Test sonuçları
│   ├── STATUS_REPORT.md        # İlerleme raporu
│   └── USAGE.md                # Detaylı kullanım kılavuzu
├── .env.example                # Örnek ortam değişkenleri
├── README.md                   # Proje README'si
└── CHANGELOG.md                # Versiyon geçmişi
```

---

## 8. İpuçları & En İyi Pratikler

### Daha İyi Sonuçlar için

- **Dökümanı detaylı yazın:** Ne kadar çok bilgi verirseniz, çıktı o kadar iyi olur.
- **Teknik tercihleri belirtin:** Framework, veritabanı, dil tercihlerinizi dökümanınıza ekleyin.
- **Önce `/proje_incele` kullanın:** Geliştirmeye başlamadan önce ajanın projeyi doğru anladığını teyit edin.
- **Düzenli durum kontrolü yapın:** `/proje_durum` ile ilerlemeyi takip edin.

### Admin Paneli

Her projede `/admin` rotasında bir admin paneli oluşturulur. Varsayılan özellikler:
- Kullanıcı yönetimi (CRUD)
- İçerik yönetimi
- Sistem ayarları
- Raporlama ve istatistikler
- Log görüntüleme

### Yapılandırma Ekranı

`/proje_bitir` sonrası `/setup` adresinde açılan yapılandırma ekranında:
- Gerçek veritabanı bilgilerinizi girin.
- SMTP ayarlarınızı test edin.
- Tüm bilgiler `.env` dosyasına güvenli şekilde kaydedilir.

---

## 9. Sorun Giderme

### Komutlar listede görünmüyor

**Çözüm:**
1. `.cursor/commands/` klasörünün doğru konumda olduğunu kontrol edin.
2. Cursor IDE'yi yeniden başlatın.
3. Chat panelini kapatıp tekrar açın (`Ctrl+L`).

### Ajan bir sonraki göreve geçmiyor

**Çözüm:**
- `/proje_durum` yazarak mevcut durumu kontrol edin.
- Engelleyen bir bağımlılık olup olmadığını görün.
- `/proje_test` ile hata olup olmadığını kontrol edin.

### Dosyalar oluşturulmuyor

**Çözüm:**
1. Cursor'un proje klasöründe yazma iznine sahip olduğunu kontrol edin.
2. `docs/` klasörünün var olduğunu doğrulayın (yoksa oluşturun).
3. Gerekirse manuel olarak klasör oluşturup tekrar deneyin:
```bash
mkdir -p docs scripts
```

### Tailwind CSS çalışmıyor

**Çözüm:**
Proje dökümanınıza şu satırı ekleyin:
```
Teknik gereksinim: Tailwind CSS v3 kullanılmalı. CDN veya npm ile kurulabilir.
```

---

## 📬 Destek & Geri Bildirim

Sorun veya öneriniz için:
- GitHub Issues: [github.com/KULLANICI_ADIN/cursor-agent-tr/issues](https://github.com/KULLANICI_ADIN/cursor-agent-tr/issues)
- Pull Request'lerinizi bekliyoruz!

---

*Bu kılavuz, her proje aşamasında otomatik olarak güncellenir.*
