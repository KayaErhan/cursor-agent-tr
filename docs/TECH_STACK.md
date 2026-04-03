# Teknik Stack Secimi - Spor Tesisi Projesi

## Dil ve Framework

- Secilen: **TypeScript + Next.js** (varsayilan web full-stack)
- Neden:
  - SSR/ISR ile hizli ve SEO dostu deneyim
  - Admin panel + landing sayfasi ayni projede yonetilebilir

## Veritabani ve ORM

- Secilen SQL/DB: **PostgreSQL**
- Onerilen ORM / Data katmani:
  - Next.js icin: **Prisma** veya **Drizzle**

## Test ve Kalite

- Test:
  - **Vitest** veya **Jest** (unit/integration)
  - **Playwright** (E2E, admin panel ve rezervasyon akislarini test icin)
- Lint/Format:
  - **ESLint + Prettier**

## UI ve Tasarim

- CSS: **Tailwind CSS** (zorunlu)
- Ikonlar: **lucide-react**
- Grafikler: **recharts**
- Mikro-animasyonlar: **framer-motion**

## Secim Kurali Notu

- Kullanici farkli bir dil/DB belirtmedigi icin, `docs/STACK_MATRIX.md` kurallarina gore
  varsayilan kombinasyon olan **TypeScript + Next.js + PostgreSQL** uygulanmistir.

