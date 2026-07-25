# WORKFLOW Definition of Done (DoD)

Bu dosya, n8n benzeri workflow mantigi icin her adimin *bitmis sayilmasi* icin minimum kriterleri tanimler.

## Ortak Kurallar

- Her adim tamamlandiginda `docs/WORKFLOW_STATE.md` guncellenmeli:
  - `current_step` bir sonrakine gecmeli.
  - `completed_steps` listesine eklenmeli.
  - Gerekirse `blocked_by` ve `last_error` temizlenmeli.
- Kritik sorular:
  - Sadece teknik yonde kritik belirsizlikler icin 1 net soru sor.
  - Cevap yoksa, tanimli varsayilanlari kullan ve devam et.

---

## 1. analysis (Inceleme)

Bitmis sayilmasi icin:
- `docs/ANALYSIS.md` olusmus ve asagidaki basliklar doldurulmus olmali:
  - Proje amaci
  - Kullanici rolleri
  - Fonksiyonel gereksinimler
  - Fonksiyonel olmayan gereksinimler
  - Riskler
  - Basari kriterleri
- `docs/TECH_STACK.md` olusmus olmali:
  - Yazilim dili/framework secimi net.
  - SQL/veritabani secimi net.
- `docs/STACK_MATRIX.md` dikkate alinarak ana paket/araç oneri seti yazilmis olmali (uygulandi/ileride uygulanacak seklinde).

---

## 2. design (Tasarim)

Bitmis sayilmasi icin:
- `docs/DESIGN_PROFILE.md` olusmus olmali:
  - Tasarim profili: `kurumsal` veya `standart`.
  - Tema modu: `dark`, `soft-dark`, `light` veya `hepsi`.
- Admin panel kurallari net yazilmis olmali:
  - Sol menulu sidebar.
  - Topbar icinde bildirim, email/mesaj ve profil bolumu.
  - Dashboard icin KPI kartlari, grafikler ve son aktiviteler/olaylar.
- UI icin minimum kalite notlari tanimlanmis olmali:
  - Tailwind CSS zorunlu.
  - Renk paleti, ikon seti (`lucide-react` gibi) ve temel bilesen seti belirlendi.

---

## 3. dev (Gelistirme)

Bitmis sayilmasi icin:
- `docs/TODO.md` olusmus olmali:
  - Altyapi, backend, frontend, admin, test, dokumantasyon, DevOps kategorilerinden gorevler.
  - Satir formati (v2 oncelikli): `GOREV-XXX | ... | Agent: ... | Oncelik: ... | Durum: ... | Bagimlilik: ...`
  - Eski format da kabul edilir (`docs/AGENT_CONTRACTS.md`).
  - Gorevlerde `Agent:` ve dosya sahipligi atanmis olmali (orkestra).
- **Orkestra dalga kotasi:** `dev` icinde en az **bir oturumda 3+** gorev islenmis ve kanitlanmis olmali (`WORKFLOW_STATE.tasks_completed_this_wave` veya TODO `[x]`).
- Ilk temel moduller icin kod taslagi (admin, landing, ornek API).

---

## 4. gap_scan (Eksik Tarama)

Bitmis sayilmasi icin:
- `docs/GAP_REPORT.md` olusmus olmali:
  - Kritik / Onemli / Iyilestirme olarak siniflandirilmis maddeler var.
  - Tasarim ve admin standartlari icin eksik tespiti yapilmis:
    - Renk/ikon, admin layout, bildirim/email, dashboard grafik ve KPI, tema uyumu vb.
- Kritik ve onemli tum maddeler `docs/TODO.md` icine yeni gorevler olarak eklenmis olmali.

---

## 5. continue (Eksiklerden Devam)

Bitmis sayilmasi icin:
- Kritik ve onemli TODO maddelerinin buyuk cogu kapatilmaya calisilmis olmali.
- **Orkestra:** `/proje_orkestra` veya `/proje_devam` cagrisi basina **min 3 gorev** kotasi uygulanmis olmali (tek gorevde durma yasagi).
- `docs/STATUS_REPORT.md` guncel.

---

## 6. test (Test)

Bitmis sayilmasi icin:
- En azindan su seviyelerde test stratejisi uygulanmis olmali:
  - Birim veya fonksiyonel testler (mimariye uygun sekilde).
  - Temel entegrasyon testi (veritabani veya ana API ile).
- `docs/TEST_REPORT.md` olusmus olmali:
  - Calistirilan test tipleri.
  - Basarili/hatali durumlar.
  - Kritik hatalar var ise kisa aciklama.

---

## 7. quality_gate (Kalite Kapisi)

Bitmis sayilmasi icin:
- `docs/QUALITY_GATE_REPORT.md` olusmus olmali:
  - Build, test, guvenlik, tasarim ve dokumantasyon icin puanlama yapilmis.
  - Toplam skor en az 85 uzerinden olmus veya altindaysa net olarak nedenleri yazili.
- `scripts/validate_quality.py` **ve** `scripts/validate_orchestra.py` calistirilmis kabul edilmeli.

---

## 8. security (Guvenlik)

Bitmis sayilmasi icin:
- `docs/SECURITY_REPORT.md` olusmus olmali:
  - RBAC, girdiler, yaygin web aciklari, gizli bilgi yonetimi, log temizlik kurallari icin kontrol notlari var.
  - Bulunan sorunlar Kritiklik seviyesine gore (Kritik, Yuksek, Orta, Dusuk) isaretlenmis.
- Kritik ve Yuksek seviye sorunlar icin:
  - Ya cozum uygulanmis olmali.
  - Ya da `blocked_by` alaninda acikca neden cozumlenemedigi yazilmis olmali (teslimi engeller).

---

## 9. finish (Bitirme)

Bitmis sayilmasi icin:
- Tum oncesi adimlarin DoD'leri saglanmis olmali.
- `docs/STATUS_REPORT.md` final durumla guncellenmis olmali:
  - Yapilanlar, kalan dusuk oncelikli maddeler, bilinen kisitlar.
- Config/setup tarafi hazir olmali:
  - `/setup` veya `/config` rotasi.
  - Temel baglanti ayarlari (DB, SMTP vb.) icin alanlar.
  - Mümkünse temel baglanti testi akisi.
- Kullaniciya son mesajda:
  - Yapilanlar, kalanlar ve bir sonraki adim onerisi net yazilmis olmali.

