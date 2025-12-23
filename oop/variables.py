class calisan:
    zam = 1.1
    def __init__(self, name, surname, maas):
        self.name = name
        self.surname = surname
        self.maas = maas
    

calisan1 = calisan("Ahmet", "Yılmaz", 250000)

# instance variable yani nesnelerin değişkenleri
calisan2 = calisan("Ayşe", "Yılmaz", 220000)

print(calisan1.__dict__)
print(calisan2.__dict__) # self.name deki name yazdırılır


# print(calisan.__dict__)

# ortak değişken, ister nesne ister sınıf üzerinden erişilebilir

print(calisan.zam)

print(calisan1.zam)
print(calisan2.zam)

# calisan a zam direkt gözüküyor
print(calisan.__dict__)
print(calisan1.__dict__)


# ilk önce nesneye bakar bulamaz ise sınıfı kontrol eder

calisan1.zam = 1.2
print(calisan1.zam)
print(calisan2.zam)
print(calisan.zam)


print(calisan1.__dict__)

# Output:
# {'name': 'Ahmet', 'surname': 'Yılmaz', 'maas': 250000}
# {'name': 'Ayşe', 'surname': 'Yılmaz', 'maas': 220000}
# 1.1
# 1.1
# 1.1
# {'__module__': '__main__', '__firstlineno__': 1, 'zam': 1.1, '__init__': <function calisan.__init__ at 0x0000018E925E3F60>, '__static_attributes__': ('maas', 'name', 'surname'), '__dict__': <attribute '__dict__' of 'calisan' objects>, '__weakref__': <attribute '__weakref__' of 'calisan' objects>, '__doc__': None}
# {'name': 'Ahmet', 'surname': 'Yılmaz', 'maas': 250000}
# 1.2
# 1.1
# 1.1
# {'name': 'Ahmet', 'surname': 'Yılmaz', 'maas': 250000, 'zam': 1.2} # zam artık nesneye eklenmiş gibi oldu


