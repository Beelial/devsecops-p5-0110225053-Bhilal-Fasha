# Pencatat Nilai Mahasiswa

Proyek untuk tugas **Pertemuan 5: Pipeline DevSecOps dengan GitHub Actions**.
Pipeline ini menjalankan build, unit test, **SAST (Bandit)**, dan **Quality Gate** secara otomatis.

## 1. Nama Aplikasi dan Fungsinya

**Pencatat Nilai Mahasiswa** adalah program berbasis teks (CLI) untuk mencatat nilai mahasiswa.

Fungsi utama:

- Menambah mahasiswa (NIM dan nama).
- Mengisi nilai per mata kuliah.
- Menghitung rata-rata dan nilai huruf (A-E).
- Menampilkan statistik kelas: jumlah, rata-rata, tertinggi, terendah, dan persen lulus.
- Menyimpan data ke berkas JSON agar tidak hilang saat program ditutup.

## 2. Bahasa dan Framework

- **Bahasa:** Python 3.12 (tanpa framework, hanya library bawaan)
- **Unit test:** pytest
- **SAST tool:** Bandit
- **CI/CD:** GitHub Actions

Struktur proyek:

```
.
├── .github/workflows/devsecops.yml   # definisi pipeline
├── src/
│   ├── main.py          # menu utama
│   ├── models.py        # class Mahasiswa
│   ├── penilaian.py     # konversi huruf dan statistik
│   ├── validasi.py      # validasi input
│   └── penyimpanan.py   # simpan dan muat JSON
├── tests/               # unit test
└── requirements.txt
```

## 3. Cara Menjalankan Aplikasi

```bash
# 1. Clone repository
git clone https://github.com/<username>/devsecops-p5-<nim>.git
cd devsecops-p5-<nim>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
python -m src.main

# 4. Jalankan unit test
pytest -v
```

## 4. Overview Pipeline CI/CD

Pipeline ada di `.github/workflows/devsecops.yml` dan berjalan saat **push** atau **pull request** ke branch `main`.
Semua job memakai runner `ubuntu-latest`.

```
build  ──►  sast-scan (termasuk Quality Gate)
```

| Job | Tugas |
|---|---|
| `build` | Install dependencies dan jalankan unit test dengan pytest |
| `sast-scan` | Pindai kode dengan **Bandit**, simpan laporan, lalu jalankan **Quality Gate** |

**Quality Gate:** pipeline dinyatakan **gagal** jika Bandit menemukan kerentanan dengan severity **MEDIUM** atau **HIGH**
(perintah `bandit -r src -ll`). Temuan severity LOW hanya menjadi informasi.

### Menjalankan SAST secara lokal

```bash
pip install bandit
bandit -r src        # tampilkan semua temuan
bandit -r src -ll    # Quality Gate: gagal jika ada MEDIUM/HIGH
```
