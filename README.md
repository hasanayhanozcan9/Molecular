# Molecular
🧬 Pakize Diken Molecular OS (PD-MOS)
PD-MIP: Pakize Diken Moleküler İnternet Protokolü
Bu proje, biyolojik ortamlarda (kan, su veya hücreler arası sıvı) veri iletimini simüle eden bir Moleküler İletişim (MC) protokolüdür. Geleneksel elektromanyetik dalgalar yerine, bilginin molekül konsantrasyonları aracılığıyla iletildiği bir nanonetwork mimarisi sunar.
🚀 Özellikler
Pakize Diken tarafından geliştirilen bu sistem, OSI modelini moleküler düzeye taşır:
Physical Layer (PHY): Stokes-Einstein denklemi ve Fick’in 2. kanununu kullanarak 3D akışkan ortamda difüzyon tabanlı yayılım modeller.
Data Link Layer: Konsantrasyon Kaydırmalı Anahtarlama (CSK) modülasyonu ve MD5 tabanlı hata denetimi (checksum) içerir.
Network Layer: Veriyi moleküler paketlere (MolecularPacket) ayırır ve hedefleme yapar.
Adaptive Thresholding: Alıcı tarafta, gürültülü (Brownian motion) sinyali anlamlı veriye dönüştüren adaptif eşikleme algoritması.
🛠 Teknik Mimari
Sistem üç temel aşamadan oluşur:
Modülasyon: İkili veriler (0 ve 1), belirli miktardaki molekül salınımlarına dönüştürülür.
Yayılım: Moleküller, bio-ortamda Brown hareketi ile rastgele dağılır.
Kritik Denklem: D = \frac{k \cdot T}{6 \pi \eta r}
Demodülasyon: Alıcı düğüm, ortamdaki konsantrasyon değişimini örnekleyerek mesajı deşifre eder.
