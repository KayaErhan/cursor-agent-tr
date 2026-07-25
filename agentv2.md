CURSOR AGENT ORKESTRASYON SİSTEMİ — REPOYU UÇTAN UCA GELİŞTİRME TALİMATI

Bu görev yalnızca analiz veya öneri üretme görevi değildir.

Bu repoyu doğrudan incele, gerekli dosyaları oluştur, mevcut dosyaları güncelle, sistemi test et ve çalışan bir çoklu agent orkestrasyon altyapısı haline getir.

Çalıştığın repo:

KayaErhan/cursor-agent-tr

Bu repo bir uygulama projesi değil, Cursor içinde farklı yazılım projelerini A'dan Z'ye tamamlayacak bir agent framework projesidir.

1. Ana hedef

Mevcut tek-agent ve sıralı workflow yapısını, Cursor’ın güncel native subagent özelliklerini kullanan bir Orkestra Agent Sistemi v2 mimarisine dönüştür.

Kullanıcı bir proje dokümanı, fikir, görev veya mevcut kod tabanı verdiğinde sistem:

Projeyi analiz etmeli.
Eksik ve belirsiz gereksinimleri belirlemeli.
Teknik mimariyi hazırlamalı.
Tasarım sistemini hazırlamalı.
Ayrıntılı TODO listesi oluşturmalı.
Görevleri uzman agent’lara dağıtmalı.
Uygun görevleri paralel çalıştırmalı.
Kodlamayı gerçekleştirmeli.
Testleri çalıştırmalı.
Hataları otomatik düzeltmeli.
TODO ile gerçek kod durumunu karşılaştırmalı.
Eksik kalan işleri yeniden TODO’ya eklemeli.
Kritik ve önemli işler bitene kadar geliştirmeye devam etmeli.
Güvenlik, kalite, tasarım ve dokümantasyon kontrollerini yapmalı.
Projenin gerçekten teslim edilebilir olduğunu doğrulamalı.
Yarım kalan bir çalışma varsa state dosyalarından tespit edip kaldığı yerden devam etmeli.

Sistem yalnızca plan üretip durmamalı. Projeyi mümkün olan en ileri tamamlanmış seviyeye kadar götürmelidir.

2. Mevcut yapıyı koru ve geliştir

Önce aşağıdaki mevcut dosyaları ve aralarındaki ilişkileri ayrıntılı biçimde incele:

.cursor/rules/agent.md
.cursor/commands/proje_workflow.md
.cursor/commands/proje_basla.md
.cursor/commands/proje_devam.md
.cursor/commands/proje_durum.md
.cursor/commands/proje_eksik_tara.md
.cursor/commands/proje_tasarim.md
.cursor/commands/proje_test.md
.cursor/commands/proje_kalite_kapisi.md
.cursor/commands/proje_guvenlik_tara.md
.cursor/commands/proje_bitir.md
docs/WORKFLOW_STATE.md
docs/WORKFLOW_DOD.md
docs/CANONICAL_FLOW.md
docs/TODO.md
docs/STATUS_REPORT.md
scripts/validate_quality.py
README.md
docs/USAGE.md
CHANGELOG.md

Mevcut komutları silme veya geriye dönük uyumluluğu bozma.

Gerekli yerlerde mevcut komutları yeni orkestratör sistemine yönlendiren alias veya delegasyon komutları haline getir.

3. Native Cursor subagent yapısını oluştur

Cursor’ın kurulu sürümündeki güncel native subagent formatını kullan.

Önce mevcut Cursor sürümünün desteklediği subagent dosya formatını doğrula. Schema veya frontmatter alanlarını tahmin etme. Güncel desteklenen formata göre .cursor/agents/ altında agent dosyaları oluştur.

En az aşağıdaki uzman agent’ları oluştur:

3.1 project-discovery-agent

Görevleri:

Proje dokümanını ve mevcut kod tabanını incelemek.
Kullanıcı rollerini çıkarmak.
Fonksiyonel ve fonksiyonel olmayan gereksinimleri belirlemek.
Edge case’leri tespit etmek.
Harici servis, API, veritabanı ve entegrasyon ihtiyaçlarını çıkarmak.
Başarı kriterlerini hazırlamak.
Belirsizlikleri risk seviyesine göre sınıflandırmak.
Teknik olarak kritik olmayan konularda güvenli varsayımlar önermek.

Bu agent ağırlıklı olarak inceleme ve raporlama yapmalıdır.

3.2 todo-controller-agent

Görevleri:

docs/TODO.md dosyasının tek görev doğruluk kaynağı olmasını sağlamak.
Görev ID’lerinin benzersizliğini kontrol etmek.
Görev bağımlılıklarını doğrulamak.
Kod ile TODO durumunun uyumunu kontrol etmek.
Tamamlanmamış, yanlış işaretlenmiş veya unutulmuş görevleri bulmak.
Eksik görevleri otomatik eklemek.
Her görev için kabul kriteri ve doğrulama komutu bulunmasını sağlamak.
Sayısal ilerleme özetini güncellemek.
Sahipsiz veya bloke görevleri tespit etmek.

Merkezi TODO dosyasını aynı anda yalnızca bu agent veya ana orkestratör güncelleyebilsin.

3.3 progress-state-agent

Görevleri:

docs/WORKFLOW_STATE.md dosyasını yönetmek.
Aktif fazı, aktif agent’ları ve görev dağılımlarını kaydetmek.
Son başarıyla tamamlanan kontrol noktasını kaydetmek.
Yarım kalan işlemleri tespit etmek.
Eski veya hatalı state kayıtlarını kod ve TODO ile karşılaştırmak.
Sistemin hangi görevden devam edeceğini belirlemek.
Blocker, hata, retry ve doğrulama sonuçlarını kaydetmek.
Kullanıcı tekrar komut verdiğinde kaldığı yerden devam edilmesini sağlamak.

Merkezi state dosyasının tek yazarı bu agent veya ana orkestratör olmalıdır.

3.4 software-architect-agent

Görevleri:

Sistem mimarisini belirlemek.
Modül sınırlarını oluşturmak.
Veritabanı şemasını ve veri akışını planlamak.
API sözleşmelerini hazırlamak.
Yetkilendirme, RBAC ve audit log yapısını planlamak.
Teknik borç ve ölçeklenebilirlik risklerini belirlemek.
Mimari kararları docs/DECISIONS.md veya uygun ADR dosyalarına yazmak.
Uygulama agent’larının dosya sahipliği sınırlarını belirlemek.
3.5 ui-ux-design-agent

Görevleri:

Proje türüne uygun tasarım sistemini hazırlamak.
Renk, tipografi, spacing, ikon ve bileşen sistemini belirlemek.
Responsive davranışları tanımlamak.
Admin paneli, dashboard, form, tablo, empty state, loading state ve error state yapılarını tasarlamak.
Erişilebilirlik gereksinimlerini belirlemek.
Tasarımın yalnızca wireframe seviyesinde kalmasını engellemek.
Tasarım ile gerçek implementasyonu karşılaştırarak eksikleri raporlamak.
Gerekirse browser aracıyla ekranları incelemek.
3.6 implementation-agent

Görevleri:

Kendisine atanmış TODO görevlerini kodlamak.
Yalnızca sahipliği kendisine atanmış dosyalarda değişiklik yapmak.
Göreve başlamadan önce bağımlılıkları kontrol etmek.
Kodla birlikte gerekli testleri yazmak.
Build, lint ve type-check sonuçlarını doğrulamak.
Yaptığı değişiklikleri yapılandırılmış handoff formatında ana orkestratöre bildirmek.
Tamamlanmayan görevi tamamlanmış göstermemek.

Proje büyüklüğüne göre ana orkestratör birden fazla implementation micro-agent oluşturabilmelidir:

frontend implementation agent
backend implementation agent
database implementation agent
integration implementation agent
DevOps implementation agent

Ancak paralel agent’lar aynı dosya veya modülde eş zamanlı değişiklik yapmamalıdır.

3.7 test-qa-agent

Görevleri:

Projenin test altyapısını tespit etmek.
Birim, entegrasyon, API, UI ve smoke testlerini çalıştırmak.
Eksik testleri belirlemek.
Hata yeniden üretme adımlarını hazırlamak.
Test başarısızlıklarını kök nedenleriyle sınıflandırmak.
Test raporunu güncellemek.
Düzeltilebilir hataları ilgili implementation agent’a geri göndermek.
Test edilmemiş bir görevin tamamlanmasına izin vermemek.
3.8 security-quality-agent

Görevleri:

Güvenlik, dependency, secret, input validation, authorization ve veri erişimi kontrollerini yapmak.
RBAC’ın yalnızca arayüzde değil backend seviyesinde de uygulandığını doğrulamak.
Audit log yapısını kontrol etmek.
Build, lint, type-check, test, dokümantasyon ve kod kalitesi kapılarını değerlendirmek.
Kritik ve yüksek güvenlik sorunlarında teslimi engellemek.
Kalite puanını kanıtlarla üretmek.
Gerçekte çalıştırılmamış kontrolleri başarılı göstermemek.
3.9 completion-auditor-agent

Bu en önemli denetim agent’ıdır.

Görevleri:

“Proje tamamlandı” iddiasını bağımsız olarak doğrulamak.
Proje dokümanı ile gerçek kodu karşılaştırmak.
TODO, state, kod, testler ve dokümantasyon arasındaki tutarsızlıkları bulmak.
Placeholder, mock-only yapı, çalışmayan buton, boş sayfa, sahte API, TODO yorumları ve yarım entegrasyonları tespit etmek.
UI butonlarının gerçek aksiyonlara bağlı olup olmadığını kontrol etmek.
Route, API ve veritabanı bağlantılarını doğrulamak.
Eksik bulursa teslimi reddetmek.
Eksikleri GAP_REPORT.md ve TODO.md ile ilişkilendirmek.
Kritik ve önemli eksikler sıfırlanana kadar yeniden geliştirme döngüsü istemek.

Bu agent mümkün olduğunca read-only denetçi olarak çalışmalıdır.

3.10 documentation-release-agent

Görevleri:

README, kullanım dokümanı, kurulum, environment değişkenleri ve changelog dosyalarını güncellemek.
Gerçek implementasyonla dokümantasyonun uyumunu doğrulamak.
Çalıştırma ve test komutlarını doğrulamak.
Final teslim raporunu oluşturmak.
Bilinen kısıtları açıkça yazmak.
Proje tamamlanmadıysa “tamamlandı” ifadesi kullanmamak.
4. Ana agent “Orkestra Şefi” olsun

.cursor/rules/agent.md dosyasını yeniden düzenle.

Ana agent’ın rolü:

Kullanıcı isteğini ana hedefe çevirmek.
Hangi uzman agent’ların çalışacağını belirlemek.
Birbirinden bağımsız işleri paralel başlatmak.
Birbirine bağlı işleri doğru sıraya koymak.
Agent çıktılarını birleştirmek.
Dosya sahipliği çakışmalarını engellemek.
Merkezi state ve TODO güncellemelerini koordine etmek.
Agent sonuçlarını körü körüne kabul etmemek.
Her implementasyon dalgasından sonra test ve gap kontrolü çalıştırmak.
Proje gerçekten tamamlanana kadar döngüyü devam ettirmek.

Ana agent mümkün olan her şeyi kendisi yapmaya çalışmamalı; uzman işi uygun subagent’a devretmelidir.

Ancak yalnızca agent çağırıp bekleyen pasif bir yönetici de olmamalıdır. Sonuçları doğrulamalı ve entegrasyonu yönetmelidir.

5. Tek komutlu uçtan uca workflow oluştur

Yeni bir ana komut oluştur:

.cursor/commands/proje_orkestra.md

Kullanımı:

/proje_orkestra

Bu komut bütün workflow’u kullanıcıdan ek slash komutları beklemeden yürütmelidir.

Eski /proje_workflow komutunu geriye dönük uyumluluk için koru ancak yeni orkestrasyon sistemine yönlendir.

Akış:

Bootstrap ve resume kontrolü
Proje discovery
Gereksinim analizi
Teknik stack ve mimari
Tasarım sistemi
TODO üretimi
Bağımlılık grafiği
Agent ve dosya sahipliği dağıtımı
Paralel veya sıralı implementasyon dalgaları
Her dalga sonrası build/lint/type-check/test
TODO ve kod senkron kontrolü
Gap scan
Eksiklerin yeniden atanması
Test düzeltme döngüsü
Güvenlik kontrolü
Kalite kapısı
Completion auditor kontrolü
Gerekirse yeniden geliştirme
Dokümantasyon ve release hazırlığı
Final teslim

Sistem her faz sonunda kullanıcıdan yeni komut istememelidir.

Yalnızca aşağıdaki durumlarda kullanıcıya soru sorulabilir:

Geri döndürülemez veri kaybı riski
Gerçek ödeme veya ücretli servis işlemi
Erişim anahtarı ya da gizli bilgi zorunluluğu
Birbiriyle çelişen ve ürün davranışını kökten değiştiren gereksinimler
Hukuki veya güvenlik açısından kullanıcı kararı gerektiren durumlar

Bunların dışındaki konularda güvenli ve profesyonel varsayımlar kullanarak devam et.

6. Resume ve eksik iş devam mekanizması

Her /proje_orkestra, /proje_workflow veya /proje_devam çağrısının başında:

Git durumunu incele.
Değiştirilmiş fakat doğrulanmamış dosyaları tespit et.
WORKFLOW_STATE.md dosyasını oku.
TODO.md dosyasını oku.
Son test ve kalite raporlarını oku.
Kod ile TODO durumunu karşılaştır.
Yarım kalan agent görevlerini belirle.
En son başarılı kontrol noktasını bul.
Çalışmaya oradan devam et.

State dosyasını aşağıdaki bilgileri tutacak şekilde genişlet:

schema version
run ID
proje durumu
aktif faz
aktif implementasyon dalgası
tamamlanan fazlar
aktif agent’lar
agent görevleri
görev sahiplikleri
dosya sahiplikleri
blocker listesi
retry sayıları
son başarılı doğrulama
son başarısız komut
resume noktası
build durumu
lint durumu
type-check durumu
test durumu
kalite kapısı durumu
güvenlik kapısı durumu
completion audit durumu
son güncelleme zamanı

State içine TODO görevlerinin tam kopyasını koyma. Görevlerin tek kaynağı docs/TODO.md olarak kalmalıdır.

7. Görev sözleşmesi

Her TODO görevi aşağıdaki alanları içermelidir:

Görev ID
Başlık
Kategori
Açıklama
Öncelik
Şiddet
Bağımlılıklar
Sorumlu agent
Dosya veya modül sahipliği
Durum
Kabul kriterleri
Doğrulama komutları
Tamamlanma kanıtı
Blocker
Retry sayısı
Son güncelleme

Desteklenen durumlar:

Bekliyor
Hazır
Devam Ediyor
İncelemede
Test Ediliyor
Bloke
Başarısız
Tamamlandı

Bir görev yalnızca şu koşullarda Tamamlandı olabilir:

Kod veya gerekli çıktı gerçekten oluşturuldu.
Kabul kriterleri sağlandı.
İlgili doğrulama komutları çalıştı.
Test sonucu başarılı.
Tamamlanma kanıtı yazıldı.
Başka bir agent tarafından yapılan denetimde açık kritik sorun bulunmadı.
8. Paralel çalışma ve çakışma kuralları

Bağımsız görevlerde subagent’ları paralel çalıştır.

Ancak aşağıdaki kuralları zorunlu uygula:

İki agent aynı dosyayı aynı anda düzenleyemez.
Her yazma görevinin açık dosya veya modül sahipliği olmalıdır.
Merkezi workflow, TODO ve status dosyalarını paralel implementation agent’ları düzenleyemez.
Subagent’lar sonuçlarını yapılandırılmış handoff olarak ana agent’a iletmelidir.
Ana agent veya progress-state agent merkezi dosyaları güncellemelidir.
Paralel yazma gerektiğinde ve Cursor sürümü destekliyorsa izole Git worktree kullan.
Worktree kullanılamıyorsa çakışabilecek görevleri sıralı çalıştır.
Merge öncesinde build, test ve conflict kontrolü yap.
Kontrolsüz şekilde sonsuz sayıda agent oluşturma.
Varsayılan eş zamanlı yazan agent sayısını makul tut.
İç içe agent oluşturma derinliği en fazla iki seviye olsun.
Küçük projelerde gereksiz agent oluşturma; görev kapsamına göre gerekli rolleri seç.
9. Handoff standardı

Her subagent görevin sonunda ana orkestratöre şu yapıda çıktı vermelidir:

Agent adı
Görev ID’leri
İncelenen dosyalar
Değiştirilen dosyalar
Yapılan işlemler
Alınan teknik kararlar
Çalıştırılan komutlar
Test sonuçları
Açık kalan sorunlar
Yeni tespit edilen görevler
Riskler
Önerilen sonraki agent
Durum: başarılı / kısmi / bloke / başarısız

“Tamamlandı” demek tek başına yeterli kanıt değildir.

10. Otomatik tamamlama döngüsü

Ana orkestratör aşağıdaki mantığı uygulamalıdır:

while project_is_not_verified_complete:
    resume_and_reconcile_state()
    inspect_todo_and_code()
    select_ready_tasks()
    assign_agents_with_file_ownership()
    execute_independent_tasks_in_parallel()
    integrate_results()
    run_build_lint_typecheck_tests()
    reconcile_todo_with_real_code()
    run_gap_scan()
    run_completion_audit()

    if critical_or_important_gaps_exist:
        add_or_update_todo_tasks()
        continue

    run_security_gate()
    run_quality_gate()

    if any_required_gate_fails:
        create_fix_tasks()
        continue

    update_documentation()
    run_final_smoke_test()
    verify_delivery_artifacts()

    if all_exit_criteria_pass:
        mark_project_complete()
        break

Sonsuz döngüyü engellemek için:

Aynı hata için en fazla üç otomatik düzeltme denemesi yap.
Üç deneme sonunda hata devam ederse blocker olarak kaydet.
Blocker’ın nedeni, denenen çözümler ve gerekli kullanıcı girdisi açıkça yazılsın.
Blocker varsa proje “tamamlandı” olarak işaretlenmesin.
11. Completion exit kriterleri

Proje yalnızca aşağıdaki koşulların tamamı sağlandığında teslim edilmiş sayılmalıdır:

Kritik TODO sayısı sıfır.
Önemli TODO sayısı sıfır veya yalnızca açıkça onaylanmış blocker’lardan oluşuyor.
Build başarılı.
Lint başarılı.
Type-check başarılı.
Zorunlu testler başarılı.
Temel smoke test başarılı.
Kritik veya yüksek güvenlik sorunu yok.
Placeholder veya sahte implementasyon yok.
Çalışmayan ana buton ya da route yok.
API ile UI sözleşmeleri uyumlu.
Veritabanı migration ve schema durumu uyumlu.
Environment örneği güncel.
README ve kullanım dokümanı gerçek komutlarla uyumlu.
TODO ile gerçek kod durumu uyumlu.
Completion auditor teslimi onayladı.
Kalite kapısı geçti.
Güvenlik kapısı geçti.
Final durum raporu oluşturuldu.

Bu koşullardan biri sağlanmıyorsa kullanıcıya “proje tamamen hazır” deme.

12. Yeni ve güncellenecek dosyalar

En az aşağıdaki yapıyı oluştur veya uygun biçimde uyarlayarak oluştur:

.cursor/
├── agents/
│   ├── project-discovery-agent.md
│   ├── todo-controller-agent.md
│   ├── progress-state-agent.md
│   ├── software-architect-agent.md
│   ├── ui-ux-design-agent.md
│   ├── implementation-agent.md
│   ├── test-qa-agent.md
│   ├── security-quality-agent.md
│   ├── completion-auditor-agent.md
│   └── documentation-release-agent.md
├── commands/
│   ├── proje_orkestra.md
│   └── mevcut komutlar...
└── rules/
    └── agent.md

Ayrıca gerekli görürsen oluştur:

docs/AGENT_CONTRACTS.md
docs/AGENT_HANDOFFS.md
docs/DECISIONS.md
docs/ORCHESTRA_REPORT.md
docs/FILE_OWNERSHIP.md
docs/ORCHESTRATION_ARCHITECTURE.md
scripts/validate_orchestra.py

Ortak ve tekrar eden prosedürler için Cursor’ın güncel Agent Skills yapısı uygunsa .cursor/skills/ altında yeniden kullanılabilir skill’ler oluştur:

workflow state management
TODO reconciliation
completion audit
testing protocol
documentation synchronization

Agent dosyalarında aynı uzun prosedürleri tekrar etmek yerine ortak skill veya referans doküman kullan.

13. Validation scripti

scripts/validate_orchestra.py oluştur.

Bu script en az aşağıdakileri kontrol etsin:

Gerekli agent dosyaları var mı?
Agent isimleri benzersiz mi?
Agent açıklamaları delegasyon için yeterince açık mı?
Orkestrasyon komutu var mı?
Eski komutlar yeni sisteme uyumlu mu?
State schema gerekli alanları içeriyor mu?
TODO formatı geçerli mi?
Duplicate görev ID var mı?
Geçersiz görev bağımlılığı var mı?
Tamamlanmış görevlerde kanıt ve kabul kriteri var mı?
Aktif görevlerin sahibi var mı?
Aynı dosya üzerinde çakışan aktif sahiplik var mı?
Workflow DoD ile agent sözleşmeleri uyumlu mu?
README ve USAGE yeni komutu içeriyor mu?
Kırık dahili doküman linki var mı?
Placeholder veya unutulmuş şablon metni var mı?

Mevcut scripts/validate_quality.py ile entegrasyon kur.

Mümkünse ana kalite doğrulama komutu iki validasyonu da çalıştırsın.

14. Dokümantasyon güncellemeleri

Aşağıdaki dosyaları yeni sistemle uyumlu hale getir:

README.md
docs/USAGE.md
docs/CANONICAL_FLOW.md
docs/WORKFLOW_DOD.md
docs/WORKFLOW_STATE.md
docs/TODO.md
docs/STATUS_REPORT.md
CHANGELOG.md

README’de şunları açıkla:

Orkestra sistemi nedir?
Hangi agent ne iş yapar?
/proje_orkestra nasıl kullanılır?
Yarım kalan proje nasıl devam eder?
Paralel görevler nasıl yönetilir?
Dosya çakışmaları nasıl önlenir?
Projenin tamamlandığı nasıl doğrulanır?
Native subagent desteği olmayan eski Cursor sürümlerinde fallback davranışı nedir?
15. Fallback davranışı

Kurulu Cursor sürümünde native custom subagent özelliği bulunmuyorsa sistemi tamamen iptal etme.

Aynı agent rollerini ana agent içinde sıralı ve izole bağlam bölümleri halinde simüle eden fallback mekanizması oluştur.

Ancak native subagent mevcutsa mutlaka native yapıyı kullan.

Fallback durumu README ve status raporunda açıkça belirtilsin.

16. Gerçek doğrulama senaryosu

Değişiklikler bittikten sonra yalnızca dosyaların varlığını kontrol etmekle yetinme.

Örnek bir proje dokümanı üzerinden orkestrasyon sisteminin mantığını doğrula.

Kontrol et:

Discovery agent doğru çıktı üretiyor mu?
TODO görevleri bağımlılıklarla oluşuyor mu?
Agent sahipliği atanıyor mu?
State dosyası güncelleniyor mu?
Eksik görev tespit edildiğinde TODO’ya ekleniyor mu?
Tamamlanmamış görev yanlışlıkla tamamlandı sayılıyor mu?
Test hatası yeniden geliştirme döngüsü oluşturuyor mu?
Completion auditor eksik teslimi reddediyor mu?
Resume mekanizması kaldığı görevden devam ediyor mu?
Validator scriptleri başarılı çalışıyor mu?

Repo bir meta-agent framework olduğu için gerçek bir demo uygulaması yazmak zorunda değilsin. Ancak örnek state, TODO ve agent handoff akışının doğrulanabilir olduğunu göster.

17. Çalışma biçimi

Şimdi şu sırayla ilerle:

Repoyu tamamen incele.
Mevcut mimarinin güçlü ve zayıf noktalarını çıkar.
Kısa bir migration planı oluştur.
Kullanıcı onayı beklemeden implementasyona başla.
Agent dosyalarını oluştur.
Ana rule ve komutları güncelle.
State, TODO ve DoD sözleşmelerini geliştir.
Validation scriptlerini oluştur.
Dokümantasyonu güncelle.
Validation scriptlerini çalıştır.
Bulduğun hataları düzelt.
Git diff üzerinden son denetimi yap.
Completion audit uygula.
Final raporu sun.

Yalnızca yapılacakları anlatıp durma.

Dosyaları gerçekten değiştir.

Kod ve dokümantasyon üret.

Komutları gerçekten çalıştır.

Test edilmemiş bir sistemi tamamlanmış gösterme.

18. Final cevap formatı

İşlem sonunda şu başlıklarla rapor ver:

Oluşturulan agent’lar

Her agent ve görevi.

Değiştirilen dosyalar

Dosya bazında kısa açıklama.

Orkestrasyon akışı

Yeni uçtan uca çalışma şekli.

Resume mekanizması

Yarım kalan işin nasıl bulunduğu ve devam ettirildiği.

Paralel çalışma güvenliği

Dosya sahipliği ve worktree yaklaşımı.

Çalıştırılan doğrulamalar

Komut ve sonuçları.

Bulunan ve düzeltilen sorunlar

Önemli düzeltmeler.

Açık blocker’lar

Varsa açıkça belirt.

Final durum

Aşağıdakilerden yalnızca birini kullan:

TESLİME HAZIR
KISMEN HAZIR — BLOCKER VAR
DOĞRULAMA BAŞARISIZ

Şimdi repo incelemesini başlat ve Orkestra Agent Sistemi v2 dönüşümünü doğrudan uygula.