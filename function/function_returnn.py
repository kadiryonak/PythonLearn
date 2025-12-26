# ==========================================
# FONKSİYON DÖNDÜRME (Return Function)
# ==========================================
# Python'da fonksiyonlar birinci sınıf vatandaştır (first-class citizen)
# Yani fonksiyonlar değişkenlere atanabilir ve döndürülebilir.


# ÖRNEK 1: Basit Fonksiyon Döndürme
def dis_fonksiyon():
    def ic_fonksiyon():
        return "Ben iç fonksiyonum!"
    return ic_fonksiyon  # Parantez YOK - fonksiyonun kendisini döndür

sonuc = dis_fonksiyon()  # sonuc artık ic_fonksiyon'a referans
print(sonuc())  # "Ben iç fonksiyonum!"




# ÖRNEK 2: Parametre ile Fonksiyon Fabrikası
def carpan_olustur(carpim):
    def carp(sayi):
        return sayi * carpim
    return carp

ikiyle_carp = carpan_olustur(2)
ucle_carp = carpan_olustur(3)

print(ikiyle_carp(5))   # 10
print(ucle_carp(5))     # 15




# ÖRNEK 3: Koşula Göre Farklı Fonksiyon Döndürme
def islem_sec(islem):
    def topla(a, b):
        return a + b
    def cikar(a, b):
        return a - b
    def carp(a, b):
        return a * b
    
    if islem == "topla":
        return topla
    elif islem == "cikar":
        return cikar
    elif islem == "carp":
        return carp

hesapla = islem_sec("carp")
print(hesapla(4, 5))  # 20



# ÖRNEK 4: Closure (Kapalı Değişken)
def sayac_olustur():
    sayac = 0
    def artir():
        nonlocal sayac  # Dış değişkeni değiştirmek için
        sayac += 1
        return sayac
    return artir

sayac1 = sayac_olustur()
print(sayac1())  # 1
print(sayac1())  # 2
print(sayac1())  # 3

sayac2 = sayac_olustur()  # Yeni bağımsız sayaç
print(sayac2())  # 1
