import pytest

from src.validasi import validasi_angka, validasi_nama, validasi_nim


def test_nim_valid():
    assert validasi_nim(" 20230001 ") == "20230001"


@pytest.mark.parametrize("nim", ["123", "abcdefgh", "1234567890123", ""])
def test_nim_tidak_valid(nim):
    with pytest.raises(ValueError):
        validasi_nim(nim)


def test_nama_valid():
    assert validasi_nama("  Budi Santoso ") == "Budi Santoso"


@pytest.mark.parametrize("nama", ["", "B", "Budi123", "<script>"])
def test_nama_tidak_valid(nama):
    with pytest.raises(ValueError):
        validasi_nama(nama)


def test_angka_valid():
    assert validasi_angka("85.5") == 85.5


@pytest.mark.parametrize("teks", ["abc", "", "-1", "101"])
def test_angka_tidak_valid(teks):
    with pytest.raises(ValueError):
        validasi_angka(teks)
