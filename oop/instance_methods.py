# instance variables

from datetime import date

class kisi:
    zam_orani = 1.1
    kisi_sayisi = 0
    
    def __init__(self, name, yas, dogumyili ):
        self.name = name
        self.yas = yas
        kisi.kisi_sayisi += 1
        self.dogumyili = dogumyili


    def show_info(self):
        print(self.name, self.yas)

    def bilgilerini_söyle(self): # Instance Method
        print(self.name, self.yas)

    @classmethod
    def kisi_sayisini_goster(cls):# bunu class üzerinden kullanacağız 
        print(cls.kisi_sayisi)

    @classmethod # class method class ı otomatik üzerine alır statik methodda böyle bir şey yok
    def dogum_yili_olustur(cls, isim, dogumyili):
        return cls(isim, date.today().year - dogumyili, dogumyili)
    
    @staticmethod    
    def dogum_yili():
        return date.today().year

kisi1 = kisi("Ahmet", 25)
kisi2 = kisi("Ayşe", 22)

print(kisi.bilgilerini_söyle(kisi1))
print(kisi1.bilgilerini_söyle())
print(kisi.kisi_sayisini_goster()) # gösterir çünkü direkt class üzerinden çalışıyor
# nesne üretmesem dahi bu fonksiyonu çalıştırabilirim. Contructor olarak kullanılabilir.

#kisi1.show_info()
#kisi2.show_info()
# Output:

# Hata verecek çünkü name instance variable
# print(kisi.name)

#   File "c:\Users\w\Desktop\Kodlama\VsCode\HelloWorld\python\oop\instance_methods.py", line 18, in <module>    
#     print(kisi.name)
#           ^^^^^^^^^
# AttributeError: type object 'kisi' has no attribute 'name'
# zam oranı class veriable
print(kisi.zam_orani)
print(kisi1.zam_orani)


# Eğer class üzerinden ulaşıp değiştirirsem bütün her yerde değişir zam orani
# ama nesne üzerinden erişip değiştirirsem sadece o nesnede değişir

kisi.zam_orani = 1.2
print(kisi.zam_orani)
print(kisi1.zam_orani)

kisi2.zam_orani = 1.3
print(kisi2.zam_orani)
print(kisi1.zam_orani)

# Output:

# 1.2
# 1.2
# 1.3
# 1.2