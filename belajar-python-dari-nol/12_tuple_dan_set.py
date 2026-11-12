# ============================================================
# 12 - TUPLE DAN SET
# ============================================================
# TUPLE mirip list, tetapi elemennya tidak dapat diubah setelah dibuat.
koordinat = (10, 20)
print("Koordinat:", koordinat)
print("Nilai x:", koordinat[0])

# Tuple dengan satu elemen harus memakai koma.
satu_data = (7,)

# SET menyimpan nilai unik (tidak duplikat) dan tidak memakai indeks.
angka = {1, 2, 2, 3, 3, 3}
print("Set tanpa duplikat:", angka)

angka.add(4)
angka.discard(2)  # discard tidak error jika nilai tidak ditemukan.
print("Set setelah perubahan:", angka)

# Operasi himpunan.
a = {1, 2, 3}
b = {3, 4, 5}
print("Gabungan:", a | b)
print("Irisan:", a & b)
print("Selisih a - b:", a - b)

# LATIHAN:
# 1. Buat tuple berisi nama, umur, dan jurusan.
# 2. Buat dua set berisi angka, lalu tampilkan gabungan dan irisannya.
