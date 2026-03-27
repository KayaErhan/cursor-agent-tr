# /proje_bitir - Projeyi Kapat ve Teslim Et

Projeyi teslime kapatmadan once final kalite kapisini uygula.

---

## Final Kalite Kapisi

1. `/docs/TODO.md` icinde kritik ve onemli acik gorev var mi kontrol et.
2. Acik varsa otomatik tamamlamayi dene; tamamlanamayanlari net raporla.
3. `/docs/GAP_REPORT.md` icindeki kritikler kapandi mi kontrol et.
4. `/docs/TEST_REPORT.md` son sonucunu guncelle.
5. `/docs/QUALITY_GATE_REPORT.md` sonucu en az 85 mi kontrol et.
6. `/docs/SECURITY_REPORT.md` icinde kritik/yuksek acik kalmadi mi kontrol et.

---

## Config/Setup Uretimi (Zorunlu)

Teslimden once asagidaki adimlar zorunludur:

1. `/setup` veya `/config` rotasinda calisan bir konfigurasyon ekrani olustur.
2. En az su alanlari icersin:
   - Veritabani: host, port, database, user, password
   - SMTP: host, port, user, password, sender
   - Uygulama: app url, timezone, locale
3. Kaydetme akisinda bilgiler `.env` (veya esdeger guvenli config dosyasi) ile senkronlansin.
4. Gerekirse "baglanti testi" butonlari eklenerek dogrulama saglansin.
5. Bu adim tamamlanmadan proje "teslime hazir" raporlanamaz.

---

## Cikti Paketleri

- `/README.md`
- `/docs/USAGE.md`
- `/docs/ANALYSIS.md`
- `/docs/STATUS_REPORT.md`
- `/CHANGELOG.md`

Bu dosyalarin hepsi son durumla tutarli olmali.

---

## Teslim Ozeti (Zorunlu Format)

`Proje Teslim Ozeti` basligi altinda:
- Tamamlanan gorev orani
- Kapatilan eksik sayisi
- Kalan dusuk oncelik maddeler
- Calistirma komutu
- Config/setup yolu
