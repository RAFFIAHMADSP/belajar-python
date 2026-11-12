# ============================================================
# 06 - STRING DAN FORMAT TEKS
# ============================================================
# String adalah tipe data untuk menyimpan teks.

kalimat = "Saya sedang belajar Python"
print(kalimat)

# Mengakses karakter menggunakan indeks. Indeks dimulai dari 0.
print(kalimat[0])   # S
print(kalimat[1])   # a
print(kalimat[-1])  # n (karakter terakhir)

# Slicing mengambil sebagian string: teks[mulai:akhir].
# Indeks akhir tidak ikut diambil.
print(kalimat[0:4])
print(kalimat[5:])

# Beberapa method string yang sering dipakai.
teks = "  Belajar Python  "
print(teks.strip())
print(teks.lower())
print(teks.upper())
print(teks.replace("Python", "Pemrograman"))
print("python" in teks.lower())

# f-string memudahkan menyisipkan variabel ke dalam teks.
nama = "Budi"
umur = 19
print(f"Nama saya {nama}, umur saya {umur} tahun.")

# LATIHAN:
# Minta pengguna memasukkan nama lengkap.
# Tampilkan nama dalam huruf kapital dan jumlah karakternya.
# Petunjuk: gunakan upper() dan len().
