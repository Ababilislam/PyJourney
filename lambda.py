# x = lambda a:a+10
# print(x(5))
#
# x = lambda b:b*5
#
# print(x(5))
#
# x = lambda a, b : b*a
# print(x(5,2))

def my_func(n):
    return lambda a:a*n

mydouble = my_func(2)

print(mydouble(11))