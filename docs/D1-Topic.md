# D1. Topik & Pernyataan Masalah

## 1. Nama & Deskripsi Aplikasi
**Nama Aplikasi:** Cakruh (Cakrawala Suruh)
**Deskripsi:** Cakruh adalah aplikasi penyedia jasa *on-demand* yang dirancang khusus untuk mahasiswa di lingkungan kampus. Aplikasi ini bertujuan membantu mengatasi berbagai permasalahan sehari-hari mahasiswa dengan menyediakan layanan jasa yang mudah diakses dan memiliki tarif yang terjangkau (ramah di kantong mahasiswa).

## 2. Pernyataan Masalah (Problem Statement)
Belakangan ini banyak sekali mahasiswa yang pusing karena sedang banyak tugas maupun tempat yang sulit untuk dijangkau, contohnya seperti tempat fotokopi. Karena kebingungan untuk mengakses itu, mahasiswa jadi kesulitan untuk *print* tugas, *print* makalah, dan juga skripsi.

Selain sulit untuk mencari tempat seperti fotokopi, mahasiswa juga terkadang ingin memesan makanan tetapi dikarenakan ongkos kirim yang mahal, mahasiswa jadi malas untuk memesannya dan akhirnya tidak jadi memesan makanan maupun minuman. Selain dua hal tersebut, mahasiswa juga sering kesusahan ketika terjadi masalah mendadak, seperti kendaraan yang suka tiba-tiba mogok, ban kendaraan kempes tiba-tiba, atau bingung ingin pergi ke suatu tempat tetapi harga pesan ojek sangat mahal.

Maka dari beberapa permasalahan di atas, kami berinisiatif untuk menghadirkan aplikasi jasa yaitu **Cakruh (Cakrawala Suruh)**. Kami membuat jasa Cakruh untuk mengatasi permasalahan-permasalahan mahasiswa yang terjadi dengan harga yang relatif jauh lebih murah. Kami juga membuat aplikasi Cakruh agar mahasiswa mudah memesan jasa dan bisa melihat *pricelist* jasa yang tersedia, sehingga bisa lebih menyesuaikan dengan dompet mahasiswa yang sedang mengalami masalah namun tetap mudah untuk diakses.

## 3. Target Pengguna (Aktor)
Sistem aplikasi Cakruh melibatkan 3 aktor utama:
1. **Mahasiswa:** Aktor yang bertindak sebagai pengguna/pemesan jasa untuk menyelesaikan masalah mereka.
2. **Petugas Cakruh:** Aktor yang bertindak sebagai penyedia jasa (menerima pesanan, mengerjakan tugas, dan menerima pembayaran).
3. **Admin:** Aktor yang memantau kelancaran sistem, melihat status keberangkatan petugas, dan mengirimkan notifikasi pemesanan maupun penyelesaian kepada mahasiswa.

## 4. Ruang Lingkup (Scope)
**Apa yang AKAN dilakukan oleh aplikasi (In-Scope):**
* Mengelola pendaftaran dan verifikasi akun khusus mahasiswa (Modul Registration).
* Menyediakan fitur pemesanan (*booking*) untuk berbagai kategori jasa seperti bantuan fotokopi, titip beli makanan, ojek kampus, dan bantuan perbaikan kendaraan ringan.
* Menampilkan daftar harga (*pricelist*) dan menghitung total biaya secara transparan sebelum pemesanan (Modul Booking).
* Menyediakan berbagai metode pembayaran yang fleksibel seperti Cash (Bayar di tempat), QRIS, Transfer Bank, dan E-Wallet (Modul Payment).
* Mengirimkan notifikasi status pesanan, keberangkatan petugas, dan keberhasilan pembayaran (Modul Notification).

**Apa yang TIDAK AKAN dilakukan oleh aplikasi (Out of Scope):**
Cakruh memiliki batasan layanan dan **tidak** menyediakan jasa berikut:
1. **Joki Tugas:** Cakruh tidak bisa melakukan joki tugas karena hal itu merupakan kecurangan, dan Cakruh tidak mentoleransi kecurangan apa pun.
2. **Joki Skripsi:** Dikarenakan skripsi adalah tugas akhir mahasiswa, Cakruh tidak ingin mengambil risiko dengan menerima joki tugas akhir.
3. **Joki Game:** Karena Cakruh berada di lingkungan mahasiswa dan tujuan utamanya adalah membantu permasalahan produktivitas/logistik di sekitar kampus, maka Cakruh tidak bersedia melayani jasa joki *game*.
