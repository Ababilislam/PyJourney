from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# a class method useing cls
    @classmethod
    def ageFromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

    # static method to check age
    @staticmethod
    def isAdult(age):
        return age>18


p1 = Person("ab", 21)
p2 = Person.ageFromBirthYear("udoy", 1998)

print(p1.age)
print(p2.age)

print(p2.isAdult())