# ============================================================
# 11 - LIST
# ============================================================
# List menyimpan banyak nilai dalam satu variabel.
# List dapat diubah, dan indeksnya dimulai dari 0.

buah = ["apel", "jeruk", "mangga"]
print(buah)
print(buah[0])
print(buah[-1])

# Mengubah item berdasarkan indeks.
buah[1] = "pisang"
print(buah)

# Menambah dan menghapus item.
buah.append("anggur")          # Menambah di akhir.
buah.insert(1, "semangka")     # Menambah pada indeks tertentu.
buah.remove("apel")            # Menghapus berdasarkan nilai.
item_terakhir = buah.pop()      # Menghapus dan mengambil item terakhir.
print(buah)
print("Item yang di-pop:", item_terakhir)

# Fungsi/method list yang sering digunakan.
angka = [5, 2, 8, 1]
print("Panjang:", len(angka))
print("Nilai terbesar:", max(angka))
print("Nilai terkecil:", min(angka))
print("Jumlah:", sum(angka))
angka.sort()
print("Urut naik:", angka)
angka.reverse()
print("Urut terbalik:", angka)

# Mengulang list.
for item in buah:
    print(item)

# LATIHAN:
# Buat list berisi 5 nama teman.
# Tambahkan satu nama, hapus satu nama, lalu tampilkan seluruh nama.
