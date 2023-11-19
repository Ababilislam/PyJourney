class Aniaml:

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep")


class Dog(Aniaml):
    def bark(self):
        print("I can bark! woof woof!")


dog1 = Dog()
dog1.eat()
dog1.bark()
