# *args **kwargs


def kuvvet_al(x,y): # positional arguments, hepsi tam olarak girilmeli
    return print(x ** y)

kuvvet_al(2,3)

# def bilgi_göster(name, surname, yas = "Girilmedi"): # Yas keyword arguemant diye geçer
#     return print(f"Ad: {name}, Soyad: {surname}, Yaş: {yas}")


# bilgi_göster("Ahmet", "Yılmaz")



def bilgi_göster2(name, surname = "Girilmedi", yas = "Girilmedi"): # Yas keyword arguemant diye geçer
    return print(f"Ad: {name}, Soyad: {surname}, Yaş: {yas}")

bilgi_göster2("Ahmet",yas = 34) # yanlış atamaması için parametre bilgisini vermemiz gerekir.

def topla2(a,b):
    return a + b

def topla3(a,b,c):
    return a + b + c

def topla4(*args): # *args kaç parametre verirsem vereyim çalışır 
    
    for ar in args:
        print(ar)
    

topla4(1,2,3,4, "Python", "Java", "C++")

def ortalama(*args):
    return print(sum(args) / len(args))


ortalama(1,2,3,4,5,6,7,8,9,10)


# ** args olursa parametreye değişken vermem gerekiyor. *args ise vermemelisin



def topla5(**kwargs):
    return print(kwargs)

topla5(a = 1, b = 2, c = 3, d = 4, e = "Python", f = "Java", g = "C++")
