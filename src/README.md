## D7 - UNIT TEST CODE
Folder ini berisi Unit Test untuk Modul Payment pada aplikasi Cakruh

## Struktur File
- **`payment_function.py` / `payment_modul.py`**: Logika utama aplikasi untuk modul pembayaran. Fungsi yang diuji adalah validasi metode pembayaran.
- **`pytest_payment.py`**: Berisi kumpulan test cases yang ditulis menggunakan `pytest`. File ini menguji berbagai skenario mulai dari (*common cases*) hingga (*edge cases*).



## Cara Menjalankan Pengujian

Untuk menjalankan semua unit test, buka terminal, arahkan ke folder yang berisi file ini (misalnya folder `src` atau `tests`), dan jalankan perintah berikut:

```bash
pip install pytest
```

```bash
pytest pytest_payment.py -v
```
