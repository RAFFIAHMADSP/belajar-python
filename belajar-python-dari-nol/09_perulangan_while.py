# ============================================================
# 09 - PERULANGAN WHILE
# ============================================================
# while mengulang blok kode selama kondisinya bernilai True.

angka = 1
while angka <= 5:
    print("Angka:", angka)
    angka += 1  # Perubahan kondisi agar perulangan suatu saat berhenti.

# Contoh meminta kata sandi sampai pengguna memasukkan jawaban benar.
# Untuk latihan, sandi di bawah ini hanya contoh sederhana.
sandi_benar = "python123"
sandi = ""

while sandi != sandi_benar:
    sandi = input("Masukkan sandi latihan: ")
    if sandi != sandi_benar:
        print("Sandi belum tepat, coba lagi.")

print("Sandi benar. Selamat datang!")

# Hati-hati infinite loop (perulangan tanpa akhir).
# Pastikan kondisi while dapat berubah atau sediakan cara untuk berhenti.

# LATIHAN:
# Buat program yang meminta angka sampai pengguna memasukkan angka 0.
# Setelah berhenti, tampilkan jumlah angka yang sudah dimasukkan (tanpa 0).
