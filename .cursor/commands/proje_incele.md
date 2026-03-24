# /proje_incele - Dokuman Analizi ve Otomatik Gorev Cikarma

Dokumani derin analiz et ve sadece raporlama yapma; otomatik TODO altyapisini da hazirla.

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
