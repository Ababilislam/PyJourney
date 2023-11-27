from abc import ABC, abstractmethod
import datetime
from datetime import date

class Person(ABC):
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob

    def age(self):
        """abstruct methode"""
        pass

class Student(Person):
    def __init__(self,name,dob):
        super().__init__(name,dob)

    def age(self):
        today = datetime.date.today()
        # age = today -self.dob.year -((today.month,today.day)<(self.dob.month,self.dob.day))
        print("age")

s1 = Student("ab",date(2000,2,3))
s1.age()

print(datetime.date.today())