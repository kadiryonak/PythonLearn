# INPUT VE DÖNGÜLER - KAPSAMLI PRATİK PROBLEMLER
# 25+ problem: Sayı işlemleri, Desenler, Algoritmalar

# ============================================================
# BÖLÜM 1: SAYI İŞLEMLERİ
# ============================================================

def problem_01_basamak_sayisi():
    """Bir sayının kaç basamaklı olduğunu bul."""
    
    sayilar = [5, 42, 123, 9999, 100000]
    for sayi in sayilar:
        basamak = 0
        temp = sayi
        while temp > 0:
            basamak += 1
            temp //= 10
        print(f"{sayi} -> {basamak} basamaklı")


def problem_02_basamak_toplami():
    """Bir sayının rakamları toplamını bul."""
    
    sayilar = [123, 456, 9999, 12345]
    for sayi in sayilar:
        toplam = 0
        temp = sayi
        while temp > 0:
            toplam += temp % 10
            temp //= 10
        print(f"{sayi} -> Rakamlar toplamı: {toplam}")


def problem_03_sayi_ters_cevir():
    """Bir sayıyı tersine çevir."""
    
    sayilar = [123, 4567, 12345]
    for sayi in sayilar:
        ters = 0
        temp = sayi
        while temp > 0:
            ters = ters * 10 + temp % 10
            temp //= 10
        print(f"{sayi} -> {ters}")


def problem_04_palindrom_sayi():
    """Sayı palindrom mu? (Tersi kendisine eşit mi?)"""
    
    sayilar = [121, 123, 1221, 12321, 12345]
    for sayi in sayilar:
        ters = 0
        temp = sayi
        while temp > 0:
            ters = ters * 10 + temp % 10
            temp //= 10
        if sayi == ters:
            print(f"{sayi} ✓ PALİNDROM")
        else:
            print(f"{sayi} ✗ Palindrom değil")


def problem_05_armstrong_sayi():
    """Armstrong sayısı mı? (Rakamların küpü toplamı = kendisi)"""
    
    sayilar = [153, 370, 371, 407, 123, 1634]
    for sayi in sayilar:
        basamak_sayisi = len(str(sayi))
        toplam = 0
        temp = sayi
        while temp > 0:
            toplam += (temp % 10) ** basamak_sayisi
            temp //= 10
        if sayi == toplam:
            print(f"{sayi} ✓ ARMSTRONG")
        else:
            print(f"{sayi} ✗ Armstrong değil")


def problem_06_mukemmel_sayi():
    """Mükemmel sayı mı? (Bölenlerinin toplamı = kendisi)
    Örnek: 6 = 1 + 2 + 3"""
    
    sayilar = [6, 12, 28, 496, 100]
    for sayi in sayilar:
        toplam = 0
        for i in range(1, sayi):
            if sayi % i == 0:
                toplam += i
        if toplam == sayi:
            print(f"{sayi} ✓ MÜKEMMEL (bölenler toplamı: {toplam})")
        else:
            print(f"{sayi} ✗ Mükemmel değil (bölenler toplamı: {toplam})")


def problem_07_faktoriyel():
    """Faktöriyel hesapla."""
    
    for n in range(1, 8):
        fakt = 1
        for i in range(1, n + 1):
            fakt *= i
        print(f"{n}! = {fakt}")


def problem_08_fibonacci():
    """Fibonacci serisi."""
    
    n = 15
    a, b = 0, 1
    print(f"İlk {n} Fibonacci: ", end="")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def problem_09_asal_sayilar():
    """1-100 arası asal sayılar."""
    
    print("Asallar: ", end="")
    for sayi in range(2, 101):
        asal = True
        for i in range(2, int(sayi ** 0.5) + 1):
            if sayi % i == 0:
                asal = False
                break
        if asal:
            print(sayi, end=" ")
    print()


def problem_10_obeb_okek():
    """OBEB ve OKEK hesapla."""
    
    ciftler = [(12, 18), (24, 36), (15, 25)]
    for a, b in ciftler:
        x, y = a, b
        while y:
            x, y = y, x % y
        obeb = x
        okek = (a * b) // obeb
        print(f"({a}, {b}) -> OBEB: {obeb}, OKEK: {okek}")


def problem_11_ikili_donusum():
    """Ondalık sayıyı ikiliye çevir."""
    
    sayilar = [5, 10, 25, 100, 255]
    for sayi in sayilar:
        ikili = ""
        temp = sayi
        while temp > 0:
            ikili = str(temp % 2) + ikili
            temp //= 2
        print(f"{sayi} -> {ikili}")


# ============================================================
# BÖLÜM 2: DESEN VE PİRAMİTLER
# ============================================================

def problem_12_sol_ucgen():
    """Sol hizalı yıldız üçgeni."""
    
    n = 5
    for i in range(1, n + 1):
        print("*" * i)


def problem_13_sag_ucgen():
    """Sağ hizalı yıldız üçgeni."""
    
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def problem_14_ortali_piramit():
    """Ortalanmış piramit."""
    
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def problem_15_ters_piramit():
    """Ters piramit."""
    
    n = 5
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def problem_16_elmas():
    """Elmas deseni."""
    
    n = 5
    # Üst yarı
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Alt yarı
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def problem_17_ici_bos_kare():
    """İçi boş kare."""
    
    n = 5
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def problem_18_ici_bos_piramit():
    """İçi boş piramit."""
    
    n = 5
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - 1) + "*")
        elif i == n:
            print("*" * (2 * n - 1))
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")


def problem_19_sayi_piramidi():
    """Sayı piramidi (1, 12, 123...)."""
    
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def problem_20_ters_sayi_piramidi():
    """Ters sayı piramidi."""
    
    n = 5
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def problem_21_floyd_ucgeni():
    """Floyd üçgeni."""
        
    n = 5
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{num:3}", end="")
            num += 1
        print()


def problem_22_pascal_ucgeni():
    """Pascal üçgeni."""
    
    n = 6
    for i in range(n):
        # Sol boşluk
        print(" " * (n - i - 1) * 2, end="")
        val = 1
        for j in range(i + 1):
            print(f"{val:3} ", end="")
            val = val * (i - j) // (j + 1)
        print()


def problem_23_harf_piramidi():
    """Harf piramidi (A, AB, ABC...)."""
    
    n = 5
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()


def problem_24_kum_saati():
    """Kum saati deseni."""
    
    n = 5
    # Üst yarı (daralan)
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Alt yarı (genişleyen)
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def problem_25_kelebek():
    """Kelebek deseni."""
    
    n = 4
    # Üst yarı
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    # Alt yarı
    for i in range(n - 1, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)


# ============================================================
# BÖLÜM 3: ALGORİTMA PROBLEMLERİ
# ============================================================

def problem_26_carpim_tablosu():
    """Çarpım tablosu."""

    
    for i in range(1, 6):
        for j in range(1, 11):
            print(f"{i}x{j}={i*j:2}", end="  ")
        print()


def problem_27_harf_frekansi():
    """Cümledeki harf frekansı."""

    
    cumle = "merhaba dünya"
    frekans = {}
    for harf in cumle.lower():
        if harf != " ":
            frekans[harf] = frekans.get(harf, 0) + 1
    
    for harf, sayi in sorted(frekans.items()):
        print(f"'{harf}': {'█' * sayi} ({sayi})")


def problem_28_en_buyuk_en_kucuk():
    """Listede en büyük ve en küçük bulma."""

    
    liste = [34, 12, 89, 23, 56, 7, 45]
    print(f"Liste: {liste}")
    
    en_buyuk = liste[0]
    en_kucuk = liste[0]
    
    for sayi in liste:
        if sayi > en_buyuk:
            en_buyuk = sayi
        if sayi < en_kucuk:
            en_kucuk = sayi
    
    print(f"En büyük: {en_buyuk}")
    print(f"En küçük: {en_kucuk}")


def problem_29_tekrar_eden_elemanlar():
    """Listede tekrar eden elemanları bul."""

    
    liste = [1, 2, 3, 2, 4, 3, 5, 6, 3, 7]
    print(f"Liste: {liste}")
    
    tekrarlar = {}
    for eleman in liste:
        tekrarlar[eleman] = tekrarlar.get(eleman, 0) + 1
    
    print("Tekrar edenler: ", end="")
    for eleman, sayi in tekrarlar.items():
        if sayi > 1:
            print(f"{eleman}({sayi}x) ", end="")
    print()


def problem_30_collatz():
    """Collatz dizisi (3n+1 problemi)."""
    
    n = 27
    print(f"Başlangıç: {n}")
    adim = 0
    print(n, end="")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(f" -> {n}", end="")
        adim += 1
    print(f"\nToplam {adim} adımda 1'e ulaştı!")


def problem_31_tersten_sayma():
    """1000'den 1'e kadar tersten sayma."""

    
    print("İlk 20 sayı: ", end="")
    for i in range(1000, 980, -1):
        print(i, end=" ")
    print("... ", end="")
    
    print("\nSon 20 sayı: ", end="")
    for i in range(20, 0, -1):
        print(i, end=" ")
    print()
    
    # Toplam
    toplam = sum(range(1, 1001))
    print(f"1'den 1000'e toplam: {toplam}")


def problem_32_asal_son_rakam():
    """İlk 10.000 asal sayının kaç tanesi 3 ve 7 ile biter?"""

    
    def asal_mi(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # İlk 10.000 asalı bul
    asallar = []
    sayi = 2
    while len(asallar) < 10000:
        if asal_mi(sayi):
            asallar.append(sayi)
        sayi += 1
    
    # Son rakam analizi
    sonu_1 = sum(1 for p in asallar if p % 10 == 1)
    sonu_3 = sum(1 for p in asallar if p % 10 == 3)
    sonu_7 = sum(1 for p in asallar if p % 10 == 7)
    sonu_9 = sum(1 for p in asallar if p % 10 == 9)
    sonu_2 = sum(1 for p in asallar if p % 10 == 2)  # sadece 2
    sonu_5 = sum(1 for p in asallar if p % 10 == 5)  # sadece 5
    
    print(f"İlk 10.000 asal sayı analizi:")
    print(f"  10.000. asal sayı: {asallar[-1]}")
    print(f"\nSon rakam dağılımı:")
    print(f"  Sonu 1 ile biten: {sonu_1} (%{sonu_1/100:.1f})")
    print(f"  Sonu 3 ile biten: {sonu_3} (%{sonu_3/100:.1f})")
    print(f"  Sonu 7 ile biten: {sonu_7} (%{sonu_7/100:.1f})")
    print(f"  Sonu 9 ile biten: {sonu_9} (%{sonu_9/100:.1f})")
    print(f"  Sonu 2 ile biten: {sonu_2} (sadece 2)")
    print(f"  Sonu 5 ile biten: {sonu_5} (sadece 5)")
    print(f"\n>>> Sonu 3 veya 7 ile biten: {sonu_3 + sonu_7} (%{(sonu_3+sonu_7)/100:.1f})")


def problem_33_rakam_kupu():
    """3 basamaklı sayılardan, rakamları toplamının küpüne eşit olanlar."""

    print("PROBLEM 33: Rakam Toplamı Küpüne Eşit Sayılar")

    
    print("3 basamaklı sayılar (100-999) arasında:")
    print("Sayı = (Rakamların Toplamı)³ olanlar:\n")
    
    bulunanlar = []
    
    for sayi in range(100, 1000):
        # Rakamları ayır
        yuzler = sayi // 100
        onlar = (sayi // 10) % 10
        birler = sayi % 10
        
        # Rakamların toplamı
        toplam = yuzler + onlar + birler
        
        # Küpü hesapla
        kup = toplam ** 3
        
        if sayi == kup:
            bulunanlar.append(sayi)
            print(f"  {sayi} = ({yuzler}+{onlar}+{birler})³ = {toplam}³ = {kup} ✓")
    
    print(f"\nToplam {len(bulunanlar)} adet sayı bulundu: {bulunanlar}")


# === ANA PROGRAM ===
if __name__ == "__main__":



    
    # Sayı İşlemleri
    problem_01_basamak_sayisi()
    problem_02_basamak_toplami()
    problem_03_sayi_ters_cevir()
    problem_04_palindrom_sayi()
    problem_05_armstrong_sayi()
    problem_06_mukemmel_sayi()
    problem_07_faktoriyel()
    problem_08_fibonacci()
    problem_09_asal_sayilar()
    problem_10_obeb_okek()
    problem_11_ikili_donusum()
    
    # Desenler
    problem_12_sol_ucgen()
    problem_13_sag_ucgen()
    problem_14_ortali_piramit()
    problem_15_ters_piramit()
    problem_16_elmas()
    problem_17_ici_bos_kare()
    problem_18_ici_bos_piramit()
    problem_19_sayi_piramidi()
    problem_20_ters_sayi_piramidi()
    problem_21_floyd_ucgeni()
    problem_22_pascal_ucgeni()
    problem_23_harf_piramidi()
    problem_24_kum_saati()
    problem_25_kelebek()
    
    # Algoritmalar
    problem_26_carpim_tablosu()
    problem_27_harf_frekansi()
    problem_28_en_buyuk_en_kucuk()
    problem_29_tekrar_eden_elemanlar()
    problem_30_collatz()
    problem_31_tersten_sayma()
    problem_32_asal_son_rakam()
    problem_33_rakam_kupu()
    
    print("\n" + "=" * 50)
    print("   33 PROBLEM TAMAMLANDI! 🎉")
    print("=" * 50)

