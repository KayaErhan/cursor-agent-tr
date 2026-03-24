# /proje_incele - Dokuman Analizi ve Otomatik Gorev Cikarma

Dokumani derin analiz et ve sadece raporlama yapma; otomatik TODO altyapisini da hazirla.

---

## Baslangicta Sorulacak Teknik Tercihler (Zorunlu)

Kullanicidan su iki tercihi net sor:

1. Yazilim dili / framework tercihi nedir?
   - Ornek: TypeScript + Next.js, Python + Django, PHP + Laravel
2. SQL/veritabani tercihi nedir?
   - Ornek: PostgreSQL, MySQL, SQLite, MSSQL

Eger kullanici cevap vermezse:
- Dil varsayilani: `TypeScript + Next.js`
- SQL varsayilani: `PostgreSQL`

Secimi `/docs/ANALYSIS.md` ve `/docs/TECH_STACK.md` dosyalarina yaz.

---

## Zorunlu Ciktilar

1. `/docs/ANALYSIS.md`
   - Problem tanimi
   - Hedef kitle
   - Kapsam / kapsam disi
   - Teknik stack onerisi
   - Risk analizi
2. `/docs/FLOWCHART.md`
   - Sistem mimarisi
   - Veri akis diyagrami
3. `/docs/TODO.md`
   - Analizden cikarilan ilk gorev listesi
   - Bagimliliklar ve oncelikler
4. `/docs/TECH_STACK.md`
   - Secilen yazilim dili / framework
   - Secilen SQL/veritabani
   - Neden bu secim yapildi
   - Alternatifler (kisa)
5. `/docs/STACK_MATRIX.md`
   - Dile gore framework onerileri
   - Dile gore test/kalite araci onerileri
   - Veritabaniya gore ORM/surucu onerileri

---

## Eksik Yakalama Kurali

Analiz sonrasinda "muhtemel unutulanlar" taramasi yap:
- Auth/Yetki
- Hata yonetimi
- Loglama
- Performans
- Guvenlik
- Erisilebilirlik
- Dokumantasyon

Bulunan her eksigi TODO'ya otomatik gorev olarak ekle.

---

## Cikti Formati

Son mesaja su netlikte yaz:
- Tahmini toplam gorev
- Kritik risk sayisi
- Otomatik eklenen eksik gorev sayisi
- Onerilen sonraki komut: `/proje_basla`
