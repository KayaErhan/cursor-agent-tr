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

---

## Uygulama Kurallari (Tailwind CSS Zorunlu)

Her iki profilde de:
- Tailwind CSS kullan
- Responsive tasarim
- Dark/light mode
- Erisilebilirlik (kontrast, focus state, klavye gezinimi)

### Kurumsal Profil
- Daha premium tipografi hiyerarsisi
- Daha belirgin spacing sistemi
- Kart, tablo, form, dashboard gorunumunde yuksek detay
- Daha guclu durum/uyari bilesenleri

### Standart Profil
- Daha sade ve hizli gelistirme odakli
- Dengeli ama daha az gorsel yogunluk
- Temiz ve minimum bilesen seti

---

## Dosyalama

Secilen profil ve uygulama notlarini `/docs/DESIGN_PROFILE.md` dosyasina yaz.
Tasarimla ilgili eksikler varsa TODO'ya otomatik ekle.
