import functools
"""max number from a list and their total"""
# list = [1,2,31,4,5,6]
#
# print("The sum of the list elements is :", end="")
# print(functools.reduce(lambda a,b :a+b,list))
#
# print("the maximum element of the list is :", end="")
# print(functools.reduce(lambda a,b: a if a>b else b,list))
#
# print(functools.reduce(lambda a,b : a if a>b else b, list))

import operator

list = [1,2,4,3,5,3]

print("the sum of the list element is :",end="")
print(functools.reduce(operator.add,list))

print("the product of the list elements is : ",end="")
print(functools.reduce(operator.mul,list))