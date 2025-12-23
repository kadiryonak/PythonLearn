import os
import time
import random
import datetime as dt   
 
class RandomModul:
    """Random modülü ile ilgili metodları içerir"""
    def __init__(self, names: list[str]):
        self.names = names
        print("Random modülü constructor çalıştı")
        
    def randrange_ornegi(self):
        """random.randrange(start, stop, step) - Belirtilen aralıkta ve adımda rastgele sayı üretir"""
        for i in range(10):
            print(random.randrange(1, 10, 3))  # 1'den 10'a kadar 3'er 3'er artarak (1,4,7)
    
    def random_ornegi(self):
        """random.random() - 0 ile 1 arasında rastgele ondalıklı sayı üretir"""
        for i in range(10):
            print(random.random())
    
    def randint_ornegi(self):
        """random.randint(a, b) - a ile b arasında (ikisi de dahil) rastgele tam sayı üretir"""
        for i in range(10):
            print(random.randint(1, 50))
    
    def uniform_ornegi(self):
        """random.uniform(a, b) - a ile b arasında rastgele ondalıklı sayı üretir"""
        for i in range(10):
            print(random.uniform(1.5, 10.5))
    
    def shuffle_ornegi(self):
        """random.shuffle(list) - Listeyi karıştırır (orijinal listeyi değiştirir)"""
        random.shuffle(self.names)
        print(self.names)
    
    def choice_ornegi(self):
        """random.choice(sequence) - Diziden rastgele bir eleman seçer"""
        for _ in range(10):
            print(random.choice(self.names))
    
    def choices_ornegi(self):
        """random.choices(sequence, k=n) - Diziden n adet rastgele eleman seçer (tekrar edebilir)"""
        print(random.choices(self.names, k=5))
    
    def sample_ornegi(self):
        """random.sample(sequence, k) - Diziden k adet rastgele eleman seçer (tekrar etmez)"""
        for _ in range(5):
            print(random.sample(self.names, 2))
    
    def seed_ornegi(self):
        """random.seed(a) - Rastgele sayı üretecini başlatır, aynı seed aynı sonuçları verir"""
        random.seed(42)
        print(random.random())  # Her zaman aynı sonucu verir


class TimeModul:
    """Time modülü ile ilgili metodları içerir"""
    def __init__(self):
        print("Time modülü constructor çalıştı")
    
    def time_ornegi(self):
        """time.time() - 1 Ocak 1970'ten bu yana geçen saniyeyi döndürür (epoch time)"""
        print(f"Şu anki zaman (epoch): {time.time()}")
    
    def ctime_ornegi(self):
        """time.ctime() - Mevcut zamanı okunabilir string formatında döndürür"""
        print(f"Okunabilir zaman: {time.ctime()}")
    
    def sleep_ornegi(self):
        """time.sleep(seconds) - Programı belirtilen saniye kadar durdurur"""
        print("3 saniye bekleniyor...")
        time.sleep(3)
        print("Bekleme bitti!")
    
    def localtime_ornegi(self):
        """time.localtime() - Yerel zamanı struct_time objesi olarak döndürür"""
        yerel_zaman = time.localtime()
        print(f"Yıl: {yerel_zaman.tm_year}, Ay: {yerel_zaman.tm_mon}, Gün: {yerel_zaman.tm_mday}")
    
    def strftime_ornegi(self):
        """time.strftime(format) - Zamanı belirtilen formatta string'e çevirir"""
        zaman = time.localtime()
        print(time.strftime("%d/%m/%Y %H:%M:%S", zaman))
    
    def performans_olcumu(self):
        """time.time() kullanarak kod performansını ölçer"""
        baslangic = time.time()
        liste = []
        for i in range(10000000):
            liste.append(i)
        bitis = time.time()
        print(f"İşlem süresi: {bitis - baslangic:.2f} saniye")
    
    def perf_counter_ornegi(self):
        """time.perf_counter() - Yüksek çözünürlüklü performans sayacı (daha hassas)"""
        baslangic = time.perf_counter()
        time.sleep(0.5)
        bitis = time.perf_counter()
        print(f"Geçen süre: {bitis - baslangic:.6f} saniye")


class DatetimeModul:
    """Datetime modülü ile ilgili metodları içerir"""
    def __init__(self):
        print("Datetime modülü constructor çalıştı")
    
    def datetime_now_ornegi(self):
        """datetime.datetime.now() - Şu anki tarih ve saati döndürür"""
        simdi = dt.datetime.now()
        print(f"Şimdi: {simdi}")
    
    def date_ornegi(self):
        """datetime.date(year, month, day) - Sadece tarih objesi oluşturur"""
        tarih = dt.date(2025, 12, 22)
        print(f"Tarih: {tarih}")
    
    def time_ornegi(self):
        """datetime.time(hour, minute, second) - Sadece saat objesi oluşturur"""
        saat = dt.time(14, 30, 45)
        print(f"Saat: {saat}")
    
    def timedelta_ornegi(self):
        """datetime.timedelta() - Zaman farkı hesaplar"""
        simdi = dt.datetime.now()
        bir_hafta_sonra = simdi + dt.timedelta(days=7)
        iki_saat_once = simdi - dt.timedelta(hours=2)
        print(f"Bir hafta sonra: {bir_hafta_sonra}")
        print(f"İki saat önce: {iki_saat_once}")
    
    def strftime_ornegi(self):
        """strftime() - Datetime objesini formatlı string'e çevirir"""
        simdi = dt.datetime.now()
        print(simdi.strftime("%d.%m.%Y %H:%M:%S"))  # 22.12.2025 14:30:45
        print(simdi.strftime("%A, %d %B %Y"))  # Monday, 22 December 2025
    
    def strptime_ornegi(self):
        """datetime.strptime() - String'i datetime objesine çevirir"""
        tarih_str = "22/12/2025 14:30:00"
        tarih_obj = dt.datetime.strptime(tarih_str, "%d/%m/%Y %H:%M:%S")
        print(f"String'den datetime: {tarih_obj}")
    
    def tarih_farki_ornegi(self):
        """İki tarih arasındaki farkı hesaplar"""
        dogum_tarihi = dt.date(1990, 5, 15)
        bugun = dt.date.today()
        fark = bugun - dogum_tarihi
        print(f"Yaşadığınız gün sayısı: {fark.days}")


class OsModul:
    """OS modülü ile ilgili metodları içerir"""
    def __init__(self):
        print("OS modülü constructor çalıştı")
    
    def getcwd_ornegi(self):
        """os.getcwd() - Şu anki çalışma dizinini döndürür (Get Current Working Directory)"""
        print(f"Şu anki dizin: {os.getcwd()}")
    
    def chdir_ornegi(self):
        """os.chdir(path) - Çalışma dizinini değiştirir (Change Directory)"""
        eski_dizin = os.getcwd()
        print(f"Eski dizin: {eski_dizin}")
        # os.chdir(r"C:\Users\w\Desktop")
        # print(f"Yeni dizin: {os.getcwd()}")
        # os.chdir(eski_dizin)  # Geri dön
    
    def listdir_ornegi(self):
        """os.listdir(path) - Belirtilen dizindeki dosya ve klasörleri listeler"""
        print("Mevcut dizindeki dosyalar:")
        for item in os.listdir():
            print(f"  - {item}")
    
    def mkdir_ornegi(self):
        """os.mkdir(path) - Tek bir klasör oluşturur"""
        # os.mkdir("yeni_klasor")
        print("Klasör oluşturuldu (örnek)")
    
    def makedirs_ornegi(self):
        """os.makedirs(path) - İç içe klasörler oluşturur"""
        # os.makedirs("ana_klasor/alt_klasor/ic_klasor")
        print("İç içe klasörler oluşturuldu (örnek)")
    
    def rmdir_ornegi(self):
        """os.rmdir(path) - Boş bir klasörü siler"""
        # os.rmdir("yeni_klasor")
        print("Boş klasör silindi (örnek)")
    
    def removedirs_ornegi(self):
        """os.removedirs(path) - İç içe boş klasörleri siler"""
        # os.removedirs("ana_klasor/alt_klasor/ic_klasor")
        print("İç içe boş klasörler silindi (örnek)")
    
    def remove_ornegi(self):
        """os.remove(path) - Dosya siler"""
        # os.remove("silinecek_dosya.txt")
        print("Dosya silindi (örnek)")
    
    def rename_ornegi(self):
        """os.rename(old, new) - Dosya veya klasör adını değiştirir"""
        # os.rename("eski_ad.txt", "yeni_ad.txt")
        print("Dosya adı değiştirildi (örnek)")
    
    def path_exists_ornegi(self):
        """os.path.exists(path) - Dosya veya klasörün var olup olmadığını kontrol eder"""
        print(f"Mevcut dosya var mı: {os.path.exists('main.py')}")
    
    def path_isfile_ornegi(self):
        """os.path.isfile(path) - Belirtilen yolun dosya olup olmadığını kontrol eder"""
        print(f"Bu bir dosya mı: {os.path.isfile('main.py')}")
    
    def path_isdir_ornegi(self):
        """os.path.isdir(path) - Belirtilen yolun klasör olup olmadığını kontrol eder"""
        print(f"Bu bir klasör mü: {os.path.isdir('.')}")
    
    def path_join_ornegi(self):
        """os.path.join() - Yol parçalarını birleştirir (işletim sistemine uygun)"""
        yol = os.path.join("klasor", "alt_klasor", "dosya.txt")
        print(f"Birleştirilmiş yol: {yol}")
    
    def path_split_ornegi(self):
        """os.path.split(path) - Yolu dizin ve dosya adı olarak ayırır"""
        dizin, dosya = os.path.split(r"C:\Users\w\Desktop\dosya.txt")
        print(f"Dizin: {dizin}, Dosya: {dosya}")
    
    def walk_ornegi(self):
        """os.walk(path) - Dizin ağacını dolaşır, tüm alt klasörleri ve dosyaları gezer"""
        print("\nDizin ağacı:")
        for gecerli_dizin, klasorler, dosyalar in os.walk("."):
            print(f"Dizin: {gecerli_dizin}")
            print(f"  Klasörler: {klasorler}")
            print(f"  Dosyalar: {dosyalar}")
            print()
    
    def getsize_ornegi(self):
        """os.path.getsize(path) - Dosya boyutunu byte cinsinden döndürür"""
        if os.path.exists("main.py"):
            boyut = os.path.getsize("main.py")
            print(f"Dosya boyutu: {boyut} byte")


class ZarSimulasyonu:
    """Zar simülasyonu örneği"""
    def __init__(self):
        print("Zar simülasyonu hazır")
    
    def tek_zar_olasiligi(self):
        """Tek zar atma olasılığı simülasyonu"""
        zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        atim_sayisi = 10000
        
        for i in range(atim_sayisi):
            zar = random.randint(1, 6)
            zarlar[zar] += 1
        
        print(f"\n{atim_sayisi} atımda zar olasılıkları:")
        for zar in zarlar:
            oran = zarlar[zar] / atim_sayisi
            print(f"{zar} gelme olasılığı: %{oran * 100:.2f}")
    
    def cift_alti_olasiligi(self):
        """İki zarla 6-6 gelme simülasyonu"""
        alti_alti = 0
        deneme_sayisi = 0
        hedef = 10
        
        while alti_alti < hedef:
            deneme_sayisi += 1
            zar1 = random.randint(1, 6)
            zar2 = random.randint(1, 6)
            
            if zar1 == 6 and zar2 == 6:
                alti_alti += 1
        
        print(f"\n{hedef} adet 6-6 gelmesi için {deneme_sayisi} deneme yapıldı")
        print(f"Ortalama: Her {deneme_sayisi / hedef:.1f} atışta bir 6-6 geldi")


if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON MODÜL ÖRNEKLERİ")
    print("=" * 60)
    
    # Random Modülü
    print("\n--- RANDOM MODÜLÜ ---")
    listee = ["Kadir", "Fatima", "Ali", "Veli", "Ayşe"]
    rand = RandomModul(listee)
    rand.randint_ornegi()
    rand.choice_ornegi()
    rand.sample_ornegi()
    
    # Time Modülü
    print("\n--- TIME MODÜLÜ ---")
    time_mod = TimeModul()
    time_mod.time_ornegi()
    time_mod.ctime_ornegi()
    time_mod.strftime_ornegi()
    
    # Datetime Modülü
    print("\n--- DATETIME MODÜLÜ ---")
    dt_mod = DatetimeModul()
    dt_mod.datetime_now_ornegi()
    dt_mod.timedelta_ornegi()
    dt_mod.strftime_ornegi()
    
    # OS Modülü
    print("\n--- OS MODÜLÜ ---")
    os_mod = OsModul()
    os_mod.getcwd_ornegi()
    os_mod.listdir_ornegi()
    os_mod.path_exists_ornegi()
    
    # Zar Simülasyonu
    print("\n--- ZAR SİMÜLASYONU ---")
    zar = ZarSimulasyonu()
    zar.tek_zar_olasiligi()
    zar.cift_alti_olasiligi()
    
    print("\n" + "=" * 60)