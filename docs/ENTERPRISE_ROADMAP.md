# Enterprise Roadmap

Bu yol haritasi, mevcut yapiyi kurumsal urun seviyesine cikarmak icin 3 fazli uygulama planini tanimlar.

## Durum Legend

- `done`: tamamlandi
- `in-progress`: aktif calisiliyor
- `pending`: henuz baslanmadi

## Faz 1 (Hizli Kazanim - 1 Hafta)

| Madde | Durum |
|---|---|
| Kalite kapisi komutunu devreye al (`/proje_kalite_kapisi`) | done |
| Guvenlik tarama komutunu devreye al (`/proje_guvenlik_tara`) | done |
| Cikti sozlesmelerini standartlastir (TODO/GAP/TEST/STATUS) | in-progress |
| Design token/tema standardini netlestir | in-progress |

Hedef:
- Tutarli ciktı
- Daha az regressions
- Teslim oncesi net kalite karari

## Faz 2 (Orta Vade - 1 Ay)

| Madde | Durum |
|---|---|
| RBAC matrisini varsayilan hale getir | in-progress |
| Audit log ve activity timeline modulu | in-progress |
| CI/CD iskeleti olusturma (lint-test-build-security) | pending |
| Release checklist ve rollback plani | pending |

Hedef:
- Kurumsal guvenlik ve operasyon hazirligi
- Takimlar arasi standardizasyon

## Faz 3 (Olgunluk - 1 Ceyrek)

| Madde | Durum |
|---|---|
| Sektor bazli blueprint kutuphanesi (SaaS, CRM, e-ticaret, portal) | pending |
| Performans butcesi ve izleme metrikleri | pending |
| Komut telemetri ve KPI dashboard | pending |
| Coklu dil (tr/en) raporlama standardi | pending |

Hedef:
- Tekrarlanabilir urun kalitesi
- Olceklendirilebilir ekip kullanim modeli
