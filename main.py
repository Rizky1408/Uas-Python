import os

os.system("clear")


class Volume:

    def __init__(self, alas, tinggi, T) -> None:
        self.alas = alas
        self.tinggi = tinggi
        self.T = T

    def get_volume(self):
        return 0.5 * self.alas * self.tinggi * self.T


class luas(Volume):

    def __init__(self, alas, tinggi, T, a1, a2, a3) -> None:
        super(luas, self).__init__(alas, tinggi, T)
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def get_luasPermukaan(self):
        return (self.a1 + self.a2 + self.a3) * self.T + self.alas * self.tinggi

    def get_luasSisi(self, sisi1, sisi2, sisi3, tinggi):
        # Overloading Konstruktor
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3
        self.tinggi = tinggi

        return (self.sisi1 + self.sisi2 + self.sisi3) * self.tinggi


class main:

    print("1. Hitung Volume ")
    print("2. Hitung Luas Permukaan")
    print("3. Hitung Luas Sisi")

    pilih = int(input("Masukan Pilihan :"))

    if pilih == 1:
        alas = float(input("Masukan alas dari bangun ruang :"))
        tinggi = float(input("Masukan Tinggi dari bangun ruang :"))
        T = float(input("Masukan Tinggi Limas :"))
        Volume1 = Volume(alas, tinggi, T)
        hasil = Volume1.get_volume()
        print("Luas Volume adalah ", hasil)
    elif pilih == 2:
        sisi1 = float(input("masukan  sisi pertama :"))
        sisi2 = float(input("masukan sisi kedua :"))
        sisi3 = float(input("masukan sisi ketiga :"))
        alas = float(input("Masukan alas dari bangun ruang :"))
        tinggi = float(input("Masukan Tinggi dari bangun ruang :"))
        T = float(input("Masukan Tinggi Limas :"))
        luas1 = luas(alas, tinggi, T, sisi1, sisi2, sisi3)
        hasil = luas1.get_luasPermukaan()
        print("Luas permukaan adalah :", hasil)

    elif pilih == 3:
        sisi1 = float(input("masukan  sisi pertama  :"))
        sisi2 = float(input("masukan sisi kedua :"))
        sisi3 = float(input("masukan sisi ketiga :"))
        tinggi = float(input("Masukan Tinggi dari bangun ruang :"))
        luasSisi = luas.get_luasSisi(sisi1, sisi2, sisi3, tinggi)

        print("Luas sisi dari bangung ruang adalah ", luasSisi)
