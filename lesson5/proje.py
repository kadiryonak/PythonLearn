import os
import time
import random
import datetime as dt
from typing import List, Dict, Optional

# ==================== PROJE 1: ŞANS OYUNU SİMÜLATÖRÜ ====================
class SansOyunu:
    """
    Random modülü kullanarak çeşitli şans oyunları simülasyonu
    Loto, tombala, kumanda gibi oyunlar
    """
    def __init__(self):
        self.bakiye = 1000
        self.oyun_gecmisi = []
        
    def loto_oyna(self, bahis: int = 10) -> bool:
        """6/49 loto oyunu - kullanıcı 6 sayı seçer, sistem 6 sayı çeker"""
        if self.bakiye < bahis:
            print("Yetersiz bakiye!")
            return False
            
        print("\nLOTO OYUNU BAŞLIYOR!")
        print(f"Bahis: {bahis} TL | Kalan Bakiye: {self.bakiye - bahis} TL")
        
        # Kullanıcıdan sayılar al
        print("\n1-49 arasından 6 sayı seçin:")
        kullanici_sayilari = random.sample(range(1, 50), 6)
        kullanici_sayilari.sort()
        print(f"Seçtiğiniz sayılar: {kullanici_sayilari}")
        
        # Sistem sayıları çek
        print("\nSayılar çekiliyor...")
        time.sleep(1)
        sistem_sayilari = random.sample(range(1, 50), 6)
        sistem_sayilari.sort()
        print(f"Çekilen sayılar: {sistem_sayilari}")
        
        # Eşleşme kontrolü
        eslesen = set(kullanici_sayilari) & set(sistem_sayilari)
        eslesen_sayisi = len(eslesen)
        
        print(f"\nEşleşen sayılar ({eslesen_sayisi} adet): {sorted(eslesen) if eslesen else 'Yok'}")
        
        # Ödül hesaplama
        odul = 0
        if eslesen_sayisi == 6:
            odul = bahis * 1000
            print(f"BÜYÜK İKRAMİYE! +{odul} TL")
        elif eslesen_sayisi == 5:
            odul = bahis * 100
            print(f"5 Bildiniz! +{odul} TL")
        elif eslesen_sayisi == 4:
            odul = bahis * 10
            print(f"4 Bildiniz! +{odul} TL")
        elif eslesen_sayisi == 3:
            odul = bahis * 2
            print(f"3 Bildiniz! +{odul} TL")
        else:
            print(f"Kaybettiniz! -{bahis} TL")
            
        self.bakiye = self.bakiye - bahis + odul
        self.oyun_gecmisi.append({
            'oyun': 'Loto',
            'bahis': bahis,
            'kazanc': odul - bahis,
            'tarih': dt.datetime.now()
        })
        
        print(f"\nGüncel Bakiye: {self.bakiye} TL")
        return odul > bahis
    
    def zar_oyunu(self, bahis: int = 50) -> bool:
        """İki zar atılır, toplam 7 veya 11 gelirse kazanırsınız"""
        if self.bakiye < bahis:
            print("Yetersiz bakiye!")
            return False
            
        print("\nZAR OYUNU!")
        print(f"Bahis: {bahis} TL")
        print("Kural: İki zar toplamı 7 veya 11 ise 3x kazanırsınız!")
        
        time.sleep(1)
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        toplam = zar1 + zar2
        
        print(f"\nZar 1: {zar1}")
        print(f"Zar 2: {zar2}")
        print(f"Toplam: {toplam}")
        
        if toplam == 7 or toplam == 11:
            kazanc = bahis * 3
            print(f"\nKAZANDINIZ! +{kazanc} TL")
            self.bakiye += kazanc - bahis
            sonuc = True
        else:
            print(f"\nKaybettiniz! -{bahis} TL")
            self.bakiye -= bahis
            sonuc = False
            
        self.oyun_gecmisi.append({
            'oyun': 'Zar',
            'bahis': bahis,
            'kazanc': (kazanc - bahis) if sonuc else -bahis,
            'tarih': dt.datetime.now()
        })
        
        print(f"Güncel Bakiye: {self.bakiye} TL")
        return sonuc
    
    def cark_cevir(self) -> None:
        """Çarkıfelek oyunu - farklı ödüller kazanma şansı"""
        print("\nÇARKIFELEK!")
        
        oduller = [
            ("100 TL", 100),
            ("50 TL", 50),
            ("25 TL", 25),
            ("Bedava Tur", 0),
            ("Hiç", 0),
            ("200 TL", 200),
            ("Hiç", 0),
            ("75 TL", 75)
        ]
        
        print("Çark dönüyor...")
        for _ in range(20):
            print(random.choice(oduller)[0], end="\r")
            time.sleep(0.1)
        
        kazanilan = random.choice(oduller)
        print(f"\n\nSonuç: {kazanilan[0]}")
        
        self.bakiye += kazanilan[1]
        self.oyun_gecmisi.append({
            'oyun': 'Çarkıfelek',
            'bahis': 0,
            'kazanc': kazanilan[1],
            'tarih': dt.datetime.now()
        })
        
        print(f"Güncel Bakiye: {self.bakiye} TL")
    
    def gecmis_goster(self) -> None:
        """Oyun geçmişini gösterir"""
        print("\nOYUN GEÇMİŞİ")
        
        toplam_kazanc = 0
        for i, oyun in enumerate(self.oyun_gecmisi[-10:], 1):
            tarih = oyun['tarih'].strftime("%d.%m.%Y %H:%M")
            kazanc_str = f"+{oyun['kazanc']}" if oyun['kazanc'] > 0 else str(oyun['kazanc'])
            print(f"{i}. {oyun['oyun']:<12} | {tarih} | {kazanc_str:>8} TL")
            toplam_kazanc += oyun['kazanc']
        
        print(f"Toplam Kar/Zarar: {'+' if toplam_kazanc > 0 else ''}{toplam_kazanc} TL")
        print(f"Mevcut Bakiye: {self.bakiye} TL")


# ==================== PROJE 2: ÇALIŞAN YÖNETİM SİSTEMİ ====================
class CalisanYonetimi:
    """
    Datetime modülü ile çalışan kayıt, maaş, izin, mesai takip sistemi
    """
    def __init__(self):
        self.calisanlar: Dict[int, Dict] = {}
        self.calisan_id_sayac = 1
        
    def calisan_ekle(self, ad: str, soyad: str, pozisyon: str, maas: float) -> None:
        """Yeni çalışan ekler"""
        ise_giris = dt.datetime.now()
        
        self.calisanlar[self.calisan_id_sayac] = {
            'ad': ad,
            'soyad': soyad,
            'pozisyon': pozisyon,
            'maas': maas,
            'ise_giris': ise_giris,
            'izinler': [],
            'mesailer': []
        }
        
        print(f"\nÇalışan eklendi: {ad} {soyad} (ID: {self.calisan_id_sayac})")
        print(f"   Pozisyon: {pozisyon}")
        print(f"   Maaş: {maas} TL")
        print(f"   İşe Giriş: {ise_giris.strftime('%d.%m.%Y')}")
        
        self.calisan_id_sayac += 1
    
    def izin_ekle(self, calisan_id: int, baslangic: str, bitis: str, tur: str) -> None:
        """Çalışana izin ekler (format: DD.MM.YYYY)"""
        if calisan_id not in self.calisanlar:
            print("Çalışan bulunamadı!")
            return
        
        baslangic_tarih = dt.datetime.strptime(baslangic, "%d.%m.%Y")
        bitis_tarih = dt.datetime.strptime(bitis, "%d.%m.%Y")
        gun_sayisi = (bitis_tarih - baslangic_tarih).days + 1
        
        izin = {
            'baslangic': baslangic_tarih,
            'bitis': bitis_tarih,
            'gun_sayisi': gun_sayisi,
            'tur': tur
        }
        
        self.calisanlar[calisan_id]['izinler'].append(izin)
        
        calisan = self.calisanlar[calisan_id]
        print(f"\nİzin eklendi: {calisan['ad']} {calisan['soyad']}")
        print(f"   Tarih: {baslangic} - {bitis}")
        print(f"   Gün Sayısı: {gun_sayisi}")
        print(f"   İzin Türü: {tur}")
    
    def mesai_ekle(self, calisan_id: int, tarih: str, saat: float) -> None:
        """Çalışana mesai ekler"""
        if calisan_id not in self.calisanlar:
            print("Çalışan bulunamadı!")
            return
        
        mesai_tarihi = dt.datetime.strptime(tarih, "%d.%m.%Y")
        mesai_ucreti = saat * 50  # Saat başı 50 TL
        
        mesai = {
            'tarih': mesai_tarihi,
            'saat': saat,
            'ucret': mesai_ucreti
        }
        
        self.calisanlar[calisan_id]['mesailer'].append(mesai)
        
        calisan = self.calisanlar[calisan_id]
        print(f"\nMesai eklendi: {calisan['ad']} {calisan['soyad']}")
        print(f"   Tarih: {tarih}")
        print(f"   Saat: {saat}")
        print(f"   Ücret: {mesai_ucreti} TL")
    
    def calisan_raporu(self, calisan_id: int) -> None:
        """Çalışan detaylı rapor"""
        if calisan_id not in self.calisanlar:
            print("Çalışan bulunamadı!")
            return
        
        calisan = self.calisanlar[calisan_id]
        bugun = dt.datetime.now()
        
        # Çalışma süresi
        calisma_suresi = bugun - calisan['ise_giris']
        yil = calisma_suresi.days // 365
        ay = (calisma_suresi.days % 365) // 30
        
        # İzin istatistikleri
        toplam_izin = sum(izin['gun_sayisi'] for izin in calisan['izinler'])
        
        # Mesai istatistikleri
        toplam_mesai_saat = sum(mesai['saat'] for mesai in calisan['mesailer'])
        toplam_mesai_ucret = sum(mesai['ucret'] for mesai in calisan['mesailer'])
        
        print(f"\nÇALIŞAN RAPORU - {calisan['ad']} {calisan['soyad']} (ID: {calisan_id})")
        print(f"Pozisyon: {calisan['pozisyon']}")
        print(f"Maaş: {calisan['maas']} TL")
        print(f"İşe Giriş: {calisan['ise_giris'].strftime('%d.%m.%Y')}")
        print(f"Çalışma Süresi: {yil} yıl {ay} ay")
        print(f"\nİSTATİSTİKLER:")
        print(f"  - Toplam İzin: {toplam_izin} gün")
        print(f"  - Toplam Mesai: {toplam_mesai_saat} saat")
        print(f"  - Mesai Ücreti: {toplam_mesai_ucret} TL")
        print(f"  - Toplam Gelir: {calisan['maas'] + toplam_mesai_ucret} TL")
        
        # Son izinler
        if calisan['izinler']:
            print(f"\nSON İZİNLER:")
            for izin in calisan['izinler'][-5:]:
                print(f"  - {izin['baslangic'].strftime('%d.%m.%Y')} - "
                      f"{izin['bitis'].strftime('%d.%m.%Y')} | "
                      f"{izin['gun_sayisi']} gün | {izin['tur']}")
    
    def tum_calisanlar_listesi(self) -> None:
        """Tüm çalışanları listeler"""
        print(f"\nTÜM ÇALIŞANLAR LİSTESİ")
        print(f"{'ID':<5} {'Ad Soyad':<25} {'Pozisyon':<20} {'Maaş':<15} {'İşe Giriş'}")
        print(f"{'-' * 80}")
        
        for calisan_id, calisan in self.calisanlar.items():
            ad_soyad = f"{calisan['ad']} {calisan['soyad']}"
            ise_giris = calisan['ise_giris'].strftime('%d.%m.%Y')
            print(f"{calisan_id:<5} {ad_soyad:<25} {calisan['pozisyon']:<20} "
                  f"{calisan['maas']:<15} {ise_giris}")


# ==================== PROJE 3: DOSYA YÖNETİM SİSTEMİ ====================
class DosyaYoneticisi:
    """
    OS modülü ile dosya/klasör yönetimi, arama, düzenleme
    """
    def __init__(self, ana_dizin: str = "."):
        self.ana_dizin = os.path.abspath(ana_dizin)
        print(f"Dosya Yöneticisi başlatıldı: {self.ana_dizin}")
    
    def dizin_agaci_goster(self, dizin: str = None, max_derinlik: int = 3) -> None:
        """Dizin ağacını gösterir"""
        if dizin is None:
            dizin = self.ana_dizin
        
        print(f"\nDİZİN AĞACI: {dizin}")
        
        for kok, klasorler, dosyalar in os.walk(dizin):
            seviye = kok.replace(dizin, '').count(os.sep)
            
            if seviye >= max_derinlik:
                klasorler[:] = []  # Alt klasörlere girme
                continue
            
            girinti = '  ' * seviye
            klasor_adi = os.path.basename(kok) or kok
            print(f"{girinti}[KLASOR] {klasor_adi}/")
            
            alt_girinti = '  ' * (seviye + 1)
            for dosya in dosyalar:
                dosya_yolu = os.path.join(kok, dosya)
                boyut = os.path.getsize(dosya_yolu)
                boyut_str = self._boyut_formatla(boyut)
                print(f"{alt_girinti}[DOSYA] {dosya} ({boyut_str})")
    
    def dosya_ara(self, arama_metni: str, uzanti: str = None) -> List[str]:
        """Belirli isme veya uzantıya sahip dosyaları arar"""
        print(f"\nArama: '{arama_metni}'" + (f" | Uzantı: {uzanti}" if uzanti else ""))
        bulunan_dosyalar = []
        
        for kok, _, dosyalar in os.walk(self.ana_dizin):
            for dosya in dosyalar:
                # Uzantı kontrolü
                if uzanti and not dosya.endswith(uzanti):
                    continue
                
                # İsim kontrolü
                if arama_metni.lower() in dosya.lower():
                    dosya_yolu = os.path.join(kok, dosya)
                    bulunan_dosyalar.append(dosya_yolu)
        
        if bulunan_dosyalar:
            print(f"{len(bulunan_dosyalar)} dosya bulundu:")
            for i, dosya in enumerate(bulunan_dosyalar, 1):
                boyut = os.path.getsize(dosya)
                print(f"{i}. {dosya} ({self._boyut_formatla(boyut)})")
        else:
            print("Hiç dosya bulunamadı!")
        
        return bulunan_dosyalar
    
    def buyuk_dosyalari_bul(self, min_boyut_mb: float = 1.0) -> List[tuple]:
        """Belirli boyuttan büyük dosyaları bulur"""
        print(f"\n{min_boyut_mb} MB'dan büyük dosyalar aranıyor...")
        buyuk_dosyalar = []
        min_boyut_byte = min_boyut_mb * 1024 * 1024
        
        for kok, _, dosyalar in os.walk(self.ana_dizin):
            for dosya in dosyalar:
                dosya_yolu = os.path.join(kok, dosya)
                try:
                    boyut = os.path.getsize(dosya_yolu)
                    if boyut >= min_boyut_byte:
                        buyuk_dosyalar.append((dosya_yolu, boyut))
                except:
                    continue
        
        # Boyuta göre sırala
        buyuk_dosyalar.sort(key=lambda x: x[1], reverse=True)
        
        if buyuk_dosyalar:
            print(f"{len(buyuk_dosyalar)} büyük dosya bulundu:")
            for i, (dosya, boyut) in enumerate(buyuk_dosyalar[:10], 1):
                print(f"{i}. {dosya}")
                print(f"   Boyut: {self._boyut_formatla(boyut)}")
        else:
            print("Büyük dosya bulunamadı!")
        
        return buyuk_dosyalar
    
    def dosya_uzanti_istatistikleri(self) -> Dict[str, int]:
        """Dizindeki dosya uzantılarının istatistiklerini gösterir"""
        print("\nDOSYA UZANTI İSTATİSTİKLERİ")
        uzanti_sayilari = {}
        
        for kok, _, dosyalar in os.walk(self.ana_dizin):
            for dosya in dosyalar:
                _, uzanti = os.path.splitext(dosya)
                uzanti = uzanti.lower() if uzanti else 'uzantısız'
                uzanti_sayilari[uzanti] = uzanti_sayilari.get(uzanti, 0) + 1
        
        # Sırala
        sirali_uzantilar = sorted(uzanti_sayilari.items(), key=lambda x: x[1], reverse=True)
        
        toplam = sum(uzanti_sayilari.values())
        print(f"Toplam dosya: {toplam}")
        
        for uzanti, sayi in sirali_uzantilar:
            yuzde = (sayi / toplam) * 100
            bar = '#' * int(yuzde / 2)
            print(f"{uzanti:<15} {sayi:>5} adet {bar} {yuzde:.1f}%")
        
        return uzanti_sayilari
    
    def yedekle(self, hedef_dizin: str) -> None:
        """Belirli dosyaları yedekler"""
        print(f"\nYedekleme başlıyor...")
        
        if not os.path.exists(hedef_dizin):
            os.makedirs(hedef_dizin)
            print(f"Hedef dizin oluşturuldu: {hedef_dizin}")
        
        yedeklenen = 0
        for kok, _, dosyalar in os.walk(self.ana_dizin):
            for dosya in dosyalar:
                if dosya.endswith(('.py', '.txt', '.md')):  # Sadece belirli dosyalar
                    kaynak = os.path.join(kok, dosya)
                    hedef = os.path.join(hedef_dizin, dosya)
                    
                    try:
                        with open(kaynak, 'r', encoding='utf-8') as f:
                            icerik = f.read()
                        with open(hedef, 'w', encoding='utf-8') as f:
                            f.write(icerik)
                        yedeklenen += 1
                        print(f"Yedeklendi: {dosya}")
                    except:
                        print(f"Hata: {dosya}")
        
        print(f"\nToplam {yedeklenen} dosya yedeklendi!")
    
    def _boyut_formatla(self, boyut: int) -> str:
        """Byte'ı okunabilir formata çevirir"""
        for birim in ['B', 'KB', 'MB', 'GB']:
            if boyut < 1024.0:
                return f"{boyut:.1f} {birim}"
            boyut /= 1024.0
        return f"{boyut:.1f} TB"


# ==================== PROJE 4: PERFORMANS İZLEYİCİ ====================
class PerformansIzleyici:
    """
    Time modülü ile kod performans ölçümü ve karşılaştırma
    """
    def __init__(self):
        self.olcumler = []
    
    def olcum_yap(self, fonksiyon, *args, **kwargs):
        """Bir fonksiyonun çalışma süresini ölçer"""
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        
        sure = bitis - baslangic
        
        self.olcumler.append({
            'fonksiyon': fonksiyon.__name__,
            'sure': sure,
            'tarih': dt.datetime.now()
        })
        
        return sonuc, sure
    
    def liste_performans_testi(self):
        """Farklı liste oluşturma yöntemlerinin performansını karşılaştırır"""
        print("\nLİSTE PERFORMANS TESTİ")
        
        n = 1000000
        
        # Yöntem 1: append
        def append_yontemi():
            liste = []
            for i in range(n):
                liste.append(i)
            return liste
        
        # Yöntem 2: list comprehension
        def comprehension_yontemi():
            return [i for i in range(n)]
        
        # Yöntem 3: range to list
        def range_yontemi():
            return list(range(n))
        
        print(f"Test: {n:,} elemanlı liste oluşturma\n")
        
        # Test 1
        print("1. Append yöntemi...")
        _, sure1 = self.olcum_yap(append_yontemi)
        print(f"   Süre: {sure1:.4f} saniye")
        
        # Test 2
        print("2. List comprehension...")
        _, sure2 = self.olcum_yap(comprehension_yontemi)
        print(f"   Süre: {sure2:.4f} saniye")
        
        # Test 3
        print("3. Range to list...")
        _, sure3 = self.olcum_yap(range_yontemi)
        print(f"   Süre: {sure3:.4f} saniye")
        
        # Karşılaştırma
        print("\nSONUÇLAR:")
        sonuclar = [
            ("Append", sure1),
            ("List Comprehension", sure2),
            ("Range to List", sure3)
        ]
        sonuclar.sort(key=lambda x: x[1])
        
        en_hizli = sonuclar[0][1]
        for i, (yontem, sure) in enumerate(sonuclar, 1):
            kat = sure / en_hizli
            print(f"{i}. {yontem:<20} {sure:.4f}s (Referansa göre {kat:.2f}x)")
    
    def arama_performans_testi(self):
        """Farklı arama yöntemlerinin performansını karşılaştırır"""
        print("\nARAMA PERFORMANS TESTİ")
        
        # Test verisi
        liste = list(range(100000))
        set_veri = set(liste)
        dict_veri = {i: i for i in liste}
        
        aranan = 99999
        
        print(f"Test: {len(liste):,} eleman içinde {aranan} aramak\n")
        
        # Liste aramasi
        print("1. Liste içinde arama (in operatörü)...")
        baslangic = time.perf_counter()
        sonuc = aranan in liste
        bitis = time.perf_counter()
        sure1 = bitis - baslangic
        print(f"   Süre: {sure1:.6f} saniye")
        
        # Set araması
        print("2. Set içinde arama...")
        baslangic = time.perf_counter()
        sonuc = aranan in set_veri
        bitis = time.perf_counter()
        sure2 = bitis - baslangic
        print(f"   Süre: {sure2:.6f} saniye")
        
        # Dict araması
        print("3. Dictionary içinde arama...")
        baslangic = time.perf_counter()
        sonuc = aranan in dict_veri
        bitis = time.perf_counter()
        sure3 = bitis - baslangic
        print(f"   Süre: {sure3:.6f} saniye")
        
        print("\nSONUÇ:")
        print(f"Set/Dict, listeden yaklaşık {sure1/sure2:.0f}x daha hızlı!")
    
    def rapor_goster(self):
        """Tüm ölçümlerin raporunu gösterir"""
        if not self.olcumler:
            print("Henüz ölçüm yapılmamış!")
            return
        
        print("\nPERFORMANS RAPORU")
        
        for olcum in self.olcumler:
            tarih = olcum['tarih'].strftime("%d.%m.%Y %H:%M:%S")
            print(f"- {olcum['fonksiyon']:<30} {olcum['sure']:.6f}s | {tarih}")


# ==================== ANA PROGRAM ====================
def main():
    while True:
        print("\nPYTHON MODÜL PROJELERİ")
        print("1. Şans Oyunu Simülatörü (Random)")
        print("2. Çalışan Yönetim Sistemi (Datetime)")
        print("3. Dosya Yönetim Sistemi (OS)")
        print("4. Performans İzleyici (Time)")
        print("0. Çıkış")
        
        secim = input("\nSeçiminiz (0-4): ").strip()
        
        if secim == "1":
            sans_oyunu_menu()
        elif secim == "2":
            calisan_yonetim_menu()
        elif secim == "3":
            dosya_yonetim_menu()
        elif secim == "4":
            performans_menu()
        elif secim == "0":
            print("\nGörüşmek üzere!")
            break
        else:
            print("Geçersiz seçim!")


def sans_oyunu_menu():
    """Şans oyunu menüsü"""
    oyun = SansOyunu()
    
    while True:
        print(f"\nŞANS OYUNU | Bakiye: {oyun.bakiye} TL")
        print("1. Loto Oyna (10 TL)")
        print("2. Zar Oyunu (50 TL)")
        print("3. Çarkıfelek (Bedava)")
        print("4. Oyun Geçmişi")
        print("0. Ana Menü")
        
        secim = input("\nSeçim: ").strip()
        
        if secim == "1":
            oyun.loto_oyna()
        elif secim == "2":
            oyun.zar_oyunu()
        elif secim == "3":
            oyun.cark_cevir()
        elif secim == "4":
            oyun.gecmis_goster()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")
        
        if oyun.bakiye <= 0:
            print("\nBakiyeniz tükendi! Oyun bitti.")
            break


def calisan_yonetim_menu():
    """Çalışan yönetim menüsü"""
    yonetim = CalisanYonetimi()
    
    # Örnek çalışanlar ekle
    yonetim.calisan_ekle("Ahmet", "Yılmaz", "Yazılım Geliştirici", 15000)
    yonetim.calisan_ekle("Ayşe", "Demir", "Proje Yöneticisi", 20000)
    yonetim.calisan_ekle("Mehmet", "Kaya", "Sistem Yöneticisi", 18000)
    
    # Örnek izinler
    yonetim.izin_ekle(1, "15.12.2025", "20.12.2025", "Yıllık İzin")
    yonetim.mesai_ekle(1, "10.12.2025", 5)
    
    while True:
        print("\nÇALIŞAN YÖNETİM SİSTEMİ")
        print("1. Tüm Çalışanları Listele")
        print("2. Çalışan Raporu Göster")
        print("3. Yeni Çalışan Ekle")
        print("4. İzin Ekle")
        print("5. Mesai Ekle")
        print("0. Ana Menü")
        
        secim = input("\nSeçim: ").strip()
        
        if secim == "1":
            yonetim.tum_calisanlar_listesi()
        elif secim == "2":
            calisan_id = int(input("Çalışan ID: "))
            yonetim.calisan_raporu(calisan_id)
        elif secim == "3":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            pozisyon = input("Pozisyon: ")
            maas = float(input("Maaş: "))
            yonetim.calisan_ekle(ad, soyad, pozisyon, maas)
        elif secim == "4":
            calisan_id = int(input("Çalışan ID: "))
            baslangic = input("Başlangıç (GG.AA.YYYY): ")
            bitis = input("Bitiş (GG.AA.YYYY): ")
            tur = input("İzin Türü: ")
            yonetim.izin_ekle(calisan_id, baslangic, bitis, tur)
        elif secim == "5":
            calisan_id = int(input("Çalışan ID: "))
            tarih = input("Tarih (GG.AA.YYYY): ")
            saat = float(input("Mesai Saati: "))
            yonetim.mesai_ekle(calisan_id, tarih, saat)
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")


def dosya_yonetim_menu():
    """Dosya yönetim menüsü"""
    yonetici = DosyaYoneticisi()
    
    while True:
        print("\nDOSYA YÖNETİM SİSTEMİ")
        print("1. Dizin Ağacını Göster")
        print("2. Dosya Ara")
        print("3. Büyük Dosyaları Bul")
        print("4. Dosya Uzantı İstatistikleri")
        print("0. Ana Menü")
        
        secim = input("\nSeçim: ").strip()
        
        if secim == "1":
            yonetici.dizin_agaci_goster()
        elif secim == "2":
            arama = input("Aranacak kelime: ")
            uzanti = input("Uzantı (opsiyonel, örn: .py): ").strip() or None
            yonetici.dosya_ara(arama, uzanti)
        elif secim == "3":
            boyut = float(input("Minimum boyut (MB): "))
            yonetici.buyuk_dosyalari_bul(boyut)
        elif secim == "4":
            yonetici.dosya_uzanti_istatistikleri()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")


def performans_menu():
    """Performans izleyici menüsü"""
    izleyici = PerformansIzleyici()
    
    while True:
        print("\nPERFORMANS İZLEYİCİ")
        print("1. Liste Performans Testi")
        print("2. Arama Performans Testi")
        print("3. Performans Raporu")
        print("0. Ana Menü")
        
        secim = input("\nSeçim: ").strip()
        
        if secim == "1":
            izleyici.liste_performans_testi()
        elif secim == "2":
            izleyici.arama_performans_testi()
        elif secim == "3":
            izleyici.rapor_goster()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()