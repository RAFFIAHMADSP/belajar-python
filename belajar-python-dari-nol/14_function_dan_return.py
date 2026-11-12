# ============================================================
# 14 - FUNCTION, PARAMETER, DAN RETURN
# ============================================================
# Function (fungsi) adalah blok kode yang dapat dipanggil berulang kali.
# def digunakan untuk mendefinisikan fungsi.

def sapa():
    print("Halo, selamat belajar Python!")

sapa()  # Memanggil fungsi.

# Parameter menerima data ketika fungsi dipanggil.
def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Rina")

# Fungsi dapat memiliki lebih dari satu parameter.
def tambah(a, b):
    hasil = a + b
    return hasil  # Mengembalikan nilai kepada pemanggil.

hasil_penjumlahan = tambah(5, 3)
print("Hasil:", hasil_penjumlahan)

# Parameter default dipakai jika argumen tidak diberikan.
def perkenalan(nama, kampus="Kampus saya"):
    print(f"Nama saya {nama}, kuliah di {kampus}.")

perkenalan("Doni")
perkenalan("Doni", "Universitas Contoh")

# LATIHAN:
# Buat fungsi hitung_luas_persegi(panjang_sisi) yang mengembalikan luas.
# Buat fungsi cek_genap(angka) yang mengembalikan True jika genap.
