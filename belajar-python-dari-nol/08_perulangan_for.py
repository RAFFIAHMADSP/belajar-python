# ============================================================
# 08 - PERULANGAN FOR
# ============================================================
# for digunakan untuk mengulang setiap item pada suatu kumpulan data
# atau mengulang sejumlah langkah tertentu.

# range(5) menghasilkan angka 0, 1, 2, 3, 4.
for i in range(5):
    print("Perulangan ke-", i)

# range(mulai, berhenti) tidak menyertakan angka berhenti.
for angka in range(1, 6):
    print(angka)

# range(mulai, berhenti, langkah).
for angka in range(2, 11, 2):
    print("Bilangan genap:", angka)

# Menghitung jumlah bilangan 1 sampai 5.
total = 0
for angka in range(1, 6):
    total = total + angka
print("Jumlah:", total)

# Mengulang isi list.
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print("Saya suka", item)

# LATIHAN:
# 1. Tampilkan kelipatan 3 dari 3 sampai 30.
# 2. Hitung jumlah seluruh bilangan 1 sampai 100.
# 3. Tampilkan tabel perkalian dari angka pilihan pengguna.
