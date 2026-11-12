# ============================================================
# 15 - SCOPE, LAMBDA, DAN RECURSION
# ============================================================
# SCOPE adalah area tempat sebuah variabel dapat diakses.
# Variabel lokal dibuat di dalam fungsi.
# Variabel global dibuat di luar fungsi.

pesan_global = "Saya variabel global"

def contoh_scope():
    pesan_lokal = "Saya variabel lokal"
    print(pesan_lokal)
    print(pesan_global)

contoh_scope()
# print(pesan_lokal)  # Error: variabel lokal tidak tersedia di luar fungsi.

# LAMBDA adalah fungsi kecil tanpa nama, biasanya untuk ekspresi singkat.
kuadrat = lambda angka: angka ** 2
print("Kuadrat 5:", kuadrat(5))

# RECURSION adalah fungsi yang memanggil dirinya sendiri.
# Wajib memiliki kondisi dasar (base case) agar tidak terus memanggil diri.
def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif.")
    if n == 0 or n == 1:  # Kondisi dasar.
        return 1
    return n * faktorial(n - 1)

print("Faktorial 5:", faktorial(5))

# LATIHAN:
# Buat fungsi rekursif untuk menghitung jumlah bilangan 1 sampai n.
