from src.main import jalankan


def jalankan_dengan(tmp_path, jawaban):
    """Jalankan menu dengan jawaban yang sudah disiapkan, kembalikan semua output."""
    iterator = iter(jawaban)
    keluaran = []
    jalankan(str(tmp_path / "data.json"), baca=lambda prompt="": next(iterator), tulis=keluaran.append)
    return "\n".join(keluaran)


def test_alur_lengkap(tmp_path):
    hasil = jalankan_dengan(tmp_path, [
        "1", "20230001", "Budi Santoso",
        "2", "20230001", "Basis Data", "90",
        "3", "4", "0",
    ])
    assert "Mahasiswa berhasil ditambahkan" in hasil
    assert "Nilai Basis Data disimpan" in hasil
    assert "Budi Santoso | rata-rata 90.0 | A" in hasil
    assert "persen_lulus: 100.0" in hasil
    assert "Data disimpan" in hasil


def test_nim_duplikat(tmp_path):
    hasil = jalankan_dengan(tmp_path, [
        "1", "20230001", "Budi", "1", "20230001", "Siti", "0",
    ])
    assert "NIM sudah terdaftar" in hasil


def test_input_tidak_valid(tmp_path):
    hasil = jalankan_dengan(tmp_path, [
        "1", "abc", "Budi",
        "2", "99999999",
        "9", "3", "0",
    ])
    assert "Input tidak valid" in hasil
    assert "NIM tidak ditemukan" in hasil
    assert "Pilihan tidak dikenal" in hasil
    assert "Belum ada data" in hasil


def test_nilai_tidak_valid_dan_matkul_kosong(tmp_path):
    hasil = jalankan_dengan(tmp_path, [
        "1", "20230001", "Budi",
        "2", "20230001", "", 
        "2", "20230001", "Jaringan", "150",
        "0",
    ])
    assert "tidak boleh kosong" in hasil
    assert "antara 0 dan 100" in hasil


def test_data_tersimpan_dan_dimuat_lagi(tmp_path):
    jalankan_dengan(tmp_path, ["1", "20230001", "Budi", "0"])
    hasil = jalankan_dengan(tmp_path, ["3", "0"])
    assert "20230001 | Budi" in hasil
