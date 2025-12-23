# DÖNGÜLER (Loops) - Python'da Tekrarlı İşlemler
# For ve While döngüleri ile farklı kullanım örnekleri

if __name__ == "__main__":


    print("1. FOR DÖNGÜSÜ - TEMEL KULLANIM")


    # Liste üzerinde döngü
    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Liste elemanları:")
    for i in liste:
        print(i, end=" ")
    print()

    # range() kullanımı
    print("\nrange(5): ", end="")
    for i in range(5):  # 0'dan 4'e kadar
        print(i, end=" ")
    
    print("\nrange(2, 8): ", end="")
    for i in range(2, 8):  # 2'den 7'ye kadar
        print(i, end=" ")
    
    print("\nrange(0, 10, 2): ", end="")  # Adım: 2 (çift sayılar)
    for i in range(0, 10, 2):
        print(i, end=" ")
    
    print("\nrange(10, 0, -1): ", end="")  # Tersten sayma
    for i in range(10, 0, -1):
        print(i, end=" ")
    print()

    # Toplam hesaplama
    sonuc = 0
    for a in range(4, 10):
        sonuc += a
    print(f"\n4'ten 9'a kadar toplam: {sonuc}")


    print("2. İÇ İÇE DÖNGÜLER (Nested Loops)")


    liste1 = [1, 2, 3]
    liste2 = ["a", "b", "c"]

    for sayi in liste1:
        for harf in liste2:
            print(f"({sayi}, {harf})", end=" ")
        print()  # Satır sonu

    # Çarpım tablosu
    print("\nÇarpım Tablosu (1-5):")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i*j:3}", end=" ")
        print()


    print("3. BREAK VE CONTINUE")


    # break - Döngüyü tamamen durdurur
    print("break örneği (5'te dur):")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()

    # continue - Bu adımı atla, sonrakine geç
    print("\ncontinue örneği (5'i atla):")
    for i in range(10):
        if i == 5:
            continue
        print(i, end=" ")
    print()

    print("4. ELSE İLE DÖNGÜ")

    # for-else: Döngü break olmadan biterse else çalışır
    print("Asal sayı kontrolü (7):")
    sayi = 7
    for i in range(2, sayi):
        if sayi % i == 0:
            print(f"{sayi} asal değil, {i}'ye bölünür")
            break
    else:
        print(f"{sayi} asal sayıdır!")


    print("5. ENUMERATE - İNDEKS İLE GEZİNME")

    meyveler = ["elma", "armut", "muz", "çilek"]

    # Klasik yöntem
    print("Klasik yöntem:")
    for i in range(len(meyveler)):
        print(f"  {i}: {meyveler[i]}")

    # enumerate() ile (daha Pythonic!)
    print("\nenumerate ile:")
    for index, meyve in enumerate(meyveler):
        print(f"  {index}: {meyve}")

    # Başlangıç indeksini değiştirme
    print("\nenumerate(start=1):")
    for index, meyve in enumerate(meyveler, start=1):
        print(f"  {index}. {meyve}")

    print("6. ZIP - BİRDEN FAZLA LİSTE GEZİNME")

    isimler = ["Ali", "Ayşe", "Mehmet"]
    yaslar = [25, 30, 22]
    sehirler = ["Ankara", "İstanbul", "İzmir"]

    print("zip() ile paralel gezinme:")
    for isim, yas, sehir in zip(isimler, yaslar, sehirler):
        print(f"  {isim} - {yas} yaşında - {sehir}'de yaşıyor")

    print("\n" + "=" * 50)
    print("7. WHILE DÖNGÜSÜ")
    print("=" * 50)

    # Temel while
    print("1'den 5'e kadar:")
    i = 1
    while i <= 5:
        print(i, end=" ")
        i += 1
    print()

    # while ile kullanıcı girişi simülasyonu
    print("\nŞifre denemesi simülasyonu:")
    dogru_sifre = "1234"
    deneme = 0
    max_deneme = 3
    sifreler = ["yanlış", "hata", "1234"]  # Simülasyon için

    while deneme < max_deneme:
        girilen = sifreler[deneme]
        print(f"  Deneme {deneme + 1}: '{girilen}'", end="")
        if girilen == dogru_sifre:
            print(" ✓ Doğru!")
            break
        print(" ✗ Yanlış")
        deneme += 1
    else:
        print("  Çok fazla yanlış deneme!")

    print("\n" + "=" * 50)
    print("8. LIST COMPREHENSION (Tek Satırda Döngü)")
    print("=" * 50)

    # Klasik yöntem
    kareler = []
    for x in range(1, 6):
        kareler.append(x ** 2)
    print(f"Klasik: {kareler}")

    # Comprehension ile
    kareler2 = [x ** 2 for x in range(1, 6)]
    print(f"Comprehension: {kareler2}")

    # Koşullu comprehension
    cift_kareler = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    print(f"Çift sayıların kareleri: {cift_kareler}")

    # İç içe comprehension
    matris = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"3x3 Matris: {matris}")

    print("\n" + "=" * 50)
    print("9. DICTIONARY VE SET COMPREHENSION")
    print("=" * 50)

    # Dict comprehension
    kup_dict = {x: x ** 3 for x in range(1, 6)}
    print(f"Küp sözlüğü: {kup_dict}")

    # Set comprehension
    benzersiz_harfler = {harf for harf in "merhaba dünya"}
    print(f"Benzersiz harfler: {benzersiz_harfler}")

    print("\n" + "=" * 50)
    print("10. GENERATOR EXPRESSION (Bellek Dostu)")
    print("=" * 50)

    # List vs Generator
    liste_buyuk = [x ** 2 for x in range(5)]  # Tamamını bellekte tutar
    generator = (x ** 2 for x in range(5))    # Tembel hesaplama (lazy)

    print(f"Liste: {liste_buyuk}")
    print(f"Generator: {generator}")
    print(f"Generator elemanları: ", end="")
    for val in generator:
        print(val, end=" ")
    print()

    # sum, max, min ile generator
    toplam = sum(x for x in range(1, 101))
    print(f"\n1'den 100'e toplam: {toplam}")

    print("\n" + "=" * 50)
    print("ÖZET")
    print("=" * 50)
    print("for   -> Belirli sayıda tekrar (liste, range)")
    print("while -> Koşul doğru olduğu sürece tekrar")
    print("break -> Döngüyü tamamen durdur")
    print("continue -> Bu adımı atla")
    print("enumerate -> İndeks + değer birlikte")
    print("zip -> Birden fazla listeyi paralel gez")
    print("comprehension -> Tek satırda döngü")