# ============================================================
# 17 - EXCEPTION HANDLING (PENANGANAN KESALAHAN)
# ============================================================
# try-except membuat program dapat menangani error tertentu.
# Program tidak langsung berhenti jika kesalahan yang ditangani terjadi.

try:
    angka = int(input("Masukkan bilangan bulat: "))
    hasil = 100 / angka
except ValueError:
    print("Input harus berupa bilangan bulat.")
except ZeroDivisionError:
    print("Angka tidak boleh nol karena pembagian dengan nol tidak diperbolehkan.")
else:
    # else dijalankan jika tidak ada exception.
    print("Hasil:", hasil)
finally:
    # finally tetap dijalankan, baik terjadi error maupun tidak.
    print("Pemeriksaan input selesai.")

# raise digunakan untuk memunculkan exception secara sengaja.
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif.")
    return umur

try:
    print(cek_umur(19))
except ValueError as error:
    print("Terjadi kesalahan:", error)

# LATIHAN:
# Minta pengguna memasukkan dua angka dan lakukan pembagian.
# Tangani input bukan angka dan pembagian dengan nol.
