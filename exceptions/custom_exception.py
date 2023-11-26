# class Custom_exception(Exception):
#     "raisese when the input value is less then 18"
#     pass
#
# num = 18
#
# try:
#     input_nam = int(input("enter the number: "))
#     if input_nam<num:
#         raise Custom_exception
#     else:
#         print("eligable to vote")
# except Custom_exception:
#     print("Exception occured : Invalid Age")

#=============salary not in range======
class Salary_not_in_range(Exception):

    def __init__(self,salary, message = "salary not in (5000,15000) range "):
        self.salary = salary
        self.message =message
        super().__init__(self.message)


salary = int(input("Enter the salary : "))
if not 5000 < salary <15000:
    raise Salary_not_in_range(salary)