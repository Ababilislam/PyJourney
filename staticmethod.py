# class Maths():
#
#     @staticmethod
#     def AddNum(num1, num2):
#         return num1 + num2
#
#
# res = Maths.AddNum(1, 2)
# print("the result is : ", res)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        return age >= 18

result = Person.isAdult(12)
print("is person adult:", result)

result = Person.isAdult(22)
print("\n Is person adult:",result)
