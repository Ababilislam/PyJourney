# import json
# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])

""" dictornary to json"""

import json

x = {
    "name": "ab",
    "age": 30,
    "city": "new york"
}

y = json.dumps(x)
print(y)
