"""
SOLID - L: Liskov Substitution Principle (LSP)
===============================================
Liskov Yerine Geçme Prensibi

TANIM:
------
Alt sınıflar, üst sınıfların yerine geçebilmelidir.
Yani, bir program üst sınıf tipinde nesne beklerken,
alt sınıf nesnesi de sorunsuz çalışmalıdır.

NEDEN ÖNEMLİ?
-------------
- Polimorfizmin doğru çalışmasını sağlar
- Beklenmeyen davranışları önler
- Kod güvenilirliğini artırır
- Interface sözleşmelerine uyumu garanti eder

KURAL:
------
"S, T'nin alt tipi ise, T tipindeki nesneler 
S tipindeki nesnelerle değiştirilebilmelidir"
- Barbara Liskov (1987)
"""

from abc import ABC, abstractmethod

# ==========================================
# ❌ YANLIŞ ÖRNEK - LSP İhlali (Klasik Kare-Dikdörtgen)
# ==========================================

class DikdortgenKotu:
    """Dikdörtgen sınıfı"""
    
    def __init__(self, genislik: float, yukseklik: float):
        self._genislik = genislik
        self._yukseklik = yukseklik
    
    @property
    def genislik(self) -> float:
        return self._genislik
    
    @genislik.setter
    def genislik(self, deger: float):
        self._genislik = deger
    
    @property
    def yukseklik(self) -> float:
        return self._yukseklik
    
    @yukseklik.setter
    def yukseklik(self, deger: float):
        self._yukseklik = deger
    
    def alan(self) -> float:
        return self._genislik * self._yukseklik


class KareKotu(DikdortgenKotu):
    """
    ❌ LSP İHLALİ!
    Kare, dikdörtgenin özel hali gibi görünse de,
    davranışsal olarak farklıdır.
    """
    
    def __init__(self, kenar: float):
        super().__init__(kenar, kenar)
    
    @DikdortgenKotu.genislik.setter
    def genislik(self, deger: float):
        # Kare'de genişlik değişince yükseklik de değişmeli
        self._genislik = deger
        self._yukseklik = deger  # Beklenmeyen davranış!
    
    @DikdortgenKotu.yukseklik.setter
    def yukseklik(self, deger: float):
        self._genislik = deger
        self._yukseklik = deger  # Beklenmeyen davranış!


def dikdortgen_alanini_test_et(dikdortgen: DikdortgenKotu):
    """
    Bu fonksiyon dikdörtgen beklediğinde kare verirsek
    beklenmeyen sonuçlar alırız!
    """
    dikdortgen.genislik = 5
    dikdortgen.yukseklik = 4
    # Beklenen alan: 5 * 4 = 20
    # Kare verilirse: 4 * 4 = 16 (YANLIŞ!)
    return dikdortgen.alan()


# ==========================================
# ✅ DOĞRU ÖRNEK - LSP Uygulanmış
# ==========================================

class Sekil(ABC):
    """Soyut şekil sınıfı - Interface tanımlar"""
    
    @abstractmethod
    def alan(self) -> float:
        pass
    
    @abstractmethod
    def cevre(self) -> float:
        pass


class Dikdortgen(Sekil):
    """Dikdörtgen - Bağımsız implementasyon"""
    
    def __init__(self, genislik: float, yukseklik: float):
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    def alan(self) -> float:
        return self.genislik * self.yukseklik
    
    def cevre(self) -> float:
        return 2 * (self.genislik + self.yukseklik)
    
    def __str__(self):
        return f"Dikdörtgen({self.genislik}x{self.yukseklik})"


class Kare(Sekil):
    """Kare - Bağımsız implementasyon (kalıtım yok!)"""
    
    def __init__(self, kenar: float):
        self.kenar = kenar
    
    def alan(self) -> float:
        return self.kenar ** 2
    
    def cevre(self) -> float:
        return 4 * self.kenar
    
    def __str__(self):
        return f"Kare({self.kenar})"


class Daire(Sekil):
    """Daire - Bağımsız implementasyon"""
    
    def __init__(self, yaricap: float):
        self.yaricap = yaricap
    
    def alan(self) -> float:
        return 3.14159 * self.yaricap ** 2
    
    def cevre(self) -> float:
        return 2 * 3.14159 * self.yaricap
    
    def __str__(self):
        return f"Daire(r={self.yaricap})"


def sekil_bilgisi_yazdir(sekil: Sekil):
    """
    Bu fonksiyon HERHANGİ bir Sekil alt tipiyle çalışır!
    LSP sayesinde tüm alt tipler beklendiği gibi davranır.
    """
    print(f"  {sekil}")
    print(f"    Alan: {sekil.alan():.2f}")
    print(f"    Çevre: {sekil.cevre():.2f}")


# ==========================================
# BONUS: Kuş Örneği - Davranışsal LSP
# ==========================================

class Kus(ABC):
    """Soyut kuş sınıfı"""
    
    @abstractmethod
    def ye(self) -> str:
        pass
    
    @abstractmethod
    def uyu(self) -> str:
        pass


class UcanKus(Kus):
    """Uçabilen kuşlar"""
    
    @abstractmethod
    def uc(self) -> str:
        pass


class YuruenKus(Kus):
    """Uçamayan kuşlar"""
    
    @abstractmethod
    def yuru(self) -> str:
        pass


class Kartal(UcanKus):
    def ye(self) -> str:
        return "🦅 Kartal et yiyor"
    
    def uyu(self) -> str:
        return "🦅 Kartal yuvada uyuyor"
    
    def uc(self) -> str:
        return "🦅 Kartal yüksekten uçuyor"


class Serce(UcanKus):
    def ye(self) -> str:
        return "🐦 Serçe tohum yiyor"
    
    def uyu(self) -> str:
        return "🐦 Serçe dalda uyuyor"
    
    def uc(self) -> str:
        return "🐦 Serçe kısa mesafe uçuyor"


class Penguen(YuruenKus):
    """
    ✅ Penguen UcanKus'tan türemez!
    Çünkü uçamaz - LSP ihlali olurdu.
    """
    def ye(self) -> str:
        return "🐧 Penguen balık yiyor"
    
    def uyu(self) -> str:
        return "🐧 Penguen ayakta uyuyor"
    
    def yuru(self) -> str:
        return "🐧 Penguen yürüyor/kayıyor"


class Devekusu(YuruenKus):
    def ye(self) -> str:
        return "🦃 Devekuşu bitki yiyor"
    
    def uyu(self) -> str:
        return "🦃 Devekuşu yerde uyuyor"
    
    def yuru(self) -> str:
        return "🦃 Devekuşu hızla koşuyor"


def ucan_kuslari_ucur(kuslar: list[UcanKus]):
    """Sadece uçabilen kuşlarla çalışır"""
    for kus in kuslar:
        print(f"  {kus.uc()}")


def tum_kuslari_besle(kuslar: list[Kus]):
    """Tüm kuşlarla çalışır - LSP garantili"""
    for kus in kuslar:
        print(f"  {kus.ye()}")


# ==========================================
# KULLANIM ÖRNEĞİ
# ==========================================

if __name__ == "__main__":
    print("=" * 55)
    print("LISKOV SUBSTITUTION PRINCIPLE (LSP)")
    print("=" * 55)
    
    # Yanlış örnek gösterimi
    print("\n❌ YANLIŞ ÖRNEK (Kare-Dikdörtgen İhlali):")
    print("-" * 35)
    
    dikdortgen = DikdortgenKotu(10, 10)
    kare = KareKotu(10)
    
    print(f"  Dikdörtgen ile test: {dikdortgen_alanini_test_et(dikdortgen)}")
    print(f"  Kare ile test: {dikdortgen_alanini_test_et(kare)}")
    print("  → Beklenen: 20, Kare sonucu: 16 (YANLIŞ!)")
    
    # Doğru örnek
    print("\n" + "=" * 55)
    print("✅ DOĞRU ÖRNEK (Şekil Hiyerarşisi):")
    print("-" * 35)
    
    sekiller = [
        Dikdortgen(10, 5),
        Kare(7),
        Daire(4)
    ]
    
    print("\nTüm şekillerin bilgisi:")
    for sekil in sekiller:
        sekil_bilgisi_yazdir(sekil)
        print()
    
    # Kuş örneği
    print("=" * 55)
    print("✅ DOĞRU ÖRNEK (Kuş Hiyerarşisi):")
    print("-" * 35)
    
    ucan_kuslar = [Kartal(), Serce()]
    yuruyen_kuslar = [Penguen(), Devekusu()]
    tum_kuslar = ucan_kuslar + yuruyen_kuslar
    
    print("\nUçan kuşlar uçuyor:")
    ucan_kuslari_ucur(ucan_kuslar)
    
    print("\nTüm kuşlar yemek yiyor:")
    tum_kuslari_besle(tum_kuslar)
    
    print("\n" + "=" * 55)
    print("ÖZET:")
    print("-" * 35)
    print("""
LSP'nin Temel Kuralları:
  • Alt sınıf, üst sınıfın davranışını bozmamalı
  • Ön koşullar gevşetilebilir ama sıkılaştırılamaz
  • Son koşullar sıkılaştırılabilir ama gevşetilemez
  
Penguen neden UcanKus'tan türemez?
  → Penguen.uc() metodu anlamsız olurdu
  → Hata fırlatmak veya hiçbir şey yapmamak LSP ihlalidir
  → Doğru tasarım: Ayrı YuruenKus sınıfı
    """)
