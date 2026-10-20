"""Model data mahasiswa."""
from src.penilaian import konversi_huruf


class Mahasiswa:
    """Menyimpan identitas mahasiswa dan nilai mata kuliahnya."""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.nilai = {}  # contoh: {"Basis Data": 85.0}

    def tambah_nilai(self, matkul, angka):
        """Tambah atau perbarui nilai untuk satu mata kuliah."""
        self.nilai[matkul] = float(angka)

    def rata_rata(self):
        """Rata-rata semua nilai; 0.0 jika belum ada nilai."""
        if not self.nilai:
            return 0.0
        return round(sum(self.nilai.values()) / len(self.nilai), 2)

    def huruf(self):
        """Nilai huruf berdasarkan rata-rata."""
        return konversi_huruf(self.rata_rata())

    def ke_dict(self):
        """Ubah ke dictionary agar bisa disimpan sebagai JSON."""
        return {"nim": self.nim, "nama": self.nama, "nilai": self.nilai}

    @classmethod
    def dari_dict(cls, data):
        """Buat objek Mahasiswa dari dictionary hasil ke_dict()."""
        mahasiswa = cls(data["nim"], data["nama"])
        for matkul, angka in data.get("nilai", {}).items():
            mahasiswa.tambah_nilai(matkul, angka)
        return mahasiswa
