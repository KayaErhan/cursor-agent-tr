# /git_agent_update - Agent Komutlarini Guncelle

Bu komut, ajanin komut/rule setini git reposundan guncelleyip mevcut ortama senkronlar.

---

## Amac

- Uzak repoda yeni surum var mi kontrol et
- Varsa repoyu guncelle (`git pull`)
- **Yeni veya degisen** `.cursor/commands` ve `.cursor/rules` dosyalarini tespit et
- Bu dosyalar varsa kullaniciya **sormadan** global kopyalama yapma; asagidaki soruyu kullan

---

## Is Akisi

1. Git repo kontrolu:
   - `git status` ile yerel degisiklikleri kontrol et.
   - Yerel degisiklik varsa once raporla; otomatik overwrite yapma.
2. Pull oncesi referans:
   - `git rev-parse HEAD` ile mevcut commit hash’ini not al (`ONCEKI_COMMIT`).
3. Uzak kontrol:
   - `git fetch origin`
   - Local ile remote commit farkini kontrol et.
4. Guncelleme:
   - Guncelleme varsa `git pull --ff-only` uygula.
   - Fast-forward mumkun degilse sebebi raporla.
5. Degisen dosya tespiti (pull basarili ve commit ilerlediyse):
   - `git diff --name-only ONCEKI_COMMIT..HEAD -- .cursor/commands .cursor/rules` ile listele.
   - Veya `git log -1 --name-only` / `git show --name-only --pretty="" HEAD` ile son commit’te bu yollarda degisen dosyalari al.
   - Bos degilse: asagidaki **kullanici onayi** adimina gec.
6. Kullanici onayi (yeni veya guncellenen komut/rule **varsa** — zorunlu):
   - Otomatik olarak `~/.cursor/commands` veya `~/.cursor/rules` altina **kopyalama yapma**.
   - Kullaniciya **acikca** su anlamda sor (metin serbest ama soru sart):

     > "Yeni veya guncellenen komut veya kural dosyalari var. Bunlari global Cursor klasorune (`~/.cursor/commands`, `~/.cursor/rules`) eklemek veya mevcut dosyalari bu surumle degistirmek istiyor musunuz?"

   - Kullanici **evet** derse:
     - Windows: `$env:USERPROFILE\.cursor\commands` ve `$env:USERPROFILE\.cursor\rules`
     - macOS/Linux: `~/.cursor/commands` ve `~/.cursor/rules`
     - Eksik klasorleri olustur; ilgili dosyalari repodan kopyala.
   - Kullanici **hayir** veya netleştirme istemezse: sadece repodaki dosyalarin listesini ve yolunu raporla; global kopyalama yapma.
7. Proje bazli kullanim:
   - Repodaki `.cursor/commands/*.md` ve `.cursor/rules/*.md` zaten proje acikken aktif olur; bunu kullaniciya hatirlat.
8. Dogrulama:
   - Yeni veya guncellenen komut dosyalarini isim bazinda listele.
   - `/` menusunda gorunmesi gereken komutlari raporla.

---

## Guvenlik Kurali

- Yerel degisiklik varsa otomatik reset/revert yapma.
- Destructive git komutlari kullanma (`reset --hard`, force pull vb.).
- Global kopyalama **yalnizca** kullanici onayindan sonra.
- Hata durumunda raporla ve kullaniciya secenek sun.

---

## Cikti Formati

Sonuc mesajinda su alanlar olmali:

- Guncelleme durumu: `guncel` / `guncellendi` / `hata`
- Onceki commit -> yeni commit
- `.cursor/commands` ve `.cursor/rules` icinde degisen dosya listesi (yoksa "degisiklik yok")
- **Yeni veya guncellenen komut/rule varsa:** kullaniciya soruldu mu ve cevap (evet/hayir/beklemede)
- Senkronlanan komut/rule sayisi (onaylansa global, yoksa sadece repo)
