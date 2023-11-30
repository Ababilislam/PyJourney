# from urllib.parse import urlunparse
#
# lst = ["https",'example.com','/employees/names/',"","salsay>=2500",""]
# new_url = urlunparse(lst)
# print("url:",new_url)

from urllib.request import urlopen
obj = urlopen("https://www.tutorialspoint.com/static/images/simply-easy-learning.jpg")
data = obj.read()
img = open("img.jpg", "wb")
img.write(data)
img.close()