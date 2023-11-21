
class Celcius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_furenhite(self):
        return (self.temperature*1.8)+32

    #getter
    def get_temperature(self):
        print("getting value")
        return self._temperature

    #setter
    def set_temperature(self, value):
        print("setting vlaue")
        if value < -273.15:
            raise ValueError("temperature blew  negetive 273 is not possible")
        self._temperature = value


    temperature = property(get_temperature,set_temperature)


human =Celcius(37)

print(human.temperature)
print(human.to_furenhite())
human.temperature=-300
print(human.to_furenhite())
