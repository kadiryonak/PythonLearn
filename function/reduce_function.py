# ==========================================
# REDUCE FONKSİYONU
# ==========================================
# reduce(): Bir listeyi tek bir değere indirger.
# Listedeki elemanları soldan sağa iki iki işleyerek
# sonunda tek bir sonuç üretir.
#
# reduce(fonksiyon, iterable, başlangıç_değeri)
#
# functools modülünden import edilir.

from functools import reduce


# ==========================================
# TEMEL ÖRNEKLER
# ==========================================

# ÖRNEK 1: Toplama
print("Toplama")
sayilar = [1, 2, 3, 4, 5]

toplam = reduce(lambda x, y: x + y, sayilar)
print(f"Toplam: {toplam}")  # 15

# Nasıl çalışır:
# 1. adım: 1 + 2 = 3
# 2. adım: 3 + 3 = 6
# 3. adım: 6 + 4 = 10
# 4. adım: 10 + 5 = 15


# ÖRNEK 2: Çarpma (Faktöriyel benzeri)
print("\nÇarpma")
sayilar = [1, 2, 3, 4, 5]

carpim = reduce(lambda x, y: x * y, sayilar)
print(f"Çarpım: {carpim}")  # 120


# ÖRNEK 3: Başlangıç değeri ile
print("\nBaşlangıç Değeri ile")
sayilar = [1, 2, 3, 4, 5]

# 100'den başla ve topla
toplam = reduce(lambda x, y: x + y, sayilar, 100)
print(f"100 + toplam: {toplam}")  # 115


# ==========================================
# KARŞILAŞTIRMA ÖRNEKLERİ
# ==========================================

# ÖRNEK 4: En büyük değer
print("\nEn Büyük Değer")
sayilar = [45, 12, 89, 23, 67, 34]

en_buyuk = reduce(lambda x, y: x if x > y else y, sayilar)
print(f"En büyük: {en_buyuk}")  # 89


# ÖRNEK 5: En küçük değer
print("\nEn Küçük Değer")
sayilar = [45, 12, 89, 23, 67, 34]

en_kucuk = reduce(lambda x, y: x if x < y else y, sayilar)
print(f"En küçük: {en_kucuk}")  # 12


# ==========================================
# STRING İŞLEMLERİ
# ==========================================

# ÖRNEK 6: String birleştirme
print("\nString Birleştirme")
kelimeler = ["Python", " ", "çok", " ", "güzel!"]

birlesik = reduce(lambda x, y: x + y, kelimeler)
print(f"Birleşik: {birlesik}")


# ÖRNEK 7: En uzun kelime
print("\nEn Uzun Kelime")
kelimeler = ["Python", "Java", "JavaScript", "C", "Go"]

en_uzun = reduce(lambda x, y: x if len(x) > len(y) else y, kelimeler)
print(f"En uzun: {en_uzun}")  # JavaScript


# ==========================================
# LİSTE İŞLEMLERİ
# ==========================================

# ÖRNEK 8: İç içe listeyi düzleştirme
print("\nListe Düzleştirme")
ic_ice = [[1, 2], [3, 4], [5, 6]]

duz = reduce(lambda x, y: x + y, ic_ice)
print(f"Düz liste: {duz}")  # [1, 2, 3, 4, 5, 6]


# ÖRNEK 9: Ortak elemanları bulma
print("\nOrtak Elemanlar")
listeler = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]

ortak = reduce(lambda x, y: x & y, listeler)  # & = kesişim
print(f"Ortak elemanlar: {ortak}")  # {3, 4}


# ÖRNEK 10: Birleşim
print("\nBirleşim")
listeler = [{1, 2}, {3, 4}, {5, 6}]

birlesim = reduce(lambda x, y: x | y, listeler)  # | = birleşim
print(f"Birleşim: {birlesim}")  # {1, 2, 3, 4, 5, 6}


# ==========================================
# PRATİK ÖRNEKLER
# ==========================================

# ÖRNEK 11: Faktöriyel hesaplama
print("\nFaktöriyel")

def faktoriyel(n):
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(f"5! = {faktoriyel(5)}")   # 120
print(f"6! = {faktoriyel(6)}")   # 720


# ÖRNEK 12: Sayı basamaklarını birleştirme
print("\nBasamakları Birleştirme")
basamaklar = [1, 2, 3, 4, 5]

sayi = reduce(lambda x, y: x * 10 + y, basamaklar)
print(f"Sayı: {sayi}")  # 12345


# ÖRNEK 13: Sözlükleri birleştirme
print("\nSözlük Birleştirme")
sozlukler = [
    {"a": 1},
    {"b": 2},
    {"c": 3}
]

birlesik = reduce(lambda x, y: {**x, **y}, sozlukler)
print(f"Birleşik sözlük: {birlesik}")  # {'a': 1, 'b': 2, 'c': 3}


# ÖRNEK 14: Pipe (fonksiyon zinciri)
print("\nFonksiyon Zinciri (Pipe)")

def iki_katini_al(x):
    return x * 2

def bir_ekle(x):
    return x + 1

def karesi(x):
    return x ** 2

fonksiyonlar = [iki_katini_al, bir_ekle, karesi]
sayi = 3

# 3 -> 6 -> 7 -> 49
sonuc = reduce(lambda x, f: f(x), fonksiyonlar, sayi)
print(f"Pipe sonuç: {sonuc}")  # 49


# ==========================================
# REDUCE vs DÖNGÜ
# ==========================================
print("\nReduce vs Döngü")
sayilar = [1, 2, 3, 4, 5]

# reduce ile
reduce_sonuc = reduce(lambda x, y: x + y, sayilar)

# for döngüsü ile (aynı sonuç)
toplam = 0
for s in sayilar:
    toplam += s

print(f"reduce: {reduce_sonuc}")
print(f"for: {toplam}")

# sum() ile (en basit)
print(f"sum(): {sum(sayilar)}")
