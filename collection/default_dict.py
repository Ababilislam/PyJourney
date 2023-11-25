from collections import defaultdict

d = defaultdict(int)

l= [1,2,3,4,5,3,2,4,2,1]

# data loader in deafult dict valriable
for i in l:
    d[i]+=1

print(d)
d[2]=2
print(d)