# /proje_workflow - n8n Benzeri Super Workflow Komutu

Bu komut, projeyi **n8n tarzi adim adim workflow** ile yonetir. Hedef:
- Kullanici icin tek komut: `/proje_workflow`
- Gerektiginde sadece `/proje_devam` ile ayni adimda devam edebilmek
- Kritik noktalarda en fazla **1 net soru sorup** sonra varsayilanlarla ilerlemek

---

## Temel Mantik

1. `docs/WORKFLOW_STATE.md` dosyasini oku.
2. `current_step` alanina gore siradaki adimi belirle.
3. Her adim icin:
   - Ilgili cikti dosyalarini ve `WORKFLOW_DOD.md` icindeki DoD'leri baz alarak ne yapman gerektigini planla.
   - Gerekliyse ilgili yardimci komutlarin (proje_incele, proje_tasarim, proje_eksik_tara, proje_devam, proje_test, proje_kalite_kapisi, proje_guvenlik_tara, proje_bitir) kurallarini uygula, fakat kullanicidan ayni komutlari tekrar yazmasini bekleme.
4. Adim sonunda:
   - DoD saglaniyorsa:
     - `completed_steps` listesine ekle.
     - `current_step`'i bir sonrakine guncelle.
   - DoD saglanmiyorsa:
     - Ayni adimda kal, `blocked_by` alanina kisa bir not yaz.

Varsayilan adim sirasi:

1. `analysis`
2. `design`
3. `dev`
4. `gap_scan`
5. `continue`
6. `test`
7. `quality_gate`
8. `security`
9. `finish`

---

## Adimlara Gore Davranis

### 1) analysis

- Yapilacaklar:
  - Proje dokumanini analiz et (gerekirse `/proje_incele` mantigini uygula).
  - `docs/ANALYSIS.md`, `docs/TECH_STACK.md`, `docs/STACK_MATRIX.md` dosyalarini olustur/guncelle.
  - Yazilim dili/framework ve SQL/DB secimi icin:
    - Eger zaten belirgin degilse **1 kez soru sor**.
    - Cevap yoksa varsayilan: `TypeScript + Next.js` ve `PostgreSQL`.
  - Secilenleri `docs/TECH_STACK.md` ve ilgili yerlerde belirt.
- DoD icin referans: `docs/WORKFLOW_DOD.md` icindeki `analysis` bolumu.

### 2) design

- Yapilacaklar:
  - `/proje_tasarim` mantigini kullanarak:
    - Tasarim profili (`kurumsal` / `standart`) icin 1 soru sor; cevap yoksa `kurumsal`.
    - Tema modu (`dark` / `soft-dark` / `light` / `hepsi`) icin 1 soru sor; cevap yoksa `hepsi`.
  - `docs/DESIGN_PROFILE.md` dosyasina profil ve tema secimlerini kaydet.
  - Admin panel icin:
    - Sol menulu sidebar
    - Topbar icinde bildirim, email/mesaj ve profil alani
    - Dashboard icin KPI kartlari, grafikler ve son aktiviteler
    - Tailwind CSS, ikon kutuphanesi (ornegin `lucide-react`), grafik icin (`recharts`), animasyon icin (`framer-motion`) onerilerini yaz.
- DoD icin referans: `design` bolumu.

### 3) dev

- Yapilacaklar:
  - `docs/TODO.md` uzerinden kapsamli gorev listesi olustur:
    - Altyapi, backend, frontend, admin, test, dokumantasyon, DevOps kategorileri.
  - En az bir gorevi `Durum: Devam Ediyor` yap ve bu gorevden baslayarak kod olustur.
  - Admin panel, landing vs. icin temel sayfalari ve yapilari olustur.
- DoD icin referans: `dev` bolumu.

### 4) gap_scan

- Yapilacaklar:
  - `/proje_eksik_tara` mantigini kullanarak:
    - Kod, test, guvenlik, UX, performans, erisilebilirlik ve dokumantasyon aciklarini tara.
    - Tasarim ve admin kalite checklistlerini kullan.
  - Sonuclari `docs/GAP_REPORT.md` dosyasina yaz:
    - Kritik / Onemli / Iyilestirme seviyelerinde.
  - Kritik ve onemli tum maddeleri `docs/TODO.md` icine gorev olarak ekle.
- DoD icin referans: `gap_scan` bolumu.

### 5) continue

- Yapilacaklar:
  - `docs/TODO.md` icindeki Kritik ve Onemli maddeleri ele al:
    - Uygula, test et, gorev durumlarini guncelle.
  - `docs/STATUS_REPORT.md` icine:
    - Kapatilan kritik/onemliler,
    - Kalan kritik/onemli maddeler,
    - Iyilestirme seviyesindeki maddelerden ozet yaz.
- Dogrudan kod ve dokuman gelistirmeye devam et; kullanicidan ekstra komut bekleme.
- DoD icin referans: `continue` bolumu.

### 6) test

- Yapilacaklar:
  - Mimariye uygun sekilde temel testleri calistir veya olustur:
    - Birim/fonksiyonel testler.
    - Gerekliyse basit entegrasyon testleri.
  - `docs/TEST_REPORT.md` dosyasini yaz/guncelle.
- DoD icin referans: `test` bolumu.

### 7) quality_gate

- Yapilacaklar:
  - `/proje_kalite_kapisi` mantigini kullan:
    - Build, test, guvenlik, tasarim, dokumantasyon icin puanlama yap (toplam 100 uzerinden).
  - Sonucu `docs/QUALITY_GATE_REPORT.md` dosyasina yaz.
  - Mümkünse `scripts/validate_quality.py` calistirilmis kabul edilerek:
    - Komut/dokuman tutarliligi ve kritik placeholder/kirik link sorunlarini ele al.
  - `docs/WORKFLOW_STATE.md` icinde `quality_validated` bayragini guncelle.
- DoD icin referans: `quality_gate` bolumu.

### 8) security

- Yapilacaklar:
  - `/proje_guvenlik_tara` mantigini kullan:
    - RBAC, girdiler, yaygin web aciklari, gizli bilgi yonetimi, HTTP header'lar, rate limiting, audit log, PII maskesi vb.
  - Sonuclari `docs/SECURITY_REPORT.md` dosyasina yaz.
  - Kritik/Yuksek maddeler varsa:
    - Cozum uretmeye calis.
    - Cozumlenemeyenler icin `blocked_by` alanina acik not birak.
  - `docs/WORKFLOW_STATE.md` icinde `security_validated` bayragini guncelle.
- DoD icin referans: `security` bolumu.

### 9) finish

- Yapilacaklar:
  - Onceki tum adimlarin DoD'lerinin saglandigini kontrol et.
  - Config/setup ekraninin hazir oldugunu dogrula (`/setup` veya `/config`):
    - DB, SMTP vb. icin alanlar.
    - Basit baglanti testi akisi varsa acikla.
  - `docs/STATUS_REPORT.md` final ozetini guncelle:
    - Yapilanlar, kalan dusuk oncelikli maddeler, bilinen kisitlar.
  - README ve USAGE dokumanlarinin gercek ciktiya uygun oldugunu kisaca gozden gecir.
- Son kullaniciya verilecek mesajda:
  - `Yapilanlar`
  - `Kalan dusuk oncelikli maddeler`
  - `Bir sonraki adim onerisi` net yazilmali.

---

## /proje_devam Ile Iliski

- `/proje_devam` komutu calistiginda:
  - `docs/WORKFLOW_STATE.md` icindeki `current_step` degeri kullanilir.
  - Eger adimin DoD'si saglanmadiysa, ayni adimda daha fazla derinlesmek icin kullanilir (ozellikle `dev`, `gap_scan`, `continue`, `test`, `quality_gate`, `security`).
- `/proje_workflow` komutu ise:
  - Mevcut state'e bakarak **sıradaki mantikli adimi** calistirir.
  - Boylece kullanici genellikle sadece `/proje_workflow` ve gerekirse `/proje_devam` komutlarini kullanarak neredeyse n8n benzeri bir akisi deneyimler.

---

## Ilk Calistirma Davranisi

Eger `docs/WORKFLOW_STATE.md` dosyasi yoksa veya bos/bozuksa:
- Yeni bir state olustur:
  - `current_step = "analysis"`
  - `completed_steps = []`
  - Diger alanlari bos/varsayilandaki gibi ayarla.
- Kullaniciya kisaca acikla:
  - "Yeni workflow baslatildi. Adim sirasi: analysis → design → dev → gap_scan → continue → test → quality_gate → security → finish. Genelde sadece /proje_workflow ve ara sira /proje_devam komutlarini kullanman yeterli."

