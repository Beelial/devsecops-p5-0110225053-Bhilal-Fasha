from src.models import Mahasiswa
from src.penyimpanan import muat, simpan


def test_muat_berkas_belum_ada(tmp_path):
    assert muat(str(tmp_path / "tidak_ada.json")) == []


def test_simpan_lalu_muat(tmp_path):
    path = str(tmp_path / "data.json")
    mhs = Mahasiswa("20230001", "Budi")
    mhs.tambah_nilai("Basis Data", 90)
    simpan([mhs], path)

    hasil = muat(path)
    assert len(hasil) == 1
    assert hasil[0].nama == "Budi"
    assert hasil[0].nilai == {"Basis Data": 90.0}
