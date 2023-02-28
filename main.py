class Mahasiswa:
    """ kelas yang digunakan untuk mendefinisikan atribut
    dan method pada mahasiswa
    definisi atribut:
    kuis : atribut untuk menyimpan nilai kuis (integer)
    uts : atribut untuk menyimpan nilai uts (integer)
    uas : atribut untuk menyimpan nilai uas (integer) """
    # Definisi method:
    ## Method tampilkan
    def tampilkan(self):
        print("Kuis : ",self.kuis,"UTS : ", self.uts, "UAS : ", self.uas)
        return
    ## Method Hitung Nilai Akhir
    def hitungNilaiAkhir(self):
        return (self.kuis*3+self.uts*3+self.uas*4)/10
    ## menampilkan nilai Index Prestasti
    def tampilkanIP(self):
        nilaiAkhir = self.hitungNilaiAkhir()
        if (nilaiAkhir>=80):
            print("IP Anda : A")
        elif (nilaiAkhir>=70):
            print("IP Anda : B")
        elif (nilaiAkhir>=60):
            print("IP Anda : C")
        elif (nilaiAkhir>=50):
            print("IP Anda : D")
        else:
            print("IP Anda : E")
        return


def main():
    b = Mahasiswa ()
    b.kuis = int(input("masukan nilai kuis :"))
    b.uts = int(input("masukan nilai uts :"))
    b.uas = int(input("masukan nilai uas :"))
    b.tampilkan()
    print("nilai si b = ", b.hitungNilaiAkhir())
    b.tampilkanIP()
    return
if __name__=='__main__':
    main()
