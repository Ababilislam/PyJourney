import pandas as pd
from sklearn import linear_model
df = pd.read_csv("data.csv")

"""x indenpendent variable y dependent variable"""

X = df[['Weight', 'Volume']]
y = df["CO2"]

liner_regress_model = linear_model.LinearRegression()

liner_regress_model.fit(X,y)


"""predictor give value of weight and volume"""

pridector = liner_regress_model.predict([[3300,1300]])

print(pridector)
print(liner_regress_model.coef_)
