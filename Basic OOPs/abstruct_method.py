from abc import ABC, abstractmethod


class ploygon():

    @abstractmethod
    def sides(self):
        pass


class Triangel(ploygon):
    def sides(self):
        print("no of sides is 3")


class pentagon(ploygon):
    def sides(self):
        print("no of sides is 5")


class hexagon(ploygon):
    def sides(self):
        print("no of side is 6")


t = Triangel()
t.sides()
s = pentagon()
s.sides()
h = hexagon()
h.sides()
