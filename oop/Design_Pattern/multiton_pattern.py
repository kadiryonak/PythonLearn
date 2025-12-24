"""
MULTITON PATTERN 


NE İÇİN KULLANILIR?

Multiton pattern, Singleton pattern'in genelleştirilmiş halidir.
Singleton'da tek bir örnek varken, Multiton'da belirli anahtarlara göre
kontrollü sayıda örnek oluşturulur. Her anahtar için yalnızca bir örnek bulunur.

KULLANIM ALANLARI:
- Veritabanı bağlantı havuzları (her veritabanı için tek bağlantı)
- Dil/Locale yönetimi (her dil için tek örnek)
- Logger sistemleri (farklı log seviyeleri için)
- Cache yönetimi (farklı cache türleri için)
- Oyun geliştirmede world/level yönetimi

AVANTAJLARI:
- Kaynak yönetimini kontrol eder
- Aynı anahtarla her zaman aynı nesne döner
- Global erişim noktası sağlar
- Nesne sayısını sınırlar

SINGLETON vs MULTITON:
- Singleton: Tek bir global örnek
- Multiton: Anahtar başına bir örnek (sözlük tabanlı)
"""

# ÖRNEK 1: Temel Multiton Pattern

class VeritabaniBaglantisi:
    """
    Her veritabanı adı için tek bir bağlantı örneği oluşturur.
    """
    _instances = {}  # Tüm örnekleri tutan sözlük
    
    def __new__(cls, db_adi: str):
        if db_adi not in cls._instances:
            print(f"[YENİ] '{db_adi}' için bağlantı oluşturuluyor...")
            instance = super().__new__(cls)
            instance.db_adi = db_adi
            instance.bagli = True
            cls._instances[db_adi] = instance
        else:
            print(f"[MEVCUT] '{db_adi}' bağlantısı zaten var, aynısı döndürülüyor.")
        return cls._instances[db_adi]
    
    def sorgu_calistir(self, sorgu: str):
        return f"[{self.db_adi}] Sorgu çalıştırıldı: {sorgu}"
    
    @classmethod
    def tum_baglantilari_goster(cls):
        print(f"\nToplam {len(cls._instances)} adet bağlantı var:")
        for db_adi, instance in cls._instances.items():
            print(f"  - {db_adi}: {id(instance)}")


# ==========================================
# ÖRNEK 2: Logger Multiton (Dekoratör ile)
# ==========================================

class Logger:
    """
    Farklı log seviyeleri için ayrı logger örneği.
    (INFO, DEBUG, ERROR, WARNING)
    """
    _loggers = {}
    
    SEVIYELER = ["DEBUG", "INFO", "WARNING", "ERROR"]
    
    def __new__(cls, seviye: str = "INFO"):
        seviye = seviye.upper()
        if seviye not in cls.SEVIYELER:
            raise ValueError(f"Geçersiz seviye: {seviye}. Geçerli: {cls.SEVIYELER}")
        
        if seviye not in cls._loggers:
            instance = super().__new__(cls)
            instance.seviye = seviye
            instance._loglar = []
            cls._loggers[seviye] = instance
        return cls._loggers[seviye]
    
    def log(self, mesaj: str):
        log_kaydi = f"[{self.seviye}] {mesaj}"
        self._loglar.append(log_kaydi)
        print(log_kaydi)
    
    def gecmis(self):
        return self._loglar.copy()
    
    @classmethod
    def tum_loggerlar(cls):
        return list(cls._loggers.keys())



# ÖRNEK 3: Dil/Locale Multiton


class Dil:
    """
    Her dil için tek bir çeviri örneği.
    """
    _diller = {}
    
    _ceviriler = {
        "tr": {"merhaba": "Merhaba", "gule_gule": "Güle Güle", "evet": "Evet"},
        "en": {"merhaba": "Hello", "gule_gule": "Goodbye", "evet": "Yes"},
        "de": {"merhaba": "Hallo", "gule_gule": "Auf Wiedersehen", "evet": "Ja"},
        "fr": {"merhaba": "Bonjour", "gule_gule": "Au revoir", "evet": "Oui"},
    }
    
    def __new__(cls, dil_kodu: str):
        dil_kodu = dil_kodu.lower()
        if dil_kodu not in cls._ceviriler:
            raise ValueError(f"Desteklenmeyen dil: {dil_kodu}")
        
        if dil_kodu not in cls._diller:
            instance = super().__new__(cls)
            instance.kod = dil_kodu
            cls._diller[dil_kodu] = instance
        return cls._diller[dil_kodu]
    
    def cevir(self, anahtar: str) -> str:
        ceviriler = self._ceviriler.get(self.kod, {})
        return ceviriler.get(anahtar, f"[{anahtar}]")
    
    @classmethod
    def desteklenen_diller(cls):
        return list(cls._ceviriler.keys())


# ==========================================
# KULLANIM ÖRNEKLERİ
# ==========================================

if __name__ == "__main__":

    print("MULTITON PATTERN ÖRNEKLERİ")

    
    # Örnek 1: Veritabanı Bağlantı Havuzu
    print("\n1. Veritabanı Bağlantı Havuzu:")

    
    mysql_1 = VeritabaniBaglantisi("MySQL")
    postgres_1 = VeritabaniBaglantisi("PostgreSQL")
    mysql_2 = VeritabaniBaglantisi("MySQL")  # Mevcut örnek döner
    
    print(f"\nmysql_1 == mysql_2: {mysql_1 == mysql_2}")  # True
    print(f"mysql_1 == postgres_1: {mysql_1 == postgres_1}")  # False
    
    VeritabaniBaglantisi.tum_baglantilari_goster()
    
    # Örnek 2: Logger Sistemi
    print("\n2. Logger Sistemi:")
    
    info_logger = Logger("INFO")
    error_logger = Logger("ERROR")
    info_logger_2 = Logger("INFO")
    
    info_logger.log("Uygulama başlatıldı")
    error_logger.log("Bir hata oluştu!")
    info_logger_2.log("Bu da INFO logger'a gider")
    
    print(f"\ninfo_logger == info_logger_2: {info_logger == info_logger_2}")
    print(f"Aktif logger'lar: {Logger.tum_loggerlar()}")
    
    # Örnek 3: Çoklu Dil Desteği
    print("\n3. Çoklu Dil Desteği:")
    
    turkce = Dil("tr")
    ingilizce = Dil("en")
    almanca = Dil("de")
    
    print(f"Türkçe: {turkce.cevir('merhaba')}")
    print(f"İngilizce: {ingilizce.cevir('merhaba')}")
    print(f"Almanca: {almanca.cevir('merhaba')}")
    
    turkce_2 = Dil("tr")
    print(f"\nturkce == turkce_2: {turkce == turkce_2}")  # True
    print(f"Desteklenen diller: {Dil.desteklenen_diller()}")
