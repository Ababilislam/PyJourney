import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

maxsplit = 1
result = re.split(pattern, string)
# result = re.split(pattern, string,maxsplit)

print(result)

# result1 = re.search(pattern, string)
# print(result1)