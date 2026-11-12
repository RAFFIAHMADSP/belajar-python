# ============================================================
# 23 - ALGORITMA DASAR
# ============================================================
# Algoritma adalah urutan langkah untuk menyelesaikan masalah.
# Contoh berikut mengenalkan pencarian dan pengurutan sederhana.

# 1. Linear search: memeriksa elemen satu per satu.
def cari_data(data, target):
    for indeks, nilai in enumerate(data):
        if nilai == target:
            return indeks
    return -1  # -1 menandakan data tidak ditemukan.

angka = [8, 3, 6, 2, 9]
print("Indeks angka 6:", cari_data(angka, 6))
print("Indeks angka 7:", cari_data(angka, 7))

# 2. Bubble sort: membandingkan elemen bersebelahan dan menukarnya
# jika urutannya salah. Ini untuk belajar konsep, bukan pilihan tercepat.
def bubble_sort(data):
    hasil = data.copy()  # Salin agar list asli tidak berubah.
    n = len(hasil)
    for i in range(n):
        for j in range(0, n - i - 1):
            if hasil[j] > hasil[j + 1]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
    return hasil

print("Sebelum diurutkan:", angka)
print("Sesudah diurutkan:", bubble_sort(angka))

# LATIHAN:
# Buat fungsi untuk mencari nilai terbesar dalam list tanpa max().
