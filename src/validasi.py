"""Validasi input pengguna."""


def validasi_nim(teks):
    """NIM harus berupa 8-12 digit angka."""
    nim = teks.strip()
    if not (nim.isdigit() and 8 <= len(nim) <= 12):
        raise ValueError("NIM harus berupa 8-12 digit angka")
    return nim


def validasi_nama(teks):
    """Nama hanya boleh berisi huruf dan spasi, minimal 2 karakter."""
    nama = teks.strip()
    if len(nama) < 2 or not nama.replace(" ", "").isalpha():
        raise ValueError("Nama hanya boleh huruf dan spasi (minimal 2 karakter)")
    return nama


def validasi_angka(teks):
    """Ubah teks menjadi angka 0-100."""
    try:
        angka = float(teks)
    except ValueError:
        raise ValueError("Nilai harus berupa angka") from None
    if angka < 0 or angka > 100:
        raise ValueError("Nilai harus antara 0 dan 100")
    return angka
