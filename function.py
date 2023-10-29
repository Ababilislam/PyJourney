# def my_function(fname, lname):
#     print(fname+" "+lname)
#
# # my_function("ab","udoy")
#
# # my_function("ab")
# # my_function("ab","udoy","thd")

# def my_function(*kids):
#     print("the youndgest kids is "+ kids[1])
#
# my_function("email", "toby","linus")


# def my_function(**kids):
#     print("his last name is "+ kids["lname"])
#
# my_function(fname = "tobi", lname="ab")

# def my_func(country = "Bagladesh"):
#     print("i am from "+country)
#
# my_func("Japan")
# my_func()

# def my_func(food):
#     for x in food:
#         print(x)
#
# fruits = ["apple","bannan","chery"]
#
# my_func(fruits)

# def my_func(x):
#     return 5*x
#
# print(my_func(5))
# print(my_func(3))

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(4))