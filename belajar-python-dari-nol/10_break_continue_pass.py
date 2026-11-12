# ============================================================
# 10 - BREAK, CONTINUE, DAN PASS
# ============================================================
# break menghentikan perulangan secara langsung.
for angka in range(1, 10):
    if angka == 5:
        break
    print("break:", angka)

# continue melewati sisa kode pada putaran saat ini lalu lanjut mengulang.
for angka in range(1, 6):
    if angka == 3:
        continue
    print("continue:", angka)

# pass tidak melakukan apa-apa. Biasanya dipakai sebagai placeholder.
for angka in range(3):
    pass  # Kode dapat ditambahkan di sini nanti.

print("Program selesai.")

# LATIHAN:
# Tampilkan angka 1 sampai 20, tetapi lewati kelipatan 4.
# Hentikan perulangan ketika mencapai angka 17.
