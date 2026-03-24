# Örnek Proje Dökümanı: E-Ticaret Platformu

> Bu dosya `/proje_basla` veya `/proje_incele` komutları ile kullanılmak üzere hazırlanmış örnek bir proje dökümanıdır.
> Kendi projeniz için bu şablonu doldurun.

---

## Genel Açıklama

Modern, ölçeklenebilir bir e-ticaret platformu. Satıcıların ürün listeleyebildiği, kullanıcıların ürün satın alabildiği ve admin'in tüm sistemi yönettiği çok taraflı bir platform.

## Hedef Kitle

- **Satıcılar:** Ürünlerini listeleyen küçük ve orta ölçekli işletmeler
- **Müşteriler:** Online alışveriş yapan son kullanıcılar
- **Adminler:** Platform yöneticileri

## Temel Özellikler

- Ürün listeleme, filtreleme ve arama
- Alışveriş sepeti ve sipariş yönetimi
- Kullanıcı kayıt / giriş sistemi
- Satıcı dashboard'u
- Sipariş takip sistemi
- Ürün yorumları ve puanlama

## Teknik Tercihler

- **Framework:** Next.js 14 (App Router)
- **Veritabanı:** PostgreSQL
- **CSS:** Tailwind CSS (zorunlu)
- **Auth:** JWT tabanlı kimlik doğrulama

## Kullanıcı Rolleri

- **Super Admin:** Tüm sisteme tam erişim
- **Satıcı:** Kendi ürün ve siparişlerini yönetir
- **Müşteri:** Ürün görüntüler, satın alır, yorum yapar

## Ekranlar / Sayfalar

- Ana Sayfa (ürün vitrin, öne çıkanlar)
- Ürün Listesi (filtreleme, sıralama)
- Ürün Detay (görseller, açıklama, yorumlar)
- Alışveriş Sepeti
- Ödeme / Checkout
- Kullanıcı Profili
- Sipariş Geçmişi
- Satıcı Dashboard
- Admin Paneli (`/admin`)

## Kapsam Dışı

- Gerçek ödeme entegrasyonu (Stripe, iyzico vb.)
- Mobil uygulama
- Çoklu para birimi
