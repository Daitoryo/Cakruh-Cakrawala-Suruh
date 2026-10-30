import pytest

from payment import validate_payment


# ===============================================================
# KASUS UMUM (common case): pembayaran normal
# ===============================================================

def test_ewallet_before_job_allowed():
    """[D6: TC-PAY-01] E-wallet boleh dibayar sebelum pekerjaan selesai."""
    assert validate_payment("ewallet", 50000, False) is True


def test_transfer_before_job_allowed():
    """[D6: TC-PAY-02] Transfer bank boleh dibayar di muka."""
    assert validate_payment("transfer", 75000, False) is True


def test_qris_allowed():
    """[D6: TC-PAY-03] QRIS boleh dibayar setelah pekerjaan selesai."""
    assert validate_payment("qris", 30000, True) is True


def test_cash_after_job_allowed():
    """[D6: TC-PAY-04] Cash boleh dibayar setelah pekerjaan selesai."""
    assert validate_payment("cash", 100000, True) is True


# ===============================================================
# KASUS TEPI (edge case): data aneh atau di batas
# ===============================================================

def test_cash_before_job_rejected():
    """[D6: TC-PAY-05] Cash ditolak kalau pekerjaan belum selesai."""
    assert validate_payment("cash", 100000, False) is False


def test_method_case_and_spaces_ignored():
    """[D6: TC-PAY-06] Huruf besar dan spasi di tepi tidak masalah."""
    assert validate_payment("  QRIS ", 20000, False) is True


def test_unknown_method_raises():
    """[D6: TC-PAY-07] Metode yang tidak dikenal menghasilkan error."""
    with pytest.raises(ValueError):
        validate_payment("kartu_kredit", 50000, True)


def test_non_string_method_raises():
    """[D6: TC-PAY-15] Metode yang bukan teks menghasilkan error."""
    with pytest.raises(ValueError):
        validate_payment(None, 50000, True)


@pytest.mark.parametrize("nominal", [0, -1, -50000])
def test_amount_zero_or_negative_raises(nominal):
    """[D6: TC-PAY-08, 09, 10] Nominal nol atau minus menghasilkan error."""
    with pytest.raises(ValueError):
        validate_payment("ewallet", nominal, True)


@pytest.mark.parametrize("nominal", ["50000", None, True])
def test_amount_non_numeric_raises(nominal):
    """[D6: TC-PAY-11, 12, 13] Nominal bukan angka menghasilkan error."""
    with pytest.raises(ValueError):
        validate_payment("ewallet", nominal, True)


def test_minimum_valid_amount():
    """[D6: TC-PAY-14] Nominal terkecil yang sah (1) harus diterima."""
    assert validate_payment("transfer", 1, False) is True


# ===============================================================
# TES TAMBAHAN: celah yang ditemukan saat pengecekan
# ===============================================================

@pytest.mark.parametrize("nominal", [float("nan"), float("inf")])
def test_amount_nan_or_infinity_raises(nominal):
    """[BARU] Nominal 'nan' dan 'inf' bukan uang yang masuk akal."""
    with pytest.raises(ValueError):
        validate_payment("qris", nominal, True)


@pytest.mark.parametrize("status", ["false", None])
def test_job_done_must_be_true_or_false(status):
    """[BARU] job_done berupa teks 'false' tidak boleh dianggap True."""
    with pytest.raises(ValueError):
        validate_payment("cash", 5000, status)
