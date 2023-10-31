# def fectorial(n):
#     """ this is recursive function to
#      find the factorial of a number"""
#     if n == 1:
#         return 1
#     else:
#         return n * fectorial(n - 1)
#
# value =3
# print("factorial of {} is {}".format(value,fectorial(value)))


def num_table(n, i=1):
    if (i > 10):
        return

    print(n, "*", i, "=", n * i)

    return num_table(n, i + 1)


n = int(input("enter what numberring table you want to see: "))

num_table(n)

