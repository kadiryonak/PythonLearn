"""
SOLID - O: Open/Closed Principle (OCP)
=======================================
Açık/Kapalı Prensibi

TANIM:
------
Yazılım varlıkları (sınıflar, modüller, fonksiyonlar) 
genişlemeye AÇIK, değişikliğe KAPALI olmalıdır.

NEDEN ÖNEMLİ?
-------------
- Mevcut kodu değiştirmeden yeni özellikler eklenebilir
- Mevcut testler bozulmaz
- Kod daha stabil ve güvenilir olur
- Yan etki riski azalır

NASIL UYGULANIR?
----------------
- Soyutlama (abstraction) kullanın
- Kalıtım ve polimorfizm kullanın
- Strategy pattern uygulayın
"""

from abc import ABC, abstractmethod
from enum import Enum

# ==========================================
# ❌ YANLIŞ ÖRNEK - OCP İhlali
# ==========================================

class IndirimTipi(Enum):
    NORMAL = "normal"
    VIP = "vip"
    OGRENCI = "ogrenci"


class IndirimHesaplayiciKotu:
    """
    Bu sınıf OCP'yi ihlal ediyor!
    Her yeni indirim tipi eklendiğinde bu sınıfı değiştirmek gerekiyor.
    """
    
    def indirim_hesapla(self, fiyat: float, tip: IndirimTipi) -> float:
        if tip == IndirimTipi.NORMAL:
            return fiyat * 0.05  # %5 indirim
        elif tip == IndirimTipi.VIP:
            return fiyat * 0.20  # %20 indirim
        elif tip == IndirimTipi.OGRENCI:
            return fiyat * 0.15  # %15 indirim
        # Yeni tip eklemek için bu metodu DEĞİŞTİRMEK gerekiyor! ❌
        else:
            return 0


# ==========================================
# ✅ DOĞRU ÖRNEK - OCP Uygulanmış
# ==========================================

class IndirimStratejisi(ABC):
    """Soyut indirim stratejisi - GENİŞLEMEYE AÇIK"""
    
    @property
    @abstractmethod
    def isim(self) -> str:
        pass
    
    @abstractmethod
    def hesapla(self, fiyat: float) -> float:
        pass


class NormalIndirim(IndirimStratejisi):
    """Normal müşteri indirimi - %5"""
    
    @property
    def isim(self) -> str:
        return "Normal Müşteri"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * 0.05


class VIPIndirim(IndirimStratejisi):
    """VIP müşteri indirimi - %20"""
    
    @property
    def isim(self) -> str:
        return "VIP Müşteri"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * 0.20


class OgrenciIndirim(IndirimStratejisi):
    """Öğrenci indirimi - %15"""
    
    @property
    def isim(self) -> str:
        return "Öğrenci"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * 0.15


# ✅ YENİ İNDİRİM TİPLERİ - Mevcut kod DEĞİŞMEDEN eklendi!
class EmekliIndirim(IndirimStratejisi):
    """Emekli indirimi - %25"""
    
    @property
    def isim(self) -> str:
        return "Emekli"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * 0.25


class BlackFridayIndirim(IndirimStratejisi):
    """Black Friday özel indirimi - %40"""
    
    @property
    def isim(self) -> str:
        return "Black Friday"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * 0.40


class YuzdelikIndirim(IndirimStratejisi):
    """Dinamik yüzdelik indirim oluşturmak için"""
    
    def __init__(self, yuzde: float, aciklama: str = "Özel"):
        self._yuzde = yuzde
        self._aciklama = aciklama
    
    @property
    def isim(self) -> str:
        return f"{self._aciklama} (%{self._yuzde})"
    
    def hesapla(self, fiyat: float) -> float:
        return fiyat * (self._yuzde / 100)


class IndirimHesaplayici:
    """
    Bu sınıf DEĞİŞİKLİĞE KAPALI!
    Yeni indirim tipleri eklendiğinde bu sınıf değişmez.
    """
    
    def indirim_uygula(self, fiyat: float, strateji: IndirimStratejisi) -> dict:
        indirim_tutari = strateji.hesapla(fiyat)
        yeni_fiyat = fiyat - indirim_tutari
        
        return {
            "orijinal_fiyat": fiyat,
            "indirim_tipi": strateji.isim,
            "indirim_tutari": indirim_tutari,
            "son_fiyat": yeni_fiyat
        }


# ==========================================
# BONUS: Şekil Çizim Örneği
# ==========================================

class Sekil(ABC):
    """Soyut şekil sınıfı"""
    
    @abstractmethod
    def alan(self) -> float:
        pass
    
    @abstractmethod
    def cevre(self) -> float:
        pass
    
    @abstractmethod
    def ciz(self) -> str:
        pass


class Dikdortgen(Sekil):
    def __init__(self, genislik: float, yukseklik: float):
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    def alan(self) -> float:
        return self.genislik * self.yukseklik
    
    def cevre(self) -> float:
        return 2 * (self.genislik + self.yukseklik)
    
    def ciz(self) -> str:
        return f"▭ Dikdörtgen ({self.genislik}x{self.yukseklik})"


class Daire(Sekil):
    def __init__(self, yaricap: float):
        self.yaricap = yaricap
    
    def alan(self) -> float:
        return 3.14159 * self.yaricap ** 2
    
    def cevre(self) -> float:
        return 2 * 3.14159 * self.yaricap
    
    def ciz(self) -> str:
        return f"◯ Daire (r={self.yaricap})"


# ✅ YENİ ŞEKİL - Mevcut kod değişmedi!
class Ucgen(Sekil):
    def __init__(self, taban: float, yukseklik: float, kenarlar: tuple):
        self.taban = taban
        self.yukseklik = yukseklik
        self.kenarlar = kenarlar
    
    def alan(self) -> float:
        return 0.5 * self.taban * self.yukseklik
    
    def cevre(self) -> float:
        return sum(self.kenarlar)
    
    def ciz(self) -> str:
        return f"△ Üçgen (taban={self.taban})"


class SekilCizici:
    """Bu sınıf yeni şekiller eklendiğinde DEĞİŞMEZ!"""
    
    def toplam_alan(self, sekiller: list[Sekil]) -> float:
        return sum(s.alan() for s in sekiller)
    
    def tum_sekilleri_ciz(self, sekiller: list[Sekil]) -> None:
        for sekil in sekiller:
            print(f"  {sekil.ciz()} - Alan: {sekil.alan():.2f}")


# ==========================================
# KULLANIM ÖRNEĞİ
# ==========================================

if __name__ == "__main__":
    print("=" * 55)
    print("OPEN/CLOSED PRINCIPLE (OCP)")
    print("=" * 55)
    
    # İndirim Örneği
    print("\n✅ İNDİRİM SİSTEMİ:")
    print("-" * 35)
    
    hesaplayici = IndirimHesaplayici()
    fiyat = 1000.0
    
    indirimler = [
        NormalIndirim(),
        VIPIndirim(),
        OgrenciIndirim(),
        EmekliIndirim(),
        BlackFridayIndirim(),
        YuzdelikIndirim(30, "Yılbaşı Kampanyası")
    ]
    
    print(f"\nÜrün Fiyatı: {fiyat} TL")
    print("-" * 45)
    
    for strateji in indirimler:
        sonuc = hesaplayici.indirim_uygula(fiyat, strateji)
        print(f"  {sonuc['indirim_tipi']:25} → "
              f"İndirim: {sonuc['indirim_tutari']:6.2f} TL | "
              f"Son: {sonuc['son_fiyat']:6.2f} TL")
    
    # Şekil Örneği
    print("\n" + "=" * 55)
    print("✅ ŞEKİL ÇİZİM SİSTEMİ:")
    print("-" * 35)
    
    cizici = SekilCizici()
    sekiller = [
        Dikdortgen(10, 5),
        Daire(7),
        Ucgen(6, 4, (6, 5, 5))
    ]
    
    cizici.tum_sekilleri_ciz(sekiller)
    print(f"\n  Toplam Alan: {cizici.toplam_alan(sekiller):.2f}")
    
    print("\n" + "=" * 55)
    print("ÖZET:")
    print("-" * 35)
    print("""
OCP'nin Faydaları:
  • Yeni indirim tipi eklemek için:
    → Sadece yeni sınıf yaz
    → IndirimHesaplayici DEĞİŞMEZ!
    
  • Yeni şekil eklemek için:
    → Sadece yeni Sekil sınıfı yaz
    → SekilCizici DEĞİŞMEZ!
    
  • Mevcut testler bozulmaz
  • Yan etki riski yok
    """)
