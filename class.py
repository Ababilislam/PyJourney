class Dog:
    # kind = "canine"


    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("fidy")
e = Dog("buddy")

# print(d.kind)
# print(e.kind)
d.add_trick("roll_over")
e.add_trick("play_dead")

print(d.name)
print(e.name)
print(d.tricks)
print(e.tricks)
