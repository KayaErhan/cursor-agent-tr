# /proje_durum - Anlik Durum ve Sonraki Aksiyon

`/docs/TODO.md`, `/docs/GAP_REPORT.md` ve `/docs/STATUS_REPORT.md` dosyalarini kullanarak durumu tek yerde ozetle.

---

## Zorunlu Rapor Basliklari

1. Genel Ilerleme
2. Son Tamamlanan 5 Gorev
3. Su Anki Aktif Gorev
4. Sonraki 5 Gorev (oncelik sirali)
5. Engeller / Riskler
6. Gap Raporundan acik kalan kritik maddeler
7. Kalite kapisi puani (varsa)
8. Guvenlik raporu ozeti (varsa)
9. Onerilen tek sonraki komut

---

## Onerilen Komut Mantigi

- Kritik eksik varsa: `/proje_devam`
- Test acigi varsa: `/proje_test`
- Tum gorevler kapandiysa: `/proje_kalite_kapisi`
- Kalite kapisi gectiyse: `/proje_guvenlik_tara`
- Guvenlik taramasi temizse: `/proje_bitir`

Raporu `/docs/STATUS_REPORT.md` dosyasina tarih damgasiyla kaydet.
