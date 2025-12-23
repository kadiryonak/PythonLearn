# class ve instence kavramları

# attributes and methods


# class calisan:
#     pass

# calisan1 = calisan()


# calisan1.name = "Ahmet"
# calisan1.age = 25
# calisan1.gender = "Erkek"

# print(calisan1.name)


# calisan2 = calisan()

# calisan2.name = "Ayşe"
# calisan2.age = 22
# calisan2.gender = "Kadın"

# print(calisan2.name)

class calisan:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"{self.name} {self.surname} {self.age} {self.gender}")


calisan1 = calisan("Ahmet", "Yılmaz", 25, "Erkek")
#print(calisan1)

calisan2 = calisan("Ayşe", "Yılmaz", 22, "Kadın")
#print(calisan2.age,calisan2.name)


#calisan.show_info(calisan1)
print(calisan1 == calisan2) # False

#Output1:
# <__main__.calisan object at 0x000001A009D96CF0>
# <__main__.calisan object at 0x000001A00A004A50>
# Ahmet Yılmaz 25 Erkek
#Output2:
# <__main__.calisan object at 0x00000219DF686BA0>
# 22 Ayşe
# Ahmet Yılmaz 25 Erkek
# Problem şu contructor sürekli değişiyor. Çözüm singleton pattern kullanmak.



