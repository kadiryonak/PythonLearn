# liste nedir?
class ListL:
    def __init__(self, listt=None):
        if listt is None:
            self.listt = []
        else:
            self.listt = listt

    def append(self, data):
        self.listt.append(data)

    def delete(self, data):
        self.listt.remove(data)

    def print_list(self):
        print(self.listt)

    def length(self):
        return len(self.listt)


if __name__ == "__main__":

    renkler = []
    renk_listesi = ListL(renkler)

    renk_listesi.append("lacivert") # eleman ekleme
    renk_listesi.append("kırmızı")
    renk_listesi.append("sarı")
    renk_listesi.append("yeşil")
    renk_listesi.append("beyaz")
    renk_listesi.append("pembe")
    renk_listesi.append("mor")

    renk_listesi.print_list()
    renk_listesi.delete("lacivert") # eleman silme
    print("Lacivert silindi")
    renk_listesi.print_list()

    print("Join metodu")
    stringrenkler = " ".join(renkler)  # elemanları birleştirir
    print(stringrenkler)

    renkler2 = stringrenkler.split(" ")  # elemanları ayırır
    print(renkler2)

    print("Kırmızı" in renkler) # eleman var mı kontrol eder

    # index ve data şeklinde yazdırır
    print(list(enumerate(renkler, 1)))

    print("sınıf çalıştı")
    print(type(renkler))
    print(renkler)
    print(len(renkler))

    # liste elemanlarına erişim
    print(renkler[0])
    print(renkler[1])
    print(renkler[2])
    print(renkler[3])

    print(renkler[1:4])
    print(renkler[:2])
    print(renkler[2:])
    print(renkler[1:4:2])

    print("Enumerate")

    bos_liste = []
    print(bos_liste)
    print(type(bos_liste))

    bos_liste.append("lacivert")
    bos_liste.append("kırmızı")
    bos_liste.append("sarı")
    bos_liste.append("yeşil")
    bos_liste.append("beyaz")
    bos_liste.append("pembe")
    bos_liste.append("mor")

    print(bos_liste)

    bos_liste.remove("mor")
    print(bos_liste)

    bos_liste.pop()
    print(bos_liste)

    bos_liste.index("lacivert")
    print(bos_liste)

    bos_liste.count("lacivert")
    print(bos_liste)

    bos_liste.sort()
    print(bos_liste)

    bos_liste.reverse()
    print(bos_liste)

    bos_liste.copy()
    print(bos_liste)

    bos_liste.clear()
    print(bos_liste)

    bos_liste.extend("beyaz")
    print(bos_liste)

    bos_liste.insert(0, "yeşil")
    print(bos_liste)

    bos_liste.append(renkler)
    print(bos_liste)
