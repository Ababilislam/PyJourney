from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    dept:str
    salary:int


jhon = Employee("jhon","computer", 1000)
print(jhon.dept)
print(jhon.salary)