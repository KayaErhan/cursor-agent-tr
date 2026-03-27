# Expert Seviye Urun ve Admin Panel Standardi

Bu dokumanin amaci, ajanin uretecegi projeleri "basit demo" seviyesinden cikarip kurumsal, olculebilir ve expert seviye urun kalitesine tasimaktir.

---

## 1) Hedef Seviye ve Basari Gosterge Seti

Her proje asagidaki sonuc odakli KPI'lari saglamalidir:

- Teknik kalite skoru >= 85/100
- UI/UX kalite skoru >= 85/100
- Guvenlik ve uyumluluk skoru >= 85/100
- Kritik hata sayisi: 0
- Yuksek siddetli bulgu: 0
- Teslimde dokumantasyon eksigi: 0

Expert seviyede "calisiyor" yeterli degildir; "olceklendirilebilir, bakimi kolay, guvenli ve premium" olmasi zorunludur.

---

## 2) Expert Seviye Admin Panel (Zorunlu)

## 2.1 Bilgi Mimarisi ve Modul Haritasi

Admin panel asgari degil, tam kapsamli bir operasyon merkezi olmali:

1. Dashboard (operasyonel + yonetsel ozet)
2. Kullanici ve Hesap Yonetimi
3. RBAC (Rol/Izin/Politika)
4. Organizasyon ve Takim Yonetimi (multi-tenant senaryolari)
5. Icerik/Kaynak Yonetimi
6. Is Akislari ve Gorev Orkestrasyonu
7. Bildirim Merkezi (in-app)
8. Email / Mesaj Merkezi (template + kuyruk + durum)
9. Raporlar ve Analitik
10. Faturalama/Planlama (uygun urunlerde)
11. Sistem Ayarlari ve Konfigurasyon
12. Audit Log ve Olay Gecmisi
13. Hata/Alarm Merkezi
14. Entegrasyonlar (API key, webhook, baglanti ayarlari)

## 2.2 Admin Ekran Agaci (Minimum)

- `/admin`
  - `/dashboard`
  - `/users`
  - `/roles`
  - `/permissions`
  - `/workflows`
  - `/notifications`
  - `/messages`
  - `/reports`
  - `/settings/general`
  - `/settings/security`
  - `/audit-logs`
  - `/system-events`

Bu agac urun tipine gore genisleyebilir, ama daralamaz.

## 2.3 Layout ve Navigasyon Standardi

- Sol sidebar zorunlu (desktop sabit, mobil drawer).
- Topbar zorunlu: global arama, bildirim, mesaj/email, profil, hizli aksiyon.
- Breadcrumb zorunlu.
- Sayfa seviyesinde filtre/sort/search kalici olabilmeli (query state).
- Komut paleti (Ctrl/Cmd+K) zorunluya yakin.
- Favori menu ve son ziyaret edilen ekranlar bolumu onerilir.

## 2.4 Dashboard Expert Kriterleri

Dashboard bir "gosterge panosu" degil, karar destek sistemi olmali:

- KPI kartlari:
  - Gunluk/haftalik/aylik karsilastirma
  - Trend oku (up/down) + sapma yuzdesi
  - Hedefe gore durum (on-track/off-track)
- En az 8 bilesen:
  - Line chart
  - Bar chart
  - Donut chart
  - Funnel veya conversion
  - Heatmap veya dagilim
  - Son aktiviteler akisi
  - Risk/uyari paneli
  - Bekleyen kritik aksiyon listesi
- Drill-down zorunlu: kart/grafik tiklaninca detay sayfa acilmali.
- Segment ve tarih filtresi zorunlu.
- Gercek veri yoksa tutarli mock veri kullanilmali.

## 2.5 Data Table Expert Kriterleri

Tum liste ekranlarinda zorunlu:

- Server-side pagination
- Multi-column sorting
- Gelismis filtreleme (text, enum, date range, numeric range)
- Kaydedilebilir filtre setleri
- Kolon gizle/goster + kolon sirasi
- Toplu islem (bulk actions) + islem onayi
- CSV/Excel export
- Satir detay paneli (inline detail)
- Empty/loading/error state
- Buyuk veri setinde performansli render

## 2.6 Form Expert Kriterleri

- Alan bazli + form bazli validation
- Geri al (undo) + taslak kaydet (draft)
- Wizard mod (cok adimli formlar)
- Otomatik kaydet (uygunsa)
- Dosya yukleme + onizleme + tur/size kontrolu
- Hata metinleri aksiyon odakli olmali
- Kritik guncellemelerde degisiklik ozeti ve onay adimi

## 2.7 Bildirim ve Mesaj Merkezi Kriterleri

- In-app bildirim kutusu (okunmamis/okunmus)
- Email template yonetimi
- Gonderim kuyrugu durumu (pending/sent/failed)
- Yeniden deneme (retry) aksiyonu
- Olay bazli bildirim kurallari (trigger tabanli)
- Sessize alma/kanal secimi (uygunsa)

## 2.8 Audit Log ve Olay Gecmisi

- Kim, neyi, ne zaman degistirdi?
- Eski deger / yeni deger (uygun alanlarda)
- IP, cihaz, oturum bilgisi (uygun guvenlik politikasiyla)
- Filtrelenebilir ve export edilebilir loglar
- Kritik islemlerde immutable audit trail yaklasimi

---

## 3) Tasarim Sistemi ve UI Detay Standardi (Genisletilmis)

## 3.1 Design System Katmanlari

Asagidaki katmanlar net ayrilmali:

1. Design tokens (color, spacing, radius, shadow, typography, motion)
2. Primitive components (button, input, badge, tooltip)
3. Composite components (datatable, filterbar, stat-card, chart-card)
4. Pattern library (crud page, settings page, wizard flow)

## 3.2 Tema Mimarisi

- Tema secenekleri: dark, soft-dark, light, hepsi.
- Hepsi seciliyse tema switcher zorunlu.
- Her temada ayni kontrast standardi korunmali.
- Tema tokenlari kodda hard-code edilmemeli; token uzerinden yonetilmeli.

## 3.3 Renk ve Tipografi Standardi

- En az su renk rolleri tanimli olmali:
  - primary, secondary, accent
  - success, warning, danger, info
  - surface, background, border, muted
- Tipografi:
  - Display, heading, body, caption seviyeleri
  - Satir yuksekligi ve letter spacing tutarliligi

## 3.4 Ikonografi ve Gorsel Dil

- Ikon seti tutarli olmali (or. `lucide-react`).
- Ikon boyut kurallari tanimli olmali (16/20/24/32).
- Durum ikonlari (success/warn/error/info) ayni semantik dilde kullanilmali.

## 3.5 Mikro Etkilesimler ve Motion

- Hover, focus, active, disabled state'leri zorunlu.
- Mikro animasyonlar amaca hizmet etmeli, dikkat dagitmamalı.
- Sayfa gecis animasyonlari 150-250ms araliginda kalmali.
- Loading state'lerde skeleton tercih edilmeli.

## 3.6 UI Kabul Kriterleri (Olculebilir)

- Kontrast seviyesi WCAG AA altina dusmemeli.
- Her ana sayfada en az 3 farkli reusable component kullanilmali.
- Bos/yukleniyor/hata state'leri tum kritik ekranlarda bulunmali.
- Formlarda keyboard navigation kesintisiz olmali.

---

## 4) Expert Seviye Proje Mimarisi

## 4.1 Mimari Prensipler

- Katmanli yapi: presentation / application / domain / infrastructure
- Moduler monolith veya bounded-context tabanli moduller
- Is kurallarini UI'dan ayirma
- Transaction sinirlari ve side-effect yonetimi net
- Domain odakli isimlendirme ve klasorleme

## 4.2 Klasorleme Standardi (Ornek)

`src/modules/<domain>/`:

- `api/` (routes, controllers)
- `application/` (use-cases, services)
- `domain/` (entities, value objects, policies)
- `infrastructure/` (repositories, adapters)
- `dto/`, `schema/`, `mappers/`, `tests/`

## 4.3 API ve Sozlesme Standardi

- Tutarli response envelope
- Standard hata kodlari ve hata siniflari
- Idempotency (uygun endpointlerde)
- Pagination/filter/sort standardizasyonu
- API versiyonlama (v1, v2)
- Contract dokumani (OpenAPI veya esdeger)

---

## 5) Guvenlik ve Uyum (Genisletilmis)

- RBAC zorunlu (rol + izin matrisi)
- Kritik islemlerde cift onay/adim
- Audit log zorunlu
- Rate limiting + brute-force korumasi
- Input validation + output encoding
- Secret management + env hijyeni
- Guvenlik basliklari (CSP dahil, uygulanabilirlik durumuna gore)
- PII maskeleme ve log sanitization
- Dosya yuklemelerinde tarama/politika (boyut/tur)
- Session/token omru ve yenileme politikasi

---

## 6) Performans ve Olceklenebilirlik (Genisletilmis)

- Performans butcesi:
  - Ilk yukleme suresi
  - API p95 suresi
  - Etkilesim gecikmesi
- Lazy loading + code splitting
- Cache stratejisi (client/server)
- DB index plani + slow query analizi
- N+1 korumasi
- Buyuk listelerde virtualized render (uygunsa)
- Asenkron isler icin queue stratejisi (uygun senaryoda)

---

## 7) Test Stratejisi (Expert)

Zorunlu test katmanlari:

1. Unit test
2. Integration test
3. API contract test
4. E2E kritik akis testleri
5. RBAC/izin testleri
6. UI regression smoke test
7. Error-path testleri

Minimum kapsam:

- Kritik modullerde test kapsam >= %80
- Kritik akislarda e2e pass zorunlu
- Security regression testleri her release oncesi

---

## 8) Operasyon, DevOps ve Gozlemlenebilirlik

- CI: lint + test + build + security checks
- CD: staging/production ayrimi + rollback plani
- Feature flag stratejisi
- Healthcheck + readiness endpoint
- Merkezi loglama + alarm kriterleri
- Error tracking entegrasyon noktasi
- Deploy runbook ve incident playbook

---

## 9) Dokumantasyon Standardi (Genisletilmis)

Her expert proje sonunda:

- `README.md` (kurulum + mimari + hizli baslangic)
- `docs/USAGE.md` (urun kullanim rehberi)
- `docs/ARCHITECTURE.md` (sistem tasarimi)
- `docs/SECURITY.md` (guvenlik politikasi)
- `docs/OPERATIONS.md` (deploy, izleme, rollback)
- `docs/TEST_STRATEGY.md` (test yaklasimi)
- `docs/API_CONTRACT.md` veya OpenAPI ciktisi
- `docs/ADMIN_STANDARD.md` (admin modulleri ve kabul kriterleri)

---

## 10) Kalite Kapisi (Teslim Oncesi)

Zorunlu checklist:

- [ ] Kritik/yuksek guvenlik bulgusu yok
- [ ] Kalite kapisi puani >= 85
- [ ] Guvenlik skoru >= 85
- [ ] UI/UX skoru >= 85
- [ ] Admin modulleri ve akislari eksiksiz
- [ ] RBAC + audit log aktif
- [ ] Dashboard expert kriterleri tamam
- [ ] Dokumantasyon paketleri tam ve guncel

Bu maddeler gecmeden proje "teslime hazir" kabul edilmez.

---

## 11) Ajan Entegrasyon Notu

Bu dokuman onaylandiginda asagidaki entegrasyon onerilir:

1. `/proje_basla` komutuna `expert_mode=true` varsayilani eklenir.
2. `/proje_tasarim` bu dokumandaki UI kriterlerini checklist olarak kullanir.
3. `/proje_eksik_tara` admin ve tasarim odakli daha genis checklist tarar.
4. `/proje_kalite_kapisi` puanlamasi bu dokuman KPI'lariyla esitlenir.
5. `/proje_guvenlik_tara` RBAC/audit/headers/rate-limit maddelerini zorunlu denetler.

Bu sekilde ajan, varsayilan olarak basit proje yerine expert seviye urun cikarir.
