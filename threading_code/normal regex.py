# import re
#
# pattern = '^a...s$'
# test_string = 'abyxs'
# result = re.match(pattern, test_string)
#
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)