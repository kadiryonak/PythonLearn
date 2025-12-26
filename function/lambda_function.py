kare_al = lambda x: x ** 2

toplam = lambda x, y: x + y


genel_toplama = lambda *args: sum(args)

print(genel_toplama(1, 2, 3, 4, 5))

print(kare_al(5))
print(toplam(3, 4))

print("İsim vermeden kullanım")
print((lambda x , y, z: x * y + z)(5, 6, 7))
print("Ortalama: ", (lambda *args: sum(args)/len(args))(5, 6, 7, 8, 9))

# lamda ifadeleri genellikle map, filter, sorted gibi fonksiyonlarla birlikte kullanılır

# ÖRNEK 1: Map ile Kullanım
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # [1, 4, 9, 16, 25]

# ÖRNEK 2: Filter ile Kullanım
def cift_mi(x):
    return x % 2 == 0

sayilar = [1, 2, 3, 4, 5, 6]
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(ciftler)  # [2, 4, 6]

# ÖRNEK 3: Sorted ile Kullanım
isimler = ["Ali", "Zeynep", "Can", "Berna"]
isimler.sort(key=lambda x: len(x))
print(isimler)  # ['Can', 'Ali', 'Berna', 'Zeynep']



# LİSTE İLE LAMBDA ÖRNEKLERİ



print("\n Sayı Sıralamaları")
sayilar = [5, 2, 8, 1, 9, 3]


kucukten_buyuge = sorted(sayilar)
print(f"Küçükten büyüğe: {kucukten_buyuge}")

buyukten_kucuge = sorted(sayilar, key=lambda x: -x)
print(f"Büyükten küçüğe: {buyukten_kucuge}")


karisik = [-5, 2, -8, 1, -9, 3]
mutlak_sirali = sorted(karisik, key=lambda x: abs(x))
print(f"Mutlak değere göre: {mutlak_sirali}")



print("\n String Sıralamaları")
kelimeler = ["Python", "java", "C++", "javascript", "Go"]


alfabetik = sorted(kelimeler, key=lambda x: x.lower())
print(f"Alfabetik: {alfabetik}")


uzunluk_sirali = sorted(kelimeler, key=lambda x: len(x))
print(f"Uzunluğa göre: {uzunluk_sirali}")


son_harf = sorted(kelimeler, key=lambda x: x[-1].lower())
print(f"Son harfe göre: {son_harf}")



print("\n Sözlük Listesi Sıralamaları")
ogrenciler = [
    {"isim": "Ali", "not": 85, "yas": 22},
    {"isim": "Zeynep", "not": 92, "yas": 20},
    {"isim": "Can", "not": 78, "yas": 23},
    {"isim": "Berna", "not": 88, "yas": 21}
]


nota_gore = sorted(ogrenciler, key=lambda x: x["not"], reverse=True)
print("Nota göre:")
for o in nota_gore:
    print(f"  {o['isim']}: {o['not']}")


yasa_gore = sorted(ogrenciler, key=lambda x: x["yas"])
print("Yaşa göre:", [o["isim"] for o in yasa_gore])

isme_gore = sorted(ogrenciler, key=lambda x: x["isim"])
print("İsme göre:", [o["isim"] for o in isme_gore])


print("\n İç İçe Liste Sıralamaları")
koordinatlar = [[3, 5], [1, 8], [4, 2], [2, 6]]


ilk_eleman = sorted(koordinatlar, key=lambda x: x[0])
print(f"İlk elemana göre: {ilk_eleman}")

# İkinci elemana göre
ikinci_eleman = sorted(koordinatlar, key=lambda x: x[1])
print(f"İkinci elemana göre: {ikinci_eleman}")

# Toplama göre
toplam_gore = sorted(koordinatlar, key=lambda x: x[0] + x[1])
print(f"Toplama göre: {toplam_gore}")

print("\n Çoklu Kriter Sıralama")
urunler = [
    ("Laptop", 15000, 4.5),
    ("Telefon", 8000, 4.8),
    ("Tablet", 8000, 4.2),
    ("Monitor", 5000, 4.5)
]

coklu_siralama = sorted(urunler, key=lambda x: (x[1], -x[2]))
print("Fiyat ve puana göre:")
for urun in coklu_siralama:
    print(f"  {urun[0]}: {urun[1]} TL, {urun[2]} puan")


print("\n Reduce Kullanımı")
from functools import reduce

sayilar = [1, 2, 3, 4, 5]


carpim = reduce(lambda x, y: x * y, sayilar)
print(f"Çarpım: {carpim}")  # 120


en_buyuk = reduce(lambda x, y: x if x > y else y, sayilar)
print(f"En büyük: {en_buyuk}")  # 5

kelimeler = ["Merhaba", " ", "Dünya", "!"]
birlesik = reduce(lambda x, y: x + y, kelimeler)
print(f"Birleşik: {birlesik}")