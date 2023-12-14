import re

pattern = '^a...s$'
test_string = "abkls"
result = re.match(pattern,test_string)
if result:
    print("search successfull")
else:
    print("search not successfull")
