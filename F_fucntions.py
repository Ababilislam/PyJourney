# def add_two_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum : ",sum)
#
#
# add_two_numbers(5,4)


# def find_square(num):
#     result = num*num
#     return result
#
# squire = find_square(3)
#
# print(squire)

def find_sum(*num):
    result = 0

    for x in num:
        result = result + x
    print("Sum = ", result)


find_sum(1, 2, 3)

find_sum(5, 10)
