import pytest

from src.penilaian import apakah_lulus, konversi_huruf, ringkasan_kelas


@pytest.mark.parametrize(
    "angka,huruf",
    [(100, "A"), (85, "A"), (84, "B"), (70, "B"), (55, "C"), (40, "D"), (39, "E"), (0, "E")],
)
def test_konversi_huruf(angka, huruf):
    assert konversi_huruf(angka) == huruf


@pytest.mark.parametrize("angka", [-1, 101])
def test_konversi_huruf_di_luar_rentang(angka):
    with pytest.raises(ValueError):
        konversi_huruf(angka)


def test_apakah_lulus():
    assert apakah_lulus(55) is True
    assert apakah_lulus(54.9) is False


def test_ringkasan_kelas_kosong():
    assert ringkasan_kelas([])["jumlah"] == 0


def test_ringkasan_kelas():
    hasil = ringkasan_kelas([90, 70, 50, 60])
    assert hasil["jumlah"] == 4
    assert hasil["rata_rata"] == 67.5
    assert hasil["tertinggi"] == 90
    assert hasil["terendah"] == 50
    assert hasil["persen_lulus"] == 75.0
