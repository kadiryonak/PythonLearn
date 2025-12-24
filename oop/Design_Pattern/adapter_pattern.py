"""
ADAPTER PATTERN (Adaptör Deseni)


NE İÇİN KULLANILIR?
-------------------
Adapter pattern, uyumsuz arayüzlere sahip sınıfların birlikte çalışmasını sağlar.
Bir sınıfın arayüzünü, istemcinin beklediği başka bir arayüze dönüştürür.
Düşünün: Avrupa prizine Türk fiş adaptörü takmak gibi!

KULLANIM ALANLARI:
- Eski sistem (legacy) entegrasyonu
- Üçüncü parti kütüphane entegrasyonu
- Farklı veri formatları arasında dönüşüm (XML ↔ JSON)
- API versiyonları arası uyumluluk
- Farklı ödeme sistemleri entegrasyonu

AVANTAJLARI:
- Mevcut kodu değiştirmeden yeni sistemlerle çalışabilirsiniz
- Single Responsibility: Dönüşüm mantığı ayrı sınıfta
- Open/Closed: Yeni adaptörler eklenebilir

İKİ TİP ADAPTER:
1. Object Adapter (Nesne Adaptörü) - Kompozisyon kullanır (önerilen)
2. Class Adapter (Sınıf Adaptörü) - Çoklu kalıtım kullanır
"""

from abc import ABC, abstractmethod


# ÖRNEK 1: Ödeme Sistemi Adaptörü


# Hedef arayüz (Target Interface) - İstemcinin beklediği arayüz
class OdemeSistemi(ABC):
    @abstractmethod
    def odeme_yap(self, miktar: float) -> str:
        pass
    
    @abstractmethod
    def bakiye_sorgula(self) -> float:
        pass


# Mevcut sistem - Bizim kullandığımız standart ödeme
class BankaOdeme(OdemeSistemi):
    def __init__(self, hesap_no: str, bakiye: float = 1000.0):
        self.hesap_no = hesap_no
        self._bakiye = bakiye
    
    def odeme_yap(self, miktar: float) -> str:
        if miktar <= self._bakiye:
            self._bakiye -= miktar
            return f"Banka: {miktar} TL ödeme başarılı. Kalan: {self._bakiye} TL"
        return "Banka: Yetersiz bakiye!"
    
    def bakiye_sorgula(self) -> float:
        return self._bakiye


# Uyumsuz sistem (Adaptee) - Farklı API'ye sahip üçüncü parti
class PayPalAPI:
    """PayPal'ın kendi API'si - Farklı metot isimleri kullanıyor"""
    def __init__(self, email: str, balance: float = 500.0):
        self.email = email
        self._balance = balance
    
    def make_payment(self, amount: float, currency: str = "USD") -> dict:
        if amount <= self._balance:
            self._balance -= amount
            return {"status": "success", "amount": amount, "currency": currency}
        return {"status": "failed", "error": "insufficient_funds"}
    
    def get_balance(self) -> dict:
        return {"balance": self._balance, "currency": "USD"}


# ADAPTER - PayPal'ı OdemeSistemi arayüzüne uyarlar
class PayPalAdapter(OdemeSistemi):
    """PayPal API'sini OdemeSistemi arayüzüne adapte eder"""
    
    USD_TO_TRY = 32.0  # Döviz kuru
    
    def __init__(self, paypal: PayPalAPI):
        self._paypal = paypal  # Kompozisyon (Object Adapter)
    
    def odeme_yap(self, miktar: float) -> str:
        # TL'yi USD'ye çevir
        miktar_usd = miktar / self.USD_TO_TRY
        sonuc = self._paypal.make_payment(miktar_usd, "USD")
        
        if sonuc["status"] == "success":
            return f"PayPal: {miktar} TL ({miktar_usd:.2f} USD) ödeme başarılı"
        return f"PayPal: Ödeme başarısız - {sonuc.get('error', 'Bilinmeyen hata')}"
    
    def bakiye_sorgula(self) -> float:
        sonuc = self._paypal.get_balance()
        # USD'yi TL'ye çevir
        return sonuc["balance"] * self.USD_TO_TRY



# ÖRNEK 2: Veri Formatı Adaptörü (XML ↔ JSON)


class JSONVeriKaynagi:
    """Modern JSON tabanlı veri kaynağı"""
    def __init__(self):
        self._veri = {
            "kullanicilar": [
                {"id": 1, "ad": "Ahmet", "yas": 25},
                {"id": 2, "ad": "Ayşe", "yas": 30}
            ]
        }
    
    def veri_getir(self) -> dict:
        return self._veri
    
    def kullanici_ekle(self, kullanici: dict) -> bool:
        self._veri["kullanicilar"].append(kullanici)
        return True


class XMLVeriKaynagi:
    """Eski XML tabanlı sistem"""
    def __init__(self):
        self._xml = """
        <kullanicilar>
            <kullanici id="1"><ad>Mehmet</ad><yas>35</yas></kullanici>
            <kullanici id="2"><ad>Fatma</ad><yas>28</yas></kullanici>
        </kullanicilar>
        """
    
    def read_xml(self) -> str:
        return self._xml
    
    def write_xml(self, xml_str: str) -> bool:
        self._xml = xml_str
        return True


class XMLtoJSONAdapter:
    """XML veri kaynağını JSON arayüzüne adapte eder"""
    
    def __init__(self, xml_kaynak: XMLVeriKaynagi):
        self._xml_kaynak = xml_kaynak
    
    def veri_getir(self) -> dict:
        """XML'i JSON formatına dönüştürür (basitleştirilmiş)"""
        xml_icerik = self._xml_kaynak.read_xml()
        
        # Basit XML parsing (gerçek projede xml.etree kullanılır)
        kullanicilar = []
        import re
        pattern = r'<kullanici id="(\d+)"><ad>(\w+)</ad><yas>(\d+)</yas></kullanici>'
        matches = re.findall(pattern, xml_icerik)
        
        for match in matches:
            kullanicilar.append({
                "id": int(match[0]),
                "ad": match[1],
                "yas": int(match[2])
            })
        
        return {"kullanicilar": kullanicilar}
    
    def kullanici_ekle(self, kullanici: dict) -> bool:
        """JSON formatındaki kullanıcıyı XML'e dönüştürüp ekler"""
        yeni_xml = f'<kullanici id="{kullanici["id"]}"><ad>{kullanici["ad"]}</ad><yas>{kullanici["yas"]}</yas></kullanici>'
        mevcut_xml = self._xml_kaynak.read_xml()
        guncel_xml = mevcut_xml.replace("</kullanicilar>", f"{yeni_xml}\n</kullanicilar>")
        return self._xml_kaynak.write_xml(guncel_xml)



# ÖRNEK 3: Elektrik Prizi Adaptörü


class AvrupaPriz:
    """Avrupa tipi priz (220V, 2 pin)"""
    def elektrik_ver(self) -> str:
        return "220V, 50Hz, 2-pin Avrupa standardı elektrik"


class AmerikaFis:
    """Amerika tipi fiş (110V, 3 pin) - Uyumsuz!"""
    def __init__(self, cihaz_adi: str):
        self.cihaz_adi = cihaz_adi
    
    def connect_to_110v(self) -> str:
        return f"{self.cihaz_adi}: 110V, 60Hz, 3-pin Amerikan fişe bağlandı"


class AmerikaToAvrupaAdaptor:
    """Amerikan cihazları Avrupa prizine bağlar"""
    
    def __init__(self, amerikan_cihaz: AmerikaFis):
        self._cihaz = amerikan_cihaz
    
    def avrupa_prizine_bagla(self, priz: AvrupaPriz) -> str:
        # Voltaj ve frekans dönüşümü simülasyonu
        avrupa_elektrik = priz.elektrik_ver()
        # 220V -> 110V dönüştürücü
        return (f"[ADAPTÖR] {avrupa_elektrik}\n"
                f"         → 110V'a dönüştürüldü\n"
                f"         → {self._cihaz.cihaz_adi} çalışıyor!")


# KULLANIM ÖRNEKLERİ


def odeme_isle(odeme_sistemi: OdemeSistemi, miktar: float):
    """Herhangi bir ödeme sistemiyle çalışabilen fonksiyon"""
    print(f"  Bakiye: {odeme_sistemi.bakiye_sorgula():.2f} TL")
    print(f"  {odeme_sistemi.odeme_yap(miktar)}")
    print(f"  Yeni Bakiye: {odeme_sistemi.bakiye_sorgula():.2f} TL")


if __name__ == "__main__":
    print("ADAPTER PATTERN ÖRNEKLERİ")
    # Örnek 1: Ödeme Sistemi
    print("\n1. Ödeme Sistemi Adaptörü:")

    
    # Normal banka ödemesi
    print("\n  [Banka Ödemesi]")
    banka = BankaOdeme("TR123456789")
    odeme_isle(banka, 100)
    
    # PayPal - Adaptör ile
    print("\n  [PayPal Ödemesi - Adaptör ile]")
    paypal_api = PayPalAPI("user@email.com", 500)  # 500 USD
    paypal_adapter = PayPalAdapter(paypal_api)
    odeme_isle(paypal_adapter, 320)  # 10 USD = 320 TL
    
    # Örnek 2: Veri Formatı Dönüşümü
    print("2. XML → JSON Adaptörü:")

    
    json_kaynak = JSONVeriKaynagi()
    print(f"\n  [JSON Kaynak]: {json_kaynak.veri_getir()}")
    
    xml_kaynak = XMLVeriKaynagi()
    xml_adapter = XMLtoJSONAdapter(xml_kaynak)
    print(f"  [XML→JSON Adaptör]: {xml_adapter.veri_getir()}")
    

    print("3. Elektrik Prizi Adaptörü :")

    
    avrupa_priz = AvrupaPriz()
    amerikan_laptop = AmerikaFis("MacBook Pro")
    adaptor = AmerikaToAvrupaAdaptor(amerikan_laptop)
    
    print(f"\n  {adaptor.avrupa_prizine_bagla(avrupa_priz)}")
