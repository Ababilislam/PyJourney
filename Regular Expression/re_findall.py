import re

# pattern = '\d+'
# string = 'hello 12 hi 89. Howdy 34'
# result = re.findall(pattern, string)
# print(result)
# if result:
#     print("search successful")
# else:
#     print("search not successful")


string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)
