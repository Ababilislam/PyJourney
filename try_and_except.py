# try:
#     f = open("demp.txt")
#     try:
#         f.write("hello")
#     except:
#         print("some thing went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("some thing went wrong when opening a file")
#
#

x = -1

if x < 0:
    raise Exception("please enter number greater then 0")