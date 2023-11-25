from collections import OrderedDict

# print("this is a Dict:\n")
# d={}
# d['a']=1
#
# d['c']=3
# d['b']=2
# d['d']=4
#
# for key, value in d.items():
#     print(key, ":", value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 3
od['d'] = 4
od['c'] = 2
print("before deleting:")
for key, value in od.items():
    print(key, ":", value)

od.pop('a')

od['a']=1
print("after re-installationg:")
for key, value in od.items():
    print(key, ":", value)