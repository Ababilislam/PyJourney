class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @salary.deleter
    def salary(self):
        del self._salary


emp1 = Employee("ashik", 25000)
print(emp1.name)
print(emp1.salary)
emp1.name = "ABABIL"
# print(emp1.__repr__())
print(emp1.name)
del emp1.name
print(emp1.name)
