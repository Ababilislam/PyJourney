import re

# pattern = 'a|b'
# test_string = "adeb"
# result = re.findall(pattern,test_string)
# print(result)
# if result:
#     print("search successfull")
# else:
#     print("search not successfull")

# GROUP/////////////////////////
# pattern = '(a|b|c)xy'
# test_string = "abxy"
# result = re.findall(pattern,test_string)
# print(result)
# if result:
#     print("search successfull")
# else:
#     print("search not successfull")

#***************back slash********** to escape special symbol

# pattern = '\$xy'
# test_string = "$xy"
# result = re.findall(pattern,test_string)
# print(result)
# if result:
#     print("search successfull")
# else:
#     print("search not successfull")

# special sequence  to check at start

# pattern = '\Athe'
# test_string = "the sun"
# result = re.match(pattern,test_string)
# print(result)
# if result:
#     print("search successfull")
# else:
#     print("search not successfull")

# #  digit////////////
pattern = '\d'
test_string = "12and3"
result = re.findall(pattern,test_string)
print(result)
if result:
    print("search successfull")
else:
    print("search not successfull")