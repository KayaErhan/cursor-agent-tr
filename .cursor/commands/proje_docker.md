# /proje_docker - Docker Kurulumu ve Konteyner Yapisi

Kullanici Docker kurulumu veya konteynerlestirme istediginde projeye uygun **Dockerfile**, **Compose**, **.dockerignore** ve **ortam degiskeni** dokumantasyonunu ekle veya guncelle.

---

## Amaç

- Veritabani ve yardimci servisleri Compose ile ayaga kaldirmak (bu repoda sablon: `docker/compose.yml`).
- Gerekirse uygulama (or. Next.js) icin **uretim veya gelistirme** Dockerfile’i eklemek.
- `README.md` ve `docs/USAGE.md` icinde Docker bolumunu guncel tutmak.

---

## 0) Kapsam

- **Zorunlu degildir**; kullanici istemedikce Docker dosyasi ekleme.
- Bu repoda hazir **PostgreSQL + istege bagli pgAdmin** sablonu `docker/` altindadir; baska projede ayni yapiyi kopyalayabilir veya uyarlayabilirsin.

---

## 1) Stack Tespiti

- `package.json`, `next.config.*`, `Dockerfile` varligi, mevcut `docker-compose.yml` / `compose.yml` dosyalarini kontrol et.
- Veritabani `PostgreSQL` ise `docker/compose.yml` sablonu ile uyumlu `DATABASE_URL` ornegi ver.

---

## 2) Veritabani (PostgreSQL)

- Projede henuz yoksa ve kullanici DB’yi Docker’da istiyorsa:
  - `docker/compose.yml` ve `docker/env.example` yapisini kullan veya projeye uyarla.
  - Kok veya `docker/.env` icin `env.example` icerigini senkron tut.
- Saglik kontrolu (`healthcheck`) ve kalici volume kullanimini koru.

---

## 3) Uygulama Dockerfile (Next.js / Node)

- Istendiginde cok asamali Dockerfile ekle:
  - Bagimlilik kurulumu, `next build`, `node` ile calistirma veya `standalone` cikti.
- Root `.dockerignore` ekle: `node_modules`, `.git`, `.next`, `*.md` gereksizleri haric tut.
- Compose icinde `app` servisi eklenecekse `postgres`’e `depends_on` ve ortak ag kullan.

---

## 4) Guvenlik

- Ornek sifreleri dokumantasyonda **degistirilmesi gerektigini** belirt.
- Gercek sifreleri repoya commit etme; `.env` gitignore’da olmali.

---

## 5) Dokumantasyon

- Proje `README.md`: "Docker ile calistirma" basligi, komutlar, portlar.
- `docs/USAGE.md` veya `docker/README.md`: baglanti URL’leri ve profil (`--profile tools`) aciklamasi.

---

## 6) Son Mesaj

- Eklenen dosyalarin listesi.
- Calistirma komutlari (`docker compose ...`).
- Sonraki adim: `/proje_calistir` (yerel) veya container icinde test.
