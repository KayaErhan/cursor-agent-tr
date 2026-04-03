# /proje_baslat - /proje_workflow Icin Kolay Alias

Bu komut, kullanici aliskanliklari icin **kolay hatirlanan bir alias** olarak davranir.
Ana orkestrasyon ve n8n benzeri akıs mantigi `/proje_workflow` komutunda tanimlidir.

Kullanim:
- Kullanici `/proje_baslat` yazdiginda, bu komut **/proje_workflow ile ayni niyetle** calismalidir:
  - `docs/WORKFLOW_STATE.md` dosyasini kontrol et.
  - Gerekirse yeni bir state olustur (`current_step = "analysis"`).
  - Siradaki mantikli adimi belirleyip, o adim icin gerekli calismayi gerceklestir.

Notlar:
- Dokumantasyonda, ana tavsiye edilen komut ismi yine `/proje_workflow` olarak korunabilir;
  ancak pratikte `/proje_baslat` da tamamen ayni sureci tetikleyen kullanisli bir giris noktasi olarak
  kabul edilir.

