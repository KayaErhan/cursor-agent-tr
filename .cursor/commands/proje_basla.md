# /proje_basla - Projeyi Uca Kadar Otonom Baslat

Kullanicinin verdigi dokumana dayanarak projeyi minimum eforla calisir hale getir. Adimlari sirasiyla ve otomatik yurut; kritik belirsizlik disinda durma.

---

## 0) On Hazirlik ve Tasarim Modu

1. Dokumani oku, proje tipini belirle (web, api, cli, mobil).
2. `/docs/TODO.md` yoksa olustur; varsa koru ve devam et.
3. `/proje_tasarim` mantigini uygula:
   - Kullanici tercihi belirtilmisse onu kullan.
   - Belirtilmemisse varsayilan: `kurumsal`.
4. Tum UI islerinde Tailwind CSS kullan.

> Tasarim profili `/docs/DESIGN_PROFILE.md` dosyasina kaydedilmeli.

---

## 1) Analiz ve Planlama

- `/docs/ANALYSIS.md` dosyasina su basliklarla net analiz yaz:
  - Proje amaci
  - Kullanici rolleri
  - Fonksiyonel gereksinimler
  - Fonksiyonel olmayan gereksinimler
  - Riskler
  - Basari kriterleri
- `/docs/FLOWCHART.md` dosyasina mimari ve veri akis diyagrami ekle (Mermaid veya ASCII).

---

## 2) Ilk TODO Uretimi (Zorunlu)

Dokumandan ilk gorev havuzunu kesin olarak uret ve `/docs/TODO.md` dosyasina yaz.

Her gorev satiri su standarda uymali:

`[ ] GOREV-XXX | Baslik | Bagimlilik: ... | Oncelik: Yuksek/Orta/Dusuk | Durum: Bekliyor`

Ek olarak:
- Kategoriye gore grupla: Altyapi, Backend, Frontend, Admin, Test, Dokumantasyon, DevOps.
- Baslangicta en az 1 aktif gorev sec ve `Durum: Devam Ediyor` yap.

---

## 3) Gelistirme Dongusu

Her gorev icin:
1. Gorevi uygula.
2. Ilgili testleri calistir.
3. Gorev satirini `[x]` yap ve kisa sonuc notu dus.
4. Sonraki goreve gec.

Kritik kural:
- Bir gorev tamamlandiginda TODO tablosundaki sayisal ozeti guncelle (toplam, tamamlanan, devam eden, bekleyen).

---

## 4) Tasarim Sonrasi Otomatik Eksik Taramasi (Zorunlu)

Ilk calisan surum olustuktan hemen sonra otomatik `eksik tarama` yap ve sonucu manuel komut beklemeden uygula:

1. Kod, test, guvenlik, UX, performans, erisilebilirlik ve dokumantasyon aciklarini tara.
2. Buldugun eksikleri `/docs/GAP_REPORT.md` dosyasina siniflandir:
   - Kritik
   - Onemli
   - Iyilestirme
3. Bu eksikleri otomatik olarak `/docs/TODO.md` dosyasina yeni gorevler olarak ekle.
4. Eklenen gorevleri oncelige gore uygula.

Bu adim atlanamaz.

---

## 5) Sonlandirma Paketleri

- `/docs/TEST_REPORT.md` guncelle.
- `/docs/STATUS_REPORT.md` guncelle.
- `/README.md` ve `/docs/USAGE.md` dosyalarini gercek cikan yapiya gore guncelle.
- Kurulum veya calistirma adimlarinda eksik varsa tamamla.

---

## 6) Teslim Kurali

Teslim etmeden once:
- TODO'da kritik ve onemli acik gorev kalmamis olmali.
- Uygulama en az bir kez bastan sona calistirilmis olmali.
- Kullaniciya hangi eksiklerin kapatildigi net raporlanmali.

Son mesaj formati:
- Yapilanlar
- Kalan dusuk oncelikli maddeler
- Bir sonraki komut onerisi (`/proje_durum`, `/proje_test`, `/proje_bitir`)
