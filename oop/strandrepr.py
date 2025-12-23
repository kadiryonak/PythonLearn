# __str__ ve __repr__ Magic Methods
# ===================================
# __str__: Kullanıcı dostu string temsili (print için)
# __repr__: Geliştirici dostu string temsili (debug için)


class Karikaturcu:
    """Karikatürcü sınıfı - __str__ ve __repr__ örneği"""
    
    def __init__(self, isim, takma_ad, yil, dergi):
        self.isim = isim
        self.takma_ad = takma_ad
        self.yil = yil  # Karikatüre başladığı yıl
        self.dergi = dergi
        self.eserler = []
    
    def eser_ekle(self, eser):
        """Karikatürcüye eser ekler."""
        self.eserler.append(eser)
    
    def __str__(self):
        """Kullanıcı dostu çıktı - print() ile kullanılır."""
        return f" {self.takma_ad} ({self.isim}) - {self.dergi} dergisinde çiziyor"
    
    def __repr__(self):
        """Geliştirici dostu çıktı - debug ve nesne temsili için."""
        return f"Karikaturcu(isim='{self.isim}', takma_ad='{self.takma_ad}', yil={self.yil}, dergi='{self.dergi}')"


# Örnek kullanım
if __name__ == "__main__":
    
    # Karikatürcüler oluştur
    karikaturcu1 = Karikaturcu("Turhan Selçuk", "Abdülcanbaz", 1950, "Milliyet")
    karikaturcu1.eser_ekle("Abdülcanbaz Serisi")
    karikaturcu1.eser_ekle("Günlük Karikatürler")
    
    karikaturcu2 = Karikaturcu("Kemal Sunal", "KemalS", 1970, "Gırgır")
    
    # __str__ kullanımı - print() otomatik olarak __str__'ı çağırır
    print(karikaturcu1)
    print(karikaturcu2)
    
    # __repr__ kullanımı - nesneyi doğrudan yazdırma
    print(repr(karikaturcu1))
    print(repr(karikaturcu2))
    
    # Liste içinde nesneler - __repr__ kullanılır
    karikaturculer = [karikaturcu1, karikaturcu2]
    print(karikaturculer)  # Liste içindeki nesneler için __repr__ kullanılır
    
    # __str__ vs __repr__ farkı
    print(f"str():  {str(karikaturcu1)}")
    print(f"repr(): {repr(karikaturcu1)}")


    # özel olarak çağırabiliriz
    print(karikaturcu1.__repr__())
    print(karikaturcu1.__str__())

# OUTPUT:

#  Abdülcanbaz (Turhan Selçuk) - Milliyet dergisinde çiziyor
#  KemalS (Kemal Sunal) - Gırgır dergisinde çiziyor
#  1. tercihi __str__ oluyor ama bulamazsa repr e gidiyor
#  

# Karikaturcu(isim='Turhan Selçuk', takma_ad='Abdülcanbaz', yil=1950, dergi='Milliyet')
# Karikaturcu(isim='Kemal Sunal', takma_ad='KemalS', yil=1970, dergi='Gırgır')
#
# [Karikaturcu(isim='Turhan Selçuk', ...), Karikaturcu(isim='Kemal Sunal', ...)]
#
# === Fark ===
# str():   Abdülcanbaz (Turhan Selçuk) - Milliyet dergisinde çiziyor
# repr(): Karikaturcu(isim='Turhan Selçuk', takma_ad='Abdülcanbaz', yil=1950, dergi='Milliyet')
