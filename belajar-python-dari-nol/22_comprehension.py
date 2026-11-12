# ============================================================
# 22 - LIST, SET, DAN DICTIONARY COMPREHENSION
# ============================================================
# Comprehension adalah cara ringkas membuat koleksi dari iterable.

# Cara biasa membuat list kuadrat.
kuadrat_biasa = []
for angka in range(1, 6):
    kuadrat_biasa.append(angka ** 2)
print("Cara biasa:", kuadrat_biasa)

# List comprehension: [ekspresi for item in iterable]
kuadrat = [angka ** 2 for angka in range(1, 6)]
print("List comprehension:", kuadrat)

# Dapat ditambah kondisi if.
genap = [angka for angka in range(1, 11) if angka % 2 == 0]
print("Bilangan genap:", genap)

# Set comprehension menghasilkan set (nilai unik).
huruf_unik = {huruf for huruf in "programming"}
print("Huruf unik:", huruf_unik)

# Dictionary comprehension menghasilkan dictionary.
kubik = {angka: angka ** 3 for angka in range(1, 5)}
print("Dictionary kubik:", kubik)

# Gunakan comprehension jika membuat kode lebih jelas.
# Untuk logika yang rumit, for biasa sering lebih mudah dibaca.

# LATIHAN:
# Buat list berisi kuadrat bilangan ganjil dari 1 sampai 15.
