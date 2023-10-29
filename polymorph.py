class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


# car1 = Car("Ford", "Mustang")  # Create a Car object
# boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
# plane1 = Plane("Boeing", "747")  # Create a Plane object

car = Car("ford", "sustang")
boat = Boat("ibz", "turing")
plane = Plane("Boaing","787")

for x in (car, boat, plane):
    print(x.brand, x.model)
    # print(x.model)
    # x.move()
