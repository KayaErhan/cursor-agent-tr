# /proje_kalite_kapisi - Kurumsal Kalite Kapisi

Projeyi bir sonraki asamaya gecirmeden once asagidaki kalite kapilarini zorunlu kontrol et.
Puanlama ve kontrol maddeleri `/docs/EXPERT_PRODUCT_STANDARD.md` ile uyumlu olmalidir.

---

## Kapilar

1. Build kapisi
   - Proje build aliyor mu?
2. Test kapisi
   - Kritik testler geciyor mu?
3. Guvenlik kapisi
   - Kritik guvenlik acigi var mi?
4. Tasarim kapisi
   - UI kalite standardi saglandi mi?
   - Design token + component katmanlari tam mi?
   - Admin panel expert ekran agaci tamam mi?
5. Dokumantasyon kapisi
   - README/USAGE/TODO/GAP tutarli mi?

---

## Puanlama (100)

- Build: 20
- Test: 25
- Guvenlik: 25
- Tasarim: 20
- Dokumantasyon: 10

Esikler:
- 85+ -> Gec
- 70-84 -> Sartli gecis (TODO'ya zorunlu iyilestirme)
- 0-69 -> Gecemez, duzeltme zorunlu

Zorunlu blokaj:
- Guvenlik skoru < 85 ise gecemez
- UI/UX skoru < 85 ise gecemez
- Kritik/yuksek guvenlik bulgusu varsa gecemez

---

## Cikti

Raporu `/docs/QUALITY_GATE_REPORT.md` dosyasina yaz:
- Toplam puan
- Gecen/kalan kapilar
- Bloke eden maddeler
- Onerilen sonraki komut (`/proje_devam` veya `/proje_bitir`)
