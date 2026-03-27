# /git_agent_update - Agent Komutlarini Guncelle

Bu komut, ajanin komut/rule setini git reposundan guncelleyip mevcut ortama otomatik senkronlar.

---

## Amac

- Uzak repoda yeni surum var mi kontrol et
- Varsa repoyu guncelle (`git pull`)
- Guncellenen `.cursor/commands` ve `.cursor/rules` icerigini aktif kullanim konumuna kopyala

---

## Is Akisi

1. Git repo kontrolu:
   - `git status` ile yerel degisiklikleri kontrol et.
   - Yerel degisiklik varsa once raporla; otomatik overwrite yapma.
2. Uzak kontrol:
   - `git fetch origin`
   - Local ile remote commit farkini kontrol et.
3. Guncelleme:
   - Guncelleme varsa `git pull --ff-only` uygula.
   - Fast-forward mumkun degilse sebebi raporla.
4. Komut senkronu:
   - Proje bazli kullanimda: repodaki `.cursor/commands/*.md` ve `.cursor/rules/*.md` zaten aktif olur.
   - Global kullanim istenirse:
     - `~/.cursor/commands` ve `~/.cursor/rules` altina kopyala.
5. Dogrulama:
   - Yeni komut dosyalarini listele.
   - `/` menusunda gorunmesi gereken komutlari raporla.

---

## Guvenlik Kurali

- Yerel degisiklik varsa otomatik reset/revert yapma.
- Destructive git komutlari kullanma (`reset --hard`, force pull vb.).
- Hata durumunda raporla ve kullaniciya secenek sun.

---

## Cikti Formati

Sonuc mesajinda su alanlar olmali:

- Guncelleme durumu: `guncel` / `guncellendi` / `hata`
- Onceki commit -> yeni commit
- Senkronlanan komut/rule sayisi
- Gorunmesi beklenen yeni komutlar (varsa)
