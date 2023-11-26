#
# try:
#     numerator =10
#     denominator = 0
#
#     result = numerator/denominator
#     print(result)
# except:
#     print("Error : denominator cannot be zero")

#  ----------multiple exception
# try:
#     even = [2,4,6,8]
#     print(even[5])
# except ZeroDivisionError:
#     print("Denominator cant be 0.")
# except IndexError:
#     print("Index out of bound.")


#-----------try else exception
#
# try:
#     num = int(input("enter a number: "))
#     assert num%2==0
# except:
#     print("not even number")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

#--------finally
try:
   num = int(input("enter a number: "))
   assert num%2==0
except:
    print("not even number")
finally:
    print("this is finally block what ever the code its always run")