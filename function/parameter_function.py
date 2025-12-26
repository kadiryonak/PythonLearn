# ==========================================
# PARAMETRE OLARAK FONKSİYON VERME
# ==========================================
# Fonksiyonlar parametre olarak diğer fonksiyonlara verilebilir.
# Bu "Higher-Order Function" (Yüksek Seviye Fonksiyon) olarak adlandırılır.


# ÖRNEK 1: Basit Kullanım
def selamla():
    return "Merhaba!"

def mesaj_yazdir(fonksiyon):
    print(fonksiyon())

mesaj_yazdir(selamla)  # "Merhaba!"




# ÖRNEK 2: İşlem Uygulayıcı
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def hesapla(islem_fonksiyonu, x, y):
    return islem_fonksiyonu(x, y)

print(hesapla(topla, 10, 5))  # 15
print(hesapla(cikar, 10, 5))  # 5
print(hesapla(carp, 10, 5))   # 50




# ÖRNEK 3: Listeye Fonksiyon Uygulama
def kare_al(x):
    return x ** 2

def kup_al(x):
    return x ** 3

def listeye_uygula(liste, fonksiyon):
    return [fonksiyon(eleman) for eleman in liste]

sayilar = [1, 2, 3, 4, 5]
print(listeye_uygula(sayilar, kare_al))  # [1, 4, 9, 16, 25]
print(listeye_uygula(sayilar, kup_al))   # [1, 8, 27, 64, 125]




# ÖRNEK 4: Built-in Örnekler (map, filter, sorted)
sayilar = [1, 2, 3, 4, 5]

# map: Her elemana fonksiyon uygular
kareler = list(map(lambda x: x**2, sayilar))
print(f"Kareler: {kareler}")  # [1, 4, 9, 16, 25]

# filter: Koşula uyanları filtreler  
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(f"Çiftler: {ciftler}")  # [2, 4]

# sorted: Özel sıralama kriteri
isimler = ["Ali", "Zeynep", "Can", "Berna"]
uzunluga_gore = sorted(isimler, key=lambda x: len(x))
print(f"Uzunluğa göre: {uzunluga_gore}")  # ['Ali', 'Can', 'Berna', 'Zeynep']

print("-" * 40)


# ÖRNEK 5: Callback Fonksiyonu
def islem_yap(veri, basari_callback, hata_callback):
    try:
        sonuc = int(veri) * 2
        basari_callback(sonuc)
    except:
        hata_callback("Geçersiz veri!")

def basari(sonuc):
    print(f"Başarılı Sonuç: {sonuc}")

def hata(mesaj):
    print(f" Hata: {mesaj}")

islem_yap("5", basari, hata)   # ✓ Başarılı! Sonuç: 10
islem_yap("abc", basari, hata) # ✗ Hata: Geçersiz veri!
