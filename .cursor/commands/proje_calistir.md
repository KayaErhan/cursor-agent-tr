# /proje_calistir - Gelistirme Sunucusunu Calistir

Acik olan proje klasorunde uygulamayi **yerel gelistirme modunda** calistir; bagimlilik ve stack tespitini yap; cikti URL/port bilgisini ozetle.

---

## Amaç

- Kullanicinin elle komut arastirmasina gerek kalmadan `dev` / `start` surecini baslatmak.
- Uzun sure calisan sureci (HTTP sunucusu vb.) terminalde **arka planda** tutmak; chat cevabinda hangi komutun kullanildigini ve nasil durdurulacagini belirtmek.

---

## 0) Kok Dizin

- Calisma dizini: kullanicinin Cursor’da actigi **workspace kok dizini** (veya kullanici baska bir alt klasor belirttiyse o).

---

## 1) Stack Tespiti (sirayla bak)

Asagidakilerden ilk esleseni temel al; gerekirse `README.md`, `docs/USAGE.md`, `Makefile`, `compose.yaml` / `docker-compose.yml` dosyalarini oku.

| Isaret | Onerilen komut (once bagimlilik) |
|--------|----------------------------------|
| `package.json` + `pnpm-lock.yaml` | `pnpm install` (gerekirse) → `pnpm dev` veya `pnpm run dev` / `scripts` icindeki `dev` |
| `package.json` + `yarn.lock` | `yarn` → `yarn dev` |
| `package.json` (diger) | `npm install` → `npm run dev` |
| `bun.lock` / `bunfig.toml` | `bun install` → `bun run dev` |
| `Cargo.toml` (Rust) | `cargo run` veya README’deki dev komutu |
| `go.mod` | `go run .` veya Makefile/README |
| `docker-compose.yml` veya `compose.yaml` | `docker compose up` (gerekirse `--build`) |
| `Makefile` ve `make dev` / `make run` var | `make dev` |

- `package.json` icinde `scripts.dev` yoksa sirayla dene: `dev`, `start`, `serve`, `develop` veya README’de yazan script adi.
- Monorepo ise (or. `apps/web`): once kullaniciya veya `package.json` workspace yapisina gore **dogru alt paket** dizinine `cd` et.

---

## 2) Bagimlilik

- Node projesinde `node_modules` yoksa veya eksik modul hatasi bekleniyorsa once paket yoneticisi ile kurulum calistir.
- Python ise `requirements.txt` / `pyproject.toml` varsa sanal ortam + kurulum adimlarini README’ye uygun uygula.

---

## 3) Sunucuyu Baslat

- **Bloklamayan** uzun sureli komutlari terminal araciligiyla calistir (ornegin arka plan / `block_until_ms: 0` ile); chat cevabinda kullaniciya **hangi terminalde** calistigini soyle.
- Ilk birkac saniyelik logdan **port ve URL** cikarmaya calis (or. `localhost:3000`, `127.0.0.1:5173`).
- Port mesgul ise: hatayi raporla; mumkunse farkli port (or. `PORT=3001`) ile tekrar denemeyi degerlendir veya kullaniciya net cozum yaz.

---

## 4) Dokumantasyon

- Projede `/docs/USAGE.md` veya `README.md` icinde “Nasil calistirilir” bolumu yoksa veya komut yanlis ise, **sadece bu bilgiyi** guncelle; gereksiz genis dokumasyon ekleme.

---

## 5) Son Mesaj Ozeti

- Calistirilan komut(lar) (tam satir).
- Tahmini erisim URL’si (veya Docker icin map edilen port).
- Durdurmak icin: `Ctrl+C` ilgili terminalde veya `docker compose down` vb.

---

## Sonraki Adim Onerileri

- Kod degisikligi sonrasi yeniden derleme: ayni komutu tekrar `/proje_calistir` veya dosya kaydina bagli hot-reload.
- Veritabani veya imaj/Compose kurulumu: `/proje_docker`
- Test: `/proje_test`
- Durum: `/proje_durum`
