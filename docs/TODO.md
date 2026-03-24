# Yapılacaklar Listesi (TODO)

> Bu dosya `/proje_basla` komutu tarafından otomatik oluşturulur ve güncellenir.
> Her tamamlanan görev `[x]` olarak işaretlenir.

---

## 📊 İlerleme Özeti

| Durum | Sayı |
|---|---|
| ✅ Tamamlanan | 0 |
| 🔄 Devam Eden | 0 |
| ⏳ Bekleyen | 0 |
| **Toplam** | **0** |

---

## 🏗️ Altyapı

```
[ ] GÖREV-001 | Proje klasör yapısını oluştur         | Bağımlılık: YOK          | Öncelik: YÜKSEK
[ ] GÖREV-002 | Bağımlılıkları yükle ve yapılandır    | Bağımlılık: GÖREV-001    | Öncelik: YÜKSEK
[ ] GÖREV-003 | Veritabanı şemasını oluştur           | Bağımlılık: GÖREV-001    | Öncelik: YÜKSEK
[ ] GÖREV-004 | Ortam değişkenlerini (env) ayarla     | Bağımlılık: GÖREV-001    | Öncelik: YÜKSEK
```

## ⚙️ Backend

```
[ ] GÖREV-005 | API temel yapısını kur                | Bağımlılık: GÖREV-002    | Öncelik: YÜKSEK
[ ] GÖREV-006 | Authentication sistemi (giriş/çıkış)  | Bağımlılık: GÖREV-003    | Öncelik: YÜKSEK
[ ] GÖREV-007 | CRUD endpoint'lerini oluştur          | Bağımlılık: GÖREV-005    | Öncelik: YÜKSEK
[ ] GÖREV-008 | E-posta (SMTP) entegrasyonu           | Bağımlılık: GÖREV-004    | Öncelik: ORTA
```

## 🎨 Frontend

```
[ ] GÖREV-009 | Tailwind CSS kurulumu ve tema         | Bağımlılık: GÖREV-002    | Öncelik: YÜKSEK
[ ] GÖREV-010 | Ana sayfa tasarımı                    | Bağımlılık: GÖREV-009    | Öncelik: YÜKSEK
[ ] GÖREV-011 | Giriş / Kayıt sayfaları               | Bağımlılık: GÖREV-006    | Öncelik: YÜKSEK
[ ] GÖREV-012 | Dashboard tasarımı                    | Bağımlılık: GÖREV-009    | Öncelik: ORTA
[ ] GÖREV-013 | Responsive düzenlemeler               | Bağımlılık: GÖREV-010    | Öncelik: ORTA
```

## 🛡️ Admin Paneli (Zorunlu)

```
[ ] GÖREV-014 | Admin panel temel yapısı (/admin)     | Bağımlılık: GÖREV-006    | Öncelik: YÜKSEK
[ ] GÖREV-015 | Kullanıcı yönetimi (CRUD)             | Bağımlılık: GÖREV-014    | Öncelik: YÜKSEK
[ ] GÖREV-016 | İçerik yönetimi                       | Bağımlılık: GÖREV-014    | Öncelik: ORTA
[ ] GÖREV-017 | Raporlama ve istatistikler            | Bağımlılık: GÖREV-014    | Öncelik: ORTA
[ ] GÖREV-018 | Sistem ayarları ekranı                | Bağımlılık: GÖREV-014    | Öncelik: DÜŞÜK
```

## 🧪 Test

```
[ ] GÖREV-019 | Birim testleri yaz                    | Bağımlılık: GÖREV-007    | Öncelik: ORTA
[ ] GÖREV-020 | Entegrasyon testleri yaz              | Bağımlılık: GÖREV-007    | Öncelik: ORTA
[ ] GÖREV-021 | UI/UX ve erişilebilirlik testleri     | Bağımlılık: GÖREV-013    | Öncelik: ORTA
```

## ⚙️ Yapılandırma Ekranı

```
[ ] GÖREV-022 | Config/Setup arayüzü oluştur (/setup) | Bağımlılık: GÖREV-009    | Öncelik: ORTA
[ ] GÖREV-023 | .env dosyasına güvenli yazma          | Bağımlılık: GÖREV-022    | Öncelik: ORTA
```

## 📚 Dokümantasyon

```
[ ] GÖREV-024 | README.md tamamla                     | Bağımlılık: GÖREV-023    | Öncelik: DÜŞÜK
[ ] GÖREV-025 | USAGE.md (kullanım kılavuzu) tamamla  | Bağımlılık: GÖREV-023    | Öncelik: DÜŞÜK
[ ] GÖREV-026 | CHANGELOG.md oluştur                  | Bağımlılık: GÖREV-024    | Öncelik: DÜŞÜK
```

---

*Bu dosya ajan tarafından otomatik güncellenir.*
