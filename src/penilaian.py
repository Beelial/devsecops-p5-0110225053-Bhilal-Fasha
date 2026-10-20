"""Aturan penilaian: konversi angka ke huruf dan statistik kelas."""

BATAS_LULUS = 55


def konversi_huruf(angka):
    """Ubah nilai angka (0-100) menjadi nilai huruf A-E."""
    if angka < 0 or angka > 100:
        raise ValueError("Nilai harus antara 0 dan 100")
    if angka >= 85:
        return "A"
    if angka >= 70:
        return "B"
    if angka >= 55:
        return "C"
    if angka >= 40:
        return "D"
    return "E"


def apakah_lulus(angka):
    """Mahasiswa lulus jika nilainya minimal BATAS_LULUS."""
    return angka >= BATAS_LULUS


def ringkasan_kelas(daftar_rata_rata):
    """Hitung jumlah, rata-rata, tertinggi, terendah, dan persentase lulus."""
    if not daftar_rata_rata:
        return {"jumlah": 0, "rata_rata": 0.0, "tertinggi": 0.0, "terendah": 0.0, "persen_lulus": 0.0}
    jumlah = len(daftar_rata_rata)
    lulus = sum(1 for angka in daftar_rata_rata if apakah_lulus(angka))
    return {
        "jumlah": jumlah,
        "rata_rata": round(sum(daftar_rata_rata) / jumlah, 2),
        "tertinggi": max(daftar_rata_rata),
        "terendah": min(daftar_rata_rata),
        "persen_lulus": round(lulus / jumlah * 100, 2),
    }
