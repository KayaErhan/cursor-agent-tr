# /proje_guvenlik_tara - Guvenlik ve Uyum Taramasi

Projeyi kurumsal guvenlik kontrol listesine gore tara ve raporla.

---

## Kontrol Alanlari

- Kimlik dogrulama ve yetkilendirme (RBAC)
- Input validation / sanitization
- SQL injection / XSS / CSRF temel kontrolleri
- Secret ve env yonetimi
- HTTP guvenlik basliklari
- Rate limiting / brute-force korumasi
- Audit log varligi

---

## Siddet Seviyeleri

- Kritik
- Yuksek
- Orta
- Dusuk

Kural:
- Kritik ve yuksek bulgular TODO'ya otomatik eklenir ve once ele alinir.

---

## Cikti

Raporu `/docs/SECURITY_REPORT.md` dosyasina yaz:
- Bulgu listesi
- Siddet dagilimi
- Cozum onerileri
- Tekrar test sonucu
