


def dis_fonksiyon():
    print("Dis fonksiyon")
    def ic_fonksiyon():
        print("Ic fonksiyon")
    print("dış fonksiyon sonlanıyor")
    return ic_fonksiyon()

dis_fonksiyon()



def hesaplama(a):
    def karakok():
        return a ** 0.5

    def kuvvet():
        return a ** 2

    def faktoriyel():
        return a * (a - 1)

    def mutlak():
        return abs(a)

    return (
        f"Karakok: {karakok()}, "
        f"Kuvvet: {kuvvet()}, "
        f"Faktoriyel: {faktoriyel()}, "
        f"Mutlak: {mutlak()}"
    )

print(hesaplama(5))
