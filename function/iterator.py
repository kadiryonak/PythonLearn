# ==========================================
# ITERATOR (YINELEYICI)
# ==========================================
# Iterator: Bir koleksiyonun elemanlarını tek tek gezmeye yarayan objedir.
# Her iterator iki önemli metod içerir:
#   __iter__(): Iterator objesini döndürür
#   __next__(): Sıradaki elemanı döndürür


# ==========================================
# TEMEL KAVRAMLAR
# ==========================================

# Iterable: Üzerinde gezinilebilen objeler (list, tuple, string, dict)
# Iterator: Iterable'dan oluşturulan, next() ile gezilen obje

# ÖRNEK 1: Liste ile Iterator
print("Liste Iterator")
liste = [1, 2, 3]
iterator = iter(liste)  # Listeyi iterator'a çevir

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration hatası verir!


# ÖRNEK 2: String ile Iterator
print("\nString Iterator")
metin = "Python"
iterator = iter(metin)

for _ in range(len(metin)):
    print(next(iterator), end=" ")
print()


# ÖRNEK 3: for döngüsü aslında iterator kullanır
print("\nfor döngüsü = Iterator")
# Bu ikisi aynı işi yapar:

# for ile
for i in [1, 2, 3]:
    print(i, end=" ")
print()

# Iterator ile (arka planda olan)
iterator = iter([1, 2, 3])
while True:
    try:
        print(next(iterator), end=" ")
    except StopIteration:
        break
print()


# ==========================================
# KENDİ ITERATOR'UMUZU YAZALIM
# ==========================================

# ÖRNEK 4: Sayaç Iterator
print("\n Kendi Iterator'umuz: Sayaç")

class Sayac:
    def __init__(self, baslangic, bitis):
        self.baslangic = baslangic
        self.bitis = bitis
    
    def __iter__(self):
        self.sayi = self.baslangic
        return self
    
    def __next__(self):
        if self.sayi <= self.bitis:
            sonuc = self.sayi
            self.sayi += 1
            return sonuc
        else:
            raise StopIteration

# Kullanım
sayac = Sayac(1, 5)
for s in sayac:
    print(s, end=" ")  # 1 2 3 4 5
print()


# ÖRNEK 5: Çift Sayılar Iterator
print("\n Çift Sayılar Iterator")

class CiftSayilar:
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        self.sayi = 0
        return self
    
    def __next__(self):
        self.sayi += 2
        if self.sayi <= self.limit:
            return self.sayi
        else:
            raise StopIteration

ciftler = CiftSayilar(10)
print(list(ciftler))  # [2, 4, 6, 8, 10]


# ÖRNEK 6: Fibonacci Iterator
print("\n Fibonacci Iterator")

class Fibonacci:
    def __init__(self, adet):
        self.adet = adet
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.sayac = 0
        return self
    
    def __next__(self):
        if self.sayac < self.adet:
            sonuc = self.a
            self.a, self.b = self.b, self.a + self.b
            self.sayac += 1
            return sonuc
        else:
            raise StopIteration

fib = Fibonacci(10)
print(f"İlk 10 Fibonacci: {list(fib)}")


# ÖRNEK 7: Ters Çevirici Iterator
print("\n Ters Çevirici Iterator")

class TersCevir:
    def __init__(self, veri):
        self.veri = veri
    
    def __iter__(self):
        self.index = len(self.veri)
        return self
    
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.veri[self.index]
        else:
            raise StopIteration

ters = TersCevir("Python")
print(f"Ters: {''.join(list(ters))}")  # nohtyP

ters_liste = TersCevir([1, 2, 3, 4, 5])
print(f"Ters liste: {list(ters_liste)}")  # [5, 4, 3, 2, 1]


# ÖRNEK 8: Sonsuz Iterator (dikkatli kullan!)
print("\n Sonsuz Iterator (ilk 5 eleman)")

class SonsuzSayac:
    def __init__(self):
        self.sayi = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.sayi += 1
        return self.sayi

sonsuz = SonsuzSayac()
for i, sayi in enumerate(sonsuz):
    if i >= 5:  # Sonsuz olduğu için manuel durduralım
        break
    print(sayi, end=" ")
print()


# ==========================================
# GENERATOR vs ITERATOR
# ==========================================
print("\n Generator (Kısa Yol)")

# Iterator yerine generator kullanmak daha kolay:
def sayac_generator(baslangic, bitis):
    sayi = baslangic
    while sayi <= bitis:
        yield sayi  # yield ile değer döndür
        sayi += 1

for s in sayac_generator(1, 5):
    print(s, end=" ")
print()

# Fibonacci generator
def fibonacci_gen(adet):
    a, b = 0, 1
    for _ in range(adet):
        yield a
        a, b = b, a + b

print(f"Fibonacci (generator): {list(fibonacci_gen(10))}")
