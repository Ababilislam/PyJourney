from scipy import stats
import matplotlib.pyplot as plt

"""car speed over the year x=car age y = speed"""
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

"""this one to see not a good predictor"""
x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def speed_predictor(x):
    return slope * x + intercept


"""input vlaue in year in side of function"""
# future_car_speed = speed_predictor(10)


# print(future_car_speed)

"""this is to see this is not a very good predictor """
my_model = list(map(speed_predictor,x))

plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()

print(r)