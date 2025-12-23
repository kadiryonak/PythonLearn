# SÖZLÜK (Dictionary) - Python'un En Güçlü Veri Yapılarından Biri
# Anahtar-Değer (Key-Value) çiftleri şeklinde veri saklar
# Süslü parantez {} ile oluşturulur

if __name__ == "__main__":

    # --- 1. SÖZLÜK OLUŞTURMA ---
    print("1. SÖZLÜK OLUŞTURMA")


    # Boş sözlük
    bos_sozluk = {}
    bos_sozluk2 = dict()
    print(f"Boş sözlük: {bos_sozluk}, Tipi: {type(bos_sozluk)}")

    # Değerlerle oluşturma
    ogrenci = {
        "ad": "Ahmet",
        "soyad": "Yılmaz",
        "yas": 22,
        "bolum": "Bilgisayar Mühendisliği",
        "notlar": [85, 90, 78]
    }
    print(f"Öğrenci: {ogrenci}")

    # --- 2. ELEMANLARA ERİŞİM ---

    print("2. ELEMANLARA ERİŞİM")


    # Köşeli parantez ile
    print(f"Ad: {ogrenci['ad']}")
    print(f"Yaş: {ogrenci['yas']}")

    # get() metodu - Anahtar yoksa hata vermez, None döner
    print(f"Telefon (yok): {ogrenci.get('telefon')}")
    print(f"Telefon (varsayılan): {ogrenci.get('telefon', 'Bilgi yok')}")
    print(f"yas: {ogrenci.get('yas', 'Bilgi yok')}")
    # --- 3. ELEMAN EKLEME VE GÜNCELLEME ---
    print("3. ELEMAN EKLEME VE GÜNCELLEME")

    # Yeni anahtar ekleme
    ogrenci["email"] = "ahmet@example.com"
    ogrenci["telefon"] = "555-1234"
    print(f"Email eklendi: {ogrenci['email']}")

    # Değer güncelleme
    ogrenci["yas"] = 23
    print(f"Yaş güncellendi: {ogrenci['yas']}")

    # update() ile toplu güncelleme
    ogrenci.update({"sehir": "Ankara", "yas": 24})
    print(f"Toplu güncelleme sonrası: {ogrenci}")

    # --- 4. ELEMAN SİLME ---
    print("4. ELEMAN SİLME")

    # pop() - Değeri döndürerek siler
    silinen_email = ogrenci.pop("email")
    print(f"Silinen email: {silinen_email}")

    # del - Direkt siler
    del ogrenci["telefon"]
    print(f"Telefon silindi: {ogrenci}")

    # popitem() - Son eklenen çifti siler (Python 3.7+)
    son_eklenen = ogrenci.popitem()
    print(f"Son eklenen silindi: {son_eklenen}")

    # --- 5. SÖZLÜK METOTLARİ ---
    print("5. SÖZLÜK METOTLARI")

    test_dict = {"a": 1, "b": 2, "c": 3}

    # keys() - Tüm anahtarlar
    print(f"Anahtarlar: {list(test_dict.keys())}")

    # values() - Tüm değerler
    print(f"Değerler: {list(test_dict.values())}")

    # items() - Anahtar-değer çiftleri (tuple olarak)
    print(f"Çiftler: {list(test_dict.items())}")

    # --- 6. SÖZLÜKTE DÖNGÜ ---
    print("6. SÖZLÜKTE DÖNGÜ")

    meyveler = {"elma": 5, "armut": 3, "muz": 7}

    # Sadece anahtarlar
    print("Sadece anahtarlar:")
    for meyve in meyveler:
        print(f"  - {meyve}")

    # Anahtar ve değer birlikte
    print("\nAnahtar ve Değer:")
    for meyve, adet in meyveler.items():
        print(f"  - {meyve}: {adet} adet")

    # --- 7. KONTROL İŞLEMLERİ ---
    print("7. KONTROL İŞLEMLERİ")

    # Anahtar var mı?
    print(f"'elma' var mı? {'elma' in meyveler}")
    print(f"'kiraz' var mı? {'kiraz' in meyveler}")

    # Uzunluk
    print(f"Kaç eleman var? {len(meyveler)}")

    # --- 8. İÇ İÇE SÖZLÜKLER (Nested Dictionary) ---
    print("8. İÇ İÇE SÖZLÜKLER")

    sinif = {
        "ogrenci1": {
            "ad": "Ali",
            "not": 85
        },
        "ogrenci2": {
            "ad": "Ayşe",
            "not": 92
        },
        "ogrenci3": {
            "ad": "Mehmet",
            "not": 78
        }
    }

    print(f"Öğrenci 2'nin adı: {sinif['ogrenci2']['ad']}")
    print(f"Öğrenci 3'ün notu: {sinif['ogrenci3']['not']}")

    # İç içe döngü
    print("\nTüm sınıf:")
    for ogrenci_id, bilgiler in sinif.items():
        print(f"  {ogrenci_id}: {bilgiler['ad']} - Not: {bilgiler['not']}")

    # --- 9. DICTIONARY COMPREHENSION ---
    print("9. DICTIONARY COMPREHENSION")

    # Sayıların karesini içeren sözlük
    kareler = {x: x**2 for x in range(1, 6)}
    print(f"Kareler: {kareler}")

    # Koşullu comprehension
    cift_kareler = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Çift sayıların kareleri: {cift_kareler}")

    # Listeden sözlük oluşturma
    isimler = ["ali", "veli", "ayşe"]
    isim_uzunluk = {isim: len(isim) for isim in isimler}
    print(f"İsim uzunlukları: {isim_uzunluk}")

    # --- 10. PRATİK ÖRNEKLER ---
    print("10. PRATİK ÖRNEKLER")

    # Harf sayacı
    cumle = "merhaba dünya"
    harf_sayaci = {}
    for harf in cumle:
        if harf != " ":
            harf_sayaci[harf] = harf_sayaci.get(harf, 0) + 1
    print(f"Harf sayacı: {harf_sayaci}")

    # İki liste birleştirme (zip ile)
    anahtarlar = ["a", "b", "c"]
    degerler = [1, 2, 3]
    birlesik = dict(zip(anahtarlar, degerler))
    print(f"Birleştirilmiş: {birlesik}")

    # Sözlüğü kopyalama
    kopya = meyveler.copy()
    print(f"Kopya: {kopya}")

    # Sözlüğü temizleme
    kopya.clear()
    print(f"Temizlendi: {kopya}")

    print("ÖZET: Sözlük = Anahtar ile hızlı erişim O(1)")
