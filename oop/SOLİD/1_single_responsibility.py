"""
SOLID - S: Single Responsibility Principle (SRP)
=================================================
Tek Sorumluluk Prensibi

TANIM:
------
Bir sınıf yalnızca BİR sorumluluğa sahip olmalı ve değişmek için 
yalnızca BİR nedeni olmalıdır.

NEDEN ÖNEMLİ?
-------------
- Kod daha okunabilir ve anlaşılır olur
- Test etmesi kolay olur
- Bakımı ve değişikliği kolay olur
- Hatalar izole edilir, bir değişiklik diğerlerini etkilemez

KURAL:
------
"Bir sınıf, yalnızca bir aktör için sorumlu olmalıdır"
- Uncle Bob (Robert C. Martin)
"""

# ==========================================
# ❌ YANLIŞ ÖRNEK - SRP İhlali
# ==========================================

class KullaniciYoneticiKotu:
    """
    Bu sınıf SRP'yi ihlal ediyor!
    Birden fazla sorumluluğu var:
    1. Kullanıcı verisi yönetimi
    2. Veritabanı işlemleri
    3. E-posta gönderimi
    4. Loglama
    """
    
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email
    
    def kullanici_kaydet(self):
        # Veritabanı işlemi - Bu ayrı bir sınıf olmalı!
        print(f"Veritabanına kaydediliyor: {self.ad}")
        # Burada SQL sorguları olurdu...
    
    def email_gonder(self, mesaj):
        # E-posta işlemi - Bu ayrı bir sınıf olmalı!
        print(f"{self.email} adresine gönderiliyor: {mesaj}")
        # SMTP bağlantısı ve e-posta gönderimi...
    
    def log_yaz(self, eylem):
        # Loglama işlemi - Bu ayrı bir sınıf olmalı!
        print(f"[LOG] Kullanıcı {self.ad}: {eylem}")
        # Dosyaya veya log servisine yazma...
    
    def sifre_dogrula(self, sifre):
        # Doğrulama işlemi - Bu ayrı bir sınıf olmalı!
        return len(sifre) >= 8


# ==========================================
# ✅ DOĞRU ÖRNEK - SRP Uygulanmış
# ==========================================

class Kullanici:
    """Sadece kullanıcı verisini tutar - TEK SORUMLULUK"""
    
    def __init__(self, ad: str, email: str):
        self.ad = ad
        self.email = email
    
    def __str__(self):
        return f"Kullanıcı: {self.ad} ({self.email})"


class KullaniciRepository:
    """Sadece veritabanı işlemlerinden sorumlu - TEK SORUMLULUK"""
    
    def __init__(self):
        self._veritabani = []  # Simülasyon
    
    def kaydet(self, kullanici: Kullanici) -> bool:
        self._veritabani.append(kullanici)
        print(f"✓ Veritabanına kaydedildi: {kullanici.ad}")
        return True
    
    def bul(self, email: str) -> Kullanici | None:
        for k in self._veritabani:
            if k.email == email:
                return k
        return None
    
    def sil(self, email: str) -> bool:
        kullanici = self.bul(email)
        if kullanici:
            self._veritabani.remove(kullanici)
            return True
        return False


class EmailServisi:
    """Sadece e-posta gönderiminden sorumlu - TEK SORUMLULUK"""
    
    def __init__(self, smtp_server: str = "smtp.example.com"):
        self.smtp_server = smtp_server
    
    def gonder(self, alici: str, konu: str, mesaj: str) -> bool:
        print(f"✉ E-posta gönderildi: {alici}")
        print(f"  Konu: {konu}")
        print(f"  Mesaj: {mesaj}")
        return True
    
    def hosgeldin_emaili_gonder(self, kullanici: Kullanici):
        return self.gonder(
            kullanici.email,
            "Hoş Geldiniz!",
            f"Merhaba {kullanici.ad}, aramıza hoş geldiniz!"
        )


class Logger:
    """Sadece loglama işlemlerinden sorumlu - TEK SORUMLULUK"""
    
    def __init__(self, dosya_adi: str = "app.log"):
        self.dosya_adi = dosya_adi
        self._loglar = []
    
    def info(self, mesaj: str):
        log = f"[INFO] {mesaj}"
        self._loglar.append(log)
        print(log)
    
    def hata(self, mesaj: str):
        log = f"[ERROR] {mesaj}"
        self._loglar.append(log)
        print(log)
    
    def uyari(self, mesaj: str):
        log = f"[WARNING] {mesaj}"
        self._loglar.append(log)
        print(log)


class SifreDogrulayici:
    """Sadece şifre doğrulamadan sorumlu - TEK SORUMLULUK"""
    
    def __init__(self, min_uzunluk: int = 8):
        self.min_uzunluk = min_uzunluk
    
    def dogrula(self, sifre: str) -> tuple[bool, str]:
        if len(sifre) < self.min_uzunluk:
            return False, f"Şifre en az {self.min_uzunluk} karakter olmalı"
        if not any(c.isupper() for c in sifre):
            return False, "Şifre en az bir büyük harf içermeli"
        if not any(c.isdigit() for c in sifre):
            return False, "Şifre en az bir rakam içermeli"
        return True, "Şifre geçerli"


class KullaniciServisi:
    """
    Servisler arasında koordinasyon sağlar.
    Her servis kendi sorumluluğuna sahip.
    """
    
    def __init__(self):
        self.repository = KullaniciRepository()
        self.email_servisi = EmailServisi()
        self.logger = Logger()
        self.sifre_dogrulayici = SifreDogrulayici()
    
    def kayit_ol(self, ad: str, email: str, sifre: str) -> bool:
        # Şifre doğrulama
        gecerli, mesaj = self.sifre_dogrulayici.dogrula(sifre)
        if not gecerli:
            self.logger.uyari(f"Kayıt başarısız - {mesaj}")
            return False
        
        # Kullanıcı oluştur ve kaydet
        kullanici = Kullanici(ad, email)
        self.repository.kaydet(kullanici)
        
        # Hoşgeldin e-postası gönder
        self.email_servisi.hosgeldin_emaili_gonder(kullanici)
        
        # Logla
        self.logger.info(f"Yeni kullanıcı kaydı: {ad}")
        
        return True


# ==========================================
# KULLANIM ÖRNEĞİ
# ==========================================

if __name__ == "__main__":
    print("=" * 55)
    print("SINGLE RESPONSIBILITY PRINCIPLE (SRP)")
    print("=" * 55)
    
    print("\n✅ DOĞRU UYGULAMA:")
    print("-" * 35)
    
    servis = KullaniciServisi()
    
    # Zayıf şifre ile deneme
    print("\n[Test 1: Zayıf şifre]")
    servis.kayit_ol("Ahmet", "ahmet@email.com", "123")
    
    # Güçlü şifre ile kayıt
    print("\n[Test 2: Güçlü şifre]")
    servis.kayit_ol("Ayşe", "ayse@email.com", "Guclu123")
    
    print("\n" + "=" * 55)
    print("ÖZET:")
    print("-" * 35)
    print("""
Her sınıf TEK bir iş yapıyor:
  • Kullanici        → Veri tutma
  • KullaniciRepository → Veritabanı işlemleri  
  • EmailServisi     → E-posta gönderimi
  • Logger           → Loglama
  • SifreDogrulayici → Şifre doğrulama
  • KullaniciServisi → Koordinasyon
    """)
