import os 

def duzenle():
    dosyalar = []
    uzantılar = []
    
    kadir = input("Düzenlecek doyanın ismi: ")

    def list_dir():
        for dosya in os.listdir(kadir):
            if os.path.isdir(os.path.join(kadir, dosya)):
                continue
            if dosya.startwith("."): # gizli dosya mı?
                continue

    list_dir()

    # Uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1] 
        if uzanti in uzantılar:
            continue
        else:
            uzantılar.append(uzanti)
    for uzanti in uzantılar:
        if os.path.isdir(os.path.join(kadir, uzanti)):
            continue
        else:
            os.mkdir(os.path.join(kadir, uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1] 
        os.rename(os.path.join(kadir, dosya), os.path.join(kadir, uzanti, dosya))

if __name__ == "__main__":

    print("Hello, Dünya!") 

    duzenle()

    