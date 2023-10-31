# greet = lambda : print("hello world")
#
# greet()

# greet_user = lambda name : print("hey there,", name)
#
# greet_user("ab")

# x = lambda a:a+10
# print(x(5))

# div = lambda val : val+2
#
# print(div(5))



# vlaue = lambda n:n%3

# print(vlaue(29))

"""lambda using map"""
# num = [2,4,5,6,7,8]
# result = map(lambda x:x*x,num)
# print(list(result))


"""map and lambda using multiple iterator """

num1 = [1,3,5,6,4,2]
num2 = [2,5,3,2,5,2]

result = map(lambda n1,n2 : n1+n2, num1,num2)

print(sum(list(result)))