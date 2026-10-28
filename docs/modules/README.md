# Dokumentasi Modul Sistem: Cakruh - Cakrawala Suruh

Dokumentasi ini berisi penjelasan lengkap mengenai modul-modul utama yang membangun aplikasi **Cakruh-Cakrawala-Suruh**, mencakup tanggung jawab, pengelolaan data, aturan bisnis, serta alur hubungan antar-modul.

---

## Ringkasan Modul

| Kode Modul | Nama Modul | Deskripsi Singkat |
| :---: | :--- | :--- |
| **01** | [Registration](01-registration.md) | Pengelolaan pendaftaran, autentikasi, verifikasi identitas, dan profil mahasiswa. |
| **02** | [Booking](02-booking.md) | Penanganan proses pemesanan jasa, kategorisasi masalah, penentuan tarif, dan penyesuaian jadwal/lokasi. |
| **03** | [Payment](03-payment.md) | Pengelolaan transaksi pembayaran jasa melalui berbagai opsi metode pembayaran. |
| **04** | [Notification](04-notification.md) | Pengiriman pembaruan status pemesanan, pelacakan posisi petugas, dan konfirmasi transaksi secara real-time. |

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
