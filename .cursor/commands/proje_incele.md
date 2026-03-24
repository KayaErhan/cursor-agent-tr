# /proje_incele — Döküman Analizi & Ön Değerlendirme

Sağlanan proje dökümanını analiz et ve geliştirme başlamadan önce kapsamlı bir ön değerlendirme sun.

---

## Çıktılar

### 1. Proje Özeti
- Ne yapıyor? Kimin için? Hangi sorunu çözüyor?
- Temel özellikler ve kapsam dışı bırakılanlar

### 2. Teknik Gereksinimler
- Önerilen programlama dili ve framework
- Veritabanı tercihi ve nedeni
- Harici bağımlılıklar (kütüphaneler, araçlar)
- Altyapı gereksinimleri

### 3. Sistem Mimarisi & Akış Şeması
Bileşenler arası ilişkileri ve veri akışını Mermaid veya ASCII formatında göster:

```
[Kullanıcı] → [Frontend] → [API Gateway] → [Backend] → [Veritabanı]
```

### 4. Risk Analizi
| Risk | Olasılık | Etki | Öneri |
|---|---|---|---|
| ... | ... | ... | ... |

### 5. Görev Tahmini
- Toplam tahmini görev sayısı
- Kategori dağılımı (Altyapı, Backend, Frontend, Test, Dokümantasyon)
- Tahmini karmaşıklık seviyesi (Düşük / Orta / Yüksek)

### 6. Önerilen Teknoloji Stack'i
Projeye özgü en uygun stack'i açıkla ve neden seçildiğini belirt.

---

## Kayıt

Tüm analiz sonuçlarını `/docs/ANALYSIS.md` dosyasına kaydet.

Analiz tamamlandıktan sonra kullanıcıya sor:
> "Analiz tamamlandı. `/proje_basla` komutu ile geliştirmeye başlayalım mı, yoksa değişiklik yapmak ister misin?"
