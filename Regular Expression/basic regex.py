import re

# pattern = '^a...s$'
# test_string = "abkls"
# pattern = 'a{2,3}'
# test_string = "aabc daaat"
pattern = '[0-9]{2,4}'
test_string = "12 and 345673	"
result = re.match(pattern,test_string)
print(result)
if result:
    print("search successfull")
else:
    print("search not successfull")
