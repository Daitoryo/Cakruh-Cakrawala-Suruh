# 💳 Modul Payment - Aplikasi Cakruh (Cakrawala Suruh)

Modul **Payment** adalah komponen inti dari aplikasi **Cakruh (Cakrawala Suruh)** yang menangani alur transaksi keuangan mahasiswa, validasi aturan bisnis pembayaran, serta pengelolaan riwayat transaksi secara aman dan terstruktur.

---

## 📌 Daftar Isi
- [Gambaran Umum Modul](#-gambaran-umum-modul)
- [Fitur & Aturan Bisnis](#-fitur--aturan-bisnis)
- [Arsitektur Kode & Fungsi](#-arsitektur-kode--fungsi)
- [Skenario CLI & Pengujian Interaktif](#-skenario-cli--pengujian-interaktif)
- [Pengujian Unit (Pytest Automation)](#-pengujian-unit-pytest-automation)
- [Tabel Test Case & Edge Cases](#-matriks-test-case--edge-cases)
- [Cara Menjalankan Program & Testing](#-cara-menjalankan-program--testing)

---

## 🔍 Gambaran Umum Modul

Dalam ekosistem **Cakruh**, modul ini bertugas memastikan bahwa:
1. Mahasiswa dapat membayar jasa bantuan kampus (print, beli makanan, antar paket, dll.) dengan lancar.
2. Keuangan mahasiswa terlindungi dari pembayaran fiktif atau *double payment*.
3. Aturan waktu pembayaran (sebelum vs sesudah pekerjaan selesai) ditegakkan secara mutlak oleh sistem.

---

## ⚖️ Fitur & Aturan Bisnis

### 1. Metode Pembayaran yang Didukung
* **E-Wallet:** GoPay, OVO, ShopeePay, DANA, LinkAja (Bisa dibayar di awal / *Pre-payment*).
* **Transfer Bank:** BCA, Mandiri, BNI, BRI (Bisa dibayar di awal / *Pre-payment*).
* **QRIS:** Bebas biaya admin, pembayaran instan (Bisa dibayar di awal / *Pre-payment*).
* **Cash (Tunai):** Bayar langsung di tempat (**Hanya diperbolehkan setelah pengerjaan selesai**).

### 2. Aturan Validasi Khusus (`validate_payment`)
* **Sanitasi String:** Metode pembayaran bersifat *case-insensitive* dan toleran terhadap spasi tak sengaja (contoh: `"  QRIS "` $\rightarrow$ `"qris"`).
* **Validasi Nominal:**
  * Nominal harus ber-tipe angka (`int` atau `float`). Tipe `str`, `None`, dan `bool` (`True`/`False`) akan memicu `ValueError`.
  * Nominal harus lebih besar dari 0 ($> 0$). Nilai $0$ atau negatif akan memicu `ValueError`.
* **Keterikatan Pekerjaan (`job_done`):**
  * Jika metode pembayaran adalah `"cash"` dan `job_done = False`, fungsi mengembalikan `False` (ditolak).

---

## 🛠️ Arsitektur Kode & Fungsi

### 1. Logika Inti Validasi (`payment_function.py`)
* `validate_payment(method, amount, job_done)`: Core function yang memverifikasi tipe data, nominal, dan aturan pengerjaan sebelum transaksi diproses.

### 2. Implementasi CLI & Menu Interaktif (`payment_saja.py`)
* `rupiah(angka)`: Formatter otomatis untuk mengubah angka menjadi string mata uang (contoh: `10000` $\rightarrow$ `"Rp10.000"`).
* `bayar(nama, jasa, jumlah, metode, detail, pekerjaan_selesai)`: Fungsi pemroses transaksi yang menyimpan data ke `riwayat` jika validasi sukses.
* `input_angka(pesan)` & `pilih_dari_daftar(pesan, daftar)`: Helper function untuk menangani kesalahan input user secara eksplisit di terminal.
* `menu_bayar()`, `menu_riwayat()`, `main()`: Antarmuka berbasis teks untuk navigasi user.

---

## 🧪 Skenario CLI & Pengujian Interaktif

File `pytest_payment.py` digunakan untuk menguji alur interaktif antarmuka CLI dengan teknik *mocking* `input()` menggunakan `monkeypatch` dan pengujian output layar menggunakan `capsys`.

### Cakupan Pengujian CLI:
* **Pengulangan Input Otomatis:** Memastikan prompt terus mengulang jika pengguna memasukkan huruf/karakter saat diminta angka, atau memilih nomor menu di luar jangkauan.
* **Perhitungan Kembalian Tunai:** Memastikan perhitungan kembalian uang cash tepat (misal: Tagihan Rp10.000, bayar Rp15.000 $\rightarrow$ Kembalian Rp5.000).
* **Penanganan Transaksi Dibatalkan:** Jika pembayaran gagal atau uang cash kurang, riwayat transaksi dipastikan tetap bersih (`p.riwayat == []`).

---

## 🟢 Pengujian Unit (Pytest Automation)

Pengujian modul dilakukan menggunakan *framework* **Pytest**. Berdasarkan eksekusi `test_payment.py`, seluruh **15 test cases** telah lulus secara sempurna (100% PASSED).

```text
=========================== test session starts ===========================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\USER\Downloads\pytest_payment
collected 15 items

test_payment.py::test_ewallet_before_job_allowed PASSED            [  6%]
test_payment.py::test_transfer_before_job_allowed PASSED           [ 13%]
test_payment.py::test_qris_allowed PASSED                           [ 20%]
test_payment.py::test_cash_after_job_allowed PASSED                [ 26%]
test_payment.py::test_cash_before_job_rejected PASSED               [ 33%]
test_payment.py::test_method_case_and_spaces_ignored PASSED         [ 40%]
test_payment.py::test_unknown_method_raises PASSED                  [ 46%]
test_payment.py::test_amount_zero_or_negative_raises[0] PASSED      [ 53%]
test_payment.py::test_amount_zero_or_negative_raises[-1] PASSED     [ 60%]
test_payment.py::test_amount_zero_or_negative_raises[-50000] PASSED [ 66%]
test_payment.py::test_amount_non_numeric_raises[50000] PASSED      [ 73%]
test_payment.py::test_amount_non_numeric_raises[None] PASSED       [ 80%]
test_payment.py::test_amount_non_numeric_raises[True] PASSED       [ 86%]
test_payment.py::test_minimum_valid_amount PASSED                  [ 93%]
test_payment.py::test_non_string_method_raises PASSED               [100%]

========================= 15 passed in 0.17s =========================
```

---

## 📊 Matriks Test Case & Edge Cases

| ID Case | Title | Type | Skenario Pengujian | Input / Steps | Expected Output | Status |
| :--- | :--- | :---: | :--- | :--- | :--- | :---: |
| **TC-01** | `test_ewallet_before_job_allowed` | Common | Bayar E-Wallet sebelum selesai | `"ewallet"`, `50000`, `False` | `True` | **PASSED** |
| **TC-02** | `test_transfer_before_job_allowed` | Common | Transfer bank di muka | `"transfer"`, `75000`, `False` | `True` | **PASSED** |
| **TC-03** | `test_qris_allowed` | Common | QRIS setelah selesai | `"qris"`, `30000`, `True` | `True` | **PASSED** |
| **TC-04** | `test_cash_after_job_allowed` | Common | Cash setelah pengerjaan selesai | `"cash"`, `100000`, `True` | `True` | **PASSED** |
| **TC-05** | `test_cash_before_job_rejected` | Edge | Cash sebelum pekerjaan selesai | `"cash"`, `100000`, `False` | `False` | **PASSED** |
| **TC-06** | `test_method_case_and_spaces_ignored` | Edge | Toleransi spasi & kapitalisasi | `"  QRIS "`, `20000`, `False` | `True` | **PASSED** |
| **TC-07** | `test_unknown_method_raises` | Edge | Metode pembayaran asing | `"kartu_kredit"`, `50000`, `True` | `ValueError` | **PASSED** |
| **TC-08** | `test_amount_zero_or_negative_raises` | Edge | Nominal bernilai 0 | `"ewallet"`, `0`, `True` | `ValueError` | **PASSED** |
| **TC-09** | `test_amount_zero_or_negative_raises` | Edge | Nominal negatif kecil (-1) | `"ewallet"`, `-1`, `True` | `ValueError` | **PASSED** |
| **TC-10** | `test_amount_zero_or_negative_raises` | Edge | Nominal negatif besar | `"ewallet"`, `-50000`, `True` | `ValueError` | **PASSED** |
| **TC-11** | `test_amount_non_numeric_raises` | Edge | Nominal berupa string | `"ewallet"`, `"50000"`, `True` | `ValueError` | **PASSED** |
| **TC-12** | `test_amount_non_numeric_raises` | Edge | Nominal bernilai `None` | `"ewallet"`, `None`, `True` | `ValueError` | **PASSED** |
| **TC-13** | `test_amount_non_numeric_raises` | Edge | Nominal bertipe boolean (`True`) | `"ewallet"`, `True`, `True` | `ValueError` | **PASSED** |
| **TC-14** | `test_minimum_valid_amount` | Edge | Batas bawah nominal valid (Rp1) | `"transfer"`, `1`, `False` | `True` | **PASSED** |
| **TC-15** | `test_non_string_method_raises` | Edge | Metode pembayaran bertipe `None` | `None`, `50000`, `True` | `ValueError` | **PASSED** |

---

## 💻 Cara Menjalankan Program & Testing

### 1. Menjalankan Aplikasi CLI Interaktif
```bash
python payment_modul.py
```

### 2. Menjalankan Seluruh Pengujian Unit (Core Logic)
```bash
pytest payment_function -v
```

### 3. Menjalankan Pengujian Alur CLI & Mock Input
```bash
pytest pytest_payment.py -v
```
