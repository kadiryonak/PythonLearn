# ==========================================
# MAP FONKSİYONU
# ==========================================
# map(): Bir listedeki TÜM elemanlara aynı fonksiyonu uygular.
# Sözdizimi: map(fonksiyon, iterable)
# Sonuç: map objesi döner, list() ile listeye çevrilir.


# ÖRNEK 1: Temel Kullanım
def kare_al(x):
    return x ** 2

sayilar = [1, 2, 3, 4, 5]
kareler = list(map(kare_al, sayilar))
print(f"Kareler: {kareler}")  # [1, 4, 9, 16, 25]


# ÖRNEK 2: Lambda ile Kullanım
sayilar = [1, 2, 3, 4, 5]

# Karesi
kareler = list(map(lambda x: x ** 2, sayilar))
print(f"Kareler: {kareler}")

# Küpü
kupler = list(map(lambda x: x ** 3, sayilar))
print(f"Küpler: {kupler}")

# 10 ekle
on_ekle = list(map(lambda x: x + 10, sayilar))
print(f"10 eklenmiş: {on_ekle}")


# ÖRNEK 3: String İşlemleri
print("\nString İşlemleri")
isimler = ["ali", "zeynep", "can", "berna"]

# Büyük harfe çevir
buyuk_harf = list(map(str.upper, isimler))
print(f"Büyük harf: {buyuk_harf}")

# İlk harfi büyük
ilk_buyuk = list(map(str.capitalize, isimler))
print(f"İlk harf büyük: {ilk_buyuk}")

# Uzunlukları
uzunluklar = list(map(len, isimler))
print(f"Uzunluklar: {uzunluklar}")


# ÖRNEK 4: Birden Fazla Liste ile map()
print("\nBirden Fazla Liste")
liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]

# İki listeyi topla
toplam = list(map(lambda x, y: x + y, liste1, liste2))
print(f"Toplam: {toplam}")  # [11, 22, 33, 44]

# İki listeyi çarp
carpim = list(map(lambda x, y: x * y, liste1, liste2))
print(f"Çarpım: {carpim}")  # [10, 40, 90, 160]

# Üç liste ile
liste3 = [100, 200, 300, 400]
uc_liste = list(map(lambda x, y, z: x + y + z, liste1, liste2, liste3))
print(f"Üç liste toplamı: {uc_liste}")  # [111, 222, 333, 444]


# ÖRNEK 5: Tür Dönüşümleri
print("\nTür Dönüşümleri")

# String -> Integer
str_sayilar = ["1", "2", "3", "4", "5"]
int_sayilar = list(map(int, str_sayilar))
print(f"String -> Int: {int_sayilar}")

# Integer -> String
sayilar = [1, 2, 3, 4, 5]
str_liste = list(map(str, sayilar))
print(f"Int -> String: {str_liste}")

# Float'a çevir
float_liste = list(map(float, sayilar))
print(f"Int -> Float: {float_liste}")


# ÖRNEK 6: Sözlük ile map()
print("\nSözlük ile Kullanım")
ogrenciler = [
    {"isim": "Ali", "not": 85},
    {"isim": "Zeynep", "not": 92},
    {"isim": "Can", "not": 78}
]

# Sadece isimleri al
isimler = list(map(lambda x: x["isim"], ogrenciler))
print(f"İsimler: {isimler}")

# Sadece notları al
notlar = list(map(lambda x: x["not"], ogrenciler))
print(f"Notlar: {notlar}")

# Notlara 5 puan ekle
yeni_notlar = list(map(lambda x: {**x, "not": x["not"] + 5}, ogrenciler))
print("5 puan eklenmiş:")
for o in yeni_notlar:
    print(f"  {o}")


# ÖRNEK 7: map vs list comprehension
print("\nmap vs List Comprehension")
sayilar = [1, 2, 3, 4, 5]

# map ile
map_sonuc = list(map(lambda x: x ** 2, sayilar))

# list comprehension ile (aynı sonuç)
comp_sonuc = [x ** 2 for x in sayilar]

print(f"map: {map_sonuc}")
print(f"comprehension: {comp_sonuc}")
# İkisi de aynı sonucu verir: [1, 4, 9, 16, 25]


# ÖRNEK 8: Pratik Kullanım - Celsius -> Fahrenheit
print("\nCelsius -> Fahrenheit Dönüşümü")
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
