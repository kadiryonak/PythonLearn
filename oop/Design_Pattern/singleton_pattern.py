
class calisanbes:
    _instance = None   # class variable (tek nesne burada tutulur)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, surname, age, gender):
        # init her çağrılır, ama nesne aynıdır
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.gender}"
    
    @classmethod  # constructer dinamik olabilir statik metotta olmaz 
    def string_ile_olustur(cls, str_):
        name, surname, age, gender = str_.split(",")
        return cls(name, surname, age, gender)


        


calisan3 = calisanbes("Ahmet", "Yılmaz", 25, "Erkek")
calisan4 = calisanbes("Ayşe", "Yılmaz", 22, "Kadın")

#print(calisan3)
#print(calisan4)

print(calisan3 == calisan4) # True