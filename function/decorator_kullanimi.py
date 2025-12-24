# ==========================================
# DECORATOR KULLANIMI
# ==========================================
# Decorator: Bir fonksiyonu sarmalayarak (wrap) 
# ek özellikler ekleyen fonksiyondur.
# @ işareti ile kullanılır.


# ÖRNEK 1: Basit Decorator
def selamla(fonksiyon):
    def wrapper():
        print("Merhaba!")
        fonksiyon()
        print("Hoşça kal!")
    return wrapper

@selamla  # mesaj_yaz = selamla(mesaj_yaz) ile aynı
def mesaj_yaz():
    print("Ben bir mesajım.")

mesaj_yaz()
# Çıktı:
# Merhaba!
# Ben bir mesajım.
# Hoşça kal!

print("-" * 40)


# ÖRNEK 2: Parametreli Fonksiyona Decorator
def log_decorator(fonksiyon):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {fonksiyon.__name__} çağrıldı")
        print(f"[LOG] Parametreler: {args}, {kwargs}")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"[LOG] Sonuç: {sonuc}")
        return sonuc
    return wrapper

@log_decorator
def topla(a, b):
    return a + b

topla(5, 3)

print("-" * 40)


# ÖRNEK 3: Zaman Ölçen Decorator
import time

def zaman_olc(fonksiyon):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.4f} saniye sürdü")
        return sonuc
    return wrapper

@zaman_olc
def uzun_islem():
    toplam = 0
    for i in range(1000000):
        toplam += i
    return toplam

uzun_islem()

print("-" * 40)


# ÖRNEK 4: Birden Fazla Decorator
def bold(fonksiyon):
    def wrapper():
        return f"<b>{fonksiyon()}</b>"
    return wrapper

def italic(fonksiyon):
    def wrapper():
        return f"<i>{fonksiyon()}</i>"
    return wrapper

@bold
@italic  # Önce italic, sonra bold uygulanır
def metin():
    return "Python"

print(metin())  # <b><i>Python</i></b>
