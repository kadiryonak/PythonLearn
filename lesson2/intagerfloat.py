# Matematiksel İşlemler
    

#    1. Toplama: +
#    2. Çıkarma: -
#    3. Çarpma: *
#    4. Bölme: /
#    5. Modülüs (Kalan Bulma): %
#    6. Üs Alma: **
#    7. Tamsayı Bölme (Floor Division): //
#    mutlak değer: abs()
#    yuvarlama: round()
    
 
sayi = 10
sayi2 = 20.5
sayi3 = 5 **3
print(sayi3)
print(type(sayi3))

print(type(sayi))
print(type(sayi2))

toplam = sayi + sayi2
print(toplam)


print(abs(-55))  # 55
print(round(5.67))  # 6
print(round(5.34))  # 5
print(round(5.6789, 2))  # 5.68
print(round(5.6789, 3))  # 5.679

print(10 + 3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 / 3)  # 3.3333333333333335
print(10 % 3)  # 1
print(10 ** 3)  # 1000
print(10 // 3)  # 3

# Karşılaştırma Operatörleri
#    1. Eşittir: ==
#    2. Eşit Değildir: !=
#    3. Büyüktür: >
#    4. Küçüktür: <
#    5. Büyük Eşittir: >=
#    6. Küçük Eşittir: <=

print( sayi == sayi2 )  # False
print( sayi != sayi2 )  # True
print( sayi > sayi2 )   # False
print( sayi < sayi2 )   # True
print( sayi >= sayi2 )  # False
print( sayi <= sayi2 )  # True

sayi += 5  # sayi = sayi + 5