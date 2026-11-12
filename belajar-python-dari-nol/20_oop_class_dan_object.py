# ============================================================
# 20 - OOP: CLASS DAN OBJECT
# ============================================================
# OOP (Object-Oriented Programming) adalah paradigma pemrograman
# yang mengelompokkan data dan perilaku ke dalam object.
# Class adalah cetak biru, sedangkan object adalah hasil dari class.

class Mahasiswa:
    # __init__ adalah constructor yang dipanggil saat object dibuat.
    # self merujuk pada object yang sedang digunakan.
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    # Method adalah fungsi yang berada di dalam class.
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari {self.jurusan}.")


# Membuat object dari class Mahasiswa.
mahasiswa_1 = Mahasiswa("Raka", "Teknik Informatika")
mahasiswa_2 = Mahasiswa("Nina", "Sistem Informasi")

mahasiswa_1.perkenalan()
mahasiswa_2.perkenalan()

# Mengakses dan mengubah atribut object.
print("Nama awal:", mahasiswa_1.nama)
mahasiswa_1.nama = "Raka Putra"
print("Nama baru:", mahasiswa_1.nama)

# LATIHAN:
# Buat class Buku dengan atribut judul dan penulis.
# Tambahkan method tampilkan_info() dan buat dua object buku.
