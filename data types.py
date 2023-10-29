import time

# starting time
start = time.time()*1000

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# end time
end = time.time()*1000

# total time taken
print(f"Runtime of the program is {end - start}")