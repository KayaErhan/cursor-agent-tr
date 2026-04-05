# Docker ile yerel kurulum (isteğe bağlı)

Bu klasör, ajanın varsayılan stack’i (**PostgreSQL**) ile uyumlu, **isteğe bağlı** Docker Compose tanımlarını içerir. Cursor kuralları veya `/proje_docker` komutu ile üretilen uygulama projelerinde veritabanını konteynerda çalıştırmak için kullanılır.

## Ne zaman kullanılır?

- Yerelde PostgreSQL kurmak istemiyorsanız.
- Ekip içinde aynı DB sürümünü (ör. 16) paylaşmak istiyorsanız.
- Üretilen Next.js / Node projesinin `DATABASE_URL` değerini bu servise bağlamak istiyorsanız.

## Hızlı başlangıç

1. `docker/env.example` dosyasını `docker/.env` olarak kopyalayın ve şifreleri değiştirin.
2. Proje kökünden:

```bash
docker compose -f docker/compose.yml up -d
```

3. Bağlantı örneği (uygulama `.env` içinde):

```text
DATABASE_URL=postgresql://app:app@localhost:5432/app
```

`POSTGRES_*` değerlerini `docker/.env` ile aynı tutun.

## pgAdmin (isteğe bağlı)

```bash
docker compose -f docker/compose.yml --profile tools up -d
```

Tarayıcı: `http://localhost:5050` (varsayılan; `PGADMIN_PORT` ile değişir.)

## Durdurma ve veri

```bash
docker compose -f docker/compose.yml down
```

Kalıcı veriyi de silmek için: `docker compose -f docker/compose.yml down -v`

## Uygulama imajı

Saf veritabanı dosyası burada bırakıldı; web uygulaması için `Dockerfile` üretimi `/proje_docker` komutu veya geliştirme sürecinde istenerek eklenir.
