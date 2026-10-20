import hashlib
import subprocess

def jalankan_perintah(masukan_pengguna):
      return subprocess.call("ls " + masukan_pengguna, shell=True)

def hash_kata_sandi(kata_sandi):
     return hashlib.md5(kata_sandi.encode()).hexdigest()