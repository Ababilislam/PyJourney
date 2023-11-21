class add:
    def __init__(self,a,b):
        self.a = a
        self.b =b

        print("init run")

    def add(self):
        c =self.a+self.b
        print("inside add")
        print(c)
        return c

    def __str__(self):
        print("str run",self.a+self.b)


ad =add(2,3)
ad.add()
# ad.__str__()
# ad.__name__()
print(ad.__str__())