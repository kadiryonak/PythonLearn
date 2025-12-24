# ==========================================
# ZIP FONKSİYONU
# ==========================================
# zip(): Birden fazla iterable'ı birleştirerek tuple'lar oluşturur.
# Her iterable'dan sırayla eleman alır ve eşleştirir.
# En kısa iterable bitince durur.


# ==========================================
# LİSTE İLE KULLANIM
# ==========================================
print("Liste ile zip()")

isimler = ["Ali", "Zeynep", "Can", "Berna"]
yaslar = [25, 30, 22, 28]

# İki listeyi birleştir
birlesik = list(zip(isimler, yaslar))
print(f"Birleşik: {birlesik}")
# [('Ali', 25), ('Zeynep', 30), ('Can', 22), ('Berna', 28)]

# for döngüsü ile kullanım
print("\nfor ile gezinme:")
for isim, yas in zip(isimler, yaslar):
    print(f"{isim}: {yas} yaşında")


# Üç liste birleştirme
print("\nÜç liste birleştirme:")
isimler = ["Ali", "Zeynep", "Can"]
yaslar = [25, 30, 22]
sehirler = ["İstanbul", "Ankara", "İzmir"]

for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"{isim}, {yas} yaşında, {sehir}'da yaşıyor")


# Farklı uzunluktaki listeler
print("\nFarklı uzunlukta listeler:")
liste1 = [1, 2, 3, 4, 5]
liste2 = ["a", "b", "c"]

sonuc = list(zip(liste1, liste2))
print(f"Sonuç: {sonuc}")  # En kısa olanda durur: [(1, 'a'), (2, 'b'), (3, 'c')]


# ==========================================
# TUPLE İLE KULLANIM
# ==========================================
print("\n Tuple ile zip()")

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = (True, False, True)

# Tuple'ları birleştir
birlesik = list(zip(tuple1, tuple2, tuple3))
print(f"Birleşik tuple'lar: {birlesik}")

# Tuple olarak döndür
tuple_sonuc = tuple(zip(tuple1, tuple2))
print(f"Tuple sonuç: {tuple_sonuc}")


# ==========================================
# SET İLE KULLANIM
# ==========================================
print("\n Set ile zip()")

set1 = {1, 2, 3}
set2 = {"a", "b", "c"}

# Set'leri birleştir (sıra garantisi yok!)
birlesik = list(zip(set1, set2))
print(f"Set birleştirme: {birlesik}")
# Dikkat: Set'ler sırasızdır, eşleşme değişebilir!

# zip sonucunu set'e çevir
set_sonuc = set(zip([1, 2, 3], ["a", "b", "c"]))
print(f"Set sonuç: {set_sonuc}")


# ==========================================
# PRATİK ÖRNEKLER
# ==========================================

# ÖRNEK 1: Sözlük oluşturma
print("\n Sözlük Oluşturma")
anahtarlar = ["isim", "yas", "sehir"]
degerler = ["Ali", 25, "İstanbul"]

sozluk = dict(zip(anahtarlar, degerler))
print(f"Sözlük: {sozluk}")


# ÖRNEK 2: İki listeyi toplama
print("\n İki Listeyi Toplama")
liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]

toplam = [a + b for a, b in zip(liste1, liste2)]
print(f"Toplam: {toplam}")  # [11, 22, 33, 44]


# ÖRNEK 3: Paralel döngü
print("\n Paralel Döngü")
urunler = ["Laptop", "Telefon", "Tablet"]
fiyatlar = [15000, 8000, 5000]
stoklar = [10, 25, 15]

for urun, fiyat, stok in zip(urunler, fiyatlar, stoklar):
    print(f"{urun}: {fiyat} TL, Stok: {stok}")


# ÖRNEK 4: enumerate + zip
print("\n enumerate + zip")
isimler = ["Ali", "Zeynep", "Can"]
puanlar = [85, 92, 78]

for i, (isim, puan) in enumerate(zip(isimler, puanlar), 1):
    print(f"{i}. {isim}: {puan} puan")


# ÖRNEK 5: unzip (zip'i geri alma)
print("\n Unzip (Geri Alma)")
birlesik = [("Ali", 25), ("Zeynep", 30), ("Can", 22)]

# * operatörü ile unzip
isimler, yaslar = zip(*birlesik)
print(f"İsimler: {isimler}")  # ('Ali', 'Zeynep', 'Can')
print(f"Yaşlar: {yaslar}")    # (25, 30, 22)


# ÖRNEK 6: Matris transpozu
print("\n Matris Transpozu")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpoz = list(zip(*matris))
print("Orijinal:")
for satir in matris:
    print(f"  {satir}")

print("Transpoz:")
for satir in transpoz:
    print(f"  {list(satir)}")


# ÖRNEK 7: zip_longest (itertools)
print("\n zip_longest (eksikleri doldur)")
from itertools import zip_longest

liste1 = [1, 2, 3, 4, 5]
liste2 = ["a", "b", "c"]

# Normal zip - kısa olanda durur
normal = list(zip(liste1, liste2))
print(f"Normal zip: {normal}")

# zip_longest - eksikleri None ile doldurur
uzun = list(zip_longest(liste1, liste2, fillvalue="-"))
print(f"zip_longest: {uzun}")
