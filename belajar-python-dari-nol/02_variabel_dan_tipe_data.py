# ============================================================
# 02 - VARIABEL DAN TIPE DATA
# ============================================================
# Variabel adalah nama yang digunakan untuk menyimpan suatu nilai.
# Gunakan tanda = untuk memberikan nilai ke variabel.

nama = "Andi"              # str: teks
umur = 19                  # int: bilangan bulat
berat_badan = 50.5         # float: bilangan desimal
mahasiswa_aktif = True     # bool: True atau False

print("Nama:", nama)
print("Umur:", umur)
print("Berat badan:", berat_badan)
print("Mahasiswa aktif:", mahasiswa_aktif)

# type() digunakan untuk mengetahui tipe data sebuah nilai.
print(type(nama))
print(type(umur))
print(type(berat_badan))
print(type(mahasiswa_aktif))

# Aturan nama variabel:
# - Tidak boleh diawali angka.
# - Tidak boleh mengandung spasi. Gunakan garis bawah (_).
# - Tidak boleh memakai kata kunci Python seperti if, for, atau class.
# - Nama variabel peka terhadap huruf besar dan kecil.

# Nilai variabel dapat diubah.
jumlah = 10
jumlah = 15
print("Jumlah terbaru:", jumlah)

# LATIHAN:
# Buat variabel berisi nama, umur, jurusan, IPK, dan status mahasiswa.
# Tampilkan semua variabel beserta tipe datanya.
