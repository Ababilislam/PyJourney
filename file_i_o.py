# file = open("demofile.txt","r")
#
# for data in file:
#     print(data)
#
# file.close()

# file = open("demofile.txt","a")
#
# file.write("now file has new content by write")
#
# file.close()

# f = open("demofile.txt","r")
# print(f.read())

f = open("demofile.txt", "w")
f.write("woops! I have deleted the content!")
f.close()
# f = open("demofile.txt","r")
# print(f.read())

"""creating a file with x or w """
# f = open("demofile.txt","w")
# f.write("I have added the content!")
# f.close()
""" deleting a file with proper message"""

import os

# os.remove("demofile.txt")
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
#     print("file remove successfully")
# else:
#     print("file does not exists")

""" remove directory of """
# if os.path.exists("myfolder"):
#     os.rmdir("myfolder")
#     print("folder removee succesfully")
# else: print("folder does not exists")

