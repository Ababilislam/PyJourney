# def my_generatoor(n):
#     value = 0
#
#     while value<n:
#         yield value
#
#         value+=1
#
#
# for value in my_generatoor(5):
#     print(value)

# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
# print(all_even())
#
# for i in all_even():
#     print(i)

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

da =[]
fb = fibonacci_numbers(10)
for i in fb:
    da.append(i**2)
print(da)
print(sum(da))
# sq =square(fb)
# print(list(fb))
# print(list(sq))
# print(sum(square(fibonacci_numbers(10))))