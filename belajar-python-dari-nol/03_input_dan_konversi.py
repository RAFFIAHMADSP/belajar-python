# ============================================================
# 03 - INPUT DAN KONVERSI TIPE DATA
# ============================================================
# input() digunakan untuk menerima masukan dari pengguna.
# Hasil input() selalu berupa string (str), walaupun pengguna mengetik angka.

nama = input("Masukkan nama: ")
print("Halo,", nama)

# Jika masukan akan dihitung, ubah tipenya terlebih dahulu.
# int() mengubah nilai menjadi bilangan bulat.
# float() mengubah nilai menjadi bilangan desimal.

umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi badan dalam cm: "))

print("Tahun depan umur kamu:", umur + 1)
print("Tinggi badan:", tinggi, "cm")

# Contoh konversi tipe data lainnya:
angka_teks = "25"
angka_integer = int(angka_teks)
angka_float = float(angka_teks)
teks_lagi = str(angka_integer)

print(angka_integer + 5)
print(angka_float + 0.5)
print("Angka dalam bentuk teks: " + teks_lagi)

# Catatan:
# int("abc") akan menghasilkan ValueError karena "abc" bukan angka.
# Materi penanganan kesalahan akan dibahas pada file exception handling.

# LATIHAN:
# Buat program yang meminta dua angka dari pengguna, lalu tampilkan jumlahnya.
