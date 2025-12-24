"""
SOLID - I: Interface Segregation Principle (ISP)
=================================================
Arayüz Ayrımı Prensibi

TANIM:
------
İstemciler, kullanmadıkları arayüzlere bağımlı olmaya 
zorlanmamalıdır. Büyük arayüzler yerine küçük ve 
özelleşmiş arayüzler tercih edilmelidir.

NEDEN ÖNEMLİ?
- Gereksiz bağımlılıkları önler
- Daha esnek ve modüler kod sağlar
- Test etmesi daha kolay olur
"""

from abc import ABC, abstractmethod

# ==========================================
# ❌ YANLIŞ - Şişman Arayüz
# ==========================================

class CokAmacliCihazKotu(ABC):
    """Tüm cihazlar bu devasa interface'i implement etmeli"""
    
    @abstractmethod
    def yazdir(self, belge: str): pass
    
    @abstractmethod
    def tara(self) -> str: pass
    
    @abstractmethod
    def faksla(self, belge: str, numara: str): pass


class BasitYaziciKotu(CokAmacliCihazKotu):
    """Bu yazıcı sadece yazdırabilir ama hepsini implement etmeli!"""
    
    def yazdir(self, belge: str):
        print(f"Yazdırılıyor: {belge}")
    
    def tara(self) -> str:
        raise NotImplementedError("Bu cihaz tarama yapamaz!")
    
    def faksla(self, belge: str, numara: str):
        raise NotImplementedError("Bu cihaz faks gönderemez!")


# ==========================================
# ✅ DOĞRU - Küçük Özelleşmiş Arayüzler
# ==========================================

class Yazici(ABC):
    @abstractmethod
    def yazdir(self, belge: str): pass


class Tarayici(ABC):
    @abstractmethod
    def tara(self) -> str: pass


class Faks(ABC):
    @abstractmethod
    def faksla(self, belge: str, numara: str): pass


class BasitYazici(Yazici):
    """Sadece yazdırabilir - tek interface"""
    def yazdir(self, belge: str):
        print(f"🖨️ Yazdırılıyor: {belge}")


class CokFonksiyonluYazici(Yazici, Tarayici, Faks):
    """Tüm özelliklere sahip"""
    def yazdir(self, belge: str):
        print(f"🖨️ Yazdırılıyor: {belge}")
    
    def tara(self) -> str:
        return "taranan_belge.pdf"
    
    def faksla(self, belge: str, numara: str):
        print(f"📠 Faks: {belge} → {numara}")


# İşçi örneği
class Calisan(ABC):
    @abstractmethod
    def calis(self) -> str: pass


class Yemekli(ABC):
    @abstractmethod
    def yemek_ye(self) -> str: pass


class InsanCalisan(Calisan, Yemekli):
    def __init__(self, isim: str):
        self.isim = isim
    
    def calis(self) -> str:
        return f"👨‍💼 {self.isim} çalışıyor"
    
    def yemek_ye(self) -> str:
        return f"🍽️ {self.isim} yemek yiyor"


class RobotCalisan(Calisan):
    """Robot sadece çalışır, yemek yemez!"""
    def __init__(self, model: str):
        self.model = model
    
    def calis(self) -> str:
        return f"🤖 {self.model} 7/24 çalışıyor"


if __name__ == "__main__":
    print("=" * 50)
    print("INTERFACE SEGREGATION PRINCIPLE")
    print("=" * 50)
    
    basit = BasitYazici()
    coklu = CokFonksiyonluYazici()
    
    basit.yazdir("Rapor.pdf")
    coklu.yazdir("Belge.pdf")
    coklu.faksla("Sözleşme.pdf", "555-1234")
    
    print("\nÇalışanlar:")
    ahmet = InsanCalisan("Ahmet")
    robot = RobotCalisan("R2-D2")
    
    print(ahmet.calis())
    print(ahmet.yemek_ye())
    print(robot.calis())
    # robot.yemek_ye() → Metod yok, hata vermez!
