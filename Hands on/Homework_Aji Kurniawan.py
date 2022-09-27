class hewan:
    #class attribute
    nama_latin = "Cygnini"
    
    #instance attribute
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    #method bangun
    def bangun(self):
        return "{} berumur {} tahun bangun ".format(self.nama,self.umur)
    
    #class method change_nama_latin
    @classmethod
    def change_nama_latin(self, nama_latin):
        return nama_latin

#child class hewan
class kucing(hewan):
    
    # class method change nama latin dengan value berbeda dari parent class
    def change_nama_latin(self):
        return ("Felis catus")
     
    #ovveride method bangun 
    def bangun(self):
        return "{} berumur {} tahun bangun ".format(self.nama,self.umur)
    
    #method lari
    def lari(kecepatan):
        if kecepatan>10:
            print("Cepat Sekali")
        else:
            print("Lambat")
        
#memanggil kelas hewan dan method bangun   
kelas_hewan=hewan('angsa',1)
print(kelas_hewan.bangun())
print("hewan ini bernama latin {}".format(kelas_hewan.__class__.nama_latin))

#memanggil child class kucing
kelas_kucing=kucing('kucing',10)
print(kelas_kucing.bangun())
print("hewan ini bernama latin {}".format(kelas_kucing.change_nama_latin()))

#memanggil method lari dari child class 
kucing.lari(11)
kucing.lari(9)