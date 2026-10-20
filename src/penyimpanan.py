"""Simpan dan muat data mahasiswa dari berkas JSON."""
import json
import os

from src.models import Mahasiswa


def simpan(daftar, path):
    """Tulis daftar Mahasiswa ke berkas JSON."""
    data = [mahasiswa.ke_dict() for mahasiswa in daftar]
    with open(path, "w", encoding="utf-8") as berkas:
        json.dump(data, berkas, indent=2, ensure_ascii=False)


def muat(path):
    """Baca daftar Mahasiswa dari berkas JSON; kosong jika berkas belum ada."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as berkas:
        data = json.load(berkas)
    return [Mahasiswa.dari_dict(item) for item in data]
