from src.models import Mahasiswa


def test_rata_rata_tanpa_nilai():
    assert Mahasiswa("20230001", "Budi").rata_rata() == 0.0


def test_tambah_nilai_dan_rata_rata():
    mhs = Mahasiswa("20230001", "Budi")
    mhs.tambah_nilai("Basis Data", 90)
    mhs.tambah_nilai("Jaringan", 80)
    assert mhs.rata_rata() == 85.0
    assert mhs.huruf() == "A"


def test_nilai_matkul_yang_sama_ditimpa():
    mhs = Mahasiswa("20230001", "Budi")
    mhs.tambah_nilai("Basis Data", 60)
    mhs.tambah_nilai("Basis Data", 100)
    assert mhs.nilai == {"Basis Data": 100.0}


def test_ke_dict_dan_dari_dict():
    mhs = Mahasiswa("20230001", "Budi")
    mhs.tambah_nilai("Basis Data", 88)
    salinan = Mahasiswa.dari_dict(mhs.ke_dict())
    assert salinan.nim == "20230001"
    assert salinan.nama == "Budi"
    assert salinan.nilai == {"Basis Data": 88.0}
