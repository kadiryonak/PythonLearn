



def selamla(isim):
    print("Merhaba " + isim)

def carp(a,b):
    return a*b



selamla("Kadir")

# -------------------------------------------------
# Ek örnek fonksiyonlar (öğrenmek için)
# -------------------------------------------------

def faktoriyel(n):
    """n! (faktöriyel) hesaplar."""
    sonuc = 1
    for i in range(2, n + 1):
        sonuc *= i
    return sonuc

def palindrome(s):
    """Verilen string'in palindrome olup olmadığını döndürür."""
    return s == s[::-1]

def toplam_liste(l):
    """Bir listedeki sayıları toplar."""
    return sum(l)

def ortalama(*args):
    """Değişken sayıda sayının ortalamasını döndürür."""
    if not args:
        return 0
    return sum(args) / len(args)

def bilgi(**kwargs):
    """Anahtar kelime argümanlarını ekrana yazdırır."""
    for k, v in kwargs.items():
        print(f"{k}: {v}")


