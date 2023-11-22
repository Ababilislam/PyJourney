# file = open("tex.txt",'r')
#
# print(file.read())

# with open('tex.txt') as file:
#     data = file.read()
#
# print(data)
#

# file = open('tex.txt','r')
# print(file.read(20))
# li

# file = open('tex.txt','w')
# file.write("This is the write command")
# file.write("this allows us to write in a perticular file")
# file.close()
#
# fileopn = open('tex.txt','r')
# print(fileopn.readline())


# append mode

# with open('tex.txt','a') as file:
#     file.write("this will add this line\n and")
#     file.close()
#
# file = open('tex.txt','r')
# print(file.read())

# ######################
import os

# print(os.getcwd())

# os.chdir('/home/ab')
# print(os.getcwd())
# print(os.listdir())
# os.chdir("/home/ab/Downloads")
# print(os.listdir())

# os.mkdir("test")
# print(os.listdir())

# os.rename("test","new_test")
# os.remove("filename")
# os.rmdir("new_test")
# print(os.listdir())

# ##################### to remove empty directory us shutil
# import shutil
# shutil.rmtree("mydir")

# with open("tex.txt",'r') as f:
#     data = f.read()
#     print(
#         data
#     )
#

import os

# entry = os.listdir("/home/ab")
# for each_entry in entry:
#     print(each_entry)

# entry = os.scandir("/home/ab")
# for i in entry:
    # print(i.name)

# path = "/home/ab"
# for each_path in os.listdir(path):
#     if os.path.isdir(os.path.join(path,each_path)):
#         print(each_path)

from pathlib import Path
#
# path = Path("/home/ab")
# file_in_path = path.iterdir()
# # print(file_in_path)
# for item in file_in_path:
#     if item.is_file():
#         print(item.name)

##### to see when last file modified.

# from datetime import datetime
# from os import scandir
#
# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date
#
# def get_files():
#     dir_entries = scandir('/home/ab')
#     for entry in dir_entries:
#         if entry.is_file():
#             info = entry.stat()
#             print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
#
#
# print(get_files())

# for creating single dir

# os.mkdir("dir_name/")
# print(os.listdir())

# for multiple dir using os
# os.makedirs('2023/11/21')
# print(os.listdir())

for file_name in os.listdir(os.getcwd()):
    if file_name.endswith(".txt"):
        print(file_name)
