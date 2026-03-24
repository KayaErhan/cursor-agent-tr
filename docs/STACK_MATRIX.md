# Stack Oneri Matrisi

Bu dosya, secilen yazilim dili/framework ve SQL tercihlerine gore ajanin kullanacagi varsayilan paket onerilerini tanimlar.

## 1) Dil ve Framework Onerileri

| Dil | Framework (Web) | API Alternatifi | Not |
|---|---|---|---|
| TypeScript/JavaScript | Next.js | NestJS / Express | Varsayilan web stack |
| Python | Django | FastAPI | Hizli API gelistirme icin FastAPI uygun |
| PHP | Laravel | Slim | Laravel tam kapsamli |
| Java | Spring Boot | Spring Boot | Kurumsal projelerde guclu |
| C# | ASP.NET Core | ASP.NET Core | Microsoft ekosistemi icin uygun |
| Go | Gin | Fiber | Yalniz API odakli projelerde hizli |

## 2) SQL ve Veri Erişim Onerileri

| SQL / Veritabani | ORM / Data Layer Onerisi | Surucu / Not |
|---|---|---|
| PostgreSQL | Prisma / Drizzle / SQLAlchemy / Eloquent | Olgun, varsayilan tercih |
| MySQL | Prisma / TypeORM / SQLAlchemy / Eloquent | Yaygin barindirma uyumu |
| SQLite | Prisma / SQLAlchemy / Eloquent | Kucuk proje ve prototip |
| MSSQL | TypeORM / Sequelize / EF Core | Kurumsal ortamlarda yaygin |

## 3) Test ve Kalite Onerileri

| Dil | Test | Lint/Format |
|---|---|---|
| TS/JS | Vitest / Jest + Playwright | ESLint + Prettier |
| Python | Pytest | Ruff + Black |
| PHP | PHPUnit / Pest | Pint / PHP-CS-Fixer |
| Java | JUnit | Checkstyle / Spotless |
| C# | xUnit / NUnit | dotnet format |
| Go | go test | golangci-lint + gofmt |

## 4) UI ve Tasarim Onerileri (Web UI varsa)

- Tailwind CSS (zorunlu)
- lucide-react (ikon)
- recharts (grafik)
- framer-motion (mikro-animasyon)

## 5) Secim Kurali

1. Kullanici secimi varsa onu esas al.
2. Secim yoksa varsayilan:
   - Dil/Framework: TypeScript + Next.js
   - SQL: PostgreSQL
3. Projede halihazirda tutarli bir stack varsa zorla degistirme.
4. Eksik araclar kritik degilse TODO/GAP'a "onemli iyilestirme" olarak ekle.
