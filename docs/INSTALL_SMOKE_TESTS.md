# Install Smoke Test Senaryolari

Bu dokuman, `scripts/install.sh` icin temel smoke test senaryolarini listeler.

## Kapsam

- Global kurulum
- Proje bazli kurulum
- Hatali path senaryosu
- Komut gorunurluk dogrulamasi

---

## Senaryo 1 - Global Kurulum

1. Repo kokunde:
   - `bash scripts/install.sh`
2. Secim: `1` (Global)
3. Beklenen:
   - `~/.cursor/commands` altina komut dosyalari kopyalanir
   - `~/.cursor/rules` altina `agent.md` kopyalanir
   - Komut listesi terminalde gorunur

## Senaryo 2 - Proje Bazli Kurulum

1. Test icin bos bir proje klasoru olustur.
2. `bash scripts/install.sh`
3. Secim: `2` (Yerel)
4. Hedef path olarak test klasorunu ver.
5. Beklenen:
   - `<hedef>/.cursor/commands` olusur ve dosyalar kopyalanir
   - `<hedef>/.cursor/rules` olusur ve dosyalar kopyalanir

## Senaryo 3 - Hatali Path

1. `bash scripts/install.sh`
2. Secim: `2`
3. Var olmayan bir klasor path'i ver.
4. Beklenen:
   - Script hata verip cikis kodu 1 ile sonlanir.

## Senaryo 4 - Komut Gorunurluk Kontrolu

Kurulum sonrasi Cursor chat panelinde `/` yazip su komutlarin gorunurlugunu kontrol et:

- `/proje_incele`
- `/proje_basla`
- `/proje_durum`
- `/proje_test`
- `/proje_eksik_tara`
- `/proje_devam`
- `/proje_tasarim`
- `/proje_kalite_kapisi`
- `/proje_guvenlik_tara`
- `/proje_bitir`

---

## Ek Not

Smoke testler manuel checklist olarak tanimlanmistir. Ilerleyen asamada CI ortaminda script tabanli hale getirilebilir.
