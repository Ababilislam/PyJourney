import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

"""what if 90 percent"""

x = numpy.percentile(ages,90)
print(x)
"""  meaning that __% of the people are x(43) or younger."""