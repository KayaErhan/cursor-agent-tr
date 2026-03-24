# /proje_durum — Mevcut Geliştirme Durumunu Göster

`/docs/TODO.md` dosyasını oku ve projenin anlık durumunu aşağıdaki formatta sun.

---

## Durum Raporu Formatı

### 📊 Genel İlerleme
```
Toplam Görev   : XX
Tamamlanan     : XX  ✅
Devam Eden     : XX  🔄
Bekleyen       : XX  ⏳
İlerleme       : %XX  [████████░░░░] 
```

### ✅ Tamamlanan Görevler
Son tamamlanan 5 görevi listele.

### 🔄 Şu An Üzerinde Çalışılan
Aktif görevin adı, açıklaması ve tahmini bitiş süreci.

### ⏳ Sıradaki Görevler
Bir sonraki 3 görevi öncelik sırasıyla listele.

### ⚠️ Engelleyen Sorunlar
Bekleyen bağımlılıklar, hatalar veya çözüm bekleyen durumlar.

### 📁 Oluşturulan Dosyalar
Bu güne kadar oluşturulan önemli dosyaları listele.

---

Raporu `/docs/STATUS_REPORT.md` dosyasına da kaydet.
