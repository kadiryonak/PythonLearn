# inheritance

class calisan:
    zam_orani = 1.05
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} Email: {}".format(self.isim, self.soyisim, self.maas, self.email)

calisan1 = calisan("Ahmet", "Yılmaz", 5000)
calisan2 = calisan("Fatma", "Gül", 10000)
print(calisan1.email)
print(calisan2.email)

class yazilimci(calisan):  # inherit calisan class
    zam_orani = 1.1
    def __init__(self, isim, soyisim, maas, yetenekler):
        super().__init__(isim, soyisim, maas)  # Ana class dan gelen bilgileri kullanıyoruz.
        # super class miras aldığımız sınıfın özelliklerini barındırır.
        self.yetenekler = yetenekler

    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} Email: {} Yetenekler: {}".format(self.isim, self.soyisim, self.maas, self.email, ", ".join(self.yetenekler))

yazilimci1 = yazilimci("Ahmet", "Yılmaz", 5000, ["Python", "C++", "Java"])
print(yazilimci1.email)

yazilimci2 = yazilimci("Fatma", "Gül", 10000, ["Python", "C++", "Java"])
print(yazilimci2.email)

print(calisan.zam_orani)
print(yazilimci.zam_orani)


print(yazilimci2.bilgileri_goster())



class yonetici(calisan): # inherit calisan class
    pass

yonetici1 = yonetici("Kadir", "Abc", 5000)
print(yonetici1.email)

yonetici2 = yonetici("Fatma", "Lo", 10000)
print(yonetici2.email)

print(yonetici.zam_orani)