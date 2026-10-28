"""Modul payment aplikasi Cakruh (Cakrawala Suruh).

Fungsi yang diuji: validate_payment()
Aturan (dari spesifikasi modul payment):
  - Metode yang tersedia: e-wallet, transfer bank, bayar di tempat (cash), QRIS.
  - Cash hanya boleh dibayar SETELAH pengerjaan selesai.
  - Transfer bank boleh dibayar terlebih dahulu (sebelum pengerjaan).
  - E-wallet dan QRIS bisa dibayar kapan saja.
"""

SUPPORTED_METHODS = {"ewallet", "transfer", "cash", "qris"}


def validate_payment(method, amount, job_done):
    """Cek apakah pembayaran boleh diproses.

    Args:
        method (str): "ewallet", "transfer", "cash", atau "qris"
                      (tidak case-sensitive, spasi di tepi diabaikan).
        amount (int | float): nominal pembayaran, harus > 0.
        job_done (bool): True jika petugas sudah selesai mengerjakan.

    Returns:
        bool: True jika pembayaran boleh diproses, False jika ditolak
              (cash sebelum pengerjaan selesai).

    Raises:
        ValueError: metode tidak dikenal atau nominal tidak valid.
    """
    if not isinstance(method, str):
        raise ValueError("Metode pembayaran harus berupa string")

    normalized = method.strip().lower()
    if normalized not in SUPPORTED_METHODS:
        raise ValueError(f"Metode pembayaran tidak didukung: {method!r}")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Nominal harus berupa angka")
    if amount <= 0:
        raise ValueError("Nominal harus lebih dari 0")

    if normalized == "cash":
        return bool(job_done)

    return True
