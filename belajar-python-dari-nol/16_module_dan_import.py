# ============================================================
# 16 - MODULE DAN IMPORT
# ============================================================
# Module adalah file Python yang berisi kode yang dapat digunakan kembali.
# import digunakan untuk memakai module bawaan atau module buatan sendiri.

import math
import random

print("Akar kuadrat 81:", math.sqrt(81))
print("Nilai pi:", math.pi)
print("Angka acak 1-10:", random.randint(1, 10))

# Mengimpor fungsi tertentu saja.
from math import pow
print("2 pangkat 3:", pow(2, 3))

# Membuat alias nama module.
import datetime as dt
sekarang = dt.datetime.now()
print("Tanggal dan waktu komputer:", sekarang)

# Module buatan sendiri:
# 1. Buat file bernama matematika_sederhana.py pada folder yang sama.
# 2. Isi file tersebut dengan: def kali(a, b): return a * b
# 3. Pada file lain, tulis: from matematika_sederhana import kali
# 4. Gunakan: print(kali(4, 5))

# LATIHAN:
# Gunakan module random untuk membuat program undian nama sederhana.
