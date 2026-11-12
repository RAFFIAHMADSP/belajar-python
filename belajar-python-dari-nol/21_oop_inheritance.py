# ============================================================
# 21 - OOP: INHERITANCE (PEWARISAN)
# ============================================================
# Inheritance memungkinkan class anak mewarisi atribut dan method
# dari class induk.

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan mengeluarkan suara.")


class Kucing(Hewan):
    # Class Kucing mewarisi __init__ dari Hewan.
    # Method suara() di bawah melakukan overriding (mengganti perilaku).
    def suara(self):
        print(f"{self.nama} berkata: Meong!")


class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} berkata: Guk guk!")


kucing = Kucing("Milo")
anjing = Anjing("Bruno")
kucing.suara()
anjing.suara()

# super() dapat dipakai untuk memanggil method milik class induk.
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama


class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, semester):
        super().__init__(nama)
        self.semester = semester

    def tampilkan(self):
        print(f"{self.nama} adalah mahasiswa semester {self.semester}.")


orang = MahasiswaAktif("Dina", 1)
orang.tampilkan()

# LATIHAN:
# Buat class Kendaraan dengan method bergerak().
# Buat class Mobil yang mewarisi Kendaraan dan memiliki atribut merek.
