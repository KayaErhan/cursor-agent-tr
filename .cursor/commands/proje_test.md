# /proje_test - Kapsamli Test, Duzeltme ve TODO Senkronu

Projedeki tamamlanan modulleri test et, kritik ve orta seviyeleri otomatik duzelt, sonucu TODO ile senkronla.

---

## Test Alanlari

1. Birim test
2. Entegrasyon test
3. UI/UX ve responsive
4. Guvenlik ve yetkilendirme
5. Admin panel fonksiyonlari
6. Performans temel kontrolleri (yavas sorgu, buyuk bundle, gereksiz tekrar render)

---

## Zorunlu Davranis

- Bulunan her hata icin TODO'ya gorev ac.
- Kritik ve orta hatalari ayni akista otomatik duzeltmeyi dene.
- Duzeltme sonrasinda ilgili testi tekrar calistir.
- Sonucu `/docs/TEST_REPORT.md` ve `/docs/GAP_REPORT.md` dosyalarina yaz.

---

## Test Sonu Karari

- Kritik hata varsa: sonraki komut onerisi `/proje_devam`
- Kritik yok, sadece dusuk iyilestirme varsa: `/proje_bitir`
