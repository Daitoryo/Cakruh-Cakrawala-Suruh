# Dokumentasi Modul Sistem: Cakruh - Cakrawala Suruh

Dokumentasi ini berisi penjelasan lengkap mengenai modul-modul utama yang membangun aplikasi **Cakruh-Cakrawala-Suruh**, mencakup tanggung jawab, pengelolaan data, aturan bisnis, serta alur hubungan antar-modul.

---

## Ringkasan Modul

| Kode Modul | Nama Modul | Deskripsi Singkat |
| :---: | :--- | :--- |
| **01** | [Registration](#1-modul-registration) | Pengelolaan pendaftaran, autentikasi, verifikasi identitas, dan profil mahasiswa. |
| **02** | [Booking](#2-modul-booking) | Penanganan proses pemesanan jasa, kategorisasi masalah, penentuan tarif, dan penyesuaian jadwal/lokasi. |
| **03** | [Payment](#3-modul-payment) | Pengelolaan transaksi pembayaran jasa melalui berbagai opsi metode pembayaran. |
| **04** | [Notification](#4-modul-notification) | Pengiriman pembaruan status pemesanan, pelacakan posisi petugas, dan konfirmasi transaksi secara real-time. |

---

## Detail Spesifikasi Modul

### 1. Modul Registration

#### Tanggung Jawab
Mendaftar akun di aplikasi Cakrawala Suruh untuk memfasilitasi kemudahan proses *login* serta melakukan validasi identitas pengguna di dalam sistem Cakruh.

#### Pengelolaan Data
- **Metode Pendaftaran**: Pilihan opsi pendaftaran akun.
- **Verifikasi Autentikasi**: Pengiriman & konfirmasi Kode OTP.
- **Profil & Keamanan**: Pengisian data pribadi pengguna dan pengamanan akun.
- **Pengaturan Lokasi**: Penentuan titik lokasi utama pengguna.
- **Aktivasi & Dasbor**: Status aktif akun dan integrasi halaman utama (*dashboard*).

#### Aturan Bisnis
1. Pendaftaran akun terhubung secara otomatis ke dalam aplikasi Cakruh.
2. Pendaftaran dinyatakan **berhasil** jika seluruh data verifikasi valid.
3. Pengisian profil wajib berfungsi sebagai bukti sah bahwa pengguna adalah mahasiswa Cakrawala yang terdaftar.
4. Pengaturan lokasi digunakan untuk memastikan pengguna berada di dalam lingkungan kampus.

#### Hubungan Antar Modul
- **Modul Notification**: Mengirimkan notifikasi saat akun berhasil melakukan login/pendaftaran.

---

### 2. Modul Booking

#### Tanggung Jawab
Melayani dan memproses pemesanan jasa kepada petugas Cakruh secara langsung melalui aplikasi Cakruh.

#### Pengelolaan Data
- **Kategori & Jenis Masalah**: Penentuan jenis kendala/masalah yang dialami pengguna.
- **Pilihan Kategori Jasa**: Opsi tipe bantuan yang dibutuhkan.
- **Lokasi Pemesanan**: Titik jemput/lokasi pengerjaan.
- **Jadwal Pemesanan**: Waktu pelaksanaan jasa.
- **Tarif Jasa**: Pengaturan dan penyesuaian biaya jasa.
- **Matching System**: Pencocokan pesanan pengguna dengan petugas Cakruh yang bersedia/tersedia.

#### Aturan Bisnis
1. Mahasiswa melakukan pemesanan jasa sesuai dengan masalah yang dihadapi.
2. Mahasiswa mengatur dan menetapkan penyesuaian tarif jasa yang dipesan.
3. Waktu dan lokasi pengerjaan disesuaikan sepenuhnya berdasarkan input jadwal dan lokasi yang dipilih mahasiswa.

#### Hubungan Antar Modul
- **Modul Payment**: Menentukan besaran harga/tarif jasa yang akan dibayarkan.
- **Modul Notification**: Mengirimkan notifikasi konfirmasi dan status pemesanan setelah proses booking selesai.

---

### 3. Modul Payment

#### Tanggung Jawab
Memfasilitasi transaksi pembayaran jasa oleh pemesan atas pekerjaan yang telah diselesaikan oleh petugas Cakruh menggunakan berbagai kanal pembayaran.

#### Pengelolaan Data
- **Metode e-Wallet**: Pembayaran via dompet digital.
- **Metode Transfer Bank**: Pembayaran via transfer antarbank.
- **Metode Cash / Di Tempat**: Pembayaran langsung secara tunai setelah pengerjaan.
- **Metode QRIS**: Pembayaran secara instan menggunakan kode QRIS.

#### Aturan Bisnis
1. Memberikan kemudahan bagi mahasiswa untuk memilih metode pembayaran yang sesuai.
2. Memungkinkan skema bayar di awal (*pre-payment*) via Transfer Bank atau QRIS.
3. Memungkinkan skema bayar di akhir (*post-payment*) secara tunai (*cash*) setelah pengerjaan selesai.

#### Hubungan Antar Modul
- **Modul Booking**: Menerima rincian tarif jasa hasil pemesanan dari modul booking.
- **Modul Notification**: Memicu pengiriman notifikasi konfirmasi ketika pembayaran telah berhasil diproses.

---

### 4. Modul Notification

#### Tanggung Jawab
Mengirimkan notifikasi dan informasi pembaruan status (seperti pergerakan petugas ke lokasi pemesan) setelah pesanan berhasil dibuat oleh pengguna.

#### Pengelolaan Data
- **Notifikasi Aplikasi**: Pesan pemberitahuan dalam aplikasi (*push notification*).
- **Maps Petugas**: Pelacakan posisi lokasi petugas secara *real-time*.
- **Notifikasi Pembayaran**: Konfirmasi status transaksi sukses.
- **Notifikasi Status Pekerjaan**: Pemberitahuan bahwa pengerjaan jasa telah selesai.

#### Aturan Bisnis
1. Mengirimkan pemberitahuan secara *real-time* kepada pemesan terkait pembaruan status pesanan.
2. Memantau dan menampilkan pergerakan posisi petugas saat menuju lokasi pemesan.
3. Menginformasikan kepastian bahwa pembayaran telah diterima.
4. Menginformasikan bahwa pekerjaan telah selesai dilaksanakan oleh petugas.

#### Hubungan Antar Modul
- **Modul Registration**: Mengirimkan pemberitahuan status pendaftaran / autentikasi login.
- **Modul Booking**: Menerima pemicu notifikasi saat pendaftaran booking selesai dibuat.
- **Modul Payment**: Menerima pemicu notifikasi saat proses transaksi pembayaran dinyatakan berhasil.

---

## Alur Interaksi Antar Modul (Workflow)

```
[ Modul Registration ] ──(Verifikasi Akun & Notifikasi Login)──> [ Modul Notification ]
          │
          ▼
   [ Modul Booking ] ───(Inisiasi Booking)─────────────────────> [ Modul Notification ]
          │
          ├──(Kalkulasi Biaya & Tarif Jasa)
          ▼
   [ Modul Payment ] ───(Konfirmasi Pembayaran Berhasil)──────> [ Modul Notification ]
```
