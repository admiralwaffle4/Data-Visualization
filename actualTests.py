import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from sklearn.metrics import r2_score
from sklearn import linear_model
import theCars, theCars2

#grab data
cars = theCars.Cars()
cars2 = theCars2.CarsTwo()
cars3 = theCars2.CarsThree()

'''#form r and the regression line
n = len(cars.name)+1
m, b, r, p, stErr = stats.linregress(cars.age,cars.speed)
print (m,b)
def estimate(x):
    return x*m+b
estValues = list(map(estimate,cars.age))

#plot our data and regression line
plt.scatter(cars.age,cars.speed)
plt.plot(cars.age,estValues)

#add words to graph for maroney's sake
plt.title("Age of Car vs Averge Speed")
plt.xlabel("Age")
plt.ylabel("Average Speed (mph)")

plt.show()'''

mymodel = np.poly1d(np.polyfit(cars2.time, cars2.speed, 3))

polyLine = np.linspace(1,22,100)

rSquared = r2_score(cars2.speed,mymodel(cars2.time))

test1 = mymodel(20)

plt.scatter(cars2.time,cars2.speed)
plt.plot(polyLine,mymodel(polyLine))
plt.plot(20,test1,'o')
plt.title("Polynomial Regression of Age vs Cars")
plt.suptitle(f"R-Squared={rSquared}")

plt.show()

regr = linear_model.LinearRegression()
regr.fit(cars3.X,cars3.y)

predictedCO2 = regr.predict([[2300, 1300]])
