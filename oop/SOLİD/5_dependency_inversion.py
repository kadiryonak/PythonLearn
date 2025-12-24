"""
SOLID - D: Dependency Inversion Principle (DIP)
=================================================
Bağımlılık Tersine Çevirme Prensibi

TANIM:
------
1. Yüksek seviyeli modüller, düşük seviyeli modüllere 
   bağımlı olmamalı. İkisi de soyutlamalara bağımlı olmalı.
   
2. Soyutlamalar detaylara bağımlı olmamalı.
   Detaylar soyutlamalara bağımlı olmalı.

NEDEN ÖNEMLİ?
- Gevşek bağlılık (loose coupling)
- Test edilebilirlik (mock injection)
- Esneklik ve değiştirilebilirlik
"""

from abc import ABC, abstractmethod

# ==========================================
# ❌ YANLIŞ - Somut Bağımlılık
# ==========================================

class MySQLVeritabaniKotu:
    def baglan(self):
        print("MySQL'e bağlanıldı")
    
    def sorgu(self, sql: str):
        return f"MySQL sonuç: {sql}"


class KullaniciServisKotu:
    """Doğrudan MySQL'e bağımlı - DEĞİŞTİRİLEMEZ!"""
    
    def __init__(self):
        self.db = MySQLVeritabaniKotu()  # ❌ Somut sınıfa bağımlı
    
    def kullanici_getir(self, id: int):
        return self.db.sorgu(f"SELECT * FROM users WHERE id={id}")


# ==========================================
# ✅ DOĞRU - Soyutlamaya Bağımlılık
# ==========================================

class Veritabani(ABC):
    """Soyut veritabanı arayüzü"""
    
    @abstractmethod
    def baglan(self): pass
    
    @abstractmethod
    def sorgu(self, sql: str) -> str: pass


class MySQLVeritabani(Veritabani):
    def baglan(self):
        print("🐬 MySQL'e bağlanıldı")
    
    def sorgu(self, sql: str) -> str:
        return f"[MySQL] {sql}"


class PostgreSQLVeritabani(Veritabani):
    def baglan(self):
        print("🐘 PostgreSQL'e bağlanıldı")
    
    def sorgu(self, sql: str) -> str:
        return f"[PostgreSQL] {sql}"


class SQLiteVeritabani(Veritabani):
    def baglan(self):
        print("📦 SQLite'a bağlanıldı")
    
    def sorgu(self, sql: str) -> str:
        return f"[SQLite] {sql}"


class KullaniciServis:
    """Soyut Veritabani'na bağımlı - HERHANGİ biri olabilir!"""
    
    def __init__(self, veritabani: Veritabani):  # ✅ Dependency Injection
        self.db = veritabani
        self.db.baglan()
    
    def kullanici_getir(self, id: int):
        return self.db.sorgu(f"SELECT * FROM users WHERE id={id}")


# ==========================================
# BONUS: Bildirim Örneği
# ==========================================

class BildirimServisi(ABC):
    @abstractmethod
    def gonder(self, mesaj: str, alici: str): pass


class EmailBildirim(BildirimServisi):
    def gonder(self, mesaj: str, alici: str):
        print(f"📧 Email → {alici}: {mesaj}")


class SMSBildirim(BildirimServisi):
    def gonder(self, mesaj: str, alici: str):
        print(f"📱 SMS → {alici}: {mesaj}")


class PushBildirim(BildirimServisi):
    def gonder(self, mesaj: str, alici: str):
        print(f"🔔 Push → {alici}: {mesaj}")


class SiparisServis:
    """Herhangi bir bildirim servisiyle çalışır"""
    
    def __init__(self, bildirim: BildirimServisi):
        self.bildirim = bildirim
    
    def siparis_olustur(self, urun: str, musteri: str):
        print(f"✅ Sipariş oluşturuldu: {urun}")
        self.bildirim.gonder(f"Siparişiniz alındı: {urun}", musteri)


if __name__ == "__main__":
    print("=" * 50)
    print("DEPENDENCY INVERSION PRINCIPLE")
    print("=" * 50)
    
    print("\n✅ Veritabanı Örneği:")
    print("-" * 30)
    
    # Aynı servis, farklı veritabanları
    mysql_servis = KullaniciServis(MySQLVeritabani())
    print(mysql_servis.kullanici_getir(1))
    
    postgres_servis = KullaniciServis(PostgreSQLVeritabani())
    print(postgres_servis.kullanici_getir(2))
    
    print("\n✅ Bildirim Örneği:")
    print("-" * 30)
    
    # Aynı servis, farklı bildirim yöntemleri
    email_siparis = SiparisServis(EmailBildirim())
    email_siparis.siparis_olustur("Laptop", "ahmet@mail.com")
    
    sms_siparis = SiparisServis(SMSBildirim())
    sms_siparis.siparis_olustur("Telefon", "+90 555 123")
    
    print("\n" + "=" * 50)
    print("ÖZET: Somut sınıflara değil, arayüzlere bağımlı ol!")
