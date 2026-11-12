# ============================================================
# 25 - MINI PROJECT: TEBAK ANGKA
# ============================================================
# Project ini memakai module random, input, while, if, dan penghitung.

import random

print("=== PERMAINAN TEBAK ANGKA ===")
print("Saya memilih angka dari 1 sampai 20.")

angka_rahasia = random.randint(1, 20)
jumlah_percobaan = 0

while True:
    try:
        tebakan = int(input("Masukkan tebakan: "))
        jumlah_percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil. Coba lagi!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar. Coba lagi!")
        else:
            print(f"Benar! Angkanya adalah {angka_rahasia}.")
            print(f"Jumlah percobaan: {jumlah_percobaan}")
            break

    except ValueError:
        print("Masukkan bilangan bulat, ya.")

# PENGEMBANGAN:
# 1. Berikan batas maksimal percobaan.
# 2. Tambahkan pilihan tingkat kesulitan.
# 3. Tanyakan apakah pemain ingin bermain lagi.
