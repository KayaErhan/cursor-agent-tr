# Changelog

Bu proje [Semantic Versioning](https://semver.org/lang/tr/) kullanır.

---

## [Unreleased] — Orkestra v2

### Eklenenler
- `/proje_orkestra` — çoklu subagent, dalga kotası (min 3 TODO), otomatik devam
- `.cursor/agents/` — 10 uzman subagent tanımı
- `docs/ORCHESTRATION_ARCHITECTURE.md`, `AGENT_CONTRACTS.md`, `FILE_OWNERSHIP.md`
- `scripts/validate_orchestra.py` — orkestra yapısal doğrulama
- `WORKFLOW_STATE` schema v2 (resume, dalga, dosya sahipliği)

### Değişiklikler
- `agent.md` — Orkestra Şefi rolü; tek-iki madde durma yasağı
- `/proje_workflow`, `/proje_devam`, `/proje_basla` — orkestraya delegasyon
- TODO v2 satır formatı (`Agent:` alanı)

---

## [1.0.0] — 2025-03-24

### Eklenenler
- `/proje_basla` — 7 aşamalı tam otomatik geliştirme komutu
- `/proje_incele` — Döküman analizi ve ön değerlendirme komutu
- `/proje_durum` — Anlık ilerleme raporu komutu
- `/proje_test` — Kapsamlı test ve uyum kontrolü komutu
- `/proje_bitir` — Proje sonlandırma ve teslim komutu
- `/proje_sifirla` — Temizle ve sıfırla komutu
- `.cursor/rules/agent.md` — Sistem kuralları ve davranış tanımı
- `scripts/install.sh` — Otomatik kurulum scripti
- `docs/USAGE.md` — Detaylı kullanım kılavuzu
- `docs/examples/` — Örnek proje dökümanları

---

*Yeni sürümler için bu dosyayı takip edin.*
