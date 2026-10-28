import pytest

import payment_saja as p

CASH = "Bayar di Tempat (Cash)"


@pytest.fixture(autouse=True)
def bersihkan_riwayat():
    """Dijalankan otomatis sebelum setiap tes, supaya riwayat selalu kosong."""
    p.riwayat.clear()


def isi_input(monkeypatch, daftar_jawaban):
    """
    Mengganti input() dengan jawaban palsu secara berurutan.
    Contoh: isi_input(monkeypatch, ["Andi", "Fotokopi"])
    -> input() pertama menjawab "Andi", input() kedua menjawab "Fotokopi".
    """
    jawaban = iter(daftar_jawaban)
    monkeypatch.setattr("builtins.input", lambda teks="": next(jawaban))


# TES FUNGSI rupiah()

@pytest.mark.parametrize("angka, hasil", [
    (500, "Rp500"),
    (10000, "Rp10.000"),
    (1500000, "Rp1.500.000"),
])
def test_rupiah_format(angka, hasil):
    assert p.rupiah(angka) == hasil


# TES FUNGSI bayar()  (inti aturan payment)

def test_cash_ditolak_jika_pekerjaan_belum_selesai():
    berhasil, pesan = p.bayar("Andi", "Fotokopi", 5000, CASH,
                              pekerjaan_selesai=False)
    assert berhasil is False
    assert "setelah pekerjaan selesai" in pesan


def test_cash_diterima_jika_pekerjaan_sudah_selesai():
    berhasil, pesan = p.bayar("Andi", "Fotokopi", 5000, CASH,
                              pekerjaan_selesai=True)
    assert berhasil is True
    assert pesan == "Pembayaran berhasil."


@pytest.mark.parametrize("metode, detail", [
    ("E-Wallet", "GoPay"),
    ("Transfer Bank", "BCA"),
    ("QRIS", ""),
])
def test_metode_non_cash_boleh_bayar_duluan(metode, detail):
    # pekerjaan_selesai=False artinya pembayaran dilakukan di awal
    berhasil, _ = p.bayar("Siti", "Beli makan", 10000, metode, detail,
                          pekerjaan_selesai=False)
    assert berhasil is True


@pytest.mark.parametrize("jumlah", [0, -1000])
def test_jumlah_tidak_valid_ditolak(jumlah):
    berhasil, pesan = p.bayar("Budi", "Antar paket", jumlah, "QRIS")
    assert berhasil is False
    assert "lebih dari 0" in pesan


def test_pembayaran_berhasil_tersimpan_di_riwayat():
    p.bayar("Siti", "Beli makan", 10000, "E-Wallet", "OVO")

    assert len(p.riwayat) == 1
    data = p.riwayat[0]
    assert data["nama"] == "Siti"
    assert data["jasa"] == "Beli makan"
    assert data["jumlah"] == 10000
    assert data["metode"] == "E-Wallet"
    assert data["detail"] == "OVO"


def test_pembayaran_gagal_tidak_masuk_riwayat():
    p.bayar("Andi", "Fotokopi", 5000, CASH, pekerjaan_selesai=False)
    p.bayar("Andi", "Fotokopi", 0, "QRIS")

    assert p.riwayat == []


# TES FUNGSI BANTU INPUT

def test_input_angka_mengulang_sampai_benar(monkeypatch, capsys):
    # tiga jawaban salah dulu, baru yang keempat benar
    isi_input(monkeypatch, ["abc", "0", "-5", "7500"])

    hasil = p.input_angka("Masukkan angka: ")

    assert hasil == 7500
    assert "Masukkan angka yang benar" in capsys.readouterr().out


def test_pilih_dari_daftar_mengulang_jika_salah(monkeypatch):
    isi_input(monkeypatch, ["9", "x", "2"])

    hasil = p.pilih_dari_daftar("Pilih bank:", p.DAFTAR_BANK)

    assert hasil == "BRI"   # nomor 2 di DAFTAR_BANK


# TES MENU PEMBAYARAN

def test_menu_cash_belum_selesai_gagal(monkeypatch, capsys):
    isi_input(monkeypatch, ["Andi", "Fotokopi", "5000", "3", "n"])

    p.menu_bayar()

    assert "Gagal" in capsys.readouterr().out
    assert p.riwayat == []


def test_menu_cash_uang_kurang_dibatalkan(monkeypatch, capsys):
    isi_input(monkeypatch, ["Andi", "Fotokopi", "10000", "3", "y", "5000"])

    p.menu_bayar()

    assert "Uang kurang" in capsys.readouterr().out
    assert p.riwayat == []


def test_menu_cash_berhasil_dengan_kembalian(monkeypatch, capsys):
    isi_input(monkeypatch, ["Siti", "Beli makan", "10000", "3", "y", "15000"])

    p.menu_bayar()

    keluar = capsys.readouterr().out
    assert "Kembalian: Rp5.000" in keluar
    assert "LUNAS" in keluar
    assert len(p.riwayat) == 1


def test_menu_ewallet_berhasil(monkeypatch, capsys):
    # metode "1" = E-Wallet, lalu pilih nomor 2 = OVO
    isi_input(monkeypatch, ["Budi", "Antar paket", "8000", "1", "2"])

    p.menu_bayar()

    assert "OVO" in capsys.readouterr().out
    assert p.riwayat[0]["detail"] == "OVO"


def test_menu_transfer_bank_berhasil(monkeypatch):
    # metode "2" = Transfer Bank, lalu pilih nomor 1 = BCA
    isi_input(monkeypatch, ["Budi", "Antar paket", "8000", "2", "1"])

    p.menu_bayar()

    assert p.riwayat[0]["metode"] == "Transfer Bank"
    assert p.riwayat[0]["detail"] == "BCA"


def test_menu_qris_berhasil(monkeypatch, capsys):
    isi_input(monkeypatch, ["Budi", "Antar paket", "8000", "4"])

    p.menu_bayar()

    assert "QRIS" in capsys.readouterr().out
    assert len(p.riwayat) == 1


def test_menu_metode_tidak_valid(monkeypatch, capsys):
    isi_input(monkeypatch, ["Budi", "Antar paket", "8000", "9"])

    p.menu_bayar()

    assert "Metode tidak valid" in capsys.readouterr().out
    assert p.riwayat == []


# TES MENU RIWAYAT DAN MENU UTAMA

def test_menu_riwayat_kosong(capsys):
    p.menu_riwayat()

    assert "Belum ada pembayaran" in capsys.readouterr().out


def test_menu_riwayat_menampilkan_total(capsys):
    p.bayar("Siti", "Beli makan", 10000, "QRIS")
    p.bayar("Budi", "Antar paket", 8000, "E-Wallet", "OVO")

    p.menu_riwayat()

    keluar = capsys.readouterr().out
    assert "Siti" in keluar
    assert "Budi" in keluar
    assert "Rp18.000" in keluar


def test_menu_utama_keluar(monkeypatch, capsys):
    isi_input(monkeypatch, ["0"])

    p.main()

    assert "Sampai jumpa" in capsys.readouterr().out


def test_menu_utama_pilihan_salah_lalu_keluar(monkeypatch, capsys):
    isi_input(monkeypatch, ["99", "0"])

    p.main()

    keluar = capsys.readouterr().out
    assert "Menu tidak valid" in keluar
    assert "Sampai jumpa" in keluar
