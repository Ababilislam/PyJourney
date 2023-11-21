class Celcius:
    def __init__(self, temperature=0):
        self.temperature =temperature


    def to_farenheit(self):
        return (self.temperature*1.8)+32

human1 = Celcius()
human1.temperature = 37

print(human1.temperature)
print(human1.to_farenheit())

print(human1.__dict__)