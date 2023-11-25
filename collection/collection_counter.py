from collections import Counter

print((Counter(['b','b','a','c','b','a','c'])))

print(Counter({'a':3,'b':2,'c':2}))

print(Counter(a=3,b=5,c=2))
#  we  can initilize a empty counter
count = Counter()
print(count)
# update counter
count.update([1,2,3,1,3])
print(count)