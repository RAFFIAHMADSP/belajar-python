# ============================================================
# 18 - FILE HANDLING (MEMBACA DAN MENULIS FILE)
# ============================================================
# Python dapat membaca dan menulis file teks.
# Mode "w" membuat/menimpa file, sedangkan "a" menambahkan isi di akhir.
# Mode "r" digunakan untuk membaca file.
# with akan menutup file secara otomatis setelah blok selesai.

nama_file = "catatan_belajar.txt"

# Menulis file. Jika file sudah ada, isinya akan diganti.
with open(nama_file, "w", encoding="utf-8") as file:
    file.write("Saya sedang belajar Python.\n")
    file.write("Materi file handling.\n")

# Menambahkan baris tanpa menghapus isi yang sudah ada.
with open(nama_file, "a", encoding="utf-8") as file:
    file.write("Saya akan terus berlatih.\n")

# Membaca seluruh isi file.
with open(nama_file, "r", encoding="utf-8") as file:
    isi = file.read()

print("Isi file:")
print(isi)

# Catatan:
# File dibuat pada current working directory (folder kerja terminal).
# Jangan membuka file dari sumber yang tidak dipercaya secara sembarangan.

# LATIHAN:
# Buat file daftar_tugas.txt, tulis tiga tugas, lalu baca dan tampilkan.
