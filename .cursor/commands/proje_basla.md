# /proje_basla - Workflow Tabanli Ana Gelistirme

Bu komut gelistirme fazini hizli baslatir. **Tam otomasyon ve coklu TODO dalgasi** icin **`/proje_orkestra`** kullanin.

`/proje_basla` yazildiginda:
- Kisa yol: `current_step = dev` ise **`proje_orkestra.md` dalga kotasi** (min 3 gorev) uygula.
- Tam surec: kullaniciya `/proje_orkestra` oner (tek komut, durmadan devam).

Tam orkestrasyon: `/proje_orkestra` veya `/proje_workflow` (alias).


---

## 0) On Hazirlik ve State Kontrolu

1. `docs/WORKFLOW_STATE.md` dosyasi yoksa:
   - `current_step = "analysis"` olacak sekilde yeni bir state olustur.
   - Kullaniciya tam otomatik ilerlemek icin esas komutun `/proje_orkestra` oldugunu belirt.
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

   `[ ] GOREV-XXX | Baslik | Agent: implementation-agent | Oncelik: Yuksek/Orta/Dusuk | Durum: Bekliyor | Bagimlilik: yok`

4. **Dalga kotasi:** tek gorevde durma; en az **3** gorevi ayni oturumda isle (`docs/AGENT_CONTRACTS.md`).
5. Her gorev icin: kod yaz, test calistir, `[x]` + kanit notu.

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
      veya bir sonraki adima hazir isen, `/proje_orkestra` ile devam edilecegini belirt.
  - `last_command` alanini `/proje_basla` olarak yaz.

---

## 4) Son Mesaj

Kullaniciyi bilgilendirirken:
- Olusturulan veya guncellenen gorevler (adet ve kategori bazinda ozet).
- Tamamlanan gorevler ve kilit fonksiyonlar.
- Admin/UI tarafinda yapilan gelistirmelerden kisa bir liste.
- Onerilen sonraki komut:
  - Tam otomatik akisa devam icin: `/proje_orkestra` veya `/proje_workflow`
  - Ayni adimda derinlesmek icin: `/proje_devam`

