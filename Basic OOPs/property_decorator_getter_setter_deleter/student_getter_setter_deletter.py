class Student:
    def __init__(self, f_name, l_name, age=0):
        self._first_name = f_name
        self._last_name = l_name
        self._age = age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, f_name):
        self._first_name = f_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, lname):
        self._last_name = lname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @first_name.deleter
    def first_name(self):
        del self._first_name, self._last_name, self._age

    @last_name.deleter
    def last_name(self):
        del self._last_name, self._age

    @age.deleter
    def age(self):
        del self._age

    # property info
    def information(self):
        print("student name is {} {} and {} years old ".format(self._first_name, self._last_name, self._age))
        # return (self._first_name, self._last_name, self._age)


stu = Student("ab", "udoy", 25)
stu.first_name
print(stu.first_name)
# stu.first_name ="ABABIL"
# print(stu.first_name)
# stu.last_name = "Islam"
# stu.information
#
# del stu.age
# stu.information
