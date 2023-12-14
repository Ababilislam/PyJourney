import re

pattern = 'a|b'
test_string = "adeb"
result = re.findall(pattern,test_string)
print(result)
if result:
    print("search successfull")
else:
    print("search not successfull")
