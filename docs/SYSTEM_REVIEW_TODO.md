# Sistem Inceleme TODO Listesi

Bu liste, son denetimde cikan bulgularin uygulanabilir is maddelerine donusturulmus halidir.
Durum ve karar kolonlarini birlikte doldurabiliriz.

---

## Karar Legend

- Karar: `YAP`, `ERTELE`, `IPTAL`
- Durum: `[ ]` Bekliyor, `[-]` Karar Bekliyor, `[x]` Tamamlandi

---

## A) Kritik ve Yuksek Oncelik

[x] TODO-001 | README dosya agacindaki `docs/examples/blog.md` tutarsizligini gider | Karar: YAP | Oncelik: KRITIK  
Not: Dosya gercekten eklenecek mi, yoksa referans kaldirilacak mi?

[x] TODO-002 | `docs/TODO.md` formatini `proje_basla` standartlariyla birebir hizala (`Durum`, ID, oncelik vb.) | Karar: YAP | Oncelik: YUKSEK  
Not: Komutlarin bekledigi tek format tanimlanmali.

[x] TODO-003 | `DevOps` kategori uyumsuzlugunu gider (`proje_basla` <-> `docs/TODO.md`) | Karar: YAP | Oncelik: YUKSEK  
Not: Ya kategori zorunlu kilinsin ya komuttan cikarilsin.


---

## B) Orta Oncelik

[ ] TODO-005 | `scripts/install.sh` icin script-konumu bazli guvenli path cozumu ekle (`SCRIPT_DIR`) | Karar: IPTAL | Oncelik: ORTA  
Not: Farkli dizinden calistirmada kirilmamali.

[ ] TODO-006 | `scripts/install.sh` icin yedek/confirm mekanizmasi ekle (global kurulum overwrite riski) | Karar: IPTAL | Oncelik: ORTA  
Not: Mevcut kullanici komutlari kaybolmamali.

[x] TODO-007 | `README`, `USAGE`, `proje_basla` arasinda tek kanonik asama akisi belirle ve senkronla | Karar: YAP | Oncelik: ORTA  
Not: Asama sayisi ve adlari birebir ayni olmali.

[x] TODO-008 | `proje_bitir` komutuna config/setup ekrani uretimini net zorunlu adim olarak ekle (veya dokumanda iddiayi yumusat) | Karar: YAP | Oncelik: ORTA  
Not: Urun vaadi ile davranis ayni olmali.

---

## C) Dusuk Oncelik (Kalite Iyilestirme)

[x] TODO-009 | `agent.md` icin karar onceligi ekle ("kritik soru zorunlu, digerleri opsiyonel") | Karar: YAP | Oncelik: DUSUK

[x] TODO-010 | `docs/ENTERPRISE_ROADMAP.md` durum bazli hale getir (`done/in-progress/pending`) | Karar: YAP | Oncelik: DUSUK

---

## D) Test ve Otomasyon Bosluklari

[x] TODO-011 | Komut dokumanlari icin tutarlilik denetimi ekle (referans dosya var mi, asama adlari uyumlu mu) | Karar: YAP | Oncelik: ORTA

[x] TODO-012 | Dokumantasyon placeholder/kirik link kontrolu ekle | Karar: YAP | Oncelik: ORTA

[x] TODO-013 | `install.sh` icin smoke test senaryolari ekle | Karar: YAP | Oncelik: ORTA

[x] TODO-014 | TODO formati icin sema/regex dogrulama ekle | Karar: YAP | Oncelik: ORTA

[x] TODO-015 | README/USAGE iddialari ile komut davranisi arasinda sozlesme checklist testi ekle | Karar: YAP | Oncelik: ORTA

---

## E) Birlikte Karar Icin Onerilen Siralama

1. TODO-001, TODO-004 (hizli guvenilirlik duzeltmeleri)
2. TODO-002, TODO-003 (otomasyon format tutarliligi)
3. TODO-005, TODO-006 (kurulum guvenligi)
4. TODO-007, TODO-008 (davranis-dokuman uyumu)
5. Test otomasyonu (TODO-011..015)
