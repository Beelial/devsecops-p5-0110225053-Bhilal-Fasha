"""Program utama: menu teks untuk mencatat nilai mahasiswa.

Jalankan dengan: python -m src.main
"""
from src.models import Mahasiswa
from src.penilaian import ringkasan_kelas
from src.penyimpanan import muat, simpan
from src.validasi import validasi_angka, validasi_nama, validasi_nim

FILE_DATA = "data_mahasiswa.json"

MENU = """
=== Pencatat Nilai Mahasiswa ===
1. Tambah mahasiswa
2. Input nilai
3. Lihat daftar mahasiswa
4. Statistik kelas
0. Simpan dan keluar
"""


def cari(daftar, nim):
    """Cari mahasiswa berdasarkan NIM; None jika tidak ada."""
    for mahasiswa in daftar:
        if mahasiswa.nim == nim:
            return mahasiswa
    return None


def tambah_mahasiswa(daftar, baca, tulis):
    try:
        nim = validasi_nim(baca("NIM  : "))
        nama = validasi_nama(baca("Nama : "))
    except ValueError as error:
        tulis(f"Input tidak valid: {error}")
        return
    if cari(daftar, nim) is not None:
        tulis("NIM sudah terdaftar.")
        return
    daftar.append(Mahasiswa(nim, nama))
    tulis("Mahasiswa berhasil ditambahkan.")


def input_nilai(daftar, baca, tulis):
    mahasiswa = cari(daftar, baca("NIM mahasiswa : ").strip())
    if mahasiswa is None:
        tulis("NIM tidak ditemukan.")
        return
    matkul = baca("Mata kuliah : ").strip()
    if not matkul:
        tulis("Nama mata kuliah tidak boleh kosong.")
        return
    try:
        angka = validasi_angka(baca("Nilai (0-100) : "))
    except ValueError as error:
        tulis(f"Input tidak valid: {error}")
        return
    mahasiswa.tambah_nilai(matkul, angka)
    tulis(f"Nilai {matkul} disimpan.")


def lihat_daftar(daftar, tulis):
    if not daftar:
        tulis("Belum ada data.")
        return
    for mahasiswa in daftar:
        tulis(f"{mahasiswa.nim} | {mahasiswa.nama} | rata-rata {mahasiswa.rata_rata()} | {mahasiswa.huruf()}")


def lihat_statistik(daftar, tulis):
    ringkasan = ringkasan_kelas([m.rata_rata() for m in daftar if m.nilai])
    for kunci, isi in ringkasan.items():
        tulis(f"{kunci}: {isi}")


def jalankan(file_data=FILE_DATA, baca=input, tulis=print):
    """Loop menu utama. baca/tulis bisa diganti agar mudah diuji."""
    daftar = muat(file_data)
    while True:
        tulis(MENU)
        pilihan = baca("Pilih menu: ").strip()
        if pilihan == "1":
            tambah_mahasiswa(daftar, baca, tulis)
        elif pilihan == "2":
            input_nilai(daftar, baca, tulis)
        elif pilihan == "3":
            lihat_daftar(daftar, tulis)
        elif pilihan == "4":
            lihat_statistik(daftar, tulis)
        elif pilihan == "0":
            simpan(daftar, file_data)
            tulis("Data disimpan. Sampai jumpa!")
            break
        else:
            tulis("Pilihan tidak dikenal.")


if __name__ == "__main__":
    jalankan()
