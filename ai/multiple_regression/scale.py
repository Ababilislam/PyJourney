import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data.csv")

"""x independent variable y dependent variable"""

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regressor_model = linear_model.LinearRegression()
regressor_model.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regressor_model.predict([scaled[0]])
print(predictedCO2)
