# Listelerden farkı ne ?
if __name__ == "__main__":
    

    print("demet yani tuple")
    demet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" )


    print(type(demet))
    print(demet)


    for harf in demet:
        print(harf)

    print(demet[3])

    #demet.append("n")

    # demet nasıl oluşturulduysa o şekilde kalır. Tuple'lar değiştirilemez. 
    print("Küme yani set")

    kume = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"}
    # Kümede bir eleman ancak bir kere bulunabilir. Aynı elemanı ekleriz lakin yazdırdığımızda gözükmez
    kume2 = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    print(kume.union(kume2))  # küme birleşimi (union) - iki kümenin tüm elemanlarını birleştirir
    
    print(kume.intersection(kume2))
    
    print(kume.difference(kume2))
    
    print(kume.symmetric_difference(kume2))
    
    print(kume.isdisjoint(kume2))

    print("k" in kume.union(kume2))

    print(type(kume))
    print(kume)
    kume.add("n")
    kume.remove("a")
    kume.pop()
    kume.__sizeof__()

    for harf in kume:
        print(harf)

    kume.add("n")
    # Küme sırasız bir veri yapısı. Her çalıştırdığımızda başka sıra ile gelebilir

    bos_liste1 = []
    bos_liste2 = list()
    print(type(bos_liste1))
    print(type(bos_liste2))
    print(bos_liste1)
    print(bos_liste2)

    bos_kume1 = set()
    bos_kume2 = {} # sözlüktür bu
    print(type(bos_kume1))
    print(type(bos_kume2))

    bos_demet1 = ()
    bos_demet2 = tuple()
    print(type(bos_demet1))
    print(type(bos_demet2))


    python = "PYTHON"

    kumee = set(python)
    print(kumee)