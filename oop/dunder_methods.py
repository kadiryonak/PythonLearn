print(3+5) # arkada gerçekleşen aslında alttaki

print(int.__add__(3,5))

# İfadeler aynı 



class MyClass:
    pass

obj = MyClass()


# Sınıfın dunder methodlarını yazdırır
print(dir(obj))

print("\n\n\n")
print(dir(int))
print("\n\n\n")
print(dir(list))
print("\n\n\n")
print(dir(str))


class MyList(list):
    # Kendi add fonksiyonumu yazmış oldum
    def __add__(self, other):
        if len(self) != len(other):
            return print("Listelerin uzunlukları aynı olmalıdır.")
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i] + other[i])
            return result

    def __sub__(self, other):
        if len(self) != len(other):
            return print("Listelerin uzunlukları aynı olmalıdır.")
        else:
            return MyList([self[i] - other[i] for i in range(len(self))])
    def __eq__(self, other):
        if len(self) != len(other):
            return print("Listelerin uzunlukları aynı olmalıdır.")
        else:

            for i in range(len(self)):
                if self[i] == other[i]:
                    return True
                else:
                    return False
    def __abs__(self):
        result = MyList()
        for i in self:
            if i in self:
                result.append(i)
            else:
                result.append(-i)
        return result


listee = MyList([1, 2, 3, 4])
listee2 = MyList([5, -6, 7, -8])

print(listee + listee2)
print(listee - listee2)
print(listee == listee2)

lis1 = [1,2,3,4]
lis2 = [5,6,7,8]

print(lis1 + lis2)


print(abs(listee2))