# ==========================================
# FILTER FONKSİYONU
# ==========================================
# filter(): Bir listedeki elemanları koşula göre süzer.
# Koşulu sağlayan (True dönen) elemanları tutar.
#
# filter(fonksiyon, iterable)
#
# Sonuç: filter objesi döner, list() ile listeye çevrilir.


# ==========================================
# TEMEL ÖRNEKLER
# ==========================================

# ÖRNEK 1: Çift sayıları filtrele
print("Çift Sayılar")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cift_mi(x):
    return x % 2 == 0

ciftler = list(filter(cift_mi, sayilar))
print(f"Çiftler: {ciftler}")  # [2, 4, 6, 8, 10]


# ÖRNEK 2: Lambda ile kullanım
print("\nLambda ile")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tek sayılar
tekler = list(filter(lambda x: x % 2 != 0, sayilar))
print(f"Tekler: {tekler}")  # [1, 3, 5, 7, 9]

# 5'ten büyükler
buyukler = list(filter(lambda x: x > 5, sayilar))
print(f"5'ten büyükler: {buyukler}")  # [6, 7, 8, 9, 10]


# ÖRNEK 3: Negatif sayıları filtrele
print("\nNegatif Sayılar")
sayilar = [-5, -2, 0, 3, 7, -1, 8]

negatifler = list(filter(lambda x: x < 0, sayilar))
pozitifler = list(filter(lambda x: x > 0, sayilar))

print(f"Negatifler: {negatifler}")  # [-5, -2, -1]
print(f"Pozitifler: {pozitifler}")  # [3, 7, 8]


# ==========================================
# STRING İŞLEMLERİ
# ==========================================

# ÖRNEK 4: Boş stringleri filtrele
print("\nBoş Stringleri Filtrele")
kelimeler = ["Python", "", "Java", "", "C++", ""]

dolu = list(filter(None, kelimeler))  # None = boş olmayanlar
print(f"Dolu olanlar: {dolu}")  # ['Python', 'Java', 'C++']


# ÖRNEK 5: Uzun kelimeleri filtrele
print("\nUzun Kelimeler")
kelimeler = ["ali", "zeynep", "can", "mert", "elif", "berna"]

uzunlar = list(filter(lambda x: len(x) > 4, kelimeler))
print(f"4 harften uzun: {uzunlar}")  # ['zeynep', 'berna']


# ÖRNEK 6: Belirli harfle başlayanlar
print("\nHarfle Başlayanlar")
isimler = ["Ali", "Ayşe", "Berk", "Canan", "Ahmet", "Deniz"]

a_ile = list(filter(lambda x: x.startswith("A"), isimler))
print(f"A ile başlayanlar: {a_ile}")  # ['Ali', 'Ayşe', 'Ahmet']


# ==========================================
# LİSTE VE SÖZLÜK İŞLEMLERİ
# ==========================================

# ÖRNEK 7: Sözlük listesi filtreleme
print("\nSözlük Filtreleme")
ogrenciler = [
    {"isim": "Ali", "not": 85},
    {"isim": "Zeynep", "not": 92},
    {"isim": "Can", "not": 45},
    {"isim": "Berna", "not": 78},
    {"isim": "Mert", "not": 55}
]

# Geçenler (50 ve üzeri)
gecenler = list(filter(lambda x: x["not"] >= 50, ogrenciler))
print("Geçenler:")
for o in gecenler:
    print(f"  {o['isim']}: {o['not']}")

# Kalanlar
kalanlar = list(filter(lambda x: x["not"] < 50, ogrenciler))
print(f"Kalanlar: {[o['isim'] for o in kalanlar]}")


# ÖRNEK 8: None değerleri filtrele
print("\nNone Filtreleme")
veriler = [1, None, 2, None, 3, None, 4]

temiz = list(filter(lambda x: x is not None, veriler))
print(f"None'sız: {temiz}")  # [1, 2, 3, 4]




# ÖRNEK 9: Asal sayıları bul
print("\nAsal Sayılar")

def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sayilar = range(1, 30)
asallar = list(filter(asal_mi, sayilar))
print(f"Asal sayılar: {asallar}")


# ÖRNEK 10: Email doğrulama
print("\nEmail Doğrulama")
emails = [
    "ali@gmail.com",
    "zeynephotmail.com",  # @ yok
    "can@yahoo.com",
    "bernaoutlook",       # @ ve . yok
    "mert@test.org"
]

def gecerli_email(email):
    return "@" in email and "." in email

gecerli = list(filter(gecerli_email, emails))
print(f"Geçerli emailler: {gecerli}")


# ÖRNEK 11: Yaş kontrolü
print("\nYaş Kontrolü")
kisiler = [
    {"isim": "Ali", "yas": 17},
    {"isim": "Zeynep", "yas": 25},
    {"isim": "Can", "yas": 15},
    {"isim": "Berna", "yas": 30}
]

yetiskinler = list(filter(lambda x: x["yas"] >= 18, kisiler))
print(f"Yetişkinler: {[k['isim'] for k in yetiskinler]}")


# ==========================================
# FILTER vs LIST COMPREHENSION
# ==========================================
print("\nFilter vs List Comprehension")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter ile
filter_sonuc = list(filter(lambda x: x % 2 == 0, sayilar))

# list comprehension ile (aynı sonuç)
comp_sonuc = [x for x in sayilar if x % 2 == 0]

print(f"filter: {filter_sonuc}")
print(f"comprehension: {comp_sonuc}")


# ==========================================
# MAP + FILTER BİRLİKTE
# ==========================================
print("\nMap + Filter Birlikte")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Çift sayıların karesini al
sonuc = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, sayilar)))
print(f"Çift sayıların karesi: {sonuc}")  # [4, 16, 36, 64, 100]
