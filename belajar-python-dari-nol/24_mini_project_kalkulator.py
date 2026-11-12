# ============================================================
# 24 - MINI PROJECT: KALKULATOR SEDERHANA
# ============================================================
# Project ini menggabungkan input, konversi tipe, percabangan,
# operator aritmatika, dan exception handling.

print("=== KALKULATOR SEDERHANA ===")

try:
    angka_1 = float(input("Masukkan angka pertama: "))
    operator = input("Pilih operator (+, -, *, /): ").strip()
    angka_2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = angka_1 + angka_2
    elif operator == "-":
        hasil = angka_1 - angka_2
    elif operator == "*":
        hasil = angka_1 * angka_2
    elif operator == "/":
        if angka_2 == 0:
            print("Error: tidak bisa membagi dengan nol.")
        else:
            hasil = angka_1 / angka_2
    else:
        print("Operator tidak dikenal.")

    # Variabel hasil hanya dibuat jika operator valid dan pembagian aman.
    if operator in ("+", "-", "*") or (operator == "/" and angka_2 != 0):
        print(f"Hasil: {hasil}")

except ValueError:
    print("Input angka tidak valid. Masukkan angka, bukan teks.")

# PENGEMBANGAN:
# 1. Tambahkan operator pangkat (**), modulus (%), dan pembagian bulat (//).
# 2. Buat menu agar kalkulator dapat digunakan berulang kali.
