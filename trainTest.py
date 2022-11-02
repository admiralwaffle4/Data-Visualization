import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

trainx = x[:80]
trainy = y[:80]

testx = x[80:]
testy = y[80:]

trainingModel = numpy.poly1d(numpy.polyfit(trainx, trainy, 4))

trainingLine = numpy.linspace(0, 6, 100)

rSquaredTr = r2_score(trainy, trainingModel(trainx))

testingModel = numpy.poly1d(numpy.polyfit(testx, testy, 4))

testingLine = numpy.linspace(0,6,100)

rSquaredTe = r2_score(testy,testingModel(testx))

print(rSquaredTr, rSquaredTe)
print(testingModel(5),testingModel(.2))