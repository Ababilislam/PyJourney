class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("selling price is  {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice=price


computer1 = Computer()
computer1.sell()

computer1.__maxprice = 100
computer1.sell()

computer1.setMaxprice(100)
computer1.sell()