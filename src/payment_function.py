import math

# Daftar metode yang diizinkan
METODE_VALID = ["ewallet", "transfer", "cash", "qris"]


def validate_payment(method, amount, job_done):
    """
    method   : nama metode bayar, contoh "cash"
    amount   : jumlah uang, contoh 50000
    job_done : True jika pekerjaan sudah selesai, False jika belum

    Hasil:
        True  -> pembayaran boleh diproses
        False -> pembayaran ditolak (cash sebelum pekerjaan selesai)
        Error (ValueError) -> datanya salah
    """

    # --- Cek 1: metode harus berupa teks ---
    if not isinstance(method, str):
        raise ValueError("Metode pembayaran harus berupa teks")

    # Rapikan teks: buang spasi di tepi dan jadikan huruf kecil
    metode = method.strip().lower()

    # --- Cek 2: metode harus ada di daftar ---
    if metode not in METODE_VALID:
        raise ValueError("Metode pembayaran tidak didukung")

    # --- Cek 3: nominal harus berupa angka ---
    # (True/False ditolak, karena Python menganggapnya angka 1 dan 0)
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Nominal harus berupa angka")

    # --- Cek 4: nominal harus masuk akal ---
    if math.isnan(amount) or math.isinf(amount):
        raise ValueError("Nominal tidak valid")
    if amount <= 0:
        raise ValueError("Nominal harus lebih dari 0")

    # --- Cek 5: job_done harus True atau False ---
    if not isinstance(job_done, bool):
        raise ValueError("job_done harus True atau False")

    # --- Aturan utama ---
    if metode == "cash":
        return job_done   # cash: boleh hanya kalau pekerjaan sudah selesai

    return True           # metode lain: boleh kapan saja
