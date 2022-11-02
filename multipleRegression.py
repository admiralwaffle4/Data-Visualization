import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

class CM3:
    df = pd.read_csv("carsCM3.csv")

    X = df[['Weight', 'Volume']]
    y = df['CO2']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    def predict(self,weight,volume):
        self.weight = weight
        self.volume = volume
        prediction = self.regr.predict([[weight,volume]])
        return prediction

cm3 = CM3()
print(cm3.predict(2300,1300),cm3.predict(3300,1300))
print(cm3.regr.coef_)

class L:
    df = pd.read_csv("carsL.csv")

    X = df[['Weight','Volume']]
    y = df['CO2']

    scaledX = scale.fit_transform(X)

    regr = linear_model.LinearRegression()
    regr.fit(scaledX, y)

    scaled = scale.transform([[2300, 1.3]])

    def predict(self,weight,volume):
        self.weight = weight
        self.volume = volume
        scaledWV = scale.transform([[weight,volume]])
        prediction = self.regr.predict([scaledWV[0]])
        return prediction

L = L()
print(L.scaledX)
print(L.predict(2300,1.3))