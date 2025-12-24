"""
DECORATOR PATTERN

NE İÇİN KULLANILIR?

Decorator pattern, mevcut bir nesneye dinamik olarak yeni özellikler veya 
davranışlar eklemek için kullanılır. Orijinal sınıfı değiştirmeden, 
nesneleri "sarmalayarak" (wrap) işlevsellik ekler.

KULLANIM ALANLARI:
- Logging (loglama) ekleme
- Yetkilendirme kontrolü
- Önbellekleme (caching)
- Performans ölçümü
- Input/Output validasyonu

AVANTAJLARI:
- Open/Closed prensibine uyar (genişlemeye açık, değişikliğe kapalı)
- Çalışma zamanında davranış eklenebilir
- Alt sınıf patlamasını önler
"""


# ÖRNEK 1: Python'un @decorator syntax'ı


import time
from functools import wraps

def zamanlayici(func):
    """Fonksiyonun çalışma süresini ölçen decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = func(*args, **kwargs)
        bitis = time.time()
        print(f"'{func.__name__}' fonksiyonu {bitis - baslangic:.4f} saniyede çalıştı")
        return sonuc
    return wrapper

def loglayici(func):
    """Fonksiyon çağrılarını loglayan decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} çağrıldı - Args: {args}, Kwargs: {kwargs}")
        sonuc = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} tamamlandı - Sonuç: {sonuc}")
        return sonuc
    return wrapper


@zamanlayici
@loglayici
def toplama(a, b):
    """İki sayıyı toplar"""
    time.sleep(0.1)  # Simülasyon için bekleme
    return a + b



# ÖRNEK 2: Sınıf Tabanlı Decorator Pattern

class Kahve:
    """Temel kahve sınıfı"""
    def maliyet(self):
        return 10
    
    def aciklama(self):
        return "Sade Kahve"


class KahveDekorator(Kahve):
    """Decorator temel sınıfı"""
    def __init__(self, kahve: Kahve):
        self._kahve = kahve
    
    def maliyet(self):
        return self._kahve.maliyet()
    
    def aciklama(self):
        return self._kahve.aciklama()


class SutEkle(KahveDekorator):
    """Süt ekleyen decorator"""
    def maliyet(self):
        return self._kahve.maliyet() + 3
    
    def aciklama(self):
        return self._kahve.aciklama() + " + Süt"


class SekerEkle(KahveDekorator):
    """Şeker ekleyen decorator"""
    def maliyet(self):
        return self._kahve.maliyet() + 1
    
    def aciklama(self):
        return self._kahve.aciklama() + " + Şeker"


class KremEkle(KahveDekorator):
    """Krem ekleyen decorator"""
    def maliyet(self):
        return self._kahve.maliyet() + 5
    
    def aciklama(self):
        return self._kahve.aciklama() + " + Krem"



# KULLANIM ÖRNEKLERİ


if __name__ == "__main__":

    print("DECORATOR PATTERN ÖRNEKLERİ")

    
    # Örnek 1: Fonksiyon decorator'ları
    print("\n1. Fonksiyon Decorator'ları:")

    sonuc = toplama(5, 3)
    print(f"Sonuç: {sonuc}")
    
    # Örnek 2: Sınıf tabanlı decorator
    print("\n2. Sınıf Tabanlı Decorator :")

    
    # Sade kahve
    kahve = Kahve()
    print(f"  {kahve.aciklama()}: {kahve.maliyet()} TL")
    
    # Sütlü kahve
    sutlu_kahve = SutEkle(Kahve())
    print(f"  {sutlu_kahve.aciklama()}: {sutlu_kahve.maliyet()} TL")
    
    # Sütlü ve şekerli kahve (decorator'ları zincirleme)
    ozel_kahve = SekerEkle(SutEkle(Kahve()))
    print(f"  {ozel_kahve.aciklama()}: {ozel_kahve.maliyet()} TL")
    
    # Tüm eklemelerle kahve
    super_kahve = KremEkle(SekerEkle(SutEkle(Kahve())))
    print(f"  {super_kahve.aciklama()}: {super_kahve.maliyet()} TL")
