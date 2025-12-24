# ==========================================
# PROPERTY - GETTER - SETTER - DELETER
# ==========================================
# Property: Sınıf attribute'larına kontrollü erişim sağlar.
# Dışarıdan normal değişken gibi görünür ama arka planda 
# fonksiyonlar çalışır.


# ÖRNEK 1: Property Olmadan (Kötü Yöntem)
class KotuOrnek:
    def __init__(self):
        self.yas = 0  # Dışarıdan doğrudan erişilebilir
        
kisi = KotuOrnek()
kisi.yas = -5  # Geçersiz değer atanabilir! Kontrol yok.
print(f"Kötü örnek yaş: {kisi.yas}")



# ÖRNEK 2: Getter ve Setter Metodları (Eski Yöntem)
class EskiYontem:
    def __init__(self):
        self._yas = 0  # _ ile private olduğunu belirtiyoruz
    
    def get_yas(self):
        return self._yas
    
    def set_yas(self, deger):
        if deger < 0:
            print("Yaş negatif olamaz!")
        else:
            self._yas = deger

kisi2 = EskiYontem()
kisi2.set_yas(-5)  # "Yaş negatif olamaz!"
kisi2.set_yas(25)
print(f"Eski yöntem yaş: {kisi2.get_yas()}")  # 25



# ÖRNEK 3: @property Dekoratörü (Modern Yöntem)
class Kisi:
    def __init__(self, isim, yas):
        self._isim = isim
        self._yas = yas  # Private değişken
    
    # GETTER - Değeri okumak için
    @property
    def yas(self):
        print("[GETTER çağrıldı]")
        return self._yas
    
    # SETTER - Değer atamak için
    @yas.setter
    def yas(self, deger):
        print("[SETTER çağrıldı]")
        if deger < 0:
            raise ValueError("Yaş negatif olamaz!")
        elif deger > 150:
            raise ValueError("Yaş 150'den büyük olamaz!")
        self._yas = deger
    
    # DELETER - Değeri silmek için
    @yas.deleter
    def yas(self):
        print("[DELETER çağrıldı]")
        print("Yaş silindi, varsayılan değer atandı.")
        self._yas = 0

# Kullanım
print("\nProperty Kullanımı")
ahmet = Kisi("Ahmet", 30)

# Getter - okuma
print(f"Yaş: {ahmet.yas}")  # [GETTER çağrıldı] -> 30

# Setter - yazma
ahmet.yas = 35  # [SETTER çağrıldı]
print(f"Yeni yaş: {ahmet.yas}")  # 35

# Deleter - silme
del ahmet.yas  # [DELETER çağrıldı]
print(f"Silindikten sonra: {ahmet.yas}")  # 0



# ÖRNEK 4: Hesaplanmış Property (Sadece Getter)
class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    @property
    def alan(self):
        return self.genislik * self.yukseklik
    
    @property
    def cevre(self):
        return 2 * (self.genislik + self.yukseklik)

print("\nHesaplanmış Property")
dikdortgen = Dikdortgen(5, 3)
print(f"Alan: {dikdortgen.alan}")    # 15 (otomatik hesaplanır)
print(f"Çevre: {dikdortgen.cevre}")  # 16



# ÖRNEK 5: Property ile Veri Doğrulama
class Email:
    def __init__(self):
        self._email = ""
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, deger):
        if "@" not in deger:
            raise ValueError("Geçersiz email! '@' karakteri olmalı.")
        if "." not in deger:
            raise ValueError("Geçersiz email! '.' karakteri olmalı.")
        self._email = deger

print("\nEmail Doğrulama")
kullanici = Email()
kullanici.email = "test@example.com"  # Geçerli
print(f"Email: {kullanici.email}")

# kullanici.email = "gecersizemail"  # ValueError fırlatır!