<!-- validate_quality kanonik: /proje_incele | Dil/Framework + SQL | /proje_tasarim | /proje_basla | /proje_eksik_tara | /proje_devam | /proje_test | /proje_kalite_kapisi | /proje_guvenlik_tara | /proje_bitir -->
# /proje_basla - Workflow Tabanli Ana Gelistirme

Bu komut, artik **n8n benzeri workflow yapisinin gelistirme odakli parcasi** gibi davranir.
Tam orkestrasyon icin tercih edilen komut: `/proje_workflow`.

Amac:
- Döküman analizi ve tasarimdan sonra gelistirme fazini hizli baslatmak.
- Gerekirse `docs/WORKFLOW_STATE.md` icindeki adimi `dev` veya sonrasi icin ilerletmek.

---

## 0) On Hazirlik ve State Kontrolu

1. `docs/WORKFLOW_STATE.md` dosyasi yoksa:
   - `current_step = "analysis"` olacak sekilde yeni bir state olustur.
   - Kullaniciya tam otomatik ilerlemek icin esas komutun `/proje_workflow` oldugunu belirt.
2. Eger state varsa:
   - `current_step` degerini kontrol et.
   - `analysis` veya `design` ise:
     - Kisa bir ozetle bu adimlari tamamlamaya calis veya kullaniciya `/proje_workflow` komutunu onermeyi dusun.

---

## 1) TODO Tabanli Gelistirme Baslatma

1. `/docs/TODO.md` yoksa olustur; varsa iceriğini ve formatini koru.
2. Proje dokumanindan ve mevcut analizden yola cikarak:
   - Altyapi, Backend, Frontend, Admin, Test, Dokumantasyon, DevOps kategorilerinde gorevler ekle.
3. Her gorev satiri icin su formata yakin kal:

   `[ ] GOREV-XXX | Baslik | Bagimlilik: ... | Oncelik: Yuksek/Orta/Dusuk | Durum: Bekliyor`

4. En az bir gorevi `Durum: Devam Ediyor` yap ve bu gorevden baslayarak:
   - Kod yaz.
   - Ilgili testleri calistir.
   - Gorev satirini `[x]` yap ve kisa sonuc notu ekle.

---

## 2) UI ve Admin Panel Odaklari

1. Admin panel icin:
   - Sol sidebar + topbar yapisini uygula.
   - Topbar icinde bildirim, email/mesaj ve profil alanlarini planla.
   - Dashboard icin KPI kartlari, grafikler ve son aktiviteleri tasarla.
2. Tum UI islerinde Tailwind CSS kullan.
3. Gerekirse asagidaki kutuphaneleri oner:
   - Ikonlar icin: `lucide-react`
   - Grafikler icin: `recharts`
   - Mikro animasyonlar icin: `framer-motion`

---

## 3) Workflow State Ile Guncelleme

- Eger gelistirme adiminda anlamli ilerleme kaydedildiyse:
  - `docs/WORKFLOW_STATE.md` dosyasini guncelle:
    - `current_step` degeri, hala gelistirme asamasinda kalabilir (`"dev"`),
      veya bir sonraki adima hazir isen, kullaniciya `/proje_workflow` komutuyla
      siradaki adima gecilecegini belirt.
  - `last_command` alanini `/proje_basla` olarak yaz.

---

## 4) Son Mesaj

Kullaniciyi bilgilendirirken:
- Olusturulan veya guncellenen gorevler (adet ve kategori bazinda ozet).
- Tamamlanan gorevler ve kilit fonksiyonlar.
- Admin/UI tarafinda yapilan gelistirmelerden kisa bir liste.
- Onerilen sonraki komut:
  - Tam otomatik akisa devam icin: `/proje_workflow`
  - Ayni adimda derinlesmek icin: `/proje_devam`

