# /proje_workflow - n8n Benzeri Super Workflow Komutu

Bu komut, projeyi **n8n tarzi adim adim workflow** ile yonetir. Hedef:
- Kullanici icin tek komut: `/proje_workflow`
- Gerektiginde sadece `/proje_devam` ile ayni adimda devam edebilmek
- Kritik noktalarda en fazla **1 net soru sorup** sonra varsayilanlarla ilerlemek

Detayli komut sirasi (insan okumasi): `docs/CANONICAL_FLOW.md`.

---

## Temel Mantik

1. `docs/WORKFLOW_STATE.md` dosyasini oku.
2. `current_step` alanina gore siradaki adimi belirle.
3. Her adimda asagidaki bolumdeki **referans komut dosyasinin** mantigini uygula (tam metin orada); kullanicidan ayri ayri slash yazmasini bekleme.
4. Adim sonunda DoD saglaniyorsa `completed_steps` + sonraki `current_step`; degilse `blocked_by` notu.

Varsayilan adim sirasi:

`analysis` → `design` → `dev` → `gap_scan` → `continue` → `test` → `quality_gate` → `security` → `finish`

---

## Adimlara Gore Davranis

Her adimda olusturulacak/guncellenecek dosyalar ve DoD tanimlari icin: **`docs/WORKFLOW_DOD.md`** ilgili baslik.

### 1) analysis

- Uygula: **`.cursor/commands/proje_incele.md`**
- Ciktilar: `docs/ANALYSIS.md`, `docs/TECH_STACK.md`, `docs/STACK_MATRIX.md`
- Dil/framework ve SQL net degilse **en fazla 1 soru**; yoksa `TypeScript + Next.js` + `PostgreSQL`.

### 2) design

- Uygula: **`.cursor/commands/proje_tasarim.md`**
- Cikti: `docs/DESIGN_PROFILE.md` (kurumsal/standart, tema modlari; admin UI kurallari ozeti).

### 3) dev

- `docs/TODO.md` ile gorevler; en az birini `Devam Ediyor` yapip kod uret; admin/landing iskeleti.

### 4) gap_scan

- Uygula: **`.cursor/commands/proje_eksik_tara.md`**
- Cikti: `docs/GAP_REPORT.md`; kritik/onemli maddeler `TODO.md` ile bagla.

### 5) continue

- Uygula: **`.cursor/commands/proje_devam.md`** mantigi (TODO kritik/onemli kapat, `STATUS_REPORT.md`).

### 6) test

- Uygula: **`.cursor/commands/proje_test.md`**
- Cikti: `docs/TEST_REPORT.md`

### 7) quality_gate

- Uygula: **`.cursor/commands/proje_kalite_kapisi.md`**
- Mumkunse `scripts/validate_quality.py`; cikti `docs/QUALITY_GATE_REPORT.md`; state bayraklari.

### 8) security

- Uygula: **`.cursor/commands/proje_guvenlik_tara.md`**
- Cikti: `docs/SECURITY_REPORT.md`; kritik/yuksek cozum veya `blocked_by`.

### 9) finish

- Uygula: **`.cursor/commands/proje_bitir.md`**
- `/setup` veya `/config`; final `STATUS_REPORT.md`; README/USAGE tutarlilik ozeti.

---

## /proje_devam Iliskisi

`/proje_devam`: `WORKFLOW_STATE.current_step` ile ayni adimda derinlesme (DoD tamamlanmadan).

`/proje_workflow`: State’e gore **siradaki** adimi calistirir.

---

## Ilk Calistirma

`WORKFLOW_STATE.md` yoksa olustur: `current_step = "analysis"`, `completed_steps = []`.

Kullaniciya: tek komut `/proje_workflow`; ara sira `/proje_devam`; adim sirasi `docs/CANONICAL_FLOW.md` ile uyumlu ozetlenebilir.
