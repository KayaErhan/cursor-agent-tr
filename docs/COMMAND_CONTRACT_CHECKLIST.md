# Command Contract Checklist

Bu checklist, README/USAGE iddialari ile komut dosyasi davranislarinin uyumunu denetlemek icin kullanilir.

## 1) Akis Sozlesmesi

Asagidaki siralama README, USAGE ve `.cursor/commands/proje_basla.md` icinde ayni olmalidir:

1. `/proje_incele`
2. Dil/Framework + SQL secimi
3. `/proje_tasarim`
4. `/proje_basla`
5. `/proje_eksik_tara`
6. `/proje_devam`
7. `/proje_test`
8. `/proje_kalite_kapisi`
9. `/proje_guvenlik_tara`
10. `/proje_bitir`

## 2) Komut-Referans Sozlesmesi

- README/USAGE'de gecen tum `/proje_*` komutlari `.cursor/commands/` altinda gercek dosya olarak bulunmali.

## 3) TODO Sozlesmesi

- `docs/TODO.md` formati:
  - `[ ] GOREV-XXX | ... | Bagimlilik: ... | Oncelik: Yuksek/Orta/Dusuk | Durum: ...`
- `DevOps` bolumu zorunlu.
- En az bir gorev `Durum: Devam Ediyor` olmali.

## 4) Bitiş Sozlesmesi

- `/proje_bitir` icinde config/setup uretimi zorunlu adim olarak tanimli olmali:
  - `/setup` veya `/config`
  - `.env`/guvenli config senkronu
  - zorunlu alanlar

## 5) Link/Placeholder Sozlesmesi

- Markdown lokal linkleri kirik olmamali.
- `KULLANICI_ADIN` gibi placeholderlar yayinlanan dokumanda kalmamali.

---

## Otomasyon

Bu checklist maddeleri `scripts/validate_quality.py` ile otomatik denetlenir.
