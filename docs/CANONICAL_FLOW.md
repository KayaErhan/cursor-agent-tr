# Kanonik kullanım sırası

Özet: döküman → analiz → dil/SQL → tasarım → geliştirme → eksik tarama → devam → test → kalite kapısı → güvenlik → teslim.

**Token maliyeti:** Bu sırayı README veya USAGE içinde tekrar etmeyin; buraya link verin.

---

## validate_quality doğrulaması

Aşağıdaki satırlar `scripts/validate_quality.py` tarafından **bu dosyada** sırayla aranır (tek kaynak):

/proje_incele
Dil/Framework + SQL
/proje_tasarim
/proje_basla
/proje_eksik_tara
/proje_devam
/proje_test
/proje_kalite_kapisi
/proje_guvenlik_tara
/proje_bitir

---

## İnsan okuması için kısa akış

| Adım | Komut veya adım | Not |
|------|-----------------|-----|
| 1 | `/proje_incele` | Döküman analizi |
| 2 | Dil/Framework + SQL | Stack netliği |
| 3 | `/proje_tasarim` | Profil + tema |
| 4 | `/proje_basla` veya `/proje_workflow` | Geliştirme / süper workflow |
| 5 | `/proje_eksik_tara` | Gap |
| 6 | `/proje_devam` | Kapanmayan kritikler |
| 7 | `/proje_test` | Test |
| 8 | `/proje_kalite_kapisi` | Kalite |
| 9 | `/proje_guvenlik_tara` | Güvenlik |
| 10 | `/proje_bitir` | Teslim |

İsteğe bağlı: `/proje_durum`, `/proje_calistir`, `/proje_docker`, `/git_agent_update`.
