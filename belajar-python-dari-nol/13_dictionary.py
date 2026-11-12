# ============================================================
# 13 - DICTIONARY
# ============================================================
# Dictionary menyimpan data dalam pasangan key (kunci) dan value (nilai).
# Setiap key harus unik.

mahasiswa = {
    "nama": "Sinta",
    "umur": 19,
    "jurusan": "Teknik Informatika"
}

print(mahasiswa)
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa.get("umur"))

# Menambah atau mengubah data.
mahasiswa["semester"] = 1
mahasiswa["umur"] = 20

# Menghapus data.
mahasiswa.pop("semester")

# Mengambil key, value, atau pasangan key-value.
print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

# Mengulang dictionary.
for kunci, nilai in mahasiswa.items():
    print(f"{kunci}: {nilai}")

# LATIHAN:
# Buat dictionary data buku dengan key judul, penulis, dan tahun.
# Tampilkan setiap pasangan key dan value menggunakan for.
