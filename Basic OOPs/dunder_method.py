class add:
    def __init__(self,a,b):
        self.a = a
        self.b =b

        print("init run")

    def __add__(self):
        c =self.a+self.b
        print("inside add")
        print(c)

    def __str__(self):
        print("str run",self.a+self.b)


ad =add(2,3)
ad.__add__()
# ad.__str__()