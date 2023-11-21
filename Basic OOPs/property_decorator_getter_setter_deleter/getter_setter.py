
class Celcius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_furenhite(self):
        return (self.temperature*1.8)+32

    @property
    def temperature(self):
        print("getting vlaue")
        return self._temperature


    @temperature.setter
    def temperature(self,value):
        print("setting value")
        if value<-273.15:
            raise ValueError("Temp is blew absulute zero. try with valid temperature.")
        self._temperature =value


human =Celcius(37)

print(human.temperature)
# print("boo")
# print(human.to_furenhite())
# # human.temperature=-300
# print(human.to_furenhite())
