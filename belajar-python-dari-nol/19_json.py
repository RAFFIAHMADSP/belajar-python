# ============================================================
# 19 - JSON
# ============================================================
# JSON adalah format teks untuk menyimpan dan bertukar data.
# Module json bawaan Python membantu mengubah dictionary menjadi JSON
# dan membaca JSON kembali menjadi struktur data Python.

import json

mahasiswa = {
    "nama": "Ayu",
    "umur": 19,
    "mata_kuliah": ["Python", "Matematika", "Logika"]
}

# Mengubah dictionary menjadi string JSON.
json_teks = json.dumps(mahasiswa, indent=4, ensure_ascii=False)
print(json_teks)

# Mengubah string JSON menjadi dictionary Python.
data_kembali = json.loads(json_teks)
print("Nama:", data_kembali["nama"])

# Menyimpan JSON ke file.
with open("mahasiswa.json", "w", encoding="utf-8") as file:
    json.dump(mahasiswa, file, indent=4, ensure_ascii=False)

# Membaca JSON dari file.
with open("mahasiswa.json", "r", encoding="utf-8") as file:
    data_file = json.load(file)

print("Mata kuliah:", data_file["mata_kuliah"])

# LATIHAN:
# Buat dictionary data produk (nama, harga, stok).
# Simpan sebagai produk.json, lalu baca kembali file tersebut.
