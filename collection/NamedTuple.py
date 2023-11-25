from collections import namedtuple

studnet = namedtuple('stuent',['name','age','DOB'])

s =studnet("ab",'25','511998')

print("the stuedent age of index is :",end="")
print(s[1])
print(
    f'the student name is {s.name}')

print(type(s))