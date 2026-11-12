# ============================================================
# 05 - OPERATOR PERBANDINGAN DAN LOGIKA
# ============================================================
# Operator perbandingan menghasilkan nilai True atau False.

x = 10
y = 5

print(x == y)  # Sama dengan
print(x != y)  # Tidak sama dengan
print(x > y)   # Lebih besar
print(x < y)   # Lebih kecil
print(x >= y)  # Lebih besar atau sama dengan
print(x <= y)  # Lebih kecil atau sama dengan

# Operator logika menggabungkan beberapa kondisi.
# and: semua kondisi harus True.
# or : minimal satu kondisi harus True.
# not: membalik nilai True menjadi False, dan sebaliknya.

umur = 20
memiliki_kartu = True

print(umur >= 17 and memiliki_kartu)
print(umur < 17 or memiliki_kartu)
print(not memiliki_kartu)

# Contoh penggunaan kondisi untuk rentang nilai.
nilai = 85
lulus = nilai >= 60 and nilai <= 100
print("Status lulus:", lulus)

# LATIHAN:
# Minta umur dan status memiliki kartu pelajar.
# Tampilkan apakah pengguna memenuhi dua syarat yang kalian tentukan.
