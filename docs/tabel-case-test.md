## Tabel Test Case

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|---|---|---|---|---|---|
| TC-01 | Bayar dengan QRIS (alur utama) | Common | Mahasiswa sudah login; pesanan sudah dibuat dengan `id_pesanan` valid; tarif Rp30.000 | Pilih QRIS → scan kode QR → konfirmasi | Status "Pembayaran Sukses"; notifikasi pembayaran berhasil terkirim; UI menampilkan struk digital |
| TC-02 | Bayar dengan e-wallet, saldo cukup | Common | Pesanan sudah dibuat; tarif Rp50.000; saldo e-wallet Rp100.000; pengerjaan belum selesai | Pilih e-wallet → konfirmasi | Status "Pembayaran Sukses"; saldo berkurang Rp50.000; notifikasi terkirim; struk digital tampil |
| TC-03 | Bayar di muka dengan transfer bank | Common | Pesanan sudah dibuat dengan status "Menunggu Petugas"; pengerjaan belum dimulai; tarif Rp75.000 | Pilih transfer bank → transfer sesuai nominal → konfirmasi | Pembayaran diterima sebelum pengerjaan; status "Pembayaran Sukses"; notifikasi terkirim |
| TC-04 | Bayar cash setelah pengerjaan selesai | Common | Petugas sudah menandai pengerjaan selesai; tarif Rp100.000 | Pilih cash → serahkan uang tunai → konfirmasi | Pembayaran tercatat; status "Pembayaran Sukses"; notifikasi pembayaran berhasil terkirim |
| TC-05 | Nominal pembayaran sama dengan tarif di booking | Common | Mahasiswa memesan jasa dengan tarif Rp75.000 yang ia atur sendiri di Modul Booking | Buka halaman pembayaran untuk pesanan tersebut | Nominal yang dikirim ke `prosesPembayaran` adalah Rp75.000, sama dengan tarif booking |
| TC-06 | Saldo kurang, lalu pindah ke metode lain (alur alternatif) | Common | Pengerjaan sudah selesai; tarif Rp50.000; saldo e-wallet Rp20.000 | Pilih e-wallet → konfirmasi (gagal) → pilih Cash → konfirmasi | Percobaan pertama menampilkan pesan "Saldo tidak mencukupi, pilih metode lain (misal: Cash)"; setelah pilih Cash, status "Pembayaran Sukses"; hanya satu pembayaran sukses tercatat |
| TC-07 | Konfirmasi bayar tanpa memilih metode | Edge (input kosong) | Pesanan sudah dibuat | Tekan konfirmasi tanpa memilih metode apa pun | Pembayaran ditolak dengan pesan "Pilih metode pembayaran"; `prosesPembayaran` tidak dipanggil; tidak ada transaksi tercatat |
| TC-08 | Nominal tepat nol | Edge (nilai batas) | Pesanan dengan tarif Rp0 (data tidak valid) | Pilih e-wallet → konfirmasi | Pembayaran ditolak karena nominal harus lebih dari 0; tidak ada notifikasi dikirim |
| TC-09 | Nominal berformat tidak valid | Edge (format tidak valid) | Pesanan sudah dibuat | Masukkan nominal `"50000abc"` → konfirmasi | Pembayaran ditolak dengan pesan nominal tidak valid; status tetap belum bayar |
| TC-10 | Saldo e-wallet kurang Rp1 dari nominal | Edge (nilai batas) | Tarif Rp50.000; saldo e-wallet Rp49.999 | Pilih e-wallet → konfirmasi | Status "Pembayaran Gagal"; UI menampilkan "Saldo tidak mencukupi, pilih metode lain (misal: Cash)"; saldo tidak berubah; tidak ada notifikasi sukses |
| TC-11 | Bayar dua kali untuk pesanan yang sama | Edge (duplikasi) | Pesanan sudah berstatus "Pembayaran Sukses" (atau tombol konfirmasi ditekan dua kali berturut-turut) | Kirim ulang pembayaran untuk `id_pesanan` yang sama | Hanya satu transaksi tercatat; permintaan kedua ditolak dengan pesan "Pesanan sudah dibayar"; saldo tidak terpotong dua kali |
| TC-12 | Nominal melebihi batas maksimum transaksi | Edge (batas limit) | Batas maksimum per transaksi Rp10.000.000 (asumsi tim); tarif Rp10.000.001 | Pilih e-wallet → konfirmasi | Pembayaran ditolak dengan pesan melebihi batas transaksi; tidak ada transaksi tercatat |
| TC-13 | Bayar cash sebelum pengerjaan selesai | Edge (state tak terduga) | Pesanan berstatus "Menunggu Petugas"; pengerjaan belum selesai | Pilih cash → konfirmasi | Pembayaran ditolak dengan pesan "Pembayaran cash hanya bisa dilakukan setelah pengerjaan selesai" |
| TC-14 | `id_pesanan` tidak ditemukan | Edge (state tak terduga) | Pesanan sudah dihapus atau `id_pesanan` tidak ada di sistem | Pilih QRIS → konfirmasi | Pembayaran ditolak dengan pesan pesanan tidak ditemukan; tidak ada uang diproses; tidak ada notifikasi dikirim |

---

## Cara Memilih Edge Case

* Nyari 6 Celah (Edge Case): Kalian ngecek 6 kemungkinan celah error (mulai dari input kosong, angka batas, format salah, data ganda, batas maksimal, sampai kondisi aneh-aneh).
* Ngecek Kasus Saldo Kurang: Buat ngetes nilai batas, skenarionya pas saldo kurang Rp1 dari total harga.
* Aturan Main Modul: Kasus-kasus tesnya diambil dari aturan aplikasi, contohnya: bayar cash harus nunggu pekerjaan selesai, duitnya nggak boleh nol/minus, dan satu pesanan nggak boleh dibayar dua kali.
* Fokus Utama (Keamanan Uang): Prioritas utamanya nyegah error yang bisa ngerugiin duit mahasiswa (kayak bayar dua kali atau bayar pesanan fiktif).
* Catatan Batas Maksimal: Angka maksimal di tes (TC-12) itu cuma asumsi awal, jadi nanti bisa diubah sesuai aturan asli aplikasinya.

---
