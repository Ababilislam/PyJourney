"""reverse the data with generator"""
# def reverse(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
#
# for char in reverse("spam"):
#     print(char)

"""sum of squire with generator"""

# sum_of_number= sum(i for i in range(10))
# print(sum_of_number)



page = "Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions."
unique_words = set(word for line in page  for word in line.split())
print(len(unique_words))

