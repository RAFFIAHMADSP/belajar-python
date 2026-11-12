# ============================================================
# 07 - PERCABANGAN IF, ELIF, DAN ELSE
# ============================================================
# Percabangan membuat program memilih tindakan berdasarkan kondisi.
# Perhatikan tanda titik dua (:) dan indentasi pada setiap blok.

nilai = int(input("Masukkan nilai (0-100): "))

if nilai >= 85:
    print("Nilai A")
elif nilai >= 75:
    print("Nilai B")
elif nilai >= 60:
    print("Nilai C")
else:
    print("Nilai D")

# if  : kondisi pertama yang diperiksa.
# elif: kondisi alternatif, boleh digunakan lebih dari satu kali.
# else: dijalankan jika tidak ada kondisi sebelumnya yang True.

# Contoh kondisi sederhana.
usia = 18
if usia >= 17:
    print("Boleh membuat KTP sesuai ketentuan yang berlaku.")
else:
    print("Belum memenuhi batas usia tersebut.")

# LATIHAN:
# Buat program menentukan bilangan positif, negatif, atau nol.
# Tantangan: buat program menentukan bilangan ganjil atau genap.
