

if __name__ == "__main__":

    if True:
        print("True")
    elif False:
        print("False")
    else:
        print("Ne yazık ki")


    a = 10
    b = 20

    if a > b:
        print("a b'den büyük")
    elif a == b:
        print("a b'ye eşit")
    else:
        print("a b'den küçük")


    if a == b or a > b:
        print("a b'den büyük veya eşit")
    else:
        print("a b'den küçük")  

    if a == b and a > b:
        print("a b'den büyük veya eşit")
    else:
        print("a b'den küçük")  

    liste = [1, 2, 3, 4, 5]

    a = 3

    if a in liste:
        print("3 liste içinde var")
    else:
        print("3 liste içinde yok")

    isim = "Python"

    k = "P"

    if k in isim:
        print("p isim içinde var")
    else:
        print("p isim içinde yok")