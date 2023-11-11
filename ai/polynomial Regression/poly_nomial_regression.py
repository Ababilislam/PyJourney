import numpy
import matplotlib.pyplot as plt

"""The x-axis represents the hours of the day 
and the y-axis represents the speed:"""
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
"""line space take min value fo x and max vlaue of x, x represnt hour a car driving"""
myline = numpy.linspace(min(x), max(x), 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

"""testing is model is it fit 0 means not fit and 1 means fit"""
from sklearn.metrics import r2_score
relations_chance = r2_score(y, mymodel(x))
if relations_chance>.5:
    print("has a high realtionship")
    print(relations_chance)
else:
    print("low chance", relations_chance)




"""now testing at a specific time the change of passing a car"""

speed = mymodel(17)
print("the passing car speed:", speed)

