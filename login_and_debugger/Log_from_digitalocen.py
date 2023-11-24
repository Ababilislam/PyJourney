import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format="name:- %(name)s :: level:- %(levelname)s :: message:- %("
                           "message)s :: %(asctime)s", datefmt='date:- %d-%m-%y '
                                                               'time:- %H:%M:%S')


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # print("Pizza created: {} (${})".format(self.name, self.price))
        logging.debug("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        # print("Made {} {} pizza(s)".format(quantity, self.name))
        logging.debug("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        # print("Ate {} pizza(s)".format(quantity))
        logging.debug("ate {} {} pizza(s)".format(quantity, self.name))


pizza_01 = Pizza("artichoke", 15)
pizza_01.make()
pizza_01.eat()

pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
pizza_02.eat()
