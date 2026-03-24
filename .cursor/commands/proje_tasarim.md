# /proje_tasarim - Tasarim Profili Sec ve Uygula

Projenin tasarim tarzini kullanicidan secmesini iste ve secime gore butun UI katmanina uygula.

---

## Kullaniciya Sorulacak Secim

Soru:
`Tasarim profili secin: kurumsal mi, standart mi?`

Secenekler:
- `kurumsal` (varsayilan)
- `standart`

Kullanici cevap vermezse `kurumsal` uygula.

Ikinci soru:
`Tema modu secin: dark, soft-dark, light, yoksa hepsi mi?`

Secenekler:
- `dark`
- `soft-dark`
- `light`
- `hepsi` (varsayilan)

Uygulama kurali:
- `hepsi` secilirse tema gecis anahtari (switcher) zorunlu.

---

## Uygulama Kurallari (Tailwind CSS Zorunlu)

Her iki profilde de:
- Tailwind CSS kullan
- Responsive tasarim
- Secilen tema modlari (dark / soft-dark / light)
- Erisilebilirlik (kontrast, focus state, klavye gezinimi)
- Zengin renk paleti (primary, secondary, accent, success, warning, danger)
- Ikon seti ile tutarli ikonografi
- Gorunur durum bilesenleri (badge, alert, toast, progress, skeleton)
- Kartlar, tablolar, formlar ve modallar icin tutarli tasarim sistemi

## Onerilen UI Kutuphane Politikasi

UI kaliteyi sabitlemek icin asagidaki paketleri tercih et:

- `lucide-react` -> ikon sistemi (zorunluya yakin, varsayilan)
- `recharts` -> dashboard grafik bilesenleri (line/bar/donut)
- `framer-motion` -> mikro-animasyon ve sayfa gecisleri

Uygulama kurali:
- Projede denk bir kutuphane zaten varsa onu bozma, mevcut standardi koru.
- Hicbir UI kutuphanesi yoksa yukaridaki 3'lu seti varsayilan olarak kur.
- Grafik/ikon/animasyon ihtiyaci oldugu halde kutuphane kullanilmadiysa bunu eksik olarak TODO ve GAP raporuna ekle.

## Admin Paneli Zorunlu UI Standarti

- Sol menulu (left sidebar) yapi zorunlu.
- Sidebar her zaman solda ve tutarli; desktop'ta sabit, mobilde acilir-kapanir.
- Ust bar (topbar) icinde en az:
  - Bildirim merkezi
  - Email/mesaj kisayolu
  - Profil menusu
- Dashboard ana ekraninda:
  - KPI kartlari
  - En az 3 farkli grafik (line/bar/donut)
  - Son aktiviteler
  - Hizli islem butonlari
- Grafikler gercek veri yoksa ornek/veri taklit (mock) ile dolu gorunmeli.

## Site Tarafi UI Standarti (Varsa)

- Hero, ozellik kartlari, CTA, referanslar/istatistik, SSS ve footer bolumleri.
- Gorsel hiyerarsi guclu, bosluk/typography dengeli ve premium hisli.
- Ikon ve dekoratif gorsel kullanimi zorunlu (asiriya kacmadan).
- Sayfa gecisleri ve mikro-animasyonlar yumusak olmali.

### Kurumsal Profil
- Daha premium tipografi hiyerarsisi
- Daha belirgin spacing sistemi
- Kart, tablo, form, dashboard gorunumunde yuksek detay
- Daha guclu durum/uyari bilesenleri
- Renk kontrasti yuksek, marka hissi guclu
- Daha zengin cam/gradient/golge kombinasyonlari (abartisiz)

### Standart Profil
- Daha sade ve hizli gelistirme odakli
- Dengeli ama daha az gorsel yogunluk
- Temiz ve minimum bilesen seti
- Yine de duz ve renksiz gorunum kabul edilmez; temel renk ve ikon dili korunur

---

## Dosyalama

Secilen profil ve uygulama notlarini `/docs/DESIGN_PROFILE.md` dosyasina yaz.
Tasarimla ilgili eksikler varsa TODO'ya otomatik ekle.
Tasarim kalite kontrol sonucunu `/docs/GAP_REPORT.md` dosyasina da ekle.
