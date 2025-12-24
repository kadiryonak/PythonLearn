"""
FACTORY PATTERN 


NE İÇİN KULLANILIR?

Factory pattern, nesne oluşturma mantığını istemci kodundan ayırır.
Hangi sınıfın örneğinin oluşturulacağına çalışma zamanında karar verir.
İstemci, somut sınıfları bilmeden nesneler oluşturabilir.

ÜÇ TİP FACTORY:
1. Simple Factory - Basit bir fabrika metodu
2. Factory Method - Alt sınıfların nesne oluşturmasına izin verir
3. Abstract Factory - İlişkili nesne aileleri oluşturur

KULLANIM ALANLARI:
- Oyunlarda farklı düşman/karakter oluşturma
- Belge formatları (PDF, Word, Excel) oluşturma
- Veritabanı bağlantıları (MySQL, PostgreSQL, SQLite)
- UI bileşenleri (Button, TextBox, Checkbox)
- Ödeme yöntemleri (Kredi kartı, PayPal, Kripto)

AVANTAJLARI:
- Loose coupling (gevşek bağlılık)
- Single Responsibility: Nesne oluşturma ayrı yerde
- Open/Closed: Yeni tipler kolayca eklenebilir
- Kod tekrarını azaltır
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Type

# ÖRNEK 1: Simple Factory (Basit Fabrika)

class Hayvan(ABC):
    """Soyut hayvan sınıfı"""
    
    @abstractmethod
    def ses_cikar(self) -> str:
        pass
    
    @abstractmethod
    def hareket_et(self) -> str:
        pass


class Kopek(Hayvan):
    def ses_cikar(self) -> str:
        return "Hav hav! 🐕"
    
    def hareket_et(self) -> str:
        return "Koşarak hareket ediyor"


class Kedi(Hayvan):
    def ses_cikar(self) -> str:
        return "Miyav! 🐱"
    
    def hareket_et(self) -> str:
        return "Sessizce yürüyor"


class Kus(Hayvan):
    def ses_cikar(self) -> str:
        return "Cik cik! 🐦"
    
    def hareket_et(self) -> str:
        return "Uçarak hareket ediyor"


class HayvanFabrikasi:
    """Simple Factory - Hayvan nesneleri oluşturur"""
    
    @staticmethod
    def hayvan_olustur(hayvan_tipi: str) -> Hayvan:
        hayvanlar = {
            "kopek": Kopek,
            "kedi": Kedi,
            "kus": Kus
        }
        
        hayvan_tipi = hayvan_tipi.lower()
        if hayvan_tipi not in hayvanlar:
            raise ValueError(f"Bilinmeyen hayvan tipi: {hayvan_tipi}. "
                           f"Geçerli tipler: {list(hayvanlar.keys())}")
        
        return hayvanlar[hayvan_tipi]()


# ÖRNEK 2: Factory Method Pattern

class Belge(ABC):
    """Soyut belge sınıfı"""
    
    @abstractmethod
    def olustur(self) -> str:
        pass
    
    @abstractmethod
    def kaydet(self, dosya_adi: str) -> str:
        pass


class PDFBelge(Belge):
    def olustur(self) -> str:
        return "PDF belgesi oluşturuldu"
    
    def kaydet(self, dosya_adi: str) -> str:
        return f"{dosya_adi}.pdf olarak kaydedildi"


class WordBelge(Belge):
    def olustur(self) -> str:
        return "Word belgesi oluşturuldu"
    
    def kaydet(self, dosya_adi: str) -> str:
        return f"{dosya_adi}.docx olarak kaydedildi"


class ExcelBelge(Belge):
    def olustur(self) -> str:
        return "Excel belgesi oluşturuldu"
    
    def kaydet(self, dosya_adi: str) -> str:
        return f"{dosya_adi}.xlsx olarak kaydedildi"


class BelgeOlusturucu(ABC):
    """Factory Method - Alt sınıflar belge tipini belirler"""
    
    @abstractmethod
    def belge_olustur(self) -> Belge:
        """Factory method - alt sınıflar override eder"""
        pass
    
    def belge_isle(self, dosya_adi: str) -> str:
        """Template method - ortak işlem mantığı"""
        belge = self.belge_olustur()
        sonuc = []
        sonuc.append(belge.olustur())
        sonuc.append(belge.kaydet(dosya_adi))
        return "\n".join(sonuc)


class PDFOlusturucu(BelgeOlusturucu):
    def belge_olustur(self) -> Belge:
        return PDFBelge()


class WordOlusturucu(BelgeOlusturucu):
    def belge_olustur(self) -> Belge:
        return WordBelge()


class ExcelOlusturucu(BelgeOlusturucu):
    def belge_olustur(self) -> Belge:
        return ExcelBelge()


# ÖRNEK 3: Abstract Factory Pattern

# Ürün aileleri
class Buton(ABC):
    @abstractmethod
    def tikla(self) -> str:
        pass


class TextBox(ABC):
    @abstractmethod
    def yaz(self, metin: str) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def sec(self) -> str:
        pass


# Windows ürün ailesi
class WindowsButon(Buton):
    def tikla(self) -> str:
        return "[Windows] Buton tıklandı ✓"


class WindowsTextBox(TextBox):
    def yaz(self, metin: str) -> str:
        return f"[Windows] TextBox: '{metin}'"


class WindowsCheckbox(Checkbox):
    def sec(self) -> str:
        return "[Windows] Checkbox seçildi ☑"


# MacOS ürün ailesi
class MacButon(Buton):
    def tikla(self) -> str:
        return "[macOS] Buton tıklandı ●"


class MacTextBox(TextBox):
    def yaz(self, metin: str) -> str:
        return f"[macOS] TextBox: '{metin}'"


class MacCheckbox(Checkbox):
    def sec(self) -> str:
        return "[macOS] Checkbox seçildi ✔"


# Linux ürün ailesi
class LinuxButon(Buton):
    def tikla(self) -> str:
        return "[Linux] Buton tıklandı 🐧"


class LinuxTextBox(TextBox):
    def yaz(self, metin: str) -> str:
        return f"[Linux] TextBox: '{metin}'"


class LinuxCheckbox(Checkbox):
    def sec(self) -> str:
        return "[Linux] Checkbox seçildi ▣"


# Abstract Factory
class UIFabrikasi(ABC):
    """Abstract Factory - UI bileşen ailesi oluşturur"""
    
    @abstractmethod
    def buton_olustur(self) -> Buton:
        pass
    
    @abstractmethod
    def textbox_olustur(self) -> TextBox:
        pass
    
    @abstractmethod
    def checkbox_olustur(self) -> Checkbox:
        pass


class WindowsFabrikasi(UIFabrikasi):
    def buton_olustur(self) -> Buton:
        return WindowsButon()
    
    def textbox_olustur(self) -> TextBox:
        return WindowsTextBox()
    
    def checkbox_olustur(self) -> Checkbox:
        return WindowsCheckbox()


class MacFabrikasi(UIFabrikasi):
    def buton_olustur(self) -> Buton:
        return MacButon()
    
    def textbox_olustur(self) -> TextBox:
        return MacTextBox()
    
    def checkbox_olustur(self) -> Checkbox:
        return MacCheckbox()


class LinuxFabrikasi(UIFabrikasi):
    def buton_olustur(self) -> Buton:
        return LinuxButon()
    
    def textbox_olustur(self) -> TextBox:
        return LinuxTextBox()
    
    def checkbox_olustur(self) -> Checkbox:
        return LinuxCheckbox()


def fabrika_sec(os_tipi: str) -> UIFabrikasi:
    """İşletim sistemine göre uygun fabrikayı döndürür"""
    fabrikalar = {
        "windows": WindowsFabrikasi,
        "macos": MacFabrikasi,
        "linux": LinuxFabrikasi
    }
    
    os_tipi = os_tipi.lower()
    if os_tipi not in fabrikalar:
        raise ValueError(f"Desteklenmeyen OS: {os_tipi}")
    
    return fabrikalar[os_tipi]()


# ÖRNEK 4: Registry-based Factory

class OdemeYontemi(ABC):
    @abstractmethod
    def odeme_yap(self, miktar: float) -> str:
        pass


class KrediKarti(OdemeYontemi):
    def odeme_yap(self, miktar: float) -> str:
        return f"💳 Kredi kartı ile {miktar} TL ödendi"


class Havale(OdemeYontemi):
    def odeme_yap(self, miktar: float) -> str:
        return f"🏦 Havale ile {miktar} TL ödendi"


class Kripto(OdemeYontemi):
    def odeme_yap(self, miktar: float) -> str:
        return f"₿ Kripto para ile {miktar} TL ödendi"


class OdemeYontemiFabrikasi:
    """Registry-based Factory - Dinamik kayıt sistemi"""
    
    _yontemler: Dict[str, Type[OdemeYontemi]] = {}
    
    @classmethod
    def kayit_ol(cls, isim: str, yontem_sinifi: Type[OdemeYontemi]):
        """Yeni ödeme yöntemi kaydet"""
        cls._yontemler[isim.lower()] = yontem_sinifi
        print(f"  ✓ '{isim}' ödeme yöntemi kaydedildi")
    
    @classmethod
    def olustur(cls, isim: str) -> OdemeYontemi:
        """Kayıtlı ödeme yöntemi oluştur"""
        isim = isim.lower()
        if isim not in cls._yontemler:
            raise ValueError(f"Kayıtlı olmayan yöntem: {isim}. "
                           f"Mevcut: {list(cls._yontemler.keys())}")
        return cls._yontemler[isim]()
    
    @classmethod
    def mevcut_yontemler(cls) -> list:
        return list(cls._yontemler.keys())



if __name__ == "__main__":

    print("FACTORY PATTERN ÖRNEKLERİ")

    
    # Örnek 1: Simple Factory
    print("\n1. Simple Factory - Hayvan Fabrikası:")

    
    for tip in ["kopek", "kedi", "kus"]:
        hayvan = HayvanFabrikasi.hayvan_olustur(tip)
        print(f"  {tip.capitalize()}: {hayvan.ses_cikar()} - {hayvan.hareket_et()}")
    

    print("\n" + "=" * 55)
    print("2. Factory Method - Belge Oluşturucular:")

    
    olusturucular = [
        ("Rapor", PDFOlusturucu()),
        ("Makale", WordOlusturucu()),
        ("Bütçe", ExcelOlusturucu())
    ]
    
    for dosya_adi, olusturucu in olusturucular:
        print(f"\n  [{dosya_adi}]")
        print(f"  {olusturucu.belge_isle(dosya_adi)}")
    
    # Örnek 3: Abstract Factory
    print("3. Abstract Factory - UI Bileşenleri:")

    
    for os_tipi in ["Windows", "macOS", "Linux"]:
        print(f"\n  [{os_tipi} UI]")
        fabrika = fabrika_sec(os_tipi)
        
        buton = fabrika.buton_olustur()
        textbox = fabrika.textbox_olustur()
        checkbox = fabrika.checkbox_olustur()
        
        print(f"    {buton.tikla()}")
        print(f"    {textbox.yaz('Merhaba Dünya')}")
        print(f"    {checkbox.sec()}")
    
    # Örnek 4: Registry-based Factory
    print("4. Registry-based Factory - Ödeme Yöntemleri:")

    
    # Yöntemleri kaydet
    print("\n  [Kayıt İşlemi]")
    OdemeYontemiFabrikasi.kayit_ol("kredi_karti", KrediKarti)
    OdemeYontemiFabrikasi.kayit_ol("havale", Havale)
    OdemeYontemiFabrikasi.kayit_ol("kripto", Kripto)
    
    # Yöntemleri kullan
    print(f"\n  [Mevcut Yöntemler]: {OdemeYontemiFabrikasi.mevcut_yontemler()}")
    print("\n  [Ödeme İşlemleri]")
    
    for yontem in ["kredi_karti", "havale", "kripto"]:
        odeme = OdemeYontemiFabrikasi.olustur(yontem)
        print(f"    {odeme.odeme_yap(150)}")
