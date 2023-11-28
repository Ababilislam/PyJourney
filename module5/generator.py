# def first_n(n):
#     """Build and return a list"""
#     num,nums = 0,[]
#     while num<n:
#         nums.append(num)
#         num +=1
#     return nums
#
#
# sum_of_first_n = sum(first_n(1000000000))
# print(sum_of_first_n)
# this is regular pattern and it will take a lot of space
# thus we resort to generator pattern

# class first_n(object):
#
#     def __init__(self,n):
#         self.n =n
#         self.num =0
#
#     def __iter__(self):
#         return self
#
#     # python 3 compitable next
#     def __next__(self):
#         return self.next()
#
#     def next(self):
#         if self.num <self.n:
#             cur, self.num = self.num, self.num+1
#             return cur
#         raise StopIteration()


# sum_of_first_n = sum(first_n(1000000))
# print(sum_of_first_n)

# rewrite the iterator using generator to minimize the code cost.

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(first_n(100))
print(sum_of_first_n)
