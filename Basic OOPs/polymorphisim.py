import math


class Square:
    def __init__(self):
        pass

    def perimeter(self, data):
        self.data = data
        print(data * data)


class Triangel:
    def __init__(self):
        pass

    @classmethod
    def perimeter(self, data1, data2, data3):
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        print(data1 + data2 + data3)


class Circle:
    def __init__(self):
        pass

    @classmethod
    def perimeter(self, data):
        self.data = data
        print(2 * math.pi * data)


# perimetter of circle is
circle1 = Circle()
circle1.perimeter(2)

sqr = Square().perimeter(2)

tri = Triangel
tri.perimeter(2,3,3)
